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

# RQ8 — If we know the exact reverse diffusion process, why do we still need a neural network?

## Motivation

In the previous chapter, we derived the exact reverse diffusion posterior

\[
q(x_{t-1}\mid x_t,x_0).
\]

This result is mathematically exact and follows directly from Bayes' theorem and the forward diffusion process.

At first glance, it appears that the reverse diffusion problem has been solved.

So why does DDPM introduce a neural network?

---

# The Catch

The reverse posterior is

\[
q(x_{t-1}\mid x_t,x_0).
\]

Notice that it depends on **two** quantities:

- the noisy image \(x_t\),
- the clean image \(x_0\).

During **training**, this is not a problem because the clean image is available.

```text
Training

Known:
✓ x₀
✓ xₜ
```

Therefore, the exact reverse posterior can be computed.

---

# What Happens During Generation?

Image generation starts from pure Gaussian noise.

At timestep \(t\), we only observe

\[
x_t.
\]

The original clean image does not exist yet because it is exactly what we are trying to generate.

```text
Inference

Known:
✗ x₀
✓ xₜ
```

Without the clean image, we cannot evaluate

\[
q(x_{t-1}\mid x_t,x_0).
\]

Therefore, although the reverse posterior is known mathematically, it cannot be used directly during inference.

---

# The Solution

Instead of requiring the unknown clean image \(x_0\), DDPM learns to estimate the missing information from the noisy image.

A neural network is introduced that receives

\[
(x_t,t)
\]

as input and produces an estimate that allows us to approximate the reverse diffusion process.

The exact choice of **what** the neural network predicts is a design decision that we will examine in the next chapter.

---

# Key Insight

The neural network is **not** introduced because the reverse diffusion equations are unknown.

They are already known.

The neural network exists because those equations require the unknown clean image \(x_0\), which is unavailable during image generation.

The role of learning is therefore to estimate the missing information that mathematics alone cannot provide during inference.

---

# Takeaways

- The reverse posterior has an exact closed-form solution.
- It depends on both \(x_t\) and the unknown clean image \(x_0\).
- During training, \(x_0\) is available.
- During inference, only \(x_t\) is available.
- Therefore, the exact reverse posterior cannot be evaluated directly.
- A neural network is introduced to estimate the missing information required for reverse diffusion.

---

# Next Research Question

> **RQ9 — What should the neural network predict, and why is predicting Gaussian noise the preferred choice?** than predicting the clean image directly?**
