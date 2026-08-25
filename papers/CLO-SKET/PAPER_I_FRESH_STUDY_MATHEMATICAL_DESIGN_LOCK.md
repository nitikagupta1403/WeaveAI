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

Under an ideal rigid rotation by (\phi), the adopted convention requires

\[
F'_{2,i}(r)=e^{-2\mathrm{i}\phi}F_{2,i}(r),
\]

and therefore

\[
R'_{2,i}(r)=R_{2,i}(r),
\qquad
\alpha'_{2,i}(r)=\alpha_{2,i}(r)+\phi\pmod{\pi}.
\]

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

Coding may begin only after the following are recorded:

- [ ] exact DINOv2 model identifier and immutable weight provenance;
- [ ] exact image preprocessing and pooling rule;
- [ ] dataset acquisition and file-order specification;
- [ ] authoritative row/identity/fold hash verification;
- [ ] bootstrap, permutation, and repeated-partition seeds;
- [ ] mechanical-test rotations and numerical tolerances;
- [ ] software environment specification;
- [ ] output schema and manifest format;
- [ ] confirmation that no new learned-baseline outcomes have been inspected.

## 20. Freeze declaration

This design is prospective with respect to the new learned-baseline contrasts. Existing morphology, axial–radial, HOG, alignment-control, and diagnostic results are acknowledged as previously observed and cannot be treated as prospectively blind.

After the pre-code checklist is completed, any methodological change must be recorded in a dated amendment stating whether it occurred before or after inspection of the affected outcome. The original design must remain in version history.
