from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "CLO_SKET_IVC_Manuscript.md"

SECTIONS = [
    "CLO_SKET_Final_Abstract.md",
    "CLO_SKET_Final_Introduction.md",
    "CLO_SKET_Final_Related_Work.md",
    "CLO_SKET_Final_Methods.md",
    "CLO_SKET_Final_Results.md",
    "CLO_SKET_Final_Discussion.md",
    "CLO_SKET_Final_Conclusion.md",
    "CLO_SKET_Availability_and_Reproducibility.md",
]

FRONT_MATTER = r'''# CLO-SKET — IVC Submission Manuscript

> **Submission front matter to complete before journal upload**
>
> - Final manuscript title: [TO BE CONFIRMED]
> - Author names: [TO BE CONFIRMED]
> - Affiliations: [TO BE CONFIRMED]
> - Corresponding author and email: [TO BE CONFIRMED]
>
> The scientific body below is assembled from the frozen repository source files. Do not edit scientific claims in this master independently; edit the canonical source section and rebuild instead.

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
    print(f"Source sections: {len(SECTIONS)}")


if __name__ == "__main__":
    main()
