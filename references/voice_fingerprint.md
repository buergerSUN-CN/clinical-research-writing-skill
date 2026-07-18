# Voice fingerprint — quantitative style targets (median [IQR])

Measured by `scripts/metrics.py` over 32 hand-picked exemplars, split by genre:
**A** = single-centre / observational / prognostic / procedural clinical (Nanjing neurovascular circle + some multicentre-observational), n=13 · **B** = imaging-biomarker / imaging-technique, n=7 · **C** = randomized-trial voice (RCT + post-hoc; NEJM/Lancet/JAMA/Radiology), n=12.

**How to use.** Mount the row for your paper's genre. After drafting a section, run `python3 scripts/check_draft.py <draft.txt> --genre A` (or eyeball against these) and pull any metric outside the genre IQR back toward the median. These are *distributions with tolerances*, not single targets — hitting the median on every sentence is itself an AI tell (see `#burstiness`). The section-bound rules (`#hedging`, `#passive`) are load-bearing and appear again in `clinical_ai_tells.md`.

## Sentence rhythm & burstiness {#burstiness}
| metric | A | B | C |
|---|---|---|---|
| mean sentence length (words) | 31 [27–37] | 30 [28–33] | 35 [31–37] |
| SD of sentence length | 43 [38–63] | 38 [32–42] | 52 [44–60] |
| burstiness (mean abs successive diff) | 24 [19–37] | 21 [21–26] | 31 [28–33] |
| % short ≤15 words | 25 [20–31] | 26 [23–29] | 30 [23–34] |
| % long ≥40 words | 13 [9–16] | 13 [12–16] | 20 [16–23] |

**Law — vary the rhythm.** Real prose alternates long explanatory sentences with short declarative ones (SD runs **~1.3–1.5× the mean** — A ~1.4, B ~1.3, C ~1.5; short sentences ≤15 words are ~25% in A/B, ~30% in C). Never write 3 consecutive sentences of similar length. C (top-journal RCTs) runs longer and denser (35 words, 20% long) than A/B (~30 words).
- **Correct (paper02, rhythm):** "…the benefit of thrombectomy. Early risk stratification is therefore essential." (long clause → 6-word punch)
- **Incorrect (AI, uniform):** every sentence 20–24 words, evenly hedged, no short beats — flat cadence a reader clocks as machine-written.
- **Caveat (do NOT overcorrect):** a short sentence is a substantive declarative, **not** an aphoristic one-liner ("The reading is speculative.", "The novelty is elsewhere."). Clipped essayistic beats are themselves an LLM tell — see `clinical_ai_tells.md #llm-signatures`.

## Hedging — non-uniform, section-bound {#hedging}
| hedge words /1000 | A | B | C |
|---|---|---|---|
| Results | 0.7 [0–1.6] | 1.4 [0–2.3] | 0.7 [0–0.9] |
| Discussion | 11 [8–12] | 11 [9–14] | 8 [6–11] |

**Law — hedge in the Discussion, not the Results.** Hedging jumps ~10× from Results (~0–1) to Discussion (~8–11). Report findings as facts in Results (no "may/appears/likely"); reserve hedging for interpretation. **Uniform hedging across the whole paper is the single strongest AI tell.**
- **Correct — Results (paper02):** "sICH occurred in 48 of 395 patients (12.2%)." · **Discussion (paper02):** "Elevated D-dimer *may* reflect a prothrombotic state that *could* predispose to…"
- **Incorrect (AI):** "sICH *may have* occurred in approximately 12% of patients, which *could suggest* a *potential* association." (hedged fact in Results)

## Passive voice by section {#passive}
| passive-sentence ratio | A | B | C |
|---|---|---|---|
| Methods | 0.56 [0.46–0.67] | **0.72 [0.50–0.78]** | 0.55 [0.43–0.59] |
| Results | 0.26 | 0.41 | 0.28 |
| Discussion | ~0.3 | ~0.4 | ~0.3 |

**Law — Methods is passive on purpose; do NOT de-passivize it.** Methods runs ~55–72% passive ("patients were enrolled", "sICH was adjudicated") — this is correct scientific register, highest in imaging (B). A generic "prefer active voice" polish that rewrites Methods to active is WRONG here (see `clinical_ai_tells.md` humanizer-exemption table). Results/Discussion sit lower (~0.3).

## Numbers: absolute-rate-first & statistic density {#numbers}
| metric | A | B | C |
|---|---|---|---|
| stat tokens /100 words (Results) | 3.1 [2.5–4.7] | 2.6 [2.2–3.3] | 1.9 [1.0–3.3] |

**Law — lead Results with an absolute rate + denominator, then the inferential stat.** The rate rarely opens the *sentence* (it usually follows the subject), but every key Results clause carries `n of N (x%)` and every association carries `effect + 95% CI + exact P`. A/B pack more stats per word (denser numeric Results) than C.
- **Correct (paper02):** "sICH occurred in 48 of 395 patients (12.2%); on multivariable analysis D-dimer was associated with sICH (adjusted OR 2.45, 95% CI 1.75–3.43, P<0.001)."
- **Incorrect (AI):** "Nearly one in five patients experienced bleeding, a notably high rate." (no denominator, no CI, soft-news framing — see `voice_principles.md #results-abs-rate`)

## Punctuation {#punct}
| /1000 words | A | B | C |
|---|---|---|---|
| **em-dash (—)** | **0 [0–0]** | **0 [0–0.5]** | 0.2 [0–0.7] |
| parentheses | 56 [47–68] | 49 [37–52] | 43 [41–50] |
| semicolons | 9 [5–11] | **13 [9–16]** | 8 [7–13] |

**Law — em-dash ≈ 0 for A/B.** The Nanjing group essentially never uses the em-dash "—"; a draft sprinkled with em-dashes reads off-voice (and AI-ish). (En-dash in numeric ranges like `1.75–3.43` is fine and separate.) Parenthetical asides are frequent (esp. A). Imaging (B) leans on semicolons to chain parallel measurements.

## Connective spectrum {#connectives}
Per-1000-word medians. **Rare-to-zero and, as a *sentence-initial capitalized* connective, an AI tell:** `Moreover` (~0), `Notably` (0), `Importantly` (0), `Consequently` (0), `Hence` (0), `Nevertheless` (0), `By contrast` (0); `Additionally` (~0.2) and `Furthermore` (~0.2 in A/B, ~0.15 in C) do occur mid-sentence but the group almost never opens a sentence/paragraph with them.
- The group's actual connectives: **however** (A 0.5 / **B 1.5** / C 0.4), **although** (~0.3), **therefore** (~0.3), **in addition** (A 0.4). B (imaging) uses "however" ~3× more than A/C. Note: by raw frequency A's *furthermore* (0.24) ≈ *therefore* (0.26) — the ban is on **register** (paragraph-head "Moreover,/Furthermore,/Notably,") not on the word existing mid-clause.
- **Law:** if a draft is peppered with paragraph-head *Moreover / Additionally / Notably / Furthermore / Importantly*, it is off-voice. Prefer *however / although / therefore*, used sparingly.

## Aim/opener phrasing {#openers}
- **Openers** cluster on **disease-burden** and **standard-of-care-limitation** across all genres (the clinical opener; never a molecular/mechanistic gap). B occasionally opens on an **imaging-limitation**.
- **Objective form** does NOT split cleanly by genre (bare-infinitive "To investigate…", "The purpose of our study was to…", and "The aim was to…" all appear in each) — treat as a per-paper VARIANT, not a genre rule. Detail in `voice_principles.md #introduction`.

## Genre contrast at a glance {#genre-contrast}
- **A (clinical observational):** medium sentences, dense stats, most parentheses, em-dash 0, hypothesis-generating claims.
- **B (imaging):** most passive Methods, most "however", most semicolons, em-dash 0.
- **C (RCT voice):** longest/densest/burstiest sentences, most long sentences, low Results hedging (~0.7, comparable to A — A is marginally lowest), practice-changing claims — use ONLY when writing/modelling a randomized trial, not a single-centre cohort.

## Quick Search Targets {#grep}
```
rg -n -A6 "#burstiness"     references/voice_fingerprint.md    # sentence rhythm law
rg -n -A5 "#hedging"        references/voice_fingerprint.md    # non-uniform hedging (Results vs Discussion)
rg -n -A5 "#passive"        references/voice_fingerprint.md    # Methods-passive exemption
rg -n -A4 "#numbers"        references/voice_fingerprint.md    # absolute-rate-first + CI
rg -n -A6 "#connectives"    references/voice_fingerprint.md    # banned AI connectives + real ones
rg -n -A6 "#punct"          references/voice_fingerprint.md    # em-dash ≈ 0
rg -n -A5 "#genre-contrast" references/voice_fingerprint.md    # A vs B vs C
```
Rebuild the fingerprint from an exemplar workspace with `python3 scripts/metrics.py <workspace>`. Check a draft with `python3 scripts/check_draft.py <draft.txt> --genre A`.
