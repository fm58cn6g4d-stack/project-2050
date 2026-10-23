# Calendar C: October 23 development case

**Status:** development authorized by Espen; this is a planning specification, not a validated leadership schedule or a model-input change. Source baseline: claude/pensive-mendel-g1lwl5 at e15c5c4a711b4cd2b482bac8300de45f2e08721f. Governing D1/D2/D5/D8 and governing/project-2050-post-pilot-decisions.md control the direction.

## Fixed directions and distinct clocks

R1 targets administration weeks 3–4; February preferred and March latest. It is the affordability/restoration package, with visible household delivery and preparation for longer reforms. D2-F is a first-Senate-week action, not an administration-week-3 action. DEM-1 takes the floor after R1 signature/benefits announcement, without a compulsory midyear delay, and targets spring-2030 enactment within mid-2030. SS remains spring 2030, with its closer open. R2 targets summer 2029 on the FY2030 resolution; R3 remains summer 2030.

MOV-31 is considered in the second Congress seated January 2031 for FY2032–36. Its assumed predecessor expiry at end FY2031 is a planning premise requiring verification/continuity planning, not a verified claim that a future authorization has passed. A late authorization may use an explicit extension. Do not accelerate MOV into 2029–30 merely to satisfy general first-Congress wording. The separate 2029/2030 transportation reconciliation components remain. Second Congress 2031–32 differs from the DEM-3/4/9 second-trifecta package in 2033.

## Accounting and full-scope inventory

The existing F case is 172 = 51 reconciliation + 4 rules + 117 regular-order days against 163. MOV is already excluded. New CLI-3/6 net savings s and additional reserve/capacity b remain unknown: C = 172 − s + b. Retain CLI-7/8 fallback; count earlier passage only for enacted complete coverage. No extra credit for existing C23–C28 mergers/fast tracks/nomination measures.

The following inventory reproduces the unchanged input targets for traceability; they are **not approved new reservations**. Raw floor inputs pass through ledger-paths.py’s F minimum and fast-track treatment. Durations are legacy planning estimates, not validated procedural estimates. The full 21-bill scope remains visible:

| Bill | Legacy modeled F days | Existing input target | Scope |
| --- | --- | --- | --- |
| HLT-3 | 8 | 2030-02 | Health III: Public option guarantee with auto-enrollment (carries HLT-5) |
| SS-1 | 8 | 2030-06 | Social Security: solvency first, targeted increase (D8 baseline, SS-1 to SS-4) |
| CLI-3 | 6 | 2030-01 | Clean Energy Standard in statute plus AAJA fixes (Sec. 1401 override, Judgment Fund cap, 401 and rail fixes); carries CLI-4 Clean Air Act restoration |
| CLI-6 | 4.5 | 2030-05 | Grid and utility statute (transfer minimums, PBR standard, utility lobbying ban, RTO governance, large-load floor extension) |
| CLI-7 | 4.5 | 2030-05 | Disaster response and flood insurance, with CLI-8 climate risk (cabinet FEMA, mitigation set-aside, NFIP with premium support, floodplain standard) |
| HOU-7 | 4.5 | 2030-03 | Housing floor bill: zoning conditions on new transportation and CDBG money (HOU-6), institutional-investor limit made permanent (HOU-7) |
| LAB-1 | 8 | 2030-03 | Labor bill: PRO Act core, enforcement after Slaughter, sectoral boards, living wage mandate, heat standard, wage theft (LAB-1 to LAB-4, LAB-6, LAB-7) |
| LAB-9D | 2 | 2029-09 | National service authorization (LAB-9D): a bipartisan regular-order bill at about LAB-9B's scale, with mixing kept |
| COM-1 | 5 | 2030-03 | Competition bill: merger law, enforcers and HSR fees, platforms, non-compete ban, junk fees, CFPB durability (COM-1 to COM-6; E10 merged, C24) |
| IMM-1 | 12 | 2029-09 | Immigration bill: tiered legalization, backlogs and H-1B fee, asylum processing, enforcement priorities and detention cap, birthright codification, USCIS delivery (IMM-1 to IMM-6) |
| AI-1 | 5 | 2030-05 | AI bill: frontier transparency, floor preemption, pre-deployment evaluation, government use, platform transparency, public media and FOIA (AI-1 to AI-3, AI-5, AI-7, AI-10); carries EDU-8's education rules |
| DEM-1 | 10 | 2029-07 | Electoral and civil-rights package: Freedom to Vote floor, John Lewis VRAA, Callais response, 6:1 match (INT-5B), DISCLOSE (INT-2); carries DEM-2, DEM-12, DEM-13 |
| DEM-5 | 5 | 2029-03 | D.C. statehood |
| DEM-6 | 4.5 | 2029-03 | Puerto Rico Status Act (with DEM-7 territorial and tribal representation) |
| INT-1 | 1 | 2029-05 | [Fast track C27] Government ethics and anti-corruption (stock ban, divestiture, IGs; INT-1, INT-3, INT-4, INT-6) |
| CRT-P1 | 6 | 2029-07 | Courts package: term limits, phased judgeships, random assignment, ethics (DEM6 merged, C11) |
| EXE-1 | 6 | 2029-05 | Executive-power guardrails: emergencies, impoundment, Insurrection Act, pardons, tariffs, war powers (DEM9 merged, C10) |
| CAP-8 | 2 | 2029-06 | [Fast track C27] Civil service modernization, successor agencies and congressional capacity (CAP-1 to CAP-6, CAP-8 to CAP-12, CAP-14, CAP-15; DEM12 merged, C26); proposed to carry EDU-6's Education Department protections |
| RTS-1 | 4.5 | 2029-04 | Reproductive Freedom Act (statutory right, medication abortion floor, contraception, IVF, travel, EMTALA); RTS-2 riders via appropriations |
| RTS-3 | 4.5 | 2029-06 | Equality Act with civil-rights enforcement restoration (RTS-3, RTS-4) |
| SAF-1 | 6 | 2029-11 | Safe Everywhere Act (rules): clearance, standards and liability, background checks, pretrial, public-servant protection, fraud duties, sentencing and cannabis (SAF-1, 2, 5, 7-9 rules, SAF-11; S4 merged, C25) |

The table totals 117 modeled days across 21 bills. A reserved earlier SS place must not conceal the bill it displaces. The script’s target/month ordering is not a dependency-based operational calendar.

## Work packages to turn C into a usable calendar

| Work | Product and dependency | Decision gate |
| --- | --- | --- |
| C-01: R1 transition package | Clause/instruction/score map; bicameral text; authority-to-award-to-household milestones for health, CTC, transport and surge | Verify available FY2029 slot and text-specific eligibility. No invented cash profile or service launch. |
| C-02: successive resolutions | FY2029 R1 completion then FY2030 instruction/committee plan; pre-October R2 consideration | Budget-specialist confirmation of instructions, allocations and points of order before the next framework supersedes the one R1 relies on |
| C-03: protected deadlines | DEM signature dependency; state mapping/remedy milestones; spring SS reservation; House/conference work | Demonstrate that reservation is feasible, disclose displacement and retain D8 closer as open |
| C-04: merger comparison | CLI-3/6 combined versus separate scope, jurisdiction, amendment exposure, coalition and bicameral work | Adopt only after time saving and passage/durability tradeoff are explicit; no assumed six-day combined bill |
| C-05: disaster precursor | Exact earlier enacted CLI-7/8 coverage and residual statutory work | Keep full fallback unless actual scope eliminates it; no hoped-for 4.5-day saving |
| C-06: full capacity | Explained 163-day basis, appropriations, nominations, NDAA, other business, conference and disruption; every inventory row accounted for | b unknown, not zero; identify additional days or return specific scope choices to Espen |
| C-07: second-Congress MOV | Predecessor authority/expiry, continuity and coalition; committee/House/conference plan; data/privacy clauses needed before earlier operations | MOV floor duration m₂ and contingency unknown; do not assume a first-Congress vote or free second-Congress passage |
| C-08: synchronized inputs | Approved windows/dependencies and scenario representation, then generators and diffs | No model input changed in this pass. Do not guess a summer month, merger saving, reserve or launch merely to satisfy schema. |

These are local work labels, not new policy IDs or supported duration estimates.

## R1 contingencies and benefit delivery

May–June R1 delays authority for restoration, CTC preparation, transport and surge execution; consumes time needed for summer R2; and compresses DEM’s after-signature route. Prepare a benefit-by-benefit recovery path and escalation at a March miss. Goodwill is an intended strategic benefit, not an empirical forecast. A lost FY2029 opportunity is a distinct scenario: do not repeat the old exactly-one-year CTC delay as a validated consequence of any slip.

## Primary-source check and limitations

[2 USC 631](https://uscode.house.gov/us/usc/119-118/t2/s631/) places reconciliation work before October 1; [632(a), (b)(2)](https://uscode.house.gov/us/usc/119-118/t2/s632/) addresses the coming fiscal year’s resolution and instructions; [641](https://uscode.house.gov/us/usc/119-118/t2/s641/) sets the committee/reporting route and OASDI prohibition. This supports pre-FY2030 enactment in principle, not clearance of a bill. [644](https://uscode.house.gov/us/usc/119-118/t2/s644/) still governs extraneous matter. OLRC text inspected October 23; official CRS R44058 retrieval failed. Exact predecessor-reauthorization enactment/expiry was not independently verified in this revision.

Sources: governing decisions D1/D2/D5/D8; democracy DEM-1F; transportation draft/calendar source; index/data/inputs/ledger-bills.csv; ledger-paths.py and votes-model.py; saved legislative-calendar reconciliation and post-pilot brief. No current floor manager, specialist, House calendar or negotiated coalition estimate was obtained. No numerical input or generated output changed.
