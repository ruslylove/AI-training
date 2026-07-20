# Dataset Notes: Cargo Fill-Level Photos

## Source

Internal fleet dashcam footage, not a public dataset. Two fixed IP cameras are
mounted inside each truck's cargo box (one near the front, one near the rear,
both facing into the cargo). Each camera saves a snapshot whenever it triggers on
an "alarm" event (motion/door activity), timestamped to the millisecond.

## Raw layout

```
datasets/raw/{plate}-{location}-{date}/
├── {camera_ip}-กล้องหน้า/{date}/alarm/*.jpg   # front camera
└── {camera_ip}-กล้องหลัง/{date}/alarm/*.jpg   # rear camera
```

- `plate` — vehicle license plate, e.g. `66-0129`
- `location` — route/depot name (Thai), e.g. `มีนบุรี` (Min Buri)
- `date` — capture date
- `กล้องหน้า` = front camera, `กล้องหลัง` = rear camera
- filenames are `{17-digit-timestamp}-alarm.jpg`, where the timestamp is
  `YYYYMMDDHHMMSSmmm`

## Current data (as of 2026-07-20)

One vehicle-day: plate `66-0129`, Min Buri route, 2026-06-10 — 21 front + 21 rear
alarm snapshots (42 images total), spanning roughly 03:00–21:00 as the truck was
loaded through the day.

## Adding more data

Drop additional `{plate}-{location}-{date}/` folders (same internal layout) into
`datasets/raw/`, then re-run `python3 scripts/organize_dataset.py`. It rebuilds
`datasets/processed/images/` and `manifest.csv`, and preserves any labels already
entered for images it has seen before (matched by `image_id`), so re-running is
safe and never erases labeling progress.

## Known limitations

- Single vehicle, single day so far — not enough variety (lighting, truck type,
  camera angle) to train a model that generalizes; treat this as a teaching demo,
  not a production dataset.
- `fill_level` labels are subjective human estimates, not measured volume — see
  `docs/LABELING_GUIDE.md`.
