#!/usr/bin/env python3
"""Audit the public Paper-II provenance release without executing analysis."""

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_ROOT = ROOT.parent
PROVENANCE = ROOT / "provenance"
DOWNSTREAM = PROVENANCE / "CLO_SKET_Probabilistic_Fourier_Morphology_FROZEN_EXECUTED.ipynb"
UPSTREAM = PROVENANCE / "CLO_Raw_fft_UPSTREAM_GENERATOR.ipynb"
MANUSCRIPT = PAPER_ROOT / "P2_19_MANUSCRIPT_MASTER.md"
VALUES = ROOT / "figures" / "frozen_reported_values.json"


def check(condition, message):
    if not condition:
        raise RuntimeError(message)
    print(f"PASS  {message}")


def verify_hashes():
    for line in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        expected, relative = line.split(maxsplit=1)
        path = ROOT / relative
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        check(observed == expected, f"SHA-256 {relative}")


def notebook_contract(path, expected_code_cells, expected_executed):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    code = [cell for cell in notebook["cells"] if cell.get("cell_type") == "code"]
    executed = [cell for cell in code if cell.get("execution_count") is not None]
    check(len(code) == expected_code_cells, f"{path.name}: {expected_code_cells} code cells")
    check(len(executed) == expected_executed, f"{path.name}: {expected_executed} executed code cells")
    return notebook


def main():
    verify_hashes()
    notebook_contract(UPSTREAM, 78, 76)
    downstream = notebook_contract(DOWNSTREAM, 46, 45)
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    notebook_text = json.dumps(downstream, ensure_ascii=False)

    anchors = [
        ("population", ("2,300", "2300")),
        ("garment identities", ("230 garment identities", "Garment identities")),
        ("categories", ("23 categories", "Categories")),
        ("radial shells", ("72-shell", "72")),
        ("positive harmonics", ("k=1,\\ldots,36", "36")),
        ("full complex dimension", ("2,592", "2592")),
        ("hybrid complex dimension", ("1,504", "1504")),
        ("full real dimension", ("5184", "5184")),
        ("hybrid real dimension", ("3008", "3008")),
        ("coefficient reduction", ("41.98%", "41.98")),
        ("low-band effect", ("0.059306", "0.059306")),
        ("low-band adjusted p", ("0.000200", "0.000200")),
        ("first intermediate effect", ("0.005984", "0.005984")),
        ("second intermediate effect", ("0.010959", "0.010959")),
        ("high-band effect", ("0.039300", "0.039300")),
        ("high-band adjusted p", ("0.019698", "0.019698")),
        ("largest nonlinear contrast", ("0.014341", "0.014341")),
        ("nonlinear adjusted p", ("0.2500", "0.25")),
        ("quadratic delta R2", ("0.432042", "0.432042")),
        ("PCA64 retained variance", ("44.65%", "0.446455")),
        ("local dimension", ("median number of directions required", "15")),
        ("localization fractions", ("78.54%", "0.785350", "0.668410", "0.513031")),
    ]
    for name, needles in anchors:
        check(needles[0] in manuscript, f"manuscript anchor: {name}")
        for needle in needles[1:]:
            check(needle in notebook_text, f"notebook anchor: {name} contains {needle}")

    tables = [int(value) for value in re.findall(r"(?m)^### Table (\d+)\.", manuscript)]
    check(tables == [1, 2, 3], "table numbering is 1, 2, 3")

    values = json.loads(VALUES.read_text(encoding="utf-8"))
    check(values["representation_dimensions"]["hybrid_complex"] == 1504, "reported-values schema")
    check(values["pca64_localization"]["outer_by_intermediate"] == 0.513031, "reported localization value")

    seeds = sorted(set(re.findall(r"20260\d{3}", notebook_text)))
    required_seeds = {"20260821", "20260913", "20260914"}
    check(required_seeds.issubset(seeds), "frozen manuscript seeds are discoverable")
    print(f"INFO  discovered frozen-date seeds: {', '.join(seeds)}")
    print("\nPaper-II public provenance audit: PASS")


if __name__ == "__main__":
    main()
