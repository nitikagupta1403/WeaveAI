# CLO-SKET — Manuscript Outline

## 0. Working Manuscript Identity

### Working title

**Quantitative Organization of Garment Sketch Morphology through
Complementary Geometric Representations**

### Alternative title

**Quantitative Morphology and Radial–Angular Geometry in Garment Sketches**

### Current preferred title

**Quantitative Organization of Garment Sketch Morphology through
Complementary Geometric Representations**

The title deliberately avoids:

- semantic language;
- morphology grammar;
- morphology manifold;
- universal morphology;
- semantic primitives.

Those claims are not established by the current evidence.

---

# 1. Central Scientific Question

The manuscript asks:

> Can garment sketches be characterized as a quantitatively organized
> population using an explicit morphology representation, and does an
> independently constructed radial–angular representation reveal
> complementary geometric information?

This is the central question.

All experiments should serve this question.

---

# 2. Central Scientific Claim

The manuscript's central claim is:

> Garment sketches exhibit reproducible quantitative geometric
> organization that can be characterized using explicit morphology
> measurements, while an independently constructed radial–angular
> representation captures related but non-identical structure and
> provides additional task-level utility.

This claim has two levels.

### Primary contribution

Quantitative organization of garment-sketch morphology.

### Secondary contribution

Complementary radial-angular geometric information beyond the
135-dimensional morphology representation under the tested downstream
task.

---

# 3. Paper Logic

The paper should follow this scientific progression:

    Why study sketch morphology?
              ↓
    Explicit quantitative representation
              ↓
    Is morphology organized?
              ↓
    Independent radial-angular representation
              ↓
    Are the representations related?
              ↓
    Is the relationship sketch-specific?
              ↓
    Does radial-angular geometry add useful information?
              ↓
    Is the improvement explained by dimensionality?
              ↓
    Is utility concentrated in one descriptor block?
              ↓
    What can and cannot be concluded?

This progression should be visible throughout the manuscript.

---

# 4. Abstract

## Purpose

Provide a compact statement of:

1. problem;
2. approach;
3. dataset;
4. primary morphology result;
5. cross-branch result;
6. downstream complementarity result;
7. claim boundary.

## Structure

### Background

Garment sketches contain visual structure that is difficult to
characterize quantitatively using only semantic labels or raw image
pixels.

### Objective

Determine whether explicit image-derived morphology measurements reveal
reproducible quantitative organization and whether an alternative
radial-angular representation provides complementary information.

### Methods

Use 2,300 Clo-Sket sketches.

Construct:

    135-D morphology representation

and:

    28-D radial-angular representation.

Evaluate:

- morphology-space organization;
- feature-level association;
- cross-validated recovery;
- row-permutation correspondence;
- downstream complementarity;
- dimension-matched control;
- descriptor ablation.

### Results

Report the strongest numerical results:

    morphology → F₂ magnitude:
    CV R² = 0.2961

    morphology → R₂ at F₂ peak:
    CV R² = 0.2170

    Macro-F1:
    0.3413 → 0.4123

    Δ Macro-F1:
    +0.0710

    Balanced accuracy:
    0.3426 → 0.4157

### Conclusion

The results support reproducible quantitative morphology organization
and task-level complementary utility of radial-angular geometry.

Do NOT claim semantic understanding.

---

# 5. Introduction

## 5.1 Paragraph 1 — The Problem

Introduce garment sketches as structured visual artifacts rather than
simply images to be classified.

Motivation:

- designers communicate form through sketches;
- sketches contain shape and spatial organization;
- quantitative analysis requires representations that expose this
  structure.

---

## 5.2 Paragraph 2 — Existing Gap

Establish the gap:

Much work in visual fashion analysis emphasizes:

- recognition;
- retrieval;
- generation;
- learned visual embeddings;
- image-to-image transformation.

The present work focuses on a narrower question:

> What quantitative organization exists within garment-sketch
> morphology itself?

This section must be supported by the literature review.

---

## 5.3 Paragraph 3 — Representation Problem

Explain that raw pixels are high-dimensional and difficult to interpret,
while learned embeddings can obscure the geometric meaning of
individual coordinates.

Motivate explicit quantitative morphology measurements.

---

## 5.4 Paragraph 4 — Study Strategy

Introduce the two representations:

    explicit morphology
          +
    radial-angular geometry.

Explain that the purpose is not to claim that one representation is
"correct."

Instead, the study asks whether alternative geometric descriptions
capture overlapping and complementary structure.

---

## 5.5 Paragraph 5 — Contribution

State the contributions explicitly.

### Contribution 1

An explicit 135-dimensional quantitative morphology representation for
2,300 garment sketches.

### Contribution 2

A systematic analysis of quantitative morphology organization using
multiple geometric and permutation-based analyses.

### Contribution 3

Cross-branch evaluation showing reproducible correspondence between
morphology and independently constructed radial-angular geometry.

### Contribution 4

A downstream complementarity analysis demonstrating additional
task-level utility of the radial-angular representation beyond
morphology.

### Contribution 5

Dimension-matched and descriptor-ablation controls that constrain
interpretation of the downstream improvement.

---

# 6. Related Work

## 6.1 Fashion Sketch Understanding

Review literature on:

- fashion sketch recognition;
- garment sketch analysis;
- clothing image understanding;
- sketch-based fashion retrieval.

Question:

> What has been measured about the internal morphology of fashion
> sketches?

---

## 6.2 Shape and Silhouette Representation

Review:

- shape descriptors;
- occupancy-based representations;
- silhouette representations;
- contour-based methods;
- geometric descriptors.

Position the 135-D representation carefully.

Do not claim that occupancy profiles themselves are novel.

The contribution is the analysis of the quantitative organization they
enable in this domain.

---

## 6.3 Representation Learning

Review:

- learned visual embeddings;
- dimensionality reduction;
- representation geometry;
- self-supervised visual representations.

Position explicit morphology as complementary to opaque learned
representations.

---

## 6.4 Radial and Angular Shape Representations

Review relevant:

- radial descriptors;
- polar representations;
- angular shape descriptors;
- contour geometry;
- relational geometric representations.

Clearly distinguish existing mathematical ideas from the specific
radial-angular representation used here.

---

## 6.5 Semantic Fashion Representation

Review work involving:

- garment parts;
- attributes;
- semantic parsing;
- fashion vocabularies;
- sketch semantics.

Use this literature to establish the boundary:

    existing semantic interpretation
              vs
    present quantitative morphology analysis.

---

## 6.6 Gap Statement

End Related Work with:

> Existing work provides powerful mechanisms for recognizing or
> generating fashion imagery, but comparatively less attention has been
> given to establishing and validating an explicit quantitative
> morphology space for garment sketches and examining how alternative
> geometric representations relate to that space.

This statement must be adjusted after the final literature review.

---

# 7. Methods

## 7.1 Dataset

Describe:

    Clo-Sket
    n = 2300.

Include dataset provenance and category structure.

---

## 7.2 Canonical Image Preprocessing

Describe exactly:

    grayscale conversion
    intensity normalization
    foreground threshold
    64 × 64 canonical spatial size.

Use the frozen preprocessing definition.

Do not imply optimization unless demonstrated.

---

## 7.3 Morphology Representation

Define:

    horizontal occupancy = 64
    vertical occupancy = 64
    global descriptors = 7

Total:

    135 dimensions.

Explain mathematically what occupancy means.

Include one intuitive example.

---

## 7.4 Morphology Representation Freezing

State that the morphology matrix was treated as a frozen artifact.

Include:

- shape;
- dtype;
- feature ordering;
- SHA-256;
- provenance.

This is important for reproducibility.

---

## 7.5 PCA

Describe PCA only where necessary.

State:

- where standardization occurs;
- variance-retention criterion;
- number of retained coordinates;
- whether PCA is fitted globally or within folds for predictive
  analyses.

Important distinction:

### Exploratory morphology PCA

Describe the global morphology organization analysis.

### Predictive PCA

For Cell 5-type target construction, PCA is fitted within training
folds.

Do not mix these two uses.

---

## 7.6 Morphology Organization Analyses

Describe the analyses that establish quantitative organization.

Organize them by scientific question rather than notebook cell.

Possible subsections:

### Variance structure

### Neighborhood structure

### Graph organization

### Density organization

### Ordered occupancy structure

### Permutation controls

---

# 8. Radial–Angular Representation

## 8.1 Motivation

Explain why a second geometric representation is useful.

The objective is to test representation sensitivity and
complementarity.

---

## 8.2 Descriptor Construction

Define:

    F₂ radial = 9
    α₂ = 7
    observed circular = 3
    learned circular = 4
    relational = 5

Total:

    28 dimensions.

Use the exact terminology established in the computational analysis.

---

## 8.3 Important Clarification

The number 28 is not claimed to be mathematically optimal.

State:

> "The 28-dimensional representation is the predefined compact
> radial-angular descriptor set evaluated in this study."

---

# 9. Provenance and Alignment

Describe:

- 2,300 morphology observations;
- 2,300 radial-angular observations;
- image-path arrays;
- exact row-order matching;
- duplicate/empty reference audit.

State:

> Cross-branch association analyses were performed only after
> row-level provenance was verified.

This is a critical methodological safeguard.

---

# 10. Cross-Branch Association

## 10.1 Feature-Level Association

Describe:

- Spearman correlation;
- 135 morphology features;
- four radial-angular targets;
- Benjamini–Hochberg FDR correction.

Explicitly state:

> Association does not imply redundancy, complementarity, causality, or
> semantic meaning.

---

## 10.2 Cross-Validated Recovery

Describe:

- 5-fold cross-validation;
- shuffled folds;
- random state 42;
- out-of-sample prediction;
- R²;
- MAE;
- RMSE;
- Spearman correlation.

---

# 11. Permutation-Validated Correspondence

Describe the row-permutation null.

Null:

    morphology[i]
    paired with
    radial-angular[π(i)].

The null preserves the target distribution while destroying
sketch-level correspondence.

State:

    permutations = 100
    seed = 2026.

Explain empirical p-value calculation.

Do not overstate p-value resolution.

---

# 12. Downstream Complementarity

## 12.1 Task

Describe the 23-category discrimination task.

Clearly distinguish:

    label-free representation construction

from:

    supervised downstream evaluation.

---

## 12.2 Baseline

    135-D morphology.

---

## 12.3 Augmented Representation

    135-D morphology
    +
    28-D radial-angular.

---

## 12.4 Evaluation

Describe:

- cross-validation;
- primary metric: Macro-F1;
- secondary metric: Balanced Accuracy.

---

# 13. Dimension-Matched Control

Describe how the number of added dimensions is preserved while
true sketch-level correspondence is destroyed.

Scientific question:

> Is the observed improvement explained merely by adding features?

Interpretation:

> The control tests dimensional expansion as an alternative
> explanation.

Do not call it an information-theoretic independence test.

---

# 14. Descriptor Ablation

Describe the predefined radial-angular blocks:

- F₂ radial;
- α₂;
- observed circular;
- learned circular;
- relational;
- full RA.

Scientific question:

> Is downstream utility concentrated in one descriptor block?

State the limitation:

> Block-specific statistical significance was not separately tested.

---

# 15. Results

Results should mirror the Methods structure.

## 15.1 Morphology Organization

Present:

- Figure 2;
- Table 2.

Primary message:

> reproducible quantitative organization.

---

## 15.2 Cross-Branch Association

Present:

- feature association results;
- selected effect sizes.

Avoid listing all 135 features in the main text.

Move complete feature tables to Supplementary Material.

---

## 15.3 Morphology → Radial-Angular Recovery

Present:

- Figure 3;
- Table 3.

Highlight:

    F₂ magnitude:
    R² = 0.2961

    R₂ at F₂ peak:
    R² = 0.2170.

Mention weaker recovery for F₂ radius.

This variation should be retained rather than hidden.

---

## 15.4 Permutation Correspondence

Present:

- Figure 4;
- Table 4.

Message:

> observed cross-validated recovery exceeded all 100 row-permutation
> replicates.

---

## 15.5 Downstream Complementarity

Present:

- Figure 5;
- Table 5.

Main result:

    Macro-F1:
    0.3413 → 0.4123

    Balanced accuracy:
    0.3426 → 0.4157.

---

## 15.6 Dimension-Matched Control

Present alongside complementarity.

Message:

> improvement is not adequately explained by dimensional expansion
> alone under the tested control.

---

## 15.7 Descriptor Ablation

Present:

- Figure 6;
- Table 6 or Supplementary Table.

Message:

> full radial-angular representation produced the largest observed
> downstream gain among the tested configurations.

---

# 16. Discussion

The Discussion should follow this structure.

## 16.1 Principal Finding

Quantitative morphology is structured.

## 16.2 Why Explicit Morphology Matters

Interpretability and measurable geometry.

## 16.3 Why PCA Is Not the Contribution

PCA is a tool, not the scientific claim.

## 16.4 Why the Radial-Angular Branch Matters

Alternative coordinate description.

## 16.5 Association vs Complementarity

Explain the evidence progression.

## 16.6 Why the Permutation Result Matters

Actual sketch-level correspondence.

## 16.7 Why the Dimension-Matched Control Matters

Rules out simple feature-count explanation under the tested null.

## 16.8 What "Complementary" Means Here

Task-level complementarity, not information-theoretic independence.

## 16.9 Representation Sensitivity

Different coordinate systems expose different useful structure.

## 16.10 Relationship to Semantic Understanding

Position the work as a quantitative substrate, not semantic
validation.

## 16.11 Limitations

Use the reviewer-risk document.

## 16.12 Future Work

Prioritize:

1. external validation;
2. preprocessing sensitivity;
3. larger permutation analysis;
4. model-family robustness;
5. semantic annotation.

---

# 17. Conclusion

The conclusion should be short.

Recommended structure:

### Sentence 1

Garment sketches exhibit reproducible quantitative geometric
organization under an explicit morphology representation.

### Sentence 2

An independently constructed radial-angular representation is
systematically associated with morphology and captures additional
task-relevant structure.

### Sentence 3

The downstream improvement survives the dimension-matched control and
is not confined to a single descriptor block.

### Sentence 4

The results provide a quantitative representation-level foundation
for future investigation of semantic structure in garment sketches.

Do NOT conclude:

> "We discovered the semantic language of fashion."

---

# 18. Supplementary Material

The Supplementary Material should contain details that are scientifically
important but would interrupt the main narrative.

Recommended contents:

## Supplementary S1

Complete 135-feature list.

## Supplementary S2

Complete feature-wise Spearman association tables.

## Supplementary S3

Complete FDR results.

## Supplementary S4

All morphology-space statistical diagnostics.

## Supplementary S5

Complete permutation distributions.

## Supplementary S6

Descriptor-level ablation details.

## Supplementary S7

Dimension-matched control details.

## Supplementary S8

Provenance and artifact audit.

## Supplementary S9

Additional visualization panels.

---

# 19. What Does NOT Belong in the Main Manuscript

Do not include every notebook output.

Avoid:

- raw debugging logs;
- object existence checks;
- Python variable names;
- repeated shape audits;
- every individual correlation;
- every intermediate visualization;
- implementation errors;
- notebook execution history.

The manuscript describes the scientific procedure.

The repository preserves the computational history.

---

# 20. What Must Be Preserved in the Repository

The following should remain available even if omitted from the manuscript:

- frozen morphology artifact;
- radial-angular artifact;
- provenance arrays;
- feature names;
- metadata;
- random seeds;
- fold definitions;
- permutation results;
- downstream predictions;
- residuals;
- ablation results;
- dimension-matched control results;
- figure-generation code;
- analysis notebooks.

---

# 21. Claim Hierarchy

Every major claim should map to evidence.

| Claim | Evidence |
|---|---|
| Morphology is quantitatively organized | Morphology-space analyses |
| Morphology and RA are associated | Cell 3 |
| Morphology recovers RA | Cell 4 |
| Correspondence is sketch-specific | Cell 6 |
| RA improves downstream task | Cells 8–9 |
| Improvement is not simple dimension count | Cell 10 |
| Utility is not confined to one RA block | Cell 11 |

No claim should appear in the manuscript without an identifiable
analysis supporting it.

---

# 22. Claims Explicitly Excluded

The manuscript will not claim:

- semantic novelty;
- semantic garment-part recognition;
- universal morphology categories;
- morphology primitives;
- morphology grammar;
- mathematical manifold structure;
- causal mechanisms;
- information-theoretic independence;
- human-like visual understanding.

These may appear only as future research questions.

---

# 23. Manuscript Narrative in One Paragraph

Garment sketches are treated as quantitative geometric objects rather
than only as semantic images. An explicit 135-dimensional morphology
representation is constructed from occupancy profiles and global
descriptors and evaluated for reproducible organization across
multiple geometric analyses. An independently constructed
28-dimensional radial-angular representation is then used to test
whether alternative geometric coordinates capture related structure.
Feature-wise association, cross-validated recovery, and
row-permutation analysis establish reproducible sketch-level
correspondence. A downstream 23-category discrimination experiment
then tests whether radial-angular geometry adds task-level utility
beyond morphology. The observed improvement survives a
dimension-matched control and is not confined to a single descriptor
block. Together, the results support quantitative geometric
organization and representation-level complementarity without
requiring claims of semantic primitives, grammar, manifold structure,
or information-theoretic independence.

---

# 24. Final Manuscript Architecture

The final paper should therefore be:

    TITLE

    ABSTRACT

    1. INTRODUCTION

    2. RELATED WORK

    3. METHODS
       3.1 Dataset
       3.2 Canonical preprocessing
       3.3 Morphology representation
       3.4 Morphology organization analysis
       3.5 Radial-angular representation
       3.6 Provenance alignment
       3.7 Cross-branch association
       3.8 Cross-validated recovery
       3.9 Permutation correspondence
       3.10 Downstream complementarity
       3.11 Dimension-matched control
       3.12 Descriptor ablation

    4. RESULTS
       4.1 Morphology organization
       4.2 Cross-branch association
       4.3 Morphology → RA recovery
       4.4 Permutation correspondence
       4.5 Downstream complementarity
       4.6 Dimension-matched control
       4.7 Descriptor ablation

    5. DISCUSSION
       5.1 Principal findings
       5.2 Interpretation
       5.3 Representation sensitivity
       5.4 Implications
       5.5 Limitations
       5.6 Future work

    6. CONCLUSION

    REFERENCES

    SUPPLEMENTARY MATERIAL

---

# 25. Final Writing Principle

The paper should not read as:

    "Here are all the things we tried."

It should read as:

    "Here is a scientific question.
     Here is a representation.
     Here is the evidence that it is structured.
     Here is an independent geometric description.
     Here is evidence that the two correspond.
     Here is evidence that the second adds task-level utility.
     Here are the controls that constrain that interpretation.
     Here is what we still cannot claim."

That is the final narrative architecture of CLO-SKET.