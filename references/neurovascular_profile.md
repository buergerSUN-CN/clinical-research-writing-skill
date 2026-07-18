# Neurovascular and stroke profile

Mount this profile only for stroke, neuroimaging, or neurointerventional manuscripts. It is distilled
from 32 exemplars: 13 observational/procedural, 7 imaging, and 12 randomized or trial-secondary
papers. The corpus supports specialty calibration, not universal clinical-writing norms.

## Vocabulary and endpoint control {#vocabulary}

- Define modified Rankin Scale thresholds and assessment time points rather than writing only
  `favorable outcome`.
- Distinguish recanalization from reperfusion and state the named grading system and successful-grade
  threshold used by the study.
- Expand NIHSS, ASPECTS, hemorrhage classifications, imaging parameters, and vessel territories on
  first relevant use according to journal style.
- Keep technical success, tissue reperfusion, symptomatic hemorrhage, mortality, and functional
  outcome as separate endpoints.
- Read `domain_notes.md` for specialty definitions; never import a threshold absent from the source.

## Clinical reasoning habits {#reasoning}

- Frame residual disability after technically successful reperfusion as a patient-outcome problem,
  not as a molecular-mechanism paper.
- For a biomarker, distinguish bedside availability, incremental information, and actual clinical
  utility. Do not claim treatment selection value without decision-impact evidence.
- For procedural comparisons, balance workflow or access advantages against complications and
  patient outcomes.
- For trial-secondary analyses, tie the inference to the parent trial while marking the analysis as
  secondary.

## Measured fingerprint {#fingerprint}

Use `voice_fingerprint.md` and `check_draft.py --profile neurovascular` only as a diagnostic check.
The corpus shows:

- intentionally passive Methods, especially in imaging studies;
- far more hedging in Discussion than Results;
- dense denominator/effect/uncertainty reporting in Results;
- near-zero em-dash use in observational and imaging papers;
- varied sentence rhythm rather than uniformly polished cadence.

Do not force a manuscript toward every median. Flag large deviations, then judge whether journal
style, specialty, section length, or the source author's voice explains them.
