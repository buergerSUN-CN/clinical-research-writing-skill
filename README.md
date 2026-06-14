# clinical-research-writing

A Claude skill that makes clinical research manuscripts read as genuine **clinical** research rather than basic science — diagnosing and rewriting toward patient- and decision-centered framing, in the voice of strong clinical exemplars, and with concision.

> **Status: work in progress (private).** Distilled from a curated corpus of neurovascular/stroke and neuroimaging clinical papers. To be refined before any public release.

## What it does

- **Mode A** — diagnose & rewrite a draft section or excerpt.
- **Mode B** — draft a section from scratch.
- **Mode C** — polish a whole manuscript: classify study type → split into sections → triage → per-section rewrite (parallelizable) → cross-section "golden-thread" consistency pass → severity-ranked report **or** a tracked-changes `.docx`.

The central idea: basic-science writing makes the *mechanism* the subject; clinical writing makes the *patient and the bedside decision* the subject. It never fabricates data — only reframes, restructures, and trims.

## Layout

```
SKILL.md                                  # core: philosophy, contrast table, checklist, workflow
references/
  section-playbook.md                     # 8-section moves / pitfalls / exemplars / variants
  phrasebank.md                           # categorized verbatim clinical-voice phrases
  diagnostic-checklist.md                 # full "too basic-science?" checklist
  cross-section-consistency.md            # whole-manuscript golden-thread checks
  effect-interpretation-and-reporting.md  # significance vs magnitude, NNT, TRIPOD, etc.
  domain-notes.md                         # neurovascular/imaging scales, stats, reporting standards
scripts/
  apply_tracked_changes.py                # apply an edits.json to an unpacked .docx as Word tracked changes + comments
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
