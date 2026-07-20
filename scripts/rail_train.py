#!/usr/bin/env python3
"""Train a rail surface defect detector on the RSDDs dataset.

Reads model settings from configs/rail_ndt_config.yaml (edit that file, not
this one) and saves the trained model to models/checkpoints/rail_model.joblib,
together with the exact train/val/test image split used, so later evaluation
always tests on the same held-out images regardless of later config edits.

Usage:
    python3 scripts/rail_train.py
"""
import sys
from pathlib import Path

import joblib
import numpy as np
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from rail_common import CHECKPOINT_PATH, MAX_TRAIN_PIXELS_PER_IMAGE, list_image_ids, load_mask, pixel_features, split_ids

CONFIG_PATH = Path(__file__).resolve().parent.parent / "configs" / "rail_ndt_config.yaml"

MODEL_BUILDERS = {
    "random_forest": lambda cfg: RandomForestClassifier(
        n_estimators=cfg.get("n_estimators", 100),
        max_depth=cfg.get("max_depth", 8),
        class_weight="balanced",
        random_state=cfg.get("random_seed", 42),
    ),
    "logistic_regression": lambda cfg: LogisticRegression(
        class_weight="balanced",
        max_iter=2000,
    ),
}


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def subsample_indices(mask_flat: np.ndarray, max_pixels: int, rng: np.random.RandomState) -> np.ndarray:
    """Pick up to max_pixels indices, keeping a mix of defect and background pixels."""
    all_idx = np.arange(mask_flat.shape[0])
    if len(all_idx) <= max_pixels:
        return all_idx

    pos_idx = all_idx[mask_flat == 1]
    neg_idx = all_idx[mask_flat == 0]
    n_pos = min(len(pos_idx), max_pixels // 2)
    n_neg = min(len(neg_idx), max_pixels - n_pos)

    pos_sample = rng.choice(pos_idx, size=n_pos, replace=False) if n_pos > 0 else np.array([], dtype=int)
    neg_sample = rng.choice(neg_idx, size=n_neg, replace=False) if n_neg > 0 else np.array([], dtype=int)
    return np.concatenate([pos_sample, neg_sample])


def main():
    config = load_config()
    model_type = config.get("model_type", "random_forest")
    if model_type not in MODEL_BUILDERS:
        print(f"error: model_type '{model_type}' not recognized, expected one of {list(MODEL_BUILDERS)}")
        sys.exit(1)

    seed = config.get("random_seed", 42)
    ids = list_image_ids()
    if not ids:
        print("error: no RSDDs images found -- run scripts/fetch_rsdds.py first")
        sys.exit(1)

    split = split_ids(seed)
    rng = np.random.RandomState(seed)

    print(f"extracting pixel features for {len(split['train'])} training images...")
    X_parts, y_parts = [], []
    for image_id in split["train"]:
        feats = pixel_features(image_id)
        mask_flat = load_mask(image_id).flatten()
        idx = subsample_indices(mask_flat, MAX_TRAIN_PIXELS_PER_IMAGE, rng)
        X_parts.append(feats[idx])
        y_parts.append(mask_flat[idx])

    X = np.concatenate(X_parts)
    y = np.concatenate(y_parts)
    print(f"training on {len(y)} sampled pixels ({y.sum()} defect / {len(y) - y.sum()} background)")

    model = MODEL_BUILDERS[model_type](config)
    model.fit(X, y)

    CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "config": config, "split": split}, CHECKPOINT_PATH)

    print(f"trained {model_type} on {len(split['train'])} images")
    print(f"saved model to {CHECKPOINT_PATH}")


if __name__ == "__main__":
    main()
