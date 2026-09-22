# First unit: junction diodes

Status: source-mapping draft for Stage 1. No educator approval or working tutor is claimed.

## Scope and credit

Primary source: Robert L. Boylestad and Louis Nashelsky, *Electronic Devices and Circuit Theory*, 11th edition, Pearson Education, Inc., 2013. ISBN-13: 978-0-13-262226-4. Bibliography verified against the uploaded title and copyright pages. Exact file versions are in [register.json](register.json).

The supplied Semester 3 guide, PDF pp. 10–11, places these topics in Analog Electronics-I, ECC-211. It is a directional guide referencing a legacy handbook; its extensions and likely labs are not confirmed assessment requirements. Assignment 1 provides evidence of current topic relevance. Assignment 2 is reserved for later BJT coverage. The assignment header identifies Maharaja Agrasen Institute of Technology; no individual author credit was verified.

## Source map

All book anchors below are 1-based. Within this sampled span, PDF page = printed page + 21. Do not apply that offset to front matter or uninspected parts of the book. Ranges can overlap where sections share a page.

| Topic | Book section | Printed pages | PDF pages | Assignment 1 mapping | Trial status |
| --- | --- | --- | --- | --- | --- |
| Doping, carriers and junction prerequisites | 1.5 | 7–10 | 28–31 | Q2(a) background | Text extracted; content review pending |
| Junction formation; no, reverse and forward bias | 1.6 | 10–13 | 31–34 | Q2(a) | Text extracted; content review pending |
| Exponential I–V equation and thermal voltage | 1.6, equations 1.2–1.3 | 13–15 | 34–36 | Q3(a) | PDF p.34 visually checked; conditions require explicit fields |
| Practical material curves, including Ge | 1.6 | 16–18 | 37–39 | Q1(a) | Curve reading review pending |
| Temperature effects | 1.6, Fig.1.19 | 18–19 | 39–40 | Q1(c) | Both pages visually checked; unit extraction error found |
| Ideal model | 1.7 | 20–21 | 41–42 | Q1(a) | Text extracted; content review pending |
| Static, dynamic and average resistance | 1.8 | 21–27 | 42–48 | Q3(b) | Text extracted; equation review pending |
| Piecewise-linear and constant-drop models | 1.9 | 27–30 | 48–51 | Q1(b) | PDF p.49 visually checked; model assumptions must be retained |

Capacitances (Q2(b)), rectifiers, breakdown/regulation applications, clippers/clampers and all BJT questions are outside this first answering unit. Shared pages may contain such text; page extraction does not grant topic eligibility. Section 1.10 starts on PDF p.51 and must be excluded when constructing the first pack.

## Citation and course-pack contract

An evidence record must contain `resource_id`, `source_sha256`, `section`, `pdf_page`, `printed_page`, optional figure/equation IDs, concept ID, applicable assumptions, and review status. Display authors, short title, edition and printed page; open the exact PDF page from the same hashed local resource. A replacement PDF requires remapping and a new pack version. Never silently use an offset from another edition.

Answer cards are separate authored records with evidence references, expected concepts, prerequisites, model assumptions, common misconceptions and review provenance. Raw extraction is never automatically promoted to a reviewed card. The initial pack is private and will not contain assignment answer keys. The public repository contains metadata, original development prompts and tooling, not textbook excerpts, page images or copied assignments.

## Initial decisions

- D01: user-reported baseline is M2, 8 GB unified memory, Sonoma 14.5, 252.18 GB available / 494.38 GB total. This is a test target, not a supported-device claim.
- D07: bounded diode foundations unit above selected for feasibility. Whole-course reconciliation remains open.
- D04: attribution recorded; redistribution permission remains unresolved. Source access for development does not establish publication permission.
- No model, runtime or production preparation framework has been selected.

## Next work and review needs

1. Finish visual checking of the selected sections, including graph axes and resistance equations.
2. Build private draft cards and review their conditions and citations before use as baseline A.
3. Expand the initial development prompts to the proposed 40; reserve 80 held-out cases before tuning. The initial prompts are not a completed evaluation set.
4. Implement retrieval and then compare local model configurations on the target Mac.

Faculty confirmation and subject review are needed before assessed coverage or reviewed-content claims. They do not block this extraction trial. No terminal action is needed from Jeet yet.
