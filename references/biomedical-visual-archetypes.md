# Biomedical Visual Archetypes

本文件把高质量医学机制图拆成可复用的**构图原型**，用于选择比例、视觉中心、信息密度和辅助区域。学习的是视觉语法，不复制参考图的具体内容、标签、数据或独特构图。

## 总原则：先选 archetype，再分配画布

生物医学图不要默认“平均分成若干卡片”。先判断主叙事属于哪一种：

1. `anatomy_to_microstructure`：器官/母体环境 → 组织 → 微观结构/交换界面
2. `cell_centric_mechanism`：一个大细胞/细胞器作为 hero，周围放调控与分子细节
3. `preparation_plus_validation_split`：顶部制备/构建，底部 in vitro / in vivo 双验证
4. `horizontal_causal_pathway`：从刺激 → 细胞过程 → 分子机制 → 功能结局
5. `closed_loop_therapy`：递送/治疗 → 细胞死亡 → 免疫激活 → 再杀伤的闭环
6. `multiscale_zoom`：宏观器官 → 局部组织 → 细胞 → 分子/膜蛋白的连续放大
7. `educational_explainer`：核心机制 + 3–6 个带编号的放大步骤，适合科普/教学但仍保持科学准确

---

## A. Anatomy → microstructure：解剖主视觉 + 微结构主体

### 适用
胎盘交换、肺泡-毛细血管、肾小球滤过、肠绒毛吸收、血脑屏障等跨尺度交换问题。

### Portrait/A4 推荐比例
- Header/title：画布高度 6–9%
- 上部宏观解剖：26–34%
- 中部/下部微结构 hero：40–50%
- 左右辅助机制栏：各占宽度 15–20%，但视觉饱和度低于中心 hero
- 底部 2–4 个 detail zoom：高度 14–20%
- 外边距：3–5%

### 层级
中心微结构面积必须最大；左右机制栏不得抢主视觉。

### 常见结构
`macro anatomy → dashed zoom → microstructure → transport / immunity / barrier detail`

---

## B. Cell-centric：大细胞 hero + 周边调控/分子放大

### 适用
胃壁细胞质子泵、线粒体代谢、肝细胞脂代谢、神经元突触、肾小管转运等。

### Portrait 推荐比例
- Hero cell：宽度 42–55%，高度 55–72%
- 左侧 regulatory sidebar：18–24%
- 右侧 molecular-detail inset：20–28%
- 底部 cycle / resting-vs-active：20–30% 高度，可与 hero 部分重叠布局
- 细胞内部标签：优先 keyline + 黑字，不用彩色文字贴在复杂背景上

### Hero 内部
细胞膜、细胞器、泵/通道的位置必须符合生物学空间关系。

### 视觉节奏
`whole cell → membrane transport → molecular detail → regulation → state comparison`

---

## C. Preparation + in vitro/in vivo split

### 适用
外泌体、纳米药物、基因载体、细胞治疗、材料制备 + 动物验证。

### Landscape 4:3 / 16:9 推荐比例
- 顶部 preparation strip：14–22% 高度
- 底部 validation area：74–82% 高度
- 底部左右 split：48:48 或 46:50，gutter 2–4%
- `in vitro` 与 `in vivo` 用非常浅的不同底色区分，不用高饱和大色块
- 主治疗物/纳米载体在上下区域保持同一视觉编码

### 叙事
`construct → in vitro mechanism → in vivo phenotype/outcome`

---

## D. Horizontal causal pathway

### 适用
信号通路、兴奋-收缩耦联、炎症 → 转录 → 表型、药物 → receptor → outcome。

### 16:9 推荐比例
- 如果是教学/GA，可有 title：高度 6–8%；正文投稿图则通常不在图内放标题
- 主路径区域：高度 70–82%，宽度 88–94%
- validation/inset：总面积 12–25%
- 左右推进：3–6 个关键 stage，尽量单向不回头
- 每个 stage 的 visual footprint 与科学重要性成比例，不要求等宽

### 叙事
`trigger → entry/activation → amplification → molecular switch → functional output`

---

## E. Closed-loop therapy

### 适用
肿瘤化疗+免疫、代谢-免疫反馈、材料响应-治疗-免疫循环等。

### 16:9 推荐比例
- Hero loop 占画布 68–80%
- 起始制备/给药：10–18%
- 细胞内机制：28–40%
- 免疫/组织结局：22–32%
- feedback loop arrow 只保留 1 条主闭环，不要多条大回环竞争
- 结论 ribbon 若存在：≤8% 高度；Nature 正文模式通常移除 ribbon

### 闭环必须成立
只有原文支持反馈或协同闭环时才能画回环；否则画成线性协同链。

---

## F. Multiscale zoom

### 适用
器官 → 组织 → 细胞 → 膜蛋白/基因；尤其适合跨尺度医学解释。

### 推荐结构
- 3–4 个尺度，最多 5 个
- 每次 zoom 使用虚线框、放大镜或 thin keyline；不要用多个粗边框
- 下一级面积可比上一级大 1.3–2.2 倍
- 最终 molecular inset 要成为“机制解释终点”，不是装饰

---

## G. Educational explainer

### 适用
医学科普、课程图、讲义、答辩说明图。

### 推荐比例
- 主体 anatomy/cell：35–50% 画布
- 3–6 个 numbered step：总面积 35–50%
- 最终 outcome：8–15%
- 标题可占 6–9%；正文科研图则默认取消大标题

### 与投稿图区别
教学图允许更明显的编号、浅色卡片和解释性 icon；投稿正文图应减小标题、卡片背景、装饰性图标和渐变。

---

## Archetype 选择规则

优先回答以下问题：

1. 读者首先要理解“空间结构”还是“因果过程”？
2. 是否存在一个天然 hero（器官、细胞、纳米粒、组织界面）？
3. 验证证据是主结论的一部分，还是辅助？
4. 是否真的存在闭环？
5. 是否必须跨尺度？

不要为了“看起来丰富”混用 4 种以上 archetype。通常 1 个主 archetype + 1 个辅助 archetype 足够。
