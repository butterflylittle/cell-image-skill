# Color, Proportion & Density System

科研图的颜色与比例用于表达**科学层级和语义**，不是装饰。

## 1. Palette budget

默认一张医学机制图：
- 1 个 neutral family：白/暖白/浅灰
- 2–4 个 semantic families：例如 cell/tissue、ion/signal、immune、drug/material
- 1 个 accent：仅用于关键触发/结果
- 主色相总数建议 ≤5；如果必须更多，低饱和处理
- 高饱和 accent 同时出现不超过 2 个

### Biomedical semantic defaults

| 语义 | 默认建议 | 示例色 |
|---|---|---|
| 正文/文字 | 深蓝黑/炭灰 | `#1F2940`, `#252525` |
| 细胞/组织 | peach / rose | `#F3B7BE`, `#F6C8C3` |
| membrane/skin | soft pink | `#EFA7B5` |
| nucleus / SR / vesicle | lavender | `#A996D9`, `#C2B3E8` |
| Ca²⁺ / water / transport | cyan / sky blue | `#38A9E8`, `#77C9F2` |
| immune T cell | blue / blue-violet | `#5A8EDB`, `#6E78D8` |
| tumor | muted rose / mauve | `#D98A9A`, `#B77B9E` |
| activation / energy | amber / orange | `#E89B31`, `#F3B64B` |
| inhibition / damage | vermillion | `#D55E00` |
| supportive / repair | teal / bluish green | `#009E73`, `#68A991` |

这些是默认 token，不要求机械套用；同一实体在全图必须同色。

## 2. Accessibility

Nature 官方 figure guide 要求考虑色觉障碍，避免 red/green 作为唯一差异编码，并建议高对比、可访问色板。正文文字尽量黑/白，不使用彩色文字。

可使用 Okabe-Ito / Nature-compatible 基础色：
- Orange `#E69F00`
- Sky blue `#56B4E9`
- Bluish green `#009E73`
- Yellow `#F0E442`
- Blue `#0072B2`
- Vermillion `#D55E00`
- Reddish purple `#CC79A7`
- Black `#000000`

医学插画不需要把这 8 色全部用上；通常取 3–5 色即可。

## 3. Saturation hierarchy

- 背景：0–5% 视觉饱和；推荐纯白或暖白
- 大面积组织/面板：20–45% 饱和
- 次要结构：30–55%
- hero signal / Ca²⁺ / drug / blockade：55–80%
- 禁止全图每个对象都 80% 饱和

## 4. Panel tint

如果需要分区：
- panel 背景只用 3–8% 色相染色
- 同一画布最多 3 种 panel tint
- Nature 正文模式尽量减少或取消 panel tint
- GA/教学模式可保留浅 tint，但不要像商业 dashboard

## 5. Line hierarchy

按最终尺寸：
- 主因果箭头：1.4–2.2 pt
- 次级箭头/transport：0.8–1.4 pt
- keyline/callout：0.6–1.0 pt
- Nature 最低线宽仍需服从期刊规范；不要用极细 hairline
- inhibition blunt bar 宽度与主箭头一致

## 6. Typography hierarchy

### 投稿正文图
- 服从期刊 profile；Nature 一般 5–7 pt、Arial/Helvetica
- panel label 独立，黑字
- figure title 通常不放图内

### Graphical Abstract / 教学图
在 16:9 1920×1080 等效预览时：
- title：48–68 px（若需要）
- stage heading：28–38 px
- entity label：20–28 px
- micro-detail：18–22 px，若再小就应减少标签

最终仍以物理尺寸而不是屏幕 px 判定可读性。

## 7. Canvas proportion rules

### 16:9 biomedical mechanism
- Outer margin：3–5% 宽/高
- Title（可选）：6–8% 高
- Hero mechanism：55–72% 面积
- Supporting/validation：15–28% 面积
- Footer/summary（可选）：≤8% 高
- Empty breathing space：总面积保留约 8–15%，不要全部填满

### A4 / portrait biomedical explainer
- Header：6–9%
- Hero area：40–55% 面积
- Sidebars：每侧 15–22% 宽度
- Detail/insets：15–25% 面积
- Bottom legend/cycle：8–15%

## 8. Information density levels

### D1 — minimal manuscript schematic
- 6–12 visible labels
- 1 hero + 1 support
- 最适合 Nature/Lancet 正文

### D2 — standard mechanism
- 12–20 labels
- 1 hero + 2–4 support relations
- 适合大多数 paper schematic / GA

### D3 — rich explainer
- 20–35 labels
- 允许 3–6 insets / numbered steps
- 适合教学、综述、海报；投稿时需要重新减法

### D4 — atlas/encyclopedic
- 35+ labels
- 仅用于综述/科普大图或附录；不作为默认投稿机制图

默认从 D2 开始，不要默认 D3/D4。
