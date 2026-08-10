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

**Next Section:** 3.1.2 Definition 1 (Geometry Event)

### 3.1.2 Definition 1 (Geometry Event)

Continuous garment contours exhibit geometric variations at multiple spatial scales. While some variations correspond to meaningful structural changes in garment geometry, others arise from minor drawing fluctuations, digitization artifacts, or stylistic differences between sketches. Consequently, constructing stable computational representations requires distinguishing persistent structural changes from transient local irregularities.

The objective of this stage is therefore to identify localized geometric changes that consistently characterize the structural organization of garment contours. These localized geometric changes constitute the fundamental observations from which higher-level geometric representations are subsequently learned.

#### Definition 1 (Geometry Event)

A **geometry event** is defined as a persistent localized change in garment contour geometry identified through variations in local geometric properties of the contour.

Unlike semantic garment components, geometry events are purely geometric entities. They are determined solely by the local organization of the garment contour and remain independent of predefined garment-part labels.

Formally, let

$$
C=\{c_1,c_2,\ldots,c_n\}
$$

denote the ordered sequence of contour points representing a garment sketch.

Let

$$
G(c_i)
$$

denote the local geometric descriptor evaluated at contour point

$$
c_i.
$$

A geometry event is identified by the mapping

$$
E_i=\Phi(G(c_i)),
$$

where

- \(E_i\) denotes the geometry event associated with contour location \(c_i\),
- \(G(\cdot)\) represents the local geometric descriptor, and
- \(\Phi(\cdot)\) denotes the event identification operator that determines whether the observed geometric variation satisfies the persistence criteria required to constitute a geometry event.

#### Scientific Interpretation

A geometry event represents a localized structural observation rather than an isolated geometric measurement. By requiring geometric changes to satisfy persistence criteria, the proposed framework suppresses transient local irregularities while preserving stable geometric organization that recurs across garment sketches.

Geometry events therefore constitute the first computational representation learned directly from garment geometry. Rather than representing complete garment parts, they provide localized geometric observations from which progressively richer representations are subsequently constructed.

The collection of geometry events identifies where meaningful geometric changes occur within a garment contour. However, individual geometry events remain localized observations and do not yet constitute reusable structural units. The next stage therefore investigates whether recurring geometry events observed across multiple garment sketches can be organized into a finite set of reusable geometry primitives.
