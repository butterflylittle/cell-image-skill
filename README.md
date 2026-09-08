# Cell Image Skill v2.4

一个把 **Research Content → Scientific Figure** 标准化的科研绘图 Skill。

它综合了三类能力：

1. **科研论证**：先定义 claim / evidence / reviewer risk，再画图。
2. **AI 绘图工程**：Domain Master × Figure Type × Visual Schema × Exact Text。
3. **出版规范**：Nature、The Lancet、Cell Press、Elsevier 等期刊的尺寸、字体、分辨率、文件格式与 AI artwork policy gate。


## Figure Intake：不再先问一堆参数

Cell Image 会先自动推断 `purpose / aspect_ratio / style / palette / language / output_formats`。只有高影响信息无法判断时才追问，默认最多一次确认 4 类：用途、比例、风格与色系、输出格式。科学结论或证据边界不清时，优先追问科学问题。

内置：
- `references/intake-workflow.md`
- `schemas/figure-intake.schema.json`
- `scripts/validate_intake.py`

同时新增 approved raster → editable Master SVG 的文字/几何分离工作流：先冻结构图、记录 Text Manifest，再进行重建和 live text 恢复，避免“PNG 很漂亮，SVG 重画后变成圆圈流程图”。

## 核心工作流

```text
Paper / Proposal / Abstract
          ↓
   Research Parser
          ↓
   Figure Contract
          ↓
 ┌────────┴─────────┐
Domain Router   Figure-Type Router
          ↓
 Journal / AI Policy Gate
          ↓
      Visual Schema
          ↓
 Exact Visible Text Contract
          ↓
     Rendering Route
  ┌───────┼────────┐
Vector  Image-assisted  Data plot
          ↓
    Scientific Critic
          ↓
   Publication / Visual QA
          ↓
SVG (authoritative editable source) + PNG preview + PDF/EPS/TIFF when required
```

## 适用领域

- 生物医学：信号通路、药物机制、肿瘤免疫、纳米递送、临床机制
- 材料化学：自组装、响应材料、界面、反应、能量/传质
- 教育/社科：研究框架、治理、评价、主体关系、路径
- CS/AI：Agent、RAG、模型架构、系统流程、知识图谱

## 重要改进

### 1. 不再把“BioRender 风格”当作期刊规范

BioRender-like 只解决“科学实体如何视觉化”。

期刊规范另外控制：

- 最终宽度/高度
- 字号
- 线宽
- 是否允许阴影/装饰
- 图题是否放图内
- 文件格式
- DPI
- editable text
- AI artwork policy

### 2. 图像生成只是一条渲染路径

- 中文/结构密集图：SVG/矢量优先
- 生物医学概念机制：image-assisted
- 真实数据：deterministic plot
- 显微/WB/病理：绝不生成伪数据

### 3. 强制 SVG + PNG 双交付

所有机制图、Graphical Abstract、技术路线、研究框架默认输出：

```text
figure.svg   # 主文件，可编辑
figure.png   # 预览文件
```

SVG 分为三种模式：

- `vector_native`：框架图、技术路线、CS/AI 架构等原生矢量。
- `hybrid_editable`：生物医学/纳米材料复杂插画可局部嵌入 raster，但文字、箭头、关系必须为 SVG 矢量对象。
- `vector_reconstructed`：根据 AI 草图重新搭建正式投稿版。

禁止把整张 PNG 塞进 `<svg>` 作为唯一内容来冒充矢量文件。Skill 内置 `scripts/audit_svg.py` 做检查。

### 4. Exact Visible Text

最终图像 Prompt 内强制限定可见文字白名单，降低 AI 乱字和随机标题。


### 5. 新增 Biomedical Layout / Palette 规范

Skill 现在会先判断医学图属于哪类构图：

- anatomy → microstructure
- cell-centric mechanism
- preparation + in vitro/in vivo split
- horizontal causal pathway
- closed-loop therapy
- multiscale zoom
- educational explainer

并使用统一的比例预算、颜色预算和信息密度等级，而不是“看到多少内容就塞多少框”。

默认 16:9 医学机制图以 **55–72% 画布留给 hero mechanism**，support/validation 只占 15–28%；主色相建议不超过 5 个，高饱和强调色不超过 2 个。

参考图只抽取布局、层级、颜色、箭头、字体密度和 zoom 方式，形成 style patch；不复制具体科学内容。

## 快速使用

```text
使用 cell-image：
根据下面研究内容生成一张 16:9 生物医学机制图。
目标：Cell/Nature 风格内部设计草图。
先给 Figure Contract，再生成 Visual Schema 和最终图。
```

或：

```text
使用 cell-image：
把这份国家社科课题论证生成 A4 活页研究框架图。
vector-first，中文，输出 SVG + PNG。
```

## 期刊 Profile

已内置：

- `nature_main_figure`
- `lancet_figure`
- `cell_graphical_abstract`
- `elsevier_main_figure`
- `science_style_main_figure`
- `generic_high_impact`
- `cn_grant_a4`
- `internal_biorender_draft`

**投稿前仍需复核目标期刊当前官方 Guide for Authors。**

## 来源说明

本 Skill 的架构设计吸收了：
- claim-first / QA-first 的科研图工程思想；
- Domain Master、Visual Schema、Exact Visible Text、Reference Style Patch 等 prompt-engineering 思路；
- Nature、The Lancet、Cell Press、Elsevier 等官方图件规范。

具体来源与版权边界见 `references/source-notes.md`。本 Skill 文本为重新组织和原创实现，不复制第三方 Skill 的大段原文。


## v2.4 Intake + Editable Reconstruction

v2.4 将 skill 正式更名为 **cell-image**，并加入 Figure Intake Gate。用户不再需要手工回答字体、线宽、箭头等大量细节；Skill 自动推断，只有关键歧义才追问。

同时强化 approved raster → editable SVG：`Anchor Map + Text Manifest + Master SVG + Fidelity QA`。整张 PNG 包进 `<svg><image>` 仍不算合格 editable SVG。
