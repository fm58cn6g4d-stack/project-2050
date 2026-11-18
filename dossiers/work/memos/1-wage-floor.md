# Memo 1: The wage floor, its level and how it adjusts

Role: decision memo for Espen on the federal minimum wage (agenda LAB-4, with its options LAB-4A to 4C, and LAB-5, the small-business credit), answering section 2's questions 1 and 2 (`../2-what-works.md`, "Questions this section leaves for section 3"). Status: **decided** (`DEC-2026-11-17-01`, `-02`, `-34`, November 17, 2026): part 1 **B**, as recommended; part 2 **C, not as recommended**: B plus a small, temporary credit for employers under 50 workers during the first three steps, about $0.02-0.04 trillion over FY2030-39 (judgment, below; re-derived from the need for Espen's W7, the credit as now drafted is about $2.1 billion, provisional: "Revised for W7", below, and `../6-cost.md`, part 4, item 1). At booking it replaces the budget model's LAB-5 row of $0.10 trillion; it is not rebooked here. Espen's 2007 precedent (the Baucus-Grassley small-business package) is checked in `../notes/espen-questions-2026-11-17.md`, part a. The text below is the memo as Espen decided it; its recommendation was part 2 B. Section 4 carries the decided design. **Record correction (milestone review W-6, after the decision; it does not reopen it):** the legacy LAB-4B is "$15, then indexed to the median" (`legacy/domains/domain-labor.md`, line 100), not the price-indexed Hawley-Welch bill that part 1 C describes, so C's drawback of a bite that falls as real wages grow does not apply to the legacy option, which indexes to the median; and the legacy LAB-4C is raising the floor to two-thirds of the median over ten years with no fixed dollar step, with no commission in its description (line 101), so part 1 D's commission is this memo's addition. Espen chose B between the options as written here. Every design here, the legacy one included, is an option: the legacy file's choices are working choices, not Espen's decisions (`DEC-2026-10-30-02`). [Stage F answers, November 18: W7, the small-business credit's size, is a direction, `DEC-2026-11-18-07` (reconsider the need); W9, the territories' floor, is a direction, `DEC-2026-11-18-09`. Part 2 C stands; both stay provisional until a revision step drafts them and Espen confirms. Revised to both directions: "Revised for W7" and "Revised for W9", below.] Sources are named in plain text; bracketed tags point to `../evidence.json`. "Project arithmetic" and "judgment" mark the project's own figures, with their basis in `../3-design.md`, "What the options cost".

**Decision line.** Recommended: **part 1 B, $17 an hour reached in steps over five years from January 2030, then indexed each year to the growth of the median wage, with a standing wage commission that reports each year on how far the floor reaches nationally and by county and may recommend a higher target to Congress; part 2 B, one national schedule with a recession pause written into the statute and no small-business credit.** Cost to the federal budget: about **+$0.03 trillion over FY2030-39 (range zero to +$0.08 trillion) and about +$3-8 billion in FY2040** (judgment, scaled from CBO's 2021 score), against the legacy small-business credit's $0.10 trillion, which part 2 B drops. Evidence: quasi-experimental U.S. and German studies and reviews on both sides; CBO's scores; the United Kingdom's commission and its own data; no evaluation of circuit breakers, size phase-ins or a wage credit.

## Revised for W7: the credit sized from the need (`DEC-2026-11-18-07`)

Espen found the credit "too small" and asked to "reconsider what the need is". The decided design (`-02`, `-34`: a small, temporary credit for employers under 50 in the first three steps) is not reopened; its size is. The revision works from the need, what the floor costs the employers it targets, and then asks how much of it the credit should carry (`../tools/work_path.py --credit-options`; project arithmetic, not a score).

**The working.**
1. *The floor's whole added wage bill.* EPI's model puts the Raise the Wage Act's $17 by 2030 at about $70 billion a year in 2025 dollars, for 22.2 million workers, direct and spillover raises counted [EV-WRK-479] (an advocate's estimate; CBO's 2019 $15 option is the same order, 17 million with raises [EV-WRK-029]). That bill reaches about 58% of 2030's median; LAB-4.01's schedule reaches $17 five years later, at about 49% of the median. The bill is scaled to each year's bite: it is near zero at $7.25's 30% of the median and rises with the square of the bite above that (range: power 1.5 to 2.5; judgment), growing with wages.
2. *The share at employers under 50:* 30% (range 25-45%; judgment). Such firms hold about a quarter of private jobs and a larger share of low-wage ones; in Oregon's records, employers under 50 held 38% of jobs and 45% of minimum-wage jobs [EV-WRK-497].
3. *The need, the added wage cost at employers under 50 (calendar years, $ billion):*

| Year | Floor | Bite | All employers | Employers under 50 (range) |
| --- | --- | --- | --- | --- |
| 2030 | $9.50 | 33% | 0.7 | 0.2 (0.1-1.1) |
| 2031 | $11.00 | 37% | 4.5 | 1.4 (0.5-4.3) |
| 2032 | $12.50 | 40% | 11.3 | 3.4 (1.7-8.5) |
| 2033 | $14.00 | 43% | 20.5 | 6.2 (3.5-13.5) |
| 2034 | $15.50 | 46% | 31.9 | 9.6 (6.1-18.9) |
| 2035 | $17.00 | 49% | 45.2 | 13.5 (9.3-24.7) |
| 2040 | $20.19 | 49% | 53.6 | 16.1 (11.0-29.4) |

About **$5 billion over 2030-32** and **$34 billion over 2030-35**; from 2035 about $14-16 billion a year, which is the floor itself, permanent, and not a transition a credit can carry.

**What it shows.** The first three steps are when the floor costs small employers least: about a seventh of the phase-in's cost to them falls in 2030-32, because $9.50 to $12.50 sits below many states' floors. And the credit as first specified paid only for each step's increment, for four quarters, at 50%, 35% and 20%, so the cost of the first step went uncovered in the second and third years. Priced on the need, it comes to about **$0.8 billion**, not the $3 billion section 6 first put on it with judgment step costs: Espen's "too small" is right.

| Option | FY2030-39 (range) | Share of the 2030-32 need | Share of the 2030-35 need |
| --- | --- | --- | --- |
| A. As first specified: 50%, 35%, 20% of each step's increment | $0.8 billion (0.3-2.5) | 16% | 2% |
| **B. Half the whole added cost in each of the three step years (drafted)** | **$2.1 billion (0.8-6.9)** | **42%** | 6% |
| C. All six steps, tapering: 50% in 2030-31, then 40%, 30%, 20%, 10% through 2035 | $6.2 billion (2.9-16.4) | 124% | 18% |

- **B, drafted (provisional until Espen confirms):** inside the decided window, the credit pays half of the floor's whole added cost since 2029 for each eligible worker: the rate in force (or the worker's wage, if lower) less the worker's wage in the last quarter of 2029, times hours paid. One reference wage per worker, kept once, replaces a new calculation at each step, so the paperwork falls as the size rises. The $20,000 cap per employer per year stays and trims the total about 15%.
- **C** follows the need through the whole phase-in, and covers more than the first three years' need in total, but it changes the decided "first three steps" (`-34`), so it is Espen's to choose; it is not drafted.
- **The flat amount per hour** (milestone review L-1) remains an alternative form for B at the same size: a set amount for each hour a worker is paid below the rate in force, with no reference wage at all.
- **What would change this:** state floors rising faster than assumed before 2030 (the need in 2030-32 falls further), or a firm-size count of affected workers (the share at employers under 50 is the largest uncertainty; JCT's score, point 15, would settle the size).

## The question

The federal floor has been $7.25 since July 24, 2009, longer than any earlier gap (Labor Department) [EV-WRK-002] [EV-WRK-003]. In January 2029 it will still be $7.25 under current law, with 20 states at that level unless they act (section 1, part F) [EV-WRK-013]. The question is how high the plan sets the floor, who sets later steps, and what protects the places where it bites hardest.

The legacy design (LAB-4A) is $17, then two-thirds of the national median wage, with longer phase-ins for small firms (five years for large firms, eight for the smallest), a county circuit breaker where the floor would pass about 60% of the local median, and a recession off-ramp, paired with a refundable small-business credit (LAB-5) costed at about $0.10 trillion (range $0.05-0.15 trillion) [EV-WRK-700] [EV-WRK-703]. Those are the legacy author's choices, not Espen's.

## Why it matters

- **Who would get a raise.** Oxfam estimates 39 million workers, 23% of the workforce, earned under $17 an hour in 2024 (Oxfam America, 2024) [EV-WRK-028]. CBO found a $15 floor by 2025 would have raised pay for 17 million workers (CBO, 2019) [EV-WRK-029].
- **What the floor is worth.** EPI puts the federal floor 41% below its 1968 value (Economic Policy Institute, 2025) [EV-WRK-023]. It is 24% of the median full-time wage, against 49% in Canada and Germany and 62% in the United Kingdom and France (OECD, 2025) [EV-WRK-057].
- **For a household.** A full-time worker at $7.25 earns $15,080 a year (CRS) [EV-WRK-022]. At $17 the same hours pay $35,360 (project arithmetic: $17 times 2,080 hours), before the benefits that phase out as pay rises (section 1, A.6) [EV-SEC-537].

## What the evidence says, in five lines

1. **Up to about 60% of the local median, most studies find small job effects** (Dube's review for the U.K. Treasury, 2019; a study of 138 state increases; and one county study, Godøy and Reich's, up to 0.82 of the median, which Dube's review reports as its 81% figure, so they count as one finding) [EV-WRK-050] [EV-WRK-051] [EV-WRK-033] [EV-WRK-063]. Moderate: the state studies are several, the county result is one study, and reviews and recession evidence point the other way (line 2).
2. **The other view is real.** A review counts 79% of estimates as negative (Neumark and Shirley, 2022) [EV-WRK-034]; the 2007-09 federal steps cut low-skilled employment in a recession (Clemens and Wither, 2019) [EV-WRK-064]; CBO's median estimate for $15 was 1.4 million fewer jobs and 0.9 million fewer people in poverty (CBO, 2021) [EV-WRK-032].
3. **Two-thirds of the median has been reached nationally only in the United Kingdom,** through an expert commission, which judged it had no significant effect on jobs but warns of rising risk with higher targets (Low Pay Commission, 2025-26) [EV-WRK-053] [EV-WRK-054] [EV-WRK-055]. No independent causal study of those steps is in the register.
4. **Recessions are when floors cost jobs on the evidence** [EV-WRK-064]; Dube's review recommends a mandate to pause if job losses appear [EV-WRK-052]. No trigger has been evaluated.
5. **No study evaluates county circuit breakers, firm-size phase-ins or a small-business wage credit** (section 2, A.3). Prices rise about 0.36% for a 10% increase, borne equally by poor and rich households (Renkin, Montialoux and Siegenthaler) [EV-WRK-065].

## How far each target reaches

The bite depends on which median is meant, and the legacy file does not say.
- **The all-jobs median** (BLS's survey of employers, which counts part-time jobs) was $24.51 an hour in May 2025 [EV-WRK-078]. Grown at a working assumption of 3.5% a year (range 3-4%; judgment), it is about $34.6 in 2035 (range $32.9-36.3). So **$17 in 2035 is about half of it (47-52%)**, and two-thirds of it would be about $23 (project arithmetic).
- **The median full-time wage** (OECD's measure) is about $30.10 in 2025, since $7.25 is 24.09% of it [EV-WRK-057] (project arithmetic). Two-thirds of it is about $20 today and about $28 in 2035 on the same growth assumption.
- **In low-wage places the local median is well below either,** so a national floor at half the national median sits nearer 60% of the local median there; at two-thirds it would sit far above the studied range. The register has no county measure of reach (Evidence still needed). That gap is the commission's first task under option B. [Measured in the milestone review's fix step 2, on BLS's state and nonmetro medians, May 2023, grown at 3.5%: $17 in 2035 is about 62% of Mississippi's median and 68% of its northwest nonmetro area's [EV-WRK-462] [EV-WRK-463], about 93% of Puerto Rico's and 105% of the Northern Mariana Islands' [EV-WRK-455] [EV-WRK-460] (`tools/territory_bite.py`; the territories are LAB-4.10, `5-delivery.md`, part 5). The "nearer 60%" holds for the low-wage states checked, a little above it; some counties will be lower.]

## Part 1. The level and who sets later steps

**A. The legacy LAB-4A: $17, then two-thirds of the national median.**
- *What it does:* $17 on Raise the Wage's schedule, then steps each year until the floor reaches two-thirds of the national median, and is held there.
- *For a household:* a home health aide or cook in a $7.25 state reaches $17 by 2035 and keeps rising faster than the median until about $23 an hour (on the all-jobs median) or more (on the full-time median), on project arithmetic.
- *Cost:* the federal budget effect rises with the bite; above CBO's $15 pattern by the late 2030s (judgment: +$0.05 to +$0.15 trillion over FY2030-39).
- *Risk:* above 60% of the local median the evidence is the U.K.'s own, and the U.S. has far wider regional wage gaps; the circuit breaker in part 2 is what keeps it within range, and it is untested.

**B. $17 by 2035, then indexed to the median, with a wage commission (recommended).**
- *What it does:* the Raise the Wage Act of 2025's schedule ($9.50 at the start, then $11.00, $12.50, $14.00, $15.50 and $17.00 at one to five years) [EV-WRK-042], with the first step on January 1, 2030; from the next year the floor rises by the growth of the median wage, so its bite holds at about half the median. A standing wage commission (worker, employer and independent members, on the U.K. model) publishes each year the floor's ratio to national, state and county medians and its effects, and may recommend a higher target to Congress; a higher target needs a vote.
- *For a household:* the same aide reaches $17 by 2035 and then keeps pace with typical pay.
- *Cost:* about +$0.03 trillion over FY2030-39 (range zero to +$0.08 trillion) and +$3-8 billion in FY2040 (judgment): CBO's $54 billion for $15 by 2025 [EV-WRK-032], which bit at about 61% of 2025's all-jobs median (project arithmetic on [EV-WRK-078]), lowered for B's smaller bite of about half and its slower phase-in.
- *Why:* it lands inside the range the evidence covers well, nationally, and asks the commission to find where it bites before going further, as Dube's review advises [EV-WRK-052]. One caution on indexing: the one study of it finds larger immediate job effects in states that index to inflation, mostly in the first 14 quarters, though not in its most restrictive specification (Brummund and Strain, 2020) [EV-WRK-077]; it measures indexing to prices, and the register has no study of indexing to the median.

**C. The legacy LAB-4B: $15, then indexed.** The bipartisan Hawley-Welch bill sets $15 from the January after enactment, then adjusts it each year [EV-WRK-040].
- *What it buys:* a smaller first step with Republican sponsors; a $15 floor in 2030 is about 51% of the projected 2030 median (project arithmetic: $24.51 grown 3.5% a year for five years is about $29.1).
- *What it costs:* a lower floor for the next decade; as described here through Hawley-Welch's bill, indexed to prices rather than the median, its bite falls as real wages grow. The legacy LAB-4B indexes to the median, which has no such drawback (record correction, status line above).

**D. The legacy LAB-4C: the commission alone, to two-thirds over ten years, with no dollar step.**
- *What it buys:* the U.K.'s institution, with steps set each year on evidence [EV-WRK-053].
- *What it costs:* no legible number for workers, and no guarantee the commission moves; a later administration appoints it.

## Part 2. Protection where the floor bites hardest

**A. The legacy set:** phase-ins by firm size (five to eight years), a county circuit breaker at about 60% of the local median with a hard sunset, a recession off-ramp, and the refundable small-business credit, about $0.10 trillion (range $0.05-0.15 trillion) [EV-WRK-700] [EV-WRK-703].
- *Burden:* employers must know their size tier and their county's schedule; a worker's floor depends on where and for whom they work; the credit needs an application and a payroll-tax computation. None of it is evaluated (section 2, A.3).

**B. One national schedule with a recession pause in statute, no credit (recommended).**
- *What it does:* every covered employer follows the same steps. If the national unemployment rate's three-month average rises half a point above its low of the previous year (the trigger shape in the 2025 unemployment insurance bill) [EV-WRK-395], the next step waits a year; the floor never falls.
- *Why:* the five-year schedule is itself the phase-in, and the floor stays near half the median; the pause answers the one finding of recession job loss [EV-WRK-064]. Simple for employers and for the Wage and Hour Division to enforce (`DEC-2026-11-09-13`).
- *Cost:* zero; it drops the booked LAB-5 credit (budget model row LAB-5).

**C. B plus a small, time-limited credit** for employers under 50 workers during the first three steps, paid through the payroll-tax return.
- *Cost:* about $0.02-0.04 trillion (judgment, a third of the legacy credit's range).
- *What it buys:* the legacy pairing (a visible cushion for small employers) at lower cost; the version to offer if votes need it.

**D. B plus one more year for employers under 25 workers,** without a credit. Simpler than A, but it gives small-firm workers a lower floor for a year and asks employers to certify their size.

## Against the bills

| Bill | Level and indexing | Subminimums | Protections | Against the recommendation |
| --- | --- | --- | --- | --- |
| **Raise the Wage Act of 2025**, H.R. 2743 / S. 1332 [EV-WRK-042] [EV-WRK-043] [EV-WRK-044] [EV-WRK-045] | $9.50 to $17 over five years, then indexed from year six | Tipped, youth and 14(c) phased out | None beyond the schedule | **Match** on the schedule and indexing; B adds the commission and the pause |
| **Higher Wages for American Workers Act**, S. 2013 (Hawley, Welch) [EV-WRK-040] [EV-WRK-041] | $15 from the next January, then adjusted yearly | — | — | **Diverge** on level; option C |
| **Raise the Wage Act of 2021** (CBO score) [EV-WRK-032] | $15 by 2025 | Phased out | — | The score B is benchmarked against |
| **Legacy LAB-4A and LAB-5** [EV-WRK-700] [EV-WRK-703] | $17, then two-thirds of the median | Phased out | Size tiers, circuit breaker, off-ramp, credit | **Match** on $17; **diverge** on the target and part 2 |
| **U.K. National Living Wage** [EV-WRK-053] | Two-thirds of the median, set yearly on a commission's advice | Lower youth rates | Commission's judgment | **Match** on the commission; **diverge** on the target |

No CBO or JCT score of the 2025 bills was found; CBO's 2019 and 2021 scores are the nearest (section 2, "Evidence still needed").

## Consequences at a glance

| | A (legacy) | **B** | C | D |
| --- | --- | --- | --- | --- |
| Floor in 2035 | $17 and rising to two-thirds of the median | $17, then with the median | $15 indexed (about $17-18 in 2035) | Set by the commission |
| Bite, all-jobs median | Rising to about 67% | About 50% | About 50% and falling | Up to 67% over ten years |
| Inside the well-studied range nationally | Not by the late 2030s | Yes | Yes | Not by the end |
| Federal cost FY2030-39 | +$0.05-0.15 trillion, plus the $0.10 trillion credit | About +$0.03 trillion | Smaller | Like A |
| Burden on employers | Size tier, county schedule, credit claim | One schedule | One schedule | One schedule, changing yearly |

## Recommendation: part 1 B, part 2 B

- **B puts $17 in law on a schedule people can read,** keeps it from eroding, and stays where most of the evidence says job effects are small.
- **The commission is how to go further on evidence,** not by a target set in advance. The two-thirds goal stays available: the commission can recommend it, county by county evidence in hand.
- **One schedule with a pause** is simpler than tiers and breakers that no study tests, and it drops a $0.10 trillion credit with no evaluation behind it.
- **What it costs in burden:** an employer follows one published schedule; the commission's reports use data agencies already hold.

**What would change this:** a county-level measure showing the half-median floor above about 60% of the local median in many places (add a phase-in for those counties); evidence that the U.K.'s two-thirds steps caused no job loss in its low-wage regions (raise the target); a recession during the phase-in (the pause handles it).

## If you decide

- **Under B and B:** section 4 writes the schedule, the indexing formula (the median from BLS's survey, published each autumn for January), the commission's membership and annual report, and the pause trigger; the budget model's LAB-5 row is proposed for removal at booking; the household model is asked to measure how much of the raise families keep after phase-outs (section 1, "Evidence still needed").
- **Vehicle:** the wage floor is a rule, so it rides the regular-order labor bill (point 16 in `../3-design.md`); the 2021 parliamentarian ruling barred a wage mandate from reconciliation (`legacy/domains/domain-labor.md`, LAB-4).
- **Preparation before 2029:** ask CBO to score B on its 2029 baseline (point 15).
