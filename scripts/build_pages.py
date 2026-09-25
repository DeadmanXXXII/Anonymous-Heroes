#!/usr/bin/env python3
"""
Compose generated panel art + dialogue/narration into finished comic page
images (one PNG per page, panels arranged in a grid).

Usage:
    python scripts/build_pages.py
    python scripts/build_pages.py --issue 1
"""
import argparse
import math
import os
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (  # noqa: E402
    GENERATED_ART_DIR,
    OUTPUT_DIR,
    load_all_issues,
    load_bible,
    panel_art_filename,
    ensure_dirs,
)

PAGE_MARGIN = 24
PANEL_GAP = 16
CAPTION_BOX_H = 90


def load_font(size, bold=False):
    # Falls back to Pillow's built-in bitmap font if no TTF is bundled;
    # drop a real font into assets/fonts/ for production-quality output.
    candidates = [
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     "assets", "fonts", "Inter-Bold.ttf" if bold else "Inter-Regular.ttf"),
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def grid_dims(n_panels):
    cols = 2 if n_panels > 1 else 1
    rows = math.ceil(n_panels / cols)
    return cols, rows


def compose_page(issue, page, art_dir, palette):
    panels = page["panels"]
    cols, rows = grid_dims(len(panels))
    panel_w, panel_h = 700, 700

    page_w = PAGE_MARGIN * 2 + cols * panel_w + (cols - 1) * PANEL_GAP
    page_h = PAGE_MARGIN * 2 + rows * (panel_h + CAPTION_BOX_H) + (rows - 1) * PANEL_GAP

    bg = palette.get("background", "#e7e0d3")
    ink = palette.get("ink", "#20201d")

    canvas = Image.new("RGB", (page_w, page_h), bg)
    draw = ImageDraw.Draw(canvas)
    font_body = load_font(20)
    font_caption = load_font(18)

    for idx, panel in enumerate(panels):
        col, row = idx % cols, idx // cols
        x = PAGE_MARGIN + col * (panel_w + PANEL_GAP)
        y = PAGE_MARGIN + row * (panel_h + CAPTION_BOX_H + PANEL_GAP)

        art_path = os.path.join(art_dir, panel_art_filename(issue["slug"], page["page"], panel["id"]))
        if os.path.exists(art_path):
            art = Image.open(art_path).convert("RGB").resize((panel_w, panel_h))
        else:
            art = Image.new("RGB", (panel_w, panel_h), "#cccccc")
        canvas.paste(art, (x, y))
        draw.rectangle([x, y, x + panel_w, y + panel_h], outline=ink, width=3)

        # Caption/dialogue box under the panel
        cap_y = y + panel_h + 6
        lines = []
        if panel.get("narration"):
            lines.append(f"NARR: {panel['narration']}")
        for d in panel.get("dialogue", []) or []:
            lines.append(f"{d['speaker']}: \u201c{d['line']}\u201d")
        text = "  |  ".join(lines) if lines else ""
        wrapped = textwrap.wrap(text, width=70)[:3]
        ty = cap_y
        for line in wrapped:
            draw.text((x + 6, ty), line, fill=ink, font=font_caption)
            ty += 22

    # Page footer
    footer = f"{issue['title']} - Issue {issue['number']:02d}  |  Page {page['page']}"
    draw.text((PAGE_MARGIN, page_h - 20), footer, fill=ink, font=font_body)

    return canvas


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue", type=int, default=None)
    args = parser.parse_args()

    bible = load_bible()
    palette = bible.get("palette", {})
    issues = load_all_issues()

    for issue in issues:
        if args.issue and issue["number"] != args.issue:
            continue
        out_dir = os.path.join(OUTPUT_DIR, "pages", f"issue-{issue['number']:02d}-{issue['slug']}")
        ensure_dirs(out_dir)
        for page in issue["pages"]:
            img = compose_page(issue, page, GENERATED_ART_DIR, palette)
            out_path = os.path.join(out_dir, f"page-{page['page']:02d}.png")
            img.save(out_path)
            print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
