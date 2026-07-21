# Nitrodynamics Product-Line Business Models

Self-contained business models for each of the **six product verticals** in the NDAD Defense Platform plan. Platform modules (M1–M5) are shared engineering assets, not product lines, and are referenced inside each model rather than given separate files.

**Investor capital-allocation memos** (thesis, financial case, ask/gates, diligence): see [`../business-cases/`](../business-cases/).

**Sources (authoritative):**

- `Defense_Platform_Business_Plan_Financial_V2.xlsx` — sheets `V1_AESA` … `V6_MilAI`, `Backlog`, `Revenue`, `Assumptions`, `Platform`, `ReuseMatrix`
- `investor_plan/03_strategy_and_products.md`, `02_market_opportunity.md`, `04_financial_model.md`, `07_operating_model.md`, `08_risk_register.md`
- `Defense_Platform_Workbook_Explanation.md`

**Currency:** INR Crore (₹ Cr) unless noted. Horizon: Y1–Y10.

**Important model note:** Consolidated *recognized* revenue comes from `Backlog` deliveries (`Revenue!D6:M11`), not from V-sheet unit × ASP totals. V-sheets are unit-economics / COGS-ratio detail. Figures below use **recognized revenue** for P&L impact and **V-sheet** for ASP / BoM / units.

---

## Index

| Code | Product line | Launch | File | One-line summary |
| ---- | ------------ | ------ | ---- | ---------------- |
| **V1** | AESA Radar | Y2 | [business-model-aesa-radar.md](./business-model-aesa-radar.md) | Multi-band AESA (air / ground / naval); ~₹865 Cr recognized revenue by Y10; heavy M1–M3 reuse. |
| **V2** | Electronic Warfare & SIGINT | Y1 | [business-model-ew-sigint.md](./business-model-ew-sigint.md) | Day-1 cash engine; iDEX ESM MoQ ₹210 Cr; four EW/SIGINT variants; anchors Y1–Y3. |
| **V3** | Counter-UAS (Anti-Drone) | Y2 (MVP) | [business-model-counter-uas.md](./business-model-counter-uas.md) | Highest unit volume; layered soft/hard-kill C-UAS; ~₹1,037 Cr recognized by Y10. |
| **V4** | MALE-class ISR UAS | Y4 | [business-model-male-uas.md](./business-model-male-uas.md) | Longest-cycle airframe + certification; ISR / strike / SIGINT variants; largest Y10 backlog. |
| **V5** | Autonomous AUV / USV | Y3 | [business-model-autonomous-auv-usv.md](./business-model-autonomous-auv-usv.md) | Asset-light maritime autonomy; partner hulls; AUV mine-hunt / ASW + USV ISR host. |
| **V6** | Military AI Systems | Y1 (ship) / Y2 (recog.) | [business-model-military-ai.md](./business-model-military-ai.md) | Highest GM (~93–94%); edge box + OIDSS + fusion middleware; attaches to all hardware lines. |

---

## Portfolio snapshot (recognized revenue, ₹ Cr)

| Vertical | Y1 | Y5 | Y10 | Y10 mix |
| -------- | --: | --: | --: | ------: |
| V1 AESA | 0 | 328 | 865 | 17% |
| V2 EW/SIGINT | 105 | 428 | 760 | 15% |
| V3 C-UAS | 0 | 232 | 1,037 | 21% |
| V4 MALE UAS | 0 | 262 | 1,386 | 27% |
| V5 AUV/USV | 0 | 100 | 549 | 11% |
| V6 Military AI | 0 | 95 | 458 | 9% |
| **Total** | **105** | **1,444** | **5,055** | **100%** |

*Source: `Revenue!D6:M12` / `Backlog!D89:M95`.*

---

## Shared platform (not a product line)

Five modules amortised across V1–V6 (~₹575 Cr cumulative platform NRE): **M1** Radio/Microwave · **M2** Signal Processing · **M3** Systems Engineering · **M4** Embedded & Mission Software · **M5** AI/ML. Reuse strength rises from ~25–60% in Y1 to ~97–99% by Y10 (`Platform`, `ReuseMatrix`).
