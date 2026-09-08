# Language & Visible Text Strategy

## 三层语言

1. 用户沟通语言
2. 绘图模型 Prompt 语言
3. 图中可见文字语言

不要混为一谈。

### 英文 SCI
- 用户可中文交流
- Prompt 建议英文
- 图中标签英文

### 中文课题
- 用户中文
- Prompt 中文/英文均可
- 图中标签中文

---

## Exact Visible Text Contract

英文：

```text
All visible text in the figure must use only the following exact labels:
1. "..."
2. "..."

Do not render any title, legend, paragraph, footnote, random text,
or structural field outside this list.
```

中文：

```text
图中所有可见文字只能使用以下内容：
1. “……”
2. “……”

不要生成列表之外的标题、图例、说明段、脚注、随机文字或结构字段。
```

## 标签密度

- 机制图：通常 8–18 个短标签
- 复杂 GA：通常 10–25 个短标签
- Nature 正文图：尽量进一步减少
- 中文研究框架：文字很多时必须 vector-first

## 文本长度

- 英文核心标签：1–5 words
- 中文核心标签：2–10 汉字
- 次级说明：尽量不超过 8–12 words / 18 汉字

## AI 文字风险

即使使用强文字渲染模型：
- gene/protein/drug 名称仍需逐项核对
- promoter / receptor / phosphorylation 等词容易被拼错
- 最终投稿版优先用矢量文字覆盖
