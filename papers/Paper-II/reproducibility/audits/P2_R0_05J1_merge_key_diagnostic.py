from pathlib import Path
import pandas as pd

I8 = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport/"
    "P2_R0_05I8_robust_support_metric_audit/"
    "P2_R0_05I8_per_image_robust_support_metrics.csv"
)

I2 = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I2_per_image_band_fraction_change.csv"
)

a = pd.read_csv(I8, keep_default_na=False)
b = pd.read_csv(I2, keep_default_na=False)

print("=" * 140)
print("P2-R0-05J1 — MERGE-KEY DIAGNOSTIC")
print("=" * 140)

print("\nI8 rows:", len(a))
print("I2 rows:", len(b))

print("\nI8 columns:")
print(list(a.columns))

print("\nI2 columns:")
print(list(b.columns))

# ---------------------------------------------------------------------
# Row-index diagnostics
# ---------------------------------------------------------------------

print("\n" + "-" * 140)
print("ROW_INDEX")
print("-" * 140)

print("I8 unique row_index:", a["row_index"].nunique())
print("I2 unique row_index:", b["row_index"].nunique())

m_row = a.merge(
    b,
    on="row_index",
    how="inner",
    suffixes=("_i8", "_i2"),
    validate="one_to_one",
)

print("Merge on row_index only:", len(m_row))

# ---------------------------------------------------------------------
# Compare fields after row_index-only alignment
# ---------------------------------------------------------------------

pairs = [
    ("relative_path", "relative_path"),
    ("category", "category"),
    ("fold_id", "fold_id"),
]

for x, y in pairs:
    left = f"{x}_i8"
    right = f"{y}_i2"

    if left in m_row.columns and right in m_row.columns:
        same = (m_row[left].astype(str) == m_row[right].astype(str))
        print(f"{x}: exact matches {int(same.sum())}/{len(same)}")

        bad = m_row.loc[
            ~same,
            [
                "row_index",
                left,
                right,
            ],
        ].head(15)

        if len(bad):
            print(f"\nFirst mismatches for {x}:")
            print(bad.to_string(index=False))

# ---------------------------------------------------------------------
# Relative path-only diagnostics
# ---------------------------------------------------------------------

print("\n" + "-" * 140)
print("RELATIVE_PATH")
print("-" * 140)

print("I8 unique relative_path:", a["relative_path"].nunique())
print("I2 unique relative_path:", b["relative_path"].nunique())

m_path = a.merge(
    b,
    on="relative_path",
    how="inner",
    suffixes=("_i8", "_i2"),
)

print("Merge on relative_path only:", len(m_path))

# ---------------------------------------------------------------------
# Normalized relative path diagnostics
# ---------------------------------------------------------------------

def norm_path(s):
    return (
        s.astype(str)
        .str.replace("\\\\", "/", regex=False)
        .str.strip()
        .str.lower()
    )

a2 = a.copy()
b2 = b.copy()

a2["_norm_path"] = norm_path(a2["relative_path"])
b2["_norm_path"] = norm_path(b2["relative_path"])

m_norm = a2.merge(
    b2,
    on="_norm_path",
    how="inner",
    suffixes=("_i8", "_i2"),
)

print("Merge on normalized relative_path:", len(m_norm))

# ---------------------------------------------------------------------
# Row-index offset test
# ---------------------------------------------------------------------

print("\n" + "-" * 140)
print("ROW_INDEX OFFSET CHECK")
print("-" * 140)

for offset in range(-5, 6):
    hits = len(
        a.assign(_k=a["row_index"] + offset).merge(
            b[["row_index"]],
            left_on="_k",
            right_on="row_index",
            how="inner",
        )
    )
    print(f"offset {offset:+d}: {hits}")

print("\nSTOP — send this diagnostic output before patching 05J again.")