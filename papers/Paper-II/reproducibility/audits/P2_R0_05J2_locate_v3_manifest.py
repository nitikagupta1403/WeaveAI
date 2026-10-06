from pathlib import Path

ROOTS = [
    Path("/Users/nitikagupta/Research"),
    Path("/Users/nitikagupta/Desktop"),
]

print("=" * 140)
print("P2-R0-05J2 — LOCATE V3_CROP_ONLY MANIFEST")
print("=" * 140)

hits = []

for root in ROOTS:
    if not root.exists():
        continue

    for p in root.rglob("*.csv"):
        s = str(p).lower()

        if (
            "v3_crop_only" in s
            or "crop_only" in s
            or "05f" in s
        ):
            hits.append(p)

if not hits:
    print("NO CANDIDATES FOUND")
else:
    for i, p in enumerate(sorted(set(hits)), start=1):
        print(f"{i:03d}  {p}")

print("\nSTOP — send the candidate list back.")