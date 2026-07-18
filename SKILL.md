---
name: clinical-research-writing
description: >-
  Make a clinical research manuscript read as genuine CLINICAL research written in a real research
  group's voice — not basic science, and not AI. Use whenever drafting, revising, or polishing a
  clinical study paper or any IMRaD section (Title, Abstract, Introduction, Methods, Results,
  Discussion, Limitations, Conclusion), and ESPECIALLY when a reviewer/supervisor/co-author says the
  writing feels "too basic-science", lacks "clinical feel" / 临床感, is too mechanism-focused, reads
  templated, or "sounds AI-generated" / 有AI感/人机感. Also use to convert mechanism-first framing into
  patient- and decision-centered framing, to self-edit a draft against a quantitative voice
  fingerprint, or to make a paper more publishable in a clinical journal. Distilled per-genre from 32
  exemplars — A: single-centre observational/prognostic/procedural (neurovascular/stroke), B:
  imaging-biomarker/technique, C: multicentre RCT — so mount the genre that matches the paper.
  Principles transfer to any clinical specialty. Trigger generously.
---

# Clinical Research Writing

Encodes **how specific clinical-research groups actually write**, distilled per-genre from 32 hand-picked exemplars, so a draft reads as *clinical* (not basic-science) and *human* (not AI/templated). Two things make this work and set it apart from generic clinical-writing advice:

1. **A quantitative voice fingerprint** (`scripts/metrics.py` → `references/voice_fingerprint.md`): measured sentence burstiness, section-bound hedging, passive-by-section, connective spectrum, punctuation — objective targets you can check a draft against.
2. **Anti-template principles** (`references/voice_principles.md`): every move is a *principle + real Correct exemplar + AI Incorrect counter-example*, never a fill-in-the-blank frame. Copying a frame is what produced templated output like "Nearly one in five patients experienced X" — the exact AI tell this skill kills.

**The one idea.** Basic-science writing makes the *mechanism* the subject; clinical writing makes the *patient and the bedside decision* the subject. Keep the paper's top-level claim sharp and calibrated to the design — never flatten it while trimming. It never fabricates data; it reframes, restructures, trims, and de-AIs.

## Reference map — grep, don't load {#refs}
These files are large and grep-indexed (`{#anchor}` + Quick Grep Targets in each). **Never read one whole**; pull the 20–40 lines you need per step.

| file | what it holds | grep when |
|---|---|---|
| `references/voice_fingerprint.md` | genre A/B/C numeric targets + the anti-AI laws | before/after writing any section |
| `references/voice_principles.md` | 39 section moves (Title→Conclusion), sourced, Correct/Incorrect | writing/rewriting a section |
| `references/structure_contract.md` | study_type×genre skeleton, claim-gradient, cross-section pass | planning a section or a whole paper |
| `references/clinical_ai_tells.md` | banned AI patterns + humanizer wrap/exemptions | the de-AI post-draft pass |
| `references/domain_notes.md` | mRS/ASPECTS/TICI/κ… field vocabulary & cut-offs | need a scale/stat/reporting convention |
| `references/display_items.md` | self-contained figure legends / table footnotes | writing any display item |
| `references/reporting_checklists.md` | STROBE / CONSORT / STARD / TRIPOD items, per-item, grep-indexed | Mode D checklist audit |

**Defer (don't re-implement):** general IMRaD structure, hedging taxonomy, tense, paragraph craft → `academic-research-skills` plugin (`academic_writing_style.md`, `paper_structure_patterns.md`) and the `scientific-writing` skill. Word-level de-AI → `humanizer_academic` (English) / `humanizer-zh-academic` (Chinese). Final Word formatting → `submission-format`. Citation checks → `citecheck`. This skill only adds the clinical + group-voice + anti-AI delta.

## Step 0 — classify first (always) {#classify}
Fix **study_type** (interventional-cohort / prognostic-predictor / diagnostic-accuracy / imaging-technique / procedural-comparative / rct / rct-posthoc) and **genre** (A single-centre-observational / B imaging / C RCT) — rules branch on both (`structure_contract.md #classify`). Mount that genre's fingerprint row and VARIANT moves.

## Modes {#modes}

### Mode A — diagnose & rewrite a section (most common)
1. `grep` the relevant section anchors in `voice_principles.md` + the genre row in `voice_fingerprint.md`.
2. Find the sentences that read basic-science, templated, or AI. Quote the offender, name the failed move/tell, show a clinical rewrite. No vague "add clinical relevance".
3. Preserve every number and citation exactly — you change framing, not results.

### Mode B — draft a section from scratch
Draft straight from the section's moves in `voice_principles.md` (per genre), keeping numeric targets from `voice_fingerprint.md` and scales from `domain_notes.md`. Self-check against `clinical_ai_tells.md` before returning.

### Mode C — polish a whole manuscript
A full paper is NOT one diagnostic pass — split, polish per section, reassemble.
1. **Classify** (Step 0) once.
2. **Split** into units: Title, Abstract/boxes, Intro, Methods, Results, Discussion, Limitations, Conclusion, Tables, legends. (For `.docx`, convert with the `docx`/`markitdown` tooling first.)
3. **Triage** each unit against `clinical_ai_tells.md` + the section moves; don't churn clean sections.
4. **Rewrite** each flagged unit with its `voice_principles.md` moves (parallelizable — one agent per section for a long paper).
5. **Cross-section consistency pass (MANDATORY)** — `structure_contract.md #cross-section`: golden thread aim→conclusion, numeric reconciliation, Methods↔Results fidelity, claim-gradient monotonic, terminology, no dangling supplement refs. Cannot be done section-by-section.
6. **Deliver** (usually Output 2 + 3 together).

### Mode D — checklist audit
For any draft (or a finished manuscript), audit it against the applicable reporting standard. Run this **before** Mode C polish, or as a standalone pre-submission check.
1. From Step 0's study_type, find the checklist(s) via `references/reporting_checklists.md #mapping`.
2. `grep` the checklist section(s) (e.g. `grep -A30 "#strobe" references/reporting_checklists.md`).
3. Go item by item. For each: search the draft for the required content. Mark it **✅ reported** (cite where), **⚠️ partial** (what's missing), **❌ missing** (severity: ■high / ■medium / ■low), or **N/A**.
4. Deliver a gap report: (a) summary line — total/passed/partial/missing/N/A; (b) pass items in one compact block ("Items 1a, 1b, 2, 3…: ✅"); (c) every missing/partial item called out with its severity, the draft location that should hold it, and a one-line fix (what to add, or whether to state as a limitation). No vague "consider adding X" — say what's absent and what to write into which section.

## The per-section loop {#loop}
For each section: **classify → grep moves+fingerprint → draft/rewrite → self-check → (whole paper) cross-section pass.** Example (Results, genre A):
```
grep -A6  "#results"          references/voice_principles.md
grep -A5  "#hedging"          references/voice_fingerprint.md   # Results ≈ 0 hedge
grep -A4  "#numbers"          references/voice_fingerprint.md   # n/N (%) + CI
grep -A15 "#tells"            references/clinical_ai_tells.md
```
Then, to check a draft objectively: `python scripts/metrics.py` (point it at the draft) and pull outliers back toward the genre IQR. For a checklist audit, see Mode D above and grep the relevant checklist from `references/reporting_checklists.md`.

## Anti-AI — run these passes in order {#anti-ai}
1. Clinical reframing + genre voice (this skill: `voice_principles` + `structure_contract`).
2. **This skill's AI-tell self-check** + fingerprint compare (`clinical_ai_tells.md #tells`, `metrics.py`).
3. `humanizer_academic` word-level pass — WITH the clinical exemptions (`clinical_ai_tells.md #humanizer`: Methods stays passive; em-dash is a threshold not zero; hedging stays section-bound; whitelist "associated with" etc.).
4. Language/journal polish last. Chinese output → `humanizer-zh-academic`.

## Mode C outputs {#outputs}
**Output 1 — Markdown revision report:** study-type+genre line; findings table (section · offending text · failed move/tell · severity · rewrite); cross-section thread map; prioritized checklist. Numbers/citations untouched.

**Output 2 — Tracked-changes `.docx`.** Rewrite boldly, concisely, in the genre voice; aim for **net fewer words**. **Never fabricate** — every number in an edit is lifted verbatim from the manuscript; a needed-but-absent number becomes a comment, not an invention. Apply with `scripts/apply_tracked_changes.py` (preserves run formatting; rejecting all changes restores the original exactly):
```bash
python <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/ --merge-runs false
python scripts/apply_tracked_changes.py unpacked/ edits.json --author "Claude"
python <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx
```
`edits.json` = list of `{"type":"replace","find":…,"replace":…}` / `{"type":"insert_after","find":…,"insert":…}` / `{"type":"comment","find":…,"comment":…}`; each `find` is verbatim source text within ONE paragraph; `[brackets]` for any number not in the source. **Seam rules (the failure mode):** a `find` starts/ends at a clause boundary and includes any leading connective the rewrite changes; a `replace` substituted in place must be a grammatically complete sentence; don't swallow a superscript-citation/bold run unless you reproduce it; verify with a seam+grammar pass, not just number-checking (`pandoc --track-changes=all`).

**Output 3 — Chinese rationale `.docx` (《修改理由》):** pure Chinese, two lines per edit (**改动** what→what, no English sentences; **理由** the clinical/voice principle + source line/table for any number). Group by IMRaD; `comment`-type items under 「### 建议补充（批注）」. Save as Markdown then:
```bash
python scripts/build_rationale_docx.py 修改理由.md manuscript_修改理由.docx
```

## Hard rules {#rules}
Integrity floor — distinct from voice:
- **Never fabricate or alter data, statistics, citations, methods, or analyses.** A failed checklist item usually means the study *didn't do* something — that's a note to the author or a limitation, never license to invent.
- **Match study_type and genre.** Don't force ROC/AUC onto a binary read, an adjusted OR onto a procedural comparison, or C's RCT register onto a single-centre cohort.
- **Results states facts; Discussion interprets.** Keep narrative framing ("the central paradox", "strikingly") out of Results.
- **Don't cite a supplement/appendix the paper doesn't have.**
- **Don't paste exemplar sentences into a real manuscript** — they are style models; reuse the reasoning, not the words.
- **Finished/submitted manuscripts: be conservative** — edit only what fails a check; preserve the author's voice; keep numbers and citations untouched.
