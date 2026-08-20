# 1. Introduction

Garment sketches encode design form before physical realization. A small number of lines can establish silhouette, proportion, symmetry, direction and the spatial arrangement of garment structure. Yet a sketch is not simply a low-detail photograph. It is a sparse geometric construction whose information is distributed relative to an implied centre, across distance from that centre and around angular directions. This makes garment sketches relevant not only to recognition, retrieval, generation and garment modelling, but also to a prior measurement question: **how can their radial and axial organization be represented explicitly and evaluated without assuming semantic meaning?**

Most computational work involving fashion sketches has been organized around downstream tasks, including sketch-based garment modelling, fashion-flat recognition, multimodal design and transfer from drawings to three-dimensional characters (An & Li, 2014; Fondevilla et al., 2021; Wang et al., 2018; Yasseen et al., 2013). These studies demonstrate the utility of sketch geometry, but task performance does not necessarily reveal which geometric properties carry the signal. Learned embeddings can be effective while leaving their coordinates difficult to interpret; conversely, handcrafted descriptors can appear interpretable while silently duplicating algebraically dependent quantities or encoding assumptions not tested by the data.

An explicit representation therefore requires more than assigning intuitive names to features. Each coordinate should have a declared mathematical source; exact identities and constructed dependencies should be distinguished from empirical associations; validation units should reflect the structure of the dataset; and uncertainty should account for repeated observations of the same underlying object. These requirements are particularly important for CLO-SKET, where multiple sketches are associated with each source garment (Arnia, 2020). A random split over individual sketch files can place different drawings of the same garment in both training and testing, thereby evaluating new renderings of familiar garments rather than transfer to unseen garment identities.

The present study develops a centroid-relative radial–angular description of 2,300 CLO-SKET images. For each sketch, foreground intensity is accumulated in radial and angular bins around an intensity-weighted centroid. Normalizing the angular weights within each radial shell produces a conditional angular distribution \(p(\theta\mid r)\). Its complex second harmonic is

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-\mathrm{i}2\theta_k}.
\]

The magnitude \(|F_2(r)|\) measures the strength of second-order angular organization at radius \(r\), while half of the phase defines an undirected or axial orientation. The doubled angle is essential: an axial direction satisfies \(\alpha\equiv\alpha+180^\circ\), unlike an ordinary directional variable. The construction therefore separates three interpretable aspects of sketch geometry: where radial-angular structure occurs, how strongly it is expressed and how its axial orientation varies across radius.

The study does not treat every quantity derived from this harmonic as a separate feature. The observed second resultant satisfies

\[
R_2(r)=\sqrt{C_2(r)^2+S_2(r)^2}=|F_2(r)|,
\]

and is therefore identical to the harmonic magnitude rather than independent evidence. Similarly, raw axial angles are unsuitable as ordinary linear coordinates because \(0^\circ\) and \(180^\circ\) denote the same axis. We address these issues through a provenance audit that retains only direct, non-tautological summaries and replaces axial angles by doubled-angle Cartesian coordinates.

The resulting primary representation is an exact 14-dimensional vector. Eight descriptors summarize the radial magnitude profile: its integral, radial centroid, spread, concentration near the discrete peak, onset radius, termination radius, peak radius and peak magnitude. Six descriptors summarize axial organization: cosine and sine encodings of the peak and magnitude-weighted mean axes, axial coherence and orientation drift. The representation is compact by construction, but compactness is not itself the central claim. Its importance lies in the traceable relationship between every coordinate and the underlying conditional angular field.

The representation permits a controlled information-loss experiment. Writing the observed second moment as

\[
F_2(r)=C_2(r)-\mathrm{i}S_2(r),
\]

we ask how well \(C_2(r)\) and \(S_2(r)\) can be reconstructed when the model is supplied only with radius and \(|F_2(r)|\), but not the harmonic phase. Reconstructed magnitude and axial orientation are then derived from the predicted Cartesian components. This experiment does not recover an independent physical target: predictor and targets arise from the same angular field. Instead, it measures how much component and orientation structure remains recoverable after phase has been deliberately omitted.

Validation is performed at the garment-identity level. Filename and category structure recover 230 category-qualified garment identities, each represented by approximately ten sketches. Five category-balanced folds withhold complete garment identities, place two identities from every category in each test fold and ensure zero identity overlap between training and testing. Final uncertainty estimation resamples complete garment identities, and primary association probabilities are obtained by permuting garment-level summaries within category strata. This design prevents the 2,300 correlated sketches from being treated as 2,300 independent sampling units.

The empirical analysis addresses three questions:

1. **Representation:** Can radial magnitude and axial phase be summarized in a finite, mathematically valid vector without retaining exact same-field derivatives or reconstruction-derived quantities as primary features?
2. **Reconstruction:** How much of the observed \(C_2/S_2\) field and peak-shell axial orientation is recoverable from radius and second-harmonic magnitude for unseen garment identities?
3. **Association:** Are observed peak-shell magnitude and selected peak radius associated with axial reconstruction error after the analysis unit is reduced to garment identity and category composition is held fixed?

The study makes four contributions. First, it provides a mathematically specified radial–angular construction based on conditional angular distributions and axial Fourier moments. Second, it establishes an exact \(8+6=14\)-dimensional provenance lock that excludes redundant, tautological and model-derived feature families. Third, it identifies garment-identity leakage in the historical sketch-level folds and replaces them with category-balanced, identity-disjoint out-of-fold reconstruction. Fourth, it separates algebraic verification, descriptive diagnostics and cluster-conditional inference through complete-identity bootstrap resampling and within-category permutation.

The intended contribution is geometric and methodological. We do not claim that the second harmonic identifies garment parts, that the learned reconstruction recovers the complete angular density, or that peak-shell magnitude is a causal or prospectively calibrated reliability measure. The study contains no semantic annotations, causal intervention or external physical measurement. It therefore does not establish semantic garment understanding, human-like interpretation, a universal garment grammar or a physical radial law. Within these boundaries, it demonstrates how garment sketches can be studied as explicit radial–angular objects while preserving the distinction between what is true by mathematics, what is observed descriptively and what is supported conditionally by statistical inference.
