# Source Notes & Attribution

本 Skill 的文字、路由与实现为重新组织和原创实现。

## GitHub 架构启发

### Yuan1z0825/nature-skills
项目：
https://github.com/Yuan1z0825/nature-skills

学习点：
- claim-first / figure contract
- evidence hierarchy
- journal QA
- plotting / AI schematic 分路由
- final-size QA

该项目标注 Apache-2.0；本 Skill 未复制其大段原文。

### BAIKEMARK/happy-figure-skill
项目：
https://github.com/BAIKEMARK/happy-figure-skill

学习点：
- domain master × figure type
- Visual Schema
- exact visible text whitelist
- reference style patch
- 三层语言策略

该仓库 LICENSE 标注 CC BY-NC-SA 4.0。
本 Skill 不复制其长提示词母版，仅吸收抽象设计思想并重新实现。

## 官方出版规范

- Nature Research Figure Guide
  https://research-figure-guide.nature.com/
- The Lancet artwork guidelines
  https://www.lancet.com/pb/assets/raw/Lancet/authors/artwork-guidelines.pdf
- Cell Press graphical abstract guidance
  https://crosstalk.cell.com/hubfs/Files/GA_guide.pdf
- Elsevier artwork instructions
  https://www.elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions
- Elsevier generative AI policies
  https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Nature Portfolio AI policy
  https://www.nature.com/nature-portfolio/editorial-policies/ai

## 注意
规范会更新。本 Skill 内的数字只作为 2026-09-07 核验时的默认 profile；
真正投稿必须重新核对目标期刊官方页面。


## 用户提供的视觉参考

Skill 还吸收了用户提供的多类医学示意图作为**构图研究样本**，包括：
- 解剖→微结构交换界面
- 细胞中心型离子泵/转运机制
- 制备→体外→体内验证
- 横向因果机制
- 闭环治疗与教学型机制图

仅抽取布局、比例、颜色、箭头、文字密度和放大关系，不在 Skill 中分发或复制原始第三方图片。

## v2.3 local synthesis note
The SVG fidelity contract was added after comparing a high-fidelity biomedical raster draft with a separately redrawn SVG that preserved semantics but lost composition, biological detail, and visual hierarchy. The rule therefore treats approved raster composition as frozen and requires anchor-based reconstruction rather than semantic re-layout.
