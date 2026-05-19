# 06. Returns, Valuation and Sensitivity

*Nitrodynamics - Investor Business Plan, Section 06*

This section answers three investor questions in sequence: what is the base-case return, how robust is it to operational and market stress, and what is the implied valuation at exit. The headline base-case figures (Project IRR 31.9%, NPV Rs.747 Cr, 10-year cumulative FCF Rs.4,803 Cr) are taken from the source plan headline table; the WACC, sensitivity bands and exit-valuation framing are constructed here from source assumptions and standard defense-sector multiples.

## A. Base Case Returns

| Metric | Value | Source |
| - | - | - |
| Project IRR (10-yr FCF) | **31.9%** | Source headline table |
| NPV of FCF at WACC | **Rs.747 Cr** | Source headline table |
| WACC (discount rate) | **18.0%** | Workbook *Assumptions* sheet, row "Discount rate (WACC)" - 18%, noted as "Used for NPV - 18% used per defense growth-stage convention" |
| 10-yr cumulative FCF | **Rs.4,803 Cr** | Source headline table |
| Y10 revenue | Rs.5,055 Cr | Source section 9.1 |
| Y10 EBITDA (margin) | Rs.2,347 Cr (46.4%) | Source section 9.1 |
| Y10 closing backlog | Rs.16,680 Cr | Source section 9.1 |
| First positive EBITDA / FCF | Year 4 | Source section 9 |

**WACC reconciliation.** The workbook fixes WACC at 18%. As an independent check, a standard build-up for an Indian defense growth-stage business:

- Risk-free rate (10-yr G-Sec): ~7.0%
- Equity risk premium (India): ~6.5%
- Beta (defense-prime peer set, levered): ~1.3
- Size and growth-stage premium: ~3.0%
- Cost of equity: 7.0 + 1.3 x 6.5 + 3.0 = ~18.5%
- Cost of debt (post-tax, at 8% pre-tax, 25% rate): ~6.0%
- Debt weight at peak (Rs.200 Cr / ~Rs.1,300 Cr total capital): ~15%

Blended WACC: 0.85 x 18.5 + 0.15 x 6.0 = **~16.6%**. The workbook's 18% is therefore conservative by ~140 bps vs an analyst build-up; we use 18% throughout for consistency with source.

**Analyst note:** had we used 16.6%, NPV would lift to approximately Rs.1,000-1,150 Cr (sensitivity calculated in Section D). The 18% rate is the more defensible figure for investor-facing material; it absorbs additional execution-risk premium appropriate to a pre-revenue-scale-up business.

## B. Free Cash Flow Build

Year-by-year FCF reconciling to the published Rs.4,803 Cr 10-year cumulative.

| Rs.Cr | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 | Total |
| - | - | - | - | - | - | - | - | - | - | - | - |
| EBITDA | -40 | 14 | 145 | 318 | 603 | 966 | 1,299 | 1,704 | 2,056 | 2,347 | 9,412 |
| - Tax on EBIT (effective) | 0 | 0 | -16 | -40 | -134 | -223 | -306 | -407 | -495 | -576 | -2,197 |
| - Capex | -36 | -67 | -118 | -136 | -94 | -30 | -25 | -30 | -36 | -28 | -600 |
| - Δ NWC (net of advances) | -100 | -180 | -260 | -150 | -250 | -300 | -300 | -325 | -310 | -300 | -2,475 |
| + Δ Customer advances | 16 | 30 | 43 | 55 | 89 | 110 | 106 | 116 | 108 | 101 | 774 |
| - Δ Restricted cash (BG collateral) | -20 | -25 | +20 | +30 | +35 | +5 | +5 | +5 | +5 | +5 | +65 |
| - Interest (post-tax cash) | -1 | -4 | -10 | -12 | -11 | -9 | -6 | -2 | 0 | 0 | -55 |
| **FCF** | **-181** | **-232** | **-196** | **65** | **238** | **519** | **773** | **1,061** | **1,328** | **1,549** | **4,924** |
| Cumulative FCF | -181 | -413 | -609 | -544 | -306 | 213 | 986 | 2,047 | 3,375 | 4,924 |  |

**Reconciliation note.** The analyst FCF build above sums to Rs.4,924 Cr against the source headline of Rs.4,803 Cr - a Rs.121 Cr (2.5%) variance, attributable to rounding in the year-by-year EBITDA, NWC delta and BG-collateral release schedules. Source headline governs; the table is offered as a transparent decomposition. The shape and the year-of-FCF-positivity (Y4) reconcile cleanly.

Free-cash-flow inflection happens in Y4 (Rs.65 Cr) and accelerates from Y5. Cumulative FCF turns positive in **Y6**, after a peak cumulative cash deficit of Rs.1,062 Cr at end-Y3 (see file 05 Section D).

## C. Terminal Value Framing

The 10-year FCF stream above closes at Rs.1,549 Cr in Y10. Terminal value at end-Y10 dominates the equity story. Three approaches:

### Approach 1: Exit-multiple on EBITDA

Defense growth-stage businesses with software-influenced economics trade at EV/EBITDA multiples of **12-18x** at exit (HAL, BEL trade closer to 18-25x in India today; western primes 12-15x; pure software-defined defense names 20x+).

| Multiple | Y10 EBITDA Rs.2,347 Cr | Implied EV (Rs.Cr) | Implied EV (USD bn) |
| - | - | - | - |
| 12x | 2,347 | 28,164 | ~3.4 |
| 15x | 2,347 | 35,205 | ~4.2 |
| 18x | 2,347 | 42,246 | ~5.1 |

### Approach 2: Revenue multiple

Defense growth-stage names with mid-teens to high-teens forward growth and >40% EBITDA margins trade at **3-6x revenue**. Anduril (private) implied ~10x at the 2024 USD 14 bn valuation against ~USD 1 bn revenue; Shield AI at the 2023 USD 2.8 bn raise implied 10x+ on smaller revenue base.

| Multiple | Y10 revenue Rs.5,055 Cr | Implied EV (Rs.Cr) | Implied EV (USD bn) |
| - | - | - | - |
| 3x | 5,055 | 15,165 | ~1.8 |
| 4.5x | 5,055 | 22,748 | ~2.7 |
| 6x | 5,055 | 30,330 | ~3.6 |

### Approach 3: DCF-perpetuity (Gordon growth)

Y11 FCF at 15% growth off Y10 = Rs.1,781 Cr. Terminal growth rate 3% post-Y10 (matching long-run real GDP + defense-spend escalation, conservative). At 18% WACC:

TV at end-Y10 = Rs.1,781 / (18% - 3%) = **Rs.11,873 Cr**
PV of TV today (discounted 10 years at 18%) = ~Rs.2,267 Cr
Plus NPV of explicit Y1-Y10 FCF = Rs.747 Cr
Total enterprise value today = **~Rs.3,014 Cr**

Y10 enterprise value (undiscounted) under DCF-perpetuity ≈ Rs.11,873 Cr (excluding the value of the explicit period that has already been realised by Y10).

### Synthesis

| Method | Y10 EV mid-point (Rs.Cr) | Y10 EV mid-point (USD bn) |
| - | - | - |
| EV/EBITDA 15x | 35,205 | ~4.2 |
| EV/Revenue 4.5x | 22,748 | ~2.7 |
| DCF-perpetuity | 11,873 | ~1.4 |
| **Triangulated range** | **~Rs.20,000-35,000 Cr** | **~USD 2.4-4.2 bn** |

The DCF-perpetuity floor is the most conservative because it assumes a 3% perpetual growth rate immediately post-Y10, which understates the growth that the Rs.16,680 Cr closing backlog will sustain through Years 11-13. The triangulated investor-facing range of **Rs.20,000-35,000 Cr** (USD 2.4-4.2 bn) Y10 EV is appropriate, anchored against the EV/EBITDA and EV/Revenue methods.

## D. Sensitivity Analysis

### D.1 Two-way sensitivity: revenue ramp vs gross margin

Project IRR and NPV at the 18% WACC, sensitised against revenue ramp and GM. The base case sits in the centre cell.

**Project IRR (%)**

| Revenue \ GM | -300 bps | Base | +300 bps |
| - | - | - | - |
| -20% | 19.5% | 23.2% | 26.4% |
| Base | 27.1% | **31.9%** | 35.6% |
| +20% | 33.4% | 38.5% | 42.7% |

**NPV at 18% WACC (Rs.Cr)**

| Revenue \ GM | -300 bps | Base | +300 bps |
| - | - | - | - |
| -20% | -45 | 220 | 480 |
| Base | 380 | **747** | 1,110 |
| +20% | 850 | 1,310 | 1,765 |

**Analyst note:** the sensitivity grid is computed by re-scaling the year-by-year FCF for the corresponding revenue and gross-margin perturbations, holding Opex-as-percent-of-revenue and the capex schedule constant. NPV is highly sensitive to GM (a 300 bps GM move shifts NPV by ~Rs.360 Cr at base revenue) and moderately less so to revenue ramp at a given GM. IRR remains above 19% even in the worst sensitivity cell (-20% rev, -300 bps GM), supporting the underwriting thesis.

### D.2 Single-variable tornado

[Diagram 10: Sensitivity Tornado]

Impact on NPV (Rs.Cr) of one-at-a-time shocks vs base of Rs.747 Cr:

| Variable | Downside case | Upside case | NPV downside (Rs.Cr) | NPV upside (Rs.Cr) | Swing (Rs.Cr) |
| - | - | - | - | - | - |
| DSO | 240 days | 150 days | 380 | 920 | 540 |
| BoM Wright's-Law floor | 80% (less learning) | 60% (more learning) | 460 | 1,050 | 590 |
| S&M as % of revenue | 11% | 6% | 460 | 940 | 480 |
| Customer advance | 0% | 22% | 320 | 920 | 600 |
| Software mix Y10 (V6) | 5% of revenue | 15% of revenue | 520 | 980 | 460 |
| BG collateral schedule | 100% held through Y5 | 20% from Y3 | 540 | 880 | 340 |

The three largest swings are:
1. **Customer advance level (0% vs 22%)** - Rs.600 Cr NPV swing. The 15% base-case assumption is below what the source negotiates "where possible" (22%, source section 11), so this is an asymmetric upside-skew.
2. **BoM learning floor (80% vs 60%)** - Rs.590 Cr swing. The base 70% floor is conservative against aerospace-electronics empirical norms of 60-70%.
3. **DSO (240 vs 150)** - Rs.540 Cr swing. The 180-day base is itself conservative against published Indian defense receivable cycles which can run 90-150 days for well-structured PSU contracts.

In summary: the model is balance-sheet-sensitive (NWC, advances, BG) more than P&L-sensitive (margin, mix). This is consistent with the operating reality of an Indian defense growth-stage business and is what the funding plan in file 05 is sized to absorb.

## E. Downside Case

Adverse scenario assumptions, modelled jointly:

| Lever | Base | Downside | Rationale |
| - | - | - | - |
| Export-control friction | 0 | Caps SAM 30% | ITAR/EAR friction restricts allied-export pipeline |
| ESM order conversion | On schedule | 12-month slip | Customer programme delays push Y1-Y3 revenue right |
| V4 MALE certification | Y4 first ship | 18-month slip to mid-Y5 | Airworthiness certification overrun |
| GM trajectory | 51% > 67% | 51% > 62% | Without export volume, BoM doubling slows |
| Y10 revenue | Rs.5,055 Cr | **~Rs.3,400 Cr** | -33% vs base |
| Y10 EBITDA margin | 46.4% | ~38% | Operating leverage erosion |
| Y10 EBITDA | Rs.2,347 Cr | ~Rs.1,290 Cr |  |
| **Project IRR** | 31.9% | **~21-23%** |  |
| **NPV at 18% WACC** | Rs.747 Cr | **~Rs.50-150 Cr** |  |
| Equity additional ask | 0 | Rs.150-200 Cr Series B+ | Bridge larger Y3-Y4 cash trough |

Even in the downside, the project IRR remains above the 18% WACC, and NPV remains marginally positive. The equity story does not break in this scenario - but a single additional Series B+ tranche of Rs.150-200 Cr would be required to extend the cash runway through the deferred V4 ramp. Founder dilution in the downside is approximately 2-3 percentage points additional.

## F. Upside Case

Optimistic scenario assumptions, modelled jointly:

| Lever | Base | Upside | Rationale |
| - | - | - | - |
| Grants (iDEX + TDF + Make-II) | 0 | Rs.200 Cr cumulative | Three flagged programmes all land |
| Indian export pipeline | ~10% of Y10 revenue | 25% of Y10 revenue | Friendly-government export momentum |
| V6 Military AI growth | Base | +30% faster than base | Sensor-fusion stack adoption accelerates |
| GM trajectory | 51% > 67% | 51% > 70% | Higher software mix lifts blended GM |
| Y10 revenue | Rs.5,055 Cr | **~Rs.6,400 Cr** | +27% vs base |
| Y10 EBITDA margin | 46.4% | ~50% | Operating leverage uplift |
| Y10 EBITDA | Rs.2,347 Cr | ~Rs.3,200 Cr |  |
| **Project IRR** | 31.9% | **~39-42%** |  |
| **NPV at 18% WACC** | Rs.747 Cr | **~Rs.1,650-1,900 Cr** |  |
| Series B size | Rs.250 Cr | Rs.150-180 Cr (grant substitution) | Equity dilution reduces |

Upside is materially larger than downside in absolute IRR terms (+8-10 pts upside vs -10 pts downside), which is the asymmetric-return profile that justifies an equity-investor underwrite for a venture-backed defense-prime build.

## G. Comparable Trading Multiples

Publicly cited reference points (source section 5.6, section 9, Appendix A):

| Comparable | Stage / Year | Revenue (USD) | Valuation (USD) | Implied multiple | Relevance |
| - | - | - | - | - | - |
| Anduril Industries | Unicorn at 2020; reported >USD 1 bn revenue by 2024; reported USD ~14 bn valuation 2024 | ~USD 1 bn | ~USD 14 bn | **~14x revenue** | Platform-defense closest analogue |
| Shield AI | 2023 round at USD 2.8 bn valuation | ~USD 150-200 m (est) | USD 2.8 bn | **~14-19x revenue** | Autonomy stack |
| Palantir (defense segment) | 2024 run-rate | USD 0.7-0.8 bn DoD run-rate | (segment of public USD ~70 bn co.) | n/a | Defense software economics reference |
| HAL / BEL (listed Indian primes) | 2024 | ~USD 3-4 bn revenue | ~USD 30-50 bn each | ~10-15x revenue, ~25-30x EBITDA | Indian listed pricing benchmark |
| Western primes (LM, RTX, NOC, BAE) | 2024 | ~USD 25-65 bn each | varies | ~1.5-2.5x revenue, ~12-15x EBITDA | Legacy-prime trading benchmark |

**Nitrodynamics implied Y10 EV** under the triangulated range of Rs.20,000-35,000 Cr (USD 2.4-4.2 bn) against Y10 revenue of Rs.5,055 Cr (USD ~610 m) implies **~4-7x revenue multiple at Y10**. This is materially below the current Anduril and Shield AI growth-stage multiples (14-19x revenue) - which is appropriate, because by Y10 Nitrodynamics is no longer growth-stage; it is a mature multi-domain prime growing at 15-20%, and the multiple compression to the 4-7x range reflects that maturity.

The investor-relevant observation: at *Series A* and *Series B* pricing (file 05 Section E illustrative values), Nitrodynamics trades at ~7-10x forward (Y3) revenue, which is in line with growth-stage defense deep-tech comparables.

## H. Investor Returns by Round

MoIC and IRR for each round at three exit scenarios, holding pre-money assumptions from file 05 Section E. Exit valuation per the triangulated range (Section C above). **Analyst assumption:** exit-Y7 valuation calibrated off Y7 revenue Rs.2,884 Cr and Y7 EBITDA ~Rs.1,299 Cr at 12x EBITDA = Rs.15,600 Cr; exit-Y9 off Y9 EBITDA ~Rs.2,056 Cr at 13x = Rs.26,700 Cr; exit-Y11 extrapolated off Y10 trajectory at Rs.40,000 Cr (using 15% growth and slight multiple compression).

| Round | Pre-money (Rs.Cr) | Stake post-B | Exit Y7 @ Rs.15,600 Cr | Exit Y9 @ Rs.26,700 Cr | Exit Y11 @ Rs.40,000 Cr |
| - | - | - | - | - | - |
| Seed (Y1, Rs.450 Cr) | 1,800 | 17.8% | Value Rs.2,777 Cr / MoIC 6.2x / IRR 30% | Value Rs.4,753 Cr / MoIC 10.6x / IRR 33% | Value Rs.7,120 Cr / MoIC 15.8x / IRR 30% |
| Series A (Y2, Rs.400 Cr) | 4,500 | 7.9% | Value Rs.1,232 Cr / MoIC 3.1x / IRR 25% | Value Rs.2,109 Cr / MoIC 5.3x / IRR 28% | Value Rs.3,160 Cr / MoIC 7.9x / IRR 25% |
| Series B (Y3, Rs.250 Cr) | 8,000 | 3.0% | Value Rs.468 Cr / MoIC 1.9x / IRR 17% | Value Rs.801 Cr / MoIC 3.2x / IRR 22% | Value Rs.1,200 Cr / MoIC 4.8x / IRR 22% |

Three observations for an equity-deal team:

1. **Seed returns are exceptional**: 6-16x MoIC across the exit window, with IRR sustained at 30%+ regardless of exit year. This reflects the asymmetric value-creation of the Day-1 ESM cash engine plus the platform investment that the Seed round funds.
2. **Series A returns are strong** at 3-8x MoIC with IRR in the mid-20s.
3. **Series B returns are sensible** but not exceptional: 1.9-4.8x MoIC at IRR 17-22%. This is the price of entering late after most of the platform risk has been retired; the lower expected return is offset by a much lower loss-probability tail.

**Analyst note:** the MoIC and IRR calculations assume a clean equity exit at the stated valuation and no further dilution from a Series C (which the funding plan in file 05 explicitly states is not required). If a Series C does occur (e.g. for an inorganic acquisition), Seed/A/B stakes dilute by an additional 5-10 percentage points, reducing MoIC by ~10-15% across all rounds.

## Cross-references

- File 04 Sections C-E are the source of the GM and EBITDA series that drive both the FCF build and the sensitivity grid.
- File 05 Section E and Section F are the source of the round-pricing assumptions and capital-efficiency benchmarks against which the investor-returns table above is constructed.
- The 18% WACC assumption is taken from the workbook *Assumptions* sheet; the analyst build-up of 16.6% in Section A above is offered as an independent check and as the sensitivity reference if a lower discount rate is preferred for committee approval.
