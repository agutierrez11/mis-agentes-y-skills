---
name: media-generation
description: Generate visual assets — SVG vectors, PNG/JPEG raster images, and video — routing each to the right engine: the Magnific MCP for vector and video when connected, and the Codex and Antigravity CLIs (already covered by the user's ChatGPT and Google subscriptions) for raster, never a metered API. Use whenever a task needs a generated icon, logo, illustration, photo, texture, hero image, background, mockup, or video clip; when the user asks to "generate an image / make an icon / create a hero"; or when deciding whether an asset should be vector or raster.
---

# Media Generation

Two local CLIs generate images on subscriptions the user already pays for. Neither charges per token or per image. Prefer them over any metered API.

**Never reach for a paid image/video API without asking first.** The whole point of this skill is avoiding extra billing.

## Pick the right format first

This decision matters more than which engine you use. Getting it wrong produces assets that look cheap or bloat the page.

| Asset | Format | How |
|---|---|---|
| Icon, logo, wordmark | **SVG** | See SVG routing below |
| Pattern, divider, blob, texture overlay | **SVG** | See SVG routing below |
| Decorative illustration, vector scene, sticker art | **SVG** | See SVG routing below |
| Chart, diagram, wireframe | **SVG** | Always author the markup — the data must be exact |
| Photo, product shot, hero, portrait | **Raster** | `generate_image` (see engines) |
| Texture, painterly background, sprite | **Raster** | `generate_image` |
| UI mockup, packaging mockup | **Raster** | `generate_image` |

Rules that follow from this:

- **Never substitute an SVG placeholder for a requested photo.** If the user asked for a photograph, generate a raster.
- **Match the existing repo.** If the project already has an SVG icon set, extend it in the same style — do not generate a raster icon that clashes with the set.
- **Tracing a raster into SVG is a last resort.** It works acceptably on flat art with few colors; on a photograph it produces thousands of junk paths, a huge file, and edges that shimmer when scaled.

### Generating SVG

**Default rule: if the Magnific MCP is connected, use the vector model. If it is not, author the markup with Codex.**

**1. Text-to-SVG model — preferred when available.** Recraft v4 Pro Vector, via Magnific `images_generate_svg` (supports `aspectRatio`). `images_to_svg` traces an existing raster.

Output is true vector, but expect many paths, no semantic grouping, and hardcoded fills rather than `currentColor`. Clean it up before shipping if the asset has to theme with CSS.

**2. Author the markup — fallback, and free.** You or `codex exec` write the SVG directly. SVG is code, and a code agent is good at it. Covers icons, logos, geometry, patterns, dividers, and charts completely.

Keep it clean: a `viewBox`, no fixed `width`/`height` unless required, `currentColor` for strokes and fills so CSS can theme it, no editor cruft (`<metadata>`, `id="Layer_1"`, inline `<style>` blocks).

One case overrides the default: when **extending an existing icon set** in the repo, author the markup regardless of what is connected. A generated icon will not match the stroke weight, corner radius, and grid of icons already there.

## Engines for raster

### Codex CLI (ChatGPT subscription)

The binary is **not on PATH** — it ships inside the desktop app:

```
/Applications/ChatGPT.app/Contents/Resources/codex
```

```bash
/Applications/ChatGPT.app/Contents/Resources/codex exec --skip-git-repo-check \
  "Generate an image: <prompt>. Print the absolute path of the saved file."
```

- Output: `~/.codex/generated_images/<session-uuid>/<call-id>.png`, 1536x1024 by default.
- Formats: PNG (default), JPEG, WebP.
- **Gotcha:** the default sandbox is read-only, so Codex cannot copy the file into the working directory itself — it will report `Operation not permitted`. Copy it out yourself with `cp` afterwards, or pass `--sandbox workspace-write`.
- Transparency: generate on a flat chroma-key background, then run `~/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py`.
- Ships a built-in `imagegen` skill with prompting guidance at `~/.codex/skills/.system/imagegen/`.

Verify auth with `codex doctor` — look for `auth mode: chatgpt`.

### Antigravity CLI (Google subscription)

```bash
agy -p "Generate a <aspect> image with generate_image: <prompt>. Then print only the absolute saved path. Do not run any shell commands."
```

- Output: `~/.gemini/antigravity-cli/brain/<uuid>/<name>_<timestamp>.jpg`
- Format: JPEG only.
- Aspect ratio is respected when stated in the prompt: 16:9 yields 1376x768, square yields 1024x1024.
- **Gotcha:** in headless (`-p`) mode any shell command the agent tries to run is auto-denied and the whole run dies with `jetski: no output produced`. Always add *"Do not run any shell commands"* to the prompt. Do not reach for `--dangerously-skip-permissions` to work around it.

Install via `brew install --cask antigravity-cli` (links the binary as `agy`).

### Choosing between them

Codex for anything needing PNG, transparency, non-square control, or more than 1024px on the short edge. Antigravity for quick JPEG drafts. When quality matters, generate with both and compare — both are free.

## Video

**There is no free programmatic path to video generation on this machine.** Investigated and confirmed 2026-07-30:

- Antigravity CLI has `generate_image` but **no video tool** and no plugins that add one.
- The full Antigravity desktop app was installed and ruled out too. Its `language_server` binary contains `generate_image` and zero strings for `generate_video`, `veo`, `imagen`, or any video tool. Same agent backend as the CLI. Uninstalled again.
- Gemini API: Veo 3.1 is explicitly *not available* on the free tier. Paid is $0.40/s at 1080p.
- The Gemini CLI `genmedia` extension requires a Google Cloud project, Vertex AI, and a GCS bucket — metered billing.
- Gemini.app is a native Swift app with no bundled CLI and no AppleScript support. GUI only.

Veo on a subscription lives only behind a GUI (gemini.google.com, Flow, Gemini.app). So:

1. **Ask the user** before spending anything on video.
2. If a Magnific MCP is connected, `video_generate` with slug `google-veo3_1` is the only working programmatic route (4K, 4/6/8s, audio, start+end keyframes, 3 image refs).
3. Best results come from generating the exact opening frame with Codex, then passing it as the start keyframe so the model only animates — far better than text-to-video blind.
4. Often the right answer is no generated video at all: real footage, or an animated SVG/CSS loop, which costs nothing and looks sharper.

## Prompting

Structure as **scene/backdrop → subject → details → constraints**. State the intended use (hero, ad, UI mock) so the model picks the right polish level. Use camera and composition language for photorealism — focal length, depth of field, time of day. Quote text verbatim and spell tricky words letter-by-letter. Iterate with one targeted change at a time, repeating the invariants each round so the image does not drift.

Always view the generated file before using it. Check subject, composition, text accuracy, and anything you told it to avoid.
