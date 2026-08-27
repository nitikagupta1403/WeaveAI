# Experiment 08 Compactness Bootstrap Correction Record

## Status

This record documents a post-outcome correction to the compactness-analysis bootstrap implementation for CLO-SKET Experiment 08.

The correction does not modify the frozen compactness estimand, classifier specification, fold structure, bootstrap seed, bootstrap replicate count, non-inferiority margin, or feature representations.

## Original implementation defect

The compactness analysis prespecified a paired, within-category garment-identity bootstrap with sampling of complete recovered garment identities with replacement.

In the earlier implementation, sampled identity row blocks were accumulated and subsequently deduplicated. This removed multiplicity from identities sampled more than once.

For example, a bootstrap draw equivalent to

`[A, B, B, C]`

was effectively evaluated as

`[A, B, C]`.

This is not a valid with-replacement identity bootstrap.

Accordingly, the earlier compactness bootstrap confidence interval and any non-inferiority inference derived from that bootstrap are invalid and must not be used.

## Correction

The bootstrap implementation now preserves the full row block every time an identity is sampled.

Repeated sampled identities therefore contribute repeated row blocks to the bootstrap sample exactly as required by with-replacement sampling.

The paired outcome vectors for RA14 and DINOv2-PCA14 use the same multiplicity-preserving sampled row indices.

Implementation correction commit:

`bce2bb7` — Preserve Experiment 08 bootstrap identity multiplicity

## Frozen analysis specification retained

The corrected analysis retains:

- estimand: `D_{G,L14} = F1(G) - F1(L^(14))`
- primary metric: pooled out-of-fold macro-F1
- bootstrap unit: complete recovered garment identities
- stratification: within category
- pairing: preserved across compared models
- bootstrap replicates: 10,000
- seed: `20260821`
- non-inferiority margin: `-0.02`
- non-inferiority rule: lower bound of paired 95% bootstrap CI > `-0.02`

No parameter or decision threshold was altered in response to the corrected result.

## Corrected result

Corrected evidence:

`papers/CLO-SKET/evidence/Experiment_08/experiment08_compactness_corrected_bootstrap.json`

Evidence commit:

`41ca373` — Record corrected Experiment 08 compactness bootstrap

SHA-256:

`9f3ea226255b7516a3591e21189f1c78eec306c0dbb76f732e1b7f1ffbe37b12`

Corrected point estimate:

`D_{G,L14} = -0.49330945434360446`

Corrected paired 95% bootstrap CI:

`[-0.5322598503022689, -0.45316390290724373]`

Non-inferiority result:

`False`

RA14 pooled out-of-fold macro-F1:

`0.17400518326194342`

DINOv2-PCA14 pooled out-of-fold macro-F1:

`0.6673146376055479`

## Interpretation boundary

The corrected compactness analysis does not support non-inferiority of RA14 relative to the 14-dimensional DINOv2-PCA representation.

This correction does not alter the separate Experiment 08 mechanical-validation status.

Because the frozen mechanical validity gate failed before predictive interpretation, this compactness result remains post-outcome / exploratory evidence and must not be presented as a confirmatory predictive result.

## Supersession rule

Any earlier compactness bootstrap confidence interval or non-inferiority conclusion produced by the multiplicity-destroying bootstrap implementation is superseded by the corrected evidence identified above.

The earlier point-estimate workflow is not invalidated solely by this bootstrap defect; the invalidation applies specifically to inference derived from the defective resampling procedure.
