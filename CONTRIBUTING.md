# Contributing to Cell Image

感谢你帮助改进 Cell Image。这个项目接受文档、schema、validator、journal/layout profile、领域规则和可复现实例等贡献。

## Before opening a change

1. 先搜索现有 issue，避免重复工作；较大的行为变更建议先开 issue 说明目标和证据来源。
2. 不要提交受版权限制的论文图片、期刊插图、品牌素材或未经授权的数据。
3. 不要把生成式显微图、病理图、WB、医学影像或其他合成内容描述为真实实验结果。
4. 涉及期刊规范或 AI artwork policy 时，优先引用官方来源，并记录查阅日期。

## Development principles

- **Scientific correctness first**：不得把 `ASSOCIATED` 关系升级为因果关系。
- **Structured before rendered**：优先更新 Figure Contract / Visual Schema，再调整渲染提示。
- **Editable by default**：正式机制图应保留可编辑文字、箭头和关键关系。
- **Small, reviewable changes**：一个 PR 聚焦一个问题，并解释行为变化。
- **No fake SVGs**：整张 PNG 包进 `<svg><image>` 不算可编辑交付。

## Local checks

```bash
python3 scripts/validate_intake.py examples/figure-intake.biomedical.json
python3 scripts/validate_spec.py examples/closed-loop.visual-schema.json
```

如果改动 SVG 工作流，请额外运行：

```bash
python3 scripts/audit_svg.py path/to/figure.svg --mode hybrid_editable
python3 scripts/audit_svg_fidelity.py path/to/figure.svg path/to/reference.png
```

后一个命令需要 Pillow 和 Inkscape；它只做粗粒度筛查，仍需人工视觉与科学 QA。

## Pull request checklist

- [ ] 变更目标和使用场景写清楚了。
- [ ] 新增或修改的结构化示例可以通过对应 validator。
- [ ] 可见文字、实体 ID 与关系引用保持一致。
- [ ] 因果关系有足够证据支持，没有越过原始材料。
- [ ] 新增外部规则包含来源与查阅日期。
- [ ] 新增图片和数据拥有可再分发许可，并说明其性质（真实数据、示意图或 AI 辅助草图）。
- [ ] 文档和 `CHANGELOG.md` 已在需要时同步更新。

提交 PR 即表示你同意按本项目的 Apache-2.0 许可证授权你的贡献。

