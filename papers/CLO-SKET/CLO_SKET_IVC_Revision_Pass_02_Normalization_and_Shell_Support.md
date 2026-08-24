# IVC Major-Revision Pass 02 — Radial Normalization and Shell-Support Wording

Status: **audited correction text; no frozen feature or Experiment 06 result modified**.

## 1. Reviewer risk addressed

The current Methods wording says that within-sketch radial normalization is used "to remove sketch-specific overall scale." That wording is too strong. The implementation uses two coordinate normalizations:

1. an aspect-ratio-preserving image-coordinate normalization factor

\[
S_i=\max(W_i,H_i),
\]

applied identically to both image axes; and

2. a within-sketch radial normalization

\[
\rho_{ip}=R_{ip}/R_{i,\max}.
\]

The second operation makes radial position dimensionless relative to the maximum centroid-relative foreground extent represented in that sketch. It does **not** establish invariance to physical garment scale, drawing scale, cropping, framing, or canvas occupancy.

## 2. Required Methods replacements

### Replacement A

Replace:

> For an image of width \(W_i\) and height \(H_i\), a common isotropic scale was defined as

with:

> For an image of width \(W_i\) and height \(H_i\), a common isotropic image-coordinate normalization factor was defined as

### Replacement B

Replace:

> To remove sketch-specific overall scale while preserving internal radial proportions, radius was normalized separately within each sketch:

with:

> To express radial position relative to the maximum centroid-relative foreground extent represented in each sketch, radius was normalized separately within each image:

Immediately after the definition of \(\rho_{ip}\), add:

> This produces a dimensionless within-sketch radial coordinate. It should not be interpreted as removing physical garment scale or as guaranteeing invariance to changes in drawing scale, cropping, framing, or canvas occupancy.

## 3. Shell-conditioning clarification

The implementation uses

\[
M_i(r_j)>10^{-14}
\]

only to distinguish numerically nonempty from empty shells before forming the conditional angular distribution. Stage-1 source-image auditing showed that this epsilon is many orders of magnitude below the support of shells that actually enter the frozen primary-domain descriptors.

Across all \(2300\times25=57{,}500\) primary-domain sketch-shell combinations:

- minimum shell mass fraction: **0.0004915941**;
- 1st percentile: **0.0018218202**;
- median: **0.0205695736**.

Across the 2,300 shells selected as the frozen \(R_2\)-peak shell:

- minimum peak-shell mass fraction: **0.0015248280**;
- 1st percentile: **0.0028645115**;
- median: **0.0207027302**.

Audit-only support thresholds up to **0.001** left the selected peak radius and peak magnitude unchanged for all 2,300 sketches. At threshold **0.002**, only 2/2300 peak shells fell below support and exact peak-radius agreement remained **0.999130**. The lower support-onset descriptor was more sensitive, consistent with the manuscript's existing characterization of localized radial descriptors as support/domain-sensitive.

## 4. Required Methods clarification after shell conditioning

After the paragraph explaining that shell conditioning prevents high-ink shells from dominating solely because of mass, add a short clarification such as:

> The \(10^{-14}\) criterion is an empty-shell numerical guard rather than a substantive foreground-support threshold. In a source-image support audit over the frozen 25-shell primary domain, every retained shell carried at least \(4.92\times10^{-4}\) of total sketch darkness mass and every selected \(R_2\)-peak shell at least \(1.52\times10^{-3}\). Peak selection was unchanged for all 2,300 sketches under an audit-only minimum relative shell-mass threshold of \(10^{-3}\). Localized support-boundary descriptors were more sensitive to stronger support perturbations and are interpreted accordingly.

## 5. Claim boundary

This audit supports the statement that the frozen primary descriptors are not being driven by numerically empty or near-empty shells under the tested support perturbations. It does **not** establish general robustness to arbitrary shell-support definitions, alternative radial domains, alternative image framing, or changes in preprocessing.

No threshold was optimized or selected from these results, and no Stage-2 predictive propagation is required for this specific reviewer concern.
