# Publication-figure reproducibility layer

The public notebooks preserve embedded historical plots, but the current release
does not include the complete frozen arrays needed to regenerate all final
multi-panel publication figures faithfully.

`frozen_reported_values.json` records only values explicitly reported in the
frozen manuscript. `export_reported_summary.py` converts those values into
reviewer-auditable CSV tables. It does not rerun inference and does not present
newly drawn charts as replacements for the final figures.

Exact regeneration still requires:

- Figure 1: source image examples or frozen schematic assets;
- Figure 2: category/bootstrap-level plotting objects and final layout code;
- Figure 3: all five fold-level contrasts and quadratic-audit plotting objects;
- Figure 4: the 64 inverse-mapped morphology fields, 3×4 localization matrix and
  centroid coordinates.

These missing objects must be exported from the trusted historical archive
before the manuscript can claim complete figure reproducibility.
