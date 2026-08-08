# EXP-001 — Observations

Date:
2026-08

---

# Objective

Investigate the hierarchical visual representations learned by a pretrained ResNet-50 when processing fashion sketches.

---

# Initial Expectations

Expected the CNN to learn a hierarchical representation:

- Early layers would detect edges and simple contours.
- Intermediate layers would begin representing garment parts.
- Deeper layers would encode the overall garment structure.
- Similar sketches might occupy nearby locations in embedding space.

---

# Observations

## Conv1

- Strong responses along sketch contours.
- Fine edges and line strokes were clearly preserved.
- Almost every visible garment boundary was activated.

---

## Layer1

- Local curves and simple garment structures became more apparent.
- Activations were less noisy than Conv1.
- Beginning of meaningful spatial organization.

---

## Layer2

- Larger garment regions started responding.
- Sleeve-like and torso-like structures became distinguishable.
- Fine edge information was gradually reduced.

---

## Layer4

- Activation became highly abstract.
- The network no longer represented individual lines.
- Entire garment regions contributed to the representation.
- Feature maps appeared to encode semantic garment structure rather than raw pixels.

---

# Embedding Extraction

Successfully extracted:

- 2048-dimensional embedding
- Shape: (2048,)
- Float32 representation

The embedding can now be used for downstream analysis.

---

# PCA Analysis

Generated embeddings for 32 representative sketches.

Applied PCA for dimensionality reduction.

Observed:

- Sketches occupied distinct regions in embedding space.
- No obvious separation by garment category at this small sample size.
- Several nearby sketches appeared visually similar.
- The embedding space was structured rather than random.

This suggests the pretrained CNN already learns a meaningful representation of fashion sketches.

---

# Interesting Findings

The transition from low-level edges to semantic garment representations was clearly visible across network depth.

Layer4 contained highly abstract information compared with Conv1.

The PCA visualization suggested that embeddings preserve visual similarity despite the network never being trained specifically on fashion sketches.

---

# Limitations

- Only 32 representative sketches were analyzed.
- PCA captures only two principal components.
- No quantitative clustering metrics were computed.
- The network was ImageNet pretrained and not fine-tuned on fashion sketches.

---

# Questions Raised

- Would UMAP reveal clearer semantic clusters?
- Would fine-tuning improve category separation?
- Which garment primitives contribute most to the embedding?
- Are sleeves more influential than necklines?
- How stable are embeddings under controlled sketch modifications?

---

# Next Experiment

EXP-002 — Looking Through the CNN's Eyes with Grad-CAM

Goal:

Identify which regions of a sketch contribute most strongly to the learned representation.
