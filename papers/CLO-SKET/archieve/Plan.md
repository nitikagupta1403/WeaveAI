REVIEWER-2 AUDIT
       ↓
1. Same-region retention null
       ↓
2. Cross-scale profile-correlation null
       ↓
3. Check KDE / density methodology
       ↓
4. Audit “continuous” wording
       ↓
5. Replace “generalization” → “cross-scale reproducibility”
       ↓
6. Demote feature-order shuffling
       ↓
7. Lock claim hierarchy
       ↓
8. THEN rewrite Abstract / Introduction / Discussion
       ↓
9. Figures + tables
       ↓
10. Final Reviewer-2 simulation

             PAPER I
                │
       ┌────────┴────────┐
       ↓                 ↓
 Existing literature   Our evidence
       │                 │
       └────────┬────────┘
                ↓
       REPRESENTATION TEST
                ↓
     morphology vs baselines
                ↓
       NULL GEOMETRY TEST
                ↓
       category comparison
                ↓
        reviewer attack
                ↓
          final paper

| Priority | Paper                                                  | Role                                          |
| -------- | ------------------------------------------------------ | --------------------------------------------- |
| ⭐⭐⭐⭐⭐    | **P03 Sketch-a-Net**                                   | Sketch-specific representation foundation     |
| ⭐⭐⭐⭐⭐    | **P10 Clothing Sketch Component Segmentation**         | Closest geometric clothing-sketch precedent   |
| ⭐⭐⭐⭐⭐    | **P05 SketchGNN**                                      | Structured point/stroke/graph representation  |
| ⭐⭐⭐⭐     | **P04 Abstracting Sketches through Simple Primitives** | Geometric abstraction / primitive precedent   |
| ⭐⭐⭐⭐     | **P12 Fashion Transfer**                               | Fashion-sketch morphology / shape / folds     |
| ⭐⭐⭐⭐     | **P06/P09 Context-Aware Garment Modeling**             | Geometric interpretation/context              |
| ⭐⭐⭐      | **P02 Fashionpedia**                                   | Predefined semantic ontology contrast         |
| ⭐⭐⭐      | **P13 GarmentSketch**                                  | Recent fashion-sketch computational landscape |

Then:

P01, P08, P14, P15, P16 → bibliography/supporting citations.

P07 → mainly Weave downstream context.

Deep Self-Supervised Representation Learning for Free-Hand Sketch — Xu et al., 2020
DCR: Disentangled Component Representation for Sketch Generation — Cao et al., 2021
SSR-GNNs: Stroke-Based Sketch Representation With Graph Neural Networks — 2022 workshop paper

And I would keep:

Sketch-RNN / A Neural Representation of Sketch Drawings — foundational background, but not a core novelty paper.


automatic extraction of flat-sketch design elements from clothing images.

GarmentSketch is a genuinely recent large-scale resource: 26,249 fashion sketches across 21 garment categories, paired with detailed text descriptions.


                         SKETCH UNDERSTANDING
                                  │
          ┌───────────────────────┼────────────────────────┐
          ↓                       ↓                        ↓
   REPRESENTATION            STRUCTURAL                 SEMANTIC
          │                   ORGANIZATION             INTERPRETATION
          │                       │                        │
   Sketch-a-Net                  │                 SketchGNN
   Sketch-RNN                    │                 Clothing CRF
   Self-supervised              │                 DCR
   SSR-GNN                       │                 Fashionpedia
          │                       │                        │
          └───────────────────────┼────────────────────────┘
                                  ↓
                         OUR SCIENTIFIC GAP
                                  │
                                  ↓
                    quantitative morphology
                                  ↓
                    population-level organization
                                  ↓
                    local / connected geometry
                                  ↓
                    recurring density structure
                                  ↓
                    regional morphology profiles
                                  ↓
                    null + cross-scale validation
                                  ↓
                         SEMANTIC MEANING?
                                  │
                                  ↓
                         WE DO NOT KNOW YET

DCR — Disentangled Component Representation for Sketch Generation

P17 — Deep Self-Supervised Representation Learning for Free-Hand Sketch

P18 — DCR: Disentangled Component Representation for Sketch Generation

P19 — SSR-GNNs: Stroke-Based Sketch Representation With Graph Neural Networks

📚 Add as foundational/background

P20 — A Neural Representation of Sketch Drawings (Sketch-RNN)

Supporting only

Automatic extraction of flat sketch design elements from clothing images

Recent landscape, not core

GarmentSketch

SKTNet


                 CLO-SKET
                    │
          ┌─────────┴─────────┐
          │                   │
   135-D MORPHOLOGY      RADIAL–ANGULAR
      REPRESENTATION       GEOMETRY
          │                   │
      PCA / M1-M2        F₂ + α₂ + circular
          │                   │
   unsupervised structure  interpretable geometry
          │                   │
          └─────────┬─────────┘
                    │
              CROSS-VALIDATION
                    │
             CATEGORY TESTING


| Relationship                                                             | Current evidence     | Status |
| ------------------------------------------------------------------------ | -------------------- | ------ |
| Both detect non-semantic quantitative structure                          | Yes                  | 🟢     |
| Both contain category-discriminative information                         | Yes                  | 🟢     |
| Radial-angular representation is a component of the 135-D representation | Not established      | 🔴     |
| Morphology-space distances agree with radial-angular distances           | Not tested           | 🟡     |
| Morphology regions differ in radial-angular geometry                     | Not tested           | 🟡     |
| Morphology position predicts radial-angular recovery                     | Not tested           | 🟡     |
| Radial-angular branch explains morphology regions                        | Not demonstrated     | 🔴     |
| Radial-angular branch validates morphology-space organization            | Not demonstrated yet | 🔴     |
| Radial-angular branch extends morphology analysis                        | **Yes**              | 🟢     |


The next thing I'd do before writing a single sentence of the paper is a brutal reviewer audit: What exactly is novel here compared with prior computational fashion-sketch representation papers? That is the question that determines whether this is merely publishable or genuinely strong.

CURRENT FASHION-AI LANDSCAPE

        SEMANTIC / GENERATIVE SIDE
                    │
     ┌──────────────┼────────────────┐
     │              │                │
   sketch →      sketch →          sketch →
   text          image            pattern/3D
     │              │                │
   MLLM          diffusion        geometry
     │              │                │
     └──────────────┼────────────────┘
                    │
                    │
              CLO-SKET
                    │
                    ▼
        ┌───────────────────────┐
        │ quantitative morphology│
        │       BEFORE semantics │
        └───────────────────────┘
                    │
            135-D morphology
                    │
                   PCA
                    │
          structured morphology
                    │
                    ▼
          independent radial-
             angular geometry
                    │
                    ▼
             complementary
               information
CLO-SKET/
│
├── README.md
│
├── paper/
│   ├── 00_RESEARCH_QUESTION.md
│   ├── 01_CONTRIBUTION.md
│   ├── 02_LITERATURE_POSITIONING.md
│   ├── 03_METHODS.md
│   ├── 04_RESULTS.md
│   ├── 05_DISCUSSION.md
│   ├── 06_LIMITATIONS.md
│   └── 07_REVIEWER_ATTACK.md
│
├── evidence/
│   ├── evidence_ledger.csv
│   ├── claim_evidence_matrix.md
│   └── cell_results/
│
├── experiments/
│   ├── morphology_135D/
│   └── radial_angular/
│
├── reviewer/
│   ├── novelty_matrix.md
│   └── reviewer_questions.md
│
└── frozen/
    └── checkpoints/