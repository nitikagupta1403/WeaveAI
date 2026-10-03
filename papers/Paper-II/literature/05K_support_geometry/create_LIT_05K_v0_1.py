from pathlib import Path
import pandas as pd
import hashlib
import json


ROOT = Path(
    "/Users/nitikagupta/Research/WeaveAI/"
    "papers/Paper-II/literature/05K_support_geometry"
)

ROOT.mkdir(parents=True, exist_ok=True)


# =============================================================================
# Literature ledger
# =============================================================================

rows = [

    {
        "paper_id": "LIT-05K-001",
        "citation_short": "Zahn & Roskies (1972)",
        "title": "Fourier Descriptors for Plane Closed Curves",
        "domain": "generic 2D closed shapes",
        "representation": "closed contour / Fourier descriptor",
        "author_level_contribution":
            "Classical Fourier representation of plane closed curves with "
            "normalisation/invariance considerations.",
        "raster_canvas_support_explicitly_tested": "NO EVIDENCE YET",
        "same_pixels_canvas_changed": "NO EVIDENCE YET",
        "relation_to_05K": "GENERAL THEORY",
        "relation_to_future_representation":
            "Foundational Fourier shape-normalisation background.",
        "weaveai_interpretation":
            "Classical precedent for removing nuisance coordinate effects, "
            "but not currently a direct precedent for the same-pixel "
            "2-D canvas-support intervention.",
        "status": "WORKING_REVIEW",
    },

    {
        "paper_id": "LIT-05K-002",
        "citation_short": "Persoon & Fu (1977)",
        "title": "Shape Discrimination Using Fourier Descriptors",
        "domain": "generic shapes / characters / machine parts",
        "representation": "closed boundary Fourier descriptors",
        "author_level_contribution":
            "Fourier-descriptor-based shape discrimination and matching.",
        "raster_canvas_support_explicitly_tested": "NO EVIDENCE YET",
        "same_pixels_canvas_changed": "NO EVIDENCE YET",
        "relation_to_05K": "GENERAL THEORY / PARTIAL PRECEDENT",
        "relation_to_future_representation":
            "Practical Fourier shape-discrimination precedent.",
        "weaveai_interpretation":
            "Relevant to invariant shape comparison but presently not "
            "evidence of the exact support-only intervention audited in 05K.",
        "status": "WORKING_REVIEW",
    },

    {
        "paper_id": "LIT-05K-003",
        "citation_short": "Kuhl & Giardina (1982)",
        "title": "Elliptic Fourier Features of a Closed Contour",
        "domain": "diverse generic closed shapes",
        "representation": "elliptic Fourier contour representation",
        "author_level_contribution":
            "Fourier description and normalisation of arbitrary closed "
            "contours with treatment of nuisance transformations.",
        "raster_canvas_support_explicitly_tested": "NO EVIDENCE YET",
        "same_pixels_canvas_changed": "NO EVIDENCE YET",
        "relation_to_05K": "STRONG GENERAL NORMALISATION PRECEDENT",
        "relation_to_future_representation":
            "Strong intrinsic/object-normalisation precedent.",
        "weaveai_interpretation":
            "Important because it demonstrates that intrinsic contour "
            "normalisation is established prior art across diverse shapes; "
            "our novelty cannot be 'object-relative normalisation itself'.",
        "status": "WORKING_REVIEW",
    },

    {
        "paper_id": "LIT-05K-004",
        "citation_short": "Belongie, Malik & Puzicha (2002)",
        "title": "Shape Matching and Object Recognition Using Shape Contexts",
        "domain": "generic shapes / line and contour point sets",
        "representation": "sampled contour points + log-polar shape contexts",
        "author_level_contribution":
            "Shape description from relative distributions of sampled "
            "shape points, followed by correspondence and alignment.",
        "raster_canvas_support_explicitly_tested": "NO EVIDENCE YET",
        "same_pixels_canvas_changed": "NO EVIDENCE YET",
        "relation_to_05K": "CLOSE REPRESENTATIONAL PRECEDENT",
        "relation_to_future_representation":
            "Established dense/sampled object-relative point representation; "
            "candidate baseline rather than something for WeaveAI to reinvent.",
        "weaveai_interpretation":
            "Very close to fine-line garment sketches because geometry is "
            "represented through relative point relationships rather than "
            "absolute raster position.",
        "status": "HIGH_PRIORITY_WORKING_REVIEW",
    },

    {
        "paper_id": "LIT-05K-005",
        "citation_short": "Cootes et al. (1995)",
        "title": "Active Shape Models—Their Training and Application",
        "domain": "deformable object shape modelling",
        "representation":
            "corresponding landmarks + statistical point distribution model",
        "author_level_contribution":
            "Learns allowable shape variation from corresponding labelled "
            "points and fits the model to image evidence.",
        "raster_canvas_support_explicitly_tested": "NO EVIDENCE YET",
        "same_pixels_canvas_changed": "NO EVIDENCE YET",
        "relation_to_05K": "DIRECT SSM/LANDMARK PRECEDENT",
        "relation_to_future_representation":
            "Direct foundation for semantic landmarks, alignment, statistical "
            "shape modelling and constrained landmark fitting.",
        "weaveai_interpretation":
            "Strong precedent for separating semantic structural geometry "
            "from incidental raster content; directly relevant to the planned "
            "garment landmark/SSM branch.",
        "status": "HIGH_PRIORITY_WORKING_REVIEW",
    },
]


df = pd.DataFrame(rows)

CSV = ROOT / "LIT_05K_literature_ledger_v0_1.csv"
df.to_csv(CSV, index=False, lineterminator="\n")


# =============================================================================
# Rich working notes
# =============================================================================

notes = """# LIT-05K — Working Literature Notes v0.1

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
"""


MD = ROOT / "LIT_05K_working_notes_v0_1.md"
MD.write_text(notes, encoding="utf-8")


# =============================================================================
# Manifest
# =============================================================================

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


manifest = {
    "version": "v0.1",
    "status": "WORKING_LITERATURE_CAPTURE",
    "paper_count": len(df),
    "novelty_assessed": False,
    "literature_complete": False,
    "files": {
        CSV.name: sha256(CSV),
        MD.name: sha256(MD),
    },
}


MANIFEST = ROOT / "LIT_05K_manifest_v0_1.json"

MANIFEST.write_text(
    json.dumps(manifest, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)


print("=" * 90)
print("LIT-05K WORKING LITERATURE CAPTURE v0.1")
print("=" * 90)

print("Papers:", len(df))
print("Novelty assessed: NO")
print("Literature complete: NO")

print()
print("OUTPUTS")

for path in [CSV, MD, MANIFEST]:
    print(path.name, sha256(path))

print()
print("SAFE TO COMMIT AS VERSIONED WORKING LITERATURE NOTES.")
print("DO NOT LABEL AS FINAL LITERATURE SYNTHESIS.")