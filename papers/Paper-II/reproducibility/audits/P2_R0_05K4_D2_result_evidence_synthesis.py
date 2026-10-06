from pathlib import Path
import hashlib
import json

import pandas as pd


# =============================================================================
# P2-R0-05K4-D2
# RESULT-LEVEL EVIDENCE SYNTHESIS
#
# PURPOSE
#   Construct a manuscript-facing evidence ledger from already established
#   and source-locked results spanning 05F → 05G → 05J → 05K.
#
# THIS STAGE DOES NOT:
#   - rerun an experiment
#   - recompute statistics
#   - change thresholds
#   - select favorable results
#   - introduce new hypotheses
#   - claim novelty
#
# Every result below:
#   1. was already produced in an earlier frozen/audited stage,
#   2. is bound to an exact source artifact + SHA-256,
#   3. is assigned an explicit evidence class,
#   4. records both supported and prohibited interpretations.
#
# CORE STRUCTURE
#
#   Observation
#       ↓
#   Evidence class
#       ↓
#   Interpretation
#       ↓
#   Supports
#       ↓
#   Does NOT support
#       ↓
#   Remaining gap
#       ↓
#   Manuscript-safe wording
# =============================================================================


REPO = Path(
    "/Users/nitikagupta/Research/WeaveAI"
)

RESEARCH = Path(
    "/Users/nitikagupta/Research"
)

AUDITS = (
    REPO
    / "papers/Paper-II/reproducibility/audits"
)

FROZEN = (
    REPO
    / "papers/Paper-II/reproducibility/frozen"
)

OUT = (
    AUDITS
    / "05K4_D2_result_evidence_synthesis"
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
# 1. Lock D1 itself before interpreting any result
# =============================================================================

D1_DIR = (
    FROZEN
    / "05K4_D1_Authoritative_Evidence_Source_Ledger_v1_0"
)

D1_LEDGER = (
    D1_DIR
    / "P2_R0_05K4_D1_authoritative_source_ledger.csv"
)

D1_HIERARCHY = (
    D1_DIR
    / "P2_R0_05K4_D1_evidence_hierarchy.csv"
)

D1_CLAIMS = (
    D1_DIR
    / "P2_R0_05K4_D1_claim_boundary_ledger.csv"
)

D1_REPORT = (
    D1_DIR
    / "P2_R0_05K4_D1_report.json"
)


EXPECTED_D1_SHA = {
    "ledger":
        "3b41db8b878bec944a6baba4a69b0cd2eac779e1d6930ebad70729e141a05a36",

    "hierarchy":
        "369071314fe38850777418099bcd49a45a97aa29f5f0ea1c7a40b4943b77765a",

    "claims":
        "185c9cb553dd89dac7e670f0a1b0a4ebb1886a67cefd870dc999805fd1e4ae26",

    "report":
        "3b7b0be4b0dbde438ce40d40abed363299fcd9bcb9d18c3f8b792e74343a0ceb",
}


for label, path in [
    ("ledger", D1_LEDGER),
    ("hierarchy", D1_HIERARCHY),
    ("claims", D1_CLAIMS),
    ("report", D1_REPORT),
]:

    require(
        path.is_file(),
        f"Missing frozen D1 artifact: {path}",
    )

    observed = sha256_file(
        path
    )

    require(
        observed
        == EXPECTED_D1_SHA[
            label
        ],
        (
            f"D1 {label} SHA mismatch\n"
            f"expected={EXPECTED_D1_SHA[label]}\n"
            f"observed={observed}"
        ),
    )


d1 = pd.read_csv(
    D1_LEDGER,
    keep_default_na=False,
)


require(
    len(d1) == 25,
    f"Expected 25 D1 locked sources; got {len(d1)}",
)


# =============================================================================
# 2. Authoritative source registry
#
# These are already D1-verified. D2 verifies them again because every
# result row below explicitly depends on one or more of them.
# =============================================================================

SOURCE = {

    "05F2_LOG": {
        "path":
            AUDITS
            / "05K4_D0_2_05F_replay_capture"
            / "P2_R0_05F2_replay_full_log.txt",

        "sha256":
            "8208e3d7674d221e159919b1525c7c7c09e725315f707f3d254da530b8e96ff5",
    },


    "05G1_METRICS": {
        "path":
            RESEARCH
            / "paper2_r0_05g_frame_border_gradient"
            / "P2_R0_05G1_frame_border_gradient_metrics.csv",

        "sha256":
            "d40b052db1ca17b5f91d2a20cb57caa9d66930a53b341eb80804a292fa75c055",
    },


    "05G2_ASSOC": {
        "path":
            RESEARCH
            / "paper2_r0_05g_frame_border_gradient"
            / "P2_R0_05G2_mechanism_associations.csv",

        "sha256":
            "f632a572ec9c5b5f0102bd884178469ebd2774e178ac83c083423fc6ba4a6faf",
    },


    "05J_METRICS": {
        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_per_image_population_metrics.csv",

        "sha256":
            "f667d8850c43001f1ee251bc2c14f18765a5289c0ebf8e8be42b972e03f6995a",
    },


    "05J_ASSOC": {
        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_associations.csv",

        "sha256":
            "5c9a584ea5bca6ba4159f089722a5982ae120f8c1083675c11e06e805cd9fc6e",
    },


    "05J_STRATA": {
        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_support_change_strata.csv",

        "sha256":
            "bc6ecf96c0e9674daa419c6b06ad6147d477e6168fb5ef3eb3bd95d630b53eb3",
    },


    "05J_CATEGORY": {
        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_category_summary.csv",

        "sha256":
            "a15f0c94a48b4e6a476c58bc8a1131a0bdcdeb3cc60d195363c595fd7711f66f",
    },


    "05K2_REPORT": {
        "path":
            FROZEN
            / "05K2_B2_Sentinel_Trajectory_Analysis_v1_0"
            / "P2_R0_05K2_B2_report.json",

        "sha256":
            "46383baa02a7c33c55e5ec65e32c38493cfd5e8e0f32df58cc19501a3a073f18",
    },


    "05K3_REPORT": {
        "path":
            FROZEN
            / "05K3_D_Calibration_Trajectory_Analysis_v1_0"
            / "P2_R0_05K3_D_report.json",

        "sha256":
            "4ad144a58f16149c69374843e5bbd8197a9710b111296557b33fbcd42b6c8c8b",
    },


    "05K3_CATEGORY": {
        "path":
            FROZEN
            / "05K3_D_Calibration_Trajectory_Analysis_v1_0"
            / "P2_R0_05K3_D_category_endpoint_summary_23.csv",

        "sha256":
            "60fdf63ccdd7fbe2686914580759b4c2e0819a2ad5bf32171103681fad950573",
    },


    "05K4_IMAGE": {
        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_per_image_endpoint_summary_2300.csv",

        "sha256":
            "ee2993069e3a3b062e411dc9acbedda81039eb33aee3993a100908a12fe27e19",
    },


    "05K4_SUPPORT": {
        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_support_level_descriptive_summary.csv",

        "sha256":
            "f8bfc45ec6fd0f4a156b7e20db66bd476e3c19e2bdfe5ba91c2fdb98166b0b93",
    },


    "05K4_CATEGORY": {
        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_category_endpoint_effects_23.csv",

        "sha256":
            "91f549289f95bc0beae723c66a2ed4d71169c63f4894200345376ac2d397dc41",
    },


    "05K4_INFERENCE": {
        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_exact_category_signflip_inference.csv",

        "sha256":
            "a378b36f457fced975967f75cfb229e9a6b8798fcafd649e93f97f948727bde7",
    },


    "05K4_REPORT": {
        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_report.json",

        "sha256":
            "9bd7a370176dd805681e377e3f2cdfcb3f06d6ea24c7619c735d26cad1a53e6b",
    },
}


print("=" * 120)
print(
    "P2-R0-05K4-D2 — "
    "RESULT-LEVEL EVIDENCE SYNTHESIS"
)
print("=" * 120)

print()
print("Verifying authoritative result sources...")


for key, spec in SOURCE.items():

    path = Path(
        spec[
            "path"
        ]
    )

    require(
        path.is_file(),
        f"Missing source {key}: {path}",
    )

    observed = sha256_file(
        path
    )

    require(
        observed
        == spec[
            "sha256"
        ],
        (
            f"{key} SHA mismatch\n"
            f"expected={spec['sha256']}\n"
            f"observed={observed}"
        ),
    )

    print(
        f"{key:16s}",
        "PASS",
    )


# =============================================================================
# 3. Verify the archived 05F2 replay contains the exact historical results
# =============================================================================

f2_text = (
    SOURCE[
        "05F2_LOG"
    ][
        "path"
    ]
    .read_text(
        encoding="utf-8"
    )
)


required_05f_lines = [

    "P2-R0-05F2 CROP-VS-RESAMPLING REPLAY: COMPLETE",

    "TEXT_ONLY - RAW: 0.005416511203638084",

    "CROP_ONLY - RAW: -0.039142530431528634",

    "LOCALIZE_ONLY - CROP_ONLY: -0.00015726993533439436",

    "CLEAN - LOCALIZE_ONLY: -0.00010457326556180406",
]


for line in required_05f_lines:

    require(
        line in f2_text,
        (
            "Expected 05F2 replay result absent:\n"
            f"{line}"
        ),
    )


# =============================================================================
# 4. Result evidence ledger
#
# Numerical results below were already established in the source stages.
# D2 records them; it does not calculate them.
# =============================================================================

RESULTS = [

    # -------------------------------------------------------------------------
    # R01 — preprocessing localization
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R01",

        "stage":
            "05F2",

        "observation":
            (
                "The high-band effect changes little after text-only "
                "blanking, but drops substantially at the crop-only "
                "transition."
            ),

        "numerical_evidence":
            (
                "TEXT_ONLY−RAW = +0.0054165112; "
                "CROP_ONLY−RAW = −0.0391425304; "
                "LOCALIZE_ONLY−CROP_ONLY = −0.0001572699; "
                "CLEAN−LOCALIZE_ONLY = −0.0001045733."
            ),

        "evidence_class":
            "preprocessing_ablation",

        "interpretation":
            (
                "The dominant high-band change enters when the "
                "raster is cropped/reframed, not during text removal "
                "and not during the later resize/pad component."
            ),

        "supports":
            (
                "Localization of the instability to the crop/new-raster-"
                "support transition."
            ),

        "does_not_support":
            (
                "Does not identify the precise geometric mechanism and "
                "does not establish interpolation as the cause."
            ),

        "remaining_gap":
            (
                "Determine which property of the changed raster support "
                "tracks the spectral redistribution."
            ),

        "manuscript_safe_wording":
            (
                "A preprocessing ablation localized the high-band change "
                "primarily to the crop-only transition; subsequent "
                "resize/pad processing produced negligible additional "
                "change."
            ),

        "source_keys":
            "05F2_LOG",
    },


    # -------------------------------------------------------------------------
    # R02 — same crop pixels / centroid
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R02",

        "stage":
            "05G1",

        "observation":
            (
                "The crop contained the exact retained RAW garment "
                "pixels and mapped its foreground centroid back to the "
                "RAW frame with zero error."
            ),

        "numerical_evidence":
            (
                "Maximum centroid map-back error = 0.0; retained crop "
                "intensities unchanged."
            ),

        "evidence_class":
            "descriptive_geometry",

        "interpretation":
            (
                "Cropping did not alter retained pixel intensities or "
                "the garment centroid in source coordinates."
            ),

        "supports":
            (
                "Rules out retained-pixel modification and centroid "
                "movement as necessary explanations for the observed "
                "RAW→CROP spectral change."
            ),

        "does_not_support":
            (
                "Centroid invariance does not imply spectral invariance "
                "because the representation also depends on raster-relative "
                "coordinates."
            ),

        "remaining_gap":
            (
                "Quantify how garment extent relative to raster support "
                "changes after cropping."
            ),

        "manuscript_safe_wording":
            (
                "The retained crop pixels and source-coordinate centroid "
                "were unchanged, indicating that centroid displacement or "
                "pixel modification was not required for the spectral shift."
            ),

        "source_keys":
            "05G1_METRICS",
    },


    # -------------------------------------------------------------------------
    # R03 — raster/support geometry changes substantially
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R03",

        "stage":
            "05G1",

        "observation":
            (
                "Cropping substantially changed foreground occupancy and "
                "frame-relative image geometry."
            ),

        "numerical_evidence":
            (
                "Median crop area fraction = 0.2559; "
                "RAW foreground fraction = 0.02293; "
                "CROP foreground fraction = 0.09448; "
                "radius/grid ratio median 0.92886→0.92238; "
                "gradient mean 0.03476→0.14179; "
                "border-gradient fraction 0.00066→0.07234."
            ),

        "evidence_class":
            "descriptive_geometry",

        "interpretation":
            (
                "The crop changes how the same garment content occupies "
                "the raster frame."
            ),

        "supports":
            "A raster-support mechanism is geometrically plausible.",

        "does_not_support":
            (
                "Gradient concentration or border-gradient change alone "
                "cannot be labeled causal from these descriptives."
            ),

        "remaining_gap":
            (
                "Test which frame-relative descriptors actually track "
                "spectral change across images."
            ),

        "manuscript_safe_wording":
            (
                "Cropping markedly altered garment occupancy and "
                "frame-relative geometry despite preserving retained "
                "garment pixels."
            ),

        "source_keys":
            "05G1_METRICS",
    },


    # -------------------------------------------------------------------------
    # R04 — 05G2 associations
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R04",

        "stage":
            "05G2",

        "observation":
            (
                "Among the tested frame/support descriptors, change in "
                "foreground radius relative to grid radius showed the "
                "strongest surviving association with high-frequency "
                "spectral change."
            ),

        "numerical_evidence":
            (
                "Category-centered rho for Δ high fraction = +0.268988, "
                "p=0.000200, q=0.002200; "
                "rho for Δ log high energy = +0.290318, "
                "p=0.000100, q=0.001650."
            ),

        "evidence_class":
            "observational_association",

        "interpretation":
            (
                "The instability tracks radial scale relative to raster "
                "support more strongly than centroid displacement or "
                "border-gradient change."
            ),

        "supports":
            (
                "Prioritizes raster-relative radial support as a candidate "
                "mechanism for controlled testing."
            ),

        "does_not_support":
            "Association does not establish causation.",

        "remaining_gap":
            (
                "Confirm the association in the full population using "
                "a more robust support descriptor."
            ),

        "manuscript_safe_wording":
            (
                "Exploratory association analysis implicated garment "
                "extent relative to raster support as the strongest "
                "candidate descriptor of the spectral redistribution."
            ),

        "source_keys":
            "05G2_ASSOC",
    },


    # -------------------------------------------------------------------------
    # R05 — 05J robust population association
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R05",

        "stage":
            "05J",

        "observation":
            (
                "Across all 2,300 images, crop-induced change in robust "
                "q99 radius relative to grid size was associated with "
                "systematic redistribution across the four bands."
            ),

        "numerical_evidence":
            (
                "Δq99/grid associations: "
                "low rho = −0.332738; "
                "mid rho = −0.155208; "
                "highmid rho = +0.345008; "
                "high rho = +0.257411; "
                "all reported q = 0.000150."
            ),

        "evidence_class":
            "population_observational_association",

        "interpretation":
            (
                "Larger crop-induced changes in raster-relative garment "
                "extent are associated with reduced low/mid allocation "
                "and increased highmid/high allocation."
            ),

        "supports":
            (
                "A population-wide relationship between raster-relative "
                "support change and spectral redistribution."
            ),

        "does_not_support":
            (
                "The association is not deterministic and does not by "
                "itself establish that support change causes the spectral "
                "redistribution."
            ),

        "remaining_gap":
            (
                "Directly manipulate raster support while holding garment "
                "pixels unchanged."
            ),

        "manuscript_safe_wording":
            (
                "At population scale, the magnitude of crop-induced "
                "raster-relative support change was associated with "
                "redistribution from lower toward higher angular-frequency "
                "bands."
            ),

        "source_keys":
            "05J_ASSOC;05J_METRICS",
    },


    # -------------------------------------------------------------------------
    # R06 — 05J strata/category breadth
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R06",

        "stage":
            "05J",

        "observation":
            (
                "Images with larger support change showed larger spectral "
                "redistribution, and all 23 category medians showed positive "
                "RAW→CROP high-band change."
            ),

        "numerical_evidence":
            (
                "Q1 vs Q4 Δq99/grid: 0.062476 vs 0.483714; "
                "Δlow +0.012615 vs −0.018741; "
                "Δhighmid +0.005523 vs +0.027711; "
                "Δhigh +0.013246 vs +0.041898; "
                "L1 0.127022 vs 0.160238. "
                "23/23 category median Δhigh positive."
            ),

        "evidence_class":
            "population_descriptive_stratification",

        "interpretation":
            (
                "The observational relationship is broadly distributed "
                "rather than confined to a small number of categories."
            ),

        "supports":
            "Breadth of the association across the dataset.",

        "does_not_support":
            "Still does not provide intervention-based causal evidence.",

        "remaining_gap":
            "Controlled same-pixel support intervention.",

        "manuscript_safe_wording":
            (
                "Support-change strata and category summaries indicated "
                "that the association was broadly distributed across "
                "garment classes."
            ),

        "source_keys":
            "05J_STRATA;05J_CATEGORY",
    },


    # -------------------------------------------------------------------------
    # R07 — sentinel intervention
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R07",

        "stage":
            "05K2-B2",

        "observation":
            (
                "In ten preregistered diagnostic sentinels, enlarging "
                "blank raster support while keeping the embedded garment "
                "pixels unchanged generally produced the inverse spectral "
                "direction to crop tightening."
            ),

        "numerical_evidence":
            (
                "At s=3 endpoint concordance: "
                "low 8/10; highmid 9/10; high 8/10. "
                "Full-trajectory monotonicity: "
                "low 5/10; highmid 6/10; high 4/10."
            ),

        "evidence_class":
            "controlled_intervention_diagnostic",

        "interpretation":
            (
                "A support-only intervention is capable of changing the "
                "historical raster-relative spectrum in the predicted "
                "opposite direction."
            ),

        "supports":
            (
                "Feasibility and direction of the controlled support "
                "intervention."
            ),

        "does_not_support":
            (
                "Ten sentinels are not population evidence and do not "
                "establish universal monotonic trajectories."
            ),

        "remaining_gap":
            "Scale the intervention beyond diagnostic sentinels.",

        "manuscript_safe_wording":
            (
                "Diagnostic same-pixel support interventions showed the "
                "predicted inverse endpoint direction while also revealing "
                "substantial image-level trajectory heterogeneity."
            ),

        "source_keys":
            "05K2_REPORT",
    },


    # -------------------------------------------------------------------------
    # R08 — calibration intervention
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R08",

        "stage":
            "05K3-D",

        "observation":
            (
                "The 230-case deterministic calibration reproduced the "
                "support-intervention direction broadly across images and "
                "all categories."
            ),

        "numerical_evidence":
            (
                "s=3 endpoint concordance: "
                "low 208/230 (90.4%); "
                "highmid 200/230 (87.0%); "
                "high 194/230 (84.3%). "
                "Category medians: 23/23 in the predicted direction "
                "for low, highmid, and high."
            ),

        "evidence_class":
            "controlled_intervention_calibration",

        "interpretation":
            (
                "The sentinel behavior extends to a substantially broader "
                "deterministic calibration set."
            ),

        "supports":
            (
                "Justifies full-population execution of the preregistered "
                "support intervention."
            ),

        "does_not_support":
            (
                "The lexicographically selected calibration set is not a "
                "random representative sample and was not used for "
                "population inference."
            ),

        "remaining_gap":
            "Execute the intervention over all 2,300 images.",

        "manuscript_safe_wording":
            (
                "A 230-case calibration reproduced the predicted endpoint "
                "direction across all 23 garment categories, motivating "
                "full-population evaluation."
            ),

        "source_keys":
            "05K3_REPORT;05K3_CATEGORY",
    },


    # -------------------------------------------------------------------------
    # R09 — exact intrinsic control
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R09",

        "stage":
            "05K4-C",

        "observation":
            (
                "The object-relative representation remained exactly "
                "unchanged under every primary support intervention."
            ),

        "numerical_evidence":
            (
                "Intrinsic field exact 16,100/16,100; "
                "intrinsic bands exact 16,100/16,100; "
                "maximum field difference = 0.0; "
                "maximum band difference = 0.0."
            ),

        "evidence_class":
            "controlled_primary_intervention_control",

        "interpretation":
            (
                "Removing raster-grid dependence through object-relative "
                "coordinates eliminates the tested support sensitivity."
            ),

        "supports":
            (
                "The observed dependence is representation-specific and "
                "is absent under the tested object-relative normalization."
            ),

        "does_not_support":
            (
                "Does not imply universal invariance of the object-relative "
                "representation to arbitrary transformations."
            ),

        "remaining_gap":
            (
                "None for the tested support-only intervention; broader "
                "transformational robustness remains outside this audit."
            ),

        "manuscript_safe_wording":
            (
                "The matched object-relative representation was exactly "
                "invariant to all 16,100 support conditions."
            ),

        "source_keys":
            "05K4_REPORT",
    },


    # -------------------------------------------------------------------------
    # R10 — primary image-level endpoint breadth
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R10",

        "stage":
            "05K4-C",

        "observation":
            (
                "Across the full 2,300-image intervention, most images "
                "changed in the preregistered endpoint direction."
            ),

        "numerical_evidence":
            (
                "low increase 2104/2300 (91.5%); "
                "highmid decrease 2059/2300 (89.5%); "
                "high decrease 2008/2300 (87.3%)."
            ),

        "evidence_class":
            "controlled_primary_intervention_descriptive",

        "interpretation":
            (
                "The endpoint response is broad at image level."
            ),

        "supports":
            (
                "Broad response to the support-only intervention."
            ),

        "does_not_support":
            (
                "Image rows are not treated as independent inferential "
                "units."
            ),

        "remaining_gap":
            (
                "Use category-level inferential units to evaluate the "
                "preregistered directional endpoint."
            ),

        "manuscript_safe_wording":
            (
                "At the image level, the preregistered endpoint direction "
                "was observed in approximately 87–92% of sketches across "
                "the three directional bands."
            ),

        "source_keys":
            "05K4_IMAGE",
    },


    # -------------------------------------------------------------------------
    # R11 — population/category primary inference
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R11",

        "stage":
            "05K4-C",

        "observation":
            (
                "All 23 category median endpoint effects agreed with the "
                "preregistered support-enlargement direction, with exact "
                "category-level sign-flip support after joint max-T "
                "familywise correction."
            ),

        "numerical_evidence":
            (
                "Category concordance: 23/23 for all three tested bands. "
                "Median category effects: "
                "low +0.052497; "
                "highmid −0.035074; "
                "high −0.046223. "
                "Exact max-T FWER p: "
                "low 1.430511e−06; "
                "highmid 1.192093e−07; "
                "high 1.192093e−07."
            ),

        "evidence_class":
            "controlled_primary_intervention_inference",

        "interpretation":
            (
                "Changing raster support alone, with embedded garment "
                "pixels fixed, produces a systematic directional change "
                "in the historical raster-relative spectral representation."
            ),

        "supports":
            (
                "Dependence of the frozen historical representation on "
                "raster support under the tested intervention."
            ),

        "does_not_support":
            (
                "Does not establish that raster support is the only source "
                "of spectral variation, and does not justify external-"
                "population generalization."
            ),

        "remaining_gap":
            (
                "Scientific synthesis with the earlier observational and "
                "localization evidence; no additional support experiment "
                "is required to establish the tested dependency."
            ),

        "manuscript_safe_wording":
            (
                "In the full same-pixel intervention, all 23 category "
                "medians changed in the preregistered direction, with "
                "exact category-level sign-flip inference remaining "
                "supported after joint max-T familywise correction."
            ),

        "source_keys":
            "05K4_CATEGORY;05K4_INFERENCE",
    },


    # -------------------------------------------------------------------------
    # R12 — aggregate graded response vs individual heterogeneity
    # -------------------------------------------------------------------------

    {
        "result_id":
            "R12",

        "stage":
            "05K4-C",

        "observation":
            (
                "Aggregate median spectral displacement increased across "
                "support levels, but individual-image trajectories were "
                "frequently non-monotonic."
            ),

        "numerical_evidence":
            (
                "Median four-band L1 from s=1: "
                "0.000000, 0.045464, 0.072890, 0.099140, "
                "0.132808, 0.157245, 0.179920 for "
                "s=1.00,1.10,1.25,1.50,2.00,2.50,3.00. "
                "Individual monotonicity: "
                "low 1171/2300 (50.9%); "
                "highmid 1015/2300 (44.1%); "
                "high 869/2300 (37.8%); "
                "L1 nondecreasing 1296/2300 (56.3%)."
            ),

        "evidence_class":
            "controlled_primary_intervention_descriptive",

        "interpretation":
            (
                "The population-level response is graded in aggregate, "
                "while local image-level trajectories remain heterogeneous."
            ),

        "supports":
            (
                "Aggregate support sensitivity together with substantial "
                "per-image heterogeneity."
            ),

        "does_not_support":
            (
                "Does not support a deterministic monotonic law for every "
                "garment image."
            ),

        "remaining_gap":
            (
                "Heterogeneity could be studied separately, but it is not "
                "required for the current support-dependence conclusion."
            ),

        "manuscript_safe_wording":
            (
                "Median displacement increased progressively with added "
                "support, although individual trajectories were often "
                "non-monotonic."
            ),

        "source_keys":
            "05K4_SUPPORT;05K4_IMAGE",
    },
]


# =============================================================================
# 5. Bind each result to exact sources
# =============================================================================

rows = []


for result in RESULTS:

    source_keys = (
        result[
            "source_keys"
        ]
        .split(
            ";"
        )
    )


    source_paths = []
    source_hashes = []


    for key in source_keys:

        require(
            key in SOURCE,
            f"Unknown source key in result {result['result_id']}: {key}",
        )


        source_paths.append(
            str(
                SOURCE[
                    key
                ][
                    "path"
                ]
            )
        )


        source_hashes.append(
            SOURCE[
                key
            ][
                "sha256"
            ]
        )


    rows.append({
        **result,

        "source_paths":
            " ; ".join(
                source_paths
            ),

        "source_sha256":
            " ; ".join(
                source_hashes
            ),
    })


ledger = pd.DataFrame(
    rows
)


require(
    ledger[
        "result_id"
    ].is_unique,
    "Result IDs are not unique",
)


# =============================================================================
# 6. Evidence-chain summary
# =============================================================================

CHAIN = [

    {
        "chain_step":
            1,

        "stage":
            "05F2",

        "question":
            "Where does the high-band change enter?",

        "answer_status":
            "SUPPORTED",

        "answer":
            (
                "Primarily at the crop-only/new-raster-support transition."
            ),

        "evidence_class":
            "preprocessing_ablation",
    },

    {
        "chain_step":
            2,

        "stage":
            "05G1",

        "question":
            "What changes geometrically?",

        "answer_status":
            "SUPPORTED",

        "answer":
            (
                "Frame-relative garment occupancy/support geometry changes "
                "while retained crop pixels and source-coordinate centroid "
                "remain unchanged."
            ),

        "evidence_class":
            "descriptive_geometry",
    },

    {
        "chain_step":
            3,

        "stage":
            "05G2/05J",

        "question":
            (
                "Does the magnitude of raster-relative support change "
                "track spectral redistribution?"
            ),

        "answer_status":
            "SUPPORTED_AS_ASSOCIATION",

        "answer":
            (
                "Yes. Robust raster-relative extent change is associated "
                "with systematic band redistribution at population scale."
            ),

        "evidence_class":
            "observational_association",
    },

    {
        "chain_step":
            4,

        "stage":
            "05K2/05K3",

        "question":
            (
                "Does directly changing support with garment pixels held "
                "fixed produce the predicted response?"
            ),

        "answer_status":
            "SUPPORTED_DESCRIPTIVELY",

        "answer":
            (
                "Yes in sentinel and calibration interventions, with "
                "substantial individual trajectory heterogeneity."
            ),

        "evidence_class":
            "controlled_intervention_calibration",
    },

    {
        "chain_step":
            5,

        "stage":
            "05K4-C",

        "question":
            (
                "Does the support-only intervention remain supported over "
                "the complete 2,300-image dataset?"
            ),

        "answer_status":
            "SUPPORTED_WITH_PRIMARY_INFERENCE",

        "answer":
            (
                "Yes. All 23 category medians agree with the preregistered "
                "direction and exact joint sign-flip inference supports "
                "all three tested bands."
            ),

        "evidence_class":
            "controlled_primary_intervention",
    },

    {
        "chain_step":
            6,

        "stage":
            "05K4-C_INTRINSIC_CONTROL",

        "question":
            (
                "Does the same support intervention affect an object-relative "
                "version of the representation?"
            ),

        "answer_status":
            "NO_CHANGE_OBSERVED",

        "answer":
            (
                "No. The intrinsic field and band vectors are exactly "
                "invariant across all 16,100 support conditions."
            ),

        "evidence_class":
            "matched_intervention_control",
    },
]


chain_df = pd.DataFrame(
    CHAIN
)


# =============================================================================
# 7. Final synthesis boundary
# =============================================================================

SYNTHESIS_BOUNDARY = {

    "supported_core_conclusion":
        (
            "Under the frozen historical raster-relative coordinate "
            "normalization, raster support is a demonstrated dependency "
            "of angular spectral allocation in the tested dataset and "
            "same-pixel support intervention."
        ),

    "matched_control_conclusion":
        (
            "The tested object-relative normalization eliminates this "
            "support dependence exactly under the same intervention."
        ),

    "heterogeneity_boundary":
        (
            "The endpoint effect is broad and category-consistent, but "
            "individual trajectories are not universally monotonic."
        ),

    "prohibited_claims": [

        (
            "Raster support is the sole determinant of angular spectral "
            "behavior."
        ),

        (
            "Every image changes monotonically with increasing support."
        ),

        (
            "All Fourier or shape descriptors are inherently canvas-sensitive."
        ),

        (
            "The object-relative representation is invariant to arbitrary "
            "transformations."
        ),

        (
            "The results automatically generalize beyond the tested dataset "
            "and frozen implementation."
        ),

        (
            "The support audit by itself establishes methodological novelty."
        ),
    ],

    "remaining_scientific_gap":
        (
            "The tested dependency is established for the frozen representation. "
            "Residual image-level heterogeneity remains unexplained, but resolving "
            "that heterogeneity is not necessary for the current support-dependence "
            "claim."
        ),
}


# =============================================================================
# 8. Save
# =============================================================================

LEDGER_CSV = (
    OUT
    / "P2_R0_05K4_D2_result_evidence_ledger.csv"
)

CHAIN_CSV = (
    OUT
    / "P2_R0_05K4_D2_evidence_chain.csv"
)

BOUNDARY_JSON = (
    OUT
    / "P2_R0_05K4_D2_synthesis_boundary.json"
)

REPORT_JSON = (
    OUT
    / "P2_R0_05K4_D2_report.json"
)


ledger.to_csv(
    LEDGER_CSV,
    index=False,
    lineterminator="\n",
)


chain_df.to_csv(
    CHAIN_CSV,
    index=False,
    lineterminator="\n",
)


BOUNDARY_JSON.write_text(
    json.dumps(
        SYNTHESIS_BOUNDARY,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


report = {

    "stage":
        "P2_R0_05K4_D2_RESULT_EVIDENCE_SYNTHESIS",

    "status":
        "PASS_RESULT_LEVEL_SYNTHESIS",

    "result_count":
        int(
            len(
                ledger
            )
        ),

    "chain_steps":
        int(
            len(
                chain_df
            )
        ),

    "all_sources_sha_verified":
        True,

    "d1_source_lock_verified":
        True,

    "statistics_recomputed":
        False,

    "experiments_rerun":
        False,

    "thresholds_changed":
        False,

    "new_hypotheses_added":
        False,

    "novelty_claim_made":
        False,

    "mechanism_scope":
        (
            "Support dependence under the frozen raster-relative "
            "coordinate normalization and tested same-pixel intervention."
        ),

    "next_stage":
        (
            "05K4-D3: freeze manuscript-safe synthesis and decide whether "
            "the mechanism audit is closed or whether a separate "
            "heterogeneity study is scientifically necessary."
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
# 9. Checksums
# =============================================================================

OUTPUTS = [
    LEDGER_CSV,
    CHAIN_CSV,
    BOUNDARY_JSON,
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
# 10. Final
# =============================================================================

print()
print("=" * 120)
print(
    "P2-R0-05K4-D2 — "
    "RESULT-LEVEL EVIDENCE SYNTHESIS: PASS"
)
print("=" * 120)

print(
    "Result records:",
    len(
        ledger
    ),
)

print(
    "Evidence-chain steps:",
    len(
        chain_df
    ),
)

print()


print("RESULT LEDGER")

print(
    ledger[
        [
            "result_id",
            "stage",
            "evidence_class",
            "remaining_gap",
        ]
    ]
    .to_string(
        index=False
    )
)


print()
print("EVIDENCE CHAIN")

print(
    chain_df[
        [
            "chain_step",
            "stage",
            "answer_status",
            "answer",
        ]
    ]
    .to_string(
        index=False
    )
)


print()
print("CORE SYNTHESIS BOUNDARY")

print(
    SYNTHESIS_BOUNDARY[
        "supported_core_conclusion"
    ]
)

print()
print("MATCHED CONTROL")

print(
    SYNTHESIS_BOUNDARY[
        "matched_control_conclusion"
    ]
)

print()
print("HETEROGENEITY BOUNDARY")

print(
    SYNTHESIS_BOUNDARY[
        "heterogeneity_boundary"
    ]
)


print()
print("PROHIBITED OVERCLAIMS")

for i, claim in enumerate(
    SYNTHESIS_BOUNDARY[
        "prohibited_claims"
    ],
    start=1,
):

    print(
        f"{i}. {claim}"
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
print("Statistics recomputed : NO")
print("Experiments rerun      : NO")
print("Threshold changed      : NO")
print("New hypotheses         : NO")
print("Novelty claim          : NO")

print()
print("=" * 120)
print(
    "STOP — FREEZE D2 BEFORE MANUSCRIPT-SAFE SYNTHESIS"
)
print("=" * 120)