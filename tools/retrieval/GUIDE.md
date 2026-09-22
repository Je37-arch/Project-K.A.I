# Template-routed diode guide, prototype 1

This adds a conservative decision layer alongside the unchanged lexical baseline. It is standard-library Python 3.10+ code with no model or network dependency. It does not prove that the small-model hypothesis works.

## Run against the private pack

Use the separately supplied review pack 0.2.0 (11 draft cards) under ignored `course-packs/diode-draft/`. From the repository root:

```sh
python3 tools/retrieval/guide.py \
  --pack course-packs/diode-draft/pack.json \
  --source 'ae-book-11e=/absolute/path/to/local-book.pdf' \
  --query 'Compare static and dynamic diode resistance' \
  --include-drafts
python3 -m unittest discover -s tests -p 'test_guide.py' -v
```

The tests run without a textbook and use fictional card bodies. The private pack is not in GitHub. No terminal action is required from Jeet yet; the commands document reproducibility, not a request to install a model.

## Decision contract

- Validate the pack and, in the CLI, every source file hash before returning evidence.
- Enforce ECC-211 / diode-foundations scope. No automatic course switching.
- Catch a small list of unsupported evidence, outside-unit, source-conflict, visual and numerical requests.
- Match the **whole normalised query** to an explicit template. Unrecognised text asks for clarification; there is no lexical-search fallback.
- Resolve required card IDs. Missing cards cause abstention. All selected cards must be reviewed unless draft preview is explicitly enabled.
- Return unchanged card text, conditions, review provenance and citations. No generated result or calculation.

Outcomes are `clarify`, `abstain`, `draft_preview`, or `reviewed_cards`, with a machine-readable reason. The last state requires recorded review metadata on every selected card; it does not authenticate that metadata. Test fixtures exercise it with clearly fictional reviewer metadata. All actual diode cards remain drafts.

## Supported example questions

- What is a PN junction?
- Explain forward and reverse bias.
- Compare ideal and constant-drop diode models.
- Compare silicon and germanium diodes.
- What happens to forward voltage when a silicon diode warms at fixed current?
- Explain the reverse current temperature approximation.
- Compare static and dynamic diode resistance.
- Explain the piecewise-linear diode model.
- Explain thermal voltage.
- Explain the Shockley equation.

The rule table lives in `guide.py`. Stable card IDs bind each template to prepared content; these IDs must not be reassigned to different concepts. Pack validation checks structure, not whether prose actually teaches that concept. Subject review remains essential.

## Known limitations

This is a manually authored template router informed by the 12 development questions, not semantic reasoning. Familiar paraphrases can be missed. Broad keyword exclusions may reject a valid conceptual question that merely mentions an excluded topic. Negations, Unicode notation, mixed-language questions and complex false premises are not reliably understood. Multi-part requests only work when the entire form is explicitly supported. Output cards may contain more context than the exact question needs.

The template router is deliberately separate from baseline A: compare it as an additional structured, non-generative condition rather than silently changing the lexical experiment. No broad accuracy, adversarial robustness or held-out performance is claimed. There is still no conversation state, attachment understanding, source viewer, deterministic solver, model runtime or Mac benchmark. Full offline operation remains untested on the target device.

See the [routing experiment report](../../docs/experiments/guide-routing-001.md). Reverting `guide.py`, its tests and this documentation leaves the lexical baseline unchanged.
