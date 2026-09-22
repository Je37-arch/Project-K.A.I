# Diode extraction trial 001

Stage 1 evidence, 22 September 2026 UTC. Development environment only; no Mac performance or model quality measurement.

## Reproduction

See [the extraction utility](../../tools/ingestion/README.md). Run PDF pages 28–51 inclusive against `ae-book-11e` with the hash in [the register](register.json). PyMuPDF 1.26.6 was available in the development environment; no production dependency decision is implied.

## Recorded results

- Four PDFs opened and were not encrypted: book 927 pages, guide 16, assignments 2 each.
- The bounded book run generated 24 text files, 24 rendered pages and one manifest in ignored artifacts.
- Total extracted characters in that run: 101957. This is a volume measurement, not a correctness score.
- Pages with suspicious control characters: 0 / 24. Absence of these characters does not mean a page is clean.
- Every generated page remains `unreviewed`; printed-page labels require explicit mapping.
- One synthetic integration test passed, covering page-2 selection, text identity, render creation, unreviewed status, overwrite rejection, invalid ranges and output-boundary rejection. No inference tests have run.

## Manual observations

| Evidence | Finding | Required handling |
| --- | --- | --- |
| PDF p.34 / printed p.13 | Equation 1.2 and thermal-voltage equation are readable visually; extracted superscripts and symbols lose structure. The text declares an ideality-factor convention. | Represent the equations separately after review; preserve ideality factor, kelvin temperature and current units. |
| PDF p.39 / printed p.18 | Fig.1.19 uses different forward/reverse current scales and temperature-labelled curves. | Preserve axes and fixed-current interpretation; do not reduce the graph to unordered extracted labels. |
| PDF p.40 / printed p.19 | Raw extraction gives a milliamp unit where the rendered temperature example shows microamps. The same page contains Table 1.5 and prose outside the table. | Never auto-correct globally; flag the affected span and record a reviewed correction. Keep table rows associated with their material labels. |
| PDF p.49 / printed p.28 | Piecewise model diagram includes polarity, threshold and resistance. Prose explains that its voltage-source symbol is not a separate physical power supply. | Carry model semantics and conditions into any explanation; text alone does not encode wiring. |
| Assignment PDFs, all four pages | Some question text and circuit values are embedded images; text extraction omits parts. | Visually transcribe only selected items; do not claim complete assignment ingestion. |

These are agent visual spot checks, not educator content approval. No complete equation transcription or corrected answer pack has been produced. Temperature coefficients in the book must be labelled as the source's approximations and not universal device laws. Printed/PDF page mapping is limited to the sampled section.

## Outcome

Proceed with bounded, visually reviewed preparation. Reject raw PDF text as a ready-to-use knowledge base. Stage 1 remains open: retrieval, model comparisons, offline restart testing, memory and latency measurements are still outstanding.
