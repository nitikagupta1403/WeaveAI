# 5. Discussion

## 5.1 Principal finding: incremental value without evidence of garment-specific alignment

The central result of this study is that a compact, explicitly defined axial–radial representation contributes reproducible garment-category information beyond the frozen morphology representation under garment-identity-disjoint validation. Morphology alone achieved macro-F1 \(0.297788\), whereas morphology augmented by the complete 14-dimensional axial–radial block achieved \(0.335765\), giving the prospectively locked increment

\[
\Delta F_1=+0.037977.
\]

The corresponding balanced-accuracy increment was \(+0.037826\). Category-stratified garment-identity bootstrap intervals excluded zero for both metrics, and the effect remained positive in all 10 repeated grouped partitions. These results establish that the compact representation contains predictive structure not fully exploited by the morphology baseline under the tested classification protocol.

The strongest control, however, materially narrows that interpretation. When complete axial–radial identity blocks were reassigned within garment category, preserving category and block-size structure while destroying exact garment-level correspondence for 97.39% of rows, the correctly aligned increment was not unusually large. The empirical alignment probabilities were \(p=0.762619\) for macro-F1 and \(p=0.729635\) for balanced accuracy. The null mean increment was in fact slightly larger than the observed aligned increment.

This is not evidence that misalignment improves prediction. Rather, the alignment permutation asks whether correct sketch/garment-level pairing yields an increment exceeding that obtainable from category-preserving axial–radial structure. It did not. The evidence therefore supports **incremental predictive utility**, but not the stronger proposition that this utility requires exact garment-specific morphology–axial–radial correspondence.

This distinction is central to the contribution. Without the alignment control, the improvement from \(M\) to \(M+R+A\) could easily be described as evidence of complementary garment-level geometry. The experiment shows that such wording would exceed the data. A more defensible interpretation is that the axial–radial representation captures category-conditioned geometric organization that remains useful alongside morphology, while the present experiment does not localize that gain to garment-specific correspondence.

---

## 5.2 What information is carried by the radial and axial blocks?

The ablation structure helps localize the observed predictive gain. The eight-dimensional radial block achieved substantially higher standalone category discrimination than the six-dimensional axial block: macro-F1 was \(0.206831\) for \(R\) and \(0.081165\) for \(A\). When added to morphology, the radial block increased macro-F1 by \(+0.026752\), whereas the axial block alone increased it by only \(+0.002299\). The complete block produced the largest observed increment, \(+0.037977\).

The direct empirical contribution is therefore concentrated primarily in radial organization. This is compatible with the construction of the representation. The radial coordinates summarize where and how strongly second-harmonic angular organization occurs relative to the sketch centroid—through integrated magnitude, centroid, spread, concentration, support limits, peak location, and peak strength. These quantities can vary systematically across garment categories even when exact correspondence to a particular morphology vector is unnecessary.

The axial block should be interpreted differently. Its low standalone performance does not imply that axial geometry is meaningless. Peak and magnitude-weighted orientations are coordinate-frame-dependent equivariant quantities, and the rotation analyses show that the canonical upright frame contains strong population-level orientation structure. Moreover, \(M+R+A\) descriptively exceeded \(M+R\). However, Experiment 06 did not prospectively specify a separate conditional significance test of \(A\) given \(M+R\). We therefore do not claim an independently established axial increment beyond the radial block.

The ablation evidence supports a mechanistic description, not a hierarchy of universal feature importance: within this dataset, classifier, coordinate frame, and locked representation, radial second-harmonic organization accounts for most of the directly observed incremental category signal.

---

## 5.3 Why the alignment result matters scientifically

The alignment permutation distinguishes two forms of “complementarity” that are otherwise easy to conflate.

The first is **incremental predictive utility**: adding one representation to another improves out-of-fold prediction. Experiment 06 supports this statement. The second is **instance-specific complementarity**: the additional benefit depends on the axial–radial representation belonging to the same garment instance or identity as the morphology representation. The alignment experiment does not support this stronger statement.

This distinction can be expressed schematically. Let \(M_i\) denote morphology for sketch \(i\), \(Z_i\) its correctly aligned axial–radial representation, and \(Z_{\pi(i)}\) a category-preserving identity-level reassignment. The observed comparison establishes

\[
\operatorname{Perf}(M_i,Z_i)
>
\operatorname{Perf}(M_i)
\]

under the locked evaluation. But the alignment control asks whether

\[
\operatorname{Perf}(M_i,Z_i)
>
\operatorname{Perf}(M_i,Z_{\pi(i)})
\]

more strongly than expected under the restricted permutation distribution. The data provide no such evidence.

This negative control is informative rather than disappointing. It identifies the scale at which the present evidence resides. The gain appears compatible with axial–radial distributions shared within garment categories rather than requiring exact garment-level coupling. In other words, the representation contributes useful structured information, but the experiment does not demonstrate that it encodes a unique geometric residual for each garment after morphology is known.

Several mechanisms could generate this pattern. Category-conditioned radial organization may be sufficiently stable that a misaligned representation from another garment in the same category still supplies useful category information. The morphology classifier may also leave category-level decision structure that the axial–radial block can reinforce without needing exact instance correspondence. These are plausible explanations, not separately tested mechanisms, and should not be elevated to causal conclusions.

The important methodological point is broader: an increase after feature concatenation is not, by itself, evidence that two representations contain uniquely paired information. Restricted alignment tests provide a practical way to separate predictive gain from instance-specific correspondence when repeated or grouped data permit such a control.

---

## 5.4 The second harmonic as an explicit axial measurement

The predictive experiment sits within a representation whose geometric meaning is defined independently of category performance. For each radial shell,

\[
F_2(r)
=
\sum_k p(\theta_k\mid r)e^{-i2\theta_k}
=
C_2(r)-iS_2(r)
=
R_2(r)e^{-i2\alpha_2(r)}.
\]

The magnitude

\[
R_2(r)=\sqrt{C_2(r)^2+S_2(r)^2}
\]

quantifies the strength of second-order angular organization, while

\[
\alpha_2(r)
=
\frac12\operatorname{atan2}(S_2(r),C_2(r))
\pmod{\pi}
\]

gives its undirected axial orientation.

The choice \(m=2\) follows from the symmetry being represented rather than from downstream classification performance. Because an axial orientation satisfies

\[
\theta\equiv\theta+\pi,
\]

a harmonic transforms under reversal as

\[
F_m(\theta+\pi)=(-1)^mF_m(\theta).
\]

The second harmonic is therefore the lowest non-zero Fourier order compatible with \(180^\circ\) axial equivalence. The empirical low-order spectrum is consistent with this choice: among \(m=1,2,3,4\), \(m=2\) had the largest median integrated and peak magnitude. That comparison is supportive, not a post-hoc selection rule.

The representation is geometric rather than semantic. A high \(R_2\) does not identify a sleeve, waistline, collar, flare, or other named garment component. Likewise, \(\alpha_2\) describes a harmonic axis, not a functional garment direction. Category discrimination demonstrates that these measurements carry information relevant to the tested labels; it does not convert the coordinates into semantic annotations.

---

## 5.5 Algebraic dependence and representation discipline

A central design principle was to keep deterministic relationships separate from empirical evidence. In particular,

\[
R_2=|F_2|=\sqrt{C_2^2+S_2^2}
\]

is an identity, not an independent confirmation among three measurements. Likewise, radial extent is exactly termination radius minus onset radius and was therefore removed from the compact radial block.

Axial directions cannot be treated as ordinary scalar angles because \(\alpha\equiv\alpha+180^\circ\). Peak and magnitude-weighted orientations were consequently represented by

\[
(\cos2\alpha,\sin2\alpha),
\]

which respects axial periodicity and permits ordinary Euclidean learning algorithms to operate on the encoded coordinates without introducing a discontinuity at the angular wrap point.

These choices matter for interpretation of Experiment 06. The observed gain is not obtained by simply appending obvious algebraic duplicates of the morphology baseline. The 14 coordinates are explicit summaries of a separately constructed radial–angular field. At the same time, “separately constructed” does not mean statistically independent: both representations ultimately derive from the same sketch images. The study therefore claims incremental predictive utility under a specified model, not information-theoretic independence.

---

## 5.6 Transformation behavior and the role of the canonical image frame

The representation contains both invariant and equivariant quantities under rigid in-plane rotation. For a physical rotation by \(\phi\),

\[
F_2'(r)=e^{-i2\phi}F_2(r),
\qquad
R_2'(r)=R_2(r),
\]

while axial orientation transforms as

\[
\alpha_2'=\alpha_2+\phi\pmod{\pi}.
\]

Accordingly, the doubled-angle pair transforms by the ordinary two-dimensional rotation \(R(2\phi)\), whereas magnitude-derived radial summaries and relative scalar quantities such as coherence are intended to remain invariant.

The rigid-image rotation control largely reproduced this structure over \(\pm5^\circ,\pm10^\circ,\pm20^\circ\). Radial-magnitude profiles showed small median perturbations attributable to raster interpolation and finite binning, and the doubled-angle orientations closely followed the imposed rotations. Magnitude-weighted mean orientation was especially stable, with 95th-percentile transformation error below \(0.85^\circ\) across the tested range. Coherence was numerically stable; orientation drift had small median changes but a wider upper tail.

A different rotation experiment exposed an important limitation of reconstruction from radius and magnitude. Common analytic rotations left coordinate-free reconstruction metrics essentially unchanged, whereas assigning independent rotations to garment identities increased median peak-shell axial error from \(4.104^\circ\) to \(44.675^\circ\), close to the \(45^\circ\) chance expectation for an axial angle.

Thus, radius and \(R_2\) do not intrinsically determine harmonic phase. Strong phase reconstruction in the canonical CLO-SKET images depends substantially on population-level orientation structure relative to the common image frame. This conclusion is conceptually consistent with the Experiment 06 alignment result: both controls caution against interpreting dataset-level regularities as uniquely paired garment-level geometry.

---

## 5.7 Garment identity defines the internal generalization target

CLO-SKET contains repeated drawings of common source garments. Treating all 2,300 sketches as independent would therefore overstate the effective independence of the dataset and could allow different renderings of the same garment to occur in both training and test sets.

The primary evaluation instead grouped the sketches into 230 recovered garment identities, with 10 identities in each of the 23 categories. Every primary test fold withheld two complete identities per category, and no garment identity occurred in both training and test data.

This design changes the interpretation of performance. The reported results concern transfer to previously unseen recovered garment identities **within CLO-SKET**. They do not establish generalization to another sketch dataset, another drawing population, another preprocessing pipeline, or another institutional or cultural source of garment designs.

The same grouping principle governs uncertainty estimation and the alignment control. Bootstrap resampling operates on complete garment identities, and misalignment is performed at the identity-block level rather than by independently shuffling sketch rows. This preserves the repeated-sketch dependency structure instead of manufacturing an artificially large number of independent units.

The identity labels themselves were reconstructed from filename and category structure, including one explicitly audited exceptional filename. They provide the strongest available grouping variable in CLO-SKET but cannot rule out higher-level dependence among source garments, designers, templates, or collections.

---

## 5.8 Reconstruction is a consistency experiment, not independent target prediction

The earlier reconstruction analysis remains useful, but its role is secondary to the incremental-representation experiment. It asks whether the Cartesian harmonic components \(C_2\) and \(S_2\) can be statistically reconstructed from radius and observed magnitude \(R_2\) under identity-disjoint validation.

Because

\[
R_2=\sqrt{C_2^2+S_2^2},
\]

the predictors and targets arise from the same harmonic field. Reconstruction therefore does not constitute prediction of an independently measured physical quantity. It is a controlled information-reduction experiment that probes regularities in the observed radial–angular field.

Under identity-disjoint validation, whole-field reconstructed \(R_2\) had RMSE \(0.145610\) and Pearson \(r=0.926390\); at the observed peak shell, RMSE was \(0.148303\), Pearson \(r=0.810543\), and median axial error \(4.104^\circ\). These values demonstrate reproducible internal structure but should not be interpreted as proof that magnitude mathematically determines phase.

The identity-randomized rotation control is decisive on this point. Once common absolute orientation was removed across identities, axial reconstruction approached chance. The original reconstruction performance therefore reflects statistical regularity in the canonical dataset rather than an intrinsic inversion of magnitude into phase.

This distinction also explains why reconstruction and Experiment 06 answer different questions. Reconstruction evaluates internal correspondence among quantities derived from the radial–angular field. Experiment 06 asks whether the compact representation improves an external downstream category-discrimination task relative to morphology. The latter provides the stronger evidence that the representation carries practically distinct predictive structure, although the alignment permutation limits the scale at which that distinctness can be localized.

---

## 5.9 Robustness is stronger for broad radial summaries than localized coordinates

The sensitivity analyses reveal a consistent hierarchy of numerical robustness. Integrated magnitude, radial centroid, and radial spread were comparatively stable across changes in radial domain and discretization. Localized descriptors—particularly peak radius, onset, termination, and concentration—were more dependent on analysis boundaries and resolution.

The primary radial domain contained endpoint peaks for approximately 22% of sketches. Among sketches whose primary peak occurred at the upper boundary \(r=27.5\), 40.9% moved to a larger radius when the domain was expanded to \(30.5\). Peak radius should therefore be interpreted as a domain-conditioned localization statistic rather than an intrinsic physical scale.

This qualification is particularly important because the radial block accounts for most of the direct incremental category signal in Experiment 06. The classifier result establishes usefulness of the **locked block as a whole**; it does not imply that every radial coordinate is equally stable or equally transferable. A feature may contribute predictive information in the fixed CLO-SKET measurement system while remaining sensitive to the chosen measurement window.

Accordingly, the 14-dimensional representation is best regarded as a reproducible measurement specification rather than an empirically optimized or universally invariant coordinate system.

---

## 5.10 Harmonic magnitude conditions axial uncertainty

The observed relationship between harmonic magnitude and axial reconstruction error has a direct perturbation-theoretic explanation. For

\[
\alpha_2
=
\frac12\operatorname{atan2}(S_2,C_2),
\]

a first-order perturbation gives

\[
d\alpha_2
=
\frac{C_2\,dS_2-S_2\,dC_2}{2R_2^2},
\]

and therefore

\[
|d\alpha_2|
\le
\frac{\sqrt{dC_2^2+dS_2^2}}{2R_2}.
\]

For a fixed Cartesian perturbation, phase becomes less well conditioned as harmonic magnitude decreases.

The garment-level results follow this geometry. Median observed peak \(R_2\) was negatively associated with median axial error (\(\rho=-0.356\)), but Cartesian reconstruction-error magnitude showed a stronger association (\(\rho=+0.760\)). Their combined conditioning quantity,

\[
\frac{\|\Delta(C_2,S_2)\|}{2R_2},
\]

was more strongly associated still (\(\rho=+0.789\)). Median axial error decreased from \(5.988^\circ\) in the weakest-\(R_2\) quartile to \(2.918^\circ\) in the strongest.

This provides an explanatory geometric account of the magnitude–error association without turning it into a causal statement. Increasing \(R_2\) is not shown to cause improved reconstruction; both harmonic strength and Cartesian prediction error contribute to angular uncertainty.

---

## 5.11 Inferential scope

The analysis deliberately separates mathematical identities, descriptive patterns, uncertainty estimates, and permutation-based hypothesis tests.

The primary Experiment 06 effect is supported by paired garment-identity bootstrap uncertainty and by reproducibility across repeated grouped partitions. The alignment permutation addresses a different hypothesis and fails to reject its restricted null. These results are not contradictory: the first establishes a reproducible predictive increment, whereas the second shows that the increment is not demonstrably dependent on exact garment-level alignment.

Similarly, the garment-level association between observed peak-shell \(R_2\) and axial reconstruction error is supported under category-stratified permutation, but this does not establish a causal effect of harmonic magnitude. Peak-radius associations are additionally sensitivity-qualified because peak localization depends materially on radial domain and resolution.

The effective inferential population is the 230 recovered garment identities, conditional on treating them as independent sampling units. CLO-SKET does not provide sufficient lineage metadata to establish independence among designers, templates, collections, or other higher-level sources. All population-level claims therefore remain internal to this dependency assumption.

No result in the study establishes information-theoretic independence between morphology and the axial–radial representation, semantic understanding of garment parts, causal geometric mechanisms, or universal performance beyond the evaluated dataset.

---

## 5.12 Scientific contribution

The individual mathematical tools used here—polar coordinates, Fourier moments, axial statistics, regularized classification, bootstrap resampling, and permutation testing—are established. The contribution lies in assembling them into an auditable representation-and-validation framework for sparse garment sketches and then testing progressively stronger interpretations of that representation.

The framework contributes four linked elements.

First, it provides an explicit 14-dimensional measurement of radial second-harmonic organization and axial orientation whose coordinates have defined geometric meanings and transformation rules.

Second, it evaluates that representation under garment-identity-disjoint validation rather than image-level random splitting, respecting the repeated-sketch structure of CLO-SKET.

Third, it demonstrates reproducible incremental category-discrimination value beyond a frozen 135-dimensional morphology representation: approximately \(+0.038\) macro-F1 in the primary partition, a positive category-stratified identity-bootstrap interval, and positive effects across all 10 repeated grouped partitions.

Fourth, it subjects the attractive interpretation of that gain to a stronger falsification control. Category-preserving identity-level misalignment does not reduce the increment sufficiently for correct alignment to appear exceptional. The contribution is therefore not a claim of uniquely paired garment-level complementarity. It is the narrower—and better supported—demonstration that a compact, geometrically interpretable axial–radial measurement contributes reproducible category-conditioned predictive structure beyond the tested morphology baseline.

This claim boundary is itself part of the methodological contribution. The study illustrates how representation research can move from “the added features improve prediction” to the more demanding question “what correspondence is actually required for that improvement?” without conflating the two.

---

## 5.13 Limitations

Several limitations constrain interpretation.

First, all experiments use a single dataset. Identity-disjoint validation tests internal transfer to unseen recovered garment identities within CLO-SKET, not external generalization.

Second, garment identities were reconstructed from filename and category structure rather than provided through an independently curated lineage table. Higher-level dependence among garments cannot be excluded.

Third, both morphology and axial–radial coordinates derive from the same source sketches. Incremental predictive utility therefore does not imply statistical or information-theoretic independence.

Fourth, the alignment control preserves garment category by design. It establishes that exact within-category garment pairing is not required for the observed gain, but it does not determine which category-conditioned distributional properties generate that gain. Resolving that mechanism requires additional experiments or external data.

Fifth, the canonical upright coordinate frame contains substantial population-level orientation structure. Phase reconstruction deteriorates to approximately chance after garment-identity-specific rotation, so orientation-dependent findings should not be assumed to transfer unchanged to arbitrarily oriented sketch collections.

Sixth, localized radial descriptors depend on analysis domain and discretization. Peak radius, onset, termination, and concentration require greater caution than integrated magnitude, centroid, and spread.

Seventh, \(m=2\) is a targeted lowest-order axial summary, not a complete representation of the angular distribution. Odd and higher even harmonics contain additional structure.

Eighth, the phase-conditioning analysis uses a first-order approximation and is most interpretable for local perturbations.

Finally, no garment-part annotations, independent physical measurements, causal interventions, or external prospective outcomes are available. The study therefore does not establish semantic garment understanding, causal design principles, calibrated reliability classes, or physical garment laws.

---

## 5.14 Future work

The most important next step is external validation on independently curated garment-sketch collections with explicit garment, designer, and collection identifiers. The 14-dimensional representation, morphology baseline, estimator, and evaluation protocol should be fixed before examining those data.

A second priority is to determine the source of the category-conditioned incremental signal revealed by Experiment 06. Because within-category misalignment preserved the gain, future analyses should test whether radial–axial category prototypes, distributional summaries, or other category-level geometric statistics reproduce the same benefit. Such analyses should be treated as new hypotheses rather than retroactive explanations of the current result.

A third direction is evaluation of explicitly orientation-normalized or rotation-equivariant variants. This would help separate information intrinsic to garment geometry from information introduced by the canonical acquisition frame.

Radial localization could also be improved through continuous or multiscale estimators and through domains normalized to garment extent. This is particularly important before treating peak radius as a transferable geometric characteristic.

Finally, semantic validation requires independent annotations. Expert-defined attributes such as silhouette, flare, symmetry, sleeve organization, or other design properties could be tested prospectively against the geometric coordinates. Such work would determine whether the present representation is merely category-informative or also corresponds to interpretable design concepts.


---
