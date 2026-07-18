# Distillation method

This build treats the source papers as private evidence and the public skill as a compact decision
system. It borrows two useful ideas from prior skill builders: separate measurable surface style from
structure and cognition, and compile dense decision rules for on-demand runtime use rather than
shipping raw source text.

The methodological inspirations are `larashero3-dotcom/writing-dna-skill` for layered language,
structure, and cognition analysis, and `virgiliojr94/book-to-skill` for compile-time synthesis,
decision rules, anti-patterns, and progressive disclosure. The clinical schemas, corpus design,
measurement code, rules, and validation gates here are project-specific.

## Inputs and boundary

- Use at least 20 complete papers; the reference build uses 32.
- Cover the study families and journals the profile claims to support.
- Keep PDFs and extracted text in the private workspace only.
- Record corpus inclusion rationale before measuring style.
- Do not claim general validation from a specialty-specific corpus.

## Phase 1: metadata first

Create `_meta/paperNN.json` using `schemas/metadata.schema.json`. Annotate study family, specialty,
design, center structure, primary endpoint, claim gradient, journal, and year. Do not infer style
groups from prose metrics alone.

Gate: every corpus file has valid metadata and the family distribution matches the intended profile.

## Phase 2: deterministic fingerprint

Run:

```bash
python3 distillation/pipeline.py metrics --workspace <private-workspace>
python3 distillation/pipeline.py export-sections --workspace <private-workspace>
```

Measure sentence rhythm, section-bound hedging, passive voice, statistic density, connective use, and
punctuation. Inspect section-detection failures before accepting aggregate values.

Gate: per-paper metrics exist for every paper; distributions are reported as median and IQR, not a
single ideal value.

## Phase 3: section moves and cognition

For each of title/abstract, Introduction, Methods, Results, and Discussion:

1. Read all extracted section files or a declared stratified sample.
2. Extract decisions, not sentence templates.
3. For each move record applicability, evidence paper IDs, counterexamples, failure mode, and a
   manuscript check using `schemas/patterns.schema.json`.
4. Separately extract recurring clinical propositions, claim habits, signature reasoning moves, and
   avoided behaviors using `schemas/cognition.schema.json`.

Gate: each public rule has traceable private evidence and distinguishes invariant from family/profile
specific behavior.

## Phase 4: adversarial critic

Run three independent checks:

- Source fidelity: every evidence ID supports the attributed move.
- Template trap: reject rules that can be copied as a fixed sentence frame.
- Contradiction and scope: compare qualitative rules with measured distributions and declared corpus
  limits.

Keep exact quotations only in private audit artifacts. Compile public rules as paraphrased decisions.

## Phase 5: leave-one-out and before/after

Hold out at least one paper per supported family. Give the writer only title/abstract facts and the
candidate skill; do not expose the real Introduction or Discussion. Blind a judge to real vs generated
and old vs new outputs. Record factual invention, genre/profile fit, template recurrence, numeric
retention, and clinical decision focus with `schemas/evaluation.schema.json`.

Gate: no invented facts; no factual-integrity regression; the candidate improves clinical authenticity
or anti-template behavior in most tested families.

## Phase 6: compile and release

- Keep `SKILL.md` as a lean router.
- Split section, study-family, and specialty-profile references one level below it.
- Exclude raw text, PDFs, local paths, and long verbatim overlaps.
- Run workspace validation, public-tree scanning, runtime tests, and host-specific smoke tests.
- Publish aggregate counts and limitations, not source prose.

Useful commands:

```bash
python3 distillation/pipeline.py validate --workspace <private-workspace>
python3 distillation/pipeline.py scan-public --root <skill-root> --corpus <private-workspace>/_corpus
python3 distillation/pipeline.py report --workspace <private-workspace> --out report.json
```
