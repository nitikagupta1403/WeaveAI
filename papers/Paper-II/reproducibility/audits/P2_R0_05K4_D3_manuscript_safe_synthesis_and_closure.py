from pathlib import Path
import hashlib
import json

import pandas as pd


# =============================================================================
# P2-R0-05K4-D3
# MANUSCRIPT-SAFE SYNTHESIS AND SUPPORT-AUDIT CLOSURE
#
# PURPOSE
#   Convert the frozen D2 result-evidence synthesis into:
#
#   1. manuscript-safe scientific statements,
#   2. an explicit Observation → Interpretation → Boundary ledger,
#   3. a formal closure decision for the support-dependence audit.
#
# THIS STAGE DOES NOT:
#   - rerun any experiment
#   - recompute any statistic
#   - change thresholds
#   - select new examples
#   - introduce a new representation
#   - establish methodological novelty
#   - perform literature review
#
# IMPORTANT
#   "Closed" below means:
#
#   The specific internal question
#
#       "Does raster support affect the frozen historical
#        raster-relative representation under a controlled
#        same-pixel support intervention?"
#
#   has sufficient evidence for the present Paper-II mechanism audit.
#
#   Closure DOES NOT mean:
#   - every source of spectral variation has been explained,
#   - image-level heterogeneity has been explained,
#   - external generalization has been established,
#   - novelty relative to prior literature has been established.
# =============================================================================


REPO = Path(
    "/Users/nitikagupta/Research/WeaveAI"
)

FROZEN = (
    REPO
    / "papers/Paper-II/reproducibility/frozen"
)

AUDITS = (
    REPO
    / "papers/Paper-II/reproducibility/audits"
)

D2_DIR = (
    FROZEN
    / "05K4_D2_Result_Evidence_Synthesis_v1_0"
)

OUT = (
    AUDITS
    / "05K4_D3_manuscript_safe_synthesis_and_closure"
)

OUT.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Helpers
# =============================================================================

def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha256_file(path):
    h = hashlib.sha256()

    with Path(path).open("rb") as f:
        for chunk in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
            h.update(chunk)

    return h.hexdigest()


# =============================================================================
# 1. Frozen D2 inputs
# =============================================================================

D2_LEDGER = (
    D2_DIR
    / "P2_R0_05K4_D2_result_evidence_ledger.csv"
)

D2_CHAIN = (
    D2_DIR
    / "P2_R0_05K4_D2_evidence_chain.csv"
)

D2_BOUNDARY = (
    D2_DIR
    / "P2_R0_05K4_D2_synthesis_boundary.json"
)

D2_REPORT = (
    D2_DIR
    / "P2_R0_05K4_D2_report.json"
)


EXPECTED_D2_SHA = {

    "ledger":
        "8e870a34538d60782339b8fdb4fc0ebbb538b24fc40cb3a68326a432669e0111",

    "chain":
        "1590b7675442619c11135fe95f5c26c08bfe7534a747093a1b0375a71f891dbd",

    "boundary":
        "0468b4b4f6ebdf96be7994d987ad02ee064e1754076c11de37fd0f9dfabfb280",

    "report":
        "805dec22acb9237c0cc4f5ab39d16e20828f6a80f9921f3314f5e99de0b355a3",
}


print("=" * 122)
print(
    "P2-R0-05K4-D3 — "
    "MANUSCRIPT-SAFE SYNTHESIS AND SUPPORT-AUDIT CLOSURE"
)
print("=" * 122)

print()
print("Verifying frozen D2 inputs...")


for label, path in [

    ("ledger", D2_LEDGER),
    ("chain", D2_CHAIN),
    ("boundary", D2_BOUNDARY),
    ("report", D2_REPORT),

]:

    require(
        path.is_file(),
        f"Missing frozen D2 artifact: {path}",
    )

    observed = sha256_file(
        path
    )

    expected = EXPECTED_D2_SHA[
        label
    ]

    require(
        observed == expected,
        (
            f"D2 {label} SHA mismatch\n"
            f"expected={expected}\n"
            f"observed={observed}"
        ),
    )

    print(
        f"{label:10s}",
        "PASS",
    )


# =============================================================================
# 2. Load frozen D2 synthesis
# =============================================================================

ledger = pd.read_csv(
    D2_LEDGER,
    keep_default_na=False,
)

chain = pd.read_csv(
    D2_CHAIN,
    keep_default_na=False,
)

boundary = json.loads(
    D2_BOUNDARY.read_text(
        encoding="utf-8"
    )
)

report_d2 = json.loads(
    D2_REPORT.read_text(
        encoding="utf-8"
    )
)


require(
    len(ledger) == 12,
    f"Expected 12 D2 result records; got {len(ledger)}",
)

require(
    len(chain) == 6,
    f"Expected 6 D2 evidence-chain steps; got {len(chain)}",
)

require(
    report_d2[
        "status"
    ]
    == "PASS_RESULT_LEVEL_SYNTHESIS",
    "Frozen D2 report is not PASS_RESULT_LEVEL_SYNTHESIS",
)


# =============================================================================
# 3. Result IDs required for D3
# =============================================================================

REQUIRED_RESULTS = {
    "R01",
    "R02",
    "R03",
    "R04",
    "R05",
    "R06",
    "R07",
    "R08",
    "R09",
    "R10",
    "R11",
    "R12",
}


observed_result_ids = set(
    ledger[
        "result_id"
    ]
    .tolist()
)


require(
    observed_result_ids == REQUIRED_RESULTS,
    (
        "Unexpected D2 result universe\n"
        f"expected={sorted(REQUIRED_RESULTS)}\n"
        f"observed={sorted(observed_result_ids)}"
    ),
)


# =============================================================================
# 4. Manuscript-safe claim ledger
#
# No new result is being generated here.
# Each statement is a synthesis of already frozen D2 records.
# =============================================================================

CLAIMS = [

    # -------------------------------------------------------------------------
    # M01 — localization
    # -------------------------------------------------------------------------

    {
        "claim_id":
            "M01",

        "section_role":
            "mechanism_localization",

        "source_result_ids":
            "R01",

        "observation":
            (
                "The high-band change was negligible after text-only "
                "blanking but appeared predominantly at the crop-only "
                "transition."
            ),

        "interpretation":
            (
                "The instability enters primarily when the image is "
                "reframed onto a different raster support."
            ),

        "manuscript_safe_claim":
            (
                "Preprocessing ablation localized the high-band change "
                "primarily to the crop-only transition, whereas subsequent "
                "resize/pad processing produced negligible additional change."
            ),

        "strength":
            "supported_preprocessing_localization",

        "boundary":
            (
                "This localizes the responsible preprocessing component "
                "but does not by itself identify the geometric dependency."
            ),
    },


    # -------------------------------------------------------------------------
    # M02 — retained pixels and centroid
    # -------------------------------------------------------------------------

    {
        "claim_id":
            "M02",

        "section_role":
            "geometry_control",

        "source_result_ids":
            "R02;R03",

        "observation":
            (
                "Cropping preserved retained garment pixels and the "
                "source-coordinate foreground centroid while substantially "
                "changing frame-relative occupancy and support geometry."
            ),

        "interpretation":
            (
                "The spectral change does not require modification of the "
                "retained garment pixels or displacement of the garment "
                "centroid."
            ),

        "manuscript_safe_claim":
            (
                "The crop preserved retained garment intensities and "
                "source-coordinate centroid, while markedly altering "
                "garment occupancy relative to the raster."
            ),

        "strength":
            "supported_descriptive_geometry",

        "boundary":
            (
                "These descriptives establish geometric plausibility but "
                "do not establish which support variable is causal."
            ),
    },


    # -------------------------------------------------------------------------
    # M03 — observational association
    # -------------------------------------------------------------------------

    {
        "claim_id":
            "M03",

        "section_role":
            "population_association",

        "source_result_ids":
            "R04;R05;R06",

        "observation":
            (
                "Changes in garment extent relative to raster support were "
                "associated with systematic redistribution across angular "
                "frequency bands."
            ),

        "interpretation":
            (
                "Raster-relative extent is a plausible explanatory variable "
                "for the RAW→CROP redistribution."
            ),

        "manuscript_safe_claim":
            (
                "Across the full dataset, larger crop-induced changes in "
                "raster-relative garment extent were associated with reduced "
                "low/mid allocation and increased highmid/high allocation."
            ),

        "strength":
            "supported_observational_association",

        "boundary":
            (
                "The population association remains observational and "
                "cannot establish support dependence on its own."
            ),
    },


    # -------------------------------------------------------------------------
    # M04 — intervention
    # -------------------------------------------------------------------------

    {
        "claim_id":
            "M04",

        "section_role":
            "controlled_support_intervention",

        "source_result_ids":
            "R07;R08;R10;R11",

        "observation":
            (
                "Increasing blank raster support while holding the embedded "
                "garment pixels fixed changed the frozen raster-relative "
                "spectral allocation in the preregistered direction."
            ),

        "interpretation":
            (
                "Raster support is a demonstrated dependency of the frozen "
                "historical raster-relative representation under the tested "
                "same-pixel intervention."
            ),

        "manuscript_safe_claim":
            (
                "In a controlled same-pixel intervention, increasing raster "
                "support systematically increased low-band allocation and "
                "decreased highmid/high allocation. All 23 category medians "
                "changed in the preregistered direction, with exact "
                "category-level sign-flip inference remaining supported "
                "after joint max-T familywise correction."
            ),

        "strength":
            "supported_controlled_dependency",

        "boundary":
            (
                "This demonstrates dependence under the tested frozen "
                "representation and intervention; it does not imply that "
                "raster support is the sole determinant of spectral behavior."
            ),
    },


    # -------------------------------------------------------------------------
    # M05 — matched intrinsic control
    # -------------------------------------------------------------------------

    {
        "claim_id":
            "M05",

        "section_role":
            "matched_object_relative_control",

        "source_result_ids":
            "R09",

        "observation":
            (
                "The object-relative field and band vectors remained "
                "exactly unchanged across all 16,100 support conditions."
            ),

        "interpretation":
            (
                "The tested support dependence arises from the historical "
                "raster-relative coordinate normalization and is absent "
                "under the matched object-relative normalization."
            ),

        "manuscript_safe_claim":
            (
                "Under the same support intervention, the matched "
                "object-relative representation was exactly invariant "
                "across all 16,100 conditions."
            ),

        "strength":
            "supported_matched_control",

        "boundary":
            (
                "This is invariance to the tested blank-support manipulation, "
                "not a claim of invariance to arbitrary image transformations."
            ),
    },


    # -------------------------------------------------------------------------
    # M06 — heterogeneity
    # -------------------------------------------------------------------------

    {
        "claim_id":
            "M06",

        "section_role":
            "heterogeneity_boundary",

        "source_result_ids":
            "R10;R12",

        "observation":
            (
                "Endpoint response was broad, but individual trajectories "
                "were frequently non-monotonic."
            ),

        "interpretation":
            (
                "The support dependency is systematic at population/category "
                "level without constituting a deterministic per-image law."
            ),

        "manuscript_safe_claim":
            (
                "The endpoint response was broad and category-consistent, "
                "although individual-image trajectories were often "
                "non-monotonic."
            ),

        "strength":
            "supported_boundary_statement",

        "boundary":
            (
                "Do not describe the intervention as universally monotonic "
                "for individual images."
            ),
    },
]


claims_df = pd.DataFrame(
    CLAIMS
)


# =============================================================================
# 5. Verify every manuscript claim points only to frozen D2 results
# =============================================================================

for _, row in claims_df.iterrows():

    ids = row[
        "source_result_ids"
    ].split(
        ";"
    )

    for result_id in ids:

        require(
            result_id in REQUIRED_RESULTS,
            (
                f"Claim {row['claim_id']} points to unknown "
                f"result ID {result_id}"
            ),
        )


# =============================================================================
# 6. Manuscript synthesis paragraph
#
# This paragraph is deliberately conservative.
# It contains no novelty statement and no external-generalization statement.
# =============================================================================

MANUSCRIPT_SYNTHESIS = (
    "Preprocessing ablation localized the historical high-frequency "
    "change primarily to the crop-only transition rather than to text "
    "removal or subsequent resize/pad processing. The retained garment "
    "pixels and source-coordinate centroid were unchanged by this crop, "
    "while garment occupancy relative to the raster changed substantially. "
    "Population-level analyses subsequently showed that the magnitude of "
    "raster-relative support change was associated with systematic spectral "
    "redistribution. To test this dependency directly, raster support was "
    "then manipulated while the embedded garment pixels were held fixed. "
    "Across the complete 2,300-image dataset, increasing blank support "
    "produced the preregistered directional response: low-band allocation "
    "increased whereas highmid and high allocation decreased. All 23 "
    "category medians agreed with these directions, and exact category-level "
    "sign-flip inference remained supported after joint max-T familywise "
    "correction. Under the same intervention, the matched object-relative "
    "representation was exactly invariant across all 16,100 support "
    "conditions. Together, these results demonstrate that raster support is "
    "a dependency of the frozen historical raster-relative representation "
    "under the tested same-pixel intervention, while also showing that the "
    "endpoint response is broad rather than universally monotonic at the "
    "individual-image level."
)


# =============================================================================
# 7. Short Results-style paragraph
# =============================================================================

RESULTS_PARAGRAPH = (
    "The support audit localized the high-band change to the crop-only "
    "transition and identified raster-relative garment extent as the "
    "strongest population-level correlate of spectral redistribution. "
    "A controlled same-pixel intervention then increased blank raster "
    "support without resizing, resampling, or altering the embedded garment "
    "pixels. At s=3, 91.5% of images increased in low-band allocation, "
    "89.5% decreased in highmid allocation, and 87.3% decreased in high "
    "allocation. All 23 category medians changed in the preregistered "
    "direction. Exact category-level sign-flip inference with joint max-T "
    "familywise correction supported the low, highmid, and high endpoint "
    "effects. In contrast, the matched object-relative representation "
    "remained exactly invariant across all 16,100 intervention conditions."
)


# =============================================================================
# 8. Discussion-style interpretation
# =============================================================================

DISCUSSION_PARAGRAPH = (
    "These findings indicate that the historical angular spectral "
    "allocation is not solely a property of the embedded garment geometry: "
    "it also depends on how that geometry is normalized relative to the "
    "raster support. The controlled intervention is important because the "
    "garment pixels themselves were unchanged; only surrounding blank "
    "support was altered. The matched object-relative control removes this "
    "specific support dependence under the tested intervention. However, "
    "the result should not be interpreted as a universal claim about Fourier "
    "descriptors or as evidence that support is the only source of spectral "
    "variation. Individual trajectories also remained heterogeneous and "
    "frequently non-monotonic."
)


# =============================================================================
# 9. Closure decision
# =============================================================================

CLOSURE = {

    "audit":
        "P2-R0-05K raster-support dependency audit",

    "decision":
        "CLOSED_FOR_CURRENT_SUPPORT_DEPENDENCE_QUESTION",

    "decision_basis": [

        (
            "05F localized the dominant high-band change to the "
            "crop/new-raster-support transition."
        ),

        (
            "05G showed that retained pixels and source-coordinate centroid "
            "were preserved while raster-relative geometry changed."
        ),

        (
            "05G/05J showed population-level association between "
            "raster-relative support change and spectral redistribution."
        ),

        (
            "05K2 and 05K3 reproduced the predicted intervention direction "
            "in sentinel and calibration stages."
        ),

        (
            "05K4 reproduced the preregistered endpoint direction over the "
            "complete 2,300-image dataset."
        ),

        (
            "All 23 category medians agreed with the primary directional "
            "hypotheses and exact category-level max-T inference supported "
            "all three directional bands."
        ),

        (
            "The matched object-relative representation remained exactly "
            "invariant across all 16,100 support conditions."
        ),
    ],

    "no_additional_support_only_experiment_required":
        True,

    "unresolved_but_nonblocking": [

        (
            "Why individual-image trajectories are frequently non-monotonic."
        ),

        (
            "Which garment-level geometric properties explain intervention "
            "response heterogeneity."
        ),

        (
            "Whether analogous support dependence appears in other datasets "
            "or other raster-relative descriptors."
        ),

        (
            "How the present finding relates to prior methodological "
            "literature and whether it contributes novelty."
        ),
    ],

    "future_work_status":
        (
            "Image-level heterogeneity may be investigated as a separate "
            "future study. It is not required to establish the current "
            "support-dependence result."
        ),

    "literature_status":
        (
            "NOT_ASSESSED_IN_D3. Literature integration and novelty "
            "assessment must be performed separately before manuscript "
            "novelty claims are written."
        ),
}


# =============================================================================
# 10. Prohibited manuscript statements
# =============================================================================

PROHIBITED = [

    {
        "id":
            "P01",

        "prohibited":
            (
                "Cropping changes the spectrum because interpolation "
                "destroys high-frequency information."
            ),

        "reason":
            (
                "05F falsified interpolation/resampling as the dominant "
                "transition; most change already occurred at crop-only."
            ),
    },

    {
        "id":
            "P02",

        "prohibited":
            (
                "Centroid instability caused the RAW→CROP spectral change."
            ),

        "reason":
            (
                "05G found zero centroid map-back error."
            ),
    },

    {
        "id":
            "P03",

        "prohibited":
            (
                "Border gradients caused the spectral redistribution."
            ),

        "reason":
            (
                "Border-gradient changes were descriptive and were not the "
                "strongest population-level support correlate."
            ),
    },

    {
        "id":
            "P04",

        "prohibited":
            (
                "Raster support completely explains spectral behavior."
            ),

        "reason":
            (
                "Observed associations were moderate and individual "
                "trajectories remained heterogeneous."
            ),
    },

    {
        "id":
            "P05",

        "prohibited":
            (
                "Every image responds monotonically to increasing support."
            ),

        "reason":
            (
                "Full image-level monotonicity occurred only in subsets "
                "of the population."
            ),
    },

    {
        "id":
            "P06",

        "prohibited":
            (
                "Object-relative normalization is invariant to all image "
                "transformations."
            ),

        "reason":
            (
                "Only the tested same-pixel support manipulation was audited."
            ),
    },

    {
        "id":
            "P07",

        "prohibited":
            (
                "This audit establishes a novel Fourier method."
            ),

        "reason":
            (
                "Novelty requires separate literature comparison and is "
                "outside the evidentiary scope of 05K."
            ),
    },
]


prohibited_df = pd.DataFrame(
    PROHIBITED
)


# =============================================================================
# 11. Closure matrix
# =============================================================================

CLOSURE_MATRIX = [

    {
        "question_id":
            "Q01",

        "question":
            "Where does the historical high-band change enter?",

        "status":
            "RESOLVED",

        "resolution":
            "Primarily at crop-only/new-raster-support transition.",

        "support":
            "05F2",
    },

    {
        "question_id":
            "Q02",

        "question":
            (
                "Are retained-pixel modification or centroid displacement "
                "required?"
            ),

        "status":
            "RESOLVED",

        "resolution":
            "No.",

        "support":
            "05G1",
    },

    {
        "question_id":
            "Q03",

        "question":
            (
                "Does raster-relative support change track spectral change "
                "at population scale?"
            ),

        "status":
            "RESOLVED_AS_ASSOCIATION",

        "resolution":
            "Yes.",

        "support":
            "05G2/05J",
    },

    {
        "question_id":
            "Q04",

        "question":
            (
                "Can support alone alter the historical raster-relative "
                "representation when garment pixels are fixed?"
            ),

        "status":
            "RESOLVED_BY_CONTROLLED_INTERVENTION",

        "resolution":
            "Yes.",

        "support":
            "05K2/05K3/05K4",
    },

    {
        "question_id":
            "Q05",

        "question":
            (
                "Is the full-population endpoint response supported at "
                "category-level inferential units?"
            ),

        "status":
            "RESOLVED",

        "resolution":
            "Yes for low, highmid, and high directional endpoints.",

        "support":
            "05K4-C",
    },

    {
        "question_id":
            "Q06",

        "question":
            (
                "Does the matched object-relative representation retain "
                "the same support dependence?"
            ),

        "status":
            "RESOLVED",

        "resolution":
            "No; exact invariance under tested support intervention.",

        "support":
            "05K4-C intrinsic control",
    },

    {
        "question_id":
            "Q07",

        "question":
            (
                "Are individual trajectories universally monotonic?"
            ),

        "status":
            "RESOLVED_NEGATIVE",

        "resolution":
            "No.",

        "support":
            "05K4-C",
    },

    {
        "question_id":
            "Q08",

        "question":
            (
                "Why do individual trajectories differ?"
            ),

        "status":
            "OPEN_NONBLOCKING",

        "resolution":
            (
                "Not explained by the current audit; separate "
                "heterogeneity question."
            ),

        "support":
            "Future work",
    },

    {
        "question_id":
            "Q09",

        "question":
            (
                "Is the support-dependence result methodologically novel "
                "relative to prior literature?"
            ),

        "status":
            "OPEN_REQUIRES_LITERATURE",

        "resolution":
            "Not assessed in 05K.",

        "support":
            "Literature review required",
    },
]


closure_df = pd.DataFrame(
    CLOSURE_MATRIX
)


# =============================================================================
# 12. Save outputs
# =============================================================================

CLAIMS_CSV = (
    OUT
    / "P2_R0_05K4_D3_manuscript_claim_ledger.csv"
)

CLOSURE_MATRIX_CSV = (
    OUT
    / "P2_R0_05K4_D3_closure_matrix.csv"
)

PROHIBITED_CSV = (
    OUT
    / "P2_R0_05K4_D3_prohibited_claims.csv"
)

CLOSURE_JSON = (
    OUT
    / "P2_R0_05K4_D3_closure_decision.json"
)

SYNTHESIS_MD = (
    OUT
    / "P2_R0_05K4_D3_manuscript_safe_synthesis.md"
)

REPORT_JSON = (
    OUT
    / "P2_R0_05K4_D3_report.json"
)


claims_df.to_csv(
    CLAIMS_CSV,
    index=False,
    lineterminator="\n",
)


closure_df.to_csv(
    CLOSURE_MATRIX_CSV,
    index=False,
    lineterminator="\n",
)


prohibited_df.to_csv(
    PROHIBITED_CSV,
    index=False,
    lineterminator="\n",
)


CLOSURE_JSON.write_text(
    json.dumps(
        CLOSURE,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


markdown = f"""# P2-R0-05K4-D3 — Manuscript-Safe Synthesis

## Status

**Support-dependence audit: CLOSED for the current internal question.**

No additional support-only experiment is required to establish the tested
dependency of the frozen historical raster-relative representation.

This closure does **not** establish external generalization or methodological
novelty.

---

## Core manuscript-safe synthesis

{MANUSCRIPT_SYNTHESIS}

---

## Results-style version

{RESULTS_PARAGRAPH}

---

## Discussion-style version

{DISCUSSION_PARAGRAPH}

---

## Supported core conclusion

{boundary["supported_core_conclusion"]}

---

## Matched control conclusion

{boundary["matched_control_conclusion"]}

---

## Heterogeneity boundary

{boundary["heterogeneity_boundary"]}

---

## Closure decision

**{CLOSURE["decision"]}**

No additional support-only experiment required:

**{CLOSURE["no_additional_support_only_experiment_required"]}**

---

## Unresolved but non-blocking questions

"""

for item in CLOSURE[
    "unresolved_but_nonblocking"
]:

    markdown += (
        f"- {item}\n"
    )


markdown += """

---

## Literature / novelty status

"""

markdown += (
    CLOSURE[
        "literature_status"
    ]
)

markdown += "\n"


SYNTHESIS_MD.write_text(
    markdown,
    encoding="utf-8",
)


report = {

    "stage":
        "P2_R0_05K4_D3_MANUSCRIPT_SAFE_SYNTHESIS_AND_CLOSURE",

    "status":
        "PASS_SUPPORT_AUDIT_CLOSED",

    "d2_frozen_inputs_verified":
        True,

    "manuscript_claim_count":
        int(
            len(
                claims_df
            )
        ),

    "closure_question_count":
        int(
            len(
                closure_df
            )
        ),

    "prohibited_claim_count":
        int(
            len(
                prohibited_df
            )
        ),

    "statistics_recomputed":
        False,

    "experiments_rerun":
        False,

    "thresholds_changed":
        False,

    "new_mechanism_test":
        False,

    "novelty_assessed":
        False,

    "literature_review_performed":
        False,

    "support_dependency_audit_closed":
        True,

    "additional_support_only_experiment_required":
        False,

    "heterogeneity_explained":
        False,

    "heterogeneity_is_blocking":
        False,

    "next_research_action":
        (
            "Literature comparison / manuscript integration. "
            "Treat image-level heterogeneity as optional separate work."
        ),
}


REPORT_JSON.write_text(
    json.dumps(
        report,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


# =============================================================================
# 13. Checksums
# =============================================================================

OUTPUTS = [

    CLAIMS_CSV,
    CLOSURE_MATRIX_CSV,
    PROHIBITED_CSV,
    CLOSURE_JSON,
    SYNTHESIS_MD,
    REPORT_JSON,

]


SUMS = (
    OUT
    / "SHA256SUMS.txt"
)


with SUMS.open(
    "w",
    encoding="utf-8",
) as f:

    for path in OUTPUTS:

        f.write(
            f"{sha256_file(path)}  "
            f"{path.name}\n"
        )


# =============================================================================
# 14. Final report
# =============================================================================

print()
print("=" * 122)
print(
    "P2-R0-05K4-D3 — "
    "MANUSCRIPT-SAFE SYNTHESIS AND CLOSURE: PASS"
)
print("=" * 122)

print()

print(
    "Manuscript claims:",
    len(
        claims_df
    ),
)

print(
    "Closure questions:",
    len(
        closure_df
    ),
)

print(
    "Prohibited claims:",
    len(
        prohibited_df
    ),
)


print()
print("CLOSURE MATRIX")

print(
    closure_df[
        [
            "question_id",
            "status",
            "resolution",
        ]
    ]
    .to_string(
        index=False
    )
)


print()
print("CORE CONCLUSION")

print(
    boundary[
        "supported_core_conclusion"
    ]
)


print()
print("MATCHED CONTROL")

print(
    boundary[
        "matched_control_conclusion"
    ]
)


print()
print("CLOSURE DECISION")

print(
    CLOSURE[
        "decision"
    ]
)


print()
print(
    "Additional support-only experiment required:",
    CLOSURE[
        "no_additional_support_only_experiment_required"
    ]
    is False,
)


print()
print("LITERATURE / NOVELTY")

print(
    CLOSURE[
        "literature_status"
    ]
)


print()
print("OUTPUT HASHES")

for path in OUTPUTS:

    print(
        path.name,
        sha256_file(
            path
        ),
    )


print(
    "SHA256SUMS.txt",
    sha256_file(
        SUMS
    ),
)


print()
print("Statistics recomputed            : NO")
print("Experiments rerun                 : NO")
print("New support mechanism test        : NO")
print("Novelty assessed                  : NO")
print("Literature review performed       : NO")
print("Support-dependence audit closed   : YES")
print("Heterogeneity remains unexplained : YES")
print("Heterogeneity blocks closure      : NO")


print()
print("=" * 122)
print(
    "STOP — FREEZE D3. "
    "NEXT SCIENTIFIC STEP IS LITERATURE/MANUSCRIPT INTEGRATION, "
    "NOT ANOTHER SUPPORT EXPERIMENT."
)
print("=" * 122)