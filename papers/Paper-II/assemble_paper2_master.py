from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

TITLE = "Evidence-Controlled Radial–Spectral Representation of Garment-Sketch Morphology"
AUTHOR = "NITIKA GUPTA"
OUT = ROOT / "P2_19_MANUSCRIPT_MASTER.md"


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def clean_section_body(body):
    """Remove source-file boundary rules so the assembler owns section spacing."""
    body = body.strip()
    body = re.sub(r"\A(?:\s*---\s*)+", "", body)
    body = re.sub(r"(?:\s*---\s*)+\Z", "", body)
    return body.strip()


def section(text, start, end=None):
    """Extract a manuscript section beginning at an exact Markdown H1 heading."""
    pat = (
        rf"(?ms)^# {re.escape(start)}\s*\n(.*?)(?=^# {re.escape(end)}\s*$|\Z)"
        if end
        else rf"(?ms)^# {re.escape(start)}\s*\n(.*)\Z"
    )
    m = re.search(pat, text)
    if not m:
        raise RuntimeError(f"Could not extract section: {start}")
    return f"# {start}\n\n" + clean_section_body(m.group(1)) + "\n"


intro_rw = read("P2_11_INTRODUCTION_RELATED_WORK.md")
methods = read("P2_08_METHODS_FINAL.md")
results = read("P2_09_RESULTS_FINAL.md")
discussion = read("P2_10_DISCUSSION_FINAL.md")
front = read("P2_12_ABSTRACT_TITLE_KEYWORDS.md")
conclusion = read("P2_13_CONCLUSION_FINAL.md")
legacy = read("P2_18_CVIU_CITATION_INTEGRATED_MANUSCRIPT.md")
figure_captions = read("P2_21_FIGURE_CAPTIONS_CVIU_FINAL.md")
references = read("P2_14_REFERENCES_FINAL.md")

abstract = section(front, "Abstract", "Keywords")
keywords = section(front, "Keywords", "Running title")
intro = section(intro_rw, "1. Introduction", "2. Related Work")
related = section(intro_rw, "2. Related Work")
methods_s = section(methods, "3. Methods")
results_s = section(results, "4. Results")
discussion_s = section(discussion, "5. Discussion")
conclusion_s = section(conclusion, "6. Conclusion")
data_av = section(legacy, "Data Availability", "Code Availability")
code_av = section(legacy, "Code Availability", "References")
captions_s = section(figure_captions, "Figure Captions")
refs = section(references, "References")

master = "\n\n---\n\n".join([
    f"# {TITLE}\n\n**{AUTHOR}**",
    abstract,
    keywords,
    intro,
    related,
    methods_s,
    results_s,
    discussion_s,
    conclusion_s,
    data_av,
    code_av,
    captions_s,
    refs,
]).strip() + "\n"

for forbidden in [
    "[CITATIONS]",
    "They did not.",
    "radial representation requirements are harmonic-scale dependent",
    "radial representation requirements and retained latent morphology vary systematically",
    "Step 9 lock",
    "Results claim boundary",
    "MANUSCRIPT ASSEMBLY DRAFT",
    "Local geometry was evaluated in the descriptive PCA-64 score space",
    "Peak radial–harmonic coordinates for all 64 retained PCA axes",
    "0.0245",
    "local/global ratio",
    "This train-only preprocessing prevents information from held-out garment identities entering latent-model construction.",
]:
    if forbidden.lower() in master.lower():
        raise RuntimeError(f"Forbidden stale manuscript text detected: {forbidden}")

required = [
    TITLE,
    AUTHOR,
    "# Abstract",
    "Compact spectral shape descriptors commonly apply one encoding rule",
    "# 1. Introduction",
    "# 2. Related Work",
    "# 3. Methods",
    "# 4. Results",
    "# 5. Discussion",
    "# 6. Conclusion",
    "# Data Availability",
    "# Code Availability",
    "# Figure Captions",
    "# References",
    "2592",
    "1504",
    "41.98%",
    "rank at most 19",
    "conditional on that previously selected hybrid representation",
    "w(x,y)=\\max\\{255-I(x,y),0\\}",
    "R_{\\mathrm{norm}}(x,y)=\\frac{R(x,y)}{R_{\\max}}",
    "10^{-14}",
    "44.65%",
    "78.54%",
    "66.84%",
    "51.30%",
    "Spectral-centroid × radial-centroid localization",
    "Zhang and Lu, 2002",
    "An and Li (2014)",
    "Jolliffe and Cadima, 2016",
    "Hinton and Salakhutdinov, 2006",
    "Kingma and Welling, 2014",
]
for token in required:
    if token not in master:
        raise RuntimeError(f"Required manuscript token missing: {token}")

# Final assembly hygiene: section boundaries must contain exactly one rule.
if re.search(r"(?m)^---\s*\n\s*---\s*$", master):
    raise RuntimeError("Duplicate horizontal-rule boundary detected")

# Guard against accidental duplicate top-level manuscript sections.
for heading in [
    "Abstract", "Keywords", "1. Introduction", "2. Related Work", "3. Methods",
    "4. Results", "5. Discussion", "6. Conclusion", "Data Availability",
    "Code Availability", "Figure Captions", "References",
]:
    n = len(re.findall(rf"(?m)^# {re.escape(heading)}\s*$", master))
    if n != 1:
        raise RuntimeError(f"Expected exactly one '# {heading}' heading; found {n}")

OUT.write_text(master, encoding="utf-8")
print(f"Wrote {OUT}")
print(f"Words: {len(master.split()):,}")
