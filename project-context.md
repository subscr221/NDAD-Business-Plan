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

- **Company one-liner:** Nitrodynamics is India's platform-native defense
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
  Day-1 ESM cash engine — the **Rs.105 Cr opening order book (Phase 1: 5 systems ×
  Rs.21 Cr, 12-month delivery)** of a **firm Rs.210 Cr iDEX ESM MoQ** (10 systems ×
  Rs.21 Cr, two 5-system phases of 12 months each, ~24 months total; development
  complete, 4 milestones signed off; first-of-production-model in build) — funds
  build-out. This is iDEX **production-order revenue**, distinct from the iDEX/TDF
  development grants excluded by D-005. _(Workbook `Cover!C7`/`Strategy!C10` label this
  ~Rs.200 Cr — a rounding to be corrected to Rs.210 Cr; see D-012.)_

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
| D-008 | 2026-06-28 | Soften "India's **first** platform-native defense prime" to a positioning claim anchored on the structural moat (cross-domain M1-M5 reuse + IP ownership) | Keep "first" / demote to positioning | "First" superlative is externally unverifiable and easily contested; structural + IP framing is defensible and ties to MoD atmanirbhar/source-code preference (D-001/D-006) | ACTIVE | Refines §1 one-liner |
| D-009 | 2026-06-28 | Define the Rs.105 Cr ESM book as a **5-system iDEX production order (5 × ~Rs.21 Cr) within a 10-system program**; classify as production-order revenue in the base case | — | Resolves prior undefined status (signed/LOI/forecast); 4 completed milestones de-risk technical/qualification; confirms order revenue (not grant), consistent with D-005 | ACTIVE | — |
| D-010 | 2026-06-28 | Record that the **full 10-system order is firm and held by NDAD**, delivered 5+5 systems per year (~Rs.210 Cr total firm backlog); the Rs.105 Cr opening order book is the Year-1 tranche, Year-2 (~Rs.105 Cr) is firm backlog | — | Firm full-program commitment (not a 5-of-10 dual-source split) materially de-risks Day-1 traction and lengthens the funded runway; refines the scope context of D-009 | SUPERSEDED | Value (~Rs.210 Cr) corrected by D-011; firm-order fact still valid; Refines D-009 |
| D-011 | 2026-06-28 | Reconcile ESM value after workbook trace: keep **Rs.105 Cr opening order book (Year-1, 5 systems)** as the headline; record the **full firm iDEX ESM MoQ at ~Rs.200 Cr** (workbook `Cover!C7` / `Strategy!C10`), firm across Y1–Y2 (Year-2 balance ~Rs.95 Cr) | Rs.200 (workbook) / Rs.210 (10×~21) / Rs.105 headline | Workbook governs headline numbers (§0); founder decision keeps Rs.105 Cr lead with the full ~Rs.200 Cr MoQ described behind it; resolves the 105/200/210 conflict | SUPERSEDED | Value refined by D-012 (Rs.210 Cr, phased terms); Supersedes D-010 (value only) |
| D-012 | 2026-06-28 | **Definitive ESM MoQ terms (founder/contract):** full firm iDEX ESM MoQ = **Rs.210 Cr** = 10 systems × **Rs.21 Cr**, delivered in **two phases of 5 systems**, each phase over **12 months** (~24 months total). Phase 1 = the **Rs.105 Cr opening order book**; Phase 2 = Rs.105 Cr | Rs.210 (contract) vs Rs.200 (workbook label) | Founder-stated actual contract terms are authoritative over the rounded workbook label; confirms the Rs.210 Cr figure first noted in D-010 and fixes the per-unit price at Rs.21 Cr/system. **Action:** correct workbook `Cover!C7`/`Strategy!C10` 200→210 | ACTIVE | Supersedes D-011 (value); confirms D-010 value |

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
- **OQ-A (ESM contractual status & value) — RESOLVED (D-009, D-012):** Rs.105 Cr opening
  order book = **Phase 1** (5 systems × Rs.21 Cr, 12-month delivery) of a **firm Rs.210 Cr
  iDEX ESM MoQ** (10 systems × Rs.21 Cr, two 5-system phases of 12 months each; Phase 2 =
  Rs.105 Cr). Production-order revenue, post-qualification (4 milestones),
  first-of-production-model in build. _Action:_ correct the workbook's Rs.200 Cr label
  (`Cover!C7`/`Strategy!C10`) to Rs.210 Cr — narrative label only; revenue is Backlog-derived.
- **OQ-B (the "first" superlative) — RESOLVED (D-008):** demoted from a factual claim
  to a structural positioning statement.
- **OQ-C (MoQ unit price vs catalogue SKU) — OPEN:** D-012 fixes the iDEX ESM MoQ unit
  price at **Rs.21 Cr/system**, but the deck catalogue (`investor_plan/03_strategy_and_products.md`)
  prices the ESM SKUs at **EW-A Rs.25-30 Cr** and **EW-B Rs.29-35 Cr** — both *above* Rs.21 Cr.
  The SOT does not state which catalogue SKU the MoQ covers. Two candidate resolutions, **neither
  yet confirmed by the founder/contract:** (a) Rs.21 Cr is iDEX **anchor / first-production-order
  pricing** on the EW-A (or EW-B) SKU, below commercial list; or (b) the MoQ covers a **distinct,
  lower-spec ESM configuration** not separately listed in the catalogue. _Interim deck treatment
  (non-inventive):_ use Rs.21 Cr for all MoQ/Day-1 figures, reserve catalogue ranges for forward
  commercial volume pricing, and flag the gap inline (reconciliation note added to §V2 of section 03).
  _Action:_ founder to confirm (a) vs (b); on resolution, log as a decision and remove this OQ.

---

## 4. Artifact Registry (dependency chain)

> Read top-to-bottom. Each artifact derives from the ones above it **plus this SOT**.
> Sync rule: when an upstream artifact changes, log the change in Section 2, re-distill
> for the downstream consumer (`bmad-distillator`, `--validate`), then regenerate downstream.
> Canonical folder-by-folder registry companion: `summaries/NDAD_Artifact_Registry.md`.

| Order | Artifact | Path | Derives from | Owner agent / skill |
| - | - | - | - | - |
| 0 | **SOT (this file)** | `project-context.md` | — | All agents |
| 0.5 | Registry map companion | `summaries/NDAD_Artifact_Registry.md` | SOT | All agents |
| 1 | Source financial model | `Defense_Platform_Business_Plan_Financial_V2.xlsx` | SOT | — |
| 1 | Investor plan sections | `investor_plan/00..10_*.md` | SOT + model | — |
| 2 | Product Brief | `{planning_artifacts}/brief.md` | SOT + investor plan | `bmad-product-brief` |
| 3 | PRFAQ + PRD distillate | `{planning_artifacts}/prfaq-nitrodynamics.md` | brief + SOT | `bmad-prfaq` |
| 4 | PRD | `{planning_artifacts}/prd.md` | PRFAQ distillate + SOT | `bmad-create-prd` |
| 5 | UX / visual system | `Design Folders/` | PRD + SOT | `wds-agent-freya-ux` |
| 6 | Validation pass | `summaries/*` | brief + PRFAQ | `bmad-cis-design-thinking` |
| 7 | **Investor Deck** | `investor_plan/` deck output | PRD + brief + PRFAQ FAQ + SOT | `bmad-cis-agent-presentation-master` |

---

## 5. Change Log (of this file)

| Date | Author | Change |
| - | - | - |
| 2026-06-28 | subscr221 | Initial SOT established (Canonical Facts, Master Decision Log D-001..D-007, Artifact Registry, Authority Rules). |
| 2026-06-28 | subscr221 | Logged D-008 (soften "first platform-native" → positioning) and D-009 (define Rs.105 Cr ESM as a 5-system iDEX production order, 5 × ~Rs.21 Cr); resolved OQ-A / OQ-B; updated §1 one-liner and the ESM canonical fact. |
| 2026-06-28 | subscr221 | Logged D-010: full 10-system ESM order is firm (5+5 delivered per year, ~Rs.210 Cr total); Rs.105 Cr = Year-1 tranche, Year-2 (~Rs.105 Cr) firm backlog. Resolved OQ-A firm/phased residual. |
| 2026-06-28 | subscr221 | Workbook trace (`Cover!C7`, `Strategy!C10`): full iDEX ESM MoQ = ~Rs.200 Cr (not ~Rs.210 Cr). Logged D-011 (supersedes D-010 value); kept Rs.105 Cr Year-1 as headline; corrected §1 fact and OQ-A. |
| 2026-06-28 | subscr221 | Founder contract terms: ESM MoQ = **Rs.210 Cr** (10 × Rs.21 Cr), two 5-system phases of 12 months each; Phase 1 = Rs.105 Cr opening book. Logged D-012 (supersedes D-011 value; confirms D-010's Rs.210). Workbook Rs.200 label flagged for correction. |
| 2026-06-28 | Claude (regen) | Downstream regeneration to D-008..D-012: added MoQ-vs-catalogue price reconciliation note to §V2 of `investor_plan/03_strategy_and_products.md` and logged **OQ-C** (Rs.21 Cr MoQ price vs Rs.25-35 Cr EW-A/EW-B catalogue — unresolved SKU/anchor-pricing question, not invented). Regenerated consolidated `investor_plan/Nitrodynamics_Investor_Plan.md` from corrected sections 00-10 via deterministic build script `build_investor_plan.py`. .docx/.pdf exports: original LibreOffice-on-Linux pipeline absent on this Windows host (no pandoc/LibreOffice/PDF renderer) — flagged to founder. |
