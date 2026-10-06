# Figure 3 source and claim audit v1.0

Frozen values used:
- band effects: [0.059306, 0.005984, 0.010959, 0.0393]
- bootstrap CIs: [(0.023295, 0.108196), (-0.014164, 0.060361), (-0.003088, 0.07332), (0.01913, 0.091021)]
- FWER p-values: [0.0002, 0.608939, 0.487751, 0.019698]
- retained representations: ['DCT₄', 'RAW₇₂', 'RAW₇₂', 'db4₄']
- hybrid dimension: 1504 complex / 3008 real
- full representation: 2592 complex
- coefficient reduction: 41.98%
- compression ratio: 1.7234×
- whole-representation mean MRR: {'Full RAW72': 0.819373, 'Hybrid': 0.816766, 'Uniform RAW42': 0.815896, 'Uniform db4-42': 0.789378, 'Uniform DCT42': 0.783503}
- whole-representation real dimensions: {'Full RAW72': 5184, 'Hybrid': 3008, 'Uniform RAW42': 3024, 'Uniform db4-42': 3024, 'Uniform DCT42': 3024}

Claim boundaries preserved:
1. support for tested compression differs across harmonic scale under the frozen design;
2. non-supported compression does not imply intrinsic incompressibility;
3. uniform RAW42 remains a close descriptive baseline;
4. hybrid is not framed as a performance breakthrough;
5. whole-representation comparisons remain post-selection descriptive sensitivities.

SVG SHA-256: `3216f41114dea6a336291e0346a1b199bba0c382eee454e6ffe772e78c05e94e`
Caption SHA-256: `ad5929606e3dd8fbf6991cb6fe1a19f7889d589092581d4bcbfa35316f1f3a85`
