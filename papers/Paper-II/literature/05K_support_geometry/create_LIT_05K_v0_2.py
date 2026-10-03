from pathlib import Path
import hashlib
import json

import pandas as pd


# =============================================================================
# LIT-05K v0.2
#
# PURPOSE
#   Extend the working literature capture after close comparison of:
#
#       Zhang & Lu Generic Fourier Descriptor (GFD)
#       versus
#       WeaveAI 05H intrinsic representation
#       versus
#       historical WeaveAI raster-relative representation
#
# IMPORTANT
#   - v0.1 remains untouched.
#   - This is still WORKING literature synthesis.
#   - No final novelty claim is made.
#   - Representation-family overlap and exact implementation identity
#     are deliberately distinguished.
# =============================================================================


ROOT = Path(
    "/Users/nitikagupta/Research/WeaveAI/"
    "papers/Paper-II/literature/05K_support_geometry"
)


V01_LEDGER = (
    ROOT
    / "LIT_05K_literature_ledger_v0_1.csv"
)

V01_NOTES = (
    ROOT
    / "LIT_05K_working_notes_v0_1.md"
)


require_paths = [
    V01_LEDGER,
    V01_NOTES,
]

for path in require_paths:
    if not path.is_file():
        raise RuntimeError(
            f"Missing required v0.1 source: {path}"
        )


# =============================================================================
# Helpers
# =============================================================================

def sha256(path):
    h = hashlib.sha256()

    with Path(path).open("rb") as f:
        for chunk in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
            h.update(chunk)

    return h.hexdigest()


# =============================================================================
# 1. Extend literature ledger
# =============================================================================

ledger_v01 = pd.read_csv(
    V01_LEDGER,
    keep_default_na=False,
)


new_record = {

    "paper_id":
        "LIT-05K-007",

    "citation_short":
        "Zhang & Lu (2002)",

    "title":
        "Shape-based Image Retrieval Using Generic Fourier Descriptor",

    "domain":
        "generic 2-D region shape retrieval",

    "representation":
        (
            "object-centred polar-raster shape representation "
            "+ 2-D Fourier transform"
        ),

    "author_level_contribution":
        (
            "Introduces the Generic Fourier Descriptor (GFD), "
            "using a polar-raster representation and 2-D Fourier "
            "transform to encode radial and angular shape information "
            "for generic shape retrieval."
        ),

    "raster_canvas_support_explicitly_tested":
        "NO DIRECT SAME-PIXEL SUPPORT TEST IDENTIFIED YET",

    "same_pixels_canvas_changed":
        "NO DIRECT PRECEDENT IDENTIFIED YET",

    "relation_to_05K":
        "VERY STRONG REPRESENTATION-FAMILY PRIOR ART",

    "relation_to_future_representation":
        (
            "Mandatory object-centred polar-Fourier baseline. "
            "Prevents any novelty claim for object-centred polar "
            "Fourier shape representation itself."
        ),

    "weaveai_interpretation":
        (
            "GFD and 05H occupy closely related object-centred "
            "polar/spectral representation territory. They must not "
            "be treated as identical implementations: GFD retains "
            "normalized 2-D radial-angular Fourier coefficients, "
            "whereas the frozen WeaveAI analysis constructs its own "
            "radial-angular field and summarizes angular spectral "
            "allocation into predefined bands. The historical WeaveAI "
            "representation differs critically through raster/grid-"
            "relative normalization, whose support dependence was "
            "demonstrated by 05K."
        ),

    "status":
        "HIGH_PRIORITY_WORKING_REVIEW",
}


if (
    "LIT-05K-007"
    in ledger_v01[
        "paper_id"
    ].tolist()
):
    raise RuntimeError(
        "LIT-05K-007 already exists in v0.1 ledger"
    )


ledger_v02 = pd.concat(
    [
        ledger_v01,
        pd.DataFrame(
            [
                new_record
            ]
        ),
    ],
    ignore_index=True,
)


V02_LEDGER = (
    ROOT
    / "LIT_05K_literature_ledger_v0_2.csv"
)


ledger_v02.to_csv(
    V02_LEDGER,
    index=False,
    lineterminator="\n",
)


# =============================================================================
# 2. Exact comparison ledger
#
# "Exact" here means exact with respect to our current documented
# understanding. It does NOT mean the two representations are identical.
# =============================================================================

comparison_rows = [

    {
        "comparison_item":
            "Representation purpose",

        "Zhang_Lu_GFD":
            (
                "Generic handcrafted shape descriptor for "
                "shape-based retrieval."
            ),

        "WeaveAI_05H_intrinsic":
            (
                "Object-relative radial-angular representation used "
                "as the matched support-invariant control/audit "
                "representation."
            ),

        "Historical_WeaveAI":
            (
                "Frozen radial-angular spectral representation used "
                "in the historical retrieval pipeline."
            ),

        "scientific_status":
            "DIFFERENT PURPOSES; RELATED REPRESENTATION FAMILY",
    },


    {
        "comparison_item":
            "Input geometry",

        "Zhang_Lu_GFD":
            "2-D shape region",

        "WeaveAI_05H_intrinsic":
            (
                "Foreground/object geometry represented in a "
                "radial-angular field."
            ),

        "Historical_WeaveAI":
            (
                "Foreground/object geometry represented in a "
                "radial-angular field."
            ),

        "scientific_status":
            "RELATED",
    },


    {
        "comparison_item":
            "Coordinate origin",

        "Zhang_Lu_GFD":
            "Object centroid / center of mass",

        "WeaveAI_05H_intrinsic":
            "Foreground centroid",

        "Historical_WeaveAI":
            (
                "Historical coordinate construction; centroid-relative "
                "geometry combined with raster/grid-relative scale."
            ),

        "scientific_status":
            (
                "GFD AND 05H OBJECT-CENTRED; "
                "HISTORICAL IMPLEMENTATION RETAINS GRID DEPENDENCE"
            ),
    },


    {
        "comparison_item":
            "Radial scale normalization",

        "Zhang_Lu_GFD":
            "Object-derived maximum radius",

        "WeaveAI_05H_intrinsic":
            "Maximum foreground/object radius",

        "Historical_WeaveAI":
            "Raster/grid-derived radius normalization",

        "scientific_status":
            (
                "CRITICAL DIFFERENCE BETWEEN OBJECT-RELATIVE "
                "AND HISTORICAL REPRESENTATION"
            ),
    },


    {
        "comparison_item":
            "External blank canvas enters coordinate definition?",

        "Zhang_Lu_GFD":
            (
                "Not intended to, after object-centred/object-scale "
                "normalization."
            ),

        "WeaveAI_05H_intrinsic":
            (
                "No under tested same-pixel support intervention; "
                "05K observed exact invariance."
            ),

        "Historical_WeaveAI":
            (
                "Yes. Raster dimensions affect the normalized "
                "coordinate domain."
            ),

        "scientific_status":
            "CENTRAL 05K DISTINCTION",
    },


    {
        "comparison_item":
            "Polar / radial-angular domain",

        "Zhang_Lu_GFD":
            "Yes — polar-raster representation",

        "WeaveAI_05H_intrinsic":
            "Yes — object-relative radial-angular field",

        "Historical_WeaveAI":
            "Yes — radial-angular field",

        "scientific_status":
            "STRONG FAMILY OVERLAP",
    },


    {
        "comparison_item":
            "Whole-region versus single contour",

        "Zhang_Lu_GFD":
            "Region-based polar raster",

        "WeaveAI_05H_intrinsic":
            (
                "Dense/occupancy-style object-relative field; "
                "not merely one outer r(theta) contour."
            ),

        "Historical_WeaveAI":
            (
                "Dense radial-angular representation; "
                "not simply an elliptic Fourier contour descriptor."
            ),

        "scientific_status":
            "STRONG CONCEPTUAL OVERLAP",
    },


    {
        "comparison_item":
            "Spectral transform",

        "Zhang_Lu_GFD":
            "2-D Fourier transform in polar raster coordinates",

        "WeaveAI_05H_intrinsic":
            (
                "Frozen radial-angular spectral computation with "
                "angular-frequency analysis."
            ),

        "Historical_WeaveAI":
            (
                "Frozen radial-angular spectral computation with "
                "angular-frequency analysis."
            ),

        "scientific_status":
            (
                "RELATED FOURIER/SPECTRAL FAMILY; "
                "DO NOT CALL IMPLEMENTATIONS IDENTICAL"
            ),
    },


    {
        "comparison_item":
            "Final descriptor / summary",

        "Zhang_Lu_GFD":
            (
                "Selected normalized 2-D Fourier coefficients "
                "indexed by radial and angular frequency."
            ),

        "WeaveAI_05H_intrinsic":
            (
                "Angular spectral allocation derived from the "
                "radial-angular representation; evaluated using "
                "predefined angular bands."
            ),

        "Historical_WeaveAI":
            (
                "Angular spectral allocation summarized into "
                "low, mid, highmid, and high bands."
            ),

        "scientific_status":
            "GENUINE IMPLEMENTATION / SUMMARY DIFFERENCE",
    },


    {
        "comparison_item":
            "Frozen angular bands",

        "Zhang_Lu_GFD":
            "Not the WeaveAI four-band construction",

        "WeaveAI_05H_intrinsic":
            (
                "low 1-4; mid 5-12; highmid 13-24; high 25-36"
            ),

        "Historical_WeaveAI":
            (
                "low 1-4; mid 5-12; highmid 13-24; high 25-36"
            ),

        "scientific_status":
            "WEAVEAI-SPECIFIC ANALYSIS CHOICE",
    },


    {
        "comparison_item":
            "Learned from training data?",

        "Zhang_Lu_GFD":
            "No — deterministic handcrafted transform",

        "WeaveAI_05H_intrinsic":
            "No — deterministic representation",

        "Historical_WeaveAI":
            "No — deterministic representation",

        "scientific_status":
            "SAME",
    },


    {
        "comparison_item":
            "Primary invariance intention",

        "Zhang_Lu_GFD":
            (
                "Generic robust shape description with geometric "
                "nuisance normalization."
            ),

        "WeaveAI_05H_intrinsic":
            (
                "Object-relative control removing raster-support "
                "dependence under the tested intervention."
            ),

        "Historical_WeaveAI":
            (
                "Was not support-invariant under the frozen "
                "grid-relative normalization."
            ),

        "scientific_status":
            "IMPORTANT DIFFERENCE IN IMPLEMENTATION BEHAVIOR",
    },


    {
        "comparison_item":
            "Same-pixel support-only canvas sweep",

        "Zhang_Lu_GFD":
            (
                "No direct experiment identified in current review."
            ),

        "WeaveAI_05H_intrinsic":
            (
                "Yes — matched control in 05K over the frozen "
                "support intervention."
            ),

        "Historical_WeaveAI":
            (
                "Yes — primary representation under the same "
                "controlled support intervention."
            ),

        "scientific_status":
            "POTENTIAL DISTINCTIVE EXPERIMENTAL AUDIT",
    },


    {
        "comparison_item":
            "Observed support-only behavior",

        "Zhang_Lu_GFD":
            "Not established by current literature review",

        "WeaveAI_05H_intrinsic":
            (
                "Exact invariance across all tested 16,100 "
                "support conditions."
            ),

        "Historical_WeaveAI":
            (
                "Systematic support-dependent redistribution; "
                "primary 05K directional inference supported."
            ),

        "scientific_status":
            "WEAVEAI EMPIRICAL RESULT",
    },
]


comparison_df = pd.DataFrame(
    comparison_rows
)


COMPARISON_CSV = (
    ROOT
    / "LIT_05K_GFD_vs_05H_vs_Historical_comparison_v0_2.csv"
)


comparison_df.to_csv(
    COMPARISON_CSV,
    index=False,
    lineterminator="\n",
)


# =============================================================================
# 3. Novelty-boundary ledger
# =============================================================================

novelty_rows = [

    {
        "claim_id":
            "NB01",

        "candidate_claim":
            "Object-centred shape coordinates are novel.",

        "status":
            "PROHIBITED",

        "reason":
            (
                "Centroid/object-derived coordinate normalization "
                "is established prior art."
            ),
    },


    {
        "claim_id":
            "NB02",

        "candidate_claim":
            "Object-radius normalization is novel.",

        "status":
            "PROHIBITED",

        "reason":
            (
                "Classical invariant shape descriptors and GFD-type "
                "methods already use object-derived normalization."
            ),
    },


    {
        "claim_id":
            "NB03",

        "candidate_claim":
            (
                "Polar/radial-angular Fourier shape representation "
                "is novel."
            ),

        "status":
            "PROHIBITED",

        "reason":
            (
                "Zhang & Lu GFD is direct prior art for an "
                "object-centred polar-raster Fourier descriptor."
            ),
    },


    {
        "claim_id":
            "NB04",

        "candidate_claim":
            (
                "Object-relative normalization should remove "
                "blank-canvas dependence."
            ),

        "status":
            "GENERAL PRIOR-ART PRINCIPLE",

        "reason":
            (
                "If coordinates depend only on object centroid and "
                "object-derived scale, outer blank support is absent "
                "from the coordinate definition by construction."
            ),
    },


    {
        "claim_id":
            "NB05",

        "candidate_claim":
            (
                "The frozen historical raster-relative representation "
                "systematically redistributes angular spectral evidence "
                "when only surrounding support changes while embedded "
                "garment pixels remain fixed."
            ),

        "status":
            "WEAVEAI EMPIRICAL RESULT; NOVELTY NOT YET FINAL",

        "reason":
            (
                "Demonstrated by the controlled 05K same-pixel "
                "support intervention. Current literature review has "
                "not yet identified a direct equivalent experiment."
            ),
    },


    {
        "claim_id":
            "NB06",

        "candidate_claim":
            (
                "Matched raster-relative versus object-relative "
                "representations can be contrasted under the same "
                "bit-identical foreground support sweep."
            ),

        "status":
            "POTENTIALLY DISTINCTIVE EXPERIMENTAL DESIGN",

        "reason":
            (
                "05K directly isolates frame/support dependence while "
                "holding embedded pixels unchanged. Novelty relative "
                "to literature remains open until the audit is broader."
            ),
    },


    {
        "claim_id":
            "NB07",

        "candidate_claim":
            (
                "WeaveAI's four angular-frequency bands constitute "
                "a new generic Fourier descriptor."
            ),

        "status":
            "DO NOT CLAIM",

        "reason":
            (
                "They are a project-specific analysis/aggregation "
                "of the frozen representation, not evidence of a "
                "new generic Fourier theory."
            ),
    },
]


novelty_df = pd.DataFrame(
    novelty_rows
)


NOVELTY_CSV = (
    ROOT
    / "LIT_05K_novelty_boundary_v0_2.csv"
)


novelty_df.to_csv(
    NOVELTY_CSV,
    index=False,
    lineterminator="\n",
)


# =============================================================================
# 4. Rich v0.2 notes
# =============================================================================

v01_text = V01_NOTES.read_text(
    encoding="utf-8"
)


appendix = r"""

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

"""

V02_NOTES = (
    ROOT
    / "LIT_05K_working_notes_v0_2.md"
)


V02_NOTES.write_text(
    v01_text
    + appendix,
    encoding="utf-8",
)


# =============================================================================
# 5. Manifest
# =============================================================================

MANIFEST = (
    ROOT
    / "LIT_05K_manifest_v0_2.json"
)


manifest = {

    "version":
        "v0.2",

    "status":
        "WORKING_LITERATURE_CAPTURE",

    "parent_version":
        "v0.1",

    "paper_count":
        int(
            len(
                ledger_v02
            )
        ),

    "new_primary_focus":
        "Zhang_Lu_2002_Generic_Fourier_Descriptor",

    "material_change":
        (
            "Object-centred polar Fourier representation is now "
            "explicitly treated as strong prior art. Potential "
            "contribution boundary shifts toward the controlled "
            "same-pixel raster-support audit rather than the broad "
            "representation family."
        ),

    "novelty_assessed":
        False,

    "novelty_boundary_updated":
        True,

    "literature_complete":
        False,

    "new_experiment_performed":
        False,

    "files": {

        V02_LEDGER.name:
            sha256(
                V02_LEDGER
            ),

        COMPARISON_CSV.name:
            sha256(
                COMPARISON_CSV
            ),

        NOVELTY_CSV.name:
            sha256(
                NOVELTY_CSV
            ),

        V02_NOTES.name:
            sha256(
                V02_NOTES
            ),
    },
}


MANIFEST.write_text(
    json.dumps(
        manifest,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


# =============================================================================
# 6. Final
# =============================================================================

print("=" * 100)
print(
    "LIT-05K WORKING LITERATURE CAPTURE v0.2"
)
print("=" * 100)

print()

print(
    "Parent version:",
    "v0.1",
)

print(
    "Papers:",
    len(
        ledger_v02
    ),
)

print(
    "Added:",
    "LIT-05K-007 Zhang & Lu (2002) GFD",
)

print()

print(
    "NOVELTY BOUNDARY UPDATED: YES"
)

print(
    "Novelty finalized: NO"
)

print(
    "Literature complete: NO"
)

print(
    "New experiment performed: NO"
)

print()

print(
    "KEY CHANGE"
)

print(
    "Object-centred polar Fourier shape representation "
    "is treated as strong prior art."
)

print(
    "Potential Paper-II distinction shifts toward the "
    "controlled same-pixel raster-support audit."
)

print()

print(
    "OUTPUT HASHES"
)

for path in [

    V02_LEDGER,
    COMPARISON_CSV,
    NOVELTY_CSV,
    V02_NOTES,
    MANIFEST,

]:

    print(
        path.name,
        sha256(
            path
        ),
    )

print()

print(
    "SAFE TO COMMIT AS WORKING LITERATURE v0.2."
)

print(
    "DO NOT FREEZE AS FINAL NOVELTY SYNTHESIS."
)