# Experiment 06 Corrective Reanalysis — Prospective Scientific Lock

## Status

**PROSPECTIVE / PRE-OUTCOME LOCK.**

This document defines the minimum corrective analysis required before Paper I can again make a confirmatory claim about the incremental predictive utility of RA14 under true garment-identity-disjoint validation and garment-only sketch geometry.

The prior submission candidate at commit `60063623eedde05ed7c351c3c947a605f6be5344` remains immutable historical provenance. It must not be edited or retrospectively relabeled as the corrected analysis.

No corrected Experiment-06 predictive outcome may be inspected, computed, summarized, or used to alter this protocol before the preprocessing artifacts, corrected identity map, fold map, and implementation hashes required below are frozen and committed.

## Why this corrective analysis is necessary

The frozen candidate was independently audited and found to contain two candidate-internal defects that invalidate its confirmatory framing:

1. **True garment-identity leakage.** Two sketches were historically assigned to incorrect recovered garment groups, placing true same-garment peers across fold boundaries despite zero overlap under the historical identifiers.
2. **Canvas-annotation contamination.** Experiment 06 measured RA14 and the 135-D morphology comparator from native sketch canvases in which non-garment handwriting can contribute to the foreground measurement field.

The purpose of this correction is not to strengthen the result. It is to answer the **same frozen scientific question** under a valid identity map and an outcome-blind garment-only measurement field.

## Frozen scientific question

Does the frozen 14-dimensional axial-radial representation add garment-category predictive utility beyond the frozen 135-dimensional morphology representation when validation withholds complete **corrected true source-garment identities** and both representations are computed from an **annotation-controlled garment-only measurement field**?

The primary contrast remains

\[
\Delta F_1 = F_1^{\mathrm{macro}}(M+R+A)-F_1^{\mathrm{macro}}(M),
\]

with pooled out-of-fold balanced-accuracy difference secondary.

No alternative target, model family, hyperparameter search, feature-selection procedure, additional predictive baseline, or outcome-dependent preprocessing choice may be introduced into the confirmatory correction.

## Frozen representation definitions

The original compact representation remains unchanged:

- `R`: 8 radial descriptors;
- `A`: 6 axial descriptors;
- `R+A`: 14 RA14 descriptors;
- `M`: 135 morphology coordinates;
- `M+R`: 143 coordinates;
- `M+A`: 141 coordinates;
- `M+R+A`: 149 coordinates.

RA14 mathematics, shell definitions, second-harmonic convention, doubled-angle encoding, radial summaries, and rotation sign convention must remain unchanged except that their input measurement field is the annotation-controlled garment-only image defined below.

The 135-D comparator must be described explicitly as the **lower-performing frozen morphology baseline** consisting of:

- 64 horizontal occupancy-profile coordinates;
- 64 vertical occupancy-profile coordinates;
- 7 frozen global morphology/statistical coordinates as implemented by the historical Experiment-06 extractor.

The corrective analysis must not redesign this baseline.

## Corrected garment-identity map

The corrected recovered garment identities are the validation unit.

At minimum, the authoritative corrected map must encode the two pre-outcome corrections already documented in the repository audit:

- `Dress/1-3.tif`: historical `DressG01` / historical Fold 0 -> corrected `DressG10` / corrected Fold 4;
- `Harem/6-6.tif`: historical `HaremG06` / historical Fold 2 -> corrected `HaremG02` / corrected Fold 0.

These fold reassignments follow the corrected identities so that each corrected source garment remains indivisible within one fold.

Before any predictive outcome is computed:

1. the complete 2,300-row corrected identity table must be deposited;
2. every row must have exactly one category, corrected garment identity, and fold assignment;
3. exactly 230 recovered garment identities must be represented, 10 per category, unless a pre-outcome data-integrity audit demonstrates that this count itself must be corrected;
4. a machine check must verify zero corrected-garment train/test overlap for every fold;
5. the corrected identity table and resulting fold array must each receive SHA-256 hashes recorded in a provenance manifest.

If the corrected identity audit reveals any additional ambiguous or incorrect garment groupings, those must be resolved **before** fold generation and before any predictive outcome is computed. Resolution must use visual/source evidence only, never model performance.

## Fold-generation lock

Primary validation remains five category-balanced grouped folds with corrected garment identity as the indivisible grouping unit.

The fold-generation algorithm must be frozen and deterministic before outcomes are computed. It must target:

- 5 folds;
- category balance;
- complete corrected garment identities assigned wholly to one fold;
- no corrected garment identity appearing in both train and test for any split.

The resulting fold map is to be treated as the single confirmatory fold map for this corrective analysis.

Repeated grouped-partition analyses, if retained for continuity with the historical study, remain robustness analyses and must use corrected garment identities. Their seeds and generation rule must be frozen before outcomes are inspected.

## Annotation-control lock

### Measurement target

Both RA14 and the 135-D morphology baseline must be computed from the **same garment-only foreground field**. Non-garment handwriting, labels, page marks, and other canvas artifacts must not contribute to the foreground mass used by either representation.

### Outcome blindness

Annotation control must be completed without access to Experiment-06 class predictions, foldwise scores, pooled scores, RA14-vs-baseline deltas, bootstrap intervals, or any other corrected predictive outcome.

### Complete image audit

All 2,300 source TIFFs must receive an annotation-status record before predictive analysis. Each record must state at least:

- annotation present: yes/no;
- annotation overlaps or touches garment strokes: yes/no;
- garment-only mask/crop source;
- reviewer status;
- final mask hash.

### Garment-only field creation

The correction must preserve garment strokes while excluding non-garment annotation.

For annotations spatially separable from the garment, an outcome-blind mask or crop may remove only the non-garment annotation while retaining the garment sketch.

For annotations that touch, cross, or are inseparable from garment strokes, the garment-only mask must be manually adjudicated from the image by reviewers who are blinded to Experiment-06 predictions and performance. The adjudication is a preprocessing/data-quality task, not a predictive-analysis decision.

The same final garment-only mask must be supplied to both the RA14 and morphology extractors. A representation-specific cleaning rule is prohibited.

### Reliability and provenance

At least two independent reviewers should adjudicate ambiguous overlap cases where feasible. Disagreements must be resolved before outcomes are computed and recorded in a preprocessing manifest.

All final garment-only masks or equivalent deterministic preprocessing artifacts must be frozen, hashed, and committed before feature extraction for the corrective confirmatory run.

No cleaning rule may be changed after corrected predictive outcomes are inspected.

## Prespecified raw-versus-clean annotation diagnostic

Because the historical raw-canvas Experiment-06 result is confounded simultaneously by the historical identity map and annotation exposure, it must **not** be used by itself as the quantitative annotation-effect comparator.

To isolate the effect of annotation control under the repaired validation design, the corrective package will compute, after the full pre-outcome checkpoint is frozen, two runs using the **same corrected identity map, same corrected folds, same estimator, same row order, and same representation definitions**:

1. **Corrected-map RAW diagnostic:** features re-extracted from the original native canvases without annotation removal, using corrected true garment identities and corrected folds. This run is diagnostic/sensitivity evidence only and cannot support the garment-only construct claim.
2. **Corrected-map CLEAN confirmatory run:** features re-extracted from the frozen annotation-controlled garment-only field, using the identical corrected identities and corrected folds. This is the sole confirmatory corrected Experiment-06 analysis.

The prespecified annotation-impact table will report, for `M` and `M+R+A` at minimum:

- pooled macro-F1 under corrected-map RAW;
- pooled macro-F1 under corrected-map CLEAN;
- pooled balanced accuracy under corrected-map RAW;
- pooled balanced accuracy under corrected-map CLEAN;
- the RA14 incremental contrast `M+R+A - M` in each preprocessing condition;
- CLEAN minus RAW change in the absolute baseline score;
- CLEAN minus RAW change in the absolute augmented score;
- CLEAN minus RAW change in the incremental contrast.

These quantities are descriptive diagnostics of annotation sensitivity. No additional hypothesis test, threshold, optimization, or preprocessing selection will be introduced based on them. The CLEAN confirmatory result governs the manuscript's corrected scientific claim regardless of whether the RAW diagnostic looks better or worse.

The existing historical raw-canvas / historical-map result remains provenance only and may be shown separately as the superseded candidate result; it is not a clean estimate of annotation impact.

## Estimator lock

The historical estimator specification remains fixed:

- training-fold `StandardScaler`;
- `LogisticRegression`;
- L2 penalty;
- `C=1.0`;
- `solver="lbfgs"`;
- `max_iter=5000`;
- `class_weight=None`;
- `random_state=20260820`.

No hyperparameter search or feature-set-specific classifier change is permitted.

## Primary and secondary outcomes

Primary outcome:

- pooled out-of-fold macro-F1 difference `M+R+A - M` from the **corrected-map CLEAN confirmatory run**.

Secondary outcome:

- pooled out-of-fold balanced-accuracy difference `M+R+A - M` from the **corrected-map CLEAN confirmatory run**.

The analysis must report the absolute scores of both feature sets as well as the differences.

All five primary fold-level differences must be reported descriptively regardless of sign.

The corrected result is reportable whether positive, null, or negative.

## Uncertainty lock

The identity bootstrap remains a **paired uncertainty analysis conditional on the frozen out-of-fold predictions**. It must not be described as incorporating model-refitting uncertainty.

If the historical category-stratified bootstrap is retained:

- resampling unit: complete corrected garment identity;
- resampling within garment category;
- paired baseline and augmented OOF predictions retained together;
- replicates: 5,000;
- percentile 95% interval;
- macro-F1 primary, balanced accuracy secondary.

The unrestricted historical bootstrap may be retained only as a labeled robustness audit and must not replace the category-stratified corrected-identity result.

## Alignment-permutation lock

If repeated after the corrective primary analysis, the category-preserving alignment permutation must preserve corrected identity blocks and block sizes within category and use the same corrected primary fold map.

Its interpretation is strictly:

> whether the observed incremental utility is unusually dependent on exact garment-level morphology–RA14 correspondence relative to category-preserving misalignment.

A high upper-tail permutation probability may support the statement that the observed gain is **compatible with category-conditioned distributional structure**. It must not be used to claim that category structure is sufficient to explain the improvement.

Permutation count remains 2,000 if this control is retained.

## Repeated grouped-partition robustness

If retained, the historical ten-repeat grouped-partition robustness analysis must use the corrected garment identities and a prospectively frozen deterministic seed schedule. It remains a robustness analysis, not a second confirmatory endpoint.

For continuity, the historical seed schedule `20260820` through `20260829` should be reused unless the implementation makes that impossible. Any unavoidable change must be documented before outcomes are computed.

## Reproducibility requirements before manuscript revision

The corrected Experiment-06 package must be end-to-end auditable from source images to reported outcomes. At minimum it must deposit:

- corrected 2,300-row identity table;
- corrected fold map;
- annotation-status table for all 2,300 images;
- frozen garment-only masks or deterministic equivalent preprocessing artifacts;
- preprocessing manifest and hashes;
- frozen corrected-map RAW feature matrices used for the annotation diagnostic;
- frozen corrected-map CLEAN 135-D morphology matrix and 14-D RA14 matrix with identical row order;
- feature-matrix hashes;
- environment/package lock;
- executable feature-extraction code;
- executable five-fold model-fitting code;
- row-level OOF predictions for `M` and `M+R+A` for both RAW diagnostic and CLEAN confirmatory conditions;
- primary pooled and foldwise metric outputs;
- prespecified raw-versus-clean annotation-impact table;
- bootstrap code and output for the CLEAN confirmatory analysis;
- any retained alignment/permutation and repeated-partition code/output;
- final manifest connecting every manuscript number to an immutable artifact.

A verifier that checks only hashes is not sufficient by itself; a clean rerun path must exist.

## Decision rule and claim discipline

No minimum positive effect size is required for scientific acceptability. The corrected analysis answers the frozen question; the manuscript must follow the result.

### If the corrected primary increment remains positive with an interval excluding zero

The manuscript may support a confirmatory claim of incremental predictive utility under corrected identity-disjoint, annotation-controlled validation, subject to appropriate baseline, novelty, and uncertainty wording.

### If the corrected primary increment is positive but its interval includes zero

The manuscript must describe the incremental evidence as uncertain under the corrected confirmatory analysis. Historical positive Experiment-06 results may be reported only as superseded historical results, not as confirmatory rescue evidence.

### If the corrected primary increment is zero or negative

The manuscript must report that outcome and abandon the confirmatory positive-utility claim. Experiment 07 and Experiment 08 must not be promoted to rescue it.

No additional predictive experiment may be initiated solely because the corrected result is unfavorable without a new, separately justified prospective scientific question and lock.

## Novelty and manuscript repair boundary

The corrective analysis does not restore broad novelty claims for radial-angular or Fourier shape representation. Manuscript revision must independently narrow contribution claims relative to MPEG-7 ART, Generic Fourier Descriptor, angular-radial sketch/shape descriptors, angular-radial edge histograms, shape contexts, phase-aware ART, and related polar/Fourier descriptors.

The defensible contribution to test after correction is the specific compact shell-conditioned second-harmonic 14-D axial-radial formulation and its dependency-aware evaluation framework, not radial-angular representation as a general class.

## Experiment-07 and Experiment-08 boundary

Experiment 07 remains a secondary conventional HOG baseline and cannot rescue Experiment 06.

Experiment 08 failed its prospective mechanical gate. Predictive outputs already frozen before gate reconciliation and all later Experiment-08 predictive evidence remain exploratory/post-outcome. None may be reclassified as confirmatory support for the corrected Experiment-06 question.

## Governance checkpoint

Before running either the corrected-map RAW diagnostic or the corrected-map CLEAN confirmatory predictive analysis, the repository must contain a committed pre-outcome checkpoint containing:

1. this protocol;
2. corrected identity table and fold map;
3. complete annotation-control manifest and garment-only preprocessing artifacts;
4. executable corrective Experiment-06 script supporting both prespecified preprocessing conditions;
5. environment lock;
6. hashes of the input row order, deterministic preprocessing artifacts, feature-generation implementation, and fold array;
7. a machine-generated statement that **no corrected-map RAW or CLEAN predictive outcome has yet been computed**.

Only after that checkpoint is committed may either corrected predictive condition be computed. The RAW diagnostic must not be inspected and then used to alter the CLEAN preprocessing or protocol.

## Historical-result quarantine

The historical Experiment-06 numbers remain part of the scientific provenance record but are superseded for confirmatory inference once the corrective analysis is run. They must not be silently overwritten.

The frozen submission candidate commit `60063623eedde05ed7c351c3c947a605f6be5344` remains the immutable record of the audited candidate that was judged not ready for submission.
