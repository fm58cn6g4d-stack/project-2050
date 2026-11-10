# Care you can count on, part A (health): specification

Role: section 4 of the care dossier, health part. It writes the decided health design as provisions: what each does, its parameters, who is covered and who pays, the vehicle, the agency, how it changes current law, and the evidence it rests on. Provision IDs and their fields are in `provisions.json`. Status: draft (stage D, step 4, PR 1). Espen decided the design in `DEC-2026-11-09-07`, `DEC-2026-11-10-09`, `DEC-2026-11-10-11` and `DEC-2026-11-10-12`; where the memos and the later decisions differ, the later decisions govern ("What the decisions changed" below). Costs are in `6-cost.md`; each provision's `cost_source` points there.

## How to read this section

- **Status of each provision.** *Decided* means Espen decided it (a memo option, a yes-or-no point or a later decision). *Adopted from the S. 1506 comparison* means `research-s1506-comparison.md` recommended it as following from a decision already made, as the brief for this section asked; none of those needs a new decision (list below). *A working choice* is a parameter this section sets so the draft is complete; it rests on judgment and can change without reopening a decision. *Open* marks a question left open under "What needs an answer now" (`DEC-2026-11-10-07`), with its alternatives. *For Espen* marks the one provision that waits on a yes-or-no answer (HLT-7.15).
- **Commitments and working assumptions.** Section 4 commits to who is covered, the benefit, the rate basis, the order and dates, the protections and the plumbing. Exact copay amounts, the employer contribution's share, the state share and the size of the funds are working assumptions with ranges in section 6.
- **Dates.** The plan begins in January 2029 (`DEC-2026-10-29-01`). Calendar dates are when people are covered; fiscal years are for money. Nothing here is a 2027-28 exception.
- **One public plan, built in steps.** The 2029 law creates the single plan (called "the plan" below) as an expansion of Medicare. People join it in waves: everyone uninsured or in the individual market and every child in 2031; Medicaid enrollees and employer groups in thirds over 2033-35; everyone else on January 1, 2035. Until each group joins, its current coverage continues, and today's Medicare enrollees keep Medicare with the upgrades in HLT-2.
- **Shared rules** stay in one place: "Shared rules kept in one place" below.
- **Evidence.** The last column of each table lists the evidence IDs a provision rests on. Where a parameter is a working choice with no entry, the column says so. Figures marked "project arithmetic" come from `tools/health_path.py` on the coverage model (`models/tools/health-coverage/`, exploratory).

## The vehicles

| Vehicle | Votes | When | What it carries | Money (section 6) |
| --- | --- | --- | --- | --- |
| 2029 reconciliation act (R1) | 51 | 2029, the first bill | Restoration (HLT-1); the Medicare Advantage fix (HLT-6.01); drug negotiation extended (HLT-6.02); USDA rural health lending and grants (HLT-8.01) | Restoration about $86 billion in FY2030 before wave 1 replaces most of it; the Advantage fix saves about $0.5 trillion over FY2030-34 |
| The Medicare for All Act of 2029 (HLT-7) | Regular order under the Senate rules reform the plan assumes (D2, decided: graduated cloture in the first week of 2029; `dossiers/scenario/4-2029-plan.md`) | Enacted in 2029; wave 1 January 1, 2031; endpoint January 1, 2035 | The plan: entitlement, enrollment, benefits, providers, payment, the five protections, the fund, the federal systems, the end of duplicative coverage; Medicare's upgrades and other bridge rules for today's enrollees (HLT-2); the end of federal abortion funding limits (RTS-2) | The plan's net federal cost: about $25.7 trillion over FY2030-39 before the employer contribution, $4.7 trillion in FY2040 |
| Financing settlement (not this dossier) | — | Before the endpoint | The taxes that replace premiums, including the payroll contribution that replaces the employer transitional contribution (HLT-7.18) | The amount to be financed (section 6, part 4) |
| Annual appropriations | 60 today; majority under D2 | Each year | The Indian Health Service (open item, HLT-7.24); the plan-era appropriations acts carry no Hyde-type riders (RTS-2.02) | — |

**Why the plan is not in reconciliation.** Reconciliation carries spending and revenue, not program design that has no budget effect (the Byrd rule), so an entitlement with its rights, provider rules, offices and an endpoint written into law needs regular order. The legacy design put the public option on the same footing (HLT-3, rail FLOOR in `models/data/inputs/ledger-bills.csv`). If the rules reform fails, the fallback is to move the plan's money (the waves' spending, the fund's streams) into a later reconciliation act and leave the rest for 60 votes; section 5 sets out that path and section 8 names it as a risk.

## The 2029 reconciliation act: restoration and Medicare payment (HLT-1, HLT-6, HLT-8)

Point 1 of `3-design.md`, decided: restore first, whatever else passes.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| HLT-1.01 | Repeal the 2025 law's Medicaid eligibility cuts (decided, point 1) | Repeal the work requirement (sec. 71119), six-month redeterminations for expansion adults (sec. 71107), the retroactive-coverage limit (sec. 71112) and cost sharing for expansion adults (sec. 71120); effective on enactment, before the work requirement's later state start dates bite | HHS (CMS); states | EV-CAR-001, EV-CAR-002, EV-CAR-006, EV-CAR-007, EV-CAR-010, EV-CAR-025, EV-CAR-026 |
| HLT-1.02 | Restore lawfully present immigrants to Medicaid and the premium credit (decided, point 1; shared rule 3) | Repeal secs. 71109 and 71301's limits and the emergency-Medicaid match cut (sec. 71110); people without status are the immigration flagship's decision (point 3) | HHS (CMS); Treasury (IRS) | EV-CAR-008, EV-CAR-009, EV-CAR-016, EV-CAR-103 |
| HLT-1.03 | Restore Medicaid financing: provider taxes and state directed payments (decided, point 1) | Repeal secs. 71115 and 71116 and the expansion-incentive limit (sec. 71114); lasts until each state's Medicaid enrollees join the plan (HLT-7.03) | HHS (CMS) | EV-CAR-011, EV-CAR-012, EV-CAR-013, EV-CAR-024 |
| HLT-1.04 | Restore the enhanced premium credits and repeal the marketplace verification rules until wave 1 (decided, point 1) | Enhanced credit schedule for plan year 2030; repeal secs. 71303 and 71304 (verification before credits; special-enrollment limits); the individual market joins the plan on January 1, 2031, which ends the credits | Treasury (IRS); HHS (CMS) | EV-CAR-017, EV-CAR-018, EV-CAR-028, EV-CAR-029, EV-CAR-049, EV-CAR-050 |
| HLT-6.01 | Medicare Advantage: fix coding and benchmarks on MedPAC's method (decided, point 5) | Risk scores from two years of encounter data with a coding-intensity adjustment set to MedPAC's estimate; benchmarks rebased so Advantage pays no more than traditional Medicare for similar people; payment year 2030 at half strength, 2031 in full; savings counted at MedPAC's lower 2026 estimate (14%, about $76 billion in 2026); Advantage ends at the endpoint (HLT-7.25) | HHS (CMS) | EV-CAR-061, EV-CAR-135 |
| HLT-6.02 | Drug price negotiation extended to all drugs Medicare covers, then to the plan (decided, memo 5 B) | Builds on the 2022 law's Medicare negotiation; removes its yearly drug count and small-molecule wait; negotiated prices apply to the plan from 2031 (HLT-7.13) | HHS (CMS) | EV-CAR-220 |
| HLT-8.01 | Rural health through USDA Rural Development: scale what exists (decided, point 6 option b) | Community Facilities direct lending for rural hospitals, clinics and nursing homes raised to $3-5 billion a year; $200-500 million a year of competitive grants restored; Rural Development's state offices as a front door to HRSA, CMS and the Rural Health Transformation Program; no new service. The navigator's remit is set in section 5 | USDA (Rural Development); HHS (HRSA, CMS) | EV-CAR-015 (and `dossiers/foundations/rural-delivery.md`, SRC-2112, SRC-2125, SRC-2131) |

## The Medicare for All Act of 2029 (HLT-7, HLT-2, RTS-2)

Memo 1 B with the endpoint in law, decided (`DEC-2026-11-10-09`), with the endpoint moved to 2035 (`DEC-2026-11-10-11`).

### Title I: who is covered, how and when (HLT-7.01 to HLT-7.04)

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| HLT-7.01 | Entitlement: every resident (decided, point 3; status rule proposed to the immigration flagship) | Every person who lives in the United States is entitled to the plan once their wave starts; residency by rule, on the S. 1506 model (sec. 102), which the immigration flagship receives as the proposal for shared rule 3; people without status: the immigration flagship decides (open for that owner) | HHS (CMS) | EV-CAR-103, EV-CAR-270 |
| HLT-7.02 | Automatic enrollment and renewal from records; no premiums; a card without a Social Security number (decided, point 2; the card adopted from the S. 1506 comparison) | Enrolled at birth, on establishing residency, or on the group's wave date, from records the government holds (tax, Social Security, Medicaid, employer payroll); renewal at most yearly and without forms where records suffice; no work requirement; no premium; the card shows no Social Security number (S. 1506 sec. 105); anyone missed is enrolled at the point of care | HHS (CMS); SSA; Treasury (IRS) for records | EV-CAR-206, EV-CAR-210, EV-CAR-211, EV-CAR-212, EV-CAR-271 |
| HLT-7.03 | The waves and the endpoint, written as automatic (decided, memo 2 order and `DEC-2026-11-10-11`) | **Wave 1, January 1, 2031:** the uninsured, the individual market and every child under 19, plus Medicare at 60 (HLT-2.04). **Wave 2, 2033-35:** Medicaid and CHIP enrollees and employer groups together, required, in three cohorts on January 1 of 2033, 2034 and 2035 (working choice: about a third of each group a year; Medicaid by state, employer groups by firm size, smallest firms first). **Endpoint, January 1, 2035:** everyone else, including today's Medicare enrollees, FEHB enrollees and any group not yet moved. Each date takes effect unless Congress votes to delay it; HHS publishes a readiness report 18 months before each date (a published count, not a gate) | HHS (CMS); Labor and Treasury for employer cohorts | EV-CAR-200, EV-CAR-272, EV-CAR-293, EV-CAR-310, EV-CAR-313 |
| HLT-7.04 | No gap in anyone's coverage (decided, protection 1) | A person leaves their old coverage only when the plan is active for them; an employer or state may not end coverage before its cohort's date; anyone who loses coverage before their wave is enrolled in the plan at once | HHS (CMS) | EV-CAR-210 |

### Title II: benefits (HLT-7.05 to HLT-7.07)

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| HLT-7.05 | Comprehensive benefits, including abortion and reproductive care (decided, memo 4 C and `DEC-2026-11-10-11`) | Hospital, outpatient, primary and preventive care, prescription drugs, mental health and addiction treatment, maternity and newborn care, comprehensive reproductive care including abortion, contraception and fertility care, dental, vision and hearing, rehabilitation and devices, laboratory and imaging; the S. 1506 list (sec. 201) as the drafting base, without its long-term care title (HLT-7.07) | HHS (CMS) | EV-CAR-110, EV-CAR-276 |
| HLT-7.06 | Small capped copays above 200% of poverty (decided, memo 4 C) | No cost sharing below 200% of the poverty guideline, or for anyone for primary care, prevention, maternity, mental health and chronic-condition drugs; small fixed copays for other services above that line; a yearly cap of $1,000 a person (working figure); income from the prior year's tax records, and no copay where no record shows income above the line; no deductibles, coinsurance or networks. S. 1506's stricter protection (no cost sharing at or below 250%) is noted as the alternative | HHS (CMS); Treasury (IRS) for income | EV-CAR-113, EV-CAR-219, EV-CAR-223, EV-CAR-224, EV-CAR-277 |
| HLT-7.07 | Long-term care left to part B; Medicaid's long-term care continues meanwhile (decided, memo 4) | Home and community services and nursing-home care stay in Medicaid, with today's eligibility and state roles, when Medicaid enrollees' other care moves to the plan; part B decides whether and how they move; estate recovery is a part B question | HHS (CMS); states | EV-CAR-138, EV-CAR-278 |

### Title III: providers (HLT-7.08 to HLT-7.09)

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| HLT-7.08 | Participation, no balance billing, all-in or all-out private contracts, no utilization bonuses (adopted from the S. 1506 comparison) | A participating provider accepts the plan's payment in full; a provider who contracts privately for covered services does so for all patients for a year, as Medicare's opt-out works today; no pay or bonus tied to the volume of care used; the VA, IHS, tribal and military facilities qualify as providers (S. 1506 secs. 301-303, 302(b)) | HHS (CMS) | EV-CAR-279, EV-CAR-315 |
| HLT-7.09 | Non-discrimination, with a private right of action (adopted from the S. 1506 comparison) | No provider or the plan may discriminate on the grounds in S. 1506 sec. 104; a person may sue to enforce it | HHS (Office for Civil Rights); courts | EV-CAR-270 (the bill's text, SRC-3260); evidence still needed for sec. 104's wording |

### Title IV: payment (HLT-7.10 to HLT-7.15)

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| HLT-7.10 | Hospital rates on a five-year glide path to about 1.15 times Medicare (decided, memo 5 B and protection 3) | In 2031 the plan's hospital conversion factor pays, on average, today's all-payer average hospital rate (about 1.25 times Medicare on the coverage model's inputs; project arithmetic); it falls in five equal steps to about 1.15 times Medicare in 2036; the target by service is set by rule (working figure 1.15) | HHS (CMS) | EV-CAR-131, EV-CAR-220, EV-CAR-259 |
| HLT-7.11 | Global budgets for rural, critical-access and safety-net hospitals (decided, memo 5 B) | A fixed yearly budget, set from the hospital's prior net patient revenue and indexed, with a volume corridor, on Maryland's model; eligible: critical-access and sole-community hospitals, hospitals in areas under the plan's rural test (the housing dossier's one rural test, up to 35,000 people, `DEC-2026-11-10-02`), and safety-net hospitals (top quarter by share of Medicaid and uninsured patient days); during and after the glide | HHS (CMS) | EV-CAR-259, EV-CAR-261 |
| HLT-7.12 | Physicians and other clinicians at Medicare's fee schedule, with primary-care and rural add-ons (decided, memo 5 B) | Medicare's fee schedule from 2031; a primary-care add-on and a rural and shortage-area add-on (working figure: 10% each, on Medicare's shortage-area bonus); no glide | HHS (CMS) | EV-CAR-220 |
| HLT-7.13 | Drug prices: negotiated for all drugs, a fallback price, a formulary (decided, memo 5 B; the fallback and formulary adopted from the S. 1506 comparison) | Annual negotiation for every covered drug (HLT-6.02); if no agreement is reached, the price is the lowest of the VA's price and Medicaid's best price (the fallback in S. 1506 sec. 1012(d)); a national formulary that favors generics and biosimilars | HHS (CMS); VA (price data) | EV-CAR-220, EV-CAR-285, EV-CAR-315 |
| HLT-7.14 | Medicare Advantage ends at the endpoint (decided, point 5) | No new Advantage contracts after plan year 2034; the plan pays providers directly from January 1, 2035 | HHS (CMS) | EV-CAR-135, EV-CAR-288 |
| HLT-7.15 | **Hospital transition fund and a revenue floor for global-budget hospitals (recommended; for Espen, question 1)** | A capped fund, $100 billion over FY2033-38 (working figure, range $50-150 billion), for hospitals whose net patient revenue falls more than 5% below their pre-transition level as their patients' coverage moves; first claim for global-budget hospitals (HLT-7.11) and sole providers in their area; for three years after their area moves, global budgets are at least the hospital's pre-transition net patient revenue, indexed, paid from the fund; replacement falls from 100% of the loss in the first year to 20% in the fifth; conditions: keep emergency, obstetric and behavioral health services open, no fund money for executive bonuses or distributions to owners. Keeps the five-year glide unchanged | HHS (CMS) | EV-CAR-333, EV-CAR-335, EV-CAR-336, EV-CAR-337, EV-CAR-338, EV-CAR-339, EV-CAR-340, EV-CAR-341; project arithmetic (6-cost.md, part 3) |

**Why a fund and not a slower glide** (Espen's direction: "we can alter the hospital pay glide path and/or add some extra funding to soften the blow of a faster transition, especially for rural providers"). On the coverage model's inputs, the move to the plan's rates changes hospital revenue as a whole little, but moves a great deal of it between hospitals. At the target rate (2032 terms), commercial hospital revenue falls by about $770 billion a year, and Medicaid's patients, today's Medicare patients and the newly insured bring about $690-780 billion more, net of what hospitals collect for the uninsured today (project arithmetic, `tools/health_path.py`). The net for hospitals as a whole is between about 4% lower and 1% higher, while the shift between them is about ten times that: hospitals with many commercial patients lose, and hospitals with many Medicaid and uninsured patients gain. A slower glide pays every hospital by its volume, including those that gain, and costs about $0.3 trillion more over FY2030-39 for a seven-year glide. It would cover a possible dip in hospitals' total revenue in FY2035-37, but it does little for the hospitals that lose most, because the glide starts at the all-payer average, not at commercial rates. A lasting shortfall in hospitals as a whole would be a question about the 1.15 target (memo 5), not the transition. The hospitals with room to absorb a cut are those that now earn most: in FY2024 for-profit hospitals' all-payer operating margin was 14.5% against 5.9% at nonprofits, and urban hospitals' 6.6% against 1.5% in rural areas outside micropolitan towns (MedPAC, 2026) [EV-CAR-336], and market power is what raises commercial prices (CBO, 2022; MedPAC, 2017) [EV-CAR-340] [EV-CAR-341]. Rural hospitals lean more on Medicare, which pays them closer to cost than it pays urban hospitals (a −3.4% Medicare margin against −12.6%) [EV-CAR-337], so a plan rate above Medicare's helps them; the ones at risk are rural hospitals with thin margins and a large commercial share, which the fund reaches first. Since 2010, 87 rural hospitals have closed and 68 converted (Sheps Center, 2026) [EV-CAR-338]. A capped fund aimed at the hospitals that lose, with rural and sole providers first, reaches the hospitals Espen named at about a third of the cost. The options and their costs are in section 6, part 3.

### Title V: protections during the change (HLT-7.16 to HLT-7.18)

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| HLT-7.16 | Help for insurance and billing workers (decided, protection 2) | Wage replacement and continued pay toward retirement for up to three years, training, job placement, and first claim on the plan's administrative jobs; eligibility from employer records (an insurer, billing firm or provider billing office certifies the layoff), not individual proof; FY2033-38 | Labor; HHS | EV-CAR-232, EV-CAR-233, EV-CAR-282, EV-CAR-345, EV-CAR-346, EV-CAR-347 |
| HLT-7.17 | States keep paying a share: maintenance of effort (decided, protection 5 and memo 3 B) | Each state pays the fund a fixed amount for its residents who move: half of its own current Medicaid spending for them (working figure; range 0-80%, set by the financing settlement), indexed to the plan's per-person cost growth; long-term care stays with the state under HLT-7.07 | HHS (CMS); states | EV-CAR-060, EV-CAR-278 |
| HLT-7.18 | Employers' transitional contribution, required (decided, protection 4 and `DEC-2026-11-10-11`) | From the date an employer's workers or their children move until the financing settlement's payroll contribution takes effect, the employer pays the fund a set share of what it paid toward premiums for that coverage in a base year (2030), indexed to the plan's per-person cost growth; paid with payroll tax deposits; an employer that offered no coverage pays nothing; the share is the financing settlement's (working figure: about 65%, the share at which employer moves cost the federal budget nothing on the coverage model; project arithmetic) | Treasury (IRS); Labor | EV-CAR-111, EV-CAR-295, EV-CAR-296, EV-CAR-299 |

### Title VI: administration (HLT-7.19 to HLT-7.21)

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| HLT-7.19 | The administering agency (decided in substance by memo 1 B: an expansion of Medicare) | CMS runs the plan, with Medicare's contractors and claims systems; its staffing, regional structure and the readiness reports are in section 5 | HHS (CMS) | EV-CAR-310, EV-CAR-311, EV-CAR-312, EV-CAR-313 |
| HLT-7.20 | A Beneficiary Ombudsman (adopted from the S. 1506 comparison) | Extends Medicare's existing Beneficiary Ombudsman to every enrollee: handles complaints and appeals and reports yearly; may not advocate for higher payments (S. 1506 title IV) | HHS | EV-CAR-280 |
| HLT-7.21 | An Office of Health Equity, an Office of Primary Health Care and a data firewall (adopted from the S. 1506 comparison) | Both offices as in S. 1506 secs. 616-617, the primary-care office setting national goals within a year; plan and equity data may not be used for any law enforcement or immigration purpose (its immigration side goes to the immigration flagship with point 3) | HHS | EV-CAR-286 |

### Title VII: the fund, private coverage, ownership and the federal systems (HLT-7.22 to HLT-7.27)

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| HLT-7.22 | One trust fund with named streams (decided, memo 3 B, confirmed in `DEC-2026-11-10-11`; point 7) | Receives: Medicare's payroll tax and general revenue for Parts B and D (premiums end for each group as it moves); the federal Medicaid and CHIP money and premium-credit money the plan replaces; FEHB's employer share; **the revenue from ending the employer tax exclusion, counted only on former premiums that become taxable wages, never on premiums replaced by the employer contribution**; the states' payments (HLT-7.17); the employer contribution (HLT-7.18); new revenue from the financing settlement. The hospital insurance trust fund is kept whole until the endpoint, with Medicare savings credited to it first, then folds in | Treasury; HHS (CMS) | EV-CAR-052, EV-CAR-287 |
| HLT-7.23 | No duplicative private coverage from the endpoint; extras allowed (decided, `DEC-2026-11-10-12`) | From January 1, 2035 no one may sell or offer coverage that duplicates the plan's benefits, as in Canada and S. 1506 (secs. 107, 801-802), rather than parallel private insurance as in the UK and Australia; coverage of benefits the plan does not cover stays legal; COBRA ends then. Before then, private and employer coverage continue for groups not yet moved. Private firms may serve as the plan's claims contractors | HHS; Labor; Treasury | EV-CAR-275 |
| HLT-7.24 | The VA, TRICARE and the Indian Health Service continue, and the people they serve are also entitled to the plan (decided, `DEC-2026-11-10-11`) | Eligibility for VA care, TRICARE and the IHS is unchanged; their facilities are plan providers, and the plan pays IHS and tribal facilities at its rates for the plan's enrollees, as Medicaid and Medicare do now; no change to the IHS without consultation with tribal leaders (S. 1506 sec. 901(c)). **Open:** how the IHS is funded alongside the plan, including whether advance appropriations continue; whether TRICARE's purchased care folds into the plan (the House bill's choice) or continues | HHS (IHS, CMS); VA; Defense | EV-CAR-292, EV-CAR-315, EV-CAR-316, EV-CAR-348, EV-CAR-349, EV-CAR-350 |
| HLT-7.25 | Today's Medicare moves into the plan at the endpoint | Parts A, B and D, Advantage and Medigap end for covered services on January 1, 2035; enrollees get the plan's benefit and copay rules (HLT-7.05, 7.06); Part B and D premiums end then | HHS (CMS) | EV-CAR-288 |
| HLT-7.26 | FEHB folds in at the endpoint | Federal employees and retirees join the plan with the endpoint cohort; the federal government pays the employer contribution (HLT-7.18) for them like any employer | OPM; HHS | EV-CAR-315 |
| HLT-7.27 | Ownership stays as it is, with targeted guardrails (decided, `DEC-2026-11-10-12`) | No public takeover of hospitals or clinics. Guardrails: ownership transparency (every owner of a participating provider reported to CMS and published); limits on private-equity buyouts of hospitals, nursing homes and physician practices (working choice: prior notice and review of any such acquisition, with authority to block one that would reduce access or quality); regional review of large capital projects so new money goes where care is short (working choice: projects above a threshold set by rule). Not adopted: S. 1506's bar on profit from the plan's payments and its public capital budget for every hospital | HHS (CMS); FTC and Justice for acquisitions | EV-CAR-283, EV-CAR-284, EV-CAR-336, EV-CAR-340, EV-CAR-341 |

### Medicare before the endpoint (HLT-2)

People already on Medicare join the plan in 2035. Until then (`DEC-2026-11-10-11`, item 3):

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| HLT-2.01 | The legacy upgrades from 2031 (decided, `DEC-2026-11-10-11`) | A $5,000 yearly out-of-pocket cap in traditional Medicare and hearing and vision coverage from January 1, 2031; dental phased in from 2033; the plan's benefit replaces them in 2035 | HHS (CMS) | EV-CAR-137, EV-CAR-289; legacy `domain-health.md`, HLT-2 |
| HLT-2.02 | Guaranteed issue of Medigap, 2031-34 (adopted from the S. 1506 comparison) | Any Medicare enrollee may buy any Medigap plan at any time without medical underwriting (S. 1506 sec. 1005) | HHS (CMS); state insurance regulators | Evidence still needed (the bill's sec. 1005 is in SRC-3260; no entry yet) |
| HLT-2.03 | No 24-month wait for people on disability (adopted from the S. 1506 comparison) | From January 1, 2031, people awarded Social Security disability benefits are entitled to Medicare at once (S. 1506 sec. 1004) | SSA; HHS (CMS) | EV-CAR-342, EV-CAR-343, EV-CAR-344 (counts and cost are dated: about 1.8 million people were in the wait in 2007; no current count) |
| HLT-2.04 | Medicare at 60 (decided, memo 2 wave 1) | From January 1, 2031, people 60 to 64 are entitled to Medicare with the upgrades; those uninsured or in the individual market are enrolled in the plan instead; those with employer coverage may choose Medicare as primary, with their employer paying the transitional contribution (HLT-7.18) | HHS (CMS); SSA | EV-CAR-207, EV-CAR-208, EV-CAR-268 |

### Ending federal abortion funding limits (RTS-2)

Decided in `DEC-2026-11-10-11`, item 4: the plan covers abortion with no Hyde-type limit on the fund, and the plan ends the Hyde Amendment in general, with this dossier as its home.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| RTS-2.01 | No abortion funding limit on the plan's fund (decided) | The plan pays for abortion like any covered service, notwithstanding any appropriations limit (as S. 1506 sec. 701(b)(3) does for its fund) | HHS (CMS) | EV-CAR-276, EV-CAR-287 |
| RTS-2.02 | End the Hyde Amendment and the other federal abortion funding limits (decided) | Repeal the statutory limits (for Defense health care, 10 U.S.C. 1093; the statutory cross-reference that applies Hyde to the IHS; CHIP's own limits; the ACA's segregation rule, 42 U.S.C. 18023) and override the annual appropriations riders (the Labor-HHS Hyde sections 506 and 507, FEHB's sections 613 and 614, D.C.'s section 810, and the State-Foreign Operations limits) by a "notwithstanding" clause in the 2029 Act; the plan's appropriations acts carry none. Federal conscience laws are unchanged here (the rights dossier owns them with RTS-1) | HHS; OPM; Defense; VA; Justice | EV-CAR-330, EV-CAR-331, EV-CAR-332 (the riders as in the FY2024 act; re-check against the current act); 42 U.S.C. 18023 has no entry yet |

## What the decisions changed

- **The endpoint moved from 2037 to 2035** (`DEC-2026-11-10-11`), so memo 1's and memo 2's 2037 dates, and memo 1 B's Medicare at 50 in 2035, are superseded: everyone joins on January 1, 2035.
- **Employer groups move with Medicaid in wave 2, required**, not last (memo 2's wave 3) and not voluntarily (the S. 1506 note's option C).
- **Memo 3 B adds a named stream:** the revenue from ending the employer tax exclusion, counted only on premiums that become wages (HLT-7.22).
- **Today's Medicare enrollees get the legacy upgrades from 2031** (HLT-2.01), which `3-design.md` point 4 had applied only under memo 1 A.
- **Abortion is covered, and the Hyde Amendment ends** (HLT-7.05, RTS-2); memo 4 had been silent on it.
- **The federal systems continue alongside the plan** (HLT-7.24).
- **No duplicative coverage at the endpoint, and ownership kept with guardrails** (`DEC-2026-11-10-12`; HLT-7.23, 7.27), in place of S. 1506's profit bar and capital budget.

## Adopted from the S. 1506 comparison

The comparison's recommendations (`research-s1506-comparison.md`, part a), each adopted as it recommends, since each follows from a decision already made: the card without a Social Security number (HLT-7.02); all-in or all-out private contracting and no utilization bonuses (HLT-7.08); the ombudsman (HLT-7.20); the fallback drug price and a formulary (HLT-7.13); the equity and primary-care offices and the data firewall (HLT-7.21); Medigap guaranteed issue (HLT-2.02); no disability waiting period (HLT-2.03); non-discrimination with a private right of action (HLT-7.09). Worker help keeps its need-based design, with a wider cost range in section 6 (HLT-7.16). None needs Espen.

**Decided not to adopt** (`DEC-2026-11-10-12`): S. 1506's bar on profit from program payments (sec. 615) and its public capital budget for every hospital (sec. 611). Ownership guardrails (HLT-7.27) take their place.

**Left open, not adopted** (no decision turns on them now; `DEC-2026-11-10-07`):
- *A bar on using quality measures to set payment* (sec. 615(e)): alternatives are the bar or Medicare's current value programs; no choice in this design turns on it.
- *A national health budget* (sec. 601): the alternative section 8 names if spending growth beats its target.

## Design lens

Each requirement the plan adds, what it buys and what it costs in burden (`DEC-2026-11-09-13`):

| Requirement | Buys | Burden | Why kept |
| --- | --- | --- | --- |
| Copays above 200% of poverty (HLT-7.06) | Damps use where supply is tightest | A charge at some visits; an income line from tax records | Decided (memo 4 C). No one applies; no record means no copay |
| Wave dates by payer (HLT-7.03) | Each step can be built and staffed | For some years, people in the same income band are in different plans | Decided. Each wave uses records the government holds |
| Employer contribution (HLT-7.18) | Employer moves cost the federal budget little | One more payment on the payroll deposit | Decided. No new filing; non-offering firms pay nothing |
| State payment (HLT-7.17) | Keeps money states already spend | A yearly calculation for 50 states and D.C. | Decided. One formula, no per-person test |
| Transition fund conditions (HLT-7.15) | Keeps essential services open | A claim and a services report for hospitals that ask | For Espen; only hospitals that lose apply |
| Readiness reports (HLT-7.03) | Visible problems before each date | A report by HHS | Published counts, not gates |

## Shared rules kept in one place

| Rule | Owner | Health's working answer | Where it applies |
| --- | --- | --- | --- |
| 3. Immigrant eligibility | Immigration (flagship 6) | Every resident is entitled; lawfully present immigrants restored in 2029; people without status decided by the owner, on S. 1506's residency rule as the proposal | HLT-1.02, HLT-7.01, HLT-7.21 |
| 1 and 2. Income and phase-outs | Secure floor | The plan has no premium to phase out; copays use one income line | HLT-1.04 (2030 only), HLT-7.06 |
| 4. Income lines | Secure floor | 200% of the federal poverty guideline, from prior-year tax records | HLT-7.06 |
| 5. Who verifies | Democratic renewal | Records the government holds; residency by rule | HLT-7.02 |
| 7. Services that make housing work | **Care (owner)** | Unchanged until part B decides long-term care; Medicaid's home and community services continue (HLT-7.07) | HLT-7.07 |
| 8. Workforce | Immigration and work | Part D sizes the supply; the copays and rates are the design's levers meanwhile | HLT-7.06, HLT-7.10 |

## Consistency check

Every decided amount and date, and where it appears. Search the dossier for an old figure before changing one.

| Item | Value | Appears in |
| --- | --- | --- |
| Endpoint | January 1, 2035 | HLT-7.03, 7.14, 7.23, 7.25, 7.26; sections 5, 6; README; `3-design.md` and memos 1-2 status lines (via `DEC-2026-11-10-11`) |
| Wave 1 | January 1, 2031: uninsured, individual market, children under 19, Medicare at 60 | HLT-7.03, HLT-2.04; sections 5, 6 |
| Wave 2 | 2033-35, Medicaid and employer groups, a third each January (working choice) | HLT-7.03; sections 5, 6 |
| Hospital rate | 1.25 times Medicare in 2031 (all-payer average, project arithmetic) to about 1.15 in 2036 | HLT-7.10; section 6 |
| Copay line and cap | 200% of poverty; $1,000 a person (working figure) | HLT-7.06; section 6 |
| Employer contribution | About 65% of base-year employer premium contributions (working figure; settlement sets it) | HLT-7.18; section 6 |
| State payment | Half of own Medicaid spending for movers (working figure; range 0-80%) | HLT-7.17; section 6 |
| Medicare upgrades | $5,000 cap, hearing and vision 2031; dental from 2033 | HLT-2.01; section 6 |
| Advantage savings | 14%, about $76 billion in 2026 (MedPAC) | HLT-6.01; section 6 |
| USDA rural health | $3-5 billion a year lending; $200-500 million grants | HLT-8.01; section 6 |
| Hospital transition fund | $100 billion over FY2033-38 (range $50-150 billion), for Espen | HLT-7.15; section 6 |
| Net federal cost | About $25.7 trillion FY2030-39 on the model's path before the employer contribution (about $25.6 trillion with the items outside it; about $20.1 trillion with the contribution at 65%); about $4.7 trillion in FY2040 | Sections 4, 6; README |

## Evidence still needed

- The Hyde riders in the current (FY2026) appropriations acts, the IHS cross-reference's citation, and 42 U.S.C. 18023 (RTS-2.02; the entries use the FY2024 act).
- Hospital-level payer mix, rural and urban (Medicare cost reports; the Chartis Center), to size HLT-7.15 and to test the finding that the move redistributes more than it removes. No government source gives rural hospitals' commercial share.
- Children's share of Medicaid and CHIP spending (MACPAC), used in section 6 as an assumption.
- A current count of people in Medicare's disability waiting period and CBO's cost of ending it (the entries are from 2007-09).
- S. 1506's secs. 104 (non-discrimination), 1004 (waiting period) and 1005 (Medigap) as entries anchored in SRC-3260.
- Whether the trade-adjustment program was reauthorized after 2021 (HLT-7.16).
- Check EV-CAR-340 (CBO, 2022) and EV-CAR-342 (Commonwealth Fund, 2009) against the originals: their quotations came from search extracts, before the milestone review.
