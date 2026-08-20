# 3. Methods

## 3.1 Study design

This study investigated the quantitative geometric organization of garment sketches using two explicitly defined, independently constructed representations: a canonical 135-dimensional morphology representation and a 28-dimensional radial–angular representation. The analysis was representation-focused rather than semantic. Neither garment-category labels nor manually annotated garment parts were used to construct either representation.

The analytical sequence was: (1) reconstruction and integrity verification of the frozen morphology representation; (2) independent construction of radial–angular descriptors from the same source images; (3) row-level provenance verification between representations; (4) characterization of morphology-space organization and feature-level cross-representation associations; (5) cross-validated recovery of radial–angular measurements from morphology; and (6) evaluation of downstream representation complementarity under source-identity-grouped classification. Supplementary analyses assessed sensitivity to fold allocation, held-out sketch-level alignment, and direct axial-orientation recovery.

## 3.2 Dataset and source-identity reconstruction

The study used the CLO-SKET dataset (Arnia, 2020), which contains 2,300 garment sketches derived from 230 source clothing photographs: 23 predefined garment subcategories, 10 source photographs per subcategory, and 10 sketchers per source photograph. The present analysis used all 2,300 TIFF sketches. File paths were retained in the frozen radial–angular row order and were used to align all subsequent representations.

Source identity was reconstructed from the filename convention, in which the first numeric token identified the source garment within a category and the second numeric token represented a replicate identifier. The observed separators (`-`, `_`, and one `+`) were audited rather than normalized in the source records. Source identity was defined as the combination of garment category and the first numeric token, because numeric source identifiers repeat across categories.

This procedure identified 230 source-garment identities, with exactly 10 identities per category. Replication was not assumed to be perfectly factorial: source identities contained 9–11 images because of irregular filename records, including repeated identity–replicate combinations and two nonstandard replicate identifiers. All 2,300 images were retained. Grouped analyses used the source-garment identity as the indivisible sampling and partitioning unit.

## 3.3 Canonical 135-dimensional morphology representation

The morphology representation was derived from canonical 64 × 64 grayscale sketch images. Pixel intensities were divided by 255, and foreground pixels were defined using an intensity threshold below 0.8. The representation comprised 64 horizontal occupancy coordinates, 64 vertical occupancy coordinates, and seven global geometric descriptors:

\[
64 + 64 + 7 = 135.
\]

The resulting matrix had shape 2,300 × 135 and was stored as `float32`. The canonical matrix was reconstructed directly from the frozen source-image paths using the original preprocessing definition. Reconstruction produced 2,300 finite vectors without failure and reproduced the recorded SHA-256 fingerprint exactly (`66ae04156ee3fbf3f2605f382a16fc41cf19af34b50e59dd43f6c9427d96b2ee`). The matrix was subsequently treated as read-only.

## 3.4 Morphology-space organization

For analyses requiring standardized coordinates, each morphology feature was standardized before principal component analysis (PCA). The retained PCA representation explained approximately 95% of standardized morphology variance using 73 components. PCA was used only as a coordinate and variance-retention procedure and was not interpreted as a semantic decomposition or as proof of mathematical intrinsic dimensionality.

Morphology-space organization was examined using local-neighborhood, spectral, graph-geodesic, transition, multiscale-density, and permutation-based analyses. Density-defined regions were treated as areas of differing quantitative morphology density rather than discrete garment states. Region-size-preserving permutations were used to assess local neighbor retention and cross-scale stability of feature-level regional discrimination. Feature-order permutations disrupted the spatial ordering of occupancy coordinates while preserving each sketch's occupancy values. These analyses tested reproducible quantitative organization and did not use garment-category labels to construct the morphology space.

## 3.5 Independent radial–angular representation

The radial–angular branch was constructed independently of the frozen morphology matrix. Source sketches were represented in an isotropic physical coordinate system and referenced to an intensity-weighted centroid. Radial and angular profiles were used to characterize the spatial distribution of sketch intensity, including second-harmonic radial magnitude and phase, circular concentration, and relationships between observed and learned axial organization.

The final compact representation contained 28 descriptors distributed across five predefined blocks:

| Descriptor block | Dimensions |
|---|---:|
| F₂ radial | 9 |
| α₂ | 7 |
| Observed circular | 3 |
| Learned circular | 4 |
| Relational | 5 |
| **Total** | **28** |

The resulting matrix had shape 2,300 × 28 and contained only finite values. The representation was not used to modify, select, or tune the morphology features.

Radial–circular comparisons used a locked radial domain from 3.5 to 27.5 with 25 circular shells. The F₂ peak radius was matched to the corresponding circular shell. The maximum mismatch between the recorded peak radius and matched shell center was zero across all observations.

## 3.6 Row-level provenance verification

Before any cross-representation analysis, morphology-side and radial–angular image references were audited for population size, missing values, duplicates, and ordering. Both branches contained 2,300 unique, nonempty image paths. The path arrays matched exactly in row order; therefore, morphology row \(i\) and radial–angular row \(i\) referred to the same source sketch for every observation.

## 3.7 Feature-level cross-representation association

Spearman correlation was used to quantify association between each of the 135 morphology coordinates and four independently derived radial–angular targets: F₂ peak magnitude, F₂ peak radius, observed R₂ at the matched F₂ peak shell, and axial-disagreement magnitude at that shell. The last target was defined as the unsigned axial difference between observed and learned orientations, folded onto [0°, 90°].

Benjamini–Hochberg false-discovery-rate correction was performed separately across the 135 morphology coordinates for each target. These tests were interpreted as feature-level association analyses; they did not establish causality, redundancy, complementarity, or feature independence.

## 3.8 Cross-validation designs

### 3.8.1 Historical image-level folds

The frozen historical classification analysis used five-fold `StratifiedKFold` cross-validation with shuffling and random state 42. Audit showed that all test sketches had their source identity represented in the corresponding training set. These folds were retained only to reproduce the historical image-level result and were interpreted as evaluation on unseen sketches of observed source identities.

The historical morphology-to-radial–angular recovery analysis used five-fold shuffled `KFold` cross-validation with random state 42. This distinct split definition was reproduced exactly when verifying the historical regression results.

### 3.8.2 Primary source-identity-grouped folds

For the primary evaluation, five exactly category-balanced grouped partitions were constructed. Within each of the 23 categories, the 10 source identities were randomly assigned so that each fold tested exactly two identities per category. Each test fold therefore contained 46 complete source identities and all 23 garment categories. Source identities never crossed training and testing; every identity and every sketch appeared in exactly one test fold. Because identity-level replication was slightly unbalanced, test-fold sizes ranged from 459 to 461 images.

### 3.8.3 Repeated grouped partitions

Sensitivity to identity-to-fold allocation was evaluated using ten independently generated, exactly category-balanced grouped partitions with random seeds 20260820–20260829. The fold-construction constraints were identical in every repeat: two test identities per category, all categories in every fold, zero source-identity overlap, and one test assignment per observation.

## 3.9 Downstream classification

Three representations were evaluated in the predefined 23-category classification task: morphology alone (135 dimensions), radial–angular descriptors alone (28 dimensions), and their concatenation (163 dimensions). All comparisons used identical folds and target labels.

The fixed classification pipeline consisted of `StandardScaler` fitted within each training fold followed by multinomial logistic regression with L2 regularization (`C = 1`, `solver = lbfgs`, `max_iter = 5000`, and `tol = 10⁻⁴`). No feature selection or hyperparameter search was performed. Performance was summarized using pooled out-of-fold Macro-F1 and balanced accuracy. Fold-level metrics and category-level F1 values were retained as secondary stability measures.

The historical image-level morphology and integrated results were first reproduced using the original stored folds and their original fold-mean reporting convention. The primary morphology, radial–angular, and integrated comparison was then performed using the source-identity-grouped folds.

## 3.10 Identity-aware uncertainty for the integration effect

Uncertainty in the grouped integration gain was evaluated using a category-stratified source-identity bootstrap. Within each category, the 10 source identities were sampled with replacement, and all sketches belonging to each selected identity were included as a cluster. Morphology-only and integrated out-of-fold predictions remained paired within every replicate. Macro-F1 and balanced accuracy were recomputed for 5,000 bootstrap samples using random seed 20260820.

Percentile intervals were defined by the 2.5th and 97.5th percentiles. The fraction of bootstrap effects less than or equal to zero was recorded descriptively. Because the out-of-fold predictions were held fixed, these intervals quantify uncertainty across sampled identities conditional on the fitted fold-specific models; they are not model-refitting permutation-test p-values.

## 3.11 Within-category alignment control

To test whether downstream performance specifically depended on exact held-out sketch-level pairing, radial–angular rows were permuted within garment category among the test observations of each grouped fold. This preserved category membership and the category-level radial–angular distribution while disrupting exact morphology–radial–angular pairing. Trained fold-specific models, morphology rows, representations, and grouped partitions remained unchanged.

Macro-F1 and balanced accuracy were recomputed for 2,000 perturbations using random seed 20260821. The aligned-minus-permuted effect and the +1-corrected empirical probability were reported. This fixed-model test measures sensitivity to test-time alignment and is not equivalent to a full model-refitting permutation test.

## 3.12 Morphology-to-radial–angular recovery

The recovery analysis used the 135 morphology coordinates as predictors and four radial–angular quantities as targets: F₂ peak magnitude, F₂ peak radius, observed R₂ at the F₂ peak, and axial-disagreement magnitude. The estimator was fixed as a pipeline containing training-fold `StandardScaler` followed by `Ridge(alpha = 1.0)`. No category labels, feature selection, or target-specific tuning were used.

Historical recovery was reproduced using shuffled five-fold `KFold` cross-validation with random state 42 and pooled out-of-fold R², MAE, RMSE, Pearson correlation, and Spearman correlation. The morphology matrix was promoted to `float64` before modelling, matching the historical implementation. The identical estimator and preprocessing were then applied to the source-identity-grouped folds; only the partition design changed.

Uncertainty in grouped R², MAE, RMSE, and Spearman correlation was assessed with 5,000 category-stratified source-identity bootstrap replicates using random seed 20260820. Complete identities were resampled as clusters while grouped out-of-fold predictions remained fixed.

## 3.13 Supplementary direct axial-orientation analysis

Because axial-disagreement magnitude is a scalar rather than a directional target, direct recovery of observed axial orientation was evaluated separately. Observed orientation \(\alpha\) was encoded using the doubled-angle representation

\[
(\cos 2\alpha,\;\sin 2\alpha),
\]

which respects 180° axial periodicity. Separate fold-local standardized Ridge models with \(\alpha_{\mathrm{Ridge}}=1\) predicted the cosine and sine components from morphology under the primary source-grouped folds. Predicted component pairs were normalized and transformed back to an axial angle in [0°, 180°).

Prediction error was calculated as the shortest unsigned axial difference,

\[
d_{\mathrm{axial}}(\alpha,\hat{\alpha})=
\min\left(|\alpha-\hat{\alpha}|,\;180^\circ-|\alpha-\hat{\alpha}|\right),
\]

which lies in [0°, 90°]. A training-fold mean axial direction served as an internal no-morphology reference. Metrics included mean and median axial error, interquartile error range, proportions within 10°, 15°, and 30°, mean \(\cos(2\Delta\alpha)\) agreement, and an observed-R₂-weighted mean error. The complete 2,300-sketch population was primary; thresholds of observed R₂ ≥ 0.20 and R₂ ≥ 0.40 were supplementary sensitivity strata rather than exclusion criteria.

Model–reference differences were evaluated using 5,000 paired, category-stratified source-identity bootstrap samples. Complete identities were resampled, and both methods were evaluated on identical resampled observations. Positive effects were defined consistently as favoring the morphology model. This component-wise analysis respects axial periodicity but is not a full probabilistic circular-regression model.

## 3.14 Computational integrity and reproducibility

All final analyses used Python 3.12.13, NumPy 2.0.2, pandas 2.2.3, and scikit-learn 1.6.1. Frozen runtime backups were inventoried and hashed before validation. The canonical morphology matrix was reproduced exactly from the source images, and grouped-fold construction was audited for category coverage, test assignment, and source-identity overlap.

Final result tables, uncertainty summaries, fold-design records, and claim boundaries were consolidated into a versioned result package. Each canonical table received an individual SHA-256 fingerprint. The final pickle package had SHA-256 `c174f33bd40950bc4daa66d39ee0290869b79f758eac77f3ae9303847ed9a2df`; its compressed archive and uncompressed contents were independently copied and hash-verified.

## 3.15 Methodological scope

The representations and association analyses were label-free; garment-category labels entered only the downstream classification task and the category-stratified design of grouped folds and bootstrap resampling. The analyses test quantitative organization, cross-representation association, recoverability, and task-level complementarity under the specified dataset and fixed estimators. They do not test semantic garment-part recognition, causal mechanisms, information-theoretic independence, universal morphology categories, or a garment grammar.
