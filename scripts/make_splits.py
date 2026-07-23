#!/usr/bin/env python3
"""Assign train/val/test splits to hand-labeled cargo images.

Run this only after every row in datasets/processed/manifest.csv has a
fill_level filled in by hand (see docs/LABELING_GUIDE.md). It fills in fill_pct
from the bin table below, then splits images into train/val/test, grouped by
event_id so a front/rear pair from the same moment always lands in the same
split (otherwise the model could be "tested" on a near-duplicate of a training
image, which would make evaluation misleadingly optimistic).

The dataset is small enough (~20 events) that a plain random split can easily
leave a split missing some fill_level values entirely, which makes results
misleading -- a MAE never checked against a 100%-full photo, or a model that
never trained on one. So splits are built deliberately, via greedy set-cover,
applied twice:

  1. `test` is built first: events are added (biggest new fill_pct coverage
     first, ties broken by a fixed shuffle) until every fill_pct value that
     appears anywhere in the manifest is represented in test.
  2. `train` is built the same way from whatever events are left, but only
     covering fill_pct values still available in that leftover pool (some
     values may have been used up entirely by test's requirement above) --
     capped at train's normal target share of events.

Whatever's left over after both (often very few) becomes `val`. `val` is
treated as the flex bucket here -- it's the one allowed to shrink and/or end
up with uneven fill_pct coverage.
"""
import csv
import random
import sys
from collections import defaultdict

from cargo_common import FILL_PCT_BY_LEVEL, MANIFEST_PATH

SPLIT_RATIOS = {"train": 0.7, "val": 0.15, "test": 0.15}
SEED = 42


def greedy_cover(pool: list, event_pcts: dict, target_pcts: set, budget: int = None) -> tuple:
    """Greedily pick events from `pool` (in its given order) to cover as much
    of `target_pcts` as possible, preferring events that cover the most
    still-missing values at each step. Stops once `target_pcts` is fully
    covered, `budget` events have been picked (if given), or no remaining
    event adds new coverage. Returns (chosen_events, leftover_pool)."""
    pool = pool.copy()
    covered = set()
    chosen = []
    while covered != target_pcts and pool and (budget is None or len(chosen) < budget):
        best = max(pool, key=lambda e: len(event_pcts[e] - covered))
        if not (event_pcts[best] - covered):
            break  # no remaining event adds new coverage
        chosen.append(best)
        covered |= event_pcts[best]
        pool.remove(best)
    return chosen, pool


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
    event_pcts = {eid: {int(r["fill_pct"]) for r in evt_rows} for eid, evt_rows in events.items()}

    all_pcts = set().union(*event_pcts.values()) if event_pcts else set()
    test_events, remaining = greedy_cover(event_ids, event_pcts, all_pcts)
    split_for_event = {eid: "test" for eid in test_events}

    n_train = min(round(n * SPLIT_RATIOS["train"]), len(remaining))
    remaining_pcts = set().union(*(event_pcts[e] for e in remaining)) if remaining else set()
    train_priority, remaining = greedy_cover(remaining, event_pcts, remaining_pcts, budget=n_train)
    for eid in train_priority:
        split_for_event[eid] = "train"

    n_train_left = n_train - len(train_priority)
    for eid in remaining[:n_train_left]:
        split_for_event[eid] = "train"
    for eid in remaining[n_train_left:]:
        split_for_event[eid] = "val"

    for r in rows:
        r["split"] = split_for_event[r["event_id"]]

    with open(MANIFEST_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    counts = defaultdict(int)
    pcts_by_split = defaultdict(set)
    for r in rows:
        counts[r["split"]] += 1
        pcts_by_split[r["split"]].add(int(r["fill_pct"]))
    print(f"assigned splits across {n} events / {len(rows)} images: {dict(counts)}")
    for split in ("train", "val", "test"):
        print(f"  {split}: fill_pct values covered = {sorted(pcts_by_split[split])}")


if __name__ == "__main__":
    main()
