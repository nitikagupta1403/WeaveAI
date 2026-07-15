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

# RQ2 — Why can't we directly sample from the latent distribution?

## The Problem

The encoder predicts a Gaussian distribution using its mean (μ) and variance (σ²).

A natural implementation would be:

```python
z = sample(mu, sigma)
```

However, sampling behaves like a black box. The sampled value is produced, but the computation connecting it to μ and σ is hidden.

As a result, GradientTape cannot determine how changes in μ or σ affect the sampled latent vector.

---

## The Insight

Instead of sampling `z` directly, separate the randomness from the learnable parameters.

```python
epsilon = N(0,1)

z = mu + sigma * epsilon
```

The randomness now comes entirely from ε, while μ and σ remain inside an explicit mathematical expression.

---

## Why it Works

During one forward pass, ε is fixed.

GradientTape therefore differentiates

```
z = μ + σ × constant
```

which allows gradients to flow back through μ and σ.

The model remains stochastic while still being trainable using backpropagation.

---

## Code

```python
std = tf.exp(0.5 * logvar)

epsilon = tf.random.normal(tf.shape(mu))

z = mu + std * epsilon
```

---

## One-line Takeaway

The reparameterization trick does not remove randomness.

It rewrites the sampling process into a differentiable computation that automatic differentiation can optimize.
