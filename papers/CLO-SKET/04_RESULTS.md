## Source-identity-aware validation design

The CLO-SKET evaluation population comprised 2,300 sketches from 23 garment categories and 230 source-garment identities. Each category contained 10 source identities. Replication was approximately balanced but not perfectly factorial: individual identities contained 9–11 images because of irregularities in the filename-derived replicate records.

The original five-fold image-level cross-validation partitioned individual sketches while preserving category balance. Audit of these folds showed that every test sketch had a source-garment identity represented in its corresponding training set. Consequently, the original analysis evaluates unseen sketches of previously observed source identities rather than generalization to unseen garments.

To evaluate the stricter latter condition, five category-balanced grouped folds were constructed. Each fold withheld exactly two source identities per category, giving 46 test identities across all 23 categories. No source identity crossed training and testing, every row was tested exactly once, and fold sizes ranged from 459 to 461 sketches.

## Reproduction of the original image-level integration result

Before grouped evaluation, the original downstream classification result was reproduced using the frozen 135-dimensional morphology representation, the independently derived 28-dimensional radial–angular representation, and the original five image-level folds.

Under the original fold-mean convention, morphology alone achieved a Macro-F1 of 0.3411 and balanced accuracy of 0.3422. Combining morphology with the radial–angular representation increased Macro-F1 to 0.4123 and balanced accuracy to 0.4157, corresponding to improvements of 0.0712 and 0.0735, respectively.

These values reproduce the original integration result but retain its image-level interpretation: test sketches may belong to source garments represented in training.

## Integration under unseen source-garment evaluation

Under source-identity-grouped evaluation, morphology alone achieved a pooled Macro-F1 of 0.3068 and balanced accuracy of 0.3078. The integrated morphology–radial–angular representation achieved a Macro-F1 of 0.3414 and balanced accuracy of 0.3422. The resulting gains were:

[
\Delta\mathrm{Macro\text{-}F1}=+0.0346
]

and

[
\Delta\mathrm{Balanced\ Accuracy}=+0.0343.
]

The integrated representation outperformed morphology alone in all five grouped folds for both metrics. At the category level, integration improved F1 for 18 of the 23 categories.

Thus, the integration advantage persisted when complete source-garment identities were excluded from training, although its magnitude was smaller than under the original image-level evaluation.

| Evaluation                    | Representation              | Macro-F1 | Balanced accuracy |
| ----------------------------- | --------------------------- | -------: | ----------------: |
| Original image-level folds    | Morphology                  |   0.3411 |            0.3422 |
| Original image-level folds    | Morphology + radial–angular |   0.4123 |            0.4157 |
| Source-identity-grouped folds | Morphology                  |   0.3068 |            0.3078 |
| Source-identity-grouped folds | Morphology + radial–angular |   0.3414 |            0.3422 |

## Identity-aware uncertainty and split robustness

Uncertainty in the grouped integration effect was evaluated by resampling complete source-garment identities within each category while holding the grouped out-of-fold predictions fixed. Across 5,000 bootstrap replicates, the observed Macro-F1 gain of 0.0346 had a 95% interval of [0.0158, 0.0540]. The balanced-accuracy gain of 0.0343 had a corresponding interval of [0.0156, 0.0543]. Only 0.04% of replicates produced a non-positive effect for either metric.

Sensitivity to identity-to-fold allocation was assessed using ten independently generated, exactly category-balanced grouped partitions. The integrated representation improved pooled Macro-F1 and balanced accuracy in all ten partitions. The mean Macro-F1 gain was 0.0423 across partitions, with an SD of 0.0070 and a range of 0.0336–0.0529. The mean balanced-accuracy gain was 0.0406, with an SD of 0.0071 and a range of 0.0313–0.0517. At the individual-fold level, 49 of 50 comparisons were positive for each metric, and no convergence warnings occurred.

These analyses indicate that the grouped integration result was not dependent on one favorable assignment of source identities to folds. The bootstrap intervals are conditional on the fixed out-of-fold predictions, while variation across repeated grouped partitions is interpreted as descriptive split-robustness evidence rather than an independent confidence interval.

## Radial–angular representation alone

The radial–angular representation was also evaluated independently under the same grouped folds. Radial–angular features alone achieved a Macro-F1 of 0.2653 and balanced accuracy of 0.2761, below both morphology alone and the integrated representation.

| Representation              |   Macro-F1 | Balanced accuracy |
| --------------------------- | ---------: | ----------------: |
| Radial–angular only         |     0.2653 |            0.2761 |
| Morphology only             |     0.3068 |            0.3078 |
| Morphology + radial–angular | **0.3414** |        **0.3422** |

The integrated representation exceeded radial–angular features alone by 0.0761 Macro-F1 and 0.0661 balanced accuracy and improved category-level F1 for 19 of 23 categories relative to the radial–angular-only model.

The radial–angular representation is therefore not a stronger standalone classifier than morphology. Its downstream value arises when it is combined with morphology, supporting representation-level complementarity under the tested task.

## Within-category alignment control

A within-category alignment control examined whether the grouped integration gain specifically depended on the correct pairing between each held-out sketch’s morphology and radial–angular descriptors. Within each grouped test fold, radial–angular rows were permuted among sketches belonging to the same garment category while the fitted models and morphology rows remained fixed. This preserved category membership and category-level radial–angular distributions while disrupting exact held-out sketch correspondence.

Across 2,000 perturbations, the aligned combined model achieved a Macro-F1 of 0.3414, compared with a permuted mean of 0.3353. The aligned-minus-permuted difference was 0.0062, with an empirical probability of 0.1419. For balanced accuracy, the aligned value was 0.3422 and the permuted mean was 0.3353, giving a difference of 0.0068 and an empirical probability of 0.1229.

Correct sketch-level alignment produced slightly higher performance on average, but the observed advantage did not exceed the within-category perturbation distribution sufficiently to support a strong alignment-specific mechanism. Accordingly, the grouped classification result supports complementary category-discriminative information in the radial–angular representation, but it does not establish that the gain depends specifically on exact sketch-level morphology–radial–angular correspondence.

## Cross-validated recovery of radial–angular measurements

The historical morphology-to-radial–angular recovery analysis was first reproduced exactly. The original estimator consisted of fold-local standardization followed by Ridge regression with (\alpha=1), evaluated using shuffled five-fold cross-validation with random state 42. No category labels, feature selection, or hyperparameter search were used.

The reproduced historical results matched all reported metrics at six-decimal precision. The same fixed estimator was then evaluated using the source-identity-grouped folds.

| Target                       | Historical image-level (R^2) | Grouped (R^2) | Grouped 95% identity-bootstrap interval | Grouped Spearman (\rho) |
| ---------------------------- | ---------------------------: | ------------: | --------------------------------------: | ----------------------: |
| F₂ peak magnitude            |                       0.2961 |    **0.3022** |                        [0.2669, 0.3339] |                  0.6311 |
| F₂ peak radius               |                       0.0594 |        0.0143 |                       [−0.0423, 0.0666] |                  0.3249 |
| (R_2) at the F₂ peak         |                       0.2170 |    **0.1910** |                        [0.1214, 0.2539] |                  0.5216 |
| Axial-disagreement magnitude |                       0.1979 |    **0.2063** |                        [0.1482, 0.2601] |                  0.4429 |

F₂ peak magnitude showed the strongest grouped recovery, with (R^2=0.3022) and (\rho=0.6311). Angular coherence at the F₂ peak also remained recoverable, with (R^2=0.1910) and (\rho=0.5216). The magnitude of disagreement between observed and learned axial orientations yielded (R^2=0.2063) and (\rho=0.4429). All three targets had positive (R^2) and Spearman intervals under identity-aware resampling.

F₂ peak radius behaved differently. Its grouped (R^2) was 0.0143, and its identity-bootstrap interval included zero. Its Spearman association remained positive, however, with (\rho=0.3249) and a 95% interval of [0.2841, 0.3661]. Morphology therefore retained ordinal information about peak radius but did not reliably recover its precise metric value.

These results indicate that morphology contains identity-generalizable information about harmonic magnitude, angular coherence, and observed–learned axial-disagreement magnitude. The recovery analysis uses a fixed linear estimator as an information probe and does not imply complete reconstruction or a causal relationship between the representations.

## Supplementary direct axial-orientation sensitivity analysis

The axial-disagreement target above is a scalar error magnitude rather than a directional variable. Direct recovery of observed axial orientation was therefore examined separately using the doubled-angle representation:

[
X_{\mathrm{morphology}}
\rightarrow
\left(\cos 2\alpha_{\mathrm{obs}},
\sin 2\alpha_{\mathrm{obs}}\right).
]

The two components were predicted using fold-local standardized Ridge models under the same source-identity-grouped folds. Predictions were converted back to axial directions and evaluated using angular error on ([0^\circ,90^\circ]). A training-fold mean axial direction served as a no-morphology internal reference.

The morphology model reduced mean axial error from (21.46^\circ) to (20.01^\circ), an improvement of (1.45^\circ). A paired identity-aware bootstrap interval for this reduction was [(0.43^\circ,2.53^\circ)]. Mean axial agreement also increased by 0.048, with an interval of [0.023, 0.075], and accuracy within (30^\circ) increased by 1.78 percentage points.

The result was not uniformly favorable, however. Median angular error was (7.49^\circ) for the morphology model and (6.14^\circ) for the mean-direction reference. The reference also exceeded the morphology model for accuracy within (10^\circ), by 5.13 percentage points. Differences in (R_2)-weighted mean error and accuracy within (15^\circ) were inconclusive.

Thus, morphology provided limited tail-sensitive directional information, reducing some larger axial errors, but it did not improve typical high-precision orientation prediction beyond the dominant training-fold direction. This analysis is treated as supplementary sensitivity evidence rather than a central positive result.

## Integrated result

The principal finding is that radial–angular geometry provides complementary downstream information beyond the frozen morphology representation under a strict unseen-source-garment evaluation. The improvement was positive across all primary grouped folds, all ten repeated grouped partitions, and most garment categories, with identity-aware uncertainty intervals excluding zero.

Morphology also retained identity-generalizable information about several independently derived radial–angular quantities. This recovery was strongest for F₂ peak magnitude and remained meaningful for angular coherence and axial-disagreement magnitude. Exact F₂ peak-radius recovery was weak, and direct axial-orientation recovery produced mixed results relative to a strong mean-direction reference.

The evidence therefore supports representation-level complementarity and cross-representation quantitative association. It does not establish semantic garment primitives, universal morphology categories, causal mechanisms, information-theoretic independence, or a general dependence of downstream utility on exact sketch-level morphology–radial–angular alignment.
