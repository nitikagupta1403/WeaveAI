# CLO-SKET Paper 2 — Reconciled Introduction and Related Work v1.1

## Status

**FREEZE-READY INTRODUCTION + RELATED WORK v1.1 — RECONCILED WITH P2_13 v1.0**

This document preserves the citation-integrated structure of the current Paper-II introduction and related work while revising the manuscript spine to reflect the completed 05F–05K representation-validity audit.

The governing order is:

\[
\boxed{
\text{representation validity}
\rightarrow
\text{representation allocation}
\rightarrow
\text{latent interpretation}
}
\]

No historical numerical result or frozen representation-selection decision is altered here.

---

# 1. Introduction

Representing garment sketches computationally requires more than choosing a descriptor. It requires deciding which observed structure belongs to the garment itself and which may depend on the coordinate frame in which the garment is measured.

This distinction becomes important in radial-angular spectral representations. Once sketch morphology is expressed as a conditional angular distribution

\[
P(\theta\mid r),
\]

angular organization can be decomposed into harmonic morphology functions

\[
F_k(r).
\]

The harmonic index \(k\) distinguishes angular scale, while the radial coordinate \(r\) retains where that angular structure occurs. The result is an explicit two-coordinate morphology field rather than an undifferentiated image embedding.

Fourier descriptors, polar coordinate systems, radial-angular basis functions, object centering, and scale normalization are all established ideas in shape analysis. The present study therefore does not ask whether spectral or polar representations can describe shape.

It asks two ordered questions.

First:

> **When garment morphology is encoded in raster-relative radial-angular coordinates, does changing only the surrounding raster support alter angular spectral allocation even when garment pixels are unchanged?**

Second:

> **Given the radial-angular Fourier field, should radial representation be imposed uniformly across angular harmonic orders, or selected conditionally on harmonic scale using held-out evidence?**

The ordering matters. A representation should be audited as a measurement system before its internal spectral allocation is optimized or interpreted.

The historical CLO-SKET representation normalized radial coordinates relative to the complete raster grid. This creates a potential coupling between garment geometry and the observation frame: if the raster support changes, the normalized radial coordinate assigned to an otherwise unchanged garment can also change.

To test whether this dependence was practically consequential, we performed a staged representation-validity audit. The historical preprocessing chain was first decomposed to localize where the previously observed spectral change entered. Candidate frame-related descriptors were then examined at image level and population level. Finally, a controlled same-pixel intervention enlarged only the surrounding raster support while preserving the garment rectangle exactly and prohibiting resize, interpolation, antialiasing, rethresholding, or crop recomputation.

A matched object-relative construction was evaluated under the same intervention. Its role was not to introduce a new normalization method, but to provide a counterfactual measurement system in which coordinates were defined relative to the object rather than to the surrounding raster frame.

This validity audit changes the hierarchy of the manuscript, but not the frozen historical analysis.

The original representation-selection question remains important. A common response to high-dimensional spectral representations is to impose a single compression family or coefficient budget globally. That assumes radial information has comparable representational requirements across the angular spectrum. The opposite strategy—retaining every radial coefficient—avoids this assumption but preserves potentially unnecessary dimensionality.

Neither strategy asks whether compression is actually supported in a particular spectral regime.

We therefore formulate representation construction as an **evidence-controlled selection problem**. Candidate radial representations are evaluated separately within prespecified harmonic bands. Compact encoding is retained only when its held-out effect survives garment-identity-disjoint validation and multiplicity control; where such support is absent, complete radial structure is preserved.

Thus:

\[
\boxed{
\text{compress where supported; preserve otherwise.}
}
\]

This principle yields a heterogeneous representation

\[
\mathcal H
=
\bigoplus_b
\mathcal R_b
\left(
F_k(r)
\right),
\]

where the radial operator \(\mathcal R_b\) may differ across harmonic bands.

A third question arises after this radial-spectral structure has been frozen. High-dimensional morphology can contain nonlinear predictive relationships, but detectable nonlinearity does not itself establish that a nonlinear encoder offers better held-out utility. Autoencoders and variational autoencoders provide nonlinear latent mappings, whereas PCA supplies a simpler linear basis with an exact inverse path.

We therefore distinguish:

\[
\text{Is nonlinear predictive structure detectable?}
\]

from

\[
\text{Does a nonlinear latent model provide validated task advantage?}
\]

Conditional on the historical hybrid representation, AE and VAE alternatives are compared directly with same-dimensional PCA representations under identity-disjoint validation and multiplicity-controlled inference. Nonlinear predictive structure is then audited separately so that evidence of a quadratic coordinate relation cannot retrospectively determine the model-selection decision.

A final requirement is traceability. Compact latent coordinates are useful only if their relation to the structured morphology can remain explicit. Because the hybrid representation retains an exact inverse path, a perturbation along PCA direction \(j\) can be mapped back to the Fourier morphology field,

\[
PC_j
\longrightarrow
\Delta F_j(r,k),
\]

and localized through the sign-invariant energy

\[
E_j(r,k)
=
\left|
\Delta F_j(r,k)
\right|^2.
\]

This provides mathematical localization rather than semantic disentanglement. A concentration of latent energy in a radial zone or harmonic range does not by itself identify a sleeve, hem, neckline, silhouette, or other garment concept.

We study these questions using CLO-SKET (Arnia, 2020), a controlled garment-sketch corpus containing 2,300 sketches representing 230 garment identities across 23 garment categories. The repeated-identity structure enables all main validation procedures to separate complete garment identities between training and held-out groups.

The study makes three main methodological contributions.

1. **Controlled representation-validity audit.**  
   We test whether surrounding raster support alone can change angular spectral allocation under the historical raster-relative coordinate system while garment pixels are held fixed, and we compare this response with a matched object-relative control.

2. **Harmonic-conditioned, evidence-controlled radial representation selection.**  
   We test radial compression separately across angular harmonic regimes and construct a heterogeneous representation in which compact bases are retained only where inferential support is established, while complete radial structure is preserved elsewhere.

3. **Exact latent-to-morphology traceability.**  
   We map retained PCA directions through the inverse hybrid representation into explicit radial-harmonic morphology fields without assigning unsupported semantic meaning.

The same evidential discipline is applied separately to latent-model complexity: PCA is compared with AE and VAE alternatives under identity-disjoint validation, while nonlinear predictive structure is audited independently so that evidence of nonlinearity does not retrospectively determine model selection.

The resulting experiments establish a layered result.

Under the historical raster-relative coordinate system, surrounding raster support is a demonstrated dependency of angular spectral allocation in the tested same-pixel intervention. The matched object-relative construction remains numerically invariant under that intervention.

Within the historical representation in which the original analysis was performed, support for radial compression is not uniform across angular harmonic scale. Compact radial encodings are supported at the lowest and highest tested harmonic ranges, whereas complete radial structure is retained across the intermediate orders.

Nonlinear encoders subsequently do not establish a multiplicity-controlled task advantage over same-dimensional PCA despite separately detectable nonlinear predictive structure.

Finally, inverse mapping of retained PCA variation reveals structured but heterogeneous radial-harmonic localization.

The contribution is therefore **not** a new Fourier transform, polar coordinate system, normalization scheme, DCT, wavelet family, PCA method, or nonlinear latent model.

It is a study of:

\[
\boxed{
\text{representation validity}
+
\text{evidence-controlled representation allocation}
+
\text{traceable latent interpretation}.
}
\]

---

# 2. Related Work

## 2.1 Classical Fourier shape description and contour normalization

Fourier representations have a long history in quantitative shape analysis. Classical contour formulations represented closed boundaries through Fourier coefficients, including early Fourier contour descriptors and elliptic Fourier descriptors (Zahn and Roskies, 1972; Kuhl and Giardina, 1982).

These methods established several ideas that remain relevant here:

- shape can be represented compactly in a spectral basis;
- translation, scale, rotation, starting point, and contour parameterization can be normalized or otherwise controlled;
- spectral coefficients can support reconstruction and shape comparison.

Accordingly, Fourier shape description itself is not novel in this study.

Likewise, modern work on complete elliptic Fourier descriptor normalization continues to refine normalization under basic contour transformations (Wu et al., 2026). Such work provides important precedent for shape normalization but does not constitute a direct precedent for the same-pixel raster-support intervention examined here.

The present study therefore does not claim to introduce object centering, scale normalization, or invariant Fourier shape description.

---

## 2.2 Polar, radial-angular, and region-based spectral descriptors

Region-based polar methods retain spatial organization beyond a single contour sequence.

The Generic Fourier Descriptor applies a two-dimensional Fourier transform to a polar-raster representation of a shape, incorporating radial and angular frequency information within a common descriptor (Zhang and Lu, 2002).

The Angular Radial Transform similarly represents shape using radial and angular basis functions and has been used in MPEG-7 region-shape description and later extensions (Ricard et al., 2005).

Polar Harmonic Transforms provide further precedent for orthogonal bases defined directly in polar coordinates (Yap et al., 2010).

These studies establish that:

\[
\boxed{
\text{polar coordinates and radial-angular spectral analysis are prior art}.
}
\]

CLO-SKET uses a different decomposition for a different question. Angular morphology is normalized conditionally within each radial shell,

\[
P_i(\theta\mid r),
\]

and Fourier analysis over \(\theta\) produces an explicit complex radial function for each harmonic,

\[
F_{i,k}(r).
\]

The radial coordinate is therefore retained as an object of later representation analysis rather than immediately absorbed into a fixed two-dimensional transform basis.

This explicit radial dependence permits a separate question:

> Should the radial function attached to every angular harmonic be represented in the same way?

That representation-allocation question is distinct from introducing radial-angular spectral coordinates themselves.

---

## 2.3 Scale normalization, digital invariance, and implementation limits

Classical normalization theory often defines representations intended to be invariant to translation, scale, or rotation.

Digital implementation introduces additional complications. Discretization, rasterization, sampling density, boundary placement, interpolation, and noise can prevent mathematically intended invariance from being realized exactly in a sampled image representation.

Zernike-moment normalization studies provide a useful example: the mathematical normalization objective and its digital realization are not identical, because finite rasterization and discretization introduce implementation error (Yang and Fang, 2010).

This distinction is directly relevant to Paper II.

The present support audit is not motivated by the claim that shape normalization is new. It is motivated by the need to test whether the particular historical raster-relative coordinate system used by CLO-SKET is stable when an irrelevant part of the observation frame—surrounding blank support—is changed independently of garment pixels.

The matched object-relative construction therefore functions as a control, not as a new normalization invention.

---

## 2.4 Finite support, windows, cropping, and zero-padding

Fourier analysis of finite signals has long recognized that observed spectral structure depends on how a signal is windowed and sampled (Harris, 1978).

Finite-window theory is therefore general prior art, and image preprocessing/corruption has also been studied in relation to Fourier-domain behavior (Dzanic, Shah, and Witherden, 2020).

Cropping is also known to alter image statistics and can leave detectable signatures in image distributions (Van Hoorick and Vondrick, 2021). However, ordinary cropping changes the observed image content or context and often changes the rasterized object support itself.

Similarly, ordinary Fourier zero-padding is a standard signal-processing operation. In one-dimensional boundary-descriptor work, zero-padding can change sequence length and spectral sampling density without constituting a new shape-normalization principle (Kunttu, Kunttu, and Visa, 2005).

These precedents are important because they define what 05K is **not**.

05K is not presented as a discovery that:

- zero-padding creates spectral information;
- finite windows matter in Fourier analysis;
- image cropping can affect spectra;
- scaling can alter rasterized descriptors.

The specific experimental question is narrower:

> If a bit-identical garment patch is embedded in progressively larger two-dimensional raster support, with no resize, interpolation, antialiasing, contour retracing, rethresholding, or crop recomputation, does the historical raster-relative radial-angular representation systematically reassign spectral allocation across the frozen angular bands?

The observed effect is interpreted through coordinate remapping relative to raster support, not through the claim that padding itself creates garment frequencies.

---

## 2.5 Same-pixel raster-support manipulation: precedent boundary

The literature reviewed for this project contains strong adjacent precedents but no direct match to the complete controlled intervention.

The relevant precedent classes can be summarized as follows.

| Literature family | Core contribution | Relation to 05K |
|---|---|---|
| Classical Fourier / EFD shape descriptors | spectral contour representation and normalization | general theory |
| GFD | polar-raster Fourier shape representation | close partial precedent |
| ART / MPEG-7 region shape | angular-radial region basis | close partial precedent |
| Zernike normalization studies | digital normalization accuracy and discretization limits | partial precedent |
| finite-window Fourier analysis | dependence on finite observation support | general theory |
| boundary-signal zero-padding | sequence-length / spectral-sampling change | different operation |
| image cropping studies | effects of crop/context change | partial but content-changing |
| 05K | bit-identical patch + independent 2-D support manipulation + no resampling + predefined band endpoints + population inference + matched object-relative control | current study |

The reviewed literature establishes that the mathematical ingredients are old.

The literature review did **not** identify a direct precedent combining all of the following:

\[
\text{bit-identical garment pixels}
\]

\[
+
\]

\[
\text{independent 2-D raster-support manipulation}
\]

\[
+
\]

\[
\text{no resize/interpolation}
\]

\[
+
\]

\[
\text{prespecified support dose}
\]

\[
+
\]

\[
\text{bandwise spectral redistribution}
\]

\[
+
\]

\[
\text{population-level inference}
\]

\[
+
\]

\[
\text{matched object-relative invariance control}.
\]

This is a literature-search boundary, not a proof of absolute priority.

The manuscript should therefore state:

> **We did not identify a direct precedent in the reviewed literature for this specific same-pixel support-dependence audit.**

It should not state:

> “No previous work has done this.”

---

## 2.6 Multiscale, wavelet, and compact spectral descriptors

Spectral shape descriptors have also been extended across scale.

Multiscale Fourier descriptors organize contour-based shape information across multiple resolutions (Kunttu et al., 2006). Fourier and wavelet operations have likewise been combined in fashion-flat analysis. Wavelet Fourier Descriptor pipelines therefore establish prior art for combining Fourier analysis with wavelet-based compact shape description, including direct fashion-flat classification work (An and Li, 2014).

Consequently:

\[
\boxed{
\text{Fourier + wavelet is not the Paper-II novelty}.
}
\]

The distinction in CLO-SKET concerns **how a basis and coefficient budget are accepted**.

DCT, wavelet, and complete radial representations are treated as candidate encodings rather than globally prescribed components. Candidate compression is evaluated separately within prespecified harmonic bands using training garment identities for selection and held-out identities for confirmation.

A compact representation is adopted only where the frozen inferential criterion supports replacement of the complete radial field.

If tested compression is not supported, the complete radial function is retained.

This preservation decision does not establish intrinsic incompressibility. It states only that the tested compact alternatives did not earn replacement under the specified candidate family, coefficient budgets, dataset, and validation criterion.

---

## 2.7 Garment sketches, retrieval, and learned visual representations

Garment and fashion sketches have been studied for classification, retrieval, design assistance, vectorization, and image synthesis.

Handcrafted spectral shape pipelines provide direct precedent for fashion-flat classification (An and Li, 2014).

More recent systems use learned image representations for cross-domain sketch-photo retrieval, zero-shot sketch-based image retrieval, abstraction-aware retrieval, noise-tolerant retrieval, and representation transfer (Lei et al., 2021; Li et al., 2022; Bhunia et al., 2022; Chaudhuri et al., 2023; Koley et al., 2024).

Other work focuses on extraction and vectorization of design elements from clothing imagery (Lee et al., 2024), while recent surveys place sketch-guided retrieval within the wider fashion-retrieval landscape (Islam et al., 2024).

These systems address important problems, but their primary question differs from the present study.

They generally ask how to:

- improve recognition;
- align sketch and photo domains;
- learn invariant visual features;
- recover design elements;
- support semantic retrieval;
- synthesize or vectorize garment representations.

The present study instead asks how to validate and allocate complexity within an explicit morphology field whose coordinates remain mathematically interpretable.

The unit of held-out generalization is also different. Garment identity, not category alone, is used as the main validation grouping unit. Repeated drawings of the same garment identity therefore permit evaluation of whether a representation preserves identity-specific morphology across sketch realizations and transfers to garment identities absent from fitting.

---

## 2.8 Linear latent representations, nonlinear encoders, and nonlinear geometry

After representation construction, latent dimensionality introduces another complexity decision.

PCA provides an orthogonal variance-ordered basis with a transparent linear inverse (Jolliffe and Cadima, 2016).

Autoencoders learn nonlinear mappings through reconstruction objectives (Hinton and Salakhutdinov, 2006), while variational autoencoders add a probabilistic latent-variable formulation (Kingma and Welling, 2014).

Principal curves, Isomap, diffusion maps, and other manifold-oriented methods provide separate tools for exploring nonlinear organization (Hastie and Stuetzle, 1989; Tenenbaum et al., 2000; Coifman and Lafon, 2006).

The presence of nonlinear structure, however, is logically distinct from evidence that a nonlinear encoder improves a held-out task.

CLO-SKET therefore separates:

\[
\text{nonlinear predictive structure}
\]

from

\[
\text{validated nonlinear-model advantage}.
\]

Conditional on the frozen historical hybrid, same-dimensional AE and VAE representations are compared with PCA using identity-disjoint held-out retrieval and multiplicity-controlled inference.

Fixed quadratic coordinate relationships and manifold-oriented analyses are treated separately as geometry diagnostics.

This separation prevents two opposite errors:

\[
\text{AE/VAE non-superiority}
\not\Rightarrow
\text{globally linear geometry}
\]

and

\[
\text{detectable nonlinear relation}
\not\Rightarrow
\text{nonlinear encoder required}.
\]

---

## 2.9 Traceability from latent coordinates back to morphology

Interpretability can mean semantic disentanglement, causal factor recovery, or simply mathematical traceability.

Paper II claims only the third.

For PCA direction \(j\),

\[
PC_j
\rightarrow
\Delta x_j
\rightarrow
\Delta F_j(r,k),
\]

and the mapped perturbation is summarized by

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

PCA reconstruction and Fourier-domain visualization themselves are not presented as new.

The methodological role of the inverse path is to preserve traceability after heterogeneous compression so that retained latent variation can still be localized in the same radial-harmonic coordinates used for representation decisions.

This is intentionally weaker than semantic disentanglement.

An energy concentration at an outer radial location or within a harmonic band is a mathematical localization statement. It is not evidence that a PCA direction corresponds to a hem, sleeve, neckline, silhouette, or other semantic garment component.

---

## 2.10 Position of the present study

The mathematical components used in Paper II have substantial precedent:

- Fourier contour descriptors;
- elliptic Fourier descriptors;
- polar-raster Fourier descriptors;
- Angular Radial Transform descriptors;
- Polar Harmonic Transforms;
- DCT and wavelet compression;
- object-centering and scale normalization;
- PCA;
- autoencoders;
- variational autoencoders;
- manifold-learning tools;
- fashion-sketch classification and retrieval.

The contribution therefore does not lie in inventing any one of these ingredients.

The study instead combines three levels of methodological control.

### Level 1 — representation validity

The historical raster-relative measurement system is subjected to a controlled same-pixel support intervention before its spectral allocation is interpreted as object structure.

### Level 2 — representation allocation

Within the historical representation, radial encoding is selected separately across angular harmonic bands using identity-disjoint, multiplicity-controlled validation.

### Level 3 — latent interpretation

Latent complexity is validated separately, and retained PCA variation is mapped exactly back to radial-harmonic coordinates.

The manuscript-safe contribution statement is:

> **Paper II combines a controlled representation-validity audit with evidence-controlled allocation of radial representation complexity across angular harmonic scale and exact latent-to-radial-harmonic traceability.**

The manuscript should not claim:

- a new Fourier transform;
- a new polar coordinate system;
- a new scale-normalization method;
- a universally support-invariant descriptor;
- a universally optimal harmonic partition;
- a general law of garment morphology;
- universal superiority of the heterogeneous descriptor;
- semantic meaning for radial zones or harmonic bands.

---

## 2.11 Contemporary computer-vision context and remaining gap

Recent sketch-based computer-vision work increasingly focuses on learned invariance, cross-domain retrieval, abstraction robustness, representation transfer, and semantic alignment.

These advances do not remove the gap addressed here because the scientific questions differ.

The contemporary learned-representation question is often:

> How can a model learn features that improve recognition, retrieval, transfer, or synthesis?

The present question is:

> Given an explicit morphology coordinate system, which observed structure is stable to irrelevant observation-frame changes, and where is dimensional simplification empirically justified?

This distinction is central.

A learned model can be highly effective without exposing whether its internal features change when blank raster support changes. Conversely, an explicit spectral descriptor can be mathematically interpretable while still embedding a coordinate dependency on the observation frame.

Paper II therefore contributes an audit-and-selection framework rather than a benchmark race against contemporary neural retrieval systems.

---

## 2.12 Final novelty boundary

The safest literature-level conclusion is:

\[
\boxed{
\text{normalization mathematics is established prior art;}
\quad
\text{the controlled audit design is the contribution.}
}
\]

The strongest literature-facing sentence is:

> **Among the reviewed literature, we did not identify a direct precedent that combines a bit-identical foreground patch, independent two-dimensional raster-support manipulation without resampling, prespecified support dose, bandwise spectral redistribution, population-level inference, and a matched object-relative invariance control.**

The strongest representation-selection sentence remains:

> **Within the historical radial-angular representation, radial encoding is selected separately across angular harmonic bands using garment-identity-disjoint, multiplicity-controlled evidence, compressing supported bands while preserving complete radial structure where compression is not supported.**

These two claims are complementary rather than competing.

The first concerns whether the measurement system itself depends on the observation frame.

The second concerns how representation complexity should be allocated once the historical measurement system is fixed.

Together they support the revised Paper-II scientific identity:

\[
\boxed{
\text{validate the representation;}
\rightarrow
\text{allocate complexity with evidence;}
\rightarrow
\text{interpret through explicit coordinates.}
}
\]


---

## Citation integration note

This reconciled file restores the principal inline citations already present in the frozen P2_11 literature layer and adds only the support-audit precedents explicitly carried by P2_13. The existing manuscript bibliography should be preserved during final integration, with the P2_13 support-audit references added where not already present.
