from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05H4A — FOLD-3 EFFECT-TABLE STRUCTURE PROBE
#
# Purpose:
#   Before writing the fold-3 category/identity decomposition, inspect the
#   exact frozen replay objects returned by replay_cell13_selection().
#
# Why a probe first:
#   05H3 established that INTRINSIC fold 3 has a real low/mid training-MRR
#   elevation, but the internal effect-table schema is not yet frozen in our
#   audit notes. We do not guess column names or reconstruct retrieval logic.
#
# This script:
#   - verifies RAW / CROP_ONLY / INTRINSIC provenance
#   - replays Cell-13 selection exactly
#   - recursively inspects the returned effect_tables object for each dataset
#   - exports every DataFrame leaf unchanged
#   - writes a compact schema inventory
#
# No tuning. No inference. No exclusion. No decomposition claim yet.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)

H1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate"
)

H1_FIELD_NPZ = (
    H1_ROOT
    / "P2_R0_05H1_intrinsic_coordinate_field.npz"
)

EXPECTED_H1_FIELD_SHA256 = (
    "aaa69c8a6a416979dc037ae6c0197d5c62f1959eb41cc0482c8b5a3bdde21c03"
)

CROP_ONLY_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_vs_resampling/"
    "V3_CROP_ONLY"
)

CROP_ONLY_MANIFEST = (
    CROP_ONLY_ROOT
    / "materialized_manifest.csv"
)

EXPECTED_CROP_ONLY_MANIFEST_SHA256 = (
    "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e"
)

EXPECTED_ROWS = 2300

OUTPUT_ROOT = (
    H1_ROOT
    / "P2_R0_05H4A_effect_table_probe"
)

SCHEMA_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4A_effect_table_schema.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05H4A_report.json"
)


# =============================================================================
# Helpers
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
            h.update(chunk)
    return h.hexdigest()


def load_verified_definitions():

    if not BASE_AUDIT.is_file():
        raise RuntimeError(
            f"Base audit missing: {BASE_AUDIT}"
        )

    source = BASE_AUDIT.read_text(
        encoding="utf-8"
    )

    marker = 'if __name__ == "__main__":'

    if marker not in source:
        raise RuntimeError(
            "Could not locate __main__ boundary"
        )

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
        "load_and_validate_fold_package",
        "replay_cell13_selection",
        "normalize_runtime_relative_path",
    ]

    missing = [
        name
        for name in required
        if name not in namespace
    ]

    if missing:
        raise RuntimeError(
            f"Missing verified definitions: {missing}"
        )

    print(
        "P2-R0-05H4A VERIFIED DEFINITIONS: PASS"
    )

    return namespace


def validate_intrinsic(
    runtime: dict,
    normalize_runtime_relative_path,
):

    if not H1_FIELD_NPZ.is_file():
        raise RuntimeError(
            "05H1 intrinsic NPZ missing"
        )

    if sha256_file(
        H1_FIELD_NPZ
    ) != EXPECTED_H1_FIELD_SHA256:
        raise RuntimeError(
            "05H1 intrinsic NPZ SHA mismatch"
        )

    artifact = np.load(
        H1_FIELD_NPZ,
        allow_pickle=False,
    )

    field = np.asarray(
        artifact[
            "conditional_angular"
        ],
        dtype=np.float64,
    )

    radial_centers = np.asarray(
        artifact[
            "radial_centers"
        ],
        dtype=np.float64,
    )

    paths = np.asarray(
        artifact[
            "relative_paths"
        ],
        dtype=str,
    )

    runtime_paths = np.asarray(
        [
            normalize_runtime_relative_path(x)
            for x in runtime[
                "image_paths"
            ]
        ],
        dtype=str,
    )

    if field.shape != (
        EXPECTED_ROWS,
        72,
        72,
    ):
        raise RuntimeError(
            f"Unexpected intrinsic field shape: {field.shape}"
        )

    if not np.array_equal(
        paths,
        runtime_paths,
    ):
        raise RuntimeError(
            "Intrinsic/runtime population-order mismatch"
        )

    return (
        np.fft.rfft(
            field,
            axis=2,
        ),
        radial_centers,
    )


def reconstruct_crop(
    runtime: dict,
    ra14_module,
    normalize_runtime_relative_path,
):

    if not CROP_ONLY_MANIFEST.is_file():
        raise RuntimeError(
            "CROP_ONLY manifest missing"
        )

    if sha256_file(
        CROP_ONLY_MANIFEST
    ) != EXPECTED_CROP_ONLY_MANIFEST_SHA256:
        raise RuntimeError(
            "CROP_ONLY manifest SHA mismatch"
        )

    manifest = pd.read_csv(
        CROP_ONLY_MANIFEST,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    runtime_paths = np.asarray(
        [
            normalize_runtime_relative_path(x)
            for x in runtime[
                "image_paths"
            ]
        ],
        dtype=str,
    )

    manifest_paths = manifest[
        "relative_path"
    ].astype(str).to_numpy()

    if not np.array_equal(
        runtime_paths,
        manifest_paths,
    ):
        raise RuntimeError(
            "CROP_ONLY population-order mismatch"
        )

    categories = np.asarray(
        runtime[
            "image_categories"
        ],
        dtype=str,
    )

    rows = []

    for i, rec in manifest.iterrows():

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
                        categories[
                            i
                        ]
                    ),

                "path":
                    (
                        CROP_ONLY_ROOT
                        / str(
                            rec[
                                "output_relative_path"
                            ]
                        )
                    ),
            }
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

    print(
        "P2-R0-05H4A CROP_ONLY RECONSTRUCTION: PASS"
    )

    print(
        "Max mass error:",
        mass_error,
    )

    print(
        "Max normalization error:",
        norm_error,
    )

    return np.fft.rfft(
        np.asarray(
            conditional,
            dtype=np.float64,
        ),
        axis=2,
    )


def safe_name(text: str) -> str:
    out = []

    for ch in str(text):
        if ch.isalnum() or ch in (
            "-",
            "_",
        ):
            out.append(ch)
        else:
            out.append("_")

    return "".join(out)


def describe_leaf(
    dataset: str,
    path_tokens: list[str],
    value,
    rows: list[dict],
):

    object_path = "/".join(
        path_tokens
    )

    if isinstance(
        value,
        pd.DataFrame,
    ):

        csv_name = (
            f"{safe_name(dataset)}__"
            f"{safe_name(object_path)}.csv"
        )

        csv_path = (
            OUTPUT_ROOT
            / csv_name
        )

        value.to_csv(
            csv_path,
            index=False,
        )

        rows.append(
            {
                "dataset":
                    dataset,

                "object_path":
                    object_path,

                "object_type":
                    "DataFrame",

                "shape":
                    str(
                        value.shape
                    ),

                "columns":
                    " | ".join(
                        map(
                            str,
                            value.columns.tolist(),
                        )
                    ),

                "dtype":
                    "",

                "preview":
                    "",

                "exported_csv":
                    str(
                        csv_path
                    ),

                "exported_csv_sha256":
                    sha256_file(
                        csv_path
                    ),
            }
        )

        return

    if isinstance(
        value,
        pd.Series,
    ):

        rows.append(
            {
                "dataset":
                    dataset,

                "object_path":
                    object_path,

                "object_type":
                    "Series",

                "shape":
                    str(
                        value.shape
                    ),

                "columns":
                    str(
                        value.name
                    ),

                "dtype":
                    str(
                        value.dtype
                    ),

                "preview":
                    repr(
                        value.head(
                            5
                        ).tolist()
                    ),

                "exported_csv":
                    "",

                "exported_csv_sha256":
                    "",
            }
        )

        return

    if isinstance(
        value,
        np.ndarray,
    ):

        preview = repr(
            value.ravel()[
                :8
            ].tolist()
        )

        rows.append(
            {
                "dataset":
                    dataset,

                "object_path":
                    object_path,

                "object_type":
                    "ndarray",

                "shape":
                    str(
                        value.shape
                    ),

                "columns":
                    "",

                "dtype":
                    str(
                        value.dtype
                    ),

                "preview":
                    preview,

                "exported_csv":
                    "",

                "exported_csv_sha256":
                    "",
            }
        )

        return

    rows.append(
        {
            "dataset":
                dataset,

            "object_path":
                object_path,

            "object_type":
                type(
                    value
                ).__name__,

            "shape":
                "",

            "columns":
                "",

            "dtype":
                "",

            "preview":
                repr(
                    value
                )[
                    :500
                ],

            "exported_csv":
                "",

            "exported_csv_sha256":
                "",
        }
    )


def walk_object(
    dataset: str,
    value,
    path_tokens: list[str],
    rows: list[dict],
):

    if isinstance(
        value,
        dict,
    ):

        rows.append(
            {
                "dataset":
                    dataset,

                "object_path":
                    "/".join(
                        path_tokens
                    ),

                "object_type":
                    "dict",

                "shape":
                    f"len={len(value)}",

                "columns":
                    "",

                "dtype":
                    "",

                "preview":
                    "keys="
                    + repr(
                        list(
                            value.keys()
                        )[
                            :30
                        ]
                    ),

                "exported_csv":
                    "",

                "exported_csv_sha256":
                    "",
            }
        )

        for key, child in value.items():
            walk_object(
                dataset,
                child,
                path_tokens
                + [
                    str(
                        key
                    )
                ],
                rows,
            )

        return

    if isinstance(
        value,
        (list, tuple),
    ):

        rows.append(
            {
                "dataset":
                    dataset,

                "object_path":
                    "/".join(
                        path_tokens
                    ),

                "object_type":
                    type(
                        value
                    ).__name__,

                "shape":
                    f"len={len(value)}",

                "columns":
                    "",

                "dtype":
                    "",

                "preview":
                    "",

                "exported_csv":
                    "",

                "exported_csv_sha256":
                    "",
            }
        )

        for i, child in enumerate(
            value
        ):
            walk_object(
                dataset,
                child,
                path_tokens
                + [
                    str(
                        i
                    )
                ],
                rows,
            )

        return

    describe_leaf(
        dataset,
        path_tokens,
        value,
        rows,
    )


# =============================================================================
# Main
# =============================================================================

def main():

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    if SCHEMA_CSV.exists():
        raise RuntimeError(
            f"Refusing to overwrite: {SCHEMA_CSV}"
        )

    if REPORT_JSON.exists():
        raise RuntimeError(
            f"Refusing to overwrite: {REPORT_JSON}"
        )

    base = load_verified_definitions()

    runtime = (
        base[
            "load_paper2_runtime"
        ]()
    )

    (
        ra14_module,
        raw_conditional,
    ) = (
        base[
            "validate_geometry_equivalence"
        ](
            runtime
        )
    )

    raw_fft = np.fft.rfft(
        raw_conditional,
        axis=2,
    )

    (
        G,
        C,
        folds,
        fold_sha,
    ) = (
        base[
            "load_and_validate_fold_package"
        ](
            runtime
        )
    )

    crop_fft = reconstruct_crop(
        runtime,
        ra14_module,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    (
        intrinsic_fft,
        intrinsic_radial_centers,
    ) = validate_intrinsic(
        runtime,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    raw_radial_centers = np.asarray(
        runtime[
            "radial_centers"
        ],
        dtype=np.float64,
    )

    replay = (
        base[
            "replay_cell13_selection"
        ]
    )

    datasets = {}

    for label, fft, radial_centers in [
        (
            "RAW",
            raw_fft,
            raw_radial_centers,
        ),
        (
            "V3_CROP_ONLY",
            crop_fft,
            raw_radial_centers,
        ),
        (
            "INTRINSIC",
            intrinsic_fft,
            intrinsic_radial_centers,
        ),
    ]:

        print(
            f"\nP2-R0-05H4A — replaying {label}"
        )

        (
            selection,
            effect_tables,
        ) = replay(
            fft,
            radial_centers,
            G,
            C,
            folds,
            f"{label}_H4A",
        )

        datasets[
            label
        ] = {
            "selection":
                selection,

            "effect_tables":
                effect_tables,
        }

    schema_rows = []

    for dataset, objects in datasets.items():

        walk_object(
            dataset,
            objects[
                "selection"
            ],
            [
                "selection"
            ],
            schema_rows,
        )

        walk_object(
            dataset,
            objects[
                "effect_tables"
            ],
            [
                "effect_tables"
            ],
            schema_rows,
        )

    schema = pd.DataFrame(
        schema_rows
    )

    schema.to_csv(
        SCHEMA_CSV,
        index=False,
    )

    schema_sha = sha256_file(
        SCHEMA_CSV
    )

    print(
        "\n"
        + "=" * 140
    )

    print(
        "P2-R0-05H4A — EFFECT TABLE SCHEMA INVENTORY"
    )

    print(
        "=" * 140
    )

    display_cols = [
        "dataset",
        "object_path",
        "object_type",
        "shape",
        "columns",
    ]

    print(
        schema[
            display_cols
        ].to_string(
            index=False
        )
    )

    dataframe_rows = schema[
        schema[
            "object_type"
        ]
        == "DataFrame"
    ].copy()

    print(
        "\nP2-R0-05H4A — EXPORTED DATAFRAME LEAVES"
    )

    if len(
        dataframe_rows
    ) == 0:
        print(
            "No DataFrame leaves found."
        )
    else:
        print(
            dataframe_rows[
                [
                    "dataset",
                    "object_path",
                    "shape",
                    "columns",
                    "exported_csv",
                ]
            ].to_string(
                index=False
            )
        )

    report = {
        "stage":
            "P2_R0_05H4A_EFFECT_TABLE_STRUCTURE_PROBE",

        "status":
            "COMPLETE",

        "rows":
            EXPECTED_ROWS,

        "fold_package_sha256":
            fold_sha,

        "h1_field_sha256":
            EXPECTED_H1_FIELD_SHA256,

        "schema_csv_sha256":
            schema_sha,

        "dataframe_leaf_count":
            int(
                len(
                    dataframe_rows
                )
            ),

        "interpretation_boundary":
            (
                "This probe only inventories the exact effect-table schema "
                "returned by the frozen selection replay. It performs no "
                "fold-3 category/identity decomposition and makes no "
                "scientific claim."
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
        "\nP2-R0-05H4A EFFECT-TABLE "
        "STRUCTURE PROBE: COMPLETE"
    )

    print(
        "Schema CSV:",
        SCHEMA_CSV,
    )

    print(
        "Schema CSV SHA-256:",
        schema_sha,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — schema frozen. "
        "Build 05H4B only from observed structure."
    )


if __name__ == "__main__":
    main()