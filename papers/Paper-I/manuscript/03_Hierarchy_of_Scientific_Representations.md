# Learning the Semantic Language of Fashion Sketches

---

# Section 3

# Hierarchy of Scientific Representations

---

## Document Information

| Field | Value |
|-------|-------|
| Paper | Learning the Semantic Language of Fashion Sketches |
| Section | 3 |
| Version | 1.0 (Working Draft) |
| Status | Under Development |
| Target Journal | Computers & Graphics |
| Last Updated | 10 August 2026 |

---

## Scientific Philosophy

The proposed framework is organized as a hierarchy of progressively richer scientific representations rather than as a sequence of computational algorithms. Each representation is introduced only when the preceding representation becomes insufficient to answer the next scientific question. Consequently, the methodology progresses through successive levels of abstraction while preserving explicit traceability to the original garment geometry.

---

## Version History

| Version | Date | Status | Description |
|----------|------|--------|-------------|
| 1.0 | 10 Aug 2026 | Working Draft | Canonical manuscript initialized |

---

# 3. Hierarchy of Scientific Representations

## 3.0 Overview

The proposed framework progressively transforms raw garment sketches into increasingly expressive computational representations. Rather than describing a sequence of computational algorithms, the framework is organized as a hierarchy of scientific representations, where each representation addresses a distinct scientific question while preserving the evidence established at the preceding level.

Beginning with localized contour geometry, the framework successively learns reusable geometry primitives, symbolic garment representations, learned sequential organization, visual grammar, primitive morphology, semantic representations, knowledge graph organization, and finally semantic reasoning. Each representation extends the descriptive capability of the previous representation without redefining or replacing it, thereby providing complete traceability from high-level semantic reasoning back to the original garment geometry.

Figure 3.1 illustrates the hierarchy of scientific representations proposed in this work.


## Representation Hierarchy

| Representation | Scientific Question |
|---------------|---------------------|
| Geometry Event | Where do meaningful geometric changes occur? |
| Geometry Primitive | Which geometric changes recur? |
| Primitive Vocabulary | What reusable geometric units exist? |
| Garment Sentence | How is an individual garment represented symbolically? |
| Learned Sequential Organization | How are geometry primitives sequentially organized? |
| Visual Grammar | What recurring organizational structure exists across the sketch corpus? |
| Primitive Prototype | What represents the characteristic geometry of a primitive? |
| Primitive Morphology | How does a primitive vary geometrically? |
| Context-dependent Primitive Morphology | How is morphology associated with grammatical context? |
| Semantic Representation | What structural meaning emerges from geometry and grammar? |
| Knowledge Graph Representation | How are semantic representations organized? |
| Semantic Reasoning | What higher-order knowledge can be inferred? |

## Notation

| Symbol | Description |
|--------|-------------|
| \(G\) | Garment sketch |
| \(C\) | Garment contour |
| \(E\) | Geometry event |
| \(P\) | Geometry primitive |
| \(\mathcal{V}\) | Primitive vocabulary |
| \(\mathcal{S}\) | Garment sentence |
| \(\mathcal{R}\) | Learned sequential organization |
| \(\mathcal{G}\) | Visual grammar |
| \(\Pi\) | Primitive prototype |
| \(\mathcal{M}\) | Primitive morphology |
| \(\Sigma\) | Semantic representation |
| \(\mathcal{K}\) | Knowledge graph |
| \(\Omega\) | Semantic reasoning operator |

---

## 3.1 Geometry-Derived Primitive Representation

### 3.1.1 Scientific Motivation

Fashion sketches are traditionally interpreted through predefined semantic garment components such as collars, sleeves, necklines, cuffs, and hems. These semantic representations provide meaningful descriptions of garment structure; however, they implicitly assume that the underlying garment semantics are known *a priori*. Consequently, they do not address a more fundamental question: **does the sketch itself contain an intrinsic geometric organization from which higher-level structural representations can be learned?**

The proposed framework begins by investigating garment sketches at the level of geometry rather than semantics. Instead of interpreting a sketch through predefined garment-part labels, the garment contour is viewed as a continuous geometric signal whose localized geometric variations may reveal recurring structural patterns. If such recurring geometric structures exist consistently across a sketch corpus, they may serve as reusable computational building blocks for representing garment sketches independent of predefined semantic knowledge.

The objective of this stage is therefore to determine whether continuous garment contours can be decomposed into reusable computational units that preserve recurring geometric organization while remaining independent of predefined garment semantics. Establishing such units provides the geometric foundation upon which all subsequent representations proposed in this work are constructed.

Accordingly, the first research question addressed in this section is:

> **Can continuous garment sketches be discretized into reusable computational units that preserve recurring geometric organization while remaining independent of predefined garment semantics?**

---

**Development Status:** 🔒 Locked

**Manuscript Version:** 1.0

**Reviewed:** 10 August 2026


### 3.1.2 Definition 1 (Geometry Event)

#### Scientific Motivation

Continuous garment contours encode geometric information as uninterrupted sequences of contour points. However, not every location along a contour contributes equally to its structural organization. While many contour points simply preserve geometric continuity, others correspond to localized changes in geometric behavior that distinguish one structural region of the contour from another. Identifying these meaningful geometric transitions is essential for transforming a continuous contour into a computational representation capable of supporting higher-level structural analysis.

Rather than treating every contour point as an independent computational entity, the proposed framework interprets garment contours as ordered sequences of localized geometric events. These events represent observable transitions in contour geometry and provide the first level of abstraction above raw contour coordinates. By identifying only those locations where meaningful geometric behavior changes, the framework establishes a stable and compact representation from which reusable geometric structures can subsequently be learned.

Accordingly, the first computational representation introduced in the proposed hierarchy is the **Geometry Event**.

#### Definition 1 (Geometry Event)

A **Geometry Event** is defined as a localized and computationally identifiable transition in the geometric behavior of a continuous garment contour that partitions the contour into adjacent regions exhibiting distinct geometric characteristics.

Unlike semantic garment components, geometry events are purely geometric entities. They are determined solely by the local organization of the garment contour and remain independent of predefined garment-part labels. Geometry events therefore represent elementary observations of geometric change rather than complete structural components.

Formally, let

$$
C=\{c_1,c_2,\ldots,c_n\}
$$

denote the ordered sequence of contour points representing a garment sketch.

Let

$$
G(c_i)
$$

denote the local geometric descriptor evaluated at contour point \(c_i\).

A geometry event is identified through the mapping

$$
E_i=\Phi(G(c_i)),
$$

where

- \(E_i\) denotes the geometry event associated with contour location \(c_i\),
- \(G(\cdot)\) represents the local geometric descriptor, and
- \(\Phi(\cdot)\) denotes the event identification operator that determines whether the observed geometric behavior satisfies the criteria required to constitute a geometry event.

#### Scientific Interpretation

A geometry event represents an elementary observation of geometric change rather than an isolated contour point. Multiple contour points may collectively describe a single geometric event, while neighboring events together characterize the structural organization of a garment contour. Consequently, geometry events should be interpreted as computational observations of localized geometric behavior rather than discrete geometric objects.

Geometry events constitute the first computational representation learned directly from garment geometry. By identifying where meaningful geometric transitions occur, they provide the observational foundation from which higher-level geometric primitives are subsequently discovered.

Although geometry events identify locations of meaningful geometric change, individual events remain localized observations and do not yet constitute reusable structural units. The next stage therefore investigates whether recurring geometry events observed across multiple garment sketches can be organized into a finite set of reusable **geometry primitives**, thereby establishing the first reusable representation within the proposed hierarchy.

### 3.1.3 Definition 2 (Geometry Primitive)

#### Scientific Motivation

Individual geometry events identify localized transitions in garment contour geometry. Although these events provide meaningful observations of geometric change, they remain isolated and highly localized. Consequently, they cannot by themselves represent the recurring structural organization observed across multiple garment sketches.

The proposed framework therefore investigates whether geometry events exhibiting similar geometric behavior repeatedly occur throughout a sketch corpus. If such recurring observations exist, they may be consolidated into reusable computational entities that capture stable geometric characteristics independent of any individual garment sketch.

Rather than treating every geometry event as unique, the proposed framework groups geometrically similar events into a finite collection of reusable representations referred to as **geometry primitives**. Geometry primitives therefore constitute the first reusable geometric vocabulary learned directly from garment contours.

#### Definition 2 (Geometry Primitive)

A **Geometry Primitive** is defined as a reusable computational representation that summarizes a class of geometrically similar geometry events recurring across one or more garment sketches.

Unlike individual geometry events, which represent localized observations of geometric change, geometry primitives capture stable geometric structures that repeatedly occur within the learned geometric organization of the sketch corpus. Consequently, geometry primitives represent reusable structural units rather than individual geometric observations.

Let

$$
\mathcal{E}
=
\{E_1,E_2,\ldots,E_m\}
$$

denote the set of geometry events extracted from a garment sketch corpus.

A geometry primitive

$$
P_k
$$

is obtained by grouping geometry events exhibiting similar geometric characteristics,

$$
P_k
=
\Psi(\mathcal{E}_k),
$$

where

- \(\mathcal{E}_k\subseteq\mathcal{E}\) denotes the subset of geometrically similar geometry events, and
- \(\Psi(\cdot)\) denotes the primitive learning operator that constructs a reusable geometry primitive from recurring geometry events.

#### Scientific Interpretation

A geometry primitive should not be interpreted as a single contour segment or an individual geometric observation. Instead, it represents the characteristic geometric behavior shared by multiple geometry events recurring throughout the sketch corpus.

By consolidating recurring geometric observations into reusable structural units, geometry primitives transform continuous garment geometry into a finite computational vocabulary. This vocabulary provides the first reusable representation capable of describing garment sketches independently of individual contour instances.

Although geometry primitives establish a reusable geometric vocabulary, they remain independent computational entities. A garment sketch cannot yet be represented solely as an unordered collection of primitives because the sequential arrangement of primitives also contributes to garment structure. The next stage therefore investigates how geometry primitives can be organized into ordered symbolic representations capable of describing complete garment sketches.

### 3.1.3 Definition 2 (Geometry Primitive)

#### Scientific Motivation

Geometry events identify localized transitions in garment contour geometry and provide elementary observations of geometric change. Although these observations preserve meaningful local geometric behavior, they remain specific to individual contour locations and therefore cannot directly characterize the recurring structural organization shared across multiple garment sketches.

The proposed framework therefore investigates whether geometrically similar geometry events repeatedly occur throughout a sketch corpus. If such recurring observations exist, they may be consolidated into reusable computational representations that capture stable geometric characteristics independent of any individual garment sketch.

Rather than treating every geometry event as a unique observation, the proposed framework groups recurring geometry events exhibiting similar geometric behavior into reusable structural representations referred to as **geometry primitives**. Geometry primitives therefore establish the first reusable geometric vocabulary learned directly from garment contours.

#### Definition 2 (Geometry Primitive)

A **Geometry Primitive** is defined as a reusable computational representation that summarizes a class of geometrically similar geometry events recurring across one or more garment sketches.

Unlike geometry events, which represent localized observations of geometric change, geometry primitives capture stable geometric structures that repeatedly emerge throughout the sketch corpus. Consequently, geometry primitives represent reusable structural units rather than individual geometric observations.

Formally, let

$$
\mathcal{E}
=
\{E_1,E_2,\ldots,E_m\}
$$

denote the set of geometry events extracted from a garment sketch corpus.

A geometry primitive

$$
P_k
$$

is obtained by grouping geometry events exhibiting similar geometric characteristics,

$$
P_k
=
\Psi(\mathcal{E}_k),
$$

where

- \(\mathcal{E}_k \subseteq \mathcal{E}\) denotes the subset of geometrically similar geometry events, and
- \(\Psi(\cdot)\) denotes the primitive learning operator that constructs a reusable geometry primitive from recurring geometry events.

#### Scientific Interpretation

A geometry primitive should not be interpreted as a single contour segment or an individual geometric observation. Instead, it represents the characteristic geometric behavior shared by multiple recurring geometry events distributed throughout the sketch corpus.

By consolidating recurring geometric observations into reusable structural units, geometry primitives establish the first finite computational vocabulary learned directly from continuous garment geometry. This vocabulary forms the representational foundation upon which symbolic garment descriptions, visual grammar, and higher-level semantic representations are subsequently constructed.

Although geometry primitives establish a reusable geometric vocabulary, they remain independent computational entities. A complete garment sketch cannot yet be represented as an unordered collection of primitives because the sequential arrangement of primitives also contributes to garment structure. The next stage therefore introduces a symbolic representation capable of organizing geometry primitives into complete garment descriptions.

### 3.1.4 Primitive Vocabulary

#### Scientific Motivation

Individual geometry primitives provide reusable representations of recurring geometric structures. However, considered independently, they remain isolated computational entities and therefore cannot support consistent symbolic descriptions of garment sketches. A computational language requires not only reusable structural units but also a finite vocabulary that assigns a unique symbolic identity to each reusable unit.

The proposed framework therefore organizes all learned geometry primitives into a finite primitive vocabulary. Rather than treating each primitive as an independent geometric object, the vocabulary establishes a standardized symbolic representation that enables geometry primitives to be referenced consistently across all garment sketches.

The primitive vocabulary therefore provides the first symbolic layer of the proposed framework, transforming reusable geometric structures into discrete computational symbols suitable for higher-level structural analysis.

### 3.1.4 Geometric Primitive Vocabulary

A ** Geometric Primitive Vocabulary** is defined as the finite set of all reusable geometry primitives learned from a garment sketch corpus.

Each geometry primitive is assigned a unique symbolic identifier within the vocabulary, allowing recurring geometric structures to be represented consistently across different garment sketches. Consequently, the primitive vocabulary establishes a common symbolic language through which garment geometry can subsequently be described.

Formally, let

$$
\mathcal{P}
=
\{P_1,P_2,\ldots,P_K\}
$$

denote the complete set of learned geometry primitives.

The primitive vocabulary is therefore defined as

$$
\mathcal{V}
=
\{v_1,v_2,\ldots,v_K\},
$$

where each symbol

$$
v_k
$$

corresponds uniquely to geometry primitive

$$
P_k.
$$

Accordingly,

$$
v_k
\longleftrightarrow
P_k,
\qquad
k=1,\ldots,K.
$$

The vocabulary therefore establishes a one-to-one correspondence between symbolic identifiers and reusable geometry primitives.

#### Scientific Interpretation

The primitive vocabulary represents the first symbolic representation introduced within the proposed hierarchy. While geometry primitives capture recurring geometric structures, the vocabulary provides the symbolic abstraction required for describing complete garment sketches.

Importantly, the vocabulary itself contains no sequential or semantic information. It specifies only the available symbolic units from which higher-level structural representations can subsequently be constructed. As a result, the primitive vocabulary serves as the computational alphabet of the proposed geometric language.

Although the primitive vocabulary defines the available symbolic units, it does not specify how these symbols are organized within an individual garment sketch. Describing a complete garment therefore requires an ordered symbolic representation that preserves the sequential arrangement of geometry primitives along the garment contour. The next stage consequently introduces the **Garment Sentence**, which represents each garment sketch as an ordered sequence of primitive vocabulary symbols.

## 3.2 Garment Sentence Representation

### 3.2.1 Scientific Motivation

The Geometric Primitive Vocabulary establishes the finite set of reusable geometric symbols available for describing garment sketches. However, a vocabulary alone does not constitute a complete representation because it specifies only the available symbols without describing how they are organized within an individual garment sketch.

A garment sketch is fundamentally characterized not only by the geometry primitives it contains but also by the sequential arrangement of those primitives along the garment contour. Consequently, representing a garment as an unordered collection of primitives would discard the structural relationships that distinguish one garment from another.

The proposed framework therefore introduces the **Garment Sentence**, an ordered symbolic representation that preserves the sequential organization of geometry primitives observed along the garment contour. Analogous to a sentence in natural language, the garment sentence is not intended to imply linguistic meaning but rather to represent an ordered sequence of reusable geometric symbols that collectively describe the structural organization of an individual garment sketch.

The Garment Sentence therefore constitutes the first complete symbolic representation of an individual garment within the proposed hierarchy.

### 3.2.2 Definition 4 (Garment Sentence)

#### Definition

A **Garment Sentence** is defined as an ordered symbolic sequence of geometric primitive vocabulary symbols describing the structural organization of an individual garment sketch.

Unlike the Geometric Primitive Vocabulary, which defines only the available reusable geometric symbols, the garment sentence preserves the sequential organization of those symbols as they occur along the garment contour. Consequently, the garment sentence provides the first complete, geometry-derived symbolic representation of an individual garment sketch while maintaining explicit traceability to its underlying geometric organization.

Formally, let

$$
\mathcal{V}
=
\{v_1,v_2,\ldots,v_K\}
$$

denote the Geometric Primitive Vocabulary.

A garment sentence is represented as the ordered sequence

$$
S
=
(s_1,s_2,\ldots,s_n),
$$

where

$$
s_i \in \mathcal{V},
\qquad
i=1,\ldots,n.
$$

Each symbol \(s_i\) denotes the geometric primitive observed at the corresponding position along the garment contour. The ordering of symbols preserves the sequential organization of the garment and therefore represents both the structural composition and the relative arrangement of geometry primitives.

#### Scientific Interpretation

The garment sentence constitutes the first complete, geometry-derived symbolic representation of an individual garment sketch within the proposed representation hierarchy. Unlike raw contour geometry, the garment sentence abstracts continuous geometric information into an ordered sequence of reusable symbolic units while preserving the structural organization of the original garment.

Importantly, a garment sentence remains purely descriptive. It specifies which geometry primitives occur and the order in which they appear, but it does not yet characterize the statistical regularities shared across multiple garment sketches. Consequently, the garment sentence provides the symbolic foundation upon which corpus-level structural representations can subsequently be learned.

An individual garment sentence provides a complete symbolic representation of a single garment sketch. However, meaningful structural regularities do not emerge from an individual garment alone. Instead, they become observable only when garment sentences are analyzed collectively across a sketch corpus. The next stage therefore investigates the statistical organization of geometry primitives across multiple garment sentences, leading to the representation referred to as the **Learned Sequential Organization**.

### 3.2.2 Definition 4 (Garment Sentence)

#### Definition

A **Garment Sentence** is defined as an ordered symbolic sequence of Geometric Primitive Vocabulary symbols that describes the structural organization of an individual garment sketch.

Unlike the Geometric Primitive Vocabulary, which specifies only the available reusable geometric symbols, a garment sentence preserves the sequential arrangement of those symbols as they occur along the garment contour. Consequently, the garment sentence provides the first complete symbolic representation of an individual garment while maintaining explicit traceability to its underlying geometric organization.

#### Mathematical Representation

Formally, let

$$
\mathcal{V}
=
\{v_1,v_2,\ldots,v_K\}
$$

denote the Geometric Primitive Vocabulary.

A garment sentence is represented as the ordered symbolic sequence

$$
S
=
(s_1,s_2,\ldots,s_n),
$$

where

$$
s_i \in \mathcal{V},
\qquad
i=1,\ldots,n.
$$

Each symbol \(s_i\) represents the geometry primitive observed at the corresponding position along the garment contour. The ordering of symbols preserves the sequential organization of the garment contour and therefore captures both the structural composition and the relative arrangement of recurring geometric primitives.

#### Scientific Interpretation

The garment sentence constitutes the first complete symbolic representation of an individual garment sketch within the proposed representation hierarchy. By transforming continuous garment geometry into an ordered sequence of reusable geometric symbols, the garment sentence preserves the structural organization of the original contour while providing a compact symbolic representation suitable for subsequent statistical and semantic analysis.

Importantly, the garment sentence remains a descriptive representation rather than a statistical or semantic model. It specifies which geometry primitives occur and the order in which they appear within an individual garment, but it does not yet characterize the structural regularities shared across multiple garment sketches. Consequently, the garment sentence provides the symbolic foundation upon which corpus-level structural organization can subsequently be learned.

Although a garment sentence provides a complete symbolic representation of an individual garment sketch, it does not by itself reveal the recurring structural organization shared across a garment sketch corpus. Such organization emerges only when multiple garment sentences are analyzed collectively.

By examining the statistical relationships among geometry primitives across a collection of garment sentences, it becomes possible to identify recurring sequential patterns that characterize the structural organization of garment sketches. The next stage therefore introduces the **Learned Sequential Organization**, which models these corpus-level sequential relationships.

# 3.3 Learned Sequential Organization

## 3.3.1 Scientific Motivation

A garment sentence provides a complete, geometry-derived symbolic representation of an individual garment sketch. However, considered independently, a single garment sentence cannot reveal the structural regularities that characterize an entire garment sketch corpus. Such regularities emerge only when multiple garment sentences are analyzed collectively.

Within a garment sketch corpus, geometry primitives do not occur randomly. Instead, certain primitives consistently precede, follow, or co-occur with other primitives, giving rise to recurring patterns of sequential organization. These statistical regularities reflect the underlying structural organization shared across garment sketches rather than the characteristics of any individual garment.

The proposed framework therefore investigates the sequential relationships among geometry primitives across an entire sketch corpus. Rather than analyzing garment sentences independently, all garment sentences are collectively examined to identify recurring sequential patterns that remain consistent across multiple garments.

The resulting representation is referred to as the **Learned Sequential Organization**, as it captures the statistically learned organization of geometry primitives emerging directly from the garment sketch corpus.

### 3.3.2 Statistical Representation

The Learned Sequential Organization is derived by collectively analyzing the sequential arrangement of geometry primitives across all garment sentences within the sketch corpus. Rather than considering geometry primitives in isolation, the proposed framework estimates how frequently one geometry primitive is followed by another throughout the observed garment sentences.

Each garment sentence contributes evidence regarding the sequential relationships between neighboring geometry primitives. By aggregating these observations across the complete sketch corpus, recurring sequential transitions become statistically observable. These aggregated transition statistics characterize the structural organization shared across multiple garment sketches rather than the structural properties of any individual garment.

Let

$$
\mathcal{S}
=
\{S_1,S_2,\ldots,S_N\}
$$

denote the collection of garment sentences extracted from the sketch corpus.

For every pair of consecutive geometry primitives

$$
(v_i,v_j),
$$

the observed transition frequency is computed as

$$
f(v_i,v_j),
$$

representing the number of times geometry primitive \(v_j\) immediately follows geometry primitive \(v_i\) throughout the corpus.

Collectively, these transition frequencies constitute the statistical representation of the Learned Sequential Organization. At this stage, the representation captures only the observed sequential evidence present within the garment sketch corpus and does not yet impose any graph-theoretic or probabilistic assumptions.

#### Scientific Interpretation

The statistical representation provides the first corpus-level description of garment structure within the proposed framework. Unlike individual garment sentences, which describe single garment sketches, the aggregated transition statistics reveal recurring sequential organization shared across the entire sketch corpus.

Importantly, this representation remains purely observational. It summarizes empirical evidence extracted from the garment corpus without introducing additional modeling assumptions. Consequently, every subsequent representation—including graph-based organization and probabilistic modeling—is constructed directly from statistically observed sequential relationships.

Although the statistical representation captures recurring sequential relationships between geometry primitives, these relationships remain expressed as independent transition frequencies. A more expressive representation is required to describe the global structural organization emerging from these interconnected relationships.

The next stage therefore organizes the learned sequential relationships into a weighted directed graph, providing a unified representation of the Learned Sequential Organization.

### 3.3.3 Graph Representation

The statistical representation characterizes the frequency with which geometry primitives occur sequentially throughout the garment sketch corpus. Although these transition frequencies quantify pairwise sequential relationships, they remain distributed across individual observations and therefore do not explicitly represent the global organization of the learned sequential structure.

A more expressive representation is therefore required to integrate all observed sequential relationships into a unified computational framework. Since each transition frequency describes a directed relationship between two geometry primitives, the complete collection of observed transitions naturally forms a weighted directed graph.

Formally, the Learned Sequential Organization is represented as

$$
\mathcal{R}
=
(\mathcal{N},\mathcal{E},\mathcal{W}),
$$

where

- \(\mathcal{N}\) denotes the set of nodes corresponding to the Geometric Primitive Vocabulary,
- \(\mathcal{E}\) denotes the set of directed edges representing observed sequential transitions between geometry primitives, and
- \(\mathcal{W}\) denotes the edge weights corresponding to the observed transition frequencies.

Each directed edge

$$
(v_i,v_j)\in\mathcal{E}
$$

indicates that geometry primitive \(v_j\) has been observed immediately following geometry primitive \(v_i\) within one or more garment sentences. The corresponding edge weight

$$
w_{ij}
=
f(v_i,v_j)
$$

records the frequency with which this sequential transition occurs throughout the garment sketch corpus.

#### Scientific Interpretation

Representing the Learned Sequential Organization as a weighted directed graph unifies all observed sequential relationships within a single computational representation. Unlike the statistical representation, which treats transition frequencies as independent observations, the graph explicitly captures the interconnected organization of geometry primitives across the entire sketch corpus.

Importantly, the graph remains an observational representation. Edge weights correspond directly to empirically observed transition frequencies and therefore preserve explicit traceability to the underlying garment sentences. At this stage, no probabilistic assumptions have yet been introduced; the graph represents only the structural organization learned from the observed sequential evidence.

Although the weighted directed graph captures the global organization of sequential relationships, the edge weights remain expressed as absolute transition frequencies. Direct comparison of sequential relationships therefore remains dependent upon the number of observations contributing to each transition.

A normalized representation is consequently required to estimate the relative strength of sequential relationships independently of their absolute occurrence frequencies. The first-order Markov representation is therefore not introduced as an independent modelling assumption, but emerges naturally from the requirement to estimate the statistical strength of sequential relationships within the learned sequential organization.

### 3.3.4 First-Order Markov Representation

#### Scientific Motivation

The weighted directed graph represents the Learned Sequential Organization through observed transition frequencies between geometry primitives. Although these frequencies quantify how often individual sequential transitions occur, they remain dependent upon the number of observations contributing to each transition. Consequently, absolute transition frequencies cannot directly quantify the relative strength of sequential relationships within the learned sequential organization.

A normalized representation is therefore required to estimate the likelihood of transitioning from one geometry primitive to another independently of the total number of observations associated with each primitive. Such normalization converts empirical transition frequencies into conditional transition probabilities while preserving the sequential organization learned from the garment sketch corpus.

Accordingly, the proposed framework introduces a first-order Markov representation as a probabilistic interpretation of the observed sequential relationships.

#### Mathematical Representation

Let

$$
w_{ij}
$$

denote the observed transition frequency associated with the directed edge from geometry primitive

$$
v_i
$$

to geometry primitive

$$
v_j.
$$

The corresponding transition probability is computed as

$$
P(v_j \mid v_i)
=
\frac{w_{ij}}
{\sum_{k} w_{ik}},
$$

where

$$
\sum_{k} w_{ik}
$$

denotes the total number of outgoing transitions originating from geometry primitive

$$
v_i.
$$

The resulting transition probabilities satisfy

$$
\sum_j P(v_j \mid v_i)=1,
$$

thereby defining a first-order Markov representation of the learned sequential organization.

#### Scientific Interpretation

The first-order Markov representation does not introduce additional structural information beyond the weighted directed graph. Instead, it provides a normalized probabilistic interpretation of the sequential relationships already observed within the garment sketch corpus.

Consequently, transition probabilities quantify the relative strength of sequential relationships independently of the absolute frequency with which individual geometry primitives occur. This probabilistic representation therefore provides a statistically comparable description of sequential organization while remaining directly traceable to the observed transition frequencies.

Although the first-order Markov representation quantifies the probabilistic strength of individual sequential relationships, it remains fundamentally local because each transition is evaluated independently of the broader organization of the learned sequential structure. A higher-level representation is therefore required to characterize the global structural organization emerging from these probabilistic relationships.

The next stage consequently investigates the structural properties of the Learned Sequential Organization as a whole, leading to the representation referred to as the **Visual Grammar**.

## 3.4 Visual Grammar

### 3.4.1 Scientific Motivation

The first-order Markov representation quantifies the probabilistic strength of sequential relationships between neighboring geometry primitives. Although these local transition probabilities describe how individual geometry primitives are connected, they remain insufficient for characterizing the higher-order structural organization shared across the garment sketch corpus.

Garment sketches exhibit organization that extends beyond isolated pairwise transitions. Groups of geometry primitives repeatedly participate in larger structural arrangements that collectively describe characteristic garment configurations. These recurring organizational patterns cannot be fully understood by examining individual transition probabilities independently.

The proposed framework therefore investigates the global structural organization emerging from the complete Learned Sequential Organization. Rather than interpreting sequential relationships as isolated probabilistic transitions, the framework analyzes how these relationships collectively organize into recurring structural patterns distributed throughout the garment sketch corpus.

The resulting representation is referred to as the **Visual Grammar**, as it captures the recurring structural organization governing the sequential arrangement of geometry primitives learned directly from garment sketches.

### 3.4.2 Definition 5 (Visual Grammar)

#### Definition

A **Visual Grammar** is defined as the global structural organization emerging from the statistically learned sequential relationships among geometry primitives within a garment sketch corpus.

Unlike the Learned Sequential Organization, which represents observed sequential relationships between geometry primitives, the Visual Grammar characterizes the higher-order structural organization arising from the collective interaction of these relationships. Consequently, the Visual Grammar describes the recurring organizational principles governing the composition of garment sketches rather than individual sequential transitions.

#### Mathematical Representation

Let

$$
\mathcal{R}
=
(\mathcal{N},\mathcal{E},\mathcal{W})
$$

denote the Learned Sequential Organization.

The corresponding Visual Grammar is represented as

$$
\mathcal{G}
=
\Gamma(\mathcal{R}),
$$

where

- \(\mathcal{G}\) denotes the learned Visual Grammar, and
- \(\Gamma(\cdot)\) represents the grammar extraction operator that identifies the higher-order structural organization emerging from the complete Learned Sequential Organization.

Unlike the Learned Sequential Organization, which preserves individual sequential relationships, the Visual Grammar represents the global structural organization collectively exhibited by those relationships.

#### Scientific Interpretation

The Visual Grammar represents the first representation within the proposed hierarchy that captures organization extending beyond individual garment sketches. Rather than describing isolated geometry primitives or pairwise sequential relationships, it characterizes the recurring structural principles that consistently govern the organization of garment sketches throughout the corpus.

Importantly, the Visual Grammar is not manually specified through predefined design rules or garment-part annotations. Instead, it emerges directly from the statistically learned sequential organization of geometry primitives. Consequently, the Visual Grammar provides an interpretable structural representation linking low-level geometric observations to higher-level semantic organization.

Although the Visual Grammar represents the global structural organization of garment sketches, understanding its organization requires quantitative characterization of its structural properties. Graph-theoretic analysis therefore provides a principled framework for investigating the organization of the learned grammar.

The following sections analyze the Visual Grammar through complementary graph-theoretic measures that collectively characterize its structural organization.



