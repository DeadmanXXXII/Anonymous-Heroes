#!/usr/bin/env python3
"""
Compile composed page images into PDFs: one per issue, plus one combined
full-series PDF.

Usage:
    python scripts/render_pdf.py
"""
import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUTPUT_DIR, OUTPUT_PDF_DIR, load_all_issues, ensure_dirs  # noqa: E402


def issue_page_images(issue):
    slug = f"issue-{issue['number']:02d}-{issue['slug']}"
    src_dir = os.path.join(OUTPUT_DIR, "pages", slug)
    if not os.path.isdir(src_dir):
        return []
    return [
        Image.open(os.path.join(src_dir, f)).convert("RGB")
        for f in sorted(os.listdir(src_dir))
    ]


def main():
    issues = load_all_issues()
    ensure_dirs(OUTPUT_PDF_DIR)

    all_pages = []
    for issue in issues:
        imgs = issue_page_images(issue)
        if not imgs:
            print(f"skip issue {issue['number']} (no composed pages found — run build_pages.py first)")
            continue
        slug = f"issue-{issue['number']:02d}-{issue['slug']}"
        out_path = os.path.join(OUTPUT_PDF_DIR, f"{slug}.pdf")
        imgs[0].save(out_path, save_all=True, append_images=imgs[1:])
        print(f"wrote {out_path}")
        all_pages.extend(imgs)

    if all_pages:
        combined_path = os.path.join(OUTPUT_PDF_DIR, "anonymous-heroes-full-series.pdf")
        all_pages[0].save(combined_path, save_all=True, append_images=all_pages[1:])
        print(f"wrote {combined_path}")


if __name__ == "__main__":
    main()
