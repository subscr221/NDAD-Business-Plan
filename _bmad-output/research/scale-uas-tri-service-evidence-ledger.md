<!-- markdownlint-disable MD029 MD034 -->

# SCALE UAS tri-service evidence ledger

## Purpose and scope note

This ledger audits every material claim in the task-specified 3P source draft.
For reproducibility, the exact audited bytes are committed at
`_bmad-output/research/source-snapshots/business-case-scale-uas-investor.REWRITE-DRAFT-3P.INPUT-SNAPSHOT.md`.

Snapshot provenance:

- Parent input:
  `d:\WINCODE\NDAD-Business-Plan\NDAD-Business-Plan\_bmad-output\business-case-scale-uas-investor.REWRITE-DRAFT-3P.md`
- Snapshot created: 2026-07-22
- Copy method: byte-for-byte file copy; parent input left unchanged
- Parent SHA-256:
  `504D6148D3C55C0B636B4C15331DBC07F6C69479C35B5612CF0E3A6FCD9E34E9`
- Snapshot SHA-256:
  `504D6148D3C55C0B636B4C15331DBC07F6C69479C35B5612CF0E3A6FCD9E34E9`
- Hash comparison: identical

The ledger also compares the committed main draft
(`_bmad-output/business-case-scale-uas-investor.md`) and a small set of
overlapping claims in `business-cases/business-case-male-uas.md`.

**Source-quality finding:** the 3P draft adds an appendix with nine grouped
source notes and several URLs, while the committed main draft contains no
inline citations, URLs, publisher names, or publication dates. The 3P
appendix materially improves traceability, but most notes bundle several
claims and publishers without mapping each claim to a specific article,
quotation, publication date, or primary record. Claims are therefore marked
`reported` unless the draft itself discloses arithmetic that can be checked
directly. No appendix claim is promoted to `confirmed` merely because a URL is
present.

Claim IDs are unique (`C001`, `C002`, ...) across the whole ledger; file order
follows the required subject sections rather than strict numeric order.
"Source" records what the draft itself says about provenance, verbatim or
closely paraphrased, not an externally verified citation. Where the draft
gives nothing at all, Source/Publisher/Published/URL are marked "Not stated
in draft." No URL, publisher, or date has been invented for this ledger.

**Explicit exclusions from claim-by-claim coverage (Step 4 categories):** the
following recur throughout the drafts and are not logged as individual claims
because they are definitions, section headings, reader-facing verification
prompts, or narrative restatements of a table already logged elsewhere:
the SCALE/C5ISR/MALE/MUM-T/P-8I glossary entries; every "**What to
verify:**" or "**Diligence focus.**" callout (instructions, not independent
facts); prose restating the ten-year table already captured as C039; and
diligence-checklist items that restate claims logged elsewhere. Definitions
that carry a material performance threshold (for example, the 1-to-5-tonne
and 24-to-40-hour SCALE definition) remain logged.

**Excluded internal-origin note:** `business-cases/business-case-male-uas.md`
is a Nitrodynamics-origin internal company case. Its entries in this ledger
exist only to expose internal consistency issues and provenance. They are not
market evidence, are excluded from the company-agnostic evidence baseline, and
must not migrate into the tri-service rewrite as sourced facts or company
framing.

---

## 1. Cross-service procurement and allocations

- Claim ID: C001
  - Service: Tri-service / cross-service
  - Claim: In 2024 the Government of India signed for 31 MQ-9B aircraft at roughly USD 4 billion.
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft. Referenced again at lines 16 and 46 of the source file with identical wording.
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: Plausible and widely reported externally, but the draft itself cites nothing. Needs a primary MoD/PIB/US DSCA source in Task 2 before it can be marked confirmed.

- Claim ID: C002
  - Service: Tri-service / cross-service (Navy-weighted)
  - Claim: The committed main draft says only that the Indian Navy took the largest share of the 31-aircraft MQ-9B order; it gives no numeric Navy/Army/Air Force split.
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft.
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: Superseded for audit coverage by the external 3P draft's explicit 15 Navy / 8 Army / 8 Air Force allocation (C045, C049, C051), while retained to show what the committed main draft omitted.

- Claim ID: C003
  - Service: Tri-service / cross-service
  - Claim: India's stated requirement for the decade runs to 70 to 100 aircraft in this class.
  - Status: reported
  - Source type: secondary (draft table labels this "Publicly reported tri-service requirement")
  - Source: Table row, §3: "Publicly reported tri-service requirement."
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: Repeated verbatim at lines 16, 46, 59, 79, 208, 217. The draft asserts this is "tri-service" but supplies no service-by-service breakdown anywhere, which is itself a structural gap (see §11).

- Claim ID: C004
  - Service: Tri-service / cross-service
  - Claim: [Structural gap in the committed main draft] Neither the 31-aircraft MQ-9B buy nor the 70–100 aircraft decade requirement is broken out by service there.
  - Status: rejected
  - Source type: secondary (internal audit observation)
  - Source: Absence noted across the full document.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Rejected as a data point because it is an absence, not a claim. The 3P input resolves the MQ-9B allocation gap (C045) but not service allocation for the 87-, 97- or projected 350-platform figures.

- Claim ID: C044
  - Service: Tri-service / cross-service (procurement policy)
  - Claim: "India's indigenisation regime, positive-indigenisation lists and import-substitution mandates, keeps closing the home market to foreign airframes"; the 2024 MQ-9B buy "reads best as a stopgap purchased while the domestic pipeline matures, and the stated ambition on the record remains a sovereign platform."
  - Status: assumption
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §8, line 180.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Positive Indigenisation Lists are a real, named MoD policy instrument, but no specific list, notification, or date is cited here. The "stopgap" characterization of the MQ-9B buy is the author's interpretive framing, not a sourced government statement, and should be labeled as interpretation rather than fact in the rewrite.

- Claim ID: C005
  - Service: Tri-service / cross-service
  - Claim: `business-case-male-uas.md` restates "India needs an estimated 70–100 MALE-class airframes this decade; the 2024 MQ-9B buy confirms appetite."
  - Status: reported
  - Source type: secondary (internal sibling business case, not an external source)
  - Source: `business-cases/business-case-male-uas.md`, §1 and §2 table.
  - Publisher: Internal document (Nitrodynamics company business case), not a public authority.
  - Published: Not dated in the sibling document.
  - URL: n/a (repository file)
  - Accessed: 2026-07-22
  - Drafting note: **EXCLUDED INTERNAL ORIGIN.** Nitrodynamics-origin comparison only; not part of the company-agnostic evidence baseline and not eligible to migrate into the rewrite. It shows only that two internal documents agree, not independent external verification.

- Claim ID: C045
  - Service: Tri-service / cross-service
  - Claim: On 15 October 2024 India signed a ₹28,000 crore (USD 3.5 billion) contract for 31 MQ-9Bs, allocated as 15 SeaGuardians to the Navy and eight SkyGuardians each to the Army and Air Force, plus a separate ₹4,350 crore depot-level-maintenance contract; deliveries run from January 2029 through October 2030.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 1, "MQ-9B contract, 15 Oct 2024"; grouped reporting by The Indian Express, The Hindu, and Times of India.
  - Publisher: The Indian Express; The Hindu; Times of India
  - Published: October 2024
  - URL: https://indianexpress.com/article/india/india-us-rs-28000-crore-deal-to-procure-31-mq-9b-drones-for-armed-forces-9621240/ ; https://www.thehindu.com/news/national/mq-9b-armed-uavs-to-be-delivered-by-2030/article68761650.ece
  - Accessed: 2026-07-22
  - Drafting note: This resolves the earlier concern that the service split was absent from the audited source: it is explicit in the external 3P draft. Status remains `reported`, not `confirmed`, because the appendix bundles all package, allocation, maintenance, and delivery claims across several press sources rather than linking each claim to a primary contract record.

- Claim ID: C046
  - Service: Tri-service / cross-service
  - Claim: The Defence Acquisition Council cleared an indigenous procurement of 87 MALE-class aircraft above ₹30,000 crore in August 2025 under IDDM with a 60% indigenous-content mandate; the RFP issued in November 2025 and bids closed on 16 June 2026.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 2, "87-aircraft MALE tender."
  - Publisher: idrw.org; Indian Defence News
  - Published: June 2026
  - URL: https://idrw.org/indias-30000-crore-indigenous-male-uav-program-enters-crucial-evaluation-phase-after-rfp-deadline-closure/ ; https://www.indiandefensenews.in/2026/06/ten-indian-firms-compete-for-30000.html
  - Accessed: 2026-07-22
  - Drafting note: Central demand claim, but supported in the 3P draft only by low-transparency defense sites, not a linked DAC release or RFP. It must be corroborated with primary MoD material before promotion to `confirmed`.

- Claim ID: C047
  - Service: Tri-service / cross-service
  - Claim: The 87-aircraft procurement sits within a stated tri-service requirement of 97 platforms, with service projections reaching 350 units.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 2, which attributes the figures generally to "MoD and defense-press reporting, 2025-26."
  - Publisher: idrw.org; Indian Defence News; unspecified MoD reporting
  - Published: 2025–2026
  - URL: https://idrw.org/indias-30000-crore-indigenous-male-uav-program-enters-crucial-evaluation-phase-after-rfp-deadline-closure/ ; https://www.indiandefensenews.in/2026/06/ten-indian-firms-compete-for-30000.html
  - Accessed: 2026-07-22
  - Drafting note: Procurement status is ambiguous: 97 is called a "stated requirement," while 350 is explicitly a projection, not an approved or tendered quantity. Do not sum either with the 87-aircraft tender.

- Claim ID: C048
  - Service: Tri-service / cross-service
  - Claim: Roughly ten Indian firms bid for the 87-aircraft tender, including HAL, Tata Advanced Systems, Larsen & Toubro, Adani Defence, Solar Defence and Raphe mPhibr; the ministry plans a dual award between the two best compliant bidders in a 64-to-36 ratio.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 2, "87-aircraft MALE tender."
  - Publisher: idrw.org; Indian Defence News
  - Published: June 2026
  - URL: https://www.indiandefensenews.in/2026/06/ten-indian-firms-compete-for-30000.html
  - Accessed: 2026-07-22
  - Drafting note: The draft alternates between "plans," "assumes," and "guarantees" when describing the dual award. Until an RFP or MoD record is obtained, retain `reported` status and avoid saying the structure guarantees two awards.

- Claim ID: C071
  - Service: Tri-service / cross-service (tender schedule)
  - Claim: The 87-aircraft tender's bid deadline was extended twice.
  - Status: reported
  - Source type: secondary
  - Source: 3P §5; the appendix provides no specific citation for the extension history.
  - Publisher: Not stated for this claim.
  - Published: Not stated.
  - URL: Not stated for this claim.
  - Accessed: 2026-07-22
  - Drafting note: Material schedule evidence used to argue that qualification slips are normal. Needs the original RFP amendments or attributable reporting before reuse.

- Claim ID: C072
  - Service: Tri-service / cross-service (procurement cycle)
  - Claim: Defense sales cycles run three to seven years, with one ministry-level customer per country and lumpy contracts following formal trials.
  - Status: estimate
  - Source type: secondary (internal draft explainer; no external citation)
  - Source: 3P §1 procurement explainer.
  - Publisher: Internal draft.
  - Published: July 2026
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: General procurement heuristic rather than an India-specific rule; sales-cycle duration should be presented as a range/estimate, not a universal fact.

---

## 2. Indian Army missions and programmes

- Claim ID: C049
  - Service: Army
  - Claim: The Army allocation in the 2024 MQ-9B contract is eight SkyGuardian aircraft.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 1, "MQ-9B contract, 15 Oct 2024."
  - Publisher: The Indian Express; The Hindu; Times of India
  - Published: October 2024
  - URL: https://indianexpress.com/article/india/india-us-rs-28000-crore-deal-to-procure-31-mq-9b-drones-for-armed-forces-9621240/
  - Accessed: 2026-07-22
  - Drafting note: This is an allocation, not an Army demand model. The 3P draft still supplies no Army-specific mission analysis, demand wedge, basing, qualification boundary, or substitute test.

- Claim ID: C050
  - Service: Army
  - Claim: The Army and Navy each bought two Drishti-10 Starliners under emergency procurement at roughly ₹120 crore per aircraft.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 4, "Drishti-10 Starliner."
  - Publisher: Business Today; Economic Times; ThePrint; Asianet
  - Published: 2024–2025
  - URL: https://theprint.in/defence/navy-gets-its-first-male-drone-made-by-adani-as-army-awaits-next-larger-order-in-play/1917870/
  - Accessed: 2026-07-22
  - Drafting note: The exact "2 Navy + 2 Army" quantity and price are bundled with multiple other Drishti claims in the appendix. Keep `reported` pending contract-level or service confirmation.

### Task 2 additions: transaction evidence, Army demand, and mission boundaries

- Claim ID: C073
  - Service: Tri-service / cross-service
  - Claim: The Defence Acquisition Council accorded Acceptance of Necessity on 15 June 2023 for 31 MQ-9B RPAS — 16 SkyGuardian and 15 SeaGuardian — for the tri-services through the U.S. Foreign Military Sales route; the AoN included associated equipment and recorded a then-estimated U.S. price of USD 3.072 billion, still subject to negotiation.
  - Status: confirmed
  - Source type: primary
  - Source: "Acquisition of MQ-9B drones: Speculative reports uncalled for."
  - Publisher: Press Information Bureau / Ministry of Defence, Government of India
  - Published: 25 June 2023
  - URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=1935160
  - Accessed: 2026-07-22
  - Direct support: The release states the AoN date, quantity, variants, tri-service purpose, FMS route, associated-equipment scope, and provisional price; it also explains that the later LOA would settle equipment, terms, and price.
  - Limitations: AoN is an approval to proceed, not a signed acquisition contract. The release does not publish the Army/Air Force split within the 16 SkyGuardians.
  - Drafting note: This replaces any wording that treats the June 2023 AoN or its USD 3.072 billion estimate as the final contract.

- Claim ID: C074
  - Service: Tri-service / cross-service
  - Claim: The U.S. State Department approved and notified Congress of a **possible** FMS to India of 31 MQ-9B aircraft and related equipment at an estimated ceiling of USD 3.99 billion.
  - Status: confirmed
  - Source type: primary
  - Source: "Arms Sales Notification," Transmittal No. 23-75, India — MQ-9B Remotely Piloted Aircraft.
  - Publisher: U.S. Department of State / Defense Security Cooperation Agency, reproduced in the U.S. Federal Register
  - Published: notification dated 1 February 2024; Federal Register publication 6 January 2025
  - URL: https://www.govinfo.gov/content/pkg/FR-2025-01-06/pdf/2024-31699.pdf
  - Accessed: 2026-07-22
  - Direct support: The notice lists 31 aircraft, 161 embedded navigation systems, 35 COMINT suites, 170 AGM-114R Hellfire missiles, 16 captive training missiles, 310 laser Small Diameter Bombs, eight guided test vehicles, radars, sonobuoys, ground-control, communications, training, spares, software, transport, engineering, logistics, and programme support.
  - Limitations: A congressional notification is a maximum possible scope and estimated value, not proof that every line item entered the final LOA or was contracted at that value. It calls all 31 aircraft "Sky Guardian" and does not provide India's service allocation.
  - Drafting note: Use this source to define the notified package ceiling and weapons/support breadth, never as the executed contract price.

- Claim ID: C075
  - Service: Tri-service / cross-service
  - Claim: India signed the 31-aircraft MQ-9B contract on 15 October 2024; public reporting based on the Ministry announcement allocates 15 SeaGuardians to the Navy and eight SkyGuardians each to the Army and Air Force.
  - Status: reported
  - Source type: secondary (attributable national reporting quoting the Ministry announcement)
  - Source: "India, U.S. conclude $3.5bn deal for 31 MQ-9B armed UAVs"; "MQ-9B armed UAVs to be delivered by 2030."
  - Publisher: The Hindu
  - Published: 15 October 2024; 17 October 2024
  - URL: https://www.thehindu.com/news/national/india-to-procure-31-predator-long-endurance-drones-from-us/article68755738.ece ; https://www.thehindu.com/news/national/mq-9b-armed-uavs-to-be-delivered-by-2030/article68761650.ece
  - Accessed: 2026-07-22
  - Direct support: The reports state the contract date, nearly USD 3.5 billion value, and 15/8/8 allocation, and quote the Ministry's statement that one contract covered the tri-service systems and another covered performance-based logistics and depot-level MRO in India.
  - Limitations: The Ministry's social-media announcement was not available as a stable contract document. The 15/8/8 split is strongly corroborated by The Hindu, Indian Express, Reuters, and Janes but remains `reported` here because the signed LOA and Indian contract are not public.
  - Drafting note: C045 and C049 are corroborated but not promoted beyond the evidence. The Army's eight-aircraft allocation is an executed allocation, not evidence of a larger Army quantity.

- Claim ID: C076
  - Service: Tri-service / cross-service
  - Claim: Reported contractual delivery is January 2029 through September 2030 (first aircraft at 51 months, last at 72 months); the package includes two years of contracted logistics support and a separate performance-based logistics arrangement for depot-level MRO in India, reported as up to eight years or 150,000 flight hours.
  - Status: reported
  - Source type: secondary (official-sourced reporting)
  - Source: "MQ-9B armed UAVs to be delivered by 2030."
  - Publisher: The Hindu
  - Published: 17 October 2024
  - URL: https://www.thehindu.com/news/national/mq-9b-armed-uavs-to-be-delivered-by-2030/article68761650.ece
  - Accessed: 2026-07-22
  - Direct support: The article quotes officials on the 51-to-72-month delivery clause, dates, logistics period, PBL ceiling, and Indian depot-level MRO.
  - Limitations: Delivery and PBL details are not independently visible in a released contract. GA-ASI's 14 February 2023 HAL announcement supports intended Indian engine MRO but predates contract signature and says the comprehensive programme still had to be formulated.
  - Drafting note: Do not restate the older October 2030 endpoint in C045; the checked source says September 2030.

- Claim ID: C077
  - Service: Tri-service / cross-service
  - Claim: In July 2025, an 87-aircraft indigenous MALE procurement was reported as being accelerated but still awaiting high-level Ministry clearance, with a value above ₹20,000 crore, a 60% indigenous-content requirement, more than 30-hour endurance, at least 35,000-foot ceiling, and all-terrain ISR/strike capability.
  - Status: reported
  - Source type: secondary (attributable national reporting based on officials and a project source)
  - Source: "Government fast-tracks procurement of MALE class drones to enhance border surveillance."
  - Publisher: The Hindu
  - Published: 9 July 2025
  - URL: https://www.thehindu.com/news/national/government-fast-tracks-procurement-of-male-class-drones-to-enhance-border-surveillance/article69792928.ece
  - Accessed: 2026-07-22
  - Direct support: The report directly supports 87 aircraft, local manufacture, the pre-clearance status on that date, reported value, performance envelope, and 60% content requirement.
  - Limitations: No public DAC release, AoN, RFP, amendment, bid record, or service allocation was found. Later reports of August 2025 approval, a September 2025 RFP, June 2026 bid closure, approximately ten bidders, ₹30,000-plus crore value, and a 64:36 award rely on anonymous or low-transparency reporting.
  - Drafting note: Keep C046/C048 `reported`; do not call the 64:36 structure guaranteed. No directly verifiable public source was found for a 97-aircraft requirement, 350-aircraft projection, or service allocation, so C047 cannot support demand arithmetic.

- Claim ID: C078
  - Service: Army
  - Claim: The Army has a documented need for persistent land-border surveillance: official material says surveillance drones are deployed on high-altitude northern borders, while Army/BEL's SANJAY system is designed to fuse ground and aerial sensors into a common surveillance picture across vast land borders.
  - Status: confirmed
  - Source type: primary
  - Source: "Drone Policy"; "Raksha Mantri Shri Rajnath Singh flags-off 'SANJAY - The Battlefield Surveillance System' from New Delhi."
  - Publisher: Press Information Bureau / Government of India
  - Published: April 2023; 24 January 2025
  - URL: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2023/apr/doc2023424185301.pdf ; https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2095712
  - Accessed: 2026-07-22
  - Direct support: The policy document says Army surveillance drones monitor high-altitude northern border areas. SANJAY integrates all ground and aerial battlefield sensors over secured Army and satellite networks and was planned for all operational brigades, divisions, and corps.
  - Limitations: Neither source quantifies orbit count, aircraft quantity, geographic coverage, or a requirement for a particular MALE/HALE platform. Western-border persistence is supported only by reported Drishti-10/Heron deployments, not by this primary pair.
  - Mission-boundary note:
    - **Tactical UAS:** wins for local, responsive sector coverage; loses for theatre-wide persistence and heavy multi-sensor carriage. SCALE complements it as the wide-area layer.
    - **Satellite:** wins for sovereign broad-area access without aircrew basing; loses on continuous stare and rapid retasking unless a constellation is dense. SCALE complements revisit coverage.
    - **Aerostat:** wins for low-cost fixed-site persistence; loses mobility, weather tolerance, and deep look across masking terrain. SCALE wins for repositionable coverage.
    - **Crewed ISR aircraft:** wins where onboard judgement, payload power, and rapid cross-cueing matter; loses endurance and exposes crew. SCALE complements scarce sorties.
    - **Ground sensor:** wins for persistent local detection and concealment; loses horizon and wide-area identification. SCALE complements cueing and classification.
    - **HAPS:** can win on weeks-long persistence over a broad fixed region once operational; loses payload flexibility and remains developmental in India. SCALE is the nearer-term, recoverable complement.
    - **Attritable drone:** wins in contested forward airspace and for affordable mass; loses endurance/payload at equivalent range. SCALE should remain standoff sensor/relay, not a disposable penetrator.

- Claim ID: C079
  - Service: Army
  - Claim: High-altitude Army operations impose demonstrated drone-performance constraints: rarified air reduces lift and engine performance, while extreme cold and high winds compound the problem; the Army therefore tested surveillance, logistics, loitering, swarm, EW, SAR, COMINT and ELINT drone solutions at 4,000–5,000 metres in Ladakh.
  - Status: confirmed
  - Source type: primary
  - Source: "Curtain raiser for HIM-DRONE-A-THON-2 & HIMTECH-2024: Setting the course for demonstration of drones in high altitude areas."
  - Publisher: Press Information Bureau / Ministry of Defence
  - Published: 4 September 2024
  - URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2051715
  - Accessed: 2026-07-22
  - Direct support: The release states the physical effects of rarified atmosphere, cold, and wind and identifies the altitude and mission/payload categories to be demonstrated.
  - Limitations: It is a technology-demonstration requirement, not proof that any SCALE airframe passed, was selected, or can launch fully loaded from a high-altitude strip. No equally specific primary source for hot-desert MALE performance was found.
  - Drafting note: High-altitude qualification must be treated as a design and trial gate. Western-desert surveillance is reported for Drishti-10 from Bathinda, but the public record does not publish a desert environmental qualification.

- Claim ID: C080
  - Service: Army
  - Claim: The public Army fleet record supports active use/procurement of Heron Mk2 and Drishti-10 for northern/eastern and western surveillance, but does not establish Army induction of TAPAS or Archer-NG.
  - Status: reported
  - Source type: secondary (multiple defence-source reporting) plus primary developer status pages
  - Source: "Armed forces contract more long endurance drones from Israel under emergency procurement"; "Indian army to induct first Hermes-900 Drone for surveillance along Pakistan border"; DRDO TAPAS-BH and UAV Certification pages.
  - Publisher: The Hindu; Business Today; Defence Research and Development Organisation
  - Published: 7 November 2023; 11 May 2024; DRDO webpages undated
  - URL: https://www.thehindu.com/news/national/armed-forces-contract-more-long-endurance-drones-from-israel-under-emergency-procurement/article67510035.ece ; https://www.businesstoday.in/india/story/indian-army-to-induct-first-hermes-900-drone-for-surveillance-along-pakistan-border-429181-2024-05-11 ; https://drdo.gov.in/drdo/tapas-bh ; https://www.drdo.gov.in/drdo/uav-certification
  - Accessed: 2026-07-22
  - Direct support: The Hindu reports four Army Heron Mk2s bought in 2021 and inducted in 2022, with two at Leh and two in Eastern Command, plus two Hermes 900s contracted in 2023. Business Today reports two Army Drishti-10s and planned Bathinda deployment for the desert and areas north of Punjab. DRDO describes TAPAS as an Armed Forces ISR design/certification programme.
  - Limitations: Army quantities, basing, and induction dates are not backed by released contracts or Army inventory tables. TAPAS's DRDO status does not prove user acceptance or procurement; Archer-NG remained in development in public material. Do not represent either as an operational Army fleet.

- Claim ID: C081
  - Service: Army
  - Claim: Artillery target acquisition, fire correction, and battle-damage assessment are documented Army UAS roles; official artillery material also treats UAVs, surveillance sensors, and weapon-locating radars as complementary target-acquisition systems.
  - Status: confirmed
  - Source type: primary
  - Source: "Exercise Sarvatra Prahar"; "NISHANT UAV to be handed over to Indian Army soon"; "Maiden Flight of Panchi."
  - Publisher: Press Information Bureau / Ministry of Defence
  - Published: 12 January 2016; 12 February 2009; 24 December 2014
  - URL: https://www.pib.gov.in/newsite/erelcontent.aspx?relid=134367 ; https://www.pib.gov.in/newsite/erelcontent.aspx?relid=47445 ; https://pib.gov.in/newsite/PrintRelease.aspx?relid=114071
  - Accessed: 2026-07-22
  - Direct support: The releases identify UAV target tracking/localisation and artillery-fire correction and show UAVs used alongside surveillance sensors and weapon-locating radars.
  - Limitations: Nishant/Panchi are tactical precedents, not evidence that every artillery mission needs a SCALE platform. The official sources do not allocate BDA by echelon or state a MALE quantity.
  - Mission-boundary note:
    - **Tactical UAS:** normally wins for responsive brigade/battalion target acquisition and fire correction; SCALE wins only for deep, wide-area, multi-hour search and cross-formation support.
    - **Satellite:** complements pre-mission cueing and large-area change detection; revisit and latency can lose against moving-target correction.
    - **Aerostat:** wins for persistent observation of a fixed frontage in permissive conditions; loses mobility and masking.
    - **Crewed ISR aircraft:** complements complex deep-target collection but is costlier and crew-risked for long stare.
    - **Ground sensor:** weapon-locating radar and observation systems win for specific emitters/trajectories; SCALE complements identification, track continuity, and BDA.
    - **HAPS:** could win persistent theatre sensing once fielded, but payload/retasking and Indian maturity are unresolved.
    - **Attritable drone:** wins as the forward sensor or effector in defended airspace; SCALE complements from standoff and should not be the default fire-correction asset.

- Claim ID: C082
  - Service: Army
  - Claim: Airborne communications relay across difficult terrain is a documented UAS role, while GSAT-7B is already contracted to provide the Army with mission-critical beyond-line-of-sight communications to troops, formations, weapons, and airborne platforms.
  - Status: confirmed
  - Source type: primary
  - Source: "Compendium of Products for Export 2025" (Unmanned Aerial System); Ministry announcement of contracts for Project Akashteer, Sarang ESM and GSAT-7B.
  - Publisher: Defence Research and Development Organisation; Press Information Bureau / Ministry of Defence
  - Published: 2025; 29 March 2023
  - URL: https://www.drdo.gov.in/drdo/sites/default/files/schemes_services/CompendiumProductforExport2025.pdf ; https://www.pib.gov.in/PressReleasePage.aspx?PRID=1911937
  - Accessed: 2026-07-22
  - Direct support: DRDO specifies a UAV Communication Repeater for tactical communications in difficult terrain. MoD states the ₹2,963 crore GSAT-7B contract will provide Army BLOS service to troops, formations, weapons, and airborne platforms.
  - Limitations: The DRDO compendium describes an offered platform capability, not an Army contract. GSAT-7B validates demand for BLOS connectivity but is a substitute/backbone, not proof of an airborne-relay fleet size.
  - Mission-boundary note:
    - **Tactical UAS:** wins for a temporary local relay over one ridge; loses coverage radius, endurance, and payload power for theatre networks.
    - **Satellite:** GSAT-7B wins for broad BLOS backbone; SCALE complements local capacity, directional links, and resilience but cannot replace strategic SATCOM.
    - **Aerostat:** wins persistent relay over a fixed area with logistics access; loses mobility and weather resilience.
    - **Crewed ISR aircraft:** can relay during a mission but loses on endurance and crew cost; use only when already tasked.
    - **Ground sensor/relay:** wins where line-of-sight towers or radio relay can be protected; terrain masking and kinetic vulnerability create gaps.
    - **HAPS:** likely wins the long-duration wide-area relay mission once mature; Indian AS-HAPS had AoN, not an operational system, as of access.
    - **Attritable drone:** wins for expendable emergency mesh nodes near the forward edge; SCALE complements as the higher-capacity standoff gateway.

- Claim ID: C083
  - Service: Army
  - Claim: ELINT/COMINT collection is a documented payload mission for Indian MALE UAS and Army-oriented aerostats.
  - Status: confirmed
  - Source type: primary
  - Source: DRDO "UAV Certification"; DRDO "Compendium of Products for Export 2025"; DRDO "Technologies and Products" (COMINT payload for Aerostat platform for Indian Army).
  - Publisher: Defence Research and Development Organisation
  - Published: certification webpage undated; compendium 2025; product webpage undated
  - URL: https://www.drdo.gov.in/drdo/uav-certification ; https://www.drdo.gov.in/drdo/sites/default/files/schemes_services/CompendiumProductforExport2025.pdf ; https://drdo.gov.in/drdo/technology-cluster-links/labs-products-detail/2141/188
  - Accessed: 2026-07-22
  - Direct support: DRDO lists TAPAS ELINT/COMINT payloads and SATCOM control, describes emitter detection/direction-finding/geolocation, and records an evaluated COMINT payload integrated on an aerostat for the Indian Army.
  - Limitations: Payload availability and evaluation do not prove operational Army procurement, collection performance, or authority to conduct particular missions. SIGINT is used here as the umbrella term; sources specifically say ELINT and COMINT.
  - Mission-boundary note:
    - **Tactical UAS:** wins for close, local emitter hunting; SCALE wins payload aperture, power, endurance, and wide-area geolocation baselines.
    - **Satellite:** wins inaccessible-area collection and broad coverage; SCALE complements dwell, retasking, and lower-latency localisation.
    - **Aerostat:** is the closest confirmed Army substitute and wins fixed-area persistence/cost; SCALE wins mobility and deep stand-off geometry.
    - **Crewed ISR aircraft:** wins payload/operator flexibility but loses endurance and crew exposure; complementary for surge and complex exploitation.
    - **Ground sensor:** wins covert persistent monitoring at choke points; loses horizon and relocation speed.
    - **HAPS:** may win persistent wide-area SIGINT once payload and platform mature; currently complements rather than displaces recoverable MALE aircraft.
    - **Attritable drone:** wins risky close-in collection and decoying; loses payload, endurance, and recoverability. SCALE remains the standoff collector.

- Claim ID: C084
  - Service: Army
  - Claim: The Army's April 2026 UAS technology roadmap publicly identifies HALE, MALE, HAPS and other surveillance classes, loitering munitions, anti-swarm drones, and a special "mother-child" configuration in which a mother UAS carries and controls child drones.
  - Status: reported
  - Source type: secondary (attributable reporting from the Army roadmap release and Army officials)
  - Source: "Army unveils future blueprint for drones, loitering munitions requirements to industry, academia."
  - Publisher: The Hindu BusinessLine
  - Published: 6 April 2026
  - URL: https://www.thehindubusinessline.com/news/national/army-unveils-future-blueprint-for-drones-loitering-munitions-requirements-to-industry-academia/article70830864.ece
  - Accessed: 2026-07-22
  - Direct support: The report names the Army document, release officials, surveillance classes, loitering/air-defence categories, and mother-child control concept.
  - Limitations: Only selective roadmap pages were shared because requirements are confidential. The public report does not say the mother must be SCALE/MALE, disclose quantities, or establish an approved procurement or contract.
  - Mission-boundary note:
    - **Tactical UAS:** wins direct control of nearby effects with lower latency; SCALE wins reach, persistence, payload capacity, and multi-formation coordination.
    - **Satellite:** complements communications and theatre awareness but cannot physically launch/recover effects.
    - **Aerostat:** can host communications/control over a fixed area but is poorly suited to mobile launch geometry.
    - **Crewed ISR aircraft/helicopter:** wins human judgement and is already relevant to MUM-T; loses endurance and exposes crew.
    - **Ground sensor/control station:** wins bandwidth and operator capacity when links survive; loses horizon and can be fixed/targetable.
    - **HAPS:** may win persistent high-level command/relay but has limited payload/recovery flexibility and remains immature.
    - **Attritable drone:** is normally the launched effect, not the command platform; SCALE complements by carrying, cueing, or controlling it from standoff.

- Claim ID: C085
  - Service: Army
  - Claim: Local convoy escort, camp security, and base-perimeter overwatch are not evidenced as core SCALE missions in the checked Army record.
  - Status: rejected
  - Source type: primary-and-secondary research finding
  - Source: Mission-boundary review of C078–C084 and the Army UAS roadmap reporting.
  - Publisher: n/a
  - Published: n/a
  - URL: See C078–C084.
  - Accessed: 2026-07-22
  - Direct support: Public evidence ties large endurance UAS to wide-area border surveillance, deep/long-range sensing, BLOS relay, signals collection, and mother-child/special roles. It ties local observation and close support to tactical, swarm, FPV, tethered, or ground/aerial sensor layers.
  - Limitations: Absence of public evidence is not proof the Army never uses a large UAS for local overwatch; classified operational practice may differ.
  - Drafting note: Exclude convoy/base overwatch from the core SCALE demand case unless a later source demonstrates a range, endurance, heavy-payload, or airborne-command requirement that tactical systems cannot meet.

- Claim ID: C086
  - Service: Common platform / airworthiness
  - Claim: CEMILAC and DGAQA are India's technical military-airworthiness authorities; certification starts with requirements and proceeds concurrently through design review, inspection, qualification and development trials, while type approval follows satisfactory service performance and does not itself assure a production order.
  - Status: confirmed
  - Source type: primary
  - Source: "Indian Military Airworthiness Procedure 2023"; "Certification Services."
  - Publisher: CEMILAC / Defence Research and Development Organisation
  - Published: 2023; certification webpage undated
  - URL: https://www.drdo.gov.in/drdo/sites/default/files/form_formats/IMAP2023.pdf ; https://drdo.gov.in/drdo/en/offerings/schemes-and-services/certification-services
  - Accessed: 2026-07-22
  - Direct support: IMAP-2023 defines the authorities and DGAQA's quality-assurance role; CEMILAC describes concurrent certification and explicitly states that type approval is not assurance of a production order.
  - Limitations: Neither source supports the draft's universal five-to-seven-year certification duration or "hundreds to thousands of flight-test hours."
  - Drafting note: C016 can be promoted to `confirmed`; C014 and the flight-hour portion of C055 remain unsupported estimates.

---

## 3. Indian Air Force missions and programmes

- Claim ID: C051
  - Service: Air Force
  - Claim: The Air Force allocation in the 2024 MQ-9B contract is eight SkyGuardian aircraft.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 1, "MQ-9B contract, 15 Oct 2024."
  - Publisher: The Indian Express; The Hindu; Times of India
  - Published: October 2024
  - URL: https://indianexpress.com/article/india/india-us-rs-28000-crore-deal-to-procure-31-mq-9b-drones-for-armed-forces-9621240/
  - Accessed: 2026-07-22
  - Drafting note: This is an allocation, not an Air Force demand model. The 3P draft still supplies no Air Force-specific mission analysis, demand wedge, survivability boundary, or substitute test.

---

## 4. Indian Navy missions and programmes

- Claim ID: C006
  - Service: Navy
  - Claim: India has 7,500 kilometres of coastline and an exclusive economic zone of 2.4 million square kilometres.
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft (Prologue, line 14).
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: Commonly cited figures externally (coastline ~7,500 km is a standard rounding; EEZ figures for India are reported in a 2.0–2.4 million sq km range depending on source), but this draft cites none. This claim is also flagged structurally in §11 because the design spec instructs the rewrite to stop opening with this frame.

- Claim ID: C007
  - Service: Navy
  - Claim: "Chinese survey ships, submarines and task groups now move as a matter of routine" through India's EEZ.
  - Status: assumption
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft (Prologue, line 14).
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: An unquantified operational characterization with no supporting incident, date, or source. Should be either dropped or replaced with a specific, sourced incident in the rewrite.

- Claim ID: C008
  - Service: Navy
  - Claim: The Indian Navy's weighting of the MQ-9B order shows the customer has already done the "cost per surveilled square kilometre per hour" arithmetic favoring large aircraft over small drones.
  - Status: assumption
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §4, line 91.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: An inference the author draws from C002, not an independent fact. Its evidentiary weight is exactly as strong as C002's (reported, uncited).

- Claim ID: C009
  - Service: Navy
  - Claim: A P-8I costs "several times as much per flying hour" than a SCALE-class UAS, and its crew of nine can stay airborne for "a third as long."
  - Status: estimate
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §1, line 34.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Specific comparative performance and cost figures with no cited basis. Needs a real P-8I operating-cost and endurance source before reuse.

- Claim ID: C010
  - Service: Navy
  - Claim: One continuous orbit 1,000 kilometres offshore requires three to four aircraft of 30-plus-hour endurance rotating on station.
  - Status: estimate
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §4, line 91.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: A derivable arithmetic estimate (transit time vs. endurance) but not tied to a named platform's actual transit speed/fuel curve, so it is presented as fact without the underlying numbers shown. Reasonable as an illustrative estimate; should be labeled as such if reused.

- Claim ID: C011
  - Service: Navy (export framing)
  - Claim: "Navies are the natural first export customers" for the SCALE class.
  - Status: rejected
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §8, line 184.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Rejected as a thesis-level claim for the rewrite. The design spec explicitly instructs the tri-service rewrite to test rather than assume naval export primacy, and this is one of the five structural gaps required to be recorded (§11).

- Claim ID: C012
  - Service: Navy (export framing)
  - Claim: "Coastal states from the Gulf to Southeast Asia share India's ocean-awareness problem at smaller scale."
  - Status: assumption
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §8, line 184.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: A generic geographic assertion, not tied to any named country, transaction, or requirement. This is exactly the kind of "coloured map" claim the draft's own §8 callout warns against ("an export thesis that starts with navies ... rather than a coloured map"), yet the draft does it anyway. No country-level evidence exists to promote this to Indo-Pacific/Gulf sections (§7, §8 below).

- Claim ID: C052
  - Service: Navy
  - Claim: India's officially revised coastline is 11,098.81 km (rounded in the 3P body to 11,099 km), promulgated on 29 April 2025, and its exclusive economic zone is approximately 2.3 million km².
  - Status: reported
  - Source type: primary
  - Source: 3P Appendix item 9, "Geography"; Ministry of Ports, Shipping and Waterways / PIB release and related reporting.
  - Publisher: Press Information Bureau; Ministry of Ports, Shipping and Waterways; The Hindu BusinessLine
  - Published: 29 April 2025
  - URL: https://www.pib.gov.in/PressReleasePage.aspx?lang=3&PRID=2198800&reg=3
  - Accessed: 2026-07-22
  - Drafting note: This supersedes the committed main draft's older 7,500 km / 2.4 million km² framing (C006). The appendix provides a primary-source link, but it bundles coastline and EEZ; retain `reported` until the cited release is checked claim-by-claim.

- Claim ID: C053
  - Service: Navy
  - Claim: The Navy moved first on Drishti-10 under emergency powers, based the aircraft at Porbandar for Arabian Sea surveillance, and is described as heading toward a ten-aircraft naval fleet.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 4, "Drishti-10 Starliner."
  - Publisher: Business Today; Economic Times; ThePrint; Asianet
  - Published: 2024–2025
  - URL: https://theprint.in/defence/navy-gets-its-first-male-drone-made-by-adani-as-army-awaits-next-larger-order-in-play/1917870/
  - Accessed: 2026-07-22
  - Drafting note: The appendix combines completed emergency purchases with a future ten-aircraft "path." Treat the latter as a reported plan, not a contract or approved quantity.

---

## 5. Common-platform architecture and qualification

- Claim ID: C013
  - Service: Common platform
  - Claim: A SCALE UAS is defined as a 1-to-5-tonne-class aircraft with 24-to-40-hour endurance.
  - Status: assumption
  - Source type: secondary (internal draft definition)
  - Source: Not stated in draft, header block and §1, lines 8 and 36.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: This is the document's own class definition, not an external fact; treated as a working assumption/definition for the sector, excluded from the "needs a citation" count but recorded because Task 4 will need to test it against real weight/endurance specs of named platforms.

- Claim ID: C014
  - Service: Common platform (certification)
  - Claim: Military airworthiness certification for an aircraft this size takes five to seven years.
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §2, line 47.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: A specific, checkable duration claim (explicitly called out as a "qualification duration" in the audit brief). No source given. Needs a CEMILAC/DGAQA-linked or comparable named-program source.

- Claim ID: C015
  - Service: Common platform (certification)
  - Claim: The certification toll gate turns a crowded field into "an oligopoly of two or three winners per sovereign market."
  - Status: assumption
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §2, line 47.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Analytical inference, not an empirical count of any actual national market. No named market is checked against this claim anywhere in the draft.

- Claim ID: C016
  - Service: Common platform (certification)
  - Claim: In India, CEMILAC is the design certification authority and DGAQA is the quality authority for military airworthiness.
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §5 callout, line 103.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Widely known institutional fact, but the draft cites nothing. Low risk, easy to source in Task 2/4 from official DRDO/CEMILAC material.

- Claim ID: C017
  - Service: Common platform (certification precedent)
  - Claim: "India's indigenous Tapas program has run more than a decade without reaching series production."
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §5, line 109.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: A specific, checkable programme-history claim used as certification-risk precedent. Needs a dated DRDO/MoD/parliamentary source.

- Claim ID: C018
  - Service: Common platform (certification)
  - Claim: Autonomy and mission software "must be certified alongside the airframe, under standards such as DO-178C for airborne software."
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §5, line 113.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: DO-178C is a real, named industry standard; the general applicability statement is uncited but low-risk. Should still be attributed in the rewrite.

- Claim ID: C019
  - Service: Common platform (sustainment economics)
  - Claim: Sustainment, software support and upgrade revenue runs at roughly 8 to 12 percent of installed fleet value per year.
  - Status: estimate
  - Source type: secondary (internal draft; no external citation)
  - Source: Draft states "checkable against published sustainment contracts" (§6, line 129) but names none.
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: Explicitly flagged as a sustainment percentage by the audit brief. The draft asserts it is checkable but does not check it. Repeated at lines 48, 129, 235. See C060: the ₹4,350 crore logistics package is 15.5% of acquisition value, but without contract duration and scope it does **not** independently support an 8–12% annual rate. C019 therefore remains an estimate needing a named annual sustainment benchmark.

- Claim ID: C020
  - Service: Common platform
  - Claim: Service life in this class runs 25 years.
  - Status: assumption
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §2 and §6, lines 48 and 129.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Standard defense-aerospace planning assumption; no named platform or program cited.

- Claim ID: C021
  - Service: Common platform (archetype framework)
  - Claim: A "platform-owner" (owns airframe IP, mission computer, autonomy stack) captures the sustainment/upgrade annuity; a "shell-maker" (assembles airframe around licensed foreign sensors) does not.
  - Status: assumption
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §6, lines 123–127.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: An analytical framework, not a sourced fact; no named example of either archetype is tested against real contract data anywhere in the draft.

- Claim ID: C022
  - Service: Common platform (capital planning)
  - Claim: "A contingency of 25 to 30 percent on non-recurring engineering is the credible norm for a first-of-class aircraft with certified software."
  - Status: estimate
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §7, line 168.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Industry-benchmark style figure with no named source. Repeated in the diligence scorecard at line 242.

- Claim ID: C054
  - Service: Common platform (qualification precedent)
  - Claim: TAPAS-BH-201 ran for more than a decade, missed altitude and endurance targets, closed as a mission-mode project in January 2024, was confirmed excluded from the 87-aircraft tender by March 2026, and continues as a technology demonstrator feeding Archer-NG.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 3, "TAPAS-BH-201 closure as mission-mode program ... and exclusion from the tender."
  - Publisher: idrw.org; Kodainya analysis
  - Published: January 2024–March 2026
  - URL: https://idrw.org/end-of-the-road-for-drdos-tapas-bh-201-uav-program-after-years-of-development-challenges/
  - Accessed: 2026-07-22
  - Drafting note: The appendix offers no primary DRDO closure record, tender exclusion notice, or exact missed performance thresholds. Use as a reported programme history only; do not infer causal exclusion from the missed targets without primary evidence.

- Claim ID: C055
  - Service: Common platform (airworthiness)
  - Claim: Military acceptance requires design, software and production-process certification involving design reviews, ground rigs, and hundreds to thousands of flight-test hours; CEMILAC is India's design authority and DGAQA its quality authority.
  - Status: reported
  - Source type: secondary
  - Source: 3P §5 airworthiness explainer; no appendix item specifically supports the authority roles or flight-hour range.
  - Publisher: Not stated for this claim.
  - Published: Not stated.
  - URL: Not stated for this claim.
  - Accessed: 2026-07-22
  - Drafting note: The named authorities are readily checkable, but the "hundreds to thousands" range is material and uncited. Split and source these elements in Task 4.

- Claim ID: C056
  - Service: Common platform (Drishti configuration)
  - Claim: Drishti-10 is a licence-built Elbit Hermes 900 with 36-hour endurance, 450 kg payload, STANAG 4671 certification, and approximately 70% claimed indigenous content; a Navy acceptance-trials aircraft crashed in January 2025.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 4, "Drishti-10 Starliner."
  - Publisher: Business Today; Economic Times; ThePrint; Asianet
  - Published: 2024–2025
  - URL: https://theprint.in/defence/navy-gets-its-first-male-drone-made-by-adani-as-army-awaits-next-larger-order-in-play/1917870/
  - Accessed: 2026-07-22
  - Drafting note: Five distinct performance, provenance, certification, content and loss claims are bundled across several outlets. "Claimed indigenous content" must remain qualified; STANAG certification should be tied to the exact configuration, and the crash should be verified separately before reuse.

---

## 6. Indian transactions and pricing

- Claim ID: C023
  - Service: Cross-service (pricing anchor)
  - Claim: Price anchor is ₹150–210 Cr per aircraft system (~USD 130 m per system-equivalent), "derived from the 2024 India MQ-9B transaction: 31 aircraft, ~USD 4 bn including weapons, ground stations and support."
  - Status: rejected
  - Source type: secondary (internal draft derivation; no external citation)
  - Source: Table row, §3, line 60.
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: **Arithmetic flag.** USD 4 bn / 31 aircraft ≈ USD 129 m per aircraft-equivalent, which the draft itself restates as "~USD 130 m per system-equivalent" in the same table cell — that part is internally consistent. But ₹150–210 Cr, at commonly used INR/USD rates in the ₹83–87/USD range, converts to roughly USD 17–25 m, not USD 130 m: an order-of-magnitude gap the draft never reconciles. The draft is implicitly using two different scope definitions in the same sentence (a bare aircraft-system catalogue price in rupees, versus a full-program cost-per-aircraft-equivalent in dollars that includes weapons, ground stations, training and support), but it presents them as the same anchor. This is exactly the kind of package-total-vs-unit-price conflation the design spec warns against ("Treat catalogue prices and contract totals carefully; identify whether figures include aircraft, ground stations, weapons, training, infrastructure, logistics, taxes, or sustainment"). Rejected as currently stated; Task 6 must rebuild this anchor with the scope of each figure made explicit and the two currencies reconciled at a stated, sourced exchange rate.

- Claim ID: C024
  - Service: Cross-service (market sizing)
  - Claim: Global market for large long-endurance UAS is USD 4–5 bn per year, growing 8–10% annually.
  - Status: estimate
  - Source type: analyst (draft labels this "Analyst consensus range")
  - Source: Table row, §3, line 58: "Analyst consensus range; re-verify against current Teal Group and Janes estimates at time of use."
  - Publisher: Teal Group and Janes are named as reference points but not linked or dated.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: The draft flags this itself as needing re-verification. Treat as a placeholder range pending an actual Teal Group/Janes citation with a publication date.

- Claim ID: C025
  - Service: Cross-service (financial sensitivity)
  - Claim: "At catalogue prices of ₹150–210 Cr per aircraft, a twelve-month slip defers roughly ₹180 to 540 Cr of annual deliveries at the ramp rates in §7."
  - Status: estimate
  - Source type: secondary (internal model derivation)
  - Source: Not stated in draft, §5 and §7, lines 111 and 158; repeated in §9 risk table, line 196, and falsifier list, line 205.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Consistent with the draft's own illustrative model (2–3 aircraft/year at ₹180–210 Cr roughly spans ₹360–630 Cr, in the same order as the stated ₹180–540 Cr), so it is at least self-consistent with the illustrative scenario in §7/§10 below. It inherits C023's unresolved anchor problem, though, since the price band itself is flagged as rejected.

- Claim ID: C026
  - Service: Cross-service (margin)
  - Claim: BoM-only gross margin in this sector runs "near 70 percent"; a fully loaded gross margin of 35 to 50 percent at maturity is the credible band.
  - Status: estimate
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §7 callout, line 156.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Presented as a warning to diligence readers ("the BoM-margin trap"), not as a sourced statistic. See C029 for a cross-document tension worth flagging.

- Claim ID: C027
  - Service: Cross-service (pricing anchor, cross-document)
  - Claim: `business-case-male-uas.md` restates the same ₹150–210 Cr catalogue price band for MALE-class airframes ("sparse high-ASP airframes (₹150–210 Cr catalogue)").
  - Status: reported
  - Source type: secondary (internal sibling business case)
  - Source: `business-cases/business-case-male-uas.md`, §1, line 9.
  - Publisher: Internal document.
  - Published: Not dated.
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Same figure, same lack of external citation, in a second internal document. Confirms internal consistency between the two drafts, not external validity. Inherits C023's unresolved USD/₹ reconciliation problem if reused.

- Claim ID: C028
  - Service: Cross-service (financial sensitivity, cross-document conflict)
  - Claim: `business-case-male-uas.md`'s risk register states a 12-month slip "Defers ~₹150–210 Cr/yr," a different figure than this draft's own ₹180–540 Cr/yr slip-deferral claim (C025) for what should be the same underlying concept.
  - Status: rejected
  - Source type: secondary (internal sibling draft; no external citation)
  - Source: `business-cases/business-case-male-uas.md`, §5, "Scale / payback milestones" table, line 97.
  - Publisher: Internal document.
  - Published: Not dated.
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: The male-UAS figure (₹150–210 Cr) looks like it restates the single-aircraft price band rather than an annual multi-aircraft delivery deferral, while the SCALE UAS draft's figure (₹180–540 Cr) is derived from 2–4 aircraft/year at that price. These are not describing the same quantity but are being used interchangeably across sibling documents. Flag for reconciliation in Task 6; do not carry either figure into the rewrite without recomputing from the rebuilt ramp schedule.

- Claim ID: C029
  - Service: Cross-service (margin, cross-document tension)
  - Claim: `business-case-male-uas.md` reports "Y10 BoM COGS ≈ ₹399 Cr → ~71% GM (BoM only)" as a headline supporting figure, without stating the fully loaded margin.
  - Status: reported
  - Source type: secondary (internal sibling business case, sourced to its own workbook cell references)
  - Source: `business-cases/business-case-male-uas.md`, §5, line 66 ("`V4_UAS_MALE`" table).
  - Publisher: Internal workbook (`Defense_Platform_Business_Plan_Financial_V2.xlsx`), not independently verifiable here.
  - Published: Not dated.
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: This is the exact trap the SCALE UAS draft's own §7 "BoM-margin trap" callout (C026) warns readers against: quoting BoM-only gross margin (~70%) as if it were the business's real margin. The sibling company document does precisely that, with no fully loaded figure alongside it. Worth flagging explicitly in the rewrite so the tri-service case does not repeat the same framing it criticizes elsewhere in the same document family.

- Claim ID: C057
  - Service: Cross-service (market sizing)
  - Claim: The global MALE segment was approximately USD 8.2 billion in 2025 with roughly 7.8% annual growth; wider-scope estimates exceed USD 30 billion, while the overall military-drone market was approximately USD 28 billion in 2025.
  - Status: estimate
  - Source type: analyst
  - Source: 3P Appendix item 8, "Market sizing."
  - Publisher: MarketIntelo; The Business Research Company; MarketsandMarkets
  - Published: 2025–2026
  - URL: Not stated in the 3P draft.
  - Accessed: 2026-07-22
  - Drafting note: Scope definitions differ substantially, which is why the estimates span USD 8–30+ billion. Do not present these values as one comparable market series or use them to derive entrant revenue.

- Claim ID: C058
  - Service: Cross-service (transaction-derived pricing)
  - Claim: The 3P draft derives an imported system-equivalent price of about ₹900 crore (₹28,000 crore / 31, also stated as about USD 113 million), a domestic tender system-equivalent of about ₹345 crore (₹30,000 crore / 87), and a Drishti-10 aircraft floor of about ₹120 crore.
  - Status: estimate
  - Source type: secondary
  - Source: 3P §3 transaction table and Appendix items 1, 2 and 4.
  - Publisher: The Indian Express; The Hindu; idrw.org; Indian Defence News; ThePrint and other named outlets
  - Published: 2024–2026
  - URL: https://indianexpress.com/article/india/india-us-rs-28000-crore-deal-to-procure-31-mq-9b-drones-for-armed-forces-9621240/ ; https://idrw.org/indias-30000-crore-indigenous-male-uav-program-enters-crucial-evaluation-phase-after-rfp-deadline-closure/ ; https://theprint.in/defence/navy-gets-its-first-male-drone-made-by-adani-as-army-awaits-next-larger-order-in-play/1917870/
  - Accessed: 2026-07-22
  - Drafting note: The divisions are arithmetically sound but not like-for-like unit prices: the MQ-9B package includes support and other scope; the tender is an indicative programme value; Drishti is described per aircraft. "Transaction corridor" is therefore an analytical construct, not a directly observed catalogue-price range.

- Claim ID: C059
  - Service: Cross-service (catalogue-price assumption)
  - Claim: A domestic entrant's ₹150–210 crore catalogue-price band is asserted to sit above the ₹120 crore licence-built floor, below the ₹345 crore domestic system-equivalent, and at a fraction of the ₹900 crore import system-equivalent.
  - Status: assumption
  - Source type: secondary
  - Source: 3P §3 narrative; the ₹150–210 crore band originates in the internal drafts, while the comparison anchors are grouped in Appendix items 1, 2 and 4.
  - Publisher: Internal draft plus named press sources for the transaction anchors
  - Published: 2024–2026
  - URL: See C058.
  - Accessed: 2026-07-22
  - Drafting note: The 3P rewrite fixes the committed draft's direct USD/₹ equivalence error (C023) by distinguishing system-equivalents from catalogue price. It does not source the ₹150–210 crore catalogue band itself, so the band remains an assumption rather than a transaction-supported fact.

- Claim ID: C060
  - Service: Cross-service (sustainment anchor)
  - Claim: The separate ₹4,350 crore MQ-9B performance-based logistics contract is approximately 15% of the ₹28,000 crore acquisition value and is used as evidence for a broader 8–12% annual sustainment assumption.
  - Status: estimate
  - Source type: secondary
  - Source: 3P §6 and Appendix item 1.
  - Publisher: The Indian Express; The Hindu; Times of India
  - Published: October 2024
  - URL: https://indianexpress.com/article/india/india-us-rs-28000-crore-deal-to-procure-31-mq-9b-drones-for-armed-forces-9621240/
  - Accessed: 2026-07-22
  - Drafting note: ₹4,350 / ₹28,000 = 15.5%, so "roughly 15%" is arithmetically correct. It is not an annual rate unless contract duration and included scope are known. Cross-reference C019: this package percentage does **not** independently validate the separate 8–12% annual sustainment assumption.

---

## 7. Indo-Pacific export markets

- No country-specific Indo-Pacific export-market claim appears in either draft. The only related statement is the generic "coastal states from the Gulf to Southeast Asia" line recorded as C012, which contributes no country-level requirement, transaction, access or localisation evidence. Task 5 must build this section from new research.

---

## 8. Gulf export markets

- The 3P draft names one Gulf transaction: Baykar's reported 60-aircraft Saudi order with a local production line (C064). It supplies no Saudi requirement detail, package value, delivery schedule, mission mix or Indian-supplier access analysis, and no other Gulf country is assessed. Task 5 must therefore research this market rather than treat the comparator as an addressable-demand claim.

---

## 9. Competition and substitutes

- Claim ID: C030
  - Service: Cross-service (competitive field)
  - Claim: Five incumbent platforms are named with positioning claims: GA-ASI MQ-9B (USA, "incumbent in India as of the 2024 buy"); Baykar TB2/Akıncı (Turkey, "export template ... now repositioning Akıncı as a drone controller"); IAI Heron/Heron-TP (Israel, "long-serving legacy fleet in India"); Elbit Hermes 900 (Israel, "strong export footprint with dedicated maritime variants"); CASC Wing Loong II (China, "price-led exporter ... excluded from India on political grounds").
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §3 table, lines 68–73.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Broadly consistent with public knowledge of these programmes, but none of the five positioning statements carries a citation. Each should get a named source in Task 4 (common-platform/competition) research.

- Claim ID: C031
  - Service: Cross-service (loss/attrition claim)
  - Claim: The Bayraktar TB2 "went from cover-story icon to routine air-defense kill inside eighteen months."
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §1, line 24.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: A specific timeframe claim about combat losses with no cited incident, date range, or source.

- Claim ID: C032
  - Service: Cross-service (loss/attrition claim)
  - Claim: "Houthi missiles costing a fraction of an MQ-9 have brought down more than a dozen of them over the Red Sea since 2023."
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §1, line 24.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: This is exactly the kind of "loss claim" the audit brief calls out for careful sourcing. "More than a dozen" is specific enough to verify against public loss trackers/press reporting; currently uncited.

- Claim ID: C033
  - Service: Cross-service (competitor programme claim)
  - Claim: "General Atomics is already integrating air-launched effects on the MQ-9B, and Baykar markets the Akıncı as a controller."
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §4, line 95.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Specific programme claims about two named competitors, no citation given.

- Claim ID: C034
  - Service: Cross-service (go-to-market precedent)
  - Claim: Baykar's TB2 entered Turkish service in 2014; combat validation followed in Syria, Libya, Nagorno-Karabakh and Ukraine; the export flywheel now spans "more than thirty customer countries, with exports the majority of revenue."
  - Status: reported
  - Source type: secondary (internal draft; no external citation)
  - Source: Not stated in draft, §8, line 176.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: The "thirty customer countries" and "majority of revenue" figures are specific and checkable against Baykar's own public reporting; currently uncited. Central to the go-to-market playbook the design spec asks the rewrite to test against India specifically.

- Claim ID: C035
  - Service: Cross-service (falsifier / kill criterion)
  - Claim: An "attritable endurance breakthrough" is defined as a sub-USD-1M airframe demonstrating 20-plus hours endurance, 200-plus kilograms of multi-sensor payload, and satellite communications at production scale.
  - Status: assumption
  - Source type: secondary (internal draft assumption)
  - Source: Not stated in draft, §9, line 205.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: An author-defined threshold for a kill criterion, not an empirical claim about an existing system. Appropriately treated as an assumption; no citation is owed for a defined threshold, but the rewrite should confirm no system already meets it.

- Claim ID: C036
  - Service: Cross-service (falsifier / kill criterion)
  - Claim: "Satellite substitution" is defined as proliferated low-orbit radar/RF constellations reaching sub-15-minute revisit with real-time tasking at a cost per maintained track that closes the maritime gap.
  - Status: assumption
  - Source type: secondary (internal draft assumption)
  - Source: Not stated in draft, §9, line 206 (unnumbered in rg output; adjacent to line 205/208).
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Same treatment as C035 — a defined threshold, not an empirical claim.

- Claim ID: C037
  - Service: Cross-service (falsifier / procurement tell)
  - Claim: "India's 70 to 100 aircraft requirement has to materialise as tenders and follow-on orders by roughly 2028."
  - Status: assumption
  - Source type: secondary (internal draft assumption)
  - Source: Not stated in draft, §9, line 208.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: The "2028" deadline is the author's inference, not a cited procurement schedule. Should be checked against any actual published tender timeline in Task 2.

- Claim ID: C061
  - Service: Cross-service (loss/attrition)
  - Claim: The Houthis claim 22 MQ-9 Reapers downed over Yemen since October 2023; US officials acknowledged at least 12 by March 2025 and seven losses in under six weeks during the spring 2025 campaign, at roughly USD 30 million per aircraft.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 6, "MQ-9 losses over Yemen."
  - Publisher: The War Zone; Associated Press
  - Published: 2025
  - URL: https://www.twz.com/news-features/what-air-defenses-do-the-houthis-in-yemen-actually-have ; https://apnews.com/article/houthis-us-warships-red-sea-e6e97a7131c48640ccf74b1916628234
  - Accessed: 2026-07-22
  - Drafting note: Keep Houthi claims separate from US-acknowledged losses. The draft's "over half a billion dollars" statement is based on the claimed 22 × USD 30 million, not the acknowledged count, and should not be presented as a confirmed US loss value.

- Claim ID: C062
  - Service: Cross-service (Operation Sindoor)
  - Claim: The 3P appendix describes 7–10 May 2025 as the first large-scale South Asian drone conflict and says Indian Harop, Nagastra-1 and SkyStriker strikes were guided in real time by Heron Mk II and TAPAS aircraft at standoff range, while Pakistani waves of 300–600 small drones were neutralised by layered air defence including upgraded L-70/ZU-23 guns.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 7. Carnegie supports general conflict-level lessons only and is explicitly excluded as support for the named Harop/Nagastra-1/SkyStriker/Heron Mk II/TAPAS claims. The 3P appendix points generally to The Hindu, ORF and CAPSS for platform-specific reporting but does not map each subclaim to a direct citation.
  - Publisher: The Hindu; Observer Research Foundation; CAPSS (platform-specific claims pending direct source mapping); Carnegie Endowment for International Peace (general context only)
  - Published: 2025
  - URL: https://carnegieendowment.org/russia-eurasia/research/2025/10/military-lessons-from-operation-sindoor ; https://www.thehindu.com/news/national/autonomous-warfare-in-operation-sindoor/article69633124.ece
  - Accessed: 2026-07-22
  - Drafting note: Keep `reported` pending direct verification of each platform-specific subclaim. Do not cite Carnegie for those details. The 3P body strengthens them into "found and fixed targets" and "steering ... in real time"; neither formulation may migrate until a supporting source is mapped claim by claim.

- Claim ID: C063
  - Service: Cross-service (operational inference)
  - Claim: Operation Sindoor demonstrates that large standoff UAS acted as the sensor and command layer while attritable drones acted as effectors, making the durable SCALE role "controller and C5ISR node, not penetrating strike."
  - Status: assumption
  - Source type: secondary
  - Source: Analytical inference in 3P Executive Summary and §§2/4, based on the reported events in C062.
  - Publisher: n/a
  - Published: July 2026 draft
  - URL: See C062.
  - Accessed: 2026-07-22
  - Drafting note: This is an investment-thesis inference, not a directly sourced operational fact. Preserve the permissive/standoff qualifier and do not generalise one conflict into universal mission validation.

- Claim ID: C064
  - Service: Cross-service (Baykar comparator)
  - Claim: By 2025 Baykar had TB2 contracts in 36 countries, Akıncı contracts in 16, more than 110 Akıncıs delivered, and a 60-aircraft Saudi order with a local production line.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 5, "Baykar 2025 results."
  - Publisher: Defensehere; Türkiye Today; Daily Sabah; Envanter Medya
  - Published: Early 2026
  - URL: https://defensehere.com/en/baykar-posts-2-2-billion-in-drone-exports-in-2025-retains-global-lead/
  - Accessed: 2026-07-22
  - Drafting note: The appendix bundles contract-country counts, deliveries and Saudi order scope across several outlets. Treat each as reported until checked against Baykar/Saudi primary announcements.

- Claim ID: C065
  - Service: Cross-service (competitive structure)
  - Claim: Most Indian bidders are partnered with foreign OEMs including Elbit, IAI and General Atomics; tender evaluation checks genuine platform IP, critical-subsystem localisation, and control over design, software and data systems.
  - Status: reported
  - Source type: secondary
  - Source: 3P §§3/6; apparently derived from Appendix item 2, but no exact tender-document citation is provided.
  - Publisher: idrw.org; Indian Defence News; unspecified ministry commentary
  - Published: 2025–2026
  - URL: https://idrw.org/indias-30000-crore-indigenous-male-uav-program-enters-crucial-evaluation-phase-after-rfp-deadline-closure/
  - Accessed: 2026-07-22
  - Drafting note: "Most" and the named selection criteria are material competition claims. They need the actual RFP or attributable ministry quotation before being stated as customer-published requirements.

---

## 10. Financial assumptions

- Claim ID: C038
  - Service: Cross-service (illustrative model, core assumptions)
  - Claim: The ten-year illustrative scenario uses: midpoint price ₹180 Cr per aircraft system; first delivery in Year 4; sustainment/software/spares at 10 percent of installed fleet value per year, beginning the year after each delivery; orders booked from Year 2.
  - Status: assumption
  - Source type: secondary (internal draft; self-labeled illustrative)
  - Source: §7, line 139: "Everything in this section is an illustration, never a forecast."
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Correctly labeled by the draft itself as illustrative, not a forecast. Inherits C023's price-anchor problem (₹180 Cr midpoint sits inside the disputed ₹150–210 Cr band).

- Claim ID: C039
  - Service: Cross-service (illustrative model, table arithmetic)
  - Claim: The ten-year revenue/backlog table (§7, lines 141–150) is internally consistent with its own stated assumptions.
  - Status: confirmed
  - Source type: primary (self-verifiable arithmetic within the document under audit)
  - Source: §7 table, lines 141–150, checked against the assumptions in C038.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Recomputed by hand during this audit: aircraft revenue = units delivered that year × ₹180 Cr; sustainment = prior-year closing fleet × ₹180 Cr × 10%; total = aircraft + sustainment; closing backlog = cumulative orders − cumulative deliveries, in ₹ Cr at ₹180 Cr/unit. Every cell in the table reproduces correctly from the stated rule. This is the one claim in the entire ledger that can honestly be marked `confirmed`, because the "citation" is the document's own disclosed formula and it holds up. It confirms only internal consistency, not that the underlying assumptions (C038) are realistic.

- Claim ID: C040
  - Service: Cross-service (illustrative model, pre-build test)
  - Claim: "In this scenario, six units ordered by end of Year 3 against one delivered in Year 4," illustrating a roughly 3× book-to-bill pre-build.
  - Status: confirmed
  - Source type: primary (self-verifiable arithmetic)
  - Source: §7 callout, line 154, checked against the table in C039.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Cumulative orders through Year 3 (0 + 3 + 3 = 6) against one aircraft delivered in Year 4 matches the table exactly. Confirmed as internally consistent, not as an externally validated procurement pattern.

- Claim ID: C041
  - Service: Cross-service (illustrative model, prose/table mismatch)
  - Claim: "On the illustrative fleet in §7, fourteen aircraft at ₹180 Cr, the annuity reaches ₹200 to 300 Cr of recurring annual revenue by Year 10."
  - Status: rejected
  - Source type: secondary (internal derivation checked against the draft's table)
  - Source: §6, line 129, checked against the §7 table (C039).
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: **Internal inconsistency flag.** The §7 table's actual "Sustainment & software" value at Year 10 is ₹198 Cr, not "200 to 300 Cr." A full-fleet run-rate calculation (14 aircraft × ₹180 Cr × 10% = ₹252 Cr) does fall in the stated range, so the sentence may be describing a steady-state run rate once all 14 aircraft are delivered and sustained a full year, rather than the Year 10 table value itself — but the draft does not say which, and ₹198 Cr (the actual Year 10 cell) is below the stated range either way. Rejected as currently worded; Task 6 must state explicitly whether this is the Year 10 table figure or a full-fleet run-rate figure, and correct the number or the label.

- Claim ID: C042
  - Service: Cross-service (cross-document financial model)
  - Claim: `business-case-male-uas.md`'s internal V4 model shows ~₹1,386 Cr recognized revenue and ~₹4,800 Cr closing backlog by Year 10, with 14 supporting units by Year 10, first ship in Year 4, win probability rising from ~0.20 to ~0.35, and a Year-1 book-to-bill target up to ~3.0.
  - Status: assumption
  - Source type: secondary (internal sibling business case, sourced to its own workbook)
  - Source: `business-cases/business-case-male-uas.md`, §4–§5.
  - Publisher: Internal workbook (`Defense_Platform_Business_Plan_Financial_V2.xlsx`).
  - Published: Not dated.
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: The "14 units by Year 10" figure matches this draft's own illustrative scenario (C038/C039) exactly, and the "~3.0 Year-1 book-to-bill" matches the pre-build logic in C040. This is useful cross-document corroboration of internal modeling consistency, but both figures plausibly trace to the same underlying illustrative construction rather than two independent estimates, so it should not be treated as independent validation.

- Claim ID: C043
  - Service: Cross-service (cross-document, self-flagged inconsistency)
  - Claim: `business-case-male-uas.md` itself flags two unresolved internal inconsistencies: "Y3 ₹33 Cr recognized vs Y4 first ship" needs reconciliation, and "Narrative Y10 ~₹900 Cr vs workbook ₹1,386 Cr — align IC materials."
  - Status: reported
  - Source type: secondary (self-reported by the sibling document's own "Open diligence — critical" section)
  - Source: `business-cases/business-case-male-uas.md`, §8, lines 131–132.
  - Publisher: Internal document.
  - Published: Not dated.
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Recorded for awareness only. This is a known, self-acknowledged issue in a document outside the scope of this task (the male-UAS case is read-only reference material here, not something this task modifies). Do not import either the ₹900 Cr narrative figure or the unreconciled Year 3 figure into the tri-service rewrite without independent resolution.

- Claim ID: C066
  - Service: Cross-service (3P illustrative model)
  - Claim: The 3P draft repeats the committed main draft's ten-year order, delivery, revenue, sustainment and backlog table unchanged, using ₹180 crore price, Year 4 first delivery and 10% support assumptions.
  - Status: assumption
  - Source type: secondary
  - Source: 3P §7 illustrative financial scenario.
  - Publisher: Internal draft.
  - Published: July 2026
  - URL: n/a (untracked local input)
  - Accessed: 2026-07-22
  - Drafting note: The arithmetic remains internally consistent as recorded in C039/C040. The price, timing and support inputs remain assumptions; the 3P source appendix does not convert them into confirmed facts.

- Claim ID: C067
  - Service: Cross-service (3P tender-share calibration)
  - Claim: The 3P draft says the scenario books 33 units across the decade, "almost exactly" the 36% minority share of the 87-aircraft tender (31 aircraft), and describes this as winning the second award slot.
  - Status: rejected
  - Source type: secondary
  - Source: 3P §7 narrative immediately before the financial table.
  - Publisher: Internal draft.
  - Published: July 2026
  - URL: n/a (untracked local input)
  - Accessed: 2026-07-22
  - Drafting note: The table books 33 units; 36% of 87 is 31.32. The gap is 1.68 aircraft (5.4% above 31.32), so "almost exactly" is subjective. More importantly, the model assumes orders before a tender win and treats the reported 64:36 award split as a percentage of units without a primary RFP. Label as illustrative entrant capture, not a transaction-calibrated or "not heroic" assumption.

- Claim ID: C068
  - Service: Cross-service (Baykar financial comparator)
  - Claim: Baykar reported USD 2.2 billion of exports in 2025, 88% of USD 2.5 billion revenue, and says 83% of cumulative revenue was earned abroad while development was internally funded.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 5, "Baykar 2025 results."
  - Publisher: Defensehere; Türkiye Today; Daily Sabah; Envanter Medya
  - Published: Early 2026
  - URL: https://defensehere.com/en/baykar-posts-2-2-billion-in-drone-exports-in-2025-retains-global-lead/
  - Accessed: 2026-07-22
  - Drafting note: Company-reported financial and cumulative-share figures should remain attributed to Baykar; they are a comparator, not an entrant forecast.

- Claim ID: C069
  - Service: Cross-service (post-conflict procurement)
  - Claim: After Operation Sindoor, Indian services earmarked a further ₹30,000 crore of emergency procurement for drones, counter-drone systems, loitering munitions and electronic warfare.
  - Status: reported
  - Source type: secondary
  - Source: 3P Appendix item 7, "Operation Sindoor."
  - Publisher: Carnegie Endowment for International Peace; The Hindu; Observer Research Foundation; CAPSS
  - Published: 2025
  - URL: https://www.thehindu.com/news/national/autonomous-warfare-in-operation-sindoor/article69633124.ece
  - Accessed: 2026-07-22
  - Drafting note: "Earmarked" does not establish allocation to SCALE/MALE aircraft. Keep this separate from the 87-aircraft programme and do not count it in SCALE demand.

- Claim ID: C070
  - Service: Cross-service (procurement falsifier)
  - Claim: The 3P draft assumes the 87-aircraft award must be decided and contracted through 2027, with follow-on tranches of the 97-to-350 requirement appearing behind it.
  - Status: assumption
  - Source type: secondary
  - Source: 3P §9 falsifier 4; no source in the appendix supplies this schedule.
  - Publisher: Internal draft.
  - Published: July 2026
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Treat 2027 as an author-defined monitoring trigger, not an official procurement milestone.

---

## 11. Claims removed or unresolved

### Required structural gaps (per task brief, recorded verbatim in substance)

1. The existing case opens with coastline and exclusive economic zone (C006), establishing the maritime frame before any other service is introduced.
2. The existing case uses maritime physics (endurance vs. transit time vs. antenna/radar power, §4) as its principal substitution argument against small drones, built entirely around a naval surveillance scenario (C008, C010).
3. The existing case treats navies as the natural first export customers (C011), asserted rather than tested, and pairs it with an unsupported generic "Gulf to Southeast Asia" market claim (C012).
4. The existing case gives no service-specific Army or Air Force demand model anywhere in its text (§2 and §3 above are both empty).
5. The existing case does not test whether one platform can meet all three services without commonality erosion; it defines a single-service (Navy-weighted) illustrative scenario (C038) and a platform-owner/shell-maker economic framework (C021) without ever asking whether Army- or Air Force-specific payload or qualification requirements would erode the shared-platform economics it assumes.

### Additional gaps and unresolved items found during this audit

6. **Traceability differs sharply by draft.** The committed main draft contains zero URLs, publisher names, or dated sources. The external 3P draft adds nine grouped appendix notes and links, but most bundle multiple claims and publishers without claim-level quotations, exact article titles/dates, or primary records. External claims therefore remain `reported`/`estimate`; only arithmetic self-checks C039/C040 are `confirmed` as internal consistency.
7. **Unresolved price-anchor arithmetic (C023).** The ₹150–210 Cr per-aircraft-system band and the "~USD 130 m per system-equivalent" figure in the same table cell are off by roughly an order of magnitude at any plausible INR/USD rate, because they mix a bare-aircraft rupee price with a full-program dollar cost-per-equivalent. Must be rebuilt in Task 6 with each figure's scope stated explicitly.
8. **Unresolved slip-deferral conflict across sibling documents (C025 vs. C028).** This draft says a 12-month certification slip defers ₹180–540 Cr/year; the sibling `business-case-male-uas.md` says the same event defers "~₹150–210 Cr/yr." These describe different quantities (a delivery-ramp deferral vs. a single-unit price) but are used as if interchangeable. Must be recomputed consistently in Task 6.
9. **Sustainment-annuity prose/table mismatch (C041).** The draft's own text claims the sustainment annuity "reaches ₹200 to 300 Cr ... by Year 10," but its own table shows ₹198 Cr at Year 10. Needs correction or relabeling as a post-Year-10 steady-state figure.
10. **Cross-document margin-framing tension (C026 vs. C029).** This draft's own "BoM-margin trap" callout warns against quoting BoM-only gross margin (~70%) as a headline figure; the sibling `business-case-male-uas.md` does exactly that (quotes ~71% BoM-only GM without a fully loaded figure alongside it). Should not be repeated in the tri-service rewrite.
11. **Export evidence remains inadequate (§7, §8).** There is no country-specific Indo-Pacific evidence. The only Gulf transaction is the reported Saudi Akıncı order (C064), with insufficient scope or market-access detail for an Indian entrant.
12. **Tri-service allocation concern resolved, demand-model gap remains.** The external 3P draft explicitly supplies the 15 Navy / 8 Army / 8 Air Force MQ-9B allocation (C045, C049, C051). It still provides no Army- or Air Force-specific mission case or demand model and gives no service allocation for the 87-, 97-, or projected 350-platform figures.
13. **Tender-status precision.** The 87-aircraft programme, 64:36 split, bidder count, 97 requirement and 350 projection (C046–C048) rely in the appendix on low-transparency defense sites rather than linked MoD/DAC/RFP records. Keep `reported`, separate tendered quantity from projections, and do not say the structure "guarantees" two winners.
14. **Scenario-to-tender calibration is overstated (C067).** The 33-unit illustrative order book is not equal to 36% of 87 (31.32), and the draft lacks primary support for treating 64:36 as an exact unit split. This must remain an illustrative entrant-capture assumption.
15. **Operational reporting needs claim-level checking (C061–C063).** Houthi claims must remain separate from US-acknowledged MQ-9 losses; Operation Sindoor sensor-to-shooter assertions bundle several sensitive details and should not exceed the exact public sources.
16. **`business-case-male-uas.md` self-flagged inconsistencies (C043)** remain unresolved in that document and are out of scope for this task's edits; recorded here only so the rewrite does not inadvertently import the disputed figures.
