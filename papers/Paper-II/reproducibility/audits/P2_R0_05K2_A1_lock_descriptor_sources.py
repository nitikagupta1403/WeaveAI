from pathlib import Path
import ast
import hashlib
import json
import re


# ============================================================================
# P2-R0-05K2-A1
# EXACT DESCRIPTOR SOURCE-LOCK RECOVERY
#
# READ-ONLY SOURCE INSPECTION.
#
# NO descriptor execution.
# NO FFT execution.
# NO band fractions computed.
# NO 05K trajectories opened.
# ============================================================================


ROOT = Path(
    "/Users/nitikagupta/Research/WeaveAI/"
    "papers/Paper-II/reproducibility/audits"
)

OUTDIR = (
    ROOT
    / "05K2_A1_descriptor_source_lock"
)

OUTDIR.mkdir(
    parents=True,
    exist_ok=True,
)


KNOWN = {
    "H2": ROOT / "P2_R0_05H2_intrinsic_representation_replay.py",
    "H1": ROOT / "P2_R0_05H1_intrinsic_coordinate_field.py",
    "I2": ROOT / "P2_R0_05I2_objective_real_garment_candidate_selection.py",
}


# ============================================================================
# Helpers
# ============================================================================

def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha256_file(path):
    h = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
            h.update(chunk)

    return h.hexdigest()


def get_function_nodes(text):
    tree = ast.parse(text)

    out = {}

    for node in ast.walk(tree):
        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
            ),
        ):
            out.setdefault(
                node.name,
                [],
            ).append(node)

    return tree, out


def source_segment(text, node):
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


def relevant_function_records(
    path,
    required_terms,
):

    text = path.read_text(
        encoding="utf-8",
        errors="replace",
    )

    _, functions = get_function_nodes(text)

    records = []

    for name, nodes in functions.items():

        for node in nodes:

            segment = source_segment(
                text,
                node,
            )

            blob = (
                name
                + "\n"
                + segment
            ).lower()

            matched = [
                term
                for term in required_terms
                if term.lower() in blob
            ]

            if matched:

                records.append({
                    "name":
                        name,

                    "line_start":
                        int(node.lineno),

                    "line_end":
                        int(
                            getattr(
                                node,
                                "end_lineno",
                                node.lineno,
                            )
                        ),

                    "matched_terms":
                        matched,

                    "source":
                        segment,
                })

    return records


# ============================================================================
# Start
# ============================================================================

print("=" * 96)
print("P2-R0-05K2-A1 — EXACT DESCRIPTOR SOURCE LOCK")
print("=" * 96)
print("Descriptor execution performed : NO")
print("FFT executed                    : NO")
print("Band fractions computed         : NO")
print("05K trajectories opened         : NO")
print()


# ============================================================================
# 1. Verify known anchor scripts exist and hash them
# ============================================================================

known_sha = {}

for label, path in KNOWN.items():

    require(
        path.exists(),
        f"Missing known source: {path}",
    )

    digest = sha256_file(
        path
    )

    known_sha[label] = digest

    print(
        f"{label}: {path.name}"
    )
    print(
        f"SHA256: {digest}"
    )
    print()


# ============================================================================
# 2. Locate exact recover_geometry definition
#
# We do NOT infer module identity from a function call.
# We search historical Python files for the actual definition.
# ============================================================================

recover_hits = []

for path in sorted(
    ROOT.rglob("*.py")
):

    # Exclude current 05K2 scripts to avoid self-discovery.
    if "05K2" in path.name:
        continue

    try:
        text = path.read_text(
            encoding="utf-8",
            errors="replace",
        )

        tree, functions = get_function_nodes(
            text
        )

    except Exception:
        continue

    if "recover_geometry" not in functions:
        continue

    for node in functions[
        "recover_geometry"
    ]:

        segment = source_segment(
            text,
            node,
        )

        recover_hits.append({
            "path":
                str(path),

            "sha256":
                sha256_file(path),

            "line_start":
                int(node.lineno),

            "line_end":
                int(
                    getattr(
                        node,
                        "end_lineno",
                        node.lineno,
                    )
                ),

            "source":
                segment,
        })


print("=" * 96)
print("RECOVER_GEOMETRY DEFINITIONS")
print("=" * 96)
print(
    "Definitions found:",
    len(recover_hits),
)

for n, hit in enumerate(
    recover_hits,
    start=1,
):

    print()
    print("-" * 96)
    print(f"[{n}] {hit['path']}")
    print("SHA256:", hit["sha256"])
    print(
        "LINES:",
        hit["line_start"],
        "-",
        hit["line_end"],
    )
    print("-" * 96)
    print(hit["source"])


# ============================================================================
# 3. Trace H2's validate_geometry_equivalence / RA14 loading chain
# ============================================================================

H2 = KNOWN["H2"]

h2_text = H2.read_text(
    encoding="utf-8",
    errors="replace",
)

h2_terms = [
    "load_verified_d4_definitions",
    "validate_geometry_equivalence",
    "ra14_module",
    "recover_geometry",
    "importlib",
    "spec_from_file_location",
    ".py",
]

print()
print("=" * 96)
print("H2 LOADING / RA14 TRACE")
print("=" * 96)

h2_lines = h2_text.splitlines()

for lineno, line in enumerate(
    h2_lines,
    start=1,
):

    if any(
        term.lower()
        in line.lower()
        for term in h2_terms
    ):

        lo = max(
            1,
            lineno - 3,
        )

        hi = min(
            len(h2_lines),
            lineno + 3,
        )

        print()
        print(
            f"--- context around H2 line {lineno} ---"
        )

        for j in range(
            lo,
            hi + 1,
        ):
            print(
                f"{j:04d}: "
                f"{h2_lines[j - 1]}"
            )


# ============================================================================
# 4. Find validate_geometry_equivalence definition
# ============================================================================

validate_hits = []

for path in sorted(
    ROOT.rglob("*.py")
):

    if "05K2" in path.name:
        continue

    try:
        text = path.read_text(
            encoding="utf-8",
            errors="replace",
        )

        _, functions = get_function_nodes(
            text
        )

    except Exception:
        continue

    if (
        "validate_geometry_equivalence"
        not in functions
    ):
        continue

    for node in functions[
        "validate_geometry_equivalence"
    ]:

        validate_hits.append({
            "path":
                str(path),

            "sha256":
                sha256_file(path),

            "line_start":
                int(node.lineno),

            "line_end":
                int(
                    getattr(
                        node,
                        "end_lineno",
                        node.lineno,
                    )
                ),

            "source":
                source_segment(
                    text,
                    node,
                ),
        })


print()
print("=" * 96)
print("VALIDATE_GEOMETRY_EQUIVALENCE DEFINITIONS")
print("=" * 96)

print(
    "Definitions found:",
    len(validate_hits),
)

for n, hit in enumerate(
    validate_hits,
    start=1,
):

    print()
    print("-" * 96)
    print(f"[{n}] {hit['path']}")
    print("SHA256:", hit["sha256"])
    print(
        "LINES:",
        hit["line_start"],
        "-",
        hit["line_end"],
    )
    print("-" * 96)
    print(hit["source"])


# ============================================================================
# 5. I2 — exact spectral / band-reduction functions
# ============================================================================

i2_records = relevant_function_records(
    KNOWN["I2"],
    [
        "np.fft.rfft",
        "BANDS",
        "band_fraction",
        "angular",
        "magnitude",
        "abs(",
        "sum(",
        "1:37",
        "25, 37",
    ],
)


print()
print("=" * 96)
print("I2 SPECTRAL / BAND FUNCTIONS")
print("=" * 96)

print(
    "Relevant functions:",
    len(i2_records),
)

for rec in i2_records:

    print()
    print("-" * 96)
    print(
        rec["name"],
        f"(lines "
        f"{rec['line_start']}-"
        f"{rec['line_end']})",
    )
    print(
        "MATCH:",
        rec["matched_terms"],
    )
    print("-" * 96)
    print(rec["source"])


# Also print module-level lines around BANDS.
i2_text = KNOWN["I2"].read_text(
    encoding="utf-8",
    errors="replace",
)

i2_lines = i2_text.splitlines()

print()
print("=" * 96)
print("I2 MODULE-LEVEL BAND CONSTANTS")
print("=" * 96)

for lineno, line in enumerate(
    i2_lines,
    start=1,
):

    if (
        "low_1_4" in line
        or "mid_5_12" in line
        or "highmid_13_24" in line
        or "high_25_36" in line
    ):

        if lineno < 150:

            lo = max(
                1,
                lineno - 3,
            )

            hi = min(
                len(i2_lines),
                lineno + 3,
            )

            for j in range(
                lo,
                hi + 1,
            ):
                print(
                    f"{j:04d}: "
                    f"{i2_lines[j - 1]}"
                )

            print()


# ============================================================================
# 6. H1 — exact intrinsic construction functions
# ============================================================================

h1_records = relevant_function_records(
    KNOWN["H1"],
    [
        "centroid",
        "max_radius",
        "foreground",
        "conditional",
        "radial",
        "angular",
        "np.fft.rfft",
        "72",
        "< 250",
        "250",
    ],
)


print()
print("=" * 96)
print("H1 INTRINSIC GEOMETRY FUNCTIONS")
print("=" * 96)

print(
    "Relevant functions:",
    len(h1_records),
)

for rec in h1_records:

    print()
    print("-" * 96)
    print(
        rec["name"],
        f"(lines "
        f"{rec['line_start']}-"
        f"{rec['line_end']})",
    )
    print(
        "MATCH:",
        rec["matched_terms"],
    )
    print("-" * 96)
    print(rec["source"])


# ============================================================================
# 7. Build source-lock report
# ============================================================================

REPORT = {
    "audit":
        "P2-R0-05K2-A1 exact descriptor source lock",

    "status":
        "SOURCE_IDENTIFICATION_ONLY",

    "known_anchor_sha256": {
        label:
            known_sha[label]

        for label
        in sorted(known_sha)
    },

    "recover_geometry_definitions":
        recover_hits,

    "validate_geometry_equivalence_definitions":
        validate_hits,

    "i2_spectral_band_functions":
        i2_records,

    "h1_intrinsic_functions":
        h1_records,

    "anti_peeking": {
        "descriptor_executed":
            False,

        "fft_executed":
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
    / "P2_R0_05K2_A1_descriptor_source_lock.json"
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
print("=" * 96)
print("SOURCE-LOCK RECOVERY OUTPUT")
print("=" * 96)

print(REPORT_OUT)
print("SHA256:", report_sha)

print()
print("Descriptor executed      : NO")
print("FFT executed             : NO")
print("Band fractions computed  : NO")
print("05K trajectories opened  : NO")

print()
print("=" * 96)
print(
    "STOP — DO NOT REPLAY s=1 UNTIL "
    "AUTHORITATIVE SOURCES ARE IDENTIFIED"
)
print("=" * 96)