# Nitrodynamics (NDAD) — Financial Model Architecture

**Companion explainer for `Defense\\\_Platform\\\_Business\\\_Plan\\\_Financial\\\_V2.xlsx`**

> This document bridges the raw Excel workbook and the Nitrodynamics investor narrative. It walks every worksheet and every logical table inside it, classifying each as an **Input/Assumption**, a **Calculation Engine**, or an **Output/Reporting** layer; explaining why it matters to the NDAD story; tracing how its numbers flow into the three-statement model and the valuation; and quoting the actual formulas that do the work. Every formula, cell address and value cited below was extracted directly from the live workbook — nothing is approximated.

## At a Glance

| Property | Value |
| - | - |
| Workbook | `Defense\\\_Platform\\\_Business\\\_Plan\\\_Financial\\\_V2.xlsx` |
| Worksheets | 26 |
| Formulas | ~4,723 |
| External links / defined names | None |
| Formula errors | 0 (fully recalculable; balance sheet ties to zero in all 10 years) |
| Currency / units | Indian Rupees in **Crore (₹ Cr)**; per-item Capex/Headcount rows are in ₹ Lakh and rolled to ₹ Cr by ÷100 |
| Projection horizon | Y1–Y10 |
| Valuation basis | WACC 18% (`Assumptions!C7`); Project IRR 31.9%; NPV ₹747 Cr; 10-yr cumulative FCF ₹4,803 Cr |
| Status as analysed | 2026-06-28 |


**Who is NDAD?** Nitrodynamics Aerospace & Defence is an Indian defence-technology company building a **multi-domain hardware + AI platform** that is reused across six product verticals — AESA radar (V1), Electronic Warfare / SIGINT (V2), Counter-UAS (V3), UAS/MALE drones (V4), Autonomous systems (V5), and Military AI (V6). The financial thesis rests on **capital efficiency through IP reuse**: one platform investment amortised across many defence programmes, anchored by a Day-1 iDEX firm order for naval Electronic Support Measures (ESM).

## How to Read This Document

The model is organised as a directed pipeline, not a flat set of tabs. The chapters below follow the **direction of data flow**, from raw drivers to investor-facing outputs:

1. **Strategic Narrative & Platform Sheets** — the framing layer (plus `Platform`, which is secretly a driver).

2. **R&D Economics & Reuse Moat** — how shared engineering is quantified and capitalised.

3. **Assumptions & Vertical Product Models** — the global input register and the six product lines (incl. the iDEX MoQ bridge).

4. **Revenue Recognition & Backlog Engine** — the core: how an order book converts into recognised revenue.

5. **Cost & Resource Build** — headcount, capex/depreciation, and opex.

6. **The Integrated Three-Statement Model** — P&L, Cash Flow, Balance Sheet.

7. **Funding, Returns, KPIs & Break-Even** — the capital stack and the investor dashboard / valuation.

Each entry uses a fixed five-part template: **Functional Overview → Strategic Significance → Modeling Impact & Data Flow → Structural Detail & Key Formulas → Glossary**. A consolidated master glossary, a model-integrity register, and a full sheet inventory appear in the appendices.


## 0. Workbook-Wide Architecture & Data Flow

The single most important thing to understand about this model is its **recognition spine**: reported revenue is **not** driven by the per-product vertical sheets — it is driven by the **Backlog** sheet. The vertical sheets (V1–V6) are explicitly labelled *"READ ONLY SUPPORTING DETAIL"*; editing units or ASP on a vertical sheet does **not** move the consolidated top line. They survive only to (a) document the product economics and (b) supply the gross-margin ratios that rescale COGS. This is deliberate: in defence, revenue is earned as a firm order book is *delivered*, so the model recognises revenue from backlog burn-down, giving every rupee of forecast revenue an order-book pedigree.

### The pipeline

```
                ┌──────────────────────────────────────────────────────────┐   
 DRIVERS       │  Assumptions (global knobs)                               │   
 │  Platform  ──►  ReuseMatrix  ──►  R&D\\\_Buckets / R&D\\\_NRE    │   
 │  V1..V6 vertical product models (ASP, BoM, units)         │   
 └───────────────┬───────────────────────┬──────────────────┘   
 │ (COGS ratios only)     │ (bookings)   
 ▼                         ▼   
 REVENUE SPINE         ┌───────────────┐        ┌───────────────┐   
 │   Backlog     │ ─────► │   Revenue     │   
 │ open+adds−rec │ recog. │ rows 6–11/23–28│   
 └───────────────┘        └──────┬────────┘   
 │ totals r12 (rev) / r29 (COGS)   
 COST BUILD                                            ▼   
 Headcount ─┐                                  ┌───────────────┐   
 Capex ─────┼─────────────────────────────────►│     P&L       │   
 Opex ──────┤   (labour, D&A, opex, R&D)       │ GP→EBITDA→NI  │   
 R&D\\\_NRE ───┘                                  └──────┬────────┘   
 │ NI, D&A, capex, funding   
 ┌─────────────────────────┼───────────────────────┐   
 ▼                          ▼ ▼   
 THREE STATEMENTS    ┌───────────────┐         ┌───────────────┐ ┌───────────────┐   
 │   CashFlow    │ closing │ BalanceSheet  │◄──────│ Funding    │   
 │ CFO/CFI/CFF   │ cash──► │ A = L + E (=0) │ equity│ rounds + debt │   
 └──────┬────────┘         └───────────────┘  /debt └───────────────┘   
 │ FCF   
 OUTPUTS / VALUATION        ▼   
 ┌───────────────────────────────────────────────┐   
 │  KPIs (dashboard, terminal value, equity NPV)  │   
 │  BreakEven (IRR 31.9%, NPV ₹747 Cr, B/E rev)   │   
 └───────────────────────────────────────────────┘
```

### Equivalent Mermaid view

```
flowchart TD    
  A\\\[Assumptions\\\] --\\\> P\\\[Platform\\\]    
  P --\\\> RM\\\[ReuseMatrix\\\]    
  RM --\\\> RNRE\\\[R&D\\\_NRE\\\]    
  P --\\\> RB\\\[R&D\\\_Buckets\\\]    
  V\\\[V1..V6 vertical models\\\<br/\\\>READ-ONLY detail\\\] -. COGS ratios .-\\\> REV\\\[Revenue\\\]    
  V -. bookings .-\\\> BL\\\[Backlog\\\]    
  BL -- recognised deliveries --\\\> REV    
  REV -- total rev r12 / COGS r29 --\\\> PL\\\[P&L\\\]    
  HC\\\[Headcount\\\] --\\\> PL    
  CX\\\[Capex + depreciation\\\] --\\\> PL    
  OX\\\[Opex\\\] --\\\> PL    
  RNRE --\\\> PL    
  PL -- net income / D&A --\\\> CF\\\[CashFlow\\\]    
  CX --\\\> CF    
  FND\\\[Funding\\\] --\\\> CF    
  PL -- retained earnings --\\\> BS\\\[BalanceSheet\\\]    
  CX --\\\> BS    
  FND --\\\> BS    
  CF -- closing cash --\\\> BS    
  CF -- FCF --\\\> KPI\\\[KPIs\\\]    
  CF -- FCF --\\\> BE\\\[BreakEven\\\<br/\\\>IRR / NPV\\\]    
  PL --\\\> KPI    
  BS --\\\> KPI
```

### Five conventions that govern the whole workbook

1. **Backlog-driven recognition.** `Revenue!D6:M11 = Backlog!D89:M94` (a cell-for-cell mirror of recognised deliveries). The top line is the order book burning down, not the product sheets.

2. **V-sheets are read-only detail.** They feed *only* the COGS rescale (`Revenue!23:28`), preserving each line's gross-margin % while the top line comes from Backlog.

3. **The column offset.** The **Funding** sheet uses columns **D:M** for Y1–Y10; **every other statement uses C:L**. Cross-sheet links honour this one-column shift (e.g. `P&L!C21 = Funding!D17`). Inserting a column on Funding silently misaligns its consumers — the model's single biggest structural fragility.

4. **Recognised basis vs planned shipments.** Where a sheet shows both (e.g. BreakEven), the financial rows pull the *recognised* basis from `Revenue!`, while any "units" column shows V-sheet *planned* shipments for context only.

5. **Honest non-cash flags.** "NRE avoided", terminal value, and project IRR are labelled in-cell as analytics, explicitly *not* realised cash and *not* investor IRR — a transparency choice that matters for diligence.

## 1. Strategic Narrative & Platform Sheets

This section documents the five strategic / narrative front-matter sheets that frame the NDAD financial model: **Cover**, **Strategy**, **MarketPositioning**, **Roadmap**, and **Platform**. Four of the five are pure narrative/context (zero downstream wiring). The fifth, **Platform**, is the one genuine exception in this slice — it is a live calculation driver whose NRE and reuse-strength outputs feed the R&D/NRE cost build, the ReuseMatrix, and ultimately the P&L. Currency throughout is Indian Rupees in Crore (₹ Cr); the planning horizon is Y1–Y10.

### Cover

**Type:** Output/Reporting (front-matter / orientation sheet) **1. Functional Overview:** The workbook title page and reader's orientation guide. It states the company thesis ("new-age defense prime built on owned IP across six product verticals"), the operating model, the core USP, the planning horizon, the cell-colour legend (yellow = input, blue = calculated), the recommended read order, and a "product verticals at a glance" lookup table mapping each vertical code (V1–V6) to its name, domain, launch year, and supporting sheet. **2. Strategic Significance:** Establishes the investor narrative up front — six already-designed product lines, owned IP fielded inside Y3, five reusable platform modules, and a bank-confirmed 10% BG (bank guarantee) margin. It positions NDAD as a capital-efficient, asset-light "software-company-like" prime rather than a legacy program-directorate prime, and frames the multi-domain (Air/Land/Sea/Cyber) penetration story the rest of the model quantifies. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: none — manual narrative input.

- Downstream outputs: none. Verified by formula scan: zero inbound references to `Cover!` anywhere in the workbook. Purely orientation/context; it does not feed any calculation. **4. Structural Detail & Key Formulas:**

- Structure: range B2:F20, 20 rows × 6 cols, 0 formulas. Two logical blocks: (a) a label/value narrative block (B5:C11 — thesis, operating model, verticals, USP, horizon, colour key, read order) and (b) a 6-row "Product verticals at a glance" table (B14:F20) with headers Code | Vertical | Domain | Launch | Sheet. Data types: all text/string.

- Key formulas: none. The sheet is entirely hard-typed strings. Example content cell: `B5` = "Company thesis", `C5` = "A new-age defense prime built on owned IP across six product verticals…". The vertical table rows e.g. `B16:F16` = V2 | Electronic Warfare & SIGINT | Air/Land/Sea (RF + DSP) | Y1 | V2\_EW\_SIGINT. **5. Glossary of Terms:** NDAD = Nitrodynamics Aerospace & Defence (the company). BG = Bank Guarantee. IP = Intellectual Property. USP = Unique Selling Proposition. V1–V6 = the six product verticals (AESA Radar; EW & SIGINT; Counter-UAS; MALE-class ISR UAS; Autonomous AUV/USV; Military AI). AESA = Active Electronically Scanned Array (radar). EW = Electronic Warfare. SIGINT = Signals Intelligence. UAS = Unmanned Aerial System. MALE = Medium-Altitude Long-Endurance. ISR = Intelligence, Surveillance & Reconnaissance. AUV = Autonomous Underwater Vehicle. USV = Unmanned Surface Vessel. RF = Radio Frequency. DSP = Digital Signal Processing. iDEX = Innovations for Defence Excellence (Indian MoD scheme). MoQ = Minimum order Quantity. INR = Indian Rupee.

### Strategy

**Type:** Output/Reporting (narrative strategy sheet) **1. Functional Overview:** The strategic narrative — a label/value table presenting Vision (10-yr), Mission, the new-age-prime operating model, the operating thesis vs. legacy primes, the core USP, the five strategic pillars, compressed "capability waves," the modelled margin trajectory, the funding strategy, key risks & mitigants, and a "how to read this workbook" pointer. **2. Strategic Significance:** This is the qualitative spine of the investor pitch. It articulates the core value proposition that the financial model is built to prove: industrialise six pre-designed defense product lines on commercial-software cycle times; convert owned IP and the iDEX-anchored ₹210 Cr ESM MoQ into early revenue; expand gross margin from ~25% (Y1) toward 70–80% (Y10) via BoM learning, platform reuse, and a growing software/AI mix; and fund growth through three stage-gated equity rounds totalling ₹1,100 Cr (Seed 450, Series A 400, Series B 250) plus ₹200 Cr venture/PSU debt. It directly grounds the capital-efficiency and defense-penetration themes. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: none — manual narrative input (it *describes* model outputs such as the margin trajectory, but does not pull live cell references).

- Downstream outputs: none. Verified: zero inbound references to `Strategy!`. Purely narrative/context. **4. Structural Detail & Key Formulas:**

- Structure: range B2:C14, 14 rows × 3 cols, 0 formulas. A single 2-column label/value table: column B = topic label (Vision, Mission, Operating model, Operating thesis, Core USP, Strategic pillars, Capability waves, Margin trajectory, Funding strategy, Key risks & mitigants, How to read), column C = the prose. All text/string.

- Key formulas: none. Representative cell: `C9` (Strategic pillars) = "1) Platform Engineering - five reusable tech modules (RF · DSP · SysEng · SW · AI). 2) Multi-Domain Coverage - Air (UAS)…". `C12` (Funding strategy) names the ₹1,100 Cr equity stack + ₹200 Cr debt. **5. Glossary of Terms:** NRE = Non-Recurring Engineering (one-time design/development cost). BoM = Bill of Materials (unit hardware cost). RF / DSP / SysEng / SW / AI = the five reusable platform engineering modules (Radio-Frequency, Digital Signal Processing, Systems Engineering, Software, Artificial Intelligence/ML). ESM = Electronic Support Measures (the EW receiving system; the iDEX MoQ product). MoQ = Minimum order Quantity. PSU = Public Sector Undertaking (Indian state-owned enterprise). Seed/Series A/B = staged equity-financing rounds. C-UAS = Counter-UAS. MVP = Minimum Viable Product. DCS = Direct Commercial Sale. FMS = Foreign Military Sales.

### MarketPositioning

This sheet contains two logical tables: a scored competitive-landscape matrix (B4:I20) and a qualitative positioning-summary block (B22:I26).

#### Table A — Competitive landscape scoring matrix (B4:I20)

**Type:** Calculation Engine (self-contained scoring) — but Output/Reporting in workbook terms (no downstream consumers) **1. Functional Overview:** A 0–4 capability scorecard rating NDAD ("Our platform firm") against six competitor archetypes (Tier-1 prime, Specialty RF vendor, C-UAS pure-play, UAS pure-play, AUV/USV specialist, Defense AI startup) across 15 capability dimensions, with a SUM composite score per column. **2. Strategic Significance:** Quantifies the differentiation thesis for investors: NDAD scores a leading composite **55** vs. the broad Tier-1 prime's **42** and every pure-play in the 27–29 range. NDAD's structural advantages cluster exactly where the platform model is supposed to win — platform reuse / amortised NRE, time-to-market for new variants, cost-to-deliver (NRE per $ revenue), software/AI revenue mix, and capital efficiency (revenue per $ raised) — all scored 4. It concedes primes lead on scale, clearances, and export/FMS readiness, which keeps the story credible. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: none — manual analyst scores (0–4) entered by hand into C5:I19.

- Downstream outputs: none. Verified: zero inbound references to `MarketPositioning!`. The composite scores are presentation-only; they do not feed the three-statement model. **4. Structural Detail & Key Formulas:**

- Structure: header row R4 (B4 "Capability dimension" + 7 competitor columns C:I); 15 scored dimension rows (R5:R19); composite-score row R20. Dimensions × competitors = 15 × 7 integer-score grid. Data types: integers 0–4.

- Key formulas (7 total, all in row 20): `C20` `=SUM(C5:C19)` → 55 (NDAD); `D20` `=SUM(D5:D19)` → 42 (Tier-1 prime); `E20` `=SUM(E5:E19)` → 29; `F20` `=SUM(F5:F19)` → 29; `G20` `=SUM(G5:G19)` → 27; `H20` `=SUM(H5:H19)` → 27; `I20` `=SUM(I5:I19)` → 28. Each simply totals its column's 15 capability scores. **5. Glossary of Terms:** AESA = Active Electronically Scanned Array. EW/SIGINT = Electronic Warfare / Signals Intelligence. C-UAS = Counter-UAS (anti-drone). UAS = Unmanned Aerial System. MALE = Medium-Altitude Long-Endurance. AUV/USV = Autonomous Underwater Vehicle / Unmanned Surface Vessel. NRE = Non-Recurring Engineering. FMS = Foreign Military Sales. RF = Radio Frequency. Score legend: 0 = absent, 1 = weak, 2 = partial, 3 = strong, 4 = leader.

#### Table B — Positioning summary (B22:I26)

**Type:** Output/Reporting (narrative) **1. Functional Overview:** A prose annex to the scorecard: the 0–4 score legend, the Differentiation statement, the "Primes vs. us" trade-off, and the "Path to category leadership." **2. Strategic Significance:** Converts the numeric scorecard into the narrative claim — only the platform firm spans all three domains AND amortises RF/DSP/SysEng/SW/AI across six product lines; the path to leadership is to win one marquee program per vertical in Y2–Y5, build reference accounts, develop an allied/FMS pipeline, and monetize Military AI. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: none — manual narrative input.

- Downstream outputs: none. Purely narrative/context. **4. Structural Detail & Key Formulas:** Structure: B22 section header, then four label/value text rows (R23–R26). 0 formulas; all text/string. **5. Glossary of Terms:** (see Table A above — same domain terms; FMS = Foreign Military Sales.)

### Roadmap

**Type:** Output/Reporting (narrative timeline / Gantt-style grid) **1. Functional Overview:** A 10-year (Y1–Y10) phase-status grid for 14 tracks — the five platform modules (M1 RF, M2 DSP, M3 SysEng, M4 SW, M5 AI/ML), the six product verticals (V1–V6), and three enabling tracks (Facilities & cert, Funding milestones, Export/FMS). Each cell carries a single-letter stage code (R/D/Q/S/X) per year, with a phase/focus description in column C and a legend block at the bottom. **2. Strategic Significance:** Visualises the "capability waves" sequencing that underpins the revenue ramp and the capital-efficiency story: V2 EW/SIGINT and V6 Military AI ship in Y1 (early cash), V1 AESA and V3 C-UAS qualify early and ship by Y2–Y3, while the longest pole — V4 MALE UAS — researches/develops Y1–Y3 and ships from Y5. It shows facilities moving from partner labs (Y1–Y2) to owned (Y3+) and funding milestones tapering at later stages — i.e., front-loaded investment, then scale-out — reinforcing the staged, de-risked execution narrative. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: none — manual narrative input.

- Downstream outputs: none. Verified: zero inbound references to `Roadmap!`. The timeline communicates sequencing but does not numerically drive any sheet (the actual ship-year economics live in the V1–V6 and Backlog sheets). **4. Structural Detail & Key Formulas:**

- Structure: range B2:M21, 21 rows × 13 cols, 0 formulas. Header row R4 (Track | Phase/focus | Y1…Y10). 14 track rows (R5:R18), then a Legend block (R20:R21). Data types: text labels + single-char status codes.

- Key formulas: none. The grid is hard-typed letter codes, e.g. `D12:M12` (V1 AESA Radar) = D, Q, S, S, S, X, X, X, X, X. Legend (R21) defines: R = Research/seed, D = Develop, Q = Qualify/cert, S = Ship/scale, X = Export/scale-out. **5. Glossary of Terms:** M1–M5 = the five platform modules (RF, DSP, SysEng, SW, AI/ML). V1–V6 = product verticals. Stage codes: R = Research/seed, D = Develop, Q = Qualify/cert, S = Ship/scale, X = Export/scale-out. C2 = Command & Control. MOSA/FACE = Modular Open Systems Approach / Future Airborne Capability Environment (open-architecture standards). FMS = Foreign Military Sales. DCS = Direct Commercial Sale. ESM = Electronic Support Measures.

### Platform

This sheet is the one calculation-bearing sheet in this slice (70 formulas) and stacks **three logical tables**: (A) NRE investment by module, (B) module maturity, and (C) effective reuse strength. Tables A and C feed downstream financial sheets — this sheet is a genuine model driver, NOT pure front-matter.

#### Table A — Platform NRE investment by module + cumulative (B5:M12)

**Type:** Input/Assumption + Calculation Engine (manual NRE inputs with SUM/running-total formulas) **1. Functional Overview:** The shared-platform engineering budget. Five module rows (RF/Microwave, DSP, Systems Engineering, Embedded & Mission Software, AI/ML) carry hand-entered annual NRE spend (₹ Cr) for Y1–Y10, with a "Total platform NRE" row (SUM) and a "Cumulative platform NRE" running-total row. **2. Strategic Significance:** This is the capital-efficiency engine made numeric. It shows the single shared investment — ₹101 Cr in Y1, peaking at ₹210 Cr in Y2, then decaying to ₹3.1 Cr by Y10 (cumulative ₹575.2 Cr) — that six product lines amortise against, instead of each vertical re-paying full NRE. The front-loaded, decaying curve embodies the "build the platform once, harvest reuse forever" thesis and directly sizes the early capital raise. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: module NRE cells D6:M10 are manual yellow inputs (none upstream).

- Downstream outputs: **active driver.** `Platform!D11:M11` (Total platform NRE) flows to `R&D\\\_NRE!D5:M5` ("Platform NRE (shared)") and to `ReuseMatrix!D48:M48`; individual module rows D6:M10 flow row-by-row to `R&D\\\_Buckets!C7:M11` (capitalisation bucketing). From R&D\_NRE, platform NRE rolls into the **P&L** R&D/NRE expense line (`P&L!D12 ='R&D\\\_NRE'!E12`) and the tax/amortisation bridges — i.e., it ultimately hits P&L → CashFlow → BalanceSheet. **4. Structural Detail & Key Formulas:**

- Structure: section header R5; 5 module rows (R6:R10) with Module name (B), Scope text (C), and Y1–Y10 NRE values (D:M, numeric ₹ Cr); Total row R11; Cumulative row R12.

- Key formulas: `D11` `=SUM(D6:D10)` → 101 — total platform NRE for Y1 (this is the cell consumed by R&D\_NRE). `E11` `=SUM(E6:E10)` → 210 (Y2 peak). `D12` `=D11` → 101 and `E12` `=D12+E11` → 311 … `M12` `=L12+M11` → 575.2 — the cumulative running total of platform NRE across the horizon. **5. Glossary of Terms:** NRE = Non-Recurring Engineering. RF/Microwave = Radio-Frequency module (T/R modules, receivers, antennas, GaN MMICs). T/R = Transmit/Receive. GaN = Gallium Nitride. MMIC = Monolithic Microwave Integrated Circuit. PA/LNA = Power Amplifier / Low-Noise Amplifier. DBF = Digital Beam Forming. DSP = Digital Signal Processing. FPGA = Field-Programmable Gate Array. SDR = Software-Defined Radio. SysEng = Systems Engineering. MIL-STD-810/461/704 = US military environmental/EMI/power standards. V&V = Verification & Validation. RTOS = Real-Time Operating System. C2 = Command & Control. MOSA/FACE = open-architecture standards. CV = Computer Vision. MLOps = Machine-Learning Operations.

#### Table B — Platform module maturity (0..1) (B14:M19)

**Type:** Input/Assumption (manual TRL-style maturity curves) **1. Functional Overview:** A 0–1 maturity ("TRL-style") progression for each of the five modules across Y1–Y10, used as the raw "reuse strength" before the global multiplier is applied. E.g., RF rises 0.55 → 0.99; AI/ML rises from 0.25 (Y1, least mature) → 0.99 (Y10). **2. Strategic Significance:** Encodes the platform "flywheel" — each module's qualified work matures over time so that successive products inherit a rising share of proven engineering. The fact that AI/ML starts lowest (0.25) but is the heaviest-reuse module reflects the highest-growth, highest-leverage bet in the portfolio. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: manual yellow inputs (D15:M19).

- Downstream outputs: consumed only by Table C on the same sheet (rows 21–25 multiply these by the Assumptions multiplier); Table C in turn feeds ReuseMatrix. So Table B is an indirect upstream driver of the reuse economics. **4. Structural Detail & Key Formulas:**

- Structure: section header R14; 5 module rows (R15:R19) with module name (B), a "TRL-style progression - used as reuse strength" note (C), and Y1–Y10 maturity decimals (D:M, 0..1).

- Key formulas: none — all hard-typed decimals. Representative: `D19:M19` (AI/ML) = 0.25, 0.5, 0.7, 0.83, 0.9, 0.94, 0.96, 0.97, 0.98, 0.99. **5. Glossary of Terms:** TRL = Technology Readiness Level (a 1–9 maturity scale; here normalised 0..1). Module abbreviations as in Table A.

#### Table C — Effective reuse strength per module (= maturity × multiplier, capped 1) (B20:M25)

**Type:** Calculation Engine **1. Functional Overview:** Converts Table B's raw maturity into "effective reuse strength" per module per year by multiplying maturity by a global reuse multiplier from the Assumptions sheet and capping the result at 1.0. These are the values the rest of the model uses to compute how much vertical NRE each product line avoids. **2. Strategic Significance:** This is the mathematical heart of the cost-avoidance / capital-efficiency claim. The effective-reuse curve is precisely what lets six product lines be built for far less than their standalone counterfactual (~~₹1,350 Cr standalone vs. ~~₹994 Cr cost avoidance cited in the investor narrative). The single Assumptions multiplier makes the entire reuse thesis a one-knob sensitivity lever for investors. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: `Platform!D15:M19` (Table B maturity, same sheet) × `Assumptions!$C$26` ("Platform reuse maturity multiplier", currently = 1).

- Downstream outputs: **active driver.** `Platform!D21:M25` are the per-module reuse coefficients consumed by `ReuseMatrix!D15:M20` (which dot-products each vertical's module-mix weights C6:G11 against these reuse strengths). ReuseMatrix then produces post-reuse leveraged vertical NRE → `R&D\\\_NRE!D6:M6` → P&L. So Table C ultimately drives the R&D/NRE expense line and the "NRE avoided by platform reuse" KPI (`KPIs!C14 ='R&D\\\_NRE'!D8-'R&D\\\_NRE'!D6`). **4. Structural Detail & Key Formulas:**

- Structure: section header R20; 5 "…- effective" module rows (R21:R25) with Y1–Y10 computed coefficients (D:M). 50 formulas (5 rows × 10 years).

- Key formulas: `D21` `=MIN(1,D15\\\*Assumptions!$C$26)` → 0.55 — RF effective reuse = RF maturity (0.55) × global multiplier (1), capped at 1. The MIN(1,…) cap guarantees reuse strength never exceeds 100%. `D25` `=MIN(1,D19\\\*Assumptions!$C$26)` → 0.25 (AI/ML, Y1). The pattern repeats across all 50 cells, each pointing to its Table-B maturity cell and the absolute reference `$C$26`. **5. Glossary of Terms:** Effective reuse strength = qualified maturity actually creditable as reuse after the global multiplier. `Assumptions!C26` = "Platform reuse maturity multiplier" (global dial, =1). MIN(1,…) = Excel cap function. ReuseMatrix = the downstream sheet that converts these coefficients + per-vertical module-mix weights into post-reuse NRE per product line.

### Cross-sheet anomalies & architecture notes (this slice)

1. **Platform is a real driver, not front-matter.** The scope brief and the architecture note hypothesised these sheets are "context/reference rather than calculation inputs." That holds for Cover, Strategy, MarketPositioning, and Roadmap (all 0 inbound references, verified). But **Platform is an active upstream input to the cost build**: row 11 (Total NRE) → R&D\_NRE, R&D\_Buckets, ReuseMatrix; rows 21–25 (effective reuse) → ReuseMatrix; both ultimately reach P&L row 12 and the KPIs. This is consistent with the broader "cost build → P&L → CashFlow & BalanceSheet" architecture (R&D\_NRE is one of the named cost-build sheets), but it means Platform should be classed with the drivers, alongside Assumptions and V1–V6, not with the narrative front matter.

2. **MarketPositioning's 7 formulas are inert.** They are column SUMs (composite scores) with zero downstream consumers — presentation math only, fully consistent with the architecture (no contradiction).

3. **Column convention.** All five sheets that use a year grid (Roadmap, Platform) place Y1–Y10 in columns D:M, matching the workbook-wide "C:L for statements, D:M for Funding" note only loosely — here the year axis simply starts at column D because column C holds a Scope/Phase description. Downstream, Platform!D11 (Y1) maps to R&D\_NRE!D5 (Y1), so the D:M→D:M alignment is internally consistent.

4. **The reuse multiplier is currently neutral.** `Assumptions!C26 = 1`, so Table C effective-reuse values equal Table B maturity exactly today. This is the single sensitivity lever an investor would flex to stress-test the entire platform-reuse cost-avoidance thesis.

## 2. R&D Economics & Reuse Moat

This section documents the three sheets that quantify NDAD's core moat — reusable platform IP amortised across six product verticals — and the accounting machinery that turns that reuse into capital efficiency on the three financial statements. The economic chain is: **Platform module-maturity curves → ReuseMatrix (how much engineering each vertical inherits) → R&D\_Buckets (Ind AS 38 expense/capitalise split of the shared platform spend) → R&D\_NRE (the consolidated R&D/NRE P&L line, intangible additions, and amortisation) → P&L, CashFlow, BalanceSheet, KPIs, BreakEven.**

All values are in INR Crore (₹ Cr). Horizon Y1–Y10 maps to columns D:M on these three sheets (col C carries source/driver notes). Consuming statement sheets (P&L, CashFlow, BalanceSheet) use cols C:L for Y1–Y10, so a one-column right-shift occurs at the boundary (e.g. `R&D\\\_NRE!D12` → `P&L!C12`).

### Sheet: ReuseMatrix (49 × 14, 236 formulas)

**Type:** Calculation Engine (with one Input block: module composition %) **1. Functional Overview:** The quantitative heart of the platform-reuse moat. It computes, per vertical (V1–V6) and per year, the effective reuse-savings % the vertical inherits from the shared platform, then applies `(1 − reuse%)` to each vertical's *gross standalone* NRE to produce the *leveraged* (post-reuse) NRE actually incurred. It rolls those up into portfolio-level totals and an explicit reuse-savings (cost-avoidance) line. **2. Strategic Significance:** This is the sheet that makes the "₹575 Cr platform investment compounds into ~₹994 Cr of cost avoidance" thesis auditable. Reuse % is not assumed flat — it is *derived* as `module-composition × platform-maturity`, so a vertical heavy in mature modules (RF/DSP/SysEng) inherits more reuse than an AI-heavy vertical early on, and every vertical converges to ~99% reuse by Y10. This is the capital-efficiency engine: it removes net-new NRE from each successive vertical, which is what lets one engineering organisation field six product lines without six full programme budgets (the "product squads, not programme directorates" operating model in section 7). **3. Modeling Impact & Data Flow:**

- Upstream dependencies:

  - `Platform!D21:M25` — *effective reuse strength per module* (RF, DSP, SysEng, Embedded SW, AI/ML), each `=MIN(1, maturity × Assumptions!$C$26)` where maturity is a TRL-style curve on `Platform!D15:M19` and `Assumptions!C26` is a reuse multiplier. These are the columns the reuse formula in block B dots against module composition.

  - Block A (`C6:G11`) module-composition percentages are **hard-coded inputs** (the only non-derived numeric block on the sheet).

  - Gross vertical NRE schedules (rows 24/27/30/33/36/39) are **hard-coded inputs** ("Total ~209/114/152/523/247/105 INR Cr over 10y" per vertical).

- Downstream outputs:

  - `R&D\\\_NRE!D6:M6` ("Σ Leveraged vertical NRE, post-reuse") = sum of the six leveraged-NRE rows `ReuseMatrix!\\\{25,28,31,34,37,40\\\}` — this is the single largest feed into the R&D/NRE P&L line.

  - `R&D\\\_NRE!D8:M8` ("Σ Gross NRE, standalone memo") = sum of the six gross-NRE rows `ReuseMatrix!\\\{24,27,30,33,36,39\\\}`.

  - **No other sheet references `ReuseMatrix!` by name** — its entire downstream influence is routed through R&D\_NRE rows 6 and 8 (and from there into KPIs row 14/40 and BreakEven C36, which reconstruct gross−leveraged = reuse savings). The sheet's portfolio-total block D (rows 45–49) is a self-contained reconciliation/display copy that no other sheet reads. **4. Structural Detail & Key Formulas:**

- Structure: four labelled blocks, all keyed by the six verticals down the rows and Y1–Y10 across D:M.

  - **A. Module composition per vertical** (rows 5–11): inputs, rows sum to 100% (`H6=SUM(C6:G6)` check column).

  - **B. Effective reuse savings % per vertical/year** (rows 13–20): composition × platform maturity.

  - **C. Gross vs leveraged NRE per vertical** (rows 22–41): for each vertical a gross input row, a leveraged formula row, and a per-vertical "savings" row.

  - **D. Portfolio NRE totals** (rows 43–49): Σ gross, Σ leveraged, Σ savings, + standalone platform NRE, total.

- Key formulas (verbatim):

  - `D15` `=C6\\\*Platform!D21+D6\\\*Platform!D22+E6\\\*Platform!D23+F6\\\*Platform!D24+G6\\\*Platform!D25` — V1's Y1 effective reuse % = dot-product of its module mix (45% RF, 25% DSP, 20% SysEng, 8% SW, 2% AI) with the five module maturities. Result 0.5225 (≈52% reuse for AESA in Y1). The same pattern fills rows 15–20 for all six verticals.

  - `D25` `=D24\\\*(1-D15)` — V1 leveraged NRE = gross ₹62.7 Cr × (1 − 0.5225) = ₹29.94 Cr. This is the (1 − reuse%) lever applied per cell; rows 28/31/34/37/40 replicate it for V2–V6.

  - `D26` `=D24-D25` — per-vertical reuse savings (cost avoided), ₹32.76 Cr for V1 in Y1.

  - `D47` `=D45-D46` — portfolio reuse savings = Σ gross − Σ leveraged (₹119.9 Cr avoided in Y1, peaking ~₹211 Cr in Y3).

  - `D49` `=D46+D48` — total R&D/NRE = leveraged vertical NRE + standalone platform NRE (display roll-up; the live P&L number is assembled in R&D\_NRE, not here). **5. Glossary of Terms:**

- **NRE (Non-Recurring Engineering):** one-time design/development cost to bring a product to production-ready state (distinct from recurring per-unit BoM/COGS).

- **Gross / standalone NRE:** the counterfactual cost of building a vertical from scratch with no platform to inherit from.

- **Leveraged / post-reuse NRE:** the NRE actually incurred after subtracting the reuse-savings %.

- **Reuse % (reuse strength / savings):** fraction of a vertical's engineering inherited from already-qualified platform modules; here `Σ(module-mix × module-maturity)`, capped at 1.

- **Module composition:** how a vertical's engineering decomposes across the five platform modules M1–M5 (RF, DSP, SysEng, Embedded SW, AI/ML).

- **Platform maturity (TRL-style):** Technology-Readiness-Level-style progression curve per module, rising toward ~0.99.

### Sheet: R&D\_Buckets (104 × 13, 465 formulas)

**Type:** Calculation Engine (Ind AS 38 capitalisation engine) with two % input blocks **1. Functional Overview:** Takes the *shared platform* NRE (the M1–M5 module spend, sourced from the Platform sheet) and splits each module-year into three accounting buckets — **research (expensed), qualifying development (capitalised), and non-eligible development (expensed)** — under an evidence-led Ind AS 38 / AS 26 policy. It then converts those % into ₹ Cr amounts, derives the financial-statement outputs (book-expensed platform R&D, capitalised additions, amortisation), and runs a tax bridge memo. This is the *platform* leg of R&D; the *vertical* leg lives in ReuseMatrix. **2. Strategic Significance:** This sheet is the IP-ownership and capital-efficiency accounting layer. By capitalising qualifying development (a rising ~26%→75% of platform NRE, weighted), it converts R&D spend into a balance-sheet intangible asset — the reusable IP that *is* the moat — and shifts cost out of EBITDA into D&A, improving EBITDA-margin optics 2–4 ppt in Y3–Y6 (per investor section 4). The policy discipline (research expensed immediately; only evidence-backed development capitalised) is exactly the Ind AS 38 posture the Audit Committee oversees (section 9), making the capitalisation defensible rather than aggressive. **3. Modeling Impact & Data Flow:**

- Upstream dependencies:

  - `Platform!C6:M10` / `Platform!D11:M11` — source platform NRE by module (rows 7–12 mirror the Platform sheet; `D12=SUM(D7:D11)` checks to `Platform!D11`).

  - `Assumptions!$C$58` (`NRE\\\_Amort\\\_Life` = 6 yrs) — drives the straight-line amortisation OFFSET window in row 90.

  - Input %: research-expensed % (rows 16–20) and capitalised-development % (rows 25–29) are hard-coded; non-eligible % (rows 34–38) is the residual `1 − research − capitalised`.

- Downstream outputs (consumed by R&D\_NRE and KPIs):

  - `R&D\\\_Buckets!D87:M87` (book-expensed platform R&D) → `R&D\\\_NRE!D17:M17` (and `KPIs!C53` reads row 82 detail).

  - `R&D\\\_Buckets!D88:M88` (capitalised R&D additions) → `R&D\\\_NRE!D16:M16` (intangible additions) and `KPIs!C52`. Row 88's own note: *"Feeds R&D\_NRE row 16 and CashFlow CFI."*

  - `R&D\\\_Buckets!D89:M89` (weighted capitalisation %) → `R&D\\\_NRE!D14:M14` and `KPIs!C50`.

  - `R&D\\\_Buckets!D90:M90` (amortisation of capitalised R&D) → `R&D\\\_NRE!D18:M18` (which then flows to P&L D&A row 19 and BalanceSheet accum-amort row 38).

  - `R&D\\\_Buckets!D60:M60` (total research expensed) → `KPIs!C51`.

  - Note: rows 99–101 of this sheet *read back* from R&D\_NRE (`'R&D\\\_NRE'!D16/D18`) and `'P&L'!C27` to build a tax-basis-PBT memo — a deliberate reverse reference for the tax bridge, not a circularity in the core build. **4. Structural Detail & Key Formulas:**

- Structure: ten labelled blocks (A–J), each a 5-module × 10-year grid:

  - A Source platform NRE (rows 5–12) · B Research-expensed % input (14–20) · C Capitalised-development % input (23–29) · D Non-eligible development % calc (32–38) · E 100% bucket check (41–49) · F Research expensed ₹ (52–60) · G Development capitalised ₹ (63–71) · H Development expensed ₹ (74–82) · I Financial-statement outputs (85–94) · J Tax bridge memo (97–101).

- Key formulas (verbatim):

  - `D34` `=1-D16-D25` — non-eligible development % = residual after research and capitalised; guarantees the three buckets sum to 100% (validated by `D49 =IF(AND(D43=1,…),"OK","CHECK")`, which returns "OK" across all years).

  - `D65` `=D7\\\*D25` — capitalised development ₹ = source module NRE × capitalised % (RF/Microwave Y1 = ₹45 Cr × 25% = ₹11.25 Cr).

  - `D87` `=SUM(D60,D82)` — total book-expensed platform R&D = research expensed + non-eligible development expensed (₹74.75 Cr Y1).

  - `D89` `=IFERROR(D88/D12,0)` — weighted platform capitalisation % (capitalised additions ÷ total platform NRE), rising 26%→75%.

  - `D90` `=IFERROR(SUM(OFFSET(D$88,0,-MIN(COLUMN(D$88)-COLUMN($D$88),Assumptions!$C$58-1),1,MIN(COLUMN(D$88)-COLUMN($D$88)+1,Assumptions!$C$58)))/Assumptions!$C$58,0)` — straight-line amortisation: an OFFSET window walks back up to `NRE\\\_Amort\\\_Life`−1 (5) prior years of capitalised additions and divides the rolling sum by 6, so each tranche amortises evenly over 6 years.

  - `D94` `=D60+D71+D82-D12` — integrity check that the three bucketed amounts reconstitute the source platform NRE exactly (returns 0 every year). **5. Glossary of Terms:**

- **R&D buckets:** the three accounting classifications of platform spend — research (always expensed), qualifying development (capitalised), non-eligible development (expensed).

- **Capitalisation (Ind AS 38 / AS 26):** recognising qualifying development cost as an intangible asset rather than an immediate expense, permitted only when technical feasibility, intent/ability to complete, future economic benefit, resources, and reliable measurement are demonstrable.

- **Amortisation:** straight-line write-down of the capitalised intangible over its useful life (6 yrs here, `Assumptions!C58`); flows into D&A.

- **Weighted capitalisation %:** capitalised additions as a share of total platform NRE in a year.

- **Research vs development:** research = expensed early-stage work; development = later-stage work that may qualify for capitalisation.

- **Tax-basis PBT bridge:** memo reconciling book PBT to a tax-basis PBT by adding back book amortisation and deducting current-year eligible capitalised development (subject to CA review).

### Sheet: R&D\_NRE (19 × 14, 111 formulas)

**Type:** Output/Reporting (consolidation hub) — assembles the single P&L R&D/NRE line and the intangible-asset feeds **1. Functional Overview:** The consolidation layer that combines the *platform* R&D legs (from R&D\_Buckets) with the *vertical* leveraged NRE (from ReuseMatrix), adds R&D personnel cost (from Headcount) and a 30% NRE contingency uplift, and produces the authoritative `TOTAL R&D / NRE EXPENSE (P&L)` line plus the capitalisation/amortisation values that downstream statements consume. It is the funnel through which everything in this section reaches the three-statement model. **2. Strategic Significance:** This is where the reuse moat shows up as a *number on the P&L*. Row 9 ("NRE avoided by platform reuse vs standalone build") makes the cost-avoidance explicit (~~₹120 Cr Y1 rising to ~~₹211 Cr Y3), and the P&L line stays roughly flat-to-declining even as six verticals come online — the visible proof of capital efficiency. The capitalisation split it carries (rows 16–18) is what converts moat-building spend into a depreciating IP asset rather than a pure cash burn. **3. Modeling Impact & Data Flow:**

- Upstream dependencies:

  - `Platform!D11:M11` → row 5 (Platform NRE, shared).

  - `ReuseMatrix!\\\{25,28,31,34,37,40\\\}` → row 6 (Σ leveraged vertical NRE); `ReuseMatrix!\\\{24,27,30,33,36,39\\\}` → row 8 (Σ gross, memo).

  - `Headcount!D67:M67` → row 7 (R&D personnel cost).

  - `R&D\\\_Buckets!D87:M87` → row 17; `D88:M88` → row 16; `D89:M89` → row 14; `D90:M90` → row 18.

  - `Assumptions!C58` → row 15 (amortisation life label).

- Downstream outputs (the exact consuming cells traced across all 26 sheets):

  - **P&L R&D expense line:** `R&D\\\_NRE!D12:M12` → `P&L!C12:L12` (R&D / NRE expense).

  - **P&L D&A line:** `R&D\\\_NRE!D18:M18` → `P&L!C19:L19` (`=Capex!…39 + 'R&D\\\_NRE'!…18`, amortisation of capitalised R&D inside D&A).

  - **P&L tax/NOL block:** rows 16 & 18 feed `P&L!C29/C30/C32` (NOL added/utilised/taxable income) and the tax-bridge memo `P&L!C41` (`='R&D\\\_NRE'!D18`) and `P&L!C42` (`='R&D\\\_NRE'!D16`).

  - **CashFlow CFI:** `R&D\\\_NRE!D16:M16` → `CashFlow!C19` (`=C17+C18-'R&D\\\_NRE'!D16`, capitalised R&D as investing outflow) and the memo `CashFlow!C32` (`=-'R&D\\\_NRE'!D16`).

  - **BalanceSheet intangibles:** row 16 & row 18 → `BalanceSheet!C15` (net intangibles `='R&D\\\_NRE'!D16-'R&D\\\_NRE'!D18`, then cumulative), `BalanceSheet!C37` (gross capitalised R&D, cumulative, `=row 16`), `BalanceSheet!C38` (accumulated amortisation, cumulative, `=row 18`).

  - **KPIs:** row 12 → `KPIs!C39` (`=SUM('R&D\\\_NRE'!D12:M12)`); rows 6 & 8 → `KPIs!C14`/`C40` and per-year reuse-savings `KPIs!C14=D8-D6`.

  - **BreakEven:** `R&D\\\_NRE!D12:M12` → `BreakEven!C17` (`=INDEX('R&D\\\_NRE'!$D$12:$M$12,$C$4)`); rows 6 & 8 → `BreakEven!C36`.

  - This sheet is the most-referenced of the three: **134 external references** across KPIs, P&L, CashFlow, BalanceSheet, BreakEven. **4. Structural Detail & Key Formulas:**

- Structure: one continuous schedule, B = line label, C = source note, D:M = Y1–Y10. Three logical bands:

  - **Component build** (rows 5–9): Platform NRE, Σ leveraged vertical NRE, R&D personnel, Σ gross memo, NRE-avoided counterfactual.

  - **P&L line** (rows 11–12): the consolidated total.

  - **Capitalisation block (C4)** (rows 13–19): cap rate, amort life, capitalised additions, expensed portion, amortisation, contingency uplift.

- Key formulas (verbatim):

  - `D12` `=D17+D6+D7+D19` — **TOTAL R&D / NRE EXPENSE (P&L)** = platform R&D expensed (R&D\_Buckets row 87 via row 17) + leveraged vertical NRE (row 6) + R&D personnel (row 7) + 30% contingency (row 19). Note: it *excludes* the capitalised portion (row 16) — that flows to the balance sheet, with the in-period amortisation (row 18) reaching the P&L through D&A only, avoiding double-count (per the row-12 source note).

  - `D6` `=ReuseMatrix!D25+ReuseMatrix!D28+ReuseMatrix!D31+ReuseMatrix!D34+ReuseMatrix!D37+ReuseMatrix!D40` — the live consumption of ReuseMatrix's leveraged vertical NRE.

  - `D9` `=D8-D6` — NRE avoided by platform reuse (counterfactual cost-avoidance memo).

  - `D19` `=0.3\\\*(D5+D6)` — 30% NRE contingency uplift on platform + leveraged vertical NRE (realistic AESA/MALE/AUV cost cushion).

  - `D16` `='R&D\\\_Buckets'!D88` — development capitalised (intangibles addition), the value routed to BalanceSheet/CashFlow. **5. Glossary of Terms:**

- **R&D / NRE expense (P&L line):** the in-period income-statement charge for research, expensed development, leveraged vertical NRE, R&D personnel, and contingency — net of the capitalised portion.

- **Capitalised portion / intangibles addition:** qualifying development moved to the balance sheet instead of being expensed (row 16).

- **Amortisation (in D&A):** straight-line write-down of the capitalised intangible recognised on the P&L via the D&A line (row 18 → P&L row 19).

- **NRE contingency:** 30% uplift buffering optimistic engineering estimates for hardware-heavy verticals.

- **Counterfactual / NRE avoided:** Σ gross standalone NRE minus Σ leveraged NRE — the quantified value of the reuse moat.

- **R&D personnel cost:** salaried platform-engineering headcount expense (from Headcount), the recurring human side of platform investment.

- **Double-count avoidance:** the modelling rule that capitalised R&D hits cash (CFI) and the balance sheet, and reaches the P&L only through amortisation — never both as expense and as capex.

## 3. Assumptions & Vertical Product Models

This section documents the eight driver sheets that define NDAD's product economics: the global `Assumptions` register and the six vertical product models (`V1\\\_AESA` … `V6\\\_MilAI`). All values are in Indian Rupees Crore (₹ Cr), horizon Y1–Y10.

> **Architectural rule that governs this entire section (authoritative):** Consolidated reported revenue is **Backlog-driven, not V-sheet-driven.** `Revenue!D6:M11` link to `Backlog!D89:M94` (recognized deliveries = opening backlog × per-vertical delivery rate). Every V-sheet carries the banner *"READ ONLY SUPPORTING DETAIL — Editing units/ASP here does NOT change consolidated revenue, but DOES rescale COGS."* The V1–V6 sheets feed the model in exactly **one** way: the COGS-ratio rescale in `Revenue!D23:M28`, where each vertical's BoM COGS is scaled by `(backlog-recognized revenue ÷ V-sheet revenue)` to preserve the gross-margin %. Editing units or ASP on a V-sheet moves COGS (and therefore gross margin) but never the top line.

### 3.1 Assumptions — Global Planning Register

**Type:** Input/Assumption **1. Functional Overview:** The single, authoritative register of every global planning lever — currency, tax, WACC, escalation, learning-curve constants, working-capital days, overhead percentages, and R&D capitalization policy. It is referenced by name/cell across the whole workbook. Dimensions 66×4; effectively all hand-keyed inputs with exactly **one formula** (`C53 =C52`, a self-reference alias). **2. Strategic Significance:** Encodes the capital-efficiency thesis: an 18% WACC reflecting unlisted Indian defense equity cost-of-capital; a Wright's-Law BoM learning curve (0.92 per doubling) that drives the gross-margin climb from ~51% to ~67%; a blended 180-day DSO calibrated to the real mix of iDEX/Make-II (90–120d), MoD CapEx (240–365d) and export (120d) payment behavior; and a 60% R&D capitalization rate under Ind AS 38 that shifts platform cost out of EBITDA into D&A. The M9 fix note (R&D salary escalation cut 12%→4%) is a documented model-discipline correction. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: None — this is the root input sheet.

- Downstream outputs: Referenced workbook-wide. **Used heavily inside every V-sheet:** the ASP-elasticity exponent `Assumptions!$C$39` (=0.5), the BoM floor `Assumptions!$C$40` (=0.7), the learning-curve factor `Assumptions!$C$10` (=0.92), and the doubling log-base `Assumptions!$C$41` (=2) appear in the ASP and BoM formulas of all six verticals. Tax `C6`, WACC `C7`, escalation `C8/C9`, DSO/DPO/Inventory `C11:C13`, S&M/G&A/B&P `C15:C17`, and capitalization `C57:C59` feed P&L, CashFlow, BalanceSheet, Opex, R&D\_NRE and Funding. **Note the read-only relationship is one-directional here too:** Assumptions feeds the V-sheet detail, but the V-sheet revenue does not reach the consolidated top line (which is Backlog-driven). **4. Structural Detail & Key Formulas:**

- Structure: `A2` title; header row 3 (`Driver | Value | Note`); rows 4–66 are driver/value/note triples. A second labelled block begins at `B28` ("Defense-specific operating context"), then "Backlog & revenue flow drivers" (`B48`), "Product Pricing & Cost Assumptions" (`A50`), "R&D Capitalization & Amortization" (`A56`), "Working Capital & Funding" (`A61`), "Manufacturing & Warranty" (`A64`).

- Key assumptions (verbatim values):

  - `C5` Planning horizon = 10 yr; `C6` Corporate tax = 0.25; `C37` MAT rate = 0.15.

  - `C7` WACC = 0.18; `C8` Cost escalation = 0.04; `C9` R&D salary escalation = 0.04 (note: *"reduced from 12% to 4%"*).

  - `C10` BoM learning curve per doubling = 0.92 (Wright's law); `C39`/`C51` ASP elasticity exponent = 0.5; `C40` BoM floor = 0.7; `C41`/`C46`/`C54` log doubling base = 2.

  - `C11` DSO = 180 d; `C12` DPO = 45 d; `C13` Inventory = 90 d; `C14` retired (legacy WC% removed, row kept to preserve references).

  - `C15` S&M = 0.08; `C16` G&A = 0.07; `C17` B&P = 0.03 of revenue.

  - `C18` Export-control = 2; `C19` CMMC L3 = 14.25; `C20` AS9100/CMMI = 8.55 (annual bases, escalating; sum ≈ ₹24.8 Cr Y1).

  - `C21` PBG = 0.03; `C22` Advance = 0.15; `C23` BG fee = 0.011; `C62` BG collateral = 0.10.

  - `C25` Min cash reserve = 100 (triggers funding rounds); `C42` USD→INR = 95.

  - `C49` HW revenue lag = 15 mo (range 12–18); `C43` lag = 12 mo (hardware avg).

  - `C57` Platform NRE cap rate = 0.6; `C58` NRE amort life = 6 yr; `C59` Vertical NRE amort life = 5 yr.

  - `C65` Mfg overhead = 0.20 of direct material+labour; `C66` Warranty = 0.02 of COGS.

  - The **only formula:** `C53` `=C52` — `BoM\\\_Min\\\_Pct` aliases `BoM\\\_Floor\\\_Pct` (=0.5 on this sheet's later block; note the active V-sheet floor reference is `C40`=0.7).

- Column convention warning (`B38`): *"Y1 = col C on P&L/CashFlow/BalanceSheet/BreakEven/KPIs; Y1 = col D on Revenue/Headcount/Capex/Opex/Funding/Backlog/V1–V6/R&D\_NRE. DO NOT INSERT COLUMNS without re-auditing every cross-sheet reference."* **5. Glossary of Terms:** **WACC** weighted-average cost of capital (discount rate for NPV); **DSO/DPO** days sales outstanding / days payable outstanding; **BoM** bill of materials (unit hardware cost); **Wright's Law** cost falls by a fixed factor per cumulative-volume doubling; **ASP elasticity** exponent linking ASP decline to BoM decline (0.5 = square-root); **PBG/ABG** performance / advance bank guarantee; **MAT** Minimum Alternate Tax (India Sec 115JB book-profit floor); **NRE** non-recurring engineering (development cost, capitalized at 60% under **Ind AS 38**); **CMMC L3 / AS9100 / CMMI** US/aerospace cybersecurity & quality accreditations.

### 3.2 V1\_AESA — AESA Radar (the V-sheet archetype, documented in full)

**Type:** Calculation Engine (read-only supporting detail) **1. Functional Overview:** Unit-economics model for the AESA radar line across three variants (X-band Airborne, S-band Ground Surveillance, X-band Naval). For each variant it computes ASP, BoM, revenue, COGS and contribution margin per year, then rolls up V1 totals. Dimensions 36×14, 204 formulas. **Launch Y2.** This sheet is the structural template that V3–V6 replicate. **2. Strategic Significance:** AESA is a USD 5–7 bn/yr global market (7–9% CAGR) that India almost entirely imports; the MoD's stated direction is domestic substitution. Variant A leverages the partly-developed ESM RF/DSP front-end (reuse ~50% in Y1 rising to ~99% by Y10), the platform-flywheel mechanism that lets NDAD field a radar line off the V2 ESM investment. Selling prices ₹22–45 Cr; ~95 blended units/yr by Y10; Y10 share is a low single-digit % of the global market. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: `Assumptions!$C$39` (ASP elasticity 0.5), `$C$40` (BoM floor 0.7), `$C$10` (learning curve 0.92), `$C$41` (doubling base 2). All Y1 ASP/BoM/units are hand-keyed yellow inputs.

- Downstream outputs (**read-only**): V1 totals `D31:M31` (revenue) and `D32:M32` (COGS) are consumed by exactly one place — `Revenue!D23:M23`, the V1 COGS rescale: `=IFERROR(V1\\\_AESA!D32\\\*(D6/V1\\\_AESA!D31),0)`. The consolidated V1 **revenue** line `Revenue!D6:M6` is `=Backlog!D89:M89` (opening backlog × 0.5 delivery rate), NOT this sheet. Editing units/ASP here changes only the COGS ratio, never the reported top line. **4. Structural Detail & Key Formulas:**

- Structure: `B1` read-only banner; `B2` title (variant/domain/launch); `B3` description; header row 5 (`Line | Driver | Y1…Y10` = cols D–M). Three variant blocks (rows 6–12, 14–20, 22–28), each a 5-row pattern: ASP / BoM / Units / Revenue / Contribution margin. Totals block rows 30–36.

- Per-variant input baselines (Y1, col D): Variant A ASP 26 / BoM 11; Variant B ASP 45 / BoM 17.765; Variant C ASP 36 / BoM 14.6775. Units D9:M9 (A) = 2,8,10,20,50,50,60,60,80,80; B = 0,1,2,3,4,5,6,7,8,8; C = 0,1,1,2,3,4,5,6,6,7.

- Key formulas (verbatim, Variant A; all variants identical pattern):

  - ASP erosion: `E7` `=IFERROR($D$7\\\*(E8/$D$8)^Assumptions!$C$39,0)` — ASP scales off Y1 ASP by (current BoM ÷ Y1 BoM) raised to the 0.5 elasticity exponent. ASP falls only as BoM falls.

  - BoM learning curve: `E8` `=MAX($D$8\\\*Assumptions!$C$40,$D$8\\\*Assumptions!$C$10^LOG(MAX(1,SUM($D9:E9)),Assumptions!$C$41))` — Wright's Law: Y1 BoM × 0.92^(log₂ cumulative units), floored at 70% of Y1 BoM.

  - Revenue: `D10` `=D7\\\*D9` (ASP × units). COGS: `D11` `=D8\\\*D9` (BoM × units).

  - Contribution margin: `D12` `=IF(D7=0,0,1-D8/D7)`.

  - Totals: `D31` `=D10+D18+D26` (revenue), `D32` `=D11+D19+D27` (COGS), `D34` `=D31-D32` (gross profit), `D35` `=IFERROR((D31-D32)/D31,0)` (gross margin %), `D36` `=D31` then `E36` `=D36+E31` (cumulative).

- Computed totals: V1 revenue Y1–Y10 = 52, 262, 336, 623, 1340, 1403, 1683, 1749, 2222, 2252; gross margin climbs 57.7% → 65.0%. (These are the *V-sheet* memo figures; the consolidated V1 top line via Backlog is far lower — Y2 ₹50 Cr, Y10 ₹865 Cr.) **5. Glossary of Terms:** **AESA** Active Electronically Scanned Array (electronic-beam-steered radar); **X-band / S-band** radar frequency bands; **ASP** average selling price per unit; **COGS** cost of goods sold (= BoM here); **contribution margin** 1 − BoM/ASP; **units shipped** annual deliveries (\#); **ESM** electronic support measures (the V2 line whose RF/DSP front-end V1 reuses).

### 3.3 V2\_EW\_SIGINT — Electronic Warfare & SIGINT (full, incl. the iDEX MoQ bridge)

**Type:** Calculation Engine (read-only supporting detail) + traceability bridge **1. Functional Overview:** Unit-economics model for the EW/SIGINT line — the Day-1 cash engine — across **four** variants (EW-A Naval ESM/ELINT, EW-B Aerial ESM Pod, EW-C Anti-Drone Jammer, EW-D Ground SIGINT Station), plus a dedicated **iDEX ESM MoQ traceability bridge** (`B47:D55`). Dimensions 55×14, 258 formulas — larger than the other V-sheets because of the fourth variant and the MoQ block. **Launch Y1.** **2. Strategic Significance:** EW/SIGINT is the only line shipping in Year 1; it is part-developed and contracted at plan start, turning Y1 from a pure burn year into a revenue-and-gross-profit year and funding the other five lines concurrently (no per-product re-equitisation — the structural reason equity rounds step *down* Seed 450 → A 400 → B 250). Global EW market USD 22–25 bn/yr (6–8% CAGR); NDAD targets sub-1% globally with Indian mid-tier leadership. The MoQ bridge documents the firm iDEX ESM anchor contract: ₹210 Cr (10 systems × ₹21 Cr concessional) delivered in two ₹105 Cr phases — Phase 1 is the headline opening order book. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: Same `Assumptions` references as V1 (`$C$39`, `$C$40`, `$C$10`, `$C$41`). Yellow Y1 inputs per variant. The MoQ bridge links the catalogue ASP `=D7` and cross-checks `Backlog!D76`.

- Downstream outputs (**read-only**): V2 totals `D39:M39` (revenue) / `D40:M40` (COGS) feed only `Revenue!D24:M24` COGS rescale: `=IFERROR(V2\\\_EW\\\_SIGINT!D40\\\*(D7/V2\\\_EW\\\_SIGINT!D39),0)`. Consolidated V2 **revenue** `Revenue!D7:M7` = `=Backlog!D90:M90` (V2 opening backlog × 0.5). **The MoQ block drives nothing** — it is documentation/traceability only; it does not create a separate revenue line. The ₹105 Cr Phase 1 enters the model solely as the hand-keyed V2 Y1 opening backlog `Backlog!D76 = 105`, which the bridge then reconciles to. **4. Structural Detail & Key Formulas:**

- Structure: identical 5-row variant pattern as V1, but **four** blocks (rows 6–12, 14–20, 22–28, 30–36) and totals at rows 38–44 (note offset vs V1's 30–36). Then the MoQ bridge `B47:D55`.

- Per-variant Y1 inputs (col D): EW-A ASP 30 / BoM 14; EW-B ASP 35 / BoM 13.775; EW-C ASP 2 / BoM 0.8075; EW-D ASP 114 / BoM 60. (Catalogue ASPs ₹30/₹35 vs the ₹21 Cr iDEX concession ≈ 30% discount.)

- Core formulas (same engine as V1): ASP `E7 =IFERROR($D$7\\\*(E8/$D$8)^Assumptions!$C$39,0)`; BoM `E8 =MAX($D$8\\\*Assumptions!$C$40,$D$8\\\*Assumptions!$C$10^LOG(MAX(1,SUM($D9:E9)),Assumptions!$C$41))`; Revenue `D10 =D7\\\*D9`; COGS `D11 =D8\\\*D9`; totals `D39 =D10+D18+D26+D34` (four variants), `D40 =D11+D19+D27+D35`, gross margin `D43 =IFERROR((D39-D40)/D39,0)`.

- **iDEX ESM MoQ traceability bridge — `B47:D55` cell-by-cell (extracted verbatim):** | Cell | Label (col B) | Value (col C) | Note (col D) | |---|---|---|---| | R47 | iDEX ESM MoQ - traceability bridge (anchor contract within V2) | — | — | | R48 | MoQ systems (\#) | `C48 = 10` | 10-system iDEX first-article order | | R49 | Concessional price / system (₹ Cr) | `C49 = 21` | iDEX concessional rate per system | | R50 | MoQ total (₹ Cr) | `C50 =C48\\\*C49` → **210** | 10 × ₹21 Cr = ₹210 Cr | | R51 | Phase 1 (Y1, 5 systems) (₹ Cr) | `C51 =C49\\\*5` → **105** | Two-phase delivery: 5 + 5 systems | | R52 | Phase 2 (Y2, 5 systems) (₹ Cr) | `C52 =C50-C51` → **105** | Balance of MoQ | | R53 | Catalogue ASP - Naval ESM suite (₹ Cr) | `C53 =D7` → **30** | Link to EW-A catalogue ASP (D7); pod ASP (D15)=35 | | R54 | Concession vs catalogue (%) | `C54 =IFERROR(1-C49/C53,0)` → **0.30** | iDEX discount of concessional rate vs catalogue | | R55 | Check: Phase 1 ties to V2 Y1 opening backlog | `C55 =IF(ROUND(C51-Backlog!D76,2)=0,"OK - ties to Backlog!D76 (105)","CHECK")` → **"OK - ties to Backlog!D76 (105)"** | Backlog!D76 = V2 Y1 opening backlog (₹105 Cr) |

- Computed V2 totals (memo): revenue Y1–Y10 = 167, 367, 640, 958, 1014, 1074, 1223, 1621, 1775, 1859; gross margin 55.3% → 61.2%. (Consolidated V2 via Backlog is lower: Y1 ₹52.5 Cr → Y10 ₹760 Cr.) **5. Glossary of Terms:** **EW** electronic warfare; **SIGINT** signals intelligence; **ESM** electronic support measures; **ELINT** electronic intelligence; **iDEX** Innovations for Defence Excellence (Indian MoD innovation/procurement programme); **MoQ** Minimum order Quantity (the firm anchor-contract floor, here 10 systems / ₹210 Cr); **anchor contract** the first committed production order that de-risks the line; **concessional price** the discounted launch/volume contract price (₹21 Cr) below catalogue (₹30/₹35 Cr); **Phase 1/2** the two 5-system delivery tranches of ₹105 Cr each.

### 3.4 V3\_CUAS — Counter-UAS (Anti-Drone)

**Type:** Calculation Engine (read-only supporting detail) — mirrors the V1 archetype (36×14, 204 formulas). **1. Functional Overview:** Three-variant unit-economics model for multi-layered counter-drone systems (radar + RF + EO/IR + AI fusion + soft/hard-kill effectors). MVP fielded Y2 on the shared RF/DSP/AI stack, scaled Y3+. **Differs from V1 archetype:**

- Product/title: "V3 - Counter-UAS (Anti-Drone) | Domain: Land/Air (RF + AI fusion) | **Launch Y2**."

- Variants & Y1 inputs (ASP / BoM): CUAS-A Dismounted Soldier Kit (1.5 / 0.9); CUAS-B Vehicle-Mounted (14.25 / 8); CUAS-C Fixed Site Integrated (65 / 27.075).

- Units (highest unit volumes in the portfolio): CUAS-A ramps 0→320/yr; total units 0,13,48,96,155,214,263,312,348,383.

- Timing/ramp: zero in Y1; V-sheet revenue 0, 53, 202, 389, 600, 810, 1005, 1201, 1310, 1450; gross margin 47.5%→55.3%.

- Highest unit volumes; positioned as the AI-fusion showcase; global C-UAS market USD 2–3 bn rising to 6–7 bn by 2030 at 25–30% CAGR. **Read-only data-flow note:** V3 feeds ONLY `Revenue!D25:M25` COGS rescale `=IFERROR(V3\\\_CUAS!D32\\\*(D8/V3\\\_CUAS!D31),0)`. Consolidated V3 revenue `Revenue!D8:M8` = `=Backlog!D91:M91` (V3 opening backlog × **0.33** delivery rate). Editing units/ASP here does not change the top line.

### 3.5 V4\_UAS\_MALE — MALE-class ISR UAS

**Type:** Calculation Engine (read-only supporting detail) — mirrors the V1 archetype (36×14, 204 formulas). **1. Functional Overview:** Three-variant model for MALE-class unmanned aircraft (ISR baseline + strike-capable + SIGINT/EW mission variant). Longest development cycle (airframe + airworthiness), compressed via MOSA reuse of the mission-computer/AI stack. **Differs from V1 archetype:**

- Product/title: "V4 - MALE-class ISR UAS | Domain: Air (SysEng + SW + AI) | **Launch Y4**" (latest first-ship in the portfolio).

- Variants & Y1 inputs (ASP / BoM): UAS-A MALE ISR baseline (150 / 51.3); UAS-B MALE strike-capable (210 / 75.05); UAS-C MALE SIGINT/EW variant (200 / 64.6) — highest ASPs in the workbook.

- Units low/late: total 0,0,0,2,4,6,8,10,12,14 (nothing ships Y1–Y3).

- Timing/ramp: V-sheet revenue 0,0,0,350,683,974,1268,1540,1822,2098; gross margin 66.9%→71.2% (highest hardware margins).

- India needs ~70–100 MALE airframes over the decade; sub-1% global share but materially higher in India; clears DO-178C/254 + type certification before Y4 production. **Read-only data-flow note:** V4 feeds ONLY `Revenue!D26:M26` COGS rescale `=IFERROR(V4\\\_UAS\\\_MALE!D32\\\*(D9/V4\\\_UAS\\\_MALE!D31),0)`. Consolidated V4 revenue `Revenue!D9:M9` = `=Backlog!D92:M92` (V4 opening backlog × **0.33** delivery rate).

### 3.6 V5\_Autonomous — Autonomous Systems (AUV/USV)

**Type:** Calculation Engine (read-only supporting detail) — mirrors the V1 archetype (36×14, 204 formulas). **1. Functional Overview:** Three-variant model for unmanned maritime systems (small mine-hunting AUV, large ASW AUV, mid-size USV). Rapid hull iteration; autonomy stack reused from V6. **Differs from V1 archetype:**

- Product/title: "V5 - Autonomous Systems (AUV/USV) | Domain: Sea (SysEng + SW + AI) | **Launch Y3**."

- Variants & Y1 inputs (ASP / BoM): AUV-A Small AUV mine-hunting/survey (15 / 4.085); AUV-B Large ASW AUV (60 / 20.425); USV-A Mid-size USV ISR/C-UAS host (45 / 15.39).

- Units: total 0,0,2,5,12,19,29,38,44,51 (first ship Y3).

- Timing/ramp: V-sheet revenue 0,0,60,126,311,440,675,876,998,1171; gross margin 67.5%→73.3% (highest in portfolio).

- Unmanned-maritime market USD 2.5–3.5 bn/yr at 12–15% CAGR; reuses the V6 autonomy/AI stack. **Read-only data-flow note:** V5 feeds ONLY `Revenue!D27:M27` COGS rescale `=IFERROR(V5\\\_Autonomous!D32\\\*(D10/V5\\\_Autonomous!D31),0)`. Consolidated V5 revenue `Revenue!D10:M10` = `=Backlog!D93:M93` (V5 opening backlog × **0.25** delivery rate).

### 3.7 V6\_MilAI — Military AI Systems

**Type:** Calculation Engine (read-only supporting detail) — mirrors the V1 archetype (36×14, 204 formulas). **1. Functional Overview:** Three-variant **software-led** model (Edge AI box + cloud SaaS analytics + sensor-fusion middleware) on a software-defined quarterly release cadence. Ships from Y1 alongside V2. **Differs from V1 archetype:**

- Product/title: "V6 - Military AI Systems | Domain: Cross-domain (AI/SW) | **Launch Y1**."

- Variants & Y1 inputs (ASP / BoM): AI-A Edge AI mission box per-platform (3.8 / 0.6175); AI-B OIDSS per-yr license (11.4 / 0.475); AI-C Sensor-fusion middleware license (5.7 / 0.19).

- **Software economics:** tiny BoM ratios → gross margin ~93.1%→94.4% (far above the ~55–73% hardware lines). Same Wright/elasticity formulas apply but the BoM floor barely matters because BoM is already minimal.

- Units: total 5,11,22,41,59,80,102,115,130,142; ships in Y1 (with V2).

- Timing/ramp: V-sheet revenue 30.4,58.7,111.5,206,299,417,537,610,693,757.

- Attaches to every hardware line (so its effective software-economics share of the P&L exceeds the ~10% headline); anchor share in Indian platforms; reference points Palantir/Anduril. **Read-only data-flow note:** V6 feeds ONLY `Revenue!D28:M28` COGS rescale `=IFERROR(V6\\\_MilAI!D32\\\*(D11/V6\\\_MilAI!D31),0)`. Consolidated V6 revenue `Revenue!D11:M11` = `=Backlog!D94:M94` (V6 opening backlog × **0.25** delivery rate).

### 3.8 Verification Notes & Anomalies

- **Backlog-driven top line confirmed by reading the cells:** `Revenue!D6 =Backlog!D89`; `Backlog!D89 =D75\\\*D82` (opening backlog × delivery rate). The "Original V-sheet revenue (memo)" column N on Revenue explicitly labels the V-sheet figures as a memo. `Revenue!B1` banner: *"V1-V6 sheets retained as unit/ASP analytics only; their edits do not flow into consolidated revenue."*

- **COGS rescale confirmed:** `Revenue!D23:M28` each = V-sheet total COGS × (Backlog revenue ÷ V-sheet revenue), preserving the V-sheet gross-margin % onto the Backlog-recognized revenue.

- **MoQ self-check passes:** `V2!C55` evaluates to "OK - ties to Backlog!D76 (105)". Concession `C54` = exactly 30%.

- **Delivery-rate convention:** RF/hardware lines V1/V2 recognize 50%/yr of opening backlog; V3/V4 33%; V5/V6 25% (`Backlog!D82:M87`).

- **Anomalies:** (1) Narrative/label rounding — the deck's `Cover!C7`/`Strategy!C10` label the MoQ "₹200 Cr" whereas the workbook math is ₹210 Cr (flagged for correction; label only, revenue unaffected since it is Backlog-derived). (2) The `Assumptions` sheet duplicates several constants under two cell addresses (ASP elasticity at `C39`=0.5 and `C51`=0.5; BoM floor at `C40`=0.7 but `C52`=0.5; doubling base at `C41`/`C46`/`C54`) — the **active** V-sheet references are `C39`, `C40`, `C41`; the lower block (`C51:C54`) appears to be a partly-redundant later register and its `C52`=0.5 floor is NOT the one the V-sheets use. (3) V2 totals block is at rows 38–44, offset from the V1/V3–V6 totals at rows 30–36, because of V2's fourth variant — anyone diffing the sheets by absolute row will mismatch.

## 4. Revenue Recognition & Backlog Engine

This section documents the CORE revenue engine of the NDAD V2 workbook: the `Backlog` → `Revenue` → `P&L` recognition chain. The central architectural claim — **consolidated revenue is Backlog-driven, not V-sheet-driven** — was verified cell-by-cell and **holds true**: every consolidated revenue cell `Revenue!D6:M11` is a direct link to the per-vertical recognized-delivery rows `Backlog!D89:M94`. The V1–V6 product sheets are read-only supporting detail and feed only the COGS-ratio rescale in `Revenue` rows 23–28. All figures are in ₹ Crore (₹ Cr) over a Y1–Y10 horizon. Funding/Backlog use columns D:M = Y1:Y10; Revenue/P&L share the same Y1:Y10 grid but P&L reads them into its own C:L offset.

### Sheet: Revenue (35×14, 220 formulas)

The sheet header (`Revenue!B1`) self-declares the architecture verbatim: *"READ ONLY SUPPORTING DETAIL upstream - Revenue (rows 6-12) is sourced from Backlog!D89:M95 (Section L deliveries). V1-V6 sheets retained as unit/ASP analytics only; their edits do not flow into consolidated revenue."* `Revenue!B34`: *"Note: Revenue = Backlog!Deliveries (rows 89-94). Edit per-vertical delivery rates in Backlog!D82:M87."*

Layout: column B = row labels, column C = stream tag, columns D:M = Y1:Y10, column N = memo ("Original V-sheet revenue (memo)"). Logical blocks: **A. Revenue by vertical** (rows 6–12), **B. Revenue mix %** (rows 15–20), **C. COGS – BoM by vertical** (rows 23–29), **D. Gross profit / margin** (rows 32–33).

#### Table A — Revenue by vertical (rows 6–12)

**Type:** Output/Reporting (mechanically a pass-through of the Backlog engine) **1. Functional Overview:** Six per-vertical recognized-revenue rows (V1 AESA row 6 … V6 Military AI row 11) plus `TOTAL REVENUE` row 12. Each cell is a pure link to the corresponding Backlog recognized-delivery cell — this row block is where backlog becomes revenue. **2. Strategic Significance:** This is the model's claim to **backlog-backed revenue visibility**. Revenue is not a top-down market-share guess; per `investor\\\_plan/04\\\_financial\\\_model.md` ("A. Revenue Architecture") it is "built up from booked orders … then released into revenue under a recognition-lag schedule that matches how the Indian MoD and allied customers actually pay against milestones." Y1 revenue (₹52.5 Cr, V2 only) is the **iDEX ESM cash engine** — production-order revenue, not a grant — making Y1 a revenue-and-gross-profit year rather than pure burn. Order-book quality is high: this is post-qualification iDEX MoQ production-order backlog (4/4 dev milestones cleared), one rung below a multi-year series contract on the commitment ladder. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: `Backlog!D89:M94` (Section L recognized deliveries = opening backlog × delivery rate). Nothing from the V-sheets touches these revenue rows.

- Downstream outputs: `Revenue!D12:M12` (total revenue) → `P&L!C5` (`=Revenue!D12`, total revenue, year-shifted into P&L's C:L grid); also consumed back inside Backlog at `Backlog!D53:M53` (`=Revenue!D12`, memo recognized revenue), `Backlog!38/39/49` (book-to-bill & coverage KPIs use `Revenue!D12` / `Revenue!D6:D11`), and `Backlog!43:48` derived B:B (`Revenue!D6`…`Revenue!D11`). Per-vertical revenue rows 6–11 also feed the COGS rescale in rows 23–28 (numerator of the delivered/V-sheet ratio). **4. Structural Detail & Key Formulas:**

- Structure: headers row 4 (Vertical | Stream | Y1…Y10 | memo); 6 vertical rows + 1 total; data type = links / SUM; values in ₹ Cr.

- Key formulas (verbatim):

  - `Revenue!D6` `=Backlog!D89` → explains the central claim: V1 Y1 recognized revenue = V1 Y1 deliveries. Row mapping is 1:1 and contiguous: `D7=Backlog!D90`, `D8=Backlog!D91`, `D9=Backlog!D92`, `D10=Backlog!D93`, `D11=Backlog!D94`; and across years e.g. `M6=Backlog!M89`, `M11=Backlog!M94`. So the whole block `Revenue!D6:M11 ← Backlog!D89:M94` is a verbatim cell-for-cell mirror.

  - `Revenue!D7` `=Backlog!D90` → V2 ESM Y1 = ₹52.5 Cr, the Day-1 cash engine (105 opening × 0.5 delivery rate).

  - `Revenue!D12` `=SUM(D6:D11)` → TOTAL REVENUE Y1 = ₹52.5 Cr; `Revenue!M12 =SUM(M6:M11)` = ₹5,055.3 Cr Y10. **This is the row P&L consumes.**

#### Table B — Revenue mix % (rows 15–20)

**Type:** Output/Reporting **1. Functional Overview:** Each vertical's revenue as a share of total, for portfolio-mix reporting (V1 mix … V6 mix). **2. Strategic Significance:** Shows the portfolio rotating away from single-line dependence — V2 ESM is 100% of Y1 revenue but only ~15% by Y10 as AESA, C-UAS and MALE UAS scale; evidence of diversification of the order book away from a single program. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: `Revenue!D6:M11` and `Revenue!D12:M12`.

- Downstream outputs: presentation only (mix table / charts); not consumed by P&L. **4. Structural Detail & Key Formulas:**

- Key formula: `Revenue!D15` `=IFERROR(D6/D12,0)` → V1 mix = V1 revenue / total revenue, IFERROR guards the Y1 zero-revenue verticals.

#### Table C — COGS, BoM by vertical (rows 23–29) — the V-sheet rescale

**Type:** Calculation Engine **1. Functional Overview:** Cost of goods sold (Bill-of-Materials only, pre-personnel) per vertical, rows 23–28, plus `TOTAL COGS - BoM` row 29. This is the **only** place the V1–V6 product sheets enter consolidated numbers. COGS is rescaled so gross-margin % follows the underlying unit economics of each V-sheet. `Revenue!B35`: *"COGS scaled: V-sheet BoM × (delivered revenue / V-sheet revenue) so gross margin % follows the underlying unit economics."* **2. Strategic Significance:** Decouples cost from the backlog-driven revenue while **preserving each vertical's gross-margin signature** (e.g. the ~93–94% margin software line V6). Lets the model honor defense-prime unit economics (Wright's-Law BoM learning curve, platform-reuse leverage) from the V-sheets without letting V-sheet revenue override the contracted backlog. Anchors gross profit → P&L → cash generation. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: per-vertical V-sheet **revenue** and **COGS totals** — V1 `V1\\\_AESA!D31` (Total revenue) and `V1\\\_AESA!D32` (Total COGS BoM); V2 `V2\\\_EW\\\_SIGINT!D39`/`!D40`; V3 `V3\\\_CUAS!D31`/`!D32`; V4 `V4\\\_UAS\\\_MALE!D31`/`!D32`; V5 `V5\\\_Autonomous!D31`/`!D32`; V6 `V6\\\_MilAI!D31`/`!D32`. Plus the delivered revenue numerator from `Revenue!D6:M11`.

- Downstream outputs: `Revenue!D29:M29` (total COGS) → `P&L!C6` (`=Revenue!D29`, "COGS – BoM"). Also feeds gross profit rows 32–33. **4. Structural Detail & Key Formulas:**

- Structure: 6 vertical COGS rows + 1 total; data type = IFERROR ratio products.

- Key formulas (verbatim):

  - `Revenue!D23` `=IFERROR(V1\\\_AESA!D32\\\*(D6/V1\\\_AESA!D31),0)` → V1 BoM COGS = V-sheet BoM COGS × (delivered revenue ÷ V-sheet revenue). The ratio `D6/V1\\\_AESA!D31` is the share of the V-sheet's modeled revenue that the backlog actually delivers; multiplying the V-sheet COGS by it holds the V-sheet's COGS/revenue (hence gross-margin) ratio constant. This is the COGS-rescale formula.

  - `Revenue!D24` `=IFERROR(V2\\\_EW\\\_SIGINT!D40\\\*(D7/V2\\\_EW\\\_SIGINT!D39),0)` → same pattern for V2 (note V-sheet rows differ per sheet: V2 uses 39/40, V1/V3/V4/V5/V6 use 31/32).

  - `Revenue!D29` `=SUM(D23:D28)` → TOTAL COGS – BoM. **This is the COGS row P&L consumes.**

#### Table D — Gross profit / margin (rows 32–33)

**Type:** Output/Reporting **1. Functional Overview:** Gross profit (BoM only, before COGS personnel) and gross-margin %. **2. Strategic Significance:** The headline profitability of the contracted order book; gross margin rises from ~55% (Y1) to ~68% (Y10) as the mix shifts to high-margin software and reuse matures — the structural margin story underpinning the equity case. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: `Revenue!D12` (revenue), `Revenue!D29` (COGS).

- Downstream outputs: reporting / margin trend; the inputs (12, 29) flow independently to P&L which recomputes gross profit downstream into CashFlow/BalanceSheet. **4. Structural Detail & Key Formulas:**

- `Revenue!D32` `=D12-D29` → gross profit (BoM) = revenue − COGS.

- `Revenue!D33` `=IFERROR((D12-D29)/D12,0)` → gross margin %.

**5. Glossary of Terms (Revenue sheet):**

- **Recognized revenue / recognized deliveries:** the portion of opening backlog actually delivered and booked as revenue in the year (`Revenue` rows 6–11 ≡ `Backlog` rows 89–94).

- **COGS (BoM):** cost of goods sold, bill-of-materials only, excluding COGS personnel.

- **Gross profit / gross margin:** revenue − COGS, and that as a % of revenue.

- **ASP:** average selling price per system (the V-sheets carry unit/ASP analytics; e.g. iDEX ESM contracted at ₹21 Cr/system).

- **Revenue mix:** each vertical's share of total revenue.

- **V-sheet:** a per-product detail sheet (V1\_AESA … V6\_MilAI); here read-only, supplying only COGS/revenue ratios.

### Sheet: Backlog (102×13, 426 formulas)

`Backlog!B2`: *"Backlog, Pipeline & Book-to-Bill - Defense Contract Mechanics."* `Backlog!B3`: *"Bookings = … contract awards. Backlog rolls forward (prior + bookings − recognized). Pipeline = Bookings / Pwin. Defense bookings typically lead revenue by 12–18 months for HW, 6–12 months for SW."* `Backlog!B101`: *"Revenue is now FULLY DERIVED from Backlog deliveries (Section L drives Revenue sheet)."*

Layout: B = labels, C = "Default" (row averages), D:M = Y1:Y10. Lettered sections: **A** target book-to-bill (6–11), **B** Pwin (13–18), **C** Bookings input driver (19–26), **D** Backlog roll-forward / closing (28–35), **E** Consolidated KPIs (37–40), **F** Derived book-to-bill check (42–49), **G** Pipeline / contract-liability / advance (51–57), **I** Bank guarantees PBG+ABG (59–64), **K** Opening backlog (74–80), **L** Delivery schedule – rates (81–87), then Deliveries (89–95), **N** notes (97–102).

#### Table C — Bookings (new contract awards) — input driver (rows 19–26)

**Type:** Input/Assumption **1. Functional Overview:** Six per-vertical bookings rows (V1 row 20 … V6 row 25) as independent static inputs, plus `Σ Bookings` row 26. `Backlog!B98`: *"Bookings are now INDEPENDENT static inputs (not derived from revenue)."* **2. Strategic Significance:** Bookings are firm/forecast contract awards — the leading indicator of the order book. Defense bookings lead revenue by 12–18 months (HW) / 3–12 months (SW), so this is what builds the ₹16,680 Cr Y10 closing backlog (3.3× Y10 revenue), the model's revenue-visibility moat. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: none (hard-keyed yellow inputs, e.g. V1 Y1 `D20=100`, V2 Y1 `D21=341.075`).

- Downstream outputs: roll-forward additions (rows 29–34 add `+D20`…`+D25`), `Σ Bookings` row 26 → advance inflow `Backlog!52` and KPI/book-to-bill rows 38/49. **4. Structural Detail & Key Formulas:**

- `Backlog!D26` `=SUM(D20:D25)` → consolidated bookings; Y1 = ₹477.555 Cr.

#### Table D — Backlog roll-forward (closing) (rows 28–35)

**Type:** Calculation Engine **1. Functional Overview:** The order-book roll-forward per vertical (V1 closing row 29 … V6 closing row 34) plus `Σ Closing backlog` row 35. `Backlog!B28`: *"D. Backlog roll-forward = prior + bookings − recognized revenue."* **2. Strategic Significance:** This is the **order-book accounting** that produces revenue visibility: closing backlog = opening + bookings − recognized deliveries. Backlog coverage (`Σ closing` ÷ revenue) and book-to-bill (\>1 = backlog growing) come straight from here; closing backlog of ₹16,680 Cr at Y10 (\>3.3× revenue) is the headline visibility metric. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: prior-year closing (rows 29–34 themselves, recursive), bookings (rows 20–25), deliveries (rows 89–94).

- Downstream outputs: closing rows 29–34 → opening-backlog rows 75–80 next year (e.g. `E75=D29`), making the loop closed; `Σ Closing` row 35 → backlog-coverage KPI `Backlog!39`, growth `Backlog!40`, and PBG guarantees `Backlog!61`. **4. Structural Detail & Key Formulas:**

- Key formulas (verbatim — the roll-forward, closing = opening + additions − recognized):

  - `Backlog!D29` `=(D20-D89)` → V1 Y1 closing = Y1 bookings − Y1 deliveries (no prior backlog in Y1).

  - `Backlog!E29` `=(D29+E20-E89)` → V1 Y2 closing = prior closing (D29) + Y2 bookings (E20) − Y2 recognized deliveries (E89). This is the canonical **closing = opening + additions − recognized** form.

  - `Backlog!D35` `=SUM(D29:D34)` → consolidated closing backlog; Y10 `M35` ≈ ₹16,680 Cr.

#### Table K — Opening backlog (rows 74–80) — carry-forward + iDEX ESM anchor

**Type:** Calculation Engine (with two hard-keyed Y1 seeds) **1. Functional Overview:** Opening backlog carried forward from prior-year closing, per vertical (V1 row 75 … V6 row 80). `Backlog!B74`: *"K. Opening backlog (carried forward from prior-year closing)."* **2. Strategic Significance:** Holds the **iDEX ESM anchor**: `Backlog!D76 = 105` is V2's Y1 opening backlog — Phase 1 of the firm ₹210 Cr iDEX ESM MoQ (10 systems × ₹21 Cr; Phase 1 = ₹105 Cr). Production-order backlog, post-qualification (4/4 dev milestones cleared), distinct from grants. (Note: the narrative `Cover!C7`/`Strategy!C10` label this "₹200 Cr" — per `investor\\\_plan/slide\\\_day1\\\_traction.md` that is a narrative-only rounding to be corrected to ₹210 Cr; the model is Backlog-derived, so revenue is unaffected. The cell value 105 = half of ₹210 Cr, confirming the ₹210 Cr / 10×₹21 Cr anchor.) **3. Modeling Impact & Data Flow:**

- Upstream dependencies: prior-year closing backlog (rows 29–34); Y1 cells are hard inputs (`D75=0`, `D76=105`, `D77:D80=0`).

- Downstream outputs: deliveries (rows 89–94 multiply opening × delivery rate); roll-forward implicitly via the closing rows. **4. Structural Detail & Key Formulas:**

- `Backlog!D76` `=105` (input) → V2 Y1 opening backlog = iDEX ESM Phase-1 anchor.

- `Backlog!E76` `=D30` → V2 Y2 opening = V2 Y1 closing (carry-forward); `E75=D29` for V1, etc.

#### Table L — Delivery schedule, per-vertical recognition rates (rows 81–87)

**Type:** Input/Assumption (the recognition-rate driver) **1. Functional Overview:** Per-vertical % of opening backlog recognized as revenue each year (V1 rate row 82 … V6 rate row 87). `Backlog!B81`: *"L. Delivery schedule - per-vertical % of opening backlog recognized as revenue."* `Backlog!B102`: *"Edit yellow cells in Section L (D82:M87) to tune per-vertical recognition rates."* **2. Strategic Significance:** Encodes the **defense recognition lag** as a fraction released per year (HW slower, SW faster): V1/V2 = 0.50, V3/V4 = 0.33, V5/V6 = 0.25 across all years. This is the single lever that bridges opening backlog → recognized revenue, i.e. it sets how fast the order book converts to revenue. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: none (flat assumptions).

- Downstream outputs: deliveries rows 89–94. **4. Structural Detail & Key Formulas:**

- `Backlog!D82` `=0.5` (input) → V1 delivery rate (50% of opening backlog recognized per year).

#### Deliveries — revenue recognized (rows 89–95) — the link target

**Type:** Calculation Engine (and the exact cells `Revenue` mirrors) **1. Functional Overview:** Recognized deliveries per vertical = opening backlog × delivery rate (V1 row 89 … V6 row 94), plus `Σ Deliveries (revenue recognized)` row 95. These rows ARE the consolidated revenue. **2. Strategic Significance:** The literal point of **revenue recognition** — where contracted, post-qualification defense backlog becomes booked revenue. `Backlog!B95` labels row 95 "Σ Deliveries (revenue recognized)"; `Σ` row 95 equals `Revenue!12` to the rupee. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: opening backlog (rows 75–80) × delivery rates (rows 82–87).

- Downstream outputs: **`Backlog!D89:M94` → `Revenue!D6:M11`** (1:1, the central link); deliveries also subtract in the roll-forward closing rows 29–34 (`-D89` … `-D94`). **4. Structural Detail & Key Formulas:**

- `Backlog!D89` `=D75\\\*D82` → V1 deliveries = opening backlog × delivery rate; **this is the cell `Revenue!D6` points at.**

- `Backlog!D90` `=D76\\\*D83` → V2 Y1 deliveries = 105 × 0.5 = ₹52.5 Cr (the Day-1 ESM revenue).

- `Backlog!D95` `=SUM(D89:D94)` → Σ deliveries = ₹52.5 Cr Y1, matching `Revenue!D12`.

#### Tables E / F / G / I — KPIs, derived book-to-bill, contract liability, guarantees (rows 37–64)

**Type:** Output/Reporting (E, F) + Calculation Engine (G, I) **1. Functional Overview:** E Consolidated KPIs (book-to-bill 38, coverage-months 39, growth 40); F derived B:B per vertical (43–49) as a check; G advance/contract-liability schedule (52–57); I bank guarantees PBG+ABG and restricted cash (60–64). **2. Strategic Significance:** Translates the order book into the metrics investors test: **book-to-bill** (\>1 = backlog growing, tapering 1.5×→1.0× across the plan), **backlog coverage in months of revenue** (~97 mo Y1 → ~40 mo Y10), and the working-capital mechanics of defense contracts — 15% advance payments create a **contract liability** that amortizes into revenue, and PBG/ABG guarantees require restricted cash collateral. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: `Σ Bookings` (26), `Σ Closing backlog` (35), `Revenue!D12` and `Revenue!D6:D11`, and `Assumptions` rates (advance `C22=0.15`, PBG `C21=0.03`, BG fee `C23=0.011`).

- Downstream outputs: contract-liability ending balance (56) and guarantees feed CashFlow/BalanceSheet (restricted cash, deferred revenue); KPIs are reporting. **4. Structural Detail & Key Formulas:**

- `Backlog!D38` `=IFERROR(D26/Revenue!D12,0)` → consolidated book-to-bill = bookings ÷ recognized revenue.

- `Backlog!D39` `=IFERROR(D35/Revenue!D12\\\*12,0)` → backlog coverage in months.

- `Backlog!D56` `=MAX(0,D54+D52-D55)` → contract liability ending balance = beginning + advance inflow − amortized; `D55 =MIN(D54+D52,D53\\\*Assumptions!$C$22)` amortizes advance into recognized revenue.

- `Backlog!D61` `=Assumptions!$C$21\\\*D35` → PBG outstanding = PBG rate × closing backlog.

**5. Glossary of Terms (Backlog sheet):**

- **Bookings:** new firm contract awards (independent inputs); the leading order-intake indicator.

- **Backlog (order book):** undelivered contracted value; **opening** = prior-year closing carried forward, **closing** = opening + bookings − recognized deliveries.

- **Recognized deliveries / revenue recognition:** opening backlog × delivery rate; the slice released to revenue (= `Revenue` rows 6–11).

- **Delivery / recognition rate:** % of opening backlog recognized per year (the defense recognition-lag lever).

- **Book-to-bill (B:B):** bookings ÷ recognized revenue; \>1 grows backlog, ~1 steady-state, \<1 shrinking.

- **Backlog coverage:** closing backlog expressed as months of revenue (revenue visibility).

- **Pwin:** probability of win on qualified pipeline (Pipeline = Bookings / Pwin).

- **Contract liability / advance payment:** 15% advance collected at award, amortized into revenue as delivered.

- **PBG / ABG:** Performance / Advance Bank Guarantee; backed by restricted-cash collateral.

- **MoQ:** Minimum Order Quantity (iDEX ESM = 10 systems × ₹21 Cr = ₹210 Cr; Phase 1 = ₹105 Cr = `Backlog!D76`).

## 5. Cost & Resource Build

This section documents the operating-cost engine of the NDAD financial model: the three sheets that convert the staffing plan and asset base into the cost lines consumed by the P&L, Balance Sheet, and Cash Flow. All currency is in ₹ Crore (₹ Cr) unless a row is explicitly labelled "₹ L" (lakhs); the per-item input rows are entered in ₹ Lakhs and divided by 100 to roll up into ₹ Cr. Horizon is Y1–Y10 (columns D:M). Cost escalation is applied via a `(1+rate)^(year-index)` power term anchored at `^0` in Y1.

The three sheets sit between the revenue/backlog engine and the three financial statements:

- **Headcount** → personnel cost split four ways (R&D / COGS / S&M / G&A) → P&L rows 7, 13, 14 and `R&D\\\_NRE`; headcount KPI.

- **Capex** → straight-line depreciation → P&L D&A (row 19), Balance Sheet gross PP&E / accumulated depreciation (rows 12–13), Cash Flow investing (row 17).

- **Opex** → non-personnel operating expense → P&L "Other Opex" (row 15).

### Headcount

#### Table A — Headcount (\# people) by role \[rows 5–34\]

**Type:** Input/Assumption **1. Functional Overview:** The staffing plan. 28 role rows (R6:R33) grouped implicitly by function — RF/microwave, DSP/FPGA, antenna, embedded, systems, mechanical, aerospace, naval, autonomy, mission SW, cyber, AI/ML, MLOps, T&E, certification (the R&D/engineering block); manufacturing, technicians, supply chain, field service (the production/COGS block); BD/capture, solution architects, marketing (the S&M block); executive, finance, HR, legal, export-control, IT (the G&A block). Each role carries a "Cost band (₹ L/yr)" per-FTE fully-loaded salary in column C and a per-year FTE count across D:M. Row 34 totals EoY headcount. **2. Strategic Significance:** Encodes the operating-leverage thesis. Headcount scales 91 (Y1) → 543 (Y10) while revenue grows ~95×, so personnel cost falls steadily as a % of revenue. The mix deliberately shifts from R&D-heavy (~57% engineering in Y1) to production-heavy (~51% production/field in Y10), reflecting the move from platform build to multi-domain prime. The cross-domain engineering bench (RF, DSP, antenna, autonomy, AI/ML, naval, aerospace under one roof) is what makes the five reusable platform modules possible — talent breadth is the source of the reuse economics captured downstream in gross margin. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: `Assumptions!$C$8` (general cost escalation 4%) and `Assumptions!$C$9` (R&D salary escalation 4%); cost bands in column C; FTE counts are hard-coded inputs.

- Downstream outputs: feeds Table C (cost rollup) only within this sheet; row 34 → `KPIs!C28` "Total headcount (EoY)". **4. Structural Detail & Key Formulas:**

- Structure: 76×14. Header row 4 (`Role | Cost band (₹ L/yr) | Y1..Y10`). FTE counts are integers; cost band is ₹ L/FTE/yr.

- Key formulas:

  - `D34` `=SUM(D6:D33)` — total EoY headcount = 91 in Y1.

#### Table B — Personnel cost by role (escalated) \[rows 36–64\]

**Type:** Calculation Engine **1. Functional Overview:** Converts each role's FTE count × cost band into an escalated ₹ Cr cost, one cost row per headcount row, and tags each with a category code in column C: `R&D` (rows 37–51), `COGS` (52–55), `S&M` (56–58), `G&A` (59–64). **2. Strategic Significance:** The category tagging is the mechanism that routes labour into the correct P&L line (COGS labour vs. R&D vs. operating expense), so gross margin and EBITDA reflect where engineering effort actually lands. Escalation at 4%/yr keeps the salary build realistic rather than flat. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: own Table A FTE counts and cost bands; `Assumptions!$C$9` (R&D rows) and `Assumptions!$C$8` (all non-R&D rows).

- Downstream outputs: aggregated by Table C; not consumed directly off this block by other sheets. **4. Structural Detail & Key Formulas:**

- Structure: parallel to Table A; values in ₹ Cr (cost band ₹ L × FTE ÷ 100, escalated).

- Key formulas (the Headcount cost-build formula):

  - `D37` `=C6\\\*(1+Assumptions!$C$9)^0\\\*D6/100` — R&D role cost: cost band (₹ L) × R&D escalation^0 × FTE ÷ 100 = ₹ Cr. The exponent is the year index (`^0` Y1, `^1` Y2 …), e.g. `E37` `=C6\\\*(1+Assumptions!$C$9)^1\\\*E6/100`.

  - `D52` `=C21\\\*(1+Assumptions!$C$8)^0\\\*D21/100` — COGS role cost: identical form but uses the general escalation `$C$8`.

#### Table C — Personnel cost by category \[rows 66–72, note rows 71/72/76\]

**Type:** Output/Reporting (with one orphaned floor) **1. Functional Overview:** Sums Table B into the four category totals the rest of the model consumes: R&D personnel (R67), COGS personnel (R68), S&M personnel (R69), G&A personnel (R70), plus a grand total in R71. **2. Strategic Significance:** This is the hand-off surface to the three statements. It is also where the model's S&M/G&A driver logic is reconciled: rows 69–70 are the *bottom-up* personnel figure, while the P&L takes `MAX(bottom-up, %-of-revenue)`. Columns C of rows 69–70 carry live `IF(...)` audit strings that print "-\> % of revenue binds (row = memo only)" vs. "-\> headcount binds". **3. Modeling Impact & Data Flow:**

- Upstream dependencies: Table B rows 37–64.

- Downstream outputs:

  - `R67` → `R&D\\\_NRE!D7` "R&D personnel cost (from Headcount)".

  - `R68` → `P&L!C7` "COGS - personnel + service".

  - `R69` → `P&L!C13` (S&M) as the floor inside a `MAX`.

  - `R70` → `P&L!C14` (G&A) as the floor inside a `MAX`. **4. Structural Detail & Key Formulas:**

- Structure: category roll-up rows; explicit additive sums (not `SUM` ranges) to skip the category boundaries.

- Key formulas:

  - `D67` `=D37+D38+D39+D40+D41+D42+D43+D44+D45+D46+D47+D48+D49+D50+D51` — R&D personnel cost = ₹12.51 Cr Y1.

  - `D68` `=D52+D53+D54+D55` — COGS personnel cost.

  - `D69` `=D56+D57+D58` and `D70` `=D59+D60+D61+D62+D63+D64` — S&M / G&A personnel cost.

  - `C69` (audit) `=IF(ROUND('P&L'!C13,6)\\\>ROUND(Headcount!D69,6),"-\\\> % of revenue binds (row = memo only)","-\\\> headcount binds")`.

- **ORPHAN FLAG:** Per the workbook's own integrity note in `B76` (Integrity audit 2026-06-28): the %-of-revenue floor in P&L rows 13–14 (S&M 8%, G&A 7%) is binding in **all 10 years**, so Headcount rows 69–70 are a *non-binding* floor and **do not actually flow to the P&L**. They are computed but effectively orphaned (consumed only as the losing argument of `MAX`). Confirmed below in the Opex/P&L driver discussion.

**5. Glossary of Terms:**

- **FTE** — Full-Time Equivalent; one head-count unit of staff.

- **Cost band (₹ L/yr)** — fully-loaded annual cost of one FTE in that role, in ₹ Lakhs (includes salary + on-costs).

- **COGS labour** — production/field personnel charged to Cost of Goods Sold (rows 52–55), reducing gross margin.

- **R&D personnel** — engineering staff whose cost feeds the R&D line (via `R&D\\\_NRE`), partly capitalised under Ind AS 38.

- **S&M / G&A** — Sales & Marketing / General & Administrative; here the personnel component of those operating-expense lines.

- **Escalation** — annual % salary inflation (`Assumptions!C8`/`C9` = 4%), compounded by year index.

- **Fully-loaded** — cost including benefits, overhead allocation, and on-costs, not base salary alone.

### Capex

#### Table A — Capex per-item spend \[rows 5–21\]

**Type:** Input/Assumption **1. Functional Overview:** The capital-expenditure schedule. 14 asset rows (R6:R19, plus a blank R20) each with a useful "Life (yr)" in column C and per-year spend in ₹ L across D:M: test infrastructure (VNA suite, anechoic chamber, cleanroom, SMT line, HALT/HASS, EMI/EMC cell, RF/EW bench), compute (FPGA stations, GPU cluster), domain-specific (UAS flight-test hangar, maritime test tank), and office/IT/vehicles. Row 21 totals gross capex in ₹ Cr. **2. Strategic Significance:** Encodes the capital-efficiency thesis. The build is deliberately back-end-loaded to the inflection phase (Y3–Y5) so that early years stay asset-light on rented/partner facilities and owned infrastructure only replaces partner-lab dependence once volume justifies it (~₹600 Cr gross over 10 yrs). Long-life test assets (anechoic 15 yr, hangar/tank 20 yr) vs. short-life compute (GPU cluster 4 yr, FPGA/IT 5 yr) show the asset base is sized to revenue, not built ahead of it — capital efficiency on the heavy end, refresh discipline on the perishable end. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: none (hard-coded spend inputs + life assumptions). No escalation applied to capex spend.

- Downstream outputs:

  - `R21` → `BalanceSheet!C12` (gross PP&E, made cumulative on the BS), `CashFlow!C17` "− Capex (gross)" (sign-flipped), `KPIs!C30` "Capex (gross)", `KPIs!C42` `=SUM(Capex!D21:M21)` "Total Capex (10 yr)". **4. Structural Detail & Key Formulas:**

- Structure: 39×14. Header row 4 (`Item | Life (yr) | Y1..Y10`). Spend in ₹ L; row 21 converts to ₹ Cr.

- Key formulas:

  - `D21` `=SUM(D6:D20)/100` — gross capex Y1 = ₹35.45 Cr.

#### Table B — Depreciation (straight-line) per item \[rows 23–39\]

**Type:** Calculation Engine **1. Functional Overview:** A vintage-tracked straight-line depreciation schedule, one row per capex item. Each year's cell sums the annual depreciation charge of every prior-and-current capex vintage that is still within its useful life, producing that year's total depreciation expense (D&A) per item. Row 39 totals annual D&A. **2. Strategic Significance:** Converts the capital build into the periodic non-cash expense that hits EBIT and the balance sheet, and (combined with Ind AS 38 capitalised-R&D amortisation) shapes the EBITDA-vs-EBIT gap. Straight-line over realistic equipment lives keeps the depreciation profile defensible to investors. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: own Table A spend (D6:M19) and life (C6:C19).

- Downstream outputs:

  - `R39` → `P&L!C19` "Depreciation & Amortization" (combined with `R&D\\\_NRE!D18`), and → `BalanceSheet!C13` "Accumulated depreciation" (made cumulative on the BS). **4. Structural Detail & Key Formulas — DEPRECIATION SCHEDULE LOGIC (explicit):**

- **Method:** Straight-line (sheet title literally reads "Capital Expenditure & Depreciation (Straight-line)"). Annual charge per vintage = spend ÷ life.

- **Useful life:** per-item in column C — e.g. VNA 7 yr, anechoic 15 yr, cleanroom 10 yr, SMT line 7 yr, HALT/HASS 10 yr, EMI/EMC 15 yr, RF/EW bench 7 yr, FPGA stations 5 yr, GPU cluster 4 yr, UAS hangar 20 yr, maritime tank 20 yr, office/facilities 15 yr, IT/network 5 yr, vehicles 5 yr.

- **How accumulated depreciation builds:** Each item's yearly cell adds `spend\\\_v / life` for every vintage `v` whose age is still **less than** the life — the `IF(C\\\>k, ...)` guards switch a vintage *off* once it has fully depreciated. Year-1 cell has one term; Year-2 cell has two (prior vintage tested with the larger threshold, current with `\\\>0`), and so on. Crucially, the **Balance Sheet** turns this annual D&A into *accumulated* depreciation by running its own cumulative sum (`=C13+Capex!E39` …); the Capex sheet itself reports the annual charge, not the running balance.

- Key formulas (verbatim — the depreciation schedule):

  - `D24` `=IFERROR((IF(C6\\\>0,D6/C6,0))/100,0)` — Y1 VNA depreciation: only the Y1 vintage, charged if life\>0; ÷100 to ₹ Cr; `IFERROR`→0 guards a zero/blank life.

  - `F24` `=IFERROR((IF(C6\\\>2,D6/C6,0)+IF(C6\\\>1,E6/C6,0)+IF(C6\\\>0,F6/C6,0))/100,0)` — Y3 VNA depreciation = sum of the Y1 vintage (still alive if life\>2), Y2 vintage (life\>1), and Y3 vintage (life\>0). This is the vintage-by-vintage straight-line accumulation; each older vintage drops out when its `C\\\>k` test fails.

  - `D39` `=SUM(D24:D38)` — total annual D&A Y1 = ₹5.397 Cr.

**5. Glossary of Terms:**

- **Capex** — Capital Expenditure; spend on long-lived physical/intangible assets capitalised on the balance sheet rather than expensed.

- **Depreciation** — periodic allocation of a tangible asset's cost over its useful life (here straight-line).

- **Straight-line** — equal depreciation each year = cost ÷ useful life.

- **Useful life (yr)** — the number of years over which an asset is depreciated.

- **Vintage** — the year an asset was purchased; each year's spend depreciates on its own clock.

- **PP&E** — Property, Plant & Equipment; the gross/net fixed-asset line on the balance sheet.

- **Gross PP&E** — cumulative capex before depreciation. **Net PP&E** — gross less accumulated depreciation.

- **Accumulated depreciation** — running total of depreciation charged to date (built on the Balance Sheet, fed by Capex row 39).

- **D&A** — Depreciation & Amortisation; the combined non-cash charge in the P&L.

### Opex

#### Table A — Operating expenses, non-personnel \[rows 5–23\]

**Type:** Calculation Engine (mostly Input, three assumption-driven lines) **1. Functional Overview:** The non-personnel operating-expense stack. 15 line items (R6:R20) in ₹ L: facilities/rent/utilities, cloud/compute, software licences (CAD/EDA/HFSS/MATLAB), travel & demos, defense exhibitions, certifications (DO-178/254, AS9100), ITAR/export-control overhead, cybersecurity/CMMC L3, quality/CMMI/AS9100 ops, insurance, legal/IP, bid & proposal direct costs, recruiting/training, range/flight-test ops, miscellaneous/contingency. Plus a bank-guarantee fee line (R21, ₹ Cr) and a partner-lab prepaid-opex line (R23). Row 22 totals in ₹ Cr. **2. Strategic Significance:** Captures the real, recurring compliance and go-to-market cost of operating as an Indian defense prime — export control, CMMC L3, AS9100/CMMI, and bid-&-proposal are *structural* costs of competing for fixed-price MoD programmes, not optional spend. Several lines are assumption-driven and escalate at 4%/yr, keeping the cost base honest as the business scales; the bank-guarantee fee ties operating cost to the working-capital/backlog mechanics. The partner-lab credit line (₹380 L, reclassified from Capex in milestone m4 to prepaid opex under Ind AS) reflects the asset-light early strategy. **3. Modeling Impact & Data Flow:**

- Upstream dependencies: `Assumptions!$C$18` (export-control overhead ₹2 Cr), `$C$19` (cyber/CMMC L3 ₹14.25 Cr), `$C$20` (quality/AS9100/CMMI ₹8.55 Cr), each ×`(1+Assumptions!$C$8)^year`; `Backlog!D64` (bank-guarantee fee). Remaining lines are hard-coded ₹ L inputs.

- Downstream outputs: `R22` → `P&L!C15` "Other Opex (facilities, compliance, exhibitions, etc.)" — the **only** external consumer of this sheet. **4. Structural Detail & Key Formulas:**

- Structure: 23×14. Header row 4 (`Item | Y1..Y10`). Inputs in ₹ L; total converted to ₹ Cr.

- Key formulas:

  - `D12` `=Assumptions!$C$18\\\*100\\\*(1+Assumptions!$C$8)^0` — ITAR/export-control overhead: ₹ Cr assumption ×100 → ₹ L, escalated; pattern repeats for cyber (`D13`) and quality (`D14`).

  - `D21` `=Backlog!D64` — bank-guarantee (PBG+ABG) fee in ₹ Cr, pulled from the backlog engine.

  - `D22` `=SUM(D6:D20)/100+D23/100+D21` — Total Opex (non-personnel) = (₹ L line items ÷ 100) + partner-lab credit (₹ L ÷ 100) + BG fee (already ₹ Cr) = ₹41.70 Cr Y1.

- **STRUCTURAL NOTE / minor anomaly:** Row 23 (partner-lab prepaid credit, ₹380 L) sits *below* the total row 22 but is explicitly added back into R22 (`+D23/100`); it is not double-counted because R22's `SUM(D6:D20)` stops at row 20. Row 19 (range/flight-test ops) is ₹0 in Y1 — expected, since UAS/AUV ranges come online later.

**5. Glossary of Terms:**

- **Opex** — Operating Expenses; recurring period costs (here the non-personnel portion: facilities, compliance, GTM, etc.) that hit the P&L below gross profit.

- **S&M / G&A** — Sales & Marketing / General & Administrative expense; in this model the *non-personnel* part of these flows partly through "Other Opex" while the %-of-revenue driver lives in the P&L (see flag below).

- **ITAR / Export control** — defense trade-compliance regime; a mandatory recurring overhead.

- **CMMC L3 / AS9100 / CMMI / DO-178 / DO-254** — defense and aerospace quality/cyber/software certifications carrying recurring operating cost.

- **Bid & Proposal (B&P)** — direct cost of competing for fixed-price programme awards.

- **Bank guarantee (PBG/ABG) fee** — annual fee on Performance/Advance Bank Guarantees posted against backlog.

- **Prepaid opex (Ind AS)** — partner-lab usage credits reclassified from capex to a prepaid operating expense.

### S&M / G&A %-Driver Verification (cross-sheet, requested by prior audit)

**The %-of-revenue drivers ARE consumed — they live in the P&L, not in Opex.** `Assumptions!C15` (S&M = 8% of revenue) and `Assumptions!C16` (G&A = 7% of revenue) are consumed by `P&L!C13` `=MAX(Headcount!D69,C5\\\*Assumptions!$C$15)` and `P&L!C14` `=MAX(Headcount!D70,C5\\\*Assumptions!$C$16)`, where `C5` is P&L revenue. The driver is therefore **binding** (it is the larger of the two `MAX` arguments).

**Orphan finding:** Because the %-of-revenue figure exceeds the bottom-up personnel figure in all 10 years, **Headcount rows 69 (S&M personnel) and 70 (G&A personnel) are the non-binding `MAX` argument and never flow to the P&L** — they are computed-but-orphaned floors. This is documented by the workbook itself in `Headcount!B76`. No silent error; it is an intentional floor that simply never activates. Opex (this scope's sheet) holds neither the S&M nor G&A %-driver — those are in `Assumptions` and consumed in `P&L`; Opex contributes only the single "Other Opex" line.

## 6. The Integrated Three-Statement Model

The final layer of the NDAD model is the integrated three-statement engine: **P&L**, **CashFlow**, and **BalanceSheet**. These three sheets are *consumers* of the operating build (Revenue/Backlog, Headcount, Capex, Opex, R&D\_NRE, Funding) and *producers* of the headline financials that drive valuation. They articulate so that the P&L net income flows into both cash and equity, capex flows into both investing cash and PP&E, funding flows into both financing cash and the capital structure, the cash-flow closing-cash becomes the balance-sheet cash plug, and the balance sheet ties out exactly (Assets − (Liabilities + Equity) = 0 in every year).

**Column convention (verified):** P&L / CashFlow / BalanceSheet use columns **C:L for Y1–Y10** (row 4 headers confirmed: C=Y1 … L=Y10). The **Funding** sheet uses **D:M for Y1–Y10** (Funding row 4: D=Y1 … M=Y10). Every pull from Funding therefore carries a **one-column left offset** — e.g. P&L Y1 interest `C21 = Funding!D17`, BalanceSheet Y1 debt `C21 = Funding!D16`. The Revenue sheet likewise leads by one column (P&L Y1 revenue `C5 = Revenue!D12`).

**Balance check result:** Using `data\\\_only=True` values, BalanceSheet row 32 `Check (A = L + E) = Assets − (Liab+Equity)` returns **0 in all ten years (max absolute residual = 0)**. The model balances perfectly.

### 6.1 P&L (Income Statement)

**Type:** Output / Reporting — a calculated income statement. It contains no independent assumptions; every line is either a cross-sheet pull or an arithmetic roll of other P&L rows. The only embedded logic is the tax sub-schedule (NOL pool + MAT + R&D tax bridge, rows 26–43), which is a self-contained calculation block feeding row 23/38.

**1. Functional Overview:** The 10-Year Consolidated Income Statement. It assembles revenue and COGS into gross profit, subtracts the operating-cost stack (R&D/NRE, S&M, G&A, other Opex) to reach EBITDA, deducts D&A to reach EBIT, deducts interest to reach pretax income, applies the tax schedule, and reports NET INCOME (row 24). Dimensions 43×13; 328 formulas.

**2. Strategic Significance:** This sheet is the **path-to-profitability** statement. Gross margin climbs from **51.5% (Y1) → 66.8% (Y10)** on platform reuse (M1–M5 modules carry NRE off the per-product P&L) and rising high-margin V6 software mix (93–94% GM). EBITDA crosses zero by **Year 4** (Y1 −₹324.5 Cr → Y3 −₹22.8 Cr → Y4 +₹190.5 Cr), and the EBITDA margin trajectory runs **−618% (Y1) → +22.3% (Y4) → +46.4% (Y10)**, landing in the defense-software-influenced 40%+ band. NET INCOME turns positive in **Year 4 (+₹99.5 Cr)** and compounds to **₹1,717 Cr by Y10**. Early-year losses are tax-shielded by the NOL pool (all losses utilised by Y3 per the model note), with MAT (15%) applying from first book profitability — establishing a realistic Indian-tax path to GAAP profit.

**3. Modeling Impact & Data Flow:**

- **Upstream dependencies:**

  - Revenue (backlog-driven): `Revenue!D12` → total revenue (R5); `Revenue!D29` → COGS-BoM (R6).

  - Headcount: `Headcount!D68` → COGS personnel/service (R7); `Headcount!D69/D70` → S&M / G&A personnel floors (R13/R14).

  - R&D\_NRE: `'R&D\\\_NRE'!D12` → R&D/NRE expense (R12); `'R&D\\\_NRE'!D18` (amortisation) and `'R&D\\\_NRE'!D16` (capitalised dev) → D&A (R19) and the tax R&D bridge (R29–R43).

  - Capex: `Capex!D39` (depreciation) → D&A (R19).

  - Opex: `Opex!D22` → other Opex (R15).

  - Funding (D:M offset): `Funding!D17` → interest expense (R21).

  - Assumptions: `$C$15`/`$C$16` (S&M/G&A opex %), `$C$6` (25% tax), `$C$37` (15% MAT).

- **Downstream outputs:**

  - Net income (R24) → CashFlow R6 (CFO) and → BalanceSheet R26 (retained earnings).

  - D&A (R19) → CashFlow R7 (non-cash add-back).

  - Closing MAT credit asset (R38) → BalanceSheet R11/R40 (DTA) and CashFlow R15 (non-cash DTA adjustment).

  - Revenue (R5) and COGS (R8) → CashFlow working-capital memos (R8–R10) and thence BalanceSheet AR/Inv/AP.

  - EBIT (R20) → BalanceSheet ROIC (R35). Net income / margins → KPIs and Valuation.

**4. Structural Detail & Key Formulas:**

- **Structure:** Header in B2; B4 "Line item" with C4:L4 = Y1…Y10. Column B holds row labels; C:L hold numeric formulas (₹ Cr). Three logical blocks: (a) operating P&L R5–R24; (b) tax detail R26–R38; (c) tax R&D bridge memo R40–R43.

- **Key formulas (verbatim, Y1 column C):**

  - Gross profit: `C9` `=C5-C8` where COGS `C8` `=C6+C7` — revenue less (BoM + personnel/service COGS); gross margin `C10` `=IFERROR(C9/C5,0)`.

  - **EBITDA build:** `C16` `=C9-C12-C13-C14-C15` — gross profit minus R&D/NRE, S&M, G&A and other Opex (the full operating-cost stack, before D&A and interest). Margin `C17` `=IFERROR(C16/C5,0)`.

  - D&A: `C19` `=Capex!D39+'R&D\\\_NRE'!D18` — PP&E depreciation plus capitalised-R&D amortisation.

  - **EBIT build:** `C20` `=C16-C19` — EBITDA less D&A.

  - **Net-income build:** `C22` `=C20-C21` (pretax = EBIT − interest, `C21=Funding!D17`); tax `C23` `=C33`; `C24` `=C22-C23` (NET INCOME = pretax − tax).

  - Tax engine: regular tax `C33` `=C32\\\*Assumptions!$C$6` on taxable income `C32` `=MAX(0,(C27+'R&D\\\_NRE'!D18-'R&D\\\_NRE'!D16)-C30)` (book PBT, R&D tax bridge, less NOL utilised); MAT `C34` `=MAX(0,C27)\\\*Assumptions!$C$37`; closing MAT credit asset `C38` `=C35+C37-C36`.

**5. Glossary of Terms:** **COGS** — cost of goods sold (BoM + production personnel/service). **Gross profit / gross margin** — revenue − COGS, and that as % of revenue. **R&D/NRE** — research & non-recurring engineering. **S&M / G&A** — selling & marketing / general & administrative expense. **EBITDA** — earnings before interest, tax, depreciation & amortisation (operating profit pre-D&A). **D&A** — depreciation (PP&E) & amortisation (capitalised R&D). **EBIT** — operating profit after D&A. **Pretax income (PBT)** — EBIT − interest. **NET INCOME** — profit after tax. **NOL** — net operating loss carry-forward pool shielding early-year tax. **MAT** — Minimum Alternate Tax (15%), creditable as a DTA. **DTA** — deferred tax asset (MAT credit). **Operating / net margin** — EBIT and net income as % of revenue.

### 6.2 CashFlow (Cash Flow Statement)

**Type:** Output / Reporting — a calculated cash-flow statement. Lines are pulls from P&L, Funding, Capex, Backlog and Assumptions, plus arithmetic rolls. Working-capital lines are memo derivations from P&L revenue/COGS via day-count assumptions.

**1. Functional Overview:** The 10-Year Cash Flow Statement, split into CFO (operating, A), CFI (investing, B), CFF (financing, C), then FCF & cash position (D). It converts accrual net income to cash by adding back D&A, subtracting the working-capital build, adding customer advances, then nets capex/restricted-cash/capitalised-R&D and financing flows, and rolls the closing cash balance. Dimensions 35×13; 250 formulas.

**2. Strategic Significance:** This is the **self-funding** statement. FCF (CFO+CFI) is negative Y1–Y3 (−₹359.9, −₹467.7, −₹234.1 Cr) and turns positive in **Year 4 (+₹3.0 Cr)**, accelerating to **+₹1,660.9 Cr by Y10** — confirming the business funds its own growth from Y4 onward. CFF is front-loaded (₹470, ₹500, ₹330 Cr equity/debt in Y1–Y3) then goes negative (debt repayment) from Y5, demonstrating the external-capital taper. The closing cash balance never breaches the minimum-reserve alert (row 35), rising to **₹5,903 Cr by Y10**, evidencing balance-sheet resilience across the long Indian defense cash cycle (the model explicitly tracks AR/Inventory/AP day-counts, customer advances, and BG-collateral restricted cash).

**3. Modeling Impact & Data Flow:**

- **Upstream dependencies:** P&L net income `'P&L'!C24` (R6), D&A `'P&L'!C19` (R7), MAT credit `'P&L'!C38` (R15); Assumptions `$C$11`(DSO)/`$C$12`(DPO)/`$C$13`(InvDays)/`$C$25`(min cash) for the WC memos; Backlog `D57`(Δ advances), `D63`(restricted/BG collateral), `D56`; Capex `Capex!D21` (gross capex, R17); R&D\_NRE `'R&D\\\_NRE'!D16` (capitalised R&D, R19/R32); Funding (D:M offset) `Funding!D9` (equity, R22), `Funding!D13/D14` (debt draw/repay, R23).

- **Downstream outputs:** Closing cash `C30` → BalanceSheet cash `C6` (the cash plug). WC memos R8/R9/R10 → BalanceSheet AR (`C8`), Inventory (`C9`), AP (`C19`). FCF and cumulative FCF (R27/R28) → returns/IRR/NPV (file 06). Min-cash buffer & alert (R34/R35) → Funding-sizing feedback.

**4. Structural Detail & Key Formulas:**

- **Structure:** B2 title; B4 "Line item", C4:L4 = Y1…Y10. Sections A (CFO, R5–R15), B (CFI, R16–R19), C (CFF, R21–R24), D (FCF & cash, R26–R35). ₹ Cr.

- **Key formulas (verbatim, Y1 = C; Y2 = D shows the Δ logic):**

  - **Operating cash (CFO):** `C14` `=C6+C7-C12+C13+C15` — net income + D&A − ΔWorking capital + Δcustomer advances + ΔMAT-credit adjustment. Working capital `C11` `=C8+C9-C10` (AR+Inv−AP); ΔWC `C12` `=C11` in Y1 then `D12` `=D11-C11` thereafter (Day-0 NWC=0). DTA adj `C15` `=-'P&L'!C38`.

  - Investing (CFI): `C19` `=C17+C18-'R&D\\\_NRE'!D16` — −gross capex (`C17=-Capex!D21`) − Δrestricted cash (`C18=-Backlog!D63`) − capitalised R&D.

  - Financing (CFF): `C24` `=C22+C23` — equity raised + net debt.

  - Free cash flow: `C27` `=C14+C19` (CFO + CFI).

  - **Closing-cash roll-forward:** net change `C29` `=C27+C24` (FCF + CFF); cash EoY `C30` `=C29` in Y1, then `D30` `=C30+D29` — i.e. **prior-year closing cash + current-year net change**. Cumulative FCF `D28` `=C28+D27`.

  - Control: `C35` `=IF(C30\\\<Assumptions!$C$25,"BELOW MIN - RAISE/DRAW","OK")`.

**5. Glossary of Terms:** **CFO / CFI / CFF** — cash from operations / investing / financing. **FCF** — free cash flow (CFO + CFI). **Working capital (NWC)** — AR + Inventory − AP, the cash tied up in the operating cycle. **AR / AP** — accounts receivable (DSO-based) / accounts payable (DPO-based). **DSO / DPO / Inventory days** — day-count drivers from Assumptions. **Customer advances (contract liability)** — cash received ahead of revenue recognition. **Restricted cash (BG collateral)** — cash pledged against bank guarantees. **Capitalised R&D** — development spend recorded as an intangible (within CFI). **Cash plug** — closing cash that becomes the balancing cash line on the balance sheet.

### 6.3 BalanceSheet

**Type:** Output / Reporting — a fully articulated balance sheet. Every line is a cross-sheet pull or a cumulative roll; the Check row (R32) and ratio block (R33–R36) are verification/analytics. It carries no independent assumptions (WC and CCC come from Assumptions day-counts).

**1. Functional Overview:** The Integrated Balance Sheet, stating Assets (A), Liabilities (B), Shareholders' Equity (C), and a Check & ratios block (D). Cash is the plug from CashFlow; PP&E is gross cumulative capex less accumulated depreciation; intangibles are cumulative capitalised R&D less amortisation; retained earnings is cumulative net income; paid-in capital is cumulative equity. Dimensions 40×13; 280 formulas.

**2. Strategic Significance:** This sheet evidences **capital-structure strength**. Debt/Equity peaks at **0.75 (Y2)** as venture debt funds the trough, then de-levers to **~0.0 by Y8** as retained earnings build and debt is repaid — the business becomes essentially unlevered and self-financing. The current ratio strengthens from **2.24 (Y1) to 3.36 (Y10)**, signalling ample short-term liquidity through the long defense cash cycle. Retained earnings is deeply negative through the J-curve (trough −₹782 Cr at Y3) and turns positive at **Year 6 (+₹388.6 Cr)**, compounding to **+₹5,548 Cr by Y10**. Total assets grow from ₹201.8 Cr to ₹9,357 Cr, with cash (₹5,903 Cr) the dominant Y10 asset — a fortress balance sheet that backs the valuation case.

**3. Modeling Impact & Data Flow:**

- **Upstream dependencies:** CashFlow `C30` → cash (R6), and WC memos `CashFlow!C8/C9/C10` → AR/Inventory/AP (R8/R9/R19); Backlog `D63` (restricted cash R7), `D56` (contract liabilities R20); P&L `C38` (MAT credit DTA, R11/R40), `C24` (retained earnings, R26), `C20` (EBIT for ROIC, R35); Capex `D21` (gross PP&E, R12), `D39` (accumulated depreciation, R13); R&D\_NRE `D16`/`D18` (intangibles & amortisation, R15/R37/R38); Funding (D:M offset) `D9` (paid-in capital, R25), `D16` (venture debt, R21); Assumptions `$C$6`(tax), `$C$11/$C$12/$C$13` (CCC).

- **Downstream outputs:** Terminal balance-sheet metrics (cash, equity, net debt, ROIC, D/E) feed Valuation and the returns/sensitivity analysis (file 06). The Check row (R32) is the integrity gate confirming the whole three-statement system reconciles.

**4. Structural Detail & Key Formulas:**

- **Structure:** B2 title; B3 methodology note; B4 "Line item", C4:L4 = Y1…Y10. Sections A Assets (R5–R16), B Liabilities (R18–R22), C Equity (R24–R29), D Check/ratios (R31–R40). ₹ Cr.

- **Key formulas (verbatim, Y1 = C; Y2 = D shows cumulative roll):**

  - Cash plug: `C6` `=CashFlow!C30`. Net PP&E `C14` `=C12-C13` where gross PP&E `D12` `=C12+Capex!E21` (cumulative capex) and accumulated dep `D13` `=C13+Capex!E39`. Net intangibles `D15` `=C15+'R&D\\\_NRE'!E16-'R&D\\\_NRE'!E18`.

  - Total assets: `C16` `=C10+C11+C14+C15` (current assets + MAT-DTA + net PP&E + net intangibles).

  - Liabilities: AP `C19` `=CashFlow!C10`; contract liabilities `C20` `=Backlog!D56`; venture debt `C21` `=Funding!D16`; total `C22` `=C19+C20+C21`.

  - **Retained-earnings link:** `C26` `='P&L'!C24` in Y1, then `D26` `=C26+'P&L'!D24` — **prior retained earnings + current-year net income** (cumulative net income). Paid-in capital `D25` `=C25+Funding!E9`. Total equity `C27` `=C25+C26`.

  - **Balancing identity:** total L+E `C29` `=C22+C27`; **Check `C32` `=C16-C29`** (Total Assets − Total Liabilities & Equity). Verified **= 0 for all Y1–Y10** (max |residual| = 0). The balance ties because cash is the CashFlow plug and equity absorbs cumulative net income, so Assets ≡ Liabilities + Equity by construction.

  - Ratios: current ratio `C33` `=IFERROR(C10/(C19+C20),0)`; D/E `C34` `=IFERROR(C21/C27,0)`; ROIC `C35` `=IFERROR('P&L'!C20\\\*(1-Assumptions!$C$6)/(C21+C27),0)`; CCC `C36` `=Assumptions!$C$11+Assumptions!$C$13-Assumptions!$C$12` (constant 195 days by assumption).

**5. Glossary of Terms:** **PP&E** — property, plant & equipment (gross capex less accumulated depreciation). **Net intangibles** — capitalised R&D less accumulated amortisation. **Retained earnings** — cumulative net income retained in the business. **Paid-in capital** — cumulative equity raised. **Contract liabilities / customer advances** — revenue billed/collected ahead of recognition (a liability). **Restricted cash** — cash pledged as BG collateral. **MAT credit asset (DTA)** — deferred tax asset from MAT paid. **Working capital** — AR + Inventory − AP. **Current ratio** — current assets ÷ current liabilities. **D/E** — debt ÷ equity. **ROIC** — NOPAT ÷ (debt + equity). **CCC** — cash conversion cycle (DSO + Inventory days − DPO). **Balancing identity** — Assets = Liabilities + Equity, the closure condition of a sound three-statement model.

## 7. Funding, Returns, KPIs & Break-Even (Outputs & Valuation)

This section documents the three output/reporting-layer sheets of the NDAD V2 workbook: **Funding** (the capital-raise / financing-cash-flow engine), **BreakEven** (per-vertical contribution + company break-even + the model's headline financial indicators including IRR and NPV), and **KPIs** (the investor-facing executive dashboard, cumulative indicators, and a Terminal-Value / Equity-Returns memo). All figures are in Indian Rupees Crore (₹ Cr) over the Y1–Y10 horizon.

> **CRITICAL COLUMN-OFFSET CONVENTION (verified live).** The **Funding** sheet places Y1–Y10 in **columns D:M**, whereas **every other statement** (P&L, CashFlow, BalanceSheet, Revenue, Backlog, KPIs, BreakEven) uses **C:L**. Cross-sheet links therefore shift by exactly one column. This is confirmed verbatim by `Funding!D25 = =CashFlow!C30` (Funding's Y1 column D reads CashFlow's Y1 column C) and, in the reverse direction, by `KPIs!C26 = =Funding!D9` and `KPIs!C27 = =Funding!D16` (KPIs' Y1 column C reads Funding's Y1 column D). This offset is a **known fragility**: inserting or deleting a single column anywhere on the Funding sheet would silently misalign every consumer (KPIs rows 26–27, BalanceSheet, and the cross-references in BreakEven rows 37–38). It must be preserved on any edit.

### Funding (28×14, 109 formulas)

**Type:** Calculation Engine (financing cash-flow / capital-stack engine) — NOT a valuation or cap-table engine.

**1. Functional Overview:** Builds the financing side of the model: (A) the equity round schedule, (B) the venture-debt schedule (draw / repay / balance roll-forward / interest), (C) the consolidated Cash-Flow-from-Financing (CFF) line, and (D) a minimum-cash compliance check that confirms projected end-of-year cash never falls below the reserve target. It is the source of the "Equity raised" and "Debt balance" rows consumed downstream, and feeds CFF into the three-statement cash flow.

**2. Strategic Significance:** This is **the funding ask**. The plan raises **₹1,100 Cr of equity across three down-sized rounds** — Seed (Y1) ₹450 Cr, Series A (Y2) ₹400 Cr, Series B (Y3) ₹250 Cr (rows 6–9) — plus **₹200 Cr of venture/bank debt** drawn Y1–Y3 (₹20 + ₹100 + ₹80, row 13) at 8% (row 12), repaid Y5–Y9 on a ₹36/36/55/65/8 schedule (row 14). The strategic message is **capital efficiency and a step-DOWN round structure** (450 \> 400 \> 250): the Day-1 ESM cash engine self-funds the company from Y4, so no Series C is required. The min-cash check (rows 23–26) is the **runway proof** — projected EoY cash (row 25) stays above the ₹100 Cr reserve target every year, so the funding gap (row 26) is ₹0 throughout, i.e. the rounds as sized are sufficient. The narrative layer (`05\\\_funding\\\_and\\\_capital.md` §E "Dilution Mathematics" and `06\\\_returns\\\_and\\\_sensitivity.md` §H "Investor Returns by Round") wraps **illustrative pre/post-money valuations and a cap table** around these flows (Seed 1,800 pre / 20% stake; A 4,500 pre / 8.2%; B 8,000 pre / 3.0%; post-B founders+ESOP ~71.3%) — but those are **analyst assumptions, not computed in this sheet**.

**3. Modeling Impact & Data Flow:**

- **Upstream dependencies:**

  - `Funding!D24:M24 = =Assumptions!$C$25` — min-cash reserve target (₹100 Cr).

  - `Funding!D25:M25 = =CashFlow!C30 … =CashFlow!L30` — projected EoY cash. **This is the D:M → C:L offset in action** (Funding column D pulls CashFlow column C).

  - Equity rows (6–8), debt draw/repay (13–14), and interest rate (12) are hard-keyed inputs/assumptions, not pulled from other sheets.

- **Downstream outputs:**

  - `KPIs!C26 = =Funding!D9` (Equity raised) and `KPIs!C27 = =Funding!D16` (Debt balance EoY) — again the offset (KPIs C ← Funding D).

  - `BreakEven!C37 = =SUM(Funding!D9:M9)` (total equity raised) and `BreakEven!C38 = =MAX(Funding!D16:M16)` (peak debt).

  - Total CFF (row 22) and interest expense (row 17) feed the CashFlow / P&L. These are otherwise **terminal financing outputs**.

**4. Structural Detail & Key Formulas:**

- **Structure:** Header row 4 (`Round/Item`, `Detail`, then `Y1..Y10` in D4:M4). Four labelled blocks: **A. Equity rounds** (5–10), **B. Venture debt** (11–17), **C. CFF** (19–22), **D. Min-cash compliance check** (23–28). Column B = long descriptive labels, column C = detail notes, D:M = numeric. Data types: ₹ Cr amounts, a rate (8%), and counts of years.

- **Key formulas (verbatim):**

  - `D9` `=SUM(D6:D8)` — total equity raised per year (sum of the three round rows).

  - `D16` `=MAX(0,D15+D13-D14)` — **debt-balance roll-forward**: EoY balance = BoY + drawn − repaid, floored at 0; `E15 = =D16` carries EoY into next-year BoY.

  - `D17` `=MAX(0,(D15+D16)/2)\\\*D12` — **interest expense on the average balance** × annual rate.

  - `D22` `=D20+D21+D10` — **Total CFF** = equity inflow + net debt + grant top-up (row 10).

  - `D24` `=Assumptions!$C$25` — min-cash target; `D25` `=CashFlow!C30` — projected EoY cash (**offset link**).

  - `D26` `=MAX(0,D24-D25)` — **funding gap** = shortfall vs the reserve target (0 in all years → rounds are adequately sized).

- **Valuation / IRR / MOIC / cap table: NONE on this sheet.** The Funding sheet computes the financing stack, runway adequacy, and debt economics only. It does **not** compute pre/post-money valuation, IRR, MOIC, or a cap table. (IRR/NPV are on BreakEven & KPIs; the valuation/cap-table/MOIC-by-round live only in the narrative markdown as analyst assumptions.)

**5. Glossary of Terms:** **CFF** (Cash Flow from Financing — net cash from equity issuance + debt draws/repayments). **Venture debt** (loan capital raised alongside equity, here at 8%). **Runway** (months/years the business can operate before cash hits the reserve floor — proven here by rows 24–26). **Min-cash reserve target** (the ₹100 Cr floor below which the model must not dip). **Funding gap** (shortfall of projected cash vs the reserve target; \>0 would mean rounds need up-sizing). **Pre-money / Post-money** (company valuation immediately before / after a round; pre + investment = post — narrative only). **Dilution** (reduction in existing holders' ownership % as new shares are issued). **Cap table** (the ownership register by stakeholder — Founders+ESOP / Seed / A / B; narrative only). **BoY / EoY** (Beginning- / End-of-Year balance).

### BreakEven (40×7, 55 formulas)

**Type:** Calculation Engine + Output/Reporting (per-vertical contribution analysis, company break-even, and the model's consolidated financial-indicator block).

**1. Functional Overview:** Three analytic layers plus a headline-indicator block: (A) per-vertical revenue / COGS / gross profit / GM% / units at a chosen snapshot year (row 4, default Y6); (B) the fixed-cost stack at that snapshot year; (C) the company break-even revenue = fixed cost ÷ weighted GM%; and (D) full-10-year key financial indicators — first EBITDA-positive year, first FCF-positive year, peak cash deficit, cumulative revenue/EBITDA/net income, NPV, and **Project IRR**.

**2. Strategic Significance:** Answers the investor's two survival questions — *"how much revenue do we need to cover costs?"* and *"when do we turn the corner?"* The snapshot break-even revenue is **₹989.5 Cr** (row 27) at a weighted gross margin of **65.8%** (row 26); the company is **EBITDA-positive in Year 4** (row 30) and **FCF-positive in Year 4** (row 31), with a peak cumulative cash deficit of **−₹1,061.8 Cr** (row 32) — the maximum the funding stack must cover. It also carries the **base-case returns**: NPV of FCF **₹747.2 Cr** at the 18% WACC (row 39) and **Project IRR 31.9%** (row 40). Critically, row 40's label flags that this is **project IRR on FCF only — it EXCLUDES equity/debt flows and is NOT the investor IRR** (the investor MoIC/IRR-by-round table is analyst-built in the narrative).

**3. Modeling Impact & Data Flow:**

- **Upstream dependencies (this is the recognized-basis tie-out):**

  - **Rows 8–13 pull the RECOGNIZED REVENUE BASIS:** revenue from `Revenue!$D$6:$M$6 … $D$11:$M$11` (rows 6–11) and BoM COGS from `Revenue!$D$23:$M$23 … $D$28:$M$28` (rows 23–28), both selected by the snapshot year via `INDEX(...,$C$4)`. Because Revenue is backlog-driven and flows to the P&L, BreakEven **ties to the P&L** — it is the *recognized* (delivered) basis, not the planned-shipment basis.

  - **Column G (units) is V-sheet PLANNED shipments for CONTEXT ONLY** — `G8 = =INDEX(V1\\\_AESA!$D$33:$M$33,$C$4)`, `G9 = =INDEX(V2\\\_EW\\\_SIGINT!$D$41:$M$41,$C$4)`, etc. Row 15 states this verbatim: *"Revenue & BoM COGS = recognized basis … Units (col G) = planned shipments from V-sheets, shown for context only."* The distinction is explicit: do **not** treat column G as the recognized basis.

  - Fixed-cost stack (rows 17–22) pulls from `R&D\\\_NRE!D12:M12`, `P&L!C7/C13/C14/C15/C19` (COGS-personnel, S&M, G&A, Other Opex, D&A) via `INDEX(...,$C$4)`.

  - Indicator block reads `P&L` (rows 5/16/24), `CashFlow` (rows 27/28/30), `Assumptions!$C$7` (WACC), and `Funding!D9:M9` / `Funding!D16:M16` (note the offset when reading Funding).

- **Downstream outputs:** Terminal — this sheet is read by humans / the deck; the same indicators are mirrored into KPIs rows 36–47.

**4. Structural Detail & Key Formulas:**

- **Structure:** `Snapshot year` control in `C4` (1..10, default 6). Block A is a 6-vertical table (rows 8–13) + total (14) with columns C:G = Revenue/COGS/GrossProfit/GM%/Units. Block B = 6-line fixed-cost stack + total (23). Block C = GM% and break-even revenue. Block D = 12 single-cell full-horizon indicators (rows 30–40).

- **Key formulas (verbatim):**

  - `C8` `=INDEX(Revenue!$D$6:$M$6,$C$4)` — vertical revenue at the snapshot year (**recognized basis**); `D8` `=INDEX(Revenue!$D$23:$M$23,$C$4)` — BoM COGS.

  - `F8` `=IFERROR(E8/C8,0)` — vertical gross margin %; `F14` `=IFERROR(E14/C14,0)` — company weighted GM% (= 65.8%).

  - `C23` `=C17+C18+C19+C20+C21+C22` — **total fixed cost** (₹651.4 Cr).

  - **BREAK-EVEN FORMULA:** `C27` `=IFERROR(C23/C26,0)` — *Break-even annual revenue = Total Fixed Cost ÷ weighted Gross-Margin %* = 651.4 / 0.6583 = **₹989.5 Cr**. (`C26 = =F14`, the contribution-margin proxy.)

  - `C30` `=IFERROR(MATCH(TRUE(),INDEX('P&L'!C16:L16\\\>0,0),0),"n/a")` — first EBITDA-positive year (=4); `C31` likewise on `CashFlow!C27:L27` (first FCF-positive year = 4).

  - `C32` `=MIN(CashFlow!C28:L28)` — peak cumulative cash deficit (−₹1,061.8 Cr).

  - **NPV / IRR (returns):** `C39` `=NPV(Assumptions!$C$7,CashFlow!C27:L27)` — NPV of FCF at 18% WACC (₹747.2 Cr); `C40` `=IFERROR(IRR(CashFlow!C27:L27),0)` — **Project IRR 31.9% (FCF only, excludes equity/debt — NOT investor IRR)**.

  - `C36` `=SUM('R&D\\\_NRE'!D8:M8)-SUM('R&D\\\_NRE'!D6:M6)` — counterfactual NRE avoided (₹994.3 Cr), explicitly labelled *NOT realized cash savings*.

**5. Glossary of Terms:** **Break-even** (revenue level at which total cost is exactly covered; profit = 0). **Contribution margin** (revenue − variable cost, here proxied by gross margin %; the fraction of each ₹ of revenue available to cover fixed cost). **Fixed cost** (costs that do not scale with units — R&D/NRE, S&M, G&A, D&A, COGS-personnel here). **GM% (gross margin)** (gross profit ÷ revenue). **Recognized basis** (revenue/COGS as recognized on the P&L from delivered backlog — vs *planned shipments*). **EBITDA** (Earnings Before Interest, Taxes, Depreciation & Amortisation — operating profitability proxy). **FCF (Free Cash Flow)** (operating cash flow − capex). **NPV** (Net Present Value — future FCFs discounted to today at the WACC). **IRR** (Internal Rate of Return — discount rate at which NPV = 0; here project-level, not investor-level). **WACC** (Weighted Average Cost of Capital — the 18% discount rate, Assumptions!C7).

### KPIs (65×13, 325 formulas)

**Type:** Output/Reporting (the investor-facing executive dashboard) — pure consumer of upstream statements; computes only ratios and a terminal-value memo.

**1. Functional Overview:** The investor dashboard. Four blocks: (1) a **CXO Executive Summary** (rows 2–4) with the five headline numbers; (2) the **Executive KPI Dashboard** (rows 8–33) — a year-by-year (Y1–Y10) grid of ~25 metrics across growth, profitability, balance-sheet, capital and efficiency; (3) **10-year cumulative & strategic indicators** (rows 35–47); (4) an **R&D bucket accounting summary** (rows 49–54); and (5) a **Terminal Value & Equity Returns memo** (rows 56–65).

**2. Strategic Significance:** This is the **investor-facing transparency layer** — every headline claim is traceable to a cell. It surfaces the growth story (Y10 revenue ₹5,055 Cr, Y10 EBITDA ₹2,347 Cr at 46.4% margin), the returns (IRR 31.9%, NPV ₹747 Cr at WACC, 10-yr cumulative FCF ₹4,803 Cr), capital efficiency (revenue per employee climbing to ₹9.3 Cr; ROIC; current ratio), and — uniquely — a **valuation bridge** in the Terminal-Value memo: TV at 12× Y10 EBITDA (₹28,165 Cr), TV via Gordon growth (₹11,405 Cr), each discounted to PV, and an **Equity NPV incl. TV** of ₹6,128 Cr (12× case) / ₹2,926 Cr (Gordon case). Row 65 explicitly notes IRR-including-TV is not auto-computed but would jump ~8–12 pts over the FCF-only IRR. Many rows carry honest counterfactual / non-cash flags (e.g. row 14 "NRE avoided … NOT realized cash").

**3. Modeling Impact & Data Flow:**

- **Upstream dependencies:** Effectively every core statement. `P&L` (revenue 5, gross profit 9, R&D 12, EBITDA 16, net income 24); `CashFlow` (FCF 27, cumulative FCF 28, cash 30, NWC 11); `BalanceSheet` (current ratio 33, ROIC 35, capitalised R&D 39); `Backlog` (restricted cash 63, contract liabilities 56, BGs 62); `Headcount!D34:M34`; `Capex!D21:M21`; `R&D\\\_NRE` and `R&D\\\_Buckets`; `Assumptions!$C$7` (WACC). **Funding links honor the offset:** `C26 = =Funding!D9`, `C27 = =Funding!D16` (KPIs column C ← Funding column D).

- **Downstream outputs:** **Terminal** — this is the top of the reporting stack; consumed by humans / the pitch deck, nothing downstream reads it.

**4. Structural Detail & Key Formulas:**

- **Structure:** Year header `C8:L8 = Y1..Y10`. Dashboard rows 9–33 are 10-wide formula rows (one per year, C:L). Cumulative rows 36–47 and TV rows 57–64 are single-cell. Mix of ₹ Cr values, %, ratios, and a TEXT-formatted summary string (D4). Heavy use of `IFERROR(...,0)` for divide-by-zero safety.

- **Key formulas (verbatim):**

  - Executive summary: `B4` `='P&L'!L5` (Y10 revenue); `D4` `="₹ "&TEXT('P&L'!L16,"\\\#,\\\#\\\#0.0")&" Cr ("&TEXT(IFERROR('P&L'!L16/'P&L'!L5,0),"0.0%")&")"` (Y10 EBITDA & margin string); `F4` `=SUM(CashFlow!C27:L27)` (10-yr cumulative FCF); `H4` `=IFERROR(IRR(CashFlow!C27:L27),0)` (IRR); `J4` `=NPV(Assumptions!$C$7,CashFlow!C27:L27)` (NPV @ WACC).

  - **Growth (the "CAGR" slot):** `L10` `=IFERROR(L9/K9-1,0)` — **revenue growth Y/Y** (current ÷ prior − 1; C10 hard-set to 0 as the base year). **There is NO compound-CAGR `=(End/Start)^(1/n)-1` formula anywhere in the workbook** (verified by full text scan of all three sheets — the string "CAGR" never appears); growth is modelled strictly as year-over-year. The equivalent 10-yr revenue CAGR is implied (≈ `(L9/C9)^(1/9)-1` ≈ 65%) but is not a cell.

  - Margins: `C12` `=IFERROR(C11/C9,0)` (gross margin %); `C16` `=IFERROR(C15/C9,0)` (EBITDA margin %).

  - Efficiency: `C29` `=IFERROR(C9/C28,0)` (**revenue per employee** = revenue ÷ headcount); `C31` `=BalanceSheet!C33` (current ratio); `C32` `=BalanceSheet!C35` (ROIC).

  - Cumulative: `C36` `=SUM('P&L'!C5:L5)` (10-yr revenue ₹21,209 Cr); `C44` `=IFERROR(IRR(CashFlow!C27:L27),0)`; `C43` `=NPV(Assumptions!$C$7,CashFlow!C27:L27)`.

  - **Valuation / returns (Terminal-Value memo):** `C59` `=12\\\*C57` — **TV @ 12× Y10 EBITDA** (₹28,165 Cr); `C60` `=C58\\\*1.03/(Assumptions!C7-0.03)` — **Gordon-growth TV** = Y10 FCF × (1+g) ÷ (WACC − g), g = 3% (₹11,405 Cr); `C61` `=C59/(1+Assumptions!C7)^10` — **PV of TV** discounted 10 yrs at WACC; `C63` `=C43+C61` — **Equity NPV incl. TV (12× case)** = NPV of FCF + PV of TV (₹6,128 Cr); `C64` `=C43+C62` (Gordon case, ₹2,926 Cr).

  - **MOIC: not computed on the sheet.** MoIC and investor-IRR-by-round live only in `06\\\_returns\\\_and\\\_sensitivity.md` §H as analyst assumptions (Seed 6.2–15.8× MoIC / IRR ~30%; A 3.1–7.9× / mid-20s; B 1.9–4.8× / 17–22%).

**5. Glossary of Terms:** **KPI** (Key Performance Indicator). **CAGR** (Compound Annual Growth Rate — `(End/Start)^(1/n)−1`; **the workbook uses Y/Y growth `End/Start−1` instead**, no compounded CAGR cell exists). **Gross / EBITDA margin** (gross profit / EBITDA as a % of revenue). **Revenue per employee** (revenue ÷ headcount — productivity/efficiency ratio). **ROIC** (Return On Invested Capital — NOPAT ÷ (debt + equity)). **Current ratio** (current assets ÷ current liabilities — liquidity). **NWC** (Net Working Capital). **FCF / NPV / IRR / WACC / EBITDA** (as defined above). **Terminal Value (TV)** (estimated business value at the end of the explicit forecast — here via an EBITDA exit multiple or the Gordon perpetuity-growth model). **Gordon growth model** (TV = FCF×(1+g)/(r−g), constant-growth perpetuity, g = 3%, r = WACC). **Equity NPV incl. TV** (present value of explicit-period FCF plus discounted terminal value — the full equity-value estimate). **MOIC / MoIC** (Multiple Of Invested Capital — exit value ÷ invested capital; narrative only). **Pre/post-money, dilution, cap table** (valuation & ownership concepts carried in the narrative, not this sheet).

## 8. Consolidated Master Glossary

Each chapter carries its own local glossary; this is the deduplicated, document-wide reference for non-financial stakeholders.

### Company, products & programmes

| Term | Meaning |
| - | - |
| **NDAD / Nitrodynamics** | Nitrodynamics Aerospace & Defence — the company being modelled. |
| **Platform** | The shared hardware + AI core (modules, IP) reused across all six verticals; the source of the capital-efficiency thesis. |
| **Vertical (V1–V6)** | A product line: V1 AESA, V2 EW/SIGINT, V3 CUAS, V4 UAS/MALE, V5 Autonomous, V6 MilAI. |
| **AESA** | Active Electronically Scanned Array — modern radar architecture (V1). |
| **EW / SIGINT** | Electronic Warfare / Signals Intelligence (V2). |
| **ESM** | Electronic Support Measures — the passive-sensing naval EW system that is NDAD's Day-1 iDEX anchor order. |
| **CUAS** | Counter-Unmanned Aerial Systems — anti-drone defence (V3). |
| **UAS / MALE** | Unmanned Aerial System / Medium-Altitude Long-Endurance drone (V4). |
| **MilAI** | Military AI software/products (V6). |
| **iDEX** | Innovations for Defence Excellence — India's MoD innovation procurement channel; source of the anchor order. |
| **MoQ** | Minimum order Quantity — the 10-system / ₹210 Cr firm ESM order, delivered in two ₹105 Cr phases. |
| **ADITI** | iDEX grant scheme (Acing Development of Innovative Technologies with iDEX) referenced in funding. |
| **MoD** | Ministry of Defence (India). |


### Market & strategy

| Term | Meaning |
| - | - |
| **TAM / SAM / SOM** | Total / Serviceable / Serviceable-Obtainable Market — nested market-size measures. |
| **Reuse %** | Share of a vertical's engineering content satisfied by the shared platform rather than new build — the moat, quantified. |
| **NRE avoided** | Counterfactual engineering cost the platform saves by reuse; a non-cash analytic, not a cash inflow. |


### Revenue, cost & margin

| Term | Meaning |
| - | - |
| **Backlog / order book** | Firm signed orders not yet delivered; the basis for revenue recognition here. |
| **Bookings** | New orders added to backlog in a period. |
| **Recognised deliveries** | The portion of backlog delivered (and therefore recognised as revenue) in a period. |
| **Revenue recognition** | Converting delivered backlog into reported revenue (`Revenue ← Backlog`). |
| **ASP** | Average Selling Price per unit. |
| **BoM** | Bill of Materials — the per-unit hardware cost driving COGS. |
| **COGS** | Cost of Goods Sold — direct cost of delivered product. |
| **Gross margin (GM)** | (Revenue − COGS) ÷ Revenue. |
| **Contribution margin** | Revenue − variable cost; the denominator in break-even revenue. |
| **Wright's Law** | Cost falls a fixed % per doubling of cumulative volume — the learning-curve used to erode BoM. |
| **ASP erosion** | Modelled price decline as volume scales. |


### Engineering & capital

| Term | Meaning |
| - | - |
| **R&D** | Research & Development. |
| **NRE** | Non-Recurring Engineering — one-time design/development cost (vs recurring per-unit cost). |
| **Capitalisation** | Recording development spend as an intangible asset and amortising it, rather than expensing immediately. |
| **Amortisation** | Spreading an intangible's cost over its life (NRE amort life = 6 yrs; vertical NRE = 5 yrs). |
| **Depreciation** | Spreading a tangible asset's cost over its useful life (straight-line, per-vintage). |
| **D&A** | Depreciation & Amortisation. |
| **PP&E** | Property, Plant & Equipment — tangible fixed assets. |
| **Capex / Opex** | Capital expenditure (assets) / Operating expenditure (period costs). |
| **S&M / G&A** | Sales & Marketing / General & Administrative expense (here as % of revenue floors). |
| **FTE** | Full-Time Equivalent headcount. |


### Statements, returns & valuation

| Term | Meaning |
| - | - |
| **P&L** | Profit & Loss (income statement). |
| **EBITDA / EBIT** | Earnings Before Interest, Taxes, (Depreciation & Amortisation) / before Interest & Taxes. |
| **Net income (NI)** | Bottom-line profit after tax. |
| **Working capital (NWC)** | Current assets − current liabilities; AR + Inventory − AP. |
| **AR / AP** | Accounts Receivable / Accounts Payable. |
| **Retained earnings** | Cumulative net income retained in equity. |
| **CFO / CFI / CFF** | Cash Flow from Operations / Investing / Financing. |
| **FCF** | Free Cash Flow. |
| **Runway** | Months/years of cash before depletion; here governed by a ₹100 Cr minimum-cash rule. |
| **WACC** | Weighted Average Cost of Capital — the 18% discount rate (`Assumptions!C7`). |
| **NPV** | Net Present Value (₹747 Cr on project FCF). |
| **IRR** | Internal Rate of Return (31.9% project IRR on FCF; explicitly *not* investor IRR). |
| **MOIC** | Multiple On Invested Capital (a narrative metric; not computed in the workbook). |
| **CAGR** | Compound Annual Growth Rate = (End/Start)^(1/n)−1 — **note:** the workbook reports year-over-year growth only and contains no compounded-CAGR formula. |
| **Terminal value (TV)** | Enterprise value beyond Y10 (12× EBITDA exit and Gordon-growth variants, in KPIs). |
| **MAT / NOL / DTA** | Minimum Alternate Tax / Net Operating Loss / Deferred Tax Asset — the tax-bridge mechanics in P&L. |
| **Pre-/Post-money** | Equity valuation before / after a financing round (narrative only; not in the workbook). |


## 9. Model Integrity & Known Anomalies

Surfaced during the cell-level audit. None are formula errors (the workbook recalculates to zero errors and the balance sheet ties to zero every year); they are documentation nuances and structural cautions worth knowing before editing.

| \# | Finding | Severity | Detail |
| - | - | - | - |
| 1 | **₹200 vs ₹210 Cr label** | Cosmetic | `Cover!C7` / `Strategy!C10` describe the iDEX MoQ as "₹200 Cr"; the workbook math is **₹210 Cr** (10 × ₹21 Cr). Revenue is Backlog-derived (`Backlog!D76 = 105`), so the label is presentation-only and does not affect any number. Recommend correcting the narrative text to ₹210 Cr. |
| 2 | **Column-offset fragility** | Structural | Funding uses **D:M**; all other statements use **C:L**. Consumers honour the one-column shift, so inserting/deleting a column on Funding silently misaligns `P&L`, `BalanceSheet`, `KPIs`, `BreakEven`. Edit Funding columns with care. |
| 3 | **Orphan Headcount rows 69/70** | Benign | Bottom-up S&M/G&A personnel are non-binding floors; the live P&L S&M/G&A lines use `MAX(Headcount!…, Revenue × Assumptions %)` and the %-of-revenue driver wins in all 10 years. The bottom-up rows are computed but never flow through. Self-documented in `Headcount!B76`. |
| 4 | **ReuseMatrix block D (rows 45–49)** | Benign | A display roll-up that duplicates the live R&D\_NRE math; no sheet reads it. The P&L R&D number is assembled in `R&D\\\_NRE`, not here. |
| 5 | **No compounded CAGR** | By design | Growth is reported strictly year-over-year (`=L9/K9-1`); the string "CAGR" appears nowhere in the workbook. If a true CAGR is wanted for the deck, add `=(End/Start)^(1/n)-1`. |
| 6 | **IRR/NPV/valuation location** | Orientation | The Funding sheet is a pure cash-stack/runway tool — it computes **no** valuation. IRR (31.9%) and NPV (₹747 Cr) live on **BreakEven**/**KPIs**; terminal value and equity NPV live in the **KPIs** memo. MOIC and pre/post-money are narrative-only. |
| 7 | **Tax simplification** | By design | Regular tax flows to P&L; MAT credit is carried on the balance sheet / cash only (Ind AS 12 simplification, noted in-sheet). |
| 8 | **Reuse lever at neutral** | Watch | `Assumptions!C26` (global reuse multiplier) = 1, so Platform effective-reuse currently equals raw module maturity. This single knob flexes the entire cost-avoidance thesis. |
| 9 | **Assumptions duplicate constants** | Watch | A later assumptions block (`C51:C54`) partly duplicates active drivers (`C39:C41`); its BoM floor (0.5) differs from the value the V-sheets actually use (`C40`=0.7). Cosmetic today, but a trap if someone repoints a formula to the wrong block. |
| 10 | **Funding grants in CFF** | Cosmetic | `Funding!D22` includes iDEX/ADITI grants in total financing even though labels say grants are "excluded / not relied upon" — a label-vs-formula mismatch worth reconciling. |


## 10. Appendix — Sheet Inventory & Classification

| \# | Sheet | Dim (r×c) | Formulas | Architecture tier | Primary type |
| - | - | - | - | - | - |
| 0 | Cover | 20×6 | 0 | Narrative | Reference |
| 1 | KPIs | 65×13 | 325 | Output / Valuation | Output/Reporting |
| 2 | Strategy | 14×3 | 0 | Narrative | Reference |
| 3 | MarketPositioning | 26×9 | 7 | Narrative | Reference (inert formulas) |
| 4 | Roadmap | 21×13 | 0 | Narrative | Reference |
| 5 | Platform | 25×14 | 70 | **Driver** (R&D/reuse) | Input + Calculation |
| 6 | R&D\_Buckets | 104×13 | 465 | R&D economics | Calculation Engine |
| 7 | ReuseMatrix | 49×14 | 236 | R&D economics | Calculation Engine |
| 8 | Assumptions | 66×4 | 1 | Global inputs | Input/Assumption |
| 9 | V1\_AESA | 36×14 | 204 | Vertical (read-only detail) | Input + Calculation |
| 10 | V2\_EW\_SIGINT | 55×14 | 258 | Vertical + iDEX MoQ bridge | Input + Calculation |
| 11 | V3\_CUAS | 36×14 | 204 | Vertical (read-only detail) | Input + Calculation |
| 12 | V4\_UAS\_MALE | 36×14 | 204 | Vertical (read-only detail) | Input + Calculation |
| 13 | V5\_Autonomous | 36×14 | 204 | Vertical (read-only detail) | Input + Calculation |
| 14 | V6\_MilAI | 36×14 | 204 | Vertical (read-only detail) | Input + Calculation |
| 15 | Revenue | 35×14 | 220 | Revenue spine | Calculation Engine |
| 16 | Backlog | 102×13 | 426 | Revenue spine | Calculation Engine |
| 17 | Headcount | 76×14 | 342 | Cost build | Calculation Engine |
| 18 | R&D\_NRE | 19×14 | 111 | Cost build / R&D | Calculation Engine |
| 19 | Capex | 39×14 | 170 | Cost build | Calculation Engine |
| 20 | Opex | 23×14 | 50 | Cost build | Calculation Engine |
| 21 | P&L | 43×13 | 328 | Three-statement | Output/Reporting |
| 22 | CashFlow | 35×13 | 250 | Three-statement | Output/Reporting |
| 23 | BalanceSheet | 40×13 | 280 | Three-statement | Output/Reporting |
| 24 | Funding | 28×14 | 109 | Funding / capital | Calculation + Output |
| 25 | BreakEven | 40×7 | 55 | Output / Valuation | Output/Reporting |


**End-to-end trace (one line):** `Assumptions + Platform/ReuseMatrix + V1–V6` → `Backlog` (order book) → `Revenue` (recognised deliveries + COGS rescale) → `P&L` (with Headcount/Capex/Opex/R&D\_NRE costs) → `CashFlow` + `BalanceSheet` (fed also by `Funding`) → `KPIs` + `BreakEven` (dashboard, IRR/NPV, terminal value).

*Generated by structural + strategic audit of `Defense\\\_Platform\\\_Business\\\_Plan\\\_Financial\\\_V2.xlsx` (26 sheets, ~4,723 formulas, 0 errors) against the `investor\\\_plan/` artifacts. All formulas and values quoted verbatim from the live workbook.*

