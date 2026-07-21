#!/usr/bin/env python3
"""Evaluate a trained cargo fill-level model on the held-out test photos.

Loads the model saved by scripts/cargo_train.py, scores it on the manifest's
'test' split, prints the Mean Absolute Error (in percentage points -- lower is
better), and saves two pictures + a JSON report so you can compare with
classmates:
  - cargo_eval.png -- every test photo side by side, sorted by actual fill %,
    each captioned with actual vs. predicted, so you can see at a glance
    where the model's guesses track (or miss) reality.
  - cargo_eval_scatter.png -- the classic predicted-vs-actual scatter plot,
    for a quick at-a-glance read of overall accuracy across every test photo
    at once (dots closer to the diagonal = better).

Usage:
    python3 scripts/cargo_evaluate.py
"""
import csv
import json
import math
import sys
from datetime import datetime, timezone

import joblib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from cargo_common import (
    CHECKPOINT_PATH, FIGURES_DIR, MANIFEST_PATH, PROCESSED_DIR, REPORTS_DIR, extract_features,
)

MAX_COLS = 7


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

    order = np.argsort(y_true)
    n = len(order)
    n_cols = min(n, MAX_COLS)
    n_rows = math.ceil(n / n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(2.3 * n_cols, 2.7 * n_rows))
    axes = np.atleast_2d(axes)

    for slot, i in enumerate(order):
        row, col = divmod(slot, n_cols)
        ax = axes[row, col]
        img = Image.open(PROCESSED_DIR / test_rows[i]["filepath"])
        ax.imshow(img)
        ax.axis("off")
        error = abs(y_true[i] - y_pred[i])
        color = "tab:green" if error <= 10 else "tab:orange" if error <= 20 else "tab:red"
        ax.set_title(f"actual {y_true[i]:.0f}%  |  pred {y_pred[i]:.0f}%", fontsize=9, color=color)

    for slot in range(n, n_rows * n_cols):
        row, col = divmod(slot, n_cols)
        axes[row, col].axis("off")

    fig.suptitle(
        f"Cargo fill-level -- test photos sorted by actual %  (MAE = {mae:.1f} pts)\n"
        "green = close prediction, orange = off, red = way off",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(FIGURES_DIR / "cargo_eval.png", dpi=150)

    fig2, ax2 = plt.subplots(figsize=(5, 5))
    ax2.plot([0, 100], [0, 100], "--", color="gray", label="perfect prediction")
    ax2.scatter(y_true, y_pred, color="tab:blue")
    ax2.set_xlabel("actual fill %")
    ax2.set_ylabel("predicted fill %")
    ax2.set_title(f"Cargo fill-level: MAE = {mae:.1f} pts")
    ax2.set_xlim(-5, 105)
    ax2.set_ylim(-5, 105)
    ax2.legend()
    fig2.tight_layout()
    fig2.savefig(FIGURES_DIR / "cargo_eval_scatter.png", dpi=150)

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

    print(f"saved photo strip to {FIGURES_DIR / 'cargo_eval.png'}")
    print(f"saved scatter plot to {FIGURES_DIR / 'cargo_eval_scatter.png'}")
    print(f"saved report to {REPORTS_DIR / 'cargo_eval.json'}")


if __name__ == "__main__":
    main()
