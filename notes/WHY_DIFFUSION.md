# Why Diffusion?

> This document is **not** a summary of the DDPM paper.
>
> It reconstructs the reasoning that leads to diffusion models.
>
> Instead of asking **"What is the equation?"**, every section asks **"Why does this equation appear?"**

---

# Research Questions

- RQ1 — Why formulate generation as denoising?
- RQ2 — Why Gaussian noise?
- RQ3 — Why gradual corruption?
- RQ4 — Why a Markov process?
- RQ5 — Why can we jump directly to any timestep?
- RQ6 — Why predict noise instead of the image?
- RQ7 — How do we derive the reverse diffusion process?
- RQ8 — Why does noise prediction become score matching?

---

# RQ1 — Why formulate generation as denoising?

Image generation can be viewed as learning a mapping from random noise to realistic images. Unfortunately, this is an extremely difficult learning problem. A random Gaussian vector contains almost no semantic structure, whereas a natural image contains rich spatial, statistical and semantic relationships. Learning this transformation in a single step requires solving a highly nonlinear inverse problem.

Diffusion models approach the problem differently.

Instead of learning one large transformation, they decompose generation into a sequence of much simpler transformations. At every step, the model removes only a small amount of noise from the current image. Each denoising step is therefore much easier than generating an entire image from scratch.

Generation becomes an iterative refinement process.

```text
Pure Noise
     │
     ▼
Slightly Denoised
     │
     ▼
More Structure
     │
     ▼
Almost Clean
     │
     ▼
Final Image
```

Rather than solving one impossible problem, diffusion models solve many simple ones whose composition produces a realistic image.

---

# RQ2 — Why Gaussian noise?

Once we decide to formulate generation as denoising, the next question becomes:

> **What kind of corruption should we add?**

Several possibilities exist.

- Salt-and-pepper noise
- Blur
- Random masking
- Gaussian noise

Not all corruption processes are equally useful.

Salt-and-pepper noise permanently destroys pixel values. Blur removes high-frequency information. Random masking deletes entire regions of the image. These transformations are difficult or even impossible to invert accurately.

Gaussian noise behaves differently.

Instead of replacing information, it perturbs every pixel by a small continuous amount. The original image remains embedded beneath the noise and can, in principle, be recovered.

Gaussian distributions also possess several mathematical properties that make them ideal for probabilistic modelling.

- The sum of independent Gaussian variables is Gaussian.
- Affine transformations of Gaussian variables remain Gaussian.
- A Gaussian distribution is completely determined by its mean and covariance.
- Many probability calculations admit closed-form solutions.

These properties allow the forward diffusion process and its reverse to be derived analytically.

Gaussian noise is therefore chosen not because it is conventional, but because it is simultaneously a realistic corruption process and a mathematically tractable probability distribution.

---

# RQ3 — Why gradual corruption?

Even with Gaussian noise, another question remains.

> **Should we corrupt the image all at once?**

Suppose we immediately transform

```text
Dog Image
```

into

```text
Pure Gaussian Noise
```

Recovering the original image from complete randomness would require solving an extremely difficult inverse problem.

Instead, diffusion models introduce noise gradually.

```text
x₀
 │
 ▼
x₁
 │
 ▼
x₂
 │
 ▼
...
 │
 ▼
xₜ
 │
 ▼
...
 │
 ▼
x_T
```

Each transition introduces only a very small amount of additional corruption.

Consequently,

- consecutive states remain highly similar,
- information disappears gradually,
- and the reverse transformation becomes much easier to learn.

Rather than reconstructing an image from complete randomness in one step, the model learns to reverse many small perturbations.

This transforms a difficult inverse problem into a sequence of simple denoising problems.

---

# RQ4 — Why a Markov process?

A gradual corruption process specifies *how much* noise is added, but not *what information each step should depend upon*.

One possibility is

\[
q(x_t \mid x_{t-1},x_{t-2},...,x_0),
\]

where every previous state influences the next.

This quickly becomes computationally expensive.

Diffusion models instead make the **Markov assumption**.

> The next state depends only on the current state.

Mathematically,

\[
q(x_t \mid x_{t-1},x_{t-2},...,x_0)
=
q(x_t \mid x_{t-1}).
\]

This assumption dramatically simplifies the model.

Instead of learning dependencies across the entire trajectory, each transition only needs to model one local transformation.

The Markov property also allows the forward process to be factorized as

\[
q(x_{1:T}\mid x_0)
=
\prod_{t=1}^{T}
q(x_t\mid x_{t-1}),
\]

which becomes the probabilistic foundation of diffusion models.

---

# RQ5 — Why can we jump directly to any timestep?

The forward process is defined recursively.

Each state depends on the previous one.

\[
x_0
\rightarrow
x_1
\rightarrow
x_2
\rightarrow
\cdots
\rightarrow
x_t.
\]

Naively, generating \(x_t\) requires simulating every intermediate state.

This would make training unnecessarily expensive.

Fortunately, repeated substitution reveals a closed-form solution.

\[
x_t
=
\sqrt{\bar{\alpha}_t}\,x_0
+
\sqrt{1-\bar{\alpha}_t}\,\epsilon,
\]

where

\[
\epsilon\sim\mathcal N(0,I).
\]

This equation allows any timestep to be sampled directly from the original image.

Training no longer needs to simulate the entire trajectory.

Instead,

1. choose a random timestep,
2. sample one Gaussian noise vector,
3. construct \(x_t\) immediately.

The recursive process defines the diffusion dynamics.

The closed-form solution makes training computationally efficient.

---

# RQ6 — Why predict noise instead of the image?

During training, three prediction targets appear possible.

- Predict the clean image \(x_0\).
- Predict the previous image \(x_{t-1}\).
- Predict the injected noise \(\epsilon\).

The third option turns out to be the simplest.

During the forward process, we generate

\[
x_t
=
\sqrt{\bar{\alpha}_t}x_0
+
\sqrt{1-\bar{\alpha}_t}\epsilon.
\]

Since **we sample** the noise ourselves, its exact value is known during training.

This provides perfect supervision.

Predicting \(x_0\) is substantially harder because heavily corrupted images may correspond to many plausible clean images.

Predicting the injected noise avoids this ambiguity.

Once the model predicts

\[
\hat{\epsilon},
\]

the clean image can be recovered algebraically.

\[
\hat{x}_0
=
\frac{
x_t
-
\sqrt{1-\bar{\alpha}_t}\hat{\epsilon}
}
{\sqrt{\bar{\alpha}_t}}.
\]

Thus, predicting noise does not discard information about the clean image.

Instead, it converts image reconstruction into a simpler supervised learning problem while still allowing the clean image to be recovered whenever needed.

---

# Summary

By answering the first six research questions, we have constructed the complete **forward diffusion process**.

We now understand

- why generation is formulated as denoising,
- why Gaussian noise is used,
- why corruption is gradual,
- why the process is Markovian,
- why any timestep can be sampled directly,
- and why predicting injected noise is the preferred learning objective.

The forward process is now complete.

What remains unanswered is the central mathematical question:

> **How do we reverse the diffusion process?**

This leads to the next research question.

---

# Next

**RQ7 — How do we derive the reverse diffusion process?**
