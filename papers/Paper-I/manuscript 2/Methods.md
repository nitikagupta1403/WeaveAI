## RQ010. Garment-Level Sequential Similarity

### Methods

To evaluate whether the learned symbolic representation captures recurring sequential structure across garments, garment sentences were compared at two levels of abstraction: the individual geometry-primitive level and the broader primitive-family level.

For each garment, the ordered sequence of learned primitive identifiers was represented as a garment sentence,

\[
S_g=(P_1,P_2,\ldots,P_n),
\]

where \(P_i\) denotes the geometry primitive assigned to the corresponding persistent geometry event.

From each garment sentence, an ordered bigram representation was constructed by recording every pair of consecutive primitives,

\[
B_g =
\{(P_i,P_{i+1})\}_{i=1}^{n-1}.
\]

Each garment was subsequently represented as a bigram-frequency vector over the corpus-level transition vocabulary. Pairwise cosine similarity was computed between these vectors to quantify the degree of shared local sequential structure between garments.

Cosine similarity was defined as

\[
\operatorname{sim}(g_a,g_b)
=
\frac{
\mathbf{b}_{g_a}\cdot\mathbf{b}_{g_b}
}{
\|\mathbf{b}_{g_a}\|
\|\mathbf{b}_{g_b}\|
},
\]

where \(\mathbf{b}_{g}\) denotes the bigram-frequency representation of garment \(g\).

The same procedure was repeated after replacing individual primitive identities with their corresponding primitive-family identities. Each garment was therefore represented by a family-level bigram vector,

\[
B_g^{F}
=
\{(F_i,F_{i+1})\}_{i=1}^{n-1},
\]

where \(F_i\) denotes the primitive family associated with primitive \(P_i\).

Pairwise similarity was then compared between the primitive-level and family-level representations. This comparison tests whether abstraction from individual geometric primitives to broader primitive families preserves or increases recurring local sequential structure across garments.

All pairwise comparisons were performed over the complete set of garment pairs.


