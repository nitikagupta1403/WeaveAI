#!/usr/bin/env python3
"""Export frozen manuscript-reported values as audit tables, without inference."""

import argparse
import csv
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--values", type=Path, default=Path(__file__).with_name("frozen_reported_values.json"))
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    payload = json.loads(args.values.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    radial_path = args.output_dir / "radial_representation.csv"
    rows = payload["radial_representation"]
    with radial_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    for key in ("representation_dimensions", "latent_summary", "pca64_localization"):
        (args.output_dir / f"{key}.json").write_text(
            json.dumps(payload[key], indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    print(f"Exported frozen reported-value tables to {args.output_dir}")


if __name__ == "__main__":
    main()
