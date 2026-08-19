# CLO-SKET — Limitations and Reviewer Risks

## 1. Purpose

This document is an internal reviewer-risk register for the CLO-SKET
manuscript.

Its purpose is to identify:

1. claims that a reviewer may challenge;
2. methodological weaknesses;
3. alternative explanations;
4. experiments that already address those concerns;
5. concerns that remain unresolved; and
6. wording that should be used to prevent overclaiming.

This document is intentionally more critical than the manuscript.

The objective is not to defend every result.

The objective is to identify where the evidence is strong, where it is
conditional, and where the manuscript should explicitly acknowledge
uncertainty.

---

# 2. Highest-Risk Reviewer Objections

The most important anticipated objections are:

1. The 135-D representation is hand-designed and therefore not novel.
2. PCA is standard and therefore the contribution may appear trivial.
3. The 28-D radial-angular representation is manually chosen.
4. The downstream improvement may simply result from adding 28 features.
5. The radial-angular representation may contain information already
   encoded in morphology.
6. The downstream task uses category labels, weakening the claim of
   purely unsupervised organization.
7. The study uses only one dataset.
8. The study does not establish semantic meaning.
9. The study does not establish a mathematical manifold.
10. The permutation test uses only 100 permutations.
11. The 28-dimensional representation may have been selected after
    observing the data.
12. The downstream classifier may favor one representation because of
    model choice.
13. The radial-angular descriptors may depend on preprocessing choices.
14. The morphology representation may be sensitive to threshold and
    spatial resolution.
15. The observed organization may reflect dataset composition rather
    than intrinsic properties of garment sketches.
16. The manuscript may overstate novelty relative to existing shape
    analysis literature.

These risks should be addressed explicitly.

---

# 3. Reviewer Risk: "The 135-D Representation Is Not Novel"

## Likely reviewer statement

> The proposed morphology representation consists of standard occupancy
> profiles and global descriptors. What is novel?

## Assessment

This criticism is valid.

The individual mathematical operations are not claimed as novel.

The study does not propose a fundamentally new image descriptor.

## Correct response

The contribution should be framed as an empirical and analytical
contribution rather than an algorithmic descriptor contribution.

The relevant question is:

> What quantitative organization becomes measurable when garment sketches
> are represented explicitly in this way?

The study then evaluates that representation through:

- morphology-space organization;
- independent radial-angular geometry;
- cross-branch correspondence;
- downstream complementarity;
- dimension-matched controls; and
- descriptor ablation.

## Manuscript action

Do NOT write:

> "We introduce a novel 135-D feature descriptor."

Prefer:

> "We construct an explicit quantitative morphology representation
> and investigate the organization it induces in a population of
> garment sketches."

---

# 4. Reviewer Risk: "This Is Just PCA"

## Likely reviewer statement

> The paper appears to reduce handcrafted features with PCA. Why is
> this a research contribution?

## Assessment

The criticism would be valid if PCA were the central result.

It is not.

PCA is used as a coordinate transformation within the broader
morphology analysis.

The cross-branch analysis does not depend on PCA as the scientific
hypothesis.

## Correct response

The evidence chain includes:

    explicit morphology
        ↓
    geometric organization
        ↓
    independent radial-angular representation
        ↓
    cross-branch validation
        ↓
    downstream complementarity
        ↓
    dimension-matched control
        ↓
    ablation

PCA is therefore a methodological component rather than the
contribution itself.

## Manuscript action

Avoid titles or claims such as:

> "PCA-based morphology representation."

Use:

> "quantitative morphology representation."

---

# 5. Reviewer Risk: "The 28 Dimensions Were Arbitrarily Chosen"

## Likely reviewer statement

> Why 28 dimensions? Why these five descriptor blocks?

## Assessment

This is one of the most legitimate unresolved methodological issues.

The 28-D representation is a predefined compact descriptor set.

The experiments establish that this representation is useful.

They do NOT establish that 28 is optimal.

They also do not establish that these are the only meaningful
radial-angular descriptors.

## Current evidence

Cell 11 shows that:

- F₂ radial alone improves performance;
- α₂ improves performance;
- observed circular descriptors improve performance;
- learned circular descriptors improve performance;
- relational descriptors improve performance;
- the complete representation produces the largest observed gain.

This reduces concern that the result is entirely caused by one
arbitrarily selected block.

## Remaining limitation

The study does not perform a formal search over alternative
radial-angular dimensionalities.

## Manuscript wording

Use:

> "the predefined 28-dimensional radial-angular representation used
> in this study."

Do NOT write:

> "the optimal 28-dimensional representation."

---

# 6. Reviewer Risk: "The Improvement Is Just Because You Added 28 Features"

## Likely reviewer statement

> Of course 163 features can outperform 135 features. Did you test
> whether the improvement is caused simply by dimensionality?

## Assessment

This is a major reviewer risk.

## Current evidence

Cell 10 implements a dimension-matched control.

The number of added dimensions is retained while sketch-level
correspondence is destroyed.

The correctly aligned radial-angular representation outperforms the
dimension-matched control.

## Interpretation

This directly weakens the simple dimensional-expansion explanation.

## Claim boundary

The result supports:

> the observed improvement depends on the specific aligned
> radial-angular representation rather than dimensionality alone under
> the tested control.

It does NOT establish:

> information-theoretic independence.

---

# 7. Reviewer Risk: "The Radial-Angular Representation Is Redundant"

## Likely reviewer statement

> If morphology predicts radial-angular quantities, then the second
> representation may simply be a re-expression of the same information.

## Assessment

This is a legitimate possibility.

## Evidence addressing it

Cell 3:

    feature-wise association

Cell 4:

    cross-validated morphology → radial-angular recovery

Cell 6:

    row-permutation correspondence

Cells 8–9:

    downstream complementarity

The key observation is that morphology can recover some radial-angular
quantities while the radial-angular representation nevertheless
improves downstream discrimination.

This indicates partial overlap rather than complete redundancy.

## Claim boundary

Use:

> "partially overlapping but functionally complementary."

Do NOT use:

> "independent information" in an information-theoretic sense.

---

# 8. Reviewer Risk: "The Downstream Result Is Circular"

## Likely reviewer statement

> Was the radial-angular representation designed to improve the same
> downstream task on which it was evaluated?

## Assessment

This is potentially serious.

The paper must make the construction sequence clear.

The radial-angular representation must be described as an independently
derived geometric representation, not as a feature-selection procedure
optimized against the 23-category task.

## Current evidence

The radial-angular branch was constructed independently of the frozen
135-D morphology representation.

The final 28-D representation consists of predefined descriptor
blocks.

The downstream evaluation is then performed on the fixed
representation.

## Remaining risk

If descriptor selection or dimensionality decisions were influenced
by downstream category performance during experimentation, that must
be documented honestly.

The manuscript should not claim strict preregistration unless it
actually occurred.

---

# 9. Reviewer Risk: "The 23 Categories Are Driving the Result"

## Likely reviewer statement

> If categories were not used for morphology construction, how do you
> know the observed structure is meaningful rather than simply
> category-related?

## Assessment

This is an important distinction.

The morphology organization analyses are label-free.

The downstream complementarity analysis is explicitly supervised.

Therefore the manuscript must separate these two claims.

## Supported

The quantitative morphology representation exhibits organization
without using category labels.

## Also supported

The representation improves performance on a specific 23-category
discrimination task.

## Not supported

The claim that the entire morphology organization is independent of
semantic categories.

## Manuscript action

State explicitly:

> "Category labels were excluded from representation construction and
> morphology-space organization analyses, but were used in the
> downstream discrimination experiment."

---

# 10. Reviewer Risk: "Only One Dataset"

## Likely reviewer statement

> How do you know this is a property of garment sketches rather than
> Clo-Sket?

## Assessment

This criticism is valid.

## Current evidence

The study uses:

    2300 Clo-Sket sketches.

## Remaining limitation

No independent external dataset has yet been used for replication.

## Manuscript response

State:

> "The conclusions are currently demonstrated within the Clo-Sket
> population and require external validation."

Do not generalize to all garment sketches.

---

# 11. Reviewer Risk: "Dataset Composition May Create the Geometry"

## Likely reviewer statement

> The discovered structure may simply reflect the sampling structure
> or category composition of Clo-Sket.

## Assessment

This cannot be completely eliminated by the current study.

The label-free morphology analyses reduce direct dependence on category
labels but do not eliminate dataset-specific sampling effects.

## Current controls

- no category labels used for morphology construction;
- no category labels used for morphology organization;
- permutation tests;
- density-region nulls;
- feature-order permutation analyses.

## Remaining limitation

External dataset replication is still required.

---

# 12. Reviewer Risk: "The Representation Is Sensitive to Thresholding"

## Likely reviewer statement

> Why use foreground threshold < 0.8? Would another threshold produce
> the same morphology structure?

## Assessment

This is a legitimate robustness concern.

## Current method

The canonical representation uses:

    grayscale
    intensity normalization by 255
    foreground threshold < 0.8
    64 × 64 spatial resolution.

## Current evidence

The canonical representation is frozen and provenance-controlled.

## Remaining limitation

The present experiment does not establish invariance to alternative
threshold values.

## Manuscript action

Explicitly acknowledge threshold and resolution dependence.

Do not claim preprocessing invariance.

---

# 13. Reviewer Risk: "Why 64 × 64?"

## Likely reviewer statement

> Why was the sketch resized to 64 × 64? Does the morphology structure
> depend on this resolution?

## Assessment

The resolution is part of the canonical preprocessing pipeline.

It is not itself scientifically optimized in the present analysis.

## Remaining limitation

Resolution sensitivity has not been comprehensively evaluated.

## Manuscript action

Describe 64 × 64 as:

> "the frozen canonical spatial representation used in this study."

Do not describe it as an objectively optimal resolution.

---

# 14. Reviewer Risk: "Why 28-D Radial–Angular Geometry?"

## Likely reviewer statement

> Why not 20, 40, or 100 descriptors?

## Assessment

The 28-D representation is a predefined compact representation.

Its utility is demonstrated empirically.

Its optimality is not.

## Current evidence

Descriptor ablation demonstrates that:

    full RA > each individual block

for the tested downstream metrics.

## Remaining limitation

Alternative descriptor sets have not been exhaustively compared.

---

# 15. Reviewer Risk: "The Permutation Test Uses Only 100 Permutations"

## Likely reviewer statement

> Why only 100 permutations?

## Assessment

This is a real limitation.

With 100 permutations and the +1 correction:

    minimum nonzero p = 1 / 101 ≈ 0.0099.

The reported p = 0.0099 should therefore not be presented as a
high-resolution probability estimate.

## Correct interpretation

The observed statistic exceeded all 100 sampled null replicates.

## Recommended wording

> "The observed statistic exceeded all 100 permutation replicates
> (empirical p = 0.0099 under the +1 correction)."

This is more transparent than simply writing:

> p < 0.01.

## Future work

A confirmatory analysis could use:

    1,000
    or
    5,000+

permutations.

---

# 16. Reviewer Risk: "Permutation Null Is Too Weak"

## Likely reviewer statement

> Randomly permuting rows may not preserve all relevant dependence
> structure.

## Assessment

This is theoretically possible.

The current permutation test is a row-level correspondence null.

It asks a specific question:

> Does the observed sketch-to-sketch correspondence matter?

It does not test every conceivable null model.

## Claim boundary

State:

> "The result exceeds the specified row-permutation null."

Do not claim:

> "The result cannot be explained by any alternative null model."

---

# 17. Reviewer Risk: "The Radial-Angular Representation Is Another Handcrafted Descriptor"

## Likely reviewer statement

> Why should this be considered a meaningful scientific contribution
> rather than another engineered feature set?

## Response

The scientific value is not attributed to mathematical novelty of
polar/radial operations.

It is attributed to testing whether a geometrically distinct
representation:

1. corresponds to morphology;
2. captures partially overlapping structure;
3. adds downstream utility; and
4. survives dimensionality controls.

This makes the radial-angular representation a representation-sensitivity
and complementarity experiment rather than a claim of mathematical
novelty.

---

# 18. Reviewer Risk: "The Complementarity Result Is Model-Specific"

## Likely reviewer statement

> Maybe the radial-angular representation only helps this particular
> classifier.

## Assessment

This is a legitimate limitation unless multiple downstream model
families are evaluated.

## Current evidence

The complementarity result is evaluated under the specified
cross-validation and downstream model.

## Remaining limitation

Model-family robustness has not been comprehensively established.

## Manuscript wording

Use:

> "under the tested downstream discrimination task."

Avoid:

> "universally improves classification."

---

# 19. Reviewer Risk: "Cross-Validation May Still Contain Leakage"

## Likely reviewer statement

> Was any preprocessing fitted using the full dataset before
> cross-validation?

## Required response

For analyses in which PCA is used to construct predictive target
coordinates, PCA fitting is performed within the training fold.

Therefore test observations do not contribute to the PCA transformation
used to generate the corresponding training/test target coordinates.

This must remain explicit in the Methods.

## Reviewer-facing principle

All learned preprocessing used for predictive evaluation must be
training-fold specific.

---

# 20. Reviewer Risk: "The Morphology-to-RA Analysis Is Circular"

## Likely reviewer statement

> Are the radial-angular targets themselves derived from morphology?

## Assessment

This is a crucial conceptual question.

The manuscript must clearly distinguish:

    primary morphology representation

from:

    independently derived radial-angular measurements.

The cross-branch experiment is only meaningful if the radial-angular
branch is independently derived rather than simply mathematically
repackaging the same 135 coordinates.

## Manuscript action

Explicitly describe the radial-angular construction and demonstrate
which quantities are independently measured.

Do not use the phrase "independent representation" without explaining
the sense in which independence is meant.

Prefer:

> "independently constructed geometric representation"

rather than:

> "statistically independent representation."

---

# 21. Reviewer Risk: "Independent Representation Does Not Mean Independent Information"

This distinction must be explicit.

The radial-angular representation is independently constructed.

That does NOT mean:

    statistically independent
    information-theoretically independent
    causally independent.

The results actually demonstrate some overlap between the two
representations.

Therefore the manuscript should use:

> independently constructed

rather than:

> independent information.

---

# 22. Reviewer Risk: "The Study Claims a Semantic Language"

## Likely reviewer statement

> Where is the semantic validation?

## Assessment

A semantic-language claim is not supported by the current experiments.

There are no explicit human semantic annotations establishing that
morphology coordinates correspond to semantic concepts.

## Correct manuscript position

The study provides:

> a quantitative morphology representation.

It does not provide:

> a validated semantic language of fashion.

## Important rule

The phrase "semantic language" should not appear in the Results or
Conclusion unless it is explicitly qualified as a future hypothesis.

---

# 23. Reviewer Risk: "You Claim Morphological Primitives"

## Assessment

Not currently supported.

A primitive would imply a reusable elemental unit of morphology with
demonstrated semantic or compositional significance.

The current experiments identify quantitative coordinates and regions,
not primitives.

## Manuscript rule

Do not call morphology coordinates:

- primitives;
- parts;
- atoms;
- tokens;
- semantic units.

---

# 24. Reviewer Risk: "You Claim a Morphology Grammar"

## Assessment

Not supported.

A grammar requires evidence for compositional rules.

The current study demonstrates geometric organization but not
compositional generative rules.

## Manuscript rule

Use:

> morphology organization

not:

> morphology grammar.

---

# 25. Reviewer Risk: "You Claim a Morphology Manifold"

## Assessment

Not formally established.

The graph and PCA analyses show geometric organization but do not
prove that the data form a smooth mathematical manifold.

## Manuscript rule

Use:

> quantitative morphology space

instead of:

> morphology manifold.

---

# 26. Reviewer Risk: "The 73 PCA Dimensions Are the Intrinsic Dimension"

## Assessment

Not supported.

The 73 dimensions arise from the selected variance-retention
criterion.

They are not an estimate of mathematical intrinsic dimension.

## Manuscript rule

Write:

> "73 PCA coordinates retained approximately 95% of standardized
> variance."

Do not write:

> "The morphology space has intrinsic dimension 73."

---

# 27. Reviewer Risk: "Significance Does Not Mean Importance"

The study contains many statistically significant feature-wise
associations.

A reviewer may correctly point out that:

> statistical significance does not imply strong effect size.

This is particularly relevant because some associations have modest
absolute correlation values.

The manuscript should therefore report:

- effect sizes;
- FDR-adjusted significance;
- block-level summaries; and
- predictive performance.

The study should not characterize every significant association as
"strong."

---

# 28. Reviewer Risk: "Large Sample Size Creates Significance"

With:

    n = 2300

small correlations can achieve very small p-values.

Therefore the manuscript should emphasize effect sizes such as:

    Spearman ρ

rather than p-values alone.

For example:

    ρ ≈ 0.20

should be described as a modest association even if its p-value is
extremely small.

This is a critical reviewer-proofing principle.

---

# 29. Reviewer Risk: "The Downstream Improvement May Be Numerically Large
But Practically Narrow"

A Δ Macro-F1 of approximately:

    +0.071

is meaningful within the tested task.

However, it does not establish practical utility in a real-world
fashion-design workflow.

The manuscript should distinguish:

    statistical/task-level improvement

from:

    practical deployment value.

No production or design-system claim should be made.

---

# 30. Reviewer Risk: "The Full 28-D Representation Was Selected After
Seeing Ablation Results"

If the final 28-D representation was fixed before the downstream
evaluation, this should be documented.

If descriptor selection was influenced by downstream results, the
manuscript must not imply that the evaluation was completely
hold-out/preregistered.

## Required principle

The manuscript should accurately describe the chronology of descriptor
selection and evaluation.

Never reconstruct a cleaner experimental history than actually
occurred.

---

# 31. Reviewer Risk: "The Study Is Exploratory"

## Assessment

Parts of the study are exploratory.

This is not inherently a weakness.

The problem occurs only if exploratory observations are presented as
predefined hypotheses.

## Recommended framing

The paper can describe the work as:

> an empirical representation-analysis study with confirmatory
> controls applied to key downstream claims.

This is more credible than pretending every analysis was specified
before seeing the data.

---

# 32. Reviewer Risk: "Multiple Experiments Increase the Chance of
False Positives"

The morphology organization section contains multiple analyses.

Therefore the manuscript should avoid treating every individual
statistical result as an independent discovery.

The strongest argument is based on convergence across analysis types.

The paper should emphasize:

> convergent evidence

rather than:

> a large number of significant tests.

---

# 33. Reviewer Risk: "Why Not Compare Against Deep Embeddings?"

This is a reasonable potential request.

A reviewer may ask whether the explicit morphology representation
provides anything that a modern learned embedding would not.

## Current status

No comprehensive comparison with pretrained deep visual embeddings has
been performed.

## Importance

This is potentially a valuable future experiment.

## However

It is not necessary to claim that the explicit representation
outperforms deep learning.

The study asks a different question:

> Can transparent quantitative morphology provide measurable
> organization and complementary geometric information?

A deep-embedding benchmark would answer a related but distinct
question.

---

# 34. Reviewer Risk: "Why Not Use a Stronger Classifier?"

The complementarity result is task- and model-dependent.

A reviewer may request multiple classifier families.

## Current position

The present result demonstrates complementarity under the tested
downstream model and cross-validation protocol.

## Manuscript action

Do not claim universal classifier improvement.

A stronger-model comparison can be listed as future validation.

---

# 35. Reviewer Risk: "Why Not Test External Generalization?"

This is a valid request.

External validation would strengthen the paper substantially.

## Current status

No independent dataset replication is included.

## Response

Explicitly state this limitation.

The current contribution is demonstrated within Clo-Sket.

---

# 36. Reviewer Risk: "Could the Radial-Angular Representation Be
Mathematically Derived From the Same Image Information?"

Yes.

Both representations ultimately originate from the same sketch image.

This is not a problem.

The relevant distinction is:

> independently constructed coordinate descriptions

rather than independent data sources.

The study should never imply that radial-angular geometry comes from a
different dataset or measurement modality.

---

# 37. Reviewer Risk: "Why Call the Representations Complementary?"

The term "complementary" is justified only at the task level.

Evidence:

    morphology-only
    Macro-F1 = 0.3413

    morphology + RA
    Macro-F1 = 0.4123

with:

    Δ = +0.0710

and the observed improvement exceeding the corresponding
dimension-matched permutation null.

Therefore:

> task-level complementary utility

is supported.

The broader statement:

> the two representations encode fundamentally complementary
> information

is too strong.

---

# 38. Reviewer Risk: "Why Not Call Them Independent?"

Do not.

The association analysis demonstrates substantial overlap.

The downstream result demonstrates additional utility.

Together these indicate:

> overlap + additional task-level utility.

That is not the same as statistical or information-theoretic
independence.

---

# 39. Reviewer Risk: "The Radial–Angular Representation Might Encode
the Same Signal in a More Convenient Coordinate System"

This is a valid interpretation.

The present evidence does not completely distinguish:

    genuinely additional geometric information

from:

    a coordinate transformation that makes some existing information
    easier for the downstream model to use.

The dimension-matched control strengthens the claim that the specific
representation matters.

However, the paper should avoid claiming that the radial-angular
representation discovers fundamentally new information in an
information-theoretic sense.

---

# 40. Reviewer Risk: "The Results Depend on the Specific 23-Class Task"

Yes.

This limitation must be acknowledged.

The strongest defensible claim is:

> radial-angular geometry provides reproducible incremental utility
> under the tested 23-category discrimination task.

Not:

> radial-angular geometry universally improves garment recognition.

---

# 41. Reviewer Risk: "The Dataset Labels Could Be Reflected in Shape"

This is possible.

Garment categories naturally differ in morphology.

Therefore even a label-free morphology representation may exhibit
structures that correlate strongly with category composition.

The present study does not claim otherwise.

Its contribution is to characterize quantitative morphology without
using category labels to construct the representation.

The downstream task then explicitly tests category discrimination.

These are different analytical stages.

---

# 42. Reviewer Risk: "Can the Results Be Replicated?"

The study has several reproducibility safeguards:

- frozen morphology artifact;
- SHA-256 fingerprint;
- explicit feature names;
- explicit metadata;
- image-path provenance;
- fixed random seeds;
- cross-validation specification;
- stored result objects;
- stored permutation results; and
- documented experiment sequence.

These should be made available with the repository where possible.

---

# 43. Reviewer Risk: "Notebook Results Are Not a Reproducible Pipeline"

This is a practical concern.

The computational experiment was developed in notebook form.

The final manuscript should not depend solely on screenshots or
interactive notebook state.

## Repository requirement

The final repository should contain:

    paper/
    notebooks/
    src/
    artifacts/
    results/
    figures/

where possible.

The frozen artifacts should be separated from transient notebook
objects.

The final analysis should be runnable from a clean environment if
practical.

---

# 44. Reviewer Risk: "The Paper Is Too Many Experiments"

This is a possible presentation problem.

The manuscript currently contains a long evidence chain.

A reviewer may perceive this as excessive if the central question is
not clearly stated.

## Solution

Organize the Results around the scientific logic:

    1. morphology organization
    2. independent geometric representation
    3. correspondence
    4. complementarity
    5. controls

Do not present every notebook cell as an independent scientific
discovery.

Cells are implementation units.

They are not manuscript-level contributions.

---

# 45. Reviewer Risk: "The Paper Does Not Have a Single Central Claim"

This is perhaps the most important writing risk.

The manuscript should have one central statement:

> Garment sketches exhibit reproducible quantitative geometric
> organization that can be characterized through explicit morphology
> measurements, while an independently constructed radial–angular
> representation captures additional task-relevant structure.

Everything else supports this statement.

---

# 46. Reviewer Risk Matrix

| Reviewer concern | Current evidence | Status |
|---|---|---|
| Handcrafted 135-D representation | Explicitly acknowledged | Managed |
| PCA is standard | PCA positioned as method | Managed |
| Why 28 dimensions? | Descriptor definition + ablation | Partially resolved |
| Added dimensions explain gain | Dimension-matched control | Strongly addressed |
| RA is redundant | Association + downstream complementarity | Addressed at task level |
| Category leakage | Label-free representation construction | Partially addressed |
| Single dataset | Clo-Sket only | Unresolved limitation |
| Threshold sensitivity | Frozen preprocessing | Unresolved |
| Resolution sensitivity | Fixed 64×64 | Unresolved |
| Permutation count | 100 permutations | Known limitation |
| Weak null model | Row permutation | Scope-limited |
| Model dependence | Single tested downstream setting | Unresolved |
| External validation | None | Unresolved |
| Semantic meaning | No semantic validation | Explicitly not claimed |
| Manifold claim | Not established | Explicitly excluded |
| Grammar claim | Not established | Explicitly excluded |
| Information-theoretic independence | Not tested | Explicitly excluded |
| Deep embedding comparison | Not performed | Future work |
| Reproducibility | Frozen artifacts + provenance | Strongly addressed |

---

# 47. What We Should NOT Add Merely to Satisfy Reviewers

Not every conceivable experiment should be added.

The following should not be added unless a specific reviewer or
scientific question requires them:

- arbitrary additional descriptor families;
- more clustering algorithms without a hypothesis;
- more PCA variants;
- random visualization experiments;
- increasingly complex classifiers;
- semantic labels merely to make the paper appear semantic;
- deep-learning models solely for novelty;
- large numbers of additional permutation tests without a specific
  null hypothesis.

Additional experiments should only be added if they resolve a clearly
identified scientific objection.

---

# 48. What Would Most Strengthen the Paper?

If additional experimental effort becomes necessary, the highest-value
extensions are:

### Priority 1 — External dataset replication

Demonstrates that the morphology organization is not specific to
Clo-Sket.

### Priority 2 — Preprocessing sensitivity

Test alternative threshold and/or resolution settings.

### Priority 3 — Larger permutation count

Increase the number of permutations for confirmatory null
distributions.

### Priority 4 — Model-family robustness

Test whether downstream complementarity persists across more than one
reasonable classifier family.

### Priority 5 — Semantic validation

Use human/expert annotations to determine whether quantitative
morphology aligns with interpretable design concepts.

These experiments answer substantially different reviewer questions and
are therefore more valuable than adding more variants of the current
analysis.

---

# 49. Final Reviewer-Proof Claim Boundary

## Strong claims supported

The study supports:

> quantitative morphology organization of the examined garment-sketch
> population.

It supports:

> reproducible sketch-level correspondence between explicit morphology
> and independently constructed radial-angular geometry.

It supports:

> task-level complementary utility of radial-angular geometry beyond
> morphology under the tested 23-category discrimination task.

It supports:

> evidence that this utility is not adequately explained by dimensional
> expansion alone under the dimension-matched control.

---

## Claims deliberately excluded

The study does not establish:

> semantic novelty.

It does not establish:

> semantic garment-part recognition.

It does not establish:

> a universal morphology vocabulary.

It does not establish:

> a morphology grammar.

It does not establish:

> a mathematical morphology manifold.

It does not establish:

> information-theoretic independence.

It does not establish:

> causal mechanisms.

It does not establish:

> human-like visual understanding.

---

# 50. Internal Decision

The current evidence is sufficient to support the central
representation-analysis story.

The manuscript should therefore NOT expand the experimental scope
unless a specific unresolved reviewer objection requires it.

The primary task now is:

    tighten claims
        ↓
    improve literature positioning
        ↓
    document exact methodology
        ↓
    produce reviewer-readable figures
        ↓
    construct evidence-linked tables
        ↓
    write the final manuscript.

The goal is not to make the paper claim more.

The goal is to make every claim impossible to misunderstand.