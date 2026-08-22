# 5. Discussion

## 5.1 Principal findings

This study developed and evaluated an explicit radial–angular representation of garment sketches based on shell-conditioned angular Fourier moments. The final representation contains eight radial descriptors of second-harmonic magnitude and six axial-safe descriptors of second-harmonic orientation. Its purpose is not semantic garment recognition, but geometrically interpretable measurement of how foreground structure is distributed with radius and orientation around the sketch centroid.

Several findings define the contribution.

First, the second harmonic provides a mathematically natural description of axial garment-sketch organization. If orientation is undirected,

\[
\theta \equiv \theta+\pi,
\]

then

\[
F_m(\theta+\pi)=(-1)^mF_m(\theta).
\]

Even harmonics are therefore invariant under a \(180^\circ\) reversal, whereas odd harmonics are not. The choice \(m=2\) is consequently the lowest non-zero harmonic compatible with the required axial symmetry. The empirical low-order spectrum supports this choice without being used to select it retrospectively: among \(m=1,2,3,4\), the second harmonic had the largest median integrated and peak magnitudes, while remaining only moderately related to the higher even harmonic \(m=4\).

Second, garment identity is the appropriate internal unit for evaluating generalization in CLO-SKET. The dataset contains 2,300 sketches corresponding to 230 recovered garment identities, with approximately ten sketches per identity. Complete garment identities were therefore withheld during five-fold cross-validation. Under this identity-disjoint design, reconstructed second-harmonic magnitude remained strongly aligned with observation, with whole-field \(R_2\) RMSE \(=0.145610\) and Pearson \(r=0.926390\), peak-shell RMSE \(=0.148303\) and Pearson \(r=0.810543\), and median peak-shell axial error \(=4.104^\circ\).

Third, the reconstruction experiment is strongly dependent on the common image coordinate frame. Global analytic rotation left coordinate-free performance essentially unchanged, but assigning independent rotations to garment identities caused peak-shell axial error to approach the \(45^\circ\) chance expectation for an axial angle. Thus, radius and \(R_2\) do not intrinsically determine phase. The strong phase recovery observed in upright sketches depends substantially on population-level orientation structure relative to the common image axes.

Fourth, robustness differs substantially across descriptor families. Broad radial summaries such as integrated magnitude, radial centroid, and radial spread were comparatively stable under reasonable discretization and domain perturbations. Localized descriptors—particularly onset, termination, concentration, and peak radius—were more dependent on radial resolution and analysis boundaries. Approximately 22% of primary peak radii occurred at a radial-domain endpoint, and 40.9% of sketches whose primary peak occurred at the upper boundary moved beyond that boundary when the domain was expanded to 30.5. Peak radius must therefore be interpreted as a domain-conditioned localization statistic rather than an intrinsic physical scale.

Fifth, axial reconstruction error follows the expected conditioning geometry of harmonic phase. At the garment-identity level, observed peak \(R_2\) was negatively associated with axial error (\(\rho=-0.356\)), while Cartesian reconstruction perturbation showed a much stronger positive association (\(\rho=+0.760\)). Their combined conditioning quantity was more strongly associated still (\(\rho=+0.789\)). The weakest observed-\(R_2\) quartile had approximately twice the median axial error of the strongest quartile.

Together, these findings support a narrow interpretation: garment sketches contain measurable radial–angular structure that can be represented explicitly, but the interpretation of individual coordinates depends on symmetry, coordinate frame, numerical resolution, radial support, repeated-measure structure, and the conditioning geometry of phase estimation.

---

## 5.2 What the second angular harmonic measures

For each radial shell, the conditional angular distribution

\[
p(\theta\mid r)
\]

describes how foreground mass is distributed around the sketch centroid. Its second Fourier moment,

\[
F_2(r)
=
\sum_k
p(\theta_k\mid r)
e^{-i2\theta_k},
\]

can be written as

\[
F_2(r)
=
C_2(r)-iS_2(r)
=
R_2(r)e^{-i2\mu_2(r)}.
\]

The magnitude

\[
R_2(r)
=
\sqrt{C_2(r)^2+S_2(r)^2}
\]

measures the strength of second-order angular organization within that shell, while

\[
\mu_2(r)
=
\frac12\operatorname{atan2}(S_2(r),C_2(r))
\pmod{\pi}
\]

gives its undirected axial orientation.

This interpretation is geometric rather than semantic. A large \(R_2\) indicates that foreground mass within a shell is strongly organized according to a second-harmonic angular pattern. It does not identify sleeves, collars, waistlines, garment parts, or any other semantic attribute. Likewise, \(\mu_2\) describes the orientation of the harmonic axis; it does not establish a physical or functional garment direction.

The 14-dimensional representation preserves this distinction. Eight coordinates summarize how second-harmonic magnitude varies with radius, whereas six doubled-angle coordinates summarize axial orientation, coherence, and drift. Each coordinate therefore has an explicit geometric definition, but explicitness should not be confused with semantic sufficiency.

---

## 5.3 Why \(m=2\) is the primary harmonic

The primary harmonic order follows from the symmetry of the quantity being represented.

For a general angular harmonic,

\[
F_m(r)
=
\sum_k
p(\theta_k\mid r)e^{-im\theta_k},
\]

a \(180^\circ\) reversal produces

\[
F_m(\theta+\pi)
=
(-1)^mF_m(\theta).
\]

Odd harmonics therefore change sign under axial reversal, whereas even harmonics remain invariant. Because garment orientation in this representation is axial rather than directional, \(m=2\) is the lowest non-zero harmonic satisfying the required symmetry.

The low-order harmonic comparison is consistent with this rationale. Median integrated magnitudes for \(m=1,2,3,4\) were respectively 6.240, 7.891, 5.691, and 5.694. Median peak magnitudes were 0.592, 0.660, 0.533, and 0.540. The second harmonic exceeded \(m=4\) in integrated magnitude for 87.2% of sketches and in peak magnitude for 84.7%.

These empirical comparisons are supportive rather than determinative. A strong \(m=1\) or \(m=3\) component would indicate directional asymmetry in the sketch, not failure of the axial \(m=2\) representation. Similarly, \(m=4\) is also axially invariant but represents finer angular organization. The moderate association between \(m=2\) and \(m=4\) integrated magnitudes (\(\rho=0.490\)) indicates related but non-identical structure.

The justification for \(m=2\) is therefore not that it happens to maximize an empirical performance measure. It is the parsimonious lowest-order nontrivial harmonic implied by the symmetry of the measurement.

---

## 5.4 Representation structure and mathematical dependence

A central requirement of an interpretable representation is that algebraic identities are not presented as independent empirical evidence.

In particular,

\[
R_2(r)
=
|F_2(r)|
=
\sqrt{C_2(r)^2+S_2(r)^2}
\]

is a mathematical identity. These quantities describe different forms of the same second-harmonic vector and cannot be interpreted as independent confirmations of one another.

Likewise, if onset and termination radii are retained, their difference does not constitute an independent geometric coordinate. Raw axial angles also cannot be treated as ordinary Euclidean variables because

\[
\alpha \equiv \alpha+180^\circ.
\]

The representation therefore encodes axial directions through doubled-angle Cartesian coordinates,

\[
(\cos 2\alpha,\sin 2\alpha).
\]

The resulting 14-dimensional representation contains direct radial and axial summaries rather than reconstructed outputs or algebraically redundant transformations. This is more important scientifically than the reduction in dimensionality itself: it keeps the distinction between measured coordinates, deterministic transformations, model outputs, and statistical evidence explicit.

---

## 5.5 Garment identity and the generalization target

CLO-SKET contains repeated drawings of common source garments. The 2,300 sketches correspond to 230 recovered garment identities distributed across 23 garment categories, with 9–11 sketches per identity.

This structure changes the appropriate validation question. Randomly separating sketch files can place different drawings of the same source garment in both training and test sets. Such a split measures prediction for an unseen rendering of a previously represented garment identity. It does not measure transfer to a garment identity absent from training.

The primary evaluation therefore keeps every garment identity intact. Each of the five test folds contains 46 complete identities, including two identities from each garment category, and train/test identity overlap is zero.

Under this stricter evaluation, whole-field \(R_2\) RMSE was 0.145610 and Pearson correlation was 0.926390. At the observed peak shell, RMSE was 0.148303 and Pearson correlation was 0.810543. Median peak-shell axial error was \(4.104^\circ\).

These results establish internal transfer to withheld garment identities within CLO-SKET. They do not establish transfer to another dataset, another drawing population, another preprocessing system, or another cultural or institutional source of garment designs.

The same dependency structure also motivates garment-level inference. Repeated sketches of a common garment are not treated as 2,300 independent inferential units. Uncertainty estimation resamples complete garment identities, and confirmatory associations are evaluated after reducing repeated sketches to garment-level summaries.

---

## 5.6 What magnitude-only reconstruction actually shows

The reconstruction experiment deliberately removes explicit phase information. The predictors are only

\[
[r,R_2(r)],
\]

while the targets are

\[
C_2(r),S_2(r).
\]

Because

\[
R_2(r)
=
\sqrt{C_2(r)^2+S_2(r)^2},
\]

magnitude determines the length of the harmonic vector but not its direction. In general, infinitely many component pairs can share the same magnitude.

Consequently, successful reconstruction of \(C_2\) and \(S_2\) cannot be interpreted as phase being mathematically encoded in \(R_2\). It instead implies that the dataset contains statistical regularities relating radius and magnitude to orientation in its observed coordinate system.

The rotation experiments make this distinction explicit.

Under common global rotations of \(0^\circ\), \(22.5^\circ\), \(45^\circ\), \(67.5^\circ\), and \(90^\circ\), coordinate-free reconstruction metrics were essentially unchanged. Vector RMSE varied by only 0.000103, \(R_2\) RMSE by 0.000307, and median axial error by \(0.056^\circ\). At \(45^\circ\), the \(C_2\) and \(S_2\) component errors exchanged exactly, demonstrating that their apparent asymmetry is coordinate dependent.

The stronger test independently rotated each garment identity while keeping the rotation constant across its repeated sketches. This preserved radius, \(R_2\), garment identity, and the validation folds while removing common absolute orientation across identities.

Under this manipulation, median peak-shell axial error increased from

\[
4.104^\circ
\]

to

\[
44.675^\circ,
\]

close to the \(45^\circ\) chance expectation for an axial angle. The proportion with error \(\leq15^\circ\) was 0.166, essentially the chance value \(1/6\), and the proportion exceeding \(45^\circ\) was 0.497, essentially the chance value 0.5.

Magnitude reconstruction also deteriorated: whole-field \(R_2\) RMSE increased from 0.146 to 0.362, and peak-shell \(R_2\) RMSE from 0.148 to 0.590.

These results materially constrain the interpretation of the original reconstruction experiment. Radius and \(R_2\) do not intrinsically determine second-harmonic phase. The strong phase reconstruction in the upright dataset depends substantially on shared population-level orientation structure relative to the canonical image frame.

This does not invalidate the radial–angular representation. It identifies what information the reconstruction experiment is exploiting and prevents a coordinate-dependent statistical regularity from being mistaken for an intrinsic geometric identity.

---

## 5.7 Parameter sensitivity and the distinction between global and localized descriptors

An explicit representation is only as interpretable as its dependence on numerical design choices.

The sensitivity analyses show a clear distinction between broad radial summaries and localized descriptors.

Changing the support threshold from 0.10 to 0.05 or 0.15 left six of the eight radial descriptors exactly unchanged. As expected, changes were confined primarily to onset and termination, which are defined directly through the threshold.

Changing the concentration half-width from \(\pm4\) radial units to \(\pm2\) or \(\pm6\) changed the concentration statistic by construction but left the other seven radial descriptors unchanged.

Second-harmonic magnitude was highly stable to angular coarsening. Relative to 72 angular bins, the rank correlation of \(R_2\) remained 0.999 with 36 bins and 0.997 with 24 bins. Peak-radius rank correlations were 0.973 and 0.953 respectively.

Radial discretization had a larger effect on localized statistics. When 24-, 36-, and 72-bin radial fields were compared over exactly the same normalized physical interval, integrated magnitude retained rank correlations of 0.942 and 0.978 relative to 72 bins, radial centroid 0.931 and 0.967, and radial spread 0.893 and 0.949. Peak-radius correlations were lower, at 0.691 and 0.791.

The radial domain produced the strongest caution for peak-based interpretation. Within the primary 3.5–27.5 interval, 22.0% of peaks occurred at an endpoint. Of the sketches peaking at the upper boundary of 27.5, 40.9% moved beyond that boundary when the domain was expanded to 30.5. Across the widest tested expansion, peak-radius rank correlation with the primary configuration fell to 0.511.

The primary domain should therefore not be described as uniquely optimal or as revealing an intrinsic radial scale. Rather, it defines a reproducible analysis window within which broad radial summaries are comparatively stable and localized descriptors are conditional on domain and discretization.

This distinction also changes the interpretation of peak radius in subsequent association analyses. A peak-radius association can be a useful dataset-level observation, but it should not be elevated to a general physical law without external validation and a less boundary-sensitive localization procedure.

---

## 5.8 Why phase error depends on harmonic magnitude

The empirical relationship between harmonic magnitude and angular reconstruction error has a direct mathematical basis.

For

\[
\mu_2
=
\frac12\operatorname{atan2}(S_2,C_2),
\]

a small perturbation in the Cartesian components gives

\[
d\mu_2
=
\frac{
C_2\,dS_2-S_2\,dC_2
}{
2R_2^2
}.
\]

By the Cauchy inequality,

\[
|d\mu_2|
\leq
\frac{
\sqrt{dC_2^2+dS_2^2}
}{
2R_2
}.
\]

The same Cartesian perturbation therefore produces a larger possible angular perturbation when \(R_2\) is small.

The empirical results follow this geometry. At the garment-identity level, median observed peak \(R_2\) was negatively associated with median axial error,

\[
\rho=-0.356.
\]

However, Cartesian component-error magnitude was more strongly associated with axial error,

\[
\rho=+0.760,
\]

and the combined conditioning quantity

\[
\frac{
\|\Delta(C_2,S_2)\|
}{
2R_2
}
\]

showed the strongest association,

\[
\rho=+0.789.
\]

The first-order phase-error approximation was also strongly associated with observed angular error,

\[
\rho=+0.712.
\]

Magnitude stratification showed the same ordering. Median axial error decreased monotonically from \(5.988^\circ\) in the weakest observed-\(R_2\) quartile to \(2.918^\circ\) in the strongest, a ratio of approximately 2.05. The median conditioning bound simultaneously decreased from \(10.160^\circ\) to \(5.268^\circ\).

These results clarify the meaning of the \(R_2\)-error association. Larger \(R_2\) provides better geometric conditioning for phase estimation, but \(R_2\) does not determine error by itself. The Cartesian prediction perturbation is at least as important. Nor does the association imply that manipulating \(R_2\) would causally improve reconstruction.

The first-order approximation is also not exact for large perturbations. Its role is explanatory: it connects the observed pattern to the local geometry of harmonic phase estimation.

---

## 5.9 Statistical interpretation

The analysis separates mathematical identities, descriptive empirical patterns, and inferential claims.

Relations such as

\[
R_2=|F_2|
\]

are algebraic and require numerical verification rather than hypothesis testing.

Whole-field shell-level correlations, quartile profiles, rotation diagnostics, sensitivity comparisons, and low/high-error bands describe the realized dataset. They are scientifically useful, but repeated shells and repeated sketches prevent them from being interpreted as collections of independent observations.

Confirmatory association analysis therefore operates at the garment-identity level. Complete garment identities are used as the bootstrap unit, and category-stratified permutation preserves garment-category composition. Multiplicity correction is applied to the two primary association hypotheses.

Within this framework, observed peak-shell \(R_2\) showed a modest negative garment-level association with axial error,

\[
\rho=-0.355875,
\]

with bootstrap 95% CI

\[
[-0.455749,-0.248336]
\]

and Holm-adjusted permutation

\[
p=0.000200.
\]

Peak radius showed a weaker association,

\[
\rho=-0.207675,
\]

with bootstrap 95% CI

\[
[-0.322472,-0.095626]
\]

and Holm-adjusted

\[
p=0.030097.
\]

The first association is additionally supported by the phase-conditioning geometry. The second must be interpreted more cautiously because peak radius is materially sensitive to radial boundaries and resolution.

Inference remains conditional on treating the 230 recovered garment identities as mutually independent sampling units. The dataset structure supports that grouping more strongly than sketch-level independence, but it cannot establish broader lineage independence among garments, designers, templates, or collections.

---

## 5.10 Scientific contribution

None of the individual mathematical operations used here is new. Polar coordinates, Fourier moments, axial statistics, tree-based regression, bootstrap resampling, and permutation inference are established methods.

The contribution lies in combining them into an explicit measurement framework in which the assumptions and failure modes remain observable.

The framework provides:

1. a centroid-relative conditional angular field separating radial position from angular organization;
2. an axial second-harmonic representation whose order follows from \(180^\circ\) symmetry;
3. a compact 14-dimensional feature vector that excludes algebraically redundant and model-derived quantities;
4. garment-identity-disjoint reconstruction for evaluating transfer to unseen source garments;
5. analytic and identity-randomized rotation controls that expose dependence on the common coordinate frame;
6. parameter-sensitivity analyses that distinguish robust global summaries from boundary- and resolution-sensitive localized descriptors;
7. a perturbation-theoretic explanation of the relationship between harmonic magnitude and phase error; and
8. garment-level uncertainty and permutation inference that respect the repeated-sketch structure.

The resulting contribution is therefore methodological rather than semantic. CLO-SKET demonstrates how a sparse garment drawing can be converted into a compact radial–angular measurement while keeping mathematical dependence, coordinate-frame effects, numerical choices, validation units, and inferential scope explicit.

---

## 5.11 Limitations

Several limitations remain.

First, the study uses a single dataset. Identity-disjoint cross-validation demonstrates internal transfer to unseen recovered garment identities within CLO-SKET, not external generalization to other datasets, designers, institutions, drawing instruments, preprocessing systems, or cultural design traditions.

Second, garment identities were reconstructed from filename and category structure rather than supplied through an independently curated lineage table. This provides a defensible clustering variable for the present analysis but cannot exclude higher-level dependence among garments arising from common templates, designers, collections, or other unrecorded sources.

Third, all harmonic quantities arise from the same foreground images and conditional angular field. Reconstruction therefore remains a shared-source information-reduction experiment, not prediction of an independently measured target.

Fourth, the common upright image frame contains substantial population-level orientation information. The identity-randomized rotation experiment demonstrates that phase recovery depends strongly on this alignment. Performance should therefore not be assumed to transfer unchanged to arbitrarily rotated or differently standardized sketch collections.

Fifth, localized radial descriptors depend on the analysis window and radial discretization. Peak radius, onset, termination, and concentration require greater caution than integrated magnitude, centroid, and spread. In particular, the frequency of endpoint peaks indicates meaningful radial-domain censoring.

Sixth, \(m=2\) captures the lowest-order axial component, not the complete angular distribution. Odd harmonics and higher even harmonics contain additional information, and substantial signal was observed at \(m=1,3,4\). The 14-dimensional representation is consequently a targeted summary, not a sufficient representation of every aspect of sketch geometry.

Seventh, the phase-conditioning analysis uses a first-order perturbation approximation. It explains local sensitivity but becomes less accurate for large component perturbations.

Eighth, garment-level medians protect against pseudoreplication and give each identity equal inferential weight, but they discard within-identity variation. A hierarchical axial model could represent both sketch-level and garment-level variability directly.

Finally, no garment-part annotations, semantic labels beyond garment category, physical measurements, causal interventions, or prospective reliability outcomes are available. The results therefore do not establish semantic understanding, causal design principles, calibrated failure prediction, or physical garment laws.

---

## 5.12 Future work

The highest-priority extension is external validation on independently curated garment-sketch collections with explicit garment, designer, and collection identifiers. The representation and evaluation protocol should be specified before examining transfer performance so that external validation tests generalization rather than enabling another round of parameter selection.

A second priority is hierarchical modelling of axial quantities. Models based on doubled-angle representations or explicit axial likelihoods could retain sketch-level variation while accounting for garment identity and category, and could propagate uncertainty as \(R_2\) approaches zero.

The rotation results also motivate evaluation under naturally heterogeneous sketch orientations. Rather than relying on a common canonical frame, future work could compare orientation-normalized, rotation-equivariant, and explicitly frame-dependent representations to determine which information is intrinsic to garment geometry and which is introduced by acquisition convention.

Radial localization could be improved through continuous or multiscale peak estimation and through radial domains defined relative to normalized garment extent rather than a fixed shell interval. Such work is particularly important before interpreting peak radius as a transferable geometric characteristic.

The low-order harmonic analysis suggests another extension: a multiharmonic representation in which \(m=2\) remains the primary axial component but odd and higher even harmonics encode complementary directional and fine-scale organization. Such an extension should be evaluated for added information rather than simply increased dimensionality.

Finally, semantic validation would require independent annotations. Expert-defined attributes such as silhouette structure, symmetry, flare, sleeve organization, or other design properties could be tested against the geometric coordinates prospectively. Such work would constitute a new study; semantic meaning should not be assigned retrospectively to the present harmonic descriptors.

---

## 5.13 Conclusion

CLO-SKET demonstrates that garment sketches can be represented as explicit radial–angular measurements using shell-conditioned second-harmonic geometry.

The second harmonic is justified by the axial symmetry of the represented orientation: \(m=2\) is the lowest non-zero Fourier order invariant under \(180^\circ\) reversal. The resulting 14-dimensional representation separates radial harmonic magnitude from axial orientation while avoiding algebraically redundant coordinates.

Under five-fold garment-identity-disjoint validation, reconstructed second-harmonic magnitude remained strongly aligned with observation: whole-field \(R_2\) RMSE was 0.145610 with Pearson \(r=0.926390\), peak-shell RMSE was 0.148303 with Pearson \(r=0.810543\), and median peak-shell axial error was \(4.104^\circ\).

Rotation controls provide an essential qualification. Common global rotations left coordinate-free reconstruction performance essentially unchanged, whereas independently rotating garment identities increased median axial error to \(44.675^\circ\), approximately the axial chance level. Radius and harmonic magnitude therefore do not intrinsically determine phase; successful phase reconstruction in the original data depends substantially on shared orientation structure in the common image coordinate frame.

Sensitivity analyses further show that broad radial summaries are more robust than localized descriptors. Integrated magnitude, radial centroid, and radial spread remain comparatively stable under coarser discretization and domain perturbation, whereas peak radius, onset, termination, and concentration depend more strongly on radial resolution and boundaries.

Finally, the association between harmonic magnitude and axial error is consistent with phase-conditioning geometry. At the garment-identity level, peak \(R_2\) was negatively associated with axial error (\(\rho=-0.356\)), while Cartesian perturbation (\(\rho=+0.760\)) and the combined conditioning quantity (\(\rho=+0.789\)) tracked angular error more strongly. The weakest-harmonic identities exhibited approximately twice the median axial error of the strongest.

The evidence therefore supports a deliberately bounded conclusion. CLO-SKET provides a reproducible geometric measurement framework for radial and axial organization in repeated garment sketches. It does not establish semantic garment understanding, a uniquely optimal representation, an intrinsic physical peak radius, causal geometric effects, complete angular-density reconstruction, or orientation-independent phase predictability.

Its principal value is that the geometry, coordinate assumptions, numerical sensitivity, repeated-measure structure, and limits of inference remain explicit rather than hidden inside the representation.
