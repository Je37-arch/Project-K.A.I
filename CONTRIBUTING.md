# Contributing

## Workflow

1. Read the project bible and relevant stage plan.
2. Create a focused branch such as `feat/local-retrieval`, `docs/course-pack` or `fix/source-anchors`.
3. Implement one bounded task; include its requirement ID and acceptance evidence.
4. Inspect `git status` and `git diff --cached` before committing. Never force-add private material.
5. Open a pull request describing the purpose, behaviour, tests and limitations.
6. Merge after review and relevant checks; preserve a usable main branch.

The empty-repository foundation is bootstrapped directly on main. Subsequent development uses branches and pull requests. Branch protection is not currently enforced by repository settings.

## Validation

There is no application test suite or CI pipeline yet. For documentation, verify relative links, requirements and formatting. For future code, run focused unit and integration tests for changed behaviour. Add reproducible reference tests for numerical models and human-reviewed evaluation for generated answers.

Report the exact commands and results. Never say tests passed when they were not run. Do not present performance measurements from a development server as MacBook measurements.

## Data and dependencies

Keep textbooks, private course packs, model weights, student chats, credentials and raw evaluation outputs untracked. Sanitise error reports. Only add redistributable fixtures with source and licence notes. Pin chosen dependencies and document setup when the stack is selected.

## Scope

Prove the local Study Guide before expanding simulations. No unrelated Project K.A.I applications, silent cloud fallback or automatically assigned reviewed labels. Update decisions and the bible when scope changes.
