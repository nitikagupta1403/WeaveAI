# 2. Related Work

## 2.1 Computational geometry of garment sketches

Garment sketches have been used as geometric inputs to several computational design problems. Sketch-based modelling systems recover garment boundaries or construction geometry from drawn contours and transform them into representations suitable for three-dimensional modelling or simulation. For example, Yasseen et al. (2013) generated quadrilateral garment meshes from contours sketched on a mannequin, demonstrating that sparse drawn geometry can constrain a simulation-ready garment representation. Fondevilla et al. (2021) used annotated fashion drawings to transfer garment style to three-dimensional characters, incorporating silhouette, borders, folds, pose, and body morphology. These studies establish that fashion drawings contain computationally recoverable information about garment form.

Learning-based work has extended this relationship across multiple garment modalities. Wang et al. (2018), for example, learned a shared latent space linking sketched fold patterns, body shape, sewing-pattern parameters, and simulated three-dimensional garments. Such methods enable reconstruction, editing, or retargeting across modalities, but their principal objective is task-oriented garment design. The sketch is encoded as an input to a predictive or generative system rather than treated as the primary observational unit of a population-level morphology analysis.

The present study addresses a different question. Instead of asking how a sketch can be transformed into a garment model, it asks whether geometric variation across a sketch population can be represented explicitly, examined as a quantitative space, and related to an independently constructed geometric coordinate system.

## 2.2 Explicit representations of fashion flats and silhouettes

Fashion-flat research provides direct precedent for mathematically defined contour representations. An and Li (2014) combined a wavelet Fourier descriptor with supervised dimensionality reduction and classification to discriminate fashion-flat categories. This work demonstrates that fashion-flat contours can be transformed into quantitative shape descriptors. However, a representation optimized to separate predefined classes answers a different question from an unsupervised characterization of how morphology varies across a sketch population.

Quantitative analysis of garment silhouettes also predates the present study. Tsuru et al. used standardized geometric measurements with multidimensional scaling and cluster analysis to classify clothing silhouettes. This establishes that fashion-silhouette populations can be analysed statistically using explicit geometric measurements. Accordingly, neither geometric garment descriptors, multivariate shape analysis, nor PCA-based organization is claimed here as novel in isolation.

The distinction lies in the observational object and evaluation design. Existing silhouette studies generally analyse physical garments, collection imagery, or predefined silhouette classes, whereas many sketch studies use drawings as inputs to reconstruction, transfer, or classification. The less-established intersection is the treatment of a heterogeneous population of two-dimensional garment sketches as the primary morphological population, using explicit image-derived measurements without defining the representation through semantic categories.

## 2.3 Geometric morphometrics and population-level shape

Geometric morphometrics provides a broader methodological foundation for treating visual form as quantitative data. Bookstein's sliding-semilandmark framework enabled curves without dense homologous landmarks to be incorporated into statistical shape analysis. McCane (2013) subsequently proposed a distance for outline shapes that does not require extraction of fixed discrete points along each curve and used the resulting distances to embed shape samples in a low-dimensional Euclidean space.

These approaches establish a general progression from individual outline representation to population-level shape geometry. They also emphasize that a numerical encoding does not automatically constitute a scientifically meaningful morphology: the representation, correspondence assumptions, distance, and inferential procedure must be appropriate to the object being studied.

The morphology representation used here is not presented as a conventional landmark-based morphometric model. Rather, geometric morphometrics motivates the underlying principle that explicitly measured form can be analysed at the population level while keeping representation assumptions and claim boundaries visible.

## 2.4 Alternative representations and cross-representation evidence

Any organization observed in one feature system may partly reflect the coordinate system used to describe the data. Agreement between independently constructed representations therefore provides a stronger test than structure observed in one representation alone. In the present study, each sketch is described both by a 135-dimensional occupancy-based morphology representation and by a 28-dimensional radial–angular representation derived independently from centroid-referenced radial and circular geometry.

The scientific question is not whether these representations are identical or statistically independent. Instead, we test whether they capture reproducibly related information about the same sketches. This distinction is evaluated at two levels. Feature-wise association and cross-validated recovery measure shared quantitative structure, while downstream classification tests whether radial–angular descriptors provide additional task-relevant information when combined with morphology.

Cross-representation association does not imply complementarity. Two representations may be strongly related yet contribute little incremental predictive information, or they may share broad structure while retaining task-relevant differences. Complementarity must therefore be evaluated directly by comparing morphology alone, radial–angular descriptors alone, and their integration under identical held-out observations.

## 2.5 Identity-aware evaluation of sketch representations

Sketch datasets may contain multiple drawings derived from the same source garment. Conventional image-level cross-validation can then place drawings of one source identity in both training and testing. Such a design measures performance on unseen sketches but does not establish generalization to unseen garment identities.

This distinction is central to the present work. Historical image-level results are retained as reproduction analyses, whereas primary downstream and recovery results use source-identity-grouped folds that withhold complete garments. Each grouped fold preserves all garment categories, preventing the evaluation from conflating missing-category effects with source-identity separation. Identity-aware bootstrap resampling and repeated grouped partitions further distinguish uncertainty across source garments from sensitivity to a particular fold allocation.

The same logic constrains mechanistic interpretation of representation complementarity. A gain from concatenated features does not by itself show that performance depends on exact sketch-level alignment. We therefore use a within-category alignment control that preserves garment-category membership and category-level radial–angular distributions while disrupting exact held-out sketch pairing. This separates evidence for complementary category-discriminative information from the stronger claim that integration requires exact morphology–radial–angular correspondence for each sketch.

## 2.6 Research gap and questions

Prior work establishes that garment sketches contain recoverable geometric information, that fashion flats and silhouettes can be represented using explicit shape descriptors, that garment populations can be examined with multivariate methods, and that general outline populations can be analysed geometrically. What remains less established is an evidence chain in which a population of two-dimensional garment sketches is represented explicitly, related to an independently constructed geometric description, and evaluated for complementary utility under complete source-garment separation.

The study therefore addresses three research questions:

1. **Does an explicit 135-dimensional morphology representation exhibit reproducible quantitative organization across the CLO-SKET sketch population?**
2. **Are independently derived radial–angular measurements associated with morphology and recoverable for previously unseen source-garment identities?**
3. **Does the radial–angular representation provide complementary category-discriminative information beyond morphology under unseen-source-identity evaluation?**

These questions are deliberately representation-focused. The study does not seek to learn semantic garment parts, establish a universal morphology vocabulary, identify discrete morphology states, or infer causal mechanisms. Its intended contribution is an empirically validated geometric layer for analysing garment-sketch morphology and testing the relationship between alternative explicit representations.
