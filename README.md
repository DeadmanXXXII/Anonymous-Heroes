# Anonymous Heroes — Comic Build Pipeline

A cyberpunk comic series, written as structured data and rendered into a
web comic (HTML) and downloadable PDFs, fully automated through GitHub
Actions.

## How it fits together

```
content/source/issues_data.py   <- EDIT STORY HERE (Python source of truth)
        |  (scripts/export_issue_yaml.py)
        v
content/issues/issue-NN-*.yaml  <- generated, don't hand-edit
        |  (scripts/generate_art.py)
        v
assets/generated/*.png          <- panel art (procedural, OpenAI, or Google)
        |  (scripts/build_pages.py)
        v
output/pages/issue-NN/*.png     <- composed comic pages (art + dialogue)
        |  (scripts/render_html.py + scripts/render_pdf.py)
        v
output/html/   output/pdf/      <- the finished web comic + PDFs
```

## Getting this into a repo from Codespaces

1. Unzip this into an empty (or existing) repo folder.
2. In a Codespaces terminal:
   ```bash
   python scripts/export_issue_yaml.py   # generate content/issues/*.yaml from source
   pip install -r requirements.txt
   git add .
   git commit -m "Add Anonymous Heroes comic build pipeline"
   git push
   ```
3. From there, either build locally (`python scripts/build_all.py --backend pollinations`)
   or trigger the **Build & Release Comic** workflow from the Actions tab.

## Editing the story

Don't hand-edit the YAML files in `content/issues/` — they're generated.
Edit `content/source/issues_data.py` (plain Python data), then run:

```bash
python scripts/export_issue_yaml.py
```

## Running the pipeline locally

```bash
pip install -r requirements.txt

# Fastest, zero network — geometric/silhouette placeholder art:
python scripts/build_all.py --backend procedural

# Real AI art, completely free, no signup, no key:
python scripts/build_all.py --backend pollinations

# Once you have paid keys set as environment variables too:
export OPENAI_API_KEY=...
export GOOGLE_API_KEY=...
python scripts/build_all.py --backend auto   # tries OpenAI, then Google, then Pollinations, then procedural

# Just one issue while you're iterating:
python scripts/build_all.py --backend pollinations --issue 1
```

Output lands in `output/html/` (open `index.html`) and `output/pdf/`.

## Publishing via GitHub Pages

The workflow already deploys `output/html/` to GitHub Pages on every run
(toggle it off per-run with the `deploy_pages` input if you just want a
release build). One-time setup:

1. Repo **Settings → Pages → Source** → set to **GitHub Actions**.
2. Run the workflow by hand from the **Actions** tab, or push a `v*.*.*` tag.
3. The `deploy-pages` job prints the live URL when it finishes (also shown
   under **Settings → Pages** and in the repo's "Environments" tab).

Every successful run redeploys the site, so the Pages URL always reflects
the most recent build/backend you ran the workflow with.

## Publishing via GitHub Releases

1. Push this repo to GitHub.
2. Nothing required for free AI art — the `pollinations` backend needs no
   secret. If you want the paid OpenAI/Google backends too, add repo
   secrets: **Settings → Secrets and variables → Actions**
   - `OPENAI_API_KEY` (optional, paid)
   - `GOOGLE_API_KEY` (optional, paid)
   - `POLLINATIONS_API_KEY` (optional, free — lifts the anonymous tier's
     rate limit/watermark; get one at auth.pollinations.ai)
3. Run the workflow by hand any time from the **Actions** tab
   (`Build & Release Comic` → *Run workflow*), choosing a backend and
   optionally a single issue number.
4. To cut an official release with the HTML site + PDFs attached, push a
   version tag:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
   The workflow builds everything and attaches `anonymous-heroes-html-site.zip`
   plus every issue's PDF (and the combined full-series PDF) to the GitHub
   Release automatically.
5. To host the web comic as a live blog rather than a release download,
   point GitHub Pages at `output/html/` — already wired up above; this
   step is a no-op now.

## Art backends

| Backend        | Needs a key? | Notes |
|-----------------|--------------|-------|
| `procedural`    | No, no network | Deterministic geometric/silhouette art drawn with Pillow. Matches the Acubi minimalist brief directly and can never fail — the safety-net default. |
| `pollinations`  | No (free anonymous tier) | Real AI-generated art via Pollinations.ai's open image endpoint. No signup required; the anonymous tier is rate-limited (~1 request/15s) and may add a small watermark. Register free at auth.pollinations.ai and set `POLLINATIONS_API_KEY` as a repo secret to lift both. |
| `openai`        | `OPENAI_API_KEY` (paid) | Calls `gpt-image-1`. |
| `google`        | `GOOGLE_API_KEY` (paid) | Calls Imagen via the Gemini API. |
| `auto`          | None required | Tries OpenAI, then Google, then Pollinations (free), then procedural — whichever is available. This is the recommended setting: real art for free, with paid backends used automatically if you ever add those keys. |

## Fonts

Drop `Inter-Regular.ttf` / `Inter-Bold.ttf` into `assets/fonts/` for
production-quality text rendering on composed pages. Without them, Pillow's
built-in bitmap font is used as a safe fallback.

## Open story items (see `content/series-bible.yaml` → `open_items`)

- Shadow's final identity/design (Issue 13)
- MSmaster's ultimate fate (affects Issue 16 ending)
- Whether Chuck folds into Zero's role
- Hadess Banshees individual names/designs
- Alex Olsen's hero name
