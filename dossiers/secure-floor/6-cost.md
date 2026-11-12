# A secure floor for every household: cost

Role: section 6 of the secure floor dossier. It prices the provisions of `4-specification.md` on federal fiscal years against the January 2029 law, reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`), reprices memo 1 A without the $2,200 floor Espen declined, and re-runs the child-poverty model on the decided design. Status: draft (stage D, board row S4, PR 1), on `DEC-2026-11-12-06`. Every figure is project arithmetic, not an official score. **Nothing is booked here**: booking is a separate later step, and part 6 lists exactly which ledger rows and inputs it would change.

## Counting rules

- **Conventions.** Federal cost, nominal $ billion unless marked, against the January 2029 law (section 1, part F), a cost positive.
- **Fiscal years.** FY y runs from October of y-1. A benefit paid monthly in calendar year y counts three quarters in FY y and a quarter in FY y+1, as care's and health's paths do. A refundable credit claimed on the return (the childless earned income credit, the refundable dependent care credit, the safe harbor) is paid in the filing season after its tax year, so tax year 2030 lands in FY2031. SNAP's and SSI's changes are fiscal-year amounts from FY2030.
- **The path.** `tools/secure_floor_path.py` (run: `python3 dossiers/secure-floor/tools/secure_floor_path.py`). Each line's anchor and growth are in its comments, judgment labeled. The child benefit's floor is priced by `tools/afa_floor.py` on the official CPS ASEC 2026 public-use file (income year 2025; SHA-256 `fe819d0d…7d93`, the hash the legacy baseline records), which stays outside the repository.
- **The booked basis.** The budget model's central case (`mixed`), as committed at `34faa21`: FAM-1 at $1,900 billion over FY2030-39 and $214.7 billion in FY2040; the participation envelope (LAB-10) at $100 billion and $14.0 billion; paid leave through the leave fund at high take-up; Social Security through the model's own fund run. Read from the model's audit lines, not rebuilt.
- **Each figure's status** (commitment, working assumption, open question) is in part 8.

## 1. The decided set on the general fund, by fiscal year

| Line | Provision | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The child benefit, as booked | FAM-1 | 171.4 | 175.3 | 179.3 | 183.3 | 187.4 | 191.7 | 196.0 | 200.5 | 205.1 | 209.9 | **1,900.0** | **214.7** |
| less the $2,200 floor, declined | FAM-1.02 | −3.0 | −3.9 | −4.4 | −4.5 | −5.0 | −4.9 | −5.2 | −5.7 | −5.5 | −5.6 | **−47.7** | **−5.8** |
| The child's own ID | FAM-1.04 | 1.9 | 2.5 | 2.6 | 2.7 | 2.7 | 2.8 | 2.8 | 2.9 | 3.0 | 3.1 | **27.0** | **3.1** |
| Records-based delivery | FAM-1.08 to 1.10 | 1.5 | 1.5 | 1.6 | 1.6 | 1.6 | 1.7 | 1.7 | 1.8 | 1.8 | 1.8 | **16.7** | **1.9** |
| The repayment safe harbor | FAM-1.06 | 0 | 1.0 | 1.0 | 1.0 | 1.1 | 1.1 | 1.1 | 1.1 | 1.2 | 1.2 | **9.9** | **1.2** |
| The childless earned income credit | INC-1.01 | 0 | 14.9 | 15.2 | 15.5 | 15.8 | 16.1 | 16.5 | 16.8 | 17.1 | 17.5 | **145.3** | **17.8** |
| SNAP restored | INC-2.01 | 20.5 | 21.0 | 21.5 | 22.1 | 22.6 | 23.2 | 23.8 | 24.4 | 25.0 | 25.6 | **229.7** | **26.2** |
| SSI's asset limits | INC-3.01 | 1.1 | 1.1 | 1.2 | 1.2 | 1.2 | 1.3 | 1.3 | 1.4 | 1.4 | 1.4 | **12.6** | **1.5** |
| SSI's exclusions indexed | INC-3.02 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | **10.5** | **1.6** |
| The refundable dependent care credit | INC-4.01 | 0 | 4.5 | 4.6 | 4.7 | 4.8 | 5.0 | 5.1 | 5.2 | 5.3 | 5.5 | **44.8** | **5.6** |
| The exclusion rule's forgone offsets | INC-5.01 | 0 | 2.0 | 2.1 | 2.1 | 2.2 | 2.3 | 2.3 | 2.4 | 2.5 | 2.5 | **20.3** | **2.6** |
| Paid on-ramps, as booked | LAB-10 | 2.4 | 5.0 | 7.8 | 10.8 | 11.2 | 11.6 | 12.1 | 12.5 | 13.0 | 13.5 | **100.0** | **14.0** |
| **The secure floor on the general fund** | | **196.4** | **225.7** | **233.2** | **241.4** | **246.8** | **252.9** | **258.7** | **264.6** | **271.3** | **277.8** | **2,469.1** | **284.4** |

- **Booked:** FAM-1 and LAB-10, $2,000 billion over FY2030-39 and $228.7 billion in FY2040.
- **Not booked (new lines):** about **$517 billion over FY2030-39 and $61.6 billion in FY2040**, within section 3's $0.45-0.6 trillion and $50-60 billion (a little above in FY2040, because the credits grow from their first year on fiscal years).
- **The floor declined:** about **−$48 billion over FY2030-39 and −$5.8 billion in FY2040** against the booked child benefit.
- **Net change a booking would make:** about **+$469 billion over FY2030-39 and +$55.8 billion in FY2040** (0.10% of GDP).
- *The other paths:* the INC lines' anchors and growth are memo 3's and section 3's judgment (on CBO's $187 billion of SNAP savings [EV-SEC-035], SSA's actuaries' $8.9 billion for SSI's limits [EV-SEC-630], the Tax Policy Center's $135.4 billion for the childless credit [EV-SEC-610]), laid on fiscal years; `secure_floor_path.py` gives each.

### Memo 1 A without the floor: what changed

Memo 1 priced A at about $1.9 trillion over FY2030-39 (range $1.7-2.1 trillion), with the $2,200 floor "small, inside the range". Espen declined the floor (point 2), so the bill's own phase-out applies (FAM-1.02). On the CPS file (`tools/afa_floor.py`):

| Tax year | 2030 | 2032 | 2034 | 2036 | 2038 | 2040 |
| --- | --- | --- | --- | --- | --- | --- |
| What the floor would pay ($ billion) | 4.0 | 4.6 | 5.1 | 5.3 | 5.4 | 5.9 |
| Children in families getting less than the 2029 law (million) | 8.8 | 8.7 | 8.6 | 8.1 | 7.5 | 7.5 |
| Their families (million) | 5.4 | 5.4 | 5.3 | 5.0 | 4.7 | 4.7 |

- **Who.** Couples above about $210,000 and other filers above about $165,000 in 2030, where the bill's credit has fallen below the law's $2,200 indexed (about $2,500 in 2030); the most a family loses is the gap between the law's indexed credit and the bill's unindexed $2,000 a child, about $500 a child in 2030 and $1,100 in 2040, and the gap closes again as both phase out above $400,000.
- **The cost.** The floor would have cost about $4-6 billion a year: **about $0.05 trillion over FY2030-39 and $6 billion in FY2040** on fiscal years. The decided child benefit is therefore about **$1.85 trillion over FY2030-39 (range $1.65-2.05 trillion) and $209 billion in FY2040** on the booked profile.
- **Poverty.** None of it reaches poor children: about 5,500 of the source year's 9.7 million poor children live in families that get less, well below the model's precision. The poverty results (part 3) are unchanged.
- **Why the range moves by the floor alone.** The legacy $1.9 trillion is a planning range anchored to the Tax Policy Center's score of the bill as written, about $1.4 trillion over FY2026-35 [EV-SEC-690] [EV-SEC-266], which has no floor, but memo 1 said the floor was inside it. Taking the floor out of the decided design lowers the central figure by its value and leaves the range's width.
- **A static check on the CPS file.** At full take-up, with no behavior, the bill's credit (newborn month excluded) costs about $109 billion a year more than the source year's credits in 2025 dollars, about $123 billion in 2030 prices, for the 67.9 million children the public-use file links to a claimant (project arithmetic). Scaled to the 72 million children Census counts, about $130 billion in 2030, or about $1.45-1.5 trillion over FY2030-39 growing with prices. That sits below the legacy range, as the Tax Policy Center moved to the 2030s (about $1.6-1.7 trillion, memo 1) does. The booked range carries the reach memo 2 B adds (about $10-20 billion a year, memo 2), the newborn month and the file's known undercount of income. It is not trimmed here (`DEC-2026-11-10-05`); a JCT or Treasury score would settle it (`4-specification.md`, "Evidence still needed").

## 2. What the total leaves out

| Item | Provision | FY2030-39 | FY2040 | Basis | Firm or contingent |
| --- | --- | --- | --- | --- | --- |
| The $500 credit for other dependents | FAM-1.11 | none against the 2029 law; about $0.05-0.07 trillion against the bill as written | about $5-7 billion against the bill | About 14.8 million adults claimed as dependents at $500 (CPS; an upper bound, the credit being nonrefundable). Whether the Tax Policy Center's score counts the bill's ending of it is not known. Kept as recommended, pending Espen | Open (Espen) |
| SNAP's immigrant rules (sec. 10108) | INC-2.01 | outside | outside | Restored and priced by immigration's table (`DEC-2026-11-12-07`, memo 6 C: about $0.05-0.11 trillion for the whole table); not counted here, so not twice | Immigration's |
| A work response to the child benefit | FAM-1 | not counted | not counted | The legacy DY3 sensitivity, −$0.02 to −$0.12 trillion of lost receipts (`legacy-research.md`, 1.9); CBO's conventional scores leave it out; the evidence is contested (section 2, part A.2) | Not counted |
| The IRS's and SSA's general rebuild | CAP-7 | booked there | booked there | The legacy capacity lines; the child benefit's own build is counted above, so a change to CAP-7 does not lose it | Booked |
| Parents' added earnings from paid leave and child care | FAM-3 | not counted | not counted | The legacy DY6, $0.15-0.30 trillion with child care (`legacy-research.md`, 3.2) | Not counted |
| SS-11's loan | SS-11.01 | zero if the 2030 act passes on time | zero | A repayable loan of up to roughly the gap at depletion, about $400-450 billion a year (legacy estimate, `legacy-research.md`, 4.1), only if depletion comes first | Contingent, zero to that |
| SS-7's fallback | SS-7.01 | zero unless triggered | zero unless triggered | A trust-fund revenue, from 2035 at the earliest | Contingent |
| The exclusion rule in housing's books | INC-5.01 | inside INC-5.01 | inside | The forgone rent offsets fall in housing's voucher costs; counted once, here | Firm |

**All-in on the general fund:** about **$2.47 trillion over FY2030-39 and $284 billion in FY2040** (range about $2.1-2.7 trillion and $250-320 billion, part 7). It is not a score.

## 3. The child-poverty re-run on the decided design

**What was run.** The legacy microsimulation's comparison (`models/tools/child-poverty/comparison_analysis.py`) on the official Census archive, fetched again for this step from census.gov (November 12, 2026), with the output kept outside the repository. Its "adopted package" analogue, the American Family Act at 2025 real face amounts with one million housing awards, **retains $2,000.04 a child above the first phase-out, the bill's own $166.67 a month** (`comparison_analysis.py`, line 37). That is the decided design: no $2,200 floor. Every legacy result reproduced exactly (`legacy_moderate_reproduced: true`):

| Delivery case (analyst assumption) | Child SPM poverty | Deep poverty | Children lifted |
| --- | --- | --- | --- |
| Same-scenario baseline (2034 population basis) | 13.40% | 3.45% | — |
| Moderate | 8.73% | 1.97% | 3.12 million |
| Enhanced | 8.34% | 1.85% | 3.38 million |
| Full | 8.09% | 1.78% | 3.55 million |

[EV-SEC-692] [EV-SEC-674]

**The decided design's own pieces, on top.**
- *The floor declined:* no change (part 1).
- *The child's own ID (FAM-1.04) and records-based enrollment (FAM-1.08):* the model has no number branch; coverage is a scalar (95% moderate, 98% enhanced). The decided rule removes the parent test that excludes about 500,000 children [EV-SEC-016], and memo 2 B targets the children a filing-based design misses, so the decided delivery sits between the moderate and enhanced cases: **about 8.3-8.7%** on source-year incomes (judgment).
- *The 2029 baseline:* the model cannot rebuild it (`legacy-research.md`, 2). The 2025 law's SNAP and Medicaid cuts push it up (Urban: 0.8 million more children in deep poverty [EV-SEC-634]; judgment +0.5 to +1.5 points, section 3). INC-2.01 restores SNAP, which takes back part of that rise; the Medicaid part is health's restoration (HLT-1). With both, the rise is at the low end (judgment).
- *A work response:* none in the model. The largest predicted response cuts the reduction by about a third (Corinth and others' 34% to 22% [EV-SEC-218]), about 1.6-1.7 points here (project arithmetic).

**Result (working assumption, `DEC-2026-11-10-07`):** child SPM poverty under the decided design on the 2029 baseline is **about 9% (range 8-12%)**, against a 2029 baseline of about 13.5-14.5%; about 3 million to 3.5 million fewer poor children. S3's working assumption (about 9-10%, range 8-12%) holds; SNAP's restoration moves it toward the low end. *Cost of being wrong:* it changes section 9's numbers, not any choice. *Still to do with the household model:* the 2029 baseline itself, an explicit number branch and the employment range (section 7).

## 4. The funds: paid leave and Social Security

**Paid leave (FAM-3), booked at high take-up** (mature cost 1.01% of payroll, the case the 1.10% ceiling is built for; `models/tools/recovery-budget/model.py`, `leave_fund`):

| FY | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **2030-39** | **2040** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contribution rate (%) | 0.60 | 0.60 | 0.65 | 0.70 | 0.75 | 0.80 | 0.85 | 0.90 | 0.95 | 1.00 | | 1.05 |
| Contributions | 79 | 83 | 93 | 105 | 117 | 130 | 143 | 157 | 172 | 188 | **1,269** | **204** |
| Benefits | 0 | 70 | 116 | 152 | 158 | 165 | 171 | 177 | 183 | 190 | **1,382** | **197** |
| SSA administration | 3.0 | 2.1 | 3.5 | 4.6 | 4.7 | 4.9 | 5.1 | 5.3 | 5.5 | 5.7 | **44** | **5.9** |
| Treasury loan, year end | 0 | 0 | 0 | 0 | 28 | 70 | 107 | 137 | 161 | 176 | | **182** |
| General fund's income-tax offset | 9.9 | 10.4 | 11.7 | 13.1 | 14.6 | 16.3 | 17.9 | 19.7 | 21.5 | 23.5 | **159** | **25.6** |

- **The decided design fits the booking.** The FAMILY Act's bands pay more at the bottom and less at the top; on average they are roughly cost-neutral against the legacy "about two-thirds" (memo 5's judgment), so the booked benefits stand. Memo 5's central $0.9 trillion is the middle take-up case; the booking uses the high case, $1.4 trillion, which is the prudent basis for the fund.
- **The loan.** At high take-up the loan peaks at about $185 billion on the fund's own scale in FY2040 (about $182 billion as booked) and is repaid in 2058; it is a fund balance, not a general-fund line. *A correction for the board:* the board's row D-9c reports the loan peaking at $124 billion and repaid by 2048 at the 1.10% ceiling. That is the funds model (`legacy/index/dedicated-funds.md`) without SSA's administration; the recovery budget's central case, with administration, gives the figures above (`legacy-research.md`, section 0, point 4, found the same).
- **The general fund's share:** the income-tax offset (12.5% of contributions, an allowance, not a JCT score; the 24.4% question in board question 0q is for excises, not this) is booked: about $159 billion over FY2030-39 and $25.6 billion in FY2040.

**Social Security (the 2030 act), on the trust funds.** Effects in percent of taxable payroll over 75 years on SSA's 2026 single-provision scores (memo 6):

| Piece | Effect | Provision |
| --- | --- | --- |
| SS-1, SS-2, SS-3, SS-4 (D8) | about +2.85 after the stacking haircut [EV-SEC-695] | SS-1.01 to 4.01 |
| SS-5 | about +0.87 (D8 with SS-5 about +3.7, 84% of the 4.42% gap) [EV-SEC-696] | SS-5.01 |
| SS-8, the reserve investment | about +0.5 to +1.0 (legacy estimate) [EV-SEC-697] | SS-8.01 |
| SS-B4, the caregiver credit | judgment −0.1 to −0.2 | SS-B4.01 |
| **The decided package** | **about +4.0 to +4.6 against the 4.42% gap**: at or near 75-year balance; SS-7.01 covers a shortfall | |

(Memo 6's +4.2 to +4.7 for part 1 and −0.5 to −0.6 for part 2 counted SS-3 and SS-4 in both; netted once, as above, the package is +4.0 to +4.6.) No whole-package score exists [EV-SEC-477]; point 12 asks for one.

**What the budget model books for Social Security, and where it differs.** The central case does not use the SS-1 ledger row (its note says "net −$2.75T"; its path sums to −$4.74 trillion). It runs its own fund model of SS-1 to SS-5 **plus a broad two-point payroll rate phased in over 2035-44** and a joint-interaction adjustment (`model.py`, `build_case`; `legacy-research.md`, 4.5): about $5.70 trillion of trust-fund revenue over FY2030-39, and $520 billion of income-tax offset on the general fund ($90 billion in FY2040). **The decided design has no broad rate unless SS-7.01's trigger fires, and then one point, not two; it closes the gap with SS-8.** So the booking overstates trust-fund revenue from 2035 and the general fund's offset with it. The size depends on how the model records SS-8's purchases of stocks, which is open for the booking step (part 6): CBO's treatment of a trust fund's stock purchases, and whether they change the unified deficit, needs a check before it is modeled.

## 5. The fiscal-rule report

Each figure has one basis: federal fiscal years, $ billion, a cost positive, against what the budget model books (case `mixed`, commit `34faa21`).

| Measure | FY2030-39 | FY2040 (permanent) |
| --- | --- | --- |
| The secure floor on the general fund, as decided (part 1) | $2,469 billion | $284 billion (0.53% of GDP) |
| Already booked for the same purposes: FAM-1; LAB-10 | $1,900 billion; $100 billion | $214.7 billion; $14.0 billion |
| **Net change a booking would make** | **about +$469 billion** | **about +$55.8 billion (0.10% of GDP)** |
| *of which:* the floor declined | −$48 billion | −$5.8 billion |
| *of which:* new lines (memo 3, points 4, 7 and 8, memo 1 part 2, memo 2, memo 7) | +$517 billion | +$61.6 billion |
| Paid leave: the general fund's income-tax offset (booked) | $159 billion | $25.6 billion |
| Social Security: on its trust funds; the general fund's offset as booked overstates the decided package (part 4) | — | — |

- **The yearly cost** is in part 1: about $196 billion in FY2030 rising to $278 billion in FY2039.
- **Permanent cost from FY2040: about $284 billion a year** on the general fund, growing with prices and the child population. Every line is permanent; nothing in the set sunsets.
- **Its share of the plan-wide margin.** The plan-wide general-fund primary gap in FY2040 is **$4,182.6 billion short** as booked (7.7% of GDP; `agenda_gf_primary_bn`, case `mixed`, a positive figure a shortfall). A booking of the decided set adds about $55.8 billion, to about **$4,238 billion (7.8% of GDP)**: **about 1.3% of the plan-wide gap**. The secure floor's whole general-fund cost, booked and new, is about **6.7% of that gap** in FY2040. Additive on the primary balance before interest; the new lines carry no revenue offset (outlays and refundable credits).
- **The test years.** The decided costs are permanent and grow with prices (the benefit's amounts) and wages (paid leave). The leave fund's loan is repaid in 2058 at high take-up.
- It is a figure to report, not an error to fix (`DEC-2026-11-10-05`). No part of it goes to Espen on its own: the memos already weighed the cheaper designs that reach the same children (memo 1 B), and the one money question left is FAM-1.11, which is small.

## 6. What a booking would change (proposed, not made)

Tier 3, for the lead after the milestone review, on the same pattern as care's (`dossiers/care/6bcd-cost.md`, part 5) and health's (`models/tools/health_booking.py`). This PR changes none of `models/data/inputs/`.
1. `models/data/inputs/ledger-bills.csv`, line 13 (FAM-1, 1.7 / 1.9 / 2.1): to **1.65 / 1.85 / 2.05**, with the note "AFA without the $2,200 floor (DEC-2026-11-12-06); floor about $0.05T (dossiers/secure-floor/6-cost.md, part 1)". The CPI profile in `fiscal-profiles.csv` (line 13) stays.
2. New `ledger-bills.csv` rows on rail R1, general fund, one per new agenda item: INC-1 (0.145), INC-2 (0.23), INC-3 (0.023), INC-4 (0.045), INC-5 (0.02), with FAM-1.04, 1.06 and 1.08-1.10 (0.054 together) as a FAM-1 component or an FAM-1 row of its own; year shapes in `fiscal-years.csv` from `tools/secure_floor_path.py`; rows in `models/data/budget/provisions.csv`.
3. LAB-10: the participation envelope in `recovery-adoption.json` (`participation_tn`, 0.1) stays; its line gains the name LAB-10 in `provisions.csv` so the dossier's provisions trace to it.
4. FAM-3: no change. The bands are roughly cost-neutral; the booking already uses high take-up and the 1.10% ceiling (#266).
5. Social Security: `models/tools/recovery-budget/assumptions.json`, `social_security`: replace the two-point broad rate phased 2035-44 with the decided package, SS-8's reserve investment and SS-7.01's one-point contingent fallback, once it is settled how to record the stock purchases (part 4); and correct the SS-1 ledger row's note (−$2.75T against its −$4.74T path).
6. Incidence: `models/data/inputs/incidence-rows.csv` F1 (key `ctc`) to the decided design's distribution, which pays the top quintile less than the 2029 law (part 1's 5.4 million families); new rows for INC-1 and INC-2 (keys for low-wage workers and SNAP households).
7. `ledger-dynamic.csv` DY3 (the child credit's work response) stays as a sensitivity in no total.

## 7. Sensitivities

| Input | Central | Range | Effect on FY2030-39 | Basis |
| --- | --- | --- | --- | --- |
| The child benefit's planning range | $1.85 trillion | $1.65-2.05 trillion | ±$0.2 trillion | Legacy range less the floor; the CPS static check is at the low end, the Tax Policy Center moved to the 2030s at about the low-to-middle |
| Real income growth in the floor's pricing | 1.0% a year | 0.5-1.5% | ±$0.01 trillion | More growth pushes more families above the unindexed lines |
| SNAP's restoration | $0.23 trillion | $0.20-0.25 trillion | ±$0.03 trillion | CBO's window's later years [EV-SEC-035] [EV-SEC-038] |
| The childless credit | $0.145 trillion | $0.13-0.16 trillion | ±$0.015 trillion | JCT and TPC [EV-SEC-609] [EV-SEC-610] |
| The dependent care credit | $0.045 trillion | $0.03-0.06 trillion | ±$0.015 trillion | Section 3, point 7 |
| The child's own ID | $0.027 trillion | $0.02-0.03 trillion | small | 500,000 children [EV-SEC-016] |
| Paid leave take-up | high (booked) | low to high: $0.6-1.4 trillion of benefits | fund only | Legacy cases [EV-SEC-693] |
| **The general fund, all** | **$2.47 trillion** | **about $2.1-2.7 trillion** | | |

## 8. What each figure is

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| The child benefit's amounts, phase-out, ages, ID rule, payee | Commitment (decided) |
| Its cost range | Working assumption: legacy planning range less the floor, checked against the CPS and the Tax Policy Center |
| The floor's value | Working assumption: CPS static arithmetic, full take-up |
| The 2029 child-poverty rate | Working assumption, about 9% (8-12%), not on the critical path |
| The credit for other dependents | Open question for Espen (FAM-1.11) |
| The new lines' costs | Working assumptions on outside scores, laid on fiscal years |
| LAB-10's $100 billion | Commitment (the envelope); people served, about 400,000-900,000 over the decade, a working assumption (memo 4) |
| Paid leave's take-up | Working assumption; the booking uses the high case |
| Social Security's package effect | Working assumption on single-provision scores; to study with SSA's whole-package score (point 12) |
| How to book SS-8 | Open question for the booking step |
| SS-11's loan | Contingent, zero to the gap at depletion |
