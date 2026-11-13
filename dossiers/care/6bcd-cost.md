# Care you can count on, parts B-D (long-term care, child care and pre-K, the care workforce): cost

Role: section 6 of the care dossier for parts B, C and D. It prices the provisions of `4bcd-specification.md` on federal fiscal years and reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`). Status: reviewed at L3 (parts B-D, `review-milestone-bcd.md`; see the README), on `DEC-2026-11-11-02` to `-06`, and booked (#265). Every figure is project arithmetic, not an official score; part 5 reports the booked rows.

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
| Part B, long-term care | 14 | 15 | 27 | 28 | 30 | 193 | 303 | 367 | 396 | 416 | **1,789** | **437** |
| Part C, child care and pre-K | 0 | 35 | 80 | 116 | 140 | 146 | 148 | 154 | 161 | 169 | **1,149** | **176** |
| Part D, the workforce | 10 | 18 | 22 | 32 | 40 | 72 | 90 | 100 | 105 | 111 | **600** | **116** |
| **All three** | **25** | **68** | **128** | **176** | **210** | **412** | **541** | **621** | **663** | **695** | **3,537** | **729** |

**By line, FY2030-39 and FY2040 ($ billion):**

| Line | Provision | FY2030-39 | FY2040 | Shape |
| --- | --- | --- | --- | --- |
| The bridge: 6 points from FY2030, up to 10 from FY2032 | HLT-4.01 | 122 | 0 | About $14 billion in FY2030 at 6 points; up to about $27-30 billion a year in FY2032-34; to December 31, 2034, so FY2035 takes a quarter |
| The benefit (memo 6 B): states' relief net of their payment, richer budgets, new users | HLT-9.01-9.06 | 1,579 | 386 | About $300 billion in calendar 2035, growing 5.5% a year |
| People below the line after 2034 (not served by the plan) | HLT-9.02 | −39 | −23 | Ramps to about 6% of the Medicaid home care line by 2040 |
| The state option below the line, at the regular match | HLT-4.08 | 24 | 14 | 60% of the line above |
| Option 2, tiers one to four 10% lower | HLT-9.03 | −84 | −21 | 7% of richer budgets and new users |
| Option 4, new users phased over 2035-36 | HLT-9.07 | −140 | 0 | Half the new-user line in 2035, a fifth in 2036 |
| Institutional care, the care part (memo 8 C) | HLT-9.08 | 369 | 90 | About $70 billion in calendar 2035 (range $50-90 billion) |
| Option 5, residents contribute up to 20% | HLT-9.08 | −42 | −10 | About $8 billion in 2035 |
| **Part B** | | **1,789** | **437** | |
| Child care (memo 10 B) at 90% | FAM-2.01 | 699 | 110 | $20 billion in 2030-31, $85 billion in 2033-34, $110 billion in 2039-40 |
| Child care at 80% from 2033-34 | FAM-2.08 | −69 | −14 | About $10 billion from the fourth year, growing |
| Pre-K (memo 11 A), 90% then 75% | FAM-2.02 | 493 | 80 | $10 billion in 2030-31 to $60 billion in 2033-34 and $80 billion in 2039-40 |
| Facilities fund | FAM-2.05 | 25 | 0 | $5 billion a year, five school years |
| **Part C** | | **1,149** | **176** | |
| The floor in Medicaid, 2030-34, at the bridge rate | HLT-10.01 | 65 | 0 | 12% of payroll on Medicaid home care, 68% federal |
| The floor in the plan's rates, from 2035 | HLT-10.01 | 220 | 54 | About $42 billion in calendar 2035 |
| Early educators' floor and scale to parity | FAM-2G.01 | 259 | 53 | About $25 billion in 2033-34 at 90%; parity in 2036-37; 80% from 2033-34 |
| Nursing home staffing | HLT-11 | 36 | 7 | $1-2 billion a year in 2031-34; $5-7 billion from 2035 |
| Training and health supply | HLT-10.06, 10.07 | 20 | 2 | About $2 billion a year |
| **Part D** | | **600** | **116** | |

**From the decided figures to the fiscal-year figures.** Memo 17 gives about $3.80 trillion over 2030-39 and $736 billion in 2040, on calendar and school years. Two steps take it to this section's $3.54 trillion and $729 billion:

| Step | 2030-39 ($ trillion) | 2040 ($ billion) |
| --- | --- | --- |
| Memo 17, as decided (calendar and school years): B 1.90, C 1.32, D 0.58 | 3.80 | 736 |
| Rebuilt year by year from the same pieces | 3.89 | — |
| *of which:* memo 15's path, rebuilt from its own anchors (about $25 billion in 2033 and parity by 2036-37), sums to about $0.31 trillion over school years 2030-39, not the $0.22 trillion memo 15 and 3d give (a correction, below) | +0.09 | — |
| *of which:* the bridge's progress points start in FY2032, as HLT-4.01 says, not FY2030 as memo 17 priced them; the bridge runs to December 31, 2034 | −0.01 | — |
| On fiscal years: a quarter of calendar 2039 moves past FY2039 for the benefit and the floor; school year 2039-40 (child care, pre-K and parity) is FY2040 | −0.35 | −7 |
| **This section, fiscal years** | **3.54** | **729** |

- **The fiscal-year total is lower in the window** because costs grow fastest at its end, and child care's first school year (2030-31) is FY2031. It is a timing change, not a saving: FY2040 is about the same ($729 billion against $736 billion; the gap is the same timing on a smaller scale).
- **The correction to memo 15's cost.** Memo 15 B reaches the same end point as option A (parity, about $53 billion in FY2040 at the child care share) four years later. Its stated total, $0.22 trillion, would need the scale to stay near the floor until about 2035. Laid on the memo's own dates, with the scale rising in equal steps from about $25 billion in 2033-34 to parity in 2036-37, the cost is about $0.26 trillion on fiscal years ($0.31 trillion on school years 2030-39; $0.34 trillion at 90%). The decision is unchanged (Espen kept parity at 2036, `DEC-2026-11-11-06`); the figure is reported, not trimmed (`DEC-2026-11-10-05`). Part D's FY2030-39 cost here, $0.60 trillion, uses the corrected path. Parity's FY2040 end point is program year 2039-40, as child care's and pre-K's are, so it is about $53 billion, as memo 15 gives. Memo 17's option 3 (parity by 2038) would have saved somewhat more than its stated $0.04 trillion on this path.

## 2. What the decided total leaves out

| Item | Provision | FY2030-39 | FY2040 | Basis | Firm or contingent |
| --- | --- | --- | --- | --- | --- |
| Money Follows the Person, the resource limits, no estate recovery, the CAPABLE demonstration | HLT-4.02, 4.03, 4.04, 4.07 | about $26 billion | under $1 billion | Points 2-4 and 6: $0.45 billion, $2-6 billion and under $0.5 billion a year; the demonstration small (judgment) | Firm |
| Child care's labor grown with wages, not prices (3d's finding) | FAM-2.01, 2.04 | about $20 billion | about $6 billion | Two-thirds of child care cost is labor; care wages about 1% a year above prices (judgment) | Firm if wages grow so |
| The floor on new users' hours delayed by option 4 | HLT-10.01 | about −$10 billion | 0 | Memo 17 took option 4's saving off part B but not off the floor on the same hours | Firm |
| Room and board from 2035 without an asset test (the milestone review's B-1) | HLT-4.08, 9.08 | about $14 billion | about $3.5 billion | Memo 8 C as decided: Medicaid's room-and-board help income-tested only. A few hundred thousand long-stay residents with savings above $10,000 and income below room and board; $3-6 billion a year in all in 2035, about 60% federal (judgment; range $1.8-3.6 billion federal in 2035) | Firm |
| CCDF kept for school-age children (M-2) | FAM-2.04 | about $48 billion | about $6 billion | Part C netted all of today's CCDF into the under-5 guarantee; only its under-5 share moves now. In ACF's FY2023 data, 34% of the children CCDF serves are 6 to under 13 and 10% are 5 to under 6 [EV-CAR-700]; school-age care costs less a child, so the working share of spending is 35% (range 30-44%) of about $12.4 billion, at the FY2029 level indexed to prices (`care_bcd_path.py`, `CCDF_SCHOOL_AGE_SHARE`) | Firm |
| The territories (M-1): child care and pre-K; long-term care from 2035; the bridge and floor outside the capped allotments in 2030-34 | FAM-2.07, HLT-9.01, HLT-4.01, HLT-10.01 | about $29 billion ($8, $19 and $2 billion) | about $6 billion | About 3.5 million people [EV-CAR-356] [EV-CAR-357], with about 92,431 children under 5 in Puerto Rico [EV-CAR-701], not in the part files' national figures; CCDF already reserves up to half of 1% for the four smaller territories and treats Puerto Rico as a state [EV-CAR-702]: 0.5-1.0% of part C's path, 0.5-1.5% of the benefit and the care part, and $0.2-1.0 billion a year for the bridge and floor (judgment) | Firm |
| The status rule (part 2b): new users with no status not covered | HLT-9.01, 9.08, HLT-10.01 | about −$3.6 billion | about −$0.9 billion | `DEC-2026-11-13-01`; `tools/status_rule.py` | Firm |
| **With these, all three** | | **about $3.66 trillion** | **about $750 billion** | | |
| Respite and training in the bridge | HLT-4.06 | inside the bridge | — | "A few billion a year inside point 1's match" (memo 9) | — |
| The hold-harmless | HLT-9.02 | inside the benefit | inside | About $0.18 trillion over 2035-39 and $24 billion in FY2040, already counted (3b) | — |
| Rural home care add-on | `5bcd-delivery.md`, part 6 | not priced | not priced | A working choice inside tier budgets | Inside the range |
| Mothers' added earnings and taxes; lower turnover; less public assistance; quality | — | not counted | not counted | CBO's conventional scores leave them out; Quebec's evidence puts child care's long-run fiscal recapture at 75-117% of cost [EV-CAR-534], Norway's much less [EV-CAR-544] | Not counted |
| Head Start's own grant | FAM-2.07 | outside | outside | About $12.4 billion, by appropriation [EV-CAR-504] | Current law |
| The dependent care credit and exclusion fall | Point 4 (current law kept) | not counted | not counted | Lower net cost: when care is free at or below 85% of state median income and capped at 7% above it, families' claimable expenses fall, and so does the cost of the 2025 law's credit and $7,500 exclusion [EV-CAR-500] [EV-CAR-501] [EV-CAR-502]; probably several billion a year (judgment). The secure floor's refundability choice should be priced on the post-guarantee base | Not counted |
| The floor in mixed-payer providers, 2030-34 | HLT-10.01 | not counted | — | A provider cannot pay the same aide $20 for Medicaid clients and less for others, so in practice the floor lifts the whole payroll, and private payers and Medicare bear the rest through prices until 2035. Not a federal cost under `DEC-2026-11-11-05`, except Medicare's share of skilled nursing and home health, which is not counted (working assumption) | Not counted |
| The residency slots | HLT-10.07 | outside | outside | Already in HLT-4's booked safety-net component; not counted again | Booked |

**All-in:** about **$3.66 trillion** over FY2030-39 and **$750 billion** in FY2040 (range about $2.1-6.3 trillion and $400-1,390 billion, part 6). It is not a score. Part 5's booked-basis figures and the margin run use the decided pieces; the items above add about $22 billion in FY2040 to a booking (about $9 billion to the general-fund gap (room and board $3.5 billion, the territories' long-term care $4.8 billion, the small part B items $0.3 billion), and the rest with part C, wherever it is booked).

**Who pays now.** Most of the long-term care and child care cost replaces what families pay out of pocket or give unpaid [EV-CAR-401] [EV-CAR-436] [EV-CAR-514]. CBO counts about two-fifths of a broad long-term care benefit's federal cost as replacing state and out-of-pocket spending [EV-CAR-452]. It is a shift to public money as well as new care.

## 2b. The status rule for long-term care

Espen decided that long-term care narrows with the health plan (November 13, `DEC-2026-11-13-01`: "no, long-term care narrows too"). From January 1, 2035 the home and community care benefit and the care part of institutional care cover people with lawful or registered status, a filing receipt included (HLT-9.01 follows HLT-7.01; IMM-1.23), not every resident. People with no status keep emergency care as today. `tools/status_rule.py` prices it, and `care_bcd_path.py` carries it as three lines:

| Line | FY2030-39 | FY2040 | Booked on |
| --- | --- | --- | --- |
| The benefit's new users with no status (memo 6 B's new-user line, net of options 2 and 4) | −$2.9 billion | −$0.8 billion | HLT-9, `status-rule` |
| The care part of institutional care, net of option 5, for residents with no status | −$0.4 billion | −$0.1 billion | HLT-9, `status-rule` |
| The care floor on those new users' hours | −$0.2 billion | −$0.1 billion | HLT-10 |
| **The status rule, long-term care** | **−$3.6 billion** (range −$5.7 to −$1.2 billion) | **−$0.9 billion** (range −$1.5 to −$0.3 billion) | |

- **Who it reaches.** Only new users. The states' relief, the richer budgets and the hold-harmless reach people already on Medicaid home care, and Medicaid has paid for people with no status only in emergencies since 1996 [EV-CAR-008]. People with no status in each year come from the immigration model: eligible people who have not filed, about 4.9 million in FY2035 and 4.0 million from FY2039 (all of them, since long-term care has no residual like health's).
- **The basis** (working assumption, with its range): their share of the population times their relative need. Need is low because they are young: about 1% of unauthorized immigrants are 65 or older, against about 13-18% of everyone [EV-CAR-705] [EV-CAR-706], and about two-thirds of the benefit's new users are older people (judgment). Relative need is taken as 0.3 for the home benefit (range 0.15-0.45) and 0.1 for nursing homes (0.05-0.2). That puts about 13,000-16,000 of the benefit's roughly 3.9 million new users outside it.
- **The cost of being wrong is small.** Even at twice the high reading, the line stays under $2 billion a year: little turns on it.
- **What is not counted.** People who arrive without status after the act is signed (they would add a little). People with no status who need long-term care fall back on families, emergency care and state-only programs, as now.

## 3. Federal and state shares

What states pay toward parts B-D, beside the federal cost (central; `care_bcd_path.py` and `care_repricing.py`):

| Part | States pay | Federal pays | Basis |
| --- | --- | --- | --- |
| Long-term care, from 2035 | About $115 billion in 2035, of which about $42 billion institutional; about $150 billion in FY2040, indexed | The rest of the benefit and the care part, net of that payment (part 1) | 50% of current long-term care spending (HLT-9.09) |
| The bridge's floor, 2030-34 | About $31 billion in all | About $65 billion | Each state's bridge rate, about 68% federal (HLT-10.01) |
| The bridge's match points | States keep their own spending (the entry condition) | About $122 billion | HLT-4.01 |
| Child care | About $10 billion a year for the first three years, then about $20 billion at maturity | About $74 billion at maturity (2033), $97 billion in FY2040 | 90%, then 80% (FAM-2.08) |
| Pre-K | About $34 billion at maturity, their current $14.4 billion included [EV-CAR-519] | About $57 billion at maturity, $80 billion in FY2040 | 90%, then 75%, of the cost above states' current spending, which states keep paying (FAM-2.08); about 63% federal of the whole. States that already fund pre-K (Oklahoma, Georgia, New York among them) pay their current spending plus a quarter of the rest, so early adopters carry more of the same program than late ones (the review's A-2; decided, not argued here) |
| Early educators' pay | A fifth of the scale's cost from 2033-34 | Part 1's line | Child care's share (FAM-2G.01) |
| Families | Room and board from income in nursing homes, up to 20% of the care part from income left after it; child care copays above 85% of state median income, at most 7% of income; capped plan copays above 200% of poverty | — | HLT-9.08, FAM-2.01, HLT-7.06 |

- **Medicaid money that moves in is not new.** About $165 billion of federal Medicaid home care money in 2035 moves into the plan as a transfer (3b), as health counts the Medicaid money it replaces; only the net is counted above.
- **States' payments are offsetting receipts** in a booking, as health's are (health's review, F-4 item 4). Part 1's figures are already net of them; a booking enters either the net or the gross with the receipts, not both.
- **If the states' obligation fails** in court, part 6 gives the federal cost.

## 4. Fit with the legacy rows and the down payment

- **HLT-4's legacy down payment.** HLT-4 is booked at $0.498 trillion over FY2030-39, of which **$0.319 trillion is "HCBS down payment and care workforce"** (`models/data/inputs/fiscal-components.csv`, line 34), about $44 billion in FY2040 on the legacy profile. The bridge ($122 billion) and the bridge-period floor ($65 billion) are that down payment. A booking **retires the long-term care component and books parts B and D in its place**, so nothing is counted twice. The bridge and floor together, $187 billion, are less than the component over 2030-34; the component also runs on past 2034, which the decided design replaces with the benefit.
- **HLT-4's other parts stay.** The safety-net component (health centers, 14,000 residency slots, the Momnibus, Title X: $0.138 trillion) is untouched; HLT-10.07's slots are those slots, not new ones. Children's coverage and Medicaid dental already end with their waves.
- **FAM-2's legacy row.** FAM-2 is booked at $0.6 trillion over FY2030-39 ($94 billion in FY2040) on a six-year ramp (`ledger-bills.csv`, line 11). In the budget model's case `mixed`, FAM-2 is transferred into the adopted EDU-9B education fund, whose **care component** runs $12 billion in 2030, $88 billion in 2033 and $106 billion from 2036 (`models/tools/recovery-budget/assumptions.json`, `education_components.care`): about $786 billion over FY2030-39 and $106 billion in FY2040. Part C and memo 15 replace it: about $1,407 billion and $230 billion.
- **LAB-3's note** that a home care wage floor "adds an unscored Medicaid rate cost" (HLT-4's ledger note) is answered: HLT-10.01 prices it.

## 5. The fiscal-rule report

Under `DEC-2026-11-10-05`, parts B-D report their effect and pass it to the settlement. The budget model books the decided design (`models/tools/care_booking.py`; #265, with the status rule for long-term care in #313), so this part reports the booked rows. Each figure is the fiscal model's generated row path (`models/tools/fiscal-model.py`, the `rows` of its JSON output and the components in `models/data/inputs/fiscal-components.csv`): federal fiscal years, general fund, a cost positive; the plan-wide balance is `models/data/recovery-budget-paths.csv` (case `mixed`).

| Row | What it books | FY2030-39 ($ trillion) | FY2040 ($ billion) |
| --- | --- | --- | --- |
| HLT-4, care's parts | The bridge (HLT-4.01), the care wage floor in Medicaid in 2030-34, training and supply money (HLT-10.06, 10.07), the small items (HLT-4.02 to 4.04, 4.07) and the territories' bridge and floor. They replace HLT-4's legacy long-term care component ("HCBS down payment and care workforce", 0.3194). Health's parts of the row are in `6-cost.md`, part 5; the whole row is 0.414 and 21.1 | 0.235 | 2.3 |
| HLT-9 | Long-term care, regular order from 2035 (rail FLOOR): the home and community care benefit and the care part of institutional care gross, the states' payment as an offsetting receipt, the state option below the line, room and board, the territories, and the status rule (`DEC-2026-11-13-01`) | 1.697 | **444.1** |
| | of which the home and community care benefit (HLT-9.01 to 9.07) | 1.702 | 437.4 |
| | of which the care part of institutional care (HLT-9.08) | 0.546 | 133.6 |
| | of which the states' payment (HLT-9.09, an offsetting receipt) | −0.605 | −148.1 |
| | of which the state option below the line | 0.024 | 13.8 |
| | of which room and board help | 0.014 | 3.5 |
| | of which the territories | 0.019 | 4.8 |
| | of which the status rule (part 2b) | −0.003 | −0.8 |
| HLT-10 | The care wage floor in the plan's rates from 2035, net of option 4's delay and of the new users with no status | 0.210 | **53.9** |
| HLT-11 | The nursing home staffing standard | 0.036 | **6.9** |
| FAM-2 | Child care and pre-K with early educators' pay (FAM-2G), reconciliation (R2): in case `mixed` the EDU-9B fund carries it | 1.484 | **242.8** |
| | of which child care (FAM-2.01, 2.08) | 0.651 | 102.3 |
| | of which pre-K (FAM-2.02) | 0.493 | 80.0 |
| | of which early educators' pay (FAM-2G.01) | 0.259 | 53.3 |
| | of which CCDF kept for school-age children (FAM-2.04) | 0.048 | 6.0 |
| | of which the facilities fund (FAM-2.05, FY2030-34) | 0.025 | 0 |
| | of which the territories | 0.008 | 1.2 |
| **Parts B-D, as booked** (the rows above) | | **3.662** | **750.0** |

A row's components can differ from its total by 0.1 in the last place, from rounding. The booked total is $3,662 billion over FY2030-39 and $750 billion in FY2040, and `test_fiscal_care.py` checks both against the dossier's path (part 1's decided pieces are $3,537 billion and $729 billion; the booked rows add part 2's items and the status rule).

| Measure, FY2040 | As booked |
| --- | --- |
| Parts B-D, federal cost (the rows above) | **$750.0 billion** (1.4% of GDP) |
| Plan-wide general-fund primary balance (`agenda_gf_primary_bn`, case `mixed`, before interest; every booked flagship) | **$4,240.4 billion short** (7.83% of GDP) |
| The EDU-9B fund's general-fund grant (the whole fund, FAM-2's care component included) | $139.2 billion |

**Where part C is counted.** Part C is counted once. In case `mixed` the EDU-9B fund's care component is FAM-2's booked path (`models/tools/recovery-budget/assumptions.json`, `education_components.care`, `ledger_row` FAM-2), and the general fund pays the fund a grant of 30% of the fund's outlays after 2034 (`models/tools/recovery-budget/model.py`, `edu_fund`; `gf_share_mixed`). So the general fund bears about 30 cents of each part C dollar after 2034, and the rest falls on the fund's payroll receipts and reserve: its solvency is the settlement's to cover with the fund's rate. Counting part C on the general fund instead is the settlement's choice (`3c-design-child-care.md`, "Inherited assumptions"). That alternative has not been re-priced since the booking.

**Its share of the plan-wide margin.** The model reports the plan-wide gap only, not each flagship's part of it. Parts B-D's rows carry $750.0 billion of FY2040 outlays, of which FAM-2's $242.8 billion sits in the EDU-9B fund in case `mixed`, so their general-fund effect is below the rows' total. GDP is the budget model's ($54,167 billion in FY2040). The gap is expected: health's and care's shift from premiums and out-of-pocket costs to taxes is what the financing settlement designs. It is a figure to report, not an error to fix (`DEC-2026-11-10-05`), and no part of it goes to Espen on its own.

**The status rule** (part 2b) is booked on HLT-9's `status-rule` component (the table) and in HLT-10's row, with health's on HLT-7's (`6-cost.md`, part 2b); both are inside the figures above.

**The test years.** The decided costs are permanent: the benefit, the care part, child care and pre-K, the floor and parity all continue past FY2040 and grow with wages and the population over 85. Nothing in parts B-D ends after FY2040 except the facilities fund (FY2035) and the bridge (FY2034).

**What the booking did, and what it left out** (each labeled on its row):
1. **HLT-4's legacy long-term care component is retired**, and its down payment is the bridge and the floor in the rows above, so nothing is counted twice (part 4). HLT-9, HLT-10 and HLT-11 are new bills in regular order; FAM-2 is on the decided path.
2. **The states' payments are booked net** (HLT-9.09, FAM-2.08; part 1's figures are net of them). HLT-9.09 is its own offsetting receipt on health's HLT-7.17 instrument, labeled with the joint legal risk that part 6 prices.
3. **The household test (D3)** carries the F2 and H4 rows, HLT-9's H9 row on the `ltc_universal` key, and DY6's added employment (`models/data/inputs/incidence-rows.csv`, `incidence-keys.csv`, `ledger-dynamic.csv`).
4. **Not booked:** the hold-harmless (inside HLT-9), the residency slots (in HLT-4's safety-net component, health's), and Head Start's grant (current law).

## 6. Sensitivities

| Case | FY2030-39 ($ trillion) | FY2040 ($ billion) | Note |
| --- | --- | --- | --- |
| As decided | 3.54 | 729 | Part 1 |
| Low (each piece's low) | 1.98 | 388 | Fewer new users, lower cost each, low take-up of child care |
| High (each piece's high) | 6.17 | 1,354 | Part B's new users at 5.6 million and $82,500 each; child care take-up high |
| Part B at Urban's best guess (about $560 billion in 2035 at three activities, against $300 billion) | about +1.3 | about +330 | The outside model that sits highest (3b) |
| The states' long-term care payment fails in court (hold harmless) | about +0.6 | about +150 | HLT-9.09; the payment ends and the federal government pays it |
| A third of states decline child care and pre-K and the obligation fails | about +0.1 | about +18 | On one basis (before today's CCDF money is netted and administration added): child care about $87 billion rather than $80 billion at maturity, and pre-K $64 billion rather than $57 billion; about $14 billion more in 2033, grown to FY2040 (re-derived after the review's C-6; memo 17 compared $87 billion gross with $74 billion net) |
| **Joint failure: one ruling against the offset instrument** (health's HLT-7.17, HLT-9.09 and FAM-2.08 together) | not summed here | about +650 | Health's payment, about $480 billion in FY2040 (its $307 billion in 2032, `6-cost.md`, part 6, grown with the plan's per-person cost; the review's reading), plus about $150 billion and $25 billion here. One legal risk, not three: the largest single swing in the plan's financing after the taxes. Health's window path is in `6-cost.md`, part 6 |
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
