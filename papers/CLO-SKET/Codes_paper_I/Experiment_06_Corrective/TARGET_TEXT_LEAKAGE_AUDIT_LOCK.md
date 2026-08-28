# CLO-SKET Paper I
## Experiment 06 Corrective Reanalysis
## Target-Text Leakage Audit Lock

### Status

POST-OUTCOME INPUT-INTEGRITY AUDIT PROTOCOL, FROZEN BEFORE REVIEW OF THE CLEAN IMAGES FOR TARGET-TEXT LEAKAGE.

The corrected Experiment-06 predictive outcome has already been computed under the previously frozen execution protocol. This audit does not alter, rerun, optimize, or select any predictive model. Its purpose is narrower: determine whether the already-frozen CLEAN image field visibly retains class-identifying garment-category text.

Until this audit is completed, the corrective Experiment-06 outcome must not be treated as fully cleared for manuscript use.

## Question

For each of the 2,300 already-frozen CLEAN images, does visible text remain that directly reveals, abbreviates, or strongly encodes the true garment-category label?

This is distinct from:

- garment-identity leakage;
- generic handwriting/annotation contamination;
- ordinary non-target text;
- morphology or style cues inherent to the sketch itself.

## Frozen source field

The audit inspects only the frozen Experiment-08 materialized-v4 CLEAN images already used by corrective Experiment 06.

The images must not be edited, re-cropped, re-masked, re-rendered, or otherwise changed during this audit.

The authoritative row-order table is:

`papers/CLO-SKET/evidence/Experiment_06_Corrective/experiment06_annotation_status.csv`

The audit script verifies the existing `clean_png_sha256` for every inspected image before rendering review sheets.

## Review population

Primary audit population: all 2,300 CLEAN images.

No sampling-based clearance is permitted for the final target-text leakage conclusion.

## Review labels

Each image receives exactly one target-text status:

- `NONE` — no visible class-identifying target text;
- `EXACT` — the true category name is visibly present;
- `PARTIAL_OR_ABBREVIATED` — a visible abbreviation/partial form strongly identifies the true category;
- `AMBIGUOUS` — visible text may encode the target but cannot be classified confidently.

A separate `other_text_visible` field may record generic non-target text.

## Blinding / display rule

The review sheet shows the true category outside the image tile so the reviewer can compare visible text against the target label. The category caption is not part of the CLEAN image and must never be interpreted as image content.

## Decision rule

After full review:

1. If zero images are `EXACT`, `PARTIAL_OR_ABBREVIATED`, or unresolved `AMBIGUOUS`, target-text leakage is cleared for the frozen CLEAN field.
2. If any such image exists, quantify affected rows, categories, folds, and garment identities before interpreting the corrective Experiment-06 result.
3. No post hoc masking, deletion, or rerun may be described as the original confirmatory analysis. Any later label-sanitized rerun would be explicitly post-outcome sensitivity analysis with separate inferential status.

## Governance

This audit is visual/input-integrity review only.

It must not:

- fit a classifier;
- compute predictions or metrics;
- inspect model coefficients or errors to decide which images to review;
- modify CLEAN images;
- create a new confirmatory result.

The complete review table and summary must be archived before any claim that target-text leakage has been ruled out.
