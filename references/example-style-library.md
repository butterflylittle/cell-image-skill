# Example-derived Style Library

本文件记录从用户提供及公开学术图例中抽取的**可迁移设计规律**。只学习布局、比例、颜色、层级、箭头和信息密度，不复制具体图像内容。

## Example family 1 — Placental / exchange-interface atlas

可迁移规律：
- portrait 长图适合“宏观解剖 + 中央微结构 + 两侧机制栏 + 底部放大细节”
- 中央 villous/microstructure 是 hero，占最大面积
- 母体/胎儿两套流向用成对暖/冷色编码，并在全图保持一致
- 辅助机制栏使用浅色卡片，不与中心 hero 同饱和度
- dashed zoom 连接宏观与微观，比粗箭头更适合“放大关系”
- 密集标签仍通过 keyline 与黑字保持可读

适用：placenta、lung alveoli、glomerulus、intestinal villi、BBB。

## Example family 2 — Gastric parietal cell / cell-centric atlas

可迁移规律：
- 一个超大细胞承担 45–55% 画布，作为空间坐标系
- 泵、通道、囊泡、线粒体直接放在生物学正确位置
- 左侧放 regulation / activation / inhibition，右侧放 molecular-detail inset
- 底部 cycle 用环形结构解释 ATP 驱动过程
- 颜色按离子/结构语义统一，而不是每个 panel 自己换色

适用：ion pump、transport cell、metabolic cell、secretory cell。

## Example family 3 — Exosome / nanoparticle preparation + validation

可迁移规律：
- 顶部 15–20% 只讲“制备/装载”，一条直线完成
- 下方 80% 再分 `in vitro` / `in vivo`
- 两大验证区用轻微底色差异，而不是边框堆叠
- 同一载体图标在 preparation、cell、animal 三个尺度保持同一颜色和形态
- before/after 只在 in vivo 中出现，避免与体外机制争抢

适用：exosome、nanocarrier、cell therapy、gene delivery。

## Example family 4 — Horizontal mechanism / causal story

可迁移规律：
- 16:9 中把主要机制压成 4–6 个动作节点
- 每个节点都有明确“实体 + 动作”，而不是只有一个词
- 主箭头尽量横向统一，分支/反馈只作为次级关系
- outcome 放在右侧终点，避免把验证证据平均铺开

适用：signaling、excitation-contraction、drug-response、metabolic pathway。

## Example family 5 — Closed-loop chemo-immunotherapy

可迁移规律：
- 上层制备，中层细胞内机制，下层免疫结局，是强语义分层
- 大回环只能表示真正的协同/反馈，不是装饰
- 颗粒、肿瘤细胞、T cell 要保持跨区域视觉身份一致
- 免疫检查点 blockade 用明确 receptor-ligand + blunt/block symbol，不用普通箭头

## Example family 6 — Educational cardiomyocyte explainer

可迁移规律：
- 上方一个完整 cardiomyocyte 给空间全貌
- 下方 4–6 个 numbered magnified steps 提供局部过程
- Ca²⁺ 使用单一高识别度 cyan，高饱和只用于离子与电信号
- action potential → Ca influx → CICR → troponin → cross-bridge 是严格单向故事
- 教学图可使用 title 和编号；投稿正文版应删除大标题与大卡片背景

## 对用户新增参考图的处理规则

任何新参考图先抽取八类属性：
1. canvas/aspect ratio
2. hero area proportion
3. zone count and hierarchy
4. reading direction
5. palette and semantic colors
6. line/arrow grammar
7. typography density
8. inset/zoom pattern

形成 style patch 后再叠加到 Domain Master，不复制图片中的科学内容、数据、标注、logo、水印或独特图形资产。
