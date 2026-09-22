# Stage 1 feasibility experiment

## Question

Can a small local model provide useful, source-supported answers for one course unit on the target device?

## Dependencies

Complete [Stage 0](stage-0-inputs.md). Select at least two local configurations after measuring hardware requirements and checking licences. Do not choose a model based only on parameter count.

## Experiment

1. Inspect representative pages containing prose, equations, tables and diagrams. Record failures and manual corrections.
2. Extract a bounded unit with exact resource-version and page references.
3. Build baseline A: retrieval or reviewed cards without generation.
4. Build B: local model with ordinary retrieved passages.
5. Build C: the same model with structured answer assembly and source constraints.
6. Run the same development questions with equivalent length limits and source versions.
7. Disconnect the network, restart the application and ask a new question. Verify answering and source viewing work without external inference calls.
8. Record response quality, cold start, warm p50/p95 timing, memory, disk usage and preparation effort on the target Mac.
9. Document failures and choose a configuration or reduce scope. Do not hide failure with a cloud fallback.

## Evaluation discipline

Follow the bible's proposed 120-case design: 40 development cases and 80 held-out cases. Keep near-duplicate questions in the same split. Held-out keys stay outside course packs and prompts. Reserve them before tuning; use them for Stage 2 acceptance, not repeated Stage 1 optimisation.

Use a subject reviewer for expected facts and citations. Automated checks do not establish semantic correctness. Proposed timing and accuracy thresholds remain provisional until frozen before held-out evaluation.

## Run record

Record code commit, model name and hash, runtime version, quantisation, prompt version, pack hash, retrieval settings, output limit, hardware, power mode, cold/warm status, elapsed time, peak memory, factual score and failure reason. Only sanitised results may be committed.

## Exit

At least two local configurations have been assessed; the offline path works on the named device; extraction limits and measured performance are documented. This is a feasibility gate, not a claim of release-quality accuracy.
