# Effect Interpretation & Reporting — Making Numbers Read Clinical

The core skill already enforces *reporting* numbers correctly (absolute rate + denominator; effect size + 95% CI + exact P). This file covers *interpreting* them clinically — the move that separates a clinician's paper from a statistician's table.

Apply where relevant to the study design. **Do not bolt these onto a study that did not measure them, and never invent the underlying numbers.** When one of these is missing from a finished manuscript, it is usually a note to the author or a limitation to state — not license to fabricate an analysis.

## 1. Clinical vs statistical significance
- A small P is not clinical importance. Once significance is established, interpret the *magnitude*: is the effect large enough to change management? Say so explicitly.
- Anchor to a minimal clinically important difference (MCID) where one exists for the outcome.
- A wide confidence interval undercuts clinical usability even when "significant" (e.g., OR 74.7, 95% CI 4.6–1206 tells a clinician almost nothing about the true effect). Flag it rather than quoting the point estimate as if precise.
- A non-significant result is not "no effect," especially if underpowered. Frame as "no significant difference was detected," and note the event count / power as a limitation.

## 2. Absolute vs relative effects, NNT/NNH
- Relative measures (OR/HR/RRR) exaggerate apparent benefit; always pair them with the absolute risks (rates per group) and, where the design supports it, the absolute risk difference.
- For an actionable intervention or threshold, translate into number-needed-to-treat (NNT) or number-needed-to-harm (NNH) — the most decision-usable form of an effect.
- Never report a relative effect alone in the Abstract or Conclusion.

## 3. Prediction-model / risk-score / cut-off papers (TRIPOD)
When the deliverable is a predictor model, risk score, or diagnostic cut-off, the expected reporting standard is TRIPOD. Verify:
- **Discrimination AND calibration** are both reported (AUC/C-statistic + a calibration assessment such as a calibration plot or Hosmer–Lemeshow). Discrimination alone is incomplete.
- **Internal validation / optimism correction** (bootstrap or cross-validation): a cut-off or model derived and tested in the *same* sample is optimistically biased. Report apparent vs validated performance, or flag the absence as a limitation.
- If external validation is absent, name it as the key next step.

## 4. Methodological-completeness moves clinical reviewers expect
- Missing data: how much, and how handled (complete-case vs imputation) — not silently dropped.
- Sensitivity analyses for key modeling choices; for time-to-event with deaths, competing-risks where appropriate.
- Loss to follow-up reported with the flow diagram.

## 5. Anchor to practice, not only to trials
- Benchmark against named clinical practice guidelines / standard-of-care documents, not only prior RCTs, and state where the finding confirms, refines, or challenges current recommended practice.
