# NDAD Artifact Registry Map

This is the folder-by-folder registry for NDAD. `project-context.md` remains the source of truth; this map only explains where artifacts live, who writes them, and who reads them. All names below use local skill IDs as the single naming scheme.

## Registry rules

- One writer per artifact family.
- Downstream artifacts are read-only to downstream consumers.
- Presentation artifacts never outrank planning artifacts.
- If an upstream artifact changes, regenerate the next downstream artifact before treating it as current.
- `bmad-spec` is the preferred contract layer between requirements and solutioning.

## Current artifact lanes

| Layer | Folder / file | Written by skill ID | Read by skill ID | Notes |
| --- | --- | --- | --- | --- |
| SOT | `project-context.md` | all skills | all skills | Canonical authority for NDAD facts and routing. |
| Evidence | `Defense_Platform_Business_Plan_Financial_V2.xlsx`, `investor_plan/00..10_*.md` | human source material | `bmad-product-brief`, `bmad-prfaq`, `bmad-create-prd`, `bmad-create-architecture`, `bmad-cis-design-thinking`, `bmad-cis-agent-presentation-master` | Inputs only; do not overwrite as outputs. |
| Brief | `{project-root}/_bmad-output/planning-artifacts/brief.md` | `bmad-product-brief` | `bmad-prfaq`, `bmad-create-prd`, `bmad-cis-agent-presentation-master` | First structured strategy artifact. |
| Working Backwards | `{project-root}/_bmad-output/planning-artifacts/prfaq-<project>.md` | `bmad-prfaq` | `bmad-create-prd`, `bmad-spec`, `bmad-cis-agent-presentation-master` | Customer-first validation of the concept. |
| PRD | `{project-root}/_bmad-output/planning-artifacts/prd.md`, `addendum.md` | `bmad-create-prd`, `bmad-edit-prd` | `bmad-spec`, `bmad-create-architecture`, `bmad-create-epics-and-stories`, `bmad-check-implementation-readiness` | Canonical requirements source. |
| Validation | `{project-root}/_bmad-output/planning-artifacts/validation-report.html`, `.md` | `bmad-validate-prd`, `bmad-check-implementation-readiness` | `bmad-product-brief`, `bmad-create-prd`, `bmad-create-architecture` | Gate output; never a source doc. |
| UX | `Design Folders/` | `wds-agent-freya-ux` | `bmad-spec`, `bmad-create-architecture`, `bmad-cis-agent-presentation-master` | Visual and behavioral design lane. |
| Architecture | `{project-root}/_bmad-output/planning-artifacts/ARCHITECTURE-SPINE.md` or `architecture.md` | `bmad-create-architecture` | `bmad-create-epics-and-stories`, `bmad-quick-dev`, `bmad-cis-agent-presentation-master` | Technical decision layer. |
| Spec kernel | `{project-root}/_bmad-output/specs/spec-<slug>/SPEC.md`, `.memlog.md`, companions | `bmad-spec` | `bmad-create-architecture`, `bmad-create-epics-and-stories`, `bmad-dev-story`, `bmad-cis-agent-presentation-master` | Canonical machine contract; preserve `CAP-N` IDs. |
| Epics / stories | `{project-root}/_bmad-output/planning-artifacts/epics*.md` | `bmad-create-epics-and-stories` | `bmad-create-story`, `bmad-dev-story`, `bmad-check-implementation-readiness` | Turns requirements into implementable work. |
| Summary artifacts | `summaries/*.md` | `bmad-cis-design-thinking`, `bmad-review-adversarial-general`, `bmad-review-edge-case-hunter` | `bmad-product-brief`, `bmad-prfaq`, `bmad-create-prd`, `bmad-cis-agent-presentation-master` | Use for stress tests, audits, and IC-style summaries. |
| Investor deck | `investor_plan/` deck output | `bmad-cis-agent-presentation-master` | exec stakeholders | Narrative output; must stay aligned to upstream artifacts. |

## Skill responsibility map

| Skill ID | Writes | Reads | Primary use |
| --- | --- | --- | --- |
| `wds-agent-saga-analyst` | Brief, PRFAQ inputs, requirement framing | SOT, evidence, brief, PRFAQ, PRD, spec | Strategy-to-requirement mapping. |
| `wds-agent-freya-ux` | UX/visual system | PRD, spec, architecture | Requirements-to-design translation. |
| `bmad-cis-design-thinking` | Validation notes, stress-test summaries | Brief, PRFAQ, PRD, spec, validation | Challenge weak claims and expose gaps. |
| `bmad-cis-agent-presentation-master` | Investor deck and presentation narrative | SOT, brief, PRFAQ, PRD, spec, architecture, summaries | Keep the deck synchronized with the source chain. |
| `bmad-create-architecture` | Architecture | PRD, spec, validation, UX | Make technical decisions explicit. |
| `bmad-agent-dev` | Code and tests | Epics, stories, architecture, spec | Implement only after the upstream chain is complete. |

## Recommended registry order

1. `project-context.md`
2. Evidence in `investor_plan/` and the financial model
3. Brief and PRFAQ under `_bmad-output/planning-artifacts/`
4. PRD and validation gates
5. `bmad-spec` spec folder under `_bmad-output/specs/`
6. Architecture and epics/stories
7. UX, summaries, and deck outputs

## Ownership summary

- `wds-agent-saga-analyst` owns strategy capture.
- `bmad-prfaq` owns the working-backwards challenge.
- `bmad-create-prd` owns the PRD.
- `bmad-spec` owns the canonical spec folder.
- `bmad-create-architecture` owns architecture.
- `wds-agent-freya-ux` owns UX.
- `bmad-cis-agent-presentation-master` owns the investor deck.
- `bmad-cis-design-thinking` owns validation and synthesis summaries.
