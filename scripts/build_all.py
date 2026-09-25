#!/usr/bin/env python3
"""
Run the full pipeline: art generation -> page composition -> HTML -> PDF.

Usage:
    python scripts/build_all.py --backend auto
    python scripts/build_all.py --backend procedural --issue 1
"""
import argparse
import subprocess
import sys

HERE = sys.path[0] or "."


def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend",
                         choices=["procedural", "pollinations", "openai", "google", "auto"],
                         default="procedural")
    parser.add_argument("--issue", type=int, default=None)
    args = parser.parse_args()

    art_cmd = [sys.executable, f"{HERE}/generate_art.py", "--backend", args.backend]
    pages_cmd = [sys.executable, f"{HERE}/build_pages.py"]
    if args.issue:
        art_cmd += ["--issue", str(args.issue)]
        pages_cmd += ["--issue", str(args.issue)]

    run(art_cmd)
    run(pages_cmd)
    run([sys.executable, f"{HERE}/render_html.py"])
    run([sys.executable, f"{HERE}/render_pdf.py"])

    print("\nBuild complete. See output/html/ and output/pdf/.")


if __name__ == "__main__":
    main()
