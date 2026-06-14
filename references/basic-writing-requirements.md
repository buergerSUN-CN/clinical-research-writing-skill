# Basic Academic-Writing Requirements

> Distilled from the **academic-research-skills (ARS)** plugin's writing-convention references
> (`academic_writing_style.md`, `writing_quality_check.md`, `writing_judgment_framework.md`,
> `paper_structure_patterns.md`, `statistical_reporting_standards.md`).

These are the FOUNDATIONAL academic-writing rules that sit **under** this skill's clinical-voice
guidance. The rest of the skill makes a paper read as genuine clinical research; this file covers the
generic IMRaD craft any reviewer assumes is already in place. Apply these as an editor's checklist, not
as prose advice. Where this skill's clinical references go further (effect interpretation, the
golden-thread consistency pass, clinical framing), those take precedence — this file does not repeat them.

## Contents
1. [Section roles — what each IMRaD section is FOR (and NOT for)](#1-section-roles)
2. [Sentence & paragraph craft](#2-sentence--paragraph-craft)
3. [Precision & hedging](#3-precision--hedging)
4. [Reporting & numbers basics](#4-reporting--numbers-basics)
5. [Do-not list](#5-do-not-list)

---

## 1. Section roles

Each section answers ONE question for the reader. Material that belongs to another section is a defect,
even when it is true and well written.

| Section | Answers | Contains | Does NOT contain |
|---------|---------|----------|------------------|
| **Introduction** | Why this study? | Problem, what is known, the specific gap, the aim/question (and primary outcome) | Methods detail, results, your own interpretation |
| **Methods** | Can I trust/reproduce this? | Design, population, variables, procedures, analysis plan, ethics — reproducible facts in the past tense | Results, justification framed as findings, interpretation |
| **Results** | What did you find? | Findings only: numbers, estimates, CIs, P values, tables/figures, described plainly | Interpretation, comparison to prior work, mechanism, "surprisingly/paradoxically", implications, limitations |
| **Discussion** | What does it mean? | Main finding restated, interpretation, comparison with literature, mechanism, implications, limitations | New results not shown in Results; restating every number |
| **Conclusion** | What do I remember/do? | The direct answer to the aim + one actionable take | Hedge-free overclaiming, new data, new arguments |

### The load-bearing rule: Results state, Discussion interprets

**Results report findings as facts and nothing else; the Discussion owns all interpretation, comparison,
mechanism, surprise/paradox framing, and implications.** If a Results sentence says what a finding
*means*, why it is *unexpected*, or what it *implies for practice*, it belongs in the Discussion.

- Results, allowed: "Mortality was 12% (n = 24/200) in the treatment group vs 19% (38/200) in controls
  (RR 0.63, 95% CI 0.39–1.01, P = .06)."
- Results, NOT allowed: "Surprisingly, despite the lower mortality, the difference did not reach
  significance, suggesting the treatment may still benefit patients." → move every clause after the
  numbers to the Discussion.
- Test each Results sentence: does it report an observation, or judge one? Judging = Discussion.
- Conversely, the Discussion should not re-list numbers; cite the finding by name and interpret it.

### Lead with the finding, not the test

In Results, the finding comes first and the statistic supports it — not the reverse. Write "Risk fell
by 7 percentage points (RR 0.63 …)", not "A chi-square test was performed, which yielded …".

---

## 2. Sentence & paragraph craft

### Paragraphs
- **One idea per paragraph.** If you can't name the paragraph's single point, split it.
- **Topic sentence first.** State the point in sentence one; the rest supports it.
- **Given-before-new.** Open each sentence with information the reader already has, then add the new
  element. This is what makes paragraphs flow; reversed order reads as disjointed.
- **Clarity test:** if deleting a paragraph loses nothing, delete it. Invest most in load-bearing
  paragraphs; keep supporting ones short.
- Vary paragraph length deliberately — uniform 150–200-word blocks read as machine-stamped.

### Sentences
- **Parallelism.** Items in a list or series take the same grammatical form ("we measured X, recorded Y,
  and computed Z" — not "computing Z").
- **Signposting.** Use transitions to mark logical moves: contrast (however, in contrast), addition
  (moreover, furthermore), cause (therefore, consequently), sequence (first, subsequently). Don't
  signpost every sentence — only real turns.
- **Vary sentence length.** Short sentences land key findings; longer ones develop reasoning. Five
  consecutive same-length sentences read as monotonous — break the pattern.
- **Consistent terminology, not elegant variation.** One term per concept. Do not cycle
  patients → subjects → participants → cases within a section to avoid repetition; repetition is clarity.

### Active vs passive
- **Methods:** passive is conventional and fine ("samples were analyzed"); it keeps focus on the
  procedure, not the actor.
- **Findings, aim, and contribution:** prefer active and direct ("we found", "this study shows") where
  it improves clarity — but follow the target journal's convention.
- Avoid passive that hides who did or decided something when that matters.

### Tense conventions

| Where | Tense | Example |
|-------|-------|---------|
| Established knowledge / what a theory states | Present | "Hypertension increases stroke risk." |
| Prior studies' specific findings | Past | "Smith et al. reported a 12% reduction." |
| Methods | Past | "Data were collected from …" |
| Results | Past | "Mortality was 12% …" |
| Discussion — interpreting your findings | Present | "These findings suggest …" |
| Conclusion / implications | Present or future | "This supports … / Future work should …" |

---

## 3. Precision & hedging

### Match the claim to the evidence
- Use the **most specific** term available; define technical terms at first use; avoid ambiguous "this"
  / "it" without a clear antecedent.
- Claim strength must match evidence strength. Strong verbs (demonstrates, establishes, confirms)
  require strong evidence; correlational or single-study findings get moderate verbs (suggests,
  indicates, is associated with).
- **Causal language only for designs that support causation.** Observational/associational designs use
  "associated with", not "caused", "led to", "reduced" (as an action). This is a common and serious
  defect.

### Hedge appropriately — neither over- nor under-hedge

| Strength | Devices | Use for |
|----------|---------|---------|
| Tentative | may, might, could, possibly | results needing replication; alternative explanations exist |
| Moderate | suggests, indicates, appears, is consistent with | typical interpretation of a sound finding |
| Strong | demonstrates, establishes, confirms | well-replicated or directly measured facts |

- **Hedge** causal claims from non-experimental data, generalizations from limited/selected samples, and
  interpretations with plausible alternatives.
- **Do NOT hedge** plain data ("the response rate was 78%", not "appeared to be 78%"), your own
  methodology ("we used …", not "we attempted to use …"), or settled facts.
- One hedge per claim is enough. Stacked hedges ("may possibly suggest that it might …") read as evasive.

---

## 4. Reporting & numbers basics

- **Consistency above all.** A number that appears in more than one place (abstract, text, tables,
  figures) must be identical everywhere. Reviewers read numeric drift as carelessness.
- **Effect size + interval, not just P.** Every key comparison reports an effect size (difference, RR,
  OR, HR, d, etc.) with its **95% CI**; the P value supports, it does not replace, the estimate.
- **Report exact statistics.** Give exact P (P = .032), not only "P < .05"; use "P < .001" for very
  small values; never report "P = .000". Report the test statistic with its df where applicable
  (e.g., t(58) = 2.45). State the alpha level and any correction for multiple comparisons.
- **Significant figures / decimals.** Be consistent and don't over-report precision. Two decimals is the
  usual default for estimates; percentages 0–1 decimals. Match precision to the measurement, not to the
  software's output width.
- **Leading zeros.** Quantities that can exceed 1 take a leading zero (M = 0.75); quantities bounded by
  ±1 do not (r = .45, P = .03). Follow the target journal/style (APA shown here) and apply it uniformly.
- **Denominators with rates.** Percentages travel with their raw counts and the n they are out of
  (12%, 24/200) — a percentage alone hides the sample size.
- **Report the non-significant and the missing too.** Don't selectively report only significant results;
  state missing-data amount and how it was handled.
- **Abbreviation discipline.** Define each abbreviation at first use, then use it consistently; don't
  alternate with the spelled-out form, and don't introduce an abbreviation used only once.

---

## 5. Do-not list

A short list of patterns an editor strikes on sight:

- **Vague attributions.** "Many studies show…", "it is well known that…", "some researchers argue…" —
  name them with citations or delete the claim.
- **Editorializing in Results.** Any "surprisingly", "importantly", "strikingly", "as expected", or
  implication/mechanism statement inside Results. Report; interpret later.
- **Hype / novelty inflation.** "groundbreaking", "novel", "cutting-edge", "paradigm-shifting",
  "comprehensive", "robust" used as praise rather than as a precise claim. At most one restrained
  novelty claim per paper, and only if defensible.
- **Throat-clearing openers.** "It is important to note that…", "In the realm of…", "It is worth
  mentioning that…", "In today's rapidly evolving…", "In order to…". Cut to the content.
- **Meta-commentary.** "This section will discuss…", "We now turn to…" — just do it. (Genuine
  Introduction roadmap sentences are fine.)
- **Redundancy.** Saying the same thing twice across sentences/sections; restating numbers in the
  Discussion that the Results already gave.
- **AI-tell vocabulary defaulting.** delve, leverage, foster, underscore, showcase, tapestry, navigate
  (non-literal), multifaceted, nuanced. Not banned, but ask if it's the most precise word — usually it
  isn't.
- **Filler / wordiness.** "due to the fact that" → because; "in order to" → to; "a large number of" →
  many; "has the ability to" → can; "it is important to note that" → (delete).
- **Em-dash and semicolon overuse.** Prefer commas, parentheses, or separate sentences; reserve the
  semicolon for closely parallel clauses.
