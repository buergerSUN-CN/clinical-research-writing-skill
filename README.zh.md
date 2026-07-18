<div align="right"><a href="README.md">English</a></div>

# 临床科研写作

一个 Claude Code skill,解决一个问题:**把临床科研论文从「像基础科学写的」改成「像临床课题组写的」,同时把 AI 味压下去。**

从课题组自己的 32 篇范文里提炼出来的——包括神经血管/卒中方向的单中心观察性研究、影像标志物研究,以及 NEJM / Lancet / JAMA 上的顶刊多中心 RCT。提炼方式不是"读一读然后总结几条规则",而是先**跑脚本算量化指标**(句长节奏、分节 hedging 密度、连接词频谱、被动语态分布……),再逐节深读抽取模式,最后用对抗批评 + 留一盲判兜底——确保蒸馏出来的东西经得起验证,不是凭感觉写的。

## 三种用法

**Mode A — 改稿(最常用)。** 给一段稿子,一句一句告诉你哪里读起来不对——是基础科学腔、模板腔、还是 AI 腔——然后给出临床化的改写。对照量化指纹做自查,不是瞎改。

**Mode B — 从零写。** 告诉它论文类型和研究设计,直接按对应体裁的腔调起草某一节。

**Mode C — 整篇打磨。** 先确定研究类型和体裁 → 按 IMRaD 拆成单元 → 逐个单元改(各节可以并行,一篇长稿让多个 agent 同时改不同节)→ 最后跑一遍**强制跨节金线校验**(目的→结论的对齐、数字一致性、Methods↔Results 互查、没有悬空的"见补充材料"引用)→ 出三种东西:
- **一份 Markdown 修改报告**——哪段、什么问题、多严重、怎么改
- **一份带 Word 修订追踪的 .docx**——拒绝全部修订就能精确还原,改了什么一眼可见
- **一份纯中文《修改理由》.docx**——每条修改两行中文说清楚:改了什么、为什么(给导师看/给审稿人回)

## 跟泛泛的"临床写作技巧"有什么不一样

**第一,不是凭感觉,是量化的。** 把范文的语言特征算成了可查的指标,按体裁分了三档(A 临床观察 / B 影像标志物 / C 随机对照)。比如句长节奏——真实论文的句子长短落差很大(SD 大约是均值的 1.3–1.5 倍),AI 写的句子就是一个长一个长一个长,均匀到头;hedging 密度——Results 几乎不 hedge(≈0),Discussion 才密集(8–11/千词),差了一个数量级,全篇均匀 hedge 就是 AI 味最硬的信号;Methods 被动占比 55–72% 是**对的**,别拿通用"多用主动"去改;破折号在这个组几乎不用(≈0),一多就是 AI。这些都有脚本可跑——`scripts/metrics.py` 算指标,`scripts/check_draft.py` 一行命令查草稿。

**第二,教的是原理,不是模板。** 旧版有个 phrasebank,把范文拆成带空格的框架,让人往里填——结果就是"Nearly one in five patients experienced X"这种复读机模板。新版彻底推翻了:39 条招式,每条给的是**原理 + 范文原句(每条例句都 grep 回原文核实过,不是编的) + AI 腔反例 + 防重复提示**。不留任何可粘贴的空格句,你要理解的是为什么这么写,而不是抄一个句式。

**第三,降 AI 感这件事是从范文反推的,不是拍脑袋的。** 硬信号是语料本身告诉你的——uniform hedging、AI 高频连接词(Moreover / Additionally / Notably…)、"有重要临床意义"这种空洞收尾、假分数修辞("nearly one in five")。更隐蔽的 LLM 签名信号是跑留一盲判时发现的——警句式的段落收束("The novelty is elsewhere.")、人为制造的对称对偶、太整齐的 Frist…Second…Third 限制段、数字被削薄成概述、过度的润色把 ESL 论文该有的粗粝质感都磨掉了。这些现在都收在 `clinical_ai_tells.md` 里,写完自己查一遍。

**第四,该引用别人的就不自己写。** 通用 IMRaD 结构、hedging 体系、时态规范、CONSORT/STROBE/TRIPOD 这些报告标准——交给 `academic-research-skills` 插件和 `scientific-writing` skill,本 skill 不重复。词法层面的去 AI(26 条 pattern)交给 `humanizer_academic`,但给了临床豁免——Methods 被动语态别动、破折号按阈值不按零容忍、hedging 按 section 绑着来。本 skill 只做别处没有的事:**这个课题组到底怎么写。**

## 目录

```
SKILL.md                      # 路由、体裁分类、三种Mode、grep 循环、降 AI 顺序、引用表
references/
  voice_fingerprint.md        # A/B/C 量化指标 + 反 AI 硬规则(grep 索引)
  voice_principles.md         # 39 条反模板招式,逐条标范文出处 + AI 反例
  structure_contract.md       # 体裁骨架 + claim 强度梯级 + 强制跨节一致性
  clinical_ai_tells.md        # 语料推演的 AI 信号清单 + humanizer 临床豁免
  domain_notes.md             # mRS/ASPECTS/TICI/κ… 领域词表(只留课题组真用的)
  display_items.md            # 图注/表注/表格脚注——让读者不翻正文也能看懂
scripts/
  apply_tracked_changes.py    # ← v1 保留
  build_rationale_docx.py     # ← v1 保留
  metrics.py                  # 算量化指纹
  check_draft.py              # 一行查稿:python scripts/check_draft.py draft.txt --genre A
```

## 安装

```bash
git clone https://github.com/buergerSUN-CN/clinical-research-writing-skill.git \
  ~/.claude/skills/clinical-research-writing
```

## Mode C 修订追踪流水线

依赖 `docx` skill 自带的 `unpack.py` / `pack.py`:

```bash
python <docx-skill>/scripts/office/unpack.py manuscript.docx unpacked/ --merge-runs false
python scripts/apply_tracked_changes.py unpacked/ edits.json --author "Claude"
python <docx-skill>/scripts/office/pack.py unpacked/ manuscript_revised.docx --original manuscript.docx
```

## 实际怎么写(比如 Results,体裁 A)

```
grep -A6  "#results"          references/voice_principles.md
grep -A5  "#hedging"          references/voice_fingerprint.md   # Results ≈ 0
grep -A4  "#numbers"          references/voice_fingerprint.md   # n/N (%) + CI
grep -A15 "#tells"            references/clinical_ai_tells.md
```

写完跑:`python scripts/check_draft.py draft.txt --genre A`
