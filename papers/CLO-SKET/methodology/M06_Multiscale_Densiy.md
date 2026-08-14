# M06 — Multiscale Density Landscape & Basin Construction

## Evidence class

A. Intrinsic Geometry → Density Organization

---

## STATUS

🟢 CAST-IRON LOCKED

This module defines the unsupervised multiscale density
analysis applied to the frozen 73-D intrinsic morphology
space.

The purpose is to determine whether recurring density
organization can be observed within morphology geometry
without imposing a predetermined number of morphology
states.

Density organization is treated as a geometric property
of the morphology representation.

It is not interpreted as semantic categorization.

---

# 1. INPUT

The analysis receives the frozen source morphology
geometry established by M03:

    Z_source ∈ R^(2300 × 73)

where:

    N = 2300 observations
    D = 73 PCA coordinates

The 73-D representation is not refitted during density
analysis.

No target data are used.

---

# 2. OBJECTIVE

The density analysis asks:

    Does the morphology geometry contain recurring
    regions of observational density?

The analysis deliberately does NOT ask:

    How many morphology categories exist?

Instead, density structure is examined across multiple
empirically determined observational scales.

---

# 3. LOCAL DISTANCE SCALE

For each observation, local morphology distance is first
characterized using its k-nearest-neighbor neighborhood.

The local-neighborhood scale is:

    k = 5

For observation i, let:

    d_i^(5)

denote its distance to the fifth nearest neighbor in
the frozen 73-D morphology space.

The empirical distribution of these distances provides
the basis for selecting observational density scales.

---

# 4. EMPIRICAL SCALE LADDER

Six density scales are defined from empirical quantiles
of the fifth-nearest-neighbor distance distribution.

The selected quantiles are:

    Q25
    Q40
    Q55
    Q70
    Q85
    Q95

The resulting observed scales are:

    scale 1 = 4.707252
    scale 2 = 5.416895
    scale 3 = 6.248407
    scale 4 = 7.596034
    scale 5 = 10.640832
    scale 6 = 16.568532

These scales are therefore determined from the observed
morphology geometry rather than selected to produce a
desired number of regions.

---

# 5. KERNEL DENSITY ESTIMATION

For each observational scale h, a Gaussian kernel density
estimate is constructed in the frozen 73-D morphology space.

The density at observation x is conceptually:

    ρ_h(x)
        =
    (1 / N)
    Σ_i K_h(x - x_i)

where K_h is the Gaussian kernel associated with scale h.

The density landscape is recomputed independently at each
of the six observational scales.

No category information enters density estimation.

---

# 6. DENSITY MAXIMA

Local density maxima are identified from the estimated
density landscape.

A density maximum represents a location in morphology
space around which observations exhibit locally elevated
estimated density at the corresponding observational
scale.

Density maxima are not interpreted as morphology
categories.

They are geometric features of the estimated density
landscape.

---

# 7. DENSITY-ASCENT BASINS

Each observation is assigned to a density maximum by
following local density ascent.

Conceptually:

    observation
         ↓
    local density comparison
         ↓
    move toward higher-density neighbor
         ↓
    repeat
         ↓
    terminal density maximum
         ↓
    basin membership

Observations terminating at the same local maximum form
a density-ascent basin.

Thus basin membership emerges from the density landscape.

No basin count is specified in advance.

---

# 8. OBSERVED BASIN COUNTS

The six observational scales produce:

    scale = 4.707252
        basins = 7

    scale = 5.416895
        basins = 6

    scale = 6.248407
        basins = 5

    scale = 7.596034
        basins = 7

    scale = 10.640832
        basins = 7

    scale = 16.568532
        basins = 8

The variation in basin count across scales is retained as
an observed property of the density landscape.

No single basin count is declared canonical.

---

# 9. SCALE-INDEPENDENCE PRINCIPLE

The analysis deliberately avoids selecting one preferred
density scale.

Instead:

    six observational scales
        ↓
    six independently derived density landscapes
        ↓
    six basin organizations

are compared.

This allows persistent organization to be distinguished
from structure that appears only at a particular
smoothing scale.

---

# 10. CROSS-SCALE AGREEMENT

Basin organizations are compared across scales using
observation-level and pairwise agreement measures.

The principal comparison is:

    adjusted Rand index (ARI)

between independently derived basin assignments.

The analysis also computes observation-level cross-scale
consensus and cross-scale co-membership.

These measures quantify whether observations tend to
remain associated with similar density regions as the
observational scale changes.

---

# 11. OBSERVED CROSS-SCALE AGREEMENT

The observed pairwise basin agreement is:

    mean pairwise ARI ≈ 0.734

with:

    minimum ARI ≈ 0.498

    maximum ARI ≈ 0.926

Observation-level consensus is:

    mean ≈ 0.874

and approximately:

    1917 / 2300 = 83.35%

of observations have consensus ≥ 0.90.

These results indicate that substantial cross-scale
recurrence exists, while also showing that basin
organization is not perfectly invariant across scales.

---

# 12. CROSS-SCALE INTERPRETATION

High agreement across independently derived scales is
interpreted as evidence that density organization recurs
within the morphology geometry.

Lower agreement indicates scale-dependent density
organization.

Therefore the analysis distinguishes:

    persistent broad organization

from:

    finer-scale or scale-dependent density structure.

No requirement is imposed that all observations belong
to a single scale-invariant partition.

---

# 13. BASIN IDENTITIES ARE NOT SEMANTIC IDENTITIES

A basin identifier is only an identifier for a density
maximum within one density landscape.

Therefore:

    basin 307 at scale A

does NOT automatically mean:

    basin 307 at scale B

represents the same morphology region.

Basin IDs are not matched across scales by label.

Cross-scale comparisons instead use quantitative
agreement measures and profile structure.

---

# 14. DISCOVERY-ONLY LOCK

Density discovery uses only:

    frozen 73-D morphology geometry

It does not use:

    category labels
    replication labels
    target sketches
    target labels
    semantic labels
    KMeans
    GMM
    hierarchical clustering
    supervised learning
    CNN
    neural networks

The density landscape is therefore discovered independently
of external category structure.

---

# 15. RELATION TO LATER VALIDATION

M06 establishes density organization.

It does not by itself establish that density regions
correspond to meaningful morphology organization.

Later evidence tests whether independently discovered
regions exhibit:

    • morphological coherence
    • reproducible quantitative feature profiles
    • stronger-than-null feature differences
    • cross-scale profile generalization

Therefore:

    M06
        ↓
    density organization discovered

followed by:

    E07/E08/E09/E10
        ↓
    density-region structure validated and characterized

---

# 16. CLAIM BOUNDARY

M06 establishes:

    ✓ a reproducible multiscale density-analysis procedure

    ✓ six empirically derived observational scales

    ✓ density-ascent basin organization

    ✓ observed basin counts at each scale

    ✓ cross-scale basin agreement

    ✓ recurring density organization within morphology space

M06 does NOT establish:

    ✗ morphology categories

    ✗ semantic morphology states

    ✗ semantic primitives

    ✗ morphology grammar

    ✗ a preferred number of morphology modes

    ✗ exact manifold dimensionality

    ✗ causal morphology structure

    ✗ semantic interpretation of any basin

---

# 17. FINAL M06 LOCK

Input:

    Z_source = 2300 × 73

Local scale:

    5-nearest-neighbor distance

Empirical scale quantiles:

    Q25
    Q40
    Q55
    Q70
    Q85
    Q95

Observed scales:

    4.707252
    5.416895
    6.248407
    7.596034
    10.640832
    16.568532

Density model:

    Gaussian KDE

Region discovery:

    density maxima
        +
    density ascent

Observed basin counts:

    7
    6
    5
    7
    7
    8

Cross-scale agreement:

    mean ARI ≈ 0.734

Observation consensus:

    mean ≈ 0.874

Interpretation:

    recurring quantitative density organization

NOT:

    semantic morphology states

---

# FINAL M06 STATUS

🟢 INPUT SPACE FROZEN

🟢 SCALE LADDER EMPIRICAL

🟢 NO PREFERRED SCALE

🟢 NO PREDEFINED BASIN COUNT

🟢 DENSITY DISCOVERY UNSUPERVISED

🟢 BASIN IDENTITIES NOT FORCED ACROSS SCALES

🟢 CROSS-SCALE RECURRENCE QUANTIFIED

🟢 SEMANTIC INTERPRETATION LOCKED OUT

🟢 TARGET DATA EXCLUDED

🟢 CATEGORY LABELS EXCLUDED

🟢 CNN / NN EXCLUDED

🔒 M06 = CAST-IRON LOCKED