# M09 — Region–Feature Profile Permutation Null

## Evidence class

B. Density Organization → Quantitative Regional Validation

---

## STATUS

🟢 CAST-IRON LOCKED

This module tests whether the quantitative morphology
differences associated with independently discovered
density regions exceed a size-matched permutation null.

The purpose is to determine whether regional feature
discrimination reflects a relationship between morphology
and density-region membership rather than arbitrary
partitioning of observations.

No semantic interpretation is introduced.

---

# 1. INPUT

Canonical morphology feature space:

    X_source ∈ R^(2300 × 135)

Frozen density-basin assignments:

    B ∈ R^(2300 × S)

where S represents the six observational density scales.

The canonical feature representation is inherited from M02.

The density-basin assignments are inherited from M06.

Neither is modified during the null analysis.

---

# 2. SCIENTIFIC QUESTION

M08 established that independently discovered density
regions possess measurable differences in their canonical
morphology feature profiles.

M09 asks:

    Are those observed regional differences stronger than
    expected if observations were assigned arbitrarily to
    regions having exactly the same sizes?

This is a null-model test of regional feature association.

---

# 3. NULL DESIGN

For each observational scale:

    observed basin sizes are preserved exactly.

Observation-to-basin membership is then randomly permuted.

Therefore the permutation null preserves:

    • number of regions
    • region-size distribution
    • overall morphology-feature distributions
    • number of observations

while destroying:

    • the observed relationship between morphology
      and density-basin membership

The null therefore tests whether the observed regional
feature discrimination is greater than expected from
partition size alone.

---

# 4. OBSERVED STATISTIC

For each scale, feature-level regional discrimination
is calculated using the same procedure defined in M08.

The primary summary statistic is:

    mean feature discrimination

Additional summaries include:

    median feature discrimination
    maximum feature discrimination

The exact statistic is held constant between:

    observed data

and:

    permutation null replicates.

No statistic is selected after inspecting the null results.

---

# 5. PERMUTATION PROCEDURE

For each density scale:

    1. retain the observed basin-size distribution

    2. randomly permute observation membership

    3. preserve the number of observations in every basin

    4. recompute regional feature discrimination

    5. record the resulting null statistic

    6. repeat across permutation replicates

The same procedure is independently applied at all six
observational scales.

---

# 6. OBSERVED REGIONAL DISCRIMINATION

Observed mean feature discrimination:

    scale = 4.707252
        0.309747

    scale = 5.416895
        0.310943

    scale = 6.248407
        0.303514

    scale = 7.596034
        0.301466

    scale = 10.640832
        0.300478

    scale = 16.568532
        0.298850

These values provide the observed regional feature
discrimination against which the permutation null is
compared.

---

# 7. PERMUTATION NULL RESULTS

The observed statistics and corresponding null
distributions are:

    scale = 4.707252
        observed = 0.309747
        null mean = 0.164513
        p = 0.004975
        z = 6.138

    scale = 5.416895
        observed = 0.310943
        null mean = 0.158761
        p = 0.009950
        z = 4.703

    scale = 6.248407
        observed = 0.303514
        null mean = 0.116115
        p = 0.004975
        z = 8.615

    scale = 7.596034
        observed = 0.301466
        null mean = 0.197008
        p = 0.054726
        z = 2.232

    scale = 10.640832
        observed = 0.300478
        null mean = 0.243837
        p = 0.134328
        z = 1.182

    scale = 16.568532
        observed = 0.298850
        null mean = 0.254862
        p = 0.169154
        z = 0.735

---

# 8. SCALE-DEPENDENT NULL RESULT

The observed regional discrimination exceeds the
permutation null most clearly at the lower and
intermediate observational scales.

At the first three scales:

    p < 0.01

while at the larger scales:

    p > 0.05

Therefore the evidence for regional feature association
is not equally strong across the complete scale ladder.

This scale dependence is retained.

The analysis does NOT select the strongest scale as the
canonical morphology scale.

---

# 9. INTERPRETATION

The null comparison supports the following limited
conclusion:

    At several observational scales, the quantitative
    morphology differences between independently discovered
    density regions are greater than expected from arbitrary
    size-matched regional assignment.

This supports a non-random relationship between density
organization and measurable morphology properties.

However:

    the evidence weakens at larger observational scales.

Therefore the correct interpretation is:

    regional feature association is supported at
    multiple scales, but is not uniformly significant
    across the entire scale ladder.

---

# 10. FEATURE-LEVEL NULL ANALYSIS

The permutation analysis is additionally performed at
the individual-feature level.

A feature is considered to show consistent regional
signal when its observed discrimination repeatedly
exceeds the corresponding permutation null across
multiple observational scales.

The strongest consistently associated features include:

    bbox_width
    aspect_ratio
    centroid_x
    horizontal_occupancy_61
    vertical_occupancy_04
    symmetry
    horizontal_occupancy_22
    horizontal_occupancy_35
    vertical_occupancy_03
    foreground_fraction

These are quantitative morphology measurements.

They are not assigned semantic meanings.

---

# 11. CONSISTENT FEATURE SIGNAL

The strongest feature-level null results include:

    bbox_width
        median z ≈ 6.96
        significant across all six scales

    aspect_ratio
        median z ≈ 4.61
        significant across five scales

    centroid_x
        median z ≈ 4.45
        significant across all six scales

    horizontal_occupancy_61
        median z ≈ 3.45
        significant across all six scales

    vertical_occupancy_04
        median z ≈ 3.34
        significant across all six scales

Additional features show recurring but less uniform
regional association.

These results characterize measurable feature-level
regional structure.

They do not establish semantic primitives.

---

# 12. FEATURE-BLOCK NULL STRUCTURE

The permutation results show different levels of regional
signal across the three canonical feature blocks:

    global_descriptor
    horizontal_occupancy
    vertical_occupancy

Observed mean median-z values are approximately:

    global_descriptor
        3.91

    horizontal_occupancy
        1.31

    vertical_occupancy
        0.98

This indicates that global morphology descriptors contain
particularly strong and reproducible regional signal under
the tested null framework.

The result does not imply that occupancy features are
uninformative.

Rather, it indicates that regional discrimination is
distributed unevenly across the canonical feature blocks.

---

# 13. RELATION TO M08

M08 established:

    reproducible quantitative regional feature profiles.

M09 asks:

    whether those differences exceed a size-matched
    arbitrary-partition null.

Therefore:

    M08
        ↓
    regional feature differences observed

    M09
        ↓
    non-random regional feature association tested

This strengthens the evidence chain without changing
the discovered basin assignments.

---

# 14. DISCOVERY / NULL SEPARATION

The density regions were discovered independently
from morphology geometry in M06.

The permutation procedure does not rediscover or
optimize density regions.

Instead, it takes the observed basin-size structure
as fixed and destroys only the observation-to-region
relationship.

Thus:

    discovery
        =
    morphology geometry

while:

    null test
        =
    size-matched random regional membership

This separation is maintained deliberately.

---

# 15. MULTIPLE-SCALE INTERPRETATION

The six scales are treated as a family of observational
scales rather than six independent claims of universal
significance.

The observed pattern shows:

    strong null separation
        at lower/intermediate scales

and:

    weaker null separation
        at larger scales.

This is interpreted as evidence that quantitative
regional morphology organization is most clearly
detectable at some portions of the density landscape's
scale range.

No scale is declared optimal.

---

# 16. CLAIM BOUNDARY

M09 establishes:

    ✓ a size-matched permutation null

    ✓ preservation of basin-size distributions

    ✓ destruction of morphology-to-basin membership

    ✓ observed-vs-null regional feature discrimination

    ✓ evidence for non-random regional feature association
      at multiple scales

    ✓ scale dependence of regional feature association

    ✓ recurring feature-level regional signals

M09 does NOT establish:

    ✗ morphology categories

    ✗ semantic morphology states

    ✗ semantic primitives

    ✗ morphology grammar

    ✗ causal relationships

    ✗ a preferred density scale

    ✗ a preferred number of morphology modes

---

# 17. IMPORTANT NEGATIVE / QUALIFYING EVIDENCE

The larger observational scales do not show strong
permutation-null separation under the reported test.

Therefore the paper must not summarize M09 as:

    "regional feature profiles are significant
     at all scales."

The defensible statement is:

    "Regional feature discrimination exceeded a
     size-matched permutation null at several
     lower and intermediate observational scales,
     with weaker evidence at larger scales."

This scale dependence is retained as part of the
evidence rather than treated as an inconvenience.

---

# 18. FINAL M09 LOCK

Input:

    canonical 2300 × 135 morphology

    +
    
    frozen M06 basin assignments

Null:

    exact basin-size-preserving membership permutation

Primary statistic:

    mean regional feature discrimination

Secondary evidence:

    feature-level z scores
    scale recurrence
    feature-block contribution

Observed pattern:

    strong null separation at several scales

    weaker separation at larger scales

Interpretation:

    density-region membership has a non-random
    quantitative relationship with morphology
    features at multiple observational scales.

NOT:

    semantic morphology categories.

---

# FINAL M09 STATUS

🟢 CANONICAL FEATURE SPACE FROZEN

🟢 BASIN ASSIGNMENTS FROZEN

🟢 BASIN SIZES PRESERVED

🟢 SIZE-MATCHED PERMUTATION NULL IMPLEMENTED

🟢 OBSERVED VS NULL DISCRIMINATION TESTED

🟢 FEATURE-LEVEL SIGNAL TESTED

🟢 FEATURE-BLOCK SIGNAL TESTED

🟢 SCALE DEPENDENCE RETAINED

🟢 NO SEMANTIC INTERPRETATION

🟢 NO CATEGORY LABELS

🟢 NO TARGET DATA

🟢 NO KMEANS / GMM / HIERARCHY

🟢 NO CNN / NN

🔒 M09 = CAST-IRON LOCKED