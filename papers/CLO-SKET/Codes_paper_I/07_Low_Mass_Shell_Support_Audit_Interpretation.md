# CLO-SKET Low-Mass Shell Support Audit — Stage-1 Interpretation

## Status

**Reviewer-risk audit only. No feature definition, Experiment 06 model, fold, hypothesis, or frozen result is modified.**

The concern under review was that shell-conditioned angular normalization could allow a shell carrying negligible foreground mass to receive the same conditional angular normalization as a well-supported shell and therefore spuriously determine localized second-harmonic descriptors.

## Stage-1 empirical findings

The audit recomputed radial-angular mass from all 2,300 source TIFF sketches and examined the frozen 25-shell primary domain, `r = 3.5, ..., 27.5`.

### 1. No negligibly supported shell occurs in the frozen primary domain

Across all sketch-shell observations in the primary domain, the minimum shell mass fraction was

- minimum: `0.0004915941` (~0.0492% of total sketch darkness mass),
- 1st percentile: `0.0018218202`,
- median: `0.0205695736`,
- maximum: `0.1244173426`.

Thus the implementation epsilon `M_i(r) > 1e-14` is only an empty-shell numerical guard. It is not the effective support level of shells contributing to the primary 14-D representation.

### 2. Peak-shell support is materially above the numerical epsilon

For the shell selected by the frozen second-harmonic peak,

- minimum peak-shell mass fraction: `0.0015248280` (~0.1525%),
- 1st percentile: `0.0028645115`,
- median: `0.0207027302`.

No selected peak shell fell below mass fractions of `1e-5`, `5e-5`, `1e-4`, `5e-4`, or `1e-3`.

At an audit-only `0.002` threshold, only 2 / 2,300 sketches (`0.0870%`) had a peak shell below threshold. Exact peak-radius agreement remained `0.999130`; peak-magnitude rank agreement remained `0.999862`.

### 3. Moderate audit thresholds leave the representation essentially unchanged

At threshold `0.001` (0.1% of total darkness mass), mean retained shells were `24.952 / 25`; peak radius and peak magnitude were unchanged for all 2,300 sketches. Integrated and broad radial summaries had rank correlations >= `0.999956` except support onset (`0.988379`).

At threshold `0.002` (0.2%), mean retained shells were `24.711 / 25`; exact peak-radius agreement was `0.999130`, peak-radius Spearman correlation `0.998146`, and peak-magnitude Spearman correlation `0.999862`.

### 4. The lower radial endpoint is the most support-sensitive localized quantity

The lower primary-domain endpoint was below the audit threshold in

- 0 / 2,300 sketches at `1e-4`,
- 1 / 2,300 at `5e-4`,
- 81 / 2,300 (`3.52%`) at `0.001`,
- 304 / 2,300 (`13.22%`) at `0.002`,
- 854 / 2,300 (`37.13%`) at `0.005`.

This is consistent with the manuscript's existing treatment of onset/termination and peak localization as localized, domain-sensitive descriptors. It does not indicate that the primary representation is driven by numerical-empty shells.

The upper endpoint was never below thresholds through `0.002` and was below `0.005` in only 2 sketches (`0.087%`).

### 5. The `0.005` perturbation is deliberately aggressive and is not a replacement definition

At `0.005` (0.5% of total darkness mass per shell), substantial endpoint and localized-descriptor changes appear. This threshold excludes non-negligible foreground support and therefore should be interpreted as a stress test, not evidence that the frozen `1e-14` guard is inadequate.

## Decision

**Stage-2 predictive propagation is not required to address the stated negligible-mass-shell reviewer concern.**

Reason: within the actual frozen 25-shell domain, every contributing shell already carries at least ~0.049% of total sketch darkness mass, and every frozen peak shell carries at least ~0.153%. Peak selection is completely unchanged through a 0.1% support threshold and changes in only 2 / 2,300 sketches at 0.2%. The feared failure mode—an effectively empty shell winning the second-harmonic peak—is therefore not observed.

A predictive rerun under an alternative support threshold would amount to evaluating a post-hoc modified representation and is unnecessary for this specific concern. The frozen Experiment 06 remains unchanged.

## Manuscript implication

The paper should not claim that the `1e-14` criterion itself guarantees meaningful shell support. Instead, the Methods/limitations text may state that it is an empty-shell numerical guard and that a source-image audit found all shells in the frozen primary domain to carry at least `4.92e-4` of total sketch darkness mass, with frozen peak shells carrying at least `1.52e-3`.

The existing caution that localized descriptors are more sensitive to domain/support choices than broad radial summaries should be retained.
