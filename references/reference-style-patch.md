# Reference Style Patch

参考图只用于提取“可迁移设计属性”，不复制科学内容。

## 必须抽取的 10 类属性

1. `canvas`：长宽比、portrait/landscape、是否 A4/16:9/square
2. `hero_ratio`：视觉中心大约占总面积多少
3. `zone_hierarchy`：主区、辅助区、validation/inset 的面积与先后级
4. `reading_direction`：左→右、上→下、中心→外、clockwise
5. `palette`：主色相数量、冷暖关系、饱和度、背景色
6. `semantic_color_mapping`：哪些颜色对应离子/细胞/免疫/药物/损伤等
7. `line_arrow_grammar`：线宽、实虚、activation/inhibition/zoom 连接方式
8. `typography_density`：标签数量、字号层级、黑字/彩色字、keyline 方式
9. `container_inset_style`：是否有卡片、放大框、虚线 zoom、圆形 detail inset
10. `depth_texture`：扁平、轻微渐变、soft 3D、组织/细胞纹理程度

## 可迁移

- reading direction
- visual center
- information density
- hero/support 比例
- palette saturation / semantic colors
- line/arrow style
- container shapes
- white-space rhythm
- label placement
- flat vs subtle depth
- icon detail level
- zoom/callout pattern

## 不可迁移

- 参考图具体结论
- 数据
- 文字标签
- 样本名
- 实验结果
- logo
- watermark
- 独特版权构图的精确复刻
- 可识别的专有图标/插画资产

## 输出 Style Patch

```yaml
canvas:
  aspect_ratio:
  orientation:
  margin_pct:
layout:
  archetype:
  hero_area_pct:
  support_area_pct:
  zones:
hierarchy:
reading_direction:
palette:
  background:
  main_hues:
  high_saturation_accents:
  semantic_mapping:
arrow_style:
container_style:
typography:
  density_level:
  title_policy:
  label_style:
depth:
zoom_pattern:
do_not_copy:
```

Style Patch 的优先级低于：
科学事实、用户明确要求、Evidence Boundary、Journal Profile。
