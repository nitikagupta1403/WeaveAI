# WHY DIFFUSION?

This repository is not a summary of the DDPM paper.

It is a reconstruction of the reasoning that leads to Diffusion Models.

Instead of asking *"What is the forward diffusion equation?"*, every section asks *"Why does this equation have to exist?"*

---

# The Journey

Need to generate realistic images

        │
        ▼

Generation from scratch is extremely difficult

        │
        ▼

Can a difficult generation problem be converted into many easy problems?

        │
        ▼

Need a process that gradually destroys information

        │
        ▼

Need a corruption process that is unbiased and mathematically tractable

        │
        ▼

Gaussian Noise

        │
        ▼

Need to corrupt the image gradually instead of instantly

        │
        ▼

Markov Process

        │
        ▼

Need to describe any noisy image directly

        │
        ▼

Forward Diffusion

        │
        ▼

Need to reverse the corruption

        │
        ▼

Reverse Diffusion

        │
        ▼

Need a neural network to learn the reverse process

        │
        ▼

DDPM

---

## Research Questions

- RQ1 — Why formulate generation as denoising?
- RQ2 — Why Gaussian noise?
- RQ3 — Why gradual corruption?
- RQ4 — Why a Markov process?
- RQ5 — Why can we jump directly to any timestep?
- RQ6 — Why predict noise instead of the image?
- RQ7 — Why does noise prediction become score matching?

> Reverse engineering Diffusion Models by understanding the engineering problems they were designed to solve.
