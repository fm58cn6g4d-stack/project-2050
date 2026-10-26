# Domain file: Capacity — Congress and the successor state (CAP)

**Current recovery allocation ([October 26 approval](../governing/project-2050-governing-decisions.md#recovery-and-solvency-recommendations-approved-october-26)).** CAP-7S is now a $300B lifetime surge and CAP-7 a $300B FY2030–39 sustained-increase envelope, replacing $600B/$490B. Shift $10B of surge cash from FY2030 to FY2029 without increasing its lifetime total. Immediate legal availability remains selected. Protect adjudication, payments, workforce and enforcement; rebuild allocations from current agency budgets/workloads rather than prorating the old table. The previous amounts and agency split below are historical comparisons, not current allocations. A $200B IRS-receipt risk allowance accompanies the reduction. The separate $100B delivery contingency is not an additional allocation to every agency. Current amounts are consumed from [recovery-adoption.json](../index/data/inputs/recovery-adoption.json); the old ledger CSV is a preserved comparison.

Canonical (batch 2, with the per-agency allocation and the Decision Brief 2 restructuring of CAP-7). This file covers staging inventory sections 8 (congressional capacity) and 9 (state capacity and the successor state), which are pointers to it. It is where D9's agency rebuild is designed; D9 sets the direction (a multi-year surge of ~$0.6T fully available immediately on enactment (R1 target FY2029, Oct 21 decision) plus a sustained increase of ~0.12% of GDP, provisional) and this file says what it buys, which agencies it names and what each gets.

All figures are ten-year totals for 2030-39 in trillions unless a table says $B. Basis tags: **sourced**, **scaled**, **estimate** (mine). Survival tags follow D1: ✔, ◐, ✖.

**Why this file comes before the rest of the agenda, not after.** Design rule 6 says every delivery item names the agency and staffing it depends on. Across batch 1 that produced a list — IRS for monthly CTC payments, SSA or a leave office, HHS and the states for child care slots, CMS for auto-enrollment — and batch 2 adds more (the EAC, the FEC, EOIR's successor, the integrity-enforcement units). Batch 3 adds FEMA, EPA, DOE and FERC, the NLRB, the Wage and Hour Division and OSHA, and the FTC and DOJ Antitrust. None of those commitments is real until this file is funded. The health file's auto-enrollment build and the family file's monthly payments are the two places where a capacity failure would be publicly visible within the first year.

**Window caveat (Oct 21):** numerical window totals below retain the old cash proxy. Immediate FY2029 availability is decided; FY2029 outlays are unpriced, and the accelerated path has not been fiscally validated. See index/capacity-funding-model.md.

## Summary

| ID | Policy | Chosen design | Cost | Vehicle | @51 | Felt by Nov 2030? |
| --- | --- | --- | --- | --- | --- | --- |
| CAP-1 | Congressional staff and pay | Personal and committee budgets to real 1979 levels; fix pay compression | 0.02 (0.01-0.03) | AP | ◐ | Yes |
| CAP-2 | Office of Technology Assessment | Re-establish as the Congressional Office of Technology | 0.00 (0.00-0.01) | AP | ◐ | Yes |
| CAP-3 | CRS, GAO, CBO | Restore to at least 1992 levels; rebuild CBO scoring capacity | 0.01 (0.01-0.02) | AP | ◐ | Yes |
| CAP-4 | Budget process | Biennial budgeting; automatic CR at prior-year levels with an escalating congressional penalty | 0.00 | FL | ◐ | Yes |
| CAP-5 | Earmarks | Restore transparent, competitively awarded, capped earmarks | 0.00 | FL | ◐ | Yes |
| CAP-6 | Statute-tracking office | Nonpartisan office tracking judicial readings and drafting overrides | 0.00 | AP | ◐ | No |
| CAP-7S | Agency rebuild surge | ~$0.6T multi-year appropriation fully available immediately on enactment; R1 target FY2029; D4/C42 financing | 0.60 (0.45-0.75), lifetime working total; window proxy pending cash costing | R1 target | ◐ pending Byrd/jurisdiction review | Partly |
| CAP-7 | Sustained capacity increase | Steps up over FY2030-32 (about $15B, $31B, $49B) to ~0.12% of GDP, then tracks GDP; permanent, with statutory staffing floors | 0.49 (0.40-0.60) | AP | ◐ | Partly |
| CAP-8 | Schedule Policy/Career prohibition | Statutory prohibition; the executive rescission is EXE-17 | 0.00 | FL | ◐ | Yes |
| CAP-9 | Civil service modernization | Real performance management with real political insulation | 0.00 (0.00-0.01) | FL | ◐ | No |
| CAP-10 | Successor architecture | Development and education functions rebuilt, enforcement separated from policy | 0.00 | FL | ◐ | No |
| CAP-11 | Federal hiring reform | Time-to-hire targets, direct-hire authority, salary flexibility | 0.00 | FL | ◐ | Yes |
| CAP-12 | Technology procurement | Procurement reform; in-house engineering capacity | 0.00 (0.00-0.01) | FL | ◐ | No |
| CAP-13 | State and local capacity grants | Implementation grants where federal policy dies | 0.03 (0.02-0.05) | AP | ◐ | No |
| CAP-14 | Member housing allowance | A DC residence allowance, packaged with INT-1 | 0.00 | AP | ◐ | No |
| CAP-15 | Legislative technology | Unified drafting and scoring systems | 0.00 (0.00-0.01) | AP | ◐ | No |
| CAP-16 | Committee jurisdiction | Realignment for AI, climate and cyber | 0.00 | RU | ✔ | Yes |
| CAP-17 | Legal culture | Congressional clerkships, drafting clinics, legislation courses | 0.00 | X | ✔ | No |
| CAP-18 | Draft in opposition | All successor legislation and delegation templates written 2027-28 | 0.00 | X | ✔ | — |
| | **General-fund total** | | **1.15 (0.89-1.49)**; the ledger carries 1.13 (CAP-7S, CAP-7, and CAP-8 for the congressional and civil-service rows), with CAP-13 unscored and in no total | | | |

The congressional-capacity items (CAP-1 to CAP-6, CAP-14, CAP-15) total about $0.03-0.07T — a few percent of the agency rebuild, and the cheapest high-leverage spending anywhere in the project.

## Crosswalk

| This file | Ledger row | Staging rows |
| --- | --- | --- |
| CAP-1 to CAP-5, CAP-14, CAP-15 | DEM12 (merged into DEM13, C26) | 8.1-8.7 |
| CAP-6 | DEM13 (the CAP-8 row) | 8.9 |
| CAP-7S, CAP-7 | A1 (two rows) | 9.1 |
| CAP-8 to CAP-12 | DEM13 (fast track, C27) | 9.2-9.6, 9.8 |
| CAP-13 | (new row needed) | 9.9 |
| CAP-16 | (House rules; no row) | 8.8 |
| CAP-17, CAP-18 | (no rows) | 8.10, 9.10 |
| (pointer) | E3 / climate file | 9.7 permitting — home is domain-climate.md (CLI-3, CLI-6) |

## Congressional capacity

### CAP-1. Staff and pay

**Design.** Personal and committee staff budgets restored to real 1979 levels, with pay compression fixed so senior staff are not priced out by lobbying salaries. **Packaged with the stock ban** (domain-integrity.md INT-1): accountability buys capacity, which is the only framing under which "Congress spends on itself" survives contact with a press cycle.

**The numbers.** House committee staff went from 2,001 (1994) to 1,317 (1995), a one-third cut (CRS). Brookings counts it differently (2,147 to 1,266). Committee staff fell about 35% from 1994 to 2014 while leadership staff funding rose 89% (Pascrell, 2019).

**Cost.** About $0.02T, range $0.01T to $0.03T (estimate) — roughly $1.5-3B a year across both chambers.

### CAP-2. Office of Technology Assessment

**Design.** Re-establish OTA, renamed the Congressional Office of Technology on the Takano-Foster-Casten-Beyer bill. Peak budget $21.3M with a statutory staff cap of 143; not funded beyond February 1996. The House Select Committee on the Modernization of Congress endorsed re-establishing an improved OTA unanimously, which makes this the most bipartisan row in batch 2.

**Cost.** Under $0.01T (estimate) — a few hundred million a year at modern scale.

### CAP-3. CRS, GAO and CBO

**Design.** Restore CRS and GAO to at least 1992 levels and rebuild CBO's scoring capacity. GAO fell from 5,062 staff (1992) to 2,989 (2015); CRS from 838 to 609, with the current headcount around 600 (Brookings and CRS; counts vary by method, and the caveat travels with the figure).

**Why CBO is in this row.** Half the open items across every domain file in this project are "needs a score." A Congress that cannot score its own bills within a reconciliation window cannot run the D5 schedule. This is the least glamorous row in batch 2 and arguably the one with the highest return on the agenda's own terms.

**Cost.** About $0.01T, range $0.01T to $0.02T (estimate).

### CAP-4. Budget process

**Design.** Biennial budgeting and an automatic continuing resolution at prior-year levels, with an escalating penalty that falls on Congress rather than on programs: no recess, no non-appropriations floor business, suspended member travel until appropriations are done (Instruments #9).

**Reciprocity.** The penalty design is the point. An automatic CR alone rewards the party that prefers flat funding; the penalty restores the pressure to legislate without taking hostages. Option: the Merkley-Daines two-day appropriations fast track (path A, sec. 108), which does similar work through the rules rather than by statute.

### CAP-5. Earmarks

**Design.** Transparent, competitively awarded, capped earmarks. The honest case: earmarks are a legislative-capacity instrument — they are how a leadership assembles majorities for hard votes — and removing them removed a tool without removing the need.

### CAP-6. Statute-tracking office

**Design.** A nonpartisan office that tracks judicial readings of statutes and drafts override legislation, on the *Ledbetter* and Civil Rights Act of 1991 pattern. This is the institutional form of the courts file's CRT-14: statutory repairs happen reliably only if someone's job is to notice that one is needed.

### CAP-14, CAP-15. Housing allowance and legislative technology

A DC residence allowance addresses a de facto wealth filter on who can serve; package it with INT-1 to blunt the optics. Unified drafting and scoring systems are second-wave and cheap.

### CAP-16, CAP-17. Rules and culture

Committee jurisdiction realignment for AI, climate and cyber is a House rules-package item — ✔ at 51, and available in a January 2027 rules package if the House flips (staging 18.9). Legal-culture investments (congressional clerkships, drafting clinics, legislation courses, support for legisprudence scholarship) sit mostly outside the federal budget and are ✔.

## The successor state

### CAP-7. The agency rebuild line

**Historical sizing and rationale (October 20; amounts superseded October 26).** A rebuild needs a concentrated infusion paired with lasting funding, so the line is two rows (all figures estimates, provisional under D9):

| Row | What it is | Timing | 2030-39 | After 2039 | Financing (D4-B) |
| --- | --- | --- | --- | --- | --- |
| **CAP-7S, rebuild surge** | Multi-year funding for hiring, training, systems, facilities, claims and service backlogs | Full ~$600B immediately available on enactment; target R1 in FY2029. Old $70B/$120B/$130B/$120B/$100B/$60B FY2030-35 schedule is only an interim cash proxy | ~$0.60T lifetime working total (0.45-0.75); 2030-39 total to be restated after FY2029 costing | No permanent operations funded from this finite surge; final obligation period to be drafted | D4/C42 financing and written agency return cases; no extra envelope amount or FY2029 cash estimate adopted |
| **CAP-7, sustained increase** | A permanent addition to the same agencies' funding, lower than the surge, that carries the staff the surge hires and the systems it builds | Phases in over FY2030-32 to ~0.12% of GDP (~$50B in 2033, ~$65B in 2040), then tracks GDP | ~$0.49T (0.40-0.60) | Permanent | Paid for at maturity, like any permanent program |

Under the interim outlay proxy, combined funding peaks at about $180B in FY2032 (surge $130B plus sustained ~$50B) and settles at the sustained level (~$56B) from FY2036. The sustained level, 0.12% of GDP, sits between two alternatives: 0.10% of GDP (~$0.41T in the window, ~$54B in 2040) and 0.148% (~$0.60T, ~$80B in 2040, the level of an even ~$0.6T ten-year line); Espen accepted the surge's shape and 0.12% as the working figures. **Immediate availability (decided, Espen, Oct 21).** All surge funding is available upon enactment as multi-year money, targeting R1 in FY2029. Availability permits early commitments, not an assumption that the full amount is spent immediately. Build agency-specific obligation and cash profiles. Hiring and acquisition teams begin with the funding; check CAP-11/CAP-12 policy provisions separately rather than holding every agency for a later reform bill. Byrd/jurisdiction checks remain open, including SSA's scope; use the earliest viable companion for anything ineligible. D5's lost-R1 fallback must disclose delivery consequences. The per-agency split below applies to both rows, pro rata, until the bottom-up review (open item 2) replaces it.

**Design.** A named line with **statutory staffing floors** for the agencies delivery depends on. D9's list: IRS service, SSA, HUD, FTA, USCIS, CDC, NOAA, Education and USAID; the agencies the democracy, courts, executive-power and integrity files depend on, and CMS, which the health file names; and FEMA, EPA, DOE and FERC, the NLRB, the Wage and Hour Division and OSHA, and the FTC and DOJ Antitrust. The governing doc's D9 list matches the table below; the batch 4 agencies are still to be added (pending Espen, see the reserve row).

**What the line is: increments, not totals.** The figures below are **supplementary to each agency's baseline appropriations**, not total funding levels. They are each agency's share of the $600B multi-year surge available immediately on enactment; the same shares apply to the sustained row. The old FY2030-35 cash schedule is an interim proxy, not an availability restriction. Read the IRS's $130B as 22% of the surge on top of whatever the baseline provides, plus 22% of the sustained increase. That follows from D9, which sizes a "rebuild" line separate from the discretionary baseline, but the ledger does not say so explicitly and the baseline is not modeled. Two consequences: (1) the line only means what it says if baseline funding holds, so explicit funding and baseline-maintenance design matter; a staffing floor alone does not prevent a hostile appropriator from offsetting the increment; (2) the true cost of rebuilding is a function of where each agency's baseline now sits against its past level, which this file does not know.

**Historical per-agency allocation; replace rather than prorate.** Every figure below is **my estimate, with no project source**, set by judgment from how much of the agenda each agency carries and what the batch 1 to 3 files require of it. It is not derived from any agency's current budget; I did not look those up. Read it as a proposed split to argue with, not a finding. **Next refinement (Espen's request):** research current and past funding and staffing levels agency by agency, reason about what rebuilding and expanding capacity will actually require, and use the full domain files as inputs (each program's administrative needs, ramp dates and felt-by dates), replacing this top-down split with a bottom-up one.

| Agency or unit | $B, 2030-39 (est.) | Share | What it buys and which files depend on it |
| --- | --- | --- | --- |
| IRS (service and enforcement) | 130 | 22% | Monthly Child Tax Credit payments (FAM-1); the enforcement the revenue base assumes (REV-G8); valuation capacity for mark-to-market (REV-G11); clean-energy credits and direct pay (CLI-1); Climate Dividend payments (CLI-2) |
| USAID successor / development functions | 60 | 10% | Rebuilt development architecture (CAP-10); funding sits here, not in a separate line |
| SSA | 55 | 9% | The D8 baseline's benefit credit and minimum-benefit changes (SS-1 to SS-4); field-office and phone service; Climate Dividend payments to beneficiaries (CLI-2) |
| CMS | 50 | 8% (rounded; exact share 1/12) | All HLT-1 to HLT-6 delivery: restoration/state support; Medicare benefits/claims; public-plan operations/auto-enrollment; commercial-price implementation; payment integrity. Annex below; HLT administration overlap unresolved |
| CDC | 15 | 2.5% | D9-named. A placeholder for restoring core public-health staffing (set at $15B on Espen's review). Its named work is NSC-8's biosurveillance and preparedness capacity (domain-national-security.md, which proposes keeping it at $15B). Another need is the Thriving Economy map's expansion of CDC's Climate-Ready States and Cities program from 13 jurisdictions toward all 50, which no CLI row carries |
| HUD | 45 | 8% | Emergency aid, vouchers, public housing repair and the Housing Supply Fund (HOU-1 to HOU-6); the programs the ROAD to Housing Act assigned it without funding |
| NOAA | 40 | 7% | D9-named; climate and weather services; flood mapping for CLI-7 and CLI-8 |
| USCIS | 40 | 7% | Administration of comprehensive immigration reform (ledger E11) |
| Education | 40 | 7% | Pell, SAVE and PSLF servicing, Title I and IDEA administration (FAM-4) |
| FTA | 30 | 5% | Transit capacity; **overlap with Moving America, see below** |
| OPM and merit-systems capacity | 10 | 2% | Hiring reform and civil service modernization (CAP-9, CAP-11) |
| Integrity-enforcement units | 12 | 2% | FinCEN beneficial-ownership unit (INT-9), DOJ FARA unit (INT-11), Office of Government Ethics (INT-1, INT-3, INT-4, INT-6, INT-13), SEC compliance (INT-15); about $5B, $3B, $2B and $2B |
| EAC | 3 | 0.5% | Administers DEM-1's federal floor and DEM-11's funding formula |
| FEC | 3 | 0.5% | INT-7's restructured enforcement bureau |
| FEMA | 8 | 1.3% | Cabinet-level FEMA, the mitigation set-aside, the Universal Survivor Application and NFIP administration (CLI-7) |
| EPA (air office) | 5 | 0.8% | Vehicle and power-sector standards under the restored Clean Air Act authority (CLI-4) |
| DOE (loan and grid offices) and FERC | 4 | 0.7% | CES administration with EIA (CLI-3), plan-selected transmission and the 45X expansions (CLI-5), the grid statute (CLI-6). FERC is mostly fee-funded through annual charges |
| NLRB | 4 | 0.7% | The PRO Act's caseload and the post-*Slaughter* enforcement design (LAB-1, LAB-2) |
| DOL Wage and Hour Division and OSHA | 6 | 1% | The living wage (LAB-4), the heat standard (LAB-6), wage-theft and misclassification enforcement (LAB-7) |
| FTC and DOJ Antitrust | 3 | 0.5% | Merger law, platforms, non-competes and junk fees (COM-1 to COM-5), for the part COM-2's higher merger fees do not cover |
| Immigration court administrative division | 0 here | — | Funded in CRT-5 (about $0.03T); not counted twice |
| Unallocated reserve | 37 | 6.2% | For the batch 4 agencies (AI, immigration, rights, national security). The batch 4 files propose about $31B of it (USCIS asylum, civil-rights offices, CAISI, ATF/NICS, State), pending Espen |
| **Total** | **600** | 100% | Range follows CAP-7S's $0.45-0.75T pro rata |

**The reserve.** The reserve holds **$37B for batch 4** (AI governance, immigration delivery, state capacity, national security), and the batch 4 files propose $31B of it, pending Espen. If batch 4 needs more, D9 lets the line rise, with the sustained part paid for at maturity under D4-B. The other route — trimming, starting with the FTA overlap and the NOAA placeholder — is the fallback.

**Overlaps to check before anyone relies on these numbers.** The line is meant to be additive only where the program row does not already include its own administration, and the source files do not say:

- **IRS and REV-G8.** The revenue base counts $0.4T of restored enforcement. If that figure is net of the enforcement spending, the IRS allocation here is double-counted; if it is gross, this line is the cost of earning it. Unchecked.
- **CMS, HUD, Education, USCIS against their program rows.** HLT-3, HOU-1 to HOU-6, FAM-4 and E11 may each already include administration. Unchecked. HOU-4 explicitly includes housing agencies' administrative fees, which are local, not HUD's.
- **FTA against Moving America.** The Moving America plan funds transit through its own trust-fund and reconciliation acts. The $30B here should be cut to zero unless it pays for staffing the Moving America figures do not.
- **FTC and DOJ Antitrust against COM-2.** COM-2's higher merger fees (about $0.004T, estimate) fund most of the enforcement increase; the $3B here is only for what the fees miss. If the fee schedule is raised further, cut this line.
- **FEMA against CLI-7.** CLI-7 is unscored; when it is scored, check whether its figure includes FEMA's own staffing.
- **CDC and NOAA** are named in D9 but nothing in the project sizes their need. CDC holds a $15B placeholder, tied to NSC-8. NOAA's $40B is the largest allocation with the thinnest basis: its one dependency is flood mapping for CLI-7 and CLI-8. It is the next candidate for the same review.

**Statutory floors and funding.** Draft staffing floors after a comparable staffing baseline and workload estimate exist. A floor can constrain staffing decisions but does not itself supply budget authority or secure operations through a funding lapse. Pair any floor with legally available funding and duties; assess enforceability separately. See the CMS review's GAO appropriations-law reference.

**Instrument question (open; target decided Oct 21).** Target R1 direct multi-year appropriations for all CAP-7S funding, available immediately on enactment. This is a policy direction, not certification that every provision passes Byrd or jurisdiction tests. Check each function, including SSA administration versus Title II benefit changes. CAP-7's permanent instrument remains a separate question. See index/capacity-funding-model.md for availability versus cash.

**Cost.** CAP-7S about $0.60T (lifetime working total, immediately available on enactment; old FY2030-35 cash path provisional; D4/C42 financing) plus CAP-7 about $0.49T in the window and about 0.12% of GDP a year after it (estimates). Ledger cut C17 (holding the line to $0.5T) is declined (Decision Brief 2).

### CAP-8. Schedule Policy/Career prohibition

**Design.** Statutory prohibition of Schedule Policy/Career (the rebranded Schedule F). OPM published the final rule Feb 6, 2026, effective March 2026, covering an estimated 50,000 positions or 2% of the workforce, with the President placing positions by executive order (CRS LSB11412; Federal Register).

**Two instruments, in order.** The executive rescission is EXE-17 (day one, reversible); the statutory prohibition is this row (durable). The rule exists now, so the 2029 bill is a repeal-and-prohibit, not a prophylactic — it should be drafted against the actual rule text.

### CAP-9. Civil service modernization

**Design.** Real performance management paired with real political insulation. Post-*Slaughter*, insulation rests on career-employee protections and on structure, not on for-cause removal of officers — career civil servants are not the officers Slaughter addressed, which is the distinction the drafting must hold onto.

**Why both halves.** A defense of the civil service that offers no answer on performance loses the argument in public. The trade is explicit: stronger protections against political removal, in exchange for a management system that can actually address poor performance.

### CAP-10. Successor architecture

**Design.** Successor architecture for demolished development functions (USAID; its funding sits inside CAP-7) and for education functions, with enforcement separated from policy. Pairs with ledger F4. Drafted in opposition under CAP-18.

### CAP-11, CAP-12. Hiring and technology

Federal hiring reform — time-to-hire targets, direct-hire authority, salary flexibility — is the row that determines whether CAP-7's money becomes people within the window. Technology procurement reform and in-house engineering capacity are second-wave but gate the IRS and CMS builds that batch 1 depends on.

### CAP-13. State and local capacity grants

**Design.** Implementation grants to state and local governments, because implementation is where federal policy dies (design rule 5). Child care slots, election administration, housing production and transit all run through governments that are not the federal one.

**Cost.** About $0.03T, range $0.02T to $0.05T (estimate; unscored). **Flagged:** no source in the project sizes this.

### CAP-18. Draft in opposition

**Design.** All successor legislation, the day-one executive bridge and the express-delegation templates (CRT-8) drafted during 2027-28, so text exists on day one. ✔ at 51 because it needs no votes.

**Why it is in a domain file and not just a plan.** The express-delegation templates are the single largest drafting task in the agenda — every statute the trifecta passes needs one — and there is no version of the 2029 calendar in which they can be written in 2029.

## Survival at 51 (D1 stress test)

| Tag | Items |
| --- | --- |
| ✔ survives | CAP-16 (House rules), CAP-17, CAP-18 |
| ◐ needs a D2 path | CAP-1 to CAP-15 |
| ✖ | none |

The annual-appropriations rows (CAP-1, CAP-2, CAP-3, CAP-7, CAP-13) are ◐ because annual appropriations still face a 60-vote Senate in practice. CAP-7S targets R1 but remains ◐ pending Byrd/jurisdiction review; the vote model's R1 routing is conditional, not a survival-at-51 certification. That is the strongest argument for the mandatory-funding question flagged under CAP-7: if CAP-7 can be made Byrd-eligible, the agenda's single largest capacity item moves from ◐ to ✔.

## Dependencies

- **D9:** CAP-7S and CAP-7 are D9's line. D9's agency list names every agency in the table above; the batch 4 agencies are still to be added.
- **D2:** CAP-1 to CAP-15.
- **D4 (D4-B):** CAP-7S is finite multi-year funding fully available immediately on enactment, with D4/C42 financing and written agency return cases. FY2029 cash and envelope treatment must be reconciled; existing fiscal results use the interim cash proxy, not a validated accelerated spending path. CAP-7 is permanent, so it is counted in the general-fund claims that are paid for at maturity (FY2040 and every later year). A larger line for batch 4 adds to those claims.
- **Courts file:** CRT-8 (express delegations) is unenforceable without CAP-1 to CAP-3; CRT-14 is CAP-6's workload; CRT-5 funds the immigration court's administrative division.
- **Executive power file:** CAP-8's statutory form pairs with EXE-17's rescission; CAP-10 depends on EXE-3 for the money to reach successors.
- **Integrity file:** CAP-1 and CAP-14 are packaged with INT-1; INT-7, INT-9, INT-11, INT-13 and INT-15 draw on the integrity-enforcement allocations above.
- **Democracy file:** the EAC and DEM-11 draw on the allocation above.
- **Batch 1 files:** IRS (FAM-1 monthly payments), SSA or a leave office (FAM-3), HHS and the states (FAM-2), CMS (HLT-1 to HLT-3 auto-enrollment). Every one of those felt dates assumes CAP-7S, CAP-7 and CAP-11.
- **Batch 3 files:** domain-climate.md (FEMA, EPA, DOE and FERC, NOAA, IRS and SSA for the dividend), domain-housing.md (HUD), domain-labor.md (NLRB, Wage and Hour, OSHA), domain-competition.md (FTC and DOJ Antitrust, mostly fee-funded under COM-2).

## Design-rule check

| Rule | How this file meets it |
| --- | --- |
| Reciprocity | CAP-4's penalty falls on the Congress that failed, whichever party holds it; CAP-9's trade (insulation for performance management) is one we would accept in the minority |
| Durable instruments | CAP-7's statutory staffing floors; CAP-8's statute behind EXE-17's order; the open question of making CAP-7 mandatory is the file's biggest durability lever |
| Legibility | Low, and unavoidable: nobody experiences "agency capacity." It becomes visible only when it fails — a CTC check that does not arrive |
| Pairing | CAP-1 and CAP-14 with INT-1, the clearest pairing trade in the agenda |
| Supply with demand | The file's whole purpose: capacity before the transfers that raise demand on it |
| Capacity first | This is the capacity file; CAP-7S and CAP-7 name every agency batches 1 to 3 depend on, with an allocation for each, and a reserve for batch 4 |
| Write for this Court | CAP-9 keeps career protections distinct from the officer-removal question Slaughter decided |
| One version per policy | CAP-4 carries the Merkley-Daines fast track as a named option; permitting is a pointer, not a second version |
| Every number has a basis | Tagged; the per-agency split, CAP-13 and the 1979/1992 staffing baselines are the weak ones, and the first two have no source |

## Open items

1. **R1 instrument review for CAP-7S; permanent instrument for CAP-7.** Immediate multi-year availability for all surge funding is decided; Byrd/jurisdiction checks, SSA scope and any companion route remain open.
2. **Rebuild CAP-7 bottom-up.** The per-agency allocation is a top-down, unsourced set of increments over baseline. Next step (Espen's request): research each agency's current and historical funding and staffing, reason about what rebuilding and expanding capacity requires, and take the domain files as inputs. It also has six unchecked overlaps (IRS with G8; CMS, HUD, Education and USCIS with their program rows; FTA with Moving America; FTC and Antitrust with COM-2's fees; FEMA with CLI-7; CDC and NOAA placeholders).
3. **Envelope size for batch 4.** The reserve holds $37B; the batch 4 files propose $31B of it (pending Espen, then D9's list is extended). If batch 4 needs more, the line rises, paid for under D4-B, or existing lines are trimmed (NOAA next).
4. **CAP-13 is unsourced.**
5. **Staffing baselines are counted differently by CRS and Brookings** — pick one method for the findings record.
6. **CAP-7S and CAP-7 remain provisional** under D9 until the whole agenda is priced. C17 is declined (Decision Brief 2). The surge's shape and the sustained level (0.12% of GDP, against 0.10% or 0.148%) are **Espen's accepted working figures**; the bottom-up review (item 2) may revise both.
7. **CAP-13 has no ledger row** (see crosswalk); add it in the ledger input tables, not the ledger.
8. **CMS cash costing and overlaps.** Use the annex and sources/health-cms-implementation-cost-register.csv to identify embedded HLT administration, existing balances, FY2029 obligations/outlays, state shares and recurring operations. Blank amounts mean unpriced, not zero. No allocation increase, headcount floor or provider-participation rule is adopted.

## CMS implementation annex (Oct 21, approved direction)

The review's recommendations are accepted for implementation. CMS's $50B surge allocation and exact 1/12 share of sustained funding remain provisional. The baseline implied ~$40.8B sustained funding over 2030-39 and ~$5.4B/year around FY2040 (derived estimates). The old ~$90.8B combined window total must be restated once FY2029 outlays are priced.

### Delivery responsibilities and gates

| Health row | Proposed functional owner and work | Readiness target/evidence | Cost packages |
| --- | --- | --- | --- |
| HLT-1 | CMS marketplace/Medicaid teams, states, Treasury/IRS: restoration, eligibility, subsidy recalculation, notices and assistance | Plan year 2030; payment and eligibility changes tested during 2029 | CMS-IMP-01, 02, 11 |
| HLT-2 | Medicare operations/contractors: cap accumulator, claims edits, provider onboarding, vision/hearing/dental and premium coordination | Physician pay on adopted schedule; cap/vision/hearing 2031; dental from 2033; claims and access tests | CMS-IMP-03, 04 |
| HLT-3 | CMS public-plan team, marketplaces, states, Treasury/IRS: pricing, participation, payments, enrollment, assistance and appeals | Public plan 2031; auto-enrollment 2032; payment/provider tests before coverage and data/correction tests before defaults | CMS-IMP-05, 06, 07 |
| HLT-4 | CMS/state Medicaid teams, relevant HHS partners for other safety-net functions | From 2030; state plan/waiver, HCBS, casework and payment readiness | CMS-IMP-02, 08 |
| HLT-5 | Proposed CMS/HHS lead with Labor/Treasury and competition authorities; jurisdiction to be settled | Adopted phase-ins from 2031; price data, applicable plans, complaints and enforcement specified | CMS-IMP-09 |
| HLT-6 | Medicare payment, clinical/actuarial, drug-pricing and integrity teams | Separate payment-rule changes from audit recoveries; cost implementation and verify savings delivery | CMS-IMP-10, 12 |
| Shared | Federal engineering, acquisition, legal, cyber, accessibility and service ownership | Start upon enactment; modular delivery, named integration owner and independent testing | CMS-IMP-01, 11, 13 |

These are functional assignments for costing, not an agency reorganization. Gates require reporting and remediation, not silent benefit delays or indefinite executive discretion to withhold benefits.

### Cost and funding rules

Use sources/health-cms-implementation-cost-register.csv as the hand-written work register. Blank costs mean unpriced, never zero. Each package needs a baseline-resource inventory, HLT overlap finding, gross/net cost, price basis, federal/state share, obligation/outlay years and one ledger owner before any amount is added to totals.

Separate finite federal setup (CAP-7S), continuing federal staff/contracts/hosting/service (CAP-7 or a reconciled HLT allowance), state implementation and matching (HLT-1/4), and other HHS/partner-agency duties. Do not charge a cost to CAP, an HLT score and state matching at the same time. Existing restricted balances are not automatically available for repurposing.

Begin leadership, hiring/acquisition, state readiness and restoration work in FY2029 from the immediately available full multi-year surge. A separate extra CMS bridge appropriation is not the default. Size FY2029 use within the provisional allocation and disclose it outside the 2030-39 display. The old cash profile is not a revised acceleration score.

Automatic enrollment needs eligibility/data authority, premium/default rules, other-coverage coordination, notice, correction, opt-out, appeal and non-digital assistance. Public-option provider participation, commercial-plan jurisdiction and staffing floors remain explicit design/drafting questions.

### First costing priorities

1. Establish a constant-scope CMS baseline and existing obligated/unobligated resources by purpose and expiration.
2. Resolve HLT-1/3/4 administrative-score boundaries and state/federal shares.
3. Price FY2029 preparation and its continuing commitments; revise the lifetime cash path without normalizing away pre-window costs.
4. Build staffing by function and retained-government versus contracted duties; the review's FTE scenarios are sensitivities, not targets.
5. Cost claims/payment, provider onboarding, drug pricing and audits alongside enrollment.
6. Re-run D4 on the revised cash path, preserving HI reserves and avoiding duplicate savings.

Evidence and limitations: sources/health-cms-capacity-review-2026-10-21.md. No allocation increase, headcount floor, provider mandate or extra appropriation is adopted by this annex.

## Sources

- staging/unified-reform-inventory-current.md, sections 8 and 9, and its cited sources.
- sources/courts-rebalancing-the-three-branches-2026.md, Key Finding 5 and Reform 20: the CRS and Brookings staffing figures, OTA's budget and staff cap, the Modernization Committee's unanimous endorsement, the Pascrell leadership-staff figure, and the legal-culture program.
- frameworks/instruments-and-consequences.md: #9 (the budget-process penalty), #15 (staffing packaged with the stock ban).
- frameworks/radical-means-moderate-ends.md: civil service modernization as a prerequisite for every ramp time.
- OPM final rule, Federal Register Feb 6, 2026; CRS LSB11412 (Mar 26, 2026).
- index/2029-trifecta-master-ledger.md: rows A1 (CAP-7, CAP-7S), DEM12, DEM13; cuts C17, C26, C27, C42.
- governing/project-2050-governing-decisions.md: D9 (the envelope and the agency list), design rules 2, 5 and 6.
- Batch 3 domain files (domain-climate.md, domain-housing.md, domain-labor.md, domain-competition.md): the batch 3 agency needs and their proposed allocations.

## Health acceleration dependency: October 23 development direction

Developing 2029 restoration and January-2030 HLT-2 hearing/vision requires a dated CMS/state/provider work plan, not a new title-wide lag. See [canonical health alternatives](domain-health.md#earlier-delivery-alternatives-development-approved-october-23) and [the evidence assessment](../sources/health-2029-restoration-and-2030-medicare-option.md). Identify FY2029 hiring, rulemaking, contractor/claims changes, testing, supplier participation, outreach and state costs. Separate legal availability, obligations and cash; reconcile embedded HLT administration against CAP-7S/CAP-7 before adding costs. Current allocations and outlay proxies do not certify the accelerated launches. No capacity allocation, spending profile or health date is changed by this approved development work.


## Health bridge follow-up: October 24

Use the [completed health bridge](../sources/health-delivery-resource-bridge.md) and [decision packet](../sources/health-hearing-vision-decision-packet.md) to price existing CMS-IMP work, not repeat CMS-IMP-02. Compare MA-contract changes and a possible Original-Medicare payment bridge, including MAC claims, supplier access, notices, appeals and existing supplemental obligations. FY2029 cash, marginal costs and CAP/HLT overlap remain unpriced. This research adds no appropriation, allocation, headcount or spending profile.


**PR #22 accepted allocations, October 26.** The historical proportional table above is superseded for IRS, CMS, HUD and ED by [the component review](../sources/capacity-recovery-budget-review.md). Within unchanged $300B surge/$300B sustained envelopes, working $B allocations are IRS 9/92.4, CMS 8/14.5, HUD 2.8/10.4 and ED 2.3/8.3. Rounded remainders are 277.9/174.4. IRS includes +24,000 enforcement FTE; receipt-risk allowance rises to $250B. PHA fees belong to housing, state Medicaid and public-plan operations to program rows, meals/care to USDA/HHS, and IES/NCES to EDU-8. Boundaries do not prove every program-row cost is priced. FY2029 four-agency cash estimate is $0.3–2.2B; all-agency adequacy of $10B remains unresolved. Unpriced functions remain explicit in the review.
