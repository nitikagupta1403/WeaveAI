from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image


# =============================================================================
# FROZEN PATHS / CONSTANTS
# =============================================================================

E8 = Path(__file__).resolve().parent

DATASET_ROOT = Path(
    "/Users/nitikagupta/Desktop/Clo-Sket"
)

RA14_SOURCE_MANIFEST = (
    E8 / "experiment08_ra14_source_manifest.csv"
)

OUTPUT_NPY = (
    E8 / "experiment08_morphology_features.npy"
)

OUTPUT_MANIFEST = (
    E8 / "experiment08_morphology_manifest.json"
)

EXPECTED_ROWS = 2300
EXPECTED_FEATURES = 135

EXPECTED_RAW_ARRAY_SHA256 = (
    "66ae04156ee3fbf3f2605f382a16fc41"
    "cf19af34b50e59dd43f6c9427d96b2ee"
)


# =============================================================================
# HASH HELPERS
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


def sha256_array(array: np.ndarray) -> str:
    array = np.ascontiguousarray(array)

    return hashlib.sha256(
        array.tobytes()
    ).hexdigest()


# =============================================================================
# EXACT FROZEN MORPHOLOGY EXTRACTOR
# =============================================================================

def morphology_features(
    path: Path,
    size: int = 64,
) -> np.ndarray:
    """
    Exact frozen 135-D morphology definition copied from the
    historical Validation Shield / morphology-discovery lineage.

    64 horizontal occupancy coordinates
    + 64 vertical occupancy coordinates
    + 7 global descriptors
    = 135 dimensions.
    """

    with Image.open(path) as image:
        image.load()

        image = image.convert("L")

        array = np.asarray(
            image,
            dtype=np.float32,
        )

    # Exact frozen intensity normalization.
    array = (
        array
        / np.float32(255.0)
    )

    # Exact frozen foreground definition.
    foreground = (
        array < np.float32(0.8)
    )

    # Exact historical resize operation.
    #
    # IMPORTANT:
    # Do not specify a new resampling mode here.
    # The canonical historical implementation called .resize()
    # without a resample argument, so Pillow's historical default
    # behavior is preserved exactly.
    foreground_image = Image.fromarray(
        foreground.astype(
            np.uint8
        )
        * 255
    ).resize(
        (size, size)
    )

    mask = (
        np.asarray(
            foreground_image,
            dtype=np.float32,
        )
        / np.float32(255.0)
    )

    # -------------------------------------------------------------------------
    # 64 horizontal occupancy coordinates
    # -------------------------------------------------------------------------

    horizontal = mask.mean(
        axis=1
    )

    # -------------------------------------------------------------------------
    # 64 vertical occupancy coordinates
    # -------------------------------------------------------------------------

    vertical = mask.mean(
        axis=0
    )

    # -------------------------------------------------------------------------
    # Seven global descriptors
    # -------------------------------------------------------------------------

    total = (
        mask.sum()
        + np.float32(1e-8)
    )

    yy, xx = np.indices(
        mask.shape
    )

    centroid_x = (
        (xx * mask).sum()
        / total
    )

    centroid_y = (
        (yy * mask).sum()
        / total
    )

    centroid_x = (
        centroid_x
        / size
    )

    centroid_y = (
        centroid_y
        / size
    )

    ys, xs = np.where(
        mask > 0
    )

    if len(xs) > 0:
        bbox_width = (
            xs.max()
            - xs.min()
            + 1
        ) / size

        bbox_height = (
            ys.max()
            - ys.min()
            + 1
        ) / size

        aspect_ratio = (
            bbox_width
            / (
                bbox_height
                + 1e-8
            )
        )

    else:
        bbox_width = 0.0
        bbox_height = 0.0
        aspect_ratio = 0.0

    flipped = np.fliplr(
        mask
    )

    symmetry = (
        1.0
        - np.mean(
            np.abs(
                mask
                - flipped
            )
        )
    )

    features = np.concatenate([
        horizontal,
        vertical,
        np.array(
            [
                centroid_x,
                centroid_y,
                bbox_width,
                bbox_height,
                aspect_ratio,
                symmetry,
                mask.mean(),
            ]
        ),
    ])

    features = features.astype(
        np.float32
    )

    if features.shape != (
        EXPECTED_FEATURES,
    ):
        raise RuntimeError(
            "Morphology extractor returned "
            f"{features.shape}; expected "
            f"({EXPECTED_FEATURES},)."
        )

    if not np.isfinite(
        features
    ).all():
        raise RuntimeError(
            f"Non-finite morphology features: {path}"
        )

    return features


# =============================================================================
# MAIN
# =============================================================================

def main():
    print(
        "=" * 88
    )
    print(
        "EXPERIMENT 08 — CANONICAL 135-D MORPHOLOGY MATERIALIZATION"
    )
    print(
        "=" * 88
    )

    # -------------------------------------------------------------------------
    # 1. Frozen source manifest
    # -------------------------------------------------------------------------

    if not RA14_SOURCE_MANIFEST.is_file():
        raise FileNotFoundError(
            RA14_SOURCE_MANIFEST
        )

    manifest = pd.read_csv(
        RA14_SOURCE_MANIFEST,
        keep_default_na=False,
    )

    required_columns = {
        "row_index",
        "relative_path",
        "category",
    }

    missing = (
        required_columns
        - set(manifest.columns)
    )

    if missing:
        raise RuntimeError(
            "RA14 source manifest missing: "
            + ", ".join(
                sorted(missing)
            )
        )

    if len(manifest) != EXPECTED_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_ROWS} rows, "
            f"found {len(manifest)}."
        )

    if (
        manifest[
            "row_index"
        ].tolist()
        != list(
            range(
                EXPECTED_ROWS
            )
        )
    ):
        raise RuntimeError(
            "row_index is not exactly 0..2299."
        )

    if manifest[
        "relative_path"
    ].duplicated().any():
        raise RuntimeError(
            "Duplicate source relative paths."
        )

    print(
        "\nSOURCE POPULATION"
    )
    print(
        "-" * 88
    )
    print(
        "Rows       :",
        len(manifest),
    )
    print(
        "Categories :",
        manifest[
            "category"
        ].nunique(),
    )
    print(
        "Row order  : frozen Experiment-08 RA14 source manifest"
    )

    # -------------------------------------------------------------------------
    # 2. Resolve TIFF paths
    # -------------------------------------------------------------------------

    source_paths = [
        DATASET_ROOT
        / relative_path
        for relative_path
        in manifest[
            "relative_path"
        ].tolist()
    ]

    missing_paths = [
        path
        for path in source_paths
        if not path.is_file()
    ]

    if missing_paths:
        print(
            "\nFIRST MISSING PATHS"
        )

        for path in (
            missing_paths[:10]
        ):
            print(path)

        raise FileNotFoundError(
            f"{len(missing_paths)} source TIFFs "
            "are missing."
        )

    if len(
        set(
            str(path)
            for path
            in source_paths
        )
    ) != EXPECTED_ROWS:
        raise RuntimeError(
            "Resolved TIFF paths are not unique."
        )

    print(
        "TIFF files  :",
        len(source_paths),
    )

    # -------------------------------------------------------------------------
    # 3. Extract exact frozen morphology
    # -------------------------------------------------------------------------

    test_vector = (
        morphology_features(
            source_paths[0]
        )
    )

    print(
        "\nEXTRACTOR PREFLIGHT"
    )
    print(
        "-" * 88
    )
    print(
        "Test path   :",
        manifest.loc[
            0,
            "relative_path",
        ],
    )
    print(
        "Shape       :",
        test_vector.shape,
    )
    print(
        "dtype       :",
        test_vector.dtype,
    )
    print(
        "Finite      :",
        bool(
            np.isfinite(
                test_vector
            ).all()
        ),
    )

    rows = []

    print(
        "\nRECONSTRUCTING MORPHOLOGY"
    )
    print(
        "-" * 88
    )

    for i, path in enumerate(
        source_paths
    ):
        vector = (
            morphology_features(
                path
            )
        )

        rows.append(
            vector
        )

        if (
            (i + 1) % 250 == 0
            or
            i == EXPECTED_ROWS - 1
        ):
            print(
                f"processed "
                f"{i + 1}/{EXPECTED_ROWS}"
            )

    X = np.ascontiguousarray(
        np.vstack(
            rows
        ),
        dtype=np.float32,
    )

    # -------------------------------------------------------------------------
    # 4. Canonical validation
    # -------------------------------------------------------------------------

    if X.shape != (
        EXPECTED_ROWS,
        EXPECTED_FEATURES,
    ):
        raise RuntimeError(
            "Unexpected morphology matrix shape: "
            f"{X.shape}"
        )

    if X.dtype != np.float32:
        raise RuntimeError(
            "Morphology matrix is not float32."
        )

    if not np.isfinite(
        X
    ).all():
        raise RuntimeError(
            "Morphology matrix contains non-finite values."
        )

    raw_array_sha256 = (
        sha256_array(
            X
        )
    )

    print(
        "\nCANONICAL MORPHOLOGY AUDIT"
    )
    print(
        "-" * 88
    )
    print(
        "Matrix shape        :",
        X.shape,
    )
    print(
        "dtype               :",
        X.dtype,
    )
    print(
        "Finite              :",
        bool(
            np.isfinite(
                X
            ).all()
        ),
    )
    print(
        "Observed array SHA  :",
        raw_array_sha256,
    )
    print(
        "Expected array SHA  :",
        EXPECTED_RAW_ARRAY_SHA256,
    )

    if (
        raw_array_sha256
        != EXPECTED_RAW_ARRAY_SHA256
    ):
        raise RuntimeError(
            "\nCANONICAL MORPHOLOGY HASH MISMATCH.\n"
            "The reconstructed matrix will NOT be saved "
            "or used for Experiment 08."
        )

    # -------------------------------------------------------------------------
    # 5. Save only after exact canonical fingerprint passes
    # -------------------------------------------------------------------------

    np.save(
        OUTPUT_NPY,
        X,
        allow_pickle=False,
    )

    saved_npy_sha256 = (
        sha256_file(
            OUTPUT_NPY
        )
    )

    source_manifest_sha256 = (
        sha256_file(
            RA14_SOURCE_MANIFEST
        )
    )

    output_manifest = {
        "experiment":
            "CLO-SKET Experiment 08",

        "representation":
            "M",

        "representation_name":
            "Frozen 135-D morphology",

        "population":
            EXPECTED_ROWS,

        "n_features":
            EXPECTED_FEATURES,

        "dtype":
            "float32",

        "finite":
            True,

        "source_row_order":
            "experiment08_ra14_source_manifest.csv",

        "source_manifest_sha256":
            source_manifest_sha256,

        "dataset_root_runtime":
            str(
                DATASET_ROOT
            ),

        "feature_definition": {
            "grayscale":
                "PIL convert('L')",

            "intensity_normalization":
                "array / 255.0",

            "foreground_rule":
                "array < 0.8",

            "mask_resize":
                "PIL Image.resize((64,64)) with historical default resampling",

            "horizontal_occupancy_dimensions":
                64,

            "vertical_occupancy_dimensions":
                64,

            "global_dimensions":
                7,

            "global_features": [
                "centroid_x",
                "centroid_y",
                "bbox_width",
                "bbox_height",
                "aspect_ratio",
                "left_right_symmetry",
                "mask_mean",
            ],
        },

        "canonical_raw_array_sha256":
            raw_array_sha256,

        "expected_canonical_raw_array_sha256":
            EXPECTED_RAW_ARRAY_SHA256,

        "saved_npy_sha256":
            saved_npy_sha256,

        "canonical_hash_match":
            True,

        "category_labels_used_for_feature_extraction":
            False,

        "classifier_fitted":
            False,

        "predictive_outcome_computed":
            False,

        "approval_boundary":
            (
                "Canonical morphology reconstructed from the "
                "historical frozen extractor and accepted only "
                "after exact SHA-256 reproduction."
            ),
    }

    OUTPUT_MANIFEST.write_text(
        json.dumps(
            output_manifest,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    # Make runtime matrix read-only after acceptance.
    X.setflags(
        write=False
    )

    print(
        "\n" + "=" * 88
    )
    print(
        "EXPERIMENT 08 — CANONICAL MORPHOLOGY RESTORED"
    )
    print(
        "=" * 88
    )
    print(
        "Matrix              :",
        X.shape,
    )
    print(
        "dtype               :",
        X.dtype,
    )
    print(
        "Array SHA-256       :",
        raw_array_sha256,
    )
    print(
        "Saved NPY SHA-256   :",
        saved_npy_sha256,
    )
    print(
        "Source manifest SHA :",
        source_manifest_sha256,
    )
    print(
        "Feature matrix      :",
        OUTPUT_NPY,
    )
    print(
        "Manifest            :",
        OUTPUT_MANIFEST,
    )

    print(
        "\nCANONICAL HASH MATCH: PASS"
    )
    print(
        "Classifier fitted   : False"
    )
    print(
        "Outcome computed    : False"
    )


if __name__ == "__main__":
    main()