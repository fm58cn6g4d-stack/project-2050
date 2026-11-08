# The 2028 Senate: a seat-by-seat model

Role: a runnable model of the 2028 Senate elections, run under several national environments; a test of Espen's priors against it; the Murkowski and Alaska branches; and what the Senate it implies means for the 2029 plan. It builds on `5-senate-2028.md`, corrects it where noted, and replaces its arithmetic (the older script stays for the record). The 2030 and 2032 classes are in `2030-2034-control.md`. Status: draft (stage B follow-up), November 8, 2026.

**What kind of evidence this is.** Every probability here is **this project's own scenario analysis**, not a forecast and not a published rating; none of Cook, Sabato or Inside Elections has rated 2028 yet. The inputs are data (election results, FEC filings, statutes) with sources; the weights, error sizes and Murkowski branch odds are labeled assumptions with tested ranges. 2026 margins are unofficial. Code: `tools/senate_model.py` (standard library; `--write` regenerates `senate-model-outputs.md`, which holds every table quoted here). Tests: `tools/test_senate_model.py`.

## In brief

- **The map: 35 races in 2028.** The 34 Class 3 seats plus a Tennessee special for Blackburn's seat [SRC-0582]. Republicans defend 19 and Democrats 16. Three of the lead's beliefs are **confirmed**:
  - Georgia's 2028 seat is Warnock's.
  - Montana has **no** 2028 race: Sheehy is Class 1, up in 2030, and the seat Daines held is Class 2, won by Alme in 2026 and up in 2032.
  - Murkowski's seat is Class 3, up in 2028.
- **One correction to `5-senate-2028.md`.** Klobuchar's election as governor triggers a **Minnesota special election on November 2, 2027**, not in 2028 (Minn. Stat. 204D.28) [SRC-0578] [SRC-0579]. Its winner serves to January 2031. So the "40 seats not up" base needs three uncertain wins (Alaska 2026, Mississippi 2026 and Minnesota 2027), and only **37 are certain**.
- **With a Democratic president, the central Senate is about 56-57 seats.** Under the evidence-weighted environment (D+3, SD 4.5), conditional on a Democrat winning the presidency:
  - mean 56.6, 90% range 53-60;
  - 55 or more in 84% of runs;
  - 60 or more in 9%.

  By fixed environment, across all runs: neutral 53.9 (51-57), D+3 55.4 (52-58), D+6 56.8 (54-60), R+3 52.4 (49-56). Even under a Republican president, Democrats keep control in 85% of runs.
- **Where the Senate is decided.** Control turns on New Hampshire, Georgia, Nevada, Pennsylvania and Arizona: these are the tipping-point seats for the 50th and 51st votes. Ohio rarely decides control (about 2% of runs). It matters for the 58th to 60th seats, along with Florida, Iowa and Alaska.
- **Espen's priors, scored.**

  | Prior | Verdict | Evidence |
  | --- | --- | --- |
  | Ohio is the riskiest Democratic seat by a lot | **Right** | 21% in a neutral year; the next lowest are Arizona and Pennsylvania at 56% |
  | Arizona, Georgia and Nevada are safe-leaning in a neutral year | **Too optimistic** | 56%, 71% and 60%; all three held in only 30% of runs. True only from about D+6 (73%) |
  | Hard to lose the Senate before 2032 | **Right** | Democrats hold 50+ through the 2031-32 Congress in 82-85% of runs with a Democratic president. The danger is the 2032 election itself, when the wave class of 2026 is up |
  | A very solid shot at North Carolina and Wisconsin | **Toss-ups in a neutral year** | 45% and 39%; favored from D+3 (65% and 57%) |
  | Montana | **Not up** | The southern and Midwestern "wild map" needs a 2026-sized environment: at D+13, Iowa 66%, Florida 56%, Alaska 31%, Kansas 30%, Missouri 28% |
  | Murkowski deals with Democrats or caucuses with them | **Evidence runs against it** | Below |

  Murkowski in detail:
  - She endorsed Sullivan against Peltola in January 2026 "to keep in the majority" [SRC-0591].
  - Her net approval fell from +3 to −47 in 2025, and her rating among Alaska progressives fell from net +54 to net −21 [SRC-0590].
  - She has pledged to "vote against any motion to weaken the filibuster" [SRC-0592].
  - Even as a Democratic-caucusing independent she would win only 19% of runs in a neutral year (51% at D+6), and she would not be a vote for D2.
- **For the plan.** 60 seats is a remote upside (about 9% with a Democratic president), so D2's rules change stays the path for every regular-order flagship. The 2029 Senate is the largest the decade is likely to offer (`2030-2034-control.md`), which argues for doing regular-order work in 2029-30. The estimate supports #80's option B (53-56) and sits at the top of it.

## 1. Which seats are up, checked

| Belief (lead) | Verdict | Evidence |
| --- | --- | --- |
| Georgia's 2028 seat is Warnock's | **Confirmed** | Warnock holds the Class 3 seat (won 2022 runoff, D+2.8) [SRC-0565]; Ossoff's Class 2 seat was up in 2026 (`1-results.md`) |
| Montana has no regular 2028 race | **Confirmed** | Sheehy won the Class 1 seat in 2024 (R+7.1) [SRC-0576], next up **November 2030**; the Class 2 seat (Daines's) was won by Alme in 2026, next up 2032 (`1-results.md`). No vacancy is pending |
| Murkowski's seat is Class 3 | **Confirmed** | Up in 2028; she was last elected in 2022 under the top-four and ranked-choice system [SRC-0565] |
| (`5-senate-2028.md`) 40 Democratic seats not up if Alaska and Mississippi go Democratic | **Corrected** | The 40 also needs Minnesota's **November 2027** special: Klobuchar takes office as governor January 4, 2027; a vacancy at least 11 weeks before the August primary is filled "at the next November election," which in Minnesota includes odd years (204D.28, subd. 6) [SRC-0578] [SRC-0579]. Certain seats not up: **37** |
| Tennessee special in 2028 | **Confirmed, more firmly** | The appointee serves until the November 2028 election; the winner serves to January 2031, then the seat is up again in 2030 [SRC-0582] |
| (new) Texas | **No 2028 race** | Cruz (Class 1) is up in 2030; Talarico (Class 2) in 2032 |
| (new) Colorado | **Bennet is staying** | He lost the June 30 governor primary to Weiser, 45-55 [SRC-0580], so no vacancy; his 2028 committee had $0.19 million on hand on September 30 [SRC-0577] |

Montana's next Senate vote is November 2030 (Sheehy), then 2032 (Alme). For the "wild map", the closest equivalents among the seats that are up are Iowa, Florida, Alaska, Kansas, Missouri, South Carolina, Indiana, Utah and Louisiana (section 6).

## 2. The inputs

**Lean** (positive = more Democratic than the nation) blends three results, each measured against that year's national margin:
- the 2020 presidential margin (weight 0.2) [SRC-0575];
- the 2024 presidential margin (weight 0.5) [SRC-0459];
- the 2026 statewide margins (weight 0.3) [SRC-0574] [SRC-0483].

Round 2 (section 8) cleaned the 2026 margins: it nets out incumbency (2 points for a senator, 3 for a governor) and gives governor races half weight, since they stray about four points further from partisan lean than Senate races [SRC-0589]. National margins: 2020 D+4.46, 2022 R+2.6 (House vote) [SRC-0570], 2024 R+1.48, 2026 D+12.9 (House vote, unofficial) [SRC-0464].

**Candidate effect** is incumbency (2 points) plus 40% of how far the holder ran ahead of or behind the state's expected result in their last D-v-R race, capped at 6 points:
- 2022 [SRC-0565] for most holders;
- 2024 for Brown, whose loss ran 7.6 points ahead of Harris [SRC-0576].

Five holders are set by hand: Moody, Kennedy, Hoeven, Lee and the Tennessee appointee.

**Money** is cash on hand on September 30, 2026, from the FEC [SRC-0577]; the extract is in `senate-model-fec-cash.csv`. It is reported as a signal, not converted into votes.

| Seat | Holder | Lean | Candidate effect | Status | Cash on hand (FEC, Sept 30) | P(D) neutral | P(D) D+3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| New Hampshire | Hassan (D) | +1.4 | +4.5 | Running (assumed) | $2.0M | 84% | 93% |
| Georgia | Warnock (D) | -1.0 | +4.3 | Running (assumed) | $4.1M | 71% | 85% |
| Nevada | Cortez Masto (D) | -1.9 | +3.3 | Intent unknown | $3.5M | 60% | 77% |
| Pennsylvania | Fetterman (D) | +1.1 | 0 (set; extra uncertainty) | Many possible primary challengers [SRC-0564] | $2.3M | 56% | 73% |
| Arizona | Kelly (D) | -3.7 | +5.8 | 75% he is the nominee: deciding on a presidential run after the election; Arizona law lets him run for both [SRC-0581] | **$26.5M**, the most of any 2028 incumbent | 56% | 72% |
| North Carolina | Budd (R) | 0.0 | -0.7 | Running; a primary challenger filed [SRC-0564] | $0.7M | 45% | 65% |
| Wisconsin | Johnson (R) | -1.9 | +0.1 | 25% he runs: "does not want" a fourth term [SRC-0586] | $1.1M | 39% | 57% |
| Ohio | Brown (D) | -9.1 | +4.2 | Up for the full term | (2026 committee; not in the 2028 list) | 21% | 38% |
| Iowa | Grassley (R) | -10.3 | -0.2 | 35% he runs; decides in 2027, 95 in 2028 [SRC-0572] | $0.5M | 5% | 12% |
| Alaska | Murkowski (R) | -11.9 | branch model (section 5) | Dunleavy expected to challenge [SRC-0584] | $1.6M | 3% | 6% |
| Florida | Moody (R) | -11.6 | -0.6 | Up for the full term | (2026 committee) | 2% | 6% |
| Kansas | Moran (R) | -13.5 | -2.6 | Intent unknown | $6.0M | <1% | 1% |

The other 23 seats are safe in every environment up to D+6. Democratic: California, Colorado, Connecticut, Hawaii, Illinois, Maryland, New York, Oregon, Vermont, Washington. Republican: Alabama, Arkansas, Idaho, Indiana, Kentucky, Louisiana, Missouri, North Dakota, Oklahoma, South Carolina, South Dakota, Tennessee (special), Utah. Their rows are in `senate-model-outputs.md`, section 1.

**Uncertain seats not up** (assumptions): Alaska 2026 78%, Mississippi 2026 87% (both from `1-results.md`), Minnesota 2027 special 90% (range 80-95%; Minnesota was D+4.2 in 2024 and D+10.1 in 2026, and the 2027 electorate votes under Trump).

## 3. The model

| Piece | Choice | Range tested | Why |
| --- | --- | --- | --- |
| National environment E | The Democratic presidential margin; fixed per scenario, or drawn (D+3, SD 4.5) for the "evidence-weighted prior" | R+3 to D+13 | See below |
| Presidential error | SD 2.0 around E; Democrats win the Electoral College if the drawn margin exceeds 1.0 | Bias 0-3 | The tipping-point state ran 3.8 points right of the nation in 2020 (Wisconsin) and 0.2 in 2024 (Pennsylvania) [SRC-0575] [SRC-0459] |
| Senate-wide error | SD 1.0 (all races move together off the presidential result) | | Senate and presidential margins correlated at about 0.95 in 2024 [SRC-0576]; 91% of races since 2012 matched the presidential winner [SRC-0569] |
| Regional error | SD 2.5, shared within six blocs: Rust Belt, Sun Belt, Plains, South, Mountain, coastal blue | 1.5-3.5 | States' 2020-24 swings differed from the national swing with an SD of 2.4 (this project's arithmetic on [SRC-0575] [SRC-0459]) |
| Race error | SD 5.0 for an incumbent; about 5.6 for an open seat | 4-6 | 2024 Senate margins differed from the same state's presidential margin with an SD of 5.9 points, candidate effects included (Montana +12.8, Maryland -16.7) [SRC-0576] |
| Uncertain candidacies | Kelly, Grassley and Johnson drawn per run; an open seat loses the candidate effect | | Section 2 |

**The evidence-weighted environment (D+3, SD 4.5), an assumption.** Since 1994 the national vote has reverted toward the party that lost the midterm by 0-8 points in the following presidential year. It grew instead from 2006 to 2008, the closest analog to an open-seat year after a two-term president (`5-senate-2028.md`, section 2). Reverting from D+12.9 would center 2028 around D+5 to D+9. But no presidential margin since 1992 has exceeded 8.5 points [SRC-0588], and the nominees are unknown. So the center is set below the reversion arithmetic, at D+3, with a wide spread. Under it, Democrats win the presidency in 66% of runs. The fixed-environment rows show what changes if the center is wrong.

**Sensitivity (D+3).** Across every range above, the mean moves by at most 0.6 seats and P(55+) by at most 7 points (`senate-model-outputs.md`, section 7). The seats not up move it more:
- if Republicans win both uncalled 2026 races, the mean falls to 53.7 and P(55+) from 69% to 36%;
- losing the Minnesota special costs a full seat (P(55+) 52%).

## 4. Results

**Democratic-caucus seats in January 2029** (20,000 runs each; `senate-model-outputs.md`, sections 2-3):

| Environment | Mean | 90% range | P(≥51) | P(≥55) | P(≥58) | P(≥60) | P(Democrats control) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R+3 | 52.4 | 49-56 | 83% | 15% | <1% | <1% | 83% |
| Neutral | 53.9 | 51-57 | 96% | 39% | 3% | <1% | 96% |
| D+3 | 55.4 | 52-58 | 99% | 70% | 14% | 1% | 100% |
| D+6 | 56.8 | 54-60 | 100% | 90% | 36% | 5% | 100% |
| 2026 repeat (D+13, a midterm-style electorate) | 59.9 | 57-63 | 100% | 100% | 92% | 59% | 100% |
| **Evidence-weighted, Democratic president (66% of runs)** | **56.6** | **53-60** | 100% | 84% | 34% | 9% | 100% |
| Evidence-weighted, Republican president (34%) | 52.8 | 49-56 | 85% | 22% | 1% | <1% | 85% |

"Control" counts 50 seats plus a Democratic Vice President. In a neutral year conditional on a Democratic president (31% of neutral runs), the mean is 55.1 (52-58).

**Tipping points** (evidence-weighted): the seat that delivers each threshold when the races are ranked by margin.

| Threshold | Seats most often decisive (share of runs) |
| --- | --- |
| 50th and 51st seats (control) | New Hampshire 17%, Georgia 14%, Nevada 9%, Pennsylvania 9%, Arizona 9%, North Carolina 6%, Wisconsin 5%; often a safe Democratic seat, meaning control was never in doubt |
| 60th seat | Florida 15%, Iowa 15%, Alaska 14%, Kansas 11%, Missouri 10%, South Carolina 7%, Ohio 7%, Indiana 6% |

**Reading it.** The Senate majority itself is very likely with a Democratic president, and likely even without one. The real question for the plan is size. The likely band is 53-60, which holds:
- with **5-10 votes of margin** for a D2 rules change at 51;
- **0-7 seats short** of 60.

## 5. Murkowski and Alaska

**The facts.**
- Murkowski is up in 2028, under Alaska's top-four primary and ranked-choice general election.
- Measure 2, which would repeal that system and restore closed party primaries, trails about 48-52 with ballots still out; tabulation is November 18 [SRC-0583].
- Gov. Dunleavy, term-limited, is widely reported as a 2028 challenger, though he had filed no committee as of August 2026 [SRC-0584].
- Her signals cut both ways:
  - In June 2025 she called caucusing with Democrats an "interesting hypothetical," tied to a 50-50 Senate [SRC-0585].
  - In January 2026 she endorsed Sullivan against Peltola within hours of Peltola's launch, saying "we want to figure out how we're going to keep in the majority" [SRC-0591].
  - She has since endorsed the Democrat Kreiss-Tomkins for governor (reported in the same coverage; not opened).
  - Alaska Survey Research put her net approval at +3 in January 2025 and −47 in late July, after her vote for the reconciliation bill; among progressives it went from net +54 to net −21 [SRC-0590].
  - She has said she "will vote against any motion to weaken the filibuster or create carveouts within it" [SRC-0592].

**The submodel.** Each run computes the margin a generic Democrat would get against Dunleavy. It then splits voters into a Democratic side and a Republican side and gives Murkowski a share of each:
- Calibrated to 2022 [SRC-0565] (first choices Murkowski 43.4, Tshibaka 42.6, Chesbro (D) 10.4), she then drew about 77% of the Democratic side and 16% of the Republican side.
- About three in four Chesbro ballots then transferred to her.
- For 2028 her Democratic-side share is drawn lower, at 35-70%, because of the 2025 collapse.

| Branch (weight, assumption) | Neutral: Murkowski / Democrat / Dunleavy | D+3 | D+6 | Seat counts for |
| --- | --- | --- | --- | --- |
| **Runs as a Republican** (56%) | 25% / 1% / 74% | 38% / 2% / 59% | 51% / 5% / 43% | Republicans, whoever wins |
| **Independent, caucusing with Democrats** (6%) | 19% / none / 81% | 34% / none / 66% | 51% / none / 49% | Democrats if she wins |
| **Independent, caucusing with neither** (8%) | 36% / none / 64% | 53% / none / 47% | 70% / none / 30% | Neither: a free vote in a close Senate |
| **Retires** (30%; she is 71 in 2028) | open: Democrat 3% | 9% | 19% | The winner's party |

With ranked-choice voting repealed (15% assumed), a Republican Murkowski must first win a closed primary against Dunleavy (assumed 30%). If she wins it, she is the nominee against a Democrat and wins about 30% of runs in every environment. If she loses and runs as an independent, she splits the anti-Dunleavy vote under plurality rules and almost never wins. As an independent from the start (either independent branch) she wins 2-11% under plurality. Her Democratic-side share as an independent caucusing with Democrats is an assumption: at her 2022 Republican-side share (16% rather than 12%) that branch rises to 48% neutral, 64% at D+3 and 79% at D+6.

**What it means.**
1. **Ranked-choice voting is what keeps her viable without her party.** If Measure 2 passes, her fate turns on a closed Republican primary, and as an independent she almost never wins. The Democratic-caucus route disappears.
2. **A strong Democrat is a spoiler for a Republican Murkowski.** In the Republican branch, the stronger the Democratic candidate, the likelier Murkowski finishes third and Dunleavy wins. A Democratic Party that wanted her to survive would field a weak nominee or none (as with Osborn in Nebraska in 2024). That buys a moderate Republican, not a Democratic seat.
3. **A caucus deal is worth least when it is likeliest to be offered.** A deal matters to Democrats only near 50-50, and with a Democratic president the model puts 50 or 51 seats at about 1%. At 56 seats her vote does not decide control. Her filibuster position also means she would not be the 51st vote for D2. She is valuable mainly as a possible Republican vote toward 60 on specific bills (permitting, appropriations, Alaska-specific items), not as a path to a rules change.
4. **Across the branches**, the Alaska seat goes to the Democratic caucus in about 8% of evidence-weighted runs. The model counts that seat; it does not count a Murkowski switch after the election, which would be a separate gain.

## 6. Espen's priors against the evidence

| Prior (Espen's words) | Model and evidence | Agree? | Why they differ, where they do |
| --- | --- | --- | --- |
| "Ohio is the riskiest dem seat to defend by a lot, and it's not close." | Ohio 21% in a neutral year and 38% at D+3; the next lowest Democratic seats are Arizona and Pennsylvania at 56% | **Yes** | Ohio's lean is R+9 even after 2026. Brown ran 7.6 points ahead of Harris in 2024 and about 3 points ahead of what Ohio's lean implied in 2026, and that brand is in the model (+4.2). It still leaves him about 5 points short in a neutral year. Ohio is the riskiest seat, but it rarely decides control (2% of 51st-seat tipping points) |
| "If it's even a neutral year I find it unlikely we lose Arizona or Georgia or Nevada seats coming off four years of Trump." | Neutral year: Arizona 56%, Georgia 71%, Nevada 60%; all three held in **30%** of runs, losing at least one in 70%. At D+3, 52%; at D+6, 73% | **No, for a truly neutral year** | All three states voted to the right of the nation in 2024 (by 4, 0.7 and 1.6 points). Nevada's 2026 governor margin, even net of Lombardo's incumbency, was below the national swing. Kelly's 25% chance of leaving the race costs Arizona about 10 points. "Coming off four years of Trump" is an argument about the environment, not about these states: if it means D+5 or better, the prior holds (73% for all three at D+6). The disagreement is whether 2028 is neutral; at a real neutral, these are lean, not safe, seats. Matching the prior takes an extra 2.5-5.5 points in each state, more than any input supports (`senate-model-outputs.md`, section 5) |
| "Realistically I actually think it's gonna be hard for us to lose the senate before 2032." | Control in January 2029: 100% with a Democratic president, 85% without. Holding 50+ through the 2031-32 Congress: 82-85% with a Democratic president | **Yes** | The 2030 class (elected in 2024's R+1.5 year) is not over-extended, so even a typical midterm penalty costs only about 2-3 seats. The danger is the **2032 election**, when the 2026 wave class is up: `2030-2034-control.md` |
| "A very solid shot to pick up the other North Carolina and Wisconsin seats in 28" | Neutral: North Carolina 45%, Wisconsin 39%, both 19%. D+3: 65%, 57%, both 38%. D+6: 81%, 74%, both 60% | **Partly**: "solid" from about D+3 | North Carolina's 2026 Senate win (D+19.6) was partly Cooper's own popularity. Wisconsin's 2026 governor margin (D+8.0) ran 5 points behind the nation. Johnson retiring (75% assumed) helps Democrats only slightly, since his own record carries no penalty in the model |
| "Maybe make some more wild map expanding plays in the south or Midwest. Montana, anyone?" | Montana is not up. At D+6: Iowa 25%, Florida 16%, Alaska 12%, Kansas 4%, Missouri 4%. At D+13: Iowa 66%, Florida 56%, Alaska 31%, Kansas 30%, Missouri 28%, South Carolina 18%, Indiana 15% | **Only in a 2026-sized year** | Expected Republican-held pickups: 0.9 seats neutral, 1.5 at D+3, 2.2 at D+6, 4.5 at D+13. Iowa is the best wild seat if Grassley retires: Democrats won both Iowa statewide races in 2026, but the state still sits about 10 points right of the nation. Spending in these seats is a bet on the environment, worth most for the 60-seat upside |
| "Murkowski is up I believe, and I could see her trying to strike a deal with Dems or even becoming an independent and caucusing with us." | She is up. A Democratic-caucusing run wins 19-51% depending on the year, but is given only a 6% chance of happening | **Fact right; the deal is unlikely and would not help D2** | She endorsed Sullivan "to keep in the majority" (January 2026) and her standing with Alaska's left collapsed in 2025. Her leverage is lowest when Democrats hold 55+, and she opposes weakening the filibuster (section 5) |

## 7. What it means for Project 2050

Options and questions, not decisions. Nothing for 2029 is decided (`dossiers/home/3-design.md`). D1 is Espen's to approve in #80, and D2 and D5 are unchanged.

**Which 2029 plans each Senate makes possible.**

| Senate in January 2029 | Chance (evidence-weighted, Democratic president) | What becomes possible |
| --- | --- | --- |
| 50-51 | about 1% | Reconciliation (R1-R3, D5) and executive action only. D2-F needs every Democrat; the fallback (G, the democracy carve-out) is likelier |
| 52-54 | about 15% | D2-F with 2-4 defections allowed. This is the legacy D1 band |
| 55-57 | about 50% | D2-F with 5-7 defections allowed, enough to absorb the institutionalists the 2027 caucus may hold (`4-2029-plan.md`). This is the center of the estimate and the top of #80's option B |
| 58-59 | about 25% | As above; a few Republican votes could reach 60 on specific bills, from a moderate pool that is smaller now that Collins has lost (Murkowski, if re-elected, is one) |
| 60+ | about 9% | Cloture without a rules change on a united caucus. Remote: 1% at D+3, 5% at D+6 |

**Reconciliation-only or regular order, by flagship.** Reconciliation passes at 51 regardless of D2. Regular order needs D2's rules change, or 60.

| Flagship | Can ride reconciliation (D5) | Needs regular order (D2 or 60) | What a 53-57 Senate means |
| --- | --- | --- | --- |
| 1. Secure floor | Child benefit, income support, paid-leave money | Social Security changes (section 310(g)); program rules that only set rules | Spending pieces are safe at 51. D8's spring-2030 bill needs D2 |
| 2. Care | Health restoration, Medicare payment reform (R1); child care, Medicare upgrades (R2) | Public option design and insurance-market rules beyond budget effects; workforce standards | Mostly reconcilable; the Byrd rule decides the edges |
| 3. Home | Rental guarantee money, building and repair money (R2) | Zoning-incentive conditions and fair-housing rules where they are not budgetary | Money at 51; conditions may need D2. Espen's housing memos are pending |
| 4. Clean power | Carbon fee and dividend, clean-energy credits (R2) | The Clean Energy Standard and permitting fixes (CLI-3) | CLI-3 needs D2: the clearest case where the Senate's size matters |
| 5. Work | Little | Labor law, wage floors, sectoral standards (the 2021 minimum-wage ruling shows the Byrd limit) | All of it needs D2 at 53-57 |
| 6. Immigration | Fees and funding only (legalization was ruled out of reconciliation in 2021) | Status for long-settled residents, legal pathways, adjudication | Needs D2, or a bipartisan bill at 60, which is out of reach without Republicans |
| Democratic renewal (DEM-1) | None | All | D2-F first, or the G carve-out |

**How the expected map compounds across 2029-2034** (details in `2030-2034-control.md`). The Senate seated in January 2029 is probably the largest of the decade:
- with a Democratic president, about 56.6 seats in 2029;
- about 54 after the 2030 midterm;
- about 49-51 after 2032.

Options this raises for Espen:
- (a) Keep D1's first-trifecta scope as written: regular-order bills in 2029-30. The model supports it, since the 2029-30 Congress has the most room for defections.
- (b) Treat R3 (the FY2031 resolution, summer 2030) as the last reconciliation bill passed with the 2029 Senate, and plan what slips from it with that in mind.
- (c) In D2's adoption resolution, weigh the choice between narrowing reconciliation from 2031 (R3) or from 2037 (R4) against a real chance of a Republican Senate from January 2033. The narrowing would then bind a Republican majority too.
- (d) Decide whether 2032 Senate defense (Texas, South Carolina, Kansas, Iowa, Mississippi, Alaska) shapes what is delivered and felt in those states by 2032.

Questions only; none is a recommendation yet.

**Notes for #80 (D1).** #80 is Espen's decision, and nothing here changes D1. Two facts bear on it:
- Its "40 not up" base also needs the Minnesota 2027 special.
- The model's center with a Democratic president (56.6) sits at the top of option B's 53-56 band. It supports B over A, and does not by itself argue for C, because 2029 is the peak.

## 8. How the model was iterated

**Round 1** built the model above, without the round 2 and 3 changes. It raised three questions:
1. Are the 2026 governor results, which feed the lean, distorted by incumbents?
2. Is the race-level error the right size?
3. Is the drop in 2032 (`2030-2034-control.md`) real or an artifact?

**Round 2.**
1. **Governors.** Split Ticket finds governor races stray about four points further from partisan lean than Senate races: average deviation 14.5 against 10.0 in 2014, 11.7 against 8.0 in 2018 [SRC-0589]. Several 2026 margins were incumbents' results: Lombardo (NV, lost by 7.6), Ayotte (NH, won by 4.3), Hobbs (AZ), Shapiro (PA). The fix nets out incumbency (3 points for a governor, 2 for a senator) and gives governor races half weight. The effect:
   - Nevada 53% → 60% in a neutral year;
   - New Hampshire 79% → 84%;
   - Arizona 60% → 56%;
   - Pennsylvania 62% → 56%;
   - seat totals unchanged.
2. **Error size.** States' 2020-24 swings varied around the national swing with an SD of 2.4. 2024 Senate margins varied around the same state's presidential margin with an SD of 5.9, including candidate effects. The model's combined state error of about 5.7, on top of explicit candidate effects, is slightly conservative, so no change.
3. **2032.** Brookings's seat-change table [SRC-0570] shows how midterm wave classes did six years later in a presidential year:

   | Wave | Six years later | Change for the wave party |
   | --- | --- | --- |
   | 1946 | 1952 | +1 |
   | 1958 | 1964 | +1 |
   | 1974 | 1980 | about −12 |
   | 1986 | 1992 | 0 |
   | 1994 | 2000 | −5 |
   | 2006 | 2012 | +2 |
   | 2010 | 2016 | −2 |
   | 2014 | 2020 | −3 |

   The median is −1 and the mean −2. In 2018, though, Democrats lost 4 of the 10 seats they held in Trump-won states (Indiana, Missouri, North Dakota, Florida) in a D+8.7 House year [SRC-0587]. The 2026 class reaches deeper into hostile states (Texas R+13.7, South Carolina R+17.9, Kansas R+16.1 in 2024) than any earlier wave class. The model's 2032 loss (about 5 seats near D+4) is therefore heavy by the long-run base rate but in line with the polarized era. It stays, with the base rate reported beside it.

**Round 3.**
1. **The Electoral College bias.** Computed from the data: 3.8 points in 2020 and 0.2 in 2024, so 1.0 is kept. Testing 0 and 3 changes nothing at D+3 (control 99-100%).
2. **Murkowski's crossover.** Her 2025 approval collapse and her Sullivan endorsement [SRC-0590] [SRC-0591] lowered her assumed Democratic-side share from 45-80% to 35-70%, and the Democratic-caucus branch from 10% to 6%.
3. **Her filibuster position** [SRC-0592] moved the Murkowski reading from "possible 51st vote" to "possible Republican vote toward 60 on specific bills." That changed the section 7 text, not the numbers.

## 9. Limits

- **The environment is the dominant input,** and it is an assumption. Every row shows its environment for that reason.
- **Candidate effects come from one past race,** shrunk toward zero. The model knows nothing about 2028 nominees, scandals or primaries beyond the three drawn candidacies and Fetterman's extra uncertainty.
- **No polling is used;** none exists for 2028 races yet.
- **Inputs are typed from sources,** and Wikipedia's tables are crowd-edited [SRC-0575] [SRC-0576]. Margins agree with `1-results.md` and `5-senate-2028.md` to within 0.1 points, apart from the source differences noted there.
- **Money enters only as context.**
- **The regional blocs are a simple correlation structure,** not a demographic model.

## Next questions

1. **The certified count.** Recheck after November 18-25: the Alaska and Mississippi results (they set 37-39 of the base), the Measure 2 result (it decides whether the Murkowski branches matter) and the certified 2026 margins.
2. **The Minnesota 2027 special.** Who Klobuchar appoints, and whether Republicans recruit seriously. It is one full seat in every 2029 scenario.
3. **Retirements,** in order of effect: Kelly (presidential decision), Grassley (2027), Johnson, Murkowski, Cortez Masto. Kelly alone moves Arizona by about 10 points.
4. **First published ratings** (Cook, Sabato, Inside Elections) and the first 2028 polls, to check the model's lean and candidate effects against independent judgment.
5. **The 2027 caucus count for D2-F.** Which Democrats would vote against graduated cloture? The margin for defections is 5-10 seats in this model, and the number of likely defectors decides whether that is enough. This connects to `4-2029-plan.md` (D2).
6. **Byrd-rule edges for each flagship.** The table in section 7 is a first sort. The care, housing-conditions and paid-leave edges need a parliamentarian-precedent check before the 2029 vehicles are fixed (D5).
7. **A demographic correlation structure.** For example, by education and Hispanic share, to test whether Arizona, Nevada and Georgia (or Wisconsin, Ohio and Iowa) move together more than the regional blocs allow.
