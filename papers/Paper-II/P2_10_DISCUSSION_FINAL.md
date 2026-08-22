# CLO-SKET Paper 2 — Final Discussion

## Status

**FINAL DISCUSSION ASSEMBLY: READY FOR MANUSCRIPT INTEGRATION**

This Discussion interprets only the frozen Paper 2 evidence.

The central scientific question is not whether one transform is universally superior.

It is:

\[
\boxed{
\text{Does radial representation requirement depend on angular harmonic scale?}
}
\]

The results support that conclusion within the present CLO-SKET framework.

---

# 5. Discussion

## 5.1 Radial representation requirements depend on angular harmonic scale

The principal finding of this study is that radial representation could not be treated uniformly across angular harmonic order.

When the radial functions

\[
F_k(r)
\]

were evaluated separately across four harmonic ranges, compact representations were supported at the low and highest tested harmonic bands, whereas the tested compression of the two intermediate ranges was not supported under garment-identity-disjoint, family-wise-error-rate-controlled inference.

The resulting representation was therefore heterogeneous:

\[
\boxed{
\mathrm{DCT}_4
/
\mathrm{RAW}_{72}
/
\mathrm{RAW}_{72}
/
\mathrm{db4}_4
}.
\]

This result is important because a conventional dimensionality-reduction strategy could instead impose a common radial basis or common coefficient budget across all harmonic orders.

The present evidence does not support such uniform treatment.

Rather, the amount and form of radial structure that can be compactly represented under the tested task criterion depend on angular harmonic scale.

---

## 5.2 Unsupported compression is itself informative

The intermediate harmonic results are central to this conclusion.

For

\[
k=5{:}12
\]

and

\[
k=13{:}24,
\]

the tested compact radial representations did not survive the simultaneous inferential criterion.

The appropriate response was therefore not to force a compact representation, but to preserve the complete 72-shell radial functions.

This distinction separates evidence-guided compression from compression imposed primarily to achieve a target dimensionality.

In the present framework,

\[
\boxed{
\text{absence of compression support}
\Rightarrow
\text{preservation}
}
\]

rather than

\[
\text{absence of compression support}
\Rightarrow
\text{search until some compression succeeds}.
\]

The negative results therefore contribute directly to the architecture of the final representation.

They identify portions of the radial-harmonic field for which the tested compact encodings could not be justified under the frozen validation criterion.

Importantly, this does not establish that the intermediate bands are mathematically incompressible.

It establishes only that the tested compression strategies were not sufficiently supported to justify replacing their full radial structure.

---

## 5.3 The results argue against a simple low-frequency signal / high-frequency noise hierarchy

A tempting interpretation of Fourier morphology is to regard low angular frequencies as meaningful global shape and progressively higher frequencies as increasingly irrelevant detail or noise.

The present results do not support that simple hierarchy.

The highest tested harmonic band,

\[
k=25{:}36,
\]

supported compact radial representation using a localized wavelet basis, while both intermediate ranges retained their full radial structure.

Moreover, within the retained PCA-64 subspace, most variance-weighted mapped morphology energy occurred at the intermediate harmonic orders

\[
k=5{:}24.
\]

Thus, the spectral organization observed here cannot be summarized as a monotonic transition from useful low-frequency structure to disposable high-frequency content.

A more appropriate description is that different angular scales exhibit different forms of radial organization.

---

## 5.4 Different radial bases may capture different forms of radial organization

The type of compact representation supported at the two ends of the harmonic range also differed.

For

\[
k=1{:}4,
\]

four DCT coefficients were sufficient under the frozen inferential criterion.

A compact DCT representation is consistent with radial structure that can be represented efficiently using a small number of smooth global basis functions.

At

\[
k=25{:}36,
\]

the supported compact representation instead used four db4-wavelet coefficients.

Wavelet bases provide localized and multiscale radial support and can therefore represent radial structure differently from a global cosine basis.

This contrast is consistent with the possibility that the radial organization associated with low and high angular orders differs structurally.

However, this interpretation should remain cautious.

The present experiments establish comparative support for the tested representations.

They do not prove that low-frequency radial morphology is intrinsically globally smooth or that high-frequency morphology possesses a unique wavelet-generating mechanism.

Those hypotheses would require more direct structural tests.

---

## 5.5 The hybrid representation follows evidence rather than architectural symmetry

The final representation reduced the radial-harmonic field from

\[
2592
\]

to

\[
1504
\]

complex coefficients, corresponding to a coefficient reduction of approximately

\[
41.98\%.
\]

More important than the numerical reduction itself is how that reduction was obtained.

The final architecture is deliberately asymmetric.

It does not assign the same radial encoding to every harmonic range merely because such an architecture would be simpler to describe.

Instead,

\[
\boxed{
\text{compress where supported;
preserve where support is absent}.
}
\]

The resulting DCT/raw/raw/wavelet structure can therefore be understood as an evidence-selected representation rather than a uniformly engineered compression scheme.

The 41.98% value should consequently be interpreted as a reduction in coefficient count.

It is not an estimate of the amount of redundant information, noise, or irrelevant morphology removed from the sketches.

---

## 5.6 Nonlinear geometry and nonlinear model utility are different questions

A second finding of the study concerns the geometry of the resulting representation.

The geometric audits identified departures from a purely linear description.

However, the tested nonlinear latent models did not establish a multiplicity-controlled downstream task advantage over PCA.

These findings are not contradictory.

They address two different questions:

\[
\boxed{
\text{Is the geometry nonlinear?}
}
\]

and

\[
\boxed{
\text{Does a nonlinear latent model improve validated task performance?}
}
\]

The first can be true without the second.

Local curvature or nonlinear neighborhood structure does not guarantee that a nonlinear representation will improve generalization under a particular downstream task, dataset size, architecture, or validation design.

Conversely, failure of the tested nonlinear models to outperform PCA does not establish that the underlying morphology space is globally linear.

Maintaining this distinction avoids using either predictive performance or geometric visualization as a surrogate for the other.

---

## 5.7 Why PCA remained the practical latent representation

PCA was retained because the tested nonlinear alternatives did not establish a multiplicity-controlled task advantage sufficient to justify replacing it.

Its retention should therefore be interpreted pragmatically rather than ontologically.

PCA provides:

- a deterministic orthogonal coordinate system;
- direct variance ordering;
- stable inverse mapping through the frozen representation;
- straightforward perturbation analysis;
- a practical reference against which nonlinear alternatives can be evaluated.

These properties made PCA particularly useful for tracing latent variation back into

\[
F_k(r).
\]

The conclusion is therefore not:

\[
\boxed{
\text{garment morphology is linear}.
}
\]

It is:

\[
\boxed{
\text{PCA remained the validated practical latent basis under the present evaluation}.
}
\]

---

## 5.8 There was no evidence for one canonical nonlinear morphology trajectory

The nonlinear geometry analyses also constrained stronger manifold interpretations.

Although geometric departures from linearity were detectable, principal-curve analysis did not establish a stable one-dimensional trajectory.

The diffusion-map sensitivity analysis likewise did not provide sufficient evidence for replacing the frozen PCA representation with a unique diffusion coordinate system.

The present data therefore do not support describing CLO-SKET morphology as lying along one canonical nonlinear trajectory.

This is an important negative result.

Complex morphology spaces can contain nonlinear local geometry without being reducible to a single stable curve or uniquely preferred low-dimensional manifold.

Accordingly, the geometric evidence is better interpreted as:

\[
\boxed{
\text{nonlinear local structure}
}
\]

rather than:

\[
\boxed{
\text{one discovered garment-morphology manifold}.
}
\]

---

## 5.9 Exact inverse mapping makes the latent representation interpretable in the original spectral coordinates

A major advantage of retaining a mathematically explicit latent representation is that PCA directions can be mapped back through the exact frozen representation.

For component \(j\), the one-score-standard-deviation perturbation

\[
\Delta x_j
\]

was reconstructed as

\[
\Delta F_j(r,k),
\]

allowing each latent direction to be examined directly in radial-harmonic coordinates.

Because PCA eigenvector sign is arbitrary, interpretation used

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2,
\]

which is invariant to sign reversal.

This provides a direct bridge between latent variation and the original spectral representation:

\[
\boxed{
PC_j
\rightarrow
\Delta F_j(r,k)
\rightarrow
E_j(r,k).
}
\]

The latent representation therefore remains mathematically traceable to the radial-angular morphology from which it was constructed.

---

## 5.10 Retained latent variation was dominated by intermediate harmonic structure

Within the retained PCA-64 subspace, the majority of variance-weighted mapped morphology energy occurred at

\[
k=5{:}24.
\]

This observation is especially informative when considered alongside the compression inference.

The same broad intermediate harmonic range for which compact radial representation was not supported also contained most of the mapped morphology energy represented within PCA-64.

These findings are conceptually compatible with an important role for radially resolved intermediate-harmonic structure in the retained latent variation.

However, the two results should not be collapsed into a causal argument.

The compression analysis and PCA localization answer different questions:

\[
\text{compression analysis}
\rightarrow
\text{whether tested radial reduction is supported}
\]

whereas

\[
\text{PCA localization}
\rightarrow
\text{where retained latent perturbation energy is located}.
\]

The present analysis does not establish that the intermediate bands resisted compression *because* they contained 78.54% of retained mapped morphology energy.

That would require a separate formal test.

---

## 5.11 Radial position is an important coordinate of retained latent variation

The retained PCA morphology was also strongly radially organized.

Approximately two-thirds of the variance-weighted mapped morphology energy within PCA-64 occurred in the outer radial zone.

Furthermore, more than half occurred jointly within outer radial positions and intermediate harmonic orders.

This demonstrates that the retained latent variation is not spatially homogeneous with respect to radius.

However,

\[
\boxed{
\text{outer radial}
\neq
\text{garment boundary}.
}
\]

The radial zones are defined in representation space and were not annotated using garment-part semantics.

An outer-radial spectral perturbation could reflect multiple aspects of sketch geometry.

Without independent spatial annotation, it cannot automatically be labeled as sleeve, hem, silhouette, contour, or another garment component.

---

## 5.12 Joint localization should not be interpreted as a radial-harmonic interaction

The concentration of retained morphology energy within the outer-radial × intermediate-harmonic region is a joint descriptive quantity.

The marginal concentrations were themselves substantial.

Therefore the observed joint value should not be interpreted as demonstrating enrichment or statistical interaction between radial zone and harmonic range.

No formal independence or interaction hypothesis was tested.

The scientifically appropriate statement is therefore:

> retained PCA morphology showed substantial joint localization in outer radial positions and intermediate harmonic orders.

This distinction prevents a descriptive localization statistic from acquiring an inferential meaning it was not designed to carry.

---

## 5.13 The representation remains morphological rather than semantic

The present framework characterizes how sketch variation is organized mathematically.

It does not establish semantic correspondence between individual spectral or latent coordinates and garment concepts.

Neither

\[
k
\]

nor

\[
r
\]

nor

\[
PC_j
\]

should automatically be interpreted as a garment attribute.

For example, the present analysis does not establish axes corresponding specifically to:

- sleeve structure;
- neckline;
- waist;
- hem;
- drape;
- fit;
- style.

Establishing such correspondence requires independent semantic labels, spatial annotations, or controlled perturbation experiments.

This distinction is especially important for downstream use in generative fashion systems, where mathematical controllability and semantic controllability are not equivalent.

---

# 5.14 Limitations

## 5.14.1 Dataset scope

The current findings were established within CLO-SKET.

Although garment identities and categories were explicitly incorporated into the validation design, external replication on independent sketch datasets is required before the observed harmonic-dependent representation pattern can be treated as a general property of garment sketches.

---

## 5.14.2 Candidate representation space

The compression conclusions are conditional on the candidate representations evaluated.

Failure to support compression in the intermediate bands does not prove that no compact representation exists.

Alternative transforms, learned bases, adaptive dictionaries, or larger coefficient budgets could yield different results.

The correct conclusion is therefore:

\[
\boxed{
\text{tested compression was not supported}
}
\]

rather than:

\[
\boxed{
\text{compression is impossible}.
}
\]

---

## 5.14.3 PCA-64 is a partial representation

The first 64 components accounted for

\[
44.65\%
\]

of standardized representation variance.

Consequently, the morphology-localization analysis describes only the retained PCA-64 subspace.

The reported localization percentages cannot be interpreted as percentages of total garment morphology or even as a complete decomposition of the original 3008-dimensional representation.

---

## 5.14.4 Radial zones lack semantic annotation

The inner, middle, and outer zones were equal-shell descriptive partitions.

They were not derived from anatomical or garment-component annotations.

Future work should test whether reproducible relationships exist between radial spectral structure and independently annotated garment regions.

---

## 5.14.5 PCA axes lack semantic labels

The principal components are mathematical directions of variation.

No one-to-one correspondence between individual PCs and semantic garment properties was established.

Future semantic interpretation requires external attributes or controlled morphology interventions.

---

## 5.14.6 Nonlinear negative results are method-conditional

The absence of validated superiority among the tested nonlinear models applies only to:

- the methods evaluated;
- their frozen hyperparameter ranges;
- the present dataset;
- the current validation framework;
- the current downstream objective.

It should not be interpreted as a general rejection of nonlinear latent modeling.

---

## 5.14.7 Task-oriented compression is not universal compression

Representation selection was performed according to the frozen task-oriented validation criterion.

A representation optimized for another objective—such as reconstruction, retrieval, semantic prediction, or generation—could favor a different radial encoding.

The resulting hybrid representation should therefore be understood as evidence-supported under the present evaluation framework rather than universally optimal.

---

# 5.15 Future directions

The present framework suggests several targeted extensions.

First, the harmonic-dependent compression pattern should be tested on independent garment-sketch datasets to determine whether the DCT/raw/raw/wavelet structure replicates beyond CLO-SKET.

Second, semantic and spatial annotations could be introduced to determine whether radial-harmonic localization corresponds reproducibly to garment components or attributes.

Third, the candidate radial representation family could be expanded while preserving the same inferential selection principle.

This would test whether the intermediate harmonic bands remain resistant to compact representation under richer basis families.

Fourth, larger datasets could provide a stronger test of nonlinear latent models and nonlinear geometry.

The present negative nonlinear results should therefore be viewed as a benchmark against which future representations can be evaluated rather than as a terminal conclusion.

Finally, the exact mapping

\[
PC_j
\rightarrow
\Delta F_j(r,k)
\]

provides a foundation for controlled morphology experiments.

Future work could test whether deliberate perturbations in selected radial-harmonic regions produce predictable and semantically meaningful changes in reconstructed or generated garment sketches.

Such experiments would move the framework from descriptive morphology interpretation toward validated morphology control.

---

# 5.16 Scientific interpretation

Taken together, the results support a representation of garment-sketch morphology in which radial organization depends on angular harmonic scale.

The evidence does not support a uniform radial compression rule across the complete Fourier field.

Instead, the final representation preserves full radial structure where compact encoding was not supported and applies compact bases only where the inferential evidence justified them.

The resulting latent representation additionally shows that nonlinear geometric structure can coexist with the absence of a validated nonlinear-model advantage.

PCA therefore remains useful as a practical and mathematically traceable latent basis without requiring an assumption of globally linear morphology.

Finally, mapping PCA perturbations back into radial-harmonic coordinates shows that variation within the retained PCA-64 subspace is strongly structured across both angular harmonic order and radial position.

Together, these findings motivate treating garment-sketch morphology as a structured radial-angular spectral field rather than as a globally compressed Fourier descriptor or a single canonical latent manifold.

---

# Discussion logic

\[
\boxed{
\text{compression differs across }k
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{radial redundancy is scale dependent}
}
\]

but not:

\[
\text{low = signal,\ high = noise}.
\]

---

\[
\boxed{
\text{intermediate compression unsupported}
}
\]

\[
+
\]

\[
\boxed{
\text{intermediate PCA localization dominant}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{intermediate radial-harmonic structure is important within the retained representation}
}
\]

but not:

\[
\text{one result causes the other}.
\]

---

\[
\boxed{
\text{nonlinear geometry detectable}
}
\]

\[
+
\]

\[
\boxed{
\text{nonlinear task advantage not established}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{geometry}
\neq
\text{model utility}.
}
\]

---

\[
\boxed{
66.84\%\ \text{outer}
}
\]

does not imply:

\[
\boxed{
\text{outer}=\text{garment boundary}.
}
\]

---

\[
\boxed{
51.30\%\ \text{outer}\times\text{intermediate}
}
\]

means:

\[
\boxed{
\text{joint localization}
}
\]

not:

\[
\boxed{
\text{statistical interaction}.
}
\]

---

# Discussion claim lock

## We can say

> Radial representation requirements differed across angular harmonic scale under the present validation framework.

> The evidence-supported representation was heterogeneous rather than uniformly compressed.

> Intermediate harmonic ranges retained substantial radially resolved structure under the tested criterion.

> Detectable nonlinear geometry did not translate into a validated nonlinear-model advantage.

> PCA provided a stable and interpretable practical latent basis.

> Retained PCA morphology exhibited structured radial-harmonic localization.

---

## We cannot say

> We discovered the universal spectral structure of garment morphology.

> Intermediate harmonics cannot be compressed.

> High harmonics are noise.

> DCT represents global garment shape.

> Wavelets represent garment details.

> Outer radial energy represents silhouette.

> PCA components correspond to garment attributes.

> PCA explains 44.65% of total garment morphology.

> CLO-SKET lies on one nonlinear manifold.

> Nonlinear methods do not work for garment morphology.

---

# Step 10 lock

\[
\boxed{
\textbf{PAPER 2 FINAL DISCUSSION — ASSEMBLED}
}
\]

The scientific core is now:

\[
\boxed{
\text{METHODS}
\rightarrow
\text{RESULTS}
\rightarrow
\text{DISCUSSION}
}
\]

with one continuous evidence chain.

Next:

\[
\boxed{
\textbf{STEP 11 — INTRODUCTION + RELATED WORK}
}
\]

This step is different.

Unlike Methods, Results, and Discussion, it cannot safely be assembled only from our notebook evidence.

It requires the verified literature/novelty audit so that we position the contribution against prior Fourier descriptors, polar/angular-radial representations, wavelet-Fourier methods, and morphology representations without accidentally making a false priority claim.