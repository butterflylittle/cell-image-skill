# SVG Fidelity Contract

Use this whenever an approved raster draft, reference layout, or user-confirmed composition must become SVG.

## 1. Composition freeze

Treat the approved image as a frozen composition, not a loose inspiration. Preserve:

- canvas aspect ratio and outer margins
- hero element position and visual weight
- major-object bounding boxes and relative scale
- reading order and causal arrow topology
- label anchor positions
- semantic color roles
- whitespace rhythm and visual hierarchy

Do not add section headers, new legends, or alternative layouts unless the user explicitly requests redesign.

## 2. Anchor map

Before reconstruction, create an internal anchor map using normalized canvas coordinates (0..1):

```json
{
  "canvas": {"w": 1672, "h": 941},
  "anchors": [
    {"id":"hero_cell","bbox":[0.05,0.19,0.84,0.59]},
    {"id":"nanoparticle","center":[0.53,0.13],"size":[0.10,0.17]},
    {"id":"checkpoint","bbox":[0.18,0.62,0.40,0.80]}
  ]
}
```

Use the anchor map to drive SVG reconstruction.

## 3. Delivery modes

### vector_native
All meaningful shapes, text, arrows and scientific objects are vectors. Best for frameworks, technical routes and CS diagrams.

### hybrid_editable
Allowed for complex biomedical art. Complex cell/tissue/organelle art may be local raster assets, but:

- never use one full-canvas raster as the whole figure
- editable SVG text is required
- editable arrows/relations are required
- editable inhibition/activation symbols are required
- local raster assets must be cropped to their object/region and grouped semantically

### vector_reconstructed
Rebuild the approved visual as editable vector artwork. Scientific fidelity outranks exact decorative texture.

## 4. Hard failures

Fail delivery if any is true:

- one full-canvas `<image>` carries essentially the whole figure
- hero mechanism was simplified away
- major objects were moved into a new layout without approval
- large arrows dominate where they were subordinate in the approved raster
- biological objects were replaced by generic circles/rectangles solely to make SVG easier
- label wording, direction, or causal relation changed
- the SVG preview differs materially in reading order or hierarchy

## 5. Fidelity QA checklist

Compare the rendered SVG at the same canvas ratio against the approved raster:

1. hero region position and area
2. top-level zone heights/widths
3. object count and major-object bounding boxes
4. arrow direction and branching topology
5. label anchors and line crossings
6. semantic colors
7. visual dominance: hero > mechanism support > validation > decoration
8. final-size readability

Recommended tolerances:

- major bbox center shift <= 5% of canvas
- major bbox size drift <= 10%
- hero-area drift <= 8%
- label-anchor drift <= 4% of canvas
- arrow topology and reading order: exact

When these cannot be met with full vector reconstruction, use hybrid_editable rather than redesigning the figure.
