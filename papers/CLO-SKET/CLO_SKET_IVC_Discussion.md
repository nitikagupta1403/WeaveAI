# 5. Discussion

## 5.1 Corrective Experiment 06 supports incremental utility beyond morphology

The manuscript-facing Experiment-06 result is the corrected annotation-controlled CLEAN analysis. Morphology alone achieved macro-F1 \(0.271429\), whereas morphology+RA14 achieved \(0.314256\), giving

\[
\Delta F_1=+0.042827,
\]

with balanced-accuracy increment \(+0.042609\). Category-stratified corrected-garment-identity bootstrap intervals excluded zero, and the increment remained positive across all 10 corrected repeated grouped partitions.

This identifies a specific and bounded role for RA14: the complete frozen 14-dimensional representation contributes reproducible category-discriminative information beyond the frozen morphology representation under corrected garment-identity-disjoint evaluation. It does not imply statistical independence of the two representations, because both are derived from the same underlying images.

A post-outcome target-text audit identified two affected CLEAN images. Excluding their two complete garment identities reduced the macro-F1 increment from \(+0.042827\) to \(+0.036402\), while all 5,000 sensitivity bootstrap replicates and all 10 repeated grouped partitions remained positive. We therefore interpret the sensitivity as persistence with modest attenuation, not as evidence that the two target-text cases account for the existence of the corrected incremental effect. Because this analysis was specified after outcome exposure, it remains descriptive post-outcome evidence.

## 5.2 The corrected analysis does not localize the increment to radial or axial sub-blocks

The historical Experiment-06 package contained radial-only, axial-only, and combined ablations. Those analyses were generated under the historical raw-canvas and historical identity-map configuration and were not rerun under the corrected CLEAN confirmatory design.

Consequently, the corrected manuscript does not use the historical ablations to claim that the current \(+0.042827\) increment is predominantly radial or to establish an independent axial contribution. The supported confirmatory claim concerns the complete frozen RA14 block. Historical ablations may motivate future decomposition studies, but they do not define the inferential interpretation of the corrected result.

This distinction is important because repairing the identity map and annotation-controlled measurement field changes the confirmatory analysis population and preprocessing context. A component-level claim would require a separately locked corrected analysis rather than inheritance from superseded historical values.

## 5.3 The HOG comparator remains secondary and representation-dependent

Experiment 07 provides a secondary conventional-image-descriptor comparison. HOG alone achieved macro-F1 \(0.648242\), and HOG+RA14 achieved \(0.649135\); the paired garment-identity bootstrap interval crossed zero.

Experiment 07 was frozen under its own historical Experiment-06-derived fold provenance before the later corrective Experiment-06 identity-map repair. It is therefore retained as a secondary external baseline rather than treated as a same-fold rerun of the corrected CLEAN primary analysis.

The qualitative conclusion remains narrow: RA14 should not be interpreted as a universal accuracy booster. A clear increment is supported relative to the corrected morphology baseline, whereas no clear additional benefit was established beyond the tested high-dimensional HOG descriptor under Experiment 07's frozen protocol.

## 5.4 Predictive increment and garment-specific correspondence remain different questions

The corrected alignment experiment tested a stronger claim than predictive improvement. The CLEAN primary analysis established that correctly aligned morphology+RA14 outperformed morphology alone. The restricted permutation then asked whether correct garment-level pairing performed unusually well relative to category-preserving, block-size-matched RA14 reassignment.

It did not. Corrected empirical alignment probabilities were \(p=0.722639\) for macro-F1 and \(p=0.685657\) for balanced accuracy.

Thus the corrected predictive increment is reproducible, but the evidence does not localize it to exact garment-level morphology–RA14 correspondence. Category-conditioned RA14 structure remains compatible with the observed predictive gain even after exact correspondence is largely disrupted.

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
