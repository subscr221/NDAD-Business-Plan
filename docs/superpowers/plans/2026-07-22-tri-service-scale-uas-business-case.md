# Tri-service SCALE UAS business case implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a fully researched, humanized investor business case for one common SCALE UAS platform serving Indian Navy, Army, and Air Force requirements, with focused Indo-Pacific and Gulf export evidence and rebuilt financials.

**Architecture:** Build a claim-level evidence ledger first, using separate research passes for each Indian service, export markets, technology, qualification, and transactions. Use the ledger to write a new document from a tri-service outline rather than extending the coastal draft. Recalculate the illustrative scenario from disclosed assumptions, then run source, arithmetic, service-balance, and anti-AI fidelity audits.

**Tech Stack:** Markdown, public primary and attributable secondary sources, Python 3 standard library for arithmetic checks, ripgrep for document audits, and Git for isolated documentation commits.

## Global constraints

- Anchor market: India.
- Export comparison: selected Indo-Pacific and Gulf states.
- Product framing: one common SCALE platform with modular Navy, Army, and Air Force mission packages.
- Rebuild demand, pricing, order cadence, risks, and the illustrative ten-year scenario around tri-service sales.
- Create `_bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md`.
- Leave all existing business-case drafts unchanged.
- Keep the case company-agnostic and written for defence-literate lead investors and generalist co-investors.
- Distinguish signed contracts, approved requirements, tenders, reported plans, estimates, and internal assumptions.
- Lead with official and primary sources; corroborate, downgrade, or remove claims supported only by low-transparency aggregators.
- Do not infer non-public operational information or unsupported service allocations.
- Humanize the final prose without altering facts, figures, caveats, or source meaning.

---

### Task 1: Build the baseline claim audit and evidence ledger

**Files:**
- Read: `_bmad-output/business-case-scale-uas-investor.REWRITE-DRAFT-3P.md`
- Read: `_bmad-output/business-case-scale-uas-investor.md`
- Read: `business-cases/business-case-male-uas.md`
- Create: `_bmad-output/research/scale-uas-tri-service-evidence-ledger.md`

**Produces:** A structured ledger with fields for claim ID, service, claim, claim status, source type, source title, publisher, publication date, URL, access date, and drafting note.

- [ ] **Step 1: Create the ledger structure**

Add sections for:

1. Cross-service procurement and allocations.
2. Indian Army missions and programmes.
3. Indian Air Force missions and programmes.
4. Indian Navy missions and programmes.
5. Common-platform architecture and qualification.
6. Indian transactions and pricing.
7. Indo-Pacific export markets.
8. Gulf export markets.
9. Competition and substitutes.
10. Financial assumptions.
11. Claims removed or unresolved.

Use one bullet per claim with this exact field order:

```markdown
- Claim ID:
  - Service:
  - Claim:
  - Status: confirmed | reported | estimate | assumption | rejected
  - Source type: primary | secondary | analyst
  - Source:
  - Publisher:
  - Published:
  - URL:
  - Accessed: 2026-07-22
  - Drafting note:
```

- [ ] **Step 2: Audit the current draft claim by claim**

Capture every procurement quantity, price, delivery date, performance figure, loss claim, market estimate, service allocation, sustainment percentage, qualification duration, and operational assertion. Mark each item `confirmed` only if the existing citation directly supports it; otherwise mark it `reported`, `estimate`, `assumption`, or `rejected`.

- [ ] **Step 3: Record structural gaps**

Under `Claims removed or unresolved`, record that the existing case:

- opens with coastline and exclusive economic zone;
- uses maritime physics as its principal substitution argument;
- treats navies as the natural first export customers;
- gives no service-specific Army or Air Force demand model;
- does not test whether one platform can meet all three services without commonality erosion.

- [ ] **Step 4: Verify the audit is complete**

Run:

```powershell
rg -n "₹|USD|%|aircraft|platform|hours|kilomet|delivery|tender|contract|requirement|projection" _bmad-output/business-case-scale-uas-investor.REWRITE-DRAFT-3P.md
```

Expected: every material match is represented in the ledger or explicitly excluded as a definition, heading, or repeated summary.

- [ ] **Step 5: Commit the baseline ledger**

```powershell
git add -- _bmad-output/research/scale-uas-tri-service-evidence-ledger.md
git commit -m "docs: audit SCALE UAS evidence baseline"
```

### Task 2: Research Indian cross-service procurement and Army requirements

**Files:**
- Modify: `_bmad-output/research/scale-uas-tri-service-evidence-ledger.md`

**Consumes:** The evidence-ledger format from Task 1.

**Produces:** Corroborated Indian cross-service transaction evidence and an Army mission case that distinguishes strategic MALE tasks from tactical-UAS tasks.

- [ ] **Step 1: Research official cross-service demand**

Search Indian Ministry of Defence, PIB, Parliament, service publications, and official US material for:

- the 31-aircraft MQ-9B contract and the 15 Navy / 8 Army / 8 Air Force allocation;
- contract scope, weapons and support scope, local sustainment, delivery timing, and approval history;
- any reliable public documentation for the 87-aircraft indigenous programme, its procurement category, content rules, award structure, and service allocation;
- public statements that separate approved requirements from long-range projections.

Record direct quotations only when they clarify procurement status. Paraphrase routine facts.

- [ ] **Step 2: Research Army operating requirements**

Collect evidence for:

- northern and western border persistence;
- high-altitude and desert operating constraints;
- artillery target acquisition and battle-damage assessment;
- communications relay across terrain;
- SIGINT/ELINT and electronic-support missions;
- control of launched effects and tactical-drone formations;
- current Army Heron, Drishti-10, TAPAS/Archer-NG, or comparable usage and procurement where publicly documented.

- [ ] **Step 3: Test the mission boundary**

For each Army mission, add a ledger note naming the closest substitute:

- tactical UAS;
- satellite;
- aerostat;
- crewed ISR aircraft;
- ground sensor;
- HAPS;
- attritable drone.

State why a SCALE aircraft wins, loses, or complements that substitute. Reject convoy or local base overwatch as a core SCALE mission unless range, endurance, payload, or command-role evidence justifies the class.

- [ ] **Step 4: Check source quality**

Run:

```powershell
rg -n "Status: confirmed|Status: reported|Source type:" _bmad-output/research/scale-uas-tri-service-evidence-ledger.md
```

Expected: every new Army and cross-service claim has both a status and source type; no central demand claim relies only on an analyst or aggregator.

- [ ] **Step 5: Commit Army and cross-service research**

```powershell
git add -- _bmad-output/research/scale-uas-tri-service-evidence-ledger.md
git commit -m "docs: research Army SCALE UAS requirements"
```

### Task 3: Research Indian Air Force requirements and operational limits

**Files:**
- Modify: `_bmad-output/research/scale-uas-tri-service-evidence-ledger.md`

**Consumes:** The evidence-ledger format and cross-service procurement facts.

**Produces:** An Air Force mission case with explicit survivability and substitution limits.

- [ ] **Step 1: Research Air Force demand**

Use Indian Air Force, Ministry of Defence, PIB, Parliament, DRDO, CEMILAC, and attributable specialist sources to document:

- persistent standoff ISR and ELINT;
- tactical-data and communications relay;
- strike-package coordination;
- unmanned teaming and launched effects;
- surveillance support to theatre and air-base defence;
- Air Force use or procurement of Heron, MQ-9B SkyGuardian, TAPAS/Archer-NG, or other relevant systems.

- [ ] **Step 2: Research adjacent systems**

Document where AEW&C, crewed ISR, fighter reconnaissance, satellites, HAPS, and combat collaborative aircraft outperform or complement SCALE. Include sensor altitude, survivability, crew, persistence, and command-authority differences only when supported.

- [ ] **Step 3: Write explicit red lines into the ledger**

Add rejected claims for:

- replacing AEW&C;
- routine penetration of dense integrated air defences;
- replacing fast survivable reconnaissance;
- autonomous lethal action without human authorization;
- treating battle-management support as equivalent to full air-battle management.

- [ ] **Step 4: Verify operational qualifiers**

Run:

```powershell
rg -n "AEW|penetrat|surviv|permissive|standoff|battle.management|human" _bmad-output/research/scale-uas-tri-service-evidence-ledger.md
```

Expected: Air Force claims consistently state the operating condition and do not overstate survivability or command role.

- [ ] **Step 5: Commit Air Force research**

```powershell
git add -- _bmad-output/research/scale-uas-tri-service-evidence-ledger.md
git commit -m "docs: research Air Force SCALE UAS requirements"
```

### Task 4: Refresh Navy evidence and define the common platform

**Files:**
- Modify: `_bmad-output/research/scale-uas-tri-service-evidence-ledger.md`
- Read: `business-cases/business-case-aesa-radar.md`
- Read: `business-cases/business-case-ew-sigint.md`
- Read: `business-cases/business-case-military-ai.md`

**Produces:** Updated maritime evidence and a claim-tested common-platform architecture.

- [ ] **Step 1: Refresh the maritime demand evidence**

Verify coastline and exclusive-economic-zone figures, MQ-9B SeaGuardian allocation, Drishti-10 procurement, current maritime-UAS use, delivery timing, and documented maritime mission requirements. Separate surface-search evidence from unsupported ASW claims.

- [ ] **Step 2: Define the common technical core**

Add evidence-backed notes for:

- airframe, propulsion, flight controls, power, and endurance;
- satellite and line-of-sight communications;
- mission computer, ground-control system, autonomy, and sensor fusion;
- open payload interfaces and configuration control;
- military airworthiness and software/hardware assurance;
- training, support, mission-data updates, and upgrades.

- [ ] **Step 3: Define service-specific mission packages**

Record which hardware and software change for:

- maritime surface search and communications;
- Army land surveillance, relay, and SIGINT;
- Air Force standoff ISR, ELINT, and coordination.

Identify each change that may require new flight test, electromagnetic-compatibility work, software assurance, weapon clearance, or customer integration.

- [ ] **Step 4: Calculate a commonality test**

Use three labels in the ledger:

- `shared without requalification`;
- `shared with incremental qualification`;
- `service-specific`.

Expected: the common-platform claim is supported at subsystem level and does not imply that every payload can move between services without cost.

- [ ] **Step 5: Commit maritime and platform research**

```powershell
git add -- _bmad-output/research/scale-uas-tri-service-evidence-ledger.md
git commit -m "docs: define tri-service SCALE platform commonality"
```

### Task 5: Research focused Indo-Pacific and Gulf export comparators

**Files:**
- Modify: `_bmad-output/research/scale-uas-tri-service-evidence-ledger.md`

**Produces:** A small country set in which every market contributes a documented procurement, mission, localisation, pricing, or access lesson.

- [ ] **Step 1: Screen candidate markets**

Screen Australia, Indonesia, Philippines, Japan, Vietnam, Saudi Arabia, United Arab Emirates, Oman, and Qatar against:

- documented MALE-class procurement or requirement;
- land-border, maritime, or air-force mission fit;
- incumbent platform and supplier relationship;
- local-content or industrial-participation policy;
- export-control and diplomatic feasibility for an Indian supplier;
- accessible transaction or programme evidence.

- [ ] **Step 2: Select four to six comparators**

Keep only markets with at least one primary source and one concrete lesson. Do not include a country merely to enlarge the addressable market.

- [ ] **Step 3: Capture transaction scope**

For each selected country, record whether reported values include aircraft, ground stations, weapons, training, infrastructure, sustainment, local production, or technology transfer. Do not compare unadjusted package totals as aircraft unit prices.

- [ ] **Step 4: Derive the export sequence**

Use the evidence to assess:

1. domestic Indian reference;
2. first export into a permissive or standoff ISR mission;
3. local support or assembly;
4. payload and software upgrades;
5. later mission-package expansion.

- [ ] **Step 5: Commit export research**

```powershell
git add -- _bmad-output/research/scale-uas-tri-service-evidence-ledger.md
git commit -m "docs: research SCALE UAS export comparators"
```

### Task 6: Rebuild transaction anchors, demand wedges, and financial scenario

**Files:**
- Modify: `_bmad-output/research/scale-uas-tri-service-evidence-ledger.md`
- Create: `_bmad-output/research/scale-uas-tri-service-financial-check.py`

**Produces:** Disclosed demand and pricing assumptions plus reproducible ten-year bookings, deliveries, revenue, backlog, and support calculations.

- [ ] **Step 1: Define evidence classes**

Create four demand categories in the ledger:

- `contracted`;
- `approved or tendered`;
- `reported requirement`;
- `illustrative entrant capture`.

Never sum the first three into one market total without identifying overlap.

- [ ] **Step 2: Define the base scenario**

Use only transaction-supported price ranges. Set separate disclosed assumptions for:

- baseline aircraft and ground-system package;
- Navy mission-package increment;
- Army mission-package increment;
- Air Force mission-package increment;
- annual sustainment and software rate;
- domestic order timing;
- export order timing;
- delivery ramp;
- qualification slip sensitivity.

If evidence does not support a distinct service price, use one common package range and state that service mix affects payload cost rather than catalogue price.

- [ ] **Step 3: Write the arithmetic checker**

Create a standard-library Python script containing:

```python
YEARS = tuple(range(1, 11))

def calculate_scenario(
    orders: tuple[int, ...],
    deliveries: tuple[int, ...],
    aircraft_price_cr: float,
    support_rate: float,
) -> list[dict[str, float]]:
    backlog_units = 0
    fleet_units = 0
    rows: list[dict[str, float]] = []
    for year, ordered, delivered in zip(YEARS, orders, deliveries, strict=True):
        opening_fleet = fleet_units
        backlog_units += ordered - delivered
        fleet_units += delivered
        aircraft_revenue = delivered * aircraft_price_cr
        support_revenue = opening_fleet * aircraft_price_cr * support_rate
        rows.append(
            {
                "year": year,
                "ordered": ordered,
                "delivered": delivered,
                "fleet": fleet_units,
                "backlog_units": backlog_units,
                "aircraft_revenue_cr": aircraft_revenue,
                "support_revenue_cr": support_revenue,
                "total_revenue_cr": aircraft_revenue + support_revenue,
            }
        )
    return rows
```

Add assertions that tuple lengths equal ten, cumulative deliveries never exceed cumulative orders, backlog never becomes negative, and each total equals aircraft plus support revenue.

- [ ] **Step 4: Run base and downside cases**

Run:

```powershell
python _bmad-output/research/scale-uas-tri-service-financial-check.py
```

Expected: the script prints base and twelve-month-slip tables and exits with code 0 after all assertions pass.

- [ ] **Step 5: Record assumptions and outputs**

Copy exact inputs and outputs into the ledger. Label them `assumption`, not `confirmed`. Explain how the scenario relates to a plausible Indian award or follow-on path without claiming a market share already won.

- [ ] **Step 6: Commit the financial model**

```powershell
git add -- _bmad-output/research/scale-uas-tri-service-evidence-ledger.md _bmad-output/research/scale-uas-tri-service-financial-check.py
git commit -m "docs: rebuild SCALE UAS financial scenario"
```

### Task 7: Draft the new tri-service business case

**Files:**
- Create: `_bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md`
- Read: `_bmad-output/research/scale-uas-tri-service-evidence-ledger.md`
- Read: `_bmad-output/research/scale-uas-tri-service-financial-check.py`

**Produces:** A complete investor case whose thesis, demand proof, economics, risks, and diligence criteria are tri-service.

- [ ] **Step 1: Write the executive summary**

Open with the funded tri-service requirement and explain the common-platform thesis. State the principal limitation: the aircraft operates in permissive or standoff conditions and does not replace penetrating or AEW&C platforms.

- [ ] **Step 2: Write the mission and architecture sections**

Draft:

1. why the requirement is tri-service;
2. class definition;
3. Army mission case;
4. Air Force mission case;
5. Navy mission case;
6. common core and mission packages.

Each service section must include the operational problem, suited missions, unsuitable missions, substitutes, procurement evidence, and investor implication.

- [ ] **Step 3: Write market and competition sections**

Draft Indian demand by evidence class, transaction anchors, selected export comparators, incumbent platforms, substitute systems, qualification gates, and platform-owner economics.

- [ ] **Step 4: Write financial and go-to-market sections**

Insert the arithmetic-checked ten-year scenario, assumptions, base/downside sensitivities, domestic-to-export sequence, and recurring-revenue treatment.

- [ ] **Step 5: Write risks, falsifiers, and diligence**

Cover:

- qualification slip;
- tender or anchor-order loss;
- commonality erosion;
- price compression;
- service-specific integration cost;
- import and export-control exposure;
- survivability limits;
- substitution by tactical drones, satellites, aerostats, HAPS, or crewed systems;
- export delay.

Every falsifier must include an observable trigger rather than a generic warning.

- [ ] **Step 6: Add glossary and annotated sources**

For each source, state which claim group it supports. Include publication and verification dates. Do not cite the evidence ledger as the ultimate source.

- [ ] **Step 7: Check tri-service balance**

Run:

```powershell
rg -c -i "Army|land force|border|artillery" _bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md
rg -c -i "Air Force|IAF|air battle|AEW|ELINT" _bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md
rg -c -i "Navy|naval|maritime|ocean|coast" _bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md
```

Expected: each service appears throughout the executive summary, mission case, demand, economics, risks, and diligence sections. Counts are diagnostic only; revise based on substantive coverage, not numerical equality.

- [ ] **Step 8: Commit the sourced first draft**

```powershell
git add -- _bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md
git commit -m "docs: draft tri-service SCALE UAS investor case"
```

### Task 8: Humanize the prose and preserve fidelity

**Files:**
- Modify: `_bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md`
- Read: `_bmad-output/research/scale-uas-tri-service-evidence-ledger.md`

**Produces:** Natural investor prose without AI-writing patterns or factual drift.

- [ ] **Step 1: Run the first anti-AI audit**

Search for:

```powershell
rg -n -i "pivotal|crucial|vital|landscape|showcas|underscore|testament|game.changer|at its core|the real question|not just|not only|in order to|it is important to note|moving forward|future looks|challenges and" _bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md
```

Expected: inspect every match and retain only technically necessary uses.

- [ ] **Step 2: Rewrite for natural rhythm**

Remove promotional claims, repetitive rules of three, false contrasts, rhetorical questions, sentence fragments used for drama, excessive em dashes, generic positive conclusions, and paragraph openings that restate headings. Preserve technical terminology where precision requires it.

- [ ] **Step 3: Run the humanizer self-question**

Answer in working notes:

> What makes the draft still sound obviously AI-generated?

Check for uniform paragraph length, mechanical service symmetry, overly tidy transitions, slogan-like conclusions, and suspiciously polished claims unsupported by the ledger. Revise those passages.

- [ ] **Step 4: Perform paragraph-level fidelity checks**

For every paragraph containing a number, procurement status, operational event, programme name, or performance claim:

1. locate its ledger entry;
2. confirm status and qualifier survived the rewrite;
3. confirm no new claim was added;
4. confirm the source still supports the final wording.

- [ ] **Step 5: Commit the humanized draft**

```powershell
git add -- _bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md
git commit -m "docs: humanize tri-service SCALE UAS case"
```

### Task 9: Verify sources, arithmetic, structure, and repository scope

**Files:**
- Verify: `_bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md`
- Verify: `_bmad-output/research/scale-uas-tri-service-evidence-ledger.md`
- Verify: `_bmad-output/research/scale-uas-tri-service-financial-check.py`

**Produces:** A clean final document with documented unresolved evidence gaps and no accidental edits to prior drafts.

- [ ] **Step 1: Re-run financial verification**

Run:

```powershell
python _bmad-output/research/scale-uas-tri-service-financial-check.py
```

Expected: exit code 0; printed totals match the final document.

- [ ] **Step 2: Scan unsupported certainty**

Run:

```powershell
rg -n -i "will buy|will award|guarantees|proves|settles demand|winner|market share|service allocation" _bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md
```

Expected: each match is either directly sourced, explicitly conditional, or rewritten.

- [ ] **Step 3: Scan placeholders and citation gaps**

Run:

```powershell
rg -n -i "TBD|TODO|citation needed|source needed|placeholder|example\.com|\[\]|\(\)" _bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md _bmad-output/research/scale-uas-tri-service-evidence-ledger.md
```

Expected: no unresolved placeholders. Any genuine evidence gap appears in a labelled limitations note, not as drafting residue.

- [ ] **Step 4: Validate Markdown and whitespace**

Run:

```powershell
git diff --check
```

Expected: no whitespace errors.

- [ ] **Step 5: Confirm prior drafts are untouched by this work**

Run:

```powershell
git status --short
git diff --name-only HEAD~5..HEAD
```

Expected: implementation commits contain only the new tri-service document, evidence ledger, arithmetic checker, and approved planning documents. Pre-existing user changes to older drafts remain unstaged and uncommitted.

- [ ] **Step 6: Final source spot-check**

Randomly select at least ten material claims across all three services, exports, pricing, and qualification. Open each cited source and verify that the final wording does not exceed the source.

- [ ] **Step 7: Commit verification corrections**

If verification required edits:

```powershell
git add -- _bmad-output/business-case-scale-uas-investor.TRI-SERVICE-REWRITE.md _bmad-output/research/scale-uas-tri-service-evidence-ledger.md _bmad-output/research/scale-uas-tri-service-financial-check.py
git commit -m "docs: verify tri-service SCALE UAS case"
```

If no correction was required, do not create an empty commit.
