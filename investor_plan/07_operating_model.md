# 07. Operating Model

*Nitrodynamics Investor Plan - Section 7*
*Date: 2026-05-17*

## A. Organisational Philosophy

Nitrodynamics is organised as a software firm that happens to ship defense-grade hardware. The operating model is engineered to deliver the single core USP described in source section 4: one engineering organisation, five reusable modules (M1-M5), six product lines (V1-V6), four domains.

The structural choice is **product squads inside a platform-engineering matrix**, not legacy programme directorates. Legacy primes assign each programme a self-contained engineering team that re-solves radio, signal-processing, systems-engineering and software problems from scratch on a 5-7 year cycle. Nitrodynamics instead runs:

- A **Platform Engineering function** (VP Platform Engineering) that owns the five reusable modules - M1 Radio/Microwave, M2 Signal Processing, M3 Systems Engineering, M4 Embedded/Mission Software, M5 AI/ML. Each module has a module lead, a qualification engineer, and a documentation/IP owner. Platform Engineering is the firm's true capital expenditure (source section 6).
- A **Product function** (VP Product) that runs six product squads (V1-V6), each a small cross-functional team owning a product end-to-end on a 12-24 month minimum-viable-product cycle.
- A **Programme Management Office** that interfaces with MoD, allied governments and prime customers, manages bid-and-proposal, contract milestones, and Performance/Advance Bank Guarantees.

The discipline is that product squads do not re-implement what Platform Engineering already qualifies. A product squad consuming an M1 transmit/receive module accepts the qualified building block as-is and contributes back only product-specific integration and enhancements that are themselves promoted back into the platform after qualification. This is the mechanism that converts the 25-60% Year-1 reuse strength into the 97-99% reuse strength by Year 10 (source section 6).

**Concurrent development and production** is non-negotiable. The ESM line (V2) is industrialising and shipping into the Rs.105 Cr opening backlog in Year 1 while AESA (V1) and Counter-drone (V3) squads are in qualification and the MALE (V4) squad is in research. We do not gate one product behind another. The cash from V2 and V6 funds the rest, consistent with source section 10.

## B. Organisation Chart

### B.1 Year-2 organisation chart (~156 headcount)

Reference: `[Diagram 8: Operating Model Org]`

```
                            Board of Directors
                                   |
                                  CEO
                                   |
   +---------------+---------------+---------------+----------------+----------------+
   |               |               |               |                |                |
  CTO /         COO / VP        CFO          CCO / VP Sales      GC / Export      Chief of
  Chief         Manufacturing   |            and Capture         Compliance       Staff /
  Engineer      |               |            |                   |                PMO
  |             |               |            |                   |                |
  +-VP Platform |+-Production   +-FP&A       +-Capture leads     +-Export-control +-Programme
  | Engineering ||  Engineering |+-Treasury  |  (MoD, Navy, Air, |  officer (ITAR/|  managers
  | |           ||+-Quality (AS |  / BG desk |   Army, Exports)  |  EAR/SCOMET)   |  by product
  | +-M1 Radio  || 9100, CMMI)  |+-Controller+-Bid and Proposal  +-Contracts /    |
  | +-M2 DSP    |+-Supply Chain |+-Tax /     +-Customer Success  |  legal counsel +-Security
  | +-M3 SysEng |+-Contract Mfg ||  Statutory|  (field reps      +-IP / patent    |  /
  | +-M4 Embed  ||  partnerships||           |  embedded in      |  counsel       |  classified
  | +-M5 AI/ML  ||              ||           |  squads)          |                |  programmes
  |             ||              ||           |                   |                |  firewall
  +-VP Product  ||              ||           |                   |                |
    +-V2 ESM    ||              ||           |                   |                |
    +-V6 Mil AI ||              ||           |                   |                |
    +-V1 AESA   ||              ||           |                   |                |
    +-V3 C-UAS  ||              ||           |                   |                |
    +-V5 AUV/USV||              ||           |                   |                |
    +-V4 MALE   ||              ||           |                   |                |
               ||
               |+-Contract-manufacturing partners (qualified panel; 30-40% of unit
               |  volumes for V1, V3, V5 hardware lines - source section 9.5)
```

In Year 2, the V4 MALE squad is in research, V5 AUV/USV in development, V1 AESA and V3 C-UAS in qualification, and V2 ESM and V6 Military AI in production-and-ship mode. Headcount of ~156 (source section 9.5) is weighted to R&D and platform engineering, with a thin manufacturing footprint absorbed largely through contract-manufacturing partners.

### B.2 Year-10 organisation chart (~543 headcount)

```
                            Board of Directors
                                   |
                                  CEO
                                   |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   |           |           |           |           |           |           |
  CTO /      COO / VP    CFO       CCO / VP    GC / Export   CISO        Chief of
  Chief      Mfg                   Sales,      Compliance    (CMMC L3,   Staff /
  Engineer                         Capture                   ISO 27001)  PMO
  |          |           |         and Export  |             |           |
  |          |           |         |           |             |           |
  +-VP       +-Production+-FP&A    +-MoD       +-Export-      +-Cyber    +-Programme
  | Platform | Engineering         | Capture   | control       defense   | Mgmt
  | Eng      +-Quality   +-Treasury+-Allied    | (ITAR/EAR/   +-Insider   | (MoD,
  | (~80)    | (AS9100,  | / BG    | Exports   | SCOMET, FMS, threat     | exports,
  |          |  CMMI L3) | / cash  | (per      | DCS)         +-Supply-  | classified)
  +-M1 Radio +-Supply    | mgmt    | region)   +-Contracts    | chain    |
  +-M2 DSP   | Chain     +-        +-Customer  | (MoD DAP,    | cyber    +-Security
  +-M3 SysEng+-Owned     | Controll| Success   | offset)      +-AI model | / classified
  +-M4 Embed | facilities+-Tax,    | (field    +-IP / patent  | red-team | programmes
  +-M5 AI/ML | (anechoic | statutor| service,  | (60+         |          | firewall
  |          | / EMI /   | / Ind AS| installed | filings)     |          |
  +-VP       | cleanroom | 38      | base      +-Ethics /     |          |
  | Product  | / SMT /   | R&D     | support)  | Responsible  |          |
  | (~220)   | UAS hangar| capn)   +-Bid /     | Use officer  |          |
  |          | / maritime|         | Proposal  |              |          |
  +-V1 AESA  | test tank)|         |           |              |          |
  +-V2 ESM   +-Contract  |         |           |              |          |
  +-V3 C-UAS | Mfg       |         |           |              |          |
  +-V4 MALE  | panel     |         |           |              |          |
  +-V5 AUV/  | (cleared, |         |           |              |          |
  |   USV    | 30-40%    |         |           |              |          |
  +-V6 Mil AI| absorption|         |           |              |          |
            |  on V1,V3,|
            |  V5)
```

Year-10 headcount of ~543 (source section 9.5) is production-heavy, with manufacturing engineers, production technicians and field service staff scaling fastest. Platform Engineering plateaus in absolute terms because by Year 10 reuse strength is 97-99% and the marginal effort per new variant is integration not net-new module development.

## C. Squad Composition

A typical product squad blends platform-consumer engineering with product-specific domain expertise. **Analyst assumption** on typical squad sizing, calibrated to the 91-to-543 headcount trajectory in source section 9.5:

| Squad | Year 2 size | Year 10 size | Composition notes |
| - | - | - | - |
| V1 AESA Radar | 16-20 | 55-65 | RF engineers (4-6), DSP/FPGA (3-4), systems integration (2-3), embedded SW (2-3), AI/sensor fusion (1-2), production engineering (2-3), product lead (1), customer-success/field rep (1-2) |
| V2 ESM/SIGINT | 18-22 | 55-65 | RF (5-7), DSP (3-4), systems (2-3), embedded SW (2), AI (1-2), production (2-3), product lead (1), field rep (2) |
| V3 Counter-drone | 12-16 | 50-60 | RF (2-3), DSP (2), systems (2), embedded (2), AI fusion (3-4), effector engineering (2-3), production (2-3), product lead (1), field rep (2) |
| V4 MALE UAS | 10-14 (research) | 60-70 | Airframe and avionics (8-10), embedded SW DO-178C (4-5), DO-254 HW (2-3), AI/autonomy (3-4), payload integration (3-4), flight test (3-4), product lead (1), field rep (2) |
| V5 AUV/USV | 8-12 | 35-45 | Mechanical / hull (2-3), embedded SW (2-3), AI/autonomy (3-5), systems (2-3), test (2-3), product lead (1), field rep (1-2) |
| V6 Military AI | 12-16 | 40-50 | AI/ML engineers (6-8), sensor-fusion (3-4), MLOps (2-3), software engineering (3-4), product lead (1), customer-success (2-3) |

Every squad includes a **product lead** (a single accountable owner, comparable to a commercial-tech product manager but with defense domain depth) and at least one **customer-success / field representative** embedded with the squad. The field rep closes the loop between deployed-product behaviour and the next release, replacing the classical "engineering throws over the wall to field service" pattern at legacy primes.

Platform Engineering (M1-M5) sits adjacent and is consumed by squads through qualified-module pull. **Analyst assumption** on Platform Engineering sizing: ~25 engineers in Year 2, plateauing at ~80 by Year 10 across all five modules.

## D. Facilities Footprint

The facilities plan tracks source section 9.6 (Rs.~600 Cr cumulative capex, weighted Y3-Y5) and the asset-light Year 1-2 posture (source section 3 and section 14).

| Facility | Y1-Y2 | Y3 | Y4 | Y5 | Y6-Y10 | Primary product lines served |
| - | - | - | - | - | - | - |
| Anechoic chamber | Rented (partner labs) | Owned (commissioned) | Owned | Owned | Owned, second cell | V1 AESA, V2 ESM, V3 C-UAS |
| EMI/EMC test cell | Rented | Owned (commissioned) | Owned | Owned | Owned | All hardware lines |
| HALT/HASS environmental | Rented | Rented | Owned | Owned | Owned | All hardware lines |
| Cleanroom + SMT line | n/a | Owned (commissioned) | Owned | Owned | Owned, expanded | V1 AESA, V2 ESM, V3 C-UAS |
| GaN packaging (partial in-house) | n/a | Y2 ramp (source section 11) | Owned | Owned | Owned | V1 AESA, V2 ESM |
| FPGA/GPU development labs | Owned (low capex) | Owned | Owned | Owned | Owned, expanded | All lines |
| Outdoor RF range | Rented | Rented | Rented | Owned (partner-shared) | Owned | V1, V2, V3 |
| UAS flight-test hangar | n/a | n/a | Owned (commissioned) | Owned | Owned | V4 MALE |
| Maritime test tank | n/a | n/a | n/a | Owned (commissioned) | Owned | V5 AUV/USV |
| Mission-software dev / cybersecurity SCIF-equivalent | Owned (low capex) | Owned | Owned, expanded | Owned | Owned | V6, all software-led work |

This footprint preserves capital in Years 1-2 (combined gross capex ~Rs.103 Cr per source section 14) and invests in owned infrastructure only after the product mix justifies it. Each owned facility is justified against a specific qualification or production bottleneck observed in the prior 12 months.

## E. Supply Chain and Manufacturing

The supply chain is engineered around two structural realities of Indian defense electronics: (1) single-source exposure on Gallium Nitride (GaN) packaging and high-performance FPGAs, and (2) the cleared-supplier and offset compliance regime.

**Source mitigation timeline.**

- **GaN power amplifiers and packaging.** Year 1-2 single-source on tier-1 international suppliers. Partial in-house GaN packaging capability stood up by Year 2 (source section 11). Second-source qualified by Year 3. Strategic stock buffer of ~6 months on critical GaN dice.
- **FPGAs (Xilinx/AMD, Altera/Intel, Microchip).** Multi-source by design wherever the design tools permit dual targets. Strategic stock buffer of ~9 months on lead FPGA families used in M2 Signal Processing pipelines, reflecting the post-2021 FPGA allocation lessons.
- **RF connectors, cables, passive components.** Multi-source from Day 1; Indian-domestic substitution wherever MoD positive-indigenisation lists require it.
- **Mechanical, structural, hull, airframe.** Indian-domestic by default. Specialised aerospace composites for V4 MALE qualified through 2-3 Indian aerospace tier-2 partners.

**Contract manufacturing.** 30-40% of unit volumes on V1 AESA, V3 Counter-drone and V5 AUV/USV hardware lines are absorbed through a panel of qualified contract manufacturers (source section 9.5). These partners are cleared at the level appropriate to their workscope, audited annually, and held to AS9100 and the relevant MIL-STD environmental tests. The cleared-supplier panel is a controlled list maintained by Supply Chain with sign-off from GC/Export Compliance and CISO.

**Cleared-supplier panel governance.**

- Annual cyber-hygiene audit (CMMC-L3-aligned for suppliers touching controlled data).
- Conflict-minerals declaration on every tier-1 supplier (ESG control).
- Dual-use export classification recorded for every part above a materiality threshold.
- Strategic stock policy reviewed quarterly by the Risk and Compliance committee.

## F. Talent Pipeline

Cleared-engineer scarcity in India is a structural risk (source section 11). Mitigations:

**University partnerships.** Suggested 4-6 anchor institutions (Analyst suggestion):

- IIT Madras (RF, signal processing, control systems)
- IIT Bombay (radio, communications, embedded systems)
- IIT Kanpur (aerospace, control, AI)
- IISc Bengaluru (AI/ML, autonomy, systems engineering)
- IIIT Hyderabad (AI/ML, computer vision, robotics)
- BITS Pilani (electronics, software)

Each partnership operates a mix of: (a) sponsored MTech/PhD theses on platform-relevant problems, (b) summer internship pipelines, (c) endowed lab equipment in exchange for first-look hiring, (d) joint publication and patent rights, (e) a cleared-track onboarding programme that converts interns into Year-1 hires.

**Remote-friendly software roles.** Roles in V6 Military AI, M4 Embedded/Mission Software, MLOps and parts of M2 Signal Processing remain remote-friendly to expand the catchment beyond the cleared-hardware-engineer pool concentrated in Bengaluru, Hyderabad and Pune. Cleared workspaces in those three cities remain mandatory for classified workstreams.

**Retention.** Long-vesting equity (4-year cliff-back-loaded), defense-domain career progression and a deliberate practice of cross-squad rotation through Platform Engineering before product specialisation. Attrition target (Analyst assumption): below 12% annualised in engineering through Y5, against an Indian tech-sector benchmark of 18-22%.

**Cleared-workforce moat.** Section 3 of the source plan names "cleared workforce" as the first item in the defensible moat. Operationally, this means a clearance pipeline (background verification, programme-specific access) that is started 6-9 months before need, an internal clearance-tracking system as part of the Programme Management Office's classified-programme firewall, and a deliberate over-hiring buffer on cleared roles.
