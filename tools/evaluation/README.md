# Development observation runner

Standard-library Python 3.10+. Runs the unchanged lexical baseline and the template guide against the same private development questions. It is not a model benchmark or automatic correctness grader.

```sh
python3 tools/evaluation/run_development.py \
  --pack course-packs/diode-draft/pack.json \
  --cases evals/private/diode-development-v0.1.jsonl \
  --source 'ae-book-11e=/absolute/path/to/local-book.pdf' \
  --output evals/results/development-run-001.json \
  --include-drafts
```

The separate private evaluation bundle supplies the 40-case dataset. Existing 12-case seed input also works. Every case must explicitly be development, have a unique ID and include a family, category, prompt, expected-behaviour draft and review status. Held-out labels are rejected. This is a workflow guard, not access control: someone could relabel a file, so maintain separation of evaluation custody.

Only prompt text is passed to the retrieval/router functions. Expected behaviour is not evidence or a prompt. Recorded outputs can contain private card text and belong under ignored `evals/results/`; overwriting an existing result is rejected. All correctness scores remain null until subject review. Elapsed time is for the local non-generative pair, not model latency or a Mac measurement.

Cases with explicit conversational history are not supported by this runner yet. The expanded set uses standalone questions only; held-out multi-turn cases require a future session runner.
