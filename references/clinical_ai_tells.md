# Clinical AI-tell checks

Run this after clinical framing and numeric reconciliation. Do not optimize prose to evade a detector;
remove patterns that weaken scientific meaning.

## Positive signals to preserve {#positive}

- Section-specific behavior: factual Results, interpretive Discussion, reproducible Methods.
- Recoverable denominators, named effect measures, uncertainty, time points, and endpoint definitions.
- Specific comparison with prior evidence rather than vague citation clusters.
- Uneven but purposeful rhythm; short sentences carry content rather than rhetorical attitude.
- Limitations tied to the inference they threaten.
- Concrete clinical meaning that stays below the evidence boundary.

For neurovascular work, use the measured distributions in `voice_fingerprint.md`. Do not treat those
specialty measurements as universal.

## Rewrite these patterns {#tells}

- Editorial connectives at paragraph heads: `Moreover`, `Furthermore`, `Additionally`, `Notably`,
  `Importantly`, or `Consequently` when they add no logic.
- Rhetorical fractions without denominator, such as `nearly one in five`, used as decoration.
- Adjective piles such as `simple, accessible, reproducible, cost-effective, and widely available`.
- Content-free implications: `important clinical implications`, `may inform decisions`, or `warrants
  further investigation` without naming the decision or missing evidence.
- Vague attribution: `several studies`, `it is well known`, or `the literature suggests` when the
  manuscript contains specific sources.
- Hype: `paradigm shift`, `revolutionary`, `pivotal role`, `game-changing`, or unsupported `first` claims.
- Causal verbs applied to observational associations.
- Hedge stacking or hedging an observed Result.
- Mechanism paragraphs that never return to the population, endpoint, or management question.
- British/American spelling drift relative to the target journal.

## Too-polished failure mode {#too-polished}

- Aphoristic paragraph endings that sound like an essay rather than a clinical paper.
- Repeated antithesis or manufactured symmetry in every paragraph.
- Exactly balanced, generic limitation lists that could fit any manuscript.
- Smoothing away arm counts, event counts, windows, thresholds, and uncertainty.
- Replacing named trials or studies with vague attribution.
- Moving a statistic into a section where the source manuscript did not report it.
- Removing defensible non-native phrasing until every sentence has the same cadence.

## Humanizer boundary {#humanizer}

If an academic-humanizer skill is available, apply it only after this clinical pass:

- preserve intentional passive voice in Methods;
- preserve clinical-standard terms and endpoint labels;
- preserve section-bound hedging;
- preserve every number, citation, unit, and statistical symbol;
- reject edits that change the claim gradient or invent fluency around missing evidence.

## Quick search targets {#search}

```bash
rg -n -A12 "#tells" references/clinical_ai_tells.md
rg -n -A8 "#too-polished" references/clinical_ai_tells.md
rg -n -A8 "#humanizer" references/clinical_ai_tells.md
```
