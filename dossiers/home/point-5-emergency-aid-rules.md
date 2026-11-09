# Point 5: the rules for emergency rent help

Role: a note for Espen on point 5 of "Recommended without a memo" in `3-design.md` (delivery rules for emergency aid), worked out rule by rule. Status: approved by Espen as written, all eight rules and the five-line summary, on November 8, 2026 (Notion comment "All approved", 14:10 UTC, on the mirrored page; restated to the reviewer session at 14:35 UTC: "Point 5: yes, as written"). Rule 3's episode limits were amended on November 9 (`DEC-2026-11-09-16`, `-17`; see rule 3). These rules are now the working choice for section 4 to specify; the decisions-log entry follows in the batched housing-decisions PR with memos 3-8.

**What this note does and does not decide.** It recommends the rules any emergency rent program in the plan should carry. It does not choose the fund's size or vehicle, which stay with memo 6 (`memos/6-prevention.md`): the rules work under A ($85 billion one time), B ($40 billion one time) or C (a standing fund with a smaller start, recommended there). Where a rule matters more under one option, the note says so. It does not edit the memo or `3-design.md`.

**How to read the sources.** Tags in brackets point to the evidence register (`evidence.json`, `EV-HOU-`) or, for sources new to this note, to the library catalog (`SRC-`). Executive-branch sources carry the administration that produced them (`DEC-2026-10-30-01`). Treasury ran the last national program, Emergency Rental Assistance (ERA), under the Biden administration in 2021-22; the HUD-funded evaluation was published in 2026 under the second Trump administration; Treasury's inspector general sits inside the executive branch, so its reports carry the administration in office when they were issued. GAO and the Congressional Research Service (CRS) work for Congress and carry no administration label. "Judgment" marks this note's own reasoning.

**What each rule needs.** Each rule ends with one of three answers: **a law** (the authorizing statute must say it), **appropriations** (it costs money that must be provided), or **guidance only** (HUD or Treasury, whichever runs the program, can set it under a general grant of authority). In ERA, Congress wrote eligibility, payment limits and who gets paid into the statute; Treasury set self-attestation, proxies and fraud controls by guidance (CRS, 2023) [SRC-0304] [SRC-0991].

## The eight rules at a glance

| Rule | Recommendation in one line | Needs |
| --- | --- | --- |
| 1. Eligibility | Low-income renters (at or below 50% of area median income, or already enrolled in a means-tested program) facing a housing crisis now; no "caused by" test | Law |
| 2. Risk screen | Rank eligible applicants with a short, tested risk score; court cases go first | Law sets the principle; guidance sets the tool |
| 3. Payment caps | Back rent plus up to two months ahead, capped by local rent levels; an annual cap of four months' Fair Market Rent per household, usable across crises (amended November 9) | Law sets the cap; guidance the figure |
| 4. Self-attestation and sample checks | Let tenants state income and hardship; check identity and the landlord before paying; audit a random sample after | Guidance only, but write the permission into law so it lasts |
| 5. Landlord applications | Landlords may start applications with the tenant's consent; pay the landlord first, the tenant if the landlord won't take it; pay within 30 days | Law for who gets paid; guidance for the rest |
| 6. Payment-error measurement | Estimate the error rate from a random sample in year one and publish it yearly | Law and a small appropriation |
| 7. Grantee network | One administrator per place, states plus large localities, linked to courts and legal aid; money moves by need and performance | Law and appropriations |
| 8. Data standard | One payment-level record format for every grantee, with a duplicate check and links to court and shelter records | Law for the requirement and privacy; guidance for the format; a small appropriation |

## 1. Eligibility

**Recommendation.** Help renters with household income at or below 50% of area median income, or who are already enrolled in a means-tested program such as SNAP, Medicaid or SSI, and who face a housing crisis now: unpaid rent with a notice, an eviction filing, a utility shutoff, or displacement by a declared disaster. Drop ERA's test that the hardship be caused by a named event.

**Evidence.**
- ERA's statute set the line at 80% of area median income, plus a pandemic hardship and a risk of homelessness, and told grantees to put households at or below 50% first (CRS, 2023) [SRC-0304]. In practice most of the 5.35 million households helped were at or below 30% (CRS, 2023) [EV-HOU-150], so a 50% line would have excluded few of the people ERA actually reached (judgment from those figures).
- Treasury let grantees accept income already verified by another means-tested program ("categorical eligibility") or a self-attestation backed by neighborhood income data (Treasury FAQs, Biden administration, 2021-22) [SRC-0991]. Administrators and researchers credit these shortcuts with faster take-up (Urban Institute, 2025) [SRC-1066].
- Targeting decides value. In Chicago, aid cost about $10,300 per case of homelessness averted, and the authors expect much less with tighter targeting on lower-income callers (Evans, Sullivan and Wallskog, 2016) [EV-HOU-108].
- A disaster trigger matters because the ROAD to Housing Act's disaster recovery grants end in July 2029 (CRS, 2026) [EV-HOU-228], the question `3-design.md` leaves to section 4.

**Main alternative: keep ERA's 80% line.** It reaches more households, but mostly households further from losing their homes, and administrators already tended to aim too far upstream (Aiken and others, *Housing Policy Debate*, 2022) [SRC-1064]. With a fixed sum, a wider door means less for those at the edge.

**Needs: a law.** Eligibility was statutory in ERA and should be again; guidance can list the accepted documents and enrolled programs.

## 2. Risk screen

**Recommendation.** Among eligible applicants, put first those most likely to lose their homes, using a short points-based screen that each grantee tests on its own records, and fast-track anyone with an eviction case or court date. Publish the screen.

**Evidence.**
- In New York City, a 15-question screen built from Homebase records beat caseworkers' judgment: serving the same number of families, it would have reached 26% more of those who later entered shelter and cut misses by almost two-thirds (Shinn and others, *American Journal of Public Health*, 2013) [SRC-1065]. Even so, most families the screen rates high-risk do not enter shelter, so a screen improves aim without making it precise (same source).
- Prevention's effect shrinks at scale: Homebase cut family shelter entries by 5% to 11% citywide (Goodman, Messeri and O'Flaherty, 2016) [EV-HOU-111], much less than in its trial [EV-HOU-110].
- ERA reached the right neighborhoods on the whole: more money per renter went to tracts with more evictions before the pandemic (Treasury Office of Economic Policy working paper, Biden administration, 2024) [SRC-0992]; an independent team using the same payment data agrees (Hepburn and others, Eviction Lab, *Journal of Urban Affairs*, 2026) [SRC-1063]. But the highest-risk quarter of neighborhoods got less than its share of need (HUD-funded evaluation, published under the second Trump administration, 2026, chapter 3) [SRC-0397].
- Lotteries in five programs found aid raised rent payment but did little to keep people from moving (Collinson and others, NBER, 2025) [EV-HOU-153], consistent with much of the aid going to households who would have stayed anyway.
- In Milwaukee, only about 37% of ERA applicants who answered the question had received an eviction notice (Stout, 2023, for the program's funder) [SRC-1067].

**Main alternative: first come, first served** (common in ERA). It is simple and seems fair, but it rewards the best-informed and quickest applicants, not those at most risk. Requiring an eviction filing before help is the other alternative; it comes too late for informal evictions, which unfunded households in Philadelphia and Los Angeles reported more often (HUD-funded evaluation, 2026) [SRC-0397].

**Needs: a law for the principle, guidance for the tool.** The statute should require grantees to rank by risk with a tested screen; HUD or Treasury publishes a model screen and approves local versions. Testing it fits in the administrative allowance (rule 7).

## 3. Payment caps

**Recommendation.** Pay back rent and utilities owed plus up to two months of future rent, a deposit or moving costs, capped at a multiple of the area's Fair Market Rent (for example, four months' worth); one episode per household in 12 months, two in three years. Legal help and services are paid separately and do not count against the cap.

**Amended November 9, 2026** (`DEC-2026-11-09-16`, `DEC-2026-11-09-17`). The episode limits give way to an annual cap of four months of the area's Fair Market Rent per household in any 12 months, usable across any number of crises. A second crisis within 12 months prompts a referral to long-term help. The local or state administrator tracks use, with income verified through tax data where that is possible and easy, and HUD publishes the share of payments going to repeat users, with a review trigger rather than an automatic cutoff. Section 4 writes the amended rule (HOU-1D.01).

**Evidence.**
- Short, small help is what worked in the trials: about $2,000 a household in Santa Clara County (MIT Press Reader on Phillips and Sullivan, 2023) [EV-HOU-109], one-time payments in Chicago [EV-HOU-108].
- What people owe is in that range: the median Milwaukee ERA applicant owed about $2,000 in back rent from May 2021 to May 2022, falling to about $1,600 by late 2022 (Stout, 2023) [SRC-1067].
- ERA allowed up to 12 months plus 3, and then 18 months across both rounds, with future rent paid three months at a time (CRS, 2023) [SRC-0304]. Long help turns emergency aid into a short-lived voucher, and the lottery studies found little effect on stability [EV-HOU-153].

**Main alternative: ERA's 18 months.** It helps a few households for a long time; the plan's rental guarantee (memo 2) is the tool for lasting help. Under memo 6's C, a long cap would drain a standing fund in the first downturn (judgment). Under A or B, the one-time money would go further but to fewer people.

**Needs: a law for the cap's form, guidance for the figure.** ERA's limits were statutory; the statute should set the form (episode length, frequency, tie to Fair Market Rent) and let HUD or Treasury set and index the multiple.

## 4. Self-attestation and sample checks

**Recommendation.** Let tenants state their income and hardship in writing when documents are not at hand; before paying, check identity, the tenancy and the landlord's ownership against public and agency records; after paying, audit a random sample, with documents requested only then.

**Evidence.**
- ERA spending doubled in June 2021, the month after Treasury allowed self-attestation (CRS, 2023) [EV-HOU-150]. Programs that let tenants self-attest their tenancy distributed more of their money (Aiken and others, 2022) [SRC-1064].
- GAO found that self-attestation raises the risk of payments to ineligible households, and that Treasury had not checked whether grantees ran the controls it required (GAO, February 2022) [SRC-1060]; it also recommended post-payment reviews, which Treasury had not designed (GAO, January 2022) [SRC-0990].
- State housing agencies, which ran the programs and have a stake in the finding, reported that pre-payment identity checks using tax records and sample reviews after payment stopped many attempted scams (National Council of State Housing Agencies, 2022) [SRC-1069].
- **Where the fraud was.** In the inspector general's questioned-cost findings, the bad payments came from fabricated leases and false landlords, not from tenants misstating income: a fabricated lease, false landlord and a fake ownership record in Michigan (Treasury inspector general, August 2024, Biden administration) [SRC-0995]; one person posing as both landlord and tenant in Virginia (October 2026, second Trump administration) [SRC-0993]; and in Florida, invalid lease or landlord documents or payment to the wrong landlord, "not self-attestations for eligibility" (October 2026, second Trump administration) [SRC-0994]. These are case findings, not a sample, so they show where controls failed, not how often (judgment).

**Main alternative: full documents up front.** It catches some errors before payment, but it is what made ERA slow (about 6% of the first round spent by May 2021 [EV-HOU-150]) and it screens out the households with the least paperwork, often those at most risk [SRC-1064]. The case findings suggest the cheaper check is on the landlord and the property, not the tenant's pay stubs.

**Needs: guidance only.** Treasury set all of this by guidance in ERA [SRC-0991]. Because a later administration could reverse it by the same route, the statute should state that self-attestation is allowed and that sample checks are required (judgment).

## 5. Landlord applications

**Recommendation.** Let landlords start an application, with the tenant's signed consent and notice to the tenant; pay the landlord first and the tenant directly if the landlord refuses or does not answer within 10 days; require the landlord to drop the nonpayment case and not evict for nonpayment for the months paid; and pay within 30 days of a complete application.

**Evidence.**
- Landlord-initiated applications were 30 percentage points more likely to succeed (HUD-funded evaluation, published under the second Trump administration, 2026) [EV-HOU-152]. No independent study yet confirms this, so it rests on that evaluation and judgment.
- ERA's first law paid landlords first and tenants if landlords would not take the money; Treasury's guidance let landlords apply with tenant signatures and notice, and barred eviction for nonpayment during paid months (CRS, 2023) [SRC-0304].
- Landlords in Milwaukee said they would accept aid from a standing source only if it arrived within two to three weeks of an application (Stout, 2023) [SRC-1067]. Administrators and providers recommend paying the landlord directly unless there is a reason not to, and not tying aid to long rent freezes, which kept some landlords out (Urban Institute, 2025) [SRC-1066].
- The fraud cases in rule 4 are why the landlord's ownership is checked before payment [SRC-0995] [SRC-0993].

**Main alternative: tenant-only applications, paid to tenants.** It protects tenants with adversarial landlords, which the fallback already does, but it loses the landlord channel that reaches tenants who would never apply, and arrears paid to tenants may not reach the landlord before the court date (judgment). Long eviction freezes as a condition are the other alternative; they deter landlords [SRC-1066].

**Needs: a law for who gets paid; guidance for the rest.** The payee order and the no-eviction condition were statutory or tied to it in ERA; the consent form, the waiting period and the payment deadline can be guidance, though a payment deadline in law would bind grantees more firmly (judgment).

## 6. Payment-error measurement

**Recommendation.** From the first year, the agency running the program estimates improper and unknown payments from a random sample of grantee payments, publishes the rate each year with a target, and recovers errors from grantees without evicting tenants over honest mistakes.

**Evidence.**
- The general law already applies: the Payment Integrity Information Act requires an estimate for a program likely to exceed 1.5% and $10 million, or $100 million, in improper payments (Treasury inspector general, 2024, Biden administration) [SRC-0315].
- ERA was never measured. Treasury told OMB in August 2022 that it would not estimate improper payments for short-term pandemic programs, and only its FY2024 risk assessment found ERA susceptible (Treasury inspector general, 2025, second Trump administration) [EV-HOU-182]. Its FY2023 assessment had wrongly found ERA not susceptible (Treasury inspector general, 2024) [EV-HOU-154].
- GAO found Treasury's early risk assessment looked only at allocations to grantees, not at grantees' payments to households, and that 2% of households in the first round were paid by more than one grantee (GAO, December 2022) [SRC-1061]. Treasury finished a quantitative risk assessment only in September 2024, under the Biden administration (same source, status update).
- Measurement gaps are not unique to Treasury: in FY2024, HUD's tenant-based rental assistance was among programs judged susceptible that reported no estimate (GAO, 2025) [SRC-1062].

**Main alternative: rely on the general law as it stands.** It lets a new program wait through risk-assessment cycles and argue it is short-term, which is how ERA went unmeasured; under memo 6's A or B the money would be spent before the first estimate (judgment).

**Needs: a law and a small appropriation.** The statute should require a first-year sample estimate and set aside federal administrative money for it; OMB guidance could require it too, but did not last time.

## 7. Grantee network

**Recommendation.** One administrator per place: every state, plus cities and counties above a population floor (ERA's first round used 200,000 people) that choose to run their own program, with no overlapping programs in one place; each grantee must link to the eviction court, legal aid and the local 211 line; money is allocated by a need formula and moved from slow to fast grantees on published performance measures.

**Evidence.**
- ERA had about 740 grantees, including all states, 382 local governments and tribes (Housing Initiative at Penn, 2021) [SRC-1068], many with no program before; more than $3.1 billion of first-round money was taken from slow grantees and given to others (CRS, 2023) [EV-HOU-150].
- Allocations did not match need; reallocation was "an incomplete and inefficient fix"; overlapping state and local programs needed rules to prevent duplication (Urban Institute, 2025) [SRC-1066]. Overlap is how 2% of households came to be paid twice [SRC-1061].
- ERA's first round paid states and local governments serving at least 200,000 people directly (CRS, 2023) [SRC-0304].
- Landlords and their lawyers in Milwaukee called sustained, efficient rental aid an essential complement to pre-filing diversion, mediation and tenants' legal help, and complained of slow payment and no news on applications (Stout, 2023, for the right-to-counsel program's funder) [SRC-1067]. The link to courts and legal aid rests on that and on judgment.

**Main alternative: one federal portal run from Washington.** It would standardize everything, but it has no tie to local courts and landlords, and no federal agency has run household-level rent payments at this scale (judgment). ERA's open, overlapping set of grantees is the other alternative; it is what produced the duplication and the reallocation scramble.

**Needs: a law and appropriations.** Who receives grants and how money is allocated are statutory; the performance measures can be guidance. Under memo 6's C, a standing network is the point: it is built once, not again in each crisis.

## 8. Data standard

**Recommendation.** Every grantee reports every payment monthly in one federal format: a protected household identifier, address and census tract, amounts and months covered, payee, income band, risk score, how eligibility was established, and dates of application and payment. The agency runs a duplicate check across grantees, and records can be linked, under privacy rules, to eviction-court and shelter data for evaluation.

**Evidence.**
- Treasury was missing data on 26% of 2021 payments, mostly because grantees did not report, although the statute required six performance measures quarterly; complete closeout data arrived only in 2025 (GAO, December 2022, with 2025 status) [SRC-1061].
- The 2% double payments [SRC-1061] are what a common identifier and cross-grantee check would catch.
- Where payment-level data existed, it allowed the targeting studies in rule 2 [SRC-0992] [SRC-1063]; administrators call for standardized systems that draw on existing data to speed take-up and reduce fraud (Urban Institute, 2025) [SRC-1066].
- ERA's first law already required grantees to protect the data they collect (Treasury FAQs) [SRC-0991].

**Main alternative: quarterly totals by grantee (ERA's performance measures).** They tell Congress how much was spent but cannot catch duplicates, measure errors (rule 6) or show who was helped and whether they stayed housed (judgment).

**Needs: a law for the requirement and privacy, guidance for the format, and a small appropriation** for the reporting system and grantees' costs.

## How the rules fit memo 6's options

- **Under A or B (one-time money):** rules 4, 5 and 7 decide how fast money moves; rule 6 must start before most of it is spent. The lesson of 2021 is that rules written after launch arrive too late (Urban Institute, 2025) [SRC-1066].
- **Under C (standing fund):** rules 2, 3 and 8 matter most, because a permanent fund lives or dies on aiming small payments well and showing that it works.
- **Not in this note:** the fund's size, which agency runs it, the vehicle (reconciliation or a regular bill), and whether legal help is a federal right; memo 6 and point 4 cover those.

## Summary for Espen (approve or amend)

1. Eligibility and risk: help renters at or below 50% of area income (or already on SNAP, Medicaid or SSI) who face a housing crisis now, ranked by a short tested risk screen, court cases first (law).
2. Payments: back rent plus up to two months ahead, capped by local rents, at most four months' Fair Market Rent per household in 12 months across any number of crises (amended November 9); legal help paid separately (law, with the figure by guidance).
3. Checks: tenants may state income and hardship; identity, tenancy and the landlord's ownership checked before paying; a random sample audited after (guidance, written into law so it lasts).
4. Landlords: may apply with tenant consent; paid first, tenants paid if they refuse; no eviction for paid months; payment within 30 days (law for the payee order, guidance for the rest).
5. Accountability: error rate measured from year one and published; one administrator per place with a need-and-performance formula; one payment-level data standard with a duplicate check (law and small appropriations).
