# Nitrodynamics - Stress-Test Appendix

## Scenario S1 - Platform Reuse Underperformance

**Lever:** Assumptions!C26 reuse multiplier from base **1.0 → 0.8 (S1a) → 0.7 (S1b)**.

**Mechanism:** Lowers effective reuse strength in Platform rows 21–25, raises vertical NRE in ReuseMatrix Section C, increases R&D/NRE expense in R&D\_NRE row 12, compresses GM via the engineering-in-COGS line.

### Driver-level impact

| Metric | Base (1.0x) | S1a (0.8x) | S1b (0.7x) |
| - | - | - | - |
| Y10 effective reuse strength (RF, weighted) | 0.97–0.99 | 0.78–0.79 | 0.68–0.69 |
| Y1 effective reuse strength (blended) | 0.25–0.60 | 0.20–0.48 | 0.17–0.42 |
| Cumulative NRE avoided (10-yr) | Rs. 994 Cr | ~Rs. 795 Cr *(est.)* | ~Rs. 696 Cr *(est.)* |
| Additional cumulative R&D expense vs. base | - | ~Rs. 199 Cr *(est.)* | ~Rs. 298 Cr *(est.)* |


### Financial cascade *(estimated)*

| Line | Base | S1a (0.8x) | S1b (0.7x) |
| - | - | - | - |
| Y10 GM% | 67% | ~64–65% | ~62–63% |
| Y10 EBITDA margin | 46.4% | ~43–44% | ~41–42% |
| Y10 EBITDA (Rs. Cr) | 2,347 | ~2,170 | ~2,050 |
| Cumulative EBITDA 10-yr | 8,100 | ~7,650 | ~7,350 |
| Cumulative FCF 10-yr | 4,803 | ~4,470 | ~4,250 |
| First EBITDA-positive year | Y4 | **Y4** (just) | **Y5** (slips one year) |
| First FCF-positive year | Y4 | Y4 | **Y5** |
| Peak cumulative cash deficit | (1,062) | ~(1,140) | ~(1,210) |
| NPV @ 18% WACC | 747 | ~620 | ~510 |
| Project IRR | 31.9% | ~28% | ~25% |


**Funding implication:**

- **S1a:** Plan absorbs within existing Rs. 1,300 Cr funding capacity; cushion drops from Rs. 138 Cr to ~Rs. 60 Cr above min-cash.

- **S1b:** Plan breaches min-cash in Y4–Y5. Requires either (a) ~Rs. 100–125 Cr additional equity in Y3, or (b) extending the venture debt tranche to Rs. 275 Cr peak.

**Diligence flag:** Treat **S1a as the planning case** and S1b as a covenant trigger. Quarterly board-pack reporting should include actualised reuse strength per module (M1–M5) against the maturity curve in Platform rows 15–19.

## Scenario S2 - DSO Slippage (MoD payment-cycle stress)

**Lever:** Assumptions DSO from base **180 days → 210 days (S2a) → 240 days (S2b)**.

**Mechanism:** AR = Revenue × DSO/365. Increases NWC absorption in CashFlow; no P&L impact except a marginal BG-fee increase on higher ABG outstanding.

### Year-by-year incremental AR absorption (Rs. Cr)

| Year | Revenue | ΔAR @ 210 DSO | ΔAR @ 240 DSO | Cumulative cash drag (210) | Cumulative cash drag (240) |
| - | - | - | - | - | - |
| Y1 | 53 | 4 | 9 | 4 | 9 |
| Y2 | 203 | 17 | 33 | 21 | 42 |
| Y3 | 491 | 40 | 81 | **61** | **123** |
| Y4 | 855 | 70 | 141 | 131 | 264 |
| Y5 | 1,448 | 119 | 238 | 250 | 502 |
| Y10 | 5,055 | 416 | 832 | (peak NWC, see below) |  |


### Financial cascade *(estimated)*

| Line | Base | S2a (210 DSO) | S2b (240 DSO) |
| - | - | - | - |
| Y10 AR balance | ~2,492 | ~2,908 | ~3,324 |
| Y10 Net NWC (post-advance) | ~2,370 | ~2,790 | ~3,200 |
| Peak cumulative cash deficit (Y3) | (1,062) | **(1,123)** | **(1,185)** |
| Funding capacity through Y3 (equity Rs. 1,100 + debt Rs. 200) | 1,300 | 1,300 | 1,300 |
| Cushion above Rs. 100 Cr min-cash | 138 | 77 | **15** |
| Cumulative FCF 10-yr (Y10 NWC tied up) | 4,803 | ~4,387 | ~3,971 |
| NPV @ 18% WACC | 747 | ~688 | ~588 |
| Project IRR | 31.9% | ~30.4% | ~28.5% |


**Funding implication:**

- **S2a (210 DSO):** Plan absorbs with thin cushion. Recommend a Rs. 50 Cr standby line.

- **S2b (240 DSO):** Cushion below min-cash buffer in Y3–Y4. Recommend Rs. 100 Cr standby commitment, drawable on a covenant trigger (e.g., trailing-12-month actualised DSO \> 210 days).

## Combined Adverse Case (S1b + S2b)

**Compounding effect:** S2 hits **cash**; S1 hits **profit**. The two are largely additive.

| Line | Base | Combined (0.7x reuse + 240 DSO) *(est.)* |
| - | - | :-: |
| Peak cumulative cash deficit | (1,062) | ~(1,330) |
| Funding capacity (equity + debt) | 1,300 | 1,300 |
| Shortfall vs. capacity + min-cash | - | ~Rs. 130 Cr |
| NPV @ 18% WACC | 747 | ~350–400 |
| Project IRR | 31.9% | ~22–23% |
| First FCF-positive year | Y4 | Y5–Y6 |


**Combined-case recommendation:** A **Rs. 150 Cr structured standby facility** (equity warrant or convertible) sized for the combined adverse case is the cleanest committee outcome. Plan economics remain intact under both lever stresses; the standby converts the residual scenario into a known cost.


## Recommended Re-Runs in the Workbook Itself

Before final term-sheet, execute the following sensitivity grid directly in the model and replace the *(estimated)* lines above with cell-derived values:

| Re-run | Lever | Values |
| - | - | - |
| 1 | Assumptions!C26 reuse multiplier | 1.0, 0.8, 0.7 |
| 2 | Assumptions DSO | 180, 210, 240 |
| 3 | Combined | 0.7x reuse AND 240 DSO simultaneously |
| 4 | Assumptions BoM floor | 70%, 75%, 80% |
| 5 | Backlog Pwin scalar | 1.0x, 0.8x, 0.6x of plan |
| 6 | Capex profile | +25% in Y3–Y5 |
| 7 | Funding debt cost | 8%, 11%, 14% |


For each re-run, capture: Y10 GM, EBITDA, NPV, IRR, peak cumulative deficit, first FCF-positive year, and cushion vs. min-cash.


*Cross-references: one-page summary in IC\_Summary\_OnePager.md; row-level verification protocol in Diligence\_Audit\_Checklist.md.*

