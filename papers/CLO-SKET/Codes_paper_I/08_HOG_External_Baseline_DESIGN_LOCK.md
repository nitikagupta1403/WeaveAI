# Experiment 07 — Conventional image-descriptor baseline — design lock

## Status

**LOCKED BEFORE OUTCOME COMPUTATION.**

This experiment is a secondary reviewer-facing comparator. It does not modify, replace, retune, or reopen Experiment 06, the frozen 14-dimensional axial–radial representation, the frozen 135-dimensional morphology representation, or any previously reported result.

## Scientific question

Does the frozen 14-dimensional axial–radial representation add category-discrimination information to a conventional image-gradient descriptor under the same garment-identity-disjoint validation logic used for Experiment 06?

The experiment is not designed to show that the proposed representation “beats HOG.” The relevant comparison is the incremental contrast

\[
\Delta_{HOG+RA}=F_1^{macro}(HOG+RA_{14})-F_1^{macro}(HOG).
\]

Balanced accuracy is secondary.

## Frozen dataset and validation requirements

- 2,300 CLO-SKET TIFF sketches.
- 23 garment categories.
- 230 recovered garment identities, exactly 10 per category.
- The **same five deterministic category-balanced garment-identity-disjoint folds used by Experiment 06**.
- 46 complete garment identities in each test fold, exactly two per category.
- Zero train/test garment-identity overlap.
- Every sketch receives exactly one out-of-fold prediction.
- Pooled out-of-fold macro-F1 is primary; pooled balanced accuracy is secondary.

The Experiment-07 code must not silently reconstruct a different fold assignment. Before any model fit, the exact frozen fold map must be loaded from a verified artifact or reproduced from a verified Experiment-06 source and checked against the Experiment-06 fold-size/identity constraints.

## Frozen axial–radial input requirement

`RA14` must be the exact frozen 2,300 × 14 representation used in Experiment 06, in the identical sketch-row order. Before any model fit, its row order and content must be verified from a frozen artifact or from the canonical measurement code with a stored hash/identity check. Experiment 07 must not redefine or optimize any axial–radial feature.

## HOG preprocessing lock

HOG is baseline-specific preprocessing only; it is not applied to the proposed axial–radial representation.

For each grayscale TIFF:

1. retain grayscale intensity;
2. preserve image aspect ratio;
3. resize so the longer image side is 256 pixels;
4. center the resized image on a 256 × 256 white canvas (`255`);
5. do not geometrically stretch the image;
6. compute HOG on this fixed canvas with:
   - orientations = 9;
   - pixels_per_cell = (16, 16);
   - cells_per_block = (2, 2);
   - block_norm = `L2-Hys`;
   - transform_sqrt = False;
   - feature_vector = True;
   - channel_axis = None.

No HOG parameter search, image augmentation, thresholding, binarization, foreground segmentation, rotation normalization, or learned preprocessing is permitted.

## Compared feature sets

Primary Experiment-07 comparison:

- `HOG`
- `HOG + RA14`

For contextual reporting only, the already frozen Experiment-06 values for `M` and `M+RA14` may be quoted from the Experiment-06 evidence record; they are not recomputed or used to tune Experiment 07.

## Estimator lock

Exactly the Experiment-06 classifier specification:

- training-fold `StandardScaler`;
- `LogisticRegression`;
- L2 penalty;
- `C=1.0`;
- `solver="lbfgs"`;
- `max_iter=5000`;
- `class_weight=None`;
- `random_state=20260820`.

No hyperparameter search, feature selection, dimensionality reduction, classifier replacement, or feature-set-specific estimator change.

## Outcome policy

The experiment is run once after all input/fold checks pass. Whatever result occurs is retained and reported.

Possible outcomes are interpreted symmetrically:

- positive `HOG+RA14 − HOG`: evidence that the compact representation adds predictive utility to this conventional descriptor under the tested protocol;
- near-zero increment: no evidence of additional utility relative to HOG under this protocol;
- negative increment: adding RA14 reduces performance relative to HOG under this protocol.

No result changes the already frozen Experiment-06 conclusion.

## Prohibited post-outcome actions

After the primary Experiment-07 outcome is observed, do not:

- alter HOG parameters;
- alter canvas size;
- alter folds;
- alter `RA14`;
- select a different conventional descriptor because the result is unfavorable;
- change the classifier specification;
- remove difficult categories or identities;
- relabel the analysis as prespecified if its design was changed after seeing results.

Any later sensitivity analysis must be explicitly labeled post hoc and kept inferentially separate from this locked comparator.
