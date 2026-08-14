# M03 — Source Standardization & PCA / Intrinsic Morphology Space

## Evidence class
A. Morphology Representation → Intrinsic Geometry

## 1. INPUT

Canonical Clo-Sket morphology:

    X_source ∈ R^(2300 × 135)

The 135 dimensions consist of:

    64 horizontal occupancy features
    64 vertical occupancy features
    7 global descriptors

Global descriptors:

    cx
    cy
    width
    height
    aspect
    symmetry
   foreground_fraction
   

---

## 2. STANDARDIZATION

A StandardScaler is fitted using the Clo-Sket source
morphology matrix only.

The fitted source scaler is frozen as:

    source_scaler

The transformation is:

    X_scaled = source_scaler.transform(X_source)

No target/external dataset is included during fitting.

---

## 3. PCA

PCA is fitted on the standardized Clo-Sket morphology
representation.

The recovered PCA specification uses:

    n_components = 0.95
    svd_solver = "full"
    random_state = 42

The 0.95 variance criterion determines the retained
number of principal components.

Observed source dimensionality:

    135 → 73

Therefore:

    Z_source ∈ R^(2300 × 73)

---

## 4. VARIANCE RETENTION

The retained 73-dimensional representation explains
approximately 95% of the standardized morphology variance.

The corresponding variance-retention dimensions are:

    80%  → 32
    85%  → 41
    90%  → 53
    95%  → 73
    97.5% → 91
    99%  → 108

The 73-D representation is therefore a variance-based
intrinsic analysis space.

---

## 5. TERMINOLOGY

The 73-D representation is referred to as the:

    intrinsic morphology space

However, this terminology does NOT imply an exact
mathematical manifold dimension.

The later intrinsic-dimension analyses are treated
separately.

Therefore:

    PCA dimensionality
        ≠
    exact manifold dimensionality

---

## 6. SOURCE PIPELINE REPRODUCTION

The recovered source PCA transformer reproduces the
stored source morphology representation.

The pipeline consistency test verifies:

    stored 73-D representation
        =
    source_pca.transform(source_scaled)

within numerical tolerance.

This establishes that the source transformation can be
reproduced from the frozen preprocessing objects.

---

## 7. FROZEN TRANSFORMATION

After fitting on Clo-Sket:

    source_scaler
        ↓
    source_pca

are treated as frozen transformations.

Subsequent analyses do not refit these transformations
using target data.

---

## 8. GEOMETRY ANALYSIS SPACE

The 73-D PCA representation is the principal coordinate
space used for the local morphology geometry analyses.

It is used for:

    • local neighborhoods
    • morphology continuity
    • transition analysis
    • graph construction
    • geodesic analysis
    • density-ascent analysis
    • cross-scale morphology organization

The original 135-D representation remains the canonical
feature space for feature-level analyses.

---

## 9. TWO ANALYTICAL SPACES

### Canonical feature space

    X_source
    2300 × 135

Used for:

    feature contribution
    feature perturbation
    feature-block analysis
    regional feature profiles
    permutation tests

### Intrinsic morphology space

    Z_source
    2300 × 73

Used for:

    local geometry
    graph geometry
    geodesics
    density organization
    morphology continuity

This separation is maintained throughout the study.

---

## 10. SPECTRAL CHARACTERIZATION

The PCA spectrum is subsequently characterized using:

    • eigenvalue decay
    • cumulative variance
    • variance-retention dimensions
    • participation-ratio effective dimension
    • spectral resampling

Observed participation-ratio effective dimension:

    ≈ 10.55

This quantity is treated as an effective spectral
complexity measure.

It is not interpreted as an exact intrinsic manifold
dimension.

---

## 11. STANDARDIZATION LOCK

The scaler is fitted only on the canonical Clo-Sket
source morphology.

Therefore:

    source_scaler.fit(X_source)

is part of the source model definition.

No target-specific centering or scaling is introduced
for the geometry-transfer branch.

---

## 12. NO-LEAKAGE LOCK

PCA fitting does NOT use:

    category labels
    replication labels
    target sketches
    morphology-state labels
    KMeans assignments

The PCA representation is derived from quantitative
morphology alone.

---

## 13. KMEANS SEPARATION

A later source-model branch fits KMeans on the 73-D
representation.

That model is separate from the geometry-validation
pipeline.

The geometry evidence does NOT require KMeans.

Therefore:

    morphology geometry
        ↓
    PCA / intrinsic space

is established independently of:

    KMeans morphology-state discovery.

---

## 14. MODEL FREEZE

The source pipeline is frozen as:

    135-D morphology
          ↓
    source StandardScaler
          ↓
    73-D source PCA
          ↓
    optional downstream morphology-state model

For the geometry study:

    downstream state model = NOT REQUIRED

---

## 15. CLAIM BOUNDARY

This procedure establishes:

✓ a reproducible 135-D → 73-D dimensional reduction

✓ a standardized source morphology coordinate system

✓ approximately 95% variance retention

✓ a frozen intrinsic morphology analysis space

It does NOT establish:

✗ exact manifold dimensionality

✗ morphology categories

✗ semantic morphology states

✗ morphology grammar

✗ causal morphology structure

---

## STATUS

M03 = 🟢 CAST-IRON LOCKED

Source:

    Clo-Sket only

Input:

    2300 × 135

Standardization:

    frozen StandardScaler

PCA:

    full SVD
    95% variance criterion
    73 retained components

Geometry space:

    2300 × 73

No target fitting:

    ✓

No semantic labels:

    ✓

No KMeans required for geometry: