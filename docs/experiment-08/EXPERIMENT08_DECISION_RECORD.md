# CLO-SKET Experiment 08 — Consolidated Decision Record

**Date:** 2026-08-27  
**Scope:** Paper I / CLO-SKET / Experiment 08  
**Status:** Post-outcome consolidated scientific record

## Overall decision

Experiment 08 does **not** support a confirmatory claim for RA14.

The prespecified mechanical-validity gate failed because the raster magnitude criterion failed. The exact analytic transformation audit passed, and raster axial behavior passed its frozen criterion, but these partial successes do not override the failed overall mechanical gate.

All predictive results involving RA14 are therefore retained for auditability as **exploratory/post-outcome evidence only**.

No failed gate is retroactively revised or rescued.

---

## Decision map

| Component | Result | Scientific status |
|---|---|---|
| Analytic harmonic transformation | PASS | Valid analytic verification |
| Raster axial equivariance | PASS | Valid mechanical sub-result |
| Raster magnitude robustness | FAIL | Frozen mechanical failure |
| Overall RA14 mechanical gate | FAIL | Blocks confirmatory interpretation |
| Rotation-sign convention | RESOLVED | Coordinate clarification only; no gate change |
| Post-outcome mechanical sensitivity | COMPLETED | Diagnostic/explanatory only |
| Primary RA14 predictive analyses | COMPUTED | Exploratory only |
| Original compactness bootstrap inference | INVALID | Superseded |
| Corrected compactness bootstrap | COMPLETED | Exploratory only |
| RA14 compactness non-inferiority | NOT SUPPORTED | Corrected CI far below frozen NI margin |

---

## 1. Mechanical validation

### Analytic component

The exact harmonic transformation audit passed.

The implementation-level doubled-angle transformation error was within the frozen analytic tolerance.

### Raster component

Raster axial behavior passed its frozen criterion.

Raster harmonic-magnitude robustness did not pass its frozen criterion.

Therefore:

**Overall mechanical-validity status: FAIL**

This status is immutable for the frozen Experiment 08 analysis.

Canonical mechanical evidence remains the original frozen mechanical-validation evidence.

---

## 2. Coordinate convention

The apparent sign discrepancy between the analytic equation and raster observations has been resolved as a coordinate-system issue.

Cartesian coordinates use a vertical axis positive upward.

The frozen raster implementation uses native image coordinates with the vertical axis positive downward.

Accordingly, for a visual counterclockwise image rotation by `phi`:

`alpha_img' = alpha_img - phi (mod pi)`

is consistent with the frozen raster implementation.

This clarification changes no feature values, hashes, thresholds, predictions, or gate outcomes.

---

## 3. Post-outcome mechanical sensitivity

A diagnostic sensitivity analysis was prospectively specified after the original mechanical failure and executed without altering the original gate.

Its purpose was to investigate the raster magnitude failure, not to replace the frozen metric.

The diagnostic evidence indicates:

- relative magnitude error is strongly influenced by low reference `R2`;
- denominator conditioning is therefore a major contributor;
- shell-support dependence is also present but weaker;
- rotation-dependent raster/interpolation effects remain;
- absolute perturbation is not identically zero at moderate/high `R2`.

The sensitivity analysis therefore explains part of the failure mechanism but does not convert the original mechanical result to PASS.

**Original mechanical gate remains FAIL.**

---

## 4. Predictive interpretation boundary

Because the mechanical gate did not pass before predictive interpretation, predictive analyses involving RA14 cannot be described as confirmatory.

Existing predictive outputs may be retained only as exploratory evidence.

They must not be used to claim that RA14 has established:

- mechanical validity;
- confirmatory additive predictive value;
- confirmatory non-inferiority;
- a validated compact substitute for a learned representation.

---

## 5. Compactness bootstrap correction

The original paired identity-bootstrap implementation did not preserve multiplicity of identities sampled repeatedly with replacement.

The defective bootstrap inference is invalid.

Implementation correction:

`bce2bb7` — Preserve Experiment 08 bootstrap identity multiplicity

Corrected evidence:

`papers/CLO-SKET/evidence/Experiment_08/experiment08_compactness_corrected_bootstrap.json`

Evidence commit:

`41ca373` — Record corrected Experiment 08 compactness bootstrap

Correction record:

`docs/experiment-08/compactness-bootstrap-correction-record.md`

Correction-record commit:

`13e13ad`

Governance reconciliation:

`e0f67ec` — Reconcile Experiment 08 compactness correction chronology

### Corrected compactness result

Estimand:

`D_{G,L14} = F1(G) - F1(L^(14))`

Point estimate:

`-0.49330945434360446`

Corrected paired 95% bootstrap CI:

`[-0.5322598503022689, -0.45316390290724373]`

Frozen non-inferiority margin:

`-0.02`

Frozen rule:

lower bound of paired 95% bootstrap CI must exceed `-0.02`.

Result:

**Non-inferiority = FALSE**

RA14 pooled OOF macro-F1:

`0.17400518326194342`

DINOv2-PCA14 pooled OOF macro-F1:

`0.6673146376055479`

Thus RA14 is not supported as a compact predictive substitute for the equally 14-dimensional DINOv2-PCA representation under this Experiment 08 analysis.

Because the mechanical gate had already failed, this corrected compactness result remains exploratory/post-outcome evidence.

---

## 6. Supersession rules

The following are superseded and must not be used:

1. any compactness bootstrap confidence interval generated by the multiplicity-destroying implementation;
2. any non-inferiority conclusion derived from that defective bootstrap;
3. any interpretation treating Experiment 08 predictive results as confirmatory despite the failed mechanical gate.

The corrected compactness result supersedes only the defective compactness inference.

It does not alter the frozen mechanical failure.

---

## 7. Manuscript rule

For Paper I, Experiment 08 must either:

1. be omitted from confirmatory claims and primary conclusions; or
2. be presented explicitly as exploratory/post-outcome evidence.

If reported, the manuscript must disclose:

- the failed raster magnitude gate;
- the overall failed RA14 mechanical gate;
- the coordinate-convention clarification;
- the post-outcome mechanical sensitivity result;
- the defective original compactness bootstrap;
- the corrected multiplicity-preserving bootstrap;
- the corrected failure of compactness non-inferiority.

The terms **validated**, **mechanically verified**, **confirmatory**, or **non-inferior** must not be used to characterize RA14 on the basis of Experiment 08.

---

## 8. Current authorization boundary

No further predictive analysis is authorized by this record.

Any new predictive sensitivity, filtering, stratification, or revised estimand requires a separate prospective amendment committed before the corresponding outcomes are computed.

---

## Final status

**Experiment 08 overall scientific status: EXPLORATORY / POST-OUTCOME**

**Frozen RA14 mechanical-validity gate: FAIL**

**Corrected compactness non-inferiority: FALSE**

**Confirmatory RA14 claim permitted: NO**
