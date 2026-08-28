# Experiment 06 Corrective Reanalysis — Annotation-Control Reuse Lock

## Status

**PRE-OUTCOME / NO-PREDICTIVE-ANALYSIS LOCK.**

This lock fixes the annotation-controlled image field for the corrective Experiment-06 analysis before any corrected Experiment-06 feature matrix, classifier fit, prediction, score, bootstrap interval, permutation statistic, or RAW-versus-CLEAN diagnostic is computed.

## Scientific purpose

The audited historical Experiment-06 candidate measured RA14 and the 135-D morphology comparator from native canvases containing non-garment handwriting. The corrective confirmatory analysis therefore requires a common garment-only measurement field for both representations.

The corrective analysis will **not invent or tune a new cleaning rule after seeing the historical Experiment-06 outcome**. Instead it reuses, without modification, the already-frozen Experiment-08 preprocessing/materialization policy that was selected from image geometry and annotation evidence before the Experiment-08 learned baseline was computed.

This reuse decision is made before any corrected Experiment-06 outcome is computed.

## Frozen clean-field source

The clean image field is defined by the exact Experiment-08 preprocessing/materialization v4 artifacts:

- preprocessing manifest SHA-256: `c464feafbb382c8e9d111433047298d8f42e1c661e018735e3df0b6016eaff4d`;
- materialized manifest SHA-256: `071ee7b6c535361951f9eb0044ff166c9a4d42b0ef55a3c0a72aab27af2af6a4`;
- ordered 2,300-image pixel-array SHA-256: `30006ee3661f18b4cc3925c753c2ada6e3eb6ea7bf7f56326e5edf7cb7be5703`.

The frozen policy is:

1. apply encoded orientation;
2. convert to grayscale and use the frozen polarity normalization;
3. crop to the frozen garment box;
4. whiten every reviewed handwriting-box intersection with the garment crop;
5. resize the localized garment field with the frozen deterministic rule;
6. center on a white canvas;
7. use the resulting identical clean image as input to both RA14 and the 135-D morphology extractor.

No representation-specific cleaning is permitted.

## Existing review evidence preserved

The frozen Experiment-08 preprocessing evidence records:

- 2,300 total images;
- 928 human-reviewed images;
- 1,372 automatic-remainder images retained after the frozen deterministic QC procedure;
- 593 reviewed handwriting boxes;
- 22 ambiguous geometric garment/text overlaps;
- all 22 ambiguous overlaps received explicit before/after visual approval before the learned Experiment-08 analysis.

These historical preprocessing records are reused as preprocessing provenance only. Experiment-08 predictive results have no role in selecting, modifying, or validating the corrective Experiment-06 cleaning rule.

## Corrective Experiment-06 binding

The clean field must be joined one-to-one to the already-frozen corrected Experiment-06 identity map:

`papers/CLO-SKET/evidence/Experiment_06_Corrective/experiment06_corrected_identity_map.csv`

Frozen corrected identity-map SHA-256:

`c2510fb74b452da22d3b4e9badb46cfe4cbd2653c0ee99acb573942262c1ac2b`

The annotation preflight must verify:

- exactly 2,300 rows;
- exact row indices `0..2299`;
- exact path/order agreement across corrected identity map, preprocessing manifest, and materialized manifest;
- exact frozen hashes above;
- physical presence of all 2,300 materialized clean images;
- per-image PNG and pixel hashes;
- exact ordered pixel-array hash;
- generation of a 2,300-row Experiment-06 annotation-status table.

## Annotation-status table

For every row the preflight records at minimum:

- row index and relative source path;
- category;
- corrected garment identity and corrected fold;
- whether a reviewed annotation box is present;
- reviewed annotation-box count;
- whether the frozen review marked a geometric garment/text overlap;
- garment-only field source;
- selection/review cohort;
- localization source;
- reviewer status (`human_reviewed` or `automatic_remainder_after_frozen_qc`);
- clean-image path;
- clean PNG SHA-256;
- clean pixel SHA-256;
- source-image SHA-256.

The table does not claim that every one of the 2,300 images underwent individual human handwriting review. It transparently distinguishes the 928 reviewed images from the 1,372 automatic remainder accepted under the frozen QC design.

## No new annotation optimization

After this lock:

- no crop, mask, handwriting-removal rule, margin, threshold, or reviewer decision may be changed based on corrected Experiment-06 outcomes;
- no alternate clean-field candidate may replace this field because it yields a more favorable predictive result;
- any subsequently discovered source-integrity defect must be handled transparently as a data-quality issue and must not be resolved using predictive performance.

## RAW diagnostic versus CLEAN confirmatory analysis

After the entire pre-outcome corrective checkpoint is frozen, two corrected-map conditions remain prespecified:

- **RAW diagnostic:** native historical canvases with the corrected identity/fold map;
- **CLEAN confirmatory:** the exact frozen clean image field defined by this lock with the same corrected identity/fold map.

RAW is diagnostic only. CLEAN governs the corrected confirmatory claim regardless of whether RAW produces a larger or smaller increment.

## Stop boundary

Passing `02_annotation_control_preflight.py` authorizes only the statement that the corrected identity map and clean-image field are frozen and internally consistent.

It does **not** authorize immediate predictive execution until the remaining pre-outcome items are also frozen, including the end-to-end feature-extraction implementation, estimator implementation, environment lock, output contract, bootstrap implementation, and final execution manifest required by the main prospective lock.
