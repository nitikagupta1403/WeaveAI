from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image


N_ANGULAR = 72
N_RADIAL = 72

MASS_EPS = 1e-14
MASS_TOL = 1e-10

PRIMARY_RADIUS_MIN = 3.5
PRIMARY_RADIUS_MAX = 27.5

EXPECTED_POPULATION = 2300

F2_PRIMARY = [
    "F2_integral",
    "F2_radial_centroid",
    "F2_radial_spread",
    "F2_radial_concentration",
    "F2_onset_radius",
    "F2_termination_radius",
    "F2_peak_radius",
    "F2_peak_magnitude",
]

RA14_COLUMNS = [
    *F2_PRIMARY,
    "alpha2_peak_cos2",
    "alpha2_peak_sin2",
    "alpha2_weighted_mean_cos2",
    "alpha2_weighted_mean_sin2",
    "alpha2_axial_coherence",
    "alpha2_orientation_drift_deg",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_array(array: np.ndarray) -> str:
    arr = np.ascontiguousarray(array)
    return hashlib.sha256(arr.tobytes()).hexdigest()


def axial_difference_deg(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    d = np.mod(np.abs(a - b), 180.0)
    return np.minimum(d, 180.0 - d)


def axial_mean_deg(angle_deg, weights, axis=1, eps=1e-12):
    angle = np.asarray(angle_deg, dtype=float)
    weights = np.asarray(weights, dtype=float)

    valid = (
        np.isfinite(angle)
        & np.isfinite(weights)
        & (weights > 0)
    )

    z = np.sum(
        np.where(
            valid,
            weights * np.exp(2j * np.deg2rad(angle)),
            0.0,
        ),
        axis=axis,
    )

    w = np.sum(
        np.where(valid, weights, 0.0),
        axis=axis,
    )

    out = (
        0.5 * np.degrees(np.angle(z))
    ) % 180.0

    return np.where(w > eps, out, np.nan)


def discover_images(root: Path):
    rows = []

    for category_dir in sorted(root.iterdir(), key=lambda p: p.name):
        if not category_dir.is_dir():
            continue

        for path in sorted(category_dir.iterdir(), key=lambda p: p.name):
            if path.suffix.lower() not in {".tif", ".tiff"}:
                continue

            relative_path = path.relative_to(root).as_posix()

            rows.append({
                "relative_path": relative_path,
                "category": category_dir.name,
                "path": path,
            })

    if len(rows) != EXPECTED_POPULATION:
        raise RuntimeError(
            f"Expected {EXPECTED_POPULATION} TIFF sketches, "
            f"found {len(rows)}."
        )

    normalized_paths = [row["relative_path"] for row in rows]

    if len(set(normalized_paths)) != len(normalized_paths):
        raise RuntimeError("Duplicate normalized relative paths found.")

    return rows


def recover_geometry(image_rows):
    theta_edges = np.linspace(
        -np.pi,
        np.pi,
        N_ANGULAR + 1,
    )

    r_edges = np.linspace(
        0.0,
        1.0,
        N_RADIAL + 1,
    )

    normalized_radial_centers = (
        r_edges[:-1] + r_edges[1:]
    ) / 2.0

    joint_mass = np.zeros(
        (
            EXPECTED_POPULATION,
            N_RADIAL,
            N_ANGULAR,
        ),
        dtype=np.float64,
    )

    total_mass = np.zeros(
        EXPECTED_POPULATION,
        dtype=np.float64,
    )

    for i, row in enumerate(image_rows):
        path = row["path"]

        with Image.open(path) as im:
            im.load()

            img = np.asarray(
                im.convert("L"),
                dtype=np.float64,
            )

        if img.ndim != 2:
            raise RuntimeError(
                f"Expected grayscale image, got {img.shape}: {path}"
            )

        if not np.isfinite(img).all():
            raise RuntimeError(
                f"Non-finite image values: {path}"
            )

        # Historical continuous darkness:
        # white=255, black=0.
        w = 255.0 - img
        w = np.maximum(w, 0.0)

        mass = float(np.sum(w))

        if (
            not np.isfinite(mass)
            or mass <= 0
        ):
            raise RuntimeError(
                f"Invalid total ink mass: {path}"
            )

        total_mass[i] = mass

        height, width = w.shape

        # Historical isotropic coordinate scale.
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
            np.sum(w * X) / mass
        )

        cy = float(
            np.sum(w * Y) / mass
        )

        Xc = X - cx
        Yc = Y - cy

        R = np.sqrt(
            Xc**2 + Yc**2
        )

        # Historical native image-axis convention.
        Theta = np.arctan2(
            Yc,
            Xc,
        )

        Rmax = float(np.max(R))

        if Rmax <= 0:
            raise RuntimeError(
                f"Invalid radial extent: {path}"
            )

        Rnorm = np.clip(
            R / Rmax,
            0.0,
            1.0,
        )

        r_idx = (
            np.searchsorted(
                r_edges,
                Rnorm,
                side="right",
            )
            - 1
        )

        r_idx = np.clip(
            r_idx,
            0,
            N_RADIAL - 1,
        )

        theta_idx = (
            np.searchsorted(
                theta_edges,
                Theta,
                side="right",
            )
            - 1
        )

        theta_idx = np.clip(
            theta_idx,
            0,
            N_ANGULAR - 1,
        )

        valid = (
            np.isfinite(w)
            & np.isfinite(Rnorm)
            & np.isfinite(Theta)
        )

        np.add.at(
            joint_mass[i],
            (
                r_idx[valid],
                theta_idx[valid],
            ),
            w[valid],
        )

        if (
            (i + 1) % 250 == 0
            or i == EXPECTED_POPULATION - 1
        ):
            print(
                f"RA14 geometry: processed "
                f"{i + 1}/{EXPECTED_POPULATION}"
            )

    recovered_mass = joint_mass.sum(
        axis=(1, 2)
    )

    relative_mass_error = (
        np.abs(
            recovered_mass - total_mass
        )
        / total_mass
    )

    max_mass_error = float(
        np.max(relative_mass_error)
    )

    if max_mass_error > MASS_TOL:
        raise RuntimeError(
            "Radial-angular mass conservation failed: "
            f"{max_mass_error:.3e}"
        )

    shell_mass = joint_mass.sum(axis=2)

    conditional_angular = np.zeros_like(
        joint_mass
    )

    nonempty = shell_mass > MASS_EPS

    for i in range(EXPECTED_POPULATION):
        valid_shells = nonempty[i]

        conditional_angular[
            i,
            valid_shells,
            :
        ] = (
            joint_mass[
                i,
                valid_shells,
                :
            ]
            / shell_mass[
                i,
                valid_shells,
                None,
            ]
        )

    conditional_sum = conditional_angular.sum(
        axis=2
    )

    if np.any(nonempty):
        normalization_error = float(
            np.max(
                np.abs(
                    conditional_sum[nonempty]
                    - 1.0
                )
            )
        )
    else:
        normalization_error = 0.0

    if normalization_error > MASS_TOL:
        raise RuntimeError(
            "Conditional angular normalization failed: "
            f"{normalization_error:.3e}"
        )

    return (
        conditional_angular,
        nonempty,
        normalized_radial_centers,
        max_mass_error,
        normalization_error,
    )


def recover_f2(conditional_angular):
    conditional_fft = np.fft.rfft(
        conditional_angular,
        axis=2,
    )

    f2_complex = conditional_fft[:, :, 2]

    F2_mag = np.abs(
        f2_complex
    )

    alpha2_deg = (
        np.degrees(
            -0.5 * np.angle(
                f2_complex
            )
        )
        % 180.0
    )

    return F2_mag, alpha2_deg


def build_ra14(F2_mag, alpha2_deg):
    # Historical downstream descriptor coordinates:
    # 0.5, 1.5, ..., 71.5
    radial_centers = (
        np.arange(
            N_RADIAL,
            dtype=np.float64,
        )
        + 0.5
    )

    zone_mask = (
        (radial_centers >= PRIMARY_RADIUS_MIN)
        & (radial_centers <= PRIMARY_RADIUS_MAX)
    )

    zone_r = radial_centers[zone_mask]
    zone_f2 = np.asarray(
        F2_mag[:, zone_mask],
        dtype=np.float64,
    )

    zone_alpha = np.asarray(
        alpha2_deg[:, zone_mask],
        dtype=np.float64,
    )

    if len(zone_r) != 25:
        raise RuntimeError(
            f"Expected 25 primary shells, got {len(zone_r)}."
        )

    dr = np.gradient(zone_r)

    n = zone_f2.shape[0]

    F2_integral = np.full(n, np.nan)
    F2_radial_centroid = np.full(n, np.nan)
    F2_radial_spread = np.full(n, np.nan)
    F2_radial_concentration = np.full(n, np.nan)
    F2_onset_radius = np.full(n, np.nan)
    F2_termination_radius = np.full(n, np.nan)
    F2_peak_radius = np.full(n, np.nan)
    F2_peak_magnitude = np.full(n, np.nan)

    for i in range(n):
        m = np.where(
            np.isfinite(zone_f2[i]),
            zone_f2[i],
            0.0,
        )

        if not np.any(m > 0):
            continue

        peak_idx = int(np.argmax(m))
        peak_value = float(m[peak_idx])
        peak_radius = float(zone_r[peak_idx])

        F2_peak_magnitude[i] = peak_value
        F2_peak_radius[i] = peak_radius

        if peak_value <= 0:
            continue

        mass = float(
            np.sum(m * dr)
        )

        if mass <= 0:
            continue

        F2_integral[i] = mass

        centroid = float(
            np.sum(
                zone_r * m * dr
            )
            / mass
        )

        F2_radial_centroid[i] = centroid

        variance = float(
            np.sum(
                ((zone_r - centroid) ** 2)
                * m
                * dr
            )
            / mass
        )

        F2_radial_spread[i] = np.sqrt(
            max(variance, 0.0)
        )

        concentration_mask = (
            np.abs(
                zone_r - peak_radius
            )
            <= 4.0
        )

        local_mass = float(
            np.sum(
                m[concentration_mask]
                * dr[concentration_mask]
            )
        )

        F2_radial_concentration[i] = (
            local_mass / mass
        )

        threshold = 0.10 * peak_value

        above = m >= threshold

        if np.any(above):
            onset_idx = int(
                np.where(above)[0][0]
            )

            termination_idx = int(
                np.where(above)[0][-1]
            )

            F2_onset_radius[i] = float(
                zone_r[onset_idx]
            )

            F2_termination_radius[i] = float(
                zone_r[termination_idx]
            )

    # Axial descriptors.
    alpha_weighted_mean = axial_mean_deg(
        zone_alpha,
        zone_f2,
    )

    alpha_weight_sum = np.sum(
        zone_f2,
        axis=1,
    )

    doubled = np.exp(
        2j * np.deg2rad(
            zone_alpha
        )
    )

    resultant = np.sum(
        zone_f2 * doubled,
        axis=1,
    )

    coherence = np.divide(
        np.abs(resultant),
        alpha_weight_sum,
        out=np.full(n, np.nan),
        where=alpha_weight_sum > 1e-12,
    )

    peak_index = np.argmax(
        zone_f2,
        axis=1,
    )

    alpha_peak = zone_alpha[
        np.arange(n),
        peak_index,
    ]

    orientation_drift = axial_difference_deg(
        zone_alpha[:, 0],
        zone_alpha[:, -1],
    )

    frame = pd.DataFrame({
        "F2_integral":
            F2_integral,

        "F2_radial_centroid":
            F2_radial_centroid,

        "F2_radial_spread":
            F2_radial_spread,

        "F2_radial_concentration":
            F2_radial_concentration,

        "F2_onset_radius":
            F2_onset_radius,

        "F2_termination_radius":
            F2_termination_radius,

        "F2_peak_radius":
            F2_peak_radius,

        "F2_peak_magnitude":
            F2_peak_magnitude,

        "alpha2_peak_cos2":
            np.cos(
                2.0
                * np.deg2rad(
                    alpha_peak
                )
            ),

        "alpha2_peak_sin2":
            np.sin(
                2.0
                * np.deg2rad(
                    alpha_peak
                )
            ),

        "alpha2_weighted_mean_cos2":
            np.cos(
                2.0
                * np.deg2rad(
                    alpha_weighted_mean
                )
            ),

        "alpha2_weighted_mean_sin2":
            np.sin(
                2.0
                * np.deg2rad(
                    alpha_weighted_mean
                )
            ),

        "alpha2_axial_coherence":
            coherence,

        "alpha2_orientation_drift_deg":
            orientation_drift,
    })

    if list(frame.columns) != RA14_COLUMNS:
        raise RuntimeError(
            "RA14 column-order lock violated."
        )

    matrix = frame.to_numpy(
        dtype=np.float64
    )

    if matrix.shape != (
        EXPECTED_POPULATION,
        14,
    ):
        raise RuntimeError(
            f"Unexpected RA14 shape: {matrix.shape}"
        )

    if not np.isfinite(matrix).all():
        bad_columns = [
            col
            for col in frame.columns
            if not np.isfinite(
                frame[col].to_numpy()
            ).all()
        ]

        raise RuntimeError(
            "RA14 contains non-finite values: "
            + ", ".join(bad_columns)
        )

    return frame, matrix


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dataset-root",
        type=Path,
        required=True,
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(
            "papers/CLO-SKET/"
            "Codes_paper_I/"
            "Experiment_08"
        ),
    )

    args = parser.parse_args()

    dataset_root = args.dataset_root.expanduser().resolve()
    output_dir = args.output_dir.resolve()

    if not dataset_root.is_dir():
        raise RuntimeError(
            f"Dataset root does not exist: {dataset_root}"
        )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    image_rows = discover_images(
        dataset_root
    )

    print(
        f"Source population: {len(image_rows)}"
    )

    (
        conditional_angular,
        nonempty,
        normalized_radial_centers,
        max_mass_error,
        normalization_error,
    ) = recover_geometry(
        image_rows
    )

    F2_mag, alpha2_deg = recover_f2(
        conditional_angular
    )

    frame, matrix = build_ra14(
        F2_mag,
        alpha2_deg,
    )

    matrix_path = (
        output_dir
        / "experiment08_ra14_features.npy"
    )

    csv_path = (
        output_dir
        / "experiment08_ra14_features.csv"
    )

    manifest_path = (
        output_dir
        / "experiment08_ra14_manifest.json"
    )

    source_manifest_path = (
        output_dir
        / "experiment08_ra14_source_manifest.csv"
    )

    np.save(
        matrix_path,
        matrix,
        allow_pickle=False,
    )

    frame.to_csv(
        csv_path,
        index=False,
    )

    source_manifest = pd.DataFrame([
        {
            "row_index": i,
            "relative_path": row["relative_path"],
            "category": row["category"],
            "byte_size": row["path"].stat().st_size,
            "sha256": sha256_file(row["path"]),
        }
        for i, row in enumerate(image_rows)
    ])

    source_manifest.to_csv(
        source_manifest_path,
        index=False,
    )

    manifest = {
        "experiment": "Experiment_08",
        "representation": "RA14",
        "population": int(matrix.shape[0]),
        "n_features": int(matrix.shape[1]),
        "dtype": str(matrix.dtype),

        "columns": RA14_COLUMNS,

        "dataset_root_runtime": str(dataset_root),

        "source_rule": (
            "original TIFF -> grayscale L -> "
            "continuous darkness 255-I -> "
            "intensity-weighted centroid -> "
            "72x72 radial-angular mass -> "
            "conditional P(theta|r) -> "
            "rFFT harmonic 2 -> "
            "25-shell primary domain 3.5..27.5"
        ),

        "array_sha256": sha256_array(matrix),

        "saved_npy_sha256":
            sha256_file(matrix_path),

        "source_manifest_sha256":
            sha256_file(source_manifest_path),

        "max_relative_mass_error":
            max_mass_error,

        "max_conditional_normalization_error":
            normalization_error,

        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "category_labels_used_for_feature_extraction": False,
    }

    manifest_path.write_text(
        json.dumps(
            manifest,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print("\n" + "=" * 80)
    print("EXPERIMENT 08 — RA14 EXTRACTION COMPLETE")
    print("=" * 80)
    print(f"Matrix              : {matrix.shape}")
    print(f"Finite              : {np.isfinite(matrix).all()}")
    print(f"Array SHA-256       : {manifest['array_sha256']}")
    print(f"Saved NPY SHA-256   : {manifest['saved_npy_sha256']}")
    print(f"Source manifest     : {source_manifest_path}")
    print(f"Feature matrix      : {matrix_path}")
    print(f"Feature CSV         : {csv_path}")
    print(f"Manifest            : {manifest_path}")
    print("Classifier fitted   : False")
    print("Outcome computed    : False")


if __name__ == "__main__":
    main()