# Retrieval baseline 001

Stage 1 / CORE 03. Recorded 22 September 2026 UTC. Developer environment only; no target-Mac measurement or educator approval.

## Delivered

A Python standard-library CLI with explicit draft preview, source-file identity checks, pack validation and deterministic card retrieval. Seven privately stored diode draft cards were authored from visually inspected PDF pages 34, 39, 40, 41, 49 and 50 (printed pages 13, 18, 19, 20, 28 and 29). They cover the exponential equation, thermal voltage, forward/reverse temperature approximations, ideal behaviour, piecewise-linear and simplified models. Text is paraphrased; numerical conventions and conditions remain tied to the cited edition. No full textbook pages or assignment answers are included in the review pack.

Visual checking is agent preparation work, not independent subject review. Junction formation, depletion behaviour, material comparisons and resistance derivations still need cards. The unit source map is larger than this initial card collection.

## Validation run

`python -m unittest discover -s tests -v`: seven tests passed (six retrieval tests plus the existing extraction test). Retrieval checks cover draft exclusion/opt-in, exact card text and citations, empty/unrelated queries, malformed pack rejection, source identity and missing sources, a socket-blocked non-generative path, and a real CLI subprocess round trip. Synthetic fixture content is original and fictional. This does not establish future LLM instruction resistance or the full offline source-viewing contract.

The actual uploaded textbook hash matched the private pack register. The twelve existing development prompts were run once with drafts enabled and the default three-result cap. Raw output remains ignored. This was a retrieval smoke run, not a scored or reviewed quality benchmark; no acceptance percentage is claimed.

| Development case | Observed candidate IDs, in rank order | Interpretation |
| --- | --- | --- |
| 001 | None | Missing depletion/bias card; coverage gap |
| 002 | constant-drop, ideal, piecewise | Relevant model-comparison evidence retrieved |
| 003 | constant-drop, thermal, exponential | Relevant first result; extra candidates not necessarily useful |
| 004 | forward-temperature, reverse-temperature, ideal | Relevant first result; overbroad secondary evidence |
| 005 | None | Missing resistance card; coverage gap |
| 006 | piecewise, constant-drop, ideal | Relevant first result about the equivalent circuit |
| 007 | ideal, exponential, forward-temperature | Incomplete numerical request; clarification not implemented |
| 008 | exponential, forward-temperature | Missing fixed-variable/device context not detected |
| 009 | reverse-temperature, exponential | Out-of-scope amplifier request still retrieves shared words |
| 010 | exponential | Missing graph request yields unrelated evidence |
| 011 | reverse-temperature | No fabricated citation generated, but irrelevant match returned |
| 012 | constant-drop | Related card found; source-conflict handling not implemented |

These observations illustrate why returning candidates must stay separate from judging answer support. In particular, cases 007–012 do not pass their intended behavioural goals. Do not label this tool a functioning study assistant.

## Next gate

Complete draft coverage, obtain subject review, implement explicit question/answer-support checks and prepare the full development/held-out split before model tuning. Then compare this baseline with ordinary and structured local-model answering. The current threshold remains provisional and must be frozen after development, before held-out evaluation. No cloud fallback was added.
