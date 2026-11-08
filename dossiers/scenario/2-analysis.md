# Why it happened: the data and the competing readings

Role: a review of the survey data and published analysis on why the 2026 midterms went as they did, five days after the vote. Status: draft (stage B, step 1), read November 8, 2026. Data (survey toplines and crosstabs) are kept apart from analysis (interpretations of cause), as `charter/STANDARDS.md` requires (`DEC-2026-10-28-07`). No reading here is adopted; the competing readings are set side by side for Espen. Results themselves are in `1-results.md`.

## In brief

- **One survey, not three.** In 2026 AP VoteCast, the Edison exit poll and Fox News Voter Analysis were folded into one study, **The Voter Poll by SSRS** (about 80,000 registered voters, October 19-November 3), which AP, ABC, CBS, CNN, Fox, NBC and MS NOW each publish in their own cut [SRC-0489] [SRC-0490]. Outlets' numbers therefore agree by construction, and **any comparison with 2024 or 2018 exit polls crosses a change of method** [SRC-0500].
- **The data point one way on mood and several ways on cause.** Voters were sour (75% rate the economy poor or not so good), disapproved of Trump (37-38% approve), and said by 44% to 16% that their vote expressed opposition rather than support [SRC-0489]. Cost of living, corruption and the Iran war each mattered to large majorities, and the survey cannot say which one moved votes.
- **Thirteen readings are in circulation**, from a referendum on Trump to a moderate-candidate effect to a left mandate (section 3). Most agree on the mood; they split on what Democrats should take from it. Several headline readings outrun their own numbers (section 4).
- **The decisive evidence is months away.** Validated voter-file studies separate turnout from persuasion; Pew's arrives around mid-2027 and Catalist's around spring 2027 (section 5). Until then, every causal claim here is provisional.

## 1. Data: who voted how (The Voter Poll by SSRS, national House vote)

From the Fox News cut, read November 8 (live page, latest weighting) [SRC-0489]. Changes against 2024 are NPR's, comparing the 2026 SSRS data with 2024 Edison exit polls (method break) [SRC-0500].

| Group | Share of voters | D | R | Change in D margin since 2024 (NPR) |
| --- | --- | --- | --- | --- |
| All House voters | | about 55 | about 43 | about +15 (Cook's count, `1-results.md`) |
| Men / women | 47 / 53 | 50 / 59 | 48 / 40 | +16 / +13 |
| Ages 18-29 | 11 | 73 | 25 | +34 |
| Ages 65+ | 36 | 50 | 50 | |
| White / Black / Latino | 73 / 9 / 10 | 49 / 90 / 64 | 49 / 9 / 34 | Latino +21 |
| College graduates / no degree | 47 / 53 | 63 / 48 | 35 / 50 | |
| White, no degree (men; women) | 18; 19 | 35; 41 | 63; 57 | |
| Income under $50,000 | 27 | 57 | 41 | |
| Union household | 16 | 60 | 38 | |
| Rural | 35 | 41 | 57 | |
| Independents | 8 | 58 | 32 | |
| Moderates | 41 | 66 | 32 | |
| 2024 Trump voters | 44 | 7 | 91 | |
| 2024 non-voters | 4 | 70 | 25 | |

The Latino margin varies by source: Nate Cohn cites 69-29 from New York Times estimates against the Voter Poll's 64-34 [SRC-0497]. Expect such gaps until validated data arrive.

## 2. Data: mood, issues and Trump (same survey unless noted)

| Item | Result | Source |
| --- | --- | --- |
| Trump approval among voters | 37% approve, 63% disapprove (54% strongly); CBS's cut has 38%, "lowest for a president in a midterm" | [SRC-0489] [SRC-0492] |
| Vote meant to express | Opposition to Trump 44%, support 16%, not a factor 40% (an earlier weighting had 43%, the figure in the input docs) | [SRC-0489] [SRC-0503] |
| Economy | Excellent or good 25%, poor or not so good 75%; family finances worse than two years ago 44%, better 18% | [SRC-0489] |
| Inflation hardship | Severe 21%, moderate 58% | [SRC-0489] |
| "Very concerned" about costs | Gas 59%, groceries 59%, health care 59%, utilities 53% | [SRC-0489] |
| How much each mattered (crucial; crucial or major) | Corruption 55%; 90%. Cost of living 49%; 89%. Iran war 34%; 74%. Immigration enforcement 36% crucial (these voters went Republican 57-42) | [SRC-0489] |
| Most important of six issues | Economy 39, state of democracy 33, immigration 14, health care 8, foreign policy 4, crime 3 | [SRC-0489] |
| Blame for prices | More because of Trump's policies 63%, factors outside his control 37% | [SRC-0489] |
| Tariffs | Hurt the national economy 66%, helped 21% | [SRC-0489] |
| Iran war | Wrong decision 63%; about a quarter of Republicans say so | [SRC-0489] [SRC-0492] |
| Immigration enforcement | Gone too far 58%, not far enough 20%; ICE approval 40% | [SRC-0489] |
| Party better on (D-R) | Health care 50-30; foreign policy 45-38; economy 44-37; taxes 40-38; corruption 37-30; immigration 41-43 | [SRC-0489] |
| Party favorability | Democratic 47-52; Republican 40-60; about one in five Democratic voters view their own party unfavorably | [SRC-0489] [SRC-0490] |
| Checks on the president | Congress doing "not enough" to check him: 71%, about 4 in 10 Republicans included | [SRC-0489] [SRC-0490] |
| AI and data centers | A crucial or major factor for 56%; 76% oppose a data center in their own community | [SRC-0489] |
| Health costs | 55% say the administration made their own costs worse; they voted 83% Democratic. In seven battleground states, voters "very concerned" about health costs backed Democratic Senate candidates about 2 to 1 after favoring Trump 54-44 in 2024 | KFF [SRC-0494] |

**Two figures in the input docs, checked.**
- "Voters trusted Democrats more on health costs (42% to 22%) and on the cost of living (39% to 25%)" is **real but from a different study**: KFF's own September tracking poll (fielded September 16-21, released October 6), not a post-election survey [SRC-0495]. KFF's post-election analysis has Democrats ahead on health care 50-30, their largest issue lead [SRC-0494].
- "About a third of Democratic voters identify as democratic socialists" comes from a July 2026 CNN/SSRS poll of adults. The Voter Poll is consistent with it: 17% of all voters are Democrats who call themselves democratic socialists, about 35% of Democrats including leaners by this project's arithmetic [SRC-0489]. AEI's Karlyn Bowman reports 21% of Democrats, which does not reconcile with the Fox table [SRC-0499]; recheck against the SSRS crosstab. "Moderates were about half the winning coalitions in flipped Senate states" has **no source found**; national arithmetic gives about 49% of the Democratic House vote, but state crosstabs are needed.

**Turnout and composition (data and model).** G. Elliott Morris estimates from county data that Black turnout in the Deep South held at about 96% of 2024 levels against about 71% for other voters, and that without that shift Hyde-Smith would lead Mississippi by about 4 points [SRC-0498]. The Brennan Center reports the smallest white-Black turnout gap in Georgia of any midterm in 20 years [SRC-0488]. Both are estimates from aggregate data, not validated voter files.

## 3. Analysis: the competing readings

Each row is an interpretation. Its supporting and cutting data come from sections 1-2. "Who" names the publisher and its stake, as `charter/STANDARDS.md` asks.

| Reading | Who argues it (stake) | Data that support it | Data that cut against it |
| --- | --- | --- | --- |
| **1. A referendum on Trump** | National Review editors (Trump-skeptical right) [SRC-0503]; Nate Silver (independent analyst) [SRC-0496]; AP [SRC-0491] | Approval 37-38%; opposition 44% against support 16%; 62% say he puts his own interests first | Trump says he "wasn't on the ballot" [SRC-0508]; 40% said he was not a factor |
| **2. Costs and affordability** | Third Way (centrist Democrats) [SRC-0510]; Teixeira and Baharaeen (center-left) [SRC-0512]; Caitlin Flanagan in The Free Press [SRC-0505]; UBS [SRC-0516] | 89% call cost of living crucial or major; voters for whom it was crucial went D 66-32; 63% blame Trump for prices | Corruption was crucial for more voters (55%) than costs (49%); Democrats lead on the economy only 44-37 |
| **3. Tariffs** | National Review [SRC-0503]; Washington Post's Arnsdorf (news analysis) [SRC-0501] | 66% say tariffs hurt the economy | No separate vote-factor item; tariffs fold into prices |
| **4. The Iran war and gas prices** | Vance ("The reason we lost is the war"); The Federalist (pro-Trump, anti-war right) [SRC-0504]; Matt Walsh [SRC-0506] | 74% crucial or major, D 64-34 among them; 63% say wrong decision | Only 34% call it crucial, below corruption and costs; the environment was poor for Republicans before the war began on February 28 (National Review concedes this) [SRC-0503] |
| **5. Health care and the lapsed ACA credits** | KFF (nonpartisan health research) [SRC-0494]; Third Way [SRC-0510] | Democrats' largest issue lead, 50-30; 55% say their costs got worse | Health care was the top issue for only 8% |
| **6. Corruption and checks on power** | AP [SRC-0491]; House Democrats (Garcia's "LAWYER UP") | Corruption crucial for 55% (D 63-35); democracy top issue for 33%; 71% want more checks | Democrats lead on corruption only 37-30, 32% neither; Third Way's battleground poll: 73% want a focus on affordability, 17% on investigating Trump [SRC-0510] |
| **7. Immigration enforcement backlash** | Progressive members (Jayapal) [SRC-0513]; NPR on the Latino swing [SRC-0500] | 58% say enforcement has gone too far; ICE approval 40%; Latino swing of about 21 points | Republicans still lead on immigration 43-41, and enforcement-crucial voters went Republican |
| **8. Candidates: moderates delivered** | Third Way, "Moderates made Democratic majorities" [SRC-0511]; CNN's Aaron Blake [SRC-0509] | Moderate Senate picks ran about 16-26 points ahead of Harris, the four Sanders-endorsed candidates in key races 0-10 points; center-left endorsees flipped 29 House seats | DSA candidates ran furthest ahead of Harris (+16.5, n=7) against Blue Dogs +15.4 and New Democrats +14.1 (Morris's tabulation, cited by Blake); three of the four "worst" won; the gaps are small next to a 15-point wave |
| **9. Turnout, not persuasion** | G. Elliott Morris (data journalist) [SRC-0498]; Arnsdorf: fewer Republicans voted [SRC-0501] | Deep South Black turnout held while others fell | 7% of 2024 Trump voters crossed over and 2024 non-voters went D 70-25; recalled 2024 votes mix turnout with misreporting. Only validated files can split the two |
| **10. Redistricting backfired** | CBS (Linton) [SRC-0502]; ABC [SRC-0471]; UBS [SRC-0516] | Republicans lost most of the seats they redrew (about two-thirds by ABC's count) | An amplifier of the wave, not its cause; California's Democratic map added about five seats |
| **11. Fundamentals: the sixth-year midterm** | National Review [SRC-0503]; The Federalist [SRC-0504]; NPR's 2006 analogy | Anger at 38-39% against 31% in 2024 [SRC-0499] | Does not explain the size, the second-largest House swing since World War II [SRC-0496], or the deep-red Senate flips |
| **12. A mandate for the left** (corporate power, AI, oligarchy) | Rep. Casar and the Progressive Caucus; Working Families Party [SRC-0513]; DSA's record House night [SRC-0514] | 70% say the economic system favors the wealthy; 76% oppose a local data center; DSA's House contingent more than triples | Socialism favorable at 33%; liberals 26% of voters against conservatives 33%; AI crucial for only 23% |
| **13. A rejection, not a realignment** | Teixeira [SRC-0512]; National Review [SRC-0503]; Jacobin's Abbott, on class (socialist left) [SRC-0515] | Democratic Party favorability 47-52; 15% dislike both parties | Democrats lead on 7 of 8 issues tested; the Washington Post reports the first Democratic lead on the economy in over a decade [SRC-0501] |

**What most readings share.** Nearly every analyst, left to right, agrees on three things: voters were angry about prices; Trump's standing was low and his choices (tariffs, the war) were blamed; and the result punished the governing party more than it endorsed the opposition. They split on what Democrats should do with it: deliver on costs and stay broad (readings 2, 8, 13), pursue accountability (6), or move boldly left (12). That split matters for the 2027-28 framework (`3-framework-2027-28.md`, question 3).

**Trump's own account.** Voters "just weren't inspired"; "a mood in the air, I guess"; he would have won "in a landslide" had he been on the ballot [SRC-0508]. He partly blamed Iran and called Vance's war comment "largely true" while saying the war was "worth it" (reported by CBS, seen only in a search summary).

## 4. Where a headline outruns its own numbers

| Piece | Headline claim | What its own data show |
| --- | --- | --- |
| CNN, Blake: "bad news for progressive Democrats" [SRC-0509] | Moderates are the fruitful path | Most named progressives won; the tabulation it cites has DSA candidates overperforming most |
| The Federalist: Iran is "the best explanation" [SRC-0504] | The war and gas prices drove the loss | On "crucial" ratings Iran (34%) trails corruption (55%) and costs (49%) |
| Third Way: "Moderates made Democratic majorities" [SRC-0511] | Moderate candidates delivered the flips | Its list of six Senate flips omits Maine, won by a progressive; "moderate" is defined by endorsement; its battleground poll showed a tied generic ballot that undershot the result [SRC-0510] |
| National Review: "less evidence ... of an ideological victory" [SRC-0503] | Republicans still trusted on taxes and immigration | Current weighting has Democrats ahead 40-38 on taxes; moderates went Democratic 2 to 1 |

## 5. Not yet available

| What | Expected | Why it matters |
| --- | --- | --- |
| Pew validated-voter study | About June-July 2027 (the 2024 study came out June 26, 2025) | Splits turnout from persuasion with voter-file matches |
| Catalist "What Happened" | About spring 2027 | Same, with a larger file |
| Final Voter Poll weights and state crosstabs | Weeks | Tests the "moderates were half the coalition" claim and the Latino margin |
| Precinct and county swing datasets | Weeks | Only snippet-level claims so far |
| Post-election analysis not yet found | Recheck by mid-November | Cook (Walter, Wasserman), Sabato's Crystal Ball, Split Ticket, The Dispatch, the Wall Street Journal editorial board, Patrick Ruffini, Kristen Soltis Anderson, Navigator, Data for Progress, Blue Rose Research |

A reading should not be relied on in the plan until an independent publisher supports it (`DEC-2026-10-28-07`). On present evidence, readings 1 and 2 have the broadest independent support across the spectrum; readings 8, 9 and 12 are the most contested and the most dependent on data not yet published.
