# Business Model — V2 Electronic Warfare & SIGINT

**Product code:** V2 · **Sheet:** `V2_EW_SIGINT` · **Domain:** Air / Land / Sea (RF + DSP) · **First ship:** Year 1  
**Parent plan:** Nitrodynamics Defense Platform · Sources: `03_strategy_and_products.md` §D; `V2_EW_SIGINT`; `Backlog` / `Revenue`

---

## 1. Overview & value proposition

The **Day-1 cash engine** of the platform. Electronic Support Measures (ESM), ELINT, tactical anti-drone jamming, and strategic ground SIGINT — already partly developed at plan start, with industrialisation and scale-up as the Y1 focus rather than invention.

**Value proposition:** GSQR-aligned indigenous EW/SIGINT with a firm iDEX production MoQ, then catalogue expansion across four variants that feed RF/DSP maturity into every later vertical (AESA, C-UAS, UAS-C payload).

---

## 2. Problem solved

- Indian EW procurement spans Army (Samyukta, Himshakti), Navy (Sangraha, Varuna), and IAF pod-based EW — historically import-heavy and slow.
- Border and maritime threat environments demand concurrent naval, aerial, tactical, and strategic SIGINT capability without four independent NRE programmes.
- Need for a production-ready indigenous ESM line that can fund the rest of the platform while still immature.

---

## 3. Solution & packaging

| Variant | Role | Catalogue ASP (Y1) | Y10 ASP (model) | Y10 units |
| ------- | ---- | -----------------: | --------------: | --------: |
| **EW-A** Naval ESM/ELINT suite | Warships | ₹30 Cr | ~₹25.1 Cr | 15 |
| **EW-B** Aerial ESM pod | Aircraft / large UAVs | ₹35 Cr | ~₹29.3 Cr | 20 |
| **EW-C** Tactical anti-drone jammer | High-volume tactical | ₹2.0 Cr | ~₹1.67 Cr | 80 |
| **EW-D** Ground SIGINT station | Strategic fixed site | ₹114 Cr | ~₹95.4 Cr | 8 |
| **V2 total** | | | | **123** |

*Source: `V2_EW_SIGINT` rows 6–41.*

### iDEX ESM MoQ (anchor contract)

| Item | Value | Source |
| ---- | ----- | ------ |
| Systems | 10 | `V2_EW_SIGINT!C48` |
| Concessional price / system | **₹21 Cr** | C49 |
| MoQ total | **₹210 Cr** | C50 |
| Phase 1 (Y1, 5 systems) | ₹105 Cr | C51 |
| Phase 2 (Y2, 5 systems) | ₹105 Cr | C52 |
| Concession vs EW-A catalogue | ~30% | C54 |

> **OQ / diligence note (from plan):** Whether ₹21 Cr is iDEX first-production pricing on the same SKU as EW-A/B or a lower-spec configuration is **unconfirmed** (tracked as OQ-C in `project-context.md`). MoQ / Day-1 traction figures use ₹21 Cr; catalogue ranges apply to forward commercial volume.

**Platform modules:** M1, M2 (primary); M3 qualification; M4 mission SW.

---

## 4. Customer segments / buyers

| Segment | Variants | Notes |
| ------- | -------- | ----- |
| Indian Navy | EW-A | Sangraha / Varuna-class ESM demand |
| Indian Air Force | EW-B | Pod / UAV ESM |
| Indian Army | EW-C, EW-D | Tactical jammer + strategic SIGINT |
| Paramilitary / critical infra | EW-C | Overlap with C-UAS soft-kill |
| Allied export (Y2+) | ITAR-clean EW packs | Early export channel with V6 |

**Comparables:** Saab, Elbit (integrated EW); broader EW specialist field.

---

## 5. Revenue model & pricing logic

- **Model:** Hardware programme sales; MoQ at concessional ₹21 Cr/system; commercial catalogue thereafter.
- **Recognition:** 50% of opening backlog per year (`Backlog!D83`).
- **Y1 opening backlog:** ₹210 Cr (full MoQ booked into opening) → Y1 deliveries **₹105 Cr** (`Backlog!D76`, `D90`).
- **Pwin:** Held ~0.40 across horizon — customer-relationship premium from incumbent MoQ (`Backlog` V2 Pwin; workbook explanation).

### Recognized revenue (₹ Cr) — `Revenue!D7:M7`

| Y1 | Y2 | Y3 | Y4 | Y5 | Y10 |
| --: | --: | --: | --: | --: | --: |
| **105** | 118 | 252 | 331 | 428 | **760** |

Y1 = **100%** of consolidated recognized revenue; Y10 mix ≈ **15%**. Closing backlog Y10 ≈ ₹1,590 Cr.

### Supporting unit economics — `V2_EW_SIGINT`

| Metric | Y1 | Y5 | Y10 |
| ------ | --: | --: | --: |
| Supporting revenue | 167 | 1,014 | 1,859 |
| Units | 11 | 64 | 123 |
| Gross margin % (BoM) | ~55% | ~61% | ~61% |

---

## 6. Cost structure & key drivers

| Driver | Detail |
| ------ | ------ |
| BoM | RF front-end, DSP/FPGA, antennas, jammer RF chains, SIGINT station infrastructure |
| Learning | 0.92 Wright factor / 70% BoM floor — EW-C hits floor early on volume |
| Industrialisation | Y1 spend is production stand-up, not greenfield invention |
| Shared platform | ESM RF/DSP becomes the reuse base for V1 and V3 |
| BG / working capital | Advances 15%; DSO 180 days; PBG 3% of backlog — material for this cash-engine line |

Y10 recognized BoM COGS ≈ ₹295 Cr on ₹760 Cr → **~61% GM (BoM only)**.

---

## 7. Go-to-market / channels

1. **Deliver MoQ** — Phase 1 Y1 / Phase 2 Y2 against iDEX production order (production revenue, not grant).
2. **Follow-on MoD blocks** — Navy ESM, Army EW, IAF pods using MoQ as reference account.
3. **Catalogue upsell** — EW-C volume and EW-D strategic stations after ESM credibility.
4. **Export** — early FMS-equivalent EW packages from Y2 (paired with V6).

---

## 8. Key partners & resources

- Existing iDEX / MoD programme relationship and drawings/spares posture from MoQ.
- M1/M2 platform teams (same RF stack feeds AESA).
- Partner EMI/EMC and outdoor ranges Y1–Y2.
- Cleared EW systems engineers and field integration teams.
- BG banking panel (cash collateral heavy in Y1–Y2).

---

## 9. Competitive differentiation

- Only line with **Day-1 contracted production backlog**.
- Integrated EW + SIGINT + tactical jammer family on one RF/DSP platform (pure-plays rarely span all four).
- Incumbency Pwin (~40%) vs new-entrant AESA/C-UAS (~25–35%).
- Feeds platform flywheel: every ESM shipment matures modules that lower NRE for V1/V3.

---

## 10. Unit economics & financial highlights

- Global EW TAM USD 22–25 bn / yr, 6–8% CAGR; Nitrodynamics seeks India mid-tier leadership, sub-1% global (`02_market_opportunity.md`).
- Bookings Y1 ₹341 Cr (71% of Y1 consolidated bookings) → Y10 ~₹830 Cr (`Backlog!D21:M21`).
- Highest early cash contribution; funds concurrent development of V1, V3–V5.
- **Narrative vs workbook:** Some investor-plan tables show Y1 company revenue ~₹53 Cr with V2 ~₹40 Cr — **workbook recognizes ₹105 Cr V2 in Y1**. Prefer workbook for financial diligence; treat ~₹53 as an alternate narrative snapshot.

---

## 11. Risks & assumptions

| Risk | Residual | Mitigation |
| ---- | -------- | ---------- |
| MoD DSO / cash conversion (R-F-01) | Medium-High | 15% advances; milestone billing; WC facilities |
| Qualification slip on remaining variants (R-P-01) | Medium | MVP-first; partner lab slots |
| GaN / FPGA supply (R-SC-01/02) | Medium | Dual-source roadmap |
| MoQ SKU vs catalogue ambiguity (OQ-C) | Diligence | Confirm configuration parity with customer |

**Key assumptions:** MoQ phases complete on schedule; Pwin stays ~0.40; commercial ASPs hold after concessional MoQ; 50% backlog burn rate remains valid.

---

## 12. Success metrics / KPIs

| KPI | Target / signal |
| --- | --------------- |
| MoQ Phase 1 / Phase 2 delivery | ₹105 Cr each in Y1 / Y2 |
| Y1 recognized revenue | ₹105 Cr (workbook) |
| Units Y10 | ~123 across four variants |
| GM (BoM) | Mid-50s → ~61% |
| Book-to-bill | Near 1.0–1.1 early; ~1.0 mature |
| Follow-on awards beyond MoQ | Visible in Y2–Y3 bookings |
| Module maturity contributed to V1/V3 | Reuse strength climb on M1/M2 |
