# Capacity recovery review, round 2: the other agencies and the scope of capacity

**Status:** review-ready, revised Oct 26 after Espen's questions and the pricing of three surge items (Claude Code; branch `claude/pensive-mendel-g1lwl5` from main aa8552d, PR #23). Evidence and recommendations.

Two items are decided under the project-coworker delegation, and are marked as such: how the development agency's spending is categorized, and how SSA's added staff are financed. **Espen accepted DEV-P and SSA administration of paid leave on Oct 26** (governing record). Nothing else here is adopted.

- **Data:** [capacity-recovery-components.csv](capacity-recovery-components.csv), 203 rows.
- **Arithmetic:** `python3 index/tools/capacity-review/review.py`, which reads only.
- **Units:** $B, nominal, midpoint with the range in brackets. Round 1 (IRS, CMS, HUD, Education) is [capacity-recovery-budget-review.md](capacity-recovery-budget-review.md).

## Answers to Espen's questions

**Was $2.3B enough for NOAA?** No. That figure covered both surge and sustained, and it was too low because I used the wrong staffing loss: the National Weather Service's 560-600 positions instead of NOAA's.
- **Staff losses.** NOAA lost about 2,200 of its roughly 13,000 staff in 2025, nearly 20% (E&E News, from staff trackers). The Weather Service also carried vacancies before the cuts.
- **Program cuts.** Climate research (OAR) fell nearly 10% in FY2026. Regional climate services lost funding in 2025. The IRA rescission took about $384M of NOAA grants (CBO, via CRS).
- **Revised NOAA:**
  - rehire about 2,500 staff: $0.45B a year;
  - restore climate research and services: $0.15B a year;
  - flood-map data: a $0.5B surge;
  - replace the rescinded grants: a $0.4B surge.
  - **Total: about $8.5B** (range $6.2-12.9B).
- **What remains outside capacity and where it is counted.** Satellites, ships and fisheries were not cut: Congress held them near FY2025 levels in FY2026. They sit in the current-law baseline, so nothing is lost by leaving them out.

**Are costs I excluded as "not capacity" still counted somewhere?** That question changed the method. Every exclusion now has a row in a **boundary ledger** (30 items in the CSV). Each row states where the cost is counted and whether it is priced. Going through it surfaced four gaps:
- **Development, humanitarian and global health programs.** Counted nowhere until now. Proposed new row **DEV-P, about $92B** over FY2030-39.
- **Paid-leave administration.** The funds model counts about $0.9T of *benefits* over FY2030-39 but no cost of administering them. Proposed: **about $30B of administration, charged to the leave fund**, roughly $3-4B a year once mature.
  - **Claim-volume check.** Mature benefits of about $120B a year at $6,000-10,000 per claim mean about 12-20 million claims a year. At $150-350 of processing per claim, that is about $2-7B a year, or 1.5-6% of benefits.
  - **Comparison.** That is a fraction of SSA's $14.8B administrative budget. Short, frequent leave claims with medical certification cost more per benefit dollar than pensions do.
- **State and local implementation grants (CAP-13).** Estimated at $0.03T but in no total. After the overlap check (below): **count about $8B inside the surge.**
- **Unpriced at first, now priced (below):**
  - Medicare claims operations for HLT-2's new benefits;
  - FEMA's future-conditions flood mapping;
  - the IRS's dividend and mark-to-market functions;
  - HUD's ROAD Act programs.

  Still unpriced: USDA conservation delivery, needed only if CLI-13 is chosen.

The round 1 voucher-fee correction (about +$12.2B on HOU-4) is the fourth program-row cost already found.

## Revised method

1. **Three layers per agency.** Each agency is now sized in three layers:
   - **Restore:** losses since January 2025.
   - **Pre-2025:** shortfalls that existed before the cuts, where documented. Examples: SSA's January 2025 staffing was already a multi-decade low; FEMA was short of its own staffing targets; the Weather Service had vacancies.
   - **Agenda:** new work the domain files assign.

   Each layer is split into surge (finite builds) and sustained (recurring staff and operations).
2. **Boundary ledger.** Every cost kept out of capacity is recorded with its home. The homes are a program row, fees, a trust fund, the current-law baseline, or "no home" (a gap that needs a row).
3. **Scope.** The scope is every federal entity whose capacity the agenda depends on, not only the D9 list. The added entities are:
   - **Not on the D9 list:** HHS ACF (child care and pre-K), HRSA, USDA FNS, Treasury's Fiscal Service, the paid-leave administrator, Commerce BIS, and DOE's contracts-for-difference office.
   - **Shared capacity:** state and local implementation (CAP-13), a federal digital service corps (CAP-12), and inspector-general and GAO oversight of the surge.
   - **Checked and found already counted elsewhere:** congressional capacity, judgeships, DOT administration, OJP grant administration, BLS and NSF, VA, public media and immigration courts.

## Decisions made under the delegation

**1. The development agency (USAID successor).** Espen asked for funding at the level needed to fundamentally re-establish a USAID-type agency by 2029. It is categorized three ways:

| Part | Category | Cost | Basis |
| --- | --- | --- | --- |
| Re-establishment: headquarters, about 60-80 missions, systems, security, rehiring about 10,000 staff | Surge (restore) | $4.0B (range $2.5-6.0B) | Before 2025, USAID had over 10,000 direct hires and contractors in about 80 missions (CRS, as reported). Estimate |
| Operating expenses and capital fund | Sustained capacity | $1.95B a year; $24.7B over FY2030-39 | USAID operating expenses were $1.73B in FY2024 and $0.11B in FY2026. The capital fund was $0.26B and is now zero. FY2024 real level |
| **DEV-P: development, humanitarian and global health programs** | **New permanent program row, not capacity** | **About $92B (range $70-115B) over FY2030-39** | FY2024 non-emergency base $25.7B (CRS R47579) against the comparable FY2026 accounts at $21.7B (CRS R48624). The gap is about $7.3B a year in FY2026 dollars, phased 50/80/100% over FY2030-32 |

- **Why the FY2024 real level.** FY2024 was the last ordinary year before the dismantling. Rebuilding to it restores the agency's operating scale without choosing a new foreign-aid policy.
- **Why the programs are their own row.** An agency without programs is not re-established. And a permanent program cannot hide inside a capacity line.
- **Effect on the 2040 test.** DEV-P is a general-fund claim, paid for at maturity under D4-B. It adds about $10B a year in FY2040, about 0.03% of GDP, so it **needs a ledger row and financing**.
- **Also counted:** contractor staff paid from program accounts are carried in DEV-P.

**2. Who pays for SSA's added staff: keep the current-law split.**
- **How it works now.** The administrative account is first paid from the Social Security and Medicare trust funds. The general fund reimburses work that is not theirs, such as SSI (CRS).
- **The decision:**
  - the OASDI share of SSA's restoration is charged to the Social Security trust funds;
  - the Medicare share is charged to Medicare;
  - the general fund pays the SSI share and the Climate Dividend work.
- **Why.**
  - It is the existing system, and it keeps benefit administration paid for by the program it serves.
  - The cost is small: about $3B a year at the midpoint, roughly 0.02% of taxable payroll, under half a percent of the 4.42% gap.
  - The project's Social Security goals do not require departing from it.
- **What it changes.** CAP-7 should carry only the general-fund share of SSA's increase. The SSA figures in the table are gross, so the general-fund sustained claim is lower than shown by the OASDI and Medicare shares. The current split by source was not found; Codex should take it from SSA's budget.
- **Recommended, not decided: who runs paid leave.** SSA should administer paid leave on the FAMILY Act model, financed by the leave fund on the same principle.

## Surge recommendation, after pricing the three items (Oct 26)

**The three items Espen asked to price:**

| Item | What it costs | Where it sits | Effect on the surge |
| --- | --- | --- | --- |
| **HLT-2 claims and contractor operations** | Build about $1B (inside CMS's existing $8B launch surge). Recurring about $0.25B a year (range $0.15-0.4B) from 2031 | Build: CMS surge, unchanged. Recurring: new CMS sustained row, paid through the SMI trust fund | None. Sustained +$2.9B |
| **CLI-7 future-conditions flood mapping** | Completion about $9B (range $4-15B). Maintenance about $0.1B a year above the current program | FEMA. Completion is a finite federal data build with a return case, so it sits in the surge | **+$9B** |
| **CAP-13 overlap check** | Residual about $8B (range $4-15B), down from the unsourced $30B | Surge (state and local implementation) | **-$22B** |

- **HLT-2.** The new benefits add about 85 million traditional-Medicare claims a year: dental about 40M, vision about 40M, hearing about 5M. Medicare Advantage enrollees get these benefits through their plans' bids. That is about 7% more claims on a contractor base that costs about $0.72B a year to process 1.2-1.3B claims, so processing itself is cheap. Most of the recurring cost is enrolling and screening dentists, optometrists and audiologists, plus appeals, beneficiary calls and dental fraud control. It is far smaller than the round 1 worry.
- **Flood mapping.** ASFPM's 2020 estimate is $3.2-11.8B to complete the nation's flood maps, scaled about 30% to 2030 dollars. FY2026 mapping partner grants allow no new map starts.
- **CAP-13.** Most state work is already funded inside the program rows:
  - elections: DEM-11;
  - Medicaid eligibility: the federal administrative match, which CBO's Medicaid scores include;
  - child care: state administration is likely inside FAM-2's allotments, on the existing child care block grant model;
  - Title I and IDEA: their state set-asides;
  - housing finance agencies: their fees;
  - paid-leave partnerships: the leave fund.

  What remains is cross-program state eligibility and integration systems, pre-launch planning before program money flows, and direct local grants where a state opts out (FAM-2D).

**All entities now need:**

| Layer | Surge | Sustained, FY2030-39 |
| --- | --- | --- |
| Restore 2025-26 losses | 9.4 (5.6-15.4) | 177.2 (120.2-227.4) |
| Pre-2025 shortfalls | 25.9 (13.5-42.2) | 11.4 (4.3-20.5) |
| Agenda work | 24.6 (12.3-45.7) | 66.0 (36.2-107.3) |
| **Total** | **59.8 (31.4-103.3)** | **254.6 (160.7-355.1)** |

**Following Codex's review,** the last named items are each split into a finite build (surge) and recurring operations (sustained), so the surge carries no recurring costs:
- **Mark-to-market unit:** $0.3B set-up, plus $0.15B a year.
- **IRS dividend work:** $0.5B build, plus $0.1B a year.
- **ROAD Act programs:** $0.5B set-up, plus $0.1B a year.

**Recommendation: size the surge (CAP-7S) at about $105B.** Espen's decision; the $300B stays until they decide.
- **Why $105B.** It covers the high case ($103B). Every named finite build is now priced, so no extra reserve is needed for them.
- **The rest of the $300B ($240B at the midpoint) has no identified use.** If Espen wants a margin for needs nobody has written down, a named contingency of a stated size is better than an unallocated balance.
- **Effect.** About $195B less borrowing inside the D4-B investment envelope, mostly FY2030-35. FY2040 is unaffected, because the surge ends.
- **No surge-to-sustained transfer is proposed.** The recurring parts are already in sustained, and sustained has no spare room at the high case (below).
- **What the surge holds now.** The pre-2025 layer is now the largest part: modernization at the IRS, SSA and student aid, flood maps, and backlogs.

**Sustained: $300B is a planning ceiling. Its adequacy is conditional.**

| Reading | Need, FY2030-39 | Against $300B |
| --- | --- | --- |
| Midpoint | $254.6B | $45B under |
| High | $355.1B | **$55B over** |
| Unpriced recurring | USDA conservation delivery, only if CLI-13 is chosen | Adds to both |

- **Trust-fund shares.** The table counts SSA gross ($31B). The Social Security and Medicare shares are charged to their trust funds under the current-law split, so the general-fund claim on CAP-7 is lower by those shares. The current split by source was not found.
- **What would push it over.** If the high case materialized, $300B would be short. Either the line rises (paid for at maturity under D4-B), or the lowest-priority rows wait. The midpoint fits.
- **Recommendation.** Keep $300B as the planning ceiling. Treat restoration rows as first claims and agenda rows as phased with their programs.

**FY2029.** A $5B shift (from $10B) is a planning alternative, not a resolved question.
- **Basis.** Cash for the reviewed agencies is about $1.7B (range $0.5-4.5B).
- **What it assumes:**
  - R1 enactment around April 2029;
  - small agencies under $0.1B each;
  - the four entities not reviewed in depth (ACF, HRSA, FNS, Fiscal Service) using little first-year cash.
- **Risks the other way.** Earlier enactment, faster hiring or unwritten needs would raise it. Decide it with the surge.

## All entities

| Entity | Surge | Sustained, FY2030-39 | Total | FY2040 run rate | Old split |
| --- | --- | --- | --- | --- | --- |
| IRS | 9.8 | 95.5 | 105.3 (65.6-138.1) | 12.6 | 236.2 |
| CMS | 8.0 | 17.4 | 25.4 (14.3-40.4) | 2.3 | 90.8 |
| HUD | 3.3 | 11.7 | 15.0 (9.4-23.9) | 1.5 | 81.8 |
| ED | 2.3 | 8.3 | 10.6 (5.8-15.5) | 1.1 | 72.7 |
| SSA (gross; mostly trust-fund financed) | 3.9 | 31.0 | 34.9 (19.5-49.8) | 4.0 | 99.9 |
| USCIS (asylum and refugee processing inside IMM-3) | 3.5 | 0.3 | 3.8 (1.9-6.6) | 0.0 | 83.6 |
| Development agency (capacity only; programs in DEV-P) | 4.0 | 24.7 | 28.7 (24.0-33.8) | 3.2 | 109.0 |
| State (diplomacy) | 0.5 | 11.4 | 11.9 (6.6-18.7) | 1.5 | 14.5 |
| CDC | 1.5 | 7.6 | 9.1 (5.4-15.7) | 1.0 | 27.2 |
| FEMA (includes flood maps) | 10.0 | 13.0 | 23.0 (12.5-36.8) | 1.7 | 14.5 |
| NOAA | 0.9 | 7.6 | 8.5 (6.2-12.9) | 1.0 | 72.7 |
| FTA (Moving America funds it from 2031) | 0.15 | 0 | 0.15 | 0 | 54.5 |
| EPA | 0.2 | 1.8 | 2.0 (1.1-3.4) | 0.2 | 9.1 |
| DOE | 0.2 | 1.9 | 2.1 (1.4-3.6) | 0.2 | 7.3 |
| DOL | 0.2 | 4.6 | 4.8 (2.8-6.7) | 0.6 | 10.9 |
| NLRB | 0.05 | 1.9 | 1.9 (1.3-3.3) | 0.2 | 7.3 |
| FTC and DOJ Antitrust | 0 | 0.4 | 0.4 (0-1.0) | 0.0 | 5.5 |
| Integrity units | 0.2 | 1.9 | 2.1 (1.1-3.4) | 0.2 | 21.8 |
| FEC | 0 | 0.5 | 0.5 (0.3-0.8) | 0.1 | 5.5 |
| EAC | 0 | 0.4 | 0.4 (0.3-0.6) | 0.0 | 5.5 |
| OPM | 0.3 | 1.0 | 1.3 (0.8-2.1) | 0.1 | 18.2 |
| Civil-rights offices | 0 | 2.3 | 2.3 (1.5-3.3) | 0.3 | 10.9 |
| CAISI and DOE labs | 0.3 | 1.6 | 1.9 (0.9-3.1) | 0.2 | 10.9 |
| ATF and NICS | 0.1 | 0.6 | 0.7 (0.4-1.5) | 0.1 | 9.1 |
| HHS ACF | 1.0 | 1.9 | 2.9 (1.5-5.8) | 0.2 | — |
| HRSA | 0 | 0.6 | 0.6 (0.3-1.3) | 0.1 | — |
| USDA FNS | 0 | 0.4 | 0.4 (0.1-0.8) | 0.0 | — |
| Treasury Fiscal Service | 0.3 | 0.6 | 0.9 (0.4-1.9) | 0.1 | — |
| Commerce BIS | 0 | 0.6 | 0.6 (0.3-1.3) | 0.1 | — |
| State and local implementation (CAP-13, residual) | 8.0 | 0 | 8.0 (4.0-15.0) | 0 | in no total |
| Digital service corps (CAP-12) | 0.5 | 3.2 | 3.7 (2.2-6.1) | 0.4 | — |
| Inspectors general and GAO oversight | 0.6 | 0 | 0.6 (0.4-1.0) | 0 | — |
| **All** | **59.8 (31.4-103.3)** | **254.6 (160.7-355.1)** | **314.4 (192.1-458.4)** | **33.0** | 1,079 |

**Program-row costs this review found (outside CAP; each needs its owner):**

| Cost | Where it belongs | Amount, FY2030-39 | Payer |
| --- | --- | --- | --- |
| DEV-P development programs | New permanent row | $92B ($70-115B) | General fund |
| Paid-leave administration | FAM-3 and the leave fund | $30B ($18-60B) | Leave fund |
| Voucher administrative fees (round 1) | HOU-4, inside HOU-1 | $12.2B ($8.1-15.2B) | General fund |

**Midpoint sustained path, $B nominal FY2030-39:** 10.4, 18.1, 24.4, 25.9, 26.8, 27.8, 28.8, 29.8, 30.8, 31.9.

## Agency notes (changes since the first round 2 draft)

- **NOAA:** revised as above.
- **SSA:** the pre-2025 layer rose to about +4,000 staff ($0.8B a year), because January 2025 staffing was already a multi-decade low.
- **FEMA:** about +5,000 staff, including a pre-2025 shortfall against FEMA's own targets (estimate).
- **Development agency:** decided as above.
- **USCIS:** the asylum and refugee processing row is reconciled with IMM-3 (Codex review). IMM-3 already carries about $10B of processing costs for asylum officers, regional processing and port screening. The bottom-up need (about $5.4B) fits inside it, so CAP carries only the backlog, online filing and the Office of New Americans. IMM-3 is about double the bottom-up figure; the immigration owner may trim it.
- **IRS and HUD:** the mark-to-market unit, dividend work and ROAD Act programs are priced, each split into a finite build and recurring operations.
- **CDC:** public health grants clawed back in 2025 were time-limited COVID-era money, so they are not restored. NSC-8 carries its program money.
- **New entities:**
  - **CAP-13** ($30B surge): it was in no total.
  - **Digital service corps** ($0.25B a year plus a $0.5B build): 18F was terminated in 2025 and USDS became DOGE.
  - **Surge oversight** (about 1% of the surge): the ARRA and IRA precedents.
  - **DOE's contracts-for-difference office** for CLI-9.
  - **Commerce BIS licensing** for NSC-7.
- **Other agencies:** their rows are unchanged from the first draft. The CSV has their basis.

## Proposed input changes (for the owners; not made here)

1. **Codex: integration and the funds model.**
   - Add **DEV-P** as a general-fund program row with its path, and record its financing need under D4-B.
   - Add **paid-leave administration** to the leave-fund model, at about 3% of benefits plus start-up.
   - Carry **SSA's OASDI and HI shares** of the restoration in the funds model and only the general-fund share in CAP-7.
   - **If Espen accepts:** `cap_surge_tn` 0.3 → about 0.11 and `early_admin_bn` 10 → 5. `cap_sustained_tn` stays 0.3. No change until they decide.
2. **Housing owner:** the HOU-4 fee correction from round 1.
3. **Governing record, on Espen's acceptance:**
   - Record the two delegated decisions: development-agency categorization and SSA financing.
   - Extend D9's list to the added entities.
   - Count CAP-13 in the surge.
4. **Family domain:** name SSA as the paid-leave administrator, financed by the leave fund (recommended).

## Uncertainty and limits

- **Mostly estimates.** Most figures are estimates built on sourced baselines. Staffing losses often come from press and advocacy reporting, which Espen accepts for the 2025-26 cuts.
- **DEV-P** uses FY2024 non-emergency account levels and a crosswalk to the FY2026 consolidated accounts (National Security Investment Programs and International Humanitarian Assistance). The crosswalk is approximate.
- **Paid-leave administration** rests on a 2-6% band, not a score.
- **CAP-13's $30B** is the project's prior unsourced estimate, now counted but not re-derived.
- **Not an official score.**

## Sources (added in this revision)

- ASFPM, [Flood Mapping for the Nation (2020)](https://www.floods.org/asfpm-history-ctp/2020-flood-mapping-for-the-nation/).
- [ASFPM on FEMA flood map funding](https://www.floods.org/annual-legislative-activities/asfpm-makes-case-for-fema-flood-map-funding-in-letter-to-omb/).
- HFMA, [CMS FY2026 budget (MAC claims processing)](https://www.hfma.org/payment-reimbursement-and-managed-care/more-details-on-hhs-budget-proposals-for-fy26/).
- CMS, [FY2026 Program Management operating plan](https://www.cms.gov/files/document/fy-2026-program-management-operating-plan.pdf).

- CRS, [NOAA FY2026](https://www.everycrsreport.com/files/2026-03-12_IF13024_eb7ce330a93e719e4ae88b7880d3a76d47b0721b.html).
- E&E News, [NOAA early retirements](https://www.eenews.net/articles/more-than-1000-noaa-staffers-take-early-retirement/).
- [NPR on Regional Climate Centers](https://www.stlpr.org/2025-04-18/regional-climate-centers-shut-down-abruptly).
- CRS, [SFOPS FY2024](https://www.everycrsreport.com/files/2024-07-16_R47579_9b231b0a8d9129a4e0b72772b4ed5de4e40e6edb.html) and [SFOPS/NSRP FY2026](https://www.everycrsreport.com/files/2026-07-15_R48624_48cf729af75f7e8e8c710d63e39078520bd54f59.html).
- [USAID workforce reporting citing CRS](https://www.nbcnewyork.com/news/national-international/usaid-announces-nearly-all-direct-hires-will-be-placed-on-administrative-leave/6136471/?amp=1).
- CRS, [SSA LAE FY2023 (funding mechanism)](https://www.everycrsreport.com/reports/R47480.html).
- The first draft's sources are in git history at commit 268fd8d.
