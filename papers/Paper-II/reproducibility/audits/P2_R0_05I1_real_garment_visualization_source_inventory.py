from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


# =============================================================================
# P2-R0-05I1 — REAL GARMENT VISUALIZATION SOURCE INVENTORY
#
# Purpose:
#   Prepare Canvas v0.4 without guessing paths or schemas.
#
#   This probe searches only the established Paper-II research roots for:
#     - RAW population / runtime-linked manifests
#     - V1_TEXT_ONLY manifests
#     - V3_CROP_ONLY manifests
#     - CLEAN manifests
#     - 05G2 spectral diagnostic CSVs
#     - 05H4B2 identity summaries
#
#   It inventories candidate CSV/manifest files and prints their schemas.
#
# No scientific calculation.
# No image selection.
# No artifact mutation.
# =============================================================================


SEARCH_ROOTS = [
    Path("/Users/nitikagupta/Research"),
    Path("/Users/nitikagupta/Research/WeaveAI/papers/Paper-II"),
]

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas"
)

INVENTORY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I1_source_inventory.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05I1_report.json"
)

NAME_HINTS = [
    "05g2",
    "05h4b2",
    "text_only",
    "crop_only",
    "clean",
    "manifest",
    "spectral",
    "identity",
]

MAX_BYTES = 50 * 1024 * 1024


def interesting(path: Path) -> bool:
    low = path.name.lower()

    if path.suffix.lower() not in {".csv", ".json"}:
        return False

    return any(
        hint in low
        for hint in NAME_HINTS
    )


def csv_schema(path: Path):
    try:
        df = pd.read_csv(
            path,
            nrows=5,
            keep_default_na=False,
        )
    except Exception as exc:
        return {
            "read_status": f"ERROR: {type(exc).__name__}: {exc}",
            "columns": "",
            "preview_rows": "",
        }

    return {
        "read_status": "PASS",
        "columns": " | ".join(
            map(
                str,
                df.columns.tolist(),
            )
        ),
        "preview_rows": repr(
            df.head(2).to_dict(
                orient="records"
            )
        )[:2000],
    }


def main():

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    if INVENTORY_CSV.exists():
        raise RuntimeError(
            f"Refusing to overwrite: {INVENTORY_CSV}"
        )

    if REPORT_JSON.exists():
        raise RuntimeError(
            f"Refusing to overwrite: {REPORT_JSON}"
        )

    seen = set()
    rows = []

    for root in SEARCH_ROOTS:

        if not root.exists():
            continue

        for path in root.rglob("*"):

            if not path.is_file():
                continue

            resolved = str(
                path.resolve()
            )

            if resolved in seen:
                continue

            seen.add(
                resolved
            )

            if not interesting(
                path
            ):
                continue

            size = path.stat().st_size

            if size > MAX_BYTES:
                rows.append(
                    {
                        "path":
                            resolved,

                        "filename":
                            path.name,

                        "suffix":
                            path.suffix.lower(),

                        "size_bytes":
                            size,

                        "read_status":
                            "SKIP_TOO_LARGE",

                        "columns":
                            "",

                        "preview_rows":
                            "",
                    }
                )
                continue

            if path.suffix.lower() == ".csv":
                info = csv_schema(
                    path
                )
            else:
                info = {
                    "read_status":
                        "JSON_NOT_EXPANDED",

                    "columns":
                        "",

                    "preview_rows":
                        "",
                }

            rows.append(
                {
                    "path":
                        resolved,

                    "filename":
                        path.name,

                    "suffix":
                        path.suffix.lower(),

                    "size_bytes":
                        size,

                    **info,
                }
            )

    inventory = pd.DataFrame(
        rows
    ).sort_values(
        [
            "filename",
            "path",
        ]
    ).reset_index(
        drop=True
    )

    inventory.to_csv(
        INVENTORY_CSV,
        index=False,
    )

    print(
        "=" * 140
    )

    print(
        "P2-R0-05I1 — REAL GARMENT VISUALIZATION SOURCE INVENTORY"
    )

    print(
        "=" * 140
    )

    if len(
        inventory
    ) == 0:
        print(
            "No candidate files found."
        )
    else:
        print(
            inventory[
                [
                    "filename",
                    "read_status",
                    "columns",
                    "path",
                ]
            ].to_string(
                index=False
            )
        )

    # Highlight files most likely to be useful for v0.4.
    likely = inventory[
        inventory[
            "filename"
        ].str.lower().str.contains(
            "05g2|text_only|crop_only|manifest|identity",
            regex=True,
        )
    ].copy()

    print(
        "\n"
        + "=" * 140
    )

    print(
        "P2-R0-05I1 — LIKELY V0.4 INPUTS"
    )

    print(
        "=" * 140
    )

    if len(
        likely
    ) == 0:
        print(
            "No likely inputs identified."
        )
    else:
        print(
            likely[
                [
                    "filename",
                    "columns",
                    "path",
                ]
            ].to_string(
                index=False
            )
        )

    report = {
        "stage":
            "P2_R0_05I1_REAL_GARMENT_VISUALIZATION_SOURCE_INVENTORY",

        "status":
            "COMPLETE",

        "candidate_file_count":
            int(
                len(
                    inventory
                )
            ),

        "likely_input_count":
            int(
                len(
                    likely
                )
            ),

        "inventory_csv":
            str(
                INVENTORY_CSV
            ),

        "interpretation_boundary":
            (
                "This stage inventories existing real-data audit sources only. "
                "It does not select examples, calculate spectra, or modify "
                "Paper-II artifacts."
            ),
    }

    REPORT_JSON.write_text(
        json.dumps(
            report,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "\nP2-R0-05I1 SOURCE INVENTORY: COMPLETE"
    )

    print(
        "Inventory CSV:",
        INVENTORY_CSV,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — use observed paths/schemas to build 05I2 candidate selection."
    )


if __name__ == "__main__":
    main()