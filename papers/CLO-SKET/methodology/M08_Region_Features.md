# M08 — Region–Feature Profile Consistency

## Evidence class

B. Density Organization → Quantitative Regional Characterization

---

## STATUS

🟢 CAST-IRON LOCKED

This module characterizes the quantitative morphology
profiles associated with independently discovered density
regions.

The purpose is to determine whether density regions differ
reproducibly in measurable morphology properties.

The analysis does not assign semantic meanings to regions
or features.

---

# 1. INPUT

Canonical morphology feature space:

    X_source ∈ R^(2300 × 135)

Density-basin assignments:

    B ∈ R^(2300 × S)

where S represents the six independently derived
observational scales.

The density assignments are inherited directly from M06.

The canonical 135-D feature representation is inherited
directly from M02.

Neither is modified in this module.

---

# 2. SCIENTIFIC QUESTION

The analysis asks:

    Do independently discovered density regions possess
    reproducibly different quantitative morphology
    profiles?

This is a feature-profile question.

It is distinct from asking whether regions are globally
compact in morphology space.

Therefore:

    M07
        tests regional geometric coherence

    M08
        tests regional quantitative feature profiles

---

# 3. PROFILE REPRESENTATION

For each density region, a morphology feature profile is
constructed from the canonical 135-D representation.

The profile contains quantitative summaries of:

    • horizontal occupancy
    • vertical occupancy
    • centroid geometry
    • bounding-box geometry
    • aspect ratio
    • symmetry
    • foreground fraction

No semantic feature names are introduced beyond the
canonical M02 feature namespace.

---

# 4. FEATURE PROFILE EXTRACTION

For each density basin b:

    X_b

denotes the subset of the canonical 135-D morphology
matrix belonging to that basin.

A regional feature profile summarizes the distribution
of each canonical morphology feature within X_b.

The profile is therefore a quantitative description of
the morphology measurements associated with that region.

---

# 5. REGION PROFILE DISTANCE

Pairs of regional profiles are compared using their
quantitative feature-profile distances.

This produces a profile-distance structure describing
how different the discovered regions are in the canonical
morphology feature space.

The analysis does not assume that any region is a semantic
category.

---

# 6. WITHIN-SCALE PROFILE SEPARATION

For each observational scale, profile separation is
evaluated using the regional feature profiles discovered
at that scale.

A silhouette-based measure is used to characterize the
separation of regional profiles.

The silhouette value is interpreted descriptively:

    positive value
        →
    stronger separation of regional profiles

    value near zero
        →
    substantial overlap between regional profiles

    negative value
        →
    regional profiles are not cleanly separated under
    the tested profile-distance representation

The result is not interpreted as evidence for semantic
categories.

---

# 7. OBSERVED PROFILE SEPARATION

The observed silhouette values are:

    scale = 4.707252
        silhouette = -0.191627

    scale = 5.416895
        silhouette = -0.183667

    scale = 6.248407
        silhouette = -0.131744

    scale = 7.596034
        silhouette = -0.187342

    scale = 10.640832
        silhouette = -0.204588

    scale = 16.568532
        silhouette = -0.216238

These values indicate that regional feature profiles are
not strongly separated as compact profile clusters under
the tested silhouette formulation.

This result is retained explicitly.

---

# 8. BETWEEN / WITHIN PROFILE CONTRAST

For each scale, regional profile distances are summarized
by:

    between-region profile distance

and:

    within-region profile distance

The observed ratios are:

    scale = 4.707252
        ratio = 0.562107

    scale = 5.416895
        ratio = 0.556002

    scale = 6.248407
        ratio = 0.550778

    scale = 7.596034
        ratio = 0.550312

    scale = 10.640832
        ratio = 0.549580

    scale = 16.568532
        ratio = 0.568106

The ratio is retained as a descriptive measure of
regional profile contrast.

It is not interpreted independently of the underlying
profile-distance definition.

---

# 9. FEATURE-LEVEL REGIONAL DISCRIMINATION

For each canonical morphology feature, the analysis
quantifies how strongly its regional distributions differ.

The strongest observed regional discriminators include:

    bbox_width
    aspect_ratio
    centroid_x

along with multiple horizontal and vertical occupancy
features.

The global descriptor block shows particularly strong
regional discrimination.

Observed examples include:

    bbox_width
    aspect_ratio
    centroid_x
    symmetry
    foreground_fraction

and spatial occupancy measurements from both occupancy
families.

These are quantitative regional associations.

They are NOT declared semantic primitives.

---

# 10. FEATURE-BLOCK CONTRIBUTION

Regional feature discrimination is summarized by feature
block:

    global_descriptor
    horizontal_occupancy
    vertical_occupancy

Observed mean discrimination:

    global_descriptor
        ≈ 0.518

    horizontal_occupancy
        ≈ 0.313

    vertical_occupancy
        ≈ 0.264

The corresponding median values are:

    global_descriptor
        ≈ 0.442

    horizontal_occupancy
        ≈ 0.340

    vertical_occupancy
        ≈ 0.291

These results indicate that global morphology descriptors
contribute strongly to quantitative differences among the
discovered regional profiles.

They do not imply that the descriptors represent semantic
morphology primitives.

---

# 11. CROSS-SCALE FEATURE-PROFILE STABILITY

Regional feature-profile structure is compared across
independently derived density scales.

Basin IDs are not matched directly between scales.

Instead, quantitative feature-profile structure is compared.

Observed adjacent-scale profile correlations include:

    4.707252 → 5.416895
        rho = 0.987665

    5.416895 → 6.248407
        rho = 0.901663

    6.248407 → 7.596034
        rho = 0.919744

    7.596034 → 10.640832
        rho = 0.970510

    10.640832 → 16.568532
        rho = 0.964808

These values indicate strong reproducibility of the
quantitative feature-profile structure across adjacent
observational scales.

---

# 12. INTERPRETATION

The results support the following limited conclusion:

    independently discovered density regions are
    associated with reproducible quantitative
    morphology-profile differences.

However, the negative silhouette values indicate that
these profiles should NOT be described as cleanly separated
compact feature-space clusters.

Therefore the evidence is better characterized as:

    reproducible quantitative regional organization

rather than:

    discrete morphology categories.

---

# 13. RELATION TO M07

M07 asks:

    Are observations within a density region
    locally morphologically coherent?

M08 asks:

    Do the regions possess different measurable
    morphology profiles?

These are complementary questions.

The evidence chain is:

    M06
        density regions discovered

        ↓

    M07
        local regional coherence tested

        ↓

    M08
        quantitative regional profiles characterized

No semantic interpretation is required for either test.

---

# 14. DISCOVERY / VALIDATION SEPARATION

Density regions were discovered in M06 using morphology
geometry alone.

M08 does not use:

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

The regional feature profiles are measured only after
the density regions have been independently derived.

---

# 15. CLAIM BOUNDARY

M08 establishes:

    ✓ quantitative feature profiles for density regions

    ✓ measurable regional feature differences

    ✓ feature-level regional discrimination

    ✓ feature-block contribution

    ✓ strong cross-scale feature-profile reproducibility

M08 does NOT establish:

    ✗ morphology categories

    ✗ semantic morphology states

    ✗ semantic primitives

    ✗ morphology grammar

    ✗ cleanly separated feature-space clusters

    ✗ causal morphology structure

---

# 16. IMPORTANT NEGATIVE EVIDENCE

The negative silhouette values must be retained.

They indicate that regional feature profiles do not form
strongly separated compact clusters under the tested
profile representation.

Therefore the correct interpretation is NOT:

    "The density regions are discrete morphology classes."

Instead:

    "The independently discovered density regions exhibit
     reproducible quantitative differences in morphology
     profiles, while their profiles remain substantially
     overlapping."

This distinction prevents density organization from being
overinterpreted as categorical structure.

---

# 17. FINAL M08 LOCK

Input:

    X_source = 2300 × 135

    +
    
    frozen M06 basin assignments

Primary evidence:

    regional feature-profile differences

Secondary evidence:

    feature-level discrimination
    feature-block contribution
    cross-scale feature-profile stability

Observed:

    strong cross-scale profile reproducibility

    but negative silhouette values

Interpretation:

    reproducible quantitative regional organization
    without evidence for clean discrete profile clusters.

---

# FINAL M08 STATUS

🟢 CANONICAL 135-D FEATURE SPACE FROZEN

🟢 M06 BASIN ASSIGNMENTS FROZEN

🟢 REGIONAL FEATURE PROFILES EXTRACTED

🟢 FEATURE-LEVEL DISCRIMINATION TESTED

🟢 FEATURE-BLOCK CONTRIBUTION TESTED

🟢 CROSS-SCALE PROFILE STABILITY TESTED

🟢 NEGATIVE SILHOUETTE RESULT PRESERVED

🟢 NO SEMANTIC LABELS

🟢 NO CATEGORY LABELS

🟢 NO TARGET DATA

🟢 NO KMEANS / GMM / HIERARCHY

🟢 NO CNN / NN

🔒 M08 = CAST-IRON LOCKED