#!/usr/bin/env python3
"""Generate a one-page PDF report summarizing your Lab 2 (rail NDT) results.

Reads results/reports/rail_eval.json (written by rail_evaluate.py) and the
two pictures it saved, and lays them out on a single PDF page --
results/reports/rail_report.pdf -- with your settings, score, and both
plots, ready to print or share with a classmate/instructor. Built entirely
with matplotlib (already a dependency of this lab) -- no LaTeX, no extra
packages to install.

Usage:
    python3 scripts/rail_report.py
"""
import json
import sys

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from rail_common import FIGURES_DIR, REPORTS_DIR

REPORT_JSON = REPORTS_DIR / "rail_eval.json"
OVERLAY_PATH = FIGURES_DIR / "rail_eval.png"
CURVE_PATH = FIGURES_DIR / "rail_eval_threshold_curve.png"


def score_color(iou: float) -> str:
    if iou >= 0.5:
        return "#1a7f37"
    if iou >= 0.25:
        return "#9a6700"
    return "#cf222e"


def main():
    if not REPORT_JSON.exists():
        print(f"error: no report found at {REPORT_JSON}")
        print("run scripts/rail_evaluate.py first")
        sys.exit(1)
    if not OVERLAY_PATH.exists() or not CURVE_PATH.exists():
        print("error: figures not found -- run scripts/rail_evaluate.py first")
        sys.exit(1)

    report = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
    config = {k: v for k, v in report["train_config"].items() if k != "threshold"}
    config["threshold (used here)"] = report["threshold_used"]
    iou = report["mean_iou"]
    dice = report["mean_dice"]

    overlay_img = mpimg.imread(OVERLAY_PATH)
    curve_img = mpimg.imread(CURVE_PATH)

    fig = plt.figure(figsize=(8.27, 11.69))  # A4 portrait

    fig.text(0.07, 0.965, "Lab 2 Report", fontsize=20, fontweight="bold", va="top")
    fig.text(0.07, 0.94, "Rail Defect Detection", fontsize=13, color="0.25", va="top")
    fig.text(
        0.07, 0.915,
        f"Generated {report['timestamp'][:19]} UTC  ·  {report['n_test']} held-out test images",
        fontsize=9, color="0.4", va="top",
    )

    fig.text(0.07, 0.875, "Mean IoU / Mean Dice", fontsize=10, color="0.3", va="top")
    fig.text(0.07, 0.86, f"{iou:.3f} / {dice:.3f}", fontsize=28, fontweight="bold", color=score_color(iou), va="top")
    fig.text(0.44, 0.845, "(higher is better, 1.0 = perfect)", fontsize=10, color="0.4", va="top")

    fig.text(0.07, 0.775, "Settings used", fontsize=12, fontweight="bold", va="top")
    ax_table = fig.add_axes((0.07, 0.60, 0.5, 0.16))
    ax_table.axis("off")
    table = ax_table.table(
        cellText=[[k, str(v)] for k, v in config.items()],
        colLabels=["setting", "value"],
        cellLoc="left",
        loc="upper left",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9.5)
    table.scale(1, 1.5)
    table.auto_set_column_width([0, 1])

    fig.text(0.07, 0.565, "Example predictions", fontsize=12, fontweight="bold", va="top")
    ax1 = fig.add_axes((0.06, 0.38, 0.88, 0.175))
    ax1.imshow(overlay_img)
    ax1.axis("off")

    fig.text(0.07, 0.345, "Threshold sweep", fontsize=12, fontweight="bold", va="top")
    ax2 = fig.add_axes((0.18, 0.03, 0.64, 0.30))
    ax2.imshow(curve_img)
    ax2.axis("off")

    out_path = REPORTS_DIR / "rail_report.pdf"
    fig.savefig(out_path)
    print(f"saved report to {out_path}")


if __name__ == "__main__":
    main()
