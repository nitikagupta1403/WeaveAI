from __future__ import annotations

import ast
import json
from pathlib import Path


# =============================================================================
# P2-R0-05H4B1 — TRAINING-MRR SOURCE TRACE
#
# Purpose:
#   05H4A showed that effect_tables contain 46 rows per fold, matching the
#   held-out test identities. Those tables therefore cannot, by themselves,
#   explain the INTRINSIC fold-3 *training* MRR elevation observed in 05H3.
#
#   Before reconstructing any per-query training decomposition, inspect the
#   exact frozen implementation that computes:
#
#       train_full_mrr
#       train_selected_mrr
#
#   and freeze the relevant source blocks / helper call graph.
#
# No experiment is run here.
# No retrieval logic is reconstructed here.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate/"
    "P2_R0_05H4B1_training_mrr_source_trace"
)

TRACE_TXT = (
    OUTPUT_ROOT
    / "P2_R0_05H4B1_training_mrr_source_trace.txt"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05H4B1_report.json"
)


TARGET_TERMS = [
    "train_full_mrr",
    "train_selected_mrr",
    "replay_cell13_selection",
]


def source_segment(
    source: str,
    node: ast.AST,
) -> str:

    lines = source.splitlines()

    start = int(
        getattr(
            node,
            "lineno",
            1,
        )
    )

    end = int(
        getattr(
            node,
            "end_lineno",
            start,
        )
    )

    return "\n".join(
        lines[
            start - 1:end
        ]
    )


def function_map(
    tree: ast.AST,
):

    out = {}

    for node in ast.walk(
        tree
    ):

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
            ),
        ):
            out[
                node.name
            ] = node

    return out


def called_function_names(
    node: ast.AST,
):

    names = set()

    for child in ast.walk(
        node
    ):

        if isinstance(
            child,
            ast.Call,
        ):

            fn = child.func

            if isinstance(
                fn,
                ast.Name,
            ):
                names.add(
                    fn.id
                )

            elif isinstance(
                fn,
                ast.Attribute,
            ):
                names.add(
                    fn.attr
                )

    return sorted(
        names
    )


def main():

    if not BASE_AUDIT.is_file():
        raise RuntimeError(
            f"Base audit missing: {BASE_AUDIT}"
        )

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for path in (
        TRACE_TXT,
        REPORT_JSON,
    ):
        if path.exists():
            raise RuntimeError(
                f"Refusing to overwrite: {path}"
            )

    source = BASE_AUDIT.read_text(
        encoding="utf-8"
    )

    tree = ast.parse(
        source
    )

    funcs = function_map(
        tree
    )

    if (
        "replay_cell13_selection"
        not in funcs
    ):
        raise RuntimeError(
            "replay_cell13_selection not found"
        )

    replay_node = funcs[
        "replay_cell13_selection"
    ]

    replay_source = source_segment(
        source,
        replay_node,
    )

    calls = called_function_names(
        replay_node
    )

    direct_helpers = [
        name
        for name in calls
        if name in funcs
        and name
        != "replay_cell13_selection"
    ]

    # Also freeze any function that contains either training-MRR variable name.
    mrr_related_functions = []

    for name, node in funcs.items():

        segment = source_segment(
            source,
            node,
        )

        if (
            "train_full_mrr"
            in segment
            or
            "train_selected_mrr"
            in segment
        ):
            mrr_related_functions.append(
                name
            )

    # Search exact source locations of the two training-MRR variables.
    all_lines = source.splitlines()

    hit_rows = []

    for i, line in enumerate(
        all_lines,
        start=1,
    ):

        for term in TARGET_TERMS:

            if term in line:

                hit_rows.append(
                    (
                        i,
                        term,
                        line,
                    )
                )

    output = []

    output.append(
        "=" * 120
    )

    output.append(
        "P2-R0-05H4B1 — TRAINING-MRR SOURCE TRACE"
    )

    output.append(
        "=" * 120
    )

    output.append(
        ""
    )

    output.append(
        "BASE AUDIT:"
    )

    output.append(
        str(
            BASE_AUDIT
        )
    )

    output.append(
        ""
    )

    output.append(
        "SOURCE HITS"
    )

    output.append(
        "-" * 120
    )

    for lineno, term, line in hit_rows:

        output.append(
            f"L{lineno:05d} [{term}] {line}"
        )

    output.append(
        ""
    )

    output.append(
        "REPLAY FUNCTION CALLS"
    )

    output.append(
        "-" * 120
    )

    output.extend(
        calls
    )

    output.append(
        ""
    )

    output.append(
        "DIRECT LOCAL HELPERS CALLED BY replay_cell13_selection"
    )

    output.append(
        "-" * 120
    )

    if direct_helpers:

        output.extend(
            direct_helpers
        )

    else:

        output.append(
            "<none>"
        )

    output.append(
        ""
    )

    output.append(
        "FUNCTIONS CONTAINING TRAIN-MRR VARIABLES"
    )

    output.append(
        "-" * 120
    )

    output.extend(
        mrr_related_functions
    )

    output.append(
        ""
    )

    output.append(
        "=" * 120
    )

    output.append(
        "SOURCE: replay_cell13_selection"
    )

    output.append(
        "=" * 120
    )

    output.append(
        replay_source
    )

    # Freeze direct helper source as well.
    for helper_name in direct_helpers:

        output.append(
            ""
        )

        output.append(
            "=" * 120
        )

        output.append(
            f"SOURCE: {helper_name}"
        )

        output.append(
            "=" * 120
        )

        output.append(
            source_segment(
                source,
                funcs[
                    helper_name
                ],
            )
        )

    TRACE_TXT.write_text(
        "\n".join(
            output
        )
        + "\n",
        encoding="utf-8",
    )

    report = {
        "stage":
            "P2_R0_05H4B1_TRAINING_MRR_SOURCE_TRACE",

        "status":
            "COMPLETE",

        "base_audit":
            str(
                BASE_AUDIT
            ),

        "source_hits":
            [
                {
                    "line":
                        lineno,

                    "term":
                        term,

                    "text":
                        line,
                }
                for lineno, term, line
                in hit_rows
            ],

        "replay_called_names":
            calls,

        "direct_local_helpers":
            direct_helpers,

        "functions_containing_train_mrr_variables":
            mrr_related_functions,

        "interpretation_boundary":
            (
                "This stage only freezes the exact source implementation "
                "used to compute training MRR. It performs no retrieval "
                "decomposition and makes no scientific claim."
            ),
    }

    REPORT_JSON.write_text(
        json.dumps(
            report,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "P2-R0-05H4B1 TRAINING-MRR "
        "SOURCE TRACE: COMPLETE"
    )

    print(
        "Functions containing train MRR variables:",
        mrr_related_functions,
    )

    print(
        "Direct local helpers:",
        direct_helpers,
    )

    print(
        "Trace:",
        TRACE_TXT,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — source frozen. "
        "Build the fold-3 training decomposition "
        "only from this observed implementation."
    )


if __name__ == "__main__":
    main()