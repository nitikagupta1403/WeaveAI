# 5. Discussion

## 5.1 A compact geometric representation adds information beyond morphology

The main result is simple: the axial–radial representation contributes reproducible category-discriminative information beyond the frozen morphology baseline under garment-identity-disjoint validation.

Morphology alone achieved macro-F1 \(0.297788\), whereas morphology augmented by the complete 14-dimensional axial–radial representation achieved \(0.335765\), giving the locked increment

\[
\Delta F_1=+0.037977.
\]

Balanced accuracy increased by \(+0.037826\). Category-stratified garment-identity bootstrap intervals excluded zero for both metrics, and the macro-F1 increment remained positive across all 10 repeated grouped partitions.

This result matters because the added representation is small and explicit. Its 14 coordinates describe where second-harmonic directional organization occurs radially, how strongly it is expressed, and how its undirected orientation is arranged. The gain therefore shows that this geometric description contains category-relevant structure not fully captured by the 135-dimensional morphology representation.

The result therefore identifies a specific role for RA14: an explicit geometric summary that contributes useful information beyond morphology under dependency-aware evaluation.

## 5.2 Most of the directly observed increment lies in radial organization

The ablations make the source of that gain more interpretable.

The eight-dimensional radial block achieved standalone macro-F1 \(0.206831\), compared with \(0.081165\) for the six-dimensional axial block. Added to morphology, the radial block increased macro-F1 by \(+0.026752\), while the axial block alone increased it by \(+0.002299\). The complete axial–radial representation produced the largest observed increment, \(+0.037977\).

This pattern is consistent with the geometry being summarized. The radial coordinates encode where second-harmonic angular organization is distributed relative to the sketch centroid through integrated magnitude, centroid, spread, concentration, support limits, peak location, and peak strength. Such quantities can vary systematically across garment categories even when exact garment-level correspondence is unnecessary.

The axial block has a different role. Peak and magnitude-weighted orientations are equivariant quantities defined relative to the common image frame, and the rotation experiments show substantial orientation structure in the upright CLO-SKET population. The complete representation also descriptively exceeded \(M+R\). However, Experiment 06 did not prespecify a separate conditional test of the axial block given \(M+R\), so the evidence supports a radial-dominant incremental effect rather than a separately established axial contribution.

## 5.3 The HOG comparator reveals representation-dependent complementarity

Experiment 07 provides an important second view of the same question.

HOG alone achieved macro-F1 \(0.648242\), and appending RA14 increased this only to \(0.649135\). The corresponding paired garment-identity bootstrap interval crossed zero. Thus the large gain observed relative to morphology was not reproduced when a high-dimensional local-gradient representation was already present.

This makes the contribution more specific, not weaker.

RA14 should not be understood as a general-purpose accuracy booster. Instead, its additional value depends on what information the baseline already represents. The morphology baseline leaves useful radial–angular structure unexploited, whereas HOG appears to encode much of the same category-relevant edge and orientation information in a far higher-dimensional form.

The distinction is important. HOG provides a dense local-gradient description; RA14 compresses a targeted second-harmonic radial–axial measurement into only 14 interpretable coordinates. Their predictive roles overlap, but their representational purposes are different.

The combined Experiment-06 and Experiment-07 evidence therefore supports **representation-dependent complementarity**: RA14 contributes information beyond morphology, while much of that information is already available to the HOG representation.

## 5.4 Predictive increment and garment-specific correspondence are different questions

The alignment experiment asks a stronger question than whether RA14 improves prediction.

Let \(M_i\) denote morphology for sketch \(i\), \(Z_i\) the correctly aligned axial–radial representation, and \(Z_{\pi(i)}\) a category-preserving identity-level reassignment.

Experiment 06 established

\[
\operatorname{Perf}(M_i,Z_i)
>
\operatorname{Perf}(M_i)
\]

under the locked evaluation.

The alignment control instead asked whether the correctly paired representation performs unusually well compared with

\[
\operatorname{Perf}(M_i,Z_{\pi(i)}),
\]

where garment identity correspondence is disrupted while garment category and block-size structure are preserved.

The correctly aligned effect was not exceptional under that restricted null.

The empirical alignment probabilities were \(p=0.762619\) for macro-F1 and \(p=0.729635\) for balanced accuracy. The predictive increment is therefore reproducible, but the present evidence does not localize that increment to exact garment-level morphology–RA14 pairing.

This is the most useful interpretation of the control. Category-conditioned radial–angular organization can remain informative even when RA14 comes from another garment in the same category. The representation carries structured geometric information, but that information need not behave as a unique residual tied to one particular morphology vector.

More broadly, feature concatenation and instance-specific complementarity should not be treated as equivalent. When grouped observations are available, restricted alignment controls provide a direct way to distinguish those two claims.

## 5.5 The second harmonic gives the representation a direct geometric meaning

The predictive experiments sit on top of a representation whose geometry is defined independently of classification performance.

For each radial shell,

\[
F_2(r)
=
\sum_k p(\theta_k\mid r)e^{-i2\theta_k}
=
C_2(r)-iS_2(r)
=
R_2(r)e^{-i2\alpha_2(r)}.
\]

Its magnitude,

\[
R_2(r)=\sqrt{C_2(r)^2+S_2(r)^2},
\]

measures the strength of second-order angular organization, while

\[
\alpha_2(r)
=
\frac12\operatorname{atan2}(S_2(r),C_2(r))
\pmod{\pi}
\]

gives the corresponding undirected axial orientation.

The use of \(m=2\) follows from the symmetry of an axis. Because

\[
\theta\equiv\theta+\pi,
\]

the second harmonic is the lowest non-zero Fourier order compatible with \(180^\circ\) equivalence. The observed low-order spectrum is consistent with this choice: among \(m=1,2,3,4\), the second harmonic had the largest median integrated and peak magnitude.

This gives RA14 an interpretable mathematical structure, but not a semantic one. A high \(R_2\) does not identify a sleeve, waistline, collar, flare, or other named design component. The coordinates measure harmonic organization rather than garment parts.

The same discipline applies algebraically. \(R_2=\sqrt{C_2^2+S_2^2}\) is an identity, not an independent confirmation among three variables, and radial extent was excluded because it is exactly termination radius minus onset radius. Axial directions were represented through \((\cos2\alpha,\sin2\alpha)\) so that the encoding respects axial periodicity.

## 5.6 Transformation behaviour separates intrinsic structure from coordinate-frame structure

Writing rotation in terms of the measurement-coordinate increment \(\phi\) defined in Methods (\(\phi=-\beta\) for raw Pillow raster angle \(\beta\)), the ideal transformation is

\[
F_2'(r)=e^{-i2\phi}F_2(r),
\qquad
R_2'(r)=R_2(r),
\]

and

\[
\alpha_2'=\alpha_2+\phi\pmod{\pi}.
\]

The earlier rigid-image rotation experiment was broadly consistent with this organization over the tested perturbations. Radial-magnitude profiles changed only modestly at the median, and axial orientations followed the imposed rotations closely. Magnitude-weighted mean orientation had a maximum 95th-percentile transformation error below \(0.85^\circ\).

A different control reveals what is supplied by the common image frame. Global analytic rotations preserved coordinate-free reconstruction behaviour, whereas assigning different rotations to different garment identities increased median peak-shell axial reconstruction error from \(4.104^\circ\) to \(44.675^\circ\), close to the \(45^\circ\) chance expectation for axial orientation.

Thus radius and \(R_2\) do not intrinsically determine phase. Much of the strong phase regularity observed in the upright dataset depends on population-level orientation structure relative to the canonical frame.

The later Experiment-08 audit further narrows the transformation-validity claim. Its prospectively frozen raster harmonic-magnitude P95 criterion failed even though analytic harmonic rotation and raster axial-angle subchecks passed. The earlier image-rotation observations therefore remain useful descriptive diagnostics, but they are not treated as confirmatory mechanical validation of RA14.

## 5.7 Broad radial summaries are more stable than localized coordinates

The sensitivity analyses reveal a useful hierarchy within the representation.

Integrated magnitude, radial centroid, and radial spread were comparatively stable under changes in radial domain and discretization. Localized descriptors—particularly peak radius, onset, termination, and concentration—were more sensitive to analysis boundaries and resolution.

This is especially clear for peak location. Approximately 22% of sketches selected a peak at a boundary of the primary radial domain, and among sketches peaking at the upper boundary \(r=27.5\), 40.9% moved outward when the domain was expanded.

Peak radius is therefore best interpreted as a localization statistic defined relative to the locked measurement window rather than as an intrinsic physical scale.

The shell-mass audit shows that this sensitivity is not explained simply by vanishing foreground support. Selected peak shells exceeded the tested minimum-mass threshold, but stronger mass filtering, radial-domain changes, and radial coarsening still affect localized quantities.

The practical implication is that RA14 should be treated as a fixed measurement specification. The predictive experiment validates the usefulness of the block under that specification; it does not imply that every coordinate has equal numerical portability.

## 5.8 Harmonic magnitude explains part of axial uncertainty

The relation between harmonic magnitude and axial uncertainty follows directly from the geometry of phase estimation.

For

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

For a fixed Cartesian perturbation, smaller harmonic magnitude makes phase estimation less well conditioned.

The garment-level results follow this geometry. Median peak \(R_2\) was negatively associated with median axial error (\(\rho=-0.356\)), while Cartesian reconstruction-error magnitude showed a stronger association (\(\rho=+0.760\)). Their combined conditioning quantity,

\[
\frac{\|\Delta(C_2,S_2)\|}{2R_2},
\]

was more strongly associated still (\(\rho=+0.789\)). Median axial error decreased from \(5.988^\circ\) in the weakest-\(R_2\) quartile to \(2.918^\circ\) in the strongest.

The interpretation is geometric rather than causal: harmonic strength conditions angular sensitivity, while the actual reconstruction perturbation also matters.

## 5.9 Scope, contribution, and next steps

The effective experimental population is the 230 recovered garment identities. Identity-disjoint validation therefore tests transfer to unseen recovered garments within CLO-SKET rather than external generalization to another dataset, drawing population, or design source.

The grouping is itself an important part of the study. Sketch-level random splitting would allow repeated renderings of the same source garment to cross the training/test boundary. By grouping complete garment identities in validation, bootstrap resampling, and alignment permutation, the analysis preserves the strongest observable dependency structure in the dataset.

Several boundaries remain. Garment identities were reconstructed rather than supplied through an independent lineage table, so higher-level dependence among designers, collections, or templates cannot be excluded. Both morphology and RA14 derive from the same images, so incremental predictive utility does not imply statistical or information-theoretic independence. The common upright coordinate frame carries substantial orientation structure. Localized radial descriptors remain domain-sensitive. The second harmonic is a targeted axial summary rather than a complete angular representation. No garment-part annotations or independent physical measurements are available.

Within those boundaries, the contribution has two connected parts.

The first is representational: a compact, explicit 14-dimensional description of radial second-harmonic organization and axial orientation with defined geometric meaning and transformation behaviour.

The second is methodological: a dependency-aware evaluation strategy that distinguishes three progressively stronger statements—whether the representation carries category information, whether it adds predictive value beyond another representation, and whether that added value depends on exact garment-level correspondence.

Experiment 06 supports the first two statements relative to morphology. Experiment 07 shows that the additional value is baseline-dependent. The alignment control does not support the third. Experiment 08 narrows the mechanical transformation-validity claim without altering the frozen Experiment-06 result.

The next scientific step is therefore not to enlarge the present claim, but to test it elsewhere. External garment-sketch collections with explicit garment, designer, and collection identifiers would provide the clearest validation. Orientation-normalized or rotation-equivariant variants could separate intrinsic geometry from acquisition-frame structure. Prospective semantic annotations could test whether the geometric coordinates correspond to recognizable design concepts. Category-level prototypes or distributional summaries could also test what form of category-conditioned structure accounts for the alignment result.

Together, these directions move the representation from an internally validated geometric measurement toward a more general model of garment-sketch structure.
