# Business Model — V5 Autonomous Systems (AUV / USV)

**Product code:** V5 · **Sheet:** `V5_Autonomous` · **Domain:** Sea (SysEng + SW + AI) · **First ship:** Year 3  
**Parent plan:** Nitrodynamics Defense Platform · Sources: `03_strategy_and_products.md` §D; `V5_Autonomous`; `Revenue` / `Backlog`

---

## 1. Overview & value proposition

Autonomous Underwater Vehicles (mine-hunting / survey and large ASW) and mid-size Unmanned Surface Vessels (ISR / C-UAS host). Autonomy software is shared with V6; **hulls iterate through partner shipyards**, keeping the line asset-light versus building a full naval yard.

**Value proposition:** Software-defined maritime autonomy on partner hulls — Indian Navy mine-countermeasures and seabed warfare demand without the capex profile of a traditional naval OEM.

---

## 2. Problem solved

- Unmanned maritime is the “next wave” after aerial drones (USN Task Force 59, Australia Ghost Shark, Ukrainian Magura USV precedent).
- Indian Navy needs AUVs for MCM / seabed warfare (Project 75 follow-on context; NSTL Vizag indigenous AUV programmes).
- Specialists lead on hull hydrodynamics but score poorly on multi-domain sensors and AI fusion that increasingly decide autonomy performance.

---

## 3. Solution & packaging

| Variant | Role | ASP Y1 input | Y10 ASP | Y10 units |
| ------- | ---- | -----------: | ------: | --------: |
| **AUV-A** Small AUV | Mine-hunting / seabed survey | ₹15 Cr | ~₹12.5 Cr | 32 |
| **AUV-B** Large ASW AUV | Anti-submarine | ₹60 Cr | ~₹51.2 Cr | 4 |
| **USV-A** Mid-size USV | ISR / C-UAS host platform | ₹45 Cr | ~₹37.6 Cr | 15 |
| **V5 total** | | | | **51** |

*Source: `V5_Autonomous` rows 6–33. AUV-A + USV-A from Y3; AUV-B from Y5.*

**Platform modules:** M3, M4, M5 (primary); sensors may pull M1/M2; autonomy shared with V6.

**Packaging:** Vehicle + autonomy stack + C2; optional V3 C-UAS payload on USV-A; V6 edge AI / fusion licences.

---

## 4. Customer segments / buyers

| Segment | Variants | Notes |
| ------- | -------- | ----- |
| Indian Navy | AUV-A/B, USV-A | Primary buyer — MCM, ASW, harbour ISR |
| Indian Army (limited) | Small AUV | Inland water / riverine edge cases |
| Allied navies (export) | All | Middle East / Indo-Pacific unmanned maritime interest |
| Critical ports | USV-A | Harbour surveillance / C-UAS host |

**Comparables:** Anduril Dive-LD / Ghost Shark, L3Harris, Saab Sea Wasp / AUV62, Kongsberg.

---

## 5. Revenue model & pricing logic

- **Model:** Hardware platform sales with high software content; partner-built hulls.
- **Recognition:** **25%** of opening backlog / year — slowest HW burn (`Backlog!D86`), reflecting long maritime delivery cycles.
- **Pwin:** ~0.22 early → ~0.35.
- First supporting shipments Y3 (2 units); recognized revenue Y3 ₹19 Cr.

### Recognized revenue (₹ Cr) — `Revenue!D10:M10`

| Y1 | Y2 | Y3 | Y4 | Y5 | Y10 |
| --: | --: | --: | --: | --: | --: |
| 0 | 0 | 19 | 50 | 100 | **549** |

Y10 mix ≈ **11%**. Closing backlog Y10 ≈ ₹2,684 Cr.

### Supporting unit economics — `V5_Autonomous`

| Metric | Y3 | Y5 | Y10 |
| ------ | --: | --: | --: |
| Supporting revenue | 60 | 311 | 1,171 |
| Units | 2 | 12 | 51 |
| Gross margin % (BoM) | ~68% | ~71% | ~73% |

Strong hardware GM because autonomy/software content is high and hull BoM is partner-optimised.

---

## 6. Cost structure & key drivers

| Driver | Detail |
| ------ | ------ |
| Hull / mechanical BoM | Partner shipyard COGS; asset-light Nitrodynamics footprint |
| Autonomy / GNC software | Shared with V6 — NRE in M5/M4, not fully on V5 P&L |
| Sensors / energy / acoustic payloads | AUV-B ASW suite is cost spike |
| Maritime test tank | Owned facilities wave Y3+ |
| 30% NRE contingency | Applied to AUV programmes in model |
| Contract manufacturing | 30–40% volume absorption |

Y10 recognized BoM COGS ≈ ₹147 Cr on ₹549 Cr → **~73% GM (BoM only)**.

---

## 7. Go-to-market / channels

1. **Navy-first** — MCM / seabed survey AUV-A as entry; USV as C-UAS/ISR host; AUV-B as flagship ASW.
2. **Wave 3 timing** — ship from Y3 while V4 still in certification (concurrency thesis).
3. **Bundle** — USV-A + V3 C-UAS + V6 autonomy as harbour-defense package.
4. **Export** — allied navies seeking Task Force 59-like mass unmanned presence.
5. **Shipyard partnerships** — rapid hull iteration without owning yards.

---

## 8. Key partners & resources

- Partner shipyards (hull fabrication / iteration).
- M5 autonomy / GNC team (shared with V6).
- Acoustic / sonar payload suppliers for AUV-B.
- Maritime test tank / range (capex from Y3).
- Naval capture lead inside CCO organisation.

---

## 9. Competitive differentiation

| vs AUV specialists | Trails pure maritime depth (3 vs 4) but wins on AI fusion, multi-domain sensors, and C-UAS-host USV |
| vs Tier-1s | Faster unmanned cycles; lower overhead |
| vs Software-only autonomy startups | Ships vehicles + stack, not just licences |

Strategic role: **sea domain completeness** for the four-domain platform thesis (Air / Land / Sea / Cyber).

---

## 10. Unit economics & financial highlights

- Global unmanned maritime TAM USD 2.5–3.5 bn / yr, 12–15% CAGR.
- Bookings Y2 ₹76 Cr → Y10 ~₹1,036 Cr (`Backlog!E24:M24`).
- Y10 supporting ₹1,171 Cr vs recognized ₹549 Cr — 25% delivery rate keeps a large backlog cushion.
- Investor narrative Y10 ~₹575 Cr aligns closely with workbook recognized ~₹549 Cr.

---

## 11. Risks & assumptions

| Risk | Residual | Mitigation |
| ---- | -------- | ---------- |
| Programme cost overrun (R-F-04) | Medium | 30% NRE contingency; partner hull competition |
| CM / shipyard quality (R-SC-04) | Low-Medium | Dual partners by Y4 |
| AI / autonomy safety (R-CY-03, R-R-01) | Medium | Human-on-the-loop for lethal ASW actions |
| Navy budget cyclicality | Medium | Multi-variant + export |

**Key assumptions:** Partner shipyards deliver on schedule; autonomy reuse from V6 works underwater/surface; 25% recognition rate; AUV-B slips do not block AUV-A/USV cash.

---

## 12. Success metrics / KPIs

| KPI | Target / signal |
| --- | --------------- |
| First AUV-A / USV-A delivery | Y3 |
| First AUV-B | Y5 |
| Units Y5 / Y10 | ~12 / ~51 |
| Recognized revenue Y10 | ~₹549 Cr |
| Partner hull cost vs plan | Within contingency |
| Navy reference programme | ≥ 1 marquee by Y5 |
| V6 autonomy attach | Standard on all V5 platforms |
| Export USV/AUV award | Mid-horizon |
