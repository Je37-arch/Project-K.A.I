# Forty-case development observation 001

Recorded 22 September 2026 UTC. Model inference: none. Target Mac: not tested.

## Inputs and procedure

Private diode pack 0.2.0 (11 draft cards) and development set v0.1 (40 original project-authored prompts including the previous 12 seeds). The 28 additions include unfamiliar phrasing, wrong premises, model assumptions, missing data, unsupported scope and three numerical targets. Expected behaviours remain unreviewed subject drafts. No assignment text was copied.

Dataset SHA-256: `cf7adb68bcac25339249eee123523998f4bded47e532523b2d0e319f2682f055`.

Ran `tools/evaluation/run_development.py` with draft preview enabled and the actual uploaded book's hash verified. The runner records both lexical and template outputs; no expected-behaviour text reaches either component. Raw card-containing outputs stay ignored and are not published. Guide rules and card content were not changed to accommodate the new questions.

## Observations

| Subset | Draft explanation preview | Clarification | Abstention |
| --- | ---: | ---: | ---: |
| Original 12 | 6 | 4 | 2 |
| Added 28 | 0 | 26 | 2 |
| All 40 | 6 | 30 | 4 |

These are status counts, not correctness scores. Excessive clarification is a usefulness failure when a question could be answered from the prepared material. The guide cannot handle ordinary paraphrases broadly, and it still has no numerical solver. This result argues against treating the template demonstration as a finished tutor. It creates a concrete comparison target for local generation.

No human correctness labels, evidence-support rate or held-out acceptance score has been collected. The new 28 cases remain development data after this run. A future model must improve helpfulness without trading away grounded correctness.

## Software checks

18 tests passed via `python -m unittest discover -s tests -v`: previous 14 plus four evaluation-runner tests. New checks cover held-out/duplicate/malformed input rejection, dataset checksum sensitivity, null scoring and exclusion of expected-behaviour notes from answering calls.

## Next dependencies

Subject review and an actual sealed 80-case held-out set before quality tuning; model adapter and fair evidence assembly; target-Mac tooling preflight, pinned runtime, local files and measured offline runs. Candidate model selection is documented in [the local-model plan](local-model-plan.md), not a measured deployment decision.
