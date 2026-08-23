We'll make Figure 3.1 the first actual evidence-to-representation figure, using one real garment sketch.

Figure 3.1 — locked concept

Panel A: Original garment sketch G
Panel B: Same sketch with extracted contour C
Panel C: Same contour with detected geometry events E
1
	​

,E
2
	​

,…,E
m
	​

 marked

No semantic labels. No primitive labels yet.

Caption:

**Figure 3.1. Geometry events extracted from a garment sketch.** 
The garment sketch \(G\) is represented by its contour \(C\), from which localized changes in geometric behavior are identified as geometry events \(E_i\). Event locations are shown on the original sketch without assigning predefined semantic garment-part labels.

Then immediately after the figure, we continue:

Across the sketch dataset, the resulting geometry events are treated as localized observations of geometric change and subsequently grouped according to geometric similarity.

That gives us the exact transition:

G→C→E→P

And then Figure 3.2 can show the emergence of the 12-primitives vocabulary from many event observations.

This is going to make the Methods section much easier to understand visually.

**Figure 3.3. Sequential organization of learned geometry primitives.**
(A) Representative garment sentences obtained by ordering the learned geometry primitives according to their occurrence along the garment width signature. Each sequence preserves the observed order of persistent geometry events. (B) Directed transition network constructed by aggregating consecutive primitive pairs across the garment corpus. Edge thickness represents transition frequency. The network represents observed sequential organization among learned geometric primitives and does not constitute a deterministic grammar or predefined design rule.

**Figure 3.2. Learned geometry primitive vocabulary.**
Normalized local geometry-event curves are grouped into 12 learned primitive clusters (P0–P11). Faint curves represent individual event instances assigned to each primitive, while the prominent curve represents the cluster-level prototype. Cluster membership is determined from geometric similarity rather than predefined garment-part or semantic labels. The number of event instances assigned to each primitive is shown in the panel title.

The resulting vocabulary contains 12 recurring geometric primitives. Each primitive represents a cluster of locally similar geometry-event curves and therefore provides a discrete representation of recurring geometric form. These learned primitives are subsequently assigned to their corresponding events within each garment, producing an ordered primitive sequence for the complete sketch.


**Figure 3.3. From geometry events to a symbolic garment sentence.**
A garment sketch is represented as an ordered sequence of persistent geometry events
(E₁, E₂, …, Eₘ). Each event is assigned to one of the learned geometry primitives,
producing a symbolic garment sentence. For the example shown, the resulting
representation is S_g = (P₁, P₈, P₁, P₆). Primitive identifiers denote learned
geometry patterns and do not correspond to predefined semantic garment-part labels.

For each garment, the ordered persistent geometry events were mapped to their
corresponding learned primitive identities, producing a symbolic garment sentence
\(S_g=(P_1,P_2,\ldots,P_n)\). This representation converts the continuous geometric
observations into an ordered sequence over the learned primitive vocabulary while
retaining the original event ordering. The resulting garment sentences form the
basis for subsequent analysis of primitive composition and sequential organization.

**Figure 3.3. From geometry events to a symbolic garment sentence.**
Persistent geometry events identified within an individual garment are assigned to learned geometry primitives according to their geometric similarity. The resulting primitive identities preserve the original event order and form an ordered symbolic garment sentence, \(S_g=(P_1,P_8,P_1,P_6)\). Repeated primitive identities may occur at multiple positions within the same garment sequence.


For each garment, the ordered primitive identities assigned to its persistent geometry events define a symbolic garment sentence,
\[
S_g=(P_1,P_2,\ldots,P_n).
\]
This representation preserves the sequential order of recurring geometric primitives while replacing the continuous event curves with discrete primitive identities. Garment sentences therefore provide the representation used for subsequent analysis of transition structure, predictive dependencies, and compositional organization.

## Figure 3.4 — Learned Sequential Organization of Geometry Primitives

Figure 3.4 illustrates the transition from individual garment-level symbolic representations to corpus-level sequential organization.

Panel (A) shows representative garment sentences obtained by mapping ordered persistent geometry events to the learned geometry primitive vocabulary. Each garment is therefore represented as an ordered sequence of primitive identities,

\[
S_g=(P_1,P_2,\ldots,P_n).
\]

Panel (B) shows the corresponding corpus-level directed transition structure obtained by aggregating consecutive primitive pairs across the garment corpus. Nodes represent the 12 learned geometry primitives, while directed edges represent observed transitions between consecutive primitives. Edge width reflects transition frequency. The network displays the strongest 25 of the 85 unique observed transitions.

The sequential representation was constructed from 333 garments containing 1,934 primitive events and 1,601 observed consecutive transitions. The resulting 85 unique transitions provide an empirical representation of recurring sequential organization among learned geometry primitives.

The transition structure is descriptive and corpus-derived. It does not represent a predefined grammar or deterministic production-rule system. Statistical validation of the observed sequential organization is examined separately using the within-garment permutation null model.

**Caption:**  
**Figure 3.4. Learned sequential organization of geometry primitives.** Representative garment sentences are shown in (A), illustrating the conversion of ordered geometry events into symbolic primitive sequences. In (B), consecutive primitive pairs are aggregated across the corpus to form a directed transition structure. Nodes denote learned geometry primitives and edge width reflects transition frequency. The network displays the strongest 25 of 85 observed transitions. The structure is corpus-derived and descriptive; statistical enrichment of sequential relationships is evaluated separately using a within-garment permutation null model.

**Figure 3.4. Learned sequential organization of geometry primitives.**
(A) Examples of garment-level primitive sentences obtained by assigning learned primitive identities to ordered geometry events. Each sentence preserves the spatial order of the corresponding garment events. (B) Corpus-level transition structure obtained by aggregating consecutive primitive pairs across 333 garments. The network displays the 25 strongest transitions among the 85 observed transition types; edge width indicates transition frequency. The network represents empirical sequential organization and does not constitute a predefined deterministic grammar.

Across the 333 garments, the 1,934 primitive events produced 1,601 consecutive primitive transitions, of which 85 distinct transition types were observed. The resulting transition structure captures recurring local sequential relationships among the learned geometry primitives. These empirical relationships provide the basis for testing whether primitive ordering differs from randomized within-garment arrangements and whether immediate sequential context contains predictive information about subsequent primitives.

## Figure 3.5 — Statistical Validation of Sequential Organization

The statistical enrichment of observed primitive transitions was evaluated using a within-garment permutation null model. For each garment, primitive identities were preserved while their ordering was randomly permuted, thereby retaining garment-level primitive composition while removing the observed sequential arrangement.

Figure 3.5 compares the observed frequency of each transition with its mean frequency under 2,000 within-garment permutations. The diagonal represents equality between observed and null expectation. Transitions above the diagonal occur more frequently than expected under randomized ordering. Points are distinguished according to whether the transition remained significant after Benjamini–Hochberg false-discovery-rate correction at \(\alpha=0.05\).

Of the 85 observed transition types, 37 remained significant after FDR correction. The result indicates that a subset of primitive-to-primitive transitions exhibits systematic sequential enrichment beyond that expected from the primitive composition of individual garments.

**Caption:**  
**Figure 3.5. Statistical validation of primitive sequential organization.** Observed transition frequencies are compared with their mean frequencies under 2,000 within-garment permutations. The diagonal denotes equality between observed and null expectation. Transitions surviving Benjamini–Hochberg FDR correction at \(\alpha=0.05\) are distinguished from non-significant transitions. Of 85 observed transition types, 37 remained FDR-significant, providing evidence for non-random sequential organization among learned geometry primitives.

## Figure 3.5 — Statistical Validation of Sequential Organization

The statistical enrichment of observed primitive transitions was evaluated using a within-garment permutation null model. For each garment, primitive identities were preserved while their ordering was randomly permuted, thereby retaining garment-level primitive composition while removing the observed sequential arrangement.

Figure 3.5 compares the observed frequency of each transition with its mean frequency under 2,000 within-garment permutations. The diagonal represents equality between observed and null expectation. Transitions above the diagonal occur more frequently than expected under randomized ordering. Transitions are distinguished according to whether they remained significant after Benjamini–Hochberg false-discovery-rate correction at α = 0.05.

Of the 85 observed transition types, 37 remained significant after FDR correction. The result indicates that a subset of primitive-to-primitive transitions exhibits systematic sequential enrichment beyond that expected from the primitive composition of individual garments.

**Figure 3.5. Statistical validation of primitive sequential organization.** Observed transition frequencies are compared with their mean frequencies under 2,000 within-garment permutations. The diagonal denotes equality between observed and null expectation. Transitions surviving Benjamini–Hochberg FDR correction at α = 0.05 are distinguished from non-significant transitions. Of 85 observed transition types, 37 remained FDR-significant, providing evidence for non-random sequential organization among learned geometry primitives.

### RQ017 — Learned Sequential Organization

Across 333 garments, 1,934 persistent geometry events were represented as learned primitive identities, producing 1,601 observed primitive-to-primitive transitions across 85 unique transition types.

The observed transition structure was evaluated against a within-garment permutation null model in which primitive composition was preserved while primitive ordering was randomized. Across 2,000 permutations, 37 of the 85 observed transition types remained significant after Benjamini–Hochberg FDR correction at α = 0.05.

These results provide evidence that sequential organization among the learned geometry primitives is not fully explained by the primitive composition of individual garments alone.

**Figure 3.5. Statistical validation of primitive sequential organization.**
Observed transition counts are compared with their mean expected counts under within-garment permutation across the 2,000 permutations. Each point represents one of the 85 observed primitive transition types. The dashed diagonal indicates equality between observed and permutation-null expected counts. Orange points denote transitions that remain significant after Benjamini–Hochberg false-discovery-rate correction (\(\alpha=0.05\)); blue points denote transitions that do not survive correction. In total, 37 of the 85 observed transition types remain significant after FDR correction.

The observed transition frequencies were compared with transition frequencies generated by randomly permuting primitive order within each garment. Of the 85 observed transition types, 37 remained significant after Benjamini–Hochberg false-discovery-rate correction at \(\alpha=0.05\). The significant transitions were predominantly located above the permutation-null expectation, indicating enrichment relative to randomized within-garment ordering.

These results provide statistical evidence that the observed sequential organization is not explained solely by the primitive composition of individual garments. Instead, specific primitive-to-primitive transitions occur at frequencies that differ systematically from those expected when the same primitive identities are randomly reordered within garments.

## Figure 3.5 — Statistical Enrichment of Primitive Transitions

To evaluate whether the observed sequential organization was consistent with non-random ordering, each observed primitive transition was compared with its expected frequency under a within-garment permutation null model. The permutation procedure preserved the primitive composition of each garment while randomizing the ordering of primitive identities. Enrichment was calculated as the difference between the observed transition count and the mean transition count under the permutation distribution.

The 85 observed transition types were ranked according to this enrichment. Thirty-seven transitions remained significant after Benjamini–Hochberg false-discovery-rate correction at α = 0.05. The positive enrichment of these transitions indicates that they occurred more frequently than expected under randomized within-garment ordering, whereas non-significant transitions showed weaker or negative deviations from the null expectation.

**Figure 3.5. Statistical enrichment of primitive transitions.** Observed transition counts are expressed relative to their mean frequency under 2,000 within-garment permutations. Transitions are ordered by observed-minus-null enrichment. FDR-significant transitions are distinguished from non-significant transitions. Of 85 observed transition types, 37 remained significant after Benjamini–Hochberg correction at α = 0.05.

**Figure 3.5. Statistical enrichment of primitive transitions.**
Observed transition counts are compared with their mean counts under within-garment permutation across 2,000 permutations. Bars show the difference between the observed transition count and its permutation-null mean for each of the 85 observed primitive transition types, ordered by this difference. Orange bars indicate transitions that remain significant after Benjamini–Hochberg false-discovery-rate correction (\(\alpha=0.05\)); blue bars indicate transitions that do not survive correction. The analysis tests upper-tail enrichment, and 37 of the 85 observed transition types remain significantly enriched after FDR correction.

Across the 85 observed primitive transition types, 37 remained significantly enriched after Benjamini–Hochberg false-discovery-rate correction at \(\alpha=0.05\). The observed transition counts showed substantial departures from their within-garment permutation-null expectations, with the FDR-significant transitions occurring on the enrichment side of the null distribution (Figure 3.5). These results indicate that specific primitive-to-primitive transitions occur more frequently than expected when the same primitive identities are randomly reordered within garments.

## Figure 3.6 — Garment-Level Sequential Similarity

To examine whether recurring local sequential structure persists under abstraction from individual geometry primitives to broader primitive families, all 55,278 pairs of garments were compared using cosine similarity between their bigram-frequency representations.

At the individual primitive level, the mean pairwise similarity was 0.096 and the median was 0.000. After replacing primitive identities with their learned family identities, the mean similarity increased to 0.430 and the median to 0.447. Family-level similarity exceeded primitive-level similarity for 65.48% of garment pairs, was equal for 32.18%, and was lower for 2.34%.

These results show that local sequential structure becomes substantially more shared across garments when represented at the broader primitive-family level. The result demonstrates preservation of recurring sequential organization under the learned abstraction, while the increase in similarity is interpreted as a property of the coarser representation rather than as independent evidence of human semantic equivalence.

**Figure 3.6. Garment-level sequential similarity under primitive-family abstraction.** Each hexagonal bin represents garment pairs according to their primitive-level and family-level bigram cosine similarities. The dashed diagonal denotes equal similarity at the two representation levels. Across 55,278 garment pairs, mean similarity increased from 0.096 at the primitive level to 0.430 at the family level, with 65.48% of pairs showing higher family-level similarity.

### RQ010 — Garment-Level Sequential Similarity

Across 333 garments, pairwise comparison of primitive-level bigram representations produced 55,278 garment pairs. Mean cosine similarity was 0.096 (median = 0.000). After abstraction to learned primitive families, mean similarity increased to 0.430 (median = 0.447).

Family-level similarity was greater than primitive-level similarity for 65.48% of garment pairs, equal for 32.18%, and lower for 2.34%.

The result indicates that recurring local sequential organization is substantially more shared across garments at the family level than at the individual primitive level. This supports the use of primitive families as a higher-level structural abstraction, without treating the increase in similarity itself as evidence of independently validated human semantic categories.

**Figure 3.6. Garment-level sequential similarity under primitive-family abstraction.**
Pairwise cosine similarity between garment bigram-frequency representations is shown before and after abstraction from individual geometry primitives to their corresponding primitive families. Each point represents a garment pair, with the primitive-level similarity on the x-axis and family-level similarity on the y-axis. The dashed diagonal indicates equal similarity at the two representation levels. Across 55,278 garment pairs, mean similarity increased from 0.096 at the primitive level to 0.430 at the family level, while the median increased from 0.000 to 0.447. Family-level similarity exceeded primitive-level similarity for 65.5% of garment pairs, was equal for 32.2%, and was lower for 2.3%.

The effect of primitive-family abstraction was examined by comparing garment-level bigram similarity before and after replacing individual primitive identities with their corresponding primitive families (Figure 3.6). Across 55,278 garment pairs, mean cosine similarity increased from 0.096 at the primitive level to 0.430 at the family level, while median similarity increased from 0.000 to 0.447. Family-level similarity exceeded primitive-level similarity for 65.5% of garment pairs, was equal for 32.2%, and was lower for 2.3%.

This result indicates that broader primitive-family representation captures recurring sequential structure that is less apparent when garments are compared using individual primitive identities. The finding is consistent with a hierarchical organization in which distinct geometric primitives can participate in shared higher-level sequential patterns. The analysis is descriptive and does not by itself establish that the predefined family categories correspond to human semantic categories.

# Figure 3.7 — Primitive Morphology

This figure examines the continuous geometric variation associated with
the learned discrete primitive vocabulary.

For each primitive, the learned representation contains:

- observed normalized geometric curves,
- a prototype curve,
- within-primitive variation,
- and the number of observations assigned to the primitive.

The analysis therefore separates recurring primitive identity from
variation in its geometric realization.

**Figure 3.7. Learned morphology of the geometry primitives.**
Normalized event curves are shown for each of the 12 learned geometry primitives. Individual curves represent observed event instances assigned to each primitive, while the central curve represents the corresponding prototype morphology and the shaded region summarizes the observed variation around the prototype. Curves are aligned by normalized event position and normalized geometric magnitude. The figure demonstrates that primitive identity is associated with recurring geometric form while allowing continuous variation among individual realizations.

The learned primitives exhibited distinct but non-identical geometric morphologies (Figure 3.7). Within each primitive, observed event curves were concentrated around a characteristic prototype while retaining substantial continuous variation across instances. The degree and pattern of variation differed among primitives: some primitives exhibited relatively narrow morphological distributions, whereas others showed broader deviations from their prototype.

This organization indicates that the learned primitive vocabulary captures recurring geometric forms without requiring each primitive to correspond to a single fixed curve. Primitive identity therefore provides a discrete structural representation while the observed within-primitive variation preserves continuous morphological information.

# Figure 3.8 — Context-Conditioned Primitive Morphology

This figure examines whether the geometric realization of a primitive
varies according to its immediately preceding primitive.

For the current primitive P0, context-specific prototypes are estimated
for preceding primitives with at least 10 observations.

Each prototype represents the mean normalized geometric realization
observed for a specific primitive transition context.

The analysis is exploratory: context-conditioned morphology is visualized
without interpreting observed differences as evidence of a causal effect
of sequential context.

**Figure 3.8. Context-conditioned morphology of primitive \(P_0\).**
Observed realizations of \(P_0\) are shown separately according to their immediately preceding primitive. Each panel corresponds to one predecessor context, with the number of observations indicated above the panel. Individual curves represent observed realizations, the central curve represents the context-specific prototype, and the shaded region summarizes within-context morphological variation. Curves are aligned by normalized event position and normalized geometric magnitude. Differences among context-conditioned prototypes indicate variation in the geometric realization of \(P_0\) across sequential contexts.


The geometric realization of a primitive was further examined as a function of its immediate sequential context (Figure 3.8). For \(P_0\), context-conditioned prototypes were estimated separately for six observed predecessor contexts: \(P_4\rightarrow P_0\), \(P_5\rightarrow P_0\), \(P_6\rightarrow P_0\), \(P_8\rightarrow P_0\), \(P_9\rightarrow P_0\), and \(P_{10}\rightarrow P_0\). The resulting prototype curves show broadly similar overall geometric behavior but differ in their local morphology and in the extent of within-context variation.

These differences indicate that the geometric realization of a primitive can vary across sequential contexts. The result provides evidence for an association between sequential context and primitive morphology, while not establishing that context causally determines geometric form.

# Figure 3.9 — Context Sensitivity of Primitive Morphology

For each geometry primitive, context-specific prototypes are compared
using their pairwise Euclidean distances.

The resulting context-sensitivity score measures the degree to which
the geometric realization of a primitive varies across its observed
sequential contexts.

Lower values indicate greater morphological stability across contexts,
whereas higher values indicate greater variation among context-specific
realizations.

This analysis is descriptive of the learned representation and does not
by itself establish a causal effect of grammatical context on primitive
geometry.

**Figure 3.9. Context sensitivity of primitive morphology.**
Mean pairwise context distance is shown for each of the 12 learned geometry primitives. Context distance quantifies the average morphological difference between context-conditioned realizations of a primitive across its observed sequential contexts. Larger values indicate greater variation in morphological realization across contexts, whereas smaller values indicate greater morphological consistency across contexts. Primitives are ordered by decreasing mean context distance.

Context sensitivity varied substantially across the learned primitives (Figure 3.9). Mean pairwise context distance ranged from relatively high values for \(P_6\) and \(P_7\) to substantially lower values for \(P_9\), indicating that the extent to which morphological realization varied across sequential contexts differed among primitives.

This variation suggests that sequential context is associated with morphological differences to different degrees across the primitive vocabulary. Some primitives exhibit relatively stable geometric realization across contexts, whereas others show greater context-dependent variation. The analysis therefore supports heterogeneous context sensitivity within the learned primitive system rather than a uniform contextual effect across all primitives.

# Figure 3.10 — Semantic Representation

The Semantic Representation \(\Sigma\) integrates four complementary
learned representations:

- Geometric Primitive Vocabulary \(\mathcal{V}\)
- Visual Grammar \(\mathcal{G}\)
- Primitive Morphology \(\mathcal{M}\)
- Context-Dependent Primitive Morphology \(\mathcal{M}^{(\Gamma)}\)

The resulting representation is defined as

\[
\Sigma =
\Phi_s
\left(
\mathcal{V},
\mathcal{G},
\mathcal{M},
\mathcal{M}^{(\Gamma)}
\right).
\]

The Semantic Representation is an interpretive computational layer
derived from measurable geometric, structural, morphological, and
contextual regularities. It does not introduce independently validated
semantic ground truth or manually assigned garment-part labels.

**Figure 3.10. Semantic integration of the learned structural representations.**
The semantic representation \(\Sigma\) is constructed by integrating the learned primitive vocabulary \(\mathcal{V}\), sequential organization represented by the Visual Grammar \(\mathcal{G}\), primitive morphology \(\mathcal{M}\), and context-dependent morphology \(\mathcal{M}^{(\Gamma)}\). The integration operator \(\Phi_S\) provides a computational mechanism for combining geometric, structural, morphological, and contextual evidence into a higher-order representation. The resulting semantic representation remains traceable to the underlying geometric evidence and is interpreted as a computational semantic organization rather than independently validated semantic ground truth.

The higher-order semantic representation integrates the structural components established in the preceding analyses. Specifically, the primitive vocabulary, sequential organization, primitive morphology, and context-dependent morphology provide complementary evidence about the organization and realization of recurring geometric structures (Figure 3.10). These representations are integrated through \(\Phi_S\) to obtain the semantic representation \(\Sigma\).

The resulting semantic representation is therefore derived from the learned geometric structure rather than introduced as an independently specified semantic ontology. Because the present study does not include independent human semantic annotations or external semantic ground truth, \(\Sigma\) is interpreted as a computational representation of higher-order organization rather than as a validated measurement of human semantic meaning.


# Figure 3.11 — Knowledge Graph Representation

The Knowledge Graph Representation organizes the semantic entities and
relationships contained within the Semantic Representation into an
explicit relational structure.

The Knowledge Graph is defined as

\[
\mathcal{K} =
(\mathcal{V}_K,\mathcal{E}_K)
\]

and constructed from the Semantic Representation through

\[
\mathcal{K} =
\Psi_K(\Sigma).
\]

Here, \(\mathcal{V}_K\) denotes learned semantic entities and
\(\mathcal{E}_K\) denotes the relationships connecting those entities.

The Knowledge Graph reorganizes relationships already represented within
\(\Sigma\); it does not introduce an independent source of semantic
evidence or an externally curated ontology.

**Figure 3.11. Knowledge graph representation of the learned structural relationships.**
The semantic representation \(\Sigma\) is transformed through the graph-construction operator \(\Psi_{\mathcal{K}}\) into an explicit relational representation \(\mathcal{K}=(\mathcal{V}_{\mathcal{K}},\mathcal{E}_{\mathcal{K}})\). Nodes represent learned structural entities, while directed edges encode relationships such as geometric relatedness, morphology, sequential organization, and contextual association. The graph makes relationships among the learned representations explicit while remaining a descriptive relational representation rather than an externally curated semantic ontology.

The integrated semantic representation can be reorganized into an explicit relational structure using a knowledge graph representation (Figure 3.11). The graph represents learned entities as nodes and their observed or derived relationships as directed edges, allowing geometric, morphological, sequential, and contextual relationships to be examined within a common relational structure.

The resulting knowledge graph does not introduce an independent semantic ontology. Instead, it provides an explicit representation of relationships already established within the learned computational framework. Consequently, graph edges should be interpreted as descriptive relationships within the learned representation rather than as externally validated semantic relations.