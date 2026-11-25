# Stage G step 9: the fiscal path revision for batch 3

Role: folds Espen's batch 3 answers (`DEC-2026-11-25-01` to `-11`) into the fiscal path review, redrafts what Espen sent back (G15 "a little more aggressive", G19 re-checked with a VAT allowed after the first years), checks the clean-energy credits' cost after FY2039 (Espen's question on G17), and answers the reviewer's open notes on step 8. Its forks are batch 4, memos [G23](memos/G23-debt-path-redraft.md) to [G25](memos/G25-cli1-after-the-fix.md), provisional until Espen confirms them. Status: **draft, stage G step 9, November 25, 2026. Nothing booked.** The tier-3 bookings (PH-3, the CLI-1 correction, then whatever batch 4 confirms) follow Espen's answers. Figures: [`notes/revision-results.md`](notes/revision-results.md) (`models/tools/fiscal_revision.py`) and [`notes/cli1-tail-check.md`](notes/cli1-tail-check.md) (`models/tools/cli1_tail.py`).

Units: federal fiscal years, nominal $B or % of GDP; central r − g (CBO's February 2026 rates), the conventional score. Project arithmetic on exploratory models, not official scores.

## In plain terms

1. **The clean-energy credits do phase down, as Espen suspected.** The budget model kept about $77-82B a year of them forever after FY2045. That was a modeling error: an old cost profile that never ends, from before the step-down was decided. On the decided statute the cost falls from about $53B in FY2040 to zero by FY2047 (ten-year production credits and storage and firm power started by 2039 are the real tail). Correcting it saves about $1.1T over FY2040-56 and lowers FY2056 debt from 133.1% to 131.6% of GDP. It also widens the thin years: the tightest margin goes from $0.4B (FY2042) to $9B (FY2040). The fix changes an adopted model input, so it is its own tier-3 PR.
2. **G19's money was overstated.** Re-scored on the 2025 law, G19 B's steps raise about $328B in FY2040, not $430-460B. Deduction limits are worth less now that the 2017 law's larger standard deduction is permanent, and a bigger carbon fee raises almost nothing for the deficit once its dividend is paid. So even G15 B as decided (flat at about 116%) needs about $130-170B more from somewhere in FY2040.
3. **A little more aggressive (G23 B, recommended): debt falling to 110% of GDP by FY2056,** about 1.0% of GDP of new deficit reduction phased in over FY2035-39 ($541B in FY2040). Against holding flat it costs about $85B more in FY2040 and saves $2.4T more interest by FY2056. On CBO's own estimate of how debt moves interest rates (2-3 basis points per point of debt), it brings rates down to about growth (r − g about 0.0 to +0.2 by the 2050s). Getting to 100% by FY2056 (G23 C) gets rates below growth on that estimate but costs about $790B in FY2040, 1.46% of GDP. The debt-path rule (G20 B) sends half of any good luck to the path, so B moves toward C if results beat CBO's assumptions.
4. **A VAT (G24): it doesn't beat G19 B's other steps on the household tests, but it is the only big source left that doesn't reverse G16 B.** At the same money, a VAT with a rebate leaves slightly fewer workers ahead on the take-home test than raising the health contribution, and fewer low-income workers. But G16 B (decided) holds the health contribution at 3.80% to FY2040 and steps it down after that, so the remainder can't come from it without undoing G16. **Recommended: G19 B's deduction limits and AGI surtax, then a VAT of about 4.75% from FY2035 with a rebate of $150 a point for every adult** (about $710 an adult in FY2040). Every fifth below the top stays ahead in FY2040 and FY2050. Workers ahead on the take-home test fall from 69% to about 51%, well short of the 85-90% target; every goal more aggressive than "flat" pays for itself partly out of that target.
5. **The populist start holds:** nothing new reaches the middle class before FY2035, seven years in. The VAT's enactment date is a point for Espen (G24).

## Part 1. What Espen decided, and where it is written

| Memo | Decided | Where it is written | Booked? |
| --- | --- | --- | --- |
| G15 | B, made more aggressive (`-01`); amends `DEC-2026-11-20-07`'s VAT part and `-24-18`: a VAT or broad measures allowed, not in the first few years | Memo G15's status; redrafted as G23 (part 3) | No: batch 4 |
| G16 | B (`-02`) | Memo G16; `4-fiscal-path.md` part 6 | Nothing to book up front (a trigger) |
| G17 | B (`-03`) | Memo G17; part 2 here (the CLI-1 check) | PH-3: with the tier-3 booking after batch 4 |
| G18 | D′ (`-04`), replacing held G8 | Memos G18 and G8 | A trigger |
| G19 | B, to be re-checked (`-05`) | Memo G19's status; re-checked as G24 (part 4) | No: batch 4 |
| G20 | B, points 1-3 (`-06`) | `5-budget-process.md` parts 3 and 8; its path follows G23 | No: a 2029 law; its path after batch 4 |
| G21 | A (`-07`) | `5-budget-process.md` part 5 | A 2029 commitment |
| G22 | Yes to all four (`-08` to `-11`) | `5-budget-process.md` part 6.1: D4's rewrite and D3's test years as proposal text | Rules, not bookings |

## Part 2. CLI-1's cost after FY2039 (Espen's question on G17)

[`notes/cli1-tail-check.md`](notes/cli1-tail-check.md) has the tables.

- **Where the tail came from.** CLI-1 in the budget model is a baseline row plus the climate export's redesign delta (`models/tools/climate-integration.py`). The baseline is the legacy credit set on its profile in `models/data/inputs/fiscal-profiles.csv`: 80% kept after FY2039, fading 4% a year, grown with GDP ("scale down as deployment saturates after 2039 (estimate)"). It never reaches zero. The delta, the redesign's saving, ends in FY2047, so from then on the booked cost is the old profile's tail alone, about $80B a year.
- **What the statute leaves** (`../../clean-power/4-specification.md`, CLI-1A.02): power credits for construction starts through 2037 (60% for 2035-37), storage and firm power through 2039, vehicles through 2034, low-income heat pumps, 45X and 48C through 2039. The energy model runs that schedule, with wind's production credit paid for ten years: $62.7B in 2040, $24.6B in 2043, $7.4B in 2045, nothing from 2047. That is the real tail.
- **The correction:** after FY2039, CLI-1 follows the energy model's decline from the booked FY2039 level: about $53B in FY2040, $21B in FY2043, $6B in FY2045, zero from FY2047. The FY2030-39 window is unchanged: it is calibrated to the ledger and G17 B's hold is decided on it.
- **What it saves:** $1,115B over FY2040-56, about $80B a year from FY2047; FY2056 debt 131.6% instead of 133.1%. The general fund's thinnest year goes from −$0.4B in FY2042 to −$9.2B in FY2040, so D4's annual test is less fragile in the early 2040s (`2-settlement.md` part 5).
- **It is tier 3:** the fix is one row in `models/data/inputs/fiscal-after.csv` (an adopted input), in its own PR. Everything in this file is priced on the corrected base, as a what-if until that row lands; the tools detect the booked row and don't count it twice.
- **G17 B's hold of FY2038-39 (PH-3) still stands.** The booked window rises in FY2038-39 because the export's saving narrows as the legacy credit set it is measured against ends. On the energy model's own shape the credits fall in those years anyway. So PH-3 works as a ceiling written in law at the FY2037 level: it saves $52B against the booked shape and costs nothing if the credits come in on the statute's path. Memo G25 asks Espen to confirm both points.

## Part 3. The debt goal, redrafted (memo G23)

**The base** is the booked settlement with CLI-1 corrected and PH-3: debt 117.7% in FY2040, 125.5% in FY2050 and 131.4% in FY2056.

**The reviewer's note on G15 B's level is right.** G19 B's first steps (deduction limits, the larger carbon fee, the outside fix) start in FY2037. They lower the debt carried into FY2040, so "held flat" holds 116.1%, not 116.9%.

| Goal | New deficit reduction | FY2040 | FY2050 | FY2056 | Interest saved FY2030-56 | Debt FY2040 / FY2050 / FY2056 | r − g in the 2050s, with CBO's feedback (not counted) | +100 bp from FY2035: debt FY2056 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A. Held flat from FY2040 (G15 B restated) | year by year, about 0.8-0.9% of GDP | $457B | $596B | $899B | $4.3T | 116.1 / 116.1 / 116.1 | +0.21 to +0.33 | 138.8 |
| **B. Falling to 110% by FY2056 (recommended)** | **1.00% of GDP, phased in over FY2035-39** | **$541B** | **$776B** | **$955B** | **$6.7T** | **113.6 / 110.8 / 110.0** | **+0.03 to +0.21** | **131.8** |
| C. Falling to 100% by FY2056 | 1.46%, FY2035-39 | $792B | $1,137B | $1,400B | $9.7T | 111.7 / 104.0 / 100.0 | −0.23 to +0.03 | 120.8 |
| D. Under 100% by FY2050 | 1.51%, FY2033-37 | $820B | $1,176B | $1,448B | $11.9T | 108.4 / 100.0 / 95.5 | −0.36 to −0.06 | 115.5 |

- **r − g.** On the conventional score the rate doesn't respond to debt, so r − g stays about +0.56 in every goal. Espen's aim, rates below growth on average, is about the feedback: CBO's working paper puts it at 2-3 basis points per point of debt [EV-FIN-076]. On that estimate B brings r − g to about zero in the 2050s, C just below it and D clearly below it. By the hard rule (`DEC-2026-11-25-11`) the feedback counts toward no goal; it is the risk each goal buys down.
- **The readings.** If rates run half a point below growth, B costs nothing and C 0.31% of GDP. If they run 1.5 points above it, B needs 2.38% and C 2.79%.
- **The shocks.** A +100bp shock from FY2035 leaves B at 132% in FY2056 unless the plan responds, and B would need 1.92% of GDP to stay on its path (C 2.34%). The rule's rate watch (`5-budget-process.md` part 3.5) starts the return plan early.
- **Why B.** Espen asked for "a little more aggressive", was "torn between B and A" in batch 3, and wants rates below growth. B lowers debt by about a quarter point a year from its FY2039 peak of 113.8%. It costs about $85B more than flat in FY2040, and can be paid for without the health contribution and without a VAT above 5% (part 4). C is the choice if getting rates below growth on CBO's estimate matters more than about $250B a year more from FY2040, most of it a larger VAT. Under G20 B, half of any lead goes to the path, so B is a floor that results can move toward C.
- **What the rule measures.** G20 B's path becomes the chosen goal's path, falling from the FY2040 peak in equal steps to its FY2056 level. The rule's mechanics don't change (`5-budget-process.md` part 3.1).

## Part 4. G19's mix with a VAT allowed after the first years (memo G24)

### 4.1 The sources, re-scored on the post-2025 law

CBO's December 2024 options were priced on a baseline in which the 2017 law's individual provisions expired after 2025. P.L. 119-21 made them permanent. The re-score is the agent's own rough arithmetic, not CBO's or JCT's (`models/tools/fiscal_revision.py`, header):

| Source | FY2040, re-scored | Step 8b | Why it moved |
| --- | --- | --- | --- |
| Limits on itemized deductions beyond C39 | $95B ($55-140B) | $123-312B | The larger standard deduction, the SALT limit and the top-bracket cap on itemized deductions are permanent: fewer itemizers and a smaller base, about 0.45 of the old yield |
| A larger carbon fee (buildings, non-road) | $15B ($0-30B) | $111-147B | Step 8b used CBO's economy-wide option. Most of its base is already priced by the booked fee and Moving America's fuel steps, and with a dividend that keeps the bottom two fifths whole, little is left for the deficit |
| An AGI surtax, 2 points above $100K/$200K | $190B ($160-215B) | $167-225B | AGI barely moves with the 2025 law; less the plan's avoidance allowance on the top rows |
| CRFB's SALT-workaround fix | $28B | $28B | Unchanged, to confirm against C39 |
| **G19 B, in all** | **$328B ($235-413B)** | $430-460B | |
| A broad VAT | $90B a point; $48B a point after a $150 rebate for every adult | $72-110B a point | Its base is consumption, which the 2025 law doesn't change |
| The health contribution R | $224B a point | $224B | |

**What remains unscored.** Every other row of the outside screen ([`notes/outside-proposals.md`](notes/outside-proposals.md)) is still CBO's December 2024 figure scaled to FY2040, on pre-2025 law; none enters a recommendation. These re-scores are working assumptions until JCT or CBO prices the plan's own versions: the deduction limits' 0.45 factor is the agent's reading of the 2017 law's effect on itemizing, not a measured figure, and the carbon increment rests on the energy model's economy-wide read.

### 4.2 The VAT's design: protecting low and middle incomes

- **A rebate for every adult of $150 a VAT point** (2040 dollars, indexed): the VAT on the first $15,000 of each adult's spending. It is paid through systems that already exist: with the child benefit, with Social Security and SSI, or as a refundable credit. Nobody applies and there is no income test (`DEC-2026-11-09-13`). At 4.75% it is about $710 an adult in FY2040. It costs about $42B a point, so a point nets about $48B.
- **Retirees and others on indexed benefits** are also protected if prices rise with the VAT, because Social Security and SSI rise with them (step 4's reading (a)). Fixed pensions and savings are not.
- **The base** is CBO's broad base less the care the plan pays for from 2035 (`packages.VAT_POINT_2040`).
- **D3 holds in every mix:** every fifth below the top stays ahead in FY2040 and FY2050 (`notes/revision-results.md` part 4).

### 4.3 The mixes, on goal B

| Mix | Plug | FY2040 money | D3 Q4 FY2040 / FY2050 ($ a household) | Workers ahead, take-home FY2040 | Workers below 200% of poverty ahead | Reaches the middle class |
| --- | --- | --- | --- | --- | --- | --- |
| 1. G19 B as decided, R last | R to 5.03% from FY2040 | $328B + $276B | +10,950 / +14,998 | 52.8% | 97.7% | FY2037 |
| **2. G19 B's deduction limits and surtax, then a rebated VAT (recommended)** | **VAT 4.75% from FY2035** | **$313B + $229B** | **+9,356 / +12,721** | **51.1%** | **92.0%** | **FY2035** |
| 3. A rebated VAT alone | VAT 9.47% from FY2035 | $28B + $456B | +6,699 / +8,881 | 41.9% | 83.6% | FY2035 |
| 4. As 2, VAT from FY2037 | VAT 5.21% | $313B + $251B | +9,053 / +12,285 | 50.0% | 91.4% | FY2037 |
| 5. As 2, VAT from FY2033 | VAT 4.37% | $313B + $210B | +9,607 / +13,081 | 52.0% | 92.8% | FY2033 |
| 6. As 2, R half a point higher | R 4.30% and VAT 3.00% | $425B + $145B | +9,934 / +13,582 | 51.4% | 94.6% | FY2035 |

The booked base: Q4 +12,998 in FY2040; 69.0% of workers ahead, 99.5% below 200% of poverty.

**Read across.**
- **At the same money, R does slightly better than a rebated VAT on the take-home test** (52.8% against 51.1%), and better for low-income workers (97.7% against 92.0%), because the health contribution exempts income up to 138% of poverty. The test counts workers only. A VAT also reaches retirees and spending financed from wealth, which the test doesn't see.
- **But R is spoken for.** G16 B (decided) holds it at 3.80% to FY2040 and steps it down from there on certified savings, and G13's backstop raises it if D2 misses. Mix 1 would take it to 5.03% in FY2040, reversing G16 B and stacking on G13's instrument. That is why the recommendation is mix 2.
- **Timing.** Each two years the VAT waits adds about 0.4 points to its rate: 4.37% from FY2033, 4.75% from FY2035, 5.21% from FY2037.
- **The take-home target.** No mix keeps 69%: any goal beyond "flat" is paid for partly out of the 85-90% target, as step 8 found. The target is reached later only through G16 B's step-downs, as certified savings appear.

### 4.4 The populist start and the VAT's enactment date

Nothing new reaches the middle class before FY2035 (mix 2) or FY2037 (mix 1). G20 B enacts the ladder in the first Congress (2029-30), on by default, which is what makes the money count and spares a later Congress a vote for a tax increase. For a VAT, Espen's reason for waiting (`DEC-2026-11-24-18`: "toxic until dems prove they can deliver consistently") points the other way: enacting it in 2029 puts it on the ballot in 2030 and 2032. Memo G24's point 2 asks Espen to choose. The recommendation is to enact it in the 2033-34 Congress with a FY2035 start. The other steps go in the first Congress, and the rule's return plan (G20 B) is the backstop if the VAT isn't enacted.

## Part 5. The reviewer's open notes on step 8

1. **The Bowsher line** (G20's draft let a CBO disagreement block a certified giveback). Corrected in `5-budget-process.md` part 3.8 and memo G20. CBO's reading is a published check with no legal effect. The tests' inputs are fixed in the statute, a giveback waits 60 days, and Congress can stop it by joint resolution.
2. **G15 B's level reads high once the FY2037-39 steps are in.** Right: 116.1%, not 116.9% (part 3).
3. **The CBO anchors in the evidence register.** EV-FIN-086 to EV-FIN-093: federal investment's return (CBO 2016); the ACA's labor-supply effect (CBO 2014); the immigration surge (CBO 2024); the 2025 law's dynamic effect ($125B; CBO's February 2026 outlook, Appendix A, not working paper 61257, which has no such figure); labor-supply elasticities (CBO 2012); CBO's 2026 rules of thumb; and two from CBO's 2025 letter on dynamic analysis. CBO 2019-01 and the Dallas Fed's 2513 were already EV-FIN-076 and -077. **Not entered:** CBO 2016's "about a third offset" isn't on the summary page read, so it stays unanchored until the report body is read. The 0.25 budget response is the registration's own figure, not CBO's (EV-FIN-091 says so).
4. **The outside tax options on the post-2025 law.** Re-scored for G19's sources (part 4.1). The rest is still unscored, and the outside screen says so.

## Part 6. Batch 4 (provisional)

| Memo | Question | Recommended |
| --- | --- | --- |
| [G23](memos/G23-debt-path-redraft.md) | The debt goal, more aggressive | **B**: debt falling to 110% of GDP by FY2056, 1.0% of GDP phased in over FY2035-39 |
| [G24](memos/G24-later-revenue-with-a-vat.md) | G19's mix with a VAT | **Mix 2**: G19 B's deduction limits and surtax, then a VAT of about 4.75% from FY2035 with a $150-a-point rebate for every adult; point 2: enact the VAT in the 2033-34 Congress |
| [G25](memos/G25-cli1-after-the-fix.md) | CLI-1 after the correction | **Yes to both**: book the corrected tail (tier 3), and keep G17 B's hold as a ceiling in law |

Nothing is booked until Espen confirms. The tier-3 bookings that follow are PH-3 and the CLI-1 row (already its own PR), then the confirmed goal's path in G20's law text and, once the sources are scored, the ladder.

## Method and sources

- `models/tools/fiscal_revision.py` (tests: `test_fiscal_revision.py`) on `fiscal_path.py`'s engine and the booked case `mixed`, with `cli1_tail.py`'s correction (tests: `test_cli1_tail.py`). D3 in the mature years is approximate (`5-budget-process.md` part 6.1; the tool's header). The take-home test is `take_home_vat.py`'s method with every new source counted.
- The energy model's decided credit path is `models/tools/energy/model.py`, case `decided` (`cli1_tail.py --engine` re-runs it).
- Sources: CBO's December 2024 budget options (SRC-1855) via [`notes/outside-proposals.md`](notes/outside-proposals.md); CBO working paper 2019-01 [EV-FIN-076]; the evidence entries in part 5.
