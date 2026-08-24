# CLO-SKET Paper 2 — Final Discussion

## Status

**FINAL DISCUSSION ASSEMBLY: REWRITTEN TO MATCH THE EVIDENCE-CONTROLLED RESULTS SPINE**

This Discussion interprets only the frozen Paper-II evidence. It preserves the distinction between confirmatory radial-representation selection, validated latent-model comparison, nonlinear predictive-structure characterization, and descriptive retained-subspace morphology localization.

---

# 5. Discussion

## 5.1 Evidence-controlled representation design is the central contribution

The main contribution of this study is not a new Fourier transform, DCT basis, wavelet family, or PCA procedure. Each of those elements has substantial prior precedent. The methodological contribution lies instead in treating representation complexity as an empirical decision that may differ across a structured spectral field.

Starting from the radial-harmonic morphology field \(F_k(r)\), radial representation was evaluated separately across prespecified angular harmonic ranges. Compact encodings entered the final representation only when they were supported under garment-identity-disjoint validation with simultaneous family-wise error control. Where that support was not established, complete radial structure was preserved rather than compressed by default.

The resulting representation was

\[
\boxed{
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
}.
\]

This structure is important because it was not chosen for architectural symmetry. The low and highest tested harmonic bands supported compact radial encodings, while the two intermediate ranges did not. The framework therefore embodies the principle

\[
\boxed{
\text{compress where supported; preserve otherwise.}
}
\]

This is more than a compression rule. It is a representation-preservation rule. Negative evidence contributes directly to the architecture by preventing unsupported dimensional reduction.

The conclusion is deliberately conditional. The present experiments establish that support for the tested radial compression strategies differed across angular harmonic scale under the frozen CLO-SKET validation design. They do not establish a universal law relating angular harmonic order to radial complexity, nor do they prove that the intermediate bands are intrinsically incompressible.

---

## 5.2 The heterogeneous representation rejects simple spectral heuristics

The selected DCT/raw/raw/wavelet structure also cautions against a simple low-frequency-signal/high-frequency-noise interpretation of garment-sketch morphology. If useful structure decreased monotonically with harmonic order, one might expect progressively stronger compression support toward the highest harmonics. That pattern was not observed. The highest tested band, \(k=25{:}36\), supported compact db4-wavelet encoding, whereas both intermediate bands, \(k=5{:}24\), retained complete 72-shell radial structure.

The retained latent morphology showed a similarly non-monotonic organization. Within the PCA-64 subspace, 78.54% of variance-weighted mapped morphology energy occurred at intermediate harmonic orders \(k=5{:}24\). Thus, the bands that were not supported for tested compression also contained much of the mapped variation represented by the retained latent subspace. These two results should not be conflated causally: compression inference asks whether a tested compact representation can replace the full radial field under the held-out identity criterion, whereas latent localization asks where retained PCA perturbation energy lies after the final representation has been frozen.

The two supported compact bases also differed. The lowest harmonic band retained four DCT coefficients, whereas the highest band retained four db4-wavelet coefficients. The contrast is consistent with different radial organizations being represented efficiently by different basis families, but the experiment does not establish an intrinsic physical correspondence between low harmonics and global smoothness or between high harmonics and wavelet-like structure.

The hybrid representation reduced the complex coefficient count from 2592 to 1504, a 41.98% reduction. That value is strictly a representation-dimensionality result. It is not an estimate of removed noise, redundant morphology, irrelevant geometry, or semantic content.

---

## 5.3 Nonlinear pairwise structure and nonlinear-model utility are different scientific questions

The latent analysis illustrates a second methodological principle: detectable nonlinear predictive structure does not automatically justify a nonlinear latent model.

At matched latent dimensions, the tested AE and VAE representations did not establish a multiplicity-controlled held-out garment-identity retrieval advantage over PCA. This comparison is conditional on the hybrid representation already selected by the preceding cross-validated band analysis; it is not an untouched end-to-end validation of representation selection followed by latent-model selection. The strongest observed nonlinear contrast was \(\mathrm{VAE}_{16}-\mathrm{PCA}_{16}\), with mean \(\Delta\mathrm{MRR}=+0.014341\), but its max-statistic adjusted fold-level probability was \(p=0.2500\). PCA was therefore retained as the practical latent baseline **within the frozen hybrid representation** because the downstream comparison did not provide sufficient evidence to replace it.

That decision does not imply that every relationship in the representation is linear. A separate held-out audit found one FWER-supported quadratic PCA-coordinate relation, with best mean improvement

\[
\overline{\Delta R^2}=+0.432042.
\]

The appropriate interpretation is **pairwise nonlinear predictability**: for one prespecified directed PC relation, the fixed quadratic predictor improved held-out prediction relative to the corresponding linear predictor. This result is not, by itself, evidence of differential-geometric manifold curvature; category structure or other mixture effects may also generate nonlinear coordinate relationships.

The neighborhood dimensionality calculation is retained only as a scale-conditioned descriptive diagnostic. At 20 neighbours, the identity-level median number of directions required for 90% within-neighborhood variance was 15, but a centered 20-neighbour matrix has rank at most 19 by construction. The value therefore cannot support a quantitative comparison with the global PCA dimension or an intrinsic-dimensionality claim, and the previously reported local/global ratio is retired.

These results are compatible rather than contradictory. Nonlinear pairwise predictability can be present without producing a measurable generalization advantage for a particular nonlinear encoder, dataset size, task, or validation design. Conversely, failure of the tested nonlinear models to outperform PCA is not evidence that all relationships in the morphology representation are linear.

The principal-curve and diffusion-map sensitivity analyses reinforce this bounded interpretation. They did not establish a single stable nonlinear coordinate system or canonical one-dimensional morphology trajectory that warranted replacing PCA. Accordingly,

\[
\boxed{
\text{nonlinear pairwise structure}
\neq
\text{validated nonlinear-model utility}.
}
\]

PCA should therefore be understood here as a practical validated basis, not as a claim about the fundamental geometry of garment morphology.

---

## 5.4 Exact latent-to-Fourier mapping provides mathematical traceability

A central advantage of retaining an explicit radial-harmonic representation is that latent variation can be mapped back to the coordinates from which the representation was constructed.

For PCA direction \(j\), a one-score-standard-deviation perturbation is mapped through the exact frozen inverse hybrid representation to obtain

\[
\Delta F_j(r,k).
\]

Because PCA eigenvector orientation is arbitrary, interpretation is based on the sign-invariant morphology-energy field

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

The resulting traceability chain is

\[
\boxed{
PC_j
\rightarrow
\Delta F_j(r,k)
\rightarrow
E_j(r,k).
}
\]

This construction does not make PCA components semantic factors. Its value is more basic: variation expressed in a latent coordinate can be localized in explicit radial and harmonic coordinates rather than remaining an opaque embedding dimension.

The selected examples illustrate that different latent directions occupy different regions of the morphology field. PC1 and PC3 were strongly outer-radial, whereas PC15 was predominantly inner-radial. Their maximum-energy harmonic coordinates also differed. These differences show that the retained PCA space contains multiple radial-harmonic modes of variation rather than a single uniform morphology pattern.

This form of interpretability is mathematical rather than semantic. It establishes where a latent perturbation acts in the representation; it does not establish what garment attribute that perturbation means.

---

## 5.5 Retained-subspace localization is informative only with its denominator and claim boundary intact

The first 64 principal components accounted for 44.65% of variance in the standardized frozen representation. All subsequent radial-harmonic localization therefore applies only to that retained PCA-64 subspace.

Within this subspace, 78.54% of variance-weighted mapped morphology energy occurred at intermediate harmonic orders \(k=5{:}24\), 66.84% occurred in the outer radial zone \(r=49{:}72\), and 51.30% occurred jointly in the outer-radial × intermediate-harmonic region. The largest individual radial-harmonic cells were outer × \(k=13{:}24\) and outer × \(k=5{:}12\).

These numbers describe how variation represented by PCA-64 is localized after exact inverse mapping. They are not percentages of total garment morphology, not percentages of the complete 3008-dimensional representation, and not estimates of semantic garment-part contribution.

The radial coordinates themselves also remain morphological rather than semantic. In particular,

\[
\boxed{
\text{outer radial}
\neq
\text{garment boundary}.
}
\]

The radial zones are partitions of the representation space, not annotated regions such as hem, sleeve, neckline, waist, or silhouette edge. Likewise, harmonic order and PCA index are mathematical coordinates rather than garment attributes.

The 51.30% joint outer-radial × intermediate-harmonic quantity is also descriptive. No radial-zone-by-harmonic-band interaction or independence hypothesis was tested, so the observation should not be described as enrichment, synergy, coupling, or interaction.

These boundaries are not merely conservative wording. They define what kind of interpretability the present framework actually supplies: explicit spatial-spectral localization with a verifiable mathematical denominator, without semantic labels that the data do not contain.

---

## 5.6 Limitations and generalizability

Several limitations determine how broadly these findings can be interpreted.

First, the empirical results are currently specific to CLO-SKET. Garment identity and category structure were incorporated into validation, but independent garment-sketch datasets are required before the selected DCT/raw/raw/wavelet pattern can be considered a general property of fashion-sketch morphology.

Second, radial-representation selection is conditional on the candidate family, coefficient budgets, objective, and validation statistic tested here. The lack of support for compression at \(k=5{:}24\) does not imply that no compact representation exists for those ranges. Alternative analytical bases, adaptive dictionaries, learned representations, larger budgets, or different evaluation objectives could lead to different decisions.

Third, the nonlinear-model conclusion is also model-conditional. It applies to the tested PCA, AE, and VAE configurations, latent dimensions, dataset size, and five-fold outer validation design. With only five outer folds, exhaustive fold-level sign-flip inference has coarse probability resolution, and overlapping training sets limit population-level interpretation. The result therefore supports retention of PCA under the present evidence rather than a general rejection of nonlinear latent modeling.

Fourth, the neighborhood dimensionality diagnostic is scale- and sample-size-dependent. At the prespecified 20-neighbour scale, the centered local matrix has rank at most 19; the observed median of 15 is therefore retained only as a descriptive within-neighborhood variance summary and is not interpreted as an intrinsic dimension or compared quantitatively with the global PCA dimension.

Finally, the PCA localization analysis is limited by its 44.65% retained-variance denominator and by the absence of independent semantic or spatial garment annotations. The current study can localize variation mathematically but cannot determine whether particular radial-harmonic patterns correspond reproducibly to named garment features.

---

## 5.7 Implications and future work

The broad methodological implication is that dimensionality reduction need not be imposed uniformly across a structured representation. When the representation has interpretable subdomains—here, angular harmonic ranges with explicit radial dependence—complexity can instead be treated as a locally testable design choice.

This suggests a more general workflow:

\[
\boxed{
\text{structured representation}
\rightarrow
\text{subdomain-specific candidate encodings}
\rightarrow
\text{held-out evidence}
\rightarrow
\text{compress or preserve}
}.
\]

Such a principle could be useful beyond garment sketches wherever morphology is represented over organized spatial, spectral, temporal, or multiscale coordinates. The present study does not establish transfer to those domains, but it provides a concrete example of how representation reduction can be made conditional on evidence rather than architectural convenience.

For garment morphology specifically, the first priority is external replication of the harmonic-dependent radial-selection pattern. The candidate radial family can then be expanded while retaining the same identity-disjoint and multiplicity-controlled decision logic. A larger dataset would also permit stronger tests of nonlinear latent models and more stable geometry inference.

A second priority is semantic validation. Spatial annotations or garment-attribute labels would allow direct tests of whether particular radial-harmonic localization patterns correspond reproducibly to sleeves, neckline structure, waist shape, hem geometry, silhouette, or other interpretable garment properties. Until such labels are introduced, those meanings should not be inferred from mathematical coordinates alone.

A third direction follows from the exact inverse mapping. Controlled perturbations localized to selected \((r,k)\) regions could be reconstructed and evaluated to determine whether they produce reproducible geometric changes. Such experiments would move the framework from descriptive localization toward experimentally testable morphology control. They would constitute a new study rather than evidence already established here.

---

## 5.8 Scientific interpretation

The strongest conclusion from Paper II is not that one transform is superior to another. It is that representation complexity did not behave uniformly across the radial-harmonic morphology field, and that this heterogeneity could be handled explicitly rather than hidden inside a single global descriptor.

Under the CLO-SKET identity-disjoint inferential framework, compact radial representations were supported for the lowest and highest tested harmonic bands, whereas full radial structure was preserved in the intermediate ranges because the tested compression alternatives did not receive sufficient support. The resulting hybrid reduced coefficient count without assuming uniform compressibility.

At the latent level, greater model complexity likewise had to earn empirical support. The tested nonlinear encoders did not establish a multiplicity-controlled task advantage over PCA, even though a separate audit detected nonlinear pairwise predictability. PCA therefore remained the practical representation for interpretation without being promoted to a claim of intrinsic linearity.

Finally, exact inverse mapping retained traceability from latent coordinates back to radial-harmonic morphology. Within the PCA-64 subspace, mapped variation showed strong intermediate-harmonic and outer-radial organization while individual components remained heterogeneous.

The scientific identity of the paper can therefore be summarized as follows:

\[
\boxed{
\text{representation complexity must earn empirical support;}
\newline
\text{unsupported structure is preserved rather than discarded;}
\newline
\text{and retained latent variation remains traceable to explicit morphology coordinates.}
}
\]

The contribution is thus not a new spectral transform, but an evidence-controlled strategy for deciding how different parts of a structured morphology representation should be encoded, preserved, and interpreted.