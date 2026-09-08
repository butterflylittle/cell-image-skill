#!/usr/bin/env python3
import argparse, json
from pathlib import Path

REQUIRED = [
    "core_conclusion", "artifact_purpose", "domain", "figure_type",
    "reading_order", "zones", "entities", "relations",
    "visible_text", "forbidden_content", "output_formats", "svg_mode",
    "layout_profile", "density_level", "design_tokens"
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    args = ap.parse_args()
    data = json.loads(Path(args.spec).read_text(encoding="utf-8"))

    errors = [f"missing: {k}" for k in REQUIRED if k not in data]

    labels = data.get("visible_text", [])
    if len(labels) != len(set(labels)):
        errors.append("visible_text contains duplicates")

    formats = data.get("output_formats", [])
    if "svg" not in formats:
        errors.append("output_formats must include svg")
    if "png" not in formats:
        errors.append("output_formats should include png preview")
    if data.get("svg_mode") not in {"vector_native", "hybrid_editable", "vector_reconstructed"}:
        errors.append("invalid svg_mode")


    if data.get("density_level") not in {"D1","D2","D3","D4"}:
        errors.append("invalid density_level")

    dt = data.get("design_tokens", {})
    if dt:
        if not (0 <= dt.get("outer_margin_pct", -1) <= 12):
            errors.append("design_tokens.outer_margin_pct must be 0..12")
        if not (30 <= dt.get("hero_area_pct", -1) <= 85):
            errors.append("design_tokens.hero_area_pct must be 30..85")
        if dt.get("main_hues", 99) > 7:
            errors.append("design_tokens.main_hues must be <= 7")
        if dt.get("high_saturation_accents", 99) > 3:
            errors.append("design_tokens.high_saturation_accents must be <= 3")
        if dt.get("panel_tints", 99) > 4:
            errors.append("design_tokens.panel_tints must be <= 4")

    if data.get("domain") == "biomedical":
        if dt.get("main_hues", 0) > 5:
            errors.append("biomedical default: main_hues should be <= 5")
        if dt.get("high_saturation_accents", 0) > 2:
            errors.append("biomedical default: high_saturation_accents should be <= 2")

    ids = {e.get("id") for e in data.get("entities", [])}
    for r in data.get("relations", []):
        if r.get("source") not in ids:
            errors.append(f"relation source not found: {r.get('source')}")
        if r.get("target") not in ids:
            errors.append(f"relation target not found: {r.get('target')}")
        if r.get("relation") in {"activates","inhibits","drives","binds"} and r.get("evidence") == "ASSOCIATED":
            errors.append(f"causal relation uses ASSOCIATED evidence: {r}")

    if errors:
        print("FAIL")
        for e in errors:
            print("-", e)
        return 1
    print("PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
