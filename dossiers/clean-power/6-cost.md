# Clean, affordable power and a prepared country: cost

Role: section 6 of the clean power dossier. It prices the provisions of `4-specification.md` on federal fiscal years against the January 2029 law and against the legacy climate rows the budget model already books, and reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`). Status: reviewed (L2), on `DEC-2026-11-13-06` and `DEC-2026-11-13-07`, with the milestone review's fixes (`review-milestone.md`); L3 after the booking. **Not booked:** the booking is a later tier-3 step, after the milestone review (part 6 lists what it changes). Every figure is project arithmetic on the booked rows and the legacy models, not an official score.

## Counting rules

- **Conventions.** Federal cost on the general fund, nominal $ billion unless marked, a cost positive, against the January 2029 law (section 1, part F).
- **Fiscal years.** FY y runs from October of y-1. The booked rows are already on fiscal years.
- **The booked basis.** The budget model's central case (`mixed`), read at `6204281`; the climate rows are unchanged at main's head after #339 and #344. Read from its audit lines (`legacy/sources/recovery-budget-audit.csv`), not rebuilt: about **$1,811 billion over FY2030-39 and $164.9 billion in FY2040** for the sixteen climate rows (section 3's table, unchanged).
- **The path.** `tools/clean_power_path.py` (run: `python3 dossiers/clean-power/tools/clean_power_path.py`). It reads the booked rows, reads the carbon model for memo 1 B's coverage (`tools/coverage_read.py`, which runs `models/tools/carbon/` on the decided package and changes nothing in `models/`), and adds each decided change with its basis in the comments.
- **Revenue and spending stay apart.** The 24.4% income and payroll tax offset on the fees is its own revenue line (CX, CXP, `DEC-2026-11-12-08`) and is never added to a spending line (`dossiers/TEMPLATE.md`, "One basis for each fiscal figure").
- **Each figure's status** (commitment, working assumption, open question) is in part 7.

## 1. The decided set on the general fund, by fiscal year

| Line | Provisions | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fee and dividend accounting, as booked (CX, CXP, CLI-2O) | REV-C1, CLI-2 | 11.2 | 14.7 | 17.3 | 23.6 | 29.2 | 56.2 | 62.8 | 69.3 | 62.2 | 63.2 | **409.6** | **71.1** |
| Credits and industry, as booked (CLI-1, CLI-9) | CLI-1A, CLI-9 | 87.2 | 94.7 | 102.6 | 103.9 | 103.1 | 65.5 | 64.5 | 64.1 | 88.8 | 91.7 | **866.1** | **76.3** |
| Standards, as booked (CLI-3) | CLI-3A, CLI-4, CLI-14 | 0.9 | 1.8 | 1.9 | 2.0 | 2.0 | 2.1 | 2.2 | 2.3 | 2.4 | 2.5 | **20.0** | **2.5** |
| Grid, first tranche, as booked (CLI-10G) | CLI-10G | 3.6 | 3.6 | 3.7 | 3.8 | 3.9 | 4.0 | 4.1 | 4.2 | 4.2 | 4.3 | **39.4** | **0** |
| Bills and add-ons, as booked (CLI-5, 5L, 5W) | CLI-5 | 7.3 | 22.0 | 28.9 | 29.2 | 28.8 | 19.3 | 19.0 | 19.0 | 25.1 | 25.5 | **224.2** | **1.7** |
| Adaptation, as booked (CLI-7, 7K, 7C, 7N) | CLI-7, CLI-8 | 11.5 | 14.5 | 19.7 | 20.1 | 20.6 | 21.0 | 21.5 | 21.9 | 22.4 | 22.9 | **196.1** | **9.8** |
| Farms and forests, as booked (CLI-13A, 13F) | CLI-13 | 5.0 | 5.1 | 5.2 | 5.4 | 5.5 | 5.6 | 5.7 | 5.8 | 6.0 | 6.1 | **55.4** | **3.5** |
| **Booked legacy rows** | | **126.6** | **156.5** | **179.4** | **188.0** | **193.0** | **173.7** | **179.7** | **186.6** | **211.1** | **216.2** | **1,810.8** | **164.9** |
| Memo 1 B: the fee offset on receipts no longer charged | REV-C1G.01 | −5.2 | −7.1 | −8.7 | −12.4 | −15.8 | −19.2 | −22.2 | −25.5 | −26.4 | −27.2 | **−169.9** | **−29.1** |
| Memo 1 B: the add-ons' lost transition share | REV-C1G.01, CLI-2A.04 | 4.3 | 5.8 | 7.2 | 10.1 | 13.0 | 15.8 | 18.2 | 20.9 | 21.7 | 22.3 | **139.2** | **0** |
| Memo 4 B: the second tranche and the builder of last resort | CLI-10.01 to .03 | 0 | 0 | 0 | 3.0 | 6.0 | 8.0 | 9.0 | 10.0 | 11.0 | 13.0 | **60.0** | **0** |
| Memo 5 B: the bill credit, permanent from FY2040 | CLI-5H.01 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | **9.9** |
| Memo 7 B: the transition guarantee | CLI-11 | 0.7 | 1.4 | 1.7 | 1.9 | 2.2 | 1.7 | 1.1 | 1.0 | 0.9 | 0.8 | **13.6** | **0.7** |
| The transition share from FY2040 stays in the general fund (its waterfall draws are the memo 5 B and 7 B rows; `DEC-2026-11-13-13`) | CLI-2A.04 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | **−33.1** |
| **Change against the booking** | | **−0.2** | **0.2** | **0.1** | **2.7** | **5.3** | **6.2** | **6.1** | **6.5** | **7.2** | **8.9** | **43.0** | **−51.6** |
| **The decided set on the general fund** | | **126.4** | **156.7** | **179.5** | **190.7** | **198.3** | **179.9** | **185.9** | **193.0** | **218.3** | **225.1** | **1,853.8** | **113.3** |

- **The decided set:** about **$1.85 trillion over FY2030-39 and $113 billion in FY2040**, against $1.81 trillion and $165 billion booked: **about +$0.04 trillion over the ten years and about −$52 billion in FY2040.** The re-review on the energy model (`review-m4.md`, `DEC-2026-11-13-12`) moved only memo 7 B's timing (coal closes by 2035 on that model); every other line reconciles with it. Espen's decision on the transition share (`DEC-2026-11-13-13`, option A) keeps what the waterfall does not use in the general fund from FY2040: about −$33 billion that year against the ledger, which counts the whole share as spent (part 2). On the ledger's convention FY2040 would be about $146 billion.
- **Against section 3's estimate** (+$0.11 trillion; about $156 billion in FY2040), two things moved, both on the decided designs:
  - *Memo 7 B is priced bottom-up* on Espen's parameters, at about $0.014 trillion and $0.7 billion in FY2040, in place of the legacy session estimate of $0.08 trillion [EV-CLP-713] (part 1, memo 7).
  - *Memo 1 B is read year by year* from the carbon model: power and industry's share of receipts falls from 69% in 2030 to 58% in 2040 as power cleans up, so the offset saving in FY2040 is about $29 billion, not $26 billion.
- **FY2030 and the price's start.** The table uses the booked year shape, which starts the price in January 2030. Under CLI-2A.03 the price starts on the first quarter at least six months after enactment, July 1, 2030 on the working timeline, so FY2030's fee lines (receipts, the offset and memo 1 B's two rows alike) would be about a third of what the table shows. The net effect on the general fund is a few billion dollars in FY2030 and none after. The booking sets the shape (part 6).
- **The ranges** (part 5) are wide: about **−$0.06 to +$0.17 trillion** over FY2030-39 and **−$61 to −$34 billion** in FY2040 against the booking.

### Memo 1 B: the price on power plants and large industry

- **What the read says.** On the carbon model's decided package, power plants and industry pay about **$1.26 trillion of the fee's $2.00 trillion over 2030-39 (63%)**; buildings about $0.47 trillion and non-road transport $0.27 trillion [EV-CLP-714] (the read reproduces these exactly). Their share by year: 68.5% in 2030, 64.5% in 2035, 59.3% in 2039 and 58.1% in 2040 (the carbon model read). Industry's receipts keep rising with the price while power's peak in 2036 and fall as coal leaves.
- **On the booked basis.** The ledger books REV-C1 at $1.90 trillion, so under B about **$1.20 trillion is raised, $0.96 trillion returned and $0.24 trillion goes to the transition share** over FY2030-39. Each year's lost receipts are the booked receipts times one less that year's share.
  - *The offset (CX) falls* by 24.4% of the lost receipts: **about −$170 billion over FY2030-39 and −$29 billion in FY2040.**
  - *The add-ons lose 20% of the lost receipts* as financing, so the general fund pays that much more of their gross cost: **about +$139 billion over FY2030-39**. The booking ends the add-ons with the window, so nothing booked changes from FY2040 (part 2 says what that leaves out).
  - *Net:* **about −$31 billion over FY2030-39 and −$29 billion in FY2040**, section 3's −$0.03 trillion.
- **The threshold.** The read takes the model's whole power and industry sectors. REV-C1G.01 does not charge industrial facilities below 25,000 tons, which the model's industry includes, so the receipts and the dividend lean a little high. Each lost dollar of receipts lowers the offset by 24.4 cents and raises the add-ons' cost by 20 cents, so the general fund barely moves (judgment; the covered-facility count sizes it).
- **What the read is not.** The model prices every sector at one price; it cannot leave buildings unpriced. The read takes power and industry's receipts under the full package. Leaving buildings unpriced weakens their abatement in the model, which the clean-heat standard (CLI-4H.01) is meant to replace; that barely moves power and industry's own receipts. The O5 bridge (CLI-2O, CXP) keeps its booked accounts, since process emissions stay priced; part of Package A's combustion loss (CB1) is in buildings, which B no longer charges, so the rerun in the booking step should, if anything, improve the bridge slightly (judgment).
- **The dividend.** About **$133 an adult in 2030, $439 in 2035 and $492 in 2040** (nominal), against $195, $681 and $847 on the economy-wide fee: about a third smaller in 2035 [EV-CLP-706]. It is paid from the fee in its own channel and does not touch the general fund.

### Memo 4 B: the second tranche and the builder of last resort

- **The second tranche** ($40 billion of grants, $200 billion of loans, $40 billion of capacity contracts, CLI-10.01) at the first tranche's ratio of deficit cost to instruments (about $32 billion for $145 billion [EV-CLP-717]): **about $60 billion over FY2030-39**, released only on milestones, so none before FY2033 on the working path. Range **$0 to $80 billion**: zero if no milestone is met; the top end adds the builder of last resort's start-up, which is small because the eastern corporation starts lean and grows only with the lines it takes on (`DEC-2026-11-13-10`); its lines are financed by its bonds and repaid from their rates (part 2).
- **Time-limited capital** under the fiscal rule's investment envelope (D4-B), ending with the window like the first tranche: **zero in FY2040**.
- **The public builders' borrowing** (CLI-10.02) is repaid from the lines' rates. How the budget counts it is in part 2.

### Memo 5 B: the automatic bill credit

- **In the window, inside the booked line.** Reaching about half of eligible households, three times today's 17% [EV-CLP-038], takes about $12 billion a year against LIHEAP's $4 billion [EV-CLP-035]: about $8 billion a year more, $0.08 trillion over FY2030-39, inside the add-ons' $0.12 trillion for energy, Weatherization and water help [EV-CLP-721]. Range $0.05-0.12 trillion, so the line holds it at every point in the range.
- **From FY2040, new money.** The add-ons are time-limited and the credit is permanent: **about $9.9 billion in FY2040** ($8 billion in 2030 dollars, grown 2.2% a year), range $6-14 billion.
- **What the figures assume, and who is matched.** Two working assumptions (judgment): reach rises in proportion to money (three times the money, three times today's reach), and the credit grows 2.2% a year with energy prices. The money starts in FY2031, when R3 carries it (first credits in winter 2030-31); FY2030's share of the booked line is unspent, which the booking records. The match is likely larger than "about half" of eligible households: LIHEAP's 5.9 million households at 17% imply about 35 million eligible [EV-CLP-038], and SNAP alone serves about 22.6 million households in an average month [EV-CLP-054], before SSI, FDPIR and LIHEAP's own households, and more over a year. With 25-30 million households matched (judgment), $12 billion is about **$400-500 a household**, below today's average benefit and short of 6% of income for many (project arithmetic). CLI-5H.01 therefore makes the $12 billion a fixed sum, with every credit scaled down in proportion if the matched credits exceed it (a working choice: the cost is known and the formula published). Guaranteeing each matched household the 6% target instead would cost roughly $15-20 billion a year (judgment); that would be a change for Espen, not a working choice. The standard's payments (part 2) add to the sum from the mid-2030s. The 2027-28 preparation match sizes it.

### Memo 7 B: the transition guarantee, on Espen's parameters

Priced bottom-up in `clean_power_path.py`, every input a working assumption labeled there. In short:

| Input | Working assumption | Basis |
| --- | --- | --- |
| Covered layoffs, contractors included | 80,000 over FY2030-39: 14,000 a year in 2030-34, 2,000 a year in 2035-39 (range 50,000-130,000) | Coal capacity of 172 GW in May 2025, scheduled to fall to 145 GW by the end of 2028 [EV-CLP-508]. On the energy model the decided set leaves 31 GW of coal in 2030 and none by 2035 (127 and 89 GW under current law), while gas plants stay open and run less (591 GW in 2030, 699 GW in 2040; `models/tools/energy/results.md`), so closures come early: coal plants at about 0.18 jobs a megawatt plus a quarter for contractors (judgment), most of 44,060 coal mine jobs [EV-CLP-500], then refineries and gas processing |
| Take-up | 85% | Automatic from records |
| Paths | 25% aged 55 or more; of the rest, 65% re-employed, 25% in training | Judgment |
| Prior pay, after the cap at twice the median wage | $90,000 in 2030, +3% a year | Judgment |
| New hourly wage | 30% below the old one | UK miners' hourly wages fell 40% [EV-CLP-517]; Canadian coal workers' earnings fell 32% and recovered [EV-CLP-518] |
| Hours worked | 80% of the old schedule, 20 of 24 months | Judgment |
| Unemployment benefits | 35% of capped pay for six months, counted toward the 90% | Judgment |
| Pension bridge | Treasury reimburses a plan's waiver: about $170,000 a worker with a defined-benefit plan (60% of those 55 or more) | Judgment |
| Lost local and tribal tax and royalty revenue | $0.15 billion for each 8,000 closures, replaced in full, then 10 points less a year | Judgment; Rosebud County's plant and mine property was $76 million of $95 million taxable [EV-CLP-514]; the Navajo Nation's and Hopi Tribe's losses [EV-CLP-534] |

- **Result:** about **$14 billion over FY2030-39** and **about $0.7 billion in FY2040**: front-loaded, because coal closes by 2035 on the energy model. Range about **$6-40 billion** over FY2030-39 and $0.3-5 billion in FY2040.
- **Why it is far below section 3's $0.08 trillion.** The legacy figure was a session estimate for guaranteed pensions, health care and an energy-communities fund, with no derivation [EV-CLP-713]. The decided design has no separate health guarantee (the care plan covers health), pays the top-up only on hours actually worked, caps pay at twice the median wage, and counts unemployment benefits toward the 90%. Each of Espen's parameters lowers the cost; only covering contractors raises it.
- **It is paid first from the transition share** (CLI-11.08), which then finances that much less of the add-ons, so the general fund carries it either way.
- **The gas fleet.** The 8,000 rests mainly on coal. CLI-11.01 also covers gas-fired plants, and under 100% clean power by 2040 unabated gas must stop serving retail sales or pay the standard's payments, so closures in 2036-40 may run above the count. The range's top ($40 billion over FY2030-39; $5 billion in FY2040) is that case. EIA's gas fleet data and plant employment would replace the judgment (`4-specification.md`, "Evidence still needed").
- **The cost of being wrong:** a few billion dollars a year at most. It does not change the choice; it changes section 9's description of the guarantee as "cheap next to the rest of the dossier", which it is.

## 2. What the total leaves out

| Item | Provisions | FY2030-39 | FY2040 | Basis | Firm or contingent |
| --- | --- | --- | --- | --- | --- |
| The credits' cost risk | CLI-1A | about +$0.27 trillion on the energy model; up to about +$0.74 trillion on the legacy model | about +$8 to +$50 billion | The energy model counts the decided set's credits at about $1.03 trillion over FY2030-39 before the standby builder, and $1.19 trillion with the extra credited wind, solar and storage its lines connect, against the booked $0.76 trillion (`models/tools/energy/results.md`, item 5; a cross-check, not a score); the legacy carbon model counted $1.50 trillion [EV-CLP-710]; the IRA's credits ran far above their first score [EV-CLP-200] [EV-CLP-201]. The trigger (CLI-1A.03) limits it | Contingent; the trigger bounds it |
| The reinsurance facility's exposure | CLI-7C.01 | $0-150 billion in a bad year, recouped | same | $75-150 billion of contingent liability, disclosed in every fiscal test, never scored [EV-CLP-718] | Contingent |
| Disaster appropriations outside the baseline | — | about $150-250 billion | about $15-25 billion | Current-law exposure that recurs outside CBO's extrapolated baseline [EV-CLP-720]; not this plan's cost | Reported beside the test |
| Permit-certainty damages | CLI-3A.03 | $0 to the cap | same | Only if the bipartisan package becomes law; the cap bounds what the Judgment Fund pays [EV-CLP-255] [EV-CLP-256] | Contingent |
| The standard's payments | CLI-3A.02 | about $0.16 trillion, collected and paid out ($0.07 trillion with the permitting package) | about $40 billion, collected and paid out ($20 billion with the package) | Suppliers short of the decided path (80% by 2035, 100% by 2040) pay the $40 cap (2025 dollars) on each missing megawatt-hour. On the energy model (MOD-energy, `models/tools/energy/results.md`) clean power reaches 73% in 2035, 88% in 2040 and 92% in 2045, held back by grid access, not price; the payments run $9 billion in 2032 rising to $40 billion in 2040, then $19-35 billion a year to 2050. The legacy carbon model, which assumes the permitting package, gave $0.11 trillion and $29 billion (`tools/coverage_read.py`); the energy model with the package gives $0.07 trillion and $20 billion, lower because its standby builder adds lines. Treasury collects them and pays them to the bill credit (CLI-3A.02), so they net to about zero on the general fund, except that an excise-like receipt may carry the 24.4% offset (`DEC-2026-11-12-08`): up to about $10 billion in FY2040 if it applies. The energy model applies none ("a capped compliance payment, not a tax") | A receipt and an outlay; the offset is the booking's question |
| The transition share after FY2039 | CLI-2A.04 | — | about $33 billion a year raised | Under B the 20% share is about $33 billion in FY2040 on this tool and on the energy model alike. The ledger books CLI-2's outlay as the whole fee (`models/tools/ledger-build.py`), so from FY2040, when the add-ons end, the share counts as spent though nothing is funded. The statute's waterfall (CLI-2A.04) pays the guarantee and the bill credit from it first (about $10.6 billion in FY2040). Espen decided the remainder, about $23 billion, stays in the general fund (`DEC-2026-11-13-13`, option A; `review-m4.md`, R-3). Part 1 counts it as a −$33.1 billion row in FY2040, because the waterfall's draws are already the memo 5 B and 7 B rows | Decided (waterfall, CLI-2A.04; remainder, `DEC-2026-11-13-13`) |
| The public builders' borrowing | CLI-10.02, .03 | not counted | not counted | TVA's, Bonneville's and WAPA's capital spending shows in federal outlays as it is built and is repaid from rates over decades. How much more they build under the higher limits is not known; at $5-10 billion of added capital a year it would add that to outlays in build years and return it later (judgment). Not costless: WAPA's program and DOE's Transmission Facilitation Program both forgive any balance a line's rates have not repaid at the end of its life [EV-CLP-465] [EV-CLP-466]. WAPA's program at $10 billion (CLI-10.02) covers a few large lines at most. Needs CBO's treatment of the power marketing administrations and TVA checked before the booking | Timing, with a contingent cost; to check |
| The O5 bridge's rerun | CLI-2O.01 | small, probably favorable | small | Part 1, memo 1 | To rerun in the booking |
| The dividend's administration | CLI-2A.01 | under $2 billion | under $0.2 billion | A second payment on the child benefit's file (judgment); the IRS's rebuild is CAP-7 | Firm, left to the booking |
| No offset of the dividend | CLI-2A.02 | about $0.01 trillion | about $1 billion | Judgment, on the child benefit's FAM-1.07 line ($1-3 billion a year for a larger payment) | Firm, not counted |
| The inventory duty | CLI-14.02 | under $1 billion | under $0.1 billion | EPA's inventory and reporting staff; inside EPA's base appropriation (judgment) | Firm, not counted |
| Extending the guarantee to oil and gas field workers | — | about $0.01-0.05 trillion if extended | a few billion | Not in the decided design (`4-specification.md`, "Where particular groups fall"); judgment | Not decided |
| Bill protection's sunset | CLI-5L.01 | inside the booked $7.2 billion | ends early if bills fall | The booked path stands; the sunset can only shorten it | Firm, a possible saving |

**All-in on the general fund:** about **$1.85 trillion over FY2030-39 and $113 billion in FY2040**, with the credits' cost risk, the facility's exposure and the standard's payments disclosed beside it. It is not a score.

## 3. Benchmarks against outside scores

| Piece | This dossier | Outside figure | Reading |
| --- | --- | --- | --- |
| Credits | $0.757 trillion over FY2030-39, booked | JCT's 2022 score of the IRA's energy credits, $271 billion over FY2022-31 [EV-CLP-200]; CBO's 2024 baseline, about $800 billion over 2025-34 [EV-CLP-201]; JCT's scores of the 2025 repeal, about $543 billion over 2025-34 [EV-CLP-214] | The booking sits near CBO's later figure for a set that steps down; the carbon model's $1.50 trillion is the high end |
| Carbon price receipts | $1.20 trillion over FY2030-39 under B | No outside score of a power-and-industry price on this path is in the register; the legacy model's $2.00 trillion is a project estimate and responds more slowly than NEMS, REGEN or E3 [EV-CLP-705] | A faster-responding model would show lower receipts and a smaller offset saving |
| Disaster package | $0.196 trillion booked | The legacy disaster file's $100 billion core and $54 billion fuller tier in 2025 dollars [EV-CLP-719] | Consistent once inflation and the facility are added |
| The guarantee | $0.012 trillion | Canada's task force set the same 90%-for-two-years parameters without a cost [EV-CLP-529]; New Mexico's San Juan bonds put $40 million of $360 million toward workers and the community [EV-CLP-530] | No outside score of a U.S. guarantee is in the register (part 4's gap) |

## 4. The fiscal-rule report

One basis: federal fiscal years, $ billion, a cost positive, against what the budget model books (case `mixed`; the climate rows are the same at `6204281` and main's head).

| Measure | FY2030-39 | FY2040 (permanent) |
| --- | --- | --- |
| The decided set on the general fund (part 1) | $1,854 billion | $113.3 billion (0.21% of GDP) |
| Already booked for the same purposes (the sixteen legacy rows) | $1,811 billion | $164.9 billion |
| **Net change a booking would make** | **about +$43 billion** | **about −$51.6 billion (−0.10% of GDP)** |
| *of which:* memo 1 B | −$31 billion | −$29.1 billion |
| *of which:* memo 4 B | +$60 billion | 0 |
| *of which:* memo 5 B | 0 | +$9.9 billion |
| *of which:* memo 7 B | +$14 billion | +$0.7 billion |
| *of which:* the transition share kept in the general fund (`DEC-2026-11-13-13`) | 0 | −$33.1 billion |

- **The yearly cost** is in part 1: about $126 billion in FY2030, rising to $226 billion in FY2039 as the price, the credits and the add-ons ramp up, then about $113 billion in FY2040 as the time-limited pieces end and the transition share's remainder stays in the general fund (`DEC-2026-11-13-13`; part 2).
- **The permanent cost from FY2040: about $113 billion a year** on the general fund, with the transition share's remainder kept there (`DEC-2026-11-13-13`; about $146 billion on the ledger's convention, which counts the whole share as spent). Of it, the fee offset is about $42 billion (net of B's saving) and the credits and contracts about $76 billion (stepping down), less about $33 billion of transition share the ledger counts as spent; the rest is the standards' administration, the permanent disaster pieces, farms, the bill credit and the guarantee. Time-limited capital (both grid tranches, the disaster capital, the add-ons) ends with the window.
- **Its share of the plan-wide margin.** The plan-wide FY2040 general-fund primary gap is **$4,245.4 billion short** at main's head (7.84% of GDP; `agenda_gf_primary_bn`, case `mixed`, in `models/data/recovery-budget-paths.csv`, after #339's rebooking of INC-4 and immigration's memo 6, `DEC-2026-11-13-04`, `-05`; the tool reads it, not a hard-coded figure). Clean power's whole decided set is about **2.7% of that gap** in FY2040 (section 3 said about 3.7% on the earlier gap). A booking of it would change the gap by **about −$52 billion, to about $4,194 billion (7.74% of GDP)**: −1.2% of the gap, most of it the transition share kept in the general fund (`DEC-2026-11-13-13`). The standard's payments (part 2) would add up to about $7 billion if the offset applies to them.
- **The test years.** The decided costs that are permanent grow with prices and the economy; the fee offset grows with the price (5% a year after 2037) faster than covered emissions fall, and the dividend with it.
- **It is a figure to report, not an error to fix** (`DEC-2026-11-10-05`). Nothing here goes to Espen on its own: no memo set options that reach the same people at very different cost, except memo 2's restore-everything option, which Espen did not take.

## 5. Sensitivities

| Input | Central | Range | Effect on FY2030-39 | Effect on FY2040 | Basis |
| --- | --- | --- | --- | --- | --- |
| Power and industry's share of receipts (memo 1 B) | 69% → 58% | ±10 points | about ±$0.04 trillion | about ±$7 billion | Faster or slower abatement in the covered sectors than the model's; the legacy model responds slowly [EV-CLP-705] |
| How receipts respond overall | the booked $1.90 trillion | $1.65-2.10 trillion | about ±$0.02 trillion on memo 1 B's net | small | The ledger's range for C1 |
| The second tranche (memo 4 B) | $60 billion | $0-80 billion | −$0.06 to +$0.02 trillion | 0 | Milestones |
| The bill credit (memo 5 B) | $9.9 billion in FY2040 | $6-14 billion | 0 | −$4 to +$4 billion | Reach and prices |
| The guarantee (memo 7 B) | $14 billion | $6-40 billion | −$0.01 to +$0.03 trillion | −$0.4 to +$4 billion | Part 1's inputs |
| The credits' take-up | as booked | up to twice | up to +$0.74 trillion | up to +$50 billion | Part 2; not in the range below |
| **The change against the booking, all** | **+$0.04 trillion; −$52 billion** | **−$0.06 to +$0.17 trillion; −$61 to −$34 billion** | | | Summed line by line, so wide; the credits' risk shown separately |

## 6. The booking (tier 3, after the milestone review)

On the pattern of the secure floor's (`dossiers/secure-floor/6-cost.md`, part 6) and immigration's. The booking step derives the rows from `tools/clean_power_path.py` in a booking module under `models/tools/`, with a test.
1. **Rerun the carbon model with memo 1 B's coverage.** Either add a coverage setting to `models/tools/carbon/cfd-model.js` that leaves buildings and non-road transport unpriced (defaulting to today's behavior, so no other output moves), or keep this dossier's read as the basis and say so. The rerun also refreshes the O5 accounts (`climate-adoption.json`) and the dividend per adult.
2. **REV-C1 (C1)** in `models/data/inputs/ledger-revenue.csv`: about **$1.20 trillion** (range on the ledger's own $1.65-2.10 trillion times the covered share), with the note "power plants and large industry (memo 1 B, DEC-2026-11-13-06)"; CX follows at 24.4%; `fiscal-years.csv`'s CX shape from the rerun.
3. **CLI-2** (the dividend) at 80% of the new C1; **CLI-5**'s financing (`ledger-build.py`'s `_c5`) on the new C1, less the guarantee's draw.
4. **New rows:** CLI-10 (the second tranche, $0.06 trillion, time-limited capital, D4-B), CLI-5H (the bill credit, permanent from FY2040; inside CLI-5 before), CLI-11 (the guarantee, $0.014 trillion and $0.7 billion in FY2040), each on its rail with a year shape from the path.
5. **Decide where the transition share sits after FY2039** (part 2) and book the guarantee's and bill credit's FY2040 cost accordingly.
6. **Check the budget treatment of the public builders' added borrowing** (part 2), including forgiveness of unrepaid balances under the builder's statute.
6a. **The standard's payments** (part 2): a receipt and an outlay to the bill credit, by year from the energy model (`results.json`, `provisions`, CLI-3A.02: $157 billion over FY2030-39, $40 billion in FY2040); record whether the 24.4% offset applies (the energy model applies none).
6b. **Timing:** the price's start (part 1, FY2030 note), CLI-5H's money from FY2031, and the year shape that follows.
6c. **The energy model (MOD-energy, `models/tools/energy/`).** Clean power was re-reviewed on it (`review-m4.md`, `DEC-2026-11-13-12`). The booking uses its `results.json` `provisions` for the standard's payments and the year shapes of REV-C1, C1P, C2, C3 and CX; this tool's booked-basis arithmetic for the changes against the ledger (they reconcile within 1-2%: `tools/clean_power_path.py`, the re-review table); and its receipts as the high side of a range, since its PR-2 benchmark runs 26% above CBO.
6d. **The transition share after FY2039** (part 2; decided, `DEC-2026-11-13-13`, option A): from FY2040, CLI-2's outlay at 80% of C1 plus the waterfall's draws; the remainder stays in the general fund.
6e. **The builders' borrowing** (part 2): TVA's, Bonneville's, WAPA's and the eastern corporation's line capital as time-limited capital (D4-B) outlays as built, with rate repayments over the lines' lives; only expected forgiveness is a net cost. The energy model's standby-builder program cost (about $6 billion a year in 2025 dollars at half strength) overlaps the second tranche (CLI-10.01) and must not be booked twice; its extra credited generation belongs to CLI-1's risk, not to the builder.
7. **Incidence:** the household model's dividend and fee rows on the narrower base: no heating charge, a smaller dividend (section 7 checks D3 with it).
8. **Rows the decisions leave as booked:** CLI-1, CLI-9, CLI-3 (CLI-3E's zero-direct-cost row relabeled 80%/100%), CLI-10G, CLI-5L, CLI-5W, CLI-7, CLI-7K, CLI-7C, CLI-7N, CLI-13A, CLI-13F, CLI-2O, CXP.

## 7. What each figure is

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| Coverage, price path, the 80/20 split, the dividend's design | Commitment (decided) |
| Power and industry's share of receipts | Working assumption: the carbon model read, on the booked $1.90 trillion; range ±10 points |
| The dividend per adult | Working assumption: the carbon model read |
| The credits' cost | Booked path; its risk a disclosed range, bounded by the trigger (commitment) |
| The standard's payments | Working assumption: the energy model's run of the decided path, about $0.16 trillion over FY2030-39 and $40 billion in FY2040 ($0.07 trillion and $20 billion with the permitting package), to the bill credit; whether the offset applies is the booking's question |
| The bill credit's size | Working choice: a fixed sum, scaled down in proportion; the matched count is studied in the 2027-28 preparation match |
| The second tranche's cost | Working assumption on the first tranche's ratio; released on milestones (commitment) |
| The bill credit's cost | Working assumption on LIHEAP's reach and cost |
| The guarantee's cost | Working assumption, bottom-up on judgment inputs; to study in implementation with the published counts (CLI-11.05) |
| The transition share after FY2039 | Commitment: the waterfall (CLI-2A.04), then the remainder stays in the general fund (`DEC-2026-11-13-13`) |
| The public builders' borrowing in the budget | Time-limited capital with rate repayments; net cost is expected forgiveness (part 6, 6e) |
| The disaster package, the facility, farms and forests | Booked; the facility's exposure contingent and disclosed |
