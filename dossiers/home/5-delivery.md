# A home you can keep: delivery

Role: section 5 of the housing dossier. It says who runs each provision in `4-specification.md` and `provisions.json`, whether they can, what fixes their capacity, the timeline from 2029 to 2038 matched to the vehicles, how the one rental help system works on the ground, how states, cities and tribes take part, the remedies tenants have, the fraud controls, and what the statute must say so that delivery does not depend on a willing agency. Status: draft (stage C, step 5), on top of section 4 (PR #136, not yet merged). It changes no provision; where delivery argues for a change, it says so and leaves the change to the section 4 owner or to Espen. Choices that are Espen's are listed at the end and in the README as questions, not decided here.

## How to read this section

- **Evidence.** Tags in brackets point to `evidence.json`. Entries new to this section are EV-HOU-340 to 352. Executive-branch sources carry the administration that produced them (`DEC-2026-10-30-01`). GAO and CRS work for Congress. "Judgment" marks this section's own reasoning.
- **The skepticism rule applied to delivery.** The same rule that discounts an administration's analysis applies to its willingness to carry out a law. The plan starts under a friendly administration in 2029, but the guarantee becomes a right in 2037 and stage 3 opens in 2038, two presidential terms later. So every provision is written to run under an agency that is slow, thin or hostile. Section 8 of this file lists what the statute must say for that.
- **The calendar.** Dates for the vehicles come from the scenario calendar (`models/data/calendar-scenarios.json`, 146 runs). It is a research prototype with illustrative inputs, not a forecast, so this section uses its ranges, not its points.

## 1. Who runs each provision

| Provision | Federal lead | Delivers on the ground | Partners | Main capacity question |
| --- | --- | --- | --- | --- |
| HOU-4.01 shared rules | HUD | Housing agencies; HOU-1D grantees | HHS (Medicaid, TANF), USDA (SNAP), SSA, IRS (income data) | Data agreements (section 4 below) |
| HOU-4.02 one rental help system; HOU-4.03 order of reach | HUD | Housing agencies, HOU-1D grantees, Continuums of Care (coordinated entry) | Eviction courts, legal aid, 211 lines | One application and one record across hundreds of local bodies |
| HOU-4A.01, 4A.02 new awards; HOU-4D.01 stage 2; HOU-4.08 stage 3 | HUD (Public and Indian Housing) | Housing agencies | CoCs for stage 1; state Medicaid agencies for stage 3 services | Housing agency staff and lease-up (2.2) |
| HOU-4.04 attached awards; HOU-4.05 neighborhood payment limits | HUD | Housing agencies | State housing finance agencies (the homes attached help goes to) | Project-based caps and choice mobility in current law (2.2) |
| HOU-4.06 source-of-income protection | HUD (Fair Housing and Equal Opportunity); Justice Department | Fair housing groups; state and local fair housing agencies; courts | — | HUD's fair housing staff (2.1, 6.1) |
| HOU-4.07 search help | HUD | Housing agencies, or a regional nonprofit where agencies are small | Landlord groups | Search counselors (2.3) |
| HOU-1D.01 to .04 emergency fund | HUD (section 4's choice, HOU-4.02) | One grantee per place: states, and cities and counties of 200,000 or more that opt in | Courts, legal aid, 211 | A network built from scratch in 2030 (2.5) |
| HOU-4.09 to 4.12 Housing First, recovery housing, supportive housing | HUD (CoC and ESG programs), VA (HUD-VASH), HHS (SAMHSA; CMS for Medicaid) | CoCs and nonprofit providers; state Medicaid agencies | Care flagship (HLT-1, HLT-4) | The services workforce (2.6) |
| HOU-3C.01 state revolving funds | HUD | State housing finance agencies (or a state's designated fund) | Localities; nonprofit and tax-credit developers | State readiness (2.4) |
| HOU-3C.02 construction loans | HUD, with the Federal Financing Bank (Treasury) | State agencies originate and service under a risk-share | CBO (subsidy rate) | A new HUD lending office (2.4) |
| HOU-3C.03 conditions on plan-financed homes | HUD | State agencies and owners (recorded restrictions) | Care flagship (accessible-unit share) | Monitoring for decades |
| HOU-5.01, 5.02 public housing repair and right to return | HUD | Housing agencies | Residents' councils | Enforcement record (6.2) |
| HOU-6.01, 6.02 zoning reward and transportation condition | HUD (Innovation Fund); DOT (Moving America) | States, regions, localities | — | A production count that cannot be gamed |
| HOU-8.01 social housing pilot; HOU-9A.01 small builder | HUD; the new corporation | Public and nonprofit owners; the corporation | GSA and other land-holding agencies | A new corporation's start-up |
| HOU-2.01 tax credits | Treasury (IRS) | State allocating agencies | — | Open with Espen's decision |

**One federal lead for rental help.** Section 4 put the emergency fund at HUD so one agency holds the application, the record and the income findings. Delivery confirms the choice on two grounds and qualifies it on one. For it: housing agencies already verify income with federal matching data (shared rule 5), and one agency is what makes one record possible. Against it: HUD lost about 29% of its staff in 2025 (GAO, 2026) [EV-HOU-340], while Treasury has run the only national household rent program. The answer is not to move the fund but to write it so it runs with a thin HUD: formula money that flows to grantees by statute, a shared data system built and staffed with its own money, and default rules where HUD misses a deadline (section 8). The Treasury alternative stays available if the 2029 rebuild fails; this section does not reopen it (judgment).

## 2. Capacity, and the fixes

### 2.1 HUD itself

**What the record shows.** HUD's workforce fell from about 8,800 to about 6,300 between December 2024 and December 2025; over half of those who left had at least ten years at HUD, 41% more than twenty; HUD hired 193 people in 2025 (GAO, 2026) [EV-HOU-340]. The same report records stakeholders' accounts of slower answers and of a housing agency locked out of HUD's payment system for three months [SRC-1440]. The ROAD to Housing Act gave HUD about 38 new duties with no money for staff (`road-act.md`, "HUD's load").

**Fixes.**
1. **Staff for the plan's programs, paid with the programs.** HOU-4A.02 and HOU-1D.03 already carry administration money for housing agencies and grantees. The statute should also set aside a share of each new mandatory program for federal administration, systems and evaluation, available until spent, so the plan's programs do not wait on the yearly HUD salaries account (judgment). The agency rebuild lines (CAP-7S, CAP-7) cover HUD's base; this covers what the plan adds.
2. **Hiring authority for 2029.** Direct-hire authority for HUD's rental assistance, data and lending offices in 2029-31, and authority to bring back former staff without pay penalties. This is executive action in 2029 where OPM allows it, and the regular bill where it needs law (judgment).
3. **A delivery office.** A small HUD office for the one rental help system, reporting monthly on applications, awards, leases and payments by place, with a technology team on the model the federal digital service units use (judgment). Its reports are public by statute.
4. **Build what HUD would have to build anyway, once.** The data standard, the application and the duplicate check (section 4 below) are one system, not three.

### 2.2 Housing agencies: staff and lease-up

**What the record shows.**
- Housing agencies are paid a fee per leased voucher, and Congress funds less than the formula: HUD estimated calendar-2026 fees at 85% proration (HUD notice, second Trump administration, 2026) [EV-HOU-343]. Agencies run the program on the fee, so short fees mean fewer caseworkers and inspectors.
- In ordinary times, 61% of new voucher holders leased within six months, less in tight markets (Furman Center study, 2024) [EV-HOU-092].
- Emergency Housing Vouchers (EHV) are the closest precedent: 70,000 vouchers with mandatory money and extra fees for services and landlord incentives [EV-HOU-188]. A year in, 87% were leased or issued, and issuance to lease averaged 77 days (USICH, Biden administration, 2022) [EV-HOU-344]. By February 2023, 67% were leased; 129 of 610 agencies had leased less than half, and only 62 had leased all of theirs (Terner Center, 2023) [EV-HOU-345]. More than 60,000 households were housed, and 59,323 vouchers were still leased in April 2025. Interviewed agencies credited partnerships with Continuums of Care, existing case managers, separate waiting lists, at least 120 days to search, self-certified documents and income, pre-inspection and higher payment standards (Urban Institute, 2025) [EV-HOU-346]. EHV fees were funded in full while regular voucher fees were prorated [EV-HOU-343].

**The scale problem.** The plan issues 250,000 awards a year from 2030, more than three times EHV's whole allocation every year, and EHV took about two years to reach two-thirds leased [EV-HOU-345]. At EHV's pace the 2030 awards would not all be leased until 2032 (judgment from those figures). The award count is fixed by memo 8; the delivery task is to lease them as fast as the market allows.

**Fixes.**
1. **Fees for the new awards are paid in full, by statute, from mandatory money** (HOU-4A.02), as EHV's were [EV-HOU-343]. They are never prorated with the regular voucher fee. They include an issuance fee for each award, paid when the voucher is issued, not only when it leases, so agencies are paid for the search work that EHV's experience shows takes months (judgment).
2. **Write EHV's waivers into the statute for every new award:** a 120-day minimum search term with extensions, self-certified documents and income at application with checks after, pre-inspection [EV-HOU-232], separate lists for the guarantee's stages, and payment standards up to 120% of the limit where lease-up is low [EV-HOU-346]. In EHV these were waivers HUD could withdraw; here they are law (judgment).
3. **Over-issue and reallocate.** Agencies may issue more vouchers than awards, as California and New York agencies did with EHV [SRC-1444]. Awards an agency has not issued within 6 months, or leased within 18, move to another agency or to the state agency serving the same area, on published measures. This copies ERA's reallocation [EV-HOU-150], but on a rule set in advance.
4. **A backstop administrator.** Where an agency declines new awards or misses the measures twice, the state housing agency or a regional consortium takes them. Small agencies may pool administration (judgment).
5. **Pace by readiness, not by waiting.** The 2030 awards go first to places that sign the CoC and data agreements by mid-2030; the rest follow in the second half (judgment). HUD's 2030-31 awards are then spread by need through the year rather than in one batch.

**Project-based limits in current law (section 4's open check).** An agency may now project-base at most 20% of its authorized units, plus 10% for homeless, veteran, supportive and hard-to-use areas (42 U.S.C. 1437f(o)(13)(B)) [EV-HOU-351]. HOU-4.04's attached awards would exceed this in some tight markets, so the statute must exempt them, as section 4 assumed. Current law's right to move after 12 months is real, but if no voucher is available the agency may give the family priority for the next one [EV-HOU-352]. That is a wait, not a right. For HOU-4.04's "right to move", the statute should say the move-out voucher is funded from the award itself, so it is always available (judgment). Both points go to the section 4 owner as text changes; this section does not edit section 4.

### 2.3 Landlords

**What the record shows.** The number of landlords taking vouchers fell from just over 700,000 to about 640,000 between 2010 and 2016 while vouchers rose; housing agency staff named payment levels and paperwork, more than views of tenants, as the reason (HUD study, first Trump administration, 2019) [EV-HOU-347]. In paired tests, most landlords refused vouchers in three of five metros, and few did where state or local law barred refusal [EV-HOU-093].

**Fixes**, mostly already in section 4:
- the national source-of-income protection from 2030 (HOU-4.06), with enforcement that does not rest on HUD alone (6.1);
- neighborhood payment limits (HOU-4.05) [EV-HOU-095];
- search help with landlord outreach and deposits (HOU-4.07) [EV-HOU-091];
- quick inspections: one recent passing inspection under another program counts, and pre-inspection [EV-HOU-232];
- **two additions for the statute (judgment):** first payment to a new landlord within 30 days of the lease, with interest if late; and a damage and vacancy-loss fund inside HOU-4.07's fee, so a first-time landlord's main financial worry is covered.

### 2.4 State revolving funds and the construction loans

**What the record shows.** State housing finance agencies already run the low-income housing tax credit and report tenant data [EV-HOU-118], and many ran ERA, where they credited pre-payment checks and sample reviews with stopping scams (National Council of State Housing Agencies, which has a stake, 2022) [SRC-1069]. HOME is a standing state and local channel [EV-HOU-226]. The register has no measure of how ready each state is to run a revolving loan fund at $8 billion a year, nor of how fast the drinking water and clean water revolving funds reached that scale. That gap is listed at the end.

**Fixes.**
1. **The ramp fits the gap.** HOU-3C.01's $3 billion in 2030 and $5 billion in 2031 give states two years to stand funds up before $8 billion a year (HOU-3C.01).
2. **A plan before money.** Each state files a fund plan (uses, the 30% for extremely low-income homes, the 20% match, underwriting rules) within 9 months of enactment. HUD has 60 days to object; silence is approval (judgment; section 8).
3. **Where a state does not take part**, its share goes to the alternatives in section 5 below.
4. **The construction loans need a new HUD lending office** and a CBO subsidy rate. The risk-share model lets state agencies originate and service the loans, so HUD underwrites the program, not each loan (HOU-3C.02). The loans start at $10 billion in 2030 for the same reason as the grants (legacy ramp).

### 2.5 The emergency fund network

ERA built about 740 grantees almost from nothing in 2021 [SRC-1068], spent about 6% of its first round in five months, moved more than $3.1 billion from slow grantees [EV-HOU-150], paid 2% of households twice [SRC-1061], and was never measured for improper payments [EV-HOU-182]. Point 5's rules (approved by Espen) answer each lesson; delivery adds only the order of building:
1. **2029:** HUD publishes the data standard, the model risk screen and the grantee application within 6 months of enactment (statutory deadline).
2. **2030:** grantees are named. The one-time start (HOU-1D.04) runs through them, so the network is tested at volume and then stays.
3. **2031 on:** the standing fund runs through the same grantees, with money moving between them on published measures.
4. **Where no state or eligible locality applies,** HUD names a nonprofit or regional administrator (section 5 below).

### 2.6 The services workforce for supportive housing

**What the record shows.**
- HUD-VASH, the model for vouchers paired with case management, has been held back by staff: in fiscal 2024 over a quarter of VA medical centers with two or more case managers had at least 20% of the posts empty, turnover ran 20-26% a year, and short staffing reduced services and delayed admissions (GAO, 2026) [EV-HOU-341]. VA did not record why eligible veterans were not referred in 87% of 174,045 cases, so the shortfall cannot be measured [EV-HOU-342].
- In an advocacy group's 2023 survey of homeless services workers, 55% of full-time respondents earned under $50,000, three in four said their employers were understaffed, and 71% reported high turnover (National Alliance to End Homelessness, a convenience sample) [EV-HOU-349].
- HRSA projects large shortages of addiction counselors, psychiatrists and mental health counselors [EV-HOU-338]. Medicaid, the largest possible funder, now faces budget-neutral waivers from 2027 [EV-HOU-337] and rescinded guidance [EV-HOU-339], and Minnesota's housing benefit ended over provider fraud [EV-HOU-329].

**Fixes** (HOU-4.12 sets the money; this is how it is delivered):
1. **Wage floors and caseload limits as conditions on service money** (HOU-4.12, item 3), so new money buys staff who stay, not only more posts (research note, recommendation 5).
2. **Contracts, not open billing.** Service money pays providers on contracts with staffing and contact standards [EV-HOU-329].
3. **Peers and non-clinical navigators carry most contact work;** clinicians sit on teams (research note, judgment). Training money for peer specialists goes with the first awards in 2030.
4. **Rent is never held back for want of a navigator.** Stage 1 awards go out on HOU-4.03's order. Where the navigator duty in HOU-4.11 cannot be met, the provider reports it and the shortfall is funded, but the tenant keeps the home (Housing First, memo 5 B).
5. **Measure the gap.** Every provider and VA medical center reports unfilled navigator posts and households waiting for one. GAO's HUD-VASH finding shows what is lost without this [EV-HOU-342].
6. **HUD-VASH itself.** The research note's change (a veteran who stops engaging moves to a regular voucher automatically) [EV-HOU-325] needs a HUD notice in 2029 and the regular bill. VA case manager hiring is the VA's and the care flagship's; this dossier asks for it to be counted.

## 3. Timeline, 2029-2038

### The vehicles in the calendar

| Vehicle | What housing puts in it | Central range in the calendar | Favorable | Difficult |
| --- | --- | --- | --- | --- |
| Executive action, January 2029 | Revoke the July 2025 order's conditions [EV-HOU-107]; HUD notices and rules (Housing First, CoC rule, HUD-VASH, payment limits); hiring | First weeks | — | — |
| R1 (FY2029 resolution) | Nothing in section 4. A question for Espen: a small readiness tranche (systems, data, staff) | Done by about February 20, 2029 (median) | Late January | July 2029 (median); as late as November |
| R2 (FY2030 resolution) | All of housing's mandatory money and conditions | Median **January 14, 2030**; runs span June 2029 to December 2030 | Median July 12, 2029 | Median run does not finish |
| R3 (FY2031 resolution) | Fixes found in 2030; any housing piece that slips from R2 | Median July 2, 2030 | May 2030 | Median run does not finish |
| Housing regular bill (calendar row HOU-7) | HOU-4.01 definitions, 4.02 data and privacy, 4.05, 4.06, 4.09, 4.11, 1D.03 privacy, 5.02, 6.01 eligibility, 6.02, 9A.01 | Median February 26, 2030; September 2029 to October 2030 | Median July 24, 2029 | Median run does not finish |
| Appropriations | Evaluations; renewals after the mandatory windows; HUD's base staff (CAP-7S, CAP-7) | Yearly from FY2030 (October 1, 2029) | — | — |

**What this means.** Section 4 calls R2 "fall 2029"; in the calendar's central runs it is about January 2030, and in difficult runs it may not pass. A plan whose first awards are dated "2030" must still work if R2 is signed in mid-2030. So:
- **Dates run from enactment, with a latest date.** "First awards within 6 months of enactment" rather than a fixed month; and money for each award year is available until spent, so a late law does not lose a year (judgment).
- **The money does not wait on the regular bill.** Section 4 already writes R2's zoning money so it can be spent under the Act's current rules (HOU-6.01). The same applies to the data system: R2 funds it, and until the regular bill gives the data-sharing authority, programs share records under current law with the household's consent (section 4 below).
- **If R2 fails** (the calendar's difficult case), the guarantee, the fund and the construction money have no other vehicle that carries mandatory spending except R3. Housing would then move to R3 whole. This is a scenario point for the lead and Espen, not a housing decision.

### Year by year

| Year | Rental help | Emergency fund | Homes and repair | Supportive housing and services | Rules and remedies |
| --- | --- | --- | --- | --- | --- |
| 2029 | HUD readiness: data standard, application, award formula; agencies and CoCs sign agreements | Grantee rules, model screen, data standard published | State fund plans due 9 months after R2; HUD lending office | Executive order revoked; HUD notices on Housing First, CoC scoring, HUD-VASH; CoC rule change starts | Regular bill moves |
| 2030 | First 250,000 awards, all tenant-based; full fees; search help | Grantees named; one-time start begins (HOU-1D.04) | Revolving funds $3 billion; loans $10 billion; Capital Fund rises; right-to-return rules on repair money | Recovery-housing grants (HOU-4.10, 2030-34); HUD services backstop begins; peer training | Source-of-income protection in force; payment limits in tight markets |
| 2031 | Second 250,000; reallocation of unused awards | Start ends; standing fund runs | Funds $5 billion; loans $20 billion | Medicaid tenancy services, if the care flagship's bill passes | First payment-error estimate published (from year one's sample) |
| 2032 | Third 250,000; attached awards may begin in tight markets (up to 25%) | Standing | Funds $8 billion a year from here | — | Payment limits by ZIP code in all metros; HUD's Build Now study due |
| 2033 | Fourth 250,000; stage 1 served, stage 2 begun | Standing | — | — | The plan's second-term election is in 2032: section 8's protections are tested from here |
| 2034 | Stage 2 opens: up to 300,000 families a year | Standing | — | Recovery-housing evaluation; renewal by appropriations | — |
| 2035-36 | Stage 2 enrollment; attached-help evaluation reports (2036) | Standing | — | — | — |
| 2037 | **Stage 2 becomes a right**: every eligible family that applies gets help | Standing | — | — | Guarantee remedies in force (6.3); GAO and HUD investor-limit reports |
| 2038 | **Stage 3 opens** for disabled extremely low-income renters, with Medicaid services and reserved accessible units | Standing | Accessible-unit reservations begin at turnover | HCBS with tenancy supports must be in place where stage 3 lands | — |

Readiness gates (judgment): stage 2's 2034 opening and stage 3's 2038 opening each need HUD to certify, a year ahead, that the data system, fees and agency agreements are in place. If HUD does not certify, the opening still happens on the date in law; the certification only triggers extra administrative money. A gate that could delay a right would hand a slow agency a veto (section 8).

## 4. One application, income checked once, and the hand-offs

Section 4 defines the system (HOU-4.02). Delivery has to make it work across housing agencies, emergency grantees and CoCs that today use different forms and systems.

**The pieces.**
1. **One application.** A federal application, on paper and online, that any access point can start: the emergency grantee, the housing agency, coordinated entry, or the eviction court through the grantee. HUD builds and hosts the online version and an interface local systems can use; local bodies may keep their own front end if it writes to the same record (judgment).
2. **One household record.** Built on point 5's payment-level standard (rule 8): a protected household identifier, address and tract, income band and how it was found, risk score, program, dates and payments. It is what lets HUD check for duplicates across grantees [SRC-1061] and trace hand-offs.
3. **Income checked once.** An income finding by any of the three programs, or by TANF, Medicaid or SNAP, counts for the others for 12 months (HOU-4.02 item 5, extending 1437a(a)(7)(D)). In practice: the record stores the finding, its source and its date; the next program reads it rather than asking for pay stubs. Federal income-matching data (shared rule 5) confirms it after award, not before (point 5, rule 4).
4. **Hand-offs in the record.** Each hand-off in HOU-4.02 (emergency to long-term, repeat need, attached to tenant-based, homelessness to housing, health and benefits) is a status change on the same record with a deadline: the receiving program must act within 30 days, and the household is told in writing (judgment).

**Who builds it.** HUD's delivery office (2.1), with money from R2's administration set-aside. A first version for the emergency fund and the new awards in 2030; CoC systems (HMIS) and existing voucher systems connect by 2032. One system for the plan's new programs, not a rebuild of every agency's software (judgment).

**Law needed.** The regular bill gives the authority to share records across programs and with eviction courts and shelters, with privacy rules: use only for eligibility, payment, duplicate checks and evaluation; no use for immigration or criminal enforcement; access logs; penalties for misuse (judgment, consistent with ERA's data-protection duty [SRC-0991]). **Until it passes**, records are shared with each household's signed consent, which current programs already use for income checks (judgment; the statutory basis is a section 4 open check).

**Where it can fail.** Mixed-status families need prorated help and must not be deterred by data sharing (shared rule 3); the no-enforcement-use rule is the protection, and the immigration flagship owns the table. Coordinated entry had limited capacity to match people to EHV at first [SRC-1444]; the agreements in 2.2 item 5 address that.

## 5. States, cities and tribes

### Who takes part

- **Housing agencies** are local or regional bodies under state law, not state governments. A state cannot by itself stop its agencies from taking new awards, so the guarantee reaches every state (judgment). The backstop administrator (2.2 item 4) covers places where an agency declines.
- **States** run the revolving funds and are the default emergency fund grantee. They also hold Medicaid, which decides whether services reach supportive housing.
- **Cities and counties** of 200,000 or more may run their own emergency fund program, with no overlap; they compete for the zoning reward; and they are where eviction courts and CoCs sit.
- **Tribes.** ERA's first round set aside $0.800 billion for tribal areas by the Native American Housing Block Grant formula; its second round had none [EV-HOU-350]. Tribal HUD-VASH is a pilot that GAO says lacks measurable objectives and an evaluation plan [SRC-1441]. The register has no evidence on how the new awards would reach tribal lands, where vouchers are hard to use. The working answer here is a tribal set-aside in HOU-1D, HOU-3C.01 and the new awards, run through tribes or their housing entities under the block grant law. The share is a question for Espen (judgment).

### Where a state refuses

| Program | If the state refuses or does not act | Why this route |
| --- | --- | --- |
| HOU-3C.01 revolving fund | Its share goes, in order, to eligible cities and counties in the state, then to a nonprofit or regional fund HUD selects, then to HOU-3C.02's direct loans in that state. It stays in the state | Federal money for people in the state is not lost because of a governor (judgment) |
| HOU-1D emergency fund | Eligible cities and counties run it; HUD names a nonprofit or regional administrator for the rest of the state | Point 5's one-administrator rule still holds |
| New awards (HOU-4A, 4D, 4.08) | Not a state program; housing agencies run them; backstop administrator where an agency declines | No state veto |
| Services (HOU-4.12) | Where a state does not cover tenancy services in Medicaid, the HUD services backstop pays for them | Section 4 limits the backstop to tenants without Medicaid; delivery suggests it also cover tenants whose state Medicaid program does not pay for the service. A question for Espen |
| Source-of-income protection (HOU-4.06) | Applies everywhere; state laws that protect more stay [EV-HOU-247] | Federal civil-rights floor |
| Zoning reward (HOU-6.01) | Voluntary: a state that declines does not compete; its localities may | Spending condition limits (`NFIB v. Sebelius`, HOU-6.02) |

## 6. Tenant remedies and enforcement

### 6.1 Source-of-income protection

The protection rides the Fair Housing Act's remedies (HOU-4.06): a HUD complaint, a private suit, and Justice Department suits for patterns. HUD's fair housing office was cut and its testing grants terminated and later reinstated in 2025 [SRC-1440]. So enforcement must not depend on HUD alone (judgment):
- the private right to sue under the Act is the main remedy and needs no new law;
- the regular bill funds the Fair Housing Initiatives Program's testing and enforcement grants as mandatory money for 2030-34, the years landlords learn the rule, so paired tests like HUD's 2018 study [EV-HOU-093] keep running whatever the yearly bill says;
- state and local fair housing agencies that enforce the federal protection are reimbursed on the same terms as other Fair Housing Act cases.

### 6.2 Right to return and repair first

HOPE VI returned few residents to rebuilt sites: 19% in one study [EV-HOU-122]. RAD's evaluation found 82% stayed at the same property and 92% were in the original property after conversion, but its survey covered 298 residents of 18 early, mostly southern conversions and HUD's data could not track movers (HUD-commissioned, first Trump administration, 2019) [EV-HOU-348]. The ROAD to Housing Act now requires HUD to publish yearly how many residents stay or return [EV-HOU-231]. Delivery (judgment):
- **every displaced resident is tracked in the household record** (section 4), so the yearly count is a census, not a survey;
- **residents have a private right to enforce** the right to return, one-for-one replacement and relocation payments (HOU-5.02), with fees for a resident who wins;
- **HUD's withholding power** stays, but residents do not have to wait for it.

### 6.3 The guarantee as a right from 2037

From 2037 every eligible family that applies gets stage 2 help (HOU-4D.01). A right on paper needs these in the statute (judgment):
1. **Entitlement words and money.** "Shall provide" to each eligible family, paid from mandatory money that does not depend on a yearly vote (already the design).
2. **A decision deadline.** A complete application is decided within 30 days; a family that hears nothing is treated as approved, pending checks after award.
3. **Notice and a hearing.** A written decision with reasons; an informal hearing before an officer outside the deciding office; then review in federal court. The voucher program's existing hearing rules are the base.
4. **No waiting list for the entitled.** An agency may not put an eligible stage 2 family on a waiting list after 2037. If it cannot issue, the backstop administrator issues.
5. **A private right of action** for families denied or delayed, with fees, and standing for legal aid groups.
6. **Stage 3 from 2038** carries the same remedies if Espen and the care flagship make it a right; section 4 leaves its pace open.

### 6.4 Emergency fund and other remedies

- Payment within 30 days of a complete application (point 5, rule 5), with written reasons for a denial and one appeal to the grantee.
- No eviction for nonpayment for the months paid (HOU-1D.02).
- Housing First tenants: non-engagement can never end the lease or the subsidy (HOU-4.11). A tenant can enforce this against the provider through the CoC grievance process and in court (judgment).

## 7. Fraud and improper payments

**Where the risk is.** In ERA the bad payments in the inspector general's cases came from fabricated leases and false landlords, not from tenants misstating income (point 5, rule 4) [SRC-0995] [SRC-0994]. Duplicate payments came from overlapping grantees [SRC-1061]. ERA was never measured [EV-HOU-182], and HUD's own tenant-based rental assistance reported no improper payment estimate in FY2024 though judged susceptible [SRC-1062]. In Medicaid housing services, the fraud was by providers billing fee-for-service [EV-HOU-329].

**Controls**, in the order money moves:
1. **Before paying a landlord:** identity, ownership and tenancy checked against public records (point 5, rule 4), for vouchers as well as emergency help. A new landlord's first payment waits for the ownership check (judgment).
2. **Before paying a household:** no documents beyond self-attestation where the statute allows it; checks after award against federal income data.
3. **Across programs:** the household identifier and a monthly duplicate check across grantees and agencies (section 4).
4. **Providers:** contracts with staffing standards, not open fee-for-service billing, for services money [EV-HOU-329].
5. **Measurement:** an improper and unknown payment estimate from a random sample in year one, published yearly with a target, for the new awards as well as the fund (point 5, rule 6). It is funded from the programs' own set-aside, so it is not skipped.
6. **Recovery:** errors are recovered from grantees and landlords, never by evicting a tenant over an honest mistake (HOU-1D.03).
7. **The inspector general** gets a set-aside from the mandatory money for audits of the new programs (judgment). ERA's oversight came from the inspector general and GAO; both need money and access.

## 8. A hostile or slow agency: what the statute must say

The project's rule is to give an administration's analysis skepticism in proportion to its record (`DEC-2026-10-30-01`). For delivery, the same record means assuming that a later HUD may want the programs to fail. The 2025 record includes a 29% staff cut [EV-HOU-340], fair housing grants terminated and reinstated [SRC-1440], a hiring freeze that led VA medical centers to rescind case-manager offers [SRC-1441], and an executive order against Housing First [EV-HOU-107]. So:

| Risk | What the statute says | Provisions |
| --- | --- | --- |
| Money withheld or slowed | Mandatory money appropriated in the statute, allocated by a formula in the statute, paid to grantees and agencies on a schedule in the statute; any delay beyond 30 days is reported to Congress and GAO; impoundment is barred by name | All R2 programs |
| Rules never written | Each rule has a deadline; if HUD misses it, a default in the statute applies (the tight-market list from Census vacancy data; the per-award fee at a set amount; the model screen as published by a named date; fund plans approved by silence) | HOU-4.04, 4A.02, 4.07, 1D.02, 3C.01 |
| Rules rewritten | The design choices that guidance could undo are written into law: self-attestation; no work or treatment conditions; Housing First; EHV-style search terms; the payee order; non-engagement never ends housing | HOU-4.01, 4.09, 4.11, 1D.02, 2.2 above |
| Waivers used to hollow programs | No waivers of eligibility, rent, conditions, remedies or the data rules; Moving to Work's limits on rent and work-rule waivers are the model [EV-HOU-234] | All |
| Staff cut | A share of each program for federal administration, available until spent (2.1); fees paid in full (2.2) | HOU-4A.02, 1D.03 |
| Data hidden | Monthly public reports by place, generated from the shared record; GAO access by right | Section 4 above |
| Enforcement abandoned | Private rights of action and fees (section 6); mandatory testing grants for 2030-34 | HOU-4.06, 5.02, 4D.01 |
| Readiness used as a veto | Readiness certifications trigger money, never a delay of a right (section 3) | HOU-4D.01, 4.08 |
| Program moved or merged | The rental help system's lead office and its funds stay in HUD unless a later law moves them (judgment) | HOU-4.02 |

None of this makes a law self-executing against an agency that ignores it; it gives tenants, grantees, states and courts the tools to make it run, and it removes the discretionary steps where delay has happened before (judgment).

## 9. Lessons from past programs

| Program | What happened | Lesson | Where it is used here |
| --- | --- | --- | --- |
| Emergency Rental Assistance (2021-22) | Slow start (about 6% spent by May 2021); spending doubled after self-attestation; $3.1 billion reallocated [EV-HOU-150]; 2% paid twice and 26% of payment data missing [SRC-1061]; never measured for improper payments [EV-HOU-182] | Rules before money; one administrator per place; measurement from year one; self-attestation with checks on landlords | 2.5; section 4; section 7; point 5 |
| Emergency Housing Vouchers (2021-) | 87% leased or issued in a year, 77 days to lease [EV-HOU-344]; 67% leased by February 2023, with wide variation [EV-HOU-345]; more than 60,000 housed [EV-HOU-346]; fees paid in full [EV-HOU-343] | Mandatory money, full fees, CoC partnerships and written-in flexibilities work; leasing still takes months, and weak agencies need a backstop | 2.2 |
| HOPE VI (1990s-2000s) | 19% returned to rebuilt sites in one study [EV-HOU-122] | Replacement and return must be rights with tracking, not goals | 6.2; HOU-5.02 |
| Rental Assistance Demonstration (2012-) | Most surveyed residents stayed on site [EV-HOU-348], but the evidence is thin and HUD could not track movers; now permanent with yearly reporting [EV-HOU-231] | Count every resident in the record; give residents the remedy | 6.2 |
| HUD-VASH (2008-) | Each voucher cut veteran homelessness by about one [EV-HOU-176]; held back by case-manager vacancies and turnover [EV-HOU-341]; reasons for non-referral unrecorded [EV-HOU-342]; non-participation can end the voucher [EV-HOU-325] | Pair rent with funded, retained services staff; measure the services gap; never tie housing to engagement | 2.6; HOU-4.11 |

## 10. Main delivery risks

| Risk | Likelihood (judgment) | Effect | Mitigation |
| --- | --- | --- | --- |
| R2 passes in 2030 or later | Central case in the calendar | First awards slip a year | Dates from enactment; money available until spent (section 3) |
| Lease-up lags the 250,000 pace | High in tight markets | Awards sit unused; cost looks lower than need | Full fees, search help, over-issue, reallocation (2.2) |
| Services workforce short | High | Supportive housing tenants without navigators | Wage floors, peers, measurement; rent not held back (2.6) |
| A later HUD slows the programs | Material after 2033 | Rights on paper only | Section 8 |
| States slow or refuse on revolving funds | Some states | Construction money idle | Ramp, plan-by-silence, pass-through (2.4, 5) |
| Regular bill stalls | Calendar's difficult case | No data-sharing law, no source-of-income protection | Consent-based sharing; R2 conditions where they can carry the rule; the protection waits on the bill |
| Data system late | Medium | No duplicate check; slow hand-offs | Emergency fund first, then awards; consent sharing |

## Questions for Espen

These are flagged, not decided; each also appears in the README.
1. **A readiness tranche in R1?** A small amount of mandatory money in the first reconciliation bill (February 2029) for HUD's data system, the application, hiring and the grantee rules, so 2030 is not lost if R2 runs to 2030. The alternative is FY2029-30 appropriations, which a Democratic Congress would also write. Recommendation: yes, if R1's scope allows it (judgment).
2. **A tribal set-aside** in the emergency fund, the revolving funds and the new awards, and its size. ERA used about 3% of its first round [EV-HOU-350] ($0.800 billion of $25 billion [EV-HOU-150]). Recommendation: yes, at a share set from need data in section 6.
3. **The services backstop where a state's Medicaid program does not cover tenancy services.** Section 4 pays it only for tenants without Medicaid; delivery suggests extending it to tenants whose state does not cover the service. It costs more and lowers the pressure on states to cover it. Recommendation: yes, through 2035, then only for tenants without Medicaid.
4. **Mandatory fair housing testing money for 2030-34** to enforce source-of-income protection while HUD's fair housing office rebuilds. Recommendation: yes.
5. **Deemed approval** for guarantee applications not decided within 30 days from 2037. It protects the right against a slow agency but pays some families before checks. Recommendation: yes, with checks after award.

## Changes this section asks of section 4

For the section 4 owner; not made here.
- HOU-4.04: exempt attached awards from the project-based cap [EV-HOU-351], and fund each household's move-out voucher from its own award, since current law allows a wait for the next voucher [EV-HOU-352].
- HOU-4A.02: fees for the new awards paid in full, never prorated [EV-HOU-343], with an issuance fee.
- HOU-4A.01 and others: dates written from enactment, with money available until spent.
- HOU-4.02: the consent-based fallback for data sharing until the regular bill passes.

## Evidence still needed

- State readiness to run housing revolving funds: state housing finance agency capacity and the start-up record of the clean water and drinking water revolving funds (EPA, GAO).
- How vouchers and emergency help reach tribal lands (HUD's Native American programs; GAO).
- Search-help costs and design (HOU-4.07's open research, section 4).
- The statutory basis for consent-based record sharing across HUD, HHS and USDA programs (democratic renewal, CAP-13).
- Voucher lease-up and HUD-VASH voucher use from HUD's own data after 2024, and HUD's improper payment estimate for tenant-based rental assistance when it publishes one [SRC-1062].
- Homeless services wages from a representative source, to replace the convenience survey [EV-HOU-349].
