# Stage G, step 4: the settlement draft

Role: the recommended financing package for the whole plan, the one place where the plan is balanced (`DEC-2026-11-10-05`; `charter/PLAN.md` section 6, stage G; `1-audit.md` part E, step G4). It takes health's share from the top-end and corporate rows first (`DEC-2026-11-15-20`), then gives way on other spending or refinances it (`DEC-2026-11-15-04`), and closes FY2040 and every later year on the general fund. Status: **draft, November 20, 2026, revised for the milestone review ([`review-milestone.md`](review-milestone.md), #470); every fork provisional, drafted on the recommendations** (Espen's stage G method). Nothing here is decided or booked: no file under `models/data/inputs/` changes, and stage G's step 7 books what Espen decides. The forks are memos G1-G9 in [`memos/`](memos/README.md).

**Naming:** "step 5" and "step 7" are stage G's steps (the milestone review; the booking). "G1" to "G9" are the memos.

Units and sources:
- Federal fiscal years, case `mixed`, nominal $B. A positive gap is a shortfall.
- **The base is #467's corrected model:** $615.6B short in FY2040 and $3,998.5B over FY2030-39, with H1a counted once and D3 on the booked package.
- **The screens:**
  - `models/tools/financing-protection/packages.py` prices every package on the budget model's own `build_case` and on D3 (Q-H7 with each option's edits).
  - `screen.py` is the risk table.
  - `take_home_vat.py` is the take-home test with the VAT counted.
  - Full output is in [`notes/settlement-results.md`](notes/settlement-results.md), and the state table is in [`notes/states-2026-11-20.md`](notes/states-2026-11-20.md).
- Project arithmetic on the project's exploratory models, not official scores.

## In plain terms

1. **The plan is about 1.1% of GDP short each year from FY2040, and the shortfall grows.** Health's share of other flagships' revenue is $532B of the $616B. The gap grows after 2045 because the national health budget lets health grow a point faster than the economy (D2), and long-term care grows faster still.
2. **The top end can't close it.** Health's $532B takes the most durable top-end and corporate rows (part 1). The top-end stack is already at 68-73% on top wages, and over 100% on the wealthiest holders' capital income before the cap (memo G4).
3. **The recommended package** (part 2) does six things:
   - fixes four pricing items;
   - caps the wealth tax against the income taxes on the same return (G4);
   - ends a $300 adult credit that was carried in the gap without a decision, and has the states pay their full current share of long-term care, as they already do for health (G1);
   - makes the education fund solvent at 1.7 points (G7);
   - **folds the 2 points on income above $20,000/$40,000 into the health contribution**, which moves from 2.25% to 3.25% from 2035 with its exemption below 250% of poverty (G2);
   - **closes the rest with a broad value-added tax** from the January 2035 endpoint: 2.95%, stepping to 3.6%, 3.85% and 4.6% by FY2051 as health's costs grow (G3, G8).
4. **Why fold, not drop.** The first draft dropped the 2 points and used a larger VAT, so that 88.7% of workers came out ahead on health's take-home test. But the take-home test counts health costs only. **With the VAT counted, folding protects the poorest far better:** 90.4% of workers below 200% of poverty are ahead, against 79.7%, and retirees on private pensions and savings do better too. On all workers the two are close (57.8% against 55.6%), within what the rough VAT allocation could move. Folding also halves the VAT. The costs: the health-only test falls to 76.2% of workers ahead, below Espen's 85-90% target, and folding reopens the decided 2.25% rate (`DEC-2026-11-15-11`) (memo G2).
5. **With the package, every year from FY2040 to FY2056 closes** (−$3.0B in FY2040).
   - Debt is 117.9% of GDP in FY2040, against the baseline's 132.7%, and 134.4% in FY2056, against 180.2%.
   - Every fifth of households below the top comes out ahead on D3, on the decade average and in every single year from FY2033 to FY2039. The fourth fifth is +$4,553 on the average, +$2,001 in its thinnest year (FY2033) and +$10,551 by FY2039.
   - D3's revenue-mix test passes: 61% of new general-fund revenue over FY2030-39, 54% in FY2040 and 50% in FY2056.
   - Social Security is unchanged.
6. **The risks are large.**
   - Without D2 and the wealth tax, the package is $396B short in FY2040, about 4.4 VAT points. Memo G5 recommends a contingent backstop in law.
   - Three yield risks together (the top end's response, old scores, the VAT's yield) are about $313B, about 3.5 points, with no backstop.
   - If the Federal Reserve lets prices rise with the VAT, indexed benefits add about $120B a year (part 5).
7. **The real choices are G2 and G3.** Every broad source falls on households:
   - a VAT on what they buy;
   - the health contribution on what they earn;
   - or cuts on the scale of whole programs (G1 D).
   No option keeps 85% of workers ahead once everything they pay is counted.

## Part 1. Health's share, from the top-end and corporate rows first

Health's first call on the plan's other revenue is **$532.1B in FY2040** (`health_booking.first_call()`). `DEC-2026-11-15-20` takes it from the top-end and corporate rows first.

The allocation below gives health the most durable of those rows: statutory rate changes on large, well-measured bases, with no open constitutional question. The rows with the most legal or behavioral risk (G11, G6) stay with the rest of the plan. **So if G6 or G11 fails, the loss falls on the rest of the plan, not on health** (review N-2).

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

- Over FY2030-39 health's first call is about $2.12T: −$660B over FY2030-34, while its sources run ahead of its need, and +$2.78T over FY2035-39. The same rows cover it, as they total $8.66T over the decade.
- This allocation moves no figure. The plan as a whole is still $615.6B short in FY2040, which the rest of this file closes.

## Part 2. The recommended package, step by step

Each step's effect on the general-fund gap, in the order applied ($B; − lowers the gap).

| Step | What | Who decides | FY2040 | FY2045 | FY2056 | FY2030-39 |
| --- | --- | --- | --- | --- | --- | --- |
| | **The plan as booked** (#467) | | **615.6** | **676.4** | **1,158.5** | **3,998.5** |
| 1 | GX narrowed: its 15% haircut no longer applies to H1b's wage half, which HCH takes back from 2035 (`1-audit.md` part D, item 3) | Agent; the judgment call left to this step | −6.5 | −8.1 | −12.5 | −27.9 |
| 2 | HCA, the 0.9% tax folded in, re-derived at $70B in FY2040, not $53.5B (item 15) | Agent; working assumption | +16.6 | +19.8 | +29.0 | +70.2 |
| 3 | The health contribution's avoidance allowance set by tier: 10% on the base rate, 20% on the surcharge (item 9) | Agent; working assumption, range 10-25% | −63.0 | −77.7 | −120.7 | −376.7 |
| 4 | The stack cap, C1 (memo G4) | **Espen, G4** | +40.0 | +49.3 | +76.6 | +328.2 |
| 5 | The general fund's grant to Medicare's HI fund ended from the 2035 endpoint (part 6) | Agent; accounting correction, confirmed by the review | −85.2 | −101.6 | −147.0 | −235.3 |
| 6 | The $300 adult credit ended (memo G1) | **Espen, G1** | −105.8 | −120.9 | −162.3 | −915.9 |
| 7 | The states' long-term care payment at 100% of current spending (memo G1) | **Espen, G1** | −148.1 | −192.4 | −312.6 | −605.3 |
| 8 | The education fund at 1.7 points (memo G7) | **Espen, G7** | +7.5 | +9.1 | +14.0 | −46.4 |
| 9 | The 2 points above $20K/$40K folded into the health contribution: the base rate R from 2.25% to 3.25% from 2035, reopening `DEC-2026-11-15-11` (memo G2) | **Espen, G2** | −7.7 | +156.7 | +207.7 | −493.1 |
| | *Left to close* | | *263.4* | *410.6* | *730.7* | *1,696.3* |
| 10 | A VAT: 2.95% from the January 2035 endpoint, 3.6% from FY2041, 3.85% from FY2044, 4.6% from FY2051 (memos G3, G8) | **Espen, G3 and G8** | −266.4 | −417.8 | −733.8 | −1,193.5 |
| | **The recommended package** | | **−3.0** | **−7.2** | **−3.1** | **+502.8** |

**Why the agent's steps are not forks:**
- **Steps 1 to 3** are pricing items the audit sent here, with no change to any design. Step 1: HCU's own 20% allowance already covers H1b's folded half, so a second 15% haircut on it counts the same avoidance twice. Step 3: income withheld at source is rarely misreported, and a 2.25-3.25% rate on a broad base gives little reason to avoid. But the base rate also falls on self-employment, partnership and rental income, where misreporting is highest. So the range is 10-25%, with 10% at its floor (review F-3; part 5).
- **Step 5** is an accounting correction (part 6). The review confirms it.

**Step 9's yield.** The fold raises the health contribution's base rate by a point from 2035. In FY2040 that matches the 2 points, still at 1.2 points then. From FY2044 the 2 points would have been at their full rate, and the fold doesn't grow with them, so G8's VAT steps take up the difference. The fold is priced at about $56B a quarter point in FY2040 (`health-household-contribution.md` section 2), grown on HCU's path.

## Part 3. What the package does

### The general fund, year by year

| | FY2030 | FY2031 | FY2032 | FY2033 | FY2034 | FY2035 | FY2036 | FY2037 | FY2038 | FY2039 | **FY2040** | FY2045 | FY2050 | FY2056 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| As booked | −160 | −44 | 130 | 132 | 25 | 554 | 840 | 851 | 856 | 813 | **616** | 676 | 825 | 1,159 |
| **Recommended** | −213 | −122 | 37 | 25 | −100 | −5 | 230 | 234 | 233 | 183 | **−3** | −7 | −5 | −3 |

- **The rule's test (FY2040 and every later year): passes** in every year to FY2056. The margin is thin: about $3-7B a year. Memo G8 offers a margin of 0.1% of GDP as an option.
- **The decade (FY2030-39):** +$502.8B short, with health's early surplus counted. Held as the plan's fund reserve (memo G6), the rest of the plan's own decade figure is +$1,162.7B. FY2036-39 run about $183-234B short a year (review N-8). The rule doesn't test those years, and the debt guardrail passes with room. Read "every year from FY2040 closes" as just that, not as the decade closing.
- **Why the VAT starts in 2035, not FY2033** (review B-4): started earlier, it put the fourth fifth behind on D3 in FY2033 (−$235) and only just ahead in FY2034, before health's savings arrive. From 2035, households get the plan's health savings and the VAT in the same year. The FY2033 start is priced as an option in memo G3: it lowers the decade figure to +$83.9B and changes nothing from FY2040.

### Debt (the guardrail, on the unified budget; the budget model is the reading of record)

| % of GDP | FY2039 | FY2040 | FY2056 |
| --- | --- | --- | --- |
| Baseline | 130.3 | 132.7 | 180.2 |
| As booked (#467) | 124.8 | 126.8 | 162.5 |
| **Recommended** | **117.0** | **117.9** | **134.4** |

**The budget model is the reading of record** (`1-audit.md` item 26, an agent's choice): it carries the dedicated funds, Social Security's actual path and the education fund, which the long-term model does not.

### With and without D2 and the wealth tax (HS2)

| General-fund gap, $B | FY2040 | FY2045 | FY2056 | FY2030-39 |
| --- | --- | --- | --- | --- |
| Recommended package | −3.0 | −7.2 | −3.1 | 502.8 |
| Without D2 | 246.3 | 316.8 | 523.2 | 847.0 |
| Without HS2 | 146.9 | 177.9 | 284.2 | 1,732.8 |
| Without both | 396.3 | 501.9 | 810.5 | 2,077.0 |

Memo G5 recommends balancing with both counted, as decided, and enacting a contingent backstop. If the backstop were fully triggered, the VAT would be about 7.3% in FY2040 and about 9.7% by FY2056.

### Households: the take-home test

Health's take-home test (`DEC-2026-11-15-02`) counts visible health costs only: premiums, out-of-pocket costs, the household contribution, copays and the tax on former premiums. The review (B-3) asked for the same test with the VAT counted too. That is `take_home_vat.py`, FY2040, each option at the VAT rate its package needs:

| Memo G2 option | VAT, FY2040 | Workers ahead, health costs only (the decided test) | **Workers ahead, VAT counted** | Below 200% of poverty | 250-400% of poverty | Retirees and others (b) | Retirees and others (a) | Of them, mostly Social Security or SSI (a) | Mostly other income (a) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A: drop the 2 points | 5.40% | 88.7% | 55.6% | 79.7% | 62.8% | 85.6% | 88.4% | 97.1% | 79.3% |
| B: keep them | 3.05% | 70.1% | 53.0% | 89.1% | 61.1% | 87.9% | 90.2% | 97.8% | 82.4% |
| **C: fold into R = 3.25% (recommended)** | **2.95%** | **76.2%** | **57.8%** | **90.4%** | **64.3%** | **89.9%** | **91.9%** | **97.9%** | **85.7%** |
| D: drop, R = 2.5% | 4.80% | 85.9% | 56.0% | 82.1% | 63.0% | 86.4% | 89.0% | 97.3% | 80.5% |
| G3 E: no VAT, R = 4.45% | 0% | 60.8% | 60.8% | 98.2% | 69.0% | 96.9% | 96.9% | 100.0% | 93.8% |

How to read it:
- "(b)" is CBO's convention, with nominal incomes fixed. "(a)" is prices rising by the VAT rate, with Social Security and SSI rising too, so a retiree living on them gets the VAT back. Fixed private pensions and savings get no such offset (review B-1).
- The VAT is allocated by fifth on D3's consumption key and split among each household's tax units by persons. That is rough: consumption within a fifth isn't modelled.
- **On the decided test, A is best, at 88.7%. With the VAT counted, C is better than A for every group.** The gaps for workers below 200% of poverty and for retirees on private income are large and robust. The gap for all workers is small, within what the fifth-average VAT allocation could move. The health contribution exempts income below 138% of poverty and phases in to 250%, and a VAT has no exemption.
- **No option keeps 85% of workers ahead once the VAT is counted.** Every broad source falls on households.
- **The group just above the exemption (250-400% of poverty)** does worst under every option, at 61-69% ahead.

### Households: D3 by quintile

$ a household a year, FY2030-39 average, measured keys, every payroll row gross (the reviewer's note on #467, part 6):

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| As booked, Q-H7 as committed (EDUP net of its offset) | +14,840 | +13,209 | +12,070 | +6,837 | −62,271 | −910,567 |
| As booked, one convention (EDUP gross) | +14,827 | +13,160 | +11,972 | +6,669 | −62,652 | −912,272 |
| **Recommended package** | **+14,308** | **+12,171** | **+10,440** | **+4,553** | −65,980 | −927,243 |
| G2 A (the 2 points dropped, a VAT of 5.4%) | +13,917 | +11,701 | +9,978 | +4,157 | −65,233 | −905,968 |
| G1 B (with the four cheaper designs; VAT 1.25%) | +13,544 | +11,672 | +10,255 | +4,882 | −64,997 | −924,750 |

**D3 year by year** (`packages.Household.series`, the package's edits and the VAT on its own path; nominal $ a household):

| | FY2033 | FY2034 | FY2035 | FY2036 | FY2039 |
| --- | --- | --- | --- | --- | --- |
| Q1 | +11,764 | +13,672 | +16,021 | +18,120 | +21,553 |
| Q2 | +8,692 | +11,161 | +14,637 | +17,217 | +20,741 |
| Q3 | +6,678 | +9,129 | +12,972 | +15,760 | +19,130 |
| **Q4** | **+2,001** | **+3,291** | **+5,967** | **+8,345** | **+10,551** |
| Q5 | −60,473 | −67,705 | −71,795 | −72,287 | −80,571 |

- The fourth fifth is thinnest in FY2033-34, before the endpoint, and ahead in every year. The year-by-year engine reads about $400 above the decade average for Q4, an unexplained offset noted for the household model (review N-5).
- **The VAT a household pays in FY2040,** per point, gross: about $370 in the bottom fifth, $570 in the second, $780 in the middle, $980 in the fourth and $1,390 in the top fifth. At 2.95% that is about $1,090, $1,690, $2,300, $2,900 and $4,110.
- These figures use the FY2034-35 household count, so FY2040's count would lower them by a few percent (N-6).
- D3 doesn't count the $300 credit or the states' payment, so neither moves its quintiles. The credit's end is still a loss of up to $600 a year for a two-adult household.

### The revenue-mix test

D3's revenue-mix test requires that the top 1% (by incidence) and corporations (statutory) bear more than half of new general-fund revenue, with health's contributions left out (`DEC-2026-11-15-29`). It is computed as `d3.D3.gf_test` does, on each package's edited rows, with the VAT at its general-fund (net) yield. The single-year readings weight each row by its own path.

| Package | FY2030-39 (the test's window) | FY2040 | FY2056 |
| --- | --- | --- | --- |
| As booked | 64% | 57% | 52% |
| **Recommended** | **61%** | **54%** | **50%** |
| G2 A (dropped, larger VAT) | 57% | 50% | 46% |
| G1 B | 63% | 58% | 52% |
| G3 E (no VAT, R = 4.45%) | 65% | 61% | 58% |

- The recommended package passes on the decided window and holds about half by FY2056.
- **G3 E's higher share is partly a matter of labels:** a larger health contribution is left out of the test as a premium replacement (`DEC-2026-11-15-29`), although beyond 3.25% it pays for more than premiums. Memo G3 says so.
- With the VAT counted at its gross yield, the decade readings are 2-3 points lower.

### Social Security, HI and the education fund

- **Social Security:** unchanged, on CBO's convention. It depletes in 2093, with a 75-year balance of −0.31% of payroll. The VAT is booked at CBO's net yield, and a statutory transfer holds the trust funds harmless for their share of its payroll-tax offset (memo G3).
- **If prices rise with the VAT (reading (a))**, benefits rise by the rate. Unless the hold-harmless also covers that cost-of-living increase, the 75-year balance worsens. The cost is in the risk table (part 5): about $120B in FY2040, Social Security being most of it.
- **HI:** under the plan HI folds into the plan's fund at the January 2035 endpoint (HLT-7.22), and Medicare's hospital claims are kept whole to then. The model's HI fund after 2035 is a current-law comparison only, so its depletion date is not a plan result (review F-1, item 3).
- **The education fund:** solvent to 2104 at 1.7 points, with a reserve of $106B in FY2040. As booked, at 1.4 points, it runs out in 2035.

## Part 4. The forks, with the alternatives and their costs

The memos have the full options. Each fork is decided on its own, but the VAT is what the others add up to. Every package below is solved for the VAT that closes FY2040-56 (`packages.vat_schedule`), at about $90B a point:

| If Espen chooses... | VAT, FY2035 → FY2051 | Workers ahead, VAT counted (FY2040) |
| --- | --- | --- |
| **Every recommendation** | **2.95% → 4.6%** | **57.8%** |
| G1 B (the four cheaper designs) | 1.25% → 2.95% | not run |
| G1 at 80% for long-term care | 3.6% → 5.4% | not run |
| G1 C (the $300 credit kept) | 4.1% → 5.6% | not run |
| G2 A (drop the 2 points) | 5.4% → 7.3% | 55.6% |
| G2 B (keep them) | 3.05% → 3.3% | 53.0% |
| G2 D (drop, R = 2.5%) | 4.8% → 6.6% | 56.0% |
| G3 E (no VAT; the health contribution at about 4.45%, rising) | 0% | 60.8% |
| G8 with a margin of 0.1% of GDP | 3.55% → 5.2% | not run |
| G4 D1 (wealth tax as a minimum tax) | about 0.65 points more | |
| G5 C (balance without D2 now) | about 2.7 points more | |
| G7 C (education top-ups from the general fund) | about 0.5 points more | |
| G1 D or G3 D (no VAT, no larger contribution) | $263B in FY2040 and $731B in FY2056 must be cut | |

## Part 5. Risks

Each risk alone, added to the recommended package (`screen.py`). "VAT points" is the extra rate that would cover it in FY2040.

| Risk | Basis | FY2040 | FY2056 | VAT points |
| --- | --- | --- | --- | --- |
| Without D2 | Never achieved [EV-CAR-742] | +246.3 | +523.2 | 2.7 |
| Without HS2 | Legal risk high; *Moore* (2024) left it open | +146.9 | +284.2 | 1.6 |
| Without both | Memo G5's backstop covers these two | +396.3 | +810.5 | 4.4 |
| **Joint yield risk:** the wage stack at the working elasticity, pre-2025-law scores 10% low and the VAT 15% short | Review F-2; **no backstop covers these** | +312.7 | +647.1 | 3.5 |
| The wage stack yields at the working elasticity (0.25) | Stack note part 3: up to about $140B (rough, unverified) | +137.0 | +261.9 | 1.5 |
| Pre-2025-law scores 10% low | About $4.9T of the decade's revenue rests on them (`1-audit.md` item 22) | +132.7 | +272.1 | 1.5 |
| **Prices rise with the VAT and indexed benefits follow (reading (a))** | Review B-1: Social Security's baseline outlays times the rate, plus a third more for other indexed programs (rough). Brackets and higher nominal receipts left out | +120.4 | +347.7 | 1.3 |
| If a scorer counted the fold-in's HI shortfall as new | Part 6, item 4: the correction stands; this is the grant's size | +82.2 | +144.0 | 0.9 |
| The avoidance allowance at 20% on the base rate | Within item 9's 10-25% range; 25% would be about +$90B | +60.0 | +117.6 | 0.7 |
| C3A's compliance payments vanish | Suppliers comply (item 43) | +38.5 | +70.3 | 0.4 |
| The VAT yields 15% less | Compliance and erosion, beyond the health base already taken out | +36.9 | +107.0 | 0.4 |
| The stack cap at its high end ($55B) | Stack note part 4 | +12.0 | +25.7 | 0.1 |

- **The package has no margin.** Every risk row breaks the rule on its own. The yield risks fall on a later Congress unless memo G8's margin option is taken.
- **Capacity and delivery risk.** #467 set the long-term model's cautious reading (DEC-CAUT) to book CAP-7S, CAP-7 and AI-4 at their adopted amounts, so it carries no cost risk for them. The plan's cushion for delivery is the two contingencies: memo 10's, $78.5B inside CAP-7S and CAP-7, and the $100B line, $14.0B in FY2040. Memo G9 keeps both, with written lanes.
- **The VAT's own risks** are delivery risks: standing up a new collection system by January 2035, alongside 45 states' sales taxes.

## Part 6. Agent decisions, corrections and items carried

**Decided here (agent):**
1. **GX narrowed** (step 1; `1-audit.md` part D, item 3).
2. **HCA at $70B** (step 2; item 15). Step 7 re-derives it from the CPS's top wages when it books.
3. **The avoidance allowance by tier** (step 3; item 9), at 10% on the base rate, with a range of 10-25%.
4. **The HI grant (step 5): an accounting correction, confirmed by the milestone review** (F-1). Its basis:
   - HLT-7.22 (`DEC-2026-11-10-11`) lists the plan fund's named streams: Medicare's payroll tax, general revenue for Parts B and D, and the others. There is no general-revenue stream for Part A. HI is kept whole until the endpoint and then folds in.
   - `DEC-2026-11-15-29` puts any shortfall of the plan's fund on the general fund, so after 2035 a general-fund grant into HI is the general fund paying itself.
   - #467 cut H1a's and HLT-6's HI credits at the endpoint for the same reason.
   - The grant's amount was never adopted: "the 0.35-point illustration is not an actuarially verified adopted amount", and "a final HI grant amount" is under `not_selected` in `models/data/inputs/recovery-adoption.json`. The October 26 governing decision lists it as not selected (`legacy/governing/project-2050-governing-decisions.md`, line 450).
   - `models/tools/budget/CONVENTIONS.md` line 12 books benefits in full even after a trust fund is exhausted, so HI's current-law shortfall is in the baseline, not in the plan's gap.
   - It is intragovernmental: ending it moves the general-fund reading, not unified debt (tested).
   - **The obligation it moves, disclosed:** at the fold-in, the plan's fund takes on Part A's current-law shortfall, which the funds model puts at 0.56% of HI payroll over 75 years. Under CBO's convention that isn't a cost against the baseline, but it is a real legal commitment the plan adds, of the same order as the grant removed. The risk row "if a scorer counted it as new" sizes it.
5. **D3 on one payroll convention** (the reviewer's note on #467): every payroll row gross, as households pay it. This moves Q4 by −$168 on the booked package. Step 7 sets EDUP's incidence row to gross when it books.
6. **The VAT's yield and convention** (review B-1, B-2):
   - CBO's 5% broad-base option leaves out government-reimbursed health care but includes privately paid care (CBO budget option 56872). The plan pays for that care from 2035, so it leaves the base.
   - Taking out about 14% of the base (private health spending, about 10% of personal consumption, on a base near two-thirds of it, plus a little for public child care and pre-K) gives about **$90B a point in FY2040**, not $105B. The working assumption is a range of 12-16%.
   - Scored on CBO's convention, nominal incomes fixed, with the price-rise reading (a) as a risk row.
   - The legacy menu's "$3.5T over 2026-35" re-windows CBO's December 2024 figure, about $3.4T over 2025-34 (review N-7). It is a pre-2025-law score.
7. **The budget model as the reading of record** for the debt guardrail (item 26).
8. **The financing screens rebuilt** (item 25):
   - `models/tools/financing-protection/packages.py`, `screen.py`, `take_home_vat.py` and `test_packages.py`.
   - The pre-PR26 ceilings ("additional housing 135 to 100" and the others) are retired; they are in Git history.
   - `test_inputs_untouched` now also hashes `models/data/inputs/` (review N-4).

**The state table** (item 10; review B-5) is in [`notes/states-2026-11-20.md`](notes/states-2026-11-20.md):
- In the base year no state pays more than its current state share, at any long-term care share up to 100%.
- At 100%, the care-heavy states lose the most relief: New York's payment rises from $32.5B to $41.8B, and North Dakota's from 71% to 100% of its state share.
- On a proxy, 30 states' long-term care spending grew more than a point a year slower than the national rate over 2019-23. An index at national growth could charge them more than their own path in later years.
- Memo G1 now says so, and offers an index option.

**Carried to step 7, small, not done here** (listed in #467 for this step, outside its brief):
- the payroll point by base (item 16);
- DEM-17.02 against IMLS's baseline (item 34, up to −$0.25B in FY2040);
- CAP-7P against the SSA reclassification (item 36, about +$1.0-1.2B over FY2030-33, none in FY2040).

**Leave open, as the audit proposed:** items 6, 14, 19, 23, 27, 29, 30, 37, 38, 41 and 42. Item 29 (R1's child benefit after its window) is financed in the out-years by this package, and the Byrd-rule vehicle stays a 2029 drafting item. Item 30 (the fuel-tax path) is not needed by the package.

## Part 7. What step 7 books, if Espen takes the recommendations

All tier 3, in one PR after the decision batch:
- **Ledger rows:**
  - GX narrowed;
  - HCA at the re-derived figure;
  - HCU's allowance by tier, and its base rate at 3.25% from 2035;
  - HS2 net of the cap;
  - the recovery credit to zero;
  - HLT-9's states' payment at 100%;
  - the broad 2 points to zero;
  - a new VAT row with its path, its base net of the plan's health spending, and its statutory transfer to the trust funds.
- **Model parameters:**
  - the HI grant ended from 2035;
  - the education rate at 1.7 points.
- **D3:**
  - a VAT incidence row (consumption key, gross);
  - EDUP gross;
  - ICB dropped and HCU raised;
  - Q-H7 updated;
  - the revenue-mix test recomputed.
- **The rest:**
  - the backstop and the step rule (memos G5 and G8), as statutory text in the settlement's specification, with their legal footing;
  - the gap, D3, the take-home test (both readings) and Social Security restated.

## Method and sources

- Gap and debt: `models/tools/recovery-budget/model.py` `build_case`, case `mixed`, with each option as an explicit, labeled adjustment ("Exploratory: ...") or a `build_case` argument.
  - Revenue options enter as outlay-equivalent adjustments, which moves the general-fund and unified balances correctly; that is not a classification.
  - The education rate and the HI grant are set for one screen and restored.
  - Each package's VAT is solved for (`vat_schedule`): the lowest rates, rounded up to 0.05 points, that close FY2040-56 with steps in FY2041, FY2044 and FY2051.
- D3: `models/tools/household/d3.py` and `provisions.py` on the measured keys, scenario Q-H7, with each option's edits (`packages.Household`). The revenue-mix test is `gf_test`'s logic on the edited rows.
- The take-home test: `models/tools/health_cost_review.py` (`visible`, the unified contribution on the decided steady-rate exemption) with the VAT added (`take_home_vat.py`).
- Option sources:
  - the stack note's cap menu (`../notes/stack-2026-11-16.md` part 4);
  - `health-household-contribution.md` sections 2 and 8;
  - care memo 17 (option 7) and the flagships' own memos for G1 B (checked by the review, F-4);
  - CBO's VAT option (budget option 56872) via the legacy menu;
  - MACPAC and CMS for the state table.
- Health's first call: `models/tools/health_booking.py` `first_call()`.
- Tests: `python3 models/tools/financing-protection/test_packages.py`, after the common rebuild.
