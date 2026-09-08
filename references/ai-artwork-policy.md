# AI Artwork Policy Gate

**Last checked: 2026-09-07. 政策变化很快；投稿前必须重新核对目标期刊官方页面。**

## 1. 基本分类

### A. Explanatory / conceptual figure
如：
- flow chart
- schematic
- mechanism concept
- experimental workflow

可否 AI 生成：取决于出版商/期刊政策。

### B. Data visualization
必须直接、可复现地来自真实数据。

AI 可以辅助代码，但不能编造数据。

### C. Primary research image
如：
- microscopy
- histology
- western blot
- gel
- radiology
- patient photo

**禁止用生成式 AI 创造“看起来像实验结果”的图像。**

---

## 2. Elsevier journals — 2026 policy

Elsevier 2026 更新后的 journal policy：

- 某些 explanatory images 可使用 AI 辅助创建，但要求 human oversight 和 disclosure
- primary research images 不允许用生成式 AI 创造/修改
- graphical abstracts：通用 generative AI image tools 不应使用；建议 dedicated scientific illustration tools，如 BioRender / Mind the Graph / professional illustration tools
- 需要检查工具许可是否允许发表
- 可能要求保留 AI 使用文档

官方：
https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals

### Skill 行为
目标为 Elsevier graphical abstract 时：
- image_gen 输出只能标记 `INTERNAL_DESIGN_DRAFT`
- 推荐最终在 BioRender/Illustrator/Inkscape 中重建
- 不称为 submission-ready

---

## 3. Nature Portfolio

Nature Portfolio 官方 AI policy 采用风险评估、透明、人类负责、保密优先的框架。

同时，2026 Nature Methods editorial 明确表示 Nature Portfolio 不允许 AI-generated artwork（并强调版权/法律不确定性）。

官方：
https://www.nature.com/nature-portfolio/editorial-policies/ai
https://www.nature.com/articles/s41592-026-03020-1

### Skill 行为
目标为 Nature Portfolio：
- 默认 `AI_ARTWORK_STATUS = VERIFY_REQUIRED`
- 通用图像模型生成的图只作为 internal concept draft
- 投稿终稿应采用人工/专业科学绘图工具重建，除非目标期刊最新官方规则明确允许
- 不上传未授权的保密稿件到第三方公共 AI 服务

---

## 4. The Lancet

The Lancet 属 Elsevier 体系，同时有内部 artwork redraw 工作流。

### Skill 行为
- 生成式机制图作为构图草稿
- 投稿终稿优先提供可编辑矢量/专业科学插图
- 按 Elsevier 最新 AI 图像政策额外核验

---

## 5. Policy status 输出

每次投稿向任务都应返回：

```text
AI_POLICY_STATUS:
- VERIFIED_ALLOWED
- VERIFIED_WITH_DISCLOSURE
- VERIFY_REQUIRED
- NOT_ALLOWED_FOR_FINAL_ARTWORK
```

和：

```text
DELIVERY_STATUS:
- SUBMISSION_CANDIDATE
- INTERNAL_DESIGN_DRAFT
```
