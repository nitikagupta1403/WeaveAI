from __future__ import annotations

from pathlib import Path
import pandas as pd


# =============================================================================
# P2-R0-05I9 — FOLD-3 OVERLAY FOR 05I6 FROZEN EXEMPLARS
#
# Purpose
# -------
# Check whether the frozen HIGH_FREQUENCY, TEXT_SENSITIVE, and TIGHT_SUPPORT
# exemplar cohorts contain identities assigned to outer test fold 3.
#
# Important
# ---------
# "fold 3" is an identity assignment property.
# Every sketch belonging to a garment identity inherits that identity's fold_id.
#
# This stage does not alter any ranking.
# =============================================================================


BASE = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport"
)

FILES = {
    "HIGH_FREQUENCY":
        BASE / "P2_R0_05I6_top_high_frequency.csv",

    "TEXT_SENSITIVE":
        BASE / "P2_R0_05I6_top_text_sensitive.csv",

    "TIGHT_SUPPORT":
        BASE / "P2_R0_05I6_top_tight_support.csv",
}

OUT = (
    BASE
    / "P2_R0_05I9_fold3_overlay.csv"
)


def main():

    if OUT.exists():
        raise RuntimeError(
            f"Refusing to overwrite: {OUT}"
        )

    frames = []

    for cohort, path in FILES.items():

        df = pd.read_csv(
            path,
            keep_default_na=False,
        ).copy()

        required = [
            "row_index",
            "relative_path",
            "category",
            "garment_id",
            "fold_id",
        ]

        missing = [
            c
            for c in required
            if c not in df.columns
        ]

        if missing:
            raise RuntimeError(
                f"{cohort} missing columns: {missing}"
            )

        df.insert(
            0,
            "cohort",
            cohort,
        )

        df[
            "is_fold3"
        ] = (
            df[
                "fold_id"
            ].astype(int)
            == 3
        )

        frames.append(
            df
        )

    out = pd.concat(
        frames,
        ignore_index=True,
    )

    out.to_csv(
        OUT,
        index=False,
    )

    print(
        "=" * 140
    )

    print(
        "P2-R0-05I9 — FOLD-3 OVERLAY"
    )

    print(
        "=" * 140
    )

    for cohort in FILES:

        sub = out[
            out[
                "cohort"
            ]
            == cohort
        ].copy()

        print(
            f"\n{cohort}"
        )

        print(
            sub[
                [
                    "row_index",
                    "relative_path",
                    "category",
                    "garment_id",
                    "fold_id",
                    "is_fold3",
                ]
            ].to_string(
                index=False
            )
        )

        n3 = int(
            sub[
                "is_fold3"
            ].sum()
        )

        print(
            f"Fold-3 count: {n3}/{len(sub)}"
        )

    print(
        "\n"
        + "=" * 140
    )

    print(
        "P2-R0-05I9 — UNIQUE FOLD-3 IDENTITIES ACROSS ALL THREE COHORTS"
    )

    print(
        "=" * 140
    )

    fold3 = (
        out[
            out[
                "is_fold3"
            ]
        ][
            [
                "garment_id",
                "category",
                "fold_id",
            ]
        ]
        .drop_duplicates()
        .sort_values(
            [
                "category",
                "garment_id",
            ]
        )
    )

    if len(
        fold3
    ) == 0:
        print(
            "No fold-3 identities in the frozen top-12 cohorts."
        )
    else:
        print(
            fold3.to_string(
                index=False
            )
        )

    print(
        "\nP2-R0-05I9 FOLD-3 OVERLAY: COMPLETE"
    )

    print(
        "Output:",
        OUT,
    )

    print(
        "\nSTOP — compare these fold-3 identities against the H4C fold-3 "
        "difficulty result before making any interpretation."
    )


if __name__ == "__main__":
    main()