# Business Model — V6 Military AI Systems

**Product code:** V6 · **Sheet:** `V6_MilAI` · **Domain:** Cross-domain (AI / SW) · **Launch:** Year 1 (shipping) · **First recognized revenue (workbook):** Year 2  
**Parent plan:** Nitrodynamics Defense Platform · Sources: `03_strategy_and_products.md` §D; `V6_MilAI`; `Revenue` / `Backlog`

---

## 1. Overview & value proposition

Software-led product family on a software-defined release cadence: edge AI mission boxes, OIDSS decision-support licences, and sensor-fusion middleware. **Highest gross margins** in the portfolio (~93–94%) and the strategic lock-in layer — attached to every AESA, ESM, C-UAS, UAS, and AUV/USV sale.

**Value proposition:** Defense AI that ships *with* Nitrodynamics hardware (not as an orphaned SaaS competing with Palantir alone), raising attach rates and blended company GM while creating switching costs across the installed base.

---

## 2. Problem solved

- Hardware primes ship sensors without a coherent fusion / decision layer; AI startups ship software without the platforms their models run on.
- Operators need edge inference on disconnected platforms **and** enterprise OIDSS at HQ — rarely from one vendor under Indian clearance constraints.
- Blended defense-prime margins stay low without a software mix shift; V6 is the explicit mix lever to ~67% company GM / ~46% EBITDA by Y10.

---

## 3. Solution & packaging

| Variant | Role | Pricing model | ASP Y1 | Y10 ASP | Y10 units / licences |
| ------- | ---- | ------------- | -----: | ------: | -------------------: |
| **AI-A** Edge AI mission box | Bolt-on compute for platforms | Hardware-ish edge appliance | ₹3.8 Cr | ~₹3.18 Cr | 55 |
| **AI-B** OIDSS | Operational intelligence & decision support | **Annual licence** | ₹11.4 Cr / yr | ~₹9.54 Cr | 35 |
| **AI-C** Sensor-fusion middleware | Lattice-like fusion layer | Licence | ₹5.7 Cr | ~₹4.77 Cr | 52 |
| **V6 total** | | | | | **142** |

*Source: `V6_MilAI` rows 6–33. Sheet description: “Edge AI box + Cloud SaaS analytics + sensor-fusion middleware.”*

**Platform module:** M5 AI/ML is both the product engine and a shared module consumed by V3–V5 autonomy/fusion.

**Packaging:** Standalone licences **or** attach SKUs on V1–V5 contracts; MOSA/FACE-aligned interfaces; CMMC L3 cybersecurity posture for FMS readiness.

---

## 4. Customer segments / buyers

| Segment | Variants | Notes |
| ------- | -------- | ----- |
| All Indian services | A, B, C | Attach to hardware buys; OIDSS for HQs |
| Paramilitary / infra | A, C | C-UAS fusion |
| Allied governments | B, C (EAR99/ITAR-clean) | Early export with V2 |
| Internal pull-through | All | Every Nitrodynamics hardware programme |

**Comparables:** Palantir (OIDSS analogue; ~USD 0.7–0.8 bn DoD run-rate reference), Anduril Lattice (fusion), Shield AI (autonomy valuations).

---

## 5. Revenue model & pricing logic

- **Models:** (1) Edge appliance sale (AI-A); (2) recurring annual OIDSS licence (AI-B); (3) middleware licence (AI-C).
- **Recognition lag:** SW 3–12 months; AI-A 6–9 months hardware-style (`04_financial_model.md`). Workbook uses **25%** of opening backlog / year (`Backlog!D87`).
- **Pwin:** ~0.30–0.35.
- **Workbook timing gap:** V-sheet shows Y1 supporting revenue ₹30.4 Cr (5 units); Backlog Y1 opening for V6 = 0 → **Y1 recognized = ₹0**; first recognition Y2 ₹9.12 Cr. Strategy narrative says V6 “ships” Y1 — operationally true on the unit plan; P&L recognition lags one year in the backlog engine.

### Recognized revenue (₹ Cr) — `Revenue!D11:M11`

| Y1 | Y2 | Y3 | Y4 | Y5 | Y10 |
| --: | --: | --: | --: | --: | --: |
| 0 | 9 | 24 | 50 | 95 | **458** |

Y10 mix ≈ **9%** of revenue but **disproportionate GM contribution**. Closing backlog Y10 ≈ ₹2,130 Cr.

### Supporting unit economics — `V6_MilAI`

| Metric | Y1 | Y5 | Y10 |
| ------ | --: | --: | --: |
| Supporting revenue | 30.4 | 299 | 757 |
| Units / licences | 5 | 59 | 142 |
| Gross margin % | **93.1%** | **94.1%** | **94.4%** |

---

## 6. Cost structure & key drivers

| Driver | Detail |
| ------ | ------ |
| BoM | Low — AI-A compute/enclosure; AI-B/C near-pure software (BoM ₹0.19–0.48 Cr Y1 inputs) |
| MLOps / model training | M5 platform NRE (~₹160 Cr of ₹575 Cr platform total over 10 yrs) |
| Cloud / secure hosting | For OIDSS (not fully itemised per-vertical in V-sheet) |
| Compliance | Share of CMMC L3 ₹14.25 Cr / yr company compliance stack |
| Talent | Cleared ML + embedded AI engineers |

Y10 recognized BoM COGS ≈ ₹26 Cr on ₹458 Cr → **~94% GM (BoM only)**.

---

## 7. Go-to-market / channels

1. **Attach-first** — standard line item on V1–V5 proposals (primary motion).
2. **Land-and-expand OIDSS** — AI-B annual renewals; expand seats / theatres.
3. **Early ship with V2** — Y1 industrial narrative; export AI with EW packs from Y2.
4. **Software release cadence** — quarterly iteration vs multi-year hardware blocks.
5. **Middleware lock-in** — once AI-C fuses a customer’s sensor fleet, hardware displacement cost rises.

---

## 8. Key partners & resources

- M5 AI/ML module team (CV, fusion, autonomy, MLOps).
- Hardware product squads (attach channel).
- Secure cloud / on-prem OEM partners for OIDSS deployments.
- Academic partnerships for early tech signal (`07_operating_model.md`).
- CISO / CMMC programme (trust prerequisite for FMS AI).

---

## 9. Competitive differentiation

| vs Defense AI startups | Ships the hardware the AI runs on → higher attach, lower displacement |
| vs Tier-1 primes | Software/AI mix score 4 vs ~2; faster release cadence |
| vs Palantir-class | Narrower horizontal analytics; deeper vertical integration with owned sensors |

Company scorecard: Military AI / sensor fusion **4/4**; Software/AI revenue mix **4/4**.

---

## 10. Unit economics & financial highlights

- Defense AI TAM USD 8–12 bn today, ~3× by 2030, 20%+ CAGR.
- Bookings Y1 ₹36.5 Cr → Y10 ₹757 Cr (`Backlog!D25:M25`) — bookings track supporting revenue late-horizon.
- Mix only ~9–10% of Y10 revenue but drives ~250–300 bps of blended GM lift (`04_financial_model.md`).
- Strategic KPI is **attach rate**, not standalone TAM share.

**Assumptions flagged:**

1. Y1 ship vs Y1 recognize discrepancy (see §5).
2. Investor tables sometimes show Y1 V6 ~₹13 Cr recognized — workbook shows ₹0 Y1 / ₹9 Cr Y2.
3. OIDSS renewal rates and multi-year licence duration are **not** separately modelled beyond unit × ASP on the V-sheet — treat retention as an operating assumption.

---

## 11. Risks & assumptions

| Risk | Residual | Mitigation |
| ---- | -------- | ---------- |
| AI model poisoning / adversarial inputs (R-CY-03) | Medium | MLOps provenance; red-team; human-on-the-loop |
| IP claims on fusion algorithms (R-C-04) | Medium | FTO analysis; defensive patents |
| CMMC L3 failure (R-C-02) | Medium | ₹14.25 Cr annual compliance programme |
| Attach under-delivery | High impact | Bundle mandates in hardware capture playbooks |
| Software GM dilution if services creep | Medium | Keep professional services out of V6 COGS narrative |

**Key assumptions:** 93–94% GM sustained; attach on majority of hardware awards; 25% backlog recognition; OIDSS renewals implicit in unit ramp.

---

## 12. Success metrics / KPIs

| KPI | Target / signal |
| --- | --------------- |
| Supporting shipments Y1 | 5 units / licences (V-sheet) |
| First recognized revenue | Y2 (workbook) |
| GM (BoM) | ≥ 93% every year |
| Recognized revenue Y5 / Y10 | ~₹95 / ~₹458 Cr |
| Attach rate on V1–V5 awards | Rising to “standard” by Y5 |
| AI-B renewals | High single-digit to mid retention (ops assumption) |
| Contribution to blended company GM | ~250–300 bps by Y10 |
| Export AI licences | From Y2 with V2 packs |
