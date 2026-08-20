# 5. Discussion

## 5.1 Principal findings

This study established and audited a compact radial–angular representation of garment sketches based on the second angular harmonic. Five findings define the contribution. First, the final primary representation was reduced to an exact, provenance-locked 14-dimensional vector containing eight direct \(F_2\) radial descriptors and six axial-safe \(\alpha_2\) descriptors. Second, source reconstruction identified 230 garment identities and showed that the historical sketch-level validation allowed complete garment-identity leakage. Third, repeating the reconstruction with category-balanced, identity-disjoint folds produced similar aggregate performance, demonstrating transfer to sketches from unseen recovered garment identities. Fourth, observed peak-shell second-harmonic magnitude and selected peak radius were modestly associated with axial reconstruction error at the garment-identity level. Fifth, the separation in observed \(R_2\) between outcome-defined low- and high-error bands remained directionally stable across four prespecified threshold choices.

The study therefore contributes neither a new classifier nor a claim of semantic garment understanding. Its contribution is an explicit mathematical representation, a computational-provenance audit, and a dependency-aware validation framework showing how radial location, bilateral angular strength, and axial orientation can be measured and reconstructed without confusing exact identities, shared-source diagnostics, descriptive contrasts, and conditional statistical evidence.

## 5.2 What the second angular harmonic measures

The conditional angular distribution \(p(\theta\mid r)\) describes how sketch intensity is distributed around the centroid at each radial shell. Its second harmonic,

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-\mathrm{i}2\theta_k},
\]

is naturally suited to axial organization because doubling the angle maps directions separated by \(180^\circ\) to the same point. The magnitude \(|F_2(r)|\) measures the strength of second-order or bilaterally repeated angular organization at shell \(r\), whereas the half-phase gives its undirected axial orientation. A strong magnitude does not identify a garment part or attach physical meaning to the axis; it indicates only that intensity at that shell is concentrated in a pattern expressed strongly by the second harmonic.

This separation between magnitude and phase is central to the interpretation. The eight radial descriptors summarize where and how strongly the second-harmonic magnitude occurs across radius. The six axial-safe descriptors summarize peak direction, magnitude-weighted mean direction, coherence across shells, and end-to-end orientation drift while respecting \(\alpha\equiv\alpha+180^\circ\). The representation is therefore explicit in the limited but useful sense that each coordinate has a declared geometric definition. “Explicit” does not imply semantic, causal, or uniquely sufficient.

## 5.3 Why the 14-dimensional lock strengthens the study

The historical 28-dimensional assembly combined direct descriptors with observed circular quantities, learned reconstruction outputs, and relational features. The audit showed that several such families were exact same-field derivatives, reconstructed derivatives, or tautological comparisons. In particular,

\[
R_2(r)=\sqrt{C_2(r)^2+S_2(r)^2}=|F_2(r)|,
\]

so observed \(R_2\) and observed \(|F_2|\) cannot be presented as independent sources of information. Similarly, radial extent is exactly termination radius minus onset radius and adds no independent coordinate once both endpoints are retained.

Removing these constructed or redundant quantities makes the final representation scientifically clearer. The retained \(8+6\) features are direct summaries of harmonic magnitude and phase, raw axial directions are encoded by \(\cos(2\alpha)\) and \(\sin(2\alpha)\), and the column order is computationally locked. This reduction is not merely dimensional compression. It prevents mathematical identities and model-derived quantities from being reintroduced as apparently independent evidence, thereby making both the representation and the manuscript easier to audit.

## 5.4 Garment identity, leakage and the relevant generalization target

The source-independence audit changed the interpretation of the validation design. Although no exact raw-file or decoded-pixel duplicates were found, the filenames and category folders revealed 230 garment identities, each represented by approximately ten sketches. Under the historical sketch-level folds, every test sketch had other sketches of the same garment identity in training. That design evaluates a legitimate but narrow problem—prediction for an unseen sketch of a previously observed garment—but it does not evaluate transfer to an unseen garment identity.

The identity-disjoint design instead kept every garment cluster intact. Each test fold contained two identities from every category, no identity crossed training and testing, and every sketch was predicted exactly once. This is the appropriate internal validation target for the current dataset because it prevents a model from exploiting repeated sketches of the same source garment across folds.

Despite the complete leakage detected in the earlier fold structure, aggregate reconstruction estimates changed little after identity separation. Whole-field \(R_2\) RMSE changed from 0.145516 to 0.145610, and peak-shell RMSE changed from 0.149218 to 0.148303. This stability suggests that the fitted relationship was not driven primarily by memorization of garment-specific replicates. It does not retroactively validate the historical folds: the identity-disjoint estimates are methodologically preferable because their generalization target is explicit and defensible.

## 5.5 Reconstruction from radius and harmonic magnitude

The identity-disjoint reconstruction used only radius and \(|F_2(r)|\) to estimate \(C_2(r)\) and \(S_2(r)\). Adding magnitude to radius reduced \(C_2\) RMSE by 24.06%, but reduced \(S_2\) RMSE by only 1.03%. This asymmetry is informative. Magnitude specifies the length of the second-moment vector but contains no explicit phase; it therefore cannot, by itself, determine how that vector divides into cosine and sine components. The larger gain for \(C_2\) may reflect population structure relative to the fixed image axes, whereas the weak incremental gain for \(S_2\) shows that magnitude does not recover both components equally. Because no rotational-control experiment was performed, the component asymmetry is treated as descriptive rather than as evidence of a preferred physical orientation.

This result must be interpreted as a shared-source reconstruction diagnostic. The predictor \(|F_2|\) and targets \(C_2,S_2\) arise from the same conditional angular field. The experiment asks how much of the component structure is recoverable after discarding phase and retaining only magnitude and radius. It does not demonstrate prediction of an independently observed biological, physical, or semantic quantity.

Reconstructed \(R_2\) remained strongly correlated with observed \(R_2\), but its peak-shell median was lower by 0.0843. Nearly every sketch had reconstructed peak magnitude below the observed value. This attenuation is consistent with calibration compression: regression toward common component values shortens the reconstructed resultant, particularly when phase information is unavailable. It should not be described as semantic failure or loss of a physical garment property.

## 5.6 Magnitude, radius and axial-error regimes

Median axial error decreased from 8.59° in the weakest observed-\(R_2\) quartile to 2.89° in the strongest quartile, and the high-error proportion decreased from 24.87% to 10.26%. At the garment-identity level, median observed peak-shell \(R_2\) was negatively associated with median axial error (Spearman \(\rho=-0.356\)). The direction remained visible when the error thresholds were varied: low-error sketches consistently had higher observed \(R_2\) than high-error sketches, with Cliff's \(\delta\) between 0.237 and 0.300 across the four prespecified definitions.

This pattern has a direct geometric explanation. When a resultant vector is short, small perturbations in its Cartesian components can cause a comparatively large change in its angle. Stronger second-harmonic magnitude therefore provides a more stable geometric basis for estimating axial orientation. The result is an association inherent partly in the vector geometry, not evidence that increasing \(R_2\) would causally improve a garment or that \(R_2\) is a calibrated prospective reliability score.

The near-zero within-quartile correlations do not contradict the overall ordering. Conditioning on a narrow range of observed \(R_2\) removes much of the variation that supports the population association. Moreover, the ordered quartile medians constitute four descriptive summaries, not four independent observations from which an inferential correlation should be calculated.

Selected peak radius also showed a negative garment-level association with axial error, and low-error sketches had a substantially larger median selected radius than high-error sketches. This result is best regarded as a dataset sensitivity. Peak radius is selected from 25 discrete shells, the search is bounded at 3.50 and 27.50, and 22.04% of peaks occurred exactly at a domain endpoint. The analysis therefore does not establish a continuous or physical radial law.

## 5.7 Statistical interpretation and evidentiary levels

The final analysis deliberately separates three forms of evidence. Exact computational identities, such as \(R_2=|F_2|\), are algebraic and require numerical verification rather than hypothesis testing. Descriptive diagnostics, including sketch-level correlations, quartile profiles, outcome-defined bands, and the observed-\(R_2\)-versus-\(\Delta R_2\) relationship, summarize the realized dataset but are not promoted as independent confirmatory tests. Conditional inferential statements are restricted to garment-level primary associations evaluated using complete-cluster bootstrap intervals and category-stratified permutation.

This distinction avoids several common errors. Reporting both \(|F_2|\) and \(R_2\) as separate predictors would double-count one quantity. Assigning a p-value to observed \(R_2\) versus \(\Delta R_2=\widehat R_2-R_2\) would ignore algebraic coupling. Treating four overlapping threshold definitions as independent replications would overstate evidence. Treating 2,300 correlated sketches as 2,300 independent units would understate uncertainty.

Even the garment-cluster analysis has a boundary. The filename convention establishes a defensible grouping unit, but it does not prove that the 230 garment identities are mutually independent. The confidence intervals and permutation results therefore support superpopulation language only conditional on that remaining assumption.

## 5.8 Scientific contribution

The individual operations used here—polar coordinates, Fourier moments, doubled-angle statistics, gradient-boosting regression, bootstrap resampling and permutation—are established methods. The scientific contribution lies in their controlled assembly into a representation and audit framework for garment sketches:

1. a centroid-relative conditional angular field that separates radial location from angular organization;
2. an axial second-harmonic description with mathematically valid \(180^\circ\) invariance;
3. an exact 14-dimensional feature lock that excludes same-field identities and reconstruction-derived features;
4. garment-identity-disjoint reconstruction that prevents replicate leakage; and
5. cluster-aware uncertainty with an explicit final claim boundary.

Together, these elements show that garment sketches contain measurable radial variation in the strength and orientation of bilateral angular organization. They also show precisely which parts of that organization remain recoverable when phase is omitted. This is a stronger and more reproducible contribution than claiming a broad semantic language unsupported by annotations or external semantic validation.

## 5.9 Limitations

First, all analyses used one dataset. Internal transfer to unseen recovered garment identities does not establish external generalization across datasets, designers, drawing instruments, preprocessing conventions, institutions, or cultural design traditions.

Second, garment identities were reconstructed from filenames and category folders rather than provided through a curated provenance table. Irregular separators, eight repeated identity–replicate records, and 9–11 sketches per identity demonstrate imperfections in the metadata. Although exact file and decoded-pixel duplication were absent, perceptual-hash candidates and broader designer, template, or collection lineage were not fully resolved.

Third, all harmonic quantities arise from the same source images and conditional angular field. Algebraic audits identify exact dependence, but shared-source empirical associations can still reflect common image construction, normalization, fixed alignment, category composition or other unmeasured structure.

Fourth, the radial domain is discrete and bounded. Peak selection can be unstable when neighboring shells have similar magnitudes, and endpoint peaks may be censored by the analysis window. Onset, termination and concentration can likewise be affected by domain clipping and the fixed 10% support and ±4-unit concentration definitions.

Fifth, the reconstruction inputs contain magnitude but no explicit phase. The model cannot be interpreted as a complete reconstruction of the conditional angular density, and axial orientation becomes intrinsically unstable when resultant magnitude is weak.

Sixth, the primary garment-level analysis reduces the sketches within each identity to medians. This gives identities equal weight and protects against pseudoreplication, but discards within-identity variation. Hierarchical modelling could represent both levels directly if independently curated lineage and a larger number of identities become available.

Finally, the study contains no garment-part annotations, semantic attributes, causal intervention, prospective reliability study or external physical measurement. Consequently, semantic recognition, human-like understanding, causal effects, prospective error classification and physical laws lie outside the evidence.

## 5.10 Future work

The highest-priority next step is external validation with independently curated garment, designer and collection identifiers. The current radial domain, feature definitions, 14-dimensional column order and identity-disjoint evaluation protocol should be frozen before transfer. This would test whether the observed reconstruction and association patterns survive changes in drawing population and image acquisition.

A hierarchical circular model could retain sketch-level variation while accounting for garment identity and category. Such a model should operate on doubled-angle quantities or an appropriate axial likelihood and should quantify uncertainty when resultant magnitude is weak. External annotations could subsequently test whether any radial or axial descriptor corresponds reproducibly to expert-defined design properties; that would constitute a new semantic-validation study rather than a reinterpretation of the current geometric evidence.

Further technical work could examine sensitivity to radial resolution, angular resolution, centroid definition, support threshold, concentration width and locked-domain endpoints. These analyses should be prespecified and should distinguish robustness of the representation from optimization against the current outcome. Reconstruction models that receive phase information may also be studied, but they would answer a different question from the current magnitude-only information-loss experiment.

## 5.11 Conclusion

CLO-SKET garment sketches exhibit measurable radial–angular organization under an explicit second-harmonic representation. The final provenance-locked vector contains eight direct radial-magnitude descriptors and six axial-safe orientation descriptors. It is an exact 14-dimensional construction with no PCA stage and no historical 28-dimensional family assembly.

After garment identities were recovered, the historical sketch-level folds were found to contain complete identity leakage. The replacement five-fold design withheld complete, category-balanced garment identities and achieved zero train/test identity overlap. Under this identity-disjoint evaluation, reconstructed resultant magnitude remained strongly aligned with observation across the field (RMSE $=0.145610$, Pearson $r=0.926390$) and at the observed peak shell (RMSE $=0.148303$, Pearson $r=0.810543$). Median peak-shell axial error was $4.104^\circ$ (garment-cluster bootstrap 95% CI $3.815^\circ$–$4.512^\circ$).

At the garment-identity level, observed peak-shell second-harmonic magnitude was modestly associated with lower axial error (Spearman $\rho=-0.355875$, 95% CI $-0.455749$ to $-0.248336$, Holm-adjusted $p=0.000200$). Selected peak radius showed a weaker negative association ($\rho=-0.207675$, 95% CI $-0.322472$ to $-0.095626$, Holm-adjusted $p=0.030097$). Descriptive low/high-error contrasts retained the same direction across four prespecified threshold pairs.

These findings establish a reproducible geometric measurement, provenance-audit and identity-aware validation framework. They do not establish semantic garment understanding, causality, a physical radial law, prospective reliability classification, von Mises fitting, or complete angular-density reconstruction. Statistical inference also remains conditional on mutual independence of the 230 recovered garment identities. The study is strongest precisely where its mathematics, validation unit and evidentiary boundaries are explicit.