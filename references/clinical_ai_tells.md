# Clinical AI-tells — make it read human, not machine

Reverse-inferred from the 32-exemplar corpus: **what real papers in this voice do that an AI writer flattens**, plus a banned-pattern checklist, plus how to run `humanizer_academic` without breaking clinical convention. Run this as a **post-draft pass** (see order at bottom). Numeric targets live in `voice_fingerprint.md`; phrasing principles in `voice_principles.md`.

## (A) Positive signals real papers have and AI drops {#positive}
- **Burstiness.** Sentence length varies hard (SD ≈ **1.3–1.5× the mean**; short ≤15 words ~25% in A/B, ~30% in C). AI writes uniform 20–24-word sentences. → after a long explanatory sentence, land a short *substantive* declarative — NOT an aphorism (see `#llm-signatures`). (`voice_fingerprint.md #burstiness`)
- **Non-uniform, section-bound hedging.** Results states facts (hedge ≈0); Discussion interprets (hedge 8–11/1000). AI hedges everywhere. Never write "sICH *may have* occurred in ~12%". (`#hedging`)
- **Methods is passive on purpose** (~55–72%). Do NOT de-passivize it. (`#passive`)
- **Absolute rate + denominator + CI**, not a rhetorical fraction. "48 of 395 (12.2%)… adjusted OR 2.45, 95% CI 1.75–3.43, P<0.001". (`voice_principles.md #results-abs-rate` / `#numbers`)
- **Named, specific prior-work gaps.** "Piero et al. showed X *but did not analyze* Y" — a named author + what they showed + the one thing they didn't. Not "several studies have shown…".
- **One number, stated once.** An OR appears inline once; it is NOT re-skinned in words ("a 13% reduction", "nearly one-seventh lower", "a protective effect").
- **A concrete management directive**, keyed to a stratum ("ultrasound every 3 months in the first 15 months for high-risk"), not "these findings have important clinical implications".
- **em-dash ≈ 0** in this group (A/B). En-dash in numeric ranges (`1.75–3.43`) is fine.

## (B) The banned-pattern checklist — AI tells to delete {#tells}
Scan every draft for these; each is a rewrite:
- **Fake-fraction flourish** — "Nearly one in five patients experienced X", "roughly one third of…" as decoration. → `n of N (x%)`; a fraction is allowed ONLY as an NNT or benchmarked absolute difference (genre C). *(flagged independently by A, B, and C.)*
- **Adjective pile** — "simple, accessible, reproducible, cost-effective, widely available". → ONE concrete operational virtue ("reported within half an hour", "no post-processing", "available at primary stroke centres"). *(the "simple/accessible/reproducible" triad is a real group phrase but a phrasebank trap — vary it.)*
- **Content-free implications** — "has important/significant clinical implications", "may inform future treatment decisions", "warrants further investigation". → the actual instruction or the specific named gap.
- **Vague attribution** — "Several studies have shown / It is well known that". → named author + specific finding + specific deficiency.
- **AI connective scaffolding** — paragraph-head *Moreover / Furthermore / Additionally / Notably / Importantly / Consequently*. Near-zero in the whole corpus. → *however / although / therefore*, sparingly. (`#connectives`)
- **Uniform / misplaced hedging** — any "may/could/appears/likely" on a Results fact; hedge-stacking ("may have the potential to possibly…"). → fact in Results; ≤1 hedge per Discussion claim.
- **Hype register** — "novel, paradigm shift, revolutionize, pivotal role, crucial, sheds light, underscores". This group is measured. At most one restrained "to our knowledge, the first…".
- **Causal verbs on associational data** — "dehydration *protects* / *reduces* mortality" from an OR. → "was *associated with* lower risk (adjusted OR 0.87…)", and name the model that adjusted.
- **(C only) limp null** — "the primary endpoint was not met but our findings provide valuable insights". → reframe to a decision/guideline message ("thrombolysis should not delay endovascular treatment; current guidelines should remain in place") or a design lesson.
- **(C only) standalone mechanism paragraph** — pathway prose (oxidative stress, apoptosis, BBB) that never returns to who gets treated. → every mechanistic clause ends in a treatment/timing/feasibility consequence.
- **Spelling drift** — mixing British/American. → match the target journal (Lancet: ischaemic/randomised; NEJM/JAMA: ischemic/randomized).

## (B2) LLM-signature tells — the "too-good" failure mode {#llm-signatures}
These survived a first-pass contract-guided rewrite and were caught by a blind judge holding the real paper — the rewrite read *too* polished. Scan for them; they are the difference between "genre-competent" and "reads human":
- **Aphoristic / essayistic closers.** Clipped one-liners used as rhetorical beats — "The novelty is elsewhere.", "The reading is speculative.", "Nothing here supports that.", "Safety moved in the opposite direction." Real Discussions don't land every paragraph on an epigram. → cut the aphorism; end on the specific finding or directive.
- **Manufactured symmetry / antithesis.** Every paragraph opening on a tidy thesis and closing on a balanced take; see-sawing "on one hand… the trade-off is modest on both sides". Real prose is lumpier and digresses. → let paragraphs be uneven; allow a genuine tangent.
- **Too-perfect enumerated limitations.** A clean "First… Second… Third… Finally…" covering exactly the four canonical limitation types, each an evenly-weighted clause. Real limitations are lumpier, more numerous, unevenly weighted, and often paired with a concrete defense. → make them specific and uneven; add a strengths note where the corpus does.
- **Thinned quantitative specificity.** Rewrites keep the top-line effect and drop the granular checkable numbers (arm counts, per-hour deltas, NNT vs comparator, exact windows). Real papers in this voice are number-dense. → keep the specific paired numbers; don't smooth them into prose.
- **Stripped or vague citations.** Replacing named attributions with "have been reported", "prior series", or plausible-but-wrong gestures ("HERMES-style syntheses"). → keep the author's real citations and specific named trials; never invent a synthesis or a "first to show".
- **Native-fluent over-smoothing.** Erasing every seam into uniform polish. The exemplars have honest roughness and terse domain phrasing. → don't sand the draft into frictionless prose; preserve the author's specific, slightly-uneven constructions.
- **Numbers placed where the source didn't have them.** Do not move summary statistics (AUC, NPV, specificity) into a section the source didn't, or invent an editorial angle (an "NPV story") the data don't foreground. Report what the manuscript reports, where it reports it.

## (C) Running humanizer_academic without breaking clinical convention {#humanizer}
`humanizer_academic` (`~/.claude/skills/humanizer_academic/`) owns the word-level AI-tell cleanup (26 patterns). Reuse it as a pass, but **override these where it conflicts with clinical register**:

| humanizer rule | conflict | clinical override |
|---|---|---|
| **#13 em-dash zero-tolerance** | dogmatic | **threshold, not zero**: match `voice_fingerprint.md #punct` (A/B ≈0 anyway; C tolerates ~0.2/1000). En-dash numeric ranges are exempt. |
| **passive → active** | Methods SHOULD be passive | **exempt Methods** (`#passive`); apply only in Intro/Discussion. |
| **#17 simplify hedging** | must stay section-bound | apply, but keep hedging in Discussion (≤1/claim) and drive Results to ≈0 — do not flatten to uniform. |
| **AI-vocabulary banlist / classical-term restoration** | some terms are clinical standard | apply, but **whitelist**: "associated with", "independent predictor", "functional independence", scale names, "reperfusion". |

**Order of passes (put in SKILL.md workflow):**
1. Clinical reframing + genre voice (this skill: `voice_principles` + `structure_contract`).
2. **This file's self-check** (A/B) + fingerprint compare (`python scripts/metrics.py` on the draft).
3. `humanizer_academic` (word-level), with the overrides above.
4. Language/journal polish (e.g. a `nature-polishing`-type pass) — last.

**Chinese output** (中文摘要 or 《修改理由》): route Chinese-language AI-smoothing to `humanizer-zh-academic`; this file is English-tuned.

## Quick Grep Targets {#grep}
```
grep -A10 "#positive"       references/clinical_ai_tells.md   # what to preserve
grep -A15 "#tells"          references/clinical_ai_tells.md   # banned patterns
grep -A10 "#llm-signatures" references/clinical_ai_tells.md   # the "too-polished" tells
grep -A8  "#humanizer"      references/clinical_ai_tells.md   # humanizer exemptions + pass order
```
