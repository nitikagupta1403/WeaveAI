# M10 — Cross-Scale Region–Feature Generalization

## Evidence class

B. Density Organization → Cross-Scale Generalization

---

## STATUS

🟢 CAST-IRON LOCKED

This module tests whether the quantitative morphology
organization associated with independently discovered
density regions remains recognizable when the observational
density scale changes.

The analysis does not assume that basin identities persist
across scales.

Instead, it compares quantitative regional profile
structure across independently derived density landscapes.

---

# 1. INPUT

Canonical morphology feature space:

    X_source ∈ R^(2300 × 135)

Frozen density-basin assignments:

    B ∈ R^(2300 × S)

where S represents the six observational density scales.

The canonical morphology representation is inherited from M02.

The density landscapes and basin assignments are inherited
from M06.

No representation is refitted during this analysis.

---

# 2. SCIENTIFIC QUESTION

The analysis asks:

    Does quantitative morphology organization associated
    with density regions remain recognizable when the
    observational density scale changes?

This is a cross-scale generalization question.

It does NOT ask:

    Are the same basin IDs recovered at every scale?

---

# 3. BASIN IDENTITY LOCK

Basin identifiers are local to each density landscape.

Therefore:

    basin 307 at scale A

is NOT assumed to equal:

    basin 307 at scale B.

No direct basin-ID matching is performed.

This prevents numerical basin identifiers from being
mistaken for persistent biological or semantic identities.

---

# 4. REGIONAL PROFILE EXTRACTION

At each observational scale, a quantitative morphology
profile is extracted for every independently discovered
density region.

Each profile is based on the canonical 135-D morphology
feature representation.

The resulting profile collection contains:

    scale 4.707252
        7 regions

    scale 5.416895
        6 regions

    scale 6.248407
        5 regions

    scale 7.596034
        7 regions

    scale 10.640832
        7 regions

    scale 16.568532
        8 regions

Total regional profiles:

    40

---

# 5. PROFILE-DISTANCE STRUCTURE

For each density scale, pairwise distances among regional
morphology profiles are calculated.

The resulting profile-distance structure describes the
quantitative morphology organization of the regions at that
observational scale.

The analysis compares this structure across scales without
requiring one-to-one basin correspondence.

---

# 6. OBSERVED PROFILE DISTANCES

The regional profile-distance distributions are:

    scale = 4.707252
        median = 5.027430
        mean   = 5.363601

    scale = 5.416895
        median = 4.953348
        mean   = 5.304154

    scale = 6.248407
        median = 5.122721
        mean   = 5.270094

    scale = 7.596034
        median = 5.313292
        mean   = 5.251579

    scale = 10.640832
        median = 5.215745
        mean   = 5.323307

    scale = 16.568532
        median = 5.670407
        mean   = 5.493323

The profile-distance structure remains quantitatively
similar across the observational scale ladder.

---

# 7. CROSS-SCALE FEATURE-PROFILE AGREEMENT

Quantitative regional feature-profile structure is compared
between scales using feature-profile rank correlation.

For each pair of observational scales:

    feature-profile correlation

is calculated across the canonical morphology features.

This evaluates whether the relative quantitative
organization of morphology features remains similar as the
density scale changes.

---

# 8. OBSERVED CROSS-SCALE AGREEMENT

The observed mean feature-profile correlations are:

    4.707252 → 5.416895
        rho = 0.999893

    4.707252 → 6.248407
        rho = 0.999812

    4.707252 → 7.596034
        rho = 0.999867

    4.707252 → 10.640832
        rho = 0.999668

    4.707252 → 16.568532
        rho = 0.999331

    5.416895 → 6.248407
        rho = 1.000000

    5.416895 → 7.596034
        rho = 0.999893

    5.416895 → 10.640832
        rho = 0.999360

    5.416895 → 16.568532
        rho = 0.998816

    6.248407 → 7.596034
        rho = 0.999812

    6.248407 → 10.640832
        rho = 0.998875

    6.248407 → 16.568532
        rho = 0.997900

    7.596034 → 10.640832
        rho = 0.999466

    7.596034 → 16.568532
        rho = 0.999331

    10.640832 → 16.568532
        rho = 0.999389

The cross-scale feature-profile agreement is therefore
extremely high.

---

# 9. FEATURE-LEVEL CROSS-SCALE CONSISTENCY

Feature-level profile consistency is additionally examined
for individual canonical morphology features.

The analysis asks whether the regional organization of a
given feature remains quantitatively consistent across
independently derived density scales.

The observed results show very high consistency across
the canonical feature representation.

For the reported feature subset:

    median cross-scale rho = 1.0

and:

    mean cross-scale rho = 1.0

for the displayed features.

---

# 10. FEATURE-BLOCK CONSISTENCY

Cross-scale consistency is summarized separately for:

    global_descriptor
    horizontal_occupancy
    vertical_occupancy

Observed results:

    global_descriptor
        mean = 1.000000
        median = 1.000000
        minimum = 1.000000
        maximum = 1.000000

    horizontal_occupancy
        mean = 1.000000
        median = 1.000000
        minimum = 1.000000
        maximum = 1.000000

    vertical_occupancy
        mean = 0.999074
        median = 1.000000
        minimum = 0.985611
        maximum = 1.000000

The quantitative regional feature structure is therefore
highly stable across observational scales.

---

# 11. INTERPRETATION

The results support the following limited conclusion:

    Quantitative morphology-profile organization associated
    with independently discovered density regions remains
    highly reproducible across the tested observational
    scales.

This is evidence for persistent quantitative morphology
organization underlying the multiscale density landscape.

It does NOT mean that the exact same density regions are
recovered at every scale.

The number of regions changes across scales:

    5–8 regions

and basin identities are not matched directly.

The persistent quantity is the:

    quantitative profile structure

rather than:

    basin identity.

---

# 12. RELATION TO M09

M09 asks:

    Are observed regional feature differences stronger
    than expected from arbitrary size-matched regional
    assignments?

M10 asks:

    Does the resulting quantitative regional organization
    remain recognizable across observational scales?

Therefore:

    M09
        ↓
    non-random regional feature association

    M10
        ↓
    cross-scale generalization of quantitative
    regional organization

Together these provide complementary evidence.

---

# 13. RELATION TO M06

M06 discovers density organization independently at each
observational scale.

M10 does not modify that discovery.

Instead it asks whether the quantitative morphology
organization associated with those independently discovered
regions is reproducible across scales.

The scale ladder therefore functions as a robustness
framework rather than as a model-selection procedure.

---

# 14. SCALE IS NOT OPTIMIZED

No density scale is selected because it produces the
strongest cross-scale agreement.

All six observational scales are retained.

The result is therefore a characterization of the
multiscale density landscape.

This prevents circular selection of a preferred scale
based on downstream morphology-profile behavior.

---

# 15. DISCOVERY / GENERALIZATION SEPARATION

Density regions were discovered using morphology geometry
only.

M10 uses those frozen assignments to evaluate quantitative
profile generalization.

No external labels are introduced.

The analysis does not use:

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

---

# 16. CLAIM BOUNDARY

M10 establishes:

    ✓ quantitative regional profiles can be extracted
      independently at multiple density scales

    ✓ regional profile-distance distributions remain
      quantitatively similar

    ✓ feature-profile organization shows extremely high
      cross-scale agreement

    ✓ feature-level regional organization is highly stable

    ✓ feature-block organization is highly stable

    ✓ quantitative regional morphology organization
      generalizes across the tested density scales

M10 does NOT establish:

    ✗ persistent basin identities

    ✗ morphology categories

    ✗ semantic morphology states

    ✗ semantic primitives

    ✗ morphology grammar

    ✗ a preferred density scale

    ✗ a preferred number of morphology modes

    ✗ causal morphology structure

---

# 17. IMPORTANT INTERPRETATION BOUNDARY

The extremely high cross-scale correlations should not be
described as evidence that the individual observations are
assigned to identical regions at every scale.

Instead, the defensible claim is:

    independently derived regional morphology profiles
    exhibit highly reproducible quantitative organization
    across observational density scales.

The unit of generalization is therefore:

    quantitative regional profile structure

rather than:

    basin identity.

---

# 18. FINAL M10 LOCK

Input:

    canonical 2300 × 135 morphology

    +

    frozen multiscale density-basin assignments

Regional profiles:

    40 total profiles

Regional counts:

    7
    6
    5
    7
    7
    8

Primary evidence:

    cross-scale regional feature-profile agreement

Observed agreement:

    approximately 0.998–1.000

Feature-block agreement:

    global descriptors ≈ 1.000

    horizontal occupancy ≈ 1.000

    vertical occupancy ≈ 0.999

Interpretation:

    quantitative morphology-region organization
    generalizes strongly across the tested density scales.

NOT:

    persistent semantic categories.

---

# FINAL M10 STATUS

🟢 CANONICAL 135-D FEATURE SPACE FROZEN

🟢 M06 BASIN ASSIGNMENTS FROZEN

🟢 BASIN IDS NOT MATCHED ACROSS SCALES

🟢 REGIONAL PROFILES EXTRACTED INDEPENDENTLY

🟢 CROSS-SCALE PROFILE DISTANCE STRUCTURE TESTED

🟢 CROSS-SCALE FEATURE AGREEMENT TESTED

🟢 FEATURE-LEVEL CONSISTENCY TESTED

🟢 FEATURE-BLOCK CONSISTENCY TESTED

🟢 ALL DENSITY SCALES RETAINED

🟢 NO SCALE OPTIMIZATION

🟢 NO SEMANTIC INTERPRETATION

🟢 NO CATEGORY LABELS

🟢 NO TARGET DATA

🟢 NO KMEANS / GMM / HIERARCHY

🟢 NO CNN / NN

🔒 M10 = CAST-IRON LOCKED