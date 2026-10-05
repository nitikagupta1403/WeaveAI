# WeaveAI — Structured Sketch Understanding / Garment Language
## Conceptual Literature Synthesis — Freeze v0.1

**Status:** Conceptual literature checkpoint.  
**Scope:** primitive → relation → graph → grammar → program → probabilistic semantic understanding.  
**Boundary:** This is **not** a frozen WeaveAI architecture and does not establish novelty.

---

## 1. Core synthesis

Across sketch understanding, relational learning, graphical models, CAD structure, visual grammar, and program induction, a coherent representation hypothesis emerges:

\[
\boxed{
\text{signal}
\rightarrow
\text{geometric primitives}
\rightarrow
\text{relations}
\rightarrow
\text{graph}
\rightarrow
\text{grammar}
\rightarrow
\text{program}
\rightarrow
\text{probabilistic semantic understanding}
}
\]

For WeaveAI, probability may operate at several levels rather than only at the final classifier.

A shorter working statement is:

\[
\boxed{
\text{signal}
\rightarrow
\text{geometry}
\rightarrow
\text{structure}
\rightarrow
\text{probability}
\rightarrow
\text{semantics}
}
\]

---

## 2. Signal-level representation

Morphological Component Analysis (MCA) motivates treating a sketch as a superposition of structures with different morphologies rather than as one undifferentiated raster:

\[
x=\sum_k \Phi_k\alpha_k+\epsilon
\]

A probabilistic extension would infer:

\[
p(\alpha_1,\ldots,\alpha_K\mid x)
\]

rather than forcing an early hard decomposition.

**WeaveAI implication:** MCA/probabilistic sparse decomposition may provide cleaner or more interpretable evidence for later geometry extraction, but MCA itself does not provide garment semantics.

---

## 3. Primitive geometry as a sketch alphabet

Primitive-recognition work such as PaleoSketch and related early sketch-processing systems supports compact geometric vocabularies:

\[
\{\text{line},\text{arc},\text{circle},\text{ellipse},\text{curve},\text{polyline},\ldots\}
\]

This supports moving beyond pixels.

However:

\[
\boxed{\text{primitive geometry} \neq \text{semantic meaning}}
\]

The same primitive can play different semantic roles depending on position, neighbourhood, and context.

**Interpretation:** primitives may provide an **alphabet**, but not yet a garment language.

---

## 4. Context transforms primitives into components

Stroke-based sketch-segmentation literature shows that a stroke or stroke group can acquire different meanings depending on surrounding structure.

A better formulation is:

\[
\text{primitive}
+
\text{position}
+
\text{neighbourhood}
+
\text{relations}
\rightarrow
\text{semantic interpretation}
\]

This motivates explicit relational representations.

---

## 5. Graphs should represent structural relations, not merely similarity

SketchGraphs and related CAD work show the usefulness of representing geometric entities as nodes and constraints as edges.

The critical WeaveAI lesson is:

\[
\boxed{\text{similarity does not imply relation}}
\]

Two visually similar primitives may be unrelated, while two geometrically different primitives may be structurally connected.

A future relation model is therefore better expressed as:

\[
P(r_{ij}\mid v_i,v_j,g_{ij},C)
\]

where \(v_i,v_j\) are node representations, \(g_{ij}\) is pairwise geometry, \(C\) is broader context, and \(r_{ij}\) is a typed relation.

Candidate relation types remain hypotheses, not a frozen ontology:

\[
\{
\text{connected},
\text{symmetric},
\text{parallel},
\text{inside},
\text{continuation},
\text{terminates-at},
\text{bounds},
\text{none}
\}
\]

---

## 6. MIL becomes more useful when instances are relational

Zhou, Sun & Li (2009), *Multi-Instance Learning by Treating Instances As Non-I.I.D. Samples*, is especially relevant because it treats instances within a bag as inter-correlated components rather than independent samples.

For WeaveAI, a garment sketch may be represented as a bag of strokes/components, but those instances are structurally dependent.

The paper also provides a critical warning: incorrect structure can be worse than ignoring structure.

Therefore:

\[
\boxed{\text{graph quality must be earned before graph learning}}
\]

A GNN should not be introduced merely because a graph can be constructed.

---

## 7. MIL and graph reasoning solve different problems

MIL may help when supervision is available only at garment level while component labels are unknown:

\[
B=\{v_1,\ldots,v_n\}
\]

Graph reasoning instead asks how the instances are related.

Thus a future combination could be:

\[
\boxed{\text{graph-structured MIL}}
\]

with:

- MIL → weak supervision
- graph structure → relationships
- probabilistic inference → uncertainty

---

## 8. Latent relation inference

Neural Relational Inference provides a useful precedent in which edge type itself is latent:

\[
q_\phi(z_{ij}\mid X)
\]

For WeaveAI, the broader target may eventually be:

\[
P(R,Y\mid X)
\]

where:

- \(X\) = observed signal/geometric evidence
- \(R\) = latent typed relations
- \(Y\) = latent semantic node interpretations

This separates:

\[
\text{What is this node?}
\]

from:

\[
\text{How is it related to other nodes?}
\]

---

## 9. Probabilistic graphical reasoning

The HMM/CRF analogy is useful conceptually.

A CRF-like view asks:

\[
P(Y\mid X)
\]

where local evidence and pairwise compatibility jointly determine a structured interpretation.

For raw garment sketches, an even richer problem may be:

\[
P(Y,R\mid X)
\]

where both node states and relations can be uncertain.

---

## 10. Grammar describes valid compositions

Shape grammar, And–Or grammar, LADDER, SketchREAD, scene-graph, and related traditions support moving beyond isolated parts toward rules governing valid compositions.

A useful distinction is:

- **graph:** describes one structured instance
- **grammar:** describes allowable structures, alternatives, and compositions across instances

Potential garment-grammar concepts include hierarchy, optional components, alternatives, symmetry, repetition, and attachment patterns.

These must emerge from evidence rather than be invented prematurely.

---

## 11. Programs provide a stronger representation than static graphs

Graphics-program induction, Bayesian Program Learning, Vitruvion, and ShapeAssembly support representing structured objects through executable or program-like descriptions.

A graph may state:

\[
\text{sleeve attached-to bodice}
\]

while a program may represent:

\[
\text{create bodice}
\rightarrow
\text{attach sleeve under structural constraints}
\]

Programs can potentially encode hierarchy, repetition, symmetry, attachment, parameterization, and construction logic.

ShapeAssembly is especially useful conceptually because it makes the object feel like a constrained assembly system:

\[
\boxed{
\text{parts}
+
\text{attachment rules}
+
\text{hierarchy}
+
\text{constraints}
}
\]

This motivates a possible future **garment assembly language**.

---

## 12. Bayesian Program Learning and probabilistic programming

Bayesian Program Learning is closely aligned with the WeaveAI philosophy:

\[
P(H\mid E)\propto P(E\mid H)P(H)
\]

where \(H\) is a structured hypothesis/program and \(E\) is the observed drawing.

A useful conceptual definition is:

\[
\boxed{
\text{understanding}
=
\text{finding a plausible structured explanation for the observation}
}
\]

Probabilistic programming / analysis-by-synthesis extends this idea:

\[
\text{latent program}
\rightarrow
\text{generated observation}
\]

and inference runs backward:

\[
\text{observation}
\rightarrow
P(\text{latent program}\mid \text{observation})
\]

A long-term abstraction for WeaveAI could be:

\[
P(S,G,R,H\mid x)
\]

where:

- \(S\) = signal/morphological decomposition
- \(G\) = geometric primitive configuration
- \(R\) = relational structure
- \(H\) = garment structural/program hypothesis
- \(x\) = observed sketch

This is conceptual only, not yet an implementation specification.

---

## 13. Current WeaveAI representation hypothesis

\[
\boxed{
\text{raw sketch}
\rightarrow
\text{probabilistic signal evidence}
\rightarrow
\text{geometric primitives}
\rightarrow
\text{probabilistic typed relations}
\rightarrow
\text{graph}
\rightarrow
\text{grammar}
\rightarrow
\text{garment program}
\rightarrow
\text{semantic understanding}
}
\]

This is a **representation hypothesis**, not a frozen architecture.

---

## 14. Methodological boundary

The literature does **not** justify immediately building a model containing MCA + Bayesian inference + GNN + MIL + grammar + program synthesis.

The research sequence remains:

\[
\boxed{
\text{problem}
\rightarrow
\text{assumptions}
\rightarrow
\text{mathematics}
\rightarrow
\text{representation}
\rightarrow
\text{method}
\rightarrow
\text{experiment}
}
\]

Each layer must solve a demonstrated limitation of the previous one.

In particular:

\[
\boxed{
\text{earn the nodes}
\rightarrow
\text{earn the edges}
\rightarrow
\text{earn the graph}
\rightarrow
\text{then choose the learner}
}
\]

---

## 15. High-value research questions

1. What should constitute a node in a garment sketch: stroke, primitive, connected component, morphological component, or hierarchical combination?
2. Which node features can be derived reliably from MCA + geometry + uncertainty?
3. Which garment relations are recoverable from geometry alone?
4. Which relations require global context or probabilistic inference?
5. Can typed garment edges be inferred reliably with limited training data?
6. Does explicit relational structure improve learning over independent-instance representations?
7. Can garment-level labels support useful weak supervision through MIL?
8. At what point does a graph become insufficient and require grammar?
9. Can a garment grammar be partly learned rather than entirely hand-designed?
10. Can the final structure be represented as an interpretable garment program?

---

## 16. Frozen conceptual principles

\[
\boxed{
\textbf{When data is limited, encode what is already known structurally and learn only what remains uncertain.}
}
\]

\[
\boxed{
\textbf{Geometry supplies evidence; structure supplies constraints; probability manages uncertainty.}
}
\]

---

## 17. Freeze status

**Freeze as:** conceptual synthesis / literature checkpoint v0.1.

**Not frozen:**

- final architecture
- node definition
- edge ontology
- MCA dictionary selection
- Bayesian formulation
- MIL formulation
- GNN choice
- grammar
- garment DSL/program language
- novelty claim

These remain experimental and literature questions.
