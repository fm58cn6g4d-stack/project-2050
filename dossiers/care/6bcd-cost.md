# Care you can count on, parts B-D (long-term care, child care and pre-K, the care workforce): cost

Role: section 6 of the care dossier for parts B, C and D. It prices the provisions of `4bcd-specification.md` on federal fiscal years and reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`). Status: draft (stage D, board row D-9, PR 1), on `DEC-2026-11-11-02` to `-06`. Every figure is project arithmetic, not an official score. **Nothing is booked here**: the booking follows the milestone review, and part 5 lists exactly which ledger rows and inputs it would change.

## Counting rules

- **Conventions.** Federal cost, nominal $ billion unless marked, against current law (the 2029 baseline of sections 1b, 1c and 1d), a cost positive. Health's booking keeps Medicaid's long-term care in Medicaid at current-law cost (board row D-4c; `6-cost.md`, part 1), so these figures are also the increment over health's booking.
- **The basis.** The decided pieces are memo 17's (`memos/17-cost-options.md`; `tools/care_repricing.py`), as Espen decided them: the three-activity line with the hold-harmless, workforce lines at the federal cost only, the recommended state shares, options 2, 4 and 5, and the state option below the line (`DEC-2026-11-11-06`). Those figures are in calendar years (child care in school years). This section lays each piece on a year-by-year path and converts it.
- **Fiscal years.** FY y runs from October of y-1. A calendar-year line counts a quarter of the year before and three quarters of its own, as health's path does (`tools/health_path.py`); a January 1, 2035 start counts nine months in FY2035. Medicaid's match changes (the bridge) are fiscal-year amounts already. A school or program year starting in the fall of y is counted in FY y+1, since it runs almost exactly from October to September. This is the basis the budget model books, so it is the one reported (health's review, F-2).
- **The path.** `tools/care_bcd_path.py` (run: `python3 dossiers/care/tools/care_bcd_path.py`; it imports `care_repricing.py`, so the two cannot drift). Each line's shape and its anchors are in the script's comments; judgment is labeled there.
- **Each figure's status** (commitment, working assumption, open question) is in part 7.

## 1. The decided parts on fiscal years

**Yearly path, central ($ billion, federal):**

| FY | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Part B, long-term care | 24 | 25 | 27 | 28 | 30 | 186 | 303 | 367 | 396 | 416 | **1,801** | **437** |
| Part C, child care and pre-K | 0 | 35 | 80 | 116 | 140 | 146 | 148 | 154 | 161 | 169 | **1,149** | **176** |
| Part D, the workforce | 10 | 18 | 22 | 32 | 40 | 72 | 89 | 100 | 104 | 109 | **595** | **114** |
| **All three** | **34** | **78** | **128** | **176** | **210** | **403** | **540** | **620** | **661** | **693** | **3,544** | **727** |

**By line, FY2030-39 and FY2040 ($ billion):**

| Line | Provision | FY2030-39 | FY2040 | Shape |
| --- | --- | --- | --- | --- |
| The bridge, up to 10 points | HLT-4.01 | 134 | 0 | About $24 billion in FY2030, growing with home care, to FY2034 |
| The benefit (memo 6 B): states' relief net of their payment, richer budgets, new users | HLT-9.01-9.06 | 1,579 | 386 | About $300 billion in calendar 2035, growing 5.5% a year |
| People below the line after 2034 (not served by the plan) | HLT-9.02 | −39 | −23 | Ramps to about 6% of the Medicaid home care line by 2040 |
| The state option below the line, at the regular match | HLT-4.08 | 24 | 14 | 60% of the line above |
| Option 2, tiers one to four 10% lower | HLT-9.03 | −84 | −21 | 7% of richer budgets and new users |
| Option 4, new users phased over 2035-36 | HLT-9.07 | −140 | 0 | Half the new-user line in 2035, a fifth in 2036 |
| Institutional care, the care part (memo 8 C) | HLT-9.08 | 369 | 90 | About $70 billion in calendar 2035 (range $50-90 billion) |
| Option 5, residents contribute up to 20% | HLT-9.08 | −42 | −10 | About $8 billion in 2035 |
| **Part B** | | **1,801** | **437** | |
| Child care (memo 10 B) at 90% | FAM-2.01 | 699 | 110 | $20 billion in 2030-31, $85 billion in 2033-34, $110 billion in 2039-40 |
| Child care at 80% from 2033-34 | FAM-2.08 | −69 | −14 | About $10 billion from the fourth year, growing |
| Pre-K (memo 11 A), 90% then 75% | FAM-2.02 | 493 | 80 | $10 billion in 2030-31 to $60 billion in 2033-34 and $80 billion in 2039-40 |
| Facilities fund | FAM-2.05 | 25 | 0 | $5 billion a year, five school years |
| **Part C** | | **1,149** | **176** | |
| The floor in Medicaid, 2030-34, at the bridge rate | HLT-10.01 | 65 | 0 | 12% of payroll on Medicaid home care, 68% federal |
| The floor in the plan's rates, from 2035 | HLT-10.01 | 220 | 54 | About $42 billion in calendar 2035 |
| Early educators' floor and scale to parity | FAM-2G.01 | 254 | 51 | About $25 billion in 2033-34 at 90%; parity in 2036-37; 80% from 2033-34 |
| Nursing home staffing | HLT-11 | 36 | 7 | $1-2 billion a year in 2031-34; $5-7 billion from 2035 |
| Training and health supply | HLT-10.06, 10.07 | 20 | 2 | About $2 billion a year |
| **Part D** | | **595** | **114** | |

**From the decided figures to the fiscal-year figures.** Memo 17 gives about $3.80 trillion over 2030-39 and $736 billion in 2040, on calendar and school years. Two steps take it to this section's $3.54 trillion and $727 billion:

| Step | 2030-39 ($ trillion) | 2040 ($ billion) |
| --- | --- | --- |
| Memo 17, as decided (calendar and school years): B 1.90, C 1.32, D 0.58 | 3.80 | 736 |
| Rebuilt year by year from the same pieces | 3.89 | — |
| *of which:* memo 15's path, rebuilt from its own anchors (about $25 billion in 2033 and parity by 2036-37), sums to about $0.33 trillion over school years 2030-39, not the $0.22 trillion memo 15 and 3d give (a correction, below) | +0.08 | — |
| *of which:* part B, rounding | +0.01 | — |
| On fiscal years: a quarter of calendar 2039 moves past FY2039 for the benefit and the floor; school year 2039-40 (child care, pre-K and parity) is FY2040 | −0.35 | −9 |
| **This section, fiscal years** | **3.54** | **727** |

- **The fiscal-year total is lower in the window** because costs grow fastest at its end, and child care's first school year (2030-31) is FY2031. It is a timing change, not a saving: FY2040 is about the same ($727 billion against $736 billion; the gap is the same timing on a smaller scale).
- **The correction to memo 15's cost.** Memo 15 B reaches the same end point as option A (parity, about $53 billion in FY2040 at the child care share) four years later. Its stated total, $0.22 trillion, would need the scale to stay near the floor until about 2035. Laid on the memo's own dates, with the scale rising in equal steps from about $25 billion in 2033-34 to parity in 2036-37, the cost is about $0.25 trillion on fiscal years ($0.33 trillion on school years 2030-39). The decision is unchanged (Espen kept parity at 2036, `DEC-2026-11-11-06`); the figure is reported, not trimmed (`DEC-2026-11-10-05`). Part D's FY2030-39 cost here, $0.595 trillion, uses the corrected path. Memo 17's option 3 (parity by 2038) would have saved somewhat more than its stated $0.04 trillion on this path.

## 2. What the decided total leaves out

| Item | Provision | FY2030-39 | FY2040 | Basis | Firm or contingent |
| --- | --- | --- | --- | --- | --- |
| Money Follows the Person, the resource limits, no estate recovery, the CAPABLE demonstration | HLT-4.02, 4.03, 4.04, 4.07 | about $26 billion | under $1 billion | Points 2-4 and 6: $0.45 billion, $2-6 billion and under $0.5 billion a year; the demonstration small (judgment) | Firm |
| Child care's labor grown with wages, not prices (3d's finding) | FAM-2.01, 2.04 | about $20 billion | about $6 billion | Two-thirds of child care cost is labor; care wages about 1% a year above prices (judgment) | Firm if wages grow so |
| The floor on new users' hours delayed by option 4 | HLT-10.01 | about −$10 billion | 0 | Memo 17 took option 4's saving off part B but not off the floor on the same hours | Firm |
| **With these, all three** | | **about $3.58 trillion** | **about $733 billion** | | |
| Respite and training in the bridge | HLT-4.06 | inside the bridge | — | "A few billion a year inside point 1's match" (memo 9) | — |
| The hold-harmless | HLT-9.02 | inside the benefit | inside | About $0.18 trillion over 2035-39 and $24 billion in FY2040, already counted (3b) | — |
| Rural home care add-on | `5bcd-delivery.md`, part 6 | not priced | not priced | A working choice inside tier budgets | Inside the range |
| Mothers' added earnings and taxes; lower turnover; less public assistance; quality | — | not counted | not counted | CBO's conventional scores leave them out; Quebec's evidence puts child care's long-run fiscal recapture at 75-117% of cost [EV-CAR-534], Norway's much less [EV-CAR-544] | Not counted |
| Head Start's own grant | FAM-2.07 | outside | outside | About $12.4 billion, by appropriation [EV-CAR-504] | Current law |
| The residency slots | HLT-10.07 | outside | outside | Already in HLT-4's booked safety-net component; not counted again | Booked |

**All-in, FY2030-39:** about **$3.58 trillion** over FY2030-39 and **$733 billion** in FY2040 (range about $2.0-6.2 trillion and $390-1,360 billion, part 6). It is not a score.

**Who pays now.** Most of the long-term care and child care cost replaces what families pay out of pocket or give unpaid [EV-CAR-401] [EV-CAR-436] [EV-CAR-514]. CBO counts about two-fifths of a broad long-term care benefit's federal cost as replacing state and out-of-pocket spending [EV-CAR-452]. It is a shift to public money as well as new care.

## 3. Federal and state shares

What states pay toward parts B-D, beside the federal cost (central; `care_bcd_path.py` and `care_repricing.py`):

| Part | States pay | Federal pays | Basis |
| --- | --- | --- | --- |
| Long-term care, from 2035 | About $115 billion in 2035, of which about $42 billion institutional; about $150 billion in FY2040, indexed | The rest of the benefit and the care part, net of that payment (part 1) | 50% of current long-term care spending (HLT-9.09) |
| The bridge's floor, 2030-34 | About $31 billion in all | About $65 billion | Each state's bridge rate, about 68% federal (HLT-10.01) |
| The bridge's match points | States keep their own spending (the entry condition) | About $134 billion | HLT-4.01 |
| Child care | About $10 billion a year for the first three years, then about $20 billion at maturity | About $74 billion at maturity (2033), $97 billion in FY2040 | 90%, then 80% (FAM-2.08) |
| Pre-K | About $34 billion at maturity, their current $14.4 billion included [EV-CAR-519] | About $57 billion at maturity, $80 billion in FY2040 | 90%, then 75% (FAM-2.08) |
| Early educators' pay | A fifth of the scale's cost from 2033-34 | Part 1's line | Child care's share (FAM-2G.01) |
| Families | Room and board from income in nursing homes, up to 20% of the care part from income left after it; child care copays above 85% of state median income, at most 7% of income; capped plan copays above 200% of poverty | — | HLT-9.08, FAM-2.01, HLT-7.06 |

- **Medicaid money that moves in is not new.** About $165 billion of federal Medicaid home care money in 2035 moves into the plan as a transfer (3b), as health counts the Medicaid money it replaces; only the net is counted above.
- **States' payments are offsetting receipts** in a booking, as health's are (health's review, F-4 item 4). Part 1's figures are already net of them; a booking enters either the net or the gross with the receipts, not both.
- **If the states' obligation fails** in court, part 6 gives the federal cost.

## 4. Fit with the legacy rows and the down payment

- **HLT-4's legacy down payment.** HLT-4 is booked at $0.498 trillion over FY2030-39, of which **$0.319 trillion is "HCBS down payment and care workforce"** (`models/data/inputs/fiscal-components.csv`, line 34), about $44 billion in FY2040 on the legacy profile. The bridge ($134 billion) and the bridge-period floor ($65 billion) are that down payment. A booking **retires the long-term care component and books parts B and D in its place**, so nothing is counted twice. The bridge and floor together, $199 billion, are less than the component over 2030-34; the component also runs on past 2034, which the decided design replaces with the benefit.
- **HLT-4's other parts stay.** The safety-net component (health centers, 14,000 residency slots, the Momnibus, Title X: $0.138 trillion) is untouched; HLT-10.07's slots are those slots, not new ones. Children's coverage and Medicaid dental already end with their waves.
- **FAM-2's legacy row.** FAM-2 is booked at $0.6 trillion over FY2030-39 ($94 billion in FY2040) on a six-year ramp (`ledger-bills.csv`, line 11). In the budget model's case `mixed`, FAM-2 is transferred into the adopted EDU-9B education fund, whose **care component** runs $12 billion in 2030, $88 billion in 2033 and $106 billion from 2036 (`models/tools/recovery-budget/assumptions.json`, `education_components.care`): about $786 billion over FY2030-39 and $106 billion in FY2040. Part C and memo 15 replace it: about $1,403 billion and $227 billion.
- **LAB-3's note** that a home care wage floor "adds an unscored Medicaid rate cost" (HLT-4's ledger note) is answered: HLT-10.01 prices it.

## 5. The fiscal-rule report

Each figure has one basis: federal fiscal years, $ billion, a cost positive, against what the budget model now books (`models/data/recovery-budget-paths.csv`, case `mixed`, read after `bash models/tools/run-all.sh` at commit `aa6b250`).

| Measure | FY2030-39 | FY2040 (permanent) |
| --- | --- | --- |
| Parts B-D, federal cost as decided (part 1) | $3,544 billion | $727 billion (1.3% of GDP) |
| With the items in part 2 | $3,581 billion | $733 billion |
| Already booked for the same purposes: HLT-4's long-term care component; the EDU-9B fund's care component | $319 billion; $786 billion | $44 billion; $106 billion |
| **Net change a booking would make** | **about $2,439 billion** | **about $577 billion (1.1% of GDP)** |
| *of which on the general fund:* long-term care and the workforce in home care and nursing homes, net of HLT-4's component | about $1,822 billion | about $456 billion |
| *of which:* child care, pre-K and early educators' pay, net of the fund's care component, on the general fund or the education fund as the settlement decides | about $617 billion | about $121 billion |

**Its share of the plan-wide margin.** The plan-wide general-fund primary balance in FY2040 is **$3,750 billion short** as booked (`agenda_gf_primary_bn`, case `mixed`, before interest; 6.9% of GDP; health's booking, `6-cost.md`, part 5). Booking parts B-D as decided would make it about **$4,206 billion short** with child care and pre-K left in the education fund, or about **$4,327 billion short** (8.0% of GDP) with them on the general fund. Parts B-D are about an eighth of the plan-wide gap, after health's $4,243 billion; GDP is the budget model's ($54,167 billion in FY2040). The gap is expected: health's and care's premium-and-out-of-pocket-to-tax shift is what the financing settlement designs. It is a figure to report, not an error to fix (`DEC-2026-11-10-05`), and no part of it goes to Espen on its own.

**The test years.** The decided costs are permanent: the benefit, the care part, child care and pre-K, the floor and parity all continue past FY2040 and grow with wages and the population over 85. Nothing in parts B-D ends after FY2040 except the facilities fund (FY2035) and the bridge (FY2034).

**What a booking would change** (tier 3, for the lead after the milestone review; the same pattern as health's `models/tools/health_booking.py` and `test_fiscal_health.py`):
1. `models/data/inputs/fiscal-components.csv`, line 34 (`HLT-4,ltc-hcbs-care-workforce,0.3194`): retire, and add a component for the bridge (HLT-4.01) on a year shape.
2. `models/data/inputs/ledger-bills.csv`, line 5 (HLT-4, 0.319 / 0.498 / 0.677): the midpoint and range change, since HLT-4's components must sum to its midpoint (`ASM-PROF-COMPONENTS`); the note's LAB-3 sentence goes.
3. `ledger-bills.csv`: new rows for HLT-9 (the benefit and the care part; rail FLOOR, regular order, from 2035), HLT-10 (the floor: an R1 part for 2030-34 and a regular-order part from 2035, as a `split` row in `models/data/budget/provision-splits.csv`) and HLT-11 (regular order); or the same as components of HLT-4 and HLT-7. Recommended: new rows, since each has its own vehicle and agenda home.
4. `models/data/inputs/fiscal-years.csv`: one year-shape row per new component, from `tools/care_bcd_path.py`'s fiscal-year lines; `models/data/inputs/fiscal-profiles.csv`: rows for the new bills, and line 11 (FAM-2's six-year GDP ramp) replaced by a year shape.
5. `ledger-bills.csv`, line 11 (FAM-2, 0.4 / 0.6 / 0.9, R2) to the decided path, with memo 15's parity either inside it or as a FAM-2G row; **and** `models/tools/recovery-budget/assumptions.json`, `education_components.care` (anchors 12, 88, 106, 106, 123, 143 for 2030, 2033, 2036, 2040, 2045, 2049) set to the same path, or FAM-2 taken out of `transferred_agenda` in `models/data/inputs/education-adoption.json`. Part C must be counted in one place; which one is the financing settlement's choice, since EDU-9B is a legacy decision now held as a working choice (`3c-design-child-care.md`, "Inherited assumptions").
6. `models/data/budget/provisions.csv`: rows 5-9 (HLT-4 and its components) and 18 (FAM-2), and new rows for HLT-9, HLT-10, HLT-11 and FAM-2G with their vehicles.
7. States' payments (HLT-9.09, FAM-2.08) as offsetting receipts, labeled as health's are; part 1 is net of them.
8. Incidence: `models/data/inputs/incidence-rows.csv` lines 27 (F2, key `childcare`) and 35 (H4, key `medicaid_ltc`), `incidence-phase-in.csv` lines 3 (F2's ramp) and 23 (H4's booked path), and a row for HLT-9 (key `medicaid_ltc` or a new one for a universal benefit, which reaches higher quintiles than Medicaid does).
9. `models/data/inputs/ledger-dynamic.csv`, DY6 (parents' added employment from FAM-2, $0.15-0.30 trillion), which scales with the program it follows; and `votes-bills.csv` lines 3 and 9, if the bills' sizes enter the vote model.
10. Not booked: the hold-harmless (inside HLT-9), the residency slots (in HLT-4's safety-net component), Head Start's grant (current law).

## 6. Sensitivities

| Case | FY2030-39 ($ trillion) | FY2040 ($ billion) | Note |
| --- | --- | --- | --- |
| As decided | 3.54 | 727 | Part 1 |
| Low (each piece's low) | 1.98 | 387 | Fewer new users, lower cost each, low take-up of child care |
| High (each piece's high) | 6.17 | 1,351 | Part B's new users at 5.6 million and $82,500 each; child care take-up high |
| Part B at Urban's best guess (about $560 billion in 2035 at three activities, against $300 billion) | about +1.3 | about +330 | The outside model that sits highest (3b) |
| The states' long-term care payment fails in court (hold harmless) | about +0.6 | about +150 | HLT-9.09; the payment ends and the federal government pays it |
| A third of states decline child care and pre-K and the obligation fails | about +0.1 | about +25 | Child care $87 billion rather than $74 billion at maturity; pre-K $64 billion rather than $57 billion (memo 17) |
| Two daily activities instead of three (not decided) | about +0.4 | about +130 | Memo 7 A; about $80 billion more in 2035 |
| No phase-in (option 4 not taken) | about +0.14 | 0 | Option 4's saving |

The largest uncertainty is still part B's count of new users and their cost (3b), then child care's under-3 take-up (3c). Both are working assumptions with wide ranges; the financing settlement should plan on the central figure and keep the top of the range visible.

## 7. Commitment, assumption or open question

| Input | Status | Basis and range |
| --- | --- | --- |
| The three-activity line, the hold-harmless, the tiers' structure, no asset test, the care part from 2035, the floor at $20, parity by 2036-37, the staffing numbers, the states' shares, the dates | Commitments (decided) | Section 4 |
| New users (about 3.9 million in 2035) and their cost (about $50,000) | Working assumption | 2.8-5.6 million; $31,000-83,000 (3b) |
| Growth of long-term care spending | Working assumption | 5.5% a year, 4.5-6.5% (3b) |
| Tier amounts; option 2's 10% | Working assumption until the national assessment study | Section 4, HLT-9.03 |
| Room-and-board share and the protected allowance | Working assumption | 30-40%; about double today's allowance (HLT-9.08) |
| Under-3 take-up and cost per child | Working assumption | 3.5-6.0 million; $18,000-28,000 (3c) |
| The floor's payroll lift | Working assumption | 8-18% at $20 (3d) |
| Memo 15's path | Working assumption | The memo's anchors; part 1's correction |
| Fiscal-year shapes | Convention | Part "Counting rules" |
| Where part C is booked (general fund or EDU-9B) | Open, the settlement's | Part 5, item 5 |
| Paid family care nationally | Study in implementation | The evaluation (HLT-4.06), then the decision point (HLT-9.05) |

## Open questions

- Where part C is booked (part 5, item 5): the settlement's.
- Nursing-home spending by payer and the room-and-board share, to firm up memo 8 C's $50-90 billion (3b, "Evidence still needed").
- An independent estimate of early educator parity's cost (3d, "Evidence still needed"), now that its path is corrected here.
