# EXP-001 — CNN Sketch Representation

## Objective

To investigate how a pretrained ResNet-50 represents fashion sketches and to understand the progression of visual information from low-level edge detection to high-level semantic representations.

---

## Research Question

How does a pretrained convolutional neural network transform fashion sketches into feature representations, and do these representations exhibit meaningful structure in the embedding space?

---

## Dataset

- Fashion sketch dataset
- 16 garment categories
- Two representative sketches randomly selected from each category
- Total sketches used: **32**

The reduced dataset was intentionally chosen to facilitate manual inspection and interpretation during exploratory analysis.

---

## Model

**Architecture**

- ResNet-50
- ImageNet pretrained weights

Only the feature extractor was used.

The final fully connected classification layer was removed.

The extracted embedding dimension was:

2048

---

## Experimental Pipeline

Fashion Sketch

↓

Image Preprocessing

↓

Pretrained ResNet-50

↓

Feature Maps

- Conv1
- Layer1
- Layer2
- Layer4

↓

2048-dimensional Embedding

↓

Principal Component Analysis (PCA)

↓

Visualization and Interpretation

---

## Results

### Feature Hierarchy

The visualization of intermediate feature maps demonstrated the hierarchical nature of CNN representations.

**Conv1**

- Strong activation along garment boundaries
- Detection of edges and simple line orientations
- Preservation of sketch contours

**Layer1**

- Combination of low-level edges into larger local structures
- Early garment components begin to emerge

**Layer2**

- Increased semantic organization
- Responses correspond to larger garment regions such as sleeves and torso

**Layer4**

- Highly abstract representation
- Fine edge information is largely discarded
- Global garment structure dominates the representation

---

## Embedding Analysis

The final 2048-dimensional embeddings were extracted for all 32 sketches.

Principal Component Analysis was performed.

Variance explained:

- PC1 = 10.82%
- PC2 = 9.52%

Total explained variance:

Approximately 20.3%

The PCA visualization revealed:

- distributed embedding space
- several local neighborhoods
- a small number of isolated outliers
- no strong category-wise separation using the pretrained ImageNet representation

---

## Discussion

The experiment demonstrates that a generic pretrained ResNet-50 produces meaningful hierarchical representations for fashion sketches despite not being trained specifically on sketch data.

Low-level layers preserve contour information while deeper layers encode increasingly abstract garment representations.

Although the PCA embedding space exhibits local organization, clear garment-category clustering is not yet observed, suggesting that additional domain adaptation or sketch-specific representation learning may be beneficial.

---

## Limitations

- Small exploratory dataset (32 sketches)
- PCA captures only approximately 20% of the embedding variance
- No quantitative similarity analysis performed in this experiment
- Embeddings obtained from a network pretrained on natural images rather than fashion sketches

---

## Future Work

- Grad-CAM visualization
- Cosine similarity analysis
- Nearest-neighbor retrieval
- UMAP visualization
- Primitive perturbation experiments
- Sketch-specific representation learning

---

## Figures

- Conv1 feature maps
- Layer1 feature maps
- Layer2 feature maps
- Layer4 feature maps
- PCA embedding visualization

---

## Conclusion

This experiment establishes a reproducible baseline for understanding how pretrained convolutional neural networks represent fashion sketches. The extracted embeddings provide the foundation for subsequent experiments on interpretability, similarity analysis, and fashion-specific representation learning.
