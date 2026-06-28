# PROJECT CONTEXT — Nitrodynamics (NDAD) Business Plan

> **Single Source of Truth (SOT).** This file is the authoritative reference for
> every AI agent (Saga, Freya, Maya, Caravaggio) and every BMAD skill working on
> this project. It is auto-loaded as a persistent fact via the
> `file:{project-root}/**/project-context.md` glob.

---

## 0. AI Authority Rules (read first)

- This file is the **single source of truth**. On any conflict between an
  artifact (brief, PRFAQ, PRD, financial model, deck) and this file, **THIS FILE WINS**.
- **No strategic claim** enters the brief, PRFAQ, PRD, or investor deck unless it
  is logged in the Master Decision Log (Section 2) or the Canonical Facts (Section 1).
- All headline numbers must trace to the workbook
  `Defense_Platform_Business_Plan_Financial_V2.xlsx` or `investor_plan/`. If a
  number is an analyst reconstruction or assumption, it must be **flagged as such**.
- The Master Decision Log is **append-only**. Never overwrite a decision; mark it
  `SUPERSEDED` and reference the superseding decision ID.
- When a fact here is missing, ambiguous, or stale, **ask before inventing** —
  raise it as an Open Question (Section 3), do not silently fill the gap.
- Currency is **INR Crore (Rs.Cr)** unless explicitly stated otherwise.

---

## 1. Canonical Facts

- **Company one-liner:** Nitrodynamics is India's first platform-native defense
  prime — a single reusable engineering platform (radio/microwave, signal
  processing, systems engineering, embedded/mission software, AI/ML) industrialised
  into six product lines across air, land, sea and cyber.
- **Tagline:** "Engineer once, deploy everywhere. One platform, six product lines, four domains."
- **Target customer:** Indian Ministry of Defence (MoD) and armed services as
  anchor buyer (Day 1); allied / friendly foreign governments via the export
  channel from Year 2 (Rs.50,000 Cr 2028-29 export target).
- **Market:** Multi-domain defense — EW/SIGINT, AESA radar, counter-UAS,
  autonomous maritime (AUV/USV), MALE surveillance drones, and Military AI.
  Counter-UAS ~25-30% CAGR to USD 6-7bn by 2030; EW ~USD 22-25bn/yr globally.
- **Business model:** Platform reuse compounding — qualified building blocks (M1-M5)
  are reused across product lines (V1-V6), lifting blended gross margin from ~51%
  (Y1) to ~67% (Y10) and EBITDA margin to ~46.4%, vs 10-15% legacy-prime norm.
  Day-1 ESM cash engine (Rs.105 Cr opening order book) funds build-out.

### Headline plan metrics (authoritative subset)

| Metric | Value |
| - | - |
| 10-yr cumulative revenue | Rs.21,200 Cr |
| Year-10 revenue | Rs.5,055 Cr |
| Year-10 backlog | Rs.16,680 Cr |
| Year-10 EBITDA / margin | Rs.2,347 Cr / 46.4% |
| 10-yr cumulative FCF | Rs.4,803 Cr |
| Project IRR / NPV @ WACC | 31.9% / Rs.747 Cr |
| Total equity raised | Rs.1,100 Cr (Seed 450 / A 400 / B 250) |
| Peak debt / repaid by | Rs.200 Cr / Year 9 |
| First positive EBITDA / FCF | Year 4 |

---

## 2. Master Decision Log (append-only, ADR-style)

| ID | Date | Decision | Options considered | Rationale | Status | Supersedes |
| - | - | - | - | - | - | - |
| D-001 | 2026-05-17 | Anchor on MoD as primary buyer; layer allied-export pipeline from Y2 | MoD-only / export-first / dual | Atmanirbhar Bharat preference + dated Rs.50,000 Cr export target de-risk demand | ACTIVE | — |
| D-002 | 2026-05-17 | Lead with ESM/SIGINT (V2) as Day-1 cash engine | ESM-first / AESA-first / C-UAS-first | Part-developed line + Rs.105 Cr opening backlog funds remaining five lines | ACTIVE | — |
| D-003 | 2026-05-17 | Raise Rs.1,100 Cr equity across three rounds (450/400/250) | Single large round / 3 stepped rounds | Stepped, milestone-gated rounds preserve ~71% founder+ESOP post-B | ACTIVE | — |
| D-004 | 2026-05-17 | Dual-gate every round (platform-maturity AND contracted backlog) | Backlog-only / platform-only / joint | Joint gate avoids fixed-price exposure and equity burn on un-demanded tech | ACTIVE | — |
| D-005 | 2026-05-17 | Exclude iDEX / TDF / Make-II grants from base case | Include / exclude | Plan must stand alone; grants framed as separable upside | ACTIVE | — |
| D-006 | 2026-05-17 | Ship ITAR-clean and EAR99 dual variants from Day 1 | Single variant / dual variant | Maximises addressable export buyers, mitigates export-control friction | ACTIVE | — |
| D-007 | 2026-05-17 | Seek **Seed Rs.450 Cr** as the lead ask | — | Single tranche unlocks platform M1-M5 + ESM industrialisation flywheel | ACTIVE | — |

---

## 3. Pivot Points / Open Questions

- **OQ-001:** Pre-money valuations are analyst illustrations (Seed 1,800 / A 4,500 /
  B 8,000 Rs.Cr), not founder-published. Confirm before any deck valuation claim.
- **OQ-002:** Series B (Rs.250 Cr) is pricing-sensitive to Y3 milestone slip
  (V5 first-ship, V4 qualification, Rs.1,800 Cr cumulative bookings). Trigger: any
  Wave-3 slip forces a Series B re-size / re-price decision.
- **OQ-003:** BG collateral de-escalation schedule (100%→50%→30%→20%) assumed; if
  the bank holds at 100% past Y2, peak deficit extends — revisit Series B sizing.
- **OQ-004:** Cash-EoY line in funding plan is an analyst reconstruction; workbook
  `CashFlow` sheet is authoritative and was saved without recalc cache.

---

## 4. Artifact Registry (dependency chain)

> Read top-to-bottom. Each artifact derives from the ones above it **plus this SOT**.
> Sync rule: when an upstream artifact changes, log the change in Section 2, re-distill
> for the downstream consumer (`bmad-distillator`, `--validate`), then regenerate downstream.

| Order | Artifact | Path | Derives from | Owner agent / skill |
| - | - | - | - | - |
| 0 | **SOT (this file)** | `project-context.md` | — | All agents |
| 1 | Source financial model | `Defense_Platform_Business_Plan_Financial_V2.xlsx` | SOT | — |
| 1 | Investor plan sections | `investor_plan/00..10_*.md` | SOT + model | — |
| 2 | Product Brief | `{planning_artifacts}/brief.md` | SOT + investor plan | Saga · `bmad-product-brief` |
| 3 | PRFAQ + PRD distillate | `{planning_artifacts}/prfaq-nitrodynamics.md` | brief + SOT | `bmad-prfaq` |
| 4 | PRD | `{planning_artifacts}/prd.md` | PRFAQ distillate + SOT | `bmad-create-prd` |
| 5 | UX / visual system | `Design Folders/` | PRD + SOT | Freya · `wds-agent-freya-ux` |
| 6 | Validation pass | `summaries/*` | brief + PRFAQ | Maya · `bmad-cis-design-thinking` |
| 7 | **Investor Deck** | `investor_plan/` deck output | PRD + brief + PRFAQ FAQ + SOT | Caravaggio · `bmad-cis-agent-presentation-master` |

---

## 5. Change Log (of this file)

| Date | Author | Change |
| - | - | - |
| 2026-06-28 | subscr221 | Initial SOT established (Canonical Facts, Master Decision Log D-001..D-007, Artifact Registry, Authority Rules). |
