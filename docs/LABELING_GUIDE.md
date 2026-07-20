# Cargo Fill-Level Labeling Guide

This is a teaching exercise: students look at each cargo photo and estimate how full
the truck is, so we get the "answer key" (labels) an AI model will later learn to
predict on its own. There is no automatic ground truth for this — a human has to
decide it first, exactly like real-world data labeling for AI projects.

## What you're looking at

Each photo comes from a fixed camera bolted inside the cargo box of a delivery
truck — one camera near the front, one near the rear, both facing into the pile of
boxes/parcels. As the truck gets loaded during the day, the pile grows. The goal is
to estimate what fraction of the cargo box's volume is currently taken up by cargo.

## How to label

1. Open `datasets/processed/manifest.csv` (e.g. in Excel/Google Sheets/Numbers).
2. For each row, open the image at `datasets/processed/<filepath>` and look at it.
3. Fill in the `fill_level` column with one of these five words:

| fill_level | fill_pct | What it looks like |
|---|---|---|
| `empty`  | 0   | Floor of the cargo box is fully visible, little to no cargo. |
| `low`    | 25  | Some boxes/bags on the floor, most of the floor still visible. |
| `medium` | 50  | Cargo covers roughly half the floor area, or is piled about waist-height. |
| `high`   | 75  | Cargo fills most of the visible space, stacked well above waist-height. |
| `full`   | 100 | Cargo fills the frame edge-to-edge / floor-to-ceiling, no empty space visible. |

Use your best visual judgment — this is a rough estimate, not a precise
measurement. Being consistent across images matters more than being exact on any
one photo.

4. Leave `fill_pct` and `split` blank — scripts fill those in automatically later.
5. Optionally jot anything unusual in `notes` (e.g. "camera angle blocked",
   "door partially closed").

## Tips

- Front and rear camera views of the *same moment* (matching `event_id`) should
  usually get a similar label, since they're looking at the same pile from
  opposite ends — but they don't have to match exactly if one camera's view is
  more obstructed.
- Sort the CSV by `vehicle_id`, `date`, `camera_view`, `event_seq` to view each
  camera's photos in chronological order — fullness should generally increase
  over the course of the day, which is a good sanity check on your own labels.

## After labeling

Once every row has a `fill_level`, run:

```bash
python3 scripts/make_splits.py
```

This fills in `fill_pct` from the table above and assigns each image to
`train`/`val`/`test` (grouped so a front/rear pair from the same event always
stays together, so the model isn't accidentally tested on a view of the same
moment it trained on).
