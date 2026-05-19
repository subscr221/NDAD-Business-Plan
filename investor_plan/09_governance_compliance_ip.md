# 09. Governance, Compliance and IP

*Nitrodynamics Investor Plan - Section 9*
*Date: 2026-05-17*

## A. Board Composition

The proposed board is sized to balance founder execution authority, investor oversight proportional to capital deployed, and independent defense-sector judgement on programme, technical and compliance matters. Composition evolves through funding rounds:

| Stage | Independent Chair | Founder / Executive Directors | Investor Directors | Independent Directors (defense / government background) | Total |
| - | - | - | - | - | - |
| Post-Seed (Y1) | 1 | 2 | 1 | 1 | 5 |
| Post-Series A (Y2) | 1 | 2 | 2 | 2 | 7 |
| Post-Series B (Y3 onward) | 1 | 2 | 3 | 2 | 8 |

The composition principle is that investor seats track capital materially deployed (one per major round, capped at three), independent directors with defense or government provenance maintain technical and policy credibility, and the Independent Chair is a non-investor non-founder convenor. The aim is a board that is small enough to debate, large enough to staff committees, and weighted to independent judgement on programme and compliance risk.

**Board Committees** (chartered post-Series A, formalised post-Series B):

- **Audit Committee** - majority independent, chaired by an independent director with finance / Big Four background. Oversees external audit, Ind AS compliance (including Ind AS 38 R&D capitalisation per source section 9.3), internal controls, statutory reporting, related-party transactions, and whistleblower mechanism. Meets quarterly.
- **Nomination and Remuneration Committee** - majority independent. Oversees executive compensation, equity grants, succession planning for C-level and module-lead roles, board composition recommendations. Meets at least twice yearly.
- **Risk and Compliance Committee** - chaired by an independent director with defense / government background. Oversees the risk register (section 8), ITAR/EAR, SCOMET, CMMC L3 posture, IP, ESG and Responsible-Use policies, and material legal exposure. Meets quarterly.
- **Programme and Technical Advisory Committee** - chaired by an independent director with defense engineering or operations background. Oversees platform roadmap (M1-M5), product qualification milestones (V1-V6), DO-178C / DO-254 certification pathway for V4, and major NRE commitments above a delegated authority threshold. Meets quarterly with technical deep-dives.

Director independence is tested annually against an explicit policy (no material commercial relationship, no past employment within 3 years, no related-party). The Independent Chair has a casting vote in tied resolutions.

## B. Defense-Sector Compliance Architecture

Compliance is a structural cost of being a defense prime, not an overhead to minimise. The architecture below maps to the standards named in source section 12 and the annual compliance spend in source section 9.3.

### B.1 Quality

- **AS9100 Rev D** - aerospace quality management. Required for any tier-1 or tier-2 position on Indian and allied aerospace programmes. Annual surveillance audits; full recertification triennially.
- **CMMI Level 3** - software development process maturity. Required for credible delivery on classified software workstreams and for export to US/UK FMS-aligned customers.

Combined annual cost: **Rs.8.55 Cr** (source section 9.3).

### B.2 Cybersecurity

- **CMMC Level 3** - US DoD baseline for contractors handling Controlled Unclassified Information. Adopted as the most demanding standard so that FMS-aligned exports are not gated on a separate uplift later (source section 12). Annual cost: **Rs.14.25 Cr** (source section 9.3).
- **ISO/IEC 27001** alignment as the global commercial baseline, harmonised with CMMC controls to avoid duplicated effort.
- Continuous-monitoring tooling (SIEM, EDR, controlled-data DLP) under the CISO from Y2 onward.
- Annual third-party penetration test on production and corporate networks; internal red-team programme by Y3.

### B.3 Hardware Test Standards

The M3 Systems Engineering module owns the test framework that covers every hardware product:

- **MIL-STD-810** - environmental stress (temperature, humidity, vibration, shock, altitude).
- **MIL-STD-461** - electromagnetic interference and electromagnetic compatibility (EMI/EMC).
- **MIL-STD-704** - aircraft electrical power characteristics (applies to V1 airborne variants and V4).
- **MIL-STD-1275** - vehicle electrical power characteristics (applies to V3 vehicle-mounted, V2 land variants).

Equivalent Indian standards (JSS 55555, JSS 50101) are mapped in parallel for MoD acceptance.

### B.4 Airworthiness

- **DO-178C** - software considerations in airborne systems. Applied to V4 MALE mission software and any airborne variant of V1 or V6. Design Assurance Levels are partitioned by function so safety-critical code is contained in a smaller, more rigorously qualified footprint.
- **DO-254** - design assurance for airborne electronic hardware. Applied to V4 FPGA and complex-electronic-hardware items.
- **Type certification** via DGCA (India) for V4, with an early-stage Designated Engineering Representative (DER) plan executed from Y2.

### B.5 Export Control

- **ITAR / EAR baseline.** Every product is assessed at design intake for jurisdiction (ITAR vs EAR) and classification (USML category vs ECCN). The default architecture is ITAR-clean by deliberate design choice on critical paths, with US-origin items either substituted or contained in optional variants.
- **EAR99 variants from Day 1** for V2, V3 and V6 where commercially feasible (source section 11). These are the broadest-export variants and underwrite the allied-government export pipeline.
- **Indian SCOMET classification.** Every export build is mapped to the Special Chemicals, Organisms, Materials, Equipment and Technologies list maintained by the Directorate General of Foreign Trade. Export authorisations are tracked in a single system of record under GC.
- **Offset compliance.** Indian offset obligations on imported-content contracts are tracked by an offset officer within the Capture team; offset commitments are baked into sales-and-marketing budgets (source section 12).

### B.6 Compliance Cost Summary

| Programme | Annual Cost (Rs.Cr) | Source |
| - | - | - |
| AS9100 + CMMI L3 (quality) | 8.55 | Source section 9.3 |
| CMMC L3 (cyber) | 14.25 | Source section 9.3 |
| Export control (baseline) | 2.00 starting | Source section 9.3, rising over time |
| Programme-specific certification (MIL-STD test campaigns, DO-178C/DO-254 evidence packs) | Variable | Allocated to product NRE |

## C. Indian Regulatory Map

The Indian defense regulatory environment is the firm's primary operating context. Key reference points:

- **Defence Acquisition Procedure (DAP 2020 and subsequent amendments).** Governs the MoD procurement cycle. Nitrodynamics is positioned principally under the "Buy (Indian-IDDM)" and "Make-II" categories of DAP, where indigenous design and minimum 50% local content qualify products for preferential procurement.
- **Positive Indigenisation Lists (PILs)** - four lists issued by the Department of Military Affairs (the latest in 2024) name items that must be sourced indigenously after a stated date. The Nitrodynamics product portfolio is deliberately aligned to multiple PIL items (ESM variants, certain radar classes, counter-drone, autonomous maritime).
- **Defence Production and Export Promotion Policy (DPEPP) 2020.** Sets the policy target of USD 25 billion (Rs.~1.75 lakh Crore) defense industry turnover and Rs.50,000 Cr defense exports by 2028-29. This is the macro-policy umbrella under which Nitrodynamics's export ambition operates.
- **iDEX (Innovations for Defence Excellence).** Eligibility for prototype grants and rapid-procurement pathways through the Defence Innovation Organisation. Treated as upside, not base case, per source section 10.
- **TDF (Technology Development Fund).** DRDO-administered grants up to Rs.50 Cr per project for indigenous technology development. Eligible for selected M1/M2/M5 module workstreams. Upside only.
- **Make-II.** Industry-funded indigenous-development pathway with assured MoD procurement on successful prototype. Eligible for several product lines. Upside only.
- **FDI Cap.** Defense FDI is currently capped at 74% under the automatic route and 100% with government approval. The cap-table strategy preserves Indian-resident majority in the base plan, with headroom for non-resident strategic investors within policy limits.
- **Industrial Licensing.** Defense industrial licence under the Industries (Development and Regulation) Act, with associated security clearances for premises, key managerial personnel and shareholding above thresholds.

The DGFT, DGAQA (Directorate General of Aeronautical Quality Assurance), DGQA (Directorate General of Quality Assurance) and CEMILAC (Centre for Military Airworthiness and Certification) are the operating-level Indian counterparts engaged programme by programme.

## D. IP and Data Rights Strategy

The IP strategy operationalises the moat stack named in source section 3: "cleared workforce, retained data rights, IP-led licensing".

**Government-Purpose Rights as default.** Per source section 12, the default contracting position is Government-Purpose Rights (GPR): the customer (typically the Indian MoD) receives unrestricted rights to use the IP for governmental purposes, while commercial-market rights remain with Nitrodynamics. This is the same posture that has produced durable IP-led franchises at US primes (for example, the legacy of GPR positions taken by L3Harris and Northrop Grumman on EW systems).

**Unlimited Rights priced separately.** Where a customer requires Unlimited Rights (the right to compete the future manufacture or modification of the IP), this is negotiated as a separate line item with a deliberate uplift in contract price. The uplift is benchmarked against the foregone option value of future programme revenue.

**Platform IP retained across all programmes.** The five reusable modules (M1-M5) are platform-level IP whose ownership is retained by Nitrodynamics regardless of the product (V1-V6) in which they are embedded. Contract clauses isolate platform IP from product-specific custom work so a programme-level GPR or Unlimited Rights grant does not bleed into the platform stack.

**Patent strategy** - Analyst target: by Y5 a portfolio of 60-80 patent filings across the five modules and six products, with priority filings in India, the United States, the European Patent Office, and selected allied jurisdictions (Israel, UAE, Australia, UK). Patents are used principally for defensive purposes (freedom to operate, exclusion of copy-cat suppliers) and for cross-licensing leverage with global tier-1 primes.

**Trade-secret protection.** AI model weights, training data, FPGA bitstream firmware, and proprietary calibration data are treated as trade secrets rather than patents because publication via the patent route would erode the moat. Trade-secret controls:

- Identification register of trade-secret assets per module, owned by the IP counsel within GC.
- Access on need-to-know within the classified-programme firewall.
- Departing-employee processes including exit interviews, return-of-materials, and post-employment restrictive covenants where enforceable.
- Watermarking and code-fingerprinting on AI weights to enable forensic provenance in disputes.

**Cleared workforce as the third leg of the moat.** The combination of GPR-default contracting, platform IP retention and a cleared workforce that cannot trivially move between defense employers produces a structurally durable competitive position even where individual patents lapse or are invented around.

## E. ESG and Responsible-Use Posture

Defense companies face heightened ESG scrutiny on the use of force, end-user diversion, and supply-chain provenance. Nitrodynamics's posture is published, audited and reflected at board level through the Risk and Compliance Committee.

- **Lethal-autonomy guardrails.** Hard-kill effectors (V3 CUAS-B / CUAS-C hard-kill variants, V4 strike, V5 anti-submarine AUV) operate strictly with **human on the loop** for lethal engagement decisions by design. The mission-computer architecture (M4) records an immutable audit trail of operator decisions on lethal action.
- **End-user policy.** No sales to end-users on the MEA (Ministry of External Affairs) restricted-country list. End-user certifications are mandatory on every export build, with post-shipment verification protocols.
- **AI-decision audit trail.** Every AI-assisted recommendation in V6 sensor-fusion and autonomy decisions is logged with model version, training-data fingerprint and operator override, satisfying both internal Responsible-Use review and customer audit requests.
- **Supply-chain conflict minerals.** Annual conflict-minerals declaration on every tier-1 supplier, with escalation on red-flag findings.
- **Environmental compliance** on owned facilities (cleanroom, SMT, GaN packaging) under Indian environmental law and ISO 14001 alignment from Y4.
- **Responsible-Use Officer** within GC from Y5, reporting jointly to GC and to the Risk and Compliance Committee.

## F. Internal Controls and Reporting

The internal control system is COSO-aligned and tailored to defense-programme realities.

**Cadence of management review.**

- **Monthly Programme Reviews.** Each product squad (V1-V6) and each platform module (M1-M5) reports earned-value, qualification milestone status, supplier health, top risks and BG / cash exposure. Chaired by CEO with CTO, COO, CFO present.
- **Monthly Executive Risk Forum.** Top-quartile residual risks (section 8) reviewed; cross-functional mitigations tracked to closure.
- **Monthly Liquidity Review.** CFO with Treasury - BG outstanding, restricted cash, working capital, debt service, FX cover position.
- **Quarterly Audit Committee.** External audit, financial controls, Ind AS compliance (including Ind AS 38 R&D capitalisation), related-party, whistleblower.
- **Quarterly Risk and Compliance Committee.** ITAR/EAR, SCOMET, CMMC L3, IP, ESG, Responsible Use.
- **Quarterly Programme and Technical Advisory Committee.** Platform roadmap, V4 certification pathway, NRE above delegated authority.

**Specific control mechanisms.**

- **BG and PBG tracking.** Single system of record for all bank guarantees (Performance and Advance), with weekly reconciliation to the issuing-bank confirmations and monthly to the balance sheet. Collateral schedule tracked against source section 9.4 (100% Y1-Y2, declining to 20% Y5+).
- **Classified-programme firewall.** Physical, logical and personnel separation between classified and unclassified workstreams. Access lists owned by the Chief of Staff / PMO with quarterly attestation.
- **Delegated authority matrix.** Spend, contract, hiring and equity authorities delegated from board to CEO and onward with explicit thresholds. NRE commitments above a board-defined threshold escalate to the Programme and Technical Advisory Committee.
- **Whistleblower channel.** Independent third-party-administered channel reporting to the Audit Committee Chair.
- **Internal Audit.** Stood up by Y3, reporting administratively to CFO and functionally to the Audit Committee. Annual rolling-three-year internal audit plan covering programme, financial, compliance and cyber controls.

The reporting data lineage runs from programme systems (earned value, supplier, quality, qualification) through finance (general ledger, Ind AS) to board packs, with auditable mapping at every step. This lineage is itself subject to internal audit review at least biennially.
