# Evaluation workspace

Evaluation is planned, not yet implemented. See [Stage 1](../docs/stage-1-feasibility.md) and sections 10–11 of the [bible](../docs/project-bible.md).

Compare retrieval-only, ordinary local retrieval-augmented answers and structured local answers. Use the same model for the latter pair when measuring the effect of structure.

Public datasets must contain only redistributable, reviewed material. Keep private questions and held-out keys under ignored `evals/private/`; raw runs under ignored `evals/results/`. Distributed course packs must never contain held-out keys. Commit sanitised benchmark reports only after reviewing their contents.

No model results or passing scores are claimed at repository initialisation.
