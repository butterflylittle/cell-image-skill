# Changelog

## 2.4.0 — cell-image rename + Figure Intake

- Skill renamed from `scientific-figure-generator` to `cell-image`.
- Added `Figure Intake Gate`: infer first, ask only high-impact unknowns.
- Added `schemas/figure-intake.schema.json` and `scripts/validate_intake.py`.
- Added purpose-driven defaults for aspect ratio, style, palette, density and title policy.
- Added partial-update rule: when the user changes one token such as palette, do not re-ask all settings.
- Added `schemas/text-manifest.schema.json` and `references/editable-reconstruction.md` for approved raster → editable Master SVG.
- Retains v2.3 SVG Fidelity Contract: composition freeze, anchor map, no re-layout, no full-canvas raster wrapper as final editable SVG.

## 2.3.0

- Added SVG Fidelity Contract and layout-fidelity audit guidance.
