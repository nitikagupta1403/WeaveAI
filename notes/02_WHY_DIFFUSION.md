# RQ9 — Why Does DDPM Predict Gaussian Noise Instead of the Clean Image?

## Motivation

In the previous chapter, we discovered why a neural network is necessary.

Although the reverse diffusion posterior

\[
q(x_{t-1}\mid x_t,x_0)
\]

is mathematically known, it cannot be evaluated during inference because the clean image \(x_0\) is unknown.

This naturally leads to the next question.

> **If we already need a neural network, what should it learn?**

At first glance, several choices seem reasonable.

The network could predict

- the previous noisy image \(x_{t-1}\),
- the original clean image \(x_0\),
- or the Gaussian noise \(\epsilon\).

Surprisingly, DDPM chooses the third option.

Why?

---

# Candidate 1 — Predict the Previous Image

One possibility is to train the network to predict

\[
f_\theta(x_t,t)=x_{t-1}.
\]

This seems intuitive because reverse diffusion removes noise one step at a time.

However, the target changes at every timestep.

At early timesteps, \(x_{t-1}\) is almost identical to the clean image.

At later timesteps, it is almost pure noise.

The network therefore has to solve a different prediction problem at every timestep.

---

# Candidate 2 — Predict the Clean Image

Another possibility is to predict

\[
f_\theta(x_t,t)=x_0.
\]

This is attractive because the final goal of diffusion is to recover the clean image.

However, the distribution of clean images is extremely complex.

Natural images contain

- people,
- animals,
- buildings,
- landscapes,
- medical images,
- textures,
- fabrics,

and infinitely many other visual patterns.

Learning this entire distribution directly is a difficult task.

---

# Candidate 3 — Predict the Gaussian Noise

Instead, DDPM predicts the noise

\[
\epsilon_\theta(x_t,t)=\hat{\epsilon}.
\]

At first, this choice seems strange.

After all, we ultimately care about generating images—not noise.

The key insight is that the added noise is always sampled from

\[
\epsilon \sim \mathcal N(0,I).
\]

Unlike images, this distribution never changes.

Whether the original image is

- a cat,
- a dog,
- a flower,
- an MRI scan,
- or a dress,

the added noise is always Gaussian.

The learning target therefore remains simple and consistent throughout training.

---

# Comparing the Three Choices

| Prediction Target | Target Distribution | Learning Difficulty |
|-------------------|---------------------|---------------------|
| \(x_{t-1}\) | Changes at every timestep | High |
| \(x_0\) | Complex natural image distribution | High |
| \(\epsilon\) | Standard Gaussian \(\mathcal N(0,I)\) | Lower |

From a learning perspective, Gaussian noise is the simplest target.

---

# Why This Works

Recall the forward diffusion process

\[
x_t
=
\sqrt{\bar{\alpha}_t}x_0
+
\sqrt{1-\bar{\alpha}_t}\epsilon.
\]

The noisy image is simply a mixture of

- the clean image,
- and Gaussian noise.

If the network can estimate the noise,

\[
\hat{\epsilon},
\]

then the clean image can be recovered using algebra alone.

Rearranging the forward diffusion equation gives

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

Thus, predicting the noise is enough to recover an estimate of the original image.

The neural network never needs to learn this equation—it follows directly from the mathematics of the forward diffusion process.

---

# The Bigger Picture

An important lesson from DDPM is that machine learning is not only about designing powerful neural networks.

It is also about choosing the right learning target.

Although predicting

- \(x_{t-1}\),
- \(x_0\),
- and \(\epsilon\)

are mathematically related, they are not equally easy to learn.

DDPM chooses the target that is simplest and most consistent across all timesteps.

This design decision significantly simplifies optimization while preserving the ability to reconstruct the clean image.

---

# Key Insight

The neural network is **not** trained to generate images directly.

Instead, it learns to identify the Gaussian noise hidden inside a noisy image.

Once that noise is known, the clean image follows directly from the diffusion equations.

In other words,

> **The neural network learns the unknown; mathematics computes everything else.**

---

# Takeaways

- A neural network could predict \(x_{t-1}\), \(x_0\), or the added noise.
- Predicting \(x_{t-1}\) leads to a target that changes throughout the diffusion process.
- Predicting \(x_0\) requires learning the highly complex distribution of natural images.
- Predicting Gaussian noise provides a simple and consistent learning target.
- Once the noise is predicted, the clean image can be recovered analytically.
- DDPM's success comes not only from its neural network, but also from choosing the right prediction target.

---

# Next Research Question

> **RQ10 — How is the neural network trained to predict the correct Gaussian noise?**
