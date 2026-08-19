# 🧪 CLO-SKET — DIRECTIONAL / ANGULAR MORPHOLOGY EXPERIMENT
## Findings from the Predefined 135-D Morphology Representation

**Status:** FROZEN BEFORE RAW-DATA ANALYSIS

**Purpose:**  
Document the complete directional / angular morphology experiment
performed on the existing canonical CLO-SKET morphology representation
before moving to an independent analysis directly from raw sketch data.

---

# 1. Experimental Question

The experiment asked whether the existing quantitative morphology
representation could be transformed into an independently defined
directional description and whether that description would reveal
reproducible geometric structure.

The experiment was deliberately designed so that:

\[
\boxed{
\text{Paper-I morphology representation remains unchanged}
}
\]

The directional representation was therefore treated as an
**additional analysis**, not as a replacement for the canonical
morphology representation.

---

# 2. Starting Representation

The frozen canonical morphology matrix was:

\[
\mathbf{X}\in\mathbb{R}^{2300\times135}
\]

with:

- 2,300 sketches;
- 64 horizontal occupancy measurements;
- 64 vertical occupancy measurements;
- 7 global geometric descriptors.

Thus:

\[
64+64+7=135.
\]

The saved canonical matrix passed an exact SHA-256 integrity check.

### Canonical preprocessing

- grayscale conversion;
- intensity normalization by 255;
- foreground threshold \(<0.8\);
- canonical spatial resolution \(64\times64\).

The saved matrix was verified to be identical to the frozen
Paper-I representation.

---

# 3. Exact Recovery of the Underlying 64 × 64 Masks

The original CLO-SKET source images were restored using the canonical
source-path ordering.

The dataset contained:

\[
2300
\]

TIFF images across:

\[
23
\]

source categories.

The exact canonical preprocessing was reapplied to recover:

\[
\boxed{
2300\times64\times64
}
\]

morphology masks.

The recovered masks were then projected back into the original
horizontal and vertical occupancy measurements.

---

# 4. Canonical Reproduction Verification

The recovered masks reproduced the original morphology representation
exactly.

### Horizontal occupancy

\[
\text{maximum absolute error}=0
\]

\[
\text{mean absolute error}=0
\]

### Vertical occupancy

\[
\text{maximum absolute error}=0
\]

\[
\text{mean absolute error}=0
\]

Therefore:

\[
\boxed{
\text{Recovered mask}
\rightarrow
\text{occupancy}
=
\text{original canonical occupancy}
}
\]

This establishes that the subsequent directional analysis operated on
the same underlying image-derived morphology rather than on a newly
introduced image representation.

---

# 5. Centroid Geometry Inspection

For each \(64\times64\) morphology mask, an intensity-weighted morphology
centroid was calculated.

The centroid was used initially **only for geometric inspection**.

It did not modify the canonical representation.

### Centroid statistics

\[
\mu_{c_x}=31.0745
\]

\[
\sigma_{c_x}=2.1659
\]

\[
\mu_{c_y}=28.8701
\]

\[
\sigma_{c_y}=4.1869
\]

Ranges:

\[
c_x\in[22.568,\;40.089]
\]

\[
c_y\in[11.929,\;48.160]
\]

Normalized mean centroid:

\[
\boxed{
(0.4855,\;0.4511)
}
\]

Normalized SD:

\[
(0.0338,\;0.0654)
\]

The centroid therefore provided a reasonably concentrated population-level
geometric reference, while still exhibiting substantial sketch-level
variation.

No radial representation had yet been created at this stage.

---

# 6. Centroid-Referenced Angular Morphology

Each morphology mask was transformed into centroid-referenced polar
coordinates:

\[
(x,y)
\rightarrow
(r,\theta)
\]

and the foreground morphology was accumulated as a weighted angular
distribution.

For sketch \(i\):

\[
\boxed{
A_i(\theta)
}
\]

denotes its centroid-referenced angular morphology profile.

The angular domain was discretized into:

\[
72
\]

bins, corresponding to:

\[
5^\circ
\]

per bin.

Thus:

\[
\mathbf{A}
\in
\mathbb{R}^{2300\times72}.
\]

Each angular profile was normalized.

### Profile integrity

Minimum profile sum:

\[
0.9999998
\]

Maximum profile sum:

\[
1.0000002
\]

Therefore all angular profiles effectively satisfy:

\[
\boxed{
\sum_{\theta}A_i(\theta)=1
}
\]

for every sketch.

---

# 7. Bilateral Symmetry

Bilateral angular symmetry was measured empirically.

The experiment did **not** assume that garments are symmetric.

### Population statistics

Mean symmetry:

\[
\boxed{0.6499}
\]

Median:

\[
0.6664
\]

SD:

\[
0.1020
\]

10th percentile:

\[
0.5247
\]

90th percentile:

\[
0.7607
\]

Minimum:

\[
0.0417
\]

Maximum:

\[
0.8536
\]

Thus the population contains substantial bilateral organization,
but also considerable sketch-level variation.

The important methodological point is:

\[
\boxed{
\text{symmetry was measured, not assumed}
}
\]

---

# 8. Circular Concentration

For each angular profile, a weighted circular resultant was calculated.

The resultant length is:

\[
R=
\sqrt{C^2+S^2}
\]

with circular variance:

\[
V_c=1-R.
\]

### Population results

Mean resultant:

\[
\boxed{
R=0.08658
}
\]

Median:

\[
0.07276
\]

SD:

\[
0.06181
\]

10th percentile:

\[
0.02016
\]

90th percentile:

\[
0.17228
\]

Mean circular variance:

\[
0.91342
\]

Median circular variance:

\[
0.92724
\]

The interpretation is important.

The low mean \(R\) indicates that morphology directions do not
generally concentrate around one single global direction.

However:

\[
\boxed{
R\approx0
\neq
\text{absence of angular morphology}
}
\]

because opposing directions can cancel in the first circular resultant.

This became particularly important in the subsequent Fourier analysis.

---

# 9. Symmetry–Resultant Relationship

The correlation between bilateral symmetry and circular resultant
length was:

\[
\boxed{
r=-0.3884
}
\]

Thus sketches with stronger measured bilateral organization tended,
on average, to exhibit lower first-order directional concentration.

This is consistent with the possibility that opposing directional
components cancel in the first circular resultant.

No formal Rayleigh significance test was used because the observations
are weighted angular morphology profiles rather than independent raw
directional observations.

Therefore this result is treated as **descriptive circular statistics**.

---

# 10. Angular Fourier Representation

The angular profiles were transformed using a real Fourier transform.

Input:

\[
2300\times72
\]

Output:

\[
2300\times37
\]

real Fourier coefficients.

The harmonics provide a frequency-domain description of angular
morphology:

\[
A(\theta)
\rightarrow
F_k.
\]

Conceptually:

- \(k=0\): mean angular morphology;
- \(k=1\): first directional component;
- \(k=2\): two-fold angular structure;
- higher \(k\): progressively finer angular variation.

---

# 11. First- and Second-Harmonic Structure

The first harmonic had:

\[
|F_1|=0.08658
\]

which agrees with the circular resultant:

\[
R=0.08658.
\]

The second harmonic was substantially larger:

\[
|F_2|=0.24774.
\]

Therefore:

\[
\frac{|F_2|}{|F_1|}
=
2.8615
\]

with median ratio:

\[
2.9275.
\]

Thus:

\[
\boxed{
|F_2|\gg|F_1|
}
\]

for the population on average.

This demonstrates why the low first circular resultant should not be
interpreted as an absence of angular structure.

The first directional component can be weak because opposing
directions cancel, while higher-order angular structure remains strong.

---

# 12. Fourier Power Structure

After correcting the real-FFT power spectrum for the omitted
negative-frequency conjugate terms, Parseval energy conservation was
verified.

Maximum absolute energy error:

\[
3.89\times10^{-9}
\]

Mean absolute energy error:

\[
6.65\times10^{-10}
\]

Therefore:

\[
\boxed{
\text{Parseval energy conservation verified}
}
\]

The dominant non-DC harmonic was \(k=2\).

Selected corrected power fractions:

| Harmonic | Magnitude | Fraction of total power |
|---|---:|---:|
| \(k=0\) | 1.0000 | 0.6065 |
| \(k=1\) | 0.0866 | 0.0137 |
| \(k=2\) | 0.2477 | 0.1045 |
| \(k=3\) | 0.1415 | 0.0330 |
| \(k=4\) | 0.1174 | 0.0239 |
| \(k=6\) | 0.1012 | 0.0179 |
| \(k=8\) | 0.0880 | 0.0133 |
| \(k=12\) | 0.0678 | 0.0081 |
| \(k=16\) | 0.0566 | 0.0056 |
| \(k=24\) | 0.0447 | 0.0034 |
| \(k=36\) | 0.0355 | 0.0013 |

The angular morphology therefore contains structure across multiple
frequency scales rather than being represented entirely by one or two
low-frequency components.

---

# 13. Fourier Reconstruction

The angular profiles were reconstructed using increasing numbers of
Fourier harmonics.

| \(K\) | Mean RMSE | Median RMSE | Mean explained variance |
|---:|---:|---:|---:|
| 1 | 0.01046 | 0.00982 | 0.038 |
| 2 | 0.00892 | 0.00838 | 0.270 |
| 4 | 0.00789 | 0.00738 | 0.432 |
| 8 | 0.00651 | 0.00600 | 0.610 |
| 16 | 0.00487 | 0.00448 | 0.772 |
| 32 | 0.00193 | 0.00178 | 0.960 |

Thus:

\[
K=8
\rightarrow
\sim61\%
\]

of mean explained variance,

while

\[
K=16
\rightarrow
\sim77\%
\]

and

\[
K=32
\rightarrow
\sim96\%.
\]

This indicates that the angular representation has a meaningful
frequency-domain structure, but its complete morphology is not
captured by only the first few harmonics.

---

# 14. Harmonic–Symmetry Association

Each harmonic magnitude was correlated with the independently measured
bilateral symmetry score.

The strongest listed association occurred at:

\[
k=3
\]

with:

\[
r_{\text{Pearson}}=-0.6063
\]

and

\[
\rho_{\text{Spearman}}=-0.5496.
\]

Other notable associations included:

\[
k=5:
\quad
\rho=-0.4490
\]

\[
k=7:
\quad
\rho=-0.3902
\]

\[
k=1:
\quad
\rho=-0.3361
\]

\[
k=9:
\quad
\rho=-0.3140
\]

and several additional harmonics showed moderate negative
associations.

This indicates that bilateral organization is reflected in the
distribution of angular frequency components, rather than being
restricted to the first harmonic.

---

# 15. Important Negative Finding: \(k=2\) Is Not Simply "Symmetry"

Although \(k=2\) had the largest non-DC magnitude, its direct association
with the independently measured bilateral symmetry score was weak:

\[
r_{\text{Pearson}}=-0.1273
\]

\[
\rho_{\text{Spearman}}=-0.0849.
\]

Therefore the experiment does **not** support the simplistic statement:

\[
\boxed{
k=2=\text{bilateral symmetry}
}
\]

Instead:

\[
\boxed{
k=2
\text{ is a strong angular harmonic, but is not equivalent to the
measured bilateral-symmetry score.}
}
\]

This distinction must be preserved in the manuscript.

---

# 16. Even–Odd Harmonic Structure

Non-DC angular power was divided between even and odd harmonics.

Even-harmonic non-DC power:

\[
0.3679
\]

Odd-harmonic non-DC power:

\[
0.2810
\]

Even fraction:

\[
\boxed{
0.5669
}
\]

Odd fraction:

\[
\boxed{
0.4331
}
\]

Thus the angular morphology contains somewhat more even-harmonic than
odd-harmonic power, but both contribute substantially.

This again argues against reducing the geometry to a single
symmetry-related harmonic.

---

# 17. Comparison with Canonical Horizontal Occupancy

The canonical horizontal occupancy representation was independently
transformed using a 64-point Fourier transform.

Therefore two geometric descriptions of the same 2,300 sketches were
compared:

### Representation A

\[
\text{horizontal occupancy}
\rightarrow
64\text{-point FFT}
\]

### Representation B

\[
\text{centroid-referenced angular morphology}
\rightarrow
72\text{-point circular FFT}
\]

The resulting representations were:

\[
2300\times33
\]

and

\[
2300\times37.
\]

---

# 18. Fourier Dimensionality

PCA dimensionality required to explain different fractions of variance:

| Variance threshold | Horizontal Fourier | Angular Fourier |
|---|---:|---:|
| 80% | 11 | 21 |
| 90% | 19 | 28 |
| 95% | 25 | 32 |
| 99% | 31 | 36 |

The angular Fourier representation therefore required more principal
components than the horizontal Fourier representation at the tested
variance thresholds.

This indicates that the angular representation is not simply a
lower-dimensional restatement of horizontal occupancy.

---

# 19. Matched-Harmonic Correlations

Directly matching Fourier harmonic indices between the horizontal and
angular representations produced generally modest correlations.

The mean absolute matched-harmonic correlation was:

\[
\boxed{
0.0717
}
\]

The maximum absolute matched-harmonic correlation was:

\[
\boxed{
0.1818
}
\]

The largest listed matched relationship occurred at:

\[
k=1
\]

with:

\[
r=-0.1818.
\]

Thus individual harmonic coordinates do not appear to be strongly
redundant across the two representations.

---

# 20. Multivariate CCA

Although individual matched harmonics were only weakly correlated,
Canonical Correlation Analysis revealed substantially stronger
multivariate correspondence.

Using PCA representations retaining 95% variance:

\[
25
\]

horizontal dimensions and

\[
32
\]

angular dimensions were retained.

The first canonical correlation was:

\[
\boxed{
r_1=0.5525
}
\]

followed by:

\[
r_2=0.2838
\]

\[
r_3=0.2003
\]

with progressively smaller correlations thereafter.

This is an important distinction:

\[
\boxed{
\text{weak coordinate-wise correspondence}
\neq
\text{weak multivariate correspondence}
}
\]

The shared structure appears to be distributed across combinations of
features rather than concentrated in one-to-one harmonic correspondences.

---

# 21. Held-Out CCA

Because CCA can overfit in high-dimensional settings, the analysis
was repeated using a train/test design.

Population:

\[
2300
\]

Training:

\[
1840
\]

Testing:

\[
460
\]

or:

\[
80\%/20\%.
\]

PCA dimensionality was determined using the training set only:

\[
25
\]

horizontal dimensions,

\[
32
\]

angular dimensions,

both corresponding to 95% explained variance.

---

# 22. Held-Out CCA Results

| Component | Train \(r\) | Held-out \(r\) |
|---:|---:|---:|
| 1 | 0.5724 | **0.4873** |
| 2 | 0.2842 | 0.2024 |
| 3 | 0.2196 | 0.0856 |
| 4 | 0.1873 | 0.0706 |
| 5 | 0.1752 | 0.0805 |
| 6 | 0.1337 | 0.0326 |
| 7 | 0.1226 | -0.0129 |
| 8 | 0.1157 | -0.0274 |
| 9 | 0.1035 | 0.0557 |
| 10 | 0.0921 | 0.0042 |

The primary result is:

\[
\boxed{
r_{1,\text{train}}=0.5724
}
\]

\[
\boxed{
r_{1,\text{test}}=0.4873
}
\]

---

# 23. Generalization Ratio

The held-out to training ratio was:

\[
\frac{0.4873}{0.5724}
=
\boxed{
0.8513
}
\]

Thus approximately 85.1% of the training first-component
correlation was retained on unseen sketches.

This provides evidence that the leading multivariate correspondence is
not solely a training-set artifact.

---

# 24. Permutation Null

A permutation test was performed using:

\[
200
\]

random permutations.

The training correspondence between the two representations was
destroyed while the held-out test correspondence remained correctly
paired.

Observed held-out:

\[
\boxed{
r_1=0.4873
}
\]

Permutation null:

\[
\text{mean}=-0.00294
\]

\[
\text{SD}=0.05430
\]

\[
95\text{th percentile}=0.08351
\]

\[
99\text{th percentile}=0.11164
\]

Empirical one-sided permutation probability:

\[
\boxed{
p=0.00498
}
\]

The observed held-out correlation therefore lies far above the
permutation distribution.

---

# 25. Strongest Result of This Experiment

The most defensible result from the complete experiment is:

\[
\boxed{
\text{Centroid-referenced angular morphology exhibits reproducible
multivariate correspondence with canonical occupancy morphology.}
}
\]

This correspondence:

1. is visible in multivariate CCA;
2. persists on held-out sketches;
3. substantially exceeds the row-permutation null;
4. is not explained by strong one-to-one matched-harmonic correlations.

The result therefore supports a relationship between the two geometric
descriptions at the population level.

---

# 26. What This Experiment Establishes

The experiment provides evidence that:

### 1. The canonical morphology masks can be recovered exactly

\[
\text{mask}
\rightarrow
\text{canonical occupancy}
\]

with zero reconstruction error.

### 2. Centroid-referenced angular morphology is computationally
well-defined for the CLO-SKET population.

### 3. Angular morphology contains structured frequency-domain variation.

### 4. The first circular resultant is insufficient to characterize
the angular morphology.

### 5. Higher angular harmonics contain substantial morphology.

### 6. Bilateral organization is distributed across multiple harmonic
components.

### 7. Angular morphology and canonical occupancy share reproducible
multivariate structure.

### 8. This shared structure generalizes to held-out sketches.

### 9. The observed correspondence is substantially stronger than a
row-permutation null.

---

# 27. What This Experiment Does NOT Establish

The experiment does **not** establish:

- semantic garment-part representations;
- semantic garment categories;
- a universal garment morphology vocabulary;
- a morphology grammar;
- a learned semantic language;
- a mathematical manifold;
- causal mechanisms;
- human-like visual understanding;
- information-theoretic independence;
- that angular morphology is superior to canonical morphology;
- that \(k=2\) is equivalent to bilateral symmetry;
- that the Fourier representation is universally optimal.

In particular:

\[
\boxed{
\text{geometric correspondence}
\neq
\text{semantic correspondence}
}
\]

---

# 28. Important Interpretation Boundary

The angular representation was derived from the existing canonical
morphology masks.

Therefore this experiment should not be presented as evidence that
angular morphology was discovered independently from raw images.

Its correct interpretation is:

\[
\boxed{
\text{predefined morphology}
\rightarrow
\text{independent geometric transformation}
\rightarrow
\text{reproducible structure}
}
\]

This is why a subsequent raw-data experiment is scientifically useful.

---

# 29. Why We Now Move to Raw Data

The current experiment establishes that an angular description can reveal
reproducible structure when derived from the canonical morphology masks.

The next experiment asks a stronger and more independent question:

\[
\boxed{
\text{raw sketch image}
\rightarrow
\text{directional / radial geometry}
}
\]

rather than:

\[
\boxed{
\text{canonical morphology}
\rightarrow
\text{directional / radial geometry}
}
\]

The distinction is important.

### Current experiment

Tests whether the new geometric description is related to the existing
morphology representation.

### Raw-data experiment

Tests whether similar geometric organization can be recovered directly
from the sketch images without first passing through the predefined
135-D morphology coordinates.

---

# 30. Relationship Between the Two Experimental Stages

The experimental progression is therefore:

\[
\boxed{
\text{Stage 1}
}
\]

\[
135\text{-D canonical morphology}
\rightarrow
64\times64\text{ mask}
\rightarrow
\text{centroid}
\rightarrow
A(\theta)
\rightarrow
\text{Fourier}
\rightarrow
\text{CCA}
\]

followed by:

\[
\boxed{
\text{Stage 2}
}
\]

\[
\text{raw sketch}
\rightarrow
\text{independent geometric representation}
\rightarrow
\text{population structure}
\]

The purpose of Stage 2 is therefore **not to replace Stage 1**.

It provides an additional robustness test for whether the observed
geometric organization depends strongly on the predefined morphology
representation.

---

# 31. Frozen Scientific Interpretation

The current notebook supports the following bounded statement:

> Across 2,300 CLO-SKET sketches, a centroid-referenced angular
> morphology representation derived from the canonical 64 × 64
> morphology masks exhibits structured multi-harmonic variation and
> reproducible multivariate correspondence with canonical occupancy
> morphology. The leading correspondence generalizes to held-out
> sketches and exceeds a row-permutation null.

The stronger interpretation that this constitutes a semantic morphology
space remains outside the evidence of this experiment.

---

# 32. Status Before Raw-Data Analysis

\[
\boxed{
\textbf{PREDEFINED-MORPHOLOGY DIRECTIONAL EXPERIMENT = FROZEN}
}
\]

Canonical Paper-I representation:

\[
\boxed{\text{UNCHANGED}}
\]

Number of sketches:

\[
\boxed{2300}
\]

Canonical morphology dimensions:

\[
\boxed{135}
\]

Angular morphology dimensions:

\[
\boxed{72}
\]

Angular Fourier dimensions:

\[
\boxed{37}
\]

Held-out CCA:

\[
\boxed{r_1=0.4873}
\]

Permutation null 95th percentile:

\[
\boxed{0.0835}
\]

Empirical permutation probability:

\[
\boxed{p=0.00498}
\]

Generalization ratio:

\[
\boxed{0.8513}
\]

---

# 33. Final Experimental Conclusion

The predefined-morphology experiment provides evidence that the
canonical CLO-SKET morphology representation contains geometric
structure that can be expressed through a centroid-referenced angular
description.

The angular description is not reducible to a single directional
component: its structure is distributed across multiple Fourier
harmonics, with particularly strong second-harmonic magnitude and
substantial higher-frequency content.

More importantly, the angular and canonical representations exhibit
reproducible multivariate correspondence:

\[
\boxed{
r_{1,\text{held-out}}=0.4873
}
\]

with:

\[
\boxed{
p_{\text{permutation}}=0.00498
}
\]

and:

\[
\boxed{
\text{test/train ratio}=0.8513.
}
\]

Therefore the current experiment provides a robust **geometric
correspondence result**, while deliberately stopping short of semantic
interpretation.

The next stage is to determine whether comparable geometric structure
can be recovered **directly from the raw sketch data**.