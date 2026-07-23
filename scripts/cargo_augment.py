#!/usr/bin/env python3
"""Generate extra, altered copies of the labeled TRAINING cargo photos.

Optional step (Part 5.5 of the cargo lab): with only ~30 training photos, the
model has very little variety to learn from. This script makes each training
photo do double duty by saving a few randomly altered copies next to it --
flipped, slightly rotated, and brightness/contrast-jittered -- and adding them
to datasets/processed/manifest.csv as extra 'train' rows with the same
fill_level/fill_pct as their original. It never touches 'val' or 'test' rows,
so evaluation always happens on real, unaltered photos.

Controlled by `augment_per_image` in configs/cargo_config.yaml (0 disables
it, and un-does a previous run). Safe to re-run: it first removes any
augmented rows/images left over from a previous run, then regenerates from
whatever is currently labeled 'train' -- so re-label or re-run
scripts/make_splits.py with augment_per_image set to 0 before touching either
one, then augment again afterwards.

Usage:
    python3 scripts/cargo_augment.py
"""
import csv
import random
import shutil
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageEnhance

from cargo_common import MANIFEST_PATH, PROCESSED_DIR

CONFIG_PATH = Path(__file__).resolve().parent.parent / "configs" / "cargo_config.yaml"
AUGMENTED_DIR = PROCESSED_DIR / "images_augmented"
NOTE_PREFIX = "augmented from "
SEED = 42

ROTATION_RANGE = (-8, 8)       # degrees
BRIGHTNESS_RANGE = (0.8, 1.2)  # multiplier, 1.0 = unchanged
CONTRAST_RANGE = (0.8, 1.2)    # multiplier, 1.0 = unchanged


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_rows():
    with open(MANIFEST_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_rows(rows):
    with open(MANIFEST_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def make_variant(img: Image.Image, rng: random.Random) -> Image.Image:
    out = img
    if rng.random() < 0.5:
        out = out.transpose(Image.FLIP_LEFT_RIGHT)
    out = out.rotate(rng.uniform(*ROTATION_RANGE), resample=Image.BICUBIC, fillcolor=(0, 0, 0))
    out = ImageEnhance.Brightness(out).enhance(rng.uniform(*BRIGHTNESS_RANGE))
    out = ImageEnhance.Contrast(out).enhance(rng.uniform(*CONTRAST_RANGE))
    return out


def main():
    config = load_config()
    n_per_image = int(config.get("augment_per_image", 0))

    rows = load_rows()
    originals = [r for r in rows if not r["notes"].startswith(NOTE_PREFIX)]

    if AUGMENTED_DIR.exists():
        shutil.rmtree(AUGMENTED_DIR)

    if n_per_image <= 0:
        save_rows(originals)
        print("augment_per_image is 0 in configs/cargo_config.yaml -- augmentation skipped")
        print(f"removed any previously generated augmented photos/rows; manifest now has {len(originals)} rows")
        return

    train_rows = [r for r in originals if r["split"] == "train"]
    if not train_rows:
        print("error: no rows assigned to the 'train' split")
        print("label photos and run scripts/make_splits.py before augmenting")
        sys.exit(1)

    rng = random.Random(SEED)
    new_rows = []
    for r in train_rows:
        img = Image.open(PROCESSED_DIR / r["filepath"]).convert("RGB")
        view_dir = AUGMENTED_DIR / r["camera_view"]
        view_dir.mkdir(parents=True, exist_ok=True)

        for i in range(1, n_per_image + 1):
            variant = make_variant(img, rng)
            aug_id = f"{r['image_id']}_aug{i}"
            out_path = view_dir / f"{aug_id}.jpg"
            variant.save(out_path, quality=90)

            new_row = dict(r)
            new_row["image_id"] = aug_id
            new_row["filepath"] = str(out_path.relative_to(PROCESSED_DIR))
            new_row["notes"] = f"{NOTE_PREFIX}{r['image_id']}"
            new_rows.append(new_row)

    save_rows(originals + new_rows)
    print(f"generated {len(new_rows)} augmented copies from {len(train_rows)} training photos ({n_per_image} each)")
    print(f"saved images under {AUGMENTED_DIR}")
    print(f"added {len(new_rows)} rows to {MANIFEST_PATH} (split=train)")
    print("run scripts/cargo_train.py to retrain including the augmented photos")


if __name__ == "__main__":
    main()
