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