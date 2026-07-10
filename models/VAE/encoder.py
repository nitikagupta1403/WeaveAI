"""
Encoder

Why does this file exist?

The encoder transforms an input image into a compact feature representation
and predicts the parameters (μ and logσ²) of a latent Gaussian distribution.

It does not predict the latent vector directly.

Instead, it predicts a probability distribution from which the latent vector
will later be sampled using the reparameterization trick.
"""
