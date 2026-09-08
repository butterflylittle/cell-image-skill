# Figure Intake Workflow

目标：用最少问题得到足够稳定的绘图约束。不要把科研绘图变成问卷。

## 1. 三层参数

### A. 用户参数（优先让用户控制）

- `purpose`：论文正文 / Graphical Abstract / 基金申请 / PPT / 教学科普 / 综述
- `aspect_ratio`：16:9 / 4:3 / A4 portrait / 1:1 / journal profile / custom
- `style`：BioRender-like / restrained journal / medical illustration / flat vector / semi-realistic / reference-derived
- `palette`：蓝紫科研 / 蓝粉医学 / 青绿生物 / 红蓝对比 / Nature低饱和 / 黑白打印 / reference-derived / custom
- `language`：中文 / English / bilingual
- `reference_image`：无 / 只参考布局 / 只参考配色 / 只参考画风 / 综合 style patch
- `output_formats`：PNG / SVG / SVG+PNG / PPTX / AI / PDF

### B. Skill 自动参数（默认不要逐项询问）

- `figure_type`
- `layout_profile`
- `density_level`
- `hero_area_pct`
- `outer_margin_pct`
- `arrow_grammar`
- `font_scale`
- `line_weight`
- `panel_tint`
- `title_policy`

### C. 科学参数（必须获取或可靠推断）

- `core_conclusion`
- `required_entities`
- `required_relations`
- `evidence_status`
- `forbidden_content`
- `visible_text`

## 2. 询问策略

### 2.1 先自动推断，再询问

先从用户上传的论文、摘要、课题文本、参考图和当前请求中推断 Figure Setup。不要重复询问已经明确的信息。

### 2.2 最多一次询问 4 个关键设置

如果仍有会显著影响结果的未知项，优先询问：

1. 用途
2. 比例/版式
3. 风格与色系
4. 输出格式

科学结论或证据边界不清时，科学问题优先级高于视觉问题。

### 2.3 可以直接使用默认值的情况

当用户只是说“生成机制图”且上下文足够时，可展示推断后的设置并直接执行，除非存在高影响歧义。

推荐默认：

```yaml
purpose: internal_concept_draft
aspect_ratio: "16:9"
style: biorender_like
palette: biomedical_blue_purple_pink
language: auto
output_formats: [svg, png]
density_level: D2
background: "#FFFFFF"
title_policy: none
```

### 2.4 必须追问的情况

以下未知项若无法从上下文安全推断，则必须追问：

- 用户明确要求投稿，但未说明目标期刊且其版面要求会影响尺寸/AI policy
- 核心结论存在两种以上互斥解释
- 关键关系到底是因果还是相关无法判断
- 用户要求严格复刻参考图，但没有提供参考图
- 用户要求自定义尺寸/品牌色，但没有给具体约束

## 3. 推荐用户确认格式

不要连续问十几个问题。输出一个紧凑的 Figure Setup，例如：

```text
已识别：
用途：论文机制图
图型：closed_loop_therapy
比例：16:9
风格：BioRender-like
配色：蓝紫 + 粉红
信息密度：D2
标题：无
输出：SVG + PNG

如无修改，我按以上设置生成。
```

若用户只修改“绿色”，只更新 palette，不重新询问其他字段。

## 4. 用途驱动默认值

| 用途 | 默认比例 | 默认密度 | 标题 | 风格 |
|---|---|---:|---|---|
| manuscript_figure | journal profile / 16:9 draft | D1-D2 | none | restrained journal |
| graphical_abstract | 1:1 or journal profile | D2 | optional | BioRender-like / editorial |
| proposal_framework | A4 / 4:3 | D2-D3 | optional | vector-first |
| presentation_overview | 16:9 | D2-D3 | yes/optional | presentation |
| educational_explainer | 16:9 / A4 | D3 | optional | medical explainer |
| review_figure | 16:9 / journal profile | D3 | none | structured dense |

## 5. 参考图语义

用户上传参考图时，不默认“照抄”。先解析：

- `layout_reference`
- `palette_reference`
- `rendering_reference`
- `arrow_reference`
- `typography_density_reference`

默认只提取视觉语法，不复制第三方具体科学内容、标签、logo、水印或可识别专有美术资产。
