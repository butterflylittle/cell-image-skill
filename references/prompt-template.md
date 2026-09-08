# Prompt Template

以下为 image-assisted / AI schematic 的推荐模板。

```text
ROLE
You are a scientific illustrator creating a concept draft for [artifact purpose].

SCIENTIFIC MESSAGE
[one-sentence claim]

FIGURE TYPE
[mechanism / graphical abstract / closed loop / multiscale zoom]

LAYOUT PROFILE
[biomed_landscape_16x9 / biomed_portrait_a4 / biomed_split_validation / biomed_multiscale_zoom / custom]

INFORMATION DENSITY
[D1 / D2 / D3 / D4]

READING ORDER
[left-to-right / top-to-bottom / clockwise]

HERO ELEMENT
[the one causal step that must dominate]

REQUIRED ENTITIES
- ...
- ...

REQUIRED RELATIONSHIPS
1. A activates B
2. C inhibits D
3. E is transported to F

EVIDENCE BOUNDARY
- Demonstrated: ...
- Supported: ...
- Association only: ...
- Context only: ...
- Do not imply: ...

LAYOUT
ZONE 1 ...
ZONE 2 ...
ZONE 3 ...

ARROW GRAMMAR
- solid arrow = activation/progression
- blunt bar = inhibition
- dashed arrow = transport/secretion
- thin dashed line = association only

COLOR SEMANTICS
- neutral/context = ...
- disease/inhibition = ...
- activation/rescue = ...
- hero signal = ...
- main hues <= 5 for biomedical defaults
- high-saturation accents <= 2
- panel tints <= 3 and very pale

PROPORTION BUDGET
- outer margin = ...%
- hero mechanism = ...% of total area
- support/validation = ...% of total area
- title = none / compact / educational
- breathing space = ...%

JOURNAL CONSTRAINTS
[target profile summary]

EXACT VISIBLE TEXT
All visible text in the figure must use only the following exact labels:
1. "..."
2. "..."
Do not render any other text.

FORBIDDEN CONTENT
- no invented data
- no fake microscopy/histology
- no unsupported pathway
- no journal logo
- no random decorative molecules
- no structural prompt words such as ZONE or LAYOUT

OUTPUT
[16:9 / square / final target size]
white background
publication-style scientific schematic
[concept draft / submission candidate]
Generate/design for downstream SVG reconstruction. The authoritative final deliverable must be SVG + PNG.
SVG mode: [vector_native / hybrid_editable / vector_reconstructed].
All labels, arrows, inhibition bars, relation lines, and annotations must remain separately editable in the SVG.
Do not satisfy the SVG requirement by embedding one full-canvas raster image inside an SVG wrapper.
```

## 关键原则

Prompt 写的是“物理构图 + 科学关系”，不是堆形容词。

坏：
> premium, beautiful, stunning, top journal style

好：
> central HOK cell occupies 45% of canvas; VDR-promoter binding is the focal event; clinical-sample evidence is a low-contrast supporting strip at lower left.
