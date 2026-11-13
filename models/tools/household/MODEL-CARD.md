# Household model: model card

Role: the model card of `MOD-household`, the core model that measures taxes, benefits, poverty and distribution for real households (`charter/PLAN.md` 3.4). Status: **working** for the 2029 current-law baseline, the provision interface and the D3 report (with the secure floor's INC-1 to INC-5), the typical families and the 65-cent ceiling check; step M3, part 2. Owner: Claude Code (the M3 worker sessions), reporting to the lead. Generated results are in [`results.md`](results.md) and `results.json`; never quote a figure from this card that `results.md` no longer shows.

## What it answers, and what it cannot

It answers, at the 2029 current-law baseline (`DEC-2026-10-29-01`):
- **each household's budget**: market income, cash benefits, the main noncash benefits, federal income tax after credits, payroll tax and state income tax, for the 137 million households of the CPS (142 million aged to 2029);
- **distribution**: average federal tax rates and any provision's net effect by income quintile and decile, with the top 1% split out, on the D3 convention (below);
- **SPM-style poverty**: rates and counts for all people, children, working-age adults and people 65 and over, and the poverty gap, with the model's own taxes;
- **typical families**: the cents lost from each added dollar of earnings, layer by layer, for the three families the secure floor's 65-cent ceiling names (INC-5.02);
- **provisions**: every booked provision that has an incidence key, distributed by household group, for each scenario in `models/data/inputs/scenarios.json`.

It cannot answer, by design: behavior (work, take-up, migration or marriage responses to a provision); macroeconomic effects; anything below the national level except as a CPS state code; individual benefit determinations or official scores (`charter/PLAN.md` 3.4: "the toolkit never claims to produce official scores or individual benefit determinations"). See "What it does not do".

## What it replaces

| Legacy piece | What it did | Now |
| --- | --- | --- |
| `models/tools/incidence-model.py`, `incidence-years.py`, `incidence-make-md.py` → `legacy/index/revenue-household-incidence-model.md` | The D3 net test with typed distribution keys over 140 million households, its year-by-year profiles and its report | **Retired (M3 part 2).** `d3.py` is the engine: its legacy version gives the legacy figures exactly (tested against the last legacy run, `test-data/`) and writes `incidence.json` for the budget model's readers; its model version uses the measured keys. The year profiles are ported (`d3.py`, `series`), and the report's text is `results.md`, sections 5, 6 and 8. The legacy report is the scripts' last output, no longer regenerated |
| `models/tools/child-poverty/` → `legacy/sources/family-child-poverty-*.md`, `legacy/index/child-poverty-agenda-analysis.html` | Child SPM poverty on the CPS ASEC 2026, the agenda's family experiments, replicate-weight uncertainty | The same archive and SPM measurement (`extract.py` checks the same SHA-256), with taxes recomputed, for every age group and aged to 2029. The child-poverty tool's replicate-weight intervals, delivery and identification branches and its eight agenda cases are not yet ported (part 2) |

## Data

- **Source:** the Census Bureau's CPS Annual Social and Economic Supplement, 2026 public-use file (income year 2025), `https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asecpub26csv.zip`, SHA-256 `fe819d0d2fc4470c282e76c247b8aa8b6054811619730307e9f2fe6186707d93` (the hash `legacy/sources/family-child-poverty-cps-baseline.md` records). It is a U.S. government work.
- **The committed extract** (`models/data/household/`, 5 MB, built by `extract.py`): 72,979 tax units (Census `TAX_ID` within each household), 55,401 SPM units and 53,344 households. The archive itself (139 MB) is not committed; the extract lets the model and its tests run in the checks.
- **Units:** tax units for taxes (the Census's own assignment of filers, spouses and dependents); SPM units for poverty; households for distribution.
- **Why the CPS and not the legacy cells:** the legacy incidence model's keys are typed estimates "anchored to a published pattern; no row is yet a microsimulation" (its own words). The CPS has every element the D3 test and the SPM need for most keys, and the child-poverty tool had already validated the 2026 file against the Census's published rates. The ACS was not used: it lacks the SPM elements and the Census tax model's figures.
- **Weights:** person weights (`MARSUPWT`) for poverty, household weights (`HSUP_WGT`) for distribution, the head's person weight for tax units.

## Rules modeled at the 2029 baseline

All in `params.py` (parameters) and `tax.py` (calculator); 2025 values are the law as enacted, and 2029 values are indexed from them.

- **Income tax:** the 2017 act's brackets, made permanent by P.L. 119-21; the 0/15/20% rates on gains and dividends (all dividends treated as qualified); the standard deduction ($31,500 joint in 2025, P.L. 119-21 sec. 70102) and its additions at 65; taxable Social Security (sec. 86); the net investment income tax.
- **Credits:** the child tax credit ($2,200 in 2025, $2,400 in 2029, refundable up to $1,700 and $1,800, 15% of earnings above $2,500, phased out above $200,000/$400,000), the $500 credit for other dependents, and the earned income credit by number of children (childless workers 25-64).
- **The 2025-2028 items expire before 2029:** the $6,000 senior deduction is applied in 2025 and gone in 2029; the tips, overtime and car-loan deductions are not modeled in either year (the CPS cannot see them).
- **Payroll taxes:** Social Security and Medicare, both halves, the self-employment tax and the additional Medicare tax.
- **Benefits:** Social Security, SSI, TANF, unemployment insurance, veterans' benefits, SNAP, housing assistance, school meals, WIC and energy assistance, as the CPS reports them or the Census imputes them for the SPM. The model does not yet simulate eligibility for them, except SNAP for the typical families. In 2029, P.L. 119-21's SNAP changes are applied to the reported amounts (A-8).
- **Typical families:** SNAP's federal rules (FY2025 parameters uprated: the gross income test at 130% of poverty or a state's broad option up to 200%, the 20% earnings deduction, the standard deduction, an optional excess shelter deduction, 30% of net income); the premium tax credit on the 2010 act's schedule (2026 applicable percentages).

### Assumptions (labeled, with their basis and range)

| ID | Assumption | Basis | Range, and the cost of being wrong |
| --- | --- | --- | --- |
| A-1 | The CPS's 2025 households stand for 2029's: no change in who lives together, works or claims whom | Static aging is the standard first step (CBO's and TPC's models also age a base year) | Demographic change over four years is small next to the keys' uncertainty; a reweighting to CBO's age structure is a part 2 option |
| A-2 | Amounts grow 2025 to 2029 by type, with CBO's February 2026 projections: earnings with wages per payroll job (+15.8%), prices (+10.7%), interest, dividends and rents per household, capital gains with GDP per household; weights grow with CBO's households (+3.6%) | CBO's fiscal-year series (`models/data/cbo/`), standing in for calendar years | Earnings growing faster than the law's indices is what produces bracket creep and EITC erosion in 2029; a slower wage path lowers 2029's poverty rate |
| A-3 | Tax indexing uses CBO's fiscal-year chained CPI-U (FY2028 over FY2024) for the code's twelve months ending August | Gives $2,400 and $1,800 for the 2029 child credit; CBO's own path has $2,400 and $1,900 in 2030 | Off by at most one rounding step in a few amounts |
| A-4 | The Social Security wage base follows CBO's wages per job in place of SSA's average wage index | The two move together | A few hundred dollars on the base |
| A-5 | SPM thresholds grow with CBO's consumer spending per household (+13.6%) | The Census sets the thresholds from five years of spending on food, clothing, shelter and utilities, so they rise with spending, not prices | With prices instead (+10.7%) the 2029 poverty rate would be about 12.6% instead of 13.3% |
| A-6 | Units the Census tax model marks as nonfilers get no refundable credits | Keeps the Census's convention, so the SPM baseline stays calibrated | A full take-up run gives the same 2029 poverty rates to two decimals |
| A-7 | No itemized deductions, AMT or the dependent care, education, saver's and premium credits in the microdata | The CPS has no itemized deductions; the Census's own tax model imputes them | Income tax after credits is about 9% above the Census tax model's in 2025, most of it in the top quintile |
| A-8 | 2029 SNAP is 2025's, uprated, with P.L. 119-21's changes applied (`snap2025.py`). The wider work rule (sec. 10102) removes benefits from adults not disabled who worked under 20 hours a week, with probabilities calibrated so each group's loss matches CBO's participation estimate as a share of USDA's participants (EV-SEC-036, EV-SEC-039). The energy and internet changes (secs. 10103-04) are applied as CBO's expected amounts (EV-SEC-038). The Thrifty Food Plan rule (sec. 10101) needs nothing beyond price uprating. Not applied: the state cost share's state responses (about 300,000 people) and the noncitizen rule (about 90,000), which need behavior or immigration status the model lacks. The law's Medicaid changes stay with the health coverage model | CBO's section estimates (EV-SEC-034 to 038), which the secure floor already uses | The CPS records about $42B of 2025 SNAP against USDA's $95.8B, so the law's poverty effect is understated by about half. The model's cut is 10.1% of benefits, against about 9.8% implied by CBO's sections. CBPP counted 4.7 million fewer participants by March 2026, against CBO's 3 million for 2026 (EV-SEC-040); at that pace the loss would be larger |
| A-9 | The premium credit's 2026 applicable percentages hold in 2029 | The percentages are reindexed yearly; their direction depends on premium growth against income growth | A few tenths of a cent per dollar in the family rates |
| A-10 | State median income for FAM-2.01's charge is the CPS's median cash income of four-person SPM units, nationally ($160,852 in 2029) and in the lowest-income state ($98,693), scaled by HHS's size factors | HHS sets the lines from the ACS; the CPS has every state but small samples (at least 59 four-person units each) | The CPS's SPM-unit median runs above HHS's family median, so the charge may start lower than modeled; it moves the charge's start, not the ceiling's binding point at 100-125% of poverty |

## Distribution conventions

- **D3 convention (the fairness test):** households ranked by expanded cash income (cash income plus the employer's payroll tax) divided by the square root of household size, in quintiles and deciles of **equal numbers of households**, so a per-household average is comparable with the legacy model's. The top 1% is the top 1% of households on the same ranking.
- **Benchmark conventions:** tax units in quintiles of equal numbers of people (the Tax Policy Center's); households of equal numbers of people would be CBO's.
- The size adjustment is a model-design choice: an unadjusted ranking puts large families higher than their living standard warrants. It moves households between groups; it changes no booked amount.

## Provision interface

- **Inputs:** the budget model's `ledger.json` (each provision's FY2030-39 amount) and the adopted `incidence-rows.csv`, which books each row as a formula over ledger IDs and splits it across incidence keys (both read only).
- **Keys** (`keys.csv`): for each key, `micro` measures its shares on the 2029 baseline households (a household field, or a rule computed tax unit by tax unit in `rules.py`), and `legacy` keeps the typed key, with the reason.
- **Measured:** 20 keys. In part 1, 14: Earnings and capped earnings; people and adults; FAM-1's child benefit (the American Family Act's credit less today's child and other-dependent credits, household by household); housing assistance; Medicaid and marketplace coverage; Medicare (three keys); employer coverage; Social Security; energy assistance; and C20's surtax base. In part 2, the secure floor's six: INC-1's childless credit (`eitc_childless`, a rule), SNAP's 2025 cuts and SNAP before them (`snap_cut`, `snap`, INC-2), SSI received and SSI's indexed exclusions (`ssi`, `ssi_exclusions`, a rule, INC-3), and the refundable dependent care credit (`cdctc`, a rule, INC-4). INC-5's forgone rent offsets use housing's key. INC-4's rule measures about $0.3 billion a year of refundability against a $4.5 billion booking; `results.md`, section 6, gives the reasons the CPS may run low and the data that would settle it. INC-1.02 is read as moving no money: no family loses the earned income credit from the shared definition (the lead, on #320).
- **Kept, with the reason in `keys.csv`:** 29 keys, where the CPS cannot see the base: consumption and excises, capital and corporate income, the top-end taxes and the health coverage model's own keys.
- **The top 1%:** for earnings and the surtax, the top 1%'s share is the legacy key's, because the CPS top-codes high incomes. It finds 9% of earnings and 28% of the surtax base in the top 1%, against the legacy 12% and 55%.
- **Outputs:** net dollars per household per year, FY2030-39 average, by group, for every scenario, in the legacy model's arithmetic. They are divided by the model's mid-window household count: the CPS count grown to FY2034-35 with CBO's household growth, 147.1 million against the legacy 140 million.
- **Poverty effects** need a provision as a rule (`rules.py`), not a key. There are five: FAM-1's child benefit, C20's surtax, INC-1's childless credit, INC-3.02's SSI exclusions and INC-4's refundable care credit.
- **The secure floor's rows** (`incidence-rows.csv`, INC1 to INC5; `results.md`, section 6): INC-2 is split on CBO's sections of P.L. 119-21 (43.7% on the households the model cuts, 56.3% on SNAP households before the law); INC-3 on the booking's parts (75.5% on today's SSI recipients, standing in for new eligibles and for the territories, which the CPS does not cover; 24.5% on the exclusions rule). INC-4's rule nets out the child care guarantee: care of children under 5 counts only up to the guarantee's charge, with the CPS's national median income of four-person units standing in for state median income. Its keys were added to `incidence-keys.csv` as measured, rounded, so the legacy arithmetic runs on the same rows.

## Typical families

`families.py` computes, for a single parent of two, a married couple with two (one earner) and a single adult, the cents lost per added dollar of earnings from 50% to 300% of poverty: payroll tax, income tax after credits, SNAP and, as a variant, the premium credit, plus a variant with an excess shelter deduction (a $1,400 monthly rent in 2025 dollars). Medicaid and CHIP are cliffs and are listed apart. The "plan preview" adds FAM-1 and INC-1.01 only. It is not the 65-cent ceiling check, which needs every plan layer and is part 2.

What part 1 already shows, at 2029 law (`results.md`, section 4):
- **Without a shelter deduction:** the single parent and the married couple lose 52.7 cents at 100-125% of poverty (SNAP 24, the earned income credit's phase-out 21, payroll 7.7), as the dossier's arithmetic says. Their combined rate is 39-41 cents at 150-200%, where the credit's phase-out meets the 12% bracket. On the marketplace, that rises to about 55 cents.
- **With rent counted in SNAP's shelter deduction:** SNAP's effective rate is 36 cents, not 24. Each added dollar also shrinks the deduction by 50 cents. The two families then reach 64.7 cents at 100-125% of poverty under current law. **This matters for INC-5.02:** the memo's arithmetic used 24 cents.
- **In the plan preview:** removing today's child credit takes away the credit's offset to the 10% bracket at 100-125% of poverty, so those families reach 62.7 cents before any shelter effect.

**The ceiling check (INC-5.02; `results.md`, section 7)** adds every plan layer (`plan_budget`): paid leave's worker share (0.3%, 0.55% at its ceiling), FAM-1, INC-1.01, SNAP as INC-2 restores it, the premium credit in 2030-34 only, and child care's charge (FAM-2.01) net of INC-4's refundable credit. State median income, which sets the charge's lines, is the CPS's median for four-person SPM units: nationally and in the lowest-income state (assumption A-10). **Result:** met from 2035 without SNAP's shelter deduction (63.0 cents for families with children, 56.5 for the single adult); not met for families with children at 100-125% of poverty with the deduction (75.0 from 2035, 77.1 in 2030-34 on the marketplace), nor at 65.1 in 2030-34 on the marketplace without it. The results give two fixes' static costs for the lead's options.

## Benchmarks

| Benchmark | Model | Official or independent | Gap and its cause |
| --- | --- | --- | --- |
| SPM poverty, 2025, Census taxes (all / children / 18-64 / 65+) | 13.1 / 13.4 / 12.3 / 15.4% | Census P60-290, table 8 (SRC-3602): 13.1 / 13.4 / 12.3 / 15.4% | None: the model rebuilds `SPM_RESOURCES` from its elements exactly (tested) |
| SPM poverty, 2025, the model's own taxes | 13.2 / 13.4 / 12.3 / 15.4% | Same | +0.04 points for all people: the model's income tax is slightly higher (no itemized deductions, A-7) |
| SPM poverty, 2029 current law (model) | 13.3 / 13.4 / 12.3 / 16.0% | No official projection | The 2025 rates aged: earnings outgrow the tax law's indices (bracket creep and EITC erosion); thresholds rise with spending (A-5); the senior deduction ends (65+ up from 15.4 to 16.0%); P.L. 119-21's SNAP changes add about 0.06 points, 210,000 people (A-8; understated, since the CPS records under half of SNAP) |
| Earned income credit, 2025 law | $41.0B | Census tax model on the same records $40.5B; IRS SOI tax year 2023 (table 2.5) $66.3B on 24.4M returns | The CPS under-reports low and self-employment earnings and family links, and the IRS total includes claims its own compliance studies find improper; the model follows the Census on the same records |
| Child and other-dependent credits, 2025 law | $119.7B, of which $23.0B refundable | Census $118.8B ($23.6B); IRS SOI 2023 (tables 2.5, 3.3) $118.9B at the $2,000 credit ($34.5B refundable) | About 7% below SOI once SOI is put at the $2,200 credit; the refundable part is $11B lower, the low-earnings under-reporting again |
| AGI, 2025 | $16.0T | Census tax model $16.2T | 1% |
| Average federal rates by quintile, 2029: income tax / payroll, tax units with equal people (Q1 to Q5, top 1%) | −2.1/5.7, 2.1/10.0, 6.5/10.7, 9.8/11.4, 18.6/9.2; 28.7/5.4% | Tax Policy Center T26-0045 (June 2026; current law with P.L. 119-21): −3.7/6.1, −0.1/7.7, 4.5/7.7, 7.7/7.9, 16.2/5.5; 23.3/2.1% | The model's rates run 1.5-2.4 points (income) and 2-3.7 points (payroll) higher, mostly in the denominator. TPC's expanded cash income adds what the CPS lacks: employer health and retirement contributions, retirement-account earnings, imputed corporate tax and SNAP. TPC's income is $29.0T against the model's $21.9T. In dollars the model's income tax is lower ($2.68T against TPC's $3.15T), because the CPS top-codes and misses top incomes and gains; its payroll tax is higher ($2.16T against $1.89T), because CPS earnings run above the national accounts' wages ($15.8T against CBO's $15.2T). The ordering and the progressivity match |
| CBO, *The Distribution of Household Income, 2022* (January 2026), table 9 | — | Q1 −10.1% income tax, 9.5% payroll; top 1% 23.9% and 2.0% | Not comparable directly: a different year and law, and CBO ranks by income before transfers and taxes. Recorded for part 2's household-convention check |
| JCT | — | No distribution table under P.L. 119-21 yet (JCX-38-25 says its estimates were not ready); the latest, JCX-26-24, is pre-2025 law | Not used |

Sources: Census P60-290 is SRC-3600 (report) and SRC-3602 (table 8). TPC T26-0038 and T26-0045 are SRC-4800 and SRC-4801 (licensed, cited only); CBO 61911 is SRC-4802. IRS SOI's tax year 2023 tables 2.5 and 3.3 are at `irs.gov/pub/irs-soi/23in25ic.xls` and `23in33ar.xls`; `fetch_public.py` cannot read legacy `.xls`, so they are cited until it can. 

## Reconciliation with the legacy incidence model

Scenario Q (the decided package), net dollars per household per year, FY2030-39 (`results.md`, section 5, reconciliation table):
- The legacy model gives Q1 to Q4 +$8,889, +$6,433, +$3,323 and **−$527**. The household model gives +$9,595, +$5,477, +$3,301 and **−$327**. The **D3 result does not change**: the fourth quintile still comes out behind on scenario Q, and ahead on the base package alone (+$457 against +$340). These figures include the secure floor's INC-1 to INC-5 (part 2); before them, part 1 gave −$629 and −$420.
- **What moves the fourth quintile:**
  - the household count, 147.1 million against 140 million (+$25);
  - the earnings keys (+$143): the CPS puts 54% of earnings in the top quintile, against the typed 46%, so payroll-based costs (the paid-leave contribution, the education fund) fall less on the fourth;
  - FAM-1's key (+$50);
  - partly offset by the housing key (−$94): the CPS puts today's housing assistance 93% in the first quintile, against the typed 60%.
- **The second quintile falls by about $960 in all.** The housing key accounts for about $450 of it, the larger household count for about $310 and the other keys for the rest. Housing's key is a model-design choice, and the lead settled it on #318: the CPS-measured spread (today's assisted households, 93% in the first quintile) is the central case. The legacy key (60%) is a stated sensitivity in `results.md`: with it, Q1 is +$8,789, Q2 +$5,932 and Q4 −$233. If the housing dossier expects new awards to reach higher up than today's assistance, the sensitivity is the reading to use.
- **The top 1%** pays $639,233 a year against $671,627, from the larger household count.
- **What's still open:** the remaining typed keys (capital, consumption and the top-end taxes) dominate the costs, so the measured keys change the picture at the margin, not at the core. Replacing them needs tax data (TPC or CBO tables by key), part 2.

## What it does not do (limits)

- **No behavior:** take-up, work, avoidance and macro effects are out. New benefits are paid at full take-up; current-law credits follow the Census's filing status.
- **Benefits are reported or imputed, not simulated.** CPS under-reporting of SNAP, TANF and SSI is not corrected (the Urban Institute's TRIM3 does this; not available here).
- **No itemized deductions, AMT, or the dependent care, education and premium credits** in the microdata (A-7).
- **The top of the distribution is thin:** the CPS top-codes income and misses most capital gains, so top-1% results come from the legacy keys where it matters (`keys.csv`).
- **No health coverage values:** coverage enters only as counts for keys. The health coverage model owns premiums and out-of-pocket costs.
- **Year-by-year paths are shapes:** the phase-in profiles spread each row's ten-year total (`d3.py`, `series`); they are not scored annual paths.
- **No replicate-weight intervals yet:** sampling error on the 2029 rates is about ±0.3 points for all people and ±0.6 for children (the Census's 90% margins for 2025).

## Status and next steps

- **Working:** the 2029 baseline, the benchmarks above, the provision interface on legacy and measured keys, the D3 report and its year paths (`d3.py`; the legacy incidence scripts are retired), the secure floor's INC-1 to INC-5, the typical families and the 65-cent ceiling check.
- **Still to do:**
  - replicate-weight intervals;
  - a CBO-convention check against CBO 61911;
  - the child-poverty tool's agenda cases;
  - moving the budget model's readers from the legacy version to the measured keys (a visible change to their outputs).

## How to run

From the repository root:

```bash
bash models/tools/run-all.sh                                   # builds the ledger, runs the tests and the model
python3 models/tools/household/run.py --ledger build/ledger.json --out build/household
python3 models/tools/household/test_household.py               # 26 tests; the legacy check needs build/
python3 models/tools/household/extract.py --archive /path/to/asecpub26csv.zip   # rebuild the extract
```

## Tests

`test_household.py` covers:
- hand-checked tax cases: the brackets, the earned income credit, the refundable child credit, taxable Social Security, the child credit's phase-out rounding and the wage base;
- the 2029 law's values;
- the exact SPM identity and the Census's published rates;
- household accounting: net income equals its parts, and unit and household totals agree;
- equal-household groups and keys that sum to 100%;
- the FAM-1 rule, and the secure floor's: the 2021 childless credit, the care credit's rates and the guarantee's charge, the refundable part, SSI's exclusions, and SNAP's cuts as the key's base;
- P.L. 119-21's SNAP changes: the source year untouched, 2029's losses matching CBO's share, a cut of 8-12% of benefits;
- the typical families, and the ceiling check's layers, charge and verdicts;
- **exact reproduction of the legacy incidence model's last results** in every scenario, while its inputs are unchanged, and year profiles that sum to each row's total.

## Run log

| Run | Model version | Inputs | Provisions |
| --- | --- | --- | --- |
| `RUN-household-2026-11-13-a` | #318, merged as `13d4664` (M3 part 1) | CPS ASEC 2026 extract (SHA-256 above); CBO February 2026 economic projections; `incidence-rows.csv`, `incidence-keys.csv`, `scenarios.json` as on main | The ledger as built from main on November 13, 2026 |
| `RUN-household-2026-11-13-b` | The A-8 PR's head (M3 part 2, first piece: SNAP under P.L. 119-21) | As run a, with the SPM extract's four work-rule counts added | As run a; no provision result changes |
| `RUN-household-2026-11-13-c` | #320, merged as `e897ac6` (M3 part 2, INC-1 to INC-5) | As run b, with the extract's child care spending (`SPM_CHILDCAREXPNS`), children under 5 and 5-12, and SSI recipients' detail added (no existing field changes) | As run a, with `incidence-rows.csv` INC1 to INC5 and their keys |
| `RUN-household-2026-11-13-d` | #321, merged as `d204a85` (M3 part 2, the 65-cent ceiling check) | As run b | As run a; results section 7 added, no provision result changes |
| `RUN-household-2026-11-13-e` | M3 part 2, the legacy reports moved (this PR's head) | As runs c and d | As run c; `d3.py` in place of the legacy scripts; results section 8 added |
