from pathlib import Path
import hashlib
import json


# =============================================================================
# P2-R0-05K4-D0
# SYNTHESIS SOURCE LOCK
#
# PURPOSE
#   Locate and hash candidate frozen evidence artifacts needed for the final
#   05K synthesis.
#
# THIS STAGE DOES NOT:
#   - interpret results
#   - restate scientific claims
#   - select favorable outcomes
#   - perform statistics
#   - change any frozen artifact
#
# It is provenance discovery / source locking only.
# =============================================================================


REPO = Path(
    "/Users/nitikagupta/Research/WeaveAI"
)

PAPER2 = (
    REPO
    / "papers/Paper-II/reproducibility"
)

FROZEN = (
    PAPER2
    / "frozen"
)

AUDITS = (
    PAPER2
    / "audits"
)

OUT = (
    AUDITS
    / "05K4_D0_synthesis_source_lock"
)

OUT.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Helpers
# =============================================================================

def sha256_file(path):
    h = hashlib.sha256()

    with Path(path).open("rb") as f:
        for chunk in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
            h.update(chunk)

    return h.hexdigest()


def file_record(path):
    return {
        "path":
            str(
                path
            ),

        "name":
            path.name,

        "size_bytes":
            int(
                path.stat().st_size
            ),

        "sha256":
            sha256_file(
                path
            ),
    }


def find_candidates(tokens):
    """
    Search reproducibility tree without modifying anything.

    All tokens must occur somewhere in the lowercase full path.
    """

    hits = []

    for path in PAPER2.rglob("*"):

        if not path.is_file():
            continue

        low = str(
            path
        ).lower()

        if all(
            token.lower() in low
            for token in tokens
        ):
            hits.append(
                path
            )

    return sorted(
        hits,
        key=lambda p:
            str(
                p
            ),
    )


# =============================================================================
# Stage search definitions
#
# We deliberately search broadly first.
# D1 synthesis should consume only exact artifacts we confirm here.
# =============================================================================

SEARCHES = {
    "05F_CROP_ONLY": [
        ["05f"],
    ],

    "05G_SUPPORT_GEOMETRY": [
        ["05g"],
    ],

    "05J_POPULATION_SUPPORT_ASSOCIATION": [
        ["05j"],
    ],

    "05K2_B2_SENTINEL_TRAJECTORY": [
        ["05k2", "b2"],
        ["05k2_b2"],
    ],

    "05K3_D_CALIBRATION_TRAJECTORY": [
        ["05k3", "d"],
        ["05k3_d"],
    ],

    "05K4_C_PRIMARY_INFERENCE": [
        ["05k4", "c"],
        ["05k4_c"],
    ],
}


# =============================================================================
# Known authoritative 05K packages
# =============================================================================

KNOWN_LOCKS = {
    "05K3_D": {
        "directory":
            FROZEN
            / "05K3_D_Calibration_Trajectory_Analysis_v1_0",

        "expected_files": [
            "P2_R0_05K3_D_per_condition_trajectories_1610.csv",
            "P2_R0_05K3_D_per_case_summary_230.csv",
            "P2_R0_05K3_D_support_level_summary.csv",
            "P2_R0_05K3_D_category_endpoint_summary_23.csv",
            "P2_R0_05K3_D_report.json",
        ],
    },

    "05K4_C": {
        "directory":
            FROZEN
            / "05K4_C_Primary_Trajectory_Inference_v1_0",

        "expected_files": [
            "P2_R0_05K4_C_per_condition_trajectories_16100.csv",
            "P2_R0_05K4_C_per_image_endpoint_summary_2300.csv",
            "P2_R0_05K4_C_support_level_descriptive_summary.csv",
            "P2_R0_05K4_C_category_endpoint_effects_23.csv",
            "P2_R0_05K4_C_exact_category_signflip_inference.csv",
            "P2_R0_05K4_C_report.json",
        ],
    },
}


# =============================================================================
# Header
# =============================================================================

print("=" * 116)
print(
    "P2-R0-05K4-D0 — "
    "SYNTHESIS SOURCE LOCK"
)
print("=" * 116)

print("Interpretation       : NO")
print("Statistical analysis : NO")
print("Artifact mutation    : NO")
print("Source discovery     : YES")
print()


# =============================================================================
# 1. Verify known locked packages
# =============================================================================

known_output = {}


print("=" * 116)
print("KNOWN AUTHORITATIVE PACKAGES")
print("=" * 116)


for stage, spec in KNOWN_LOCKS.items():

    directory = spec[
        "directory"
    ]

    if not directory.is_dir():

        raise RuntimeError(
            f"Missing known frozen directory: {directory}"
        )


    stage_records = []


    print()
    print(stage)
    print("-" * 116)


    for name in spec[
        "expected_files"
    ]:

        path = (
            directory
            / name
        )


        if not path.is_file():

            raise RuntimeError(
                f"Missing authoritative file: {path}"
            )


        rec = file_record(
            path
        )


        stage_records.append(
            rec
        )


        print(
            rec[
                "sha256"
            ],
            rec[
                "path"
            ],
        )


    known_output[
        stage
    ] = {
        "directory":
            str(
                directory
            ),

        "files":
            stage_records,
    }


# =============================================================================
# 2. Search earlier evidence stages
# =============================================================================

search_output = {}


print()
print("=" * 116)
print("EARLIER-STAGE CANDIDATE DISCOVERY")
print("=" * 116)


for stage, alternatives in SEARCHES.items():

    unique = {}


    for tokens in alternatives:

        for path in find_candidates(
            tokens
        ):

            unique[
                str(
                    path
                )
            ] = path


    hits = list(
        unique.values()
    )


    # Prefer scientifically useful structured/text artifacts in display.
    preferred_suffixes = {
        ".csv",
        ".json",
        ".txt",
        ".md",
        ".py",
    }


    preferred = [
        p
        for p in hits
        if p.suffix.lower()
        in preferred_suffixes
    ]


    search_output[
        stage
    ] = [
        file_record(
            path
        )
        for path in preferred
    ]


    print()
    print(stage)
    print("-" * 116)
    print(
        "Candidates:",
        len(
            preferred
        ),
    )


    for rec in search_output[
        stage
    ]:

        print(
            rec[
                "sha256"
            ],
            rec[
                "path"
            ],
        )


# =============================================================================
# 3. Commit provenance
# =============================================================================

git_head = None


head_path = (
    REPO
    / ".git/HEAD"
)


if head_path.is_file():

    head_text = (
        head_path
        .read_text(
            encoding="utf-8"
        )
        .strip()
    )


    if head_text.startswith(
        "ref:"
    ):

        ref = (
            head_text
            .split(
                ":",
                1,
            )[
                1
            ]
            .strip()
        )


        ref_path = (
            REPO
            / ".git"
            / ref
        )


        if ref_path.is_file():

            git_head = (
                ref_path
                .read_text(
                    encoding="utf-8"
                )
                .strip()
            )


# =============================================================================
# 4. Save discovery manifest
# =============================================================================

MANIFEST_JSON = (
    OUT
    / "P2_R0_05K4_D0_synthesis_source_candidates.json"
)


manifest = {
    "stage":
        "P2_R0_05K4_D0_SYNTHESIS_SOURCE_LOCK",

    "purpose":
        (
            "Discover and hash exact evidence artifacts "
            "before scientific synthesis."
        ),

    "repo":
        str(
            REPO
        ),

    "git_head_if_resolved":
        git_head,

    "known_authoritative_packages":
        known_output,

    "candidate_searches":
        search_output,

    "analysis_boundary": {
        "interpretation":
            False,

        "statistical_analysis":
            False,

        "claim_generation":
            False,

        "artifact_mutation":
            False,
    },
}


MANIFEST_JSON.write_text(
    json.dumps(
        manifest,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


# =============================================================================
# 5. Human-readable inventory
# =============================================================================

INVENTORY_TXT = (
    OUT
    / "P2_R0_05K4_D0_inventory.txt"
)


lines = []


lines.append(
    "P2-R0-05K4-D0 — SYNTHESIS SOURCE INVENTORY"
)

lines.append(
    "=" * 116
)

lines.append("")


for stage, records in search_output.items():

    lines.append(stage)

    lines.append(
        "-" * 116
    )


    if len(
        records
    ) == 0:

        lines.append(
            "NO CANDIDATES FOUND"
        )

    else:

        for i, rec in enumerate(
            records,
            start=1,
        ):

            lines.append(
                f"[{i:03d}] "
                f"{rec['sha256']}  "
                f"{rec['path']}"
            )


    lines.append("")


INVENTORY_TXT.write_text(
    "\n".join(
        lines
    )
    + "\n",
    encoding="utf-8",
)


# =============================================================================
# 6. Output checksums
# =============================================================================

SUMS = (
    OUT
    / "SHA256SUMS.txt"
)


with SUMS.open(
    "w",
    encoding="utf-8",
) as f:

    for path in [
        MANIFEST_JSON,
        INVENTORY_TXT,
    ]:

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
    "P2-R0-05K4-D0 — SOURCE DISCOVERY COMPLETE"
)
print("=" * 116)

print()
print(
    "Manifest:",
    MANIFEST_JSON,
)

print(
    "Inventory:",
    INVENTORY_TXT,
)

print()

print(
    "Manifest SHA:",
    sha256_file(
        MANIFEST_JSON
    ),
)

print(
    "Inventory SHA:",
    sha256_file(
        INVENTORY_TXT
    ),
)

print(
    "SHA256SUMS SHA:",
    sha256_file(
        SUMS
    ),
)

print()
print("Interpretation       : NO")
print("Statistical analysis : NO")
print("Claims generated     : NO")
print("Artifacts modified   : NO")

print()
print("=" * 116)
print(
    "STOP — REVIEW CANDIDATE INVENTORY BEFORE 05K4-D1 SYNTHESIS"
)
print("=" * 116)