<p align="center">
  <img src="https://raw.githubusercontent.com/TeachDiffusion/.github/main/assets/teachdiffusion_logo.svg" alt="TeachDiffusion" width="280"/>
</p>

<h1 align="center">teachdiffusion-space</h1>

<p align="center">
  Gradio demo app, deployed to HuggingFace Spaces.
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/TeachDiffusion/demo"><img src="https://img.shields.io/badge/🤗-Try%20the%20demo-yellow.svg" alt="HuggingFace Space"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
</p>

> For project mission, the full 8-layer architecture, sibling repositories, and roadmap, see the [TeachDiffusion organization profile](https://github.com/TeachDiffusion).

---

## About this repo

A thin **Gradio wrapper** around the core [`teachdiffusion`](https://github.com/TeachDiffusion/TeachDiffusion) package. The whole UI is one file — [`app.py`](app.py) — that calls `TeachDiffusionPipeline.generate_lesson(...)` and renders the resulting script, explanation, and (when a GPU is available) video.

This repo contains no model logic of its own. When something in the pipeline needs to change, change it in the core repo; the Space picks it up via the `teachdiffusion` dependency in [`requirements.txt`](requirements.txt).

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Gradio launches on `http://localhost:7860`.

## Inputs

The demo accepts a math topic, a difficulty (`beginner` / `intermediate` / `advanced`), and a persona, then surfaces:

- **Script** — the per-step lesson plan (step type, gesture, pacing)
- **Explanation** — the layered hook → intuition → formal → examples breakdown
- **Video** (GPU-enabled deployments only) — the rendered teacher video

## Assets

[`assets/examples/`](assets/examples) holds sample inputs and outputs surfaced inside the Gradio UI.

## Deploy

The repo is mirrored to a HuggingFace Space at [`TeachDiffusion/demo`](https://huggingface.co/spaces/TeachDiffusion/demo). Pushes to the deployment branch trigger a rebuild on the Space.

## License

Apache 2.0 — see [LICENSE](LICENSE).
