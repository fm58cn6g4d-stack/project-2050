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
| HOU-4.01 | Shared rules for all housing help (income, income lines, immigrant eligibility, verification, conditions), with the mixed-status protection | Decided by reference; working answers per `shared-rules.md`; mixed-status protection decided (`DEC-2026-11-09-10`); voucher rent ignores free or capped child care (`DEC-2026-11-10-03`) | Regular bill (definitions) and R2 (as conditions on the new money) |
| HOU-4.02 | One rental help system: the guarantee, vouchers and emergency rent help harmonized | Decided (memo 8); the record's contents and enforcement bar (`DEC-2026-11-09-11`); R1 readiness money (`-10`) | R1 (readiness); R2 (money and conditions); regular bill (data sharing and privacy) |
| HOU-4.03 | The order of reach, with a stated route for the 2040s | Decided (memo 8; point 7; stage 1's test `DEC-2026-11-09-12`; the 2040s route `DEC-2026-11-10-03`, its date and pace `DEC-2026-11-10-04`) | R2; regular bill (the 2040s route) |
| HOU-4.04 | Matching the tool to the market: tight-market rule, attached help, right to move | Decided (memo 1 B) | R2 |
| HOU-4.05 | Payment limits by neighborhood | Decided (point 1) | Regular bill or HUD rule; no new money |
| HOU-4.06 | National source-of-income protection, with testing money for 2030-34 | Decided (point 2; testing money `DEC-2026-11-09-10`) | Regular bill; R2 (testing money) |
| HOU-4.07 | Search help with every new award | Decided (point 3); design research open | R2 (mandatory fee); appropriations (evaluation) |
| HOU-4.08 | Stage 3: extremely low-income renters with long-term disabilities, of any age, from 2038 | Decided (memo 2 condition; 62 and over and the severe-problems test `DEC-2026-11-10-03`); definition and services with the care flagship | R2 (authorized now, effective 2038); section 6 and the financing settlement |
| HOU-4.09 | Housing First as the federal rule for homelessness help, with the no-sweeps condition | Decided (memo 5 B; no-sweeps condition `DEC-2026-11-09-10`) | Executive action (January 2029); regular bill |
| HOU-4.10 | A voluntary recovery-housing option, evaluated | Decided (memo 5 B) | R2 (mandatory, time-limited); appropriations |
| HOU-4.11 | Supportive housing: an engagement standard (a duty on providers) and treatment access | Decided (memo 5 B; parameters adopted, `DEC-2026-11-09-10`) | Executive action and rule (2029); regular bill |
| HOU-4.12 | Services and workforce for supportive housing | Decided (parameters and the wider backstop through 2035, `DEC-2026-11-09-10`) | Care flagship's bill (Medicaid); R2 (HUD backstop) |
| HOU-4.13 | Tribal housing: set-asides, through tribes, by self-determination | Decided (`DEC-2026-11-09-10`; sizes `DEC-2026-11-09-16`) | R2 (set-asides); regular bill (NAHASDA rules) |
| HOU-4A.01 | One million new awards, 2030-33 (stage 1 and the start of stage 2) | Decided (memos 1, 2, 8) | R2, mandatory |
| HOU-4A.02 | Housing agency administration for the new awards | Decided with HOU-4A (legacy allowance) | R2, mandatory |
| HOU-4D.01 | Stage 2: a guarantee for the poorest families with children, enrolled 2034-37, with the duty to house from 2037 | Decided (memo 2 B; duty to house and remedies `DEC-2026-11-09-10`; exit line `-11`) | R2, mandatory |
| HOU-1D.01 | Standing emergency-rent fund: eligibility, uses and caps | Decided (memo 6 C; point 5 rules 1 and 3; point 4; about $5 billion a year, `DEC-2026-11-10-03`) | R2, mandatory |
| HOU-1D.02 | How the fund pays: risk screen, self-attestation and checks, landlord applications | Decided (point 5 rules 2, 4, 5) | R2 |
| HOU-1D.03 | Accountability: grantee network, payment-error measurement, data standard | Decided (point 5 rules 6-8) | R2 (money and conditions); regular bill (privacy and record links) |
| HOU-1D.04 | The one-time start, 2030-31 | Decided (memo 6 C; about $15 billion, and HOU-1A's construction gap money dropped, `DEC-2026-11-10-03`) | R2, mandatory |
| HOU-3C.01 | State housing revolving funds: about $72 billion of grants, awarded by 2037 | Decided (memo 3 part 3 B; timing `DEC-2026-11-09-09`) | R2, mandatory (borrowed inside the D4-B envelope, C21) |
| HOU-3C.02 | Federal construction and acquisition loans: $300 billion, committed by 2038 | Decided (memo 3 part 3 B; timing `DEC-2026-11-09-09`) | R2 (credit subsidy) |
| HOU-3C.03 | Lasting affordability, attached help and accessible homes in plan-financed buildings | Decided (memo 3 part 3 B; memo 1 B; memo 2 condition; tax-credit homes `DEC-2026-11-09-08`) | R2 (grant and loan conditions) |
| HOU-3C.04 | Published production targets: homes the plan pays for, homes in zoning-reward places, and a national goal | Decided (`DEC-2026-11-09-10`; three numbers `DEC-2026-11-09-14`; the numbers `DEC-2026-11-09-17`); each state's expected count is its money divided by its own cost per home (`DEC-2026-11-10-03`) | Regular bill (the targets); R2 (reporting conditions) |
| HOU-5.01 | Public housing repair | Legacy working choice; timing `DEC-2026-11-09-09` | R2, mandatory (C31) |
| HOU-5.02 | Repair first, one-for-one replacement and a right to return with no re-screening | Decided (point 6) | Regular bill; R2 (conditions on the repair money) |
| HOU-6.01 | The zoning reward through the ROAD to Housing Act's Innovation Fund | Decided (memo 4 B; ends with its FY2030-39 money unless renewed, `DEC-2026-11-10-03`) | R2 (money); regular bill (who may apply, what is paid for) |
| HOU-6.02 | The condition on new transportation money | Decided (memo 4 B) | Regular bill (Moving America's 2031 authorization) |
| HOU-7B.01 | The investor limit left as enacted | Decided (point 8) | None |
| HOU-8.01 | Social housing pilot | Legacy working choice; a size target and an evaluation date (`DEC-2026-11-10-03`; the numbers `DEC-2026-11-10-04`) | R2 (through HOU-3C.02 and a small equity grant) |
| HOU-9A.01 | A small federal builder from 2029 | Decided (memo 3 part 2, A-small) | Regular bill (the corporation); R2 (capital and loan authority) |
| HOU-2D.01 | A bigger low-income credit with the boost for the poorest renters | Decided (memo 3 part 1 D, `DEC-2026-11-09-08`); the rural high-cost boost is left out (`DEC-2026-11-10-03`) | R2 (revenue) |
| HOU-2D.02 | A middle-income credit in high-cost areas, a 2030-34 trial | Decided (`DEC-2026-11-09-08`) | R2 (revenue) |
| HOU-2D.03 | The neighborhood homes credit, a 2030-34 trial | Decided (`DEC-2026-11-09-08`) | R2 (revenue) |
| HOU-2D.04 | Permanent affordability for every rental home the plan pays for | Decided (`DEC-2026-11-09-08`) | R2 (credit conditions); regular bill |
| HOU-10.01 | Down payment help for first-time buyers through state housing finance agencies, 2030-39 | Decided (memo 9 part 1 C, with Espen's two changes, `DEC-2026-11-09-19`); income limits decided by Espen, `DEC-2026-11-09-24`; capped at $25,000, or $30,000 for a new home, within FHA's loan limit (`DEC-2026-11-10-03`) | R2, mandatory, time-limited |
| HOU-10.02 | FHA's annual premium on purchase loans cut to 0.30% for loans endorsed 2030-39, with a safety line and a review | Decided (memo 9 part 2 B, `DEC-2026-11-09-19`); safety line decided by Espen, `DEC-2026-11-09-24`; through 2039 with a review (`DEC-2026-11-10-03`) | R2 (credit subsidy) or regular bill; CBO decides how it scores |
| HOU-3C.05 | Homes to buy: up to $30 billion of the construction loans for starter homes and condos, and revolving-fund grants for resale-limited homes | Decided (memo 9 part 3 C, `DEC-2026-11-09-19`) | R2 (inside HOU-3C's amounts) |
| HOU-11.01 | Cheaper loans for manufactured homes | Decided (memo 10 part 2 B, `DEC-2026-11-09-20`); grant amount decided by Espen, `DEC-2026-11-09-24` | FHFA action (2029); regular bill; R2 (community grants) |
| HOU-11.02 | Federal land near growing western cities sold at fair value for housing | Decided (memo 10 part 3 B, `DEC-2026-11-09-20`); proceeds split decided by Espen, `DEC-2026-11-09-24` | Regular bill |
| HOU-11.03 | Assisted infill housing excluded from federal environmental review | Decided (memo 10 part 4 B, `DEC-2026-11-09-20`) | Regular bill |
| HOU-12.01 | The home repair fund for low- and moderate-income owners, 2030-39 | Decided (memo 11 part 1 C, `DEC-2026-11-09-21`); amounts decided (`DEC-2026-11-09-25`) | R2, mandatory, time-limited |
| HOU-12.02 | Repairs for renters: landlord loans with a light rent term, city repair funds, receivership, relocation help | Decided (memo 11 part 2 B, `DEC-2026-11-09-21`); loan limits decided (`DEC-2026-11-09-25`) | R2 (inside HOU-12.01) |
| HOU-12.03 | One front door with the clean-power programs; the fund pays readiness repairs | Decided (memo 11 part 3 B, `DEC-2026-11-09-21`) | Regular bill; R2 (inside HOU-12.01) |
| HOU-12.04 | Older adults: repairs and home changes on the CAPABLE model | Decided (memo 12 part 2 B, `DEC-2026-11-09-22`) | R2 (inside HOU-12.01) |
| HOU-13.01 | A federal match for state property-tax relief for older owners, with deferral | Decided (memo 12 part 1 B, `DEC-2026-11-09-22`); threshold and maintenance of effort decided (`DEC-2026-11-09-25`) | R2, mandatory, permanent |
| HOU-13.02 | Protecting older owners' equity: legal help, reverse-mortgage relief in law, a payment plan before tax sales | Decided (memo 12 part 3 B, `DEC-2026-11-09-22`); amount decided (`DEC-2026-11-09-25`) | R2 (grants); regular bill |
| HOU-13.03 | Service coordinators in older renters' buildings | Decided (memo 12 part 4 C, `DEC-2026-11-09-22`); amount decided (`DEC-2026-11-09-25`) | R2, mandatory, permanent |
| HOU-13.04 | Home-sharing grants | Decided (memo 12 smaller point 2, `DEC-2026-11-09-22`); amount decided (`DEC-2026-11-09-25`) | R2, mandatory, time-limited |
| HOU-3C.06 | Homes for older and disabled renters inside HOU-3C, by each state's need | Decided (memo 12 part 4 C, `DEC-2026-11-09-22`) | R2 (inside HOU-3C's amounts) |
| HOU-14.01 | Rural Development's field staff, local decisions and one loan system, 2030-39 | Decided (memo 13 part 1 B, `DEC-2026-11-10-02`) | R2, mandatory, time-limited; then appropriations |
| HOU-14.02 | Section 502: direct loans at scale, to 100% of area median income; guaranteed loans to HOU-10.01's limits | Decided (memo 13 part 2 C, `DEC-2026-11-10-02`) | R2 (credit subsidy); regular bill (income limits) |
| HOU-14.03 | Rural rental homes: rent help after every mortgage ends, vouchers, a preservation fund | Decided (memo 13 part 4 B, `DEC-2026-11-10-02`) | R2 (fund); appropriations (rental assistance, vouchers) |
| HOU-14.04 | Self-help and farmworker housing, 2030-39 | Decided (memo 13 part 5 B, `DEC-2026-11-10-02`); the immigration-status rule left for later | R2, mandatory, time-limited |
| HOU-14.05 | One rural test for housing, up to 35,000 people, with no one losing eligibility | Decided (memo 13 part 6 B, `DEC-2026-11-10-02`, as Espen qualified it) | Regular bill |
| HOU-14.06 | Day-one rule changes at USDA, 2029 | Decided (memo 13, "Day one", `DEC-2026-11-10-02`) | Executive action and rule |

## 1. Rules shared by all housing help

### HOU-4.01 Shared rules, kept in one place

Every provision below that tests income, status or need uses the definitions here. Each rule's owner dossier can change it without a rewrite (`shared-rules.md`).

| Rule | Working answer in this dossier | Range tested | Owner |
| --- | --- | --- | --- |
| Income for rent (shared rule 1) | Current law: tenants pay 30% of adjusted income (42 U.S.C. 1437a(a)(1)). Refundable tax credits paid in advance, the child tax credit included, are not income (26 U.S.C. 6409). Assume no new benefit from another flagship raises rent. **Voucher rent ignores the value of free or capped child care** (`DEC-2026-11-10-03`): where FAM-2 makes a family's care free or caps its cost, the rent calculation keeps the child care deduction at what the family would pay without FAM-2, using a standard amount per child in care that HUD publishes each year by area from the care program's own payment rates, so no receipts are needed (judgment on the form; the care and secure floor dossiers may choose another form that gives the same result) | No effect, up to 30 cents per dollar of any new benefit paid outside the tax code | Secure floor (flagship 1); the child care rule with care (flagship 2) |
| How fast help falls (rule 2) | 30 cents per added dollar of adjusted income. Increases in earnings are counted at the annual review. No new phase-out | Set by the secure floor's ceiling on combined phase-out rates | Secure floor, with the household model |
| Immigrant eligibility (rule 3) | Current law for HOU-4 and HOU-4A/4D: Section 214's list (42 U.S.C. 1436a), with help prorated for mixed-status families, protected as below (`DEC-2026-11-09-10`). HOU-1D's rule is set by the immigration flagship's eligibility table; this section does not fix it. The owner and buyer programs follow current law's defaults, written out below ("Immigrant eligibility for the owner and buyer programs") | Section 214 up to the immigration flagship's table for new statuses | Immigration (flagship 6) |
| Income lines (rule 4) | Area median income. "Extremely low income" is the statutory line (1437a(b)(2)(C)). The emergency fund uses 50% of area median income or enrollment in a means-tested program (HOU-1D.01) | — | Secure floor (definitions); democratic renewal (common application) |
| Verification (rule 5) | Housing agencies verify, reusing income already found by TANF, Medicaid or SNAP (1437a(a)(7)(D)) and federal income-matching data (1437a(a)(7)(E)). HOU-4.02 extends reuse across the three housing programs | — | Democratic renewal (CAP-13) |
| Conditions (rule 6) | No work condition and no treatment condition on any housing help in this dossier (memo 5 B). The public housing community-service rule (42 U.S.C. 1437j(c)) does not apply to households housed under HOU-4A, HOU-4D or HOU-4.08 | — | Work (flagship 5) records the cross-program principle |
| Services (rule 7) | Services come through Medicaid and local programs. Housing pays only a services backstop for supportive-housing tenants without Medicaid (HOU-4.12) | — | Care (flagship 2, HLT-4) |
| Residency | No residency requirement and no preference by length of residence in any new program (point 7), as the voucher rules already require (24 CFR 982.207) [EV-HOU-189] | — | This dossier |

- **Mixed-status protection** (`DEC-2026-11-09-10`). A mixed-status family keeps prorated help for its eligible members for as long as it is otherwise eligible, as current regulations allow, and a member may decline to contend eligible status without ending the others' help. HUD's February 2026 proposed rule would make proration temporary, pending verification of every member [EV-HOU-402]; a HUD analysis of the draft found about 20,000 assisted mixed-status families affected, 16,000 with children, as reported [EV-HOU-403]. The executive action of January 2029 withdraws the proposed rule, or rescinds it if it is final by then. The regular bill writes both protections into Section 214 (42 U.S.C. 1436a), so a later rule cannot undo them. Espen's decision says the repeal may be in statute ("possibly in statute"); this section writes it there, as section 7 recommended (`7-validation.md`, 3.4). Executive action alone is the alternative. The immigration flagship still owns the wider eligibility table (rule 3).
- **Immigrant eligibility for the owner and buyer programs** (working answers under rule 3, for the immigration flagship's table; `review-milestone.md`, M-5). Section 214 covers rental help and USDA's direct loans, not the other owner programs [EV-HOU-806]. By default the 1996 welfare law's rule for federal public benefits, which include grants and loans paid with federal money, applies to them [EV-HOU-804], and a signed statement is only the first step where a provider must verify [EV-HOU-807]. So these programs' "signed statement, no further papers" covers income, first-time and first-generation status, age and need, not immigration status. Working answers, each current law unless the immigration flagship's table changes it:
  | Program | Rule by default | Who is checked, and how |
  | --- | --- | --- |
  | HOU-10.01 down payment help | Welfare-law rule for federal public benefits [EV-HOU-804] | The buyer named on the loan only. The state agency or lender checks status through the federal SAVE system or the loan file it already holds, not new papers from the buyer; a nonprofit provider need not verify [EV-HOU-805]. Other household members are never asked (design lens) |
  | HOU-10.02 FHA's premium | FHA's own residency rule: since 2025, U.S. citizens, permanent residents and citizens of the Freely Associated States (Micronesia, the Marshall Islands and Palau) only [EV-HOU-810] | The lender, as today. Whether the 2029 executive action restores FHA's earlier rule for lawful non-permanent residents is for the immigration flagship |
  | HOU-12.01 to .04 repair fund | **Working assumption** (the stopping rule, PR #190): the same default as HOU-10.01, the welfare-law rule for federal public benefits. *Basis:* the statute's text reaches any federal grant or loan to a household [EV-HOU-804]; HUD's November 2025 notice naming HOME and CDBG [EV-HOU-808] was set aside by a federal court in 2026, subject to appeal [EV-HOU-809], so it is not relied on either way. *What would change it:* HUD's pre-2025 reading of HOME and CDBG, which is not in the register, if it treated them as outside the rule; an appeal ruling; or the immigration flagship's table. *Cost of being wrong:* the fund's amount is fixed, so only who it reaches moves, not what it costs. If a check applies | The owner of record only, by the grantee through SAVE; nonprofit subrecipients need not verify [EV-HOU-805]. A renter household's repairs (HOU-12.02) are help to the landlord's building, so no tenant is asked |
  | HOU-13.01 property-tax match | Unsettled: the match is a payment to the state, and whether the state's relief is a federal or a state benefit, or a benefit at all, is not decided by any source found [EV-HOU-813] | The regular bill states that the match is a grant to the state for the state's own relief program, so the state's rule applies (judgment; legal review needed) |
  | HOU-14.02 Section 502 direct | Section 214, by statute [EV-HOU-806] [EV-HOU-811] | USDA, as today |
  | HOU-14.02 Section 502 guaranteed | USDA's rule: evidence of status as a citizen, non-citizen national or qualified alien [EV-HOU-812] | The lender, as today |
  - *For the immigration flagship's table* (`shared-rules.md`, rule 3): whether the new owner programs should reach mixed-status owner families the rental side protects (`DEC-2026-11-09-10`), for example by letting any eligible member be the applicant, as they already can be where the eligible member owns the home. This dossier proposes no new status rule.
- **Criminal-record screening for the new awards** (decided, `DEC-2026-11-10-06`; `review-milestone.md`, M-1). For households entering through HOU-4A, HOU-4D and HOU-4.08, the housing agency applies only the screening federal law requires: the two statutory bans, lifetime sex-offender registration and producing methamphetamine in assisted housing [EV-HOU-793] [EV-HOU-794], and the statute's mandatory drug rules as written, with their waivers. It does not use its discretionary authority to deny for other past criminal activity [EV-HOU-792] [EV-HOU-795]. The current right to see and dispute a record before denial stays (24 CFR 960.204(c)). This is the rule HOU-5.02 already uses for the right to return, which has no re-screening.
  - *Why.* Stage 1 is the plan's lowest-barrier door; agency screening beyond the statute would turn away at the agency the people leaving prison or jail whom the plain test names (HOU-4.03). HUD's 2024 proposal to require a look at recency and relevance before any discretionary denial was withdrawn in January 2025 [EV-HOU-796], and HUD's 2016 fair housing guidance on criminal records was withdrawn in 2025 [EV-HOU-797], so no current HUD rule or guidance limits blanket local bans; the Fair Housing Act itself, including its discriminatory-effects standard, still applies.
  - *What it does not cover.* A private landlord renting to a voucher holder still screens its own tenants; HOU-4.06's protection covers source of income, not records. Owners of plan-financed buildings (HOU-3C.03) admit households referred through the new awards on the same terms, and use an individualized review of recency and relevance for others (judgment).
  - *Evidence and its limits.* The register has no study of whether past records predict tenancy outcomes for voucher holders. A housing program for people leaving Ohio's prisons cut rearrests but not re-incarceration [EV-HOU-803].
  - *Vehicle.* The regular bill amends 42 U.S.C. 13661(c) for these awards; R2 carries it as a condition on the new money. No cost.
- **Vehicle.** The definitions are restated in a regular bill. In R2 they appear as conditions on the new money, which reconciliation can carry.
- **Changes to current law.** 1437a(b)(5) gains the standard child care deduction for families whose care FAM-2 makes free or caps (`DEC-2026-11-10-03`); nothing else in 1437a changes. Section 214 gains the mixed-status protection. The community-service rule binds only public housing residents, so it already misses voucher households. The new subsection disapplies 1437j(c) for households whose award is attached to a public housing unit, in redevelopment under HOU-5.02 or a social housing building. It rides the regular bill, because it has no budget effect.
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
2. **Stage 2 (HOU-4D.01 from 2034; HOU-4A.01 too, if stage 1 is served first).** Extremely low-income families with children with severe problems. Since stage 1 has no cap (`DEC-2026-11-09-12`), literal homelessness alone is expected to fill the million awards, so stage 2 starts in practice with HOU-4D.01 in 2034 (`research-doubled-up.md`, section 3; `6-cost.md`, 2.12).
3. **Stage 3 (HOU-4.08, from 2038).** Extremely low-income renters with long-term disabilities, of any age (`DEC-2026-11-10-03`). Older renters who are not disabled are reconsidered once the care program is scoped (`DEC-2026-11-09-10`), and are in the 2040s route below meanwhile.
4. **A stated route for the 2040s** (`DEC-2026-11-10-03`; the date and pace `DEC-2026-11-10-04`). Households with no funded stage get a next stage in law: extremely low-income renters with worst case needs outside stages 1-3 (single adults and other households who are not disabled, and older renters who are not disabled), and families with children between 30% and 50% of area median income with worst case needs. Enrollment opens in 2042 at up to 400,000 households a year, in HOU-4.03's order (most severe problems first), on stage 2's terms. The regular bill states the stage and its date; R2 does not fund it. HUD reports the count and cost with stage 3's opening in 2038, and the money is enacted only with its financing, as D4 requires. Section 6 gives its rough scale, about 3.3 million households and roughly $60 billion a year once fully enrolled (`6-cost.md`, 2.12). It makes the guarantee's limits visible and dated rather than open-ended (`7-validation.md`, question 7).

- **Within a stage.** In stage 1, local need-based intake decides the order, not quotas (`DEC-2026-11-09-12`). In stages 2 and 3, the order is memo 2 B's (`DEC-2026-11-09-01`): most severe problems first, then the youngest children, then date of application. That order is national guidance, with local need-based intake deciding, as in stage 1 (`DEC-2026-11-09-14`, under `DEC-2026-11-09-13`). The published counts (stage 1) and section 7's signals show whether the order works.
- **Local preferences.** Housing agencies may keep local preferences inside a stage, but not residency or length-of-residence rules (24 CFR 982.207) [EV-HOU-189] (point 7).
- **People at imminent risk** go to HOU-1D, not to this line (memo 8).
- **Who counts as "without a home"** (`DEC-2026-11-09-12`). One plain test, "no home of your own": people literally homeless, and families with children who are doubled up. A family shows it by its own word or by an existing school record. There is no deadline test and no cap. The order within stage 1 follows local need-based intake, not quotas. Counts are published yearly, and an imbalance two years running triggers a review, not an automatic restriction. Doubled-up families are where tenant vouchers do best at reaching people [EV-HOU-114]. Section 5 sets the forms.
- **People leaving prison, jail, a hospital, treatment or another institution, and youth leaving foster care** (`review-milestone.md`, M-1 and M-2). Anyone leaving with no home to go to has no home of their own, so the plain test already counts them; this section names them so local intake does not miss them. They may apply up to 90 days before release, or 180 days for youth leaving foster care, as HUD already allows for foster youth vouchers [EV-HOU-800], by their own word or the institution's or child welfare agency's discharge plan, so the award can be ready on the day they leave (judgment). State and federal prisons alone released 453,200 people in 2023 [EV-HOU-798]; formerly incarcerated people are homeless at about ten times the general rate on an advocacy group's estimate [EV-HOU-799], and 31-46% of youth aging out of foster care were homeless at least once by 26 [EV-HOU-802].
  - *Decided (`DEC-2026-11-10-06`):* someone leaving prison, jail or foster care for a relative's or friend's home, doubled up, also counts for the first 12 months after leaving. `DEC-2026-11-09-12` admits doubled-up households to stage 1 only when they have children, so this widens the test for two named groups. It changes who stage 1 houses first within the same million awards, not the cost (judgment).
  - *Foster youth vouchers.* The Family Unification and Foster Youth to Independence vouchers continue under current law: ages 18-24, up to 36 months plus up to 24 more [EV-HOU-800]; about 8,000 exist, and 64% were leased in June 2026 [EV-HOU-801]. When one ends at its time limit and the youth has no other home, the youth counts as without a home for HOU-4A's turnover awards, so the time limit never ends in the street (judgment).
  - *Screening.* The new awards use only the screening federal law requires (HOU-4.01, "Criminal-record screening for the new awards"; `DEC-2026-11-10-06`).
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
1. **Who.** Extremely low-income renter households (HOU-4.01), unassisted, with severe problems (stage 2's test), in which a member of any age has a long-term disability, as defined with the care flagship. Disabled renters 62 and over are included (`DEC-2026-11-10-03`). This dossier's placeholder is the voucher program's existing definition of a person with disabilities, pending that work. Receipt of SSI or SSDI, or Medicaid coverage on the basis of disability, counts as proof, with no new disability finding (`DEC-2026-11-09-14`). Many people 62 and over never had such a record; for them the voucher program's current verification applies, so the stage adds no new test (judgment). Honest errors are corrected, not punished (HOU-4D.01, item 8). *Severe problems* (`DEC-2026-11-10-03`): the household shows severe problems by its own statement of rent and conditions, with income found once (HOU-4.02, item 5), checked after award, as in stage 2 (HOU-4D.01).
2. **When.** Enrollment opens in 2038, after stage 2 is complete. The pace is set with the care flagship and section 6.
3. **Form.** Tenant-based vouchers, or awards attached to accessible homes reserved under HOU-3C.03. Help comes with home and community-based services offered through Medicaid (shared rule 7), never as a condition.
4. **Accessible homes.** See HOU-3C.03.

- **Vehicle.** Authorized in R2 with a 2038 effective date, so it is law from the start and its first two years fall inside the FY2030-39 window. The alternative is to enact it later in the care flagship's bill. Section 6 and the financing settlement decide the financing; it must be paid for from FY2040 under D4.
- **Evidence.** 1.16 million households with severe needs include someone under 62 with a disability [EV-HOU-032]. Extremely low-income renters make up most worst case needs [EV-HOU-185]. 1.749 million older extremely low-income renter households have worst case needs [EV-HOU-186], and 47% of HUD-assisted older households report a disability [EV-HOU-786].
- **Cost.** Section 6 (outside HOU-4D's $135 billion): under 62, about $5 billion in FY2038-39 and $14 billion a year by FY2042; 62 and over, about $5 billion and $14 billion more (`6-cost.md`, 2.1 and 2.12).

### HOU-4.09 Housing First as the federal rule

**Parameters** (memo 5 B):
1. In January 2029 the President revokes the July 2025 executive order's conditions [EV-HOU-107].
2. A regular bill makes Housing First the standard for homelessness help that HUD and HHS fund, including McKinney-Vento grants and the new awards: no requirement of treatment, sobriety or service participation to get or keep housing; services offered.
3. The National Strategic Plan due in July 2027 [EV-HOU-238] is reissued to match.
4. **No sweeps** (`DEC-2026-11-09-10`). Extending current law's precedent in the Emergency Solutions Grants [EV-HOU-237], new federal homelessness money does not go to places that remove people or their belongings without offering shelter or housing. The ROAD to Housing Act's version covers only FY2027-2030 grants [EV-HOU-237], so the regular bill must pass before the FY2031 grants (`road-funding.md`, 5).

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
- **Who.** Stage 1, then stage 2 if stage 1 is served first (HOU-4.03). Stage 1 is expected to take the whole million, since it has no cap (`6-cost.md`, 2.12). A tribal share goes through tribes (HOU-4.13).
- **Form.** HOU-4.04. All awards are tenant-based in 2030-31; in tight markets from 2032 up to the attached share.
- **Rent.** As current vouchers (HOU-4.01). Payment limits follow HOU-4.05.
- **Renewal.** An award does not lapse for lack of appropriations: its continuing cost is mandatory, outside the yearly voucher renewal vote. Lease-up is measured separately from the award (legacy design).
- **Vehicle.** R2, mandatory.
- **Current law.** New awards under 42 U.S.C. 1437f(o), funded outside the tenant-based rental assistance appropriation [EV-HOU-187]. Precedent: Emergency Housing Vouchers [EV-HOU-188].
- **Evidence.** [EV-HOU-086] [EV-HOU-092] [EV-HOU-187] [EV-HOU-188] [EV-HOU-013].
- **Cost source.** Legacy working midpoint $150 billion over FY2030-39, or $162.2 billion with administration. In the ledger it is component `HOU-1/additional-600000-voucher-awards` ($0.09 trillion, the increment over the older 400,000 inside the housing title), in `models/data/budget/provisions.csv`. Section 6 rescores it.

### HOU-4A.02 Housing agency administration

- **What it does.** An administration allowance for the new awards, covering intake through the common application (HOU-4.02).
- **Amount.** The legacy planning allowance of $12.2 billion over FY2030-39 on the whole million (`legacy/domains/domain-housing.md`, "PR #22 fee correction"). Fees for the new awards are paid at HUD's full, unprorated rate (`DEC-2026-11-10-06`), never prorated as yearly appropriations now allow, and include a one-time issuance fee for each new award (`5-delivery.md`, 2.2) [EV-HOU-343]. Section 6 checks the allowance against that rule.
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
8. **Honest errors are corrected, not punished** (`review-milestone.md`, L-1; HOU-1D.03's rule, point 5). A check after award that finds a household's statement of income, rent or conditions wrong changes its help from the next month. Help ends only for fraud: a knowing false statement, found after notice and a hearing. A household is never asked to repay help it received through an honest mistake or an agency's error; overpayments from agency error are recovered from the agency's administration money, not the household. Deemed approval (item 6) follows the same rule. The same rule covers stage 1's statements (HOU-4.03) and stage 3's (HOU-4.08). *Change to current law:* the voucher rules' repayment of underpaid rent is not yet read for whether it reaches honest mistakes (open check); the regular bill writes this rule for these awards, under `DEC-2026-11-09-13`.

- **Amount.** The $135 billion over FY2030-39 is an estimate, not a cap, because stage 2 is a right from 2037 (memo 2 B).
- **Vehicle.** R2, mandatory. It is enacted in 2029 with 2034 and 2037 effective dates.
- **Current law.** New awards under 1437f(o), like HOU-4A.01.
- **Evidence.** [EV-HOU-185] [EV-HOU-186] [EV-HOU-086] [EV-HOU-090] [EV-HOU-011] [EV-HOU-395] [EV-HOU-346].
- **Cost source.** `housing_extra_tn` = 0.135 in `models/data/inputs/recovery-adoption.json`. Memo 2 arithmetic (not a score): about $114 billion through 2039 at full sign-up, or $123 billion with administration. Section 6's central figure is $81 billion over FY2030-39, plus about $3 billion for the duty to house (`6-cost.md`, 1.2). The wider entry under `DEC-2026-11-09-12` adds about $17 billion over FY2030-39 and $8 billion in FY2040 (`6-cost.md`, 2.7). Restating the count with stage 1 uncapped, about 1.6 million renter families rather than 1.2 million, adds about $17 billion more and $8 billion in FY2040 (`6-cost.md`, 2.12). Section 6 prices 85% of eligible families applying as the central case, with full sign-up as the cautious reading (`DEC-2026-11-10-03`).
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

- **Amount.** A capped yearly amount of about $5 billion from FY2031, set in the statute and indexed to prices (`DEC-2026-11-10-03`; `6-cost.md`, 2.2).
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
- **Building money.** HOU-3C stays at its decided amounts (about $72 billion of grants and $300 billion of loans; `DEC-2026-11-09-03`). So HOU-1A's construction gap money leaves the plan with HOU-1A; it is not added to HOU-3C. Gap financing is an eligible use within HOU-3C's existing amounts. Memo 6 C said the gap money "moves into the construction funds", while memo 3 part 3 B kept those funds' amounts. **Decided (`DEC-2026-11-10-03`): HOU-1A's construction gap money is dropped, not added to HOU-3C.**
- **Rules.** The same as the standing fund (HOU-1D.01 to .03). The network is built once and stays.
- **Amount.** About $15 billion over 2030-31 (`DEC-2026-11-10-03`; `6-cost.md`, 2.2).
- **Vehicle.** R2, mandatory and one-time, so it makes no FY2040 claim (D4).
- **Cost source.** The ledger's housing title component `HOU-1/legacy-housing-title` ($0.47 trillion) still carries HOU-1A's $85 billion. Section 6 replaces it with HOU-1D's standing fund and smaller start.

## 4. Homes: building, buying and repair

### HOU-3C.01 State housing revolving funds

- **What it does.** Capitalization grants to a housing revolving fund in each state (memo 3 part 3 B).
- **Amounts.** About $72 billion, awarded over FY2030-37 so that it is spent by 2039 (`DEC-2026-11-09-09`): $3 billion in 2030, $5 billion in 2031, $10 billion a year in 2032-33 and $11 billion a year in 2034-37. The total and the first two years are as decided (memo 3 part 3 B); the legacy schedule ran $8 billion a year to 2039, and this yearly split is this section's (judgment). States match 20%. Section 5's fund plans and plan-by-silence (`5-delivery.md`, 2.4) carry the faster ramp.
- **Tribal share.** Part of the grants goes through tribes (HOU-4.13).
- **For the poorest renters.** At least 30% goes out as grants or forgivable loans for homes for extremely low-income renters.
- **Eligible uses.** New building, plus buying and preserving existing rental buildings and single-family homes, including tax-credit buildings whose rent limits are ending [EV-HOU-119]. Also permanently affordable homes to buy with a resale limit, from the grants outside the 30% share (HOU-3C.05; `DEC-2026-11-09-19`).
- **Vehicle.** R2, mandatory. It is borrowed inside the D4-B envelope as time-limited capital (ledger C21).
- **Cost source.** Legacy file. The grant channel is about $0.06 trillion of HOU-3C's $0.075 trillion midpoint (range $0.061-0.10 trillion), and it is the part C21 borrows. The rest, about $0.015 trillion, is the loans' subsidy cost (HOU-3C.02). Both sit inside the ledger's housing title component ($0.47 trillion).
- **Agency.** HUD, with state housing finance agencies.
- **Current law.** New. It works beside HOME, with no set amount, and CDBG's new construction use (ROAD to Housing Act sections 501 and 204) [EV-HOU-215] [EV-HOU-226].
- **Vacant-building conversions (decided, `DEC-2026-11-10-01`; `road-funding.md`).** Converting empty commercial buildings is an eligible use, so the ROAD to Housing Act's RESIDE grants (sec. 210, ending FY2031) [EV-HOU-229] get no plan money of their own after FY2029. A FY2029 bridge of about $100 million for RESIDE in FY2029 appropriations counts inside the $72 billion, taken from the last award year.
- **Evidence.** [EV-HOU-118] [EV-HOU-150] [EV-HOU-119] [EV-HOU-024].

### HOU-3C.02 Federal construction and acquisition loans

- **What it does.** A HUD Housing Construction Loan program, funded through the Federal Financing Bank.
- **Amounts.** $300 billion of commitments, made over 2030-38 so the loans are disbursed by about 2039 (`DEC-2026-11-09-09`): $10 billion in 2030, $20 billion in 2031, $30 billion in 2032, then $40 billion a year in 2033-38. The legacy ramp ran about $34 billion a year to 2039; this split is this section's (judgment).
- **Who borrows.** Mixed-income and social housing, with HOU-8 the first borrower; housing agencies' new building; nonprofit and tax-credit projects; and tribes and tribally designated housing entities (HOU-4.13). Acquisition and preservation are eligible, as in HOU-3C.01. Up to $30 billion of the commitments may be construction and construction-to-permanent loans for homes to buy (HOU-3C.05; `DEC-2026-11-09-19`).
- **Terms.** Loans are priced near Treasury rates plus a margin for administration. State agencies originate and service them under a risk-share (the HUD-HFA Risk-Sharing model, sec. 542(c)).
- **Vehicle.** R2, for the credit subsidy. Only the expected loss scores under the Federal Credit Reform Act; it needs CBO's subsidy rate.
- **Cost source.** Legacy file: about $0.015 trillion of subsidy cost (range $0.006-0.03 trillion). HOU-3C as a whole is about $0.075 trillion inside the ledger's housing title.

### HOU-3C.03 Conditions on plan-financed homes

1. **Lasting affordability.** Every rental home that HOU-3C, HOU-8 or HOU-9A builds or buys stays affordable for good, through a recorded use restriction and a nonprofit or public right of first refusal on sale (memo 3 part 3 B). So do the resale-limited homes for sale that HOU-3C.01's grants fund, through their recorded resale limit (HOU-3C.05, item 3). The market-rate starter homes and condos built with HOU-3C.05's construction loans are not covered: their only condition is the first sale at or under FHA's area loan limit to a buyer who will live there (`DEC-2026-11-09-19`, memo 9 part 3 C). The same rule reaches new tax-credit buildings (HOU-2D.04, `DEC-2026-11-09-08`).
2. **Attached help.** In tight markets, HOU-4.04's attached awards go first to homes these funds finance or buy. A project's loan underwriting may count the attached rent (memo 1 B; that pairing is why the loan-heavy construction money works).
3. **Accessible homes for stage 3.** Every building these funds finance meets the federal accessibility minimums for assisted new construction (Section 504 rules; not yet in the register). From 2038, a share of its accessible units is reserved at each turnover for HOU-4.08's households. The share is set with the care flagship, in a law that also requires HUD to publish the count of reserved units by place.
4. **Climate.** New building meets CLI-8's hazard-resistant code baseline (legacy dependency).

- **Vehicle.** R2, as grant and loan conditions.
- **Evidence.** [EV-HOU-119] [EV-HOU-118] [EV-HOU-032].

### HOU-3C.04 Published production targets: three numbers

Espen's direction (`DEC-2026-11-09-10`): publish a target for homes built and preserved. Section 7 found the plan had none (`7-validation.md`, 1.4). Espen then asked for three numbers, each checkable, with the direct count including homes the tax credits finance (`DEC-2026-11-09-14`), and approved the three numbers below (`DEC-2026-11-09-17`). Each state's expected count of number 1 is its money divided by its own cost per home (`DEC-2026-11-10-03`; "For all three", below).

**1. Homes the plan pays for: about 1.3 million built or preserved over 2030-39 (range 0.8-1.9 million), at least 120,000 of them for extremely low-income renters (range 100,000-160,000).** It counts only homes the plan's added money pays for. The credit's current-law production, about 95,000 homes a year since 1987 [EV-HOU-443], is the baseline and is not counted. Each home counts once, whatever mix of money it uses.

| Source | Homes, 2030-39 (central, range) | Basis |
| --- | --- | --- |
| Construction money: HOU-3C grants and loans, HOU-8, HOU-9A | 900,000 (600,000-1,300,000) | *Grants:* about $86 billion with the state match, at $150,000-300,000 of gap subsidy a home, finances about 290,000-580,000 homes (`7-validation.md`, 1.4) [EV-HOU-412] [EV-HOU-411]. *Loans:* $300 billion of commitments at $250,000-350,000 of loan a home would finance 0.9-1.2 million homes if every loan went to a separate home (`7-validation.md`, 1.4). Many loans pair with the grants or credits, so this section counts only loan-only homes, mostly mixed-income, social housing and acquisitions in tight markets: about half the loan money (a third to 60%), so about 500,000 (300,000-700,000; judgment). Loan-only homes must earn rents that repay the loan, so few are deeply affordable, and demand for the loans is untested at this scale |
| Bigger low-income credit with the deep-income boost (HOU-2D.01) | 300,000 (200,000-330,000) | Novogradac's estimates for the parts of the bill HOU-2D.01 carries [EV-HOU-444]: 104,000 from the extremely low-income boost and 167,000 from the 9% allocation increase, counted in full because the firm's baseline already assumes the 12.5% increase, which the 2025 law's permanent 12% roughly matches [EV-HOU-260]. Of the 175,000 from 30% basis boosts, only the rural and tribal boosts are in HOU-2D.01: the tribal one decided (`DEC-2026-11-09-16`, HOU-4.13), the rural one left out (`DEC-2026-11-10-03`); the bond-financed boost (AHCIA section 308), likely the largest, is in only for buildings using the poorest-renter boost (`DEC-2026-11-09-18`), about 3,000-18,000 homes financed (memo 3b), within this row's range. This section counts about 30,000-40,000 for them (judgment, at most a third of the 175,000; the rural boost's share is out, which stays inside the row's range). The firm has a stake and assumes gap money scales; the plan's construction grants are that gap money. The low end discounts that assumption (judgment) |
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
- *What the targets do.* Each state's expected count of number 1 is its share of the grants, loans and credits divided by its own cost per home, from the cost reports state agencies already file for tax-credit buildings; a state "misses" when it finishes well under that count two years running (`DEC-2026-11-10-03`; the milestone review's option b). This is fair across high- and low-cost states and adds no paperwork. HOU-9A.01's builder may build only where state channels have missed their count. Missing a target is a published warning (section 7, 6), not a reason to withhold money (judgment, under `DEC-2026-11-09-13`).

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
- **Size target and evaluation date** (`DEC-2026-11-10-03`; the numbers `DEC-2026-11-10-04`). About 60,000 homes (40,000-100,000) financed by public or nonprofit owners, at least ten owners in at least five states, awarded over 2030-35. An independent evaluation, contracted in 2030, reports in 2034 (start-up, costs, who lives there) and in 2037 (rents, operating results, whether the funds revolve), so a scale-up decision can be made with the 2040s route (HOU-4.03). The size follows from the $10 billion of equity at about $100,000-250,000 a home in mixed-income buildings, with the loans carrying the rest (judgment; `6-cost.md`, 2.12). The nearest U.S. case, Montgomery County's revolving fund, is a projection and uncorroborated [EV-HOU-141]. Missing the target is a published finding, not a reason to cut the money (`DEC-2026-11-09-13`).
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
- the 2033 end date goes;
- places and states also earn credit for six further reforms (memo 10 part 1 B, `DEC-2026-11-09-20`): single-stair apartment buildings up to six stories [EV-HOU-580]; manufactured homes treated like other homes wherever houses are allowed, including titling as real property on land the owner holds (HOU-11.01) [EV-HOU-578]; small lots [EV-HOU-596]; no parking minimums [EV-HOU-592]; a state exemption of zoning-consistent infill from state environmental review [EV-HOU-590]; and condo defect-liability reform on Colorado's warranty-for-narrower-claims model [EV-HOU-598]. No new money and no new rule: the award still follows homes finished. Because HOU-6.02 uses the Innovation Fund's list, the same reforms count toward the transportation condition.

- **Build Now.** Its CDBG reallocation stays as the only test on community development grants [EV-HOU-208]. HUD studies whether it penalizes steady builders below 4% growth [EV-HOU-244] and reports by 2032, with a proposed fix if it does.
- **Vehicle (split).** The money is a direct appropriation in R2, mandatory. The changes to who may apply and what is paid for go in a regular bill. The R2 money is written so it can be spent under the Act's current rules until the regular bill passes (judgment; memo 4).
- **Funding before R2 and counting it once (decided, `DEC-2026-11-10-01`; `road-funding.md`).** The $30 billion is the fund's total for FY2029-39, counting any yearly appropriation that continues beside it. Up to about $1 billion of it may pay for the Act's planning grants (sec. 207), pattern books (sec. 209) and single-stair grants (sec. 102), which the regular bill folds into the fund. The plan seeks the authorized $200 million a year in FY2027 and FY2028 appropriations and a FY2029 bridge of about $270 million (the fund, the planning grants and the small grants) in FY2029 appropriations, counted inside the $30 billion and taken from its last year (`6-cost.md`, 2.10). Nothing is funded in FY2027 so far [EV-HOU-751] [EV-HOU-754].
- **Evidence.** [EV-HOU-123] [EV-HOU-124] [EV-HOU-177] [EV-HOU-206] [EV-HOU-208].
- **After 2039** (`DEC-2026-11-10-03`). The reward ends with its FY2030-39 money unless Congress renews it on its results: the 2037 report on homes finished in rewarded places against similar places (HOU-3C.04, number 2) is the basis. Continuing it at the same scale would cost about $3 billion a year (`6-cost.md`, question 6).
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
- **Tribal and rural areas.** The bill's treatment of tribal areas as high-cost areas with a basis boost, which the 2025 law dropped, is kept (`DEC-2026-11-09-16`; HOU-4.13) [EV-HOU-263]. **Rural areas: left out** (`DEC-2026-11-10-03`). States can already give the 30% boost to any building they designate except bond-financed ones [EV-HOU-461], and most rural credit buildings are not bond-financed. Instead, each state agency publishes how often it uses its designation power in rural places, and the 2034 credit review revisits a rural boost if rural deals still do not get built.
- **The 30% boost for bond-financed buildings that use the poorest-renter boost** (`DEC-2026-11-09-18`; memo 3b, option (b)). AHCIA section 308 lets a housing credit agency give the 30% basis boost to bond-financed buildings it designates, which current law forbids outside designated qualified census tracts and difficult development areas [EV-HOU-461] [EV-HOU-462]. HOU-2D.01 enacts it only for bond-financed buildings that use the poorest-renter boost above; there it reaches the building's other homes, since the set-aside homes already have the 150% boost [EV-HOU-263]. Designated tracts and areas already get the boost under current law [EV-HOU-460]. The agency's existing designation is the only test, so no new paperwork (design lens, `DEC-2026-11-09-13`). Published yearly counts of boosted bond projects by area; reviewed in 2034 with the credit trials, and widened toward the bill's full section 308 only if deep-income bond buildings still don't pencil.
- **Attached help.** In tight markets, new credit homes are eligible for HOU-4.04's attached awards, which reach extremely low-income tenants [EV-HOU-118].
- **Evidence.** Nationally about eight in ten credit homes replace homes that would have been built anyway, but much less in dense places [EV-HOU-275] [EV-HOU-277] [EV-HOU-115].
- **Cost source.** Section 6: about $0.10 trillion over FY2030-39 (range $0.08-0.12 trillion; legacy estimate HOU-2B), permanent, plus about $1 billion ($0.4-1.6 billion) for the bond-deal boost (memo 3b).

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

## 7. Homeownership and broad supply (memos 9 and 10)

Espen decided memos 9 and 10 on November 9, 2026 (`DEC-2026-11-09-19`, `-20`), from the section 3 addendum (`3-design.md`; research in `research-ownership-supply.md`). Memo 9 part 1 came with two changes: a higher income limit, in the 135-150% range, and a plain rule that states may stack the federal help with their own. The design lens applies throughout: one plain test, the buyer's own statement, records the lender already holds, and published counts with review triggers.

### HOU-10.01 Down payment help for first-time buyers, 2030-39

**Parameters** (memo 9 part 1 C, as changed by Espen).
1. **Who.** First-time buyers who will live in the home. First-time means not having owned a home in the past three years, by the buyer's signed statement (the usual federal three-year test; judgment).
2. **Income limit: 140% of area median income, and 160% in high-cost areas (decided by Espen, `DEC-2026-11-09-24`).** Espen asked for a limit in the 135-150% range; the 160% high-cost limit sits above it, and Espen accepted it as recommended. 140% is the limit the plan's neighborhood homes credit already uses for its buyers [EV-HOU-269], so the plan's two buyer programs share one number (design lens); it sits inside the 150% where the 2025 buyer-credit bill starts phasing out [EV-HOU-524]. The high-cost limit keeps the bill's 20-point step above the standard limit [EV-HOU-525] and matches the cap in the 2021 credit bill [EV-HOU-523]. A high-cost area is one where FHA's loan limit is above its national floor, a list HUD already publishes, so no new test is needed (judgment). Income is the figure in the mortgage file the lender already underwrites.
3. **First-generation priority.** Where requests exceed a state's money, first-generation buyers come first: those whose parents did not own a home, or who were in foster care, by the buyer's signed statement, with no further papers, and lenders who rely on it in good faith are protected [EV-HOU-526]. Within each group, the state's own queue order (first come, or a lottery, as California used [EV-HOU-542]).
4. **Amount, capped** (`DEC-2026-11-10-03`). The greater of $20,000 or 10% of the price [EV-HOU-525], up to **$25,000**, or up to **$30,000 for a newly built home**, so the money pulls building rather than bidding up existing homes. **The home's price may not exceed FHA's loan limit for the area**, the limit HUD already publishes and HOU-3C.05 already uses, so no new test is needed. A flat cap reaches more buyers with the same money and puts less of it into the costliest markets [EV-HOU-545] [EV-HOU-546] (`review-milestone.md`, O-4 and A-2). The earlier draft let a state add 25% for new homes and homes in zoning-reward places, with no cap and no price limit; the cap replaces it. Espen's answer names only newly built homes for the higher cap, so the extra help for existing homes in zoning-reward places is dropped (the reward itself still pays those places for homes finished, HOU-6.01). At an average of about $24,000-26,000, the money reaches about 1.1-1.2 million buyers (`6-cost.md`, 2.12).
5. **Form, by each state.** A grant; a zero-interest second mortgage forgiven over five years; or a zero-interest deferred loan repaid at sale or refinance, including a shared-appreciation loan [EV-HOU-540]. Repaid money stays in the state's program.
6. **Stacking, written plainly into the law.** States may combine this help with any other down payment or closing-cost help: state, city, county, tribal, employer, nonprofit or family, and with a second mortgage from any of them, as state agencies already do [EV-HOU-535].
   - The federal help is never reduced because a buyer has other help.
   - No separate federal limit or form on the total; the normal financing process settles how the pieces fit (`DEC-2026-11-09-23`; Espen, November 9, 2026: "don't let that be an extra limit constraining process here via another set of paperwork"). Espen expects that where more help is available than a buyer needs at closing, it will usually show up as a larger second mortgage from the state or local agency; that is a prediction about practice, not a rule.
   - Combined loan amounts follow the first mortgage's own rules (for example, up to 105% combined loan-to-value for agency second loans under Freddie Mac's rules [EV-HOU-535]); the federal program adds no limit of its own.
   - No federal approval of the other programs is needed. The closing statement records each source.
7. **Counseling, offered, not required by federal rule (decided by Espen, `DEC-2026-11-09-24`, point 5).** Each state offers every buyer free homebuyer counseling, which state agencies already provide and which is part of the package tied to lower default [EV-HOU-537]. Federal law does not make it a condition of the help: a required course adds a step and a wait before closing, and the evidence ties lower default to the agency's whole package (counseling with sound loans and its own servicing), not to counseling alone. States that already require it may keep doing so. Where counseling is simply part of an agency's or lender's normal loan process, it stays as it is and is not an added requirement (Espen: "yes unless 'counseling' just means a part of the normal loan process, which might be the case").
8. **Money.** $3 billion a year to states by formula through their housing finance agencies, FY2031-39, with $1.5 billion in FY2030 while programs start (about $28.5 billion; judgment). Each year's money stays available until spent. A tribal share goes through tribes (HOU-4.13's set-aside rule).
9. **Review, not a cap.** HUD publishes each year who was helped (income, age, race, first-generation status, new or existing home) and the price trend in the places using the most help. A price rise in those places well above their region's for two years triggers a review of the amounts there (section 8). Missing a group's projected share is a published finding, not a reason to withhold money (`DEC-2026-11-09-13`).
10. **Rural buyers (memo 13 part 2 C, `DEC-2026-11-10-02`).** This help stacks with USDA's Section 502 direct and guaranteed loans under item 6, and HOU-14.02 gives the guaranteed loans this provision's income limits, so a rural buyer who qualifies for one qualifies for both. State agencies and USDA offices refer buyers to each other.

- **Agency.** HUD, through state housing finance agencies; tribes for the tribal share.
- **Vehicle.** R2, mandatory, time-limited (FY2030-39). As a time-limited program it can borrow inside the D4-B envelope (section 6, 2.8).
- **Current law.** New. HOME's homebuyer help (up to 100% of area median income under the ROAD to Housing Act [EV-HOU-226]) and state programs continue and stack with it.
- **Evidence.** [EV-HOU-525] [EV-HOU-526] [EV-HOU-535] [EV-HOU-536] [EV-HOU-537] [EV-HOU-539] [EV-HOU-540] [EV-HOU-541] [EV-HOU-544] [EV-HOU-545] [EV-HOU-546] [EV-HOU-547].
- **Cost source.** Section 6, 2.8 and 2.12: about $28 billion of outlays over FY2030-39.

### HOU-10.02 FHA's annual premium on purchase loans cut to 0.30%

**Parameters** (memo 9 part 2 B).
1. **The cut.** FHA's annual mortgage insurance premium on new purchase loans falls from 0.55% [EV-HOU-551] to 0.30% from January 2030. Refinances keep HUD's rate. HUD may set it lower but not higher while the safety line holds.
2. **The safety line: FHA's insurance fund keeps a capital ratio of at least 3% in its annual actuarial review (decided by Espen, `DEC-2026-11-09-24`).** That is one point above the 2% legal minimum; the ratio was 11.47% in fiscal 2025, and 4.42% under a severe stress test [EV-HOU-552]. If the ratio falls below 3%, HUD may raise the premium back toward 0.55%, by published review, only as far as needed to restore the line.
3. **No buyer test.** The premium follows the loan; there is nothing to apply for.
4. **Through 2039, with a review** (`DEC-2026-11-10-03`). The 0.30% premium applies to loans endorsed from January 2030 through September 30, 2039 (FY2039), for the life of each loan. HUD reviews the cut in its FY2038 actuarial report: how many added first-time buyers it brought, its effect on the fund's capital ratio, and prices in the places with the most FHA lending. Congress may renew it on that review; otherwise loans endorsed from FY2040 pay HUD's ordinary rate.

- **Agency.** HUD (FHA).
- **Vehicle.** In law, so a later administration cannot raise it while the line holds. It changes the subsidy cost of FHA's loans under the Federal Credit Reform Act; whether that scores as direct spending in R2 or against appropriations is CBO's call (needs CBO). If R2 cannot carry it, the regular bill does.
- **Current law.** The premium is set by HUD within statutory maximums; 0.55% since 2023 [EV-HOU-551].
- **Evidence.** [EV-HOU-550] [EV-HOU-551] [EV-HOU-552].
- **Cost source.** Section 6, 2.8 and 2.12: about $25 billion over FY2030-39 on a credit-reform basis; nothing from FY2040 unless renewed, when it would cost about $3 billion a year.

### HOU-3C.05 Homes to buy: starter homes, condos and resale-limited homes

**Parameters** (memo 9 part 3 C).
1. **Loans.** Up to $30 billion of HOU-3C.02's $300 billion of commitments may be construction loans, and construction-to-permanent loans that become the buyer's mortgage, for homes sold to people who will live in them. Small, nonprofit and other builders borrow through state agencies and community development lenders. No new money: the rental share shrinks by what is used.
2. **Price.** Each home sells at or under FHA's loan limit for its area, the limit HUD already publishes. The builder certifies the sale price and the buyer's statement that they will live there; there is no buyer income test. This first-sale price limit is the only condition on these market-rate homes; HOU-3C.03's permanent affordability does not apply to them (resale-limited homes under item 3 are the exception).
3. **Resale-limited homes.** The revolving-fund grants (HOU-3C.01), outside the 30% share reserved for extremely low-income renters, may fund homes sold below market with a recorded resale limit, through land trusts and similar owners, so the discount stays with the home for later buyers [EV-HOU-548]. A price check at each resale; owners keep a share of the gain set by the state.
4. **Pairing.** HOU-10.01's larger amount for newly built homes applies to these homes.
5. **Count.** HOU-3C.04's first number is unchanged; homes for sale are reported as their own line, by type (market-rate starter home, condo, resale-limited).

- **Agency.** HUD, with state housing finance agencies and community development lenders.
- **Vehicle.** R2, inside HOU-3C's amounts.
- **Evidence.** [EV-HOU-567] [EV-HOU-568] [EV-HOU-569] [EV-HOU-548] [EV-HOU-597]. The register has no evaluation of federal construction lending to small builders.
- **Cost source.** Section 6, 2.8: no added cost; short construction loans may carry a lower subsidy rate than the rental loans (needs CBO).

### HOU-11.01 Cheaper loans for manufactured homes

**Parameters** (memo 10 part 2 B).
1. **Chattel loans bought by Fannie Mae and Freddie Mac.** The two companies buy loans secured by the home but not the land, under their existing duty to serve the manufactured housing market, with consumer protections like those on mortgages (ability to repay, limits on fees, foreclosure-style notice before repossession). FHFA acts in 2029; the regular bill writes the purchases into the duty-to-serve goals. Today 42% of manufactured-home purchase loans are chattel loans, at a median 8.6% against 4.9% for manufactured-home mortgages [EV-HOU-576].
2. **Titling as real property.** A manufactured home on land the owner holds can be titled as real property, so it qualifies for a mortgage; 17% of such owners still take chattel loans [EV-HOU-576]. States that allow it earn credit in the zoning reward (HOU-6.01).
3. **Resident purchases of communities.** Fund the ROAD to Housing Act's grants for manufactured-home communities (PRICE), authorized but unfunded [EV-HOU-220], at $350 million a year for FY2030-38 and $150 million in FY2039, after a $200 million FY2029 bridge in appropriations, $3.5 billion in all (decided by Espen, `DEC-2026-11-09-24`, amended by `DEC-2026-11-10-01`), with priority to resident and nonprofit purchases; the regular bill extends the program past its 2033 end.

- **Agency.** FHFA (the companies); HUD (PRICE).
- **Vehicle.** FHFA action; regular bill; R2 for the grants. Before R2 (decided, `DEC-2026-11-10-01`; `road-funding.md`): PRICE at $100 million in FY2027 and FY2028 appropriations and $200 million in FY2029, the FY2029 amount counted inside the $3.5 billion.
- **Evidence.** [EV-HOU-575] [EV-HOU-576] [EV-HOU-577] [EV-HOU-578] [EV-HOU-219] [EV-HOU-220]. No study shows how far chattel rates would fall.
- **Cost source.** Section 6, 2.8: about $3.5 billion over FY2030-39 for the grants; the companies' new credit risk is unpriced (CBO counts their guarantees as governmental [EV-HOU-556]).

### HOU-11.02 Federal land for housing near growing western cities

**Parameters** (memo 10 part 3 B).
1. **Sales.** The Bureau of Land Management sells land within a set distance of cities with housing shortages to local governments with a housing plan for it, at appraised fair market value, on the Southern Nevada model [EV-HOU-585]. The list of eligible land comes from the Interior-HUD task force's work [EV-HOU-582].
2. **Proceeds (decided by Espen, `DEC-2026-11-09-24`).** Up to half pays for water, sewer and roads serving the new homes; the rest goes to the Treasury. The Southern Nevada law sends most proceeds to projects in the state [EV-HOU-585].
3. **Affordability.** None required on the land itself; the plan's construction money and the zoning reward can add it there.
4. **Surplus buildings.** Homeless providers keep their first claim on surplus federal property under McKinney-Vento Title V [EV-HOU-586].
5. **Limits.** Environmental review and tribal consultation for the sales stay as under current law; the infill exclusion (HOU-11.03) does not apply to greenfield sites.

- **Agency.** Interior (BLM), with HUD.
- **Vehicle.** Regular bill.
- **Evidence.** [EV-HOU-582] [EV-HOU-583] [EV-HOU-584] [EV-HOU-585] [EV-HOU-586]. How many homes is contested: about 0.1 to 1 million over a decade [EV-HOU-583] [EV-HOU-584]. HOU-3C.04's targets do not count on them.
- **Cost source.** Section 6, 2.8: receipts, not counted in the totals.

### HOU-11.03 Assisted infill housing excluded from federal environmental review

**Parameters** (memo 10 part 4 B).
1. **The exclusion.** Housing that receives federal money from any agency, the plan's included, on an infill site is categorically excluded from review under the National Environmental Policy Act. An infill site is one with existing infrastructure beyond a road, not a greenfield, and outside high-risk flood and wildfire tracts, the definition the ROAD to Housing Act already uses for USDA [EV-HOU-217].
2. **Deemed complete.** A review that still applies (a non-infill site, or an extraordinary circumstance) is deemed complete 90 days after a complete application unless the agency has finished it.
3. **The project's test.** The developer certifies the site meets the infill definition; false certification is grounds to recover the money.
4. **States.** Part 1 of memo 10 rewards states that exempt infill from their own review (HOU-6.01).

- **Agency.** Each funding agency; CEQ guidance.
- **Vehicle.** Regular bill. It builds on the ROAD to Housing Act's HUD rulemaking [EV-HOU-218] rather than waiting for it.
- **Evidence.** [EV-HOU-217] [EV-HOU-218] [EV-HOU-589] [EV-HOU-591]. The only federal cost figure is dated [EV-HOU-589]; the time saved is judgment.
- **Cost source.** None.

### How these fit the rest of section 4

- **HOU-3C.04.** Number 1 is unchanged; homes for sale under HOU-3C.05 are reported as their own line. Federal-land homes and HOU-10.01's buyers are not counted toward the targets.
- **HOU-2D.03.** Neighborhood homes credit buyers may also use HOU-10.01, under its stacking rule.
- **HOU-4.01.** Buyer programs use the mortgage file's income, not the rental help's income rules, so a renter household moving to ownership has no second income check.
- **D3.** HOU-10.01's higher limit and HOU-10.02 are the plan's main new reach into the middle income groups; the incidence model checks them (section 7).

## 8. Repair and aging in place (memos 11 and 12)

Espen decided memos 11 and 12 on November 9, 2026 (`DEC-2026-11-09-21`, `-22`), from the section 3 addendum, part 2 (`3-design.md`; research in `research-repair-aging.md`). Every part went as recommended. Espen kept two further options open for other dossiers: merging repair and Weatherization (memo 11 part 3 C), if the clean-power dossier finds it workable or preferable, and CAPABLE as a Medicare benefit (memo 12 part 2 C), for the care dossier to review. Section 202 construction (memo 12 part 4 B) is added if the GAO study shows it merits it (Espen: "C, and B if ROAD study shows it merits it"). The amounts the decisions left open were proposed here and decided by Espen as proposed (`DEC-2026-11-09-25`; `6-cost.md`, question 10). The design lens applies throughout: one plain income test by the person's own statement or a benefit record the government already holds, no credit or tax-current test, local judgment on need, and published counts with review triggers instead of caps or quotas.

### HOU-12.01 The home repair fund, 2030-39

**Parameters** (memo 11 part 1 C).
1. **Who.** Owner-occupants at or below 80% of area median income get grants; owners from 80% to 120% get zero-interest loans repaid only at sale, refinance with cash out, or when no owner lives in the home any longer. Heirs and others with an interest in the home who live in it count as owners, as the ROAD to Housing Act's pilot already allows [EV-HOU-676]. Owners of manufactured homes count, whether the home is titled as real or personal property.
2. **The one plain test.** Income by the owner's signed statement, or automatic eligibility for anyone already enrolled in SNAP, Medicaid, SSI, LIHEAP or Weatherization. No credit score, and no test of being current on property taxes, water bills or a mortgage: owners who are behind are referred to HOU-13.01 and HOU-13.02, not turned away (Philadelphia's program, by contrast, requires owners to be current [EV-HOU-648]).
3. **What it pays for.** Health, safety and basic systems first: roofs, heat and cooling, wiring and electric panels, plumbing, lead hazards, mold and asthma triggers, accessibility (HOU-12.04), and the repairs that let a home take weatherization or a heat pump (HOU-12.03). The work fixes what is wrong; it does not bring the whole house to code, the rule that makes each HOME repair cost about $57,724 [EV-HOU-609] [EV-HOU-610]. Lead work follows the lead-safe rules [EV-HOU-613].
4. **Amount per home: decided (`DEC-2026-11-09-25`).** Grants and loans up to $25,000 a home, plus up to $15,000 more where lead hazard control or accessibility work is added. Basis: Philadelphia's repairs averaged about $8,909 [EV-HOU-647] and Detroit's grants $16,498 [EV-HOU-660]; Pennsylvania's $50,000 cap produced costly repairs and long waits [EV-HOU-658] (judgment).
5. **Accessory units.** The zero-interest loans may also pay toward an accessory unit an older owner builds for a caregiver or a tenant, up to the same cap (memo 12, smaller point 1; `DEC-2026-11-09-22`). FHA's Title I loans can finance the rest [EV-HOU-220].
6. **Who runs it.** Money by formula to the states, cities and urban counties that already receive CDBG and HOME, using their existing grantee network, with the tribal share below. Each grantee chooses its contractors and its order of need. Small grantees may pool through their state.
7. **Tribal share: decided (`DEC-2026-11-09-25`).** 5% through tribes, by the Native American Housing Block Grant formula and each tribe's housing plan, on HOU-4.13's model. Basis: the construction grants' 5% share [EV-HOU-406] (judgment).
8. **Wage rule.** Repairs to owner-occupied homes of one to seven units do not trigger federal prevailing-wage rules, the line CDBG already draws for small residential buildings (judgment; Pennsylvania's counties capped grants below their state's wage trigger [EV-HOU-657]).
9. **Money: decided (`DEC-2026-11-09-25`, amended by `DEC-2026-11-10-01`).** A $300 million FY2029 bridge through the ROAD to Housing Act's repair pilot, then $2 billion in FY2030 while grantees start, $4 billion a year in FY2031-38 and $3.7 billion in FY2039, about $38 billion in all, available until spent. HOU-12.02 to .04 are paid from the same money; there are no set-asides inside it.
10. **Review, not a cap.** HUD publishes each year homes repaired, waits, cost per home, and the share of grants to owners under 30% and 50% of area median income, to older owners and to renters (HOU-12.02), by place. A grantee whose waits run past a year, or whose poorest owners get a falling share, gets a published review, not a funding cut (`DEC-2026-11-09-13`).
11. **The rural door (memo 13 part 3 B, `DEC-2026-11-10-02`).** In USDA-eligible rural areas (HOU-14.05), an owner may apply at a USDA Rural Development office or a Section 533 grantee [EV-HOU-768], or at the state or local grantee. Either door gives the same help on this fund's terms: items 1 to 5, with no age test, no assets test, no credit test and no repayment on sale within three years, the Section 504 rules this fund does not use [EV-HOU-761]. About a sixth of the fund, about $6 billion over FY2030-39, goes to USDA by interagency transfer, out of the states' rural shares; a state may pass more of its rural share to USDA. The sixth is judgment until USDA and HUD count low-income owners in eligible areas; section 6 resets it from that count without changing the fund's total. USDA reports on item 10's terms, by state. HOU-12.04's older-adult track runs through both doors. No new money.

- **Agency.** HUD (Office of Community Planning and Development), with CDBG and HOME grantees; HUD's Office of Native American Programs and tribes for the tribal share. USDA Rural Development runs the rural door (item 11) through its offices funded under HOU-14.01; Section 504 continues alongside it, opened to owners of any age by rule (HOU-14.06) [EV-HOU-615].
- **Vehicle.** R2, mandatory, time-limited (FY2030-39). As time-limited capital it can borrow inside the D4-B envelope, like HOU-3C.01 and HOU-5.01 (section 6, 2.9). The wage rule and the eligibility of heirs go in the regular bill if reconciliation cannot carry them.
- **Current law.** The ROAD to Housing Act's whole-home repair pilot (sec. 202) runs only if appropriated and ends October 1, 2031 [EV-HOU-230]; this fund replaces it. HOME, CDBG and Section 504 continue [EV-HOU-611] [EV-HOU-616].
- **Funding before R2 (decided, `DEC-2026-11-10-01`; `road-funding.md`).** The pilot is funded in appropriations at about $100 million in FY2027, $150 million in FY2028 and $300 million in FY2029, so grantees are staffed before FY2030. The FY2029 amount counts inside this fund's $38 billion; the FY2027-28 amounts are spent before it and are not part of it. If R2 slips past FY2030, FY2030 appropriations carry the pilot one more year. HOME and CDBG, whose grantees run this fund, are held at FY2026 levels against the House's FY2027 HOME cut [EV-HOU-753].
- **Evidence.** [EV-HOU-601] [EV-HOU-602] [EV-HOU-603] [EV-HOU-606] [EV-HOU-609] [EV-HOU-610] [EV-HOU-645] [EV-HOU-646] [EV-HOU-647] [EV-HOU-649] [EV-HOU-656] [EV-HOU-660] [EV-HOU-661].
- **Cost source.** Section 6, 2.9: $38 billion of budget authority, about $37 billion of outlays over FY2030-39 and a $1.2 billion tail in FY2040.

### HOU-12.02 Repairs for renters, without rent jumps

**Parameters** (memo 11 part 2 B).
1. **Landlord loans.** HOU-12.01's grantees may lend to owners of up to 20 rental units (decided, `DEC-2026-11-09-25`), up to $25,000 a unit (decided, `DEC-2026-11-09-25`), for the same kinds of repair. A loan is forgiven after three years if annual rent increases on the repaired units stay at or below 5% or inflation, whichever is lower, the ROAD to Housing Act pilot's own term [EV-HOU-230]; otherwise it is repaid at the grantee's rate. Units rented to voucher holders are exempt from the rent term, since their rent is set by the voucher's own rules (judgment). The landlord signs a statement; there is no tenant income check and no ownership-period requirement, the rules that kept Pennsylvania's landlord loans nearly unused [EV-HOU-655] [EV-HOU-656] [EV-HOU-657].
2. **No pass-through.** The cost of work paid for with this money may never be passed on in rent, in any program, as New York now requires for building upgrades [EV-HOU-665] and the federal energy rebates require for two years [EV-HOU-632].
3. **City repair funds.** Grantees may pay to repair hazards a landlord fails to fix after notice, and bill the owner, recovering through a lien, as New York City does [EV-HOU-663].
4. **Receivership.** Grantees may lend to court-appointed receivers of neglected rental buildings, as a revolving fund [EV-HOU-669].
5. **Relocation help.** Where a local government orders tenants out of an unsafe home, the fund pays moving costs and up to three months' rent at the new home (decided, `DEC-2026-11-09-25`), so enforcement does not become eviction [EV-HOU-667].
6. **No federal inspection mandate.** Proactive inspection stays a local choice [EV-HOU-666].

- **Agency, vehicle, money.** As HOU-12.01, from its money.
- **Evidence.** [EV-HOU-651] [EV-HOU-652] [EV-HOU-655] [EV-HOU-656] [EV-HOU-657] [EV-HOU-663] [EV-HOU-664] [EV-HOU-665] [EV-HOU-667] [EV-HOU-668] [EV-HOU-669] [EV-HOU-230] [EV-HOU-632].
- **Cost source.** Section 6, 2.9: inside HOU-12.01, about $0.5-1 billion a year (judgment).

### HOU-12.03 One front door with the clean-power programs

**Parameters** (memo 11 part 3 B).
1. **One application, one assessment.** A household applies once, to the local program the state names, and gets one home assessment for repairs, lead, accessibility and energy. Anyone eligible for HOU-12.01, Weatherization, LIHEAP or the clean-power retrofits is eligible for all of them on the same statement or benefit record.
2. **Readiness repairs.** HOU-12.01 pays for the repairs that let a home take weatherization or a heat pump: roofs, floors, wiring and panels, mold. Weatherization and the clean-power retrofits pay for the energy work. About one in five low-income homes is now deferred for such repairs, and 40% of those are never served [EV-HOU-639] [EV-HOU-623].
3. **Either agency.** Where a state runs Weatherization and housing repair through different agencies, the money may flow to whichever the state names.
4. **Left to clean power.** Whether to merge repair and Weatherization into one program (memo 11 part 3 C) is the clean-power dossier's call; Espen is open to it if that dossier finds it workable or preferable (`DEC-2026-11-09-21`). So are the home energy credits (CLI-1A), LIHEAP and Weatherization's size (CLI-5) and the low-income heat-pump retrofits (CLI-5W).

- **Agency.** HUD and DOE jointly issue the common assessment and eligibility rule; HHS for LIHEAP.
- **Vehicle.** Regular bill for the shared eligibility and the joint rule; R2 money through HOU-12.01.
- **Evidence.** [EV-HOU-622] [EV-HOU-623] [EV-HOU-639] [EV-HOU-640] [EV-HOU-636] [EV-HOU-638].
- **Cost source.** Section 6, 2.9: inside HOU-12.01, about $0.25-0.75 billion a year once CLI-5W runs (judgment).

### HOU-12.04 Older adults: repairs and home changes on the CAPABLE model

**Parameters** (memo 12 part 2 B).
1. **Who.** Owners and renters 65 or over, or with a disability, at or below 80% of area median income, on HOU-12.01's plain test.
2. **What.** A home assessment by an occupational therapist, and the changes it finds: grab bars, rails, ramps, a first-floor bathroom, lighting, plus HOU-12.01's system repairs. For people with daily-living limits, the CAPABLE package: nurse and occupational-therapist visits with a handyman's work [EV-HOU-686].
3. **Renters.** With the landlord's written consent; the landlord may not raise rent for the work (HOU-12.02, point 2).
4. **The care line.** The fund pays for the home. Whether Medicare or Medicaid pays for CAPABLE's nurse and therapist visits, and how Medicaid home care grows, is the care dossier's decision (HLT-4; memo 12 part 2 C noted for it, `DEC-2026-11-09-22`). Until it decides, the fund may pay for the visits in the CAPABLE package. Grantees refer people to Medicaid home care where they qualify [EV-HOU-691].
5. **Measured from the start.** Grantees report falls, emergency visits and moves to nursing homes among people served, by consent, so the lasting effect, which faded by 12 months in the trial [EV-HOU-688], can be checked.

- **Agency, vehicle, money.** As HOU-12.01, from its money; HUD's Older Adults Home Modification grants [EV-HOU-689] continue or fold into it at HUD's choice.
- **Evidence.** [EV-HOU-686] [EV-HOU-687] [EV-HOU-688] [EV-HOU-689] [EV-HOU-673] [EV-HOU-690] [EV-HOU-608].
- **Cost source.** Section 6, 2.9: inside HOU-12.01, about $0.3-1.6 billion a year (judgment).

### HOU-13.01 A federal match for state property-tax relief for older owners

**Parameters** (memo 12 part 1 B).
1. **The match.** From FY2031, the federal government pays half of what a state spends on property-tax relief for owners 65 or over, and owners with disabilities, with incomes up to 80% of area median income, on relief that meets the three standards below.
2. **Standard 1, relief by income.** Tax above a share of income the state sets is credited back, as a circuit breaker does. The federal match counts relief only above 3% of income (decided, `DEC-2026-11-09-25`), so states set their own threshold at or above it [EV-HOU-682]. That is below the 4-6% memo 12 gave as an example: a lower floor lets states that already start relief lower draw the match, and costs more; a 5% floor would cost roughly a third less (judgment). Espen kept 3% ("keep 3%"; `DEC-2026-11-09-25`).
3. **Standard 2, deferral for the rest.** Any older owner may defer the rest of the bill as a lien repaid at sale or death, at a rate no higher than the state's borrowing cost, with no yearly reapplication.
4. **Standard 3, records first.** States enroll owners from the state tax and benefit records they already hold where they can; owners who do not file sign a one-page statement. Yearly requalification is not allowed: California's deferral program with yearly requalification reached about 1,000 of over a million eligible [EV-HOU-683].
5. **Renters.** States may extend the match to renters 65 or over, crediting the share of rent that stands for property tax.
6. **Maintenance of effort.** The match pays only on relief above each state's 2028 spending on the same groups, so it adds relief rather than replacing state money (decided, `DEC-2026-11-09-25`).
7. **Before any tax sale** of the home of an owner 65 or over, a state taking the match first offers a payment plan or deferral (HOU-13.02).
8. **Review.** Treasury and HUD publish each year enrollment, average relief and moves among older owners in matched states.

- **Agency.** Treasury, paying states; HUD for the reporting.
- **Vehicle.** R2, mandatory, permanent: a capped entitlement to states at the match rate. The standards ride as conditions on the money; any reconciliation strikes go to the regular bill.
- **Current law.** None federal. 29 states and DC have circuit breakers [EV-HOU-682]; Tyler v. Hennepin County protects equity after a tax sale but not the home [EV-HOU-677].
- **Evidence.** [EV-HOU-670] [EV-HOU-671] [EV-HOU-681] [EV-HOU-682] [EV-HOU-683].
- **Cost source.** Section 6, 2.9: about $20 billion over FY2030-39 as states join, and about $3 billion a year from FY2040, permanent. This is the addendum's main permanent cost, and it adds to the FY2040 gap (section 6, 2.9).

### HOU-13.02 Protecting older owners' equity

**Parameters** (memo 12 part 3 B).
1. **Legal help.** Grants to legal aid and nonprofit providers, $200 million a year from FY2030 (decided, `DEC-2026-11-09-25`), to clear tangled titles, write simple wills and transfer-on-death deeds, and defend tax foreclosures, for owners of any age at or below 80% of area median income, on HOU-12.01's test. Clearing a title costs about $9,200 [EV-HOU-684].
2. **Reverse mortgages.** FHA's 2023 relief becomes law: servicers need not call a loan due while property-charge arrears are $5,000 or less, and repayment plans may run up to five years [EV-HOU-680]. HOU-13.01's deferral can cover the taxes [EV-HOU-678].
3. **Tax sales.** HOU-13.01, point 7.
4. **Heirs' property.** HUD and USDA publish the states that have enacted the uniform partition law [EV-HOU-685]; nothing is required of states.

- **Agency.** HUD (FHA; legal-aid grants through the Office of Housing Counseling).
- **Vehicle.** R2, mandatory, for the grants; the regular bill for the reverse-mortgage rules.
- **Evidence.** [EV-HOU-677] [EV-HOU-678] [EV-HOU-679] [EV-HOU-680] [EV-HOU-684] [EV-HOU-685].
- **Cost source.** Section 6, 2.9: about $2 billion over FY2030-39, $0.2 billion a year permanent. The reverse-mortgage rule has no scored cost while the program's capital ratio stays high [EV-HOU-679] (judgment).

### HOU-13.03 Service coordinators in older renters' buildings

**Parameters** (memo 12 part 4 C).
1. Every federally assisted rental building where most households are headed by someone 62 or over may get a service coordinator, who links tenants to home care, meals and benefits, adding to Section 202's about 1,500 [EV-HOU-672].
2. **Money: decided (`DEC-2026-11-09-25`).** $150 million a year more from FY2031, about $1.35 billion over the window. Basis: HUD's $122 million for about 1,500 grants [EV-HOU-672].
3. The coordinator refers tenants to Medicaid home care and to HOU-12.04.

- **Agency.** HUD (multifamily housing).
- **Vehicle.** R2, mandatory, permanent.
- **Evidence.** [EV-HOU-672] [EV-HOU-698] [EV-HOU-696].
- **Cost source.** Section 6, 2.9.

### HOU-13.04 Home-sharing grants

**Parameters** (memo 12, smaller point 2; `DEC-2026-11-09-22`). Small grants to nonprofits that match older owners with tenants who pay low rent and help around the house, as HomeShare Vermont does [EV-HOU-692]: $30 million a year in FY2031-39 (decided, `DEC-2026-11-09-25`; under the $50 million `DEC-2026-11-09-22` set). Time-limited, with HUD reporting matches and moves by 2035.

- **Agency.** HUD. **Vehicle.** R2, mandatory, time-limited. **Cost source.** Section 6, 2.9: about $0.27 billion.

### HOU-3C.06 Homes for older and disabled renters inside HOU-3C

**Parameters** (memo 12 part 4 C).
1. **A share by need.** Each state's revolving-fund plan (HOU-3C.01) and its loan pipeline (HOU-3C.02) states what share goes to homes for older and disabled renters, accessible and near services, set by the state's own need. There is no federal quota (`DEC-2026-11-09-22`).
2. **Count.** HOU-3C.04 reports homes built or preserved for older and disabled renters as their own line, by state. 2.46 million older renter households had worst case needs in 2023 [EV-HOU-672].
3. **Section 202.** If GAO's study of capital advances, due within a year of the ROAD to Housing Act [EV-HOU-676], shows Section 202 construction merits it, the plan adds it (memo 12 part 4 B; `DEC-2026-11-09-22`: "C, and B if ROAD study shows it merits it"), as a later decision.

- **Vehicle.** R2, inside HOU-3C's amounts. **Cost source.** None added.

### How these fit the rest of section 4

- **Rental help.** Nothing here changes who gets rental help. Older renters who are not disabled are still reconsidered once the care program is scoped (`DEC-2026-11-09-10`); stage 3's age limit is still open (`6-cost.md`, question 2).
- **HOU-4.13.** HOU-12.01's tribal share follows its rules.
- **HOU-5.01.** Public housing repair is separate; HOU-12 covers private homes.
- **HOU-3C.04.** Number 1 is unchanged; HOU-3C.06's homes are a reported line within it. Homes repaired under HOU-12 are reported separately and not counted toward the targets.
- **HOU-4.01.** The repair fund and the tax match use their own plain test, not the rental help's income rules, so a household on rental help has no second income check.
- **Clean power and care.** HOU-12.03 is the boundary with clean power; HOU-12.04 and HOU-13.03 with care. Each later dossier may change its side of the line.

## 9. The rural channel (memo 13)

Espen decided memo 13 on November 10, 2026 (`DEC-2026-11-10-02`): every part as recommended, with two words of their own. On Part 5: "grow both, leave immigration question for later". On Part 6: "carefully implemented to improve systems and delivery without leaving people behind". The research is the rural delivery note (`../foundations/rural-delivery.md`). These provisions make USDA Rural Development the plan's rural delivery channel: its field offices take and decide applications, and the plan's rural repair money flows through them. The design lens applies throughout: one plain income test, records the government already holds, local decisions in state and area offices, and published counts with review triggers instead of caps. Amounts and counts marked judgment are this section's; the headline numbers are the memo's, which Espen accepted.

### HOU-14.01 Rural Development's field staff, offices and systems, 2030-39

**Parameters** (memo 13 part 1 B).
1. **Staff.** About 2,000 more Rural Development staff over FY2030-32, back to about 5,000, FY2012's level, mostly housing loan and repair specialists in state and area offices, plus engineers and inspectors [EV-HOU-777] [EV-HOU-778]. The yearly hiring path is USDA's to set; the target is a published count by state.
2. **Decisions stay local.** Direct loan and grant applications under HOU-14.02 to .04 and HOU-12.01's rural door are taken and decided in state and area offices. National offices keep servicing support and systems. This reverses the June 2026 plan to centralize origination (rural delivery note, section 1.1).
3. **One loan system.** One origination and servicing platform with online applications, replacing the mainframe single-family system [EV-HOU-782], built in stages, single-family housing first. The ROAD to Housing Act already lets USDA use appropriated money for this [EV-HOU-758]; GAO's July 2027 technology report informs the build.
4. **Nonprofit packagers.** Local nonprofits that help families assemble applications are paid a packaging fee set to cover their cost, paid from the loan as now [EV-HOU-779].
5. **Review, not a rule.** USDA publishes each quarter, by state, how long decisions take, the share decided within 90 days and applicants' satisfaction, building on the ROAD Act's yearly timeliness reports [EV-HOU-763]. A state office past 90 days for two quarters gets a published review and more staff, not a penalty (`DEC-2026-11-09-13`).
6. **Money.** About $0.3 billion a year once staffed, plus about $0.15 billion a year for the system over FY2030-34, available until spent (judgment; section 6, 2.11).

- **Agency.** USDA Rural Development (Rural Housing Service), state and area offices.
- **Vehicle.** R2, mandatory, time-limited (FY2030-39), a salaries-and-systems appropriation like the Inflation Reduction Act's money through USDA (rural delivery note, section 1.4). From FY2040 the staff move to regular Agriculture appropriations.
- **Current law.** Salaries and expenses in annual Agriculture appropriations; USDA plans to keep FY2026's lower staffing [EV-HOU-777]. ROAD sec. 502 permits, without funding, more staff and better systems [EV-HOU-758].
- **Evidence.** [EV-HOU-763] [EV-HOU-777] [EV-HOU-778] [EV-HOU-779] [EV-HOU-780] [EV-HOU-782].
- **Cost source.** Section 6, 2.11: about $3.5 billion over FY2030-39; about $0.35 billion a year from FY2040 if kept.

### HOU-14.02 Section 502: direct loans at scale, with broader limits

**Parameters** (memo 13 part 2 C).
1. **Scale.** Direct loan levels of about $1.5 billion in FY2030, $2.5 billion in FY2031, $3.5 billion in FY2032 and $4 billion a year in FY2033-39, about 15,000 loans a year at full scale (judgment, at about $270,000 a loan [EV-HOU-700]). Each year's subsidy stays available until spent, so money unused in one year is not lost [EV-HOU-780].
2. **Direct loans to 100% of area median income.** The statutory limit rises from 80% [EV-HOU-766]. Payment help keeps its formula, so it shrinks as income rises; no new test is added.
3. **Guaranteed loans to HOU-10.01's limits.** 140% of area median income, and 160% in high-cost areas (the places HOU-10.01 already lists), instead of 115% [EV-HOU-766].
4. **First-generation priority.** Where requests exceed a state's direct loan money, first-generation buyers come first, by the buyer's signed statement, as in HOU-10.01, item 3.
5. **Loan limit and approvals.** The direct loan limit is 80% of FHA's area limits, and one state-office approval suffices (HOU-14.06).
6. **Servicing that acts early.** A borrower two payments behind is offered a modification, including a term of up to 40 years under the ROAD Act [EV-HOU-764], before any foreclosure step [EV-HOU-701].
7. **Credit elsewhere.** The statute's test [EV-HOU-765] stays, read from the credit report USDA already pulls; no lender denial letters.
8. **Review, not a cap.** USDA publishes each year loans by income band, first-generation status, race and county, and delinquency by state. A falling share of loans below 50% of area median income triggers a published review of the priority order, not an income cap.

- **Agency.** USDA Rural Housing Service, through HOU-14.01's offices and nonprofit packagers.
- **Vehicle.** R2, credit subsidy for the FY2030-39 loan levels; the income limits and the priority in the regular bill.
- **Current law.** Section 502 direct loans to 80% and guaranteed loans to 115% of area median income [EV-HOU-766]; $1 billion of direct loans in FY2026 [EV-HOU-781].
- **Evidence.** [EV-HOU-599] [EV-HOU-700] [EV-HOU-701] [EV-HOU-702] [EV-HOU-764] [EV-HOU-765] [EV-HOU-766] [EV-HOU-771] [EV-HOU-781].
- **Cost source.** Section 6, 2.11: about $3.5 billion of credit subsidy over FY2030-39; the guaranteed loans earn more in fees than they cost.

### HOU-14.03 Rural rental homes: rent help after every mortgage, and a preservation fund

**Parameters** (memo 13 part 4 B).
1. **An automatic offer.** A year before a Section 515 or 514 mortgage matures, or when an owner seeks to prepay, USDA offers continued rental assistance with no unit cap, using the authority the ROAD Act made permanent [EV-HOU-239]. Appropriations language drops the unit cap [EV-HOU-781].
2. **Vouchers when an owner leaves.** Tenants of a property that is prepaid, foreclosed or matured get rural vouchers, as the ROAD Act allows [EV-HOU-240], sized to everyone eligible.
3. **The preservation and transfer fund.** $0.5 billion a year, FY2030-39, for repairs and for sales to nonprofit, public, tribal and tenant buyers, available until spent. HOU-3C.01 and HOU-3C.02 may also finance these purchases, already an eligible use.
4. **Review, not a rule.** USDA publishes each year properties and units maturing, staying, leaving and transferred, by state, and its preservation pipeline. A state where more than a fifth of maturing units leave in a year gets a published review (judgment).

- **Agency.** USDA Rural Housing Service, multifamily staff funded under HOU-14.01.
- **Vehicle.** R2, mandatory, time-limited for the fund; appropriations for rental assistance and vouchers.
- **Current law.** Decoupling and the preservation program made permanent by the ROAD Act [EV-HOU-239]; rental assistance at $1.715 billion with decoupling up to 5,000 units in FY2026 [EV-HOU-781].
- **Evidence.** [EV-HOU-239] [EV-HOU-240] [EV-HOU-773] [EV-HOU-774] [EV-HOU-775] [EV-HOU-781] [EV-HOU-783] [EV-HOU-784] [EV-HOU-785].
- **Cost source.** Section 6, 2.11: the fund about $5 billion over FY2030-39; vouchers about $0.06 billion a year, permanent; continued rental assistance inside the baseline.

### HOU-14.04 Self-help and farmworker housing, 2030-39

**Parameters** (memo 13 part 5 B).
1. **Self-help (Section 523).** Technical-assistance grants of about $100 million a year [EV-HOU-770] [EV-HOU-776]. The family's own labor counts toward the home's value for the loan limit.
2. **Farmworker housing (Sections 514 and 516).** Loans and grants of about $200 million a year together, with rental assistance through Section 521 [EV-HOU-769] [EV-HOU-773].
3. **Not decided here.** The statute's immigration-status rule for farmworker housing occupants [EV-HOU-769] stays as it is; Espen left it for later immigration work.

- **Agency.** USDA Rural Housing Service, with nonprofit self-help grantees and farmworker housing sponsors.
- **Vehicle.** R2, mandatory, time-limited (FY2030-39).
- **Current law.** About $25 million for self-help grants and about $21 million for farmworker housing loans and grants in FY2026 [EV-HOU-756].
- **Evidence.** [EV-HOU-756] [EV-HOU-769] [EV-HOU-770] [EV-HOU-776].
- **Cost source.** Section 6, 2.11: about $2.5 billion over FY2030-39.

### HOU-14.05 One rural test for housing, with no one losing eligibility

**Parameters** (memo 13 part 6 B, as Espen qualified it).
1. **The test.** For USDA's housing programs, a rural area is any place of up to 35,000 people outside an urbanized core, on one published map. The "rural in character" and "serious lack of mortgage credit" judgments go [EV-HOU-767].
2. **No one loses eligibility.** Every place eligible on the day the law takes effect stays eligible, whatever later censuses show. Every household with a USDA loan, grant, rental assistance or a pending application keeps its help and its place in line, wherever the line moves.
3. **One step at a time.** The new map takes effect only once USDA has published it and the loan system (HOU-14.01) checks addresses against it. Until then the current definition and its grandfather clause apply, and Congress extends the grandfather clause past the 2030 census so no place falls out in the meantime [EV-HOU-767].
4. **A published count, not a gate.** Before the map takes effect and each year for five years after, USDA publishes how many places and people gained and lost eligibility, by state, and the number of applications from newly eligible places. Any place or household recorded as losing eligibility triggers a published review and a fix under item 2 (judgment; the count is the review trigger, not a condition on anyone's help).

- **Agency.** USDA Rural Development, with the Census Bureau's urban-area files.
- **Vehicle.** Regular bill (the definition and the hold-harmless).
- **Current law.** 42 U.S.C. 1490's tiers and grandfather clause to the 2030 census [EV-HOU-767]; seven definitions across Rural Development (rural delivery note, section 1.6).
- **Evidence.** [EV-HOU-767].
- **Cost source.** None of its own; it spreads fixed program money over somewhat more places (section 6, 2.11).

### HOU-14.06 Day-one rule changes, 2029

**Parameters** (memo 13, "Day one").
1. Start rulemaking to drop Section 504's age-62 grant rule, its assets test and the three-year repayment rule [EV-HOU-760] [EV-HOU-761]. A notice-and-comment rule, so it starts in 2029 and takes effect when final.
2. Restore the Section 502 direct loan limit to 80% of FHA's area limits, a packaging fee that covers cost and single approval in state offices [EV-HOU-779].
3. Keep loan origination in state and area offices (HOU-14.01, item 2).
4. Offer continued rental assistance before every maturing mortgage, up to the appropriations limit then in force (HOU-14.03) [EV-HOU-781].
5. Publish decision times and applicant satisfaction by state each quarter (HOU-14.01, item 5) [EV-HOU-763].

- **Agency.** USDA. **Vehicle.** Executive action (January 2029), handbook and rule. **Cost source.** None.

### How these fit the rest of section 4

- **HOU-12.01.** Its rural door (item 11) is the repair half of this channel; it adds no money.
- **HOU-10.01.** Its down payment help stacks with Section 502 loans (item 10), and HOU-14.02 gives the guaranteed loans the same income limits.
- **HOU-3C.** Its funds may buy and preserve Section 515 properties; HOU-3C.04's number 1 does not count USDA loans for owners, which are reported separately.
- **HOU-4.13.** Tribal areas: USDA's Native American relending pilot and Section 502 on trust land are not yet researched (rural delivery note, section 5); a later step should weigh them with the tribal set-asides.
- **Other dossiers.** The rural delivery note's other channels (water, power, broadband, community facilities) and the single test for all of Rural Development go to their own dossiers.

## Interactions with the rest of the plan

Espen asked how housing lands with the home health coverage expansion, child care, the expanded child tax credit and the secure floor, for each group in need (`DEC-2026-11-09-06`). This table states the mechanism and the check. The figures belong to the household model and section 7; none is estimated here.

| Group | What housing gives | Health coverage (HLT-1, HLT-4) | Child care (FAM-2) | Child tax credit (FAM-1) | Secure floor and other help | Checks for section 7 and the household model |
| --- | --- | --- | --- | --- | --- | --- |
| Families with children | Stage 1 (homeless families) and stage 2 (2030-37); attached homes outside poor areas; search help | Children's continuous coverage (HLT-4) can supply the Medicaid income finding the common application reuses (HOU-4.02) | FAM-2's cap lowers child care costs. Current law deducts child care costs from income when setting rent, so lower costs can raise rent slightly (deduction in 42 U.S.C. 1437a(b)(5); not yet checked) | Monthly advance credit is not counted for rent (26 U.S.C. 6409); no rent offset | Paid leave (FAM-3) and wage gains count as income unless excluded (shared rule 1) | Combined effect on net income and rent for a family on a voucher with FAM-1, FAM-2 and FAM-3; stacked phase-out rate (shared rule 2); stage 2's reach to children by age |
| The lowest-income households | The guarantee's stages; HOU-1D for crises | Restored Medicaid (HLT-1) is a route into HOU-1D's eligibility by enrollment (HOU-1D.01) | As above | As above | New income support outside the tax code raises rent by up to 30 cents per dollar unless excluded (shared rule 1) | Rent offset at 0 and 30 cents per dollar of new benefits; which households fall in no stage in the 2030s (memo 2 B) |
| Immigrants | Section 214 rules with proration for mixed-status families, protected in statute against HUD's February 2026 proposed rule (HOU-4.01, `DEC-2026-11-09-10`); the shared record holds no status and is barred from immigration enforcement use (HOU-4.02, `-11`) | Coverage rules follow the health dossier and the immigration table | FAM-2's own rules | FAM-1's taxpayer-identification rules | IMM-1's new statuses are not on Section 214's list unless the law adds them (shared rule 3) | One eligibility table across housing, health, FAM-1 and FAM-2 for each status; how many mixed-status families with children in stages 1-2 get prorated help |
| People currently and chronically homeless | Stage 1 first; Housing First (HOU-4.09); attached homes ready to enter; supportive housing with a navigator duty on providers (HOU-4.11) | Medicaid services offered on entry (shared rule 7); HLT-4's health centers | — | Homeless families may not file taxes; the common application offers FAM-1 enrollment (HOU-4.02) | Coordinated entry hands off to the guarantee | Share of homeless households reached by 2033; FAM-1 take-up among homeless families; asylum-seeker shelter demand left to the immigration dossier [EV-HOU-062] |
| People with substance use disorders | Housing without treatment conditions; voluntary recovery housing that accepts residents on prescribed medicines (HOU-4.10); treatment access in supportive housing (HOU-4.11) | Medicines for opioid use disorder and contingency management depend on what Medicaid covers. Tenancy supports and assertive community treatment are asked of HLT-4 (HOU-4.12). Restoring Medicaid (HLT-1) protects coverage from the 2027 work requirements | — | — | No treatment condition anywhere (shared rule 6) | Outcomes for people with active addiction (HOU-4.10's evaluation); whether treatment capacity is in place where HOU-4A's stage 1 lands |
| Older and disabled people | Stage 3 from 2038 for disabled extremely low-income renters of any age (HOU-4.08); accessible homes (HOU-3C.03). Older renters who are not disabled have no funded route in the 2030s; the 2040s route names them (HOU-4.03); they are reconsidered once the care program is scoped (`DEC-2026-11-09-10`) | HCBS (HLT-4) delivers the services stage 3 depends on. Medicare's out-of-pocket cap (HLT-2) may lower the medical-expense deduction older and disabled tenants take, and so raise rent slightly (not yet checked) | — | — | Social Security protection and SSI count as income for rent | Older unassisted renters with severe needs left without help through 2039 (memo 8); the medical-deduction effect; reserved accessible units against stage 3 demand |

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
| Memo 2 B: stage 2 guarantee | HOU-4D.01 | R2, mandatory | Enrollment 2034-36; a right from 2037 | $81 billion, plus about $17 billion for the count restated with stage 1 uncapped (`6-cost.md`, 2.12) (ledger: `recovery-adoption.json` `housing_extra_tn` 0.135, booked from 2030; section 6 proposes retiming) |
| Memo 2 condition: stage 3, disabled renters | HOU-4.08, HOU-3C.03 | R2 (effective 2038) | From 2038 | $5 billion in FY2038-39; about $14 billion a year by FY2042; outside the $135 billion. With disabled renters 62 and over (`DEC-2026-11-10-03`), about $10 billion and $28 billion |
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
| `DEC-2026-11-09-09`: FY2040 gap to the financing settlement; capital spent by 2039 | HOU-3C.01, HOU-3C.02, HOU-5.01 (timing) | — | Awards end 2037-38 | FY2040: about $110 billion of permanent cost, with every addendum and `DEC-2026-11-10-03`; the capital tail falls from about $16 billion to about $8 billion (`6-cost.md`, 3.3) |
| `DEC-2026-11-09-10`: duty to house from 2037 | HOU-4D.01, HOU-4.07 | R2 | From 2037 | About $3 billion in FY2037-39 (placements) |
| `DEC-2026-11-09-10`: production targets (three numbers, Espen in session November 9) | HOU-3C.04 | Regular bill; R2 (reporting) | 2030-39 | None |
| `DEC-2026-11-09-10`: mixed-status protection; repeal of HUD's proposed rule | HOU-4.01 | Executive action (January 2029); regular bill | From 2029 | None against current law |
| `DEC-2026-11-09-10`: tribal housing | HOU-4.13, HOU-1D.03, HOU-3C.01, HOU-3C.02, HOU-4A.01, HOU-4D.01, HOU-2D.01 | R2 (set-asides); regular bill (NAHASDA rules) | From 2030 | Shares of existing amounts; no added cost |
| `DEC-2026-11-09-10`: older non-disabled renters reconsidered after the care program is scoped | HOU-4.03 | — | — | None yet |
| `DEC-2026-11-09-10`: section 5's delivery items | HOU-4.02 (R1 readiness), HOU-4.12 (wider backstop), HOU-4.06 (testing), HOU-4D.01 (deemed approval; private right of action), HOU-5.02 and HOU-4.11 (private rights of action) | R1; R2; regular bill | 2029 on | Readiness $0.75 billion in FY2029; others above; attorney's fees and deemed approval's error cost unpriced |
| `DEC-2026-11-09-11`: the record holds basic information only, with an enforcement bar; stage 2's exit at 80% of area median income | HOU-4.02, HOU-4D.01 | Regular bill; R2 | From 2030 | None separately; the exit rule is inside stage 2's flat count |
| `DEC-2026-11-09-12`: stage 1's plain test, doubled-up families with children included, no cap; stage 2 widened to them and to homeless families | HOU-4.03, HOU-4D.01 | R2 | From 2030; stage 2 from 2034 | About $17 billion over FY2030-39 and $8 billion in FY2040 (`6-cost.md`, 2.7) |
| `DEC-2026-11-09-14`, `-16`, `-17`: the proposed parameters decided (production targets; tribal set-aside sizes; the emergency fund's annual cap of four months' Fair Market Rent and repeat-use review; testing money; R1 readiness; duty-to-house deadline; record and penalty rules; stage 3 disability proof; local intake order; trial report dates); the bond-deal basis boost left out, since replaced by `DEC-2026-11-09-18` (in only for poorest-renter buildings) | HOU-3C.04, HOU-4.13, HOU-1D.01, HOU-4.06, HOU-4.02, HOU-4D.01, HOU-4.08, HOU-4.03, HOU-2D.01, HOU-2D.02 | As each provision | As each provision | Testing $0.5 billion and R1 readiness $0.75 billion (section 6); the rest no added cost |
| Memo 11 part 1 C: the home repair fund (`DEC-2026-11-09-21`) | HOU-12.01 | R2, mandatory, time-limited (envelope borrowing proposed) | 2030-39 | About $37 billion of outlays (`6-cost.md`, 2.9) |
| Memo 11 parts 2 B and 3 B: renter repairs; one front door with clean power | HOU-12.02, HOU-12.03 | R2 (inside HOU-12.01); regular bill (shared eligibility) | 2030-39 | Inside HOU-12.01 |
| Memo 12 part 1 B: property-tax match for older owners (`DEC-2026-11-09-22`) | HOU-13.01, HOU-13.02 (tax-sale offer) | R2, mandatory, permanent | From FY2031 | About $20 billion; about $3 billion a year from FY2040 (`6-cost.md`, 2.9) |
| Memo 12 part 2 B: older-adult home changes | HOU-12.04 | R2 (inside HOU-12.01) | 2030-39 | Inside HOU-12.01 |
| Memo 12 part 3 B: equity protection | HOU-13.02 | R2 (grants); regular bill (reverse-mortgage rules) | From 2030 | About $2 billion; $0.2 billion a year permanent |
| Memo 12 part 4 C and smaller points: older renters' homes, service coordinators, accessory units, home sharing | HOU-3C.06, HOU-13.03, HOU-12.01 (point 5), HOU-13.04 | R2 | From 2030-31 | Coordinators about $1.35 billion and $0.15 billion a year permanent; home sharing about $0.27 billion; HOU-3C.06 inside HOU-3C |
| Memo 13 part 1 B: Rural Development's staff, local decisions, one loan system (`DEC-2026-11-10-02`) | HOU-14.01 | R2, mandatory, time-limited; then appropriations | 2030-39 | About $3.5 billion; about $0.35 billion a year from FY2040 if kept (`6-cost.md`, 2.11) |
| Memo 13 part 2 C: Section 502 at scale, broader limits | HOU-14.02, HOU-10.01 (item 10) | R2 (credit subsidy); regular bill (limits) | 2030-39 | About $3.5 billion of subsidy |
| Memo 13 part 3 B: the rural door into the repair fund | HOU-12.01 (item 11) | R2 (inside HOU-12.01); regular bill (routing) | 2030-39 | Inside HOU-12.01 |
| Memo 13 part 4 B: rent help after every mortgage, vouchers, preservation fund | HOU-14.03 | R2 (fund); appropriations | 2030-39; vouchers permanent | About $5 billion for the fund plus about $0.6 billion of vouchers; $0.06 billion a year permanent |
| Memo 13 part 5 B: self-help and farmworker housing (immigration rule left for later) | HOU-14.04 | R2, time-limited | 2030-39 | About $2.5 billion |
| Memo 13 part 6 B: one rural test, no one losing eligibility | HOU-14.05 | Regular bill | From the new map's publication | None |
| Memo 13, day one | HOU-14.06 | Executive action and rule | 2029 | None |
| `DEC-2026-11-10-03`: the milestone review's items and the open cost questions | HOU-3C.04 (state counts), HOU-2D.01 (rural boost out), HOU-4.08 (62 and over; severe-problems test), HOU-10.01 (cap), HOU-10.02 (through 2039), HOU-1D.01 and .04 (fund sizes; construction gap money dropped), HOU-6.01 (ends unless renewed), HOU-4D.01 (85% central), HOU-4.03 (2040s route), HOU-8.01 (size and evaluation), HOU-4.01 (child care) | As each provision | As each provision | About +$22 billion over FY2030-39 and +$13.7 billion in FY2040 (`6-cost.md`, 2.12) |

**Consistency notes.**
- **Totals.** The ledger's housing title ($0.56 trillion midpoint: the $0.47 trillion title and $0.09 trillion of vouchers) predates every section 3 decision. It still carries HOU-1A, HOU-2A and HOU-6's separate fund as filed. HOU-4D is carried outside the ledger in `recovery-adoption.json`. Section 6 rebuilds them from this section's provisions: about $0.81 trillion over FY2030-39 (central, with option D's credits, memos 9-13 and `DEC-2026-11-10-03`) and about $110 billion a year of permanent cost in FY2040; the FY2040 gap is about $40 billion on permanent lines ($51 billion with tails), and FY2041 fails by about $7 billion (`6-cost.md`, 3.3). Its ledger and model changes are tier-3 proposals (`6-cost.md`, 5).
- **Regular-bill items.** HOU-4.01's definitions and mixed-status protection, HOU-4.02's data rules and enforcement bar, HOU-4.05, HOU-4.06, HOU-4.09, HOU-4.11, HOU-4.13's NAHASDA rules, HOU-1D.03's privacy rules, HOU-3C.04's target, HOU-5.02, HOU-6.01's eligibility changes, HOU-6.02 and HOU-9A.01's corporation. With the legacy floor bill (ledger row HOU-7), they make one housing regular bill. Its floor time is a section 5 question.
- **Decided since the milestone review.** Fees at the full rate (HOU-4A.02), the screening rule (HOU-4.01), the 12-month rule for people leaving prison, jail or foster care (HOU-4.03) (`DEC-2026-11-10-06`); the 2040s route's date and the social housing pilot's numbers (HOU-4.03, HOU-8.01), and FY2041's gap to the financing settlement (`DEC-2026-11-10-04`). Nothing in this section waits on Espen.
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
- Reentry and foster youth (HOU-4.03, HOU-4.01): a study of whether past criminal records predict tenancy outcomes for subsidized tenants (Wilder Research's 2019 Minnesota study could not be retrieved); a federal count of homelessness among people released from prison; HHS's AFCARS count of youth leaving foster care to emancipation and NYTD's homelessness outcomes (acf.gov blocked automated download; Espen could upload copies); how many housing agencies use blanket criminal-record bans.
- Immigrant eligibility (HOU-4.01): whether a federal match for state property-tax relief is a federal or a state public benefit under 8 U.S.C. 1611 and 1621 (legal review); HUD's older guidance on CDBG and HOME under the welfare law; the appeal status of *New York v. Department of Justice* [EV-HOU-809].
- The voucher rules on repaying underpaid rent (24 CFR 982 and 5), for HOU-4D.01, item 8.
