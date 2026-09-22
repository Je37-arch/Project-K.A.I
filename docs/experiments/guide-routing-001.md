# Diode guide routing experiment 001

Stage 1, CORE 02 / CORE 03. 22 September 2026 UTC. No model inference or target-Mac measurements.

## Preparation

Expanded the private review pack from seven to eleven cards, version 0.2.0. Added junction formation, forward/reverse bias, material-dependent knee voltages, and static/dynamic resistance. Visually inspected PDF pages 31–33, 38, 42, 44 and 46 in this step; earlier checked pages supply overlapping context. Citations use exact resource hashes and explicit printed/PDF page anchors. All eleven cards remain drafts, including the seven prior cards.

This closes the four main card gaps identified in the previous smoke run, not every possible question in the source map. Detailed doping theory, resistance worked examples and broad diagram interpretation still need preparation. No educator review or full-unit coverage is claimed.

## Decision-layer design

Introduced an explicit template router that returns cards only for recognised complete query forms. It does not use lexical scores as answer confidence. It requests clarification for missing information and abstains for known unsupported tasks. Missing evidence and unreviewed content also block a normal response. Draft previews require opt-in. Every clarify/abstain response has an empty card list.

The router is a separate experimental condition; the prior lexical baseline remains unchanged. It preserves authored text, assumptions and citations rather than composing answers. Structured card lookup is not evidence that a local model is viable.

## Validation evidence

`python -m unittest discover -s tests -v`: 14 tests passed: seven earlier tests and seven new routing tests. New checks cover draft/reviewed branching, complete-template selection, missing evidence, wrong unit, numerical and visual requests, source conflict, unsupported citations, additional unmatched request text, query bounds, citation tampering and CLI source-file mismatch. The reviewed branch is tested using fictional metadata only.

The actual textbook hash verified against private pack 0.2.0. Re-ran the original twelve development prompts with draft preview enabled:

| Case | Routing outcome | Evidence IDs / reason |
| --- | --- | --- |
| 001 | draft_preview | bias |
| 002 | draft_preview | ideal, constant-drop |
| 003 | draft_preview | materials |
| 004 | draft_preview | forward-temperature |
| 005 | draft_preview | resistance |
| 006 | draft_preview | piecewise |
| 007 | clarify | numerical_context_missing |
| 008 | clarify | numerical_context_missing |
| 009 | abstain | outside_unit |
| 010 | clarify | visual_input_unsupported |
| 011 | abstain | unsupported_evidence_request |
| 012 | clarify | source_conflict |

These are development regression observations. The templates were authored with these questions visible; this is **not an independent evaluation**, and no generalisation or answer-correctness score is claimed. Case 008 receives a broad numerical-context prompt rather than a tailored fixed-variable question. Case 010 cannot consume an image even if later supplied. Questions outside the recognised templates often receive generic clarification.

## Remaining work

Independent review of card claims and scope; a full development set with grouped paraphrases and a sealed held-out set before model tuning; model/runtime feasibility and licensing review; actual offline/Mac memory/latency trials. The next model comparison should keep source versions, question sets and output budgets fixed. Do not interpret these software tests as subject validation.
