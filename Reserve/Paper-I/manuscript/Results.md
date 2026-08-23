### Results

The corpus contained 333 garment sentences, producing

\[
\binom{333}{2}=55,278
\]

unique unordered garment pairs.

At the individual primitive level, bigram similarity was sparse. Of the 55,278 garment pairs, 16,950 pairs (30.66%) exhibited non-zero cosine similarity, indicating that approximately one-third of garment pairs shared at least one observed primitive bigram.

Across all garment pairs, the primitive-level bigram representation had a median cosine similarity of 0.00, indicating substantial sparsity in exact primitive-transition overlap. The 95th percentile of the similarity distribution was 0.427, demonstrating a non-zero upper tail of garments with stronger shared local transition structure.

Among pairs with non-zero similarity, the median cosine similarity was 0.225, with the 75th, 90th, and 95th percentiles reaching 0.352, 0.507, and 0.601, respectively.

The representation became substantially more similar after abstraction from individual primitives to the three broader primitive families. At the family level, the pairwise bigram cosine similarity had a mean of approximately 0.399 and a median of approximately 0.410, compared with a primitive-level mean of approximately 0.084 and a median of 0.00.

Thus, collapsing individual primitives into broader families substantially increased pairwise similarity in local transition representations.

These results indicate that garments that differ substantially in their specific primitive-to-primitive transitions can nevertheless exhibit shared higher-order transition structure when individual primitives are represented by their broader geometric families.



### Family-Level Sequential Organization

To determine whether the family-level transition structure was itself non-random, family sequences were evaluated against a within-garment permutation null model. For each garment, the observed family identities were retained while their sequential ordering was randomly permuted. This preserves the family composition of each garment while disrupting its observed ordering.

The resulting null distributions were used to evaluate both enrichment and depletion of family-to-family transitions. Multiple comparisons were corrected using the Benjamini–Hochberg false-discovery-rate procedure.

At the family level, 4 of the 9 possible directed family transitions were significantly enriched relative to the permutation null:

| Family transition | Observed | Null expected | Enrichment | FDR |
|---|---:|---:|---:|---:|
| A → C | 86 | 55.14 | 1.56× | 0.0006 |
| B → C | 230 | 178.02 | 1.29× | 0.0006 |
| C → B | 195 | 178.30 | 1.09× | 0.0319 |
| B → B | 706 | 651.25 | 1.08× | 0.0006 |

The remaining family transitions were not enriched under the upper-tail test.

A complementary lower-tail analysis identified significantly depleted family transitions. In particular, C → C was completely absent in the observed corpus while approximately 36.27 such transitions were expected under the within-garment permutation null. This depletion remained significant after FDR correction.

Additional depleted transitions included C → A, A → A, A → B, and B → A.

Together, the enrichment and depletion analyses indicate that the family-level sequential organization is not adequately described by random ordering of the same family composition.


### RQ011. Morphological Coherence of Learned Primitives

Learned primitive assignments exhibit strong internal morphological coherence, with within-primitive similarity substantially exceeding between-primitive similarity under the specified Euclidean-distance-to-similarity transformation.

Across the 1,934 persistent geometry-event curves, the mean within-primitive similarity was

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

To assess whether this separation could arise from random assignment of primitive labels, primitive memberships were randomly permuted while preserving the observed primitive group sizes. A total of 5,000 permutations were performed using a fixed random seed of 42.

The observed difference between within- and between-primitive similarity was

\[
\Delta_{\mathrm{obs}} = 0.3249,
\]

whereas the permutation null distribution was centered near zero, with a mean difference of approximately

\[
1.38\times10^{-5}.
\]

The empirical permutation test yielded

\[
p = 0.00020.
\]

Thus, curves assigned to the same learned primitive exhibit substantially greater morphological similarity than curves assigned to different primitives, and this separation is highly unlikely under random assignment of primitive labels.

The morphological organization was substantially stronger at the learned-primitive level than under the predefined semantic-family grouping. This indicates that the learned primitive identities capture coherent geometric variation that is not simply equivalent to the predefined higher-level family taxonomy.

### RQ012. Context-Dependent Morphological Variation

We next examined whether the morphology of a current primitive varied systematically according to its immediately preceding primitive. Contexts were considered only when at least 10 curves were available, yielding 43 usable primitive-transition contexts and 10 current primitives for the aggregated context-effect analysis.

Across the tested current primitives, curves sharing the same preceding-primitive context showed a small positive increase in morphological similarity relative to curves drawn from different preceding-primitive contexts. The mean within-context minus between-context difference was

\[
0.0049.
\]

To assess whether this effect could arise from the observed context group sizes alone, context labels were randomly permuted within each current primitive while preserving the original context sizes. Across 5,000 permutations, the null distribution had a mean difference of approximately

\[
1.2\times10^{-5},
\]

with a 95% interval of

\[
[-0.0050,\;0.0064].
\]

The observed effect did not reach statistical significance (empirical permutation \(p=0.0856\)).

Thus, immediate preceding-primitive context showed a small positive morphological effect, but the present analysis does not provide sufficient evidence that the morphology of a primitive systematically depends on its immediate predecessor.

### RQ013. Predictive Sequential Organization of Geometry Primitives

Garment primitive sequences exhibit structured, predictive sequential dependencies. To test whether the observed sequential organization provides predictive information beyond marginal primitive frequency, we evaluated a first-order context-conditioned predictor that predicts the next primitive from its immediately preceding primitive.

Across 1,601 observed primitive transitions, the context-conditioned maximum-probability predictor achieved an accuracy of

\[
30.73\%,
\]

compared with

\[
15.30\%
\]

for a global-majority baseline. This corresponds to an absolute improvement of 15.43 percentage points and a relative improvement of 100.8%. A permutation test with 5,000 randomized target assignments yielded an empirical

\[
p = 0.00020,
\]

indicating that the observed predictive advantage was unlikely under randomized target assignments.

#### Unseen-Garment Generalization

We next evaluated whether this predictive structure generalized to garments that were not used to estimate the transition probabilities. The corpus was divided into 266 training garments and 67 completely unseen test garments. The test set contained 323 primitive transitions.

On these unseen garments, the context-conditioned predictor achieved

\[
30.34\%
\]

next-primitive prediction accuracy, compared with

\[
8.05\%
\]

for the training-set global-majority baseline. This represents an absolute improvement of 22.29 percentage points, corresponding to a 276.9% relative improvement over the baseline.

Thus, immediate primitive context retained substantial predictive value even when evaluated on garments excluded from the estimation of the transition model.

#### Higher-Order Context

We further examined whether extending the context from one preceding primitive to two preceding primitives provided substantially greater predictive information. The second-order model produced only a modest additional improvement over the first-order representation, indicating that most of the measurable predictive advantage was already captured by immediate predecessor context.

Predictive performance also varied across primitive types, indicating that some primitives occupy more contextually constrained sequential positions than others.

#### Interpretation

These results provide evidence that garment primitive sequences contain predictive sequential structure beyond marginal primitive frequency. In particular, immediate primitive context substantially improves prediction of the next primitive and this predictive advantage generalizes to previously unseen garments.

The result supports interpreting the learned transition structure as a component of the proposed Visual Grammar. However, the analysis establishes **predictive sequential organization**, rather than a complete generative model of garment language. The learned representation therefore provides evidence for grammar-like organization while remaining directly grounded in the observed geometry-derived primitive sequences.

### RQ014. Primitive Structural Profiles

Each learned primitive exhibits a measurable structural signature characterized by its typical position within the garment sequence and its contextual neighborhood, defined by the primitives that tend to precede and follow it.

#### Positional Specialization

Primitive occurrence positions were represented using normalized sequence position, with the first and last events corresponding approximately to 0 and 1, respectively. Position distributions were compared across the 12 learned primitives using the Kruskal–Wallis test.

The analysis revealed a strong association between primitive identity and structural position:

\[
H = 637.09,
\]

with

\[
p \approx 1.62 \times 10^{-129},
\]

and an epsilon-squared effect size of

\[
\epsilon^2 = 0.326.
\]

Thus, primitive identities are strongly associated with characteristic locations within garment sequences.

#### Position-Zone Profiles

To characterize the positional specialization of individual primitives, occurrences were divided into three normalized sequence zones: early, middle, and late.

The resulting profiles showed distinct positional tendencies across primitives. P2 was strongly concentrated in the early portion of garment sequences, with approximately 86.7% of its occurrences classified as early. In contrast, P6 and P11 were predominantly late, with approximately 81% of occurrences occurring in the late zone. P5, P8, and P9 exhibited greater concentration in the middle region, while other primitives displayed broader positional distributions.

These distributions indicate that learned primitive identities are not uniformly distributed along garment sequences but exhibit characteristic positional profiles.

#### Contextual Neighborhood Profiles

We further characterized each primitive according to its immediate sequential neighborhood. For every primitive, we measured the number of distinct predecessor and successor primitive types and identified the most frequent predecessor and successor.

The resulting profiles showed substantial variation in contextual specificity. Some primitives exhibited relatively concentrated sequential neighborhoods. For example, P11 was frequently preceded by P3, P10 was frequently preceded by P0, and P9 was frequently preceded by P0. Other primitives exhibited broader contextual distributions; for example, P1 occurred with 11 distinct predecessor types.

These differences indicate that primitive identities are associated with characteristic local sequential contexts, although the present analysis is descriptive and does not by itself establish statistical significance for individual contextual associations.

#### Structural Interpretation

Taken together, the positional and contextual analyses indicate that each learned primitive can be characterized by a measurable structural signature:

\[
\text{Primitive Structural Signature}
=
\text{Position}
+
\text{Predecessor Context}
+
\text{Successor Context}.
\]

Thus, learned primitive identities are associated not only with recurring geometric morphology, but also with characteristic positional and sequential contexts within garment sentences.

These structural profiles provide a higher-order description of primitive identity and form an important basis for subsequent semantic representation. Importantly, the present analysis should be interpreted as a computational characterization of structural organization rather than as independently validated human semantic labeling.

### RQ015. Primitive Knowledge Representation

The independently established morphological, positional, semantic-family, and sequential characteristics of the learned primitives were integrated into an explicit primitive knowledge representation.

For each of the 12 learned primitives, the resulting knowledge profile records:

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

This representation provides a compact structural description of each learned primitive by integrating complementary evidence established in the preceding analyses.

The resulting representation allows each primitive to be characterized by a measurable **structural role**, combining its morphological identity, typical position within the garment sequence, semantic-family assignment, and local sequential neighborhood.

Importantly, these structural roles are computational descriptors derived from the learned representation and should not be interpreted as independently validated human semantic labels. Rather, they provide an explicit intermediate representation through which higher-order semantic organization can subsequently be constructed.

Thus, RQ015 establishes a **primitive-level knowledge representation** that integrates the independently measured properties of the learned geometric vocabulary without introducing additional unsupported metrics or semantic assumptions.

### RQ016. Structural Organization of Semantic Families

We next examined whether the predefined semantic-family taxonomy corresponded to the integrated structural organization of the learned primitives. Each primitive was represented using eight fixed structural features capturing morphological coherence, sequence position, positional variability, positional-zone distribution, and predecessor and successor diversity.

The resulting representation contained 12 learned primitives and was evaluated through all 66 unique pairwise structural comparisons. Euclidean distance was used to quantify structural dissimilarity between primitives.

The mean structural distance between primitives belonging to the same semantic family was

\[
3.7399,
\]

whereas the mean distance between primitives belonging to different families was

\[
4.1138.
\]

Thus, within-family primitives were modestly more structurally similar than between-family primitives, corresponding to a separation ratio of approximately

\[
1.10\times.
\]

To assess whether this observed separation could arise from the family assignments alone, family labels were randomly permuted across the 12 primitives while preserving the observed family sizes. A total of 5,000 permutations were performed using a fixed random seed of 42.

The observed between-minus-within family distance difference did not reach statistical significance under the permutation null:

\[
p = 0.095.
\]

Therefore, although the predefined semantic families showed **modest structural alignment** with the integrated primitive representation, the observed separation was not statistically significant.

These results indicate that the predefined semantic-family taxonomy does not strongly account for the multidimensional structural organization learned from the garment geometry. Accordingly, the structural organization captured by the learned primitive representation should not be interpreted as simply reproducing the predefined family labels.

### RQ017. Compositional Representation of Complete Garments

Complete garments can be represented as ordered sequences drawn from the learned 12-primitive vocabulary. Across the 333-garment corpus, all 12 learned primitives were represented, while individual garments typically instantiated only a subset of the available vocabulary.

The mean number of unique primitives used per garment was

\[
4.303,
\]

with a median of

\[
4
\]

unique primitives per garment.

Thus, although the learned vocabulary contains 12 recurring geometric units, individual garments generally require only a relatively small subset of these units to construct their structural descriptions.

At the corpus level, the primitive sequences also produced a recurring vocabulary of primitive-to-primitive transitions, providing a representation of how the learned geometric units are composed sequentially within complete garments.

These observations support a **compositional representation** in which complete garment structures are assembled from a relatively small subset of recurring geometry primitives drawn from a shared corpus-level vocabulary.

Importantly, compositionality here refers to the computational representation of garment structure as ordered combinations of learned geometric primitives. It does not imply that the primitives correspond directly to predefined garment parts or independently validated human semantic concepts.