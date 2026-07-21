# Business Model — V1 AESA Radar

**Product code:** V1 · **Sheet:** `V1_AESA` · **Domain:** Air / Land / Sea (RF) · **First ship:** Year 2  
**Parent plan:** Nitrodynamics Defense Platform · Sources: `03_strategy_and_products.md` §D; `V1_AESA`; `Revenue` / `Backlog`

---

## 1. Overview & value proposition

Active Electronically Scanned Array (AESA) radars in three theatre variants, built on the shared M1 Radio/Microwave and M2 Signal Processing platform rather than as a standalone greenfield radar programme. The line reuses RF and DSP work already productised on the ESM (V2) front-end, compressing time-to-field versus legacy 5–7 year radar programmes.

**Value proposition:** Indigenous, MOSA-aligned multi-band AESA at mid-tier programme economics — performance competitive with imported tier-1 solutions, priced and delivered for Indian MoD and allied FMS-equivalent buyers who cannot profitably be served by global primes on sub-USD 500M lifetime programmes.

---

## 2. Problem solved

- India imports or jointly produces most AESAs; MoD direction is to replace imports where performance allows (Uttam AESA as indigenous reference).
- Tier-1 primes carry overhead that makes mid-tier AESA awards structurally unattractive.
- Service-specific radar needs (fighter/drone airborne, ground surveillance, naval multi-function) traditionally force separate NRE programmes; Nitrodynamics amortises one RF/DSP stack across three variants.

---

## 3. Solution & packaging

| Variant | Role | Catalogue ASP (Y1 input) | Y10 ASP (model) | Y10 units |
| ------- | ---- | -----------------------: | --------------: | --------: |
| **A — X-band Airborne** | Fighters & large drones | ₹26 Cr | ~₹21.8 Cr | 80 |
| **B — S-band Ground Surveillance** | Land surveillance | ₹45 Cr | ~₹37.6 Cr | 8 |
| **C — X-band Naval Multi-function** | Warships | ₹36 Cr | ~₹30.1 Cr | 7 |
| **V1 total** | | | | **95** |

*Source: `V1_AESA` rows 6–33. ASP/BoM decline via Wright’s-Law learning (Assumptions: 0.92 per doubling, floored at 70% of starting BoM).*

**Platform modules consumed:** M1, M2, M3 (primary); M4 for mission-computer integration.

**Packaging:** Hardware system sale + attached V6 Military AI (edge box / fusion middleware) on most awards. Qualification under MIL-STD-810/461/704/1275; MOSA/FACE open architecture for FMS-eligible variants.

---

## 4. Customer segments / buyers

| Segment | Primary variants | Notes |
| ------- | ---------------- | ----- |
| Indian Air Force | A (airborne) | Lead buyer for airborne AESA on fighters/drones |
| Indian Army | B (S-band ground) | Ground surveillance programmes |
| Indian Navy | C (naval X-band) | Ship multi-function radar |
| Allied governments (Y2+) | ITAR-clean / EAR99 variants | FMS-equivalent + DCS |

**Comparables:** Northrop Grumman, Raytheon, Leonardo, Saab, Thales, Indra; DRDO-LRDE Uttam as indigenous reference.

---

## 5. Revenue model & pricing logic

- **Model:** Fixed-price / programme hardware sales; bookings lead recognition by ~12–18 months.
- **Recognition:** 50% of opening backlog delivered each year (`Backlog!D82:M82`).
- **Pricing:** Catalogue ASP with volume/learning decline; BoM starts ~⅓–⅔ of ASP depending on variant (e.g. Variant A Y1 BoM ₹11 Cr on ₹26 Cr ASP).
- **Pwin:** Ramps ~0.25–0.35 as qualification base accumulates (`Backlog` Pwin row for V1).

### Recognized revenue (₹ Cr) — `Revenue!D6:M6`

| Y1 | Y2 | Y3 | Y4 | Y5 | Y10 |
| --: | --: | --: | --: | --: | --: |
| 0 | 50 | 125 | 206 | 328 | **865** |

Y10 mix ≈ **17%** of consolidated revenue. Closing backlog Y10 ≈ ₹1,877 Cr (`Backlog!M29`).

### Supporting unit economics (memo only) — `V1_AESA`

| Metric | Y2 | Y5 | Y10 |
| ------ | --: | --: | --: |
| Supporting revenue | 262 | 1,340 | 2,252 |
| Units | 10 | 57 | 95 |
| Gross margin % (BoM only) | ~62% | ~65% | ~65% |

---

## 6. Cost structure & key drivers

| Driver | Detail | Source |
| ------ | ------ | ------ |
| **BoM** | GaN T/R modules, beamforming, antennas, FPGA pipelines | `V1_AESA` BoM rows; Assumptions learning 0.92 / floor 70% |
| **NRE / qualification** | 30% NRE contingency uplift on AESA in model | Risk register R-F-04; Assumptions |
| **Platform share** | Amortised M1–M3 NRE (not charged full per-programme) | `Platform`, `ReuseMatrix` |
| **Manufacturing** | 30–40% unit volume via contract manufacturers | `07_operating_model.md` |
| **Warranty** | 2% of COGS (company-wide) | Assumptions |
| **Mfg overhead** | 20% of direct material + labour | Assumptions |

Y10 recognized BoM COGS ≈ ₹302 Cr on ₹865 Cr revenue → **~65% GM before personnel COGS** (`Revenue!M23` / `M6`).

---

## 7. Go-to-market / channels

1. **MoD capture** — bid against Uttam-adjacent and import-replacement AESA RFPs; service-specific capture leads (IAF / Army / Navy).
2. **Marquee win Y3–Y5** — one reference programme to unlock follow-on blocks.
3. **Export from Y2** — ITAR-clean variants via GoI FMS-equivalent and DCS into South Asia, SE Asia, Middle East, Africa.
4. **Bundle** — AESA + V2 ESM + V6 AI as integrated sensor suite where tenders allow.

---

## 8. Key partners & resources

- **Platform Engineering** — M1 GaN T/R, M2 digital beamforming, M3 EMI/EMC & environmental qualification.
- **Anechoic / EMI labs** — partner labs Y1–Y2; owned facilities from Y3.
- **GaN supply** — second-source by Y3; partial in-house packaging from Y2 (mitigates R-SC-01).
- **Cleared RF/DSP engineers** — scarce resource (R-T-01).
- **Contract manufacturers** — AS9100-cleared panel for volume builds.

---

## 9. Competitive differentiation

| vs Tier-1 primes | Matches multi-domain RF depth; wins on cycle time, cost-to-deliver, capital efficiency |
| vs RF specialists | Same RF depth **plus** multi-domain integration and AI attach |
| vs Pure-plays | Only platform firm that can bid AESA inside bundled EW / C-UAS / AI awards |

Scorecard: Radio/AESA capability **4/4** (`MarketPositioning` / strategy competitive matrix).

---

## 10. Unit economics & financial highlights

- Global TAM USD 5–7 bn / yr, 7–9% CAGR; Nitrodynamics Y10 share = low single-digit % of global (`02_market_opportunity.md`).
- First demo / deliveries Y2; volume scale to **~95 units/yr by Y10** (`V1_AESA!M33`).
- Bookings Y1 ₹100 Cr → Y10 ~₹1,012 Cr (`Backlog!D20:M20`).
- **Assumption (flagged):** Investor narrative sometimes quotes Y10 AESA revenue ~₹1,080 Cr blended; workbook **recognized** Y10 is ₹865 Cr — use workbook for diligence; V-sheet supporting ₹2,252 Cr is *not* consolidated revenue.

---

## 11. Risks & assumptions

| Risk | Residual | Mitigation |
| ---- | -------- | ---------- |
| TRL / T/R yield / thermal margins slip (R-P-03) | Medium | Module-level M1/M2 qual before integration; DoE on TRM yield |
| GaN single-source (R-SC-01) | Medium | Second source Y3; in-house packaging Y2+ |
| FX on imported RF/FPGA (R-M-01) | Medium | Forward cover; export hedge Y4+ |
| Hardware qualification retest (R-P-01) | Medium | MVP-first; 30% NRE contingency |

**Key assumptions:** Learning curve holds at 0.92; Pwin ≥ ~0.30 from mid-horizon; MoD import-replacement policy persists; delivery rate remains 50% of opening backlog.

---

## 12. Success metrics / KPIs

| KPI | Target / signal |
| --- | --------------- |
| First production delivery | Y2 |
| Cumulative units through Y5 | ≥ ~50 (`V1` unit ramp) |
| Recognized revenue Y5 / Y10 | ~₹328 / ~₹865 Cr |
| BoM-only GM | ≥ ~62% from Y2; ~65% terminal |
| Book-to-bill | Starts ~1.5, tapers toward 1.0 |
| Marquee programme win | ≥ 1 by Y5 |
| Export share of V1 bookings | Material from mid-horizon |
| Platform reuse on new AESA variant | → ~99% by Y10 |
