# CLO-SKET IVC — Experiment 07 Evidence Lock

## Status

Experiment 07 is complete and frozen. It is a secondary conventional-image-descriptor comparator and does not modify Experiment 06.

## Frozen design

- Dataset: 2,300 CLO-SKET sketches, 230 recovered garment identities, 23 categories.
- Validation: authoritative Experiment 06 row-level `fold_id`; test-row counts 459, 460, 462, 460, 459; 46 held-out identities per fold; zero train/test identity overlap.
- Conventional descriptor: HOG on a 256×256 white canvas after aspect-ratio-preserving bilinear resize and centered padding.
- HOG: 9 orientations; 16×16-pixel cells; 2×2-cell blocks; L2-Hys; `transform_sqrt=False`; 8,100 dimensions.
- Added representation: unchanged frozen Experiment 06 RA14 matrix (8 radial + 6 axial coordinates).
- Estimator: fold-local `StandardScaler` + L2 `LogisticRegression(C=1.0, solver=lbfgs, max_iter=5000, class_weight=None, random_state=20260820)`.
- Hyperparameter search: none.
- PCA / feature selection: none.
- Augmentation: none.
- Outcome-dependent descriptor change: none.

## Provenance hashes

- Experiment 06 final checkpoint SHA-256: `6e2c600c9cef37c3edcae18300793e37265ba866ee93d83c825aa1b5ad522018`
- Runtime backup SHA-256: `4e7d6ea942b3fd4b506c330f624178e154022683756e6edcffcf7aa65bd69f9f`
- Frozen RA14 array audit hash: `b2f46821d0784c519ab10780dcd4414e9a79e4aee94a5bdbff2a47bdfa334421`
- Frozen HOG array audit hash: `6f450f651ea8e72853f8faf401f4d531c2d70d28b4c364b9bf22650e74f4a00d`
- Frozen HOG `.npy` SHA-256: `b76a655de4cb487d7ae130ee730b90709d12024c0e9b6ccb0f2408cda7c99b17`
- Authoritative fold-array audit hash: `ccb6138e4bafb9f889c4c7dc92f3a0447c9d17ea870b34fc0f5c9d80ddf809b7`

The checkpoint fold map was accepted as authoritative only after it reproduced the locked Experiment 06 pooled results to numerical precision:

- M macro-F1: 0.29778797162313025
- M balanced accuracy: 0.2982608695652173
- M+R+A macro-F1: 0.3357646054136369
- M+R+A balanced accuracy: 0.3360869565217391

## Frozen Experiment 07 results

| Feature set | Dimensions | Macro-F1 | Balanced accuracy |
|---|---:|---:|---:|
| HOG | 8,100 | 0.648242 | 0.650435 |
| HOG + RA14 | 8,114 | 0.649135 | 0.651304 |

Primary secondary contrast:

- Δ Macro-F1 = +0.000894
- Δ balanced accuracy = +0.000870

## Paired garment-identity bootstrap

- Unit: garment identity.
- Replicates: 5,000.
- Seed: 20260820.
- Paired resampling: yes.
- Model refitting: no.

| Metric | Observed Δ | Bootstrap mean Δ | 95% identity-level interval | Fraction positive |
|---|---:|---:|---:|---:|
| Macro-F1 | +0.000894 | +0.000961 | [−0.002152, +0.004342] | 0.7282 |
| Balanced accuracy | +0.000870 | +0.000912 | [−0.002238, +0.004272] | 0.7110 |

Both percentile intervals include zero. The frozen interpretation is therefore **no clear evidence of incremental predictive benefit from RA14 over HOG under the tested protocol**.

## Claim boundary

Experiment 07 does not negate Experiment 06. It establishes that the incremental predictive contribution of RA14 is baseline-dependent. RA14 adds a materially larger increment to the 135-dimensional morphology representation but is nearly redundant for category discrimination once the 8,100-dimensional HOG descriptor is present. The manuscript must not claim universal predictive superiority or general-purpose complementarity of RA14.

## Expected generated local artifacts

The following local artifacts were produced under the frozen run and should be included in the eventual public evidence bundle before any code-availability claim is made:

- `experiment07_hog_features.npy`
- `experiment07_row_map.csv`
- `experiment07_fold_map.csv`
- `experiment07_feature_extraction_manifest.json`
- `experiment07_primary_results.csv`
- `experiment07_contrast_results.csv`
- `experiment07_fold_metrics.csv`
- `experiment07_oof_predictions.csv`
- `experiment07_final_manifest.json`
- `experiment07_identity_bootstrap.csv`
- `experiment07_identity_bootstrap_summary.csv`
- `experiment07_identity_bootstrap_manifest.json`

Do not rerun with altered HOG parameters, altered folds, altered RA14 coordinates, or post-outcome hyperparameter tuning.
