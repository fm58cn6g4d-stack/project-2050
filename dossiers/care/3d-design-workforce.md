# Care you can count on, part D (the care workforce): design choices

Role: section 3 of the care dossier, part D: the real forks for paying, staffing and supplying the paid care workforce, the options weighed with their evidence, a recommendation for each, one decision memo per fork (memos 14-16), and a numbered list of narrower yes-or-no points. Status: draft (stage D, step 7); **decided by Espen, November 11, 2026: all as recommended, with the $20 floor** (`DEC-2026-11-11-04`). Costs re-audited in step 8 at the federal cost only, on part B's decided three-activity line, with the bridge's state share set out (`DEC-2026-11-11-05`; "What is and isn't counted" below; further cost options in memo 17). Sources are named in plain text in the memos; bracketed tags point to `evidence.json`; "project arithmetic" is `tools/workforce_demand.py`.

## How to read this section

- **The subject** (section 1): the paid care workforce in home care, nursing homes, child care and early education, plus the health workers whose demand the decided health plan changes. Unpaid family care, K-12 teachers, displaced insurance workers and visas are other owners'.
- **One batched set.** Three memos and nine yes-or-no points, so Espen can answer once. Each is decided on its own, and none is adopted by silence.
  - *Memo 14:* how pay is set in publicly paid long-term care, and at what level.
  - *Memo 15:* early educators' pay.
  - *Memo 16:* nursing home staffing, which part B left open (`3b-design-home-care.md`, point 10).
  - *Training, immigration and health supply* are yes-or-no points, because the evidence and the bills point one way and the cost is small.
- **Evidence strength is stated** for every recommendation: randomized trial, quasi-experimental study, program evaluation, international practice or expert judgment (section 2).
- **Legacy designs are options** (`DEC-2026-10-30-02`):
  - the legacy home care standards board (LAB-3) and sectoral bargaining (LAB-3B), which belong to the work flagship;
  - care apprenticeships (LAB-8);
  - HLT-4's "care workforce" and residency slots;
  - FAM-2A's wage parity;
  - IMM-2's care-worker visa.

  "Inherited assumptions" below traces each one.
- **Report, don't gate** (`DEC-2026-11-10-05`). Costs are working assumptions with basis and range (`DEC-2026-11-10-07`), reported for the financing settlement and not trimmed to fit. Memo 14's level is mainly about money, so it comes with its cost. Financing is Codex's settlement; this part designs no tax.
- **Design lens** (`DEC-2026-11-09-13`). Each requirement says what it asks of workers, providers and states, and what it buys.
- **Time frame** (`DEC-2026-10-29-01`). Recommendations start with the 2029 law; anything before is labeled 2027-28 or preparation.
- **Ranges for parts B and C.** Espen has decided neither part. Every cost here is shown on parts B and C's recommended options, with what changes under their alternatives.

## The baseline in 2029

Section 1, part 6, gives it in full. The federal government sets no wage or staffing standard for any care setting:
- **Worker pay.** The 80% worker-pay rule would start in July 2030 but is likely to be rescinded first [EV-CAR-419] [EV-CAR-420].
- **Nursing home staffing.** The standards are vacated, barred until September 30, 2034, and repealed [EV-CAR-602] [EV-CAR-416] [EV-CAR-603].
- **Wage law.** The Labor Department has proposed restoring the home care exemption from minimum wage and overtime [EV-CAR-616].
- **States.** Minnesota, California and Washington have their own standards [EV-CAR-618] [EV-CAR-619] [EV-CAR-620].

## The forks at a glance

| Fork | Memo | Options | Recommended |
| --- | --- | --- | --- |
| 14. How pay is set in publicly paid home care and nursing homes, and at what level | `memos/14-care-pay.md` | Part 1, how: **A** a pass-through of rate increases, with the 80% share in statute (Better Care Better Jobs; the 2024 rule); **B** a federal care wage floor the payer funds in its rates, with the 80% share as the check, and states free to set more by board or bargaining (Minnesota's method, nationally); **C** state-level bargaining with the state as employer of record in every state (Washington's model; legacy LAB-3B's direction); **D** no care-specific floor (current law, with LAB-4's minimum wage). Part 2, the level for B: **A** $18; **B** $20; **C** $22.50, all in 2026 dollars and indexed | **Part 1 B; part 2 B ($20)** |
| 15. Early educators' pay | `memos/15-early-educator-pay.md` | **A** parity with elementary teachers from the guarantee's start (the Child Care for Working Families Act; legacy FAM-2A); **B** memo 14's floor at once, then a salary scale by role and credential that reaches parity by 2036; **C** memo 14's floor only; **D** a DC-style wage supplement paid outside the rates | **B** |
| 16. Nursing home staffing | `memos/16-nursing-home-staffing.md` | **A** current law (no minimum, facility assessment only) until the moratorium ends in 2034; **B** the 2024 standards in statute from 2030; **C** a statutory standard that puts registered nurses first (24/7 and 0.55 hours from 2031) and phases the 3.48 total in by 2035, funded in rates, with shortage-area exemptions; **D** published staffing and higher pay for homes that staff more, no minimum | **C** |

## What the options cost

Working assumptions, not a model run (`DEC-2026-11-10-07`). Federal new money in nominal dollars, against current law, on top of parts B and C's own costs. **Step 8 repriced this section** on part B's decided three-activity line and the recommended state shares (`tools/workforce_demand.py`, `tools/care_repricing.py`); the earlier figures are given where they help. Parts B and C priced their programs at **today's wage levels**, so a raise is part D's line. These figures replace part B's placeholder (about $55 billion for a 20% home care raise) and use part C's parity line.

**The basis (project arithmetic; judgment where marked).**
- **Home care base in 2035.**
  - *Today's Medicaid home care,* about $164 billion in 2023 [EV-CAR-404] [EV-CAR-406], grown 5.5% a year (part B's working assumption): about $312 billion.
  - *Plus the part of memo 6 B's new money that buys new hours:* richer budgets for today's users, about $30 billion, and new users with the waiting lists included, about $197 billion at the decided three activities (about $275 billion at two). Memo 6 B's other $73 billion relieves states of their share of spending already inside the Medicaid line, buys no new hours and is not added.
  - *Total:* about $538 billion of publicly paid home care that pays for hours of work in 2035 (range $413-819 billion), the figure part B itself gives for part D (`3b-design-home-care.md`); $617 billion at two activities.
  - *Labor:* about 60% of it (part B's judgment).
- **What a floor adds to payroll** (judgment).
  - *The anchor:* the 2024 median is $16.77 an hour in home care [EV-CAR-613], so a $20 floor in 2026 dollars lifts most home care workers. LeadingAge's living-wage model gave 75.3% of direct care workers a raise averaging 15.5% [EV-CAR-626].
  - *Average payroll increase by level:* $18, about 5%; $20, about 12% (range 8-18%); $22.50, about 25%.
  - *Nursing homes:* the median nursing assistant earns $42,260, about $20.30 an hour [EV-CAR-609], so a $20 floor adds little there. Judgment: $1-6 billion, depending on level.
- **The bridge, 2030-34.** Before memo 6 B starts, the floor applies to Medicaid home care: about $239 billion in 2030, about $96 billion of added payroll over the five years. **The federal government pays the floor's added cost at each state's bridge rate**, its regular match (about 60%) plus the bridge's points (about 8): about 68%, or $65 billion, with states paying about $31 billion. It was 90% before step 8 (judgment then, on Better Care Better Jobs' approach of new federal money for new conditions [EV-CAR-617]); the options are under "States' share" below.
- **Child care.**
  - *Parity:* part C's line, about $45 billion on top of memo 10 B at maturity (range $30-65 billion) and about $60 billion in FY2040 at 90% federal (`3c-design-child-care.md`); at the recommended child care share (90% for three years, then 80%), about $53 billion in FY2040.
  - *The floor alone:* about 12% on child care staff payroll. The median is $16.82 [EV-CAR-516], on part C's labor share of about two-thirds of $118 billion gross, at the child care federal share (judgment).
- **Nursing home staffing.**
  - *CMS's own figures:* $43.0 billion over ten years, $4.30 billion a year on average, rising over the decade [EV-CAR-601].
  - *The repeal's figures:* the second Trump administration's repeal analysis says $55.1 billion over ten years [EV-CAR-603], which the project shows as that administration's view.
  - *The federal share:* Medicaid pays for 63% of residents [EV-CAR-438] until 2035. From 2035, under part B's decided memo 8 C, the plan pays the care part of every stay, so the whole staffing cost is federal (step 8; it was counted at about 80%).

| Option | 2035, first year of memo 6 B ($ billion) | FY2030-39 ($ trillion) | FY2040 (about, $ billion) |
| --- | --- | --- | --- |
| Memo 14 A, pass-through only | about 0-10 (judgment: a pass-through moves no money unless rates rise) | about 0.03 | 5-10 |
| **Memo 14 B, $20 floor** (part 2 B, decided) | **about 42 (23-91)**: home care about 39, nursing homes 2-4 (two activities: 47) | **about 0.30 (0.17-0.61)**: the bridge about 0.065 at the bridge rate; from 2035 about 0.23 (two activities and 90%: 0.35) | **about 55 (30-119)** (two activities: 62) |
| Memo 14 B at $18 (part 2 A) | about 17 | about 0.12 | about 22 |
| Memo 14 B at $22.50 (part 2 C) | about 86 | about 0.61 | about 112 |
| Memo 14 C, bargaining in every state | up to about 115-130 at maturity, if wages reach Washington's everywhere, less where bargaining lags (judgment: $22.52 to $23.68 there [EV-CAR-621], about 35-40% above the national home care median); timing set by bargaining | about 0.35-0.6 | about 150-170 |
| Memo 14 D, no floor | 0 | 0 | 0 |
| Memo 15 A, parity from 2032 | about 45 (30-65), part C's line, at 90% | about 0.35 at the recommended child care share | about 53 |
| **Memo 15 B, phased to parity by 2036** (decided) | **about 25 (15-35) in 2033** | **about 0.22 (0.13-0.31)** at the recommended child care share (90%: 0.25) | **about 53 (36-76)**, the same end point as A (90%: 60) |
| Memo 15 C, the floor only | about 10 (5-15) | about 0.07 | about 12 |
| Memo 15 D, a supplement outside rates | as A or B, by level; paid by appropriation | as A or B | as A or B |
| Memo 16 B, the 2024 standards from 2030 | about 4-6, nearly all federal from 2035 | about 0.045 | about 6-8 |
| **Memo 16 C, registered nurses first, total by 2035** (decided) | **about 5-7, all federal from 2035** (about 1-2 a year in 2031-34, the federal part of Medicare and Medicaid's share) | **about 0.04** | **about 7** |
| Memo 16 D, published staffing and bonuses | about 1-2 | about 0.01 | about 2 |
| Points 5 and 7 (training; health supply beyond HLT-4) | about 1.5-2.5 a year | about 0.02 | about 2 |

- **The decided set** (14 B at $20, 15 B, 16 C, the points), after step 8:
  - at today's working state shares (the bridge's floor at 90%, child care at 90%), about $0.63 trillion over FY2030-39 and $124 billion in FY2040;
  - with the state shares Espen accepted (the bridge rate; child care at 90% then 80%; memo 17, question 2, decided), about $0.58 trillion (range $0.35-1.0 trillion) and $117 billion (range $70-205 billion);
  - against $0.65 trillion and $130 billion before step 8.

  It sits on top of parts B and C's own costs.
- **If parts B and C choose otherwise.**
  - *Memo 6 A, stronger Medicaid:* the home care base is about $312 billion with no new benefit. Memo 14 B then costs about $22 billion a year in 2035, and states pay about 47% of it unless the federal government pays the floor's cost.
  - *Memo 10 A, the block grant:* child care's base is a fraction of memo 10 B's, so memo 15's lines fall by about two-thirds. The pull of pre-K staff out of infant care (memo 15) is then worse.
- **Checks against outside estimates.**
  - *LeadingAge's model:* $9.4 billion in 2022 to lift all direct care workers to a living wage [EV-CAR-626]. Grown to 2035 at part B's rate, that is about $19 billion on today's workforce. Memo 6 B at three activities raises the home care base by about 70%, to about $33 billion on that scaling; but LeadingAge's figure covers all direct care workers (nursing homes and private pay included) at its living-wage level, not $20. So it is a rough order-of-magnitude check on memo 14 B's about $39 billion for home care, not a match.
  - *CBO's Build Back Better score:* the home care provisions, about $150 billion over ten years (KFF's report of CBO) [EV-CAR-447]. That bought a match increase with conditions like memo 14 A's, not a floor, and sits between A and B.
  - *CMS's staffing estimate:* about $4.3 billion a year for the 2024 standards [EV-CAR-601]. The repeal's higher figure is the second Trump administration's view [EV-CAR-603].
  - *Part C's parity line:* judgment, not an independent model (part C names no outside estimate). It stays a working assumption, and finding one is in "Evidence still needed".
- **What the totals leave out.**
  - *Savings from lower turnover and less public assistance.* About half of direct care workers rely on public assistance [EV-CAR-613], and LeadingAge counts $0.9-1.6 billion a year of savings (not used; the source's headline overstates its own numbers).
  - *Quality gains,* such as fewer deaths in nursing homes [EV-CAR-624]: not counted, as CBO's scores do not count them.
  - *Who pays:* the financing settlement's question (Codex), not this part's.

## What is and isn't counted (step 8)

Espen asked that part D count only workforce costs the federal government actually pays: "not assuming govt pays all of projected wage increases for workers" (`DEC-2026-11-11-05`). Each line passes three tests. It must count only (1) the cost above the wages the baseline already assumes; (2) care that public programs pay for; and (3) the federal share, with states' share shown separately.

**What is counted.** Only the gap a standard opens between what workers would have been paid anyway and what the standard requires, on hours public money buys, at the federal share.

**What is not counted.**
- Wage growth the baseline already assumes. Parts B and C grow their costs with wages (part B, 4% a year per user) or prices (part C); that growth is in their own lines, not here.
- Private-pay care, employers' own payrolls and families' payments.
- States' share. It is shown beside each line (below), not added.
- Savings from lower turnover and less public assistance, and quality gains, which CBO's scores also leave out (above).

| Line | (1) Above baseline wages only? | (2) Public-program care only? | (3) Federal share only? | Change in step 8 |
| --- | --- | --- | --- | --- |
| **Memo 14 B, the floor in home care** | **Yes.** The 12% payroll lift is measured against the wages the baseline projects for 2026: the 2024 median of $16.77 [EV-CAR-613] grown 4% a year is about $18.14, and on a wage spread fitted to the dossier's three levels the lift is 12-13%. Against 2024 wages it would be 19-20%, a figure the dossier never used (`tools/care_repricing.py`). The floor is indexed to average wages, the same growth the baseline gives care wages, so the gap stays the same share. If care wages in the baseline grow faster than average wages, the floor costs less; if slower, more | **Yes.** The base is publicly paid home care that buys hours: Medicaid's line and memo 6 B's new hours. Private-pay home care is outside the floor and outside the base | **From 2035, yes.** The plan pays its own rates, and states' maintenance of effort is a fixed amount, so the added cost is federal. **In 2030-34, corrected:** 90% federal became each state's bridge rate, about 68% | Base $617 → $538 billion (three activities); bridge share 90% → about 68% |
| Memo 14 B, the floor in nursing homes | Yes: the median nursing assistant already earns about $20.30 [EV-CAR-609], so the added cost is small ($2-4 billion) | From 2035 the plan pays the care part of every stay (memo 8 C), so all of it is public | Yes from 2035 | None |
| **Memo 15 B, early educators' parity** | **Yes.** It is a ratio on part C's base, which grows with prices only, so no wage growth is counted. Part C's base itself leaves out the real wage growth child care workers would get anyway, about 1% a year. That understates part C's own line slightly, by perhaps $4-7 billion a year by the late 2030s; section 6 should grow its labor with wages | **Yes.** Under memo 10 B a family's payment is capped at a share of income, not of cost, so a raise falls on the program. Only a family whose 7% of income exceeds the full price pays more, at incomes far above the median (judgment: a rounding error) | **Corrected** to the recommended child care share, 90% for three years then 80% | FY2040 $60 → $53 billion |
| Pre-K's parity (inside part C's memo 11 A) | Yes: priced in NIEER's cost model [EV-CAR-566] | Yes | 90% for three years, then 75% (unchanged) | None |
| **Memo 16 C, nursing home staffing** | Yes: CMS's added staffing cost [EV-CAR-601] | Before 2035, only Medicare's and Medicaid's federal part; private payers bear theirs | **Corrected upward:** from 2035 the plan pays the care part of every stay, so the cost is all federal, not about 80% | 2035 federal $4-6 → $5-7 billion; FY2040 $6 → $7 billion |
| Points 5 and 7, training and health supply | Not wages | Federal grants | Federal | None |

**Flagged for the booking, not changed here.** HLT-4 is booked at $0.50 trillion over FY2030-39 (`6-cost.md`, part 5). It includes the legacy "HCBS down payment and care workforce" (`legacy/domains/domain-health.md`, HLT-4). Part B's bridge (point 1) and memo 14's bridge-period floor are that down payment. When parts B and D are booked, they replace HLT-4's long-term care part rather than adding to it. The legacy row does not separate that part, so the booking sizes it. This is a tier-3 booking change for the lead; part D books nothing.

## States' share (step 8; the financing settlement decides)

Espen asked that states pay a portion of all of it (`DEC-2026-11-11-05`). Part D's costs follow the payer's rates, so states' share is set where the rates are set:
- *home care and nursing homes from 2035:* part B's maintenance of effort (`3b-design-home-care.md`, 50% recommended, as in health's HLT-7.17), so the floor's added cost is federal;
- *child care and pre-K:* part C's shares (`3c-design-child-care.md`).

The one share part D sets itself is the wage floor's added cost in Medicaid home care in 2030-34, before the plan pays.

| Option for the bridge's floor | Federal, 2030-34 | States, 2030-34 | Burden on states | Risk that states cut back |
| --- | --- | --- | --- | --- |
| 90% federal (before step 8) | about $86 billion | about $10 billion | Least | Least |
| **Each state's bridge rate: its regular match plus the bridge's points, about 68% (recommended)** | **about $65 billion** | **about $31 billion, about $6 billion a year** | A share at the rate the state already uses for home care in the bridge | Low for states taking the bridge's points: those points bring about $14-24 billion a year against their share of about $6 billion, and their entry condition bars cutting their own spending (part B, point 1) |
| The regular match, about 60% | about $58 billion | about $38 billion | The normal Medicaid share | Higher. Home care is mostly optional, so a state paying 40% of a new mandate could trim waiver slots or hours |

*Recommendation: the bridge rate.* States pay a real share, a third, at the rate their home care is already matched at. The bridge's points more than cover it, and their maintenance-of-effort condition guards against cuts. It saves about $0.02 trillion against 90%. Part D's point 3 (state standards above the floor at the normal share) already uses the same rule.

## Against the bills and state models

*Match* means the same choice; *diverge* gives the reason. The bills' texts are in the library.

| Feature | Recommended here | Better Care Better Jobs (S. 100, 2023) [EV-CAR-617] | HCBS Access Act (H.R. 8540, 2026) [EV-CAR-639] | 2024 rules (access, staffing) | Medicare for All (S. 1506, H.R. 3069) [EV-CAR-637] [EV-CAR-638] | Child Care for Working Families Act [EV-CAR-581] | State models | Why |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A wage number in law | **Yes:** $20 in 2026 dollars, indexed, in publicly paid home care and nursing homes (memo 14) | Diverge: none; states show "competitive wages" | Diverge: none; rates "adequate to recruit and retain" | Diverge: none | Diverge: none; budgets account for wages and bargaining agreements | Match in child care: a living wage and parity | Minnesota: $22.50 for nursing assistants [EV-CAR-618]; California $25 for large systems [EV-CAR-619] | A floor is the only design that guarantees pay; the bills left the level to states, and state rates stayed low [EV-CAR-627] |
| Pass-through of payments to wages | **Yes:** the 80% share in statute, as the floor's check | Match in part: increases passed through proportionately | Match in part: the same | Match: 80% of three services [EV-CAR-419] | Diverge: none | — | California holds nursing homes out until a spending rule exists [EV-CAR-619] | A share rule alone splits a low rate; with a floor it checks that money reaches workers |
| Bargaining | States may bargain or run boards above the floor; the floor is the national minimum | Match: cooperation with unions where workers organized | Match: cooperation, or neutrality where not | — | Diverge: recognized in budgets, not required | — | Washington [EV-CAR-620]; Minnesota's board [EV-CAR-618] | Harris v. Quinn limits fee-funded units [EV-CAR-623]; a federal floor works in states without bargaining |
| Who pays the raise | The payer: the plan from 2035; each state's bridge rate (about 68% federal) in the 2030-34 bridge | Diverge: a 10-point match for all conditions | Diverge: 100% federal match | Diverge: no money | The plan | 90% federal for child care | Minnesota funds through its Medicaid rate [EV-CAR-618] | A floor without money is the 2024 staffing rule's failure [EV-CAR-601] |
| Early educators' pay | Floor at once, parity by 2036 (memo 15 B) | — | — | — | — | Diverge on timing: parity from the start | DC's fund, cut and unfunded after FY2027 [EV-CAR-630] | Phasing matches part C's supply build and the degree pipeline (part C, point 6) |
| Nursing home staffing | Statute, registered nurses first (24/7, 0.55 hours from 2031), 3.48 total by 2035, funded (memo 16 C) | — | — | Diverge on vehicle and order: the same numbers by rule, at once, unfunded [EV-CAR-600] | Match in kind: mandatory nurse staffing ratios (H.R. 3069 standards; S. 1506 budgets) | — | New York, 3.5 hours by statute (not in register) | Courts struck the rule for want of authority [EV-CAR-602]; registered nurse hours drive quality [EV-CAR-608] |
| Training | Free entry-level training, paid training time, portable credentials (point 5) | Match: workforce training and registries | Match: training programs and registries | — | — | Match: workforce supports | — | Randomized trials: training moves people into care jobs; pay keeps them [EV-CAR-631] [EV-CAR-632] |

## Inherited assumptions, traced

| Assumption | Where it comes from | Espen decided, or a working choice? | Here |
| --- | --- | --- | --- |
| Federal home care and fast food standards boards that set wage floors (LAB-3) | Legacy labor file, from Bill Book 10 (`legacy/domains/domain-labor.md`) | **Working choice** (`DEC-2026-10-30-02`); the work flagship owns LAB-3 | Memo 14 B sets the floor through the payer instead, because public money pays most care [EV-CAR-404]. If the work flagship keeps LAB-3, its home care board can set floors above memo 14's |
| Multi-employer sectoral bargaining (LAB-3B) | Legacy labor file | Working choice, held as an option there | Memo 14 C, state-level bargaining with the state as employer, is the form that has US precedent [EV-CAR-620] |
| "Most home care is Medicaid-funded, so the board's floor needs a matching pass-through in Medicaid rates" | Legacy LAB-3 note | Analysis, not a decision | Kept: it is memo 14 B's core |
| Care apprenticeships in one registered-apprenticeship line, about $0.03 trillion (LAB-8) | Legacy labor file, estimate with no source | Working choice; the work flagship owns LAB-8 | Point 5 asks for a care line inside it and sizes it |
| HLT-4's "HCBS down payment and care workforce" and "14,000 residency slots" | Legacy health file; HLT-4 is booked at $0.50 trillion over FY2030-39 (`6-cost.md`, part 5) | Working choice. HLT-4 is booked as a legacy row; its parts are not separately decided | The down payment is part B's bridge (point 1). The residency slots are point 7, on S. 2439's design [EV-CAR-634]. **Section 6 must check** that HLT-4's booked workforce money and memo 14's bridge-period floor are not counted twice |
| Wage parity for child care workers from 2030-31 (FAM-2A) | Legacy family file | **Working choice**, chosen by an agent | Memo 15: parity kept as the end point; B phases it to 2036 |
| A care-worker visa tied to FAM-2 and HLT-4 (IMM-2) | Legacy immigration file | Working choice; the immigration flagship owns it (shared rule 8) | Point 8 names what care needs; immigration decides |
| A 20% home care raise costs about $55 billion on top of memo 6 B | Part B's placeholder (`3b-design-home-care.md`) | Agent's judgment | Replaced by memo 14's table |
| Parity costs about $45 billion on top of memo 10 B | Part C (`3c-design-child-care.md`) | Agent's judgment | Used as memo 15 A's cost |
| The single plan by January 1, 2035; long-term care in Medicaid until part B decides | `DEC-2026-11-10-09`, `-11` (HLT-7, HLT-7.07) | **Espen decided** | The demand base (section 1, part 5); the plan is the payer that funds the floor from 2035 |
| Provider rates on a glide path to about 1.15 times Medicare | `DEC-2026-11-10-09` (memo 5 B) | **Espen decided** | Not reopened. Memo 14's floor applies to long-term care rates, which memo 5 does not set |
| Help for displaced insurance and billing workers | `DEC-2026-11-10-09` (HLT-7.16) | **Espen decided** | Outside part D; its job-placement channel (American Job Centers) is the one point 5 uses |
| Time frame, design lens, report don't gate, what needs an answer now, source rules | `DEC-2026-10-29-01`, `DEC-2026-11-09-13`, `DEC-2026-11-10-05`, `-07`, `DEC-2026-10-28-07`, `DEC-2026-10-30-01` | **Espen decided** | Applied throughout. The 2024 rules' and the repeal's analyses are each shown with their administration |

## Seams with other dossiers (named, not settled)

- **Work flagship.**
  - *What it owns:* the general minimum wage (LAB-4), standards boards (LAB-3), bargaining law (LAB-1) and apprenticeships (LAB-8).
  - *What part D does:* it decides what care's payers pay for. The floor is a condition of public payment, not a labor-law minimum. So it holds whatever the labor bill does, and it can pass in a reconciliation bill, since it is a spending rule.
  - *Asks:* point 2 (home care's wage and overtime coverage) and point 5's care line go to the work flagship.
- **Immigration flagship** (shared rule 8). Point 8 lists what care needs; visas and status are immigration's.
- **Education.** The K-12 pipeline and schools of education are EDU-4's. Memo 15 coordinates pre-K hiring with it, as part C's seam says.
- **Health.**
  - *Memo 5 B's rates* cover medical care and are not reopened.
  - *Memo 16* sets nursing home staffing, which health's sections do not.
  - *The single plan's added demand for nurses and physicians* is point 7.
- **Parts B and C.** The floor applies to the benefits they design. Relatives paid through part B's benefit get the same floor, under memo 9 E's state options or 9 A's national right (point 1).
- **Financing.** Costs are reported; taxes are the settlement's.

## Recommended without a memo: nine yes-or-no points

Each is decided on its own. None is adopted by silence. Costs are judgment unless a tag gives them.

1. **Paid family caregivers get the same floor.** Wherever public money pays a relative for care, the relative is paid at least memo 14's floor, like any other worker. That holds in Medicaid in the bridge, through the state options part B's memo 9 E carries into the benefit, and under a national right if Espen chooses memo 9 A. Who may be paid is part B's question; what they are paid is this one.
   - *Why:* most self-directed hires are relatives [EV-CAR-488], and California counties estimate 70% of IHSS recipients hire family [EV-CAR-494]. A lower family rate would make care cheaper by underpaying the caregivers part B's memo 9 supports, under either answer.
   - *Evidence:* program evaluation (Cash and Counseling, randomized) [EV-CAR-488].
   - *Cost:* inside memo 14's figures, which include family hours.
   - *Political risk:* "paying families for what they did for free." Part B's audit found the principle is already mainstream in red and blue states [EV-CAR-493].

   **Recommended: yes.**
2. **Keep home care workers under federal minimum wage and overtime law.** If the Labor Department finalizes its proposal to restore the 1975 exemptions [EV-CAR-616], the first 2029 labor bill puts the 2013 coverage in statute. This is proposed to the work flagship, which owns wage law.
   - *Why:* without it, an agency-employed aide could lose overtime. Memo 14's floor covers only publicly paid care.
   - *Cost:* none federal, beyond overtime in rates (inside memo 14's range).

   **Recommended: yes, as a proposal to the work flagship.**
3. **State standards above the floor are allowable costs.** A state wage board's or bargaining agreement's higher wage is an allowable cost in Medicaid and plan rates, paid at the normal share, with approval on a fixed clock.
   - *Why:* Minnesota's standards waited for federal approval of the rate change [EV-CAR-618]. States that do more should not wait or pay alone.
   - *Burden:* none new; it shortens a review.

   **Recommended: yes.**
4. **Workforce counts from records already held.** States and the plan publish wages, hours and turnover by setting each year. The sources are nursing homes' Payroll-Based Journal, which already produces national counts [EV-CAR-604], and the payroll that fiscal agents and agencies already report for the 80% share.
   - *Why:* the floor, memo 16 and point 5 need a count. No national home care turnover figure is in the register (section 1).
   - *Burden:* no new survey; it reuses existing reports.

   **Recommended: yes.**
5. **Free entry-level training and paid training time.** For home care aides, nursing assistants and child care staff: through community colleges and registered apprenticeship (a care line in LAB-8, for the work flagship), with credentials that count in every state and job placement through American Job Centers.
   - *Cost:* about $1-2 billion a year over FY2030-39, peaking ahead of 2035 and part C's 2031-33 hiring (judgment, against HPOG and sector-training costs).
   - *Evidence:* randomized trials. Training moves people into health and care jobs [EV-CAR-631], and sector programs that place people in better-paid jobs raise earnings 11-40 percent [EV-CAR-632]. Health and human services apprenticeships grew 47 percent in five years [EV-CAR-633].
   - *Why with the floor:* training without pay did not raise earnings [EV-CAR-631].

   **Recommended: yes.**
6. **One home care aide training standard, without new barriers.** One national basic training standard for agency aides, accepted in every state, with prior experience counted. Family caregivers hired by the person they care for need only a short orientation.
   - *Why:* portability helps supply. The design lens counts against a training wall for relatives already giving care.
   - *Evidence:* expert judgment.
   - *Burden:* light for agencies; none new for families.

   **Recommended: yes.**
7. **Health supply for the single plan.**
   - *Residency slots:* keep HLT-4's 14,000 residency slots on the Resident Physician Shortage Reduction Act's design, 2,000 a year [EV-CAR-634], timed for FY2030-36, with priority for primary care and shortage areas.
   - *Nursing:* add nurse faculty and training grants sized to HRSA's projected shortage [EV-CAR-611].
   - *Why:* the single plan adds demand for about 100,000-280,000 registered nurses and 30,000-80,000 physicians at full scale (section 1, part 5), and residency takes years (judgment: three to seven, by specialty).
   - *Evidence:* the shortage projections (analysis) and the bill (design); no evaluation in the register.
   - *Cost:* the slots are in HLT-4's booking. Nurse training is about $0.5-1 billion a year (judgment).

   **Recommended: yes.**
8. **What care needs from the immigration flagship** (named, for its decision; shared rule 8):
   - (a) keep people now working in care able to stay and work;
   - (b) a visa route for care occupations that lets workers change employers, paid at least memo 14's floor;
   - (c) count care occupations in any shortage list.

   - *Why:* immigrants are 30% of direct care workers [EV-CAR-614], and enforcement measurably cut nursing home care hours [EV-CAR-635].
   - *Political risk:* a care-worker visa invites the charge of importing low-wage labor. The floor and job portability answer it.

   **Recommended: yes, as asks to immigration.**
9. **Part B's point 10 is answered by memo 16.** The moratorium is repealed only as memo 16's option requires. Under memo 16 C, the 2029 law replaces the 2024 rule with its own standard, so the moratorium's bar on the old rule no longer matters.
   - *2027-28:* no vehicle is expected. Preparation before 2029 is a CMS staffing data review, not a rule.

   **Recommended: yes.**

## Shared rules this section relies on

From `dossiers/shared-rules.md`. These are working answers, not decisions of the other owners.

| Rule | Owner | Part D's working answer | Range |
| --- | --- | --- | --- |
| 8. Workforce | Immigration (visas and status); work (apprenticeships) | Part D sets pay, staffing and training for publicly paid care; asks immigration for point 8 and work for points 2 and 5 | From no care-specific action to a full care visa program |
| 3. Immigrant eligibility | Immigration | Not used: the floor follows the job, not the worker's status | — |
| 6. Conditions on help | Work flagship | Not used: no condition on families | — |

**Proposed note for rule 8**, for Espen with points 5 and 8: "Care (part D) sets pay floors, staffing standards and training for care that public money pays for. It asks the immigration flagship to protect care workers' status and consider a portable care visa, and the work flagship to carry a care line in LAB-8 and home care's wage and overtime coverage."

## How the choices fit together

- **The recommended set, in two steps.**
  - *From 2030 (the bridge).*
    - A $20 floor (2026 dollars, indexed) in Medicaid home care, matched at each state's bridge rate (about 68% federal).
    - The 80% share in statute as its check; family caregivers at the floor.
    - Child care staff at the floor from the 2030-31 school year, and the salary scale toward parity.
    - Registered nurses first in nursing homes from 2031.
    - Free training ahead of the hiring peaks, and the residency slots.
  - *From January 1, 2035.* The plan pays the floor in its home care benefit and the care part of nursing home stays. Nursing homes meet the full 3.48 standard, and early educators reach parity by 2036.
- **Why this order.** Pay comes first because it is the lever with the best evidence [EV-CAR-624] [EV-CAR-625]. Training (point 5) and immigration (point 8) only fill jobs that pay.
- **If memo 14 is A.** Pay rises only as rates rise. Parts B and C's benefits would then meet the supply limit of section 1, part 5, and the risk of waiting lists is highest.
- **If memo 14 is C.** Wages are set state by state, and some states will not bargain. B's floor is the fallback in those states.
- **Tensions to watch.**
  - *The size of the need.* The added demand, about 2.8 million recruits on part B's decided three-activity line (range 0.9-8.8 million; 3.6 million at two activities), is the largest risk to parts B and C. Pay raises supply but cannot double it in five years. Part B's 2035 start and part C's phasing give time.
  - *Nursing homes.* A staffing standard pulls nurses toward nursing homes while the single plan pulls them toward hospitals and clinics. Memo 16 C's phasing and point 7 address it.
  - *Child care.* Pre-K at parity before child care reaches it drains infant rooms [EV-CAR-569]. Memo 15 B moves both together.

## Evidence still needed

- **An independent estimate of the cost of early educator parity** (memo 15): part C's line is judgment. Search leads not read: Bank Street's birth-to-three model, Urban's DC estimate.
- **Home care wages by percentile**, to price each floor level: BLS OEWS, which refused the project's tools.
- **A quasi-experimental study of a Medicaid home care wage pass-through** (MACPAC's March 2026 chapter, not read).
- **The outcome of the Fifth Circuit appeal** and whether CMS finalized its interim repeal (memo 16).
- **Whether California's home health tier is the $25 schedule**, and the IHSS public authorities' statute (memo 14, the bill table).
- **Child care workers' immigrant share** from a source read in full (point 8).

## Questions for Espen

Decided November 11, 2026 (`DEC-2026-11-11-04`): memo 14 B at $20, memo 15 B, memo 16 C and points 1-9, all as recommended. Memo 17's cost options were decided by Espen November 12, 2026 (board question 0n; being recorded in the lead's tier-3 PR on `claude/dec-care-cost`): the bridge's floor at each state's bridge rate, yes; early educators' parity stays at 2036 (option 3, no). Part D's decided cost: about $0.58 trillion over FY2030-39 and $117 billion in FY2040.
