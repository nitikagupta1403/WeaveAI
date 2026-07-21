# RQ9 — Why does DDPM predict Gaussian noise instead of the clean image?

## Motivation

In the previous chapter, we established that a neural network is required because the clean image \(x_0\) is unknown during inference.

A natural question now arises.

If we are already using a neural network, what exactly should it predict?

Several possibilities seem reasonable.

It could predict

- the previous image \(x_{t-1}\),
- the original clean image \(x_0\),
- or the Gaussian noise \(\epsilon\).

Surprisingly, DDPM chooses to predict the added Gaussian noise.

Why?

---

# Candidate 1 — Predict the Previous Image

One possible approach is to learn

\[
f_\theta(x_t,t)=x_{t-1}.
\]

Although intuitive, the target changes at every timestep because the appearance of \(x_{t-1}\) depends on how much noise remains in the image.

The learning problem therefore changes continuously throughout the diffusion process.

---

# Candidate 2 — Predict the Clean Image

Another possibility is to directly predict

\[
f_\theta(x_t,t)=x_0.
\]

This also appears reasonable because the clean image is ultimately what we want to generate.

However, the distribution of clean images is extremely complex.

It contains countless objects, textures, lighting conditions, shapes, and semantic structures.

Learning this distribution directly is a challenging task.

---

# Candidate 3 — Predict the Gaussian Noise

Instead, DDPM predicts

\[
\epsilon_\theta(x_t,t)=\hat{\epsilon}.
\]

The key observation is that the added noise is always sampled from

\[
\epsilon \sim \mathcal N(0,I).
\]

Unlike clean images, the target distribution never changes.

Regardless of whether the original image contains

- a cat,
- a dog,
- a human face,
- a medical scan,
- or a dress,

the added noise is always Gaussian.

The network therefore learns a much simpler and more consistent prediction task.

---

# Why Is This Easier?

The forward diffusion process is

\[
x_t
=
\sqrt{\bar{\alpha}_t}x_0
+
\sqrt{1-\bar{\alpha}_t}\epsilon.
\]

The noisy image is simply a combination of

- the underlying signal,
- and Gaussian noise.

Instead of learning the enormous distribution of natural images, the neural network learns to identify the particular Gaussian noise sample that produced the observed noisy image.

This is a considerably simpler learning problem.

---

# Recovering the Clean Image

Predicting the noise does not mean we lose the clean image.

Once the network predicts

\[
\hat{\epsilon},
\]

the clean image can be recovered directly by rearranging the forward diffusion equation.

\[
\boxed{
\hat{x}_0
=
\frac{
x_t
-
\sqrt{1-\bar{\alpha}_t}\hat{\epsilon}
}
{\sqrt{\bar{\alpha}_t}}
}
\]

Thus, predicting the noise automatically provides an estimate of the clean image.

---

# Key Insight

The choice of predicting Gaussian noise is **not mathematically required**.

It is a design choice.

Among several equivalent parameterizations of the reverse diffusion process, predicting Gaussian noise provides the simplest and most consistent learning target.

---

# Takeaways

- A neural network could predict \(x_{t-1}\), \(x_0\), or the noise.
- DDPM predicts Gaussian noise because it follows a simple, fixed distribution.
- Natural images come from a highly complex data distribution.
- Predicting Gaussian noise simplifies the learning problem.
- Once the noise is predicted, the clean image can be recovered analytically using the forward diffusion equation.

---

# Next Research Question

> **RQ10 — How is the neural network trained to predict the correct Gaussian noise?**
