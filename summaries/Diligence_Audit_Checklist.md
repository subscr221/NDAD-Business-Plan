# Nitrodynamics — Row-Level Diligence Audit Checklist

*Verification protocol for an external diligence firm against `Defense_Platform_Business_Plan_Financial_V2.xlsx` (referenced in narrative as the INR_CORRECTED workbook).*

Each item is structured as **[Sheet · Row/Range · Check · Evidence required]**. Items are intended to be executed sequentially within each section; cross-section dependencies are flagged inline.

---

## C.1 Workbook Integrity Checks (perform first)

| # | Sheet | Range | Check | Evidence required |
|---|---|---|---|---|
| 1 | `BalanceSheet` | Check row | Total Assets = Total Liabilities + Equity in every year | Zero in all 10 columns |
| 2 | `Funding` | Min-cash compliance row | Funding gap = 0 in all years | Zero in all 10 columns |
| 3 | `R&D_Buckets` | Section E | Research% + Capitalised% + Non-eligible% = 100% per module per year | 50 module-year cells sum to 1.00 |
| 4 | All sheets | Year columns | Confirm Y1 in column C (P&L/CF/BS/BreakEven/KPIs) vs. Y1 in column D (operating sheets) | Document the offset; verify no inserted columns |
| 5 | `Revenue` | D6:M11 | Cell-by-cell hard-link to `Backlog!D89:M94` | Trace each of 60 cells |
| 6 | `Platform` | Rows 21–25 | Effective reuse strength = MIN(maturity × `Assumptions!C26`, 1.0) | Spot-check 10 cells |
| 7 | `R&D_NRE` | Row 9 | NRE avoided = Row 8 (gross standalone) − Row 6 (leveraged) | Cumulative = Rs. 994.3 Cr |
| 8 | `Capex` | Section B | Each asset depreciates straight-line over stated life; SUM(depreciation) ≤ SUM(capex) | Per-asset audit |
| 9 | All | Formulas | No hard-coded values overriding formulas in calculation rows | Use Excel "Show Formulas" view |
| 10 | All | Circular refs | None (model should be acyclic) | Confirm via Excel error-check |

## C.2 Revenue & Backlog Verification

| # | Sheet | Range | Check | Evidence required |
|---|---|---|---|---|
| 11 | `Backlog` | Rows 13–18 | Pwin assumptions per vertical | Benchmark against published MoD award rates per vertical |
| 12 | `Backlog` | Rows 20–25 | Bookings = pipeline × Pwin | Reconcile to capture-plan in `07_operating_model.md` |
| 13 | `Backlog` | Rows 29–35 | Backlog roll-forward: Opening + Bookings − Revenue = Closing | Manual recompute, all 60 cells |
| 14 | `Backlog` | Row 38 | Realised B:B vs. target rows 6–11 | Year-by-year variance |
| 15 | `Backlog` | Rows 82–87 | Delivery rates 0.50/0.50/0.33/0.33/0.25/0.25 — defensible against published lead times | Cross-check to V-sheet variant production cycles |
| 16 | `Backlog` | Row 95 | Y10 closing backlog = Rs. 16,680 Cr | Reconstruct from 10-yr bookings − 10-yr revenue + opening |
| 17 | `Backlog` | Section G | Customer advance 15% × bookings; contract liability amortises with deliveries | Tie to `BalanceSheet` Customer Advances |
| 18 | V1–V6 | Per variant | ASP and unit volumes within published source bands | Per-variant cross-check |
| 19 | `Revenue` | Rows 23–28 | BoM COGS scaling: V-sheet COGS × (delivered rev ÷ V-sheet supporting rev) | Spot-check 5 vertical-years |
| 20 | V-sheets | All | Wright's-Law cost factor 0.92 per doubling; floor 70% of starting BoM | Reconstruct curve for V1 X-band airborne |

## C.3 Cost Model Verification

| # | Sheet | Range | Check | Evidence required |
|---|---|---|---|---|
| 21 | `Headcount` | Section A | HC ramp 91→543; role-level totals reconcile to function-level totals | Independent recount |
| 22 | `Headcount` | Section B | Salary escalation 4% p.a.; cost per role within Indian defense-tech market band | Market benchmark per role |
| 23 | `Headcount` | Section C | Personnel allocated to R&D / COGS / S&M / G&A consistent with org chart | Reconcile to `07_operating_model.md` |
| 24 | `R&D_NRE` | Row 5 | Platform NRE = `Platform` row 11 | Direct link verification |
| 25 | `R&D_NRE` | Row 6 | Leveraged vertical NRE from `ReuseMatrix` Section C | Independent recompute |
| 26 | `Capex` | Section A | Per-asset capex amounts within market range | Vendor quote benchmarking on top-10 line items |
| 27 | `Capex` | Y3–Y4 | Anechoic + EMI/EMC + SMT line capex profile | Vendor proposals required |
| 28 | `Opex` | Rows 6–20 | Each line item within Indian defense-tech opex norms | Per-line benchmark |
| 29 | `Opex` | Row 21 | BG fee = 1.1% × `Backlog` row 62 (total BG outstanding) | Formula check + bank-quote evidence on 1.1% rate |
| 30 | `P&L` | S&M, G&A, B&P | 8% + 7% + 3% of revenue rule | Confirm constants vs. legacy-prime benchmarks |

## C.4 Accounting Treatment — Ind AS 38 Deep-Dive

| # | Sheet | Range | Check | Evidence required |
|---|---|---|---|---|
| 31 | `R&D_Buckets` | Section B | Research% per module per year | Project-level documentation of exploratory vs. development work |
| 32 | `R&D_Buckets` | Section C | Capitalisation% per module per year | **Ind AS 38 six-criteria evidence pack per module-year**: technical feasibility, intent to complete, ability to use/sell, future economic benefit, resources to complete, reliable measurement |
| 33 | `R&D_Buckets` | Section I | Amortisation schedule rolling SL over `Assumptions!C58` life | Per-vintage amortisation trace |
| 34 | `R&D_Buckets` | Net intangibles | Capped at gross capitalised R&D (cannot be negative) | Formula check |
| 35 | `R&D_Buckets` | Section J | Tax bridge: book PBT + book amort − current-year eligible capitalised dev | Tie to `P&L` tax line; **engage tax counsel** |
| 36 | `R&D_NRE` | Row 14 | Weighted capitalisation rate ~60% blended | Reconcile against per-module weights |
| 37 | TRL evidence | Per module | Only modules at TRL ≥ 6 should be capitalised | Independent technical reviewer sign-off |
| 38 | `Capex` | All | No R&D costs misclassified as PP&E | Definition test per asset |
| 39 | `BalanceSheet` | Intangibles | Y/Y change = capitalised additions − amortisation | Independent recompute |

## C.5 Working Capital, BG and Restricted Cash

| # | Sheet | Range | Check | Evidence required |
|---|---|---|---|---|
| 40 | `Assumptions` | DSO | 180 days **must be validated against**: (a) V2 ESM payment history; (b) ≥2 reference MoD indigenous-development contracts; (c) bank/factor evidence on TReDS availability | External evidence pack |
| 41 | `Assumptions` | DPO | 45 days — cross-check against top-20 supplier MSAs | Supplier-term audit |
| 42 | `Assumptions` | Inventory | 90 days — reconcile to RF/GaN/FPGA lead times | Component lead-time matrix |
| 43 | `Backlog` | Row 61 | PBG = 3% × closing backlog | Bank confirmation of PBG sizing convention |
| 44 | `Backlog` | Section I | BG collateral schedule 100→50→30→20% | **Written commitment from ≥2 banks** |
| 45 | `Backlog` | Row 64 | Restricted cash = collateral% × total BG outstanding | Trace to `BalanceSheet` Restricted Cash |
| 46 | `CashFlow` | CFO line | ΔNWC = DSO×rev/365 − DPO×COGS/365 + inv×COGS/365 | Independent recompute |
| 47 | `CashFlow` | CFO line | Δ Customer Advances flows from `Backlog` row 57 | Direct link check |
| 48 | `CashFlow` | CFI line | Restricted cash movements | Reconcile to BG collateral schedule |
| 49 | `BalanceSheet` | AR | = revenue × DSO/365 | Year-by-year check |
| 50 | `BalanceSheet` | Customer Advances | Tied to `Backlog` Section G | Cross-link verification |

## C.6 Funding & Capital Structure

| # | Sheet | Range | Check | Evidence required |
|---|---|---|---|---|
| 51 | `Funding` | Equity rounds | 450/400/250 Rs. Cr in Y1/Y2/Y3 | Round-sizing rationale doc |
| 52 | `Funding` | Venture debt | Rs. 200 Cr peak (Y3–Y4); 8% interest; retired by Y9 | Term-sheet evidence |
| 53 | `Funding` | Interest line | 8% on outstanding debt balance | Year-by-year recompute |
| 54 | `Funding` | Min-cash check | Cash ≥ Rs. 100 Cr in every year | Verify against `CashFlow` ending cash |
| 55 | `P&L` | Interest expense | Tie to `Funding` interest schedule | Direct link check |
| 56 | `BalanceSheet` | Paid-in capital | Cumulative equity = Rs. 1,100 Cr by end Y3 | Confirm |
| 57 | `BalanceSheet` | Debt | Peak Rs. 200 Cr Y3–Y4; zero by Y9 | Confirm |

## C.7 Tax, NOL and MAT

| # | Sheet | Range | Check | Evidence required |
|---|---|---|---|---|
| 58 | `Assumptions` | Tax rate | 25% corporate; 15% MAT | Current Indian tax code reference |
| 59 | `P&L` | Tax line | NOL utilisation: Y1–Y2 losses pool; drained Y3–Y5 | NOL roll-forward schedule |
| 60 | `P&L` | Tax line | MAT applies if MAT > regular tax post-NOL | Year-by-year MAT vs. regular comparison |
| 61 | `BalanceSheet` | MAT credit asset | Builds in MAT-binding years; reverses when regular tax > MAT | Roll-forward check |
| 62 | `R&D_Buckets` | Section J tax bridge | Reconciles book vs. tax PBT | **Tax counsel sign-off required** |
| 63 | `BalanceSheet` | DTA | Recognised only to extent of probable future taxable income | Ind AS 12 recoverability test |

## C.8 Valuation Outputs

| # | Sheet | Range | Check | Evidence required |
|---|---|---|---|---|
| 64 | `BreakEven` | NPV row | Discount FCF stream at WACC; result Rs. 747 Cr | Manual XNPV recompute |
| 65 | `BreakEven` | IRR row | Project IRR on FCF stream = 31.9% | Manual XIRR recompute |
| 66 | `Assumptions` | WACC | 18% — challenge against Indian defense-tech cost of capital | Comparable beta + risk-free + ERP build |
| 67 | `KPIs` | Year-10 metrics | Revenue 5,055; EBITDA 2,347 (46.4%); NI 1,717 | Tie to `P&L` |
| 68 | `KPIs` | Cumulative metrics | Revenue 21,209; EBITDA 8,100; NI 5,548; FCF 4,803; NRE avoided 994 | Sum of years |
| 69 | `BreakEven` | Row 27 | Break-even revenue = fixed cost / weighted GM; Y6 snapshot ~Rs. 981 Cr | Recompute |

## C.9 Defense / Regulatory / Compliance Audit

| # | Item | Evidence required |
|---|---|---|
| 70 | Export-control regime | ITAR/EAR/SCOMET classification per product variant; compliance officer letter |
| 71 | AS9100 / CMMI / CMMC certification status | Current certificates or roadmap to acquire |
| 72 | MoD vendor registration | iDEX / TDF / DRDO empanelment evidence |
| 73 | Capture-team capacity | Headcount vs. pipeline size implied by Pwin |
| 74 | Bid-and-proposal capacity | B&P opex line vs. number of bids implied by pipeline |
| 75 | Cleared facilities | Lease, security clearance, classified-programme firewall evidence |
| 76 | Top-3 dependencies | Identify any single-source long-lead supplier risk (GaN MMIC, FPGA, GPU) |
| 77 | Export licence pipeline | For any FMS/DCS revenue assumptions, evidence of US/allied counterpart engagement |

## C.10 IP, Data and Information Rights

| # | Item | Evidence required |
|---|---|---|
| 78 | Patent filings | Per-module patent register; FTO opinions on top-5 modules |
| 79 | Open-source / third-party IP | Per-module SBOM with licence audit |
| 80 | Background IP carve-outs | Founder/employee IP assignment chain |
| 81 | Government-funded IP | iDEX / TDF / DRDO funded work — verify Bayh-Dole-equivalent retention rights |
| 82 | Data rights on V6 AI | Training-data provenance; sovereign-data clauses with MoD |
| 83 | Information rights for investor | Board observer seat, monthly KPI pack tied to `KPIs` sheet, audit access |

## C.11 Sensitivity Re-Runs (mandatory before term-sheet)

| # | Lever | Stress | Output to report |
|---|---|---|---|
| 84 | `Assumptions!C26` reuse multiplier | 1.0 → 0.8 → 0.7 | Y10 GM, EBITDA, NPV, IRR, peak deficit, first FCF-positive year |
| 85 | `Assumptions` DSO | 180 → 210 → 240 days | Peak deficit, Y10 NWC, NPV, cushion vs. min-cash |
| 86 | `Assumptions` BoM floor | 70% → 75% → 80% | Y10 GM, NPV |
| 87 | `Backlog` Pwin | 1.0x → 0.8x → 0.6x of plan | Y10 backlog, B:B trajectory, NPV |
| 88 | `Capex` profile | +25% in Y3–Y5 | Peak deficit, IRR |
| 89 | `Funding` debt cost | 8% → 11% → 14% | NPV, debt repayment schedule |
| 90 | **Combined adverse case** (S1b + S2b) | 0.7x reuse AND 240 DSO | Full P&L, CF, funding gap, standby sizing |

## C.12 Sign-Off Deliverables from Diligence Firm

The committee should require the diligence firm to deliver:

1. **Workbook integrity certificate** (items 1–10 passed).
2. **Revenue & backlog reconciliation memo** (items 11–20) with one independent recomputation of Y10 closing backlog.
3. **Ind AS 38 capitalisation opinion** (items 31–39) — joint sign-off by auditor + independent technical reviewer.
4. **Working-capital evidence pack** (items 40–50) — including bank commitment letters on BG terms.
5. **Tax memo** (items 58–63) — counsel sign-off on the R&D tax bridge.
6. **Valuation re-run** (items 64–69) — independent XNPV / XIRR.
7. **Defense / regulatory checklist** (items 70–77).
8. **IP / FTO opinion** (items 78–83).
9. **Sensitivity pack** (items 84–90).
10. **Red-flag register** — any item that failed verification, with severity rating and remediation.

---

*Cross-references: one-page committee summary in `IC_Summary_OnePager.md`; quantitative downside in `Stress_Test_Appendix.md`.*
