# Structure contract — skeleton, claim-gradient, coherence

Higher-altitude companion to `voice_principles.md` (which gives per-move phrasing). This file says **what goes where, how strongly to claim it, and how to keep the paper coherent**. Grep the anchor you need; never load whole.

## Step 0 — classify before writing {#classify}
Fix two axes, because the rules branch on both:
1. **study_type** — `interventional-cohort` · `prognostic-predictor` · `diagnostic-accuracy` · `imaging-technique` · `procedural-comparative` · `rct` · `rct-posthoc`. (Don't force ROC/AUC onto a binary diagnostic read, or an adjusted OR onto a procedural comparison.)
2. **genre** — **A** clinical-observational · **B** imaging-biomarker/technique · **C** randomized-trial voice. Mount that genre's row in `voice_fingerprint.md` and its VARIANT moves in `voice_principles.md`.

Single-centre observational → A. Imaging marker/technique is the star → B. Randomized trial or its post-hoc → C. See `voice_fingerprint.md #genre-contrast`.

## Section skeleton {#skeleton}
IMRaD order is INVARIANT across A/B/C; the moves below are the spine (slugs → `voice_principles.md`). VARIANT items note the genre.

- **Title** → `#title-endpoint-population-design-subtitle` (+ A/B `#title-predictor-first-noun-phrase`). Endpoint/predictor/comparison + population; design subtitle after a colon (A/C almost always; C appends the trial name).
- **Abstract** → journal-labeled structure `#abstract-structured-labels-match-journal`; open Results comparatively, define outcomes inline, conclusion restates direction in words.
- **Introduction** (funnel): cited-epidemiology opener `#opener-hard-cited-epidemiology` → (C/B) residual-burden-despite-treatment → named prior actors + **specific** gap `#gap-hard-specific-negation` → aim anchored to the named cohort `#aim-anchored-to-named-cohort`. Aim verb form is a per-paper VARIANT (`#aim-form-genre-divergence`), not a genre law.
- **Methods**: cohort provenance in one breath `#cohort-provenance-one-breath` → terse IRB/consent → numbered inclusion/exclusion with clinical thresholds → endpoints named-classification + inline gloss `#endpoints-named-classification-with-inline-gloss` → blinded adjudication + reader-experience hierarchy → stats distribution-first. VARIANT: C stacks a trial-design adjective string; B bursts imaging parameters in parentheses. **Methods is passive on purpose** (`voice_fingerprint.md #passive`).
- **Results** (facts only, no editorial): enrollment/flow first (do NOT lead a sentence with the bare rate) → count-then-percent-with-denominator → central tendency + dispersion → adjusted effect + 95% CI + exact P in one parenthetical → flat non-significance (no "trend toward") → ordering context→contrast→adjusted. VARIANT: A predictor currency (independent OR/HR); B accuracy/agreement (AUC, κ, cut-off); C arm-contrast effect hierarchy (primary → secondary → safety).
- **Discussion** (interpretation): restate own finding first → benchmark **named** prior series/RCTs → explicit management paragraph (A/C) or utility-of-marker framing (B) → mechanism subordinate & hedged (A/C) / central & detailed (B) → limitations with named bias + **direction** → call for external/prospective validation → pragmatic hedged conclusion. Quantify effect in patient terms (C: NNT/absolute pp; A: occasional high-vs-low-risk %).

## Claim-gradient — how strongly to claim {#claim-gradient}
Calibrate the top-line to the design; keep it monotonic (Abstract ≈ Conclusion, never escalating).
- **A (observational):** hypothesis-generating. Verbs: "associated with", "independent predictor of", "may favor". A single-centre retrospective cohort is **never** "practice-changing". Findings are associations, not causes; name the adjusting model.
- **B (imaging):** hypothesis-generating, openly hedged ("might/may/could"). State a modest AUC (0.68–0.76) honestly — no "excellent/robust". Frame the marker as a **surrogate** with comparable performance to a harder reference, pitched on workflow (not novelty).
- **C (RCT), bimodal by result:**
  - *Positive primary outcome* → state it **flatly and strongly**, first Discussion sentence, no hedge ("EVT led to better functional outcomes than medical management"). Translate to NNT / absolute percentage-point difference **benchmarked** to an external anchor.
  - *Null / non-inferiority-not-shown* → **reframe** to a decision/guideline message or a design lesson ("thrombolysis should not delay endovascular treatment"), never "endpoint not met but valuable insights".
  - Post-hoc/subgroup → label exploratory, "not for definitive hypothesis testing", note no multiplicity correction.

## Cross-section consistency pass — MANDATORY {#cross-section}
Not doable section-by-section; run once over the whole manuscript before delivery.
1. **Golden thread.** The aim (end of Intro) → primary endpoint (Methods) → lead Results number → Conclusion answer are the *same question*, in the same terms. No orphan aim, no conclusion the Results don't support.
2. **Numeric reconciliation.** Every number in Abstract = Results = Tables = figure legends (n, %, OR/HR, CI, P). No drift.
3. **Methods↔Results fidelity.** Every metric reported (Results/Tables/legends) is defined in Methods; every method with a numeric output appears in Results. Don't trim a method whose output is reported (e.g. don't drop "Jacobian volume preservation" from Methods while Results reports the Jacobian error).
4. **Claim-gradient monotonic.** Conclusion strength ≤ what the design licenses (see `#claim-gradient`); Abstract conclusion == Discussion conclusion.
5. **Terminology.** One term per concept throughout (pick "futile recanalization" *or* "poor outcome despite reperfusion", not both interchangeably).
6. **No dangling cross-references.** Don't cite a Supplementary Table/appendix/"data not shown" the manuscript doesn't contain.

## Quick Grep Targets {#grep}
```
grep -A6  "#classify"       references/structure_contract.md   # study_type x genre routing
grep -A12 "#skeleton"       references/structure_contract.md   # IMRaD spine + move slugs
grep -A12 "#claim-gradient" references/structure_contract.md   # how strongly to claim, by genre
grep -A10 "#cross-section"  references/structure_contract.md   # mandatory whole-manuscript pass
```
