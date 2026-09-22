# Local-model feasibility plan

Status: candidate selection and test design, 22 September 2026. No model runtime installed, model downloaded, inference executed or M2 performance measured in this step.

## Candidates

Start with publisher-provided Qwen3-0.6B and Qwen3-1.7B GGUF files, both Q8_0. Their file listings show approximately 639 MB and 1.83 GB. Record exact publisher revisions and published SHA-256 checksums in [the candidate manifest](../../configs/local-model-candidates.json); verify local bytes against those checksums before a run. Download only the named file from the pinned revision, not an entire repository or a moving tag.

Choice rationale: two sizes from one family, one quantisation format and publisher-owned distributions make an initial controlled comparison. The smaller model tests the low-resource hypothesis; the larger tests whether more capacity improves usefulness enough to justify its cost. Q8_0 is the format currently listed in these first-party repositories; no lower-bit conversion is silently substituted. This is not an exhaustive or newest-model recommendation. If memory pressure is unacceptable, assess a separately versioned lower-bit candidate.

The publisher labels both distributions Apache-2.0. llama.cpp carries MIT licensing. Preserve the applicable licence notices with future distribution; software, model and textbook permissions remain separate. No application licence or redistribution clearance is established by this inventory.

Proposed runtime: llama.cpp with Metal. The official build guide documents Metal on macOS. Freeze an exact build only after confirming the user's tools/OS compatibility; runtime revision is deliberately unresolved in the manifest. Do not promise a current binary runs on Sonoma 14.5 without testing.

## First Mac preflight

Jeet can run these read-only commands and paste their output. They inspect availability and the developer-tools path; they install or download nothing. A missing command or developer-tools error is useful information.

```sh
sw_vers -productVersion
uname -m
command -v python3 git cmake brew llama-server
xcode-select -p
```

Do not collect serial numbers, full environment dumps or private directory listings. Confirm Python's usable version later before running Python tools; merely finding a shim does not establish a usable installation.

## Freeze before quality tuning

- Review the 40 development-case drafts, numeric expectations and family groupings.
- Prepare and independently review the 80 held-out cases described in [the evaluation protocol](../../evals/protocol.md). They are not authored or sealed yet. Do not claim that reserving a count reserves an actual dataset.
- Pin runtime build, model bytes, prompt versions, course-pack hash, retrieval configuration and output budget.
- Use the same retrieved evidence IDs and length budgets for ordinary versus structured generation with the same model. If comparing raw passages versus authored cards, report that as a separate preparation ablation; do not attribute both changes to prompting alone.

## Proposed controlled run

Use one model at a time, one sequence and an initial 4096-token context with a 512-token generated-output cap; aim for answers no longer than 250 words. These are starting settings, not measured requirements. Explicitly disable thinking for the first comparison and verify effective template behaviour. The current llama.cpp server documentation exposes `--reasoning off`; the actual pinned build must support the selected control. Do not discard hidden reasoning time from latency accounting.

Compare A: lexical evidence cards, A-structured: current template guide, B: local model with ordinary source context, and C: the same model with structured answer constraints. Keep identical evidence for the B/C prompt-only comparison. Model generation adapter and evidence assembly are not implemented yet.

Three quality repetitions with recorded seeds and fixed sampling settings; independently score correctness, citation support and boundary handling. Proposed settings appear in the manifest. Before generating, count tokens and stop/reduce evidence explicitly if the context would overflow; never silently truncate conditions.

For performance, separate load/startup, first visible answer token and total answer time. At least five cold starts and thirty warm interactions per configuration; report raw samples and p50/p95, peak process memory, system memory pressure/swap, disk footprint and power mode. The small-model file size alone does not establish fit in 8 GB unified memory.

After installation, disable connectivity, restart the runtime and ask new questions using local model paths. Verify sources open locally and no remote inference fallback exists. Bind any test server only to loopback and require a local authentication token; the server adapter has not yet been implemented.

## Sources checked

- [Qwen 0.6B distribution](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF/tree/main) and [file/hash](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF/blob/main/Qwen3-0.6B-Q8_0.gguf).
- [Qwen 1.7B distribution](https://huggingface.co/Qwen/Qwen3-1.7B-GGUF/tree/main) and [file/hash](https://huggingface.co/Qwen/Qwen3-1.7B-GGUF/blob/main/Qwen3-1.7B-Q8_0.gguf).
- [Model licence, 0.6B](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF/blob/main/LICENSE) and [1.7B](https://huggingface.co/Qwen/Qwen3-1.7B-GGUF/blob/main/LICENSE).
- [llama.cpp build guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md), [server reference](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md), and [licence](https://github.com/ggml-org/llama.cpp/blob/master/LICENSE).
