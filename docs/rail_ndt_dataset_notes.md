# Dataset Notes: Railway NDT (Rail Surface Defects)

## Source: RSDDs (Rail Surface Defect Datasets)

Public academic benchmark published by Northeastern University (China).

- Source repo: https://github.com/neu-rail-rsdds/rsdds
- License/citation: no explicit license stated; cite the papers below if used
  in any report or publication.
- Citation:
  - M. Niu, K. Song, L. Huang, Q. Wang, Y. Yan and Q. Meng, "Unsupervised
    Saliency Detection of Rail Surface Defects Using Stereoscopic Images,"
    IEEE Trans. on Industrial Informatics, vol. 17, no. 3, pp. 2271-2281,
    March 2021.
  - M. Niu, Y. Wang, K. Song, Q. Wang, Y. Zhao and Y. Yan, "An Adaptive
    Pyramid Graph and Variation Residual-Based Anomaly Detection Network for
    Rail Surface Defects," IEEE Trans. on Instrumentation and Measurement,
    vol. 70, 2021, Art no. 5020013.
- Downloaded: 2026-07-20, via `scripts/fetch_rsdds.py`.

## What's in it

113 images of rail surfaces, each with three paired files:

```
datasets/raw/rail_ndt/rsdds/
├── 2D_Image/INPUT_IMG/{n}.bmp       # left camera RGB image
├── Depthmap/INPUT_IMG1/{n}.bmp      # corresponding stereo depth image
└── GroundTruth/Ground Truth/{n}.png # hand-annotated defect mask (white = defect)
```

`{n}` runs 1–113 and matches across all three folders (`1.bmp` / `1.bmp` /
`1.png` are the same rail sample).

Unlike the cargo dataset, **this one already has ground-truth labels** — the
white regions in the `GroundTruth` masks mark exactly where the defect is.
That makes it suited to a different (and more advanced) kind of exercise than
cargo fill estimation:

- **Classification**: does this rail image contain a defect? (every image
  here does, so you'd need a source of non-defective images too — see below)
- **Segmentation / localization**: given the RGB image, predict a mask of
  where the defect is (directly usable with the provided ground truth).

## Known limitations

- All 113 images contain a defect — there are no "clean rail" negative
  examples in this dataset, so it isn't directly usable for a simple
  defective-vs-not classifier on its own.
- Small dataset by deep-learning standards; expect to use heavy augmentation
  or a pretrained backbone if training from scratch.
- `.bmp` images are large/uncompressed; consider converting to `.png`/`.jpg`
  during preprocessing to save space and speed up loading.

## Other candidate datasets (not fetched)

- **Kaggle — Railway Track Fault Detection (resized 224×224)**
  (https://www.kaggle.com/datasets/gpiosenka/railway-track-fault-detection-resized-224-x-224):
  385 images, binary Defective/Non_defective labels with a pre-made
  train/valid/test split in `rails.csv`, ~13 MB, CC BY-SA 4.0. Simpler and
  better suited to a first classification exercise than RSDDs, but needs a
  Kaggle account + API token to download (none configured on this machine) —
  grab it manually from the browser, or place a `kaggle.json` token in
  `~/.kaggle/` and ask to have it fetched automatically.
- **Rail-5k** (https://zenodo.org/records/4872772): 5,000 images, 1,100
  annotated across 13 defect/accessory classes — the richest option, but
  Zenodo access is restricted; you'd need to request access directly from
  the authors before it can be downloaded.

## Adding more data

Re-run `python3 scripts/fetch_rsdds.py` any time — it skips any archive
that's already been extracted, so it won't re-download or overwrite existing
files.
