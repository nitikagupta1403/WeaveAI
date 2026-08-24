from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

TITLE = "Garment-Sketch Morphology Radial-Spectral Representation: Evidence-Controlled Conditional Compression"
AUTHOR = "NITIKA GUPTA"
OUT = ROOT / "P2_19_MANUSCRIPT_MASTER.md"


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def section(text, start, end=None):
    """Extract a manuscript section beginning at an exact Markdown H1 heading."""
    pat = rf"(?ms)^# {re.escape(start)}\s*\n(.*?)(?=^# {re.escape(end)}\s*$|\Z)" if end else rf"(?ms)^# {re.escape(start)}\s*\n(.*)\Z"
    m = re.search(pat, text)
    if not m:
        raise RuntimeError(f"Could not extract section: {start}")
    return f"# {start}\n\n" + m.group(1).strip() + "\n"


intro_rw = read("P2_11_INTRODUCTION_RELATED_WORK.md")
methods = read("P2_08_METHODS_FINAL.md")
results = read("P2_09_RESULTS_FINAL.md")
discussion = read("P2_10_DISCUSSION_FINAL.md")
front = read("P2_12_ABSTRACT_TITLE_KEYWORDS.md")
conclusion = read("P2_13_CONCLUSION_FINAL.md")
legacy = read("P2_18_CVIU_CITATION_INTEGRATED_MANUSCRIPT.md")

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
refs = section(legacy, "References")

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
    refs,
]).strip() + "\n"

for forbidden in [
    "[CITATIONS]",
    "They did not.",
    "radial representation requirements are harmonic-scale dependent",
    "radial representation requirements and retained latent morphology vary systematically",
    "Evidence-Controlled Radial-Spectral Representation of Garment-Sketch Morphology",
    "Step 9 lock",
    "Results claim boundary",
    "MANUSCRIPT ASSEMBLY DRAFT",
]:
    if forbidden.lower() in master.lower():
        raise RuntimeError(f"Forbidden stale manuscript text detected: {forbidden}")

required = [
    TITLE,
    AUTHOR,
    "# Abstract",
    "# 1. Introduction",
    "# 2. Related Work",
    "# 3. Methods",
    "# 4. Results",
    "# 5. Discussion",
    "# 6. Conclusion",
    "# Data Availability",
    "# Code Availability",
    "# References",
    "2592",
    "1504",
    "41.98%",
    "44.65%",
    "78.54%",
    "66.84%",
    "51.30%",
]
for token in required:
    if token not in master:
        raise RuntimeError(f"Required manuscript token missing: {token}")

OUT.write_text(master, encoding="utf-8")
print(f"Wrote {OUT}")
print(f"Words: {len(master.split()):,}")
