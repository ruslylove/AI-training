# AI-training: Student AI/ML Exercises

## Project Overview

Two hands-on exercises for students learning how AI/ML works end to end:

1. **Railway NDT defect detection** (main track) — detect and localize surface
   defects on rail track (e.g. rail head cracks, spalling) from images, using
   the public RSDDs benchmark dataset. This mirrors real industrial
   Non-Destructive Testing (NDT) work: condition-based maintenance without
   relying purely on manual visual inspection.
2. **Cargo fill-level estimation** (sideway exercise) — using photos from
   cameras mounted inside delivery truck cargo boxes, estimate what percentage
   of the cargo space is used. Unlike the rail dataset, there's no automatic
   ground truth here, so students walk through hand-labeling data themselves —
   a good first taste of what "preparing data for AI" actually involves before
   tackling the rail track.

**Student labsheets** (start here if you're a student, not an instructor) —
each is available as Markdown and as a formatted PDF (built from the matching
`.tex` source via `pdflatex`, requires a LaTeX install to rebuild):
- `docs/labsheets/cargo_labsheet.md` / `docs/labsheets/cargo_labsheet.pdf`
- `docs/labsheets/rail_ndt_labsheet.md` / `docs/labsheets/rail_ndt_labsheet.pdf`

To rebuild a PDF after editing its `.tex` source:
```bash
cd docs/labsheets
pdflatex cargo_labsheet.tex && pdflatex cargo_labsheet.tex   # run twice
```

**Thai versions** (`_th` suffix) — full Thai translations of both labsheets,
for the KMUTNB cohort below. Code, filenames, commands and YAML settings are
left in English (they're literal, not prose); everything else is translated.
They use a separate style (`labsheet_common_th.sty`) built for **XeLaTeX**
with a bundled Thai font (`docs/labsheets/fonts/Sarabun-*.ttf`, SIL OFL —
see `fonts/OFL.txt`) since plain `pdflatex` can't render Thai script:
- `docs/labsheets/cargo_labsheet_th.md` / `docs/labsheets/cargo_labsheet_th.pdf`
- `docs/labsheets/rail_ndt_labsheet_th.md` / `docs/labsheets/rail_ndt_labsheet_th.pdf`

To rebuild a Thai PDF after editing its `.tex` source (note `xelatex`, not
`pdflatex`):
```bash
cd docs/labsheets
xelatex cargo_labsheet_th.tex && xelatex cargo_labsheet_th.tex   # run twice
```

Both labs are "no code": all training/evaluation scripts are already
written. Students only hand-label data and/or edit a plain-text
`configs/*.yaml` settings file, then run the provided scripts.

**Slides** (`slides.md`) — a full session deck for the "AI Data Analytics
for Transportation Sector" module within the *AI-Driven Transformation in
Public Governance* program (Faculty of Engineering, KMUTNB, for Ministry of
Transport scholarship students spanning multiple departments, not just rail).
Includes a ~60
minute AI & NDT fundamentals lecture (Part 1) before the two hands-on labs
(Parts 2–3), with real sample photos from both datasets embedded. Built with
[Slidev](https://sli.dev/), theme `seriph`, branding via `global-top.vue` /
`global-bottom.vue`:
```bash
pnpm install              # one-time
pnpm run dev               # live-editable slideshow at localhost:3030
pnpm run build             # static site -> dist/
pnpm run export            # -> slides-export.pdf (uses --per-slide, required
                            # for correct page numbers with global components)
```
Slide images live in `public/img/` (referenced as `/img/...` in `slides.md`).

**Thai version** (`slides.th.md`) — full Thai translation of the deck, same
structure/layout/images, for the KMUTNB cohort above. Code blocks, YAML
settings and file/script names are left in English. Uses the bundled
`Sarabun` web font (declared via `fonts:` in its frontmatter) for correct
Thai rendering. Build/export the same way, just point at the Thai file
explicitly (the `pnpm run *` scripts above default to `slides.md`):
```bash
pnpm exec slidev build slides.th.md
pnpm exec slidev export slides.th.md --output slides-th-export.pdf --per-slide
```

## Folder Structure

```
AI-training/
├── datasets/
│   ├── raw/
│   │   ├── {plate}-{location}-{date}/   # cargo: raw fleet-camera photo dumps
│   │   └── rail_ndt/rsdds/              # rail: RSDDs images + depth + ground-truth masks
│   ├── processed/                       # cargo: renamed images/ + manifest.csv (see below)
│   └── splits/                          # train / val / test folders
├── models/
│   ├── checkpoints/  # saved model weights during training
│   └── exports/      # final exported models (TF.js, ONNX, etc.)
├── notebooks/        # Jupyter notebooks for exploration and results
├── scripts/          # Python scripts: data prep, training, evaluation (see below)
├── configs/          # student-editable settings (no code) for each lab
├── results/
│   ├── figures/      # plots, confusion matrices, POD curves
│   └── reports/      # evaluation summaries
├── docs/
│   └── labsheets/    # step-by-step student lab instructions
├── slides.md          # session deck: fundamentals lecture + both labs (Slidev)
├── global-top.vue     # slide branding: top-right overlay (every slide)
├── global-bottom.vue  # slide branding: footer with page count (every slide)
├── public/img/        # sample photos embedded in slides.md
├── package.json       # Slidev dependencies/scripts
├── .gitignore
└── README.md
```

## Datasets Used

Datasets are not committed to version control (see `.gitignore`).

- **Cargo fill-level photos** — fleet dashcam-style front/rear camera snapshots
  per truck-day, under `datasets/raw/{plate}-{location}-{date}/`. See
  `docs/cargo_dataset_notes.md` for provenance and how to add more vehicle-days.
- **RSDDs (rail surface defects)** — public academic benchmark, 113 images with
  paired depth maps and defect ground-truth masks, under
  `datasets/raw/rail_ndt/rsdds/`. See `docs/rail_ndt_dataset_notes.md` for
  citation, structure, and other candidate rail datasets considered.

## Getting Started

### Prerequisites

- Python 3.10+
- `unzip` (used by `scripts/fetch_rsdds.py` to extract the rail dataset)
- `pip install -r requirements.txt` — lightweight, classical-ML stack
  (`numpy`, `pandas`, `pillow`, `scikit-learn`, `pyyaml`, `matplotlib`), no
  `torch`/`tensorflow` required. Chosen deliberately over deep learning so
  setup is fast and reliable on student laptops.

### Setup

```bash
cd AI-training
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Workflow: Cargo fill-level estimation

Full instructions: `docs/labsheets/cargo_labsheet.md`.

1. Drop new raw camera-dump folders into `datasets/raw/` (see `docs/cargo_dataset_notes.md` for the expected layout).
2. Run `python3 scripts/organize_dataset.py` to build `datasets/processed/images/` and `datasets/processed/manifest.csv`.
3. Hand-label `fill_level` for each row in `manifest.csv` per `docs/LABELING_GUIDE.md`.
4. Run `python3 scripts/make_splits.py` to fill in `fill_pct` and assign train/val/test splits.
5. Edit `configs/cargo_config.yaml` (model type + hyperparameters, no code), then run `python3 scripts/cargo_train.py`.
6. Run `python3 scripts/cargo_evaluate.py` to get a Mean Absolute Error score, a photo strip of predictions sorted by actual fill %, and a predicted-vs-actual scatter plot.
7. (Optional) Run `python3 scripts/cargo_report.py` to bundle your settings, score, and both plots into a single `results/reports/cargo_report.pdf`.

### Workflow: Railway NDT defect detection

Full instructions: `docs/labsheets/rail_ndt_labsheet.md`.

1. Run `python3 scripts/fetch_rsdds.py` to download and extract RSDDs into `datasets/raw/rail_ndt/rsdds/` (safe to re-run; skips archives already extracted).
2. Edit `configs/rail_ndt_config.yaml` (model type + hyperparameters, no code), then run `python3 scripts/rail_train.py`.
3. Run `python3 scripts/rail_evaluate.py` to get a mean IoU/Dice score, example true/predicted defect overlays, and a threshold-vs-score sweep curve. Re-run this alone (no retraining) after changing just the `threshold` setting.
4. (Optional) Run `python3 scripts/rail_report.py` to bundle your settings, score, and both plots into a single `results/reports/rail_report.pdf`.

### Both tracks

- Trained models are saved to `models/checkpoints/` (`cargo_model.joblib`, `rail_model.joblib`).
- Evaluation plots are saved to `results/figures/`, JSON reports to `results/reports/`, and (if you ran the report scripts) shareable one-page PDF reports alongside them.
- Export final models to `models/exports/` for deployment (not covered by the current lab scripts).
