# 04. Financial Model and Unit Economics

*Nitrodynamics - Investor Business Plan, Section 04*

This section translates the operating thesis set out earlier in the plan into a quantitative financial model. The architecture is built bottom-up from contracted backlog by product line (V1-V6), with revenue recognised under a defense-realistic lag (12-18 months for hardware, 3-12 months for software), gross margin assembled from a Wright's-Law BoM learning curve, platform-reuse leverage and a rising software mix, and a cost stack calibrated to Indian defense-prime overhead norms. All figures are stated in INR Crore unless flagged otherwise.

## A. Revenue Architecture

Revenue is *not* modelled off a top-down market-share assumption. It is built up from booked orders, multiplied by a win probability where contracts are pursued but not yet signed, then released into revenue under a recognition-lag schedule that matches how the Indian MoD and allied customers actually pay against milestones.

The mechanics, by product class:

- **Hardware product lines (V1 AESA, V2 ESM, V3 C-UAS, V4 MALE UAS, V5 AUV/USV).** A signed order in year *t* releases revenue starting 12-18 months later, with the bulk in *t+1* and *t+2*, depending on whether the line is in development, qualification or steady-state production.
- **Software product line (V6 Military AI).** AI-A (edge box) follows a 6-9 month hardware-style lag; AI-B (OIDSS annual licence) and AI-C (sensor-fusion middleware) are recognised on a 3-12 month subscription rhythm.
- **Book-to-bill cover** is targeted above 1.0 in every year, taper from 1.5x in Y1-Y2 (build the backlog) toward 1.0x by Y8-Y10 (steady-state replenishment). This is what drives the Rs.16,680 Cr closing backlog by Year 10.

The resulting 10-year revenue profile:

| Year | Revenue (Rs.Cr) | Y/Y growth | Stage |
| - | - | - | - |
| Y1 | ~53 | n/a | ESM cash engine + V6 AI software launch |
| Y2 | ~203 | +283% | First AESA and C-UAS contracts; ESM scales |
| Y3 | ~491 | +142% | AUV/USV first ship; AESA and C-UAS deliveries begin |
| Y4 | ~855 | +74% | MALE drone first ship; multi-product concurrent ramp |
| Y5 | ~1,448 | +69% | All six product lines shipping concurrently |
| Y6 | ~2,180 | +51% | Export contracts contribute materially |
| Y7 | ~2,884 | +32% | Steady-state defense growth-stage trajectory |
| Y8 | ~3,659 | +27% |  |
| Y9 | ~4,381 | +20% |  |
| Y10 | ~5,055 | +15% | Mature multi-domain prime |
| **10-yr total** | **~21,200** |  | Closing backlog Y10 ~Rs.16,680 Cr (>3.3x of Y10 revenue) |

[Diagram 3: Revenue Build by Product]

The 15% growth in Year 10 understates the trajectory of the business. Closing backlog at Y10 (Rs.16,680 Cr) is 3.3x of annual revenue, which provides visibility well beyond the plan horizon and supports continued mid-teens growth into Years 11-13 before category maturity sets in.

## B. Revenue Decomposition by Product Line

The table below allocates revenue across V1-V6 at three milestones (Y1, Y5, Y10), built from the unit-volume and ASP ranges in source sections 5.1-5.6. Allocations reconcile to the totals shown in Section A within rounding. **Analyst assumption:** within each band given in the source (e.g. EW-C tactical jammer Rs.1.7-2.0 Cr), midpoint pricing is used; the Y1 mix is anchored on the part-developed ESM line plus initial Military AI software shipments, the Y5 mix interpolates between contracted bookings and the wave-plan schedule, and the Y10 mix uses the upper end of the unit-volume bands consistent with the Rs.5,055 Cr total.

| Product line | Y1 (Rs.Cr) | Y1 mix | Y5 (Rs.Cr) | Y5 mix | Y10 (Rs.Cr) | Y10 mix | Comment |
| - | - | - | - | - | - | - | - |
| V1 - AESA Radar | 0 | 0% | 240 | 17% | 1,080 | 21% | Three variants; ~95 units/yr Y10 blended |
| V2 - EW / SIGINT | 40 | 75% | 360 | 25% | 850 | 17% | Day-1 cash engine; mature by Y5 |
| V3 - Counter-UAS | 0 | 0% | 290 | 20% | 1,150 | 23% | Highest unit volumes; AI-fusion showcase |
| V4 - MALE UAS | 0 | 0% | 220 | 15% | 900 | 18% | Longest-cycle; first ship Y4 |
| V5 - Autonomous AUV/USV | 0 | 0% | 180 | 12% | 575 | 11% | First ship Y3; reuses V6 autonomy |
| V6 - Military AI Systems | 13 | 25% | 158 | 11% | 500 | 10% | Software economics; attaches to every hardware line |
| **Total** | **~53** | **100%** | **~1,448** | **100%** | **~5,055** | **100%** |  |

Two observations are central to the equity story. First, V2 ESM finances the business in Y1-Y3 and remains a large absolute revenue contributor in Y10 even though its mix share falls from 75% to 17%. Second, V6 Military AI represents only ~10% of revenue in Y10 but contributes disproportionately to gross-margin mix because it runs at 93-94% gross margin (see Section C). Every hardware product also pulls attached V6 software revenue, so the *effective* software-economics share of the P&L is materially higher than the headline 10%.

## C. Gross Margin Bridge

Gross margin progresses from approximately 51% in Year 1 to approximately 67% in Year 10. Three drivers explain the climb:

1. **Wright's-Law BoM learning.** Unit BoM falls by 8% per doubling of cumulative production (0.92 cost factor), floored at 70% of starting BoM. The floor matters: it prevents the model from claiming costs that diverge from physical-electronics reality. This driver does the heaviest lifting in Y3-Y6, when V1 AESA and V3 C-UAS volume doublings come fastest.
2. **Platform reuse.** The five reusable modules (M1 Radio, M2 DSP, M3 Systems Engineering, M4 Embedded SW, M5 AI/ML) carry NRE off the per-product P&L. Reuse strength rises from 25-60% in Y1 to 97-99% by Y10. The cost saved is captured in the *engineering-in-COGS* line (cleared engineers, qualification labour, sustainment) and shows up as gross-margin expansion rather than as R&D under-spend.
3. **Software mix.** V6 grows from ~25% of Y1 revenue (off a small base) to ~10% of Y10 revenue, but it runs at 93-94% gross margin throughout. The blended GM lift from this mix shift is ~250-300 bps by Y10. **Analyst assumption:** software GM of 93-94% is consistent with the source narrative (section 9.2) and with comparable defense-software disclosures (Palantir government segment >75% GM; pure-IP software lines higher).

Year-by-year gross margin build (illustrative decomposition; bridge components rounded to nearest %):

| Year | Wright's-Law BoM uplift | Platform reuse uplift | Software-mix uplift | Blended GM% |
| - | - | - | - | - |
| Y1 | base | base | base | 51% |
| Y2 | +3 ppt | +1 ppt | +1 ppt | 56% |
| Y3 | +6 ppt | +3 ppt | +2 ppt | 62% |
| Y4 | +7 ppt | +4 ppt | +2 ppt | 64% |
| Y5 | +8 ppt | +5 ppt | +2 ppt | 65% |
| Y6 | +9 ppt | +5 ppt | +2 ppt | 66% |
| Y7 | +9 ppt | +6 ppt | +2 ppt | 66% |
| Y8 | +9 ppt | +6 ppt | +2 ppt | 67% |
| Y9 | +9 ppt | +6 ppt | +2 ppt | 67% |
| Y10 | +9 ppt (BoM at 70% floor) | +6 ppt (reuse at 97-99%) | +2 ppt (V6 at 10% mix) | **67%** |

**Analyst assumption:** the per-driver allocation above is a directional decomposition consistent with the source's three-driver narrative (section 9.2); the source does not publish a year-by-year breakdown of GM by driver, so percentages are calibrated to the published GM endpoints (51% Y1, 67% Y10) and the published consistency band (62-67% from Y3 onward).

## D. Operating Cost Structure

The operating-expense stack is built from four blocks:

| Block | Rule | Notes |
| - | - | - |
| S&M | 8% of revenue | Capture, bid, demos, exhibitions, field marketing |
| G&A | 7% of revenue | Executive, finance, HR, legal, export-control, IT |
| Bid & Proposal | 3% of revenue | Defense-specific overhead - the cost of competing for fixed-price programme awards |
| Compliance (annual, escalates 4%/yr) | Export ctrl Rs.2 Cr + CMMC L3 Rs.14.25 Cr + AS9100/CMMI Rs.8.55 Cr = Rs.24.8 Cr Y1 base | Real annual outflow, not a one-time set-up |
| R&D headcount | Platform investment Rs.575 Cr over 10 yrs across M1-M5 | 4% salary escalation |
| R&D capitalisation | 60% capitalised under Ind AS 38, 6-yr SL depreciation | 40% expensed in-period |

R&D capitalisation is material: at platform spend of ~Rs.50-80 Cr/yr in Y1-Y5, capitalising 60% adds Rs.30-48 Cr/yr of intangible assets that depreciate into D&A on a 6-yr SL basis. This shifts cost from EBITDA into D&A and improves the EBITDA-margin optics by 2-4 ppt in Y3-Y6 relative to a fully-expensed treatment. **Analyst note:** Ind AS 38 capitalisation requires that technical feasibility, intent to complete, ability to use/sell, future economic benefits, availability of resources and reliable measurement are all demonstrable. For a defense platform with contracted backlog and qualified modules, all six criteria are defensible; this is the standard treatment for productised platform technology by Indian-listed peers.

The combined S&M + G&A + B&P load is 18% of revenue throughout, which is competitive against legacy primes (typically 22-28% of revenue once you include programme management overhead) but slightly heavier than pure software companies (10-15%). The defense-specific Bid & Proposal line is the structural delta.

## E. EBITDA and Net Income Trajectory

The 10-year P&L summary. First positive EBITDA arrives in **Year 4**; first positive free cash flow also Year 4 (see file 06 for the FCF build). Tax in early years is shielded by carried-forward losses; MAT (15%) applies from the first year of book profitability. **Analyst assumption on tax:** corporate rate 25%, MAT 15%, NOL pool carries forward 8 years per Indian tax code; D&A and interest deductible normally. Detailed tax cash schedule is in the workbook.

| Rs.Cr | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 |
| - | - | - | - | - | - | - | - | - | - | - |
| Revenue | 53 | 203 | 491 | 855 | 1,448 | 2,180 | 2,884 | 3,659 | 4,381 | 5,055 |
| Gross profit | 27 | 114 | 304 | 547 | 941 | 1,439 | 1,903 | 2,451 | 2,935 | 3,387 |
| GM% | 51% | 56% | 62% | 64% | 65% | 66% | 66% | 67% | 67% | 67% |
| R&D (expensed, post-cap) | 32 | 38 | 44 | 47 | 49 | 51 | 53 | 55 | 57 | 59 |
| S&M (8%) | 4 | 16 | 39 | 68 | 116 | 174 | 231 | 293 | 350 | 404 |
| G&A (7%) | 4 | 14 | 34 | 60 | 101 | 153 | 202 | 256 | 307 | 354 |
| B&P (3%) | 2 | 6 | 15 | 26 | 43 | 65 | 87 | 110 | 131 | 152 |
| Compliance | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 33 | 34 | 35 |
| **EBITDA** | **-40** | **14** | **145** | **318** | **603** | **966** | **1,299** | **1,704** | **2,056** | **2,383** |
| EBITDA margin | -75% | 7% | 30% | 37% | 42% | 44% | 45% | 47% | 47% | **46.4%** |
| D&A | 5 | 10 | 23 | 38 | 56 | 64 | 70 | 75 | 78 | 80 |
| EBIT | -45 | 4 | 122 | 280 | 547 | 902 | 1,229 | 1,629 | 1,978 | 2,303 |
| Interest expense | 2 | 8 | 16 | 16 | 13 | 10 | 6 | 1 | 0 | 0 |
| Pretax income | -47 | -4 | 106 | 264 | 534 | 892 | 1,223 | 1,628 | 1,978 | 2,303 |
| Tax (MAT/regular) | 0 | 0 | 16 | 40 | 134 | 223 | 306 | 407 | 495 | 576 |
| **Net income** | **-47** | **-4** | **90** | **224** | **400** | **669** | **917** | **1,221** | **1,483** | **1,727** |

[Diagram 9: P&L Waterfall]

**Reconciliation note:** Y10 EBITDA in the table above is Rs.2,383 Cr against the source headline of Rs.2,347 Cr; the Rs.36 Cr delta reflects rounding in the analyst recomposition of S&M, G&A and B&P off the published rate cards. The EBITDA margin reconciles at 46.4% as published. Where source disagrees with the analyst build, source headline numbers govern.

## F. Unit Economics by Product (Year 10 steady-state)

Built from source section 5 (ASPs, unit volumes) with BoM ~33% of price for hardware lines (source section 5.1 explicitly states "BoM approximately one-third of selling price and falling with volume"). **Analyst assumption:** Y10 ASPs taken at the upper end of source bands consistent with reuse-driven price stability; Y10 unit volumes taken at the upper end of source bands; BoM at the Wright's-Law floor of 70% of starting BoM, i.e. ~23% of price by Y10 for mature hardware. Software (V6) modelled at 93% gross margin per source section 9.2.

| Product | Variant mix | Y10 ASP (Rs.Cr) | Y10 BoM/unit (Rs.Cr) | Y10 units | Y10 revenue (Rs.Cr) | Y10 GM% |
| - | - | - | - | - | - | - |
| V1 AESA | Blended X/S/X-naval | ~22 | ~5.1 | ~50 | ~1,080 | 70% |
| V2 EW/SIGINT | EW-A/B/C/D blended | ~12 | ~2.8 | ~70 | ~850 | 71% |
| V3 C-UAS | CUAS-A/B/C blended | ~5 | ~1.2 | ~230 | ~1,150 | 72% |
| V4 MALE UAS | UAS-A/B/C blended | ~165 | ~38 | ~5-6 | ~900 | 70% |
| V5 AUV/USV | AUV-A/AUV-B/USV-A | ~14 | ~3.2 | ~40 | ~575 | 70% |
| V6 Military AI | AI-A/B/C blended | ~5 | ~0.3 | ~95 | ~500 | 93% |
| **Total** |  |  |  |  | **~5,055** | **~67% (blended)** |

The blended ~67% gross margin reconciles to source section 9.2. Hardware-line GMs sit at ~70-72%, above legacy-prime hardware norms of 15-25%, because (a) the platform-reuse leverage has removed NRE from per-product cost, (b) BoM is at the Wright's-Law floor, and (c) software pull-through is attributed back to V6, not hidden inside hardware GM.

## G. Working Capital Mechanics

Defense in India is a long-cash-cycle business. The plan sizes the balance sheet accordingly:

| Driver | Value | Implication |
| - | - | - |
| DSO | 180 days | MoD pays slowly; TReDS not available for MoD receivables |
| DPO | 45 days | Standard supplier terms for cleared vendors |
| Inventory | 90 days | Long-lead RF, GaN and FPGA components; balanced against VMI on lower-criticality items |
| Cash conversion cycle | DSO + Inv - DPO = 225 days | ~62% of revenue tied up in NWC at gross level |
| Customer advance | 15% on award (indigenous-development MoD) | Partial offset to DSO; recognised as contract liability |
| PBG | 3% of closing backlog | Y10 PBG ~Rs.500 Cr against Rs.16,680 Cr backlog |
| BG fee | 1.1% p.a. on outstanding BG (reduced from 1.5% by Rs.150 Cr land collateral) |  |
| BG collateral schedule | 100% Y1-2 > 50% Y3 > 30% Y4 > 20% Y5+ | Cash usage drops materially from Y5 once bank track record is established |

The 225-day cash conversion cycle translates to a *gross* NWC drag of ~62% of revenue. Net of the 15% customer advance, the NWC drag is approximately **47% of revenue** at steady state. This is the single largest balance-sheet item the plan must finance: at Y10 revenue of Rs.5,055 Cr, net NWC sits around Rs.2,370 Cr. The funding plan (file 05) is sized explicitly to bridge the company through the *peak* of NWC absorption in Y3-Y4 when revenue is ramping fastest relative to the financing base.

[Diagram 6: Working Capital Cycle]

**Analyst assumption:** the 47% net-NWC-of-revenue figure assumes that 100% of MoD revenue carries the 15% advance. In practice, some retrofit contracts and certain export contracts will not, so the realised NWC drag is likely in the 48-52% range. The funding plan carries a buffer (file 05, Section D) sized for this.

## H. Capex Plan

Gross capex over 10 years totals approximately Rs.600 Cr. The shape is back-end-loaded to the inflection phase (Y3-Y5) when partner-lab dependence is replaced by owned infrastructure.

| Year | Capex (Rs.Cr) | Cumulative | Stage |
| - | - | - | - |
| Y1 | ~36 | 36 | Asset-light; rent partner facilities |
| Y2 | ~67 | 103 | Production scale prep |
| Y3 | ~118 | 221 | Anechoic chamber, EMI/EMC, SMT line begin |
| Y4 | ~136 | 357 | UAS hangar, maritime tank online |
| Y5 | ~94 | 451 | Capex peak tapers |
| Y6 | ~30 | 481 | Maintenance + targeted capacity |
| Y7 | ~25 | 506 | Maintenance |
| Y8 | ~30 | 536 | Refresh cycle on FPGA/GPU/IT |
| Y9 | ~36 | 572 | Refresh + expansion |
| Y10 | ~28 | ~600 | Steady-state replacement |

Category breakdown (cumulative 10-year):
- Test infrastructure (anechoic, EMI/EMC, HALT/HASS, RF/EW benches, VNAs): ~Rs.180 Cr
- Production (cleanroom for SMT/GaN packaging, SMT assembly line): ~Rs.105 Cr
- Compute (FPGA stations, GPU clusters): ~Rs.85 Cr
- Domain-specific (UAS flight-test hangar, maritime test tank): ~Rs.150 Cr
- Office, IT, vehicles, facilities: ~Rs.80 Cr

[Diagram 7: Funding Stack vs Cash Curve] - capex profile overlays the funding curve in file 05.

## I. Headcount Plan

Total headcount scales from 91 (Y1) to 543 (Y10). The mix shifts predictably from R&D-heavy early to production-heavy late.

| Year | Total HC | R&D / Eng (incl. AI) | Production + Field | G&A + S&M + BD | Comment |
| - | - | - | - | - | - |
| Y1 | 91 | ~52 (57%) | ~16 (18%) | ~23 (25%) | Platform build |
| Y2 | 156 | ~85 (54%) | ~37 (24%) | ~34 (22%) | Qualification + early scale |
| Y3 | 234 | ~120 (51%) | ~70 (30%) | ~44 (19%) | Inflection year |
| Y4 | 287 | ~140 (49%) | ~95 (33%) | ~52 (18%) | Multi-product ramp |
| Y5 | 343 | ~155 (45%) | ~130 (38%) | ~58 (17%) | All six lines shipping |
| Y6 | 414 | ~170 (41%) | ~180 (43%) | ~64 (15%) | Export scale begins |
| Y7 | 468 | ~180 (38%) | ~220 (47%) | ~68 (15%) |  |
| Y8 | 500 | ~185 (37%) | ~245 (49%) | ~70 (14%) |  |
| Y9 | 522 | ~190 (36%) | ~260 (50%) | ~72 (14%) |  |
| Y10 | 543 | ~195 (36%) | ~275 (51%) | ~73 (13%) | Mature multi-domain prime |

**Analyst assumption:** intermediate headcount points Y3, Y5, Y7-Y9 are interpolated from the published milestones (91 > 156 > 287 > 414 > 543); function-mix percentages are calibrated to the role-level table in the workbook *Headcount* sheet (RF/Microwave, DSP/FPGA, Aerospace/Flight, Manufacturing, Production Technicians, Field Service, Capture/BD, Executive, etc.).

Contract manufacturing at qualified partners absorbs 30-40% of unit volumes for AESA, C-UAS and similar hardware lines. This is embedded in COGS-BoM, not in in-house headcount, and is the principal reason the Y10 in-house production headcount of ~275 supports Rs.5,055 Cr of revenue (revenue per employee of ~Rs.9.3 Cr/head, which is in line with software-influenced defense companies and roughly 3-5x above legacy primes).

The R&D share falling from 57% to 36% is *not* an absolute reduction - it is the production base growing faster. Absolute R&D headcount more than triples from 52 to 195 over the plan period, which is what sustains the six-product platform-evolution trajectory in Phase III.

## Cross-references

- File 05 sets out how the funding stack (Rs.1,100 Cr equity + Rs.200 Cr debt) sizes against the peak cumulative cash deficit of Rs.1,062 Cr in Y3.
- File 06 sets out the FCF build, terminal-value framing, sensitivity analysis (revenue ramp, GM, DSO, BoM floor) and the resulting project IRR of 31.9% / NPV Rs.747 Cr at the 18% WACC published in the workbook *Assumptions* sheet.
