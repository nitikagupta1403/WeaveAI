from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "CLO_SKET_IVC_Manuscript.md"

# Canonical IVC submission sources only. Do not assemble from the legacy
# CLO_SKET_Final_* files; those are retained for provenance/archive purposes.
SECTIONS = [
    "CLO_SKET_IVC_Abstract.md",
    "CLO_SKET_IVC_Introduction.md",
    "CLO_SKET_IVC_Related_Work.md",
    "CLO_SKET_IVC_Methods.md",
    "CLO_SKET_IVC_Results.md",
    "CLO_SKET_IVC_Discussion.md",
    "CLO_SKET_IVC_Conclusion.md",
]

FRONT_MATTER = r'''# Garment Sketches: Axial–Radial Geometry and Identity-Aware Validation

> **Submission front matter to complete before journal upload**
>
> - Author names: [TO BE CONFIRMED]
> - Affiliations: [TO BE CONFIRMED]
> - Corresponding author and email: [TO BE CONFIRMED]
>
> **Source-of-truth rule:** the files listed in `SECTIONS` above are the canonical IVC scientific sources. `CLO_SKET_IVC_Manuscript.md` is generated from them and should not be edited independently. Legacy `CLO_SKET_Final_*`, `CLO_SKET_IVC_Main.md`, and files under `Reserve/` are retained only for provenance and comparison.

'''

DECLARATIONS = r'''

# Declarations

## Funding

[TO BE COMPLETED TRUTHFULLY BEFORE SUBMISSION]

## Competing interests

[TO BE COMPLETED TRUTHFULLY BEFORE SUBMISSION]

## Author contributions (CRediT)

[TO BE COMPLETED TRUTHFULLY BEFORE SUBMISSION]

## Acknowledgements

[TO BE COMPLETED IF APPLICABLE]

## Ethics statement

[TO BE COMPLETED IF REQUIRED BY THE JOURNAL; DO NOT ADD AN ETHICS APPROVAL CLAIM UNLESS APPLICABLE]

## Data and code availability

[TO BE REBUILT ONLY AFTER THE PUBLIC REPOSITORY CONTENT HAS BEEN VERIFIED. DO NOT CLAIM PUBLIC AVAILABILITY OF THE EXPERIMENT 06 EVIDENCE BUNDLE UNTIL IT IS PRESENT AND ACCESSIBLE.]
'''

REFERENCES_NOTE = r'''

# References

The canonical bibliography for journal typesetting is maintained in `CLO_SKET_References.bib`. Citation formatting should be generated from that file using the final Image and Vision Computing / Elsevier bibliography style rather than manually duplicating the bibliography here.
'''


def read_required(name: str) -> str:
    path = ROOT / name
    if not path.exists():
        raise FileNotFoundError(f"Required manuscript source is missing: {path}")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Required manuscript source is empty: {path}")
    return text


def main() -> None:
    parts = [FRONT_MATTER.rstrip()]
    for name in SECTIONS:
        parts.append(read_required(name))
    parts.append(DECLARATIONS.strip())
    parts.append(REFERENCES_NOTE.strip())
    master = "\n\n---\n\n".join(parts) + "\n"
    OUT.write_text(master, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT.parent.parent)}")
    print(f"Characters: {len(master):,}")
    print(f"Canonical scientific source sections: {len(SECTIONS)}")


if __name__ == "__main__":
    main()
