# 3. Methods

## 3.1 Study design and scope

This study developed and audited a compact radial–angular representation of garment sketches. The analysis was geometric rather than semantic: garment-category labels and manually annotated garment parts were not used to construct or select the descriptors. Category information was used only to balance grouped validation folds and to stratify the final permutation procedure.

The final primary representation was a provenance-locked 14-dimensional vector comprising eight radial descriptors derived directly from the magnitude of the second angular harmonic and six axial descriptors derived from its phase. Historical 28-dimensional feature-family assemblies, principal-component analysis, von Mises fitting, full angular-density reconstruction, and category-based feature selection were not part of the final study.

The analytical sequence was: (1) construct the conditional angular distribution around each sketch's intensity-weighted centroid; (2) extract the second angular harmonic over radius; (3) summarize its radial magnitude and axial orientation in the locked 14-dimensional representation; (4) audit exact algebraic relationships among harmonic quantities; (5) recover garment identities and construct identity-disjoint folds; (6) reconstruct the observed second-moment components out of fold; and (7) quantify uncertainty using garment-identity resampling and category-stratified permutation.

## 3.2 Dataset and garment-identity reconstruction

The analysis used all 2,300 CLO-SKET images. The directory structure contained 23 garment-category folders. Garment identity was reconstructed from the category-qualified source identifier encoded in each filename; the replicate identifier denoted the sketch associated with that source garment. This procedure recovered 230 garment identities, exactly 10 per category, with 9–11 sketches per identity because of irregular filename records.

File paths were unique. SHA-256 hashing found no repeated raw files, and hashing of decoded pixel arrays found no repeated decoded images. Perceptual hashes were used only to screen candidate visually similar pairs and were not interpreted as proof of duplication or lineage. The recovered garment identity was therefore used as the indivisible unit for cross-validation and resampling. The audit did not establish that the 230 garment identities were mutually independent sampling units; population-level inference remains conditional on that assumption.

## 3.3 Polar coordinate construction

For sketch \(i\), let \(w_{ip}\geq 0\) denote the foreground intensity weight at pixel \(p\), located at isotropic Cartesian coordinates \((x_{ip},y_{ip})\). Its intensity-weighted centroid was

\[
c_{x,i}=\frac{\sum_p w_{ip}x_{ip}}{\sum_p w_{ip}},
\qquad
c_{y,i}=\frac{\sum_p w_{ip}y_{ip}}{\sum_p w_{ip}}.
\]

Each foreground location was expressed relative to this centroid as

\[
r_{ip}=\sqrt{(x_{ip}-c_{x,i})^2+(y_{ip}-c_{y,i})^2},
\qquad
\theta_{ip}=\operatorname{atan2}(y_{ip}-c_{y,i},x_{ip}-c_{x,i}).
\]

The implementation discretized radius into 72 radial bins and angle into 72 angular bins. Let \(H_i(r_j,\theta_k)\) be the accumulated intensity weight in radial bin \(j\) and angular bin \(k\). The conditional angular distribution at a nonempty radial bin was

\[
p_i(\theta_k\mid r_j)
=
\frac{H_i(r_j,\theta_k)}{\sum_{\ell=1}^{72}H_i(r_j,\theta_\ell)},
\qquad
\sum_{k=1}^{72}p_i(\theta_k\mid r_j)=1.
\]

Thus, the construction retained angular organization conditional on radius rather than allowing high-mass radial shells to dominate merely because they contained more ink.

## 3.4 Second angular harmonic and axial orientation

At each radial shell, the complex second angular moment was defined as

\[
F_{2,i}(r_j)
=
\sum_{k=1}^{72}p_i(\theta_k\mid r_j)e^{-\mathrm{i}2\theta_k}.
\]

The negative exponential records the FFT convention used by the audited implementation. Equivalently,

\[
C_{2,i}(r_j)
=
\sum_k p_i(\theta_k\mid r_j)\cos(2\theta_k),
\]

\[
S_{2,i}(r_j)
=
\sum_k p_i(\theta_k\mid r_j)\sin(2\theta_k),
\]

so that

\[
F_{2,i}(r_j)=C_{2,i}(r_j)-\mathrm{i}S_{2,i}(r_j).
\]

Its magnitude, also called the second resultant length, was

\[
m_i(r_j)=|F_{2,i}(r_j)|
=R_{2,i}(r_j)
=\sqrt{C_{2,i}(r_j)^2+S_{2,i}(r_j)^2}.
\]

The associated axial direction was

\[
\alpha_{2,i}(r_j)
=
\frac{1}{2}\operatorname{atan2}
\!\left(S_{2,i}(r_j),C_{2,i}(r_j)\right)
\pmod{\pi}.
\]

The factor of two makes the direction axial: \(\alpha\) and \(\alpha+\pi\) describe the same undirected orientation. Consequently, angular differences were folded onto \([0,\pi/2]\):

\[
d_{\mathrm{ax}}(a,b)
=
\min\!\left(
|a-b|\bmod \pi,
\pi-(|a-b|\bmod \pi)
\right).
\]

All reported angular errors used the degree-equivalent interval \([0^\circ,90^\circ]\).

## 3.5 Locked radial domain

The primary radial analysis was restricted to 25 shell centers spanning

\[
\mathcal R=\{3.5,4.5,\ldots,27.5\}.
\]

This domain was fixed before the peak-shell sensitivity and inferential analyses. For each sketch, the selected observed peak shell was

\[
j_i^\star=\arg\max_{j:r_j\in\mathcal R}m_i(r_j),
\qquad
r_i^\star=r_{j_i^\star}.
\]

The peak magnitude was \(m_i^\star=m_i(r_i^\star)\). Because \(R_2(r)=|F_2(r)|\) by construction,

\[
R_{2,i}(r_i^\star)=m_i^\star.
\]

These are therefore two names for the same measured quantity, not independent features or independent evidence. Peak radius is a selected coordinate on a discrete, bounded domain; boundary occupancy was audited explicitly.

## 3.6 Eight radial-magnitude descriptors

Let \(m_i(r)=|F_{2,i}(r)|\) over \(\mathcal R\). Integrals below were evaluated by the trapezoidal rule at the radial-shell centers. They are expressed in radial-bin-coordinate units, not physical distance, and the magnitude integral is not Fourier energy.

The integrated magnitude was

\[
I_i=\int_{\mathcal R}m_i(r)\,dr.
\]

The magnitude-weighted radial centroid and spread were

\[
\bar r_i
=
\frac{\int_{\mathcal R}r\,m_i(r)\,dr}{I_i},
\qquad
s_{r,i}
=
\sqrt{
\frac{\int_{\mathcal R}(r-\bar r_i)^2m_i(r)\,dr}{I_i}
}.
\]

With \(r_i^\star\) denoting the discrete peak radius, radial concentration was the fraction of integrated magnitude within four radial-coordinate units of the peak:

\[
q_i
=
\frac{
\int_{\mathcal R\cap[r_i^\star-4,r_i^\star+4]}m_i(r)\,dr
}{I_i}.
\]

Let \(\tau_i=0.10\,m_i^\star\). The observed onset and termination radii were

\[
r_i^{\mathrm{on}}
=\min\{r\in\mathcal R:m_i(r)\geq\tau_i\},
\qquad
r_i^{\mathrm{off}}
=\max\{r\in\mathcal R:m_i(r)\geq\tau_i\}.
\]

The eight locked radial features, in column order, were

\[
\mathbf x^{(F_2)}_i=
[
I_i,
\bar r_i,
s_{r,i},
q_i,
r_i^{\mathrm{on}},
r_i^{\mathrm{off}},
r_i^\star,
m_i^\star
]\in\mathbb R^8.
\]

The radial extent \(r_i^{\mathrm{off}}-r_i^{\mathrm{on}}\) was excluded because it is exactly determined by two retained features.

## 3.7 Six axial-safe descriptors

The peak axial direction was

\[
\alpha_i^\star=\alpha_{2,i}(r_i^\star).
\]

The magnitude-weighted axial mean used the doubled-angle resultant

\[
Z_i
=
\sum_{r_j\in\mathcal R}
m_i(r_j)e^{\mathrm{i}2\alpha_{2,i}(r_j)},
\qquad
\bar\alpha_i
=
\frac{1}{2}\arg(Z_i)\pmod{\pi}.
\]

Axial coherence was

\[
\kappa_i
=
\frac{|Z_i|}{\sum_{r_j\in\mathcal R}m_i(r_j)},
\qquad 0\leq\kappa_i\leq1,
\]

and orientation drift was the axial distance between the orientations at the first and last locked shells:

\[
\delta_i
=
d_{\mathrm{ax}}
\!\left(
\alpha_{2,i}(3.5),
\alpha_{2,i}(27.5)
\right).
\]

Raw axial angles were not entered directly into the primary vector. Each retained direction was represented by its doubled-angle Cartesian coordinates, yielding

\[
\mathbf x^{(\alpha_2)}_i=
[
\cos(2\alpha_i^\star),
\sin(2\alpha_i^\star),
\cos(2\bar\alpha_i),
\sin(2\bar\alpha_i),
\kappa_i,
\delta_i
]\in\mathbb R^6.
\]

This encoding is invariant under \(\alpha\mapsto\alpha+\pi\). Persistence and weighted-dispersion summaries were excluded after the redundancy audit; reconstructed circular quantities and tautological \(F_2\)-versus-\(R_2\) relations were retained only for auditing, not as primary features.

## 3.8 Primary 14-dimensional representation and provenance lock

The final sketch representation was the exact ordered concatenation

\[
\mathbf x_i
=
\left[
\mathbf x^{(F_2)}_i\mid
\mathbf x^{(\alpha_2)}_i
\right]
\in\mathbb R^{14}.
\]

The resulting matrix had shape \(2300\times14\), contained only finite values, and matched the locked \(8+6\) concatenation exactly with maximum numerical difference zero. Column order was frozen by the Cell 23C provenance lock. No historical 28-dimensional family assembly was asserted.

## 3.9 Garment-identity-disjoint out-of-fold reconstruction

To evaluate whether the observed second-moment field could be reconstructed from radius and harmonic magnitude while preventing source-garment leakage, five category-balanced folds were constructed over the 230 recovered garment identities. Each test fold contained two complete identities from every category, giving 46 test identities and all 23 categories per fold. Garment-identity overlap between training and testing was zero, and every sketch was tested exactly once.

At every valid sketch-shell row, the predictors were

\[
\mathbf z_{ij}=[r_j,m_i(r_j)]
\]

and the two targets were \(C_{2,i}(r_j)\) and \(S_{2,i}(r_j)\). Two `HistGradientBoostingRegressor` models were fitted independently within each training fold:

\[
\widehat C_{2,i}(r_j)=f_C(\mathbf z_{ij}),
\qquad
\widehat S_{2,i}(r_j)=f_S(\mathbf z_{ij}).
\]

Reconstructed magnitude and orientation were then derived, rather than fitted directly:

\[
\widehat R_{2,i}(r_j)
=
\sqrt{\widehat C_{2,i}(r_j)^2+\widehat S_{2,i}(r_j)^2},
\]

\[
\widehat\mu_{2,i}(r_j)
=
\frac{1}{2}\operatorname{atan2}
\!\left(
\widehat S_{2,i}(r_j),
\widehat C_{2,i}(r_j)
\right)
\pmod{\pi}.
\]

At the observed peak shell, axial reconstruction error was

\[
e_i=d_{\mathrm{ax}}
\!\left(
\widehat\mu_{2,i}(r_i^\star),
\mu_{2,i}(r_i^\star)
\right).
\]

Fold-local global and radius-only models were retained as comparators. The historical sketch-level out-of-fold arrays were preserved for audit comparison but were superseded for final reporting by the identity-disjoint estimates.

This reconstruction is a shared-source consistency diagnostic: \(m\), \(C_2\), and \(S_2\) all arise from the same conditional angular field. It does not demonstrate recovery of an independent physical or semantic target.

## 3.10 Peak-shell association analysis

The two prespecified primary quantities were observed peak-shell magnitude \(R_{2,i}(r_i^\star)\) and selected peak radius \(r_i^\star\). The primary outcome was peak-shell axial error \(e_i\).

For confirmatory association analysis, all sketches belonging to garment identity \(g\) were reduced to medians:

\[
\widetilde R_{2,g}=\operatorname{median}_{i\in g}R_{2,i}(r_i^\star),
\quad
\widetilde r_g^\star=\operatorname{median}_{i\in g}r_i^\star,
\quad
\widetilde e_g=\operatorname{median}_{i\in g}e_i.
\]

Spearman's rank correlation was computed across the 230 identities for \((\widetilde R_{2,g},\widetilde e_g)\) and \((\widetilde r_g^\star,\widetilde e_g)\). This gave equal weight to each recovered garment identity. The two primary permutation probabilities were adjusted by Holm's procedure. Corresponding correlations over all 2,300 sketches were retained as descriptive summaries without inferential p-values.

## 3.11 Garment-cluster bootstrap and stratified permutation

Confidence intervals were obtained from 5,000 bootstrap replicates. Complete garment identities, rather than individual sketches or sketch-shell rows, were resampled; every selected cluster contributed all its sketches and, where applicable, all 25 shells. Percentile 95% intervals were defined by the 2.5th and 97.5th percentiles.

For each primary association, 10,000 permutations were performed within the 23 category strata. Garment-level outcome values were permuted only among identities in the same category, thereby holding category composition fixed. With observed statistic \(T_{\mathrm{obs}}\), the two-sided corrected permutation probability was

\[
p
=
\frac{1+\sum_{b=1}^{B}
\mathbf 1\{|T_b|\geq|T_{\mathrm{obs}}|\}}
{B+1},
\qquad B=10000.
\]

All intervals and permutation results remain conditional on mutual independence of the 230 recovered garment identities.

## 3.12 Outcome-defined bands and threshold sensitivity

Peak-shell errors were summarized descriptively as low (\(e_i\leq15^\circ\)), intermediate (\(15^\circ<e_i\leq45^\circ\)), and high (\(e_i>45^\circ\)). Sensitivity was assessed using four prespecified low/high threshold pairs: \(10^\circ/30^\circ\), \(15^\circ/45^\circ\), \(20^\circ/45^\circ\), and \(20^\circ/60^\circ\).

For each pair, median observed peak-shell \(R_2\) and Cliff's delta were computed between the low- and high-error groups. Cliff's delta was oriented as

\[
\delta_C
=
P(R_{2,\mathrm{low}}>R_{2,\mathrm{high}})
-
P(R_{2,\mathrm{low}}<R_{2,\mathrm{high}}).
\]

Intervals were obtained by resampling complete garment identities. No p-values were assigned to these outcome-defined, strongly overlapping groups, and the thresholds were not optimized against the data.

## 3.13 Algebraically coupled diagnostic

Peak-shell magnitude error was

\[
\Delta R_{2,i}
=
\widehat R_{2,i}(r_i^\star)
-
R_{2,i}(r_i^\star).
\]

Because the observed value appears algebraically with a negative sign in \(\Delta R_2\), its correlation with observed \(R_2\) is mathematically coupled. This correlation was reported only as a calibration diagnostic and received no inferential p-value.

## 3.14 Evidence and claim boundary

The analysis supports exact computational-provenance claims for the 14-dimensional representation, leakage-controlled reconstruction transfer to unseen recovered garment identities, descriptive peak-shell reconstruction behavior, and conditional garment-level associations. It does not establish mutual independence of the 230 identities, causality, semantic garment-part recognition, human-like understanding, a physical radial law, a prospective reliability classifier, von Mises fitting, or reconstruction of the complete angular density.
