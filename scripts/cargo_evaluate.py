#!/usr/bin/env python3
"""Evaluate a trained cargo fill-level model on the held-out test photos.

Loads the model saved by scripts/cargo_train.py, scores it on the manifest's
'test' split, prints the Mean Absolute Error (in percentage points -- lower is
better), and saves a scatter plot + JSON report so you can compare with
classmates.

Usage:
    python3 scripts/cargo_evaluate.py
"""
import csv
import json
import sys
from datetime import datetime, timezone

import joblib
import matplotlib.pyplot as plt
import numpy as np

from cargo_common import (
    CHECKPOINT_PATH, FIGURES_DIR, MANIFEST_PATH, PROCESSED_DIR, REPORTS_DIR, extract_features,
)


def load_rows():
    with open(MANIFEST_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    if not CHECKPOINT_PATH.exists():
        print(f"error: no trained model found at {CHECKPOINT_PATH}")
        print("run scripts/cargo_train.py first")
        sys.exit(1)

    saved = joblib.load(CHECKPOINT_PATH)
    model, config = saved["model"], saved["config"]

    rows = load_rows()
    test_rows = [r for r in rows if r["split"] == "test"]
    if not test_rows:
        print("error: no rows assigned to the 'test' split -- run scripts/make_splits.py first")
        sys.exit(1)

    X = np.stack([extract_features(PROCESSED_DIR / r["filepath"]) for r in test_rows])
    y_true = np.array([float(r["fill_pct"]) for r in test_rows])
    y_pred = np.clip(model.predict(X), 0, 100)

    mae = float(np.mean(np.abs(y_true - y_pred)))

    print(f"tested on {len(test_rows)} held-out photos")
    print(f"Mean Absolute Error: {mae:.1f} percentage points (lower is better)")

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot([0, 100], [0, 100], "--", color="gray", label="perfect prediction")
    ax.scatter(y_true, y_pred, color="tab:blue")
    ax.set_xlabel("actual fill %")
    ax.set_ylabel("predicted fill %")
    ax.set_title(f"Cargo fill-level: MAE = {mae:.1f} pts")
    ax.set_xlim(-5, 105)
    ax.set_ylim(-5, 105)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "cargo_eval.png", dpi=150)

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_type": config.get("model_type"),
        "config": config,
        "n_test": len(test_rows),
        "mae_percentage_points": mae,
        "predictions": [
            {"image_id": r["image_id"], "actual": float(r["fill_pct"]), "predicted": round(float(p), 1)}
            for r, p in zip(test_rows, y_pred)
        ],
    }
    with open(REPORTS_DIR / "cargo_eval.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"saved plot to {FIGURES_DIR / 'cargo_eval.png'}")
    print(f"saved report to {REPORTS_DIR / 'cargo_eval.json'}")


if __name__ == "__main__":
    main()
