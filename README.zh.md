<div align="right"><a href="README.md">English</a></div>

# 临床科研写作

一套由 Claude Code 和 Codex 共用的临床论文写作 Skill，用于起草、诊断、修改和投稿前审计；
所有改写都必须保留原始事实、统计量、研究方法和引用。

v2 将能力明确拆成两层：

- **通用临床写作核心**：患者和临床决策导向、研究设计逻辑、claim强度、数字忠实、IMRaD
  边界和跨章节一致性。
- **神经血管/卒中画像**：卒中、神经影像和神经介入术语，以及从32篇论文测得的语言指纹。

因此，其他临床专科可以安全使用通用核心；只有真正属于卒中或神经血管研究时，才加载专科
画像和数值范围。

## 能做什么

- 逐句指出基础科学腔、模板腔或AI腔，并给出临床化改写。
- 起草标题、摘要、IMRaD、limitations、conclusion、表格和图注。
- 整篇论文精修，并强制核对Methods-Results、数字、术语和claim梯级。
- 按STROBE、CONSORT、STARD或TRIPOD逐项审计。
- 生成Word修订追踪和中文《修改理由》。
- 检查临床AI痕迹；卒中稿件还可与32篇语料的量化指纹比较。

## 新接口

```bash
python3 scripts/check_draft.py draft.txt \
  --study-family observational --profile general

python3 scripts/check_draft.py stroke_draft.txt \
  --study-family imaging --profile neurovascular
```

旧的 `--genre A|B|C` 继续兼容，并自动启用神经血管画像。

## 它是怎样蒸馏出来的

私有参考工程包含32篇完整论文：13篇观察性/程序比较、7篇诊断或影像、12篇随机试验或试验
二次分析。流水线依次进行：

1. 先标元数据和研究类型；
2. 用脚本测量分章节句长节奏、hedging、被动语态、统计密度、连接词和标点；
3. 提取Title/Abstract、Introduction、Methods、Results和Discussion；
4. 蒸馏各章节的决策规则和临床认知层；
5. 核验来源、查模板陷阱和规则矛盾；
6. 做leave-one-out和新旧版本盲评；
7. 编译成按需加载的Skill。

仓库公开[蒸馏方法](distillation/METHOD.md)、JSON Schema、聚合报告和脱敏语料清单，但不公开
PDF、论文全文、长篇逐字范文、本机路径或私有评估材料。

方法上参考了两个公开项目：
[writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill) 启发了语言、结构与
认知层的分离；[book-to-skill](https://github.com/virgiliojr94/book-to-skill) 启发了编译期抽取、
决策规则、反模式和运行时按需加载。本仓库的临床Schema、语料分析、规则、脚本和验证设计均为
本项目自己的实现。

## 双端安装

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

两端使用同一个仓库和同一套核心文件。`agents/openai.yaml` 只提供Codex界面信息，Claude Code
会自然忽略。

## 验证

```bash
python3 scripts/check_draft.py --help
python3 distillation/pipeline.py --help
python3 -m unittest discover -s tests -v
```

## 版权与能力边界

原创代码和蒸馏规则采用MIT许可证；来源论文版权仍属于原权利人，仓库不包含论文正文。量化
语言指纹只在声明的神经血管/卒中语料上得到验证，不能包装成所有临床专科的通用标准。
