#!/usr/bin/env python3
"""Train a cargo fill-level model using datasets/processed/manifest.csv.

Reads model settings from configs/cargo_config.yaml (edit that file, not this
one) and saves the trained model to models/checkpoints/cargo_model.joblib.

Usage:
    python3 scripts/cargo_train.py
"""
import csv
import sys
from pathlib import Path

import joblib
import numpy as np
import yaml
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

from cargo_common import CHECKPOINT_PATH, MANIFEST_PATH, PROCESSED_DIR, extract_features

CONFIG_PATH = Path(__file__).resolve().parent.parent / "configs" / "cargo_config.yaml"

MODEL_BUILDERS = {
    "random_forest": lambda cfg: RandomForestRegressor(
        n_estimators=cfg.get("n_estimators", 100),
        max_depth=cfg.get("max_depth", 5),
        random_state=cfg.get("random_seed", 42),
    ),
    "knn": lambda cfg: KNeighborsRegressor(
        n_neighbors=cfg.get("n_neighbors", 5),
    ),
    "linear_regression": lambda cfg: LinearRegression(),
}


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_rows():
    with open(MANIFEST_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    config = load_config()
    model_type = config.get("model_type", "random_forest")
    if model_type not in MODEL_BUILDERS:
        print(f"error: model_type '{model_type}' not recognized, expected one of {list(MODEL_BUILDERS)}")
        sys.exit(1)

    rows = load_rows()
    if any(not r["split"].strip() for r in rows):
        print("error: manifest.csv has unlabeled/unsplit rows.")
        print("label fill_level for every row, then run scripts/make_splits.py, before training.")
        sys.exit(1)

    train_rows = [r for r in rows if r["split"] == "train"]
    if not train_rows:
        print("error: no rows assigned to the 'train' split.")
        sys.exit(1)

    print(f"extracting features for {len(train_rows)} training photos...")
    X = np.stack([extract_features(PROCESSED_DIR / r["filepath"]) for r in train_rows])
    y = np.array([float(r["fill_pct"]) for r in train_rows])

    model = MODEL_BUILDERS[model_type](config)
    model.fit(X, y)

    CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "config": config}, CHECKPOINT_PATH)

    print(f"trained {model_type} on {len(train_rows)} photos")
    print(f"saved model to {CHECKPOINT_PATH}")


if __name__ == "__main__":
    main()
