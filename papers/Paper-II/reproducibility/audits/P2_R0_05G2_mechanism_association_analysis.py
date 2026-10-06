from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr


# =============================================================================
# P2-R0-05G2 — MECHANISM ASSOCIATION ANALYSIS
#
# Diagnostic only.
#
# Connects the frozen 05G1 frame/border/gradient metrics to per-image spectral
# changes from RAW -> V3_CROP_ONLY.
#
# Main questions:
#   1) Does high_25_36 change track boundary-gradient redistribution?
#   2) Does it track crop support / foreground density?
#   3) Is centroid map-back effectively a negative control?
#
# IMPORTANT:
#   - No model selection.
#   - No band redefinition.
#   - No tuning.
#   - No causal claim.
#   - Frozen Paper-II geometry implementation is reused.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)

G1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05g_frame_border_gradient"
)

G1_METRICS = (
    G1_ROOT
    / "P2_R0_05G1_frame_border_gradient_metrics.csv"
)

EXPECTED_G1_METRICS_SHA256 = (
    "d40b052db1ca17b5f91d2a20cb57caa9d66930a53b341eb80804a292fa75c055"
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

OUTPUT_ROOT = G1_ROOT

SPECTRAL_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05G2_per_image_spectral_changes.csv"
)

IDENTITY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05G2_identity_level_table.csv"
)

ASSOCIATION_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05G2_mechanism_associations.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05G2_report.json"
)

N_PERMUTATIONS = 10000
RNG_SEED = 20261001
EPS = 1e-12


HARMONIC_BANDS = {
    "low_1_4":
        np.arange(
            1,
            5,
            dtype=int,
        ),

    "mid_5_12":
        np.arange(
            5,
            13,
            dtype=int,
        ),

    "highmid_13_24":
        np.arange(
            13,
            25,
            dtype=int,
        ),

    "high_25_36":
        np.arange(
            25,
            37,
            dtype=int,
        ),
}


# =============================================================================
# Helpers
# =============================================================================

def sha256_file(
    path: Path,
) -> str:

    h = hashlib.sha256()

    with path.open(
        "rb"
    ) as f:

        for chunk in iter(
            lambda:
                f.read(
                    1024
                    * 1024
                ),
            b"",
        ):
            h.update(
                chunk
            )

    return h.hexdigest()


def load_verified_d4_definitions():

    if not BASE_AUDIT.is_file():
        raise RuntimeError(
            f"Base D4 audit missing: "
            f"{BASE_AUDIT}"
        )

    source = BASE_AUDIT.read_text(
        encoding="utf-8"
    )

    marker = (
        'if __name__ == "__main__":'
    )

    if marker not in source:
        raise RuntimeError(
            "Could not locate __main__ "
            "boundary in D4 audit"
        )

    definitions_only = source.split(
        marker,
        1,
    )[0]

    namespace = {
        "__file__":
            str(
                BASE_AUDIT
            ),

        "__name__":
            "p2_r0_05_verified_definitions",
    }

    exec(
        compile(
            definitions_only,
            str(
                BASE_AUDIT
            ),
            "exec",
        ),
        namespace,
    )

    required = [
        "load_paper2_runtime",
        "validate_geometry_equivalence",
        "load_and_validate_fold_package",
        "normalize_runtime_relative_path",
    ]

    missing = [
        name
        for name
        in required
        if name
        not in namespace
    ]

    if missing:
        raise RuntimeError(
            "Required D4 definitions "
            f"missing: {missing}"
        )

    print(
        "P2-R0-05G2 VERIFIED D4 DEFINITIONS: PASS"
    )

    return namespace


def build_crop_rows(
    crop_manifest: pd.DataFrame,
    runtime: dict,
    normalize_runtime_relative_path,
):

    runtime_paths = np.asarray(
        [
            normalize_runtime_relative_path(
                x
            )
            for x
            in runtime[
                "image_paths"
            ]
        ],
        dtype=str,
    )

    manifest_paths = (
        crop_manifest[
            "relative_path"
        ]
        .astype(
            str
        )
        .to_numpy()
    )

    if not np.array_equal(
        runtime_paths,
        manifest_paths,
    ):
        raise RuntimeError(
            "CROP_ONLY population/order "
            "does not match Paper-II runtime"
        )

    categories = np.asarray(
        runtime[
            "image_categories"
        ],
        dtype=str,
    )

    rows = []

    for i, record in (
        crop_manifest
        .iterrows()
    ):

        path = (
            CROP_ONLY_ROOT
            / str(
                record[
                    "output_relative_path"
                ]
            )
        )

        if not path.is_file():
            raise RuntimeError(
                f"Missing CROP_ONLY image: "
                f"{path}"
            )

        rows.append(
            {
                "relative_path":
                    str(
                        record[
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
                    path,
            }
        )

    return rows


def reconstruct_crop_geometry(
    ra14_module,
    crop_rows,
):

    print(
        "\nP2-R0-05G2 — reconstructing "
        "CROP_ONLY geometry..."
    )

    (
        conditional,
        nonempty,
        radial_centers,
        mass_error,
        normalization_error,
    ) = ra14_module.recover_geometry(
        crop_rows
    )

    conditional = np.asarray(
        conditional,
        dtype=np.float64,
    )

    if conditional.shape != (
        EXPECTED_ROWS,
        72,
        72,
    ):
        raise RuntimeError(
            "Unexpected CROP_ONLY "
            f"geometry shape: "
            f"{conditional.shape}"
        )

    fft = np.fft.rfft(
        conditional,
        axis=2,
    )

    if fft.shape != (
        EXPECTED_ROWS,
        72,
        37,
    ):
        raise RuntimeError(
            "Unexpected CROP_ONLY "
            f"FFT shape: "
            f"{fft.shape}"
        )

    if not (
        np.isfinite(
            conditional
        ).all()
        and
        np.isfinite(
            fft.real
        ).all()
        and
        np.isfinite(
            fft.imag
        ).all()
    ):
        raise RuntimeError(
            "CROP_ONLY geometry/FFT "
            "contains non-finite values"
        )

    print(
        "CROP_ONLY geometry: PASS"
    )

    print(
        "Max mass error:",
        mass_error,
    )

    print(
        "Max normalization error:",
        normalization_error,
    )

    print(
        "Non-empty shells:",
        int(
            np.sum(
                nonempty
            )
        ),
        "/",
        int(
            nonempty.size
        ),
    )

    return (
        conditional,
        fft,
    )


def relative_l2(
    a: np.ndarray,
    b: np.ndarray,
) -> np.ndarray:

    diff = (
        b
        - a
    )

    num = np.sqrt(
        np.sum(
            np.abs(
                diff
            )
            ** 2,
            axis=tuple(
                range(
                    1,
                    diff.ndim,
                )
            ),
        )
    )

    den = np.sqrt(
        np.sum(
            np.abs(
                a
            )
            ** 2,
            axis=tuple(
                range(
                    1,
                    a.ndim,
                )
            ),
        )
    )

    return (
        num
        / np.maximum(
            den,
            EPS,
        )
    )


def band_energy(
    fft: np.ndarray,
    harmonics: np.ndarray,
) -> np.ndarray:

    selected = fft[
        :,
        :,
        harmonics,
    ]

    return np.mean(
        np.abs(
            selected
        )
        ** 2,
        axis=(
            1,
            2,
        ),
    )


def total_non_dc_energy(
    fft: np.ndarray,
) -> np.ndarray:

    return np.mean(
        np.abs(
            fft[
                :,
                :,
                1:37,
            ]
        )
        ** 2,
        axis=(
            1,
            2,
        ),
    )


def safe_spearman(
    x: np.ndarray,
    y: np.ndarray,
):

    mask = (
        np.isfinite(
            x
        )
        &
        np.isfinite(
            y
        )
    )

    x = x[
        mask
    ]

    y = y[
        mask
    ]

    if (
        len(
            x
        )
        < 3
        or
        np.nanstd(
            x
        )
        == 0
        or
        np.nanstd(
            y
        )
        == 0
    ):
        return (
            np.nan,
            int(
                len(
                    x
                )
            ),
        )

    rho = float(
        spearmanr(
            x,
            y,
        ).statistic
    )

    return (
        rho,
        int(
            len(
                x
            )
        ),
    )


def category_center(
    values: np.ndarray,
    categories: np.ndarray,
) -> np.ndarray:

    values = np.asarray(
        values,
        dtype=float,
    )

    categories = np.asarray(
        categories,
        dtype=str,
    )

    centered = np.full_like(
        values,
        np.nan,
        dtype=float,
    )

    for category in np.unique(
        categories
    ):

        idx = np.flatnonzero(
            categories
            == category
        )

        local = values[
            idx
        ]

        finite = np.isfinite(
            local
        )

        if not np.any(
            finite
        ):
            continue

        median = float(
            np.median(
                local[
                    finite
                ]
            )
        )

        centered[
            idx[
                finite
            ]
        ] = (
            local[
                finite
            ]
            - median
        )

    return centered


def stratified_permutation_p(
    x: np.ndarray,
    y: np.ndarray,
    categories: np.ndarray,
    observed_rho: float,
    rng: np.random.Generator,
    n_perm: int,
) -> float:

    if not np.isfinite(
        observed_rho
    ):
        return np.nan

    x = np.asarray(
        x,
        dtype=float,
    )

    y = np.asarray(
        y,
        dtype=float,
    )

    categories = np.asarray(
        categories,
        dtype=str,
    )

    valid = (
        np.isfinite(
            x
        )
        &
        np.isfinite(
            y
        )
    )

    x = x[
        valid
    ]

    y = y[
        valid
    ]

    categories = categories[
        valid
    ]

    if len(
        x
    ) < 3:
        return np.nan

    groups = [
        np.flatnonzero(
            categories
            == category
        )
        for category
        in np.unique(
            categories
        )
    ]

    extreme = 0

    for _ in range(
        n_perm
    ):

        permuted = y.copy()

        for idx in groups:
            permuted[
                idx
            ] = rng.permutation(
                permuted[
                    idx
                ]
            )

        rho = spearmanr(
            x,
            permuted,
        ).statistic

        if (
            np.isfinite(
                rho
            )
            and
            abs(
                rho
            )
            >= abs(
                observed_rho
            )
        ):
            extreme += 1

    return float(
        (
            extreme
            + 1
        )
        /
        (
            n_perm
            + 1
        )
    )


def benjamini_hochberg(
    p_values: np.ndarray,
) -> np.ndarray:

    p = np.asarray(
        p_values,
        dtype=float,
    )

    q = np.full_like(
        p,
        np.nan,
        dtype=float,
    )

    finite_idx = np.flatnonzero(
        np.isfinite(
            p
        )
    )

    if len(
        finite_idx
    ) == 0:
        return q

    finite_p = p[
        finite_idx
    ]

    order = np.argsort(
        finite_p
    )

    ranked = finite_p[
        order
    ]

    m = len(
        ranked
    )

    adjusted = (
        ranked
        * m
        / np.arange(
            1,
            m
            + 1,
        )
    )

    adjusted = np.minimum.accumulate(
        adjusted[
            ::-1
        ]
    )[
        ::-1
    ]

    adjusted = np.clip(
        adjusted,
        0.0,
        1.0,
    )

    restored = np.empty_like(
        adjusted
    )

    restored[
        order
    ] = adjusted

    q[
        finite_idx
    ] = restored

    return q


# =============================================================================
# MAIN
# =============================================================================

def main():

    # -------------------------------------------------------------------------
    # Provenance gates
    # -------------------------------------------------------------------------

    if not G1_METRICS.is_file():
        raise RuntimeError(
            f"05G1 metrics missing: "
            f"{G1_METRICS}"
        )

    observed_g1_sha = sha256_file(
        G1_METRICS
    )

    if (
        observed_g1_sha
        != EXPECTED_G1_METRICS_SHA256
    ):
        raise RuntimeError(
            "05G1 metrics SHA mismatch"
        )

    if not CROP_ONLY_MANIFEST.is_file():
        raise RuntimeError(
            "CROP_ONLY manifest missing"
        )

    if (
        sha256_file(
            CROP_ONLY_MANIFEST
        )
        != EXPECTED_CROP_ONLY_MANIFEST_SHA256
    ):
        raise RuntimeError(
            "CROP_ONLY manifest SHA mismatch"
        )

    metrics = pd.read_csv(
        G1_METRICS,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    crop_manifest = pd.read_csv(
        CROP_ONLY_MANIFEST,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    if (
        len(
            metrics
        )
        != EXPECTED_ROWS
        or
        len(
            crop_manifest
        )
        != EXPECTED_ROWS
    ):
        raise RuntimeError(
            "Expected exactly 2300 rows"
        )

    if not np.array_equal(
        metrics[
            "relative_path"
        ].astype(
            str
        ).to_numpy(),
        crop_manifest[
            "relative_path"
        ].astype(
            str
        ).to_numpy(),
    ):
        raise RuntimeError(
            "05G1/CROP_ONLY row-order mismatch"
        )

    print(
        "P2-R0-05G2 INPUT PROVENANCE: PASS"
    )

    print(
        "05G1 metrics SHA-256:",
        observed_g1_sha,
    )

    # -------------------------------------------------------------------------
    # Reuse verified Paper-II geometry implementation
    # -------------------------------------------------------------------------

    base = (
        load_verified_d4_definitions()
    )

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
        garment_identity,
        category_from_folds,
        folds,
        fold_sha,
    ) = (
        base[
            "load_and_validate_fold_package"
        ](
            runtime
        )
    )

    crop_rows = build_crop_rows(
        crop_manifest,
        runtime,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    (
        crop_conditional,
        crop_fft,
    ) = reconstruct_crop_geometry(
        ra14_module,
        crop_rows,
    )

    # -------------------------------------------------------------------------
    # Per-image spectral diagnostics
    # -------------------------------------------------------------------------

    spectral = pd.DataFrame(
        {
            "row_index":
                np.arange(
                    EXPECTED_ROWS,
                    dtype=int,
                ),

            "relative_path":
                metrics[
                    "relative_path"
                ].astype(
                    str
                ).to_numpy(),

            "category":
                np.asarray(
                    runtime[
                        "image_categories"
                    ],
                    dtype=str,
                ),

            "garment_identity":
                np.asarray(
                    garment_identity
                ).astype(
                    str
                ),
        }
    )

    raw_total = total_non_dc_energy(
        raw_fft
    )

    crop_total = total_non_dc_energy(
        crop_fft
    )

    spectral[
        "raw_total_non_dc_energy"
    ] = raw_total

    spectral[
        "crop_total_non_dc_energy"
    ] = crop_total

    spectral[
        "delta_log10_total_non_dc_energy"
    ] = (
        np.log10(
            crop_total
            + EPS
        )
        -
        np.log10(
            raw_total
            + EPS
        )
    )

    for band_name, harmonics in (
        HARMONIC_BANDS.items()
    ):

        raw_energy = band_energy(
            raw_fft,
            harmonics,
        )

        crop_energy = band_energy(
            crop_fft,
            harmonics,
        )

        raw_fraction = (
            raw_energy
            / np.maximum(
                raw_total,
                EPS,
            )
        )

        crop_fraction = (
            crop_energy
            / np.maximum(
                crop_total,
                EPS,
            )
        )

        spectral[
            f"raw_{band_name}_energy"
        ] = raw_energy

        spectral[
            f"crop_{band_name}_energy"
        ] = crop_energy

        spectral[
            f"delta_log10_{band_name}_energy"
        ] = (
            np.log10(
                crop_energy
                + EPS
            )
            -
            np.log10(
                raw_energy
                + EPS
            )
        )

        spectral[
            f"raw_{band_name}_fraction"
        ] = raw_fraction

        spectral[
            f"crop_{band_name}_fraction"
        ] = crop_fraction

        spectral[
            f"delta_{band_name}_fraction"
        ] = (
            crop_fraction
            - raw_fraction
        )

    spectral[
        "conditional_relative_l2_raw_to_crop"
    ] = relative_l2(
        raw_conditional,
        crop_conditional,
    )

    spectral[
        "fourier_relative_l2_raw_to_crop"
    ] = relative_l2(
        raw_fft,
        crop_fft,
    )

    spectral.to_csv(
        SPECTRAL_CSV,
        index=False,
    )

    spectral_sha = sha256_file(
        SPECTRAL_CSV
    )

    print(
        "\nP2-R0-05G2 PER-IMAGE SPECTRAL "
        "DIAGNOSTICS: PASS"
    )

    print(
        "Spectral CSV SHA-256:",
        spectral_sha,
    )

    # -------------------------------------------------------------------------
    # Merge with 05G1 mechanism variables
    # -------------------------------------------------------------------------

    merged = metrics.merge(
        spectral,
        on=[
            "row_index",
            "relative_path",
        ],
        how="inner",
        validate="one_to_one",
        suffixes=(
            "_g1",
            "_spectral",
        ),
    )

    if len(
        merged
    ) != EXPECTED_ROWS:
        raise RuntimeError(
            "Merged table does not contain 2300 rows"
        )

    # -------------------------------------------------------------------------
    # Identity-level medians
    #
    # This avoids treating repeated sketches from one garment identity as
    # independent replicates for the association analysis.
    # -------------------------------------------------------------------------

    mechanism_predictors = [
        "crop_area_fraction_of_raw",

        "delta_foreground_fraction_crop_minus_raw",

        "grid_radius_ratio_crop_to_raw",

        "delta_foreground_radius_to_grid_radius_crop_minus_raw",

        "delta_gradient_mean_all_crop_minus_raw",

        "crop_gradient_energy_border_10px_fraction",

        "delta_gradient_energy_border_10px_fraction_crop_minus_raw",

        "crop_strong_gradient_near_border_10px_fraction_of_strong",

        "delta_strong_gradient_near_border_10px_fraction_crop_minus_raw",

        "crop_foreground_near_border_10px_fraction",

        "delta_foreground_near_border_10px_fraction_crop_minus_raw",

        "centroid_mapback_error_px",
    ]

    outcomes = [
        "delta_log10_high_25_36_energy",
        "delta_high_25_36_fraction",
        "delta_log10_mid_5_12_energy",
        "delta_mid_5_12_fraction",
        "fourier_relative_l2_raw_to_crop",
        "conditional_relative_l2_raw_to_crop",
    ]

    missing_columns = [
        c
        for c
        in (
            mechanism_predictors
            + outcomes
        )
        if c
        not in merged.columns
    ]

    if missing_columns:
        raise RuntimeError(
            "Missing analysis columns: "
            f"{missing_columns}"
        )

    identity_group_cols = [
        "garment_identity",
        "category_spectral",
    ]

    numeric_for_identity = (
        mechanism_predictors
        + outcomes
    )

    identity = (
        merged[
            identity_group_cols
            + numeric_for_identity
        ]
        .copy()
        .groupby(
            identity_group_cols,
            as_index=False,
        )[
            numeric_for_identity
        ]
        .median(
            numeric_only=True
        )
    )

    if len(
        identity
    ) != 230:
        raise RuntimeError(
            "Expected 230 garment identities, "
            f"found {len(identity)}"
        )

    identity = identity.rename(
        columns={
            "category_spectral":
                "category"
        }
    )

    identity.to_csv(
        IDENTITY_CSV,
        index=False,
    )

    identity_sha = sha256_file(
        IDENTITY_CSV
    )

    print(
        "\nP2-R0-05G2 IDENTITY AGGREGATION: PASS"
    )

    print(
        "Garment identities:",
        len(
            identity
        ),
    )

    print(
        "Identity table SHA-256:",
        identity_sha,
    )

    # -------------------------------------------------------------------------
    # Association analysis
    #
    # Two related diagnostics:
    #
    # 1) identity-level Spearman rho
    # 2) category-centered identity-level Spearman rho
    #
    # Permutation p-values shuffle the outcome WITHIN CATEGORY to preserve
    # category structure under the null.
    # -------------------------------------------------------------------------

    rng = np.random.default_rng(
        RNG_SEED
    )

    categories = identity[
        "category"
    ].astype(
        str
    ).to_numpy()

    association_rows = []

    for predictor in mechanism_predictors:

        x = pd.to_numeric(
            identity[
                predictor
            ],
            errors="coerce",
        ).to_numpy(
            dtype=float
        )

        x_centered = category_center(
            x,
            categories,
        )

        for outcome in outcomes:

            y = pd.to_numeric(
                identity[
                    outcome
                ],
                errors="coerce",
            ).to_numpy(
                dtype=float
            )

            y_centered = category_center(
                y,
                categories,
            )

            rho_raw, n_raw = safe_spearman(
                x,
                y,
            )

            rho_centered, n_centered = safe_spearman(
                x_centered,
                y_centered,
            )

            p_perm_raw = stratified_permutation_p(
                x,
                y,
                categories,
                rho_raw,
                rng,
                N_PERMUTATIONS,
            )

            p_perm_centered = stratified_permutation_p(
                x_centered,
                y_centered,
                categories,
                rho_centered,
                rng,
                N_PERMUTATIONS,
            )

            association_rows.append(
                {
                    "predictor":
                        predictor,

                    "outcome":
                        outcome,

                    "n_identities_raw":
                        n_raw,

                    "spearman_rho_identity":
                        rho_raw,

                    "category_stratified_permutation_p_identity":
                        p_perm_raw,

                    "n_identities_category_centered":
                        n_centered,

                    "spearman_rho_category_centered":
                        rho_centered,

                    "category_stratified_permutation_p_category_centered":
                        p_perm_centered,
                }
            )

    associations = pd.DataFrame(
        association_rows
    )

    associations[
        "q_FDR_identity"
    ] = benjamini_hochberg(
        associations[
            "category_stratified_permutation_p_identity"
        ].to_numpy(
            dtype=float
        )
    )

    associations[
        "q_FDR_category_centered"
    ] = benjamini_hochberg(
        associations[
            "category_stratified_permutation_p_category_centered"
        ].to_numpy(
            dtype=float
        )
    )

    associations.to_csv(
        ASSOCIATION_CSV,
        index=False,
    )

    association_sha = sha256_file(
        ASSOCIATION_CSV
    )

    # -------------------------------------------------------------------------
    # Compact ranked views for the two high-band outcomes
    # -------------------------------------------------------------------------

    high_subset = associations[
        associations[
            "outcome"
        ].isin(
            [
                "delta_log10_high_25_36_energy",
                "delta_high_25_36_fraction",
            ]
        )
    ].copy()

    high_subset[
        "abs_category_centered_rho"
    ] = np.abs(
        high_subset[
            "spearman_rho_category_centered"
        ]
    )

    high_subset = high_subset.sort_values(
        [
            "outcome",
            "abs_category_centered_rho",
        ],
        ascending=[
            True,
            False,
        ],
    )

    print(
        "\n"
        + "="
        * 132
    )

    print(
        "P2-R0-05G2 — HIGH-BAND MECHANISM "
        "ASSOCIATIONS"
    )

    print(
        "="
        * 132
    )

    print(
        high_subset[
            [
                "predictor",
                "outcome",
                "spearman_rho_identity",
                "category_stratified_permutation_p_identity",
                "spearman_rho_category_centered",
                "category_stratified_permutation_p_category_centered",
                "q_FDR_category_centered",
            ]
        ].to_string(
            index=False
        )
    )

    # -------------------------------------------------------------------------
    # Negative-control report
    # -------------------------------------------------------------------------

    centroid_values = pd.to_numeric(
        identity[
            "centroid_mapback_error_px"
        ],
        errors="coerce",
    ).to_numpy(
        dtype=float
    )

    centroid_unique = np.unique(
        centroid_values[
            np.isfinite(
                centroid_values
            )
        ]
    )

    print(
        "\nP2-R0-05G2 — CENTROID MAP-BACK NEGATIVE CONTROL"
    )

    print(
        "Unique finite identity-level "
        "centroid map-back values:",
        centroid_unique,
    )

    # -------------------------------------------------------------------------
    # Report
    # -------------------------------------------------------------------------

    report = {
        "stage":
            "P2_R0_05G2_MECHANISM_ASSOCIATION_ANALYSIS",

        "status":
            "COMPLETE",

        "rows":
            EXPECTED_ROWS,

        "garment_identities":
            int(
                len(
                    identity
                )
            ),

        "categories":
            int(
                identity[
                    "category"
                ].nunique()
            ),

        "permutations":
            N_PERMUTATIONS,

        "rng_seed":
            RNG_SEED,

        "05G1_metrics_sha256":
            observed_g1_sha,

        "spectral_csv_sha256":
            spectral_sha,

        "identity_csv_sha256":
            identity_sha,

        "association_csv_sha256":
            association_sha,

        "fold_package_sha256":
            fold_sha,

        "analysis_unit":
            (
                "garment-identity median across repeated sketches"
            ),

        "association_measure":
            (
                "Spearman rank correlation; additionally "
                "category-median-centered Spearman"
            ),

        "null_permutation":
            (
                "outcome shuffled within garment category"
            ),

        "multiplicity":
            (
                "Benjamini-Hochberg FDR across the diagnostic "
                "association table"
            ),

        "interpretation_boundary":
            (
                "05G2 is an association/mechanism diagnostic. "
                "Correlation does not establish that frame, border, "
                "or gradient changes cause the spectral change."
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
        "\nP2-R0-05G2 MECHANISM "
        "ASSOCIATION ANALYSIS: COMPLETE"
    )

    print(
        "Per-image spectral CSV:",
        SPECTRAL_CSV,
    )

    print(
        "Identity table:",
        IDENTITY_CSV,
    )

    print(
        "Association table:",
        ASSOCIATION_CSV,
    )

    print(
        "Association SHA-256:",
        association_sha,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — diagnostic association analysis "
        "complete; no causal claim made."
    )


if __name__ == "__main__":
    main()