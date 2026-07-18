# Domain Notes — Neurovascular/Stroke + Neuroimaging Vernacular

Field-specific conventions for a neurovascular/stroke + neuroimaging clinical writer: scales + cut-offs, the statistics idiom this group actually uses, imaging/technique terms. General reporting-standard prose (STROBE/CONSORT/TRIPOD) and general academic-writing advice live elsewhere — see the academic-research-skills plugin.

## Master rule {#master-rule}
Every scale introduced ONCE with full name + abbreviation + numeric range + direction-of-meaning; every numeric cut-off carries a plain-language clinical LABEL; re-gloss each scale in every table/figure footnote (self-contained display items). Numbers never appear without bedside meaning ("NIHSS ≥6 = moderate-to-severe"; "mRS 0–2 = functional independence"; "mTICI 2b–3 = successful recanalization"). The cut-off travels with the number into row stubs.

## Functional outcome scales {#outcome-scales}
- **mRS (modified Rankin Scale, 0–6, higher = worse; 6 = death).** Universal patient-centred endpoint at 90 days / 3 months. Dichotomy family: **0–1 = "excellent" / freedom from disability; 0–2 = "functional independence" / favorable; 0–3 = "favorable" / good functional status.** Full ladder: mRS 0–1 vs 2–6; 0–2 vs 3–6; 0–3 vs 4–6. BAO uses **0–3** (justified: complete independence uncommon in basilar-artery occlusion). Death is an mRS LEVEL, not censored. Primary reading = ordinal 90-day SHIFT via proportional-odds common OR, with prespecified fallback to binary if proportional-odds violated (Brant test).
- **NIHSS (National Institutes of Health Stroke Scale, 0–42, higher = worse).** Gates: ≥6 = moderate-to-severe / "mild stroke" exclusion; <10 = mild BAO. Baseline severity as median (IQR). END (early neurological deterioration) = increase ≥4 points within 24 h. Under-weights posterior circulation → pc-NIHSS for BAO.
- **Barthel Index (0–100; 95/100 = ADL independence).** **EQ-5D-5L / EQ-5D VAS** (QoL; 0.00 = equivalent to death, negative = worse than death).

## Reperfusion / recanalization {#reperfusion}
- **mTICI / eTICI (modified/expanded Thrombolysis in Cerebral Infarction, 0–3).** TECHNICAL/procedural success, NEVER a patient efficacy endpoint. **Successful recanalization = mTICI 2b–3.** TICI 3 = higher bar (chronic-occlusion recanalization). eTICI 7-point, success = 2b50 (50–66% reperfusion). First-pass recanalization = mTICI ≥2b after a single pass before rescue.
- **AOL / mAOL (Arterial Occlusive Lesion, 0–3; patency = 2 or 3).**

## Early-ischemia / clot-burden scores {#aspects}
- **ASPECTS (Alberta Stroke Program Early CT Score, 0–10, lower = larger infarct).** Anterior. Thrombectomy eligibility bands, e.g. 3–5. Narrow interindividual range → weaker predictor than NIHSS.
- **DWI-ASPECTS** operationalized: 10 named regions, 1 pt/positive region, 20%-involvement rule, normal DWI = 10; actionable cut-off post-treatment DWI-ASPECTS ≥6 predicts good outcome.
- **pc-ASPECTS (posterior-circulation, 0–10)** — correct scale for basilar disease, NOT anterior ASPECTS; subgroup split ≤8 vs >8. (Do not propagate the paper26 dual expansion.)
- **BATMAN (Basilar Artery on CTA score, 10-pt; clot burden + collaterals; split ≤8 vs >8).**

## Hemorrhage adjudication {#hemorrhage}
- Always tied to a NAMED criterion set; given equal billing with benefit.
- **Heidelberg Bleeding Classification** (dominant): HI1 (scattered petechiae, no mass effect), HI2, PH1 (hematoma <30% of infarct volume), PH2 (≥30% + mass effect). **sICH** = PH/rPH/SAH/IVH + neurological deterioration (increase ≥4 NIHSS points, or ≥2 with any ICH on imaging). Alternates named: modified **SITS-MOST** (type 2 parenchymal hematoma + ≥4 NIHSS-point deterioration), **ECASS III** (sensitivity alternate). HT = hemorrhagic transformation (umbrella); sICH = patient-relevant subset; ~12% benchmarked as typical.

## Hemorrhagic-stroke (SAH) scales {#sah}
- **Hunt–Hess grade** (clinical severity; dichotomized 1–3 vs 4–5); **modified Fisher grade** (radiographic blood burden; 1–2 vs 3–4); **DCI** (delayed cerebral ischemia, anchored to Vergouwen 2010). Ischemic scales (NIHSS/ASPECTS/TICI) correctly ABSENT in hemorrhagic work.

## Stenosis / restenosis {#stenosis}
- Stenting eligibility (ESVS 2023): carotid stenting symptomatic >50% / asymptomatic >70%; vertebral stenting symptomatic >70%. Restenosis anchored to **NASCET + WASID** criteria.
- **ISR (in-stent restenosis)** = ≥50% luminal narrowing within stent or within 5 mm of edges; DSA gold-standard adds absolute luminal loss >20%.
- Residual-stenosis "success" is procedure-specific and INCONSISTENT — keep bound: stenting success <30% residual; recanalization success TICI 3 + ≤50% residual; ≥30% residual is itself a restenosis predictor. Doppler: peak systolic velocity 300 cm/s diagnoses >70% stenosis.
- **TOAST** subtypes (LAA / cardioembolism / other / undetermined) as etiology covariate.

## Imaging-physiology / perfusion thresholds {#perfusion}
- **CTP** hemodynamic insufficiency: MTT >4 s + relative CBF <0.95 in MCA territory; MTT/rCBF reported with laterality; MTT an independent Cox predictor.
- **RAPID/iSchemaView core thresholds:** ischemic core rCBF <30% (<20% for early presenters); hypoperfused Tmax >6 s; mismatch = hypoperfused − core; **HIR** (hypoperfusion intensity ratio) = Tmax>10s / Tmax>6s. **GIC (ghost infarct core)** = CTP overestimation of final infarct volume by >10 mL. **ADC** core threshold <620×10⁻⁶ mm²/s; infarct-core 70–100 mL eligibility band.
- Workflow timing metrics: ODT (onset-to-door), DPT (door-to-puncture), onset-to-CTP (predictor cut-off ≤207 min).

## Imaging techniques / markers {#imaging-terms}
- **CTP** (CT perfusion), **DWI-ASPECTS**, **FLAIR vascular hyperintensity (FVH)** → 3-month mRS, **net water uptake (NWU / CT-NWU)** (edema quantification, ROC-modeled predictor), **photon-counting-detector CTA (PCD-CTA / UHR PCD-CTA)** (index test vs DSA), **ASL** (arterial spin labeling; reperfusion read), **CEST/APT-MRI** (saturation-power optimum 1 μT, yoked to mRS not reported as bare physics).
- **Image-quality / diagnostic-confidence = 5-point Likert**, sized via paired Wilcoxon signed-rank; SNR/CNR/blooming secondary.

## Statistics idiom actually used {#stats-idiom}
- **n/N(%) triad** — never a bare percentage; numerator BEFORE percentage + group-specific denominator, restated per outcome. Between-group contrasts = paired values + exact P with clinical adjective/direction BEFORE the numbers; never a bare P. Baseline balance via **SMD** (cut-off ≤0.1), not baseline P-values.
- **Effect measure matched to data type**, each with 95% CI, meaning stated first: ordinal mRS shift → common OR / Wilcoxon–Mann–Whitney generalized OR; dichotomized → aOR / RR (registry pairs absolute risk difference); time-to-event → **Kaplan–Meier + Cox HR + log-rank**; continuous → β / mean difference; imaging-prognostic → mean±SD vs mean±SD + correlation r.
- **Diagnostic/prognostic accuracy → ROC bundle:** ROC → AUC (95% CI; P) → optimal/Youden cut-off → Se/Sp (+ NPV), THEN dichotomize. NPV-led for rule-OUT. **DeLong** for head-to-head AUC comparison; incremental ΔAUC significance-tested, not eyeballed. Full Se/Sp/PPV/NPV/accuracy quintet each with raw fraction. **Bland–Altman / limits of agreement.** Belongs ONLY to the imaging-accuracy genre.
- **Confounding control:** **PSM** (1:1 or 1:1:2 nearest-neighbor, caliper 0.2; report SMD + variance ratio) and/or **IPTW** ("pseudo-population mimicking a randomized trial") ± instrumental-variable ± multiple imputation (MICE, Rubin's rules). Multivariable model with EXPOSURE FORCE-RETAINED; variable-selection rule stated quantitatively (univariate P<0.10 → multivariable). **Collinearity: VIF <10 / tolerance >0.1**; split models when two covariates correlate strongly.
- **Reader agreement (IMAGE reading only, never outcome adjudication):** **weighted κ** (poor/fair/good/excellent at .40/.60/.80) or Cohen's κ (>0.75 = excellent); **ICC** (5-band slight→excellent at .200/.400/.600/.800). Outcome/subtype adjudication uses blinded dual read + consensus tie-break, NO kappa.
- **NNT translation (signature move):** re-express effects as NNT (with its own CI), natural frequencies, per-hour time-cost, or absolute risk difference for a defined "average patient" (e.g. age 71, NIHSS 16, ASPECTS 9). RCT: ITT primary, single prespecified primary carries the only P; secondary/subgroup estimation-only, CIs not for hypothesis testing. IPD meta-analysis: one-step mixed-effects, within-trial-effects-first, null = "did not establish non-inferiority" (failure-to-establish, never equivalence).
- **Null / harm language:** absence-of-evidence phrasing ("no evidence of a difference"), not "no difference"; harm reported with SAME rigor as benefit, honest wide CIs on rare events shown not suppressed. SPSS + R / MedCalc named with versions; two-sided α = 0.05.

## Reporting-standard acronyms (name + point only — do not reproduce checklist prose) {#reporting-standards}
Substance over checklist-citation; the journal's structured scaffold does the standardization work. Match acronym to genre AND phase if declaring: **STROBE** = observational; **CONSORT** = RCT (Fig 1 flow, ITT, prespecified outcomes, registration, harms); **PRISMA-IPD** (+ ICEMAN, PROSPERO) = synthesis; **STROCSS** = surgical/post-hoc-as-cohort. **STARD** and **TRIPOD** appear nowhere in this corpus — do NOT add them as house convention; only paper10 reports Hosmer–Lemeshow calibration. Retrospective designs carry an IRB number only (no trial registration); prospective carry NCT / ChiCTR / PROSPERO in canonical positions.

## Quick Grep Targets {#quick-grep}
```
grep -n 'mRS 0–[123]\|functional independence\|excellent' domain_notes.md   # mRS dichotomy bands + labels
grep -n 'mTICI\|eTICI\|2b\|recanalization\|reperfusion' domain_notes.md      # reperfusion cut-offs
grep -n 'ASPECTS\|NIHSS\|BATMAN\|pc-' domain_notes.md                        # severity / early-ischemia scores
grep -n 'Heidelberg\|sICH\|SITS-MOST\|ECASS\|HI1\|PH2\|Hunt–Hess\|Fisher' domain_notes.md  # hemorrhage adjudication
grep -n 'NASCET\|WASID\|ISR\|stenosis\|residual\|TOAST' domain_notes.md      # stenosis / restenosis thresholds
grep -n 'PSM\|IPTW\|DeLong\|VIF\|κ\|ICC\|Bland–Altman\|ROC\|AUC\|NNT' domain_notes.md  # statistics conventions
grep -n 'CTP\|DWI-ASPECTS\|FVH\|FLAIR\|net water uptake\|NWU\|PCD-CTA\|Likert\|Tmax\|HIR\|GIC' domain_notes.md  # imaging terms
grep -n 'STROBE\|CONSORT\|PRISMA\|STARD\|TRIPOD' domain_notes.md             # reporting-standard names (not prose)
```
