# Capacity recovery review, round 2: the other agencies and the scope of capacity

**Status:** review-ready, revised Oct 26 after Espen's questions (Claude Code; branch `claude/pensive-mendel-g1lwl5` from main aa8552d, PR #23). Evidence and recommendations.

Two items are decided under the project-coworker delegation, and are marked as such: how the development agency's spending is categorized, and how SSA's added staff are financed. **Espen accepted DEV-P and SSA administration of paid leave on Oct 26** (governing record). Nothing else here is adopted.

- **Data:** [capacity-recovery-components.csv](capacity-recovery-components.csv), 197 rows.
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
- **State and local implementation grants (CAP-13).** Estimated at $0.03T but in no total. Proposed: **count $30B inside the surge.**
- **Still unpriced:** Medicare claims operations for HLT-2's new benefits; FEMA's future-conditions flood mapping; and USDA conservation delivery, needed only if CLI-13 is chosen.

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

## Refined surge recommendation (no change yet)

All 32 entities in the review (the 28 agencies, the paid-leave administrator and the three shared lines) now need:
- **surge: about $72B (range $43-121B);**
- **sustained: about $252B (range $160-347B).**

| Layer | Surge | Sustained, FY2030-39 |
| --- | --- | --- |
| Restore 2025-26 losses | 9.4 (5.6-15.4) | 177.2 (120.2-227.4) |
| Pre-2025 shortfalls | 16.9 (9.5-27.2) | 10.1 (4.3-16.7) |
| Agenda work | 45.2 (27.8-78.1) | 64.1 (35.4-103.3) |
| **Total** | **71.5 (42.9-120.7)** | **251.5 (159.8-347.4)** |

**Hold the surge at $300B for now.** A smaller surge looks likely, but three pending items could still move it, so price them before resizing:
1. **CMS claims and contractor systems for HLT-2's new benefits,** the largest unpriced build.
2. **CLI-7's flood-mapping score.** If it lands in FEMA's capacity instead of CLI-7's program cost, it adds to the surge.
3. **The CAP-13 overlap check** against the child care, Medicaid-match and DEM-11 administration allowances. That could move the $30B either way.

Also unpriced are the IRS's dividend system and mark-to-market unit and HUD's ROAD Act programs, which are probably a few billion dollars together.

**Once those are priced,** the evidence points to a surge of about **$125B** (the high case of $121B plus room for those items). The rest of the $300B ($228B at the midpoint today) has no identified use.

**Sustained: keep $300B.** It now has $48B of headroom against the midpoint, but the high case ($347B) exceeds it. The general-fund share is lower than shown once SSA's trust-fund shares move out, and the headroom also has to cover HLT-2's recurring claims operations. It fits; it is not loose.

**FY2029.** Cash for all agencies is about $1.7B (range $0.5-4.5B) against the $10B shifted into FY2029, so a $5B shift is enough. Hold this with the surge decision.

## All entities

| Entity | Surge | Sustained, FY2030-39 | Total | FY2040 run rate | Old split |
| --- | --- | --- | --- | --- | --- |
| IRS | 9.0 | 92.4 | 101.4 (63.7-130.2) | 12.2 | 236.2 |
| CMS | 8.0 | 14.5 | 22.5 (12.5-35.8) | 1.9 | 90.8 |
| HUD | 2.8 | 10.4 | 13.2 (8.6-20.4) | 1.3 | 81.8 |
| ED | 2.3 | 8.3 | 10.6 (5.8-15.5) | 1.1 | 72.7 |
| SSA (gross; mostly trust-fund financed) | 3.9 | 31.0 | 34.9 (19.5-49.8) | 4.0 | 99.9 |
| USCIS | 3.5 | 5.7 | 9.2 (5.1-16.1) | 0.7 | 83.6 |
| Development agency (capacity only; programs in DEV-P) | 4.0 | 24.7 | 28.7 (24.0-33.8) | 3.2 | 109.0 |
| State (diplomacy) | 0.5 | 11.4 | 11.9 (6.6-18.7) | 1.5 | 14.5 |
| CDC | 1.5 | 7.6 | 9.1 (5.4-15.7) | 1.0 | 27.2 |
| FEMA | 1.0 | 11.7 | 12.7 (8.5-18.0) | 1.5 | 14.5 |
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
| State and local implementation (CAP-13) | 30.0 | 0 | 30.0 (20.0-50.0) | 0 | in no total |
| Digital service corps (CAP-12) | 0.5 | 3.2 | 3.7 (2.2-6.1) | 0.4 | — |
| Inspectors general and GAO oversight | 0.6 | 0 | 0.6 (0.4-1.0) | 0 | — |
| **All** | **71.5 (42.9-120.7)** | **251.5 (159.8-347.4)** | **323.0 (202.8-468.1)** | **32.6** | 1,079 |

**Program-row costs this review found (outside CAP; each needs its owner):**

| Cost | Where it belongs | Amount, FY2030-39 | Payer |
| --- | --- | --- | --- |
| DEV-P development programs | New permanent row | $92B ($70-115B) | General fund |
| Paid-leave administration | FAM-3 and the leave fund | $30B ($18-60B) | Leave fund |
| Voucher administrative fees (round 1) | HOU-4, inside HOU-1 | $12.2B ($8.1-15.2B) | General fund |

**Midpoint sustained path, $B nominal FY2030-39:** 10.4, 17.9, 24.1, 25.6, 26.5, 27.4, 28.4, 29.4, 30.4, 31.5.

## Agency notes (changes since the first round 2 draft)

- **NOAA:** revised as above.
- **SSA:** the pre-2025 layer rose to about +4,000 staff ($0.8B a year), because January 2025 staffing was already a multi-decade low.
- **FEMA:** about +5,000 staff, including a pre-2025 shortfall against FEMA's own targets (estimate).
- **Development agency:** decided as above.
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
   - **No change to `cap_surge_tn`, `cap_sustained_tn` or `early_admin_bn` yet**, pending Espen's surge decision.
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

- CRS, [NOAA FY2026](https://www.everycrsreport.com/files/2026-03-12_IF13024_eb7ce330a93e719e4ae88b7880d3a76d47b0721b.html).
- E&E News, [NOAA early retirements](https://www.eenews.net/articles/more-than-1000-noaa-staffers-take-early-retirement/).
- [NPR on Regional Climate Centers](https://www.stlpr.org/2025-04-18/regional-climate-centers-shut-down-abruptly).
- CRS, [SFOPS FY2024](https://www.everycrsreport.com/files/2024-07-16_R47579_9b231b0a8d9129a4e0b72772b4ed5de4e40e6edb.html) and [SFOPS/NSRP FY2026](https://www.everycrsreport.com/files/2026-07-15_R48624_48cf729af75f7e8e8c710d63e39078520bd54f59.html).
- [USAID workforce reporting citing CRS](https://www.nbcnewyork.com/news/national-international/usaid-announces-nearly-all-direct-hires-will-be-placed-on-administrative-leave/6136471/?amp=1).
- CRS, [SSA LAE FY2023 (funding mechanism)](https://www.everycrsreport.com/reports/R47480.html).
- The first draft's sources are in git history at commit 268fd8d.
