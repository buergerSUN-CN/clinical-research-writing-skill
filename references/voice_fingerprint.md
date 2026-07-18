# Neurovascular voice fingerprint

These are medians [IQR] from 32 stroke/neurovascular exemplars: A=13 observational/procedural,
B=7 imaging, C=12 randomized or trial-secondary papers. Use only with the neurovascular profile.
They are diagnostic distributions, not universal targets.

## Sentence rhythm {#rhythm}

| Metric | A | B | C |
|---|---:|---:|---:|
| Mean words/sentence | 31 [27–37] | 30 [28–33] | 35 [31–37] |
| SD of sentence length | 43 [38–63] | 38 [32–42] | 52 [44–60] |
| Mean successive difference | 24 [19–37] | 21 [21–26] | 31 [28–33] |
| Short sentences ≤15 words | 25% [20–31] | 26% [23–29] | 30% [23–34] |
| Long sentences ≥40 words | 13% [9–16] | 13% [12–16] | 20% [16–23] |

Interpretation: real papers alternate dense explanatory sentences with short substantive statements.
Do not manufacture clipped aphorisms or optimize every paragraph toward the median.

## Section-bound hedging {#hedging}

| Hedge terms/1000 words | A | B | C |
|---|---:|---:|---:|
| Results | 0.7 [0–1.6] | 1.4 [0–2.3] | 0.7 [0–0.9] |
| Discussion | 11 [8–12] | 11 [9–14] | 8 [6–11] |

Report findings as findings in Results. Reserve uncertainty and mechanistic qualification for
interpretation. Uniform hedging across sections is off-profile.

## Methods passive voice {#passive}

| Passive-sentence ratio | A | B | C |
|---|---:|---:|---:|
| Methods | 0.56 [0.46–0.67] | 0.72 [0.50–0.78] | 0.55 [0.43–0.59] |

Do not automatically convert Methods to active voice. Imaging acquisition and adjudication often
require intentional passive constructions.

## Numbers and punctuation {#numbers}

- Results statistic tokens per 100 words: A 3.1 [2.5–4.7], B 2.6 [2.2–3.3], C 1.9 [1.0–3.3].
- Em dashes per 1000 words: A 0 [0–0], B 0 [0–0.5], C 0.2 [0–0.7].
- Parenthetical units are common; semicolons are most frequent in imaging Methods/Results.
- Sentence-initial `Moreover`, `Notably`, `Importantly`, and similar editorial connectives are rare.

Run:

```bash
python3 scripts/check_draft.py draft.txt --study-family observational --profile neurovascular
```

Rebuild private corpus metrics with `python3 scripts/metrics.py <workspace>`.
