#!/usr/bin/env python3
"""
Regenerate content/issues/issue-NN.yaml from content/source/issues_data.py.

Run this after editing issues_data.py — it is the single source of truth
for story content. The YAML files are what the art/build pipeline actually
reads, so treat them as generated output, not something to hand-edit.

Usage:
    python scripts/export_issue_yaml.py
"""
import os
import sys
import yaml

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "source"))
from issues_data import ISSUES  # noqa: E402

from common import ISSUES_DIR, ensure_dirs  # noqa: E402


def main():
    ensure_dirs(ISSUES_DIR)
    for issue in ISSUES:
        num = issue["number"]
        slug = issue["slug"]
        filename = f"issue-{num:02d}-{slug}.yaml"
        path = os.path.join(ISSUES_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(issue, f, sort_keys=False, allow_unicode=True, width=100)
        print(f"wrote {filename}")
    print(f"\nExported {len(ISSUES)} issues to {ISSUES_DIR}")


if __name__ == "__main__":
    main()
