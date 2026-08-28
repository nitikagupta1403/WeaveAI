# CLO-SKET Paper I — Scientific Remediation Roadmap

## Status

This roadmap operationalizes the corrective path from the audited submission candidate at commit `60063623eedde05ed7c351c3c947a605f6be5344` toward a new submission-ready candidate for *Image and Vision Computing*.

The audited candidate remains immutable historical provenance. All new empirical work proceeds only on the corrective revision lineage defined by `Experiment_06_Corrective_Reanalysis_PROSPECTIVE_LOCK.md`.

## Phase 1 — Remediate fatal scientific blockers

### F1. Correct garment-identity leakage

- Build and deposit the complete corrected 2,300-row garment-identity table.
- Encode the authoritative pre-outcome corrections:
  - `Dress/1-3.tif`: `DressG01`, historical Fold 0 -> `DressG10`, corrected Fold 4.
  - `Harem/6-6.tif`: `HaremG06`, historical Fold 2 -> `HaremG02`, corrected Fold 0.
- Verify that exactly one corrected garment identity and one fold are assigned to every row.
- Verify zero corrected-garment train/test overlap in each of the five folds.
- Freeze and hash the corrected identity table and fold array before any corrected predictive outcome is computed.
- Run the corrected Experiment-06 confirmatory analysis only after the complete pre-outcome checkpoint is committed.

### F2. Control canvas annotations

- Audit all 2,300 TIFFs for non-garment annotation.
- Create a single outcome-blind garment-only measurement field per image, shared by RA14 and the 135-D baseline.
- For separable annotation, use a deterministic crop/mask rule that removes only non-garment marks.
- For annotation touching or crossing garment strokes, perform blinded manual adjudication and retain provenance.
- Freeze and hash all annotation-control artifacts before feature extraction for corrected predictive analysis.

### Prespecified annotation-sensitivity diagnostic

The historical raw-canvas result cannot by itself quantify annotation impact because it also used the historical defective identity map.

Therefore, after the pre-outcome checkpoint is frozen, compute two corrected-map conditions with identical folds, row order, representations, and estimator:

1. **RAW diagnostic** — native canvases, corrected identity map/folds. Diagnostic only.
2. **CLEAN confirmatory** — frozen garment-only fields, corrected identity map/folds. Sole confirmatory analysis.

Report the prespecified RAW-versus-CLEAN table for `M` and `M+R+A`, including absolute macro-F1, balanced accuracy, the RA14 incremental contrast in each condition, and CLEAN-minus-RAW changes. No outcome-dependent preprocessing selection is permitted.

## Phase 2 — Provenance, artifacts, and end-to-end reproducibility

- Deposit corrected row map and fold map.
- Deposit annotation-status table and preprocessing manifest.
- Deposit frozen RAW and CLEAN feature matrices with identical row order.
- Deposit row-level OOF predictions for `M` and `M+R+A` for both prespecified preprocessing conditions.
- Deposit executable feature extraction and model-fitting code.
- Deposit bootstrap code/output for the CLEAN confirmatory analysis.
- Deposit retained repeated-partition and alignment-control code/output if those robustness analyses are repeated.
- Freeze the runtime/package environment.
- Create a final manifest linking every manuscript number to an immutable artifact.
- After the corrected scientific package and manuscript are final, create a tagged immutable release and archival DOI where feasible.

## Phase 3 — Novelty reframing and baseline clarification

### M1. Narrow novelty

Revise Introduction and Related Work to position RA14 against established radial/angular and Fourier shape descriptors, including:

- MPEG-7 Angular Radial Transform (ART);
- Generic Fourier Descriptor (GFD);
- angular-radial sketch/shape decomposition;
- Angular Radial Edge Histograms (AREH);
- Shape Contexts;
- phase-aware ART and related polar/Fourier descriptors.

Do not claim novelty for radial-angular/Fourier shape description broadly.

The defensible contribution is the specific compact 14-D shell-conditioned second-harmonic axial-radial formulation and its dependency-aware evaluation framework that separates incremental predictive utility from garment-specific correspondence.

### M2. Define the 135-D comparator precisely

Describe the comparator as the **lower-performing frozen morphology baseline** and explicitly document:

- 64 horizontal occupancy-profile coordinates;
- 64 vertical occupancy-profile coordinates;
- 7 frozen global morphology/statistical coordinates from the historical implementation.

Do not use `outline morphology` as a technical definition of this representation.

## Phase 4 — Claim discipline and narrative correction

### M4. Experiment-08 chronology

State that Experiment-08 predictive point estimates were already frozen before mechanical-gate reconciliation. Preserve the failed prospective gate and classify all Experiment-08 predictive evidence as exploratory/post-outcome. Do not use E08 to rescue E06.

### M5. Bootstrap estimand

State that the Experiment-06 identity bootstrap quantifies score-contrast uncertainty conditional on frozen OOF predictions. Do not describe it as including model-refitting uncertainty.

### M6. Alignment permutation

Replace affirmative `category structure is sufficient to explain` language with:

> compatible with category-conditioned distributional structure

Preserve the distinction between incremental predictive utility and exact garment-level correspondence.

### Minor wording and figures

- Rephrase the HOG null result as consistent with overlapping or already-captured category-relevant information, not proof of redundancy.
- Standardize `axial-radial` terminology in Figure 2.
- Mark Figure 3 visibly as the earlier descriptive control rather than the failed Experiment-08 gate.
- Regenerate the identity-validation figure after the corrected analysis.

## Phase 5 — Submission-readiness gate

A new submission candidate may be assembled only after all of the following are satisfied:

1. The corrected CLEAN Experiment-06 result is frozen and reported regardless of sign.
2. True zero corrected-garment train/test overlap is machine verified.
3. Annotation-control artifacts are complete and immutable.
4. The RAW-versus-CLEAN diagnostic is reported without being used to select preprocessing.
5. Every reported metric and interval reconciles to deposited evidence.
6. The 135-D baseline is fully defined.
7. Novelty claims are narrowed against primary prior art.
8. Experiment-08 chronology and exploratory status are corrected.
9. Bootstrap and alignment interpretations are correctly scoped.
10. The primary pipeline is end-to-end rerunnable from source images.
11. A simulated Reviewer-2 audit finds no unresolved fatal or major scientific contradiction.

## Decision rule

If the corrected CLEAN primary RA14 increment remains positive with its prespecified identity-bootstrap interval excluding zero, the revised manuscript may support a confirmatory incremental-utility claim under corrected identity-disjoint, annotation-controlled validation.

If the increment is positive but the interval includes zero, the revised manuscript must describe the evidence as uncertain.

If the increment is zero or negative, the positive confirmatory claim must be abandoned. Experiment 07 and Experiment 08 cannot be promoted to rescue it.

The scientific result governs the paper; the paper does not govern the result.
