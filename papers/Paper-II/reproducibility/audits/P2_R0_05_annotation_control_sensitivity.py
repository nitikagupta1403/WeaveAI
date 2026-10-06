from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image

from scipy.fft import dct, idct
import pywt


# =============================================================================
# P2-R0-05 — Annotation-Control Sensitivity
# Stage A: input / provenance validation only
# =============================================================================

VALIDATION_ONLY = True

EXPECTED_ROWS = 2300
EXPECTED_IDENTITIES = 230
EXPECTED_CATEGORIES = 23


# -----------------------------------------------------------------------------
# Repository paths
# -----------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[4]

RAW_ROOT = Path(
    "/ABSOLUTE/PATH/TO/Clo-Sket"
)

CLEAN_ROOT = Path(
    "/ABSOLUTE/PATH/TO/experiment08_materialized"
)

CLEAN_MANIFEST = (
    CLEAN_ROOT
    / "experiment08_materialized_images.csv"
)

PAPER2_RUNTIME = Path(
    "/Users/nitikagupta/Desktop/FM_Papers/Results_PI/Reserve_Codes/"
    "CLO_SKET_runtime_backup_AFTER_CELL25.pkl"
)

FOLD_PACKAGE = Path(
    "/Users/nitikagupta/Desktop/PaperII_notebooks/"
    "CLO_SKET_FINAL_IDENTITY_FIGURES.pkl"
)

# -----------------------------------------------------------------------------
# Frozen Experiment-08 provenance
# -----------------------------------------------------------------------------

EXPECTED_CLEAN_MANIFEST_SHA256 = (
    "071ee7b6c535361951f9eb0044ff166c9a4d42b0ef55a3c0a72aab27af2af6a4"
)

EXPECTED_CLEAN_ORDERED_PIXEL_SHA256 = (
    "30006ee3661f18b4cc3925c753c2ada6e3eb6ea7bf7f56326e5edf7cb7be5703"
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


# =============================================================================
# P2-R0-05A — CLEAN provenance gate
# =============================================================================

def pixel_sha256(path: Path) -> str:
    with Image.open(path) as opened:
        pixels = np.ascontiguousarray(
            np.asarray(opened.convert("L"), dtype=np.uint8)
        )
    return hashlib.sha256(pixels.tobytes()).hexdigest()


def validate_clean_manifest() -> pd.DataFrame:
    if not CLEAN_ROOT.is_dir():
        raise RuntimeError(f"CLEAN_ROOT does not exist: {CLEAN_ROOT}")

    if not CLEAN_MANIFEST.is_file():
        raise RuntimeError(f"CLEAN manifest missing: {CLEAN_MANIFEST}")

    observed_manifest_hash = sha256_file(CLEAN_MANIFEST)

    if observed_manifest_hash != EXPECTED_CLEAN_MANIFEST_SHA256:
        raise RuntimeError(
            "Frozen CLEAN manifest hash mismatch:\n"
            f"observed = {observed_manifest_hash}\n"
            f"expected = {EXPECTED_CLEAN_MANIFEST_SHA256}"
        )

    clean = pd.read_csv(CLEAN_MANIFEST, keep_default_na=False)

    required = {
        "row_index",
        "relative_path",
        "output_relative_path",
        "output_png_sha256",
        "output_pixel_sha256",
    }

    missing = required.difference(clean.columns)
    if missing:
        raise RuntimeError(
            f"CLEAN manifest missing columns: {sorted(missing)}"
        )

    if len(clean) != EXPECTED_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_ROWS} CLEAN rows, found {len(clean)}"
        )

    clean = clean.sort_values("row_index").reset_index(drop=True)

    expected_indices = np.arange(EXPECTED_ROWS)
    observed_indices = clean["row_index"].to_numpy(dtype=int)

    if not np.array_equal(observed_indices, expected_indices):
        raise RuntimeError("CLEAN row_index is not exactly 0..2299")

    if clean["relative_path"].duplicated().any():
        raise RuntimeError("Duplicate relative_path in CLEAN manifest")

    if clean["output_relative_path"].duplicated().any():
        raise RuntimeError("Duplicate output_relative_path in CLEAN manifest")

    aggregate = hashlib.sha256()

    for row in clean.itertuples(index=False):
        clean_path = CLEAN_ROOT / row.output_relative_path

        if not clean_path.is_file():
            raise RuntimeError(
                f"Missing CLEAN image: {clean_path}"
            )

        observed_png_hash = sha256_file(clean_path)

        if observed_png_hash != row.output_png_sha256:
            raise RuntimeError(
                f"CLEAN PNG hash mismatch for row {row.row_index}"
            )

        observed_pixel_hash = pixel_sha256(clean_path)

        if observed_pixel_hash != row.output_pixel_sha256:
            raise RuntimeError(
                f"CLEAN pixel hash mismatch for row {row.row_index}"
            )

        aggregate.update(
            f"{int(row.row_index)}\t{row.output_pixel_sha256}\n".encode()
        )

    observed_ordered_pixel_hash = aggregate.hexdigest()

    if observed_ordered_pixel_hash != EXPECTED_CLEAN_ORDERED_PIXEL_SHA256:
        raise RuntimeError(
            "Ordered CLEAN pixel-array hash mismatch:\n"
            f"observed = {observed_ordered_pixel_hash}\n"
            f"expected = {EXPECTED_CLEAN_ORDERED_PIXEL_SHA256}"
        )

    print("P2-R0-05A CLEAN PROVENANCE: PASS")
    print(f"Rows: {len(clean)}")
    print(f"Manifest SHA-256: {observed_manifest_hash}")
    print(f"Ordered pixel SHA-256: {observed_ordered_pixel_hash}")

    return clean

CLEAN_ROOT = Path(
    "/Users/nitikagupta/Research/experiment08_materialized_v4"
)

CLEAN_MANIFEST = (
    CLEAN_ROOT
    / "experiment08_materialized_images.csv"
)

# =============================================================================
# P2-R0-05B — Bind CLEAN manifest to Paper-II RAW population
# =============================================================================

import pickle


def load_paper2_runtime() -> dict:
    if not PAPER2_RUNTIME.is_file():
        raise RuntimeError(
            f"Paper-II runtime checkpoint missing: {PAPER2_RUNTIME}"
        )

    runtime_sha = sha256_file(PAPER2_RUNTIME)

    print(f"Paper-II runtime SHA-256: {runtime_sha}")

    with PAPER2_RUNTIME.open("rb") as f:
        runtime = pickle.load(f)

    if not isinstance(runtime, dict):
        raise RuntimeError(
            "Paper-II runtime checkpoint is not a dictionary"
        )

    print(f"Paper-II runtime objects: {len(runtime)}")

    return runtime


def inspect_runtime_population(runtime: dict) -> None:
    print("\nCandidate population-like objects:")

    for name, value in runtime.items():
        low = name.lower()

        if any(
            token in low
            for token in [
                "path",
                "file",
                "image",
                "category",
                "label",
                "garment",
                "identity",
                "row",
            ]
        ):
            shape = getattr(value, "shape", None)
            length = None

            try:
                length = len(value)
            except Exception:
                pass

            print(
                f"{name:50s} "
                f"type={type(value).__name__:20s} "
                f"len={length!s:8s} "
                f"shape={shape}"
            )

# =============================================================================
# P2-R0-05B — Exact RAW ↔ CLEAN population/order binding
# =============================================================================

def normalize_runtime_relative_path(value) -> str:
    """
    Convert the historical Paper-II image path to canonical:
        Category/filename.tif
    """
    path = Path(str(value))

    if len(path.parts) < 2:
        raise RuntimeError(f"Cannot normalize runtime path: {value!r}")

    return f"{path.parts[-2]}/{path.parts[-1]}"


def validate_raw_clean_binding(
    runtime: dict,
    clean: pd.DataFrame,
) -> None:

    required_runtime = {
        "image_paths",
        "image_categories",
        "category_labels",
    }

    missing = required_runtime.difference(runtime)
    if missing:
        raise RuntimeError(
            f"Paper-II runtime missing objects: {sorted(missing)}"
        )

    raw_paths = np.asarray(runtime["image_paths"])
    raw_categories = np.asarray(runtime["image_categories"])
    category_labels = np.asarray(runtime["category_labels"])

    if raw_paths.shape != (EXPECTED_ROWS,):
        raise RuntimeError(
            f"Unexpected image_paths shape: {raw_paths.shape}"
        )

    if raw_categories.shape != (EXPECTED_ROWS,):
        raise RuntimeError(
            f"Unexpected image_categories shape: {raw_categories.shape}"
        )

    if category_labels.shape != (EXPECTED_ROWS,):
        raise RuntimeError(
            f"Unexpected category_labels shape: {category_labels.shape}"
        )

    # -------------------------------------------------------------------------
    # Canonicalize Paper-II RAW paths
    # -------------------------------------------------------------------------

    raw_relative_paths = np.asarray(
        [normalize_runtime_relative_path(x) for x in raw_paths],
        dtype=object,
    )

    clean_relative_paths = clean["relative_path"].astype(str).to_numpy()

    # -------------------------------------------------------------------------
    # Exact row-order/path identity
    # -------------------------------------------------------------------------

    if not np.array_equal(
        raw_relative_paths,
        clean_relative_paths,
    ):
        mismatches = np.flatnonzero(
            raw_relative_paths != clean_relative_paths
        )

        first = int(mismatches[0])

        raise RuntimeError(
            "RAW/CLEAN row-order mismatch.\n"
            f"First mismatch row = {first}\n"
            f"RAW   = {raw_relative_paths[first]}\n"
            f"CLEAN = {clean_relative_paths[first]}"
        )

    # -------------------------------------------------------------------------
    # Category consistency derived independently from CLEAN relative path
    # -------------------------------------------------------------------------

    clean_categories = np.asarray(
        [Path(x).parts[0] for x in clean_relative_paths],
        dtype=object,
    )

    raw_categories_str = raw_categories.astype(str)
    category_labels_str = category_labels.astype(str)

    if not np.array_equal(
        raw_categories_str,
        clean_categories,
    ):
        mismatches = np.flatnonzero(
            raw_categories_str != clean_categories
        )

        first = int(mismatches[0])

        raise RuntimeError(
            "Paper-II image_categories mismatch CLEAN path category.\n"
            f"First mismatch row = {first}\n"
            f"runtime = {raw_categories_str[first]}\n"
            f"CLEAN   = {clean_categories[first]}"
        )

    # category_labels may or may not be a duplicate representation.
    # Test it explicitly rather than assuming.
    category_labels_match = np.array_equal(
        category_labels_str,
        clean_categories,
    )

    print("\nP2-R0-05B RAW/CLEAN POPULATION BINDING: PASS")
    print(f"Rows bound exactly: {EXPECTED_ROWS}")
    print(
        "RAW image_paths == CLEAN relative_path order: "
        "YES"
    )
    print(
        "RAW image_categories == CLEAN path categories: "
        "YES"
    )
    print(
        "category_labels == CLEAN path categories: "
        f"{category_labels_match}"
    )

    print("\nFirst 3 bound records:")
    for i in range(3):
        print(
            f"{i:4d} | "
            f"{raw_relative_paths[i]} | "
            f"{clean_categories[i]}"
        )
import importlib.util


# =============================================================================
# P2-R0-05C1 — geometry implementation equivalence gate
# =============================================================================

RA14_SOURCE = (
    REPO_ROOT
    / "papers/CLO-SKET/Codes_paper_I/Experiment_08/"
    / "extract_ra14_features.py"
)

# Local RAW Clo-Sket root.
# Expected examples:
# A-Line/1-1.tif, A-Line/1-10.tif, ...
RAW_ROOT = Path(
    "/Users/nitikagupta/Desktop/Clo-Sket"
)


def load_python_module(name: str, path: Path):
    if not path.is_file():
        raise RuntimeError(f"Module source missing: {path}")

    spec = importlib.util.spec_from_file_location(name, path)

    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import module: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def build_raw_rows_from_runtime(runtime: dict):
    if not RAW_ROOT.is_dir():
        raise RuntimeError(f"RAW_ROOT does not exist: {RAW_ROOT}")

    raw_rows = []

    for path_value, category in zip(
        runtime["image_paths"],
        runtime["image_categories"],
    ):
        relative = normalize_runtime_relative_path(path_value)

        local_path = RAW_ROOT / relative

        if not local_path.is_file():
            raise RuntimeError(
                f"Missing RAW TIFF: {local_path}"
            )

        raw_rows.append(
            {
                "relative_path": relative,
                "category": str(category),
                "path": local_path,
            }
        )

    if len(raw_rows) != EXPECTED_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_ROWS} RAW rows, "
            f"found {len(raw_rows)}"
        )

    return raw_rows


def validate_geometry_equivalence(runtime: dict):
    if "conditional_angular" not in runtime:
        raise RuntimeError(
            "Frozen Paper-II runtime lacks conditional_angular"
        )

    frozen = np.asarray(runtime["conditional_angular"])

    if frozen.shape != (EXPECTED_ROWS, 72, 72):
        raise RuntimeError(
            f"Unexpected frozen conditional_angular shape: "
            f"{frozen.shape}"
        )

    ra14_module = load_python_module(
        "p2_r0_05_frozen_geometry",
        RA14_SOURCE,
    )

    raw_rows = build_raw_rows_from_runtime(runtime)

    print(
        "\nP2-R0-05C1 — reconstructing RAW geometry "
        "for implementation-equivalence check..."
    )

    (
        reconstructed,
        nonempty,
        radial_centers,
        max_mass_error,
        normalization_error,
    ) = ra14_module.recover_geometry(raw_rows)

    reconstructed = np.asarray(
        reconstructed,
        dtype=np.float64,
    )

    if reconstructed.shape != frozen.shape:
        raise RuntimeError(
            "Reconstructed RAW geometry shape mismatch: "
            f"{reconstructed.shape} != {frozen.shape}"
        )

    max_abs_difference = float(
        np.max(
            np.abs(
                reconstructed.astype(np.float64)
                - frozen.astype(np.float64)
            )
        )
    )

    allclose = np.allclose(
        reconstructed,
        frozen,
        rtol=0.0,
        atol=1e-12,
    )

    print("\nP2-R0-05C1 GEOMETRY EQUIVALENCE")
    print(f"Shape: {reconstructed.shape}")
    print(f"Max RAW mass error: {max_mass_error}")
    print(
        "Max RAW conditional normalization error: "
        f"{normalization_error}"
    )
    print(
        "Max difference vs frozen Paper-II field: "
        f"{max_abs_difference:.17g}"
    )
    print(f"Exact/tolerance agreement: {allclose}")

    if not allclose:
        raise RuntimeError(
            "Geometry implementation does NOT reproduce "
            "the frozen Paper-II conditional field."
        )

    print(
        "P2-R0-05C1 PAPER-II GEOMETRY IMPLEMENTATION: PASS"
    )

    return ra14_module, reconstructed

# =============================================================================
# P2-R0-05C2 — CLEAN radial-angular + Fourier reconstruction
# =============================================================================

def build_clean_rows(clean_manifest: pd.DataFrame):
    rows = []

    for row in clean_manifest.itertuples(index=False):
        clean_path = CLEAN_ROOT / str(row.output_relative_path)

        if not clean_path.is_file():
            raise RuntimeError(f"Missing CLEAN image: {clean_path}")

        rows.append(
            {
                "relative_path": str(row.relative_path),
                "category": Path(str(row.relative_path)).parts[0],
                "path": clean_path,
            }
        )

    if len(rows) != EXPECTED_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_ROWS} CLEAN rows, found {len(rows)}"
        )

    return rows


def validate_clean_fourier(
    clean_manifest: pd.DataFrame,
    ra14_module,
):
    clean_rows = build_clean_rows(clean_manifest)

    print(
        "\nP2-R0-05C2 — reconstructing CLEAN geometry..."
    )

    (
        clean_conditional,
        clean_nonempty,
        clean_radial_centers,
        clean_mass_error,
        clean_norm_error,
    ) = ra14_module.recover_geometry(clean_rows)

    clean_conditional = np.asarray(
        clean_conditional,
        dtype=np.float64,
    )

    if clean_conditional.shape != (EXPECTED_ROWS, 72, 72):
        raise RuntimeError(
            f"Unexpected CLEAN conditional shape: "
            f"{clean_conditional.shape}"
        )

    if not np.isfinite(clean_conditional).all():
        raise RuntimeError(
            "CLEAN conditional field contains non-finite values"
        )

    clean_fft = np.fft.rfft(
        clean_conditional,
        axis=2,
    )

    if clean_fft.shape != (EXPECTED_ROWS, 72, 37):
        raise RuntimeError(
            f"Unexpected CLEAN rFFT shape: {clean_fft.shape}"
        )

    if not (
        np.isfinite(clean_fft.real).all()
        and np.isfinite(clean_fft.imag).all()
    ):
        raise RuntimeError(
            "CLEAN Fourier field contains non-finite values"
        )

    nyquist_max_imag = float(
        np.max(np.abs(clean_fft[:, :, 36].imag))
    )

    nonempty_sums = clean_conditional.sum(axis=2)[
        clean_nonempty
    ]

    min_nonempty_sum = float(np.min(nonempty_sums))
    max_nonempty_sum = float(np.max(nonempty_sums))

    print("\nP2-R0-05C2 CLEAN FOURIER VALIDATION")
    print(f"Conditional shape: {clean_conditional.shape}")
    print(f"rFFT shape: {clean_fft.shape}")
    print(f"Max mass error: {clean_mass_error}")
    print(
        "Max conditional normalization error: "
        f"{clean_norm_error}"
    )
    print(
        "Non-empty shells: "
        f"{int(np.sum(clean_nonempty))} / {clean_nonempty.size}"
    )
    print(
        "Conditional sum range on non-empty shells: "
        f"[{min_nonempty_sum}, {max_nonempty_sum}]"
    )
    print(
        "Max |Im(k=36 Nyquist)|: "
        f"{nyquist_max_imag:.17g}"
    )
    print(
        "Finite conditional field: "
        f"{np.isfinite(clean_conditional).all()}"
    )
    print(
        "Finite Fourier field: "
        f"{np.isfinite(clean_fft.real).all() and np.isfinite(clean_fft.imag).all()}"
    )

    if nyquist_max_imag > 1e-12:
        raise RuntimeError(
            "CLEAN Nyquist imaginary component is unexpectedly non-zero"
        )

    print(
        "P2-R0-05C2 CLEAN RADIAL-FOURIER FIELD: PASS"
    )

    return clean_conditional, clean_fft

# =============================================================================
# P2-R0-05D1 — frozen Paper-II identity-fold package
# =============================================================================

def load_and_validate_fold_package(runtime: dict):
    if not FOLD_PACKAGE.is_file():
        raise RuntimeError(
            f"Frozen fold package missing: {FOLD_PACKAGE}"
        )

    fold_sha = sha256_file(FOLD_PACKAGE)

    print("\nP2-R0-05D1 — FROZEN FOLD PACKAGE")
    print(f"Path: {FOLD_PACKAGE}")
    print(f"SHA-256: {fold_sha}")

    with FOLD_PACKAGE.open("rb") as f:
        pkg = pickle.load(f)

    if not isinstance(pkg, dict):
        raise RuntimeError(
            "Frozen fold package is not a dictionary"
        )

    required = {
        "garment_identity_ids",
        "cell30m_fold_assignment",
    }

    missing = required.difference(pkg)
    if missing:
        raise RuntimeError(
            f"Frozen fold package missing: {sorted(missing)}"
        )

    G = np.asarray(
        pkg["garment_identity_ids"],
        dtype=str,
    )

    folds = np.asarray(
        pkg["cell30m_fold_assignment"],
        dtype=int,
    )

    C = np.asarray(
        runtime["image_categories"],
        dtype=str,
    )

    if G.shape != (EXPECTED_ROWS,):
        raise RuntimeError(
            f"Unexpected garment-ID shape: {G.shape}"
        )

    if folds.shape != (EXPECTED_ROWS,):
        raise RuntimeError(
            f"Unexpected fold shape: {folds.shape}"
        )

    if C.shape != (EXPECTED_ROWS,):
        raise RuntimeError(
            f"Unexpected category shape: {C.shape}"
        )

    unique_g = np.unique(G)
    unique_folds = np.sort(np.unique(folds))
    unique_categories = np.unique(C)

    if len(unique_g) != EXPECTED_IDENTITIES:
        raise RuntimeError(
            f"Expected {EXPECTED_IDENTITIES} garment IDs, "
            f"found {len(unique_g)}"
        )

    if len(unique_categories) != EXPECTED_CATEGORIES:
        raise RuntimeError(
            f"Expected {EXPECTED_CATEGORIES} categories, "
            f"found {len(unique_categories)}"
        )

    if len(unique_folds) != 5:
        raise RuntimeError(
            f"Expected 5 folds, found {unique_folds.tolist()}"
        )

    audit_rows = []

    # Every garment identity must:
    #   1. belong to exactly one category
    #   2. belong to exactly one fold
    for garment in unique_g:
        idx = np.flatnonzero(G == garment)

        cats = np.unique(C[idx])
        garment_folds = np.unique(folds[idx])

        if len(cats) != 1:
            raise RuntimeError(
                f"{garment} spans categories: {cats.tolist()}"
            )

        if len(garment_folds) != 1:
            raise RuntimeError(
                f"{garment} spans folds: "
                f"{garment_folds.tolist()}"
            )

    for fold in unique_folds:
        test_mask = folds == fold
        train_mask = ~test_mask

        train_ids = np.unique(G[train_mask])
        test_ids = np.unique(G[test_mask])

        overlap = np.intersect1d(
            train_ids,
            test_ids,
        )

        test_ids_per_category = []
        train_ids_per_category = []

        for category in unique_categories:
            test_ids_per_category.append(
                len(
                    np.unique(
                        G[
                            test_mask
                            & (C == category)
                        ]
                    )
                )
            )

            train_ids_per_category.append(
                len(
                    np.unique(
                        G[
                            train_mask
                            & (C == category)
                        ]
                    )
                )
            )

        audit_rows.append(
            {
                "fold": int(fold),
                "train_rows": int(train_mask.sum()),
                "test_rows": int(test_mask.sum()),
                "train_ids": len(train_ids),
                "test_ids": len(test_ids),
                "identity_overlap": len(overlap),
                "train_ids_per_category_min":
                    min(train_ids_per_category),
                "train_ids_per_category_max":
                    max(train_ids_per_category),
                "test_ids_per_category_min":
                    min(test_ids_per_category),
                "test_ids_per_category_max":
                    max(test_ids_per_category),
            }
        )

    audit = pd.DataFrame(audit_rows)

    if not np.all(
        audit["identity_overlap"].to_numpy() == 0
    ):
        raise RuntimeError(
            "Frozen folds contain identity leakage"
        )

    if not np.all(
        audit["test_ids"].to_numpy() == 46
    ):
        raise RuntimeError(
            "Expected exactly 46 held-out identities per fold"
        )

    if not np.all(
        audit["train_ids"].to_numpy() == 184
    ):
        raise RuntimeError(
            "Expected exactly 184 training identities per fold"
        )

    if not np.all(
        audit["test_ids_per_category_min"].to_numpy() == 2
    ):
        raise RuntimeError(
            "A fold has fewer than 2 test IDs in a category"
        )

    if not np.all(
        audit["test_ids_per_category_max"].to_numpy() == 2
    ):
        raise RuntimeError(
            "A fold has more than 2 test IDs in a category"
        )

    if not np.all(
        audit["train_ids_per_category_min"].to_numpy() == 8
    ):
        raise RuntimeError(
            "A fold has fewer than 8 train IDs in a category"
        )

    if not np.all(
        audit["train_ids_per_category_max"].to_numpy() == 8
    ):
        raise RuntimeError(
            "A fold has more than 8 train IDs in a category"
        )

    print(audit.to_string(index=False))

    print("\nP2-R0-05D1 FROZEN OUTER FOLDS: PASS")
    print(f"Rows: {len(G)}")
    print(f"Garment identities: {len(unique_g)}")
    print(f"Categories: {len(unique_categories)}")
    print(f"Folds: {unique_folds.tolist()}")
    print("Identity leakage: 0")
    print("Test identities/category/fold: exactly 2")
    print("Train identities/category/fold: exactly 8")

    return G, C, folds, fold_sha

# =============================================================================
# P2-R0-05D0 — inspect frozen selection / fold objects
# =============================================================================

def inspect_selection_objects(runtime: dict) -> None:

    tokens = [
        "fold",
        "garment",
        "identity",
        "candidate",
        "band",
        "dct",
        "wave",
        "raw",
        "retriev",
        "mrr",
        "prototype",
        "select",
    ]

    print("\nP2-R0-05D0 — frozen selection-related runtime objects")

    found = 0

    for name, value in runtime.items():
        low = name.lower()

        if not any(token in low for token in tokens):
            continue

        found += 1

        shape = getattr(value, "shape", None)

        try:
            length = len(value)
        except Exception:
            length = None

        print(
            f"{name:55s} "
            f"type={type(value).__name__:20s} "
            f"len={str(length):8s} "
            f"shape={shape}"
        )

    print(f"\nObjects matched: {found}")

# =============================================================================
# P2-R0-05D2 — exact frozen RAW Cell-13 replay
# =============================================================================

HARMONIC_BANDS = {
    "low_1_4": np.arange(1, 5, dtype=int),
    "mid_5_12": np.arange(5, 13, dtype=int),
    "highmid_13_24": np.arange(13, 25, dtype=int),
    "high_25_36": np.arange(25, 37, dtype=int),
}

RADIAL_BUDGETS = np.asarray(
    [4, 8, 12, 18, 24, 36, 48, 72],
    dtype=int,
)

RETENTION_TARGET = 0.95


def raw_radial_reconstruct_exact(X, budget, radial_centers):
    X = np.asarray(X)

    if X.shape[-1] != 72:
        raise ValueError("Expected final radial dimension = 72.")

    if budget == 72:
        return X.copy()

    knot_idx = np.unique(
        np.round(
            np.linspace(0, 71, budget)
        ).astype(int)
    )

    if len(knot_idx) != budget:
        raise RuntimeError(
            f"Raw sampling produced {len(knot_idx)} knots "
            f"instead of {budget}."
        )

    flat = X.reshape(-1, 72)

    recon = np.empty_like(
        flat,
        dtype=X.dtype,
    )

    for i in range(flat.shape[0]):

        if np.iscomplexobj(flat):

            real_part = np.interp(
                radial_centers,
                radial_centers[knot_idx],
                flat[i, knot_idx].real,
            )

            imag_part = np.interp(
                radial_centers,
                radial_centers[knot_idx],
                flat[i, knot_idx].imag,
            )

            recon[i] = (
                real_part
                + 1j * imag_part
            )

        else:

            recon[i] = np.interp(
                radial_centers,
                radial_centers[knot_idx],
                flat[i, knot_idx],
            )

    return recon.reshape(X.shape)


def dct_radial_reconstruct_exact(X, budget):
    X = np.asarray(X)

    coeff = dct(
        X,
        type=2,
        norm="ortho",
        axis=-1,
    )

    truncated = np.zeros_like(coeff)
    truncated[..., :budget] = coeff[..., :budget]

    return idct(
        truncated,
        type=2,
        norm="ortho",
        axis=-1,
    )


WAVELET_NAME = "db4"
_wavelet = pywt.Wavelet(WAVELET_NAME)

WAVELET_LEVEL = pywt.dwt_max_level(
    data_len=72,
    filter_len=_wavelet.dec_len,
)


def wavelet_flatten_single_exact(x):
    coeffs = pywt.wavedec(
        x,
        wavelet=WAVELET_NAME,
        mode="periodization",
        level=WAVELET_LEVEL,
    )

    flat = np.concatenate(
        [np.asarray(c).ravel() for c in coeffs]
    )

    return flat, [len(c) for c in coeffs]


_test_coeffs, WAVELET_LENGTHS = (
    wavelet_flatten_single_exact(
        np.zeros(72, dtype=np.float64)
    )
)

if len(_test_coeffs) != 72:
    raise RuntimeError(
        "Frozen wavelet coefficient count is not 72"
    )


def wavelet_unflatten_single_exact(flat):
    coeffs = []
    start = 0

    for length in WAVELET_LENGTHS:
        stop = start + length
        coeffs.append(flat[start:stop])
        start = stop

    if start != len(flat):
        raise RuntimeError(
            "Wavelet coefficient unflatten mismatch"
        )

    return coeffs


def wavelet_radial_reconstruct_exact(X, budget):
    X = np.asarray(X)

    flat_X = X.reshape(-1, 72)

    recon = np.empty_like(
        flat_X,
        dtype=X.dtype,
    )

    for i in range(flat_X.shape[0]):

        real_coeff, _ = (
            wavelet_flatten_single_exact(
                flat_X[i].real
            )
        )

        imag_coeff, _ = (
            wavelet_flatten_single_exact(
                flat_X[i].imag
            )
        )

        real_keep = np.zeros_like(real_coeff)
        imag_keep = np.zeros_like(imag_coeff)

        real_keep[:budget] = real_coeff[:budget]
        imag_keep[:budget] = imag_coeff[:budget]

        real_recon = pywt.waverec(
            wavelet_unflatten_single_exact(
                real_keep
            ),
            wavelet=WAVELET_NAME,
            mode="periodization",
        )[:72]

        imag_recon = pywt.waverec(
            wavelet_unflatten_single_exact(
                imag_keep
            ),
            wavelet=WAVELET_NAME,
            mode="periodization",
        )[:72]

        recon[i] = (
            real_recon
            + 1j * imag_recon
        )

    return recon.reshape(X.shape)


def complex_band_to_vector_exact(X_band):
    X_band = np.asarray(
        X_band,
        dtype=np.complex128,
    )

    X = np.concatenate(
        [
            X_band.real,
            X_band.imag,
        ],
        axis=2,
    )

    return X.reshape(
        X.shape[0],
        -1,
    )


def fit_robust_geometry_exact(X, eps=1e-12):
    X = np.asarray(
        X,
        dtype=np.float64,
    )

    median = np.median(
        X,
        axis=0,
    )

    q25 = np.percentile(
        X,
        25,
        axis=0,
    )

    q75 = np.percentile(
        X,
        75,
        axis=0,
    )

    scale = q75 - q25

    small = scale <= eps
    scale[small] = 1.0

    return median, scale, small


def apply_robust_geometry_exact(
    X,
    median,
    scale,
):
    X = np.asarray(
        X,
        dtype=np.float64,
    )

    Xs = (
        X
        - median[None, :]
    ) / scale[None, :]

    if not np.isfinite(Xs).all():
        raise RuntimeError(
            "Shared retrieval geometry produced NaN/Inf."
        )

    return Xs


def prototype_retrieval_subset_exact(
    X,
    G_subset,
    C_subset,
):
    X = np.asarray(
        X,
        dtype=np.float64,
    )

    G_subset = np.asarray(
        G_subset,
        dtype=str,
    )

    C_subset = np.asarray(
        C_subset,
        dtype=str,
    )

    ranks = []

    for category in np.unique(C_subset):

        idx_c = np.flatnonzero(
            C_subset == category
        )

        Xc = X[idx_c]
        Gc = G_subset[idx_c]

        garments, labels = np.unique(
            Gc,
            return_inverse=True,
        )

        n_garments = len(garments)

        if n_garments < 2:
            raise RuntimeError(
                f"Category {category} has <2 identities."
            )

        garment_sum = np.zeros(
            (
                n_garments,
                X.shape[1],
            ),
            dtype=np.float64,
        )

        garment_count = np.zeros(
            n_garments,
            dtype=int,
        )

        for gg in range(n_garments):
            members = labels == gg

            garment_sum[gg] = np.sum(
                Xc[members],
                axis=0,
            )

            garment_count[gg] = int(
                np.sum(members)
            )

        if np.any(garment_count < 2):
            raise RuntimeError(
                "Identity has fewer than 2 sketches."
            )

        ordinary_proto = (
            garment_sum
            / garment_count[:, None]
        )

        diff = (
            Xc[:, None, :]
            - ordinary_proto[None, :, :]
        )

        d2 = np.sum(
            diff**2,
            axis=-1,
        )

        own_sum = garment_sum[labels]
        own_count = garment_count[labels]

        loo_proto = (
            own_sum
            - Xc
        ) / (
            own_count[:, None]
            - 1
        )

        own_d2 = np.sum(
            (Xc - loo_proto) ** 2,
            axis=1,
        )

        d2[
            np.arange(len(idx_c)),
            labels,
        ] = own_d2

        order = np.argsort(
            d2,
            axis=1,
            kind="stable",
        )

        for i in range(len(idx_c)):
            rank = (
                np.flatnonzero(
                    order[i] == labels[i]
                )[0]
                + 1
            )

            ranks.append(int(rank))

    ranks = np.asarray(
        ranks,
        dtype=int,
    )

    return {
        "top1_accuracy":
            float(np.mean(ranks == 1)),

        "mean_reciprocal_rank":
            float(np.mean(1.0 / ranks)),

        "median_rank":
            float(np.median(ranks)),

        "n_queries":
            int(len(ranks)),
    }


def reconstruction_metrics_exact(
    original,
    reconstructed,
):
    original = np.asarray(
        original,
        dtype=np.complex128,
    )

    reconstructed = np.asarray(
        reconstructed,
        dtype=np.complex128,
    )

    error_energy = np.sum(
        np.abs(
            reconstructed
            - original
        ) ** 2
    )

    signal_energy = np.sum(
        np.abs(original) ** 2
    )

    if signal_energy <= 0.0:
        raise RuntimeError(
            "Non-positive signal energy"
        )

    return {
        "global_relative_L2":
            float(
                np.sqrt(
                    error_energy
                    / signal_energy
                )
            ),

        "reconstruction_energy_fraction":
            float(
                1.0
                - error_energy
                / signal_energy
            ),
    }

def identity_distance_effect_subset_exact(
    X,
    G_subset,
    C_subset,
):
    X = np.asarray(
        X,
        dtype=np.float64,
    )

    G_subset = np.asarray(
        G_subset,
        dtype=str,
    )

    C_subset = np.asarray(
        C_subset,
        dtype=str,
    )

    garment_rows = []

    for garment in np.unique(G_subset):

        idx_g = np.flatnonzero(
            G_subset == garment
        )

        categories_g = np.unique(
            C_subset[idx_g]
        )

        if len(categories_g) != 1:
            raise RuntimeError(
                f"{garment} spans multiple categories"
            )

        category = categories_g[0]

        idx_between = np.flatnonzero(
            (C_subset == category)
            &
            (G_subset != garment)
        )

        if len(idx_between) == 0:
            raise RuntimeError(
                f"No category-matched comparison for {garment}"
            )

        Xg = X[idx_g]

        sq_g = np.sum(
            Xg**2,
            axis=1,
        )

        D2_within = (
            sq_g[:, None]
            + sq_g[None, :]
            - 2.0 * (Xg @ Xg.T)
        )

        D2_within = np.maximum(
            D2_within,
            0.0,
        )

        tri = np.triu_indices(
            len(idx_g),
            k=1,
        )

        W_g = float(
            np.median(
                np.sqrt(
                    D2_within[tri]
                )
            )
        )

        Xb = X[idx_between]

        sq_b = np.sum(
            Xb**2,
            axis=1,
        )

        D2_between = (
            sq_g[:, None]
            + sq_b[None, :]
            - 2.0 * (Xg @ Xb.T)
        )

        D2_between = np.maximum(
            D2_between,
            0.0,
        )

        B_g = float(
            np.median(
                np.sqrt(
                    D2_between
                )
            )
        )

        if B_g <= 0.0:
            raise RuntimeError(
                f"Non-positive B_g for {garment}"
            )

        delta_g = B_g - W_g
        relative_g = delta_g / B_g

        garment_rows.append(
            {
                "garment_identity": garment,
                "category": category,
                "within_median": W_g,
                "between_median": B_g,
                "delta": delta_g,
                "relative_separation": relative_g,
            }
        )

    table = pd.DataFrame(
        garment_rows
    )

    if not np.isfinite(
        table[
            [
                "within_median",
                "between_median",
                "delta",
                "relative_separation",
            ]
        ].to_numpy(
            dtype=np.float64
        )
    ).all():
        raise RuntimeError(
            "Identity-effect table contains NaN/Inf"
        )

    return table

def replay_cell13_selection(
    fft_field,
    radial_centers,
    G,
    C,
    folds,
    dataset_label,
):
    F = np.asarray(
    fft_field,
    dtype=np.complex128,
)

    radial_centers = np.asarray(
        radial_centers,
        dtype=np.float64,
    )

    if F.shape != (2300, 72, 37):
        raise RuntimeError(
            f"Unexpected frozen FFT shape: {F.shape}"
        )

    if radial_centers.shape != (72,):
        raise RuntimeError(
            f"Unexpected radial-centers shape: "
            f"{radial_centers.shape}"
        )

    F_nonDC = F[..., 1:37].copy()

    representation_functions = {
        "raw_interpolation":
            lambda X, B:
                raw_radial_reconstruct_exact(
                    X,
                    B,
                    radial_centers,
                ),

        "dct":
            dct_radial_reconstruct_exact,

        "wavelet":
            wavelet_radial_reconstruct_exact,
    }

    selection_rows = []
    garment_effect_tables = {}

    for fold in np.sort(np.unique(folds)):

        test_mask = folds == fold
        train_mask = ~test_mask

        train_idx = np.flatnonzero(
            train_mask
        )

        test_idx = np.flatnonzero(
            test_mask
        )

        G_test = G[test_idx]
        C_test = C[test_idx]

        G_train = G[train_idx]
        C_train = C[train_idx]

        for band_name, k_values in (
            HARMONIC_BANDS.items()
        ):

            k_idx = k_values - 1

            X_band_all = np.transpose(
                F_nonDC[:, :, k_idx],
                (0, 2, 1),
            )

            X_train_full = (
                X_band_all[train_idx]
            )

            X_test_full = (
                X_band_all[test_idx]
            )

            train_full_vector = (
                complex_band_to_vector_exact(
                    X_train_full
                )
            )

            (
                train_median,
                train_scale,
                _,
            ) = fit_robust_geometry_exact(
                train_full_vector
            )

            train_full_scaled = (
                apply_robust_geometry_exact(
                    train_full_vector,
                    train_median,
                    train_scale,
                )
            )

            test_full_vector = (
                complex_band_to_vector_exact(
                    X_test_full
                )
            )

            test_full_scaled = (
                apply_robust_geometry_exact(
                    test_full_vector,
                    train_median,
                    train_scale,
                )
            )

            test_full_identity_table = (
                identity_distance_effect_subset_exact(
                    test_full_scaled,
                    G_test,
                    C_test,
                )
            )

            train_full_retrieval = (
                prototype_retrieval_subset_exact(
                    train_full_scaled,
                    G_train,
                    C_train,
                )
            )

            full_train_mrr = (
                train_full_retrieval[
                    "mean_reciprocal_rank"
                ]
            )

            candidate_rows = []

            for (
                representation_name,
                reconstruction_fn,
            ) in representation_functions.items():

                for budget in RADIAL_BUDGETS:

                    X_train_hat = (
                        reconstruction_fn(
                            X_train_full,
                            int(budget),
                        )
                    )

                    recon = (
                        reconstruction_metrics_exact(
                            X_train_full,
                            X_train_hat,
                        )
                    )

                    train_hat_vector = (
                        complex_band_to_vector_exact(
                            X_train_hat
                        )
                    )

                    train_hat_scaled = (
                        apply_robust_geometry_exact(
                            train_hat_vector,
                            train_median,
                            train_scale,
                        )
                    )

                    train_retrieval = (
                        prototype_retrieval_subset_exact(
                            train_hat_scaled,
                            G_train,
                            C_train,
                        )
                    )

                    train_mrr = (
                        train_retrieval[
                            "mean_reciprocal_rank"
                        ]
                    )

                    candidate_rows.append(
                        {
                            "representation":
                                representation_name,

                            "radial_budget":
                                int(budget),

                            "train_mrr":
                                float(train_mrr),

                            "train_mrr_retention":
                                float(
                                    train_mrr
                                    / full_train_mrr
                                ),

                            "train_reconstruction_energy_fraction":
                                float(
                                    recon[
                                        "reconstruction_energy_fraction"
                                    ]
                                ),
                        }
                    )

            candidate_table = pd.DataFrame(
                candidate_rows
            )

            eligible = candidate_table.loc[
                candidate_table[
                    "train_mrr_retention"
                ]
                >= RETENTION_TARGET
            ].copy()

            if len(eligible) == 0:
                raise RuntimeError(
                    f"No eligible candidate: "
                    f"fold={fold}, band={band_name}"
                )

            minimum_budget = int(
                eligible[
                    "radial_budget"
                ].min()
            )

            finalists = eligible.loc[
                eligible[
                    "radial_budget"
                ]
                == minimum_budget
            ].copy()

            finalists = finalists.sort_values(
                [
                    "train_reconstruction_energy_fraction",
                    "representation",
                ],
                ascending=[
                    False,
                    True,
                ],
            )

            selected = finalists.iloc[0]

            selected_representation = str(
                selected["representation"]
            )

            selected_budget = int(
                selected["radial_budget"]
            )

            selected_fn = (
                representation_functions[
                    selected_representation
                ]
            )

            X_test_selected = selected_fn(
                X_test_full,
                selected_budget,
            )

            test_selected_vector = (
                complex_band_to_vector_exact(
                    X_test_selected
                )
            )

            test_selected_scaled = (
                apply_robust_geometry_exact(
                    test_selected_vector,
                    train_median,
                    train_scale,
                )
            )

            test_selected_identity_table = (
                identity_distance_effect_subset_exact(
                    test_selected_scaled,
                    G_test,
                    C_test,
                )
            )

            garment_effect_tables[
                (
                    int(fold),
                    band_name,
                    "full",
                )
            ] = test_full_identity_table.copy()

            garment_effect_tables[
                (
                    int(fold),
                    band_name,
                    "selected",
                )
            ] = test_selected_identity_table.copy()

            selection_rows.append(
                {
                    "fold":
                        int(fold),

                    "harmonic_band":
                        band_name,

                    "selected_representation":
                        str(
                            selected[
                                "representation"
                            ]
                        ),

                    "selected_radial_budget":
                        int(
                            selected[
                                "radial_budget"
                            ]
                        ),

                    "train_full_mrr":
                        float(
                            full_train_mrr
                        ),

                    "train_selected_mrr":
                        float(
                            selected[
                                "train_mrr"
                            ]
                        ),

                    "train_mrr_retention":
                        float(
                            selected[
                                "train_mrr_retention"
                            ]
                        ),

                    "train_reconstruction_energy_fraction":
                        float(
                            selected[
                                "train_reconstruction_energy_fraction"
                            ]
                        ),
                    "selected_representation":
                        selected_representation,

                    "selected_radial_budget":
                        selected_budget,
                }
            )

    replay = pd.DataFrame(
        selection_rows
    )

    print(
    f"\nP2-R0-05D2/D4 — {dataset_label} CELL-13 SELECTION REPLAY"
)

    print(
        replay.to_string(
            index=False
        )
    )

    print(
        "\nSelection stability:"
    )

    stability = (
        replay
        .groupby(
            [
                "harmonic_band",
                "selected_representation",
                "selected_radial_budget",
            ],
            as_index=False,
        )
        .size()
        .sort_values(
            [
                "harmonic_band",
                "size",
            ],
            ascending=[
                True,
                False,
            ],
        )
    )

    print(
        stability.to_string(
            index=False
        )
    )

    return replay, garment_effect_tables

# =============================================================================
# P2-R0-05D3 — exact RAW Cell-13B inferential replay
# =============================================================================

def run_cell13b_inference_exact(
    outer_selection,
    garment_effect_tables,
    dataset_label,
):
    band_order = list(
        HARMONIC_BANDS.keys()
    )

    folds = np.sort(
        outer_selection[
            "fold"
        ].unique()
    )

    paired_rows = []

    # -------------------------------------------------------------------------
    # Reconstruct complete OOF garment-level paired dataset
    # -------------------------------------------------------------------------

    for fold in folds:

        for band_name in band_order:

            key_full = (
                int(fold),
                band_name,
                "full",
            )

            key_selected = (
                int(fold),
                band_name,
                "selected",
            )

            full_table = (
                garment_effect_tables[
                    key_full
                ]
                .copy()
                .sort_values(
                    "garment_identity"
                )
                .reset_index(
                    drop=True
                )
            )

            selected_table = (
                garment_effect_tables[
                    key_selected
                ]
                .copy()
                .sort_values(
                    "garment_identity"
                )
                .reset_index(
                    drop=True
                )
            )

            if not np.array_equal(
                full_table[
                    "garment_identity"
                ].to_numpy(
                    dtype=str
                ),
                selected_table[
                    "garment_identity"
                ].to_numpy(
                    dtype=str
                ),
            ):
                raise RuntimeError(
                    "Garment pairing mismatch: "
                    f"fold={fold}, band={band_name}"
                )

            if not np.array_equal(
                full_table[
                    "category"
                ].to_numpy(
                    dtype=str
                ),
                selected_table[
                    "category"
                ].to_numpy(
                    dtype=str
                ),
            ):
                raise RuntimeError(
                    "Category pairing mismatch: "
                    f"fold={fold}, band={band_name}"
                )

            selection_row = (
                outer_selection
                .loc[
                    (
                        outer_selection["fold"]
                        == fold
                    )
                    &
                    (
                        outer_selection[
                            "harmonic_band"
                        ]
                        == band_name
                    )
                ]
            )

            if len(selection_row) != 1:
                raise RuntimeError(
                    "Expected one selection row for "
                    f"fold={fold}, band={band_name}"
                )

            selection_row = (
                selection_row.iloc[0]
            )

            for i in range(
                len(full_table)
            ):

                full_relative = float(
                    full_table.iloc[i][
                        "relative_separation"
                    ]
                )

                selected_relative = float(
                    selected_table.iloc[i][
                        "relative_separation"
                    ]
                )

                full_delta = float(
                    full_table.iloc[i][
                        "delta"
                    ]
                )

                selected_delta = float(
                    selected_table.iloc[i][
                        "delta"
                    ]
                )

                paired_rows.append(
                    {
                        "fold":
                            int(fold),

                        "harmonic_band":
                            band_name,

                        "garment_identity":
                            str(
                                full_table.iloc[i][
                                    "garment_identity"
                                ]
                            ),

                        "category":
                            str(
                                full_table.iloc[i][
                                    "category"
                                ]
                            ),

                        "selected_representation":
                            str(
                                selection_row[
                                    "selected_representation"
                                ]
                            ),

                        "selected_radial_budget":
                            int(
                                selection_row[
                                    "selected_radial_budget"
                                ]
                            ),

                        "full_relative_separation":
                            full_relative,

                        "selected_relative_separation":
                            selected_relative,

                        "paired_relative_difference":
                            (
                                selected_relative
                                - full_relative
                            ),

                        "full_delta":
                            full_delta,

                        "selected_delta":
                            selected_delta,

                        "paired_delta_difference":
                            (
                                selected_delta
                                - full_delta
                            ),
                    }
                )

    paired = pd.DataFrame(
        paired_rows
    )

    if len(paired) != 230 * 4:
        raise RuntimeError(
            f"Expected 920 paired rows, "
            f"found {len(paired)}"
        )

    counts = (
        paired
        .groupby(
            [
                "garment_identity",
                "harmonic_band",
            ]
        )
        .size()
    )

    if not np.all(
        counts.to_numpy() == 1
    ):
        raise RuntimeError(
            "Identity missing or duplicated "
            "in OOF paired table"
        )

    # -------------------------------------------------------------------------
    # Category × band paired effects
    # -------------------------------------------------------------------------

    category_paired = (
        paired
        .groupby(
            [
                "category",
                "harmonic_band",
            ],
            as_index=False,
        )
        .agg(
            n_garments=(
                "garment_identity",
                "nunique",
            ),

            category_median_difference=(
                "paired_relative_difference",
                "median",
            ),

            category_mean_difference=(
                "paired_relative_difference",
                "mean",
            ),
        )
    )

    categories = np.sort(
        category_paired[
            "category"
        ].unique()
    )

    if len(categories) != 23:
        raise RuntimeError(
            f"Expected 23 categories, "
            f"found {len(categories)}"
        )

    category_effect_matrix = (
        category_paired
        .pivot(
            index="category",
            columns="harmonic_band",
            values="category_median_difference",
        )
        .loc[
            categories,
            band_order,
        ]
        .to_numpy(
            dtype=np.float64
        )
    )

    if category_effect_matrix.shape != (
        23,
        4,
    ):
        raise RuntimeError(
            "Unexpected category-effect matrix shape"
        )

    observed_T = np.median(
        category_effect_matrix,
        axis=0,
    )

    mean_category_effect = np.mean(
        category_effect_matrix,
        axis=0,
    )

    fraction_categories_positive = (
        np.mean(
            category_effect_matrix > 0.0,
            axis=0,
        )
    )

    # -------------------------------------------------------------------------
    # Identity-level descriptive summaries
    # -------------------------------------------------------------------------

    identity_level_median = np.asarray(
        [
            np.median(
                paired.loc[
                    paired[
                        "harmonic_band"
                    ]
                    == band,
                    "paired_relative_difference",
                ].to_numpy(
                    dtype=np.float64
                )
            )
            for band in band_order
        ],
        dtype=np.float64,
    )

    fraction_identities_positive = np.asarray(
        [
            np.mean(
                paired.loc[
                    paired[
                        "harmonic_band"
                    ]
                    == band,
                    "paired_relative_difference",
                ].to_numpy(
                    dtype=np.float64
                )
                > 0.0
            )
            for band in band_order
        ],
        dtype=np.float64,
    )

    # -------------------------------------------------------------------------
    # Build category -> 10 identities × 4 bands
    # -------------------------------------------------------------------------

    garment_difference_by_category = {}

    for category in categories:

        category_rows = (
            paired
            .loc[
                paired[
                    "category"
                ]
                == category
            ]
            .copy()
        )

        garment_names = np.sort(
            category_rows[
                "garment_identity"
            ].unique()
        )

        if len(garment_names) != 10:
            raise RuntimeError(
                f"{category}: expected 10 identities, "
                f"found {len(garment_names)}"
            )

        matrix = np.empty(
            (
                10,
                4,
            ),
            dtype=np.float64,
        )

        for g_idx, garment in enumerate(
            garment_names
        ):

            garment_rows = (
                category_rows
                .loc[
                    category_rows[
                        "garment_identity"
                    ]
                    == garment
                ]
                .set_index(
                    "harmonic_band"
                )
                .loc[
                    band_order
                ]
            )

            matrix[g_idx] = (
                garment_rows[
                    "paired_relative_difference"
                ]
                .to_numpy(
                    dtype=np.float64
                )
            )

        garment_difference_by_category[
            category
        ] = matrix

    # -------------------------------------------------------------------------
    # 5000 stratified garment-identity bootstraps
    # -------------------------------------------------------------------------

    N_BOOTSTRAP = 5000

    rng_boot = np.random.default_rng(
        20260913
    )

    bootstrap_T = np.empty(
        (
            N_BOOTSTRAP,
            4,
        ),
        dtype=np.float64,
    )

    for b in range(
        N_BOOTSTRAP
    ):

        category_boot_effects = np.empty(
            (
                23,
                4,
            ),
            dtype=np.float64,
        )

        for c_idx, category in enumerate(
            categories
        ):

            matrix = (
                garment_difference_by_category[
                    category
                ]
            )

            sampled_idx = (
                rng_boot.integers(
                    0,
                    10,
                    size=10,
                )
            )

            category_boot_effects[
                c_idx
            ] = np.median(
                matrix[
                    sampled_idx
                ],
                axis=0,
            )

        bootstrap_T[b] = np.median(
            category_boot_effects,
            axis=0,
        )

    ci_low = np.percentile(
        bootstrap_T,
        2.5,
        axis=0,
    )

    ci_high = np.percentile(
        bootstrap_T,
        97.5,
        axis=0,
    )

    # -------------------------------------------------------------------------
    # 10000 category-cluster paired sign flips
    # -------------------------------------------------------------------------

    N_PERMUTATION = 10000

    rng_perm = np.random.default_rng(
        20260914
    )

    permutation_T = np.empty(
        (
            N_PERMUTATION,
            4,
        ),
        dtype=np.float64,
    )

    for b in range(
        N_PERMUTATION
    ):

        category_signs = rng_perm.choice(
            np.asarray(
                [
                    -1.0,
                    +1.0,
                ],
                dtype=np.float64,
            ),
            size=23,
            replace=True,
        )

        null_matrix = (
            category_effect_matrix
            *
            category_signs[
                :,
                None,
            ]
        )

        permutation_T[b] = np.median(
            null_matrix,
            axis=0,
        )

    # -------------------------------------------------------------------------
    # Raw one-sided p-values
    # -------------------------------------------------------------------------

    p_raw = np.empty(
        4,
        dtype=np.float64,
    )

    for j in range(4):

        p_raw[j] = (
            1
            +
            np.sum(
                permutation_T[:, j]
                >= observed_T[j]
            )
        ) / (
            N_PERMUTATION
            + 1
        )

    # -------------------------------------------------------------------------
    # Simultaneous max-stat FWER
    # -------------------------------------------------------------------------

    max_null = np.max(
        permutation_T,
        axis=1,
    )

    p_maxstat = np.empty(
        4,
        dtype=np.float64,
    )

    for j in range(4):

        p_maxstat[j] = (
            1
            +
            np.sum(
                max_null
                >= observed_T[j]
            )
        ) / (
            N_PERMUTATION
            + 1
        )

    # -------------------------------------------------------------------------
    # Frozen selection provenance
    # -------------------------------------------------------------------------

    selection_mode = (
        outer_selection
        .groupby(
            "harmonic_band"
        )
        .agg(
            selected_representation=(
                "selected_representation",
                lambda x:
                    x.value_counts().index[0],
            ),

            selected_radial_budget=(
                "selected_radial_budget",
                lambda x:
                    int(
                        x.value_counts().index[0]
                    ),
            ),

            selection_stability_folds=(
                "fold",
                "size",
            ),
        )
        .reset_index()
    )

    result = pd.DataFrame(
        {
            "harmonic_band":
                band_order,

            "observed_category_balanced_effect":
                observed_T,

            "bootstrap_ci_low":
                ci_low,

            "bootstrap_ci_high":
                ci_high,

            "mean_category_effect":
                mean_category_effect,

            "identity_level_median_difference":
                identity_level_median,

            "fraction_categories_positive":
                fraction_categories_positive,

            "fraction_identities_positive":
                fraction_identities_positive,

            "p_raw_one_sided":
                p_raw,

            "p_maxstat_FWER":
                p_maxstat,

            "FWER_supported_0.05":
                p_maxstat < 0.05,
        }
    )

    result = result.merge(
        selection_mode,
        on="harmonic_band",
        how="left",
        validate="one_to_one",
    )

    result = result[
        [
            "harmonic_band",
            "selected_representation",
            "selected_radial_budget",
            "selection_stability_folds",
            "observed_category_balanced_effect",
            "bootstrap_ci_low",
            "bootstrap_ci_high",
            "mean_category_effect",
            "identity_level_median_difference",
            "fraction_categories_positive",
            "fraction_identities_positive",
            "p_raw_one_sided",
            "p_maxstat_FWER",
            "FWER_supported_0.05",
        ]
    ]

    print(
    f"\nP2-R0-05D3/D4 — {dataset_label} CELL-13B INFERENTIAL REPLAY"
)

    print(
        result.to_string(
            index=False
        )
    )

    return (
        result,
        paired,
        category_effect_matrix,
    )

# =============================================================================
# P2-R0-05D4 — CLEAN Cell-13 + Cell-13B replay
# =============================================================================


if __name__ == "__main__":
    clean_manifest = validate_clean_manifest()

    runtime = load_paper2_runtime()

    inspect_runtime_population(runtime)

    validate_raw_clean_binding(
        runtime,
        clean_manifest,
    )               

    ra14_module, raw_conditional = (
    validate_geometry_equivalence(runtime)
)

raw_fft = np.fft.rfft(
    raw_conditional,
    axis=2,
)

if raw_fft.shape != (EXPECTED_ROWS, 72, 37):
    raise RuntimeError(
        f"Unexpected RAW rFFT shape: {raw_fft.shape}"
    )

if not (
    np.isfinite(raw_fft.real).all()
    and np.isfinite(raw_fft.imag).all()
):
    raise RuntimeError(
        "RAW Fourier field contains NaN/Inf"
    )

print(
    "\nP2-R0-05C1b VERIFIED RAW FOURIER FIELD: PASS"
)
print("RAW rFFT shape:", raw_fft.shape)
print(
    "Max |Im(k=36 Nyquist)|:",
    float(
        np.max(
            np.abs(
                raw_fft[:, :, 36].imag
            )
        )
    ),
)

clean_conditional, clean_fft = validate_clean_fourier(
    clean_manifest,
    ra14_module,
    )

G_p2, C_p2, folds_p2, fold_package_sha = (
    load_and_validate_fold_package(runtime)
    )

# ============================================================================
# D2 — RAW Cell-13 replay
# ============================================================================

(
    raw_selection_replay,
    raw_garment_effect_tables,
) = replay_cell13_selection(
    raw_fft,
    runtime["radial_centers"],
    G_p2,
    C_p2,
    folds_p2,
    "RAW",
)


# ============================================================================
# D3 — RAW Cell-13B replay
# ============================================================================

(
    raw_inference_replay,
    raw_paired_effects,
    raw_category_effect_matrix,
) = run_cell13b_inference_exact(
    raw_selection_replay,
    raw_garment_effect_tables,
    "RAW",
)


# ============================================================================
# D3 — HARD RAW EQUIVALENCE GATE
# ============================================================================

EXPECTED_RAW_D3 = {
    "low_1_4": {
        "effect": 0.059306,
        "ci_low": 0.023295,
        "ci_high": 0.108196,
        "p": 0.000200,
        "supported": True,
    },

    "mid_5_12": {
        "effect": 0.005984,
        "ci_low": -0.014164,
        "ci_high": 0.060361,
        "p": 0.608939,
        "supported": False,
    },

    "highmid_13_24": {
        "effect": 0.010959,
        "ci_low": -0.003088,
        "ci_high": 0.073320,
        "p": 0.487751,
        "supported": False,
    },

    "high_25_36": {
        "effect": 0.039300,
        "ci_low": 0.019130,
        "ci_high": 0.091021,
        "p": 0.019698,
        "supported": True,
    },
}


for band, expected in EXPECTED_RAW_D3.items():

    row = (
        raw_inference_replay
        .loc[
            raw_inference_replay[
                "harmonic_band"
            ] == band
        ]
        .iloc[0]
    )

    checks = {
        "effect": (
            float(
                row[
                    "observed_category_balanced_effect"
                ]
            ),
            expected["effect"],
        ),

        "ci_low": (
            float(
                row[
                    "bootstrap_ci_low"
                ]
            ),
            expected["ci_low"],
        ),

        "ci_high": (
            float(
                row[
                    "bootstrap_ci_high"
                ]
            ),
            expected["ci_high"],
        ),

        "p": (
            float(
                row[
                    "p_maxstat_FWER"
                ]
            ),
            expected["p"],
        ),
    }

    for name, (observed, target) in checks.items():

        if not np.isclose(
            observed,
            target,
            atol=5e-7,
            rtol=0.0,
        ):
            raise RuntimeError(
                f"D3 RAW mismatch "
                f"{band}/{name}: "
                f"observed={observed:.9f}, "
                f"expected={target:.9f}"
            )

    if bool(
        row[
            "FWER_supported_0.05"
        ]
    ) != expected["supported"]:

        raise RuntimeError(
            f"D3 support mismatch: {band}"
        )


print(
    "\nP2-R0-05D3 RAW CELL-13B "
    "INFERENTIAL EQUIVALENCE: PASS"
)


# ============================================================================
# D4 — CLEAN Cell-13 replay
# ============================================================================

(
    clean_selection_replay,
    clean_garment_effect_tables,
) = replay_cell13_selection(
    clean_fft,
    runtime["radial_centers"],
    G_p2,
    C_p2,
    folds_p2,
    "CLEAN",
)


# ============================================================================
# D4 — CLEAN Cell-13B inference
# ============================================================================

(
    clean_inference_replay,
    clean_paired_effects,
    clean_category_effect_matrix,
) = run_cell13b_inference_exact(
    clean_selection_replay,
    clean_garment_effect_tables,
    "CLEAN",
)


# ============================================================================
# D4 — RAW vs CLEAN comparison
# ============================================================================

comparison = (
    raw_inference_replay[
        [
            "harmonic_band",
            "selected_representation",
            "selected_radial_budget",
            "observed_category_balanced_effect",
            "bootstrap_ci_low",
            "bootstrap_ci_high",
            "p_maxstat_FWER",
            "FWER_supported_0.05",
        ]
    ]
    .rename(
        columns={
            "selected_representation":
                "RAW_selected_representation",

            "selected_radial_budget":
                "RAW_selected_budget",

            "observed_category_balanced_effect":
                "RAW_effect",

            "bootstrap_ci_low":
                "RAW_ci_low",

            "bootstrap_ci_high":
                "RAW_ci_high",

            "p_maxstat_FWER":
                "RAW_pFWER",

            "FWER_supported_0.05":
                "RAW_supported",
        }
    )
    .merge(
        clean_inference_replay[
            [
                "harmonic_band",
                "selected_representation",
                "selected_radial_budget",
                "observed_category_balanced_effect",
                "bootstrap_ci_low",
                "bootstrap_ci_high",
                "p_maxstat_FWER",
                "FWER_supported_0.05",
            ]
        ]
        .rename(
            columns={
                "selected_representation":
                    "CLEAN_selected_representation",

                "selected_radial_budget":
                    "CLEAN_selected_budget",

                "observed_category_balanced_effect":
                    "CLEAN_effect",

                "bootstrap_ci_low":
                    "CLEAN_ci_low",

                "bootstrap_ci_high":
                    "CLEAN_ci_high",

                "p_maxstat_FWER":
                    "CLEAN_pFWER",

                "FWER_supported_0.05":
                    "CLEAN_supported",
            }
        ),
        on="harmonic_band",
        how="inner",
        validate="one_to_one",
    )
)

comparison[
    "selection_same"
] = (
    (
        comparison[
            "RAW_selected_representation"
        ]
        ==
        comparison[
            "CLEAN_selected_representation"
        ]
    )
    &
    (
        comparison[
            "RAW_selected_budget"
        ]
        ==
        comparison[
            "CLEAN_selected_budget"
        ]
    )
)

comparison[
    "support_same"
] = (
    comparison[
        "RAW_supported"
    ]
    ==
    comparison[
        "CLEAN_supported"
    ]
)

comparison[
    "effect_change_CLEAN_minus_RAW"
] = (
    comparison[
        "CLEAN_effect"
    ]
    -
    comparison[
        "RAW_effect"
    ]
)


print(
    "\nP2-R0-05D4 — RAW vs CLEAN BAND COMPARISON"
)

print(
    comparison.to_string(
        index=False
    )
)


print(
    "\nP2-R0-05D4 CLEAN ANNOTATION-CONTROL "
    "SENSITIVITY COMPLETE"
)

# =============================================================================
# P2-R0-05D3 frozen numerical equivalence gate
# =============================================================================

EXPECTED_RAW_D3 = {
    "low_1_4": {
        "effect": 0.059306,
        "ci_low": 0.023295,
        "ci_high": 0.108196,
        "p": 0.000200,
        "supported": True,
    },

    "mid_5_12": {
        "effect": 0.005984,
        "ci_low": -0.014164,
        "ci_high": 0.060361,
        "p": 0.608939,
        "supported": False,
    },

    "highmid_13_24": {
        "effect": 0.010959,
        "ci_low": -0.003088,
        "ci_high": 0.073320,
        "p": 0.487751,
        "supported": False,
    },

    "high_25_36": {
        "effect": 0.039300,
        "ci_low": 0.019130,
        "ci_high": 0.091021,
        "p": 0.019698,
        "supported": True,
    },
}


for band, expected in EXPECTED_RAW_D3.items():

    row = (
        raw_inference_replay
        .loc[
            raw_inference_replay[
                "harmonic_band"
            ]
            == band
        ]
        .iloc[0]
    )

    checks = {
        "effect":
            ( 
                float(
                    row[
                        "observed_category_balanced_effect"
                    ]
                ),
                expected["effect"],
            ),

        "ci_low":
            (
                float(
                    row[
                        "bootstrap_ci_low"
                    ]
                ),
                expected["ci_low"],
            ),

        "ci_high":
            (
                float(
                    row[
                        "bootstrap_ci_high"
                    ]
                ),
                expected["ci_high"],
            ),

        "p":
            (
                float(
                    row[
                        "p_maxstat_FWER"
                    ]
                ),
                expected["p"],
            ),
    }

    for name, (
        observed,
        target,
    ) in checks.items():

        if not np.isclose(
            observed,
            target,
            atol=5e-7,
            rtol=0.0,
        ):
            raise RuntimeError(
                f"D3 RAW mismatch "
                f"{band}/{name}: "
                f"observed={observed:.9f}, "
                f"expected={target:.9f}"
            )

    if bool(
        row[
            "FWER_supported_0.05"
        ]
    ) != expected["supported"]:

        raise RuntimeError(
            f"D3 support mismatch: {band}"
        )


print(
    "\nP2-R0-05D3 RAW CELL-13B "
    "INFERENTIAL EQUIVALENCE: PASS"
)

# =============================================================================
# P2-R0-05D4 — RAW vs CLEAN band-level comparison
# =============================================================================

comparison = (
    raw_inference_replay[
        [
            "harmonic_band",
            "selected_representation",
            "selected_radial_budget",
            "observed_category_balanced_effect",
            "bootstrap_ci_low",
            "bootstrap_ci_high",
            "p_maxstat_FWER",
            "FWER_supported_0.05",
        ]
    ]
    .rename(
        columns={
            "selected_representation":
                "RAW_selected_representation",

            "selected_radial_budget":
                "RAW_selected_budget",

            "observed_category_balanced_effect":
                "RAW_effect",

            "bootstrap_ci_low":
                "RAW_ci_low",

            "bootstrap_ci_high":
                "RAW_ci_high",

            "p_maxstat_FWER":
                "RAW_pFWER",

            "FWER_supported_0.05":
                "RAW_supported",
        }
    )
    .merge(
        clean_inference_replay[
            [
                "harmonic_band",
                "selected_representation",
                "selected_radial_budget",
                "observed_category_balanced_effect",
                "bootstrap_ci_low",
                "bootstrap_ci_high",
                "p_maxstat_FWER",
                "FWER_supported_0.05",
            ]
        ].rename(
            columns={
                "selected_representation":
                    "CLEAN_selected_representation",

                "selected_radial_budget":
                    "CLEAN_selected_budget",

                "observed_category_balanced_effect":
                    "CLEAN_effect",

                "bootstrap_ci_low":
                    "CLEAN_ci_low",

                "bootstrap_ci_high":
                    "CLEAN_ci_high",

                "p_maxstat_FWER":
                    "CLEAN_pFWER",

                "FWER_supported_0.05":
                    "CLEAN_supported",
            }
        ),
        on="harmonic_band",
        how="inner",
        validate="one_to_one",
    )
)

comparison[
    "selection_same"
] = (
    (
        comparison[
            "RAW_selected_representation"
        ]
        ==
        comparison[
            "CLEAN_selected_representation"
        ]
    )
    &
    (
        comparison[
            "RAW_selected_budget"
        ]
        ==
        comparison[
            "CLEAN_selected_budget"
        ]
    )
)

comparison[
    "support_same"
] = (
    comparison["RAW_supported"]
    ==
    comparison["CLEAN_supported"]
)

comparison[
    "effect_change_CLEAN_minus_RAW"
] = (
    comparison["CLEAN_effect"]
    -
    comparison["RAW_effect"]
)

print(
    "\nP2-R0-05D4 — RAW vs CLEAN BAND COMPARISON"
)

print(
    comparison.to_string(
        index=False
    )
) 