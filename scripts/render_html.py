#!/usr/bin/env python3
"""
Build the static HTML site: one index page + one page per issue,
linking the composed page images from output/pages/.

Usage:
    python scripts/render_html.py
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUTPUT_DIR, OUTPUT_HTML_DIR, load_all_issues, load_bible, ensure_dirs  # noqa: E402

CSS_TEMPLATE = """
:root {
  --bg: __background__; --ink: __ink__; --cyan: __accent_cyan__;
  --magenta: __accent_magenta__; --amber: __accent_amber__;
}
* { box-sizing: border-box; }
body {
  background: var(--bg); color: var(--ink); font-family: 'Inter', sans-serif;
  margin: 0; padding: 0 0 60px;
}
header {
  padding: 40px 20px; text-align: center; border-bottom: 4px solid var(--ink);
}
header h1 { font-size: 3rem; letter-spacing: 0.05em; margin: 0; }
header p { opacity: 0.75; margin-top: 8px; }
nav.issue-list {
  max-width: 900px; margin: 30px auto; display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px; padding: 0 20px;
}
nav.issue-list a {
  display: block; padding: 18px; border: 2px solid var(--ink); border-radius: 8px;
  text-decoration: none; color: var(--ink); transition: transform 0.15s ease;
}
nav.issue-list a:hover { transform: translateY(-3px); border-color: var(--cyan); }
nav.issue-list .act-tag {
  font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.6;
}
nav.issue-list .issue-title { font-size: 1.2rem; font-weight: 700; margin-top: 4px; }
main.issue-pages { max-width: 900px; margin: 0 auto; padding: 20px; }
main.issue-pages img { width: 100%; display: block; margin-bottom: 30px; border: 2px solid var(--ink); }
a.back { display: inline-block; margin: 20px; color: var(--ink); }
"""


def render_css(palette):
    css = CSS_TEMPLATE
    for key in ("background", "ink", "accent_cyan", "accent_magenta", "accent_amber"):
        css = css.replace(f"__{key}__", palette.get(key, "#000000"))
    return css

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><style>{css}</style></head><body>
<header><h1>{title}</h1><p>{genre} &middot; {aesthetic}</p></header>
<nav class="issue-list">{issue_links}</nav>
</body></html>
"""

ISSUE_TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} \u2014 {series_title}</title><style>{css}</style></head><body>
<a class="back" href="index.html">&larr; All issues</a>
<header><h1>{title}</h1><p>Issue {number:02d} &middot; Act {act}</p></header>
<main class="issue-pages">{page_imgs}</main>
</body></html>
"""


def main():
    bible = load_bible()
    palette = bible.get("palette", {})
    issues = load_all_issues()
    ensure_dirs(OUTPUT_HTML_DIR, os.path.join(OUTPUT_HTML_DIR, "pages"))

    css = render_css(palette)

    issue_links = []
    for issue in issues:
        slug = f"issue-{issue['number']:02d}-{issue['slug']}"
        issue_links.append(
            f'<a href="{slug}.html"><div class="act-tag">Act {issue["act"]} &middot; '
            f'Issue {issue["number"]:02d}</div><div class="issue-title">{issue["title"]}</div></a>'
        )

        src_dir = os.path.join(OUTPUT_DIR, "pages", slug)
        dst_dir = os.path.join(OUTPUT_HTML_DIR, "pages", slug)
        ensure_dirs(dst_dir)
        page_imgs = []
        if os.path.isdir(src_dir):
            for fname in sorted(os.listdir(src_dir)):
                shutil.copy(os.path.join(src_dir, fname), os.path.join(dst_dir, fname))
                page_imgs.append(f'<img src="pages/{slug}/{fname}" alt="{issue["title"]} {fname}">')

        issue_html = ISSUE_TEMPLATE.format(
            title=issue["title"], series_title=bible["title"], css=css,
            number=issue["number"], act=issue["act"], page_imgs="\n".join(page_imgs),
        )
        with open(os.path.join(OUTPUT_HTML_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(issue_html)

    index_html = INDEX_TEMPLATE.format(
        title=bible["title"], genre=bible["genre"], aesthetic=bible["aesthetic"],
        css=css, issue_links="\n".join(issue_links),
    )
    with open(os.path.join(OUTPUT_HTML_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    print(f"HTML site written to {OUTPUT_HTML_DIR}")


if __name__ == "__main__":
    main()
