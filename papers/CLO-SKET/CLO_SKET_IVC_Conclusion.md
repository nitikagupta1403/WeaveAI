# 6. Conclusion

This study introduces a compact, explicit axial–radial representation of garment-sketch geometry and tests whether it contributes predictive information beyond a frozen morphology representation under garment-identity-disjoint validation. The 14-dimensional representation comprises eight radial descriptors of second-harmonic magnitude and six axial-safe orientation descriptors. Its construction follows directly from the geometry of undirected orientation: because an axial direction satisfies \(\theta\equiv\theta+\pi\), the second angular harmonic is the lowest non-zero Fourier order compatible with that symmetry.

The primary Experiment 06 result is a reproducible incremental predictive effect. Under the locked five-fold grouped evaluation, morphology alone achieved macro-F1 \(0.297788\) and balanced accuracy \(0.298261\), whereas morphology augmented with the complete axial–radial representation achieved macro-F1 \(0.335765\) and balanced accuracy \(0.336087\). The corresponding increments were

\[
\Delta F_1=+0.037977
\]

and

\[
\Delta BA=+0.037826.
\]

Category-stratified garment-identity bootstrap intervals excluded zero for both metrics: \([+0.020242,+0.055852]\) for macro-F1 and \([+0.020000,+0.056239]\) for balanced accuracy. The effect was also positive across all 10 repeated category-balanced grouped partitions, with mean macro-F1 increment \(+0.032253\) and range \(+0.020620\) to \(+0.043275\). Thus, the observed gain is not attributable to a single favorable identity partition.

The ablations localize most of the directly observed increment to radial organization. The radial block alone achieved macro-F1 \(0.206831\), compared with \(0.081165\) for the axial block, and adding the radial block to morphology increased macro-F1 by \(+0.026752\). Adding the axial block alone increased it by \(+0.002299\). The complete \(M+R+A\) representation nevertheless produced the largest primary score. These results support the predictive relevance of second-harmonic radial organization while leaving any additional conditional contribution of the axial block beyond \(M+R\) as a question for a separately specified test.

The alignment-permutation control places the strongest boundary on interpretation. Correctly aligned \(M+R+A\) did not outperform a category-preserving identity-level misalignment null unusually strongly: the empirical probabilities were \(p=0.762619\) for macro-F1 and \(p=0.729635\) for balanced accuracy. Consequently, the improvement over morphology cannot be attributed, on the present evidence, to exact garment-specific correspondence between the morphology and axial–radial representations. The supported claim is narrower: the compact axial–radial representation contains reproducible **category-conditioned predictive structure** that is useful alongside morphology, but the experiment does not demonstrate uniquely paired garment-level complementarity, statistical independence, or information-theoretic uniqueness.

The complementary geometric controls explain why such caution is necessary. Earlier rigid-image rotation experiments were broadly consistent with the intended invariant/equivariant organization over their tested perturbations, but a subsequent fresh mechanical audit (Experiment 08) failed its frozen raster harmonic-magnitude P95 gate. Those earlier rotation observations are therefore retained as descriptive diagnostics rather than treated as mechanical validation. Experiment-08 predictive comparisons are post-outcome / exploratory and do not rescue the failed gate. Garment-identity-specific analytic rotations also caused peak-shell axial reconstruction error to approach the \(45^\circ\) chance expectation. Thus, strong phase regularities in upright CLO-SKET sketches depend substantially on the common image coordinate frame. Sensitivity analyses further showed that broad radial summaries are more stable than localized quantities such as peak radius, onset, termination, and concentration, which remain conditional on radial domain and discretization.

Taken together, the evidence supports an explicit but bounded contribution. CLO-SKET contains radial–angular geometric structure that can be measured compactly, transferred to withheld garment identities, and used to improve category discrimination beyond a morphology baseline. The study also shows that predictive improvement alone is insufficient to establish instance-specific representational complementarity: a category-preserving alignment control is required to test that stronger interpretation, and here that test was negative.

The principal contribution is therefore both representational and methodological: a mathematically explicit axial–radial measurement of sparse garment sketches, coupled to a dependency-aware validation framework that distinguishes **predictive increment** from **garment-specific correspondence**. By retaining that distinction, the study identifies not only what the representation adds, but also where the available evidence stops.
