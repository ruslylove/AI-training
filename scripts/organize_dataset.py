#!/usr/bin/env python3
"""Organize raw fleet-camera cargo photos into datasets/processed/ with a labeling manifest.

Expects datasets/raw/ to contain one folder per vehicle-day, named:
    {plate}-{location}-{date}/{camera_ip}-{camera_view_label}/{date}/alarm/*.jpg

where camera_view_label is the Thai front/rear camera label (see VIEW_BY_LABEL below)
and each *.jpg is named "{17-digit-timestamp}-alarm.jpg".

Copies (never moves) images into datasets/processed/images/{front,rear}/ with clean,
sortable filenames, and writes datasets/processed/manifest.csv with one row per image.

Safe to re-run whenever a new vehicle-day folder is dropped into datasets/raw/: it
rebuilds the image copies and manifest rows, but preserves any fill_level/notes/split
values a student has already entered for images it has seen before (matched by
image_id), so re-running never wipes out labeling progress.
"""
import csv
import re
import shutil
from datetime import datetime
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parent.parent / "datasets" / "raw"
OUT_DIR = Path(__file__).resolve().parent.parent / "datasets" / "processed"
IMAGES_DIR = OUT_DIR / "images"
MANIFEST_PATH = OUT_DIR / "manifest.csv"

VIEW_BY_LABEL = {
    "กล้องหน้า": "front",
    "กล้องหลัง": "rear",
}

VEHICLE_DAY_RE = re.compile(r"^(?P<plate>[^-]+-[^-]+)-(?P<location>.+)-(?P<date>\d{4}-\d{2}-\d{2})$")
CAMERA_DIR_RE = re.compile(r"^(?P<ip>[\d.]+)-(?P<view_label>.+)$")
TIMESTAMP_RE = re.compile(r"^(?P<ts>\d{17})-alarm\.jpg$")

FIELDNAMES = [
    "image_id", "filepath", "vehicle_id", "location", "date", "camera_view",
    "camera_ip", "event_id", "event_seq", "timestamp_iso",
    "fill_level", "fill_pct", "notes", "split",
]

LABEL_FIELDS = ("fill_level", "fill_pct", "notes", "split")


def load_existing_labels() -> dict:
    if not MANIFEST_PATH.exists():
        return {}
    with open(MANIFEST_PATH, newline="", encoding="utf-8") as f:
        return {row["image_id"]: row for row in csv.DictReader(f)}


def parse_timestamp(ts: str) -> datetime:
    # ts is YYYYMMDDHHMMSSmmm (17 digits: date + time + milliseconds)
    return datetime.strptime(ts[:14], "%Y%m%d%H%M%S")


def main():
    existing = load_existing_labels()
    rows = []
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    for vd_dir in sorted(p for p in RAW_DIR.iterdir() if p.is_dir()):
        m = VEHICLE_DAY_RE.match(vd_dir.name)
        if not m:
            print(f"skip (name doesn't match plate-location-date): {vd_dir.name}")
            continue
        plate, location, date = m["plate"], m["location"], m["date"]

        for cam_dir in sorted(p for p in vd_dir.iterdir() if p.is_dir()):
            cm = CAMERA_DIR_RE.match(cam_dir.name)
            if not cm or cm["view_label"] not in VIEW_BY_LABEL:
                print(f"skip (unrecognized camera dir): {cam_dir.name}")
                continue
            ip, view = cm["ip"], VIEW_BY_LABEL[cm["view_label"]]

            parsed = []
            for jpg in sorted(cam_dir.glob("*/alarm/*.jpg")):
                tm = TIMESTAMP_RE.match(jpg.name)
                if not tm:
                    print(f"skip (unexpected filename): {jpg}")
                    continue
                parsed.append((tm["ts"], jpg))
            parsed.sort(key=lambda t: t[0])  # chronological per vehicle/date/view

            view_out_dir = IMAGES_DIR / view
            view_out_dir.mkdir(parents=True, exist_ok=True)

            for seq, (ts, jpg) in enumerate(parsed, start=1):
                event_id = ts[:14]
                dt = parse_timestamp(ts)
                image_id = f"{plate}_{date}_{view}_{seq:03d}"
                out_path = view_out_dir / f"{image_id}_{ts}.jpg"
                shutil.copy2(jpg, out_path)

                row = {
                    "image_id": image_id,
                    "filepath": str(out_path.relative_to(OUT_DIR)),
                    "vehicle_id": plate,
                    "location": location,
                    "date": date,
                    "camera_view": view,
                    "camera_ip": ip,
                    "event_id": event_id,
                    "event_seq": seq,
                    "timestamp_iso": dt.isoformat(),
                    "fill_level": "",
                    "fill_pct": "",
                    "notes": "",
                    "split": "",
                }
                prior = existing.get(image_id)
                if prior:
                    for field in LABEL_FIELDS:
                        row[field] = prior.get(field, "")
                rows.append(row)

    rows.sort(key=lambda r: (r["vehicle_id"], r["date"], r["camera_view"], int(r["event_seq"])))

    with open(MANIFEST_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} images to {IMAGES_DIR}")
    print(f"wrote manifest: {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
