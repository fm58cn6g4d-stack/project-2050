# Memo 7: Unemployment insurance

Role: decision memo for Espen on unemployment insurance, answering section 2's question 9. No legacy agenda row covers it: the secure floor left it to this flagship (`dossiers/work/1-problem.md`, part G), so a new row (ID LAB-11, now decided) is added to `agenda/agenda.csv` once Espen decides. Status: **decided** (`DEC-2026-11-17-10`): **B**, as recommended; the new agenda row is LAB-11. [Repriced after the milestone review (fix step 1): as specified, 75% of high-quarter pay up to two-thirds of the state's average weekly wage raises regular benefits about 2.1 times, **about +$42 billion a year at FY2025 levels (range $25-66 billion)**, not $15-25 billion, which is what a replacement rate near half gives; employers' state UI taxes about double. The general fund rises about +$0.09 trillion over FY2030-39 and +$11.5 billion in FY2040 with the tax offset (`../6-cost.md`, part 2). Whether to keep the 75% from 2031 or phase it in goes to Espen as a provisional question (`../6-cost.md`, "Questions for Espen", item 1). The decision stands; the text below is the memo as sent. Revised for Espen's November 18 answer W8 (#450): the part below, "Espen's November 18 questions (W8), answered", says how federal law sets the standards, that benefits are taxable, who pays, the phase-ins and how far the cap varies by state; the phase-in stays provisional.] Work-search rules are point 10 in `../3-design.md`; paid leave is the secure floor's (FAM-3) and is not reopened. Sources are named in plain text; bracketed tags point to `../evidence.json`.

**Decision line.** Recommended: **B, federal standards for every state program, on the core of the 2025 Wyden-Bennet bill: at least 26 weeks; weekly benefits of 75% of high-quarter earnings up to a state maximum of at least two-thirds of the state's average weekly wage; coverage of part-time workers and of anyone with $1,000 in a quarter and $1,500 in the base period; the most recent quarter counted; the ABC test (memo 6); work sharing in every state; Extended Benefits paid fully by the federal government and switched on automatically when unemployment rises; identity and wage checks against records the government already holds. The trust funds are rebuilt by raising and indexing the federal taxable wage base, now $7,000 [EV-WRK-310].** Cost: on the general fund about **+$0.03-0.08 trillion over FY2030-39 and +$3-8 billion in FY2040** (the federal Extended Benefits share and administration; judgment); regular benefits rise about **$15-25 billion a year in an ordinary year**, paid from the trust funds and matched by employers' taxes over the cycle (judgment). No CBO score of such a bill exists. Evidence: quasi-experimental studies on benefit generosity, spending and the pandemic supplements; official data on reach and solvency; GAO and the Inspector General on fraud.

## Espen's November 18 questions (W8), answered

Espen's November 18 answer W8 (#450) found option A's formula reasonable, was open to B's or C's phase-in, favored keeping a high share of pay, and asked three questions. This part answers them; the decision (`DEC-2026-11-17-10`) stands, and the phase-in stays **provisional** until Espen confirms this revision.

**1. Can federal law tell states how much to tax and pay?** Not by direct order: it works through a tax credit.
- Employers owe a federal unemployment tax of 6% on the first $7,000 of each worker's pay. They may credit against it what they pay into their state's fund, up to 5.4%, but only if the Labor Department certifies that the state's law meets federal conditions (26 U.S.C. 3302(a)(1), (b), (c)(1); 3304(a)) [EV-WRK-476] [EV-WRK-477]. In a conforming state the employer pays a net 0.6% federally [EV-WRK-310].
- So a state may set any law it likes, but if its law fails a condition, its employers lose the credit and pay up to 5.4% more federal tax. No state has chosen that. This is how today's rules on who is covered and how benefits are paid already work, and the Supreme Court upheld the design in 1937 (*Steward Machine Co. v. Davis*; judgment, not in the register).
- LAB-11.01's standards are new conditions of the same kind. LAB-11.10 adds a conformity reduction and lets Labor pay the difference through the state agency where a state refuses (`../6-cost.md`, part 2).

**2. Are unemployment benefits taxed?** Yes, federally: gross income includes unemployment compensation (26 U.S.C. 85(a)) [EV-WRK-475]. The only exclusion, up to $10,200, was for 2020. Whether a state taxes them is state law, not checked here. The cost lines already count it: the general fund gets back part of the tax it loses on employers' larger UI taxes (the offset line, "net of tax on benefits", `../6-cost.md`, part 1).

**3. Who pays, and how much does the federal government cover?**

| Who | What they pay for | A year, at the 75% standard |
| --- | --- | --- |
| **Employers, through state UI taxes** | Every regular benefit week, from the state's account in the trust fund | About **$42 billion more** at FY2025 levels (range $25-66 billion), roughly doubling today's state UI taxes: about $275 more a covered worker, about two-thirds of a percent of pay in all (`../6-cost.md`, part 2) |
| **Employers, through the federal tax** | Administration, loans and the federal accounts | About $42 a worker today, about $50 at the $25,000 base: almost no change (LAB-11.05) |
| **The federal general fund** | Extended Benefits at 100% (LAB-11.04), state administration (LAB-11.08), the conformity grant, and income tax lost because employers deduct larger UI taxes, net of tax on benefits | About **$11.5 billion in FY2040** in all ($0.09 trillion over FY2030-39). The part the 75% rate adds, against the replacement near half memo 7 first assumed, is about **$4 billion a year by FY2040** |
| **Social Security** (off budget) | Payroll tax lost on the same deduction | About $6 billion in FY2040 |
| **Workers** | Income tax on their benefits (above) | — |

The federal government pays **no regular benefits**. The regular benefit is paid by employers in every state; the general fund pays for recessions, administration and the tax offset.

**Phase-in, B or C** (each priced in `../tools/work_path.py --ui-options`; `../6-cost.md`, "Questions for Espen", item 1):

| Path | 2031 | 2032 | 2033 | 2034 | 2035-38 | 2039 on | Employers, FY2031-39 | General fund, FY2030-39 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A. 75% from 2031 (drafted) | 75% | 75% | 75% | 75% | 75% | 75% | $541 billion | $75.6 billion |
| B. With the wage base | 60% | 65% | 70% | 75% | 75% | 75% | $506 billion | $72.5 billion |
| C. Slow | 50% | 53% | 56% | 59% | 63-72% | 75% | $394 billion | $62.5 billion |

Every path ends at 75% of pay, the high share Espen favors. B raises the rate as the taxable wage base rises (LAB-11.05: $13,000 in 2031, $19,000 in 2032, $25,000 in 2033), so each year's larger benefits arrive with each year's larger base. It saves employers about $35 billion over nine years and nothing after 2034, at the cost of states programming the formula four times. C saves about $150 billion but reaches the standard only in 2039. **Recommended: A, with B as a reasonable choice** if Espen prefers a gentler start for the weak trust funds (only 18 states met the solvency standard at the start of 2026 [EV-WRK-304]). The drafted lines use A.

**How far the cap varies by state.** The weekly benefit is 75% of high-quarter weekly pay up to two-thirds of the state's average weekly wage. Two-thirds of BLS's 2025 average weekly wage (project arithmetic, `../tools/ui_cap_by_state.py`, on [EV-WRK-478]; a state's legal figure follows its own law and lags a year or more):

| State | Average weekly wage, 2025 | Cap | Weekly benefit at $17 an hour | At $30 an hour | At $45 an hour |
| --- | --- | --- | --- | --- | --- |
| Puerto Rico | $700 | $467 | $467 | $467 | $467 |
| Mississippi | $1,024 | $683 | $510 | $683 | $683 |
| Ohio | $1,313 | $875 | $510 | $875 | $875 |
| United States | $1,514 | $1,009 | $510 | $900 | $1,009 |
| Maryland | $1,568 | $1,045 | $510 | $900 | $1,045 |
| Massachusetts | $1,925 | $1,283 | $510 | $900 | $1,283 |
| District of Columbia | $2,479 | $1,653 | $510 | $900 | $1,350 |

- Across the states and D.C., the cap runs from about $683 (Mississippi) to $1,653 (D.C.); the middle state's is about $903. Mississippi's is about two-thirds of Maryland's.
- **For low-wage workers the cap does not bind:** a full-time worker at $17 an hour gets $510, 75% of pay, in every state but Puerto Rico. It binds for workers above about 0.89 of the state's average wage: a $30-an-hour worker gets 75% of pay in Maryland and about 57% in Mississippi.
- Mississippi's maximum today is $235 [EV-WRK-300]; the standard nearly triples it. So the larger lever Espen names works both ways: the cap tracks local wages, which keeps it near the same share of local pay everywhere, but leaves a middle-wage worker in a low-wage state with a lower share of pay.
- *If Espen wants more,* a national floor under the cap (for example, the higher of two-thirds of the state's average or half the national average, about $757 in 2025) would lift it only in Puerto Rico, Mississippi and the Virgin Islands, at a small cost to employers there (not priced). It is not drafted; it is a question for Espen (`../6-cost.md`, "Questions for Espen", item 1).

## The question

Unemployment insurance reached 27-29% of unemployed people in 2023-24, from about 10% in Kentucky to 55% in Minnesota, and replaced 43% of recipients' wages (Federal Reserve Bank of Minneapolis) [EV-SEC-045] [EV-SEC-046] [EV-WRK-302]. Weekly maximums run from $235 in Mississippi to $1,051 in Massachusetts (CRS) [EV-WRK-300]; Florida pays as few as 12 weeks [EV-WRK-314]. Only 18 state trust funds met the solvency standard at the start of 2026, down from 31 in 2020 (Labor Department) [EV-WRK-304]. The federal tax is 0.6% on the first $7,000 of pay [EV-WRK-310]. Regular federal outlays for unemployment compensation were about $41.8 billion in FY2025, against $475 billion at the pandemic peak (OMB) [EV-WRK-413]. The question is whether the plan sets national standards, and how it pays for and protects them.

## Why it matters

- **Job loss is common and costly:** 3.3 million long-tenured workers were displaced in 2023-25, and only 49% of those back in full-time work earned as much as before (BLS) [EV-WRK-315] [EV-WRK-317].
- **For a household.** A laid-off cashier in a low-recipiency state who worked part-time often does not qualify; if she does, she may get a few hundred dollars a week for 12-16 weeks. Under B she qualifies on her recent quarters and gets about three-quarters of her high-quarter weekly pay, up to a cap, for 26 weeks.

## What the evidence says, in five lines

1. **Benefits lengthen claims somewhat:** median elasticity 0.53 across 18 quasi-experimental studies (Schmieder and von Wachter, 2016) [EV-WRK-368].
2. **At scale in 2020-21, the effect on job finding was small against a large effect on spending** (Ganong and others, bank-account data; Coombs and others) [EV-WRK-370] [EV-WRK-371].
3. **Length protects spending more than level:** spending falls 12% when benefits run out, and extending benefits protects it four times as much as raising them (Ganong and Noel, *American Economic Review*) [EV-WRK-372].
4. **Extended benefits' effect on unemployment is disputed:** 2 points in 2011 on one design (Hagedorn and others) [EV-WRK-374], at most 0.3 point on a cleaner one (Chodorow-Reich, Coglianese and Karabarbounis) [EV-WRK-375].
5. **Fast expansion through weak checks invited fraud:** $100-135 billion in the pandemic, 11-15% of benefits (GAO, 2023) [EV-WRK-378]; the Inspector General puts improper payments at $191 billion or more [EV-WRK-379]. Work sharing saves jobs but can prop up firms that would shrink (Giupponi and Landais, Italy) [EV-WRK-383].

## Options

**A. Fund and fix administration only.** Restore state administration money to its FY2023-24 level ($3.13 billion, against $2.76 billion requested for FY2027) [EV-WRK-309] [EV-WRK-308]; build identity and wage matching on records the government holds; no new benefit rules.
- *Cost:* about $0.4-0.8 billion a year (judgment), $0.005-0.01 trillion.
- *What it leaves:* recipiency and benefits as state law sets them.

**B. Federal standards on the 2025 bill's core, with Extended Benefits reformed and trust funds rebuilt (recommended).**
- *Standards (conditions for employers' federal tax credit, as today's system works):* 26 weeks; 75% of high-quarter weekly earnings up to at least two-thirds of the state average weekly wage; part-time workers covered; $1,000 / $1,500 earnings test; the most recent quarter counted; ABC coverage [EV-WRK-394]; work sharing in every state, with employers filing.
- *Recessions:* Extended Benefits 100% federal, on automatic triggers (unemployment at 5.5%, or half a point above its recent low), adding weeks as unemployment climbs [EV-WRK-395].
- *Financing:* the federal taxable wage base raised from $7,000 in steps and indexed, with states' bases following; the federal rate cut so the federal tax per worker rises gradually; interest-free loans for states that meet a solvency target.
- *Integrity:* identity checks through the IRS and Social Security records and employers' quarterly wage reports, which states already receive; no new documents for claimants (`DEC-2026-11-09-13`).
- *Cost:* regular benefits up about 40-60% in an ordinary year, $15-25 billion at FY2025 levels [EV-WRK-413] (judgment: recipiency toward 40% and replacement toward about half), paid from the trust funds, which employers' taxes refill over the cycle; the federal Extended Benefits share and administration on the general fund, about +$0.03-0.08 trillion over FY2030-39 (judgment, averaging recession and ordinary years).
- *Burden:* on employers, a higher tax base; on states, new rules by a set date; on claimants, fewer denials.

**C. B plus a federal Jobseeker Allowance:** $250 a week for up to 26 weeks for unemployed people outside regular coverage, such as new entrants and the self-employed [EV-WRK-395].
- *Cost:* about $5-12 billion a year more on the general fund (judgment: one to two million recipients a year), about +$0.05-0.12 trillion.
- *Overlap:* the secure floor's decided income support and LAB-10's paid on-ramps already reach many of the same people (`DEC-2026-11-12-06`).

**D. A federal program** replacing the 53 state systems.
- *What it buys:* one set of rules and one computer system.
- *What it costs:* a rebuild during the plan's first term, against the design lens's "existing machinery first" (`DEC-2026-11-13-08`), and the pandemic's lesson that system changes under strain invite fraud [EV-WRK-378].

## Against the bills

| Bill | Benefits | Coverage | Recessions | Financing | Against the recommendation |
| --- | --- | --- | --- | --- | --- |
| **UI Modernization and Recession Readiness Act of 2025**, S. 2312 (Wyden, Bennet) [EV-WRK-394] [EV-WRK-395] | 26 weeks; 75% of high quarter; max two-thirds of the average wage; no waiting week; dependents' allowance | Part-time, $1,000 / $1,500, ABC | EB 100% federal, automatic | Not in the summary read | **Match** on the core; B leaves out the waiting-week and dependents' items for section 4 to weigh, and C is its Jobseeker Allowance |
| **2009 recovery act incentives** [EV-WRK-376] [EV-WRK-377] | — | Alternative base periods (41 of 53 had them) | — | $7 billion in incentives | B makes them standards |
| **P.L. 119-21** (2025) [EV-WRK-311] | — | Bars benefits above $1 million in base-period wages | — | — | Kept |

No CBO or JCT score of S. 2312 or its 2023 version was found (sponsors' summary; section 2, "Evidence still needed").

## Consequences at a glance

| | A | **B** | C | D |
| --- | --- | --- | --- | --- |
| Share of unemployed receiving benefits | About 27-29% | Rising toward about 40% (judgment) | Higher | As B |
| Weeks | 12-26 by state | 26, more in recessions | 26, more in recessions | As B |
| General fund FY2030-39 | About $0.01 trillion | About +$0.03-0.08 trillion | About +$0.08-0.20 trillion | Larger, plus the rebuild |
| Trust-fund benefits, ordinary year | Unchanged | +$15-25 billion, employer-financed | As B | As B |
| Fraud exposure | Lower with checks | Managed by records checks | Higher (no wage record for some) | Highest during the rebuild |

## Recommendation: B

- **The system reaches too few and pays too little to cushion job loss,** and most of the gap is state rules that a federal standard can change through the existing tax-credit lever.
- **Length matters most for families** [EV-WRK-372], so 26 weeks and automatic extensions come first.
- **Building on the 53 state systems,** with checks on records they already receive, follows "existing machinery first" and the fraud lesson.
- **C's allowance is held back** because the secure floor and LAB-10 already reach many of the same people; it stays an option.

**What would change this:** a CBO score far above the judgment here (narrow the replacement rate first, keep length); evidence that the 26-week floor lengthens joblessness more than the pandemic studies suggest.

## If you decide

- Section 4 writes the standards, the triggers, the wage-base schedule and the integrity checks, and the new agenda row is added.
- **Vehicle:** the benefit and tax changes are budget effects and can ride reconciliation (Byrd eligibility to check); the standards on state law may need the regular-order bill.
- **Preparation before 2029:** ask CBO for a score (point 15); a data agreement for identity and wage matching.
- **Seams:** clean power's transition guarantee counts unemployment benefits toward its 90% (`DEC-2026-11-13-06`), so higher benefits lower its top-up; memo 8's wage insurance runs through the same state offices.
