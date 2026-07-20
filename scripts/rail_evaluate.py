#!/usr/bin/env python3
"""Evaluate a trained rail defect detector on the held-out test images.

Loads the model saved by scripts/rail_train.py and the *current* value of
`threshold` from configs/rail_ndt_config.yaml (everything else in that file
only takes effect after re-running rail_train.py). Prints the average
Intersection-over-Union (IoU, higher is better) and saves example predicted
masks + a JSON report so you can compare with classmates.

Usage:
    python3 scripts/rail_evaluate.py
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import yaml

from rail_common import CHECKPOINT_PATH, FIGURES_DIR, HEIGHT, REPORTS_DIR, WIDTH, load_gray, load_mask, pixel_features

CONFIG_PATH = Path(__file__).resolve().parent.parent / "configs" / "rail_ndt_config.yaml"


def load_current_threshold() -> float:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return float(config.get("threshold", 0.5))


def score_image(pred_mask: np.ndarray, true_mask: np.ndarray) -> dict:
    intersection = int(np.logical_and(pred_mask, true_mask).sum())
    union = int(np.logical_or(pred_mask, true_mask).sum())
    pred_sum = int(pred_mask.sum())
    true_sum = int(true_mask.sum())

    iou = 1.0 if union == 0 else intersection / union
    dice = 1.0 if (pred_sum + true_sum) == 0 else (2 * intersection) / (pred_sum + true_sum)
    return {"iou": iou, "dice": dice}


def main():
    if not CHECKPOINT_PATH.exists():
        print(f"error: no trained model found at {CHECKPOINT_PATH}")
        print("run scripts/rail_train.py first")
        sys.exit(1)

    saved = joblib.load(CHECKPOINT_PATH)
    model, train_config, split = saved["model"], saved["config"], saved["split"]
    threshold = load_current_threshold()

    test_ids = split["test"]
    if not test_ids:
        print("error: no images assigned to the test split")
        sys.exit(1)

    print(f"evaluating on {len(test_ids)} held-out images with threshold={threshold}")

    per_image = []
    examples = []  # (gray, true_mask, pred_mask) for a few images, for the figure
    for image_id in test_ids:
        feats = pixel_features(image_id)
        true_mask = load_mask(image_id)
        probs = model.predict_proba(feats)[:, 1].reshape(HEIGHT, WIDTH)
        pred_mask = (probs >= threshold).astype(np.uint8)

        scores = score_image(pred_mask, true_mask)
        per_image.append({"image_id": image_id, **scores})

        if len(examples) < 4:
            examples.append((np.asarray(load_gray(image_id)), true_mask, pred_mask))

    mean_iou = float(np.mean([s["iou"] for s in per_image]))
    mean_dice = float(np.mean([s["dice"] for s in per_image]))

    print(f"Mean IoU:  {mean_iou:.3f} (higher is better, 1.0 = perfect)")
    print(f"Mean Dice: {mean_dice:.3f} (higher is better, 1.0 = perfect)")

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(len(examples), 3, figsize=(9, 3 * len(examples)))
    if len(examples) == 1:
        axes = axes.reshape(1, 3)
    col_titles = ["rail photo", "true defect mask", "predicted defect mask"]
    for row, (gray, true_mask, pred_mask) in enumerate(examples):
        for col, (img, title) in enumerate(zip([gray, true_mask, pred_mask], col_titles)):
            axes[row, col].imshow(img, cmap="gray")
            axes[row, col].axis("off")
            if row == 0:
                axes[row, col].set_title(title)
    fig.suptitle(f"Rail defect detection: mean IoU = {mean_iou:.3f}")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "rail_eval.png", dpi=150)

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_type": train_config.get("model_type"),
        "train_config": train_config,
        "threshold_used": threshold,
        "n_test": len(test_ids),
        "mean_iou": mean_iou,
        "mean_dice": mean_dice,
        "per_image": per_image,
    }
    with open(REPORTS_DIR / "rail_eval.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"saved example predictions to {FIGURES_DIR / 'rail_eval.png'}")
    print(f"saved report to {REPORTS_DIR / 'rail_eval.json'}")


if __name__ == "__main__":
    main()
