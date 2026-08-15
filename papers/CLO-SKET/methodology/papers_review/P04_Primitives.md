# Literature Review — Paper 04: Abstracting Sketches through Simple Primitives

## Citation

**Abstracting Sketches through Simple Primitives** (ECCV 2022).

---

## 1. Why we are reading this paper

This paper is a high-priority conceptual neighbor for Paper I because it
explicitly represents human sketches using drawing primitives.

It is therefore important to distinguish carefully between:

- **predefined primitive abstraction**, and
- **corpus-derived primitive discovery**.

The paper is also important because it demonstrates that a primitive-based
geometric representation can preserve useful semantic information for
downstream recognition and retrieval.

The key question for Paper I is therefore not whether primitives have been
used for sketches before.

They clearly have.

The question is:

> **How is the primitive vocabulary constructed?**

That distinction is central to the novelty boundary of Paper I.

---

## 2. Scientific problem addressed

The paper introduces a **Primitive-based Sketch Abstraction** task.

The proposed Primitive-Matching Network (PMN) takes human sketches and
replaces their individual strokes with simple shapes selected from a fixed
vocabulary of drawing primitives.

The resulting representation can then be communicated or compressed under
different information budgets while attempting to preserve the content and
semantic information of the original sketch.

Conceptually:

**human sketch → stroke representation → primitive matching → geometric
alignment → primitive abstraction → downstream recognition/retrieval**

The scientific objective is therefore:

> **Can a compact representation composed of simple geometric primitives
> preserve sufficient information from a human sketch for downstream
> recognition and retrieval?**

This is an abstraction/compression question rather than a primitive-discovery
question.

---

## 3. Input representation and stroke definition

The input sketches are represented as sequences of 2-D coordinates associated
with pen-state information.

A sketch can therefore be viewed as a sequence of strokes, where a stroke is
formed from a contiguous sequence of points produced during a drawing action.

Conceptually:

```text
sketch
   ↓
stroke 1
   ↓
(x1, y1), (x2, y2), ..., (xn, yn)

stroke 2
   ↓
(x1, y1), (x2, y2), ..., (xm, ym)

...The important methodological point is:

The individual stroke is already an input unit.

The PMN does not first discover a new stroke vocabulary from the sketch
corpus.

Instead, it operates on the observed stroke representation.

Therefore:

observed stroke
      ↓
learned representation
      ↓
primitive matching

rather than:

raw sketch corpus
      ↓
discover structural units
4. Primitive Vocabulary

The paper uses a fixed set of 7 drawing primitives.

The reported vocabulary contains generic geometric shapes including:

square
triangle
circle
horizontal line
curved line
U-shaped curve
L-shaped line

These are predefined generic geometric primitives.

The primitive vocabulary itself is therefore not discovered from the sketch
corpus.

Conceptually:

Paper 04


fixed primitive vocabulary
        ↓
learn stroke → primitive mapping

rather than:

Paper I


sketch corpus
        ↓
recurring geometric structure
        ↓
candidate structural vocabulary

This distinction must remain explicit in the Paper I manuscript.

5. What PMN Learns

Although the primitive vocabulary is fixed, PMN learns substantial
representation and matching structure.

The learned components include:

stroke representation,
primitive compatibility,
stroke-to-primitive association,
geometric alignment,
transformation parameters,
and reconstruction behavior.

Therefore the correct characterization is:

fixed primitive vocabulary + learned stroke-to-primitive matching +
learned geometric alignment

rather than:

learned primitive vocabulary

The model learns how to use the predefined vocabulary.

It does not learn what the primitive vocabulary should be.

6. Stroke Encoder

The PMN uses a 6-layer Transformer architecture as its encoder.

The input to the encoder is the sequence of 2-D coordinates representing a
stroke.

Conceptually:

stroke coordinates
        ↓
6-layer Transformer
        ↓
stroke embedding

The encoder therefore learns a representation of the stroke from its
coordinate sequence.

The paper also investigates positional embeddings for the ordering of
points. Adding positional embeddings did not improve performance, and the
coordinates themselves are therefore used as the point inputs.

The encoder should therefore be described as:

Transformer-based point-sequence encoding

and not as:

CNN encoding
RNN encoding

for PMN.

7. Stroke and Primitive Embeddings

The representation framework provides embeddings for observed strokes and
the predefined drawing primitives.

Conceptually:

observed stroke
       ↓
Transformer encoder
       ↓
stroke embedding




predefined primitive
       ↓
Transformer encoder
       ↓
primitive embedding

The learned embeddings provide a basis for estimating compatibility between
a stroke and candidate primitives.

The important distinction is:

The network learns the representation and matching relationship, while
the candidate primitive categories are already defined.

8. Primitive Compatibility

For an observed stroke s and candidate primitive p, PMN estimates their
compatibility.

Conceptually:

observed stroke
      ↓
stroke embedding
      ↓
compatibility with primitive 1
compatibility with primitive 2
...
compatibility with primitive 7
      ↓
primitive association

The compatibility formulation encourages geometrically compatible strokes
and primitives to have stronger associations.

This is a learned stroke-to-primitive matching problem.

It is not evidence that the primitive categories themselves were discovered
from the corpus.

9. Geometric Alignment

A primitive does not need to have the same orientation, scale, or spatial
configuration as the observed stroke.

PMN therefore learns a transformation that aligns a candidate primitive with
the target stroke.

Conceptually:

primitive
    ↓
learned transformation
    ↓
aligned primitive
    ↓
comparison with observed stroke

The learned transformation captures the geometric realization of a
predefined primitive.

Thus the model separates:

primitive identity
        +
geometric realization

This allows the same primitive type to represent different geometric
instances.

10. Distance-Transform Reconstruction

A central component of PMN is a distance-transform-based reconstruction
objective.

The observed stroke and transformed primitive are not required to contain
the same number of points.

Instead, their spatial structures are compared using a distance-transform
representation.

Conceptually:

observed stroke
       ↓
distance-transform representation
       │
       │ comparison
       ↓
transformed primitive
       ↓
distance-transform representation


       ↓


geometric reconstruction error

This allows the method to evaluate geometric similarity without requiring
direct point-to-point correspondence.

The objective therefore encourages the selected primitive, after geometric
alignment, to approximate the observed stroke.

11. What Is Predefined vs Learned?

The methodological separation can be summarized as follows.

Predefined
primitive categories
geometric identity of each primitive
number of primitive types
Learned
stroke embedding
primitive embedding
primitive compatibility
stroke-to-primitive association
geometric alignment
transformation parameters
representation used for reconstruction
Not learned
the primitive vocabulary itself

Therefore:

PREDEFINED
7 generic geometric primitives
        ↓
LEARNED
stroke representation
        ↓
LEARNED
primitive compatibility
        ↓
LEARNED
geometric alignment
        ↓
LEARNED
geometric reconstruction

This is the central methodological fact for comparison with Paper I.

12. Is PMN a Contrastive-Learning Method?

No.

PMN should not be described as a standard contrastive-learning framework.

Its principal objective is based on:

primitive compatibility
        +
geometric distance-transform reconstruction

The paper does use a contrastive objective in a separate downstream
fine-grained sketch-based image retrieval evaluation network.

Therefore the distinction is:

PMN
→ primitive matching + geometric reconstruction


FG-SBIR evaluation network
→ contrastive objective

The downstream contrastive objective should not be attributed to the PMN
training objective itself.

13. Information-Budget Formulation

A major component of the paper is the study of sketch abstraction under
different communication or information budgets.

The question is:

How much useful sketch information can be retained when the original
stroke representation is replaced by a compact primitive-based message?

Conceptually:

original stroke
    ↓
many coordinate points


versus


primitive message
    ↓
primitive identity
+
geometric transformation

The paper evaluates the ability of the primitive representation to preserve
useful information at different budgets.

This provides the main motivation for primitive-based sketch abstraction.

14. Semantic Information Preservation

It would be inaccurate to describe the seven primitives as having no
semantic relevance.

The paper evaluates the resulting primitive abstraction through downstream
tasks including:

sketch classification,
fine-grained sketch-based image retrieval.

At a 10% information budget, the reported classification accuracies include:

DSA   : 20.12%
GDSA  : 26.88%
SW    : 51.21%
PMN   : 67.08%

These results demonstrate that primitive-based abstraction can preserve
substantial information useful for downstream semantic recognition.

Therefore the correct interpretation is:

The primitive vocabulary is geometrically generic and predefined, while
semantic information preservation is demonstrated indirectly through
downstream classification and retrieval performance.

15. Semantic Preservation Is Not Semantic Discovery

This distinction is critical.

The paper demonstrates:

geometric primitive abstraction
        ↓
semantic information preserved

It does not establish:

sketch corpus
        ↓
discover semantic primitives

Therefore:

semantic information preservation
        ≠
semantic primitive discovery

A downstream classifier successfully using a primitive representation does not
by itself demonstrate that the primitive categories were independently
discovered semantic units.

This distinction should be preserved when citing the paper.

16. Primitive Usage and Category Association

The paper also examines primitive usage across object categories.

Different geometric primitives show different patterns of occurrence across
sketch categories.

This demonstrates that generic geometric primitives can carry information
associated with object structure and semantic recognition.

However, the direction of inference remains:

predefined primitive
        ↓
representation
        ↓
semantic information

rather than:

sketch corpus
        ↓
discover primitive
        ↓
discover semantic meaning

Thus the paper supports the usefulness of geometric abstraction without
establishing corpus-derived semantic primitive discovery.

17. Important Limitation of the Fixed Primitive Vocabulary

A single predefined primitive may not adequately represent every complex
human stroke.

Conceptually:

complex human stroke
        ↓
single simple primitive
        ↓
approximation error

The paper discusses future directions involving mechanisms such as splitting
or merging strokes and potentially learning the primitive set itself.

This limitation is important because it highlights the difference between:

representing strokes using a fixed vocabulary

and:

discovering the appropriate structural vocabulary itself

The latter remains outside the main PMN formulation studied in this paper.

18. Comparison With Paper I
Paper 04
predefined geometric vocabulary
        ↓
observed stroke representation
        ↓
learn stroke → primitive compatibility
        ↓
learn geometric alignment
        ↓
primitive abstraction
        ↓
semantic information preservation
        ↓
classification / retrieval
Paper I
fashion-sketch corpus
        ↓
explicit morphology representation
        ↓
quantitative morphology geometry
        ↓
recurring quantitative organization
        ↓
density-defined regional structure
        ↓
reproducible regional morphology profiles
        ↓
future semantic investigation

The direction of construction is therefore fundamentally different.

19. Central Distinction

The distinction should not be stated merely as:

"They use labels; we do not."

That is too weak and does not accurately describe the scientific difference.

The stronger distinction is:

Paper 04 begins with a predefined geometric primitive vocabulary and
learns how observed strokes map onto that vocabulary. Paper I investigates
whether reproducible quantitative morphological organization can be
characterized from garment-sketch geometry before semantic categories or
primitive meanings are imposed.

In short:

Paper 04


vocabulary
    ↓
representation learning
    ↓
matching
    ↓
abstraction

versus:

Paper I


geometry
    ↓
empirical organization
    ↓
recurring structure
    ↓
future semantic grounding
20. What Overlaps With Paper I?

There is meaningful conceptual overlap in:

geometric representation of sketches,
reduction of raw sketch complexity,
compact representation,
interpretable geometric structure,
and preservation of useful information through geometric abstraction.

Therefore Paper 04 is an important citation and a genuine conceptual
neighbor.

Paper I should explicitly acknowledge this prior work.

21. What Does Not Overlap?

Paper 04 does not establish the specific Paper I problem of:

discovering recurring morphology structures from garment sketches,
deriving a corpus-specific morphology vocabulary,
discovering density-organized morphology regions,
characterizing quantitative morphology profiles of those regions,
testing region–morphology association against size-preserving null models,
evaluating cross-scale reproducibility of those quantitative profiles,
or establishing a semantic interpretation of the discovered structures.

Its seven primitive categories are fixed generic drawing shapes.

Its main objective is abstraction and information preservation under
communication constraints.

22. Reviewer Attack
Reviewer claim

"Primitive-based sketch representation has already been studied."

Response

Yes.

This is a valid prior-art point and must be acknowledged.

Paper I should not claim novelty for the generic idea of representing sketches
using primitives.

Reviewer claim

"Therefore primitive discovery is already solved."

Response

No.

Paper 04 starts with a predefined primitive vocabulary and learns how to map
observed strokes onto that vocabulary.

It does not derive the vocabulary from the sketch corpus.

The distinction is:

Paper 04


fixed primitives
      ↓
learn matching




Paper I


fashion-sketch geometry
      ↓
discover / characterize recurring structure
Reviewer claim

"But their primitives preserve semantic information."

Response

Yes.

That result should be acknowledged.

However:

semantic information preservation
        ≠
semantic primitive discovery

Their results demonstrate that a predefined geometric vocabulary can preserve
useful information for recognition and retrieval.

They do not establish that the vocabulary itself was discovered as a set of
semantic morphology units.

23. Novelty Assessment

🟡 IMPORTANT CONCEPTUAL NEIGHBOR

The paper has meaningful conceptual overlap with Paper I because it studies
geometric sketch representation and primitive abstraction.

However, it is not a direct duplicate of the Paper I discovery problem.

The novelty boundary should therefore be placed on:

empirical characterization of reproducible quantitative morphology
organization in garment sketches before imposing semantic categories or
assigning semantic meaning to recurring structures.

Paper 04 should be cited explicitly when discussing prior work on geometric
primitive-based sketch representation.

24. Literature Matrix Entry
Field	Paper 04: Abstracting Sketches through Simple Primitives
Venue	ECCV 2022
Problem	Primitive-based sketch abstraction / compression
Input	Human sketches represented as stroke sequences
Stroke representation	2-D coordinate sequences with pen-state information
Encoder	6-layer Transformer
Primitive vocabulary	7 predefined geometric drawing primitives
Primitive discovery	No
Stroke-to-primitive mapping	Yes
Stroke embedding	Yes
Primitive embedding	Yes
Primitive compatibility	Yes
Geometric alignment	Yes
Transformation learning	Yes
Reconstruction	Yes
Main PMN objective	Distance-transform-based geometric reconstruction with primitive compatibility
Standard contrastive PMN loss	No
Contrastive objective elsewhere	Yes — downstream FG-SBIR evaluation
Information budget	Yes
Semantic information	Evaluated indirectly through downstream performance
Classification	Yes
Sketch-based retrieval	Yes
Main scientific goal	Compact / communicative sketch abstraction
Vocabulary supervision	Primitive set predefined
Corpus-derived vocabulary	No
Fashion-specific morphology discovery	No
Morphology-region discovery	No
Semantic primitive discovery	Not established
Morphology grammar	Not studied
Paper I overlap	Geometric sketch representation / primitive abstraction
Key difference	Fixed generic vocabulary vs empirical characterization of quantitative morphology organization
Reviewer threat	🟡 Moderate conceptual overlap
Importance to Paper I	High
25. One-Sentence Takeaway

Abstracting Sketches through Simple Primitives demonstrates that observed
sketch strokes can be mapped to a fixed vocabulary of simple geometric
primitives and geometrically aligned to produce compact representations that
preserve useful semantic information, whereas Paper I investigates whether
reproducible quantitative morphological organization can itself be
characterized from garment-sketch geometry before semantic categories or
primitive meanings are imposed.

26. Claim Boundary for Paper I

Paper 04 supports the following broad premise:

geometric sketch structure
        ↓
compact representation
        ↓
useful semantic information

It does not justify claiming that Paper I has already established:

recurring quantitative region
        ↓
semantic primitive

Therefore Paper I retains the following locked boundary:

Question	Paper I status
Are recurring quantitative structures present?	Supported by our evidence
Are they reproducible across our tested scales?	Supported by our evidence
Are they semantic primitives?	We don't know
Are they morphology categories?	We don't know
Is this a morphology grammar?	We don't know
Is it a mathematical manifold?	We do not establish it
Can they eventually be semantically grounded?	Future research question

Therefore:

quantitative morphology
        ↓
structured morphology geometry
        ↓
recurring quantitative organization
        ↓
        ───────────────
        semantic grounding
        ↓
candidate morphology primitives
        ↓
compositional relationships
        ↓
morphology grammar

Only the quantitative/structural portion is addressed by the present Paper I.

The semantic and compositional levels remain open scientific questions.

STATUS
🔒 PAPER 04 — ANALYSED AND FROZEN

Verified and locked:

 Scientific problem understood
 Stroke representation understood
 Stroke identification understood
 7 primitive vocabulary verified
 Primitive vocabulary is predefined
 Transformer encoder verified
 Stroke/primitive embedding mechanism understood
 Primitive compatibility understood
 Geometric alignment understood
 Distance-transform reconstruction understood
 PMN distinguished from downstream contrastive FG-SBIR evaluation
 Information-budget objective understood
 Semantic-information preservation distinguished from semantic discovery
 Fixed vocabulary vs corpus-derived discovery distinction locked
 Reviewer attack assessed
 Novelty boundary assessed
 Literature matrix entry frozen

Paper 04 is now frozen for the Literature ↔ Our Evidence matrix.

Next literature target: methods that learn or discover sketch components,
strokes, or structural units rather than mapping observed strokes to a fixed
generic primitive vocabulary.