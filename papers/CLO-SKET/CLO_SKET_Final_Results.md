# 4. Results

## 4.1 Study population and frozen representations

The analysis comprised 2,300 garment sketches from 23 garment categories and 230 source-garment identities. Each category contained 10 source identities and 100 sketches. Replication was approximately balanced, but individual source identities contained 9–11 images because of irregularities in the filename-derived replicate records. All analyses retained the observed population without deleting or normalizing these records.

Each sketch was represented by two independently constructed geometric descriptions. The frozen morphology representation contained 135 image-derived features: 64 horizontal occupancy coordinates, 64 vertical occupancy coordinates, and seven global descriptors. Exact reconstruction from the source TIFF images reproduced the stored contiguous `float32` matrix and its SHA-256 fingerprint (`66ae04156ee3fbf3f2605f382a16fc41cf19af34b50e59dd43f6c9427d96b2ee`).

The independently derived radial–angular representation contained 28 descriptors: nine F₂ radial features, seven α₂ features, three observed circular descriptors, four learned circular descriptors, and five relational descriptors. Both representations contained 2,300 finite rows. Their image-reference arrays contained 2,300 unique paths in identical order, establishing exact row-level correspondence between morphology and radial–angular measurements.

## 4.2 Quantitative organization of morphology space

After source-only standardization, 73 principal components retained approximately 95% of the variance in the 135-dimensional morphology representation. This is reported as a variance-retention result and not as evidence that the data possess a mathematical intrinsic dimension of 73.

The representation exhibited reproducible quantitative organization across neighborhood, graph-geodesic, transition, multiscale-density, and permutation analyses. The morphology graph was connected, and Euclidean and graph-based neighborhood orderings showed substantial agreement. Multiscale density analysis identified regions with different quantitative morphology profiles, while region-size-preserving permutation controls showed that same-region neighbor retention was greater than expected under the specified null. Cross-scale analyses further showed that feature-level regional discrimination profiles were more stable than expected under independently permuted, size-preserving assignments.

These findings support structured, density-associated organization in morphology space. They do not establish discrete morphology states, universal garment categories, or a garment grammar: within-region dispersion remained substantial, and the separation signal weakened across scale.

## 4.3 Feature-level morphology–radial–angular associations

Feature-wise Spearman associations were evaluated between the 135 morphology coordinates and four radial–angular measurements: F₂ peak magnitude, F₂ peak radius, observed R₂ at the F₂ peak shell, and the magnitude of axial disagreement between observed and learned orientations. Benjamini–Hochberg correction was applied separately within each target.

F₂ peak magnitude exhibited the broadest and strongest associations. The largest absolute association was observed for horizontal occupancy coordinate 50 (ρ = −0.5469), while symmetry was the strongest associated global descriptor (ρ = 0.4840). Overall, 126 of 135 morphology coordinates were significant after false-discovery-rate correction; the median and maximum absolute correlations were 0.2173 and 0.5469, respectively.

F₂ peak radius showed weaker but distributed associations. Its strongest association was with horizontal occupancy coordinate 45 (ρ = 0.3537); 93 of 135 features were significant, with median and maximum absolute correlations of 0.0979 and 0.3537. Observed R₂ at the F₂ peak was most strongly associated with horizontal occupancy coordinate 44 (ρ = 0.3944); 106 features were significant, with median and maximum absolute correlations of 0.1315 and 0.3944. Axial-disagreement magnitude showed the weakest feature-level pattern: the strongest association was with vertical occupancy coordinate 32 (ρ = −0.2171), 90 features were significant, and the median absolute correlation was 0.0871.

The multiplicity-corrected associations demonstrate distributed cross-representation correspondence. Because the morphology coordinates are correlated, counts of significant features are treated as descriptive breadth rather than counts of independent effects.

## 4.4 Evaluation design and source-identity separation

The original downstream evaluation used five category-stratified image-level folds. Audit showed that every test sketch had a source-garment identity represented in its corresponding training set. The original analysis therefore measures performance on unseen sketches of previously observed source identities, not generalization to unseen garments.

For the primary validation, five exactly category-balanced grouped folds were constructed. Each fold withheld two complete source identities per category, producing 46 test identities across all 23 categories. No source identity crossed training and testing, every identity was tested exactly once, and every sketch received one out-of-fold prediction. Fold sizes ranged from 459 to 461 images because the observed identity-level replication was slightly unbalanced.

## 4.5 Reproduction of the original image-level integration result

Before grouped evaluation, the historical downstream result was reproduced with the frozen representations and original folds. Under the original fold-mean convention, morphology alone achieved a Macro-F1 of 0.3411 and balanced accuracy of 0.3422. Adding the 28-dimensional radial–angular representation increased Macro-F1 to 0.4123 and balanced accuracy to 0.4157, corresponding to gains of 0.0712 and 0.0735, respectively.

These results reproduce the original integration finding but retain its image-level interpretation because source identities were shared between training and test partitions.

## 4.6 Primary unseen-source-identity integration result

Under source-identity-grouped evaluation, morphology alone achieved a pooled Macro-F1 of 0.3068 and balanced accuracy of 0.3078. The integrated morphology–radial–angular representation achieved a Macro-F1 of 0.3414 and balanced accuracy of 0.3422. The improvements were therefore 0.0346 Macro-F1 and 0.0343 balanced accuracy (Table 1). The integrated representation outperformed morphology alone in all five grouped folds for both metrics and improved category-level F1 in 18 of the 23 categories.

**Table 1. Classification performance under image-level and source-identity-grouped evaluation.**

| Evaluation | Representation | Macro-F1 | Balanced accuracy |
|---|---|---:|---:|
| Original image-level folds | Morphology | 0.3411 | 0.3422 |
| Original image-level folds | Morphology + radial–angular | 0.4123 | 0.4157 |
| Source-identity-grouped folds | Radial–angular | 0.2653 | 0.2761 |
| Source-identity-grouped folds | Morphology | 0.3068 | 0.3078 |
| Source-identity-grouped folds | Morphology + radial–angular | **0.3414** | **0.3422** |

Radial–angular descriptors alone were weaker than morphology alone, achieving a Macro-F1 of 0.2653 and balanced accuracy of 0.2761. The integrated representation exceeded the radial–angular-only representation by 0.0761 Macro-F1 and 0.0661 balanced accuracy and improved category-level F1 in 19 of 23 categories. Thus, radial–angular geometry was not a stronger standalone classifier; its downstream value emerged in combination with morphology.

## 4.7 Identity-aware uncertainty and split robustness

Uncertainty in the primary grouped effect was assessed by resampling complete source identities within each category while holding the grouped out-of-fold predictions fixed. Across 5,000 replicates, the observed Macro-F1 gain of 0.0346 had a 95% interval of [0.0158, 0.0540]. The balanced-accuracy gain of 0.0343 had an interval of [0.0156, 0.0543]. Only 0.04% of replicates produced a non-positive effect for either metric.

Sensitivity to identity-to-fold allocation was assessed using ten independently generated, exactly category-balanced grouped partitions. The integrated representation improved pooled Macro-F1 and balanced accuracy in all ten partitions. The mean Macro-F1 gain was 0.0423 across partitions (SD = 0.0070; range, 0.0336–0.0529), and the mean balanced-accuracy gain was 0.0406 (SD = 0.0071; range, 0.0313–0.0517). At the individual-fold level, 49 of 50 effects were positive for each metric, and no convergence warnings occurred.

The bootstrap intervals quantify uncertainty across sampled source identities conditional on fixed grouped predictions. Variation across the repeated partitions is interpreted as descriptive split-robustness evidence rather than as an independent confidence interval.

## 4.8 Within-category alignment control

A within-category perturbation tested whether the integrated classification gain specifically depended on correct held-out sketch-level pairing. Within each grouped test fold, radial–angular rows were permuted among sketches from the same garment category, preserving category membership and category-level radial–angular distributions while disrupting exact morphology–radial–angular correspondence. The trained models, morphology rows, and grouped folds remained fixed.

Across 2,000 perturbations, the aligned model achieved a Macro-F1 of 0.3414, compared with a permuted mean of 0.3353. The aligned-minus-permuted difference was 0.0062, with an empirical probability of 0.1419. For balanced accuracy, the aligned value was 0.3422 and the permuted mean was 0.3353, giving a difference of 0.0068 and an empirical probability of 0.1229.

Correct sketch-level alignment was slightly favorable on average, but the observed advantage was not sufficiently extreme relative to the within-category perturbation distribution to support an alignment-specific mechanism. The downstream result therefore supports complementary category-discriminative information in the radial–angular representation, but does not establish that the gain depends specifically on exact held-out sketch-level correspondence.

## 4.9 Recovery of radial–angular measurements from morphology

The historical recovery estimator was first reproduced exactly. It consisted of training-fold standardization followed by Ridge regression with α = 1, evaluated using shuffled five-fold cross-validation with random state 42. No category labels, feature selection, or hyperparameter search were used. All historical R², MAE, RMSE, and Spearman metrics were reproduced at their reported six-decimal precision.

The identical fixed estimator was then evaluated with the source-identity-grouped folds. F₂ peak magnitude showed the strongest grouped recovery (R² = 0.3022; Spearman ρ = 0.6311). Observed R₂ at the F₂ peak remained recoverable (R² = 0.1910; ρ = 0.5216), as did axial-disagreement magnitude (R² = 0.2063; ρ = 0.4429). Identity-aware bootstrap intervals excluded zero for both R² and Spearman association for these three targets (Table 2).

**Table 2. Morphology-to-radial–angular recovery under unseen-source-identity evaluation.**

| Target | Historical image-level R² | Grouped R² | Grouped 95% interval | Grouped Spearman ρ | Spearman 95% interval |
|---|---:|---:|---:|---:|---:|
| F₂ peak magnitude | 0.2961 | **0.3022** | [0.2669, 0.3339] | 0.6311 | [0.6024, 0.6584] |
| F₂ peak radius | 0.0594 | 0.0143 | [−0.0423, 0.0666] | 0.3249 | [0.2841, 0.3661] |
| R₂ at F₂ peak | 0.2170 | **0.1910** | [0.1214, 0.2539] | 0.5216 | [0.4798, 0.5635] |
| Axial-disagreement magnitude | 0.1979 | **0.2063** | [0.1482, 0.2601] | 0.4429 | [0.3963, 0.4884] |

F₂ peak radius showed a different pattern. Its grouped R² was 0.0143, with an interval of [−0.0423, 0.0666], whereas its Spearman association remained positive (ρ = 0.3249; 95% interval, [0.2841, 0.3661]). Morphology therefore retained ordinal information about peak radius but did not reliably recover its precise metric value.

Overall, morphology contained identity-generalizable information about harmonic magnitude, angular coherence, and the magnitude of observed–learned axial disagreement. The fixed linear estimator is interpreted as an information probe and not as evidence of complete reconstruction or a causal relationship between the representations.

## 4.10 Supplementary direct axial-orientation sensitivity analysis

The axial-disagreement target above is a scalar error magnitude rather than a direction. Direct recovery of observed axial orientation was therefore examined separately using the doubled-angle representation, predicting cos(2α) and sin(2α) from morphology under the same source-grouped folds. Predicted components were converted back to axial directions and evaluated using angular error on [0°, 90°]. A training-fold mean axial direction served as an internal no-morphology reference.

The morphology model reduced mean axial error from 21.46° to 20.01°, an improvement of 1.45° (paired identity-bootstrap 95% interval, [0.43°, 2.53°]). Mean axial agreement increased by 0.048 (95% interval, [0.023, 0.075]), and accuracy within 30° increased by 1.78 percentage points (95% interval, [0.48, 3.18]).

The result was not uniformly favorable. Median angular error was 7.49° for the morphology model and 6.14° for the mean-direction reference; the paired median difference consistently favored the reference. Accuracy within 10° was also 5.13 percentage points lower for the morphology model. Differences in R₂-weighted mean error and accuracy within 15° were inconclusive.

Morphology therefore provided limited tail-sensitive directional information, reducing some larger angular errors, but did not improve typical high-precision orientation prediction beyond the dominant training-fold direction. This analysis is treated as supplementary sensitivity evidence rather than a central positive result.

## 4.11 Integrated results and claim boundary

The principal finding is that the independently derived radial–angular representation provided complementary downstream information beyond frozen morphology under strict unseen-source-garment evaluation. The integrated advantage was positive in all five primary grouped folds, all ten repeated grouped partitions, and most garment categories, with identity-aware intervals excluding zero.

Morphology also retained identity-generalizable information about several radial–angular quantities. Recovery was strongest for F₂ peak magnitude and remained meaningful for angular coherence and axial-disagreement magnitude. Precise F₂ peak-radius recovery was weak, and direct axial-orientation recovery produced mixed results relative to a strong mean-direction reference.

The results support quantitative organization in morphology space, distributed association between morphology and independently derived radial–angular measurements, and representation-level complementarity in the tested 23-category task. They do not establish discrete morphology states, a garment grammar, semantic garment primitives, causal mechanisms, information-theoretic independence, or a general dependence of downstream utility on exact sketch-level alignment.
