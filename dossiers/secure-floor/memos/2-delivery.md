# Memo 2: How the floor reaches people

Role: decision memo for Espen, fork 3 of the secure floor (`../README.md`, "Forks for S3"; `../3-design.md`). This is the fork your November 11 direction asked for: how government delivers, not how much it pays. Status: **decided** (`DEC-2026-11-12-06`): **B**, as recommended. Specified in `../4-specification.md` (FAM-1.07 to 1.10) and `../5-delivery.md`. Sources are named in plain text; bracketed tags point to `../evidence.json`. Costs marked "judgment" are working assumptions.

**Decision line.** Recommended: **B, automatic payment from records the government already holds: the IRS pays the child benefit monthly, starting from birth and benefit records rather than a claim, with one shared payment rail and notice for the Climate Dividend and SSA and rural USDA offices as front doors.** Cost: about **$1-2 billion a year to build and run (judgment), plus about $10-20 billion a year of benefits to children a filing-based design misses (judgment)**, inside memo 1's range at full delivery. Evidence: randomized trials on take-up; the 2021 credit's delivery record; Canada's practice.

**This memo decides how the child benefit, and the floor's other new payments, reach families.** It applies under any of memo 1's options.

## The question

The legacy design pays the child benefit as a refundable tax credit, in monthly advances from the last tax return, through the IRS (`legacy/domains/domain-family.md`, FAM-1) [EV-SEC-690]. That works for families who file. The question is what the government does for the rest, and whether the floor should run on one front door and one income test or on each program's own.

## Why it matters

- **Filing decides reach.** In 2021 the IRS paid families of about 61 million children, nearly 9 in 10 by automatic deposit, because it paid from returns it already held (Treasury and IRS, 2021) [EV-SEC-107] [EV-SEC-108]. The children it missed were the poorest: estimates ran from 4 million to 7 million (Economic Security Project's roundup of CBPP and People's Policy Project estimates, 2022; advocacy estimates) [EV-SEC-058] [EV-SEC-110].
- **About 14% of people who could be on a return are not**, mostly in low-income households (CBO, via CRS) [EV-SEC-060].
- **The free filing tool is gone.** IRS Direct File will not be offered in 2026 (IRS, 2025) [EV-SEC-063].
- **SSA has lost about one worker in nine** (SSA inspector general, 2026) [EV-SEC-066], and closing a field office cut disability recipients nearby by 16% (Deshpande and Li; quasi-experimental) [EV-SEC-106].

## What the evidence says, in five lines

1. **Defaults beat outreach** (review of US and UK research): take-up rises with automatic or default enrollment and falls with administrative barriers (Currie, 2004) [EV-SEC-101]. Removing automatic enrollment cut enrollment in Massachusetts's subsidized coverage by a third (Shepard and Wagner; quasi-experimental) [EV-CAR-206].
2. **Outreach helps but misses the neediest** (randomized): in a SNAP trial, information and help raised enrollment from 6% to 18%, but brought in people with smaller benefits than the average enrollee (Finkelstein and Notowidigdo, 2019) [EV-SEC-103] [EV-SEC-104].
3. **Paperwork removes eligible people** (administrative data): most people dropped in the Medicaid unwinding lost coverage for procedural reasons (KFF, 2024) [EV-CAR-210].
4. **Records already held can find missing children** (government analysis): Treasury found 2.3 million children with health insurance who do not appear on tax returns (via CBPP, 2021) [EV-SEC-110] [EV-SEC-061].
5. **Canada starts at birth** (international practice): parents can claim the child benefit when they register the birth, with the province passing proof of birth to the tax agency [EV-SEC-113], and the agency invites low-income non-filers to file by phone [EV-SEC-114].

## Options

**A. The legacy design: monthly advances from the last return, with a non-filer sign-up.**
- **What it does.** The IRS pays from the latest return; families who do not file use a sign-up portal, as in 2021 [EV-SEC-109].
- *For people:* a filing family is paid without doing anything. A grandmother raising two children who has no filing requirement must find and complete the portal.
- *Reach:* about 9 in 10 families, as in 2021 [EV-SEC-108]. By October 2022, 4.1 million recipients had not filed the return that reconciles the advance (TIGTA, 2022) [EV-SEC-059].
- *Cost:* the IRS build that 2021 used, scaled up; little more.
- *Burden:* falls on non-filers, the poorest.

**B. Automatic payment from records the government holds, paid by the IRS (recommended).**
- **What it does.**
  - *Starting point.* A child is enrolled from the records that already show them: birth registration and the Social Security number issued at birth, the last tax return, and SSA, SNAP, Medicaid and SSI records. No claim is needed. The parent the child lives with gets a notice that confirms what the records show, and corrects it if they are wrong (memo 1, point 3).
  - *Payment.* Monthly, by deposit or prepaid card, under Treasury's permanent appropriation for refundable credits, so it continues through a lapse in appropriations (`legacy/domains/domain-family.md`, FAM-1, drafting note) [EV-SEC-690].
  - *One reconciliation a year,* with no repayment for families below a set income (a safe harbor; point 4).
  - *One rail.* The Climate Dividend, when the clean power dossier designs it, uses the same payment rail, notice and address records [EV-SEC-699]; so can paid leave's and the floor's other payments where they suit.
  - *Front doors.* Anyone can confirm, correct or start a payment at an SSA field office, a rural USDA Rural Development office (`DEC-2026-11-10-02`), a tax-help site, by phone or online.
- *Where tried:* Canada's registration at birth [EV-SEC-113]; the 2021 IRS non-filer matching [EV-SEC-061]; Social Security's own enrollment, which costs under 1% of benefits to run (SSA Trustees) [EV-SEC-115].
- *For people:* the grandmother gets a letter saying what she will be paid and asking her to confirm she cares for the children. A baby born in March is paid from April.
- *Reach:* close to every child with a record. The 2.3 million children found through health coverage records are the measure of the gain [EV-SEC-110].
- *Cost:* about $1-2 billion a year for the IRS and SSA to build and run the matching and front doors (judgment; capacity is CAP-7's in the legacy plan). The larger cost is the benefit itself: reaching perhaps 2-4 million more children at $4,000-5,000 each adds about $10-20 billion a year (judgment). Memo 1's high end assumes full delivery.
- *Political risk:* data sharing between agencies raises privacy objections. The answer is narrow statutory uses, as Canada's consent at birth registration shows.
- *Burden:* a notice to confirm, not an application.

**C. SSA pays the child benefit, outside the tax code.**
- **What it does.** SSA pays a monthly benefit, as Romney's Family Security Act proposed [EV-SEC-273].
- *Why consider it:* SSA is trusted across parties (Pew, 2025) [EV-SEC-116], more than the IRS (37% favorable; Pew, 2026) [EV-SEC-117], and pays about 71.6 million people monthly [EV-SEC-417].
- *Costs and risks:*
  - A payment outside the tax code counts as income for rent, SNAP and SSI unless a new statute excludes it; a refundable credit is excluded by section 6409 already [EV-SEC-534].
  - It would need its own appropriation or trust fund to keep paying through a shutdown.
  - SSA is short of staff [EV-SEC-066], and memo 5 already gives it paid leave.

**D. One front door and one income test for every floor benefit, run by one agency.**
- **What it does.** The child benefit, SNAP, housing help and child care merge into one application with one income test, as the UK's Universal Credit merged six benefits [EV-SEC-555].
- *Why not:* the UK's National Audit Office found Universal Credit not yet value for money and its rollout troubled [EV-SEC-556]. Programs owned by other dossiers (housing, care) would have to be rebuilt.
- *What to take from it:* one income finding reused across programs (memo 7, part 2), which HUD and Medicaid can already do [EV-SEC-510] [EV-SEC-562].

## Against the bills and programs

| Bill or program | How it delivers | Match or diverge with B, and why |
| --- | --- | --- |
| **ARPA advance credit**, 2021 [EV-SEC-109] | IRS, from returns, plus a non-filer tool | **Diverge:** that is A; B adds records beyond returns |
| **American Family Act**, 2025 [EV-SEC-262] | Monthly advance through the IRS | **Match** on agency and timing; the bill's text does not set records-based enrollment |
| **Family Security Act** (Romney, 2021) [EV-SEC-273] | SSA | **Diverge:** that is C |
| **Canada Child Benefit** [EV-SEC-113] [EV-SEC-236] | Tax agency, claimed at birth registration, paid on the prior year's return | **Match** in method; B goes further by enrolling without a claim |
| **Legacy Climate Dividend** (CLI-2) [EV-SEC-699] | IRS to filers, SSA and VA from their records, a non-filer sign-up | **Match:** the same rail; B extends it to the child benefit |
| **Universal Credit** (UK) [EV-SEC-555] [EV-SEC-556] | One benefit, one agency | **Diverge:** that is D |

## Consequences at a glance

| | A. Returns plus a portal | **B. Records, automatic** | C. SSA pays | D. One merged benefit |
| --- | --- | --- | --- | --- |
| Children reached | About 9 in 10 families | Nearly all with a record | Similar to B if SSA has the records | Unknown; long rollout |
| What a non-filer does | Finds and fills in a portal | Confirms a notice | Applies at SSA | Applies once |
| Counts for rent and SNAP | No (section 6409) | No (section 6409) | Yes, unless a new law excludes it | Program by program |
| Pays through a shutdown | Yes | Yes | Only with new authority | Unclear |
| Build cost | Low | About $1-2 billion a year | New SSA system | Very large |
| Risk | Misses the poorest | Privacy and data-matching | Staffing; income counting | Universal Credit's |

## Recommendation: B

- **It reaches the children the 2021 credit missed** without asking the poorest families to find a portal. The trials show defaults reach people outreach does not [EV-SEC-101] [EV-SEC-104].
- **It keeps the tax code's protections.** The benefit stays a refundable credit, so it never raises rent or cuts SNAP [EV-SEC-534], and it pays through a shutdown.
- **It builds one rail, not one agency.** The Climate Dividend and the child benefit share payment records, notices and front doors, so a family sees one government, without merging programs other dossiers own.
- **It follows the design lens** (`DEC-2026-11-09-13`): records the government already holds, self-attestation and one notice, where today a family must file.
- **What it costs in burden:** a notice to read and confirm. What it buys: reach to the poorest children.

**What would change this:** a privacy ruling or law that bars the data matching (toward A with stronger outreach); evidence that SSA's capacity recovers enough to run the child benefit (C would then be reasonable, with an income exclusion).

## If you decide

- **Under B:** section 4 writes the enrollment-from-records rule, the data-sharing authorities and their limits, the safe harbor and the shared rail into the child benefit's statute; section 5 (delivery) states the IRS's and SSA's build and staffing, for shared rule 5's owner (democratic renewal). The clean power dossier is told the dividend's rail is set here.
- **Preparation before 2029:** Treasury's matching of children in health coverage records to returns, repeated on 2027 data, and a Direct File replacement for simple returns.
- **Under A, C or D:** as described above.
