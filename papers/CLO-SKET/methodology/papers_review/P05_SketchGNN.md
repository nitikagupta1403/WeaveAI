# Literature Review — Paper 05: SketchGNN
## Semantic Sketch Segmentation with Graph Neural Networks

---

## 1. Overall Assessment

**Verdict: 🟢 Important and highly relevant neighboring work; not a direct
duplicate of the CLO-SKET research question.**

SketchGNN is important because it demonstrates that structured sketch
representations — including point-level, stroke-level, and graph-based
relationships — can support semantic interpretation.

However, its scientific objective is fundamentally different from CLO-SKET.

SketchGNN asks:

> Given an established semantic vocabulary, can a model determine where
> semantic components occur in a structured sketch?

CLO-SKET asks:

> Before semantic categories are imposed, does quantitative sketch
> morphology exhibit reproducible structural organization?

The distinction is therefore not merely **supervised vs. unsupervised**.
It concerns the **direction in which the representational vocabulary is
constructed**.

---

## 2. Scientific Problem Addressed by SketchGNN

SketchGNN treats sketch understanding as a **semantic sketch segmentation**
problem.

Conceptually:

    structured sketch
            ↓
    learned representation
            ↓
    semantic component assignment

The semantic categories are already provided by the benchmark datasets.

Therefore, the model learns **where existing semantic categories occur** in
the structured sketch. It does not discover those semantic categories
itself.

The literature-review evidence indicates that the benchmark datasets provide
multiple semantic labels per category, establishing an existing semantic
vocabulary against which segmentation is evaluated.

### Key distinction

SketchGNN:

    existing semantic vocabulary
            ↓
    learn semantic segmentation

CLO-SKET:

    quantitative geometry
            ↓
    discover reproducible organization
            ↓
    investigate possible structural vocabulary

This difference is fundamental to the scientific questions of the two works.

---

## 3. Representation Hierarchy

SketchGNN explicitly maintains three levels of learned representation:

    point-level
          ↓
    stroke-level
          ↓
    sketch-level

This is important because it demonstrates that a sketch can be represented
through its structural organization rather than being treated only as a
conventional raster image.

However, this hierarchy has a different scientific role from the hierarchy
being investigated in CLO-SKET.

### SketchGNN

The hierarchy is a **neural feature hierarchy** designed to improve semantic
segmentation.

    point → stroke → sketch
              ↓
       learned features
              ↓
      semantic segmentation

### CLO-SKET

The intended hierarchy is a **scientific representation hierarchy**:

    geometry
        ↓
    quantitative organization
        ↓
    recurring structural regions
        ↓
    regional morphology
        ↓
    higher-order organization
        ↓
    possible semantic interpretation

These hierarchies should not be conflated.

---

## 4. Graph Representation

SketchGNN preserves relationships among sketch elements through a graph
representation.

The model uses point-level and stroke-level information and incorporates
graph convolution operations, including static and dynamic graph branches.

This provides important methodological evidence that:

> Relationships among sketch elements can contain information useful for
> computational sketch understanding.

This is highly relevant to CLO-SKET.

However, the purpose of the graph is different.

### SketchGNN

    graph structure
          ↓
    learned representation
          ↓
    supervised semantic segmentation

### CLO-SKET

    quantitative geometry
          ↓
    identify reproducible organization
          ↓
    characterize structural regions
          ↓
    investigate their morphology

SketchGNN therefore demonstrates the usefulness of relational sketch
structure, but does not establish a corpus-derived morphology vocabulary.

---

## 5. What SketchGNN Actually Learns

The quantitative results in SketchGNN establish that structured graph-based
representations can learn effective mappings from sketch representations to
semantic segmentation labels.

The supported scientific claim is approximately:

    structured sketch representation
                ↓
       semantic segmentation

It does **not** establish:

    raw sketch geometry
                ↓
       discovery of semantic vocabulary

These are different scientific problems.

---

## 6. Does SketchGNN Discover Semantic Components?

### No.

This point should remain explicit.

The semantic labels are provided by the benchmark datasets.

The model learns to assign those labels to parts of the sketch.

Therefore:

| Question | SketchGNN |
|---|---|
| Semantic labels provided? | Yes |
| Semantic segmentation? | Yes |
| Semantic vocabulary discovered? | No |
| Primitive vocabulary discovered? | No |
| Corpus-derived primitive discovery? | No |
| Quantitative morphology discovery? | No |

The model therefore performs **semantic assignment**, not **semantic
vocabulary discovery**.

---

## 7. Comparison with CLO-SKET

### SketchGNN

    structured sketch
            ↓
    graph representation
            ↓
    learned features
            ↓
    existing semantic labels
            ↓
    semantic segmentation

### CLO-SKET

    raw / quantitative sketch geometry
            ↓
    morphology measurements
            ↓
    reproducible organization
            ↓
    recurring structural regions
            ↓
    regional morphology
            ↓
    higher-order organization
            ↓
    semantic interpretation (future / open)

The critical difference is the **direction of construction**.

### SketchGNN

    semantics → structured representation → semantic localization

### CLO-SKET

    geometry → structural organization → possible semantic interpretation

---

## 8. What Overlaps with CLO-SKET?

There is substantial conceptual overlap in:

- structured sketch representation;
- point-level and stroke-level organization;
- relational modeling;
- graph-based representation;
- hierarchical treatment of sketch information;
- the recognition that relationships among sketch elements matter;
- extraction of meaningful information from sketch structure.

Therefore SketchGNN should be treated as an **important citation** in the
literature review.

We should not minimize its relevance.

---

## 9. What Does Not Overlap?

SketchGNN does not establish the specific CLO-SKET research procedure of:

- discovering recurring structural categories directly from geometry;
- constructing a corpus-derived structural vocabulary;
- characterizing that vocabulary independently of semantic labels;
- analyzing quantitative morphology of discovered structures;
- studying density-defined or morphology-defined regions;
- testing whether such organization is reproducible across the sketch corpus;
- constructing morphology profiles around discovered regions;
- studying context-dependent morphological variation;
- constructing a morphology grammar from those discovered structures.

Its central task is semantic segmentation using established dataset labels.

---

## 10. Geometry as Input vs. Geometry as Object of Analysis

This is one of the most important conceptual distinctions emerging from the
literature review.

### Conventional computational sketch understanding

Geometry is typically used as an **input to a downstream task**.

Examples include:

    geometry → semantic segmentation

    geometry → retrieval

    geometry → recognition

    geometry → reconstruction

The geometry is therefore instrumental to another objective.

### CLO-SKET

The geometry itself becomes the **object of scientific analysis**.

    geometry
        ↓
    quantitative measurement
        ↓
    organization
        ↓
    reproducibility

The question is not initially:

> What semantic label does this region have?

The question is:

> Does the measured morphology of the sketch population exhibit
> reproducible organization at all?

This distinction should be preserved in the final paper.

---

## 11. Important Reviewer Threat

### Could a reviewer say:

> "Semantic sketch decomposition already exists."

### Answer:

**Yes.**

We should explicitly acknowledge this.

SketchGNN is evidence that structured sketch representations can support
semantic decomposition when semantic categories are available.

### Could a reviewer say:

> "SketchGNN already discovers the CLO-SKET primitive vocabulary."

### Answer:

**No.**

SketchGNN assigns existing semantic labels. It does not derive a reusable
structural vocabulary from recurring quantitative geometry.

### Could a reviewer say:

> "SketchGNN therefore invalidates the geometry-first approach."

### Answer:

**No.**

The two studies operate at different points in the representational pipeline.

---

## 12. Stronger Novelty Boundary

The novelty claim should **not** be:

> "Previous sketch methods do not use structured representations."

That would be false.

Nor should it be:

> "Previous sketch methods do not use graphs."

That would also be false.

Nor should it be:

> "Previous sketch methods do not perform semantic decomposition."

SketchGNN directly demonstrates otherwise.

The defensible distinction is:

> **Previous work demonstrates that structured point-, stroke-, and
> graph-level sketch representations can support semantic interpretation
> when semantic categories are available. CLO-SKET instead investigates
> whether reproducible quantitative organization can be identified directly
> from sketch morphology before a semantic component vocabulary is imposed.**

This is the stronger and more scientifically precise formulation.

---

## 13. Quantitative Evidence in SketchGNN

SketchGNN provides quantitative comparisons across several sketch datasets,
including:

- Huang14;
- TU-Berlin;
- SPG.

The reported experiments examine architectural choices including:

- static vs. dynamic graph branches;
- stroke pooling;
- graph-network variants;
- number of GCN units;
- sample-point settings.

The results provide evidence that structured graph representations can improve
semantic sketch segmentation.

This evidence should be acknowledged rather than minimized.

However, the performance results establish effectiveness for the stated
segmentation task. They do not establish that the model has discovered an
independent morphology vocabulary.

---

## 14. Relationship to the CLO-SKET Research Ladder

The literature can now be viewed as a sequence of increasingly structured
representational questions.

### Paper 04

    sketch strokes
          ↓
    predefined generic primitives
          ↓
    primitive abstraction

### Paper 05 — SketchGNN

    structured sketch
          ↓
    graph representation
          ↓
    existing semantic vocabulary
          ↓
    semantic segmentation

### CLO-SKET

    quantitative sketch geometry
          ↓
    measurable morphology
          ↓
    reproducible organization
          ↓
    recurring structural regions
          ↓
    regional morphology
          ↓
    higher-order organization
          ↓
    semantic interpretation

The important gap is:

    quantitative geometry
            ↓
    discover reproducible structural organization
            ↓
    before semantic labels are imposed

Neither Paper 04 nor SketchGNN establishes this specific research step.

---

## 15. What SketchGNN Strengthens

SketchGNN actually strengthens one of the broader premises of CLO-SKET:

> Sketch structure contains information that can be computationally useful
> for semantic interpretation.

This is valuable because CLO-SKET does not need to argue that sketches are
structurally meaningless until our method discovers structure.

Instead, the more precise argument is:

> Existing work demonstrates that structured sketch representations are useful
> for semantic interpretation. CLO-SKET investigates the quantitative
> organization that precedes such semantic interpretation.

This is a substantially stronger scientific position.

---

## 16. What SketchGNN Does Not Answer

SketchGNN does not answer the following questions:

### Q1
Which geometric structures recur across a sketch corpus?

**Not established.**

### Q2
Can recurring structural units be discovered without semantic labels?

**Not established.**

### Q3
Does sketch morphology form reproducible quantitative regions?

**Not established.**

### Q4
Do those regions possess characteristic morphology profiles?

**Not established.**

### Q5
Does the observed organization survive appropriate null models?

**Not established.**

### Q6
Does the organization reproduce across parameter or density scales?

**Not established.**

### Q7
Do discovered quantitative structures correspond to human semantic
components?

**Not established.**

### Q8
Does a morphology grammar emerge from those structures?

**Not established.**

These remain open questions for CLO-SKET.

---

## 17. Important Conceptual Distinction

The central distinction should be stated as:

> **Semantic decomposition and structural discovery are not the same
> scientific problem.**

SketchGNN can answer:

> "Which existing semantic category does this part of the sketch belong to?"

CLO-SKET asks:

> "Before assigning semantic categories, what quantitative structures
> actually recur in the sketch population?"

That distinction should remain central to the literature review.

---

## 18. Recommended Paper I Language

I recommend using wording close to the following:

> Previous work has demonstrated that structured sketch representations,
> including point-, stroke-, and graph-level representations, can support
> effective semantic interpretation and segmentation when semantic categories
> are available. These studies establish the computational value of
> structured sketch geometry, but they generally begin with an existing
> semantic or task-specific vocabulary. The present study addresses a
> preceding quantitative question: whether sketch morphology itself exhibits
> reproducible organization that can be characterized before semantic
> categories are imposed.

This avoids overstating novelty while preserving the actual distinction of the
study.

---

## 19. Reviewer-Style Verdict

| Reviewer Question | Assessment |
|---|---|
| Is SketchGNN directly relevant? | **Yes — highly relevant** |
| Does it use structured sketch geometry? | **Yes** |
| Does it use graph structure? | **Yes** |
| Does it model point/stroke relationships? | **Yes** |
| Does it perform semantic segmentation? | **Yes** |
| Does it discover semantic categories? | **No** |
| Does it discover primitives? | **No** |
| Does it perform corpus-derived morphology discovery? | **No** |
| Does it establish quantitative morphology organization? | **No** |
| Does it establish a morphology grammar? | **No** |
| Does it challenge broad "structured sketches are unexplored" claims? | **Yes** |
| Does it invalidate CLO-SKET's geometry-first question? | **No** |
| Novelty threat | **🟡 Moderate conceptual relevance** |
| Importance to literature review | **High** |

---

## 20. Final One-Sentence Takeaway

> **SketchGNN demonstrates that structured point- and stroke-level sketch
> representations and their relationships can support strong semantic
> segmentation when semantic labels are provided, whereas CLO-SKET asks
> whether reproducible structural organization can first be derived from
> quantitative sketch morphology before semantic labeling is introduced.**

---

# Status

**Paper 05 — SketchGNN: ANALYSED AND FROZEN**

- Semantic labels: **established as dataset-provided**
- Point/stroke/sketch hierarchy: **understood**
- Graph representation: **understood**
- Static/dynamic graph modeling: **understood**
- Quantitative evidence: **acknowledged**
- Semantic segmentation vs. structural discovery: **distinguished**
- Geometry-as-input vs. geometry-as-object-of-analysis: **distinguished**
- Comparison with CLO-SKET: **locked**
- Reviewer threat: **assessed**
- Novelty boundary: **refined**
- Matrix entry: **frozen**

### Core distinction to carry forward

```text
SketchGNN

existing semantic vocabulary
            ↓
structured sketch
            ↓
semantic segmentation


CLO-SKET

quantitative sketch geometry
            ↓
reproducible morphology
            ↓
structural organization
            ↓
semantic interpretation