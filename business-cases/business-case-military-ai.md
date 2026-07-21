# Investor Business Case — V6 Military AI Systems

**Product code:** V6 · **Ops ship:** Y1 · **First recognized revenue:** Y2 · **Y10 mix:** ~9%  
**Sibling model:** [`../business-models/business-model-military-ai.md`](../business-models/business-model-military-ai.md)  
**Sheets:** `V6_MilAI`, `Revenue!D11:M11`, `Backlog` (V6)

---

## 1. Investment thesis

V6 is the **margin and lock-in layer** of the platform: edge AI mission boxes, OIDSS decision-support licences, and sensor-fusion middleware that attach to every AESA, ESM, C-UAS, UAS, and AUV/USV sale. At only ~9% of Y10 revenue (**~₹458 Cr recognized**), it runs at **~93–94% BoM GM** and contributes an estimated **~250–300 bps** of blended company GM lift. Capital into V6 is capital into software-grade economics on a hardware footprint — the explicit mix lever toward ~67% company GM / ~46% EBITDA by Y10 — not a standalone Palantir clone orphaned from sensors.

**Why now:** Operators need edge inference on disconnected platforms *and* enterprise OIDSS under Indian clearance constraints; hardware primes lack coherent fusion; AI startups lack the platforms models run on. India CMMC/export-control posture for FMS-ready AI is a barrier that funded compliance turns into moat.

---

## 2. Opportunity & market

| Frame | Figure | Source |
| ----- | ----- | ------ |
| Defense AI TAM | USD 8–12 bn today, ~3× by 2030 | `02_market_opportunity.md` |
| CAGR | 20%+ | same |
| India | Emerging; anchor share on indigenous platforms | same |
| Comparables | Palantir DoD ~USD 0.7–0.8 bn run-rate; Anduril Lattice; Shield AI valuations | same |

**Strategic KPI is attach rate**, not standalone TAM share. Every hardware award is a distribution channel.

---

## 3. Product & competitive position

**What is sold**

| Variant | Role | Pricing | Y1 ASP | Y10 ASP | Y10 units |
| ------- | ---- | ------- | -----: | ------: | --------: |
| AI-A | Edge AI mission box | Appliance | ₹3.8 Cr | ~₹3.18 Cr | 55 |
| AI-B | OIDSS | **Annual licence** | ₹11.4 Cr/yr | ~₹9.54 Cr | 35 |
| AI-C | Sensor-fusion middleware | Licence | ₹5.7 Cr | ~₹4.77 Cr | 52 |

Y10 supporting total ~142 units/licences. M5 AI/ML is both product engine and shared module for V3–V5.

**Moat**

| vs | Edge |
| -- | ---- |
| Defense AI startups | Ships the hardware AI runs on → higher attach, lower displacement |
| Tier-1 primes | Software/AI mix score 4 vs ~2; faster release cadence |
| Palantir-class | Narrower horizontal analytics; deeper vertical integration with owned sensors |

Company scorecard: Military AI / fusion **4/4**; Software/AI revenue mix **4/4**.

---

## 4. Business model snapshot

- **Models:** Edge appliance (AI-A); recurring OIDSS (AI-B); middleware licence (AI-C).
- **Recognition:** **25%** of opening backlog / year (`Backlog!D87`). SW lag 3–12 months; AI-A 6–9 months.
- **Attach-first GTM:** Standard line item on V1–V5 proposals.
- **Detail:** Sibling business-model §§3–6.

---

## 5. Financial case (workbook)

### Recognized revenue — `Revenue!D11:M11`

| Y1 | Y2 | Y3 | Y4 | Y5 | Y10 |
| --: | --: | --: | --: | --: | --: |
| **0** | **9** | 24 | 50 | **95** | **458** |

Y10 BoM COGS ≈ ₹26 Cr → **~94% GM (BoM only)**. Closing backlog Y10 ≈ **₹2,130 Cr**.

### Supporting unit economics — `V6_MilAI`

| Metric | Y1 | Y5 | Y10 |
| ------ | --: | --: | --: |
| Supporting revenue | **30.4** | 299 | 757 |
| Units / licences | 5 | 59 | 142 |
| GM % | **93.1%** | **94.1%** | **94.4%** |

### Timing gap (ops vs P&L)

V-sheet shows Y1 supporting revenue ₹30.4 Cr (5 units); Backlog Y1 opening for V6 = 0 → **Y1 recognized = ₹0**; first recognition Y2 ₹9.12 Cr. Strategy narrative “V6 ships Y1” is operationally true; **P&L recognition lags one year** in the backlog engine.

### Bookings — `Backlog!D25:M25`

Y1 ₹36.5 Cr → Y10 ₹757 Cr (bookings track supporting revenue late-horizon).

### Capital attribution

Seed funds **first Military AI software releases** and M5 platform NRE (~₹160 Cr of ₹575 Cr platform total over 10 yrs — heaviest AI module spend Y2 ₹65 Cr). CMMC L3 compliance (~₹14.25 Cr / yr company stack) is a shared trust prerequisite. Cloud/secure hosting for OIDSS not fully itemised per-vertical. **No V6-only equity** — returns leverage attach on hardware funded by the same rounds.

### Scale milestones

| Gate | Signal |
| ---- | ------ |
| Supporting shipments Y1 | 5 units/licences (V-sheet) |
| First recognized revenue | **Y2** (workbook) |
| GM | ≥93% every year |
| Y5 / Y10 recognized | ~₹95 / ~₹458 Cr |
| Attach rate on V1–V5 | “Standard” by Y5 |
| Blended GM contribution | ~250–300 bps by Y10 |

---

## 6. Go-to-market & pipeline

1. Attach-first — mandated line item on hardware capture playbooks.
2. Land-and-expand OIDSS — AI-B renewals; expand seats/theatres.
3. Early ship with V2 — Y1 industrial narrative; export AI with EW packs from Y2.
4. Quarterly software release cadence vs multi-year HW blocks.
5. Middleware lock-in — once AI-C fuses a sensor fleet, hardware displacement cost rises.

---

## 7. Use of proceeds — what investment unlocks for V6

| Unlock | Effect |
| ------ | ------ |
| M5 AI/ML platform NRE | Models, MLOps, autonomy shared with V3–V5 |
| First software ship (Seed gate) | Proof of software cash engine alongside ESM |
| CMMC L3 / cybersecurity programme | FMS-ready AI prerequisite |
| Secure cloud / on-prem OIDSS partners | AI-B deployment path |
| Bundle mandates in capture playbooks | Attach rate = primary value driver |

---

## 8. Risks, mitigations & open diligence

| Risk | Residual | Mitigation |
| ---- | -------- | ---------- |
| Model poisoning / adversarial (R-CY-03) | Medium | MLOps provenance; red-team; human-on-the-loop |
| IP claims on fusion (R-C-04) | Medium | FTO; defensive patents |
| CMMC L3 failure (R-C-02) | Medium | ₹14.25 Cr annual compliance programme |
| Attach under-delivery | High impact | Bundle mandates in HW playbooks |
| Services creep diluting GM | Medium | Keep pro services out of V6 COGS narrative |

**Open diligence — critical**

1. **Y1 ship vs Y1 recognize:** Workbook Y1 recognized **₹0** / Y2 **₹9 Cr**; narrative sometimes shows Y1 V6 ~₹13 Cr. Prefer workbook; confirm IC tables.
2. **Y1 company revenue ₹105 Cr (workbook) vs ~₹53 Cr narrative** — V6 narrative mix (~25% of ₹53) is inconsistent with backlog engine; reconcile company-level first.
3. OIDSS renewal rates / multi-year licence duration **not separately modelled** beyond unit × ASP — treat retention as operating assumption.
4. Attach-rate evidence (contractual bundle language vs hope).

---

## 9. Ask & returns framing

Investors with V6 exposure buy **software economics and switching costs** that lift the entire platform’s terminal margins. Absolute revenue is smaller than hardware lines; contribution to equity story is disproportionate.

**Gates:** Y1 supporting ship; Y2 first recognition; GM ≥93%; attach rising to standard by Y5; CMMC on track; AI-B renewals healthy; export licences from Y2 with V2 packs. Under-delivery on attach is the primary thesis risk — more than TAM competition with Palantir.

---

## 10. Appendix — sources

- `Defense_Platform_Business_Plan_Financial_V2.xlsx` — `V6_MilAI`, `Revenue`, `Backlog`, `Platform`, `KPIs`
- `business-models/business-model-military-ai.md`
- `investor_plan/01_executive_summary.md`, `02_market_opportunity.md`, `04_financial_model.md`, `05_funding_and_capital.md`, `08_risk_register.md`
