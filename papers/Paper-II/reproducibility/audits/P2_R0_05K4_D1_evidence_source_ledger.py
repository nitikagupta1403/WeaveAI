from pathlib import Path
import hashlib
import json

import pandas as pd


# =============================================================================
# P2-R0-05K4-D1
# AUTHORITATIVE EVIDENCE SOURCE LEDGER
#
# PURPOSE
#   Freeze the exact evidence sources used for the final 05F→05K synthesis.
#
# THIS STAGE DOES NOT:
#   - rerun experiments
#   - recompute statistics
#   - reinterpret outcomes
#   - generate novelty claims
#   - generate mechanism claims beyond recorded evidence status
#
# It records:
#   stage
#   evidence role
#   exact artifact
#   SHA-256
#   evidence type
#   inference status
#   causal/interventional status
#   permitted synthesis role
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
    / "05K4_D1_evidence_source_ledger"
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
# Authoritative sources
# =============================================================================

SOURCES = [

    # -------------------------------------------------------------------------
    # 05F — deterministic historical replay
    # -------------------------------------------------------------------------

    {
        "stage":
            "05F2",

        "evidence_role":
            "crop_vs_resampling_replay_script",

        "path":
            AUDITS
            / "P2_R0_05F2_crop_vs_resampling_replay.py",

        "expected_sha256":
            "e85d4733ae990b04311ac350f0fa3bea881bd795afdfa0ffb8c4a5eae833f823",

        "evidence_type":
            "deterministic_replay_code",

        "population_scope":
            "2300_images",

        "inferential_status":
            "historical_replay",

        "interventional_status":
            "preprocessing_ablation",

        "synthesis_role":
            (
                "Locate the preprocessing transition at which "
                "the historical high-band effect changes."
            ),
    },

    {
        "stage":
            "05F2",

        "evidence_role":
            "completed_replay_log",

        "path":
            AUDITS
            / "05K4_D0_2_05F_replay_capture"
            / "P2_R0_05F2_replay_full_log.txt",

        "expected_sha256":
            "8208e3d7674d221e159919b1525c7c7c09e725315f707f3d254da530b8e96ff5",

        "evidence_type":
            "archival_stdout_capture",

        "population_scope":
            "2300_images",

        "inferential_status":
            "replayed_historical_output",

        "interventional_status":
            "preprocessing_ablation",

        "synthesis_role":
            (
                "Authoritative persisted capture of the previously "
                "print-only 05F2 comparison."
            ),
    },

    {
        "stage":
            "05F2",

        "evidence_role":
            "replay_environment",

        "path":
            AUDITS
            / "05K4_D0_2_05F_replay_capture"
            / "environment.txt",

        "expected_sha256":
            "0d7d880fedb31ce834446593abd63ed6e71bd30fb49be551bd875edcc4eda16a",

        "evidence_type":
            "environment_provenance",

        "population_scope":
            "not_applicable",

        "inferential_status":
            "not_applicable",

        "interventional_status":
            "not_applicable",

        "synthesis_role":
            "Reproducibility provenance for the archival replay.",
    },


    # -------------------------------------------------------------------------
    # 05G1 — frame/support geometry diagnostics
    # -------------------------------------------------------------------------

    {
        "stage":
            "05G1",

        "evidence_role":
            "frame_border_gradient_metrics",

        "path":
            RESEARCH
            / "paper2_r0_05g_frame_border_gradient"
            / "P2_R0_05G1_frame_border_gradient_metrics.csv",

        "expected_sha256":
            "d40b052db1ca17b5f91d2a20cb57caa9d66930a53b341eb80804a292fa75c055",

        "evidence_type":
            "per_image_geometry_diagnostics",

        "population_scope":
            "2300_images",

        "inferential_status":
            "descriptive",

        "interventional_status":
            "observational_diagnostic",

        "synthesis_role":
            (
                "Characterize what changes geometrically when the "
                "same crop operation changes raster support."
            ),
    },

    {
        "stage":
            "05G1",

        "evidence_role":
            "frame_border_gradient_report",

        "path":
            RESEARCH
            / "paper2_r0_05g_frame_border_gradient"
            / "P2_R0_05G1_report.json",

        "expected_sha256":
            "9a66b2147ce36436be18af213869ace81ff168dbaf97406606b0e359b2c10fa0",

        "evidence_type":
            "diagnostic_report",

        "population_scope":
            "2300_images",

        "inferential_status":
            "descriptive",

        "interventional_status":
            "observational_diagnostic",

        "synthesis_role":
            "05G1 execution and integrity summary.",
    },


    # -------------------------------------------------------------------------
    # 05G2 — exploratory mechanism association
    # -------------------------------------------------------------------------

    {
        "stage":
            "05G2",

        "evidence_role":
            "per_image_spectral_changes",

        "path":
            RESEARCH
            / "paper2_r0_05g_frame_border_gradient"
            / "P2_R0_05G2_per_image_spectral_changes.csv",

        "expected_sha256":
            "6e4a1ddc8c23844553f5d5557b82159dbe615e7b7ef9198d177f01d950372a07",

        "evidence_type":
            "per_image_spectral_change",

        "population_scope":
            "2300_images",

        "inferential_status":
            "association_analysis",

        "interventional_status":
            "observational",

        "synthesis_role":
            "Connect geometric changes to spectral redistribution.",
    },

    {
        "stage":
            "05G2",

        "evidence_role":
            "identity_level_table",

        "path":
            RESEARCH
            / "paper2_r0_05g_frame_border_gradient"
            / "P2_R0_05G2_identity_level_table.csv",

        "expected_sha256":
            "aeb20a2956f03396c3a3b83d39f8f911a1b4b951b733f77d0c1b120e28532d99",

        "evidence_type":
            "identity_aggregation",

        "population_scope":
            "canonical_identity_level",

        "inferential_status":
            "association_analysis",

        "interventional_status":
            "observational",

        "synthesis_role":
            "Identity-level aggregation for 05G2.",
    },

    {
        "stage":
            "05G2",

        "evidence_role":
            "mechanism_associations",

        "path":
            RESEARCH
            / "paper2_r0_05g_frame_border_gradient"
            / "P2_R0_05G2_mechanism_associations.csv",

        "expected_sha256":
            "f632a572ec9c5b5f0102bd884178469ebd2774e178ac83c083423fc6ba4a6faf",

        "evidence_type":
            "association_results",

        "population_scope":
            "2300_images_with_category_adjustment",

        "inferential_status":
            "association_only",

        "interventional_status":
            "observational",

        "synthesis_role":
            (
                "Identify which support descriptors are associated "
                "with spectral redistribution."
            ),
    },

    {
        "stage":
            "05G2",

        "evidence_role":
            "mechanism_association_report",

        "path":
            RESEARCH
            / "paper2_r0_05g_frame_border_gradient"
            / "P2_R0_05G2_report.json",

        "expected_sha256":
            "bbb70ec6cff68d38a04c1cfa800f6f1a236c338150a79d3a7b16584907ad9fa5",

        "evidence_type":
            "association_report",

        "population_scope":
            "2300_images",

        "inferential_status":
            "association_only",

        "interventional_status":
            "observational",

        "synthesis_role":
            "05G2 execution/inference summary.",
    },


    # -------------------------------------------------------------------------
    # 05J — full-population support association audit
    # -------------------------------------------------------------------------

    {
        "stage":
            "05J",

        "evidence_role":
            "producer_script_v3",

        "path":
            AUDITS
            / "P2_R0_05J_population_support_spectral_audit_V3.py",

        "expected_sha256":
            "a4974b232fdb363cffadee99956413a8f887ada1237339c63934bac88ecc7b93",

        "evidence_type":
            "analysis_code",

        "population_scope":
            "2300_images",

        "inferential_status":
            "population_association_audit",

        "interventional_status":
            "observational",

        "synthesis_role":
            (
                "Authoritative code generating the v2-named 05J "
                "output directory."
            ),
    },

    {
        "stage":
            "05J",

        "evidence_role":
            "per_image_population_metrics",

        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_per_image_population_metrics.csv",

        "expected_sha256":
            "f667d8850c43001f1ee251bc2c14f18765a5289c0ebf8e8be42b972e03f6995a",

        "evidence_type":
            "per_image_population_metrics",

        "population_scope":
            "2300_images",

        "inferential_status":
            "population_association_audit",

        "interventional_status":
            "observational",

        "synthesis_role":
            "Primary 05J population metric table.",
    },

    {
        "stage":
            "05J",

        "evidence_role":
            "associations",

        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_associations.csv",

        "expected_sha256":
            "5c9a584ea5bca6ba4159f089722a5982ae120f8c1083675c11e06e805cd9fc6e",

        "evidence_type":
            "association_results",

        "population_scope":
            "2300_images",

        "inferential_status":
            "permutation_plus_FDR",

        "interventional_status":
            "observational",

        "synthesis_role":
            (
                "Population-level association between raster-relative "
                "support change and spectral redistribution."
            ),
    },

    {
        "stage":
            "05J",

        "evidence_role":
            "support_change_strata",

        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_support_change_strata.csv",

        "expected_sha256":
            "bc6ecf96c0e9674daa419c6b06ad6147d477e6168fb5ef3eb3bd95d630b53eb3",

        "evidence_type":
            "descriptive_stratification",

        "population_scope":
            "2300_images",

        "inferential_status":
            "descriptive",

        "interventional_status":
            "observational",

        "synthesis_role":
            "Descriptive support-change quartile comparison.",
    },

    {
        "stage":
            "05J",

        "evidence_role":
            "category_summary",

        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_category_summary.csv",

        "expected_sha256":
            "a15f0c94a48b4e6a476c58bc8a1131a0bdcdeb3cc60d195363c595fd7711f66f",

        "evidence_type":
            "category_summary",

        "population_scope":
            "23_categories",

        "inferential_status":
            "descriptive",

        "interventional_status":
            "observational",

        "synthesis_role":
            "Category-level direction summaries for 05J.",
    },

    {
        "stage":
            "05J",

        "evidence_role":
            "merge_provenance_audit",

        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_merge_provenance_audit.csv",

        "expected_sha256":
            "d307fd3164c0603bcbcf7240d8a864e9704df65e0269b62048768aad2f2d4a72",

        "evidence_type":
            "merge_provenance",

        "population_scope":
            "2300_images",

        "inferential_status":
            "not_applicable",

        "interventional_status":
            "not_applicable",

        "synthesis_role":
            "Audit the corrected 05J merge key/provenance.",
    },

    {
        "stage":
            "05J",

        "evidence_role":
            "top_support_change_cases",

        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_top_support_change_cases.csv",

        "expected_sha256":
            "c414d4f02bb7c61bc3eaf3278b31140628215d0671afbe57403933a389969023",

        "evidence_type":
            "diagnostic_examples",

        "population_scope":
            "selected_extreme_cases",

        "inferential_status":
            "descriptive",

        "interventional_status":
            "observational",

        "synthesis_role":
            "Diagnostic only; not inferential evidence.",
    },

    {
        "stage":
            "05J",

        "evidence_role":
            "report",

        "path":
            RESEARCH
            / "paper2_r0_05i_real_garment_canvas"
            / "P2_R0_05I6_highfreq_text_tightsupport"
            / "P2_R0_05J_population_support_spectral_audit_v2"
            / "P2_R0_05J_report.json",

        "expected_sha256":
            "b273b375285d0ad875a83c0d51b03dd090df84afbbe0bb57f2b3c127abfa1d63",

        "evidence_type":
            "population_audit_report",

        "population_scope":
            "2300_images",

        "inferential_status":
            "permutation_plus_FDR",

        "interventional_status":
            "observational",

        "synthesis_role":
            "Authoritative 05J report.",
    },


    # -------------------------------------------------------------------------
    # 05K2-B2 — sentinel intervention
    # -------------------------------------------------------------------------

    {
        "stage":
            "05K2-B2",

        "evidence_role":
            "sentinel_report",

        "path":
            FROZEN
            / "05K2_B2_Sentinel_Trajectory_Analysis_v1_0"
            / "P2_R0_05K2_B2_report.json",

        "expected_sha256":
            "46383baa02a7c33c55e5ec65e32c38493cfd5e8e0f32df58cc19501a3a073f18",

        "evidence_type":
            "sentinel_intervention_report",

        "population_scope":
            "10_diagnostic_sentinels",

        "inferential_status":
            "descriptive_only",

        "interventional_status":
            "controlled_same_pixel_support_intervention",

        "synthesis_role":
            (
                "Early controlled intervention sanity check; "
                "not population evidence."
            ),
    },


    # -------------------------------------------------------------------------
    # 05K3-D — deterministic calibration
    # -------------------------------------------------------------------------

    {
        "stage":
            "05K3-D",

        "evidence_role":
            "calibration_report",

        "path":
            FROZEN
            / "05K3_D_Calibration_Trajectory_Analysis_v1_0"
            / "P2_R0_05K3_D_report.json",

        "expected_sha256":
            "4ad144a58f16149c69374843e5bbd8197a9710b111296557b33fbcd42b6c8c8b",

        "evidence_type":
            "calibration_intervention_report",

        "population_scope":
            "230_deterministically_selected_cases",

        "inferential_status":
            "descriptive_calibration",

        "interventional_status":
            "controlled_same_pixel_support_intervention",

        "synthesis_role":
            (
                "Intermediate-scale calibration before population "
                "intervention."
            ),
    },

    {
        "stage":
            "05K3-D",

        "evidence_role":
            "calibration_category_summary",

        "path":
            FROZEN
            / "05K3_D_Calibration_Trajectory_Analysis_v1_0"
            / "P2_R0_05K3_D_category_endpoint_summary_23.csv",

        "expected_sha256":
            "60fdf63ccdd7fbe2686914580759b4c2e0819a2ad5bf32171103681fad950573",

        "evidence_type":
            "category_descriptive_summary",

        "population_scope":
            "23_categories_230_cases",

        "inferential_status":
            "descriptive_calibration",

        "interventional_status":
            "controlled_same_pixel_support_intervention",

        "synthesis_role":
            "Category breadth check during calibration.",
    },


    # -------------------------------------------------------------------------
    # 05K4-C — full primary intervention
    # -------------------------------------------------------------------------

    {
        "stage":
            "05K4-C",

        "evidence_role":
            "primary_category_effects",

        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_category_endpoint_effects_23.csv",

        "expected_sha256":
            "91f549289f95bc0beae723c66a2ed4d71169c63f4894200345376ac2d397dc41",

        "evidence_type":
            "primary_category_effects",

        "population_scope":
            "23_categories_2300_images",

        "inferential_status":
            "primary_inferential_input",

        "interventional_status":
            "controlled_same_pixel_support_intervention",

        "synthesis_role":
            "Category-level endpoint effects for primary inference.",
    },

    {
        "stage":
            "05K4-C",

        "evidence_role":
            "primary_exact_inference",

        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_exact_category_signflip_inference.csv",

        "expected_sha256":
            "a378b36f457fced975967f75cfb229e9a6b8798fcafd649e93f97f948727bde7",

        "evidence_type":
            "exact_category_signflip_inference",

        "population_scope":
            "23_category_units",

        "inferential_status":
            "exact_joint_signflip_maxT",

        "interventional_status":
            "controlled_same_pixel_support_intervention",

        "synthesis_role":
            (
                "Primary directional inference with exact joint "
                "sign-flip max-T FWER control."
            ),
    },

    {
        "stage":
            "05K4-C",

        "evidence_role":
            "primary_image_endpoints",

        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_per_image_endpoint_summary_2300.csv",

        "expected_sha256":
            "ee2993069e3a3b062e411dc9acbedda81039eb33aee3993a100908a12fe27e19",

        "evidence_type":
            "per_image_descriptive_endpoint",

        "population_scope":
            "2300_images",

        "inferential_status":
            "descriptive_only",

        "interventional_status":
            "controlled_same_pixel_support_intervention",

        "synthesis_role":
            "Image-level breadth and heterogeneity.",
    },

    {
        "stage":
            "05K4-C",

        "evidence_role":
            "primary_support_trajectory",

        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_support_level_descriptive_summary.csv",

        "expected_sha256":
            "f8bfc45ec6fd0f4a156b7e20db66bd476e3c19e2bdfe5ba91c2fdb98166b0b93",

        "evidence_type":
            "support_level_descriptive_trajectory",

        "population_scope":
            "2300_images_x_7_support_levels",

        "inferential_status":
            "descriptive_only",

        "interventional_status":
            "controlled_same_pixel_support_intervention",

        "synthesis_role":
            (
                "Aggregate support-level response trajectory; "
                "not individual monotonicity evidence."
            ),
    },

    {
        "stage":
            "05K4-C",

        "evidence_role":
            "primary_report",

        "path":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0"
            / "P2_R0_05K4_C_report.json",

        "expected_sha256":
            "9bd7a370176dd805681e377e3f2cdfcb3f06d6ea24c7619c735d26cad1a53e6b",

        "evidence_type":
            "primary_analysis_report",

        "population_scope":
            "2300_images_23_categories",

        "inferential_status":
            "primary_analysis",

        "interventional_status":
            "controlled_same_pixel_support_intervention",

        "synthesis_role":
            "Authoritative primary-analysis report.",
    },
]


# =============================================================================
# Verify every source
# =============================================================================

rows = []


print("=" * 116)
print(
    "P2-R0-05K4-D1 — "
    "AUTHORITATIVE EVIDENCE SOURCE LEDGER"
)
print("=" * 116)

print()


for i, source in enumerate(
    SOURCES,
    start=1,
):

    path = Path(
        source[
            "path"
        ]
    )

    require(
        path.is_file(),
        f"Missing source: {path}",
    )

    observed_sha = sha256_file(
        path
    )

    expected_sha = source[
        "expected_sha256"
    ]

    status = (
        "PASS"
        if observed_sha
        == expected_sha
        else "FAIL"
    )


    print(
        f"[{i:02d}]",
        source[
            "stage"
        ],
        source[
            "evidence_role"
        ],
        status,
    )


    require(
        observed_sha
        == expected_sha,
        (
            "SHA mismatch:\n"
            f"  path={path}\n"
            f"  expected={expected_sha}\n"
            f"  observed={observed_sha}"
        ),
    )


    rows.append({
        "stage":
            source[
                "stage"
            ],

        "evidence_role":
            source[
                "evidence_role"
            ],

        "path":
            str(
                path
            ),

        "sha256":
            observed_sha,

        "evidence_type":
            source[
                "evidence_type"
            ],

        "population_scope":
            source[
                "population_scope"
            ],

        "inferential_status":
            source[
                "inferential_status"
            ],

        "interventional_status":
            source[
                "interventional_status"
            ],

        "synthesis_role":
            source[
                "synthesis_role"
            ],
    })


ledger = pd.DataFrame(
    rows
)


# =============================================================================
# Evidence hierarchy
# =============================================================================

hierarchy = [

    {
        "level":
            1,

        "stage":
            "05F2",

        "role":
            (
                "Localization: determine where in the preprocessing "
                "pipeline the high-band change appears."
            ),

        "evidence_class":
            "preprocessing_ablation",

        "causal_strength":
            "component_localization_not_mechanism_proof",
    },

    {
        "level":
            2,

        "stage":
            "05G1",

        "role":
            (
                "Geometry characterization: determine what changes "
                "in the raster/support geometry after cropping."
            ),

        "evidence_class":
            "descriptive_geometry",

        "causal_strength":
            "descriptive_only",
    },

    {
        "level":
            3,

        "stage":
            "05G2/05J",

        "role":
            (
                "Population association: test whether magnitude of "
                "support change tracks magnitude/direction of spectral "
                "redistribution."
            ),

        "evidence_class":
            "observational_association",

        "causal_strength":
            "association_not_causation",
    },

    {
        "level":
            4,

        "stage":
            "05K2-B2",

        "role":
            (
                "Sentinel same-pixel support intervention: verify "
                "numerical behavior before scaling."
            ),

        "evidence_class":
            "controlled_intervention_diagnostic",

        "causal_strength":
            "interventional_but_not_population_inference",
    },

    {
        "level":
            5,

        "stage":
            "05K3-D",

        "role":
            (
                "230-case deterministic calibration of the same-pixel "
                "support intervention."
            ),

        "evidence_class":
            "controlled_intervention_calibration",

        "causal_strength":
            "interventional_descriptive",
    },

    {
        "level":
            6,

        "stage":
            "05K4-C",

        "role":
            (
                "Full 2300-image same-pixel support intervention with "
                "category-level exact inferential analysis."
            ),

        "evidence_class":
            "controlled_primary_intervention",

        "causal_strength":
            (
                "supports_dependency_under_tested_representation_"
                "and_intervention"
            ),
    },
]


hierarchy_df = pd.DataFrame(
    hierarchy
)


# =============================================================================
# Claim-boundary ledger
#
# IMPORTANT:
# These are evidence-status boundaries, not scientific result extraction.
# D2 will populate result-specific supported claims from verified sources.
# =============================================================================

claim_boundaries = [

    {
        "claim_id":
            "CB01",

        "claim":
            (
                "Cropping/localization is the preprocessing stage "
                "where the historical high-band behavior changes."
            ),

        "minimum_required_stage":
            "05F2",

        "status":
            "eligible_for_result_verification",

        "prohibited_overreach":
            (
                "Do not attribute the change to interpolation merely "
                "because localization includes resampling elsewhere."
            ),
    },

    {
        "claim_id":
            "CB02",

        "claim":
            (
                "Raster-relative support geometry changes when the "
                "garment crop changes the frame."
            ),

        "minimum_required_stage":
            "05G1",

        "status":
            "eligible_for_result_verification",

        "prohibited_overreach":
            (
                "Do not infer spectral causation from geometry "
                "descriptives alone."
            ),
    },

    {
        "claim_id":
            "CB03",

        "claim":
            (
                "Support-change magnitude is associated with spectral "
                "redistribution."
            ),

        "minimum_required_stage":
            "05G2/05J",

        "status":
            "eligible_for_result_verification",

        "prohibited_overreach":
            "Association is not causal proof.",
    },

    {
        "claim_id":
            "CB04",

        "claim":
            (
                "Changing raster support alone while holding embedded "
                "garment pixels unchanged alters the historical "
                "raster-relative representation."
            ),

        "minimum_required_stage":
            "05K4-C",

        "status":
            "eligible_for_result_verification",

        "prohibited_overreach":
            (
                "Do not generalize beyond the tested representation, "
                "dataset, and intervention."
            ),
    },

    {
        "claim_id":
            "CB05",

        "claim":
            (
                "The matched object-relative representation is "
                "invariant to the tested same-pixel support intervention."
            ),

        "minimum_required_stage":
            "05K4-C",

        "status":
            "eligible_for_result_verification",

        "prohibited_overreach":
            (
                "Do not claim universal invariance to arbitrary "
                "transformations."
            ),
    },

    {
        "claim_id":
            "CB06",

        "claim":
            (
                "The primary support response is broad at the endpoint "
                "but not universally monotonic image-by-image."
            ),

        "minimum_required_stage":
            "05K4-C",

        "status":
            "eligible_for_result_verification",

        "prohibited_overreach":
            (
                "Do not describe support factor as a deterministic "
                "monotonic law for every image."
            ),
    },
]


claim_df = pd.DataFrame(
    claim_boundaries
)


# =============================================================================
# Save outputs
# =============================================================================

LEDGER_CSV = (
    OUT
    / "P2_R0_05K4_D1_authoritative_source_ledger.csv"
)

HIERARCHY_CSV = (
    OUT
    / "P2_R0_05K4_D1_evidence_hierarchy.csv"
)

CLAIMS_CSV = (
    OUT
    / "P2_R0_05K4_D1_claim_boundary_ledger.csv"
)

REPORT_JSON = (
    OUT
    / "P2_R0_05K4_D1_report.json"
)


ledger.to_csv(
    LEDGER_CSV,
    index=False,
    lineterminator="\n",
)


hierarchy_df.to_csv(
    HIERARCHY_CSV,
    index=False,
    lineterminator="\n",
)


claim_df.to_csv(
    CLAIMS_CSV,
    index=False,
    lineterminator="\n",
)


report = {
    "stage":
        "P2_R0_05K4_D1_AUTHORITATIVE_EVIDENCE_SOURCE_LEDGER",

    "status":
        "PASS_SOURCE_LOCK",

    "source_count":
        int(
            len(
                ledger
            )
        ),

    "stages":
        sorted(
            ledger[
                "stage"
            ].unique().tolist()
        ),

    "all_hashes_verified":
        True,

    "new_statistics_computed":
        False,

    "scientific_results_recomputed":
        False,

    "claim_generation":
        False,

    "interpretation":
        False,

    "purpose":
        (
            "Freeze exact evidence sources and evidence hierarchy "
            "before result-level synthesis."
        ),

    "next_stage":
        (
            "05K4-D2: extract source-supported results and construct "
            "observation→interpretation→remaining-gap ledger."
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
# Output checksums
# =============================================================================

OUTPUTS = [
    LEDGER_CSV,
    HIERARCHY_CSV,
    CLAIMS_CSV,
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
# Final
# =============================================================================

print()
print("=" * 116)
print(
    "P2-R0-05K4-D1 — "
    "AUTHORITATIVE SOURCE LOCK: PASS"
)
print("=" * 116)

print(
    "Verified sources:",
    len(
        ledger
    ),
)

print()

print("STAGE COUNTS")

print(
    ledger.groupby(
        "stage"
    )
    .size()
    .to_string()
)

print()
print("EVIDENCE HIERARCHY")

print(
    hierarchy_df[
        [
            "level",
            "stage",
            "evidence_class",
            "causal_strength",
        ]
    ]
    .to_string(
        index=False
    )
)

print()
print("CLAIM BOUNDARIES")

print(
    claim_df[
        [
            "claim_id",
            "minimum_required_stage",
            "status",
        ]
    ]
    .to_string(
        index=False
    )
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
print("New statistics computed : NO")
print("Results recomputed       : NO")
print("Interpretation performed : NO")
print("Claims finalized         : NO")

print()
print("=" * 116)
print(
    "STOP — FREEZE D1 BEFORE RESULT-LEVEL SYNTHESIS"
)
print("=" * 116)