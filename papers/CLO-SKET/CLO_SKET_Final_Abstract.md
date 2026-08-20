# Abstract

Garment sketches encode form through sparse marks whose organization varies with distance and direction from an implied centre. We present an auditable radial–angular representation of all 2,300 CLO-SKET sketches, comprising 23 categories and 230 recovered garment identities. Foreground intensity is accumulated in centroid-relative polar bins to estimate a conditional angular distribution (p(\theta\mid r)). Its complex second harmonic,

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-\mathrm{i}2\theta_k}
      =C_2(r)-\mathrm{i}S_2(r),
\]

separates axial concentration, (R_2(r)=|F_2(r)|), from orientation, (\alpha_2(r)=\tfrac12\operatorname{atan2}(S_2(r),C_2(r))\pmod{\pi}). A provenance audit produced an exact 14-dimensional primary vector containing eight radial-magnitude descriptors and six doubled-angle, axial-safe descriptors. No PCA, semantic labels, von Mises fitting, historical 28-dimensional assembly, or full angular-density reconstruction is used.

To quantify information retained after harmonic phase is omitted, two gradient-boosting regressors reconstructed (C_2) and (S_2) from radius and (|F_2|). Five category-balanced folds withheld complete garment identities and had zero identity overlap. Identity-disjoint reconstruction achieved whole-field (R_2) RMSE (0.145610) and Pearson (r=0.926390); at each sketch's observed peak shell, RMSE was (0.148303), Pearson (r=0.810543), and median axial error was (4.104^\circ) (garment-cluster bootstrap 95% CI (3.815^\circ)–(4.512^\circ)).

Across 230 garment-identity medians, observed peak-shell (R_2) was negatively associated with axial error (Spearman (\rho=-0.355875), 95% CI (-0.455749) to (-0.248336), category-stratified Holm-adjusted (p=0.000200)). Selected peak radius showed a weaker association ((\rho=-0.207675), 95% CI (-0.322472) to (-0.095626), adjusted (p=0.030097)). Low/high-error contrasts were directionally stable across four prespecified thresholds.

The study establishes a reproducible geometric measurement and dependency-aware validation framework, not semantic recognition, causality, a physical radial law, or a prospective reliability classifier. Inference remains conditional on independence of the 230 recovered garment identities.

**Keywords:** garment sketches; radial–angular representation; second angular harmonic; axial statistics; grouped cross-validation; cluster bootstrap; computational provenance
