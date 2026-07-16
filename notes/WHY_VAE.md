# WHY VAE?

> Reverse engineering the Variational Autoencoder by understanding the engineering problems it was designed to solve.

---

# RQ1 — Why represent an image as a distribution instead of a single latent point?

## Problem

A traditional autoencoder maps every input image to a **single deterministic latent vector**.

```
Image
   │
Encoder
   │
   ▼
Latent Point (z)
```

This representation is rigid.

Even though similar images may have similar meanings, the latent space is not explicitly structured. As a result:

- Similar images are not guaranteed to occupy nearby regions.
- Sampling arbitrary latent vectors often produces meaningless outputs.
- The model cannot naturally represent uncertainty or multiple plausible latent representations.

---

## The Idea

Instead of predicting one latent point, let the encoder predict the parameters of a Gaussian distribution.

```python
mu = Dense(latent_dim)(x)
logvar = Dense(latent_dim)(x)
```

Each image is now represented by

- **μ** — the center (mean) of the latent distribution.
- **logσ²** — the variance of the latent distribution.

Together they define

\[
q(z|x)=\mathcal N(\mu,\sigma^2)
\]

rather than a single point.

---

## Why this helps

Representing images as distributions makes the latent space smoother and more meaningful.

Instead of encoding

```
Image → Point
```

the encoder learns

```
Image → Region
```

This allows:

- smooth interpolation
- meaningful sampling
- multiple plausible latent representations
- improved generative capability

---

## Code

```python
mu = Dense(latent_dim)(x)
logvar = Dense(latent_dim)(x)
```

---

## One-line Takeaway

A VAE represents every image as a **probability distribution** instead of a **single deterministic point**.

---

# RQ2 — Why can't we directly sample from the latent distribution?

## Problem

After predicting a Gaussian distribution, the most natural implementation seems to be

```python
z = sample(mu, sigma)
```

However, this introduces a training problem.

Although the Gaussian probability distribution is differentiable, the **sampling operation itself behaves like a black box**.

The sampled latent vector is produced, but the computation connecting it to **μ** and **σ** is hidden.

```
μ, σ
   │
   ▼
 sample()
   │
   ▼
   z
```

GradientTape cannot trace how the sampled value depends on the encoder outputs.

Without this computational path, gradients cannot flow back to update the encoder.

---

## The Insight

Separate the randomness from the learnable parameters.

Instead of sampling directly,

sample only from a fixed standard normal distribution.

```python
epsilon = tf.random.normal(tf.shape(mu))

z = mu + sigma * epsilon
```

The randomness now comes entirely from **ε**.

The learnable parameters **μ** and **σ** remain inside an explicit mathematical expression.

---

## Why it Works

During one forward pass,

- μ is fixed.
- σ is fixed.
- ε is sampled once and then remains constant for that forward pass.

GradientTape therefore differentiates

```
z = μ + σ × constant
```

instead of differentiating an opaque sampling operation.

This creates a complete computational graph.

```
μ ───────────────┐
                 │
σ ──► × ε ───────┤
                 ▼
                 +
                 ▼
                 z
```

Gradients now flow naturally back through μ and σ while preserving stochastic sampling.

---

## Code

```python
std = tf.exp(0.5 * logvar)

epsilon = tf.random.normal(tf.shape(mu))

z = mu + std * epsilon
```

---

## One-line Takeaway

The reparameterization trick does **not remove randomness**.

It rewrites sampling into a differentiable computation that backpropagation can optimize.

---

## Relation to Weave AI

Future garment generation should not produce one fixed output for a given design.

A garment can have multiple realistic variations due to

- fabric drape
- body pose
- wrinkles
- lighting
- viewing angle

Representing designs as latent probability distributions enables controlled sampling of these variations while remaining trainable using gradient-based optimization.nto a differentiable computation that automatic differentiation can optimize.


# RQ3 — Why isn't reconstruction loss enough?

## Problem

Suppose the VAE is trained using only reconstruction loss.

```python
total_loss = reconstruction_loss
```

The encoder and decoder now have only one objective:

> Reconstruct the input image as accurately as possible.

Nothing in the objective encourages the latent space to have any particular structure.

---

## What happens?

The encoder is free to place images anywhere in the latent space as long as the decoder can reconstruct them.

For example,

```
Image 1 → z = [1000, -200]

Image 2 → z = [-750, 430]

Image 3 → z = [5200, 80]
```

These latent vectors may appear completely arbitrary.

The optimizer does not care because reconstruction remains accurate.

---

## Why is this a problem?

During inference we generate new samples by drawing

```python
z = tf.random.normal(...)
```

which assumes that latent vectors follow a standard normal distribution.

However, if training never encouraged such a distribution, the sampled latent vectors may lie in regions the decoder has never seen before.

As a result,

- reconstruction during training may be excellent,
- but generation during inference becomes unreliable.

---

## The Insight

Reconstruction loss teaches the decoder **how to reconstruct**.

It does **not** teach the encoder **how to organize the latent space**.

A second objective is therefore required to shape the latent representations into a distribution that can be sampled reliably.

This motivation naturally leads to the KL divergence term.

---

## Code

Without KL

```python
total_loss = reconstruction_loss
```

With KL

```python
total_loss = reconstruction_loss + kl_loss
```

---

## One-line Takeaway

Reconstruction loss learns **how to reconstruct images**.

KL divergence learns **how to organize the latent space for generation**.


# RQ4 — Why is KL Divergence the right objective for the latent space?

## Problem

Reconstruction loss teaches the decoder how to reconstruct images.

However, it does not encourage the encoder's latent distribution to match the desired prior.

We therefore need an objective that compares two probability distributions.

---

## Building the idea

A probability distribution can be viewed in terms of the uncertainty of the events it generates.

### Surprise

For one event,

```
Surprise = -log(P)
```

Rare events are more surprising than common events.

---

### Entropy

Entropy is the expected surprise of the true distribution.

```
H(P)
=
-\sum P(x)\log P(x)
```

---

### Cross Entropy

Suppose Nature generates data according to P, but our model predicts Q.

The model experiences surprise according to its own probabilities.

```
H(P,Q)
=
-\sum P(x)\log Q(x)
```

---

### KL Divergence

Subtracting entropy from cross entropy gives

```
D_KL(P||Q)

=
H(P,Q)-H(P)

=
\sum P(x)\log\frac{P(x)}{Q(x)}
```

KL divergence therefore measures the **extra surprise** introduced by using the model distribution instead of the true distribution.

---

## Applying this to the VAE

Encoder:

```
q(z|x)
```

Desired prior:

```
p(z)=N(0,I)
```

The KL loss minimizes

```
D_KL(q(z|x)||p(z))
```

forcing the encoder's latent distribution to resemble the standard Gaussian.

---

## One-line Takeaway

KL divergence does not simply compare two distributions.

It measures the extra information (or surprise) incurred when the encoder's latent distribution differs from the desired prior.

# RQ5 — Why do we optimize the ELBO instead of directly maximizing log P(x)?

---

## The Goal

A generative model should assign a high probability to the observed data.

Therefore, the ideal objective is

\[
\log p(x)
\]

where \(x\) is an observed image.

---

## The Problem

A latent variable model assumes every image is generated from an unknown latent variable \(z\).

The probability of an image is therefore

\[
p(x)
=
\int p(x|z)p(z)\,dz.
\]

This requires integrating over **every possible latent vector**.

For high-dimensional continuous latent spaces, this integral is computationally intractable.

Therefore, we cannot directly optimize

\[
\log p(x).
\]

---

## Can we infer only the relevant latent vectors?

Instead of considering every latent vector, we would prefer to know

\[
p(z|x),
\]

the posterior distribution over latent variables given the image.

Using Bayes' theorem,

\[
p(z|x)
=
\frac{p(x|z)p(z)}
{p(x)}.
\]

Unfortunately,

\[
p(x)
=
\int p(x|z)p(z)\,dz,
\]

which is exactly the intractable quantity we were trying to avoid.

Therefore the true posterior is also intractable.

---

## The Idea

Instead of computing the true posterior,

approximate it with a neural network

\[
q_\phi(z|x).
\]

The encoder predicts the parameters of a Gaussian distribution

\[
q_\phi(z|x)
=
\mathcal N(\mu,\sigma^2).
\]

Notice that we are **not** assuming the true posterior is Gaussian.

We only assume that our approximation belongs to the Gaussian family.

---

## Measuring the Approximation

To compare

\[
q_\phi(z|x)
\]

with

\[
p(z|x),
\]

we use

\[
D_{KL}(q_\phi(z|x)\;||\;p(z|x)).
\]

Applying Bayes' theorem gives

\[
\log p(x)
=
\mathcal L(x)
+
D_{KL}(q_\phi(z|x)\;||\;p(z|x)).
\]

where

\[
\mathcal L(x)
=
E_{q_\phi}
[\log p(x|z)]
-
D_{KL}(q_\phi(z|x)\;||\;p(z)).
\]

This quantity is called the **Evidence Lower Bound (ELBO).**

---

## Why is it called a Lower Bound?

KL divergence is always non-negative.

Therefore

\[
D_{KL}
\ge
0.
\]

Hence

\[
\boxed{
\mathcal L(x)
\le
\log p(x)
}
\]

The ELBO is therefore a lower bound on the true data likelihood.

---

## Final Training Objective

Machine learning libraries minimize losses.

Therefore we minimize the negative ELBO,

which becomes

```python
total_loss =
reconstruction_loss +
kl_loss
```

where

- Reconstruction loss maximizes the likelihood of reconstructing the image.
- KL loss keeps the encoder's approximate posterior close to the chosen Gaussian prior.

---

## One-line Takeaway

The ELBO was not introduced as an arbitrary objective.

It naturally emerges when approximating an intractable posterior using variational inference. Maximizing the ELBO simultaneously improves reconstruction quality while learning a structured, sampleable latent space.
