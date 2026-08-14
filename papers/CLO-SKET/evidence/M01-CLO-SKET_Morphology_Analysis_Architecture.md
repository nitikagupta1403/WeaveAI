# M01 — CLO-SKET Morphology Analysis Architecture

## 1. STUDY OBJECTIVE

The objective of the morphology analysis is to determine
whether garment sketches represented by quantitative
morphology descriptors exhibit an organized geometric
structure that can be characterized independently of
semantic category labels.

The analysis is designed to answer, in sequence:

    Is morphology geometrically structured?
            ↓
    Is the structure locally continuous?
            ↓
    Is the geometry connected?
            ↓
    Does recurring density organization exist?
            ↓
    Are regional structures quantitatively reproducible?
            ↓
    Which measurable morphology properties participate
    in that organization?

Semantic interpretation is deliberately deferred.

---

## 2. CANONICAL DATA

Number of observations:

    N = 2300

Canonical morphology representation:

    X = 2300 × 135

Feature families:

    horizontal occupancy
        64 features

    vertical occupancy
        64 features

    global morphology descriptors
        7 features

Total:

    135 quantitative morphology features

The canonical morphology matrix is frozen after
construction.

---

## 3. REPRESENTATION PREPARATION

The canonical morphology representation is standardized
before geometric analysis.

Standardized feature matrix:

    X_standardized

The morphology covariance / spectral structure is then
characterized using PCA.

Variance-retention analysis gives:

    D80 = 32
    D90 = 53
    D95 = 73
    D99 = 108

The primary intrinsic morphology representation used
throughout the local-geometry analyses is:

    2300 × 73

corresponding approximately to 95% retained variance.

---

## 4. DISCOVERY / VALIDATION SEPARATION

The analysis distinguishes between:

### Discovery

Morphology geometry is derived solely from the canonical
quantitative morphology representation.

Discovery does NOT use:

    category labels
    replication labels
    target sketches
    learned semantic representations

### Validation

Subsequent analyses test whether the discovered structure
is robust to:

    • observation resampling
    • replication-group perturbation
    • feature perturbation
    • representation changes
    • density scale changes
    • permutation nulls

Validation does not redefine the canonical morphology
representation.

---

## 5. SPECTRAL CHARACTERIZATION

The first stage characterizes the dimensional structure
of the standardized morphology matrix.

Measures include:

    • variance-retention dimensions
    • eigenvalue spectrum
    • participation-ratio effective dimension
    • spectral resampling stability
    • replication-group spectral stability

The participation-ratio effective dimension was:

    ≈ 10.55

This is treated as an effective spectral complexity
measure.

It is NOT interpreted as an exact manifold dimension.

---

## 6. LOCAL GEOMETRY

Local morphology organization is examined using
neighborhood relationships in the intrinsic morphology
space.

Analyses include:

    • neighborhood-radius progression
    • relative neighborhood growth
    • local gap statistics
    • directional consistency
    • continuity permutation null

The purpose is to determine whether nearby morphology
observations form locally organized neighborhoods rather
than widespread abrupt separation.

---

## 7. CROSS-REPRESENTATION VALIDATION

The morphology geometry is compared against independently
constructed quantitative descriptions:

    pooled occupancy
    coarse silhouette
    multiscale profile

Each representation is independently reduced to its
intrinsic space.

The analysis compares:

    • nearest-neighbor agreement
    • local distance-rank agreement

No representation is selected because it produces stronger
clustering.

The purpose is robustness testing only.

---

## 8. INTRINSIC-DIMENSION ROBUSTNESS

Dimensional complexity is characterized independently of
the PCA variance criterion.

The analysis evaluates:

    • local intrinsic-dimension estimates
    • subsample stability
    • cross-representation dimensionality

The local kNN intrinsic-dimension estimator produced
estimates exceeding the ambient dimensionality and was
therefore treated as numerically unstable.

Consequently:

    no exact manifold dimension is claimed.

Spectral dimensionality is retained as the more stable
empirical characterization.

---

## 9. SPECTRAL INFLUENCE ROBUSTNESS

The morphology spectrum is tested for sensitivity to
observation composition.

Two complementary approaches are used:

    uniform observation resampling

and

    complete replication-group removal.

For each resampled dataset:

    PCA is recomputed independently.

Measured quantities include:

    D80
    D90
    D95
    D99
    effective dimension
    leading eigenvalue contribution
    eigenspace alignment

This tests whether spectral conclusions depend strongly
on particular observations or replication groups.

---

## 10. CONTINUOUS MORPHOLOGY ORGANIZATION

The morphology space is evaluated for locally organized
transitions.

Measures include:

    • one-step neighborhood transitions
    • neighborhood overlap
    • two-step distances
    • local scale continuity
    • directional transition consistency

These analyses are interpreted as evidence about local
geometric organization.

They are NOT interpreted as discrete morphology states.

---

## 11. GRAPH GEOMETRY

A k-nearest-neighbor morphology graph is constructed.

Primary graph analysis:

    k = 10

The graph is evaluated for:

    • connectivity
    • reachability
    • geodesic distance
    • local path stretch
    • Euclidean–geodesic rank agreement

The purpose is to determine whether morphology
relationships remain traversable through connected
geometric neighborhoods.

Graph regions are not treated as semantic categories.

---

## 12. MULTISCALE DENSITY ORGANIZATION

Density-ascent analysis is applied at multiple observational
scales.

Six density scales are evaluated.

At each scale:

    density basins are independently derived
    from morphology geometry.

The number of basins is NOT predetermined.

Observed basin counts ranged from:

    5 to 8

depending on observational scale.

Cross-scale agreement is evaluated using:

    • pairwise ARI
    • observation-level consensus
    • cross-scale co-membership

The purpose is to determine whether recurring density
organization exists within the continuous morphology space.

---

## 13. DENSITY BOUNDARY VALIDATION

Density regions are subjected to boundary / gap analysis.

The analysis examines:

    local distance gaps
    density depletion
    cross-scale recurrence

The purpose is to distinguish recurring density
organization from arbitrary partitioning of observations.

Density regions remain discovery outputs rather than
predefined categories.

---

## 14. REGION MORPHOLOGY COHERENCE

For each density scale, regional morphology structure is
examined using:

    within-region morphology distance
    between-region morphology distance
    local same-region neighbor retention

Importantly, the analysis does NOT require regions to be
compact clusters.

The observed result showed that within-region distances
were not substantially smaller than between-region
distances.

Therefore the final interpretation is:

    density regions embedded within a continuous
    morphology geometry

rather than:

    compact discrete morphology clusters.

---

## 15. REGION–FEATURE PROFILES

Each density region is represented by a quantitative
morphology profile.

Profile variables include:

    horizontal occupancy
    vertical occupancy
    centroid geometry
    bounding-box geometry
    aspect ratio
    symmetry
    foreground fraction

The analysis evaluates:

    • feature-level regional discrimination
    • regional profile contrast
    • cross-scale profile consistency

Basin IDs are not assumed to correspond across scales.

Instead, quantitative profile structure is compared.

---

## 16. REGIONAL PERMUTATION NULL

Regional feature discrimination is tested against a
size-preserving permutation null.

The null preserves:

    • number of regions
    • region-size distribution
    • overall feature distributions

while destroying:

    morphology–region membership association.

This determines whether regional morphology differences
exceed what would be expected from arbitrary assignment
to regions of equivalent sizes.

---

## 17. FEATURE CONTRIBUTION

Feature participation in morphology geometry is examined
using:

    • local morphology gradients
    • feature–distance associations
    • feature-block contributions

The three feature families are:

    horizontal occupancy
    vertical occupancy
    global descriptors

Strong feature association is interpreted as quantitative
participation in morphology geometry.

It is NOT interpreted as semantic meaning.

---

## 18. FEATURE PERTURBATION

Structural influence is tested by removing complete
feature blocks and evaluating preservation of the frozen
morphology geometry.

Perturbations include:

    remove horizontal occupancy
    remove vertical occupancy
    remove global descriptors

Nearest-neighbor overlap is the primary structural
preservation metric.

This distinguishes:

    feature association

from:

    structural influence.

---

## 19. BLOCK COMPLEMENTARITY

Representations are evaluated using:

    H
    V
    G
    H + V
    H + G
    V + G
    H + V + G

where:

    H = horizontal occupancy
    V = vertical occupancy
    G = global descriptors

The purpose is to determine whether feature blocks provide
redundant or complementary information.

The complete representation preserves substantially more
of the reference morphology geometry than any individual
block.

---

## 20. SPATIAL-ORDER CONTROL

Occupancy feature ordering is independently permuted while
preserving feature values.

Conditions include:

    horizontal ordering shuffled
    vertical ordering shuffled
    both shuffled

The analysis asks whether the tested geometry depends on
explicit feature ordering.

In the current representation, spatial-order permutation
produced no measurable change in the tested neighborhood
overlap.

Therefore the current result is interpreted specifically as:

    geometry depends primarily on occupancy values /
    distributions rather than their explicit coordinate
    ordering.

This conclusion is representation-specific.

---

## 21. CROSS-SCALE REGION–FEATURE GENERALIZATION

Regional morphology profiles are compared across the six
density scales.

The analysis evaluates:

    • profile-distance structure
    • feature-profile correlation
    • feature-level consistency
    • feature-block consistency

Basin identity is never forced across scales.

The purpose is to determine whether quantitative regional
morphology organization generalizes across observational
scale.

---

## 22. STATISTICAL NULLS

Where appropriate, permutation nulls are used to test
whether observed structure exceeds expectations under
destroyed morphology relationships.

Null construction preserves relevant structural quantities
such as:

    region size
    number of regions
    feature distributions

while disrupting the relationship under investigation.

Observed effects are therefore interpreted relative to
explicit null models rather than by magnitude alone.

---

## 23. MODEL-INDEPENDENCE LOCK

The morphology geometry evidence does not require:

    CNN
    neural network
    autoencoder
    transformer
    GMM
    KMeans
    hierarchical clustering

No learned representation is used to establish the
primary morphology geometry.

A neural representation, if evaluated later, must be
treated as a separate representation-learning experiment.

---

## 24. SEMANTIC INTERPRETATION LOCK

Throughout the geometry analysis:

    quantitative morphology feature
        ≠
    semantic morphology primitive

    density basin
        ≠
    morphology category

    density recurrence
        ≠
    semantic state

    effective dimension
        ≠
    manifold dimension

These distinctions are maintained throughout the analysis.

---

## 25. FINAL ANALYTICAL LOGIC

The complete analysis follows:

    quantitative sketch morphology
                ↓
    standardized canonical representation
                ↓
    intrinsic morphology geometry
                ↓
    spectral characterization
                ↓
    local continuity
                ↓
    connected graph geometry
                ↓
    multiscale density organization
                ↓
    recurring regional profiles
                ↓
    permutation validation
                ↓
    feature contribution / perturbation
                ↓
    cross-scale generalization
                ↓
    evidence-bound morphology characterization

---

## 26. FINAL GEOMETRIC CLAIM

The analysis supports characterization of Clo-Sket as:

    a continuous and connected quantitative morphology
    geometry containing recurring density-organized
    regions with reproducible quantitative morphology
    profiles.

The analysis does NOT yet establish:

    semantic primitives
    morphology states
    morphology grammar
    causal morphology structure
    exact manifold dimensionality.

---

## 27. PAPER POSITION

This entire architecture constitutes the evidence base
for the morphology-understanding component of Paper I.

The analysis is deliberately completed before introducing
a learned neural representation.

The next methodological question is therefore NOT:

    "Can a CNN discover the morphology?"

It is:

    "Given the empirically established morphology geometry,
     what representation or formalism can encode its
     measurable structure without discarding the evidence
     already established?"

