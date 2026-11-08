# Morning brief: the politics after 2026, and what it means for 2029

Role: a plain-language summary for Espen of the scenario work done overnight on November 7-8, 2026: the 2027 races, what Democrats can do in 2027-28, the 2028 Senate and presidential outlook, and how it adds up for the plan that starts in January 2029 (`DEC-2026-10-29-01`). Status: synthesis only, November 8, 2026. It adds no new modelling. Every number below was checked against its source file at these heads: `main` at `dc6816c` (PRs #82, #86, #89 and #93 merged), PR #84 at `c47c371`, PR #88 at `dc5e920`, PR #87 at `d78ddb9`, PR #90 at `1d70867`, PR #91 at `300a884`, PR #92 at `9f75bae`, PR #80 at `af4e45a`.

**Where the files are.** Most files are merged into `main` and linked directly. Some files exist only on open PRs and are not merged yet. `senate-model-2028.md`, `senate-model-outputs.md` and `2030-2034-control.md` were merged with [PR #82](https://github.com/fm58cn6g4d-stack/project-2050/pull/82). Figures quoted here use the newer version in [PR #84](https://github.com/fm58cn6g4d-stack/project-2050/pull/84), which is still open and could move again. `2028-republican-branch.md`, `compounding-redistricting.md`, `compounding-defense.md` and `compounding-prebuild.md` came from PR #86 and are now on `main`. `house-model-2028.md` and `house-stress-test-2029.md` come from [PR #88](https://github.com/fm58cn6g4d-stack/project-2050/pull/88), which is built on #84. `presidential-model-2028.md` comes from [PR #87](https://github.com/fm58cn6g4d-stack/project-2050/pull/87), built on #84. The defense and DEM-2 memo, [memo-defense-baseline-and-dem2.md](memo-defense-baseline-and-dem2.md), is now on `main` (PRs #89 and #94). `housing-by-2029-world.md` comes from [PR #90](https://github.com/fm58cn6g4d-stack/project-2050/pull/90). `redistricting-2030-model.md` comes from [PR #91](https://github.com/fm58cn6g4d-stack/project-2050/pull/91), built on #88. `model-credibility.md` comes from [PR #92](https://github.com/fm58cn6g4d-stack/project-2050/pull/92), built on #91. The others named here are not merged yet. All the probabilities are this project's own scenario arithmetic, not forecasts. No rating service has rated 2028 yet.

## How much to trust these numbers

PR #92 (`model-credibility.md`) re-ran the Senate model on the 2018-2024 elections, using only what was known two years before each one.

- **The model is good, but it leans Republican.** Its accuracy score (Brier, lower is better) is 0.076, against 0.098 for the simple rule "each state votes for its last presidential winner." But it under-predicted Democratic seats in every cycle: 61 in total against 70 actually won. Swing-state Democrats (Arizona, Georgia, Nevada, Pennsylvania, Michigan) kept outrunning their states. The House curve under-predicted too, by about 7 seats on average.
- **The central assumption is cautious.** The best simple rule for 2028 says D+5.7; the models use D+3.0. Each 1.5 points of difference moves the chance of a trifecta by about 11-12 points: 35% at an even year, 58% as published, 77% at D+5.7.
- **Bottom line:** the published numbers are more likely too low for Democrats than too high. But four cycles is a small sample, all in the Trump era, and the model has not been re-tuned. Read the figures as a cautious central case.

**The five assumptions that matter most, and what to watch:**

| Assumption | Watch |
| --- | --- |
| The 2028 national mood (D+3.0, give or take 4.5) | Trump's approval, the generic ballot, special elections, the November 2027 results |
| Candidate strength carries over at 40%, with no extra term for weak nominees | The Republican Senate primaries in AZ, GA, NV, PA, NC and WI; FEC cash; Kelly's, Grassley's and Johnson's decisions |
| The three uncertain seats not up (Alaska, Mississippi, Minnesota) | The Alaska and Mississippi certifications; Klobuchar's appointee and the 2027 Republican candidate |
| The House break-even near D+1.5 | The New York referendum, Maryland's map, the Wisconsin rulings, freshman retirements, the first House ratings |
| The caucus's filibuster positions (D2-F at 63%) | The reform camp's statements on graduated cloture; Colom and Peltola if seated; any 2027 rules votes |

## 1. The ten most important findings

1. **With a Democratic president, the 2029 Senate is probably about 57 seats.** The average is 56.7, and 90% of runs fall between 53 and 60. 55 or more happens in 84% of runs; 60 or more in only 9%. A Democratic majority is near-certain in this case: 99.8% of runs have 51 or more, because Democrats need only one of New Hampshire, Georgia, Nevada, Pennsylvania, Arizona, North Carolina or Wisconsin. In a narrow win where Alaska, Mississippi and Minnesota all go Republican, it is about 80-90%. (`house-model-2028.md`, PR #88) (`senate-model-2028.md`, section 4, [PR #84](https://github.com/fm58cn6g4d-stack/project-2050/pull/84))
2. **The House, not the Senate, decides whether there is a 2029 trifecta.** On the current maps Democrats need about D+1.5 for an even chance at the House: they hold it in 8% of runs at R+3, 35% in a neutral year, 75% at D+3 and 96% at D+6. A full trifecta comes in 58% of runs on the central assumption, and in 89% when a Democrat wins the presidency. Under a Republican president, Democrats hold the House in only 15% of runs but the Senate in 85%. The presidency itself is close to even in a neutral year: a separate state-by-state model, which shares the Senate model's national and regional swings, gives a Democrat 38% at even, 76% at D+3 and 95% at D+6 (65% on the central assumption), with an even chance at about D+0.9. Pennsylvania, Michigan, Georgia and North Carolina are each the deciding state in 14-16% of runs. (`house-model-2028.md`, PR #88; `presidential-model-2028.md`, PR #87)
3. **January 2029 is the high point of the decade.** The average falls from 56.7 seats in 2029 to 54.1 after the 2030 midterm and 48.9 after 2032. Democrats hold 50 or more in every Congress through 2034 in only 46% of runs. (`2030-2034-control.md`, section 3, PR #84)
4. **Five seats drive the 2032 drop.** Mississippi, South Carolina, Kansas, Iowa and Alaska supply 63% of the expected 2032 losses. All are states Trump won by 13 to 23 points, and all were won in the 2026 wave. (same file, section 4)
5. **The best protection for 2032 is a milder 2030 midterm, and that depends on visible delivery in 2029-30.** Halving the usual midterm loss raises the chance of holding the Senate through 2034 from 46% to 56%. Statehood helps less than it looks (52-53%), because it also makes the Senate bigger, so a majority needs more seats. Stronger candidates in the exposed seats barely help (47-49%). (same file, section 5)
6. **On the filibuster, who is in the caucus matters more than how many seats it has.** About 6 Democrats are expected to oppose a rules change, against a margin of about 6-7 seats. The graduated-cloture plan (D2-F) has the votes in 63% of runs, but the range is 14-87% depending on senators not on record. (`senate-model-2028.md`, section 9, PR #84)
7. **The Minnesota Senate seat is on the ballot in November 2027, not 2028.** Its winner serves to January 2031. Losing it costs a full seat in every 2029 scenario and 13-19 points off the chance of 55+. Only 37 Democratic seats not up in 2028 are certain, not 40. (`senate-model-2028.md`, sections 1 and 9, PR #84; [2027-races.md](2027-races.md), section 4)
8. **There is probably one real legislative year, 2027, then a campaign.** Two budget bills that need only 51 votes (FY2027 and FY2028) are available without touching the FY2029 slot the 2029 plan needs. The chance a reconciliation bill passes Congress is put at 55-75%; the risk is how to pay for it. ([2027-28-playbook.md](2027-28-playbook.md), in brief and section 2; [2027-28-stress-tests.md](2027-28-stress-tests.md), question 3)
9. **After 2028 the map moves to the Sun Belt, and the 2030 midterm draws the next House maps.** On projected 2030 census seats, the Harris states plus Wisconsin, Michigan and Pennsylvania fall from 270 electoral votes to 258. The 2031 maps are drawn by whoever wins in November 2030. Under a Democratic president, Republicans probably hold the pen in Florida (93% of runs), North Carolina (87%), Ohio (77%), Texas (71%) and Georgia (48%). Federal fairness rules (part 2 of the redistricting reform, DEM-2) would be worth about 7 Democratic House seats on the 2032 maps (range +2 to +11), raising the chance of a Democratic House in 2033 from 57% to 68%. The mid-decade ban on its own adds about nothing in 2032. **Corrected after review:** the first version said about 10 seats (42% to 57%), because its split of the map lean did not reproduce today's maps. ([compounding-2029-2050.md](compounding-2029-2050.md), section 4; `redistricting-2030-model.md`, PR #91)
10. **The 2027-28 defense deal is locked in for a decade, and the plan's own cost checks won't show it.** The "parity" path ($905 billion in FY2028) puts about $26 billion a year more into the 2029 starting level and adds about $0.30 trillion of defense over 2030-39. NSC-1A is scored against CBO's baseline, so whatever passes becomes the baseline: the ledger and the D4 fiscal-rule checks show $0 in every path. The cost shows up only in total spending and debt. (`compounding-defense.md`, PR #86; [compounding-2029-2050.md](compounding-2029-2050.md), section 2)

## 2. Your priors, tested

| Your prior | What the model says |
| --- | --- |
| **Ohio is the riskiest Democratic Senate seat, by a lot.** | **Right.** Brown wins 21% of runs in a neutral year; the next lowest are Arizona (54%) and Pennsylvania (56%). But Ohio rarely decides control (about 2% of runs). It matters for seats 58-60. |
| **Arizona, Georgia and Nevada are safe-ish in a neutral year.** | **Too optimistic.** Neutral year: Arizona 54%, Georgia 71%, Nevada 59%, and all three hold in only 30% of runs. They are only safe-ish at about D+6 (73% for all three). If Kelly runs for president instead, Arizona drops about 10 points. |
| **It will be hard to lose the Senate before 2032.** | **Right.** With a Democratic president, Democrats hold 50+ through the 2031-32 Congress in 82% of runs (84% if the president is re-elected in 2032). The danger is the 2032 election itself: 46-60% hold through 2033-34. |
| **Good shots at North Carolina and Wisconsin.** | **Partly.** They are toss-ups in a neutral year (45% and 38%; both in 19% of runs). They become favored at D+3 (65% and 57%). |
| **Montana as a reach.** | **Montana is not up in 2028.** Sheehy is up in 2030 and Alme in 2032. The best "wild" seats among those up need a 2026-sized year: at D+13, Iowa 66% and Florida 56%. At D+3 Democrats expect to win only 1.5 Republican-held seats. |
| **A Murkowski deal, or a party switch.** | **She is up, but the evidence runs against a deal.** She endorsed Sullivan "to keep in the majority," her approval collapsed in 2025, and she has pledged to oppose weakening the filibuster. A run as a Democratic-aligned independent is given a 6% chance. Overall, the seat goes to the Democratic caucus in about 8% of runs. The repeal of ranked-choice voting (Measure 2) is losing (No 51.85%), which keeps her viable. |

Sources: `senate-model-2028.md`, sections 4-6 and 9, and `2030-2034-control.md`, section 3 (both PR #84).

## 3. Decisions waiting on you

**PR #80: which Senate size the plan designs for (D1).** It is tier 3, so only your `espen-approved` label merges it. I have not applied or asked for any label.

| Option | Plan for | Test every item at | Upside | What changes in the plan |
| --- | --- | --- | --- | --- |
| A. Keep the old D1 | 52-54 seats | 51 | 56+ | Nothing. Bills that need 55 dependable votes stay out of the base package. The old assumption that Democrats hold the Senate to 2036 stays in. |
| **B. Move to the estimate (recommended)** | **53-56** | **51** | **58+** | Each dossier designs for a somewhat bigger Senate. The 51-seat test stays, so nothing that passes today drops out. The "hold to 2036" assumption is replaced by a stated risk in 2030 and 2032. The House assumption now notes the 2027 majority and the *Callais* ruling. |
| C. Plan for the 2026 result | 55-57 | 52 | 60 | The most ambitious package. It assumes 2028 repeats 2026, and it fails in an even year. The safety test rises from 51 seats to 52. |

The newer model supports B. Its center with a Democratic president (56.7) sits at the top of B's band. It does not argue for C, because 2029 is the peak and the Senate shrinks after it. One fact for #80: its base of 40 seats not up in 2028 also needs Democrats to hold Minnesota in 2027. To choose B, add the label. To choose A or C, leave a comment and the author session will rewrite it. If you decide on a later day than November 8, say so, so the decision can be re-dated.

**The defense and DEM-2 memo: two choices, decided separately.** Neither changes anything until you decide.

*(a) How the plan counts defense.* Today the plan's cost checks measure everything against CBO's baseline, so a bigger 2027-28 defense deal would never show up (finding 10).

| Option | What it means | What changes |
| --- | --- | --- |
| A. Keep CBO for everything | The current rule | Nothing. The 2027-28 defense choice stays invisible in the plan's numbers |
| B. Measure defense against a fixed path | Flat in real terms from the 2026 level; anything above it is booked as a cost | The defense line shows the gap ($0.13-0.30 trillion), and the fiscal-rule checks tighten by the same amount |
| **C. Keep CBO, add a disclosed line (recommended)** | The tests stay the same; a separate line shows defense above the 2026 flat path | A new line in the ledger and the fiscal report. It informs but does not bind. It can be upgraded to B later |

B or C changes the adopted model inputs, which Codex looks after. That is a tier-3 change: it needs your approval, and then a request to Codex.

*(b) How the redistricting reform (DEM-2) is written.*

| Option | What it means | What changes |
| --- | --- | --- |
| A. One provision, as now | Commissions plus a ban on mid-decade redraws, together | If a court strikes the commissions, the ban may fall with them |
| B. One bill, three separable parts | Part 1, the mid-decade ban; part 2, federal fairness rules; part 3, commissions. Each stands alone | Same floor time as A. If the commissions fall, the ban and the rules survive. D1's House assumption would rest on parts 1-2 |
| C. Two bills | The ban and rules first, commissions later | Two floor fights; commissions may never get a slot before 2031 |
| **D. Ban, fairness rules and a court backstop; commissions voluntary (recommended; legacy DEM-2E)** | Part 1, the ban; part 2, federal fairness rules; part 3, a three-judge federal court that draws a map where a state's map fails the rules. A map from an independent commission is presumed to pass. No state is ordered to set up a commission | Removes the part a court is most likely to strike, so the 2031 maps aren't drawn under a pending lawsuit. Fewer states get commissions. Part 2 is written to survive on its own: plain map rules in one section, the fairness test in a separate section with one measurable standard |

The memo now recommends D, changed from B after PR #91 found that nearly all of DEM-2's value for the 2032 maps comes from part 2, not the ban. B stays the choice if you want the commission mandate tried in court. The memo's option list still has B marked "recommended" in one heading; its final recommendation is D.

**A related question for #80: what if the House is lost?** PR #88's stress test (`house-stress-test-2029.md`) looks at a Democratic president and Senate with a Republican House, about 11% of Democratic-president runs and mostly narrow wins. In that case the three budget bills are gone, probably until 2033. What remains: every nomination, the Senate's own rules, and executive action (care, clean power, work and immigration keep part of their agenda; the secure floor, the housing money and DEM-1 stall). The leverage would come from the FY2030 spending bills, the debt limit and the tax deductions that expire after 2028. It offers three options alongside #80. None changes the Senate band:

| Option | What it means |
| --- | --- |
| 1. Keep the House assumption as is | Plan as if a Democratic president brings a Democratic House (89% of runs). No plan for the narrow-win case |
| 2. Add an "H" stress tag | Each item also says whether it survives a Republican House, next to the 51-seat Senate test. Light work |
| 3. Write a divided-2029 branch plan | A short plan for that case: first 100 days of executive action, nominations, the spending and tax bargaining positions. More work, ready by November 2028 |

**Housing point 5: the rules for emergency rent help (approve or amend).** PR #93, now on `main`, answers your open question (`dossiers/home/point-5-emergency-aid-rules.md`). Its key finding: in the Treasury inspector general's cases of questioned payments in the last emergency rent program, the fraud came through fake leases and false landlords, not tenants misstating income. So the checks before payment fall on the landlord and the property. The five lines to approve or amend:
1. **Who:** renters at or below 50% of area income (or already on SNAP, Medicaid or SSI) facing a housing crisis now, ranked by a short tested risk screen, court cases first.
2. **Payments:** back rent plus up to two months ahead, capped by local rents, one episode a year; legal help paid separately.
3. **Checks:** tenants may state income and hardship; identity, tenancy and the landlord's ownership checked before paying; a random sample audited afterward.
4. **Landlords:** may apply with the tenant's consent; paid first, with tenants paid if the landlord refuses; no eviction for paid months; payment within 30 days.
5. **Accountability:** the error rate measured from year one and published; one administrator per place, funded by a need-and-performance formula; one payment data standard with a duplicate check.

**PR #76 (the merge-gate fix): nothing to do.** You approved it, and it merged on October 30.

**Three smaller questions the new files raise** (not urgent):
- Should the filibuster plan now treat the talking filibuster (D2-C) as the likely 2029 rule, with graduated cloture as the upside? (`senate-model-2028.md`, section 9)
- Which horizon matters to you: "before 2032" (82-85% safe) or "through 2034" (46-60%)? (`2030-2034-control.md`, section 6)
- Which defense level to accept in the 2027-28 budget deals, decided before about summer 2027 (finding 10; separate from #89's counting question). (`compounding-defense.md`, PR #86)

## 4. What this means for housing

None of the housing memos has a recorded decision. Memos 1 B and 2 B and a stage 3 for disabled renters are the recommended directions, not choices you have made. This section is input to the memos, not advice on what to choose (`housing-by-2029-world.md`, PR #90). **#90 is under a changes request from the reviewer**, including on how it describes memo 1 B, so treat this section as provisional.

**Four possible 2029 worlds** (central assumption, from the House model in PR #88):

| World | Chance |
| --- | --- |
| Democratic trifecta | about 58% |
| Democratic president, Republican House | about 7% |
| Republican president, Democratic Senate | about 29% |
| Full Republican government | about 5% |

- **The core of the housing plan moves only in a trifecta.** The million new rental awards (HOU-4A), the guarantee's stages and the building money (HOU-3C) all need a 51-vote budget bill (reconciliation), and that needs both chambers.
- **Three choices work in every world:** paying for zoning results through the ROAD Act's fund (memo 4 B), Housing First by reversing the 2025 order (memo 5 B), and keeping the investor limit (HOU-7B). They rest on current law, yearly funding or executive action.
- **Choices whose best answer depends on the world:**
  - Memo 6: should a standing emergency-rent fund be designed so its rules can also run on one-time money? #90 sketches "one rulebook, three taps": the same delivery rules (who qualifies, what is paid, how it is checked, who runs it) fed by a standing fund in a trifecta, a yearly appropriation in a split government, or one-time money in a recession. The sketch does not choose between memo 6's options.
  - Memo 3, parts 1-2: outside a trifecta, a tax-credit deal is likelier to widen the credits than narrow them, and a federal builder needs a law only a trifecta could pass.
  - Memo 1 B (recommended, not yet decided): much of it can start without a new law in any world with a Democratic HUD. Under 42 U.S.C. 1437f(o)(13), HUD can name areas where vouchers are "difficult to use". There, housing agencies may attach an extra 10% of their vouchers to buildings, and one building may have 40% of its units assisted instead of 25%. This was checked against the statute.
  - A possible stage 3 for disabled renters (proposed, not decided): written as an expansion of the existing disability voucher program (Mainstream), it could grow from 2027 in any world.
  - Memo 8 (who comes first): the order doesn't change, but outside a trifecta it reaches only as far as guidance to local agencies.
- **The 2027-28 risk:** a bipartisan expansion of the low-income housing tax credit would work against memo 3 part 1's recommended narrowing, if you choose it. The 2025 law already widened the credit, and that is now in the housing baseline: a permanent 12% increase from 2026, and the bond-financing test cut from 50% to 25%.

## 5. Where the models disagree, or the evidence is thin

- **The filibuster head count now follows one list, from a right-leaning source.** The two files used to disagree about Jackson, Turek, Andrews and King. #84 (`c47c371`) now uses the playbook's list: Jackson for ending the filibuster, Turek and Andrews for a talking filibuster, King opposed. That moved D2-F from 62% to 63% and the range from 9-89% to 14-87%. The list rests mainly on a Washington Examiner count, a right-leaning source, so it still needs checking senator by senator. ([2027-28-playbook.md](2027-28-playbook.md), section 6; `senate-model-2028.md`, section 9)
- **The statehood figures were corrected after review.** The first version of #84 said D.C. and Puerto Rico statehood would raise the chance of holding the Senate through 2034 from 46% to 64%. It had kept counting 50 seats as a majority in a Senate of 102 or 104. With that fixed (`5b4d0f5`), statehood gives only 52-53%, and a milder 2030 midterm becomes the biggest lever. The same fix made the filibuster count come out the same on every run; before it, figures varied by a point or so between runs.
- **A late fix to the Alaska repeal case.** #82's review fix, now merged into #84 (`4528f45`), changes the case where Alaska repeals ranked-choice voting: if Murkowski first beats Dunleavy in a closed Republican primary (assumed 30%), she then wins about 30% of runs, where the earlier text said almost never. As an independent she still almost never wins. The same fix corrects a Tennessee seat counted twice in 2030-32, which moved some figures by about one point.
- **Older files still use the 40-seat base.** The 2028 scenarios in [2028-outlook.md](2028-outlook.md) and #80 rest on the first, simpler estimate in [5-senate-2028.md](5-senate-2028.md). #82 now marks that estimate as superseded: only 37 seats are certain. Some seat odds also differ between the two (at D+3, North Carolina 54% in the old estimate against 65% in the new one; Nevada 67% against 76%).
- **Numbers changed between rounds.** Round 2 corrected for governors' personal popularity: in a neutral year Nevada went from 53% to 59%, Arizona from 60% to 54%, and Pennsylvania from 62% to 56%. Round 3 cut the Murkowski-caucuses-with-Democrats branch from 10% to 6%. Round 4 cut the chance of the ranked-choice repeal from 15% to 4%. Between #82's first version and #84 the 2029 center moved from 56.6 to 56.7 seats.
- **Small mismatches remain.** `2030-2034-control.md` cites 13,150 runs; the outputs say 13,136. P(55+) in 2029 is 84% in one table and 85% in the chained run. With DEM-2, the 2033 House chance is 68% in #91 and 67% in #92. None changes a conclusion.
- **Two House break-evens.** [2028-outlook.md](2028-outlook.md) puts the House break-even near D+3, from the map alone. PR #88 puts it near D+1.5, because it adds an assumed 1.5-point edge for the roughly 45 new Democratic incumbents (tested from 0.5 to 3.0 points). Across that range, the chance of a Democratic House at D+3 runs from 62% to 88%. #88 is a curve fitted to two published facts about the maps, not a district-by-district model, and its map sources lean progressive or reform.
- **The biggest input is a judgment call.** The 2028 national mood is set at D+3, give or take 4.5 points. That is below what history's reversion would suggest (D+5 to D+9) and is a labeled assumption.
- **The 2032 loss is heavier than history.** The model loses about 5 seats; past wave classes lost a median of 1 six years later. The model's authors argue this class is unusually deep in red states (the 2018 losses support them), but this is a contested point.
- **Sources from the current administration.** Under `DEC-2026-10-30-01`, the analysis these agencies produce gets extra skepticism. The playbook's figure that the Medicaid agency (CMS) expects to approve about 2 in 10 state exemption requests is that agency's own projection. The gas-price forecast ($3.91 to $3.56) comes from the Energy Information Administration's October 2026 outlook. Neither has an independent check yet. The Social Security dates (2032 and 2034) come through the Congressional Research Service, an independent source. The census claim in `compounding-2029-2050.md` (that the administration wants to change who counts for seats) is from memory and is marked "verify".
- **#86 leans on memory and trackers in places.** Rubio's role in a 2017 child-credit amendment and the 2015 Supreme Court dissent lineup on redistricting commissions are marked "memory; verify". Most litigation statuses come from case trackers, not the rulings. #86's 5-10 seat value of DEM-2 was anchored to FiveThirtyEight (about 5) and Brennan (6-9 in four states). PR #91's model, corrected after review, puts it at about 7, and corrects #86's claim that DEM-2 is "about neutral" if Democrats sweep 2030: it is still worth about 4 seats then, because several state chambers sit far to the right of their states. The Republican primary polling comes from a UK aggregator and one AtlasIntel poll.
- **Thin evidence in places.** Several facts are from search summaries or headlines not opened (for example Fetterman's newer filibuster stance in `4-2029-plan.md`, Murkowski's endorsement in the governor race). A 2006 House figure differs between Brookings and the House Clerk. The model uses no polling, because none exists yet for 2028.

## 6. The next research wave, ranked

1. **A senator-by-senator filibuster count for the 2027 caucus.** Confirm the list in section 5 from the senators' own words, and find the unknown positions. *Why:* it decides whether the 2029 rule is graduated cloture or a talking filibuster, and it swings D2-F from 14% to 87%.
2. **A House stress test for D1.** #88 has drafted the analysis. The next step, if you want it, is the "H" tag on each domain file or the short branch plan (section 3). *Why:* in 11% of Democratic-president runs the House is lost, and then none of the three budget bills (R1-R3) can pass, however big the Senate is.
3. **Recheck after certification (November 18-25).** Alaska, Mississippi and Measure 2, and whether a repeal would apply in 2028. *Why:* these set the base of 37-39 certain seats and decide whether the Murkowski question exists at all.
4. **Does visible delivery in 2029-30 shrink the 2030 midterm loss? And what are the House odds in 2030 and 2032?** *Why:* a milder midterm is now the biggest single lever on keeping the Senate after 2032, and it is the one that policy controls. Halving the usual loss is worth about 10 points.
5. **The talking-filibuster floor-time math at about 6 holdouts.** The old estimate was 213-272 floor days against a 163-day budget. *Why:* if graduated cloture is a coin flip, this becomes the base case, and it may not fit the first Congress.
6. **Statehood as a 2029-30 bill.** Floor time, Puerto Rico's vote on statehood, and which election cycles the new senators fall in. *Why:* after the correction it is worth only about 6-7 points on keeping the Senate after 2032, so its case rests on representation. The plan should say so plainly before spending first-Congress floor time on it.
7. **Which parts of each flagship can pass with 51 votes (Byrd-rule edges).** Care, housing conditions and paid leave first. *Why:* it sorts the 2029 bills between reconciliation and regular order before the bills are fixed.
8. **The Minnesota 2027 special.** Who Klobuchar appoints, and whether Republicans recruit a serious candidate. *Why:* a full seat in every 2029 scenario, and a placeholder appointee costs about 6 points of the chance of holding it.
9. **Whether DEM-2 survives the Court.** The memo now recommends option D (no commission mandate). What remains is checking the 2015 dissents (cited from memory), whether a statutory fairness test survives in court after *Rucho*, and whether the three-judge backstop works as the memo assumes. *Why:* part 2 carries about 7 House seats on the 2032 maps, but only if it is in force before the 2031 maps. It is the plan's main answer to losing the 2030 midterm.
