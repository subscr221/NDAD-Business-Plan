# SCALE UAS tri-service evidence ledger

## Purpose and scope note

This ledger audits every material claim in the current SCALE UAS investor case
(`_bmad-output/business-case-scale-uas-investor.md`) against the citations that
document actually provides, and cross-checks a small set of overlapping claims
in the sibling MALE UAS company business case
(`business-cases/business-case-male-uas.md`).

**Deviation from the task-1 brief, recorded for the record:** the brief and the
implementation plan both instruct auditing
`_bmad-output/business-case-scale-uas-investor.REWRITE-DRAFT-3P.md`. That file
does not exist anywhere in this worktree (confirmed by a recursive search for
`*REWRITE*`). The only existing draft in `_bmad-output/` that matches the
"current, coastal-led SCALE UAS investor case" described in the design spec
(`docs/superpowers/specs/2026-07-22-tri-service-scale-uas-business-case-design.md`)
is `_bmad-output/business-case-scale-uas-investor.md`. This ledger audits that
file instead, and the Step 4 verification command below was run against that
file for the same reason. No file was invented to satisfy the brief's literal
path; see the report for this task for the recommended follow-up.

**Headline finding:** the current draft contains no inline citations, URLs,
publisher names, or publication dates anywhere in its body text. The only
"sourcing" it offers is a handful of short parenthetical or table-cell
descriptions (e.g. "Analyst consensus range", "Government-published
transaction", "Publicly reported tri-service requirement", "Derived from the
2024 India MQ-9B transaction"). None of these descriptions link to a
verifiable primary or secondary source. Per the audit rule in the brief
("mark `confirmed` only if the existing citation directly supports it"), **no
claim in the current draft qualifies as `confirmed`**, because no claim has an
actual citation to check against. This is the single most important
structural gap this ledger records, and it is carried into
§11.

Claim IDs are sequential (`C001`, `C002`, ...) across the whole ledger.
"Source" records what the draft itself says about provenance, verbatim or
closely paraphrased, not an externally verified citation. Where the draft
gives nothing at all, Source/Publisher/Published/URL are marked "Not stated
in draft." No URL, publisher, or date has been invented for this ledger.

**Explicit exclusions from claim-by-claim coverage (Step 4 categories):** the
following recur throughout the draft and are not logged as individual claims
because they are definitions, section headings, reader-facing verification
prompts, or narrative restatements of a table already logged elsewhere:
the SCALE/C5ISR/MALE/MUM-T/P-8I glossary entries; every "**What to
verify:**" callout (these instruct the reader what to check, they do not
themselves assert a fact); the §7 prose passage restating the shape of the
ten-year table already captured as C039; and the diligence-scorecard
checklist items in the original §10, which restate figures already logged
under C003, C019, C022, C023, C026, and C038–C040 rather than introducing
new claims.

---

## 1. Cross-service procurement and allocations

- Claim ID: C001
  - Service: Tri-service / cross-service
  - Claim: In 2024 the Government of India signed for 31 MQ-9B aircraft at roughly USD 4 billion.
  - Status: reported
  - Source type: uncited (draft presents as fact with no attribution)
  - Source: Not stated in draft. Referenced again at lines 16 and 46 of the source file with identical wording.
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: Plausible and widely reported externally, but the draft itself cites nothing. Needs a primary MoD/PIB/US DSCA source in Task 2 before it can be marked confirmed.

- Claim ID: C002
  - Service: Tri-service / cross-service (Navy-weighted)
  - Claim: The Indian Navy took the largest share of the 31-aircraft MQ-9B order; no numeric Navy/Army/Air Force split is given.
  - Status: reported
  - Source type: uncited
  - Source: Not stated in draft.
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: This is the draft's only tri-service allocation statement, and it is a qualitative "largest share" claim, not a quantified split. The implementation plan's Task 2 references a "15 Navy / 8 Army / 8 Air Force" allocation; that figure appears nowhere in this draft or in `business-case-male-uas.md`, so it is not recorded here as a claim of this draft. It must be sourced independently in Task 2, not assumed from this ledger.

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
  - Claim: [Structural gap, not a sourced claim] Neither the 31-aircraft MQ-9B buy nor the 70–100 aircraft decade requirement is broken out by service anywhere in the current draft.
  - Status: rejected
  - Source type: uncited
  - Source: Absence noted across the full document.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Rejected as a data point because it is an absence, not a claim; recorded here so Task 2 knows a service-level allocation must be built from scratch rather than lifted from this document.

- Claim ID: C044
  - Service: Tri-service / cross-service (procurement policy)
  - Claim: "India's indigenisation regime, positive-indigenisation lists and import-substitution mandates, keeps closing the home market to foreign airframes"; the 2024 MQ-9B buy "reads best as a stopgap purchased while the domestic pipeline matures, and the stated ambition on the record remains a sovereign platform."
  - Status: assumption
  - Source type: uncited (policy fact stated without citation; "reads best as" and "stated ambition on the record" are the author's interpretation)
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
  - Drafting note: This corroborates C001/C003 only in the sense that two internal documents agree; it is not independent external verification, since both likely trace to the same unsourced internal figure. Do not treat repetition across internal documents as confirmation.

---

## 2. Indian Army missions and programmes

- No claims found. The current draft contains no Army-specific mission, requirement, programme, or procurement statement anywhere in its body. This confirms the structural gap recorded in §11 ("gives no service-specific Army ... demand model"). Task 2 must build this section from new research; nothing here can be inherited from the current draft.

---

## 3. Indian Air Force missions and programmes

- No claims found. The current draft contains no Air Force-specific mission, requirement, programme, or procurement statement anywhere in its body, beyond the generic, service-unspecified "IAF" mention that does not actually occur (the draft never names the Air Force at all). This confirms the structural gap recorded in §11 ("gives no service-specific ... Air Force demand model"). Task 3 must build this section from new research.

---

## 4. Indian Navy missions and programmes

- Claim ID: C006
  - Service: Navy
  - Claim: India has 7,500 kilometres of coastline and an exclusive economic zone of 2.4 million square kilometres.
  - Status: reported
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
  - Source: Not stated in draft, §8, line 184.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: A generic geographic assertion, not tied to any named country, transaction, or requirement. This is exactly the kind of "coloured map" claim the draft's own §8 callout warns against ("an export thesis that starts with navies ... rather than a coloured map"), yet the draft does it anyway. No country-level evidence exists to promote this to Indo-Pacific/Gulf sections (§7, §8 below).

---

## 5. Common-platform architecture and qualification

- Claim ID: C013
  - Service: Common platform
  - Claim: A SCALE UAS is defined as a 1-to-5-tonne-class aircraft with 24-to-40-hour endurance.
  - Status: assumption
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
  - Source: Draft states "checkable against published sustainment contracts" (§6, line 129) but names none.
  - Publisher: Not stated in draft.
  - Published: Not stated in draft.
  - URL: Not stated in draft.
  - Accessed: 2026-07-22
  - Drafting note: Explicitly flagged as a sustainment percentage by the audit brief. The draft asserts it is checkable but does not check it. Repeated at lines 48, 129, 235. Needs a named contract or industry benchmark citation.

- Claim ID: C020
  - Service: Common platform
  - Claim: Service life in this class runs 25 years.
  - Status: assumption
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
  - Source: Not stated in draft, §7, line 168.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: Industry-benchmark style figure with no named source. Repeated in the diligence scorecard at line 242.

---

## 6. Indian transactions and pricing

- Claim ID: C023
  - Service: Cross-service (pricing anchor)
  - Claim: Price anchor is ₹150–210 Cr per aircraft system (~USD 130 m per system-equivalent), "derived from the 2024 India MQ-9B transaction: 31 aircraft, ~USD 4 bn including weapons, ground stations and support."
  - Status: rejected
  - Source type: uncited (draft calls this "derived," not sourced)
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
  - Source type: uncited (internal model derivation)
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
  - Source type: uncited
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
  - Source type: uncited
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

---

## 7. Indo-Pacific export markets

- No claims found. The current draft never names a specific Indo-Pacific country, transaction, requirement, or platform. The only related statement is the generic "coastal states from the Gulf to Southeast Asia" line recorded as C012 above, which contributes no country-level evidence and is explicitly flagged there as an unsupported "coloured map" claim. Task 5 must build this section entirely from new research.

---

## 8. Gulf export markets

- No claims found. As with §7, the only related statement is the generic Gulf/Southeast Asia mention recorded as C012. No Gulf-specific country, requirement, transaction, or platform is named anywhere in the current draft. Task 5 must build this section entirely from new research.

---

## 9. Competition and substitutes

- Claim ID: C030
  - Service: Cross-service (competitive field)
  - Claim: Five incumbent platforms are named with positioning claims: GA-ASI MQ-9B (USA, "incumbent in India as of the 2024 buy"); Baykar TB2/Akıncı (Turkey, "export template ... now repositioning Akıncı as a drone controller"); IAI Heron/Heron-TP (Israel, "long-serving legacy fleet in India"); Elbit Hermes 900 (Israel, "strong export footprint with dedicated maritime variants"); CASC Wing Loong II (China, "price-led exporter ... excluded from India on political grounds").
  - Status: reported
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
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
  - Source type: uncited
  - Source: Not stated in draft, §9, line 208.
  - Publisher: n/a
  - Published: n/a
  - URL: n/a
  - Accessed: 2026-07-22
  - Drafting note: The "2028" deadline is the author's inference, not a cited procurement schedule. Should be checked against any actual published tender timeline in Task 2.

---

## 10. Financial assumptions

- Claim ID: C038
  - Service: Cross-service (illustrative model, core assumptions)
  - Claim: The ten-year illustrative scenario uses: midpoint price ₹180 Cr per aircraft system; first delivery in Year 4; sustainment/software/spares at 10 percent of installed fleet value per year, beginning the year after each delivery; orders booked from Year 2.
  - Status: assumption
  - Source type: uncited (self-labeled illustrative)
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
  - Source type: uncited (internal derivation, checked against the same document's own table)
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

---

## 11. Claims removed or unresolved

### Required structural gaps (per task brief, recorded verbatim in substance)

1. The existing case opens with coastline and exclusive economic zone (C006), establishing the maritime frame before any other service is introduced.
2. The existing case uses maritime physics (endurance vs. transit time vs. antenna/radar power, §4) as its principal substitution argument against small drones, built entirely around a naval surveillance scenario (C008, C010).
3. The existing case treats navies as the natural first export customers (C011), asserted rather than tested, and pairs it with an unsupported generic "Gulf to Southeast Asia" market claim (C012).
4. The existing case gives no service-specific Army or Air Force demand model anywhere in its text (§2 and §3 above are both empty).
5. The existing case does not test whether one platform can meet all three services without commonality erosion; it defines a single-service (Navy-weighted) illustrative scenario (C038) and a platform-owner/shell-maker economic framework (C021) without ever asking whether Army- or Air Force-specific payload or qualification requirements would erode the shared-platform economics it assumes.

### Additional gaps and unresolved items found during this audit

6. **No citations anywhere.** The current draft contains zero URLs, publisher names, or dated sources in its body text. Every material claim audited above is `reported`, `estimate`, `assumption`, or `rejected`; none is `confirmed` against an external source (only the two purely arithmetic self-checks, C039 and C040, could be confirmed, and only as internal consistency, not external validity).
7. **Unresolved price-anchor arithmetic (C023).** The ₹150–210 Cr per-aircraft-system band and the "~USD 130 m per system-equivalent" figure in the same table cell are off by roughly an order of magnitude at any plausible INR/USD rate, because they mix a bare-aircraft rupee price with a full-program dollar cost-per-equivalent. Must be rebuilt in Task 6 with each figure's scope stated explicitly.
8. **Unresolved slip-deferral conflict across sibling documents (C025 vs. C028).** This draft says a 12-month certification slip defers ₹180–540 Cr/year; the sibling `business-case-male-uas.md` says the same event defers "~₹150–210 Cr/yr." These describe different quantities (a delivery-ramp deferral vs. a single-unit price) but are used as if interchangeable. Must be recomputed consistently in Task 6.
9. **Sustainment-annuity prose/table mismatch (C041).** The draft's own text claims the sustainment annuity "reaches ₹200 to 300 Cr ... by Year 10," but its own table shows ₹198 Cr at Year 10. Needs correction or relabeling as a post-Year-10 steady-state figure.
10. **Cross-document margin-framing tension (C026 vs. C029).** This draft's own "BoM-margin trap" callout warns against quoting BoM-only gross margin (~70%) as a headline figure; the sibling `business-case-male-uas.md` does exactly that (quotes ~71% BoM-only GM without a fully loaded figure alongside it). Should not be repeated in the tri-service rewrite.
11. **No Indo-Pacific or Gulf country-level evidence (§7, §8).** The only related material is a single generic sentence (C012) naming no country, transaction, or requirement. Task 5 starts from zero on this axis.
12. **No tri-service allocation for the headline procurement figures (C002, C004).** Neither the 31-aircraft MQ-9B buy nor the 70–100 aircraft decade requirement is broken down by service in this draft. The "15 Navy / 8 Army / 8 Air Force" figure referenced in the implementation plan's Task 2 does not appear in this draft or in `business-case-male-uas.md`, so it has not been recorded here as an audited claim; it must be independently sourced, not assumed to exist because the plan mentions it.
13. **`business-case-male-uas.md` self-flagged inconsistencies (C043)** remain unresolved in that document and are out of scope for this task's edits; recorded here only so the rewrite does not inadvertently import the disputed figures.
