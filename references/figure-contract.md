# Figure Contract

## 目的

把“我要画一张图”转换成一个可审查的科学任务。

## 必填字段

```yaml
core_conclusion:
results_level_question:
artifact_purpose:
domain:
figure_type:
target_journal:
final_size:
reading_order:
hero_element:
supporting_evidence:
validation_evidence:
context_only:
forbidden_implications:
required_entities:
required_relations:
visible_text:
reviewer_risks:
ai_policy_status:
```

## Claim 强度

### DEMONSTRATED
原文有直接实验/统计/机制验证支持。

视觉：
- 主实线箭头
- 高对比
- 可作为 hero

### SUPPORTED
有间接支持或 rescue/consistent evidence，但不是直接机制证明。

视觉：
- 次级实线/较浅色
- 不用“directly activates”除非真的验证

### ASSOCIATED
只说明差异、相关、共现。

视觉：
- 虚线/关联线
- 文案用 associated with / correlated with
- 不画激活/抑制箭头

### CONTEXT
领域背景或通识，不是本文新发现。

视觉：
- 放边缘
- 低饱和
- 不抢主结论

### FORBIDDEN
摘要/原文没有支持的内容。

绝不画。

## Reviewer Risk

画图前至少问：

- 哪条箭头最可能被审稿人质疑？
- 是否把“表达下降”误画成“某分子直接抑制”？
- rescue 能否证明 direct binding？
- 体外结果是否被夸大成体内机制？
- 动物模型是否被夸大成人体疗效？
- 临床样本差异是否被画成治疗效果？


## SVG delivery contract

Figure Contract 必须额外记录：

```text
Output formats: [svg, png]
SVG mode: vector_native | hybrid_editable | vector_reconstructed
Editable text required: yes
Editable relations required: yes
```

若目标为科研机制图、GA、框架图或技术路线，`svg` 默认不可省略。
