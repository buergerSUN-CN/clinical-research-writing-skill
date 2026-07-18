# Reporting checklists — per-item audit

Map study_type to checklist(s), then audit a draft item by item.
Each item: **reported / partial / missing / N/A**, with the location in the
draft (or what's absent). Severity: ■ high (likely desk-reject) · ■ medium
(reviewer will flag) · ■ low (nice-to-have).

**How to audit.** Load the draft, identify the study_type (see `structure_contract.md #classify`),
find the checklist(s) below, then iterate — one sentence per item, one verdict.
Group items the draft passes cleanly under one summary line; call out every
missing/partial item with its severity and a one-line fix suggestion. At the
end, summarize: total items · passed · partial · missing · N/A.

## STROBE — observational studies (cohort / case-control / cross-sectional) {#strobe}

Covers: interventional-cohort, prognostic-predictor, procedural-comparative.
Source: STROBE Statement (von Elm et al., 2007/2014).

### Title & Abstract
| # | item | check |
|---|---|---|
| 1a | Study design in title or abstract ("cohort" / "case-control" / "cross-sectional") | title or abstract must name the design |
| 1b | Structured abstract with balanced summary of what was done and found | check for Background/Methods/Results/Conclusions labels or equivalent |

### Introduction
| # | item | check |
|---|---|---|
| 2 | Scientific background and rationale | disease burden / standard-of-care gap |
| 3 | Specific objectives, including any pre-specified hypotheses | aim sentence; if no pre-specification stated, flag ■medium |

### Methods
| # | item | check |
|---|---|---|
| 4 | Study design, setting, locations, relevant dates (enrolment, follow-up, data collection) | single-centre name + enrolment period + follow-up window |
| 5 | Eligibility criteria, sources of participants, methods of selection (consecutive / convenience) | "consecutive patients" + numbered inclusion/exclusion |
| 6a | All outcomes, exposures, predictors, confounders; diagnostic criteria if applicable | named scale + cut-off for each endpoint |
| 6b | Any changes to outcomes after the study started, with reasons | if none stated, flag ■low |
| 7 | How the study size was arrived at | ■high if missing: "all eligible patients during enrolment period" or formal power calculation |
| 8 | How quantitative variables were handled in analyses (continuous / categorical / cut-offs) | ROC/Youden for cut-off derivation; if using an existing threshold, cite it |
| 9 | All statistical methods, including those to control for confounding | multivariable model named; PSM/IPTW if used; list covariates |
| 10a | How missing data were addressed | if none stated, flag ■medium |
| 10b | If applicable, how loss to follow-up was addressed | ■medium if follow-up data exist but no loss-to-follow-up statement |
| 11 | How matching (PSM) was performed, including caliper and matching ratio | if PSM: caliper + ratio must be reported |
| 12a | Sensitivity analyses | ■medium if none; post-hoc subgroup can serve |
| 12b | Any methods to examine subgroups or interactions | if tested, must report interaction p; flag ■high if claimed but only within-stratum p shown |

### Results
| # | item | check |
|---|---|---|
| 13a | Numbers of individuals at each stage (flow diagram) | ■high if no participant flow anywhere; figure or text |
| 13b | Reasons for non-participation at each stage | if exclusions mentioned, must give reasons |
| 13c | Participant flow diagram (highly recommended) | ■medium if absent; text is minimum, figure is recommended |
| 14a | Characteristics of participants (demographic, clinical) and information on exposures and confounders | Table 1 required |
| 14b | Number of participants with missing data for each variable | ■medium if missing data exist but not quantified per variable |
| 14c | Follow-up time and total person-time (cohort) | mean/median follow-up + IQR |
| 15 | Outcome events and summary measures over time | absolute n/N (%) for each group or stratum |
| 16a | Unadjusted estimates + confounder-adjusted estimates with precision (95% CI) | univariate OR + adjusted OR both reported; ■high if only adjusted |
| 16b | If continuous variables categorised, report category boundaries and cut-point rationale | ■medium if cut-off used but derivation not stated |
| 16c | Translate relative risk to absolute risk where meaningful | ■low; (adjusted) OR → absolute event rates per stratum |
| 17 | Other analyses: subgroups, interactions, sensitivity | report interaction p for any claimed subgroup difference |

### Discussion
| # | item | check |
|---|---|---|
| 18 | Summarise key results with reference to study objectives | first Discussion paragraph |
| 19 | Discuss limitations: potential bias, imprecision, multiplicity | ■high if no limitations stated; each must name direction of bias |
| 20 | Interpretation in context of other evidence, cautiously (no causal language if observational) | "associated with" not "causes"; named prior studies |
| 21 | Generalisability (external validity) | single-centre → flag "requires external validation" |

### Other
| # | item | check |
|---|---|---|
| 22 | Funding source and role of funders | ■low (but mandatory at many journals) |

---

## CONSORT 2010 — randomised trials {#consort}

Covers: rct.
Source: CONSORT 2010 Statement (Schulz et al., 2010).

### Title & Abstract
| # | item | check |
|---|---|---|
| 1a | Identified as randomised trial in title | "randomised" must appear in title |
| 1b | Structured summary of trial design, methods, results, conclusions | trial registration number in abstract |

### Introduction
| # | item | check |
|---|---|---|
| 2a | Scientific background + rationale | residual-burden-despite-treatment / standard-of-care limitation |
| 2b | Specific objectives or hypotheses | aim with hypothesis direction (superiority / non-inferiority) |

### Methods
| # | item | check |
|---|---|---|
| 3a | Trial design (parallel / factorial / crossover), allocation ratio | must state design type and ratio |
| 3b | Important changes to methods after trial commencement, with reasons | if none stated, ■low |
| 4a | Eligibility criteria | numbered inclusion/exclusion |
| 4b | Settings and locations where data were collected | multicentre: number + country |
| 5 | The interventions for each group, with sufficient detail to replicate | dose / device / procedure / sham detail |
| 6a | Completely defined pre-specified primary and secondary outcome measures | named scale + cut-off + assessment time point |
| 6b | Any changes to outcomes after the trial started, with reasons | ■low if none stated |
| 7a | How sample size was determined | power, α, β, expected effect — ■high if missing |
| 7b | Interim analyses and stopping guidelines | if applicable; if DSMB mentioned, must state rules |
| 8a | Method used to generate the random allocation sequence | block size / stratification factors |
| 8b | Type of randomisation; details of any restriction (blocking, stratification) | must name stratification variables |
| 9 | Mechanism used to implement the random allocation sequence | central web-based / sealed envelopes |
| 10 | Who generated the sequence, who enrolled participants, who assigned | if not stated, ■medium |
| 11a | Blinding of participants and personnel | "single-blind" / "double-blind" + who |
| 11b | Description of similarity of interventions (if sham-controlled) | sham procedure detail |
| 12a | Statistical methods for primary and secondary outcomes | ITT / per-protocol / as-treated |
| 12b | Methods for additional analyses (subgroup, adjusted) | interaction p for subgroups |

### Results
| # | item | check |
|---|---|---|
| 13a | Participant flow (CONSORT diagram strongly recommended) | ■high if absent; numbers screened→randomised→allocated→analysed |
| 13b | Losses and exclusions after randomisation, with reasons | every post-randomisation exclusion accounted for |
| 14a | Dates defining recruitment and follow-up periods | enrolment start-to-end + follow-up window |
| 14b | Why the trial ended or was stopped | if stopped early, detailed reason |
| 15 | Baseline demographic and clinical characteristics per group (Table 1) | Table 1 with between-group comparison |
| 16 | Numbers analysed per group and whether ITT | denominator per arm for every analysis |
| 17a | Results for each primary and secondary outcome, with effect size and precision | treatment effect + 95% CI + exact P |
| 17b | Binary outcomes: present both absolute and relative effect sizes | ■high if only OR/RR reported without absolute rates |
| 18 | Any additional analyses (subgroup, adjusted) | pre-specified vs exploratory distinction |
| 19 | All important harms or unintended effects per group | safety endpoint table |

### Discussion
| # | item | check |
|---|---|---|
| 20 | Trial limitations: sources of potential bias, imprecision, multiplicity | named biases + direction |
| 21 | Generalisability (external validity, applicability) | ethnicity/geography/stroke-subtype caveats |
| 22 | Interpretation consistent with results, balancing benefits and harms | NNT / absolute risk framing |
| 23 | Registration number and name of trial registry | ■high if missing |
| 24 | Where the full trial protocol can be accessed | ■medium if missing |
| 25 | Sources of funding and other support; role of funders | mandatory at most journals |

---

## STARD 2015 — diagnostic accuracy studies {#stard}

Covers: diagnostic-accuracy.
Source: STARD 2015 (Bossuyt et al., 2015).

### Title & Abstract
| # | item | check |
|---|---|---|
| 1 | Title/abstract identifies as diagnostic accuracy study; at least one measure of accuracy (sensitivity, specificity, AUC, predictive values) | "diagnostic accuracy", "sensitivity", "AUC" or "predictive value" in title or abstract |
| 2 | Structured abstract with Background/Methods/Results/Conclusions | follow journal format |

### Introduction
| # | item | check |
|---|---|---|
| 3 | Scientific and clinical background, including the intended use and clinical role of the index test | what gap in current diagnostic pathway the index test fills |
| 4 | Study objectives: test comparisons, intended clinical application | specify whether test replacement, triage, or add-on |

### Methods
| # | item | check |
|---|---|---|
| 5 | Study design: data collected before (prospective) or after (retrospective) the index test and reference standard were performed | retrospective vs prospective; ■high if not stated |
| 6 | Eligibility criteria | how participants were identified and selected |
| 7 | On what basis potentially eligible participants were identified (symptoms, prior tests, registry) | consecutive vs convenience |
| 8 | Where and when participants were identified (setting, location, dates) | single-centre, enrolment period |
| 9 | Whether participants formed a consecutive, random, or convenience series | "consecutive" must be stated or flagged missing |
| 10a | Index test described in sufficient detail to allow replication | acquisition parameters / device / protocol |
| 10b | Reference standard described in sufficient detail to allow replication | ■high: what is the ground truth and who determined it |
| 11 | Rationale for choosing the reference standard (if alternatives exist) | why this reference over others |
| 12a | Definition of and rationale for test positivity cut-offs or result categories of the index test | ROC/Youden or established cut-off |
| 12b | Definition of and rationale for test positivity cut-offs or result categories of the reference standard | named criteria for positive reference standard |
| 13a | Whether clinical information and reference standard results were available to the index test readers | blinded? |
| 13b | Whether clinical information and index test results were available to the reference standard readers | blinded? |
| 14 | Methods for estimating and comparing measures of diagnostic accuracy | sensitivity, specificity, PPV, NPV, AUC; DeLong for AUC comparison |
| 15 | How indeterminate index test or reference standard results were handled | ■medium if not addressed |
| 16 | How missing data on the index test and reference standard were handled | ■medium if not addressed |
| 17 | Any analyses of variability in diagnostic accuracy (subgroups, reader variability) | if multiple readers: inter-reader agreement (κ / ICC) |
| 18 | Intended sample size and how it was determined | ■medium if no sample-size justification |

### Results
| # | item | check |
|---|---|---|
| 19 | Flow of participants (flow diagram strongly recommended) | screened→eligible→index test→reference standard→analysed |
| 20 | Baseline demographic and clinical characteristics | Table 1 |
| 21a | Distribution of disease severity in those with the target condition | if applicable |
| 21b | Distribution of alternative diagnoses in those without the target condition | if applicable |
| 22 | Cross-tabulation of index test against reference standard, or distribution of index test across reference standard categories | 2×2 table or equivalent |
| 23 | Estimates of diagnostic accuracy and their precision (95% CI) | sens, spec, PPV, NPV, AUC, LR+/- — each with 95% CI |
| 24 | Any adverse events from performing the index test or reference standard | ■low (often N/A for imaging) |

### Discussion
| # | item | check |
|---|---|---|
| 25 | Study limitations: potential sources of bias (spectrum, verification, imperfect reference standard) | ■high if none stated |
| 26 | Clinical applicability: discuss the intended use and clinical role of the index test | what patient population would be affected, how the result changes management |
| 27 | Registration number and registry name if prospectively registered | ■low (if prospective) |
| 28 | Where the full study protocol can be accessed | ■low |
| 29 | Sources of funding | ■low |

---

## TRIPOD — prediction model studies {#tripod}

Covers: prognostic-predictor (model development or validation).
Source: TRIPOD Statement (Collins et al., 2015).
Items below are the Type 1a (development) core; if the paper is external validation,
audit against TRIPOD Type 3/4 entries instead.

### Title & Abstract
| # | item | check |
|---|---|---|
| 1 | Title: identify as a prediction model study; report the target population and outcome | "predictors of…" / "prognostic value of…" / "nomogram for…" in title |
| 2 | Abstract: structured summary of objectives, design, setting, participants, sample size, predictors, outcome, model-building strategy, performance (discrimination + calibration), and (if validation) validation strategy | discrimination (AUC / C-statistic) AND calibration must both appear |

### Introduction
| # | item | check |
|---|---|---|
| 3a | Background: the clinical context and rationale for developing/validating a multivariable prediction model | disease burden + residual-prediction gap from existing models |
| 3b | Specific objectives, including whether the study is model development, validation, or both | must explicitly say "development" / "validation" / "both" |

### Methods
| # | item | check |
|---|---|---|
| 4a | Source of data: cohort / registry / RCT / nested case-control | parent study name + design + enrolment period |
| 4b | Key study dates: start of enrolment, end of enrolment, end of follow-up (if applicable) | exact dates or at least month/year |
| 5a | Participant eligibility criteria | numbered inclusion/exclusion |
| 5b | Details of treatments received, if relevant | especially if predicting treatment-dependent outcomes |
| 6a | Outcome: clearly defined, with any pre-specified hypotheses about how the outcome was determined | named scale + cut-off + assessment time point |
| 6b | If outcome assessed blinded to predictors | blinded adjudication status |
| 7a | Candidate predictors: how they were defined and measured, including timing | timing relative to index event |
| 7b | If predictors assessed blinded to outcome and other predictors | ■low |
| 8 | Sample size: how the study size was arrived at | EPV (events per variable) or formal sample-size calculation; ■high if no justification |
| 9 | Missing data: how missing data were handled (complete-case / imputation) | ■medium if missing data exist but method not stated |
| 10a | Model-building: how predictors were handled (continuous/categorised), variable selection method (if any) | univariate screen→multivariable; ■high if stepwise selection used without shrinkage |
| 10b | For each variable, how it was treated (continuous, categorical, or transformed) | cut-offs from Youden / ROC or prior literature |
| 10c | Non-linearity assessment, interactions | ■medium if continuous variables assumed linear without testing |
| 10d | Shrinkage of predictor weights, if performed | ■low (often absent in single-centre papers) |
| 11 | Internal validation: bootstrap / cross-validation / split-sample | ■high if model is the paper's contribution and there is NO internal validation |
| 12 | Model specification: the full prediction model presented (regression coefficients, intercept, baseline survival) | must present coefficients or a score/nomogram; ■high if AUC is the only output |
| 13 | Model performance: discrimination (C-statistic / AUC) AND calibration (calibration plot / Hosmer-Lemeshow / calibration-in-the-large / calibration slope) | ■high: AUC alone, no calibration reported |
| 14 | If validating an existing model, the original model specification and how performance was assessed | for validation studies only |

### Results
| # | item | check |
|---|---|---|
| 15a | Participant flow and number of participants | screened→eligible→included (flow diagram strongly recommended) |
| 15b | Characteristics of participants, including number of participants with missing data | Table 1 |
| 16 | Number of participants with the outcome, number of outcome events per candidate predictor | events count for each predictor category |
| 17 | The developed model presentation: regression coefficients / OR / HR with 95% CI, intercept, any penalty factor | full model specification in Results or an appendix |
| 18 | Model performance: discrimination + calibration | AUC with 95% CI + calibration figure or statistic |
| 19 | Model validation results, if performed | if internal validation, present optimism-corrected AUC |
| 20 | Predictor-outcome associations (unadjusted and adjusted) | univariate OR + multivariable OR in one table |

### Discussion
| # | item | check |
|---|---|---|
| 21 | Limitations: missing data, overfitting, measurement issues, generalisability to other populations | ■high if no limitations |
| 22 | Interpretation: explain how the model could be used, with a substantive clinical message | risk-stratification → follow-up schedule / treatment decision |
| 23 | Generalisability and any updating required before use | external validation caveat |

---

## Quick mapping: study_type → checklist {#mapping}

| study_type | primary checklist | also check |
|---|---|---|
| interventional-cohort | STROBE | — |
| prognostic-predictor | TRIPOD | STROBE (for observational cohort backbone) |
| diagnostic-accuracy | STARD | STROBE (for Methods backbone) |
| imaging-technique | STARD | STROBE |
| procedural-comparative | STROBE | — |
| rct | CONSORT | — |
| rct-posthoc | CONSORT (partial) | STROBE (observational analysis arm) |

## Quick Search Targets {#grep}
```
rg -n -A30 "#strobe"    references/reporting_checklists.md   # full STROBE
rg -n -A30 "#consort"   references/reporting_checklists.md   # full CONSORT
rg -n -A30 "#stard"     references/reporting_checklists.md   # full STARD
rg -n -A30 "#tripod"    references/reporting_checklists.md   # full TRIPOD
rg -n -A10 "#mapping"   references/reporting_checklists.md   # study_type→checklist
```
