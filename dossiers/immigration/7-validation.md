# A new consensus on immigration: validation

Role: section 7 of the immigration dossier. It compares the costs and reach in sections 4-6 with outside estimates and says what the arithmetic misses. It also covers how the decided set lands with the rest of the plan, whom it reaches, the strongest objections and the signs of failure. Status: reviewed at L3 (`review-milestone.md`, #303), with the review's fix steps applied (#305, #307); the re-check was the booking (#310). On `DEC-2026-11-12-07` and `-12`. Outcomes it serves: OUT-07 (a humane, orderly and lawful immigration system with broad public consent), OUT-06 (fair pay at work), OUT-01 and OUT-03 (child poverty and care, through the table) and OUT-09 (a government that delivers). No immigration model exists in `models/` (`legacy-research.md`, finding 8). This dossier builds a first, scoped one, `tools/immigration_model.py`: USCIS's throughput, the courts' capacity and counsel, detention against case management, and status's fiscal effect from CBO's score, with every input traced or labeled (section 6, "Counting rules"). Every figure here is project arithmetic on outside scores, laid on fiscal years by `tools/immigration_path.py`.

## 1. Against outside figures

| Line | This dossier (FY2030-39, general fund) | Outside figure (publisher, year) | How they compare |
| --- | --- | --- | --- |
| Status (memo 1) | About +$50 billion (−$50 to +$150 billion) | H.R. 6 (Dreamers and TPS): +$35.3 billion over 2021-31 (CBO, 2021) [EV-IMM-600]; farmworker bill +$4.7 billion (CBO, 2021) [EV-IMM-215] | Memo 1 reaches two to three times H.R. 6's people. Scaled and grown, that gives +$0.09-0.14 trillion; health coverage the single plan pays anyway brings it down (section 3). Same sign as both 2021 scores |
| Status, the other pattern | — | S. 744: −$158 to −$197 billion (CBO, 2013) [EV-IMM-205] [EV-IMM-200]; legalization with E-Verify and no new flows, −$10 billion in a decade (BPC) [EV-IMM-611] | S. 744's saving came from about 10 million added people by 2023 [EV-IMM-203], which memo 1 does not have. BPC's figure is the closest to the decided pairing and is near zero. The booked −$0.14 trillion rests on S. 744's pattern and does not hold |
| Legal numbers (memo 3) | About −$40 billion | The 2021-24 surge lowers deficits $0.9 trillion over 2024-34 for about 8.7 million people (CBO, 2024) [EV-IMM-219] [EV-IMM-220] | About $10,000 per added person a year, discounted for spouses and children, on 0.3-0.6 million: a fraction of CBO's surge, same direction |
| Asylum corps (memo 4) | About $6.6 billion (in the $26.0 billion line; `immigration_model.asylum_refugees`) | $180 million a year for 75,000 cases (DHS, 2022) [EV-IMM-302]; $5.4 billion over the decade (legacy capacity review) [EV-IMM-574] | DHS's figure scaled to 250,000-350,000 decisions a year gives the upper part; the legacy review sits below. DHS's estimate is the Biden administration's own, with no independent check in the register |
| Immigration judges (memo 4, IMM-3.08) | About 1,670 judges in all (920 added), about $13.2 billion over FY2030-39 | CRS: 700 more than 649, 1,349 in all, to clear a smaller backlog by FY2032 (CRS, 2023) [EV-IMM-642]; the Manhattan Institute: about 250 more a year at 957 completions a judge (2025) [EV-IMM-646] | Both point to several hundred more judges. The model uses CRS's lower completions rate, about 510 [EV-IMM-641], because fuller hearings with counsel are slower than recent rates that in absentia orders inflate [EV-IMM-106] |
| Detention and case management (memo 5) | About +$6.8 billion (range −$1 to +$27 billion) | $187.48 a bed-day and $4.11 a day for alternatives, FY2023 (ICE) [EV-IMM-628] [EV-IMM-629]; $38.47 a family a day for case management, FY2016 [EV-IMM-355] | The cap's saving is about $1 billion a year; case management for about 150,000 people at a time costs more. The net sign depends on that count and the rate (`6-cost.md`, part 1) |
| E-Verify mandate (memo 5) | About −$20 billion on the general fund, with operations; about −$42 billion to Social Security | +$30 billion to the deficit; −$88 billion off-budget; +$49 billion on-budget (CBO and JCT, 2013) [EV-IMM-394] [EV-IMM-395] | Scaled by 0.3 for the pool left after legalization and phased in from about July 2031 (IMM-4.13). The direction on each budget follows the score. The size rests on the pool, a working assumption |
| Eligibility table (memo 6, amended for health) | About +$112 billion: coverage for lawful residents above care's population base (about $79 billion, on care's own path) and the five-year wait's programs | H.R. 6's on-budget direct spending, $36.5 billion, mostly marketplace credits, Medicaid and refundable credits (CBO, 2021) [EV-IMM-601] [EV-IMM-602] | Larger, because the single plan covers lawful newcomers at care's average cost per newly covered person (about $13,500 in 2032), and the table ends the five-year wait. No score of a table like it exists |
| USCIS (memo 7) | About $17-27 billion in all | $40 billion surge line and a $6 billion pending reserve (legacy) [EV-IMM-573] [EV-IMM-578]; the 2025 fee title, $66.5 billion of fee revenue over 2025-34 (CBO, 2025) [EV-IMM-619] | Bottom-up at about half the legacy line; the fee title shows what fees can carry |
| Social Security | Not quantified for legalization | +$284 billion to the funds by 2024 for S. 744 (SSA's actuaries, 2013) [EV-IMM-604]; about $12 billion a year net from unauthorized workers already (SSA, 2010) [EV-IMM-606] | Direction certain, size open: point 13 asks the actuaries |

**The set against the booked row.** The set comes to about +$0.18 trillion, against the booked −$0.14 trillion. Of the difference, about $0.31 trillion over the decade, about $0.14 trillion is the removal of a saving drawn from a different bill (section 6, part 4). For the status title itself, outside scores agree on the direction: a legalization without large new flows is a small first-decade cost on the general fund and a gain to Social Security [EV-IMM-600] [EV-IMM-604] [EV-IMM-611].

## 2. What the arithmetic misses

| Gap | Effect on the figures | What would close it |
| --- | --- | --- |
| A first, scoped model only (`tools/immigration_model.py`) | Status's fiscal effect is CBO's 2021 score scaled, not a microsimulation; memo 3, memo 6, E-Verify and the restructure are judgment lines on outside scores; labor-market effects are cited evidence, not modeled | **A full immigration model goes to `models/` at stage H**, with a model card and benchmarks: the population by status, years here, earnings and program use. CBO's score (point 13) is the check on it |
| Take-up (about 70% [EV-IMM-609]) | Moves memos 1 and 6 up or down together, and E-Verify's pool the other way | The first year's filings (`5-delivery.md`, part 7) |
| The share with ITIN filings or posted earnings | Sets how many people prove residence from records, against the statement route | IRS and SSA counts in the 2027-28 test match (IMM-6.06) |
| Labor-market and growth effects | Left out of the total; the legacy DY8 put them at +$0.02 to +$0.20 trillion (`legacy-research.md`, section 1) | A dynamic score; never a pay-for |
| E-Verify's pool after legalization (0.3 of 2013's) | Scales every E-Verify figure | The mandate's published counts (IMM-4.18) |
| State and local budgets | Not in the federal figures; long-run effects are negative at that level [EV-IMM-222] | The financing settlement's state ledger |
| The judges IMM-3.08 needs and CRT-5's cost | The model's first estimate is about 1,670 judges in all, 920 added (range about 860-2,400 in all; at the slow end of completions a judge, 250 hires a year clear the backlog only by FY2036), priced at about $13 billion; CRT-5's own $0.03 trillion, unscored [EV-IMM-576], should be re-scored without these judge teams. The court plan as a whole (IMM-3.08 to 3.12, the corps and its cost) is expected to change once democratic renewal's judicial branch plan is done (Espen, November 12); these figures stand until then | Democratic renewal's judicial branch plan, docket model and score |
| The restructure's cost | Judgment, about $3 billion; no cost study | A GAO or CBO estimate of a component reorganization |
| Behavior at the border after enactment | The cutoff and the surge rule are designed for it; no figure assumes a change | Encounter data and the surge rule's reports (IMM-3.02) |

## 3. How it lands with the rest of the plan

- **Secure floor** (`DEC-2026-11-12-06`): the child benefit's row is the child's own ID (FAM-1.04 = IMM-1.25). SNAP's immigrant rule is counted once, in the secure floor's INC-2.01. The work-eligible numbers from registration (IMM-1.12) bring legalized parents into the earned income credit. The two files say the same thing (`dossiers/secure-floor/4-specification.md`, shared rules).
- **Care** (`DEC-2026-11-10-09`, `-11-03`, `-11-04`):
  - point 3 is answered (Espen, November 12, lead session): the single plan covers everyone with lawful or registered status, a filing receipt included, and people with no status keep emergency care as today (IMM-1.21). Lawful residents above care's population base are priced here on care's own path. Care's booked figures count some people with no status as covered beyond the 1% residual, about $430 billion over FY2030-39 too high, a correction for the lead's health booking (`6-cost.md`, part 1);
  - care's three workforce asks are answered: current care workers through tier A's work route (IMM-1.01), the portable care visa at the $20 floor (IMM-2.09) and care on shortage lists.
- **Housing** (`DEC-2026-11-09-10`, `-11`; `-11-10-02`):
  - the open items in its table are answered: owner programs by the owner of record, FHA's rule reversed, the property-tax match outside 1611 and 1621, the emergency fund without a status test, and farmworker housing as rental help, proposed (IMM-1.30 to 1.35);
  - the construction visa and tier A's construction route support its workforce condition.
- **Transportation:** the construction route is tied to its decided building (IMM-2.10).
- **Democratic renewal:** the five court requirements (IMM-3.08 to 3.12) go to CRT-5, to be scored with IMM-1. Rule 5's verification needs are met by the IRS-SSA-USCIS match (IMM-6.06). Point 14 is proposed.
- **Executive power:** officer identification is one statute (IMM-4.08).
- **Work:** the labor-standards and anti-retaliation items (IMM-4.16, 4.17) and the work routes' wage and portability rules (shared rule 8) are proposed to it.
- **The data firewall** (IMM-1.36, 4.11) matches housing's and care's rules and the secure floor's FAM-1.08.
- **The budget model:** a cost of about +$28.8 billion a year from FY2040, against a booked saving of $18.7 billion. Booking it adds about 1.1% to the plan-wide FY2040 gap (section 6, part 5).

## 4. Reach: for whom

| Group | Size (working assumption unless tagged) | What they get | When |
| --- | --- | --- | --- |
| Residents with ten years or more | About 7-9 million at enactment (MPI's 60% with ten years in 2021 [EV-IMM-617], moved to 2029) | A green card on approval (tier B) | From filing, about October 2030 |
| Dreamers, former TPS, DACA and parole holders, farm, care and construction workers, present by January 1 of the year of enactment | About 1.5-3 million outside tier B; 436,350 DACA recipients [EV-IMM-016]; TPS down to about 274,000 [EV-IMM-022] | A green card on approval (tier A); known people start on a notice | From filing; notices first |
| Everyone else present on the signature date (and tier A's late arrivals of the year of enactment) | About 2-4 million | Registered status: a work permit and protection now, a green card at ten years | From filing |
| Citizen children with an unauthorized parent | 5.3 million (MPI) [EV-IMM-007] | A parent with status and a work-eligible number; the child benefit by their own ID | 2030-31 |
| Green cards over the decade | About 6-8 million at about 70% take-up [EV-IMM-609] [EV-IMM-603] | Permanent residence; citizenship on the clock | 2031-40 |
| People still without status after memo 1 | About 1.5-3 million (memo 6) | Emergency care as today; child care and the child benefit for their children; not the single plan, its long-term care benefit (IMM-1.23), SNAP or SSI. Filing for status brings the single plan from the receipt | — |
| Families on the queues | About 3.8 million on the family waiting list [EV-IMM-127] | Spouses and children of permanent residents outside the caps; more numbers | From FY2031 |
| Refugees | At least 50,000 a year, against 7,730 admitted through June 2026 [EV-IMM-052] | Admission | From FY2030 |
| People in detention | About 65,000 held in 2026 [EV-IMM-171], to 30,000 on average | Counsel; standards; case management for others | October 2029 (cap); counsel with the act |
| Workers | About 9.6 million unauthorized workers [EV-IMM-008] | Legal work on filing; protection when they report abuse; E-Verify with error correction | From filing; E-Verify from about July 2031 on the working timeline (IMM-4.13) |

**Who is not reached, and why.**
- *People who arrive after the signature date:* they reach the standing registry only at ten years (IMM-1.04, 1.05). This is the cutoff's purpose. People who arrive during the year of enactment, before signature, can register but are not in tier A.
- *Long-settled residents removed or pushed out before the act* are reached only through family: IMM-1.15's route from abroad needs three years' presence and a citizen or resident spouse, parent or child. ICE reported 442,640 removals in FY2025 and 483,200 in FY2026 [EV-IMM-659].
- *People with no status after the act* get emergency care, not the single plan (IMM-1.21).
- *People with old removal orders or a reentry after removal* are reached: the reinstatement bar and the immigration-only grounds do not apply (IMM-1.08).
- *People with serious convictions:* barred under 1259's grounds, with waivers for old or minor ones (IMM-1.08).
- *People who never file:* about 30% at the working take-up. The records-first form and no fee below 200% of poverty are aimed at them [EV-IMM-425].

## 5. Objections answered

| Objection | Answer | Evidence |
| --- | --- | --- |
| "It's amnesty, and permanent amnesty at that." | Ten years' residence, a criminal check and biometrics for every applicant, and cutoffs: January 1 of the year of enactment for tier A, the signature date for registration. The registry is already in the law; its date has not moved since 1986 | EV-IMM-590, EV-IMM-591, EV-IMM-623 |
| "It will draw the next wave." | IRCA did not change long-run unauthorized inflows from Mexico, and Spain's 2005 regularization showed none. Here, no one who arrives after the law is signed can register, and only people here by January 1 of that year reach tier A; people who arrive during the debate can register but wait ten years for a green card. E-Verify, the surge rule and the priorities answer the rest | EV-IMM-233, EV-IMM-456 |
| "It costs taxpayers." | On our estimates, about +$0.18 trillion over ten years, mostly coverage for lawful newcomers and a shorter wait for help. The status title itself is a small first-decade cost, as outside scores of similar bills find, and a gain to Social Security | EV-IMM-600, EV-IMM-604 |
| "E-Verify will flag citizens." | At FY2009 rates, 0.2% of citizens were wrongly flagged at first. The design gives ten days to contest, no firing meanwhile, an answer in ten days or confirmation, and lost wages paid | EV-IMM-391, EV-IMM-613 |
| "E-Verify doesn't work." | It misses about half of the unauthorized workers it checks, mostly through borrowed identities. It is the trade Espen accepted for much wider status, and it lands after most workers hold status, with labor enforcement aimed at abusive employers | EV-IMM-393, EV-IMM-399 |
| "Releasing people means they disappear." | More than 99% of people in full case management with a hearing appeared, though ICE's data leave groups out | EV-IMM-354, EV-IMM-353 |
| "Abolishing ICE means no enforcement." | Interior enforcement continues in a new component, bound by priorities in law: security, public safety and recent entry. Criminal investigations get their own agency | IMM-4.01 to 4.03 |
| "A surge with no bar invites crossings." | The surge rule decides claims in about 90 days and removes people who are denied. The proclamation bar was held unlawful | EV-IMM-458, EV-IMM-054 |
| "More immigration lowers wages." | The consensus review finds very small effects on natives' wages over ten years | EV-IMM-223 |
| "The data will be used to deport people." | One firewall in law, with penalties and a private right of action; a criminal warrant for a named person is the only exception | IMM-1.36, 4.11 |

## 6. Signs of failure

| Measure | Expected | A sign of failure | Response (section 8) |
| --- | --- | --- | --- |
| Filings in the first two years | Most of 8-10 million | Under half of the eligible population | Find who is missing; look at fees, fear of data use and the front doors |
| Days to a work-permit receipt | 14 or fewer for 95% | Weeks, for months | The E-Verify start waits, by design (IMM-4.13) |
| The statement route's fraud audit | Low | Abuse at scale | Two documents per gap year (IMM-6.06) |
| E-Verify's erroneous nonconfirmations for lawful noncitizens | At or below permanent residents' rate | Above 1% | The next tranche pauses (IMM-4.13) |
| Contests resolved in ten days | Nearly all | Many closing as confirmed by default | Staff the contest line; publish the gap |
| Average daily detention | 30,000 or fewer | Waivers back to back | A statute change, not a standing waiver (IMM-4.05) |
| Appearance under case management | Near the 99% GAO found | Well below | Better case management and counsel before more detention |
| Deaths in custody | Far below FY2026's 37 [EV-IMM-179] | Any rise | The inspector's review and contract terminations (IMM-4.04, 4.09) |
| Surge activations | Rare; decisions in 90 days | Months-long backlogs at reception centers | More officers and temporary judges, not a bar (memo 4) |
| USCIS processing times | Six months for standard applications | Rising past the target | The appropriation is short; report to Congress |
| Encounters after the signature date | No lasting rise | A sustained rise | The surge rule; review the cutoff for any later law |
