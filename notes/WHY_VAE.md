## Why does the encoder predict μ and logσ²?

A deterministic autoencoder maps each image to a single latent point.

A VAE maps each image to a probability distribution.

The mean tells us where the latent representation is centered.

The variance tells us how much uncertainty or spread there is around that center.

Together they define a Gaussian from which we can sample.
