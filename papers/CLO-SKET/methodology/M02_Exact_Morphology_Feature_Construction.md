# M02 — Exact Morphology Feature Construction

## Evidence class

A. Morphology Representation → Feature Definition

---

## STATUS

🟢 CAST-IRON LOCKED

This module defines the canonical quantitative morphology
representation used throughout the CLO-SKET analysis.

The morphology representation is constructed from image
geometry alone.

No semantic labels, category labels, replication labels,
target sketches, or downstream morphology-state assignments
are used in feature construction.

---

# 1. CANONICAL INPUT

Number of Clo-Sket sketches:

    N = 2300

Each sketch is converted into a quantitative morphology
feature vector.

Canonical morphology dimensionality:

    D = 135

Therefore the canonical morphology matrix is:

    X_source ∈ R^(2300 × 135)

Each row corresponds to one sketch.

Each column corresponds to one quantitative morphology
measurement.

---

# 2. IMAGE PREPROCESSING

For each sketch:

    1. Load the image.
    2. Convert to grayscale.
    3. Convert pixel values to float32.
    4. Normalize intensity by 255.

The normalized grayscale image is represented as:

    arr = grayscale_image / 255

---

# 3. FOREGROUND ESTIMATION

Dark sketch pixels are treated as foreground.

The foreground estimate is defined by the fixed threshold:

    foreground = arr < 0.8

Thus the foreground criterion is deterministic and is not
estimated from the dataset.

The threshold is applied identically to all source sketches.

---

# 4. MORPHOLOGY IMAGE REPRESENTATION

The foreground estimate is converted to an image-valued
representation and resized to:

    64 × 64

The resulting array is converted to floating-point form
and scaled to the corresponding normalized intensity range.

The resulting 64 × 64 morphology array is denoted:

    M(x,y)

Important:

The thresholding operation creates the foreground estimate,
but the subsequent resize operation may introduce
intermediate intensity values depending on the image
resampling operation.

Therefore the final morphology array is described as the
resized normalized foreground representation rather than
being assumed to remain strictly binary after resizing.

---

# 5. HORIZONTAL OCCUPANCY

Horizontal occupancy is calculated by averaging the
morphology array across the horizontal image coordinate.

This produces 64 measurements:

    H = [H_0, H_1, ..., H_63]

where each value represents the mean morphology occupancy
associated with one image row.

Feature names:

    horizontal_occupancy_00
    ...
    horizontal_occupancy_63

Number of features:

    64

---

# 6. VERTICAL OCCUPANCY

Vertical occupancy is calculated by averaging the
morphology array across the vertical image coordinate.

This produces 64 measurements:

    V = [V_0, V_1, ..., V_63]

where each value represents the mean morphology occupancy
associated with one image column.

Feature names:

    vertical_occupancy_00
    ...
    vertical_occupancy_63

Number of features:

    64

---

# 7. GLOBAL MORPHOLOGY DESCRIPTORS

Seven global morphology descriptors are appended:

    centroid_x
    centroid_y
    bbox_width
    bbox_height
    aspect_ratio
    symmetry
    foreground_fraction

Number of global descriptors:

    7

These descriptors quantify global geometry only.

No semantic interpretation is assigned to any descriptor.

---

# 8. EXACT 135-D FEATURE VECTOR

For sketch i:

    x_i = [
        H_i,
        V_i,
        G_i
    ]

where:

    |H_i| = 64
    |V_i| = 64
    |G_i| = 7

Therefore:

    64 + 64 + 7 = 135

and:

    x_i ∈ R^135

The complete canonical morphology matrix is:

    X_source ∈ R^(2300 × 135)

---

# 9. CANONICAL FEATURE ORDER

The exact feature ordering is:

    1–64:
        horizontal_occupancy_00
        ...
        horizontal_occupancy_63

    65–128:
        vertical_occupancy_00
        ...
        vertical_occupancy_63

    129–135:
        centroid_x
        centroid_y
        bbox_width
        bbox_height
        aspect_ratio
        symmetry
        foreground_fraction

This ordering is frozen.

Downstream analyses must not silently reorder,
redefine, or replace these features.

---

# 10. GLOBAL DESCRIPTOR DEFINITIONS

## Centroid

The foreground-weighted centroid is calculated from the
64 × 64 morphology array.

The x and y coordinates are normalized by the image size.

Thus:

    centroid_x ∈ normalized x-coordinate space

    centroid_y ∈ normalized y-coordinate space

---

## Bounding-box width

For non-empty foreground:

    bbox_width =
        (x_max - x_min + 1) / 64

---

## Bounding-box height

For non-empty foreground:

    bbox_height =
        (y_max - y_min + 1) / 64

---

## Aspect ratio

    aspect_ratio =
        bbox_width /
        (bbox_height + 1e-8)

---

## Symmetry

Horizontal reflection is used:

    M_flip = fliplr(M)

Symmetry is:

    symmetry =
        1 -
        mean(
            abs(M - M_flip)
        )

Higher values indicate greater left-right
self-similarity under the defined image reflection.

---

## Foreground fraction

    foreground_fraction =
        mean(M)

This is retained as a quantitative global descriptor
within the canonical 135-D representation.

It is not assigned semantic meaning.

---

# 11. REPRESENTATION CHECK

The implementation verifies:

    X_source.shape == (2300, 135)

and requires all morphology values to be finite.

Expected result:

    Shape:
        (2300, 135)

    Finite:
        True

Failure of this condition constitutes a morphology
construction error.

---

# 12. CANONICAL REPRESENTATION LOCK

Once constructed:

    X_source = 2300 × 135

is frozen as the canonical morphology representation.

All downstream morphology analyses inherit this
representation.

Downstream analyses do not redefine morphology features.

The following therefore operate downstream of M02:

    StandardScaler
    PCA
    local-neighborhood analysis
    spectral analysis
    graph analysis
    density analysis
    basin analysis
    feature perturbation
    regional profile analysis

---

# 13. DISCOVERY-ONLY CONSTRUCTION

M02 uses quantitative image morphology only.

It does not use:

    category labels
    replication labels
    target sketches
    target fitting
    GMM
    KMeans
    hierarchical clustering
    supervised prediction
    semantic labels
    CNN
    neural networks

The representation therefore precedes and is independent
of morphology-state discovery and semantic interpretation.

---

# 14. ANALYTICAL ROLE

The 135-D representation serves as the canonical
feature space.

It is retained for:

    • feature contribution analysis
    • feature perturbation
    • feature-block analysis
    • regional feature profiles
    • permutation tests

A separate PCA-derived representation is constructed in
M03 for intrinsic morphology geometry.

Therefore:

    135-D canonical morphology
        ≠
    73-D PCA geometry space

The 135-D representation remains the source feature space
for feature-level analyses.

---

# 15. CLAIM BOUNDARY

M02 establishes:

    ✓ a reproducible quantitative morphology representation

    ✓ 2300 observations × 135 measurements

    ✓ 64 horizontal occupancy measurements

    ✓ 64 vertical occupancy measurements

    ✓ 7 global morphology descriptors

    ✓ fixed feature ordering

    ✓ source-only construction

    ✓ semantic-label-free morphology construction

M02 does NOT establish:

    ✗ morphology categories

    ✗ morphology states

    ✗ semantic morphology primitives

    ✗ morphology grammar

    ✗ exact manifold dimensionality

    ✗ causal morphology structure

    ✗ an optimal representation

---

# 16. M02 → M03 INTERFACE

M02 output:

    X_source
        shape = (2300, 135)

M03 input:

    source_scaler.fit(X_source)

followed by:

    X_scaled
        ↓
    source_pca
        ↓
    Z_source
        shape = (2300, 73)

Thus M03 cannot redefine the morphology representation
established by M02.

The dependency is:

    M02
    Exact 135-D morphology
          ↓
    M03
    Source standardization + PCA
          ↓
    73-D intrinsic morphology analysis space

---

# FINAL M02 LOCK

🟢 CANONICAL MORPHOLOGY = 2300 × 135

🟢 FEATURE CONSTRUCTION = FROZEN

🟢 FEATURE ORDER = FROZEN

🟢 FOREGROUND THRESHOLD = 0.8

🟢 IMAGE REPRESENTATION = 64 × 64

🟢 HORIZONTAL OCCUPANCY = 64

🟢 VERTICAL OCCUPANCY = 64

🟢 GLOBAL DESCRIPTORS = 7

🟢 TOTAL FEATURES = 135

🟢 SEMANTIC INFORMATION = NOT USED

🟢 TARGET INFORMATION = NOT USED

🟢 DOWNSTREAM MODELS = NOT USED

🔒 M02 = CAST-IRON LOCKED