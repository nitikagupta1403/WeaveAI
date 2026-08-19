# CLO-SKET — Discussion

## 1. Principal Finding

This study investigated whether garment sketches can be characterized
as a quantitatively organized population using explicit image-derived
morphology measurements, and whether an independently derived
radial–angular representation captures complementary geometric
information.

The results provide evidence for three related findings.

First, the 135-dimensional morphology representation exhibits
reproducible quantitative organization across multiple geometric
analyses.

Second, independently derived radial–angular measurements are
systematically associated with the morphology representation and can
be recovered from it to varying degrees under cross-validation.

Third, the radial–angular representation improves downstream
discrimination beyond the morphology representation under the tested
23-category task, with the improvement surviving a dimension-matched
permutation control.

The most important interpretation is therefore not that either
representation is a complete description of garment form.

Rather:

> garment-sketch morphology can be measured quantitatively, and
> different geometric coordinate systems can expose overlapping but
> non-identical structure in that morphology.

---

# 2. What the Morphology Representation Establishes

The first objective of the study was to determine whether a simple,
explicit representation based on occupancy profiles and global
descriptors could reveal reproducible organization in garment sketches.

The representation is intentionally transparent.

Each sketch is converted into:

    64 horizontal occupancy measurements
    +
    64 vertical occupancy measurements
    +
    7 global descriptors.

This produces a 135-dimensional quantitative morphology vector.

The resulting organization was not evaluated solely through a
downstream classifier.

Instead, multiple analyses examined:

- variance structure;
- neighborhood relationships;
- graph structure;
- transitions;
- density organization; and
- permutation-based controls.

The convergence of these analyses is important.

A single visualization can make an arbitrary high-dimensional dataset
appear structured.

The present evidence is stronger because different analyses interrogate
different aspects of the representation.

The appropriate conclusion is therefore:

> the explicit morphology representation contains reproducible
> quantitative organization under the tested analyses.

It is not:

> the representation has discovered semantic garment concepts.

---

# 3. Why Explicit Morphology Matters

A major advantage of the representation is interpretability.

The coordinates have direct spatial meaning.

A horizontal occupancy coordinate describes foreground occupancy at a
specific horizontal location.

A vertical occupancy coordinate describes foreground occupancy at a
specific vertical location.

The global descriptors summarize broader geometric properties.

This differs from treating a learned embedding as an opaque coordinate
system whose dimensions have no direct interpretation.

The representation therefore provides a measurable geometric layer
between the original sketch image and higher-level semantic analysis.

This may be particularly useful in settings where the objective is not
only prediction but also understanding how variation in garment form is
organized.

---

# 4. PCA Should Be Interpreted Carefully

PCA plays an important methodological role in the study but is not the
scientific contribution itself.

The PCA analysis demonstrates that much of the standardized morphology
variance can be represented using a reduced coordinate system.

However, PCA is fundamentally a linear variance-preserving
transformation.

It does not establish:

- semantic axes;
- intrinsic dimensionality;
- a nonlinear manifold;
- independent morphological factors; or
- causal dimensions of garment form.

The retained dimensionality should therefore be interpreted as a
property of the chosen representation and variance-retention criterion,
not as the intrinsic dimensionality of garment morphology.

This distinction is important because the language of "morphology
space" should not be allowed to imply a mathematical manifold that has
not been demonstrated.

---

# 5. Morphology Organization Without Semantic Supervision

One of the more important aspects of the analysis is the separation
between quantitative organization and semantic labeling.

The morphology representation was constructed without category labels.

Likewise, the principal organization analyses did not require
predefined garment categories.

This means that the observed structure is not simply a visualization
of labels encoded into the representation.

At the same time, the absence of semantic labels does not imply that
the resulting regions have no relationship to semantic garment
categories.

The sketches may contain morphological characteristics that correlate
with human-defined categories.

The present analysis deliberately does not assign semantic meaning to
those structures.

This is a strength of the current claim boundary.

---

# 6. Density Regions Are Not Semantic Categories

The multiscale density analysis identified regions of differing
quantitative morphology density.

These regions should be interpreted as:

> regions of relatively similar quantitative morphology under the
> chosen representation and density procedure.

They should not automatically be called:

- garment types;
- garment parts;
- styles;
- morphological primitives; or
- semantic categories.

The observation that within-region dispersion remains substantial is
also important.

A density region is therefore better understood as a continuous or
heterogeneous region of morphology space rather than a discrete class.

This supports a view of garment morphology as potentially continuous
rather than naturally partitioned into a small number of rigid
categories.

However, establishing the nature of that continuity would require
additional experiments beyond the present study.

---

# 7. Why the Radial–Angular Branch Matters

The radial–angular representation was introduced for a different
reason.

If the morphology representation already captures the relevant
structure, a second representation would add little scientific value
unless it reveals information that is useful beyond the original
coordinates.

The radial–angular branch provides an independent geometric
description.

It includes:

- radial descriptors;
- angular descriptors;
- circular descriptors; and
- relational descriptors.

The resulting representation has 28 dimensions.

The important point is not that 28 is a theoretically privileged
number.

It is the dimensionality of the predefined compact radial–angular
descriptor set used in this experiment.

The scientific question is whether this representation carries useful
geometry despite being distinct from the original 135-dimensional
morphology representation.

---

# 8. Association Does Not Mean Complementarity

The feature-wise association analysis provides the first connection
between the two representations.

Many morphology coordinates were significantly associated with
radial–angular quantities after FDR correction.

This demonstrates that the two representations are not unrelated.

However, this result alone would not justify adding radial–angular
features to the morphology representation.

If two representations encode the same information, their association
could be strong while the second representation contributes almost
nothing new.

This is why the subsequent analyses are necessary.

The evidence chain progresses from:

    association

to:

    cross-validated recovery

to:

    permutation-validated correspondence

and finally to:

    downstream complementarity.

---

# 9. Morphology Recovers Radial–Angular Geometry

The cross-validated recovery results provide evidence that the
135-dimensional morphology representation contains measurable
information about independently derived radial–angular quantities.

Recovery was strongest for F₂ peak magnitude:

    CV R² = 0.2961
    Spearman ρ = 0.6415.

Recovery was weaker for F₂ peak radius:

    CV R² = 0.0594.

The other two targets showed intermediate recovery:

    R₂ at F₂ peak:
    CV R² = 0.2170

    axial error:
    CV R² = 0.1979.

This variation is informative.

The radial–angular representation is not simply an exact re-expression
of the morphology coordinates.

Some radial–angular quantities are substantially recoverable from
morphology, whereas others are only weakly recovered.

This suggests partial overlap rather than complete equivalence.

However, recoverability should not be interpreted as evidence that the
radial–angular representation is redundant.

The downstream analysis is required to answer that question.

---

# 10. Why the Permutation Result Strengthens the Argument

The row-permutation analysis addresses a different question:

> Is the observed cross-branch relationship dependent on the actual
> sketch-to-sketch correspondence?

The morphology rows remain fixed while radial–angular targets are
randomly reassigned.

This destroys the true correspondence while preserving the target
distribution.

For all four radial–angular targets, observed performance exceeded
every permutation replicate.

The empirical p-value was:

    p = 0.0099

for each target under the 100-permutation design.

The result therefore provides evidence that the measured
morphology–radial-angular correspondence is not explained simply by
the marginal distributions of the two representations.

The interpretation should nevertheless remain narrow:

> the observed correspondence is stronger than expected under the
> specified row-permutation null.

It does not prove semantic meaning or information-theoretic
independence.

---

# 11. The Strongest Result: Downstream Complementarity

The most consequential result is the downstream comparison.

Using morphology alone:

    Macro-F1 = 0.3413
    Balanced accuracy = 0.3426.

Using morphology plus the 28-dimensional radial–angular
representation:

    Macro-F1 = 0.4123
    Balanced accuracy = 0.4157.

The corresponding improvements are:

    Δ Macro-F1 = +0.0710

and:

    Δ Balanced Accuracy = +0.0730.

This is a substantial relative improvement for the tested task.

More importantly, the improvement is not being interpreted from a
single train/test split.

It is evaluated using cross-validation and compared with a
row-permutation control.

The observed improvement therefore provides evidence that the
radial–angular representation contributes useful information beyond
the morphology representation under the tested discrimination task.

---

# 12. Why the Dimension-Matched Control Matters

A skeptical reviewer could reasonably ask:

> "Did the radial–angular representation help simply because you added
> 28 more features?"

This is an important alternative explanation.

The dimension-matched control addresses it by preserving the number of
added dimensions while destroying the actual sketch-level
correspondence.

The observed correctly aligned representation produced a substantially
larger downstream improvement than the dimension-matched null.

This strengthens the interpretation that the improvement depends on the
specific geometric information contained in the radial–angular
representation rather than merely on increasing feature count.

However, this result still does not establish information-theoretic
independence.

It establishes task-level incremental utility under the tested
control.

---

# 13. Why the Ablation Matters

Another reviewer question is:

> "Is the result really caused by one particular descriptor?"

The descriptor ablation addresses this.

Every individual radial–angular block produced a positive downstream
gain relative to morphology alone.

The largest individual gain came from the F₂ radial block:

    Δ Macro-F1 = +0.0331.

The complete 28-dimensional representation produced:

    Δ Macro-F1 = +0.0710.

The full representation therefore outperformed every individual
descriptor block.

This suggests that the downstream utility is distributed across
multiple aspects of radial–angular geometry.

However, the ablation was not designed to test statistical
significance of each block independently.

Therefore the appropriate statement is:

> utility was not empirically confined to a single descriptor block.

It is not:

> every descriptor block independently contributes significant
> information.

---

# 14. What the Combined Evidence Suggests

Taken together, the analyses support a useful conceptual distinction.

The morphology representation and radial–angular representation appear
to share some information.

This is demonstrated by:

- feature-level associations; and
- cross-validated recovery.

At the same time, the radial–angular representation contributes
additional task-level utility.

This is demonstrated by:

- downstream improvement;
- permutation validation; and
- dimension-matched control.

The two representations can therefore be viewed as:

> partially overlapping but functionally complementary geometric
> descriptions of garment sketches.

This is a more defensible conclusion than either extreme:

    "the representations are identical"

or:

    "the representations contain completely independent information."

The evidence supports neither extreme.

---

# 15. Why the Result Is More Than "Just PCA"

A potential criticism of the study is:

> "Is this simply a PCA analysis of hand-designed features?"

PCA is only one component of the morphology analysis.

The scientific contribution does not rest on PCA alone.

The study establishes a sequence:

    explicit morphology measurement
          ↓
    quantitative organization
          ↓
    independent geometric representation
          ↓
    cross-representation correspondence
          ↓
    downstream complementarity
          ↓
    dimension-matched control
          ↓
    descriptor ablation.

PCA provides a useful coordinate system for part of the morphology
analysis.

It does not constitute the entirety of the scientific result.

The radial–angular analysis is particularly important because it tests
whether the quantitative morphology organization is sensitive to the
choice of geometric coordinate system.

---

# 16. Representation Sensitivity as a Scientific Result

A central implication of the study is that representation choice
matters.

The same sketches can be described using different geometric
coordinate systems.

The morphology representation emphasizes spatial occupancy and global
shape descriptors.

The radial–angular representation emphasizes radial and angular
organization.

The fact that these representations are associated but not
interchangeable suggests that quantitative morphology is not exhausted
by one coordinate system.

This motivates a broader view:

> geometric representations of garment sketches should be evaluated
> not only by their individual predictive performance but also by the
> structure and complementary information they expose relative to
> alternative representations.

This is potentially one of the most generalizable methodological
implications of the work.

---

# 17. Relationship to Semantic Understanding

The present study deliberately stops before semantic interpretation.

It does not establish that a particular region corresponds to:

- sleeve;
- neckline;
- waist;
- hem;
- collar;
- garment type; or
- another named design concept.

This is important because the observed geometric organization may
eventually prove useful for semantic interpretation, but that requires
a separate validation layer.

A future semantic study could ask whether human-annotated garment
parts, design attributes, or expert concepts align with the
quantitative morphology coordinates.

That question is not answered here.

The present study establishes the quantitative substrate on which such
a study could be performed.

---

# 18. Why We Should Not Call This a "Morphology Grammar"

The results do not establish a grammar.

A grammar would require evidence for structured compositional rules
governing how morphology primitives combine.

The present experiments establish:

- quantitative coordinates;
- geometric organization;
- density structure;
- cross-representation correspondence; and
- downstream utility.

They do not establish compositional rules.

Therefore terms such as:

> morphology grammar

should not be used as a result claim in the current manuscript.

They may be appropriate as a future research direction.

---

# 19. Why We Should Not Call This a "Manifold"

The phrase "morphology manifold" is tempting because the data exhibit
low-dimensional and geometric organization.

However, PCA variance retention, graph structure, and neighborhood
organization do not by themselves establish that the data lie on a
smooth mathematical manifold.

A rigorous manifold claim would require additional assumptions and
analyses.

The manuscript should therefore use:

> morphology space

or:

> quantitative morphology space

rather than:

> morphology manifold.

This wording preserves the geometric intuition without making a
mathematical claim that the experiments do not support.

---

# 20. Limitations

## 20.1 Dataset Scope

The study uses 2,300 sketches from Clo-Sket.

The conclusions therefore concern this dataset and its sketch
distribution.

Generalization to:

- other sketch datasets;
- professional fashion illustrations;
- technical flats;
- hand-drawn design sketches;
- culturally diverse garment systems; or
- industrial design workflows

has not been established.

---

## 20.2 Representation Dependence

The morphology representation is explicitly constructed.

Different image preprocessing procedures or alternative descriptors
could produce different morphology organization.

Likewise, the radial–angular representation is one particular
geometric construction.

The study therefore demonstrates organization under the tested
representations rather than proving a representation-independent
property of all garment sketches.

---

## 20.3 Threshold and Resolution Dependence

The canonical morphology representation depends on:

- grayscale conversion;
- intensity normalization;
- the selected foreground threshold; and
- the 64 × 64 canonical spatial resolution.

Sensitivity to alternative preprocessing parameters should therefore
be considered in future work.

---

## 20.4 Radial–Angular Dimensionality

The 28-dimensional radial–angular representation is predefined.

The study demonstrates that this representation is useful under the
tested task.

It does not establish that 28 is the optimal dimensionality.

Nor does it establish that every one of the 28 coordinates is
necessary.

The descriptor ablation partially addresses this issue, but a formal
dimensionality-selection study would be a separate experiment.

---

## 20.5 Downstream Task Dependence

Complementarity is demonstrated under a specific 23-category
discrimination task.

Therefore:

> "complementary representation"

should be understood as:

> complementary under the tested downstream task.

The study does not establish universal complementarity across all
possible tasks.

A representation could be complementary for one task and redundant
for another.

---

## 20.6 Permutation Count

The principal permutation analyses use 100 permutations.

This is sufficient to establish that the observed statistic exceeded
all sampled null replicates under the specified design, but it limits
the resolution of the empirical p-value.

The minimum nonzero p-value under the +1 correction is approximately:

    0.0099.

Future confirmatory analyses could use substantially more permutations
if finer null-distribution resolution is required.

---

## 20.7 Semantic Validation

The study intentionally does not use semantic garment-part
annotations to validate the morphology representation.

Consequently, no claim can yet be made that the discovered geometric
organization corresponds to human-interpretable design concepts.

This is a limitation and also a deliberate scope boundary.

---

## 20.8 Causality

All analyses are observational with respect to the relationship
between morphology and radial–angular geometry.

No causal mechanism is established.

---

# 21. Alternative Explanations Considered

The experimental sequence explicitly addresses several alternative
explanations.

### Alternative 1: The two representations are unrelated

Addressed by:

- feature association;
- cross-validated recovery; and
- permutation correspondence.

Result:

> not supported under the tested analyses.

### Alternative 2: The radial–angular representation is merely redundant

Addressed by:

- downstream complementarity analysis.

Result:

> not supported under the tested task.

### Alternative 3: Improvement is caused only by adding dimensions

Addressed by:

- dimension-matched control.

Result:

> not supported under the tested control.

### Alternative 4: One radial–angular descriptor explains everything

Addressed by:

- descriptor ablation.

Result:

> the full representation outperformed each individual block.

### Alternative 5: The result is simply semantic labels encoded in the
representation

Addressed partially by:

- constructing the morphology representation without category labels;
- performing the principal morphology organization analyses without
  category labels.

However, the downstream task itself necessarily uses category labels.

Therefore this alternative is not completely eliminated for the
downstream result.

---

# 22. Broader Scientific Implication

The study suggests that garment sketches can be investigated at a
level between raw pixels and semantic labels.

A useful conceptual hierarchy is:

    pixels
      ↓
    explicit quantitative morphology
      ↓
    geometric organization
      ↓
    alternative geometric representations
      ↓
    semantic interpretation

The present study focuses on the middle layers.

This is potentially useful because semantic models often depend on
representations whose geometric structure is difficult to inspect.

An explicit quantitative morphology layer provides a measurable
intermediate representation that can be tested independently.

---

# 23. Future Work

The most direct next steps are not additional variations of the same
unsupervised analysis.

They are validation experiments.

### 23.1 Human Semantic Validation

Test whether morphology-space regions and coordinates correspond to
human expert judgments of garment form.

### 23.2 Garment-Part Annotation

Introduce explicit annotations for:

- neckline;
- sleeve;
- hem;
- waist;
- collar;
- silhouette;
- and other design elements.

Then test whether semantic attributes align with quantitative
morphology structure.

### 23.3 Cross-Dataset Validation

Repeat the analysis on independent fashion-sketch datasets.

### 23.4 Representation Stability

Evaluate whether the morphology organization survives:

- resolution changes;
- threshold changes;
- alternative occupancy definitions; and
- alternative explicit shape descriptors.

### 23.5 Learned Representations

Compare the explicit morphology representation with learned visual
embeddings.

The question would be whether explicit morphology exposes structure
that is absent, obscured, or differently organized in learned
representations.

### 23.6 Semantic Grounding

The ultimate extension would connect quantitative morphology to
designer-defined semantic concepts without assuming that the semantic
categories are already present in the geometric representation.

---

# 24. Final Interpretation

The strongest interpretation supported by the present evidence is:

> Garment sketches contain reproducible quantitative geometric
> organization that can be characterized using an explicit
> image-derived morphology representation. An independently derived
> radial–angular representation captures related but non-identical
> geometric information and provides reproducible additional utility
> under the tested downstream discrimination task.

This interpretation is deliberately narrower than claims of:

- semantic language;
- semantic primitives;
- morphology grammar;
- universal categories;
- mathematical manifold structure; or
- human-like visual understanding.

The study therefore provides a quantitative representation-level
foundation rather than a complete theory of garment-sketch semantics.

---

# 25. Discussion in One Sentence

The central finding is:

> **Quantitative garment-sketch morphology is structured, and its
> structure is better characterized by complementary geometric
> representations than by a single coordinate system alone.**
