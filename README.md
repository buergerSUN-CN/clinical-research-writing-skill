<div align="right"><a href="README.zh.md">中文</a></div>

# Clinical Research Writing

A shared Claude Code and Codex skill for drafting, revising, diagnosing, and auditing clinical
research manuscripts without changing source facts, statistics, methods, or citations.

Version 2 separates a **general clinical-writing core** from an optional **neurovascular/stroke
profile**. The general core controls patient-centered framing, study-design logic, claim strength,
numeric fidelity, IMRaD boundaries, and cross-section consistency. The specialty profile adds
stroke, neuroimaging, and neurointerventional vocabulary plus a measured 32-paper voice fingerprint.

## Capabilities

- Diagnose and rewrite a section with explicit rule-based reasons.
- Draft titles, abstracts, IMRaD sections, limitations, conclusions, tables, and legends.
- Polish a whole manuscript with a mandatory Methods-Results and numeric reconciliation pass.
- Audit STROBE, CONSORT, STARD, or TRIPOD reporting.
- Produce Word tracked changes and a Chinese revision-rationale document.
- Scan a draft for clinical AI tells and, when appropriate, neurovascular corpus drift.

## Runtime design

`SKILL.md` is a lean router. It loads only the relevant layer:

- `core_principles.md`: universal clinical integrity and claim rules.
- `study_families.md`: observational, diagnostic/imaging, procedural, and trial behavior.
- `moves_*.md`: section-specific decisions and failure modes.
- `neurovascular_profile.md`: optional specialty reasoning and vocabulary.
- `voice_fingerprint.md`: numeric distributions used only for that specialty profile.

The previous A/B/C arguments remain compatible, but the public interface now uses readable study
families and makes the specialty boundary explicit.

```bash
python3 scripts/check_draft.py draft.txt \
  --study-family observational --profile general

python3 scripts/check_draft.py stroke_draft.txt \
  --study-family imaging --profile neurovascular
```

## How it was distilled

The private reference build contains 32 complete papers: 13 observational/procedural, 7
diagnostic/imaging, and 12 randomized or trial-secondary papers. The pipeline performs:

1. metadata-first classification;
2. deterministic section-level linguistic measurement;
3. IMRaD section extraction;
4. section-move and clinical-cognition distillation;
5. source-fidelity, template-trap, and contradiction criticism;
6. leave-one-out and old-vs-new blind evaluation;
7. compilation into decision rules and on-demand references.

The public [distillation method](distillation/METHOD.md), JSON schemas, aggregate report, and
de-identified corpus manifest make that method auditable. Source PDFs, extracted full text, long
verbatim exemplars, private paths, and private evaluation artifacts are intentionally excluded.

Method influences: [writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill)
inspired the separation of measurable language, structure, and cognition;
[book-to-skill](https://github.com/virgiliojr94/book-to-skill) inspired compile-time extraction,
decision-ready rules, anti-patterns, and on-demand runtime loading. This repository's clinical
schemas, corpus analysis, rules, scripts, and validation design are original to this project.

## Install

Claude Code:

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.claude/skills/clinical-research-writing
```

Codex:

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.codex/skills/clinical-research-writing
```

The same repository is used by both hosts. `agents/openai.yaml` is Codex UI metadata and is harmless
to Claude Code.

## Validate

```bash
python3 scripts/check_draft.py --help
python3 distillation/pipeline.py --help
python3 -m unittest discover -s tests -v
```

## License and source boundary

Original code and distilled rules are released under the MIT License. Source papers remain under
their respective copyrights and are not included in this repository. The numeric fingerprint is
validated only for the declared neurovascular/stroke corpus; it should not be presented as a
universal distribution for all clinical specialties.
