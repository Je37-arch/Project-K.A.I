# Diode evaluation protocol, preparation draft

## State

40 development cases exist privately: 12 previous seeds plus 28 new original questions. All expected-behaviour notes remain subject-review drafts. No held-out questions or sealed answer keys exist yet. The 120-case plan is not complete, and no model-quality tuning has begun.

The first 12 questions informed the existing templates. The added 28 were run without changing those templates and remain development data, not a retrospectively declared held-out set. Keep original questions and raw outputs private until content review and publication decisions are complete.

## Planned held-out set

| Primary category | Planned cases |
| --- | ---: |
| Definitions/explanations | 20 |
| Comparisons/derivations | 12 |
| Numerical/circuit-state | 12 |
| Multi-turn | 12 |
| Ambiguous requests | 8 |
| Unsupported requests | 8 |
| Conflicting-source/injection | 8 |
| Total | 80 |

A subject reviewer must author or review the expected claims, disallowed claims, references, accepted alternatives and clarification criteria. The current development family tags are coarse topic/task groupings. Before sealing, refine them into semantic duplicate groups (same task, derivation or worked-example variant). Assign each such group wholly to one split. Sharing a broad concept is necessary in a bounded unit; rewording an existing development question does not make an independent acceptance case.

Store held-out prompts and keys separately under ignored evals/private/, outside course packs, prompt builders and development outputs. Use reviewer custody; write a manifest of file hashes, counts, family assignments and review version. Freeze the actual files and thresholds before model-quality tuning. Merely listing category counts is not a sealed benchmark. If acceptance cases leak into tuning, retire and replace them, reporting the exposure.

## Scoring

Human-review correctness 0–3, teaching usefulness 1–5, substantive claim support and citation accuracy separately, and expected clarify/abstain behaviour. Report failures and counts, not just percentages. Numerical targets in the development set are future capabilities: a lack of calculator support must not be scored as a correct numerical answer merely because the current router abstains.

The observation runner intentionally leaves correctness scores null. It records lexical candidates and guide decisions for inspection, not model performance. It rejects held-out-labelled inputs and never passes expected-behaviour notes to answering components. This validation is a workflow guard, not permission enforcement against deliberate relabelling.

## Comparison integrity

Keep original lexical baseline, template guide and future model conditions distinct. Ordinary versus structured generation must use identical model bytes, evidence, context limits, output limits and sampling settings when testing the value of structure. Compare changes in source preparation separately. Repeat generative runs three times with recorded seeds. Never include development or held-out expected answers in model prompts or course cards.
