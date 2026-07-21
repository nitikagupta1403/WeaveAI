# RQ7 — How do we derive the reverse diffusion process?

## Motivation

The forward diffusion process is known because we define it ourselves by gradually adding Gaussian noise to a clean image.

However, during image generation, we must reverse this process:

\[
x_T \rightarrow x_{T-1} \rightarrow \cdots \rightarrow x_0
\]

Ideally, we would like to sample from the reverse transition probability

\[
q(x_{t-1}\mid x_t).
\]

Unfortunately, this distribution is **intractable** because it depends on the unknown data distribution.

Since the clean image \(x_0\) is available during training, we instead derive

\[
q(x_{t-1}\mid x_t,x_0),
\]

which turns out to have an exact closed-form solution.

---

# Step 1 — Apply Bayes' Theorem

Using Bayes' theorem,

\[
q(x_{t-1}\mid x_t,x_0)
=
\frac{
q(x_t\mid x_{t-1})
q(x_{t-1}\mid x_0)
}
{
q(x_t\mid x_0)
}.
\]

This converts an intractable conditional probability into a product of distributions that are already known from the forward diffusion process.

---

# Step 2 — Substitute the Known Gaussian Distributions

From the forward diffusion process,

### Forward transition

\[
q(x_t\mid x_{t-1})
=
\mathcal N
\left(
\sqrt{\alpha_t}x_{t-1},
\beta_tI
\right).
\]

### Closed-form forward process

\[
q(x_{t-1}\mid x_0)
=
\mathcal N
\left(
\sqrt{\bar\alpha_{t-1}}x_0,
(1-\bar\alpha_{t-1})I
\right).
\]

\[
q(x_t\mid x_0)
=
\mathcal N
\left(
\sqrt{\bar\alpha_t}x_0,
(1-\bar\alpha_t)I
\right).
\]

Substituting these into Bayes' theorem gives a product of Gaussian distributions.

---

# Step 3 — Ignore Terms Independent of \(x_{t-1}\)

The denominator

\[
q(x_t\mid x_0)
\]

does not depend on the variable we are solving for, namely \(x_{t-1}\).

Therefore,

\[
q(x_{t-1}\mid x_t,x_0)
\propto
\exp(-A)\exp(-B),
\]

where only the exponent terms involving \(x_{t-1}\) need to be considered.

---

# Step 4 — Expand the Quadratic Terms

Expanding the Gaussian exponents and collecting terms involving \(x_{t-1}\) gives

\[
-Ax_{t-1}^2
+
Bx_{t-1}.
\]

At first glance this expression appears complicated.

However, it is simply a quadratic polynomial.

---

# Step 5 — Complete the Square

Using the familiar algebraic identity

\[
-Ax^2+Bx
=
-A
\left(
x-\frac{B}{2A}
\right)^2
+\text{constant},
\]

the quadratic can be rewritten into the standard Gaussian form.

Completing the square allows us to immediately identify

- the **posterior mean** (the center of the Gaussian),
- the **posterior variance** (the spread of the Gaussian).

---

# Final Result

The reverse posterior is itself Gaussian:

\[
\boxed{
q(x_{t-1}\mid x_t,x_0)
=
\mathcal N
\left(
\tilde{\mu}_t(x_t,x_0),
\tilde{\beta}_tI
\right)
}
\]

where

\[
\boxed{
\tilde{\mu}_t(x_t,x_0)
=
\frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}
{1-\bar{\alpha}_t}
x_0
+
\frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}
{1-\bar{\alpha}_t}
x_t
}
\]

and

\[
\boxed{
\tilde{\beta}_t
=
\frac{1-\bar{\alpha}_{t-1}}
{1-\bar{\alpha}_t}
\beta_t.
}
\]

---

# Key Insight

The reverse diffusion posterior is **not learned**.

It is derived entirely from

- the forward Gaussian process,
- Bayes' theorem,
- Gaussian algebra,
- and completing the square.

The only remaining challenge is that this posterior depends on the unknown clean image \(x_0\).

During image generation, we only observe the noisy image \(x_t\).

This naturally motivates the next research question.

## Takeaways

- The reverse distribution q(x_{t-1}|x_t) is intractable.
- Conditioning on x₀ makes the posterior analytically solvable.
- Bayes' theorem converts the problem into known Gaussian distributions.
- Completing the square reveals that the posterior is Gaussian.
- The posterior mean and variance have closed-form expressions.
- The posterior depends on x₀, which is unavailable during inference.
- This limitation motivates learning an approximate reverse process using a neural network.

---

# Next Research Question

# RQ8 — If we know the exact reverse diffusion process, why do we still need a neural network?

## Motivation

In the previous chapter, we derived the exact reverse diffusion posterior

\[
q(x_{t-1}\mid x_t,x_0).
\]

This result is mathematically exact and follows directly from Bayes' theorem and the forward diffusion process.

At first glance, it appears that the problem is solved.

So why does DDPM introduce a neural network?

---

# The Hidden Problem

Although the reverse posterior is known, it depends on the clean image \(x_0\):

\[
q(x_{t-1}\mid x_t,x_0).
\]

During **training**, this is not an issue because the original clean image is available.

```text
Training

Known:
✓ x₀
✓ xₜ

Can compute:
✓ q(xₜ₋₁ | xₜ, x₀)
```

However, image generation begins from pure Gaussian noise.

At inference time, we only observe

\[
x_t.
\]

The clean image is unknown.

```text
Inference

Known:
✗ x₀
✓ xₜ
```

As a result, we cannot evaluate the exact posterior.

---

# The Role of the Neural Network

The neural network is introduced to estimate the missing information.

Instead of requiring the true clean image \(x_0\), we learn an approximation from the noisy image.

The network receives

\[
(x_t,t)
\]

as input and predicts the Gaussian noise

\[
\hat{\epsilon}
=
\epsilon_\theta(x_t,t).
\]

Using this predicted noise, we reconstruct an estimate of the clean image

\[
\hat{x}_0
=
\frac{
x_t
-
\sqrt{1-\bar{\alpha}_t}\,
\hat{\epsilon}
}
{\sqrt{\bar{\alpha}_t}}.
\]

This estimated clean image is then used to approximate the reverse diffusion process.

---

# Why Predict Noise?

The neural network could have been trained to predict

- the previous image \(x_{t-1}\),
- the clean image \(x_0\),
- or the added noise \(\epsilon\).

DDPM chooses to predict the noise because the noise always follows the same simple Gaussian distribution

\[
\epsilon \sim \mathcal N(0,I),
\]

regardless of the image content.

In contrast, clean images come from a highly complex data distribution containing countless objects, textures, and structures.

Learning to predict a simple, consistent Gaussian target is generally easier than directly modeling the entire image distribution.

---

# Key Insight

The neural network does **not** replace the mathematics behind diffusion.

Probability theory still provides

- the forward diffusion process,
- Bayes' theorem,
- the reverse posterior,
- and the equation relating \(x_t\), \(x_0\), and the noise.

The neural network learns only the one quantity that mathematics cannot provide during inference—the unknown noise (or equivalently, the unknown clean image).

---

# Takeaways

- The exact reverse posterior depends on the unknown clean image \(x_0\).
- During inference, only the noisy image \(x_t\) is available.
- Therefore, the exact reverse posterior cannot be evaluated directly.
- A neural network is trained to estimate the missing information.
- DDPM predicts Gaussian noise rather than the clean image because it is a simpler and more consistent learning target.
- Once the noise is predicted, the clean image and the reverse diffusion step follow directly from the diffusion equations.

---

# Next Research Question

> **RQ9 — Why is predicting Gaussian noise easier than predicting the clean image directly?**
