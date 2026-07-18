# Display items — self-contained figures, tables, legends

Rules for making every figure, table, legend, title, and footnote readable and clinically interpretable when extracted ALONE. Grep the anchor you need; never load whole. Distilled from a Nanjing neurovascular/stroke + neuroimaging group and landmark stroke RCTs.

## The self-containment contract {#contract}
Every display item, read in isolation, must name four things: the **endpoint + its cut-off + the test/estimator + the cohort (with n and analysis population)**. Then it must EXPAND its own abbreviations and RE-GLOSS every clinical scale's range + direction-of-meaning ("higher = worse"), even if Methods already did. A raw scale number or bare effect estimate is uninterpretable without these.

## Figure & table titles {#titles}
- Title = self-contained descriptor of WHAT the item shows, carrying the contrast + denominator, framed as evidence — never a result or a P value.
- Name the endpoint/characteristic (the patient thing), NOT the statistical object. Not "mRS distribution" / "odds ratio plot" → state in WHOM and at what TIMEPOINT.
- Name the item by clinical ROLE: Table 1 = who the patients were / comparability; outcome table = the answer.
- Pin the analysis population in EVERY RCT title and keep the three distinct: efficacy tables tagged intention-to-treat, safety table tagged safety population.
- Encode endpoint + timepoint + the STRATIFIER (what rows/columns split by) in the title, not just a column header.
- Correct: `Distribution of the Modified Rankin Scale Scores at 1 Year (Intention-to-Treat Population)`
- Correct: `Baseline Patient Characteristics and Procedural Characteristics of Intention-to-Treat Population`
- Correct: `Diagnostic performance of post-treatment DWI ASPECTS and infarction volume in predicting good outcomes at 90 days`

## Figure legends — general {#legends}
- Two-part unit: a declarative TITLE sentence (display type + endpoint + groups + population) THEN a decoding body telling the reader what to READ OFF the panel (panel-by-panel key tied to (A)(B)… letters, the quantitative readout, the take-home).
- Embed the statistical VERDICT inline: name the test and give the P (`P<0.001, log-rank test`); for diagnostic curves give the headline metric + 95% CI (`AUC is 0.72 (95% CI: 0.62–0.83; P < 0.01)`). State the metric, NOT the method/physics; keep mechanism out (→ Discussion) and the test-name detail out (→ Methods).
- Restate the single headline EFFECT ESTIMATE with its 95% CI and cut-off inside the legend. Never a bare estimate without CI + named test.
- Restate cohort, n, denominator, group definitions and strata cut-offs in the legend (`high-risk group (score 3–6)`).
- Re-gloss every scale's range + direction each appearance (`Scores on the modified Rankin scale range from 0 to 6, with higher scores indicating greater disability`); for ordinal mRS give the level-by-level bedside gradient anchored 0→6=death.
- Multi-panel: map each panel letter to its own subgroup/cohort AND its own test/P.
- DEFINE the shaded band explicitly so it isn't misread as IQR/range (`The shading represents the 95% CI.`).
- Every figure gets its own complete abbreviation key as the LAST element — decode every symbol used ANYWHERE in the figure, even graphic-only acronyms, even if a master glossary exists.
- Correct: `ROC curve was used to evaluate the predictive ability of baseline plasma D-dimer levels for symptomatic intracranial hemorrhage (area under the curve=0.774).`

## Comparison figures — flag the null {#null-flag}
- Pair the positive finding with the EXPLICIT null so the figure cannot be over-read; carry the pairwise contrast a table's single omnibus P cannot ("which group differs").
- Correct: `No significant difference was found in the proportion of patients with hemorrhagic transformation between these two groups (40.9% vs 59.4%; p = 0.130).`
- Do NOT report only the positive contrast; keep null/non-significant rows visible.

## Kaplan-Meier {#km}
- Include a `No. at risk` table by arm and timepoint beneath the curves, exposing shrinking denominators.
- Offload the actuarial readout (group-wise event-free/cumulative rates at each timepoint) into the caption so quotable numbers travel with the curve.
- Name the test + P inline; define the shaded band as 95% CI.

## Forest / subgroup plots {#forest}
- Orient for bedside reading: plain-language direction anchors flanking the line of no effect (`Control Better | Endovascular Thrombectomy Better`), a `P for interaction` column, and an off-scale-arrow note (`The arrow indicates that the confidence interval extends outside the graphed area`). Never bare `OR`/`RR` axis labels.
- List the EXACT adjustment covariate set inline, in the same order and IDENTICAL to the matching table footnote.
- Add the guardrail on every subgroup/forest figure: not-powered / no-multiplicity-correction / post-hoc (`Prespecified` in the title pre-empts data-dredging). Show CIs that cross 1 rather than suppressing them.

## ROC / diagnostic curves {#roc}
- Repeat the decision rule in the legend: AUC (with 95% CI and P), the optimal cut-off, and sensitivity/specificity at that cut-off; add the incremental-value test when combining predictors.
- Correct: `The AUC for ΔNWU is 0.682 (95% CI, 0.546–0.817; sensitivity, 71.1%; specificity, 74.0%).`

## Waterfall / stacked-bar / distribution {#stacked}
- For ordinal mRS, use the full distribution/stacked bar (through death=6), not a single dichotomized bar; gloss each level in the legend.
- Add a rounding note when percentages don't sum to 100 (`Percentages may not total 100 because of rounding.`).
- Disclose per-arm missing data with exact counts + the imputation/handling rule (`Data were missing for one patient… imputed using the 30-day score`).

## Representative-case figures {#case}
- Open with a one-line vignette in a fixed order: age + sex + clinical context + interval since procedure + exact vessel/segment.
- Walk panel-by-panel: modality + technique + finding + on-image annotation in parentheses (`c, arrowhead`; `white arrow`); embed concrete per-panel quantities (infarct volume, ASPECTS regions, perfusion volumes, HIR).
- Restate any ordinal grading scheme inline and map each panel letter to its grade with the verbal anchor re-quoted.
- CLOSE on the hard decision-relevant outcome — always the 90-day/3-month mRS (`The mRS score was 3 at 3 months`). Never end on the image finding (e.g. `mTICI 3`) alone.
- Pair a positive with a negative case on identical sequences; for diagnostic figures pair opposite error directions (one under-, one over-estimation); use `confirms` for the arbiter panel (`Digital subtraction angiography confirms…`). Do not cherry-pick confirmatory cases.
- Annotate ONLY panels containing a discrete lesion; leave by-definition-empty panels unmarked.

## Table footnotes {#footnotes}
- Fixed three-part scaffold: (1) data-format sentence with exception clause (`Data are reported as median (interquartile range [IQR]) unless otherwise indicated`); (2) ONE alphabetized run-on sentence expanding EVERY abbreviation THIS table uses (re-expand even if defined elsewhere); (3) a symbol key decoding any asterisk/superscript.
- Flag significance with a symbol on the row and decode it (`*Statistically significant.`) rather than bolding.
- Self-label each continuous ROW with its statistic + unit at the point of the cell (`Age (years), mean ± SD`; `D-dimer, median (IQR), mg/L`).
- Carry the ADJUSTMENT covariate set (quoted in full, identical wording/order to the matching figure legend) and name the estimator per outcome row (generalized OR for ordinal mRS shift; HR for death; mean difference for volume/NIHSS; RR/ARR for binary); state the direction rule so a ratio is interpretable.
- Pin the ENDPOINT + cut-off operationally next to the number, naming the classification/adjudicator (`Symptomatic intracranial hemorrhage was defined according to the Heidelberg bleeding classification…`).
- Re-gloss every scale's range + direction each table (scale-regloss doctrine, see `#contract`); put the exposure's operational definition in the footnote when the table must stand alone (`BMI is the weight in kilograms divided by height in meters squared`).
- Disclose missingness numerically, per variable/arm, with exact denominators; state the death-handling rule (`The worst possible score was assigned for patients who had died…`); use `NA, not applicable` and dashes for reference/inapplicable cells, never a blank or zero.
- Add the multiplicity caveat for secondary outcomes (`not adjusted for multiple comparisons… may not be used for hypothesis testing`); flag what NOT to conclude at a method-switch (e.g. RR not measurable at 0 events).

## Table 1 baseline conventions {#table1}
- Group rows by clinically meaningful blocks (Demographics / Clinical / Procedural); carry units + time windows in the row labels so each number is self-describing.
- When matching is used, show explicit BEFORE/AFTER balance (unmatched beside matched, asterisk disappearing after matching); quantify balance with SMD not baseline P; restate the balance cut-off in the footnote (`SMD ≤ 0.1 … considered significantly balanced`); show exactly the covariates entered into the PS model.
- Reprint denominators in every column header; embed per-cell n where data are missing (`n = 157`).

## CONSORT / STROBE / flow diagrams {#flow}
- Legend is a terse operational ledger: a one-line enrolment caption + the abbreviation glossary. Put the full quantitative eligibility filter and itemized, clinically-labelled exclusion counts into the diagram boxes/footnote (mirroring the inclusion criteria), keeping Methods prose clean.
- Correct box run: `191 excluded / 139 did not meet inclusion or met exclusion criteria / 47 time from stroke onset to randomisation >6 h / …`.
- The flow figure carries the auditable screening-to-inclusion funnel so generalizability is checkable without the running text.

## What to offload to display items vs main text {#offload}
- Tables carry the audit trail (exact n(%), IQR, OR/HR, 95% CI, P, Sens/Spec/PPV/NPV); prose narrates only the headline claim + decision-relevant numbers.
- Assign each item a DISTINCT clinical-decision job: Table 1 = who the patients were; evaluation table = is the finding trustworthy/visible; outcome table = the answer / what predicts a bad result.
- Keep MECHANISM and biomarker data OUT of display items — push to prose/appendix so figures/tables stay patient-outcome-centred.
- Park the cut-off-selection grid (each threshold with full Sens/Spec/PPV/NPV ± CI + AUC) in a table; defend only the chosen threshold in prose.
- Report mRS BOTH ways: dichotomized clinical cut-points in the outcome table AND the ordinal SHIFT distribution in a figure.
- Statistical defensiveness (multiplicity, missing-data accounting, adjustment sets, p-sidedness) lives in Methods + footnotes, leaving Results/Discussion prose confident and patient-centred.

## Project calibration {#calibration}
Prefer SHORTER, concept-focused legends/footnotes with confident main text. Borrow the decision-relevant elements (endpoint definition, cut-off, named classification, direction anchors, adjustment intent, population tag) but NOT the Lancet-IPD defensive per-cell density (full adjustment set + p-sidedness + per-cell missingness + collinearity exclusions in every legend). Emulate the patient-facing self-contained item over exhaustive per-cell statistical disclosure where a choice must be made.

## Quick Search Targets {#grep}
```
rg -n -A4  "#contract"   references/display_items.md   # the 4-thing self-containment rule
rg -n -A9  "#legends"    references/display_items.md   # general figure-legend moves
rg -n -A5  "#null-flag"  references/display_items.md   # pair positive with explicit null
rg -n -A4  "#forest"     references/display_items.md   # direction anchors + adjustment set + guardrail
rg -n -A3  "#roc"        references/display_items.md   # AUC + cut-off + Se/Sp decision rule
rg -n -A5  "#case"       references/display_items.md   # representative-case template, close on mRS
rg -n -A11 "#footnotes"  references/display_items.md   # 3-part footnote scaffold
rg -n -A4  "#flow"       references/display_items.md   # where CONSORT/STROBE exclusions go
rg -n -A4  "#titles"     references/display_items.md   # title names endpoint+population, not the stat
```
