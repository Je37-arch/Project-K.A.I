# Retrieval-only baseline A: experimental card search

This is a standard-library Python 3.10+ command-line experiment, not a chatbot or student release. No model, embedding service, backend or additional package is required. It returns existing card text unchanged with conditions and citation metadata; it never generates a numerical result or assembles a new answer.

## Run the public fictional demonstration

From the repository root:

```sh
python3 tools/retrieval/baseline.py \
  --pack tests/fixtures/retrieval/pack.json \
  --source fixture=tests/fixtures/retrieval/source.txt \
  --query 'What does the amber switch do?' \
  --include-drafts
python3 -m unittest discover -s tests -p 'test_retrieval_baseline.py' -v
```

The fixture is original, fictional test data, not an electronics lesson. Draft preview is explicit; without `--include-drafts`, this fixture produces `no_eligible_cards`. Full test discovery also includes the earlier ingestion test and requires its separately pinned PyMuPDF dependency.

## Run private diode development cards

Place the separately supplied private pack at `course-packs/diode-draft/pack.json`, keeping it ignored. Supply the original local textbook path:

```sh
python3 tools/retrieval/baseline.py \
  --pack course-packs/diode-draft/pack.json \
  --source 'ae-book-11e=/absolute/path/to/local-book.pdf' \
  --query 'How does forward current vary with temperature?' \
  --include-drafts
```

No need for Jeet to run this yet; no Mac timings have been measured. This command verifies each supplied source file's SHA-256 against the pack before retrieving. An unavailable or altered source is an error, not a citation to a guessed version. All source IDs must be supplied exactly once. Output includes the pack checksum and exact source references. The CLI checks byte identity; it does not parse the PDF or open a source viewer. Page bounds use the declared source page count, not an independent runtime PDF count.

## Contract and review states

A version-1 pack includes `pack_id`, `version`, `course_id`, `unit_id`, a source map and cards. See the fictional JSON fixture for the exact shape. Each source has credit, SHA-256 and page count. Each card has a unique ID, title, body, tags, conditions, review provenance and at least one reference. References identify the source version, 1-based PDF page, printed page and section.

`draft` cards are excluded by default. `educator_reviewed` requires reviewer and date fields. These fields preserve recorded provenance; they are not authenticated educator approval or access control. The future classroom service must establish that authority. No included card has educator approval.

Validation rejects missing metadata, duplicate IDs, invalid page ranges, unknown source IDs and mismatched citation versions. Query input is limited to 4,000 characters; at most five cards may be requested through the Python API. The CLI returns three at most. Source paths are supplied by the operator, never executed from pack text. Pack strings are data.

## Retrieval rule and limitations

Lowercase alphanumeric tokens, remove a small fixed stop-word set, and require at least two distinct overlapping terms. Rank by corpus rarity, normalised by card token count; break ties by card ID. This provisional rule was fixed before the 12-question development smoke run. It is not tuned, calibrated or suitable as a semantic confidence score.

Statuses: `clarification_needed` for an empty/non-informative token set; `no_eligible_cards` if review filtering removes every card; `no_supported_match` if no card clears the overlap rule; `evidence_candidates` otherwise. The last status only means related text. One-word queries can be missed. Shared terms can retrieve irrelevant cards. Missing circuit values, unsupported topics, false premises and source conflicts are not reliably recognised. Do not treat candidate retrieval as a final answer or a passed boundary test.

No course switching, follow-up state, modes, OCR, semantic retrieval, numerical tools or generated responses yet. See the [recorded experiment](../../docs/experiments/retrieval-baseline-001.md) for observed gaps. Removing this standalone tool and its fixture rolls back the experiment without affecting ingestion.

## Separate structured condition

The [template-routed guide](GUIDE.md) adds explicit decision rules and card selection alongside this unchanged lexical baseline. It does not establish general language understanding.
