# Fair financing: milestone review of the settlement draft

Role: the independent adversarial review of stage G's settlement draft (stage G step 5; `charter/STANDARDS.md`, "Milestone review"; `.claude/skills/sessions/SKILL.md`, "The review pass"). It covers PR #469 at head `2f794d2`: `2-settlement.md`, memos G1-G9, `notes/settlement-results.md` and `models/tools/financing-protection/` (`packages.py`, `screen.py`, `test_packages.py`). #469 also carries #467's model fixes, which were reviewed separately; this review takes them as its base. The reviewer wrote none of the draft and tries to break it on weak evidence, missing populations, optimistic assumptions and cheaper alternatives. It also applies the design lens (`DEC-2026-11-09-13`), checks the fiscal-rule report against `DEC-2026-11-10-05`, and checks the "agent decisions" against "Who decides".

Status: current, as of #469's head `2f794d2` (November 20, 2026). Line numbers are at that commit, in `dossiers/foundations/fair-financing/` unless a path is given. Reviewer: Claude Code, `session_01UQzgBuzhC33rHj5zVGci31`. **This review changes nothing in the draft.** The fixes are for the author on #469, before Espen's decision batch.

Espen's earlier decisions are settled: `DEC-2026-11-15-01` to `-29`, `DEC-2026-11-16-01` to `-03`, and the stage E and F rows. The forks G1-G9 are provisional by Espen's stage G method, and this review does not settle them. Where a memo frames a fork wrongly or leaves out a real option, the review says so.

**Severity.** **Blocker:** must be fixed before the batch goes to Espen. **Fix:** fix on #469, but it doesn't stop the batch. **Note:** record or wording.

## Verdict

**Not yet a basis for Espen's decision batch. It is close.** The arithmetic is sound and reproduces exactly. The structure is right: health takes its share first, then the corrections, then the forks, with the VAT as the remainder. Most memos give real options with consequences. Five gaps remain, and each would change what Espen is choosing in G2, G3 or G8:

1. **B-1.** The VAT's price effect is assumed in one place and ignored in another.
2. **B-2.** The VAT's yield is CBO's base, but the plan takes most of that base's health care out of it.
3. **B-3.** The take-home test's blind spot is named but not shown.
4. **B-4.** The VAT's FY2033 start isn't justified by the rule, and it leaves the fourth fifth behind in FY2034.
5. **B-5.** The state table the audit asked for "for the batch" is missing, now that G1 A doubles the states' long-term care payment.

None of the five needs a new design. All five are restatements or added rows on the existing screens, about one session's work. Once they land, the draft can go to Espen.

**The HI grant correction (step 5) stands as an agent correction, with conditions** (F-1). It is consistent with HLT-7.22 and the budget model's conventions. It is not a disguised re-scoring, and it doesn't need Espen's decision. But its basis must be written down, and the obligation it moves must be disclosed.

## Checks run

A Standard-tier helper did these. I checked the outputs against the files.

- **The rebuild.** `bash models/tools/run-all.sh` (dry run) reported 0 changed files. `packages.py --markdown` and `screen.py --markdown` together are **byte-identical** to `notes/settlement-results.md`. `test_packages.py` passes 17 of 17.
- **No adopted input changed.** `git diff origin/claude/stage-g-2a-model-fixes..HEAD -- models/data/inputs/` is empty. The 17 files #469 adds on top of #467 are the dossier files and three files in `financing-protection/`. `recovery-budget/model.py` and `assumptions.json` are untouched.
- **The recommended package, year by year,** FY2030-56 (the helper's `years.py`):
  - Every year from FY2040 to FY2056 closes.
  - The thinnest margins: FY2043 −$0.6B (−0.001% of GDP), FY2056 −$8.7B, FY2040 −$11.4B, FY2050 −$12.7B.
  - FY2036-39 run +$175-227B short a year. FY2033-34 run $667B in surplus.
  - With the VAT held at 4.75%, the rule fails from FY2041, reaching +$279B in FY2056. That confirms memo G8's premise.
- **The VAT per household, FY2040 at 4.75%:** the code gives Q1 $2,035, Q2 $3,165, Q3 $4,296, Q4 $5,426, Q5 $7,687. These match `2-settlement.md:120` once rounded. They use the FY2034-35 mid-window household count, not an FY2040 count (N-6).
- **The FY2039 reading** (`2-settlement.md:121`, "about +$10,000 for the fourth fifth"):
  - Built by hand: Q-H7's FY2039 path, plus the package's non-VAT D3 edits, less the FY2039 VAT. It gives **+$9,650 to +$9,980**.
  - The year-by-year engine itself runs about $409 above the booked decade average for Q4. The cause isn't found; it may be the climate rows' own path in `annual_fraction`. So the true figure is probably nearer **+$9,250-9,600**.
  - "About +$10,000" is fair as a rough reading, but it is at the top of the range (N-5).
- **The $300 credit, the four cheaper designs, the states' payment and the avoidance allowance** were traced against `charter/decisions.md`, the governing record, the flagship memos and the code (findings F-3, F-4, F-5, F-7).

## 1. Blockers

### B-1. The VAT's price effect: assumed for households, ignored for the budget and Social Security

**Where:**
- `memos/G3-broad-source.md:30`: "Prices rise once by about the rate."
- `2-settlement.md:128`: "Social Security: unchanged."
- `models/tools/financing-protection/packages.py:57-64, 189-208`.

**What's wrong.** The memo tells Espen that prices rise by about the VAT rate. The budget screen books no effect of that price rise. The VAT row in `packages.py` is CBO's net yield and nothing else. There is no change for:
- Social Security's cost-of-living adjustment;
- SSI, federal and military retirement, veterans' compensation or SNAP's food plan;
- the plan's own indexed benefits (the child benefit, the secure floor's amounts);
- the income-tax brackets, which are indexed to the CPI.

The two readings can't both hold:
- **(a) Prices rise, and the Federal Reserve allows it.** Indexed spending rises by about the rate. Social Security alone is about 6% of GDP in FY2040 (about $3.2T on the model's $54.2T GDP). A 4.75% rise in its benefits is **about $150B a year**, before the other programs and the brackets. That is about 1.5-2 VAT points. Social Security's trust fund pays out more while its payroll base doesn't move, so it is **not** "unchanged". The trust-fund hold-harmless covers only the payroll-tax offset (`packages.py:61-62`, as a comment; no transfer is coded). On the other side, retirees on Social Security are protected by their cost-of-living adjustment. Retirees on fixed private pensions, annuities and savings are not.
- **(b) CBO's convention: nominal income held fixed.** The VAT then lowers wages and profits rather than raising prices. That is where the 25% offset comes from. Indexed programs don't move. But then "prices rise once" is the wrong thing to tell Espen. The burden falls through lower pay, and the consumption key in D3 is a modelling choice to state.

**The scenario.** Espen chooses between G2 A plus the VAT and G2 C (the 2 points folded into the contribution). Only the VAT raises prices. Under reading (a), the VAT's net yield to the general fund is overstated by up to a third. Under either reading, "Social Security unchanged" rests on an assumption the memo doesn't state.

**The size.** Up to about $150-200B a year in FY2040 under (a). Zero under (b), but then the memos' descriptions need rewording.

**The fix.** Pick one convention and say so in G3:
- CBO's convention (b) is the defensible default for the score.
- Add a disclosure row for reading (a): indexed outlays, the brackets, and Social Security's 75-year balance. Add it to the risk table (`2-settlement.md` part 5).
- Say plainly which retirees are protected (Social Security and SSI, by their cost-of-living adjustment) and which are not (fixed private pensions and savings).
- The hold-harmless transfer to the trust funds is a new statutory transfer. It should be named in the VAT row's specification, which G7 books (`2-settlement.md:215` already lists it).

### B-2. The VAT's yield is priced on a base the plan itself shrinks

**Where:**
- `memos/G3-broad-source.md:22`: "about $105B a point in FY2040".
- `packages.py:63`: `VAT_POINT_2040 = 105.0`.
- `2-settlement.md:170`: the "15% less" risk row.

**What's wrong.** The $105B a point scales CBO's 5% broad-base option. That option is $3.4T over 2025-34 in CBO's December 2024 report. The legacy menu's $3.5T over 2026-35 is the Committee for a Responsible Federal Budget's re-windowing of it (N-7).

As I recall CBO's option, its broad base excludes financial services, existing housing, schooling and services that government provides free. Health care is in the broad base; the narrow base excludes it. Under this plan, almost all health care is paid by the plan's fund from the January 2035 endpoint, with no fee at the point of use. Privately paid health care, through premiums and out-of-pocket costs, has been about 8-9% of personal consumption. That spending leaves the taxable base. Either it becomes untaxed government-provided care, or a VAT on it is the plan's fund paying the general fund, which nets to zero.

Child care and pre-K, partly public under care's design, shrink the base a little more. The risk table treats "15% less" as an outside risk. A base loss of roughly that size follows from the plan's own health design. It belongs in the central estimate.

**The scenario.** If the base is about 13-15% smaller from FY2035, the yield is about $90B a point in FY2040, not $105B. The recommended path needs about **5.5% rather than 4.75%** in FY2040, and about 7.3% rather than 6.3% by FY2051. Every "VAT points" figure in G1-G9 and in the README's table shifts with it.

**The size.** About $65-80B in FY2040 at 4.75%. About $130-150B in FY2056 at 6.3%.

**The fix.**
- Confirm CBO's broad-base definition from CBO's report (publication 60557), fetched through a search tool (`DEC-2026-11-08-10`).
- Take out the privately paid health spending that the plan replaces, plus the child care and pre-K share.
- Restate the yield a point and the rate path. Or, if the restatement isn't done before the batch, show the rate path as a range (4.75-5.5% stepping to 6.3-7.3%).
- Keep a separate compliance risk row on top.

### B-3. The take-home test's blind spot is named, not shown

**Where:**
- `2-settlement.md:107`;
- `memos/G2-the-two-points.md:23`;
- `memos/G3-broad-source.md:17-19`;
- `dossiers/foundations/checkpoint-financing.md:213`: a VAT "conflicts with the take-home test in a way that has to be shown".

**What's wrong.** G2 A is recommended because it is "the only option that keeps [the 85-90% test] with a margin" (`G2-the-two-points.md:42`). But the money it gives up is raised by a VAT, which the test doesn't count. The memos show average dollars by fifth: Q1 pays about $860 for two VAT points against about $30 for the 2 points. They never show the measure Espen chose, **the share of workers who come out ahead** on health costs plus the VAT that replaces the 2 points.

Retirees are missing entirely from the VAT discussion:
- They are "98.6% ahead" on the take-home test.
- They gain almost nothing from dropping the 2 points, which fall mainly on pay above $20,000/$40,000.
- They pay the VAT on everything they buy: about $2,000-4,000 a year in the bottom three fifths in FY2040.
- On B-1's reading (a), those on Social Security get it back through their cost-of-living adjustment, and those on private pensions don't.

People just above the exemption's phase-out at 250% of poverty pay the full 2.25% and the full VAT. That group isn't sized either.

**The scenario.** Espen picks G2 A to keep 88.7% of workers ahead. With the VAT counted, the share ahead could be far lower than under G2 C, which raises the same money with no price effect and an exemption below 250% of poverty. Then the recommendation reverses on Espen's own test.

**The size.** Not computed: no screen builds this number. The household model has the pieces: the take-home microdata, plus the consumption key the VAT's D3 row already uses.

**The fix.** Run the take-home test with the VAT's price effect added, for each of G2 A, B, C and D at its matching VAT rate (`2-settlement.md` part 4). Report:
- the share of workers ahead, and the share below 200% of poverty;
- the share of retirees ahead, split by income from Social Security or SSI against other income where the microdata allow, per B-1;
- the group between 250% and 400% of poverty.

Put the result in G2's options table beside the 88.7%, and say in G3 which test the recommendation rests on.

### B-4. The VAT's FY2033 start: not required by the rule, and the fourth fifth comes out behind in FY2034

**Where:**
- `memos/G3-broad-source.md:17, 25`;
- `memos/G8-later-years.md:19`;
- `2-settlement.md:79`.

**What's wrong.** The fiscal rule tests FY2040 and every later year (`2-settlement.md:81`). The VAT starts in FY2033, two years before health's endpoint. Rerun, the package runs **$168B and $499B in surplus in FY2033 and FY2034**. That is $667B collected from households before any of it is needed for the test, and in years when health's savings haven't yet reached households.

Q-H7's own fourth-fifth path is +$2,476 in FY2033 and +$3,932 in FY2034 (the helper's `q7series.py`). The VAT's gross cost to a fourth-fifth household at full rate in FY2034 is about $4,350. So **the fourth fifth is roughly $400 a year behind in FY2034**, and only just ahead in FY2033, about +$400 (rough, before the engine offset in "Checks run").

Neither G3 nor G8 offers a later start. The only reason given is the build time (FY2031-32). The decade reading improves with an early start, but the rule doesn't test the decade. G6 already shows that the decade figure is a matter of presentation, and debt passes either way.

**The scenario.** Espen approves "4.75% from FY2033" without seeing that FY2035 would meet the same rule, cost households about $590B less over FY2033-34, and keep the fourth fifth ahead in every year.

**The size.**
- About $590B less from households over FY2033-34 with a FY2035 start; the FY2040+ test is unchanged.
- The decade figure becomes about +$450B short, against −$140.5B. That is not a rule failure.
- Debt in FY2039-40 is about 1 point of GDP higher. It stays far below the baseline's 130-133%.

**The fix.** Add a start-date option to G3, or to G8's table: FY2033 (as drafted), FY2035 (with the endpoint), and FY2035 with FY2033-34 used only for registration and a 0% trial filing. Price each in `packages.py` (`opt_vat(start=...)` already takes the argument). Show the fourth fifth year by year for FY2033-36, not only the decade average.

### B-5. The state-by-state payment table that the audit said was "for the batch"

**Where:**
- `1-audit.md:180`, item 10: "Decide now (agent): a table of the combined state payment against states' current spending, for the batch."
- `2-settlement.md:201`: "G7 should tabulate ...".
- `memos/G1-who-gives-way.md:33, 35`.

**What's wrong.** G1 A doubles the states' long-term care payment, from 50% to 100%: −$148B in FY2040 and −$313B in FY2056. That is beyond every option the care dossier priced:
- HLT-7.17's range is 0-80% (`dossiers/care/4-specification.md:86`);
- care memo 3b priced 65% and 80%;
- care memo 17 priced only 65% (`dossiers/care/memos/17-cost-options.md:97`).

The memo makes two claims the repository doesn't support:
- **"No state pays more than it pays today" (`G1-who-gives-way.md:35`; repeated at `2-settlement.md:201`).** The payment is indexed. The spec says "to the plan's per-person cost growth" (HLT-7.17). The booked path grows with CBO's Medicare category, `out_medicare_net`, which includes enrollment growth (`models/data/fiscal-components.csv:55`). Nothing compares that index with each state's own long-term care cost path. A state with a younger or slower-aging population could pay more than its own spending would have been.
- **"The plan takes on all the growth" (`G1-who-gives-way.md:33`).** Under a per-person-cost index, the states' payment still grows with costs. The plan takes on only the enrollment growth and the new benefit.

The audit deferred the table "unless it shows a state's payment rising above today's". The settlement then moved it to G7, after the decision, and also raised the stakes.

**The effect on people served.** The memo says "people's benefits don't change". That is true of the plan's federal benefit. But a state paying an extra $148B (about $3B a state on average, far more in the large states) funds it from somewhere. It could come from optional state-only services outside the plan (housing supports, state supplements, behavioral health), from Medicaid's remaining roles (HLT-4.08), or from other budgets. The memo should say so.

**The legal side.** At 100%, the offset is collected against "any federal payment to the state" (HLT-9.09). That already goes beyond the Part D clawback's offset, which reaches federal Medicaid payments only. The memo's "moderate" risk should say that the larger payment is collected through the wider offset.

**The size.** $148B a year in FY2040, split unevenly across 50 states. No per-state figures exist.

**The fix.** Before the batch:
- Build the state table that item 10 asks for: health at 100% plus long-term care at 50%, 65%, 80% and 100%, against each state's current Medicaid health and long-term care spending, on the booked index.
- Flag every state whose payment would exceed its own projected spending.
- Correct the two claims above.
- Add 80% as a priced option in G1 (it is there in the results, −$88.8B, but only as a fallback in "What would change this").

## 2. Fixes

### F-1. The HI grant correction (step 5, −$85.2B): it stands as an agent correction, with its basis written down and its consequence disclosed

**Where:** `2-settlement.md:59, 185-191`; `packages.py:178-186, 281-292`; `models/tools/recovery-budget/model.py:175-179, 258, 285`.

**What it does.** The recovery budget charges the general fund a grant into HI's fund of 0.35 points of HI payroll, phased in from 2035 (`assumptions.json` `hi`). Its only effect is on the general-fund reading: it is in `fund_primary` (`model.py:285`) and not in the unified entries. Ending it lowers the general-fund gap and leaves debt unchanged.

**Is it a real correction?** Yes, on the plan's own decided design and the model's conventions:
- HLT-7.22, decided at `DEC-2026-11-10-11`, lists the plan fund's named streams: "Medicare's payroll tax and general revenue for Parts B and D ..." There is no general-revenue stream for Part A. The HI trust fund "is kept whole until the endpoint ... then folds in".
- `DEC-2026-11-15-29` puts any shortfall of the plan's fund on the general fund. So after 2035, a general-fund grant into HI is the general fund paying itself.
- #467 applied the same logic to H1a's and HLT-6's HI credits at the endpoint (`models/tools/funds-model.py:198-206`), and that was reviewed.
- The grant's amount was explicitly not adopted: "the 0.35-point illustration is not an actuarially verified adopted amount" (`models/data/inputs/recovery-adoption.json`, `architecture.hi`; "a final HI grant amount" is in `not_selected`).
- `models/tools/budget/CONVENTIONS.md:12` books benefits in full even after a trust fund is exhausted, so HI's current-law shortfall is already in the baseline, not in the plan's gap.

**Does it need Espen?** No. October 26's approved direction to "develop explicit general-fund support" for HI is overtaken by HLT-7.22's fold-in, a later decision by Espen. The governing record's standing rule is "latest controlling conflicts". G7 books it in a tier-3 PR in any case.

**What the draft leaves out.**
1. **The basis.** Part 6 argues from "the plan's fund is booked on the general fund". It should cite HLT-7.22's list of named streams, CONVENTIONS line 12, and the `not_selected` line. The README calls these corrections "step 2" (`memos/README.md:23`). They are steps 1-3 and 5.
2. **The obligation it moves.** At the fold-in, the plan's fund, backed by the general fund, takes on Part A's current-law shortfall. The funds model puts the Trustees' 75-year HI gap at 0.56% of HI payroll (`funds-model.py:374`). Under CBO's convention this isn't a cost against the baseline, which assumes the benefits are paid. But it is a real legal commitment the plan adds, of the same order as the grant it removes. A disclosure line should say so.
3. **"HI depletes in 2037 instead of 2038" (`2-settlement.md:129`).** This is a current-law comparison of a fund that no longer exists after January 2035. As written it reads as a plan result made worse by the package. Say it once as a comparison, or drop it.
4. **The risk row** "The HI grant correction is not confirmed" (+$73.8B, `2-settlement.md:169`). This review confirms the correction, so the row can go, or stay as "if a scorer counted the fold-in's HI shortfall as new".

### F-2. Combined downside: the package has no margin, and the backstop covers two risks of six

**Where:** `2-settlement.md` part 5 (lines 160-177); `memos/G5-d2-and-wealth-tax.md:21`.

**What's wrong.**
- The package is tuned to close at zero: FY2043 at −$0.6B, FY2056 at −$8.7B. Every risk row breaks the rule on its own.
- The risks are shown one at a time. A plausible joint case is the wage stack at the working elasticity (+$129B), pre-2025-law scores 10% low (+$124B) and B-2's VAT base (about +$70B). That is about **$320B in FY2040, about 3 VAT points, before D2 or HS2**.
- G5's backstop covers only D2 and the wealth tax.
- G5 doesn't show the VAT rate the backstop implies if it is triggered. Without D2 and HS2 it is about 4.75 + 3.7 = **8.5% in FY2040**, and 6.3 + 4.3 = **about 10.6% by FY2056**. With B-2 it is higher again.

**The fix.**
- Add a "joint plausible downside" row to part 5.
- Show the VAT rate on the backstop's full trigger in G5's table.
- Say in G5 and part 5 that the yield risks have no backstop, so a miss there falls on a later Congress. That is memo G8 option C's failure, the one G8 is meant to prevent.
- Consider a small margin target (for example 0.1% of GDP) as an option in G8.

### F-3. The avoidance allowance (step 3, −$63B): the range is misstated, and the low end is applied to non-wage income

**Where:**
- `2-settlement.md:57, 69`;
- `memos/README.md:37`;
- `1-audit.md:179`;
- `dossiers/foundations/health-household-contribution.md:180`.

**What's wrong.**
- The audit's working assumption was "10% on the withheld base below the surcharge and 20% above it, **with a range of 10-25%**". The settlement and the README say "range 5-20%". That puts the chosen 10% mid-range when it is the audit's floor.
- The step's reasoning ("income withheld at source is rarely misreported") fits wages. The health contribution's base rate falls on **all AGI**, and other income is "collected on the return" (`DEC-2026-11-15-10`). Self-employment, partnership and rental income is where misreporting is highest. A blended allowance on the base rate is likely above 10%.
- No `DEC-` row set the booked 20%, so this is an agent working assumption, as the draft says. But it is the third-largest agent step, about 0.6 VAT points.

**The fix.**
- Restate the range as 10-25%.
- Either split the base rate's allowance by income type (about 10% on withheld wages, 20% or more on other income), or keep 10% and widen the risk row to the range's top: 25% is about +$75-80B against the package.
- List it in the README's "What the batch rests on" with its real range.

### F-4. G1 B's prices: pre-K overstated, and the two wage-floor items may overlap

**Where:** `memos/G1-who-gives-way.md:44-48`; `packages.py:211-221`.

**What's wrong.**
- **Pre-K at 4 only: "saves about 35".** Care memo 11 gives $35B as the *cost* of the 4s-only design, not a saving. Option A costs about $60B at maturity and about $80B in FY2040 (`dossiers/care/memos/11-pre-k.md:32, 56, 67`). The saving is about $25B at maturity, or about $33B in FY2040 scaled, so $2-10B less than shown.
- **The $18 floor (memo 14 A, 33) and early educators without parity (memo 15 C, 41)** both change the same care wage floor for early educators. Memo 15 C's $12B is "Memo 14's floor only". If the floor falls to $18, part of memo 15's saving is already counted in memo 14's. The code adds them with no adjustment (`packages.py:211-221`).
- **The child benefit's 50** is memo 1's option A (with the $2,200 floor) less option C. The booked FAM-1 is the decided design without the floor (`DEC-2026-11-12-06`, point 2). It is close, but not like for like.

The other prices match their sources (secure floor memo 1, care memos 14 and 15).

**The size.** G1 B's $159B is probably $145-155B. That is 0.05-0.15 VAT points, and G1 B's VAT path moves a little.

**The fix.** Re-derive the pre-K saving on the booked FAM-2 path. Net the floor overlap. Note the child benefit's basis.

### F-5. G1's $300 credit: true, but the framing is stronger than the record

**Where:** `memos/G1-who-gives-way.md:24-29`.

**What's wrong.**
- "It was never adopted" holds. The governing decisions name "neither universal-credit amount" as not selected (`legacy/governing/project-2050-governing-decisions.md:450`). `recovery-adoption.json` lists it under `not_selected`. `models/tools/recovery-budget/README.md:170-176` says "neither is an adopted benefit".
- But the credit has been in every booked gap since October 26. `checkpoint-financing.md:98` lists "the recovery credit" inside the booked gap. Stage E closed with the checkpoint's figures "as booked" (`DEC-2026-11-16-04`). No row removes it.
- "It was meant to offset the payroll and income contributions for lower earners" is loosely supported. The budget's stated reasons are a coordinated household credit, visible early help, and a payment for people unable to work (`legacy/sources/recovery-and-solvency-budget.md:15, 108, 110`). The credit is universal and starts in FY2029, six years before the 2 points.
- "The protection it was meant to give now comes from the secure floor ..." is the memo's own inference. No dossier documents it as a replacement.

**Why it matters.** G1 ends a $300-a-head universal payment as "never promised" ($106B). G3 rejects a $350-a-head universal rebate ($95B) as "poorly targeted" and as needing "a payment channel to every adult". The credit already had one, so taken together this removes the VAT's natural offset. Espen should see the two side by side: G1 A plus G3 A is roughly a VAT with no offset, and keeping the credit is close to G3 B.

**The fix.**
- Soften the record claim to "carried in the booked gap without a decision".
- Restate the credit's actual purpose.
- In G3, cross-reference G1 and price "keep the credit as the VAT's rebate" as a variant of B.

### F-6. G3's alternatives: a targeted credit through existing channels is missing, and C is unpriced on the test that decides it

**Where:** `memos/G3-broad-source.md:15-20, 34-36`.

**What's wrong.**
- The only rebate offered is universal (B), and it is dismissed as poorly targeted.
- The design lens's own answer is missing: a VAT credit paid through channels the government already runs (`DEC-2026-11-13-08`, existing machinery first). That means SSI and Social Security (automatic under B-1's reading (a)), SNAP, the secure floor's child benefit and the childless EITC. It is cheaper than a universal rebate and reaches the bottom fifth without a new payment channel. One option of that kind should be priced, for example a credit of a set share of the bottom fifth's VAT cost paid with the child benefit and SSI, with the EITC for workers.
- **Option C** (a broad income contribution) is the main non-VAT alternative. Its take-home effect is "not priced here" (`G3-broad-source.md:19, 36`). With B-3's test it can be priced. Without it, Espen is comparing a priced option with an unpriced one.

**The fix.** Add the targeted-credit option (two to four options remain). Price C on the take-home test once B-3's screen exists.

### F-7. Memo G8: the step rule hands a tax rate to the trustees

**Where:** `memos/G8-later-years.md:24-27`.

**What's wrong.** A scheduled VAT step takes effect "unless the trustees certify that the gap it closes hasn't appeared". That leaves a tax increase to an executive finding. It is likely sound as contingent legislation, where Congress sets the rate and the trigger and an officer finds the fact (*Field v. Clark*, 1892; *J.W. Hampton*, 1928). But the memo states no legal basis and no fallback if a trustee certification is challenged. The same holds for G5's backstop triggers.

**The fix.** One paragraph in G8 and G5 on the legal footing and the fallback (the step takes effect by default). It is a drafting item for the settlement's specification, which G7 writes.

### F-8. G6: one reserve, two jobs

**Where:** `memos/G6-early-surplus.md:19, 25`; `memos/G5-d2-and-wealth-tax.md:31`.

**What's wrong.** The early surplus, about $660B plus interest, is offered as cover both for health's first years after the endpoint and for two to three years of a D2 shortfall. D2's budget starts in 2037, and health's first call is +$2.78T over FY2035-39. The general fund covers that call in the package, but the memo should say so. Otherwise the reserve looks as if it is spent once and counted twice.

**The fix.** One sentence in G6 and G5: the general fund covers health's FY2035-39 call, and the reserve is held for D2 and the backstop only.

## 3. Notes

- **N-1. The step names collide with the memo names.** "For G5 to check" (`2-settlement.md:59, 121, 185`; `notes/settlement-results.md:174`) means stage G step 5, this review, not memo G5. "G7 books" means step 7, not memo G7 (the education fund). A reader of the batch will misread both. Use "step 5" and "step 7" throughout.
- **N-2. Part 1's allocation is a quiet design choice.** Giving health "the most durable rows" (`2-settlement.md:30`) decides which flagships are exposed if G11 or G6 fails in court. It follows "health comes first" (`DEC-2026-11-15-04`) and moves no figure, so it is a fair agent choice. Say once in G5 that a failure of G6 or G11 falls on the rest of the plan, not on health.
- **N-3. The "Agent decisions, not in the batch" list is clean apart from F-3's range.** Steps 1 (GX), 2 (HCA at $70B), 3 (the allowance), 5 (the HI grant), the D3 payroll convention, the reading of record and the rebuilt screens are agent work. None is a fork that belongs to Espen. Every Espen fork (credit, states, cap, education rate, 2 points, VAT, steps, backstop, reserve, three small forks) is in G1-G9 with two to four options.
- **N-4. `test_inputs_untouched` guards memory only.** It compares in-memory copies (`test_packages.py:86-91`), not files. The file-level guarantee comes from the PR diff, which is empty for `models/data/inputs/`. That is enough for now. A one-line hash check of `models/data/inputs/` would make the test say what the settlement claims for it (`2-settlement.md:236`).
- **N-5. The FY2039 Q4 reading.** "About +$10,000" (`2-settlement.md:22, 121`; `memos/G3-broad-source.md:27`) is near the top of a likely +$9,250-9,980 range. Say "about +$9,500 to +$10,000". Note the year-by-year engine's $409 offset against the booked average as an item for the household model.
- **N-6. VAT per household uses the FY2034-35 household count** for FY2040 figures. A 2040 count would lower each figure by a few percent. Say so, or use the FY2040 count.
- **N-7. The CBO vintage.** The legacy menu's "$3.5T, 2026-35" (`legacy/sources/revenue-channels-and-full-menu.md:112`) is a re-windowing of CBO's December 2024 option ($3.4T over 2025-34). It is a pre-2025-law score, which the README already says. Cite CBO's own figure beside it.
- **N-8. Before FY2040.** FY2036-39 run +$175-227B short a year with the package (`2-settlement.md:79`). The draft says the 2030s run short. The plain-terms summary ("every year from FY2040 to FY2056 closes") is accurate. It should not be read as the decade closing.
- **N-9. A pre-existing figure gap.** `health-financing.md:244` gives the states' health payment at 100% as $689B in FY2040. `health-cost-review.md` and `checkpoint-financing.md:31` give $466B. The basis differs; B-5's table should use one figure.
- **N-10.** G1's "Medicare Part D's clawback, now at 75%", G3's VAT facts (OECD average about 19%; Canada 5%; Japan 10%) and G4's charge figures are correct as stated.

## 4. Brief checks, item by item

| Brief item | Result |
| --- | --- |
| 1. HI grant (−$85B): correction or re-scoring; Espen? | A real correction under HLT-7.22 and `CONVENTIONS.md:12`; it doesn't need Espen. Write down its basis and disclose the obligation moved (F-1) |
| 2. VAT: yield, offset, hold-harmless | Net of offset, as CBO. The hold-harmless is a comment, not code, but it is consistent. The price effect is unhandled (B-1). The base ignores the plan's health takeover (B-2) |
| 2. VAT: FY2033 start and steps | The steps are right in shape (they fail from FY2041 without them). The FY2033 start is unjustified, and Q4 is behind in FY2034 (B-4) |
| 2. VAT: distribution, retirees, the take-home blind spot | Named, not shown; retirees missing (B-3) |
| 2. Rebate or credit design | Only a universal rebate offered; targeted credits missing (F-6). G1 and G3 conflict over the $300 credit (F-5) |
| 3. Q4 +$3,458; FY2039 about +$10,000 | Decade figure reproduced exactly. FY2039 is about +$9,250-9,980 (N-5). Q4 behind in FY2034 (B-4). Retirees and the 250-400% of poverty group unshown (B-3) |
| 3. States under G1's long-term care shift | Unchecked claims, beyond the priced range, no state table (B-5) |
| 4. The $300 credit "ever booked" | Booked since October 26, never adopted; framing to soften (F-5) |
| 4. G1 B priced from the flagships' memos | Three of four match. Pre-K overstated; floor overlap (F-4) |
| 5. Optimistic yields, the C1 cap, D2, without both, the backstop | Single risks shown honestly. No margin; joint downside about 3 points before D2 and HS2; backstop VAT up to about 10.6% unshown (F-2). C1's $40B (30-55) is from the stack note; its high end is in the risk table |
| 6. Missing alternatives | VAT start date (B-4); targeted credit (F-6); G3 C unpriced (F-6). Slower flagship phase-ins don't help a permanent FY2040+ test, so their absence is fine. Smaller trims are in G1 B item by item |
| 7. Process | No adopted input changed. Numbers trace to model output, a source memo or a labeled assumption, except B-2's base and F-3's range. The agent list holds only agent decisions (N-3) |

## 5. What the author fixes on #469, in order

1. **B-1 and B-2** together: the VAT's convention and yield, restated or shown as a range. Every "VAT points" figure in G1-G9, the README and part 4 follows.
2. **B-3**: the take-home test with the VAT counted, for G2's options and for retirees. Then price G3 C on it (F-6).
3. **B-4**: the start-date option in G3 or G8, with the fourth fifth year by year for FY2033-36.
4. **B-5**: the state table, the corrected claims, and 80% as an option.
5. **F-1 to F-8 and the notes**, in the same PR.

Then a re-check of #469's new head by this reviewer or the standing reviewer, then the batch.

## 6. What this review did not do

- It didn't re-review #467's model fixes.
- It didn't fetch CBO's VAT option text. B-2's base definition and B-1's note on CBO's convention are from the reviewer's reading of CBO's past options, and the fix step should confirm them from the report.
- It didn't run the take-home microsimulation with the VAT. B-3 asks for that.
- It added no evidence entries.
