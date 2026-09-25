"""Shared paths, config loading, and small utilities for the comic pipeline."""
import os
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(ROOT, "content")
ISSUES_DIR = os.path.join(CONTENT_DIR, "issues")
BIBLE_PATH = os.path.join(CONTENT_DIR, "series-bible.yaml")
ASSETS_DIR = os.path.join(ROOT, "assets")
GENERATED_ART_DIR = os.path.join(ASSETS_DIR, "generated")
OUTPUT_DIR = os.path.join(ROOT, "output")
OUTPUT_HTML_DIR = os.path.join(OUTPUT_DIR, "html")
OUTPUT_PDF_DIR = os.path.join(OUTPUT_DIR, "pdf")


def load_bible():
    with open(BIBLE_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_issue(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def all_issue_paths():
    files = sorted(
        f for f in os.listdir(ISSUES_DIR) if f.startswith("issue-") and f.endswith(".yaml")
    )
    return [os.path.join(ISSUES_DIR, f) for f in files]


def load_all_issues():
    return [load_issue(p) for p in all_issue_paths()]


def panel_art_filename(issue_slug, page_num, panel_id):
    return f"{issue_slug}_p{page_num:02d}_panel{panel_id:02d}.png"


def ensure_dirs(*dirs):
    for d in dirs:
        os.makedirs(d, exist_ok=True)
