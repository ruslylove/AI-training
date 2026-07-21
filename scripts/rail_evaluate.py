#!/usr/bin/env python3
"""Evaluate a trained rail defect detector on the held-out test images.

Loads the model saved by scripts/rail_train.py and the *current* value of
`threshold` from configs/rail_ndt_config.yaml (everything else in that file
only takes effect after re-running rail_train.py). Prints the average
Intersection-over-Union (IoU, higher is better) and saves two pictures + a
JSON report so you can compare with classmates:
  - rail_eval.png -- several test images side by side, each showing the rail
    photo with true and predicted defect areas overlaid in color (green =
    missed defect, red = false alarm, yellow = correctly caught) and its own
    IoU score, so you can see exactly what the model gets right or wrong.
  - rail_eval_threshold_curve.png -- Mean IoU/Dice swept across every
    threshold from 0.05 to 0.95 using this same trained model, with your
    configured threshold marked -- an at-a-glance view of Part 3's
    threshold trade-off, no manual re-running needed.

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
from matplotlib.patches import Patch

from rail_common import CHECKPOINT_PATH, FIGURES_DIR, HEIGHT, REPORTS_DIR, WIDTH, load_gray, load_mask, pixel_features

CONFIG_PATH = Path(__file__).resolve().parent.parent / "configs" / "rail_ndt_config.yaml"
MAX_EXAMPLES = 6

MISSED_COLOR = np.array([0.10, 0.80, 0.10])    # green -- true defect, not predicted
FALSE_ALARM_COLOR = np.array([0.90, 0.15, 0.15])  # red -- predicted, not a true defect
CORRECT_COLOR = np.array([0.95, 0.85, 0.10])   # yellow -- true & predicted overlap


def make_overlay(gray: np.ndarray, true_mask: np.ndarray, pred_mask: np.ndarray, alpha: float = 0.6) -> np.ndarray:
    base = np.stack([gray, gray, gray], axis=-1).astype(np.float32) / 255.0
    overlay = base.copy()
    missed = (true_mask == 1) & (pred_mask == 0)
    false_alarm = (true_mask == 0) & (pred_mask == 1)
    correct = (true_mask == 1) & (pred_mask == 1)
    for region, color in [(missed, MISSED_COLOR), (false_alarm, FALSE_ALARM_COLOR), (correct, CORRECT_COLOR)]:
        overlay[region] = (1 - alpha) * base[region] + alpha * color
    return overlay


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


def sweep_thresholds(probs_by_image, true_masks, thresholds):
    mean_ious, mean_dices = [], []
    for t in thresholds:
        ious, dices = [], []
        for probs, true_mask in zip(probs_by_image, true_masks):
            pred_mask = (probs >= t).astype(np.uint8)
            scores = score_image(pred_mask, true_mask)
            ious.append(scores["iou"])
            dices.append(scores["dice"])
        mean_ious.append(float(np.mean(ious)))
        mean_dices.append(float(np.mean(dices)))
    return mean_ious, mean_dices


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
    examples = []  # (gray, true_mask, pred_mask, iou) for a few images, for the figure
    probs_by_image = []
    true_masks = []
    for image_id in test_ids:
        feats = pixel_features(image_id)
        true_mask = load_mask(image_id)
        probs = model.predict_proba(feats)[:, 1].reshape(HEIGHT, WIDTH)
        pred_mask = (probs >= threshold).astype(np.uint8)

        scores = score_image(pred_mask, true_mask)
        per_image.append({"image_id": image_id, **scores})
        probs_by_image.append(probs)
        true_masks.append(true_mask)

        if len(examples) < MAX_EXAMPLES:
            examples.append((np.asarray(load_gray(image_id)), true_mask, pred_mask, scores["iou"]))

    mean_iou = float(np.mean([s["iou"] for s in per_image]))
    mean_dice = float(np.mean([s["dice"] for s in per_image]))

    print(f"Mean IoU:  {mean_iou:.3f} (higher is better, 1.0 = perfect)")
    print(f"Mean Dice: {mean_dice:.3f} (higher is better, 1.0 = perfect)")

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(1, len(examples), figsize=(3.2 * len(examples), 3.8))
    axes = np.atleast_1d(axes)
    for col, (gray, true_mask, pred_mask, iou) in enumerate(examples):
        axes[col].imshow(make_overlay(gray, true_mask, pred_mask))
        axes[col].axis("off")
        axes[col].set_title(f"IoU: {iou:.2f}", fontsize=10)

    legend_handles = [
        Patch(color=CORRECT_COLOR, label="correctly caught"),
        Patch(color=MISSED_COLOR, label="missed defect"),
        Patch(color=FALSE_ALARM_COLOR, label="false alarm"),
    ]
    fig.legend(handles=legend_handles, loc="lower center", ncol=3, fontsize=9, frameon=False)
    fig.suptitle(f"Rail defect detection -- mean IoU = {mean_iou:.3f}", fontsize=12)
    fig.tight_layout(rect=(0, 0.08, 1, 0.94))
    fig.savefig(FIGURES_DIR / "rail_eval.png", dpi=150)

    sweep_thresholds_grid = np.linspace(0.05, 0.95, 19)
    sweep_iou, sweep_dice = sweep_thresholds(probs_by_image, true_masks, sweep_thresholds_grid)

    fig3, ax3 = plt.subplots(figsize=(6, 4.2))
    ax3.plot(sweep_thresholds_grid, sweep_iou, marker="o", label="Mean IoU", color="tab:blue")
    ax3.plot(sweep_thresholds_grid, sweep_dice, marker="o", label="Mean Dice", color="tab:orange")
    ax3.axvline(threshold, linestyle="--", color="gray", label=f"current threshold ({threshold})")
    ax3.set_xlabel("threshold")
    ax3.set_ylabel("score (higher is better)")
    ax3.set_title("Rail defect detection: score vs. threshold")
    ax3.legend()
    fig3.tight_layout()
    fig3.savefig(FIGURES_DIR / "rail_eval_threshold_curve.png", dpi=150)

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
    print(f"saved threshold sweep curve to {FIGURES_DIR / 'rail_eval_threshold_curve.png'}")
    print(f"saved report to {REPORTS_DIR / 'rail_eval.json'}")


if __name__ == "__main__":
    main()
