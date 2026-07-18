---
name: clinical-research-writing
description: >-
  Draft, revise, diagnose, or polish clinical research manuscripts in a genuine clinical-group
  voice rather than basic-science, engineering, templated, or AI-sounding prose. Use for any IMRaD
  section, title, abstract, limitation, conclusion, table, figure legend, whole-manuscript polish,
  or STROBE/CONSORT/STARD/TRIPOD audit; especially when feedback mentions clinical feel, 临床感,
  mechanism-first framing, patient- or decision-centered framing, AI感, 人机感, journal restraint,
  neurovascular/stroke studies, imaging biomarkers, observational/prognostic/diagnostic studies,
  procedural comparisons, or randomized trials. Supports genre-matched voice fingerprints and
  tracked-change DOCX delivery without changing source data or citations.
---

# Clinical Research Writing

Make the patient and bedside decision the subject of the paper. Keep mechanisms and technical
details subordinate to clinical population, endpoint, prognosis, treatment selection, diagnostic
value, workflow, and management. Preserve the manuscript's calibrated top-level claim.

This skill adds a clinical/group-voice layer to general academic writing:

- Use `references/voice_fingerprint.md` for measured genre A/B/C targets.
- Use `references/voice_principles.md` for section-specific moves and anti-template examples.
- Use `references/structure_contract.md` for study routing and whole-paper consistency.
- Use `references/clinical_ai_tells.md` for corpus-derived AI-tell checks.
- Use `references/domain_notes.md` for neurovascular, stroke, imaging, and statistics conventions.
- Use `references/display_items.md` for tables, figures, legends, and footnotes.
- Use `references/reporting_checklists.md` for STROBE, CONSORT, STARD, and TRIPOD audits.

Resolve every resource path relative to this skill directory. Search only the needed anchors with
`rg`; do not load a large reference file in full.

## Classify First

Set both dimensions before writing:

- `study_type`: interventional-cohort, prognostic-predictor, diagnostic-accuracy,
  imaging-technique, procedural-comparative, RCT, or RCT post hoc.
- `genre`: A (single-centre observational/prognostic/procedural), B (imaging), or C (RCT).

Use `references/structure_contract.md` at `#classify`, then mount the corresponding fingerprint
row and variant moves.

## Mode A: Diagnose and Rewrite a Section

1. Search the section anchors in `voice_principles.md` and the genre row in
   `voice_fingerprint.md`.
2. Quote each sentence that reads as basic-science, templated, or AI-written; identify the failed
   move or tell; provide a clinical rewrite.
3. Preserve every source number, denominator, statistic, endpoint, and citation exactly.

## Mode B: Draft a Section

1. Use the applicable moves in `voice_principles.md` and the selected genre fingerprint.
2. Use `domain_notes.md` only when a specialty scale or reporting convention is needed.
3. Draft in a restrained clinical register, then self-check against `clinical_ai_tells.md`.

## Mode C: Polish a Whole Manuscript

1. Classify the study once.
2. Split the manuscript into Title, Abstract/boxes, Introduction, Methods, Results, Discussion,
   Limitations, Conclusion, Tables, and legends. For DOCX, use the host's available `docx` or
   `markitdown` skill first.
3. Triage each unit; do not churn clean sections.
4. Rewrite flagged units section by section. Delegate sections only when the user explicitly asks
   for parallel agent work.
5. Run the mandatory `structure_contract.md` `#cross-section` pass: aim-to-conclusion thread,
   numeric reconciliation, Methods-Results fidelity, claim-gradient monotonicity, terminology, and
   dangling supplement references.
6. Deliver the requested combination of revision report, tracked-change DOCX, and Chinese rationale.

## Mode D: Reporting-Checklist Audit

1. Map `study_type` to the applicable checklist with `reporting_checklists.md` `#mapping`.
2. Audit every item as `✅ reported`, `⚠️ partial`, `❌ missing`, or `N/A`.
3. Report totals, compactly list passed items, and describe each partial/missing item with severity,
   intended manuscript location, and a concrete one-line fix.
4. Treat absent analyses or data as author queries or limitations, never as permission to invent.

## Per-Section Loop

For each section: classify → search moves and fingerprint → draft/rewrite → self-check. For a whole
paper, finish with the cross-section pass. To check a plain-text or Markdown draft quantitatively,
run:

```bash
python3 <skill-dir>/scripts/check_draft.py <draft.txt> --genre A
```

Use `scripts/metrics.py <workspace>` only to rebuild the fingerprint from a workspace containing
`_corpus/` and `_meta/`; it is not the draft checker.

## Anti-AI Pass Order

1. Apply clinical reframing and genre voice with this skill.
2. Run the AI-tell self-check and `check_draft.py` fingerprint comparison.
3. Use the host's English humanizer (`humanizer-academic` in Codex; `humanizer_academic` in
   Claude Code) or `humanizer-zh-academic` for Chinese, while preserving the clinical exemptions
   in `clinical_ai_tells.md` `#humanizer`.
4. Apply language or journal polish last.

Methods may remain intentionally passive; hedging must stay section-bound; clinical-standard terms
are exempt from generic AI-vocabulary bans.

## DOCX Deliverables

For tracked changes, use the host's available `docx` skill's unpack/pack scripts with
`scripts/apply_tracked_changes.py`. Set `--author` to the current host (`Codex` or `Claude`). Each
`find` value must be verbatim text from one paragraph and each replacement must be grammatically
complete. Preserve citation and formatting runs, then verify seams, grammar, numbers, and
tracked-change reversibility.

Build a Chinese rationale DOCX with:

```bash
python3 <skill-dir>/scripts/build_rationale_docx.py 修改理由.md manuscript_修改理由.docx
```

## Integrity Rules

- Never fabricate or alter data, statistics, citations, methods, analyses, or source meaning.
- Never force a statistic, scale, or register that does not match the study type and genre.
- Keep factual reporting in Results and interpretation in Discussion.
- Never cite a supplement or appendix that does not exist.
- Treat exemplars as style evidence; never paste their wording into a manuscript.
- Edit finished or submitted manuscripts conservatively and preserve the author's voice.
