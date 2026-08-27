# Paper I Fresh Study — Mathematical Design Lock

**Status:** Pre-code confirmatory design

**Scope:** Paper I (`papers/CLO-SKET`) only

**Purpose:** Strengthen the scientific evaluation of the frozen 14-dimensional axial–radial representation without reopening, retuning, or replacing the existing Experiment 06 and Experiment 07 results.

## 1. Scientific principle

The study asks whether a compact, explicit axial–radial representation contributes category-discriminative information beyond increasingly informative visual baselines under garment-identity-disjoint validation.

The study is not designed to maximize benchmark performance. It is designed to distinguish four claims that must not be conflated:

1. **Standalone utility:** a representation predicts garment category.
2. **Conditional increment:** adding the representation improves a specified baseline.
3. **Garment-specific correspondence:** any increment depends on pairing the representation with the correct garment identity.
4. **Compact interpretability:** a 14-dimensional explicit representation retains useful structure relative to equally compact or substantially larger opaque representations.

All outcomes, including null and negative outcomes, are admissible.

## 2. Frozen observational units

For sketch (i):

\[
(Y_i,J_i,C_i)
\]

denote garment-category label, recovered source-garment identity, and any additional category/provenance metadata. The dataset contains 2,300 sketches, 23 garment categories, and 230 recovered garment identities.

The indivisible dependency unit is (J_i), not the individual sketch. No sketch associated with a test identity may enter training, preprocessing estimation, dimensionality reduction, model selection, or calibration for that fold.

The recovered identity labels remain conditional on the filename/category reconstruction audit. They are not treated as proof that different recovered identities are independent above the garment level.

## 3. Frozen representations

The existing representations remain unchanged:

\[
M_i\in\mathbb R^{135},
\qquad
R_i\in\mathbb R^{8},
\qquad
A_i\in\mathbb R^{6},
\qquad
G_i=R_i\oplus A_i\in\mathbb R^{14}.
\]

Here (M_i) is the frozen morphology representation and (G_i) is the frozen compact axial–radial representation. The new study must not alter these coordinates in response to predictive results.

The existing HOG representation is

\[
H_i\in\mathbb R^{8100}.
\]

A frozen self-supervised visual embedding will be introduced as

\[
L_i\in\mathbb R^{d_L}.
\]

The encoder weights, image preprocessing, layer, pooling rule, and output dimension must be fixed before feature extraction. The encoder will not be fine-tuned on CLO-SKET. The primary learned representation will be a frozen DINOv2 ViT-S/14 image embedding; exact implementation provenance and model-weight hash or immutable upstream identifier must be recorded before execution.

CLIP, supervised ResNet, or any other learned representation may be evaluated only as explicitly labelled secondary sensitivity analyses. They must not replace the frozen primary learned baseline after outcomes are observed.

## 4. Geometric definition and transformation requirements

For radial shell (r), let (p_i(\theta_k\mid r)) be the normalized angular foreground distribution. The second circular harmonic is

\[
F_{2,i}(r)
=
\sum_k p_i(\theta_k\mid r)e^{-2\mathrm{i}\theta_k}
=
C_{2,i}(r)-\mathrm{i}S_{2,i}(r).
\]

Its magnitude and axial orientation are

\[
R_{2,i}(r)=|F_{2,i}(r)|,
\]

\[
\alpha_{2,i}(r)
=
-\frac12\arg F_{2,i}(r)
=
\frac12\operatorname{atan2}\!\left(S_{2,i}(r),C_{2,i}(r)\right)
\pmod{\pi}.
\]

Under an ideal rigid rotation by (\phi), the Cartesian-coordinate convention requires

\[
F'_{2,i}(r)=e^{-2\mathrm{i}\phi}F_{2,i}(r),
\]

and therefore

\[
R'_{2,i}(r)=R_{2,i}(r),
\qquad
\alpha'_{2,i}(r)=\alpha_{2,i}(r)+\phi\pmod{\pi}.
\]

### Post-outcome coordinate-convention clarification (2026-08-27)

The equations immediately above use Cartesian coordinates, with the vertical axis positive upward. The frozen raster implementation uses native image coordinates, with the vertical axis positive downward. Under a visual counterclockwise rotation by \(\phi\), its angular coordinate therefore transforms as

\[
\theta'_{\mathrm{img}}=\theta_{\mathrm{img}}-\phi.
\]

For the frozen image-coordinate implementation,

\[
F'_{2,\mathrm{img}}(r)
=
e^{+2\mathrm{i}\phi}F_{2,\mathrm{img}}(r),
\qquad
R'_{2,\mathrm{img}}(r)=R_{2,\mathrm{img}}(r),
\]

and hence

\[
\alpha'_{2,\mathrm{img}}(r)
=
\alpha_{2,\mathrm{img}}(r)-\phi
\pmod{\pi}.
\]

Thus the synthetic raster observation
\(\alpha'_{2,\mathrm{img}}-\alpha_{2,\mathrm{img}}\approx-\phi\)
is the expected image-coordinate form of the same axial equivariance, not a sign error in the frozen feature bytes. This clarification was written after predictive results were frozen. It changes neither code, feature values, hashes, thresholds, nor outcomes. It resolves only the coordinate notation; the failed raster magnitude gate and the overall failed RA14 mechanical gate remain unchanged, and Experiment 08 remains exploratory under the scientific-status amendment.

Axial comparisons must use doubled-angle coordinates or the axial distance

\[
d_{\pi}(\alpha,\beta)
=
\frac12\left|\operatorname{Arg}e^{2\mathrm{i}(\alpha-\beta)}\right|.
\]

Phase values from shells with negligible (R_2) must not be interpreted as well-conditioned orientation measurements. Mechanical validation must report errors as functions of harmonic magnitude or shell support.

## 5. Primary question and estimand

The primary scientific question is:

> Does the frozen 14-dimensional axial–radial representation add garment-category information beyond a frozen self-supervised visual embedding for unseen recovered garment identities?

Let \(\mathcal F_1(X)\) denote pooled out-of-fold macro-F1 from the locked classifier applied to feature set (X). The primary estimand is

\[
\Delta_{G\mid L}
=
\mathcal F_1(L\oplus G)-\mathcal F_1(L).
\]

The primary null hypothesis is

\[
H_0:\Delta_{G\mid L}\le 0,
\]

against the directional alternative

\[
H_1:\Delta_{G\mid L}>0.
\]

The paired category-stratified garment-identity bootstrap confidence interval is the primary inferential object. A positive point estimate alone is insufficient.

## 6. Practical-effect classification

Statistical detectability and practical magnitude will be reported separately. Before execution, the following interpretive bands are frozen for macro-F1:

- **Complementary and practically material:** 95% paired identity-bootstrap confidence interval excludes zero and \(\Delta_{G\mid L}\ge 0.01\).
- **Detectable but small:** confidence interval excludes zero and \(0<\Delta_{G\mid L}<0.01\).
- **Inconclusive:** confidence interval includes zero.
- **Evidence of deterioration:** confidence interval lies below zero.

The 0.01 threshold is an interpretive minimum, not a null-hypothesis boundary and not a universal clinical or operational standard.

## 7. Prespecified secondary contrasts

Using the same rows, folds, preprocessing boundary, classifier, and pooled predictions, estimate:

\[
\Delta_{G\mid M}
=
\mathcal F_1(M\oplus G)-\mathcal F_1(M),
\]

\[
\Delta_{G\mid H}
=
\mathcal F_1(H\oplus G)-\mathcal F_1(H),
\]

\[
\Delta_{G\mid M\oplus L}
=
\mathcal F_1(M\oplus L\oplus G)-\mathcal F_1(M\oplus L),
\]

and the radial/axial decompositions

\[
\Delta_{R\mid L}
=
\mathcal F_1(L\oplus R)-\mathcal F_1(L),
\]

\[
\Delta_{A\mid L}
=
\mathcal F_1(L\oplus A)-\mathcal F_1(L),
\]

\[
\Delta_{A\mid L\oplus R}
=
\mathcal F_1(L\oplus R\oplus A)-\mathcal F_1(L\oplus R).
\]

These contrasts are secondary. Their bootstrap p-values, if reported, will be multiplicity-adjusted within the secondary family using Holm's method. Confidence intervals and exact effect sizes remain primary for interpretation.

Balanced accuracy is secondary for every comparison. No model or representation may be selected because it improves the secondary metric.

### Pre-result compactness amendment (locked before any compactness outcome)

This amendment freezes only the two previously unresolved compactness decisions and does not alter any other compactness decision, margin, estimand, metric, bootstrap design, multiplicity rule, fold rule, representation, or classifier specification.

For the learned compact representation \(L^{(14)}\):

1. Within each frozen identity-disjoint fold, fit PCA with 14 components on the RAW frozen DINOv2 training-fold representation only.
2. Transform the training and held-out rows using that training-fitted PCA.
3. Then fit StandardScaler on the 14-D PCA training scores only.
4. Transform the held-out PCA scores with that same training-fitted scaler.
5. Fit the already-frozen LogisticRegression classifier on the scaled 14-D training scores.

Therefore the ordering is explicitly frozen as:

\[
\text{raw } L \rightarrow \text{training-fold PCA}_{14} \rightarrow \text{training-fold StandardScaler} \rightarrow \text{frozen LogisticRegression}.
\]

No full-dataset PCA or scaler fitting is permitted. The frozen explicit RA14 representation retains its already-frozen training-fold StandardScaler \rightarrow LogisticRegression treatment.

The compactness paired identity-bootstrap seed is frozen as:

\[
\texttt{20260821}
\]

This deliberately reuses the already-established Experiment-08 identity-bootstrap seed and is fixed before any compactness outcome is computed.

PRE-RESULT AMENDMENT: no RA14-vs-DINOv2-PCA14 prediction, metric, bootstrap result, or affected outcome had been computed or inspected when this amendment was frozen.

## 8. Compactness comparison

To separate interpretability from raw dimensional advantage, compare (G\) with fold-locally reduced baselines:

\[
H^{(14)}=\operatorname{PCA}_{14}(H),
\qquad
L^{(14)}=\operatorname{PCA}_{14}(L).
\]

PCA must be fitted on training rows only and then applied to the corresponding test fold. The compact comparisons are

\[
\mathcal F_1(G),
\quad
\mathcal F_1(H^{(14)}),
\quad
\mathcal F_1(L^{(14)}),
\quad
\mathcal F_1(H),
\quad
\mathcal F_1(L).
\]

For the prespecified non-inferiority description, define

\[
D_{G,L14}=\mathcal F_1(G)-\mathcal F_1(L^{(14)}).
\]

The compact explicit representation may be described as non-inferior to the 14-dimensional learned projection only if the lower bound of the paired 95% garment-identity-bootstrap confidence interval exceeds (-0.02). This margin is an interpretive design choice and must be reported transparently.

## 9. Exact-correspondence control

For baseline (B_i\), reassign complete (G)-blocks between recovered garment identities within garment category and matched block size:

\[
G_i\longrightarrow G_{\pi(i)}.
\]

For permutation (b), calculate

\[
\Delta^{(b)}_{G\mid B}
=
\mathcal F_1(B_i\oplus G_{\pi_b(i)})-
\mathcal F_1(B_i).
\]

The aligned statistic is

\[
\Delta^{\mathrm{aligned}}_{G\mid B}.
\]

Using (B=L), the empirical upper-tail probability is

\[
p_{\mathrm{align}}
=
\frac{1+\sum_{b=1}^{B}
\mathbf 1\!\left[
\Delta^{(b)}_{G\mid L}
\ge
\Delta^{\mathrm{aligned}}_{G\mid L}
\right]}
{B+1}.
\]

Use (B=2{,}000) prespecified permutations. A garment-specific correspondence claim requires both:

1. a positive primary conditional increment; and
2. (p_{\mathrm{align}}<0.05).

If the first condition passes but the second does not, the allowed conclusion is category-conditioned incremental information without evidence that exact garment pairing is required.

## 10. Validation design

The authoritative Experiment 06 row-level five-fold garment-identity assignment is retained for the primary comparison because it was frozen independently of the new learned-embedding result and permits direct comparison with existing evidence.

Each fold must satisfy:

- complete garment identities are assigned wholly to train or test;
- all 23 categories are represented in train and test;
- no train/test identity overlap;
- identical fold membership for every representation;
- preprocessing is learned from training rows only;
- pooled out-of-fold predictions contain exactly one primary prediction per sketch.

Ten additional category-balanced grouped partitions will be generated from frozen seeds before outcomes are computed. They are robustness analyses of split allocation, not independent experimental samples. No ordinary t-test over folds or repeated partitions is permitted.

## 11. Locked prediction model

The primary classifier is the same linear model family used in the existing evidence lineage:

- training-fold `StandardScaler`;
- multinomial logistic regression with L2 penalty;
- `C=1.0`;
- `solver="lbfgs"`;
- `max_iter=5000`;
- `class_weight=None`;
- frozen random seed;
- no hyperparameter search.

Every feature set must use the same estimator specification. Convergence status must be recorded. If convergence fails, increasing `max_iter` uniformly for every feature set is permitted and must be documented; representation-specific solver changes are prohibited.

No nonlinear classifier may replace the primary model. A prespecified nonlinear sensitivity analysis may be added later only under a separate pre-result amendment.

## 12. Identity-aware uncertainty

Bootstrap resampling operates on complete recovered garment identities within category. For each replicate:

1. sample identities with replacement separately inside each category;
2. include every sketch belonging to each sampled identity;
3. preserve paired predictions for all compared models;
4. compute pooled macro-F1 and balanced accuracy;
5. store the paired contrast.

Use 10,000 bootstrap replicates and a frozen seed. Report percentile 95% intervals together with the complete bootstrap distribution or a hash-locked compressed record.

The bootstrap is conditional on the recovered garment identities being the relevant independent sampling units. It does not establish independence among designers, templates, collections, or other unavailable higher-level sources.

## 13. Mechanical validity gate

Predictive interpretation is permitted only after the representation passes a separately reported mechanical gate:

1. algebraic consistency of (F_2\), (R_2\), and doubled-angle orientation;
2. rigid-rotation magnitude invariance within documented interpolation error;
3. doubled-angle axial equivariance;
4. finite-value and range checks for all 14 coordinates;
5. explicit low-support/low-magnitude conditioning diagnostics;
6. identical row ordering and identity mapping across (M\), (G\), (H\), and (L\).

Numerical tolerances must be derived from exact transformations and a frozen raster-rotation test set before downstream prediction is run. Failed mechanical checks must not be hidden by successful classification.

## 14. Leakage prohibitions

The following are prohibited:

- sketch-level random splitting;
- global scaling before fold separation;
- global PCA before fold separation;
- tuning the encoder, classifier, preprocessing, or representation on test-fold outcomes;
- selecting among learned encoders using the primary contrast;
- modifying (G\) after observing its increment beyond (L\);
- using category labels during learned feature extraction;
- treating repeated folds as independent observations;
- reporting the best seed, split, layer, crop, or embedding variant;
- silently excluding failed rows or categories.

Any unavoidable deviation requires a dated amendment written before the affected result is inspected.

## 15. Evidence hierarchy and allowed claims

Claims are governed by the strongest passed level:

| Level | Required evidence | Maximum allowed claim |
|---|---|---|
| 1 | Mechanical gate passes | The representation behaves as mathematically intended under the tested transformations. |
| 2 | Standalone identity-disjoint performance | The representation contains garment-category information under this dataset and protocol. |
| 3 | Positive \(\Delta_{G\mid M}\) | The representation adds information beyond the frozen morphology baseline. |
| 4 | Positive \(\Delta_{G\mid H}\) or \(\Delta_{G\mid L}\) | The representation adds information beyond the named stronger baseline. |
| 5 | Positive increment and significant alignment control | The added information depends on exact recovered garment-level pairing. |
| 6 | Prespecified external-dataset replication | The conclusion transfers to the evaluated external dataset. |

Passing a lower level never licenses a higher-level claim.

## 16. Outcome-contingent interpretation

### Outcome A — Material increment beyond the learned baseline

If the primary confidence interval excludes zero and \(\Delta_{G\mid L}\ge0.01\), the representation may be described as providing practically material complementary information beyond the frozen learned embedding under the locked protocol.

### Outcome B — Positive but small increment

If the interval excludes zero but the increment is below 0.01, the result must be described as detectable but small. Statistical significance must not be translated into practical importance.

### Outcome C — No increment, but compact non-inferiority

If the primary interval includes zero while (G\) is non-inferior to (L^{(14)}\), the contribution becomes compact interpretability: explicit geometry approximates useful structure available in a same-dimensional learned projection.

### Outcome D — No increment and no compact non-inferiority

The representation-performance claim is not supported. The valid scientific result is that apparent complementarity against weaker morphology does not survive stronger representation controls.

### Outcome E — Increment without alignment evidence

The result supports category-conditioned incremental information but not exact garment-specific complementarity.

No outcome may be relabelled post hoc as the originally intended primary success.

## 17. External validation boundary

External validation is desirable but cannot be manufactured from an incompatible dataset. A candidate dataset must provide or permit defensible reconstruction of:

- garment-category labels;
- repeated or source-linked garment identities;
- sufficiently comparable sketch imagery;
- lawful research access;
- enough identities per category for group-disjoint evaluation.

If these conditions are not met, the study remains explicitly single-dataset. Image-level external evaluation without identity control cannot be presented as equivalent evidence.

## 18. Frozen outputs

The implementation must produce, at minimum:

- row and identity maps;
- primary and repeated fold maps;
- feature-extraction manifest and encoder provenance;
- per-fold metrics;
- pooled out-of-fold predictions for every prespecified feature set;
- paired bootstrap distributions and summaries;
- correspondence-permutation distribution and summary;
- compactness comparison;
- mechanical-validation report;
- final decision record mapping results to the claim hierarchy;
- SHA-256 public-evidence manifest.

Headline manuscript values must be generated from these artifacts rather than copied manually.

## 19. Pre-code freeze checklist

Outcome-capable feature extraction or model fitting may begin only after the following are recorded. Non-executing validation scaffolds may be written earlier, but must terminate before extracting learned features or fitting a classifier.

- [~] exact DINOv2 model identifier approved; repository commit and downloaded-weight SHA-256 must be recorded at acquisition;
- [x] exact image preprocessing and pooling rule;
- [x] dataset acquisition and file-order specification;
- [~] authoritative row/identity/fold hash specified; clean-checkout verification remains required;
- [x] bootstrap, permutation, repeated-partition, PCA, and determinism seeds;
- [x] mechanical-test rotations and numerical tolerances;
- [~] software-environment policy approved; resolved package versions and lockfile remain required;
- [x] output schema and manifest format;
- [x] confirmation that no new learned-baseline outcomes have been inspected.

## 20. Freeze declaration

This design is prospective with respect to the new learned-baseline contrasts. Existing morphology, axial–radial, HOG, alignment-control, and diagnostic results are acknowledged as previously observed and cannot be treated as prospectively blind.

After the pre-code checklist is completed, any methodological change must be recorded in a dated amendment stating whether it occurred before or after inspection of the affected outcome. The original design must remain in version history.

### Pre-outcome amendment — peripheral annotation audit

Visual inspection of the preprocessing-only 23-category contact sheet revealed handwritten text outside several garment drawings, including apparent category or source-garment annotations. This was discovered before DINOv2 was applied to any CLO-SKET image and before any Experiment 08 predictive outcome existed.

The full-canvas learned representation is therefore retained only as a prespecified annotation-sensitivity control, denoted (L_{\mathrm{raw}}\). The primary learned representation will use a frozen label-blind geometry mask, denoted (L_{\mathrm{geometry}}\), provided that the mask passes a preprocessing-only preservation audit.

The candidate rule uses no category label, filename text, OCR, learned representation, or outcome. Ink is defined by normalized grayscale intensity below 0.95. After one 3×3 binary-dilation iteration, 8-connected components are scored using ink area, two-dimensional extent, and a fixed centre-distance weight. The highest-scoring component defines the principal garment structure. All original pixels inside its bounding box plus a candidate 5% or 10% proportional margin are retained; pixels outside are set to white. The complete source-canvas dimensions and subsequent 224×224 aspect-ratio-preserving resize/pad convention remain unchanged.

The 5% and 10% margins will be compared only by retained-ink summaries and visual geometry/annotation audit on the prespecified first image of each recovered garment identity. The chosen margin must be frozen before any learned feature is extracted. Raw-versus-geometry learned performance will quantify sensitivity to peripheral canvas information rather than being used to choose the mask.

The first single-component candidates were rejected before feature extraction because both 5% and 10% variants visibly removed approximately half of the garment in the prespecified Cardigan G03 worst-retention case. The rejected candidates remain documented in the audit.

A second pre-outcome candidate therefore defines a multi-component garment envelope. After the same threshold, dilation, and connected-component construction, a component is structural when its height is at least 12.5% of source-image height, it contains at least 1% of total ink, and its normalized centre distance is at most 0.45 of the image diagonal. The union bounding box of all structural components is expanded by 10%, and original pixels inside that box are preserved. If no component qualifies, the earlier principal-component box is used as a recorded fallback. This revision is label-blind and was specified in response to visible geometry truncation, not predictive performance.

## 21. Approved pre-code implementation specification

The following decisions were approved before any Experiment 08 learned embedding or predictive outcome was computed.

### 21.1 Frozen learned encoder

- Primary model identifier: `dinov2_vits14`.
- Architecture: original distilled DINOv2 ViT-S/14 without registers.
- Output: 384-dimensional final normalized class-token embedding.
- Weights: official pretrained backbone only; no pretrained classification head.
- Training status: evaluation mode, frozen weights, no CLO-SKET fine-tuning.
- Pooling: class token only; no patch-token mean, layer concatenation, multi-crop aggregation, or layer selection.
- Provenance gate: the exact DINOv2 source commit, official weight source, downloaded filename, byte size, and SHA-256 must be written to the extraction manifest before the first dataset embedding is produced.

No alternative DINOv2 size, register variant, CLIP model, ResNet model, crop policy, layer, or pooling rule may replace the primary encoder after outcomes are observed.

### 21.2 Frozen image preprocessing

For each source TIFF:

1. apply encoded image orientation metadata;
2. convert deterministically to floating-point grayscale;
3. determine foreground/background polarity using one dataset-independent documented rule;
4. replicate the grayscale channel three times;
5. preserve the complete uncropped source canvas;
6. resize the longest side to 224 pixels with bicubic interpolation;
7. centre-pad the shorter side to (224\times224) using the estimated background value;
8. apply the standard ImageNet channel normalization associated with DINOv2 inference;
9. apply no stochastic or deterministic augmentation beyond the declared resize/pad operation.

Foreground cropping is prohibited. The preprocessing implementation must be tested on synthetic black-on-white and white-on-black images before dataset extraction.

### 21.3 Dataset enumeration and row identity

- Recursively enumerate `.tif` and `.tiff` files case-insensitively.
- Store paths relative to the supplied dataset root.
- Normalize separators to `/` and sort lexicographically.
- Reject duplicate normalized paths.
- Join to the authoritative Paper I row map using explicit category, filename, and recovered-identity fields.
- Require exactly 2,300 rows, 23 categories, 230 identities, and a one-to-one join.
- Record relative path, byte size, SHA-256, category, identity, authoritative row index, and fold ID.
- Stop on any unmatched, duplicated, silently reordered, or non-finite row.

### 21.4 Authoritative folds

The primary fold map must reproduce test-row counts

\[
(459,460,462,460,459),
\]

with 46 held-out identities, 184 training identities, and zero identity overlap per fold. The recorded authoritative fold-array audit hash is

`ccb6138e4bafb9f889c4c7dc92f3a0447c9d17ea870b34fc0f5c9d80ddf809b7`.

The implementation must verify both this hash and the structural counts. It must stop if either check fails.

### 21.5 Frozen random seeds

| Operation | Seed |
|---|---:|
| Primary classifier | `20260820` |
| Category-stratified identity bootstrap | `20260821` |
| Category-preserving alignment permutations | `20260822` |
| Repeated grouped partitions | `20260823` |
| PCA, if a randomized solver is used | `20260824` |
| Determinism audit | `20260825` |

Feature extraction must run without stochastic augmentation. Seed recording does not substitute for environment and deterministic-backend recording.

### 21.6 Coordinate and rotation convention

The frozen RA14 values and historical angular-bin-index convention are preserved. The resulting fixed 2.5° absolute reference offset is disclosed and is not retrospectively corrected inside RA14.

Before dataset-level rotation controls, a synthetic horizontal axis must establish the implementation convention. For Cartesian geometry, image row displacement must be converted using

\[
\Delta y=c_y-y.
\]

A visual counterclockwise rotation by (+30^\circ) must then produce an axial change of (+30^\circ\pmod\pi). If an upstream routine uses native downward-positive image coordinates, that difference must be converted explicitly rather than repaired by changing signs after results are seen.

Analytic transformation tests use

\[
\phi\in\{-90^\circ,-60^\circ,-45^\circ,-30^\circ,-15^\circ,
+15^\circ,+30^\circ,+45^\circ,+60^\circ,+90^\circ\}.
\]

They require

\[
\max|R'_2-R_2|<10^{-12}
\]

and

\[
\max\|u'_2-R(2\phi)u_2\|_2<10^{-12}.
\]

Raster controls use one prespecified sketch per recovered identity and the same rotation angles. A supported shell requires (R_2(r)\ge0.05) and shell foreground mass at least 0.1% of total foreground mass. The frozen descriptive gates are:

- median relative magnitude error at most 5%;
- 95th-percentile relative magnitude error at most 15%;
- median axial error at most 5°;
- 95th-percentile axial error at most 15°.

Low-support shells are reported separately and are not silently removed from the audit.

### 21.7 Environment policy

- Python 3.12 reference environment.
- Exact versions of PyTorch, torchvision, NumPy, pandas, SciPy, scikit-learn, Pillow, and tifffile must be resolved and locked before feature extraction.
- DINOv2 source must be pinned to an exact Git commit.
- Final evidence generation uses a recorded CPU reference execution with deterministic PyTorch algorithms enabled.
- Operating system, processor, thread settings, package lock hash, and model-weight hash are recorded.
- GPU extraction is a permitted acceleration only after a prespecified CPU/GPU embedding concordance audit; final inference remains reproducible on CPU.

### 21.8 Experiment 08 evidence schema

All new artifacts are written under `evidence/Experiment_08/` and must include:

```text
experiment08_design_lock.json
experiment08_environment.json
experiment08_source_manifest.csv
experiment08_row_map.csv
experiment08_fold_map.csv
experiment08_dinov2_manifest.json
experiment08_dinov2_vits14_embeddings.npy
experiment08_primary_results.csv
experiment08_secondary_results.csv
experiment08_fold_metrics.csv
experiment08_oof_predictions.csv
experiment08_identity_bootstrap.csv
experiment08_identity_bootstrap_summary.csv
experiment08_alignment_permutations.csv
experiment08_alignment_summary.csv
experiment08_compactness_results.csv
experiment08_repeated_grouped_cv.csv
experiment08_mechanical_validation.csv
experiment08_final_decision.json
experiment08_public_manifest.json
```

The embedding matrix is included in the public evidence bundle unless an actual repository constraint arises before execution. Every published artifact receives a byte count and SHA-256 entry. Headline manuscript values must be generated from these files.

### Pre-outcome amendment — reviewed localization and architecture-aligned padding (2026-08-26)

This amendment was written before any CLO-SKET DINOv2 embedding, classifier fit, or predictive outcome was computed. It supersedes the complete-canvas prohibition in Section 21.2 for the primary learned representation and supersedes the earlier automatic geometry-mask candidate as the primary localization rule.

Dataset-wide preprocessing review produced frozen garment boxes for all 2,300 sketches: 928 boxes were human reviewed (all 628 mandatory cases plus a deterministic category-stratified quality-control sample of 300), and 1,372 automatic proposals were accepted after the quality-control sample showed zero material failures. Reviewed handwriting boxes are preprocessing metadata, not training targets. All 22 geometric garment/text overlaps received explicit before/after visual approval.

The primary learned representation is now (L_{\mathrm{localized}}). After orientation and polarity normalization, each image is cropped to its frozen reviewed garment box; only the intersections of frozen handwriting boxes with that crop are whitened. The crop is resized bicubically with its longest side equal to 196 pixels and centered on a white (224\times224) canvas. Because DINOv2 ViT-S/14 uses 14-pixel patches, 196 pixels span 14 patches and the remaining 28 pixels provide one 14-pixel patch of border on each side of the longest axis. This rule was selected from preprocessing-only integrity and visual audits, not learned features or outcomes.

DINOv2 feature extraction uses no stochastic or deterministic rotation augmentation. The 14 in RA14 denotes representation dimensionality, and the 14 in ViT-S/14 denotes patch size; neither denotes a 14-degree rotation. The separately frozen RA14 mechanical raster controls retain the angles (-90^circ,-60^circ,-45^circ,-30^circ,-15^circ,+15^circ,+30^circ,+45^circ,+60^circ,+90^circ).

The original complete-canvas representation (L_{\mathrm{raw}}) remains a prespecified annotation-and-localization sensitivity control and cannot replace the amended primary representation based on predictive results. Materialization attempts V1–V3 remain in versioned provenance as preprocessing-development evidence; V3 is explicitly superseded because it incorrectly treated 14 degrees as a rotation limit.


---

## 22. Pre-outcome Experiment 08 fold-map amendment — 2026-08-26

This amendment was recorded before any Experiment 08 classifier was fitted and
before any Experiment 08 predictive outcome was computed.

Section 21.4 records the historical public fold assignment inherited from the
earlier evidence lineage. Its recorded row counts are

\[
(459,460,462,460,459),
\]

with historical fold-array audit hash

`ccb6138e4bafb9f889c4c7dc92f3a0447c9d17ea870b34fc0f5c9d80ddf809b7`.

That historical object is retained unchanged as provenance evidence.

A frozen pre-outcome identity audit subsequently corrected one row-level
identity/fold assignment for Experiment 08 without modifying source images and
without using learned features, classifier predictions, or predictive outcomes.

Therefore, for Experiment 08 only, the active primary fold assignment is the
corrected identity-disjoint map with test-row counts

\[
(459,460,461,460,460).
\]

Each corrected fold contains exactly 46 held-out garment identities and
184 training garment identities, with zero train/test identity overlap.

The active Experiment 08 canonical fold-array SHA-256 is

`e3fb0cf57b886bc303333795de42ecfc38cb1da9728d4d5cc365b47a91504c1f`.

### Execution rule

All Experiment 08 primary and secondary outcome-producing analyses must:

1. preserve the historical fold hash above as provenance only;
2. use the corrected Experiment 08 fold map for model fitting and evaluation;
3. require corrected test-row counts `(459,460,461,460,460)`;
4. require 46 held-out and 184 training identities per fold;
5. require zero train/test identity overlap;
6. require the active Experiment 08 canonical fold-array hash
   `e3fb0cf57b886bc303333795de42ecfc38cb1da9728d4d5cc365b47a91504c1f`;
7. stop execution if any of these corrected structural checks fails.

This amendment supersedes Section 21.4 only with respect to the active
Experiment 08 fold assignment. It does not alter the historical public fold
object or its recorded provenance hash.

At the time of this amendment:

- RA14 extraction was frozen;
- DINOv2 extraction was frozen;
- RA14/DINO row correspondence was verified for all 2,300 sketches;
- no Experiment 08 classifier had been fitted;
- no Experiment 08 predictive outcome had been computed.
