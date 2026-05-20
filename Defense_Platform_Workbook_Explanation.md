# Defense Platform Workbook Explanation

Source workbook: Defense\_Platform\_Business\_Plan\_Financial\_V2.xlsx

This workbook is a 10-year strategic and financial model for a platform-based defense technology company. Currency is INR crores (1 Cr = 10 million INR) unless a sheet explicitly says otherwise. The model is built around one shared engineering platform, six product verticals, defense-style backlog mechanics, and full three-statement financial reporting.

The company thesis is a new-age defence prime built on owned IP across six product verticals. All six are already designed; V2 EW/SIGINT is GSQR-compliant with a committed Rs 200 Cr iDEX MoQ for 10 airborne ESM units now in prototype trials. Capital is deployed against prototyping, qualification, and production line stand-up, not greenfield invention. Five reusable platform modules (RF, DSP, SysEng, Embedded/SW, AI/ML) compound R&D leverage across verticals.

## Model Flow

High-level dependency chain:

1. Assumptions defines global drivers: tax, WACC, working-capital days, learning curves, bank guarantees, MAT, R&D amortization life, manufacturing overhead, warranty.

2. Platform defines shared platform NRE investment and module maturity over 10 years.

3. R&D\_Buckets splits Platform NRE into research expensed, development capitalised, and development expensed / not eligible.

4. ReuseMatrix maps each vertical to the five shared platform modules and calculates how much vertical NRE is avoided through reuse.

5. V1\_AESA to V6\_MilAI contain supporting product-level unit economics: ASP, BoM, units, revenue, COGS, margins.

6. Backlog is the consolidated revenue engine. Bookings and opening backlog flow into deliveries. Deliveries become recognized revenue.

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

- TV: Terminal Value.

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

- TV: Terminal Value. TV captures the going-concern enterprise value beyond the modelled horizon. In this workbook it is computed both as a 12x Y10 EBITDA exit multiple and as a Gordon growth model perpetuity at g = 3%.

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

Purpose: narrative entry point and model map. It states the company thesis: a new-age defence prime built on owned IP across six product verticals, with five reusable platform modules (RF, DSP, SysEng, Embedded/SW, AI/ML) that compound R&D leverage across verticals.

How it is built: it has no formulas. It lists the company thesis, operating model, product verticals (with launch year and domain), core USP, planning horizon, color key, read order, and the V1 to V6 product table.

Connections: no formula dependencies. Use it as the workbook table of contents.

### KPIs

Purpose: executive dashboard.

How it is built: it pulls outputs from P&L, CashFlow, Backlog, Funding, Headcount, Capex, BalanceSheet, R&D\_NRE, and Assumptions.

Key outputs in the saved workbook:

- Year 10 revenue: 5,055.32 INR Cr.

- Year 10 EBITDA: 2,347.09 INR Cr (46.4% margin).

- 10-year cumulative FCF: 4,803.27 INR Cr.

- Project FCF IRR (10-year, excludes financing): 31.9 percent.

- NPV at WACC 18% (10-year FCF only, no TV): 747.15 INR Cr.

- First EBITDA-positive year: Y4 (190.46 INR Cr; 22% margin).

- First FCF-positive year: Y4 (+2.99 INR Cr).

- Total equity raised across the plan: 1,100 INR Cr (Y1 Seed 450, Y2 Series A 400, Y3 Series B 250).

- Peak debt balance: 200 INR Cr (Y3 to Y4); fully retired by Y9.

- Cumulative revenue (10 years): 21,209.23 INR Cr.

- Cumulative EBITDA (10 years): 8,100.05 INR Cr.

- Cumulative net income (10 years): 5,548.24 INR Cr.

- Cumulative R&D / NRE expense: 1,365.94 INR Cr; cumulative counterfactual NRE savings via platform reuse: 994.32 INR Cr (not realized cash).

- Total Capex (10 years): 600.12 INR Cr.

- Peak cumulative cash deficit: -1,061.78 INR Cr at end of Y3.

- Year 10 deployable cash: 5,903.27 INR Cr; total cash including restricted: 6,203.50 INR Cr.

Terminal Value and Equity Returns memo (KPIs sheet, lower block):

- Terminal Value at 12x Y10 EBITDA: 28,165.08 INR Cr.

- Terminal Value via Gordon growth (g = 3%, r = WACC 18%): 11,404.81 INR Cr.

- PV of TV at Y0 (12x case): 5,381.35 INR Cr.

- PV of TV at Y0 (Gordon case): 2,179.05 INR Cr.

- Equity NPV including TV (12x case): 6,128.50 INR Cr.

- Equity NPV including TV (Gordon case): 2,926.21 INR Cr.

- Workbook note: "IRR incl. TV not auto-computed; with PV of TV ~Rs 5 to 7K Cr against Rs 1,100 Cr deployed, IRR incl. TV typically jumps 8 to 12 percentage points vs 10-yr FCF-only IRR."

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

Rows 6-10 show annual investment in each shared module. Total platform NRE peaks in Y2 at 210 INR Cr (with AI/ML alone at 65 INR Cr in Y2), then tapers to 3.10 INR Cr in Y10. Cumulative platform NRE reaches 575.20 INR Cr by Y10. The largest early investments are in AI/ML, RF/Microwave, and Embedded Software, reflecting the business thesis: spend heavily upfront to create reusable capability, then taper annual platform NRE as the modules mature.

Section B: Platform module maturity

Rows 15-19 show maturity by module on a 0 to 1 scale. RF and DSP start with relatively high maturity (0.55 and 0.60 in Y1) because ESM/SIGINT is partly developed at Day 1. AI starts lower (0.25 in Y1) because autonomy and AI workflows mature over time. By Y10 all modules reach 0.99.

Section C: Effective reuse strength

Rows 21-25 calculate the effective reuse strength for each module:

Effective reuse strength = module maturity x platform reuse maturity multiplier

The result is capped at 1.0. The multiplier comes from Assumptions!C26 (base case = 1.0).

How the Platform sheet connects to ReuseMatrix:

ReuseMatrix takes the effective reuse strength from Platform and applies it to each vertical's module composition. For example, AESA is 45% RF and 25% DSP, so it benefits strongly when RF and DSP mature. Military AI is 60% AI and 25% software, so it benefits when the AI module matures.

The formula logic is: Vertical reuse savings % = sum of (module weight x module effective reuse strength).

How the Platform sheet affects the financial model:

The platform increases early cost (heavy platform NRE before all products are generating revenue) and reduces later cost (mature modules lower vertical-specific NRE through reuse). This is the main investment tradeoff in the workbook.

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

- Feeds the R&D accounting summary in KPIs.

Weighted Platform R&D capitalisation rate from the saved workbook: Y1=26%, Y2=42%, Y3=55%, Y4=63%, Y5=68%, Y6=71%, Y7=74%, Y8=75%, Y9=75%, Y10=73%.

Business interpretation:

This sheet replaces the older blanket 60% Platform NRE capitalisation assumption. It now recognises that early RF/AI exploration is more likely to be research and expensed, while later qualified engineering, software, hardening, and platform reuse work can have a higher capitalisation percentage if evidence supports it.

The three accounting buckets are:

- Research - expensed: concept work, early feasibility, exploratory design, and uncertain technical investigation. This reduces EBITDA immediately.

- Development - capitalised: qualifying development work that meets recognition criteria and creates reusable future economic benefit. This goes to intangibles and is amortised through D&A.

- Development - expensed / not capitalisation eligible: development-related spend that does not meet the book capitalisation evidence threshold. This is expensed immediately for book purposes.

Amortisation: Capitalised development is amortised using a rolling straight-line schedule based on the amortisation life in Assumptions!C58 (6 years). Each year's capitalised addition amortises over the selected life, starting in the year of capitalisation. Accumulated amortisation is capped at gross capitalised R&D so net intangibles cannot become negative.

Tax bridge: Book accounting and tax treatment are separated. The P&L tax section keeps book PBT as the accounting base, then creates a tax-basis PBT by adding back book amortisation of capitalised R&D and deducting current-year eligible capitalised development R&D. This preserves the ability to model tax setoffs while keeping investor-facing book accounting compliant. The tax treatment remains subject to CA review.

### ReuseMatrix

Purpose: converts shared platform maturity into vertical-specific NRE savings.

How it is built:

- Section A: module composition per vertical. AESA = 45% RF, 25% DSP, 20% SysEng, 8% SW, 2% AI. EW/SIGINT = 40% RF, 30% DSP, 15% SysEng, 10% SW, 5% AI. C-UAS = 25% RF, 20% DSP, 15% SysEng, 15% SW, 25% AI. MALE UAS = 5% RF, 10% DSP, 40% SysEng, 25% SW, 20% AI. Autonomous = 5% RF, 10% DSP, 35% SysEng, 25% SW, 25% AI. Mil AI = 0% RF, 10% DSP, 5% SysEng, 25% SW, 60% AI.

- Section B: effective reuse savings by vertical and year. Formula is the weighted sum of each vertical's module mix times the corresponding platform maturity.

- Section C: compares gross standalone NRE to leveraged NRE after reuse. Leveraged NRE = gross NRE x (1 - reuse savings).

- Section D: portfolio totals: gross vertical NRE, leveraged vertical NRE, reuse savings, platform NRE, total R&D/NRE.

Reuse savings by vertical at Y1 versus Y10 (effective reuse savings %): AESA 0.52 to 0.99, EW/SIGINT 0.52 to 0.99, C-UAS 0.46 to 0.99, MALE UAS 0.42 to 0.99, Autonomous 0.41 to 0.99, Mil AI 0.35 to 0.99.

Connections:

- Depends on Platform.

- Feeds R&D\_NRE and KPI counterfactual savings.

Important interpretation: NRE savings are counterfactual savings versus standalone development. They are not cash receipts.

### Assumptions

Purpose: global driver sheet.

How it is built: mostly input rows. Major drivers include tax rate (25%), WACC (18%), cost escalation (4% annual), R&D salary escalation (4% annual, reduced from a legacy 12% which was unsustainable over 10 years), BoM learning curve (0.92 per doubling), BoM floor (70% of starting BoM), DSO (180 days), DPO (45 days), inventory days (90), S&M (8% of revenue), G&A (7%), Bid & Proposal (3%), PBG (3%), advance payment rate (15%), BG fee (1% annual, reduced from 1.5% given Rs 150 Cr land/factory collateral), cash collateral schedule (Y1-Y2 100%, Y3 50%, Y4 30%, Y5-Y10 20%), min cash reserve target (100 INR Cr), platform reuse maturity multiplier (1.0 base), MAT rate (15%), USD/INR (95), revenue recognition lag (12-15 months for HW), R&D amortization life (6 years), manufacturing overhead (20% of direct material + labour), warranty (2% of COGS).

Connections: feeds nearly every calculation-heavy sheet.

Most important rows for stress-testing:

- WACC (C7): used for NPV.

- BoM learning curve and floor: drive declining BoM cost in V-sheets.

- DSO/DPO/inventory days: drive working capital in CashFlow and BalanceSheet.

- PBG, advance payment, BG fee, collateral: drive Backlog, Opex, restricted cash, and funding needs.

- Platform reuse multiplier (C26): scales platform maturity in Platform.

- R&D amortization life (C58): feeds R&D\_Buckets, R&D\_NRE, P&L, CashFlow, and BalanceSheet.

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

This sheet reflects a later, larger-platform hardware program.

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

Consolidated recognized revenue from the saved workbook (INR Cr): Y1=52.50, Y2=203.41, Y3=491.03, Y4=855.20, Y5=1,447.70, Y6=2,180.23, Y7=2,883.85, Y8=3,659.34, Y9=4,380.66, Y10=5,055.32. Y/Y growth: 287% in Y2, 141% in Y3, 74% in Y4, decelerating to 15% in Y10.

Connections:

- Depends on Backlog for revenue.

- Depends on V1-V6 for unit-economics COGS scaling.

- Feeds P&L.

Key point: edit Backlog delivery rates/bookings to change consolidated revenue.

### Backlog

Purpose: defense contract mechanics: bookings, backlog, delivery recognition, advances, bank guarantees, restricted cash.

How it is built:

- Section A (rows 6-11): target book-to-bill ratios per vertical.

- Section B (rows 13-18): Pwin assumptions per vertical.

- Section C (rows 20-26): bookings by vertical, with row 26 the consolidated total.

- Section D (rows 29-35): backlog roll-forward = opening backlog + bookings - recognized revenue.

- Section E (rows 38-40): consolidated book-to-bill (9.10x in Y1, 1.41x in Y10), backlog coverage in months (97.16 in Y1, 39.59 in Y10), and backlog growth Y/Y.

- Section F (rows 43-49): derived book-to-bill by vertical.

- Section G/advances block (rows 52-57): advance payment inflow, recognized revenue memo, contract-liability opening/amortization/closing, and net change in contract liability.

- Section I (rows 60-64): ABG, PBG, total guarantees outstanding (76.51 in Y1, 3,002.35 in Y10), restricted cash collateral (7.65 in Y1, 300.24 in Y10), and guarantee fee (0.84 in Y1, 33.03 in Y10).

- Section K (rows 75-80): opening backlog by vertical.

- Section L (rows 82-87): delivery rate by vertical (default 0.5 for V1/V2, 0.33 for V3/V4, 0.25 for V5/V6).

- Rows 89-94: deliveries/revenue recognized by vertical. Row 95 sums them. The Revenue sheet pulls D89:M94.

Closing backlog (consolidated) from the saved workbook (INR Cr): Y1=425.06, Y2=1,127.82, Y3=2,129.67, Y4=3,793.63, Y5=5,888.30, Y6=7,977.66, Y7=10,298.86, Y8=12,516.93, Y9=14,620.82, Y10=16,679.74.

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

Total headcount from the saved workbook (EoY): Y1=91, Y2=156, Y3=216, Y4=287, Y5=349, Y6=414, Y7=475, Y8=506, Y9=530, Y10=543. Revenue per employee: Y1=0.58, Y10=9.31 INR Cr.

Connections:

- Depends on Assumptions.

- Feeds R&D\_NRE for R&D personnel.

- Feeds P&L for COGS personnel, S&M personnel, and G&A personnel.

- Feeds KPIs for total headcount and revenue per employee.

### R&D\_NRE

Purpose: total R&D/NRE cost model, including platform NRE, vertical NRE after reuse, personnel, R&D buckets, capitalization, and amortization.

How it is built:

- Row 5: shared platform NRE from Platform (Y1=101, Y2=210 peak, Y10=3.10 INR Cr).

- Row 6: leveraged vertical NRE from ReuseMatrix (Y1=141.83, Y10=0.09 INR Cr).

- Row 7: R&D personnel from Headcount (Y1=12.51, Y10=66.77 INR Cr).

- Row 8: memo gross standalone vertical NRE (counterfactual reference).

- Row 9: memo NRE avoided through platform reuse.

- Row 12: P&L R&D/NRE expense (Y1=301.94, Y2=347.81 peak, Y3=185.22, Y4=118.02, Y5=80.59, Y6=66.91, Y10=68.64).

- Row 14: weighted Platform R&D capitalisation rate from R&D\_Buckets.

- Row 16: capitalised development additions from R&D\_Buckets.

- Row 17: book-expensed Platform R&D from R&D\_Buckets.

- Row 18: amortisation of capitalised R&D from R&D\_Buckets.

- Row 19: contingency memo (30% uplift for realistic AESA/MALE/AUV costs).

Connections:

- Depends on Platform, ReuseMatrix, Headcount, and Assumptions.

- Feeds P&L, CashFlow, BalanceSheet, KPIs, and BreakEven.

Important accounting logic: research and non-eligible development are expensed immediately. Only qualifying development is capitalised, added to intangibles, and amortized through D&A. Contingency remains fully expensed by default.

### Capex

Purpose: capital expenditure and depreciation schedule.

How it is built:

- Section A: capex by asset item in INR lakhs, converted to INR Cr in totals.

- Section B: straight-line depreciation by asset life.

- Row 21: total gross capex (Y1=35.45, peaking at Y4=135.70, Y10=22.80; total 10-year = 600.12 INR Cr).

- Row 39: total D&A from PP&E (Y1=5.40, Y10=44.10 INR Cr).

Major capex items: anechoic chamber and near-field range (15-year life), cleanroom for SMT/GaN packaging, SMT assembly line, HALT/HASS chambers, EMI/EMC test cell (MIL-STD-461), RF/EW lab bench, FPGA/compute dev stations, GPU cluster for AI training, UAS flight test range/hangar, maritime test tank/subsea range, office build-out, IT/classified network, mobile demo platforms.

Connections:

- Feeds P&L D&A, CashFlow capex, BalanceSheet PP&E, KPIs, and BreakEven.

### Opex

Purpose: non-personnel operating expense model.

How it is built:

- Rows 6-20: fixed/semi-fixed operating expense lines such as facilities (1.43 INR Cr in Y1 to 8.08 in Y10), cloud/compute (1.33 to 20.62), software licenses including CAD/EDA/HFSS/MATLAB (3.42 to 18.81), travel and demos, exhibitions (DSEI, AUSA), certifications (DO-178, DO-254, AS9100), ITAR/Export Control, Cybersecurity/CMMC L3, Quality/CMMI/AS9100, insurance (product liability, E&O), legal/IP, B&P direct costs, recruiting/training, range/flight test ops, contingency.

- Row 21: computed bank guarantee fees.

- Row 22: total non-personnel opex (Y1=41.70, Y10=203.32 INR Cr).

- Row 23: partner-lab usage credit memo.

Connections:

- Depends on Assumptions and Backlog.

- Feeds P&L other opex.

### P&L

Purpose: consolidated income statement.

How it is built:

- Revenue from Revenue.

- BoM COGS from Revenue (Y1=23.46, Y10=1,631.43 INR Cr).

- Personnel COGS from Headcount (Y1=2.03, Y10=46.54 INR Cr).

- R&D/NRE from R&D\_NRE.

- S&M and G&A from revenue percentages and/or personnel categories (S&M: Y1=4.20, Y10=404.43; G&A: Y1=3.67, Y10=353.87 INR Cr).

- Other opex from Opex.

- D&A from Capex plus capitalized R&D amortization from R&D\_NRE (Y1=9.77, peaks Y6=92.69, Y10=54.56 INR Cr).

- Interest from Funding (Y1=0.80, peak Y4=16, Y10=0 INR Cr).

- Tax detail includes NOL utilization, MAT, and the R&D tax bridge.

Connections:

- Feeds KPIs, CashFlow, BalanceSheet, and BreakEven.

Saved workbook snapshot:

- Revenue: 52.50 (Y1) to 5,055.32 (Y10) INR Cr.

- EBITDA: -324.50 (Y1) to -316.78 (Y2) to -22.80 (Y3) to +190.46 (Y4 first positive) to 2,347.09 (Y10), 46.4% margin.

- Net income: -335.07 (Y1) to -355.71 (Y2) to -91.42 (Y3) to +99.49 (Y4 first positive) to 1,717.35 (Y10).

- Tax: zero through Y5 (NOL pool absorbs taxable income); MAT credit asset peaks at 89.81 INR Cr in Y6 then unwinds.

### CashFlow

Purpose: converts earnings into cash flow, including defense working capital and restricted cash.

How it is built:

- CFO = net income + D&A - change in working capital + change in customer advances, with MAT credit adjustment.

- Working capital uses DSO (180), DPO (45), and inventory-day (90) assumptions.

- CFI includes gross capex, change in restricted cash, and capitalized R&D additions from R&D\_Buckets.

- CFF pulls equity and debt flows from Funding.

- FCF = CFO + CFI.

- Cash balance = prior cash + FCF + CFF.

Connections:

- Depends on P&L, Assumptions, Backlog, Capex, R&D\_NRE, and Funding.

- Feeds KPIs, BalanceSheet, Funding, and BreakEven.

Saved workbook snapshot: peak cumulative FCF deficit is -1,061.78 INR Cr in Y3; FCF turns positive in Y4 (+2.99) and grows to 1,660.89 INR Cr by Y10. Cumulative FCF reaches 4,803.27 INR Cr by Y10. EoY deployable cash balance grows from 110.08 INR Cr in Y1 to 5,903.27 INR Cr in Y10. Min cash compliance check is OK in all years.

### BalanceSheet

Purpose: integrated balance sheet.

How it is built:

- Assets: cash, restricted cash, AR (DSO-driven), inventory (inv-days driven), MAT credit asset, gross PP&E less accumulated depreciation, net intangibles (capitalized R&D less accumulated amortization).

- Liabilities: AP (DPO-driven), customer advances (contract liabilities), venture debt.

- Equity: paid-in capital plus retained earnings.

- Check row verifies total assets equal liabilities plus equity (zero in all years).

- Ratio rows compute current ratio, debt/equity, ROIC, and CCC.

Connections:

- Depends on CashFlow, Backlog, P&L, Capex, R&D\_NRE, Funding, and Assumptions.

- Feeds KPIs.

Saved workbook snapshot: balance sheet check is zero in all years. TOTAL ASSETS grow from 201.83 INR Cr (Y1) to 9,357.08 INR Cr (Y10). Equity grows from 114.93 (Y1) to 6,648.24 INR Cr (Y10).

### Funding

Purpose: planned equity, venture debt, interest, financing cash flow, and minimum cash check.

How it is built:

- Equity rounds: Y1 Seed 450 INR Cr, Y2 Series A 400 INR Cr, Y3 Series B 250 INR Cr, totalling 1,100 INR Cr of paid-in capital.

- iDEX / grant inflows are tracked as a memo row (1.5 INR Cr in Y1, 25 INR Cr in Y2) and are explicitly excluded from the relied-on financing plan.

- Venture debt: 8 percent interest. Draws total 200 INR Cr (Y1 20, Y2 100, Y3 80). Repayments begin in Y5 (36), continue Y6 (36), Y7 (55), Y8 (65), Y9 (8). Balance fully retired by Y9. Peak debt balance is 200 INR Cr in Y3-Y4.

- CFF: equity inflow plus net debt draw/repay (Y1=470, Y2=500, Y3=330, Y4=0, Y5 onward negative as debt is repaid).

- Min-cash compliance: compares projected ending cash from CashFlow to the 100 INR Cr target cash floor from Assumptions. Funding gap is zero in all years.

- Memo: pre-plan facilities include Rs 150 Cr land/factory collateral, Rs 12.5 Cr WC limit (utilised), Rs 18.5 Cr ABG sanctioned (covers Y1 ABG of Rs 18.76 Cr), Rs 9 Cr TL approved.

Connections:

- Depends on Assumptions and CashFlow.

- Feeds P&L, CashFlow, BalanceSheet, KPIs, and BreakEven.

### BreakEven

Purpose: snapshot-year break-even and financial indicator summary.

How it is built:

- Cell C4 selects the snapshot year (default = 6).

- Rows 8-14 use INDEX to pull revenue, BoM COGS, gross profit, GM percent, and units from V1-V6 for the selected year.

- Rows 17-23 pull fixed-cost stack from R&D\_NRE, P&L, and D&A.

- Row 27 calculates break-even revenue = fixed cost / weighted gross margin.

- Rows 30-40 summarize first positive EBITDA/FCF year, peak deficit, cumulative revenue/EBITDA/net income, NRE avoided, equity raised, peak debt, NPV, and IRR.

Connections:

- Depends on V1-V6, R&D\_NRE, P&L, CashFlow, Funding, and Assumptions.

Saved workbook snapshot (Y6 basis): weighted gross margin 66%; total fixed-cost stack 651.44 INR Cr; break-even annual revenue 981.07 INR Cr. First EBITDA-positive year Y4 (190.46 INR Cr), first FCF-positive year Y4 (+2.99 INR Cr), peak cumulative cash deficit -1,061.78 INR Cr, NPV 747.15 INR Cr, project IRR 31.9%.

## Detailed Topical Walkthroughs

The walkthroughs that follow expand on the four most consequential topics in the model: how backlog converts into recognized revenue and cash, how the balance sheet integrates the three statements, how the funding plan covers the cash trough, and how break-even and NPV are computed. Each walkthrough is self-contained and intended to be readable without reference to the underlying sheets.

### Backlog and Cash Flow Projections - Detailed Walkthrough

#### Booking-to-Revenue Mechanics in Defense

Defense businesses do not convert orders to revenue the way commercial software or services firms do. A signed contract enters the books as a **booking** (an order award with binding scope and price), then sits in **backlog** until physical milestones - prototype acceptance, FAT, SAT, lot delivery, integration sign-off - release tranches into **recognized revenue**. The gap between the booking date and the revenue date is the defining feature of the working-capital profile in this plan, and it is what creates the trough-to-positive FCF arc described later in this section.

The model treats this lag explicitly with three linked statements:

- **Opening backlog** carried from the prior year-end.
- **Plus new bookings** awarded in the current year.
- **Less recognized revenue** (a vertical-specific percentage of opening backlog).
- **Equals closing backlog** carried into the next year.

This is not a black-box assumption. Each vertical has its own delivery cadence reflecting how that programme type actually executes in Indian defence procurement, and revenue only flows after a contractually defined acceptance event.

#### Bookings Strategy by Vertical

The bookings ramp is engineered around a deliberate sequencing: anchor the early years with vertical V2 (EW and SIGINT) where existing customer relationships and the iDEX MoQ-backed prototype trials shorten the sales cycle, then layer in V1 (AESA Radar), V3 (Counter-UAS), V4 (MALE-class ISR UAS), V5 (Autonomous AUV/USV), and V6 (Military AI) as platform credibility compounds.

| Year | V1 AESA | V2 EW/SIGINT | V3 C-UAS | V4 MALE UAS | V5 AUV/USV | V6 Mil AI | Total |
|------|--------:|-------------:|---------:|------------:|-----------:|----------:|------:|
| Y1 | 100.00 | 341.07 | 0.00 | 0.00 | 0.00 | 36.48 | **477.56** |
| Y2 | 200.00 | 386.51 | 73.39 | 100.00 | 75.81 | 70.46 | **906.17** |
| Y3 | 287.10 | 408.89 | 273.70 | 250.00 | 144.95 | 128.24 | **1,492.88** |
| Y4 |  |  |  |  |  |  | **2,519.16** |
| Y5 |  |  |  |  |  |  | **3,542.37** |
| Y6 |  |  |  |  |  |  | **4,269.59** |
| Y7 |  |  |  |  |  |  | **5,205.04** |
| Y8 |  |  |  |  |  |  | **5,877.41** |
| Y9 |  |  |  |  |  |  | **6,484.56** |
| Y10 |  |  |  |  |  |  | **7,114.24** |

Key structural points:

- **V2 (EW/SIGINT) anchors Y1 to Y3.** It contributes 71% of Y1 bookings (341.07 of 477.56 INR Cr) and remains the single largest contributor through Y3. This reflects an ESM Pwin assumption held flat at **0.40** across the horizon - a customer-relationships premium justified by the Rs 200 Cr iDEX MoQ already won (10 airborne ESM units in prototype trials), where the incumbent has both the drawings and the spares-pool to bid credibly.
- **V1 (AESA Radar) builds steadily** as X-band airborne, S-band ground surveillance, and X-band naval multi-function variants reach qualification. Pwin ramps **0.25 to 0.35** as the qualification base accumulates.
- **V4 (MALE-class ISR UAS) is the highest-ticket vertical** but enters only in Y2 once the airframe, payload, and SATCOM integration paths are visible to the customer. Its Pwin ramps **0.20 to 0.35** - the lowest starting point of the six. Single-contract values are large, which is why the V4 book-to-bill stays elevated.
- **V3 (Counter-UAS), V5 (Autonomous AUV/USV), and V6 (Military AI)** ramp from 0.22 to 0.30 starting Pwin to 0.35 as the threat environment institutionalises demand and the company's first systems graduate from trials.

Total bookings grow at a ~30% CAGR across the ten years (477.56 INR Cr in Y1 to 7,114.24 INR Cr in Y10), and the **share of V2 in total bookings declines from 71% to a much smaller fraction** as the higher-growth verticals scale.

#### Book-to-Bill Trajectory: From 9.1x to 1.41x

Book-to-bill (B:B = new bookings divided by recognized revenue in the same year) is the cleanest single signal of whether a defense company is in build-up, steady-state, or harvest mode.

| Year | B:B Ratio | Stage |
|------|----------:|-------|
| Y1 | 9.10x | Order-stacking; almost no deliveries yet |
| Y2 | 4.45x | Heavy booking, early deliveries on V1 / V2 |
| Y3 | 3.04x | Backlog still compounding faster than burn |
| Y4 | 2.95x | First year of meaningful FCF crossover |
| Y5 | 2.45x | Multi-vertical execution at scale |
| Y6 | 1.96x | Approaching mature defence prime ratio (1.5 to 2.0x) |
| Y7 | 1.80x |  |
| Y8 | 1.61x |  |
| Y9 | 1.48x |  |
| Y10 | 1.41x | Steady-state maturity |

A B:B above 1.0x means the order book is growing faster than revenue, which is the right shape for a company building scale; a B:B below 1.0x would signal contraction. The Y10 ratio of 1.41x is consistent with mature global defence primes (Lockheed, BAE, Thales) which typically sit in the 1.1 to 1.6x range.

The corresponding **closing backlog** compounds from **425.06 INR Cr at Y1 EoY to 16,679.74 INR Cr at Y10 EoY**, a ~39x expansion. Backlog coverage (closing backlog expressed in months of current-year revenue) starts at an extreme 97.16 months in Y1 and stabilises at roughly **39 to 53 months** in Y6 to Y10, which is the normal range for a defence prime executing multi-year platform contracts.

#### Delivery Rate Logic by Vertical

Revenue recognition is not modelled as a percentage of bookings but as a **percentage of opening backlog**, with rates that are constant across all ten years (and explicitly tied to programme physics):

| Vertical | Delivery Rate | Implied Avg Programme Life | Rationale |
|----------|--------------:|---------------------------:|-----------|
| V1 (AESA Radar) | 50% | ~2 years | X/S-band hardware delivered in lots within 18 to 24 months of contract |
| V2 (EW / SIGINT) | 50% | ~2 years | Defined GSQR drawings, predictable bench-level work, fast delivery |
| V3 (Counter-UAS) | 33% | ~3 years | System integration plus site rollout phases |
| V4 (MALE UAS) | 33% | ~3 years | Long airframe + payload integration cycle, FAT/SAT staging |
| V5 (AUV / USV) | 25% | ~4 years | Trials, sea acceptance, production qualification |
| V6 (Military AI) | 25% | ~4 years | Software-defined payloads, repeated certification cycles |

These rates are **deliberately conservative** for the longer-cycle verticals (V5, V6). Recognized revenue therefore grows from **52.50 INR Cr in Y1 to 5,055.32 INR Cr in Y10**, lagging bookings by exactly the duration profile above.

#### Cash Flow Waterfall

Three independent streams combine to produce free cash flow:

| Year | CFO | CFI | CFF | FCF | Cumulative FCF |
|------|----:|----:|----:|----:|---------------:|
| Y1 | (290.57) | (69.35) | 470.00 | (359.92) | (359.92) |
| Y2 | (298.81) | (168.92) | 500.00 | (467.73) | (827.66) |
| Y3 | (38.73) | (195.39) | 330.00 | (234.13) | (1,061.78) |
| Y4 | 211.98 | (208.99) | 0.00 | 2.99 | (1,058.79) |
| Y5 | 423.60 | (158.07) | (36.00) | 265.53 | (793.25) |
| Y6 | 671.31 | (99.34) | (36.00) | 571.97 | (221.28) |
| Y7 | 995.93 | (70.10) | (55.00) | 925.83 | 704.55 |
| Y8 | 1,147.52 | (75.69) | (65.00) | 1,071.83 | 1,776.38 |
| Y9 | 1,438.97 | (72.98) | (8.00) | 1,365.99 | 3,142.37 |
| Y10 | 1,723.03 | (62.13) | 0.00 | 1,660.89 | 4,803.27 |

- **CFO** absorbs the working-capital build during Y1 to Y3 and turns positive in Y4 once recognized revenue passes the working-capital deployment rate.
- **CFI** is heaviest in Y2 to Y4 (factory build-out, test ranges, tooling for V4/V5/V6) before tapering.
- **CFF** carries the 1,100 INR Cr equity raise and 200 INR Cr debt drawdown across Y1 to Y3, then flips negative from Y5 as the company begins amortising senior debt.

FCF (CFO + CFI, cash available before financing decisions) is the load-bearing line for the investor case.

#### Working Capital Dynamics

The single largest cash consumer in the early years is working capital. The model uses constant operating cycle assumptions:

- **DSO: 180 days.** Blended: iDEX/Make-II ~90 to 120 days, MoD CapEx ~240 to 365 days, export ~120 days.
- **DPO: 45 days.** Supplier terms net-45 typical for cleared vendors.
- **Inventory: 90 days.** Long-lead RF/FPGA components offset by JIT mission-SW and VMI arrangements.
- **Cash Conversion Cycle: 225 days** (DSO + Inv days - DPO), constant by construction.

| Year | NWC EoY (INR Cr) | Annual Change in WC (cash deployed) |
|------|-----------------:|------------------------------------:|
| Y1 | 29.03 | 29.03 |
| Y2 | 110.87 | 81.84 |
| Y3 | 264.29 | 153.41 |
| Y4 | 461.44 | 197.15 |
| Y5 | 779.15 | 317.71 |
| Y6 | 1,170.29 | 391.15 |
| Y7 | 1,545.26 | 374.97 |
| Y8 | 1,958.55 | 413.29 |
| Y9 | 2,342.18 | 383.63 |
| Y10 | 2,699.91 | 357.72 |

By Y10, **2,493.03 INR Cr is tied up in receivables**, **413.75 INR Cr in inventory**, against only **206.87 INR Cr in payables**. Net working capital of 2,699.91 INR Cr is roughly 53% of Y10 revenue - a structural feature of Indian defence revenue, not a sign of operational inefficiency.

#### Customer Advances as a Partial Offset

The plan offsets a portion of the working-capital drag through **mobilization advances** (15% of new bookings). These sit on the balance sheet as **contract liabilities** and unwind into revenue as deliveries are made.

| Year | Contract Liability EoY (INR Cr) | Net Change (Inflow to CFO) |
|------|--------------------------------:|---------------------------:|
| Y1 | 63.76 | 63.76 |
| Y2 | 169.17 | 105.41 |
| Y3 | 319.45 | 150.28 |
| Y4 | 569.04 | 249.59 |
| Y5 | 883.24 | 314.20 |
| Y6 | 1,196.65 | 313.41 |
| Y7 | 1,544.83 | 348.18 |
| Y8 | 1,877.54 | 332.71 |
| Y9 | 2,193.12 | 315.58 |
| Y10 | 2,501.96 | 308.84 |

The net change in contract liability flows to CFO each year. This is one of the few structural cash benefits of defence procurement and the model captures it explicitly rather than burying it in "other current liabilities".

#### Restricted Cash for Bank Guarantees

Every defence contract in India requires a **Performance Bank Guarantee (PBG)** (3% of contract value in this plan) plus an **Advance Bank Guarantee (ABG)** equal in value to any mobilization advance taken. The model treats the cash supporting these BGs as **restricted** (held in fixed-deposit lien) and excludes it from deployable cash.

Two design choices reduce the cash impact:

1. **The collateral schedule tapers over time.** Y1 to Y2 require 100% cash collateral; Y3 drops to 50%, Y4 to 30%, and Y5 onwards holds at 20%. This is consistent with real practice at relationship banks once the company has demonstrated repeat performance.
2. **BG issuance fee is set at 1.0% per annum** (reduced from the more typical 1.5%) because the Rs 150 Cr land and factory asset on the balance sheet provides the issuing bank with physical security beyond the cash collateral.

| Year | Total BG Outstanding (INR Cr) | Restricted Cash EoY (INR Cr) | BG Fee (INR Cr) |
|------|------------------------------:|-----------------------------:|----------------:|
| Y1 | 76.51 | 7.65 | 0.84 |
| Y2 | 203.01 | 20.30 | 2.23 |
| Y3 | 383.34 | 38.33 | 4.22 |
| Y4 | 682.85 | 68.29 | 7.51 |
| Y5 | 1,059.89 | 105.99 | 11.66 |
| Y6 | 1,435.98 | 143.60 | 15.80 |
| Y7 | 1,853.79 | 185.38 | 20.39 |
| Y8 | 2,253.05 | 225.30 | 24.78 |
| Y9 | 2,631.75 | 263.17 | 28.95 |
| Y10 | 3,002.35 | 300.24 | 33.03 |

The PBG itself is sized at 3% of closing backlog, so the BG line scales with backlog rather than revenue. By Y10, BG capacity outstanding is 3,002.35 INR Cr, but the restricted-cash drag is only 300.24 INR Cr - the rest is covered by the bank against the company's banking limits and physical collateral.

#### The Trough Year and FCF Inflection

The cumulative FCF curve moves through three regimes:

1. **Cash consumption (Y1 to Y3):** Cumulative FCF declines from -359.92 INR Cr in Y1 to a peak deficit of **-1,061.78 INR Cr in Y3**. Every line item works against cash in these years - heavy working-capital deployment, peak capex, restricted cash building against initial BGs, and recognized revenue still well below run-rate cost.
2. **Inflection (Y4):** Recognized revenue (855.20 INR Cr) finally outpaces the absolute level of working-capital deployment plus capex, and **FCF turns marginally positive at +2.99 INR Cr**. This is the operational crossover point. Cumulative FCF still sits at -1,058.79 INR Cr at this point, so the deficit has not yet been recovered.
3. **Cash accumulation (Y5 onwards):** From Y5, FCF compounds rapidly. **Cumulative FCF crosses zero between Y6 and Y7** (Y6 ends at -221.28; Y7 ends at +704.55), meaning the business has fully repaid its cumulative cash deficit and is now in net cash-generation territory.

#### Year-10 Cash Position

By the end of Y10, the company holds:

- **Deployable cash on balance sheet: 5,903.27 INR Cr** (unrestricted ending cash balance).
- **Restricted cash supporting BGs: 300.24 INR Cr.**
- **Total cash and equivalents: 6,203.50 INR Cr**.

This terminal cash pool underwrites the next investment cycle (next-generation platforms, captive subsystem M&A, export market entry) and provides underwriting capacity for the much larger BGs that will accompany the Y11+ backlog.

### Balance Sheet Assumptions and Components - Detailed Walkthrough

#### Overview: How the Balance Sheet Closes the Model

The balance sheet is the integrating statement of this three-statement model. It receives inputs from both the P&L and the CashFlow statement, and it must balance in every single year for the model to be internally consistent. The integration runs along three primary axes:

- **P&L to Balance Sheet via Retained Earnings.** Each year's net income (or loss) flows into retained earnings. In Y1 retained earnings sit at -335.07 INR Cr, deepen to -782.20 INR Cr by Y3, and only turn positive in Y6 at +388.65 INR Cr. By Y10 retained earnings reach 5,548.24 INR Cr.
- **CashFlow Statement to Balance Sheet via the Cash Plug.** Ending cash on the balance sheet equals beginning cash plus net change in cash from the CFS. Cash builds from 110.08 INR Cr in Y1 to 5,903.27 INR Cr in Y10.
- **Working Capital Bridge.** DSO, DPO, and inventory days drive AR, AP, and inventory; the period-over-period changes flow into CFO. Customer advances (contract liabilities) sit on the liability side and are the largest single working-capital line in this model given the public-sector defense customer mix.

Total assets scale from 201.83 INR Cr in Y1 to 9,357.08 INR Cr in Y10, a ~46x expansion driven primarily by cash accumulation, receivables growth, and accumulated retained earnings rather than fixed-asset intensity.

#### Current Assets Walkthrough

**Cash and equivalents.** Cash is the residual plug from the CFS. Trajectory: Y1 110.08, Y3 238.22, Y5 470.75, Y10 5,903.27 INR Cr.

**Restricted cash (BG collateral).** Y1 7.65, Y3 38.33 (50% collateral schedule), Y10 300.24 INR Cr (20% schedule). On the asset side but not available for operations; analysts should exclude it from any free-cash or quick-ratio calculation.

**Accounts Receivable.** AR is driven by DSO of 180 days blended. AR scales from 25.89 INR Cr in Y1 to 2,493.03 INR Cr by Y10. At a 180-day DSO, AR represents roughly half a year's revenue locked up - the single biggest argument against thin equity capitalization.

**Inventory.** Inventory days are held at 90 days of COGS. Y1 6.28, Y3 44.27, Y10 413.75 INR Cr. The 90-day figure is a blend of long-lead components (radiation-hardened FPGAs, GaN MMIC RF front-ends) and Just-In-Time mission software / VMI arrangements.

#### Non-current Assets

**Net Property, Plant and Equipment.** Built from cumulative capex less accumulated depreciation. Gross PP&E: 35.45 (Y1), 450.90 (Y5), 600.12 INR Cr (Y10). Accumulated depreciation: 5.40 (Y1) to 367.06 INR Cr (Y10). Net PP&E: 30.05 (Y1), 174.58 (Y3), 233.06 INR Cr (Y10). The business is **asset-light by defense-industry standards** (Net PP&E is only ~2.5% of total assets by Y10).

**Net Intangibles (Capitalized R&D).** Under Ind AS 38, qualifying development costs are capitalized and amortized straight-line over 6 years per tranche. Weighted capitalization rate: Y1=26%, Y5=68%, Y10=73%.

| Year | Gross Capitalized R&D (INR Cr) | Accum. Amortization (INR Cr) | Net Intangibles (INR Cr) |
|------|-------------------------------:|-----------------------------:|-------------------------:|
| Y1 | 26.25 | 4.38 | 21.88 |
| Y2 | 115.30 | 23.59 | 91.71 |
| Y3 | 174.51 | 52.68 | 121.83 |
| Y4 | 217.85 | 88.98 | 128.87 (peak) |
| Y5 | 243.84 | 129.62 | 114.22 |
| Y6 | 258.47 | 172.70 | 85.77 |
| Y10 | 280.60 | 266.87 | 13.73 |

The net intangible **peaks in Y4 at 128.87 INR Cr** and then declines as the amortization tail catches up with new capitalization. By Y10 the net balance is only 13.73 INR Cr because most early-platform IP is fully amortized while new R&D capitalization has slowed to maintenance levels. This is an accounting artifact; the underlying IP and competitive moat are not "depleted".

**MAT Credit Asset (Deferred Tax Asset).** Under Section 115JB, MAT at 15% of book PBT applies whenever regular corporate tax (after R&D weighted deduction and NOL) yields a lower liability. Excess paid above regular tax is recognized as a MAT credit asset under Ind AS 12. Y4 14.92, Y5 74.94, Y6 89.81 (peak), Y7 onward 0 (fully utilized).

#### Current Liabilities

**Accounts Payable.** Driven by DPO of 45 days. Y1 3.14 to Y10 206.87 INR Cr.

**Contract Liabilities (Customer Advances).** The largest single liability in the model. MoD contracts include 10 to 15% mobilization advances (the model uses 15%). These are recognized as contract liabilities under Ind AS 115 and not as revenue until the performance obligation is satisfied. Y1 63.76 to Y10 2,501.96 INR Cr.

#### Long-term Liabilities: Venture Debt Schedule

| Year | Outstanding (INR Cr) | Phase |
|------|---------------------:|-------|
| Y1 | 20 | VC bridge draw |
| Y2 | 120 | PSU bank term loan on land collateral |
| Y3 | 200 | WC line expansion (peak) |
| Y4 | 200 | Peak (interest-only) |
| Y5 | 164 | Amortization begins |
| Y6 | 128 |  |
| Y7 | 73 |  |
| Y8 | 8 |  |
| Y9 | 0 | Fully retired |
| Y10 | 0 | Debt-free |

#### Equity Build-up

Equity capitalization follows three discrete rounds (Seed, Series A, Series B) labelled in the Funding sheet. Paid-in capital: Y1 450, Y2 850, Y3 1,100 INR Cr (held flat through Y10). Retained earnings trajectory: Y1 -335.07, Y3 -782.20 (deepest cumulative loss), Y6 +388.65 (turns positive), Y10 5,548.24 INR Cr. Total equity: Y1 114.93, Y10 6,648.24 INR Cr. By Y10, retained earnings represent ~83% of total equity.

#### Balance Check (Integrity Test)

The model includes an explicit row computing TOTAL ASSETS minus (TOTAL LIABILITIES + TOTAL EQUITY). The output is **0.00 in every year of the horizon (Y1 through Y10)**, confirming P&L flows correctly into retained earnings, CFS reconciles to the cash delta, working-capital line items are consistent, and capex/D&A/R&D capitalization/amortization all flow through both statements consistently.

#### Key Ratios Trajectory

**Current Ratio** (CA / Current Liab = AP + Customer Advances): Y1 2.24, Y2 1.58, Y3 1.65, **Y4 1.33** (lowest), Y10 3.36. The Y4 trough at 1.33 is the year of greatest liquidity stress; it remains above the typical 1.0 covenant threshold but with limited headroom.

**Debt-to-Equity:** Y1 0.17, **Y2 0.75** (peak), Y10 0.00 (debt-free).

**ROIC** (NOPAT / (Debt + Equity)): Y1 -1.86, **Y4 +0.14** (first positive), **Y6 +0.36** (peak), Y10 0.26. The Y10 ROIC of 26% sits **comfortably above the 18% WACC**, indicating durable value creation.

**Cash Conversion Cycle: 225 days constant** (DSO 180 + Inv days 90 - DPO 45). Holding CCC constant is a deliberate modeling choice; in reality, scaling into exports and stretching DPO should compress CCC over time. The model takes the conservative path of holding it flat.

#### Working-Capital Intensity Warning

Net Working Capital grows from 29.03 INR Cr in Y1 to 2,699.91 INR Cr in Y10 - a ~93x expansion against the ~46x asset expansion. This is the most important caveat for any reader of this model:

- **The business is profitable on an accrual basis well before it is cash-comfortable.** Retained earnings turn positive in Y6, but absolute NWC absorption continues to grow.
- **A growth-rate surprise to the upside is a cash-flow risk, not just a positive event.**
- The current-ratio trough at Y4 (1.33) understates the underlying tension; the model relies on venture debt and customer advances to bridge the worst of this period.

The eventual cash harvest from Y7 onward is the reward for surviving the absorption phase.

### Funding Requirements and Allocation Strategy - Detailed Walkthrough

#### Funding Philosophy

The capital plan is built on a clean, three-bucket logic that maps each rupee of incoming cash to a specific class of risk it is designed to absorb. This separation is deliberate: it prevents working-capital strain from contaminating the equity story, and it prevents long-duration platform NRE from being financed with short-duration bank lines that would create amortization mismatches against MoD payment cycles.

- **Equity (Rs 1,100 Cr total)** funds non-recoverable engineering, qualification campaigns, prototype builds, ESM/AESA development, the EMI and anechoic chamber, and the working-capital buffer needed to absorb the MoD/DSO receivable lag.
- **Venture debt and bank lines (Rs 200 Cr drawn at peak)** fund the working-capital ramp - inventory build for V2/V3/V6 series production, advance bank guarantees against MoD orders, and the WC line expansion in Y3.
- **Grants (iDEX, ADITI, SPRINT, TDF)** are treated as upside only and are explicitly **excluded** from the relied-on plan.

#### Round 1 - Seed (Y1, Rs 450 Cr)

Sized to carry the company from contract win through prototype delivery on the first two priority verticals (V2 EW/SIGINT and V6 Military AI) with sufficient overhead to stand up the initial production line.

**Deployment within Y1:**
- Platform NRE for milestones M1 through M5 across the five shared modules (RF, DSP, SysEng, Embedded SW, AI/ML).
- ESM iDEX MoQ build and delivery against the Rs 200 Cr prototype order already won.
- First production line stand-up (V2 family) including tooling, test benches, and ATE.
- Working-capital buffer to absorb the MoD DSO of ~180 days on early invoicing.
- Initial ABG margin against the Y1 ABG of Rs 18.76 Cr.

**Why Rs 450 Cr and not less:** Y1 cumulative FCF deficit (-359.92 INR Cr) combined with restricted cash needs (7.65 INR Cr) exceeds Rs 360 Cr. Any seed round below Rs 400 Cr would force a bridge inside Y1. The Rs 450 Cr quantum leaves a closing cash buffer of 110.08 INR Cr - just above the 100 INR Cr policy floor.

#### Round 2 - Series A (Y2, Rs 400 Cr)

The production scale-up round.

**Deployment within Y2:**
- Production scale-up across V2 (EW/SIGINT), V3 (Counter-UAS), and V6 (Military AI) simultaneously.
- V1 AESA development and V4 MALE UAS prototype build.
- EMI and anechoic chamber facility (essential for Make-II qualification of AESA and UAS).
- Absorption of 100% of the Y1 to Y2 BG collateral requirement (compressed by the 10% bank-confirmed margin on the existing facility).

**Why Rs 400 Cr:** Y2 carries one of the largest single-year working-capital builds because three production lines are ramping concurrently. The Rs 400 Cr round, layered on top of Rs 100 Cr of PSU bank term loan, closes Y2 at 142.34 INR Cr cash.

#### Round 3 - Series B (Y3, Rs 250 Cr)

The trough-coverage round and **the final equity round in the plan**.

**Deployment within Y3:**
- Production ramp for V1 (AESA), V4 (MALE UAS), and V5 (Autonomous AUV/USV) first-of-class deliveries.
- Make-II contract working capital.
- Capex tranche for in-house test ranges.

**Trough-coverage logic:** Cumulative FCF trough across Y1 to Y3 is -1,061.78 INR Cr. Total CFF across Y1 to Y3 is 1,326.50 INR Cr (471.50 + 525 + 330, including grants). Stripping out grants, relied-on funding of 1,300 INR Cr (1,100 equity + 200 debt) provides ~22% cushion over the peak deficit.

**Why this is the last round:** Y4 turns FCF-positive at +2.99 INR Cr, and from Y5 onward operating cash flows are sufficient to service debt amortization, fund all capex, and build the cash position toward 5,903.27 INR Cr Y10 close.

#### Venture Debt Rationale and Schedule

| Year | Drawn (INR Cr) | Purpose | EoY Balance | Interest |
|------|---------------:|---------|------------:|---------:|
| Y1 | 20 | VC bridge against Seed close timing | 20 | 0.80 |
| Y2 | 100 | PSU bank term loan on land collateral | 120 | 5.60 |
| Y3 | 80 | WC line expansion for Make-II execution | 200 | 12.80 |
| Y4 | 0 | Peak balance held | 200 | 16.00 |
| Y5 | (36 repaid) | Amortization begins | 164 | 14.56 |
| Y6 | (36 repaid) | Continued amortization | 128 | 11.68 |
| Y7 | (55 repaid) | Accelerated repayment | 73 | 8.04 |
| Y8 | (65 repaid) | Near full repayment | 8 | 3.24 |
| Y9 | (8 repaid) | Final tranche cleared | 0 | 0.32 |
| Y10 | 0 | Debt-free balance sheet | 0 | 0.00 |

Peak interest of 16 INR Cr in Y4 is less than 1% of Y4 revenue (855.20 INR Cr). Cumulative interest across the ten-year plan is ~73 INR Cr on 200 INR Cr of debt drawn.

#### Why Grants Are Excluded from the Relied-On Plan

The Funding sheet labels grants explicitly: "Excluded - not relied upon in funding plan."

- **First reason:** grant cash timing in Indian defence programmes is genuinely unpredictable (milestone certification, beneficiary acceptance, tranche release can slip 6 to 18 months). A funding plan that depends on this timing is a funding plan with a hidden cash gap.
- **Second reason:** presenting grants as part of the funding ask weakens the equity story. By excluding grants, the plan demonstrates that the company is financeable on equity + bank debt alone; any grant inflow becomes a buffer improvement rather than a gap closer.

#### Pre-Plan Facility Credit

| Facility | Quantum | Status | Role in Plan |
|----------|--------:|--------|--------------|
| Land and factory (collateral base) | Rs 150 Cr | Owned, lien-clean | Anchors PSU bank TL and BG facility |
| ABG facility sanctioned | Rs 18.5 Cr | Sanctioned | Covers Y1 ABG of Rs 18.76 Cr |
| Working-capital limit | Rs 12.5 Cr | Drawn (utilised) | Operational liquidity, pre-plan |
| Term loan approved | Rs 9 Cr | Drawn in Y1 | Included in Y1 Rs 20 Cr draw |
| BG margin pricing | 10% | Bank-confirmed | Material WC efficiency vs 100% cash cover |

The bank-confirmed 10% BG margin (vs the 100% required without the existing facility) is the single most important pre-plan input. Combined with the tapering collateral schedule, it limits restricted cash to 300.24 INR Cr by Y10 against BG capacity of 3,002.35 INR Cr.

#### Total Capital Deployed and Cushion Against Peak Deficit

| Source | Y1 | Y2 | Y3 | Cumulative Y1 to Y3 |
|--------|---:|---:|---:|--------------------:|
| Seed / Series A / Series B equity | 450.00 | 400.00 | 250.00 | 1,100.00 |
| Venture debt drawn | 20.00 | 100.00 | 80.00 | 200.00 |
| Grant memo (excluded from relied plan) | 1.50 | 25.00 | 0.00 | 26.50 |
| **CFF total (with grants)** | **471.50** | **525.00** | **330.00** | **1,326.50** |

**Peak cumulative invested capital (relied-on):** 1,300 INR Cr. **Peak cumulative FCF deficit:** -1,061.78 INR Cr at close of Y3. **Cushion:** ~22% above the peak deficit.

#### Minimum Cash Compliance Check

The plan enforces a **100 INR Cr minimum cash floor** at every year-end. This is an internal liquidity policy (not a covenant) sized to cover ~3 months of payroll and committed creditor obligations at peak headcount.

| Year | Projected EoY Cash (INR Cr) | Floor | Buffer | Funding Gap |
|------|----------------------------:|------:|-------:|:-----------:|
| Y1 | 110.08 | 100 | **10.08** (tightest) | 0 |
| Y2 | 142.34 | 100 | 42.34 | 0 |
| Y3 | 238.22 | 100 | 138.22 | 0 |
| Y4 | 241.21 | 100 | 141.21 | 0 |
| Y5 | 470.75 | 100 | 370.75 | 0 |
| Y6 | 1,006.72 | 100 | 906.72 | 0 |
| Y7 | 1,877.55 | 100 | 1,777.55 | 0 |
| Y8 | 2,884.38 | 100 | 2,784.38 | 0 |
| Y9 | 4,242.37 | 100 | 4,142.37 | 0 |
| Y10 | 5,903.27 | 100 | **5,803.27** | 0 |

**Funding gap is zero in every year of the plan.**

#### Self-Funding From Y4 Onward

From Y4 onward, total CFF turns negative as the company amortizes the venture debt stack: Y5 -36, Y6 -36, Y7 -55, Y8 -65, Y9 -8, Y10 0.

**No equity round is required after Y3.** The captable closes at the Series B, and the company self-funds all subsequent growth from operating cash flows.

### Break-Even Analysis and Timeline - Detailed Walkthrough

The workbook distinguishes between several different notions of "break-even", each of which answers a different stakeholder question. The BreakEven sheet keeps them separate and reports each one on its own merits.

#### The Four Flavours of Break-Even Used in This Model

- **Revenue break-even (contribution-margin break-even):** the annual revenue level at which gross profit exactly covers the cash fixed-cost stack. Fixed Cost / Gross Margin.
- **EBITDA break-even:** the first year in which EBITDA turns positive. The operating-profitability inflection.
- **FCF break-even:** the first year in which free cash flow turns positive after capex, working-capital movement, and tax. The cash-self-sufficiency inflection.
- **Net income break-even:** the first year in which bottom-line net income is positive after interest, depreciation, and tax. The accounting-profitability inflection.

These four points do not coincide in time. EBITDA-positive almost always arrives first, then FCF-positive, then net income, and finally retained earnings turning positive (which requires cumulative profits to exceed cumulative losses).

#### Revenue Break-Even Calculation at the Y6 Snapshot

The BreakEven sheet uses Year 6 as its reference snapshot because Y6 is the first year in which all six verticals are fully commercial and the cost structure has reached steady-state proportions:

| Item | INR Cr | Notes |
|------|-------:|-------|
| R&D / NRE expense | 66.91 | Steady-state R&D post launch-burn |
| Sales and Marketing | 174.42 | 8% of consolidated revenue band |
| G&A | 152.62 | Headcount and overhead |
| Other Opex | 138.26 | Facilities, IT, professional fees |
| D&A | 92.69 | Depreciation of the Y1 to Y6 capex base plus capitalized-R&D amortization |
| COGS personnel | 26.55 | Allocated production labour outside BoM |
| **Total fixed cost** | **651.44** |  |
| Company weighted gross margin | 66% | Blended across V1 to V6 |
| **Break-even revenue (Fixed / GM%)** | **981.07** | 651.44 / 0.66 |

At the Y6 cost structure, the company needs approximately **981 INR Cr** of annual revenue to cover its fixed costs exactly. Actual Y6 revenue is **2,180.23 INR Cr**, which is **~2.2x** the break-even level - the headroom that produces the 40% EBITDA margin in that year.

#### Per-Vertical Gross Profit Contribution at the Y6 Snapshot

| Vertical | Revenue (INR Cr) | BoM (INR Cr) | Gross Profit (INR Cr) | GM% | Units |
|----------|-----------------:|-------------:|----------------------:|----:|------:|
| V1 AESA Radar | 1,403.50 | 493.13 | 910.37 | 65% | 59 |
| V2 EW/SIGINT | 1,073.52 | 415.25 | 658.27 | 61% | 76 |
| V3 Counter-UAS | 809.94 | 363.50 | 446.45 | 55% | 214 |
| V4 MALE UAS | 973.45 | 302.46 | 670.99 | 69% | 6 |
| V5 Autonomous AUV/USV | 439.55 | 120.93 | 318.62 | 72% | 19 |
| V6 Military AI | 416.49 | 23.81 | 392.68 | 94% | 80 |
| **Total** | **5,116.45** | **1,719.07** | **3,397.38** | **66%** | **454** |

- V6 Military AI is the structural margin lifter at 94% GM. Every incremental rupee of V6 revenue contributes 94 paise to fixed-cost coverage.
- V3 Counter-UAS is the lowest-margin product at 55% but the highest-volume (214 units) - it absorbs fixed cost through throughput.
- The V-sheet totals (5,116 INR Cr) are higher than the consolidated P&L revenue (2,180 INR Cr at Y6) because V-sheets show full unit-shipment economics whereas consolidated revenue is gated through the Backlog delivery-rate schedule. The BreakEven sheet uses the V-sheet detail to derive the blended GM%, which is the correct denominator for the break-even formula.

#### Why EBITDA Goes Positive Before Revenue Hits the Break-Even Line

Actual EBITDA turns positive in Y4 at a revenue level of **855.20 INR Cr** - below the 981 INR Cr revenue break-even computed from the Y6 snapshot. This is not a contradiction. The Y6 snapshot uses Y6 fixed costs (651.44 INR Cr); Y4 has a leaner fixed-cost stack because R&D/NRE expense peaks in Y2 (347.81 INR Cr) and collapses to 118.02 INR Cr by Y4 as platforms harden and reuse takes hold.

R&D/NRE expense trajectory (P&L line): Y1 301.94, Y2 347.81 (peak), Y3 185.22, Y4 118.02, Y5 80.59, Y6 66.91 (steady state).

Because R&D drops by ~230 INR Cr between Y2 and Y4, the company hits EBITDA-positive at a revenue level lower than the Y6 break-even line implies. This is the platform-reuse payoff: heavy front-loaded R&D in Y1-Y2 amortises into later years as common building blocks (T/R modules, RF front-ends, autonomy stack, edge compute) get reused across verticals. The cumulative NRE avoided (counterfactual savings versus standalone build, NOT realized cash) is 994.32 INR Cr over the 10-year horizon.

#### Profitability Timeline Summary

| Milestone | Year | Value (INR Cr) | Context |
|-----------|------|---------------:|---------|
| First EBITDA positive | Y4 | +190.46 | 22% EBITDA margin; revenue 855.20 |
| First FCF positive | Y4 | +2.99 | Just clears zero after capex and WC |
| First Net Income positive | Y4 | +99.49 | After interest, D&A, tax |
| Peak cumulative cash deficit | Y3 | -1,061.78 | Anchor for total funding need |
| Retained earnings turn positive | Y6 | +388.65 | Cumulative profits > cumulative losses |
| Modelled revenue break-even (Y6 basis) | (notional) | 981.07 | Y6 snapshot cost basis |
| Actual revenue at EBITDA+ | Y4 | 855.20 | Below Y6 break-even line due to R&D step-down |

The reasons this timeline is defensible:

- **V2 EW/SIGINT is anchored by an iDEX contract in Y1**, producing early revenue (52.50 INR Cr) and validating the platform thesis.
- **V1 AESA and V3 Counter-UAS scale rapidly in Y3-Y4** off the same RF/T-R-module IP, which is why R&D burn drops sharply rather than continuing to grow linearly with verticals.
- **V4 MALE UAS first ships in Y3-Y4**, providing the high-ticket revenue that pushes EBITDA from breakeven to +190 INR Cr in a single year.
- **V6 Military AI ships from Y1 onwards** at ~94% GM, disproportionately contributing to fixed-cost coverage.

10-year cumulative result: **21,209.23 INR Cr revenue, 8,100.05 INR Cr EBITDA, 5,548.24 INR Cr net income**, against cumulative R&D/NRE expense of 1,365.94 INR Cr (with an additional 994.32 INR Cr of NRE counterfactually avoided via platform reuse) and total Capex of 600.12 INR Cr.

### Net Present Value (NPV) - Definition, Calculation, and Strategic Intent

#### What NPV Means and Why It Matters

Net Present Value (NPV) is the value created by a project, expressed in today's rupees, after charging for the cost of capital that the project consumes. It answers the single question an investor cares about: given that money has a time value and a required return, is this project worth more than the cash it absorbs?

Mechanically, NPV discounts every future free cash flow back to year zero at the weighted-average cost of capital (WACC), then sums them:

> NPV = sum over t of [ FCF_t / (1 + WACC)^t ]

If NPV > 0, the project earns more than the investor's required return and creates value. If NPV < 0, the project destroys value relative to the next-best alternative. The size of NPV is the rupee value created above and beyond the hurdle rate.

#### The Discount Rate: 18% WACC

The model uses **WACC = 18%** as the discount rate. This is set on the **Assumptions sheet, cell C7**, with the rationale explicitly captured in the note column: "Used for NPV - 18% reflects unlisted Indian defense unlisted equity cost-of-capital (beta ~1.5, ERP 8-9%, Rf 7%)." The build-up:

- **Risk-free rate (Rf):** ~7% - approximately the 10-year Government of India bond yield.
- **Equity risk premium (ERP):** 8 to 9% - standard India-listed-equity premium adjusted for country risk.
- **Beta:** ~1.5 - reflecting a small-cap, unlisted defence company with higher sensitivity to macro and policy cycles than the broader market.
- **Cost of equity (CAPM):** Rf + Beta x ERP = 7% + 1.5 x 8.5% = ~20% gross of unlisted illiquidity adjustments.
- **Blended WACC at modest debt mix:** 18% after capital-structure weighting.

This 18% is materially higher than the 12 to 14% cost-of-capital that listed Indian defence majors (HAL, BEL, BDL) trade against, and higher than the 14 to 16% rate a typical Indian VC would apply to a growth-stage technology company. The model uses 18% precisely to avoid the criticism that NPV is being inflated by a soft hurdle rate.

#### The FCF Stream That Feeds the NPV

The FCF series used in the NPV calculation is the same one shown on the CashFlow sheet (INR Cr):

| Year | FCF | Cumulative FCF |
|------|----:|---------------:|
| Y1 | -359.92 | -359.92 |
| Y2 | -467.73 | -827.66 |
| Y3 | -234.13 | -1,061.78 |
| Y4 | +2.99 | -1,058.79 |
| Y5 | +265.53 | -793.25 |
| Y6 | +571.97 | -221.28 |
| Y7 | +925.83 | +704.55 |
| Y8 | +1,071.83 | +1,776.38 |
| Y9 | +1,365.99 | +3,142.37 |
| Y10 | +1,660.89 | +4,803.27 |

The cumulative FCF column makes the funding story explicit: peak cash deficit of -1,061.78 INR Cr in Y3, payback (cumulative FCF turning positive) between Y6 and Y7, and a 10-year cumulative FCF of +4,803.27 INR Cr.

#### The Base NPV Result: 747.15 INR Cr

Discounting the Y1 to Y10 FCF stream at 18% WACC produces:

> **NPV (10-year FCF only, no terminal value) = 747.15 INR Cr**

Against approximately 1,300 INR Cr of cumulative equity and debt deployed in Y1 to Y3 (1,100 equity + 200 debt at peak), this represents value creation of roughly 57% above the hurdle rate over a truncated 10-year horizon. The project IRR on the same FCF stream is **31.9%** - the rate at which the discounted FCFs sum to zero.

Critically, this is the **project IRR** computed on FCF only, not the **investor IRR**, because it excludes equity issuances, debt drawdowns, dividends, and exit proceeds.

#### Why the 747 INR Cr NPV Is Conservative

The 747 INR Cr figure is deliberately a floor, not a fair estimate, for two reasons:

- **It excludes terminal value.** Cutting cash flows off at Y10 implicitly assumes the business is worth zero at the end of Y10. In reality, a defence platform business generating 5,055.32 INR Cr of revenue and 2,347.09 INR Cr of EBITDA in Y10 is a substantial going concern that any acquirer would value at a meaningful multiple.
- **It uses a punitive WACC.** 18% is at the high end of any defensible cost-of-capital range for an Indian defence platform. A listed peer would discount at 12 to 14%; using 12% instead of 18% would lift the base NPV substantially.

#### Terminal Value: What the Business Is Worth at the End of Year 10

The workbook computes terminal value (TV) two ways on the KPIs sheet:

**Method 1: Exit multiple on Y10 EBITDA**
- Y10 EBITDA: 2,347.09 INR Cr
- Exit multiple: 12x (in line with listed Indian defence comparables HAL, BEL, BDL trading at 10 to 14x forward EBITDA in normal markets)
- TV at end of Y10: **28,165.08 INR Cr**
- PV of TV at Y0, discounted at 18% over 10 years: **5,381.35 INR Cr**

**Method 2: Gordon growth model (perpetual cash flow)**
- Y10 FCF: 1,660.89 INR Cr
- Perpetual growth rate (g): 3% (deliberately conservative, well below Indian nominal GDP)
- TV = FCF x (1 + g) / (r - g) = 1,660.89 x 1.03 / (0.18 - 0.03) = **11,404.81 INR Cr**
- PV of TV at Y0, discounted at 18% over 10 years: **2,179.05 INR Cr**

The exit-multiple method produces a TV roughly 2.5x the Gordon-growth TV. This gap is the standard result when WACC (18%) is well above a defensible perpetual growth rate (3%) - the Gordon formula penalises high discount rates harshly because (r - g) sits in the denominator. The 12x exit multiple anchors on observable market evidence and is the appropriate benchmark for an exit-oriented investor.

#### Equity NPV Including Terminal Value

Combining the 10-year FCF NPV with the PV of terminal value:

| Component | 12x EBITDA Case | Gordon Growth Case |
|-----------|----------------:|-------------------:|
| NPV of Y1 to Y10 FCF (at WACC 18%) | 747.15 | 747.15 |
| PV of Terminal Value at Y0 | 5,381.35 | 2,179.05 |
| **Equity NPV including TV** | **6,128.50** | **2,926.21** |

Against 1,100 INR Cr of equity deployed, the 12x case produces equity NPV of **6,128.50 INR Cr - more than 5.5x the capital deployed**, expressed in today's rupees and net of an 18% required return. The Gordon case still delivers ~2.7x capital deployed in present-value terms.

#### IRR Caveats

The 31.9% IRR on the 10-year FCF stream is the project IRR, not the investor IRR:

- **Project IRR** is computed on free cash flow alone, ignoring how that cash flow is split between debt holders and equity holders. It is the appropriate measure of whether the underlying business creates value.
- **Investor IRR** is computed on actual equity cash flows (equity in, dividends/distributions out, exit proceeds out). Because investor IRR captures the exit valuation, including terminal value is essential to compute it correctly.

The workbook does not auto-compute IRR including TV. The KPIs sheet provides the rule of thumb: "with PV of TV ~Rs 5 to 7K Cr against Rs 1,100 Cr deployed, IRR incl. TV typically jumps 8 to 12 percentage points vs 10-yr FCF-only IRR." That places the all-in investor IRR in the **40 to 44% range** for the 12x case, materially exceeding the 25 to 30% threshold that growth-stage defence investors typically target.

#### What the NPV Assumes (and What It Does Not Adjust For)

- It assumes **WACC stays at 18% throughout the 10-year horizon**. In reality, as the business de-risks (post-Y4 EBITDA inflection), its cost of capital should fall, which would mechanically lift NPV.
- It uses a **single deterministic scenario.** There is no probability weighting across base/upside/downside outcomes.
- It applies **no execution-risk haircut.** Defence-platform plans of this scale typically slip 6 to 18 months on at least one major programme; the NPV does not embed a discount for that.
- It assumes **the Backlog delivery schedule holds.** If MoD/iDEX procurement timelines slip materially, the revenue ramp pushes right and NPV falls.
- It assumes **BoM learning curves perform as modelled** (0.92 Wright's-law factor per doubling, with a 70% BoM floor). Underperformance compresses GM% and reduces both NPV and TV.

#### Strategic Intent: What the NPV Is Designed to Communicate

The strategic message embedded in the NPV machinery is layered:

1. **Even on the most punitive basis** (10-year FCF only, no TV, 18% WACC), the project produces +747.15 INR Cr of NPV against 1,100 INR Cr of equity deployed. This clears the hurdle rate without requiring any belief in terminal value or any softening of the discount rate. It is the **floor case**.

2. **The real investor return** comes from the terminal value. A defence platform that has reached 2,347.09 INR Cr of Y10 EBITDA is not a project that ends - it is a going concern that an acquirer (a listed Indian defence major, a US or European prime, a strategic PE buyer) will pay 10 to 14x EBITDA for. The 12x case is the central estimate, not the upside case.

3. **Including TV, the equity NPV is 6,128.50 INR Cr against ~1,100 INR Cr deployed** - a value-creation multiple of 5.5x in present-value terms after 18% WACC. The investor IRR rises to the 40 to 44% range. This is the **actual investment thesis**.

4. **The 10-year FCF-only NPV (747.15 INR Cr) and the equity NPV including TV (6,128.50 INR Cr) bracket the answer** for risk-averse and risk-neutral readers. A scout who wants the most conservative number takes 747. An LP or strategic acquirer comparing this against other defence platform investments takes 6,128 - and rationally, because every comparable transaction in Indian defence has been priced off forward EBITDA multiples, not truncated FCF.

#### Sensitivities Worth Flagging

The NPV is most sensitive to four variables, in roughly this order:

- **WACC.** Moving from 18% to 14% (a defensible cost of capital once the business is post-Y4) lifts both the 10-year NPV and the PV of TV materially - by roughly 30 to 40% in combination.
- **EBITDA-inflection timing.** A 12-month delay in the EBITDA-positive year (Y4 to Y5) pushes peak cash deficit deeper and reduces NPV by approximately 200 to 300 INR Cr at the 10-year FCF-only level, and proportionally more once TV is included.
- **BoM learning curve underperformance.** If the V1 to V3 learning curves deliver a 0.96 factor per doubling instead of 0.92, blended GM% in the late years compresses by 3 to 4 percentage points and Y10 EBITDA falls 250 to 350 INR Cr, with corresponding TV impact.
- **Working capital deterioration.** If receivables stretch to 240+ days (the historical norm for some MoD CapEx programmes), Y3 to Y5 FCF deteriorates further and peak funding need rises by 150 to 250 INR Cr, which both delays cash break-even and reduces NPV.

A reader who wants to stress-test the NPV should toggle these four variables on the Assumptions sheet rather than focusing on the headline figure. The robustness of the investment case is established by how much NPV survives a downside scenario, not by how high it goes in the base case.

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

1. Edit Platform NRE and maturity (rows 6-10 and 15-19).

2. Edit module mix in ReuseMatrix if the vertical architecture changes.

3. Edit Assumptions!C26 platform reuse multiplier for a one-cell scenario lever.

4. Review R&D\_NRE and KPI NRE savings.

To change working capital/funding stress:

1. Edit Assumptions DSO, DPO, inventory days, advance rate, PBG, BG fee, and collateral.

2. Review Backlog, CashFlow, restricted cash, and Funding gap.

To change accounting treatment:

1. Edit R&D\_Buckets research and development capitalisation percentage inputs.

2. Edit Assumptions amortization life (C58) if the capitalised development asset life changes.

3. Review R&D\_NRE, P&L, CashFlow, BalanceSheet, and the R&D bucket KPI rows.

4. Recalculate the workbook in Excel or LibreOffice, because formula values must be refreshed after structural accounting changes.

To stress-test NPV:

1. Change Assumptions!C7 (WACC) - 18% is the base; try 14% for an at-listing-comparable case.

2. Shift the EBITDA inflection by editing Backlog delivery rates (delay Y4 by raising V4/V5 thresholds or lowering V1/V2 delivery percentages).

3. Edit Assumptions BoM learning curve (C12) and BoM floor (the 0.92 and 0.70 base values) to test margin compression.

4. Stretch Assumptions DSO from 180 to 240 to model worst-case MoD payment behaviour.

5. Re-run the KPIs Terminal Value memo block to see how NPV including TV moves.
