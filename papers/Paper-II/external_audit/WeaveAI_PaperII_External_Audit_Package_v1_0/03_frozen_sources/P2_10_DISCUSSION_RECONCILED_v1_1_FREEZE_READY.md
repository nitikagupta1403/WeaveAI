# CLO-SKET Paper 2 — Reconciled Discussion v1.1

## Status

**FREEZE-READY DISCUSSION v1.1 — RECONCILED WITH P2_13 v1.0**

This Discussion interprets only frozen Paper-II evidence. It preserves the distinction between representation-validity auditing, confirmatory radial-representation selection, validated latent-model comparison, nonlinear predictive-structure characterization, and descriptive retained-subspace morphology localization.

---

# 5. Discussion

## 5.1 Representation validity precedes representation optimization

The central revision introduced by the 05F–05K audit is conceptual rather than numerical. The original Paper-II analysis asked how radial representation complexity should be allocated across angular harmonic scale. The later support-dependence audit showed that an earlier question had to be made explicit first: **which observed spectral allocation belongs to the garment and which depends on the raster frame in which the garment is represented?**

The historical radial-angular representation normalized radius relative to the complete raster grid. That construction is mathematically valid, but 05K demonstrated that the resulting angular spectral allocation is not neutral to surrounding raster support. When the garment pixel rectangle was held fixed and only blank raster support was enlarged, the historical raster-relative representation showed systematic redistribution toward lower angular bands and away from high-middle/high bands. The endpoint response was broad, all 23 category medians followed the prespecified low/high-middle/high directions, and the category-level effects survived exact joint max-\(T\) inference.

The matched object-relative construction behaved differently. Under the same same-pixel support manipulation, it remained numerically invariant across all tested support conditions. This result does not establish a new normalization method. Object-centering and scale normalization are established ideas in shape analysis. Its value here is as a matched counterfactual demonstrating that the support dependency observed in the historical representation is not inevitable when radial coordinates are defined relative to the object rather than the surrounding raster.

The principal implication is therefore not that Fourier analysis is intrinsically unstable to padding. The relevant dependency arises from the coordinate system through which the garment is mapped into radial-angular space. Changing the observation frame changes the raster-relative radial coordinate assignment even when the embedded garment pixels themselves are unchanged.

The strongest permitted statement is:

\[
\boxed{
\text{raster support is a demonstrated dependency of angular spectral allocation}
}
\]

under the tested historical raster-relative representation.

That statement is narrower than several tempting alternatives. The experiments do not show that all Fourier shape descriptors are support-dependent in the same way, that blank padding creates new garment information, that the historical representation is invalid for all downstream uses, or that support explains every natural RAW-to-CROP difference.

This distinction matters for the rest of the paper. Representation selection is still meaningful, but its conclusions are conditional on the measurement system in which they were obtained.

---

## 5.2 The 05F–05K sequence separates localization, association, and controlled intervention

The support-dependence result is strongest when the audit sequence is interpreted as a chain rather than as a single experiment.

The 05F preprocessing decomposition localized the historical high-band change. Text blanking alone did not reproduce the population-level effect, and the additional resize/pad stage contributed little after cropping. Most of the historical high-band change entered at the crop-only stage. This falsified the earlier working suspicion that bicubic resampling was the dominant source of the collapse.

Localization, however, is not mechanism. The 05G audit therefore examined candidate descriptors while verifying that the retained garment rectangle was pixel-identical across the RAW and crop representations and that centroid map-back error was zero. The strongest surviving associations involved foreground radial extent relative to raster support rather than centroid displacement, interpolation, or border-gradient concentration alone.

The 05J population audit then showed that stronger crop-induced raster-relative tightening was associated with redistribution away from lower angular bands and toward high-middle/high bands. The association was broad but moderate in magnitude, so it did not justify a deterministic explanation.

Only 05K provided a controlled intervention. Support was enlarged while the garment rectangle itself was copied unchanged and without resizing, interpolation, antialiasing, contour retracing, rethresholding, or crop recomputation. Under that manipulation, the historical raster-relative representation exhibited the predicted inverse response to the natural crop-tightening pattern observed in 05J.

The resulting evidential progression is:

\[
\boxed{
\text{05F: where the effect enters}
}
\]

\[
\boxed{
\text{05G/05J: what it is associated with}
}
\]

\[
\boxed{
\text{05K: support itself is a controlled dependency}
}
\]

This progression is important because it prevents the paper from overclaiming a complete preprocessing mechanism. The controlled support intervention demonstrates one genuine dependency of the historical representation. It does not exclude additional contributors to the full RAW-to-CROP transformation.

---

## 5.3 The representation-validity contribution is distinct from classical normalization prior art

The support audit must be positioned carefully relative to prior shape-analysis literature.

Fourier descriptors, elliptic Fourier descriptors, polar-raster Fourier descriptors, Angular Radial Transform descriptors, Zernike moments, translation normalization, rotation normalization, scale normalization, and object-centered coordinate constructions are all established prior art. The present paper does not claim novelty for those components.

Likewise, finite-window Fourier theory, zero-padding, digital discretization effects, and crop sensitivity are not new topics.

The distinction is experimental. In the reviewed literature, we did not identify a direct precedent that combined:

\[
\text{bit-identical foreground pixels}
\]

with

\[
\text{independent 2-D raster-support manipulation}
\]

without resizing or interpolation, together with a prespecified support dose, predefined angular-band redistribution endpoints, population-level inference, and a matched object-relative invariance control.

Accordingly, the novelty boundary should remain:

> We did not identify a direct precedent in the reviewed literature for this specific controlled support-dependence audit.

This is a literature-positioning statement, not an absolute priority claim.

The paper should therefore avoid phrases such as “first invariant Fourier descriptor,” “new scale normalization,” or “Fourier descriptors were previously assumed invariant to image size.” Those formulations would overstate the contribution and blur the distinction between established normalization mathematics and the controlled audit design introduced here.

A particularly important terminological boundary concerns zero-padding. Ordinary Fourier zero-padding appends zeros to a sampled signal before evaluating its spectral response and is a standard signal-processing operation. The 05K result should not be described as evidence that zero-padding creates low-frequency garment information. The effect arises because the historical radial-angular field is recomputed after the raster frame changes, thereby changing the mapping between garment location and raster-relative radial coordinates.

---

## 5.4 Evidence-controlled representation design remains the primary representation-learning contribution

Once the behavior of the measurement system is made explicit, the original representation-selection contribution remains intact.

The main methodological contribution is not a new Fourier transform, DCT basis, wavelet family, or PCA procedure. The contribution lies in treating representation complexity as an empirical decision that may differ across a structured spectral field.

Starting from the radial-harmonic morphology field \(F_k(r)\), radial representation was evaluated separately across prespecified angular harmonic ranges. Compact encodings entered the final representation only when they were supported under garment-identity-disjoint validation with simultaneous family-wise error control. Where that support was not established, complete radial structure was preserved rather than compressed by default.

The resulting historical representation was

\[
\boxed{
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
}.
\]

This structure was not chosen for architectural symmetry. The low and highest tested harmonic bands supported compact radial encodings, whereas the two intermediate ranges did not.

The governing principle is:

\[
\boxed{
\text{compress where supported; preserve otherwise.}
}
\]

This is more than a compression rule. It is also a representation-preservation rule. Negative inferential evidence contributes directly to the architecture by preventing unsupported dimensional reduction.

The decision procedure separates candidate admissibility from confirmatory evidence. A compact candidate first had to retain at least 95% of training-fold retrieval MRR relative to the complete radial reference. Passing that screen did not itself authorize compression. The selected candidate then had to show multiplicity-controlled positive held-out evidence on the category-balanced garment-separation endpoint.

This should not be interpreted as denoising. No discarded coefficient was classified as noise.

The conclusion remains conditional. The experiments establish that support for the tested radial compression strategies differed across angular harmonic scale under the frozen CLO-SKET validation design. They do not establish a universal law relating angular harmonic order to radial complexity, nor do they prove that the intermediate bands are intrinsically incompressible.

Most importantly after 05K, these historical selection results must be read as conditional on the raster-relative coordinate system in which they were obtained. The support audit does not invalidate them, but it clarifies their measurement context.

---

## 5.5 The heterogeneous representation rejects simple spectral heuristics

The selected DCT/raw/raw/wavelet structure cautions against a simple low-frequency-signal/high-frequency-noise interpretation of garment-sketch morphology.

If useful structure decreased monotonically with harmonic order, one might expect progressively stronger compression support toward the highest harmonics. That pattern was not observed. The highest tested band, \(k=25{:}36\), supported compact db4-wavelet encoding, whereas both intermediate bands, \(k=5{:}24\), retained complete 72-shell radial structure.

The retained latent morphology showed a similarly non-monotonic organization. Within the PCA-64 subspace, 78.54% of variance-weighted mapped morphology energy occurred at intermediate harmonic orders \(k=5{:}24\). Thus, the bands that were not supported for tested compression also contained much of the mapped variation represented by the retained latent subspace.

These two results should not be conflated causally. Compression inference asks whether a tested compact representation can replace the full radial field under the held-out identity criterion, whereas latent localization asks where retained PCA perturbation energy lies after the final representation has been frozen.

The two supported compact bases also differed. The lowest harmonic band retained four DCT coefficients, whereas the highest retained four db4-wavelet coefficients. This contrast is consistent with different radial organizations being represented efficiently by different basis families, but the experiment does not establish an intrinsic physical correspondence between low harmonics and global smoothness or between high harmonics and wavelet-like structure.

The hybrid reduced the complex coefficient count from 2592 to 1504, a 41.98% reduction. That value is strictly a representation-dimensionality result. It is not an estimate of removed noise, redundant morphology, irrelevant geometry, or semantic content.

---

## 5.6 Conditional angular morphology intentionally differs from radial occupancy and mass

The exclusion of \(k=0\) from the frozen hybrid requires a precise interpretation. For an occupied radial shell, conditioning over angle fixes

\[
F_0(r)
=
\sum_{\theta}
P(\theta\mid r)
=
1,
\]

whereas an empty shell has \(F_0(r)=0\). The DC coefficient therefore represents occupancy status under the conditional normalization rather than the amount of ink occurring at that radius.

Radial mass,

\[
M(r),
\]

is a separate quantity defined before within-shell angular normalization.

This distinction matters because an empty shell and an occupied shell with perfectly uniform angular probability both have zero positive harmonics. The dedicated occupancy sensitivity analysis showed that this theoretical ambiguity had negligible practical consequence for CLO-SKET: 99.8569% of sketch-shell locations were occupied, and appending the complete 72-dimensional occupancy mask slightly decreased mean MRR by 0.000651.

Radial mass was more informative, but only modestly so. Appending the lineage-verified \(M(r)\) profile increased mean MRR by 0.003486 and mean top-1 retrieval by 0.006973. Because this was a descriptive post-selection sensitivity rather than a prespecified inferential comparison, the gain is not interpreted as statistically established superiority.

The primary 3008-dimensional representation is therefore retained unchanged. Its scope is deliberately narrower than a complete reconstruction of sketch ink: it represents angular morphology conditional on radial location.

---

## 5.7 Whole-representation baselines support a bounded heterogeneity claim

The descriptor-level sensitivity analysis provides an important check on how strongly the heterogeneous architecture should be presented.

The hybrid did not exceed the complete \(\mathrm{RAW}_{72}\) representation in mean retrieval: full radial structure was descriptively higher by 0.002607 MRR. However, the complete representation required 5184 real coordinates, compared with 3008 for the hybrid.

The nearly dimension-matched uniform \(\mathrm{RAW}_{42}\) descriptor was also competitive, differing from the hybrid by only

\[
-0.000870
\]

mean MRR.

This is an important reviewer-facing boundary. The hybrid should not be presented as a retrieval-performance breakthrough or as proof that heterogeneous encoding is uniquely necessary for competitive retrieval.

The stronger descriptive differences appeared when a single compact transform was imposed uniformly across all harmonics. Uniform DCT-42 reduced mean MRR by 0.033263 relative to the hybrid, and uniform db4-wavelet-42 reduced it by 0.027388. Both deficits occurred in all five identity-disjoint folds.

Accordingly, the whole-representation evidence supports the bounded conclusion:

\[
\boxed{
\text{heterogeneous encoding preserves near-full retrieval at reduced dimension}
}
\]

while avoiding the larger losses observed for the tested uniformly applied compact DCT and wavelet transforms.

The competitive uniform \(\mathrm{RAW}_{42}\) baseline must remain visible because it prevents the contribution from being overstated as descriptor superiority.

---

## 5.8 Nonlinear pairwise structure and nonlinear-model utility are different scientific questions

The latent analysis illustrates a second methodological principle: detectable nonlinear predictive structure does not automatically justify a nonlinear latent model.

At matched latent dimensions, the tested AE and VAE representations did not establish a multiplicity-controlled held-out garment-identity retrieval advantage over PCA. This comparison is conditional on the hybrid representation already selected by the preceding cross-validated band analysis; it is not an untouched end-to-end validation of representation selection followed by latent-model selection.

The strongest observed nonlinear contrast was

\[
\mathrm{VAE}_{16}
-
\mathrm{PCA}_{16},
\]

with mean

\[
\Delta\mathrm{MRR}
=
+0.014341,
\]

but its max-statistic adjusted fold-level probability was

\[
p=0.2500.
\]

PCA was therefore retained as the practical latent baseline within the frozen hybrid representation because the downstream comparison did not provide sufficient evidence to replace it.

That decision does not imply that every relationship in the representation is linear. A separate held-out audit found one FWER-supported quadratic PCA-coordinate relation, with best mean improvement

\[
\overline{\Delta R^2}
=
+0.432042.
\]

The appropriate interpretation is pairwise nonlinear predictability. This result is not, by itself, evidence of differential-geometric manifold curvature; category structure or other mixture effects may also generate nonlinear coordinate relationships.

The neighborhood dimensionality calculation is retained only as a scale-conditioned descriptive diagnostic. At 20 neighbours, the identity-level median number of directions required for 90% within-neighborhood variance was 15, but a centered 20-neighbour matrix has rank at most 19 by construction. The value therefore cannot support a quantitative comparison with the global PCA dimension or an intrinsic-dimensionality claim.

These results are compatible rather than contradictory:

\[
\boxed{
\text{nonlinear pairwise structure}
\neq
\text{validated nonlinear-model utility}.
}
\]

PCA should therefore be understood here as a practical validated basis, not as a claim about the fundamental geometry of garment morphology.

---

## 5.9 Exact latent-to-Fourier mapping provides mathematical traceability

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

The selected examples illustrate that different latent directions occupy different regions of the morphology field. PC1 and PC3 were strongly outer-radial, whereas PC15 was predominantly inner-radial. Their maximum-energy harmonic coordinates also differed.

This form of interpretability is mathematical rather than semantic. It establishes where a latent perturbation acts in the representation; it does not establish what garment attribute that perturbation means.

---

## 5.10 Retained-subspace localization is informative only with its denominator and claim boundary intact

The first 64 principal components accounted for 44.65% of variance in the standardized frozen representation. All subsequent radial-harmonic localization therefore applies only to that retained PCA-64 subspace.

Within this subspace, 78.54% of variance-weighted mapped morphology energy occurred at intermediate harmonic orders \(k=5{:}24\), 66.84% occurred in the outer radial zone \(r=49{:}72\), and 51.30% occurred jointly in the outer-radial × intermediate-harmonic region.

These numbers describe how variation represented by PCA-64 is localized after exact inverse mapping. They are not percentages of total garment morphology, not percentages of the complete 3008-dimensional representation, and not estimates of semantic garment-part contribution.

The radial coordinates themselves also remain morphological rather than semantic. In particular,

\[
\boxed{
\text{outer radial}
\neq
\text{garment boundary}.
}
\]

The radial zones are partitions of representation space, not annotated regions such as hem, sleeve, neckline, waist, or silhouette edge. Harmonic order and PCA index are mathematical coordinates rather than garment attributes.

The 51.30% joint outer-radial × intermediate-harmonic quantity is also descriptive. No radial-zone-by-harmonic-band interaction or independence hypothesis was tested, so the observation should not be described as enrichment, synergy, coupling, or interaction.

These boundaries define the type of interpretability supplied by the present framework: explicit spatial-spectral localization with a verifiable denominator, without semantic labels that the data do not contain.

---

## 5.11 Limitations and generalizability

Several limitations determine how broadly these findings can be interpreted.

First, the empirical results are currently specific to CLO-SKET. Independent garment-sketch datasets are required before either the support-dependence effect size or the selected DCT/raw/raw/wavelet pattern can be treated as a general property of fashion-sketch morphology.

Second, the support intervention isolates one factor: surrounding raster support under a same-pixel construction. It does not reproduce every consequence of natural cropping. Natural crop operations may also alter border context, support occupancy, threshold interactions, or other image properties. Therefore 05K demonstrates a genuine representation dependency but not a complete causal decomposition of RAW-to-CROP preprocessing.

Third, individual support trajectories were not universally monotonic. The category-level endpoint response was broad and inferentially supported, but only approximately half of the images were fully monotonic for the low band and fewer were monotonic for the high-middle and high bands. The paper therefore supports a population-level endpoint effect, not a deterministic per-image support law.

Fourth, exact invariance of the object-relative comparator under the same-pixel intervention establishes that the tested support dependency can be removed by that matched construction. It does not establish universal superiority for retrieval, classification, semantic interpretability, robustness to all transformations, or other downstream tasks.

Fifth, radial-representation selection is conditional on the candidate family, coefficient budgets, objective, validation statistic, \(Q_c=0.95\) training-retention threshold, and prespecified harmonic-band boundaries tested here. The \(0.95\) value is a design admissibility threshold rather than a statistically calibrated non-inferiority margin. The lack of support for compression at \(k=5{:}24\) therefore does not imply that no compact representation exists for those ranges.

Sixth, the nonlinear-model conclusion is model-conditional. It applies to the tested PCA, AE, and VAE configurations, latent dimensions, dataset size, and five-fold outer validation design. The result supports retention of PCA under the present evidence rather than a general rejection of nonlinear latent modeling.

Seventh, the neighborhood dimensionality diagnostic is scale- and sample-size-dependent and is not interpreted as intrinsic dimension.

Finally, the PCA localization analysis is limited by its 44.65% retained-variance denominator and by the absence of independent semantic or spatial garment annotations. The current study can localize variation mathematically but cannot determine whether particular radial-harmonic patterns correspond reproducibly to named garment features.

The literature boundary also remains qualified. The reviewed literature establishes extensive prior work on Fourier shape descriptors, polar/radial-angular representations, scale normalization, digital invariance, finite-window effects, zero-padding, and crop sensitivity. We did not identify a direct precedent matching the complete 05K intervention, but this does not establish absolute historical priority.

---

## 5.12 Implications and future work

The broader methodological implication is that two separate design questions should be answered in order:

\[
\boxed{
\text{Is the measurement system stable to irrelevant observation-frame changes?}
}
\]

and then

\[
\boxed{
\text{How much representation complexity is justified within that measurement system?}
}
\]

This yields a stronger general workflow:

\[
\boxed{
\text{define structured representation}
\rightarrow
\text{audit representation validity}
\rightarrow
\text{select subdomain complexity with held-out evidence}
\rightarrow
\text{preserve unsupported structure}
\rightarrow
\text{interpret through an exact inverse map}.
}
\]

For Paper II itself, the immediate implication is not to retroactively replace the historical raster-relative hybrid. The original band-selection result remains a valid result of the historical analysis, conditional on its coordinate system. The support audit instead identifies a design requirement for future versions of the representation: object-relative coordinate definitions should be evaluated prospectively before repeating band-specific selection.

A future study could therefore repeat the entire representation-selection pipeline under an object-relative radial construction rather than merely using the intrinsic field as a control. The 05H2 audit showed that the pattern of band-wise compression support differs under the tested object-relative construction and therefore should not be used as a retrospective substitute for the historical hybrid. That observation should motivate a new prespecified experiment, not a retrospective substitution into the present manuscript.

A second priority is external replication of the support-dependence effect and the harmonic-dependent representation-selection pattern on an independent garment-sketch dataset.

A third priority is semantic validation. Spatial annotations or garment-attribute labels would allow direct tests of whether particular radial-harmonic localization patterns correspond reproducibly to sleeves, neckline structure, waist shape, hem geometry, silhouette, or other interpretable garment properties.

A fourth direction follows from the exact inverse mapping. Controlled perturbations localized to selected \((r,k)\) regions could be reconstructed and evaluated to determine whether they produce reproducible geometric changes. Such experiments would move the framework from descriptive localization toward experimentally testable morphology control and would constitute a new study rather than evidence already established here.

---

## 5.13 Scientific interpretation

After reconciliation with the support-dependence audit, the scientific identity of Paper II is broader than representation compression alone.

The paper first shows that a structured morphology representation must be audited for dependence on the observation frame before its internal spectral allocation is interpreted. Under the historical raster-relative construction, surrounding raster support was a demonstrated dependency of angular spectral allocation under a controlled same-pixel intervention. A matched object-relative construction was numerically invariant under that same support intervention.

The paper then shows that, within the historical representation in which the original analysis was conducted, radial representation complexity did not receive uniform empirical support across angular harmonic scale. Compact radial encodings were supported for the lowest and highest tested harmonic bands, whereas full radial structure was preserved in the intermediate ranges because the tested compression alternatives did not receive sufficient support.

At the latent level, greater model complexity likewise had to earn empirical support. The tested nonlinear encoders did not establish a multiplicity-controlled task advantage over PCA, even though a separate audit detected nonlinear pairwise predictability.

Finally, exact inverse mapping retained traceability from latent coordinates back to radial-harmonic morphology. Within the PCA-64 subspace, mapped variation showed strong intermediate-harmonic and outer-radial organization while individual components remained heterogeneous.

The reconciled scientific identity is therefore:

\[
\boxed{
\text{validate the measurement frame;}
\newline
\text{allocate representation complexity only where evidence supports it;}
\newline
\text{preserve unsupported structure;}
\newline
\text{and keep retained latent variation traceable to explicit morphology coordinates.}
}
\]

The contribution is not a new spectral transform or normalization scheme. It is a combination of **measurement-validity auditing**, **evidence-controlled representation allocation**, and **mathematically traceable latent interpretation**.
