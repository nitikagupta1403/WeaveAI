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
