> For approved-raster-to-SVG work, also read `svg-fidelity-contract.md`. SVG conversion is reconstruction under a frozen composition, not a redesign.

# SVG Output Contract

所有科研示意图、机制图、Graphical Abstract、技术路线图、研究框架图默认必须同时交付 **SVG + PNG**。SVG 是可编辑主文件，PNG 是预览/沟通版本；如目标期刊需要，再额外导出 PDF/EPS/TIFF。

## 1. SVG 是强制交付，不是可选项

除非用户明确只要位图，否则：

```text
PRIMARY_SOURCE = SVG
PREVIEW = PNG
OPTIONAL_SUBMISSION_EXPORT = PDF / EPS / TIFF according to journal profile
```

真实数据图若由 Python/R 生成，也应优先同时导出 SVG/PDF 与 PNG；显微、病理、WB 等原始位图证据本身不强制矢量化，但其排版、标注、箭头和文字层应保留为 SVG/PDF 可编辑对象。

## 2. 三种 SVG 模式

### A. `vector_native`
适用于：
- 教育/社科框架图
- 技术路线图
- CS/AI 架构图
- 流程图
- 简化机制图

要求：
- 主要形状、箭头、文字全部为 SVG 原生对象。
- 文字优先 `<text>`，不要默认转 path。
- 箭头/连线使用 `<path>` / `<line>` / marker。
- 不允许把整张 PNG 作为一张 `<image>` 塞进 SVG 冒充矢量。

### B. `hybrid_editable`
适用于：
- BioRender-like 生物医学机制图
- 器官/细胞/组织/纳米材料等需要复杂具象插画的图
- AI image-assisted 机制草图的可编辑重建

要求：
- 整体画布、所有文字、箭头、分组框、标签、强调区域必须是 SVG 矢量对象。
- 复杂生物实体允许作为局部 raster asset 嵌入 `<image>`，但不得以“整张生成图”作为唯一底图。
- 关键科学关系不能烘焙在 raster 中；必须用可编辑 SVG 箭头/阻断线重绘。
- 关键术语必须用 SVG `<text>` 重写，避免 AI 生成文字错误。
- 局部 raster asset 应按实体裁切，保留透明背景时优先使用 PNG/WebP。

### C. `vector_reconstructed`
适用于：
- AI 草图已经确定构图，需要人工/Agent 按草图重建投稿版。

要求：
- 不自动 trace 复杂 AI 图形成大量无语义 path。
- 按 Visual Schema 重新创建科学实体、箭头、文字和容器。
- AI 草图只作为 layout reference，不作为最终图层。

## 3. 禁止“假 SVG”

以下不算合格 SVG：

```xml
<svg ...>
  <image href="full_figure.png" width="100%" height="100%" />
</svg>
```

这种文件虽然扩展名是 `.svg`，但没有可编辑科学结构。

若用户只要求“能放进 SVG 容器”，可以提供，但必须标记：

`RASTER_WRAPPED_SVG — NOT EDITABLE VECTOR`

默认不得用它满足“输出 SVG 版本”的要求。

## 4. SVG 画布与尺寸

必须同时设置：

- `viewBox`
- 最终物理 `width` / `height`（投稿图优先 mm；屏幕 GA 可使用 px）
- 保持目标宽高比

示例：

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     width="183mm" height="102.94mm"
     viewBox="0 0 1600 900">
```

## 5. 文字

- 投稿版文字应尽可能保持 `<text>` 可编辑。
- 使用常见 sans-serif 字体栈，例如 `Arial, Helvetica, sans-serif`；中文可使用系统通用中文 sans-serif fallback。
- 不依赖本地私有字体文件。
- 专有名词、基因/蛋白、希腊字母必须逐字核对。
- 若期刊要求字体嵌入，应在 PDF/EPS 导出阶段处理；SVG 源文件仍保留可编辑文本。

## 6. 箭头与科学语义

箭头必须独立为 SVG 矢量对象，并与 Visual Schema 的 relation 一一对应：

- activation/progression：实线箭头
- inhibition/blockade：T-bar / blunt end
- transport/secretion：虚线箭头
- association：细虚线，无强因果暗示
- feedback：曲线回环

不能把关系只画在 raster asset 内。

## 7. 分层建议

推荐 SVG group id：

```text
<g id="background">
<g id="context">
<g id="hero-mechanism">
<g id="supporting-evidence">
<g id="validation">
<g id="relations">
<g id="labels">
<g id="annotations">
```

每个关键实体建议有稳定 `id`，便于后续自动修改。

## 8. 导出要求

每次交付至少：

```text
figure.svg   # authoritative editable source
figure.png   # preview, high resolution
```

投稿任务可再加：

```text
figure.pdf   # vector submission/export
figure.tiff  # when target journal requests raster
```

PNG 必须从最终 SVG/同一最终布局渲染，不允许 SVG 与 PNG 两套构图漂移。

## 9. SVG QA

生成后运行：

```bash
python scripts/audit_svg.py figure.svg
```

最低检查：

- [ ] XML 可解析
- [ ] 根节点为 `<svg>`
- [ ] 有 `viewBox`
- [ ] 有明确 width/height
- [ ] 不是单张 full-canvas raster wrapper
- [ ] 文字可编辑（有文字时）
- [ ] 箭头/连线为 vector object
- [ ] image-assisted 模式下 raster 只作为局部 asset
- [ ] SVG 与 PNG 的构图一致
- [ ] 最终版面字号符合 journal profile
