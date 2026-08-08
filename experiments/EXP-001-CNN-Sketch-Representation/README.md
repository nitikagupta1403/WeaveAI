# EXP-001

## Research Question

What hierarchical visual representations does a pretrained CNN learn from fashion sketches?

---

## Motivation

Fashion sketches are sparse line drawings.
Before designing sketch-specific architectures,
it is important to understand how a generic
computer vision model interprets them.

---

## Hypothesis

Early CNN layers respond to local visual
primitives (edges, contours, decorative motifs),
whereas deeper layers progressively encode
higher-level garment representations.

---

## Dataset

- 333 fashion sketches
- Generated from Pinterest garment images
- 16 garment categories
- One representative sample selected from each category

---

## Experimental Pipeline

Sketch
↓
Resize (224×224)
↓
RGB conversion
↓
ImageNet normalization
↓
Pretrained ResNet-50
↓
Forward hooks
↓
Conv1
Layer1
Layer2
Layer3
Layer4





### PCA Embedding Analysis

**Method**
- Extracted 2048-dimensional embeddings from a pretrained ResNet-50.
- Sample: 32 sketches (2 randomly selected from each garment category).
- Reduced dimensionality using PCA.

**Observations**
- The first two principal components explain approximately 20% of the embedding variance.
- No clear category-wise clustering is observed.
- Several local neighborhoods suggest visually similar sketches produce similar embeddings.
- A few sketches appear as isolated outliers and will be investigated in later experiments.
- The embedding space appears to remain highly high-dimensional.

**Conclusion**
A pretrained ImageNet ResNet-50 captures meaningful visual information from fashion sketches, but the representation is not naturally organized into well-separated garment categories. This motivates further analysis using Grad-CAM, perturbation studies, and sketch-specific representation learning.
