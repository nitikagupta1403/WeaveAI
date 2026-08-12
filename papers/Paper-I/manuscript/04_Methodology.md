## 4. Methods

### 4.1 Color Image to V1 Line-Art Sketch

Color fashion images are converted into V1 line-art sketches using the LineartDetector. The resulting V1 sketches provide the computational representation used for subsequent geometric analysis.


### 4.2 Silhouette Boundary Extraction and Width Signature

Each V1 line-art sketch is converted into a binary representation. The binary sketch is processed row-wise to identify the leftmost and rightmost foreground coordinates at each retained vertical position. These boundary trajectories are smoothed using a seven-sample moving-average filter.

The garment width at each vertical position is then computed from the separation between the smoothed left and right boundaries, producing a one-dimensional width signature.

The resulting width signature represents garment width as a function of vertical position and provides the geometric signal used for subsequent analysis.


### 4.3 Candidate Geometric Event Detection

The width signature is analyzed as a one-dimensional geometric signal. Its first and second numerical derivatives are computed, and candidate event boundaries are identified from sign changes in the first derivative.

The resulting boundaries partition the width signature into consecutive intervals. Each interval is represented as a candidate geometric event characterized by its direction of change, length, amplitude, gradient, and curvature statistics.

Candidate detection intentionally over-segments the geometric signal. The resulting candidate events are therefore treated as provisional geometric intervals for subsequent persistence analysis.


### 4.4 Persistent Geometry Event Extraction

Candidate geometric events were filtered to remove short or low-amplitude signal segments that were unlikely to represent stable geometric changes. An event was retained when its length satisfied

\[
L_i \geq L_{\min}
\]

and its absolute amplitude satisfied

\[
|A_i| \geq A_{\min},
\]

where the implementation used \(L_{\min}=8\) samples and \(A_{\min}=3\) pixels.

Following this filtering step, adjacent candidate events with the same geometric direction were merged into a single event. For a merged event, the spatial extent was defined by the first and last constituent events, while the amplitude and differential-geometric descriptors were aggregated from the constituent segments.

The surviving events were converted into `GeometryEvent` objects and stored in an ordered `GeometrySequence`. Each resulting event therefore represents a localized geometric change that satisfies the minimum duration and amplitude criteria used by the extraction procedure.

The resulting representation is:

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


### 4.5 Geometry Primitive Discovery

Persistent geometry events provide localized segments of the garment width signature. To determine whether recurring geometric patterns exist across sketches, each persistent event was represented by its corresponding local width-signature curve.

Each event curve was resampled to a fixed number of points and normalized independently in amplitude. This produces a shape-based representation that reduces the influence of differences in event duration and absolute scale while preserving the relative form of the local geometric variation.

The resulting event representations were organized into a curve matrix and analyzed using unsupervised dimensionality reduction and clustering. Principal component analysis (PCA) was used to visualize the distribution of event shapes in the resulting representation space. Agglomerative clustering was then applied to group events exhibiting similar normalized geometric profiles.

For each cluster, a representative prototype curve was computed as the point-wise median of all member curves. These prototypes represent recurring local geometric patterns rather than predefined garment categories or manually specified semantic labels.

The resulting primitive representation provides the basis for constructing a symbolic description of a garment. Each garment can therefore be represented as an ordered sequence of recurring geometric primitives rather than as a collection of independent pixel-level observations.

Primitive sequences were subsequently used to examine transitions between recurring geometric patterns. Transition frequencies were aggregated across garments to construct a primitive transition matrix and directed transition graph. This provides an initial representation of the sequential organization of geometric primitives within garment sketches.

At the corpus level, primitive occurrences were also aggregated into garment-by-primitive representations, allowing garments to be described in terms of their composition of recurring geometric patterns.

The resulting hierarchy is:

\[
\text{Persistent Geometry Event}
\rightarrow
\text{Normalized Local Curve}
\rightarrow
\text{Geometry Primitive}
\rightarrow
\text{Primitive Sequence}
\rightarrow
\text{Primitive Transition Graph}
\]

These primitives provide the reusable structural units from which the subsequent symbolic representation of individual garment sketches is constructed.

### 4.6 Learned Sequential Organization

The learned geometry primitives were used to examine whether recurring geometric structures exhibit systematic sequential organization within garment sketches.

For each garment, the persistent geometry events were ordered according to their vertical occurrence in the garment width signature. Each event was associated with a geometry primitive identified during the primitive-learning stage, producing an ordered primitive sentence,

\[
S_g=(P_1,P_2,\ldots,P_n),
\]

where \(S_g\) denotes the primitive sequence for garment \(g\).

Directed transitions were defined between consecutive primitives within each garment. For a transition from primitive \(P_i\) to primitive \(P_j\), the corpus-level transition count was computed as

\[
N(P_i\rightarrow P_j),
\]

by aggregating all consecutive occurrences of the transition across the garment corpus.

The resulting transition probabilities were calculated conditionally on the source primitive:

\[
p(P_j\mid P_i)
=
\frac{N(P_i\rightarrow P_j)}
{\sum_k N(P_i\rightarrow P_k)}.
\]

This representation preserves the direction of the sequential relationship and describes the empirical tendency of one geometry primitive to be followed by another.

### 4.6.1 Permutation Null Model

To determine whether observed primitive transitions reflected non-random sequential organization, a within-garment permutation null model was constructed.

For each garment, the set of primitive identities was preserved while their original ordering was randomly permuted. This procedure therefore retained the primitive composition of each garment while removing its observed sequential arrangement.

A total of 2,000 within-garment permutations were generated. For each permutation, primitive transitions were recomputed and accumulated to form an empirical null distribution for each observed transition.

For an observed transition \(P_i\rightarrow P_j\), the Monte Carlo significance probability was estimated as

\[
p=
\frac{
N_{\mathrm{null}}\left(
C_{\mathrm{null}}\geq C_{\mathrm{obs}}
\right)+1
}{
N_{\mathrm{perm}}+1
},
\]

where \(C_{\mathrm{obs}}\) denotes the observed transition count, \(C_{\mathrm{null}}\) denotes the corresponding transition count under a randomized ordering, and \(N_{\mathrm{perm}}\) is the number of permutations.

The resulting transition probabilities were corrected for multiple comparisons using the Benjamini–Hochberg false discovery rate procedure at

\[
\alpha=0.05.
\]

Transitions that remained significant after FDR correction were retained as statistically enriched sequential relationships.

The resulting directed transition network therefore represents primitive-to-primitive relationships that occur more frequently than expected under the within-garment permutation null model. These statistically enriched sequential regularities provide evidence for a learned geometry-level organization of primitive sequences and form the basis for the subsequent visual-grammar representation.

### 4.6.2 Sequence-Level Structural Validation

The learned sequential organization was further examined at the garment level by comparing the local transition structure of individual garment sentences. Primitive-level bigram similarity provides a measure of shared local sequential organization between garments, while family-level bigram similarity evaluates whether such organization persists after abstraction from individual primitive identities.

This analysis complements the transition-level enrichment tests described above. Whereas the permutation analysis evaluates whether specific primitive or family transitions occur more frequently or less frequently than expected under randomized within-garment ordering, pairwise bigram similarity evaluates the extent to which complete garment representations share local transition structure.

Together, these analyses distinguish two related properties of the learned representation: statistically constrained sequential relationships at the corpus level and recurring local transition structure across individual garment representations.

The resulting evidence supports interpreting the learned transition network as a representation of statistically enriched sequential organization rather than as a deterministic rule system. In this work, the term Visual Grammar therefore refers to the recurring structural organization emerging from learned geometric relationships, rather than to a manually specified linguistic grammar.