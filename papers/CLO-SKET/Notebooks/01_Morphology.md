# CLO-SKET — GRAMMAR DISCOVERY
## Source Ingestion Audit

### Status

# 🟢 SOURCE INGESTION PASSES

The grammar-discovery notebook begins from a clean and well-defined population:

\[
N = 2300
\]

Clo-Sket sketches distributed across:

\[
23 \text{ categories}
\]

with exactly:

\[
100 \text{ sketches/category}.
\]

The external 333-sketch dataset is explicitly excluded.

That is a good decision for this notebook because it keeps the grammar-discovery population internally homogeneous and prevents a second source domain from influencing the structure discovered in Clo-Sket.

---

# 1. Population Structure

The source inventory is perfectly balanced:

| Quantity | Value |
|---|---:|
| Total sketches | **2300** |
| Categories | **23** |
| Sketches per category | **100** |
| External dataset used | **No** |

Therefore:

\[
2300 = 23 \times 100.
\]

This gives the notebook an unusually clean category distribution.

There is no class-frequency imbalance at source ingestion.

---

# 2. What Has Been Established

This cell establishes only the source population.

Specifically:

\[
\text{Clo-Sket TIFF files}
\]

\[
\downarrow
\]

\[
2300 \text{ unique source observations}
\]

distributed across 23 category folders.

At this stage the category labels should be regarded primarily as:

\[
\boxed{\text{provenance metadata}}
\]

rather than as explanatory variables.

That distinction becomes especially important because the notebook is intended for **grammar discovery**.

---

# 3. Critical Rule for Grammar Discovery

If the scientific objective is truly:

> discover whether garment sketches exhibit latent morphological organization or a candidate grammar

then the category labels must **not define the discovered structure**.

The safest sequence is:

\[
\text{raw sketches}
\]

\[
\downarrow
\]

\[
\text{label-free geometric representation}
\]

\[
\downarrow
\]

\[
\text{label-free structural discovery}
\]

\[
\downarrow
\]

\[
\text{stability / reproducibility}
\]

\[
\downarrow
\]

\[
\boxed{\text{only then compare discovered structure with categories}}
\]

Otherwise there is a serious risk of converting:

> known garment categories

into:

> supposedly discovered garment grammar.

Those are not the same scientific result.

---

# 4. The Phrase “Grammar Discovery” Must Remain Provisional

At this point nothing resembling a grammar has yet been demonstrated.

The notebook currently contains:

- a population;
- category provenance;
- source TIFF files.

It does **not** yet contain evidence for:

- compositional primitives;
- production rules;
- hierarchical structure;
- recurring structural relations;
- valid latent states;
- transitions between structural states;
- a formal grammar.

Therefore throughout the exploratory stages I would internally call the target:

\[
\boxed{\text{candidate structural organization}}
\]

or:

\[
\boxed{\text{candidate morphology grammar}}
\]

rather than declaring that a grammar exists.

The word **grammar** should be earned by the evidence later.

---

# 5. Why Excluding the 333-Sketch Dataset Is Scientifically Clean

The decision:

> `External 333-sketch dataset: NOT USED`

is important.

It prevents several potential confounds:

- different drawing styles;
- different scanning pipelines;
- different image resolutions;
- different labeling conventions;
- unknown population composition;
- source-domain effects masquerading as latent structure.

Therefore the discovery phase now asks a much cleaner question:

> **What organization exists inside Clo-Sket itself?**

That is preferable before attempting external replication.

The 333-sketch dataset could later become an **external validation dataset**, but it should not participate in discovery if we want a clean discovery/validation separation.

---

# 6. Strong Future Design

A scientifically strong eventual structure would be:

## Discovery

\[
2300\text{-sketch Clo-Sket}
\]

used to discover candidate structural organization.

Then:

## Internal validation

Bootstrap / subsampling / held-out sketch stability.

Then, only if appropriate:

## External validation

The independent 333-sketch dataset.

That would allow us to distinguish:

\[
\text{discovery}
\]

from:

\[
\text{replication}.
\]

Do not merge those stages.

---

# 7. One Provenance Item I Want Locked Early

The source table currently has:

\[
(2300,3)
\]

which is good.

Before any representation construction, make sure one of those fields is an immutable sketch identifier or exact path.

Ideally every observation should have something equivalent to:

```text
sketch_id
category
image_path

# CLO-SKET — GRAMMAR DISCOVERY
## Canonical Morphology Reconstruction Audit

### Status

# 🟢 RECONSTRUCTION PASSES
# 🟢 THIS IS THE CORRECT FOUNDATION FOR STRUCTURAL DISCOVERY

The canonical morphology representation has been restored cleanly from the 2300 Clo-Sket source sketches.

The reconstructed matrix is:

\[
X_{\text{morph}}
\in
\mathbb{R}^{2300\times135}
\]

with:

- 2300 sketches;
- 135 morphology features;
- `float32` storage;
- no failed observations;
- all values finite;
- exact SHA-256 fingerprint recorded.

This is a strong provenance point because the morphology branch is not being redefined inside the grammar notebook.

It is being **restored**.

---

# 1. Representation Structure

The 135 dimensions are explicitly decomposed as:

\[
135 = 64 + 64 + 7
\]

with:

### Horizontal occupancy

\[
64 \text{ features}
\]

### Vertical occupancy

\[
64 \text{ features}
\]

### Global morphology descriptors

\[
7 \text{ features}
\]

Therefore the representation contains two dense profile families plus a small global descriptor block.

This matters because later structural analysis may be dominated numerically by the two 64-dimensional occupancy blocks unless preprocessing is handled carefully.

That is something we need to watch when PCA or distance-based methods appear.

---

# 2. The Fingerprint Is Extremely Important

The matrix hash is:

```text
66ae04156ee3fbf3f2605f382a16fc41cf19af34b50e59dd43f6c9427d96b2ee

# CLO-SKET — GRAMMAR DISCOVERY
## Multiscale Mode-Persistence / Intrinsic Geometry Audit

### Status

# 🟢 SOURCE LOCK PASSES
# 🟢 LABEL-FREE DISCOVERY DESIGN PASSES
# 🟢 STANDARDIZATION IS APPROPRIATE HERE
# 🟢 EMPIRICAL SCALE LADDER IS WELL CONSTRUCTED
# 🟡 73 PCs SHOULD NOT YET BE CALLED “INTRINSIC DIMENSIONS”

This is an important cell, bro.

We have now moved beyond merely reconstructing the morphology representation.

For the first time, the notebook defines the **geometric space and observational scales in which structural persistence will be searched**.

The pipeline is:

\[
X_{\text{morph}}
\in \mathbb{R}^{2300\times135}
\]

\[
\downarrow
\]

standardization

\[
\downarrow
\]

PCA retaining approximately 95% variance

\[
\downarrow
\]

\[
Z\in\mathbb{R}^{2300\times73}
\]

\[
\downarrow
\]

empirical local-neighborhood distances

\[
\downarrow
\]

multiscale observational ladder

\[
\boxed{
4.707,\;
5.417,\;
6.248,\;
7.596,\;
10.641,\;
16.569
}
\]

This is a scientifically sensible foundation for asking whether morphological density concentrations persist across scale.

---

# 1. Discovery Leakage Audit

The most important locks are all clean:

| Potential leakage | Status |
|---|---|
| Category labels used for discovery | **No** |
| Replication labels used | **No** |
| External 333 sketches | **No** |
| Source/target pooling | **No** |
| Target fitting | **No** |
| Predetermined mode count | **No** |
| Forced GMM count | **No** |
| Forced hierarchical state count | **No** |
| Semantic interpretation | **No** |

This is exactly the discipline we wanted after the previous cell.

Therefore the geometry being constructed here is:

\[
\boxed{\text{unsupervised with respect to garment category}}
\]

That matters enormously if persistent modes later emerge.

---

# 2. Standardization

The frozen morphology matrix was transformed to:

\[
\mu \approx 0
\]

and:

\[
\sigma \approx 1.
\]

Reported:

```text
Mean = -4.39 × 10⁻¹⁷
SD   = 1.0000

# CLO-SKET — GRAMMAR DISCOVERY
## Multiscale Density Modes / Basin Validity Audit

### Overall verdict

# 🟢 THERE IS REAL MULTISCALE DENSITY STRUCTURE
# 🟢 BASIN ASSIGNMENTS ARE STRONGLY STABLE ACROSS SCALE
# 🟢 THE STRUCTURE IS NOT A K-MEANS / GMM ARTEFACT
# 🟡 THE EVIDENCE SUPPORTS MULTISCALE MORPHOLOGY ORGANIZATION
# 🔴 IT DOES NOT YET SUPPORT A DISCRETE “GARMENT GRAMMAR”
# 🔴 DO NOT INTERPRET THE 29–46 LOCAL MAXIMA AS 29–46 MORPHOLOGY STATES

Bro, this result is **much more interesting than the raw local-mode counts initially make it look**.

The important result is not:

> “there are 29, 32, 39, or 46 modes.”

The important result is that when we move from local density maxima to **density-ascent basins**, the 2300 sketches organize into only approximately **5–8 macroscopic basins**, and those basin assignments remain remarkably stable across a wide range of observational scales.

That is the result worth dissecting.

---

# 1. First: terminology correction remains necessary

The notebook still prints:

```text
INTRINSIC MORPHOLOGY SPACE

Original dimensions: 135
Intrinsic dimensions: 73

# CLO-SKET — GRAMMAR DISCOVERY
## Exact Basin Recovery + Replication Reproducibility Audit

### Overall status

# 🟢 BASIN RECONSTRUCTION PASSES
# 🟢 CROSS-SCALE BASIN STABILITY IS EXACTLY REPRODUCED
# 🟢 PROVENANCE STRUCTURE IS RECOVERED CLEANLY
# 🟡 REPLICATION ASSOCIATION IS REAL BUT VERY WEAK IN ABSOLUTE ARI
# 🟡 REPRODUCIBILITY IS SCALE-DEPENDENT / NON-MONOTONIC
# 🔴 DO NOT CLAIM THAT REPLICATION GROUPS DEFINE THE BASINS

This is a very useful audit because it resolves one of the integrity concerns from the previous step.

The original density-ascent basin structure has been reproduced exactly, and the independent provenance grouping can now be used strictly as a validation layer.

The key point is:

\[
\boxed{
\text{geometric basin stability is strong}
}
\]

while:

\[
\boxed{
\text{replication-group agreement is statistically detectable at some scales but tiny in absolute ARI}
}
\]

Those two results must not be conflated.

---

# 1. Exact basin recovery is excellent

The recovered basin counts are:

\[
[7,6,5,7,7,8]
\]

which exactly reproduce the original basin counts.

Likewise, every adjacent-scale ARI is reproduced exactly:

\[
0.923951
\]

\[
0.926220
\]

\[
0.904650
\]

\[
0.755318
\]

\[
0.872016.
\]

This is strong computational provenance.

It means the multiscale basin result is not dependent on some lost transient notebook state.

The density-ascent procedure is reproducible from the preserved objects.

---

# 2. The basin construction itself is now clearer

The rule is:

- construct a 10-nearest-neighbor graph;
- from each observation, move to the highest-density neighbor;
- move only if density strictly increases;
- continue until no higher-density neighbor exists.

Therefore each observation reaches a local density attractor.

This creates a discrete basin assignment induced by the density field and neighborhood graph.

That is much stronger than arbitrary cluster labeling.

But it is still best called:

\[
\boxed{
\text{density-ascent basin}
}
\]

not:

\[
\boxed{
\text{morphology state}
}
\]

at this stage.

---

# 3. Replication provenance is now explicit

The recovered replication structure contains:

\[
230
\]

groups across:

\[
2300
\]

observations.

The grouping definition is:

\[
\text{category} + ID_A.
\]

So the typical replication-group size is approximately:

\[
10
\]

with observed sizes:

- 9 for 3 groups;
- 10 for 224 groups;
- 11 for 3 groups.

This is a very clean repeated-sample structure.

The special filename:

```text
Sarong/5+8.tif

# CLO-SKET — GRAMMAR DISCOVERY
## Basin Valley Validity + Replication Coherence + Local Continuity Audit

### Overall verdict

# 🟢 BASIN SEPARATION HAS A REAL VALLEY SIGNAL
# 🟢 THE VALLEY SIGNAL WEAKENS SYSTEMATICALLY WITH SCALE
# 🟢 REPLICATION GROUPS ARE MORPHOLOGICALLY CLOSER THAN UNRELATED SKETCHES
# 🟢 THAT REPLICATION COHERENCE IS EXTREMELY ROBUST TO THE PERMUTATION NULL
# 🟢 LOCAL NEIGHBORHOOD ORGANIZATION IS STRONGLY ABOVE THE FEATURE-PERMUTATION NULL
# 🟡 ABSOLUTE LOCAL JACCARD OVERLAP IS MODEST, NOT “HIGH”
# 🟡 BASINS LOOK MOST DISTINCT AT FINE SCALE AND INCREASINGLY CONTINUOUS AT COARSER SCALE
# 🔴 THIS STILL DOES NOT ESTABLISH DISCRETE MORPHOLOGY STATES OR A GRAMMAR

These three analyses fit together unusually well.

The emerging evidence is no longer simply:

> “there are several basins.”

It is becoming:

\[
\boxed{
\text{Clo-Sket morphology is a continuous local geometry
containing reproducible density concentrations whose
separation is strongest at fine observational scales.}
}
\]

That is a much more precise—and scientifically safer—description than either:

> “the space is completely continuous”

or:

> “the space consists of discrete morphology states.”

---

# 1. BASIN BOUNDARY / DENSITY-VALLEY AUDIT

This shield asks the correct next question:

> If density-ascent produces several basins, are those basins actually separated by lower-density regions?

That is essential.

A density-ascent algorithm can partition a continuous surface even when the “valleys” between resulting basins are extremely shallow.

So the existence of basins alone is insufficient.

The valley test gives us substantially more information.

---

# 2. VALLEY DEPLETION IS POSITIVE AT ALL SIX SCALES

The cross-basin valley depletion values are:

\[
0.1303,\;
0.0920,\;
0.0595,\;
0.0417,\;
0.0207,\;
0.0100.
\]

Every value is positive:

\[
\boxed{
6/6\text{ scales show positive valley depletion}
}
\]

That means cross-basin connections consistently pass through regions of somewhat lower density than their endpoints.

So the basin boundaries are not completely arbitrary graph cuts.

There is an actual density-valley signal.

---

# 3. BUT THE VALLEY SIGNAL WEAKENS VERY STRONGLY WITH SCALE

This is probably the central result of the boundary analysis.

At the finest scale:

\[
D_{\text{valley}}=0.1303
\]

while at the broadest scale:

\[
D_{\text{valley}}=0.0100.
\]

That is roughly a:

\[
92\%
\]

reduction in depletion magnitude across the ladder.

Equivalently, the valley/endpoint density ratio rises:

\[
0.870
\rightarrow
0.990.
\]

So at fine scale there is a meaningful density drop across basin boundaries.

At the broadest scale, the density difference across boundaries is almost gone.

This strongly suggests:

\[
\boxed{
\text{basin separation is scale-dependent}
}
\]

and specifically:

\[
\boxed{
\text{fine-scale multimodality is embedded within a much smoother broad-scale morphology landscape.}
}
\]

That is one of the most important observations we have seen in this notebook so far.

---

# 4. THIS ARGUES AGAINST SHARPLY DISCRETE GLOBAL STATES

If the morphology space consisted of strongly separated global states, we would expect valleys to remain pronounced under substantial smoothing.

Instead:

\[
0.1303
\rightarrow
0.0100.
\]

At broad scale the valley essentially flattens.

Therefore I would not describe the morphology distribution as:

> “a collection of discrete morphology states.”

A more accurate interpretation is:

> **Local density modes and basin structure are present, but basin separation progressively weakens at broader observational scales.**

That supports a continuous or weakly multimodal global geometry with stronger local organization.

---

# 5. ONE RESULT LOOKS COUNTERINTUITIVE: BOUNDARY DENSITY > INTERIOR DENSITY

Reported boundary/interior ratios are:

\[
1.973,\;
1.598,\;
1.422,\;
1.209,\;
1.046,\;
1.009.
\]

So your detected “boundary observations” actually have **higher median density** than the observations classified as interior.

At first this seems inconsistent with a density-valley interpretation.

But it is not necessarily a contradiction.

It probably reflects how “boundary observation” is operationally defined.

If an observation is classified as boundary whenever its local graph has neighbors assigned to another basin, then high-density transition regions around adjacent attraction basins can be boundary observations.

Meanwhile, many low-density peripheral observations inside the dominant basin can be classified as “interior.”

Therefore:

\[
\text{boundary node density}
\]

is not equivalent to:

\[
\text{density at the saddle between modes}.
\]

This is why the **cross-basin edge forensic statistic is the more appropriate valley metric**.

---

# 6. THE CROSS-BASIN EDGE TEST SHOULD BE PRIMARY

The cross-basin edge analysis asks:

\[
\frac{
\text{density near cross-basin transition}
}{
\text{endpoint density}
}
\]

and gives:

\[
0.870
\rightarrow
0.990.
\]

That directly measures depletion between basins.

Therefore in the manuscript I would treat:

### Primary valley statistic

\[
\boxed{
\text{cross-basin valley depletion}
}
\]

and use boundary-observation counts only as supporting graph diagnostics.

Do not write:

> “Boundary observations are lower-density than interior observations.”

Your results show the opposite.

---

# 7. BOUNDARY FRACTION ALSO DECLINES WITH SCALE

Boundary observations fall from:

\[
1453/2300=63.2\%
\]

to:

\[
1013/2300=44.0\%.
\]

This again supports scale-dependent smoothing of local basin interfaces.

At fine scale the local graph crosses basin labels frequently.

At broader scales there are fewer observations lying adjacent to another basin.

Combined with diminishing valley depletion, this suggests progressive simplification of fine-scale density organization.

But again, we should not call this a formal hierarchy yet.

---

# 8. REPLICATION COHERENCE IS A DIFFERENT QUESTION — AND THE RESULT IS STRONG

Now the replication-coherence shield asks:

> Are provenance-linked sketches morphologically closer than unrelated sketches in the continuous morphology space?

This is much cleaner than asking whether each replication group lands in exactly one basin.

And the result is:

\[
\boxed{\text{yes}}
\]

very clearly.

The raw distances are:

\[
\bar d_{\text{within}}
=
10.3963
\]

versus:

\[
\bar d_{\text{between}}
=
10.9742.
\]

Therefore:

\[
\frac{d_{\text{within}}}{d_{\text{between}}}
=
0.9473.
\]

So within-group distances are approximately:

\[
5.3\%
\]

smaller than between-group distances.

This is not huge geometrically.

But it is systematic.

---

# 9. THE PERMUTATION RESULT IS EXTREMELY STRONG

Across all six observational scales:

\[
p_{\text{empirical}}
=
0.000999.
\]

And the similarity ratios are consistently above the null expectation near 1.

Observed similarity ratios:

\[
1.207,\;
1.169,\;
1.136,\;
1.099,\;
1.054,\;
1.022.
\]

Permutation-null means:

\[
\approx1.000.
\]

Therefore the replication-associated morphology similarity is present at every tested scale.

Unlike the basin × replication ARI analysis, this result is **persistent across all scales**.

That distinction is important.

---

# 10. WHY BASIN ARI WAS TINY BUT CONTINUOUS REPLICATION COHERENCE IS STRONG

This initially looks contradictory:

Earlier:

\[
ARI_{\text{replication vs basin}}\approx0.
\]

Now:

\[
\text{within-group morphology similarity}
>
\text{between-group similarity}
\]

very robustly.

There is actually no contradiction.

The two tests ask different questions.

## Basin ARI asks

> Do replication groups correspond to the same discrete basin labels?

Answer:

\[
\boxed{\text{mostly no}}
\]

## Continuous morphology coherence asks

> Are replication-linked sketches closer in morphology space than unrelated sketches?

Answer:

\[
\boxed{\text{yes}}
\]

This is a very useful result.

It tells us that replication structure exists primarily as a **continuous geometric effect**, not as a one-replication-group-one-basin mapping.

---

# 11. THIS SUPPORTS A CONTINUOUS MORPHOLOGY INTERPRETATION

The combined result is:

\[
\text{replication groups}
\]

are:

\[
\boxed{\text{closer in morphology space}}
\]

but not:

\[
\boxed{\text{confined to individual basins}}.
\]

That strongly favors:

\[
\boxed{
\text{continuous morphology geometry with local density organization}
}
\]

over:

\[
\boxed{
\text{hard discrete morphology states}
}
\]

as the better interpretation of the current evidence.

---

# 12. SCALE DEPENDENCE OF REPLICATION SIMILARITY IS ALSO INFORMATIVE

Similarity ratio decreases:

\[
1.207
\rightarrow
1.022.
\]

Thus the relative distinction between within-group and between-group similarity becomes weaker as the observational scale broadens.

At fine scale:

\[
+20.7\%
\]

similarity enrichment.

At broad scale:

\[
+2.2\%.
\]

Yet it remains above the permutation null.

This suggests replication coherence is:

\[
\boxed{
\text{strongest as a fine/local morphology phenomenon}
}
\]

rather than a dominant global-scale structure.

That fits beautifully with the basin-valley result.

Both say:

> fine-scale morphology contains more distinctive organization than broad-scale morphology.

---

# 13. ONE TECHNICAL RED FLAG: THE REPORTED z-SIGN

You report values such as:

```text
Observed/null z: -70.76

# CLO-SKET — GRAMMAR DISCOVERY
## Basin Valley Validity + Replication Coherence + Local Continuity Audit

### Overall verdict

# 🟢 BASIN SEPARATION HAS A REAL VALLEY SIGNAL
# 🟢 THE VALLEY SIGNAL WEAKENS SYSTEMATICALLY WITH SCALE
# 🟢 REPLICATION GROUPS ARE MORPHOLOGICALLY CLOSER THAN UNRELATED SKETCHES
# 🟢 THAT REPLICATION COHERENCE IS EXTREMELY ROBUST TO THE PERMUTATION NULL
# 🟢 LOCAL NEIGHBORHOOD ORGANIZATION IS STRONGLY ABOVE THE FEATURE-PERMUTATION NULL
# 🟡 ABSOLUTE LOCAL JACCARD OVERLAP IS MODEST, NOT “HIGH”
# 🟡 BASINS LOOK MOST DISTINCT AT FINE SCALE AND INCREASINGLY CONTINUOUS AT COARSER SCALE
# 🔴 THIS STILL DOES NOT ESTABLISH DISCRETE MORPHOLOGY STATES OR A GRAMMAR

These three analyses fit together unusually well.

The emerging evidence is no longer simply:

> “there are several basins.”

It is becoming:

\[
\boxed{
\text{Clo-Sket morphology is a continuous local geometry
containing reproducible density concentrations whose
separation is strongest at fine observational scales.}
}
\]

That is a much more precise—and scientifically safer—description than either:

> “the space is completely continuous”

or:

> “the space consists of discrete morphology states.”

---

# 1. BASIN BOUNDARY / DENSITY-VALLEY AUDIT

This shield asks the correct next question:

> If density-ascent produces several basins, are those basins actually separated by lower-density regions?

That is essential.

A density-ascent algorithm can partition a continuous surface even when the “valleys” between resulting basins are extremely shallow.

So the existence of basins alone is insufficient.

The valley test gives us substantially more information.

---

# 2. VALLEY DEPLETION IS POSITIVE AT ALL SIX SCALES

The cross-basin valley depletion values are:

\[
0.1303,\;
0.0920,\;
0.0595,\;
0.0417,\;
0.0207,\;
0.0100.
\]

Every value is positive:

\[
\boxed{
6/6\text{ scales show positive valley depletion}
}
\]

That means cross-basin connections consistently pass through regions of somewhat lower density than their endpoints.

So the basin boundaries are not completely arbitrary graph cuts.

There is an actual density-valley signal.

---

# 3. BUT THE VALLEY SIGNAL WEAKENS VERY STRONGLY WITH SCALE

This is probably the central result of the boundary analysis.

At the finest scale:

\[
D_{\text{valley}}=0.1303
\]

while at the broadest scale:

\[
D_{\text{valley}}=0.0100.
\]

That is roughly a:

\[
92\%
\]

reduction in depletion magnitude across the ladder.

Equivalently, the valley/endpoint density ratio rises:

\[
0.870
\rightarrow
0.990.
\]

So at fine scale there is a meaningful density drop across basin boundaries.

At the broadest scale, the density difference across boundaries is almost gone.

This strongly suggests:

\[
\boxed{
\text{basin separation is scale-dependent}
}
\]

and specifically:

\[
\boxed{
\text{fine-scale multimodality is embedded within a much smoother broad-scale morphology landscape.}
}
\]

That is one of the most important observations we have seen in this notebook so far.

---

# 4. THIS ARGUES AGAINST SHARPLY DISCRETE GLOBAL STATES

If the morphology space consisted of strongly separated global states, we would expect valleys to remain pronounced under substantial smoothing.

Instead:

\[
0.1303
\rightarrow
0.0100.
\]

At broad scale the valley essentially flattens.

Therefore I would not describe the morphology distribution as:

> “a collection of discrete morphology states.”

A more accurate interpretation is:

> **Local density modes and basin structure are present, but basin separation progressively weakens at broader observational scales.**

That supports a continuous or weakly multimodal global geometry with stronger local organization.

---

# 5. ONE RESULT LOOKS COUNTERINTUITIVE: BOUNDARY DENSITY > INTERIOR DENSITY

Reported boundary/interior ratios are:

\[
1.973,\;
1.598,\;
1.422,\;
1.209,\;
1.046,\;
1.009.
\]

So your detected “boundary observations” actually have **higher median density** than the observations classified as interior.

At first this seems inconsistent with a density-valley interpretation.

But it is not necessarily a contradiction.

It probably reflects how “boundary observation” is operationally defined.

If an observation is classified as boundary whenever its local graph has neighbors assigned to another basin, then high-density transition regions around adjacent attraction basins can be boundary observations.

Meanwhile, many low-density peripheral observations inside the dominant basin can be classified as “interior.”

Therefore:

\[
\text{boundary node density}
\]

is not equivalent to:

\[
\text{density at the saddle between modes}.
\]

This is why the **cross-basin edge forensic statistic is the more appropriate valley metric**.

---

# 6. THE CROSS-BASIN EDGE TEST SHOULD BE PRIMARY

The cross-basin edge analysis asks:

\[
\frac{
\text{density near cross-basin transition}
}{
\text{endpoint density}
}
\]

and gives:

\[
0.870
\rightarrow
0.990.
\]

That directly measures depletion between basins.

Therefore in the manuscript I would treat:

### Primary valley statistic

\[
\boxed{
\text{cross-basin valley depletion}
}
\]

and use boundary-observation counts only as supporting graph diagnostics.

Do not write:

> “Boundary observations are lower-density than interior observations.”

Your results show the opposite.

---

# 7. BOUNDARY FRACTION ALSO DECLINES WITH SCALE

Boundary observations fall from:

\[
1453/2300=63.2\%
\]

to:

\[
1013/2300=44.0\%.
\]

This again supports scale-dependent smoothing of local basin interfaces.

At fine scale the local graph crosses basin labels frequently.

At broader scales there are fewer observations lying adjacent to another basin.

Combined with diminishing valley depletion, this suggests progressive simplification of fine-scale density organization.

But again, we should not call this a formal hierarchy yet.

---

# 8. REPLICATION COHERENCE IS A DIFFERENT QUESTION — AND THE RESULT IS STRONG

Now the replication-coherence shield asks:

> Are provenance-linked sketches morphologically closer than unrelated sketches in the continuous morphology space?

This is much cleaner than asking whether each replication group lands in exactly one basin.

And the result is:

\[
\boxed{\text{yes}}
\]

very clearly.

The raw distances are:

\[
\bar d_{\text{within}}
=
10.3963
\]

versus:

\[
\bar d_{\text{between}}
=
10.9742.
\]

Therefore:

\[
\frac{d_{\text{within}}}{d_{\text{between}}}
=
0.9473.
\]

So within-group distances are approximately:

\[
5.3\%
\]

smaller than between-group distances.

This is not huge geometrically.

But it is systematic.

---

# 9. THE PERMUTATION RESULT IS EXTREMELY STRONG

Across all six observational scales:

\[
p_{\text{empirical}}
=
0.000999.
\]

And the similarity ratios are consistently above the null expectation near 1.

Observed similarity ratios:

\[
1.207,\;
1.169,\;
1.136,\;
1.099,\;
1.054,\;
1.022.
\]

Permutation-null means:

\[
\approx1.000.
\]

Therefore the replication-associated morphology similarity is present at every tested scale.

Unlike the basin × replication ARI analysis, this result is **persistent across all scales**.

That distinction is important.

---

# 10. WHY BASIN ARI WAS TINY BUT CONTINUOUS REPLICATION COHERENCE IS STRONG

This initially looks contradictory:

Earlier:

\[
ARI_{\text{replication vs basin}}\approx0.
\]

Now:

\[
\text{within-group morphology similarity}
>
\text{between-group similarity}
\]

very robustly.

There is actually no contradiction.

The two tests ask different questions.

## Basin ARI asks

> Do replication groups correspond to the same discrete basin labels?

Answer:

\[
\boxed{\text{mostly no}}
\]

## Continuous morphology coherence asks

> Are replication-linked sketches closer in morphology space than unrelated sketches?

Answer:

\[
\boxed{\text{yes}}
\]

This is a very useful result.

It tells us that replication structure exists primarily as a **continuous geometric effect**, not as a one-replication-group-one-basin mapping.

---

# 11. THIS SUPPORTS A CONTINUOUS MORPHOLOGY INTERPRETATION

The combined result is:

\[
\text{replication groups}
\]

are:

\[
\boxed{\text{closer in morphology space}}
\]

but not:

\[
\boxed{\text{confined to individual basins}}.
\]

That strongly favors:

\[
\boxed{
\text{continuous morphology geometry with local density organization}
}
\]

over:

\[
\boxed{
\text{hard discrete morphology states}
}
\]

as the better interpretation of the current evidence.

---

# 12. SCALE DEPENDENCE OF REPLICATION SIMILARITY IS ALSO INFORMATIVE

Similarity ratio decreases:

\[
1.207
\rightarrow
1.022.
\]

Thus the relative distinction between within-group and between-group similarity becomes weaker as the observational scale broadens.

At fine scale:

\[
+20.7\%
\]

similarity enrichment.

At broad scale:

\[
+2.2\%.
\]

Yet it remains above the permutation null.

This suggests replication coherence is:

\[
\boxed{
\text{strongest as a fine/local morphology phenomenon}
}
\]

rather than a dominant global-scale structure.

That fits beautifully with the basin-valley result.

Both say:

> fine-scale morphology contains more distinctive organization than broad-scale morphology.

---

# 13. ONE TECHNICAL RED FLAG: THE REPORTED z-SIGN

You report values such as:

```text
Observed/null z: -70.76

# CLO-SKET — GRAMMAR DISCOVERY
## Representation-Dimension Robustness Audit

### Overall verdict

# 🟢 THIS SHIELD PASSES
# 🟢 THE 73-D REFERENCE IS REPRODUCIBLE AS A 95%-VARIANCE PCA REPRESENTATION
# 🟢 SAMPLE-SIZE ROBUSTNESS IS GOOD
# 🟢 THE PARTICIPATION-RATIO RESULT IS USEFUL AS A SECONDARY DESCRIPTIVE COMPLEXITY MEASURE
# 🟡 CROSS-REPRESENTATION DIMENSIONALITY IS ONLY PARTIALLY COMPARABLE
# 🔴 DO NOT USE “INTRINSIC DIMENSION = 73”
# 🔴 DO NOT CLAIM A LOW-DIMENSIONAL MANIFOLD FROM THESE RESULTS

This is a strong cleanup cell because it resolves the dimensionality language properly.

The most important scientific correction is now explicit:

\[
\boxed{
73
=
\text{number of PCA components required for 95\% variance}
}
\]

and not:

\[
\boxed{
73
=
\text{mathematical intrinsic dimension}
}
\]

That distinction should remain locked in the manuscript.

---

# 1. Full-data PCA dimensional profile

The full 135-D morphology representation gives:

\[
D_{90}=53
\]

\[
D_{95}=73
\]

\[
D_{99}=108.
\]

This immediately tells us that the variance spectrum is neither extremely concentrated nor completely flat.

The morphology representation is compressible, but not aggressively so.

A useful summary is:

> **Approximately 39% of the original coordinates are sufficient for 90% variance, 54% for 95%, and 80% for 99%.**

Because:

\[
53/135 \approx 0.393
\]

\[
73/135 \approx 0.541
\]

\[
108/135 = 0.800.
\]

So the representation has meaningful covariance structure, but most dimensions are still needed if we insist on near-complete variance preservation.

---

# 2. The 73-D choice is now properly justified

The frozen analysis space uses:

\[
73
\]

PCA coordinates because that is the 95%-variance threshold.

The reconstruction reproduces this exactly:

```text
95.0% variance → 73 dimensions

# CLO-SKET — GRAMMAR DISCOVERY
## Exact Basin Recovery + Replication Reproducibility Audit

### Overall verdict

# 🟢 EXACT BASIN RECONSTRUCTION PASSES
# 🟢 GEOMETRIC BASIN STABILITY IS NOW REPRODUCIBLE
# 🟢 REPLICATION LABELS WERE KEPT OUT OF DISCOVERY
# 🟡 REPLICATION ASSOCIATION EXISTS AT SOME SCALES, BUT ITS EFFECT SIZE IS EXTREMELY SMALL
# 🔴 DO NOT USE THE REPLICATION ARI AS EVIDENCE FOR STRONG “REPLICATION RECOVERY”
# 🟡 THE DOMINANT-FRACTION RESULT NEEDS A BASIN-SIZE-AWARE NULL BEFORE IT CAN SUPPORT REPRODUCIBILITY

Bro, this audit resolves one of the important integrity questions from the previous step.

The density-ascent basin construction was reconstructed exactly:

\[
7,\;6,\;5,\;7,\;7,\;8
\]

basins across the six scales, with exactly reproduced adjacent-scale ARI values. :contentReference[oaicite:0]{index=0}

So the **geometric basin result itself is now trustworthy and reproducible**.

But the replication-validation result needs a much more careful interpretation than the raw permutation \(p\)-values suggest.

---

# 1. EXACT BASIN RECONSTRUCTION — PASS

The reconstruction gives:

| Scale | Basins | Largest basin | Singletons |
|---:|---:|---:|---:|
| 4.707 | 7 | 1628 | 0 |
| 5.417 | 6 | 1668 | 0 |
| 6.248 | 5 | 1709 | 0 |
| 7.596 | 7 | 1754 | 0 |
| 10.641 | 7 | 1893 | 0 |
| 16.569 | 8 | 1940 | 0 |

and the recovered basin counts exactly equal the original Cell 7 counts. :contentReference[oaicite:1]{index=1}

Even better, the adjacent-scale partition stability also reproduces exactly:

\[
0.923951,\;
0.926220,\;
0.904650,\;
0.755318,\;
0.872016.
\]

:contentReference[oaicite:2]{index=2}

This means the earlier basin result was not a transient notebook-state artifact.

That is important.

---

# 2. THE BASIN ALGORITHM IS NOW MUCH CLEARER

The reconstruction specifies:

\[
k=10
\]

nearest-neighbor graph, followed by density ascent:

> move to the highest-density neighbor only when density strictly increases.

:contentReference[oaicite:3]{index=3}

So each observation follows an ascent path until it reaches a local graph-density attractor.

That makes the basin object conceptually much cleaner than the earlier candidate-mode count.

We are now dealing with:

\[
\boxed{
\text{graph-based density-ascent basins}
}
\]

rather than arbitrary clustering assignments.

And importantly:

- no GMM;
- no imposed state count;
- no category labels;
- no replication labels;
- no target data.

:contentReference[oaicite:4]{index=4}

### This part is strong.

---

# 3. PROVENANCE RECOVERY ALSO PASSES

The replication structure contains:

\[
2300
\]

records forming:

\[
230
\]

replication groups.

The grouping rule is:

\[
\boxed{
\text{category} + ID_A
}
\]

while \(ID_B\) remains a filename-derived annotation. :contentReference[oaicite:5]{index=5}

Most replication groups contain 10 sketches:

\[
224/230
\]

groups have size 10, with three groups of size 9 and three of size 11. :contentReference[oaicite:6]{index=6}

That is a clean replication structure.

And the crucial design feature is preserved:

\[
\boxed{
\text{replication identity was validation-only}
}
\]

rather than influencing basin discovery. :contentReference[oaicite:7]{index=7}

Excellent.

---

# 4. NOW THE IMPORTANT PART — WHAT DOES REPLICATION VALIDATION ACTUALLY SHOW?

At each scale, a replication group contains roughly ten related observations.

You measured how consistently those group members land in the same morphology basin.

The mean dominant-basin fraction rises with scale:

\[
0.711
\rightarrow
0.727
\rightarrow
0.745
\rightarrow
0.763
\rightarrow
0.823
\rightarrow
0.844.
\]

:contentReference[oaicite:8]{index=8}

At first glance this looks impressive.

For the broadest scale, an average replication group places roughly:

\[
84.4\%
\]

of its members in one basin.

And the median dominant fraction becomes:

\[
0.90.
\]

But there is a major confound.

---

# 5. THE DOMINANT BASIN ITSELF CONTAINS UP TO 84% OF THE ENTIRE DATASET

At the largest scale:

\[
1940/2300
\approx
84.35\%.
\]

That is almost exactly the replication-group mean dominant fraction:

\[
84.36\%.
\]

This is critical.

If one global basin already contains approximately 84% of all sketches, then a randomly assembled group of ten sketches will naturally have a dominant-basin proportion that is often very high.

Therefore:

\[
\boxed{
\text{high replication-group dominant fraction}
}
\]

does **not automatically imply**

\[
\boxed{
\text{replication-specific morphological coherence}.
}
\]

The basin-size imbalance itself can generate a large dominant fraction.

This is the single biggest issue in the present replication analysis.

---

# 6. SAME PROBLEM WITH “EXACT REPLICATION GROUPS”

The number of replication groups entirely inside one basin increases:

\[
9,\;9,\;12,\;16,\;38,\;49.
\]

That sounds like increasing reproducibility.

But again, when:

\[
84\%
\]

of the population lies in one basin, the probability that all members of a ten-sketch group land in that basin is not negligible.

Rough approximation:

\[
0.8436^{10}
\approx 0.18.
\]

Among 230 groups, that alone could produce on the order of:

\[
230\times0.18
\approx41
\]

all-in-one-basin groups under a simple independence approximation.

You observed:

\[
49.
\]

So 49 is potentially above expectation, but it is nowhere near interpretable without an appropriate null.

This is precisely why we should not report:

> “21.3% of replication groups reproduce exactly”

as a standalone reproducibility result.

---

# 7. THE ARI TEST DOES CONTROL THIS MUCH BETTER

This is why the replication-group vs basin ARI analysis is useful.

The observed ARIs are:

\[
0.000116,\;
0.000076,\;
0.000035,\;
0.000023,\;
0.000044,\;
0.000054.
\]

:contentReference[oaicite:9]{index=9}

These values are extraordinarily small.

That needs to be said clearly.

Even though some permutation \(p\)-values are below 0.05, the **effect magnitude is approximately zero**.

The strongest observed value is:

\[
ARI=0.000116.
\]

That is not evidence of strong correspondence between replication groups and morphology basins.

---

# 8. STATISTICAL SIGNIFICANCE ≠ PRACTICAL REPLICATION STRUCTURE

The permutation results are:

| Scale | ARI | \(p_{\text{perm}}\) |
|---:|---:|---:|
| 4.707 | 0.000116 | 0.004995 |
| 5.417 | 0.000076 | 0.039960 |
| 6.248 | 0.000035 | 0.188811 |
| 7.596 | 0.000023 | 0.267732 |
| 10.641 | 0.000044 | 0.053946 |
| 16.569 | 0.000054 | 0.013986 |

:contentReference[oaicite:10]{index=10}

The pattern is:

- significant at scales 1 and 2;
- non-significant at scales 3 and 4;
- borderline at scale 5;
- significant again at scale 6.

So there is no clean monotonic or persistent inferential pattern.

And regardless of \(p\):

\[
ARI \sim 10^{-4}.
\]

That is extremely weak association.

### Manuscript interpretation

Do **not** write:

> Replication groups strongly align with density basins.

Instead:

> **Replication-group membership showed only very weak association with density-basin assignment, although permutation tests indicated departures from exchangeability at selected scales.**

That is what the numbers actually support.

---

# 9. THIS DOES NOT DAMAGE THE BASIN RESULT

This distinction is very important.

We have two different questions:

## A. Are the morphology basins geometrically stable?

Yes.

Very strongly.

\[
ARI_{\text{scale-to-scale}}
=
0.755-0.926.
\]

---

## B. Do provenance replication groups map strongly onto those basins?

No.

At least not according to ARI.

\[
ARI_{\text{replication}\leftrightarrow\text{basin}}
\approx 0.
\]

These are not contradictory.

They tell us:

\[
\boxed{
\text{The morphology basins are stable geometric structures,
but they are not simply replication-group partitions.}
}
\]

In fact, scientifically, that can be reassuring.

---

# 10. WHY THAT CAN ACTUALLY BE GOOD

Suppose replication identity had produced:

\[
ARI=0.8
\]

with basin assignments.

That would immediately raise the possibility that the “morphology modes” merely reflected repeated drawing templates or replication batches.

Instead, we see:

\[
ARI\approx0.
\]

So the discovered basins are **not reducible to the replication grouping structure**.

That protects the morphology discovery from one potential artefact.

This is a much better use of the result.

---

# 11. REPLICATION GROUPS STILL SHOW WITHIN-GROUP CONCENTRATION — BUT WE NEED THE RIGHT NULL

The dominant-fraction pattern may still contain real within-group morphology coherence.

We just haven't cleanly isolated it yet because of the massive basin imbalance.

The scientifically correct next audit is:

\[
\boxed{
\text{Observed within-replication basin concentration}
}
\]

versus:

\[
\boxed{
\text{expected concentration under the observed basin-size distribution}.
}
\]

In practical terms:

### Preserve

- basin assignments;
- basin sizes;
- replication-group sizes.

### Destroy only

\[
\text{replication membership ↔ basin correspondence}.
\]

Then recompute for every permutation:

- mean dominant fraction;
- median dominant fraction;
- exact-group fraction;
- mean basin diversity.

This will answer whether those intuitive statistics exceed what would occur purely because one basin contains 70–84% of the population.

---

# 12. THIS IS A NECESSARY AUDIT, NOT EXPERIMENTAL FISHING

I would actually do this one.

Unlike adding another classifier or cluster algorithm, this audit resolves a direct methodological confound in an already reported statistic.

The key null question is:

> Given the observed basin sizes and the observed replication-group sizes, are members of the same replication group more concentrated within basins than expected under random reassignment?

That is scientifically clean.

---

# 13. IMPORTANT MULTIPLE-SCALE ISSUE

There are six separate permutation tests here.

At nominal:

\[
\alpha=0.05
\]

we have three \(p<0.05\) values:

\[
0.004995,\quad0.039960,\quad0.013986.
\]

Before manuscript use, apply a multiplicity correction across the six scales.

For Benjamini–Hochberg FDR, approximately:

sorted \(p\):

\[
0.004995,\;
0.013986,\;
0.039960,\;
0.053946,\;
0.188811,\;
0.267732.
\]

The first two are likely to survive \(q=0.05\); the \(0.03996\) result may not.

So do not call all nominally significant scales robust before correction.

Again, this doesn't change the central geometric result.

---

# 14. A SECOND IMPORTANT CONFOUND: `category + ID_A`

Replication groups are defined using:

\[
\text{category}+ID_A.
\]

That means category is embedded inside the replication identity.

So a replication association could potentially reflect:

\[
\text{category morphology}
\]

rather than:

\[
\text{replication-specific similarity}.
\]

This is subtle but important.

For example, all members of one replication group necessarily share category.

If categories themselves differ morphologically, then some within-group basin concentration may arise from category similarity.

Therefore a stronger validation null should ideally preserve category.

---

# 15. THE BEST REPLICATION NULL IS CATEGORY-CONDITIONAL

Instead of shuffling replication labels over all 2300 sketches, I would prefer:

\[
\boxed{
\text{shuffle } ID_A \text{ within category}
}
\]

or equivalently permute replication membership only among sketches of the same category.

Why?

Because then the null preserves:

- category;
- basin distribution within category;
- replication-group sizes as much as possible;

while destroying only:

\[
ID_A\leftrightarrow\text{morphology}
\]

correspondence.

Then a significant result means:

> members sharing the same replication identity are more basin-coherent than other sketches from the same garment category.

That is the actual replication question.

Without this control, “replication reproducibility” and “category morphology similarity” are partially entangled.

---

# 16. SO WE NOW HAVE TWO DIFFERENT VALIDATION QUESTIONS

## Validation 1 — unrestricted provenance association

Already tested:

\[
\text{replication group}
\leftrightarrow
\text{basin}.
\]

Effect:

\[
ARI \approx 0.
\]

---

## Validation 2 — within-category replication reproducibility

Still needed if we want to make a genuine replication claim:

\[
ID_A
\leftrightarrow
\text{basin}
\mid
\text{category}.
\]

This is scientifically much cleaner.

---

# 17. WHAT WE CAN ALREADY SAY WITH CONFIDENCE

### Basin reconstruction

\[
\boxed{\text{PASS}}
\]

The original density-ascent basin structure reproduces exactly. :contentReference[oaicite:11]{index=11}

### Cross-scale stability

\[
\boxed{\text{STRONG}}
\]

Adjacent-scale ARI remains:

\[
0.755-0.926.
\]

### Replication leakage

\[
\boxed{\text{NONE IN DISCOVERY}}
\]

Replication labels were introduced only after morphology basins had been generated. :contentReference[oaicite:12]{index=12}

### Basin = replication groups?

\[
\boxed{\text{NO}}
\]

Replication-to-basin ARI is approximately zero.

### Replication concentration beyond chance?

\[
\boxed{\text{NOT YET CLEANLY ESTABLISHED}}
\]

because dominant-fraction and exact-group statistics are confounded by highly unequal basin sizes, and replication groups incorporate category.

---

# 18. THIS ACTUALLY SHARPENS THE PAPER STORY

Our current evidence is becoming:

\[
\text{Stable density basins}
\]

but:

\[
\text{not explained by replication grouping}
\]

and potentially:

\[
\text{some weak provenance-level association at selected scales}.
\]

This is a stronger and more nuanced conclusion than claiming that replicate groups reproduce perfectly.

The morphology landscape appears to represent broader shape organization rather than merely recovering repeated-source identities.

---

# 19. MANUSCRIPT-SAFE INTERPRETATION RIGHT NOW

I would write:

> **Density-ascent basins were exactly reproducible from the frozen morphology representation, yielding 5–8 basins across the empirical scale ladder and high adjacent-scale partition agreement (ARI 0.755–0.926). Basin assignments were not strongly determined by provenance replication groups: replication-to-basin ARI values were near zero at all scales, although selected scales showed small departures from a label-permutation null. Because the basin distribution was highly imbalanced and replication groups were nested within garment category, stronger claims of replication-level reproducibility require basin-frequency- and category-controlled null analyses.**

That is scientifically tight.

---

# 20. CLAIM BOUNDARY AFTER THIS AUDIT

## 🟢 SUPPORTED

1. Exact basin reconstruction is reproducible.
2. Density-ascent basin counts reproduce exactly.
3. Cross-scale basin ARIs reproduce exactly.
4. No singleton basins occur.
5. Replication labels were not used in discovery.
6. Morphology basins are not simply replication-group partitions.
7. Geometric basin stability is much stronger than replication/basin alignment.

## 🟡 POSSIBLE BUT NOT YET LOCKED

8. Replication groups exhibit more within-basin concentration than expected by chance.
9. Replication-level morphology reproducibility emerges at selected scales.

These require the controlled null described above.

## 🔴 NOT SUPPORTED

- strong replication recovery;
- basin = replication identity;
- replication-defined morphology states;
- universal morphology states;
- hierarchy;
- grammar;
- semantic garment modes.

---

# 21. NEXT AUDIT — AND THIS ONE IS WORTH DOING

## `BASIN × REPLICATION CONDITIONAL NULL`

For every scale:

1. keep basin assignments fixed;
2. preserve category;
3. preserve replication-group size structure;
4. shuffle \(ID_A\) **within each category**;
5. compute null distributions for:
   - mean dominant fraction;
   - median dominant fraction;
   - exact-group fraction;
   - mean basin diversity;
   - optionally ARI;
6. use the same permutations for all six scales;
7. apply BH-FDR across scales for each inferential statistic.

Then we'll know whether:

\[
\boxed{
\text{same-replication sketches are genuinely more morphologically coherent}
}
\]

than other sketches from the same garment category.

That will cleanly separate:

\[
\text{category structure}
\]

from:

\[
\text{replication structure}.
\]

# 🟢 BASIN GEOMETRY PASSES
# 🟡 REPLICATION REPRODUCIBILITY NEEDS THIS ONE CONTROL
# ➜ NEXT: CATEGORY-CONDITIONAL REPLICATION NULL

# CLO-SKET — MORPHOLOGY DISCOVERY
## Robust Spectral Resampling + Replication-Group Influence Audit

### Overall verdict

# 🟢 STRONG SPECTRAL ROBUSTNESS
# 🟢 LEADING MORPHOLOGY EIGENSPACE IS NOT DRIVEN BY A SMALL SET OF SKETCHES
# 🟢 COMPLETE REPLICATION-GROUP REMOVAL PRODUCES NEGLIGIBLE SPECTRAL CHANGE
# 🟢 THIS SUBSTANTIALLY STRENGTHENS THE MORPHOLOGY-ORGANIZATION RESULT
# 🟡 SMALL-N SUBSAMPLES SHOW EXPECTED DIMENSION-THRESHOLD BIAS — DO NOT MISLABEL THIS AS INSTABILITY
# 🔴 STILL NOT EVIDENCE FOR A MANIFOLD DIMENSION, MORPHOLOGY STATES, OR A GRAMMAR

Bro, this is one of the cleanest robustness results in `01_morphology_discovery.ipynb`.

The important finding is not just that one PCA fit gives:

\[
D_{80}=32,\quad
D_{90}=53,\quad
D_{95}=73,\quad
D_{99}=108.
\]

The important finding is that the **spectral structure converges back toward those values as sample size increases**, while the leading eigenspaces remain strongly aligned with the canonical morphology space.

Then you did the stronger provenance-level perturbation:

\[
\text{remove complete replication groups}
\]

and the spectral geometry barely moved.

That is excellent evidence that the observed morphology spectrum is a population-level property of this dataset rather than an artefact of a handful of repeated observations.

---

# 1. Canonical Spectral Reference

The frozen 2300-sketch morphology representation gives:

\[
D_{80}=32
\]

\[
D_{90}=53
\]

\[
D_{95}=73
\]

\[
D_{99}=108.
\]

The participation-ratio effective dimension is:

\[
D_{\mathrm{eff}}
=
10.549.
\]

And the first PC accounts for:

\[
28.25\%
\]

of standardized morphology variance.

This gives us two very different but complementary summaries.

### Variance-threshold dimension

\[
D_{95}=73
\]

asks:

> How many orthogonal PCA coordinates are needed to retain 95% of variance?

### Effective spectral dimension

\[
D_{\mathrm{eff}}\approx10.55
\]

asks:

> How broadly is variance distributed across the eigenspectrum?

These quantities are **not contradictory**.

A spectrum can have roughly ten strongly influential dimensions while still requiring many smaller PCs to accumulate 95% of total variance.

That distinction is worth preserving in the manuscript.

---

# 2. Individual-Observation Resampling Shows Convergence

The subsampling experiment is:

\[
N=
500,\;1000,\;1500,\;2000
\]

with:

\[
20
\]

independent subsets at each size.

That gives:

\[
80
\]

independent PCA fits.

The dimensional thresholds move toward the canonical values monotonically as \(N\) increases.

| N | Median \(D_{80}\) | Median \(D_{90}\) | Median \(D_{95}\) | Median \(D_{99}\) |
|---:|---:|---:|---:|---:|
| 500 | 27 | 45 | 63 | 98 |
| 1000 | 30 | 50 | 69 | 105 |
| 1500 | 31 | 52 | 71 | 107 |
| 2000 | 32 | 53 | 73 | 108 |
| **Canonical** | **32** | **53** | **73** | **108** |

This is a beautiful convergence pattern.

At:

\[
N=2000
\]

the medians reproduce the full-data thresholds essentially exactly.

---

# 3. Important Interpretation of the Smaller-N Results

Do **not** interpret:

\[
D_{95}=63\quad\text{at }N=500
\]

versus:

\[
D_{95}=73\quad\text{at }N=2300
\]

as evidence that dimensionality is unstable.

Finite-sample covariance spectra systematically change with sample size.

At smaller \(N\):

- covariance estimates are noisier;
- weak directions are less well estimated;
- low-variance spectral tails can contract;
- cumulative-variance thresholds can therefore occur at fewer components.

What matters is the trajectory:

\[
63
\rightarrow
69
\rightarrow
71
\rightarrow
73.
\]

That is **convergence**, not random wandering.

The same occurs for every variance threshold.

So the manuscript-safe interpretation is:

> **Variance-threshold dimensional summaries converged toward the canonical spectrum with increasing subsample size.**

Not:

> “All spectral dimensions were invariant to sample size.”

They weren't, and they do not need to be.

---

# 4. Effective Dimension Is Much More Stable

The participation-ratio effective dimension is:

### Canonical

\[
10.549.
\]

### Resampling means

\[
N=500:
10.198
\]

\[
N=1000:
10.535
\]

\[
N=1500:
10.492
\]

\[
N=2000:
10.564.
\]

That is extremely reassuring.

Already by:

\[
N=1000
\]

the average effective dimension is essentially indistinguishable descriptively from the canonical result.

And the variability shrinks substantially:

\[
SD:
0.724
\rightarrow
0.477
\rightarrow
0.205
\rightarrow
0.134.
\]

This is precisely what a stable population spectral quantity should look like.

---

# 5. PC1 Is Also Stable

Canonical:

\[
PC_1=0.28253.
\]

Subsample means:

\[
0.28605,\;
0.28156,\;
0.28289,\;
0.28223.
\]

There is no meaningful drift here.

Even at:

\[
N=500
\]

the average leading-PC contribution is close to the population estimate.

Therefore the large first principal component is not being generated by a small unusual subset.

---

# 6. Eigenspace Alignment Is the Strongest Part of the Resampling Result

This is more informative than simply comparing \(D_{95}\).

At \(N=500\):

\[
A_{5D}=0.931
\]

\[
A_{10D}=0.853
\]

\[
A_{20D}=0.813.
\]

Already respectable.

Then:

### \(N=1000\)

\[
0.975,\;
0.930,\;
0.889.
\]

### \(N=1500\)

\[
0.990,\;
0.974,\;
0.942.
\]

### \(N=2000\)

\[
0.997,\;
0.981,\;
0.983.
\]

So the leading morphology subspaces converge strongly toward the full-data PCA geometry.

Conceptually:

\[
\boxed{
\text{same major morphology directions reappear
when different subsets of sketches are used}
}
\]

That is a stronger result than merely saying the eigenvalues are similar.

---

# 7. The 5-D Space Is Especially Stable

Even at \(N=500\):

\[
\text{mean 5-D alignment}=0.931.
\]

By \(N=1500\):

\[
0.990.
\]

And by \(N=2000\):

\[
0.997.
\]

Therefore the strongest few population axes are extremely reproducible.

This agrees nicely with the effective dimension result:

\[
D_{\mathrm{eff}}\approx10.5.
\]

A relatively small number of major axes dominate the spectrum, while many weaker directions make up the long variance tail.

---

# 8. One Technical Point to Verify Before Freezing This Cell

The output says:

> PCA recomputed independently for every subsample.

Good.

But I want one implementation detail checked in the code:

### Was standardization also refitted inside every resampled subset?

Ideally each replicate should perform:

\[
X_{\text{sub}}
\]

\[
\downarrow
\]

`StandardScaler.fit(X_sub)`

\[
\downarrow
\]

PCA.

If instead the scaler means/SDs from all 2300 observations were reused, the result remains a useful perturbation analysis, but it is not a completely independent spectral refit.

This is **not a reason to rerun anything yet**.

Just inspect the code.

If scaler fitting occurred within each replicate, perfect.

If canonical scaling was intentionally frozen, describe the analysis as stability of the PCA spectrum **under a fixed canonical coordinate scaling**.

Either design can be valid; the manuscript wording should match the implementation.

---

# 9. NOW THE STRONGER TEST — REMOVE COMPLETE REPLICATION GROUPS

This is particularly important because the first resampling experiment samples individual observations.

If Clo-Sket contains related replicate sets, individual random subsampling can retain members from the same replication groups.

So you correctly added the stronger perturbation:

\[
\boxed{
\text{remove complete replication groups}
}
\]

with:

\[
5,\;10,\;20
\]

groups removed.

Since most groups contain 10 observations, this roughly removes:

\[
50,\;100,\;200
\]

sketches.

At the strongest condition, approximately:

\[
200/2300\approx8.7\%
\]

of the population is removed as complete provenance units.

Excellent control.

---

# 10. Variance-Threshold Dimensions Barely Move Under Group Removal

Canonical:

\[
D_{80}=32,\quad
D_{90}=53,\quad
D_{95}=73.
\]

After removing 5 groups:

\[
D_{80}=32,
\quad
D_{90}\approx53,
\quad
D_{95}=73.
\]

After removing 10 groups:

essentially the same.

After removing 20 complete groups:

\[
D_{80}\approx32.05,
\quad
D_{90}\approx53.05,
\quad
D_{95}\approx73.
\]

This is almost absurdly stable.

That is precisely what we wanted to know.

---

# 11. Eigenvalue Spectrum Is Essentially Identical

Mean eigenvalue-spectrum correlation:

### Remove 5 groups

\[
r=0.999986.
\]

### Remove 10 groups

\[
r=0.999953.
\]

### Remove 20 groups

\[
r=0.999939.
\]

That is extraordinarily high.

The spectral profile itself is virtually unchanged.

Therefore the PCA spectrum does not appear to be carried by a small collection of provenance groups.

---

# 12. Leading Eigenspaces Survive Group Removal

After removing **20 entire replication groups**:

\[
A_{5D}=0.99744
\]

\[
A_{10D}=0.98939
\]

\[
A_{20D}=0.99075.
\]

That is extremely strong.

So even after deleting roughly 200 related observations as coherent units:

\[
\boxed{
\text{the leading 20-dimensional morphology subspace
remains almost unchanged}
}
\]

under the alignment metric being used.

That is probably the single strongest spectral-robustness result in this notebook.

---

# 13. This Answers an Important Artefact Question

A reviewer could ask:

> Is the morphology spectrum simply caused by repeated or related Clo-Sket samples?

The group-removal result argues strongly against that explanation.

If a few replication groups were dominating PCA geometry, removing entire groups should cause:

- dimensional thresholds to shift;
- PC1 variance to move;
- eigenvalue profiles to change;
- eigenspace alignments to drop.

Instead, essentially none of those things happen.

Therefore we can say:

\[
\boxed{
\text{The leading spectral organization is robust to
complete removal of frozen replication groups.}
}
\]

That is a clean result.

---

# 14. But Be Precise About What This Does NOT Prove

It does not prove that replication has **zero** effect.

Nor does it prove that all observations are independent.

It tests influence:

> Does removal of plausible repeated-source units materially alter the global morphology spectrum?

Answer:

\[
\boxed{\text{apparently no, under these perturbations}.}
\]

That's enough.

---

# 15. This Result Is Stronger Than the Earlier Basin × Replication Result

Notice the difference.

Earlier:

\[
\text{replication group}
\leftrightarrow
\text{density basin}
\]

produced almost zero ARI.

Here:

\[
\text{remove replication groups}
\rightarrow
\text{recompute spectrum}
\]

shows near-perfect global spectral stability.

Together these imply something useful:

\[
\boxed{
\text{The global morphology spectrum is neither determined by
replication identities nor fragile to removal of replicate groups.}
}
\]

That is much more meaningful than trying to argue that individual replication groups must reproduce the same basin.

---

# 16. The Morphology Spectrum Now Has Three Layers of Evidence

We can now distinguish:

## Layer 1 — Canonical spectrum

\[
D_{80}=32,\;
D_{90}=53,\;
D_{95}=73,\;
D_{99}=108
\]

with:

\[
D_{\mathrm{eff}}\approx10.55.
\]

---

## Layer 2 — Observation resampling

Different random subsets recover progressively similar:

- variance-threshold dimensions;
- effective dimension;
- PC1 contribution;
- leading eigenspaces.

---

## Layer 3 — Provenance-group perturbation

Removing entire replication groups leaves:

- dimensional thresholds essentially unchanged;
- eigenvalue spectrum correlation \(>0.9999\);
- 5-D alignment \(\approx0.997\);
- 10-D alignment \(\approx0.989\);
- 20-D alignment \(\approx0.991\)

even under the strongest tested deletion.

That is a very solid robustness architecture.

---

# 17. What We Can Now Say About “Dimensionality”

There are three different words we must keep separate.

### Ambient dimension

\[
135.
\]

### PCA variance-retention dimension

\[
D_{95}=73.
\]

### Spectral effective dimension

\[
D_{\mathrm{eff}}\approx10.55.
\]

Do **not** convert any of these into:

> intrinsic manifold dimension = X.

We have not estimated that.

A manuscript-safe wording is:

> **The standardized 135-dimensional morphology representation exhibited a concentrated but extended eigenspectrum: the participation-ratio effective dimension was approximately 10.5, while 73 principal components were required to retain 95% of total variance.**

That is both interesting and correct.

---

# 18. A Useful Scientific Interpretation

The spectrum appears to contain:

\[
\boxed{
\text{a small set of dominant morphology directions}
}
\]

plus:

\[
\boxed{
\text{a substantial lower-variance tail}
}
\]

rather than either extreme:

### Not

\[
\text{one or two dimensions explain everything}
\]

and not

\[
\text{135 equally important dimensions}.
\]

That is consistent with a structured but morphologically rich sketch population.

Notice I said:

> structured.

Not:

> manifold.

Not:

> grammar.

Not yet.

---

# 19. Manuscript-Safe Result Paragraph

I would eventually write this approximately as:

> **The morphology eigenspectrum was stable under repeated observation-level and provenance-group perturbations. Across uniform subsamples of 500–2000 sketches, variance-retention dimensions and the participation-ratio effective dimension converged toward the full-sample estimates, while leading eigenspace alignment increased with sample size. At \(N=2000\), median \(D_{80}\), \(D_{90}\), \(D_{95}\), and \(D_{99}\) matched the canonical values of 32, 53, 73, and 108, respectively. Robustness was even stronger when complete provenance replication groups were removed: after deletion of 20 groups, eigenvalue-spectrum correlation remained approximately 0.99994 and mean 5-, 10-, and 20-dimensional eigenspace alignments were approximately 0.997, 0.989, and 0.991. These results indicate that the leading morphology spectrum is not strongly dependent on a small subset of sketches or replication groups.**

That is a strong result without exaggeration.

---

# 20. What This Adds to the Grammar-Discovery Story

Our evidence chain is now:

\[
\text{frozen morphology representation}
\]

\[
\downarrow
\]

\[
\text{stable morphology eigenspectrum}
\]

\[
\downarrow
\]

\[
\text{empirically derived local scales}
\]

\[
\downarrow
\]

\[
\text{stable density ranking}
\]

\[
\downarrow
\]

\[
\text{stable density-ascent basins}
\]

This is becoming genuine evidence for:

\[
\boxed{
\text{population-level quantitative morphology organization}
}
\]

rather than an artefact of:

- one PCA fit;
- one subset;
- one cluster algorithm;
- replication groups;
- category labels.

That is important.

---

# 21. Current Claim Boundary

## 🟢 SUPPORTED

1. The canonical morphology spectrum is reproducible under substantial random subsampling.

2. Variance-threshold dimensional summaries converge toward their canonical values with increasing sample size.

3. Participation-ratio effective dimensionality is stable under resampling.

4. The leading PCA eigenspaces are strongly reproducible.

5. Removal of complete provenance replication groups produces negligible changes in the global morphology spectrum.

6. The spectral organization is therefore unlikely to be driven primarily by a small subset of observations or a small set of replication groups.

---

## 🟡 SUPPORTED WITH QUALIFICATION

> The morphology representation exhibits robust low-order spectral organization.

Yes.

But "low-order" should refer to the dominant part of the eigenspectrum, not claim that the entire 135-D structure is truly low-dimensional.

---

## 🔴 NOT SUPPORTED

- intrinsic manifold dimension = 10.55;
- intrinsic manifold dimension = 73;
- morphology states;
- universal latent states;
- hierarchy;
- morphology grammar;
- compositional rules;
- semantic primitives;
- category-free garment semantics.

---

# 22. Do We Need More Spectral Robustness Experiments?

## No.

I would stop here.

You now have:

- sample-size sensitivity;
- repeated subsampling;
- effective dimension stability;
- eigenspace stability;
- complete replication-group removal.

Adding bootstrap PCA, jackknife PCA, another random seed battery, another eigenspace metric, etc. would mostly become robustness inflation.

The spectral question is answered.

# 🟢 FREEZE SPECTRAL ROBUSTNESS

The next useful thing is to return to the actual scientific discovery question:

\[
\boxed{
\text{What morphology distinguishes the stable density basins?}
}
\]

But before using category labels or naming anything, we should inspect basin morphology **from the 135-D representation itself**.

That is where we find out whether these stable basins correspond to visibly and quantitatively different morphology — or whether they are mathematically stable partitions with little interpretable geometric distinction.

And yes:

> **CNN / NN can remain outside the door. 😂🚪**

# CLO-SKET — MORPHOLOGY DISCOVERY
## Mode Consensus + Feature Contribution + Structural Influence Audit

### Overall verdict

# 🟢 CROSS-SCALE MORPHOLOGY ORGANIZATION IS REPRODUCIBLE
# 🟢 LOCAL BASIN COHERENCE IS SUPPORTED
# 🔴 GLOBAL CLUSTER COMPACTNESS IS NOT SUPPORTED
# 🟢 MORPHOLOGY GEOMETRY IS DISTRIBUTED ACROSS FEATURE BLOCKS
# 🟢 NO SINGLE FEATURE DOMINATES THE STRUCTURE
# 🟡 THIS SUPPORTS MULTISCALE MORPHOLOGY ORGANIZATION, NOT DISCRETE STATES
# 🔴 A FORMAL MORPHOLOGY GRAMMAR IS STILL NOT ESTABLISHED

The current results substantially clarify the structure of the frozen 135-D morphology representation.

The evidence no longer supports thinking of the discovered density basins as conventional globally compact clusters.

Instead, the morphology space is better described as:

\[
\boxed{
\text{continuous morphology geometry}
+
\text{recurrent multiscale density organization}
}
\]

with strong local consistency but weak global basin separation.

---

# 1. CROSS-SCALE MORPHOLOGY CONSENSUS

The six independently derived observational scales produce:

\[
7,\;6,\;5,\;7,\;7,\;8
\]

density-ascent basins.

Pairwise cross-scale ARI ranges from:

\[
0.4983
\]

to:

\[
0.9262.
\]

The overall summary is:

\[
\text{Mean pairwise ARI}=0.7343
\]

\[
\text{Median pairwise ARI}=0.7553
\]

\[
\text{Adjacent-scale mean ARI}=0.8764.
\]

Therefore the partitions are neither identical nor unrelated.

The most defensible interpretation is:

\[
\boxed{
\text{persistent broad morphology organization}
+
\text{scale-dependent refinement}
}
\]

This is stronger than a single-scale clustering result because the organization recurs across independently defined observational scales.

---

# 2. PAIRWISE CO-MEMBERSHIP SUPPORTS PERSISTENCE

For every pair of sketches, cross-scale co-membership measures the fraction of the six scales for which the pair belongs to the same density basin.

The median pairwise co-membership is:

\[
0.8333
=
\frac{5}{6}.
\]

The persistence distribution is:

\[
P(C_{ij}\ge1.00)=0.4991
\]

\[
P(C_{ij}\ge0.8333)=0.5347
\]

\[
P(C_{ij}\ge0.6667)=0.5680
\]

\[
P(C_{ij}\ge0.50)=0.6093.
\]

Thus a large fraction of sketch pairs retain the same broad structural relationship across most or all observational scales.

Importantly:

> no consensus clustering was created from this matrix.

Therefore cross-scale co-membership remains a validation statistic rather than becoming another mechanism for imposing a preferred state count.

---

# 3. DO NOT TURN THE CONSENSUS INTO A MORPHOLOGY STATE COUNT

The current evidence does **not** justify declaring:

\[
K=5,\;6,\;7,\;\text{or }8
\]

as the number of morphology states.

The basin count changes with observational scale:

\[
5\rightarrow8.
\]

Therefore the correct result is:

\[
\boxed{
\text{density organization persists}
}
\]

not:

\[
\boxed{
\text{a unique discrete state count has been discovered}
}
\]

No preferred scale should be selected because it produces a visually attractive partition.

---

# 4. WITHIN-REGION MORPHOLOGY COHERENCE CHANGES THE INTERPRETATION

The basin-coherence analysis provides an important negative result.

Across all six scales:

\[
d_{\text{within}}
>
d_{\text{between}}.
\]

The mean within/between ratio is:

\[
1.05505.
\]

And:

\[
0/6
\]

scales satisfy:

\[
d_{\text{within}}<d_{\text{between}}.
\]

Therefore the density-ascent basins are **not globally compact morphology clusters**.

This result should be preserved rather than repaired.

---

# 5. LOCAL COHERENCE IS STRONG DESPITE WEAK GLOBAL SEPARATION

Although global distance separation fails, local-neighbor retention remains high.

Across scales:

\[
0.7550
\rightarrow
0.7743
\rightarrow
0.8035
\rightarrow
0.8039
\rightarrow
0.8433
\rightarrow
0.8447.
\]

The overall mean local-neighbor retention is:

\[
0.8041.
\]

Therefore:

\[
\boxed{
\text{basin membership preserves local morphology neighborhoods}
}
\]

even though:

\[
\boxed{
\text{basins are not globally compact Euclidean clusters}.
}
\]

These are different geometric questions and should remain separate.

---

# 6. CURRENT BASIN INTERPRETATION

The strongest interpretation is now:

\[
\boxed{
\text{density catchments embedded within an extended continuous morphology geometry}
}
\]

rather than:

\[
\boxed{
\text{isolated compact clusters}.
}
\]

This explains how two sketches may belong to the same density-ascent basin while still being farther apart than two sketches lying close to a boundary between different basins.

Thus:

\[
B(x_i)=B(x_j)
\]

does not imply:

\[
d(x_i,x_j)
<
d(x_i,x_k)
\]

for every sketch \(x_k\) in another basin.

---

# 7. FEATURE-GRADIENT ANALYSIS

The next question is:

> Which measurable morphology properties participate most strongly in this continuous geometry?

The strongest local gradients occur in several global descriptors:

\[
\text{aspect ratio}=0.1098
\]

\[
\text{centroid}_x=0.1061
\]

\[
\text{bbox width}=0.1037
\]

\[
\text{bbox height}=0.1027
\]

\[
\text{centroid}_y=0.0952.
\]

This indicates that coarse geometric properties change relatively rapidly along local morphology neighborhoods.

However, local gradient and global morphology-distance association are different quantities.

---

# 8. FEATURE–DISTANCE ASSOCIATIONS

The strongest individual morphology-distance associations are:

\[
\rho_{\text{foreground fraction}}=0.6940
\]

and:

\[
\rho_{\text{symmetry}}=0.6175.
\]

Several occupancy coordinates also show substantial association:

\[
|\rho|\approx0.44-0.50.
\]

At the block level:

\[
\overline{|\rho|}_{vertical}=0.2958
\]

\[
\overline{|\rho|}_{horizontal}=0.2841
\]

\[
\overline{|\rho|}_{global}=0.2413.
\]

This suggests two simultaneous forms of representation:

1. several global descriptors provide strong individual geometric signals;
2. occupancy information is distributed across many coordinates.

Therefore the geometry is not reducible to one dominant descriptor.

---

# 9. LOCAL GRADIENT BLOCK SUMMARY

Mean local gradient by block:

\[
\text{global descriptors}=0.0864
\]

\[
\text{horizontal occupancy}=0.0537
\]

\[
\text{vertical occupancy}=0.0519.
\]

Thus global descriptors exhibit stronger average local variation.

But this should not be interpreted as saying that global descriptors are globally more important to the morphology geometry.

That question requires perturbation.

---

# 10. WHOLE-BLOCK STRUCTURAL PERTURBATION

The canonical standardized 135-D space has:

\[
NN_{\text{overlap}}=0.8632
\]

relative to the frozen 73-D PCA reference.

Removing each block gives:

### Remove horizontal occupancy

\[
NN_{\text{overlap}}=0.3269
\]

\[
NN_{\text{loss}}=0.5363.
\]

### Remove vertical occupancy

\[
NN_{\text{overlap}}=0.4224
\]

\[
NN_{\text{loss}}=0.4408.
\]

### Remove global descriptors

\[
NN_{\text{overlap}}=0.6819
\]

\[
NN_{\text{loss}}=0.1813.
\]

Therefore all three feature blocks contribute to preservation of local morphology neighborhoods.

The occupancy blocks produce the largest perturbations.

---

# 11. IMPORTANT BLOCK-SIZE CAUTION

The occupancy blocks contain:

\[
64
\]

features each.

The global descriptor block contains only:

\[
7.
\]

Therefore the raw perturbation magnitudes cannot be used to claim:

> horizontal occupancy is intrinsically more important than global descriptors.

Removing 64 coordinates is a much larger intervention than removing seven.

The safe conclusion is:

\[
\boxed{
\text{occupancy blocks collectively make substantial contributions to local geometry}
}
\]

while:

\[
\boxed{
\text{global descriptors also contribute measurable non-redundant structure}.
}
\]

A dimension-matched perturbation would be required only if the paper attempted to rank block importance quantitatively.

That ranking is not necessary for the current scientific claim.

---

# 12. INDIVIDUAL FEATURE PERTURBATION SHOWS DISTRIBUTED STRUCTURE

The largest individual-feature NN loss is:

\[
0.008043
\]

for:

```text
vertical_occupancy_19

# CLO-SKET — MORPHOLOGY DISCOVERY
## Block Complementarity + Spatial Locality + Transition + Graph-Geodesic Audit

### Overall verdict

# 🟢 HORIZONTAL / VERTICAL / GLOBAL BLOCKS ARE STRUCTURALLY COMPLEMENTARY
# 🟢 OCCUPANCY COORDINATE ORDER CONTAINS STRONG SPATIAL LOCALITY
# 🟡 LOCAL MORPHOLOGY CONTINUITY IS SUPPORTED
# 🔴 COHERENT DIRECTIONAL TRAJECTORIES ARE NOT SUPPORTED
# 🟢 THE k=10 MORPHOLOGY GRAPH IS FULLY CONNECTED AND TRAVERSABLE
# 🟢 EUCLIDEAN AND GRAPH-GEODESIC ORDERING ARE STRONGLY CONSISTENT
# 🔴 NONE OF THIS YET ESTABLISHES A MANIFOLD OR A MORPHOLOGY GRAMMAR

Bro, these four shields are very useful because they answer four different structural questions without changing the frozen representation:

1. **Do the three morphology blocks carry complementary local information?**
2. **Is the spatial ordering of the occupancy coordinates meaningful?**
3. **Do local neighborhoods support coherent progression through morphology space?**
4. **Does the local graph form a globally traversable geometric structure?**

The answers are not all equally strong.

The result is now becoming quite precise:

\[
\boxed{
\text{distributed continuous morphology geometry}
}
\]

with:

\[
\boxed{
\text{strong local spatial organization}
}
\]

and:

\[
\boxed{
\text{globally connected graph structure}
}
\]

but without evidence for:

\[
\boxed{
\text{directed morphology trajectories}.
}
\]

That distinction is scientifically important.

---

# 1. BLOCK COMPLEMENTARITY

The frozen 135-D morphology consists of:

\[
H=64
\]

horizontal occupancy coordinates,

\[
V=64
\]

vertical occupancy coordinates,

and:

\[
G=7
\]

global descriptors.

The reference geometry is the frozen 73-D PCA morphology space.

Nearest-neighbor recovery gives:

| Representation | Features | Mean NN overlap |
|---|---:|---:|
| H only | 64 | 0.2978 |
| V only | 64 | 0.2273 |
| G only | 7 | 0.1152 |
| H + V | 128 | 0.6819 |
| H + G | 71 | 0.4224 |
| V + G | 71 | 0.3269 |
| H + V + G | 135 | 0.8632 |

This is a very clear structural result.

---

# 2. HORIZONTAL AND VERTICAL OCCUPANCY ARE NOT REDUNDANT

If the horizontal and vertical occupancy profiles encoded essentially the same local morphology information, then:

\[
NN(H+V)
\]

would be close to:

\[
\max(NN(H),NN(V)).
\]

Instead:

\[
NN(H)=0.2978
\]

\[
NN(V)=0.2273
\]

but:

\[
NN(H+V)=0.6819.
\]

The gain over the stronger individual block is:

\[
0.6819-0.2978
=
0.3841.
\]

That is substantial.

Therefore:

\[
\boxed{
H \text{ and } V
\text{ contain complementary information about local morphology geometry.}
}
\]

This is one of the strongest interpretable representation-level findings in the notebook.

---

# 3. GLOBAL DESCRIPTORS ADD FURTHER INFORMATION

The occupancy combination gives:

\[
NN(H+V)=0.6819.
\]

Adding the seven global descriptors gives:

\[
NN(H+V+G)=0.8632.
\]

Therefore:

\[
\Delta NN_G
=
0.1813.
\]

Despite containing only seven coordinates, the global descriptor block measurably improves recovery of the frozen local geometry.

Thus:

\[
\boxed{
G
\text{ contributes structural information not fully represented by occupancy alone.}
}
\]

This agrees with the previous feature-gradient analysis, where several global descriptors had strong individual geometric associations.

---

# 4. THE FULL MORPHOLOGY REPRESENTATION IS GENUINELY MULTI-BLOCK

The current evidence argues strongly against either extreme:

\[
\text{occupancy alone is sufficient}
\]

or:

\[
\text{global descriptors alone are sufficient}.
\]

Instead:

\[
H+V+G
>
H+V
>
H,\;V,\;G.
\]

The safest interpretation is:

\[
\boxed{
\text{the canonical representation integrates complementary spatial and global morphology information.}
}
\]

This is structural complementarity.

It is **not** information-theoretic independence.

---

# 5. ONE CAUTION ABOUT THE “NORMALIZED COMPLEMENTARITY” VALUES

You report:

\[
H\rightarrow H+V=0.5470
\]

\[
V\rightarrow H+V=0.5883
\]

\[
H+V\rightarrow H+V+G=0.5700.
\]

These can be retained as descriptive normalized gains if their denominator is clearly defined in Methods.

But they should not become primary evidence unless the normalization equation is written explicitly.

The raw overlaps and raw gains are already sufficient and easier for a reviewer to interpret.

---

# 6. BLOCK COMPLEMENTARITY CLAIM BOUNDARY

## 🟢 Supported

- H and V provide complementary local geometry information.
- G contributes additional neighborhood-recovery information beyond H+V.
- The complete 135-D representation best recovers the frozen morphology neighborhood structure.

## 🔴 Not supported

- statistical independence of H, V and G;
- causal contribution;
- semantic importance;
- semantic primitives;
- orthogonal morphology factors.

---

# 7. SPATIAL ORDER / LOCALITY — THIS RESULT IS VERY STRONG

Now we test something fundamentally different.

The occupancy coordinates are ordered spatially.

The question is:

> Does that ordering contain actual local organization, or are the 64 coordinates merely an unordered list of features?

For horizontal occupancy:

\[
\text{observed adjacent correlation}=0.7726.
\]

The randomized-order null gives:

\[
\text{null mean}=0.2049.
\]

For vertical occupancy:

\[
\text{observed}=0.7432
\]

versus:

\[
\text{null mean}=0.2330.
\]

These are enormous separations.

---

# 8. ADJACENT DIFFERENCES TELL THE SAME STORY

Horizontal:

\[
D_{\text{adj,obs}}=0.2712
\]

versus:

\[
D_{\text{adj,null}}=0.7258.
\]

Vertical:

\[
D_{\text{adj,obs}}=0.3080
\]

versus:

\[
D_{\text{adj,null}}=0.6994.
\]

Thus adjacent spatial coordinates are much more similar than arbitrary shuffled coordinate neighbors.

The relative reduction is:

\[
62.6\%
\]

for horizontal occupancy and:

\[
56.0\%
\]

for vertical occupancy.

That is strong evidence of spatial smoothness.

---

# 9. THE PERMUTATION DESIGN IS CORRECT

This is an important methodological point.

You correctly recognized that globally permuting feature columns does not change Euclidean distances if the same permutation is applied consistently.

Therefore this shield does **not** pretend that coordinate reordering perturbs Euclidean morphology geometry.

Instead it directly tests:

\[
\boxed{
\text{adjacency structure along the ordered occupancy profile}.
}
\]

The null preserves the feature values but destroys their spatial positions.

That is exactly the appropriate null for the question.

---

# 10. SPATIAL-ORDER RESULT

The empirical values lie far outside the permutation null:

\[
p=0.009901
\]

for both adjacency-difference and adjacency-correlation tests in both H and V.

With 100 permutations, that is the smallest attainable empirical value under the usual:

\[
\frac{b+1}{B+1}
\]

formula.

Therefore the proper wording is not:

> \(p<0.01\) with arbitrary precision.

It is:

> **empirical permutation \(p=0.0099\), with 100 permutations.**

---

# 11. WHAT THIS MEANS SCIENTIFICALLY

This is now direct evidence that:

\[
\boxed{
\text{occupancy morphology is spatially ordered rather than exchangeable across position.}
}
\]

That is important because occupancy measurements were not merely useful as 128 independent scalar coordinates.

Their **spatial arrangement itself** contains organized structure.

That moves the interpretation from:

\[
\text{bag of occupancy measurements}
\]

toward:

\[
\boxed{
\text{ordered morphology profiles}.
}
\]

Still not semantic primitives.

But definitely spatial organization.

---

# 12. TRANSITION STRUCTURE — HERE WE NEED TO BE MUCH MORE CONSERVATIVE

Now to the trajectory shield.

This is where the result becomes more mixed.

Nearest-neighbor distance:

\[
\text{median}=5.225.
\]

Non-backtracking two-hop distance:

\[
\text{median}=6.287.
\]

So:

\[
\frac{d_{2hop,NB}}{d_{1hop}}
\approx1.190.
\]

This indicates relatively modest expansion over two local graph steps.

That is compatible with local continuity.

---

# 13. LOCAL SCALE IS ALSO FAIRLY STABLE

The local scale ratio has:

\[
\text{median}=0.872
\]

\[
Q_{05}=0.648
\]

\[
Q_{95}=1.069.
\]

So neighboring observations often experience local neighborhood scales of similar order.

This again supports:

\[
\boxed{
\text{local geometric continuity}.
}
\]

---

# 14. BUT NEIGHBORHOOD OVERLAP IS ONLY MODERATE

Mean local transition neighborhood overlap is:

\[
0.304.
\]

Median:

\[
0.30.
\]

So when moving from a sketch to its nearest neighbor, the two observations share only about 30% of their local neighborhood membership on average.

That is not particularly high.

It is consistent with:

\[
\text{locally structured but heterogeneous geometry}.
\]

It does not suggest a smooth one-dimensional pathway.

---

# 15. THE MOST IMPORTANT TRANSITION RESULT IS NEGATIVE

Non-backtracking directional consistency is:

\[
\text{mean cosine}=-0.1734
\]

\[
\text{median}=-0.1873.
\]

This is extremely important.

If local transitions formed coherent directional trajectories, we would expect:

\[
\cos(\theta)>0
\]

on average.

Instead:

\[
\boxed{
\cos(\theta)<0.
}
\]

So after immediate backtracking has already been excluded, successive local movement tends to bend back rather than continue forward.

Therefore the evidence does **not** support:

\[
\boxed{
\text{coherent directional morphology trajectories}.
}
\]

---

# 16. DO NOT TURN THE TRANSITION RESULT INTO A GRAMMAR ARGUMENT

The correct interpretation is:

\[
\boxed{
\text{local continuity exists}
}
\]

but:

\[
\boxed{
\text{persistent directional progression does not.}
}
\]

This is actually valuable because it prevents us from forcing a trajectory narrative onto the morphology geometry.

The local graph behaves more like a connected neighborhood network than a set of directed developmental paths.

---

# 17. THE IMMEDIATE BACKTRACKING RESULT

You report:

\[
22.96\%
\]

immediate backtracking under the naive two-step nearest-neighbor walk.

That confirms why the non-backtracking correction was necessary.

The corrected implementation is scientifically better because:

\[
i\rightarrow j\rightarrow i
\]

contains no evidence of forward transition.

Removing that artifact was absolutely the right choice.

---

# 18. TRANSITION CLAIM BOUNDARY

## 🟢 Supported

- nearest-neighbor steps are local;
- non-backtracking two-hop expansion is modest;
- local neighborhood scales are reasonably stable.

## 🟡 Supported with qualification

> Local morphology geometry exhibits continuity.

Yes, descriptively.

## 🔴 Not supported

- directed morphology trajectories;
- monotonic transformation paths;
- progression rules;
- grammar transitions;
- state-transition dynamics.

The negative directional cosine is particularly important here.

---

# 19. GRAPH GEODESIC RESULT — VERY CLEAN

The kNN graph uses:

\[
k=10
\]

with:

\[
2300
\]

nodes and:

\[
19534
\]

undirected edges.

Connectivity:

\[
\text{components}=1.
\]

Largest component:

\[
2300.
\]

Reachability:

\[
100\%.
\]

Therefore:

\[
\boxed{
\text{the complete morphology population forms one connected local-neighborhood graph at }k=10.
}
\]

This is a strong descriptive result.

---

# 20. GEODESIC PATHS ARE LONGER THAN DIRECT EUCLIDEAN SEPARATION

Median global stretch:

\[
\frac{d_G}{d_E}
=
1.902.
\]

Mean:

\[
1.911.
\]

Thus local graph paths are approximately twice the direct Euclidean distance for a typical sampled pair.

This tells us the graph does not simply reproduce straight-line Euclidean connections.

But:

\[
\boxed{
\text{stretch}>1
}
\]

alone is not evidence for curvature of a manifold.

Graph paths are constrained to kNN edges, so stretch greater than one is expected.

---

# 21. LOCAL STRETCH IS SIMILAR TO GLOBAL STRETCH

Local median:

\[
1.867.
\]

Global median:

\[
1.902.
\]

That is interesting.

It suggests the path inflation is not restricted only to very distant observations.

Even local-to-intermediate paths are substantially longer when forced through the kNN graph.

But again this is a graph property, not automatically a manifold property.

---

# 22. EUCLIDEAN–GEODESIC RANK AGREEMENT IS THE STRONGER RESULT

Mean Spearman:

\[
\rho=0.8687.
\]

Median:

\[
\rho=0.9029.
\]

Even the 5th percentile is:

\[
0.6656.
\]

Therefore observations that are closer in Euclidean morphology space are generally also closer under local graph-geodesic distance.

That is a strong consistency result.

Thus:

\[
\boxed{
\text{direct and graph-based notions of morphology separation are substantially concordant.}
}
\]

This is much more meaningful than stretch alone.

---

# 23. WHAT THE GRAPH RESULT SUPPORTS

The combined graph evidence is:

\[
\text{one connected component}
\]

\[
+
\]

\[
\text{complete reachability}
\]

\[
+
\]

\[
\text{high Euclidean–geodesic rank agreement}.
\]

Therefore:

\[
\boxed{
\text{morphology space is globally traversable through local neighborhoods at }k=10.
}
\]

That is a precise and defensible statement.

---

# 24. BUT k=10 IS STILL A CHOICE

The notebook correctly acknowledges this.

Connectivity of a kNN graph can depend heavily on:

\[
k.
\]

Therefore:

\[
\text{connected at }k=10
\]

does not imply:

\[
\text{connected for all reasonable }k.
\]

If graph connectivity/path coherence becomes a central manuscript claim, then a small sensitivity audit across, for example:

\[
k=5,\;10,\;15,\;20
\]

would be scientifically justified.

But do **not** run that automatically if the notebook already contains such a shield later.

First inspect the remaining cells.

---

# 25. THE FOUR SHIELDS NOW FIT TOGETHER BEAUTIFULLY

We have:

## Block complementarity

\[
H,\;V,\;G
\]

provide complementary recovery of local morphology structure.

---

## Spatial locality

The ordered occupancy profiles contain strong adjacent-position organization.

---

## Transition analysis

Local neighborhoods show continuity but **not coherent directional progression**.

---

## Graph-geodesic analysis

The population nevertheless forms one globally traversable local-neighborhood network.

Therefore the morphology organization is best summarized as:

\[
\boxed{
\text{connected}
+
\text{locally continuous}
+
\text{spatially organized}
+
\text{non-directional}
}
\]

rather than:

\[
\boxed{
\text{a sequence of discrete states connected by directed transformations}.
}
\]

That is a major conceptual clarification.

---

# 26. UPDATED STRUCTURAL MODEL OF CLO-SKET MORPHOLOGY

The accumulated evidence now favors:

\[
\text{Frozen 135-D morphology}
\]

\[
\downarrow
\]

\[
\text{stable distributed eigenspectrum}
\]

\[
\downarrow
\]

\[
\text{complementary H/V/G feature blocks}
\]

\[
\downarrow
\]

\[
\text{ordered spatial occupancy structure}
\]

\[
\downarrow
\]

\[
\text{continuous local neighborhoods}
\]

\[
\downarrow
\]

\[
\text{recurrent density basins across scale}
\]

\[
\downarrow
\]

\[
\text{globally connected morphology graph}
\]

but:

\[
\boxed{
\text{no globally compact state structure}
}
\]

and:

\[
\boxed{
\text{no coherent directional trajectories}.
}
\]

This is becoming a very consistent geometry story.

---

# 27. WHAT THIS MEANS FOR THE “GRAMMAR” HYPOTHESIS

At this point, bro, I would **not** move the claim toward grammar.

Actually the transition test gives us evidence against one easy path to grammar.

We do not see:

\[
A\rightarrow B\rightarrow C
\]

style directional morphology progression.

Instead we see:

\[
\boxed{
\text{continuous connected organization without preferred directional flow}.
}
\]

That does not rule out every conceivable grammar.

But it means the current geometry does not provide evidence for a transition-rule grammar.

So the scientifically strongest story remains:

\[
\boxed{
\text{quantitative morphology organization}
}
\]

not:

\[
\boxed{
\text{morphology grammar}.
}
\]

---

# 28. UPDATED EVIDENCE LEDGER

| Scientific question | Evidence | Decision |
|---|---|---|
| Do H and V encode complementary structure? | H/V/H+V NN recovery | 🟢 Supported |
| Does G add beyond occupancy? | H+V vs H+V+G | 🟢 Supported |
| Is occupancy coordinate order spatially meaningful? | adjacency permutation null | 🟢 Strongly supported |
| Is morphology locally continuous? | two-hop expansion + scale continuity | 🟢 Supported descriptively |
| Do neighborhoods strongly overlap under one-step movement? | mean overlap ≈ 0.304 | 🟡 Moderate only |
| Do local steps continue directionally? | cosine ≈ -0.173 | 🔴 Not supported |
| Are coherent trajectories established? | transition analysis | 🔴 No |
| Is the k=10 graph connected? | 1 component / 2300 nodes | 🟢 Supported |
| Is every node reachable? | reachable fraction = 1 | 🟢 Supported |
| Are Euclidean and geodesic orderings consistent? | median Spearman ≈ 0.903 | 🟢 Strongly supported |
| Does stretch prove a manifold? | stretch ≈ 1.90 | 🔴 No |
| Is a formal morphology grammar established? | total evidence | 🔴 No |

---

# 29. MANUSCRIPT-SAFE SYNTHESIS

A conservative but strong paragraph would be:

> **The frozen morphology representation exhibits complementary structure across horizontal occupancy, vertical occupancy, and global descriptors. Combining horizontal and vertical occupancy substantially improved recovery of the reference local-neighborhood geometry, while global descriptors provided an additional increment. The spatial ordering of occupancy measurements was itself highly organized: adjacent occupancy coordinates were substantially more similar and more strongly correlated than under spatial-order permutation. Local graph analysis indicated modest two-hop expansion and stable local scale, supporting neighborhood continuity, but non-backtracking directional consistency was negative, providing no evidence for coherent directional morphology trajectories. Nevertheless, the k=10 morphology graph formed a single connected component with complete reachability, and Euclidean and graph-geodesic distances showed strong rank agreement. Together, these results support a connected, locally organized and spatially structured morphology geometry without implying discrete states, directed transformation rules, or a mathematical manifold.**

---

# 30. WHAT SHOULD BE FROZEN

## 🟢 FREEZE

### Block complementarity

- H only
- V only
- G only
- H+V
- H+G
- V+G
- H+V+G

### Spatial locality

- adjacent differences
- adjacent correlations
- permutation-null results

### Transition analysis

- one-step distance
- neighborhood overlap
- two-hop expansion
- non-backtracking expansion
- scale continuity
- negative directional-consistency result

### Graph-geodesic analysis

- connectivity
- reachability
- stretch
- Euclidean–geodesic rank agreement

Do not “improve” the negative transition result.

It is scientifically valuable.

---

# 31. CURRENT HIGH-LEVEL CONCLUSION

We can now say:

# 🟢 MORPHOLOGY GEOMETRY IS DISTRIBUTED
# 🟢 FEATURE BLOCKS ARE STRUCTURALLY COMPLEMENTARY
# 🟢 OCCUPANCY COORDINATES HAVE STRONG SPATIAL ORDER
# 🟢 LOCAL MORPHOLOGY GEOMETRY IS CONTINUOUS
# 🟢 THE k=10 GRAPH IS GLOBALLY TRAVERSABLE
# 🟢 DIRECT AND GRAPH DISTANCES ARE STRONGLY CONSISTENT
# 🔴 DIRECTIONAL TRAJECTORIES ARE NOT OBSERVED
# 🔴 DISCRETE MORPHOLOGY STATES ARE NOT ESTABLISHED
# 🔴 A FORMAL MORPHOLOGY GRAMMAR IS NOT ESTABLISHED
# 🔴 A MATHEMATICAL MANIFOLD IS NOT ESTABLISHED

The evidence is converging on something cleaner than the original “grammar” hypothesis:

\[
\boxed{
\textbf{CLO-SKET contains a robust, distributed,
spatially organized, multiscale continuous morphology geometry.}
}
\]

That is already a substantial scientific result.

# CLO-SKET — MORPHOLOGY DISCOVERY
## Region–Feature Consistency + Permutation Null + Cross-Scale Generalization Audit

### Overall verdict

# 🟢 DENSITY REGIONS HAVE REPRODUCIBLY DIFFERENT QUANTITATIVE FEATURE PROFILES
# 🟢 THE STRONGEST REGIONAL DIFFERENCES ARE NOT EXPLAINED BY REGION SIZE ALONE
# 🟡 GLOBAL REGION-LEVEL SIGNAL WEAKENS AT COARSER OBSERVATIONAL SCALES
# 🟢 SEVERAL INDIVIDUAL FEATURES SHOW REPEATED NON-RANDOM REGIONAL ASSOCIATION
# 🟢 THE IDENTITY OF REGION-DISCRIMINATING FEATURE TYPES IS HIGHLY STABLE ACROSS SCALE
# 🔴 WITHIN-REGION VARIATION REMAINS LARGER THAN BETWEEN-REGION CENTROID SEPARATION
# 🚨 THE FINAL CROSS-SCALE GENERALIZATION METRIC REQUIRES A CODE AUDIT BEFORE ACCEPTANCE

These shields add an important layer to the morphology result.

The previous analyses established that density-defined organization recurs across scale.

The present question is different:

> **When those density regions occur, are they associated with reproducibly different measurable morphology profiles?**

The answer is:

\[
\boxed{\text{Yes — but with important qualifications.}}
\]

The strongest defensible conclusion is not that the basins are compact morphology states.

Rather:

\[
\boxed{
\text{density organization is associated with reproducible quantitative shifts in morphology features}
}
\]

inside a geometry that still contains substantial within-region variation.

---

# 1. REGION PROFILES ARE MEASURABLY DIFFERENT

Across the six observational scales, the mean pairwise distance between regional feature centroids is remarkably stable:

\[
5.25 \text{ to } 5.49.
\]

The overall mean is:

\[
\boxed{5.333}
\]

and the nearest regional-profile distances remain approximately:

\[
3.28 \text{ to } 3.91.
\]

So independently discovered density regions do not all collapse onto essentially identical 135-D feature centroids.

There is measurable regional differentiation.

---

# 2. BUT THE REGIONS ARE NOT COMPACT FEATURE CLUSTERS

This qualification is critical.

Mean within-region morphology dispersion is:

\[
\boxed{9.589}
\]

while mean between-region centroid separation is:

\[
\boxed{5.333}.
\]

Therefore:

\[
\frac{\text{between}}{\text{within}}
=
0.556.
\]

And this ratio remains tightly constrained across all six scales:

\[
0.550-0.568.
\]

Thus:

\[
\boxed{
\text{within-region variation is substantially larger than separation among region centroids.}
}
\]

This agrees extremely well with the earlier geometry story.

The basins can have different **average quantitative profiles** without behaving like tight discrete morphology categories.

That distinction must remain explicit.

---

# 3. THIS ACTUALLY STRENGTHENS THE CONTINUOUS-GEOMETRY INTERPRETATION

We now have two observations simultaneously:

\[
\text{regional centroids differ}
\]

but:

\[
\text{regional dispersion} > \text{centroid separation}.
\]

Therefore the geometry is more consistent with:

\[
\boxed{
\text{overlapping quantitative morphology regions embedded in a continuous space}
}
\]

than with:

\[
\boxed{
\text{well-separated discrete morphology states}.
}
\]

This is an important result rather than a failure of the basin analysis.

---

# 4. WHICH FEATURES DIFFER MOST BETWEEN REGIONS?

The strongest region-discriminating measurements include:

- `bbox_width`
- `aspect_ratio`
- `centroid_x`
- several edge/near-edge horizontal occupancy coordinates
- several vertical occupancy coordinates
- `centroid_y`
- `bbox_height`
- `symmetry`
- `foreground_fraction`

The feature-block summary is particularly informative:

| Feature block | Mean discrimination | Median |
|---|---:|---:|
| Global descriptors | 0.5179 | 0.4421 |
| Horizontal occupancy | 0.3130 | 0.3403 |
| Vertical occupancy | 0.2644 | 0.2908 |

So the strongest average regional differentiation occurs among the seven global descriptors.

But that should **not** be interpreted as saying that global descriptors define the entire geometry.

Previous perturbation and complementarity shields already showed that occupancy information is structurally essential.

These are different questions:

\[
\text{regional discrimination}
\neq
\text{total geometric contribution}.
\]

---

# 5. `bbox_width` IS PARTICULARLY CONSISTENT

`bbox_width` has:

\[
\text{median discrimination}=0.7726.
\]

It is the strongest feature in the regional-profile ranking.

More importantly, the permutation analysis later gives:

\[
\text{median }z=6.965
\]

with:

\[
6/6
\]

scales satisfying the nominal permutation threshold.

That makes width-related variation one of the most reproducible measurable properties associated with density-region organization.

Still:

\[
\boxed{
\text{bbox width is an associated measurable property, not a semantic primitive.}
}
\]

---

# 6. CROSS-SCALE FEATURE-DISCRIMINATION STABILITY IS STRONG

The first shield compares the **magnitude of regional differentiation by feature** between adjacent scales.

The Spearman correlations are:

\[
0.988,\;
0.902,\;
0.920,\;
0.971,\;
0.965.
\]

Mean:

\[
\boxed{\rho=0.949}.
\]

This is strong evidence that although the basin partitions change with observational scale, similar measurable morphology properties repeatedly become important for distinguishing them.

This is a very useful result.

It means:

\[
\boxed{
\text{scale changes regional partitioning more than it changes which feature families participate in that partitioning.}
}
\]

---

# 7. THE PERMUTATION NULL IS THE KEY VALIDATION

The null preserves:

- number of regions;
- exact region-size distribution;
- overall feature distributions;

while destroying:

\[
\text{actual morphology} \leftrightarrow \text{basin membership}.
\]

That is a sensible null for the question being asked.

It directly tests whether observed regional feature differentiation exceeds what would arise from arbitrary partitions having the same sizes.

---

# 8. FINE-SCALE REGIONAL FEATURE STRUCTURE CLEARLY EXCEEDS THE NULL

For the first three scales:

### Scale 4.707

\[
z=6.138,\qquad p=0.004975
\]

### Scale 5.417

\[
z=4.703,\qquad p=0.009950
\]

### Scale 6.248

\[
z=8.615,\qquad p=0.004975.
\]

These are strong departures from the partition-size-preserving null.

Therefore at these scales:

\[
\boxed{
\text{regional morphology differentiation cannot readily be attributed to arbitrary grouping of the same sizes.}
}
\]

---

# 9. BUT THE GLOBAL SIGNAL WEAKENS AT LARGER SCALES

This is important and should absolutely remain in the notebook.

At:

\[
s=7.596
\]

the result is:

\[
p=0.0547.
\]

At:

\[
s=10.641:
\qquad p=0.1343
\]

and:

\[
s=16.569:
\qquad p=0.1692.
\]

Therefore the global mean feature-discrimination statistic does **not** exceed the permutation null at conventional nominal levels for the three coarser scales.

So we should not write:

> Regional profiles are significantly different from random at every scale.

That would be false.

Instead:

\[
\boxed{
\text{non-random regional feature differentiation is strongest at the finer/intermediate scales and weakens under coarser density organization.}
}
\]

This is scientifically more interesting anyway.

---

# 10. THE EFFECT DOES NOT DISAPPEAR ABRUPTLY

Look at the z-scores:

\[
6.138
\rightarrow
4.703
\rightarrow
8.615
\rightarrow
2.232
\rightarrow
1.182
\rightarrow
0.735.
\]

The later scales show progressively weaker global separation from the null.

This is compatible with a multiscale picture in which coarser observational scales merge or reorganize distinctions that are quantitatively clearer at finer scales.

That interpretation is plausible.

But it should remain descriptive unless explicitly tested.

---

# 11. FEATURE-LEVEL RESULTS ARE STRONGER THAN THE COARSE GLOBAL STATISTIC

Several individual features show repeated regional association across scales.

Especially:

### `bbox_width`

\[
6/6
\]

nominally significant scales.

### `centroid_x`

\[
6/6
\]

### `horizontal_occupancy_61`

\[
6/6
\]

### `vertical_occupancy_04`

\[
6/6
\]

### `horizontal_occupancy_03`

\[
6/6.
\]

`aspect_ratio` and several other measurements are also recurrent.

Thus even where the **mean over all 135 features** becomes less exceptional relative to the null, particular morphology measurements remain strongly associated with regional organization.

That is a valuable distinction.

---

# 12. MULTIPLE-TESTING CAUTION

There is one statistical boundary we should explicitly preserve.

The feature-level table evaluates many features across several scales.

Therefore:

\[
p<0.05
\]

for an individual feature/scale should not automatically be treated as confirmatory feature discovery without multiple-comparison control.

The safest current use is:

\[
\boxed{
\text{feature-level permutation results are descriptive evidence of recurrent signal}
}
\]

with emphasis on:

- effect sizes;
- median z;
- recurrence across scales;
- feature-block patterns;

rather than treating every nominal p-value as an independent discovery.

This does not invalidate the result.

It simply prevents overclaiming.

---

# 13. GLOBAL DESCRIPTORS AGAIN SHOW A CONCENTRATED SIGNAL

Median-z block summaries give:

\[
G=3.913
\]

\[
H=1.307
\]

\[
V=0.975.
\]

So global descriptors show much stronger average departure from the regional-assignment null.

This agrees with the previous region-discrimination ranking.

But again:

\[
\boxed{
\text{strong regional discrimination}
\neq
\text{dominance of total morphology geometry}.
}
\]

The perturbation results showed that removing horizontal or vertical occupancy severely damages neighborhood recovery.

Therefore the current combined picture is:

\[
\boxed{
\text{occupancy blocks carry distributed geometric structure}
}
\]

while:

\[
\boxed{
\text{global descriptors provide concentrated region-level contrast}.
}
\]

That is a much richer result than saying one block is simply “more important.”

---

# 14. NOW THE FINAL SHIELD — STOP HERE BEFORE FREEZING IT

The reported cross-scale feature-profile agreement is:

\[
0.9979-1.0000
\]

for essentially every scale pair.

And for almost every feature:

\[
\rho=1.0.
\]

Bro, **this needs a code audit.**

Not because such stability is mathematically impossible.

But because it is suspiciously close to exact identity across:

- 135 features;
- six different basin partitions;
- different numbers of regions;
- all 15 scale pairs.

More importantly, it conflicts in magnitude with the immediately preceding legitimate cross-scale feature-discrimination result:

\[
\boxed{\rho_{\text{adjacent}}\approx0.90-0.99}
\]

rather than essentially:

\[
1.000.
\]

---

# 15. WHY THE FINAL RESULT IS SUSPICIOUS

The final output says:

> Basin identities are not matched across scales.

Good.

But then it reports a **feature-level cross-scale rho** for every feature.

To compute a Spearman correlation for one feature across two scales, there must be a vector of values associated with that feature at each scale.

We need to know exactly what those vectors are.

If the code accidentally compares:

- feature indices;
- sorted vectors;
- ranks generated independently from already ordered quantities;
- repeated/global statistics;
- or values whose ordering is mathematically fixed;

then:

\[
\rho\approx1
\]

could be produced trivially.

---

# 16. THIS IS PARTICULARLY IMPORTANT BECAUSE REGION COUNTS DIFFER

For example:

\[
7\text{ regions at scale A}
\]

versus:

\[
6\text{ regions at scale B}.
\]

If basin identities are not matched, then directly correlating region-level feature values across those scales is not straightforward.

So the question is:

> **What exact equal-length objects are being correlated for each feature?**

Until we inspect that, the final shield should not enter the evidence ledger.

---

# 17. POSSIBLE VALID INTERPRETATION

There *is* a legitimate quantity we already computed:

For each scale, create a 135-vector:

\[
D_s=
(d_{s1},d_{s2},...,d_{s135})
\]

where:

\[
d_{sj}
\]

is the regional-discrimination magnitude for feature \(j\).

Then compare:

\[
D_s
\]

across scales using Spearman correlation.

That produced the earlier:

\[
0.902-0.988
\]

adjacent-scale correlations.

That test is interpretable because it asks:

> Do the same features tend to be more region-discriminating at different scales?

But then the correlation is **between feature vectors across scales**.

It does not produce a separate cross-scale rho for each feature.

---

# 18. THEREFORE THE FINAL SHIELD MAY CONTAIN A METRIC-DEFINITION PROBLEM

The output:

```text
FEATURE-LEVEL CROSS-SCALE CONSISTENCY

feature
horizontal_occupancy_00    rho = 1
horizontal_occupancy_01    rho = 1
...