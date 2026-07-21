#!/usr/bin/env python3
"""Assign train/val/test splits to hand-labeled cargo images.

Run this only after every row in datasets/processed/manifest.csv has a
fill_level filled in by hand (see docs/LABELING_GUIDE.md). It fills in fill_pct
from the bin table below, then splits images into train/val/test, grouped by
event_id so a front/rear pair from the same moment always lands in the same
split (otherwise the model could be "tested" on a near-duplicate of a training
image, which would make evaluation misleadingly optimistic).

The dataset is small enough (~20 events) that a plain random split can easily
leave `test` missing some fill_level values entirely, which makes the reported
MAE misleading (it never got checked against, say, a 100%-full photo). So
`test` is built first and deliberately, via a greedy set-cover: events are
added to test (biggest new fill_pct coverage first, ties broken by a fixed
shuffle) until every fill_pct value that appears anywhere in the manifest is
represented in test. Remaining events fill `train` up to its normal target
share; whatever's left over (often very few, if test's coverage requirement
ate into the pool) becomes `val`. `val` is treated as the flex bucket here --
it's the one allowed to shrink and/or end up with uneven fill_pct coverage.
"""
import csv
import random
import sys
from collections import defaultdict

from cargo_common import FILL_PCT_BY_LEVEL, MANIFEST_PATH

SPLIT_RATIOS = {"train": 0.7, "val": 0.15, "test": 0.15}
SEED = 42


def build_test_events(event_ids: list, event_pcts: dict) -> list:
    """Greedily pick the fewest events needed for `test` to cover every
    fill_pct value present anywhere in event_pcts, preferring events that
    cover the most still-missing values at each step."""
    all_pcts = set().union(*event_pcts.values()) if event_pcts else set()
    pool = event_ids.copy()  # already shuffled by caller
    covered = set()
    test_events = []
    while covered != all_pcts and pool:
        best = max(pool, key=lambda e: len(event_pcts[e] - covered))
        if not (event_pcts[best] - covered):
            break  # no remaining event adds new coverage
        test_events.append(best)
        covered |= event_pcts[best]
        pool.remove(best)
    return test_events


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

    test_events = build_test_events(event_ids, event_pcts)
    split_for_event = {eid: "test" for eid in test_events}

    remaining = [eid for eid in event_ids if eid not in split_for_event]
    n_train = min(round(n * SPLIT_RATIOS["train"]), len(remaining))
    for eid in remaining[:n_train]:
        split_for_event[eid] = "train"
    for eid in remaining[n_train:]:
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
