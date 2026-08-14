# M07 — Within-Region Morphology Coherence

## Evidence class

B. Density Organization → Regional Morphology Validation

---

## STATUS

🟢 CAST-IRON LOCKED

This module evaluates whether independently discovered
density-ascent regions correspond to internally coherent
morphology neighborhoods.

The density regions are inherited directly from M06.

No basin count is selected or modified in this module.

No semantic interpretation is introduced.

---

# 1. INPUT

Canonical morphology geometry:

    Z_source ∈ R^(2300 × 73)

Density-basin assignments:

    B ∈ R^(2300 × S)

where S is the number of observational density scales.

The six density scales are inherited unchanged from M06:

    4.707252
    5.416895
    6.248407
    7.596034
    10.640832
    16.568532

The basin assignments are frozen for this analysis.

---

# 2. SCIENTIFIC QUESTION

The analysis asks:

    Are observations belonging to the same
    independently discovered density region
    morphologically closer to one another than
    observations belonging to different regions?

This tests whether density organization corresponds
to measurable morphology coherence.

---

# 3. WITHIN-REGION DISTANCE

For each density basin at each scale, morphology distances
are calculated in the frozen 73-D intrinsic morphology space.

For basin b:

    W_b

denotes the set of observations assigned to that basin.

Within-region morphology distance is calculated from
pairwise distances among observations within W_b.

The resulting basin-level quantity is summarized as:

    internal_distance

representing the typical morphology separation of
observations within the region.

---

# 4. BETWEEN-REGION DISTANCE

For observations belonging to different density basins,
morphology distances are calculated in the same frozen
73-D geometry space.

The resulting quantity provides the corresponding
between-region morphology separation.

Within-region and between-region distances therefore
use the same coordinate system and distance definition.

---

# 5. WITHIN / BETWEEN RATIO

For each observational scale:

    within_mean_distance

and:

    between_mean_distance

are compared.

The ratio is defined as:

    within_between_ratio =
        within_mean_distance /
        between_mean_distance

Interpretation:

    ratio < 1

would indicate that within-region morphology distances
are smaller than between-region distances.

    ratio ≈ 1

would indicate weak separation between within-region
and between-region morphology distances.

    ratio > 1

indicates that the discovered regions are not strongly
separated according to this particular distance summary.

This ratio is therefore interpreted directly rather than
assuming that density regions must be geometrically compact.

---

# 6. LOCAL NEIGHBOR RETENTION

A secondary measure evaluates whether local morphology
neighbors tend to remain within the same density region.

For observation i, let:

    N_k(i)

represent its local morphology neighborhood.

Local same-region retention is:

    retention_i =
        fraction of local neighbors
        belonging to the same basin as i

The analysis summarizes this quantity within each density
scale and basin.

This measures local boundary coherence.

---

# 7. OBSERVED RESULTS

Across the six density scales, the observed mean
within/between ratios are:

    scale = 4.707252
        ratio = 1.070042

    scale = 5.416895
        ratio = 1.056973

    scale = 6.248407
        ratio = 1.043062

    scale = 7.596034
        ratio = 1.045968

    scale = 10.640832
        ratio = 1.039735

    scale = 16.568532
        ratio = 1.074519

The corresponding mean local-neighbor retention values are:

    0.755
    0.774
    0.804
    0.804
    0.843
    0.845

---

# 8. INTERPRETATION OF THE OBSERVED DISTANCES

The observed within/between ratios are close to 1 and
are consistently greater than 1 in the reported analysis.

Therefore the primary distance statistic does NOT support
a strong claim that density basins are compact morphology
clusters with substantially smaller within-region distances.

This negative or weak result is retained explicitly.

The analysis instead provides evidence that density regions
have substantial local neighborhood retention while not
showing strong global pairwise distance separation.

This distinction is important.

---

# 9. LOCAL COHERENCE

The local-neighbor retention increases across the
observational scales:

    approximately 0.755
        →
    approximately 0.845

This indicates that, at the tested scales, a substantial
fraction of local morphology neighbors remain within the
same density region.

The result supports local boundary coherence more strongly
than strong global within-region compactness.

---

# 10. BASIN-LEVEL HETEROGENEITY

The regional analysis retains basin-specific quantities
rather than reporting only a global average.

Observed basin sizes vary substantially.

Some large basins contain most observations, while several
small basins contain relatively few observations.

Therefore:

    basin-level morphology coherence

is not assumed to be uniform across all density regions.

Small regions are interpreted cautiously because their
distance and local-retention estimates can be less stable.

---

# 11. CROSS-SCALE ROLE

The same analysis is performed independently at all six
density scales.

The purpose is not to select the scale with the strongest
coherence.

Instead, the observed quantities are treated as a
multiscale characterization of regional morphology
organization.

A recurring pattern across scales is considered stronger
evidence than a result appearing at only one scale.

---

# 12. RELATION TO M06

M06 establishes:

    density regions exist as
    geometry-derived density-ascent basins.

M07 asks:

    whether those independently discovered regions
    correspond to coherent morphology neighborhoods.

Therefore:

    M06
        ↓
    density organization discovered

    M07
        ↓
    regional morphology coherence tested

The basin assignments themselves are not changed by M07.

---

# 13. DISCOVERY / VALIDATION SEPARATION

Density basins were discovered using morphology geometry
in M06.

M07 does not use:

    category labels
    replication labels
    target sketches
    semantic labels
    KMeans
    GMM
    hierarchical clustering
    supervised learning
    CNN
    neural networks

No basin is selected because it produces a desired
morphology-distance result.

---

# 14. CLAIM BOUNDARY

M07 establishes:

    ✓ quantitative within-region morphology distances

    ✓ quantitative between-region morphology distances

    ✓ within/between distance ratios

    ✓ local same-region neighbor retention

    ✓ basin-level heterogeneity

    ✓ multiscale regional coherence characterization

M07 does NOT establish:

    ✗ strong global geometric separation

    ✗ compact morphology clusters

    ✗ morphology categories

    ✗ semantic morphology states

    ✗ semantic primitives

    ✗ morphology grammar

    ✗ causal morphology structure

---

# 15. IMPORTANT NEGATIVE EVIDENCE

The primary within/between distance result should not
be converted into a stronger claim than the data support.

Observed:

    within / between > 1

at all six tested scales.

Therefore the evidence does not support:

    "density basins are strongly compact
     morphology clusters."

Instead, the more defensible conclusion is:

    density-derived regions exhibit substantial
    local same-region neighborhood retention,
    while global within-region morphology distances
    are not smaller than between-region distances
    under the tested distance summary.

This distinction is retained as part of the evidence chain.

---

# 16. FINAL M07 LOCK

Input:

    frozen 73-D morphology geometry
    +
    frozen M06 density-basin assignments

Primary evidence:

    within-region morphology distance
    versus
    between-region morphology distance

Secondary evidence:

    local same-region neighbor retention

Observed:

    within/between ratios ≈ 1.04–1.07

    local retention ≈ 0.755–0.845

Interpretation:

    local regional coherence is present,
    but strong global compactness is not established.

---

# FINAL M07 STATUS

🟢 M06 BASIN ASSIGNMENTS FROZEN

🟢 73-D MORPHOLOGY SPACE FROZEN

🟢 WITHIN-REGION DISTANCE TESTED

🟢 BETWEEN-REGION DISTANCE TESTED

🟢 LOCAL NEIGHBOR RETENTION TESTED

🟢 MULTISCALE ANALYSIS RETAINED

🟢 NEGATIVE / WEAK GLOBAL-SEPARATION RESULT PRESERVED

🟢 NO SEMANTIC INTERPRETATION

🟢 NO CATEGORY LABELS

🟢 NO TARGET DATA

🟢 NO KMEANS / GMM / HIERARCHY

🟢 NO CNN / NN

🔒 M07 = CAST-IRON LOCKED