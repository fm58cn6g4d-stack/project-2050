# Stage G: the financing settlement

Role: the financing package for the whole plan, the one place where the plan is balanced (`DEC-2026-11-10-05`; `charter/PLAN.md` section 6, stage G; `1-audit.md` part E). It takes health's share from the top-end and corporate rows first (`DEC-2026-11-15-20`), then gives way on other spending across the whole federal budget (`DEC-2026-11-15-04`, `DEC-2026-11-20-07`), and closes FY2040 and every later year on the general fund. Status: **booked, stage G step 7, November 24, 2026.** Every fork is decided (`DEC-2026-11-20-05` to `-14`, `DEC-2026-11-24-01` to `-09`) except **memo G8, the health contribution over time, which is provisional**; the booking holds one rate from 2035 as a labelled working assumption (part 4). The booked choices are in `models/data/inputs/settlement.json`; the figures are in [`notes/booking-results.md`](notes/booking-results.md). **The clean-energy credits' cost after FY2039 is corrected to the decided step-down** (memo [G25](memos/G25-cli1-after-the-fix.md); [`notes/cli1-tail-check.md`](notes/cli1-tail-check.md)): the booking note's figures carry it (FY2040 −$16.1B, the tightest year; FY2056 −$282.8B; debt 131.5% of GDP in FY2056; the lowest base rate that would close every year is now 3.75%, and G16 B holds 3.80%), while the figures in this text's parts are as booked in step 7, before it (FY2040 −$6.0B, FY2042 −$0.4B, FY2056 −$205.4B and 133.1%). **Stage G step 11 booked the health fund as its own account, G26-G28 and I1 A** (part 8, which restates the general fund, the debt path and take-home: every year FY2040-56 closes, FY2030-39 is +$776.5B on the general fund with health's early surplus held in the fund, and debt is 129.4% of GDP in FY2056, with memo G29's HEX fix; G27.1a is decided, A, and I2's options are memo G29, pending Espen). Memo G8 is answered by G27 A, the fund's own rule.

**Naming:** "step 7" is stage G's booking step. "G1" to "G14" are the memos in [`memos/`](memos/README.md). The ledger's revenue rows with the same names are called "row G6" and so on; a bare "G6" is a memo.

Units and sources:
- Federal fiscal years, case `mixed`, nominal $B. A positive gap is a shortfall.
- **The base** is the plan before the settlement: $614.6B short in FY2040 and $3,995.5B over FY2030-39 (#467's $615.6B and $3,998.5B, less the duty to house's HOU-1 line, which G14 C removes).
- **The booking:** `models/tools/settlement_booking.py` derives each item's path with the screens' own option functions, on the plan before the settlement; `models/tools/recovery-budget/model.py` books them in every case; `models/bookings/test_settlement_booking.py` checks both.
- The step 4 and 4b screens (`packages.py`, `screen.py`, `take_home_vat.py`, `budget_scan.py`) price from the plan before the settlement (`build_case(..., settlement=False)`). Their notes ([`notes/settlement-results.md`](notes/settlement-results.md), the VAT draft, and [`notes/budget-scan-results.md`](notes/budget-scan-results.md)) are the record of how the choices were made.
- Project arithmetic on the project's exploratory models, not official scores.

## In plain terms

1. **Before the settlement the plan was about 1.1% of GDP short each year from FY2040, and the shortfall grew.** Health's share of other flagships' revenue is $532B of the $615B. It grows after 2045 because the national health budget lets health grow a point faster than the economy (D2), and long-term care grows faster still.
2. **The top end couldn't close it.** Health takes the most durable top-end and corporate rows (part 1), and the top-end stack is already at 68-73% on top wages.
3. **There is no VAT** (`DEC-2026-11-20-07`). Cuts across the whole federal budget came first, and a larger health contribution is the fallback for what they don't close.
4. **The settlement, as booked** (part 2):
   - four pricing fixes, and the wealth tax capped against the income taxes on the same return (G4);
   - the $300 adult credit ends, and the states pay their full current share of long-term care, as they do for health (G1);
   - the education fund at 1.65 points (G7);
   - the $100B delivery line removed, with memo 10's contingency kept under written guardrails (G9.3);
   - **defense held flat in real terms after FY2036 and restructured about 5%** (G10);
   - **crop insurance reformed** (G11.2), **like-kind exchanges ended** (G12.2), and **housing's stage 2 kept as a capped program, not a right** (G14);
   - **the health contribution's base rate at 3.80% from 2035** (G2 C's fold, plus the fallback). The memos had 3.85% with every recommendation. Your two "no" answers (G11.1, G12.1) forgo about $8.7B in FY2040, but the $100B line's removal ($14.0B) and the duty to house's ($1.3B), which the memos' rate didn't count, more than cover them.
5. **Every year from FY2040 to FY2056 closes.** The tightest is FY2042, at −$0.4B: the margin is thin until the mid-2040s. From then the defense path builds a surplus, about $205B by FY2056. How the rate should move as it does is memo G8, still open.
6. **Debt** is 117.8% of GDP in FY2040, against the baseline's 132.7%, and 133.1% in FY2056, against 180.2%.
7. **For households:**
   - **Health's take-home test reads the same both ways** (G2b): **69.0% of workers come out ahead**, against the 85-90% target set on health costs alone (`DEC-2026-11-15-02`). Below 200% of poverty, 99.5% do. The group just above the exemption (250-400% of poverty) is at 81.5%.
   - **On D3 every fifth below the top comes out ahead:** the fourth fifth by $5,525 a household a year over FY2030-39, and in every single year.
   - **The revenue-mix test passes:** 65% over FY2030-39, its decided window; 61% in FY2040 and 58% in FY2056.
   - **Social Security** is unchanged.
8. **The risks:** without D2 the plan is $243B short in FY2040, and the backstop (G13) raises the health contribution up to about 1.1 points. The yield risks with no backstop are about $248B together in FY2040 (part 5).

## Part 1. Health's share, from the top-end and corporate rows first

Health's first call on the plan's other revenue is **$532.1B in FY2040** (`health_booking.first_call()`). `DEC-2026-11-15-20` takes it from the top-end and corporate rows first. The allocation gives health the most durable of them: statutory rate changes on large, well-measured bases, with no open constitutional question. The rows with the most legal or behavioral risk (row G11, row G6) stay with the rest of the plan, so if one fails, the loss falls on the rest of the plan, not on health (review N-2).

| Row (FY2040, $B) | What | To health | To the rest of the plan |
| --- | --- | --- | --- |
| G1 | Corporate rate to 28% | 201.4 | — |
| G9 | The 2025 law's cuts reversed above $450K | 181.9 | — |
| G7 | Foreign income at the full rate | 50.1 | — |
| G5 | Buyback tax 4%, corporate minimum 21% | 48.8 | — |
| G3 | Top rate to 39.6% above $400K | 37.6 | — |
| C43 | A 45% bracket above $5M | 12.3 | 10.3 |
| C38, G6, G11, C18, H1b, G8, G10, C39, C3A, C35, C40, C41, less GX and the IRS allowance | | — | 563.4 |
| **Top-end, corporate, estate and enforcement rows** | | **532.1** | **573.7** |

Over FY2030-39 health's first call is about $2.12T: −$660B over FY2030-34, while its sources run ahead of its need, and +$2.78T over FY2035-39. This allocation moves no figure.

## Part 2. The settlement as booked

Each line's own effect on the general-fund gap ($B; − lowers it), on the plan before the settlement. The lines are added in `models/data/inputs/settlement.json`; "S" items have their own paths in `settlement-paths.csv`, and the switches change a parameter the model already had.

| | What | Decided | FY2040 | FY2045 | FY2056 | FY2030-39 |
| --- | --- | --- | --- | --- | --- | --- |
| | **The plan before the settlement** | | **614.6** | **675.2** | **1,157.0** | **3,995.5** |
| S01 | GX narrowed: no second haircut on H1b's folded half | Agent (part 6) | −6.5 | −8.1 | −12.5 | −27.9 |
| S02 | HCA re-derived at $70B in FY2040 | Agent; working assumption | +16.5 | +19.8 | +29.0 | +70.2 |
| S03 | The health contribution's avoidance allowance by tier: 10% on the base rate, 20% on the surcharge | Agent; working assumption, range 10-25% | −63.0 | −77.7 | −120.7 | −376.7 |
| S04 | The stack cap: the wealth tax plus the income taxes on a 6% return capped at 100% of it | G4 C1, `DEC-2026-11-20-08` | +40.0 | +49.4 | +76.6 | +328.1 |
| switch | The general fund's grant to Medicare's HI fund ended from the 2035 endpoint | Agent; accounting correction (part 6) | −85.2 | −101.6 | −147.1 | −235.3 |
| switch | The $300 adult credit ends | G1 A, `DEC-2026-11-20-05` | −105.8 | −120.9 | −162.2 | −915.8 |
| S05 | The states pay 100% of their current long-term care spending (HLT-9.09) | G1 A, `DEC-2026-11-20-05` | −148.1 | −192.5 | −312.6 | −605.3 |
| switch | The education fund at 1.65 points | G7 B, `DEC-2026-11-20-11` | +6.2 | +7.6 | +11.7 | −38.7 |
| switch | The 2 points above $20K/$40K end … | G2 C, `DEC-2026-11-20-06` | +216.3 | +433.1 | +636.8 | +496.5 |
| S06 | … and the health contribution's base rate rises from 2.25% to **3.80%** from 2035: 3.25% for the fold, the rest the fallback | G2 C; G3 E, `DEC-2026-11-20-07`; the rate over time is G8, open | −347.2 | −428.5 | −665.1 | −1,533.9 |
| switch | The $100B delivery line removed; memo 10's contingency kept, with guardrails (part 7) | G9.3 B, `DEC-2026-11-20-14` | −14.0 | −16.8 | −24.7 | −100.0 |
| S07 | Defense flat in real terms from FY2037: NSC-1A's own rule for FY2037-39, extended after FY2039 | Agent for FY2037-39 (#474); G10.1 C after, `DEC-2026-11-24-01` | −41.9 | −166.0 | −541.5 | −40.4 |
| S08 | Defense restructured, 5% below that path by FY2033 | G10.1 C; working assumption, range 3-7% | −59.5 | −65.7 | −81.8 | −434.3 |
| S09 | Crop insurance reform | G11.2, `DEC-2026-11-24-04` | −5.0 | −5.5 | −6.9 | −42.9 |
| S10 | Like-kind exchanges ended beyond the booked $500K cap | G12.2, `DEC-2026-11-24-06` | −4.9 | −5.9 | −8.6 | −40.0 |
| S11 | Housing stage 2 a capped program, not a right, shaped on its enrollment | G14 C, `DEC-2026-11-24-09` | −18.6 | −22.3 | −32.8 | −40.7 |
| ledger | The duty to house's HOU-1 line removed | G14 C | −1.0 | | | (in the base above) |
| | **The settlement, as booked** | | **−6.0** | **−26.4** | **−205.4** | **+458.5** |

The ledger line is already in the "before" row: it moves the plan's own ledger (`fiscal-components.csv`), so it is about −$1.0B against #467's figure.

**What was decided and isn't a line:**
- **G10.2** (`DEC-2026-11-24-02`): the FY2029 base capped at CBO's February 2026 path. It changes nothing against today's baseline; it is statutory text (part 7).
- **G11.1 no** (`DEC-2026-11-24-03`): the 2025 law's farm increases stay. **G12.1 C** (`-05`): the small business stock exclusion stays as it is. **G12.3 no** (`-07`).
- **G5 B and G13 A** (`DEC-2026-11-20-09`, `DEC-2026-11-24-08`): the contingent backstop, statutory text drawn only on a finding (part 7).
- **G6 C** (`DEC-2026-11-20-10`): $250B of health's early surplus held in the plan's fund as a reserve; a use of the decade's figure, not a line.
- **G9.1 (a) and G9.2 A** (`-12`, `-13`): CRT-P1 and the capacity sizes stay as booked.

**The fallback rate.** The base rate is the lowest, to 0.05 points, that closes every year from FY2040 to FY2056 with every other line booked: **3.80%**. At 3.75% FY2042 is short. A quarter point is about $56B in FY2040 (`health-household-contribution.md` section 2), grown on HCU's path, and linear; the avoidance risk at a higher rate is in part 5.

### What the farm and housing lines carry

- **Crop insurance (G11.2)** leads with populism, as you directed: the people who bear it are the crop insurance companies, through their expense reimbursement and guaranteed return, and the farms with the largest policies; a family farm keeps most of its subsidy. The 2025 law's increases to reference prices and crop insurance stay (G11.1 no), because the new majority's first-term farm-state Democrats can't be asked to vote down their farms' support. The reform is framed and sequenced in the 2029 farm bill as a check on insurers' margins and the largest operations, which is the smaller ask of farm-state votes.
- **Housing (G14 C)** is shaped on stage 2's enrollment (the reviewer's nit on #476). Under the cap, stage 2 enrolls up to 300,000 families a year from 2034, reaching about 900,000 awards by FY2036, and then fills to about 810,000 families leased by FY2040, 53% of the right's cost. The capped path runs in a straight line from the right's FY2036 level ($14.4B) to that FY2040 level ($20.9B), never above the right's own path. The flat cut had charged the capped program less in FY2037 than in FY2036, with more families enrolled. Shaped, the FY2037-39 saving is $40.7B, not $44.0B: $3.3B less, below the nit's rough $5-10B, because the right's own FY2039 cost ($40.2B) is already near its FY2040 level. FY2040 on is unchanged. The housing dossier is restated (`../../home/4-specification.md`, HOU-4D.01; `../../home/6-cost.md`).

## Part 3. What the settlement does

### The general fund, year by year

| | FY2030 | FY2033 | FY2035 | FY2036 | FY2037 | FY2038 | FY2039 | **FY2040** | FY2041 | FY2042 | FY2045 | FY2050 | FY2056 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Before the settlement | −160 | 132 | 554 | 840 | 850 | 855 | 812 | **615** | 625 | 639 | 675 | 824 | 1,157 |
| **Booked** | −221 | −42 | 47 | 277 | 272 | 259 | 193 | **−6** | −5 | −0.4 | −26 | −143 | −205 |

- **The rule's test (FY2040 and every later year) passes** in every year to FY2056. The margin is thin in FY2040-44, $0.4-6B a year. From the mid-2040s the general fund runs ahead.
- **The base rate each year would need on its own:** 3.77% in FY2040, 3.80% in FY2042, 3.70% in FY2045, 3.38% in FY2050, 3.32% in FY2056. That falling need is memo G8's question.
- **The decade (FY2030-39):** +$458.5B short, with health's early surplus counted. G6 C holds $250B of that surplus as a reserve, so the rest of the plan's own decade figure is about +$709B. FY2036-39 run about $190-280B short a year. The rule doesn't test those years, and the debt guardrail passes with room. Read "every year from FY2040 closes" as just that, not as the decade closing.

### Debt (the guardrail, on the unified budget; the budget model is the reading of record)

| % of GDP | FY2039 | FY2040 | FY2045 | FY2050 | FY2056 |
| --- | --- | --- | --- | --- | --- |
| Baseline | 130.3 | 132.7 | | | 180.2 |
| Before the settlement | | 126.8 | | | 162.5 |
| **Booked** | **116.9** | **117.8** | **122.1** | **126.6** | **133.1** |

### With and without D2 and the wealth tax (HS2)

| General-fund gap, $B | FY2040 | FY2045 | FY2056 | Base-rate points that close FY2040 / FY2056 |
| --- | --- | --- | --- | --- |
| The settlement | −6.0 | −26.4 | −205.4 | — |
| Without D2 | 243.4 | 297.7 | 320.9 | +1.09 / +0.75 |
| Without HS2 (net of the stack cap) | 104.0 | 109.3 | 5.2 | +0.46 / +0.01 |
| Without both | 353.3 | 433.3 | 531.5 | +1.58 / +1.24 |

The later years need fewer points because the defense path's surplus absorbs part of either loss. **A correction to step 4b:** memo G13 and `3-budget-scan.md` priced the wealth tax's loss at $139.1B in FY2040 (+0.62 points), counting the whole of HS2 while the stack cap's +$40B, which only trims HS2, stayed in the package. Losing the tax loses HS2 net of its cap: $104.0B, +0.46 points. The backstop's design doesn't change.

### Households: the take-home test, both ways

`DEC-2026-11-20-06` (G2b) reports health's take-home test two ways and judges the plan with everything counted. FY2040, `take_home_vat.py`'s method at each base rate, no VAT (`budget_scan.take_home`):

| Base rate R | Workers ahead, health costs only | **Workers ahead, everything counted** | Below 200% of poverty | 250-400% of poverty | Retirees and others |
| --- | --- | --- | --- | --- | --- |
| 3.25% (G2 C's fold alone) | 76.2% | 76.2% | 100.0% | 89.9% | 98.0% |
| **3.80% (booked)** | **69.0%** | **69.0%** | **99.5%** | **81.5%** | **97.5%** |
| 4.45% (G3 E with no cuts) | 60.8% | 60.8% | 98.2% | 69.0% | 96.9% |

- **The two readings are equal.** None of the booked cuts charges a worker directly: defense is not a household charge; crop insurance falls on insurers and the largest farms; like-kind exchanges on real-estate investors, almost none of them in the test's working population; G14 lowers a benefit, which the test doesn't count as a charge. What everything counted adds over health costs is the contribution above 3.25%, which the test already counts.
- **Against the decided target** of 85-90% of workers ahead on health costs (`DEC-2026-11-15-02`), 69.0% is short. It is 11 points above the VAT package you turned down, on the reading you chose (57.8% with the VAT counted).
- **The group just above the exemption** (250-400% of poverty) bears most of it, at 81.5%.

### Households: D3 by quintile

$ a household a year, FY2030-39 average, measured keys, scenario Q-G (Q-H7 with the settlement's rows; every payroll row gross, as households pay it):

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| Q-H7, before the settlement (EDUP net of its offset, as committed) | +14,830 | +13,208 | +12,070 | +6,837 | −62,271 | −910,568 |
| **Q-G, the settlement as booked** | **+14,782** | **+12,855** | **+11,281** | **+5,525** | −65,283 | −936,107 |

**By year** (nominal $ a household; D3's phase-in profiles):

| | FY2033 | FY2035 | FY2037 | FY2039 |
| --- | --- | --- | --- | --- |
| Q1 | +11,758 | +16,909 | +20,549 | +22,579 |
| Q2 | +8,702 | +15,933 | +19,991 | +22,195 |
| Q3 | +6,699 | +14,603 | +18,677 | +20,900 |
| **Q4** | **+2,038** | **+7,895** | **+11,038** | **+12,575** |
| Q5 | −60,301 | −70,101 | −73,777 | −79,362 |

- Every fifth below the top comes out ahead on the average and in every year shown; the fourth fifth is thinnest in FY2033, before the endpoint.
- **What D3 doesn't see:** it has no rows for defense, crop insurance, like-kind exchanges, the states' long-term care payment or the $300 credit, so those move only the gap. The credit's end is a loss of up to $600 a year for a two-adult household. **D3 also has no row for housing's stage 2** (`housing_extra`), as booked or capped: its HOU row is HOU-1. So G14 C's loss to the families who wait doesn't show in Q1; the duty to house's HOU-1 line moves Q1 by about −$10.
- The household count is the FY2034-35 one, so FY2040's would lower these by a few percent (N-6).

### The revenue-mix test

D3's revenue-mix test requires that the top 1% (by incidence) and corporations (statutory) bear more than half of new general-fund revenue, with health's contributions left out (`DEC-2026-11-15-29`), read on its decided ten-year window with the mature-year share reported every year (G3b, `DEC-2026-11-20-07`).

| Package | FY2030-39 (the test's window) | FY2040 | FY2056 |
| --- | --- | --- | --- |
| Before the settlement (Q-H7) | 64% | 57% | 52% |
| **The settlement (Q-G)** | **65%** | **61%** | **58%** |

The settlement's share is higher than before because the 2 points on broad incomes end and the rest is the health contribution, which the test leaves out as a premium replacement. Beyond 3.25% the contribution pays for more than premiums, so part of the higher share is a matter of labels (memo G3 said so).

### Social Security, HI and the education fund

- **Social Security:** unchanged. On the budget model's CBO convention it depletes in 2093, with a 75-year balance of −0.31% of payroll. On the funds model's D8 reading (board), the D8 baseline closes 63% of the 75-year gap and D8 with SS-5 closes 82%; nothing in the settlement touches either.
- **HI:** HI folds into the plan's fund at the January 2035 endpoint (HLT-7.22), and Medicare's hospital claims are kept whole to then. With the grant ended, the model's HI fund after 2035 shows depletion in 2037, a current-law comparison only, not a plan result (review F-1, item 3).
- **The education fund:** solvent at 1.65 points, with a reserve of $46B in FY2040, about five weeks of outlays. One weak year of pay growth would put it back in the red (`DEC-2026-11-20-11`), so its position is reported each year.

## Part 4. The one open fork: G8, the health contribution over time

Memo [G8](memos/G8-later-years.md) is redrafted without a VAT and is **provisional**. It asks how the base rate should move as the defense path's surplus arrives: steps down on fixed dates (A), a lower start that steps up in 2040 (B), one fixed rate with the surplus paying down debt (C), or a fixed rate that steps down a quarter point only once the trustees certify two years of surplus above 0.1% of GDP, never below 3.25% (D, recommended).

**What the booking assumes:** one rate, 3.80% from 2035, with no step (`settlement.json`, "WORKING ASSUMPTION for the later years"). That is option C's path, and option D's before any finding. No G8 choice is booked. A, B or D would change the booked path from FY2046, FY2035 or FY2049, and nothing in FY2040-45.

## Part 5. Risks

Each risk alone, added to the booked package (`settlement_booking.py --report`). "Points" is the base-rate increase that would cover FY2040.

| Risk | Basis | FY2040 | FY2045 | FY2056 | Points |
| --- | --- | --- | --- | --- | --- |
| Without D2 | Never achieved [EV-CAR-742]; the backstop covers it (G13) | +243.4 | +297.7 | +320.9 | +1.09 |
| Without HS2 | Legal risk high; *Moore* (2024) left it open; the backstop covers it | +104.0 | +109.3 | +5.2 | +0.46 |
| Without both | | +353.3 | +433.3 | +531.5 | +1.58 |
| **Joint yield risk:** the wage stack at the working elasticity and pre-2025-law scores 10% low | Review F-2; **no backstop covers these** | +248.2 | +285.3 | +271.0 | +1.11 |
| The wage stack yields at the working elasticity (0.25) | Stack note part 3: up to about $140B (rough, unverified) | +134.0 | +145.9 | +59.6 | +0.60 |
| Pre-2025-law scores come in 10% low | About $4.9T of the decade's revenue rests on them (`1-audit.md` item 22) | +108.2 | +113.1 | +6.1 | +0.48 |
| If a scorer counted the fold-in's HI shortfall as new | Part 6, item 4: the correction stands; this is the grant's size | +79.2 | +75.2 | −58.3 | +0.35 |
| The avoidance allowance at 20% on the base rate | Within item 9's 10-25% range | +57.0 | +51.4 | −84.7 | +0.25 |
| C3A's compliance payments vanish | Suppliers comply (item 43) | +35.6 | +23.5 | −132.0 | +0.16 |
| The stack cap at its high end ($55B) | Stack note part 4 | +9.0 | −7.9 | −176.6 | +0.04 |

- **The working assumptions that would move the rate first** (the reviewer's note on #480). Each is booked at its central value, and none is covered by the backstop (G13 covers only D2 and the wealth tax):
  - **S03, the avoidance allowance on the base rate** (10%, range 10-25%): at 25%, about +$85B in FY2040, so the base rate would need about **+0.38 points** (4.2%). It is the largest because the base rate's yield is the largest line.
  - **S08, defense's restructuring** (5%, range 3-7%): at 3%, about +$24B in FY2040, **+0.11 points**.
  - **S02, the 0.9% folded in** ($70B, against the $53.5B first booked): at $53.5B, +$16.5B, **+0.07 points**.
  - **If one misses,** the rule fails in FY2040-44 at once: the margin there is $0.4-6B. Nothing switches on by itself. A later Congress would have to raise the base rate by the points above, or find the money elsewhere, until the defense path's surplus covers the miss in the late 2040s. Memo G8's options C and D keep that surplus in hand; A gives it back.
- **The package has almost no margin in FY2040-44.** Every risk row breaks the rule there on its own. From the late 2040s the surplus absorbs most single risks; the joint yield risk breaks it in every year.
- **The yield risks fall on a later Congress.** Without a VAT the VAT's own yield risk and the price-rise reading are gone. Memo G8's options C and D keep the later surplus in hand against them; A gives it back.
- **Defense's 5% restructuring** is a working assumption (range 3-7%), with no CBO score of the package. At 3% the FY2040 saving is about $24B smaller (memo G10).
- **Capacity and delivery risk.** The $100B delivery line is gone (G9.3), so a delivery cost outside the capacity rows (payment systems, state partners, programs with no capacity row) needs new money when it appears. Memo 10's contingency (about $78.5B inside CAP-7S and CAP-7) stays, for agency staffing and systems only (part 7).

## Part 6. Agent decisions, corrections and items carried

**Decided here (agent):**
1. **GX narrowed** (S01; `1-audit.md` part D, item 3): HCU's own 20% allowance already covers H1b's folded half, so a second 15% haircut counts the same avoidance twice.
2. **HCA at $70B** (S02; item 15), a working assumption. Re-deriving it from the CPS's top wages is carried to the next re-run; the screens' $70B is booked.
3. **The avoidance allowance by tier** (S03; item 9), 10% on the base rate, range 10-25%: income withheld at source is rarely misreported, but the base rate also falls on self-employment, partnership and rental income.
4. **The HI grant ended** (switch): an accounting correction, confirmed by the milestone review (F-1). HLT-7.22 lists no general-revenue stream for Part A; HI is kept whole until the endpoint and then folds in; `DEC-2026-11-15-29` puts any shortfall of the plan's fund on the general fund, so a grant after 2035 is the general fund paying itself. The amount was never adopted ("a final HI grant amount" is under `not_selected` in `models/data/inputs/recovery-adoption.json`). **The obligation it moves:** at the fold-in the plan's fund takes on Part A's current-law shortfall, about 0.56% of HI payroll over 75 years on the funds model; the risk row sizes it.
5. **NSC-1A's FY2037-39 years at flat real** (S07's first three years; #474): its own rule, "the FY2029 base grown with the defense deflator through FY2039" [EV-FIN-013], where the model's baseline grows defense with GDP from FY2037. −$4.1B, −$12.0B and −$24.3B; −$40.4B over the decade.
6. **G14 C shaped on enrollment** (S11; part 2), and **the duty to house's HOU-1 line removed** with it: G14 C drops the duty to house, and HOU-1 carried it as its own component (0.003; `fiscal-components.csv`), separately from `housing_extra`.
7. **D3 on one payroll convention** (the reviewer's note on #467): every payroll row gross; EDUP is booked gross in Q-G (`EDUPg`).
8. **The wealth tax's loss net of its cap** (part 3): a correction to step 4b's backstop table.
9. **The budget model as the reading of record** for the debt guardrail (item 26). The long-term model (`fiscal-model.py`) doesn't carry the settlement's lines; its DEC scenario is a disclosed comparison, as before.
10. **How it is booked:** one adopted file (`settlement.json`) and its derived paths, as health's and care's bookings are, so each line keeps its DEC- row and the ledger's flagship rows keep their own amounts. D3 books the settlement as scenario Q-G beside Q-H7.

**Carried, small, not done here:** the payroll point by base (item 16); DEM-17.02 against IMLS's baseline (item 34, up to −$0.25B in FY2040); CAP-7P against the SSA reclassification (item 36, about +$1.0-1.2B over FY2030-33, none in FY2040); two redundancy leads from step 4b (the dependent care credit under FAM-2's guarantee; homelessness grants under HOU-4D) for the full model of every account; the tariff baseline risk.

**Leave open, as the audit proposed:** items 6, 14, 19, 23, 27, 29, 30, 37, 38, 41 and 42. Item 29 (R1's child benefit after its window) is financed in the out-years by this package; the Byrd-rule vehicle stays a 2029 drafting item.

**For the later innovation topic, not reopened here:** G12.1 keeps the small business stock exclusion as the 2025 law left it, "unless the 2025 widening is really not going to hurt start-up innovation/decrease entrepreneurship" (Espen, `DEC-2026-11-24-05`). The innovation, entrepreneurship and small business topic should look for evidence on whether the widening (the higher per-company cap, the larger asset test, the three- and four-year partial exclusions) raises start-up formation or investment. If it doesn't, the topic may bring G12.1 B back (about −$2.2B in FY2040).

## Part 7. The settlement's specification: what the law says

These are the settlement's provisions as text for drafting, with their legal footing. Each is decided; the drafting is the agent's.

### 7.1 The contingent backstop (G5 B, redrawn as G13 A)

`DEC-2026-11-20-09` and `DEC-2026-11-24-08`.
1. **The finding for D2.** Each year the plan's fund trustees publish the single plan's spending against D2's path (GDP plus 1 point from 2037; `DEC-2026-11-15-08`).
2. **If D2 misses.** If spending runs more than 0.25% of GDP above the path for two years running, the health contribution's base rate rises by 0.25 points the next January, and by 0.25 points each later January while the overrun lasts, up to the rate that closes the overrun on the trustees' projection: about 1.1 points in FY2040 terms. When spending returns to the path for two years, the steps come off in the same order.
3. **If the wealth tax is struck down.** On a final ruling against HS2, three steps apply in order:
   - first, its drafted fallback, the deferral charge on unrealized gains;
   - then, the top surcharge tier of the health contribution, up to the room the stack cap leaves;
   - last, the base rate, by 0.25 points a January, up to what closes the loss (about 0.46 points in FY2040 terms, net of the cap).
   The deferral charge mostly reaches the same base as row G11, and the surcharge has little room, so most of a loss would land on the base rate.
4. **If both trigger,** the base rate reaches about 5.4% in FY2040 terms (3.80% plus 1.58 points), and about half of workers (51.6%) would come out ahead on the take-home test; with D2 alone, about 4.9% and 56.4%.
5. **Bridging.** The G6 reserve ($250B in the plan's fund) covers a shortfall while the steps phase in. It isn't spent twice: the general fund covers health's FY2035-39 call in the package (review F-8).
6. **Replacement.** Congress may replace any step with another measure of the same size by law.
7. **Legal footing.** Congress sets the rates, the steps, the triggers and the ceiling, and the trustees find a fact: contingent legislation of the kind upheld in *Field v. Clark* (1892) and *J.W. Hampton v. United States* (1928). If a finding is challenged, the step takes effect by default on its date.
8. **Burden:** none unless triggered. It is the same annual comparison the trustees publish for D2 itself (design lens: published counts with a review trigger).

### 7.2 Memo 10's delivery contingency, with guardrails (G9.3 B)

`DEC-2026-11-20-14`. The $100B `delivery_contingency` line is removed. Memo 10's contingency stays: the room inside CAP-7S and CAP-7 after democratic renewal's bottom-up allocation, about $78.5B on the booking's ramp (`DEC-2026-11-20-13` keeps the capacity sizes). It may be released only under these guardrails:
1. **What it may pay for:** agency staffing and systems for the programs the capacity rows name (`models/tools/budget/note-cap7-sizes.md`; democratic renewal part G). Not benefits, not grants to states, not a program the rows don't name, and not a cost overrun on a priced provision, which goes to Congress as a new cost.
2. **A written case for each release,** published before the money is obligated: the agency, the program, what the money buys, why the program's own allocation doesn't cover it, and how much.
3. **Public reporting of every draw:** each release and what it bought, in the agency's annual capacity report, with the contingency's remaining balance.
4. **Who releases:** the agency head, on OMB's apportionment, with notice to the appropriations committees 15 days before obligation (the reprogramming notice the committees already use).
5. **What's left over** at the end of the capacity rows' availability lapses; it isn't carried into another purpose.
These add one published page per release and one table a year to reports that already exist (design lens).

### 7.3 Defense (G10)

`DEC-2026-11-24-01`, `-02`.
- **The path:** statutory caps on defense discretionary budget authority, as in the Budget Control Act (2011) and the Fiscal Responsibility Act (2023): from FY2030, NSC-1A's base grown with the GDP price index, less the restructuring (about 1.7% of the path in FY2031, 3.3% in FY2032, 5% from FY2033). After FY2039 the caps continue on the same rule. Emergency money only for a declared emergency, outside the caps and named as such.
- **The restructuring** is made through the annual budget and the NDAA: all three nuclear legs kept, with Minuteman III extended for part of the force and the new nuclear cruise missile deferred; missile defense held to research; fewer of the worst cost-overrun programs; fewer service contracts and headquarters staff; TRICARE fees for working-age military retirees until the single plan covers everyone in 2035.
- **The base (G10.2):** NSC-1A's FY2029 base is capped at CBO's February 2026 path. Any 2027-28 level above it is phased out over FY2030-32, and new defense money is paid for inside defense. Against today's baseline this changes nothing; it stops a buildup from being locked in.

### 7.4 The health contribution's rate

`DEC-2026-11-20-06`, `-07`. From the January 2035 endpoint the base rate is 3.80% of AGI, with the exemption as decided (nothing at or below 138% of poverty, phasing up to the full rate at 250%); the pre-2035 steps and the surcharge are unchanged. The rule over time is memo G8 (open): until Espen decides it, the text carries one rate.

### 7.5 Housing stage 2 (G14 C)

`DEC-2026-11-24-09`. HOU-4D.01's enrollment stays capped (the yearly appropriation, with published counts), with need-based intake for families with no home of their own; no duty to house; the full right named as a 2040s target, with a review in 2041 on the program's own data. The housing dossier's section 4 carries the provision.

### 7.6 Farm (G11.2) and like-kind exchanges (G12.2)

- **Crop insurance:** premium subsidies cut toward 40% for the costliest policies; the insurers' expense reimbursement and guaranteed return capped, through the Risk Management Agency's Standard Reinsurance Agreement. Framed as a check on insurers' margins and the largest operations (part 2).
- **Like-kind exchanges** end beyond the booked $500K-a-year cap (REV-TS9). Both need a score against the post-2025-law baseline (JCT for the tax item) before drafting.

## Part 8. The health fund booked, and I1 (stage G step 11)

`DEC-2026-11-25-30` to `-32` (G26 A, G27 A with its three points, G28 A), under `DEC-2026-11-25-12` (the health contribution is a trust-fund levy) and `-28` (each important effect booked in its appropriate place); I1 A (`-27`). Figures: [`notes/booking-results.md`](notes/booking-results.md) and [`notes/health-trust-fund-results.md`](notes/health-trust-fund-results.md), both regenerated on the booking. They supersede parts 2-3's general-fund rows and debt path, which are step 7's.

**What is booked:**
- **The health fund is its own account** in the budget model (`settlement.json`'s `health_fund`; `recovery-budget/model.py`'s `health_fund()`).
  - Its sources: the contribution, the fold-in rows, the employer contribution, the health streams, the states' long-term care payment, and HX less its Social Security part. **The wealth tax (HS2, net of the stack cap) is paid to the fund by statute.**
  - Its spending: HLT-1, -2, -4 and -6 to -11.
  - The general fund shows only its transfer to the fund. HI keeps its $425B in its own account until the 2035 fold-in.
- **The 3.80% is re-founded** as the contribution's share of the fund's cost: 29.1% of its new spending in FY2040 (G26 A).
- **From FY2040 the contribution pays that fixed share, and the general fund pays the rest by law** (G27 A points 1 and 3). The rate steps a quarter point at most once a year when the reserve leaves the 15-25% band. It never goes below 3.25%, and it has no yearly reset. G13's backstop is the upward side. G16 B's second leg and G18 D′ are replaced.
- **G28 A:** the contribution reaches the debt plan only as a smaller general-fund share of health's cost, set by law under the ceiling the trustees certify each year (6.20% in FY2040, 7.35% in FY2056). G20 B's return order drops its health-contribution step (`5-budget-process.md`).
- **I1 A:** IMM-1's status line is on CBO's on-budget figure for H.R. 6, +$10.2B over FY2030-39 and +$2.1B in FY2040 on the general fund. Social Security's gain, about $22.2B over FY2030-39, is booked in Social Security's funds as IMM-1-SS (`dossiers/immigration/6-cost.md` part 6).

**G27.1a, decided (A, `DEC-2026-11-26-01`):** the band is on the contribution's own share of the fund's cost, tested one year ahead. That is the reading booked since step 11; no figure moves.

**I2, HX's Social Security part: one working assumption, pending Espen's answer on memo G29.** Espen chose C (`DEC-2026-11-26-02`): source the share first, then set out the options. [Memo G29](memos/G29-hx-social-security-part.md) does both.
- HX, the tax on former premiums, includes the payroll tax that current law credits to Social Security, and that can't be health money (`-12`, `-28`). The booking leaves that part out of the fund's sources. It stays on the general fund, as booked before.
- **Sourced, the part is about 28% of the net money, HX less HEX** (range 22-30%; EV-FIN-094, EV-FIN-095). That is about $100B a year in FY2040 (range $79-107B) and $78B over FY2030-34. The step-11 estimate was 29.7% of HX alone, about $290B a year, because it left out HEX.
- **The booking keeps 70.3% of HX and HEX in the fund** (`settlement.json`'s `source_shares`) until Espen answers G29. 70.3% and 72% move the fund's sources by under $10B a year in FY2040.
- **The HEX fix (G29, finding 3; this change).** HEX, the part of HX that the employer contribution takes back, carries the same Social Security part as HX. Step 11 (#507) weighted HX at 70.3% but kept HEX in full, so the fund was charged for a take-back of Social Security money it never got. Both now take 70.3%.
- **The reserve.** On the fixed figures the fund builds **$307.9B** over FY2030-34, net of HI's $425B and of its own FY2033-34 shortfalls. It is booked as built, as the standing reserve, with no FY2035 draw.
  - `-31` point 2's split would need $391B: $250B standing plus $141B to lower the FY2035 transfer. G29 sets out the options (R1 keep $307.9B; R2 $250B standing and $57.9B drawn; R3 point 2 in full, $83B short).
  - The general fund's FY2035 transfer is $371.7B (it was $497.8B in #507).

**The rate as booked:** 3.80% through FY2043, 4.05% in FY2044-45, 4.30% in FY2046-47, 4.05% in FY2048-51, 4.30% in FY2052-55, and 4.05% in FY2056.
- **It holds 3.80% to FY2043** because the reserve starts at $307.9B, 26% of the contribution's share of cost in FY2040, at the top of the band. It then drains to 16% by FY2043, and the rate steps up in FY2044. In #507, with $159.5B, it stepped up in FY2041.
- **Why it moves back and forth between 4.05% and 4.30%:**
  - At a fixed rate the contribution's yield falls behind its fixed share, because health and long-term care grow faster than its base. So the reserve drains toward 15%.
  - A quarter point, about $70-110B a year, then refills it toward 25% within a few years. The band is only about two steps wide ($230-380B in FY2045).
  - So the rate steps up in FY2046, down in FY2048 and up again in FY2052, and down in FY2056.
- **The general fund's gap from FY2040 doesn't move** with the fix: it pays the share the law fixes, so the rate moves only the fund's reserve.

| The band read on | Highest R | R in FY2056 | Reserve in FY2056 |
| --- | --- | --- | --- |
| **The contribution's share of the fund's cost (booked, decided)** | **4.30%** | **4.05%** | **$505B** |
| The fund's new spending | 4.80% | 4.30% | $1,941B |
| The fund's whole spending, the baseline's included | 5.30% | 4.30% | $3,894B |

### The general fund, restated

| $B | FY2030 | FY2033 | FY2035 | FY2036 | FY2039 | **FY2040** | FY2042 | FY2045 | FY2050 | FY2056 | FY2030-39 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Before the settlement | −160 | 133 | 555 | 841 | 814 | **607** | 601 | 606 | 746 | 1,083 | 4,006 |
| Step 7, with #493 (before this step) | −221 | −42 | 47 | 277 | 193 | **−16** | −41 | −98 | −224 | −283 | 459 |
| Step 11 as merged (#507) | −104 | −71 | 48 | 278 | 194 | −14 | −68 | −163 | −322 | −438 | 628 |
| **Booked now** (with the HEX fix) | **−104** | **−29** | **48** | **278** | **194** | **−14** | **−68** | **−163** | **−322** | **−438** | **777** |

- **Every year FY2040-56 still closes.** The tightest is FY2040, at −$14.1B.
- **The decade is $318B worse on the general fund** than step 7. $307.9B of health's early surplus now stays in the fund, and IMM-1 adds $10B. Against #507, the HEX fix moves $148B of the take-back's Social Security part, in FY2031-34, from the fund to the general fund. FY2036-39 run about $194-278B short a year, as before.
- **From the mid-2040s the general fund is further ahead,** because the health law fixes its share of the fund's cost (G27 A point 3). The contribution's share holds as health outgrows its base, and the fund's rule steps the rate to keep it there.

### Debt and take-home

| Debt, % of GDP | FY2039 | FY2040 | FY2045 | FY2050 | FY2056 |
| --- | --- | --- | --- | --- | --- |
| Step 7, with #493 | 116.9 | 117.8 | 121.7 | 125.6 | 131.5 |
| Step 11 as merged (#507) | 117.0 | 117.8 | 121.2 | 124.3 | 129.1 |
| **Booked now** (with the HEX fix) | **117.0** | **117.8** | **121.5** | **124.7** | **129.4** |

- **Take-home** (FY2040 incomes, no VAT): 69.0% of workers ahead at 3.80% in FY2040, unchanged. At the rule's later rates, as an indication only, it is 65.4% at 4.05% and 62.6% at 4.30%. Below 200% of poverty it is 98.4-99.5%.
- **D3** (FY2030-39) and the revenue-mix test (65%) don't move.
- **Social Security:** IMM-1-SS adds about $22B to the funds over FY2030-39. The budget model's CBO-convention reading is unchanged at 2093 depletion. Memo G29's option A would add about $100B a year from FY2040 (range $79-107B), if Espen books it there.

## Method and sources

- **Gap and debt:** `models/tools/recovery-budget/model.py` `build_case`, case `mixed`, with the settlement booked from `models/data/inputs/settlement.json` and `settlement-paths.csv` ("Settlement Snn: ..." audit lines; revenue items as revenue, the rest as outlays). `settlement=False` and the case `mixed_before_settlement` give the plan before it.
- **The items' paths:** `models/tools/settlement_booking.py`, with the option functions of `financing-protection/packages.py` and `budget_scan.py` on the plan before the settlement; `--solve` finds the base rate; `--report` writes [`notes/booking-results.md`](notes/booking-results.md). `test_settlement_booking.py` checks the committed paths and D3 rows against the derivation, the booked case against the screens' pricing of the same package, and the rate.
- **D3:** `models/tools/household/d3.py` on the measured keys, scenario Q-G (`scenarios.json`; rows `HCUg`, `HCUwg`, `HCAg`, `HS2g`, `EDUPg`, `GXg` in `incidence-rows.csv`). The revenue-mix test is `gf_test`; its single-year readings are `packages.single_year_levels`.
- **The take-home test:** `models/tools/health_cost_review.py` through `take_home_vat.py` at each base rate with no VAT (`budget_scan.take_home`).
- **Sources for the options:** memos G1-G14; the stack note's cap menu (`../notes/stack-2026-11-16.md` part 4); `health-household-contribution.md` sections 2 and 8; `3-budget-scan.md` and its evidence (EV-FIN-001 on); care memo 17 (option 7); the housing dossier's section 6.
- **Health's first call:** `models/tools/health_booking.py` `first_call()`.
