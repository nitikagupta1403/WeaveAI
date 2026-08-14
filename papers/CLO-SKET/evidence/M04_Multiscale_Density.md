# M04 — Multiscale Density / Basin Discovery Specification

## Evidence class

A. Continuous Morphology Geometry
→
B. Multiscale Density Organization

---

## 1. PURPOSE

The purpose of this analysis is to determine whether the
continuous morphology geometry contains recurring density
organization across observational scales.

The analysis does not impose a morphology-state count.

Instead:

    morphology geometry
        ↓
    empirical observational scales
        ↓
    density landscapes
        ↓
    local density maxima
        ↓
    density-ascent basins
        ↓
    cross-scale persistence

---

## 2. INPUT

Canonical morphology:

    X ∈ R^(2300 × 135)

The morphology representation is standardized using a
source-only StandardScaler.

The standardized representation is transformed using:

    PCA(
        n_components=0.95,
        svd_solver="full"
    )

Result:

    Z ∈ R^(2300 × 73)

The 73-D representation is the morphology coordinate
space used for all density analysis.

---

## 3. EMPIRICAL NEIGHBORHOOD GEOMETRY

Nearest-neighbor distances are computed in the 73-D
intrinsic morphology space.

The initial neighborhood calculation uses:

    n_neighbors = 21

with Euclidean distance.

The self-distance is removed.

The resulting non-self neighborhood distances are used
to characterize empirical morphology scales.

No clustering algorithm is used at this stage.

No density model is used to determine the scale ladder.

---

## 4. EMPIRICAL SCALE LADDER

The observational scales are derived directly from the
distribution of the 5-nearest-neighbor distances.

The five-nearest-neighbor distance for observation i is:

    d5(i)

The six observational scales are defined as:

    s_q = Quantile_q({d5(i)})

for:

    q ∈ {
        0.25,
        0.40,
        0.55,
        0.70,
        0.85,
        0.95
    }

Therefore:

    scale_ladder =
        [
            Q25(d5),
            Q40(d5),
            Q55(d5),
            Q70(d5),
            Q85(d5),
            Q95(d5)
        ]

The resulting empirical scales are:

    4.707252
    5.416895
    6.248407
    7.596034
    10.640832
    16.568532

The ladder is required to be strictly increasing.

---

## 5. INTERPRETATION OF SCALE

The scale values are observational bandwidth scales
derived from morphology neighborhood geometry.

They are NOT:

    • morphology-state counts
    • cluster counts
    • optimized mode counts
    • semantic categories
    • externally imposed thresholds

The scale ladder therefore provides an empirical
local → intermediate → broad characterization of
morphology density structure.

---

## 6. MULTISCALE DENSITY ESTIMATION

At each empirical scale s_j, a Gaussian kernel density
estimator is fitted to the complete 73-D morphology
representation.

For scale s_j:

    KDE_j =
        KernelDensity(
            bandwidth=s_j,
            kernel="gaussian"
        )

The estimator is fitted to:

    Z = X_intrinsic

No labels are used.

---

## 7. RELATIVE DENSITY

The KDE returns log-density values:

    log p_j(z_i)

To remove arbitrary absolute density-scale differences
between bandwidths, density values are converted to
relative density:

    r_j(i)
      =
    exp(
        log p_j(z_i)
        -
        max_i log p_j(z_i)
    )

Thus:

    0 < r_j(i) ≤ 1

within each observational scale.

The maximum-density observation at each scale therefore
has relative density:

    1.0

The resulting matrix is:

    density_matrix ∈ R^(2300 × 6)

---

## 8. DENSITY RANKS

For each scale, relative-density values are converted
to normalized ranks.

For each scale j:

    rank_j(i)

is the normalized ordering of observations by density.

Ranks are used for descriptive density-core persistence
analysis.

---

## 9. DENSITY-CORE PERSISTENCE

Descriptive density cores are examined at:

    90th percentile
    95th percentile
    98th percentile

of the within-scale density ranking.

For each observation, the number of scales on which it
belongs to the selected density core is recorded.

This analysis asks whether high-density morphology
observations recur across scales.

These cores are NOT clusters.

They do not define morphology states.

---

## 10. LOCAL DENSITY-MAXIMUM DETECTION

Candidate density modes are identified independently
at each scale.

A separate 5-nearest-neighbor graph is constructed in
the 73-D morphology space:

    n_neighbors = 6

The self-neighbor is removed, leaving:

    K = 5

local neighbors.

For observation i at scale j, let:

    d_j(i)

be its density.

Observation i is identified as a candidate local
density maximum when:

    d_j(i)
    ≥
    max{
        d_j(n):
        n ∈ N_5(i)
    }

where N_5(i) denotes the five morphology nearest
neighbors.

Thus a candidate mode is a local density maximum
relative to its 5-NN neighborhood.

No number of modes is specified.

---

## 11. DENSITY-ASCENT BASIN CONSTRUCTION

For each observational scale, every observation is
assigned to a density-ascent basin.

Starting from observation i:

    current = i

The algorithm examines the five nearest morphology
neighbors of the current observation.

The neighbor with the greatest density is selected.

A move occurs only when:

    density(neighbor)
    >
    density(current)

If a strictly denser neighbor exists:

    current → denser neighbor

The process continues iteratively.

If no neighboring observation has strictly greater
density:

    current = local density maximum

and the starting observation is assigned to that
terminal maximum.

Therefore:

    observation
        ↓
    higher-density neighbor
        ↓
    higher-density neighbor
        ↓
    ...
        ↓
    local density maximum

This produces the density-ascent basin assignment.

---

## 12. NO PREDEFINED MODE COUNT

The number of basins is an emergent property of the
density landscape.

The algorithm does not specify:

    K = number of morphology states

before analysis.

Observed basin counts were:

    scale 4.707252 → 7
    scale 5.416895 → 6
    scale 6.248407 → 5
    scale 7.596034 → 7
    scale 10.640832 → 7
    scale 16.568532 → 8

These are descriptive outputs of the density-ascent
procedure.

They are NOT interpreted automatically as morphology
categories.

---

## 13. BASIN DENSITY CONTRAST

For each basin, density contrast is characterized using:

    peak density
    median basin density
    lower-quartile basin density

The peak-to-median ratio is:

    peak_density /
    median_basin_density

This provides a quantitative diagnostic of whether
basins contain a meaningful density maximum rather than
merely reflecting nearly uniform density.

---

## 14. CROSS-SCALE BASIN STABILITY

Adjacent density scales are compared using:

    Adjusted Rand Index (ARI)

For scales:

    s_j
    s_(j+1)

the basin assignments are compared without assuming
that basin IDs themselves correspond.

The analysis therefore measures agreement in the
partition structure rather than numerical identity of
basin labels.

---

## 15. OBSERVATION-LEVEL BASIN PERSISTENCE

For each observation, basin membership is tracked across
adjacent scales.

An observation is considered continuously basin-stable
when its basin identity remains unchanged across all
adjacent scales.

This provides an observation-level measure of persistence.

However, basin IDs themselves are implementation labels
and are not treated as semantic identities.

---

## 16. MODE PERSISTENCE ANALYSIS

Candidate local maxima are also tracked directly.

For adjacent scales:

    s_j → s_(j+1)

candidate modes at scale j are compared with candidate
modes at scale j+1.

For every mode at scale j:

    • calculate morphology-space distance to every mode
      at scale j+1

    • identify the nearest mode

    • retain the match when the distance is ≤ the
      next empirical scale:

        distance ≤ s_(j+1)

Thus the matching threshold is itself derived from the
empirical morphology scale ladder.

No arbitrary matching distance is introduced.

---

## 17. MODE BIRTH / PERSISTENCE / MERGING

The multiscale analysis permits three qualitative
outcomes:

### Persistent modes

Density maxima remain identifiable across multiple
observational scales.

This supports recurring density organization.

### Mode disappearance / birth

Density maxima appear or disappear rapidly as scale
changes.

This suggests finer-scale density organization or
local density fluctuations.

### Mode merging

Several finer-scale maxima become represented by a
broader density structure at larger bandwidth.

This is consistent with multiscale organization in which
fine morphology density structure becomes progressively
coarser.

These are geometric interpretations, not semantic
morphology labels.

---

## 18. EXACT BASIN REPRODUCTION

The notebook contains an explicit basin-recovery procedure.

It reconstructs the same:

    10-NN graph
    density-ascent rule
    six-scale density representation
    basin assignments

and verifies the previously locked basin counts:

    [7, 6, 5, 7, 7, 8]

It additionally verifies adjacent-scale ARI values.

Therefore the basin structure is reproducible from the
frozen analysis specification.

---

## 19. CANONICAL BASIN MATRIX

All six scale-specific basin assignments are retained.

The resulting matrix is:

    density_basin_labels

with shape:

    (2300, 6)

Column j corresponds to empirical scale:

    scale_ladder[j]

No single observational scale is selected as the
canonical morphology-state scale.

---

## 20. DISCOVERY / VALIDATION SEPARATION

Density basins are discovered exclusively from:

    X_intrinsic
    density_matrix
    empirical morphology neighborhoods

They do NOT use:

    category labels
    replication labels
    target sketches
    semantic labels

Subsequent validation analyses examine whether the
discovered organization is reproducible.

---

## 21. MODEL-INDEPENDENCE LOCK

The multiscale density/basin analysis does NOT use:

    GMM
    KMeans
    hierarchical clustering
    CNN
    neural networks

The density landscape is derived directly from the
empirical morphology geometry.

---

## 22. CLAIM BOUNDARY

This analysis can establish:

✓ empirically defined morphology observational scales

✓ multiscale density landscapes

✓ local density maxima

✓ density-ascent basins

✓ recurring / changing density organization

✓ cross-scale basin stability

✓ density-mode persistence

It does NOT by itself establish:

✗ semantic morphology categories

✗ morphology primitives

✗ morphology grammar

✗ an exact number of morphology states

✗ an exact manifold dimension

✗ causal morphology structure

---

## 23. FINAL ANALYTICAL ROLE

M04 provides the transition from:

    continuous morphology geometry

to:

    recurring density organization.

The logical sequence is:

    continuous morphology space
            ↓
    empirical neighborhood scale
            ↓
    multiscale density landscape
            ↓
    local density maxima
            ↓
    density-ascent basins
            ↓
    cross-scale persistence
            ↓
    quantitative regional organization

This establishes density organization as an empirical
property of the morphology geometry before any semantic
interpretation is attempted.

---

## STATUS

M04 = 🟢 CAST-IRON LOCKED
