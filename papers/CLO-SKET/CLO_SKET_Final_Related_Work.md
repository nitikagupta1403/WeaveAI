# 2. Related Work

## 2.1 Garment sketches as computational geometry

Garment drawings have long served as geometric inputs to computational design systems. Yasseen et al. (2013) used contours sketched on a mannequin to construct quadrilateral garment meshes, while Fondevilla et al. (2021) transferred garment style from annotated fashion drawings to three-dimensional characters. Wang et al. (2018) learned a shared space connecting sketched fold patterns, sewing-pattern parameters, body shape, and simulated garments. Together, these studies show that sparse fashion drawings contain recoverable information about garment form.

Their main objective, however, is reconstruction, transfer, editing, or generation. The sketch is typically an input to a task-oriented model. CLO-SKET instead treats each sketch as an observational unit and asks a narrower measurement question: can its foreground geometry be summarized by an explicit radial–angular representation whose construction, dependencies, and limits are auditable?

## 2.2 Explicit garment-shape descriptors

Fashion-flat and silhouette research provides direct precedent for quantitative garment-shape representation. An and Li (2014) combined a wavelet Fourier descriptor with supervised dimensionality reduction and classification of fashion flats. Tsuru et al. (2021) used standardized silhouette measurements with multidimensional scaling and clustering to examine designer collections. These studies establish that garment outlines can be mapped to explicit numerical descriptors and analysed statistically.

More generally, Fourier descriptors encode periodic shape signals through harmonic coefficients (Zahn and Roskies, 1972), while geometric morphometrics offers alternative ways to compare curves and outlines (Bookstein, 1997; McCane, 2013). CLO-SKET does not claim novelty for Fourier analysis, outline measurement, polar coordinates, or population-level shape analysis individually. It also does not use a conventional landmark or semilandmark morphometric model. Its contribution is the audited combination of polar occupancy, a conditional angular distribution, and an axial second-harmonic summary for garment sketches.

## 2.3 Radial–angular representation and axial orientation

A centroid-referenced polar representation describes each retained foreground location by radius and angle,

\[
r=\sqrt{(x-c_x)^2+(y-c_y)^2},
\qquad
\theta=\operatorname{atan2}(y-c_y,x-c_x).
\]

This coordinate system separates distance from the sketch centroid from angular occupancy around it. Polar parameterizations also have garment-pattern precedent, although for a different task and representation (Oh and Kim, 2026).

For radial shell \(r_k\), CLO-SKET forms the observed conditional angular distribution

\[
p(\theta_j\mid r_k)
=
\frac{H(r_k,\theta_j)}
{\sum_{j'}H(r_k,\theta_{j'})},
\]

where \(H(r_k,\theta_j)\) is foreground occupancy in radial bin \(k\) and angular bin \(j\). The axial second harmonic is then

\[
F_2(r_k)
=
\sum_j p(\theta_j\mid r_k)e^{i2\theta_j}
=
C_2(r_k)+iS_2(r_k).
\]

The doubled angle is standard for axial data because orientations separated by \(\pi\) represent the same undirected axis (Jammalamadaka and SenGupta, 2001). The resultant magnitude and axial orientation are

\[
R_2(r_k)=|F_2(r_k)|
=\sqrt{C_2(r_k)^2+S_2(r_k)^2},
\qquad
\mu_2(r_k)
=
\tfrac12\operatorname{atan2}\!\left(S_2(r_k),C_2(r_k)\right)
\pmod{\pi}.
\]

Thus \(R_2\in[0,1]\) quantifies second-harmonic axial concentration, while \(\mu_2\) gives an orientation modulo \(180^\circ\). These are deterministic summaries of the observed histogram. No von Mises distribution is fitted, no likelihood-based concentration parameter is estimated, and the full angular density is not reconstructed from \(F_2\).

## 2.4 Auditable representation and reconstruction

The final primary representation is the exact 14-dimensional vector

\[
\mathbf{x}
=
\left[
\mathbf{x}_{F_2}^{(8)},
\mathbf{x}_{\alpha_2}^{(6)}
\right]
\in\mathbb{R}^{14},
\]

with a locked column order and exact concatenation audit. The eight \(F_2\)-family features summarize radial second-harmonic magnitude behaviour; the six \(\alpha_2\)-family features summarize axial-orientation behaviour. This is the study's primary representation. There is no PCA stage and no historical 28-dimensional family assembly in the audited analysis.

The reconstruction analysis has a deliberately limited role. From predictors \((r,|F_2(r)|)\), two regressors estimate

\[
\widehat C_2(r)=f_C(r,|F_2(r)|),
\qquad
\widehat S_2(r)=f_S(r,|F_2(r)|).
\]

These estimates imply \(\widehat R_2\) and \(\widehat\mu_2\) through the same vector identities used for the observations. Because the predictors and targets derive from the same observed angular field, this is a shared-source consistency diagnostic. It does not demonstrate semantic garment-part recognition, recover the full angular distribution, or establish a physical law.

## 2.5 Repeated sketches and identity-aware evaluation

The CLO-SKET data contain repeated sketches associated with recovered garment identities. Image-level splitting can therefore place sketches of the same garment in both training and test sets. Such a split evaluates unseen files but not transfer to unseen garments.

The audited design groups all sketches from a garment identity within the same fold. Five category-balanced folds each hold out two identities per category, and train/test garment-identity overlap is zero. Reconstruction is therefore evaluated out of fold on unseen recovered garment identities. For uncertainty estimation, complete garment identities—not individual sketches—are resampled. Confirmatory association tests first reduce each identity to medians and then permute within category strata. These choices address measured within-identity dependence, while inference remains conditional on the 230 recovered identities being mutually independent sampling units.

## 2.6 Research gap and study position

Prior work establishes that fashion drawings contain computationally useful geometry, garment contours can be represented explicitly, periodic shape signals admit harmonic summaries, and axial orientation requires circular rather than ordinary linear treatment. What remains less established is a complete evidence chain that keeps the representation, validation unit, algebraic dependencies, and claim boundary visible for a repeated-sketch garment dataset.

The present study therefore asks:

1. **Can CLO-SKET foreground geometry be encoded as an exact, interpretable 14-dimensional radial–angular vector without PCA or semantic labels?**
2. **How accurately do \((r,|F_2|)\) reconstruct the observed second-harmonic components for unseen garment identities?**
3. **How are observed peak-shell axial concentration and selected peak radius associated with axial reconstruction error after garment-level aggregation and category-stratified inference?**
4. **Are descriptive low/high-error contrasts stable across prespecified angular-error thresholds?**

The intended contribution is an auditable geometric measurement and validation framework. The study does not establish causality, semantic recognition, a physical radial law, a prospective reliability classifier, or human-like interpretation.
