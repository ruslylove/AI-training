#!/usr/bin/env python3
"""Download and extract the RSDDs rail surface defect dataset into datasets/raw/.

RSDDs (Rail Surface Defect Datasets) is a public academic benchmark: 113 images
with paired depth maps and hand-annotated defect ground-truth masks, published by
Northeastern University (China). Source: https://github.com/neu-rail-rsdds/rsdds
Cite (per the source repo):
  M. Niu, K. Song, L. Huang, Q. Wang, Y. Yan and Q. Meng, "Unsupervised Saliency
  Detection of Rail Surface Defects Using Stereoscopic Images," IEEE Trans. on
  Industrial Informatics, vol. 17, no. 3, pp. 2271-2281, March 2021.

The dataset is split across several GitHub-hosted zip parts (to stay under
GitHub's per-file size limit) and password-protected with the password the
authors publish in their own README ("neurail"). This script downloads the
parts, reassembles each zip, extracts it, and cleans up the intermediate files.

Safe to re-run: skips extraction if the target folder already has files.
"""
import shutil
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "https://raw.githubusercontent.com/neu-rail-rsdds/rsdds/dataset_link/"
PASSWORD = "neurail"

OUT_DIR = Path(__file__).resolve().parent.parent / "datasets" / "raw" / "rail_ndt" / "rsdds"
TMP_DIR = OUT_DIR / "_download_tmp"

# (zip part filenames as hosted on GitHub, output subfolder name)
ARCHIVES = {
    "2D_Image": [f"2D_Image.zip.{i:03d}" for i in range(1, 10)],
    "Depthmap": [f"Depthmap.zip.{i:03d}" for i in range(1, 6)],
    "GroundTruth": ["Ground Truth.zip"],
}


def download(name: str, dest: Path):
    url = BASE_URL + urllib.parse.quote(name)
    print(f"downloading {name} ...")
    urllib.request.urlretrieve(url, dest)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    for label, parts in ARCHIVES.items():
        extract_dir = OUT_DIR / label
        if extract_dir.exists() and any(extract_dir.iterdir()):
            print(f"skip {label}: already extracted at {extract_dir}")
            continue

        part_paths = []
        for part in parts:
            dest = TMP_DIR / part
            if not dest.exists():
                download(part, dest)
            part_paths.append(dest)

        combined_zip = TMP_DIR / f"{label}.zip"
        print(f"reassembling {label}.zip from {len(part_paths)} part(s)")
        with open(combined_zip, "wb") as out:
            for p in part_paths:
                out.write(p.read_bytes())

        extract_dir.mkdir(parents=True, exist_ok=True)
        print(f"extracting {label}.zip -> {extract_dir}")
        subprocess.run(
            ["unzip", "-q", "-o", "-P", PASSWORD, str(combined_zip), "-d", str(extract_dir)],
            check=True,
        )

    shutil.rmtree(TMP_DIR, ignore_errors=True)
    print(f"done. RSDDs extracted under {OUT_DIR}")


if __name__ == "__main__":
    main()
