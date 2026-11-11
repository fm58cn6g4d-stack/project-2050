# Care you can count on, part A (health): cost and financing

Role: section 6 of the care dossier, health part. It prices the provisions of section 4 on the health coverage model and reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`). Status: draft (stage D, step 4; revised after the milestone review, `review-milestone.md`, steps 1, 2 and 4; part 5 restated on the booked basis after PR #230), on `DEC-2026-11-10-09`, `-11`, `-12` and `-13`. Every figure here is project arithmetic on an exploratory model, not an official score.

## Counting rules

- **Conventions.** The budget model's (`models/tools/budget/CONVENTIONS.md`): nominal dollars by fiscal year, a cost positive, the window FY2030-39 (`ASM-WINDOW`), the increment over CBO's baseline (`ASM-INCREMENT`).
- **The model's basis.** The coverage model (`models/tools/health-coverage/`) measures federal cost as CBO does for health insurance: "federal subsidies", meaning outlays plus revenue forgone through the employer tax exclusion (`results.md`; CBO, 2026) [EV-CAR-052]. So its net figure already nets the end of the tax exclusion, a revenue effect, against spending. Part 5 splits the two, so that spending and revenue are reported on their own lines, as the budget model books them.
- **The decided variant.** The model's single plan with the decided parameters: rates about 1.15 times Medicare (memo 5 B), the model's low cost sharing for memo 4 C (3% of claims, range 1-6%, and half the rise in use that free care brings), no long-term care (part B decides it), states paying half their Medicaid spending (memo 3 B), administration at 5%. The model's "project central" single payer differs in including long-term care and no cost sharing; its $3.55 trillion in 2032 is not this design's figure.
- **The path.** `tools/health_path.py` splits the plan's 2032 cost by the group that moves and grows each group on the model's path (CBO's growth in net federal health subsidies, about 5.7% a year after 2036) [EV-CAR-052], in memo 2's order with the 2035 endpoint, on fiscal years: each fiscal year takes a quarter of the calendar year before it and three quarters of its own, so a January move counts for nine months of its first fiscal year (FY2031 runs from October 2030). It adds the hospital glide path and, as a separate stream, the employer contribution. Its simplifications are listed in the script and in part 7.
- **Run.** `python3 dossiers/care/tools/health_path.py`, November 10, 2026, on the model's committed inputs (`inputs.csv` `02448551c022`).

## 1. The plan on the coverage model

**At full scale, 2032 terms** (as if every group had moved):

| Item | $ billion, 2032 |
| --- | --- |
| The plan's outlays, net of copays ($189 billion) and including administration | 6,429 |
| Less federal money the plan replaces: Medicare 1,511; Medicaid and CHIP 763; premium credits 116 [EV-CAR-052] | −2,390 |
| Less states' payments (half their Medicaid spending, working figure; offsetting receipts, collected as section 4's HLT-7.17 sets out) | −307 |
| **Spending, net of replaced federal money and state payments** | **3,732** |
| Less revenue from ending the employer tax exclusion (a revenue effect, on CBO's convention that total compensation is fixed) [EV-CAR-052] | −680 |
| **Net federal cost on the model's basis** | **3,052** |

- Uninsured: about 3.6 million (people not enrolled or not covered because of immigration status), against 37.2 million under current law [EV-CAR-051].
- National health spending: about $212 billion lower than current law.
- Households stop paying about $1.53 trillion of premiums and out-of-pocket costs, net of the plan's copays; employers stop paying about $1.55 trillion of premiums.
- **Check against CBO.** CBO's 2020 single-payer options raised federal subsidies by $1.5 to $3.0 trillion in 2030 (CBO, 2020) [EV-CAR-218], about $1.66 to $3.32 trillion grown to 2032 (`results.md`, BM-1a). The decided variant's $3.05 trillion sits inside that range near its top; the model's own card explains why it runs high (it misses CBO's supply limits and its option specifications are not saved).

**By group** (2032, project arithmetic): today's Medicare enrollees $784 billion; Medicaid and CHIP $1,003 billion (Medicaid's low rates rise to the plan's); employer groups $692 billion; the individual market $65 billion; the newly covered $509 billion.

**Year by year, on the decided path** (net federal cost on the model's basis, before the employer contribution; $ billion):

| FY | Who is in the plan by the end of the fiscal year | Hospital rate (x Medicare, calendar year) | Net federal cost | Of which the glide path |
| --- | --- | --- | --- | --- |
| 2030 | No one yet: restoration only (HLT-1) | — | 64 | — |
| 2031 | Wave 1 (from January 2031): uninsured, individual market, children; Medicare at 60 | 1.25 | 673 | 42 |
| 2032 | Wave 1 | 1.23 | 899 | 49 |
| 2033 | + a third of Medicaid and of employer groups | 1.21 | 1,338 | 61 |
| 2034 | + a second third | 1.19 | 1,941 | 66 |
| 2035 | Everyone (endpoint, January 2035) | 1.17 | 3,283 | 70 |
| 2036 | Everyone | 1.15 | 3,774 | 18 |
| 2037 | Everyone | 1.15 | 3,967 | 0 |
| 2038 | Everyone | 1.15 | 4,191 | 0 |
| 2039 | Everyone | 1.15 | 4,429 | 0 |
| **FY2030-39** | | | **24,559** | **305** |
| 2040 | Everyone | 1.15 | **4,680** | 0 |

On calendar years, as the first draft of this section counted, the window was $25.68 trillion and FY2040 $4,743 billion; the fiscal-year basis is the one the budget model books, so it is the one reported (review F-2).

- Wave 1's children include Medicaid and CHIP children, at an assumed 20% of Medicaid spending (range 15-25%; evidence still needed). That share moves $200 billion of 2032 cost into wave 1; at 15% or 25% the FY2030-39 total moves by about $0.16 trillion either way ($24.40 to $24.72 trillion; project arithmetic).
- Medicare at 60 is counted at the model's staged-path increment until the endpoint (about $13 billion a year), an upper bound because its uninsured and individual-market movers are already in the plan.
- After 2035 every path to the same plan costs the same; the endpoint date and the order are mainly choices about money in FY2031-35.

## 2. What the model total leaves out

Items section 4 keeps that the year-by-year table does not include. Firm items (decided, expected to be spent) are apart from contingent ones (waiting on Espen or on a release condition). None is booked; each is reported:

| Item | Provision | FY2030-39 | Basis | Firm or contingent |
| --- | --- | --- | --- | --- |
| Medicare Advantage fix | HLT-6.01 | **about −$0.55 trillion** (−51 / −110 / −119 / −128 / −138 billion, FY2030-34) | MedPAC's 14%, $76 billion in 2026 [EV-CAR-135], grown at Medicare's projected 7.7% a year [EV-CAR-056]; half in 2030; Advantage ends in 2035, and the plan's cost already prices Advantage enrollees at traditional Medicare's rates | Firm (a saving) |
| Medicare upgrades for today's enrollees, FY2031-34 | HLT-2.01 | about $0.30 trillion (range $0.25-0.35 trillion) | The legacy HLT-2 profile as booked (29 / 61 / 97 / 112 billion in its first four years), moved to start in 2031 (`legacy/domains/domain-health.md`, HLT-2: $0.90-1.24 trillion over a full decade); grade D, legacy estimate | Firm |
| No disability waiting period, FY2031-34 | HLT-2.03 | about $0.10 trillion (range $0.06-0.18 trillion) | Working assumption of $15-45 billion a year (central $25 billion). Mathematica put the full cost at about $14 billion a year in 2006, about 3% of Medicare spending (Mathematica, 2009) [EV-CAR-344], and CBO's estimate was a net $6.8 billion in the first year (2011) and $110 billion through 2019, as quoted by the Commonwealth Fund (Commonwealth Fund, 2009) [EV-CAR-370]; 3% of Medicare's spending in FY2031 would be about $55-60 billion. People in the wait who are uninsured or in the individual market are already in the plan from wave 1, which lowers it, but how many are is unknown: no current count of people in the wait exists (KFF, 2024) [EV-CAR-343] | Firm |
| Worker help, FY2033-38 | HLT-7.16 | about $0.06 trillion (range $0.03-0.15 trillion) | Working assumption, widened from memo 2's $5-15 billion a year. Up to 1.8 million gross insurance and billing jobs (EPI, 2020) [EV-CAR-232], about 602,000 at insurers (BLS, 2026) [EV-CAR-233]; trade adjustment's training averaged $15,087 per completer (CRS, 2022) [EV-CAR-346], and its evaluation found weak earnings gains (Mathematica for the Labor Department, 2012) [EV-CAR-347], a single source. S. 1506 would spend at least 1% of its national budget, about $69 billion a year on the plan's scale [EV-CAR-282] | Firm |
| Hospital transition fund, FY2033-38 | HLT-7.15 | about $0.10 trillion (range $0.05-0.15 trillion) | Decided (`DEC-2026-11-10-13`); working figure, illustrated 10 / 20 / 25 / 20 / 15 / 10 billion; part 3 | Firm (a capped fund) |
| USDA rural health grants | HLT-8.01 | about $0.002-0.005 trillion | $200-500 million a year (judgment, point 6); the $3-5 billion of yearly loans costs little, at about zero subsidy (`dossiers/foundations/rural-delivery.md`) | Firm, subject to appropriation for the grants |
| Medicaid provider taxes and directed payments restored, FY2030-34 | HLT-1.03 | $0 to about $0.25 trillion | The model's `mcd_financing_restore`, $0 central, range up to about $60 billion a year (`results.md`) until each state's Medicaid moves | Firm commitment; cost is an open range |
| The territories (Puerto Rico, Guam, the U.S. Virgin Islands, the Northern Mariana Islands, American Samoa) | HLT-7.01, HLT-7.17 | about $0.13 trillion (range $0.09-0.22 trillion) | Working range of $10-25 billion a year at full scale in 2032 terms (central $15 billion), judgment. About 3.5 million people live in the five territories: Puerto Rico about 3.2 million in 2025 and the four smaller territories about 338,000 in 2020 (Census Bureau, 2025; 2020 Island Areas Censuses) [EV-CAR-357] [EV-CAR-356]. Their federal Medicaid money is capped (Puerto Rico's allotment $3.825 billion in FY2027) and the territory pays all costs above the cap (Public Law 117-328; CRS, 2023) [EV-CAR-361] [EV-CAR-358]; under current law Puerto Rico's matching rate falls back to 55% and its cap is cut from FY2028 [EV-CAR-362], so the plan's increment there is larger than its current federal money suggests. The range takes the plan's per-person cost at 50-80% of the national average for people under 65 (lower prices and use), less today's capped federal Medicaid, plus today's Medicare enrollees' move at the endpoint; it phases in on the waves (HLT-7.28). FY2040: about $23 billion (range $16-39 billion) | Firm commitment; cost is a working range |
| No abortion funding limits | RTS-2 | about $0 (legacy RTS-2: $0-0.01 trillion) | Inside the plan's cost from each wave; small in Medicaid, FEHB, the IHS and Defense before then | Firm |
| Covering people without status | HLT-7.01 | Not priced | The immigration flagship decides (point 3) | Open |
| The IHS alongside the plan | HLT-7.24 | Not priced; $0 assumed | Open item | Open |

**All-in, FY2030-39:** the plan's $24.56 trillion, less the Advantage fix ($0.55 trillion), plus the firm items above (upgrades, the disability wait, worker help, USDA grants and the transition fund, $0.56 trillion) and the territories ($0.13 trillion) is **about $24.7 trillion**. That is a reading of firm items plus the model's path, before the employer contribution. It is not a score. The Advantage fix, upgrades and disability wait are counted from their January start dates as whole fiscal years; at nine months in their first year they would be a few billion dollars lower, inside their ranges.

## 3. Softening the transition for hospitals: the options, and the decision

Espen's direction (`DEC-2026-11-10-11`): "we can alter the hospital pay glide path and/or add some extra funding to soften the blow of a faster transition, especially for rural providers". Espen chose option A below (`DEC-2026-11-10-13`).

**What the move does to hospital revenue** (project arithmetic, `hospital_revenue()`; nominal $ billion, all hospitals, by calendar year). For the newly insured, the plan's payment is counted net of what hospitals collect for them today: the low reading subtracts all of their current care (their own payments and the uncompensated care that Medicaid DSH, state programs and cost shifting now fund), the high reading only their own payments (the coverage model's `unins_paid_share`, 35%):

| Calendar year | Commercial revenue lost as employer and individual groups move | Net change, all hospitals (low to high reading) |
| --- | --- | --- |
| 2031 | −137 | +104 to +193 |
| 2033 | −362 | +26 to +126 |
| 2034 | −607 | −72 to +33 |
| 2035 | −885 | −29 to +81 |
| 2036 | −946 | −99 to +18 |
| 2039 | −1,108 | −116 to +21 |

At the target rate (2032 terms), hospitals lose about $767 billion on commercial patients and gain about $437 billion from Medicaid's patients, $126 billion from today's Medicare patients and $125-219 billion from the newly insured. The net is between about −$80 billion and +$15 billion, or between about 4% lower and 1% higher on hospital revenue of about $2 trillion (CMS's $1,634.7 billion in 2024 grown; EV-CAR-055). So the move shifts revenue between hospitals on a scale about ten times its net effect on hospitals as a whole. While the glide keeps rates above the target (through 2035) the total stays near or above today's; after it, the total may fall a little. Medicaid DSH inside Medicaid's spending is repriced with Medicaid's claims, a small upward bias on the gains.

Who loses is the hospitals with many commercial patients and high prices, where for-profit and urban hospitals earn the largest margins (MedPAC, 2026) [EV-CAR-336]. Rural hospitals depend more on Medicare, which pays them closer to cost [EV-CAR-337], so many gain. The ones at risk are rural hospitals with a large commercial share and thin margins: 87 rural hospitals have closed and 68 converted since 2010 (Sheps Center, 2026) [EV-CAR-338]. The finding rests on national averages of rates and payer mix; hospital-level data is needed to confirm it (section 4, "Evidence still needed").

| Option | What it does | FY2030-39 cost | Who it reaches |
| --- | --- | --- | --- |
| **A. Keep the five-year glide; add a capped transition fund and a revenue floor for global-budget hospitals (decided, `DEC-2026-11-10-13`)** | HLT-7.15: $100 billion over FY2033-38 for hospitals whose net patient revenue falls more than 5%, rural and sole providers first; global budgets held at least at pre-transition revenue for three years | about $0.10 trillion (range $0.05-0.15 trillion) | The hospitals that lose, and first the ones a community depends on |
| B. Slow the glide to seven years (2038) | The plan's hospital rate falls from 1.25 to 1.15 times Medicare over seven years | about +$0.29 trillion (3 / 10 / 25 / 68 / 101 / 69 / 14 billion, FY2032-38) | Every hospital by volume, including those that gain; little for the losers, because the glide starts at the all-payer average; it would cover the possible dip in hospitals' total revenue in FY2035-37 |
| C. Both | A and B | about +$0.39 trillion | Both |
| D. Neither | The decided glide alone (it costs $0.31 trillion over FY2031-36 against moving straight to 1.15) | $0 | No targeted help |

**Why A (recommended, and decided in `DEC-2026-11-10-13`).** The transition's main effect is a shift between hospitals, and A reaches the hospitals that lose, rural and sole providers first, for about a third of B's cost, without raising rates for hospitals that gain. B's case is the low reading: if hospitals as a whole lose up to about 4% after the glide ends, a seven-year glide would roughly cover that dip in FY2035-37 (it adds $68 billion and $101 billion in FY2035 and 2036). But a lasting shortfall in hospitals as a whole is a question about the 1.15 target (memo 5; section 8 sets its trigger), not about the transition, and a longer glide would not fix it. If hospital-level data shows losses wider than the national averages suggest, raise the fund's cap first.

## 4. The fund's streams and the amount to be financed

Memo 3 B, confirmed (`DEC-2026-11-10-11`): the existing public streams stay, states and employers pay a share, and new revenue fills the rest (HLT-7.22).

| Stream (full scale) | 2032 ($ billion) | FY2040 ($ billion) | Treatment |
| --- | --- | --- | --- |
| Replaced federal money (Medicare, Medicaid and CHIP, premium credits) | 2,390 | — | Already in CBO's baseline; pooled into the fund, not new cost |
| States' payments | 307 | inside the net | Working figure (half of their Medicaid spending; range 0-80%, each 10 points about $60 billion a year in 2032) |
| Revenue from ending the employer tax exclusion, with no employer contribution | 680 | 1,043 | A revenue effect, **on CBO's convention that total compensation is fixed**: every former premium not paid as the contribution becomes taxable wages. Counted only on premiums that become taxable wages. If only half the employer-paid share passed into pay (Anand, 2017) [EV-CAR-299], it would be about $242 billion lower in 2032 and $370 billion lower in FY2040 (part 6) |
| **Net federal cost on the model's basis** | **3,052** | **4,680** | Before the employer contribution |
| Employer transitional contribution at about 65%, net of the exclusion revenue it displaces | 692 | 1,061 | 65% is the share at which employer moves cost the federal budget nothing (project arithmetic). Gross it is about $1,006 billion in 2032 (65% of $1,547 billion); because that money is not paid as wages, the exclusion revenue falls by about $314 billion, so its net yield is $692 billion. Never added to a full exclusion figure |
| **Left for new revenue (the financing settlement)** | **2,360** | **3,619** | The amount the settlement finances, if the contribution is paid at 65%; about $85 billion (2032) and $130 billion (FY2040) more at half pass-through |

The contribution runs from each move until the settlement's payroll contribution takes effect (HLT-7.18). If the settlement replaces it with a broad payroll contribution, that contribution is part of the settlement's revenue, not a second stream on top. On the decided path the contribution yields about $5.31 trillion net over FY2030-39 at 65% ($6.53 trillion at 80%), bringing the net federal cost from $24.56 trillion to about $19.2 trillion ($18.0 trillion at 80%) (project arithmetic).

**A known overstatement: federal coverage inside the employer group.** The coverage model's employment-based cell includes FEHB, TRICARE and veterans' programs (`models/tools/health-coverage/inputs.csv`, row 7). So the plan prices their enrollees as employer-group movers, counts their premiums among the employer premiums removed, and counts a contribution on them. Two corrections follow, sized in part 6: TRICARE and the VA continue (HLT-7.24), so their outlays are not replaced; and FEHB's contribution is the government paying itself (HLT-7.26), intragovernmental, not revenue. Both make the employer savings and the contribution read high by the share of the cell these groups hold. The booking (part 5) keeps FEHB's contribution off the revenue side; no decision turns on the size (about 6-9% of the cell; part 6).

## 5. The fiscal-rule report

Under `DEC-2026-11-10-05`, health reports its effect and passes it to the settlement. The budget model now books the decided design (PR #230, care fix step 5, `models/tools/health_booking.py`), so this part reports the booked rows. The legacy rows they replaced are kept in the last column for comparison. Each figure has one basis: federal fiscal years, $ billion, a cost positive, read from the fiscal model's FY2040 row paths and `models/data/recovery-budget-paths.csv` (case `mixed`).

| Row | What it books | FY2030-39 ($ trillion) | FY2040 ($ billion) | Legacy row, FY2040 ($ billion) |
| --- | --- | --- | --- | --- |
| HLT-1 | Restoration before wave 1, calendar 2030 | 0.086 | 0 | 305.6 |
| HLT-2 | Medicare upgrades and no disability wait, calendar 2031-34 | 0.399 | 0 | 157.6 |
| HLT-3, HLT-5 | Retired (public option; commercial price cap) | 0 | 0 | 285.7 and −72.2 |
| HLT-4 | Long-term care and the safety-net items kept; children's coverage and Medicaid dental end as their groups join the plan | 0.498 | **62.3** | 85.1 |
| HLT-6 | Advantage fix at MedPAC's lower estimate, calendar 2030-34: Part B's 60% on the general fund; Part A's 40% ($0.218 trillion) is credited to HI | −0.328 | 0 | −192.6 |
| HLT-7 | The plan's spending line: outlays less the federal money it replaces and the states' payments, plus the hospital transition fund and the territories | 29.922 | **5,745.2** (the plan 5,722.1; the territories 23.0; the fund 0) | — |
| HLT-8 | USDA rural health grants | 0.004 | 0.5 | — |
| HX (revenue) | End of the employer tax exclusion, general fund, full pass-through | −5.219 | **−1,042.5** | — |
| **Health, net as booked** | | **25.36** | **4,765.4** | 569.2 |

The two FY2040 differences from this section's earlier proposal cancel. HLT-4 is booked at about $62 billion, not $85 billion, because its children's and Medicaid dental parts end once those groups are in the plan (review F-4, item 2). The territories add about $23 billion inside HLT-7. So the plan-wide figure is the one part 5 predicted.

| Measure, FY2040 | Before the booking (legacy health) | As booked |
| --- | --- | --- |
| Plan-wide general-fund primary balance (`agenda_gf_primary_bn`, case `mixed`, before interest) | $75.9 billion short | **$4,272 billion short** (7.9% of GDP) |
| The same, if the employer contribution were booked at 65% | — | about $3,211 billion short (5.9% of GDP) |
| Health's own net cost, as booked | $569 billion | $4,765 billion (8.8% of GDP) |

GDP is the budget model's ($54,167 billion in FY2040). Health's net cost is nearly all of the plan-wide gap. That gap is expected: it is the premium-to-tax shift that the financing settlement designs (memo 1; `3-design.md`). It is a figure to report, not an error to fix, and the plan-wide balance cannot be read until the settlement books health's financing.

**The employer contribution is reported, not booked.** At 65% it yields **$1,061 billion net in FY2040** and about $5.31 trillion over FY2030-39 (part 4). It stays off the books until the settlement sets its share (HLT-7.18; review F-4, item 3), and `test_fiscal_health.py` checks that no contribution row is booked. When it is booked, it must be booked **net of the exclusion revenue it displaces**: the contribution's gross $1,006 billion (2032) is money employers no longer pay as wages, so HX must fall by the tax on it, about $314 billion in 2032. HX assumes full pass-through: every former premium not paid as the contribution becomes taxable pay. Without that reduction, the same premium dollars would be counted twice, once as wages taxed through HX and once as the contribution.

**Why the totals differ from the all-in reading in part 2.** The booked general-fund FY2030-39 total, $25.36 trillion, is part 2's $24.7 trillion plus HLT-4 ($0.50 trillion, which part 2 leaves to part B), plus the Advantage fix's Part A share ($0.22 trillion), which goes to HI rather than the general fund, and less worker help (HLT-7.16, about $0.06 trillion over FY2033-38), which has no booked row. Worker help ends before FY2040, so it does not touch the FY2040 figures. It goes in the next tier-3 change to the health rows.

**What the booking does not yet correct** (each labeled on its row):
1. **FEHB, TRICARE and the VA** are priced as employer-group movers (part 4), so HLT-7 and HX read high. Part 6 bounds it: net cost high by about $35-105 billion in FY2040.
2. **The household test (D3)** now carries HLT-7's household rows, but only as scenario Q-H7, before the settlement's new taxes (part 8). Neither Q nor Q-H7 is health's D3 result.
3. **The hospital trust fund (HI)** now gets Part A's share of the Advantage fix (40%, $0.22 trillion, FY2030-34; a working assumption, range 36-45%), on the fix's own path, in place of the legacy $0.7 trillion held as a share of payroll forever. MedPAC's 14% is a total over Parts A and B, so the old credit counted the same savings twice. With its program sources HI lasts to 2040 on the funds model's rates, past the 2035 endpoint, when it folds into the plan's fund (HLT-7.22); that is the HI reading to quote, and only to the endpoint.
4. **HX's payroll-tax part** would by law go to the Social Security and HI trust funds. It is booked on the general fund, as the review asked; the settlement can redirect it.

## 6. Sensitivities

Each line changes one working assumption on the decided path (project arithmetic):

| Case | Net federal, 2032 full scale ($B) | FY2030-39 ($T) | FY2040 ($B) |
| --- | --- | --- | --- |
| As decided | 3,052 | 24.56 | 4,680 |
| Hospital and plan target 1.05 x Medicare | 2,538 | 20.99 | 3,891 |
| Target 1.25 x Medicare | 3,567 | 28.12 | 5,468 |
| States pay nothing (as S. 1506; also the fallback if the payment fails, HLT-7.17) | 3,359 | 27.00 | 5,150 |
| States pay 80% | 2,868 | 23.10 | 4,397 |
| Copays 1% of claims | 3,178 | 25.51 | 4,872 |
| Copays 6% of claims | 2,864 | 23.13 | 4,390 |
| Administration 3% / 8% | 2,916 / 3,268 | 23.52 / 26.20 | 4,470 / 5,010 |
| Medicaid's current rates 0.60 / 0.85 x Medicare | 3,477 / 2,727 | 27.74 / 22.12 | 5,331 / 4,182 |
| Commercial hospital prices 2.0 / 2.8 x Medicare | 3,351 / 2,939 | 26.69 / 23.75 | 5,137 / 4,506 |
| Children at 15% / 25% of Medicaid spending | 3,052 | 24.40 / 24.72 | 4,680 |
| Half of employer-paid premiums passed into pay (revenue; against CBO's convention) | +242 (no contribution) / +85 (at 65%) | — | +370 / +130 |

The payment rate dominates, as memo 5 said: each 0.1 of the target moves FY2040 by about $0.8 trillion. Medicaid's starting rates come next, because wave 2 raises them to the plan's.

**Federal coverage inside the employer cell: a bounded overstatement.** Part 4 explains the error: the coverage model's employment-based cell (169.5 million people) includes FEHB, TRICARE and veterans' coverage, so the model prices those enrollees as private employer-group movers. This bounds it. Every figure is project arithmetic, a working range, on the cell's 2032 full-scale averages: the plan's cost for the cell, $1,372 billion; employer-paid premiums, $1,547 billion; exclusion revenue, $680 billion. The FY2040 figures scale these by HX's growth (×1.53).

- **How many people.**
  - FEHB and the Postal Service plan cover about 8.2 million people [EV-CAR-371]. Those with Medicare as primary coverage sit in CBO's Medicare count, so about 6-7 million are in the cell (judgment).
  - TRICARE has 9.4 million beneficiaries, about 2.5 million of them on TRICARE for Life, which is Medicare [EV-CAR-372]. So 4.5-6.9 million are in the cell, fewer if civilian employer coverage is their primary coverage.
  - Veterans with VA care and no other coverage: 0-1.5 million (judgment).
  - Together, 10.5-15.4 million people, 6-9% of the cell.
- **The spending line (HLT-7) reads high.**
  - For FEHB, the government's own share of the premiums, 72% by law [EV-CAR-373], is federal money the plan replaces, but the model treats it as a private premium. That is $55-64 billion in 2032.
  - For TRICARE and the VA, which continue (HLT-7.24), either the plan's cost for these people is not incurred or the federal programs' purchased care falls. Neither is counted. That is up to $36-68 billion if purchased care falls one for one; military and VA facilities' own costs are mostly fixed and do not fall when patients use the plan, so the low end is about $10 billion.
  - Total: **$65-130 billion in 2032; about $100-200 billion in FY2040.**
- **The revenue line (HX) also reads high.** None of these people's coverage turns into taxable wages: FEHB's employer share goes into the fund (HLT-7.26), and TRICARE and the VA charge no employer premium. That is **$40-60 billion in 2032; about $65-95 billion in FY2040.**
- **Net federal cost reads high by about $25-70 billion in 2032 and $35-105 billion in FY2040.** That is 0.8-2.3% of the $4,680 billion, and about $0.2-0.5 trillion over FY2030-39 (employer groups move from 2033).
- **Timing.** FEHB moves at the endpoint (HLT-7.26), not in wave 2 as the model has it. This shifts some of the cost later within the window but does not change FY2040.

The range is smaller than one step of 0.05 in the target rate, and no decision turns on it. The correction (lower HLT-7 and HX by the central figures) goes in the next tier-3 change to the health rows. Until then, the rows stay labeled as overstated.

## 7. Commitment, assumption or open question

- **Commitments (decided):** who is covered and when (HLT-7.01, 7.03); the benefit and the 200% copay line (HLT-7.05, 7.06); the rate basis and its glide (HLT-7.10); the five protections; the fund's streams, including the exclusion revenue counted only on premiums that become wages (HLT-7.22).
- **Working assumptions** (basis and range above): the exclusion revenue on CBO's convention (full pass-through into wages); the 1.15 target; copays at 3% of claims and a $1,000 cap; the states' half share; the employer contribution at 65%; a third of each wave-2 group a year; children at 20% of Medicaid spending; administration at 5%; growth on CBO's net-subsidy path; the costs of worker help, the disability wait and the upgrades. The cost of being wrong is mostly in the target rate and Medicaid's starting rates (part 6).
- **Open questions:** covering people without status (the immigration flagship); IHS funding; TRICARE's purchased care; separate capital funding and a bar on profit (section 4).
- **Study in implementation:** hospital-level effects from cost reports (before the fund's formula is set, 2032); whether copays damp specialist use as memo 4 expects (wave 1's data); take-up of the plan by people the records miss.
- **Simplifications in the path** (`health_path.py`): fiscal years blend calendar years a quarter and three quarters; people restored to Medicaid in 2030 are counted with the newly covered from 2031; the glide applies to hospital claims as a share of non-drug claims; groups are grown on one growth path. None changes a decision.

## 8. Fit with the fairness test (D3)

At full scale households stop paying about $1.53 trillion a year in premiums and out-of-pocket costs (2032), keeping only the plan's copays above 200% of poverty. Employers stop paying $1.55 trillion of premiums and pay the contribution meanwhile. Whether households below the top come out ahead depends on the taxes the settlement chooses to replace those payments (D3); section 7 reports household cost by income from the coverage model before the new taxes. The project's household test now has the plan's household rows (`models/tools/health_booking.py`, `incidence()`), over FY2030-39: premiums and out-of-pocket costs households stop paying ($11.7 trillion, H7h), employer premiums that become pay on HX's full pass-through ($11.9 trillion, H7w), and HX's tax on that pay ($5.2 trillion, H7x). They count cash only, not the value of new coverage to the uninsured. They sit in scenario Q-H7, not in the decided package Q, because the plan's financing (about $3.6 trillion a year by FY2040) has no rows yet: with the relief and none of the taxes, Q-H7's fourth quintile gains about $17,500 a year, a reading before financing, not a pass. Q leaves health out on both sides. Health's D3 result can be read only once the settlement's taxes are rowed against Q-H7. Package B's exclusion cap (C19b, and its fallback C19) now ends with the exclusion it caps: it is scaled to the employer coverage not yet in the plan ($0.66 trillion to $0.16 trillion over FY2030-39, nothing from FY2036), since the cap has no base once a group's premiums leave the exclusion. That removes a double count with HX: the decided package's FY2040 general-fund shortfall in the fiscal model rises by about $101 billion (to $4,431 billion), and accepted revenue falls from $3.71 trillion to $3.21 trillion; the plan-wide figure above ($4,272 billion) already left C19b out.

## Open questions

None for Espen: the hospital fund was decided in `DEC-2026-11-10-13`.
1. **For the lead (booking, tier 3):** booked in PR #230. Two corrections wait for the next tier-3 change to the health rows: worker help (HLT-7.16, about $0.06 trillion over FY2033-38, not booked) and the federal-coverage overstatement (part 6).
2. **For the settlement:** the employer contribution's share and the date the payroll contribution replaces it; the states' share, and the hold-harmless fallback if the payment cannot be enforced (HLT-7.17; about $307 billion in 2032); the new revenue of about $2.4 trillion (2032 full scale) to $3.6 trillion (FY2040), or about $0.1 trillion more on either if less of the former premiums passes into pay.
