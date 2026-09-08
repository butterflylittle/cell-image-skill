# Domain Masters

领域母版定义“科学对象应该长什么样、关系应该如何表达”。图型定义信息组织方式，两者不能混淆。

---

## 1. Biomedical

### 适用
信号通路、肿瘤免疫、药物机制、纳米递送、感染/炎症、组织-细胞-分子跨尺度机制。

### 视觉对象

| 概念 | 推荐视觉实体 |
|---|---|
| cell | 有细胞膜/细胞质/细胞核的有机形态 |
| tumor cell | 异形细胞，必要时与正常细胞区分 |
| T cell | 蓝/青系免疫细胞，表面受体可见 |
| receptor | 位于膜或细胞内正确区域 |
| protein | 简化折叠蛋白/受体图形，不用无意义矩形 |
| DNA/promoter | 双螺旋 + 被高亮的调控区 |
| miRNA | 短 RNA / hairpin-like 符号 |
| antibody | Y-shaped |
| nanoparticle | core-shell / lipid-polymer layer / surface ligand |
| drug | 小分子球/药物载荷 |
| antigen | 小颗粒/肽段，结合 APC/T cell 语境 |
| endosome/lysosome | 囊泡 + 酸性标记 |
| blood vessel | 红色血管，只在递送/肿瘤靶向需要时出现 |

### 箭头语法
- 激活/促进：实线箭头
- 抑制：T 型 blunt bar
- 分泌/运输/易位：虚线或点线箭头
- association：细虚线，不表达因果
- feedback：曲线回环
- uptake：跨膜箭头 + 内吞囊泡
- release：载体解离/开裂 + payload 离散扩散

### 视觉层级
1. Hero mechanism
2. upstream trigger
3. downstream outcome
4. validation
5. context

### 禁止
- 不把所有分子都画成彩色圆球
- 不把所有细胞都画成同一个圆
- 不凭空增加 cytokine、receptor、organelle
- 不生成伪显微/伪病理“证据”

---

## 2. Materials & Chemistry

### 适用
纳米材料、自组装、酸/光/热响应、催化、晶格、界面、电化学、传质/能量路径。

### 视觉对象
- polymer：链/线团
- lipid/surfactant：头尾结构
- nanoparticle：核壳、层状、孔结构
- crystal：规则晶格/单元阵列
- ion：带电小球 + 标签
- interface：清晰平面边界
- reaction：反应物 → 中间态 → 产物
- trigger：pH / light / heat / redox 等明确物理刺激

### 机制语义
- 自组装：多组分收敛到统一颗粒
- 解离/释药：结构变化必须可见
- 扩散：渐疏粒子 + 方向箭头
- 催化：表面位点与反应路径对应
- 相变：结构前后对照，禁止“魔法特效”

---

## 3. Education & Social Science

### 适用
国家社科、教育学、数字教育、治理、评价、主体关系、理论模型、机制路径。

### 视觉对象
- actor：教师/学生/平台/治理者/机构
- construct：圆角模块/概念节点
- evidence：数据/评价/证据链
- governance：制度/规则/责任/平台
- feedback：闭环
- multi-dimension：轮盘/中心辐射/分层系统

### 默认
`vector-first`

### 视觉语法
- 结构 > 插画
- 中文真实文本对象
- 4–6 个低饱和模块色
- 线性图标只作为辅助，不当主视觉
- 箭头必须有关系词：驱动/支撑/中介/反馈/约束

### 禁止
- BioRender 化
- 商业咨询公司风大标题
- 玻璃拟态、霓虹
- 过多人物插画
- 长段落塞进框

---

## 4. CS / AI

### 适用
Agent、RAG、Multi-Agent、LLM pipeline、知识图谱、检索、训练推理架构。

### 视觉对象
- document：纸张/文本块
- embedding/tensor：矩阵/向量栈
- database/vector store：圆柱
- model/LLM：模块块 + 模型名
- agent：圆角模块 + tool/memory context
- graph：节点边结构
- user/system/tool：明确角色
- feedback loop：曲线回环

### 视觉语法
- pipeline 逻辑优先
- 严格正文图：扁平、少阴影
- 展示型 graphical abstract：可增加轻微层次，但不变成医学图
