# Decision Brief 2: Trims, Scope and the Fiscal Rule

Oct 20, 2026 · prepared for Espen · live doc: https://claude.ai/code/artifact/1c1b3c12-2cd6-4d76-b64a-4506c1f12ae1 (the live doc wins if they differ).

## Decisions recorded (Espen, Oct 20)

| # | Decision | Outcome |
| --- | --- | --- |
| 1a | Guardrails | **Agreed, sharpened:** measured against the real (CBO, adjusted) baseline, not held to the program's own debt. Total debt and net interest stay below the baseline, by more each decade. The sustainability layer is a reported track. **Confirmed:** permanent programs are still paid for from 2040 |
| 1b | Envelope | **Agreed:** 0.5% of GDP to 2034, tapering to zero by 2040, with the borrowing readings counted inside it. Espen: a ten-year deficit of $1-2T on a ~$10T program, mostly time-limited, is acceptable |
| 1c | Judgment Fund | **Agreed:** CLI-9 at full cost when obligated; AAJA damages as a disclosed contingent-liability line |
| 1d | Maturity test year | **Agreed:** FY2040 and every later year |
| 2 | Trims and scope | **Agreed:** every trim declined (too small to matter, too valuable to lose; some trims may be revisited later). LAB-9D; NSC-1A, with a study of reducing defense over time later in the project |
| 2b | CAP-7 (new) | **Restructured:** it was spread evenly (~$60B a year as increments). It is now a front-loaded surge, CAP-7S (the ~$0.6T over FY2030-35, borrowed inside the envelope), plus a lasting increase, CAP-7, lower than the surge (~0.12% of GDP from FY2032). Sizing (surge shape; sustained 0.12% of GDP) **confirmed by Espen as working figures**; the bottom-up agency review may revise it |
| 3 | Alternatives | **Agreed:** C38 accepted; C39 (TS12), C40 (HP1) and C41 (HP3) accepted; SC1 in reserve; HP2 folded into TS1 |

**Result after the rebuild.** The general fund runs a primary surplus of 0.07% of GDP from 2040. Its ten-year deficit is about $1.21T, almost all borrowing inside the envelope ($1.15T of $1.6T used). Total debt is 162.4% of GDP in 2056 against the baseline's 180.2%, and below it every year. The fourth quintile nets about +$1,269 a year (scenario Q). The figures below are the brief as drafted, before CAP-7 was restructured.

**Recommendation in one line:** write D4-B's guardrails relative to the baseline, size the envelope at 0.5% of GDP with the existing borrowing readings counted inside it, take none of the program trims, and pay the year-ten run rate with REV-TS12 plus two high-pay options (REV-HP1, REV-HP3). The model says this works: the general fund covers its permanent run rate from 2040 with about 0.04% of GDP to spare. Its own debt peaks at 1.6% of GDP in 2039 and is repaid in the 2040s. Every program stays whole.

## What this brief asks you to decide

Three things. The D4 choice comes first, because it sets what the trims have to achieve: under D4-B the test is the run rate in year ten and after, and a trim that only saves money inside the window does not count toward it.

| # | Decision | Recommended | Main alternative |
| --- | --- | --- | --- |
| 1a | How D4-B's debt guardrails are written | Relative to the baseline: the program's own debt peaks and falls, and total debt stays below the baseline path | Absolute guardrails plus a sustainability layer of about 2% of GDP |
| 1b | Size of the investment envelope | 0.5% of GDP to 2034, tapering to zero by 2040 (~$1.6T); C21, C30-C32 and C37 count inside it | 0.25% (~$0.8T) or 0.75% (~$2.4T) |
| 1c | Judgment Fund-backed contracts | Count them: CLI-9 at full expected cost when obligated; AAJA's damages as a disclosed contingent-liability line, bounded by CLI-3's cap | Treat both as off-budget until a judgment is paid |
| 1d | Which year "paid at maturity" is tested in | FY2039 net of time-limited lines, which in practice is the FY2040 figure, kept covered after that | FY2039 gross |
| 2 | Program trims | None: decline C5, C17, C34 and C36; take LAB-9D for national service; keep CAP-7 at $0.6T and NSC-1A | Take C36 and C17 (about 0.065% of GDP) |
| 3 | Alternatives to trims | REV-TS12 + REV-HP1 + REV-HP3 (about $0.54T; 0.12% of GDP in 2040) | TS12 alone; SC1 held in reserve |

All figures are 2030-39 totals in trillions or shares of GDP in the year shown. Every model figure is an estimate from index/tools/fiscal-model.py, run on the Oct 20 ledger with the alternatives added as extra rows (Basis and caveats, at the end). Decisions are yours. Once you decide, the ledger, the options register, the governing doc (D4 and the decision log) and the dashboard update in one pass.

## Where the numbers stand

On the planning basis plus the sprint (PB+S), the general fund is about $1.26T short over ten years. After $0.69T of borrowing readings and later-Congress rows, that leaves $0.57T on D4-A. In run-rate terms it is short 0.26% of GDP (about $134B) in 2039 and 0.08% (about $43B) in 2040.

**Most of the 2039 shortfall is time-limited.** Between 2039 and 2040 the balance improves by 0.18% of GDP with no policy change. Over that year Moving America's capital lines, HOU-1's emergency aid, LAB-5's credit and CLI-5's capital-heavy lines wind down. The permanent run rate the rule cares about is the smaller 2040 number.

| Scenario | GF balance 2039 (% GDP) | GF balance 2040 | GF balance 2045 | GF own debt: peak (year) | Total debt 2056 (% GDP) |
| --- | --- | --- | --- | --- | --- |
| Baseline (CBO Feb 2026, adjusted) | — | — | — | — | 180.2 |
| PB: Package B | 0.46 | 0.29 | 0.19 | 7.9 (still rising in 2056) | 171.3 |
| PB+S: plus the sprint (C38) | 0.26 | 0.08 | −0.03 | 3.1 (2044) | 165.2 |
| ALL: plus every trim | 0.09 | −0.01 | −0.11 | 1.2 (2039) | 161.9 |
| **Recommended: PB+S plus TS12, HP1, HP3** | **0.13** | **−0.04** | **−0.15** | **1.6 (2039)** | **161.5** |

Positive balances are deficits. "GF own debt" is the debt the program's general-fund side adds, with interest, as a share of GDP. The recommended package does slightly better on the long run than taking every trim. Its revenue grows with incomes, while C5's saving stops in 2040 and C36's shrinks with prices.

**What the total path looks like either way.** Debt held by the public rises in every scenario: 101.6% of GDP in 2026, about 125% in 2039, about 162% in 2056. The baseline's own rise (health costs, Social Security, interest) is about 2.5% of GDP of structural gap, and the program closes about 0.6 points of it, mostly through SS-1. That is why Part 1's guardrail question matters.

## Part 1. The D4 choice

### 1a. How the debt guardrails are written

**Recommended: write the guardrails relative to the baseline, and run a sustainability layer as a separate, reported track rather than a condition of D4.** As drafted, D4-B asks total debt to peak by the mid-2030s and fall through the 2040s. No version of this program can do that alone. The current-law path is rising for reasons the agenda does not touch.

| Option | The test | Passes on the recommended package? | What it would take |
| --- | --- | --- | --- |
| **A. Relative guardrails (recommended)** | (1) The general fund's own debt peaks by about 2040 and is repaid by about 2050. (2) Total debt is below the baseline path every year from 2030, and by more each decade. (3) Net interest is below the baseline's share of GDP. (4) The social-insurance funds are whole on 75 years. (5) No dynamic revenue is counted | Yes: own debt peaks at 1.6% of GDP in 2039 and is repaid in 2050. Total debt is 161.5% in 2056 against 180.2%. Net interest is 6.4% against 7.1%. Test 4 awaits the Social Security trust-fund module | Nothing beyond Parts 2 and 3 |
| B. Relative, plus a stabilization target | A's tests, plus a smaller layer of about 1% of GDP phased in over 2030-34 | Only with the layer: debt then reaches about 135% in 2056 instead of 162%, still rising | About $3.7T over 2030-39, or $0.45T a year by 2035 |
| C. Absolute guardrails (as drafted) | Total debt peaks by the mid-2030s and falls through the 2040s | Only with a layer of about **2.0% of GDP** phased in over 2030-34. Debt then peaks near 110% in 2033 and is about 108% in 2056. A 1.5% layer is not enough: debt still climbs to about 121% by 2056 | About $7.3T over 2030-39, or $0.90T a year by 2035 |

**Why A.** A 2% layer is larger than all the new general-fund revenue the agenda raises, and C's test would make every program depend on solving Medicare's and Social Security's long-run cost growth first. A is the honest version of "long arc": the program leaves the country with lower debt and lower interest than it would otherwise have, and the program's own borrowing is repaid. The structural gap still needs an answer, so A comes with a reported track. Each D4 test shows the remaining fiscal gap (now 1.84% of GDP on the recommended package), and the candidates sit beside it: health cost growth beyond HLT-5 and HLT-6, SS-5, and further revenue. That keeps the problem in view without holding the agenda hostage to it.

**What deciding A changes.** D4-B's guardrail sentence in the governing doc is rewritten as tests 1-5. The fiscal model's D4 table reports "total debt below baseline" in place of the two total-path tests that fail today.

### 1b. The size of the investment envelope

**Recommended: 0.5% of GDP to 2034, tapering to zero by 2040 (about $1.6T over 2030-39), with the borrowing readings already accepted (C21, C30, C31, C32, C37; about $0.55T) counted inside it.** That leaves about $1.05T of new room. Counting the readings inside gives D4 one borrowing ceiling instead of two, which is easier to explain and to police.

Each row below fills all the new room with investments that earn nothing, on top of the recommended package. That is the worst case: anything with the documented return D4-B requires does better.

| Envelope | Total room 2030-39 | New room after the $0.55T of readings | GF own debt: peak (year) | GF own debt 2056 | Total debt 2056 (baseline 180.2) | Net interest 2056 |
| --- | --- | --- | --- | --- | --- | --- |
| None | — | — | 1.6% (2039) | −2.0% (repaid 2050) | 161.5% | 6.40% |
| 0.25% of GDP | ~$0.8T | ~$0.25T | 2.2% (2039) | −1.4% (repaid 2052) | 162.1% | 6.43% |
| **0.5% of GDP** | **~$1.6T** | **~$1.05T** | **4.1% (2039)** | **0.8%** | **164.2%** | **6.51%** |
| 0.75% of GDP | ~$2.4T | ~$1.85T | 6.0% (2039) | 2.9% | 166.3% | 6.59% |

All three meet the relative guardrails: total debt stays 14-18 points below the baseline in 2056. At 0.5%, the program's own debt is not fully repaid by 2056 unless the investments return something. At a modest 2-3% a year it would be. 0.75% is the point where "time-limited investment" starts to look like a standing deficit allowance (D4-C by another name).

**Conditions to attach (recommended).** Only time-limited investments with a written return case, scored at enactment. Unused room does not carry forward. The envelope is available only while the paid-at-maturity test (1d) passes, so it cannot paper over a run-rate gap.

### 1c. Judgment Fund-backed contracts

**Recommended: yes, count them, in two different ways.** The Judgment Fund is a permanent, indefinite appropriation (31 U.S.C. § 1304; [Treasury](https://fiscal.treasury.gov/payments-from-government/judgment-fund/about)). Money paid from it needs no vote, so D4 cannot rely on appropriations to catch these costs.

| Exposure | What it is | Recommended treatment | Effect on the ledger |
| --- | --- | --- | --- |
| CLI-9: contracts for difference and advance purchase commitments | The project's own contracts, fully funded at enactment and backed by the Judgment Fund if a later Congress stops paying | Score the full expected net cost when the contracts are obligated (about $0.15T), as borrowing-eligible climate capital under the Oct 20 reading. The Judgment Fund backing then adds no new cost, because the money was counted at the start | None now: CLI-9 is a climate durability option, not in the ledger's totals; this sets how it is counted if it is adopted |
| AAJA Secs. 1401-1402: damages to permitted projects | The stipulated permitting law's damages, 25-50% of sunk costs (50-100% of construction cost for a pattern), paid without appropriation | Carry a disclosed contingent-liability line in every D4 test, with an expected cost estimated per policy that could trigger it (for instance, a fossil-permit action). Pass CLI-3's damages cap, which turns an open-ended exposure into a bounded one | A memo line, not a pay-for, unless a policy is chosen that makes payouts likely; that policy then carries its expected damages as a cost |

Alternative: treat both as off-budget until a judgment is paid. That is simpler but invites the charge that the project hides a liability it criticizes in AAJA.

### 1d. Which year "paid at maturity" is tested in

**Recommended: test the permanent run rate in FY2039 net of time-limited lines, which in practice is the FY2040 balance, and require it to stay covered in every later year.** The 2039 figure mixes in capital lines that end that year and are borrowing-eligible anyway. Testing gross 2039 would demand about $90B a year more revenue to pay for spending that stops 12 months later.

| Reading | PB+S | Recommended package | Every trim (ALL) |
| --- | --- | --- | --- |
| FY2039 gross (% of GDP; ≤ 0 passes) | 0.26 fails | 0.13 fails | 0.09 fails |
| **FY2040, then every later year (recommended)** | **0.08 fails** | **−0.04 passes** | **−0.01 passes** |

## Part 2. Program trims and scope

**Recommended: take none of the five trims, and settle the three scope rows as LAB-9D, CAP-7 at $0.6T and NSC-1A.** Measured by what D4-B tests, the trims are small. All five together improve the 2040 run rate by about 0.09% of GDP, and the largest of them, C5, contributes nothing after 2039. Each one also costs a design rule or the fourth quintile something. Part 3's revenue does the same job without those costs.

Each trim's effect below is measured by taking it out of the every-option package (ALL). Positive effects improve the balance.

| Trim | What it does | 2030-39 | 2039 balance (% GDP) | 2040 and after (% GDP) | 2056 debt (points of GDP) | What it costs | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C5 | Start Medicare dental after the window (HLT-A1) | $0.30T | 0.074 | **0.000** | 0.75 | Delays a benefit D6 keeps in. Pure timing: dental's full cost arrives in 2040 | **Decline under D4-B.** Keep it as the first fallback only if you stay on D4-A, where a ten-year saving is what counts |
| C36 | Meals at community-eligibility scale (EDU-3B) instead of universal | $0.19T | 0.040 | 0.040, easing to 0.032 by 2056 (meals are price-indexed) | 1.13 | Brings back the paperwork and stigma universal meals remove. Cuts about $175 a year from the fourth quintile's average gain (estimate from the incidence model's meals key), the group D3 binds on | **Decline.** The largest permanent trim, but it falls on the middle |
| C17 | Hold CAP-7's agency rebuild to $0.5T | $0.10T | 0.025 | 0.025 | 0.70 | Batch 4 already proposes $31B of the $37B reserve. At $0.5T the reserve goes, then FTA, then the CDC and NOAA placeholders, and batch 3 lines shrink. Cuts against "capacity first" | **Decline.** Keep $0.6T. Revisit once the agenda is fully priced, as D9 already says |
| C33 | National service at appropriations scale (LAB-9B, ~150,000 slots) | $0.07T | 0.018 | 0.018 | 0.50 | Reversible every year, so it fails design rule 2 | **Take LAB-9D instead** (below) |
| C34 | Safe Everywhere lean version (SAF-10D, ~$8B a year) | $0.03T | 0.007 | 0.007 | 0.21 | Cuts the compact titles by about a third for a rounding-error saving | **Decline** |
| **All five** | | **$0.69T** | **0.17** | **0.09** | **3.3** | | |

### The three scope rows

**LAB-9, national service.** Recommended: **LAB-9D**. Seek a bipartisan authorization at about LAB-9B's scale first, with the mixing requirement kept, as a regular-order bill. LAB-9A's R2 mandatory money is the fallback if it stalls. This fits capacity: AmeriCorps lost staff in 2025, and the labor file already says the ramp should start small. Fiscal effect: the ledger keeps LAB-9A's $0.12T (0.031% of GDP a year from 2033) until an authorization passes, so no saving is counted in advance. The alternatives are LAB-9A as chosen (R2 now), or C33 (smaller, reversible).

**CAP-7, the agency rebuild.** Recommended: **keep the ~$0.6T line (0.148% of GDP a year once phased in) and do not take C17.** This brief does not settle batch 4's $31B split of the reserve, which stays a separate call. If the line has to grow above $0.6T for batch 4, D9 already says matched revenue can pay for it.

**NSC-1, the defense base.** Recommended: **NSC-1A, flat real from the FY2029 base excluding one-time reconciliation money.** It costs nothing against CBO's baseline, which already grows defense with inflation.

| Option | 2030-39 claim | 2039 run rate (% GDP) | 2056 debt | Note |
| --- | --- | --- | --- | --- |
| **NSC-1A (recommended)** | 0 | 0 | 0 | Locks in whatever FY2027-28 produce, which is both its strength and its risk |
| NSC-1B: flat real from a 2026-28 average | Small; depends on FY2027-28 enactments | Small | Small | Smooths a volatile base |
| NSC-1C: flat share of GDP | About $0.89T (estimate: defense held at its FY2029 share, 2.61% of GDP, against the baseline's 2.28% by 2039) | 0.32 | About +8 points | Would cost more than the whole run-rate shortfall this brief is closing, about four times over |

## Part 3. Alternatives to trims

**Recommended: REV-TS12 plus REV-HP1 and REV-HP3, about $0.54T over 2030-39, all on the top 1% and corporations.** Together they improve the 2040 balance by about 0.125% of GDP against a 0.08% shortfall. They also lower 2056 debt by about 3.7 points, a little more than all five trims (3.3). Hold REV-SC1 as the next layer, and fold REV-HP2 into REV-TS1's drafting.

The live doc charts each option's effect on the 2040 balance. The same figures, largest first (trims measured out of ALL, alternatives added to PB+S; the PB+S shortfall in 2040 is 0.08% of GDP):

| Option | Kind | 2040 (% GDP) | 2030-39 |
| --- | --- | --- | --- |
| REV-TS12 (recommended) | Alternative | 0.093 | $0.40T |
| REV-SC1 | Alternative | 0.042 | $0.18T |
| C36 | Trim | 0.040 | $0.19T |
| C17 | Trim | 0.025 | $0.10T |
| REV-HP1 (recommended) | Alternative | 0.018 | $0.08T |
| C33 | Trim | 0.018 | $0.07T |
| REV-HP3 (recommended) | Alternative | 0.014 | $0.06T |
| C34 | Trim | 0.007 | $0.03T |
| REV-HP2 | Alternative | 0.005 | $0.02T |
| C5 | Trim | 0.000 | $0.30T |
| **TS12 + HP1 + HP3 together** | | **0.125** | **$0.54T** |

In ten-year dollars C5 is the second-largest item. In the year the rule tests, it is worth nothing.

| Option | What it does | 2030-39 mid (range) | 2040 (% GDP) | 2056 debt (points) | Who pays (D3) | Risks and overlaps | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REV-TS12 | Caps the value of itemized deductions at 28% for incomes above $450K | $0.40T (0.25-0.55), unscored | 0.093 | 2.8 | Households above $450K, roughly the top 1-2%. No quintile below the top | The 2025 law already caps the value at 35% for the top bracket. It overlaps G3, G9, C18 and SALT, so it needs a joint score before drafting | **Take.** It is the only single item that closes the run-rate gap, and it grows with incomes |
| REV-HP1 | Corporate surtax by CEO-to-median pay ratio (+0.5 points above 50:1, up to +5 points above 500:1) | $0.08T (0.04-0.15) | 0.018 | 0.5 | Corporations above $100M receipts; about a quarter on workers under the 25% convention | It rewards outsourcing low-wage work, so contract and franchise workers must count in the median. Stacks on G1 | **Take**, with the median fix |
| REV-HP3 | 21% excise on public-company top-five officers' pay above $1M, extending sec. 4960 | $0.06T (0.03-0.10) | 0.014 | 0.4 | About 7,500 executives (top 0.01%) and their firms | Pay shifts into forms the excise misses unless "pay" is defined as 162(m) defines it. Scored on top of TS1 | **Take**: your high-pay guardrail, with real money behind it |
| REV-SC1 | 45% bracket on income above $5M | $0.18T (0.10-0.25), scenario figure | 0.042 | 1.2 | Top 0.1% | Raises the combined top rate on wages from about 57% to about 62% (with SS-1 and H1b), and carries the most dynamic risk. Overlaps G3 and G9 | **Hold in reserve**, as the first fallback if TS12 scores low |
| REV-HP2 | Corporate deduction for stock options limited to the book expense | $0.02T (0.01-0.04) | 0.005 | 0.1 | Corporations and their shareholders | Mostly overlaps TS1 already | **Fold into TS1's drafting** rather than list it separately |

**If TS12 scores at the low end.** At the bottom of every range ($0.25T + $0.04T + $0.03T), the three together reach about 0.074% of GDP in 2040, just short of 0.08%. In that case add SC1, then C17. Neither touches the bottom four quintiles.

**Incidence check.** All three recommended items fall on the top 1% and corporations. The share of new general-fund revenue from that group rises from 72% on the planning basis, and no quintile below the top pays more. The incidence model should be rerun with the rows added before the package is final (D3).

## Packages compared

**The recommended package passes D4-B and misses D4-A by about $0.03T. If you stay on D4-A, add REV-SC1 to it.** Every row starts from the planning basis plus the sprint (PB+S). D4-A passes when the ten-year general-fund primary deficit is no more than $0.69T (the borrowing readings plus later-Congress rows). D4-B's maturity test passes when the 2040 balance and every later year are at or below zero.

| Package | Added to PB+S | Ten-year GF primary ($T) | D4-A | 2040 balance (% GDP) | D4-B maturity | GF own debt: peak (year) | Total debt 2056 (% GDP) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Nothing more | — | 1.26 | Fails by 0.57 | 0.08 | Fails | 3.1 (2044) | 165.2 |
| Every trim (ALL) | C5, C17, C33, C34, C36 | 0.57 | Passes | −0.01 | Passes, barely | 1.2 (2039) | 161.9 |
| Four permanent trims | C17, C33, C34, C36 | 0.87 | Fails by 0.18 | −0.01 | Passes, barely | 1.9 (2039) | 162.6 |
| **Recommended** | **TS12, HP1, HP3** | **0.72** | **Fails by 0.03** | **−0.04** | **Passes** | **1.6 (2039)** | **161.5** |
| Mixed | C36, C17, TS12 | 0.57 | Passes | −0.07 | Passes | 1.2 (2039) | 160.6 |
| Every alternative | TS12, SC1, HP1, HP2, HP3 | 0.52 | Passes | −0.09 | Passes | 1.1 (2039) | 160.1 |

**What the table shows.** TS12 does the work of all four permanent trims: the same ten-year total, the same 2040 balance, and a better 2056. Taking every trim passes D4-B only by 0.01% of GDP, because C5's money is gone by 2040. The "every alternative" row is the strongest, but it uses SC1, the reserve, which leaves nothing for a low TS12 score.

**The risk that sits outside the rule.** D4-B counts no dynamic revenue. On CBO-style dynamic feedback (about −$0.56T over the window), the recommended package's 2040 balance becomes +0.17% of GDP instead of −0.04%, a fail. Every package here fails that way, including every trim. The fixes are the ones Brief 1 already named: prefer base-broadening to rate increases and keep the cushion. That is one more reason not to spend SC1 now.

## Basis and caveats

- **Model runs (estimates).** Everything in % of GDP or 2056 debt comes from index/tools/fiscal-model.py on the Oct 20 ledger. The committed index files are unchanged; the regenerate check on Oct 20 shows no diff. Trims are measured by removing each one from ALL. Alternatives are added to PB+S as extra rows at their domain-revenue.md midpoints, starting in full in 2030 and growing with their revenue category. The alternatives are not in the ledger yet, so these runs are working files, not generated index files.
- **Scores.** TS12 is unscored (0.25-0.55, mid 0.40). SC1 is a scenario figure. HP1 is a haircut sponsor estimate, and HP2 and HP3 are rough. TS1-TS3 still need post-2025-law scores (C38 is three-quarters those). The recommendation holds at the low end only with SC1 added.
- **Envelope runs** assume the new investments earn nothing, so they show the worst case.
- **Sustainability layer** sizes are the smallest constant improvement, phased in linearly over 2030-34, that makes total debt peak by 2036 and fall every year of the 2040s on the full package. The 1% and 1.5% rows show the same layer at smaller sizes.
- **NSC-1C** holds defense discretionary outlays at their FY2029 share of GDP against CBO's baseline path (estimate).
- **Fourth-quintile effect of C36** scales the incidence model's universal-meals benefit for that group ($251 a year) by C36's share of EDU-3's cost (0.19 of 0.27) (estimate).
- **Not tested:** the 75-year social-insurance guardrail (needs the Social Security trust-fund module, on the later queue), and the incidence model with TS12 and the HP rows added.

## Sources

- index/fiscal-long-term-model.md and index/tools/fiscal-model.py, fiscal-profiles.py (Oct 20); index/2029-trifecta-master-ledger.md (Oct 20)
- governing/project-2050-governing-decisions.md and the live governing doc, https://claude.ai/code/artifact/817382ad-9f54-4875-b887-3eb601724c40 (D4, D6, D9; rev 182)
- governing/decision-brief-01-senate-rules-and-gap.md; index/options-register.md
- domains/domain-revenue.md (closing the gap, the sprint, high-pay guardrails, REV-SC1); domain-labor.md (LAB-9); domain-capacity.md (CAP-7); domain-national-security.md (NSC-1); domain-climate.md (CLI-3, CLI-9); domain-education.md (EDU-3)
- index/revenue-household-incidence-model.md (v1.4; the meals key)
- sources/permitting-aaja-2026-analysis.md (Secs. 1401-1402 damages)
- About the Judgment Fund, Bureau of the Fiscal Service, https://fiscal.treasury.gov/payments-from-government/judgment-fund/about (31 U.S.C. § 1304)
