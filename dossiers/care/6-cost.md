# Care you can count on, part A (health): cost and financing

Role: section 6 of the care dossier, health part. It prices the provisions of section 4 on the health coverage model and reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`). Status: draft (stage D, step 4, PR 1), on `DEC-2026-11-10-09` and `DEC-2026-11-10-11`. Every figure here is project arithmetic on an exploratory model, not an official score.

## Counting rules

- **Conventions.** The budget model's (`models/tools/budget/CONVENTIONS.md`): nominal dollars by fiscal year, a cost positive, the window FY2030-39 (`ASM-WINDOW`), the increment over CBO's baseline (`ASM-INCREMENT`).
- **The model's basis.** The coverage model (`models/tools/health-coverage/`) measures federal cost as CBO does for health insurance: "federal subsidies", meaning outlays plus revenue forgone through the employer tax exclusion (`results.md`; CBO, 2026) [EV-CAR-052]. So its net figure already nets the end of the tax exclusion, a revenue effect, against spending. Part 5 splits the two, so that spending and revenue are reported on their own lines, as the budget model books them.
- **The decided variant.** The model's single plan with the decided parameters: rates about 1.15 times Medicare (memo 5 B), the model's low cost sharing for memo 4 C (3% of claims, range 1-6%, and half the rise in use that free care brings), no long-term care (part B decides it), states paying half their Medicaid spending (memo 3 B), administration at 5%. The model's "project central" single payer differs in including long-term care and no cost sharing; its $3.55 trillion in 2032 is not this design's figure.
- **The path.** `tools/health_path.py` splits the plan's 2032 cost by the group that moves and grows each group on the model's path (CBO's growth in net federal health subsidies, about 5.7% a year after 2036) [EV-CAR-052], in memo 2's order with the 2035 endpoint. It adds the hospital glide path and, as a separate stream, the employer contribution. Its simplifications are listed in the script and in part 7.
- **Run.** `python3 dossiers/care/tools/health_path.py`, November 10, 2026, on the model's committed inputs (`inputs.csv` `02448551c022`).

## 1. The plan on the coverage model

**At full scale, 2032 terms** (as if every group had moved):

| Item | $ billion, 2032 |
| --- | --- |
| The plan's outlays, net of copays ($189 billion) and including administration | 6,429 |
| Less federal money the plan replaces: Medicare 1,511; Medicaid and CHIP 763; premium credits 116 [EV-CAR-052] | −2,390 |
| Less states' payments (half their Medicaid spending, working figure) | −307 |
| **Spending, net of replaced federal money and state payments** | **3,732** |
| Less revenue from ending the employer tax exclusion (a revenue effect) [EV-CAR-052] | −680 |
| **Net federal cost on the model's basis** | **3,052** |

- Uninsured: about 3.6 million (people not enrolled or not covered because of immigration status), against 37.2 million under current law [EV-CAR-051].
- National health spending: about $212 billion lower than current law.
- Households stop paying about $1.53 trillion of premiums and out-of-pocket costs, net of the plan's copays; employers stop paying about $1.55 trillion of premiums.
- **Check against CBO.** CBO's 2020 single-payer options raised federal subsidies by $1.5 to $3.0 trillion in 2030 (CBO, 2020) [EV-CAR-218], about $1.66 to $3.32 trillion grown to 2032 (`results.md`, BM-1a). The decided variant's $3.05 trillion sits inside that range near its top; the model's own card explains why it runs high (it misses CBO's supply limits and its option specifications are not saved).

**By group** (2032, project arithmetic): today's Medicare enrollees $784 billion; Medicaid and CHIP $1,003 billion (Medicaid's low rates rise to the plan's); employer groups $692 billion; the individual market $65 billion; the newly covered $509 billion.

**Year by year, on the decided path** (net federal cost on the model's basis, before the employer contribution; $ billion):

| FY | Who is in the plan | Hospital rate (x Medicare) | Net federal cost | Of which the glide path |
| --- | --- | --- | --- | --- |
| 2030 | No one yet: restoration only (HLT-1) | — | 86 | — |
| 2031 | Wave 1: uninsured, individual market, children; Medicare at 60 | 1.25 | 868 | 56 |
| 2032 | Wave 1 | 1.23 | 909 | 47 |
| 2033 | + a third of Medicaid and of employer groups | 1.21 | 1,481 | 66 |
| 2034 | + a second third | 1.19 | 2,094 | 66 |
| 2035 | Everyone (endpoint) | 1.17 | 3,680 | 71 |
| 2036 | Everyone | 1.15 | 3,805 | 0 |
| 2037 | Everyone | 1.15 | 4,021 | 0 |
| 2038 | Everyone | 1.15 | 4,248 | 0 |
| 2039 | Everyone | 1.15 | 4,489 | 0 |
| **FY2030-39** | | | **25,681** | **305** |
| 2040 | Everyone | 1.15 | **4,743** | 0 |

- Wave 1's children include Medicaid and CHIP children, at an assumed 20% of Medicaid spending (range 15-25%; evidence still needed). That share moves $200 billion of 2032 cost into wave 1; at 15% or 25% the FY2030-39 total moves by about $0.16 trillion either way (project arithmetic).
- Medicare at 60 is counted at the model's staged-path increment until the endpoint (about $13 billion a year), an upper bound because its uninsured and individual-market movers are already in the plan.
- After 2035 every path to the same plan costs the same; the endpoint date and the order are mainly choices about money in FY2031-35.

## 2. What the model total leaves out

Items section 4 keeps that the year-by-year table does not include. Firm items (decided, expected to be spent) are apart from contingent ones (waiting on Espen or on a release condition). None is booked; each is reported:

| Item | Provision | FY2030-39 | Basis | Firm or contingent |
| --- | --- | --- | --- | --- |
| Medicare Advantage fix | HLT-6.01 | **about −$0.55 trillion** (−51 / −110 / −119 / −128 / −138 billion, FY2030-34) | MedPAC's 14%, $76 billion in 2026 [EV-CAR-135], grown at Medicare's projected 7.7% a year [EV-CAR-056]; half in 2030; Advantage ends in 2035, and the plan's cost already prices Advantage enrollees at traditional Medicare's rates | Firm (a saving) |
| Medicare upgrades for today's enrollees, FY2031-34 | HLT-2.01 | about $0.30 trillion (range $0.25-0.35 trillion) | The legacy HLT-2 profile as booked (29 / 61 / 97 / 112 billion in its first four years), moved to start in 2031 (`legacy/domains/domain-health.md`, HLT-2: $0.90-1.24 trillion over a full decade); grade D, legacy estimate | Firm |
| No disability waiting period, FY2031-34 | HLT-2.03 | about $0.08 trillion (range $0.04-0.12 trillion) | Working assumption of $10-30 billion a year: Mathematica put the full cost at about $14 billion a year in 2006, about 3% of Medicare spending (Mathematica, 2009) [EV-CAR-344], a single source; many people in the wait are uninsured or in the individual market and join the plan in wave 1 anyway | Firm |
| Worker help, FY2033-38 | HLT-7.16 | about $0.06 trillion (range $0.03-0.15 trillion) | Working assumption, widened from memo 2's $5-15 billion a year. Up to 1.8 million gross insurance and billing jobs (EPI, 2020) [EV-CAR-232], about 602,000 at insurers (BLS, 2026) [EV-CAR-233]; trade adjustment's training averaged $15,087 per completer (CRS, 2022) [EV-CAR-346], and its evaluation found weak earnings gains (Mathematica for the Labor Department, 2012) [EV-CAR-347], a single source. S. 1506 would spend at least 1% of its national budget, about $69 billion a year on the plan's scale [EV-CAR-282] | Firm |
| Hospital transition fund, FY2033-38 | HLT-7.15 | $0 or about $0.10 trillion (range $0.05-0.15 trillion) | Working figure; illustrated 10 / 20 / 25 / 20 / 15 / 10 billion; part 3 | **Contingent on Espen** (question 1) |
| USDA rural health grants | HLT-8.01 | about $0.002-0.005 trillion | $200-500 million a year (judgment, point 6); the $3-5 billion of yearly loans costs little, at about zero subsidy (`dossiers/foundations/rural-delivery.md`) | Firm, subject to appropriation for the grants |
| Medicaid provider taxes and directed payments restored, FY2030-34 | HLT-1.03 | $0 to about $0.25 trillion | The model's `mcd_financing_restore`, $0 central, range up to about $60 billion a year (`results.md`) until each state's Medicaid moves | Firm commitment; cost is an open range |
| No abortion funding limits | RTS-2 | about $0 (legacy RTS-2: $0-0.01 trillion) | Inside the plan's cost from each wave; small in Medicaid, FEHB, the IHS and Defense before then | Firm |
| Covering people without status | HLT-7.01 | Not priced | The immigration flagship decides (point 3) | Open |
| The IHS alongside the plan | HLT-7.24 | Not priced; $0 assumed | Open item | Open |

**All-in, FY2030-39:** the plan's $25.68 trillion, less the Advantage fix ($0.55 trillion), plus the firm items above ($0.44 trillion) is **about $25.6 trillion**; with the transition fund, about $25.7 trillion. That is an upper reading of firm items plus the model's path, before the employer contribution. It is not a score.

## 3. Softening the transition for hospitals: the options

Espen's direction (`DEC-2026-11-10-11`): "we can alter the hospital pay glide path and/or add some extra funding to soften the blow of a faster transition, especially for rural providers".

**What the move does to hospital revenue** (project arithmetic, `hospital_revenue()`; nominal $ billion, all hospitals; before the relief of uncompensated care, a further gain for hospitals that serve the uninsured):

| FY | Commercial revenue lost as employer and individual groups move | Net change, all hospitals |
| --- | --- | --- |
| 2031 | −137 | +242 |
| 2033 | −362 | +180 |
| 2034 | −607 | +90 |
| 2035 | −885 | +141 |
| 2036 | −946 | +81 |
| 2039 | −1,108 | +95 |

At the plan's rates, the hospital revenue lost on commercial patients is more than made up across all hospitals by Medicaid's patients (about +$437 billion in 2032 terms), today's Medicare patients (+$126 billion) and the newly insured (+$270 billion). So the move redistributes hospital revenue more than it cuts it. Who loses is the hospitals with many commercial patients and high prices, where for-profit and urban hospitals earn the largest margins (MedPAC, 2026) [EV-CAR-336]. Rural hospitals depend more on Medicare, which pays them closer to cost [EV-CAR-337], so many gain. The ones at risk are rural hospitals with a large commercial share and thin margins: 87 rural hospitals have closed and 68 converted since 2010 (Sheps Center, 2026) [EV-CAR-338]. The finding rests on national averages of rates and payer mix; hospital-level data is needed to confirm it (section 4, "Evidence still needed").

| Option | What it does | FY2030-39 cost | Who it reaches |
| --- | --- | --- | --- |
| **A. Keep the five-year glide; add a capped transition fund and a revenue floor for global-budget hospitals (recommended)** | HLT-7.15: $100 billion over FY2033-38 for hospitals whose net patient revenue falls more than 5%, rural and sole providers first; global budgets held at least at pre-transition revenue for three years | about $0.10 trillion (range $0.05-0.15 trillion) | The hospitals that lose, and first the ones a community depends on |
| B. Slow the glide to seven years (2038) | The plan's hospital rate falls from 1.25 to 1.15 times Medicare over seven years | about +$0.29 trillion (3 / 13 / 28 / 81 / 107 / 57 billion, FY2032-37) | Every hospital by volume, including those that gain; little for the losers, because the glide starts at the all-payer average |
| C. Both | A and B | about +$0.39 trillion | Both |
| D. Neither | The decided glide alone (it costs $0.31 trillion over FY2031-35 against moving straight to 1.15) | $0 | No targeted help |

**Recommendation: A.** It reaches the hospitals Espen named for about a third of B's cost, and it does not raise the plan's rates for hospitals that are already gaining. If hospital-level data shows the losses are wider than the national averages suggest, the fund's cap is the number to raise, not the glide. This is the one question for Espen in this PR.

## 4. The fund's streams and the amount to be financed

Memo 3 B, confirmed (`DEC-2026-11-10-11`): the existing public streams stay, states and employers pay a share, and new revenue fills the rest (HLT-7.22).

| Stream (full scale) | 2032 ($ billion) | FY2040 ($ billion) | Treatment |
| --- | --- | --- | --- |
| Replaced federal money (Medicare, Medicaid and CHIP, premium credits) | 2,390 | — | Already in CBO's baseline; pooled into the fund, not new cost |
| States' payments | 307 | inside the net | Working figure (half of their Medicaid spending; range 0-80%, each 10 points about $60 billion a year in 2032) |
| Revenue from ending the employer tax exclusion, with no employer contribution | 680 | 1,057 | A revenue effect. **Counted only on premiums that become taxable wages** |
| **Net federal cost on the model's basis** | **3,052** | **4,743** | Before the employer contribution |
| Employer transitional contribution at about 65%, net of the exclusion revenue it displaces | 692 | 1,075 | 65% is the share at which employer moves cost the federal budget nothing (project arithmetic). Gross it is about $1,006 billion in 2032 (65% of $1,547 billion); because that money is not paid as wages, the exclusion revenue falls by about $314 billion, so its net yield is $692 billion. Never added to a full exclusion figure |
| **Left for new revenue (the financing settlement)** | **2,360** | **3,668** | The amount the settlement finances, if the contribution is paid at 65% |

The contribution runs from each move until the settlement's payroll contribution takes effect (HLT-7.18). If the settlement replaces it with a broad payroll contribution, that contribution is part of the settlement's revenue, not a second stream on top. On the decided path the contribution yields about $5.56 trillion net over FY2030-39 at 65% ($6.84 trillion at 80%), bringing the net federal cost from $25.68 trillion to about $20.1 trillion ($18.8 trillion at 80%) (project arithmetic).

## 5. The fiscal-rule report

Under `DEC-2026-11-10-05`, health reports its effect and passes it to the settlement. One basis for each figure:

| Measure | As the budget model books health now (legacy HLT-1 to HLT-6) | The decided design, on the coverage model's path |
| --- | --- | --- |
| FY2030-39 | **$4.40 trillion** (restore 2.45; upgrades 1.07; public option 1.90; Medicaid and long-term care 0.63; prices −0.40; Advantage −1.25) | **about $25.6 trillion** net (part 2), before the employer contribution; about $20.1 trillion with it at 65% |
| Permanent cost, FY2040, on the model's basis | **$569 billion** (HLT-1 306, HLT-2 158, HLT-3 286, HLT-4 85, HLT-5 −72, HLT-6 −193) | **$4,743 billion** (8.8% of GDP), before the employer contribution |
| FY2040, spending line | the same $569 billion, all spending | **$5,800 billion**: the plan's outlays less the federal money it replaces and the states' payments |
| FY2040, revenue line | none | **+$1,057 billion** from ending the tax exclusion; **+$1,075 billion** net from the employer contribution at 65% while it lasts |
| FY2040, net after the contribution | — | **$3,668 billion** (6.8% of GDP) |
| Share of the plan-wide margin, FY2040 | The plan-wide FY2040 balance is **$75.9 billion short** with legacy health booked (`models/data/recovery-budget-paths.csv`, case `mixed`, `agenda_gf_primary_bn`); legacy health's $569 billion is about 7.5 times it | Rebooked on this design, the plan-wide FY2040 gap would be about **$4.25 trillion** (7.8% of GDP) before the employer contribution and about **$3.17 trillion** (5.9% of GDP) with it. Health's net cost is nearly all of it: the plan-wide balance cannot be read until the settlement books health's financing |

GDP is the budget model's ($54,167 billion in FY2040; `recovery-budget-paths.csv`). The plan-wide figures are this section's arithmetic: $75.9 billion, less legacy health's $569 billion, plus the design's $4,743 billion (and less $1,075 billion for the contribution), before interest.

**Why the two columns differ.** The booked rows are the legacy public-option design, which the decisions replaced. The difference is not a gap in measurement: the plan moves about $3.1 trillion a year (2032) of premiums from households and employers onto the federal budget, and the settlement replaces them with taxes (memo 1; `3-design.md`). Both figures are on the same basis of measure (net federal cost, outlays less revenue gained), but the model's nets the exclusion revenue into one figure. Reported apart, as above, the spending and revenue lines are never added to each other.

**Proposed booking, for the lead** (adopted inputs, `models/data/inputs/`, tier 3; this dossier does not change them):
1. Retire HLT-3 (public option) and HLT-5 (commercial price cap): memo 1 A and memo 5 D were not chosen.
2. Rebook HLT-1 as restoration in FY2030, about $86 billion, with HLT-1.03's provider-tax range noted, and HLT-2 as the FY2031-34 upgrades (about $0.30 trillion) plus the disability wait (about $0.08 trillion).
3. Rebook HLT-6 at MedPAC's lower estimate through FY2034 (about −$0.55 trillion), ending at the endpoint.
4. Add HLT-7 as two rows: a spending row (the plan, net of replaced federal money and state payments, on part 1's path: about $5.80 trillion in FY2040) and a revenue row for the end of the tax exclusion (about $1.06 trillion in FY2040), so the exclusion is booked on the revenue side, where it falls. The employer contribution is a third, revenue row, booked only once the settlement sets its share; until then it is reported here.
5. HLT-4 (Medicaid, long-term care) stays as booked until part B decides long-term care.
6. Add HLT-8 (USDA grants) and, if Espen approves it, the transition fund in HLT-7.

## 6. Sensitivities

Each line changes one working assumption on the decided path (project arithmetic):

| Case | Net federal, 2032 full scale ($B) | FY2030-39 ($T) | FY2040 ($B) |
| --- | --- | --- | --- |
| As decided | 3,052 | 25.68 | 4,743 |
| Hospital and plan target 1.05 x Medicare | 2,538 | 21.93 | 3,944 |
| Target 1.25 x Medicare | 3,567 | 29.44 | 5,543 |
| States pay nothing (as S. 1506) | 3,359 | 28.23 | 5,220 |
| States pay 80% | 2,868 | 24.15 | 4,457 |
| Copays 1% of claims | 3,178 | 26.68 | 4,939 |
| Copays 6% of claims | 2,864 | 24.18 | 4,450 |
| Administration 3% / 8% | 2,916 / 3,268 | 24.60 / 27.40 | 4,531 / 5,079 |
| Medicaid's current rates 0.60 / 0.85 x Medicare | 3,477 / 2,727 | 29.02 / 23.12 | 5,403 / 4,238 |
| Commercial hospital prices 2.0 / 2.8 x Medicare | 3,351 / 2,939 | 27.93 / 24.83 | 5,207 / 4,567 |

The payment rate dominates, as memo 5 said: each 0.1 of the target moves FY2040 by about $0.8 trillion. Medicaid's starting rates come next, because wave 2 raises them to the plan's.

## 7. Commitment, assumption or open question

- **Commitments (decided):** who is covered and when (HLT-7.01, 7.03); the benefit and the 200% copay line (HLT-7.05, 7.06); the rate basis and its glide (HLT-7.10); the five protections; the fund's streams, including the exclusion revenue counted only on premiums that become wages (HLT-7.22).
- **Working assumptions** (basis and range above): the 1.15 target; copays at 3% of claims and a $1,000 cap; the states' half share; the employer contribution at 65%; a third of each wave-2 group a year; children at 20% of Medicaid spending; administration at 5%; growth on CBO's net-subsidy path; the costs of worker help, the disability wait and the upgrades. The cost of being wrong is mostly in the target rate and Medicaid's starting rates (part 6).
- **Open questions:** covering people without status (the immigration flagship); IHS funding; TRICARE's purchased care; separate capital funding and a bar on profit (section 4).
- **Study in implementation:** hospital-level effects from cost reports (before the fund's formula is set, 2032); whether copays damp specialist use as memo 4 expects (wave 1's data); take-up of the plan by people the records miss.
- **Simplifications in the path** (`health_path.py`): each move counts for the whole fiscal year; people restored to Medicaid in 2030 are counted with the newly covered from 2031; the glide applies to hospital claims as a share of non-drug claims; groups are grown on one growth path. None changes a decision.

## 8. Fit with the fairness test (D3)

At full scale households stop paying about $1.53 trillion a year in premiums and out-of-pocket costs (2032), keeping only the plan's copays above 200% of poverty. Employers stop paying $1.55 trillion of premiums and pay the contribution meanwhile. Whether households below the top come out ahead depends on the taxes the settlement chooses to replace those payments (D3); section 7 reports household cost by income from the coverage model before the new taxes.

## Open questions

1. **For Espen:** the hospital transition fund (part 3, option A; HLT-7.15). Yes or no.
2. **For the lead (booking, tier 3):** part 5's proposed rows.
3. **For the settlement:** the employer contribution's share and the date the payroll contribution replaces it; the states' share; the new revenue of about $2.4 trillion (2032 full scale) to $3.7 trillion (FY2040).
