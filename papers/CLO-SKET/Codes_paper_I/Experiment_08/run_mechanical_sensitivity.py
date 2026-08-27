#!/usr/bin/env python3
"""
Experiment 08 — post-outcome mechanical sensitivity analysis.

This runner implements the analysis frozen in:

    docs/experiment-08/post-outcome-mechanical-sensitivity-amendment.md

Scientific firewall
-------------------
Default invocation performs STRUCTURAL VALIDATION ONLY.

The sensitivity analysis is executed only when the caller explicitly supplies:

    --execute

The original Experiment-08 mechanical evidence is immutable. This runner first
replays the frozen raster control and verifies that the replay reproduces the
committed mechanical evidence before deriving any new sensitivity quantities.

This analysis is diagnostic/post-outcome only. It cannot change the original
mechanical FAIL decision.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image
from scipy.stats import spearmanr


# =============================================================================
# PATHS / FROZEN CONTRACT
# =============================================================================

THIS_FILE = Path(__file__).resolve()
E8 = THIS_FILE.parent
PAPER_ROOT = E8.parent.parent
REPO_ROOT = PAPER_ROOT.parent.parent

MECHANICAL_SCRIPT = E8 / "run_mechanical_validation.py"
AMENDMENT = (
    REPO_ROOT
    / "docs"
    / "experiment-08"
    / "post-outcome-mechanical-sensitivity-amendment.md"
)

FROZEN_MECHANICAL_CSV = (
    PAPER_ROOT
    / "evidence"
    / "Experiment_08"
    / "experiment08_mechanical_validation.csv"
)

OUTPUT_DIR = (
    PAPER_ROOT
    / "evidence"
    / "Experiment_08"
)

OBSERVATION_OUTPUT = (
    OUTPUT_DIR
    / "experiment08_mechanical_sensitivity_observations.csv"
)

STRATA_OUTPUT = (
    OUTPUT_DIR
    / "experiment08_mechanical_sensitivity_strata.csv"
)

REGRESSION_OUTPUT = (
    OUTPUT_DIR
    / "experiment08_mechanical_sensitivity_regression.csv"
)

SUMMARY_OUTPUT = (
    OUTPUT_DIR
    / "experiment08_mechanical_sensitivity_summary.json"
)


EXPECTED_FROZEN_MECHANICAL_SHA256 = (
    "3a51a9045a70bfcd87ce9a96756385e25db9e0908b854bc66a5a515edf45ca71"
)

EXPECTED_COLUMNS = [
    "row_index",
    "relative_path",
    "category",
    "garment_id",
    "rotation_deg",
    "shell_index",
    "radial_center",
    "reference_R2",
    "shell_mass_fraction",
    "supported_shell",
    "relative_magnitude_error",
    "axial_error_deg",
]

EXPECTED_IDENTITIES = 230
EXPECTED_PRIMARY_SHELLS = 25
EXPECTED_ANGLES = 10
EXPECTED_OBSERVATIONS = (
    EXPECTED_IDENTITIES
    * EXPECTED_PRIMARY_SHELLS
    * EXPECTED_ANGLES
)

ORIGINAL_RELATIVE_ERROR_THRESHOLD = 0.15

# Numerical replay tolerance. This is only for checking floating-point
# serialization/replay equivalence; it is not a scientific gate.
REPLAY_ATOL = 1e-12
REPLAY_RTOL = 1e-12

R2_BIN_LABELS = [
    "[0,0.05)",
    "[0.05,0.10)",
    "[0.10,0.20)",
    "[0.20,0.40)",
    "[0.40,0.60)",
    "[0.60,0.80)",
    "[0.80,1.00]",
]


# =============================================================================
# HELPERS
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def import_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def json_safe_float(value):
    value = float(value)
    if np.isfinite(value):
        return value
    return None


def percentile95(series: pd.Series):
    values = series.dropna()
    if len(values) == 0:
        return np.nan
    return float(values.quantile(0.95))


def median_or_nan(series: pd.Series):
    values = series.dropna()
    if len(values) == 0:
        return np.nan
    return float(values.median())


# =============================================================================
# STRUCTURAL VALIDATION — NO SCIENTIFIC OUTCOME COMPUTATION
# =============================================================================

def validate_structure():
    print("=" * 92)
    print("EXPERIMENT 08 — MECHANICAL SENSITIVITY STRUCTURAL VALIDATION")
    print("=" * 92)

    for path in [
        MECHANICAL_SCRIPT,
        AMENDMENT,
        FROZEN_MECHANICAL_CSV,
    ]:
        if not path.is_file():
            raise RuntimeError(f"Missing required frozen input: {path}")

    observed_hash = sha256_file(
        FROZEN_MECHANICAL_CSV
    )

    print("Frozen mechanical CSV:")
    print(" ", FROZEN_MECHANICAL_CSV)
    print("Observed SHA-256:")
    print(" ", observed_hash)
    print("Expected SHA-256:")
    print(" ", EXPECTED_FROZEN_MECHANICAL_SHA256)

    if observed_hash != EXPECTED_FROZEN_MECHANICAL_SHA256:
        raise RuntimeError(
            "Frozen mechanical evidence hash mismatch. "
            "Sensitivity execution is blocked."
        )

    header = pd.read_csv(
        FROZEN_MECHANICAL_CSV,
        nrows=0,
    )

    observed_columns = header.columns.tolist()

    if observed_columns != EXPECTED_COLUMNS:
        raise RuntimeError(
            "Frozen mechanical CSV schema mismatch.\n"
            f"Observed: {observed_columns}\n"
            f"Expected: {EXPECTED_COLUMNS}"
        )

    mechanical = import_module(
        MECHANICAL_SCRIPT,
        "experiment08_mechanical_validation",
    )

    required_attributes = [
        "ANGLES",
        "DATASET_ROOT",
        "RA14_SCRIPT",
        "rotation_safe_canvas",
        "historical_rotate_safe_canvas",
        "radial_angular_single",
    ]

    missing = [
        name
        for name in required_attributes
        if not hasattr(mechanical, name)
    ]

    if missing:
        raise RuntimeError(
            "Frozen mechanical module missing required "
            f"attribute(s): {missing}"
        )

    if len(mechanical.ANGLES) != EXPECTED_ANGLES:
        raise RuntimeError(
            "Frozen mechanical angle count differs from "
            f"{EXPECTED_ANGLES}."
        )

    print()
    print("STRUCTURAL CONTRACT")
    print("-" * 92)
    print(f"Expected observations : {EXPECTED_OBSERVATIONS}")
    print(f"Expected identities   : {EXPECTED_IDENTITIES}")
    print(f"Expected shells       : {EXPECTED_PRIMARY_SHELLS}")
    print(f"Expected angles       : {EXPECTED_ANGLES}")
    print("Frozen CSV schema     : PASS")
    print("Frozen CSV hash       : PASS")
    print("Mechanical API        : PASS")
    print()
    print("NO RASTER REPLAY WAS RUN.")
    print("NO SENSITIVITY OUTCOME WAS COMPUTED.")
    print()
    print("Execution requires explicit --execute.")
    print("=" * 92)


# =============================================================================
# FROZEN POPULATION
# =============================================================================

def load_frozen_population() -> pd.DataFrame:
    frozen = pd.read_csv(
        FROZEN_MECHANICAL_CSV,
        keep_default_na=False,
    )

    if len(frozen) != EXPECTED_OBSERVATIONS:
        raise RuntimeError(
            "Frozen mechanical observation count mismatch: "
            f"{len(frozen)} != {EXPECTED_OBSERVATIONS}"
        )

    if frozen.columns.tolist() != EXPECTED_COLUMNS:
        raise RuntimeError(
            "Frozen mechanical CSV columns changed."
        )

    frozen["supported_shell"] = (
        frozen["supported_shell"]
        .astype(str)
        .map({"True": True, "False": False})
    )

    if frozen["supported_shell"].isna().any():
        raise RuntimeError(
            "Could not parse supported_shell as Boolean."
        )

    sample = (
        frozen[
            [
                "row_index",
                "relative_path",
                "category",
                "garment_id",
            ]
        ]
        .drop_duplicates()
        .sort_values("row_index")
        .reset_index(drop=True)
    )

    if len(sample) != EXPECTED_IDENTITIES:
        raise RuntimeError(
            f"Expected {EXPECTED_IDENTITIES} frozen sketches; "
            f"observed {len(sample)}."
        )

    if sample["garment_id"].nunique() != EXPECTED_IDENTITIES:
        raise RuntimeError(
            "Frozen mechanical population is not one sketch "
            "per garment identity."
        )

    expected_per_identity = (
        EXPECTED_PRIMARY_SHELLS
        * EXPECTED_ANGLES
    )

    counts = frozen.groupby(
        "garment_id",
        sort=False,
    ).size()

    if not (
        counts.to_numpy()
        == expected_per_identity
    ).all():
        raise RuntimeError(
            "Frozen mechanical CSV does not contain exactly "
            f"{expected_per_identity} observations per identity."
        )

    if frozen["rotation_deg"].nunique() != EXPECTED_ANGLES:
        raise RuntimeError(
            "Frozen mechanical rotation-angle count mismatch."
        )

    if frozen["shell_index"].nunique() != EXPECTED_PRIMARY_SHELLS:
        raise RuntimeError(
            "Frozen primary-shell count mismatch."
        )

    return frozen


# =============================================================================
# EXACT RASTER REPLAY + NEW R2'
# =============================================================================

def replay_population(
    frozen: pd.DataFrame,
    mechanical,
    ra14,
) -> pd.DataFrame:

    records = []

    identity_rows = (
        frozen[
            [
                "row_index",
                "relative_path",
                "category",
                "garment_id",
            ]
        ]
        .drop_duplicates()
        .sort_values("row_index")
        .reset_index(drop=True)
    )

    frozen_angles = (
        frozen["rotation_deg"]
        .drop_duplicates()
        .astype(float)
        .tolist()
    )

    mechanical_angles = (
        np.asarray(
            mechanical.ANGLES,
            dtype=np.float64,
        )
        .tolist()
    )

    if frozen_angles != mechanical_angles:
        raise RuntimeError(
            "Frozen CSV angle order differs from "
            "run_mechanical_validation.py."
        )

    shell_indices = (
        frozen["shell_index"]
        .drop_duplicates()
        .astype(int)
        .tolist()
    )

    if len(shell_indices) != EXPECTED_PRIMARY_SHELLS:
        raise RuntimeError(
            "Unexpected number of frozen primary shells."
        )

    for identity_number, row in enumerate(
        identity_rows.itertuples(index=False),
        start=1,
    ):
        image_path = (
            mechanical.DATASET_ROOT
            / str(row.relative_path)
        )

        if not image_path.is_file():
            raise FileNotFoundError(
                f"Missing CLO-SKET image: {image_path}"
            )

        with Image.open(image_path) as im:
            im.load()
            raw = np.asarray(
                im.convert("L"),
                dtype=np.uint8,
            )

        safe = mechanical.rotation_safe_canvas(
            raw
        )

        reference = mechanical.radial_angular_single(
            safe,
            ra14,
        )

        ref_R2 = np.asarray(
            reference["F2_mag"],
            dtype=np.float64,
        )

        ref_shell_mass = np.asarray(
            reference["shell_mass"],
            dtype=np.float64,
        )

        ref_total_mass = float(
            reference["total_mass"]
        )

        if (
            not np.isfinite(ref_total_mass)
            or ref_total_mass <= 0.0
        ):
            raise RuntimeError(
                f"Invalid total mass for {row.relative_path}"
            )

        for phi_deg in mechanical_angles:
            rotated = (
                mechanical.historical_rotate_safe_canvas(
                    safe,
                    phi_deg,
                )
            )

            current = (
                mechanical.radial_angular_single(
                    rotated,
                    ra14,
                )
            )

            current_R2 = np.asarray(
                current["F2_mag"],
                dtype=np.float64,
            )

            for shell_index in shell_indices:
                r2 = float(
                    ref_R2[shell_index]
                )

                r2_prime = float(
                    current_R2[shell_index]
                )

                if (
                    not np.isfinite(r2)
                    or not np.isfinite(r2_prime)
                ):
                    raise RuntimeError(
                        "Non-finite harmonic magnitude encountered."
                    )

                if (
                    r2 < -1e-12
                    or r2_prime < -1e-12
                ):
                    raise RuntimeError(
                        "Negative harmonic magnitude encountered."
                    )

                if (
                    r2 > 1.0 + 1e-12
                    or r2_prime > 1.0 + 1e-12
                ):
                    raise RuntimeError(
                        "Harmonic magnitude exceeds normalized [0,1] domain."
                    )

                shell_mass_fraction = float(
                    ref_shell_mass[shell_index]
                    / ref_total_mass
                )

                e_abs = abs(
                    r2_prime - r2
                )

                if r2 > 0.0:
                    e_rel = (
                        e_abs / r2
                    )
                else:
                    e_rel = np.nan

                denominator = (
                    r2_prime + r2
                )

                if denominator > 0.0:
                    e_sym = (
                        2.0
                        * e_abs
                        / denominator
                    )
                elif (
                    r2_prime == 0.0
                    and
                    r2 == 0.0
                ):
                    e_sym = 0.0
                else:
                    raise RuntimeError(
                        "Invalid E_sym denominator state."
                    )

                records.append(
                    {
                        "row_index":
                            int(row.row_index),

                        "relative_path":
                            str(row.relative_path),

                        "category":
                            str(row.category),

                        "garment_id":
                            str(row.garment_id),

                        "rotation_deg":
                            float(phi_deg),

                        "shell_index":
                            int(shell_index),

                        "reference_R2":
                            r2,

                        "rotated_R2":
                            r2_prime,

                        "shell_mass_fraction":
                            shell_mass_fraction,

                        "E_abs":
                            float(e_abs),

                        "E_rel":
                            float(e_rel),

                        "E_sym":
                            float(e_sym),
                    }
                )

        if (
            identity_number % 25 == 0
            or
            identity_number == len(identity_rows)
        ):
            print(
                "Sensitivity raster replay: "
                f"{identity_number}/{len(identity_rows)} identities",
                flush=True,
            )

    replay = pd.DataFrame(records)

    if len(replay) != EXPECTED_OBSERVATIONS:
        raise RuntimeError(
            "Replay observation count mismatch: "
            f"{len(replay)} != {EXPECTED_OBSERVATIONS}"
        )

    return replay


# =============================================================================
# REPLAY FIREWALL
# =============================================================================

def verify_replay(
    frozen: pd.DataFrame,
    replay: pd.DataFrame,
) -> dict:

    keys = [
        "row_index",
        "relative_path",
        "category",
        "garment_id",
        "rotation_deg",
        "shell_index",
    ]

    left = frozen.copy()
    right = replay.copy()

    merged = left.merge(
        right,
        on=keys,
        how="outer",
        validate="one_to_one",
        indicator=True,
        suffixes=("_frozen", "_replay"),
    )

    if not (
        merged["_merge"] == "both"
    ).all():
        raise RuntimeError(
            "Raster replay population does not match "
            "the frozen mechanical population."
        )

    comparisons = {}

    numeric_pairs = [
        (
            "reference_R2",
            "reference_R2_frozen",
            "reference_R2_replay",
        ),
        (
            "shell_mass_fraction",
            "shell_mass_fraction_frozen",
            "shell_mass_fraction_replay",
        ),
        (
            "relative_magnitude_error",
            "relative_magnitude_error",
            "E_rel",
        ),
    ]

    for label, frozen_column, replay_column in numeric_pairs:
        a = pd.to_numeric(
            merged[frozen_column],
            errors="coerce",
        ).to_numpy(dtype=np.float64)

        b = pd.to_numeric(
            merged[replay_column],
            errors="coerce",
        ).to_numpy(dtype=np.float64)

        same_nan = (
            np.isnan(a)
            ==
            np.isnan(b)
        )

        if not same_nan.all():
            raise RuntimeError(
                f"NaN pattern mismatch for {label}."
            )

        finite = (
            np.isfinite(a)
            &
            np.isfinite(b)
        )

        if finite.any():
            max_abs = float(
                np.max(
                    np.abs(
                        a[finite]
                        -
                        b[finite]
                    )
                )
            )
        else:
            max_abs = 0.0

        if not np.allclose(
            a[finite],
            b[finite],
            rtol=REPLAY_RTOL,
            atol=REPLAY_ATOL,
        ):
            raise RuntimeError(
                "Frozen mechanical replay mismatch for "
                f"{label}; max absolute difference "
                f"{max_abs:.3e}."
            )

        comparisons[label] = {
            "max_absolute_difference":
                max_abs,
            "passed":
                True,
        }

    # Reproduce the original supported-shell rule from the frozen module.
    expected_supported = (
        np.isfinite(
            replay["reference_R2"].to_numpy(
                dtype=np.float64
            )
        )
        &
        (
            replay["reference_R2"].to_numpy(
                dtype=np.float64
            )
            >= 0.05
        )
        &
        (
            replay[
                "shell_mass_fraction"
            ].to_numpy(
                dtype=np.float64
            )
            >= 0.001
        )
    )

    frozen_supported = (
        merged["supported_shell"]
        .astype(bool)
        .to_numpy()
    )

    if not np.array_equal(
        frozen_supported,
        expected_supported,
    ):
        raise RuntimeError(
            "Supported-shell replay differs from "
            "the frozen mechanical evidence."
        )

    comparisons[
        "supported_shell"
    ] = {
        "exact_match":
            True,
        "passed":
            True,
    }

    return comparisons


# =============================================================================
# R2 STRATA
# =============================================================================

def assign_r2_stratum(value: float) -> str:
    if not np.isfinite(value):
        raise RuntimeError(
            "Non-finite reference_R2 encountered."
        )

    if value < 0.0:
        raise RuntimeError(
            f"Negative reference_R2 encountered: {value}"
        )

    if value < 0.05:
        return R2_BIN_LABELS[0]
    if value < 0.10:
        return R2_BIN_LABELS[1]
    if value < 0.20:
        return R2_BIN_LABELS[2]
    if value < 0.40:
        return R2_BIN_LABELS[3]
    if value < 0.60:
        return R2_BIN_LABELS[4]
    if value < 0.80:
        return R2_BIN_LABELS[5]
    if value <= 1.0 + 1e-12:
        return R2_BIN_LABELS[6]

    raise RuntimeError(
        "reference_R2 exceeds the prespecified "
        f"[0,1] diagnostic domain: {value}"
    )


def build_strata(
    observations: pd.DataFrame,
) -> pd.DataFrame:

    observations = observations.copy()

    observations["R2_stratum"] = (
        observations["reference_R2"]
        .map(assign_r2_stratum)
    )

    rows = []

    for label in R2_BIN_LABELS:
        group = observations[
            observations["R2_stratum"]
            == label
        ].copy()

        e_rel_defined = (
            group["E_rel"].notna()
        )

        defined_group = group[
            e_rel_defined
        ]

        if len(defined_group) > 0:
            exceedance = float(
                np.mean(
                    defined_group["E_rel"]
                    .to_numpy(dtype=np.float64)
                    >
                    ORIGINAL_RELATIVE_ERROR_THRESHOLD
                )
            )
        else:
            exceedance = np.nan

        rows.append(
            {
                "R2_stratum":
                    label,

                "n_total":
                    int(len(group)),

                "n_E_rel_defined":
                    int(e_rel_defined.sum()),

                "median_E_abs":
                    median_or_nan(
                        group["E_abs"]
                    ),

                "p95_E_abs":
                    percentile95(
                        group["E_abs"]
                    ),

                "median_E_rel":
                    median_or_nan(
                        group["E_rel"]
                    ),

                "p95_E_rel":
                    percentile95(
                        group["E_rel"]
                    ),

                "median_E_sym":
                    median_or_nan(
                        group["E_sym"]
                    ),

                "p95_E_sym":
                    percentile95(
                        group["E_sym"]
                    ),

                "median_shell_mass_fraction":
                    median_or_nan(
                        group[
                            "shell_mass_fraction"
                        ]
                    ),

                "proportion_E_rel_gt_0p15_among_defined":
                    exceedance,
            }
        )

    return pd.DataFrame(rows)


# =============================================================================
# FULL-POPULATION SUMMARY
# =============================================================================

def summarize_population(
    observations: pd.DataFrame,
) -> dict:

    defined = observations[
        observations["E_rel"].notna()
    ].copy()

    if len(defined) > 0:
        exceedance = float(
            np.mean(
                defined["E_rel"]
                .to_numpy(dtype=np.float64)
                >
                ORIGINAL_RELATIVE_ERROR_THRESHOLD
            )
        )
    else:
        exceedance = np.nan

    return {
        "n_total":
            int(len(observations)),

        "n_E_rel_defined":
            int(len(defined)),

        "median_E_abs":
            json_safe_float(
                median_or_nan(
                    observations["E_abs"]
                )
            ),

        "p95_E_abs":
            json_safe_float(
                percentile95(
                    observations["E_abs"]
                )
            ),

        "median_E_rel":
            json_safe_float(
                median_or_nan(
                    observations["E_rel"]
                )
            ),

        "p95_E_rel":
            json_safe_float(
                percentile95(
                    observations["E_rel"]
                )
            ),

        "median_E_sym":
            json_safe_float(
                median_or_nan(
                    observations["E_sym"]
                )
            ),

        "p95_E_sym":
            json_safe_float(
                percentile95(
                    observations["E_sym"]
                )
            ),

        "median_shell_mass_fraction":
            json_safe_float(
                median_or_nan(
                    observations[
                        "shell_mass_fraction"
                    ]
                )
            ),

        "proportion_E_rel_gt_0p15_among_defined":
            json_safe_float(
                exceedance
            ),
    }


# =============================================================================
# ASSOCIATIONS
# =============================================================================

def compute_associations(
    observations: pd.DataFrame,
) -> dict:

    defined = observations[
        observations["E_rel"].notna()
    ].copy()

    if len(defined) == 0:
        raise RuntimeError(
            "No observations have mathematically "
            "defined E_rel."
        )

    rho_r2 = spearmanr(
        defined["reference_R2"].to_numpy(
            dtype=np.float64
        ),
        defined["E_rel"].to_numpy(
            dtype=np.float64
        ),
        nan_policy="raise",
    )

    rho_mass = spearmanr(
        defined[
            "shell_mass_fraction"
        ].to_numpy(
            dtype=np.float64
        ),
        defined["E_rel"].to_numpy(
            dtype=np.float64
        ),
        nan_policy="raise",
    )

    return {
        "n_total":
            int(len(observations)),

        "n_E_rel_defined":
            int(len(defined)),

        "spearman_R2_vs_E_rel": {
            "rho":
                json_safe_float(
                    rho_r2.statistic
                ),
        },

        "spearman_shell_mass_fraction_vs_E_rel": {
            "rho":
                json_safe_float(
                    rho_mass.statistic
                ),
        },
    }


# =============================================================================
# DESCRIPTIVE LOG1P REGRESSION
# =============================================================================

def fit_descriptive_model(
    observations: pd.DataFrame,
):
    defined = observations[
        observations["E_rel"].notna()
    ].copy()

    angles = sorted(
        defined["rotation_deg"]
        .astype(float)
        .unique()
        .tolist()
    )

    if len(angles) != EXPECTED_ANGLES:
        raise RuntimeError(
            "Unexpected number of angles in "
            "descriptive regression."
        )

    reference_angle = angles[0]

    y = np.log1p(
        defined["E_rel"]
        .to_numpy(dtype=np.float64)
    )

    columns = [
        np.ones(
            len(defined),
            dtype=np.float64,
        ),
        np.log1p(
            defined["reference_R2"]
            .to_numpy(dtype=np.float64)
        ),
        np.log1p(
            defined[
                "shell_mass_fraction"
            ].to_numpy(dtype=np.float64)
        ),
    ]

    names = [
        "intercept",
        "log1p_reference_R2",
        "log1p_shell_mass_fraction",
    ]

    rotation_values = (
        defined["rotation_deg"]
        .to_numpy(dtype=np.float64)
    )

    for angle in angles[1:]:
        columns.append(
            (
                rotation_values
                == angle
            ).astype(np.float64)
        )
        names.append(
            f"rotation_deg_{angle:g}"
        )

    X = np.column_stack(
        columns
    )

    beta, residuals, rank, singular_values = (
        np.linalg.lstsq(
            X,
            y,
            rcond=None,
        )
    )

    fitted = X @ beta
    residual = y - fitted

    sse = float(
        np.sum(
            residual**2
        )
    )

    rows = [
        {
            "term":
                name,
            "coefficient":
                float(coef),
        }
        for name, coef in zip(
            names,
            beta,
        )
    ]

    metadata = {
        "n":
            int(len(defined)),

        "reference_rotation_deg":
            float(reference_angle),

        "rank":
            int(rank),

        "n_parameters":
            int(X.shape[1]),

        "sum_squared_residuals":
            sse,

        "residual_rmse":
            float(
                np.sqrt(
                    np.mean(
                        residual**2
                    )
                )
            ),

        "singular_values":
            [
                float(x)
                for x in singular_values
            ],

        "model":
            (
                "log1p(E_rel) ~ "
                "log1p(reference_R2) + "
                "log1p(shell_mass_fraction) + "
                "categorical(rotation_deg)"
            ),
    }

    return (
        pd.DataFrame(rows),
        metadata,
    )


# =============================================================================
# EXECUTION
# =============================================================================

def execute():
    # Structural checks happen first.
    validate_structure()

    existing_outputs = [
        path
        for path in [
            OBSERVATION_OUTPUT,
            STRATA_OUTPUT,
            REGRESSION_OUTPUT,
            SUMMARY_OUTPUT,
        ]
        if path.exists()
    ]

    if existing_outputs:
        formatted = "\n".join(
            f"  {path}"
            for path in existing_outputs
        )
        raise RuntimeError(
            "Sensitivity output already exists; refusing to overwrite:\n"
            + formatted
        )

    print()
    print("=" * 92)
    print("EXPLICIT --execute RECEIVED")
    print("Beginning frozen raster replay.")
    print("=" * 92)

    mechanical = import_module(
        MECHANICAL_SCRIPT,
        "experiment08_mechanical_validation_execute",
    )

    ra14 = import_module(
        mechanical.RA14_SCRIPT,
        "experiment08_ra14_sensitivity",
    )

    frozen = load_frozen_population()

    replay = replay_population(
        frozen,
        mechanical,
        ra14,
    )

    print()
    print("VERIFYING MAGNITUDE-SIDE REPLAY AGAINST FROZEN MECHANICAL EVIDENCE")
    print("-" * 92)

    replay_audit = verify_replay(
        frozen,
        replay,
    )

    print("Frozen magnitude-side replay verification: PASS")
    print()
    print(
        "Only now deriving post-outcome "
        "sensitivity diagnostics."
    )

    observations = replay.copy()

    observations["R2_stratum"] = (
        observations["reference_R2"]
        .map(assign_r2_stratum)
    )

    full_population_summary = (
        summarize_population(
            observations
        )
    )

    strata = build_strata(
        observations
    )

    associations = compute_associations(
        observations
    )

    regression, regression_metadata = (
        fit_descriptive_model(
            observations
        )
    )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    observations.to_csv(
        OBSERVATION_OUTPUT,
        index=False,
    )

    strata.to_csv(
        STRATA_OUTPUT,
        index=False,
    )

    regression.to_csv(
        REGRESSION_OUTPUT,
        index=False,
    )

    summary = {
        "experiment":
            "CLO-SKET Experiment 08",

        "stage":
            "POST_OUTCOME_MECHANICAL_SENSITIVITY",

        "status":
            "DIAGNOSTIC_ONLY",

        "original_mechanical_gate_remains_failed":
            True,

        "retroactive_gate_change_permitted":
            False,

        "population": {
            "n_total":
                int(len(observations)),

            "n_identities":
                int(
                    observations[
                        "garment_id"
                    ].nunique()
                ),

            "n_primary_shells":
                int(
                    observations[
                        "shell_index"
                    ].nunique()
                ),

            "n_rotation_angles":
                int(
                    observations[
                        "rotation_deg"
                    ].nunique()
                ),

            "n_E_rel_defined":
                int(
                    observations[
                        "E_rel"
                    ].notna().sum()
                ),

            "n_reference_R2_zero":
                int(
                    (
                        observations[
                            "reference_R2"
                        ]
                        == 0.0
                    ).sum()
                ),
        },

        "zero_R2_rule": {
            "E_abs":
                "defined for all observations",

            "E_rel":
                "undefined/NA when reference_R2 == 0",

            "E_sym":
                (
                    "2*abs(R2_prime-R2)/(R2_prime+R2); "
                    "defined as 0 when both magnitudes are exactly 0"
                ),

            "epsilon_denominator_used":
                False,
        },

        "original_relative_error_threshold":
            ORIGINAL_RELATIVE_ERROR_THRESHOLD,

        "support_variable": {
            "symbol":
                "m",

            "operational_definition":
                (
                    "reference shell_mass_fraction = "
                    "reference shell mass / "
                    "reference total foreground mass"
                ),

            "boolean_supported_shell_used_in_association_or_regression":
                False,
        },

        "full_population_summary":
            full_population_summary,

        "replay_audit":
            replay_audit,

        "associations":
            associations,

        "descriptive_regression":
            regression_metadata,

        "inputs": {
            "frozen_mechanical_csv":
                str(
                    FROZEN_MECHANICAL_CSV
                ),

            "frozen_mechanical_csv_sha256":
                sha256_file(
                    FROZEN_MECHANICAL_CSV
                ),

            "mechanical_script":
                str(
                    MECHANICAL_SCRIPT
                ),

            "mechanical_script_sha256":
                sha256_file(
                    MECHANICAL_SCRIPT
                ),

            "amendment":
                str(
                    AMENDMENT
                ),

            "amendment_sha256":
                sha256_file(
                    AMENDMENT
                ),
        },

        "outputs": {
            "observations":
                str(
                    OBSERVATION_OUTPUT
                ),

            "strata":
                str(
                    STRATA_OUTPUT
                ),

            "regression":
                str(
                    REGRESSION_OUTPUT
                ),
        },
    }

    SUMMARY_OUTPUT.write_text(
        json.dumps(
            summary,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print()
    print("=" * 92)
    print("POST-OUTCOME MECHANICAL SENSITIVITY COMPLETE")
    print("=" * 92)
    print(
        "Original mechanical gate remains: FAIL"
    )
    print(
        "Interpretation status: diagnostic/post-outcome only"
    )
    print()
    print("Outputs:")
    print(" ", OBSERVATION_OUTPUT)
    print(" ", STRATA_OUTPUT)
    print(" ", REGRESSION_OUTPUT)
    print(" ", SUMMARY_OUTPUT)


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    mode = parser.add_mutually_exclusive_group()

    mode.add_argument(
        "--validate-structure",
        action="store_true",
        help=(
            "Validate frozen inputs/schema/API only. "
            "No raster replay and no sensitivity outcomes."
        ),
    )

    mode.add_argument(
        "--execute",
        action="store_true",
        help=(
            "Explicitly execute the post-outcome "
            "mechanical sensitivity analysis."
        ),
    )

    args = parser.parse_args()

    if args.execute:
        execute()
        return

    # Default is deliberately non-executing.
    validate_structure()


if __name__ == "__main__":
    main()
