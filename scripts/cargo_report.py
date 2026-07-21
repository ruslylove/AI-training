#!/usr/bin/env python3
"""Generate a one-page PDF report summarizing your Lab 1 (cargo) results.

Reads results/reports/cargo_eval.json (written by cargo_evaluate.py) and the
two pictures it saved, and lays them out on a single PDF page --
results/reports/cargo_report.pdf -- with your settings, score, and both
plots, ready to print or share with a classmate/instructor. Built entirely
with matplotlib (already a dependency of this lab) -- no LaTeX, no extra
packages to install.

Usage:
    python3 scripts/cargo_report.py
"""
import json
import sys

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from cargo_common import FIGURES_DIR, REPORTS_DIR

REPORT_JSON = REPORTS_DIR / "cargo_eval.json"
STRIP_PATH = FIGURES_DIR / "cargo_eval.png"
SCATTER_PATH = FIGURES_DIR / "cargo_eval_scatter.png"

RELEVANT_KEYS_BY_MODEL = {
    "random_forest": ["model_type", "n_estimators", "max_depth", "random_seed"],
    "knn": ["model_type", "n_neighbors", "random_seed"],
    "linear_regression": ["model_type", "random_seed"],
}


def score_color(mae: float) -> str:
    if mae <= 10:
        return "#1a7f37"
    if mae <= 20:
        return "#9a6700"
    return "#cf222e"


def main():
    if not REPORT_JSON.exists():
        print(f"error: no report found at {REPORT_JSON}")
        print("run scripts/cargo_evaluate.py first")
        sys.exit(1)
    if not STRIP_PATH.exists() or not SCATTER_PATH.exists():
        print("error: figures not found -- run scripts/cargo_evaluate.py first")
        sys.exit(1)

    report = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
    full_config = report["config"]
    mae = report["mae_percentage_points"]

    relevant_keys = RELEVANT_KEYS_BY_MODEL.get(full_config.get("model_type"), list(full_config.keys()))
    config = {k: full_config[k] for k in relevant_keys if k in full_config}

    strip_img = mpimg.imread(STRIP_PATH)
    scatter_img = mpimg.imread(SCATTER_PATH)

    fig = plt.figure(figsize=(8.27, 11.69))  # A4 portrait

    fig.text(0.07, 0.965, "Lab 1 Report", fontsize=20, fontweight="bold", va="top")
    fig.text(0.07, 0.94, "Cargo Fill-Level Estimation", fontsize=13, color="0.25", va="top")
    fig.text(
        0.07, 0.915,
        f"Generated {report['timestamp'][:19]} UTC  ·  {report['n_test']} held-out test photos",
        fontsize=9, color="0.4", va="top",
    )

    fig.text(0.07, 0.875, "Mean Absolute Error", fontsize=10, color="0.3", va="top")
    fig.text(0.07, 0.86, f"{mae:.1f} pts", fontsize=28, fontweight="bold", color=score_color(mae), va="top")
    fig.text(0.34, 0.845, "(lower is better)", fontsize=10, color="0.4", va="top")

    fig.text(0.07, 0.775, "Settings used", fontsize=12, fontweight="bold", va="top")
    ax_table = fig.add_axes((0.07, 0.62, 0.5, 0.14))
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

    fig.text(0.07, 0.585, "Predictions vs. actual (sorted by actual %)", fontsize=12, fontweight="bold", va="top")
    ax1 = fig.add_axes((0.06, 0.36, 0.88, 0.215))
    ax1.imshow(strip_img)
    ax1.axis("off")

    fig.text(0.07, 0.325, "Overall accuracy", fontsize=12, fontweight="bold", va="top")
    ax2 = fig.add_axes((0.22, 0.03, 0.56, 0.285))
    ax2.imshow(scatter_img)
    ax2.axis("off")

    out_path = REPORTS_DIR / "cargo_report.pdf"
    fig.savefig(out_path)
    print(f"saved report to {out_path}")


if __name__ == "__main__":
    main()
