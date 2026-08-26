from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import balanced_accuracy_score, f1_score


# =============================================================================
# FROZEN CONTRACT
# =============================================================================

HERE = Path(__file__).resolve().parent
PAPER_ROOT = HERE.parent.parent
EVIDENCE = PAPER_ROOT / "evidence" / "Experiment_08"

OOF_PATH = EVIDENCE / "experiment08_secondary_morphology_oof_predictions.csv"
PRIMARY_PATH = EVIDENCE / "experiment08_secondary_morphology_point_estimate.json"

BOOTSTRAP_PATH = EVIDENCE / "experiment08_secondary_morphology_bootstrap.csv"
SUMMARY_PATH = EVIDENCE / "experiment08_secondary_morphology_bootstrap_summary.csv"

SEED = 20260821
N_BOOTSTRAP = 10_000
EXPECTED_ROWS = 2300
EXPECTED_CATEGORIES = 23
EXPECTED_IDENTITIES = 230


# =============================================================================
# HELPERS
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def metrics(y_true, y_pred):
    return (
        f1_score(
            y_true,
            y_pred,
            average="macro",
        ),
        balanced_accuracy_score(
            y_true,
            y_pred,
        ),
    )


# =============================================================================
# INPUT VERIFICATION
# =============================================================================

print("=" * 88)
print("EXPERIMENT 08 — SECONDARY MORPHOLOGY IDENTITY BOOTSTRAP")
print("=" * 88)

for path in [OOF_PATH, PRIMARY_PATH]:
    if not path.is_file():
        raise RuntimeError(f"Missing frozen input: {path}")

oof = pd.read_csv(
    OOF_PATH,
    keep_default_na=False,
)

required = {
    "row_index",
    "relative_path",
    "category",
    "garment_id",
    "fold_id",
    "prediction_M",
    "prediction_M_plus_G",
}

missing = required.difference(oof.columns)

if missing:
    raise RuntimeError(
        f"OOF file missing columns: {sorted(missing)}"
    )

if len(oof) != EXPECTED_ROWS:
    raise RuntimeError(
        f"Expected {EXPECTED_ROWS} OOF rows, found {len(oof)}"
    )

if oof["row_index"].tolist() != list(range(EXPECTED_ROWS)):
    raise RuntimeError("OOF row order is not exactly 0..2299")

if oof["relative_path"].nunique() != EXPECTED_ROWS:
    raise RuntimeError("OOF relative paths are not unique")

if oof["category"].nunique() != EXPECTED_CATEGORIES:
    raise RuntimeError("Expected 23 categories")

if oof["garment_id"].nunique() != EXPECTED_IDENTITIES:
    raise RuntimeError("Expected 230 garment identities")

if (oof.groupby("garment_id")["category"].nunique() != 1).any():
    raise RuntimeError(
        "At least one recovered garment identity spans multiple categories"
    )

primary = json.loads(
    PRIMARY_PATH.read_text(encoding="utf-8")
)

if primary.get("secondary_estimand") != (
    "macro_F1(M_plus_G) - macro_F1(M)"
):
    raise RuntimeError("Secondary morphology estimand differs from frozen definition")

if primary.get("identity_bootstrap_completed") is not False:
    raise RuntimeError(
        "Secondary morphology point-estimate record does not show bootstrap as pending"
    )


# =============================================================================
# VERIFY ORIGINAL POOLED POINT ESTIMATE
# =============================================================================

y = oof["category"].to_numpy()

pred_M = oof["prediction_M"].to_numpy()
pred_MG = oof["prediction_M_plus_G"].to_numpy()

f1_M, ba_M = metrics(y, pred_M)
f1_MG, ba_MG = metrics(y, pred_MG)

delta_f1 = f1_MG - f1_M
delta_ba = ba_MG - ba_M

if not np.isclose(
    delta_f1,
    float(primary["delta_G_given_M"]),
    rtol=0.0,
    atol=1e-15,
):
    raise RuntimeError(
        "OOF predictions do not reproduce frozen secondary morphology delta"
    )

print("\nFROZEN SECONDARY MORPHOLOGY POINT ESTIMATE")
print("-" * 88)
print(f"macro-F1 M        : {f1_M:.9f}")
print(f"macro-F1 M+G      : {f1_MG:.9f}")
print(f"Delta G|M         : {delta_f1:+.9f}")
print(f"Balanced acc M    : {ba_M:.9f}")
print(f"Balanced acc M+G  : {ba_MG:.9f}")
print(f"Delta BA          : {delta_ba:+.9f}")

print("\nINPUT HASHES")
print("-" * 88)
print("OOF SHA-256       :", sha256_file(OOF_PATH))
print("Secondary JSON SHA  :", sha256_file(PRIMARY_PATH))


# =============================================================================
# FROZEN IDENTITY STRUCTURE
# =============================================================================

categories = sorted(oof["category"].unique().tolist())

category_identity_rows = {}

for category in categories:

    category_frame = oof[
        oof["category"] == category
    ]

    identities = sorted(
        category_frame["garment_id"]
        .unique()
        .tolist()
    )

    if len(identities) != 10:
        raise RuntimeError(
            f"{category}: expected 10 garment identities, "
            f"found {len(identities)}"
        )

    identity_rows = {}

    for garment_id in identities:
        idx = np.flatnonzero(
            oof["garment_id"].to_numpy()
            == garment_id
        )

        if idx.size == 0:
            raise RuntimeError(
                f"No rows for identity {garment_id}"
            )

        identity_rows[garment_id] = idx

    category_identity_rows[category] = (
        identities,
        identity_rows,
    )

print("\nIDENTITY STRUCTURE")
print("-" * 88)
print("Categories            :", len(categories))
print("Identities/category   : 10")
print("Total identities      :", oof["garment_id"].nunique())
print("Bootstrap replicates  :", N_BOOTSTRAP)
print("Seed                  :", SEED)


# =============================================================================
# BOOTSTRAP
#
# Sample recovered identities WITH replacement separately within category.
# Every row from each sampled identity is included.
# The same sampled rows are used for L and L+G.
# =============================================================================

rng = np.random.default_rng(SEED)

records = []

for b in range(N_BOOTSTRAP):

    sampled_blocks = []

    for category in categories:

        identities, identity_rows = (
            category_identity_rows[category]
        )

        sampled_identities = rng.choice(
            identities,
            size=len(identities),
            replace=True,
        )

        for garment_id in sampled_identities:
            sampled_blocks.append(
                identity_rows[garment_id]
            )

    sampled_idx = np.concatenate(
        sampled_blocks
    )

    y_b = y[sampled_idx]

    pred_M_b = pred_M[sampled_idx]
    pred_MG_b = pred_MG[sampled_idx]

    f1_M_b, ba_M_b = metrics(
        y_b,
        pred_M_b,
    )

    f1_MG_b, ba_MG_b = metrics(
        y_b,
        pred_MG_b,
    )

    records.append({
        "bootstrap_rep": b,
        "n_rows": int(sampled_idx.size),

        "macro_f1_M": f1_M_b,
        "macro_f1_M_plus_G": f1_MG_b,
        "delta_macro_f1_G_given_M":
            f1_MG_b - f1_M_b,

        "balanced_accuracy_M": ba_M_b,
        "balanced_accuracy_M_plus_G": ba_MG_b,
        "delta_balanced_accuracy_G_given_M":
            ba_MG_b - ba_M_b,
    })

    if (
        (b + 1) % 1000 == 0
        or b == N_BOOTSTRAP - 1
    ):
        print(
            f"bootstrap {b + 1}/{N_BOOTSTRAP}",
            flush=True,
        )


# =============================================================================
# SAVE COMPLETE DISTRIBUTION
# =============================================================================

bootstrap = pd.DataFrame(records)

bootstrap.to_csv(
    BOOTSTRAP_PATH,
    index=False,
)


# =============================================================================
# PERCENTILE 95% INTERVALS
# =============================================================================

def percentile_summary(
    name,
    values,
    point_estimate,
):
    values = np.asarray(
        values,
        dtype=float,
    )

    return {
        "estimand": name,
        "point_estimate": point_estimate,
        "bootstrap_mean": float(
            np.mean(values)
        ),
        "bootstrap_median": float(
            np.median(values)
        ),
        "ci95_lower": float(
            np.percentile(values, 2.5)
        ),
        "ci95_upper": float(
            np.percentile(values, 97.5)
        ),
        "n_bootstrap": N_BOOTSTRAP,
        "seed": SEED,
    }


summary = pd.DataFrame([
    percentile_summary(
        "macro_f1_M",
        bootstrap["macro_f1_M"],
        f1_M,
    ),

    percentile_summary(
        "macro_f1_M_plus_G",
        bootstrap["macro_f1_M_plus_G"],
        f1_MG,
    ),

    percentile_summary(
        "delta_macro_f1_G_given_M",
        bootstrap[
            "delta_macro_f1_G_given_M"
        ],
        delta_f1,
    ),

    percentile_summary(
        "balanced_accuracy_M",
        bootstrap[
            "balanced_accuracy_M"
        ],
        ba_M,
    ),

    percentile_summary(
        "balanced_accuracy_M_plus_G",
        bootstrap[
            "balanced_accuracy_M_plus_G"
        ],
        ba_MG,
    ),

    percentile_summary(
        "delta_balanced_accuracy_G_given_M",
        bootstrap[
            "delta_balanced_accuracy_G_given_M"
        ],
        delta_ba,
    ),
])

summary["bootstrap_distribution_sha256"] = (
    sha256_file(BOOTSTRAP_PATH)
)

summary["source_oof_sha256"] = (
    sha256_file(OOF_PATH)
)

summary["source_secondary_json_sha256"] = (
    sha256_file(PRIMARY_PATH)
)

summary.to_csv(
    SUMMARY_PATH,
    index=False,
)


# =============================================================================
# DISPLAY — NO CLAIM INFLATION
# =============================================================================

delta_row = summary[
    summary["estimand"]
    == "delta_macro_f1_G_given_M"
].iloc[0]

lower = float(delta_row["ci95_lower"])
upper = float(delta_row["ci95_upper"])

print("\n" + "=" * 88)
print("IDENTITY BOOTSTRAP COMPLETE")
print("=" * 88)

print(
    summary.to_string(
        index=False,
        float_format=lambda x: f"{x:.9f}",
    )
)

print("\nSECONDARY CONTRAST")
print("-" * 88)
print(
    f"Delta G|M point estimate : "
    f"{delta_f1:+.9f}"
)
print(
    f"Percentile 95% CI        : "
    f"[{lower:+.9f}, {upper:+.9f}]"
)

print("\nSaved:")
print(" ", BOOTSTRAP_PATH)
print(" ", SUMMARY_PATH)

print("\nINTERPRETATION FIREWALL")
print("-" * 88)

if lower > 0:
    if delta_f1 >= 0.01:
        print(
            "Bootstrap criterion: positive interval; "
            "point estimate >= 0.01."
        )
    else:
        print(
            "Bootstrap criterion: positive interval; "
            "point estimate < 0.01."
        )
else:
    print(
        "Bootstrap criterion: interval does not exclude zero."
    )

print(
    "Final predictive interpretation remains conditional "
    "on completion of the separately frozen mechanical "
    "validity gate."
)