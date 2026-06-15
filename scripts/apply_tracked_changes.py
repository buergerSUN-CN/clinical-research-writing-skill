#!/usr/bin/env python3
"""
apply_tracked_changes.py — apply a list of edits to an UNPACKED .docx as real Word
tracked changes (w:ins / w:del) plus margin comments, for the clinical-research-writing
skill's Mode C "tracked-changes manuscript" output.

Pipeline (see SKILL.md Mode C):
  1. python <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/
  2. python apply_tracked_changes.py unpacked/ edits.json [--author NAME] [--date ISO]
  3. python <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx

edits.json is a list of edit objects. Each `find` is matched against the decoded text of
ONE paragraph (the first paragraph that contains it and has not yet been consumed):

  {"type": "replace",      "find": "...", "replace": "...", "comment": "optional note"}
  {"type": "insert_after", "find": "...", "insert": "...",  "comment": "optional note"}
  {"type": "comment",      "find": "...", "comment": "required note"}   # anchors a comment, no text change

Rules baked in for the skill's "never fabricate" floor:
  - `replace`/`insert_after` carry the author's wording; use [brackets] in `replace`/`insert`
    for any number not present in the source — the script inserts the bracket literally.
  - For data the author must supply (event rates, CIs, blinded-read details), use `comment`,
    not a fabricated insertion.

The script preserves each matched run's run-properties (rPr) — bold, superscript, font,
size — on kept-anchor and deleted text, so display formatting survives and rejecting a
change restores the source exactly. (New inserted text carries the span's dominant format,
which is why the SKILL's edit-mechanics rule keeps superscript citations out of replace spans.)
"""
import argparse, json, os, sys, copy
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
Wq = "{%s}" % W
NS = {"w": W}
CT = "http://schemas.openxmlformats.org/package/2006/content-types"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"


def q(tag):
    return Wq + tag


class SkipEdit(Exception):
    """Raised when an edit's span would damage a field / cross-reference / hyperlink."""


def run_text(r):
    """Concatenated text of a run's <w:t> children (None-safe)."""
    return "".join((t.text or "") for t in r.findall(q("t")))


# Characters that commonly differ between a pandoc-extracted `find` and the docx text
# but should match. All replacements are 1-char->1-char so text offsets are preserved.
_MATCH_MAP = {"\xa0": " ", " ": " ", "‘": "'", "’": "'",
              "“": '"', "”": '"', "–": "-", "—": "-"}


def norm_match(s):
    for a, b in _MATCH_MAP.items():
        s = s.replace(a, b)
    return s


def make_run(rpr, text, deleted=False):
    r = etree.Element(q("r"))
    if rpr is not None:
        r.append(copy.deepcopy(rpr))
    t = etree.SubElement(r, q("delText") if deleted else q("t"))
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    return r


def wrap_ins_del(tag, wid, author, date, runs):
    el = etree.Element(q(tag))
    el.set(q("id"), str(wid))
    el.set(q("author"), author)
    el.set(q("date"), date)
    for r in (runs if isinstance(runs, list) else [runs]):
        el.append(r)
    return el


def frags_to_runs(frags, deleted=False):
    """Materialize (rPr, text) fragments into runs, preserving each fragment's own format."""
    return [make_run(rpr, text, deleted=deleted) for rpr, text in frags]


def locate(paras, find):
    """Return (para, runs, start_idx, end_idx) for the first paragraph whose direct-child
    runs contain find. Direct-child runs only, so text already inside <w:ins>/<w:del> tracked
    changes is skipped — allowing several non-overlapping edits in the same paragraph."""
    fn = norm_match(find)
    for p in paras:
        runs = p.findall(q("r"))
        full = "".join(run_text(r) for r in runs)
        idx = norm_match(full).find(fn)  # 1:1 normalization keeps offsets valid
        if idx >= 0:
            return p, runs, idx, idx + len(fn)
    return None


def split_runs(p, runs, start, end):
    """
    Rebuild paragraph runs so the [start,end) span is isolated.
    Returns (insert_index, prefix_run_or_None, span_frags, dom_rpr_or_None, suffix_run_or_None).
    span_frags is a list of (rPr_or_None, text) reproducing the matched span with each original
    run's own formatting preserved — so superscript citations / bold labels survive in kept-anchor
    and deleted text, and rejecting a change restores the source exactly. dom_rpr is the dominant
    run's rPr, used only for genuinely-new inserted text.
    """
    # cumulative offsets per run
    offs = []
    pos = 0
    for r in runs:
        tlen = len(run_text(r))
        offs.append((pos, pos + tlen, r))
        pos += tlen
    # find start/end runs
    sidx = next(i for i, (a, b, _) in enumerate(offs) if a <= start < b or (a == b == start))
    # end-1 belongs to the run containing the last char
    eidx = next(i for i, (a, b, _) in enumerate(offs) if a < end <= b)
    # Refuse spans that cross a field / cross-reference (fldChar/instrText): rewriting their
    # runs would corrupt the field. Such edits are skipped and reported, never force-applied.
    for _, _, r in offs[sidx : eidx + 1]:
        if r.find(q("fldChar")) is not None or r.find(q("instrText")) is not None:
            raise SkipEdit("span crosses a field / cross-reference")
    # Slice the matched span into per-run fragments, keeping each run's own rPr.
    span_frags = []
    for a, b, r in offs[sidx : eidx + 1]:
        rpr = r.find(q("rPr"))
        piece = run_text(r)[max(start, a) - a : min(end, b) - a]
        if piece:
            span_frags.append((copy.deepcopy(rpr) if rpr is not None else None, piece))
    start_a, _, start_run = offs[sidx]
    end_a, _, end_run = offs[eidx]
    start_rpr = start_run.find(q("rPr"))
    end_rpr = end_run.find(q("rPr"))
    prefix = run_text(start_run)[: start - start_a]
    suffix = run_text(end_run)[end - end_a :]
    first_run_index = list(p).index(start_run)
    prefix_run = make_run(start_rpr, prefix) if prefix else None
    suffix_run = make_run(end_rpr, suffix) if suffix else None
    # dominant rPr = rPr of the in-span run holding the most text, so an inserted replacement
    # matches the body formatting rather than a short leading label (e.g. a bold "Figure 1.").
    dom = max(offs[sidx : eidx + 1], key=lambda o: len(run_text(o[2])))[2]
    dom_rpr = dom.find(q("rPr"))
    # remove the original run span
    for r in runs[sidx : eidx + 1]:
        p.remove(r)
    return first_run_index, prefix_run, span_frags, copy.deepcopy(dom_rpr) if dom_rpr is not None else None, suffix_run


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("unpacked")
    ap.add_argument("edits")
    ap.add_argument("--author", default="Claude")
    ap.add_argument("--date", default="2026-06-15T00:00:00Z")
    args = ap.parse_args()

    doc_path = os.path.join(args.unpacked, "word", "document.xml")
    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.parse(doc_path, parser)
    root = tree.getroot()
    paras = root.iter(q("p"))
    paras = list(root.iter(q("p")))

    edits = json.load(open(args.edits, encoding="utf-8"))
    wid = 90000
    comments = []  # (cid, text)
    applied, missed = [], []

    for e in edits:
        find = e["find"]
        loc = locate(paras, find)
        if not loc:
            missed.append(e)
            continue
        p, runs, s, end = loc
        # exact ORIGINAL matched text (real chars, e.g. nbsp) — used only for the auto-space check.
        orig = "".join(run_text(r) for r in runs)[s:end]
        try:
            ins_at, prefix_run, span_frags, dom_rpr, suffix_run = split_runs(p, runs, s, end)
        except SkipEdit as ex:
            missed.append({**e, "_reason": str(ex)})
            continue
        nodes = []
        if prefix_run is not None:
            nodes.append(prefix_run)
        cid = None
        if e.get("comment"):
            cid = len(comments)
            comments.append((cid, e["comment"]))
            crs = etree.Element(q("commentRangeStart")); crs.set(q("id"), str(cid))
            nodes.append(crs)
        etype = e["type"]
        if etype == "replace":
            wid += 1
            # delete the original span preserving its per-run formatting (so reject restores it)
            nodes.append(wrap_ins_del("del", wid, args.author, args.date, frags_to_runs(span_frags, deleted=True)))
            if e.get("replace"):
                wid += 1
                # new text carries the dominant run format (citations etc. can't be inferred — the
                # SKILL's edit-mechanics rule keeps specially-formatted runs out of replace spans)
                nodes.append(wrap_ins_del("ins", wid, args.author, args.date, make_run(dom_rpr, e["replace"])))
        elif etype == "insert_after":
            nodes.extend(frags_to_runs(span_frags))  # keep anchor with original formatting
            wid += 1
            ins_text = e["insert"]
            # avoid gluing the inserted text to the anchor (e.g. right after a citation
            # superscript like "30-31These ..."): add a separating space when needed.
            if orig and not orig[-1].isspace() and ins_text and ins_text[0] not in " \n(":
                ins_text = " " + ins_text
            nodes.append(wrap_ins_del("ins", wid, args.author, args.date, make_run(dom_rpr, ins_text)))
        elif etype == "comment":
            nodes.extend(frags_to_runs(span_frags))  # keep anchor with original formatting
        else:
            missed.append(e); continue
        if cid is not None:
            cre = etree.Element(q("commentRangeEnd")); cre.set(q("id"), str(cid))
            nodes.append(cre)
            refr = etree.Element(q("r"))
            rpr_ref = etree.SubElement(refr, q("rPr"))
            rstyle = etree.SubElement(rpr_ref, q("rStyle")); rstyle.set(q("val"), "CommentReference")
            cref = etree.SubElement(refr, q("commentReference")); cref.set(q("id"), str(cid))
            nodes.append(refr)
        if suffix_run is not None:
            nodes.append(suffix_run)
        for off, node in enumerate(nodes):
            p.insert(ins_at + off, node)
        applied.append(e)

    tree.write(doc_path, xml_declaration=True, encoding="UTF-8", standalone=True)

    if comments:
        write_comments(args.unpacked, comments, args.author, args.date)

    print(f"applied={len(applied)} missed={len(missed)} comments={len(comments)}")
    for m in missed:
        reason = m.get('_reason', 'find not located')
        print(f"  MISSED [{reason}]:", (m.get('find', '')[:70]))


def write_comments(unpacked, comments, author, date):
    cpath = os.path.join(unpacked, "word", "comments.xml")
    if os.path.exists(cpath):
        ctree = etree.parse(cpath); croot = ctree.getroot()
    else:
        croot = etree.Element(q("comments"), nsmap={"w": W})
        ctree = etree.ElementTree(croot)
    initials = "".join(w[0] for w in author.split()[:2]).upper() or "C"
    for cid, text in comments:
        c = etree.SubElement(croot, q("comment"))
        c.set(q("id"), str(cid)); c.set(q("author"), author)
        c.set(q("date"), date); c.set(q("initials"), initials)
        ppar = etree.SubElement(c, q("p"))
        r = etree.SubElement(ppar, q("r"))
        t = etree.SubElement(r, q("t")); t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        t.text = text
    ctree.write(cpath, xml_declaration=True, encoding="UTF-8", standalone=True)

    # relationship
    rels_path = os.path.join(unpacked, "word", "_rels", "document.xml.rels")
    rtree = etree.parse(rels_path); rroot = rtree.getroot()
    has = any(r.get("Type", "").endswith("/comments") for r in rroot)
    if not has:
        ids = [r.get("Id", "") for r in rroot]
        n = 1
        while f"rId{n}" in ids:
            n += 1
        rel = etree.SubElement(rroot, "{%s}Relationship" % REL)
        rel.set("Id", f"rId{n}")
        rel.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments")
        rel.set("Target", "comments.xml")
        rtree.write(rels_path, xml_declaration=True, encoding="UTF-8", standalone=True)

    # content type
    ct_path = os.path.join(unpacked, "[Content_Types].xml")
    cttree = etree.parse(ct_path); ctroot = cttree.getroot()
    part = "/word/comments.xml"
    has_ct = any(o.get("PartName") == part for o in ctroot)
    if not has_ct:
        ov = etree.SubElement(ctroot, "{%s}Override" % CT)
        ov.set("PartName", part)
        ov.set("ContentType", "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml")
        cttree.write(ct_path, xml_declaration=True, encoding="UTF-8", standalone=True)


if __name__ == "__main__":
    main()
