# A home you can keep: specification

Role: section 4 of the housing dossier. It writes each design Espen has decided as provisions: what each does, its parameters, who is eligible, amounts and timing, the vehicle, the agency, how it changes current law, and the evidence it rests on. Provision IDs and their fields are in `provisions.json`. Status: draft (stage C, step 5). It builds on Espen's section 3 decisions (`DEC-2026-11-09-01` to `-06`) and on the later November 9 decisions (`-08` to `-11`): the tax credits (option D, written as HOU-2D), the capital timing, the design directions from sections 5-7, the data rule and stage 2's exit line. Those decisions are recorded in `charter/decisions.md`. The doubled-up question was decided after this pass began (`DEC-2026-11-09-12`); HOU-4.03 and HOU-4D.01 state it; PR #141's count is on main, and section 6 prices stage 2's wider entry from it (`6-cost.md`, 2.7). Espen then decided the parameters this section had proposed (`DEC-2026-11-09-14`, `DEC-2026-11-09-16`, `DEC-2026-11-09-17`). Costs: this section cites figures that exist in the ledger, the budget model, the legacy domain file or section 6 (`6-cost.md`), which prices every provision. Where a parameter rests on judgment and not on evidence or a decision, it says so. Where a decision leaves a parameter open, it is marked **proposed, for Espen**, with its basis.

## How to read this section

- **Status of each provision.** *Decided* means Espen decided the design. *Legacy working choice* means it was carried over as `chosen` and section 3 did not re-weigh it (`DEC-2026-10-30-02`). *Pending* means it waits on research. *Open* means it waits on Espen. *Proposed, for Espen* marks a parameter that a decision left open; it is this section's proposal, not a decision.
- **Vehicles.** R2 is the reconciliation bill on the FY2030 budget resolution, which carries housing under the legacy decision D5 (`3-design.md`, "Starting points"). In the scenario calendar's central runs, half pass it by about October 30, 2029 and the rest by about January 14, 2030. Its runs span May 2029 to December 2030, and in difficult runs it does not pass (`5-delivery.md`, 3). R3 is a later reconciliation bill. A *regular bill* passes under the Senate's ordinary rules or the D2 rules change. *Appropriations* are the yearly discretionary bills. Reconciliation can carry only spending and revenue. So a rule with no budget effect, such as a fair-housing protection, a data-privacy rule or a change to who may apply for an existing program, goes in a regular bill even when its money rides R2. Where a program has both a mandatory part and an appropriated part, the provision names each part. Section 6 enters them in the budget model as `split` rows (`models/tools/budget/provisions.md`; `models/data/budget/provision-splits.csv`, which has no row yet). Changing a row's booking is an adopted-input change (tier 3) made in B6, so this section changes no model file.
- **Dates.** The calendar years in this section are the plan's targets. In the statute, each start date runs from enactment, with a latest date: for example, first awards within six months of enactment. Each award year's money stays available until spent, so a late R2 does not lose a year. This follows section 5 (`5-delivery.md`, 3).
- **Agency.** HUD runs everything here unless a provision says otherwise. HUD's capacity is a section 5 question (`road-act.md`, "HUD's load").
- **Shared rules** are written once, in HOU-4.01. Every other provision points there.
- **Design lens** (`DEC-2026-11-09-13`: guide, don't police). Each test, document, deadline, cap or quota below should earn its place against the burden it adds. This pass made these changes:
  1. *Stage 1's test* is one plain test with no cap, shown by the family's word or a school record (HOU-4.03; decided in `DEC-2026-11-09-12`).
  2. *Order within a stage* follows local need-based intake. Memo 2's order (severity, youngest children, date), which memo 2 B set for stage 2 (`DEC-2026-11-09-01`), becomes national guidance, not a rule, in stages 2 and 3 (HOU-4.03; decided, `DEC-2026-11-09-14`). It matters only while stage 2's 300,000-a-year cap binds (2034-36).
  3. *Stage 2's severe-problems test* is shown by the family's own statement of rent and conditions, with income found once, and checked after award (HOU-4D.01; section 4's judgment, following section 5's self-certification).
  4. *The duty to house* has a deadline for the agency, not a cutoff for the family: offers continue until the family is housed (HOU-4D.01; decided, `DEC-2026-11-09-14`).
  5. *Stage 3's disability test* accepts records the government already holds, such as SSI, SSDI or Medicaid disability coverage, as proof (HOU-4.08; decided, `DEC-2026-11-09-14`; the full definition is still set with the care flagship).
  6. *The emergency fund's episode limits* (one in 12 months, two in three years; point 5, rule 3) give way to an annual cap per household, usable across any number of crises, and a published count of repeat use with a review trigger, since a household in its third crisis is often the one most at risk (HOU-1D.01; decided, `DEC-2026-11-09-16`, `DEC-2026-11-09-17`).
  Requirements kept because they earn their place: the agency-side deadlines and reallocation rules (section 5), which bind agencies, not households; the middle-income credit's market-rent check, which decides whether the credit buys anything (HOU-2D.02, decided); and the landlord ownership check before payment, which stopped the 2021 program's main fraud (HOU-1D.02, decided).

## The provisions at a glance

| ID | Provision | Status | Vehicle |
| --- | --- | --- | --- |
| HOU-4.01 | Shared rules for all housing help (income, income lines, immigrant eligibility, verification, conditions), with the mixed-status protection | Decided by reference; working answers per `shared-rules.md`; mixed-status protection decided (`DEC-2026-11-09-10`) | Regular bill (definitions) and R2 (as conditions on the new money) |
| HOU-4.02 | One rental help system: the guarantee, vouchers and emergency rent help harmonized | Decided (memo 8); the record's contents and enforcement bar (`DEC-2026-11-09-11`); R1 readiness money (`-10`) | R1 (readiness); R2 (money and conditions); regular bill (data sharing and privacy) |
| HOU-4.03 | The order of reach | Decided (memo 8; point 7; stage 1's test `DEC-2026-11-09-12`) | R2 |
| HOU-4.04 | Matching the tool to the market: tight-market rule, attached help, right to move | Decided (memo 1 B) | R2 |
| HOU-4.05 | Payment limits by neighborhood | Decided (point 1) | Regular bill or HUD rule; no new money |
| HOU-4.06 | National source-of-income protection, with testing money for 2030-34 | Decided (point 2; testing money `DEC-2026-11-09-10`) | Regular bill; R2 (testing money) |
| HOU-4.07 | Search help with every new award | Decided (point 3); design research open | R2 (mandatory fee); appropriations (evaluation) |
| HOU-4.08 | Stage 3: extremely low-income renters with long-term disabilities, from 2038 | Decided (memo 2 condition); definition and services with the care flagship | R2 (authorized now, effective 2038); section 6 and the financing settlement |
| HOU-4.09 | Housing First as the federal rule for homelessness help, with the no-sweeps condition | Decided (memo 5 B; no-sweeps condition `DEC-2026-11-09-10`) | Executive action (January 2029); regular bill |
| HOU-4.10 | A voluntary recovery-housing option, evaluated | Decided (memo 5 B) | R2 (mandatory, time-limited); appropriations |
| HOU-4.11 | Supportive housing: an engagement standard (a duty on providers) and treatment access | Decided (memo 5 B; parameters adopted, `DEC-2026-11-09-10`) | Executive action and rule (2029); regular bill |
| HOU-4.12 | Services and workforce for supportive housing | Decided (parameters and the wider backstop through 2035, `DEC-2026-11-09-10`) | Care flagship's bill (Medicaid); R2 (HUD backstop) |
| HOU-4.13 | Tribal housing: set-asides, through tribes, by self-determination | Decided (`DEC-2026-11-09-10`; sizes `DEC-2026-11-09-16`) | R2 (set-asides); regular bill (NAHASDA rules) |
| HOU-4A.01 | One million new awards, 2030-33 (stage 1 and the start of stage 2) | Decided (memos 1, 2, 8) | R2, mandatory |
| HOU-4A.02 | Housing agency administration for the new awards | Decided with HOU-4A (legacy allowance) | R2, mandatory |
| HOU-4D.01 | Stage 2: a guarantee for the poorest families with children, enrolled 2034-37, with the duty to house from 2037 | Decided (memo 2 B; duty to house and remedies `DEC-2026-11-09-10`; exit line `-11`) | R2, mandatory |
| HOU-1D.01 | Standing emergency-rent fund: eligibility, uses and caps | Decided (memo 6 C; point 5 rules 1 and 3; point 4) | R2, mandatory |
| HOU-1D.02 | How the fund pays: risk screen, self-attestation and checks, landlord applications | Decided (point 5 rules 2, 4, 5) | R2 |
| HOU-1D.03 | Accountability: grantee network, payment-error measurement, data standard | Decided (point 5 rules 6-8) | R2 (money and conditions); regular bill (privacy and record links) |
| HOU-1D.04 | The one-time start, 2030-31 | Decided (memo 6 C) | R2, mandatory |
| HOU-3C.01 | State housing revolving funds: about $72 billion of grants, awarded by 2037 | Decided (memo 3 part 3 B; timing `DEC-2026-11-09-09`) | R2, mandatory (borrowed inside the D4-B envelope, C21) |
| HOU-3C.02 | Federal construction and acquisition loans: $300 billion, committed by 2038 | Decided (memo 3 part 3 B; timing `DEC-2026-11-09-09`) | R2 (credit subsidy) |
| HOU-3C.03 | Lasting affordability, attached help and accessible homes in plan-financed buildings | Decided (memo 3 part 3 B; memo 1 B; memo 2 condition; tax-credit homes `DEC-2026-11-09-08`) | R2 (grant and loan conditions) |
| HOU-3C.04 | Published production targets: homes the plan pays for, homes in zoning-reward places, and a national goal | Decided (`DEC-2026-11-09-10`; three numbers `DEC-2026-11-09-14`; the numbers `DEC-2026-11-09-17`) | Regular bill (the targets); R2 (reporting conditions) |
| HOU-5.01 | Public housing repair | Legacy working choice; timing `DEC-2026-11-09-09` | R2, mandatory (C31) |
| HOU-5.02 | Repair first, one-for-one replacement and a right to return with no re-screening | Decided (point 6) | Regular bill; R2 (conditions on the repair money) |
| HOU-6.01 | The zoning reward through the ROAD to Housing Act's Innovation Fund | Decided (memo 4 B) | R2 (money); regular bill (who may apply, what is paid for) |
| HOU-6.02 | The condition on new transportation money | Decided (memo 4 B) | Regular bill (Moving America's 2031 authorization) |
| HOU-7B.01 | The investor limit left as enacted | Decided (point 8) | None |
| HOU-8.01 | Social housing pilot | Legacy working choice | R2 (through HOU-3C.02 and a small equity grant) |
| HOU-9A.01 | A small federal builder from 2029 | Decided (memo 3 part 2, A-small) | Regular bill (the corporation); R2 (capital and loan authority) |
| HOU-2D.01 | A bigger low-income credit with the boost for the poorest renters | Decided (memo 3 part 1 D, `DEC-2026-11-09-08`) | R2 (revenue) |
| HOU-2D.02 | A middle-income credit in high-cost areas, a 2030-34 trial | Decided (`DEC-2026-11-09-08`) | R2 (revenue) |
| HOU-2D.03 | The neighborhood homes credit, a 2030-34 trial | Decided (`DEC-2026-11-09-08`) | R2 (revenue) |
| HOU-2D.04 | Permanent affordability for every rental home the plan pays for | Decided (`DEC-2026-11-09-08`) | R2 (credit conditions); regular bill |

## 1. Rules shared by all housing help

### HOU-4.01 Shared rules, kept in one place

Every provision below that tests income, status or need uses the definitions here. Each rule's owner dossier can change it without a rewrite (`shared-rules.md`).

| Rule | Working answer in this dossier | Range tested | Owner |
| --- | --- | --- | --- |
| Income for rent (shared rule 1) | Current law: tenants pay 30% of adjusted income (42 U.S.C. 1437a(a)(1)). Refundable tax credits paid in advance, the child tax credit included, are not income (26 U.S.C. 6409). Assume no new benefit from another flagship raises rent | No effect, up to 30 cents per dollar of any new benefit paid outside the tax code | Secure floor (flagship 1) |
| How fast help falls (rule 2) | 30 cents per added dollar of adjusted income. Increases in earnings are counted at the annual review. No new phase-out | Set by the secure floor's ceiling on combined phase-out rates | Secure floor, with the household model |
| Immigrant eligibility (rule 3) | Current law for HOU-4 and HOU-4A/4D: Section 214's list (42 U.S.C. 1436a), with help prorated for mixed-status families, protected as below (`DEC-2026-11-09-10`). HOU-1D's rule is set by the immigration flagship's eligibility table; this section does not fix it | Section 214 up to the immigration flagship's table for new statuses | Immigration (flagship 6) |
| Income lines (rule 4) | Area median income. "Extremely low income" is the statutory line (1437a(b)(2)(C)). The emergency fund uses 50% of area median income or enrollment in a means-tested program (HOU-1D.01) | — | Secure floor (definitions); democratic renewal (common application) |
| Verification (rule 5) | Housing agencies verify, reusing income already found by TANF, Medicaid or SNAP (1437a(a)(7)(D)) and federal income-matching data (1437a(a)(7)(E)). HOU-4.02 extends reuse across the three housing programs | — | Democratic renewal (CAP-13) |
| Conditions (rule 6) | No work condition and no treatment condition on any housing help in this dossier (memo 5 B). The public housing community-service rule (42 U.S.C. 1437j(c)) does not apply to households housed under HOU-4A, HOU-4D or HOU-4.08 | — | Work (flagship 5) records the cross-program principle |
| Services (rule 7) | Services come through Medicaid and local programs. Housing pays only a services backstop for supportive-housing tenants without Medicaid (HOU-4.12) | — | Care (flagship 2, HLT-4) |
| Residency | No residency requirement and no preference by length of residence in any new program (point 7), as the voucher rules already require (24 CFR 982.207) [EV-HOU-189] | — | This dossier |

- **Mixed-status protection** (`DEC-2026-11-09-10`). A mixed-status family keeps prorated help for its eligible members for as long as it is otherwise eligible, as current regulations allow, and a member may decline to contend eligible status without ending the others' help. HUD's February 2026 proposed rule would make proration temporary, pending verification of every member [EV-HOU-402]; a HUD analysis of the draft found about 20,000 assisted mixed-status families affected, 16,000 with children, as reported [EV-HOU-403]. The executive action of January 2029 withdraws the proposed rule, or rescinds it if it is final by then. The regular bill writes both protections into Section 214 (42 U.S.C. 1436a), so a later rule cannot undo them. Espen's decision says the repeal may be in statute ("possibly in statute"); this section writes it there, as section 7 recommended (`7-validation.md`, 3.4). Executive action alone is the alternative. The immigration flagship still owns the wider eligibility table (rule 3).
- **Vehicle.** The definitions are restated in a regular bill. In R2 they appear as conditions on the new money, which reconciliation can carry.
- **Changes to current law.** None to 1437a. Section 214 gains the mixed-status protection. The community-service rule binds only public housing residents, so it already misses voucher households. The new subsection disapplies 1437j(c) for households whose award is attached to a public housing unit, in redevelopment under HOU-5.02 or a social housing building. It rides the regular bill, because it has no budget effect.
- **Open check.** The voucher tenant-payment rule (42 U.S.C. 1437f(o)) is not yet read (`shared-rules.md`, "Open checks"). Section 5 reads it before writing rent rules for attached awards.

### HOU-4.02 One rental help system

Espen asked that the guarantee, the vouchers and emergency rent help be "harmonized across use cases and access points" (`DEC-2026-11-09-06`). They stay three funding lines with three purposes, but the renter meets them as one system.

| Use case | Program | What the renter gets |
| --- | --- | --- |
| Short crisis: arrears, a notice, a shutoff, a disaster | HOU-1D | One-time help, a month or two of rent, legal help |
| No home, or a lasting gap between income and rent, in the covered groups | HOU-4A, then HOU-4D, then HOU-4.08 | Long-term help: a voucher, or an award attached to a home in a tight market |
| No home, with high service needs | HOU-4A awards under HOU-4.09, with HOU-4.10 and HOU-4.11 | Housing first; services offered; a sober setting if chosen |
| Outside every covered group, with severe needs | Existing vouchers and waiting lists | No new entitlement in the 2030s (memo 2 B) |

**Parameters.**
1. **One application.** A single federal housing application with one record per household, run by the housing agency or the emergency-fund grantee in each place. An emergency-fund applicant is screened at the same time for the guarantee, and a guarantee applicant for emergency help. Judgment: this design follows Espen's direction; no evaluation of a common housing application is in the register.
2. **Access points.** The emergency-fund grantee (HOU-1D.03), the housing agency, the homelessness system's coordinated entry, and eviction court through the grantee's link to it. Each can start the common application. "No wrong door" is judgment.
3. **Hand-offs.**
   - *Emergency to long-term.* A household paid by HOU-1D that is in a covered group of the guarantee is enrolled under HOU-4.03's order without a new application.
   - *Repeat need.* A household with a second crisis within 12 months, or that reaches HOU-1D's annual cap (HOU-1D.01), is referred to the guarantee or to the housing agency's waiting list.
   - *Attached to tenant-based.* A household in an attached home can move with a voucher (HOU-4.04), with search help (HOU-4.07).
   - *Homelessness to housing.* Coordinated entry refers each household straight into the order of reach.
   - *Health and benefits.* The common application offers enrollment in Medicaid and the child tax credit's monthly payments (section 7 checks reach; see "Interactions").
4. **Data.** One household record format across HOU-1D and the new awards, using HOU-1D.03's payment-level standard. It carries a protected household identifier, so duplicates and hand-offs can be traced. Records are reused only where law allows (rule 5) and under the privacy rules in the regular bill.
   - *What the record holds* (`DEC-2026-11-09-11`): only the basic information collected for every applicant, where possible: identity, household members, address and tract, income and how it was found, program, dates and payments. It holds no citizenship or immigration status. Where Section 214 requires a status finding to prorate help, the housing agency keeps the finding and the record carries only its result, the number of eligible members and the prorated amount (decided, `DEC-2026-11-09-14`).
   - *No immigration enforcement use* (`DEC-2026-11-09-11`). The regular bill bars any use or sharing of the record, or of information collected on the application, for immigration enforcement, with penalties for misuse. This rule governs the record whatever a later verification rule says (section 7, 3.4). Penalties follow the model of the tax code's protection (`DEC-2026-11-09-14`) of taxpayer information, which makes unauthorized disclosure a crime and gives the person harmed a civil damages claim (26 U.S.C. 7213 and 7431; not yet in the register).
5. **Income found once.** An income finding made by any of the three programs, or by TANF, Medicaid or SNAP, counts for the others for 12 months (an extension of 1437a(a)(7)(D)). The 12-month window is judgment.
6. **Until the regular bill passes.** R2 funds the data system. Programs share records under current law only with the household's written consent on the common application (`5-delivery.md`, 4).
7. **Readiness money in R1** (`DEC-2026-11-09-10`). A readiness tranche in the first reconciliation bill (February 2029), mandatory and available until spent, for HUD's data system, the common application, hiring and the grantee rules, so the 2030 awards are not lost if R2 runs into 2030 (`5-delivery.md`, 3). The amount is $0.75 billion (`DEC-2026-11-09-14`), section 6's estimate (`6-cost.md`, 1.2). If R1's scope cannot carry it, FY2029 appropriations are the fallback (section 5, question 1).

- **Vehicle.** R1 carries the readiness tranche. The money for systems and grantees then rides R2 inside each program's administration allowance (HOU-4A.02; HOU-1D.03). The data-sharing authority, the privacy rules and the enforcement bar go in a regular bill.
- **Agency.** HUD runs all three programs. This is a section 4 choice: memo 6 and the point 5 note leave the fund's agency open, and one agency is what makes one application and one record possible. The alternative is Treasury, which ran the 2021-22 Emergency Rental Assistance program [EV-HOU-150]. Section 5 tests HUD's capacity for it.
- **Evidence.** The need for one data standard and one administrator per place comes from the last national program: 2% of households were paid twice, and data was missing on 26% of payments (GAO) [SRC-1061]. Overlapping programs needed rules against duplication [SRC-1066]. The rest is judgment.

### HOU-4.03 The order of reach

**Parameters** (memo 8, `DEC-2026-11-09-06`):
1. **Stage 1, 2030-33 (HOU-4A.01).** People without a home, families with children first among them.
2. **Stage 2 (HOU-4A.01 from its first awards after stage 1 is served, then HOU-4D.01 from 2034).** Extremely low-income families with children with severe problems.
3. **Stage 3 (HOU-4.08, from 2038).** Extremely low-income renters with long-term disabilities. Other households have no funded route in the 2030s. Older renters who are not disabled are reconsidered once the care program is scoped (`DEC-2026-11-09-10`).

- **Within a stage.** In stage 1, local need-based intake decides the order, not quotas (`DEC-2026-11-09-12`). In stages 2 and 3, the order is memo 2 B's (`DEC-2026-11-09-01`): most severe problems first, then the youngest children, then date of application. That order is national guidance, with local need-based intake deciding, as in stage 1 (`DEC-2026-11-09-14`, under `DEC-2026-11-09-13`). The published counts (stage 1) and section 7's signals show whether the order works.
- **Local preferences.** Housing agencies may keep local preferences inside a stage, but not residency or length-of-residence rules (24 CFR 982.207) [EV-HOU-189] (point 7).
- **People at imminent risk** go to HOU-1D, not to this line (memo 8).
- **Who counts as "without a home"** (`DEC-2026-11-09-12`). One plain test, "no home of your own": people literally homeless, and families with children who are doubled up. A family shows it by its own word or by an existing school record. There is no deadline test and no cap. The order within stage 1 follows local need-based intake, not quotas. Counts are published yearly, and an imbalance two years running triggers a review, not an automatic restriction. Doubled-up families are where tenant vouchers do best at reaching people [EV-HOU-114]. Section 5 sets the forms.
- **Evidence.** [EV-HOU-086] [EV-HOU-099] [EV-HOU-090] [EV-HOU-026] [EV-HOU-109].
- **Section 7 checks** who the order reaches, by race, place and disability (memo 8).

### HOU-4.04 Matching the tool to the market

**Parameters** (memo 1 B):
1. **Tight market.** A metro area or nonmetro county counts as tight when its rental vacancy is at or below 4% in two consecutive annual Census readings, or when fewer than half of new voucher holders there have leased up within 180 days in the latest year. The 4% line is the legacy builder trigger (`legacy/domains/domain-housing.md`, HOU-9). The lease-up test follows the search evidence [EV-HOU-092]. Both lines are judgment. HUD publishes the list each year.
2. **Form by year.** The 2030-31 awards are tenant-based vouchers everywhere. From 2032, in tight markets only, up to 25% of each year's new awards may be attached to homes financed or bought under HOU-3C, HOU-8 or HOU-9A. HUD may raise the share to at most 50% after the evaluation in item 5. Elsewhere, every award is a tenant-based voucher. Both shares are judgment: memo 1 says the attached share "should start small and be tested."
3. **Right to move.** After 12 months in an attached home, a household may move with a tenant-based voucher and search help (HOU-4.07). This follows current law's choice-mobility rule for project-based vouchers, which is not yet in the register. Its home is then re-attached for the next household. The move-out voucher is funded from the household's own award, so the household does not wait for the agency's next available voucher, as current law allows (`5-delivery.md`, 2.2) [EV-HOU-352].
4. **Where attached homes go.** No attached awards in census tracts with poverty above 30%. The exceptions are redevelopment under HOU-5.02 and acquisitions that preserve existing tenants' homes. The line is judgment; the reason is the mobility evidence [EV-HOU-090].
5. **Evaluation.** HUD randomizes which eligible households are offered attached homes, or uses lotteries where there are more households than units. It compares lease-up, stability and neighborhood with tenant-based vouchers in the same markets, reporting by 2036.

- **Vehicle.** R2: a condition on HOU-4A and HOU-4D money and on HOU-3C's grants and loans.
- **Current law.** Uses the project-based voucher authority (42 U.S.C. 1437f(o)(13)), and the plan's attached awards are new awards under it.
- **Change to current law.** The statute exempts these awards from that authority's cap on the share of a housing agency's vouchers that may be project-based. Section 5 reads the cap and finds the attached awards would exceed it in some tight markets. Section 5 confirms the statutory text.
- **Data.** Annual vacancy readings exist only for larger areas. Where none exists, the lease-up test applies alone; section 5 names the data source.
- **Evidence.** [EV-HOU-092] [EV-HOU-093] [EV-HOU-118] [EV-HOU-090] [EV-HOU-114]. The register has no evaluation of attached help in tight markets (memo 1), which is why item 5 exists.

### HOU-4.05 Payment limits by neighborhood

- **What it does.** In metro areas, voucher payment limits are set by ZIP code (Small Area Fair Market Rents) for all tenant-based vouchers, not only the new awards (point 1).
- **Phase-in.** In tight markets first, with the 2030 awards, and in all metro areas by 2032. The schedule is judgment.
- **Hold harmless.** A sitting tenant's limit does not fall for two years.
- **Vehicle.** HUD can set it by rule. A regular bill writes it into 42 U.S.C. 1437f(o) so it lasts. It needs no new money beyond what HOU-4A pays.
- **Evidence.** [EV-HOU-095].

### HOU-4.06 National source-of-income protection

- **What it does.** Landlords may not refuse a tenant, or set different terms, because the tenant pays part of the rent with a voucher or other housing assistance (point 2).
- **Who is covered.** All rental housing covered by the Fair Housing Act, with that Act's exemptions.
- **Enforcement.** Through the Fair Housing Act's existing remedies, and mandatory testing and enforcement grants through the Fair Housing Initiatives Program for 2030-34, the years landlords learn the rule, so paired tests keep running whatever the yearly bill says (`DEC-2026-11-09-10`; `5-delivery.md`, 6.1) [EV-HOU-093]. The amount is $100 million a year (`DEC-2026-11-09-17`); the program's current appropriation is not in the register.
- **Interaction.** State and local laws that protect more stay in force [EV-HOU-247]. Federal rules that bar refusals in some assisted properties stay too [EV-HOU-246].
- **Vehicle.** Regular bill. It amends the Fair Housing Act, adding source of income to the protected grounds for these purposes. It has no budget effect, so it cannot ride reconciliation. The testing money rides R2 as mandatory money for 2030-34; its rules go in the regular bill (`5-delivery.md`, "Changes this section asks of section 4").
- **Effective date.** 2030, so it lands with the first new awards.
- **Evidence.** [EV-HOU-093] [EV-HOU-094] [EV-HOU-246] [EV-HOU-247].

### HOU-4.07 Search help

- **What it does.** Every new tenant-based award, and every move from an attached home, comes with a search-help payment to the housing agency. It covers search counseling, landlord outreach, and short-term costs such as deposits and application fees (point 3).
- **Starting point.** Current law's list of pre-inspected units [EV-HOU-232].
- **Under the 2037 right,** search help and landlord recruitment are part of the duty to house (HOU-4D.01, `DEC-2026-11-09-10`).
- **Amount.** A per-award fee set by HUD. Section 6 sizes it.
- **Vehicle.** R2, mandatory, within HOU-4A.02's administration allowance or beside it (section 6 decides). Evaluation money comes through appropriations.
- **Evidence.** [EV-HOU-091] [EV-HOU-188] [EV-HOU-232].
- **Open research ask (point 3, `DEC-2026-11-09-02`).** Espen agreed "with research on its design and how to make it available." That research is not yet done. It should cover:
  - which parts of the Seattle and King County model drove its results;
  - what it costs per household;
  - whether it works outside one metro;
  - how to offer it where housing agencies are small.
  Until it lands, the fee's uses are the ones listed above and its size is section 6's.

### HOU-4.08 Stage 3: disabled extremely low-income renters, from 2038

Espen's condition on memo 2 (`DEC-2026-11-09-01`): extremely low-income renters with long-term disabilities are a third stage from 2038. Their definition and services are designed with the care flagship, their cost is carried in section 6 and the financing settlement outside the $135 billion, and a share of accessible homes is set aside for them.

**Parameters.**
1. **Who.** Extremely low-income renter households (HOU-4.01) in which a member has a long-term disability, as defined with the care flagship. This dossier's placeholder is the voucher program's existing definition of a person with disabilities, pending that work. Receipt of SSI or SSDI, or Medicaid coverage on the basis of disability, counts as proof, with no new disability finding (`DEC-2026-11-09-14`).
2. **When.** Enrollment opens in 2038, after stage 2 is complete. The pace is set with the care flagship and section 6.
3. **Form.** Tenant-based vouchers, or awards attached to accessible homes reserved under HOU-3C.03. Help comes with home and community-based services offered through Medicaid (shared rule 7), never as a condition.
4. **Accessible homes.** See HOU-3C.03.

- **Vehicle.** Authorized in R2 with a 2038 effective date, so it is law from the start and its first two years fall inside the FY2030-39 window. The alternative is to enact it later in the care flagship's bill. Section 6 and the financing settlement decide the financing; it must be paid for from FY2040 under D4.
- **Evidence.** 1.16 million households with severe needs include someone under 62 with a disability [EV-HOU-032]. Extremely low-income renters make up most worst case needs [EV-HOU-185].
- **Cost.** Section 6 (outside HOU-4D's $135 billion).

### HOU-4.09 Housing First as the federal rule

**Parameters** (memo 5 B):
1. In January 2029 the President revokes the July 2025 executive order's conditions [EV-HOU-107].
2. A regular bill makes Housing First the standard for homelessness help that HUD and HHS fund, including McKinney-Vento grants and the new awards: no requirement of treatment, sobriety or service participation to get or keep housing; services offered.
3. The National Strategic Plan due in July 2027 [EV-HOU-238] is reissued to match.
4. **No sweeps** (`DEC-2026-11-09-10`). Extending current law's precedent in the Emergency Solutions Grants [EV-HOU-237], new federal homelessness money does not go to places that remove people or their belongings without offering shelter or housing.

- **A baseline expectation of engagement.** Espen's direction for section 4 (`DEC-2026-11-09-05`, paraphrased there) asks for supportive housing in which no one is threatened with a return to homelessness for declining treatment, but where there is a baseline expectation of engaging with service navigators. HOU-4.11 drafts that as a duty on providers, not a condition on tenants.
- **Vehicle.** Executive action, then a regular bill, which carries item 4. Where R2 money is new homelessness money (HOU-4.10's grants, HOU-4.12's backstop), R2 restates item 4 as a condition on it (judgment). No direct cost.
- **Evidence.** [EV-HOU-099] [EV-HOU-101] [EV-HOU-102] [EV-HOU-100] [EV-HOU-105] [EV-HOU-016].

### HOU-4.10 A voluntary recovery-housing option

- **What it does.** Grants for recovery (sober) housing for people who choose it, never as a condition of help (memo 5 B). People with HOU-4A awards can use them there.
- **Who receives grants.** Continuums of Care, for nonprofit operators that meet a national quality standard. The standard requires operators to accept residents on prescribed medicines, methadone and buprenorphine included [EV-HOU-312] [EV-HOU-301] (research note, recommendation 7).
- **Evaluation.** Outcomes are measured for people with active addiction, the group the trials missed [EV-HOU-105]. Placement is randomized where demand exceeds places.
- **Timing.** 2030-34, renewed on the evaluation.
- **Vehicle.** R2, mandatory and time-limited, for operations and evaluation. Capital comes through HOU-3C. After 2034, any renewal comes through appropriations.
- **Cost.** Section 6.
- **Evidence.** The register has no evaluation of recovery housing (memo 5). The option rests on judgment, and the evaluation is part of the design.

### HOU-4.11 Supportive housing: an engagement standard and treatment access

Source: the memo 5 follow-up research note, `dossiers/home/research-supportive-housing.md`, section 5. This provision cites that note's recommendations by number.

**Status.** Espen's direction decides the principle (`DEC-2026-11-09-05`), and Espen adopted the parameters below, drafted from the note's recommendations (`DEC-2026-11-09-10`).

**Parameters.**
1. **The engagement standard is a duty on providers, not a condition on tenants** (recommendation 1).
   - Every tenant in federally funded supportive housing is offered a named service navigator or case manager.
   - Contact is expected at least monthly, more often at first.
   - When a tenant does not engage, the provider follows a set protocol: visits, calls, letters, a peer, a change of worker.
   - Non-engagement can never end the lease, the subsidy or the tenant's place in the program. Tenancy follows the same lease rules as any other tenant's.
   - A tenant can enforce this protection against the provider, through the Continuum of Care's grievance process and in court, with a private right of action and attorney's fees (`DEC-2026-11-09-10`; `5-delivery.md`, 6.4).
   - The contact level follows Housing First as first designed [EV-HOU-322] [EV-HOU-321]. Those programs listed the visit as a tenant requirement [EV-HOU-323], so the no-loss guarantee goes further. Finland's practice of escalating contact before any eviction step is closest [EV-HOU-327]. The design rests on judgment.
2. **Close the gaps in current rules** (recommendation 2). Amend the Continuum of Care rule (24 CFR 578.75(h)) [EV-HOU-332] and the HUD-VASH requirement [EV-HOU-325], so that not taking part in case management cannot end housing assistance. A HUD-VASH veteran who stops engaging moves to a regular voucher automatically.
3. **Treatment is never a condition, and is easy to get** (recommendation 3). Providers offer, or connect tenants to, on site or by visit:
   - medicines for opioid use disorder;
   - naloxone;
   - contingency management for stimulants;
   - assertive community treatment or intensive case management for people with serious mental illness [EV-HOU-300] [EV-HOU-302] [EV-HOU-304] [EV-HOU-308].
4. **Priority** (recommendation 6). Scale first for chronically homeless people who use the most public services, where cost offsets are largest [EV-HOU-318]. HOU-4A's stage 1 awards pay their rent.
5. **Measurement** (recommendation 8). Each program reports contact rates, housing retention, overdose deaths, medicine starts and exits by reason.
6. **The Continuum of Care in 2029** (recommendation 9). Restore its priority for permanent housing, and reverse the treatment-participation scoring and the transitional-housing set-aside [EV-HOU-334] [EV-HOU-238].

- **Vehicle.** Executive action and HUD rulemaking in 2029 for items 2 and 6. A regular bill writes items 1 and 3 into McKinney-Vento with HOU-4.09.
- **Agency.** HUD, the VA (HUD-VASH) and HHS.
- **Cost.** None directly. Services are funded under HOU-4.12.

### HOU-4.12 Services and workforce for supportive housing

1. **Medicaid first** (recommendation 4). The care flagship is asked to include tenancy-sustaining services, housing navigation and assertive community treatment in its home and community-based services expansion (HLT-4). States would then not depend on waivers, which must be budget neutral from 2027 [EV-HOU-337], after CMS withdrew its housing-services guidance [EV-HOU-339].
2. **A HUD services backstop.** A HUD services grant pays for the same services for tenants without Medicaid. Through 2035 it also pays for tenants whose state Medicaid program does not cover these services; from 2036 it returns to tenants without Medicaid (`DEC-2026-11-09-10`; `5-delivery.md`, question 3). Payment is by contract with staffing and contact standards, not open fee-for-service billing, given Minnesota's ended housing benefit [EV-HOU-329].
3. **Workforce** (recommendation 5). Service funding is tied to wage floors and caseload limits, with peer-specialist training. Behavioral health workforce shortages are projected [EV-HOU-338].

- **Status.** Adopted (`DEC-2026-11-09-10`).
- **Vehicle (split).** The Medicaid benefit is in the care flagship's bill. The HUD services grant rides R2 as mandatory money for 2030-39, with appropriations after that. This split is section 4's working choice. The note leaves the vehicle open.
- **Cost.** Section 6, with the per-unit service cost and national need the note lists as evidence still needed. Offsets are counted only for the highest-use group (recommendation 6).
- **Shared rule 7.** This provision revises the working answer that housing pays for no services: housing pays only the backstop for people Medicaid does not cover, and through 2035 for people whose state does not cover the services.

### HOU-4.13 Tribal housing: set-asides, through tribes, by self-determination

Espen's direction (`DEC-2026-11-09-10`): tribal housing gets dedicated policy and investment, with set-asides, that respect sovereignty and self-determination and restore tribes' access to resources sufficient to care for their people. The need differs in kind. In tribal areas, 23% of American Indian and Alaska Native households live in housing with a physical condition problem and 16% are overcrowded, against 5% and 2% of all U.S. households, and 42,000-85,000 Native Americans there are homeless, most of them doubled up [EV-HOU-406]. Vouchers pay rent; they do not repair or build homes (`7-validation.md`, 4.2).

**Parameters.**
1. **Set-asides in the plan's money** (sizes decided, `DEC-2026-11-09-16`). Each is a share of an amount already decided, so it adds no cost of its own (`6-cost.md`, 2.6).
   - *Emergency fund (HOU-1D.01 to .04).* 3% of the standing fund and of the one-time start. Basis: the 2021 program's first round set aside $0.800 billion of $25 billion for tribal areas [EV-HOU-350] [EV-HOU-150].
   - *New awards (HOU-4A.01, HOU-4D.01, HOU-4.08).* 3% of each year's new-award money, the rent-help share the 2021 program used [EV-HOU-350]. That is about 7,500 of each year's 250,000 awards in 2030-33.
   - *Construction grants (HOU-3C.01).* 5% of the revolving-fund grants, about $3.6 billion over 2030-37. Basis: judgment. The share is set above the rent-help share because tribal needs are mostly condition and crowding, four to eight times the national rate [EV-HOU-406], which only capital fixes. The register has no count of tribal homes needing repair or replacement to size it from need.
   - *Construction loans (HOU-3C.02).* Tribes and tribally designated housing entities are eligible borrowers; no share is reserved, because loans secured on trust land are hard to underwrite, so the grant set-aside carries the capital (judgment).
2. **Through tribal governments.** Each set-aside goes to tribes, or to the tribally designated housing entity a tribe names, by the Native American Housing Block Grant formula, under the Native American Housing Assistance and Self-Determination Act (NAHASDA) and each tribe's own housing plan, the way the 2021 program allocated its tribal share [EV-HOU-350]. Nothing passes through a state. A share not used in a year stays available until spent.
3. **The form follows the tribe's plan.** A tribe may use its share of the new awards as tenant-based rental help, as help attached to homes it owns or builds, or to repair or build those homes; and its share of the emergency fund under its own rules for crises. The tenant protections in the shared rules still apply: no work or treatment condition, Housing First, no eviction for the months paid (HOU-4.01, HOU-4.09, HOU-1D.02). Judgment, within Espen's direction on self-determination.
4. **Resources sufficient to care for their people.** The set-asides are a floor, not a measure of need. HUD and tribes report by 2032 on the tribal need for new and repaired homes, the block grant's level against it, and what the set-asides delivered, so any added investment can be decided on need data.
5. **The low-income credit.** HOU-2D.01 keeps the bill's treatment of tribal areas as high-cost areas with a basis boost, which the 2025 law dropped [EV-HOU-263].
6. **Reporting.** Awards, leases, payments and homes financed are reported for tribal areas from the shared record (`7-validation.md`, 4.2).

- **Vehicle.** R2, as set-asides in each program's money. The rules on form and administration go in the regular bill as a NAHASDA amendment, where reconciliation cannot carry them.
- **Agency.** HUD's Office of Native American Programs, with tribes and tribally designated housing entities.
- **Current law.** NAHASDA (25 U.S.C. 4101 and following; not yet in the register) and its block grant. Tribal HUD-VASH is a pilot that GAO says lacks measurable objectives and an evaluation plan [SRC-1441].
- **Evidence.** [EV-HOU-406] [EV-HOU-350] [EV-HOU-150]. Section 5 notes the register has no evidence on how new awards reach tribal lands.

## 2. Rental help: the guarantee's money

### HOU-4A.01 One million new awards, 2030-33

- **What it does.** 250,000 new awards each year from 2030 to 2033, with continuing help for each household after that, as mandatory spending (memos 1, 2 and 8 keep the count, pace and funding).
- **Who.** Stage 1, then the start of stage 2 (HOU-4.03). A tribal share goes through tribes (HOU-4.13).
- **Form.** HOU-4.04. All awards are tenant-based in 2030-31; in tight markets from 2032 up to the attached share.
- **Rent.** As current vouchers (HOU-4.01). Payment limits follow HOU-4.05.
- **Renewal.** An award does not lapse for lack of appropriations: its continuing cost is mandatory, outside the yearly voucher renewal vote. Lease-up is measured separately from the award (legacy design).
- **Vehicle.** R2, mandatory.
- **Current law.** New awards under 42 U.S.C. 1437f(o), funded outside the tenant-based rental assistance appropriation [EV-HOU-187]. Precedent: Emergency Housing Vouchers [EV-HOU-188].
- **Evidence.** [EV-HOU-086] [EV-HOU-092] [EV-HOU-187] [EV-HOU-188] [EV-HOU-013].
- **Cost source.** Legacy working midpoint $150 billion over FY2030-39, or $162.2 billion with administration. In the ledger it is component `HOU-1/additional-600000-voucher-awards` ($0.09 trillion, the increment over the older 400,000 inside the housing title), in `models/data/budget/provisions.csv`. Section 6 rescores it.

### HOU-4A.02 Housing agency administration

- **What it does.** An administration allowance for the new awards, covering intake through the common application (HOU-4.02).
- **Amount.** The legacy planning allowance of $12.2 billion over FY2030-39 on the whole million (`legacy/domains/domain-housing.md`, "PR #22 fee correction"). Fees for the new awards are paid in full, never prorated as yearly appropriations now allow, and include a one-time issuance fee for each new award (`5-delivery.md`, 2.2) [EV-HOU-343]. Section 6 checks the allowance against that rule.
- **Vehicle.** R2, mandatory. HUD's own federal staff come through the agency rebuild line (CAP-7S and CAP-7), not here.
- **Cost source.** The legacy file. It is carried inside HOU-4A's $162.2 billion working midpoint.

### HOU-4D.01 Stage 2: a guarantee for the poorest families with children

**Parameters** (memo 2 B):
1. **Who.** Renter households with income at or below the extremely low-income line (HOU-4.01), with at least one child under 18, unassisted, with severe problems (paying over half of income for rent, or living in severely inadequate housing, HUD's worst case needs test) [EV-HOU-186]. From 2034, families with children who have no home of their own under HOU-4.03's test, doubled up or homeless, can also enter (`DEC-2026-11-09-12`). The family shows severe problems by its own statement of rent and conditions, with income found once (HOU-4.02, item 5), checked after award (judgment, under `DEC-2026-11-09-13`; `5-delivery.md`, 2.2).
2. **Enrollment.** Opens in 2034, up to 300,000 families a year in HOU-4.03's order. From 2037, every eligible family that applies gets help: the cap ends and help is a right.
3. **Form.** HOU-4.04.
4. **Staying eligible.** A family stays eligible while its income is under 80% of area median income at the annual review (`DEC-2026-11-09-11`). When the youngest child turns 18, the family keeps its help until its next move or its income rises above that line; that part is judgment. The rule keeps families longer than memo 2's arithmetic, which costs enrolling the group, not how long families stay; section 6 holds the count flat (`6-cost.md`, 1.3).
5. **The duty to house, from 2037** (`DEC-2026-11-09-10`). The right is to a home, not only to a voucher: in 2022 only 57% of voucher searches succeeded [EV-HOU-395]. For every entitled family, the housing agency must:
   - give search help and landlord recruitment with the voucher (HOU-4.07);
   - when a search fails (the search term ends without a lease), offer the family a unit or a placement: an attached home (HOU-4.04, HOU-3C.03) where one is free; otherwise a reissued voucher with search help and a higher payment standard, up to 120% of the limit (`5-delivery.md`, 2.2). This is the order section 7 proposed (`7-validation.md`, 1.2);
   - where the agency cannot make the offer, the backstop administrator must (`5-delivery.md`, 6.3).
   The offer is due within 60 days of the failed search, and offers continue until the family is housed (`DEC-2026-11-09-14`). Basis: read with the project's design lens (`DEC-2026-11-09-13`), which argues against a rule that ends help after refusals. Emergency Housing Vouchers needed search terms of at least 120 days [EV-HOU-346], and the median successful search took 78 days in 2022 [EV-HOU-395].
6. **Remedies, from 2037** (`DEC-2026-11-09-10`). A complete application is decided within 30 days; one not decided in time is treated as approved, with checks after award (deemed approval). A family denied, delayed or not offered a placement on time has a private right of action, with attorney's fees, and legal aid groups have standing. Section 5's other remedies for the right (a written decision, a hearing, no waiting list for the entitled) are its delivery design (`5-delivery.md`, 6.3).
7. **Tribal share.** Part of stage 2's money goes through tribes (HOU-4.13).

- **Amount.** The $135 billion over FY2030-39 is an estimate, not a cap, because stage 2 is a right from 2037 (memo 2 B).
- **Vehicle.** R2, mandatory. It is enacted in 2029 with 2034 and 2037 effective dates.
- **Current law.** New awards under 1437f(o), like HOU-4A.01.
- **Evidence.** [EV-HOU-185] [EV-HOU-186] [EV-HOU-086] [EV-HOU-090] [EV-HOU-011] [EV-HOU-395] [EV-HOU-346].
- **Cost source.** `housing_extra_tn` = 0.135 in `models/data/inputs/recovery-adoption.json`. Memo 2 arithmetic (not a score): about $114 billion through 2039 at full sign-up, or $123 billion with administration. Section 6's central figure is $81 billion over FY2030-39, plus about $3 billion for the duty to house (`6-cost.md`, 1.2). The wider entry under `DEC-2026-11-09-12` adds about $17 billion over FY2030-39 and $8 billion in FY2040 (`6-cost.md`, 2.7).
- **Charter follow-up.** The next charter PR renames HOU-4D to say what it buys (memo 2).

## 3. Emergency rent help

### HOU-1D.01 The standing fund: eligibility, uses and caps

**Parameters** (memo 6 C; point 5 rules 1 and 3; point 4).
1. **Eligibility (rule 1).** Renter households with income at or below 50% of area median income, or already enrolled in SNAP, Medicaid or SSI, facing a housing crisis now: unpaid rent with a notice, an eviction filing, a utility shutoff, or displacement by a declared disaster. No test of what caused the hardship. A disaster counts because the disaster recovery grants end in July 2029 [EV-HOU-228].
2. **Uses and caps (rule 3).**
   - Back rent and utilities, plus up to two months of future rent, a deposit or moving costs.
   - An annual cap per household of four months of the area's Fair Market Rent in any 12 months, usable across any number of crises (`DEC-2026-11-09-17`). It replaces point 5's episode limits (one in 12 months, two in three years; `DEC-2026-11-09-16`). HUD indexes the Fair Market Rents.
   - A second crisis within 12 months prompts a referral to long-term help (HOU-4.02, item 3; `DEC-2026-11-09-17`).
   - *Tracking and review* (`DEC-2026-11-09-16`). The fund's local or state administrator tracks each household's use in the shared record; HUD's cross-grantee duplicate check stays (HOU-1D.03). Income is verified through tax data where that is possible and easy, as federal income-matching already allows (shared rule 5); the cap itself is tracked by the administrator, since rent help is not reported to the IRS. HUD publishes the share of payments going to repeat users, and a high share triggers a review under the project's review procedure (`DEC-2026-11-09-15`), not an automatic cutoff.
3. **Legal help (point 4).** Tenant legal help is an allowed use, paid apart from the cap. It is not a federal right to counsel.
4. **Permanence.** A standing program with no end date.

- **Amount.** Section 6 sizes it.
- **Vehicle.** R2, mandatory. A permanent claim, so it is paid for from FY2040 (D4).
- **Agency.** HUD (HOU-4.02).
- **Current law.** There is no standing federal emergency rent program, and the ROAD to Housing Act creates none (memo 6).
- **Evidence.** [EV-HOU-108] [EV-HOU-109] [EV-HOU-110] [EV-HOU-111] [EV-HOU-150] [SRC-0304].

### HOU-1D.02 How the fund pays

Rules 2, 4 and 5 of `point-5-emergency-aid-rules.md`, as approved.
1. **Risk screen.** Each grantee ranks eligible applicants with a short points-based screen. HUD publishes a model screen, and each grantee tests and publishes its own version. Anyone with an eviction case or a court date is fast-tracked [SRC-1065].
2. **Self-attestation and checks.**
   - Tenants may state their income and hardship in writing.
   - Before paying, the grantee checks identity, the tenancy and the landlord's ownership against public and agency records.
   - After paying, it audits a random sample.
   - The statute states that self-attestation is allowed, so a later administration cannot remove it by guidance alone [EV-HOU-150] [SRC-0991].
3. **Landlord applications.**
   - Landlords may start an application with the tenant's signed consent and notice to the tenant.
   - The landlord is paid first. The tenant is paid directly if the landlord refuses or does not answer within 10 days.
   - The landlord must drop the nonpayment case and may not evict for nonpayment for the months paid.
   - Payment within 30 days of a complete application [EV-HOU-152].

- **Vehicle.** R2, as conditions on the money. The payee order and the eligibility rules are law. The screen's form and the consent documents are set by guidance.

### HOU-1D.03 Accountability

Rules 6, 7 and 8 of the point 5 note.
1. **Grantee network.**
   - One administrator per place: every state, plus cities and counties of at least 200,000 people that choose to run their own program, plus tribes or tribally designated housing entities, as in the last program [SRC-1068] [SRC-0304], with no overlap. The tribal share is set aside and paid by the block grant formula (HOU-4.13).
   - Each links to eviction court, legal aid and the local 211 line.
   - Money is allocated by a need formula and moved from slow to fast grantees on published measures.
2. **Payment errors.** HUD estimates improper and unknown payments from a random sample in year one, and publishes the rate yearly with a target. It recovers errors from grantees, never by evicting tenants over honest mistakes [SRC-0315] [EV-HOU-154] [EV-HOU-182].
3. **Data standard.** Every grantee reports every payment monthly in one federal format, which HOU-4.02 shares. HUD runs a cross-grantee duplicate check. Records can be linked to eviction-court and shelter data for evaluation, under privacy rules [SRC-1061].

- **Vehicle (split).** The grantee allocation, the administration allowance, the measurement and the reporting system ride R2 as mandatory money. The 2021 lesson is that a measurement left to the yearly vote was skipped (point 5, rule 6). The privacy rules and the authority to link court and shelter records go in a regular bill.
- **Evidence.** [EV-HOU-150] [SRC-1066] [SRC-1061].

### HOU-1D.04 The one-time start, 2030-31

- **What it does.** A one-time tranche of rent help through the fund's network in 2030-31, smaller than HOU-1A's $85 billion. It replaces HOU-1A.
- **Building money.** HOU-3C stays at its decided amounts (about $72 billion of grants and $300 billion of loans; `DEC-2026-11-09-03`). So HOU-1A's construction gap money leaves the plan with HOU-1A; it is not added to HOU-3C. Gap financing is an eligible use within HOU-3C's existing amounts. Memo 6 C said the gap money "moves into the construction funds", while memo 3 part 3 B kept those funds' amounts. This section reads the two together as no added money. **For Espen (yes or no; not adopted):** keep it this way, or add HOU-1A's construction share to HOU-3C's grants, which would change amounts memo 3 kept.
- **Rules.** The same as the standing fund (HOU-1D.01 to .03). The network is built once and stays.
- **Amount.** Section 6 sizes the tranche.
- **Vehicle.** R2, mandatory and one-time, so it makes no FY2040 claim (D4).
- **Cost source.** The ledger's housing title component `HOU-1/legacy-housing-title` ($0.47 trillion) still carries HOU-1A's $85 billion. Section 6 replaces it with HOU-1D's standing fund and smaller start.

## 4. Homes: building, buying and repair

### HOU-3C.01 State housing revolving funds

- **What it does.** Capitalization grants to a housing revolving fund in each state (memo 3 part 3 B).
- **Amounts.** About $72 billion, awarded over FY2030-37 so that it is spent by 2039 (`DEC-2026-11-09-09`): $3 billion in 2030, $5 billion in 2031, $10 billion a year in 2032-33 and $11 billion a year in 2034-37. The total and the first two years are as decided (memo 3 part 3 B); the legacy schedule ran $8 billion a year to 2039, and this yearly split is this section's (judgment). States match 20%. Section 5's fund plans and plan-by-silence (`5-delivery.md`, 2.4) carry the faster ramp.
- **Tribal share.** Part of the grants goes through tribes (HOU-4.13).
- **For the poorest renters.** At least 30% goes out as grants or forgivable loans for homes for extremely low-income renters.
- **Eligible uses.** New building, plus buying and preserving existing rental buildings and single-family homes, including tax-credit buildings whose rent limits are ending [EV-HOU-119].
- **Vehicle.** R2, mandatory. It is borrowed inside the D4-B envelope as time-limited capital (ledger C21).
- **Cost source.** Legacy file. The grant channel is about $0.06 trillion of HOU-3C's $0.075 trillion midpoint (range $0.061-0.10 trillion), and it is the part C21 borrows. The rest, about $0.015 trillion, is the loans' subsidy cost (HOU-3C.02). Both sit inside the ledger's housing title component ($0.47 trillion).
- **Agency.** HUD, with state housing finance agencies.
- **Current law.** New. It works beside HOME, with no set amount, and CDBG's new construction use (ROAD to Housing Act sections 501 and 204) [EV-HOU-215] [EV-HOU-226].
- **Evidence.** [EV-HOU-118] [EV-HOU-150] [EV-HOU-119] [EV-HOU-024].

### HOU-3C.02 Federal construction and acquisition loans

- **What it does.** A HUD Housing Construction Loan program, funded through the Federal Financing Bank.
- **Amounts.** $300 billion of commitments, made over 2030-38 so the loans are disbursed by about 2039 (`DEC-2026-11-09-09`): $10 billion in 2030, $20 billion in 2031, $30 billion in 2032, then $40 billion a year in 2033-38. The legacy ramp ran about $34 billion a year to 2039; this split is this section's (judgment).
- **Who borrows.** Mixed-income and social housing, with HOU-8 the first borrower; housing agencies' new building; nonprofit and tax-credit projects; and tribes and tribally designated housing entities (HOU-4.13). Acquisition and preservation are eligible, as in HOU-3C.01.
- **Terms.** Loans are priced near Treasury rates plus a margin for administration. State agencies originate and service them under a risk-share (the HUD-HFA Risk-Sharing model, sec. 542(c)).
- **Vehicle.** R2, for the credit subsidy. Only the expected loss scores under the Federal Credit Reform Act; it needs CBO's subsidy rate.
- **Cost source.** Legacy file: about $0.015 trillion of subsidy cost (range $0.006-0.03 trillion). HOU-3C as a whole is about $0.075 trillion inside the ledger's housing title.

### HOU-3C.03 Conditions on plan-financed homes

1. **Lasting affordability.** Every home that HOU-3C, HOU-8 or HOU-9A builds or buys stays affordable for good, through a recorded use restriction and a nonprofit or public right of first refusal on sale (memo 3 part 3 B). The same rule reaches new tax-credit buildings (HOU-2D.04, `DEC-2026-11-09-08`).
2. **Attached help.** In tight markets, HOU-4.04's attached awards go first to homes these funds finance or buy. A project's loan underwriting may count the attached rent (memo 1 B; that pairing is why the loan-heavy construction money works).
3. **Accessible homes for stage 3.** Every building these funds finance meets the federal accessibility minimums for assisted new construction (Section 504 rules; not yet in the register). From 2038, a share of its accessible units is reserved at each turnover for HOU-4.08's households. The share is set with the care flagship, in a law that also requires HUD to publish the count of reserved units by place.
4. **Climate.** New building meets CLI-8's hazard-resistant code baseline (legacy dependency).

- **Vehicle.** R2, as grant and loan conditions.
- **Evidence.** [EV-HOU-119] [EV-HOU-118] [EV-HOU-032].

### HOU-3C.04 Published production targets: three numbers

Espen's direction (`DEC-2026-11-09-10`): publish a target for homes built and preserved. Section 7 found the plan had none (`7-validation.md`, 1.4). Espen then asked for three numbers, each checkable, with the direct count including homes the tax credits finance (`DEC-2026-11-09-14`), and approved the three numbers below (`DEC-2026-11-09-17`). Each state's share of number 1 is still proposed, for Espen.

**1. Homes the plan pays for: about 1.3 million built or preserved over 2030-39 (range 0.8-1.9 million), at least 120,000 of them for extremely low-income renters (range 100,000-160,000).** It counts only homes the plan's added money pays for. The credit's current-law production, about 95,000 homes a year since 1987 [EV-HOU-443], is the baseline and is not counted. Each home counts once, whatever mix of money it uses.

| Source | Homes, 2030-39 (central, range) | Basis |
| --- | --- | --- |
| Construction money: HOU-3C grants and loans, HOU-8, HOU-9A | 900,000 (600,000-1,300,000) | *Grants:* about $86 billion with the state match, at $150,000-300,000 of gap subsidy a home, finances about 290,000-580,000 homes (`7-validation.md`, 1.4) [EV-HOU-412] [EV-HOU-411]. *Loans:* $300 billion of commitments at $250,000-350,000 of loan a home would finance 0.9-1.2 million homes if every loan went to a separate home (`7-validation.md`, 1.4). Many loans pair with the grants or credits, so this section counts only loan-only homes, mostly mixed-income, social housing and acquisitions in tight markets: about half the loan money (a third to 60%), so about 500,000 (300,000-700,000; judgment). Loan-only homes must earn rents that repay the loan, so few are deeply affordable, and demand for the loans is untested at this scale |
| Bigger low-income credit with the deep-income boost (HOU-2D.01) | 300,000 (200,000-330,000) | Novogradac's estimates for the parts of the bill HOU-2D.01 carries [EV-HOU-444]: 104,000 from the extremely low-income boost and 167,000 from the 9% allocation increase, counted in full because the firm's baseline already assumes the 12.5% increase, which the 2025 law's permanent 12% roughly matches [EV-HOU-260]. Of the 175,000 from 30% basis boosts, only the rural and tribal boosts are in HOU-2D.01: the tribal one decided (`DEC-2026-11-09-16`, HOU-4.13), the rural one proposed, for Espen; the bond-financed boost (AHCIA section 308), likely the largest, is left out (`DEC-2026-11-09-17`). This section counts about 40,000 for them (judgment, at most a third of the 175,000). The firm has a stake and assumes gap money scales; the plan's construction grants are that gap money. The low end discounts that assumption (judgment) |
| Middle-income credit trial (HOU-2D.02) | 60,000 (40,000-90,000) | The bill's own arithmetic, about $156,000 of credit a home (`memo-3-part1-research.md`, M1), at half the allocation for five years of awards; the high-cost limit and the deeper discount lower the count (judgment) |
| Neighborhood homes credit (HOU-2D.03), homes for sale | 150,000 (110,000-250,000) | About $15 billion of credits over 2030-34 [EV-HOU-270] at roughly $60,000-130,000 of credit a home, under the bill's cap of 32% of the national median new-home price [EV-HOU-268] (judgment) |
| Less homes counted twice | −100,000 (−70,000 to −120,000) | About a third of the new low-income credit homes also draw HOU-3C grant money (judgment); loan-only homes are counted apart from both |

- *Extremely low-income homes.* At least 30% of the revolving-fund grants go to them, about 100,000 homes (85,000-130,000; `7-validation.md`, 1.4). Buildings using the deep-income boost reserve at least a fifth of their homes for them [EV-HOU-263], about 20,000 more on Novogradac's count.
- *Reported apart:* new homes and preserved homes; rental homes and homes for sale; and net additions to the stock, estimated with a published method. One subsidized home adds a third to a half of a home on average [EV-HOU-114], so net additions are perhaps half the direct count. They are reported, not targeted, because crowd-out cannot be measured place by place each year (judgment).

**2. Homes finished in places that earn the zoning reward (HOU-6.01): at least 1% of their housing stock within five years of the award, above their own prior pace. Across the country, that is about 600,000 added homes over 2030-39 (range 250,000-1.8 million).** HUD reports, for each rewarded place, homes finished against its own average for the three years before the award, and against similar places without an award.
- *Basis for the place goal.* The evidence is modest and mixed. Loosening land-use rules raised housing supply by about 0.8% within three to nine years in U.S. places [EV-HOU-177]. Auckland's broad upzoning permitted about 4.1% more of its stock over five years [EV-HOU-123]. Chicago's transit-area upzonings showed no rise [EV-HOU-124]. A 1% goal sits between the U.S. average and Auckland's result (judgment).
- *The national estimate* (this section's arithmetic; judgment on every input). The country has about 148 million homes [EV-HOU-445]. If places holding about 30% of them (20-40%) reform and earn awards, statewide reforms and the transportation condition (HOU-6.02) included, and their supply rises by about 1.5% over the decade (0.8-3%), the package adds about 0.67 million homes; the range runs from about 0.24 million (20% coverage, 0.8%) to about 1.8 million (40%, 3%). The $30 billion of awards then costs about $45,000 per added home at the center, a cross-check that the reward is large enough to matter to a place.
- *Why a goal, not a promise.* The reward pays for homes finished (HOU-6.01), so it pulls private building that no federal dollar finances. The plan influences this number but does not control it. These homes are part of the national total (number 3) and partly overlap with number 1, where plan-financed homes are built in rewarded places.

**3. A national goal: 15 million homes finished in the United States over 2030-39 (range 13-16.5 million): today's pace, held for a decade.**
- *Basis.* The country finished 1.39 to 1.63 million homes a year in 2022-25 [EV-HOU-440], about 1.49 million a year on average, and about 13.2 million over 2016-25. Fifteen million is that pace held through 2030-39.
- *Why today's pace is enough to matter.* Household growth is slowing. The Joint Center for Housing Studies projects baseline demand for 11.3 million new homes in 2025-35 and 8.0 million in 2035-45, not counting the shortage [EV-HOU-441]: about 9.7 million for 2030-39, blending the two periods (this section's arithmetic). Its demand counts include manufactured homes shipped, about 0.1 million a year (not yet in the register), which Census completions leave out, so in completion terms baseline demand is about 8.7 million. Holding today's pace instead builds about 6 million more than that, enough to close the shortage, which estimates put at 1.5-5.5 million [EV-HOU-442] [EV-HOU-017], with room for local mismatch.
- *Range.* The low end, 13 million, is baseline demand in completion terms plus a 4 million shortage closed in full. The high end, about 16.5 million, follows the Joint Center's high-immigration projection, 14.1 million for 2025-35 against 11.3 million [EV-HOU-441] (about a quarter more), in completion terms, plus the upper shortage estimate. Immigration and the construction workforce move this number most (fork 7; `7-validation.md`, 3.5, check 8).
- *Measurement.* Census completions of new privately-owned homes [EV-HOU-440].
- *What the plan itself adds.* Net of crowd-out, number 1's homes add perhaps a third to a half of a home each [EV-HOU-114], about 0.3-0.7 million, toward the low end because acquisitions and preservation keep homes affordable but add none to the stock. Number 2 adds about 0.25-1.8 million. The two overlap where plan-financed homes are built in rewarded places, about 0.1-0.2 million (judgment). Netting that out, the plan adds about 1.0 million new homes at the center (0.4-2.4 million), roughly a sixth of the 6 million by which the goal exceeds baseline demand (this section's arithmetic). The rest depends on private building holding today's pace, which the plan's rental help, zoning reward and steadier demand support but do not guarantee.
- *Why a goal, not a promise.* Most homes are built by private owners with private money; the plan's direct count is about 9% of the goal. The national number says what the plan's zoning reward, credits and capital are for, and lets voters check the result.

**For all three.**
- *Yearly reporting by place and income band* from the grant, loan and credit records and Census data: homes financed, started, finished and preserved, and public money per home.
- *What the targets do.* Each state's share of number 1 follows its share of the grants and credits (proposed, for Espen). HOU-9A.01's builder may build only where state channels have missed their share. Missing a target is a published warning (section 7, 6), not a reason to withhold money (judgment, under `DEC-2026-11-09-13`).

- **Vehicle.** The regular bill states the targets. R2 makes the reporting a condition on HOU-3C's grants and loans; the credit reporting rides HOU-2D.
- **Cost.** None directly.
- **Evidence.** [EV-HOU-440] [EV-HOU-441] [EV-HOU-442] [EV-HOU-443] [EV-HOU-444] [EV-HOU-445] [EV-HOU-114] [EV-HOU-123] [EV-HOU-124] [EV-HOU-177] [EV-HOU-411] [EV-HOU-412] [EV-HOU-263] [EV-HOU-268] [EV-HOU-270].

### HOU-5.01 Public housing repair (legacy working choice)

- **What it does.** The Capital Fund rises from $3.2 billion (FY2026), as mandatory money with a sunset, since it is a backlog program (`legacy/domains/domain-housing.md`, HOU-5). The legacy design gave about $9 billion a year for ten years, about $58 billion above FY2026. To spend it by 2039 (`DEC-2026-11-09-09`), the same $58 billion is awarded over FY2030-37: about $10.5 billion a year for eight years (this section's arithmetic).
- **Status.** Section 3 did not re-weigh the amount. Faircloth repeal (HOU-5B) is carried as chosen and not re-weighed.
- **Converted homes.** Homes that convert under the now-permanent Rental Assistance Demonstration [EV-HOU-231] keep the repair money already committed to them. They draw no new Capital Fund money after conversion.
- **Vehicle.** R2, mandatory. It is borrowed inside the D4-B envelope as time-limited capital (ledger C31).
- **Cost source.** Legacy file: about $0.06 trillion (range $0.05-0.07 trillion), inside the ledger's housing title.

### HOU-5.02 Repair first, replacement and the right to return

**Parameters** (point 6, `DEC-2026-11-09-02`).
1. **Repair first.** Sound buildings are repaired before any redevelopment.
2. **Replacement.** Where buildings are redeveloped, by the Capital Fund or under the Rental Assistance Demonstration, every unit is replaced one for one.
3. **Right to return.** Every resident in good standing on the date redevelopment is announced has a right to return to a replacement unit, with no re-screening on return: no new screening on credit, criminal record or income eligibility beyond the program's rent rule. Residents may take a tenant-based voucher as an alternative.
4. **Moving costs.** Relocation and moving costs are paid both ways.

- **Reporting.** HUD's yearly report on how many residents stay or return [EV-HOU-231] becomes the enforcement record. HUD may withhold Capital Fund money from a housing agency that breaks the rules.
- **Vehicle.** Regular bill, amending the Rental Assistance Demonstration and the public housing redevelopment rules. R2 restates the rules as conditions on HOU-5.01's money.
- **Evidence.** [EV-HOU-122] [EV-HOU-121] [EV-HOU-231]. "Repair first" is judgment.

### HOU-8.01 Social housing pilot (legacy working choice)

- **What it does.** A mixed-income public development pilot. Public or nonprofit owners set rents to cover operating and debt costs across mixed incomes.
- **Financing.** HOU-3C.02 loans plus a small federal equity grant.
- **Conditions.** HOU-3C.03 applies.
- **Vehicle.** R2.
- **Cost source.** Legacy file: about $0.01 trillion.

### HOU-9A.01 A small federal builder from 2029

**Parameters** (memo 3 part 2, A-small).
1. **The corporation.** A federal housing construction corporation, authorized in 2029-30.
2. **Where it builds.** On federal land, and land it controls by agreement, in tight markets (HOU-4.04's list) where state channels have missed their share of the published production target (HOU-3C.04).
3. **Land.** No condemnation.
4. **Federal construction.** Local permitting yields only for its own construction.
5. **Rents.** Set to cover operating and debt costs.
6. **Workforce.** It draws on LAB-8 apprenticeships.
7. **Size.** A small start, with no scheduled scale-up. A-small, unlike A-full, does not program the 2033-36 scale-up. Any growth is a later decision on its results.

- **Land sources.** Local land lists under the ROAD to Housing Act [EV-HOU-214].
- **Vehicle.** A regular bill creates the corporation. R2 carries its capital and its Federal Financing Bank loan authority.
- **Evidence.** [EV-HOU-150] [EV-HOU-161]. The register has no independent evaluation of a U.S. public developer (memo 3).
- **Cost.** Section 6: a placeholder of $5 billion of capital over FY2030-39 (range $2-20 billion), judgment; the legacy file leaves it unscored.

## 5. Zoning and markets

### HOU-6.01 The zoning reward through the Innovation Fund

**Parameters** (memo 4 B). The plan's zoning money goes into the ROAD to Housing Act's Innovation Fund (section 208) [EV-HOU-206], changed so that:
- states and regions can compete, with larger awards for statewide reform;
- awards follow homes finished, not homes permitted;
- lower-cost homes are counted and rewarded separately. The reporting the Act leaves optional becomes required [EV-HOU-207];
- the $10 million cap on awards rises;
- the 2033 end date goes.

- **Build Now.** Its CDBG reallocation stays as the only test on community development grants [EV-HOU-208]. HUD studies whether it penalizes steady builders below 4% growth [EV-HOU-244] and reports by 2032, with a proposed fix if it does.
- **Vehicle (split).** The money is a direct appropriation in R2, mandatory. The changes to who may apply and what is paid for go in a regular bill. The R2 money is written so it can be spent under the Act's current rules until the regular bill passes (judgment; memo 4).
- **Evidence.** [EV-HOU-123] [EV-HOU-124] [EV-HOU-177] [EV-HOU-206] [EV-HOU-208].
- **Cost source.** Legacy file: about $0.03 trillion (range $0.02-0.05 trillion, an estimate), inside the ledger's housing title.

### HOU-6.02 The condition on new transportation money

- **What it does.** A share of the new money in Moving America's 2031 authorization goes only to places that adopt the reforms the Innovation Fund rewards.
- **Limit.** The condition applies to new and incremental money only, never to existing base grants, to stay inside the Supreme Court's coercion limit in *NFIB v. Sebelius* (legacy design).
- **Vehicle.** Regular bill: Moving America's 2031 authorization carries the matching clause.
- **Cost.** None (ledger row HOU-7, the floor bill).

### HOU-7B.01 The investor limit, left as enacted

- **What it does.** No change. The ROAD to Housing Act's ban on large investors buying more single-family homes runs from January 7, 2027 until its repeal on January 7, 2042 [EV-HOU-222]. Its reporting stays as enacted [EV-HOU-224].
- **Next decision.** The plan decides whether to make the ban permanent after the GAO and HUD reports in 2037 (point 8).
- **Vehicle.** None.

## 6. Housing tax credits (option D)

Espen chose memo 3 part 1's option D (`DEC-2026-11-09-08`): a bit of all three credits, each where it adds homes. The bills, evidence and variants are in `memo-3-part1-research.md`. Section 6 prices the four provisions together at about $0.12 trillion over FY2030-39 (`6-cost.md`, 4). None has a JCT score. GAO's middle-income housing study is due July 11, 2027 [EV-HOU-242], before the plan starts; HOU-2D.02 is re-read against it before its parameters are final.

### HOU-2D.01 A bigger low-income credit with the boost for the poorest renters

- **What it does.** Raises the states' low-income housing tax credit allocations beyond the 2025 law's permanent 12% increase [EV-HOU-260], on the Affordable Housing Credit Improvement Act's design (S. 1515, H.R. 2725): a per-resident allocation of $4.25 in 2025, then 1.25 times that, indexed [EV-HOU-262], net of what the 2025 law already enacted.
- **The boost for the poorest renters.** A 50% basis boost, to 150% of eligible basis, for buildings where at least 20% of the homes serve households at or below 30% of area median income or the poverty line [EV-HOU-263]. This is the best-supported piece, because it is where the rent limit binds hardest [EV-HOU-118] (memo 3).
- **Tribal and rural areas.** The bill's treatment of tribal areas as high-cost areas with a basis boost, which the 2025 law dropped, is kept (`DEC-2026-11-09-16`; HOU-4.13) [EV-HOU-263]. Proposed, for Espen: keep the same treatment for rural areas.
- **Attached help.** In tight markets, new credit homes are eligible for HOU-4.04's attached awards, which reach extremely low-income tenants [EV-HOU-118].
- **Evidence.** Nationally about eight in ten credit homes replace homes that would have been built anyway, but much less in dense places [EV-HOU-275] [EV-HOU-277] [EV-HOU-115].
- **Cost source.** Section 6: about $0.10 trillion over FY2030-39 (range $0.08-0.12 trillion; legacy estimate HOU-2B), permanent.

### HOU-2D.02 A middle-income credit in high-cost areas, a 2030-34 trial

**Parameters** (memo 3 part 1 D; research variants M2 to M5):
1. **Where.** Only in high-cost areas: the difficult development areas the low-income credit already uses, and metros where rents for new buildings exceed 30% of area median income [EV-HOU-274]. States with no eligible area move their share to the low-income credit [EV-HOU-266].
2. **A real discount.** Restricted rents at least 10% below a documented market rent for comparable new homes, checked at award [EV-HOU-280]. The 10% line is judgment (memo 3).
3. **Who.** Households from 60% to 100% of area median income, averaging 80%, on the bill's rent rule of at most 30% of the income limit [EV-HOU-264]. The band follows research variant M2.
4. **Affordable for good** (HOU-2D.04).
5. **First call** for places that win memo 4's zoning reward (HOU-6.01), so the credit and by-right zoning attack land and building costs together [EV-HOU-279].
6. **Size and term.** Awards in 2030-34 only, at half the bill's allocation, about $0.50 per resident a year, with the bill's credit of 50% of basis in present value over 15 years [EV-HOU-265] [EV-HOU-266].
7. **Evaluation.** Part of each year's awards is given by lottery, as Missouri's neighborhood credit was [EV-HOU-284], so the trial measures whether it adds homes. It is renewed only if it does. An interim report comes by 2034, before any renewal, and a final one by 2037 (`DEC-2026-11-09-14`).

- **Cost source.** Section 6: about $7 billion over FY2030-39, with claims on the five years of awards running to about 2048.

### HOU-2D.03 The neighborhood homes credit, a 2030-34 trial

- **What it does.** As the Neighborhood Homes Investment Act writes it (S. 1686, H.R. 2854): a credit that fills the gap between what it costs to build or repair a home and what it sells for, capped at 40% of costs and at 32% of the national median new-home price [EV-HOU-268].
- **Where and for whom.** Tracts with low incomes, high poverty and low home values; buyers at or below 140% of area median income; $9 per resident a year, at least $12 million per state [EV-HOU-269].
- **Term.** Awards in 2030-34, with an evaluation; renewed if homes get built at a reasonable cost (memo 3). The evaluation watches cost per home, CRS's main concern about a gap-filling credit [EV-HOU-271].
- **Evidence.** Missouri's lottery-awarded analogue raised building and showed about half of each credit dollar in the home's value [EV-HOU-284].
- **Cost source.** Section 6: about $15 billion over 2030-34 by CRS's method [EV-HOU-270].

### HOU-2D.04 Permanent affordability for every rental home the plan pays for

- **What it does.** Every rental home that receives a new credit allocation under HOU-2D.01 or HOU-2D.02 from 2030 stays rent-restricted for good, through a recorded use restriction, and a nonprofit or public owner has the right to buy at a price that keeps the restriction, as for the homes HOU-3C.03 covers. About a third of today's 2.5 million credit homes leave their rent limits by 2035 [EV-HOU-119].
- **Trade-off.** Some developers will not apply, and the credit buys somewhat fewer homes per dollar (research variant M4).
- **Current law.** The credit's compliance and extended-use periods, and the exits from them, are not yet read from the statute into the register (evidence still needed).

**Vehicle and agency for HOU-2D.** R2, as revenue: the credits are tax-code changes. The affordability rules ride R2 as conditions on the credits; if any is struck as merely incidental to the budget, the regular bill carries it (judgment). Treasury (IRS) runs the credits, with the state allocating agencies.

## Interactions with the rest of the plan

Espen asked how housing lands with the home health coverage expansion, child care, the expanded child tax credit and the secure floor, for each group in need (`DEC-2026-11-09-06`). This table states the mechanism and the check. The figures belong to the household model and section 7; none is estimated here.

| Group | What housing gives | Health coverage (HLT-1, HLT-4) | Child care (FAM-2) | Child tax credit (FAM-1) | Secure floor and other help | Checks for section 7 and the household model |
| --- | --- | --- | --- | --- | --- | --- |
| Families with children | Stage 1 (homeless families) and stage 2 (2030-37); attached homes outside poor areas; search help | Children's continuous coverage (HLT-4) can supply the Medicaid income finding the common application reuses (HOU-4.02) | FAM-2's cap lowers child care costs. Current law deducts child care costs from income when setting rent, so lower costs can raise rent slightly (deduction in 42 U.S.C. 1437a(b)(5); not yet checked) | Monthly advance credit is not counted for rent (26 U.S.C. 6409); no rent offset | Paid leave (FAM-3) and wage gains count as income unless excluded (shared rule 1) | Combined effect on net income and rent for a family on a voucher with FAM-1, FAM-2 and FAM-3; stacked phase-out rate (shared rule 2); stage 2's reach to children by age |
| The lowest-income households | The guarantee's stages; HOU-1D for crises | Restored Medicaid (HLT-1) is a route into HOU-1D's eligibility by enrollment (HOU-1D.01) | As above | As above | New income support outside the tax code raises rent by up to 30 cents per dollar unless excluded (shared rule 1) | Rent offset at 0 and 30 cents per dollar of new benefits; which households fall in no stage in the 2030s (memo 2 B) |
| Immigrants | Section 214 rules with proration for mixed-status families, protected in statute against HUD's February 2026 proposed rule (HOU-4.01, `DEC-2026-11-09-10`); the shared record holds no status and is barred from immigration enforcement use (HOU-4.02, `-11`) | Coverage rules follow the health dossier and the immigration table | FAM-2's own rules | FAM-1's taxpayer-identification rules | IMM-1's new statuses are not on Section 214's list unless the law adds them (shared rule 3) | One eligibility table across housing, health, FAM-1 and FAM-2 for each status; how many mixed-status families with children in stages 1-2 get prorated help |
| People currently and chronically homeless | Stage 1 first; Housing First (HOU-4.09); attached homes ready to enter; supportive housing with a navigator duty on providers (HOU-4.11) | Medicaid services offered on entry (shared rule 7); HLT-4's health centers | — | Homeless families may not file taxes; the common application offers FAM-1 enrollment (HOU-4.02) | Coordinated entry hands off to the guarantee | Share of homeless households reached by 2033; FAM-1 take-up among homeless families; asylum-seeker shelter demand left to the immigration dossier [EV-HOU-062] |
| People with substance use disorders | Housing without treatment conditions; voluntary recovery housing that accepts residents on prescribed medicines (HOU-4.10); treatment access in supportive housing (HOU-4.11) | Medicines for opioid use disorder and contingency management depend on what Medicaid covers. Tenancy supports and assertive community treatment are asked of HLT-4 (HOU-4.12). Restoring Medicaid (HLT-1) protects coverage from the 2027 work requirements | — | — | No treatment condition anywhere (shared rule 6) | Outcomes for people with active addiction (HOU-4.10's evaluation); whether treatment capacity is in place where HOU-4A's stage 1 lands |
| Older and disabled people | Stage 3 from 2038 for disabled extremely low-income renters (HOU-4.08); accessible homes (HOU-3C.03). Older renters who are not disabled have no funded route in the 2030s; they are reconsidered once the care program is scoped (`DEC-2026-11-09-10`) | HCBS (HLT-4) delivers the services stage 3 depends on. Medicare's out-of-pocket cap (HLT-2) may lower the medical-expense deduction older and disabled tenants take, and so raise rent slightly (not yet checked) | — | — | Social Security protection and SSI count as income for rent | Older unassisted renters with severe needs left without help through 2039 (memo 8); the medical-deduction effect; reserved accessible units against stage 3 demand |

**Cross-dossier checks to run** (section 7 and the household model):
1. **Rent offsets.** Each new benefit from flagships 1 and 2, at 0 and 30 cents per dollar (shared rule 1). The secure floor decides which are excluded.
2. **Deductions that shrink.** The child care deduction under FAM-2 and the medical-expense deduction under HLT-2. Read 1437a(b)(5) and 24 CFR 5.611 first.
3. **Stacked phase-outs.** For a voucher family with earnings, across housing, FAM-1, FAM-2, health subsidies and SNAP (shared rule 2).
4. **One immigrant eligibility table** across housing, health and family programs (shared rule 3, owned by immigration). This includes HOU-1D's rule, which this section leaves open.
5. **Reach and order.** HOU-4.03 by race, place, disability and children's age (memo 8). Homeless reach by 2033.
6. **Services in place.** Medicaid HCBS (with tenancy supports, HOU-4.12), addiction treatment and the behavioral health workforce where stage 1 and stage 3 land (care flagship). The health coverage model should count supportive-housing tenants as a high-use Medicaid group.
7. **Common application.** Whether one housing application can share income findings with Medicaid, SNAP and FAM-1 under current law (democratic renewal, CAP-13).
8. **Construction workforce.** Supply under a smaller construction workforce (fork 7; immigration and work dossiers) [EV-HOU-055].

## Consistency check

Each decided item, the provisions that carry it, and where its cost comes from. Figures are section 6's central estimates over FY2030-39 (`6-cost.md`, 1.2) unless marked.

| Decided item | Provisions | Vehicle | Years | Cost source |
| --- | --- | --- | --- | --- |
| Memo 1 B: tool matched to market | HOU-4.04, HOU-3C.03 | R2 (conditions) | Attached awards from 2032 | No separate cost; inside HOU-4A and HOU-4D |
| Memo 2 B: stage 2 guarantee | HOU-4D.01 | R2, mandatory | Enrollment 2034-36; a right from 2037 | $81 billion (ledger: `recovery-adoption.json` `housing_extra_tn` 0.135, booked from 2030; section 6 proposes retiming) |
| Memo 2 condition: stage 3, disabled renters | HOU-4.08, HOU-3C.03 | R2 (effective 2038) | From 2038 | $5 billion in FY2038-39; about $14 billion a year by FY2042; outside the $135 billion |
| Memo 8: order and pace | HOU-4.03, HOU-4A.01 | R2 | 2030-33 at 250,000 a year, then as above | HOU-4A $147 billion with fees (legacy working midpoint $162.2 billion; ledger `HOU-1/additional-600000-voucher-awards` 0.09) |
| Memo 8: harmonization | HOU-4.02 | R2 (admin money); regular bill (data and privacy) | From 2030 | Inside HOU-4A.02 and HOU-1D.03, plus the federal administration set-aside ($2 billion) |
| Memo 6 C: standing fund and start | HOU-1D.01 to .04 | R2, mandatory; regular bill (privacy) | Start 2030-31; standing from 2031 | $15 billion one-time and $49 billion standing; ledger `HOU-1/legacy-housing-title` still carries HOU-1A's $85 billion |
| Point 5: delivery rules | HOU-1D.01 to .03 | R2; regular bill (privacy) | From 2030 | Inside HOU-1D |
| Point 4: legal help | HOU-1D.01 | R2 | From 2030 | Inside HOU-1D |
| Memo 5 B: Housing First and recovery; supportive housing (parameters adopted, `DEC-2026-11-09-10`) | HOU-4.09 to HOU-4.12 | Executive action and rule; regular bill; R2 (recovery 2030-34; HUD services backstop 2030-39); care flagship's bill (Medicaid services) | From January 2029 | Recovery housing $1.5 billion; backstop $6 billion, plus $6 billion for the wider backstop through 2035 (placeholders) |
| Memo 3 part 1 D: tax credits (`DEC-2026-11-09-08`) | HOU-2D.01 to .04, HOU-3C.03 | R2 (revenue and credit conditions); regular bill if a condition is struck | Low-income credit permanent; trials awarded 2030-34 | About $0.12 trillion: $0.10 trillion low-income, $7 billion middle-income, $15 billion neighborhood; needs a JCT score |
| Memo 3 part 2: small builder | HOU-9A.01 | Regular bill; R2 (capital) | Authorized 2029-30 | Placeholder $5 billion |
| Memo 3 part 3 B: construction money with acquisition | HOU-3C.01 to .03 | R2 (C21 borrowing for grants; credit subsidy for loans) | Grants awarded 2030-37, loans committed 2030-38, spent by 2039 (`DEC-2026-11-09-09`) | Grants $70 billion and loan subsidy $14 billion of outlays (legacy about $0.075 trillion, inside ledger title 0.47) |
| Memo 4 B: zoning reward | HOU-6.01, HOU-6.02 | R2 (money); regular bill (eligibility; transportation condition) | 2030 on; condition with Moving America 2031 | $25 billion of outlays (legacy about $0.03 trillion inside the title); ledger HOU-7 (floor bill, no cost) |
| Point 1: neighborhood payment limits | HOU-4.05 | Rule, then regular bill | 2030-32 | No new money; effect on cost per award unpriced |
| Point 2: source-of-income protection, with testing money (`DEC-2026-11-09-10`) | HOU-4.06 | Regular bill; R2 (testing money 2030-34) | From 2030 | Testing money about $0.5 billion (placeholder) |
| Point 3: search help | HOU-4.07 | R2, mandatory; appropriations (evaluation) | From 2030 | $8 billion |
| Point 6: repair first, right to return | HOU-5.02, HOU-5.01 | Regular bill; R2 (conditions) | Repair awarded 2030-37 (`DEC-2026-11-09-09`) | HOU-5 $57 billion of outlays (legacy about $0.06 trillion, C31) |
| Point 7: no residency rules | HOU-4.01, HOU-4.03 | R2 (conditions); regular bill | — | None |
| Point 8: investor limit as enacted | HOU-7B.01 | None | Through 2042; revisit after 2037 | None |
| Fork 7: construction workforce | Interactions, check 8 | — | — | — |
| `DEC-2026-11-09-09`: FY2040 gap to the financing settlement; capital spent by 2039 | HOU-3C.01, HOU-3C.02, HOU-5.01 (timing) | — | Awards end 2037-38 | FY2040: about $90 billion of permanent cost, with stage 2's wider entry; the capital tail falls from about $16 billion to about $8 billion (`6-cost.md`, 3.3) |
| `DEC-2026-11-09-10`: duty to house from 2037 | HOU-4D.01, HOU-4.07 | R2 | From 2037 | About $3 billion in FY2037-39 (placements) |
| `DEC-2026-11-09-10`: production targets (three numbers, Espen in session November 9) | HOU-3C.04 | Regular bill; R2 (reporting) | 2030-39 | None |
| `DEC-2026-11-09-10`: mixed-status protection; repeal of HUD's proposed rule | HOU-4.01 | Executive action (January 2029); regular bill | From 2029 | None against current law |
| `DEC-2026-11-09-10`: tribal housing | HOU-4.13, HOU-1D.03, HOU-3C.01, HOU-3C.02, HOU-4A.01, HOU-4D.01, HOU-2D.01 | R2 (set-asides); regular bill (NAHASDA rules) | From 2030 | Shares of existing amounts; no added cost |
| `DEC-2026-11-09-10`: older non-disabled renters reconsidered after the care program is scoped | HOU-4.03 | — | — | None yet |
| `DEC-2026-11-09-10`: section 5's delivery items | HOU-4.02 (R1 readiness), HOU-4.12 (wider backstop), HOU-4.06 (testing), HOU-4D.01 (deemed approval; private right of action), HOU-5.02 and HOU-4.11 (private rights of action) | R1; R2; regular bill | 2029 on | Readiness $0.75 billion in FY2029; others above; attorney's fees and deemed approval's error cost unpriced |
| `DEC-2026-11-09-11`: the record holds basic information only, with an enforcement bar; stage 2's exit at 80% of area median income | HOU-4.02, HOU-4D.01 | Regular bill; R2 | From 2030 | None separately; the exit rule is inside stage 2's flat count |
| `DEC-2026-11-09-12`: stage 1's plain test, doubled-up families with children included, no cap; stage 2 widened to them and to homeless families | HOU-4.03, HOU-4D.01 | R2 | From 2030; stage 2 from 2034 | About $17 billion over FY2030-39 and $8 billion in FY2040 (`6-cost.md`, 2.7) |
| `DEC-2026-11-09-14`, `-16`, `-17`: the proposed parameters decided (production targets; tribal set-aside sizes; the emergency fund's annual cap of four months' Fair Market Rent and repeat-use review; testing money; R1 readiness; duty-to-house deadline; record and penalty rules; stage 3 disability proof; local intake order; trial report dates); the bond-deal basis boost left out | HOU-3C.04, HOU-4.13, HOU-1D.01, HOU-4.06, HOU-4.02, HOU-4D.01, HOU-4.08, HOU-4.03, HOU-2D.01, HOU-2D.02 | As each provision | As each provision | Testing $0.5 billion and R1 readiness $0.75 billion (section 6); the rest no added cost |

**Consistency notes.**
- **Totals.** The ledger's housing title ($0.56 trillion midpoint: the $0.47 trillion title and $0.09 trillion of vouchers) predates every section 3 decision. It still carries HOU-1A, HOU-2A and HOU-6's separate fund as filed. HOU-4D is carried outside the ledger in `recovery-adoption.json`. Section 6 rebuilds them from this section's provisions: about $0.65 trillion over FY2030-39 (central, with option D's credits) and about $90 billion a year of permanent cost in FY2040, with stage 2's wider entry under `DEC-2026-11-09-12`. Its ledger and model changes are tier-3 proposals (`6-cost.md`, 5).
- **Regular-bill items.** HOU-4.01's definitions and mixed-status protection, HOU-4.02's data rules and enforcement bar, HOU-4.05, HOU-4.06, HOU-4.09, HOU-4.11, HOU-4.13's NAHASDA rules, HOU-1D.03's privacy rules, HOU-3C.04's target, HOU-5.02, HOU-6.01's eligibility changes, HOU-6.02 and HOU-9A.01's corporation. With the legacy floor bill (ledger row HOU-7), they make one housing regular bill. Its floor time is a section 5 question.
- **Still open for Espen.** Whether HOU-1A's construction gap money is dropped or added to HOU-3C (HOU-1D.04).
- **Proposed, for Espen** (parameters the decisions leave open): each state's share of the direct production count (HOU-3C.04), and the low-income credit's high-cost boost for rural areas (HOU-2D.01; the tribal boost is decided). Espen decided the other parameters this section had proposed in `DEC-2026-11-09-14`, `-16` and `-17`.
- **Section 4's own judgment.** The tight-market and attached-share parameters (HOU-4.04), the youngest-child part of stage 2's exit rule (HOU-4D.01), the capital's yearly splits (HOU-3C.01, HOU-3C.02, HOU-5.01), HUD as the emergency fund's agency (HOU-4.02), and the form rules for tribal shares (HOU-4.13).

## Evidence still needed

- Section 504 accessibility minimums and the project-based voucher rules (choice mobility, the share cap), from the regulations. HOU-4.04 and HOU-3C.03 rely on them.
- 42 U.S.C. 1437f(o) and 1437a(b)(5): the voucher tenant payment and the deductions (shared-rules open check).
- Any evaluation of recovery housing (HOU-4.10) and of attached rental help in tight markets (HOU-4.04).
- The gaps the supportive-housing note lists: per-unit service cost and national need, and homeless-services wages and turnover.
- Rural and tribal housing: a count of tribal homes needing repair or replacement, the Native American Housing Block Grant's level against it, and NAHASDA's text, to size HOU-4.13's set-asides from need (already a gap in `1-problem.md` and `3-design.md`).
- The low-income credit's compliance and extended-use rules (26 U.S.C. 42), for HOU-2D.04; GAO's middle-income housing study (July 2027) for HOU-2D.02 [EV-HOU-242].
- The tax code's taxpayer-information penalties (26 U.S.C. 7213, 7431), the model proposed for HOU-4.02's enforcement bar.
- The search-help design research (HOU-4.07).
