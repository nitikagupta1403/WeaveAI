# 5. Discussion

## 5.1 Principal findings

This study examined garment sketches as quantitative geometric objects using two explicit representations: a frozen 135-dimensional morphology representation and an independently constructed 28-dimensional radial–angular representation. Three findings define the contribution. First, the morphology measurements exhibited reproducible population-level organization across neighborhood, graph, multiscale-density, and permutation analyses, while retaining substantial within-region variation. Second, morphology and radial–angular measurements shared recoverable quantitative structure, including identity-generalizable information about F₂ magnitude, angular coherence, and observed–learned axial disagreement. Third, combining the two representations improved garment-category discrimination when complete source-garment identities were withheld from training.

The central result is therefore not the introduction of a new learning algorithm or an assertion that one handcrafted descriptor is universally optimal. It is an evidence-based characterization of garment-sketch morphology and a source-identity-aware demonstration that an alternative geometric coordinate system contributes additional downstream information beyond morphology under the tested task.

## 5.2 Morphology as a quantitative population

The morphology representation was designed to retain direct spatial interpretation. Horizontal and vertical occupancy coordinates describe how foreground structure varies across the canonical image axes, while the global descriptors summarize broader aspects of sketch geometry. Analysing these measurements jointly moves the study beyond isolated silhouette statistics toward a population-level view of sketch form.

The observed neighborhood and density-associated organization indicates that the sketches are not distributed as an arbitrary collection of independent measurements. At the same time, the results argue against a simple discrete-state interpretation. Within-region dispersion remained substantial, and density separation weakened across scale. The most defensible interpretation is therefore a structured but continuous morphology space containing locally reproducible organization rather than a small set of sharply separated garment states.

This distinction matters for the scientific positioning of the work. The findings support quantitative morphology organization without requiring semantic labels to construct the representation. They do not show that density regions correspond to garment parts, design concepts, or a latent garment grammar. Semantic interpretation would require independent annotation and validation beyond the geometric analyses performed here.

## 5.3 Complementarity under unseen-source-identity evaluation

The original image-level evaluation produced a substantial integration gain, increasing Macro-F1 from 0.3411 to 0.4123. However, audit showed that every test sketch had its source identity represented in the corresponding training set. The original result is therefore correctly interpreted as performance on unseen sketches of observed garments.

Under the stricter source-identity-grouped design, morphology alone achieved a Macro-F1 of 0.3068, whereas the integrated representation achieved 0.3414. The smaller gain of 0.0346 is scientifically more informative because it persisted when complete garment identities were excluded from training. The same direction was observed in all five primary folds, all ten repeated grouped partitions, and 18 of 23 garment categories. Identity-aware bootstrap intervals also excluded zero.

These results support complementary category-discriminative utility rather than a generic claim that adding features always improves prediction. Radial–angular descriptors alone were weaker than morphology, yet their combination with morphology was strongest. This pattern is consistent with a representation that is insufficient as a standalone description for the task but retains information that is useful conditional on the morphology coordinates.

The distinction between image-level and identity-grouped performance is itself an important methodological result. In sketch datasets containing multiple renderings of a source garment, image-level folds can answer a legitimate but narrower question than source-grouped folds. Reporting both makes the generalization target explicit and prevents performance on new sketches of familiar garments from being described as generalization to new garment identities.

## 5.4 Shared structure does not imply an exact alignment mechanism

Feature-level associations and grouped recovery show that the morphology and radial–angular branches are quantitatively related. This shared structure does not mean that the representations are redundant, nor does downstream complementarity prove that exact sketch-level correspondence causes the gain.

The within-category alignment control is important in this respect. Disrupting exact held-out morphology–radial–angular pairing while preserving category membership reduced performance slightly on average, but the aligned advantage was not sufficiently extreme relative to the perturbation distribution. The stronger statement that downstream utility depends on exact sketch-level alignment is therefore not supported.

The appropriate conclusion is narrower: radial–angular descriptors contain complementary category-discriminative information beyond morphology under unseen-source-identity evaluation. Much of this information may be associated with category-level geometric distributions rather than uniquely paired sketch-level residuals. Establishing an individual-level integration mechanism would require a stronger design, such as model-refitting conditional randomization, matched within-category analyses with greater independent identity variation, or evaluation on an external population with independently defined source identities.

## 5.5 Recoverability of radial–angular measurements

The recovery analyses clarify which aspects of radial–angular geometry are encoded in explicit morphology. F₂ peak magnitude showed the strongest identity-generalizable recovery, followed by axial-disagreement magnitude and observed R₂ at the F₂ peak. These findings indicate that occupancy-based morphology contains information about the strength and coherence of second-harmonic organization, not merely category labels used in the downstream classifier.

F₂ peak radius was notably weaker. Its grouped R² interval included zero, although its Spearman association remained positive. Morphology therefore preserved some ordinal information about where the F₂ maximum occurs but did not reliably predict its exact radial value. This difference illustrates why both metric-scale and rank-based measures were retained: a reproducible ordering can coexist with poor calibration of absolute target values.

The direct axial-orientation sensitivity analysis provided a further boundary. Doubled-angle prediction reduced mean error and improved tail-sensitive measures relative to the training-fold mean direction, but it performed worse for median error and tight 10° accuracy. Morphology thus contained limited directional information that helped some difficult cases, but it did not provide uniformly better orientation recovery than the dominant axial direction. This mixed result is appropriately treated as supplementary rather than as a primary contribution.

## 5.6 Scientific contribution

The novelty of the study lies primarily in its scientific characterization and validation framework rather than in any individual mathematical operation. Occupancy measurements, radial coordinates, Fourier harmonics, PCA, logistic regression, Ridge regression, and bootstrap resampling are established methods. The contribution arises from their controlled use to address a specific representation question:

> Can a population of garment sketches be characterized using explicit quantitative morphology, related to an independently constructed radial–angular description, and evaluated for complementary utility under unseen-source-garment separation?

The evidence supports an affirmative but bounded answer. The sketch population exhibits reproducible quantitative organization; the two explicit representations share recoverable structure; and their integration improves the tested classification task for unseen source identities. The study thereby adds an interpretable geometric layer between raw sketch images and task-specific predictive or generative systems.

## 5.7 Limitations

Several limitations constrain generalization. First, all analyses were performed on one dataset of 2,300 sketches and 23 predefined categories. The results therefore establish internal source-identity generalization, not external generalization across datasets, drawing conventions, institutions, or cultural design traditions.

Second, source identities were reconstructed from filenames rather than supplied through an independently curated provenance table. The recovered structure was coherent and enabled exact zero-overlap folds, but irregular separators, duplicate identity–replicate combinations, and 9–11 images per identity reveal imperfections in the underlying metadata. The grouped design preserved these irregularities rather than correcting them retrospectively.

Third, both representations were derived from the same source images. “Independent” refers to their construction and coordinate definitions, not to independent data acquisition. Associations between the branches may partly reflect shared image content, preprocessing, garment category, or other common causes. Feature-level associations and recovery analyses were not designed to decompose category-mediated from within-category correspondence.

Fourth, the predictive estimators were deliberately fixed and relatively simple. Logistic regression and Ridge regression provide interpretable information probes and avoid extensive model-selection flexibility, but they do not establish the maximum recoverable information in either representation. Conversely, evaluating many flexible models could inflate researcher degrees of freedom; the fixed-estimator design therefore trades predictive optimality for a clearer confirmatory boundary.

Fifth, the identity-aware bootstrap intervals condition on fixed out-of-fold predictions and do not include model-refitting variation. Repeated grouped partitions quantify sensitivity to fold allocation but are not independent confidence intervals. The within-category alignment analysis is likewise a fixed-model test-time perturbation rather than a full model-refitting conditional randomization test.

Finally, the downstream labels are predefined garment categories. Improved classification demonstrates task-level utility under that taxonomy but does not establish semantic understanding, causal representation, or general-purpose garment reasoning.

## 5.8 Future work

The most important next step is external validation on a sketch population with independently curated source identities and different drawing conditions. Such a study should freeze the present morphology and radial–angular definitions before transfer and evaluate both category discrimination and morphology-to-radial–angular recovery without representation redesign.

Additional work could separate category-level from within-category correspondence using hierarchical models or conditional randomization with model refitting. Direct circular modelling may also improve orientation analysis by representing predictive uncertainty rather than estimating doubled-angle components independently. Finally, expert annotations could be introduced after geometric discovery to test whether specific quantitative axes or regions correspond to interpretable design properties. Such semantic validation should be treated as a new experimental stage rather than inferred from geometry alone.

## 5.9 Conclusion

Garment sketches in CLO-SKET exhibit reproducible quantitative organization under an explicit morphology representation. An independently constructed radial–angular description shares measurable structure with morphology and adds category-discriminative information when complete source-garment identities are withheld from training. The evidence supports representation-level complementarity and identity-generalizable quantitative association, while remaining agnostic about discrete morphology states, semantic garment primitives, causal mechanisms, and universal garment structure.
