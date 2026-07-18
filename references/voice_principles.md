# Voice principles — how this group actually writes

Distilled from 32 exemplars (genres **A** clinical-observational · **B** imaging · **C** randomized-trial). Each entry is a PRINCIPLE with a real **Correct** exemplar (sourced) and a constructed **Incorrect (AI)** counter-example. This replaces the old phrase-bank: **lift the reasoning, never paste a frame** — copying an exemplar sentence (or filling a fixed slot) is what produced templated, AI-sounding output. Obey the **anti-repetition** notes.

Scope tags: **INVARIANT** = holds across the marked genres (a MUST); **VARIANT** = genre/subtype-specific (note which). Mount the moves for your paper's genre; cross-check numeric targets against `voice_fingerprint.md` and AI tells against `clinical_ai_tells.md`.


## Title & Abstract {#title-abstract}

> **A/B/C divergence:** TITLES: A titles are noun-phrase declaratives naming the endpoint/predictor + population, and very often carry a design subtitle after a colon ('Insights from a Propensity-Matched Study', 'A Propensity Score-Matched Analysis'); a predictor-first frame ('Emergency admission plasma D-dimer: a novel predictor for...') and 'Incidence and predictors of...' frames are A signatures, and A alone will drop a bald clinical question as a subtitle ('who can benefit?'). B titles lead with the technique/parameter or imaging marker and end '...in patients with acute ischemic stroke', frequently appending a data-source tag ('results of DIRECT-MT trial') or a head-to-head comparison ('comparison with infarction volume'). C titles are intervention-vs-comparator (or the NEJM ultra-terse 'Trial of ...') and almost always append a design/trial-name subtitle ('A Secondary Analysis of a Randomized Clinical Trial', '(OPENS-2 trial): a multicentre, randomised, single-blind, sham-controlled trial'). ABSTRACT SHAPE: A uses the journal's labeled structure — BMJ Background/Objective/Methods/Results/Conclusion, Frontiers 'Background and purpose'/Methods/Results/Conclusions, JAHA merged all-caps 'METHODS AND RESULTS' — but Springer-family A papers (paper05) run an UNLABELED single paragraph opening on a bare infinitive. B keeps Radiology-journal labels (Objectives/Materials and methods/Results/Conclusions) and adds a 'Key Points'/'Key Points' bulleted block (Question/Findings/Clinical relevance in European Radiology). C splits by house style: JAMA IMPORTANCE/OBJECTIVE/DESIGN,SETTING,AND PARTICIPANTS/INTERVENTIONS/MAIN OUTCOMES/RESULTS/CONCLUSIONS AND RELEVANCE + Key Points; Lancet Background/Methods/Findings/Interpretation/Funding; AHA merged 'METHODS AND RESULTS'. Across ALL genres the conclusion restates the direction of effect in words and never leads Results with a bare incidence rate.

### Title names the endpoint (or predictor) and the population, then earns a design/trial subtitle after a colon {#title-endpoint-population-design-subtitle}
*INVARIANT · genres: A,B,C* · Ref: paper01, paper20, paper26

**Principle.** The title front-loads the concrete clinical variable at stake — the outcome, the predictor, the compared interventions, or the imaging parameter — bound to a named patient population, and then (very often) discloses the study design or trial name in a subtitle after a colon or dash. The subtitle is doing honest work: it tells the reader up front whether this is a propensity-matched cohort, a post-hoc/secondary analysis, or a randomized trial, so the claim can be calibrated before the abstract is even read. The group does NOT use vague thematic titles ('Insights into stroke outcomes') or curiosity-gap titles.

- **Correct** (paper01): “Comparing Transbrachial and Transradial as Alternatives to Transfemoral Access for Large-Bore Neuro Stenting: Insights From a Propensity-Matched Study”
- **Correct** (paper20): “Endovascular vs Medical Management of Acute Basilar Artery Occlusion: A Secondary Analysis of a Randomized Clinical Trial”
- **Correct** (paper26): “Effectiveness of Endovascular Treatment for Acute Mild Basilar Artery Occlusion Stroke: A Multicenter Real-World Study”
- **Incorrect (AI):** Unlocking the Predictive Power of D-dimer: A Comprehensive Investigation into Hemorrhage Risk in the Modern Stroke Era

**Why.** The colon-subtitle-with-design pattern appears in A (paper01, paper05, paper26, JAHA paper08/30), and in nearly every C paper (paper20, paper24, paper25, paper29, paper32); it is how this group signals rigor and lets reviewers grade the evidence immediately. Titles that hide the design or use marketing verbs ('Unlocking', 'Comprehensive Investigation', 'Modern Era') read as generated and would be desk-flagged at these journals.

**Anti-repetition.** Do not mechanically bolt ': A [design] Study' onto every title. Vary the subtitle to the real object: a full trial acronym expansion (paper24), 'A Secondary Analysis of a Randomized Clinical Trial' (paper20), 'A Multicenter Real-World Study' (paper26), or — for a terse NEJM house style — no subtitle at all, just 'Trial of ...' (paper21). Some A titles carry no subtitle when the noun phrase is already self-describing (paper02, paper03). Match the journal, not a slot.

### Prognostic/observational titles use a bare declarative noun phrase, often predictor-first or 'Incidence and predictors of...' {#title-predictor-first-noun-phrase}
*VARIANT · genres: A,B (predictor/prognostic subtype)* · Ref: paper02, paper03, paper13

**Principle.** For predictor, incidence, and prognostic-marker studies the title is a naked noun phrase built around the variable, with no verb and no 'A study of'. Two recurring frames: (1) predictor-first, where the marker leads and a colon introduces its role ('X: a novel predictor for Y'), and (2) the survey frame 'Incidence and predictors of Y following Z'. Imaging-biomarker (B) titles lead with the imaging parameter or marker ('Prognostic value of X', 'Predictors of X on [modality]') and pin it to the population at the end.

- **Correct** (paper02): “Emergency admission plasma D-dimer: a novel predictor for symptomatic intracranial hemorrhage after thrombectomy in acute ischemic stroke”
- **Correct** (paper03): “Incidence and predictors of restenosis following successful recanalization of non-acute internal carotid artery occlusion in 252 cases”
- **Correct** (paper13): “Prognostic value of post-treatment fluid-attenuated inversion recovery vascular hyperintensity in ischemic stroke after endovascular thrombectomy”
- **Incorrect (AI):** Can D-dimer Predict Bleeding? Exploring a Promising Biomarker That May Revolutionize Stroke Care

**Why.** This is the dominant title grammar for A prognostic papers (paper02, paper03) and for the B imaging-marker series (paper11 'Predictors of ghost infarct core...', paper12 'Predictors of malignant MCA infarction...', paper13, paper14). The noun-phrase form is dense, indexable, and clinically specific. Rhetorical-question titles with hype verbs ('Revolutionize') are absent from the corpus and signal AI drafting.

**Anti-repetition.** Rotate the frame rather than defaulting to one. 'X: a novel predictor for Y' (paper02), 'Incidence and predictors of Y' (paper03), 'Prognostic value of X' (paper13, paper14), 'Predictors of X on [modality]' (paper11, paper12), 'Nomogram Model for Predicting X' (paper30). Include a sample-count tag ('in 252 cases', paper03) only when the n itself is the selling point; do not append it reflexively.

### Abstract uses the target journal's exact structured labels — not a generic Background/Methods/Results/Conclusions template {#abstract-structured-labels-match-journal}
*INVARIANT · genres: A,B,C* · Ref: paper02, paper20, paper23

**Principle.** The structured abstract adopts the label set the destination journal actually mandates, verbatim and in the journal's casing, rather than a one-size-fits-all IMRaD skeleton. BMJ/JNIS papers use singular 'Background / Objective / Methods / Results / Conclusion'; Frontiers uses 'Background and purpose / Methods / Results / Conclusions'; JAHA and Stroke merge into all-caps 'BACKGROUND / METHODS AND RESULTS / CONCLUSIONS'; JAMA uses 'IMPORTANCE / OBJECTIVE / DESIGN, SETTING, AND PARTICIPANTS / INTERVENTIONS / MAIN OUTCOMES AND MEASURES / RESULTS / CONCLUSIONS AND RELEVANCE'; Lancet uses 'Background / Methods / Findings / Interpretation / Funding'. The label choice is a fingerprint of where the paper is aimed.

- **Correct** (paper02): “Background Symptomatic intracranial hemorrhage (sICH) is a common and severe complication ... Objective To explore the ability of admission plasma D-dimer levels to predict sICH after thrombectomy. Methods ... Results ... Conclusion Elevated admission D-dimer levels are an independent predictor of sICH”
- **Correct** (paper20): “IMPORTANCE In several randomized clinical trials, endovascular thrombectomy led to better functional outcomes ... OBJECTIVE To evaluate 1-year clinical outcomes ... DESIGN, SETTING, AND PARTICIPANTS This study is an extension of the ATTENTION trial ... CONCLUSIONS AND RELEVANCE Among patients with basilar artery occlusion within 12 hours of onset, the benefits ... were sustained”
- **Correct** (paper23): “Background Intravenous thrombolysis is recommended before endovascular treatment ... Methods We conducted a systematic review and individual participant data meta-analysis ... Findings We identified 1081 studies ... Interpretation We did not establish non-inferiority ... Funding Stryker and Amsterdam University Medical Centers”
- **Incorrect (AI):** Background: Stroke is a major health burden. Methods: We did a study. Results: We found significant results. Conclusion: More research is needed. (generic labels applied regardless of the target journal, with hollow content in each slot)

**Why.** Every paper in the corpus mirrors its journal's house label set exactly (BMJ paper02/03, Frontiers paper15/16, JAHA/Stroke merged paper05/08/28/29/30/31, JAMA paper20/25/27/28, Lancet paper23/24). Using the wrong label family, or a bland generic skeleton with empty slots, immediately marks a draft as untailored and AI-templated.

**Anti-repetition.** Decide the target journal first, then copy its label set and casing; never carry BMJ's 'Objective' into a Lancet 'Findings/Interpretation' abstract or vice versa. Note two escape hatches actually used: Springer-family A/B papers (paper05) run an UNLABELED single-paragraph abstract, and European Radiology B papers add a separate 'Key Points' bullet block (paper10, paper12) or 'Key Points: Question/Findings/Clinical relevance' (paper07) after Conclusions. Reproduce those quirks when aiming there.

### The Objective sentence takes the grammatical form the genre prefers — bare infinitive (C), 'The purpose/aim was to' (A/B), and it plainly states the single question {#abstract-objective-verb-form-by-genre}
*VARIANT · genres: A,B use 'The purpose/aim of this study was to...'; C uses a bare 'To evaluate/assess...' infinitive* · Ref: paper02, paper20, paper07

**Principle.** The abstract's objective clause is a single declarative statement of the one question the study answers, but the surface form splits by genre. RCT/post-hoc (C) and terse Radiology-house abstracts open the OBJECTIVE label with a bare infinitive ('To evaluate...', 'To compare...'). A and B prognostic papers embed the aim in a full sentence — 'The purpose/aim of our study was to...' or 'We aimed to determine...'. Either way it names exactly one primary question and does not sprawl into a list of secondary aims.

- **Correct** (paper02): “The purpose of our study was to investigate the association between admission plasma D-dimer levels and sICH after thrombectomy in a single comprehensive center cohort of patients with AIS.”
- **Correct** (paper20): “OBJECTIVE To evaluate 1-year clinical outcomes in patients with acute basilar artery occlusion following endovascular thrombectomy vs control.”
- **Correct** (paper07): “Objectives To determine the optimal saturation power for chemical exchange saturation transfer (CEST) imaging and evaluate the prognostic value of CEST parameters at different saturation powers in patients with acute ischemic stroke (AIS).”
- **Incorrect (AI):** The overarching aim of this comprehensive investigation was to holistically explore, evaluate, and elucidate the multifaceted relationships between numerous biomarkers and a wide range of clinical outcomes in stroke patients.

**Why.** The meta fingerprint confirms the split: A/B objective_form clusters on 'purpose-of-sentence' and 'aim-was-to' (paper02, paper09, paper12, paper30), while C clusters on 'bare-infinitive' (paper20, paper23) or 'aim-was-to' for post-hoc (paper24, paper29). Overstuffed multi-verb objectives ('holistically explore, evaluate, and elucidate') with quantifier-inflation ('numerous', 'multifaceted', 'wide range') are the AI tell.

**Anti-repetition.** Pick the form the genre uses and keep to ONE primary aim per sentence. For B papers that legitimately have two aims (optimize a parameter AND test its prognostic value, paper07), join them with a single 'and' — do not chain three or four verbs. Avoid the AI verb-stack ('explore, evaluate, and elucidate') and hollow amplifiers ('comprehensive', 'holistically', 'multifaceted').

### Results open with the enrolled-N frame or the head-to-head comparison, never with a naked incidence rate {#results-open-comparative-not-rate}
*INVARIANT · genres: A,B,C* · Ref: paper02, paper20, paper09

**Principle.** The Results block leads with the denominator and cohort ('Of the 395 enrolled patients, 48 (12.2%) had sICH'; 'Among 217 patients...'; 'A total of 348 patients were randomly assigned'), or with the primary between-group comparison carrying its effect size and CI. It does NOT open with a bare rate stripped of its denominator, and it never opens with the soft-news 'one in five' phrasing. Effect estimates are reported as OR/HR/RR with 95% CI and P, inline, in the same sentence as the comparison.

- **Correct** (paper02): “Results Of the 395 enrolled patients, 48 (12.2%) had sICH. Patients with sICH were older (72.9 vs 69.3 years, P=0.037), more often female (62.5% vs 45.5%, P=0.027), had higher D-dimer levels (2.70 vs 0.74 mg/L, P<0.001)”
- **Correct** (paper20): “RESULTS Among 330 patients who had 1-year follow-up data, 227 (68.8%) were male, and the mean (SD) age was 67.0 (10.7) years. An mRS score 0 to 3 at 1 year was achieved by 99 of 222 patients (44.6%) in the thrombectomy group and 21 of 108 (19.4%) in the control group (adjusted rate ratio, 2.23; 95% CI, 1.51-3.29)”
- **Correct** (paper09): “RESULTS: Forty-three participants (mean age, 63.1 years ± 9.5; 8 women) with 51 stents were included. ISR was present in 14 stents and absent in 37”
- **Incorrect (AI):** Results: Nearly one in five patients experienced restenosis, a striking finding that underscores the substantial clinical burden of this understudied complication.

**Why.** results_abs_rate_lead_frac is ~0 for A and B and near-zero for C in the fingerprint; the group opens Results on the enrolled cohort or the primary comparison every time (paper02, paper08, paper09, paper20, paper24, paper28). The 'Nearly one in five' soft-news frame — with editorializing amplifiers ('striking', 'substantial burden') — is exactly the AI-phrasebank output this corpus avoids in the abstract Results. (Note: paper03 DOES use 'Nearly one in five' but in its CONCLUSION, not to open Results — see the conclusion move.)

**Anti-repetition.** Vary the opener across the two legitimate forms: 'Of the N enrolled patients, k (x%) had [event]' for cohort/prognostic (paper02), and 'Among N patients (demographics), [primary endpoint] was achieved in ... vs ... (effect, CI)' for comparative/RCT (paper20, paper28). Keep the denominator attached to every rate. Never launch Results with a rate rephrased as 'one in five/four/three' or with an evaluative adjective. CRITIC-GUARD: applies to labeled/structured abstracts; unlabeled single-paragraph abstracts (paper05) may not have a discrete Results slot.

### The abstract Conclusion restates the effect direction in plain words and calibrates the claim to the design {#conclusion-restates-direction-in-words}
*INVARIANT · genres: A,B,C* · Ref: paper26, paper03, paper04

**Principle.** The final Conclusion sentence converts the headline result back into a plain-language directional statement about patients ('are an independent predictor of', 'was associated with improved... although the risk of ... was increased', 'we did not establish non-inferiority'), and its strength is tuned to the design: observational/A and imaging/B conclude 'is associated with' / 'may be an effective marker'; RCTs/C conclude with the trial's verdict; post-hoc/small-sample papers explicitly hedge and call for confirmation. It restates BOTH the benefit and its cost when the study found a safety trade-off — it does not cherry-pick the positive.

- **Correct** (paper26): “Conclusions In this cohort of patients with acute mild BAO, EVT was associated with an improved 90-day functional outcome compared with standard medical treatment alone, although the risk of symptomatic intracerebral hemorrhage was increased.”
- **Correct** (paper03): “Conclusions Nearly one in five patients experienced restenosis following successful recanalization of non-acute ICAO. Occlusion length, residual stenosis ≥30%, and ICA wall collapse were independently associated with restenosis.”
- **Correct** (paper04): “Conclusion: Data from the CMOSS trial indicate that patients with BMI ≥ 24.5 kg/m2 are at a higher risk of IIS when treated medically only and appear to derive greater benefit from bypass surgery ... Given the small sample size and the inherent limitations of retrospective analyses, further large-scale, prospective studies are necessary to confirm these findings.”
- **Incorrect (AI):** Conclusion: This landmark study conclusively proves that our biomarker is a game-changing tool that will fundamentally transform stroke care and should be immediately adopted into all clinical guidelines worldwide.

**Why.** hedge.discussion and the claim_gradient metadata show the ladder: A/B conclusions sit at 'associated with'/'may' (paper13, paper14, paper26), C-RCTs state the trial verdict but stay bounded (paper23 'We did not establish non-inferiority', paper26 keeps the sICH trade-off), and post-hoc/small-n papers append an explicit confirmation caveat (paper04). Overclaiming verbs ('conclusively proves', 'game-changing', 'will transform', 'should be immediately adopted') never appear and are the clearest AI-inflation signal.

**Anti-repetition.** Match the hedge to the design and do not reuse one verb. Prognostic A/B: 'are an independent predictor of' (paper02), 'may be an effective prognostic marker associated with' (paper13). Comparative/RCT: pair benefit with its cost in one sentence using 'although'/'albeit' (paper18 'albeit with increased odds of...', paper26). Post-hoc/small-n: state the signal then a plain confirmation caveat (paper04, paper05 'did not support the systematic use... except in...'). The 'Nearly one in five' phrasing is acceptable HERE, in the conclusion (paper03), where it recaps a headline incidence — but not as a Results opener.

### Every outcome, threshold, and scale is defined inline the first time it appears in the abstract {#abstract-defines-outcomes-inline}
*INVARIANT · genres: A,B,C* · Ref: paper26, paper15, paper02

**Principle.** Within the abstract Methods, each endpoint and cut-point is operationalized on first mention — the functional-outcome scale with its numeric range, the recanalization grade, the hemorrhage criterion — so the abstract is self-contained and the reader never has to guess what 'good outcome' means. This is a clinical-trialist reflex the whole group shares: 'functional independence (modified Rankin Scale score of 0-2) at 90 days', 'successful reperfusion was defined as a modified Thrombolysis in Cerebral Infarction (mTICI) score of 2b/3', 'sICH was defined according to the Heidelberg Bleeding Classification'.

- **Correct** (paper26): “The primary outcome was 90-day functional independence, defined as a modified Rankin Scale score of 0 to 2.”
- **Correct** (paper15): “Successful reperfusion was defined as a modified Thrombolysis in Cerebral Infarction (mTICI) score of 2b/3. Functional dependence at 90 days was defined as a modified Rankin scale score of 3-6.”
- **Correct** (paper02): “sICH was defined according to the criterion of the Heidelberg Bleeding Classification.”
- **Incorrect (AI):** The primary outcome was good functional outcome, and we also assessed safety outcomes and other relevant clinical endpoints of interest.

**Why.** Inline operationalization appears in essentially every Methods block (paper02, paper15, paper16, paper26, paper28, paper29); it is the marker of an author who thinks in endpoints. Vague endpoint language ('good functional outcome... and other relevant clinical endpoints of interest') with no scale, range, or criterion is the AI placeholder that this group never ships.

**Anti-repetition.** Attach the definition to the endpoint's first appearance and vary the connective naturally — 'defined as', 'was defined as', a parenthetical '(modified Rankin Scale score, 0-1)', or an em-dash gloss. Do not restate the same definition twice, and do not batch all definitions into one mechanical 'Definitions:' run. Give the numeric range for any scale (mRS 0-2, mTICI 2b/3, NIHSS <10) rather than the bare adjective ('good', 'successful', 'mild'). CRITIC-GUARD: INVARIANT only WHEN the abstract has a labeled Methods slot; in ultra-compressed NEJM structured or unlabeled Springer single-paragraph abstracts (e.g. paper05) the outcome definition may move to the body Methods — do not force it.


## Introduction {#introduction}

> **A/B/C divergence:** The funnel is shared but the opener and the aim diverge by genre. OPENER: A splits evenly between disease-burden (5/13) and standard-of-care-limitation (5/13); B is disease-burden-dominant (4/7) and, being technique/imaging papers, uniquely reaches for imaging-limitation and standard-of-care-benefit openers; C splits disease-burden (5/12) vs standard-of-care-limitation/history (6/12) and is the only genre that opens on the pure residual-burden-despite-treatment frame ('half of patients do not recover despite EVT'). PRIOR-EVIDENCE SCAFFOLD: A and B build the middle of the funnel by name-checking individual prior authors (Piero et al., Davoli et al., Sabben et al., Bernsen et al.) with their n; C builds it by name-checking prior TRIALS as acronyms (COSS, CMOSS, SAMMPRIS, DAWN, DEFUSE-3, ATTENTION, BAOCHE) — trials not people. GAP: identical hard-negation habit across all three ('However, few studies…', 'remains unclear', 'to the best of our knowledge, no publications…'). AIM FORM is the sharpest divergence: A prefers the lean bare-infinitive 'this study aimed to compare…' (5/13); B disproportionately uses the formal nominal 'Therefore, the purpose of the present study was to…' (purpose-of-sentence 3/7, its signature); C most often anchors the aim to a named trial acronym ('the aim of this randomized clinical trial was…', 'the OPENS-2 trial to validate…', 'ANGEL-ASPECT trial in China aimed to…') — aim-was-to 5/12 — and, when in JAMA/NEJM/Radiology, replaces the prose aim with a journal-mandated structured label (OBJECTIVE / PURPOSE / BACKGROUND).

### Open with a hard, bracket-cited magnitude, never a soft 'one in five' paraphrase {#opener-hard-cited-epidemiology}
*INVARIANT · genres: A,B,C* · Ref: paper03, paper10, paper30

**Principle.** When the funnel opens on disease burden, the group states the magnitude as a bare numeral or range with its superscript/bracketed citation immediately attached, in the register of an epidemiology table — a specific percent, incidence, or mortality figure. They never round it into a rhetorical 'nearly one in five' or 'a staggering number of' construction. The number is evidence being cited, not a hook being sold.

- **Correct** (paper03): “Atherosclerotic internal carotid artery occlusion (ICAO) contributes to approximately 10% of transient ischemic attacks (TIAs) and 15–25% of ischemic strokes in the carotid territory, making it a major cause of ischemic stroke globally.1 2”
- **Correct** (paper10): “Between 10 and 15% of the patients with cerebral infarction in the territory of middle cerebral artery (MCA) may develop space-occupying brain edema between the second and the fifth day after the onset of stroke [1, 2].”
- **Correct** (paper30): “Acute vertebrobasilar artery occlusion (AVBAO) is a severe form of ischemic stroke, accounting for ≈1% of all ischemic strokes and 5% to 10% of proximal intracranial occlusions.1,2 Despite advancements in stroke management, AVBAO is associated with death and severe disability rates of up to 80%.3”
- **Incorrect (AI):** Stroke remains one of the most devastating conditions worldwide, and alarmingly, nearly one in five patients who suffer a large-vessel occlusion will face a lifetime of disability — a sobering reality that underscores the urgent need for better treatments.

**Why.** The old phrasebank taught 'Nearly one in five patients experienced X', which reads as journalistic soft-news and signals AI/templated writing. The corpus register is the opposite: numerals carry citations, the sentence does epidemiological work, and there is no adjectival editorializing ('alarmingly', 'devastating', 'sobering'). Matching this keeps the opener clinical rather than promotional.

**Anti-repetition.** Do not turn this into a fill-in 'X% of patients with [disease] experience [outcome]' stamp. Vary the magnitude type across drafts — sometimes prevalence (≈10%), sometimes an annual recurrence risk (>10% per year), sometimes a mortality ceiling (up to 80%), sometimes an incidence per 100 000 — and let the sentence's grammatical subject be the disease entity itself, not 'patients', so successive openers don't share a skeleton.

### The 'despite successful treatment, half still fail' opener {#opener-residual-burden-despite-treatment}
*VARIANT · genres: C primary; B secondary (procedural/technique papers)* · Ref: paper24, paper25, paper12

**Principle.** For papers whose reason-to-exist is an unmet need on top of an already-effective therapy, the funnel opens not on the disease but on the residual gap: it grants that the standard of care (EVT) is established and effective, then pivots on the same or next sentence to the blunt fact that a large fraction of patients still do poorly. The concession is genuine ('has become a mainstay', 'emerged as the standard of care') and the pivot is a plain fraction, not a hedge.

- **Correct** (paper24): “Endovascular treatment has emerged as the standard of care for patients with acute ischaemic stroke caused by large-vessel occlusion in the anterior circulation.1–5 Despite this advancement, a substantial challenge remains: approximately half of patients who undergo endovascular treatment do not have a favourable functional outcome, defined by a modified Rankin Scale (mRS) score of 0–2 at 90 days.6”
- **Correct** (paper25): “Despite a high recanalization rate with improved thrombectomy devices over the past decade, endovascular thrombectomy fails to yield a good clinical outcome in half of patients who have had a stroke.2-4”
- **Correct** (paper12): “However, although the safety and effectiveness of EVT have been fully verified, we must be aware that the rate of functional independence after EVT was only about 50% [6].”
- **Incorrect (AI):** While endovascular thrombectomy represents a remarkable breakthrough in stroke care, it is important to note that outcomes remain suboptimal in a significant proportion of patients, highlighting an unmet clinical need that this study seeks to address.

**Why.** This is the group's signature C/procedural opener and it works because the concession is specific and the deficit is a hard fraction ('approximately half', 'only about 50%'). The AI version hedges the deficit into vagueness ('suboptimal', 'a significant proportion') and pre-announces the study's mission ('this study seeks to address'), which the corpus never does at the top of the funnel — the aim comes only at the bottom.

**Anti-repetition.** Rotate the concession verb ('emerged as the standard of care' / 'has become a mainstay' / 'has been fully verified' / 'revolutionized') and the pivot word ('Despite this advancement' / 'However' / 'even if a successful recanalization is achieved'). Keep exactly one hard fraction; do not stack two deficit clauses. Never let the residual-burden sentence also contain the study aim. CRITIC-GUARD: the residual fraction is a DATUM from YOUR indication's own denominator (BAO, MeVO, late-window, wake-up all differ) — never reuse the stock '~half of patients do not have a favourable outcome' as a frame; pull the number from your cohort/control arm.

### Name the prior evidence explicitly — authors+n in A/B, trial acronyms in C {#prior-evidence-named-actors}
*VARIANT · genres: A,B name prior authors with sample size; C names prior trials as acronyms* · Ref: paper10, paper01, paper27

**Principle.** The middle of the funnel is built by attributing prior findings to concrete, named sources rather than to an anonymous 'previous studies have shown'. In the clinical/imaging genres (A, B) the sources are individual investigators, cited by surname with their cohort size, so the reader can weigh each ('Based on a study population of 98 patients, Davoli et al have reported…'). In the RCT genre (C) the sources are landmark trials cited by their acronym, treated as named agents that 'demonstrated' or 'established' something. The move is: attribution is specific enough to be arguable.

- **Correct** (paper10): “Based on a study population of 98 patients, Davoli et al have reported that high systolic blood pressure and high blood glucose on admission, and a CT angiography (CTA) ASPECTS ≤ 5 are independent predictors of mMCAi [15]. Based on a study cohort of 66 stroke patients, Sabben et al indicated that early successful reperfusion after EVT was associated with the decreased occurrence of mMCAi [16].”
- **Correct** (paper01): “Piero et al., who conducted a retrospective study of carotid artery stenting via TBA versus TRA, demonstrating the safety and effectiveness of TBA/TRA (5). However, they did not further analyze whether discrepancies exist between the two groups in terms of access site complications and procedural quality metrics.”
- **Correct** (paper27): “As a potential treatment for ICAS with impaired flow, intracranial stenting was found to be inferior to medical management in the SAMMPRIS trial and the Vitesse Intracranial Stent Study for Ischemic Stroke Therapy (VISSIT) trial mainly because of the high complication rate associated with stenting.7,12,13”
- **Incorrect (AI):** Numerous studies have investigated predictors of malignant infarction, and it has been widely reported that various clinical and imaging factors may be associated with poor outcomes after thrombectomy.

**Why.** Anonymous massed citation ('numerous studies have investigated', 'it has been widely reported') is the AI tell — it asserts consensus without letting the reader see the pieces. The group instead lays out named priors so it can then say precisely what each one missed, which is what sets up a defensible gap. Preserving the genre split (people vs trial acronyms) also keeps A/B reading as investigator-scale work and C reading as trial-scale evidence.

**Anti-repetition.** Do not mechanically append 'X et al reported…' three times in a row with the same verb. Vary the framing slot ('Based on a study cohort of N…' / 'In a retrospective analysis of 19 cases…' / bare 'Author et al indicated…') and alternate the reporting verb (reported / indicated / demonstrated / found / believed). For C, spell out each acronym once at first use and then never re-expand it; don't turn the intro into an acronym glossary.

### State the gap as a hard, specific negation — 'However, few studies…' not a soft transition {#gap-hard-specific-negation}
*INVARIANT · genres: A,B,C* · Ref: paper01, paper15, paper02

**Principle.** The gap that justifies the study is stated as an explicit negative fact, hinged on a plain 'However' (the group's default adversative), and made specific to the exact unstudied question. The negation is one of a small fixed family — 'few studies have', 'remains unclear/uncertain/ill-defined', 'has not been reported', 'to the best of our knowledge, no publications have…' — and it names the precise missing comparison, not a generic 'more research is needed'.

- **Correct** (paper01): “However, they did not further analyze whether discrepancies exist between the two groups in terms of access site complications and procedural quality metrics.”
- **Correct** (paper15): “However, few studies have investigated the predictors of FR in patients treated with MT in late time windows.”
- **Correct** (paper02): “To the best of our knowledge, no publications have reported the relationship between D-­dimer levels and sICH of patients with AIS after EVT.”
- **Incorrect (AI):** Nevertheless, despite these promising advances, the current body of literature remains somewhat limited, and further investigation is warranted to more comprehensively elucidate this important clinical question.

**Why.** The corpus adversative is overwhelmingly plain 'However' (fingerprint: 'nevertheless', 'nonetheless', 'notably' all sit at 0.0 per 1000 words across A/B/C). The AI version reaches for 'Nevertheless… further investigation is warranted to elucidate' — exactly the vague, unfalsifiable hedge the group avoids. A good gap sentence could be checked against the literature; 'the body of literature remains somewhat limited' cannot.

**Anti-repetition.** 'However' is the default but not the only word — the corpus also uses 'Nevertheless' sparingly (paper25) and 'By contrast' (paper11); rotate deliberately and keep 'Notably/Importantly' out (they read 0.0 in the fingerprint). Vary the negation verb across sections of the same intro. Anchor every gap to the specific missing variable/comparison/population so no two gap sentences are interchangeable. CRITIC-GUARD: do NOT rotate a closed bank of stems ('few studies have investigated X'). A generic 'However, few studies have investigated [X] in [Y]' is itself an AI tell. The safe form is the paper01 type: name a specific prior study's specific omission, so the gap is literature-checkable.

### Aim register diverges: lean bare-infinitive (A), formal 'the purpose was to' (B), trial-anchored (C) {#aim-form-genre-divergence}
*VARIANT · genres: A bare-infinitive-leaning; B purpose-of-sentence-leaning; C trial-acronym-anchored / structured-label* · Ref: paper16, paper11, paper24

**Principle.** The bottom-of-funnel aim is phrased in a register that tracks the genre. Genre A tends to the lean 'this study aimed to compare…' bare-infinitive. Genre B disproportionately uses the formal nominalized frame 'Therefore, the purpose of the present study was to…' — its house signature. Genre C most often binds the aim to a named trial ('the aim of this randomized clinical trial was to…', 'we initiated the multicentre OPENS-2 trial to validate…') and, in structured-abstract journals, replaces prose with a mandated OBJECTIVE/PURPOSE label. The choice is not decorative: it signals whether the unit of work is a study, a method, or a trial.

- **Correct** (paper16): “Therefore, this study aimed to compare the characteristics, reperfusion rates, and clinical outcomes between the cICA PO and true occlusion groups.”
- **Correct** (paper11): “Therefore, the purpose of the present study was to explore the predictors of GIC on baseline CTP in stroke patients achieving successful recanalization after MT, using follow-up DWI as the reference standard.”
- **Correct** (paper24): “Encouraged by these findings, we initiated the multicentre OPENS-2 trial to validate the efficacy and safety of normobaric hyperoxia plus endovascular treatment, in comparison with sham normobaric hyperoxia plus endovascular treatment, among patients with acute ischaemic stroke due to large-vessel occlusion in the anterior circulation who met criteria for endovascular treatment.”
- **Incorrect (AI):** Therefore, the purpose of our study was to investigate the potential role of this novel biomarker in predicting outcomes, in order to provide new insights and contribute to the existing body of knowledge in this important field.

**Why.** Two failures the corpus never commits: (1) applying one aim register uniformly regardless of genre — a B-style 'the purpose of our study was to' bolted onto an RCT reads wrong, and an RCT's aim that never names its trial reads under-powered; (2) the empty tail 'in order to provide new insights and contribute to the existing body of knowledge', which the group replaces with the concrete comparator, reference standard, or population. The real aims always end on something operational (a reference standard, a comparator arm, a defined cohort).

**Anti-repetition.** Pick the register from the genre, then vary within it: A can also use 'we examined…' (paper04) or 'This study's primary aim was to…' (paper03); B's nominal frame can be singular 'purpose' or plural 'aims of the present study were to (1)… (2)…' (paper12); C can front-load the trial acronym or the motivating clause ('To address these issues, we conducted…', paper23). Never end the aim on a filler purpose-clause; end it on the comparator, the reference standard, or the population.

### Anchor the aim to a named cohort / registry / trial and its setting, not to an abstract question {#aim-anchored-to-named-cohort}
*INVARIANT · genres: A,B,C* · Ref: paper01, paper17, paper31

**Principle.** The aim sentence names the concrete vehicle of the study — the specific cohort, registry, multicenter trial, or single center — and often its country or setting, so the objective is grounded in a real dataset rather than a free-floating research question. Across all three genres the aim carries a proper-noun anchor (a registry name, a trial acronym, 'in our stroke center', 'a multicenter trial conducted in China', 'a large ICH cohort from a multicenter prospective registry').

- **Correct** (paper01): “Hence, we aimed to compare the outcomes of patients undergoing TBA, TRA, and TFA for large-bore neuro stenting in our stroke center.”
- **Correct** (paper17): “We aimed to investigate the relationship between admission dehydration and in-hospital mortality in a large ICH cohort from a multicenter prospective registry.”
- **Correct** (paper31): “In this study we investigate the clinical outcomes and safety of rescue angioplasty and/or stenting in patients from a prospective multicenter LVO registry in China (Endovascular Treatment Key Technique and Emergency Work Flow Improvement of Acute Ischemic Stroke, ANGEL-­ACT)…”
- **Incorrect (AI):** In the present study, we sought to explore the association between this biomarker and clinical outcomes, with the goal of improving risk stratification and ultimately enhancing patient care.

**Why.** The AI aim floats free of any dataset ('we sought to explore the association… with the goal of… enhancing patient care'), which reads as a grant abstract, not a study. The group's aims are load-bearing: they tell you which cohort, which centers, which registry — information a reviewer needs and that pre-commits the paper to a real denominator. This is a core marker of clinical (vs basic-science / vs AI) voice.

**Anti-repetition.** Vary the anchor type so successive drafts don't all end '…in our single-center cohort': use registry acronyms (CMOSS, ANGEL-ACT, PERSIST), setting descriptors ('a multicenter trial conducted in China', 'six comprehensive stroke centers'), or a training/validation split (paper30). Place the anchor at the natural clausal position — sometimes mid-sentence, sometimes as a trailing prepositional phrase — rather than always as a final '…in [cohort]' tag.

### In structured-abstract journals, carry the funnel in mandated labels, keeping the intro proper short {#structured-background-labels-C}
*VARIANT · genres: C (JAMA/NEJM/Radiology/Lancet/JNIS structured formats); also A/B papers published in JNIS* · Ref: paper22, paper27, paper02

**Principle.** When the target journal mandates a structured front matter, the group lets those labeled slots carry the funnel in compressed form rather than duplicating it in prose. NEJM 'BACKGROUND' is two sentences (context + the exact uncertainty). JAMA runs IMPORTANCE (burden+gap) → OBJECTIVE (the aim as a bare infinitive). JNIS uses the 'WHAT IS ALREADY KNOWN / WHAT THIS STUDY ADDS / HOW THIS MIGHT AFFECT…' triad. The body intro then stays lean because the scaffolding already lives in the labels.

- **Correct** (paper22): “Endovascular thrombectomy for acute ischemic stroke due to medium-vessel occlusion has had varying results across trials. Whether thrombectomy improves functional outcomes in patients with medium-vessel occlusion and moderate-to-severe deficits is unclear.”
- **Correct** (paper27): “IMPORTANCE In-stent restenosis (ISR) is the primary reason for stroke recurrence after intracranial stenting in patients who were treated with a standard bare-metal stent (BMS). Whether a drug-eluting stent (DES) could reduce the risk of ISR in intracranial atherosclerotic stenosis (ICAS) remains unclear. OBJECTIVE To investigate whether a DES can reduce the risk of ISR and stroke recurrence in patients with symptomatic high-grade ICAS.”
- **Correct** (paper02): “WHAT IS ALREADY KNOWN ON THIS TOPIC ⇒ Clinical and imaging predictors of symptomatic intracranial hemorrhage (sICH) in patients with AIS treated with thrombectomy have been extensively investigated, unlike blood biomarkers for which publishing of results remains scarce.”
- **Incorrect (AI):** BACKGROUND Stroke is a major global health problem with enormous societal and economic impact. Over the past decades, numerous therapeutic strategies have been developed, yet many challenges remain. In this comprehensive study, we aimed to thoroughly investigate an important and clinically relevant question in this rapidly evolving field.

**Why.** The NEJM 'BACKGROUND' block is famously terse — the group matches it: one context sentence, one 'Whether X … is unclear/uncertain' sentence, and stop. The AI version pads the mandated slot with generic burden throat-clearing ('major global health problem with enormous impact', 'rapidly evolving field') and a contentless aim, which is exactly what the compressed structured format is designed to forbid. Respecting the label's word-economy is itself part of the voice.

**Anti-repetition.** Match the format the venue actually uses — do not paste JAMA IMPORTANCE/OBJECTIVE labels into an NEJM 'BACKGROUND' block or into a plain unstructured intro. In the NEJM block, the second sentence is almost always a 'Whether… is unclear/uncertain' construction; use it, but rotate the uncertainty verb (unclear/uncertain/has had varying results). Don't restate the labeled content again verbatim in the body introduction.


## Methods {#methods}

> **A/B/C divergence:** A (single-center/multicenter observational, prognostic, procedural; Nanjing circle + registry-derived): the cohort sentence is a self-contained provenance statement — one sentence that binds accrual window + 'consecutive' + center identity + retrospective/prospective nature; IRB + consent-waiver is a terse 1-2 sentence unit; endpoints are defined inline with named scales and citation superscripts; adjudication is 'two blinded readers, third for disagreement'; stats build toward a PSM/multivariable/nomogram machinery. B (imaging-biomarker/technique): cohort provenance is thinner and enrolment criteria pivot fast to the imaging protocol (scanner make/model, sequence parameters in parenthetical bursts) and to reader-grading with explicit years-of-experience and inter-reader kappa/ICC — the reader IS the instrument, so their calibration is foregrounded; consent is often OBTAINED (prospective) not waived. C (RCT / post-hoc / IPD-meta, NEJM/Lancet/JAMA voice): the cohort is a NAMED trial with registration ID + the acronym expanded, design adjectives stacked ('multicenter, prospective, open-label, blinded-endpoint, randomized'); the parent-trial is invoked by name and 'reported previously', endpoints are pre-specified with primary/secondary/safety hierarchy and every scale gets an inline range gloss; adjudication is an 'independent clinical event committee / imaging core laboratory, blinded to allocation'; stats name the ITT/per-protocol populations and the pre-specified analysis plan. NEJM abstracts (papers 21,22) compress the entire Methods to a 1-paragraph structured block; full-text C papers (24,25,27,28,29) run long with a dedicated Randomization-and-Masking subsection A/B never have.

### Cohort provenance stated in one self-contained breath: window + consecutive + center + design {#cohort-provenance-one-breath}
*INVARIANT · genres: A,B,C* · Ref: paper01, paper02, paper31

**Principle.** The opening cohort sentence is a dense provenance stamp, not a warm-up. In one or two sentences the group fixes the accrual window (dated to the month), the accrual logic ('consecutive'), the site identity, and the retrospective/prospective nature — bound together so a reader can locate and audit the sample immediately. A leads with the date range and 'consecutive'; B states it more thinly before pivoting to imaging; C replaces the raw dates with a NAMED trial and its design adjectives. What is invariant is that provenance is front-loaded and self-contained, never spread across vague throat-clearing.

- **Correct** (paper01): “From January 2019 to January 2024, a total of 4752 patients underwent large-bore neurointerventions (> 6 F) at our center, comprising 89 cases of TBA, 176 cases of TRA, and 4487 cases of TFA.”
- **Correct** (paper02): “Datasets of consecutive patients treated with EVT between February 2018 and August 2021 at our single comprehensive stroke center were retrieved from the clinical database.”
- **Correct** (paper31): “All data were derived from ANGEL-ACT, a prospective nationwide registry of endovascular treatment for acute ischemic stroke in 111 hospitals in China between November 2017 and March 2019 with a centralized imaging core laboratory.”
- **Incorrect (AI):** In order to investigate this important clinical question, we carefully collected data from a group of patients who were treated at our institution over a period of several years, ensuring that a robust and representative sample was obtained for the analysis.

**Why.** The group treats the first Methods sentence as an auditability contract — dates, count, site, and consecutiveness let a reviewer reconstruct the denominator and judge selection bias without reading further. AI padding ('important clinical question', 'robust and representative') defers the facts and signals a writer who does not think like an epidemiologist. This is the single strongest tell separating clinical Methods from generic academic prose.

**Anti-repetition.** Do not always open 'From <month year> to <month year>, X patients...'. Vary the carrier: 'Datasets of consecutive patients... were retrieved', 'We retrospectively reviewed the clinical data of 737 consecutive patients', 'This study involved a retrospective analysis of a prospectively maintained patient database'. The invariant is density-and-frontloading, not the syntactic frame; C papers legitimately swap dates for a trial name and should NOT be forced into the date-first mold.

### IRB approval + consent disposition compressed into a terse, justified unit {#irb-consent-terse-unit}
*INVARIANT · genres: A,B,C* · Ref: paper05, paper08, paper09

**Principle.** Ethics is handled as a compact administrative unit — approval body named, consent disposition stated, and the disposition JUSTIFIED by the study design in the same breath (waiver 'owing to the retrospective nature' / anonymized data; or written consent 'obtained' for prospective/RCT work). The group never inflates this into moralizing sentences; it is a checklist rendered in one to three clauses. A/B routinely WAIVE consent citing retrospective design; C and prospective-B OBTAIN written consent, and RCTs add the registration ID and reporting-guideline (CONSORT/STROBE) tag adjacent to it.

- **Correct** (paper05): “The requirement for patient consent was waived owing to the retrospective study nature.”
- **Correct** (paper08): “For this retrospective study, the requirement for informed consent was waived by the institutional review board, as the data were anonymized and collected from existing databases.”
- **Correct** (paper09): “This prospective study was approved by the institutional review board of the First Affiliated Hospital of Nanjing Medical University (approval number, 2025-SR-1229) and was conducted in accordance with the Declaration of Helsinki. Written informed consent was obtained from all participants.”
- **Incorrect (AI):** Given the sensitive nature of clinical research and our deep commitment to protecting patient rights and welfare, we took great care to ensure that all ethical standards were rigorously upheld throughout the study, and appropriate approvals were duly obtained.

**Why.** Reviewers and journals expect ethics as verifiable facts (which board, which consent path, why) — not as a display of virtue. The justification clause ('owing to the retrospective design', 'as the data were anonymized') is the load-bearing part: it shows the writer understands WHY a waiver is defensible. AI virtue-signaling ('deep commitment', 'great care') is content-free and immediately reads as non-clinical.

**Anti-repetition.** Rotate the waiver justification wording ('owing to the retrospective study nature' / 'due to the nature of a retrospective study' / 'because it conducted only a retrospective analysis of prospectively collected clinical management data') and do not append an approval number to every instance — many A papers give one, some give none. For prospective/RCT work flip to 'written informed consent was obtained' and let the registration ID / CONSORT tag sit nearby rather than manufacturing a waiver.

### Inclusion/exclusion as numbered lists keyed to concrete clinical thresholds {#inclusion-exclusion-numbered-clinical-thresholds}
*INVARIANT · genres: A,B,C* · Ref: paper03, paper02, paper20

**Principle.** Eligibility is rendered as an explicitly enumerated list ((1)(2)(3) or (i)(ii)(iii)) in which each criterion carries a concrete, decision-usable threshold — an age cut, an NIHSS or mRS band, a stenosis percentage, a time window, an imaging-confirmed occlusion site — rather than a prose paragraph of adjectives. The group frequently pins WHY a homogeneity criterion exists ('To keep the homogeneity of the enrolled patients, we limited...'). A and B carry the fullest self-authored criteria; C often DELEGATES the full list to the parent trial ('detailed in Appendix S1' / 'reported previously') and states only the analysis-specific inclusions.

- **Correct** (paper03): “The main inclusion criteria for recanalization treatment included: (1) age 18-80 years; (2) atherosclerotic total occlusion of the internal carotid artery (ICA) from the bifurcation or bulb upwards that was confirmed by digital subtraction angiography (DSA); (3) ischemic events (ipsilateral amaurosis fugax, TIA, or ischemic stroke) that occurred within the past 6 months and the most recent ischemic stroke must have occurred more than 2 weeks ago;”
- **Correct** (paper02): “To keep the homogeneity of the enrolled patients, we limited our study to patients with LVO in anterior circulation, including intracranial internal carotid artery occlusion (ICA) or proximal middle cerebral artery occlusion (M1) based on preoperative CT angiography;”
- **Correct** (paper20): “Detailed inclusion and exclusion criteria for the parent trial are shown in the eMethods in Supplement 1.”
- **Incorrect (AI):** We included a broad range of adult stroke patients who were deemed clinically appropriate for the study and who had undergone the relevant treatment, while excluding those with significant comorbidities or incomplete data that could potentially confound the results.

**Why.** Concrete thresholds are the reproducibility surface of the study — another center can apply age 18-80, NIHSS >=6, stenosis 70-99% verbatim. Vague eligibility ('broad range', 'clinically appropriate', 'significant comorbidities') is unauditable and unreproducible, and is the classic signature of a writer who has not actually run a cohort. The occasional inline rationale ('to keep homogeneity') shows methodological self-awareness reviewers reward.

**Anti-repetition.** Alternate the enumerator style the corpus actually uses ((1)(2)(3) vs (i)(ii)(iii) vs bulleted) and vary the framing verb ('Inclusion criteria were as follows', 'Patients who met the following inclusion criteria were enrolled', 'Patients were included if they...'). For C, resist re-listing the whole parent-trial criteria — point to the supplement/prior publication and only spell out THIS analysis's added restrictions, mirroring papers 20, 29, 31.

### Endpoints defined via named scales/classifications, each anchored to a citation or an inline range gloss {#endpoints-named-classification-with-inline-gloss}
*INVARIANT · genres: A,B,C* · Ref: paper02, paper21, paper03

**Principle.** Every outcome is operationalized through a named, citable instrument — mRS, NIHSS, mTICI/eTICI, ASPECTS/pc-ASPECTS, Heidelberg Bleeding Classification, NASCET/WASID, Hunt-Hess/Fisher — and the definition is bound to the scale, not invented ad hoc. sICH is repeatedly defined by pointing to a named classification plus a numeric deterioration rule (>=4 NIHSS points). C papers additionally gloss each scale's numeric range and polarity inline the FIRST time it appears ('mRS, scores range from 0 to 6, with higher scores indicating greater disability'), a courtesy A/B usually replace with a superscript citation to the defining paper.

- **Correct** (paper02): “sICH was defined according to the Heidelberg Bleeding Classification.9 ... Successful recanalization was defined as grade >=2b of the modified Thrombolysis in Cerebral Infarction score.”
- **Correct** (paper21): “The primary outcome was the score on the modified Rankin scale at 90 days (scores range from 0 to 6, with higher scores indicating greater disability), and the primary objective was to determine whether a shift in the distribution of the scores... had occurred between the two groups.”
- **Correct** (paper03): “Restenosis was defined as >70% stenosis or total reocclusion of the previously recanalized ICA. A threshold of peak systolic velocities of 300 cm/s, consistent with prior studies,21 was used to diagnose >70% stenosis.”
- **Incorrect (AI):** The primary outcome was a good clinical result at follow-up, reflecting whether patients experienced a meaningful improvement in their overall functional status and quality of life after treatment.

**Why.** Named scales make outcomes comparable across trials and immune to authorial spin — 'mRS 0-2 at 90 days' means the same thing everywhere, whereas 'good clinical result' is unmeasurable and unpoolable. The consistent pattern of scale-name + numeric rule + citation is what lets these papers feed meta-analyses. Undefined evaluative outcomes ('meaningful improvement', 'good result') are the fastest way to fail a Methods review.

**Anti-repetition.** Do not gloss the SAME scale's range on every appearance — glossing is a first-mention courtesy (heavy in C, light in A/B). Vary the definitional verb ('was defined as' / 'was defined according to' / 'was considered' / 'was categorized as') and let some definitions lean on a superscript citation instead of an inline range, matching whichever genre you are writing.

### Blinded adjudication with a named reader hierarchy and disagreement-resolution rule {#blinded-adjudication-reader-experience-hierarchy}
*INVARIANT · genres: A,B,C* · Ref: paper02, paper09, paper06

**Principle.** Image/outcome assessment is done by blinded readers arranged in an explicit escalation hierarchy, and the tie-breaking rule is stated. The recurring A/B shape is 'two [neuro]radiologists blinded to clinical data independently evaluated..., and disagreements were resolved by a third/senior reader by consensus'. B foregrounds each reader's YEARS of experience (the reader is the measuring instrument, so calibration is the datum) and reports an inter-reader kappa/ICC. C hoists adjudication to an institutional 'independent clinical event committee / imaging core laboratory, blinded to treatment allocation' — a body, not named individuals.

- **Correct** (paper02): “Two neuroradiologists who were blinded to the patient's medical information, including laboratory characteristics, independently evaluated all imaging findings. For any divergence between the two assessors, another experienced neuroradiologist reassessed the neuroimages and helped to reach a final consensus.”
- **Correct** (paper09): “Two neuroradiologists with 7 years (C.-Q.S.) and 16 years (S.L.) of experience independently evaluated all UHR PCD-CTA and simulated EID-CTA images... Disagreements were resolved by consensus and, when necessary, adjudicated by a senior neuroradiologist (F.-Y.W., with 30 years of experience).”
- **Correct** (paper06): “The incidence of stroke was determined by an independent outcome committee and an imaging core laboratory, both blinded to treatment allocation.”
- **Incorrect (AI):** All images were carefully assessed by our experienced team of radiologists, who worked together to ensure accurate and reliable evaluations of every case in the study.

**Why.** Blinding + independent reads + a stated tie-breaker is the bias-control machinery of any measurement study; naming the escalation path proves the readers could not silently negotiate away disagreement. In imaging-biomarker (B) work the readers' experience and their kappa ARE the reliability evidence, so they are quantified. AI's 'experienced team... worked together' erases exactly the independence and blinding the design depends on and reads as a writer papering over the method.

**Anti-repetition.** Vary reader count and the tie-break verb ('resolved by consensus' / 'a third reader made the final decision' / 'adjudicated by a senior neuroradiologist' / 'reached consensus through further discussion'). Include years-of-experience and a kappa/ICC when writing B (measurement reliability), but do NOT bolt experience-in-years onto C committee sentences — C uses an anonymous blinded committee/core-lab by design. When outcomes are clinical not imaging (mRS by phone), the 'reader' becomes a trained/blinded nurse or investigator; mirror that.

### Statistics march distribution-summary first, then comparison tests, then the modeling machinery, closing on software + two-sided alpha {#stats-distribution-first-then-machinery}
*INVARIANT · genres: A,B,C* · Ref: paper01, paper02, paper25

**Principle.** The Statistical Analysis paragraph follows a fixed clinical march: (1) how continuous vs categorical variables are summarized (mean/SD or median/IQR 'as appropriate'; counts/percentages), (2) which tests compare groups (t/Mann-Whitney; chi-square/Fisher), (3) the inferential engine (univariate screen at P<0.1 feeding multivariable logistic/Cox; or PSM/IPTW; or the trial's pre-specified ordinal/Poisson model), and (4) a closing stamp of the software package(s) with version and a two-sided significance threshold. The 'as appropriate' hedge is doing real work — it signals the choice is data-driven (checked for normality), not lazy.

- **Correct** (paper01): “Continuous data were appropriately presented as median (interquartile range [IQR]) or mean (standard deviation [SD]), appropriately. ... SPSS version 24 (IBM Corp., Armonk, NY, USA) and R software (version 4.0.2) were employed for analysis. Two sides P < 0.05 were considered statistically significant.”
- **Correct** (paper02): “Those predictors found to be associated with sICH on univariate analysis (P<0.10) were then enrolled into the multivariate logistic regression analysis to determine independent predictors.”
- **Correct** (paper25): “The primary outcome was analyzed by modified Poisson regression with robust error estimation as prespecified in the statistical analysis plan (Supplement 1), adjusting for time from onset or last known well time to randomization (0 to 9 hours vs 9 to 24 hours) and vessel occlusion site (ICA vs other).”
- **Incorrect (AI):** We used a variety of advanced statistical methods to thoroughly analyze the data and uncover meaningful relationships between the key variables, applying appropriate tests wherever necessary to guarantee the robustness of our findings.

**Why.** The distribution-then-test-then-model order is the shared grammar of clinical biostatistics; a reader scans it to check the tests match the data types and the multivariable model is honestly built (pre-specified covariates, a stated entry threshold). The software-version-plus-alpha closer is a reproducibility signature. Vague 'variety of advanced methods... robustness of our findings' names no test, no model, no threshold — it is the hallmark of a writer who cannot actually specify the analysis.

**Anti-repetition.** The march is an ORDER, not a script — do not reuse identical sentences. The P<0.1 univariate-screen threshold belongs to A/B predictor papers; C RCTs instead name ITT/per-protocol populations, a pre-specified primary model (ordinal logistic / modified Poisson / mixed-effects), and an explicit no-multiplicity-adjustment caveat for secondary outcomes — do not graft the P<0.1 screen onto an RCT. Rotate the closing software (SPSS/R/SAS/Stata with versions) and the two-sided-alpha phrasing; keep 'as appropriate' occasional, not on every clause.

### C: cohort is a named, registered trial introduced by an appositive stack of design adjectives {#c-named-trial-design-adjective-stack}
*VARIANT · genres: C* · Ref: paper28, paper32, paper25

**Principle.** In RCT / post-hoc / secondary-analysis voice, the sample is not raw patients but a NAMED trial (acronym expanded), and its architecture is delivered as a stacked appositive of design adjectives in a canonical order — center-multiplicity, prospective, blinding/masking status, control type, randomization — immediately followed by the registration identifier and a 'reported previously / detailed elsewhere' pointer to the design paper. Post-hoc and secondary analyses explicitly flag themselves ('This study is a prespecified secondary analysis of...' / 'the post hoc analysis conducted in this study').

- **Correct** (paper28): “The BAST trial was a multicenter, double-blind, placebo-controlled, parallel-group randomized clinical trial involving patients with acute ischemic stroke who received intravenous thrombolysis and/or endovascular treatment. Details of the trial rationale, design, and methods have been published previously21 and can be found in Supplement 1.”
- **Correct** (paper32): “This study is a prespecified secondary analysis of the ANGEL-ASPECT trial (unique identifier: NCT04551664),23 a multicenter, prospective, randomized, open-label, blinded-end point clinical trial conducted in China from October 2, 2020, to May 18, 2022...”
- **Correct** (paper25): “The OPTIMISTIC (One Pass Tirofiban in Management of Ischemic Stroke Thrombectomy in China) trial was a multicenter, prospective, open-label, blinded, end point phase 2 randomized clinical trial comparing intravenous tirofiban with usual care...”
- **Incorrect (AI):** This was a large, well-designed clinical trial that used a rigorous randomized approach to compare the two treatments in a fair and unbiased manner across multiple hospitals.

**Why.** The design-adjective stack is a compressed, standardized disclosure — each adjective ('open-label', 'blinded-endpoint', 'placebo-controlled', 'parallel-group') is a specific methodological commitment a reader must know to weigh bias, and the registration ID makes the pre-registration auditable. Self-praise ('large, well-designed', 'rigorous', 'fair and unbiased') asserts what the adjectives are supposed to PROVE and is precisely the tone real trial reports avoid.

**Anti-repetition.** Do not force every C paper into one adjective order or length; the stack flexes ('investigator-initiated, multicenter, randomised, single-blind, sham-controlled' vs 'multicenter, prospective, open-label, adaptive, randomized controlled, phase 3'). Secondary analyses lead with their OWN framing ('prespecified secondary analysis of', 'extension of', 'post hoc analysis of') before the parent-trial appositive. Never call the trial 'well-designed' or 'rigorous' — let the adjectives carry it.

### B: the imaging protocol is the methodological heart, given as scanner make/model plus parenthetical parameter bursts {#b-imaging-protocol-parenthetical-parameter-burst}
*VARIANT · genres: B* · Ref: paper07, paper09

**Principle.** In imaging-biomarker/technique papers the acquisition protocol is treated as the primary method (not an aside): a dedicated subsection names the exact scanner (make, model, field strength, coil) and lists sequence parameters as compact parenthetical bursts (TR/TE/FOV/matrix/slice thickness), then specifies the processing software and the quantitative extraction. This is where B's higher passive-voice and higher parenthesis density live, and it is legitimate — the machine and its settings ARE the experiment, so they are enumerated with instrument-manual precision.

- **Correct** (paper07): “All MRI examinations were conducted using a 3.0-T scanner (Magnetom Skyra, Siemens Healthcare) with a 20-channel head-neck coil. The imaging protocol included DWI (TR, 6400 ms; TE, 98 ms; FOV, 220 x 220 mm2; matrix, 192 x 192; slice thickness, 4 mm; 20 slices), and SWI (TR, 28 ms; TE, 20 ms; FOV, 220 x 220 mm2; matrix, 384 x 307; slice thickness, 2 mm; 48 slices).”
- **Correct** (paper09): “All examinations were performed using a dual-source PCD-CT system (NAEOTOM Alpha; Siemens Healthineers) operated in the Quantum HD UHR mode. The scanning parameters were as follows: tube voltage, 120 kVp; CARE keV image quality level, 125; pitch, 0.85; rotation time, 0.25 second; and collimation, 120x0.2 mm.”
- **Correct** (paper07): “All image processing and numeric fitting were performed with MATLAB 2020a (The MathWorks). A reformatted DWI image, matching the spatial location and matrix size of the CEST image, was reconstructed using in-house software.”
- **Incorrect (AI):** Advanced MRI imaging was performed on a state-of-the-art scanner using an optimized protocol carefully tuned to capture high-quality images suitable for our sophisticated analysis of the ischemic lesions.

**Why.** For a technique paper, another site can only replicate the biomarker if it can reproduce the exact acquisition — so make/model/field-strength and every sequence parameter are the reproducibility payload, and the parenthetical burst is the field's compact convention for delivering them. Adjectival hand-waving ('state-of-the-art', 'optimized', 'carefully tuned', 'sophisticated') gives a replicator nothing and marks the writer as outside imaging methodology. High passive voice here ('examinations were conducted', 'parameters were as follows') is correct, not a flaw to edit out.

**Anti-repetition.** This move belongs to B (and to the imaging-protocol subsection of C/A registry papers that report their own acquisition) — do NOT inject scanner-parameter bursts into a purely clinical A cohort that only pulled EMR variables. Vary the carrier ('scanned using the following parameters', 'the imaging protocol included', 'parameters were as follows') and let CT papers pivot to tube-voltage/pitch/collimation while MR papers give TR/TE/FOV/matrix. Keep the parentheticals as terse lists, not sentences.


## Results {#results}

> **A/B/C divergence:** A (single-center/observational/prognostic/procedural, Nanjing circle + some multicenter-observational): Results is a predictor hunt. Flow: enrollment/exclusion narrative -> baseline paragraph -> group-contrast paragraph(s) built from n(%) and median(IQR) -> univariate-then-multivariate OR/HR block -> often a ROC/cut-off + score/nomogram paragraph. Effect currency = OR or HR 'independently associated with' / 'independent predictor of'. B (imaging-biomarker/technique): Results is a measurement/agreement report. Same n(%)+median(IQR) spine but the effect currency shifts to diagnostic-accuracy metrics (sensitivity/specificity/PPV/NPV/accuracy, AUC with 95% CI, cut-off), inter-rater agreement (Cohen kappa / ICC / weighted kappa), and correlations (r, p). Group contrast is often good-vs-poor / with-vs-without a marker. B carries the highest Results hedge of the three (still low), reflecting qualitative image-quality language ('barely identifiable', 'clearly delineated'). C (RCT/post-hoc/meta-analysis, NEJM/Lancet/JAMA voice): Results is a two-arm outcome contrast anchored to a prespecified hierarchy (primary outcome first, then secondary, then safety, then subgroup). Effect currency = a NAMED randomized effect measure (rate ratio, common odds ratio, risk ratio, generalized OR, adjusted hazard ratio, beta coefficient) with unadjusted AND adjusted values. Enrollment sentence is date-bracketed ('Between DATE and DATE'). Two NEJM-style papers (21, 22) compress the whole Results into a single dense structured-abstract paragraph.

### Open on the enrollment/flow narrative, never on a headline rate {#no-abs-rate-lead-enrollment-first}
*INVARIANT · genres: A,B,C* · Ref: paper02, paper03, paper24

**Principle.** The Results section (and each subsection) opens by accounting for the denominator — screened, excluded, enrolled, analyzed — as running prose, not by leading with the study's most striking percentage. The reader is walked from the source population to the analyzed cohort before any effect is quoted. The punchy standalone rate as a topic sentence ('One in five patients...') is absent; the fingerprint confirms results_abs_rate_lead_frac is ~0 across all three genres.

- **Correct** (paper02): “During the study period, a total of 395 patients treated with EVT, were enrolled in this study (figure 1). The average age was 69.7±12.7 years, 207 (52.4%) patients were male, and 116 (29.4%) were treated with intravenous thrombolysis.”
- **Correct** (paper03): “A total of 347 patients with atherosclerotic symptomatic non-acute ICAO eligible for recanalization treatment were identified. Technical recanalization failure led to the exclusion of 58 patients, while 37 were excluded due to insufficient follow-up imaging data. Thus, 252 patients with 252 successfully recanalized ICAs were included.”
- **Correct** (paper24): “Between April 22, 2021, and Feb 5, 2023, 473 patients were screened, and 282 were enrolled and assigned to either the normobaric hyperoxia group (n=140) or the sham normobaric hyperoxia group (n=142).”
- **Incorrect (AI):** Nearly one in five stroke patients in our cohort went on to develop a symptomatic intracranial hemorrhage. Overall, 48 of 395 patients (12.2%) experienced this devastating complication after thrombectomy.

**Why.** Leading with the flashiest rate is a soft-news / AI move that editorializes ('devastating') and inverts the group's actual habit, which is to establish the analyzed denominator first so every downstream percentage is anchored. The group treats the flow diagram sentence as the mandatory first beat.

**Anti-repetition.** The opening verb varies by design and must not be forced into one stem: observational cohorts use 'A total of N ... were included/identified' or 'During the study period, N were enrolled'; registries use 'Of the N patients ... enrolled in the [REGISTRY] registry, M met the eligibility criteria'; RCTs use the date-bracketed 'Between DATE and DATE, N were screened'. Do not template every paper to 'A total of N patients'.

### Absolute count first, percentage in parentheses, denominator recoverable {#count-then-percent-denominator}
*INVARIANT · genres: A,B,C* · Ref: paper05, paper19, paper25

**Principle.** Every categorical result is reported as the integer count immediately followed by its percentage in parentheses — n (%) — and when the denominator is not the whole cohort it is spelled out as n/N (%). The raw number leads; the percentage is the parenthetical gloss, never the other way round. This lets the reader reconstruct the fraction and see small-n fragility.

- **Correct** (paper05): “A total of 62 (19.1%, 62/325) patients experienced an unfavorable outcome at the 3-month follow-up.”
- **Correct** (paper19): “Successful reperfusion—defined as modified treatment in cerebral ischemia 2b–3—was achieved in 112 of 129 procedures (86.8%).”
- **Correct** (paper25): “In the DES group, 2 of the 132 patients (1.5%) had an unsuccessful NOVA stent placement and received the Apollo stent.”
- **Incorrect (AI):** A substantial 19.1% of patients experienced an unfavorable outcome, while the vast majority (over 80%) recovered well. Reperfusion was successful in the overwhelming majority of procedures (86.8%).

**Why.** Percentage-first with an editorial quantifier ('a substantial', 'the vast majority', 'overwhelming majority') is the templated AI register. The group's count-first n/N (%) form is denser, verifiable, and value-neutral; it also surfaces small denominators (2 of 132) that a bare percentage would hide.

**Anti-repetition.** Alternate the connective form so it does not read as a fill-in-the-blank: 'X occurred in n (%)', 'n (%) had X', 'n of N (%) achieved X', 'X was achieved in n of N (%)'. Attach n/N specifically when the denominator differs from the section's main N (missing data, subgroup); use plain n (%) when it equals the main N.

### Continuous data as median (IQR) or mean ± SD, dispersion always attached {#central-tendency-with-dispersion}
*INVARIANT · genres: A,B,C* · Ref: paper02, paper19, paper09

**Principle.** Continuous variables never appear as a bare point estimate: skewed data are given as median (IQR) and normally distributed data as mean ± SD (or mean [SD]), with the distributional choice implicitly justified by which form is used. The unit rides with the number. The same value is reported the same way everywhere it appears.

- **Correct** (paper02): “The median National Institute of Health Stroke Scale (NIHSS) score was 16 (IQR 12–21) and the median Alberta Stroke Program Early CT Score (ASPECTS) was 9 (IQR 7–9).”
- **Correct** (paper19): “217 patients were included in the final analysis (median age, 66 years [IQR, 58–73 years]; age range, 18–91 years; 160 men).”
- **Correct** (paper09): “The final cohort consisted of 43 patients (mean age, 63.1 years ± 9.5; 8 women) with 51 stents.”
- **Incorrect (AI):** Patients were generally quite sick on admission, with NIHSS scores that were typically in the mid-teens, and were mostly of advanced age.

**Why.** Vague verbal central tendency ('generally quite sick', 'typically in the mid-teens', 'mostly of advanced age') is the antithesis of the group's numerical register. Attaching IQR or SD is not decoration — it signals whether a t-test or Mann-Whitney was used and lets the reader judge spread.

**Anti-repetition.** Do not mechanically wrap every continuous variable in the same bracket order. Real exemplars mix 'median X (IQR a–b)', 'X (IQR, a–b)', 'mean X ± SD', 'mean, X (SD)', and occasionally add range as a third element. Match the form the paper's own methods declared for that variable rather than defaulting to median(IQR) for all.

### Effect estimate + 95% CI + exact P bundled in one parenthetical {#adjusted-effect-ci-p-one-parenthetical}
*INVARIANT · genres: A,B,C* · Ref: paper02, paper05, paper19

**Principle.** When an association or between-group difference is quantified, the effect estimate, its 95% CI, and the exact P value travel together inside a single semicolon-delimited parenthetical attached to the clause that names the comparison. P is reported to its actual value (e.g., P=0.023, P=0.008) and only bottoms out at a threshold (P<0.001) — never 'p<0.05' as a catch-all, and never 'significant' without the number behind it.

- **Correct** (paper02): “ICA occlusion (acOR=2.79; 95% CI 1.40 to 5.58) were significantly associated with sICH after EVT”
- **Correct** (paper05): “Multivariate analysis revealed that only Hunt–Hess grade 4 to 5 (OR, 3.13 [95% CI, 2.11–4.64]; P<0.001), the presence of IVH (OR, 3.58 [95% CI, 1.72–7.46]; P=0.001), and smoking (OR, 2.44 [95% CI, 1.12–5.28]; P=0.024) were independently associated with”
- **Correct** (paper19): “This corresponded to an adjusted relative risk of 1.67 (95% CI: 1.14, 2.45; P = .008) and an adjusted risk difference of 0.16 (95% CI: 0.04, 0.29).”
- **Incorrect (AI):** ICA occlusion emerged as a highly significant and clinically meaningful predictor of hemorrhage (p<0.05), strongly suggesting that occlusion location plays a pivotal role in bleeding risk.

**Why.** 'Highly significant', 'clinically meaningful', 'pivotal role', and a lone 'p<0.05' are all AI amplifiers that replace the estimate with adjectives. The group lets the CI width and exact P carry the strength of evidence; interpretation is deferred to the Discussion, so the Results clause stays a bare quantified association.

**Anti-repetition.** The internal punctuation and label vary by journal house style and must be preserved, not homogenized: some papers use 'OR, 3.13 [95% CI, 2.11–4.64]; P<0.001', others 'acOR=2.45; 95% CI 1.75 to 3.43', others 'adjusted relative risk of 1.67 (95% CI: 1.14, 2.45; P = .008)'. Do not rewrite them all into one bracket convention. Vary the framing verb too: 'independently associated with', 'independent predictor of', 'corresponded to', 'yielded'.

### State non-significance and null findings flatly, with the number, no rescue language {#flat-nonsignificance-no-editorial}
*INVARIANT · genres: A,B,C* · Ref: paper31, paper02, paper20

**Principle.** Non-significant and null results are reported as plainly as significant ones — the comparison and its P (or CI crossing 1) are given, and the sentence stops. The group does not soften a null with 'trend toward', 'approached significance', or 'promising' beyond what the data show, and it does not decorate a positive with 'remarkably/strikingly/importantly'. Results hedge is ~0: the section carries almost no epistemic cushioning.

- **Correct** (paper31): “The symptomatic ICH rate of the rescue therapy group was similar to the MT alone group (9.7% vs 12.4%; OR 0.76, 95% CI 0.37 to 1.55; P=0.44).”
- **Correct** (paper02): “Significant differences were not found for the other baseline characteristics in patients with and without sICH.”
- **Correct** (paper20): “There were no significant differences in the causes of death between the 2 groups.”
- **Incorrect (AI):** Encouragingly, although the difference did not quite reach statistical significance, there was a strong and promising trend suggesting rescue therapy may importantly reduce hemorrhage risk (P=0.44), which is certainly worthy of attention.

**Why.** 'Encouragingly', 'strong and promising trend', 'may importantly reduce', 'worthy of attention' spin a null (P=0.44) into a near-positive — the exact editorializing the fingerprint's ~0 Results hedge rules out. The group reports the null, gives the number, and moves on; any hope for the finding is confined to the Discussion.

**Anti-repetition.** Vary the null phrasing across a section so it does not become a refrain: 'no significant difference', 'were similar between the two groups', 'did not differ significantly', 'was comparable', 'Significant differences were not found for'. Where a genuine numeric trend exists the group does say 'trend toward' or 'numerically higher ... with no significant difference' — reserve that for cases where the point estimate actually leans, and still attach the number.

### Order numbers cohort-context first, then group contrast, then adjusted model {#ordering-context-then-contrast-then-adjusted}
*INVARIANT · genres: A,B,C* · Ref: paper05, paper30, paper25

**Principle.** Within a subsection the numbers flow in a fixed logical order: first the descriptive/cohort context (who, how many, baseline), then the unadjusted between-group contrast (X vs Y with its P), then the adjusted estimate that survives multivariable modeling. The reader always sees the crude comparison before the adjusted one, and the baseline before the outcome. Numbers are grouped by clinical variable, not scattered.

- **Correct** (paper05): “the group with aSAH had higher proportions of rehemorrhage during hospitalization (8.8% versus 0%, respectively; P=0.027). Patients with aSAH also had statistically significantly higher in-hospital mortality (11.2% versus 1.5%; OR, 8.04 [95% CI, 1.07–60.12]; P=0.042) and DCI (12.3% versus 3.1%; OR, 4.42 [95% CI, 1.03–18.95]; P=0.045) rates”
- **Correct** (paper30): “the proportion of functional independence at 90 days remained significantly higher in the EVT group than in the SMT group (111 of 161 patients [68.9%] versus 69 of 154 patients [44.8%]) with an adjusted OR of 3.69 (95% CI, 2.04–6.68; P<0.001).”
- **Correct** (paper25): “the DES group had a significantly smaller degree of stenosis at the 1-year follow-up (median [IQR], 23.2% [13.6%-35.3%] vs 32.5% [20.5%-51.8%]), with a median difference of 7.5% (95% CI, 2.4%-12.4%; P = .003)”
- **Incorrect (AI):** The adjusted odds ratio was highly significant. Mortality was much worse in one group. When we looked at the raw numbers, they also differed, and the confidence interval was wide but reassuring overall.

**Why.** Presenting the adjusted OR before the raw rates, and narrating in vague relative terms ('much worse', 'wide but reassuring'), destroys the crude-then-adjusted logic the group relies on. The exemplars always pair the actual rates (with denominators) to the effect estimate in the same sentence, in ascending order of statistical processing.

**Anti-repetition.** The 'A vs B' contrast has several equivalent surface forms — 'X% versus Y%', 'n of N (%) versus n of N (%)', 'median [IQR] vs median [IQR]' — rotate them by data type rather than repeating one. Keep the group-name order consistent within a paper (e.g., always treatment-then-control) but do not impose a single template across variables.

### A: frame findings as predictors — univariate screen, then multivariable 'independently associated' {#A-predictor-currency-or-hr-independent}
*VARIANT · genres: A (and A-style predictor work in B)* · Ref: paper03, paper15, paper02

**Principle.** In the observational/prognostic genre the analytic payload is a predictor model: variables that pass a univariate screen (stated P threshold, e.g. P<0.1) enter multivariable regression, and the surviving variables are reported as 'independent predictors of' / 'independently associated with' the outcome, each with its adjusted OR or HR, 95% CI, and P. The section frequently closes with a ROC/cut-off, risk score, or nomogram derived from those predictors.

- **Correct** (paper03): “Occlusion length ... residual stenosis ≥30% (HR 3.08, 95% CI 1.79 to 5.30, P<0.001), as well as post-recanalization ICA wall collapse (HR 1.96, 95% CI 1.12 to 3.44, P=0.018) were independent predictors of restenosis.”
- **Correct** (paper15): “older age (OR, 1.12; 95% CI, 1.04–1.22; P = 0.005), female sex (OR, 3.79; 95% CI, 1.08–13.40; P = 0.038) ... were independently associated with the occurrence of FR after thrombectomy.”
- **Correct** (paper02): “the optimal cut-off value of D-dimer as a predictor for predicting sICH was 2.27 mg/L, which showed a sensitivity of 64.6% and a specificity of 86.2%, a negative predictive value of 94.6%, and had an area under the curve of 0.774”
- **Incorrect (AI):** Several risk factors were found to be important. Age and sex both mattered, and D-dimer was a key driver, making it a very useful biomarker for identifying at-risk patients in clinical practice.

**Why.** 'Important', 'mattered', 'key driver', 'very useful ... in clinical practice' replace the model output with clinical editorializing that belongs in the Discussion. The A-genre voice reports the adjusted estimate and the phrase 'independently associated with' and lets the cut-off/AUC stand as the evidence, without asserting clinical utility inside Results.

**Anti-repetition.** Do not reuse one closing verb for every predictor list — the corpus alternates 'were independent predictors of', 'were independently associated with', 'were identified as independent risk factors of'. When a ROC/score follows, report sensitivity/specificity/AUC in the paper's own order; some lead with the cut-off value, others with the AUC.

### B: report diagnostic-accuracy and agreement metrics as the primary currency {#B-accuracy-agreement-currency}
*VARIANT · genres: B* · Ref: paper09, paper07

**Principle.** In the imaging-biomarker/technique genre the headline numbers are measurement-performance metrics — sensitivity, specificity, PPV, NPV, accuracy (each with its n/N), AUC with 95% CI and a cut-off, inter-rater agreement (Cohen kappa / weighted kappa / ICC with 95% CI), and correlations (r with p). Modality-vs-modality or marker-present-vs-absent comparisons are quantified with these, and qualitative image descriptors ('clearly delineated', 'barely identifiable') are allowed but always paired to a number.

- **Correct** (paper09): “UHR PCD-CTA achieved excellent diagnostic performance for ISR detection, with a sensitivity of 100.0% (14/14), specificity of 97.3% (36/37), positive predictive value of 93.3% (14/15), negative predictive value of 100.0% (36/36), and overall accuracy of 98.0% (50/51)”
- **Correct** (paper09): “Interobserver agreement for subjective image quality was excellent for both data sets, with weighted Cohen κ values of 0.919 (95% CI, 0.829–1.000) for UHR PCD-CTA and 0.905 (95% CI, 0.798–1.000) for simulated EID-CTA.”
- **Correct** (paper07): “A significant correlation was found between APT# values and NIHSS24h (r = −0.272, p = 0.015), as well as between APT# values and 90-day mRS (r = −0.369, p = 0.01) at a saturation power of 1 μT.”
- **Incorrect (AI):** The new imaging technique performed remarkably well and was clearly far superior to the conventional approach, detecting nearly every case of restenosis with outstanding reliability and near-perfect agreement between readers.

**Why.** 'Remarkably well', 'clearly far superior', 'outstanding reliability', 'near-perfect' are unquantified superlatives that stand in for the actual sensitivity/specificity/kappa. The B-genre voice keeps the n/N behind every accuracy metric (100.0% [14/14]) and the CI behind every kappa, so the reader sees exactly how many cases support the claim.

**Anti-repetition.** Agreement descriptors ('excellent', 'good', 'fair') are used but must be tied to the kappa/ICC value and its 95% CI, not free-floating — mirror the corpus which writes 'excellent ... with weighted Cohen κ of 0.919 (95% CI ...)'. Rotate the metric bundles: not every paragraph needs the full sens/spec/PPV/NPV set; correlation paragraphs use r and p, agreement paragraphs use kappa/ICC and CI.

### C: two-arm outcome contrast in prespecified hierarchy, effect measure named {#C-arm-contrast-named-effect-hierarchy}
*VARIANT · genres: C* · Ref: paper20, paper27, paper22

**Principle.** In the randomized-trial voice each result is a comparison between named treatment arms (group A vs group B), reported in the prespecified order primary -> secondary -> safety -> subgroup, and every contrast explicitly names its effect measure (rate ratio, risk ratio, common odds ratio, generalized odds ratio, adjusted hazard ratio, mean/beta difference) with both unadjusted and adjusted values plus CI and P. Enrollment is date-bracketed and the intention-to-treat / per-protocol framing is stated.

- **Correct** (paper20): “good functional status (mRS score 0-3) was observed in 99 of 222 (44.6%) patients in the thrombectomy group and 21 of 108 (19.4%) patients in the control group (adjusted rate ratio, 2.23; 95% CI, 1.51-3.29)”
- **Correct** (paper27): “The proportion of participants with a positive primary outcome rate was 65% (64 of 99) in the tirofiban group and 48% (46 of 95) in the control group (adjusted risk ratio [ARR], 1.34 [95% CI, 1.04-1.73]; P = .03)”
- **Correct** (paper22): “Functional independence at 90 days was seen in 58.6% of the patients in the thrombectomy group and in 46.6% of those in the control group (adjusted rate ratio, 1.24; 95% confidence interval, 1.07 to 1.44; P = 0.004).”
- **Incorrect (AI):** Thrombectomy was a game-changer: patients did dramatically better than controls, with far more achieving a good outcome, confirming that this intervention should become the new standard of care for these patients.

**Why.** 'Game-changer', 'dramatically better', 'confirming ... should become the new standard of care' is practice-changing spin injected into Results — the group defers that verdict to the Discussion/Conclusion. The C-genre Results names the effect measure and pins both rates with denominators; the trial's importance is left implicit in the CI that excludes 1.

**Anti-repetition.** Name the effect measure that the trial's analysis plan specifies rather than defaulting to 'odds ratio' everywhere — the corpus spans rate ratio, generalized odds ratio, common odds ratio, risk ratio, adjusted hazard ratio, and beta coefficient across outcomes within a single paper. Vary the arm-naming ('thrombectomy group'/'control group', 'tirofiban'/'control', 'EVT'/'SMT') to the trial. NEJM-format papers (21, 22) compress this whole hierarchy into one dense paragraph — do not force the full subsectioned layout onto that subtype.


## Discussion, Limitations & Conclusion {#discussion}

> **A/B/C divergence:** A (single-center/observational/prognostic/procedural CLINICAL) opens the Discussion by restating its OWN cohort finding as a clinical sentence ('In this cohort of patients with X, we identified/observed a Y incidence of...'), then benchmarks NAMED author-year prior series (Hernandez et al., Kao et al., Grossberg et al.) one at a time with their n and their number, keeps mechanism short and syntactically subordinate ('The possible explanations are as follows: first...'), and lands an explicit management paragraph with concrete actionable numbers ('we recommend ultrasound every 3 months'). Limitations are a numbered First/Second/Third list naming the bias TYPE (single-center retrospective, selection bias, ascertainment bias) and closing with 'larger/multicenter/prospective/RCT studies are needed'. Hedge density ~11. B (imaging-biomarker/technique) opens with an enumerated self-summary of findings ('Our study demonstrated three main findings. First,...Second,...Third,...'), spends most of the body on the technique/mechanism itself (the marker is the subject, not a patient outcome), benchmarks rival methods and thresholds (MTRasym, rCBF<20% vs <30%, Boned/Bivard/Sarraj), and frames clinical implication as 'a simple, accessible, reproducible imaging marker'. Same numbered limitations, but the highest 'however/therefore/moreover' connective density of the three. Hedge ~11. C (RCT / post-hoc / NEJM-Lancet-JAMA voice) opens with the trial result stated as ONE clinical sentence that names the setting and the comparator ('In this trial conducted in China, patients with X had better functional recovery with EVT than with usual medical management'), benchmarks other NAMED trials/registries by acronym and their numbers (RESCUE-Japan LIMIT, SELECT, BASICS, BEST, ATTENTION, SAMMPRIS, HERMES), quantifies effect in patient-facing terms (NNT, absolute percentage-point difference, 'about 4.5 of every 10'), and DEMOTES mechanism to explicitly labelled 'hypothesis-generating' status. Its limitations foreground statistical/design threats absent from A/B: multiplicity / type I error / not powered for subgroups, unblinding/open-label, and generalizability beyond the Chinese/Asian population. Lower hedge (~8) but more explicit statistical caveats.

### Open Discussion by restating THIS study's finding as a clinical sentence, not a topic sentence {#discussion-opener-restate-own-finding}
*INVARIANT · genres: A,B,C* · Ref: paper16, paper21, paper10

**Principle.** The first sentence(s) of the Discussion re-state what THIS study found, phrased for a clinician, before any prior literature is invoked. The group never opens with a generic disease-importance sentence or a literature-gap sentence in the Discussion (that belongs in the Intro). A/B anchor the restatement in their own cohort ('In this cohort of patients with X, we identified/observed a Y%...'); C anchors it in the trial ('In this trial conducted in China, patients with X had...'). The restatement carries the actual number or direction, not a vague 'we found associations'.

- **Correct** (paper16): “In this cohort of patients with cICA occlusion on CTA, we identified a PO incidence of 54.1% based on angiographic exploration. We further found that patients with PO had an increased risk of reperfusion failure and poor outcome compared with true occlusion patients after PSM, and this finding remained robust in the sensitivity analysis.”
- **Correct** (paper21): “In this trial conducted in China, patients with acute stroke with a large cerebral infarction caused by large-vessel occlusion in the anterior circulation had better functional recovery at 90 days with endovascular therapy administered within 24 hours after stroke onset than with usual medical management.”
- **Correct** (paper10): “Our study demonstrated three main findings. First, based on a multicenter trial conducted in China, we found that the occurrence rate of mMCAi was 13.2% in stroke patients after EVT for LVO of the anterior circulation.”
- **Incorrect (AI):** Acute ischemic stroke remains a leading cause of death and disability worldwide, and endovascular therapy has revolutionized its management. In this context, our study sought to shed light on an important question that has garnered increasing attention in recent years.

**Why.** This is the group's single most consistent Discussion move and the clearest 'clinical feel' signal: the reader is told the result in plain clinical terms up front. Reopening with disease burden or a gap statement is the classic AI/soft-news tell and duplicates the Introduction.

**Anti-repetition.** Do NOT hard-code 'In this [cohort/trial/study], we found...' as a fill-in slot. Vary the anchor: cohort description (A/B), trial-setting clause (C), or an enumerated 'three main findings' self-summary (B). The number that appears must be the study's real headline statistic, and its grammatical subject rotates (incidence, we, patients, the model).

### Benchmark against NAMED prior series/trials, one at a time, with their n and their number {#discussion-named-benchmarking}
*INVARIANT · genres: A,B,C* · Ref: paper01, paper10, paper06

**Principle.** Every Discussion positions its result against specific prior work identified by name (author-et-al in A/B; trial/registry ACRONYM in C), and carries that prior work's own sample size and/or its own reported figure so the reader can compare like-for-like. The group does NOT cite prior work as an anonymous bundle ('previous studies have shown'). When it agrees it says so ('consistent with', 'in line with'); when it differs it gives the number that differs and offers a reason.

- **Correct** (paper01): “Hernandez et al. conducted a single-center prospective non-inferiority investigation aimed to explore the non-inferiority of TRA versus TFA in terms of final recanalization for patients who received thrombectomy, involving 116 patients (13). Results revealed that TRA was non-inferior to TFA in achieving successful recanalization. However, the TRA cohort experienced significantly prolonged procedure time.”
- **Correct** (paper10): “The occurrence rate of mMCAi in our study was 13.2%, which was markedly lower than that reported by Davoli et al (35.7%) and that of Tracol et al (27.3%) [15, 18]. Both of these studies were performed in a single stroke center with limited study population (98 patients and 66 patients).”
- **Correct** (paper06): “In the CASSISS (China Angioplasty and Stenting for Symptomatic Intracranial Severe Stenosis) trial, the 3-year rate of ipsilateral ischemic stroke was higher in patients with stroke as the qualifying event (15.2%) compared with those with TIA (5.6%).”
- **Incorrect (AI):** Our findings are broadly consistent with the existing body of literature, as several previous studies have similarly reported associations between these variables and clinical outcomes, underscoring the robustness of this relationship.

**Why.** Named, numeric benchmarking is what makes the Discussion read as clinical scholarship rather than a generic literature nod; it also lets the group explain WHY its number differs (single-center vs multicenter, RCT selection, Asian population), which is a recurring analytic move.

**Anti-repetition.** Rotate the citation register by genre: A/B use 'Surname et al. reported/observed/found ... (n)'; C uses the full trial acronym expanded once. Vary the verb (reported, observed, found, revealed, demonstrated, examined) and vary whether agreement or divergence leads. Never stack three identical 'X et al. found Y' sentences in a row without an intervening interpretive sentence.

### Land an explicit clinical-implications / management paragraph with concrete, actionable guidance {#discussion-explicit-management-paragraph}
*VARIANT · genres: A,C (explicit actionable paragraph); B (utility-of-marker framing)* · Ref: paper03, paper30, paper13

**Principle.** The Discussion contains a dedicated turn that translates the result into what a clinician should DO. In A and C this is a concrete management recommendation (a follow-up interval, a selection rule, a caution to weigh benefit vs risk, a counseling use). In B the equivalent turn is framed as marker utility ('a simple, accessible imaging marker' that improves workflow / risk stratification) rather than a bedside order. The implication is stated as guidance, appropriately conditioned, not as a mechanistic aside.

- **Correct** (paper03): “Given these outcomes, we recommend more frequent ultrasound follow-ups, such as every 3 months, especially within the first 15 months post-recanalization for high-risk individuals. This approach enables early interventions to reduce the risk of recurrent ischemic strokes. Conversely, the follow-up interval for patients without restenosis predictors may be extended.”
- **Correct** (paper30): “In light of our findings, it is essential for clinicians to consider the potential benefits of EVT for patients with BAO with low NIHSS, as early intervention may significantly help patients regain functional independence.”
- **Correct** (paper13): “As for the potential clinical significance of this finding, we think that FVH is a simple, accessible, and reproducible imaging marker in clinical practice. If FVH is observed on the post-treatment MRI, a reinforced medication or rehabilitation therapy should be suggested or initiated as soon as possible for improving the prognosis.”
- **Incorrect (AI):** These findings have important clinical implications and may pave the way for improved patient management, ultimately contributing to better outcomes and a brighter future for stroke care.

**Why.** The management paragraph is the payoff that separates clinical writing from basic science: it names the decision, the population, and often the number (every 3 months, first-line alternative, weigh benefit vs risk). Vague 'important implications' with no actionable content is the AI/soft-news failure mode.

**Anti-repetition.** Do not always use 'These findings have significant clinical implications' as the lead-in (paper03 uses it once; do not repeat it as a template). Sometimes the recommendation is a caution rather than an action (weigh benefits/risks of EVT given the 11% hemorrhage risk difference, paper19; do not exclude older adults, paper15). For B, keep it marker-utility framing, not a bedside order.

### Keep mechanism short, hedged, and syntactically subordinate (except B, where the mechanism IS the object of study) {#discussion-mechanism-subordinate}
*VARIANT · genres: A,C (mechanism subordinate & hedged); B (mechanism is central and detailed)* · Ref: paper02, paper01, paper07

**Principle.** In A and C, pathophysiologic explanation is offered briefly, flagged as speculative ('possible explanation', 'may reflect', 'presumably', 'we tentatively attribute'), and is never allowed to become the point of the paragraph; the clinical fact leads and the mechanism trails. C goes further and explicitly downgrades mechanism to 'hypothesis-generating'. B is the exception: because the study object is a biomarker/technique, mechanism (edema cascade, saturation efficiency, coagulation-fibrinolysis) legitimately occupies much of the body, but is still hedged.

- **Correct** (paper02): “Therefore, the baseline D-dimer level correlated with sICH presumably because higher D-dimer levels indirectly reflected comorbid burden, which included advanced age, more severe neurological deficit, and faster infarct volume growth.”
- **Correct** (paper01): “The possible explanations are as follows: first, the radial heparin and antispasmolytic agents need to be prepared before the procedure. Second, unsuccessful radial artery puncture can lead to hematoma formation and radial artery spasm, increasing the difficulty of subsequent puncture attempts.”
- **Correct** (paper07): “Although the exact cause remains unclear, we tentatively attribute this larger error at high B1 to the possible decreased saturation efficiency at high B1.”
- **Incorrect (AI):** Mechanistically, this phenomenon is driven by a well-orchestrated cascade of molecular events: endothelial dysfunction triggers oxidative stress, which in turn activates inflammatory pathways that ultimately culminate in blood-brain barrier breakdown, thereby explaining our clinical observation.

**Why.** Foregrounding a confident mechanistic cascade is the hallmark of the 'too basic-science' voice the group avoids. Subordinating and hedging mechanism keeps the clinical decision, not the pathway, as the reader's takeaway. B is the principled exception and must be flagged so mechanism-heavy imaging papers are not mis-corrected.

**Anti-repetition.** Vary the speculation flag: 'possible explanation', 'may reflect', 'presumably', 'might be due to', 'we tentatively attribute', 'a prominent hypothesis suggests' — do not reuse one hedge verbatim across paragraphs. In A/C keep mechanism to a few sentences; in B it can run longer but must still be hedged and must return to the clinical/utility point.

### Limitations: numbered list, NAME the bias type, and where possible state its DIRECTION {#discussion-limitations-named-bias-direction}
*INVARIANT · genres: A,B,C* · Ref: paper09, paper08, paper01

**Principle.** Limitations are enumerated (First/Second/Third... or First/Second/Finally) and each names a specific, recognized bias or design threat by its technical name (single-center retrospective design, selection bias, ascertainment bias, residual/unmeasured confounding, verification bias, immortal-time/misclassification). The strongest instances also state the DIRECTION of the likely distortion (may underestimate, could inflate specificity, may have masked, potentially diluting the treatment effect), rather than a generic 'limitations should be acknowledged'.

- **Correct** (paper09): “In patients without suspected ISR-particularly asymptomatic individuals-DSA was not routinely performed to avoid unnecessary invasive procedures. This may introduce partial verification bias, which could potentially inflate estimates of specificity and negative predictive value.”
- **Correct** (paper08): “Fourth, the cross-group phenomenon caused by rescue EVT may introduce bias, potentially diluting the estimated treatment effect and underestimating the true benefit of EVT.”
- **Correct** (paper01): “Finally, the lack of long-term follow-up data may result in underestimation of potential access site complications, especially the incidence of asymptomatic radial artery occlusion.”
- **Incorrect (AI):** This study is not without limitations. As with any research of this kind, several factors should be taken into consideration when interpreting our findings, and future studies are warranted to address these limitations.

**Why.** Naming the bias and its direction demonstrates methodological literacy and is a strong reviewer-satisfaction / clinical-credibility signal. A contentless 'not without limitations' preamble followed by vague generalities is the AI/template failure mode.

**Anti-repetition.** Do not make every limitation the same shape. Mix bias-naming with direction-of-effect, and let some limitations concede a strength or a mitigation in the same breath (paper05 notes PSM as a partial remedy; paper19 reports a sensitivity analysis that answers the concern). Rotate the ordinal openers and occasionally break the list to argue why a limitation is unlikely to have driven the result.

### Close limitations with a calibrated call for external validation matched to the study's own reach {#discussion-call-for-external-validation}
*INVARIANT · genres: A,B,C* · Ref: paper03, paper25, paper19

**Principle.** The generalizability limitation and the call for further work are tuned to what the study actually is. Single-center A/B papers call for larger, multicenter, prospective, or randomized studies. Chinese/Asian cohorts and trials (all three genres) flag ethnic generalizability explicitly and call for validation in other populations. RCT/post-hoc C papers call for the NEXT trial (confirmatory phase 3, Western-population trial, pre-registered NCT) rather than 'more studies'. The call names the specific missing evidence, not a generic 'more research is needed'.

- **Correct** (paper03): “Third, the generalizability of our results might be limited, given the exclusive inclusion of Chinese patients. ... Therefore, larger prospective studies are needed to validate our findings, verify the accuracy of our scoring system, and further investigate factors influencing stenosis incidence.”
- **Correct** (paper25): “Together, the 2 trials generate a strong hypothesis that adjunctive tirofiban treatment should target patients with large vessel occlusion who have had acute ischemic stroke due to intracranial atherosclerotic disease and merit a future confirmatory phase 3 trial confined to this population.”
- **Correct** (paper19): “Given the study's nonrandomized design, missing data, center-level variability, and potential for residual confounding, these findings should be considered hypothesis-generating. Randomized controlled trials are therefore needed to determine whether EVT truly confers a net clinical benefit in this late-presenting population.”
- **Incorrect (AI):** Further research is needed to confirm these findings. Larger studies with longer follow-up would help to validate our results and expand our understanding of this important topic.

**Why.** A calibrated, specific call for validation shows the authors know exactly where their evidence sits on the design hierarchy; an observational A paper asking for RCTs and a C trial asking for the named next trial are different, deliberate moves. Generic 'further research is needed' is the interchangeable AI closer.

**Anti-repetition.** Match the ask to the design and never bolt an RCT call onto a paper that IS an RCT. Vary the phrasing (are needed / are warranted / merit a future trial / should validate / a complementary trial in a Western population is ongoing). Where a next trial exists, cite its NCT number (paper24, paper25) instead of an abstract call.

### Conclusion: one pragmatic, actionable sentence, hedged to the evidence level {#discussion-conclusion-pragmatic-hedged}
*VARIANT · genres: A (feasible/favor first-line, hedged); C (result + explicit benefit-and-harm, supports consideration); B (marker MIGHT serve as surrogate)* · Ref: paper01, paper22, paper12

**Principle.** The closing conclusion states a usable takeaway and calibrates its certainty to the design. A single-center observational papers hedge to feasibility/preference ('safe and feasible', 'may favor ... as first-line'). C trials state the directional result AND its accompanying harm in the same sentence and land on 'support consideration in carefully selected patients' rather than a blanket recommendation. B papers close on the marker's conditional potential ('might be a potential surrogate'). The conclusion never overclaims beyond what the study design licenses.

- **Correct** (paper01): “In conclusion, both TBA and TRA serve as safe and feasible access routes for neuro stenting. Furthermore, procedural delays in TRA may favor TBA as the first-line alternative access to TFA.”
- **Correct** (paper22): “In this trial involving patients with medium-vessel occlusion and moderate-to-severe deficits, endovascular thrombectomy plus medical management within 24 hours after symptom onset led to a significantly higher percentage of patients with functional independence than medical management alone but also led to a higher risk of symptomatic intracranial hemorrhage. These findings support the consideration of endovascular therapy in carefully selected patients with medium-vessel occlusion.”
- **Correct** (paper12): “Post-treatment DWI ASPECTS might be a potential surrogate of infarction volume in terms of providing the prognostic information for AIS patients after EVT.”
- **Incorrect (AI):** In conclusion, our study represents a significant step forward and provides compelling evidence that this intervention is highly effective and should be widely adopted in clinical practice to improve outcomes for all patients.

**Why.** The hedged-but-actionable close is the group's signature landing: it gives the reader something to do while respecting the design ceiling. Overclaiming ('highly effective', 'should be widely adopted', 'for all patients') is both the AI failure mode and a reviewer red flag for observational or single-center work.

**Anti-repetition.** Do not open every conclusion with 'In conclusion,' — several papers omit it or use 'In summary' / lead straight with the trial-setting clause. In C, keep the benefit-AND-harm pairing in one sentence rather than a clean benefit-only claim. Match the hedge strength to genre: 'safe and feasible / may favor' (A), 'support consideration in carefully selected' (C), 'might be a potential surrogate' (B) — never upgrade an observational finding to a practice mandate.

### Quantify the effect in patient-facing terms (NNT, absolute difference, 'X of every 10') — mainly the RCT voice {#discussion-quantified-effect-in-patient-terms}
*VARIANT · genres: C (dominant: NNT / absolute pp / natural-frequency framing); A occasional (fold-risk, high-vs-low-risk %); B rare* · Ref: paper22, paper20, paper03

**Principle.** The RCT/post-hoc voice translates the treatment effect into a quantity a clinician and patient can feel: number needed to treat, absolute percentage-point difference, or a natural-frequency statement ('about 4.5 of every 10'). This is stated alongside, not instead of, the relative estimate, and is often anchored to a comparison ('a magnitude similar to that reported for established reperfusion therapies'). A papers occasionally do a lighter version (fold-increase in risk, high-risk vs low-risk absolute rates); B papers rarely do this because their endpoint is a marker, not a treatment.

- **Correct** (paper22): “The absolute between-group difference of approximately 12 percentage points corresponds to a number needed to treat of 8.2 (95% CI, 3.1 to 13.3) to observe a functional-independence outcome - a magnitude similar to that reported for established reperfusion therapies in acute ischemic stroke.”
- **Correct** (paper20): “outcome rates ... were achieved in about 4.5 of every 10 patients in the thrombectomy group compared with about 2 of every 10 in the control group, yielding a number needed to treat of 4 for 1 more patient to achieve an mRS score of 0 to 3.”
- **Correct** (paper03): “Nearly 30% of high-risk patients developed restenosis 1 year after treatment, compared with 10% in the low-risk group.”
- **Incorrect (AI):** Nearly one in five patients experienced the outcome, and this striking finding highlights the substantial and clinically meaningful impact of the intervention on patient care.

**Why.** NNT / absolute-difference framing is a genuine RCT-voice fingerprint that grounds the effect in clinical decision terms and pairs relative and absolute estimates honestly. The AI failure mode is a decorative natural-frequency flourish ('nearly one in five', 'striking') that inflates significance without the paired absolute number or a benchmark.

**Anti-repetition.** This is genre-weighted: apply NNT/pp framing freely in C, sparingly and only when the study reports an absolute contrast in A, essentially never in pure B marker papers. Do NOT deploy 'nearly one in X patients' as a rhetorical opener — the old phrasebank's tell. When a natural-frequency phrase is used, it must carry the real paired numbers and, ideally, a benchmark for scale, not stand alone as emphasis. CRITIC-GUARD: the 'N of every 10' / natural-frequency phrase is licensed ONLY carrying the study's real paired arm counts AND a benchmark/NNT in the same sentence (paper20/22). A bare 'about N of every 10 patients' with no paired denominator is grammatically identical to the banned 'nearly one in five' AI tell — see clinical_ai_tells.md #tells.


## Quick Search Targets {#grep}
```
rg -n -A40 "#title-abstract" references/voice_principles.md   # all title-abstract moves
rg -n -A40 "#introduction" references/voice_principles.md   # all introduction moves
rg -n -A40 "#methods" references/voice_principles.md   # all methods moves
rg -n -A40 "#results" references/voice_principles.md   # all results moves
rg -n -A40 "#discussion" references/voice_principles.md   # all discussion moves
# jump to one move:
rg -n -A8 "#results-abs-rate" references/voice_principles.md   # (use any move slug)
```
