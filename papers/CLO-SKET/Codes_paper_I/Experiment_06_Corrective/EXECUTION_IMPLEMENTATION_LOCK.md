# Experiment 06 Corrective Reanalysis — Execution Implementation Lock

## Status

**PRE-OUTCOME IMPLEMENTATION LOCK.**

This document is subordinate to `../Experiment_06_Corrective_Reanalysis_PROSPECTIVE_LOCK.md` and to the already frozen Phase-1A and Phase-1B evidence. It defines the final implementation boundary that must be committed before any corrected Experiment-06 predictive outcome is computed.

The historical submission candidate at `60063623eedde05ed7c351c3c947a605f6be5344` remains provenance only.

## Already frozen prerequisites

The corrective execution must consume, without modification:

- corrected 2,300-row identity map SHA-256 `c2510fb74b452da22d3b4e9badb46cfe4cbd2653c0ee99acb573942262c1ac2b`;
- corrected identity/fold-map SHA-256 `82cda5ce42be46cb939bf15b50171d21c2b62df3d3e065eb8a32bc4e587cca3b`;
- corrected fold-summary SHA-256 `7d0df33b09f9e47857877003e7d59705d87e9b922a8cf21a2c8a9c4889bef0d7`;
- frozen Experiment-08 preprocessing-manifest SHA-256 `c464feafbb382c8e9d111433047298d8f42e1c661e018735e3df0b6016eaff4d`;
- frozen materialized CLEAN manifest SHA-256 `071ee7b6c535361951f9eb0044ff166c9a4d42b0ef55a3c0a72aab27af2af6a4`;
- ordered CLEAN pixel-field SHA-256 `30006ee3661f18b4cc3925c753c2ada6e3eb6ea7bf7f56326e5edf7cb7be5703`;
- corrective annotation-status SHA-256 `b83b74b6ff0f25fa8bb4474265d2f06c900bbcd3243b2cc332152e3c74cde55e`.

Any mismatch is a hard stop.

## Scientific execution contract

The corrective analysis answers the same frozen primary question. It may not change the target, representation definitions, model family, hyperparameters, fold unit, primary contrast, bootstrap count, repeated-partition count, or alignment-permutation count after outcome exposure.

Two preprocessing conditions are permitted and only these two:

1. **RAW diagnostic** — original native TIFF canvas, corrected identity/fold map.
2. **CLEAN confirmatory** — frozen annotation-controlled v4 garment field, same corrected identity/fold map.

The CLEAN condition is the sole confirmatory condition. RAW is a prespecified annotation-sensitivity diagnostic.

## Representation contract

For each condition, one row order must be shared by all feature blocks.

- `M`: 135-D lower-performing frozen morphology baseline = 64 horizontal occupancy coordinates + 64 vertical occupancy coordinates + 7 historical global morphology/statistical coordinates.
- `R`: 8 frozen radial descriptors.
- `A`: 6 frozen axial descriptors.
- `RA14 = R+A`: 14 dimensions.
- Primary augmented representation: `M+R+A`, 149 dimensions.

RA14 mathematics, radial shells, second-harmonic convention, doubled-angle encoding, orientation sign convention, and descriptor formulas are unchanged. The only permitted difference between RAW and CLEAN feature extraction is the input image field.

The same image field must feed M and RA14 within a preprocessing condition. Representation-specific cleaning is prohibited.

## Historical implementation sources

The implementation must be reconstructed from the committed historical source materials, not redesigned from memory. At minimum the implementation preflight records hashes for:

- `01_Core_Radial_Angular_14D_and_Reconstruction.ipynb`;
- `06_Experiment_06_Evidence_Record.md`;
- any historical morphology extractor actually used to reproduce the 135-D comparator;
- the final corrective extractor and runner once created.

If the exact seven global morphology coordinates cannot be recovered unambiguously from committed provenance/code, predictive execution remains blocked. No substitute seven descriptors may be invented.

## Estimator contract

For every feature set used in the corrective run:

- fold-local `StandardScaler` fitted on training rows only;
- `LogisticRegression`;
- L2 penalty;
- `C=1.0`;
- `solver="lbfgs"`;
- `max_iter=5000`;
- `class_weight=None`;
- `random_state=20260820`.

No hyperparameter search, model selection, calibration, class weighting, or feature-set-specific estimator change is permitted.

## Primary fold contract

The already frozen corrected fold assignments are authoritative. The primary run uses five folds and must reproduce these test-row counts exactly:

- Fold 0: 459;
- Fold 1: 460;
- Fold 2: 461;
- Fold 3: 460;
- Fold 4: 460.

Each fold has exactly 46 test identities and zero corrected-identity train/test overlap.

## Output contract

Before outcome execution, the runner must have fixed output paths/contracts for at least:

- RAW M matrix `(2300,135)`;
- RAW RA14 matrix `(2300,14)`;
- CLEAN M matrix `(2300,135)`;
- CLEAN RA14 matrix `(2300,14)`;
- row-order manifest for each condition;
- feature SHA-256 manifest;
- row-level OOF predictions for M and M+R+A under RAW;
- row-level OOF predictions for M and M+R+A under CLEAN;
- pooled and foldwise macro-F1 and balanced accuracy;
- prespecified RAW-versus-CLEAN annotation-impact table;
- CLEAN category-stratified corrected-identity bootstrap, B=5000;
- retained alignment permutation, if executed, B=2000;
- retained repeated grouped partitions, if executed, seeds 20260820..20260829.

All outcome-bearing files are written only after an explicit execution unlock.

## Hard outcome gate

The corrective implementation must default to an outcome-disabled state. A preflight may inspect files, hashes, schemas, package versions, row order, feature dimensions on synthetic/self-test data, and deterministic mathematical unit tests, but it must not fit on CLO-SKET labels or produce predictive metrics.

The first real corrected outcome may be computed only after all of the following are true and committed:

1. Phase-1A identity correction PASS is frozen;
2. Phase-1B annotation-control PASS is frozen;
3. the exact 135-D historical comparator definition is recovered and documented;
4. a single RAW/CLEAN feature extractor exists;
5. the corrective runner exists with the estimator/fold/output contract above;
6. environment/package versions are recorded;
7. implementation hashes are recorded by `03_execution_lock_preflight.py`;
8. the implementation-preflight report says `preflight_passed=true` and `predictive_outcome_computed=false`;
9. that report and the implementation files are committed before the outcome command is run.

If any item is unresolved, **STOP**.

## Decision rule after unlock

The CLEAN corrected-map primary increment controls the paper:

- positive with corrected-identity bootstrap interval excluding zero: confirmatory positive incremental utility may be reported;
- positive with interval including zero: evidence is uncertain;
- zero or negative: positive confirmatory utility claim is abandoned.

E07 HOG and E08 DINOv2 remain inferentially separate and cannot rescue an unfavorable E06 correction.
