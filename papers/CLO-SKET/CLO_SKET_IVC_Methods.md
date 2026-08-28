# 3. Methods

## 3.1 Study design and scope

The study was organized around two complementary questions: **how does the axial–radial representation describe garment-sketch geometry, and does that geometry contribute predictive information beyond morphology when complete source garments are withheld?**

The first part characterizes the representation itself. Foreground sketch evidence is expressed relative to the sketch centroid, organized into radial shells, and summarized through shell-conditioned second-harmonic magnitude and axial orientation. These shell-wise quantities are reduced to a compact 14-dimensional vector containing eight radial and six axial descriptors. Rotation, reconstruction, discretization, harmonic-order, phase-conditioning, and sensitivity analyses are used to examine how these measurements behave and where their numerical limits arise.

The second part evaluates predictive contribution. A frozen 135-dimensional morphology representation is compared with the same representation augmented by the 14-dimensional axial–radial vector. All feature sets use the same category-balanced, garment-identity-disjoint folds, preprocessing, and fixed classifier. The primary estimand is the change in macro-F1 obtained by adding the complete axial–radial representation to morphology; radial-only and axial-only additions are used as ablations to locate the source of any increment.

The compact representation is constructed directly from explicit geometric measurements. It does not use principal-component analysis, a learned embedding, semantic segmentation, von Mises fitting, or reconstruction of the complete angular density.

Finally, predictive increment and exact garment-level correspondence are evaluated separately. A category-preserving identity-block permutation reassigns complete axial–radial garment blocks within category while preserving repeated-observation structure. This comparison tests whether any predictive advantage depends on pairing morphology with axial–radial geometry from the exact same garment rather than only on category-conditioned geometric information.

---

## 3.2 Dataset and garment-identity reconstruction

The analysis used all 2,300 images in the CLO-SKET dataset across 23 garment categories. Source-garment identity was reconstructed from the category-qualified source identifier encoded in each filename, while the accompanying replicate identifier denoted the repeated sketch associated with that garment.

This procedure recovered

\[
N_{\mathrm{id}}=230
\]

garment identities, exactly 10 within each category. Individual identities contained 9–11 sketches because of irregular filename records.

All 2,300 file paths were unique. SHA-256 hashing detected no repeated raw files, and hashing of decoded pixel arrays detected no repeated decoded images. Perceptual hashing was used only to identify visually similar candidate pairs and was not interpreted as evidence of file duplication or shared lineage.

Recovered garment identity was treated as the indivisible clustering unit for cross-validation, bootstrap resampling, and prespecified association analysis. The resulting inference concerns these recovered garment identities; extension to a wider population assumes that they can be treated as independent sampling units.

---

## 3.3 Raw-image radial–angular construction

The radial–angular representation was constructed directly from the original grayscale TIFF images at native spatial resolution. Rather than first extracting a binary contour, the construction retains continuous foreground darkness. No thresholding, binarization, resizing, rotation, straightening, or principal-axis alignment was applied.

For sketch \(i\), let \(I_{ip}\in[0,255]\) denote the grayscale intensity of pixel \(p\). Continuous foreground darkness was defined as

\[
w_{ip}
=
\max\left(255-I_{ip},\,0\right).
\]

Thus each sketch is treated as a spatial distribution of foreground mass: darker pixels contribute more weight, while white background pixels contribute zero.

For an image of width \(W_i\) and height \(H_i\), a common isotropic scale was defined as

\[
S_i
=
\max(W_i,H_i).
\]

Pixel coordinates \((u_{ip},v_{ip})\) were mapped to an aspect-ratio-preserving isotropic coordinate system,

\[
x_{ip}
=
\frac{u_{ip}-(W_i-1)/2
}{
S_i
},
\qquad
y_{ip}
=
\frac{
v_{ip}-(H_i-1)/2
}{
S_i
}.
\]

The same scale factor was used for both axes, preserving the image aspect ratio rather than stretching \(x\) and \(y\) independently. This normalization expresses position relative to the native image canvas; it does not impose physical scale invariance.

The darkness-weighted centroid was

\[
c_{x,i}
=
\frac{
\sum_p w_{ip}x_{ip}
}{
\sum_p w_{ip}
},
\qquad
c_{y,i}
=
\frac{
\sum_p w_{ip}y_{ip}
}{
\sum_p w_{ip}
}.
\]

Centroid-relative coordinates were then

\[
\widetilde x_{ip}
=
x_{ip}-c_{x,i},
\qquad
\widetilde y_{ip}
=
y_{ip}-c_{y,i},
\]

with Euclidean radius

\[
R_{ip}
=
\sqrt{
\widetilde x_{ip}^{\,2}
+
\widetilde y_{ip}^{\,2}
},
\]

and polar angle

\[
\theta_{ip}
=
\operatorname{atan2}
\left(
\widetilde y_{ip},
\widetilde x_{ip}
\right).
\]

Radial position was then expressed relative to the maximum centroid-relative foreground extent within each sketch. This converts absolute canvas-relative radius into a within-sketch normalized coordinate while leaving the preprocessing convention itself unchanged:

\[
R_{i,\max}
=
\max_p R_{ip},
\]

\[
\rho_{ip}
=
\frac{
R_{ip}
}{
R_{i,\max}
},
\qquad
0\leq\rho_{ip}\leq1.
\]

The normalized radial coordinate was divided into 72 equal-width bins with edges

\[
e_j^{(r)}
=
\frac{j}{72},
\qquad
j=0,\ldots,72.
\]

The corresponding normalized radial-bin centres were

\[
\rho_j
=
\frac{
j+\tfrac12
}{
72
},
\qquad
j=0,\ldots,71.
\]

For reporting and descriptor construction, these centres were expressed in shell-coordinate units,

\[
r_j
=
72\rho_j
=
j+\frac12,
\]

so that the full radial grid is

\[
r_j
=
0.5,1.5,\ldots,71.5.
\]

Angular position was divided into 72 equal-width bins over

\[
[-\pi,\pi],
\]

with edges

\[
e_k^{(\theta)}
=
-\pi
+
k\frac{2\pi}{72},
\qquad
k=0,\ldots,72.
\]

Each angular bin therefore spans

\[
5^\circ.
\]

Let

\[
H_i(r_j,\theta_k)
\]

denote the accumulated darkness mass of pixels assigned jointly to radial bin \(j\) and angular bin \(k\):

\[
H_i(r_j,\theta_k)
=
\sum_p
w_{ip}
\,
\mathbf 1
\left[
\rho_{ip}\in B_j^{(r)}
\right]
\mathbf 1
\left[
\theta_{ip}\in B_k^{(\theta)}
\right].
\]

Pixels with \(\rho_{ip}=1\) were retained in the final radial bin.

For radial shell \(r_j\), define its accumulated darkness mass as

\[
M_i(r_j)
=
\sum_{k=1}^{72}
H_i(r_j,\theta_k).
\]

For nonempty shells,

\[
M_i(r_j)>10^{-14},
\]

the conditional angular distribution was

\[
p_i(\theta_k\mid r_j)
=
\frac{
H_i(r_j,\theta_k)
}{
M_i(r_j)
},
\]

so that

\[
\sum_{k=1}^{72}
p_i(\theta_k\mid r_j)
=
1.
\]

Empty radial shells were represented by zeros.

Conditioning within each shell separates **how foreground evidence is distributed angularly** from **how much foreground mass the shell contains**. A shell with more ink therefore does not dominate the angular statistic merely because it carries more total intensity.

The \(10^{-14}\) criterion is an empty-shell numerical guard rather than a substantive foreground-support threshold. To assess whether shell conditioning or peak selection was being driven by numerically nonempty but negligibly supported shells, a post hoc source-image support audit was performed over the frozen 25-shell primary domain. For each sketch, shell darkness mass was expressed as a fraction of total sketch darkness mass. Audit-only minimum relative shell-mass thresholds from \(10^{-5}\) to \(5\times10^{-3}\) were then applied without altering the locked representation or Experiment 06.

---

## 3.4 Angular harmonics and axial orientation

Once the angular distribution has been normalized within each shell, its directional organization can be summarized through circular harmonics. For harmonic order \(m\), the complex angular moment at radial shell \(r_j\) was

\[
F_{m,i}(r_j)
=
\sum_{k=1}^{72}
p_i(\theta_k\mid r_j)
e^{-\mathrm{i}m\theta_k}.
\]

The negative exponential follows the discrete Fourier-transform convention used throughout the implementation.

For the axial geometry considered here, the primary analysis uses \(m=2\):

\[
F_{2,i}(r_j)
=
C_{2,i}(r_j)
-
\mathrm{i}S_{2,i}(r_j),
\]

where

\[
C_{2,i}(r_j)
=
\sum_k
p_i(\theta_k\mid r_j)
\cos(2\theta_k),
\]

and

\[
S_{2,i}(r_j)
=
\sum_k
p_i(\theta_k\mid r_j)
\sin(2\theta_k).
\]

The second-harmonic magnitude is

\[
R_{2,i}(r_j)
=
|F_{2,i}(r_j)|
=
\sqrt{
C_{2,i}(r_j)^2+
S_{2,i}(r_j)^2
}.
\]

For later descriptor construction, we use the shorthand

\[
m_i(r_j)
\equiv
R_{2,i}(r_j).
\]

The associated axial orientation is

\[
\alpha_{2,i}(r_j)
=
\frac12
\operatorname{atan2}
\left(
S_{2,i}(r_j),
C_{2,i}(r_j)
\right)
\pmod{\pi}.
\]

Because the orientation describes an axis rather than a directed vector, opposite directions represent the same orientation:

\[
\alpha
\equiv
\alpha+\pi.
\]

Axial angular distance was therefore defined as

\[
d_{\mathrm{ax}}(a,b)
=
\min
\left[
|a-b|\bmod\pi,\,
\pi-(|a-b|\bmod\pi)
\right],
\]

which lies on

\[
[0,\pi/2].
\]

Reported angular errors are expressed on the equivalent interval

\[
[0^\circ,90^\circ].
\]

---

## 3.5 Why the second harmonic is the primary angular statistic

The choice \(m=2\) follows directly from the symmetry of the quantity being represented. Garment orientation is treated as axial: an axis at angle \(\theta\) is equivalent to the same axis at \(\theta+\pi\). The harmonic order is therefore determined by the geometry rather than selected retrospectively from predictive performance.

Under a \(180^\circ\) reversal,

\[
\theta
\mapsto
\theta+\pi.
\]

For harmonic order \(m\),

\[
e^{-\mathrm{i}m(\theta+\pi)}
=
e^{-\mathrm{i}m\theta}
e^{-\mathrm{i}m\pi}
=
(-1)^m
e^{-\mathrm{i}m\theta}.
\]

Hence

\[
F_m(\theta+\pi)
=
(-1)^mF_m(\theta).
\]

Odd harmonics change sign under axial reversal, whereas even harmonics are invariant. Consequently,

\[
m=2
\]

is the lowest non-zero harmonic compatible with this axial equivalence.

The higher even harmonic \(m=4\) is also axially invariant but represents finer angular organization. Harmonics \(m=1\) and \(m=3\) were used as directional controls and \(m=4\) as a higher-order axial control; these comparisons were descriptive and did not redefine the primary \(m=2\) representation.

---

## 3.6 Primary radial domain and peak quantities

The reported shell coordinate \(r_j=j+\tfrac12\) is a dimensionless bin-coordinate representation of the sketch-normalized radius \(\rho_j=(j+\tfrac12)/72\); it is not a physical pixel distance.

The shell field was summarized over a fixed primary radial domain containing 25 shell centers,

\[
\mathcal R
=
\{3.5,4.5,\ldots,27.5\}.
\]

For sketch \(i\), the observed peak shell was

\[
j_i^\star
=
\arg\max_{j:r_j\in\mathcal R}
m_i(r_j),
\]

with peak radius

\[
r_i^\star
=
r_{j_i^\star},
\]

and peak magnitude

\[
m_i^\star
=
m_i(r_i^\star).
\]

Because

\[
m_i(r)=R_{2,i}(r)=|F_{2,i}(r)|,
\]

the peak magnitude can equivalently be written as

\[
m_i^\star
=
R_{2,i}(r_i^\star)
=
|F_{2,i}(r_i^\star)|.
\]

These expressions denote the same measured quantity rather than separate features.

The peak radius identifies where second-harmonic organization is strongest within the chosen radial window. Because it is a discrete argmax on a finite domain, its boundary occupancy and radial-domain sensitivity were evaluated separately.

---

## 3.7 Eight radial-magnitude descriptors

The radial component of RA14 summarizes **how second-harmonic magnitude is distributed across radius**. Let

\[
m_i(r)=R_{2,i}(r)
\]

over the primary domain \(\mathcal R\). Integrals were evaluated using the trapezoidal rule at radial-shell centers. Their units are radial-bin-coordinate units rather than physical distance, and the integrated magnitude is not interpreted as Fourier energy.

### Integrated magnitude

\[
I_i
=
\int_{\mathcal R}
m_i(r)\,dr.
\]

### Magnitude-weighted radial centroid

\[
\bar r_i
=
\frac{
\int_{\mathcal R}
r\,m_i(r)\,dr
}{
I_i
}.
\]

### Magnitude-weighted radial spread

\[
s_{r,i}
=
\sqrt{
\frac{
\int_{\mathcal R}
(r-\bar r_i)^2m_i(r)\,dr
}{
I_i
}
}.
\]

### Peak concentration

With \(r_i^\star\) denoting the discrete peak location, radial concentration was defined as the fraction of integrated magnitude within four shell-coordinate units of the peak,

\[
q_i
=
\frac{
\int_{
\mathcal R\cap
[r_i^\star-4,r_i^\star+4]
}
m_i(r)\,dr
}{
I_i
}.
\]

### Support onset and termination

Let

\[
\tau_i
=
0.10\,m_i^\star.
\]

The support onset and termination radii were

\[
r_i^{\mathrm{on}}
=
\min
\{
r\in\mathcal R:
m_i(r)\geq\tau_i
\},
\]

and

\[
r_i^{\mathrm{off}}
=
\max
\{
r\in\mathcal R:
m_i(r)\geq\tau_i
\}.
\]

Together, these quantities describe total radial magnitude, its location and spread, concentration around the strongest shell, threshold-defined support, and the observed peak. The eight radial features were therefore

\[
\mathbf x_i^{(F_2)}
=
[
I_i,\,
\bar r_i,\,
s_{r,i},\,
q_i,\,
r_i^{\mathrm{on}},\,
r_i^{\mathrm{off}},\,
r_i^\star,\,
m_i^\star
]
\in\mathbb R^8.
\]

Radial extent,

\[
r_i^{\mathrm{off}}
-
r_i^{\mathrm{on}},
\]

was not added separately because it is exactly determined by the retained onset and termination coordinates.

---

## 3.8 Six axial descriptors

The axial component summarizes **how the dominant undirected orientation changes across radius**. The peak axial orientation was

\[
\alpha_i^\star
=
\alpha_{2,i}(r_i^\star).
\]

To obtain a single mean axis while respecting \(180^\circ\) equivalence, a magnitude-weighted doubled-angle resultant was constructed as

\[
Z_i
=
\sum_{r_j\in\mathcal R}
m_i(r_j)
e^{\mathrm{i}2\alpha_{2,i}(r_j)},
\]

with

\[
\bar\alpha_i
=
\frac12
\arg(Z_i)
\pmod{\pi}.
\]

Axial coherence was

\[
\kappa_i
=
\frac{
|Z_i|
}{
\sum_{r_j\in\mathcal R}
m_i(r_j)
},
\qquad
0\leq\kappa_i\leq1.
\]

Orientation drift across the primary radial domain was

\[
\delta_i
=
d_{\mathrm{ax}}
\left[
\alpha_{2,i}(3.5),
\alpha_{2,i}(27.5)
\right].
\]

Raw axial angles were not entered directly into the Euclidean feature vector because ordinary angles would incorrectly distinguish opposite directions of the same axis. Peak and mean orientations were instead encoded in doubled-angle Cartesian form:

\[
\mathbf x_i^{(\alpha_2)}
=
[
\cos(2\alpha_i^\star),\,
\sin(2\alpha_i^\star),\,
\cos(2\bar\alpha_i),\,
\sin(2\bar\alpha_i),\,
\kappa_i,\,
\delta_i
]
\in\mathbb R^6.
\]

This encoding is invariant under

\[
\alpha
\mapsto
\alpha+\pi.
\]

Additional persistence and weighted-dispersion summaries were not retained because they were redundant with the selected coordinates. Algebraically reconstructed quantities were used only for numerical consistency checks and were not added as separate features.

---

## 3.9 Primary 14-dimensional representation

The radial and axial summaries together define the final sketch-level axial–radial representation:

\[
\mathbf x_i
=
\left[
\mathbf x_i^{(F_2)}
\mid
\mathbf x_i^{(\alpha_2)}
\right]
\in
\mathbb R^{14}.
\]

The representation matrix therefore had dimensions

\[
2300\times14.
\]

The eight radial and six axial coordinates were concatenated in the order defined above. An independent reconstruction of both feature blocks reproduced the stored 14-dimensional representation exactly: the maximum absolute numerical difference was zero, and all values were finite.

---

## 3.10 Rigid-image rotation control of the 14-dimensional representation

Before testing predictive value, we examined how the completed 14-dimensional representation behaves when the input sketch itself is rigidly rotated and the full radial–angular measurement is recomputed. This image-domain perturbation complements the later analytic coordinate-frame controls by testing the representation after image interpolation, padding, and complete remeasurement. The control is descriptive; the separate prospectively gated mechanical audit is reported in Section 3.18.

All 2,300 sketches were evaluated using Pillow raster rotation arguments

\[
\beta
\in
\{-20^\circ,-10^\circ,-5^\circ,0^\circ,5^\circ,10^\circ,20^\circ\}.
\]

The value \(\beta\) was passed directly to `PIL.Image.rotate`. The radial–angular measurement itself uses native image coordinates in which pixel row increases downward. Consequently, the angular increment in the measurement coordinate system has the opposite sign,

\[
\phi=-\beta.
\]

The transformation equations below are written in terms of this measurement-coordinate increment \(\phi\). Equivalently, a positive Pillow raster angle \(\beta\) produces an ideal axial shift of \(-\beta\) in the native image-coordinate angular convention.

This control was label-free and did not fit or refit any predictive model.

To prevent clipping of the original rectangular sketch under rotation, each grayscale image was first embedded in a square white canvas whose side length was at least the diagonal of the original image,

\[
L_i
=
\left\lceil
\sqrt{H_i^2+W_i^2}
\right\rceil,
\]

with a one-pixel parity adjustment where required to maintain centered embedding. The same padded canvas was used for the reference condition and every rotated condition.

For non-zero \(\phi\), the padded grayscale image was rotated using bilinear interpolation with fixed canvas size,

\[
\texttt{expand=False},
\]

and white background fill,

\[
\texttt{fillcolor}=255.
\]

The \(0^\circ\) condition used the same padded canvas without interpolation.

After rotation, the complete radial-angular construction was rerun from the rotated grayscale image using the same frozen measurement procedure as for the primary representation. No descriptor definition, radial domain, angular discretization, or post-processing rule was changed for the rotation control.

Writing the transformation in terms of the measurement-coordinate increment \(\phi=-\beta\), the second harmonic ideally satisfies

\[
F_2'(r)
=
e^{-i2\phi}F_2(r),
\]

so that

\[
R_2'(r)
=
R_2(r).
\]

Accordingly, radial and magnitude-derived quantities were evaluated as approximately rotation-invariant numerical descriptors.

For an axial orientation \(\alpha\),

\[
\alpha'
=
\alpha+\phi
\pmod{\pi}.
\]

Its doubled-angle Cartesian representation therefore transforms as

\[
\begin{bmatrix}
\cos 2\alpha'\\
\sin 2\alpha'
\end{bmatrix}
=
\begin{bmatrix}
\cos 2\phi & -\sin 2\phi\\
\sin 2\phi & \cos 2\phi
\end{bmatrix}
\begin{bmatrix}
\cos 2\alpha\\
\sin 2\alpha
\end{bmatrix}.
\]

Thus, the peak-orientation and magnitude-weighted mean-orientation coordinate pairs were evaluated as axial-equivariant quantities under the expected \(R(2\phi)\) action.

Axial coherence,

\[
\kappa_i,
\]

and orientation drift,

\[
\delta_i,
\]

were treated as rotation-invariant scalar descriptors because they depend on relative rather than absolute axial orientation.

Numerical stability of the radial-magnitude field was summarized by the normalized mean absolute error of the primary-domain \(R_2(r)\) profile relative to the \(0^\circ\) reference. Axial equivariance was evaluated by decoding the rotated doubled-angle orientation pairs and comparing the observed orientation shift with the expected measurement-coordinate increment \(\phi=-\beta\). Coherence and orientation drift were evaluated by their absolute changes from the reference condition.

The rotation control therefore characterizes empirical behavior over the tested angle range. Exact transformation behavior is examined separately by the analytic and prospectively gated controls described later.

---

## 3.11 Prespecified incremental representation-value experiment

Experiment 06 asked the central predictive question: does the frozen compact axial–radial representation add garment-category information beyond the frozen 135-dimensional morphology representation? Seven prespecified feature sets separated standalone, ablation, and augmented comparisons: (R), (A), (R+A), (M), (M+R), (M+A), and (M+R+A), with dimensions 8, 6, 14, 135, 143, 141, and 149. The primary contrast was

\[
\Delta F_1=F_1^{\mathrm{macro}}(M+R+A)-F_1^{\mathrm{macro}}(M),
\]

with \(\Delta BA=BA(M+R+A)-BA(M)\) secondary. Radial-only and axial-only additions were mechanistic ablations and could not replace the primary contrast.

The compact 14-dimensional experiment was prespecified and locked before its own outcome was computed. An earlier broader 28-dimensional radial–angular representation had already produced a positive result (macro-F1 increment +0.070984; balanced-accuracy increment +0.073043), so Experiment 06 was not historically blind to the possibility of improvement. That prior exposure was recorded in the design lock. The compact representation itself, its primary contrast, estimator, validation unit, bootstrap count, repeated-partition count, and alignment-permutation count were frozen before any compact-representation outcome was computed.

## 3.12 Locked estimator and grouped validation

Every feature set used training-fold `StandardScaler` followed by `LogisticRegression` with L2 penalty, \(C=1.0\), `solver=lbfgs`, `max_iter=5000`, `class_weight=None`, and `random_state=20260820`. No hyperparameter search or feature-set-specific classifier change was performed.

Five deterministic category-balanced folds were constructed over the 230 garment identities. Each fold held out exactly two complete identities from each of 23 categories (46 test identities; 184 train identities), with zero identity overlap. Every sketch appeared in exactly one test fold; test-row counts were 459, 460, 462, 460, and 459 sketches because identity block sizes varied slightly. Macro-F1 (primary) and balanced accuracy (secondary) were computed from pooled out-of-fold predictions.

## 3.13 Paired garment-identity bootstrap

Primary-effect uncertainty was estimated from paired frozen out-of-fold predictions using 5,000 complete-garment-identity bootstrap replicates (random state 20260820). Sampling an identity included all its sketches for both models.

The prespecified unrestricted bootstrap was retained as the primary resampling analysis. Because some replicates omitted an entire category, a category-stratified robustness analysis was added without model refitting or feature changes. It sampled 10 identities with replacement within each of the 23 categories, preserving every category in every replicate. Percentile 95% confidence intervals were the 2.5th and 97.5th percentiles of paired metric differences. Fraction-positive values were reported descriptively rather than interpreted as permutation probabilities.

## 3.14 Repeated grouped-partition stability

Ten complete repetitions of five-fold category-balanced grouped cross-validation used seeds 20260820 through 20260829. Within each repeat, every category again contributed exactly two identities to each test fold. The estimator, preprocessing, features, and outcomes remained fixed.

The repeated analysis evaluated (M), (M+R), and (M+R+A). For every repeat, pooled out-of-fold macro-F1 and balanced accuracy were computed and the full augmented-minus-morphology difference retained; the (M+R-M) macro-F1 difference was retained as radial-ablation stability. All 10 repeats and all 50 constituent folds were retained.

## 3.15 Category-preserving identity-alignment permutation

A separate control tested whether augmented-model utility required exact garment-level pairing. Complete (R+A) identity blocks were reassigned within garment category while also matching identity block size. Thus category composition and 9-, 10-, or 11-sketch repeated-measure structure were preserved while exact morphology–axial–radial correspondence was disrupted.

Dress, Harem, and Jumpsuit each contained singleton 9-sketch and 11-sketch category-by-size strata, so those six identities necessarily self-mapped. The audited null retained the same identity for 2.6087% of rows and misaligned 97.3913% in every permutation.

For each of 2,000 permutations, the same five frozen grouped folds, fold-local standardization, and locked logistic-regression specification were used to fit and evaluate (M+R+A_{\pi}). The null statistic was its performance increment over the frozen morphology baseline. The one-sided corrected empirical probability was

\[
p=\frac{1+\sum_{b=1}^{B}\mathbf 1[\Delta_b^{\mathrm{null}}\geq\Delta_{\mathrm{obs}}]}{B+1},
\qquad B=2000.
\]

The test was evaluated for macro-F1 and balanced accuracy. Its target is specific: whether **correct garment-level alignment is more useful than category-preserving misalignment**. Incremental predictive utility itself is established by the augmented-minus-morphology comparison above.

## 3.16 Claim hierarchy for Experiment 06

Experiment 06 separates three levels of evidence. Standalone (R), (A), or (R+A) performance shows that the corresponding representation carries discriminative information. A positive (M+R+A-M) contrast supported by garment-identity bootstrap uncertainty and repeated grouped partitions supports reproducible **incremental predictive utility** beyond morphology. The radial and axial ablations then indicate where that observed increment is concentrated. A distinct **garment-specific correspondence** claim requires the correctly aligned effect to exceed the category-preserving, block-size-matched misalignment null.

Accordingly,

\[
\text{incremental utility}\not\Rightarrow\text{garment-specific correspondence}.
\]

The interpretation therefore distinguishes predictive increment from exact garment-level correspondence; broader semantic or causal interpretations are outside the tested design.

## 3.17 Secondary conventional-image-descriptor baseline (Experiment 07)

To address the reviewer-facing question of whether the compact axial–radial representation adds predictive information beyond a conventional image descriptor, a secondary post-audit baseline was frozen before any Experiment 07 outcome was computed. This analysis did not alter Experiment 06, its features, folds, estimator, or claims.

The conventional descriptor was histogram of oriented gradients (HOG). Each native grayscale TIFF sketch was converted to an aspect-ratio-preserving 256×256 representation by isotropic bilinear resizing followed by centered white padding; images were not geometrically stretched. Pixel values were scaled to [0,1]. HOG used 9 orientations, 16×16-pixel cells, 2×2-cell blocks, L2-Hys block normalization, `transform_sqrt=False`, `feature_vector=True`, and no channel axis, producing 8,100 features per sketch. No HOG hyperparameter search, PCA, feature selection, augmentation, or outcome-dependent preprocessing was performed.

The exact 2,300×14 axial–radial matrix, category labels, garment identities, and row-level fold assignment were recovered from the frozen Experiment 06 checkpoint. The checkpoint fold map was adopted as authoritative because it reproduced the locked Experiment 06 pooled results to numerical precision: morphology macro-F1 0.297788 and balanced accuracy 0.298261; morphology plus the complete axial–radial block macro-F1 0.335765 and balanced accuracy 0.336087. The authoritative Experiment 07 test-fold sizes were 459, 460, 462, 460, and 459 sketches, with 46 held-out garment identities per fold, 184 training identities, and zero train/test garment-identity overlap in every fold.

Row order was bridged independently to the archived runtime image paths. Category labels matched exactly; the eight-dimensional radial block reproduced the archived runtime radial matrix exactly; and the six-dimensional axial block reproduced the archived runtime axial descriptors exactly. The frozen HOG matrix had shape 2,300×8,100, contained only finite values, and was hashed before classification.

Two feature sets were then evaluated under the same fold-local preprocessing and classifier specification used in Experiment 06:

\[
\mathrm{HOG}_{8100}
\]

and

\[
\mathrm{HOG}_{8100}\oplus\mathbf z_{RA,14}.
\]

For each fold, `StandardScaler` was fitted on the training partition only, followed by `LogisticRegression` with L2 penalty, \(C=1.0\), `solver=lbfgs`, `max_iter=5000`, `class_weight=None`, and `random_state=20260820`. The primary Experiment 07 contrast was pooled out-of-fold macro-F1 for HOG+RA14 minus HOG; balanced accuracy was secondary. No model or descriptor setting was changed after outcomes were observed.

Uncertainty for the final HOG+RA14-minus-HOG contrast was quantified without model refitting by a paired bootstrap over the 230 garment identities. Complete garment identities were sampled with replacement for 5,000 replicates using seed 20260820, and all sketches and both paired out-of-fold prediction sets for a sampled identity were retained together. Percentile 95% intervals were defined by the 2.5th and 97.5th percentiles of the paired metric-difference distribution. Because an unrestricted identity bootstrap can omit all true examples of a category in occasional replicates, these intervals are reported as identity-level paired bootstrap intervals rather than as a separate permutation test.

Experiment 07 is interpreted strictly as a secondary conventional-descriptor comparator. It tests whether the explicit 14-dimensional axial–radial representation supplies measurable incremental predictive benefit after a high-dimensional local-gradient representation is already present; it is not a new primary hypothesis and does not replace the prespecified Experiment 06 comparison against morphology.

## 3.18 Fresh reproducibility audit: Experiment 08

After the frozen Experiment 06 and Experiment 07 analyses, Experiment 08 provided a fresh executable audit of RA14 under a prospectively frozen mechanical gate and a frozen learned-feature comparison. It used the same 2,300 sketches, 230 recovered garment identities, and frozen 14-dimensional RA14 representation, together with independently frozen DINOv2 ViT-S/14 features. Two additional predictive controls were specified later, after Experiment 08 had already entered a post-outcome exploratory phase, and were committed before their own execution.

The mechanical gate determined whether the subsequent predictive comparison could be interpreted confirmatorily. Analytic harmonic rotation checks passed, and raster axial-angle errors satisfied their locked criteria. The raster harmonic-magnitude criterion did not: median relative magnitude error was 1.3132%, while the 95th percentile was 21.332%, exceeding the prespecified 15% threshold. The overall frozen mechanical gate therefore failed.

Predictive analysis was subsequently completed, but all Experiment-08 predictive results are interpreted as **post-outcome / exploratory**. The frozen DINOv2 comparison and the later correspondence and repeated-partition controls are reported within that exploratory status and do not change the failed mechanical-gate result.

---

## 3.19 Representation diagnostics

A complementary diagnostic analysis examined how the shell-level second-harmonic field behaves under reconstruction, coordinate-frame changes, discretization choices, neighbouring harmonic orders, and phase perturbation. These analyses characterize the measurement itself and are distinct from the prespecified Experiment-06 predictive contrast and the separately prospectively gated Experiment-08 audit.

### 3.19.1 Garment-identity-disjoint shell-field reconstruction

The observed shell field was examined through out-of-fold reconstruction of its Cartesian second-harmonic components. For sketch \(i\) and primary-domain shell \(r_j\), the predictor vector was

\[
\mathbf z_{ij}
=
\left[
r_j,\,
R_{2,i}(r_j)
\right].
\]

Separate fixed regression models estimated

\[
\widehat C_{2,i}(r_j)
=
f_C(\mathbf z_{ij}),
\qquad
\widehat S_{2,i}(r_j)
=
f_S(\mathbf z_{ij}).
\]

Five category-balanced folds withheld complete recovered garment identities, so every sketch-shell row received an out-of-fold prediction from a model trained without that garment identity. Reconstruction was treated as a shared-source consistency diagnostic because \(R_2\), \(C_2\), and \(S_2\) all derive from the same conditional angular distribution; it was not interpreted as recovery of an independent physical or semantic target.

### 3.19.2 Coordinate-frame controls

Two analytic controls examined the dependence of reconstruction on the common image coordinate frame. First, the observed harmonic field was subjected to global physical rotations in doubled-angle space, preserving \(R_2\) while rotating \(C_2\) and \(S_2\). The same predictors, estimator specification, garment-identity-disjoint folds, and coordinate-free reconstruction metrics were retained.

Second, common absolute orientation was disrupted while preserving garment identity and repeated-sketch structure. One angle

\[
\phi_g
\sim
\operatorname{Uniform}(0,\pi)
\]

was assigned independently to each recovered garment identity \(g\), and all sketches belonging to that identity received the same rotation. Ten such randomizations were evaluated. This control preserves radius, \(R_2\), garment identity, repeated-sketch structure, category labels, and validation folds while removing shared absolute orientation across garment identities.

These analytic controls complement the earlier raster-image rotation experiment in Section 3.10, which recomputed the complete 14-dimensional representation after physical image rotation.

### 3.19.3 Parameter and discretization sensitivity

Sensitivity analyses varied fixed construction choices one at a time without redefining the primary representation. The tested factors included the radial-support threshold, concentration half-width, radial-domain boundaries, angular resolution, and radial resolution.

Angular and radial coarsening were performed by exact aggregation of the canonical 72-bin mass fields rather than by image interpolation. Radial-resolution comparisons additionally used a common normalized physical interval so that changes due to resolution could be separated from changes in radial-domain extent.

These analyses were used to distinguish globally aggregated descriptors from localized quantities whose values depend more strongly on the finite radial window or discretization. They were not used to select or optimize the primary parameterization.

### 3.19.4 Low-order harmonic control

The primary second harmonic was compared descriptively with neighbouring low-order harmonics

\[
m\in\{1,2,3,4\}
\]

computed from the same canonical shell-conditioned angular distributions.

The comparison was not a search for the empirically best harmonic order. Section 3.5 defines \(m=2\) from the axial symmetry of the represented orientation. The low-order analysis instead examined whether the second harmonic constituted a substantial and non-redundant component of the observed angular field.

### 3.19.5 Phase conditioning and garment-level association

Axial phase becomes poorly conditioned when the magnitude of its underlying Cartesian harmonic vector is small. For

\[
\alpha_2
=
\frac12
\operatorname{atan2}(S_2,C_2),
\]

the first-order differential is

\[
d\alpha_2
=
\frac{
C_2\,dS_2-S_2\,dC_2
}{
2R_2^2
},
\]

and therefore

\[
|d\alpha_2|
\leq
\frac{
\sqrt{dC_2^2+dS_2^2}
}{
2R_2
}.
\]

For the out-of-fold reconstruction, the Cartesian perturbation norm was

\[
E_{CS}
=
\sqrt{
(\widehat C_2-C_2)^2+
(\widehat S_2-S_2)^2
},
\]

giving the empirical conditioning quantity

\[
B_\alpha
=
\frac{E_{CS}}{2R_2}.
\]

Repeated sketches were reduced to garment-identity medians before the principal association summaries were calculated. Spearman associations compared median axial reconstruction error with observed peak-shell \(R_2\), Cartesian reconstruction error, and the combined conditioning quantities. Peak radius was retained only as a secondary sensitivity-qualified quantity because its definition depends on an argmax over a finite radial domain.

Detailed estimator settings, validation-unit comparisons, garment-cluster bootstrap procedures, category-stratified permutation inference, parameter grids, magnitude-stratified conditioning, outcome-defined error bands, and the algebraically coupled calibration diagnostic are reported in the Supplementary Methods.
