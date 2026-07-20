"""Shared helpers for the cargo fill-level lab: label mapping + feature extraction.

Feature extraction is intentionally fixed (not a student-tunable setting) so the
lab stays "no code" -- students only choose a model type and its hyperparameters
in configs/cargo_config.yaml. Each photo is boiled down to a small, explainable
set of numbers:
  - overall brightness (mean/std of a grayscale, shrunk copy of the photo)
  - how much "edge" texture is visible (more boxes/edges -> higher value)
  - a brightness histogram (how light/dark pixels are distributed)
  - a tiny, blurry grid of the photo itself (coarse shape information)
"""
import numpy as np
from pathlib import Path
from PIL import Image, ImageFilter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "datasets" / "processed"
MANIFEST_PATH = PROCESSED_DIR / "manifest.csv"
CHECKPOINT_PATH = PROJECT_ROOT / "models" / "checkpoints" / "cargo_model.joblib"
FIGURES_DIR = PROJECT_ROOT / "results" / "figures"
REPORTS_DIR = PROJECT_ROOT / "results" / "reports"

FILL_PCT_BY_LEVEL = {"empty": 0, "low": 25, "medium": 50, "high": 75, "full": 100}

RAW_GRID_SIZE = 8   # tiny "blurry photo" grid used as coarse-shape features
HIST_BINS = 16


def extract_features(image_path: Path) -> np.ndarray:
    img = Image.open(image_path).convert("RGB")

    gray_full = img.convert("L")
    gray_arr = np.asarray(gray_full, dtype=np.float32)
    brightness_mean = gray_arr.mean() / 255.0
    brightness_std = gray_arr.std() / 255.0

    edges = np.asarray(gray_full.filter(ImageFilter.FIND_EDGES), dtype=np.float32)
    edge_density = edges.mean() / 255.0

    hist, _ = np.histogram(gray_arr, bins=HIST_BINS, range=(0, 255))
    hist = hist / hist.sum()

    small = np.asarray(
        gray_full.resize((RAW_GRID_SIZE, RAW_GRID_SIZE), Image.LANCZOS), dtype=np.float32
    ) / 255.0

    return np.concatenate([
        [brightness_mean, brightness_std, edge_density],
        hist,
        small.flatten(),
    ])
