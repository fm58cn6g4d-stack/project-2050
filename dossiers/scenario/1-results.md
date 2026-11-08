# The 2026 results record

Role: what the November 3, 2026 elections produced, kept apart by certainty: races called by a reputable desk; uncalled races with a clear projection; races still genuinely open; then margins, shifts from 2024, turnout and state government changes. Status: draft (stage B, step 1). **Every figure is unofficial, read on November 8, 2026 (ET evening of November 7) unless another date is given.** No state has certified. Section 6 lists what to recheck and when.

Sources are cited by `SRC-` ID (`library/catalog.csv`); all are citation rows, since news and results pages are licensed. Analysis of why it happened is in `2-analysis.md`, not here.

## In brief

| | Called | Uncalled, projected | Open | Most likely final |
| --- | --- | --- | --- | --- |
| **Senate** | D 54, R 44 (the 54 counts two independents who caucus with Democrats) [SRC-0440] [SRC-0457] | Mississippi: Colom (D), high confidence | Alaska: Peltola (D) leads on first choices; ranked-choice count November 18 | **55 or 56 D.** 56 only if Peltola holds on after ranked-choice transfers |
| **House** | D 254, R 162, 19 uncalled (AP, November 7) [SRC-0460] [SRC-0462] | At least 256 D (two California seats are Democrat against Democrat) | About ten seats within about 1 point; two Louisiana runoffs on December 12 | **About 256-263 D, centered near 259-260.** NBC estimates 259 [SRC-0463] |
| **Governors** | D 28, R 20 [SRC-0474] | Kansas: Holscher (D); Alaska: Kreiss-Tomkins (D) | None at the governor level | **30 D, 20 R** (from 24 D, 26 R before) |
| **Legislatures** | 12 chambers flipped to Democrats, none to Republicans (NCSL) [SRC-0477] | | Georgia House not yet called by Ballotpedia | Trifectas about 22 D, 18 R (from 16 D, 23 R) [SRC-0475] |

Espen expected Alaska and "MI" Senate to be uncalled but projected, and a final House count above 255. Two corrections: **Michigan is called** (AP projected El-Sayed early on November 4 [SRC-0443]); the second uncalled Senate race is **Mississippi**, which may be the race meant. And **Alaska is closer than "clear"**: it is a projection at low confidence (section 2). The House expectation holds: above 255 is very likely.

What this does to the arithmetic, before analysis: Democrats hold both chambers from January 3, 2027, short of a veto override in either (290 House and 67 Senate votes) and short of cloture without Republicans (60 votes: 5 Republicans at 55 seats, 4 at 56). The framework in `3-framework-2027-28.md` starts there.

## 1. Called races

### Senate: 33 of 35 called by AP

AP's call status from the States Newsroom dataset built on AP calls (CSV version of November 8, 02:48 UTC) [SRC-0444] and AP's balance-of-power box (article modified November 4) [SRC-0440]. Vote shares from the civicAPI results feed (observed November 8, 02:49 UTC) [SRC-0445], which aggregates official counts; it is not AP's tabulation. DDHQ shows the same calls [SRC-0457]. Call times are given where an opened page stated them; for most races they were not found.

| State | Winner | Loser | Margin (pts) | Flip | 2024 pres. margin | Shift toward D |
| --- | --- | --- | --- | --- | --- | --- |
| Texas | Talarico (D) | Paxton (R) | D+12.1 | **R to D** (Cornyn lost the primary) | R+13.7 | 25.8 |
| North Carolina | Cooper (D) | Whatley (R) | D+19.6 | **R to D** (open, Tillis) | R+3.2 | 22.8 |
| South Carolina | Andrews (D) | Darline Graham (R, appointed July 2026) | D+4.5 | **R to D** | R+17.9 | 22.4 |
| Kansas | Hamilton (D) | Marshall (R, inc.) | D+5.1 | **R to D**; first Democratic senator from Kansas since 1932 (AP) | R+16.1 | 21.2 |
| Iowa | Turek (D) | Hinson (R) | D+4.1 | **R to D** (open, Ernst); AP call just after 11:30 p.m. ET Nov 3 [SRC-0443] | R+13.2 | 17.3 |
| Ohio (special) | Sherrod Brown (D) | Husted (R, inc.) | D+4.9 | **R to D** | R+11.2 | 16.1 |
| Maine | Troy Jackson (D) | Collins (R, inc.) | D+6.1 | **R to D**; Collins conceded early Nov 4 | D+6.9 | -0.8 |
| Georgia | Ossoff (D, inc.) | Collins (R) | D+18.0 | | R+2.2 | 20.2 |
| Michigan | El-Sayed (D) | Rogers (R) | D+7.0 | (D hold, open) | R+1.4 | 8.4 |
| New Hampshire | Pappas (D) | Sununu (R) | D+13.7 | (D hold, open) | D+2.8 | 10.9 |
| Minnesota | Flanagan (D) | Tafoya (R) | D+10.1 | (D hold, open) | D+4.2 | 5.9 |
| Illinois | Stratton (D) | Tracy (R) | D+24.3 | (D hold, open) | D+10.9 | 13.4 |
| Virginia | Warner (D, inc.) | Mizusawa (R) | D+22.8 | | D+5.8 | 17.0 |
| New Jersey | Booker (D, inc.) | Murphy (R) | D+27.3 | | D+5.9 | 21.4 |
| New Mexico | Luján (D, inc.) | Marker (R) | D+26.5 | | D+6.0 | 20.5 |
| Colorado | Hickenlooper (D, inc.) | Baisley (R) | D+25.4 | | D+11.0 | 14.4 |
| Oregon | Merkley (D, inc.) | Smith (R) | D+19.4 | | D+14.3 | 5.1 |
| Delaware | Coons (D, inc.) | Katz (R) | D+27.1 | | D+14.7 | 12.4 |
| Massachusetts | Markey (D, inc.) | Deaton (R) | D+31.2 | | D+25.2 | 6.0 |
| Rhode Island | Reed (D, inc.) | McKay (R) | D+37.5 | | D+13.8 | 23.7 |
| Louisiana | Letlow (R) | Davis (D) | R+1.8 | | R+22.0 | 20.2 |
| Florida (special) | Moody (R, inc.) | Nixon (D) | R+2.9 | | R+13.1 | 10.2 |
| Nebraska | Ricketts (R, inc.) | Osborn (I) | R+6.2 | | R+20.5 | 14.2 (against an independent) |
| Alabama | Moore (R) | Wess (D) | R+9.4 | (R hold, open) | R+30.5 | 21.0 |
| Montana | Alme (R) | Bodnar (I); Bankhead (D) 12% | R+10.6 | (R hold, open) | R+19.9 | 9.3 (against an independent) |
| Arkansas | Cotton (R, inc.) | Shoffner (D) | R+11.9 | | R+30.6 | 18.8 |
| Kentucky | Barr (R) | Booker (D) | R+12.1 | (R hold, open) | R+30.5 | 18.5 |
| Tennessee | Hagerty (R, inc.) | Bradshaw (D) | R+12.2 | | R+29.7 | 17.5 |
| Oklahoma | Hern (R) | Thomas (D) | R+17.9 | | R+34.3 | 16.3 |
| West Virginia | Capito (R, inc.) | Anderson (D) | R+20.4 | | R+41.9 | 21.4 |
| South Dakota | Rounds (R, inc.) | Bengs (I) | R+21.0 | | R+29.2 | 8.2 (against an independent) |
| Idaho | Risch (R, inc.) | Achilles (I) | R+23.0 | | R+36.5 | 13.5 (against an independent) |
| Wyoming | Hageman (R) | Byrd (D) | R+30.5 | (R hold, open) | R+45.8 | 15.3 |

2024 presidential margins are from the state results table on Wikipedia [SRC-0459]; shift is the 2026 Senate margin minus the 2024 presidential margin, a rough measure (candidates and turnout differ). Every race but Maine moved toward Democrats, most by 10 to 26 points. Control was called for Democrats by DDHQ at 11:19 p.m. ET on November 3 [SRC-0457].

### House: 254 D, 162 R called (AP, November 7)

| Count | D | R | Uncalled | When |
| --- | --- | --- | --- | --- |
| AP, as reported by outlets carrying AP calls [SRC-0460] [SRC-0461] and Fox's AP-based results page [SRC-0462] | 254 | 162 | 19 | November 7 (Fox: 9:38 p.m. ET) |
| NBC News Decision Desk [SRC-0463] | 252 | 162 | 21 | November 7, 9:09 p.m. ET (date inferred) |
| Cook Political Report tracker [SRC-0464] | 253 | 161 | 21 | November 7 |

**Outlets disagree by one or two seats** because they call at different times. They also disagree on the **net gain** (Fox +42, NBC +41, CNN +44 for 259), because each measures against a different notional baseline for the redrawn districts. 254 is 39 more than the 215 seats Democrats won in 2024, so quote seat totals, not net gains.

**Flips.** CBS (November 6) and Fox (November 7) count **44 seats to Democrats and 2 to Republicans** (TX-32, TN-9); NBC counts 43 and 2 [SRC-0468] [SRC-0462] [SRC-0463]. Some outlets count UT-1, a new seat, as a flip and some do not. Defeated Republican incumbents include the NRCC chair, Richard Hudson (NC-9), and Lawler, Fitzpatrick, Valadao, Kean, Perry, Kiggans and Steil [SRC-0468] [SRC-0467]. The full list is on the CBS page [SRC-0468]; it is not repeated here.

### Governors: 34 of 36 called

Ballotpedia and NCSL agree: **28 D, 20 R, 2 uncalled** (Ballotpedia, November 6, 4:00 p.m. ET) [SRC-0474] [SRC-0477]. Democrats flipped **five** seats and lost none:

| State | Winner | Loser | Margin (pts, NBC [SRC-0483]) | Called |
| --- | --- | --- | --- | --- |
| Texas | Hinojosa (D) | Abbott (R, inc.) | D+7.1 | AP call reported 10:12 p.m. CT Nov 3; Abbott conceded |
| Ohio | Acton (D) | Ramaswamy (R) | D+7.9 | Ballotpedia call 10:31 p.m. ET; NBC projected |
| Georgia | Lance Bottoms (D) | Jackson (R) | D+8.6 | DDHQ and NYT, 9:13 p.m. ET |
| Nevada | Ford (D) | Lombardo (R, inc.) | D+7.6 | NYT, 7:08 a.m. ET Nov 4 |
| Iowa | Sand (D) | Lahn (R) | D+11.0 | Ballotpedia call 9:58 p.m. ET |

Democrats held Arizona (Hobbs), Michigan (Benson), Minnesota (Klobuchar), Pennsylvania (Shapiro) and Wisconsin (Crowley). Republicans held Florida, New Hampshire (Ayotte), Vermont (Scott) and Nebraska among others. Call times above are Ballotpedia's record of who projected each race; AP, CNN and NBC call times were mostly not found [SRC-0474].

## 2. Uncalled races with a projection

| Race | Current margin | Outstanding | Key dates | Projection and source | Confidence (this project's) |
| --- | --- | --- | --- | --- | --- |
| **Senate, Mississippi:** Colom (D) v. Hyde-Smith (R, inc.) | Colom +2,574 (AP, Nov 6, 5 p.m.) [SRC-0455]; AP's explainer says "nearly 2,500" [SRC-0442] | About 30,000 by AP's estimate (revised down from 44,000), mostly affidavit (provisional) ballots, plus late absentees [SRC-0442] | Nov 10: absentee receipt and ID-cure deadline. Nov 13: counties certify. CNN cites a Dec 3 certification deadline, which has not been reconciled with Nov 13 [SRC-0456]. No automatic recount: only a court can order one [SRC-0454] | Mississippi Free Press: Hyde-Smith's paths "dimming" as affidavits break for Colom [SRC-0455]. DDHQ's race page still shows a Hyde-Smith 91% forecast, apparently its stale pre-election figure [SRC-0457] | **High, about 85-90% Colom.** Hyde-Smith would need about 54% of every remaining ballot, and the affidavits counted so far favor Colom. The risk is litigation over affidavit ballots: the NRSC demanded all 82 counties segregate them, and Colom's lawyers call that unlawful [SRC-0456] [SRC-0454] |
| **Senate, Alaska:** Peltola (D) v. Sullivan (R, inc.), plus Heikes (R) and Daniel J. Sullivan Jr. (no party) | Peltola +637 on first choices, 48.2% to 47.9% (Division of Elections, Nov 4) [SRC-0446]; AP has +626 at about 74% counted [SRC-0441] | About 60,000: about 20,000 early votes and about 40,000 absentees (ADN, Nov 6) [SRC-0449]. No cure process | Nov 9-10 and Nov 13 releases; Nov 18 overseas deadline and **ranked-choice tabulation**; Nov 25 certification target; recount applications about Nov 30; contests about Dec 5 [SRC-0447] [SRC-0448] | FairVote's preliminary ranked-choice run on partial ballot data: Sullivan 51.2, Peltola 48.8; it says transfers move the race about 0.5 points toward Sullivan [SRC-0453]. Late ballots have leaned Democratic in past Alaska counts (FairVote, citing Alaska Public Media). DDHQ: Peltola 60% [SRC-0457]. The input Ledger says 75-80% | **Low, about 55-65% Peltola.** By this project's arithmetic from FairVote's transfer rates, Heikes's and Daniel J. Sullivan Jr.'s second choices net Sullivan about 950 votes against Peltola's 637, so Peltola needs the outstanding ballots to favor her by roughly half a point more than those counted. That is plausible, not clear. Treat as nearly open |
| **House, final total** | 254 D called; 2 California seats are D v. D (CA-4, CA-7) [SRC-0469] | 19 uncalled (AP) | Counts finish through mid-November; Louisiana runoffs Dec 12 | NBC 259 D [SRC-0463]; CNN "259, could hit or exceed 260" (Nov 5) [SRC-0466]; CBS pace 256 within 251-268 (Nov 5) [SRC-0467]; Jeffries (a party claim) "at least 255" | **Above 255: very high, about 95%** (254 plus the two D v. D seats is 256). **About 259-261 most likely**; 264 would need comebacks where Republicans lead |
| **Governor, Kansas:** Holscher (D) v. Masterson (R) | Holscher +7,045, 0.64% (Nov 4) [SRC-0480]; "just over 7,000" (Nov 6) [SRC-0481] | Provisionals, number unknown | A margin under 1% triggers a hand-count audit of 10% of precincts; counties certify by Nov 16; recount requests by 5 p.m. Nov 17 [SRC-0480] | Holscher declared victory and Gov. Kelly called her governor-elect; Masterson has not conceded [SRC-0481] | **High, about 90% Holscher** |
| **Governor, Alaska:** Kreiss-Tomkins (D) v. Wilson (R) and others | Kreiss-Tomkins 49% of first choices, Wilson 29% [SRC-0482] | 50,000-75,000 [SRC-0482] | Ranked-choice tabulation Nov 18 | FairVote: the margin shrinks about 9.5 points in the ranked-choice count; a snippet gave a 55-45 final round (not on the opened page) [SRC-0453]. MultiState lists it as called; AP and NBC do not | **Moderately high, about 80-85% Kreiss-Tomkins**: a Republican win needs near-total ranking discipline among the other Republican candidates' voters |

**Litigation in Alaska.** On the President's order, the Justice Department sued about October 22 to block certification unless Sullivan won and to set aside ballots for Daniel J. Sullivan Jr., whom the NYT reported Democratic operatives recruited (Peltola denies knowledge). Judge Sharon Gleason dismissed the suit on November 1 for lack of standing; the Justice Department appealed to the Ninth Circuit, where briefing is not expected before January 11 [SRC-0451] [SRC-0449]. Peltola's campaign filed a public-records suit over rejected absentee ballots on November 6 [SRC-0450]. Whether Gov. Dunleavy would certify a Peltola win was not answered on any page read.

## 3. Genuinely open

| Race | Where it stands | When it resolves |
| --- | --- | --- |
| House NC-5 | Hubbard (D) leads Foxx (R, inc.) by 99 votes, 87% counted [SRC-0469] | Count and likely recount |
| House NC-3, MN-1, TN-4 | Each under 350 votes; R leads NC-3, D leads MN-1 and TN-4 [SRC-0469] [SRC-0466] | Count; recounts possible |
| House FL-7, FL-9, FL-27, NC-7, CO-4 | Within about 1 point; CO-4 (Laubacher D over Boebert) counties count until Nov 13, with a recount inside 0.5% [SRC-0473] [SRC-0460] | Mid-November |
| House ME-2 | LePage (R) under 50%, so Maine's ranked-choice count may apply [SRC-0463] | Late November |
| House AZ-2, CA-23 | Republicans lead with 20-25% of the vote left [SRC-0469] | Mid-November |
| House LA-5, LA-6 | Runoffs; both lean Republican, LA-6 redrawn to Trump+32 after *Louisiana v. Callais* [SRC-0470] | December 12 |
| Kansas attorney general | Mann (D) leads Kobach (R, inc.) by about 12,800; audit under way [SRC-0486] | Nov 16-17 |
| Ohio attorney general | Kulewicz (D) leads by about 28,000, 102,000 provisionals out; he says Faber conceded [SRC-0486] | Canvass |
| Georgia House | Democrats reached 91 seats by a local count; one runoff Dec 1 and a 27-vote seat [SRC-0476] | December |
| Alaska Measure 2 (repeal ranked-choice voting) | "No" leads 52-48 [SRC-0484] | November 18 |

The polling-desk figures for close House races come from an unofficial aggregator and were checked against named outlets where possible; outstanding ballot counts were not found for any House race.

## 4. Margins and shifts from 2024

| Measure | 2026 | 2024 | 2018 | Source |
| --- | --- | --- | --- | --- |
| **National House vote** | D 55.7%, R 42.8%: **D+12.9** (D+13.1 two-party), 114 million votes counted | R+2.7 (Cook's final tracker; other sources give R+2.6) | D+8.6 (not opened; to verify) | Cook trackers [SRC-0464] [SRC-0465] |
| Swing in the House vote | **About 15.6 points toward Democrats** (this project's arithmetic on Cook's figures); Silver calls it the second-biggest midterm swing since World War II | | | [SRC-0496] |
| Battleground House districts | Average moved almost 16 points toward Democrats against the 2024 presidential margin (20 of 28 battlegrounds at 95% counted) | | | NBC, Nov 5 [SRC-0472] |
| Senate | Every race except Maine moved toward Democrats against the 2024 presidential margin; flipped states moved about 16-26 points | | | Table above; CBS charts [SRC-0517] |
| **Turnout** (voting-eligible population) | **About 49.4%, about 124 million ballots** (preliminary; one secondary source has 49.1%) | | 50.05%; 2022 about 46.8% (snippet) | McDonald [SRC-0487] |

CNN notes a 13-point House win would be the largest since 1976, and only the second double-digit win since 1982 [SRC-0466]. Iowa's turnout, about 63%, was its highest midterm in about 30 years; Georgia's Black turnout rose sharply against 2022 (Brennan Center) [SRC-0488].

**Redistricting.** The mid-decade redraws mostly failed to hold against the wave. In Texas Republicans gained only TX-32 of five targets while Democrats flipped TX-15 and TX-23; California's Proposition 50 map gave Democrats about four or five seats; Virginia's Democratic redraw was voided by its Supreme Court; Missouri voters rejected the new map 38-62; Utah's court map produced a Democratic seat; Indiana's and South Carolina's efforts failed in the legislature [SRC-0470] [SRC-0471] [SRC-0484]. *Louisiana v. Callais* (April 29, 2026, 6-3) narrowed Section 2 of the Voting Rights Act; new maps followed in Alabama (Figures held), Louisiana (LA-6 eliminated) and Tennessee (TN-9 flipped Republican) [SRC-0470]. Whether redistricting cost Republicans seats on net is analysis, covered in `2-analysis.md`.

**County and precinct swing.** Only snippet-level figures exist yet (for example, a claim that 94% of counties shifted left). They are not recorded until a full dataset is published.

## 5. State government

**Legislatures.** NCSL counts **12 chambers flipped to Democrats, none to Republicans**: both Arizona chambers, Georgia House, Michigan House, Minnesota House (from a tie), both New Hampshire chambers, North Carolina House, Pennsylvania Senate, Texas House, and both Wisconsin chambers [SRC-0477]. Ballotpedia has not yet called the Georgia House, and its own page gives both 11 and 12 changes [SRC-0476]. The Texas Tribune projects the Texas House at 83 D, 67 R if leads hold; the Texas Senate stays 19 R, 12 D [SRC-0479]. Republicans lost supermajorities in eleven chambers, so in Iowa, Ohio and North Carolina they now need Democratic votes to override a Democratic governor (AP) [SRC-0476].

**Trifectas.**

| Source | Before (D / R / divided) | After (D / R / divided / uncalled) |
| --- | --- | --- |
| Ballotpedia, Nov 6 [SRC-0475] | 16 / 23 / 11 | **22 / 18 / 8 / 2** |
| NCSL, Nov 5, "anticipated" [SRC-0477] | 16 / 23 / 10 | 23 / 17 / 10 |

The two disagree: NCSL's figures appear to assume the Alaska and Kansas outcomes. **New Democratic trifectas: six**, Michigan, Minnesota, Nevada, Pennsylvania, Wisconsin and **Arizona** (the input docs list five; Arizona's legislature is called so far only by State Navigate, via Ballotpedia). **Republican trifectas broken: five**, Georgia, Iowa, Ohio, Texas and New Hampshire [SRC-0475] [SRC-0478].

**Election administration for 2028.** Democrats gained six secretary of state offices, including Georgia, Indiana and Ohio, and won the open seats in Michigan and Wisconsin; Arizona's Fontes and Nevada's Aguilar were re-elected [SRC-0485]. Democrats gained attorney general seats in Georgia, Iowa and Texas [SRC-0486].

**Ballot measures with policy weight** (Ballotpedia, cached November 7) [SRC-0484]: Missouri voters defeated an abortion-ban amendment 45-55 and rejected the mid-decade congressional map 38-62; Nevada and Virginia approved abortion-rights amendments; South Dakota rejected ending Medicaid expansion; Washington rejected repealing its millionaire's tax 42-58; California approved $10 billion of housing bonds and extended its top income tax rates; North Carolina capped its income tax at 3.5%; voter ID passed in Nevada, North Carolina and Ohio and failed in Arizona, California and Colorado. California's billionaire wealth tax (Proposition 40) trails 46-54, uncalled. No November minimum-wage measure was found.

## 6. What to recheck, and when

| When | What |
| --- | --- |
| Nov 9-10 | Alaska count releases; Mississippi absentee and ID-cure deadline (Nov 10); Kansas county canvasses begin |
| Nov 13 | Mississippi county certification; Alaska domestic absentee deadline; Colorado county counts (CO-4) |
| Nov 16-17 | Kansas certification and recount deadline (governor, attorney general, secretary of state) |
| **Nov 18** | **Alaska ranked-choice tabulation** (Senate, governor, at-large House, Measure 2); House Democratic leadership elections Nov 18-19 |
| Nov 25-Dec 5 | Alaska certification target, recount applications, election contests; the Ninth Circuit appeal in the Justice Department's Alaska suit |
| Dec 3 | Mississippi certification as CNN reports it (reconcile with Nov 13) |
| Dec 12 | Louisiana runoffs (LA-5, LA-6) |
| Through December | Recounts in NC-5 and any seat under 0.5%; certified House popular vote; AP's final list of uncalled seats; NCSL versus Ballotpedia trifecta counts; whether Arizona's legislature is confirmed |

Data also outstanding: the final national House vote and 2018's D+8.6 from a primary source; precinct and county swing datasets; certified turnout.
