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


---

# v0.2 Amendment — Zhang & Lu GFD versus 05H versus Historical WeaveAI

## Why this amendment matters

Zhang & Lu's Generic Fourier Descriptor materially narrows the novelty
boundary for Paper II.

GFD is strong prior art for:

- object-centred shape coordinates;
- object-derived radial normalization;
- polar-raster representation;
- Fourier analysis of radial/angular shape information;
- deterministic handcrafted generic shape description.

Therefore Paper II must NOT present object-centred polar Fourier shape
representation itself as a new method.

---

## Representation-family conclusion

The scientifically defensible statement is:

> GFD and WeaveAI 05H occupy closely related object-centred
> polar/spectral representation territory, but they are not currently
> treated as identical implementations.

The strongest overlap is:

    object geometry
        ↓
    object-derived centre
        ↓
    object-derived radial scale
        ↓
    polar / radial-angular domain
        ↓
    Fourier / spectral representation

The implementations diverge in how the field is constructed and,
especially, in how the final spectral representation is summarized.

---

## Zhang & Lu Generic Fourier Descriptor

Conceptually:

    2-D shape region
        ↓
    centroid-centred polar coordinates
        ↓
    normalize radius using object-derived radius
        ↓
    polar raster
        ↓
    2-D Fourier transform
        ↓
    selected normalized radial-angular Fourier coefficients
        ↓
    shape descriptor

No population training is required to compute GFD.

It is a deterministic handcrafted transform.

---

## WeaveAI 05H intrinsic representation

Conceptually:

    foreground garment geometry
        ↓
    foreground centroid
        ↓
    maximum foreground/object radius
        ↓
    object-relative radial-angular field
        ↓
    frozen spectral computation
        ↓
    angular-frequency allocation / band analysis

05H is therefore NOT evidence that object-relative polar Fourier geometry
was invented by WeaveAI.

Its importance inside Paper II is instead as a matched object-relative
control for the historical representation.

Under the 05K same-pixel support intervention, the intrinsic field/band
representation remained exactly invariant across all 16,100 tested
conditions.

---

## Historical WeaveAI representation

The decisive distinction is radial normalization.

Historical normalization retained a raster/grid-derived scale.

Therefore:

    same garment pixels
        +
    different surrounding raster support
        ↓
    different object-to-grid scale
        ↓
    different normalized coordinate placement
        ↓
    potentially different spectral allocation

05K demonstrated this empirically under a controlled same-pixel
support intervention.

This is the representation issue being audited.

---

## Side-by-side conceptual pipeline

### GFD

    object
      ↓
    object centroid
      ↓
    object radius
      ↓
    polar raster
      ↓
    2-D Fourier transform
      ↓
    selected normalized 2-D coefficients


### 05H

    object
      ↓
    foreground centroid
      ↓
    foreground maximum radius
      ↓
    object-relative radial-angular field
      ↓
    spectral analysis
      ↓
    angular spectral allocation / frozen bands


### Historical WeaveAI

    object
      ↓
    radial-angular representation
      ↓
    raster/grid-relative scale normalization
      ↓
    angular spectral allocation / frozen bands
      ↓
    sensitivity to surrounding support


---

## Exact novelty consequence

### Already prior art / DO NOT CLAIM AS NOVEL

- centroid-centred coordinates;
- object-derived scale normalization;
- scale/translation nuisance normalization;
- polar shape representation;
- radial/angular Fourier representation;
- generic object-centred Fourier shape descriptor;
- mathematical expectation that a purely object-relative descriptor
  ignores unrelated blank canvas.

### Established WeaveAI empirical result

The frozen historical raster-relative representation changes when blank
raster support is changed while the embedded garment pixels remain
unchanged.

The matched object-relative implementation is exactly invariant under
the same tested support manipulation.

### Novelty still OPEN

The literature review has not yet established whether prior work has
already performed the exact experimental counterfactual:

    bit-identical real object pixels
        +
    parametric 2-D surrounding canvas/support sweep
        +
    no object resampling
        +
    measurement of raster-relative spectral redistribution
        +
    matched object-relative control.

Therefore the phrase "novel support audit" must remain provisional until
the wider literature search is completed.

---

## Implication for future experiments

GFD should now become an explicit BASELINE rather than only a citation.

The future representation comparison should currently include:

1. historical raster-relative representation;
2. 05H intrinsic object-relative representation;
3. Zhang-Lu Generic Fourier Descriptor;
4. canonical object scaling / normalized support;
5. Shape Context;
6. semantic garment landmarks;
7. landmark Statistical Shape Model.

Complex new representations must justify themselves against established
GFD/Shape-Context prior art and against the simpler 05H intrinsic control.

---

## Important distinction: representation novelty versus experimental novelty

These are now separate questions.

### Representation novelty

Currently LOW for the broad object-centred polar-Fourier idea because GFD
and earlier invariant descriptors are clear prior art.

### Experimental audit novelty

Still unresolved.

05K may remain distinctive because it isolates support/frame choice using
an exact same-pixel intervention and contrasts raster-relative and
object-relative representations under the identical intervention.

This distinction must be preserved in all subsequent literature notes.

