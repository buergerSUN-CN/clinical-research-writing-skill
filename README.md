<div align="right"><a href="README.zh.md">中文</a></div>

# clinical-research-writing

A Claude Code and Codex skill for writing clinical research papers that sound like they came from a real research group — not a basic-science lab, and not an LLM.

Built from **32 hand-picked exemplar papers** across three genres: single-centre observational & diagnostic-accuracy studies (neurovascular/stroke, Nanjing group), imaging-biomarker studies, and landmark multicentre RCTs (NEJM / Lancet / JAMA). The distillation pipeline is hybrid: quantitative linguistic fingerprinting first, then per-section deep-read pattern extraction, then adversarial validation and leave-one-out blind judging.

## Four modes

| Mode | What | When |
|---|---|---|
| **A — Diagnose & rewrite** | Quote the offending sentence, name what's wrong (basic-science framing / template / AI-tell), show a clinical rewrite. Cross-checks against a measured genre fingerprint. | Most common. Polishing a section or paragraph. |
| **B — Draft from scratch** | Write a section _de novo_ in the target genre's voice, given the study design and key numbers. | When a section hasn't been written yet. |
| **C — Whole-manuscript polish** | Classify → split into IMRaD units → triage → per-section rewrite → mandatory cross-section coherence pass → three deliverables. | A full paper, pre-submission. |
| **D — Checklist audit** | Map the study to the right reporting standard (STROBE / CONSORT / STARD / TRIPOD), audit item-by-item (✅ reported / ⚠️ partial / ❌ missing / N/A), produce a gap report with severity and one-line fixes. | Pre-submission check. Catch the items reviewers will flag. |

### Mode C deliverables

1. **Markdown revision report** — what, where, how severe, suggested rewrite.
2. **Tracked-changes `.docx`** — every edit applied; rejecting all changes restores the original exactly.
3. **Chinese 《修改理由》 `.docx`** — two lines per edit in pure Chinese: what changed and why (for supervisors and reviewers).

## What makes this different

**It's measured, not intuited.** `scripts/metrics.py` computes a per-genre voice fingerprint against the exemplar corpus — sentence burstiness (SD ≈ 1.3–1.5× mean), section-bound hedging density (Results ≈ 0, Discussion ≈ 8–11 per 1000 words), passive-voice ratios by section (Methods: 55–72% — correct, don't touch), connective spectra, em-dash frequency (~0 in this group). `scripts/check_draft.py` checks a draft against these targets in one line.

**It teaches principles, not frames.** The old phrase-bank taught fill-in-the-blank templates — "Nearly one in five patients experienced X" was the canonical output. The new skill gives 39 sourced moves (Title → Conclusion), each a *principle + verbatim Correct exemplar (source-verified) + AI Incorrect counter-example + anti-repetition constraint*. Lift the reasoning, never paste a frame.

**The anti-AI layer is corpus-derived, not guessed.** Hard signals: uniform hedging, AI connectives (*Moreover / Additionally / Notably* — near-zero in the exemplars), vacuous "significant clinical implications" closers, fake-fraction flourishes, over-smoothing that sands away the honest roughness of real ESL-authored papers. Soft signals caught by blind leave-one-out judging: aphoristic paragraph closers ("The novelty is elsewhere."), manufactured symmetry, too-perfect enumerated limitations, thinned number-density. All catalogued in `clinical_ai_tells.md`.

**It defers, it doesn't duplicate.** General IMRaD structure, hedging taxonomies, tense conventions, and reporting boilerplate belong to the host's general scientific-writing skills. Word-level de-AI uses `humanizer-academic` in Codex or `humanizer_academic` in Claude Code, with clinical exemptions: Methods passive stays, em-dash is a threshold rather than a ban, and hedging remains section-bound. This skill adds the clinical + genre-voice + anti-AI delta.

## Layout

```
SKILL.md                          # router, genre classify, four modes, grep loop, anti-AI order
agents/openai.yaml                # Codex UI metadata (ignored by Claude Code)
references/
  voice_fingerprint.md            # A/B/C numeric targets + anti-AI laws
  voice_principles.md             # 39 anti-template moves, sourced, Correct/Incorrect
  structure_contract.md           # genre skeleton, claim-gradient, mandatory cross-section pass
  clinical_ai_tells.md            # corpus-derived AI-tell checklist + humanizer exemptions
  reporting_checklists.md         # STROBE / CONSORT / STARD / TRIPOD, per-item, grep-indexed
  domain_notes.md                 # mRS / ASPECTS / TICI / κ… field vocabulary
  display_items.md                # self-contained figure legends / table footnotes
scripts/
  apply_tracked_changes.py        # apply edits.json as Word tracked changes
  build_rationale_docx.py         # format Chinese 《修改理由》 into Word
  metrics.py                      # compute the quantitative fingerprint
  check_draft.py                  # one-line draft check against genre targets
```

## Install

Claude Code:

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.claude/skills/clinical-research-writing
```

Codex:

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.codex/skills/clinical-research-writing
```

## Quick start

**Rewrite a Results paragraph (genre A):**

```
rg -n -A6  "#results"          references/voice_principles.md
rg -n -A5  "#hedging"          references/voice_fingerprint.md
rg -n -A4  "#numbers"          references/voice_fingerprint.md
rg -n -A15 "#tells"            references/clinical_ai_tells.md
```

**Check a draft:** `python3 scripts/check_draft.py draft.txt --genre A`

**Audit a manuscript before submission:**
```
rg -n -A10 "#mapping"   references/reporting_checklists.md   # find the right checklist
rg -n -A30 "#strobe"    references/reporting_checklists.md   # or #consort / #stard / #tripod
```

**Apply edits to Word:**
```bash
python3 <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/ --merge-runs false
python3 scripts/apply_tracked_changes.py unpacked/ edits.json --author "Codex"  # or Claude
python3 <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx
```
