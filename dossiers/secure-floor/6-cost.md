# A secure floor for every household: cost

Role: section 6 of the secure floor dossier. It prices the provisions of `4-specification.md` on federal fiscal years against the January 2029 law, reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`), reprices memo 1 A without the $2,200 floor Espen declined, and re-runs the child-poverty model on the decided design. Status: reviewed at L3 (milestone review `review-milestone.md`, #298; fixes #301; the booking, #304, was also the re-check), on `DEC-2026-11-12-06`, with INC-2.02 added on `DEC-2026-11-13-03`. Every figure is project arithmetic, not an official score. Parts 1-5 are the dossier's pricing; part 6 is the budget model's booking of it (`models/tools/secure_floor_booking.py`), with the leave fund and Social Security of part 4 as booked.

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
| SNAP's earned income deduction at 45% (Espen's option D, `DEC-2026-11-13-03`) | INC-2.02 | 12.0 | 12.4 | 12.7 | 13.1 | 13.5 | 13.9 | 14.3 | 14.8 | 15.2 | 15.7 | **137.6** | **16.1** |
| SSI's asset limits | INC-3.01 | 1.1 | 1.1 | 1.2 | 1.2 | 1.2 | 1.3 | 1.3 | 1.4 | 1.4 | 1.4 | **12.6** | **1.5** |
| SSI's exclusions indexed | INC-3.02 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | **10.5** | **1.6** |
| SSI in the territories (Espen, November 12, lead session) | INC-3.03 | 0 | 1.2 | 2.1 | 2.3 | 2.3 | 2.3 | 2.4 | 2.4 | 2.4 | 2.4 | **19.7** | **2.5** |
| The refundable dependent care credit, for care no other program pays for (Espen, November 13, option B) | INC-4.01 | 0 | 0.5 | 0.5 | 0.5 | 0.5 | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 | **5.0** | **0.6** |
| The exclusion rule's forgone offsets | INC-5.01 | 0 | 2.0 | 2.1 | 2.1 | 2.2 | 2.3 | 2.3 | 2.4 | 2.5 | 2.5 | **20.3** | **2.6** |
| Paid on-ramps, as booked | LAB-10 | 2.4 | 5.0 | 7.8 | 10.8 | 11.2 | 11.6 | 12.1 | 12.5 | 13.0 | 13.5 | **100.0** | **14.0** |
| **The secure floor on the general fund** | | **208.4** | **235.2** | **243.9** | **252.6** | **258.3** | **264.7** | **270.9** | **277.1** | **284.2** | **291.1** | **2,586.5** | **298.0** |

- **Booked:** FAM-1 and LAB-10, $2,000 billion over FY2030-39 and $228.7 billion in FY2040.
- **INC-2.02, added on Espen's option D** (`DEC-2026-11-13-03`), is a new line of about **$138 billion over FY2030-39 and $16.1 billion in FY2040**, booked as its own row (part 6, item 8). With it the new lines come to about $674 billion and $80.2 billion, and the set to about **$2,626 billion over FY2030-39 and $303 billion in FY2040**. The figures below, through part 5's first table, are the set before it, as #304 booked it.
- **INC-4, rescoped by Espen on November 13 (option B)** to care neither the child care guarantee nor the school-age block grant (CCDF) pays (`4-specification.md`, INC-4.01), is rebooked from $4.5 billion a year (a judgment, $3-6 billion) to about **$0.5 billion a year in tax year 2030 (range $0.2-1.0 billion)**: **$5.0 billion over FY2030-39 and $0.6 billion in FY2040**, down $39.8 billion and $5.0 billion. The household model measures $0.34 billion in 2029 at full take-up, all of it for school-age care in families below 85% of state median income (`models/tools/household/results.md`, section 6). The CPS reports what families paid, so the school-age care in it is already net of CCDF, whose school-age reach the plan keeps at today's level; netting CCDF's reach again (about 0.71 million children 5 to 12 a month against 2.99 million in paying families below its income line, EV-CAR-700) would give $0.28 billion, a lower bound. What the CPS cannot see is judged: spending it under-reports (about +$0.1 billion: the model gives $0.43 billion at half again as much spending, $0.49 billion at double, held down by the $3,000 and $6,000 limits and the earnings test) and care for a disabled adult (about +$0.1 billion, range 0-0.3); take-up below full takes about 15% off (range 0-30%). With it the set comes to about **$2,587 billion over FY2030-39 and $298 billion in FY2040**.
- **Not booked (new lines):** about **$537 billion over FY2030-39 and $64.0 billion in FY2040**, within section 3's $0.45-0.6 trillion and a little above its $50-60 billion in FY2040, because the credits grow from their first year on fiscal years and INC-3.03 was decided after section 3 (about $20 billion and $2.5 billion).
- **The floor declined:** about **−$48 billion over FY2030-39 and −$5.8 billion in FY2040** against the booked child benefit.
- **Net change a booking would make:** about **+$489 billion over FY2030-39 and +$58.2 billion in FY2040** (0.11% of GDP).
- *The other paths:* the INC lines' anchors and growth are memo 3's and section 3's judgment (on CBO's $187 billion of SNAP savings [EV-SEC-035], SSA's actuaries' $8.9 billion for SSI's limits [EV-SEC-630] and $20.7 billion for SSI in Puerto Rico [EV-SEC-705], the Tax Policy Center's $135.4 billion for the childless credit [EV-SEC-610]), laid on fiscal years; `secure_floor_path.py` gives each.

### INC-2.02: SNAP's earned income deduction at 45% (Espen's option D)

A working assumption (`DEC-2026-11-10-07`), on SNAP's own records rather than the household model's CPS bound:
- **The static gain.** Each earned dollar counts 25 cents less in net income, and SNAP takes 30 cents of net income: 7.5% of earnings for a household with net income above zero. FNS's FY2024 report counts 4.697 million such households among 5.950 million with earnings, averaging $1,645 a month across all earner households, not only those with net income [EV-SEC-616] (the subset with net income likely earns a little more, so the gain is, if anything, slightly understated): 4.697 million × $1,645 × 7.5% × 12 = **about $7.0 billion in FY2024**. (FY2023's report gives 4.744 million at $1,548, about $6.6 billion; checked against that original.)
- **The shelter interaction** (judgment). Lower income before the shelter deduction raises the excess shelter deduction by half the change, so net income falls by 0.375 of earnings instead of 0.25: about +50% for a household with an uncapped excess shelter deduction. In FNS's Table A.9 (the report behind EV-SEC-616), about 75% of earner households have an excess shelter deduction and 38.7% are at its maximum, so roughly 36-46% of them gain the extra half (the table does not say whether the 38.7% is of all earners or of those with the deduction): about +18-23%, to about $8.3-8.6 billion.
- **New entrants and take-up** (judgment). Households under the gross income test whose net income was just above the net test, and households whose small benefit was not worth claiming: about +10-20%. Households whose net income reaches zero take back a little. About **$9.5 billion in FY2024**.
- **To FY2030.** The gain moves with earnings, about 3.5% a year (judgment): **about $12 billion in FY2030**, then 3% a year, $138 billion over FY2030-39 and $16.1 billion in FY2040. **Range $8-16 billion in FY2030:** the low end has little shelter interaction and no new entrants; the high end has the full interaction, larger take-up and the 2029 caseload above FY2024's.
- **Against the $32 billion Espen was told.** #321's "up to about $32 billion a year" applied 7.5% to the CPS's annual earnings of every SNAP household in 2029 (`models/tools/household/results.md`, section 7). That is an upper bound by construction: SNAP counts income only in the months a household is on SNAP, while the CPS's annual earnings include the months before or after, often at higher wages; and it ignores households whose net income would reach zero. The central case, about $12 billion, is well below it; $32 billion stays the outer bound. *Cost of being wrong:* it changes the plan-wide gap by a few billion dollars a year, not the choice, which was made for the ceiling.

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
| The $500 credit for other dependents ends | FAM-1.11 | about −$0.05 to −$0.07 trillion against the 2029 law | about −$5-7 billion | About 14.8 million adults claimed as dependents at $500 (CPS; an upper bound, the credit being nonrefundable). Ended as the bill provides (`DEC-2026-11-12-09`); the booked FAM-1 range is unchanged, as the decision records, since whether the Tax Policy Center's score already counts it is not known. Not added to the totals | Firm (a saving, not counted) |
| SNAP's immigrant rules (sec. 10108) | INC-2.01 | inside INC-2.01 | inside | CBO's $187 billion is the whole nutrition subtitle, sec. 10108 included [EV-SEC-035] [EV-SEC-038]; immigration's memo 6 says the secure floor's SNAP restoration already prices it and does not count it again (`dossiers/immigration/memos/`, memo 6) | Firm, counted once here |
| A work response to the child benefit | FAM-1 | not counted | not counted | The legacy DY3 sensitivity, −$0.02 to −$0.12 trillion of lost receipts (`legacy-research.md`, 1.9); CBO's conventional scores leave it out; the evidence is contested (section 2, part A.2) | Not counted |
| The IRS's and SSA's general rebuild | CAP-7 | booked there | booked there | The legacy capacity lines; the child benefit's own build is counted above, so a change to CAP-7 does not lose it | Booked |
| Parents' added earnings from paid leave and child care | FAM-3 | not counted | not counted | The legacy DY6, $0.15-0.30 trillion with child care (`legacy-research.md`, 3.2) | Not counted |
| SS-11's loan | SS-11.01 | expected zero if the 2030 act passes on time (not yet shown on a year-by-year fund path; the booking step's) | zero | A repayable loan of up to roughly the gap at depletion, about $400-450 billion a year (legacy estimate, `legacy-research.md`, 4.1), only if depletion comes first | Contingent, zero to that |
| SS-7's fallback | SS-7.01 | zero unless triggered | zero unless triggered | A trust-fund revenue, from 2035 at the earliest | Contingent |
| The exclusion rule in housing's books | INC-5.01 | inside INC-5.01 | inside | The forgone rent offsets fall in housing's voucher costs; counted once, here | Firm |
| No offset or garnishment of the child benefit | FAM-1.07 | about $0.01-0.03 trillion | about $1-3 billion | Judgment: the refund offsets that would otherwise fall on the benefit [EV-SEC-701]. Only the federal-debt and federal-tax share is a federal cost; child support, state-debt and unemployment offsets pass to others and are not. No Treasury Offset Program volume is in the register yet. Not added to part 1's totals; booked in FAM-1 at $2 billion a year, the middle of the range (part 6) | Firm, not yet counted |
| The child benefit in the territories | FAM-1.07 | about $0.01-0.03 trillion | about $1-3 billion | Judgment: about 0.6 million children, mostly in Puerto Rico, at the benefit less what the 2029 law already pays them; whether the legacy FAM-1 range counts the territories is not known. Not added to part 1's totals; booked in FAM-1 at $2 billion a year, the middle of the range (part 6) | Firm, not yet counted |

**All-in on the general fund:** about **$2.59 trillion over FY2030-39 and $298 billion in FY2040** with INC-2.02 and INC-4 rescoped (range about $2.2-2.9 trillion and $255-335 billion, part 7; with INC-2.02 before INC-4's rescoping, $2.63 trillion and $303 billion; before INC-2.02, $2.49 trillion and $287 billion). It is not a score.

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

The contribution steps 0.10 points a year to the 1.10% ceiling (FAM-3.04; `DEC-2026-11-12-14`), as booked by the secure floor booking (part 6).

**Paid leave (FAM-3), booked at high take-up** (mature cost 1.01% of payroll, the case the 1.10% ceiling is built for; `models/tools/recovery-budget/model.py`, `leave_fund`):

| FY | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **2030-39** | **2040** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contribution rate (%) | 0.60 | 0.60 | 0.70 | 0.80 | 0.90 | 1.00 | 1.10 | 1.10 | 1.10 | 1.10 | | 1.10 |
| Contributions | 79 | 83 | 101 | 120 | 141 | 163 | 186 | 192 | 199 | 207 | **1,470** | **214** |
| Benefits | 0 | 70 | 116 | 152 | 158 | 165 | 171 | 177 | 183 | 190 | **1,382** | **197** |
| SSA administration | 3.0 | 2.1 | 3.5 | 4.5 | 4.7 | 4.9 | 5.1 | 5.3 | 5.5 | 5.7 | **44** | **5.9** |
| Fund balance, year end | 76 | 90 | 74 | 40 | 20 | 13 | 24 | 35 | 47 | 60 | | **73** |
| Treasury loan, year end | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | | **0** |
| General fund's income-tax offset | 9.9 | 10.3 | 12.6 | 15.0 | 17.6 | 20.3 | 23.2 | 24.0 | 24.9 | 25.8 | **184** | **26.8** |

- **The decided design fits the booking.** The FAMILY Act's bands pay more at the bottom and less at the top; on average they are roughly cost-neutral against the legacy "about two-thirds" (memo 5's judgment), so the booked benefits stand. Memo 5's central $0.9 trillion is the middle take-up case; the booking uses the high case, $1.4 trillion, which is the prudent basis for the fund.
- **No Treasury loan.** At high take-up the rate reaches the 1.10% ceiling in 2036 and the fund never borrows: its balance bottoms out at about $13 billion in 2035 and is about $73 billion in FY2040 (the recovery budget's central case, with SSA's administration). The 0.05-point step the legacy design used reached the ceiling only in 2041, so the fund borrowed up to about $182 billion as booked ($185 billion on the fund's own scale) in FY2040 and repaid it in 2058, with about $5-7 billion a year of interest near the peak; the faster step avoids that. The repayable loan (FAM-3.05) stays as the backstop. *The margin is still thin:* at high take-up the mature cost, 1.01% of payroll plus SSA's 3% of benefits, is about 1.04% against the 1.10% ceiling, and the balance is only about a month of benefits in 2035, so take-up above the high case would bring the loan back, and the general fund, as lender, carries that exposure (section 8). Once the balance passes one and a half years of benefits, the rate steps back down toward 0.6%.
- **The general fund's share:** the income-tax offset (12.5% of contributions, an allowance, not a JCT score; the 24.4% question in board question 0q is for excises, not this) is booked: about $184 billion over FY2030-39 and $26.8 billion in FY2040, more than at the 0.05 step because contributions rise sooner.

**Social Security (the 2030 act), on the trust funds.** Effects in percent of taxable payroll over 75 years on SSA's 2026 single-provision scores (memo 6):

| Piece | Effect | Provision |
| --- | --- | --- |
| SS-1, SS-2, SS-3, SS-4 (D8) | about +2.85 after the stacking haircut [EV-SEC-695] | SS-1.01 to 4.01 |
| SS-5 | about +0.87 (D8 with SS-5 about +3.7, 84% of the 4.42% gap) [EV-SEC-696] | SS-5.01 |
| SS-8, the reserve investment | about +0.05 to +0.2 at the 20% share (project arithmetic, below); the legacy estimate, +0.5 to +1.0, states no share [EV-SEC-697] | SS-8.01 |
| SS-B4, the caregiver credit | judgment −0.1 to −0.2 | SS-B4.01 |
| **The decided package before the fallback** | **about +3.6 to +3.8 against the 4.42% gap** (81-86%) | |
| SS-7.01, the fallback | expected to carry about 0.6 to 0.9 points; +0.9 to +1.0 if fully used [EV-SEC-697], somewhat less on its late start | SS-7.01 |
| **The decided package with the fallback** | **short of 75-year balance: the booked run shows about −0.31% of payroll (combined funds last to 2093) with SS-8 at zero; SS-8's +0.05 to +0.2 and the caregiver credit's −0.1 to −0.2 leave it about −0.2 to −0.45** | |

(Memo 6's +4.2 to +4.7 for part 1 and −0.5 to −0.6 for part 2 counted SS-3 and SS-4 in both; netted once, with the legacy SS-8 estimate, the package would be +4.0 to +4.6.) No whole-package score exists [EV-SEC-477]; point 12 asks for one.

**SS-8's yield at its specified share** (project arithmetic, from the milestone review, `review-milestone.md`, O-1). +0.5% of taxable payroll is about $60 billion a year in the 2030s, on payroll of about $12 trillion. At an excess return over Treasury bonds of about 3% a year, that needs about $2 trillion held in stocks; at 20% of reserves, reserves of about $10 trillion. The combined funds hold about $2.6 trillion and fall to zero in 2034 under current law [EV-SEC-400], and the package's revenue from 2031 roughly matches their yearly shortfall in the early 2030s, so reserves stay in the low trillions. At 20% of a few trillion dollars, SS-8 yields about +0.05 to +0.2. With it, D8 and SS-5 (+3.72) and the caregiver credit (−0.1 to −0.2), the package closes about +3.6 to +3.8. **So SS-7.01's fallback is the expected case:** its trigger reads the Trustees reports from 2035, its first 0.1-point step would come about 2037, and its full point about 2046. The decision stands (memo 6 C, `DEC-2026-11-12-06`): Espen kept it with the fallback as the expected case (Espen, November 12, lead session). A larger SS-8 share or an earlier SS-7 start would change this; both stay working choices to revisit with SSA's score. SSA's whole-package score (point 12) will settle it.

**What the budget model books for Social Security.** The central case does not use the SS-1 ledger row (net −$4.74 trillion over FY2030-39). It runs its own fund model of SS-1 to SS-5 with a joint-interaction adjustment (`model.py`, `build_case`; `legacy-research.md`, 4.5) and, as the decided package's expected case, **SS-7.01's one point, 0.1 a year from 2037 to the full point in 2046** (`DEC-2026-11-12-13`; `ASM-SS-FALLBACK`), in place of the broad two-point rate phased in over 2035-44 it carried before. Trust-fund revenue, net of the offset, is about $5.32 trillion over FY2030-39 (it was $5.70 trillion), and the general fund's income-tax offset about $467 billion ($71 billion in FY2040; it was $520 billion and $90 billion). **SS-8 is recorded at zero and flagged.** How the budget records a trust fund's purchases of stocks, as outlays that raise the unified deficit, as a means of financing, or with returns above Treasury's rate, is not settled, and the answer changes the unified figures by far more than SS-8's yield; it needs a check of CBO's and OMB's treatment (the Railroad Retirement trust's is the nearest precedent) before it is modeled. With SS-8 at zero and the caregiver credit (SS-B4.01) not yet on the fund engine, the fund run's 75-year balance is about −0.31% of payroll and the combined funds last to 2093; SS-8's +0.05 to +0.2 would narrow that, and the caregiver credit's −0.1 to −0.2 would widen it, so the decided package with the one-point fallback is expected to fall short of 75-year balance by roughly 0.2 to 0.45% of payroll. Espen kept the one-point cap (`DEC-2026-11-12-16`): the remaining gap is accepted and stated plainly, SS-11.01 keeps benefits full and on time, and SSA's whole-package score (point 12) will settle its size.

## 5. The fiscal-rule report

Each figure has one basis: federal fiscal years, $ billion, a cost positive, against what the budget model books (case `mixed`, commit `34faa21`).

| Measure | FY2030-39 | FY2040 (permanent) |
| --- | --- | --- |
| The secure floor on the general fund, as decided (part 1) | $2,489 billion | $287 billion (0.53% of GDP) |
| Already booked for the same purposes: FAM-1; LAB-10 | $1,900 billion; $100 billion | $214.7 billion; $14.0 billion |
| **Net change a booking would make** | **about +$489 billion** | **about +$58.2 billion (0.11% of GDP)** |
| *of which:* the floor declined | −$48 billion | −$5.8 billion |
| *of which:* new lines (memo 3, points 4, 7 and 8, memo 1 part 2, memo 2, memo 7, INC-3.03) | +$537 billion | +$64.0 billion |
| Paid leave: the general fund's income-tax offset (booked) | $184 billion | $26.8 billion |
| Social Security: on its trust funds; the general fund's offset as booked overstates the decided package (part 4) | — | — |
| **INC-2.02, SNAP's earned income deduction at 45% (`DEC-2026-11-13-03`), booked as INC-2B** | **about +$138 billion** | **about +$16.1 billion (0.03% of GDP)** |

- **The yearly cost** is in part 1: about $196 billion in FY2030 rising to $280 billion in FY2039.
- **Permanent cost from FY2040: about $287 billion a year** on the general fund ($303 billion with INC-2.02; $298 billion with INC-4 rescoped), growing with prices and the child population. Every line is permanent; nothing in the set sunsets.
- **Its share of the plan-wide margin.** The plan-wide general-fund primary gap in FY2040 is **$4,184.7 billion short** as booked at the head (7.7% of GDP; `agenda_gf_primary_bn`, case `mixed`, a positive figure a shortfall; the figure `DEC-2026-11-12-08` records, after #289; the secure floor's own booked lines are unchanged since `34faa21`). A booking of the decided set adds about $58.2 billion, to about **$4,242.9 billion (7.8% of GDP)**: **about 1.4% of the plan-wide gap**. The secure floor's whole general-fund cost, booked and new, is about **6.9% of that gap** in FY2040. *As booked (part 6):* **$4,229.9 billion short (7.8% of GDP)**, +$45.2 billion: the secure floor's rows add about $63 billion (part 1's +$58.2 billion and the two FAM-1.07 lines, about $5 billion), the leave step adds about $1 billion of income-tax offset, and Social Security's correction (part 4) takes about $19 billion of offset off the general fund. Additive on the primary balance before interest; the new lines carry no revenue offset (outlays and refundable credits).
- **The test years.** The decided costs are permanent and grow with prices (the benefit's amounts) and wages (paid leave). The leave fund needs no Treasury loan at high take-up with the 0.10-point step (part 4).
- **With option D** (part 6, item 8): the plan-wide FY2040 gap at the head before it is **$4,240.4 billion short** (7.83% of GDP); INC-2B adds $16.2 billion, to **$4,256.6 billion (7.86% of GDP)**, about 0.4% of the gap. The secure floor's whole general-fund cost is then about $303 billion in FY2040, about 7.1% of the gap.
- **With INC-4 rescoped and immigration's health line at two-thirds** (part 6, item 9; both rebooked in one step): the plan-wide FY2040 gap goes from **$4,256.6 billion to $4,245.4 billion short** (7.84% of GDP), $11.3 billion less: about $5.0 billion from INC-4 and $6.3 billion from immigration (`dossiers/immigration/6-cost.md`, part 7). The secure floor's whole general-fund cost is about $298 billion in FY2040, about 7.0% of the gap.
- It is a figure to report, not an error to fix (`DEC-2026-11-10-05`). No part of it goes to Espen on its own: the memos already weighed the cheaper designs that reach the same children (memo 1 B), and FAM-1.11 is decided (`DEC-2026-11-12-09`).

## 6. The booking

Tier 3, on the same pattern as care's (`dossiers/care/6bcd-cost.md`, part 5) and health's (`models/tools/health_booking.py`). The lead's booking derives the rows from `tools/secure_floor_path.py` in `models/tools/secure_floor_booking.py` and checks them in `models/tools/test_fiscal_secure_floor.py`. It books items 1 to 5 as listed, with the leave step at 0.10 points (`DEC-2026-11-12-14`), part 2's two lines left to the booking (the offset protection and the territories' child benefit, FAM-1.07, each at $2 billion a year, the middle of its range) and SS-8 recorded at zero and flagged (part 4). Item 6 (incidence) is not yet done.
1. `models/data/inputs/ledger-bills.csv`, line 13 (FAM-1, 1.7 / 1.9 / 2.1): to **1.65 / 1.85 / 2.05**, with the note "AFA without the $2,200 floor (DEC-2026-11-12-06); floor about $0.05T (dossiers/secure-floor/6-cost.md, part 1)". The CPI profile in `fiscal-profiles.csv` (line 13) stays.
2. New `ledger-bills.csv` rows on rail R1, general fund, one per new agenda item: INC-1 (0.145), INC-2 (0.23), INC-3 (0.043, with INC-3.03's 0.020), INC-4 (0.045), INC-5 (0.02), with FAM-1.04, 1.06 and 1.08-1.10 (0.054 together) as a FAM-1 component or an FAM-1 row of its own; year shapes in `fiscal-years.csv` from `tools/secure_floor_path.py`; rows in `models/data/budget/provisions.csv`.
3. LAB-10: the participation envelope in `recovery-adoption.json` (`participation_tn`, 0.1) stays; its line gains the name LAB-10 in `provisions.csv` so the dossier's provisions trace to it.
4. FAM-3: no change. The bands are roughly cost-neutral; the booking already uses high take-up and the 1.10% ceiling (#266).
5. Social Security: `models/tools/recovery-budget/assumptions.json`, `social_security`: replace the two-point broad rate phased 2035-44 with the decided package, SS-8's reserve investment and SS-7.01's one-point contingent fallback, once it is settled how to record the stock purchases (part 4); and correct the SS-1 ledger row's note (−$2.75T against its −$4.74T path).
6. Incidence: `models/data/inputs/incidence-rows.csv` F1 (key `ctc`) to the decided design's distribution, which pays the top quintile less than the 2029 law (part 1's 5.4 million families); new rows for INC-1 and INC-2 (keys for low-wage workers and SNAP households).
7. `ledger-dynamic.csv` DY3 (the child credit's work response) stays as a sensitivity in no total.
8. **INC-2.02, Espen's option D** (`DEC-2026-11-13-03`), booked after #304 on its pattern: a new line in `tools/secure_floor_path.py`; a row of its own, **INC-2B**, on rail R1, general fund, from FY2030 (0.092 / 0.138 / 0.183 over FY2030-39), in `ledger-bills.csv`, `fiscal-years.csv`, `fiscal-profiles.csv` and `models/data/budget/provisions.csv`, derived in `secure_floor_booking.py` (`INC_ROWS`, `RANGES`) and checked in `test_fiscal_secure_floor.py`; and an incidence row, INC2D, on its own measured key `snap_earn` (SNAP households' earnings; `models/tools/household/keys.csv`, `budget.py`). Its own row, not part of INC-2, so its range and its incidence key stay its own.
9. **INC-4 rescoped (Espen, November 13, option B)**, rebooked on the same pattern: the line in `tools/secure_floor_path.py` at $0.5 billion in tax year 2030, growing 2.5% as before; INC-4's row in `ledger-bills.csv` to 0.002 / 0.005 / 0.009 (was 0.03 / 0.045 / 0.06), its shape in `fiscal-years.csv`, its perm in `fiscal-profiles.csv` and `models/data/budget/provisions.csv`, derived in `secure_floor_booking.py` (`RANGES`) and checked in `test_fiscal_secure_floor.py`. Its incidence row, INC4, keeps the measured key `cdctc`, whose shares do not move (the rule's central case is unchanged; its text now names both programs). Booked in the same step as immigration's memo 6 health factor; together they take the plan-wide FY2040 gap from $4,256.6 billion to $4,245.4 billion short.

## 7. Sensitivities

| Input | Central | Range | Effect on FY2030-39 | Basis |
| --- | --- | --- | --- | --- |
| The child benefit's planning range | $1.85 trillion | $1.65-2.05 trillion | ±$0.2 trillion | Legacy range less the floor; the CPS static check is at the low end, the Tax Policy Center moved to the 2030s at about the low-to-middle |
| Real income growth in the floor's pricing | 1.0% a year | 0.5-1.5% | ±$0.01 trillion | More growth pushes more families above the unindexed lines |
| SNAP's restoration | $0.23 trillion | $0.20-0.25 trillion | ±$0.03 trillion | CBO's window's later years [EV-SEC-035] [EV-SEC-038] |
| SNAP's earned income deduction at 45% | $0.138 trillion ($12 billion in FY2030) | $0.09-0.18 trillion ($8-16 billion) | −$0.05 to +$0.05 trillion | FNS's FY2024 counts [EV-SEC-616]; the shelter interaction and new entrants are judgment; the CPS upper bound, about $32 billion a year, is outside the range (part 1) |
| The childless credit | $0.145 trillion | $0.13-0.16 trillion | ±$0.015 trillion | JCT and TPC [EV-SEC-609] [EV-SEC-610] |
| The dependent care credit, rescoped (option B) | $0.005 trillion ($0.5 billion in tax year 2030) | $0.002-0.009 trillion ($0.2-1.0 billion) | −$0.003 to +$0.004 trillion | The household model's $0.34 billion in 2029 (CCDF already outside the CPS's spending); adult care, under-reporting and take-up are judgment (part 1) |
| The child's own ID | $0.027 trillion | $0.02-0.03 trillion | small | 500,000 children [EV-SEC-016] |
| Paid leave take-up | high (booked) | low to high: $0.6-1.4 trillion of benefits | fund only | Legacy cases [EV-SEC-693] |
| **The general fund, all** | **$2.59 trillion** (with INC-2.02 and INC-4 rescoped) | **about $2.2-2.9 trillion** | | |

## 8. What each figure is

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| The child benefit's amounts, phase-out, ages, ID rule, payee | Commitment (decided) |
| Its cost range | Working assumption: legacy planning range less the floor, checked against the CPS and the Tax Policy Center |
| The floor's value | Working assumption: CPS static arithmetic, full take-up |
| The 2029 child-poverty rate | Working assumption, about 9% (8-12%), not on the critical path |
| The credit for other dependents | Commitment: it ends (`DEC-2026-11-12-09`); its saving a working assumption, not counted |
| The new lines' costs | Working assumptions on outside scores, laid on fiscal years |
| SNAP's earned income deduction at 45% (INC-2.02) | Commitment (decided, `DEC-2026-11-13-03`); its cost a working assumption on FNS's counts, about $12 billion in FY2030 (range $8-16 billion) |
| LAB-10's $100 billion | Commitment (the envelope); people served, about 400,000-900,000 over the decade, a working assumption (memo 4) |
| Paid leave's take-up | Working assumption; the booking uses the high case |
| Social Security's package effect | Working assumption on single-provision scores and project arithmetic for SS-8 (about +3.6 to +3.8 before the fallback); to study with SSA's whole-package score (point 12) |
| How to book SS-8 | Open question for the booking step |
| SS-11's loan | Contingent, zero to the gap at depletion |
