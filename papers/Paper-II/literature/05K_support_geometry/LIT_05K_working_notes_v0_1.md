# LIT-05K — Working Literature Notes v0.1

## Scope

Literature scope is deliberately broader than fashion.

Include:

- sketches
- line drawings
- contour drawings
- silhouettes
- handwritten shapes
- generic 2-D shape representation
- Fourier/spectral shape descriptors
- object-relative coordinate systems
- landmark models
- statistical shape models
- raster/canvas/support effects

Fashion is the application domain, not the sole literature domain.

---

# Locked Paper-II question being taken to literature

Under the frozen historical raster-relative coordinate normalization,
raster support was demonstrated to affect angular spectral allocation
under the controlled same-pixel support intervention.

The matched object-relative representation was exactly invariant under
the same tested intervention.

The literature audit must determine what parts of this are prior art,
partial precedent, or potentially unaddressed.

No novelty conclusion is made at v0.1.

---

# LIT-05K-001 — Zahn & Roskies (1972)

## Paper

Fourier Descriptors for Plane Closed Curves.

## Source-level relevance

Classical closed-contour Fourier representation and nuisance-transform
normalisation.

## Current WeaveAI interpretation

Important foundational prior art for Fourier shape normalisation.

No evidence recorded yet that the paper performs the specific
counterfactual:

    identical rasterised object pixels
    + independently changed surrounding 2-D canvas/support.

Therefore currently classified as GENERAL THEORY rather than direct
05K precedent.

---

# LIT-05K-002 — Persoon & Fu (1977)

## Paper

Shape Discrimination Using Fourier Descriptors.

## Source-level relevance

Moves Fourier descriptors toward practical shape discrimination and
recognition.

## Current WeaveAI interpretation

Relevant precedent for invariant shape comparison.

Current review has not identified an experiment equivalent to the
same-object / different-blank-canvas intervention used in 05K.

---

# LIT-05K-003 — Kuhl & Giardina (1982)

## Paper

Elliptic Fourier Features of a Closed Contour.

## Important observation

The framework is deliberately generic and is demonstrated over diverse
closed shapes rather than one narrow application domain.

## Current WeaveAI interpretation

This is strong prior art for intrinsic contour normalisation.

Therefore WeaveAI must NOT claim that:

    object-relative or intrinsic shape normalisation itself is novel.

Its relationship to the exact 05K same-pixel raster-support experiment
remains a separate question.

---

# LIT-05K-004 — Belongie, Malik & Puzicha (2002)

## Paper

Shape Matching and Object Recognition Using Shape Contexts.

## Why this paper is especially close to our sketches

The representation operates on sampled contour/edge points and uses
relative spatial relationships rather than absolute image coordinates.

This is visually and geometrically closer to fine-line garment sketches
than filled-region-only descriptors.

## Figure 3 observation

Figure 3 illustrates the core representation:

    reference shape point
        ↓
    relative coordinates of other shape points
        ↓
    log-polar spatial bins
        ↓
    shape-context histogram
        ↓
    point correspondences between shapes

Important separation:

AUTHOR-LEVEL IDEA:
    Shape Context describes a point by the relative spatial distribution
    of other points.

WEAVEAI INTERPRETATION:
    This is strongly analogous to our interest in object-relative
    radial/angular geometry and is substantially less dependent on the
    external raster frame than our historical grid-relative representation.

## Consequence for our research roadmap

We should NOT invent a new generic sampled-point relational descriptor
and present that concept as new.

Shape Context should instead become an established baseline/reference.

Potential representation ladder:

    historical raster-relative spectrum
        ↓
    intrinsic dense radial/angular field
        ↓
    established Shape Context baseline
        ↓
    semantic garment landmarks
        ↓
    statistical shape model

## Critical distinction

Shape Context points are not necessarily semantic landmarks.

Dense/sampled contour points:
    geometric / generic

Garment landmarks:
    semantic / homologous structural points

That distinction should remain explicit in future experiments.

---

# LIT-05K-005 — Cootes et al. (1995)

## Paper

Active Shape Models—Their Training and Application.

## Core representation

Corresponding labelled shape points are aligned and their population
variation is learned through a statistical point distribution model.

This directly precedes our proposed landmark/SSM branch.

---

## Figure 1 observation

Figure 1 is relevant to the distinction between:

    structural object geometry

and

    arbitrary image/raster content.

WEAVEAI INTERPRETATION:

For garment sketches, a semantic landmark model could represent:

- neckline
- shoulder tips
- sleeve endpoints
- waist locations
- hem extrema
- crotch/rise points where applicable
- leg endpoints

while incidental foreground such as:

- text
- page annotations
- stray marks

need not belong to the structural representation.

IMPORTANT:

This is a WeaveAI interpretation and hypothesis.

Do NOT write that Cootes et al. demonstrated robustness to garment text
contamination.

---

## Figure 21 observation

Figure 21 illustrates a practical fitting idea:

    current model point
        ↓
    search locally along the boundary-normal/profile direction
        ↓
    find stronger local image-edge evidence
        ↓
    propose movement of the point
        ↓
    constrain the resulting configuration using the global shape model

## Relevance to garment sketches

This provides classical precedent for how semantic garment landmarks
might eventually be refined automatically from fine-line drawings.

Potential future conceptual pipeline:

    rough garment landmark estimate
        ↓
    local edge/profile evidence
        ↓
    proposed point displacement
        ↓
    SSM / PDM global structural constraint
        ↓
    refined garment landmark configuration

This is particularly relevant because garment sketches may contain:

- folds
- seams
- internal construction lines
- text
- stray marks

so local image evidence alone may be ambiguous.

The statistical shape constraint provides a way to prevent points from
moving independently to implausible locations.

---

# Representation distinction emerging from first five papers

## Historical WeaveAI raster spectrum

Raster-relative.

Can respond to surrounding support.

---

## 05H intrinsic field

Dense object-relative representation.

Captures foreground/contour geometry over the full object-relative
domain.

---

## Shape Context

Sampled/dense relational point representation.

Captures relative geometry around contour/edge points.

Established prior art.

---

## Semantic garment landmarks

Sparse homologous structural representation.

Potentially captures:

- neckline geometry
- shoulder structure
- sleeve extent
- waist location
- hem structure
- garment topology anchors

without representing every incidental foreground mark.

---

## Statistical Shape Model

Population model over corresponding semantic shape configurations.

Captures principal structural variation after alignment.

Requires reliable correspondence and annotation.

---

# Current research consequence

Do NOT jump directly into inventing another generic object-relative
descriptor.

The next representation work should eventually compare established and
newly justified alternatives:

1. historical raster-relative spectrum
2. intrinsic object-relative dense field
3. canonical resize / object-support normalisation
4. Shape Context baseline
5. semantic garment landmarks
6. landmark SSM

More complex approaches must justify themselves against the simple
intrinsic baseline already established in Paper II.

---

# Current novelty boundary

NOT YET RESOLVED.

Known prior art already covers:

- Fourier shape normalisation
- intrinsic/object-relative shape representation
- point-relative spatial descriptors
- landmark correspondence
- statistical shape modelling
- constrained landmark fitting

Still to investigate carefully:

- explicit same-pixel 2-D canvas/support manipulation
- fixed object geometry with independently changed blank support
- resulting redistribution of raster-relative spectral bands
- matched raster-relative versus object-relative intervention analysis

No novelty statement should be written until the literature audit is
substantially broader.

---

# Next literature step

Continue the literature audit before any new representation experiment.

High-priority next families:

- MPEG-7 shape descriptors / ART
- Generic Fourier Descriptor
- raster support / zero-padding / finite-domain effects
- digital normalisation limitations
- sketch-specific shape retrieval
- landmark/SSM work closer to drawings and garments
