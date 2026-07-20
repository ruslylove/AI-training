#!/usr/bin/env python3
"""Assign train/val/test splits to hand-labeled cargo images.

Run this only after every row in datasets/processed/manifest.csv has a
fill_level filled in by hand (see docs/LABELING_GUIDE.md). It fills in fill_pct
from the bin table below, then splits images into train/val/test, grouped by
event_id so a front/rear pair from the same moment always lands in the same
split (otherwise the model could be "tested" on a near-duplicate of a training
image, which would make evaluation misleadingly optimistic).

The split is a simple random split (not stratified by fill_level) because the
dataset is currently too small (~20 events) for reliable per-bin stratification.
Re-run this once more vehicle-days are added.
"""
import csv
import random
import sys
from collections import defaultdict

from cargo_common import FILL_PCT_BY_LEVEL, MANIFEST_PATH

SPLIT_RATIOS = {"train": 0.7, "val": 0.15, "test": 0.15}
SEED = 42


def main():
    with open(MANIFEST_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    missing = [r["image_id"] for r in rows if not r["fill_level"].strip()]
    if missing:
        print(f"error: {len(missing)} images still need fill_level labeled, e.g. {missing[:5]}")
        print("label datasets/processed/manifest.csv per docs/LABELING_GUIDE.md before splitting")
        sys.exit(1)

    unknown = {r["fill_level"].strip() for r in rows} - set(FILL_PCT_BY_LEVEL)
    if unknown:
        print(f"error: unrecognized fill_level values: {unknown}")
        print(f"expected one of: {sorted(FILL_PCT_BY_LEVEL)}")
        sys.exit(1)

    for r in rows:
        r["fill_pct"] = str(FILL_PCT_BY_LEVEL[r["fill_level"].strip()])

    events = defaultdict(list)
    for r in rows:
        events[r["event_id"]].append(r)

    event_ids = list(events)
    random.Random(SEED).shuffle(event_ids)

    n = len(event_ids)
    n_train = round(n * SPLIT_RATIOS["train"])
    n_val = round(n * SPLIT_RATIOS["val"])
    split_for_event = {}
    for i, eid in enumerate(event_ids):
        if i < n_train:
            split_for_event[eid] = "train"
        elif i < n_train + n_val:
            split_for_event[eid] = "val"
        else:
            split_for_event[eid] = "test"

    for r in rows:
        r["split"] = split_for_event[r["event_id"]]

    with open(MANIFEST_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    counts = defaultdict(int)
    for r in rows:
        counts[r["split"]] += 1
    print(f"assigned splits across {n} events / {len(rows)} images: {dict(counts)}")


if __name__ == "__main__":
    main()
