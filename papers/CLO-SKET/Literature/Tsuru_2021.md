# Tsuru et al. (2021) — Silhouette Classification of Designer’s Collections in Luxury Fashion Brands

## Citation

**Tsuru, T., Sugahara, M., & Nishimura, H. (2021)**

*Silhouette Classification of Designer’s Collections in Luxury Fashion Brands*

*International Journal of Affective Engineering*

DOI: 10.5057/ijae.IJAE-D-20-00002

### Role in CLO-SKET Literature Review

This paper represents a **population-level quantitative analysis of fashion silhouette morphology**.

It is particularly important for CLO-SKET because, unlike many fashion-AI papers, it does not treat each garment merely as an image-classification example.

Instead, the authors construct a population of garment silhouettes, extract **11 quantitative measurements**, standardize them, and apply **multivariate statistical analysis using multidimensional scaling (MDS) and hierarchical cluster analysis**.

The paper therefore establishes a strong precedent for:

\[
\boxed{
\text{fashion garment population}
\rightarrow
\text{quantitative geometric measurements}
\rightarrow
\text{low-dimensional morphology map}
\rightarrow
\text{clusters / silhouette categories}
}
\]

However, the population consists of **catwalk photographs of garments**, rather than a population of **2D fashion sketches/flats**.

This distinction is central to the CLO-SKET positioning.

---

# 1. Scientific Question

The central question is:

> **How can changing fashion silhouettes be quantitatively represented, classified, and visualized across designer collections and time?**

The authors are particularly interested in understanding changes in silhouette design as fashion trends change.

The paper explicitly treats silhouette as an important element of fashion design and seeks to construct a renewed silhouette classification criterion. :contentReference[oaicite:1]{index=1}

The overall direction is:

\[
\boxed{
\text{catwalk garment images}
\rightarrow
\text{silhouette measurements}
\rightarrow
\text{multivariate analysis}
\rightarrow
\text{silhouette space}
\rightarrow
\text{classification}
}
\]

This makes the paper one of the closest precedents to the population-level component of CLO-SKET.

---

# 2. Input

The input consists of **images of garments from luxury fashion collections**.

The authors selected collections from three brands:

- Dior,
- Sacai,
- Dries Van Noten.

The analyzed collection data consisted of:

- 56 Dior images from 2012 Autumn/Winter,
- 64 Dior images from 2017 Spring/Summer,
- 43 Sacai images from 2017 Spring/Summer,
- 60 Dries Van Noten images from 2017 Spring/Summer,

for a total of:

\[
\boxed{223\text{ garment images}}
\]

The images were obtained from WGSN. :contentReference[oaicite:2]{index=2}

Importantly, these are **photographic catwalk/collection images**, not fashion flats.

---

# 3. The Core Problem

The authors note that traditional silhouette categories no longer adequately describe contemporary fashion.

Approximately 30% of the silhouettes in their broader collection of roughly 10,000 luxury-brand images were not included in existing industry silhouette categories. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

The problem is therefore:

\[
\boxed{
\text{Existing silhouette categories}
\not\approx
\text{contemporary garment population}
}
\]

The authors seek a data-driven way to discover and organize the observed silhouette variation.

---

# 4. Population Construction

This is one of the most important aspects of the paper for CLO-SKET.

The authors do not analyze a single garment.

They construct a **population of 223 garment silhouettes** and represent every individual using the same set of measurements.

Thus:

\[
\boxed{
G_1,G_2,\ldots,G_{223}
}
\]

are represented in a common measurement space.

This is fundamentally different from a conventional fashion-image classification problem.

The scientific object becomes:

\[
\boxed{
\text{population of garment silhouettes}
}
\]

rather than:

\[
\boxed{
\text{individual garment image}
}
\]

---

# 5. Quantitative Silhouette Representation

Each garment is represented using **11 measurement positions**.

The measurements are:

1. Total height
2. Neck
3. Shoulder
4. Sleeve width
5. Waist
6. Hem high
7. Hips
8. Length high
9. Hem line
10. Knee
11. Length

The authors state that these positions were selected because they correspond to feature values measured by pattern makers during garment design. :contentReference[oaicite:5]{index=5}

Conceptually:

\[
\boxed{
\mathbf{x}_i
=
[
x_{i1},
x_{i2},
\ldots,
x_{i11}
]
}
\]

for garment \(i\).

Thus the paper creates an explicit **11-dimensional geometric representation of silhouette**.

---

# 6. Normalization

The measurements are standardized relative to the **total height of each model**.

Therefore the representation is not simply raw pixel measurements.

Conceptually:

\[
\boxed{
x_{ij}^{*}
=
\frac{x_{ij}}{\text{Total Height}_i}
}
\]

This makes the measurements more comparable across garments and models.

The important methodological point is that the authors attempt to remove overall size differences so that the analysis focuses more strongly on **proportional silhouette geometry**. :contentReference[oaicite:6]{index=6}

---

# 7. Multidimensional Scaling (MDS)

The first major statistical technique is **multidimensional scaling (MDS)**.

MDS starts from pairwise distances/dissimilarities between garments.

Conceptually:

\[
\boxed{
\mathbf{X}
\rightarrow
D
\rightarrow
\text{MDS}
\rightarrow
\mathbb{R}^{2}
}
\]

where:

- \(\mathbf{X}\) = quantitative silhouette measurements,
- \(D\) = pairwise dissimilarity matrix,
- MDS = multidimensional scaling.

The paper explains that objects with greater dissimilarity are placed farther apart, while similar objects are placed closer together in the resulting low-dimensional Euclidean space. :contentReference[oaicite:7]{index=7}

This is therefore a genuine **population-level geometric similarity space**.

---

# 8. The Silhouette Location Map

The MDS output produces a two-dimensional map containing all 223 silhouettes.

This is shown in **Figure 3** of the paper.

Each point corresponds to a garment silhouette.

The resulting map allows the researchers to visually inspect:

\[
\boxed{
\text{which silhouettes are similar}
}
\]

and

\[
\boxed{
\text{which silhouettes are geometrically different}
}
\]

The authors additionally visualize brand and collection information on this map.

Thus the MDS representation becomes a kind of:

\[
\boxed{
\text{silhouette morphology map}
}
\]

---

# 9. What Does the MDS Space Mean?

This is important.

The MDS axes are **not explicitly defined morphological variables in the same sense as waist width or hem width**.

Rather, they are dimensions in a low-dimensional Euclidean configuration that preserves pairwise dissimilarities as well as possible.

In the resulting map, the authors interpret directions using observable silhouette characteristics.

For example, Figure 3 labels regions associated with properties such as:

- narrow versus wide hem width,
- short versus long garment length.

Thus:

\[
\boxed{
\text{measurement space}
\rightarrow
\text{dissimilarity space}
\rightarrow
\text{2D configuration}
}
\]

rather than:

\[
\boxed{
\text{PCA}
\rightarrow
\text{principal axes of variance}
}
\]

This distinction should be preserved in our review.

---

# 10. Important: MDS Is Not PCA

This paper gives us another useful distinction.

### PCA

PCA finds orthogonal directions that maximize variance in the original feature space.

\[
\boxed{
\text{measurements}
\rightarrow
\text{variance-maximizing axes}
}
\]

### MDS

MDS starts from pairwise dissimilarities and seeks a low-dimensional configuration that preserves those relationships.

\[
\boxed{
\text{measurements}
\rightarrow
\text{pairwise distances}
\rightarrow
\text{low-dimensional configuration}
}
\]

Therefore Tsuru et al. do **not** rotate the original measurement dimensions in the PCA sense.

They construct a new spatial representation whose geometry reflects silhouette dissimilarity.

---

# 11. Hierarchical Cluster Analysis

The second major statistical method is hierarchical cluster analysis.

The authors use:

\[
\boxed{
\text{Ward's method}
}
\]

with Euclidean distance.

The procedure begins with each silhouette as its own cluster and repeatedly merges similar clusters until a hierarchical tree is produced. :contentReference[oaicite:8]{index=8}

The resulting dendrogram is then cut into:

\[
\boxed{9\text{ silhouette clusters}}
\]

---

# 12. The Nine Silhouette Categories

The nine clusters correspond to different geometric silhouette forms.

The paper describes them in terms of characteristics including:

- garment length,
- upper-body width,
- waist narrowing,
- hem expansion,
- straightness,
- tapering,
- X-shaped structure,
- V-shaped structure.

For example:

### Cluster 1

A relaxed trapezoidal silhouette spreading from the upper body toward the bottom.

### Cluster 2

A box-like silhouette falling relatively linearly toward the hem.

### Cluster 3

A long, relatively thin rectangular / I-line silhouette.

### Cluster 4

A natural V-shaped silhouette tapering toward the hem.

### Cluster 5

Another V-shaped silhouette with different length characteristics.

### Clusters 6–9

Increasingly strong X-line structures with differences in garment length and hem expansion. :contentReference[oaicite:9]{index=9}

Thus the clusters are not merely numerical groups.

They are interpreted as **geometric silhouette morphologies**.

---

# 13. From Statistical Clusters to Morphological Categories

This is perhaps the most important conceptual step.

The pipeline is:

\[
\boxed{
\text{quantitative measurements}
\rightarrow
\text{distance relationships}
\rightarrow
\text{MDS}
+
\text{clustering}
\rightarrow
\text{interpretable silhouette categories}
}
\]

The authors then construct simplified **basic figures** representing the morphology of each cluster.

Figure 6 provides these basic silhouette figures.

Therefore:

\[
\boxed{
\text{statistical structure}
\rightarrow
\text{interpretable garment morphology}
}
\]

This is a very strong precedent for the idea that quantitative garment geometry can reveal an underlying organization of fashion forms.

---

# 14. Population-Level Analysis

This paper is important because the unit of analysis is explicitly the **population**.

The authors examine:

\[
\boxed{
223\text{ silhouettes}
}
\]

simultaneously.

They do not simply classify each garment independently.

Instead, each garment occupies a location relative to the other garments.

Thus the study establishes:

\[
\boxed{
\text{garment}
\rightarrow
\text{position within population morphology}
}
\]

This is substantially closer to CLO-SKET than conventional fashion recognition papers.

---

# 15. Temporal and Brand-Level Structure

The MDS map is also used to compare:

- different years of the same brand,
- different brands in the same season.

The authors report that similar silhouettes tend to appear in particular regions and that brand characteristics are strongly expressed by silhouette distributions. :contentReference[oaicite:10]{index=10}

They also report strong concentration of particular brands/collections within particular clusters.

For example, cluster (1) contains predominantly Sacai silhouettes, while clusters (8) and (9) are predominantly composed of Dior 2012/2017 silhouettes. :contentReference[oaicite:11]{index=11}

Thus the morphology space is not merely descriptive.

It can reveal:

\[
\boxed{
\text{brand-specific distribution}
}
\]

and

\[
\boxed{
\text{temporal fashion-trend structure}
}
\]

---

# 16. What Is Learned?

There is **no neural representation learning** in this study.

The representation is explicitly constructed from 11 measurements.

The computational pipeline is:

\[
\boxed{
\text{manual geometric measurement}
\rightarrow
\text{standardization}
\rightarrow
\text{distance calculation}
\rightarrow
\text{MDS / clustering}
}
\]

Therefore the morphology space is **statistically derived**, rather than learned as a neural latent representation.

This is an important precedent for CLO-SKET because it demonstrates that meaningful fashion morphology can emerge from explicit geometric measurements without deep representation learning.

---

# 17. What the Paper Actually Represents

The paper represents:

\[
\boxed{
\text{garment silhouette morphology}
}
\]

using:

\[
\boxed{
11\text{ normalized geometric measurements}
}
\]

and organizes the resulting population through:

\[
\boxed{
\text{MDS}
+
\text{hierarchical clustering}
}
\]

The resulting representation contains:

\[
\boxed{
\text{continuous similarity structure}
+
\text{discrete silhouette categories}
}
\]

This is substantially closer to the idea of a **shape space** than the modular assembly paper.

---

# 18. But What Is the Actual Visual Object?

This is the critical limitation.

The authors analyze **catwalk/collection photographs**.

They digitize the silhouettes visible in those images.

Therefore:

\[
\boxed{
\text{photographic garment silhouette}
}
\]

is the observed object.

It is **not**:

\[
\boxed{
\text{2D fashion sketch / fashion flat}
}
\]

This distinction must be explicit in our literature review.

---

# 19. What the Paper Does NOT Study

Despite being very close to our question, the paper does not primarily ask:

- How is morphology organized across a population of 2D fashion sketches?
- Can fashion flats themselves be treated as a statistical morphological population?
- Does a population of technical fashion drawings occupy a quantitative shape space?
- Can geometric measurements extracted directly from sketches reproduce garment morphology?
- How does sketch representation affect the resulting morphology space?
- Are sketch-specific geometric representations complementary to silhouette measurements?
- Can independent sketch representations demonstrate corresponding population structure?
- Does the morphology space emerge from the visual language of fashion drawing itself?

Most importantly:

\[
\boxed{
\text{catwalk silhouettes}
\neq
\text{2D fashion sketches}
}
\]

---

# 20. Tsuru et al. vs. CLO-SKET

## Tsuru et al.

The central question is:

\[
\boxed{
\text{How is garment silhouette morphology organized across a collection population?}
}
\]

Pipeline:

\[
\boxed{
\text{catwalk images}
\rightarrow
\text{11 silhouette measurements}
\rightarrow
\text{distance matrix}
\rightarrow
\text{MDS}
+
\text{clustering}
\rightarrow
\text{silhouette categories}
}
\]

---

## CLO-SKET

The central question is:

\[
\boxed{
\text{How is garment morphology organized across a population of 2D fashion sketches?}
}
\]

Our representation is:

\[
\boxed{
\mathbf{x}_i\in\mathbb{R}^{135}
}
\]

with:

\[
\boxed{
\mathbf{X}\in\mathbb{R}^{2300\times135}
}
\]

and an independent radial-angular representation:

\[
\boxed{
\mathbf{r}_i\in\mathbb{R}^{28}
}
\]

with:

\[
\boxed{
\mathbf{R}\in\mathbb{R}^{2300\times28}
}
\]

We then test whether the two representations correspond at the **population level**.

Thus the key distinction is:

\[
\boxed{
\text{Tsuru et al.: one geometric representation of garment silhouettes}
}
\]

versus:

\[
\boxed{
\text{CLO-SKET: population-level organization of 2D sketch morphology}
}
\]

---

# 21. The REALLY Important Gap

This paper changes our literature claim.

We absolutely **cannot** say:

> "No previous study has quantitatively analyzed populations of fashion garments."

That would be false.

Tsuru et al. clearly do exactly that.

We also cannot say:

> "No previous study has constructed a low-dimensional fashion morphology space."

Again, too broad.

Tsuru et al. construct an MDS-based silhouette location map from quantitative garment measurements.

The defensible gap is narrower:

\[
\boxed{
\text{Has anyone done this specifically for a population of 2D fashion sketches/flats?}
}
\]

That is now the question.

---

# 22. Why This Paper Is Actually Good News

Bro, this paper is **not a problem for us**.

It is actually useful because it establishes the plausibility of the broader scientific idea.

It shows:

\[
\boxed{
\text{fashion population}
+
\text{explicit geometry}
+
\text{multivariate statistics}
}
\]

can reveal meaningful morphological organization.

Therefore our scientific question is not:

> "Can mathematical analysis say anything meaningful about fashion shape?"

That has already been demonstrated.

Our question becomes:

> **Does the same population-level principle hold when the objects are 2D fashion sketches themselves, and can sketch-specific geometric representations reveal an organized morphology space?**

That is a much stronger and more precise question.

---

# 23. Tsuru et al. vs. Our Two Representations

This is where CLO-SKET becomes interesting.

Tsuru et al.:

\[
\boxed{
\text{one measurement representation}
\rightarrow
\text{MDS}
}
\]

CLO-SKET:

\[
\boxed{
\text{Representation A}
\rightarrow
\text{population geometry}
}
\]

and independently:

\[
\boxed{
\text{Representation B}
\rightarrow
\text{population geometry}
}
\]

followed by:

\[
\boxed{
A_i
\leftrightarrow
B_i
}
\]

and a row-permuted null:

\[
\boxed{
A_i
\leftrightarrow
B_{\pi(i)}
}
\]

This means our question is not simply:

> "Can we make a shape space?"

Tsuru et al. already show that.

Our stronger question is:

> **Do independently constructed geometric representations of fashion sketches encode corresponding population structure?**

That is a different scientific claim.

---

# 24. Important Difference in Representation

Tsuru et al. manually define **11 measurement locations** based partly on garment-production reference points.

Their representation is therefore:

\[
\boxed{
\text{expert-defined measurement landmarks}
}
\]

CLO-SKET instead uses explicit geometric measurements derived from the sketch itself.

Therefore one potential contribution is:

\[
\boxed{
\text{sketch geometry}
\rightarrow
\text{quantitative morphology}
}
\]

without requiring the researcher to first impose the traditional silhouette taxonomy.

---

# 25. Another Important Difference: Category Discovery

Tsuru et al. ultimately produce **nine silhouette categories**.

The categories are interpreted using the resulting clusters.

Thus:

\[
\boxed{
\text{continuous geometric population}
\rightarrow
\text{clusters}
\rightarrow
\text{named morphology}
}
\]

CLO-SKET should therefore be careful not to imply that **discovering clusters alone** is novel.

Clustering fashion morphology has precedent.

Our stronger evidence lies in whether the **population geometry itself is reproducible across independent representations**.

---

# 26. Important Limitation of Tsuru et al.

The paper's future work explicitly proposes expert interviews to determine whether the location map is consistent with silhouette classification based on experienced fashion professionals. :contentReference[oaicite:12]{index=12}

Therefore the current study provides strong **geometric/statistical organization**, but the connection between the derived map and human fashion sensibility is not fully validated within the paper.

This is useful for our reviewer framing.

We should distinguish:

\[
\boxed{
\text{geometric morphology}
}
\]

from:

\[
\boxed{
\text{human semantic / perceptual interpretation}
}
\]

---

# 27. What This Paper Establishes for the Literature

We can safely say that prior literature has already demonstrated that:

1. fashion silhouettes can be represented quantitatively;
2. a collection of garments can be treated as a population;
3. pairwise geometric dissimilarity can be used to construct a low-dimensional map;
4. hierarchical clustering can reveal recurring silhouette morphologies;
5. the resulting population structure can reveal temporal and brand-level differences.

Tsuru et al. provide direct evidence for all of these points. :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14}

---

# 28. What Remains Unresolved

The unresolved question is more specific:

\[
\boxed{
\textbf{Do 2D fashion sketches/flats themselves form a quantitatively organized morphological population?}
}
\]

More specifically:

\[
\boxed{
\text{2D fashion sketches}
\rightarrow
\text{explicit geometry}
\rightarrow
\text{population shape space}
}
\]

has not been established by this paper.

And the additional question:

\[
\boxed{
\text{Do independent sketch-geometric representations}
\rightarrow
\text{recover corresponding population structure?}
}
\]

is also outside the study.

---

# 29. Scientific Positioning

Tsuru et al. represent a **population-level quantitative silhouette morphology approach**.

Their principal concern is:

\[
\boxed{
\text{garment population}
\rightarrow
\text{silhouette morphology space}
}
\]

CLO-SKET instead asks whether this principle can be established for **2D fashion sketches themselves**.

Thus:

\[
\boxed{
\text{Tsuru et al.: photographed garment silhouettes}
\rightarrow
\text{statistical morphology}
}
\]

versus:

\[
\boxed{
\text{CLO-SKET: 2D fashion sketches}
\rightarrow
\text{statistical morphology}
}
\]

And then CLO-SKET adds:

\[
\boxed{
\text{independent geometric representation}
\rightarrow
\text{population correspondence test}
}
\]

---

# 30. FOMO Takeaway

### What this paper means for CLO-SKET

This paper **closes one version of our gap**.

We cannot claim:

> "Nobody has treated fashion as a quantitative morphological population."

They have.

We cannot claim:

> "Nobody has constructed a low-dimensional map of fashion shape variation."

They have.

We cannot claim:

> "Nobody has combined quantitative silhouette measurements with clustering."

They have.

Instead, the defensible gap becomes:

> **Prior work has demonstrated population-level quantitative analysis of garment silhouette morphology using manually defined geometric measurements, multidimensional scaling, and clustering. However, this work analyzes photographed garments rather than populations of 2D fashion sketches or technical flats. Whether the visual geometry of fashion sketches themselves forms a statistically organized morphological space, and whether independent geometric representations of those sketches recover corresponding population structure, remains a distinct question.**

That is a much stronger literature position.

---

# 31. Reviewer-Proof Classification

### **Literature category:**

\[
\boxed{
\text{Population-level quantitative fashion silhouette morphology}
}
\]

### **Primary task:**

\[
\boxed{
\text{Garment images}
\rightarrow
\text{11 measurements}
\rightarrow
\text{MDS}
+
\text{clustering}
\rightarrow
\text{silhouette categories}
}
\]

### **Representation type:**

\[
\boxed{
\text{Explicit normalized geometric measurement representation}
}
\]

### **Mathematical basis:**

\[
\boxed{
\text{Euclidean distance}
+
\text{MDS}
+
\text{Ward hierarchical clustering}
}
\]

### **Learning type:**

\[
\boxed{
\text{Statistical multivariate analysis — no neural representation learning}
}
\]

### **Population-level fashion morphology analysis:**

\[
\boxed{\textbf{Yes}}
\]

### **Population-level 2D fashion-sketch morphology analysis:**

\[
\boxed{\textbf{No}}
\]

### **Fashion flat / technical-sketch population:**

\[
\boxed{\textbf{No}}
\]

### **Direct CLO-SKET competitor:**

\[
\boxed{\textbf{Partial / adjacent}}
\]

### **Relevance to CLO-SKET:**

\[
\boxed{
\textbf{Very High — critical precedent for population-level quantitative fashion morphology}
}
\]

---

# 32. Final One-Sentence Understanding

> **Tsuru et al. treat 223 photographed fashion silhouettes as a quantitative population, represent each garment using 11 normalized geometric measurements, construct a low-dimensional dissimilarity space using MDS, and identify nine interpretable silhouette clusters using Ward hierarchical clustering; this establishes population-level statistical analysis of fashion morphology, but it does not study whether 2D fashion sketches or technical flats themselves form a quantitatively organized morphological population or whether independent sketch-specific geometric representations recover corresponding population structure.**

---

# 🔥 FOMO STATUS

\[
\boxed{
\textbf{KEEP — CRITICAL PRECEDENT}
}
\]

**This is NOT a paper we use to say "nobody did it."**

It is a paper we use to say:

\[
\boxed{
\text{Population-level quantitative fashion morphology}
\quad
\checkmark
}
\]

but:

\[
\boxed{
\text{Population-level quantitative morphology of 2D fashion sketches/flats}
\quad
?
}
\]

And THAT, bro, is exactly why our next search should be much more surgical.