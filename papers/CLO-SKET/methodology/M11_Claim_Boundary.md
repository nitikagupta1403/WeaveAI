# M11 — Evidence Integration & Claim Boundary

## Evidence class

C. Integrated Morphology Evidence

---

## STATUS

🟢 CAST-IRON LOCKED

This module integrates the preceding morphology analyses
into a single evidence chain.

The purpose is not to introduce a new statistical test.

The purpose is to determine:

    • which claims are directly supported
    • which claims are partially supported
    • which claims remain unsupported
    • which results should constrain interpretation

No new morphology representation is introduced.

No new discovery procedure is introduced.

---

# 1. PURPOSE

The preceding modules evaluate different properties of
the same frozen Clo-Sket morphology representation.

The evidence chain progresses from:

    measured morphology
        ↓
    intrinsic coordinate space
        ↓
    spectral structure
        ↓
    local geometry
        ↓
    graph organization
        ↓
    density organization
        ↓
    regional characterization
        ↓
    null testing
        ↓
    cross-scale generalization

M11 integrates these results without collapsing them into
a single score.

---

# 2. FROZEN REPRESENTATION

Canonical morphology:

    X_source ∈ R^(2300 × 135)

Operational geometry representation:

    Z_source ∈ R^(2300 × 73)

The 135-D representation remains the canonical feature
space.

The 73-D representation remains the operational PCA
geometry space.

No downstream analysis changes these definitions.

---

# 3. EVIDENCE CHAIN

## Representation

M02 establishes:

    a reproducible 135-D quantitative morphology
    representation.

The representation consists of:

    64 horizontal occupancy features
    64 vertical occupancy features
    7 global descriptors.

---

## Intrinsic coordinate space

M03 establishes:

    source-only standardization
        +
    PCA transformation

producing:

    2300 × 73

with approximately 95% retained standardized variance.

The 73-D representation is an operational geometry space.

It is not interpreted as exact manifold dimensionality.

---

## Spectral structure

M05 establishes:

    D95 = 73

and:

    effective spectral dimension ≈ 10.55

The leading principal component explains approximately:

    28.25%

of standardized morphology variance.

These quantities characterize spectral complexity.

They do not establish semantic dimensions.

---

# 4. REPLICATION STABILITY

Replication-group spectral stability is evaluated separately
in the replication perturbation evidence.

Its purpose is to determine whether the observed spectral
organization depends strongly on any single replication
group.

The replication analysis is treated as robustness evidence.

It does not create morphology categories.

It does not alter the canonical source transformation.

---

# 5. LOCAL GEOMETRIC EVIDENCE

Local morphology analyses establish that observations possess
structured nearest-neighbor relationships in the frozen
73-D space.

The local geometry is subsequently used as the basis for:

    • transition analysis
    • graph construction
    • density analysis
    • geodesic analysis

These analyses are mutually reinforcing descriptions of
the same morphology geometry.

They should not be counted as independent datasets.

---

# 6. GRAPH / GEODESIC EVIDENCE

The morphology graph is:

    k = 10

with:

    2300 nodes

and:

    39068 edges

The graph contains:

    1 connected component

with:

    2300 / 2300 observations

The observed Euclidean–geodesic rank agreement is:

    mean Spearman rho ≈ 0.869

The median is approximately:

    0.903

The median geodesic / Euclidean stretch is approximately:

    1.90

These results support a connected and locally traversable
morphology geometry.

They do not imply semantic regions.

---

# 7. DENSITY ORGANIZATION

M06 establishes independently derived density landscapes
across six observational scales.

Observed basin counts are:

    7
    6
    5
    7
    7
    8

The mean cross-scale basin agreement is approximately:

    ARI ≈ 0.734

with observed variation across scale pairs.

This supports recurring density organization while also
showing that density organization is not perfectly
scale-invariant.

No basin count is declared canonical.

---

# 8. REGIONAL MORPHOLOGY COHERENCE

M07 evaluates whether density regions are internally
morphologically coherent.

The important result is mixed.

Observed within/between distance ratios are approximately:

    1.04–1.07

across the six scales.

Therefore the analysis does NOT support a strong claim
that density regions are compact morphology clusters
under the tested global distance summary.

However, local same-region neighbor retention is substantial:

    approximately 0.755–0.845

across the scale ladder.

Therefore the strongest M07 conclusion is:

    substantial local regional coherence

rather than:

    strong global cluster compactness.

This distinction is retained.

---

# 9. REGIONAL FEATURE PROFILES

M08 establishes that independently discovered density
regions possess reproducible quantitative differences
in canonical morphology feature profiles.

Important feature groups include:

    • bounding-box geometry
    • aspect ratio
    • centroid geometry
    • symmetry
    • foreground fraction
    • horizontal occupancy
    • vertical occupancy

The feature-block analysis shows substantial contribution
from global descriptors as well as spatial occupancy
measurements.

These are quantitative associations.

They are not semantic primitives.

---

# 10. PROFILE SEPARATION QUALIFICATION

The regional profile silhouette values are negative
across all six tested scales.

Therefore the regional profiles should NOT be described
as cleanly separated compact feature-space clusters.

The defensible interpretation is:

    reproducible quantitative regional organization
    with substantial profile overlap.

This negative result is retained as part of the evidence.

---

# 11. PERMUTATION NULL

M09 tests regional feature discrimination against a
size-matched permutation null.

The observed regional discrimination exceeds the null
most clearly at lower and intermediate scales.

Observed p-values include:

    0.004975
    0.009950
    0.004975
    0.054726
    0.134328
    0.169154

across the six scales.

Therefore the regional feature association is:

    supported at several scales

but:

    not uniformly supported across the entire scale ladder.

This scale dependence must remain explicit.

---

# 12. CROSS-SCALE GENERALIZATION

M10 evaluates whether quantitative regional morphology
organization remains recognizable across independently
derived density scales.

Cross-scale feature-profile correlations are extremely high:

    approximately 0.998–1.000

across the reported scale pairs.

This supports strong reproducibility of quantitative
regional profile structure.

The result does NOT imply that individual basin identities
are identical across scales.

The generalized quantity is:

    regional quantitative profile structure

not:

    basin identity.

---

# 13. INTEGRATED EVIDENCE ASSESSMENT

The morphology evidence can therefore be summarized as:

### STRONGLY SUPPORTED

    ✓ reproducible quantitative morphology representation

    ✓ source-only dimensionality reduction

    ✓ strong spectral concentration

    ✓ connected morphology graph

    ✓ strong Euclidean–geodesic rank agreement

    ✓ recurring multiscale density organization

    ✓ highly reproducible quantitative regional profiles

    ✓ cross-scale regional profile generalization

---

### SUPPORTED WITH QUALIFICATION

    ~ local regional coherence

    ~ regional feature association

    ~ cross-scale density-region recurrence

These results are real but not uniform across every
distance statistic or observational scale.

---

### NOT ESTABLISHED

    ✗ compact discrete morphology clusters

    ✗ semantic morphology categories

    ✗ named morphology primitives

    ✗ morphology grammar

    ✗ exact manifold dimensionality

    ✗ causal morphology structure

    ✗ preferred number of morphology states

    ✗ preferred density scale

---

# 14. CENTRAL SCIENTIFIC CLAIM

The integrated evidence supports the following
conservative statement:

    Fashion sketches in the Clo-Sket source collection
    admit a reproducible quantitative morphology
    representation whose geometry exhibits structured
    local relationships, connected graph organization,
    recurring multiscale density structure, and
    reproducible quantitative regional morphology
    profiles.

This supports the existence of structured morphology
organization in the measured representation.

It does NOT by itself establish a semantic language.

---

# 15. SEMANTIC-LANGUAGE BOUNDARY

The phrase:

    "semantic language of fashion sketches"

must therefore be treated as the broader scientific
hypothesis motivating the study.

The current evidence establishes the quantitative
morphology foundation required for investigating that
hypothesis.

The evidence does not yet justify the stronger statement:

    "fashion sketches have a discovered semantic grammar."

That claim requires additional evidence connecting
quantitative morphology organization to meaningful
structural or semantic units.

---

# 16. DISCOVERY / VALIDATION BOUNDARY

The core morphology organization is discovered without:

    category labels
    replication labels
    target sketches
    semantic labels
    supervised prediction
    GMM
    KMeans
    hierarchy
    CNN
    neural networks

External structure may be introduced later only as
independent validation.

This preserves the distinction between:

    discovery

and:

    validation.

---

# 17. EVIDENCE DEPENDENCE

The individual analyses should not be treated as
statistically independent pieces of evidence.

They operate on:

    the same 2300 observations

and:

    the same frozen morphology representation.

Therefore the paper should present them as a coherent
sequence of complementary analyses rather than as a
large number of independent hypothesis tests.

The value comes from convergence of different diagnostics
on the same representation.

---

# 18. MAIN PAPER VS SUPPLEMENTARY EVIDENCE

The main paper should emphasize the shortest defensible
evidence chain:

    representation
        ↓
    intrinsic geometry
        ↓
    graph / continuity
        ↓
    density recurrence
        ↓
    quantitative regional profiles
        ↓
    null validation
        ↓
    cross-scale generalization

Detailed feature rankings, individual perturbation
results, and extensive basin-level tables can be retained
as supplementary evidence.

This prevents the central scientific argument from becoming
a catalog of diagnostics.

---

# 19. CLAIM BOUNDARY

M11 establishes the final boundary for the geometry-first
morphology evidence.

It supports:

    ✓ structured quantitative morphology organization

    ✓ reproducibility

    ✓ local geometric organization

    ✓ connected morphology geometry

    ✓ recurring density organization

    ✓ reproducible regional morphology profiles

    ✓ cross-scale quantitative generalization

It does not support:

    ✗ semantic categories

    ✗ semantic primitives

    ✗ grammar

    ✗ causal interpretation

    ✗ exact manifold dimension

---

# 20. FINAL M11 LOCK

The integrated evidence chain is:

    M02
        exact quantitative morphology representation

        ↓

    M03
        frozen source transformation

        ↓

    M05
        spectral structure

        ↓

    E03
        replication stability

        ↓

    E04
        local morphology geometry

        ↓

    E05
        graph / geodesic organization

        ↓

    M06
        multiscale density organization

        ↓

    M07
        local regional coherence

        ↓

    M08
        regional feature profiles

        ↓

    M09
        permutation-null validation

        ↓

    M10
        cross-scale generalization

        ↓

    M11
        integrated claim boundary

---

# FINAL M11 STATUS

🟢 EVIDENCE CHAIN INTEGRATED

🟢 POSITIVE RESULTS RETAINED

🟢 MIXED RESULTS RETAINED

🟢 NEGATIVE RESULTS RETAINED

🟢 CLAIMS NARROWED TO EVIDENCE

🟢 DISCOVERY / VALIDATION SEPARATED

🟢 NO SEMANTIC OVERCLAIM

🟢 NO CATEGORY ASSUMPTIONS

🟢 NO TARGET LEAKAGE

🟢 NO CNN / NN REQUIRED

🔒 M11 = CAST-IRON LOCKED