from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw


# =============================================================================
# PATHS / FROZEN CONTRACT
# =============================================================================

E8 = Path(__file__).resolve().parent
PAPER_ROOT = E8.parent.parent
EVIDENCE = PAPER_ROOT / "evidence" / "Experiment_08"

DATASET_ROOT = Path("/Users/nitikagupta/Desktop/Clo-Sket")

RA14_SCRIPT = E8 / "extract_ra14_features.py"
RA14_FEATURES = E8 / "experiment08_ra14_features.npy"
RA14_ROW_MANIFEST = E8 / "experiment08_ra14_source_manifest.csv"
RA14_LOCK = E8 / "experiment08_ra14_manifest.json"
PREFLIGHT_SCRIPT = E8 / "preflight.py"

EXPECTED_ROWS = 2300
EXPECTED_IDENTITIES = 230
EXPECTED_CATEGORIES = 23

ANGLES = np.asarray(
    [-90.0, -60.0, -45.0, -30.0, -15.0,
      15.0,  30.0,  45.0,  60.0,  90.0],
    dtype=np.float64,
)

# Frozen exact analytic gates.
ANALYTIC_MAG_TOL = 1e-12
ANALYTIC_VECTOR_TOL = 1e-12

# Frozen supported-shell definition.
MIN_R2 = 0.05
MIN_SHELL_MASS_FRACTION = 0.001

# Frozen raster descriptive gates.
MEDIAN_MAG_GATE = 0.05
P95_MAG_GATE = 0.15
MEDIAN_AXIAL_GATE = 5.0
P95_AXIAL_GATE = 15.0


# =============================================================================
# GENERIC HELPERS
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_array(array: np.ndarray) -> str:
    arr = np.ascontiguousarray(array)
    return hashlib.sha256(arr.tobytes()).hexdigest()


def import_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)

    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not import {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def axial_distance_deg(a, b):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)

    d = np.mod(np.abs(a - b), 180.0)

    return np.minimum(d, 180.0 - d)


def signed_axial_difference_deg(a, b):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)

    return (
        (a - b + 90.0) % 180.0
        - 90.0
    )


# =============================================================================
# HISTORICAL PAPER-I RASTER OPERATOR
# =============================================================================

def rotation_safe_canvas(gray):
    """
    Historical 05_Rotation_Controls.ipynb rule.

    Square side = ceil(sqrt(h^2 + w^2)), with the historical parity
    adjustment. Original grayscale image is centered on white.
    """

    gray = np.asarray(gray, dtype=np.uint8)

    if gray.ndim != 2:
        raise RuntimeError(
            f"Expected 2-D grayscale image, got {gray.shape}."
        )

    h, w = gray.shape

    side = int(
        np.ceil(
            np.sqrt(
                h * h + w * w
            )
        )
    )

    if (side - w) % 2 != 0:
        side += 1

    canvas = np.full(
        (side, side),
        255,
        dtype=np.uint8,
    )

    y0 = (side - h) // 2
    x0 = (side - w) // 2

    canvas[
        y0:y0 + h,
        x0:x0 + w,
    ] = gray

    return canvas


def historical_rotate_safe_canvas(safe, angle_deg):
    pil = Image.fromarray(
        np.asarray(safe, dtype=np.uint8),
        mode="L",
    )

    if float(angle_deg) == 0.0:
        rotated = pil
    else:
        rotated = pil.rotate(
            float(angle_deg),
            resample=Image.Resampling.BILINEAR,
            expand=False,
            fillcolor=255,
        )

    return np.asarray(
        rotated,
        dtype=np.uint8,
    )


# =============================================================================
# SINGLE-IMAGE FROZEN RA14 FIELD RECOVERY
# =============================================================================

def radial_angular_single(gray, ra14):
    """
    Single-image equivalent of the frozen Experiment-08 RA14 extractor.

    Keeps the frozen native image-axis convention:
        Theta = atan2(Yc, Xc)
    where image Y increases downward.
    """

    img = np.asarray(
        gray,
        dtype=np.float64,
    )

    if img.ndim != 2:
        raise RuntimeError(
            f"Expected 2-D grayscale image, got {img.shape}."
        )

    if not np.isfinite(img).all():
        raise RuntimeError(
            "Non-finite grayscale image."
        )

    w = np.maximum(
        255.0 - img,
        0.0,
    )

    total_mass = float(np.sum(w))

    if (
        not np.isfinite(total_mass)
        or total_mass <= 0.0
    ):
        raise RuntimeError(
            "Invalid foreground mass."
        )

    height, width = w.shape

    S = float(max(width, height))

    x = (
        np.arange(width, dtype=np.float64)
        - (width - 1) / 2.0
    ) / S

    y = (
        np.arange(height, dtype=np.float64)
        - (height - 1) / 2.0
    ) / S

    X, Y = np.meshgrid(x, y)

    cx = float(
        np.sum(w * X) / total_mass
    )

    cy = float(
        np.sum(w * Y) / total_mass
    )

    Xc = X - cx
    Yc = Y - cy

    R = np.sqrt(
        Xc**2 + Yc**2
    )

    Theta = np.arctan2(
        Yc,
        Xc,
    )

    Rmax = float(np.max(R))

    if Rmax <= 0.0:
        raise RuntimeError(
            "Invalid radial extent."
        )

    Rnorm = np.clip(
        R / Rmax,
        0.0,
        1.0,
    )

    r_edges = np.linspace(
        0.0,
        1.0,
        ra14.N_RADIAL + 1,
    )

    theta_edges = np.linspace(
        -np.pi,
        np.pi,
        ra14.N_ANGULAR + 1,
    )

    r_idx = (
        np.searchsorted(
            r_edges,
            Rnorm,
            side="right",
        )
        - 1
    )

    theta_idx = (
        np.searchsorted(
            theta_edges,
            Theta,
            side="right",
        )
        - 1
    )

    r_idx = np.clip(
        r_idx,
        0,
        ra14.N_RADIAL - 1,
    )

    theta_idx = np.clip(
        theta_idx,
        0,
        ra14.N_ANGULAR - 1,
    )

    joint_mass = np.zeros(
        (
            ra14.N_RADIAL,
            ra14.N_ANGULAR,
        ),
        dtype=np.float64,
    )

    valid = (
        np.isfinite(w)
        & np.isfinite(Rnorm)
        & np.isfinite(Theta)
    )

    np.add.at(
        joint_mass,
        (
            r_idx[valid],
            theta_idx[valid],
        ),
        w[valid],
    )

    recovered_mass = float(
        joint_mass.sum()
    )

    relative_mass_error = (
        abs(recovered_mass - total_mass)
        / total_mass
    )

    if relative_mass_error > ra14.MASS_TOL:
        raise RuntimeError(
            "Mass conservation failure: "
            f"{relative_mass_error:.3e}"
        )

    shell_mass = joint_mass.sum(
        axis=1
    )

    conditional = np.zeros_like(
        joint_mass
    )

    nonempty = (
        shell_mass > ra14.MASS_EPS
    )

    conditional[
        nonempty,
        :
    ] = (
        joint_mass[
            nonempty,
            :
        ]
        / shell_mass[
            nonempty,
            None,
        ]
    )

    F2_mag, alpha2_deg = (
        ra14.recover_f2(
            conditional[
                None,
                :,
                :,
            ]
        )
    )

    return {
        "F2_mag":
            F2_mag[0],

        "alpha2_deg":
            alpha2_deg[0],

        "shell_mass":
            shell_mass,

        "total_mass":
            total_mass,
    }


# =============================================================================
# FROZEN 14-D MATRIX VALIDITY / RANGE AUDIT
# =============================================================================

def audit_ra14_matrix():
    lock = json.loads(
        RA14_LOCK.read_text(
            encoding="utf-8"
        )
    )

    X = np.load(
        RA14_FEATURES,
        allow_pickle=False,
    )

    if X.shape != (EXPECTED_ROWS, 14):
        raise RuntimeError(
            f"Unexpected RA14 matrix shape: {X.shape}"
        )

    if not np.isfinite(X).all():
        raise RuntimeError(
            "Frozen RA14 matrix contains non-finite values."
        )

    if (
        sha256_file(RA14_FEATURES)
        != lock["saved_npy_sha256"]
    ):
        raise RuntimeError(
            "Frozen RA14 NPY SHA does not match its manifest."
        )

    if (
        sha256_array(X)
        != lock["array_sha256"]
    ):
        raise RuntimeError(
            "Frozen RA14 raw-array SHA does not match its manifest."
        )

    # Four doubled-angle coordinates.
    trig = X[:, 8:12]

    if np.any(trig < -1.0 - 1e-12):
        raise RuntimeError(
            "RA14 doubled-angle coordinate below -1."
        )

    if np.any(trig > 1.0 + 1e-12):
        raise RuntimeError(
            "RA14 doubled-angle coordinate above +1."
        )

    coherence = X[:, 12]

    if np.any(coherence < -1e-12):
        raise RuntimeError(
            "RA14 axial coherence below 0."
        )

    if np.any(coherence > 1.0 + 1e-12):
        raise RuntimeError(
            "RA14 axial coherence above 1."
        )

    drift = X[:, 13]

    if np.any(drift < -1e-12):
        raise RuntimeError(
            "RA14 axial drift below 0 degrees."
        )

    if np.any(drift > 90.0 + 1e-12):
        raise RuntimeError(
            "RA14 axial drift above 90 degrees."
        )

    return {
        "shape":
            list(X.shape),

        "finite":
            True,

        "saved_npy_sha256":
            sha256_file(
                RA14_FEATURES
            ),

        "array_sha256":
            sha256_array(X),

        "range_checks_pass":
            True,
    }


# =============================================================================
# EXACT ANALYTIC TRANSFORMATION GATE
# =============================================================================

def analytic_gate():
    theta = np.linspace(
        -np.pi,
        np.pi,
        720,
        endpoint=False,
        dtype=np.float64,
    )

    test_axes_deg = [
        0.0,
        11.0,
        37.0,
        71.0,
        123.0,
        169.0,
    ]

    records = []

    max_mag_error = 0.0
    max_vector_error = 0.0

    for base_axis_deg in test_axes_deg:
        base_axis_rad = np.deg2rad(
            base_axis_deg
        )

        p = (
            1.0
            +
            0.60
            * np.cos(
                2.0
                * (
                    theta
                    - base_axis_rad
                )
            )
        )

        p = p / p.sum()

        F2 = np.sum(
            p
            * np.exp(
                -2j * theta
            )
        )

        R2 = float(
            np.abs(F2)
        )

        alpha = (
            np.degrees(
                -0.5
                * np.angle(F2)
            )
            % 180.0
        )

        u = np.asarray(
            [
                np.cos(
                    2.0
                    * np.deg2rad(alpha)
                ),
                np.sin(
                    2.0
                    * np.deg2rad(alpha)
                ),
            ],
            dtype=np.float64,
        )

        for phi_deg in ANGLES:
            phi = np.deg2rad(
                phi_deg
            )

            F2_prime = (
                np.exp(
                    -2j * phi
                )
                * F2
            )

            R2_prime = float(
                np.abs(F2_prime)
            )

            alpha_prime = (
                np.degrees(
                    -0.5
                    * np.angle(
                        F2_prime
                    )
                )
                % 180.0
            )

            u_prime = np.asarray(
                [
                    np.cos(
                        2.0
                        * np.deg2rad(
                            alpha_prime
                        )
                    ),
                    np.sin(
                        2.0
                        * np.deg2rad(
                            alpha_prime
                        )
                    ),
                ],
                dtype=np.float64,
            )

            rotation_2phi = np.asarray(
                [
                    [
                        np.cos(2.0 * phi),
                        -np.sin(2.0 * phi),
                    ],
                    [
                        np.sin(2.0 * phi),
                        np.cos(2.0 * phi),
                    ],
                ],
                dtype=np.float64,
            )

            expected_u = (
                rotation_2phi @ u
            )

            mag_error = abs(
                R2_prime - R2
            )

            vector_error = float(
                np.linalg.norm(
                    u_prime
                    - expected_u
                )
            )

            max_mag_error = max(
                max_mag_error,
                mag_error,
            )

            max_vector_error = max(
                max_vector_error,
                vector_error,
            )

            records.append({
                "base_axis_deg":
                    base_axis_deg,

                "rotation_deg":
                    float(phi_deg),

                "magnitude_error":
                    mag_error,

                "doubled_angle_vector_error":
                    vector_error,
            })

    passed = bool(
        max_mag_error
        < ANALYTIC_MAG_TOL
        and
        max_vector_error
        < ANALYTIC_VECTOR_TOL
    )

    return (
        pd.DataFrame(records),
        {
            "max_magnitude_error":
                max_mag_error,

            "max_doubled_angle_vector_error":
                max_vector_error,

            "magnitude_tolerance":
                ANALYTIC_MAG_TOL,

            "vector_tolerance":
                ANALYTIC_VECTOR_TOL,

            "passed":
                passed,
        },
    )


# =============================================================================
# SYNTHETIC IMAGE-COORDINATE SIGN GATE
# =============================================================================

def synthetic_sign_gate(ra14, primary_mask):
    """
    Construct a horizontal axis and rotate it visually CCW by +30 degrees.
    Determine the one global sign relation used by the raster audit.
    """

    size = 257

    image = Image.new(
        "L",
        (size, size),
        255,
    )

    draw = ImageDraw.Draw(image)

    center = size // 2

    draw.line(
        (
            35,
            center,
            size - 36,
            center,
        ),
        fill=0,
        width=5,
    )

    raw = np.asarray(
        image,
        dtype=np.uint8,
    )

    safe = rotation_safe_canvas(
        raw
    )

    reference = radial_angular_single(
        safe,
        ra14,
    )

    rotated = historical_rotate_safe_canvas(
        safe,
        30.0,
    )

    rotated_fields = radial_angular_single(
        rotated,
        ra14,
    )

    ref_weights = (
        reference["F2_mag"][
            primary_mask
        ]
    )

    rot_weights = (
        rotated_fields["F2_mag"][
            primary_mask
        ]
    )

    ref_alpha = ra14.axial_mean_deg(
        reference["alpha2_deg"][
            primary_mask
        ][None, :],
        ref_weights[
            None,
            :
        ],
    )[0]

    rot_alpha = ra14.axial_mean_deg(
        rotated_fields["alpha2_deg"][
            primary_mask
        ][None, :],
        rot_weights[
            None,
            :
        ],
    )[0]

    observed_shift = float(
        signed_axial_difference_deg(
            rot_alpha,
            ref_alpha,
        )
    )

    plus_error = float(
        axial_distance_deg(
            observed_shift,
            +30.0,
        )
    )

    minus_error = float(
        axial_distance_deg(
            observed_shift,
            -30.0,
        )
    )

    if plus_error < minus_error:
        sign = +1.0
        relation = (
            "alpha_rot - alpha_ref ≈ +phi"
        )
    elif minus_error < plus_error:
        sign = -1.0
        relation = (
            "alpha_rot - alpha_ref ≈ -phi"
        )
    else:
        raise RuntimeError(
            "Synthetic sign convention is ambiguous."
        )

    return {
        "reference_alpha_deg":
            float(ref_alpha),

        "rotated_alpha_deg":
            float(rot_alpha),

        "observed_shift_deg":
            observed_shift,

        "plus_phi_error_deg":
            plus_error,

        "minus_phi_error_deg":
            minus_error,

        "sign":
            sign,

        "relation":
            relation,
    }


# =============================================================================
# RASTER CONTROL
# =============================================================================

def raster_gate(
    sample,
    ra14,
    primary_mask,
    sign,
):
    records = []

    primary_shell_indices = np.flatnonzero(
        primary_mask
    )

    for sample_number, row in enumerate(
        sample.itertuples(index=False),
        start=1,
    ):
        path = (
            DATASET_ROOT
            / row.relative_path
        )

        with Image.open(path) as im:
            im.load()

            raw = np.asarray(
                im.convert("L"),
                dtype=np.uint8,
            )

        safe = rotation_safe_canvas(
            raw
        )

        ref = radial_angular_single(
            safe,
            ra14,
        )

        ref_R2 = ref[
            "F2_mag"
        ]

        ref_alpha = ref[
            "alpha2_deg"
        ]

        ref_shell_mass = ref[
            "shell_mass"
        ]

        ref_total_mass = ref[
            "total_mass"
        ]

        support = (
            primary_mask
            &
            np.isfinite(ref_R2)
            &
            np.isfinite(ref_alpha)
            &
            (ref_R2 >= MIN_R2)
            &
            (
                ref_shell_mass
                >= (
                    MIN_SHELL_MASS_FRACTION
                    * ref_total_mass
                )
            )
        )

        for phi_deg in ANGLES:
            rotated = historical_rotate_safe_canvas(
                safe,
                phi_deg,
            )

            current = radial_angular_single(
                rotated,
                ra14,
            )

            current_R2 = current[
                "F2_mag"
            ]

            current_alpha = current[
                "alpha2_deg"
            ]

            expected_alpha = (
                ref_alpha
                + sign
                * float(phi_deg)
            ) % 180.0

            rel_mag_error = np.divide(
                np.abs(
                    current_R2
                    - ref_R2
                ),
                ref_R2,
                out=np.full(
                    ref_R2.shape,
                    np.nan,
                    dtype=np.float64,
                ),
                where=ref_R2 > 0.0,
            )

            axial_error = axial_distance_deg(
                current_alpha,
                expected_alpha,
            )

            for shell_index in primary_shell_indices:
                records.append({
                    "row_index":
                        int(row.row_index),

                    "relative_path":
                        row.relative_path,

                    "category":
                        row.category,

                    "garment_id":
                        row.garment_id,

                    "rotation_deg":
                        float(phi_deg),

                    "shell_index":
                        int(shell_index),

                    "radial_center":
                        float(
                            shell_index
                            + 0.5
                        ),

                    "reference_R2":
                        float(
                            ref_R2[
                                shell_index
                            ]
                        ),

                    "shell_mass_fraction":
                        float(
                            ref_shell_mass[
                                shell_index
                            ]
                            / ref_total_mass
                        ),

                    "supported_shell":
                        bool(
                            support[
                                shell_index
                            ]
                        ),

                    "relative_magnitude_error":
                        float(
                            rel_mag_error[
                                shell_index
                            ]
                        ),

                    "axial_error_deg":
                        float(
                            axial_error[
                                shell_index
                            ]
                        ),
                })

        if (
            sample_number % 25 == 0
            or sample_number == len(sample)
        ):
            print(
                "Raster audit: "
                f"{sample_number}/{len(sample)} identities",
                flush=True,
            )

    return pd.DataFrame(records)


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 88)
    print("EXPERIMENT 08 — RA14 MECHANICAL VALIDATION")
    print("=" * 88)

    for path in [
        RA14_SCRIPT,
        RA14_FEATURES,
        RA14_ROW_MANIFEST,
        RA14_LOCK,
        PREFLIGHT_SCRIPT,
    ]:
        if not path.is_file():
            raise RuntimeError(
                f"Missing frozen input: {path}"
            )

    ra14 = import_module(
        RA14_SCRIPT,
        "experiment08_ra14",
    )

    pf = import_module(
        PREFLIGHT_SCRIPT,
        "experiment08_preflight",
    )

    # -------------------------------------------------------------------------
    # 1. Frozen RA14 matrix
    # -------------------------------------------------------------------------

    matrix_audit = (
        audit_ra14_matrix()
    )

    print("\nFROZEN RA14 MATRIX")
    print("-" * 88)
    print("Shape        :", matrix_audit["shape"])
    print("Finite       :", matrix_audit["finite"])
    print("Range checks :", matrix_audit["range_checks_pass"])

    # -------------------------------------------------------------------------
    # 2. Corrected authoritative identity map
    # -------------------------------------------------------------------------

    manifest = pd.read_csv(
        RA14_ROW_MANIFEST,
        keep_default_na=False,
    )

    if len(manifest) != EXPECTED_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_ROWS} rows, found {len(manifest)}."
        )

    for column in [
        "row_index",
        "relative_path",
        "category",
    ]:
        if column not in manifest.columns:
            raise RuntimeError(
                f"RA14 source manifest missing {column}."
            )

    if manifest["row_index"].tolist() != list(range(EXPECTED_ROWS)):
        raise RuntimeError(
            "RA14 source row_index is not 0..2299."
        )

    rows_historical, historical_audit = (
        pf.validate_public_maps(
            pf.DEFAULT_ROW_MAP,
            pf.DEFAULT_FOLD_MAP,
        )
    )

    rows_corrected, corrected_audit = (
        pf.apply_identity_overrides(
            rows_historical,
            pf.DEFAULT_IDENTITY_OVERRIDES,
            historical_audit,
        )
    )

    authoritative_paths = (
        rows_corrected[
            "image_path_runtime"
        ]
        .map(
            pf.normalized_relative_path
        )
        .tolist()
    )

    if (
        manifest["relative_path"].tolist()
        != authoritative_paths
    ):
        raise RuntimeError(
            "RA14 source paths differ from corrected authoritative order."
        )

    if (
        manifest["category"].astype(str).tolist()
        != rows_corrected["category"].astype(str).tolist()
    ):
        raise RuntimeError(
            "RA14 source categories differ from corrected authoritative map."
        )

    manifest = manifest.copy()

    manifest["garment_id"] = (
        rows_corrected[
            "garment_id"
        ]
        .astype(str)
        .to_numpy()
    )

    if manifest["garment_id"].nunique() != EXPECTED_IDENTITIES:
        raise RuntimeError(
            "Expected 230 corrected garment identities."
        )

    if manifest["category"].nunique() != EXPECTED_CATEGORIES:
        raise RuntimeError(
            "Expected 23 categories."
        )

    # Prespecified one image per identity:
    # first authoritative row_index.
    sample = (
        manifest
        .sort_values("row_index")
        .groupby(
            "garment_id",
            sort=True,
        )
        .head(1)
        .sort_values("row_index")
        .reset_index(drop=True)
    )

    if len(sample) != EXPECTED_IDENTITIES:
        raise RuntimeError(
            f"Expected 230 mechanical-control sketches, found {len(sample)}."
        )

    if sample["garment_id"].nunique() != EXPECTED_IDENTITIES:
        raise RuntimeError(
            "Mechanical sample is not one row per identity."
        )

    print("\nPRESPECIFIED SAMPLE")
    print("-" * 88)
    print("Sketches   :", len(sample))
    print("Identities :", sample["garment_id"].nunique())
    print("Categories :", sample["category"].nunique())
    print("Selection  : first authoritative row_index per garment_id")

    # -------------------------------------------------------------------------
    # 3. Primary radial domain
    # -------------------------------------------------------------------------

    radial_centers = (
        np.arange(
            ra14.N_RADIAL,
            dtype=np.float64,
        )
        + 0.5
    )

    primary_mask = (
        (radial_centers >= ra14.PRIMARY_RADIUS_MIN)
        &
        (radial_centers <= ra14.PRIMARY_RADIUS_MAX)
    )

    if int(primary_mask.sum()) != 25:
        raise RuntimeError(
            "Expected exactly 25 primary RA14 shells."
        )

    # -------------------------------------------------------------------------
    # 4. Exact analytic gate
    # -------------------------------------------------------------------------

    analytic_df, analytic_summary = (
        analytic_gate()
    )

    print("\nANALYTIC EXACT GATE")
    print("-" * 88)
    print(
        "max |R2' - R2|           :",
        f"{analytic_summary['max_magnitude_error']:.3e}",
    )
    print(
        "max doubled-vector error :",
        f"{analytic_summary['max_doubled_angle_vector_error']:.3e}",
    )
    print(
        "PASS                      :",
        analytic_summary["passed"],
    )

    if not analytic_summary["passed"]:
        raise RuntimeError(
            "Analytic exact gate failed; raster gate blocked."
        )

    # -------------------------------------------------------------------------
    # 5. Synthetic coordinate sign
    # -------------------------------------------------------------------------

    sign_summary = (
        synthetic_sign_gate(
            ra14,
            primary_mask,
        )
    )

    print("\nSYNTHETIC +30 DEGREE SIGN TEST")
    print("-" * 88)
    print(
        "Observed shift :",
        f"{sign_summary['observed_shift_deg']:+.6f} deg",
    )
    print(
        "Relation       :",
        sign_summary["relation"],
    )

    # -------------------------------------------------------------------------
    # 6. Raster control
    # -------------------------------------------------------------------------

    print("\nRASTER CONTROL")
    print("-" * 88)
    print(
        "Angles   :",
        ANGLES.tolist(),
    )
    print(
        "Operator : rotation_safe_canvas -> "
        "PIL.Image.rotate(BILINEAR, expand=False, fillcolor=255)"
    )
    print(
        "Domain   : 25 locked RA14 primary shells"
    )

    raster = raster_gate(
        sample,
        ra14,
        primary_mask,
        sign_summary["sign"],
    )

    supported = raster[
        raster["supported_shell"]
    ].copy()

    low_support = raster[
        ~raster["supported_shell"]
    ].copy()

    if len(supported) == 0:
        raise RuntimeError(
            "No supported raster shell observations."
        )

    if not np.isfinite(
        supported[
            "relative_magnitude_error"
        ]
    ).all():
        raise RuntimeError(
            "Supported shells contain non-finite magnitude errors."
        )

    if not np.isfinite(
        supported[
            "axial_error_deg"
        ]
    ).all():
        raise RuntimeError(
            "Supported shells contain non-finite axial errors."
        )

    median_mag = float(
        supported[
            "relative_magnitude_error"
        ].median()
    )

    p95_mag = float(
        supported[
            "relative_magnitude_error"
        ].quantile(0.95)
    )

    median_axial = float(
        supported[
            "axial_error_deg"
        ].median()
    )

    p95_axial = float(
        supported[
            "axial_error_deg"
        ].quantile(0.95)
    )

    magnitude_pass = bool(
        median_mag <= MEDIAN_MAG_GATE
        and
        p95_mag <= P95_MAG_GATE
    )

    axial_pass = bool(
        median_axial <= MEDIAN_AXIAL_GATE
        and
        p95_axial <= P95_AXIAL_GATE
    )

    raster_pass = bool(
        magnitude_pass
        and
        axial_pass
    )

    mag_failure_rate = float(
        np.mean(
            supported[
                "relative_magnitude_error"
            ].to_numpy()
            > P95_MAG_GATE
        )
    )

    axial_failure_rate = float(
        np.mean(
            supported[
                "axial_error_deg"
            ].to_numpy()
            > P95_AXIAL_GATE
        )
    )

    combined_failure_rate = float(
        np.mean(
            (
                supported[
                    "relative_magnitude_error"
                ].to_numpy()
                > P95_MAG_GATE
            )
            |
            (
                supported[
                    "axial_error_deg"
                ].to_numpy()
                > P95_AXIAL_GATE
            )
        )
    )

    print("\nSUPPORTED-SHELL RESULTS")
    print("-" * 88)
    print(
        "Supported observations    :",
        len(supported),
    )
    print(
        "Low-support observations  :",
        len(low_support),
    )
    print(
        "Median relative mag error :",
        f"{median_mag:.6f}",
    )
    print(
        "P95 relative mag error    :",
        f"{p95_mag:.6f}",
    )
    print(
        "Median axial error (deg)  :",
        f"{median_axial:.6f}",
    )
    print(
        "P95 axial error (deg)     :",
        f"{p95_axial:.6f}",
    )
    print(
        "Magnitude gate PASS       :",
        magnitude_pass,
    )
    print(
        "Axial gate PASS           :",
        axial_pass,
    )

    # -------------------------------------------------------------------------
    # 7. R2-stratified diagnostics
    # -------------------------------------------------------------------------

    bins = [
        0.05,
        0.10,
        0.20,
        0.40,
        0.60,
        0.80,
        np.inf,
    ]

    labels = [
        "[0.05,0.10)",
        "[0.10,0.20)",
        "[0.20,0.40)",
        "[0.40,0.60)",
        "[0.60,0.80)",
        "[0.80,inf)",
    ]

    supported["R2_stratum"] = pd.cut(
        supported["reference_R2"],
        bins=bins,
        labels=labels,
        right=False,
    )

    strata = (
        supported
        .groupby(
            "R2_stratum",
            observed=False,
        )
        .agg(
            n=(
                "relative_magnitude_error",
                "size",
            ),
            median_relative_magnitude_error=(
                "relative_magnitude_error",
                "median",
            ),
            p95_relative_magnitude_error=(
                "relative_magnitude_error",
                lambda x: x.quantile(0.95),
            ),
            median_axial_error_deg=(
                "axial_error_deg",
                "median",
            ),
            p95_axial_error_deg=(
                "axial_error_deg",
                lambda x: x.quantile(0.95),
            ),
        )
        .reset_index()
    )

    # -------------------------------------------------------------------------
    # 8. Save evidence
    # -------------------------------------------------------------------------

    EVIDENCE.mkdir(
        parents=True,
        exist_ok=True,
    )

    analytic_path = (
        EVIDENCE
        / "experiment08_mechanical_analytic.csv"
    )

    raster_path = (
        EVIDENCE
        / "experiment08_mechanical_validation.csv"
    )

    strata_path = (
        EVIDENCE
        / "experiment08_mechanical_r2_strata.csv"
    )

    summary_path = (
        EVIDENCE
        / "experiment08_mechanical_summary.json"
    )

    analytic_df.to_csv(
        analytic_path,
        index=False,
    )

    raster.to_csv(
        raster_path,
        index=False,
    )

    strata.to_csv(
        strata_path,
        index=False,
    )

    summary = {
        "experiment":
            "CLO-SKET Experiment 08",

        "stage":
            "RA14_MECHANICAL_VALIDATION",

        "predictive_results_already_frozen":
            True,

        "predictive_outcomes_used_to_select_mechanical_settings":
            False,

        "population": {
            "n_identities":
                EXPECTED_IDENTITIES,

            "selection":
                "first authoritative row_index per garment_id",

            "n_categories":
                EXPECTED_CATEGORIES,
        },

        "primary_radial_domain": {
            "min":
                float(
                    ra14.PRIMARY_RADIUS_MIN
                ),

            "max":
                float(
                    ra14.PRIMARY_RADIUS_MAX
                ),

            "n_shells":
                int(
                    primary_mask.sum()
                ),
        },

        "angles_deg":
            ANGLES.tolist(),

        "raster_operator": {
            "safe_canvas":
                "ceil(sqrt(h^2+w^2)) square with historical parity adjustment",

            "rotation":
                "PIL.Image.rotate",

            "resample":
                "BILINEAR",

            "expand":
                False,

            "fillcolor":
                255,
        },

        "ra14_matrix_audit":
            matrix_audit,

        "analytic":
            analytic_summary,

        "synthetic_coordinate_sign":
            sign_summary,

        "supported_shell_definition": {
            "minimum_R2":
                MIN_R2,

            "minimum_shell_mass_fraction":
                MIN_SHELL_MASS_FRACTION,
        },

        "raster": {
            "supported_observations":
                int(
                    len(supported)
                ),

            "low_support_observations":
                int(
                    len(low_support)
                ),

            "median_relative_magnitude_error":
                median_mag,

            "p95_relative_magnitude_error":
                p95_mag,

            "median_axial_error_deg":
                median_axial,

            "p95_axial_error_deg":
                p95_axial,

            "magnitude_failure_rate":
                mag_failure_rate,

            "axial_failure_rate":
                axial_failure_rate,

            "combined_failure_rate":
                combined_failure_rate,

            "magnitude_gate_pass":
                magnitude_pass,

            "axial_gate_pass":
                axial_pass,

            "raster_gate_pass":
                raster_pass,
        },

        "ra14_mechanical_pass":
            bool(
                analytic_summary["passed"]
                and
                matrix_audit[
                    "range_checks_pass"
                ]
                and
                raster_pass
            ),

        "inputs": {
            "ra14_script_sha256":
                sha256_file(
                    RA14_SCRIPT
                ),

            "ra14_features_npy_sha256":
                sha256_file(
                    RA14_FEATURES
                ),

            "ra14_source_manifest_sha256":
                sha256_file(
                    RA14_ROW_MANIFEST
                ),

            "ra14_lock_sha256":
                sha256_file(
                    RA14_LOCK
                ),

            "corrected_fold_array_sha256":
                corrected_audit[
                    "experiment08_fold_array_sha256"
                ],
        },
    }

    summary_path.write_text(
        json.dumps(
            summary,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print("\n" + "=" * 88)
    print("RA14 MECHANICAL VALIDATION COMPLETE")
    print("=" * 88)
    print(
        "Analytic PASS :",
        analytic_summary["passed"],
    )
    print(
        "Raster PASS   :",
        raster_pass,
    )
    print(
        "RA14 PASS     :",
        summary[
            "ra14_mechanical_pass"
        ],
    )

    print("\nSaved:")
    print(" ", analytic_path)
    print(" ", raster_path)
    print(" ", strata_path)
    print(" ", summary_path)

    print("\nIMPORTANT")
    print("-" * 88)
    print("No classifier was refitted.")
    print("No RA14 feature was changed.")
    print("No predictive result was optimized.")


if __name__ == "__main__":
    main()
