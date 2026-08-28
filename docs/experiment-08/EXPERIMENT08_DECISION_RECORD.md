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

---

## Chronology-preserving addendum — post-outcome predictive controls

**Addendum date:** 2026-08-28

This addendum records predictive-control work that occurred **after** the consolidated decision above. It does not revise the original Experiment-08 decision chronology, reopen the failed mechanical gate, or change the scientific status of any Experiment-08 predictive result.

After Experiment 08 was already classified as post-outcome / exploratory, two additional predictive controls were prospectively authorized in `docs/experiment-08/post-outcome-predictive-controls-amendment.md` (commit `6e62d94`) and structurally clarified before execution in `docs/experiment-08/post-outcome-predictive-controls-clarification.md` (commit `7b4b283`). Their implementation was then committed before the corresponding outcomes were computed.

### A. Category/block-size-preserving correspondence permutation

The first control tested whether the correctly aligned RA14-to-DINOv2 correspondence produced an unusually large additive macro-F1 increment relative to identity-block reassignments that preserved garment category and identity-block size.

The observed exploratory DINOv2 + RA14 macro-F1 increment was:

`+0.0009466521822523166`

Across `B = 1000` prespecified correspondence permutations, the empirical upper-tail probability was:

`p = 0.999000999000999`

The permutation distribution had mean increment `0.013596323290899682`, median `0.013688493815160296`, 2.5th percentile `0.005085149860362126`, and 97.5th percentile `0.021671779289126402`.

All prespecified correspondence invariants passed. Two singleton `(category, identity_block_size)` strata were structurally fixed, while the remaining eligible identity blocks were reassigned within their frozen strata.

Interpretation is deliberately narrow. Because the permutation preserves category structure, it does **not** remove all category-associated information in RA14 and therefore does not test whether RA14 contains category signal in general. It tests whether the correctly paired garment-instance correspondence yields an unusually large additive gain relative to category/block-size-preserving reassignment. On that question, the aligned increment was not unusually high.

This result must not be interpreted as proof of harm, absence of all RA14 information, or evidence that category-conditioned RA14 structure is useless.

Canonical evidence commit:

`73eaa1a` — correspondence-control evidence

### B. Repeated identity-grouped partitions

The second control repeated the exploratory DINOv2 versus DINOv2 + RA14 comparison over 20 prespecified identity-grouped `StratifiedGroupKFold` partitions, using random-state seeds `20260823` through `20260842` exactly once each.

Across the 20 repeats, the exploratory macro-F1 increment had:

- mean: `+0.003927456181713002`
- median: `+0.002580754931087559`
- minimum: `-0.00581427160322634`
- maximum: `+0.0140545603514044`
- sample standard deviation: `0.005057883269142741`
- descriptive 2.5th percentile: `-0.004329725078960567`
- descriptive 97.5th percentile: `+0.01325764759058405`
- positive repeats: `17 / 20`

All frozen grouping and fold-integrity checks passed, and all 20 partition hashes were distinct.

These repeated-partition quantiles are descriptive summaries, **not a confidence interval**. The result is best interpreted as a small and partition-sensitive exploratory increment; three of the 20 repeats were negative. The canonical frozen-partition increment of `+0.0009466521822523166` lies toward the lower end of the repeated-partition distribution and was not an unusually favorable split.

Canonical evidence commit:

`17c3382` — repeated-partition evidence

### C. Scientific status after the controls

Neither predictive control changes the Experiment-08 decision boundary.

- the frozen mechanical gate remains **FAIL**;
- all Experiment-08 predictive results remain **post-outcome / exploratory**;
- the correspondence permutation does not establish garment-instance-specific additive information;
- the repeated-partition results do not establish a stable fixed gain;
- the corrected compactness non-inferiority result remains **FALSE**;
- no confirmatory RA14 claim is restored.

The complete Experiment-08 evidence chronology, commit relationships, hashes, supersession rules, and claim boundaries are recorded in `docs/experiment-08/EXPERIMENT08_EVIDENCE_PROVENANCE_MANIFEST.md` (commit `778d351`).

The manuscript-facing reconciliation was subsequently committed as:

`0eb6730` — Reconcile Experiment 08 manuscript claims

This addendum is documentation-only. It authorizes no new predictive analysis and does not alter any frozen evidence or outcome.
