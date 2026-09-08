# Visual & Publication QA

## 1. 3-second test
- [ ] 第一眼能看出核心机制
- [ ] 一个 hero，不是五个 hero
- [ ] 阅读方向无需猜

## 2. Layout
- [ ] 箭头不穿字
- [ ] 主要箭头交叉尽量为 0
- [ ] supporting evidence 视觉权重低于 hero
- [ ] 边缘留白均匀
- [ ] 不靠“更多颜色”解决层级

## 3. Typography
- [ ] 所有术语拼写正确
- [ ] 最终尺寸可读
- [ ] 期刊正文图不使用海报式大标题
- [ ] figure title/legend 按期刊要求放 manuscript，而非硬塞图内
- [ ] 文字可编辑或可重建

## 4. Color
- [ ] 同一概念全图同色
- [ ] 红/绿不作为唯一差异编码
- [ ] 黑白/色盲模式仍能区分主关系
- [ ] 高饱和只给 hero signal

## 5. Effects
- [ ] Nature 正文图避免 drop shadows/装饰性图标
- [ ] Lancet 图尽量 2D
- [ ] 不使用霓虹/玻璃拟态
- [ ] BioRender-style 不等于重 3D

## 6. File
- [ ] SVG + PNG 均已交付（除非用户明确取消 SVG）
- [ ] SVG 有 `viewBox` 与明确 width/height
- [ ] SVG 不是单张 full-canvas raster wrapper
- [ ] 文字、箭头、关系线可编辑
- [ ] image-assisted 时 raster 仅作为局部 asset
- [ ] PNG 与 SVG 来自同一最终布局
- [ ] `scripts/audit_svg.py` 通过
- [ ] final width 正确
- [ ] DPI 正确
- [ ] vector/bitmap 类型正确
- [ ] fonts embedded / editable
- [ ] caption 独立（若期刊要求）
- [ ] AI policy 状态明确

## 7. Proportion budget
- [ ] hero mechanism 占画布 55–72%（16:9 biomedical 默认）或符合所选 layout profile
- [ ] support/validation 不超过 hero 的视觉权重
- [ ] outer margin 约 3–5%，四边一致
- [ ] 只保留 1 个真正的视觉中心
- [ ] title 仅在 GA/教学图保留；正文投稿图遵守期刊 title policy
- [ ] 留出 8–15% breathing space，避免“每个角落都填满”

## 8. Palette budget
- [ ] biomedical 主色相默认 <=5
- [ ] 高饱和强调色 <=2
- [ ] panel tint <=3 且非常浅
- [ ] 同一实体跨区域颜色一致
- [ ] 颜色表达科学语义，不按 panel 随意换色
- [ ] red/green 不是唯一编码；灰度和色盲模拟仍可读

## 9. Density
- [ ] D1: 6–12 labels；D2: 12–20；D3: 20–35；D4: 35+
- [ ] manuscript 默认 D1–D2
- [ ] D3/D4 必须有教学/综述/atlas 的明确理由
- [ ] 文字密度提高时优先扩大画布/转 portrait，而不是无限缩字号
