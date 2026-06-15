---
name: clinical-research-writing
description: >-
  Make a clinical research manuscript read as genuine CLINICAL research rather than basic
  science. Use whenever drafting, revising, or polishing a clinical study paper or any IMRaD
  section (Title, Abstract, Introduction, Methods, Results, Discussion, Limitations, Conclusion),
  and ESPECIALLY when a reviewer, supervisor, or co-author says the writing feels "too
  basic-science", lacks "clinical feel" / 临床感, or is too mechanism-focused. Also use to convert
  mechanism-first framing into patient- and decision-centered framing, to self-edit a draft against
  clinical-writing standards, or to make a paper more publishable in a clinical journal. Tuned for
  neurovascular / stroke / neurointervention and neuroimaging / diagnostic-accuracy studies (cohort,
  registry, post-hoc RCT, predictor/prognostic, propensity-matched, diagnostic-accuracy,
  procedural-comparative), but the principles transfer to any clinical specialty. Trigger generously:
  if the task involves writing or improving a clinical research paper, consult this skill even when
  the user does not say the words "clinical voice".
---

# Clinical Research Writing

This skill encodes what makes clinical research papers read as *clinical* rather than *basic science*. It was distilled (multi-agent, per-section deep read) from 21 hand-picked exemplar papers spanning three genres: a neurovascular/stroke + neuroimaging group's single-centre observational and imaging/diagnostic-accuracy work (corresponding authors Sheng Liu, Hai-Bin Shi, Fei-Yun Wu; JAHA, Translational Stroke Research, European Radiology, Academic Radiology, JNIS) **and** landmark multicentre RCTs (NEJM, Lancet, JAMA — basilar-artery-occlusion thrombectomy). Every exemplar quoted in the reference files is verbatim and tagged with its source paper; `variant notes` flag where the three genres diverge.

## Core principles

Three principles sit underneath every mode below. They assume the academic-writing basics in `references/basic-writing-requirements.md` (section roles, paragraph craft, hedging) — obey those first, then layer the clinical voice on top.

### 1. Center of gravity — the patient and the decision, not the mechanism

**Basic-science writing makes the mechanism the subject. Clinical writing makes the patient and the bedside decision the subject.** Mechanism is still present — but demoted to *supportive plausibility*, never the headline. If a sentence's center of gravity is a pathway, a molecule, or "understanding biology," it reads basic-science. If it is a patient population, a clinical endpoint, a risk, or a management decision, it reads clinical. Everything else here is a way of pushing the center of gravity toward the patient and the decision.

### 2. Concision is clinical — say it simply

The best clinical papers state the most important clinical question in the fewest, plainest words ("用最简单的方式说出最重要的临床问题"). Clinicians read fast; every extra clause is a cost, and economy is itself a marker of good clinical writing. Reframing toward clinical voice must **not** add bulk:

- Prefer the shortest version that keeps the meaning and the numbers.
- Cut throat-clearing ("It is worth noting that…"), nominalizations ("performed an evaluation of" → "evaluated"), hedge-stacking, and redundancy.
- Push engineering/method granularity to a real supplement, or cut it; the main text carries the clinical point.
- A pure-deletion tracked edit that only trims is often the highest-value one. **Net word count should usually go down, not up.**

### 3. Edit boldly, in the exemplars' voice

When asked to polish a real manuscript, **make the edits** (tracked changes) — do not hide behind margin comments. Reserve comments only for data genuinely missing from the source (an unmeasured statistic, blinded-read details); many "missing" numbers already exist elsewhere in the manuscript and should be pulled in verbatim, not flagged. Rewrite **boldly** — recast whole sentences and openings — and match how the target group actually writes by modelling `references/phrasebank.md` and the exemplar sentences in `references/section-playbook.md`, rather than a generic clinical register. The bar is: would this pass for one of the exemplar papers?

## How to use this skill

### Step 0 — Classify the study type first (always)
Before any rewriting, classify the study, because the rules branch on it: **interventional/cohort/prognostic**, **diagnostic-accuracy**, **imaging-technique** (image quality as the primary endpoint), or **procedural-comparative**. The playbook's *variant notes* and many checklist items apply differently per type — e.g., don't force ROC/AUC onto a binary diagnostic read, or an adjusted OR onto a procedural comparison. Then pick the mode by what the user is doing.

### Mode A — Diagnose & rewrite a draft section or short excerpt (most common)
1. Run the **Quick diagnostic** below (full version: `references/diagnostic-checklist.md`). Identify the specific sentences that read basic-science.
2. Report findings concretely: quote the offending sentence, name *which* check it fails, and show a clinical rewrite. Do not give vague advice like "add more clinical relevance."
3. For each section being rewritten, open `references/section-playbook.md`, apply the *clinical moves*, avoid the *pitfalls*, and model the *exemplar sentences*. Pull framing from `references/phrasebank.md` (lift the frame, never the data).
4. Preserve the author's findings and numbers exactly. You are changing framing and emphasis, **not** inventing results.

### Mode B — Draft a section from scratch
1. Draft straight from `references/section-playbook.md` for that section (per the Step 0 study type), using `references/phrasebank.md` for connective tissue and `references/domain-notes.md` for the correct scales/statistics/reporting standards.
2. Self-check against the diagnostic checklist before returning.

### Mode C — Polish a whole finished manuscript
A full paper is **not** one big diagnostic pass — split it, polish by section, then reassemble. Pipeline:
1. **Classify** (Step 0) once for the whole paper.
2. **Split** into units: Title, structured Abstract / journal boxes (Key Points, Clinical relevance), Introduction, Methods, Results, Discussion, Limitations, Conclusion, plus Tables and figure legends. (For `.docx`, convert with the `docx`/`markitdown` tooling first.)
3. **Triage**: skim each unit against the Quick diagnostic; mark which actually need work — don't churn clean sections.
4. **Rewrite** each flagged unit with its playbook section. Independent sections can be done in parallel (one agent per section) for a long manuscript.
5. **Join — run the cross-section consistency pass (MANDATORY, do not skip)** (`references/cross-section-consistency.md`): the golden thread (aim→conclusion), numeric reconciliation, terminology, claim-gradient, **dangling cross-references** (no pointer to a Supplementary/appendix item the paper doesn't actually contain), AND **Methods↔Results fidelity** — every metric reported in Results/Tables/figure legends must still be described in Methods. Corollary for Methods trimming: **never delete a method whose numeric output appears in Results/Tables/legends** (e.g. don't drop "Jacobian-based volume preservation" from Methods while Results reports the Jacobian error). This whole-manuscript step is the highest-value one and cannot be done section-by-section; skipping it is what lets seam and fidelity errors through.
6. **Deliver** in any of the three forms below (the user usually wants Output 2 + Output 3 together).

**Output 1 — Markdown revision report:** (1) one-line study-type classification; (2) a findings table (section · offending text · failed check · severity · suggested rewrite); (3) the cross-section thread map and any breaks; (4) a short prioritized revision checklist. Keep numbers and citations untouched.

**Output 2 — Tracked-changes revised `.docx`** (edits applied in the manuscript itself). Rewrite **boldly, concisely, and in the exemplars' voice** (see *Core principles* above): recast whole sentences and openings, trim wordiness, aim for **net fewer words**. **Never fabricate** — every number in an edit must be lifted verbatim from somewhere in the manuscript; anything that needs a number or detail the source genuinely lacks (unreported event rates, CIs, blinded-read specifics) becomes a **comment**, not an invented insertion. Apply with the bundled `scripts/apply_tracked_changes.py` — it protects fields/cross-references and guarantees that rejecting all changes restores the original exactly.

Pipeline (needs the `docx` skill's `unpack.py`/`pack.py`):
```bash
python <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/
python <this-skill>/scripts/apply_tracked_changes.py unpacked/ edits.json --author "Claude"
python <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx
```
Build `edits.json` from the findings — a list of `{"type":"replace","find":"…","replace":"…"}`, `{"type":"insert_after","find":"…","insert":"…"}`, or `{"type":"comment","find":"…","comment":"…"}`. Each `find` is verbatim source text **within one paragraph**; use `[brackets]` for any number not in the source. For a long manuscript, generate the edits with per-section agents plus an adversarial pass, then apply. Verify with `pandoc --track-changes=all manuscript_revised.docx`.

**Edit mechanics — avoid seam errors (this is the failure mode that bites):**
- A `find` must start AND end at a sentence or clause boundary, and must **include any leading connective the rewrite changes or drops** ("By contrast", "However", "Therefore"). Anchoring after the connective orphans it — e.g. find "contrast, MeVO…" → "By In the MeVO…".
- A `replace` must be a **grammatically complete** unit that, substituted in place (prefix + replace + suffix), yields a clean, complete sentence — no dropped verbs, no comma-splices ("…cross-validation, combined-model discrimination was AUC…" is broken; keep the verb: "…left discrimination essentially unchanged (…)").
- `insert_after` text must not glue to the anchor — never anchor immediately after a citation superscript, and keep a separating space (the script auto-spaces, but check), e.g. avoid "neuroscience.30-31These findings…".
- **Verification MUST include a seam/grammar pass, not just number-checking:** for every edit, substitute it into the surrounding text and confirm the whole sentence is grammatical and the joins read cleanly; reject or repair otherwise.

**Output 3 — Chinese rationale `.docx` (《修改理由》)** — a reviewer-/supervisor-facing explainer of every edit. Write it in **pure Chinese**, two short lines per edit:
> **改动**：用一句中文转述把什么改成了什么（不要贴英文整句）。
> **理由**：1–2 句中文，点明对应的临床写作原则；涉及数字注明原文出处（行号/表号）。

Keep only unavoidable term abbreviations (AUC, mRS, trial names…) — no full English sentences (the user finds bilingual mixing hard to read). Group by IMRaD section; put any `comment`-type items under a 「### 建议补充（批注）」 subheading. Save the rationale as Markdown (`#` title, `##`/`###` subheadings, body lines, inline `**bold**`), then format it to Word with the bundled script:
```bash
python <this-skill>/scripts/build_rationale_docx.py 修改理由.md manuscript_修改理由.docx
```
The script enforces the required house format: **flat** (no heading/semantic styles — hierarchy only via size + bold), title 13 pt bold / subheading 11 pt bold / body 11 pt, line spacing 1.15, space-after 0.5 line, justified, Chinese in 宋体 and English/digits in Times New Roman, A4.

## Clinical vs basic-science — the contrast at a glance

| Dimension | Basic-science (avoid) | Clinical (do) |
|---|---|---|
| **Intro opening** | Molecular/mechanistic knowledge gap; a pathway or phenomenon studied for its own sake | Disease burden / epidemiology / standard-of-care limitation → funnel to a real-world clinical dilemma (incl. "residual burden despite proven treatment", or a limit of current imaging) |
| **The gap & aim** | "the mechanism is unknown"; aim = understand biology | Unmet *clinical/evidence/practice* need; aim = a decision ("which patients", "predict [endpoint]", "the prognostic/diagnostic value of [marker] for [endpoint]") |
| **Results** | Fold-changes, expression, dose-response, significance of mechanistic effects | Absolute event rate **with denominator** first; adjusted OR/HR **with 95% CI**; bedside cut-offs (ROC/Youden/AUC) or sensitivity/specificity vs a named reference standard; reader agreement (κ/ICC) |
| **Discussion landing** | Biological model / mechanism as the contribution | Restate finding clinically → benchmark named prior clinical series/RCTs → explicit **clinical-implications / management** paragraph; mechanism only as plausibility |
| **Conclusion** | Biological insight, mechanism novelty | Pragmatic, actionable (often a memorable plain statistic), hedged; for imaging add practicality ("simple, accessible, reproducible") |
| **Vocabulary** | pathway, signaling, expression, "first to elucidate the mechanism" | mRS/NIHSS/ASPECTS/TICI/sICH, independent predictor, risk stratification, sensitivity/specificity/AUC, index test/reference standard, real-world — measured and hedged |

## Quick diagnostic (the "too basic-science?" smell test)

Scan the draft for these. Each "no" is a fix. (Full, genre-aware 43-item version with caveats: `references/diagnostic-checklist.md`.)

- **Intro sentence 1** states disease burden / standard-of-care limitation / residual-burden-despite-treatment — *not* a molecular gap.
- **The aim** is a clinical, prognostic, or diagnostic *decision*. ("to investigate the **mechanism/biological role** of …" is the red flag; "to evaluate the **predictive/diagnostic value** of …" is fine.)
- **The gap** is "scarce / unclear / not reported / urgently needed" — not "the pathway is unknown".
- **Primary outcomes** are hard patient-centered endpoints (mRS, NIHSS, sICH, mortality, recurrence, technical/clinical success) — or, for an imaging marker, validated against a clinical endpoint or named reference standard.
- **Results lead** with an absolute event rate + denominator (e.g. `48/395, 12.2%`) before any inferential stat (or, for procedural/technique papers, the prespecified primary endpoint).
- **Every key association** carries effect size **+ 95% CI + exact P**, not a bare P or fold-change.
- **Prognostic markers** are turned into a bedside cut-off (Youden/AUC with CI); **diagnostic** ones report sens/spec/PPV/NPV/accuracy vs a named reference standard.
- **Subjective reads** (sICH, restenosis, ASPECTS, image quality) are blinded, independent, with inter-reader agreement (weighted κ / ICC) reported.
- **Cohort** described in design-appropriate clinical terms (consecutive patients + center; or parent-trial + registration number) with numbered inclusion/exclusion, IRB, and a flow diagram.
- **Outcomes anchored** to validated scales/classifications and their cut-offs (Heidelberg, NASCET/WASID, mTICI 2b-3 = success, mRS 0-2, ISR ≥50%).
- **Discussion** keeps mechanism subordinate and carries the contribution in an explicit clinical-implications/management paragraph, benchmarked against **named** prior series/RCTs.
- **Conclusion/Discussion** ends on a concrete management action or scan-interpretation instruction — not "biological understanding."
- **Limitations** are pragmatic, each tied to a clinical consequence, with named biases **and their direction**, plus a call for prospective/external confirmation.
- **Language** is hedged ("may/might/could/appear to") with at most one restrained "first study" claim and zero mechanism-novelty hype.
- **Title** names the endpoint/predictor/comparison + population ("Predictors of…", "Prognostic value of [marker] for [outcome] after [procedure]", "X vs Y") — not the technology/molecule alone.
- **Effect magnitude is interpreted clinically**, not just shown — is the effect big enough to change management; is a wide CI flagged; is a non-significant result framed as "not detected" rather than "no effect"? (see `references/effect-interpretation-and-reporting.md`)
- **Relative effects are paired with absolute risk** (and NNT/NNH where the design allows); no OR/HR/RRR reported alone in the Abstract or Conclusion.
- **Prediction-model / risk-score / cut-off papers** report calibration *and* discrimination and address internal validation/optimism (a cut-off derived and tested in one sample is optimistic) — TRIPOD expectations.
- **Figure legends & table footnotes are self-contained and clinical** — each names the endpoint + its cut-off, the test, and the cohort, expands abbreviations, and (for figures) tells the reader what to read off the panel; nothing forces a trip back to the text. (see `references/figures-tables-legends.md`)
- **Concision** — the key clinical message in the fewest plain words; engineering/method detail pushed to the supplement.
- **Results is interpretation-free** — numbers, comparisons, and outcomes only; NO narrative/editorial framing ("the central paradox", "tension", "the central question", "carry to the bedside", "strikingly", "intriguingly"). The *why* (paradoxes, implications) goes in the Discussion, never in Results.

## Reference map — what to load when

All files live flat in `references/`. They are large and detailed; load only what the task needs, never all at once.

**Foundation — load first, for any section:**
- `references/basic-writing-requirements.md` — academic-writing rules underneath the clinical voice (section roles incl. **Results = facts only / Discussion = interpretation**, paragraph craft, hedging, reporting basics; distilled from the academic-research-skills plugin). Obey these basics first, then layer the clinical voice. The Results-vs-Discussion boundary here is load-bearing.

**Drafting or rewriting a section — Mode A / Mode B:**
- `references/section-playbook.md` — the 8-section playbook (Title→Conclusion): clinical moves, pitfalls, verbatim exemplars, and variant notes across the three genres. **Read the relevant section before drafting/rewriting it.**
- `references/phrasebank.md` — 37 categories of verbatim, reusable framing phrases. Lift the *frame*, adapt the bracketed slots — never copy a sentence with its original numbers.
- `references/figures-tables-legends.md` — how to write figure legends/captions, figure & table titles, and table footnotes so they are self-contained and guide clinical interpretation (read before writing any display-item text).
- `references/domain-notes.md` — neurovascular/stroke + neuroimaging scales, statistics, and reporting-standard conventions (mRS, ASPECTS, TICI, PSM, STROBE/CONSORT/TRIPOD; index test/reference standard, κ, VIF, DeLong, Bland-Altman, Eur Radiol Key Points block, RCT conventions, etc.).

**Diagnosing "too basic-science":**
- `references/diagnostic-checklist.md` — the full 43-item checklist with genre caveats (incl. figure/legend, table-footnote, and concision checks).
- `references/contrast-table-full.md` — the detailed clinical-vs-basic-science contrast (the long-form of the table above), grounded with exemplars.
- `references/effect-interpretation-and-reporting.md` — interpreting effects clinically: significance vs magnitude/MCID, absolute risk & NNT, prediction-model/TRIPOD reporting, and methodological completeness.

**Whole-manuscript pass — Mode C, step 5:**
- `references/cross-section-consistency.md` — the golden-thread / coherence checks (aim→conclusion, numeric reconciliation, terminology, claim-gradient, Methods↔Results fidelity, and dangling cross-references).

## Hard rules

- **Never fabricate or alter data, statistics, or citations.** This skill changes framing, emphasis, and structure — not results. If a clinical number the framing needs (an OR, a CI, an event rate) is genuinely absent from the source, flag the gap to the user; do not invent it.
- **Match study type.** A diagnostic-accuracy paper should not be dressed in ROC/AUC it doesn't have; a procedural-comparative paper need not force an adjusted OR. The variant notes and checklist parentheticals say when a pattern does *not* apply.
- **Stay measured.** Clinical voice is hedged and decision-oriented, not hyped. Strip "novel/first-ever/elucidate the mechanism" framing.
- **Results states facts, not interpretation.** Report what was found (rates, effects, CIs) plainly; keep interpretive/narrative framing — "the central paradox", "tension", "the central question", "carry to the bedside", "strikingly" — OUT of Results. Paradoxes, mechanisms, and clinical implications belong in the Discussion. The **clinical-dilemma opener** and the **clinical-implications landing** are Introduction/Discussion moves only — never apply them to Results or Methods.
- **Don't copy exemplar sentences verbatim into a real manuscript.** They are style models; reuse the structure, not the content.
- **Don't fabricate methods or analyses.** A failed checklist item often means the study *didn't do* something (no calibration, no sensitivity analysis, no blinded read). That is a note to the author or a limitation to state — never license to invent an analysis, a reference standard, or a clinical implication the data don't support.
- **Don't cite a supplement (or appendix) the paper doesn't have.** Never point to a "Supplementary Methods/Table/Figure", an appendix, or "data not shown" unless the source manuscript actually contains it. When trimming pushes detail out of the main text, either keep it concise in-text or leave a comment for the author to add a supplement — do not invent the pointer. (This is the dangling-"Supplementary Methods" failure mode.)
- **Finished / submitted manuscripts: be conservative.** Preserve the author's voice and structure; edit only what genuinely fails a check; report rather than silently rewrite; keep numbers and citations untouched.
- **This skill does clinical *reframing*, not language polish.** It changes what the writing is *about* (center of gravity, framing, structure). For grammar, flow, and journal-style English use a language-polish skill (e.g. `nature-polishing`), and for AI-text smoothing `humanizer_academic` — run clinical reframing first, polish second. Don't duplicate their job.
