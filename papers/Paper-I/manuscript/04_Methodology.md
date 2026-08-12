# 4. Methods

## 4.1 Dataset and Sketch Corpus

The study was conducted on a corpus of 333 fashion garment sketches. Each sketch was processed independently and represented as a one-dimensional geometric signal describing variation in garment width along the vertical axis.

The resulting geometric representation was used as the basis for identifying localized geometric events, learning recurring geometric primitives, and constructing ordered symbolic representations of complete garments.

The analysis was designed as a geometry-first pipeline in which symbolic representations were derived from measurable geometric structure rather than from predefined semantic garment categories.

## 4.2 Color Image to V1 Line-Art Sketch

Color fashion images were converted into V1 line-art sketches using the LineartDetector. The resulting line-art representation was used for subsequent geometric analysis.

Each V1 sketch was converted into a binary representation in which foreground sketch structure was separated from the background. This representation provided the input for extraction of the garment's vertical boundary geometry.

## 4.3 Silhouette Boundary Extraction and Width Signature

For each binary sketch, the leftmost and rightmost foreground coordinates were identified at each retained vertical position. These boundary trajectories were smoothed using a seven-sample moving-average filter.

The garment width at each vertical position was calculated from the separation between the smoothed left and right boundaries, producing a one-dimensional width signature,

\[
W(y),
\]

where \(y\) denotes normalized or discrete vertical position.

The width signature provides a compact geometric signal describing how garment width changes along the vertical extent of the sketch. This signal was subsequently used for candidate event detection.

## 4.4 Candidate Geometric Event Detection

The width signature was analyzed as a one-dimensional geometric signal. Numerical first and second derivatives were computed to characterize local changes in width and curvature.

Candidate event boundaries were identified from changes in the direction of the first derivative. The resulting boundaries partitioned the width signature into consecutive intervals.

Each interval was represented as a `CandidateEvent` characterized by:

- event type (rise, fall, or plateau);
- start and end positions;
- event length;
- amplitude;
- mean and maximum gradient;
- mean and maximum curvature.

Candidate detection intentionally over-segmented the signal. Candidate events were therefore treated as provisional geometric intervals rather than final symbolic units.

## 4.5 Persistent Geometry Event Extraction

Candidate events were filtered to remove short or low-amplitude signal segments. An event was retained when both of the following conditions were satisfied:

\[
L_i \geq L_{\min}
\]

and

\[
|A_i| \geq A_{\min},
\]

where the implementation used \(L_{\min}=8\) samples and \(A_{\min}=3\) pixels.

Adjacent candidate events with the same event type were subsequently merged. For a merged event, the spatial extent was defined by the first and last constituent events, while amplitude and differential-geometric descriptors were aggregated from the constituent segments.

The surviving events were converted into `GeometryEvent` objects and stored in their original order within a `GeometrySequence`.

The resulting representation was therefore:

\[
\text{Candidate Events}
\rightarrow
\text{Persistence Filtering}
\rightarrow
\text{Event Merging}
\rightarrow
\text{Geometry Events}
\rightarrow
\text{Geometry Sequence}.
\]

Across the corpus, this procedure produced 1,934 persistent geometry events from the 333 garment sketches.

## 4.6 Geometry Primitive Discovery

### 4.6.1 Event-Curve Normalization

Each persistent geometry event was represented by its corresponding local width-signature curve. Because event intervals differed in length and absolute amplitude, each curve was resampled to a fixed length of 64 points.

For a curve \(c\), its horizontal coordinate was normalized to the interval \([0,1]\), and linear interpolation was used to obtain the fixed-length representation. The resulting curve was then shifted so that its minimum value was zero and, when non-constant, divided by its maximum value.

Thus, the representation emphasizes the normalized shape of local geometric variation while reducing differences caused by event length and absolute amplitude.

### 4.6.2 Feature Representation and Clustering

The normalized event curves were represented as fixed-length feature vectors. Event-level feature vectors were standardized before clustering using `StandardScaler`.

K-means clustering was then applied to the standardized representations with the number of clusters fixed at 12 and a random seed of 42.

The resulting 12 clusters define the learned geometry primitive vocabulary. Cluster identities were assigned as primitive identifiers \(P_0,\ldots,P_{11}\).

The primitive vocabulary was learned without using predefined semantic-family labels. The resulting cluster assignments were subsequently used to construct symbolic garment sequences and evaluate morphological and sequential organization.

The learned representation can therefore be summarized as:

\[
\text{Persistent Geometry Event}
\rightarrow
\text{Normalized Local Curve}
\rightarrow
\text{Standardized Feature Vector}
\rightarrow
\text{Learned Geometry Primitive}.
\]

## 4.7 Primitive Morphological Representation

To evaluate whether the learned primitive assignments corresponded to coherent geometric morphology, pairwise Euclidean distances were computed between normalized event curves.

Euclidean distances were converted to a monotonic similarity representation for comparison of morphological resemblance. Within-primitive similarity was calculated among curves assigned to the same learned primitive, while between-primitive similarity was calculated among curves assigned to different primitives.

The observed separation between within- and between-primitive similarity was evaluated using a permutation test. Primitive labels were randomly reassigned while preserving the observed size of each primitive group.

A total of 5,000 permutations were performed using a fixed random seed of 42. For each permutation, the difference between mean within-group and between-group similarity was recomputed.

The empirical significance probability was calculated as

\[
p =
\frac{
N_{\mathrm{null}}
(\Delta_{\mathrm{null}}\geq\Delta_{\mathrm{obs}})
+1
}{
N_{\mathrm{perm}}+1
}.
\]

This procedure evaluates whether the observed morphological separation could plausibly arise from random assignment of primitive identities.

## 4.8 Garment Sentences and Sequential Representation

For each garment, persistent geometry events were ordered according to their vertical occurrence in the width signature. Each event was associated with its learned primitive identifier, producing an ordered primitive sentence,

\[
S_g=(P_1,P_2,\ldots,P_n),
\]

where \(P_i\) denotes the primitive assigned to the corresponding event.

Consecutive primitive identities define directed transitions,

\[
P_i \rightarrow P_{i+1}.
\]

Corpus-level transition counts were obtained by aggregating consecutive primitive pairs across all garment sentences.

Conditional transition probabilities were calculated as

\[
P(P_j\mid P_i)
=
\frac{N(P_i\rightarrow P_j)}
{\sum_k N(P_i\rightarrow P_k)}.
\]

These probabilities provide a first-order representation of sequential organization among the learned primitives.

## 4.9 Sequential Organization and Permutation Testing

### 4.9.1 Primitive-Level Transition Enrichment

To determine whether observed primitive transitions reflected non-random sequential organization, a within-garment permutation null model was used.

For each garment, the observed set of primitive identities was retained while their ordering was randomly permuted. This preserves the primitive composition of each garment while disrupting its original sequential arrangement.

A total of 5,000 within-garment permutations were generated. Transition counts were recomputed for each permutation to obtain empirical null distributions for the observed transition types.

For each transition, an empirical upper-tail probability was calculated by comparing the observed transition count with its permutation distribution. Complementary lower-tail testing was used to identify transitions occurring significantly less frequently than expected under the null model.

Multiple comparisons were corrected using the Benjamini–Hochberg false-discovery-rate procedure with \(\alpha=0.05\).

The resulting enriched and depleted transition sets were used to characterize statistically structured sequential organization among the learned primitives.

### 4.9.2 Primitive-Family Sequential Organization

A predefined mapping from the 12 learned primitives to three broader primitive families was used to evaluate whether sequential organization persisted at a higher level of abstraction.

Each primitive sequence was transformed into its corresponding family sequence. Family-to-family transition counts were then compared with a within-garment permutation null model using the same principle as the primitive-level analysis.

Both upper-tail enrichment and lower-tail depletion were evaluated, and the resulting probabilities were corrected using the Benjamini–Hochberg false-discovery-rate procedure.

This analysis tests whether sequential regularities remain observable after individual primitive identities are collapsed into broader family categories.

### 4.9.3 Garment-Level Bigram Similarity

To evaluate recurring local sequential structure across complete garments, each garment sentence was represented by the frequency of its consecutive primitive bigrams.

For garment \(g\),

\[
B_g =
\{(P_i,P_{i+1})\}_{i=1}^{n-1}.
\]

Each garment was represented as a frequency vector over the corpus-level primitive-bigram vocabulary. Pairwise cosine similarity was then calculated between all unordered garment pairs.

For two garments \(g_a\) and \(g_b\),

\[
\operatorname{cos}(g_a,g_b)
=
\frac{
\mathbf{b}_{g_a}\cdot\mathbf{b}_{g_b}
}{
\|\mathbf{b}_{g_a}\|
\|\mathbf{b}_{g_b}\|
}.
\]

The same procedure was repeated after replacing individual primitive identifiers with their corresponding family identifiers. This produced family-level bigram representations.

All pairwise comparisons were performed over the complete set of 333 garments, yielding

\[
\binom{333}{2}=55,278
\]

unique unordered garment pairs.

This analysis distinguishes corpus-level transition enrichment from garment-level recurrence of local transition structure.

## 4.10 Context-Dependent Morphological Analysis

To examine whether the morphology of a primitive varied according to its immediate sequential context, event curves were grouped by their current primitive and immediately preceding primitive.

Only contexts containing at least 10 curves were retained for analysis. This yielded 43 usable primitive-transition contexts across 10 current primitives.

For each current primitive, morphological similarity was compared between curves sharing the same preceding-primitive context and curves belonging to different preceding-context groups.

The observed effect was defined as the difference between mean within-context similarity and mean between-context similarity.

To evaluate whether the observed effect could arise from the observed context-group sizes alone, context labels were randomly permuted within each current primitive while preserving the original context sizes.

A total of 5,000 permutations were performed. The empirical \(p\)-value was calculated from the resulting null distribution using the same Monte Carlo framework described above.

This analysis tests whether immediate preceding-primitive context is associated with measurable variation in the continuous morphology of the current primitive.

## 4.11 Predictive Sequential Analysis

The predictive value of primitive context was evaluated using a first-order maximum-probability predictor.

For each source primitive \(P_i\), the next primitive was predicted as the most frequently observed successor under the estimated transition distribution,

\[
\hat{P}_{i+1}
=
\arg\max_j P(P_j\mid P_i).
\]

Performance was compared with a global-majority baseline that always predicted the most frequent primitive in the relevant estimation set.

A permutation test with 5,000 randomized target assignments was used to assess whether the observed predictive advantage could arise under randomized next-primitive assignments.

### 4.11.1 Unseen-Garment Generalization

To evaluate generalization beyond the garments used to estimate transition probabilities, the corpus was divided into 266 training garments and 67 completely unseen test garments.

Transition probabilities were estimated using the training garments only. The resulting first-order predictor was then evaluated on the primitive transitions of the 67 unseen garments, which contained 323 observed transitions.

Prediction accuracy was compared with the global-majority baseline derived from the training set.

### 4.11.2 Higher-Order Context

A second-order predictor was also evaluated by conditioning the predicted next primitive on the two immediately preceding primitive identities.

Its performance was compared with the first-order model to determine whether extending the sequential context provided substantial additional predictive information.

## 4.12 Primitive Structural Profiles

Each learned primitive was characterized using three complementary structural dimensions: normalized sequence position, predecessor neighborhood, and successor neighborhood.

For an event occurring at index \(i\) within a sequence containing \(n\) events, normalized position was calculated as

\[
\frac{i}{\max(1,n-1)}.
\]

For each primitive, the mean, median, and standard deviation of normalized positions were calculated.

Primitive position distributions were compared using the Kruskal–Wallis test. Effect size was quantified using epsilon-squared,

\[
\epsilon^2 =
\frac{H-k+1}{N-k},
\]

where \(H\) is the Kruskal–Wallis statistic, \(k\) is the number of primitive groups, and \(N\) is the total number of primitive occurrences.

For descriptive positional profiling, occurrences were additionally divided into three normalized sequence zones:

- early: \(0 \leq x < 1/3\);
- middle: \(1/3 \leq x < 2/3\);
- late: \(2/3 \leq x \leq 1\).

For sequential neighborhood characterization, the number of distinct predecessor and successor primitive types was calculated for each primitive, together with the most frequently observed predecessor and successor.

These analyses provide a structural profile of each primitive without assigning independently validated human semantic labels.

## 4.13 Primitive Knowledge Representation

The measurements established in the preceding analyses were integrated into a primitive-level knowledge representation.

For each of the 12 primitives, the representation included:

- mean morphological coherence;
- morphological cluster assignment;
- predefined semantic-family assignment;
- number of observations;
- mean and median sequence position;
- positional standard deviation;
- early, middle, and late occurrence fractions;
- number of distinct predecessor types;
- number of distinct successor types;
- most common predecessor; and
- most common successor.

No additional statistical inference was introduced at this stage. RQ015 therefore functions as an integration layer that consolidates independently measured primitive properties into an explicit structural knowledge table.

## 4.14 Structural Organization of Semantic Families

To examine whether the predefined three-family taxonomy corresponded to the integrated structural organization of the learned primitives, each primitive was represented using eight fixed structural features:

1. mean morphological coherence;
2. mean sequence position;
3. positional standard deviation;
4. early-position fraction;
5. middle-position fraction;
6. late-position fraction;
7. number of distinct predecessor types; and
8. number of distinct successor types.

The eight features were standardized using `StandardScaler`.

Euclidean distance was then calculated between every pair of the 12 learned primitives, yielding

\[
\binom{12}{2}=66
\]

unique primitive-pair comparisons.

Pairwise distances were separated into within-family and between-family groups according to the predefined primitive-family assignments.

The observed family separation was defined as

\[
\Delta =
\bar{D}_{\mathrm{between}}
-
\bar{D}_{\mathrm{within}}.
\]

Statistical significance was assessed using a permutation test in which family labels were randomly reassigned across the 12 primitives while preserving the observed family sizes.

A total of 5,000 permutations were performed using a fixed random seed of 42. For each permutation, the between-family and within-family mean distances were recomputed and their difference recorded.

The resulting empirical distribution was used to determine whether the observed family separation was greater than expected under randomized family assignments.

## 4.15 Garment-Level Compositional Representation

Complete garment structures were represented as ordered sequences of learned primitives.

For each garment, the following quantities were calculated:

- number of persistent geometry events;
- number of primitive events;
- number of unique primitives represented;
- primitive sequence;
- sequence length; and
- primitive entropy.

Primitive vocabulary coverage was calculated by counting the total number of occurrences of each primitive across the garment corpus and the number of garments containing each primitive.

Garment-level structural diversity was characterized using the number of unique primitives occurring in each garment. The mean, median, minimum, and maximum number of unique primitives per garment were calculated.

Primitive-to-primitive transitions were also aggregated across garment sequences to characterize the recurring local sequential composition of complete garment representations.

This analysis evaluates whether complete garment sketches can be represented compositionally as ordered combinations of a relatively small subset of recurring primitives drawn from a shared corpus-level vocabulary.

## 4.16 Statistical Testing and Reproducibility

Statistical analyses used non-parametric tests and empirical permutation procedures where appropriate to avoid relying on parametric assumptions about the distributions of geometric similarity or structural distances.

Permutation analyses used fixed random seeds where specified, enabling reproducibility of the reported empirical results.

For analyses involving multiple transition types, statistical significance was controlled using the Benjamini–Hochberg false-discovery-rate procedure.

The analyses were designed to distinguish between:

- descriptive characterization of the learned representation;
- statistical association between primitive identity and morphology or position;
- enrichment or depletion of sequential transitions;
- predictive utility of sequential context; and
- structural correspondence between learned primitives and predefined semantic families.

Higher-order semantic interpretations were not treated as independently validated semantic ground truth. They were instead constructed as interpretations of the measurable geometric, positional, morphological, and sequential relationships established by the preceding analyses.