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
# P2-R0-05I3 — REAL GARMENT CANVAS EXPORT
#
# Purpose
# -------
# Freeze one representative sketch for each of the three objectively selected
# garment identities, then export a browser-ready JSON for Canvas v0.4:
#
#   RAW
#   TEXT_ONLY
#   CROP_ONLY
#   INTRINSIC
#
# The scientific quantities are computed in Python.  The browser will only
# visualize this JSON.
#
# Representative sketch rule
# --------------------------
# Within each selected identity, choose the sketch whose RAW->CROP 4-band
# delta vector is closest (Euclidean distance) to that identity's median
# 4-band delta vector.  This avoids picking the most dramatic sketch.
#
# No Paper-II artifact is modified.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)

SELECTED_CSV = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I2_selected_three_identities.csv"
)

PER_IMAGE_CSV = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I2_per_image_band_fraction_change.csv"
)

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

H1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate"
)

H1_NPZ = (
    H1_ROOT
    / "P2_R0_05H1_intrinsic_coordinate_field.npz"
)

EXPECTED_H1_SHA = (
    "aaa69c8a6a416979dc037ae6c0197d5c62f1959eb41cc0482c8b5a3bdde21c03"
)

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I3_canvas_export"
)

REPRESENTATIVE_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I3_representative_sketches.csv"
)

JSON_OUT = (
    OUTPUT_ROOT
    / "P2_R0_05I3_real_garment_canvas.json"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05I3_report.json"
)

BANDS = {
    "low_1_4": np.arange(1, 5, dtype=int),
    "mid_5_12": np.arange(5, 13, dtype=int),
    "highmid_13_24": np.arange(13, 25, dtype=int),
    "high_25_36": np.arange(25, 37, dtype=int),
}

DELTA_COLS = [
    "delta_low_1_4_fraction_crop_minus_raw",
    "delta_mid_5_12_fraction_crop_minus_raw",
    "delta_highmid_13_24_fraction_crop_minus_raw",
    "delta_high_25_36_fraction_crop_minus_raw",
]


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

    return namespace


def image_data_uri(path: Path) -> str:
    """
    Convert any source raster to a compact PNG data URI for browser display.
    This conversion is visualization-only and is not used for scientific metrics.
    """
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im).convert("L")
        buf = io.BytesIO()
        im.save(buf, format="PNG", optimize=True)

    payload = base64.b64encode(
        buf.getvalue()
    ).decode("ascii")

    return "data:image/png;base64," + payload


def field_metrics(field: np.ndarray) -> dict:
    field = np.asarray(
        field,
        dtype=np.float64,
    )

    if field.shape != (72, 72):
        raise RuntimeError(
            f"Unexpected field shape: {field.shape}"
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
        band_fraction[name] = float(
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

        "angular_histogram":
            field.sum(
                axis=0
            ).tolist(),

        "fft_magnitude_by_harmonic":
            mag.sum(
                axis=0
            ).tolist(),

        "band_fraction":
            band_fraction,
    }


def make_single_row_geometry(
    ra14_module,
    relative_path: str,
    category: str,
    path: Path,
):
    rows = [
        {
            "relative_path":
                relative_path,

            "category":
                category,

            "path":
                path,
        }
    ]

    (
        conditional,
        _nonempty,
        _radial_centers,
        mass_error,
        norm_error,
    ) = ra14_module.recover_geometry(
        rows
    )

    if float(
        mass_error
    ) != 0.0:
        raise RuntimeError(
            f"Mass error for {path}: {mass_error}"
        )

    return np.asarray(
        conditional[
            0
        ],
        dtype=np.float64,
    )


def load_manifest_map(
    manifest_path: Path,
    root: Path,
):
    df = pd.read_csv(
        manifest_path,
        keep_default_na=False,
    )

    out = {}

    for _, rec in df.iterrows():
        rel = str(
            rec[
                "relative_path"
            ]
        )

        p = (
            root
            / str(
                rec[
                    "output_relative_path"
                ]
            )
        )

        out[
            rel
        ] = p

    return out


def normalized_image_centroid(path: Path) -> dict:
    """
    Visualization-only foreground centroid from grayscale darkness.
    Uses weight = 255 - grayscale.
    """
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(
            im
        ).convert(
            "L"
        )

        arr = np.asarray(
            im,
            dtype=np.float64,
        )

    weight = (
        255.0
        - arr
    )

    mass = float(
        weight.sum()
    )

    h, w = arr.shape

    if mass <= 0:
        return {
            "cx":
                None,

            "cy":
                None,

            "cx_norm":
                None,

            "cy_norm":
                None,

            "width":
                int(
                    w
                ),

            "height":
                int(
                    h
                ),
        }

    yy, xx = np.indices(
        arr.shape
    )

    cx = float(
        (
            weight
            * xx
        ).sum()
        / mass
    )

    cy = float(
        (
            weight
            * yy
        ).sum()
        / mass
    )

    return {
        "cx":
            cx,

        "cy":
            cy,

        "cx_norm":
            cx
            / w,

        "cy_norm":
            cy
            / h,

        "width":
            int(
                w
            ),

        "height":
            int(
                h
            ),
    }


# =============================================================================
# Main
# =============================================================================

def main():

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for path in (
        REPRESENTATIVE_CSV,
        JSON_OUT,
        REPORT_JSON,
    ):
        if path.exists():
            raise RuntimeError(
                f"Refusing to overwrite: {path}"
            )

    if sha256_file(
        H1_NPZ
    ) != EXPECTED_H1_SHA:
        raise RuntimeError(
            "05H1 intrinsic NPZ SHA mismatch"
        )

    selected = pd.read_csv(
        SELECTED_CSV,
        keep_default_na=False,
    )

    per_image = pd.read_csv(
        PER_IMAGE_CSV,
        keep_default_na=False,
    )

    if len(
        selected
    ) != 3:
        raise RuntimeError(
            "Expected exactly 3 selected identities"
        )

    # -------------------------------------------------------------------------
    # Freeze one representative sketch per identity:
    # closest per-image 4-band delta vector to identity median delta vector.
    # -------------------------------------------------------------------------

    rep_rows = []

    for _, rec in selected.iterrows():

        garment_identity = str(
            rec[
                "garment_identity"
            ]
        )

        rows = per_image[
            per_image[
                "garment_identity"
            ].astype(
                str
            )
            == garment_identity
        ].copy()

        if len(
            rows
        ) == 0:
            raise RuntimeError(
                f"No per-image rows for {garment_identity}"
            )

        median_vec = rows[
            DELTA_COLS
        ].median(
            axis=0
        ).to_numpy(
            dtype=float
        )

        X = rows[
            DELTA_COLS
        ].to_numpy(
            dtype=float
        )

        distance = np.linalg.norm(
            X
            - median_vec[
                None,
                :,
            ],
            axis=1,
        )

        rows[
            "distance_to_identity_median_delta_vector"
        ] = distance

        chosen = rows.sort_values(
            [
                "distance_to_identity_median_delta_vector",
                "row_index",
            ],
            ascending=[
                True,
                True,
            ],
        ).iloc[
            0
        ]

        rep_rows.append(
            {
                "visual_role":
                    str(
                        rec[
                            "visual_role"
                        ]
                    ),

                "garment_identity":
                    garment_identity,

                "category":
                    str(
                        rec[
                            "category"
                        ]
                    ),

                "row_index":
                    int(
                        chosen[
                            "row_index"
                        ]
                    ),

                "relative_path":
                    str(
                        chosen[
                            "relative_path"
                        ]
                    ),

                "distance_to_identity_median_delta_vector":
                    float(
                        chosen[
                            "distance_to_identity_median_delta_vector"
                        ]
                    ),
            }
        )

    reps = pd.DataFrame(
        rep_rows
    )

    reps.to_csv(
        REPRESENTATIVE_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Load exact fields and stage paths.
    # -------------------------------------------------------------------------

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

    raw_paths = [
        Path(
            x
        )
        for x in runtime[
            "image_paths"
        ]
    ]

    # Runtime paths are the scientific RAW source paths.
    for p in raw_paths:
        if not p.is_file():
            raise RuntimeError(
                f"RAW source missing: {p}"
            )

    v1_map = load_manifest_map(
        V1_MANIFEST,
        V1_ROOT,
    )

    v3_map = load_manifest_map(
        V3_MANIFEST,
        V3_ROOT,
    )

    intrinsic_artifact = np.load(
        H1_NPZ,
        allow_pickle=False,
    )

    intrinsic_fields = np.asarray(
        intrinsic_artifact[
            "conditional_angular"
        ],
        dtype=np.float64,
    )

    intrinsic_paths = np.asarray(
        intrinsic_artifact[
            "relative_paths"
        ],
        dtype=str,
    )

    if not np.array_equal(
        runtime_paths,
        intrinsic_paths,
    ):
        raise RuntimeError(
            "Runtime/intrinsic path-order mismatch"
        )

    # -------------------------------------------------------------------------
    # Export browser-ready JSON.
    # -------------------------------------------------------------------------

    payload = {
        "version":
            "0.4-data-v1",

        "scientific_source":
            "Python",

        "representative_rule":
            (
                "Within each objectively selected identity, choose the sketch "
                "whose RAW-to-CROP 4-band delta vector is closest to the "
                "identity median 4-band delta vector."
            ),

        "examples":
            [],
    }

    for _, rep in reps.iterrows():

        idx = int(
            rep[
                "row_index"
            ]
        )

        relative_path = str(
            rep[
                "relative_path"
            ]
        )

        category = str(
            rep[
                "category"
            ]
        )

        if runtime_paths[
            idx
        ] != relative_path:
            raise RuntimeError(
                "Representative row/path mismatch"
            )

        raw_path = raw_paths[
            idx
        ]

        if relative_path not in v1_map:
            raise RuntimeError(
                f"TEXT_ONLY path missing for {relative_path}"
            )

        if relative_path not in v3_map:
            raise RuntimeError(
                f"CROP_ONLY path missing for {relative_path}"
            )

        text_path = v1_map[
            relative_path
        ]

        crop_path = v3_map[
            relative_path
        ]

        text_field = make_single_row_geometry(
            ra14_module,
            relative_path,
            category,
            text_path,
        )

        crop_field = make_single_row_geometry(
            ra14_module,
            relative_path,
            category,
            crop_path,
        )

        raw_field = np.asarray(
            raw_conditional[
                idx
            ],
            dtype=np.float64,
        )

        intrinsic_field = np.asarray(
            intrinsic_fields[
                idx
            ],
            dtype=np.float64,
        )

        stages = {
            "RAW":
                {
                    "display_image":
                        image_data_uri(
                            raw_path
                        ),

                    "display_centroid":
                        normalized_image_centroid(
                            raw_path
                        ),

                    "metrics":
                        field_metrics(
                            raw_field
                        ),
                },

            "TEXT_ONLY":
                {
                    "display_image":
                        image_data_uri(
                            text_path
                        ),

                    "display_centroid":
                        normalized_image_centroid(
                            text_path
                        ),

                    "metrics":
                        field_metrics(
                            text_field
                        ),
                },

            "CROP_ONLY":
                {
                    "display_image":
                        image_data_uri(
                            crop_path
                        ),

                    "display_centroid":
                        normalized_image_centroid(
                            crop_path
                        ),

                    "metrics":
                        field_metrics(
                            crop_field
                        ),
                },

            "INTRINSIC":
                {
                    # No separate raster is claimed for the intrinsic field.
                    # Use the CROP_ONLY object pixels as visual context only.
                    "display_image":
                        image_data_uri(
                            crop_path
                        ),

                    "display_centroid":
                        normalized_image_centroid(
                            crop_path
                        ),

                    "image_context_note":
                        (
                            "CROP_ONLY raster shown only as object context; "
                            "metrics come from the 05H1 intrinsic field."
                        ),

                    "metrics":
                        field_metrics(
                            intrinsic_field
                        ),
                },
        }

        payload[
            "examples"
        ].append(
            {
                "visual_role":
                    str(
                        rep[
                            "visual_role"
                        ]
                    ),

                "garment_identity":
                    str(
                        rep[
                            "garment_identity"
                        ]
                    ),

                "category":
                    category,

                "row_index":
                    idx,

                "relative_path":
                    relative_path,

                "representative_distance":
                    float(
                        rep[
                            "distance_to_identity_median_delta_vector"
                        ]
                    ),

                "stages":
                    stages,
            }
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
            "P2_R0_05I3_REAL_GARMENT_CANVAS_EXPORT",

        "status":
            "COMPLETE",

        "representatives":
            reps.to_dict(
                orient="records"
            ),

        "json_sha256":
            sha256_file(
                JSON_OUT
            ),

        "intrinsic_npz_sha256":
            EXPECTED_H1_SHA,

        "interpretation_boundary":
            (
                "The exported examples are visualization exemplars chosen "
                "by a frozen representative rule. The intrinsic stage shows "
                "the CROP_ONLY raster only as visual context; its spectral "
                "metrics come from the 05H1 intrinsic field."
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
        "P2-R0-05I3 — REPRESENTATIVE REAL-GARMENT SKETCHES"
    )

    print(
        "=" * 150
    )

    print(
        reps.to_string(
            index=False
        )
    )

    print(
        "\nP2-R0-05I3 REAL-GARMENT CANVAS EXPORT: COMPLETE"
    )

    print(
        "Representative CSV:",
        REPRESENTATIVE_CSV,
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
        "\nSTOP — use this JSON unchanged for Canvas v0.4."
    )


if __name__ == "__main__":
    main()