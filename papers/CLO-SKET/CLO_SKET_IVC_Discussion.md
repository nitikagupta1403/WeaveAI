# 5. Discussion

## 5.1 A compact geometric representation adds information beyond morphology

The main result is that RA14 contributes reproducible category-discriminative information beyond the frozen morphology baseline under garment-identity-disjoint validation. Morphology alone achieved macro-F1 \(0.297788\), whereas morphology+RA14 achieved \(0.335765\), giving

\[
\Delta F_1=+0.037977,
\]

with balanced-accuracy increment \(+0.037826\). Category-stratified garment-identity bootstrap intervals excluded zero, and the macro-F1 increment remained positive across all 10 repeated grouped partitions.

This identifies a specific role for RA14: a compact, explicit geometric summary that contributes useful information beyond morphology under dependency-aware evaluation. It does not imply that the representation is statistically independent of morphology, because both are derived from the same images.

## 5.2 Most of the directly observed increment lies in radial organization

The ablations localize most directly observed utility to the radial block. Standalone macro-F1 was \(0.206831\) for the eight-dimensional radial block and \(0.081165\) for the six-dimensional axial block. Added to morphology, their respective macro-F1 increments were \(+0.026752\) and \(+0.002299\), while complete RA14 produced \(+0.037977\).

The radial coordinates summarize where second-harmonic organization occurs relative to the sketch centroid through integrated magnitude, radial centroid, spread, concentration, support limits, peak location, and peak strength. These quantities can differ systematically by garment category without requiring exact garment-level correspondence.

The axial block alone added little to morphology. Although the complete representation descriptively exceeded \(M+R\), Experiment 06 did not prespecify a separate conditional test of the axial contribution given \(M+R\). The supported interpretation is therefore a radial-dominant increment rather than an independently established axial effect.

## 5.3 The HOG comparator reveals representation-dependent complementarity

Experiment 07 provides a stricter conventional-image-descriptor comparison. HOG alone achieved macro-F1 \(0.648242\), and HOG+RA14 achieved \(0.649135\). The paired garment-identity bootstrap interval crossed zero.

RA14 should therefore not be interpreted as a general-purpose accuracy booster. Its additional value depends on what the baseline already represents. The morphology baseline leaves useful radial-angular structure unexploited, whereas HOG appears to encode much of the same category-relevant edge and orientation information in a much higher-dimensional form.

The combined Experiment-06 and Experiment-07 evidence supports **representation-dependent complementarity**: RA14 adds information beyond morphology, while no clear additional benefit is established beyond HOG under the tested protocol.

## 5.4 Predictive increment and garment-specific correspondence are different questions

The alignment experiment tested a stronger claim than predictive improvement. Experiment 06 established that correctly aligned morphology+RA14 outperformed morphology alone. The restricted permutation then asked whether correct garment-level pairing performed unusually well relative to category-preserving, block-size-matched RA14 reassignment.

It did not. Empirical alignment probabilities were \(p=0.762619\) for macro-F1 and \(p=0.729635\) for balanced accuracy.

Thus the predictive increment is reproducible, but the evidence does not localize it to exact garment-level morphology–RA14 correspondence. Category-conditioned radial-angular structure can remain informative even when RA14 comes from another garment in the same category.

This distinction is methodologically important: feature concatenation, incremental predictive utility, and instance-specific complementarity are not equivalent claims.

## 5.5 The second harmonic gives the representation a direct geometric meaning

For each radial shell,

\[
F_2(r)
=
\sum_k p(\theta_k\mid r)e^{-i2\theta_k}
=
R_2(r)e^{-i2\alpha_2(r)}.
\]

Its magnitude \(R_2(r)\) measures the strength of second-order angular organization, while \(\alpha_2(r)\) gives undirected axial orientation modulo \(\pi\).

The choice \(m=2\) follows from axial symmetry rather than classification performance: it is the lowest non-zero Fourier order compatible with \(180^\circ\) equivalence. The later low-order spectrum was consistent with that choice but did not determine it.

This geometric interpretation should not be overextended semantically. RA14 does not identify sleeves, collars, waistlines, flare, or other garment parts. Likewise, algebraic relationships are not independent confirmations: \(R_2=\sqrt{C_2^2+S_2^2}\) is definitional, and radial extent was excluded because it is exactly termination radius minus onset radius.

## 5.6 Transformation behaviour separates intrinsic structure from coordinate-frame structure

Using the measurement-coordinate increment \(\phi\), with \(\phi=-\beta\) for raw Pillow raster angle \(\beta\),

\[
F_2'(r)=e^{-i2\phi}F_2(r),
\qquad
R_2'(r)=R_2(r),
\qquad
\alpha_2'=\alpha_2+\phi\pmod{\pi}.
\]

The earlier rigid-image rotation control was broadly consistent with the expected axial transformation over the tested perturbations, while radial-magnitude profiles showed modest raster-level deviations.

Analytic controls further separated coordinate-free structure from common-frame orientation. Global rotations left reconstruction behaviour essentially unchanged, whereas independent garment-identity rotations increased median peak-shell axial reconstruction error from \(4.104^\circ\) to \(44.675^\circ\), close to the \(45^\circ\) expectation for unrelated axial orientations. Radius and \(R_2\) therefore do not intrinsically determine phase; much of the observed phase regularity depends on the upright population frame.

Experiment 08 narrows this claim further. Its prospectively frozen raster harmonic-magnitude P95 criterion failed even though analytic rotation and raster axial-angle subchecks passed. The earlier rotation results remain descriptive controls, not confirmatory mechanical validation.

## 5.7 Broad radial summaries are more stable than localized coordinates

Sensitivity analyses revealed a hierarchy within the radial descriptors. Integrated magnitude, radial centroid, and radial spread were comparatively stable under changes in radial domain and discretization, whereas peak radius, support boundaries, and concentration were more sensitive to analysis choices.

Approximately 22% of sketches selected a peak at a boundary of the primary radial domain, and 40.9% of sketches peaking at the upper boundary moved outward when the domain was expanded. Peak radius is therefore best interpreted relative to the locked measurement window rather than as an intrinsic physical scale.

RA14 should consequently be treated as a fixed measurement specification: predictive usefulness under that specification does not imply equal numerical portability of every coordinate.

## 5.8 Harmonic magnitude explains part of axial uncertainty

For

\[
\alpha_2
=
\frac12\operatorname{atan2}(S_2,C_2),
\]

first-order perturbation gives the bound

\[
|d\alpha_2|
\le
\frac{\sqrt{dC_2^2+dS_2^2}}{2R_2}.
\]

Smaller harmonic magnitude therefore makes axial phase less well conditioned for a fixed Cartesian perturbation.

The garment-level results follow this geometry. Median peak \(R_2\) was negatively associated with axial error (\(\rho=-0.356\)), while Cartesian reconstruction-error magnitude had a stronger association (\(\rho=+0.760\)). Their combined conditioning quantity was stronger still (\(\rho=+0.789\)). The interpretation is geometric rather than causal: harmonic strength conditions angular sensitivity, but the actual Cartesian perturbation also matters.

## 5.9 Scope, contribution, and next steps

The effective experimental population is the 230 recovered garment identities. Identity-disjoint validation therefore tests transfer to unseen recovered garments within CLO-SKET, not external generalization to another dataset or design population.

Several boundaries remain. Garment identities were reconstructed rather than supplied through an independent lineage table, so higher-level dependencies cannot be excluded. Morphology and RA14 derive from the same images. The common upright frame carries orientation structure. Localized radial descriptors are domain-sensitive. The second harmonic is a targeted axial summary rather than a complete angular representation. No garment-part annotations or independent physical measurements are available.

Within these limits, the contribution is both representational and methodological. Representationally, RA14 provides an explicit 14-dimensional description of radial second-harmonic organization and axial orientation. Methodologically, the evaluation distinguishes whether the representation carries category information, whether it adds predictive value beyond another representation, and whether that added value depends on exact garment-level correspondence.

Experiment 06 supports incremental value beyond morphology. Experiment 07 shows that this value is baseline-dependent. The alignment control does not support garment-specific correspondence. Experiment 08 narrows the mechanical transformation-validity claim without altering the frozen Experiment-06 result.

The next step is external validation: independent garment-sketch collections with explicit garment, designer, and collection identifiers; orientation-normalized or rotation-equivariant variants; and prospective semantic annotation would test how far the present geometric findings generalize.
