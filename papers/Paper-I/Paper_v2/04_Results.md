# 4. Results

## 4.1 Evaluation Design and Study Populations

The empirical evaluation was conducted using two complementary data
populations with distinct scientific purposes.

The **primary research corpus comprised 333 garment sketches** and was used
for discovery and characterization of the learned symbolic representation.
Analyses on this corpus examined the learned primitive vocabulary, primitive
sequences, family-level organization, sequential structure, morphology,
compositional representation, and primitive structural profiles.

An **independent CLO-SK corpus** was subsequently used as an external
evaluation population for the frozen representation. This benchmark comprised
2,299 sketch images representing 230 garment identities, 23 garment categories,
and 12 sketchers. The benchmark contained 12,024 transferred geometry events
and used the same frozen vocabulary of 12 primitives organized into three higher-level primitive families.

The two populations therefore serve different roles. Results obtained from
the 333-garment corpus characterize the structure learned from the primary
research data, whereas the CLO-SK analyses evaluate whether the frozen
representation exhibits measurable structural behavior when transferred to
an independent sketch corpus.

The distinction is maintained throughout the Results section: analyses
referring to the 333-garment corpus are reported as primary-corpus analyses,
whereas analyses involving 2,299 images are explicitly identified as CLO-SK
benchmark analyses.

---

# 4.2 Independent CLO-SK Benchmark

## 4.2.1 Benchmark Population and Representation Integrity

To provide an independent evaluation population and a non-symbolic geometric
reference representation, a raw geometry signature was constructed for every
CLO-SK benchmark image.

All 2,299 images produced valid raw signatures, with complete alignment
between raw signatures, canonical representation keys, and benchmark image
identities. The benchmark therefore contained 2,299 valid raw geometric
representations.

Raw signature length varied substantially across images, with a mean of
609.04, a median of 646, a standard deviation of 258.50, and a range from
113 to 1,466.

The raw geometry representation was frozen before retrieval evaluation and
served as the continuous geometric reference against which the symbolic
representations were compared.

The benchmark contained 230 garment identities distributed across 23 garment
categories and 12 sketchers. Each benchmark image received a valid frozen
primitive and family representation, yielding 12,024 transferred geometry
events across the 2,299 images.

---

## 4.2.2 Unrestricted Retrieval

We first evaluated whether the symbolic representations preserved sufficient
information to retrieve sketches belonging to the same garment identity.
Retrieval was performed over all 2,299 benchmark images, with 2,298 candidate
images per query after excluding the query image itself.

Performance was evalfrozenuated using Recall@1, Recall@5, Recall@10, Recall@20,
and Mean Reciprocal Rank (MRR).

| Representation | R@1 | R@5 | R@10 | R@20 | MRR |
|---|---:|---:|---:|---:|---:|
| Raw geometry | **0.174859** | **0.355372** | **0.470639** | **0.597651** | **0.269714** |
| Primitive sequence | 0.019574 | 0.076120 | 0.115702 | 0.201827 | 0.058956 |
| Family sequence | 0.013049 | 0.053502 | 0.115702 | 0.201827 | 0.058956 |

Raw geometry substantially outperformed both symbolic sequence
representations at every retrieval depth.

These results indicate that the symbolic abstraction does not preserve all
of the image-level geometric information available to the continuous
representation. The learned primitives should therefore not be interpreted
as a lossless encoding of the original sketch geometry.

---

## 4.2.3 Cross-Sketcher Retrieval

Because sketches of the same garment can vary according to the sketcher who
produced them, retrieval was also evaluated under a stricter cross-sketcher
condition. Candidates produced by the same sketcher as the query were
excluded.

The cross-sketcher population contained all 2,299 benchmark images and
230 garment identities across 12 sketchers. Every query retained at least
one positive cross-sketcher candidate. The number of positive candidates
per query ranged from 8 to 10, with a mean of 8.995.

Four representations were compared:

- raw geometry;
- primitive sequence;
- primitive set; and
- family sequence.

| Representation | R@1 | R@5 | R@10 | R@20 | MRR |
|---|---:|---:|---:|---:|---:|
| Raw geometry | **0.190953** | **0.387125** | **0.505002** | **0.628969** | **0.291916** |
| Primitive sequence | 0.023054 | 0.081340 | 0.137016 | 0.232710 | 0.065499 |
| Primitive set | 0.019139 | 0.069161 | 0.114833 | 0.217051 | 0.059156 |
| Family sequence | 0.016094 | 0.059591 | 0.097869 | 0.172684 | 0.050616 |

Raw geometry again provided the strongest retrieval performance. At R@1,
raw geometry achieved 19.10%, compared with 2.31% for primitive sequences,
1.91% for primitive sets, and 1.61% for family sequences. The same ordering
was maintained across R@5, R@10, R@20, and MRR.

Thus, cross-sketcher evaluation confirms that the symbolic representation does
not preserve all information required for direct sketch-level retrieval.
This is treated as an informative limitation of the representation rather
than as evidence that the symbolic representation is uninformative.

---

## 4.2.4 Symbolic Sequence Diversity and Reuse

Across the 2,299 benchmark images, 1,463 unique primitive sequences were
observed, corresponding to a uniqueness fraction of 0.636.

At the broader family level, 773 unique sequences were observed,
corresponding to a uniqueness fraction of 0.336.

Thus, the primitive representation retained considerably more sequence-level
variation than the family abstraction.

Repeated symbolic patterns were nevertheless common. A total of 163
primitive sequences occurred more than once, while 199 family sequences
occurred more than once.

The most frequent primitive sequence was `(2, 6)`, occurring 131 times.
At the family level, the most frequent sequence was `('A', 'A')`, occurring
132 times.

This combination of diversity and reuse indicates that the symbolic
representation is neither a unique identifier for individual sketches nor a
fully collapsed representation. Multiple sketches can share recurring
symbolic patterns while retaining substantial sequence variation.

---

## 4.2.5 Identity-Associated Symbolic Regularity

We next examined whether symbolic representations exhibited regularity across
different sketches of the same garment identity.

Across the 230 garment identities, the mean fraction of sketches sharing the
modal primitive sequence was 0.170, with a median of 0.100 and a maximum of
0.700.

Family sequences showed slightly greater consistency, with a mean modal
sequence fraction of 0.207, a median of 0.200, and a maximum of 0.700.

No garment identity had all of its sketches represented by a single primitive
sequence or by a single family sequence.

We therefore evaluated identity-associated similarity at the primitive-set
level, where ordering is ignored and only the presence or absence of learned
primitives is retained.

Within-identity primitive sets showed a mean Jaccard similarity of 0.326 and
a median of 0.333. Corresponding between-identity values were lower, with a
mean of 0.241 and a median of 0.222.

The mean within-minus-between separation was therefore 0.085.

The comparison was based on 10,340 within-identity pairs and an equal number
of between-identity pairs. No empty primitive sets were present.

These results indicate that sketches of the same garment tend to share more
of their primitive vocabulary than sketches from different garment
identities. However, the magnitude of this separation is modest, and the
absence of any identity with complete sequence invariance demonstrates that
the symbolic representation should not be interpreted as an identity-specific
encoding.

---

## 4.2.6 Cross-Identity Symbolic Reuse

The symbolic patterns observed within individual identities were also
examined for reuse across different identities.

A total of 160 primitive sequences were shared by more than one garment
identity, while 198 family sequences were shared across identities.

Consequently, repeated symbolic patterns cannot be interpreted as unique
identifiers of individual garments. Instead, they constitute reusable
structural patterns occurring across multiple garment identities.

Together with the within-identity Jaccard analysis, this result indicates
that the symbolic representation exhibits a combination of
identity-associated regularity and cross-identity reuse. This is consistent
with a vocabulary of reusable structural units rather than a collection of
identity-specific codes.

---

## 4.2.7 Category-Associated Information

We next tested whether primitive usage contained information associated with
garment category.

The benchmark contained 23 garment categories. A classifier based on
primitive-frequency information achieved an observed accuracy of 9.13%,
compared with 4.35% for a uniform 23-category baseline.

The observed accuracy was therefore approximately 2.1 times the uniform
baseline.

The result indicates that primitive usage contains category-associated
information above the uniform baseline. However, the absolute classification
accuracy remains low. The finding is therefore interpreted as evidence of
category-related information in primitive usage rather than as evidence of
strong category classification.

---

## 4.2.8 Primitive–Geometry Associations

To determine whether primitive usage was systematically associated with
independently measured properties of the sketches, primitive fractions were
tested against two geometry variables: `signature_length` and
`foreground_fraction`.

A total of 24 association tests were performed using Spearman correlation,
with false-discovery-rate correction for multiple comparisons.

Twenty of the 24 tests were FDR-significant, and the maximum absolute
correlation was

\[
|\rho| = 0.317.
\]

The strongest association was observed for P3 and `signature_length`:

\[
\rho = 0.317,\qquad q = 2.19\times10^{-53}.
\]

Other comparatively strong associations included P7 with signature length
(\(\rho=0.308\)), P8 with signature length (\(\rho=0.295\)), P5 with
signature length (\(\rho=0.249\)), P0 with signature length
(\(\rho=0.224\)), and P4 with signature length (\(\rho=0.219\)).

The strongest geometry association for each primitive was:

| Primitive | Strongest geometry variable | Spearman rho | FDR q-value |
|---|---|---:|---:|
| P0 | signature length | +0.224 | 5.89 × 10^-27 |
| P1 | signature length | -0.045 | 3.90 × 10^-02 |
| P2 | signature length | -0.141 | 2.36 × 10^-11 |
| P3 | signature length | +0.317 | 2.19 × 10^-53 |
| P4 | signature length | +0.219 | 8.04 × 10^-26 |
| P5 | signature length | +0.249 | 5.60 × 10^-33 |
| P6 | foreground fraction | +0.172 | 3.39 × 10^-16 |
| P7 | signature length | +0.308 | 1.81 × 10^-50 |
| P8 | signature length | +0.295 | 2.30 × 10^-46 |
| P9 | signature length | +0.165 | 4.66 × 10^-15 |
| P10 | foreground fraction | +0.037 | 8.87 × 10^-02 |
| P11 | signature length | +0.110 | 1.99 × 10^-07 |

P10 showed no FDR-significant independent geometry association.

Thus, geometry associations were heterogeneous across the primitive vocabulary
rather than uniform across all primitives.

The correlations are moderate in magnitude despite extremely small
p-values, indicating that primitive usage is systematically associated with
measured geometry but does not deterministically encode these geometric
variables.

---

## 4.2.9 Primitive Morphology Profiles

To characterize the heterogeneous geometry associations at the level of
individual primitives, each primitive was assigned a morphology profile based
on its weighted associations with `signature_length` and
`foreground_fraction`.

Profiles were successfully constructed for all 12 primitives.

The mean pairwise profile distance was 1.764, with a median of 1.497.
Pairwise distances ranged from 0.177 to 4.373.

The most separated primitive profiles were:

| Primitive pair | Profile distance |
|---|---:|
| P6 – P7 | 4.373 |
| P6 – P8 | 4.252 |
| P4 – P6 | 4.110 |
| P3 – P6 | 3.885 |
| P5 – P6 | 3.663 |

Thus, the frozen primitives occupy heterogeneous regions of the measured
morphology space.

These profiles should be interpreted as computational morphology
descriptors. They do not establish that individual primitives correspond to
independently validated human-interpretable garment parts.

---

## 4.2.10 Benchmark Synthesis

The independent CLO-SK evaluation provides convergent evidence that the
frozen primitive representation captures multiple forms of measurable
structure.

First, the representation is complete with respect to the transferred
event stream: all 2,299 benchmark images and all 12,024 transferred events
are represented without missing primitive or family assignments.

Second, raw geometry substantially outperforms symbolic representations for
direct identity retrieval, including under the cross-sketcher condition.
This establishes that the symbolic representation does not preserve the full
image-level geometric information available to the continuous representation.

Third, symbolic representations nevertheless exhibit measurable structure.
Primitive-set similarity is higher within garment identities than between
identities, primitive usage contains category-associated information above
the uniform baseline, and primitive usage shows systematic associations with
independently measured geometry.

Fourth, the symbolic vocabulary exhibits both reuse and differentiation.
Primitive and family sequences recur across multiple garments and identities,
while substantial sequence diversity is retained.

Finally, the 12 primitives occupy heterogeneous morphology-associated
profiles.

These findings are complementary rather than interchangeable. Retrieval
performance demonstrates information loss relative to raw geometry, whereas
the identity, category, reuse, and morphology analyses demonstrate that the
symbolic representation nevertheless contains structured and reusable
information.

---

# 4.3 Primary Research Corpus

## 4.3.1 Primitive-Level Bigram Similarity

The primary corpus contained 333 garment sequences, producing

\[
\binom{333}{2}=55,278
\]

unique unordered garment pairs.

At the individual primitive level, bigram similarity was sparse. Of the
55,278 garment pairs, 16,950 pairs (30.66%) exhibited non-zero cosine
similarity, indicating that approximately one-third of garment pairs shared
at least one observed primitive bigram.

Across all garment pairs, the primitive-level bigram representation had a
median cosine similarity of 0.00. The 95th percentile of the similarity
distribution was 0.427, demonstrating a non-zero upper tail of garments with
stronger shared local transition structure.

Among pairs with non-zero similarity, the median cosine similarity was
0.225, with the 75th, 90th, and 95th percentiles reaching 0.352, 0.507, and
0.601, respectively.

The representation became substantially more similar after abstraction from
individual primitives to the broader primitive-family representation. At
the family level, pairwise bigram cosine similarity had a mean of
approximately 0.399 and a median of approximately 0.410, compared with a
primitive-level mean of approximately 0.084 and a median of 0.00.

Thus, collapsing individual primitives into broader families substantially
increased pairwise similarity in local transition representations.

These results indicate that garments that differ substantially in their
specific primitive-to-primitive transitions can nevertheless exhibit shared
higher-order transition structure when individual primitives are represented
by their broader geometric families.

---

## 4.3.2 Family-Level Sequential Organization

To determine whether the family-level transition structure was itself
non-random, family sequences were evaluated against a within-garment
permutation null model.

For each garment, the observed family identities were retained while their
sequential ordering was randomly permuted. This preserves the family
composition of each garment while disrupting its observed ordering.

The resulting null distributions were used to evaluate enrichment and
depletion of family-to-family transitions. Multiple comparisons were
corrected using the Benjamini–Hochberg false-discovery-rate procedure.

At the family level, The benchmark contained 230 garment identities distributed across 23
garment categories and 12 sketchers. Each benchmark image received a valid
frozen primitive and family representation, yielding 12,024 transferred
geometry events across the 2,299 images. The frozen vocabulary comprised
12 geometry primitives organized into three higher-level primitive families.
were significantly enriched relative to the permutation null:

| Family transition | Observed | Null expected | Enrichment | FDR |
|---|---:|---:|---:|---:|
| A → C | 86 | 55.14 | 1.56× | 0.0006 |
| B → C | 230 | 178.02 | 1.29× | 0.0006 |
| C → B | 195 | 178.30 | 1.09× | 0.0319 |
| B → B | 706 | 651.25 | 1.08× | 0.0006 |

The remaining family transitions were not enriched under the upper-tail
test.

A complementary lower-tail analysis identified significantly depleted family
transitions. In particular, C → C was completely absent in the observed
corpus while approximately 36.27 such transitions were expected under the
within-garment permutation null. This depletion remained significant after
FDR correction.

Additional depleted transitions included C → A, A → A, A → B, and B → A.

Together, the enrichment and depletion analyses indicate that family-level
sequential organization is not adequately described by random ordering of
the same family composition.

---

# 4.4 RQ011 — Morphological Coherence of Learned Primitives

Learned primitive assignments exhibit strong internal morphological
coherence, with within-primitive similarity substantially exceeding
between-primitive similarity under the specified Euclidean-distance-to-
similarity transformation.

Across the 1,934 persistent geometry-event curves, the mean within-primitive
similarity was

\[
0.3935,
\]

whereas the mean between-primitive similarity was

\[
0.0685.
\]

The resulting within-to-between similarity ratio was approximately

\[
5.74.
\]

To assess whether this separation could arise from random assignment of
primitive labels, primitive memberships were randomly permuted while
preserving the observed primitive group sizes. A total of 5,000 permutations
were performed using a fixed random seed of 42.

The observed difference between within- and between-primitive similarity was

\[
\Delta_{\mathrm{obs}}=0.3249,
\]

whereas the permutation null distribution was centered near zero, with a
mean difference of approximately

\[
1.38\times10^{-5}.
\]

The empirical permutation test yielded

\[
p=0.00020.
\]

Thus, curves assigned to the same learned primitive exhibit substantially
greater morphological similarity than curves assigned to different
primitives, and this separation is unlikely under random assignment of
primitive labels.

The morphological organization was substantially stronger at the
learned-primitive level than under the predefined semantic-family grouping.
This indicates that the learned primitive identities capture coherent
geometric variation that is not simply equivalent to the predefined
higher-level family taxonomy.

---

# 4.5 RQ012 — Context-Dependent Morphological Variation

We next examined whether the morphology of a current primitive varied
systematically according to its immediately preceding primitive.

Contexts were considered only when at least 10 curves were available,
yielding 43 usable primitive-transition contexts and 10 current primitives
for the aggregated context-effect analysis.

Across the tested current primitives, curves sharing the same
preceding-primitive context showed a small positive increase in morphological
similarity relative to curves drawn from different preceding-primitive
contexts.

The mean within-context minus between-context difference was

\[
0.0049.
\]

To assess whether this effect could arise from the observed context group
sizes alone, context labels were randomly permuted within each current
primitive while preserving the original context sizes.

Across 5,000 permutations, the null distribution had a mean difference of
approximately

\[
1.2\times10^{-5},
\]

with a 95% interval of

\[
[-0.0050,\;0.0064].
\]

The observed effect did not reach statistical significance
(empirical permutation \(p=0.0856\)).

Thus, immediate preceding-primitive context showed a small positive
morphological effect, but the present analysis does not provide sufficient
evidence that primitive morphology systematically depends on its immediate
predecessor.

---

# 4.6 RQ013 — Predictive Sequential Organization of Geometry Primitives

Garment primitive sequences exhibit structured, predictive sequential
dependencies.

To test whether the observed sequential organization provides predictive
information beyond marginal primitive frequency, we evaluated a first-order
context-conditioned predictor that predicts the next primitive from its
immediately preceding primitive.

Across 1,601 observed primitive transitions, the context-conditioned
maximum-probability predictor achieved an accuracy of

\[
30.73\%,
\]

compared with

\[
15.30\%
\]

for a global-majority baseline.

This corresponds to an absolute improvement of 15.43 percentage points and
a relative improvement of 100.8%.

A permutation test with 5,000 randomized target assignments yielded an
empirical

\[
p=0.00020,
\]

indicating that the observed predictive advantage was unlikely under
randomized target assignments.

### Unseen-Garment Generalization

We next evaluated whether this predictive structure generalized to garments
that were not used to estimate the transition probabilities.

The corpus was divided into 266 training garments and 67 completely unseen
test garments. The test set contained 323 primitive transitions.

On these unseen garments, the context-conditioned predictor achieved

\[
30.34\%
\]

next-primitive prediction accuracy, compared with

\[
8.05\%
\]

for the training-set global-majority baseline.

This represents an absolute improvement of 22.29 percentage points,
corresponding to a 276.9% relative improvement over the baseline.

Thus, immediate primitive context retained substantial predictive value even
when evaluated on garments excluded from estimation of the transition model.

### Higher-Order Context

We further examined whether extending the context from one preceding
primitive to two preceding primitives provided substantially greater
predictive information.

The second-order model produced only a modest additional improvement over
the first-order representation, indicating that most of the measurable
predictive advantage was already captured by immediate predecessor context.

Predictive performance also varied across primitive types, indicating that
some primitives occupy more contextually constrained sequential positions
than others.

### Interpretation

These results provide evidence that garment primitive sequences contain
predictive sequential structure beyond marginal primitive frequency.

In particular, immediate primitive context substantially improves prediction
of the next primitive, and this predictive advantage generalizes to previously
unseen garments.

The result supports interpreting the learned transition structure as a
component of the proposed Visual Grammar. However, the analysis establishes
**predictive sequential organization**, rather than a complete generative
model of garment language.

---

# 4.7 RQ014 — Primitive Structural Profiles

Each learned primitive exhibits a measurable structural profile characterized
by its morphology, typical position within the garment sequence, and local
sequential neighborhood.

## Positional Specialization

Primitive occurrence positions were represented using normalized sequence
position, with the first and last events corresponding approximately to 0
and 1, respectively.

Position distributions were compared across the 12 learned primitives using
the Kruskal–Wallis test.

The analysis revealed a strong association between primitive identity and
structural position:

\[
H=637.09,
\]

with

\[
p\approx1.62\times10^{-129},
\]

and an epsilon-squared effect size of

\[
\epsilon^2=0.326.
\]

Thus, primitive identities are strongly associated with characteristic
locations within garment sequences.

## Position-Zone Profiles

To characterize positional specialization, occurrences were divided into
three normalized sequence zones: early, middle, and late.

The resulting profiles showed distinct positional tendencies across
primitives.

P2 was strongly concentrated in the early portion of garment sequences,
with approximately 86.7% of its occurrences classified as early.

In contrast, P6 and P11 were predominantly late, with approximately 81% of
occurrences occurring in the late zone.

P5, P8, and P9 exhibited greater concentration in the middle region, while
other primitives displayed broader positional distributions.

These distributions indicate that learned primitive identities are not
uniformly distributed along garment sequences but exhibit characteristic
positional profiles.

## Contextual Neighborhood Profiles

We further characterized each primitive according to its immediate sequential
neighborhood.

For every primitive, we measured the number of distinct predecessor and
successor primitive types and identified the most frequent predecessor and
successor.

The resulting profiles showed substantial variation in contextual
specificity.

Some primitives exhibited relatively concentrated sequential neighborhoods.
For example, P11 was frequently preceded by P3, P10 was frequently preceded
by P0, and P9 was frequently preceded by P0.

Other primitives exhibited broader contextual distributions; for example,
P1 occurred with 11 distinct predecessor types.

These differences indicate that primitive identities are associated with
characteristic local sequential contexts, although the present analysis is
descriptive and does not by itself establish statistical significance for
individual contextual associations.

## Structural Interpretation

Taken together, the positional, morphological, and contextual analyses
indicate that each learned primitive can be characterized by a measurable
structural profile:

\[
\text{Primitive Structural Profile}
=
\text{Morphology}
+
\text{Sequence Position}
+
\text{Predecessor Context}
+
\text{Successor Context}.
\]

Semantic-family assignment is retained as an associated categorical
attribute rather than as an intrinsic component of the structural profile.

These structural profiles provide a higher-order computational description
of primitive identity.

Importantly, this analysis should be interpreted as a computational
characterization of structural organization rather than as independently
validated human semantic labeling.

---

# 4.8 RQ015 — Primitive Knowledge Representation

The independently established morphological, positional, semantic-family,
and sequential characteristics of the learned primitives were integrated
into an explicit primitive-level knowledge representation.

For each of the 12 learned primitives, the resulting knowledge profile
records:

- morphological coherence;
- morphological cluster assignment;
- predefined semantic-family assignment;
- number of observed curves;
- mean and median sequence position;
- positional variability;
- dominant positional zone;
- positional preference;
- number of distinct predecessor types;
- number of distinct successor types;
- most common predecessor primitive; and
- most common successor primitive.

This representation provides a compact structural description of each
learned primitive by integrating complementary evidence established in the
preceding analyses.

The resulting representation allows each primitive to be characterized by a
measurable structural role combining its morphological identity, typical
position within the garment sequence, semantic-family assignment, and local
sequential neighborhood.

Importantly, these structural roles are computational descriptors derived
from the learned representation and should not be interpreted as independently
validated human semantic labels.

Thus, RQ015 establishes a **primitive-level knowledge representation** that
integrates independently measured properties of the learned geometric
vocabulary without introducing additional unsupported metrics or semantic
assumptions.

---

# 4.9 RQ016 — Structural Organization of Semantic Families

We next examined whether the predefined semantic-family taxonomy corresponded
to the integrated structural organization of the learned primitives.

Each primitive was represented using eight fixed structural features
capturing morphological coherence, sequence position, positional variability,
positional-zone distribution, and predecessor and successor diversity.

The resulting representation contained 12 learned primitives and was
evaluated through all 66 unique pairwise structural comparisons. Euclidean
distance was used to quantify structural dissimilarity between primitives.

The mean structural distance between primitives belonging to the same
semantic family was

\[
3.7399,
\]

whereas the mean distance between primitives belonging to different families
was

\[
4.1138.
\]

Thus, within-family primitives were modestly more structurally similar than
between-family primitives, corresponding to a separation ratio of
approximately

\[
1.10\times.
\]

To assess whether this observed separation could arise from the family
assignments alone, family labels were randomly permuted across the 12
primitives while preserving the observed family sizes.

A total of 5,000 permutations were performed using a fixed random seed of 42.

The observed separation did not reach statistical significance under the
permutation null:

\[
p=0.095.
\]

Therefore, although the predefined semantic families showed **modest
structural alignment** with the integrated primitive representation, the
observed separation was not statistically significant.

These results indicate that the predefined semantic-family taxonomy does not
strongly account for the multidimensional structural organization learned
from the garment geometry.

Accordingly, the structural organization captured by the learned primitive
representation should not be interpreted as simply reproducing the
predefined family labels.

---

# 4.10 RQ017 — Compositional Representation of Complete Garments

Complete garments can be represented as ordered sequences drawn from the
learned 12-primitive vocabulary.

Across the 333-garment corpus, all 12 learned primitives were represented,
while individual garments typically instantiated only a subset of the
available vocabulary.

The mean number of unique primitives used per garment was

\[
4.303,
\]

with a median of

\[
4
\]

unique primitives per garment.

Thus, although the learned vocabulary contains 12 recurring geometric units,
individual garments generally require only a relatively small subset of the
available vocabulary to construct their structural descriptions.

At the corpus level, primitive sequences also produced a recurring vocabulary
of primitive-to-primitive transitions, providing a representation of how
learned geometric units are composed sequentially within complete garments.

These observations support a **compositional representation** in which
complete garment structures are assembled from relatively small subsets of
recurring geometry primitives drawn from a shared corpus-level vocabulary.

Importantly, compositionality here refers to the computational representation
of garment structure as ordered combinations of learned geometric primitives.
It does not imply that the primitives correspond directly to predefined
garment parts or independently validated human semantic concepts.

---

# 4.11 Summary of Results

Taken together, the two evaluation populations provide complementary
evidence about the learned symbolic representation.

The **333-garment primary corpus** establishes the internal organization of
the learned vocabulary. Learned primitives exhibit strong morphological
coherence, characteristic positional and contextual profiles, predictive
sequential organization, reusable transition structure, and a compositional
organization in which complete garments are represented through combinations
of a shared primitive vocabulary.

The frozen representation was subsequently evaluated on an independent
Clo-Sket benchmark [Clo-Sket citation]. The original dataset contains 2,300
sketch images representing 230 source garment identities across 23
subcategories. After preprocessing and integrity checks, 2,299 images were
retained for the present benchmark analysis. Raw geometry substantially
outperforms symbolic representations for direct garment-identity retrieval,
including under the cross-sketcher condition, demonstrating that the symbolic
representation does not preserve all image-level geometric information.

At the same time, the CLO-SK benchmark shows that the frozen symbolic
representation contains measurable and reusable structure. Primitive-set
similarity is higher within garment identities than between identities,
primitive usage contains category-associated information above the uniform
baseline, symbolic patterns recur across multiple identities, and primitive
usage is systematically associated with independently measured geometric
properties.

The benchmark morphology analysis further shows that the 12 primitives occupy
heterogeneous regions of measured geometry space.

Together, these findings support a **structured, compositional, and reusable
symbolic representation of garment sketches**.

The evidence does not support the stronger claim that the learned vocabulary
constitutes a complete human-interpretable semantic language. Nor does it
establish that individual primitives correspond directly to independently
validated garment concepts.

Instead, the results support the narrower scientific claim that garment
sketches contain recurring geometric units and sequential regularities that
can be represented computationally as a structured symbolic vocabulary.

This distinction defines the evidential boundary of the present study.