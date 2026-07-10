# Variational Autoencoder (VAE)

## Why does this exist?

A standard autoencoder learns a deterministic latent representation.

However, a deterministic latent space cannot be reliably sampled to generate new images.

A Variational Autoencoder (VAE) learns a probability distribution over the latent space instead of a single point.

This enables both:

- Reconstruction of existing images.
- Generation of new images by sampling from the latent space.

---

## What problem does it solve?

A VAE bridges representation learning and probabilistic generation.

Instead of asking:

"What is the latent representation?"

it asks

"What latent representations are plausible for this image?"

---

## Core Ideas

- Encoder predicts μ and logσ².
- Latent space is probabilistic.
- Reparameterization enables backpropagation.
- Decoder reconstructs images.
- ELBO balances reconstruction and latent organization.

---

This implementation is written from first principles for the Weave AI research journey.
