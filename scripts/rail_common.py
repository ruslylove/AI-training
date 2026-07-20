"""Shared helpers for the rail NDT lab: data listing, train/val/test split, and
per-pixel feature extraction.

Feature extraction is intentionally fixed (not student-tunable) so the lab
stays "no code" -- students only choose a model type, its hyperparameters, and
a decision threshold in configs/rail_ndt_config.yaml. Every pixel is described
by a small, explainable set of numbers:
  - how bright the pixel is
  - how bright its surroundings are on average ("local context")
  - how much brightness varies nearby (rough texture)
  - how strong an edge passes through it
  - where it sits in the image (row/column position)
"""
import numpy as np
from pathlib import Path
from PIL import Image, ImageFilter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RSDDS_DIR = PROJECT_ROOT / "datasets" / "raw" / "rail_ndt" / "rsdds"
IMAGE_DIR = RSDDS_DIR / "2D_Image" / "INPUT_IMG"
MASK_DIR = RSDDS_DIR / "GroundTruth" / "Ground Truth"
CHECKPOINT_PATH = PROJECT_ROOT / "models" / "checkpoints" / "rail_model.joblib"
FIGURES_DIR = PROJECT_ROOT / "results" / "figures"
REPORTS_DIR = PROJECT_ROOT / "results" / "reports"

WIDTH, HEIGHT = 128, 64  # fixed internal working resolution (downsized from 535x252)
LOCAL_RADIUS = 3          # fixed internal "how big is nearby" window
MAX_TRAIN_PIXELS_PER_IMAGE = 3000  # keeps training fast; test images use all pixels

TRAIN_FRACTION = 0.7
VAL_FRACTION = 0.15
# remaining ~0.15 goes to test


def list_image_ids():
    return sorted(int(p.stem) for p in IMAGE_DIR.glob("*.bmp"))


def split_ids(seed: int) -> dict:
    ids = list_image_ids()
    shuffled = ids.copy()
    np.random.RandomState(seed).shuffle(shuffled)
    n = len(shuffled)
    n_train = round(n * TRAIN_FRACTION)
    n_val = round(n * VAL_FRACTION)
    return {
        "train": sorted(shuffled[:n_train]),
        "val": sorted(shuffled[n_train:n_train + n_val]),
        "test": sorted(shuffled[n_train + n_val:]),
    }


def _box_filter(arr: np.ndarray, radius: int) -> np.ndarray:
    """Exact mean over a (2*radius+1)^2 window around every pixel, via cumulative sums."""
    k = 2 * radius + 1
    padded = np.pad(arr, radius, mode="reflect")

    csum_rows = np.cumsum(padded, axis=0)
    csum_rows = np.vstack([np.zeros((1, csum_rows.shape[1]), dtype=arr.dtype), csum_rows])
    row_windowed = csum_rows[k:] - csum_rows[:-k]

    csum_cols = np.cumsum(row_windowed, axis=1)
    csum_cols = np.hstack([np.zeros((csum_cols.shape[0], 1), dtype=arr.dtype), csum_cols])
    box_sum = csum_cols[:, k:] - csum_cols[:, :-k]

    return box_sum / (k * k)


def load_gray(image_id: int) -> Image.Image:
    return Image.open(IMAGE_DIR / f"{image_id}.bmp").convert("L").resize((WIDTH, HEIGHT), Image.LANCZOS)


def load_mask(image_id: int) -> np.ndarray:
    mask = Image.open(MASK_DIR / f"{image_id}.png").convert("L").resize((WIDTH, HEIGHT), Image.NEAREST)
    return (np.asarray(mask) > 127).astype(np.uint8)


def pixel_features(image_id: int) -> np.ndarray:
    """Returns an (HEIGHT*WIDTH, 6) feature matrix, row-major (matches load_mask flatten order)."""
    img = load_gray(image_id)
    gray = np.asarray(img, dtype=np.float32) / 255.0

    local_mean = _box_filter(gray, LOCAL_RADIUS)
    local_mean_sq = _box_filter(gray ** 2, LOCAL_RADIUS)
    local_std = np.sqrt(np.clip(local_mean_sq - local_mean ** 2, 0, None))

    edges = np.asarray(img.filter(ImageFilter.FIND_EDGES), dtype=np.float32) / 255.0

    rows, cols = np.indices((HEIGHT, WIDTH))
    row_norm = rows / (HEIGHT - 1)
    col_norm = cols / (WIDTH - 1)

    feats = np.stack([gray, local_mean, local_std, edges, row_norm, col_norm], axis=-1)
    return feats.reshape(-1, feats.shape[-1])
