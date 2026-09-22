# Bounded PDF extraction trial

Developer utility for Stage 1, not a student application or a selected production ingestion stack. Uses the locally exercised PyMuPDF version. Review dependency licensing before distributing a preparation application.

From the repository root, with Python 3.10 or newer:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r tools/ingestion/requirements.txt
python tools/ingestion/extract_trial.py '/absolute/path/to/local-book.pdf' --first 28 --last 51 --output artifacts/diode-trial-001
python -m unittest discover -s tests -v
```

Installation needs connectivity; extraction itself makes no network calls. No model is installed. Commands have been exercised with the existing development environment, not on the target Mac. Jeet does not need to run these yet.

The output is raw page text, rendered pages and a manifest containing the original file hash and 1-based PDF anchors. Every page remains unreviewed. No automatic OCR or symbol replacement is performed. A large text count is not evidence of correct equations; embedded-image counts also miss vector diagrams. Review page images alongside text before making answer cards.

Outputs must be in a new subdirectory of ignored `artifacts/`. Existing output directories are rejected to preserve previous trial evidence. Failed runs can leave a partial directory without a completed manifest; use a fresh directory for retry. Do not commit extracted text or rendered textbook pages. The approved public deliverables are metadata and the sanitised trial report.
