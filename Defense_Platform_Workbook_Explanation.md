# Defense Platform Workbook Explanation

Source workbook: Defense\_Platform\_Business\_Plan\_INR\_CORRECTED.xlsx

This workbook is a 10-year strategic and financial model for a platform-based defense technology company. Currency is INR crores unless a sheet explicitly says otherwise. The model is built around one shared engineering platform, six product verticals, defense-style backlog mechanics, and full financial statements.

## Model Flow

High-level dependency chain:

1. Assumptions defines global drivers: tax, WACC, working-capital days, learning curves, bank guarantees, MAT, R&D amortization life, manufacturing overhead, warranty.

2. Platform defines shared platform NRE investment and module maturity over 10 years.

3. R&D\_Buckets splits Platform NRE into research expensed, development capitalised, and development expensed / not eligible.

4. ReuseMatrix maps each vertical to the five shared platform modules and calculates how much vertical NRE is avoided through reuse.

5. V1\_AESA to V6\_MilAI contain supporting product-level unit economics: ASP, BoM, units, revenue, COGS, margins.

6. Backlog is the real consolidated revenue engine. Bookings and opening backlog flow into deliveries. Deliveries become recognized revenue.

7. Revenue pulls recognized revenue from Backlog and scales BoM COGS using the V-sheet unit economics.

8. Headcount, R&D\_NRE, Capex, and Opex build the cost base.

9. P&L combines revenue, COGS, R&D/NRE, S&M, G&A, opex, D&A, interest, tax, NOL, MAT, and the R&D tax bridge.

10. CashFlow converts the P&L into CFO, CFI, FCF, financing flows, and cash balances.

11. BalanceSheet links cash, working capital, PP&E, intangibles, debt, equity, retained earnings, and checks A = L + E.

12. Funding provides equity/debt inflows and checks minimum cash compliance.

13. KPIs and BreakEven summarize the model outputs.

Important modeling note: the six V-sheets are marked read-only supporting detail. Consolidated revenue is sourced from Backlog!D89:M94 (the six per-vertical delivery rows; row 95 is the consolidated sum), not directly from V-sheet unit shipment revenue. Editing V-sheet ASP/units changes the unit-economics baseline and therefore COGS scaling, but it does not directly change consolidated revenue unless the Backlog delivery schedule/bookings are also changed.

## Column Convention

The workbook uses two year-column conventions:

- P&L, CashFlow, BalanceSheet, BreakEven, and KPI metric rows use Y1 in column C.

- Revenue, Headcount, Capex, Opex, Funding, Backlog, V1 to V6, R&D\_NRE, Platform, R&D\_Buckets, and ReuseMatrix use Y1 in column D.

The workbook formulas compensate for this offset. Do not insert columns without auditing cross-sheet references.

## Abbreviations

- ABG: Advance Bank Guarantee.

- AESA: Active Electronically Scanned Array.

- AI: Artificial Intelligence.

- AP: Accounts Payable.

- AR: Accounts Receivable.

- ASP: Average Selling Price.

- AS9100: Aerospace quality management standard.

- ASW: Anti-Submarine Warfare.

- AUSA: Association of the United States Army exhibition.

- AUV: Autonomous Underwater Vehicle.

- AUV/USV: Autonomous Underwater Vehicle / Uncrewed Surface Vessel.

- B:B: Book-to-bill ratio, bookings divided by recognized revenue.

- BD: Business Development.

- BG: Bank Guarantee.

- BoM: Bill of Materials.

- BoY: Beginning of Year.

- B&P: Bid and Proposal.

- C2: Command and Control.

- CAD: Computer-Aided Design.

- CA: Current Assets.

- Capex: Capital Expenditure.

- CCC: Cash Conversion Cycle.

- CFI: Cash From Investing.

- CFF: Cash From Financing.

- CFO: Cash From Operations.

- CL: Current Liabilities.

- CMMC: Cybersecurity Maturity Model Certification.

- CMMI: Capability Maturity Model Integration.

- COGS: Cost of Goods Sold.

- CPFF: Cost Plus Fixed Fee.

- C-UAS / CUAS: Counter-Uncrewed Aircraft System, anti-drone system.

- CV: Computer Vision.

- D&A: Depreciation and Amortization.

- DBF: Digital Beamforming.

- DCS: Direct Commercial Sale.

- DPO: Days Payable Outstanding.

- DSO: Days Sales Outstanding.

- DSP: Digital Signal Processing.

- DTA: Deferred Tax Asset.

- EBITDA: Earnings Before Interest, Tax, Depreciation, and Amortization.

- EBIT: Earnings Before Interest and Tax.

- EDA: Electronic Design Automation.

- ELINT: Electronic Intelligence.

- EMI/EMC: Electromagnetic Interference / Electromagnetic Compatibility.

- E&O: Errors and Omissions insurance.

- EoY: End of Year.

- ESM: Electronic Support Measures.

- EW: Electronic Warfare.

- FACE: Future Airborne Capability Environment.

- FCF: Free Cash Flow.

- FPGA: Field-Programmable Gate Array.

- FMS: Foreign Military Sales.

- FP: Fixed Price.

- G&A: General and Administrative.

- GaN: Gallium Nitride.

- GM: Gross Margin.

- GNC: Guidance, Navigation, and Control.

- GPU: Graphics Processing Unit.

- HALT/HASS: Highly Accelerated Life Test / Highly Accelerated Stress Screen.

- HC: Headcount.

- HFSS: High-Frequency Structure Simulator.

- HW: Hardware.

- ICD: Interface Control Document.

- IDIQ: Indefinite Delivery / Indefinite Quantity.

- iDEX: Innovations for Defence Excellence.

- INR Cr: Indian rupees in crores. 1 crore = 10 million rupees.

- IP: Intellectual Property.

- IRR: Internal Rate of Return.

- ISR: Intelligence, Surveillance, and Reconnaissance.

- ITAR/EAR: US export-control regimes: International Traffic in Arms Regulations / Export Administration Regulations.

- JIT: Just In Time.

- LNA: Low-Noise Amplifier.

- MALE: Medium Altitude Long Endurance.

- MAT: Minimum Alternate Tax.

- MATLAB: Matrix Laboratory software.

- MFG: Manufacturing.

- MIL-STD: Military Standard.

- ML: Machine Learning.

- MLOps: Machine Learning Operations.

- MOSA: Modular Open Systems Approach.

- MVP: Minimum Viable Product.

- NOL: Net Operating Loss.

- NOPAT: Net Operating Profit After Tax.

- NPV: Net Present Value.

- NRE: Non-Recurring Engineering.

- NWC: Net Working Capital.

- OIDSS: Operational Intelligence Decision Support System.

- Opex: Operating Expense.

- PA: Power Amplifier.

- PBG: Performance Bank Guarantee.

- PBT: Profit Before Tax.

- P&L: Profit and Loss statement.

- PP&E: Property, Plant, and Equipment.

- PSU: Public Sector Undertaking.

- Pwin: Probability of Win.

- R&D: Research and Development.

- RF: Radio Frequency.

- ROIC: Return on Invested Capital.

- RTOS: Real-Time Operating System.

- S&M: Sales and Marketing.

- SDR: Software-Defined Radio.

- SIGINT: Signals Intelligence.

- SMT: Surface-Mount Technology.

- SW: Software.

- SysEng: Systems Engineering.

- TDF: Technology Development Fund.

- TL: Term Loan.

- TReDS: Trade Receivables Discounting System.

- TRL: Technology Readiness Level.

- T/R: Transmit/Receive.

- UAS: Uncrewed Aircraft System.

- UAV: Uncrewed Aerial Vehicle.

- USD: United States Dollar.

- USP: Unique Selling Proposition.

- USV: Uncrewed Surface Vessel.

- V&V: Verification and Validation.

- VC: Venture Capital.

- VMI: Vendor Managed Inventory.

- VNA: Vector Network Analyzer.

- WACC: Weighted Average Cost of Capital.

- WC: Working Capital.

- Y/Y: Year over Year.

## Abbreviation Notes And Business Impact

This section explains the abbreviations in more practical language. The technical abbreviations describe what the company builds; the financial abbreviations describe whether that build plan is fundable, profitable, cash-generative, and resilient.

### Business And Program Terms

- AESA: Advanced radar technology using electronically steered antenna arrays. This supports high-value defense products and justifies premium pricing.

- AUV / USV: Autonomous maritime platforms, underwater and surface. These expand the company into naval autonomy and create another market for the shared AI/SW/SysEng platform.

- C-UAS / CUAS: Counter-drone systems. This is a faster-cycle defense market and can generate earlier deployments than large aircraft or naval programs.

- ESM / ELINT / SIGINT / EW: Electronic support, electronic intelligence, signals intelligence, and electronic warfare. These are RF/DSP-heavy capabilities and are important because the model assumes ESM is partly developed at Day 1 and can generate early revenue.

- ISR: Intelligence, surveillance, and reconnaissance. ISR payloads and platforms tend to be mission-critical and can support recurring upgrades.

- MALE UAS: Medium Altitude Long Endurance uncrewed aircraft. This is a larger, slower-cycle product line with higher program complexity but larger contract values.

- RF / DSP / FPGA / SDR: Radio-frequency and signal-processing technologies. These are core reusable technical assets; better reuse lowers NRE and improves margins.

- AI / ML / CV / MLOps: Artificial intelligence, machine learning, computer vision, and ML operations. These increase software content and improve gross margin because software has lower BoM cost than hardware.

- SysEng / SW / RTOS / C2 / GNC: Systems engineering, software, real-time operating systems, command-and-control, and guidance/navigation/control. These are reusable platform capabilities that reduce repeat development effort across verticals.

- MIL-STD / AS9100 / CMMI / CMMC / ITAR / EAR: Defense, aerospace, quality, cybersecurity, and export-control compliance standards. These increase cost and schedule burden but are necessary to qualify for serious defense contracts.

- PBG / ABG / BG: Bank guarantees tied to performance and customer advances. They do not always hit the P&L directly, but they tie up cash as restricted collateral and can create a major funding need.

- Pwin: Probability of win. Lower Pwin means the company must maintain a larger qualified pipeline to hit the same bookings target.

- B:B: Book-to-bill ratio. Above 1.0 means backlog is growing; below 1.0 means the company is consuming backlog faster than it is winning new work.

- TRL: Technology readiness level. Higher TRL means technology is more mature, reducing delivery risk and increasing reuse potential.

- FMS / DCS: Foreign Military Sales and Direct Commercial Sale. These matter for export revenue, but also bring approval, compliance, and timing risk.

### Financial Abbreviations And Why They Matter

- ASP: Average Selling Price. Higher ASP increases revenue per unit. If ASP falls faster than BoM cost, gross margin compresses.

- BoM: Bill of Materials. This is the direct hardware cost. Lower BoM improves gross margin and cash efficiency.

- COGS: Cost of Goods Sold. This includes BoM and production/service personnel. It determines gross profit.

- GM: Gross Margin. Gross margin shows how much revenue remains after direct delivery cost. Higher GM gives the company more room to fund R&D, sales, compliance, and profit.

- R&D: Research and Development. R&D creates future products and IP, but high R&D consumes cash before revenue scales.

- NRE: Non-Recurring Engineering. NRE is one-time development cost. The core thesis of the workbook is that platform reuse reduces NRE per product.

- Capex: Capital Expenditure. Capex builds labs, test facilities, production equipment, and infrastructure. It reduces cash immediately and later appears as depreciation.

- Opex: Operating Expense. Opex is recurring operating spend such as facilities, cloud, licenses, compliance, legal, travel, and demos. It lowers EBITDA.

- S&M: Sales and Marketing. S&M helps win pipeline and bookings. Too little S&M can starve growth; too much can delay profitability.

- G&A: General and Administrative. G&A supports finance, HR, legal, compliance, and management. It must scale slower than revenue for margins to improve.

- EBITDA: Earnings before interest, tax, depreciation, and amortization. This is the main operating-profit proxy before financing and accounting charges. Positive EBITDA means the core business is becoming economically viable.

- EBIT: Earnings before interest and tax. EBIT includes D&A, so it reflects the cost of capitalized assets and intangibles more fully than EBITDA.

- D&A: Depreciation and Amortization. D&A spreads the cost of capex and capitalized R&D over time. It reduces accounting profit but is non-cash in the current year.

- PBT: Profit Before Tax. PBT determines tax exposure before NOL and MAT logic.

- NOL: Net Operating Loss. Early losses create an NOL pool that can offset future taxable income, delaying cash taxes.

- MAT: Minimum Alternate Tax. MAT can create tax cash outflow even when regular tax is reduced by NOLs. MAT credit may become a balance-sheet asset.

- DTA: Deferred Tax Asset. A DTA represents tax benefit expected in future periods. It helps the balance sheet but is not operating cash.

- NOPAT: Net Operating Profit After Tax. NOPAT is operating profit after tax and is used in ROIC calculations.

- ROIC: Return on Invested Capital. ROIC shows whether the business earns attractive returns on debt and equity capital. Sustained high ROIC supports valuation.

- WACC: Weighted Average Cost of Capital. WACC is the hurdle rate used for NPV. If business returns are below WACC, value is being destroyed.

- NPV: Net Present Value. NPV converts future FCF into today's value using WACC. Positive NPV means the plan creates value under the discount-rate assumption.

- IRR: Internal Rate of Return. IRR is the annualized return implied by the FCF stream. It is useful for project attractiveness, but in this workbook it excludes equity/debt flows and is not investor IRR.

- FCF: Free Cash Flow. FCF is cash generated after operations and investing needs. Positive FCF means the business can fund itself before financing.

- CFO: Cash From Operations. CFO shows cash produced by the operating business after working-capital effects.

- CFI: Cash From Investing. CFI captures capex, restricted cash movements, and capitalized R&D. Large negative CFI means the company is still investing heavily.

- CFF: Cash From Financing. CFF shows cash raised or repaid through equity and debt. It fills cash gaps when FCF is negative.

- AR: Accounts Receivable. AR is revenue recognized but not yet collected. High AR increases working-capital needs.

- AP: Accounts Payable. AP is supplier cost not yet paid. Higher AP temporarily preserves cash, but only within realistic supplier terms.

- DSO: Days Sales Outstanding. DSO measures customer collection delay. Higher DSO hurts cash and increases funding needs.

- DPO: Days Payable Outstanding. DPO measures how long the company takes to pay suppliers. Higher DPO improves cash timing but can strain supplier relationships.

- NWC / WC: Net Working Capital / Working Capital. NWC is cash tied up in AR and inventory less AP. Higher NWC can make a profitable business cash-hungry.

- CCC: Cash Conversion Cycle. CCC = DSO + inventory days - DPO. A longer CCC means cash is locked up for longer before converting sales into cash.

- PP&E: Property, Plant, and Equipment. PP&E represents physical assets such as labs, equipment, and facilities. It supports capability but consumes capital.

- CA / CL: Current Assets / Current Liabilities. These drive the current ratio and show short-term liquidity strength.

- P&L: Profit and Loss statement. It measures accounting profitability, not cash by itself.

- BS: Balance Sheet. It shows assets, liabilities, and equity at year-end.

- EoY / BoY: End of Year / Beginning of Year. These are timing markers used in roll-forwards such as debt, backlog, and cash.

- Y/Y: Year over Year. Y/Y growth shows how fast metrics change versus the prior year.

### How These Financial Terms Connect In This Workbook

Revenue starts in Backlog and flows to Revenue, then to the P&L. BoM and personnel COGS determine gross profit and gross margin. R&D/NRE, S&M, G&A, and opex determine EBITDA. D&A then converts EBITDA to EBIT, interest converts EBIT to PBT, and tax converts PBT to net income.

Net income does not equal cash. CashFlow adds back D&A, subtracts working-capital needs, adds customer advances, subtracts capex, restricted cash, and capitalized R&D, then adds financing from Funding. That is why the model can show revenue growth while still needing large equity/debt rounds in the early years.

## Sheet-by-Sheet Explanation

### Cover

Purpose: narrative entry point and model map. It states the company thesis: a new-age defense prime built on reusable RF, DSP, systems engineering, embedded/mission software, and AI/ML modules.

How it is built: it has no formulas. It lists the operating model, planning horizon, color key, read order, and six product verticals.

Connections: no formula dependencies. Use it as the workbook table of contents.

### KPIs

Purpose: executive dashboard.

How it is built: it pulls outputs from P&L, CashFlow, Backlog, Funding, Headcount, Capex, BalanceSheet, R&D\_NRE, and Assumptions.

Key outputs in the saved workbook:

- Year 10 revenue: 5,055.3 INR Cr.

- Year 10 EBITDA: 2,347.1 INR Cr, 46.4 percent margin.

- 10-year cumulative FCF: 4,803.3 INR Cr.

- FCF IRR: 31.9 percent.

- NPV at WACC (18 percent): 747.2 INR Cr.

- First EBITDA-positive year: Y4.

- First FCF-positive year: Y4.

- Total equity raised across the plan: 1,100 INR Cr (Y1 450, Y2 400, Y3 250).

- Peak debt balance: 200 INR Cr (Y3-Y4).

- Cumulative revenue (10 years): 21,209.2 INR Cr.

- Cumulative EBITDA (10 years): 8,100.1 INR Cr.

- Cumulative net income (10 years): 5,548.2 INR Cr.

- Cumulative R&D / NRE expense: 1,365.9 INR Cr; cumulative counterfactual NRE savings: 994.3 INR Cr.

Connections: this is an output sheet only. It should not drive the model.

### Strategy

Purpose: strategic narrative behind the model.

How it is built: static text covering vision, mission, operating thesis versus legacy primes, strategic pillars, capability waves, funding strategy, risks, and workbook reading guidance.

Connections: no formulas. It explains the qualitative thesis behind the quantitative sheets.

### MarketPositioning

Purpose: competitive positioning scorecard.

How it is built: static scoring by capability dimension across competitor categories. Rows include multi-domain coverage, AESA capability, EW/SIGINT, C-UAS, MALE UAS, AUV/USV, military AI, platform reuse, time-to-market, NRE efficiency, workforce/facility readiness, export/FMS readiness, software/AI mix, bid agility, and capital efficiency.

Connections: only the composite-score row uses formulas that sum column scores. It is not linked into financial statements.

### Roadmap

Purpose: 10-year strategic roadmap by track.

How it is built: static milestone grid for platform modules, vertical launches, facilities/certification, funding, and export/FMS.

Connections: no formulas. It explains timing assumptions that are reflected in other sheets.

### Platform

Purpose: shared platform investment and maturity model.

How it is built:

- Rows 6-10: annual shared platform NRE by module.

- Row 11: total platform NRE by year.

- Row 12: cumulative platform NRE.

- Rows 15-19: module maturity from 0 to 1.

- Rows 21-25: effective reuse strength, calculated as module maturity times the global reuse multiplier from Assumptions, capped at 1.

Connections:

- Depends on Assumptions.

- Feeds R&D\_Buckets, ReuseMatrix, and R&D\_NRE.

Detailed explanation:

The Platform sheet is the strategic core of the workbook. It represents the reusable engineering base that lets the company avoid building every product from scratch. Instead of treating AESA, EW/SIGINT, C-UAS, UAS, AUV/USV, and military AI as six unrelated businesses, the model assumes they share five technical modules:

- RF / Microwave: transmit/receive modules, receivers, antennas, GaN amplifiers, low-noise amplifiers, beamforming hardware, and RF front-end design.

- DSP / Signal Processing: FPGA pipelines, software-defined radio firmware, beamforming algorithms, real-time signal processing, and sensor-processing logic.

- Systems Engineering: mechanical, thermal, electrical, qualification, integration, MIL-STD compliance, verification, validation, and reliability engineering.

- Embedded & Mission Software: RTOS, mission computers, command-and-control interfaces, cybersecurity, mission workflows, and reusable software architecture.

- AI / ML: computer vision, sensor fusion, autonomy, target recognition, decision-support models, data pipelines, and MLOps.

Section A: Platform NRE investment by module

Rows 6-10 show annual investment in each shared module. This is the gross platform build cost. It is not tied to one product alone; it is the common engineering spend that multiple verticals can reuse.

In the saved workbook, the largest early platform investments are in Y1 and Y2. This reflects the business thesis: spend heavily upfront to create reusable capability, then taper the annual platform NRE as the modules mature. For example, RF, DSP, embedded software, and AI receive heavy early investment because those modules are reused across multiple verticals.

Row 11, Total platform NRE, sums the annual module investments. This feeds R&D\_NRE row 5 and is bucketed in R&D\_Buckets.

Row 12, Cumulative platform NRE, shows how much has been invested into the shared platform over time. This is useful for understanding how much technical asset base the company has built.

Section B: Platform module maturity

Rows 15-19 show maturity by module on a 0 to 1 scale. This is described as TRL-style maturity:

- 0 means immature or unavailable for reuse.

- 0.5 means partially reusable, but still risky or incomplete.

- 1.0 means fully reusable and mature.

The maturity curve is important because spending money on a module does not instantly make it reusable. A module becomes more valuable as it is tested, qualified, integrated, and proven in fielded products.

The maturity rows are also where the model captures different technology timelines. RF and DSP start with relatively high maturity because ESM/SIGINT is partly developed at Day 1. AI starts lower because autonomy and AI workflows mature over time. Systems engineering also ramps because defense qualification, test infrastructure, and integration know-how compound gradually.

Section C: Effective reuse strength

Rows 21-25 calculate the effective reuse strength for each module:

Effective reuse strength = module maturity x platform reuse maturity multiplier

The result is capped at 1.0. The multiplier comes from Assumptions!C26.

In the base case, the multiplier is 1.0, so effective reuse strength equals the maturity curve. If you wanted to run a conservative scenario, you could reduce the multiplier below 1.0. That would lower reuse savings in ReuseMatrix, increase vertical NRE, increase R&D/NRE expense, reduce EBITDA and FCF, and likely increase funding needs.

How the Platform sheet connects to ReuseMatrix

ReuseMatrix takes the effective reuse strength from Platform and applies it to each vertical's module composition.

Example:

- AESA radar is heavily RF/DSP-oriented.

- Military AI is heavily AI/software-oriented.

- MALE UAS and AUV/USV are more systems-engineering, software, and AI oriented.

So when RF and DSP maturity rises, AESA and EW/SIGINT benefit strongly. When AI and software maturity rises, C-UAS, UAS, autonomous maritime systems, and military AI benefit more.

The formula logic is:

Vertical reuse savings % = sum of each module weight x that module's effective reuse strength

For example, if a vertical is 45 percent RF and RF effective reuse strength is 70 percent, that RF component contributes 31.5 percentage points to that vertical's reuse savings.

How the Platform sheet affects the financial model

The platform sheet impacts the business in two opposite ways:

1. It increases early cost because the company spends large platform NRE before all products are generating revenue.

2. It reduces later cost because maturing modules lower vertical-specific NRE through reuse.

This is the main investment tradeoff in the workbook. The company accepts higher early cash burn in exchange for lower product-by-product development cost later.

Downstream effects:

- R&D\_Buckets: splits Platform NRE into research, capitalised development, and expensed/non-eligible development.

- R&D\_NRE: receives platform NRE directly and receives reduced vertical NRE indirectly through ReuseMatrix.

- P&L: R&D/NRE expense affects EBITDA; capitalized platform NRE later affects D&A.

- CashFlow: early platform investment and capitalized R&D reduce FCF.

- BalanceSheet: capitalized platform NRE becomes intangible assets and amortizes over time.

- KPIs: cumulative R&D/NRE, NRE avoided by reuse, EBITDA, FCF, NPV, and IRR all depend on how effective the platform becomes.

What to edit carefully:

- Edit rows 6-10 if the company spends more or less on shared platform modules.

- Edit rows 15-19 if module maturity is expected to ramp faster or slower.

- Edit Assumptions!C26 if you want a one-cell scenario lever for overall reuse effectiveness.

What not to change casually:

- Do not change the row structure without checking ReuseMatrix, because it directly references the effective reuse rows.

- Do not increase maturity to 1.0 too early unless there is a real technical reason. Overstating maturity will understate vertical NRE and make EBITDA/FCF look better than the operating plan can support.

Business interpretation:

The Platform sheet answers one question: how much reusable technical capability exists each year? The stronger and more mature the platform, the less the company needs to spend to launch each additional product line. This is why the model can support six verticals with a smaller NRE burden than a traditional prime contractor model.

### R&D\_Buckets

Purpose: investor-facing and audit-defensible accounting split for Platform R&D/NRE.

How it is built:

- Section A pulls module-level Platform NRE from Platform!D6:M10.

- Section B contains the Research - expensed % inputs by module and year.

- Section C contains the Development - capitalised % inputs by module and year.

- Section D calculates Development - expensed / not capitalisation eligible % as 1 - Research% - Capitalised%.

- Section E checks that all three bucket percentages sum to 100 percent for every module/year.

- Sections F-H calculate the rupee amount in each bucket.

- Section I produces financial-statement outputs: book-expensed Platform R&D, capitalised R&D additions, weighted capitalisation rate, amortisation, gross capitalised R&D, accumulated amortisation, net intangibles, and bucket checks.

- Section J shows the R&D tax bridge memo used by the P&L tax section.

Connections:

- Depends on Platform, Assumptions, R&D\_NRE, and P&L.

- Feeds R&D\_NRE rows 14, 16, 17, and 18.

- Feeds the new R&D accounting summary in KPIs.

Business interpretation:

This sheet replaces the old blanket 60 percent Platform NRE capitalisation assumption. It now recognises that early RF/AI exploration is more likely to be research and expensed, while later qualified engineering, software, hardening, and platform reuse work can have a higher capitalisation percentage if evidence supports it.

The three accounting buckets are:

- Research - expensed: concept work, early feasibility, exploratory design, and uncertain technical investigation. This reduces EBITDA immediately.

- Development - capitalised: qualifying development work that meets recognition criteria and creates reusable future economic benefit. This goes to intangibles and is amortised through D&A.

- Development - expensed / not capitalisation eligible: development-related spend that does not meet the book capitalisation evidence threshold. This is expensed immediately for book purposes.

Investor impact:

The new approach is stronger than a flat rate because it shows discipline. Investors can see that the model is not simply capitalising R&D to inflate EBITDA; it separates early research burn from qualifying platform IP creation.

Tax bridge:

Book accounting and tax treatment are separated. The P&L tax section keeps book PBT as the accounting base, then creates a tax-basis PBT by adding back book amortisation of capitalised R&D and deducting current-year eligible capitalised development R&D. This preserves the ability to model tax setoffs while keeping investor-facing book accounting compliant. The tax treatment remains subject to CA review.

Amortisation:

Capitalised development is amortised using a rolling straight-line schedule based on the amortisation life in Assumptions!C58. Each year's capitalised addition amortises over the selected life, starting in the year of capitalisation. Accumulated amortisation is capped at gross capitalised R&D so net intangibles cannot become negative.

Evidence needed:

- project-level time and cost tracking

- technical feasibility documentation

- approved development plan and budget

- evidence of intended use or sale

- expected future economic benefit

- resources to complete development

- reliable measurement of directly attributable costs

### ReuseMatrix

Purpose: converts shared platform maturity into vertical-specific NRE savings.

How it is built:

- Section A: module composition per vertical. Example: AESA is 45 percent RF, 25 percent DSP, 20 percent systems engineering, 8 percent software, 2 percent AI.

- Section B: effective reuse savings by vertical and year. Formula is the weighted sum of each vertical's module mix times the corresponding platform maturity.

- Section C: compares gross standalone NRE to leveraged NRE after reuse. Leveraged NRE = gross NRE x (1 - reuse savings).

- Section D: portfolio totals: gross vertical NRE, leveraged vertical NRE, reuse savings, platform NRE, total R&D/NRE.

Connections:

- Depends on Platform.

- Feeds R&D\_NRE and KPI counterfactual savings.

Important interpretation: NRE savings are counterfactual savings versus standalone development. They are not cash receipts.

### Assumptions

Purpose: global driver sheet.

How it is built: mostly input rows. Major drivers include tax rate, WACC, cost escalation, R&D salary escalation, BoM learning curve, DSO, DPO, inventory days, S&M/G&A rates, bank guarantee assumptions, MAT, currency conversion, revenue recognition lag, R&D amortization life, manufacturing overhead, and warranty.

Connections: feeds nearly every calculation-heavy sheet.

Most important rows:

- WACC: used for NPV.

- BoM learning curve and floor: drive declining BoM cost in V-sheets.

- DSO/DPO/inventory days: drive working capital in CashFlow and BalanceSheet.

- PBG, advance payment, BG fee, collateral: drive Backlog, Opex, restricted cash, and funding needs.

- Platform reuse multiplier: scales platform maturity in Platform.

- R&D amortization life: feeds R&D\_Buckets, R&D\_NRE, P&L, CashFlow, and BalanceSheet.

### V1\_AESA

Purpose: supporting unit economics for AESA radar.

How it is built: three product variants:

- X-band airborne.

- S-band ground surveillance.

- X-band naval multi-function.

Each variant has ASP/unit, BoM/unit, units shipped, revenue, BoM COGS, and contribution margin. ASP and BoM decline with learning-curve formulas from Assumptions. Totals roll up revenue, COGS, units, gross profit, margin, and cumulative revenue.

Connections:

- Depends on Assumptions.

- Feeds Revenue for BoM COGS scaling, not consolidated revenue directly.

Saved workbook snapshot: V1 shows 2 units and 52.0 INR Cr supporting revenue in Y1, rising to 95 units and 2,252.3 INR Cr supporting revenue by Y10, with Y10 gross margin around 65 percent.

### V2\_EW\_SIGINT

Purpose: supporting unit economics for electronic warfare and SIGINT.

How it is built: four variants:

- Naval ESM/ELINT suite.

- Aerial ESM pod.

- Tactical anti-drone jammer.

- Ground SIGINT station.

Same structure as V1, with ASP, BoM, units, revenue, COGS, contribution margin, and totals.

Connections:

- Depends on Assumptions.

- Feeds Revenue for BoM COGS scaling.

Saved workbook snapshot: V2 has the earliest revenue profile, with 167.0 INR Cr supporting revenue across 11 units in Y1 and 1,859.1 INR Cr across 123 units in Y10. Y10 gross margin is about 61 percent.

### V3\_CUAS

Purpose: supporting unit economics for counter-drone systems.

How it is built: three variants:

- Dismounted soldier kit.

- Vehicle-mounted system.

- Fixed-site integrated C-UAS.

ASP and BoM follow the same learning-curve logic as other V-sheets.

Connections:

- Depends on Assumptions.

- Feeds Revenue for COGS scaling.

Saved workbook snapshot: V3 supporting revenue grows from zero in Y1 to 1,449.9 INR Cr by Y10.

### V4\_UAS\_MALE

Purpose: supporting unit economics for MALE-class ISR UAS.

How it is built: three variants:

- MALE ISR baseline.

- MALE strike-capable.

- MALE SIGINT/EW mission variant.

This sheet reflects a later, larger-platform hardware program, with launch in Y4.

Connections:

- Depends on Assumptions.

- Feeds Revenue for COGS scaling.

Saved workbook snapshot: supporting revenue is zero in Y1 and 2,098.2 INR Cr by Y10.

### V5\_Autonomous

Purpose: supporting unit economics for maritime autonomous systems.

How it is built: three variants:

- Small AUV for mine-hunting/survey.

- Large ASW-capable AUV.

- Mid-size USV for ISR or C-UAS hosting.

Connections:

- Depends on Assumptions.

- Feeds Revenue for COGS scaling.

Saved workbook snapshot: supporting revenue is zero in Y1 and 1,171.1 INR Cr by Y10.

### V6\_MilAI

Purpose: supporting unit economics for military AI systems.

How it is built: three variants:

- Edge AI mission box.

- OIDSS license.

- Sensor-fusion middleware license.

This is the highest-margin vertical because BoM cost is low relative to software/license revenue.

Connections:

- Depends on Assumptions.

- Feeds Revenue for COGS scaling.

Saved workbook snapshot: V6 supporting revenue is 30.4 INR Cr in Y1 and 756.7 INR Cr in Y10. Gross margin is about 93 percent in Y1 and 94 percent in Y10.

### Revenue

Purpose: consolidated recognized revenue and BoM COGS by vertical.

How it is built:

- Rows 6-11: revenue by vertical, pulled cell-by-cell from Backlog!D89:M94 (one Backlog delivery row per vertical).

- Row 12: total consolidated revenue.

- Rows 15-20: revenue mix by vertical.

- Rows 23-28: BoM COGS by vertical, scaled from V-sheet COGS according to delivered revenue divided by V-sheet supporting revenue.

- Row 29: total consolidated BoM COGS.

- Rows 32-33: gross profit and gross margin before personnel COGS.

Connections:

- Depends on Backlog for revenue.

- Depends on V1-V6 for unit-economics COGS scaling.

- Feeds P&L.

Key point: edit Backlog delivery rates/bookings to change consolidated revenue.

### Backlog

Purpose: defense contract mechanics: bookings, backlog, delivery recognition, advances, bank guarantees, restricted cash.

How it is built:

- Section A (rows 6-11): target book-to-bill ratios.

- Section B (rows 13-18): Pwin assumptions.

- Section C (rows 20-26): bookings by vertical, with row 26 the consolidated total.

- Section D (rows 29-35): backlog roll-forward = opening backlog + bookings - recognized revenue.

- Section E (rows 38-40): consolidated book-to-bill, backlog coverage in months, and backlog growth Y/Y.

- Section F (rows 43-49): derived book-to-bill by vertical.

- Section G/advances block (rows 52-57): advance payment inflow, recognized revenue memo, contract-liability opening/amortization/closing, and net change in contract liability.

- Section I (rows 60-64): ABG, PBG, total guarantees outstanding, restricted cash collateral, and guarantee fee.

- Section K (rows 75-80): opening backlog by vertical.

- Section L (rows 82-87): delivery rate by vertical (default 0.5 for V1/V2, 0.33 for V3/V4, 0.25 for V5/V6).

- Rows 89-94: deliveries/revenue recognized by vertical. Row 95 sums them. The Revenue sheet pulls D89:M94.

Connections:

- Depends on Revenue for some checks.

- Depends on Assumptions for advance rates, PBG, BG fee, and collateral logic.

- Feeds Revenue, CashFlow, BalanceSheet, Opex, and KPIs.

Most important edit rows: bookings in rows 20-25 (one per vertical) and delivery rates in rows 82-87.

### Headcount

Purpose: staffing plan and fully loaded personnel costs.

How it is built:

- Section A: headcount by role.

- Section B: cost by role, escalated using salary escalation assumptions.

- Section C: personnel costs by category: R&D, COGS, S&M, and G&A.

Connections:

- Depends on Assumptions.

- Feeds R&D\_NRE for R&D personnel.

- Feeds P&L for COGS personnel, S&M personnel, and G&A personnel.

- Feeds KPIs for total headcount and revenue per employee.

### R&D\_NRE

Purpose: total R&D/NRE cost model, including platform NRE, vertical NRE after reuse, personnel, R&D buckets, capitalization, and amortization.

How it is built:

- Row 5: shared platform NRE from Platform.

- Row 6: leveraged vertical NRE from ReuseMatrix.

- Row 7: R&D personnel from Headcount.

- Row 8: memo gross standalone vertical NRE.

- Row 9: memo NRE avoided through platform reuse.

- Row 12: P&L R&D/NRE expense.

- Row 14: weighted Platform R&D capitalisation rate from R&D\_Buckets.

- Row 16: capitalised development additions from R&D\_Buckets.

- Row 17: book-expensed Platform R&D from R&D\_Buckets, including research and non-eligible development.

- Row 18: amortisation of capitalised R&D from R&D\_Buckets.

- Row 19: contingency memo.

Connections:

- Depends on Platform, ReuseMatrix, Headcount, and Assumptions.

- Feeds P&L, CashFlow, BalanceSheet, KPIs, and BreakEven.

Important accounting logic: research and non-eligible development are expensed immediately. Only qualifying development is capitalised, added to intangibles, and amortized through D&A. Contingency remains fully expensed by default.

### Capex

Purpose: capital expenditure and depreciation schedule.

How it is built:

- Section A: capex by asset item in INR lakhs, converted to INR Cr in totals.

- Section B: straight-line depreciation by asset life.

- Row 21: total gross capex.

- Row 39: total D&A from PP&E.

Connections:

- Feeds P&L D&A, CashFlow capex, BalanceSheet PP&E, KPIs, and BreakEven.

### Opex

Purpose: non-personnel operating expense model.

How it is built:

- Rows 6-20: fixed/semi-fixed operating expense lines such as facilities, cloud, licenses, travel, exhibitions, certifications, export control, cybersecurity, quality, insurance, legal, bid/proposal, recruiting, test ops, and contingency.

- Row 21: computed bank guarantee fees.

- Row 22: total non-personnel opex.

- Row 23: partner-lab usage credit memo.

Connections:

- Depends on Assumptions and Backlog.

- Feeds P&L other opex.

### P&L

Purpose: consolidated income statement.

How it is built:

- Revenue from Revenue.

- BoM COGS from Revenue.

- Personnel COGS from Headcount.

- R&D/NRE from R&D\_NRE.

- S&M and G&A from revenue percentages and/or personnel categories.

- Other opex from Opex.

- D&A from Capex plus capitalized R&D amortization from R&D\_NRE.

- Interest from Funding.

- Tax detail includes NOL utilization, MAT, and the R&D tax bridge.

Connections:

- Feeds KPIs, CashFlow, BalanceSheet, and BreakEven.

Saved workbook snapshot after the R&D bucket update: revenue grows from 52.5 INR Cr in Y1 to 5,055.3 INR Cr in Y10. EBITDA turns positive in Y4 (190.5 INR Cr) and reaches 2,347.1 INR Cr (46.4 percent margin) in Y10. Net income turns positive in Y4 and reaches 1,717.3 INR Cr in Y10.

### CashFlow

Purpose: converts earnings into cash flow, including defense working capital and restricted cash.

How it is built:

- CFO = net income + D&A - change in working capital + change in customer advances, with MAT credit adjustment.

- Working capital uses DSO, DPO, and inventory-day assumptions.

- CFI includes gross capex, change in restricted cash, and capitalized R&D additions from R&D\_Buckets.

- CFF pulls equity and debt flows from Funding.

- FCF = CFO + CFI.

- Cash balance = prior cash + FCF + CFF.

Connections:

- Depends on P&L, Assumptions, Backlog, Capex, R&D\_NRE, and Funding.

- Feeds KPIs, BalanceSheet, Funding, and BreakEven.

Saved workbook snapshot: peak cumulative FCF deficit is -1,061.8 INR Cr in Y3; cumulative FCF reaches 4,803.3 INR Cr by Y10. EoY cash balance grows from 110.1 INR Cr in Y1 to 5,903.3 INR Cr in Y10.

### BalanceSheet

Purpose: integrated balance sheet.

How it is built:

- Assets: cash, restricted cash, AR, inventory, MAT credit asset, PP&E, intangibles.

- Liabilities: AP, customer advances, venture debt.

- Equity: paid-in capital plus retained earnings.

- Check row verifies total assets equal liabilities plus equity.

- Ratio rows compute current ratio, debt/equity, ROIC, and CCC.

Connections:

- Depends on CashFlow, Backlog, P&L, Capex, R&D\_NRE, Funding, and Assumptions.

- Feeds KPIs.

Saved workbook snapshot: balance sheet check is zero in all years.

### Funding

Purpose: planned equity, venture debt, interest, financing cash flow, and minimum cash check.

How it is built:

- Equity rounds: Y1 round 450 INR Cr, Y2 round 400 INR Cr, Y3 round 250 INR Cr, totalling 1,100 INR Cr of paid-in capital. (The legacy label column on the Funding sheet still references older Seed/Series A/Series B sizing language, but the modelled cash inflows are 450/400/250.)

- iDEX / grant inflows are tracked as a memo row (1.5 INR Cr in Y1, 25 INR Cr in Y2) and are excluded from the relied-on financing plan.

- Venture debt: 8 percent interest. Draws total 200 INR Cr (20 in Y1, 100 in Y2, 80 in Y3). Repayments begin in Y5 and the balance is fully retired by Y9. Peak debt balance is 200 INR Cr in Y3-Y4.

- CFF: equity inflow plus net debt draw/repay.

- Min-cash compliance: compares projected ending cash from CashFlow to the 100 INR Cr target cash floor from Assumptions.

Connections:

- Depends on Assumptions and CashFlow.

- Feeds P&L, CashFlow, BalanceSheet, KPIs, and BreakEven.

Saved workbook snapshot: funding gap row is zero in all years after the planned rounds.

### BreakEven

Purpose: snapshot-year break-even and financial indicator summary.

How it is built:

- Cell C4 selects the snapshot year.

- Rows 8-14 use INDEX to pull revenue, BoM COGS, gross profit, GM percent, and units from V1-V6 for the selected year.

- Rows 17-23 pull fixed-cost stack from R&D\_NRE, P&L, and D&A.

- Row 27 calculates break-even revenue = fixed cost / weighted gross margin.

- Rows 30-40 summarize first positive EBITDA/FCF year, peak deficit, cumulative revenue/EBITDA/net income, NRE avoided, equity raised, peak debt, NPV, and IRR.

Connections:

- Depends on V1-V6, R&D\_NRE, P&L, CashFlow, Funding, and Assumptions.

Saved workbook snapshot: with snapshot year 6, weighted gross margin is 66.4 percent and annual break-even revenue is about 981.1 INR Cr against a total fixed-cost stack of 651.4 INR Cr. The same snapshot reports first EBITDA/FCF-positive year of Y4, peak cumulative cash deficit of -1,061.8 INR Cr, NPV of 747.2 INR Cr, and project IRR of 31.9 percent.

## Practical Editing Guide

To change revenue:

1. Edit Backlog bookings rows 20-25.

2. Edit Backlog delivery rates rows 82-87.

3. Review Revenue, P&L, CashFlow, and Funding.

To change product unit economics:

1. Edit V-sheet ASP, BoM, or unit assumptions.

2. Review Revenue BoM COGS scaling.

3. Review gross margins in P&L and BreakEven.

To change platform leverage:

1. Edit Platform NRE and maturity.

2. Edit module mix in ReuseMatrix if the vertical architecture changes.

3. Review R&D\_NRE and KPI NRE savings.

To change working capital/funding stress:

1. Edit Assumptions DSO, DPO, inventory days, advance rate, PBG, BG fee, and collateral.

2. Review Backlog, CashFlow, restricted cash, and Funding gap.

To change accounting treatment:

1. Edit R&D\_Buckets research and development capitalisation percentage inputs.

2. Edit Assumptions amortization life if the capitalised development asset life changes.

3. Review R&D\_NRE, P&L, CashFlow, BalanceSheet, and the R&D bucket KPI rows.

4. Recalculate the workbook in Excel or LibreOffice, because formula values must be refreshed after structural accounting changes.

