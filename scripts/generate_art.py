#!/usr/bin/env python3
"""
Generate panel artwork for every issue.

Three backends, chosen with --backend:

  procedural   Draws geometric/silhouette art with Pillow. No API key needed,
               no network call. Fits the Acubi (minimalist) aesthetic on its
               own and can never fail, so it's the hard default.
  pollinations Calls Pollinations.ai's open image endpoint. Free, no signup,
               no API key required on its anonymous tier (rate-limited to
               roughly one request per 15s and may add a small watermark).
               If you later register a free key at auth.pollinations.ai,
               set POLLINATIONS_API_KEY and it's picked up automatically to
               remove both limits. This is the "real AI art for free" option.
  openai       Calls OpenAI's image API (gpt-image-1 / DALL-E). Needs
               OPENAI_API_KEY in the environment. Paid.
  google       Calls Google's image API (Imagen via the Gemini API). Needs
               GOOGLE_API_KEY in the environment. Paid.
  auto         Tries openai, then google, then pollinations (free, no key),
               then procedural. Use this once you want real art without
               worrying about which keys are or aren't set.

Usage:
    python scripts/generate_art.py --backend auto
    python scripts/generate_art.py --backend pollinations --issue 1
    python scripts/generate_art.py --backend procedural --issue 1
"""
import argparse
import base64
import hashlib
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (  # noqa: E402
    GENERATED_ART_DIR,
    load_all_issues,
    load_bible,
    panel_art_filename,
    ensure_dirs,
)

PANEL_SIZE = (1024, 1024)


# --------------------------------------------------------------------------- #
# Backend: procedural (code-drawn, no API key)
# --------------------------------------------------------------------------- #
def draw_procedural(prompt_text, out_path, palette, seed_text):
    """
    Deterministic geometric/silhouette panel art. Same seed_text always
    produces the same image, so re-runs are stable in git diffs.
    """
    from PIL import Image, ImageDraw
    import random

    seed = int(hashlib.sha256(seed_text.encode("utf-8")).hexdigest(), 16) % (2**32)
    rng = random.Random(seed)

    w, h = PANEL_SIZE
    bg = palette.get("background", "#e7e0d3")
    ink = palette.get("ink", "#20201d")
    accents = [
        palette.get("accent_cyan", "#3ad6c9"),
        palette.get("accent_magenta", "#c9427a"),
        palette.get("accent_amber", "#d69a3a"),
    ]
    shadow = palette.get("shadow", "#5a5548")

    img = Image.new("RGB", (w, h), bg)
    draw = ImageDraw.Draw(img)

    # Skyline silhouette band (cyberpunk city motif, minimal)
    horizon = int(h * rng.uniform(0.55, 0.7))
    x = 0
    while x < w:
        bw = rng.randint(40, 140)
        bh = rng.randint(int(h * 0.1), int(h * 0.45))
        draw.rectangle([x, horizon - bh, x + bw, horizon], fill=shadow)
        # occasional lit window strip
        if rng.random() < 0.6:
            wx = x + rng.randint(4, max(5, bw - 10))
            wy = horizon - rng.randint(8, max(9, bh - 8))
            accent = rng.choice(accents)
            draw.rectangle([wx, wy, wx + 6, wy + 14], fill=accent)
        x += bw + rng.randint(4, 14)

    draw.rectangle([0, horizon, w, h], fill=bg)

    # Foreground silhouette shape (stands in for the character/subject)
    cx, cy = w * rng.uniform(0.35, 0.65), horizon + (h - horizon) * 0.5
    torso_w, torso_h = rng.randint(90, 160), rng.randint(220, 320)
    draw.rounded_rectangle(
        [cx - torso_w / 2, cy - torso_h / 2, cx + torso_w / 2, cy + torso_h / 2],
        radius=30,
        fill=ink,
    )
    head_r = rng.randint(34, 50)
    draw.ellipse([cx - head_r, cy - torso_h / 2 - head_r * 1.7,
                  cx + head_r, cy - torso_h / 2 + head_r * 0.3], fill=ink)

    # Accent geometric overlay (Acubi minimalism: a few clean shapes, not clutter)
    accent = rng.choice(accents)
    for _ in range(rng.randint(2, 4)):
        shape = rng.choice(["line", "circle", "tri"])
        if shape == "line":
            y = rng.randint(0, h)
            draw.line([(0, y), (w, y)], fill=accent, width=3)
        elif shape == "circle":
            r = rng.randint(20, 80)
            px, py = rng.randint(0, w), rng.randint(0, horizon)
            draw.ellipse([px - r, py - r, px + r, py + r], outline=accent, width=4)
        else:
            px, py = rng.randint(0, w), rng.randint(0, h)
            s = rng.randint(20, 60)
            draw.polygon([(px, py), (px + s, py), (px + s / 2, py - s)], fill=accent)

    # Caption strip with the prompt text (trimmed) so panels are identifiable
    # even before dialogue/narration is composited on top later.
    strip_h = 60
    draw.rectangle([0, h - strip_h, w, h], fill=ink)
    try:
        from PIL import ImageFont
        font = ImageFont.load_default()
    except Exception:
        font = None
    label = (prompt_text or "")[:90]
    draw.text((16, h - strip_h + 20), label, fill=bg, font=font)

    ensure_dirs(os.path.dirname(out_path))
    img.save(out_path)
    return out_path


# --------------------------------------------------------------------------- #
# Backend: Pollinations.ai (free, no API key on the anonymous tier)
# --------------------------------------------------------------------------- #
POLLINATIONS_MIN_INTERVAL = 16  # seconds; anonymous tier is ~1 request/15s
_last_pollinations_call = [0.0]


def draw_pollinations(prompt_text, out_path, style_suffix, seed_text, max_retries=6):
    """
    Real AI-generated art with no API key required. Uses Pollinations.ai's
    open image endpoint (https://image.pollinations.ai/prompt/...), which
    works anonymously — rate-limited and lightly watermarked on that tier.
    Set POLLINATIONS_API_KEY (free signup at auth.pollinations.ai) to lift
    both restrictions; it's used automatically if present.
    """
    import urllib.request
    import urllib.parse
    import urllib.error

    seed = int(hashlib.sha256(seed_text.encode("utf-8")).hexdigest(), 16) % (2**32)
    full_prompt = f"{prompt_text} {style_suffix}".strip()
    encoded = urllib.parse.quote(full_prompt)
    url = (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width=1024&height=1024&seed={seed}&nologo=true"
    )
    headers = {"User-Agent": "anonymous-heroes-comic-pipeline/1.0"}
    api_key = os.environ.get("POLLINATIONS_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    # Be polite to the anonymous tier's rate limit even across panels.
    elapsed = time.time() - _last_pollinations_call[0]
    if elapsed < POLLINATIONS_MIN_INTERVAL:
        time.sleep(POLLINATIONS_MIN_INTERVAL - elapsed)

    last_err = None
    RETRYABLE = {429, 500, 502, 503, 504}
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = resp.read()
            _last_pollinations_call[0] = time.time()
            ensure_dirs(os.path.dirname(out_path))
            with open(out_path, "wb") as f:
                f.write(data)
            return out_path
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in RETRYABLE and attempt < max_retries - 1:
                # 429 = rate limit, needs the full window; 5xx = transient
                # server error, a short backoff is enough.
                wait = POLLINATIONS_MIN_INTERVAL * (attempt + 1) if e.code == 429 else 5 * (attempt + 1)
                print(f"    [pollinations] HTTP {e.code}, retrying in {wait}s "
                      f"(attempt {attempt + 1}/{max_retries})...", flush=True)
                time.sleep(wait)
                continue
            if e.code in RETRYABLE:
                raise RuntimeError(f"pollinations backend HTTP {e.code} after {max_retries} attempts: {e.reason}")
            raise RuntimeError(f"pollinations backend HTTP {e.code}: {e.reason}")
        except urllib.error.URLError as e:
            last_err = e
            if attempt < max_retries - 1:
                print(f"    [pollinations] connection error, retrying in {3 * (attempt + 1)}s "
                      f"(attempt {attempt + 1}/{max_retries})...", flush=True)
                time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"pollinations backend failed after {max_retries} attempts: {last_err}")


# --------------------------------------------------------------------------- #
# Backend: OpenAI
# --------------------------------------------------------------------------- #
def draw_openai(prompt_text, out_path, style_suffix):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    resp = client.images.generate(
        model="gpt-image-1",
        prompt=f"{prompt_text} {style_suffix}",
        size="1024x1024",
    )
    image_b64 = resp.data[0].b64_json
    ensure_dirs(os.path.dirname(out_path))
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(image_b64))
    return out_path


# --------------------------------------------------------------------------- #
# Backend: Google (Gemini / Imagen)
# --------------------------------------------------------------------------- #
def draw_google(prompt_text, out_path, style_suffix):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set")
    from google import genai

    client = genai.Client(api_key=api_key)
    resp = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=f"{prompt_text} {style_suffix}",
    )
    image_bytes = None
    for part in resp.candidates[0].content.parts:
        if getattr(part, "inline_data", None) is not None:
            image_bytes = part.inline_data.data
            break
    if image_bytes is None:
        raise RuntimeError("google backend returned no image data")
    ensure_dirs(os.path.dirname(out_path))
    with open(out_path, "wb") as f:
        f.write(image_bytes)
    return out_path


# --------------------------------------------------------------------------- #
def style_suffix_from_bible(bible):
    return (
        f"Style: {bible.get('aesthetic', 'minimalist cyberpunk')}. "
        "Comic panel illustration, no text or speech bubbles in the image itself."
    )


def generate_panel(backend, prompt_text, out_path, palette, seed_text, style_suffix):
    if backend == "procedural":
        return draw_procedural(prompt_text, out_path, palette, seed_text)
    if backend == "pollinations":
        return draw_pollinations(prompt_text, out_path, style_suffix, seed_text)
    if backend == "openai":
        return draw_openai(prompt_text, out_path, style_suffix)
    if backend == "google":
        return draw_google(prompt_text, out_path, style_suffix)
    if backend == "auto":
        for b in ("openai", "google", "pollinations"):
            try:
                if b == "openai":
                    return draw_openai(prompt_text, out_path, style_suffix)
                if b == "google":
                    return draw_google(prompt_text, out_path, style_suffix)
                return draw_pollinations(prompt_text, out_path, style_suffix, seed_text)
            except Exception as e:  # noqa: BLE001
                print(f"  [auto] {b} backend unavailable ({e}); trying next...", flush=True)
        return draw_procedural(prompt_text, out_path, palette, seed_text)
    raise ValueError(f"Unknown backend: {backend}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend",
                         choices=["procedural", "pollinations", "openai", "google", "auto"],
                         default="procedural")
    parser.add_argument("--issue", type=int, default=None,
                         help="Only generate art for this issue number.")
    parser.add_argument("--force", action="store_true",
                         help="Regenerate even if the art file already exists.")
    args = parser.parse_args()

    bible = load_bible()
    palette = bible.get("palette", {})
    style_suffix = style_suffix_from_bible(bible)
    issues = load_all_issues()
    ensure_dirs(GENERATED_ART_DIR)

    total, made = 0, 0
    panel_count = sum(
        len(page["panels"])
        for issue in issues
        for page in issue["pages"]
        if not args.issue or issue["number"] == args.issue
    )
    if args.backend in ("pollinations", "auto"):
        est_minutes = round(panel_count * POLLINATIONS_MIN_INTERVAL / 60, 1)
        print(f"Backend '{args.backend}': up to {panel_count} panels. If falling back to the "
              f"free Pollinations tier, that's rate-limited to ~1 panel/{POLLINATIONS_MIN_INTERVAL}s "
              f"— roughly {est_minutes} min worst case. Progress prints below as each panel finishes; "
              f"no output for ~{POLLINATIONS_MIN_INTERVAL}s between panels is normal, not a hang.",
              flush=True)

    for issue in issues:
        if args.issue and issue["number"] != args.issue:
            continue
        for page in issue["pages"]:
            for panel in page["panels"]:
                total += 1
                fname = panel_art_filename(issue["slug"], page["page"], panel["id"])
                out_path = os.path.join(GENERATED_ART_DIR, fname)
                if os.path.exists(out_path) and not args.force:
                    continue
                prompt_text = panel.get("image_prompt") or panel["description"]
                seed_text = f"{issue['slug']}-{page['page']}-{panel['id']}-{prompt_text}"
                print(f"[{made + 1}] Generating {fname} via {args.backend}...", flush=True)
                generate_panel(args.backend, prompt_text, out_path, palette, seed_text, style_suffix)
                made += 1
                print("    done.", flush=True)

    print(f"\nDone. {made}/{total} panels generated (others already existed; use --force to redo).",
          flush=True)


if __name__ == "__main__":
    main()
