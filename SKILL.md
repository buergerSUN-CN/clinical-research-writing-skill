---
name: clinical-research-writing
description: >-
  Draft, revise, diagnose, or audit clinical research manuscripts in a restrained,
  patient- and decision-centered clinical voice. Use for titles, abstracts, IMRaD sections,
  limitations, conclusions, tables, figure legends, whole-manuscript revision, tracked-change
  DOCX delivery, or STROBE/CONSORT/STARD/TRIPOD review; especially when feedback mentions clinical
  feel, 临床感, mechanism-first framing, AI感, journal restraint, observational or prediction
  studies, diagnostic or imaging studies, procedural comparisons, randomized trials, or
  neurovascular/stroke research. Preserve all source facts, numbers, methods, and citations.
---

# Clinical Research Writing

Make the patient population, endpoint, and clinical decision the subject of the paper. Keep
mechanisms and technical details subordinate to prognosis, diagnosis, treatment selection,
workflow, and management. Preserve the claim strength justified by the design.

Resolve all paths relative to this skill directory. Load only the references needed for the
current section.

## Route the Manuscript

Set two dimensions before writing:

- `study_family`: `observational`, `diagnostic-imaging`, `procedural-comparative`, `trial`, or
  `trial-secondary`.
- `profile`: `general` for all clinical manuscripts; additionally mount `neurovascular` only for
  stroke, neuroimaging, or neurointerventional work.

Read `references/study_families.md` for design-specific claim and reporting behavior. Read
`references/neurovascular_profile.md` only when the specialty matches. Treat legacy genres as
aliases: A=`observational`/`procedural-comparative`, B=`diagnostic-imaging`, C=`trial` or
`trial-secondary`.

## Load the Writing Rules

- Always read `references/core_principles.md` for integrity, clinical framing, and section bounds.
- Load one section file: `references/moves_title_abstract.md`,
  `references/moves_introduction.md`, `references/moves_methods.md`,
  `references/moves_results.md`, or `references/moves_discussion.md`.
- For neurovascular work, load `references/neurovascular_profile.md`, then consult
  `references/domain_notes.md` and `references/voice_fingerprint.md` only as needed.
- Use `references/structure_contract.md` for whole-paper reconciliation.
- Use `references/clinical_ai_tells.md` for the final anti-template pass.
- Use `references/display_items.md` for tables, figures, legends, and footnotes.
- Use `references/reporting_checklists.md` only for a reporting-standard audit.
- Treat `references/voice_principles.md` as a compatibility index for prompts written for v1.

## Mode A: Diagnose and Rewrite

1. Quote each source sentence that fails a clinical move or shows a template/AI tell.
2. Name the failed rule and explain the clinical consequence.
3. Rewrite the smallest necessary unit while preserving every number, endpoint, method, and citation.

## Mode B: Draft a Section

1. Extract the permitted facts and label each candidate statement as `source fact`, `source-stated
   interpretation`, `inference`, or `author query` before drafting.
2. Apply the study-family rules and the relevant section moves.
3. Draft from source facts and source-stated interpretations. Do not silently fill a sparse source with
   standard background, mechanisms, limitations, management advice, validation needs, or citations.
   Include an inference only when the user asked for reasoned interpretation and mark it as such.
4. Run the anti-AI and numeric-fidelity checks.

## Mode C: Polish a Whole Manuscript

1. Classify the study once and split it into Title, Abstract/boxes, Introduction, Methods, Results,
   Discussion, Limitations, Conclusion, Tables, and legends.
2. Triage each unit; do not churn clean prose.
3. Rewrite flagged units section by section.
4. Run the mandatory cross-section pass in `structure_contract.md`: aim-to-conclusion thread,
   Methods-Results fidelity, numeric reconciliation, terminology, claim gradient, and supplement
   references.
5. Deliver the requested revision report, tracked-change DOCX, and/or Chinese rationale.

## Mode D: Reporting Audit

1. Map the design to STROBE, CONSORT, STARD, or TRIPOD with
   `reporting_checklists.md` `#mapping`.
2. Mark every item `reported`, `partial`, `missing`, or `N/A`.
3. Give severity, intended location, and a one-line fix for each partial or missing item.
4. Treat absent data or analyses as author queries, never permission to invent them.

## Quantitative Check

Use the general scan for any clinical manuscript:

```bash
python3 <skill-dir>/scripts/check_draft.py draft.txt --study-family observational --profile general
```

Use `--profile neurovascular` to compare against the measured 32-paper stroke/neurovascular
fingerprint. Legacy `--genre A|B|C` remains supported. Numeric ranges are diagnostic signals, not
targets to optimize sentence by sentence.

## Anti-AI Order

1. Correct the clinical framing and claim strength.
2. Restore section-specific behavior and number density.
3. Run `check_draft.py` and `clinical_ai_tells.md`.
4. Use the host's academic-humanizer skill only for word-level cleanup, preserving Methods passive
   voice, clinical terminology, statistics, and section-bound hedging.
5. Apply journal house style last.

## DOCX Delivery

Use the host's DOCX skill to unpack and repack Word files. Apply tracked changes with
`scripts/apply_tracked_changes.py`; pass `--author Codex` or `--author Claude` explicitly. Each
`find` value must be verbatim text from one paragraph and each replacement must be grammatically
complete. Verify seams, numbers, formatting, and reject-all reversibility.

Build a Chinese rationale DOCX with:

```bash
python3 <skill-dir>/scripts/build_rationale_docx.py 修改理由.md manuscript_修改理由.docx
```

## Integrity Rules

- Never fabricate or alter data, statistics, citations, methods, analyses, or source meaning.
- Never apply the neurovascular fingerprint to an unrelated specialty as if it were validated there.
- Keep factual reporting in Results and interpretation in Discussion.
- Never cite a supplement or appendix that does not exist.
- Treat exemplars as evidence for decisions; never paste or imitate their sentences.
- Edit submitted manuscripts conservatively and preserve defensible author voice.
