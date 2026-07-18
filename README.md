<details open>
<summary><b>English</b></summary>

# clinical-research-writing

A Claude Code skill that makes clinical research manuscripts read as **genuine clinical research** written in a real group's voice — not basic science, and not AI.

Distilled per-genre from **32 hand-picked exemplars** (neurovascular/stroke + neuroimaging, NEJM/Lancet/JAMA RCTs), using a hybrid pipeline: quantitative linguistic fingerprinting (sentence burstiness, section-bound hedging, connective spectrum) + per-section deep-read pattern extraction with adversarial validation and leave-one-out blind judging.

## What it does

- **Mode A** — diagnose & rewrite a section. Identifies specific sentences that read basic-science/templated/AI; quotes the offender; shows a clinical rewrite. Checks against a measured genre fingerprint.
- **Mode B** — draft a section from scratch in the target genre's voice.
- **Mode C** — polish a whole manuscript. Classify → split into sections → triage → per-section rewrite (parallelizable) → mandatory cross-section "golden-thread" consistency pass → deliverables:
  - **Output 1** — Markdown revision report (findings table, severity, suggested rewrites)
  - **Output 2** — Tracked-changes revised `.docx` (edits applied; rejecting all changes restores the original exactly)
  - **Output 3** — Chinese 《修改理由》 `.docx` (pure Chinese, two-line-per-edit explanation for supervisors/reviewers)

## How it's different from generic clinical-writing advice

1. **Quantitative voice fingerprint** — measured targets per genre (A observational · B imaging · C RCT): sentence burstiness (SD ≈ 1.3–1.5× mean), section-bound hedging (Results ≈ 0, Discussion ≈ 8–11 /1000), Methods-passive exemption (55–72%), em-dash ≈ 0, banned connectives. `scripts/metrics.py` computes these; `scripts/check_draft.py` checks a draft against them.

2. **Anti-template principles, not phrase banks** — 39 sourced moves (Title → Conclusion). Every move is a *principle + verbatim Correct exemplar (paperNN-verified) + AI Incorrect counter-example + anti-repetition note*. No fill-in-the-blank frames — the old skill's phrase-bank taught templating ("Nearly one in five patients experienced X"); the new skill kills it.

3. **Corpus-derived AI-tell layer** — hard anti-AI signals reverse-inferred from the exemplars (uniform hedging, AI connectives, "significant clinical implications" filler, fake-fraction flourish) plus LLM-signature tells caught by leave-one-out blind judging (aphoristic closers, manufactured symmetry, too-perfect limitations, thinned specificity).

4. **Deferral, not duplication** — general IMRaD structure / hedging taxonomy / reporting standards (CONSORT, STROBE, TRIPOD) are delegated to the `academic-research-skills` plugin and `scientific-writing` skill. Word-level de-AI delegates to `humanizer_academic` (with clinical exemptions for Methods-passive, em-dash thresholds, section-bound hedging). This skill adds only the clinical + genre-voice + anti-AI delta.

## Layout

```
SKILL.md                      # router, genre classify, Modes A/B/C, grep loop, anti-AI order, defer map
references/
  voice_fingerprint.md        # A/B/C numeric targets + anti-AI laws (grep-indexed)
  voice_principles.md         # 39 anti-template section moves, sourced, Correct/Incorrect
  structure_contract.md       # genre skeleton, claim-gradient, mandatory cross-section pass
  clinical_ai_tells.md        # corpus-derived AI-tell checklist + humanizer exemptions
  domain_notes.md             # mRS/ASPECTS/TICI/κ… field vocabulary (slim, only what's used)
  display_items.md            # self-contained figure legends / table footnotes
scripts/
  apply_tracked_changes.py    # ← preserved from v1
  build_rationale_docx.py     # ← preserved from v1
  metrics.py                  # compute the quantitative fingerprint
  check_draft.py              # one-line draft check: python scripts/check_draft.py draft.txt --genre A
```

## Install

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.claude/skills/clinical-research-writing
```

## Tracked-changes pipeline (Mode C, Output 2)

Requires the bundled `docx` skill's `unpack.py` / `pack.py`:

```bash
python <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/ --merge-runs false
python scripts/apply_tracked_changes.py unpacked/ edits.json --author "Claude"
python <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx
```

## Writing loop (example: Results, genre A)

```
grep -A6  "#results"          references/voice_principles.md
grep -A5  "#hedging"          references/voice_fingerprint.md   # Results ≈ 0
grep -A4  "#numbers"          references/voice_fingerprint.md   # n/N (%) + CI
grep -A15 "#tells"            references/clinical_ai_tells.md
```

Then: `python scripts/check_draft.py draft.txt --genre A`

</details>

<details>
<summary><b>中文</b></summary>

# 临床科研写作

一个 Claude Code skill,让临床科研论文读起来像**真实课题组写的临床研究**——而非基础科学腔,也非 AI 腔。

从 **32 篇手选范文** 按体裁分别蒸馏(神经血管/卒中 + 神经影像 + NEJM/Lancet/JAMA 顶刊 RCT),混合流水线:量化语言学指纹(句长节奏、分节 hedging、连接词频谱) + 逐节深读抽取 + 对抗补验 + 盲判留一验证。

## 能做什么

- **Mode A** — 诊断 & 改写某一节。指出具体哪句读起来像基础科学/模板/AI,给出临床化改写,对照量化指纹自查。
- **Mode B** — 从零起草某一节的体裁腔调。
- **Mode C** — 整篇打磨。分类研究类型 → 拆节 → 分诊 → 逐节改写(可并行)→ 强制跨节金线一致性校验 → 三种交付物:
  - **Output 1** — Markdown 修改报告(问题表格 + 严重度 + 建议改写)
  - **Output 2** — 带 Word 修订追踪的 `.docx`(拒绝全部修订即可精确还原原稿)
  - **Output 3** — 纯中文《修改理由》`.docx`(每条两行中文:改动 → 理由。导师/审稿人向)

## 和通用"临床写作建议"的区别

1. **量化声音指纹** — 按体裁(A 临床观察 · B 影像 · C RCT)给出可测量的指标:句长节奏(SD ≈ 均值的 1.3–1.5 倍)、分节 hedging(Results ≈ 0, Discussion ≈ 8–11/千词)、Methods 被动语态豁免(55–72%)、破折号 ≈ 0、禁用连接词。`scripts/metrics.py` 算指标,`scripts/check_draft.py` 一行查草稿。

2. **反模板原则,不是短语库** — 39 条招式(Title → Conclusion)。每条是**原理 + 范文原文(已逐条 grep 核实) + AI 腔反例 + 防重复提示**。不留"填空框"——旧版 phrasebank 教模板("Nearly one in five patients experienced X"),新版把模板杀掉了。

3. **语料推演 AI 信号层** — 从范文反推的硬 AI 特征(uniform hedging、AI 连接词、"有重要临床意义"空话、假分数修辞),加上留一盲判捕获的 LLM 签名信号(警句式收束、制造对称、整齐过头的 limitations、削薄数字密度)。

4. **下沉引用,不重复造轮子** — 通用 IMRaD 结构/hedging 体系/报告规范(CONSORT/STROBE/TRIPOD)下沉给 `academic-research-skills` 插件和 `scientific-writing` skill。词法层去 AI 下沉给 `humanizer_academic`(带临床豁免:Methods 被动不动、破折号按阈值不按零容忍、hedging 绑 section)。本 skill 只加临床增量 + 体裁腔 + 降 AI 增量。

## 目录结构

```
SKILL.md                      # 路由、体裁分类、三种Mode、grep循环、降AI顺序、defer表
references/
  voice_fingerprint.md        # A/B/C 数值靶 + 反AI铁律(grep索引)
  voice_principles.md         # 39条反模板招式,逐条带范文来源+反例
  structure_contract.md       # 体裁骨架 + claim强度梯级 + 强制跨节一致性
  clinical_ai_tells.md        # 语料反推AI-tell清单 + humanizer临床豁免
  domain_notes.md             # mRS/ASPECTS/TICI/κ 领域词表(瘦身,只留真用的)
  display_items.md            # 自足式图注/表注规则
scripts/
  apply_tracked_changes.py    # ← v1保留
  build_rationale_docx.py     # ← v1保留
  metrics.py                  # 算量化指纹
  check_draft.py              # 一行查稿:python scripts/check_draft.py draft.txt --genre A
```

## 安装

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.claude/skills/clinical-research-writing
```

## Mode C 修订追踪流水线

需要 `docx` skill 自带的 `unpack.py` / `pack.py`:

```bash
python <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/ --merge-runs false
python scripts/apply_tracked_changes.py unpacked/ edits.json --author "Claude"
python <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx
```

## 写作循环(示例:Results, genre A)

```
grep -A6  "#results"          references/voice_principles.md
grep -A5  "#hedging"          references/voice_fingerprint.md   # Results ≈ 0
grep -A4  "#numbers"          references/voice_fingerprint.md   # n/N (%) + CI
grep -A15 "#tells"            references/clinical_ai_tells.md
```

然后:`python scripts/check_draft.py draft.txt --genre A`

</details>
