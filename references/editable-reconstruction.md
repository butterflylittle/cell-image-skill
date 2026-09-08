# Editable Reconstruction Workflow

当用户确认一张高质量位图，并要求真正可编辑的 SVG/PPT/AI 时，使用此流程；不得依据语义重新设计。

```text
approved raster
  ↓
composition freeze
  ↓
anchor map + text manifest
  ↓
text-free geometry draft
  ↓
vector / local-asset reconstruction
  ↓
Master SVG
  ↓
restore live editable text
  ↓
SVG render comparison
  ↓
PNG / PDF / PPTX / AI export
```

## 1. Text Manifest First

在删除/覆盖图中文字之前，记录每个 label 的：

- exact content
- source bbox
- baseline anchor x/y
- font size/family/weight（可估计）
- color
- alignment
- rotation
- z/paint order

不要从清理后的图片重新估计文字坐标。

## 2. Preserve Non-text Geometry

文字清理只能删除字符并修复其局部背景。禁止移动、重绘、美化或新增非文字对象。清理后必须全画布对照检查：

- layout
- object shape
- connector
- line weight
- color
- crop
- scale

如非文字内容发生变化，应先修正，再进入矢量重建。

## 3. Master SVG Contract

Master SVG 必须：

- 保持 source aspect ratio
- 保持 source z-order
- compound path 保持洞/镂空语义
- text 为 live SVG text，而不是轮廓或位图
- 关键箭头、阻断线、关系线为原生 SVG geometry
- 局部复杂生物结构可以使用裁切后的 raster asset，但不得用 full-canvas raster wrapper 冒充可编辑 SVG

## 4. Fidelity QA

最终 SVG 渲染成 PNG，与 approved raster 并排检查：

- hero bbox / scale
- anchor position
- arrow topology
- label baseline
- semantic color
- z-order
- compound holes

视觉一致性优先于“为了纯 path 而把细胞画成圆圈”。
