Input Image

↓

Encoder

↓

Feature Representation h

↓

μ Head
logσ² Head

↓

Reparameterization

↓

Latent Vector z

↓

Decoder

↓

Reconstructed Image

↓

Loss

↓

Reconstruction Loss


The encoder extracts meaningful visual features.

Instead of predicting one latent vector,
it predicts the parameters of a Gaussian distribution.

This allows uncertainty to be represented.

+

KL(q(z|x)||N(0,I))


Sampling breaks gradient flow.

The reparameterization trick moves randomness outside the computational graph,
making end-to-end optimization possible.



The decoder learns how to reconstruct an image
from a sampled latent representation.



The reconstruction term preserves information.

The KL term organizes the latent space
so that random sampling remains meaningful.
