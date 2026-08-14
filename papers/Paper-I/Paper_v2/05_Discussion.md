## 5.1 Principal Findings

This study provides evidence that garment sketches contain recurring geometric
and sequential structure that can be learned as a reusable symbolic
representation without requiring predefined semantic labels at the primitive
learning stage.

Three findings are central.

First, the learned primitive vocabulary exhibits internally coherent
geometric organization. Curves assigned to the same primitive are
substantially more similar than curves assigned to different primitives, and
this separation remains significant under permutation testing. This indicates
that the learned vocabulary captures recurring regions of geometric variation
rather than arbitrary partitions of the observed sketch curves.

Second, the learned primitives are organized sequentially. Primitive identity
is associated with characteristic positions and local sequential contexts, and
primitive transitions exhibit structure that cannot be explained solely by the
marginal frequency of the primitives. In particular, immediate predecessor
context improves prediction of the subsequent primitive, with predictive
advantage retained on garments excluded from transition estimation. This
provides evidence that the representation captures sequential constraints
between geometric units rather than representing garments as unordered
collections of primitives.

Third, these properties are not restricted to the primary corpus. When the
frozen representation was transferred to the independent CLO-SK benchmark,
primitive usage retained measurable identity-associated, category-associated,
and geometry-associated structure. At the same time, raw geometric
representations substantially outperformed the symbolic representations for
direct garment-identity retrieval. The two observations together indicate
that symbolic abstraction preserves selected structural regularities while
discarding some of the fine-grained information available in the original
geometry.

The resulting picture is therefore not one of a symbolic representation that
replaces the sketch itself. Rather, the learned primitives provide an
intermediate representational level between continuous sketch geometry and
higher-order structural interpretation. They expose recurring geometric
units, their characteristic positions, and their sequential relationships
while deliberately abstracting away part of the original visual detail.

This distinction is central to the interpretation of the study. The evidence
supports a structured and reusable computational vocabulary of garment
geometry, together with measurable sequential organization. It does not by
itself establish that the learned primitives correspond to human-defined
garment concepts or that the resulting system constitutes a complete semantic
language of fashion design.

## 5.2 Geometry as the Basis of Learned Structural Units

The morphological coherence of the learned primitives provides the first
evidence that the symbolic vocabulary reflects recurring organization in
garment-sketch geometry. Curves assigned to the same primitive were
substantially more similar than curves assigned to different primitives, and
the observed separation was highly unlikely under random reassignment of
primitive labels. The important point is therefore not simply that the
clustering produced distinct groups, but that the resulting groups correspond
to reproducible regions of geometric variation within the sketch corpus.

This provides a geometry-first basis for the symbolic representation. Rather
than beginning with predefined garment parts or manually specified semantic
categories, the representation first identifies recurring geometric structure
and subsequently describes how those structures are organized within complete
garment sketches.

The distinction between learned primitives and predefined semantic categories
is important. A geometrically coherent primitive need not correspond to a
single human-interpretable garment component. Its identity is established here
by the consistency of its geometric representation, not by an independently
assigned semantic label. Consequently, the morphological coherence analysis
supports the existence of recurring computationally identifiable geometric
units, while leaving their human semantic interpretation open.

The comparison with the predefined family organization further reinforces
this distinction. The learned primitive vocabulary exhibits substantially
stronger morphological differentiation than the broader family grouping.
This suggests that the primitive level captures finer-grained geometric
variation that is not fully represented by the predefined family taxonomy.

The resulting representation can therefore be viewed as an intermediate
abstraction layer. At the lowest level, the sketch consists of continuous
geometric curves. The learned primitives provide a discrete representation
of recurring geometric configurations, while the broader families provide a
higher-level grouping of those primitives. This hierarchy allows the same
sketch geometry to be examined at multiple levels of abstraction without
requiring the learned primitives themselves to be assigned human semantic
names.

This finding is foundational for the subsequent analyses. If the primitive
assignments were not morphologically coherent, sequence-level regularities
could be difficult to interpret as properties of meaningful structural units.
The observed morphological separation therefore provides the geometric basis
on which the positional, sequential, and compositional analyses can be
interpreted.

## 5.3 What a Primitive Represents

The results indicate that the learned primitives are characterized by more than
their local geometric morphology. Primitive identity is also associated with
where a primitive tends to occur within a garment sequence and with the local
sequential contexts in which it appears. This suggests that a primitive is
better understood as a structural unit whose identity is expressed jointly
through its geometry and its relationships within the complete sketch.

The positional analysis provides evidence for this interpretation. Primitive
identities were strongly associated with normalized sequence position, and
individual primitives exhibited distinct distributions across early, middle,
and late regions of garment sequences. Some primitives were concentrated
toward particular regions of the sequence, whereas others were distributed
more broadly. Thus, the same primitive vocabulary is not used uniformly
throughout the structural organization of a garment.

Primitive identity was also associated with characteristic local sequential
neighborhoods. The observed distributions of predecessor and successor
primitives varied across the vocabulary: some primitives occurred in relatively
concentrated contexts, whereas others appeared with a broader range of
neighbors. These differences suggest that primitive identity incorporates a
relational component that cannot be described adequately by morphology alone.

The combined evidence motivates a multidimensional description of primitive
identity:

\[
\text{Primitive Structural Role}
=
\text{Morphology}
+
\text{Position}
+
\text{Local Sequential Context}.
\]

This formulation is useful because it distinguishes two related but different
properties. Morphological coherence describes what a primitive looks like in
the geometry-derived representation, whereas positional and contextual
profiles describe how that primitive participates in the organization of a
complete garment sequence.

The resulting structural profiles therefore provide a more informative
description of the learned vocabulary than morphology alone. A primitive can
be characterized by its recurring geometric form, its preferred region within
a garment sequence, and the primitive types with which it most frequently
interacts.

These observations also provide a bridge between the geometric and sequential
levels of the representation. The primitive vocabulary begins with recurring
geometric configurations, but those configurations acquire additional
structural characterization through their use within complete garment
sequences. The representation therefore moves from isolated geometric units
toward relational structural units.

Importantly, this interpretation remains computational rather than semantic.
A characteristic position or sequential neighborhood does not establish that
a primitive corresponds to a specific human-defined garment concept. Rather,
it demonstrates that primitive identity is associated with measurable
structural roles within the corpus.

This distinction is important for the interpretation of the subsequent
sequential analyses. If primitive identity is expressed jointly through
geometry and structural context, then dependencies between neighboring
primitives become a natural property to investigate. The next question is
therefore whether these sequential relationships are merely descriptive or
whether they provide measurable predictive structure.

## 5.4 Sequential Organization and Visual Grammar

The sequential analyses provide evidence that garment sketches are not adequately
described as unordered collections of geometric primitives. The ordering of
primitives contains measurable regularities, and these regularities persist
beyond the marginal frequencies of individual primitives.

At the broader family level, observed transition frequencies differed from
those expected when the family composition of each garment was preserved but
its ordering was randomly permuted. Several family transitions were enriched
relative to this null model, while others were depleted. This demonstrates
that the observed sequential organization cannot be explained solely by the
presence and frequency of the constituent families. The order in which those
families occur contributes additional structure.

The predictive analysis provides a complementary and more direct test of this
sequential organization. A predictor conditioned on the immediately preceding
primitive substantially outperformed a global-majority baseline when predicting
the next primitive. The predictive advantage was also retained when evaluated
on garments that had not been used to estimate the transition probabilities.

This generalization is important for interpretation. The observed sequential
regularity is not adequately characterized as a collection of memorized
training-garment sequences. Instead, immediate primitive context contains
information that can be reused when processing previously unseen garments
within the evaluated corpus.

The modest additional benefit obtained from extending the context to two
preceding primitives further suggests that a substantial portion of the
measurable sequential dependency is captured by local context. This does not
imply that longer-range dependencies are absent; rather, it indicates that
immediate neighborhood information already provides a substantial component of
the predictive structure detected in the present analysis.

These findings support describing the learned representation as
**grammar-like** in a computational sense. Primitive sequences exhibit
context-dependent regularities in which the occurrence of one structural unit
provides information about the likely occurrence of another. The family-level
permutation analysis additionally shows that these regularities involve
ordering rather than merely composition.

However, the present evidence does not establish a complete generative grammar
of garment sketches. A formal grammar would require a more comprehensive
account of allowable structures, longer-range dependencies, generation,
constraints, and potentially exceptions. The present experiments instead
demonstrate predictive sequential organization within the observed primitive
vocabulary.

The distinction is therefore important:

\[
\text{Sequential regularity}
\;\neq\;
\text{Complete grammar}.
\]

The appropriate interpretation is that the learned primitive representation
contains **grammar-like sequential structure** that can be measured and
predicted computationally.

This result also strengthens the interpretation of the primitive vocabulary
as compositional. If primitives were merely independent geometric labels,
their ordering would not be expected to provide substantial predictive
information. The observed context dependence instead suggests that the
learned units participate in structured combinations within complete garment
descriptions.

The sequential findings therefore provide a bridge between the learned
geometric vocabulary and the broader concept of a symbolic representation.
The primitives provide the reusable units, while their context-dependent
ordering provides a mechanism through which those units are composed into
structured garment sequences.

## 5.5 Compositionality and Reusable Structural Vocabulary

The sequential organization of the learned primitives suggests that complete
garment sketches can be represented as compositions of a shared vocabulary of
geometric units. Across the primary corpus, all 12 learned primitives were
represented, while individual garments typically instantiated only a subset of
this vocabulary. The mean number of unique primitives per garment was
approximately 4.3, indicating that individual garment descriptions generally
require only a fraction of the available primitive vocabulary.

This relationship between a shared vocabulary and partial instantiation is
consistent with a compositional representation. Rather than assigning a unique
symbolic description to every garment, the representation permits different
garments to reuse overlapping subsets of primitives and to arrange those
primitives in different sequential configurations.

The pairwise transition analysis provides additional evidence for this
interpretation. At the individual primitive level, exact bigram overlap was
sparse across the garment corpus. However, similarity increased substantially
when individual primitives were represented through their broader geometric
families. This indicates that garments can differ in their precise
primitive-level transitions while retaining more general transition structure
at a higher level of abstraction.

The independent CLO-SK benchmark provides complementary evidence for this
reuse. Across 2,299 benchmark images, the representation contained substantial
sequence diversity while also exhibiting repeated primitive and family
sequences. Importantly, repeated symbolic patterns were observed across
multiple garment identities rather than functioning as identity-specific
codes.

This combination of diversity and reuse is an important property of a
compositional vocabulary. If every garment received a unique symbolic
sequence, the representation would provide little evidence for reusable
structural units. Conversely, if most garments collapsed to the same small
number of sequences, the representation would provide little information for
distinguishing structural variation. The observed representation occupies an
intermediate regime: recurring patterns are reused, but substantial sequence
variation remains.

The identity-level analyses provide a further perspective on this balance.
Primitive sequences were not invariant within individual garment identities,
and no identity was represented by a single primitive or family sequence
across all of its sketches. Nevertheless, primitive-set similarity was higher
within garment identities than between identities. This suggests that
identity-associated structural information is present without requiring an
identity to possess a single fixed symbolic description.

The representation can therefore be understood as compositional rather than
deterministic. A garment identity is not mapped to one immutable symbolic
sentence; instead, multiple sketches can express overlapping structural
content through different primitive sequences.

This distinction is particularly relevant for fashion sketches, where the
same underlying garment design may be expressed differently by different
sketchers. A useful symbolic representation should therefore permit
variation while retaining reusable structural information. The observed
combination of within-identity similarity, cross-identity reuse, and sequence
diversity is consistent with such a representation.

The compositional interpretation should nevertheless remain computational.
The present results demonstrate reuse and structured combination of learned
geometric primitives, but they do not establish that these combinations
correspond to a human-defined grammar of garment construction or design.

The contribution at this stage is therefore a **reusable geometric vocabulary
and its observed compositional organization**, providing an intermediate
representation on which higher-level semantic interpretation can subsequently
be investigated.

## 5.6 What the Independent CLO-SK Benchmark Establishes

The independent CLO-SK evaluation provides an important test of whether the
properties observed in the primary corpus remain measurable when the frozen
representation is transferred to a separate sketch population. The benchmark
was not used to redefine the primitive vocabulary; instead, the previously
established representation was applied to 2,299 images spanning 230 garment
identities, 23 garment categories, and 12 sketchers. This separation between
representation construction and external evaluation provides evidence about
the transferability of the observed structural organization.

The benchmark results reveal a consistent distinction between geometric
fidelity and symbolic structural information. Raw geometry substantially
outperformed the symbolic representations for direct garment-identity
retrieval, both in unrestricted evaluation and under the stricter
cross-sketcher condition. This demonstrates that the symbolic representation
does not preserve all of the fine-grained information contained in the
original sketch geometry.

Importantly, however, lower retrieval performance does not correspond to an
absence of measurable structure. The frozen symbolic representation retained
several forms of organization on the independent benchmark. Primitive-set
similarity was higher among sketches belonging to the same garment identity
than among sketches from different identities. Primitive usage also contained
category-associated information above the uniform baseline, and primitive
usage showed systematic associations with independently measured geometric
properties.

These findings provide convergent evidence that the symbolic representation
retains selected structural information after transfer to an external
population. The evidence is particularly informative because the different
analyses probe different properties of the representation. Identity-level
similarity tests whether symbolic content is associated with garment identity;
category analysis tests whether primitive usage contains broader garment
class information; and geometry-association analysis tests whether primitive
usage remains systematically related to independently measured properties of
the sketches.

The benchmark therefore supports a distinction between **information
preservation** and **structural organization**. The symbolic representation
does not preserve enough image-level information to compete with raw geometry
for direct retrieval, but it does preserve measurable regularities that are
not reducible to complete visual identity matching.

This distinction also helps interpret the cross-sketcher results. Sketches
produced by different sketchers can differ substantially in their geometric
expression, making direct image-level matching more difficult. The fact that
the frozen representation continues to exhibit identity-associated and
geometry-associated structure under this setting suggests that some recurring
properties survive variation in sketch production. Nevertheless, the present
benchmark does not establish invariance to all sketching styles or drawing
conventions.

The benchmark also demonstrates that symbolic patterns are neither unique
identifiers nor completely collapsed categories. Primitive and family
sequences recur across multiple garment identities, while substantial
sequence diversity remains across the benchmark. Within-identity primitive
sets are more similar on average than between-identity sets, but the
separation is modest and no garment identity is represented by a single
invariant sequence.

Taken together, these results support interpreting the frozen vocabulary as a
transferable **structural representation** rather than as a complete visual
encoding. Its value lies in retaining selected recurring properties of
garment geometry while abstracting away some of the fine-grained variation
that is retained by the continuous geometric representation.

This external evaluation therefore strengthens the central claim of the
study in a specific way: the learned symbolic organization is not restricted
to the exact observations from which it was constructed. At the same time,
the benchmark defines the limits of that claim by showing that transfer of
structural information does not imply preservation of complete visual
information or universal sketch invariance.

## 5.7 Abstraction Versus Visual Fidelity

The retrieval results reveal an important property of the learned symbolic
representation: abstraction and preservation of fine-grained visual
information are not equivalent objectives.

Across the CLO-SK benchmark, raw geometric signatures substantially
outperformed the symbolic representations for direct garment-identity
retrieval. This difference persisted under cross-sketcher evaluation, where
same-sketcher candidates were excluded. The result demonstrates that the
symbolic representation discards information that remains available in the
continuous geometric description and is useful for distinguishing individual
sketches of the same garment.

This limitation is important because it defines what the learned vocabulary
should and should not be expected to represent. A symbolic sequence records
the occurrence and ordering of learned primitives, but it does not retain the
complete geometry of each primitive instance. Fine-grained differences in
shape, proportion, curvature, drawing extent, and other image-level properties
can therefore be lost when continuous geometry is mapped to discrete
primitive identities.

The retrieval result consequently argues against interpreting the symbolic
representation as a compressed replacement for the original sketch. Instead,
the representation should be understood as a change in representational
level. Raw geometry provides a detailed description of the individual visual
instance, whereas the symbolic representation emphasizes recurring structural
units and their relationships.

This distinction also explains why the weaker retrieval performance is not
inconsistent with the other benchmark findings. Identity retrieval asks
whether the representation preserves enough information to distinguish
individual garment instances. The identity-associated, category-associated,
and geometry-association analyses ask a different question: whether the
representation retains systematic structural regularities across a population
of sketches.

A representation can therefore lose information relevant to exact visual
matching while retaining information relevant to structural organization.
The benchmark results provide empirical evidence for precisely this
distinction.

The appropriate interpretation is thus not that symbolic representation is
inferior to geometry in general, but that the two representations preserve
different types of information. Raw geometry is better suited to tasks that
depend on fine-grained visual fidelity, whereas the symbolic representation
provides an explicit discrete description of recurring structural patterns.

This distinction is particularly relevant to the broader objective of
learning a structural vocabulary from fashion sketches. If the purpose of
the representation is to expose reusable geometric units and their
relationships, complete preservation of image-level information is neither
necessary nor expected. Conversely, applications requiring precise visual
identity or reconstruction would require access to the underlying geometric
representation or an additional mechanism capable of retaining the discarded
detail.

The benchmark therefore establishes an important boundary condition for the
proposed representation: **symbolic abstraction captures selected structural
regularities at the cost of fine-grained geometric fidelity.** Rather than
being a failure of the representation, this trade-off defines the level at
which the learned vocabulary should be interpreted and used.

## 5.8 Morphological Structure Versus Human Semantic Interpretation

An important distinction in interpreting the learned vocabulary is the
difference between geometric coherence and human semantic meaning. The
morphological analyses demonstrate that curves assigned to the same learned
primitive exhibit greater geometric similarity than curves assigned to
different primitives. The positional and sequential analyses further show that
primitive identities are associated with characteristic structural roles.
Together, these findings establish measurable organization within the learned
representation.

They do not, however, establish that individual primitives correspond to
human-defined garment concepts.

The primitive vocabulary was learned from geometric structure rather than
from independent semantic annotations. Consequently, a primitive is defined
in the present study by the properties of its learned geometric
representation, together with its observed positional and sequential
behavior.
Its interpretation as a particular garment component would require evidence
external to the learning procedure itself.

This distinction is important because geometric regularity and semantic
interpretability are related but not equivalent properties. A geometric unit
may recur consistently because it represents a particular structural form,
without that form necessarily having a unique or universally agreed human
semantic label. Conversely, a human-defined garment concept may be expressed
through multiple geometric configurations depending on design, viewpoint, or
sketching style.

The relationship between the learned primitives and the predefined semantic
families provides further evidence that these levels of representation should
not be conflated. The predefined families provide a broader categorical
organization, but they do not fully account for the multidimensional
structural organization of the learned primitives. The learned vocabulary
therefore should not be interpreted simply as a rediscovery of the predefined
semantic taxonomy.

This distinction also affects the interpretation of the term "semantic
language." The present results provide evidence for a structured symbolic
representation of garment geometry and for grammar-like sequential
organization. They do not provide independent validation that the symbols
carry stable human semantic meanings.

Accordingly, the learned representation is best regarded as a computational
intermediate representation between sketch geometry and higher-level semantic
interpretation. It provides a vocabulary of recurring geometric units and
their structural relationships, while leaving the mapping from these units to
human concepts as a separate empirical question.

Establishing such a mapping would require additional evidence, including
independent expert annotation, agreement across annotators, explicit
primitive-to-concept correspondence analyses, or evaluation of whether
human-interpretable concepts can be reliably predicted from the learned
representation.

The present study therefore deliberately separates **structural discovery**
from **semantic validation**. This separation allows the observed geometric
and sequential organization to be interpreted on its own evidence without
assuming that computationally learned primitives necessarily correspond to
predefined human concepts.

## 5.9 Relationship Between Learned Primitives and Predefined Families

The learned primitive vocabulary and the predefined semantic-family taxonomy
capture related but non-equivalent levels of organization.

The family representation provides a broader grouping of primitives, and the
family-level analyses showed that these broader categories contain meaningful
sequential structure. However, the integrated structural comparison of the
12 learned primitives showed only modest alignment with the predefined family
assignments. Primitives belonging to the same family were somewhat more
structurally similar than primitives belonging to different families, but the
observed separation did not reach statistical significance under the
permutation test.

This finding suggests that the learned primitive organization is not simply a
recovery of the predefined family taxonomy. Instead, the learned vocabulary
appears to capture finer-grained structural variation that cuts across the
broader family categories.

The distinction is useful for understanding the role of the predefined
families in the overall representation. Families provide an interpretable
higher-level grouping that can reveal broad transition regularities, whereas
the learned primitives retain more detailed morphological and sequential
distinctions. The increase in transition similarity observed after moving
from individual primitives to broader families is consistent with this
hierarchical interpretation.

At the same time, the modest and non-significant structural alignment with
family membership indicates that the family taxonomy does not fully explain
the multidimensional organization of the learned primitives. The learned
representation therefore should not be characterized as merely reproducing
the semantic categories supplied by the original taxonomy.

Instead, the two levels provide complementary descriptions: predefined
families offer a broader categorical abstraction, while learned primitives
provide a finer-grained geometry-derived vocabulary whose structural
organization is determined empirically from the sketch corpus.

This distinction is important for the proposed framework because it preserves
the possibility that useful structural organization may exist at levels that
are not captured by predefined semantic categories. The learned vocabulary
can therefore serve as an empirical intermediate representation without
requiring the higher-level family taxonomy to determine its internal
organization.

## 5.10 Generalization Across Sketchers and Unseen Garments

The study provides two complementary forms of evidence concerning the
generalization of the learned structural representation: evaluation on
garments excluded from sequential-model estimation and evaluation under
cross-sketcher conditions in the independent CLO-SK benchmark.

For sequential prediction, the context-conditioned model was evaluated on
garments that were completely excluded from estimation of the transition
probabilities. The predictor retained substantial improvement over the
training-set global-majority baseline on these unseen garments. This result
indicates that the predictive value of immediate primitive context is not
restricted to the exact garment sequences used to estimate the transition
model.

This finding is particularly relevant to the interpretation of the proposed
visual grammar. If sequential dependencies were primarily a consequence of
memorizing individual garment sequences, their predictive advantage would be
expected to diminish substantially when evaluated on excluded garments. The
persistence of the effect instead supports the interpretation that local
primitive context captures reusable sequential regularities within the
evaluated corpus.

The CLO-SK benchmark provides a complementary test under variation in
sketcher. The cross-sketcher evaluation explicitly excluded candidates
produced by the same sketcher as the query, thereby preventing retrieval
performance from being driven solely by sketcher-specific similarity. Raw
geometry remained substantially stronger than the symbolic representations
under this condition, but the frozen symbolic representation continued to
exhibit measurable identity-associated, category-associated, and
geometry-associated structure.

These two evaluations address different forms of generalization. The unseen-
garment experiment tests whether sequential predictive structure transfers
beyond the garments used to estimate the transition model. The cross-sketcher
benchmark tests whether measurable structural properties remain present when
the sketcher producing the query and candidate sketches differs.

The evidence therefore supports **limited empirical generalization within the
evaluated populations**. It does not establish invariance to arbitrary
sketching styles, designers, datasets, or garment domains. In particular, the
lower symbolic retrieval performance under cross-sketcher evaluation shows
that substantial sketch-specific geometric information remains outside the
symbolic representation.

The appropriate conclusion is consequently narrower than universal
generalization. The learned representation demonstrates reusable structural
regularities across the tested unseen-garment and cross-sketcher settings,
while broader domain invariance remains an open empirical question.

## 5.11 Computational Implications

The findings suggest that garment sketches can be represented at multiple
computational levels rather than being treated exclusively as continuous
images. The learned primitive vocabulary provides an intermediate discrete
representation in which recurring geometric configurations can be identified,
compared, and organized according to their structural relationships.

This intermediate representation has several potential computational
uses.

First, it provides an explicit vocabulary for representing recurring geometric
units. Instead of requiring downstream models to rediscover these units from
raw image data for every task, a symbolic representation can expose the
primitive composition of a garment directly.

Second, the sequential organization of the primitives provides an explicit
representation of structural relationships. Because immediate primitive
context contains predictive information about subsequent primitives, the
representation can support computational analyses of garment sequence,
transition structure, and compositional organization.

Third, the primitive-level profiles provide a basis for structured knowledge
representation. A primitive can be described through a combination of its
geometric morphology, characteristic sequence position, semantic-family
membership, and local sequential neighborhood. These attributes provide a
more explicit representation of structural roles than an isolated geometric
embedding.

Fourth, the representation provides a potential intermediate layer between
visual input and higher-level semantic analysis. The present study establishes
the geometry-to-primitive and primitive-to-sequence components of such a
representation. Human semantic interpretation can subsequently be introduced
as an additional layer rather than being imposed during the initial discovery
of geometric units.

The independent benchmark further suggests that this intermediate
representation can retain selected structural information outside the primary
corpus. However, its substantially weaker direct retrieval performance than
raw geometry demonstrates that it should not be regarded as a replacement for
the underlying visual representation.

The computational implication is therefore best understood as a change in
representation rather than a universal improvement in performance. Raw
geometry remains valuable when fine-grained visual fidelity is required,
whereas the symbolic representation makes recurring structural organization
explicit.

This distinction may be useful for downstream systems in which structural
decomposition, sequence analysis, symbolic comparison, or knowledge
representation is more important than exact visual matching. These potential
applications remain to be evaluated directly and are therefore not claimed as
demonstrated capabilities of the present study.

More broadly, the learned vocabulary provides a foundation on which future
systems could integrate geometric, sequential, categorical, and independently
validated semantic information. The present work establishes the structural
layer of such a framework rather than the complete semantic system.

## 5.12 Limitations

Several limitations define the scope of the present findings.

### 5.12.1 Scope of the Primary Corpus

The primary corpus contains 333 garment sketches. Although this corpus supports
the reported analyses of morphology, sequence, and composition, it represents
only a limited sample of the broader space of garment designs and sketching
practices.

The learned vocabulary should therefore be interpreted as a vocabulary
established for the evaluated corpus rather than as a universally complete
inventory of garment geometry. Larger and more diverse collections will be
required to determine how stable the primitive vocabulary remains across
design domains, garment categories, and sketching conventions.

### 5.12.2 Scope of the Independent Benchmark

The CLO-SK benchmark provides an independent evaluation population containing
2,299 images, 230 garment identities, 23 categories, and 12 sketchers. This
provides an important test of transfer beyond the primary corpus, but it
remains a single external benchmark.

Consequently, the observed transferability should not be interpreted as
evidence of universal generalization across all fashion-sketch datasets,
designers, or drawing conventions.

### 5.12.3 Information Loss Through Symbolic Abstraction

The retrieval experiments demonstrate a fundamental limitation of the
symbolic representation. Raw geometric signatures substantially outperform
the symbolic representations for direct garment-identity retrieval.

This indicates that discretization into primitive identities removes
fine-grained geometric information that remains available in the original
continuous representation.

The symbolic vocabulary should therefore not be interpreted as a complete
replacement for the underlying geometry. Applications requiring precise
visual identity, reconstruction, or fine-grained geometric matching would
require additional information beyond the primitive sequence itself.

### 5.12.4 Limited Morphological Measurement

The independent primitive–geometry association analysis used two independently
measured geometry variables: `signature_length` and `foreground_fraction`.

These variables capture meaningful aspects of sketch geometry but do not
constitute a complete description of garment morphology. The resulting
primitive morphology profiles should therefore be interpreted as partial
computational descriptors of geometric organization.

Additional shape descriptors could reveal further associations that are not
captured by the present analysis.

### 5.12.5 Semantic Validation

The learned primitives were derived from geometry rather than independently
annotated human semantic concepts. Their morphological coherence and
structural roles therefore establish computational organization, but do not
establish human semantic interpretation.

Independent expert annotation, inter-annotator agreement, and explicit
primitive-to-concept correspondence analyses would be required to determine
whether individual primitives consistently correspond to human-recognizable
garment structures.

This is a central limitation rather than a minor methodological detail,
because the distinction between geometric structure and semantic meaning
defines the evidential boundary of the present study.

### 5.12.6 Sequential Model Scope

The predictive sequential analysis primarily evaluates immediate predecessor
context, with an additional comparison using two preceding primitives.

Although immediate context provides substantial predictive information, the
present experiments do not establish that all relevant sequential dependencies
are local or first-order.

Longer-range dependencies, hierarchical sequence structure, and alternative
sequence models remain to be investigated.

Similarly, the observed predictive organization does not by itself constitute
a complete generative grammar.

### 5.12.7 Identity and Sketcher Variation

The benchmark demonstrates measurable within-identity primitive-set
similarity and retains structural information under cross-sketcher
evaluation. However, within-identity similarity remains modest, and symbolic
sequences are not invariant across sketches of the same garment.

This indicates that the representation captures recurring structural content
without eliminating variation between sketch instances.

Such variation may arise from differences in sketcher style, geometric
expression, or other properties of individual sketch production. The present
experiments do not isolate these sources of variation.

### 5.12.8 Association Does Not Establish Causation

The primitive–geometry analyses identify statistical associations between
primitive usage and independently measured geometric variables.

These associations do not establish causal relationships, nor do they imply
that a particular primitive uniquely determines a particular geometric
property.

Similarly, category-associated primitive information does not demonstrate
that primitive identity is sufficient for reliable garment-category
classification.

### 5.12.9 Benchmark Retrieval as a Limited Evaluation Task

Retrieval performance provides a useful test of information preservation, but
it is only one evaluation of the symbolic representation.

The weaker retrieval performance of the symbolic representations does not
demonstrate that they are generally less useful than raw geometry for every
downstream task. Conversely, measurable structural associations do not
demonstrate superiority for any particular application that was not directly
evaluated.

The appropriate interpretation is therefore task-specific: the present
benchmark establishes the relative preservation of information for the tested
retrieval task while the structural analyses establish other measurable
properties of the representation.

### 5.12.10 Limits of the Present Semantic-Family Analysis

The predefined semantic families provide a useful higher-level comparison,
but the observed alignment between family membership and the integrated
primitive structural representation was modest and not statistically
significant under permutation testing.

This means that the learned primitive organization should not be interpreted
as either a direct reproduction of the predefined taxonomy or as evidence
that the predefined family structure is incorrect.

Rather, the analysis demonstrates that the learned multidimensional
organization is not fully explained by the existing family assignments.

### 5.12.11 Overall Scope of the Limitations

Taken together, these limitations indicate that the present study establishes
a geometry-derived symbolic representation with measurable morphological,
positional, sequential, and compositional structure, but does not establish a
universal vocabulary, a complete visual encoding, or a validated human
semantic language of fashion design.

The limitations therefore define the appropriate scope of the contribution:
the study establishes a computational structural layer that can serve as a
basis for subsequent semantic validation and broader generalization studies.

## 5.13 Evidential Boundary

The combined findings define a clear boundary around the claims supported by
the present study.

The evidence supports the conclusion that garment sketches contain recurring
geometric structure that can be learned as a coherent vocabulary of discrete
primitives. The learned primitives exhibit morphological coherence and
characteristic positional and sequential organization. Primitive sequences
also contain predictive context-dependent structure, and complete garments can
be represented as ordered combinations of a shared vocabulary.

The independent CLO-SK evaluation provides additional evidence that these
structural properties are not restricted to the primary research corpus.
The frozen representation retains measurable identity-associated,
category-associated, and geometry-associated information in an independent
sketch population, including under cross-sketcher evaluation.

The evidence does not support the stronger claim that the symbolic
representation preserves the complete visual information contained in a
garment sketch. The retrieval experiments demonstrate the opposite: raw
geometry substantially outperforms the symbolic representations for direct
garment-identity retrieval.

The evidence also does not establish that individual learned primitives
correspond to human-defined garment components. Their identities are
supported by geometric coherence and structural behavior, but independent
semantic validation has not yet been performed.

Similarly, the sequential results support describing the representation as
grammar-like, but they do not establish a complete generative grammar of
fashion sketches. The experiments demonstrate predictive sequential
organization and non-random transition structure rather than a complete set
of production rules or a universal model of garment construction.

Finally, the external benchmark does not establish universal invariance
across sketchers, designers, datasets, or garment domains. It demonstrates
transfer of measurable structural information to the evaluated independent
population, while also showing that substantial sketch-specific geometric
information remains outside the symbolic representation.

The appropriate scientific claim is therefore deliberately narrower:

> **Garment sketches contain recurring geometric units and sequential
> regularities that can be learned and represented computationally as a
> structured, compositional, and reusable symbolic vocabulary.**

This claim is supported by convergent evidence from morphological coherence,
sequence organization, predictive context, compositional reuse, and
independent benchmark evaluation.

The stronger proposition that this symbolic vocabulary constitutes a complete
or universally human-interpretable semantic language of fashion design remains
an open empirical question.

Maintaining this distinction is important because the contribution of the
present study lies in establishing the computational structural layer on which
such semantic interpretation can subsequently be investigated, rather than
assuming semantic meaning from geometric regularity alone.

## 5.14 Future Research

The present findings establish a computational structural representation but
also identify several empirical questions that remain open. These questions
follow directly from the boundaries of the current evidence.

### 5.14.1 Independent Semantic Validation

The most direct next step is to evaluate whether learned primitives and their
structural profiles correspond to human-recognizable garment concepts.
Independent expert annotation could be used to determine whether particular
primitives consistently correspond to specific structural or semantic
properties of garments.

Such evaluation should include multiple annotators and explicit measurement
of agreement rather than relying on a single researcher-defined mapping. This
would allow the relationship between geometry-derived primitives and
human-interpretable concepts to be tested independently of the primitive
learning procedure.

### 5.14.2 Expansion of Morphological Representation

The present benchmark morphology analysis used two independent geometry
variables: `signature_length` and `foreground_fraction`. Future work can
extend this representation to include additional shape descriptors capturing
properties such as curvature, spatial extent, orientation, topology, and other
geometric characteristics.

A richer morphology representation would allow investigation of whether the
observed primitive profiles remain stable when a broader range of geometric
properties is considered.

### 5.14.3 Broader Evaluation of Sequential Structure

The present sequential analyses demonstrate predictive value in immediate
primitive context, while higher-order context provides only a modest
additional improvement. Future work can investigate longer-range and
hierarchical dependencies between primitives.

Such models could test whether garment structure contains dependencies that
extend beyond local predecessor-successor relationships and whether those
dependencies can be represented through more explicit hierarchical or
probabilistic sequence models.

This would provide a stronger empirical basis for determining how far the
grammar-like interpretation extends.

### 5.14.4 Cross-Dataset and Cross-Style Generalization

The independent CLO-SK benchmark demonstrates transfer to an external
population, but broader evaluation is required to establish the robustness of
the learned vocabulary.

Future experiments should evaluate the frozen representation across datasets
containing different sketching conventions, designers, garment categories,
and drawing styles. Cross-dataset evaluation would provide a stronger test of
whether the learned primitives represent recurring properties of garment
structure rather than properties specific to a particular corpus.

### 5.14.5 Task-Oriented Evaluation of the Symbolic Representation

The present retrieval experiments establish that symbolic abstraction does
not preserve all information required for direct garment-identity retrieval.
Future work should therefore evaluate the representation on tasks for which
structural abstraction is expected to be useful.

Potential evaluations include structural comparison, primitive sequence
analysis, garment-structure classification, symbolic retrieval, and
knowledge-based reasoning. Such experiments would determine whether the
explicit structural representation provides advantages that are not visible
in direct image-level retrieval.

These evaluations should be performed independently rather than assuming that
the existence of a structured representation automatically produces
downstream performance gains.

### 5.14.6 Integration of Structural and Semantic Information

The present representation establishes a geometry-derived structural layer.
A natural subsequent step is to integrate this layer with independently
validated semantic information.

Such a framework could associate learned geometric primitives with annotated
garment concepts while retaining the original geometric and sequential
evidence. This would allow semantic relationships to be represented as an
additional layer rather than being imposed on the primitive-learning stage.

The resulting architecture could be evaluated to determine whether combining
geometry-derived structure with validated semantic information provides a
more complete representation of garment sketches.

### 5.14.7 Stability of the Learned Vocabulary

An additional question concerns the stability of the 12-primitive vocabulary
itself. Future work should evaluate how primitive identities and morphology
profiles change when the corpus is expanded, resampled, or replaced by
independent datasets.

Such stability analysis would help distinguish primitives that represent
robust recurring geometric structures from primitives that depend more
strongly on the particular composition of the current corpus.

### 5.14.8 Toward a Validated Semantic Representation

Ultimately, the long-term objective is not simply to increase the number of
learned primitives or to construct increasingly complex sequence models.
Rather, the goal is to determine whether geometry-derived structural units
can form a reliable intermediate representation through which human semantic
knowledge can be incorporated and validated.

The present study provides the structural foundation for this direction. The
next stage is therefore not to assume a semantic language, but to test
systematically whether the learned geometric vocabulary can be connected to
human concepts, broader garment knowledge, and independently measurable design
properties.

## 5.15 Conclusion

This study investigated whether recurring structure in fashion sketches can be
learned directly from sketch geometry and represented through a reusable
symbolic vocabulary.

The results provide evidence that the learned representation captures
multiple complementary forms of structure. The 12 learned primitives exhibit
morphological coherence, characteristic positional distributions, and
structured sequential contexts. Primitive ordering contains predictive
information beyond marginal primitive frequency, and complete garment sketches
can be represented as compositions of a shared vocabulary of recurring
geometric units.

Evaluation on the independent CLO-SK benchmark provides additional evidence
that measurable structural information is retained when the frozen
representation is transferred beyond the primary research corpus. At the same
time, raw geometry substantially outperforms the symbolic representation for
direct garment-identity retrieval. This demonstrates that the learned
vocabulary is an abstraction of sketch geometry rather than a lossless
encoding of visual appearance.

The combined findings therefore support a specific interpretation of the
learned representation. Garment sketches contain recurring geometric units
and sequential regularities that can be represented computationally as a
structured, compositional, and reusable symbolic vocabulary. The representation
provides an intermediate structural layer between continuous sketch geometry
and higher-level interpretation.

The evidence does not establish that the learned primitives constitute
human-validated semantic concepts, nor that the resulting sequential
organization constitutes a complete or universal grammar of fashion design.
Those questions require independent semantic validation and broader
generalization studies.

The principal contribution of this work is therefore the establishment of a
geometry-derived computational representation in which recurring garment
structure can be identified, organized, and analyzed as discrete primitives
and their relationships. This provides a measurable foundation for future
investigation of the semantic organization of fashion sketches without
assuming semantic meaning from geometric structure alone.