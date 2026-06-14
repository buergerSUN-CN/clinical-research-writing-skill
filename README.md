# clinical-research-writing

A Claude skill that makes clinical research manuscripts read as genuine **clinical** research rather than basic science — diagnosing and rewriting toward patient- and decision-centered framing, in the voice of strong clinical exemplars, and with concision.

> **Status: work in progress (private).** Distilled (multi-agent, per-section deep read) from 21 exemplar papers across three genres — a neurovascular/stroke + neuroimaging group's single-centre observational and imaging/diagnostic-accuracy work, plus landmark multicentre RCTs (NEJM/Lancet/JAMA). To be refined before any public release.

## What it does

- **Mode A** — diagnose & rewrite a draft section or excerpt.
- **Mode B** — draft a section from scratch.
- **Mode C** — polish a whole manuscript: classify study type → split into sections → triage → per-section rewrite (parallelizable) → cross-section "golden-thread" consistency pass → one or more of: a severity-ranked report, a **tracked-changes revised `.docx`**, and a **pure-Chinese 《修改理由》`.docx`** explaining every edit.

The central idea: basic-science writing makes the *mechanism* the subject; clinical writing makes the *patient and the bedside decision* the subject. It never fabricates data — only reframes, restructures, and trims.

## Layout

```
SKILL.md                                  # core: philosophy, contrast table, checklist, workflow
references/
  section-playbook.md                     # 8-section moves / pitfalls / exemplars / 3-genre variants
  phrasebank.md                           # 37 categories of verbatim clinical-voice phrases
  figures-tables-legends.md               # figure legends, figure/table titles, table footnotes (deep-studied)
  diagnostic-checklist.md                 # full 43-item "too basic-science?" checklist
  contrast-table-full.md                  # long-form clinical-vs-basic-science contrast, grounded
  cross-section-consistency.md            # whole-manuscript golden-thread checks
  effect-interpretation-and-reporting.md  # significance vs magnitude, NNT, TRIPOD, etc.
  domain-notes.md                         # neurovascular/imaging scales, stats, reporting standards
scripts/
  apply_tracked_changes.py                # apply an edits.json to an unpacked .docx as Word tracked changes + comments
  build_rationale_docx.py                 # format a Chinese 《修改理由》 Markdown into Word (flat house format)
```

## Install

Copy this folder to `~/.claude/skills/clinical-research-writing/` (Claude Code) and it will be available automatically.

## Tracked-changes pipeline (Mode C, Output 2)

Needs the bundled `docx` skill's `unpack.py` / `pack.py`:

```bash
python <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/
python scripts/apply_tracked_changes.py unpacked/ edits.json --author "Claude"
python <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx
```
