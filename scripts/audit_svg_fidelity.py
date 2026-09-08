#!/usr/bin/env python3
"""Render an SVG and compare it with an approved raster at coarse visual scale.

This is a screening check only. Human visual QA and Anchor Map review remain required.
"""
from __future__ import annotations
import argparse, shutil, subprocess, tempfile
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageStat
except Exception:
    Image = None


def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('svg')
    ap.add_argument('reference')
    ap.add_argument('--threshold',type=float,default=0.22,help='max normalized coarse RGB mean absolute error')
    args=ap.parse_args()
    if Image is None:
        print('NOT AUDITABLE\n- Pillow is not installed')
        return 2
    if not shutil.which('inkscape'):
        print('NOT AUDITABLE\n- inkscape is not installed')
        return 2
    svg=Path(args.svg); ref=Path(args.reference)
    if not svg.exists() or not ref.exists():
        print('FAIL\n- input file missing')
        return 1
    with tempfile.TemporaryDirectory() as td:
        out=Path(td)/'render.png'
        subprocess.run(['inkscape',str(svg),'--export-type=png',f'--export-filename={out}'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        a=Image.open(out).convert('RGB').resize((160,90))
        b=Image.open(ref).convert('RGB').resize((160,90))
        diff=ImageChops.difference(a,b)
        mean=sum(ImageStat.Stat(diff).mean)/(3*255.0)
        print(f'coarse_rgb_mae={mean:.4f}')
        if mean > args.threshold:
            print('REVIEW REQUIRED\n- coarse visual difference exceeds threshold; inspect Anchor Map, hero area, arrows and labels')
            return 1
        print('PASS (screening only)')
        return 0

if __name__=='__main__':
    raise SystemExit(main())
