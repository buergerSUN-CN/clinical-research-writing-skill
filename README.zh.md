<div align="right"><a href="README.md">English</a></div>

# 临床科研写作

一个同时适配 Claude Code 和 Codex 的 skill，做一件事：**让临床科研论文读起来像是课题组自己写的，不是基础科学腔，也不是 AI 腔。**

从 32 篇手选范文里蒸馏出来的——包括神经血管/卒中方向的单中心观察性研究、影像标志物研究,以及 NEJM / Lancet / JAMA 上的顶刊多中心 RCT。蒸馏不是"读一读然后写几条规则":先跑脚本算量化指标(句长节奏、分节 hedging、连接词频谱、被动分布……),再逐节深读抽模式,最后用对抗批评和留一盲判兜底。

## 四种用法

| 模式 | 做什么 | 什么时候用 |
|---|---|---|
| **A — 诊断 & 改写** | 指出哪句读起来不对——是基础科学腔、模板腔、还是 AI 腔,给一句临床化的改写。对照量化指纹自查,不是瞎改。 | 最常用。改一段或一节稿子。 |
| **B — 从零起草** | 给定论文类型和研究设计,直接按对应体裁的腔调写出某一节。 | 这一节还没写。 |
| **C — 整篇打磨** | 确定研究类型和体裁 → 按 IMRaD 拆单元 → 逐单元改 → 强制跨节金线校验 → 三种交付物。 | 全稿精修,投稿前。 |
| **D — 清单审计** | 根据研究类型挂载对应的报告规范(STROBE / CONSORT / STARD / TRIPOD),逐条审计——✅ 已报 / ⚠️ 部分缺失 / ❌ 缺了 / N/A,缺的标严重度,给一句话补写建议。 | 投稿前检查,把审稿人最可能抓的清单条目提前填上。 |

### Mode C 出三种东西

1. **Markdown 修改报告**——哪段、什么问题、多严重、建议怎么改
2. **带 Word 修订追踪的 `.docx`**——拒绝全部修订就能精确还原原稿
3. **纯中文《修改理由》`.docx`**——每条两行中文:改了什么、为什么(给导师看,给审稿人回)

## 跟泛泛的"临床写作技巧"不一样在哪

**有量化的声音指纹,不是凭感觉。** 范文算成了可查的指标,按体裁分三档(A 临床观察 / B 影像标志物 / C 随机对照)。比如句长节奏——真实论文的句子长短落差很大(SD 约是均值的 1.3–1.5 倍),AI 写的句子均匀到头;hedging 密度——Results 几乎不 hedge(≈0),Discussion 才密集(8–11 / 千词),差了一个数量级,全篇均匀 hedge 就是最硬的 AI 信号;Methods 被动占比 55–72% 是**对的**,别拿"多用主动"去改它;破折号在这组几乎不用(≈0),一多就假。`scripts/metrics.py` 算指标,`scripts/check_draft.py` 一行查草稿。

**教的是原理,不是模板。** 旧版 phrasebank 把范文拆成填空框让人往里填——结果就是 "Nearly one in five patients experienced X" 这种复读机。新版彻底推翻了:39 条招式(Title 到 Conclusion),每条给的是**原理 + 经来源核验的范文原句 + AI 腔反例 + 防重复提示**,不留任何可粘贴的空格句。

**降 AI 感是语料反推的,不是拍脑袋的。** 硬信号是范文本身告诉你的——uniform hedging、AI 高频连接词(Moreover / Additionally / Notably…,范文里几乎为零)、"有重要临床意义"这种空洞收尾、假分数修辞。更隐蔽的 LLM 签名信号是跑留一盲判时发现的——警句式段落收束("The novelty is elsewhere.")、人为制造的对称对偶、太整齐的 First…Second…Third 限制段、数字被削薄成概述、过度润色把 ESL 论文该有的粗粝质感磨掉了。这些全收在 `clinical_ai_tells.md` 里,写完自己查一遍。

**该引用别人的不自己写。** 通用 IMRaD 结构、hedging 体系、时态和报告规范交给宿主环境的通用科研写作 skill。词法层去 AI 在 Codex 使用 `humanizer-academic`，在 Claude Code 使用 `humanizer_academic`，同时保留临床豁免：Methods 被动不动、破折号按阈值而非零容忍、hedging 绑定 section。本 skill 只做别处没有的：**这个课题组到底怎么写。**

## 目录

```
SKILL.md                          # 路由、体裁分类、四种 Mode、grep 循环、降 AI 顺序
agents/openai.yaml                # Codex 界面元数据（Claude Code 会忽略）
references/
  voice_fingerprint.md            # A/B/C 量化指标 + 反 AI 硬规则
  voice_principles.md             # 39 条反模板招式,逐条标范文出处 + AI 反例
  structure_contract.md           # 体裁骨架 + claim 强度梯级 + 强制跨节一致性
  clinical_ai_tells.md            # 语料反推 AI 信号清单 + humanizer 临床豁免
  reporting_checklists.md         # STROBE / CONSORT / STARD / TRIPOD,逐条可 grep
  domain_notes.md                 # mRS / ASPECTS / TICI / κ… 领域词表
  display_items.md                # 图注 / 表注 / 表格脚注——让读者不翻正文也看懂
scripts/
  apply_tracked_changes.py        # edits.json → Word 修订追踪
  build_rationale_docx.py         # 《修改理由》Markdown → Word
  metrics.py                      # 算量化指纹
  check_draft.py                  # 一行查稿,对标体裁靶值
```

## 安装

Claude Code：

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.claude/skills/clinical-research-writing
```

Codex：

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.codex/skills/clinical-research-writing
```

## 快速上手

**改一段 Results(体裁 A):**

```
rg -n -A6  "#results"          references/voice_principles.md
rg -n -A5  "#hedging"          references/voice_fingerprint.md
rg -n -A4  "#numbers"          references/voice_fingerprint.md
rg -n -A15 "#tells"            references/clinical_ai_tells.md
```

**查草稿:** `python3 scripts/check_draft.py draft.txt --genre A`

**投稿前跑清单审计:**
```
rg -n -A10 "#mapping"   references/reporting_checklists.md   # 找到对应清单
rg -n -A30 "#strobe"    references/reporting_checklists.md   # 或 #consort / #stard / #tripod
```

**把修改应用到 Word:**
```bash
python3 <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/ --merge-runs false
python3 scripts/apply_tracked_changes.py unpacked/ edits.json --author "Codex"  # Claude Code 下改为 Claude
python3 <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx
```
