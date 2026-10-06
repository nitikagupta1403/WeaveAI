# Figure 2 source and claim audit v1.0

Source basis: frozen P2_13 / 05K primary evidence.

Values used:
- support levels: [1.0, 1.1, 1.25, 1.5, 2.0, 2.5, 3.0]
- low medians: [0, 0.014163, 0.024044, 0.031578, 0.041836, 0.051059, 0.060047]
- mid medians: [0, 0.004217, 0.004795, 0.006666, 0.011776, 0.014783, 0.01653]
- high-mid medians: [0, -0.008783, -0.013892, -0.017996, -0.023574, -0.029119, -0.034858]
- high medians: [0, -0.011837, -0.020213, -0.027958, -0.038519, -0.046172, -0.052944]
- endpoint concordance: {'Low': 91.5, 'High-mid': 89.5, 'High': 87.3}
- full monotonicity: {'Low': 50.9, 'High-mid': 44.1, 'High': 37.8, 'L1': 56.3}
- endpoint category means: {'Low': 0.070816, 'High-mid': -0.037901, 'High': -0.053174}
- endpoint category medians: {'Low': 0.052497, 'High-mid': -0.035074, 'High': -0.046223}
- endpoint T statistics: {'Low': 8.876063, 'High-mid': 11.942573, 'High': 15.210773}
- endpoint max-T FWER p-values: {'Low': '1.43×10⁻⁶', 'High-mid': '1.19×10⁻⁷', 'High': '1.19×10⁻⁷'}
- object-relative invariance: 16,100 / 16,100
- s=1 replay: 2,300 / 2,300; maximum discrepancy ≈ 2.22×10^-16

Claim boundaries preserved:
1. same-pixel support intervention, not generic zero-padding;
2. object-relative result is a matched control, not a new normalization claim;
3. broad endpoint response, not universal per-image monotonicity;
4. support is a demonstrated dependency of the tested raster-relative representation, not a complete explanation of all preprocessing effects.

SVG SHA-256: `7aed6a34ebec72feba501a4be4e097427844697100d675c1ef8b7e7c874ae0a8`
Caption SHA-256: `94139a8b7dfe323cf57d5b41fec495097859898f1cbe903e91cfb1465ee66307`
