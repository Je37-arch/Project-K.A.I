# K.A.I Study

The first application within **Project K.A.I**: a local, course-grounded Study Guide connected to interactive engineering learning tools.

## Status

Repository foundation only. No application, model runtime, simulations or benchmark results have been implemented yet. We are gathering Stage 0 inputs before Stage 1 feasibility work.

## What we are building

Educators organise selected resources into versioned course packs. Students use a small local model to reconstruct source-supported explanations, switch study modes and explore related simulations. The model explains; tested simulation code computes.

Analog Electronics is the first depth showcase. Smaller Radio Room, Digital Logic and Signal Guide modules follow. The current scope is this study platform; broader Project K.A.I applications remain future work.

Local answering means generating **new answers offline after installation**, without a silent cloud fallback. Initial downloads, class updates and educator queries can require connectivity. Quality, cost and hardware accessibility are hypotheses to measure.

## Start here

- [Project bible](docs/project-bible.md)
- [Development roadmap](docs/roadmap.md)
- [Stage 0 input checklist](docs/stage-0-inputs.md)
- [Stage 1 feasibility plan](docs/stage-1-feasibility.md)
- [Architecture and repository layout](docs/architecture.md)
- [Decision register](docs/decisions/README.md)
- [Contributing](CONTRIBUTING.md)

## Next inputs

1. Analog Electronics textbook and syllabus, supplied privately.
2. Target Mac chip/processor, RAM, macOS version and approximate free storage; no serial number.
3. Optional real assignment or viva questions.

Model, runtime, framework, minimum hardware and hosting are not selected. There is no install or run command yet.

## Public repository boundaries

Keep textbooks, private course packs, student chats, credentials and model binaries outside Git. Use the ignored `private/`, `data/`, `models/` and `artifacts/` directories locally. Only publish fixtures whose redistribution is permitted. `.gitignore` is a convenience, not a security boundary; inspect every staged diff.

## Development workflow

Use focused branches and pull requests after this initial bootstrap. Keep `main` usable, document relevant decisions and attach test evidence. See [CONTRIBUTING.md](CONTRIBUTING.md). This is a documented workflow; branch protection has not been configured.

## Licence

No software licence has been selected. Public visibility does not grant an open-source licence. Model and content licences will be recorded independently before distribution.
