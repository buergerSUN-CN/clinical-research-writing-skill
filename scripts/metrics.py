#!/usr/bin/env python3
"""Quantitative voice fingerprint for the clinical-writing corpus.

Pure, reproducible, no LLM. Computes per-paper metrics + per-genre distributions
(median + IQR) that capture the traits an AI writer flattens: sentence-length
BURSTINESS (non-uniform rhythm), SECTION-WISE hedge density (Results~0 vs
Discussion high), connective spectrum, opener habits, absolute-rate-first
frequency, passive:active by section, statistic density, punctuation ratios.

Usage:
    python3 metrics.py                # all papers in _corpus/, group by _meta genre
Outputs:
    _metrics/paperNN.json             # per paper
    _metrics/genre_{A,B,C}.json       # per-genre median/IQR
    _metrics/fingerprint_summary.md   # human-readable draft (feeds voice_fingerprint.md)
"""
from __future__ import annotations

import json
import re
import statistics as st
from pathlib import Path

WS = Path("/Volumes/工作数据/claude-projects/AIS_clinical/_skill_build/redistill")
CORPUS, META, METRICS = WS / "_corpus", WS / "_meta", WS / "_metrics"

# ---------------------------------------------------------------- lexicons
HEDGES = ["may", "might", "could", "appear", "appears", "appeared", "suggest", "suggests",
          "suggested", "likely", "possibly", "possible", "potential", "potentially", "perhaps",
          "seem", "seems", "seemed", "relatively", "somewhat", "tend to", "tended to", "presumably"]
CONNECTIVES = ["however", "therefore", "thus", "moreover", "furthermore", "additionally",
               "in addition", "notably", "importantly", "consequently", "hence", "nevertheless",
               "nonetheless", "by contrast", "in contrast", "whereas", "although", "meanwhile"]
SUBORDINATORS = ["although", "though", "while", "whereas", "because", "since", "despite", "given that"]
STAT_TOKENS = [r"\bOR\b", r"\bHR\b", r"\bRR\b", r"95%\s*CI", r"\bCI\b", r"\bP\s*[<=>]",
               r"\bp\s*[<=>]", r"\bκ\b", r"kappa", r"\bICC\b", r"\bAUC\b", r"±", r"\bn\s*="]
SECTION_KEYS = {
    "abstract": r"\babstract\b",
    "introduction": r"\bintroduction\b|\bbackground\b",
    "methods": r"\bmaterials?\s+and\s+methods\b|\bpatients?\s+and\s+methods\b|\bmethods\b",
    "results": r"\bresults\b",
    "discussion": r"\bdiscussion\b",
    "conclusion": r"\bconclusions?\b",
}
ABBR = {"vs", "no", "fig", "eg", "ie", "dr", "mr", "ms", "st", "al", "cf", "approx", "ca",
        "mm", "ml", "kg", "mg", "ref", "figs", "e.g", "i.e", "et", "inc", "ltd", "co"}

WORD = re.compile(r"\b[\w'-]+\b")


def words(t): return WORD.findall(t)


def split_sentences(text):
    """Lightweight sentence splitter tolerant of abbreviations/decimals/CIs."""
    text = re.sub(r"\s+", " ", text).strip()
    n = len(text)
    sents, start = [], 0
    for m in re.finditer(r"[.!?]+", text):
        end = m.end()                      # index just past the punctuation run
        j = end
        while j < n and text[j] == " ":
            j += 1
        if j >= n:
            break
        nxt = text[j]
        if not (nxt.isupper() or nxt.isdigit() or nxt in "\"'(“‘["):
            continue                       # not a real sentence start
        prevtok = re.findall(r"[A-Za-z0-9.]+$", text[start:m.start()])
        pw = prevtok[-1].lower().rstrip(".") if prevtok else ""
        if pw in ABBR or (len(pw) == 1 and pw.isalpha()):
            continue                       # abbreviation / initial
        if m.group()[0] == "." and m.start() > 0 and text[m.start() - 1].isdigit() and nxt.isdigit():
            continue                       # decimal like 12.5
        sents.append(text[start:end].strip())
        start = end
    if start < n:
        sents.append(text[start:].strip())
    return [s for s in sents if len(words(s)) >= 2]


def strip_back_matter(text):
    """Cut references/acknowledgements/disclosures onward — they poison prose metrics."""
    low = text.lower()
    cuts = []
    for pat in (r"\n\s*references\s*\n", r"\breferences\b\s*\n", r"\n\s*r\s*e\s*f\s*e\s*r\s*e\s*n\s*c\s*e\s*s",
                r"\backnowledge?ments?\b", r"\bconflicts?\s+of\s+interest\b", r"\bdisclosures?\b\s*\n"):
        m = re.search(pat, low)
        if m and m.start() > len(text) * 0.5:
            cuts.append(m.start())
    return text[:min(cuts)] if cuts else text


HEADER_LINE = {
    "introduction": re.compile(r"^\s*(\d+\s*[.|]?\s*)?(introduction|background)\s*$", re.I),
    "methods": re.compile(r"^\s*(\d+\s*[.|]?\s*)?(materials?\s+and\s+methods|patients?\s+and\s+methods|methods)\s*$", re.I),
    "results": re.compile(r"^\s*(\d+\s*[.|]?\s*)?results\s*$", re.I),
    "discussion": re.compile(r"^\s*(\d+\s*[.|]?\s*)?discussion\s*$", re.I),
    "conclusion": re.compile(r"^\s*(\d+\s*[.|]?\s*)?conclusions?\s*$", re.I),
}


def find_sections(text):
    """IMRaD partition via header LINES (own-line 'RESULTS' / '3 | Results').

    Takes the LAST header line for each section so structured-abstract labels
    (which precede the body) are overridden by the real body header. Returns
    {section: text} + 'all' (body from first header, refs stripped) + 'raw'.
    """
    body = strip_back_matter(text)
    lines = body.split("\n")
    offsets, pos = [], 0
    for ln in lines:
        offsets.append(pos)
        pos += len(ln) + 1
    picked = {}
    for i, ln in enumerate(lines):
        for sec, rgx in HEADER_LINE.items():
            if rgx.match(ln):
                picked[sec] = offsets[i]      # keep last occurrence
    if not picked:
        return {"all": body, "raw": text}
    items = sorted(picked.items(), key=lambda kv: kv[1])
    secs = {}
    for idx, (sec, p) in enumerate(items):
        end = items[idx + 1][1] if idx + 1 < len(items) else len(body)
        secs[sec] = body[p:end]
    secs["all"] = body[items[0][1]:]
    secs["raw"] = text
    return secs


def per1000(count, wc): return round(1000 * count / wc, 2) if wc else 0.0


def hedge_density(t):
    wc = len(words(t))
    c = sum(len(re.findall(r"\b" + re.escape(h) + r"\b", t, re.I)) for h in HEDGES)
    return per1000(c, wc)


def passive_ratio(sents):
    if not sents:
        return None
    pat = re.compile(r"\b(was|were|been|being|is|are|be)\b\s+(\w+ed|shown|done|made|seen|found|given|taken|written|drawn|built|held|known|performed|assessed|analyzed|analysed|measured|obtained|defined|calculated|considered|included|excluded|recorded|reported)\b", re.I)
    p = sum(1 for s in sents if pat.search(s))
    return round(p / len(sents), 3)


def abs_rate_first(results_text):
    """Fraction of Results 'sentences' that lead with an absolute rate n/N or n of N (x%)."""
    sents = split_sentences(results_text)
    if not sents:
        return None, 0
    lead = re.compile(r"^\W*(of\s+the\s+\d|a\s+total\s+of\s+\d|\d[\d,]*\s*/\s*\d|\d[\d,]*\s+of\s+\d|\d[\d,]*\s+\(\d+\.?\d*\s*%\))", re.I)
    anyrate = re.compile(r"\d[\d,]*\s*/\s*\d[\d,]*|\d[\d,]*\s+of\s+\d[\d,]*|\d[\d,]*\s+\(\d+\.?\d*\s*%\)")
    lead_n = sum(1 for s in sents if lead.match(s))
    rate_occ = len(anyrate.findall(results_text))
    return round(lead_n / len(sents), 3), rate_occ


def sentence_stats(sents):
    lens = [len(words(s)) for s in sents]
    if not lens:
        return {}
    masd = st.mean(abs(lens[i] - lens[i - 1]) for i in range(1, len(lens))) if len(lens) > 1 else 0
    return {
        "n_sentences": len(lens),
        "mean_len": round(st.mean(lens), 1),
        "median_len": st.median(lens),
        "sd_len": round(st.pstdev(lens), 1),
        "burstiness_masd": round(masd, 1),            # mean abs successive diff — human rhythm
        "pct_short_le15": round(100 * sum(l <= 15 for l in lens) / len(lens), 1),
        "pct_long_ge40": round(100 * sum(l >= 40 for l in lens) / len(lens), 1),
    }


def connective_spectrum(t):
    wc = len(words(t))
    return {c: per1000(len(re.findall(r"\b" + re.escape(c) + r"\b", t, re.I)), wc) for c in CONNECTIVES}


def stat_density(t):
    wc = len(words(t))
    c = sum(len(re.findall(p, t)) for p in STAT_TOKENS)
    return round(100 * c / wc, 2) if wc else 0.0  # per 100 words


def punct(t):
    wc = len(words(t))
    # true em-dash (parenthetical), NOT en-dash numeric ranges like 1.75–3.43
    emdash = t.count("—") + len(re.findall(r"\s--\s", t))
    endash_ranges = len(re.findall(r"\d\s*–\s*\d", t))
    return {
        "emdash_per1000": per1000(emdash, wc),
        "endash_range_per1000": per1000(endash_ranges, wc),
        "paren_per1000": per1000(len(re.findall(r"\([^)]{1,80}\)", t)), wc),
        "semicolon_per1000": per1000(t.count(";"), wc),
    }


def subordinator_opener_pct(sents):
    if not sents:
        return None
    c = sum(1 for s in sents if any(re.match(r"\W*" + re.escape(w) + r"\b", s, re.I) for w in SUBORDINATORS))
    return round(100 * c / len(sents), 1)


def analyze(pid, text, genre):
    secs = find_sections(text)
    all_sents = split_sentences(secs.get("all", text))
    res = {"id": pid, "genre": genre, "n_words": len(words(text))}
    res["sentence"] = sentence_stats(all_sents)
    res["subordinator_opener_pct"] = subordinator_opener_pct(all_sents)
    res["hedge_per1000"] = {sec: hedge_density(secs[sec]) for sec in ("introduction", "results", "discussion") if sec in secs}
    res["hedge_per1000"]["all"] = hedge_density(secs.get("all", text))
    res["passive_ratio"] = {sec: passive_ratio(split_sentences(secs[sec])) for sec in ("methods", "results", "discussion") if sec in secs}
    if "results" in secs:
        arf, occ = abs_rate_first(secs["results"])
        res["results_abs_rate_lead_frac"], res["results_rate_occurrences"] = arf, occ
    res["stat_density_per100"] = {sec: stat_density(secs[sec]) for sec in ("results", "discussion") if sec in secs}
    res["connectives_per1000"] = connective_spectrum(secs.get("all", text))
    res["punct"] = punct(secs.get("all", text))
    res["sections_found"] = [s for s in ("introduction", "methods", "results", "discussion", "conclusion") if s in secs]
    return res


def genre_of(pid, fallback="?"):
    mf = META / f"{pid}.json"
    if mf.exists():
        try:
            return json.loads(mf.read_text()).get("genre", fallback)
        except Exception:
            pass
    return fallback


def iqr(vals):
    vals = [v for v in vals if isinstance(v, (int, float))]
    if not vals:
        return None
    vals.sort()
    q1 = st.median(vals[:len(vals) // 2]) if len(vals) > 1 else vals[0]
    q3 = st.median(vals[(len(vals) + 1) // 2:]) if len(vals) > 1 else vals[0]
    return {"median": round(st.median(vals), 2), "q1": round(q1, 2), "q3": round(q3, 2), "n": len(vals)}


def dig(d, path):
    for k in path:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def aggregate(per_paper):
    genres = {}
    for g in ("A", "B", "C"):
        papers = [p for p in per_paper if p["genre"] == g]
        if not papers:
            continue
        agg = {"genre": g, "n_papers": len(papers), "ids": [p["id"] for p in papers]}
        paths = {
            "sentence.mean_len": ["sentence", "mean_len"],
            "sentence.sd_len": ["sentence", "sd_len"],
            "sentence.burstiness_masd": ["sentence", "burstiness_masd"],
            "sentence.pct_short_le15": ["sentence", "pct_short_le15"],
            "sentence.pct_long_ge40": ["sentence", "pct_long_ge40"],
            "subordinator_opener_pct": ["subordinator_opener_pct"],
            "hedge.results": ["hedge_per1000", "results"],
            "hedge.discussion": ["hedge_per1000", "discussion"],
            "hedge.all": ["hedge_per1000", "all"],
            "passive.methods": ["passive_ratio", "methods"],
            "passive.results": ["passive_ratio", "results"],
            "passive.discussion": ["passive_ratio", "discussion"],
            "results_abs_rate_lead_frac": ["results_abs_rate_lead_frac"],
            "stat.results": ["stat_density_per100", "results"],
            "stat.discussion": ["stat_density_per100", "discussion"],
            "emdash_per1000": ["punct", "emdash_per1000"],
            "paren_per1000": ["punct", "paren_per1000"],
            "semicolon_per1000": ["punct", "semicolon_per1000"],
        }
        agg["metrics"] = {k: iqr([dig(p, path) for p in papers]) for k, path in paths.items()}
        # connective medians
        conn = {}
        for c in CONNECTIVES:
            conn[c] = iqr([dig(p, ["connectives_per1000", c]) for p in papers])
        agg["connectives_per1000"] = {c: v["median"] for c, v in conn.items() if v}
        genres[g] = agg
    return genres


def fmt(x):
    if x is None:
        return "  —  "
    return f"{x['median']} [{x['q1']}–{x['q3']}]"


def main():
    METRICS.mkdir(parents=True, exist_ok=True)
    per_paper = []
    for f in sorted(CORPUS.glob("paper*.txt"), key=lambda x: int(re.findall(r"\d+", x.stem)[0])):
        pid = f.stem
        g = genre_of(pid)
        r = analyze(pid, f.read_text(errors="ignore"), g)
        per_paper.append(r)
        (METRICS / f"{pid}.json").write_text(json.dumps(r, ensure_ascii=False, indent=2))
    genres = aggregate(per_paper)
    for g, agg in genres.items():
        (METRICS / f"genre_{g}.json").write_text(json.dumps(agg, ensure_ascii=False, indent=2))

    # human-readable summary
    L = ["# Voice fingerprint — draft (median [IQR])\n"]
    keymetrics = ["sentence.mean_len", "sentence.sd_len", "sentence.burstiness_masd",
                  "sentence.pct_short_le15", "sentence.pct_long_ge40", "subordinator_opener_pct",
                  "hedge.results", "hedge.discussion", "passive.methods", "passive.results",
                  "results_abs_rate_lead_frac", "stat.results", "emdash_per1000", "paren_per1000", "semicolon_per1000"]
    hdr = "| metric | " + " | ".join(f"{g} (n={genres[g]['n_papers']})" for g in genres) + " |"
    L.append(hdr)
    L.append("|" + "---|" * (len(genres) + 1))
    for km in keymetrics:
        row = [km] + [fmt(genres[g]["metrics"].get(km)) for g in genres]
        L.append("| " + " | ".join(row) + " |")
    L.append("\n## Connective spectrum (per 1000 words, median)\n")
    L.append("| connective | " + " | ".join(genres) + " |")
    L.append("|" + "---|" * (len(genres) + 1))
    for c in CONNECTIVES:
        L.append("| " + c + " | " + " | ".join(str(genres[g]["connectives_per1000"].get(c, 0)) for g in genres) + " |")
    L.append("\n## Genre membership\n")
    for g in genres:
        L.append(f"- **{g}** ({genres[g]['n_papers']}): {', '.join(genres[g]['ids'])}")
    (METRICS / "fingerprint_summary.md").write_text("\n".join(L), encoding="utf-8")

    print(f"analyzed {len(per_paper)} papers; genres: " + ", ".join(f"{g}={genres[g]['n_papers']}" for g in genres))
    print("wrote _metrics/*.json + fingerprint_summary.md")
    # quick sanity: section detection coverage
    missing = [p["id"] for p in per_paper if "results" not in p["sections_found"]]
    if missing:
        print("WARN: no Results section detected in:", ", ".join(missing))


if __name__ == "__main__":
    main()
