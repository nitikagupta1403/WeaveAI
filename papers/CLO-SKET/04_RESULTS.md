# CLO-SKET — Results

## 1. Overview of the Results

The analysis was performed on 2,300 garment sketches using a frozen
135-dimensional quantitative morphology representation and an
independently derived 28-dimensional radial–angular representation.

The results address four sequential questions:

1. Does the morphology representation exhibit reproducible quantitative
   organization?
2. Is the radial–angular representation associated with morphology?
3. Does morphology recover independently measured radial–angular
   quantities at the sketch level?
4. Does radial–angular geometry provide complementary downstream
   information beyond morphology?

The final cross-branch analysis was performed only after exact
row-level provenance between the two representations had been verified.

---

# 2. Canonical Quantitative Morphology Representation

The canonical morphology representation contains 135 image-derived
features for each of the 2,300 sketches:

- 64 horizontal occupancy coordinates;
- 64 vertical occupancy coordinates; and
- 7 global geometric descriptors.

The resulting matrix has shape:

    2300 × 135

The canonical morphology artifact passed finite-value validation and
matched its stored SHA-256 fingerprint.

The representation was therefore frozen before the independent
radial–angular analysis.

---

# 3. Variance Structure of the Morphology Representation

After source-only standardization, principal component analysis was
used to characterize the variance structure of the morphology
representation.

The principal morphology analysis retained approximately 95% of
standardized morphology variance using 73 principal components.

This result is reported as a PCA variance-retention result.

It is not interpreted as proof of a mathematical intrinsic dimension
of 73.

The PCA representation was subsequently used for geometric analyses
of morphology organization.

---

# 4. Quantitative Organization of Morphology Space

The morphology representation exhibited structured organization across
multiple geometric analyses.

The analysis included:

- spectral structure;
- neighborhood organization;
- graph-geodesic relationships;
- transition structure;
- multiscale density organization; and
- permutation-based locality analyses.

These analyses consistently indicated that the morphology
representation was not organized as an arbitrary collection of
independent observations.

The morphology graph was connected, and Euclidean and graph-based
neighborhood orderings showed substantial agreement.

Multiscale density analysis identified density-defined regions with
different quantitative morphology profiles.

These regions were not interpreted as compact morphology categories.

Within-region morphology dispersion remained substantial.

---

# 5. Density-Defined Regional Organization

The multiscale density analysis identified regions of differing local
morphological density.

Same-region nearest-neighbor retention was substantially greater than
expected under a region-size-preserving permutation null.

This demonstrates that density-region membership was non-randomly
associated with local morphology geometry under the specified null.

Cross-scale permutation analysis further showed that the
feature-level regional discrimination profiles were substantially
more correlated across density scales than expected under
independently permuted, size-preserving region assignments.

These results support reproducible density-associated organization.

They do not imply that the density regions represent discrete
morphological states.

---

# 6. Ordered Occupancy Structure

Feature-order permutation analysis showed reproducible local structure
in the ordered occupancy coordinates.

The null preserved each observation's occupancy values while disrupting
the original coordinate ordering.

The observed structure therefore cannot be attributed solely to the
marginal distribution of occupancy values.

This result provides additional evidence that the spatial ordering
of occupancy measurements contains reproducible quantitative
organization.

---

# 7. Independent Radial–Angular Representation

An independently derived radial–angular representation was constructed
for the same 2,300 sketches.

The compact representation contains 28 dimensions:

| Descriptor block | Dimensions |
|---|---:|
| F₂ radial | 9 |
| α₂ | 7 |
| observed circular | 3 |
| learned circular | 4 |
| relational | 5 |
| **Total** | **28** |

The radial–angular representation therefore provides a second
geometric description of the same sketch population.

The representation was not used to modify the frozen 135-dimensional
morphology matrix.

---

# 8. Cross-Branch Provenance

Before association analysis, row-level provenance was explicitly
verified.

The morphology-side and radial–angular image-reference arrays each
contained:

    2300 references

with:

    2300 unique references
    0 duplicate references
    0 empty references

The candidate morphology-side path array exactly matched the
radial–angular path ordering.

Therefore:

    morphology[i]

and

    radial-angular[i]

refer to the same sketch for every observation i.

This establishes the population and row-level alignment required for
subsequent cross-branch analyses.

---

# 9. Feature-Level Morphology ↔ Radial–Angular Association

Feature-wise Spearman association was evaluated between the 135
morphology coordinates and four radial–angular targets:

1. F₂ peak magnitude;
2. F₂ peak radius;
3. observed R₂ at the F₂ peak shell; and
4. axial angular recovery error.

Benjamini–Hochberg false-discovery-rate correction was applied
separately for each target.

## 9.1 F₂ Peak Magnitude

The strongest association was observed for:

    horizontal_occupancy_50

with:

    Spearman ρ = −0.5469

The next strongest associations were also concentrated in neighboring
horizontal occupancy coordinates.

The strongest global-descriptor association was:

    symmetry
    ρ = +0.4840

Overall:

    126 / 135 morphology features
    were FDR-significant.

Median absolute correlation:

    |ρ| median = 0.2173

Maximum absolute correlation:

    |ρ| max = 0.5469

---

## 9.2 F₂ Peak Radius

The strongest association was:

    horizontal_occupancy_45

with:

    Spearman ρ = +0.3537

Overall:

    93 / 135 morphology features
    were FDR-significant.

Median absolute correlation:

    |ρ| median = 0.0979

Maximum absolute correlation:

    |ρ| max = 0.3537

---

## 9.3 R₂ at the F₂ Peak

The strongest association was:

    horizontal_occupancy_44

with:

    Spearman ρ = +0.3944

Overall:

    106 / 135 morphology features
    were FDR-significant.

Median absolute correlation:

    |ρ| median = 0.1315

Maximum absolute correlation:

    |ρ| max = 0.3944

---

## 9.4 Axial Angular Error

The strongest association was:

    vertical_occupancy_32

with:

    Spearman ρ = −0.2171

Overall:

    90 / 135 morphology features
    were FDR-significant.

Median absolute correlation:

    |ρ| median = 0.0871

Maximum absolute correlation:

    |ρ| max = 0.2171

---

# 10. Cross-Validated Recovery of Radial–Angular Measurements

The next analysis tested whether radial–angular measurements could be
recovered from the frozen 135-dimensional morphology representation.

Five-fold shuffled cross-validation was used with random state 42.

The evaluation was strictly out-of-sample.

## 10.1 F₂ Peak Magnitude

Cross-validated performance:

    R² = 0.2961
    MAE = 0.01315
    RMSE = 0.01710
    Spearman ρ = 0.6415

---

## 10.2 F₂ Peak Radius

Cross-validated performance:

    R² = 0.0594
    MAE = 4.0152
    RMSE = 5.0096
    Spearman ρ = 0.3417

---

## 10.3 R₂ at the F₂ Peak

Cross-validated performance:

    R² = 0.2170
    MAE = 0.1258
    RMSE = 0.1599
    Spearman ρ = 0.5377

---

## 10.4 Axial Angular Error

Cross-validated performance:

    R² = 0.1979
    MAE = 20.1515
    RMSE = 26.4623
    Spearman ρ = 0.4400

---

## 10.5 Summary

| Target | CV R² | MAE | RMSE | Spearman ρ |
|---|---:|---:|---:|---:|
| F₂ peak magnitude | 0.2961 | 0.0131 | 0.0171 | 0.6415 |
| F₂ peak radius | 0.0594 | 4.0152 | 5.0096 | 0.3417 |
| R₂ at F₂ peak | 0.2170 | 0.1258 | 0.1599 | 0.5377 |
| Axial angular error | 0.1979 | 20.1515 | 26.4623 | 0.4400 |

These results show that morphology contains recoverable information
about several independently measured radial–angular quantities, with
the strongest recovery observed for F₂ peak magnitude.

---

# 11. Permutation-Validated Cross-Branch Correspondence

To determine whether the morphology ↔ radial–angular relationship
depends on actual sketch-level correspondence, radial–angular targets
were randomly permuted across observations.

The morphology representation remained fixed.

One hundred permutations were performed using random seed 2026.

## 11.1 F₂ Peak Magnitude

Observed:

    R² = 0.2961

Permutation null:

    mean R² = −0.0965
    95% interval = [−0.1284, −0.0702]
    empirical p = 0.0099
    observed percentile = 100%

---

## 11.2 F₂ Peak Radius

Observed:

    R² = 0.0594

Permutation null:

    mean R² = −0.0985
    95% interval = [−0.1324, −0.0699]
    empirical p = 0.0099
    observed percentile = 100%

---

## 11.3 R₂ at F₂ Peak

Observed:

    R² = 0.2170

Permutation null:

    mean R² = −0.0956
    95% interval = [−0.1244, −0.0666]
    empirical p = 0.0099
    observed percentile = 100%

---

## 11.4 Axial Angular Error

Observed:

    R² = 0.1979

Permutation null:

    mean R² = −0.0952
    95% interval = [−0.1309, −0.0622]
    empirical p = 0.0099
    observed percentile = 100%

---

## 11.5 Correspondence Summary

| Target | Observed R² | Null mean | Null 95% interval | Empirical p |
|---|---:|---:|---:|---:|
| F₂ peak magnitude | 0.2961 | −0.0965 | [−0.1284, −0.0702] | 0.0099 |
| F₂ peak radius | 0.0594 | −0.0985 | [−0.1324, −0.0699] | 0.0099 |
| R₂ at F₂ peak | 0.2170 | −0.0956 | [−0.1244, −0.0666] | 0.0099 |
| Axial angular error | 0.1979 | −0.0952 | [−0.1309, −0.0622] | 0.0099 |

For all four targets, the observed cross-validated performance
exceeded every permutation replicate.

Because only 100 permutations were used, the empirical p-value of
0.0099 corresponds to the minimum nonzero p-value under the +1
permutation correction.

---

# 12. Downstream Complementarity

The downstream discrimination analysis evaluated whether the
28-dimensional radial–angular representation provides information
beyond the frozen 135-dimensional morphology representation.

The baseline representation was:

    135-D morphology

The augmented representation was:

    135-D morphology
    +
    28-D radial-angular geometry.

The task involved 23 predefined categories.

## 12.1 Macro-F1

Morphology-only:

    0.341348

Morphology + radial-angular:

    0.412332

Observed improvement:

    Δ Macro-F1 = +0.070984

---

## 12.2 Balanced Accuracy

Morphology-only:

    0.342609

Morphology + radial-angular:

    0.415652

Observed improvement:

    Δ Balanced Accuracy = +0.073043

---

## 12.3 Complementarity Permutation Control

For the primary Macro-F1 metric:

    observed Δ = +0.070984
    null mean Δ = −0.020368
    null 95% interval =
        [−0.031142, −0.010537]

Empirical permutation p:

    0.009901

For balanced accuracy:

    observed Δ = +0.073043

with:

    empirical permutation p = 0.009901

The observed improvements therefore exceeded the corresponding
row-permutation null distributions.

---

# 13. Dimension-Matched Control

The downstream improvement was additionally evaluated against a
dimension-matched control.

The control preserved the number of added radial–angular dimensions
while destroying their true sketch-level correspondence.

The observed improvement of the correctly aligned representation was
substantially greater than the corresponding dimension-matched
permutation control.

This provides evidence that the downstream improvement is not
adequately explained by dimensional expansion alone.

The result is interpreted as task-level complementarity rather than
information-theoretic independence.

---

# 14. Descriptor-Level Ablation

The 28-dimensional radial–angular representation was decomposed into
its predefined descriptor blocks.

The downstream results were:

| Representation | Balanced Accuracy | Macro-F1 | Δ Macro-F1 |
|---|---:|---:|---:|
| Morphology only | 0.342609 | 0.341348 | 0.000000 |
| + F₂ radial | 0.377391 | 0.374476 | +0.033128 |
| + α₂ | 0.357391 | 0.356369 | +0.015021 |
| + observed circular | 0.359565 | 0.358571 | +0.017224 |
| + learned circular | 0.368261 | 0.366776 | +0.025428 |
| + relational | 0.364348 | 0.362158 | +0.020810 |
| **+ full radial-angular** | **0.415652** | **0.412332** | **+0.070984** |

Every individual descriptor block produced a positive mean improvement
relative to morphology alone.

The full 28-dimensional radial–angular representation produced the
largest downstream improvement.

The ablation therefore indicates that the observed utility is not
confined to one individual descriptor block.

---

# 15. Integrated Results

The complete evidence chain can be summarized as follows.

### Morphology organization

The 135-dimensional explicit morphology representation exhibits
reproducible quantitative organization across spectral, neighborhood,
graph, transition, density, and permutation analyses.

### Cross-representation association

Individual morphology coordinates show statistically significant
associations with independently derived radial–angular measurements.

### Cross-validated recovery

Several radial–angular measurements can be recovered from morphology
out-of-sample.

### Sketch-level correspondence

The observed morphology → radial–angular relationships exceed
row-permutation null expectations.

### Downstream complementarity

Adding radial–angular geometry improves the 23-category downstream
discrimination task:

    Macro-F1:
    0.3413 → 0.4123

    Balanced accuracy:
    0.3426 → 0.4157

### Control

The observed gain exceeds the corresponding dimension-matched
row-permutation control.

### Ablation

The full radial–angular representation outperforms every individual
descriptor block.

Together, these results establish a coherent empirical relationship
between explicit morphology and independently derived radial–angular
geometry.

---

# 16. Claim Boundary of the Results

The results support the following statements:

1. Garment sketches exhibit reproducible quantitative morphology
   organization under the representation and analyses used here.

2. The morphology representation is statistically associated with
   independently derived radial–angular measurements.

3. Morphology can recover several radial–angular quantities
   out-of-sample.

4. The morphology ↔ radial–angular relationship depends on
   sketch-level correspondence under the tested permutation null.

5. Radial–angular geometry provides reproducible downstream utility
   beyond morphology under the tested 23-category discrimination
   task.

6. The downstream improvement is not adequately explained by adding
   dimensions alone under the dimension-matched control.

7. The downstream utility is not confined to a single radial–angular
   descriptor block.

The results do NOT establish:

- semantic morphology primitives;
- semantic garment-part recognition;
- universal morphology categories;
- a compositional morphology grammar;
- a mathematical manifold;
- causal mechanisms;
- information-theoretic independence; or
- human-like visual understanding.

---

# 17. Results Summary Table

| Scientific question | Evidence | Result |
|---|---|---|
| Does quantitative morphology exhibit organization? | Morphology-space analyses | Structured organization observed |
| Is morphology associated with RA geometry? | Spearman + FDR | Broad feature-level associations |
| Can morphology recover RA measurements? | 5-fold CV | CV R² = 0.059–0.296 |
| Is correspondence sketch-specific? | 100-permutation null | All four targets p = 0.0099 |
| Does RA add downstream utility? | 23-category task | Δ Macro-F1 = +0.0710 |
| Is gain explained by dimension count? | Dimension-matched control | Observed gain exceeds null |
| Is gain confined to one RA block? | Descriptor ablation | Full 28-D > individual blocks |

---

# 18. Final Result Statement

The results support an empirical characterization of garment sketches
as occupying a structured quantitative morphology space.

An independently derived radial–angular representation is reproducibly
associated with this morphology and provides additional downstream
utility under the tested discrimination task.

The evidence therefore supports quantitative geometric organization
and representation-level complementarity, while remaining agnostic
about semantic morphology categories, semantic primitives, causal
mechanisms, and mathematical manifold structure.