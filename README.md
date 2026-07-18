<div align="right"><a href="README.zh.md">中文</a></div>

# clinical-research-writing

A Claude Code skill that makes clinical research manuscripts read as **genuine clinical research** written in a real group's voice — not basic science, and not AI.

Distilled per-genre from **32 hand-picked exemplars** (neurovascular/stroke + neuroimaging, NEJM/Lancet/JAMA RCTs), using a hybrid pipeline: quantitative linguistic fingerprinting (sentence burstiness, section-bound hedging, connective spectrum) + per-section deep-read pattern extraction with adversarial validation and leave-one-out blind judging.

## What it does

- **Mode A** — diagnose & rewrite a section. Identifies specific sentences that read basic-science/templated/AI; quotes the offender; shows a clinical rewrite. Checks against a measured genre fingerprint.
- **Mode B** — draft a section from scratch in the target genre's voice.
- **Mode C** — polish a whole manuscript. Classify → split into sections → triage → per-section rewrite (parallelizable) → mandatory cross-section "golden-thread" consistency pass → deliverables:
  - **Output 1** — Markdown revision report (findings table, severity, suggested rewrites)
  - **Output 2** — Tracked-changes revised `.docx` (edits applied; rejecting all changes restores the original exactly)
  - **Output 3** — Chinese 《修改理由》 `.docx` (pure Chinese, two-line-per-edit explanation for supervisors/reviewers)

## How it's different from generic clinical-writing advice

1. **Quantitative voice fingerprint** — measured targets per genre (A observational · B imaging · C RCT): sentence burstiness (SD ≈ 1.3–1.5× mean), section-bound hedging (Results ≈ 0, Discussion ≈ 8–11 /1000), Methods-passive exemption (55–72%), em-dash ≈ 0, banned connectives. `scripts/metrics.py` computes these; `scripts/check_draft.py` checks a draft against them.

2. **Anti-template principles, not phrase banks** — 39 sourced moves (Title → Conclusion). Every move is a *principle + verbatim Correct exemplar (paperNN-verified) + AI Incorrect counter-example + anti-repetition note*. No fill-in-the-blank frames — the old skill's phrase-bank taught templating ("Nearly one in five patients experienced X"); the new skill kills it.

3. **Corpus-derived AI-tell layer** — hard anti-AI signals reverse-inferred from the exemplars (uniform hedging, AI connectives, "significant clinical implications" filler, fake-fraction flourish) plus LLM-signature tells caught by leave-one-out blind judging (aphoristic closers, manufactured symmetry, too-perfect limitations, thinned specificity).

4. **Deferral, not duplication** — general IMRaD structure / hedging taxonomy / reporting standards (CONSORT, STROBE, TRIPOD) are delegated to the `academic-research-skills` plugin and `scientific-writing` skill. Word-level de-AI delegates to `humanizer_academic` (with clinical exemptions for Methods-passive, em-dash thresholds, section-bound hedging). This skill adds only the clinical + genre-voice + anti-AI delta.

## Layout

```
SKILL.md                      # router, genre classify, Modes A/B/C, grep loop, anti-AI order, defer map
references/
  voice_fingerprint.md        # A/B/C numeric targets + anti-AI laws (grep-indexed)
  voice_principles.md         # 39 anti-template section moves, sourced, Correct/Incorrect
  structure_contract.md       # genre skeleton, claim-gradient, mandatory cross-section pass
  clinical_ai_tells.md        # corpus-derived AI-tell checklist + humanizer exemptions
  domain_notes.md             # mRS/ASPECTS/TICI/κ… field vocabulary (slim, only what's used)
  display_items.md            # self-contained figure legends / table footnotes
scripts/
  apply_tracked_changes.py    # ← preserved from v1
  build_rationale_docx.py     # ← preserved from v1
  metrics.py                  # compute the quantitative fingerprint
  check_draft.py              # one-line draft check: python scripts/check_draft.py draft.txt --genre A
```

## Install

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.claude/skills/clinical-research-writing
```

## Tracked-changes pipeline (Mode C, Output 2)

Requires the bundled `docx` skill's `unpack.py` / `pack.py`:

```bash
python <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/ --merge-runs false
python scripts/apply_tracked_changes.py unpacked/ edits.json --author "Claude"
python <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx
```

## Writing loop (example: Results, genre A)

```
grep -A6  "#results"          references/voice_principles.md
grep -A5  "#hedging"          references/voice_fingerprint.md   # Results ≈ 0
grep -A4  "#numbers"          references/voice_fingerprint.md   # n/N (%) + CI
grep -A15 "#tells"            references/clinical_ai_tells.md
```

Then: `python scripts/check_draft.py draft.txt --genre A`
