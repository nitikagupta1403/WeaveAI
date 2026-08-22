# Abstract

Garment sketches encode form through sparse foreground structure distributed across radius and angle. We present an explicit radial–angular representation of all 2,300 CLO-SKET sketches, comprising 23 categories and 230 recovered garment identities. Foreground intensity is accumulated in centroid-relative polar bins to estimate the shell-conditional angular distribution \(p(\theta\mid r)\). Its second harmonic,

\[
F_2(r)
=
\sum_k p(\theta_k\mid r)e^{-i2\theta_k}
=
C_2(r)-iS_2(r),
\]

provides harmonic magnitude

\[
R_2(r)=|F_2(r)|
\]

and axial orientation

\[
\alpha_2(r)
=
\frac12\operatorname{atan2}(S_2(r),C_2(r))
\pmod{\pi}.
\]

The resulting 14-dimensional representation contains eight radial-magnitude and six doubled-angle axial descriptors. The choice \(m=2\) follows from the axial orientation quantity targeted by the representation: it is the lowest non-zero harmonic compatible with the equivalence \(\theta\equiv\theta+\pi\).

To evaluate information retained after explicit phase is omitted, \(C_2\) and \(S_2\) were reconstructed from radius and \(R_2\) using five category-balanced, garment-identity-disjoint folds. Whole-field reconstructed \(R_2\) achieved RMSE \(0.145610\) and Pearson \(r=0.926390\); peak-shell RMSE was \(0.148303\), Pearson \(r=0.810543\), and median axial error was \(4.104^\circ\).

Rigid-image and analytic rotation controls separated representation behavior from coordinate-frame dependence. Under raster rotations of \(\pm5^\circ\), \(\pm10^\circ\), and \(\pm20^\circ\), radial-magnitude quantities showed small median perturbations and doubled-angle orientation pairs tracked the imposed rotations under the expected \(R(2\phi)\) action; magnitude-weighted orientation had 95th-percentile equivariance error below \(0.85^\circ\). Separately, common global analytic rotations preserved coordinate-free reconstruction performance, whereas independent garment-identity rotations increased median axial error to \(44.675^\circ\), approximately the \(45^\circ\) axial chance level. Thus, the representation exhibited its intended invariant/equivariant organization over the tested rigid-image rotations, while radius and harmonic magnitude did not intrinsically determine phase: successful phase reconstruction depended substantially on shared orientation structure in the canonical image frame.

Sensitivity analyses showed that integrated magnitude, radial centroid, and radial spread were more stable than localized peak- and support-based descriptors. Peak radius was particularly domain-sensitive: 22.0% of primary peaks occurred at a domain endpoint.

At the garment-identity level, observed peak \(R_2\) was negatively associated with axial error (\(\rho=-0.356\)), while Cartesian reconstruction perturbation (\(\rho=+0.760\)) and the theoretically motivated phase-conditioning quantity \(\|\Delta(C_2,S_2)\|/(2R_2)\) (\(\rho=+0.789\)) tracked angular error more strongly.

CLO-SKET therefore provides an explicit, identity-aware geometric measurement framework for repeated garment sketches while exposing its coordinate dependence, numerical sensitivity, and inferential limits.

**Keywords:** garment sketches; radial–angular representation; axial harmonics; Fourier descriptors; grouped cross-validation; rotation equivariance; phase conditioning
