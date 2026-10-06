from pathlib import Path
import hashlib
import ast
import re
import json


# ============================================================================
# P2-R0-05K2-A0
# FROZEN DESCRIPTOR IMPLEMENTATION SOURCE RECOVERY
#
# NO descriptor execution.
# NO band fractions computed.
# NO 05K trajectories opened.
# ============================================================================


ROOT = Path(
    "/Users/nitikagupta/Research/WeaveAI/"
    "papers/Paper-II/reproducibility/audits"
)

OUTDIR = (
    ROOT
    / "05K2_A0_descriptor_source_recovery"
)

OUTDIR.mkdir(
    parents=True,
    exist_ok=True,
)


# Candidate historical implementations only.
#
# We deliberately do not recursively choose "best matches".
# These are the known lineages that produced the relevant audits.

CANDIDATES = [

    # ------------------------------------------------------------------------
    # Raster-relative lineage
    # ------------------------------------------------------------------------

    ROOT / "P2_R0_05J_population_support_spectral_audit.py",

    ROOT / "P2_R0_05J_population_support_spectral_audit_PATCHED.py",

    ROOT / "P2_R0_05J_population_support_spectral_audit_V2.py",

    ROOT / "P2_R0_05J_population_support_spectral_audit_V3.py",

    ROOT / "P2_R0_05I2_objective_real_garment_candidate_selection.py",

    # ------------------------------------------------------------------------
    # Object-relative / intrinsic lineage
    # ------------------------------------------------------------------------

    ROOT / "P2_R0_05H1_intrinsic_coordinate_field.py",

    ROOT / "P2_R0_05H2_intrinsic_representation_replay.py",
]


# Terms are used only to find relevant definitions.
# They do NOT establish implementation equivalence.

KEYWORDS = [
    "recover_geometry",
    "fft",
    "rfft",
    "harmonic",
    "band",
    "fraction",
    "radial",
    "polar",
    "centroid",
    "grid_radius",
    "foreground_radius",
    "intrinsic",
    "field",
    "spectrum",
    "energy",
    "low_1_4",
    "mid_5_12",
    "highmid_13_24",
    "high_25_36",
]


# ============================================================================
# Helpers
# ============================================================================

def sha256_file(path):

    h = hashlib.sha256()

    with path.open("rb") as f:

        for chunk in iter(
            lambda: f.read(
                1024 * 1024
            ),
            b"",
        ):
            h.update(chunk)

    return h.hexdigest()


def source_segment(
    text,
    node,
):

    lines = text.splitlines()

    start = node.lineno - 1

    end = getattr(
        node,
        "end_lineno",
        node.lineno,
    )

    return "\n".join(
        lines[start:end]
    )


def definition_relevant(
    name,
    source,
):

    blob = (
        str(name)
        + "\n"
        + str(source)
    ).lower()

    return any(
        kw.lower() in blob
        for kw in KEYWORDS
    )


# ============================================================================
# Start
# ============================================================================

print("=" * 92)
print(
    "P2-R0-05K2-A0 — "
    "FROZEN DESCRIPTOR SOURCE RECOVERY"
)
print("=" * 92)

print(
    "Descriptor execution performed : NO"
)
print(
    "Band fractions computed        : NO"
)
print(
    "05K trajectories opened        : NO"
)
print()


records = []


# ============================================================================
# 1. Inspect known candidate scripts
# ============================================================================

for path in CANDIDATES:

    print()
    print("=" * 92)
    print("FILE:", path)
    print("=" * 92)

    if not path.exists():

        print("STATUS: MISSING")

        records.append({
            "path": str(path),
            "exists": False,
            "sha256": None,
            "relevant_definitions": [],
        })

        continue


    digest = sha256_file(
        path
    )

    print("STATUS: FOUND")
    print("SHA256:", digest)


    text = path.read_text(
        encoding="utf-8",
        errors="replace",
    )


    try:

        tree = ast.parse(
            text
        )

    except SyntaxError as exc:

        print(
            "AST PARSE FAILED:",
            exc,
        )

        records.append({
            "path": str(path),
            "exists": True,
            "sha256": digest,
            "relevant_definitions": [],
            "ast_parse_failed": True,
        })

        continue


    relevant = []


    for node in ast.walk(tree):

        if not isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
            ),
        ):
            continue


        segment = source_segment(
            text,
            node,
        )


        if not definition_relevant(
            node.name,
            segment,
        ):
            continue


        relevant.append({
            "name":
                node.name,

            "lineno":
                node.lineno,

            "end_lineno":
                getattr(
                    node,
                    "end_lineno",
                    node.lineno,
                ),

            "source":
                segment,
        })


    print(
        "Relevant definitions:",
        len(relevant),
    )


    for item in relevant:

        print()
        print(
            "-" * 72
        )

        print(
            f"{item['name']} "
            f"(lines "
            f"{item['lineno']}-"
            f"{item['end_lineno']})"
        )

        print(
            "-" * 72
        )

        print(
            item["source"]
        )


    records.append({
        "path":
            str(path),

        "exists":
            True,

        "sha256":
            digest,

        "relevant_definitions":
            relevant,
    })


# ============================================================================
# 2. Search for exact band literals outside functions
#
# This helps catch module-level constants such as:
#
#   BANDS = {...}
#
# without interpreting them.
# ============================================================================

print()
print("=" * 92)
print("MODULE-LEVEL BAND / NORMALIZATION LITERALS")
print("=" * 92)


literal_records = []


PATTERNS = [
    r"low_1_4",
    r"mid_5_12",
    r"highmid_13_24",
    r"high_25_36",
    r"\b1\s*:\s*4\b",
    r"\b5\s*:\s*12\b",
    r"\b13\s*:\s*24\b",
    r"\b25\s*:\s*36\b",
    r"grid_radius",
    r"foreground_radius",
    r"max.*radius",
    r"rfft",
]


for path in CANDIDATES:

    if not path.exists():
        continue


    text = path.read_text(
        encoding="utf-8",
        errors="replace",
    )

    lines = text.splitlines()


    hits = []


    for n, line in enumerate(
        lines,
        start=1,
    ):

        if any(
            re.search(
                pattern,
                line,
                flags=re.IGNORECASE,
            )
            for pattern in PATTERNS
        ):

            hits.append({
                "line":
                    n,

                "text":
                    line,
            })


    literal_records.append({
        "path":
            str(path),

        "hits":
            hits,
    })


    print()
    print("FILE:", path.name)
    print("HITS:", len(hits))


    for hit in hits[:120]:

        print(
            f"{hit['line']:04d}: "
            f"{hit['text']}"
        )


    if len(hits) > 120:

        print(
            "... truncated",
            len(hits) - 120,
            "additional hits",
        )


# ============================================================================
# 3. Write recovery record
# ============================================================================

REPORT = {
    "audit":
        "P2-R0-05K2-A0 descriptor source recovery",

    "status":
        "SOURCE_RECOVERY_ONLY",

    "candidate_scripts":
        records,

    "module_level_literal_hits":
        literal_records,

    "anti_peeking": {
        "descriptor_executed":
            False,

        "band_fractions_computed":
            False,

        "05k_trajectory_opened":
            False,

        "h1_h2_h3_tested":
            False,
    },
}


REPORT_OUT = (
    OUTDIR
    / "P2_R0_05K2_A0_descriptor_source_recovery.json"
)


REPORT_OUT.write_text(
    json.dumps(
        REPORT,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


report_sha = sha256_file(
    REPORT_OUT
)


print()
print("=" * 92)
print("RECOVERY OUTPUT")
print("=" * 92)

print(
    REPORT_OUT
)

print(
    "SHA256:",
    report_sha,
)

print()
print(
    "Descriptor executed      : NO"
)
print(
    "05K trajectories opened  : NO"
)

print()
print("=" * 92)
print(
    "STOP — IMPLEMENTATION SOURCE "
    "MUST BE IDENTIFIED BEFORE REPLAY"
)
print("=" * 92)