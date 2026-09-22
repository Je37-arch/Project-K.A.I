# Architecture and proposed code boundaries

No implementation stack is selected. These are module responsibilities, not empty application packages or working services.

| Future path | Responsibility |
| --- | --- |
| apps/student | Local chat, sources, study modes and tools |
| apps/educator | Course preparation, publication and submitted questions |
| services/classroom | Membership, distribution and query delivery |
| packages/course-schema | Versioned course-pack contracts |
| packages/ingestion | Source extraction and preparation |
| packages/retrieval | Local evidence retrieval |
| packages/answer-engine | Routing, evidence assembly and output checks |
| packages/model-adapters | Replaceable local runtime integrations |
| packages/simulations | Deterministic subject models and serialisable states |
| packages/ui | Shared accessible interface components |
| evals | Evaluation specifications and permitted fixtures |

Create implementation directories when they acquire real code. Keep equations and numerical computation separate from explanatory generation.

## Boundaries

Course preparation and distribution can require connectivity. Installed core study sessions must answer locally. The preparation location remains undecided. Network transmission of uploaded material requires an explicit product choice.

Student chats remain local by default; educator queries include only selected context. A course pack is immutable and records source versions. Simulation state carries model version, parameters, units, outputs and validity warnings.

## Interfaces to define in Stage 1

- Pack validation and source lookup.
- Retrieval request and evidence result.
- Answer request with course, mode, conversation and optional simulation state.
- Answer result with evidence anchors, answer path and warnings.
- Model adapter for bounded generation.

Shared classroom authentication and synchronisation arrive in Stage 3. Do not implement speculative infrastructure before the answering experiment.
