# K.A.I Study Project Bible

Local Study Guide and Engineering Learning Platform

Planning revision 0.2 • 22 September 2026 • Product owner: Jeet

This bible defines what we intend to build, how the parts connect, the order of development, and the evidence required before release. The central deliverable is a useful local Study Guide grounded in educator-selected material. Simulations and visualisations extend its teaching capabilities; they do not replace the need to prove the answering system.

### Product definition

A course-specific study assistant that reconstructs answers from educator-selected resources, adapts explanations to the student’s chosen mode, and connects those explanations to controlled engineering experiments. Educators organise and maintain the course; students study from a versioned course pack.

### The hypothesis to test

A small existing model, supported by retrieval, reviewed answer structures and deterministic tools, can provide dependable help for a bounded course on accessible hardware. Lower recurring cloud inference cost is an intended benefit, not a demonstrated result. Quality, hardware needs and educator preparation effort must be measured together.

### What is fixed and what remains proposed

Confirmed direction: local answering; educator and student roles; educator uploads and updates; student queries; Analog Electronics as the deepest initial subject; smaller Analog Communication, DLCD and Signals and Systems demonstrations. Computational Methods is optional. The model is the main deliverable, and the product remains focused on this learning platform.

Proposed in this revision: a downloadable course pack, a local runtime, bounded initial simulations, the release sequence and numeric acceptance targets. Model, runtime, installation method, hosting, budgets and minimum hardware remain decisions to be settled with evidence. Implementation begins after the initial source and hardware decisions are settled.

### Reading map

2 Scope and requirements · 3 User journeys · 4 Architecture · 5 Course preparation · 6 Answering contract · 7 Learning modules · 8 Data and code structure · 9 Development stages · 10 Evaluation design · 11 Acceptance tests · 12 Pilot and release · 13 Risks and decisions

## 2 Scope and requirements

Release 1.0 is a professor-onboarding pilot with a working local Study Guide and a small classroom workflow. Earlier milestones are internal demonstrations, not substitutes for the agreed release scope.

| ID | Requirement | Evidence of completion |
| --- | --- | --- |
| CORE 01 | Local source-grounded chat | New questions answered with network disconnected after installation. |
| CORE 02 | Course and mode context | Course scope, notation, depth and selected mode preserved across follow-ups. |
| CORE 03 | Traceable answers | Source references resolve to the exact resource version and page or section. |
| EDU 01 | Educator workspace | Upload, organise, replace, review and publish material for an assigned class. |
| EDU 02 | Student query inbox | Receive submitted questions, answer them and optionally approve reusable explanations. |
| STU 01 | Student workspace | Join a class, download a pack, study units, use tools and submit a question. |
| SIM 01 | Analog Electronics depth | Reviewed source-backed units and validated diode, clipper, clamper and transistor demonstrations. |
| SIM 02 | Subject breadth | Radio Room, DLCD and Signal Guide each provide a bounded working demonstration. |

### Scope boundaries

- Use an existing small model first. Training a foundation model and general-purpose AI applications are outside this project.

- Generated text is labelled as generated. Educator-reviewed content is labelled only after explicit review of the applicable version.

- Initial circuit building supports declared components and arrangements. Arbitrary mixed-signal circuit simulation is a separate scope decision.

- No automatic grading, exam proctoring, institution-wide LMS replacement or automatic student profiling in 1.0.

- Computational Methods, voice interaction, multilingual coverage and phone-local inference are deferred unless the core gates are met and scope is deliberately revised.

### Existing prototype

The PhyExperts prototype is a user-experience reference: https://phyexperts-prototype.vercel.app/. It demonstrates navigation, study modes and graph tools. Its production readiness, code reuse and accessibility must be assessed from source before adoption. A hosted interface demonstration does not establish local model execution.

## 3 Users and complete journeys

### Educator prepares a course

Create a course and class; add the syllabus and permitted resources; inspect extraction quality; map resources to units; review answer cards and simulation assumptions; publish a versioned course pack. The interface must show what is usable, what needs review and what failed extraction. A PDF upload never silently becomes a verified tutor.

### Student studies a unit

Join the correct class, install the local runtime and download its course pack. Select a unit and a study mode. Ask a question, inspect its source references and follow up. If a tool helps, open it with visible parameters. Student notes, bookmarks and session history remain local by default.

### Student asks about an experiment

The student changes a diode orientation and asks why the waveform changed. The guide receives the current supported circuit, values, units, device model and computed result. It explains the relevant conduction conditions using the course material. If the circuit is unsupported or the calculation fails, it states that limitation rather than inventing a waveform.

### Student requests educator help

The student chooses to submit a question and previews the attached context. The submission includes selected messages, source references and optional simulation state. The whole private chat is not automatically exposed. Offline submissions remain queued until connectivity and authentication are available.

### Educator corrects and republishes

The educator replies to a submitted question. A separate review action can turn that reply into reusable course content. A new pack version records the correction and affected units. Students see an update notice; past responses retain their original source versions and can be marked outdated.

| Capability | Educator | Student |
| --- | --- | --- |
| Read published pack | Assigned courses | Enrolled courses |
| Edit and publish resources | Assigned course only | No |
| Read private local chats | No default access | Own local chats |
| View submitted queries | Assigned class inbox | Own submissions and replies |
| Review reusable explanations | Explicit approval action | Suggest a correction |

An account can hold different roles in different courses. A role selector alone is not authorisation: the service checks course membership for every protected operation.

## 4 Architecture and local execution

Separate course preparation and distribution from student answering. This allows shared educator updates while keeping the core study session independent of cloud inference.

| Component | Runs where | Responsibility |
| --- | --- | --- |
| Educator workspace | Connected application | Manage courses, resources, review and submitted questions. |
| Preparation pipeline | Educator workstation or managed service | Extract and organise content; build and validate packs. Location remains open. |
| Class service | Shared service | Authentication, membership, version metadata, pack distribution and question delivery. |
| Study client | Student device | Chat, local history, citations, tools and offline status. |
| Retrieval and model runtime | Student device | Local query processing, retrieval, assembly and generation. |
| Simulation engine | Student device | Compute approved models and return typed results. |

### Offline contract

After model, application and course pack installation, a student must be able to launch the guide, ask a new question, open cited downloaded material and operate installed simulations with network access disabled. Sign-in token expiry must not unexpectedly invalidate permitted offline study; the access policy must be documented before the pilot.

Network access is needed for initial downloads, new versions, membership changes and educator questions. These operations must show pending, failed and completed states. There is no silent cloud answering fallback. Offline access cannot guarantee remote revocation of already downloaded material; educators need that limitation explained.

### Deployment decision

Evaluate a desktop application or a web interface connected to a loopback-only local runtime. Browser-only inference is a candidate only if the target hardware supports it reliably. A runtime endpoint must authenticate client requests, restrict allowed origins and avoid listening on public interfaces by default.

### Locality and privacy boundaries

Preparation can use a different execution environment without changing the local answering contract, but any remote processing of educator resources must be explicit. Keep local chats off the shared service unless the student submits selected context. Diagnostics should default to timings and error codes, not raw questions or source excerpts.

## 5 Turning resources into course packs

### Preparation workflow

- Register the source: title, author or provider, edition, upload owner, allowed use, file hash and stable resource identifier.

- Extract page text and layout. Retain the original page numbering and page images needed for diagrams. Flag scanned pages, damaged equations, ambiguous symbols and unreadable tables.

- Map content to the actual syllabus. The course book supplies depth but does not define every assessed topic automatically.

- Create topic chunks with page anchors and neighbouring context. Preserve conditions, units and equation definitions rather than splitting solely by text length.

- Prepare concept cards, misconceptions, worked examples and answer structures. Generated drafts require review before acquiring reviewed status.

- Validate references and tool links; build the retrieval index; publish an immutable pack version with a change log.

### Minimum pack contents

| Record | Required information |
| --- | --- |
| Manifest | Pack ID, course ID, version, schema version, supported runtime, checksum and release notes. |
| Source register | Resource version, page mapping, permitted distribution and extraction status. |
| Topic map | Unit, learning goals, prerequisites, syllabus coverage and source links. |
| Answer cards | Supported claims, conditions, equations, notation, response structures and review state. |
| Tool catalogue | Module ID, supported parameters, assumptions, valid ranges and model version. |
| Evaluation reference | Dataset version identifiers only. Reviewed prompts and answer keys live outside distributed student course packs. |

### Publication rules

Publish a bounded unit first rather than waiting to process an entire book. A pack may contain clearly marked unreviewed resource passages, but damaged extraction must be excluded from answering until corrected. Simulation content requires its own validation; a textbook citation does not validate the implementation.

A replacement creates a new source version. Dependent cards, references and simulations are marked for review. Publish updates atomically and preserve the last usable pack if download or verification fails. Do not silently mix indexes from one version with source pages from another.

Permission to read a professor-supplied book does not automatically establish permission to redistribute it. Record whether the pack can include the PDF, authorised excerpts, original lessons, or references only. Resolve this before student distribution.

## 6 The Study Guide answering contract

### Runtime sequence

Select course and pack version; interpret the question; resolve topic and requested task; retrieve candidate evidence; check whether it supports an answer; select a response structure; call a deterministic tool if needed; assemble the explanation; validate references and required conditions; show the response with its source and review status.

### Three answer paths

- Reviewed response: return a matching approved explanation with its scope and version. Optional rewording makes the new wording generated, even when its underlying card was reviewed.

- Grounded reconstruction: combine retrieved evidence using a task structure, then use the model for a constrained explanation. Mark the answer generated from course sources.

- Insufficient support: ask a focused clarification or explain what is missing. Offer the relevant source excerpt or submission to the educator. Do not fill the gap from unlabelled model memory.

### Modes change teaching behaviour

| Mode | Expected behaviour |
| --- | --- |
| Study Buddy | Explain prerequisites, proceed in smaller steps and check understanding. |
| Helpful Senior | Concise revision, common mistakes and examination structure. |
| Assistant Professor | Formal treatment with assumptions, definitions and derivation steps. |
| Quiz Me | Ask bounded questions; use an answer rubric; explain feedback from sources. |
| Viva Prep | Short oral-style questions, follow-ups and concise model responses. |

### Constraints and failure handling

Citations must come from retrieved source IDs, never model-invented filenames or page numbers. Exact formulas and numerical results should be supplied by reviewed content or tested tools. Keyword checks and citation existence checks help but do not prove semantic correctness. Evaluate factual support with human-reviewed examples.

A retrieval score is not a calibrated confidence probability. Choose abstention thresholds on development data, then freeze them for the held-out evaluation. Follow-ups remain in the selected course unless the student explicitly changes it. Ambiguous circuit names require orientation or diagram context.

Uploaded instructions are source content, not executable commands. The model may request only allowlisted tools with validated parameter schemas. It cannot execute arbitrary code from a document or alter course permissions. Tool errors, missing models and exhausted memory produce visible recovery options.

## 7 Subject modules and integration

Analog Electronics is the depth showcase. The exact unit sequence follows the forthcoming syllabus and course book. The following are proposed module boundaries, not claims of complete syllabus coverage.

| Module | Initial scope | Required evidence |
| --- | --- | --- |
| Diode laboratory | Ideal, fixed-drop and declared nonlinear models; bias and temperature controls. Doping only after a valid model is specified. | Reference curves, units, ranges and comparison of model assumptions. |
| Clipper and clamper workbench | Supported series/shunt and biased arrangements; diode reversal; inputs, resistance and capacitance where applicable. | Conducting intervals, thresholds, transient and steady-state behaviour. |
| Transistor explorer | One selected transistor family and configuration first; input/output curves and operating regions. | Source-backed parameters, region boundaries and reference operating points. |
| Radio Room | AM and DSB-SC first, then FM and a bounded receiver demonstration; waveform and spectrum instruments. | Amplitude/frequency scaling, sidebands, demodulation assumptions and sampling limits. |
| DLCD bench | Gates and selected combinational circuits; IC pinout explorer; digital wiring, truth tables and up to four-variable K-maps. | Manufacturer-backed pinouts; exhaustive input tests; equivalent Boolean expressions. |
| Signal Guide | Standard signals, shifts, scaling, sampling and quantisation; numerical spectrum and inverse reconstruction. | Axis conventions, time/frequency scaling, finite-window effects and reconstruction error. |

### Simulation contract

Every module declares its ID, engine version, parameters and units, valid ranges, assumptions, outputs and warnings. A serialisable state captures exactly what the student sees. The guide uses computed results, not a screenshot guess, to explain the experiment. Tool calls should be previewable and reversible.

### Teaching pattern

Predict a change, adjust one parameter, observe the result, explain it using the source, and answer a short check question. Provide labelled axes, keyboard-accessible controls and a text or tabular alternative to the visual result. Decorative room design must not hide instrument units or assumptions.

Arbitrary circuits, full transistor families, advanced FM receivers, unrestricted Boolean minimisation and symbolic transforms are expansion work. Computational Methods remains optional: a bounded root-finding example with iteration table and convergence plot is sufficient if capacity remains.

## 8 Data contracts and code organisation

### Core records

| Entity | Key fields and relationships |
| --- | --- |
| Course and membership | Course ID, syllabus version; account ID, class ID and role. Membership is service-authoritative. |
| Resource version | Resource ID, version, content hash, page map, rights metadata and extraction status. |
| Unit and concept | Unit ID, topic IDs, prerequisites and links to resource versions. |
| Answer card | Card ID/version, topic, claims, source anchors, assumptions, review status and reviewer. |
| Chat turn | Session ID, pack/model/template versions, selected evidence, answer path and local timestamps. |
| Simulation state | Module/model version, parameters with units, computed outputs and validity flags. |
| Submitted query | Owner, class, selected context, pack version, queue ID, status and educator reply. |
| Evaluation run | Dataset version, code revision, runtime/model configuration, hardware, scores and failures. |

### Proposed repository boundaries

- apps/student and apps/educator: interfaces and role-specific workflows.

- services/classroom: membership, resource distribution and query inbox.

- packages/course-schema and packages/ingestion: pack contracts and preparation.

- packages/retrieval, packages/answer-engine and packages/model-adapters: local answering pipeline with interchangeable runtime adapters.

- packages/simulations and packages/ui: tested subject models and shared accessible controls.

- content/fixtures: permitted sample resources and reviewed examples; no unlicensed course books in a public repository.

- evals/datasets and evals/runners: versioned quality tests; tests/integration and tests/offline: system checks.

- docs/decisions, docs/model-specs and docs/release: rationale, assumptions and operating instructions.

### Interfaces before implementations

Define pack validation, retrieval, answer requests, model generation, simulation execution and query submission as separate interfaces. Changing a model should not require rewriting course content or circuit code. An answer request carries course version, mode and optional simulation state; the result carries text, evidence anchors, answer path and warnings.

Do not select a database, framework, model vendor or hosting provider solely to fill this document. Select them after the local execution spike. Record dependency versions, licences, lockfiles and reproducible run instructions when implementation starts.

## 9 Development stages and gates

Use evidence-based stages rather than calendar promises. Re-estimate effort after the local runtime and document extraction spikes. Jeet owns product decisions; Codex supports implementation and testing; invited educators review subject content when they agree to participate.

| Stage | Deliverable | Exit gate |
| --- | --- | --- |
| 0  Scope and inputs | Syllabus, permitted book, target device inventory, first unit and decision log. | First unit bounded; baseline questions and provisional target hardware selected. |
| 1  Feasibility | Text/equation extraction trial; at least two local configurations; retrieval-only baseline. | Offline answering runs; memory and latency measured; extraction failures understood. |
| 2  Core vertical slice | One unit, citations, modes, follow-ups, clarification and abstention. | Held-out core quality gates met before major simulator expansion. |
| 3  Classroom flow | Educator/student roles, upload/review/publish, pack updates and query inbox. | Role isolation, stale-version handling and offline queue tests pass. |
| 4  Analog Electronics | Validated clipper/clamper integration and bounded diode/transistor tools; expanded source coverage. | Guide explains exact experiment state; subject fixtures reviewed. |
| 5  Subject demonstrations | Radio Room, DLCD bench and Signal Guide minimum modules. | Each works independently and through the guide; references and limits visible. |
| 6  Professor pilot | Onboarding guide, benchmark report, installation package and issue collection. | Pilot users complete core journeys; critical defects resolved. |
| 7  Release 1.0 | Versioned app/model/pack bundle, recovery instructions and release notes. | Release checklist signed off by product owner; subject reviews recorded. |

### Stop and revise conditions

If small-model answers remain unreliable, reduce topic scope, improve evidence extraction or return reviewed cards more often. If target hardware cannot run the configuration, evaluate a smaller model or revise supported hardware explicitly. Do not mask failure with an undisclosed cloud model or relabel a static response demo as successful local generation.

### Work item discipline

Each implementation task names its requirement ID, input/output contract, permitted scope, acceptance evidence and rollback. Build one complete user journey at a time. Keep simulation mathematics separate from presentation code. Update this bible and the decision log when the product boundary changes.

## 10 Evaluation design for the core hypothesis

### Compare the right systems

Run the same question set against A: reviewed cards and retrieval without generation; B: the small local model with ordinary retrieved passages; and C: the proposed structured answer pipeline using that same model. This separates the value of structure from the value of a different model. A source-matched cloud or NotebookLM comparison is optional and must use permitted material with its configuration recorded.

### Dataset plan

Proposed first-unit dataset: 120 reviewed questions. Allocate 40 to development and keep 80 held out for acceptance. In the held-out set use 20 definitions/explanations, 12 comparisons or derivations, 12 numerical or circuit-state questions, 12 multi-turn cases, 8 ambiguous requests, 8 unsupported requests and 8 conflicting-source or injection cases. Assign one primary category to each case.

Separate paraphrases and near-duplicate worked examples across splits. Record expected facts, disallowed claims, source pages, accepted alternatives, required clarifications and applicable tool results. Keep held-out answer keys outside the course pack and prompt templates. Grow the dataset when new units are added; first-unit success does not establish whole-course reliability.

### Scoring rubric

| Dimension | Scoring method |
| --- | --- |
| Correctness | 0 incorrect; 1 material error; 2 correct with a minor omission; 3 correct and complete for the requested scope. |
| Evidence support | Count substantive claims supported by the cited source or declared tool result; separately inspect citation accuracy. |
| Teaching usefulness | 1 to 5 rating for clarity, appropriate depth and usefulness, with a short reviewer reason. |
| Boundary behaviour | Pass/fail for clarification, abstention, conflicting sources and instruction resistance. |
| Performance | Cold start, first token, completed answer p50/p95, peak memory, disk use and offline network attempts. |

### Fair measurement

Use identical resource versions and equivalent output-length limits. Record model file hash, quantisation, prompt/template version, retrieval settings, context budget, hardware and power mode. Repeat generative quality runs three times and report unstable cases. Benchmark at least 30 warm interactions and five cold starts; separate numerical correctness from fluent wording.

Use an educator or competent subject reviewer for answer keys and correctness. A second reviewer checks a sample and resolves disagreements. Automated checks assist but do not replace subject review. Report raw counts, denominators and failures alongside percentages; a small pilot is not proof of universal reliability.

## 11 Proposed acceptance tests

These targets are planning proposals, not measured results. Freeze final thresholds after Stage 1 and before evaluating the held-out set. Performance targets apply only to a named supported device and a declared answer-length limit.

| Test | Provisional gate |
| --- | --- |
| Grounded correctness | At least 90% of answerable held-out cases score 2 or 3; zero critical concept reversals or fabricated numerical results in the release suite. |
| Source support | At least 95% of substantive claims supported in the audited answers; 100% of displayed citation targets resolve to the stated version. |
| Boundaries | At least 90% correct clarify/abstain behaviour on ambiguous and unsupported cases; report each category separately. |
| Offline operation | All core offline journeys pass with network disabled; zero external inference calls or required telemetry calls. |
| Local performance | Proposed warm p95: first response token within 5 seconds, complete answer within 30 seconds for up to 250 words. Record cold start separately. |
| Simulation accuracy | All approved analytical and reference fixtures pass within tolerance defined before implementation; no unexplained invalid outputs. |
| Class isolation | All unauthorised cross-class read, write and publish attempts rejected; students cannot promote their own role. |
| Version integrity | Interrupted update leaves prior pack usable; references never mix resource versions; corrupt pack rejected. |
| Teacher queries | Offline submission survives restart, retries without duplicate delivery and shows educator reply after sync. |
| Usability | At least 4 of 5 pilot students complete a source-backed question and tool follow-up without developer help. |

### Concrete regression cases

Reverse a diode and check the correct half-cycle; change a bias supply and check the threshold; test a clamper across initial and settled cycles. Exhaustively enumerate supported Boolean inputs and compare minimised forms. Test a known sinusoid spectrum, frequency scaling and inverse reconstruction. For each tool, test invalid units, range boundaries and missing parameters.

For chat, test a missing source page, a wrong premise, a corrupted equation, a request outside the syllabus, a mode change mid-session and an instruction embedded in an uploaded document. For the system, test model unavailable, low memory, expired online session, source withdrawal and interrupted download. Show useful recovery states rather than unexplained failure.

## 12 Pilot operation and release readiness

### Pilot structure

Proposed pilot: one Analog Electronics educator and five to ten consenting students using a bounded course pack. Invite other subject professors to inspect the smaller demonstrations. Participation, availability and review time are not assumed commitments.

First demonstrate a sourced explanation, then a follow-up, a circuit-state question, an unsupported question, an offline session, an educator correction and a pack update. Include ordinary student wording and unfamiliar questions rather than only rehearsed prompts.

### What to collect

- Task completion, usefulness ratings and confusion points, with permission for any shared chat excerpts.

- Installation time, download size, device specification and observed performance.

- Educator minutes spent preparing, checking and updating each unit.

- Failure categories: missing evidence, wrong retrieval, incorrect reconstruction, simulation error, confusing UI or installation problem.

- Cost ledger: preparation compute, recurring service costs, model distribution, support and student device requirements. Avoid unsupported claims of being free or cheaper.

### Release checklist

- Core acceptance report names exact code, model, pack and evaluation versions.

- All required 1.0 modules are present; unfinished features are excluded or visibly unavailable.

- Resource permissions, review statuses and simulation assumptions are recorded.

- Application installation and first pack download succeed on supported devices.

- Offline study, update rollback, local data deletion and service backup recovery are checked.

- Professor and student onboarding instructions explain local operation and what gets shared.

- Critical correctness, privacy, authorisation and data-loss defects are closed.

- Known limitations and minimum hardware are published with the release.

### Operational ownership

Jeet approves scope and release. A designated educator approves subject content; Codex-generated explanations are not self-approved. During the pilot, review submitted problems regularly and release corrections in versioned packs. Suspend affected generated answers or tools when a critical conceptual error is confirmed.

### Success beyond the demo

A successful pilot demonstrates useful local answering, meaningful access to source evidence, a working educator correction loop and one tightly integrated simulation journey. Claims about improved learning require a separate study; satisfaction and task completion alone do not establish learning gains.

## 13 Risks decisions and first backlog

| Risk | Response |
| --- | --- |
| Small model loses conditions | Constrain evidence, use reviewed structures and test paraphrases; abstain when support is insufficient. |
| PDF extraction damages equations | Inspect representative pages early; correct or exclude broken content before indexing. |
| Scope grows around the chatbot | Gate simulator expansion on the core vertical slice; maintain explicit module limits. |
| Local install excludes students | Inventory actual devices; measure installation burden and memory before selecting runtime. |
| Teacher review is too expensive | Measure preparation time; reuse cards and highlight only affected content on updates. |
| Simulation looks right but is wrong | Declare models and validate against independent reference cases before visual polish. |
| Source updates invalidate answers | Immutable versions, dependency tracking and a visible outdated-content state. |

### Decision register

D01 Target hardware and operating systems — Jeet supplies device inventory; resolve in Stage 0. D02 Runtime and model — choose from Stage 1 measurements and licence checks. D03 Preparation location — decide where resource processing occurs and whether any cloud assistance is acceptable. D04 Book distribution — confirm permissions before a student pack is published.

D05 Circuit freedom — guided workbench is proposed; unrestricted wiring requires a simulation-engine feasibility task. D06 Offline access policy — decide persistence, enrolment expiry and shared-device behaviour. D07 Course scope — reconcile the Analog Electronics book with the syllabus. D08 Naming — K.A.I Study is the working application name within Project K.A.I. The earlier PhyExperts prototype remains a historical reference.

### First development backlog

- Obtain the Analog Electronics book and syllabus; select one clipper/clamper or diode unit based on source quality.

- Inspect representative prose, equation, diagram and table pages; record extraction limitations.

- Prepare the development questions and reserve held-out cases before tuning.

- Inventory target devices and define a representative baseline machine.

- Run the local model and retrieval feasibility spike; compare structured and unstructured answers.

- Approve the resulting architecture decision, then implement the first complete Study Guide journey.

### Maintaining this bible

Revision 0.2 preserves the agreed product direction and proposed execution plan. Each revision records the changed requirement, reason, affected tests and decision owner. Implementation evidence belongs in linked evaluation reports. Do not turn proposed targets into claimed achievements without recorded test results.

## Revision history

- 0.1: Original PhyExperts planning document.
- 0.2: Repository edition for K.A.I Study within Project K.A.I. Preserves the original scope and proposed targets; clarifies that evaluation answer keys are not distributed in course packs. No test results are claimed.
