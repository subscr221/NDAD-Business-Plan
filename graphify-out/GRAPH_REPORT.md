# Graph Report - .  (2026-06-28)

## Corpus Check
- Large corpus: 1909 files · ~1,772,805 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 377 nodes · 515 edges · 35 communities (22 shown, 13 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 78 edges (avg confidence: 0.88)
- Token cost: 5,335 input · 3,532 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Financial Returns & Valuation|Financial Returns & Valuation]]
- [[_COMMUNITY_BMAD Config & Business Model|BMAD Config & Business Model]]
- [[_COMMUNITY_Leadership & Org Structure|Leadership & Org Structure]]
- [[_COMMUNITY_Strategic Growth Phases|Strategic Growth Phases]]
- [[_COMMUNITY_Platform Modules & Roadmap|Platform Modules & Roadmap]]
- [[_COMMUNITY_Working Capital & Cash Flow|Working Capital & Cash Flow]]
- [[_COMMUNITY_Competitive Landscape|Competitive Landscape]]
- [[_COMMUNITY_Funding Stack & Debt|Funding Stack & Debt]]
- [[_COMMUNITY_Revenue by Product Line|Revenue by Product Line]]
- [[_COMMUNITY_P&L Waterfall|P&L Waterfall]]
- [[_COMMUNITY_Platform Flywheel Economics|Platform Flywheel Economics]]
- [[_COMMUNITY_Config Resolution Code|Config Resolution Code]]
- [[_COMMUNITY_IRR Sensitivity Analysis|IRR Sensitivity Analysis]]
- [[_COMMUNITY_TOML Config Merging Code|TOML Config Merging Code]]
- [[_COMMUNITY_Global Market Presence|Global Market Presence]]
- [[_COMMUNITY_Financial Model Validation|Financial Model Validation]]
- [[_COMMUNITY_Brand Identity|Brand Identity]]
- [[_COMMUNITY_Growth Metrics Icons|Growth Metrics Icons]]
- [[_COMMUNITY_Settings & Operations Icons|Settings & Operations Icons]]
- [[_COMMUNITY_Decorative Icons|Decorative Icons]]
- [[_COMMUNITY_Innovation Concept Icons|Innovation Concept Icons]]
- [[_COMMUNITY_Performance Icons|Performance Icons]]
- [[_COMMUNITY_Shield Decorative Element|Shield Decorative Element]]
- [[_COMMUNITY_Tools & Document Icons|Tools & Document Icons]]
- [[_COMMUNITY_Flow Indicator|Flow Indicator]]
- [[_COMMUNITY_Decorative Graphic|Decorative Graphic]]
- [[_COMMUNITY_Geographic Shape|Geographic Shape]]
- [[_COMMUNITY_Blank Image|Blank Image]]
- [[_COMMUNITY_Blank Image|Blank Image]]
- [[_COMMUNITY_Blank Image|Blank Image]]
- [[_COMMUNITY_Blank Image|Blank Image]]
- [[_COMMUNITY_Blank Image|Blank Image]]
- [[_COMMUNITY_Blank Image|Blank Image]]
- [[_COMMUNITY_Blank Image|Blank Image]]
- [[_COMMUNITY_Blank Image|Blank Image]]

## God Nodes (most connected - your core abstractions)
1. `Nitrodynamics` - 19 edges
2. `Revenue Build by Product Chart` - 17 edges
3. `10-Year Strategic Roadmap (Gantt)` - 15 edges
4. `Investor Plan: Strategy and Products` - 13 edges
5. `Returns, Valuation and Sensitivity (Section 06)` - 13 edges
6. `Risk Register (Section 08)` - 12 edges
7. `Phase: Ship (Shi)` - 12 edges
8. `Phase: Qualify (Qua)` - 10 edges
9. `EBITDA (46.4%)` - 10 edges
10. `Operating Model (Section 07)` - 9 edges

## Surprising Connections (you probably didn't know these)
- `Investor Plan: Financial Model` --references--> `Defense Platform Business Plan Financial Model V2`  [INFERRED]
  investor_plan/04_financial_model.md → graphify-out/converted/Defense_Platform_Business_Plan_Financial_V2_d91aafe8.md
- `Nitrodynamics Business Plan V4 (Final)` --references--> `Investor Plan: Cover and One-Pager`  [INFERRED]
  graphify-out/converted/Nitrodynamics_Business_Plan_V4_final_cf3bc159.md → investor_plan/00_cover_and_onepager.md
- `Nitrodynamics Business Plan V4 (Final)` --references--> `Investor Plan: Executive Summary`  [INFERRED]
  graphify-out/converted/Nitrodynamics_Business_Plan_V4_final_cf3bc159.md → investor_plan/01_executive_summary.md
- `BMAD Methodology Framework (v6.6.0)` --rationale_for--> `Investor Plan: Executive Summary`  [INFERRED]
  _bmad/_config/manifest.yaml → investor_plan/01_executive_summary.md
- `Investor Plan: Financial Model` --references--> `Backlog-Based Revenue Recognition Engine`  [EXTRACTED]
  investor_plan/04_financial_model.md → Defense_Platform_Workbook_Explanation.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Platform Modules M1-M5 Collectively Underpin Product Verticals V1-V6** — concept_m1_radio_microwave, concept_m2_signal_processing, concept_m3_systems_engineering, concept_m4_embedded_software, concept_m5_ai_ml, concept_v1_aesa_radar, concept_v2_ew_sigint, concept_v3_counter_drone, concept_v4_male_uas, concept_v5_autonomous_maritime, concept_v6_military_ai [EXTRACTED 1.00]
- **Seed + Series A + Series B Rounds Constitute Rs.1,100 Cr Equity Programme** — concept_seed_round, concept_series_a, concept_series_b, converted_nitrodynamics_aerospace_and_defence [EXTRACTED 1.00]
- **Atmanirbhar Bharat + Positive Indigenisation Lists + iDEX Form India Policy Demand Underwrite** — concept_atmanirbhar_bharat, concept_positive_indigenisation_lists, concept_idex_moi, converted_nitrodynamics_aerospace_and_defence [EXTRACTED 1.00]
- **Investment Decision Evidence Triangle: IC Summary, Diligence Checklist, Stress Test** — summaries_ic_summary_onepager, summaries_diligence_audit_checklist, summaries_stress_test_appendix [EXTRACTED 1.00]
- **Risk-Mitigation-Governance Loop: Risk Register, Governance Compliance, Operating Model** — investor_plan_08_risk_register, investor_plan_09_governance_compliance_ip, investor_plan_07_operating_model [INFERRED 0.85]
- **Returns, KPI and Sensitivity Framework: Section 06, Section 10, Stress Test** — investor_plan_06_returns_and_sensitivity, investor_plan_10_kpis_and_appendix, summaries_stress_test_appendix [INFERRED 0.85]

## Communities (35 total, 13 thin omitted)

### Community 0 - "Financial Returns & Valuation"
Cohesion: 0.06
Nodes (56): Returns, Valuation and Sensitivity (Section 06), Comparable Trading Multiples (Anduril, Shield AI, HAL, BEL), Downside Scenario, DSO Risk (180-Day MoD Payment Cycle), Free Cash Flow Build (10-Year), Investor Returns by Round (MoIC/IRR), Project IRR (31.9%), NPV of FCF at WACC (Rs.747 Cr) (+48 more)

### Community 1 - "BMAD Config & Business Model"
Cohesion: 0.05
Nodes (47): BMAD BAUT (Story Automator) Configuration, BMAD BMM Module Configuration, BMAD CIS (Creative Intelligence Suite) Configuration, BMAD Installation Manifest, BMAD Core Module Configuration, BMAD WDS (Web Design System) Configuration, 10-Year Strategic Financial Model, Anduril (Comparable Platform Defense Company) (+39 more)

### Community 2 - "Leadership & Org Structure"
Cohesion: 0.06
Nodes (33): Board of Directors, Capture & Bid, CCO / VP Sales & Capture, CEO, CFO, CM Partner Interface, Contracts, Controllership (+25 more)

### Community 3 - "Strategic Growth Phases"
Cohesion: 0.11
Nodes (23): Phase I - Asset-light Insurgent (Y1-Y2), Phase I Capex Deferred: Y1-Y2 ~Rs.103 Cr, Phase I EBITDA Negative (Investment Phase), Phase I Facilities: Rented Anechoic / EMI Labs, Phase I Gross Margin 51% (Y1), Phase I Headcount: ~91 (Y1) to 156 (Y2), Phase I Shipping: V2 EW, V6 Military AI, Phase II - Productised Scale-up (Y3-Y5) (+15 more)

### Community 4 - "Platform Modules & Roadmap"
Cohesion: 0.29
Nodes (22): 10-Year Strategic Roadmap (Gantt), ESM Systems Airborne, M1 RF (Productised), M2 DSP (Productised), M3 Systems Engineering, M4 Embedded SW, M5 AI / ML, Phase: Development (Dev) (+14 more)

### Community 5 - "Working Capital & Cash Flow"
Cohesion: 0.10
Nodes (22): Bank Guarantee Profile, Bank Guarantee Fee 1.1% per Year on Outstanding, Cash Conversion Cycle Formula (Inventory 90d + DSO 180d - DPO 45d = 225 days), Cash Receipt (Day +300), Customer Advance 15% Paid (Day +5), 15% Customer Advance Offsets Long DSO (Contract Liability), Delivery (Day +120), DSO Wait 180 Days (Day +120 to +300) (+14 more)

### Community 6 - "Competitive Landscape"
Cohesion: 0.13
Nodes (20): AUV Specialist, C-UAS Pure-play, Defense AI Startup, Capability: Autonomous AUV / USV, Capability: Capital Efficiency, Capability: Cost-to-deliver, Capability: Counter-drone Integration, Capability: Electronic Warfare / SIGINT (+12 more)

### Community 7 - "Funding Stack & Debt"
Cohesion: 0.14
Nodes (19): Bank Debt - Rs.20 Cr (Y1), Cumulative Deployable Cash Curve (Rs.Cr), Debt Fully Repaid: Y9, Debt Repayment Schedule Y5-Y9, Debt Repayment Y5: -Rs.36 Cr, Debt Repayment Y6: -Rs.36 Cr, Debt Repayment Y7: -Rs.55 Cr, Debt Repayment Y8: -Rs.65 Cr (+11 more)

### Community 8 - "Revenue by Product Line"
Cohesion: 0.12
Nodes (18): Nitrodynamics Business Plan, Revenue Build by Product Chart, V1 AESA Product Line, V2 EW/SIGINT Product Line, V3 C-UAS Product Line, V4 MALE UAS Product Line, V5 AUV/USV Product Line, V6 Military AI Product Line (+10 more)

### Community 9 - "P&L Waterfall"
Cohesion: 0.25
Nodes (15): Business & Partnerships Expense (3%), COGS (Cost of Goods Sold), Compliance Expense, Depreciation & Amortisation, EBIT, EBITDA (46.4%), General & Administrative Expense (7%), Gross Profit (+7 more)

### Community 10 - "Platform Flywheel Economics"
Cohesion: 0.25
Nodes (14): Gross Margin: 51% (Y1) > 67% (Y10), M1 RF / Microwave (Rs.154 Cr), M2 DSP / Signal Processing (Rs.90 Cr), M3 Systems Engineering (Rs.86 Cr), M4 Embedded SW (Rs.85 Cr), M5 AI / ML (Rs.160 Cr), Platform Flywheel: Five Modules Feed Six Verticals, Reuse Strength: 25-60% (Y1) > 99% (Y10) (+6 more)

### Community 11 - "Config Resolution Code"
Cohesion: 0.27
Nodes (12): Path, deep_merge(), _detect_keyed_merge_field(), extract_key(), find_project_root(), load_toml(), main(), _merge_arrays() (+4 more)

### Community 12 - "IRR Sensitivity Analysis"
Cohesion: 0.38
Nodes (10): Base IRR 31.9%, BoM Floor 80% vs 70%, Customer Advance 0% vs 15%, DSO 240 vs 180 Days, Export Share 0% vs 25% of Y10, Gross Margin +/-300 bps, MALE Certification +18 Months vs On-Time, Project IRR Sensitivity Tornado (Base 31.9%) (+2 more)

### Community 13 - "TOML Config Merging Code"
Cohesion: 0.42
Nodes (8): Path, deep_merge(), _detect_keyed_merge_field(), extract_key(), load_toml(), main(), _merge_arrays(), _merge_by_key()

### Community 14 - "Global Market Presence"
Cohesion: 0.46
Nodes (8): Africa Location Marker, Australia Location Marker, East Asia Location Marker, Global Market Presence, North America Location Marker, Russia Location Marker, South America Location Marker, World Map

### Community 15 - "Financial Model Validation"
Cohesion: 0.25
Nodes (5): method_a_revenue(), method_b_revenue(), Comprehensive re-derivation of the Defense Platform business plan financial mode, Read booking inputs from Backlog rows 20-25 and replicate the        opening-ba, Replicate V-sheet formulas exactly:        BoM_y = max(BoM_y1 * BoM_FLOOR, BoM_

### Community 16 - "Brand Identity"
Cohesion: 0.43
Nodes (7): Aerospace & Defence, Blue Color Scheme, Brand Identity, Dark Grey Color Scheme, Logo Mark - Speed Lines Icon, NitroDynamics, Bold Sans-Serif Typography

### Community 17 - "Growth Metrics Icons"
Cohesion: 0.70
Nodes (5): Bar Chart Visualization, Business Growth, Growth Chart Icon, Performance Metrics, Upward Trend Arrow

### Community 18 - "Settings & Operations Icons"
Cohesion: 0.67
Nodes (3): Gear / Settings Icon, Operations / Processes Concept, Settings / Configuration Concept

### Community 19 - "Decorative Icons"
Cohesion: 0.67
Nodes (3): Chandelier/Crown Icon, Decorative Symbol, Logo Graphic

### Community 20 - "Innovation Concept Icons"
Cohesion: 1.00
Nodes (3): Energy / Lightning Bolt Symbol, Innovation / Idea Concept, Lightbulb Icon

### Community 21 - "Performance Icons"
Cohesion: 0.67
Nodes (3): Business Growth, Financial Performance, Growth Chart Icon

## Ambiguous Edges - Review These
- `Dark Navy Trapezoid Graphic Element` → `Dark Navy Trapezoid Graphic Element`  [AMBIGUOUS]
  unpacked/word/media/image11.png · relation: conceptually_related_to

## Knowledge Gaps
- **133 isolated node(s):** `Defense Platform Workbook Explanation (Converted)`, `BMAD Core Module Configuration`, `BMAD BMM Module Configuration`, `BMAD CIS (Creative Intelligence Suite) Configuration`, `BMAD BAUT (Story Automator) Configuration` (+128 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Dark Navy Trapezoid Graphic Element` and `Dark Navy Trapezoid Graphic Element`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What connects `Return 'code' or 'id' if every table item carries that *same* field.      All`, `Shape-aware array merge. Base + override combined tables may opt into     keyed`, `Recursively merge override into base using structural rules.     - Table + tabl` to the rest of the system?**
  _140 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Financial Returns & Valuation` be split into smaller, more focused modules?**
  _Cohesion score 0.05584415584415584 - nodes in this community are weakly interconnected._
- **Should `BMAD Config & Business Model` be split into smaller, more focused modules?**
  _Cohesion score 0.05272895467160037 - nodes in this community are weakly interconnected._
- **Should `Leadership & Org Structure` be split into smaller, more focused modules?**
  _Cohesion score 0.0625 - nodes in this community are weakly interconnected._
- **Should `Strategic Growth Phases` be split into smaller, more focused modules?**
  _Cohesion score 0.11462450592885376 - nodes in this community are weakly interconnected._
- **Should `Working Capital & Cash Flow` be split into smaller, more focused modules?**
  _Cohesion score 0.1038961038961039 - nodes in this community are weakly interconnected._