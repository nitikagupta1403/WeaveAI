from __future__ import annotations

import base64
import hashlib
import io
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageOps


# =============================================================================
# P2-R0-05I5 — FROZEN TEXT-POSITIVE CONTROL EXPORT
#
# Controls frozen after visual verification:
#   Primary   : Mermaid/1_1.tif
#   Secondary : Mini/1_4.tif
#
# Goal
# ----
# Quantify and export, for each control:
#
#   RAW -> TEXT_ONLY
#   TEXT_ONLY -> CROP_ONLY
#
# using the same radial-angular representation as Paper II.
#
# This stage does NOT replace the 05I2 crop/support exemplars.
# It creates a separate text-removal control package.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)

TEXT_CONTROLS = [
    {
        "role": "PRIMARY_TEXT_CONTROL",
        "relative_path": "Mermaid/1_1.tif",
    },
    {
        "role": "SECONDARY_TEXT_CONTROL",
        "relative_path": "Mini/1_4.tif",
    },
]

V1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05e_preprocessing_ablation/"
    "V1_TEXT_ONLY"
)

V1_MANIFEST = (
    V1_ROOT
    / "materialized_manifest.csv"
)

V3_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_vs_resampling/"
    "V3_CROP_ONLY"
)

V3_MANIFEST = (
    V3_ROOT
    / "materialized_manifest.csv"
)

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I5_text_controls"
)

SUMMARY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I5_text_control_summary.csv"
)

JSON_OUT = (
    OUTPUT_ROOT
    / "P2_R0_05I5_text_control_canvas.json"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05I5_report.json"
)

BANDS = {
    "low_1_4": np.arange(1, 5, dtype=int),
    "mid_5_12": np.arange(5, 13, dtype=int),
    "highmid_13_24": np.arange(13, 25, dtype=int),
    "high_25_36": np.arange(25, 37, dtype=int),
}


# =============================================================================
# Helpers
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_verified_definitions():
    source = BASE_AUDIT.read_text(encoding="utf-8")
    marker = 'if __name__ == "__main__":'

    namespace = {
        "__file__": str(BASE_AUDIT),
        "__name__": "p2_r0_05_verified_definitions",
    }

    exec(
        compile(
            source.split(marker, 1)[0],
            str(BASE_AUDIT),
            "exec",
        ),
        namespace,
    )

    required = [
        "load_paper2_runtime",
        "validate_geometry_equivalence",
        "normalize_runtime_relative_path",
    ]

    missing = [x for x in required if x not in namespace]

    if missing:
        raise RuntimeError(
            f"Missing verified definitions: {missing}"
        )

    print("P2-R0-05I5 VERIFIED DEFINITIONS: PASS")

    return namespace


def reconstruct_full_variant(
    ra14_module,
    runtime_paths: np.ndarray,
    runtime_categories: np.ndarray,
    manifest_path: Path,
    root: Path,
    label: str,
) -> np.ndarray:

    manifest = pd.read_csv(
        manifest_path,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    manifest_paths = manifest[
        "relative_path"
    ].astype(str).to_numpy()

    if not np.array_equal(
        runtime_paths,
        manifest_paths,
    ):
        raise RuntimeError(
            f"{label} manifest/runtime order mismatch"
        )

    rows = []

    for i, rec in manifest.iterrows():

        p = (
            root
            / str(
                rec[
                    "output_relative_path"
                ]
            )
        )

        if not p.is_file():
            raise RuntimeError(
                f"Missing {label} image: {p}"
            )

        rows.append(
            {
                "relative_path":
                    str(
                        rec[
                            "relative_path"
                        ]
                    ),

                "category":
                    str(
                        runtime_categories[
                            i
                        ]
                    ),

                "path":
                    p,
            }
        )

    print(
        f"\nP2-R0-05I5 — reconstructing full {label} geometry..."
    )

    (
        conditional,
        _nonempty,
        _radial_centers,
        mass_error,
        norm_error,
    ) = ra14_module.recover_geometry(
        rows
    )

    conditional = np.asarray(
        conditional,
        dtype=np.float64,
    )

    if conditional.shape != (
        len(runtime_paths),
        72,
        72,
    ):
        raise RuntimeError(
            f"Unexpected {label} field shape: {conditional.shape}"
        )

    if not np.isfinite(
        conditional
    ).all():
        raise RuntimeError(
            f"{label} field contains non-finite values"
        )

    print(
        f"P2-R0-05I5 {label} FULL RECONSTRUCTION: PASS"
    )

    print(
        "Max mass error:",
        mass_error,
    )

    print(
        "Max normalization error:",
        norm_error,
    )

    return conditional


def field_metrics(field: np.ndarray) -> dict:
    field = np.asarray(
        field,
        dtype=np.float64,
    )

    F = np.fft.rfft(
        field,
        axis=1,
    )

    mag = np.abs(F)
    energy = mag ** 2

    harmonic_energy = energy.sum(
        axis=0
    )

    non_dc_total = float(
        harmonic_energy[
            1:37
        ].sum()
    )

    if non_dc_total <= 0:
        raise RuntimeError(
            "Non-positive non-DC energy"
        )

    band_fraction = {}

    for name, ks in BANDS.items():
        band_fraction[
            name
        ] = float(
            harmonic_energy[
                ks
            ].sum()
            / non_dc_total
        )

    return {
        "radial_histogram":
            field.sum(
                axis=1
            ).tolist(),

        "fft_magnitude_by_harmonic":
            mag.sum(
                axis=0
            ).tolist(),

        "band_fraction":
            band_fraction,
    }


def image_data_uri(path: Path) -> str:
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(
            im
        ).convert(
            "L"
        )

        buf = io.BytesIO()

        im.save(
            buf,
            format="PNG",
            optimize=True,
        )

    return (
        "data:image/png;base64,"
        + base64.b64encode(
            buf.getvalue()
        ).decode(
            "ascii"
        )
    )


def resolve_raw_display_path(
    historical_runtime_path: Path,
    relative_path: str,
    expected_source_sha256: str,
) -> Path:

    expected_source_sha256 = str(
        expected_source_sha256
    ).strip()

    def verified(
        p: Path
    ) -> bool:
        return (
            p.is_file()
            and
            (
                not expected_source_sha256
                or sha256_file(
                    p
                )
                == expected_source_sha256
            )
        )

    if verified(
        historical_runtime_path
    ):
        return historical_runtime_path

    rel = Path(
        relative_path
    )

    roots = [
        Path(
            "/Users/nitikagupta/Desktop/Clo-Sket"
        ),
        Path(
            "/Users/nitikagupta/Research"
        ),
        Path(
            "/Users/nitikagupta/Desktop"
        ),
    ]

    candidates = [
        roots[0]
        / rel,
    ]

    for root in roots[1:]:
        candidates.extend(
            [
                root
                / rel,

                root
                / "WeaveAI"
                / rel,

                root
                / "FashionAI"
                / "datasets"
                / "Clo-Sket"
                / "Clo-Sket"
                / rel,
            ]
        )

    hits = [
        p.resolve()
        for p in candidates
        if verified(
            p
        )
    ]

    hits = sorted(
        set(
            hits
        )
    )

    if hits:
        return Path(
            hits[
                0
            ]
        )

    suffix = str(
        rel
    ).replace(
        "\\",
        "/",
    )

    for root in roots:

        if not root.exists():
            continue

        for p in root.rglob(
            rel.name
        ):

            p_norm = str(
                p
            ).replace(
                "\\",
                "/",
            )

            if not p_norm.endswith(
                suffix
            ):
                continue

            if verified(
                p
            ):
                hits.append(
                    p.resolve()
                )

    hits = sorted(
        set(
            hits
        )
    )

    if not hits:
        raise RuntimeError(
            f"Could not resolve RAW display raster for {relative_path}"
        )

    return Path(
        hits[
            0
        ]
    )


def manifest_maps(
    manifest_path: Path,
    root: Path,
):
    df = pd.read_csv(
        manifest_path,
        keep_default_na=False,
    )

    path_map = {}

    sha_map = {}

    for _, rec in df.iterrows():

        rel = str(
            rec[
                "relative_path"
            ]
        )

        path_map[
            rel
        ] = (
            root
            / str(
                rec[
                    "output_relative_path"
                ]
            )
        )

        sha_map[
            rel
        ] = str(
            rec[
                "source_sha256"
            ]
        )

    return df, path_map, sha_map


def compare(
    before: dict,
    after: dict,
):
    band_delta = {}

    for band in BANDS:
        band_delta[
            band
        ] = (
            after[
                "band_fraction"
            ][
                band
            ]
            -
            before[
                "band_fraction"
            ][
                band
            ]
        )

    l1 = float(
        sum(
            abs(
                x
            )
            for x in band_delta.values()
        )
    )

    return {
        "band_delta":
            band_delta,

        "band_l1_change":
            l1,
    }


# =============================================================================
# Main
# =============================================================================

def main():

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for p in (
        SUMMARY_CSV,
        JSON_OUT,
        REPORT_JSON,
    ):
        if p.exists():
            raise RuntimeError(
                f"Refusing to overwrite: {p}"
            )

    base = load_verified_definitions()

    runtime = base[
        "load_paper2_runtime"
    ]()

    (
        ra14_module,
        raw_conditional,
    ) = base[
        "validate_geometry_equivalence"
    ](
        runtime
    )

    runtime_paths = np.asarray(
        [
            base[
                "normalize_runtime_relative_path"
            ](
                x
            )
            for x in runtime[
                "image_paths"
            ]
        ],
        dtype=str,
    )

    runtime_categories = np.asarray(
        runtime[
            "image_categories"
        ],
        dtype=str,
    )

    historical_raw_paths = [
        Path(
            x
        )
        for x in runtime[
            "image_paths"
        ]
    ]

    (
        v1_df,
        v1_path_map,
        v1_sha_map,
    ) = manifest_maps(
        V1_MANIFEST,
        V1_ROOT,
    )

    (
        v3_df,
        v3_path_map,
        _v3_sha_map,
    ) = manifest_maps(
        V3_MANIFEST,
        V3_ROOT,
    )

    text_conditional = reconstruct_full_variant(
        ra14_module,
        runtime_paths,
        runtime_categories,
        V1_MANIFEST,
        V1_ROOT,
        "TEXT_ONLY",
    )

    crop_conditional = reconstruct_full_variant(
        ra14_module,
        runtime_paths,
        runtime_categories,
        V3_MANIFEST,
        V3_ROOT,
        "CROP_ONLY",
    )

    path_to_idx = {
        p:
            i
        for i, p in enumerate(
            runtime_paths
        )
    }

    payload = {
        "version":
            "0.4.1-text-controls-v1",

        "scientific_source":
            "Python",

        "selection_basis":
            (
                "Controls frozen after visual verification of the 05I4 "
                "RAW|TEXT_ONLY contact sheet."
            ),

        "controls":
            [],
    }

    summary_rows = []

    for control in TEXT_CONTROLS:

        rel = control[
            "relative_path"
        ]

        if rel not in path_to_idx:
            raise RuntimeError(
                f"Control path not found in runtime: {rel}"
            )

        idx = int(
            path_to_idx[
                rel
            ]
        )

        if rel not in v1_path_map:
            raise RuntimeError(
                f"TEXT_ONLY path missing: {rel}"
            )

        if rel not in v3_path_map:
            raise RuntimeError(
                f"CROP_ONLY path missing: {rel}"
            )

        raw_path = resolve_raw_display_path(
            historical_raw_paths[
                idx
            ],
            rel,
            v1_sha_map[
                rel
            ],
        )

        text_path = v1_path_map[
            rel
        ]

        crop_path = v3_path_map[
            rel
        ]

        raw_metrics = field_metrics(
            raw_conditional[
                idx
            ]
        )

        text_metrics = field_metrics(
            text_conditional[
                idx
            ]
        )

        crop_metrics = field_metrics(
            crop_conditional[
                idx
            ]
        )

        raw_to_text = compare(
            raw_metrics,
            text_metrics,
        )

        text_to_crop = compare(
            text_metrics,
            crop_metrics,
        )

        payload[
            "controls"
        ].append(
            {
                "role":
                    control[
                        "role"
                    ],

                "relative_path":
                    rel,

                "row_index":
                    idx,

                "category":
                    str(
                        runtime_categories[
                            idx
                        ]
                    ),

                "stages":
                    {
                        "RAW":
                            {
                                "display_image":
                                    image_data_uri(
                                        raw_path
                                    ),

                                "metrics":
                                    raw_metrics,
                            },

                        "TEXT_ONLY":
                            {
                                "display_image":
                                    image_data_uri(
                                        text_path
                                    ),

                                "metrics":
                                    text_metrics,
                            },

                        "CROP_ONLY":
                            {
                                "display_image":
                                    image_data_uri(
                                        crop_path
                                    ),

                                "metrics":
                                    crop_metrics,
                            },
                    },

                "comparisons":
                    {
                        "RAW_TO_TEXT_ONLY":
                            raw_to_text,

                        "TEXT_ONLY_TO_CROP_ONLY":
                            text_to_crop,
                    },
            }
        )

        for name, comp in [
            (
                "RAW_TO_TEXT_ONLY",
                raw_to_text,
            ),
            (
                "TEXT_ONLY_TO_CROP_ONLY",
                text_to_crop,
            ),
        ]:

            row = {
                "role":
                    control[
                        "role"
                    ],

                "relative_path":
                    rel,

                "row_index":
                    idx,

                "comparison":
                    name,

                "band_l1_change":
                    comp[
                        "band_l1_change"
                    ],
            }

            for band, value in comp[
                "band_delta"
            ].items():
                row[
                    f"delta_{band}"
                ] = value

            summary_rows.append(
                row
            )

    summary = pd.DataFrame(
        summary_rows
    )

    summary.to_csv(
        SUMMARY_CSV,
        index=False,
    )

    JSON_OUT.write_text(
        json.dumps(
            payload,
            indent=2,
        ),
        encoding="utf-8",
    )

    report = {
        "stage":
            "P2_R0_05I5_FROZEN_TEXT_POSITIVE_CONTROL_EXPORT",

        "status":
            "COMPLETE",

        "controls":
            TEXT_CONTROLS,

        "summary_csv":
            str(
                SUMMARY_CSV
            ),

        "canvas_json":
            str(
                JSON_OUT
            ),

        "canvas_json_sha256":
            sha256_file(
                JSON_OUT
            ),

        "interpretation_boundary":
            (
                "These two controls are separate from the 05I2 crop/support "
                "exemplars. RAW->TEXT_ONLY and TEXT_ONLY->CROP_ONLY are "
                "descriptive per-image spectral comparisons."
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
        "=" * 150
    )

    print(
        "P2-R0-05I5 — TEXT-CONTROL SPECTRAL COMPARISON"
    )

    print(
        "=" * 150
    )

    print(
        summary.to_string(
            index=False
        )
    )

    print(
        "\nP2-R0-05I5 TEXT-POSITIVE CONTROL EXPORT: COMPLETE"
    )

    print(
        "Summary CSV:",
        SUMMARY_CSV,
    )

    print(
        "Canvas JSON:",
        JSON_OUT,
    )

    print(
        "Canvas JSON SHA-256:",
        sha256_file(
            JSON_OUT
        ),
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — use this JSON unchanged for Canvas v0.4.1."
    )


if __name__ == "__main__":
    main()