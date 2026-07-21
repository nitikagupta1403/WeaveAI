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

---

# Next Research Question

> **RQ8 — If we know the exact reverse diffusion process, why do we still need a neural network?**
