# M05 — Spectral Characterization & Effective Dimensionality

## Evidence class

A. Morphology Representation → Intrinsic Geometry

---

## STATUS

🟢 CAST-IRON LOCKED

This module characterizes the spectral structure of the
canonical 135-D morphology representation.

The purpose is to quantify:

    • variance concentration
    • eigenvalue decay
    • variance-retention dimensions
    • effective spectral dimensionality

These quantities describe the complexity of the observed
morphology representation.

They are not interpreted as exact manifold dimensionality.

---

# 1. INPUT

Canonical source morphology:

    X_source ∈ R^(2300 × 135)

The canonical representation is defined in M02.

The source standardization procedure is defined in M03.

The spectral analysis therefore operates on the standardized
Clo-Sket morphology representation.

---

# 2. STANDARDIZED MORPHOLOGY SPACE

Let:

    X_scaled = source_scaler.transform(X_source)

where `source_scaler` is fitted using the Clo-Sket source
morphology matrix only.

No target or external dataset contributes to the
standardization.

The standardized morphology representation therefore has:

    N = 2300 observations
    D = 135 standardized morphology features

---

# 3. SPECTRAL DECOMPOSITION

The covariance structure of the standardized morphology
representation is characterized through principal-component
eigenvalues.

Let the ordered eigenvalues be:

    λ₁ ≥ λ₂ ≥ ... ≥ λ₁₃₅ ≥ 0

The corresponding explained-variance contribution of
component k is:

    p_k = λ_k / Σ_j λ_j

The cumulative variance through component k is:

    C_k = Σ_{j=1}^{k} p_j

The spectrum is therefore characterized independently of
any semantic or categorical interpretation.

---

# 4. FULL-SPECTRUM REQUIREMENT

Spectral retention dimensions are evaluated from the complete
135-dimensional eigenvalue spectrum.

This is necessary because retention thresholds extending
beyond 73 components cannot be recovered from a PCA object
containing only the first 73 components.

Therefore two related quantities are distinguished:

### Full spectral characterization

    complete 135-component spectrum

Used for:

    • eigenvalue decay
    • cumulative variance
    • D80
    • D85
    • D90
    • D95
    • D97.5
    • D99
    • participation-ratio effective dimension

### Operational geometry representation

    73-component PCA representation

Used downstream as the principal coordinate space for
morphology geometry analysis.

Thus:

    full spectrum
        ≠
    retained operational geometry coordinates

---

# 5. VARIANCE-RETENTION DIMENSION

For a variance threshold τ, define:

    D_τ =
        minimum k such that
        C_k ≥ τ

The observed source spectrum gives:

    D80  = 32
    D85  = 41
    D90  = 53
    D95  = 73
    D97.5 = 91
    D99  = 108

Therefore the standardized 135-D morphology representation
shows substantial variance concentration in a substantially
smaller number of principal directions.

---

# 6. 95% VARIANCE REPRESENTATION

The 95% variance criterion gives:

    D95 = 73

Therefore the operational PCA representation is:

    Z_source ∈ R^(2300 × 73)

This is the representation used for the principal-coordinate
morphology geometry analyses.

The 73-dimensional representation is therefore a
variance-retaining analysis space.

It is not claimed to be the exact dimensionality of an
underlying morphology manifold.

---

# 7. SPECTRAL DECAY

The PCA spectrum is characterized by the ordered eigenvalues:

    λ₁, λ₂, ..., λ₁₃₅

and their cumulative variance:

    C₁, C₂, ..., C₁₃₅

The observed spectrum is strongly non-uniform.

A substantial fraction of total standardized morphology
variance is concentrated in the leading principal directions.

This motivates examination of effective spectral complexity
in addition to simple variance-retention thresholds.

---

# 8. LEADING PRINCIPAL COMPONENT

The first principal component accounts for approximately:

    PC01 variance = 0.2825302263

or approximately:

    28.25%

of the total standardized morphology variance.

This indicates that a substantial proportion of the observed
morphology variance is concentrated along the leading
principal direction.

The result is descriptive of the representation.

It does not assign a semantic meaning to PC01.

---

# 9. PARTICIPATION-RATIO EFFECTIVE DIMENSION

The effective spectral dimensionality is calculated using
the participation ratio.

For eigenvalues λ₁,...,λ_D:

    D_eff =
        (Σ λ_i)² /
        Σ λ_i²

Equivalently, using normalized spectral weights:

    p_i = λ_i / Σ λ_j

    D_eff =
        1 /
        Σ p_i²

The participation ratio measures the effective number of
principal directions contributing to the observed spectral
variance.

---

# 10. OBSERVED EFFECTIVE DIMENSION

The source morphology spectrum gives:

    D_eff ≈ 10.549

This is interpreted as an effective spectral complexity
measure.

It does NOT mean:

    morphology manifold dimension = 10.549

and it does NOT mean:

    exact intrinsic dimension = 10.549

The quantity summarizes variance concentration across the
principal spectrum.

---

# 11. DISTINCTION BETWEEN DIMENSIONALITY QUANTITIES

Three different quantities are therefore maintained:

### Original feature dimensionality

    D_feature = 135

This is the canonical morphology representation defined in M02.

### Variance-retention dimensionality

    D95 = 73

This is the number of principal components required to retain
approximately 95% of standardized morphology variance.

### Effective spectral dimensionality

    D_eff ≈ 10.55

This describes the concentration of variance across the
eigenvalue spectrum.

These quantities answer different questions.

Therefore:

    135
      ≠
    73
      ≠
    10.55

and none is automatically equivalent to an exact mathematical
manifold dimension.

---

# 12. GEOMETRY-SPACE INTERFACE

The spectral analysis establishes:

    135-D canonical morphology
            ↓
    standardized morphology
            ↓
    PCA spectrum
            ↓
    73-D 95%-variance representation

The 73-D representation is subsequently used as:

    Z_source

for:

    • local morphology neighborhoods
    • continuity analysis
    • transition analysis
    • graph construction
    • geodesic analysis
    • density organization
    • cross-scale morphology analysis

The original 135-D representation remains frozen for
feature-level analyses.

---

# 13. SPECTRAL ANALYSIS INDEPENDENCE

The spectral characterization uses morphology geometry only.

It does not use:

    category labels
    replication labels
    target sketches
    semantic labels
    morphology-state labels
    GMM
    KMeans
    hierarchical clustering
    supervised prediction
    CNN
    neural networks

The spectrum is therefore derived independently of
morphology-state discovery.

---

# 14. RELATION TO REPLICATION-GROUP STABILITY

Spectral characterization defines the reference spectrum.

A separate replication-group perturbation analysis tests
whether this spectral structure remains stable when complete
replication groups are removed.

Therefore:

    M05
        defines and characterizes
        the canonical spectral structure

    E03
        tests stability of that structure
        under replication-group perturbation

The two analyses must remain conceptually separate.

---

# 15. CLAIM BOUNDARY

M05 establishes:

    ✓ the eigenvalue spectrum of standardized morphology

    ✓ variance concentration across principal directions

    ✓ variance-retention dimensions

    ✓ D95 = 73

    ✓ D_eff ≈ 10.55

    ✓ a reproducible 73-D operational morphology space

    ✓ a distinction between variance-retention dimension
      and effective spectral dimensionality

M05 does NOT establish:

    ✗ exact manifold dimensionality

    ✗ a morphology manifold in the strict mathematical sense

    ✗ morphology categories

    ✗ morphology states

    ✗ semantic morphology primitives

    ✗ morphology grammar

    ✗ causal morphology structure

    ✗ an optimal number of morphology modes

---

# 16. FINAL SPECTRAL LOCK

Canonical morphology:

    2300 × 135

Full spectral characterization:

    135 eigenvalue directions

Variance-retention dimensions:

    D80  = 32
    D85  = 41
    D90  = 53
    D95  = 73
    D97.5 = 91
    D99  = 108

Leading component:

    PC01 = 28.253%

Effective spectral dimension:

    D_eff ≈ 10.549

Operational geometry space:

    2300 × 73

Interpretation:

    variance-retaining intrinsic analysis space

NOT:

    exact manifold dimension

---

# FINAL M05 LOCK

🟢 FULL SPECTRUM CHARACTERIZED

🟢 VARIANCE RETENTION QUANTIFIED

🟢 D95 = 73

🟢 EFFECTIVE DIMENSION ≈ 10.55

🟢 PC01 ≈ 28.25%

🟢 135-D CANONICAL SPACE REMAINS FROZEN

🟢 73-D GEOMETRY SPACE REMAINS FROZEN

🟢 NO SEMANTIC INTERPRETATION

🟢 NO CATEGORY LABELS

🟢 NO TARGET FITTING

🟢 NO KMEANS REQUIRED

🟢 NO CNN / NN

🔒 M05 = CAST-IRON LOCKED