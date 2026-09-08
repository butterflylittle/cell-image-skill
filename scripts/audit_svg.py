#!/usr/bin/env python3
"""Audit whether an SVG is a genuinely editable scientific-figure deliverable.

This is intentionally conservative. It detects common fake-SVG wrappers and
reports the presence of editable text/vector geometry versus embedded rasters.
"""
from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SVG_NS = "http://www.w3.org/2000/svg"


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("svg", help="SVG file to audit")
    ap.add_argument(
        "--mode",
        choices=["vector_native", "hybrid_editable", "vector_reconstructed"],
        default=None,
        help="Expected SVG delivery mode",
    )
    args = ap.parse_args()

    path = Path(args.svg)
    if not path.exists():
        print("FAIL\n- file not found")
        return 1

    try:
        root = ET.parse(path).getroot()
    except Exception as e:
        print(f"FAIL\n- invalid XML/SVG: {e}")
        return 1

    errors: list[str] = []
    warns: list[str] = []

    if local(root.tag) != "svg":
        errors.append("root element is not <svg>")

    viewbox = root.attrib.get("viewBox")
    width = root.attrib.get("width")
    height = root.attrib.get("height")
    if not viewbox:
        errors.append("missing viewBox")
    if not width or not height:
        errors.append("missing explicit width/height")

    counts = {
        "text": 0,
        "path": 0,
        "line": 0,
        "polyline": 0,
        "polygon": 0,
        "rect": 0,
        "circle": 0,
        "ellipse": 0,
        "image": 0,
        "g": 0,
    }

    images = []
    for el in root.iter():
        name = local(el.tag)
        if name in counts:
            counts[name] += 1
        if name == "image":
            images.append(el)

    vector_geometry = sum(counts[k] for k in ["path", "line", "polyline", "polygon", "rect", "circle", "ellipse"])

    # A single raster with essentially no vector/text content is almost always a fake SVG wrapper.
    if counts["image"] == 1 and vector_geometry == 0 and counts["text"] == 0:
        errors.append("single embedded raster with no editable vector/text content: raster-wrapped SVG")

    if args.mode in {"vector_native", "vector_reconstructed"} and counts["image"] > 0:
        warns.append(f"{args.mode} contains {counts['image']} embedded raster image(s); review whether they are necessary")

    if args.mode == "vector_native" and vector_geometry == 0:
        errors.append("vector_native mode contains no vector geometry")

    if args.mode == "hybrid_editable":
        if counts["image"] == 0:
            warns.append("hybrid_editable contains no embedded raster assets; this may actually be vector_native")
        if vector_geometry == 0:
            errors.append("hybrid_editable has no editable vector geometry")

    if counts["text"] == 0:
        warns.append("no editable <text> elements detected; acceptable only for genuinely text-free figures")

    print("SVG AUDIT")
    print(f"file: {path}")
    print(f"viewBox: {viewbox}")
    print(f"size: {width} × {height}")
    print("objects: " + ", ".join(f"{k}={v}" for k, v in counts.items()))

    if warns:
        print("WARN")
        for w in warns:
            print("-", w)

    if errors:
        print("FAIL")
        for e in errors:
            print("-", e)
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
