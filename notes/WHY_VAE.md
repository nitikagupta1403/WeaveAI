## Why does the encoder predict μ and logσ²?

A deterministic autoencoder maps each image to a single latent point.

A VAE maps each image to a probability distribution.

The mean tells us where the latent representation is centered.

The variance tells us how much uncertainty or spread there is around that center.

Together they define a Gaussian from which we can sample.

# WHY VAE?

---

## RQ1: Why represent an image as a distribution instead of a single latent point?

### Problem

A deterministic autoencoder maps every image to one fixed latent vector.

This makes the latent space rigid. Similar images do not naturally occupy regions of the latent space, making interpolation and generation unreliable.

### Idea

Instead of predicting a single latent point, predict the parameters of a Gaussian distribution.

```python
mu = Dense(latent_dim)(x)
logvar = Dense(latent_dim)(x)

# RQ2: Why can't we directly sample from a Gaussian?

## Problem

After introducing a probabilistic latent space, each input image is no longer represented by a single latent vector. Instead, the encoder predicts the parameters of a Gaussian distribution:

- Mean (μ)
- Variance (σ²)

A natural implementation would be:

```python
z = sample(mu, sigma)
```

However, this creates a problem during training.

---

## Why does direct sampling fail?

The Gaussian probability density function is differentiable with respect to μ and σ.

The **sampling operation is not**.

When we write

```python
z = sample(mu, sigma)
```

the computation of `z` is hidden inside a sampling function.

From the perspective of automatic differentiation, the computation graph becomes

```
μ, σ
  │
  ▼
 sample()
  │
  ▼
  z
```

GradientTape cannot trace how the sampled value `z` depends on `μ` and `σ`.

Without this computational path, gradients cannot flow back to the encoder.

---

## The Reparameterization Trick

Instead of sampling `z` directly, separate the randomness from the learnable parameters.

First sample from a fixed standard normal distribution

```python
epsilon = tf.random.normal(tf.shape(mu))
```

Then construct the latent vector as

```python
z = mu + sigma * epsilon
```

Now the computation graph becomes

```
μ ───────────────┐
                 │
σ ──► × ε ───────┤
                 ▼
                 +
                 ▼
                 z
```

The dependency of `z` on `μ` and `σ` is now explicit.

---

## Why does this work?

During each forward pass:

- `μ` is produced by the encoder.
- `σ` is produced by the encoder.
- `ε` is sampled once and remains fixed for that forward pass.

GradientTape therefore differentiates

```
z = μ + σ × (constant)
```

which gives

```
∂z/∂μ = 1

∂z/∂σ = ε
```

Since `μ` and `σ` are part of the computational graph, gradients can flow normally back through the encoder.

---

## Key Insight

The reparameterization trick does **not** remove randomness.

Instead, it **moves the randomness outside the learnable parameters**, exposing an explicit differentiable computation that automatic differentiation can optimize.

---

## Implementation

```python
std = tf.exp(0.5 * logvar)

epsilon = tf.random.normal(tf.shape(mu))

z = mu + std * epsilon
```

---

## Relation to Weave AI

Future garment generation should not produce identical outputs for the same design.

Different fabric drape, wrinkles, lighting conditions, and body poses should all be plausible variations of the same garment.

Representing each design as a latent probability distribution allows controlled sampling of these variations while still enabling end-to-end training through backpropagation.

---

## Personal Understanding

Initially, I thought the Gaussian itself was the issue.

The actual challenge is that **sampling is a black-box operation**.

By rewriting the sampled latent vector as

```
z = μ + σ ε
```

the dependency of `z` on the encoder outputs becomes explicit, allowing GradientTape to trace gradients back through the network.
