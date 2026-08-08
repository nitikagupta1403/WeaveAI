# EXP-002 — Looking Through the CNN's Eyes with Grad-CAM

## Objective

Visualize which regions of a fashion sketch contribute most strongly to the representation learned by a pretrained ResNet-50 using Grad-CAM.

---

## Research Question

Which garment regions receive the highest attention in the final convolutional layer of a pretrained CNN?

---

## Model

- Architecture: ResNet-50
- Weights: ImageNet pretrained
- Layer analyzed: layer4

---

## Dataset

Representative fashion sketches selected from the WeaveAI dataset.

---

## Method

1. Select a representative sketch.
2. Register forward and backward hooks on ResNet-50 layer4.
3. Compute gradients with respect to the predicted class.
4. Generate the Grad-CAM heatmap.
5. Overlay the heatmap on the original sketch.

---

## Results

The strongest activation occurred around the upper decorative region of the garment, indicating that the pretrained representation focused on highly distinctive structural and decorative features rather than treating all garment regions equally.

---

## Figures

- gradcam_overlay.png

---

## Key Observation

The Grad-CAM attention map demonstrates that the pretrained ResNet-50 emphasizes localized garment structures, suggesting that discriminative visual primitives contribute significantly to the learned representation.

---

## Status

Completed
