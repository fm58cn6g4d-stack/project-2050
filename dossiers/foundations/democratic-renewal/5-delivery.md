# Democratic renewal: delivery

Role: section 5 of the democratic renewal foundation. It says who runs each of the 137 provisions in `4-specification.md` (IDs in `provisions.json`), what capacity each body needs, the timeline from January 2029 with the preparation before it, what happens when delivery fails, what states and local election offices do, and how the provisions reach rural places. This foundation owns the plan's cross-cutting state capacity (`charter/PLAN.md` 3.1), so part 3 says how that capacity reaches the other flagships: hiring, payment systems, records, remedies, and the seams with EXE-3 and EXE-18. Status: **draft** (stage F, step 5), on `DEC-2026-11-17-40` to `-99`, the design lens (`DEC-2026-11-09-13`), existing machinery first (`DEC-2026-11-13-08`) and the rural direction (`DEC-2026-11-09-26`). Nothing here is booked or changes a model input. Costs are section 6's (`6-cost.md`); figures here are section 4's and part G's.

## How to read this section

- **Status labels** follow section 4: *decided*, *working choice* (set here so delivery is complete; changeable without reopening a decision) and *provisional* (drafted on the recommendation under the overnight relay and listed under "Questions for Espen").
- **Four provisional fixes to section 4.** Delivery showed four places where a provision cannot run as written. Each gets the smallest fix, written into `4-specification.md` and `provisions.json` and marked provisional (part 8): CAP-7.02's start rule, CRT-5.03's transfer of sitting judges, enforcement of the voting floor (DEM-1.13), and a payment deadline for the formula grants (DEM-11.01, CAP-13.01). One delivery choice is also put to Espen: the voting floor's effective dates (part 4).
- **Existing machinery first.** Every row in part 1 names the body and the channel that already exists. The new bodies are few: the immigration court office in the Administrative Office, the judiciary's inspector general, OMB's delivery unit, the statute-tracking office and a re-funded Office of Technology Assessment. Everything else is an existing body with a new duty or more staff.
- **Evidence.** Tags point to `evidence.json`; this section adds EV-DEM-345 to 350 (sources SRC-5399 to 5404). Legacy figures are restated with their file and line and weighed as evidence, not defaults (`DEC-2026-11-13-15`).

## 1. Who runs what

Every provision appears once below, by the body that runs it. "Channel" is the existing machinery it uses.

### A. Representation, elections and civic life (DEM)

| Body | What it runs | Provisions | Channel it uses | What changes for it |
| --- | --- | --- | --- | --- |
| **States' chief election officials and local election offices** | Registration from records and its notice and decline; same-day, online and preregistration; early voting; mail voting and drop boxes; identity by list or statement; the citizenship check's flags; notice and cure; list maintenance; paper ballots and risk-limiting audits; certification; the voter card's mailing; restored rights' registration; registration records used only to run elections, under their own privacy law and CAP-19.02's rules for federal records | DEM-1.01, 1.03 to 1.12, 1.14, DEM-12.01 | The statewide voter registration list every state already keeps under the Help America Vote Act, coordinated with other state databases and matched with the motor vehicle authority, which has an agreement with the Commissioner of Social Security [EV-DEM-345]. Most states already offer automatic registration, just over half same-day registration, two-thirds drop boxes and three-quarters a chance to cure [EV-DEM-346] | From opt-in registration to registration from records; one federal floor for every state; a recurring grant (DEM-11.01) for the new duties, which have never had recurring federal money |
| **Election Assistance Commission** | The federal form; voluntary voting system guidelines and equipment certification; DEM-11's formula and the equipment fund; commission start-up grants; the voter card's federal standard | DEM-1.15, DEM-11.01, 11.02, DEM-2.05 (grants), DEM-1.07 (standard) | HAVA's grant machinery: over $1 billion of election security grants distributed since 2018 [EV-DEM-171] | Rebuilt to five commissioners with a quorum that holdovers count toward, and an executive director who keeps the form, the guidelines and the formula running without a quorum (DEM-1.15). It has had no commissioners since July 9, 2026 [EV-DEM-020] |
| **SSA, USCIS (SAVE) and the State Department's passport records** | Answers to the citizenship check, yes or no, on a flag for review | DEM-1.08 | The SSA agreements HAVA already requires [EV-DEM-345]; CAP-19.02's logging and no-enforcement rule once it is law | A records answer replaces any document a voter would bring |
| **The plan's benefit agencies** (IRS, SSA, the state agencies running school meals, child care, Medicaid and the marketplace; CMS for the single plan; the national service agency; USDA Rural Development's front doors) | Registration agencies under the National Voter Registration Act, passing the citizen-of-voting-age record only | DEM-1.02 | The NVRA's agency registration, extended to the plan's new contact points | A data feed to the state, not a new desk task; a household record passes only the citizen of voting age |
| **USCIS** | Registration at naturalization | DEM-1.02 (IMM-5.05) | Naturalization ceremonies | One form at the ceremony |
| **Bureau of Prisons and state corrections** | The restored-rights notice and form on release; access for people held before trial | DEM-12.02 | Release processing | One notice |
| **Labor (Wage and Hour Division)** | Paid time to vote | DEM-13.01 | Wage and Hour's complaint process | A small new rule to enforce |
| **GSA** | The transition trigger | DEM-1.12 | Presidential transition ascertainment | A set rule replaces discretion |
| **DOJ (Civil Rights Division), the D.C. district court** | Preclearance under Title II; suits under III-A and III-B; enforcement of the floor (DEM-1.13, provisional) | DEM-1.16 to 1.19, DEM-1.13 | The Voting Section's existing work | Coverage recalculated each year from a rolling record |
| **Federal courts** (three-judge district courts; direct appeal) | Map challenges under DEM-2; certification suits; relief beyond the parties | DEM-1.13, DEM-2.01 to 2.04, 2.06, DEM-1.12 | 28 U.S.C. 2284 [EV-DEM-344] | Fast-track schedules tied to filing deadlines |
| **State legislatures and commissions** | The congressional maps under the ban and criteria; the multi-member option where a state chooses it | DEM-2.01 to 2.03, 2.05, DEM-4.01 | Each state's redistricting process | Published maps, data and reasons before adoption |
| **DOJ, with SAF-8's design** | Election-worker protection (rider) | DEM-1.20 | SAF-8's (public safety) | Rides the democracy act |
| **FEC** | Synthetic-media disclosure in political ads (rider) | DEM-1.21 | AI-8's design | A new disclaimer rule |
| **Congress, with the Census Bureau and the Architect of the Capitol** | The 2031 House review; the chamber's build report by 2030; the 2033 decisions; the presidential method; the amendment | DEM-3.01, DEM-4.02, DEM-9.01, DEM-8.02 | Apportionment after the census | The chamber seats about 448 (legacy, `domain-democracy.md`:132) |
| **Congress** (statehood and status acts); Puerto Rico's election commission | D.C. admission; the binding plebiscite; territories, tribes and the admission procedure | DEM-5.01, DEM-6.01, DEM-7.01 | Admission acts; the commission's elections | CBO scores statehood's fiscal effect before the vote (DEM-6.01) |
| **State campaigns** (outside government; no federal body) | The compact; fusion and ranked choice; the initiative; punitive preemption | DEM-8.01, DEM-10.01, DEM-19.01, DEM-20.01 | State legislatures and ballots | None federally |
| **Education** | Civic education grants | DEM-16.01 | Formula grants to state education agencies | Measures on participation, not a test |
| **IMLS and Interior** | The libraries and public space capital fund; the permanent library line | DEM-17.01, 17.02 | IMLS's Grants to States and Interior's outdoor recreation grants | IMLS's line grows 2.8 to 5.6 times [EV-DEM-338] |
| **Congress's committees, OMB and agencies** | The three national assemblies and the duty to answer | DEM-18.01 | Committee referral; OMB guidance | A written answer within 180 days (working choice) |
| **Congress** | The timing rule | DEM-1F.01 | Floor schedule | — |

### B. Money in politics and ethics (INT)

| Body | What it runs | Provisions | Channel it uses | What changes for it |
| --- | --- | --- | --- | --- |
| **FEC** | The 6:1 match and its fund; DISCLOSE; the coordination presumption; the foreign-owned ban; candidates' tax returns; contractor receipts matched and refund notices | INT-5.01, INT-2.01, INT-8.01, INT-16.01, INT-6.01, INT-14.03 | Its reports system; the presidential fund's payment process; Treasury pays from the fund | Five members, quorum of three, a citizen suit at 120 days (INT-7.01). It had two of six seats in March 2026 [EV-DEM-031] |
| **FEC (structure)** | The restructure itself | INT-7.01 | EXE-9's template | Independence by structure, not removal protection |
| **SEC** | Shareholder authorization, board votes, quarterly reports, institutional investors' votes | INT-15.01 | Exchange Act reporting | Fee-funded staff (legacy, `capacity-recovery-components.csv`:136) |
| **House and Senate ethics offices; OGE for the executive** | The stock ban: coverage, the three ways to comply, the 1043 certificates, penalties computed from filings, notice, contest and appeal; paid speech and later pay; cooling-off | INT-1.01, 1.02, 1.03, 1.04, 1.05, 1.06, INT-13.01, INT-3.01 | The STOCK Act's periodic transaction reports; OGE's certificates of divestiture [EV-DEM-334]; the chambers' late-fee rules | Automatic, published penalties; OGE's staff rebuilt in the integrity line. OGE's director was removed in February 2025 [EV-DEM-038] |
| **Treasury (IRS)** | The deferral on compliance sales | INT-1.03 | 26 U.S.C. 1043 [EV-DEM-334] | Extended to members |
| **DOJ** | Collection suits after 90 days; willful referrals; FARA with civil demands; lobbying disclosure enforcement | INT-1.04, INT-11.01, INT-10.01 | U.S. Attorneys; the FARA unit | FARA unit staffed in the integrity line |
| **Clerk of the House and Secretary of the Senate** | Lobbying registration on a contacts test | INT-10.01 | The Lobbying Disclosure Act's filings | A new test, same filings |
| **Treasury (FinCEN)** | Beneficial-ownership reporting with carve-outs closed | INT-9.01 | The Corporate Transparency Act's database | Its unit staffed in the integrity line |
| **GSA and agencies' suspension and debarment officials** | Debarment for adjudicated fraud; the pay-to-play bar; contractor identifiers for the match | INT-14.01, 14.02, 14.03 | SAM and USAspending | A bar keyed to FEC records |
| **Federal Reserve** | Officials' financial disclosure | INT-12.02 | Its ethics office | Public filing on the judiciary's rules |
| **Federal courts** | The emoluments cause of action | INT-4.01 | District courts | Private suits |
| **States** | The state track | INT-17.01 | State law | None federally |

### C. Courts and the law (CRT)

| Body | What it runs | Provisions | Channel it uses | What changes for it |
| --- | --- | --- | --- | --- |
| **The judiciary: the courts of appeals, the circuit judicial councils, the Administrative Office** | The immigration court as a unit of the district court; appointment and removal; the appellate panels; the court office; counsel for adults | CRT-5.01, 5.02, 5.04, 5.06, 5.07, 5.08, 5.09, 5.10 | The bankruptcy courts' model [EV-DEM-333]; the Criminal Justice Act's district plans and panels for counsel [EV-DEM-350] | The largest new job in this foundation: about 1,670 judges at peak (CRT-5.06), where the bankruptcy system is the nearest precedent |
| **EOIR (DOJ), until the effective date** | Hiring under IMM-3.08; the transfer of judges, staff, case system and space | CRT-5.03 | EOIR as today | Keeps hiring about 250 a year from FY2030, then transfers on October 1, 2031 (working) |
| **HHS (ORR)** | Children's counsel | CRT-5.08 | Its legal-services contracts | Extended to appointed counsel (immigration's) |
| **Federal courts** | Restored habeas and review; priority for detained cases | CRT-5.05 | District courts and courts of appeals | No fixed deadline on Article III courts |
| **Legal Services Corporation** | Civil legal aid on a published schedule released against grantee hiring | CRT-20.01 | LSC funds competitively selected local providers in designated service areas; it serves no one directly [EV-DEM-349] | The release rule (CAP-7.02's logic) applied to grantees |
| **The President, the Senate, the judiciary** | 71 judgeships in three tranches; the circuit realignment report | CRT-1.01, CRT-13.01 | Nominations; the Judicial Conference | Chambers, staff and space with each tranche |
| **The Supreme Court** | The binding code, recusal reasons, emergency-order reasons, records and cameras, certiorari before judgment, statutory splits | CRT-2.01, 2.02, CRT-4.01, CRT-6.01, CRT-11.01, 11.02 | Its own rules and clerk's office | Publication duties on set clocks |
| **The judiciary's inspector general** (new) | Investigations and published findings | CRT-2.03 | EXE-5's notice-before-removal template | A small new office |
| **The judiciary (financial disclosure office)** | Electronic, searchable disclosure for judges and Justices | INT-12.01, CRT-2.01 | Today's disclosure filings | A searchable system |
| **District courts and circuits** | Random assignment (state and federal action); three-judge courts for district-court suits against federal action beyond the parties; rule challenges in one court of appeals within 60 days, which may vacate; the *Corner Post* fix; remedies after *CASA*; penalties in district court | CRT-3.01, 3.02, CRT-7.01, 7.02, CRT-9.01, CRT-10.01, 10.02 | Clerks' assignment systems; 28 U.S.C. 2284 [EV-DEM-344] | Assignment rules by statute; about 5 to 100 panels a year (part 2) |
| **The President and Senate, the Court; AMD-2** | Term statute, sitting Justices' part, the amendment | CRT-15.01, 15.02, 15.03 | Nominations; senior status | Prospective; first statutory term ends about 2047 |
| **Congress** | Express delegations in every plan statute; the norms; the state track | CRT-8.01, CRT-17.01, CRT-18.01, CRT-19.01 | Legislative counsel with CAP-18.01's templates | Drafting rule |

### D. Congress and the capacity to deliver (CAP)

| Body | What it runs | Provisions | Channel it uses | What changes for it |
| --- | --- | --- | --- | --- |
| **OMB** | The surge and sustained allocations; the release against hiring paths; the contingency; delivery measures; the delivery unit | CAP-7S.01, 7S.02, CAP-7.01, 7.02, 7.03, 7.04 | Apportionment; the budget's agency accounts | A small delivery unit (about 30 to 50 staff, working) stood up January 20, 2029 |
| **Each agency in part G's table** | Its hiring path, its quarterly count, its measures | CAP-7.01 to 7.03 | Its own appropriations accounts | A published path and measures |
| **OPM** | Direct-hire authority, rehiring, special rates, time-to-hire reporting; Schedule Policy/Career's repeal; the performance process | CAP-11.01, CAP-8.01, CAP-9.01 | Its existing hiring authorities and data | A time-to-hire series by agency, quarterly |
| **MSPB** | Fast-track appeals within 120 days | CAP-9.01 | Its appeals process (FY2026: $51.5 million [EV-DEM-347]) | A new clock; not sized in part G (part 3) |
| **GAO; inspectors general** | Yearly audits of hiring paths and contingency releases; following the money | CAP-7.05 | Existing audit work | Staffed from the oversight line |
| **GSA and OMB, with agencies** | The digital service corps and modular procurement | CAP-12.01 | Built on or alongside the existing digital services (18F's roughly 90 staff were eliminated [EV-DEM-102]) | Product teams for the plan's systems |
| **OMB, HHS, USDA, EAC** | State and local implementation grants | CAP-13.01 | Formula by caseload | About $8 billion of surge |
| **Each plan agency; OMB for the statute** | Shared rule 5: records first, the records statute, once-only requests, sample checks, recovery protections, adoption by reference | CAP-19.01 to 19.06 | Privacy Act computer matching agreements; Do Not Pay as a flag [EV-DEM-292]; Treasury's Fiscal Service, which disbursed 87.8% of federal payments in FY2024 [EV-DEM-116] | A once-only service; logs a person can see |
| **OMB, Treasury (Fiscal Service), each paying agency** | Payments continue in a lapse | CAP-4.01 | Fiscal Service disbursement; agencies' lapse plans | Excepted payment staff named in law |
| **House and Senate** | Staff restored to real 1979 levels; the D.C. housing allowance; earmark rules; committee jurisdiction; legislative technology; clerkships and clinics | CAP-1.01, CAP-14.01, CAP-5.01, CAP-16.01, CAP-15.01, CAP-17.01 | The Chief Administrative Officer and the Secretary of the Senate; each chamber's rules | Budgets in the Legislative Branch act |
| **OTA; CRS, GAO and CBO** | A modernized OTA; support agencies toward 1992 levels; CBO's scoring staff | CAP-2.01, CAP-3.01 | OTA was defunded, not abolished (legacy, `domain-capacity.md`:65) | Published hiring paths over FY2030-34 (working) |
| **CRS's legal division or a joint legislative counsel office** | Statute tracking | CAP-6.01 | The Law Revision Counsel's work is the nearest comparator [EV-DEM-339] | A new office of 20 to 40 |
| **Outside government** (preparation) | The successor bills and templates | CAP-18.01 | — | Drafted in 2027-28 |

## 2. Capacity of this foundation's own bodies

| Body | Today | What the provisions add | Where the money is |
| --- | --- | --- | --- |
| **EAC** | $58.9 million in FY2026, a line that appears to include $45 million of election security grants [EV-DEM-347] [EV-DEM-017]; no commissioners [EV-DEM-020] | DEM-11's formula and equipment fund (about $2 billion a year), the restructure, guidelines for paper ballots and audits, the voter card's standard | Staff about $0.4 billion over FY2030-39 (legacy review) [EV-DEM-329]; the grants are DEM-11 program money |
| **FEC** | $80.9 million in FY2026 [EV-DEM-347]; two of six seats in March 2026 [EV-DEM-031] | The match fund's payments, DISCLOSE, the coordination tests, tax returns, the contractor match, citizen-suit notices | About $0.5 billion over FY2030-39 [EV-DEM-329] |
| **OGE and the integrity units** (FinCEN's unit, DOJ's FARA unit) | OGE $23.0 million in FY2026 [EV-DEM-347] | The stock ban's executive side, cooling-off, paid speech; beneficial ownership; FARA | The integrity line, about $2.1 billion over FY2030-39 (surge 0.2, sustained 1.9) [EV-DEM-329] |
| **House and Senate ethics offices** | Their committee staffs | The stock ban's notices, certificates and collection for members, spouses and dependents | Inside CAP-1.01's congressional staffing |
| **The Administrative Office** | $107.0 million in FY2026 [EV-DEM-347] | The immigration court office (records, interpreters, space, filing, education), the appellate panels, adult counsel, the judiciary's inspector general | The court's structure, about $3-10 billion over FY2030-39, unbooked (CRT-5.09); the judges and counsel in IMM-1 |
| **LSC** | Funds local grantees; 134 programs in 812 offices with about 4,591 attorneys in 2015, the latest count in the register [EV-DEM-349] | A schedule released against grantee hiring | Unbooked, unsized (CRT-20.01) |
| **OPM and MSPB** | OPM's discretionary $418.2 million in FY2026 (legacy, `capacity-recovery-components.csv`:60); MSPB $51.5 million [EV-DEM-347] | Hiring tools and the time-to-hire series; Schedule Policy/Career's reversal; fast-track appeals | OPM about $1.3 billion over FY2030-39 [EV-DEM-329]; MSPB not sized (part 3) |
| **OMB's delivery unit** | None | About 30 to 50 staff (working) | Inside the cross-cutting line |

**The immigration court is the one large build.**
- *Scale:* about 1,670 judges at peak (CRT-5.06), from 753 on board [EV-IMM-103], each with clerks, staff attorneys and interpreters, about $1.5 million a team a year [EV-IMM-644] [EV-IMM-645]. The court office is a new build inside an office whose own appropriation is about $107 million [EV-DEM-347]. The bankruptcy courts are the model in law [EV-DEM-333], and the Criminal Justice Act's district plans the model for counsel [EV-DEM-350].
- *Working sequence:*
  - from the immigration act's signature (by about December 2029), an immigration court transition office in the Administrative Office, with EOIR's case system and space plan as its first jobs;
  - within 12 months, the Judicial Conference recommends the judgeships by circuit (working);
  - in 2030-31, each circuit stands up its merit screening panel and its CJA-style counsel plan;
  - EOIR keeps hiring about 250 a year under IMM-3.08 meanwhile, so the ramp to the peak does not wait for the transfer;
  - on October 1, 2031 (working), judges, staff, the case system and space transfer.
- *The screening load is the delivery risk.* More than 1,000 sitting judges (project arithmetic: 753 on board plus about 250 hires a year until October 2031, less attrition) would need a merit screen and an initial term from a court of appeals before the effective date. Section 4 gives no rule for a judge not yet screened on that day. The fix is provisional (part 8, fix 2): judges on board on the effective date continue under an interim appointment of up to two years while the screens finish, with terms then staggered as CRT-5.03 sets.
- *The docket model* stays a joint item with the immigration dossier: the corps' size comes from the immigration model and is reset in 2033 from receipts after legalization (CRT-5.06).

**The courts' load from the forum rules (milestone fix 3; the review's L-2).** No new body, but two new loads: three-judge panels in the district courts and appeals the Supreme Court must decide. Each count below is a working assumption on our estimates, built from the entries named; the evidence that would firm it up is listed in section 4, "Evidence still needed".
- *Which cases.* Under CRT-3.02 as fixed: district-court suits against federal action seeking relief beyond the parties. Rule challenges go to the courts of appeals (CRT-7.01) and state action stays with one judge (CRT-3.01).
- *The measured floor.* CRS counts the cases in which a court actually *issued* a nationwide injunction against the federal government: 28 in the Biden administration's four years, about 7 a year; 86 in the first Trump administration, about 21 a year [EV-DEM-385]; and 50 in the second Trump administration's first 17 months or so, about 35 a year [EV-DEM-048]. These leave out nationwide-class relief and APA stays and vacatur [EV-DEM-386], so they understate the suits that win relief beyond the parties, and they count none of the suits that asked and lost.
- *From the floor to the count (working assumptions).* Two to four suits ask for relief beyond the parties for each one that wins it (judgment; no register count of requests), and 30 to 60% of today's suits are pre-enforcement rule challenges that the order rule sends to the courts of appeals instead. That gives **about 5 to 20 panels a year in a quiet period like 2021-24, about 15 to 60 in one like 2017-20, and about 30 to 100 in one like 2025-26.** As a check, the district courts received 1970 "other statutory" suits against the United States in FY2025, the category that holds APA review, and 145 environmental suits against it [EV-DEM-382] [EV-DEM-383]: 100 panels would be under 5% of them, which fits most such suits seeking relief for the plaintiff alone.
- *District judges' time.* A panel adds two judges to a case one judge hears today: one more district judge and a circuit judge (28 U.S.C. 2284(b) [EV-DEM-344]). If each such case weighs 2 to 5 weighted filings for each judge (a working assumption: these are complex, expedited suits; the register holds no case weights), 5 to 100 panels add about 10 to 500 weighted filings a year to the district courts, **about 0.02 to 1.2 judgeships' work** against the Judicial Conference's standard of about 430 weighted filings per judgeship [EV-DEM-043], and about as much to the circuits. Against the 69 district judgeships in CRT-1.01's 71 [EV-DEM-041], that is under 2%. The 71 rest on today's weighted filings [EV-DEM-042] and need not change; the order rule also takes rule challenges out of the district courts, a small offset not counted. The cost that matters is scheduling: three judges must sit together, often on a fast timetable, in the districts where national suits cluster, which the circuit-wide draw spreads.
- *What reaching state action would add.* The 487 suits a year against state statutes [EV-DEM-383], most of them, on our judgment, asking to stop enforcement statewide, would add several times the federal panels, each with a direct appeal: the regime Congress ended in 1976 [EV-DEM-387]. This is why CRT-3.02 does not reach them (section 4, "The forum rules together").
- *Direct appeals.* Each panel's order granting or denying an injunction can be appealed as of right to the Supreme Court [EV-DEM-387]. If half to nine-tenths of panels produce one and the losing side appeals (the government appeals nearly every national loss), that is **about 3 to 90 direct appeals a year**, against about one a year now: 4 mandatory cases in 2018-21, while the Court granted 217 petitions [EV-DEM-388]. Section 7 (part 3) sets these beside CRT-11.02's mandatory appeals and the Court's merits docket.

**Local election offices** are the other front line.
- More than 770,000 poll workers served in 2024, most of them 61 or older, and 47.9% of jurisdictions had trouble recruiting enough [EV-DEM-019]; 32% of local officials reported threats or harassment in 2026 [EV-DEM-022]. National service placements in election administration (LAB-9, work's) and SAF-8's protections (DEM-1.20) are the two outside supports.
- The new duties (registration from records, notice and cure, audits, the voter card) are paid by DEM-11.01's recurring grant, passed through to the offices that run elections, with a floor for small counties. The equipment fund (DEM-11.02) replaces machines on their lifecycle.
- The systems build, about $0.2-0.5 billion once for registration from records and the citizenship check (DEM-11.03), comes from CAP-13's state and local line. For scale, states reported an average of $249,000 to build online registration [EV-DEM-166].

## 3. Capacity delivered to the flagships

This foundation's main delivery job is the agency rebuild every flagship leans on. Part G of section 3 sized it; CAP-7S.01 to 7.05 and CAP-11 to CAP-13 specify it. This part says how it reaches each flagship and when.

### 3.1 What the rebuild must deliver, and by when

The dates are the flagships' own; the money is CAP-7S (available on R1's enactment) and CAP-7 (from FY2030).

| By | What must be ready | Agency and its line (part G) | Flagship file |
| --- | --- | --- | --- |
| January 20, 2029 | OMB's delivery unit; Schedule Policy/Career rescinded by order (EXE-17) | OMB; OPM | CAP-7.04, CAP-8.01 |
| R1's enactment (about February to mid-2029) | Money available; each agency's hiring path published within 90 days (working); direct-hire and rehiring authority in force | Every agency in part G; OPM | `home/5-delivery.md`:54 (direct hire for HUD 2029-31); `immigration/5-delivery.md`:28 |
| 2029-30 | ACF's staffing plan for the child care entitlement and its fallback | HHS ACF, $1.0 billion surge, $1.9 billion sustained | `care/5bcd-delivery.md`:39, :107 |
| By July 2030 | The IRS's monthly payment file and the shared rail; front doors open at SSA, Rural Development and IRS offices | IRS $8.8 billion and $94.2 billion; SSA $3.9 billion and $31.0 billion gross; Fiscal Service | `secure-floor/5-delivery.md`:46; `clean-power/5-delivery.md`:69 |
| Mid-2030 | Paid leave applications | SSA (administration from the leave fund) | `secure-floor/5-delivery.md`:47 |
| 2030 | HUD's first awards; ACF's free tier for the 2030-31 school year | HUD $3.0 billion and $9.9 billion; ACF | `home/5-delivery.md`:160; `care/5bcd-delivery.md`:54 |
| About October 1, 2030 | USCIS filing opens | USCIS (booked in IMM-1, not CAP) | `immigration/5-delivery.md`:78 |
| January 1, 2031 | CMS's wave 1; SSA's paid leave benefits | CMS $8.0 billion and $17.4 billion | `care/5-delivery.md`:43 |
| FY2031-32 | Rural Development's field staff, 1,000 more by FY2031 and 2,000 by FY2032 | Booked in HOU-14.01, not CAP | `home/5-delivery.md`:167 |
| October 1, 2031 | The immigration court (part 2) | Judiciary; unbooked structure | CRT-5.03 |
| FY2032 | NLRB field staff back to FY2014's level | NLRB, in part G's "other entities" | `work/4-specification.md`:97 |
| January 1, 2033 | CMS's wave 2; hours and occupation in states' wage records | CMS; state UI agencies (work's own line) | `care/5-delivery.md`:46; `work/4-specification.md`:185 |
| FY2034 | Wage and Hour investigators at least 1,200 | Labor, $0.2 billion and $4.6 billion with OSHA | `work/4-specification.md`:123 |
| January 1, 2035 | CMS's endpoint; the long-term care benefit | CMS; HHS | `care/5-delivery.md`:49 |
| FY2035 | The surge ends; the immigration backlog cleared | All; the court | CAP-7S.01; CRT-5.06 |

### 3.2 Hiring

- **The pace is the constraint, not the money.** About 54,000 staff are added across the six agencies sized [EV-DEM-331], against a net loss of 258,108 federal employees since January 2025 [EV-DEM-082]. Large agencies hired 65,953 people in January to June 2025 while 134,122 left [EV-DEM-085], and in 2023 the IRS lost more revenue agents than it hired with the money in hand [EV-DEM-277]. The legacy review's IRS enforcement row needs about 8,000 hires a year, "near the FY2024 pace" (legacy, `capacity-recovery-budget-review.md`:27).
- **What the rebuild uses** (CAP-11.01, in R1 as a condition on the money):
  - *Direct-hire authority* for the delivery jobs each path names;
  - *rehiring former staff without pay penalties*: 141,084 employees took the deferred resignation program [EV-DEM-083], a pool that already knows the work;
  - *special rates* for technology and actuarial jobs;
  - *a time-to-hire target for each agency*, reported quarterly by OPM. OPM's goal is 80 days; its dashboard showed FY2024 averages of 72.1 to 94.6 days for three government-wide occupations [EV-DEM-348]. That is the base the quarterly series starts from.
- **Shared hiring for common jobs** (working choice): OPM runs pooled announcements for the occupations every flagship needs at once (contact-center staff, claims examiners, data and IT staff), so agencies draw on one list instead of competing. It uses OPM's existing hiring authorities, and its cost sits in OPM's line.
- **Training before launch.** Each hiring path counts a hire only once trained for the job it fills (working choice), because new staff are not productive at once: the legacy review puts IRS hiring and training first because "revenue agents take a year or more to become productive" (legacy, `capacity-recovery-budget-review.md`:71).

### 3.3 Release, measures and the contingency

- **The release rule** (CAP-7.02): a quarterly count against each path; below 75% at mid-year, the next tranche waits a year; the money stays available. GAO audits each path and each contingency release once a year (CAP-7.05).
- **When an agency is behind,** the flagships do not all treat it the same way, and section 4's sentence "a program whose agency is behind starts later; it does not shrink" conflicts with two of them:
  - the secure floor lets paid leave's start move ("the start moves, the program does not shrink", `secure-floor/5-delivery.md`:87);
  - care's dates move "only if Congress votes to move it" (`care/5-delivery.md`:31);
  - housing's rights on a date in law "never move"; lagging offices get a backstop administrator and more administration money instead (`home/5-delivery.md`:182).

  The provisional fix (part 8, fix 1): each program follows its own statute. Where the statute lets the start move, it starts later and does not shrink. Where the statute fixes the date, the date holds, and the delivery unit's corrective plan, the contingency and the flagship's own backstop come first.
- **Measures** (CAP-7.03): every plan program publishes time to a decision, error rates, call waits and take-up each quarter. Rural Development's published speed by state, which the rural note asks for (`rural-delivery.md`, 4.1), is one of these.
- **The contingency** (CAP-7S.02): about $43 billion of surge and $30 billion of sustained money, released by OMB only against a published written need from a delivery section or readiness report, with 30 days' notice to the Appropriations Committees, and only for enacted programs. Its first known claims, from the flagships' files:
  - *Work* sends seven items as its written need (`work/5-delivery.md`:195-202, merged in #428; sizes from `work/4-specification.md`, part F). The answers:
    1. *The NLRB,* about $1.0-1.4 billion over FY2030-39 (`work/4-specification.md`:256), **fits inside** part G's legacy NLRB row, $1.9 billion sustained [EV-DEM-330]. It needs no contingency; the row narrows to work's figure at stage G, not here.
    2. *FMCS,* about $0.1-0.2 billion, is in no row: a claim on the contingency.
    3. *OSHA at the high end,* up to about +1,100 staff against part G's +700 (`work/4-specification.md`:259): a claim on the contingency, released as OSHA's hiring path shows the need.
    4. *The Office of Apprenticeship's registration staff:* a claim once Labor's 2027-28 staffing plan sizes it.
    5. *The FLRA's restored caseload:* small; a claim only if the first year's count shows one.
    6. *State UI systems (LAB-11.09):* the conformity grant stays on work's own R1 line, counted once there, because CAP-13's $8 billion is sized for cross-program eligibility systems and shared rule 5's data agreements, not one program's conformity. The UI identity and wage match (LAB-11.06), which uses SSA's and the IRS's records, is a CAP-19 data agreement and may draw on CAP-13 for the state side.
    7. *Measures:* Wage and Hour's and OSHA's inspections, the Board's case times and state UI agencies' first-payment timeliness are work's CAP-7.03 measures, with no new report.
  - *Work, not CAP-7:* state UI administration (LAB-11.08) and the national service agency are work's own program costs (`work/4-specification.md`:261-262).
  - *Care:* ACF's fallback staff, "sized in the 2029-30 capacity plan with CAP-7S" (`care/5bcd-delivery.md`:107), inside ACF's row first.
  - *This foundation:* MSPB's fast-track appeals (CAP-9.01), which part G does not size; claimed after the first year's appeal count (study in implementation).
  - *Rural Development:* if HOU-14.01's rebuild falls behind while four other flagships use its front doors, a written need from the rural front-door load.
- **#404's residual** ($7.0 billion and $20.8 billion) and options A to C stay stage G's (`models/tools/budget/note-cap7-sizes.md`). Under memo 10, option A is enough: the bottom-up need fits inside what is booked.

### 3.4 Payment systems

- **One rail.** Treasury's Fiscal Service already disburses 87.8% of federal payments, nearly 1.3 billion payments in FY2024 [EV-DEM-116]. The plan's new recurring payments (the child benefit, the Climate Dividend) run on the IRS's payment file and Fiscal Service disbursement (FAM-1.09), and the legacy review's Fiscal Service build, $0.3 billion of surge [EV-DEM-329], is in part G. The digital service corps's shared login, payment and notice platforms (legacy, `capacity-recovery-components.csv`:168) are built once for every flagship, not per program.
- **Payments in a lapse** (CAP-4.01): benefit payments, pay for the staff who make them, and payments under grants already awarded continue at the prior year's rate. Funding stopped three times in seven months in 2025-26 [EV-DEM-127], and about 670,000 or more employees were furloughed in 2025 [EV-DEM-128]. *Delivery:* each paying agency names its excepted payment staff in its yearly lapse plan, which OMB publishes (working choice). The legacy file flags a check of the general provision against the Antideficiency Act's excepted-employee rules when drafted (`domain-executive-power.md`:228); that check is part of CAP-18.01's drafting.
- **EXE-18** (executive power, wave three) writes each program's own standing authority: a permanent, indefinite appropriation for the payment and express authority to disburse in a lapse, riding the program's reconciliation bill (`domain-executive-power.md`:173). CAP-4.01 is the general rule; EXE-18 is the per-program belt. Until executive power's dossier exists, this section asks each flagship's payment statute to carry EXE-18's per-program clause where it rides reconciliation (a request to their drafting, not a change to their files).

### 3.5 Records: shared rule 5 in practice

- **Who builds it:** OMB writes the records statute's rules (CAP-19.02) with the digital service corps; each program agency signs computer matching agreements under the Privacy Act; CAP-13's state line pays for state systems to connect.
- **Until the statute passes,** each flagship's own authority carries its match: FAM-1.08 for the child benefit, immigration's IRS-SSA-USCIS agreement, housing's consent-based sharing (`home/5-delivery.md`:232). CAP-19.06 then adopts them by reference, so nothing is rebuilt.
- **The voting floor's citizenship check** runs first on the agreements HAVA already requires [EV-DEM-345], then under CAP-19.02's logging and no-enforcement rule. The Justice Department's 2025-26 suits for unredacted voter rolls [EV-DEM-021] are why the rule bars enforcement use and keeps state records out of its reach.
- **Why it matters for money:** agencies attribute about 73% of FY2021-24 overpayments to failure to use data that existed [EV-DEM-291]; a match is a flag for a person, never a denial (CAP-19.04) [EV-DEM-292].

### 3.6 EXE-3: getting money out the door

Every grant here (DEM-11's formula, CAP-13's state grants, LSC's schedule, IMLS's line) and every release under CAP-7.02 depends on an administration actually spending what Congress provides. EXE-3, executive power's anti-impoundment row, gives the intended recipient a cause of action, disbursement deadlines with deemed apportionment, termination only for cause and no new conditions after award (`domain-executive-power.md`:64-71). It is wave three. **Until it exists, the formula grants carry their own payment clock** (provisional, part 8, fix 4): DEM-11.01's and CAP-13.01's formula money is paid to each state within 60 days of the start of the fiscal year or of enactment, with the recipient able to sue to enforce it, EXE-3's form applied to these two grants only.

## 4. Timeline

| When | Step | Who |
| --- | --- | --- |
| **2027-28 (preparation, labeled)** | Every successor bill, the day-one bridge and the delegation templates drafted (CAP-18.01); the data agreements and matching templates drafted for CAP-19; each agency's draft hiring path from part G; OPM's pooled announcements designed; legal reviews of INT-15's First Amendment footing and of a mid-decade reapportionment (legacy open items); the immigration court's space plan with the immigration dossier; nominees for the EAC's and FEC's empty seats identified | Outside government; agencies' career staff where the law allows (preparation, not launch) |
| **January 3, 2029** | Chamber rules: earmarks (CAP-5.01), committee jurisdiction (CAP-16.01), each chamber's matching rule for the stock ban's penalty (INT-1.04) | House and Senate |
| **January 20, 2029** | Schedule Policy/Career rescinded (EXE-17); OMB's delivery unit stood up (CAP-7.04); OMB guidance on agency assemblies (DEM-18.01); nominations to the EAC's and FEC's seats under current law, confirmed by majority cloture as every nomination now is [EV-DEM-265], so both regain quorums in 2029 before the democracy act restructures them | The President; OMB |
| **By March 2029** | The democracy act on the floor (DEM-1F.01) | Congress |
| **About February to mid-2029** | R1: CAP-7S and CAP-7 available, CAP-11's hiring tools, CAP-13's grants; the legacy review assumed R1 about April 2029, with $1.7 billion of FY2029 cash for the reviewed agencies (range $0.5-4.5 billion) inside the $5 billion shifted into FY2029 (`capacity-recovery-other-agencies-review.md`:137-138). Hiring paths published within 90 days (working) | Congress; OMB; agencies |
| **2029** | The ethics and accountability act: the stock ban (compliance within 180 days of its effective date, working: enactment), paid speech, cooling-off, FARA, lobbying, beneficial ownership, contractors, the Federal Reserve's disclosure; the civil service and delivery act: CAP-8, CAP-9, CAP-4, CAP-19, CAP-7's accountability, CAP-12, CAP-13's authorization; the judgeships act | Congress; OGE; ethics offices; OPM; OMB |
| **October 1, 2029 (FY2030)** | CAP-7's sustained money starts on the working path, $10.4 billion in FY2030 [EV-DEM-328]; Legislative Branch appropriations for CAP-1 to CAP-3, CAP-6 and OTA; the Legal Services Corporation's first step | Congress; agencies |
| **By about December 2029** | The immigration act: the immigration court authorized; the transition office opens (part 2) | Congress; the judiciary |
| **2029-30** | The court integrity act (CRT-2, 3, 4, 6, 7, 11; INT-12.01); the Justices' code within a year of enactment (working) | Congress; the Court |
| **As soon as possible; spring 2030 the outer date** | The democracy act enacted: Divisions A to E, with the floor's effective dates below; the FEC and EAC restructured; DEM-11's first grants within 60 days (provisional fix 4) | Congress; EAC; FEC; states |
| **2030** | First judgeship tranche (CRT-1.01, working); the Architect of the Capitol's chamber report and the legal review of a mid-decade reapportionment (DEM-3.01); the voter card's first mailings; state systems for registration from records built with CAP-13 | Judiciary; Architect; states |
| **November 3, 2030** | First federal election under the floor's barrier-removing rules, if the act is law by about May 2030 (below) | States and counties |
| **Spring 2031** | Census redistricting data; Divisions B and C must already be law | Census Bureau |
| **2031** | The 2031 House review sets the House's size (DEM-3.01) and the DEM-9 fallback; maps drawn under DEM-2's ban and criteria, challenges on the three-judge fast track; the second Congress's bills (CRT-9.01, CRT-10.02, DEM-7.01) | Congress; states; courts |
| **October 1, 2031 (working)** | The immigration court takes over from EOIR (CRT-5.03), with interim appointments for unscreened judges (provisional fix 2) | The judiciary |
| **2032** | Every part of the floor in force by the general election, including registration from records, the citizenship check by records, same-day and online registration, paper ballots and audits; elections under the 2031 maps; a larger House if the census numbers came in time, otherwise in 2034 | States; EAC |
| **2033** | Second judgeship tranche with the circuit realignment (CRT-13.01); the 2033 package: nationwide multi-member districts and the presidential method (DEM-4.02, DEM-9.01) with the amendment (DEM-8.02); the immigration court's corps reset from receipts (CRT-5.06) | Congress; judiciary |
| **2035** | Third judgeship tranche; the immigration backlog cleared (about FY2035); the surge's last year | Judiciary; all agencies |
| **First odd-numbered year after the terms act** | Sitting Justices begin moving to senior status, one every two years (CRT-15.02), when that act passes | The Court |

**The staged House path** sits inside this timeline: the state option (DEM-4.01) is law with the democracy act in 2029-30; the House's size is set in the 2031 review; nationwide districts and the method in 2033.

**The floor's effective dates** (working choice, provisional for Espen, question 2 below). Election offices cannot rebuild registration in a few months, but several of the floor's rules need no new system. On the recommendation:
- *For any federal election held at least 180 days after enactment:* identity by the broad list or a signed statement (DEM-1.06), no-excuse mail voting with the receipt rule (DEM-1.05), the limits on removals (DEM-1.10), certification as a duty (DEM-1.12), restored rights on release (DEM-12.01, **if it survives a challenge**: it rests on the enforcement clauses, is a court risk and could be blocked before the first covered election; section 4, "The floor's legal footing"), the notice on release and pretrial access (DEM-12.02, which do not depend on it), paid time to vote (DEM-13.01). If the act is law by about early May 2030, these govern November 2030.
- *By the 2032 general election, earlier at a state's choice:* registration from records with its notice and decline (DEM-1.01, 1.02), same-day, online and preregistration (DEM-1.03), the two-week early-voting floor (DEM-1.04), the citizenship check by records (DEM-1.08), notice and cure (DEM-1.09), paper ballots and audits for every federal contest (DEM-1.11). The voter card's mailing to current voters is phased over the first two federal cycles (DEM-1.07).
- *What it costs:* the barrier-removing rules reach 2030's voters; the systems rules wait one cycle. The alternative, every rule for 2030, risks the failure the legacy file warns of: "registration provisions take time to land" (`domain-democracy.md`:96).

**If a vehicle is late.**
- *R1 late or struck:* the hiring authority moves to the civil service and delivery act; CAP-7S's money comes through appropriations; each flagship's dates move by its own rule (part 3.3).
- *The democracy act late past spring 2031:* the 2031 maps are drawn under current law and the ban applies from enactment; the 180-day rule moves the first covered election; the state tracks (DEM-10, DEM-19, DEM-20) continue.
- *The immigration act late:* the court's effective date moves with it, about 21 months after signature; EOIR keeps hiring under IMM-3.08 until then.
- *The ethics act's fast track fails:* its floor time is the legacy risk (`domain-integrity.md`:179); the stock ban's dates move with enactment.

## 5. Remedies when delivery fails

| Who | When | What they can do | Provisions |
| --- | --- | --- | --- |
| A voter or the Attorney General | A state does not meet the floor | Sue in federal court after written notice to the state's chief election official and a period to correct it, shortened close to an election (provisional fix 3, on the NVRA's notice-and-cure model: 90 days, 20 days within 120 days of a federal election, none within 30 days [EV-DEM-351]) | DEM-1.13 (provisional) |
| A candidate or voter | Certification is refused | A fast-track suit to compel the ministerial duty | DEM-1.12 |
| A voter whose citizenship is flagged | A records non-match | Written notice, a chance to respond, registration kept until a person decides | DEM-1.08 |
| A mail voter | A ballot defect | Notice within two business days and a cure period to the canvass's end | DEM-1.09 |
| A voter | A map that breaks the ban or the criteria | A three-judge court on a fast track; a remedial map for the cycle | DEM-2.04 |
| A complainant | The FEC does not act in 120 days | Sue the violator in district court | INT-7.01 |
| A covered official | A computed penalty | Notice, 30 days to contest, an appeal before collection | INT-1.04 |
| A person injured by an emoluments violation | — | A private cause of action | INT-4.01 |
| An immigrant in the court | A decision | Appeal to the circuit's panel, then the court of appeals, with law reviewed de novo; reopening for lack of notice | CRT-5.04, 5.05, 5.07 |
| A beneficiary in any plan program | An overpayment claim | A person's review, notice, a hardship rule, recovery capped at 10% of a monthly payment, payment during appeal, no repayment of the government's error | CAP-19.05 |
| A beneficiary | A funding lapse | Payment continues at the prior year's rate | CAP-4.01 |
| A person | A record used about them | See what was used; no enforcement use | CAP-19.02 |
| A state or election office | Formula money not paid on time | Sue to enforce the payment clock (provisional fix 4); EXE-3's general cause of action later | DEM-11.01, CAP-13.01 |
| A career employee | A move into an at-will schedule | MSPB appeal; the statute bars the schedule | CAP-8.01 |
| A program or agency behind its path | A missed hiring path or measure | A corrective plan with the delivery unit, the contingency against a written need, the flagship's own backstop; never a cut | CAP-7.02, 7.03, 7S.02 |
| Congress and the public | Any of the above | Quarterly delivery reports, GAO's yearly audits, inspectors general (about 13,800 staff in FY2025 [EV-DEM-223]) | CAP-7.04, 7.05 |

**A remedy that rests on an inspector general** is only as strong as the inspector's tenure: 17 inspectors general were fired in 2025 without the 30 days' notice the law requires [EV-DEM-036]. CRT-2.03 and CAP-7.05 use EXE-5's notice-and-reasons template, which makes a removal visible, not impossible (`domain-executive-power.md`:85).

## 6. States' and local election offices' roles

- **Chief election officials** keep the statewide list HAVA requires [EV-DEM-345] and receive the motor vehicle, benefit and federal records that register voters (DEM-1.01, 1.02); they send notices, run the citizenship flags, the cure process and the audits, and certify.
- **Counties and municipalities** run voting itself: sites, drop boxes, poll workers, ballots, the canvass. DEM-11.01's grant passes through to them by formula with a small-county floor; the equipment fund lets them replace machines on their lifecycle, not when a one-time grant happens to arrive.
- **State motor vehicle and benefit agencies** become registration sources from records they already hold; the plan's new contact points join them (DEM-1.02).
- **Corrections agencies** give the restored-rights notice (DEM-12.02).
- **Legislatures and commissions** draw the maps under DEM-2; a state may choose multi-member ranked-choice districts (DEM-4.01), and nineteen states have banned ranked-choice voting [EV-DEM-255], so uptake will be uneven.
- **State tracks** (DEM-8.01, 10.01, 19.01, 20.01, INT-17.01, CRT-19.01) are campaigns, not federal duties.
- **For the flagships,** states run SNAP, Medicaid, child care, unemployment and LIHEAP. CAP-13's about $8 billion pays for cross-program eligibility systems and the data agreements shared rule 5 needs, by caseload (CAP-13.01). States with modern systems paid pandemic unemployment faster, by 8 to 15 days on average [EV-DEM-295], which is the case for building before launch.
- **Territories** run their own elections and are in the EAC's survey [EV-DEM-346]; the floor applies to federal elections there as in the states. Voting delegates and the admission procedure are DEM-7.01's, in the second wave.
- **Tribes:** tribal identification counts for voting (DEM-1.06); DEM-7.01 adds tribal representation with enforceable consultation.
- **No new state matching cost.** The floor's new duties come with DEM-11's recurring money and CAP-13's build money.

## 7. Rural delivery

Rural delivery looks first at USDA's local channels (`DEC-2026-11-09-26`; `dossiers/foundations/rural-delivery.md`).
- **Elections.** Rural voting runs through county offices, many of them small. DEM-11's small-county floor, at least one drop box per county (DEM-1.05, working), mail voting without an excuse and the voter card by mail are the rural parts of the floor: none needs a trip to a distant office. The voter card's optional photo is taken free at a motor vehicle office, an SSA field office or the election office (DEM-1.07). SSA field office staff fell from 25,845 to 22,583 [EV-DEM-105], so the photo duty goes to motor vehicle and election offices first and to SSA only where its staffing path is on track (working choice).
- **Rural Development's front doors** are benefit-delivery points the plan expands, so under DEM-1.02 they pass registration records like any other plan agency, from the enrollment record and without a new desk task. They take nothing else from this foundation.
- **The field rebuild.** Rural Development lost about 36% of its staff in the first half of 2025, to an estimated 3,058 full-time equivalents in FY2026 [SRC-2143] [SRC-2130]. Its rebuild, about 2,000 more staff to about 5,000 by FY2032, is booked in housing's HOU-14.01, not in CAP (`home/5-delivery.md`:167), while four other flagships use its front doors. This foundation adds the cross-cutting pieces the rural note asks for (`rural-delivery.md`, section 5): CAP-11's hiring tools apply to Rural Development's jobs; CAP-7.03 publishes its speed by state; the contingency answers a written need if the front-door load outruns HOU-14.01's staff. Whether the other flagships share the rebuild's cost is stage G's.
- **Legal help and the courts.** LSC's grantees cover designated service areas in every state [EV-DEM-349], so CRT-20.01's growth reaches rural places through grantees already there. The immigration court's judgeships may sit across districts in a circuit (CRT-5.01), and its counsel plans follow the CJA's district model [EV-DEM-350]; rural detention sites are where remote appearance and circuit-wide assignment matter most (working choice: the court office sets a remote-appearance rule with the right to appear in person).
- **Libraries.** DEM-17's capital fund is weighted to places with low fiscal capacity, and DEM-17.02's operating line passes through state library agencies to local libraries, many of them rural.

## 8. What delivery changes in section 4 (provisional)

Each fix is the smallest that lets the provision run, written into `4-specification.md` and `provisions.json` and marked provisional, for Espen's review in the morning (overnight relay).

1. **CAP-7.02, the start rule.** *This amends a sentence of decided memo 10 B* ("A program whose agency is behind starts later; it does not shrink", `memos/10-capacity-size-and-pace.md`:50), which Espen chose; it narrows that sentence rather than applying it. *Problem:* "a program whose agency is behind starts later" conflicts with care's dates, which move only by a vote of Congress, and housing's rights on a date in law, which never move (part 3.3). *Fix:* each program follows its own statute: where it lets the start move, the program starts later and does not shrink; where it fixes the date, the date holds and the corrective plan, the contingency and the flagship's backstop come first.
2. **CRT-5.03, the transfer of sitting judges.** *Problem:* more than 1,000 judges (project arithmetic, part 2) would need a merit screen and a term from a court of appeals before October 1, 2031, and nothing covers a judge not yet screened on that day. *Fix:* judges on board on the effective date continue under an interim appointment of up to two years while the screens finish; initial terms are then staggered from 4 to 14 years as CRT-5.03 sets.
3. **DEM-1.13, enforcement of the floor.** *Problem:* the floor binds every state, but section 4 gives only certification (DEM-1.12) a remedy; a mandate with no enforcement fails where a state will not comply. *Fix:* DEM-1.13 (severability and forum) adds enforcement: the Attorney General, or a voter after written notice to the state's chief election official and a period to correct it (shorter close to an election), may sue in federal court to enforce Division A, on the NVRA's notice-and-cure model, whose periods are 90 days, 20 days within 120 days of a federal election and none within 30 days (52 U.S.C. 20510(b)) [EV-DEM-351].
4. **DEM-11.01 and CAP-13.01, a payment clock.** *Problem:* both are formula grants to states that an unwilling administration could slow, and EXE-3, the general cure, is wave three. *Fix:* formula money is paid within 60 days of the start of the fiscal year or of enactment, enforceable by the recipient, EXE-3's form for these two grants only.

None changes a cost.

## 9. What delivery leaves open

- **The immigration docket model:** a joint item with the immigration dossier; the corps is reset in 2033 (CRT-5.06).
- **MSPB's fast-track load:** studied in implementation from the first year's appeals (CAP-9.01).
- **SSA's trust-fund split** of its CAP-7 line (Evidence still needed in section 4).
- **The time-to-hire series by agency:** CAP-11.01 builds it; the register holds only OPM's three government-wide occupations [EV-DEM-348].
- **LSC's current grantee and staffing counts**, to size CRT-20.01's schedule in section 6.
- **The NVRA's enforcement text** is now in the register (52 U.S.C. 20510(b) [EV-DEM-351]); whether the floor copies its periods exactly is a drafting choice.
- **Rural Development's cost-sharing** among the flagships that use its front doors: stage G.

## Questions for Espen

Drafted on the recommendation and marked provisional, under the overnight relay (`charter/PROGRESS.md`, In motion, item 3); revised for Espen's answers. Section 4's own provisional item, INT-1.01's self-directed retirement accounts, stays provisional and is not repeated here.

1. **Four delivery fixes to section 4** (part 8). Each lets a provision run; none changes a cost (section 6, part 7). Fix (a) **amends the decided memo 10 B sentence** "a program whose agency is behind starts later; it does not shrink", so care's and housing's fixed dates hold: Espen would be revising their own choice. *Recommended: yes to each:* (a) a program whose agency is behind follows its own statute's start rule (CAP-7.02); (b) unscreened sitting immigration judges continue for up to two years at the transfer (CRT-5.03); (c) the voting floor is enforceable by the Attorney General and by a voter after notice (DEM-1.13); (d) election and state implementation grants are paid within 60 days, enforceable by the recipient (DEM-11.01, CAP-13.01).
2. **When the voting floor takes effect** (part 4). *Recommended:* the rules that remove barriers (ID by a statement, mail voting without an excuse, no purges for not voting, certification as a duty, restored rights if DEM-12.01 survives a challenge, paid time to vote) apply to any federal election at least 180 days after enactment, so November 2030 if the act is law by about early May 2030; the rules that need new systems (registration from records, the citizenship check by records, same-day and online registration, early voting's two weeks, notice and cure, paper ballots and audits) by the 2032 general election, earlier where a state is ready. *The alternative,* every rule for 2030, reaches more 2030 voters on paper but asks offices to rebuild registration in months.
