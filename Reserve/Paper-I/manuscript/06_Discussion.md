# 4. Discussion

## 4.1 A Learned Geometric Vocabulary

The central finding of this study is that recurring geometric structure in fashion sketches can be represented as a compact learned vocabulary of geometric primitives. From 1,934 persistent geometry events extracted across 333 garment sketches, the representation identified 12 recurring primitive classes. These primitives were not simply arbitrary frequency-based categories: curves assigned to the same learned primitive exhibited substantially greater morphological similarity than curves assigned to different primitives, with a within-to-between similarity ratio of approximately 5.74 and a permutation-based empirical \(p=0.00020\).

This result indicates that the learned vocabulary captures recurring forms of geometric organization within the sketch corpus. At the same time, the learned primitives retain continuous morphological variation rather than representing fixed shapes. The primitive therefore functions as a discrete structural identity associated with a distribution of geometric realizations.

This distinction between discrete identity and continuous realization is important for representing fashion sketches. A purely geometric representation preserves continuous variation but does not explicitly identify recurring structural units, whereas a purely symbolic representation would discard meaningful variation among instances. The learned primitive vocabulary provides an intermediate representation in which recurring geometric organization can be represented symbolically while variation within each primitive remains observable.

## 4.2 From Primitive Identity to Visual Grammar

The learned primitives also exhibited non-random sequential organization. At the primitive level, specific transitions were statistically enriched relative to a within-garment permutation null, with 37 of 85 observed primitive transition types surviving false-discovery-rate correction. At the broader family level, sequential organization also persisted: four of nine family transitions were significantly enriched, while complementary lower-tail analysis identified significantly depleted transitions.

These findings indicate that the observed ordering of primitive identities cannot be adequately described as arbitrary permutations of the same primitive composition. Instead, primitive identities participate in recurring sequential relationships within garment sketches.

The predictive analysis provides an independent test of this sequential organization. A first-order context-conditioned predictor substantially improved next-primitive prediction relative to a global-frequency baseline, achieving 30.73% accuracy compared with 15.30%. Importantly, this predictive advantage generalized to garments excluded from estimation of the transition probabilities, where the context-conditioned predictor achieved 30.34% accuracy compared with 8.05% for the training-set majority baseline.

The convergence of enrichment and predictive evidence is important. Transition enrichment demonstrates that particular sequential relationships occur more frequently than expected under randomized ordering, while predictive evaluation demonstrates that preceding primitive context contains information useful for predicting subsequent primitives. Together, these results support interpreting the learned sequential organization as a grammar-like property of the geometric representation.

The present findings do not establish a complete generative grammar of fashion design or a linguistic grammar in the human sense. Rather, the Visual Grammar proposed here is a corpus-derived statistical representation of recurring organization among geometry-derived primitive identities. Transition probabilities describe observed sequential dependencies, while the primitive vocabulary provides the representational units over which those dependencies are defined.

## 4.3 Structural Roles and Compositional Organization

The primitive representation also revealed systematic structural differences in where and how primitives occur within garment sequences. Primitive identity was strongly associated with normalized sequence position, with a Kruskal–Wallis statistic of \(H=637.09\) and an epsilon-squared effect size of \(\epsilon^2=0.326\). Individual primitives exhibited characteristic positional profiles, including strong early or late specialization for some primitives and broader distributions for others.

Primitive identities also differed in their local sequential neighborhoods. Some primitives exhibited relatively concentrated predecessor or successor relationships, whereas others occurred across a broader range of contexts. These positional and contextual properties provide each primitive with a measurable structural signature extending beyond its geometric morphology.

The resulting primitive knowledge representation integrates these complementary dimensions into an explicit structural profile. Each primitive can therefore be described in terms of its morphological coherence, positional characteristics, predefined family assignment, and local sequential neighborhood.

This representation provides a bridge between isolated geometric primitives and complete garment structures. Across the 333 garments, all 12 learned primitives were represented, while individual garments typically used only a subset of the vocabulary. The mean number of unique primitives per garment was 4.303, with a median of 4. Thus, complete garment sketches can be represented as ordered compositions of a relatively small subset of recurring geometric units drawn from a shared corpus-level vocabulary.

This compositional interpretation does not imply that individual primitives correspond directly to predefined garment parts or independently validated human semantic concepts. Rather, compositionality refers to the computational representation of complete garment structure as ordered combinations of learned geometric primitives.

## 4.4 Relationship to Predefined Semantic Families

The predefined three-family taxonomy showed only modest alignment with the integrated structural organization of the learned primitives. Within-family structural distance was 3.7399 compared with 4.1138 between families, corresponding to a separation ratio of approximately 1.10. However, this difference did not reach statistical significance under the permutation test (\(p=0.095\)).

This result is informative because it indicates that the learned structural organization is not simply a reproduction of the predefined family assignments. The learned primitives exhibit strong morphological and structural organization, but the multidimensional organization captured by morphology, position, and sequential neighborhood is not strongly explained by the predefined family taxonomy.

The result therefore supports distinguishing between learned structural organization and externally specified semantic grouping. The predefined families remain useful as a higher-level descriptive taxonomy, but the present evidence does not support treating them as the primary determinant of the learned structural representation.

## 4.5 Boundaries of Context-Dependent Morphological Interpretation

The relationship between sequential context and continuous morphology was also examined directly. Although curves sharing an immediate preceding-primitive context showed a small positive morphological effect, the observed difference did not reach statistical significance (\(p=0.0856\)).

This result places an important boundary on the interpretation of the learned representation. The evidence strongly supports sequential organization among primitive identities, but it does not establish that the geometric realization of a primitive systematically changes as a function of its immediate predecessor.

Accordingly, context-dependent morphology should be regarded as an open question rather than as an established component of the present Visual Grammar. The current evidence supports a distinction between sequential organization of primitive identities and variation in their geometric realization, without establishing a statistically validated causal or deterministic relationship between the two.

## 4.6 Contribution to a Computational Representation of Sketch Structure

The scientific contribution of the framework lies in connecting these representations through a common geometry-derived vocabulary. The individual computational procedures used in the pipeline are established analytical operations; the contribution is their integration into a traceable representation spanning persistent geometric events, learned primitive identity, sequential organization, morphological variation, structural profiles, and compositional garment sequences.

The direction of construction is central to this representation. Rather than beginning with predefined semantic categories and subsequently locating those categories within the visual data, the framework begins with measurable geometric structure and progressively constructs symbolic and relational representations. Higher-order interpretation is therefore derived from relationships established within the visual representation rather than imposed at the outset.

This provides an intermediate computational representation between continuous sketch geometry and higher-order semantic analysis. The representation preserves traceability: higher-level primitive, sequential, and structural descriptions can be related back to the geometry from which they were derived.

## 4.7 Semantic Interpretation and Limitations

The higher-order semantic interpretation proposed by the framework should be distinguished from independently validated semantic ground truth. The present study establishes computational relationships among geometric primitives, their morphology, their positions, and their sequential contexts, but it does not include human annotations that independently validate semantic meanings assigned to those structures.

Consequently, semantic roles should be interpreted as computational descriptions of learned structural organization rather than as direct measurements of human semantic concepts or design cognition. Similarly, the resulting knowledge representation and relational structures should not be interpreted as a fixed ontology of fashion design.

The Visual Grammar itself is also corpus-derived and representation-dependent. Its organization reflects the geometric regularities captured by the learned vocabulary and the particular sketch corpus used in this study. Whether the same primitive vocabulary, transition structure, positional organization, or compositional patterns persist across independent datasets, designers, drawing conventions, or garment categories remains to be established.

These limitations define the appropriate scope of the present contribution. The study demonstrates that recurring geometric structure in fashion sketches can be learned, represented symbolically, and organized into statistically structured sequential and compositional representations. It does not establish that the resulting representation constitutes a complete or universal language of fashion design.

## 4.8 Overall Interpretation

Taken together, the findings support a computational account in which fashion sketches contain recurring geometric structures that can be organized into a learned primitive vocabulary. These primitives exhibit strong morphological coherence, characteristic positional and sequential organization, predictive dependencies, and compositional use across complete garment sequences.

The statistically enriched transition structure and its predictive generalization provide evidence for grammar-like organization at the level of garment geometry. The structural profiles further show that primitive identity is associated with where primitives occur and with the local sequential neighborhoods in which they participate.

The resulting framework therefore provides a geometry-grounded intermediate representation between continuous sketch geometry and higher-order symbolic analysis. Its central contribution is not the assertion of a complete fashion language, but the demonstration that recurring geometric organization in fashion sketches can be computationally learned, represented, and analyzed as a structured system of reusable components and their relationships.