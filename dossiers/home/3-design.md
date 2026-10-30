# A home you can keep: design choices

Role: section 3 of the housing dossier: the real forks in the design, the options at each, what the evidence says for and against them, how they connect, and a recommendation. Status: draft (stage C, step 4), rebaselined on the ROAD to Housing Act (Public Law 119-101, July 11, 2026), which is current law and the starting point for every fork (`road-act.md`), and refreshed under `DEC-2026-10-30-02`: the legacy rental-help and construction-capital designs (HOU-4A, HOU-4D, HOU-3C) are starting points weighed as options, not fixed inputs. The plan these choices serve begins in January 2029 (`DEC-2026-10-29-01`): the baseline is current law as it will stand in 2029, and recommendations are dated from 2029 on. Every figure and factual claim cites the evidence register (`evidence.json`). Recommendations are the dossier's advice, not decisions: no agenda status or level changes until Espen decides, through a later charter PR. Costs are not modeled here; section 6 prices the choices with the budget model. Where this section gives an order of magnitude, it says so and shows the arithmetic.

Outcomes the choices serve:
- OUT-04, a home people can keep;
- OUT-02, planning beyond the next paycheck;
- OUT-01, child poverty.

## How to read this section

- **Eight forks.** Section 2 left seven forks and carried section 1's question of who is reached first as the eighth (`2-what-works.md`, last list). Each fork below has four parts: options, evidence, interactions and a recommendation.
- **Seven decision memos.** Seven forks are Espen's to decide. Each has a short memo in `memos/`, one file per fork, that Espen can decide from without reading the rest. The memos are separate files so each can be read, discussed and decided on its own; approval is per decision, never as a package (`charter/STANDARDS.md`). Each memo says what Espen has already chosen and what its recommendation would change.
- **Recommended without a memo: Espen decides each.** Fork 7 and eight narrower points are recommendations without a full memo, listed under "Recommended without a memo" with a yes-or-no question each. They are not decided by silence: section 4 drafts none of them until Espen agrees, item by item.
- **Evidence rules.** Recommendations rest on data or on analysis an independent publisher corroborates. Where the evidence for part of a recommendation is not yet in the register, the section and the memo say so and name what the recommendation rests on instead (Espen's October 26 direction, or this dossier's judgment). Where independent sources disagree, both views are given. Analysis without independent corroboration (EV-HOU-052, 087, 137, 141 and 158) is mentioned only as one source's view.
- **Executive-branch sources** carry the administration that produced them, in the register's context note and, on reader-facing pages, in the prose (`DEC-2026-10-30-01`). Analysis from the second Trump administration (2025 on) is presented as that administration's view and never carries a recommendation on its own.
- **Time frame.** Recommendations are for a plan that starts in January 2029. Earlier dates are labeled as preparation or as current law that takes effect before then.

## Starting points (chosen, open to revision)

Espen ruled on October 30 that the legacy decisions on the form and funding level of rental help and construction capital are working choices, not settled (`DEC-2026-10-30-02`). Keeping each of them is a fine outcome, but this section weighs keeping them as one option among others, on the evidence, rather than assuming it. Each fork that touches them lists "keep the legacy design" as an explicit option and says what each alternative would change about how the package fits together.

| Item | Legacy design (the starting point) | Weighed in | Where it comes from |
| --- | --- | --- | --- |
| HOU-4A | One million new voucher awards, mandatory funding, phased in over 2030-33 (250,000 a year), aimed at extremely low-income renters. Status `chosen` (it was `decided` until `DEC-2026-10-30-02`) | Fork 1 (form: tenant vouchers or attached awards), fork 2 (scale and funding: a fixed count or part of a guarantee), fork 8 (pace and order) | `legacy/domains/domain-housing.md`, HOU-4; legacy governing decisions, "Family package adopted, October 24" |
| HOU-4D | A bounded $135 billion expansion of rental help over FY2030-39 beyond HOU-4A. Its award count, cohort and delivery were never chosen; "approximately another million awards" was a scale illustration. It is not HOU-4C's broad entitlement. Status `chosen` | Fork 2 (what the money buys: an unnamed cohort or a defined stage of the guarantee), fork 1 (form), fork 8 (which group) | `legacy/domains/domain-housing.md`, HOU-4, "October 26 approved extension"; a row in `agenda/agenda.csv` at L1, status `chosen`, added by PR #73: its cohort, award count and phase-in are not chosen |
| HOU-3C | Construction capital in two channels: about $72 billion of grants to state revolving funds (ramped $3 billion, $5 billion, then $8 billion a year; at least 30% forgivable for extremely low-income units) and $300 billion of federal direct loans through state agencies. Chosen by Espen in the legacy domain file, unlike items carried over without an individual ruling; status `chosen` | Fork 3, part 3 (channels, amounts, eligible uses, and the balance between grants and loans and between building and rental help) | `legacy/domains/domain-housing.md`, HOU-3 |

Other `chosen` items, such as HOU-1A, HOU-2A and HOU-6's fund and conditions, are starting points in the same sense; a recommendation that would change one says so plainly, in this section and in its memo. The federal builder of last resort (HOU-9A, 9B or 9C) is an open call already on Espen's list in the legacy governing decisions. Fork 3 takes it up.

**Given.** These are not reopened here; each fork works inside them.

| Item | What is given | Where |
| --- | --- | --- |
| Housing-security direction (October 26) | A direction, not a form or a funding level. Develop a guarantee for extremely low-income renters that "should replace waiting-list luck for its defined population", alongside public and nonprofit acquisition, repair and construction, lasting affordability, and a lawful federal sponsor or backstop where state participation fails. Eligibility, supply, federal and state roles and funding are to be resolved; HOU-4A's benefits are preserved | `legacy/domains/domain-housing.md`, "Accepted housing-security development direction, October 26"; legacy governing decisions, PR #20 acceptance |
| D3 and D4 (OUT-11) | Every income group below the top better off on net, with new general-fund revenue mostly from the top 1% and corporations (D3). Permanent programs paid for at maturity, from FY2040; time-limited investments may borrow inside an envelope (D4-B) | Legacy governing decisions; `charter/outcomes.md`, OUT-11 |

The legacy vehicle decision, D5 (housing money rides the FY2030 reconciliation bill, R2), is a cross-cutting choice that `DEC-2026-10-30-02` does not address. This section keeps it as the working vehicle and does not weigh it.

## The baseline in 2029

The plan's first budget is FY2030, enacted in 2029. This is current law as it will stand then, counting enacted laws with later effective dates and scheduled expirations (`road-act.md` has the full map).
- **The ROAD to Housing Act** (Public Law 119-101, law since July 11, 2026) [EV-HOU-200]. It appropriates nothing [EV-HOU-201] [EV-HOU-202]. By 2029:
  - the large-investor purchase limit is in force, from January 7, 2027 until its repeal on January 7, 2042 [EV-HOU-222];
  - Build Now's CDBG reallocation by housing growth starts in FY2029 and runs through FY2043 [EV-HOU-208];
  - the Innovation Fund is authorized at $200 million a year for FY2027-2031 and ends in July 2033, but has money only if Congress appropriates it [EV-HOU-202] [EV-HOU-206];
  - the Rental Assistance Demonstration is permanent, with a 555,000-unit cap [EV-HOU-231], and faster voucher inspections and pre-inspection for new landlords are law [EV-HOU-232];
  - the Emergency Solutions Grants shelter waiver runs for FY2027-2030 [EV-HOU-237], and the disaster recovery block grant ends in July 2029 [EV-HOU-228];
  - GAO's workforce-housing study (July 2027) [EV-HOU-242] and the Interagency Council on Homelessness's new national plan (July 2027) [EV-HOU-238] are due before the plan starts.
- **Tax credits.** The One Big Beautiful Bill Act's permanent 12% increase in Low-Income Housing Tax Credit allocations and its lower bond-financing test apply from 2026 [EV-HOU-113].
- **Homelessness policy.** The July 2025 executive order against Housing First [EV-HOU-107] stays in force unless revoked; a president taking office in January 2029 can revoke it.
- **Rental help.** The voucher program served more than 2.3 million households [EV-HOU-013]; its 2029 size depends on appropriations not yet made. No law enacted so far adds voucher awards.

Each fork builds on this baseline rather than duplicating it.

## The forks at a glance

| Fork | Agenda items | Handled by | Recommendation in one line |
| --- | --- | --- | --- |
| 1. Help or homes | HOU-4A, HOU-4D with HOU-2, 3, 5, 6, 8 | Memo 1 | Match the tool to the market for all new awards, HOU-4A's later cohorts included: vouchers where homes are available, help tied to new and acquired homes where they are not. Changes HOU-4A's form for part of its 2032-33 cohorts; keeps its count, pace and funding |
| 2. How broad the guarantee is | HOU-4A, HOU-4D, HOU-4C | Memo 2 | Turn the legacy money into the first two stages of a guarantee: HOU-4A as filed for people without a home and the first families, then HOU-4D's $135 billion for the rest of the extremely low-income families with children with severe needs, instead of an unnamed second million awards. Keeps both amounts and mandatory funding |
| 3. Production tool | HOU-2, HOU-3, HOU-5, HOU-8, HOU-9 | Memo 3 (three parts) | Part 1: narrow the tax credits and make federally financed homes permanently affordable. Part 2: authorize a small federal backstop builder from 2029 (a limited HOU-9A). Part 3: keep HOU-3C's two channels and amounts, and open both to acquiring and preserving existing buildings |
| 4. Zoning conditions | HOU-6 | Memo 4 | Pay for results through ROAD's Innovation Fund, funded at scale and opened to states, rather than a separate fund; leave ROAD's Build Now as the only CDBG test; count lower-cost homes |
| 5. Homelessness approach | HOU-4, HOU-1, HOU-8 | Memo 5 | Housing First as the default, with a recovery-housing option people can choose, never a condition |
| 6. Prevention and emergency aid | HOU-1 | Memo 6 | A standing emergency-rent fund with tested delivery rules, plus a smaller one-time start |
| 7. Immigration and construction labor | HOU-3, HOU-6, HOU-9; OUT-07 | Recommended without a memo (yes or no) | Treat the construction workforce as a shared dependency; ask the immigration dossier to weigh it |
| 8. Who is reached first | HOU-4A, HOU-4D | Memo 8 | People without a home first, then extremely low-income families with children, then other extremely low-income renters with the most severe needs. Keeps HOU-4A's 250,000-a-year pace |

## What the ROAD to Housing Act changes

The first draft of this section did not account for the ROAD to Housing Act. It is now law, so each fork and each smaller choice was re-checked against it (`road-act.md` maps the provisions). Three verdicts are possible: no change; wording and baseline change only; or the options or recommendation change.

**In short: the Act changes the options and the recommendation at fork 4 (zoning, HOU-6), and its own reporting changes the recommendation on the investor limit (HOU-7, smaller choice 8). Every other recommendation stands, apart from one small change at fork 3.** Fork 3, the production toolkit, might have been expected to move more; it does not, because the Act adds no construction money and leaves the tax credits alone [EV-HOU-201] [EV-HOU-202].

| Fork or choice | Verdict | What changes |
| --- | --- | --- |
| 1. Help or homes | Wording and baseline only | Faster voucher inspections, including pre-inspection for landlords new to the program [EV-HOU-232], ease one cause of slow lease-up, not landlord refusal or scarcity. The Act's Build Now test already sorts places by whether rental vacancy is above the national rate [EV-HOU-208]; section 4 can reuse it as fork 1's tight-market trigger |
| 2. How broad | No change | The Act adds no rental assistance. Its one income-rule change widens HUD-VASH eligibility for disabled veterans [EV-HOU-233] |
| 3. Production toolkit | Wording and baseline, plus one small recommendation change | No new construction money and no tax-credit change. It opens existing channels: CDBG may build [EV-HOU-215], HOME is reauthorized with no amount [EV-HOU-226], banks may hold more tax-credit equity [EV-HOU-241], reviews are lighter [EV-HOU-217] [EV-HOU-218], and the Rental Assistance Demonstration becomes permanent [EV-HOU-231]. Part 1's "drop or defer" for the middle-income credit becomes "defer until GAO's workforce-housing study, due July 2027" [EV-HOU-242]; waiting for that study is this dossier's judgment. Part 2 is unchanged |
| 4. Zoning conditions | **Options and recommendation change** | The Act already has a supply-growth reward fund (the Innovation Fund) and a CDBG reallocation by housing growth (Build Now) [EV-HOU-206] [EV-HOU-208]. HOU-6 as chosen would duplicate both. New options; the recommendation now builds on these two tools instead of creating a separate fund and a second CDBG condition. See fork 4 |
| 5. Homelessness | Wording and baseline only | Housing First and the 2025 order are untouched. A new federal plan to end homelessness is due July 2027 [EV-HOU-238], and Emergency Solutions Grants recipients may shift more money to shelter and outreach for FY2027-2030, but not if they remove people without offering shelter or housing [EV-HOU-237] |
| 6. Prevention | No change | The Act creates no emergency rent aid. Its disaster recovery block grant ends July 2029 [EV-HOU-228] |
| 7. Immigration and labor | Wording only | Factory-built housing gets easier: no permanent chassis, modular financing, higher FHA Title I limits [EV-HOU-219] [EV-HOU-245] [EV-HOU-220]. Section 7's workforce scenario should count it as a partial hedge |
| 8. Who first | No change | Disabled veterans in HUD-VASH are easier to qualify [EV-HOU-233]; nothing on priorities |
| Smaller choices 1, 4, 5, 7 | No change | Nothing in the Act on payment limits, right to counsel, emergency aid rules or residency rules |
| Smaller choice 2 (source of income) | No change | Refusing vouchers is still legal under federal law, except in some federally assisted properties [EV-HOU-246]; the Act adds no protection. 23 states and the District of Columbia, and 152 cities and counties, have their own laws [EV-HOU-247]. Pre-inspection for new landlords [EV-HOU-232] complements a protection |
| Smaller choice 3 (search help) | Wording only | Housing agencies must now give new voucher holders a list of pre-inspected units [EV-HOU-232]; search help builds on it. Nothing else in the Act on mobility or search help; its Moving to Work cohort may not waive portability [EV-HOU-234] |
| Smaller choice 6 (public housing redevelopment) | Wording and baseline only | The Rental Assistance Demonstration is permanent, its cap on total conversions rises from 455,000 to 555,000 units, and HUD must report yearly on residents who stay or return [EV-HOU-231]. The right to return should cover these conversions and use that reporting |
| Smaller choice 8 (investor limit, HOU-7) | **Recommendation changes** | HOU-7 as chosen already meant removing the Act's 2042 sunset and adding reporting. The new fact is that the Act's own reporting and studies are law and do not lapse with the ban [EV-HOU-222] [EV-HOU-224], so HOU-7's added reporting is redundant. On that and on the mixed evidence, this dossier now recommends HOU-7B instead of the chosen HOU-7: leave the ban as enacted and decide after the 2037 reports. That reverses the earlier "no change" recommendation and would change Espen's choice |

## Fork 1. Help or homes

**The question.** The October 26 direction pairs rental help with building, and the legacy designs give each a form: HOU-4A's million awards and HOU-4D's envelope as tenant-based vouchers, HOU-3C's capital as state grants and federal loans. With HOU-4A and HOU-4D open (`DEC-2026-10-30-02`), the question covers all new awards: should new rental help work the same way in every market, or change where homes are scarce?

**Options.**
- **1A. Keep the legacy design: vouchers everywhere.** Every new award under HOU-4A and HOU-4D is a tenant-based voucher in every market. Building money goes out by the HOU-3 formula (renter cost burden and construction costs). *How the package fits:* help and building run side by side but are not linked; HOU-3C's homes reach extremely low-income renters only where a voucher holder happens to rent one, or through the 30% forgivable share.
- **1B. Match the tool to the market, for all new awards.** Where vacancies are low, part of the new awards, HOU-4A's later cohorts included, is attached to homes built or bought with HOU-3, HOU-5B and HOU-8 money (project-based awards), so each award comes with a home. HOU-3 and HOU-6 money is weighted toward those markets. Where homes are available, awards stay tenant-based. Tenants in attached homes can later move with a tenant-based voucher. HOU-4A's count, 2030-33 schedule and mandatory funding stay; in practice its 2030-31 cohorts stay tenant-based, because HOU-3C's first new homes will not be finished until about 2032 (its loans ramp from $10 billion in 2030; `legacy/domains/domain-housing.md`, HOU-3, and this dossier's judgment on build times). Existing buildings bought under fork 3, part 3's recommendation could host attached awards sooner. *How the package fits:* the award is the steady rent that lets a loan-financed home serve the poorest renters, so HOU-3C's loan channel and the rental help work as one tool in tight markets.
- **1B-narrow. Match the tool to the market, beyond HOU-4A only.** As 1B, but HOU-4A's million awards stay tenant-based everywhere; only HOU-4D and later stages of the guarantee can be attached. This was the first draft's recommendation, written when HOU-4A was treated as settled. *How the package fits:* as 1B from about 2034, but HOU-3C homes finished in 2032-33 in tight markets have no new awards to attach.
- **1C. Build first.** In tight markets, slow the growth of awards until units exist, and move part of the HOU-4D envelope into building. *How the package fits:* it shifts the balance from help to building; see fork 3, part 3, for what that money would buy.

**Evidence.**
- *For vouchers as the core.* Long-term subsidies sharply reduce homelessness among families who get them [EV-HOU-086] [EV-HOU-184]. Studies typically find tenant subsidies more cost-effective than production subsidies [EV-HOU-112] [EV-HOU-114], and tenant-based vouchers seem better than project-based programs at reaching people who would otherwise lack their own housing [EV-HOU-114]. A voucher expansion did not raise rents across the market [EV-HOU-096]. Moves to lower-poverty areas before age 13 raised children's adult earnings 31% [EV-HOU-090]: tenant choice matters for children.
- *Against vouchers alone in tight markets.* Only 61% of new voucher holders leased a home within six months, and fewer where vacancies are low [EV-HOU-092]. Landlords refused voucher holders 67% to 78% of the time in three metros without source-of-income laws [EV-HOU-093]. Raising payment limits across a whole metro mainly raised landlords' rents [EV-HOU-095], and the voucher expansion did raise rents for units near the limit in supply-constrained cities [EV-HOU-096]. For every 100 extremely low-income renter households there were only 38 affordable and available homes [EV-HOU-024].
- *For pairing help with homes.* More than 40% of Low-Income Housing Tax Credit tenants had extremely low incomes, and most of them also had rental help [EV-HOU-118]: building reaches the poorest when help is attached. New buildings can lower nearby rents [EV-HOU-132] [EV-HOU-133], though one Minneapolis study found higher rents for nearby lower-priced units [EV-HOU-135]; both views stand. In supply-constrained metros homes filter up to richer occupants rather than down [EV-HOU-179], so market-rate building alone reaches the poorest slowly there.
- *Against building first.* Building takes years. Holding back awards leaves families waiting who could lease now. National rental vacancy reached 7.4% in February 2026, the highest in its series [EV-HOU-068]; many markets are not tight.

**Interactions.**
- Fork 2: a broader guarantee makes market sorting more important, because more households search at once.
- Fork 3: project-based awards give HOU-3 and HOU-8 projects the steady rent they need to serve the poorest.
- Fork 4: zoning reform decides how fast supply can respond in tight markets.
- Fork 8: people leaving homelessness often need a home ready to move into; attached homes help them most.
- Fork 3, part 3: under 1A, homes for extremely low-income renters must be paid for mostly by grants, because their rents cannot carry debt; under 1B, attached awards carry the rent, and the loan-heavy HOU-3C fits.
- D4: 1C moves permanent spending (rental help) into time-limited capital. That changes how it is financed, but delays help. 1A, 1B and 1B-narrow cost about the same; they place the money differently.

**Keeping the legacy design (1A), weighed.** 1A has the strongest direct evidence: the trials that show rental help works used mostly tenant-based vouchers [EV-HOU-086], and one study finds tenant-based vouchers better than project-based programs at reaching people who would otherwise have no home of their own, mostly people doubled up with others [EV-HOU-114]. Its weakness is also measured: in tight markets many awards go unused [EV-HOU-092] and landlords refuse them [EV-HOU-093]. 1A is the right design where homes are available, and with national rental vacancy at a series high in early 2026 [EV-HOU-068], many markets are not tight; it is weakest where homes are scarce.

**HOU-4A under 1B, weighed.** Applying 1B to HOU-4A changes only part of its 2032-33 cohorts, in tight markets, because attached homes do not exist earlier. The case for including them is that a family in a tight market faces the same failed search whether its award is in the first million or the second [EV-HOU-092]; fencing off the first million leaves HOU-3C's first finished homes without awards to attach. The case against is that it adds an untested form to the one award group with the best evidence behind its plain-voucher form.

**Evidence gap.** The register does not yet hold evidence on how project-based awards lease up or affect rents (see "Evidence still needed"). The case for 1B rests on the evidence that tenant-based vouchers fail in tight markets, not on direct evidence that attached awards do better there, and one study finds tenant-based vouchers better at reaching people who would otherwise have no home of their own [EV-HOU-114].

**Current law (ROAD to Housing Act).** No change to the options.
- Inspections under the tax credit, HOME or rural programs now count for vouchers, and housing agencies may pre-inspect units of landlords new to the program and must list them for new voucher holders [EV-HOU-232]. That removes one cause of slow lease-up; landlord refusal and scarcity remain.
- The Rental Assistance Demonstration, now permanent with its cap on total conversions raised from 455,000 to 555,000 units, keeps converting public housing to project-based assistance [EV-HOU-231]: attached help already exists at scale in that stock.
- The Act's Build Now test exempts places whose rental vacancy is above the national rate [EV-HOU-208]. Section 4 can use the same Census measure as 1B's tight-market trigger, so the two federal tests agree.

**Recommendation: 1B, for all new awards.** This changes the form of HOU-4A, which is `chosen`, for a share of its 2032-33 cohorts in tight markets; its count, schedule and mandatory funding stay. The evidence supports vouchers as the core and shows where they fail: tight markets with landlords who refuse them. 1B keeps tenant choice where it works and adds homes where it does not, and it lets HOU-3C's first homes serve the poorest renters as soon as they open. Keep the attached share small and tested until project-based lease-up evidence is in, because one study finds tenant-based vouchers better at reaching people who would otherwise have no home of their own [EV-HOU-114]. 1B-narrow is the cautious fallback if Espen prefers to leave HOU-4A's form exactly as filed; it differs from 1B only in 2032-33. The share of attached awards, the vacancy trigger and the right to move are set in section 4. Memo: `memos/1-help-or-homes.md`.

## Fork 2. How broad the guarantee is

**The question.** The October 26 direction asks for a guarantee that replaces waiting-list luck for a defined group. With HOU-4A and HOU-4D open (`DEC-2026-10-30-02`), the question also covers their scale and funding: should new help be a fixed number of awards, or a guarantee for named groups? How large should the group be, how fast should it be reached, and how should it be funded?

**Options.**
- **2A. Keep the legacy design: bounded help, no guarantee.** HOU-4A's million awards plus the HOU-4D envelope, with waiting lists kept for everyone else. HOU-4D's $135 billion buys roughly another 800,000 awards on HOU-4A's schedule (arithmetic below), for a cohort never named. *How the package fits:* help is a fixed count; who gets it is decided by local waiting lists, so the order in fork 8 decides who is ever helped, not who is helped first.
- **2B. A staged guarantee within the legacy money.** The same two amounts, re-formed as the first two stages of a guarantee for extremely low-income renters (at or below 30% of area median income). Stage 1 is HOU-4A as filed: one million awards over 2030-33, reaching people without a home first and then the first families with children (fork 8). Stage 2 is HOU-4D: a guarantee for extremely low-income families with children with severe problems, instead of an unnamed second million awards. Enrollment opens in 2034 and takes up to 300,000 families a year, in an order rule set in section 4 (for example, the most severe problems and the youngest children first); from 2037 every family in the group that qualifies can get help. Later groups follow only as section 6 finds the money under D4. That narrows the earlier draft's 2B, which phased in every extremely low-income group: older and disabled renters living alone (fork 8's third group) have no funded route in the 2030s under this option. *How the package fits:* the award count becomes an outcome of who qualifies rather than a cap; for the groups reached, help is a right rather than a lottery; cost follows take-up, so the $135 billion becomes an estimate to be checked rather than a ceiling.
- **2C. A guarantee for all extremely low-income renters by 2039.** As 2B, but every group of extremely low-income renters is phased in within the decade, not only the first two. *How the package fits:* the guarantee is the plan's largest permanent claim, reaching three to four times as many households as the legacy items (arithmetic below), and needs new permanent revenue before FY2040.
- **2D. A guarantee for all very low-income renters (HOU-4C).** Every renter household at or below 50% of area median income can get help.

**Funding, under every option.** Keep the legacy choice of mandatory funding, not annual appropriations (HOU-4B was the appropriated version, not chosen). The tenant-based account is appropriated each year and 87% of it already goes to renew existing vouchers [EV-HOU-187]; new awards funded the same way would compete with renewals. Congress has funded new vouchers as mandatory spending before: $5 billion for 70,000 Emergency Housing Vouchers [EV-HOU-188]. A guarantee needs mandatory funding by definition: an appropriation can run out mid-year. That last point is judgment.

**Pace, under every option.** Keep HOU-4A's 250,000 awards a year. Even today, only 61% of new voucher holders lease a home within six months [EV-HOU-092]; a faster start would add awards faster than housing agencies and landlords can place them. That is judgment from the lease-up evidence, not a measured capacity limit.

**The size of each group.**
- There were 12.0 million extremely low-income renter households in 2023. 4.3 million had rental assistance, and only 1.9 million avoided severe housing problems without it [EV-HOU-185]. 5.8 million were unassisted with severe problems [EV-HOU-186].
- There were 19.14 million very low-income renter households [EV-HOU-020], 13.77 million of them unassisted [EV-HOU-023].
- Extremely low-income families with children with severe problems: 1.717 million households [EV-HOU-186].
- Today's voucher program serves more than 2.3 million households [EV-HOU-013]. Its account received $30.25 billion in FY2023 [EV-HOU-187].

**Rough order of magnitude (this dossier's arithmetic, not a score).** Two per-household bases:
- *The project's adopted planning input:* $15,200 per voucher-year in FY2026, growing 3% a year, with a housing-agency administration allowance on top (`legacy/domains/domain-housing.md`, HOU-4A). This is the basis the memos use.
- *A check from the evidence:* $30.25 billion for about 2.3 million households in FY2023 is roughly $13,000 [EV-HOU-187] [EV-HOU-013]. The gap is mostly rent growth since 2023.

*What the legacy money buys.* At $15,200 growing 3% a year, a voucher-year costs about $17,100 in FY2030, $19,300 in FY2034 and $22,300 in FY2039, an average of about $19,600 over FY2030-39. Before administration and any deeper subsidy for the poorest renters (per-voucher costs follow the gap between tenant incomes and market rents [EV-HOU-187]):
- HOU-4A: 250,000, 500,000 and 750,000 awards in 2030-32, then one million a year for 2033-39, is 8.5 million award-years, about $170 billion if every award were leased all year. The legacy working midpoint is $150 billion, which allows for lease-up, or $162.2 billion with the rounded $12.2 billion housing-agency administration allowance (`legacy/domains/domain-housing.md`, HOU-4 and the PR #22 fee correction). At maturity it is about $22 billion a year in FY2039.
- HOU-4D: $135 billion at about $19,600 is about 6.9 million award-years. On HOU-4A's schedule that is about 800,000 more awards ($135 billion against $170 billion for a million); started later, more.
- 2B's stage 2: the extremely low-income families with children with severe problems number 1.717 million households [EV-HOU-186]. If HOU-4A's million reaches people without a home and about half a million of these families first, about 1.2 million remain. Phasing them in at up to 300,000 a year over 2034-37 is 5.4 million award-years through FY2039, about $114 billion at full take-up before administration, or about $123 billion with HOU-4D's 8.1% administration allowance, still inside HOU-4D's $135 billion; at maturity it is about $27 billion a year in FY2039. The intake limit is what keeps it inside: a right for all 1.2 million from 2034 would be 7.2 million award-years, about $149 billion through FY2039, above the envelope. How many of HOU-4A's million go to families depends on how many households are homeless, a number the register does not yet hold (the point-in-time count is people, not households [EV-HOU-014]), so the split is this dossier's assumption.

*The full guarantees*, at FY2030 costs (about $17,100):
- 2C: about $99 billion a year if all 5.8 million unassisted extremely low-income households with severe problems took help, and about $132 billion if all 7.7 million unassisted ones did (12.0 million less 4.3 million) [EV-HOU-185] [EV-HOU-186]. That is three to four times as many households as the two legacy items reach at maturity, about 2 million. HOU-4A and HOU-4D count toward it.
- 2D: about $236 billion a year at full take-up of 13.77 million households [EV-HOU-023].

Take-up, rents and lease-up will move these numbers a great deal; section 6 prices them.

**Evidence.**
- *For a guarantee.* Waiting lists ration help: only about one in four eligible households is served [EV-HOU-011] [EV-HOU-012], and in 2023 only 28% of very low-income renters had assistance [EV-HOU-022]. Abroad, entitlement allowances reach over half of bottom-fifth households in six European countries [EV-HOU-160]; U.S. spending on them is 0.1-0.3% of GDP against 1.4% in the UK [EV-HOU-159].
- *For starting with the lowest incomes.* Extremely low-income renters had worst case needs at 48.3% and made up 68.6% of all worst case needs [EV-HOU-185]. Their problem is mostly income: rents for the poorest renters rose no faster than for the richest [EV-HOU-070], and after 2007 renters' incomes fell while rents rebounded [EV-HOU-071].
- *The risk in breadth: landlords capture part of the money where supply cannot respond.* When France extended benefits to all low-income households, 78 cents of each euro went into higher rents [EV-HOU-156], and subsidies raised rents even for unsubsidized tenants [EV-HOU-157]. When the UK cut Housing Benefit, 60% to two-thirds of the cut fell on landlords [EV-HOU-155]. A Finnish study found little pass-through where allowances follow set unit limits [EV-HOU-158]; that is one study without independent support, so both views stand. In the U.S., a voucher expansion did not raise rents overall [EV-HOU-096], but metro-wide payment increases mostly went to landlords [EV-HOU-095]. The broader the guarantee, the more households search at once in the same markets.
- *Delivery.* Lease-up is incomplete even now [EV-HOU-092]. An award is not a home.

**Interactions.**
- D4: every option is permanent spending, paid for from FY2040. The project's long-term model already shows the FY2040 test failing, by about $71.9 billion, after the October 24 adoption of the family credit and HOU-4A (legacy governing decisions, D4, "What the current long-term model shows"). 2B costs about what 2A does through FY2039, but its stage 2 is a right, so its cost can rise with take-up and rents where 2A's cannot; section 6 must test it. 2C and 2D widen the gap and need new permanent revenue.
- D3: help at these incomes lands almost entirely in the bottom two income fifths (`legacy/domains/domain-housing.md`, D3), so it supports D3's first test. The revenue that pays for it must meet D3's second: mostly from the top 1% and corporations.
- Fork 1 and fork 4: breadth without supply raises rents in tight markets.
- Fork 8 sets the order; fork 6 catches households not yet reached.
- OUT-01: about 3.3 million children lived in unassisted extremely low-income households with severe problems [EV-HOU-186].

**Current law (ROAD to Housing Act).** No change. The Act adds no rental assistance and no voucher awards [EV-HOU-201] [EV-HOU-202]. Its one change to the income rules widens HUD-VASH eligibility for veterans with VA disability benefits [EV-HOU-233].

**Keeping the legacy design (2A), weighed.** 2A's amounts and funding are sound: the arithmetic above shows they are about what the first two stages of a guarantee cost, and mandatory funding is what a lasting program needs [EV-HOU-187] [EV-HOU-188]. What 2A lacks is a defined group. Its second million awards have no named cohort, so they would go through the same waiting lists that ration help today, to about one in four eligible households [EV-HOU-011] [EV-HOU-012]. That is the "waiting-list luck" the October 26 direction asks to replace.

**Recommendation: 2B.** Keep HOU-4A as filed, as stage 1, and keep HOU-4D's $135 billion and mandatory funding, but change what HOU-4D buys: a guarantee for extremely low-income families with children with severe problems, enrolled at up to 300,000 a year from 2034 in a stated order and complete in 2037, instead of a bounded count for an unnamed cohort. This changes HOU-4D's form, which is `chosen`; it keeps both legacy amounts. The evidence: needs are deepest among extremely low-income renters, 68.6% of all worst case needs [EV-HOU-185]; families with children are the group where the evidence on children's gains is strongest [EV-HOU-090], and long-term help sharply reduced homelessness for homeless families [EV-HOU-086], though that trial does not measure the effect for housed families like most of stage 2; and on this dossier's arithmetic, the legacy money is enough to reach the whole group by 2037. Phase it in by group (fork 8) and by market readiness (fork 1). Keep 2C and 2D as later steps, judged on what the phase-in shows about rents and lease-up, because broad allowances abroad went largely into rents where supply could not respond [EV-HOU-156]. Payment rules, landlord rules and search help are resolved below; they apply under any option. Memo: `memos/2-how-broad.md`.

## Fork 3. Production tool

**The question.** The October 26 direction asks for public and nonprofit supply with lasting affordability and a federal backstop. What should the production toolkit look like: the tax credits (HOU-2), the construction capital (HOU-3C, open under `DEC-2026-10-30-02`), public housing (HOU-5), the social housing pilot (HOU-8) and a federal builder (HOU-9)?

HOU-5 with HOU-5B and the HOU-8 pilot stay as chosen under every option. The fork has three parts, decided separately; part 3, on HOU-3C, is new in this draft.

**Options, part 1: tax credits and lasting affordability.**
- **3.1A. As chosen (HOU-2A).** All three tax credit pieces: a further Low-Income Housing Tax Credit increase with a boost for extremely low-income units, a middle-income credit and a Neighborhood Homes credit. Affordability terms as under current law.
- **3.1B. Narrower credits, permanent affordability.** Change HOU-2A to HOU-2B: keep the credit increase with the extremely low-income boost; drop or defer the middle-income and Neighborhood Homes credits. Every home built or bought with HOU-3, HOU-5B, HOU-8 or HOU-9 money stays affordable permanently, through public or nonprofit ownership or a recorded restriction; new tax credit awards carry a nonprofit right to buy at the end of the compliance period.
- **3.1C. All three credits, permanent affordability.** HOU-2A as chosen, plus 3.1B's affordability rule.

**Options, part 2: a federal builder of last resort (the open call on HOU-9).**
- **HOU-9C. No federal builder;** strengthen HOU-6's conditions instead.
- **HOU-9B. Fold it into the pilot:** if the HOU-8 social housing pilot works, its sponsor becomes the federal builder. Cheapest, slowest.
- **HOU-9A, limited.** Authorize a federal builder in 2029-30 with a small pilot capitalization, building only on federal and acquired land in tight markets where state channels fall short.
- **HOU-9A, full.** As above, scaling up in 2033-36.

**Options, part 3: construction capital (HOU-3C).** The legacy design puts about $386 billion behind construction over 2030-39 (with the states' 20% match) and scores at about $75 billion, because only the loans' subsidy cost counts (`legacy/domains/domain-housing.md`, HOU-3; the loan subsidy rate is an estimate that needs CBO's figure).
- **3.3A. Keep the legacy design (HOU-3C as chosen).** About $72 billion of grants to state revolving funds, ramped $3 billion in FY2030, $5 billion in FY2031, then $8 billion a year, with at least 30% of each year's grant forgivable for extremely low-income units; and $300 billion of federal direct loans through state agencies for mixed-income and social housing, public housing authorities' new development and nonprofit and tax-credit projects. *How the package fits:* loans for homes whose rents can repay them, grants for the deepest affordability.
- **3.3B. Keep the channels and amounts; open both to buying and preserving existing buildings.** As 3.3A, but both channels may also finance public and nonprofit purchase of existing rental buildings, including tax-credit buildings leaving their rent limits and single-family homes, with part 1's permanent affordability attached. *How the package fits:* bought homes can be ready years before new ones, so fork 1's attached awards have homes from the early 2030s, and the October 26 direction's "acquisition" gets a funded channel.
- **3.3C. More grants, fewer loans (toward HOU-3D).** For example, HOU-3D's even split: $125 billion of grants and $125 billion of loans, scored at about $140 billion (`legacy/domains/domain-housing.md`, HOU-3). *How the package fits:* more homes for the poorest without depending on attached awards, so it suits fork 1's 1A. It costs about $65 billion more in score, and $12.5 billion a year of grants is close to what the mature water revolving funds absorb, about $13 billion a year (legacy file, from CRS; not in the register), for states that mostly have no housing revolving fund yet.
- **3.3D. Less building, more rental help.** Move part or all of the grant channel into rental awards. *How the package fits:* it shifts the balance from building to help. The trade is mostly in grants: $72 billion at about $19,600 a voucher-year is about 3.7 million award-years, roughly 370,000 households for a decade. The loans score at about $15 billion ($300 billion at the assumed 5% subsidy rate), so cutting them frees enough for only about 770,000 award-years, while removing $300 billion of lending. (This dossier's arithmetic; fork 2 gives the voucher-year cost.)

**Evidence.**
- *Tax credits partly replace building that would happen anyway.* Estimates of crowd-out range from little to nearly 100% [EV-HOU-112]. One subsidized unit adds a third to a half of a unit [EV-HOU-114]; one study's best estimate is that nearly all is offset [EV-HOU-115]. Crowd-out appears in gentrifying areas, not stable or declining ones [EV-HOU-116]. New building has aimed mostly at the high end [EV-HOU-066]. In this dossier's judgment, a credit for rentals at 60-100% of area median income would work mostly in markets where private building already happens, where crowd-out is greatest.
- *Credits reach the poorest mainly with rental help attached* [EV-HOU-118], which supports the extremely low-income boost paired with fork 1's attached awards.
- *Affordability expires.* About one-third of 2.5 million tax credit units are set to leave their rent limits by 2035, about 40% counting early exits [EV-HOU-119].
- *Public housing is shrinking.* From about 1.3 million units in 1993 to just under 920,000 in 2023, with $30 billion-$70 billion of repairs needed against $2 billion-$3 billion a year of capital grants [EV-HOU-120]. Lessons from redevelopment: children who left distressed high-rises with vouchers did better as adults [EV-HOU-121], but HOPE VI returned few original residents [EV-HOU-122].
- *Social housing works at a scale the U.S. lacks.* Social housing is 43% of Vienna's homes, with rents well below the city average [EV-HOU-163], against 2-10% of the stock in the U.S. [EV-HOU-161]. Its model depends on a large limited-profit sector and dedicated financing [EV-HOU-163] [EV-HOU-165]. Montgomery County's revolving fund is a projection without independent evaluation [EV-HOU-141]; it is not relied on.
- *New state programs start slowly.* Only about 6% of the first round of pandemic rental aid was spent by May 2021, and more than $3.1 billion was moved from grantees who could not spend it [EV-HOU-150]. That is the risk a federal backstop answers. The legacy case for HOU-9 rests on a scenario model, not evidence (`legacy/domains/domain-housing.md`, HOU-9), so the evidence here does not settle 9A against 9B. The same slow start bears on HOU-3C's grant ramp: a grant channel that starts at $3 billion while states build their funds is consistent with it; a larger one (3.3C) is not.
- *Grants or loans: deep affordability needs either grants or rental help.* Tax-credit buildings reach extremely low-income renters mostly when rental help is attached [EV-HOU-118]. A loan has to be repaid from rents, and the poorest renters' rents cannot carry debt: their incomes are the problem, since rents for the poorest rose no faster than for the richest [EV-HOU-070] and after 2007 renters' incomes fell while rents rebounded [EV-HOU-071]. So a loan-heavy channel (3.3A, 3.3B) serves them only with attached awards (fork 1) or the forgivable share; a grant-heavy one (3.3C) does it without. This is reasoning from the evidence; the register has no study comparing the two financing forms.
- *Help or building: the trade.* Tenant subsidies are typically more cost-effective [EV-HOU-112] [EV-HOU-114], and subsidized building partly displaces other building [EV-HOU-114] [EV-HOU-115], which favors 3.3D. Against it: there are only 38 affordable and available homes for every 100 extremely low-income renter households [EV-HOU-024], vouchers go unused where homes are scarce [EV-HOU-092], and in supply-constrained metros homes filter up rather than down [EV-HOU-179]. Crowd-out appears in gentrifying areas, not stable or declining ones [EV-HOU-116], so building aimed at tight markets and the poorest renters displaces least.
- *Preservation.* About a third of 2.5 million tax-credit homes are set to leave their rent limits by 2035, about 40% counting early exits [EV-HOU-119]. Buying them keeps homes that already exist; the register holds no evidence on what acquisition costs or achieves (see "Evidence gaps").

**Interactions.**
- Fork 1: attached awards are what let HOU-3, HOU-8 and HOU-9 homes serve extremely low-income renters. Part 3's choice and fork 1's go together: 3.3A or 3.3B with 1B; 3.3C with 1A.
- Fork 2: 3.3D would buy roughly 370,000 more households a decade of help; it would not change the guarantee's stages unless it moved the grant channel entirely.
- Fork 4: a federal builder on federal land sidesteps local permitting there; zoning reform is needed everywhere else.
- Fork 7: every production tool depends on construction workers.
- D3: the middle-income credit is the one housing item that reaches the third and fourth income fifths (`legacy/domains/domain-housing.md`, D3). D3 is still unresolved for the fourth fifth, which nets a loss in one model measure (`charter/PROGRESS.md`, PR #45). Dropping the credit removes a benefit that reaches that group, so the incidence model must check it; it also removes a permanent tax expenditure.
- D4: tax credits are permanent and paid for at maturity. HOU-3's grants and HOU-5's repair borrow inside the envelope (C21, C31). Direct loans score at their subsidy cost. A federal builder's capital would be lent; its operating and equity costs are the real claim.

**Evidence gaps.** The register holds no independent evaluation of a U.S. public development corporation (Montgomery County's fund is uncorroborated [EV-HOU-141]) and no evidence on acquisition. A builder's cost includes development, staff and the risk that projects do not repay; section 6 must price it. HOU-3C's amounts rest on the legacy file's benchmarks (the water revolving funds, from CRS) and an assumed 2-10% loan subsidy rate, not on register entries; the register also has no figure for what a new affordable home costs to build, so this section does not convert the capital into a count of homes.

**Current law (ROAD to Housing Act).** The options stand; the baseline they build on changes.
- *No new construction money, no tax-credit change.* The Act appropriates nothing [EV-HOU-201] [EV-HOU-202] and does not amend the Low-Income Housing Tax Credit. HOU-2, HOU-3C, HOU-8 and HOU-9 duplicate nothing in it.
- *Existing channels open wider.* CDBG may now pay for new affordable construction, up to 20% of a grant [EV-HOU-215]. HOME is authorized as a standing program, with no amount, no 24-month commitment deadline and homeownership help up to 100% of area median income [EV-HOU-226] [EV-HOU-227]. A vacant-building conversion program is authorized but unfunded [EV-HOU-229]. HOU-3's revolving funds sit beside HOME and CDBG; section 4 should say how a project combines them.
- *Private capital.* Banks may now hold public welfare investments, which include tax-credit equity, up to 20% of capital instead of 15% [EV-HOU-241]. That widens the investor base for any credit increase under 3.1A, 3.1B or 3.1C.
- *Lower review costs.* USDA infill projects skip environmental studies, and HUD must exempt or exclude more housing activities, including infill construction, once it writes the rules [EV-HOU-217] [EV-HOU-218].
- *Public housing.* The Rental Assistance Demonstration is permanent, and its cap on total public housing conversions since 2012 rises from 455,000 to 555,000 units [EV-HOU-231]; just under 920,000 units remained in public housing in 2023 [EV-HOU-120]. HOU-5's repair money and HOU-5B's Faircloth repeal work on a program that conversion keeps shrinking; section 4 must say how HOU-5 treats units that convert.
- *Middle incomes.* GAO must report by July 2027 on housing for households at 80-120% of area median income and on defining "workforce housing" in federal programs [EV-HOU-242]. That is the question the middle-income credit answers.
- *Land and acquisition.* CDBG grantees must publish databases of the undeveloped land they own [EV-HOU-214], a ready list of local public land for HOU-8 or HOU-9 projects. The investor limit binds only for-profit entities and excludes governments [EV-HOU-222], so public and nonprofit acquisition of single-family homes, named in the October 26 direction, is not limited by it.

**Recommendation.**
- **Part 1: 3.1B.** This would change HOU-2A, which is `chosen`. The evidence favors deep, lasting affordability over broad credits: crowd-out is large where the market already builds, and expiring rent limits are a documented loss. With the Act in force, 3.1B's middle-income credit is deferred, not dropped: the dossier revisits it when GAO's workforce-housing study arrives in July 2027 [EV-HOU-242], as preparation before the plan's 2029 start.
- **Part 2: HOU-9A, limited.** This rests on Espen's October 26 direction ("a lawful federal sponsor/backstop where state participation fails") and on the slow start of new state programs [EV-HOU-150], not on evidence that a federal builder works; that evidence is thin. A small builder authorized in 2029 means the backstop exists before it is needed. HOU-9B is the cheaper fallback if Espen prefers to wait for the pilot.
- **Part 3: 3.3B.** Keep HOU-3C's two channels, amounts and ramp, and open both to public and nonprofit purchase and preservation of existing buildings. This keeps HOU-3C's form and funding level and changes only its eligible uses. Why keep the amounts and the loan-heavy split: with fork 1's attached awards, loans can finance homes for the poorest renters, as tax-credit buildings do when rental help is attached [EV-HOU-118]; the grant ramp matches how slowly new state programs start [EV-HOU-150]; and moving the grants into rental help (3.3D) would buy relatively little, about 370,000 households for a decade, while giving up homes in the markets where vouchers fail [EV-HOU-092] [EV-HOU-024]. Why add acquisition: the October 26 direction names it, expiring tax-credit homes are a measured loss [EV-HOU-119], and bought homes give attached awards somewhere to go before new building is finished. The acquisition part rests on the direction and judgment; the register has no evidence on acquisition yet. If Espen prefers 1A in fork 1, 3.3C becomes the better fit, at about $65 billion more in score.

Memo: `memos/3-production.md`.

## Fork 4. Zoning conditions

**The question.** What makes HOU-6's Housing Supply Fund and its conditions produce homes, rather than higher land values? And now that the ROAD to Housing Act has enacted two federal tools of the same kind, should HOU-6 be a separate program at all?

**What the Act already does** (`road-act.md`, title II):
- *Innovation Fund (section 208).* Competitive grants to local governments and tribes that have shown "an objective improvement in housing supply growth", with priority to marked improvement; at least 25 grants a year, from $250,000 to $10 million each [EV-HOU-206]. The reforms it lists are HOU-6's: by-right duplexes to apartment buildings, parking reform, lot-size reform, accessory dwelling units, faster permits [EV-HOU-207]. It authorizes $200 million a year for FY2027-2031, appropriates nothing, and ends July 2033 [EV-HOU-202] [EV-HOU-206]. States cannot apply.
- *Build Now (section 213).* From FY2029 through FY2043, metropolitan cities and urban counties whose housing growth rate improved less than the median lose 10% of their CDBG grant, and the money goes to those above the median and to fast growers. Low-cost places, places with rental vacancy above the national rate, recent disaster areas and places without zoning power are exempt [EV-HOU-208]. Places growing 4% a year or more always get a share of the bonus, and bonuses follow each place's recent growth in housing units [EV-HOU-208]. CDBG was $3.3 billion in FY2025 [EV-HOU-209]. Below the 4% line, the ranking rewards a rise in a place's own growth rate rather than a high level of building (CRS) [EV-HOU-244].
- *Planning, designs and guidance.* Planning and zoning-code grants to states, cities and regions until 2031 [EV-HOU-210]; pre-reviewed building designs [EV-HOU-212]; single-stair building guidance [EV-HOU-243]; national zoning guidelines by 2029 [EV-HOU-213]. None preempts local zoning [EV-HOU-206] [EV-HOU-243].

So the Act already pays for growth rather than ordinances, which is what option 4B in the first draft asked for, and already conditions part of CDBG on housing growth, which HOU-6's conditions were to do for new CDBG money. HOU-6 as chosen would create a second reward fund and a second CDBG test for the same reforms.

**Where the Act falls short of what the evidence favors.**
- *No money.* Nothing is appropriated, and a $10 million award cap is small next to the reforms that moved permits [EV-HOU-206].
- *No states.* The reforms followed by the most building were broad: Auckland rezoned three-quarters of its residential land [EV-HOU-123], and California's accessory-dwelling laws were statewide [EV-HOU-128]. Neither the Innovation Fund nor Build Now can reward a state.
- *No count of lower-cost homes.* Reforms have done least for lower-cost units [EV-HOU-177]. The Innovation Fund's application "may include" data on income levels served [EV-HOU-207]; neither tool rewards it.
- *Build Now's measure.* Below 4% growth a year it rewards acceleration [EV-HOU-244]. In this dossier's reading, a place that builds steadily at under 4% a year can therefore lose money while a place recovering from a slump gains. No evaluation exists yet.
- *Build Now's reach.* It covers only metropolitan cities and urban counties, and it cuts their existing grants [EV-HOU-208]. HOU-6's condition, as chosen, would have reached new CDBG money, including state-run CDBG for smaller places, and only new money (`legacy/domains/domain-housing.md`, HOU-6).
- *End dates.* The Innovation Fund ends in 2033 and the planning grants in 2031 [EV-HOU-206] [EV-HOU-210].

**Options.**
- **4A. As chosen.** A separate Housing Supply Fund rewards jurisdictions that adopt reforms, with awards scaling with units permitted, plus conditions on new transportation and new CDBG money. *For:* it needs no change to who can apply for an existing program, its fund was set to ride the budget bill, and its CDBG condition reaches new CDBG money, including state-run CDBG that Build Now does not touch (`legacy/domains/domain-housing.md`, HOU-6). *Against:* under current law it runs beside the Innovation Fund and Build Now, with two reward programs and two growth tests on CDBG for the same reforms.
- **4B. Pay for results through the Act's tools (revised).** No separate fund. HOU-6's money funds the Innovation Fund at scale, amended so that states and regions can compete with larger awards for statewide or region-wide by-right reform; awards follow homes completed; lower-cost homes are reported and rewarded separately; the $10 million cap rises; and the 2033 end date goes. Build Now stays as the only CDBG test, so HOU-6's separate CDBG condition is dropped. *Risk:* state-run CDBG for smaller places is then left without any condition, and changing who may apply to the Innovation Fund needs an amendment, not just money. The condition on new transportation money (Moving America's 2031 authorization) stays; the Act has nothing like it. HOU-6 commissions an evaluation of Build Now's formula and proposes a fix if it penalizes steady builders.
- **4C. Federal override** of local permitting for federally financed homes. Unchanged. The Act chose incentives and says its grants preempt nothing [EV-HOU-206].
- **4D. The Act as enacted.** Appropriate the Innovation Fund at its authorized $200 million a year through 2031 [EV-HOU-206] and add nothing else. Cheapest; no state role, no lower-cost count, and it ends in 2033.

**Evidence.**
- Broad reforms produced building: Auckland's upzoning of three-quarters of its residential land added an estimated 21,808 permitted homes in five years [EV-HOU-123], and California's statewide accessory-dwelling laws took annual permits from 1,336 to 30,354 [EV-HOU-128]. Houston's smaller lot sizes allowed nearly 80,000 small-lot houses [EV-HOU-127].
- Narrow ones did not: Chicago's transit-area upzonings raised land values with no added permits in five years [EV-HOU-124].
- Gains are modest and mostly at the high end: loosening reforms were associated with 0.8% more housing in three to nine years, with no significant gain in lower-cost units [EV-HOU-177].
- Minneapolis's lower rents may reflect weaker demand rather than new supply [EV-HOU-126], a reading contested by another study's supply figures [EV-HOU-125]; both views stand.
- There is no evaluation yet of the Innovation Fund or Build Now; both are new.

**Interactions.**
- Fork 1: Build Now's vacancy exemption and fork 1's tight-market trigger should use the same measure.
- Fork 3: a federal builder on federal land sidesteps local permitting there; the Act's public-land databases list local public land [EV-HOU-214].
- Vehicle: money for section 208 can ride R2 as a mandatory appropriation. Amending its eligibility and award rules may need the floor bill that already carries the transportation condition; section 5 settles which (judgment, not evidence).

**Recommendation: 4B, revised.** This would change the chosen HOU-6 more than the first draft did: it keeps HOU-6's money and its transportation condition, but drops the separate fund and the CDBG condition in favor of the Act's two tools. Paying for homes built, favoring broad reform and counting lower-cost homes are still the right design, for the reasons the evidence gives. The Act supplies the vehicle; this plan supplies the money, the state role and the lower-cost count. 4D is the cheaper fallback; 4A now duplicates current law. Memo: `memos/4-zoning.md`.

## Fork 5. Homelessness approach

**The question.** Housing First keeps people housed, but a July 2025 executive order of the second Trump administration directs agencies away from it [EV-HOU-107]. The order stays in force unless a later president revokes it, so it is part of the 2029 baseline. What should the plan propose, especially for people with active addiction, where evidence is thin?

**Options.**
- **5A. Housing First as the federal default.** Housing without preconditions; services offered, not required. Reverse the 2025 order's conditions.
- **5B. Housing First default with a recovery-housing option people can choose.** As 5A, plus funded recovery housing for people who want a sober setting, never as a condition of help, with outcomes measured for people with active addiction.
- **5C. Treatment as a condition (the 2025 order).** Require participants with substance use disorder or serious mental illness to use treatment to keep help [EV-HOU-107].

**Evidence.**
- *Housing.* In Canada's trial, Housing First participants were stably housed 71% of the time against 29% [EV-HOU-099]. A meta-analysis found people 2.46 times as likely to be housed [EV-HOU-100]; a CDC review found homelessness down 88% against treatment-first programs [EV-HOU-101]. In a New York trial, substance use was no worse than in the treatment-first group [EV-HOU-098].
- *Health and addiction.* Effects on substance use are unclear [EV-HOU-100]; mortality did not differ [EV-HOU-103]. Data on people with active, severe addiction are limited [EV-HOU-105]. The order says Housing First fails to promote treatment and recovery [EV-HOU-173], the second Trump administration's view rather than research; on those outcomes the trials are consistent with its doubts, and on housing they are not.
- *Cost.* In U.S. studies median benefits exceeded median costs, $18,247 against $16,479 per person a year [EV-HOU-102].
- *At community level.* Associations are smaller: roughly 3% less chronic homelessness per added supportive unit per 10,000 adults [EV-HOU-175], one fewer homeless veteran per added veterans' voucher [EV-HOU-176], and an association that faded after the first year in another study [EV-HOU-083]. A critic argues Housing First has not been shown to end homelessness community-wide [EV-HOU-106].
- *Scale of need.* Chronic homelessness among individuals reached 155,750 in 2025, the highest recorded [EV-HOU-016].
- *Recovery housing.* The register has no corroborated evaluation yet; it is on the evidence list.

**Interactions.**
- Fork 8: people without a home come first under the recommendation there, so this choice shapes the first awards.
- Fork 1: attached homes give people leaving the street a unit ready to enter.
- The care flagship: treatment capacity and Medicaid-funded services decide whether offered services exist.
- OUT-07: asylum seekers drove most of the 2022-2024 rise in sheltered homelessness, not the unsheltered rise [EV-HOU-062]; that is a shelter and processing question for the immigration dossier.

**Current law (ROAD to Housing Act).** No change to the options; the Act neither codifies nor reverses the 2025 order.
- The Interagency Council on Homelessness must issue a new National Strategic Plan to End Homelessness by July 2027 [EV-HOU-238]. In this dossier's judgment it will likely follow the 2025 order [EV-HOU-107], so 5A and 5B would reverse any treatment conditions carried into that plan as well as the order's.
- For FY2027-2030 grants, Emergency Solutions Grants recipients may ask to spend more than the usual cap on shelter and street outreach. HUD must refuse a recipient that removes people or their belongings without offering shelter or housing [EV-HOU-237]. That rule is a federal precedent section 4 can build on.
- Veterans with VA disability benefits are easier to qualify for HUD-VASH vouchers [EV-HOU-233].

**Recommendation: 5B.** The housing evidence is strong and consistent across trials; the treatment evidence neither supports making it a condition nor shows Housing First solves addiction. A chosen recovery option respects people who want it and lets the plan learn what works for the group the trials missed. The recovery-housing part rests on judgment: no evaluation of recovery housing is in the register yet. Memo: `memos/5-homelessness.md`.

## Fork 6. Prevention and emergency aid

**The question.** HOU-1A is an $85 billion one-time package in fall 2029 for 2030-31 rental help and construction gap financing. Is a one-time package the right tool, and what rules should it carry?

**Options.**
- **6A. As filed (HOU-1A).** $85 billion, one time, rental help and construction gap financing.
- **6B. Rental help only (HOU-1C).** $40 billion, one time.
- **6C. A standing emergency-rent fund plus a smaller one-time start.** A permanent fund for one-time emergency help to renters at risk of losing their homes, run through one channel with the delivery rules below, with a smaller one-time tranche at launch; construction gap money moves into HOU-3. This is a new option, not yet in the agenda; it gets an ID only if Espen chooses it.

**Evidence.**
- *Prevention works per case.* In Chicago, callers who reached a prevention line when funds were available were 76% less likely to enter a shelter, at about $10,300 per case averted [EV-HOU-108]. In Santa Clara County, about $2,000 of aid made households 81% less likely to become homeless within six months [EV-HOU-109]. Homebase cut shelter nights by 22.6 per family [EV-HOU-110].
- *Targeting decides the effect at scale.* Across New York City, Homebase reduced shelter entries by 5% to 11% [EV-HOU-111]. The Chicago authors estimate their cost per case would fall with better targeting [EV-HOU-108].
- *One-time national aid started slowly and its effect is disputed.* About 6% of the first round was spent by May 2021 [EV-HOU-150]. A HUD-funded evaluation credits moratoriums and aid together with filings about 45% below trend [EV-HOU-152]; lotteries in five programs found aid raised rent payment but did little for moves [EV-HOU-153]. Both views stand.
- *Integrity.* Improper payments were never measured: Treasury wrongly rated the program not at risk for FY2023 [EV-HOU-154] and later found it susceptible [EV-HOU-182].
- *Need in 2030 is uncertain.* Rents eased and vacancy reached a series high in early 2026 [EV-HOU-066] [EV-HOU-068], while 23% of renters fell behind on rent at some point in 2025 [EV-HOU-008] and eviction filings stayed near pre-pandemic levels [EV-HOU-076] [EV-HOU-077]. A standing fund responds when need rises; a one-time package is sized in advance.

**Interactions.**
- Fork 2 and fork 8: while the guarantee phases in, the fund catches households not yet covered.
- D4: a one-time package adds nothing to the FY2040 run rate; a standing fund is permanent spending and must be paid for from FY2040. Its cost is likely small next to rental help, but section 6 must price it.
- Design rules: durable instruments and recurring help beat one-time help (legacy governing decisions, standing design rules 2 and 3).

**Current law (ROAD to Housing Act).** No change. The Act creates no emergency rent aid. Its Emergency Solutions Grants waiver lets recipients put more of that grant into shelter and outreach for FY2027-2030 [EV-HOU-237]; the same grant also pays for prevention, so local prevention money may shrink in those years (judgment). Its disaster recovery block grant ends July 2029 [EV-HOU-228], before 6C's fund would start; section 4 should say whether the fund also serves renters displaced by disasters.

**Recommendation: 6C.** This would change HOU-1A, which is `chosen`. The evidence supports prevention as a standing tool and shows national one-time aid is slow to start. Its value depends on targeting. The Chicago program cost about $10,300 per case of homelessness averted, and its authors expect much less with better targeting [EV-HOU-108]; the Santa Clara aid averaged about $2,000 a household [EV-HOU-109]. In this dossier's reading, the gap means many recipients would have stayed housed anyway. Moving construction money into HOU-3 puts it in the channel built for it. Memo: `memos/6-prevention.md`.

## Fork 7. Immigration and construction labor (recommended without a memo)

**The question.** The supply goals depend on construction workers, a third of whom are immigrants (Harvard Joint Center for Housing Studies, 2024) [EV-HOU-055]. How should the housing dossier align with the immigration flagship (OUT-07)?

**Evidence.** Sources are named in plain text, since Espen decides this item.
- Immigrants were 34% of construction trades workers in 2023 (Harvard Joint Center for Housing Studies, 2024) [EV-HOU-055].
- Where enforcement rolled out, homebuilding fell and new construction cost 18% more after three years (Howard, Wang and Zhang, 2024) [EV-HOU-056].
- An estimate cited by the Congressional Research Service puts construction workers who could be lost to deportation at 1.7-1.8 million (Congressional Research Service, housing supply report, 2026) [EV-HOU-057].
- Analysts on the left and the libertarian right agree (Cato Institute; Economic Policy Institute) [EV-HOU-060] [EV-HOU-061].
- Immigration also raises rents where migrants settle, modestly for the typical metro (Saiz, 2007; Wilson and Zhou, Federal Reserve Bank of Dallas, 2026; Hunt, Orrenius and Zavodny, Brookings, 2026) [EV-HOU-050] [EV-HOU-053] [EV-HOU-054], with a lag (Congressional Budget Office, 2025) [EV-HOU-183]. In the short run the recent inflows did not expand supply (Wilson and Zhou, 2026) [EV-HOU-053].
- Asylum seekers drove about 60% of the 2022-2024 rise in sheltered homelessness, concentrated in four places (Meyer, Wyse and Williams, University of Chicago, 2025; HUD, 2024 homelessness report) [EV-HOU-062] [EV-HOU-172].

**Recommendation.** This is a dependency, not a housing choice; the immigration dossier decides its own design. The housing dossier will:
1. State its supply estimates in sections 6 and 7 as conditional on the construction workforce, and test them against a scenario in which it shrinks.
2. Ask the immigration dossier's design section to weigh the housing evidence when it sets interior enforcement priorities (IMM-4A) and the scope of earned legalization (IMM-1), and whether a construction-trades channel belongs in legal immigration (IMM-2, which names agricultural and care-worker visas but not construction).
3. Count the domestic channel: construction apprenticeships under LAB-8, which the legacy file says supply HOU-3 and HOU-6. Count factory-built housing too: the ROAD to Housing Act drops the permanent-chassis rule for manufactured homes, orders a review of FHA financing for modular building and raises FHA Title I loan limits (ROAD to Housing Act, 2026; Congressional Research Service, 2026) [EV-HOU-219] [EV-HOU-245] [EV-HOU-220]. In this dossier's judgment, factory building needs fewer workers on site, so the workforce scenario should test it as a partial hedge.
4. Plan for newcomers' housing needs where they settle: shelter surges from asylum arrivals belong with asylum processing (IMM-3), and fork 6's fund can serve receiving communities.

**For Espen (yes or no):** treat the construction workforce as a dependency the immigration dossier weighs, as above? A "no" would make it a housing decision, with its own memo.

## Fork 8. Who is reached first

**The question.** Section 1's question: who must the guarantee reach first, renters at risk of losing their homes or everyone over the burden line? With HOU-4A open (`DEC-2026-10-30-02`), the question also covers its pace. Under fork 2's recommendation, the order also decides which group HOU-4D's stage of the guarantee covers.

**Pace.** Keep HOU-4A's 250,000 awards a year over 2030-33, under every option here. A faster start would front-load help for people without a home, but lease-up is already incomplete [EV-HOU-092], and awards that cannot be used help no one; fork 2 gives the reasoning. At that pace the order decides who waits.

**Options.**
- **8A. People without a home first.** Families and individuals who are homeless, then extremely low-income renters with the most severe needs.
- **8B. Families with children first.** Extremely low-income families with children with severe needs, including homeless families, then others.
- **8C. People at imminent risk of losing their home first.** Renters facing eviction or a crisis, through the guarantee.
- **8D. No group priority.** Every eligible extremely low-income household by need score or lottery, without priority groups.

**The size of each group.**
- People without a home: 771,480 on a single night in 2024 [EV-HOU-025] and 745,652 in 2025 [EV-HOU-014]. Nearly 150,000 children in 2024 [EV-HOU-026]. Chronically homeless individuals: 155,750 in 2025 [EV-HOU-016].
- Extremely low-income families with children with severe problems: 1.717 million households, and 3.339 million children in all such worst case households [EV-HOU-186].
- Extremely low-income older adults with severe problems: 1.749 million households; other nonfamily households, mostly single people: 1.780 million [EV-HOU-186]. 1.16 million households with worst case needs included someone younger than 62 with a disability [EV-HOU-032].
- Renters over the 30% burden line: over 21 million households [EV-HOU-001].

**Evidence.**
- *For homeless people first.* The strongest trials are for them: long-term subsidies for homeless families [EV-HOU-086] and Housing First for homeless adults with mental illness [EV-HOU-099] [EV-HOU-100]. Congress has targeted vouchers this way before: 70,000 Emergency Housing Vouchers for people homeless or at risk [EV-HOU-188]. In this dossier's judgment the group is small enough to reach largely in the first years of the phase-in.
- *For families with children.* People in families with children had the largest one-year rise in the 2024 homelessness count, 39% [EV-HOU-026]. Moves to lower-poverty areas before age 13 raised adult earnings [EV-HOU-090]. Rental help reduces child hardship [EV-HOU-086].
- *Against imminent risk through the guarantee.* One-time cash prevents homelessness at low cost per case [EV-HOU-108] [EV-HOU-109], so a long-term award is more than most of these households need. Targeting is hard at scale [EV-HOU-111]. Fork 6's fund serves them better.
- *Against no priority.* With 5.8 million unassisted extremely low-income households with severe problems [EV-HOU-186] and 250,000 awards a year, a lottery would leave most homeless families waiting for years.
- *Local preferences.* Housing agencies already set local preferences based on local needs; residency requirements are barred and residency preferences cannot turn on length of residence [EV-HOU-189]. A national order would sit above these.

**Interactions.**
- Fork 2: the order matters most under a phased guarantee; under bounded help it decides who is ever helped.
- Fork 5: the approach to homelessness shapes the first awards.
- Fork 6: renters at imminent risk are served by the emergency-rent fund.
- OUT-01 and OUT-04: 8B reaches the most children; 8A reaches the most severe hardship first.
- Black renters were 28% of renters but 39% of those named in eviction filings [EV-HOU-077], and worst case needs are more common among Black and Hispanic households [EV-HOU-036]. Section 7 should check who each order reaches.

**Current law (ROAD to Housing Act).** No change. The Act sets no priorities for vouchers. It makes veterans with VA disability benefits easier to qualify for HUD-VASH vouchers [EV-HOU-233], which helps reach homeless veterans under 8A.

**Recommendation: a combination of 8A and 8B.** People without a home first, families with children among them first. Then extremely low-income families with children with severe needs. Then other extremely low-income households with severe needs, including older and disabled renters. Under fork 2's recommendation, HOU-4D's money is the second step: the guarantee for the remaining extremely low-income families with children from 2034. Renters at imminent risk are served by fork 6's fund, not the guarantee's queue. If Espen keeps a one-time package instead (6A or 6B), there is no standing route for them after 2031 beyond local programs; the order should then reserve a small share of awards for households at imminent risk. Memo: `memos/8-who-first.md`.

## Recommended without a memo

Espen decides each item, yes or no. Sources are named in plain text, with the register tag after each. None is adopted by silence, and section 4 drafts none of them until Espen agrees. Points 2, 4 and 8 are policy choices with political weight; the others are closer to implementation detail. Lasting affordability, listed here in an earlier draft, is now part of memo 3.

1. **Payment limits by neighborhood.** Set voucher payment limits by ZIP code (Small Area Fair Market Rents) in metro areas, not one limit for the whole metro. Metro-wide increases mainly raised landlords' rents; neighborhood limits moved families in Dallas to safer, lower-poverty areas (Collinson and Ganong, 2018) [EV-HOU-095]. This applies under every option in fork 2.
2. **Source-of-income protection.** Bar landlords nationwide from refusing tenants because they pay with a voucher.
   - Refusal rates were 15% and 31% where such laws exist, against 67% to 78% where they do not (HUD landlord study by the Urban Institute, 2018) [EV-HOU-093].
   - The laws modestly improve where voucher holders live (Freeman and Li, 2014) [EV-HOU-094].
   - *Consequence:* it is a federal rule on private landlords, so it needs a regular bill under the Senate rules change, not reconciliation, and landlord groups will oppose it. That is judgment, not evidence from the register. The alternative is to reward states that adopt such laws through HOU-6.
   - *Is refusing vouchers already illegal?* Not under federal law in general. Source of income is not a protected class under the Fair Housing Act. A few federal rules bar refusals only in certain properties, such as some HOME, tax-credit and HUD-sold buildings (HUD Inspector General, 2025) [EV-HOU-246]. The ROAD to Housing Act adds no protection. It lets housing agencies inspect a new landlord's unit in advance (ROAD to Housing Act, 2026) [EV-HOU-232], which lowers one cost of joining the program but does not stop refusals.
   - *State and local laws fill part of the gap.* As of January 2025, 23 states and the District of Columbia barred source-of-income discrimination statewide, 16 of them naming vouchers explicitly; 152 cities and counties in 27 states had their own ordinances (HUD Inspector General, 2025) [EV-HOU-247]. So in much of the country, refusal is still legal. How many voucher holders those laws cover is not yet in the register.
3. **Search help.** Fund search help, landlord outreach and short-term costs such as deposits with every new tenant-based award, and for tenants in attached homes who move on with a voucher (fork 1).
   - In Seattle and King County they raised moves to high-opportunity areas from 15% to 53% (Bergman and others, 2024) [EV-HOU-091].
   - Emergency Housing Vouchers carried extra fees for services and landlord incentives (Congressional Research Service, voucher program overview, 2023) [EV-HOU-188].
   - Current law now requires housing agencies to give new voucher holders a list of pre-inspected units (ROAD to Housing Act, 2026) [EV-HOU-232]; search help starts from that list. The Act has no other provision on voucher mobility or search help. Its new Moving to Work cohort may not waive portability, the right to move a voucher to another area (Congressional Research Service, 2026) [EV-HOU-234].
4. **Right to counsel.** Make legal help for tenants an allowed use of fork 6's fund, without a federal mandate.
   - Full representation helped in one Massachusetts trial (Greiner, Pattanayak and Hennessy, 2013) [EV-HOU-143] and not in its companion (Greiner and others, 2012) [EV-HOU-144].
   - New York City's program reduced evictions (Cassidy and Currie, 2023) [EV-HOU-145]. But rents rose 1.2-1.6% in its second year, enough by one estimate to leave tenants slightly worse off (Collinson and others, University of Notre Dame, 2026) [EV-HOU-147].
   - Both views stand; states and cities can choose, and their programs should be evaluated.
   - *Consequence:* no national right to a lawyer in eviction court. The alternative is a federal mandate with funding, which the evidence does not yet support.
5. **Delivery rules for emergency aid.** Let tenants self-attest income and hardship, verify with neighborhood data where possible, accept applications started by landlords, and measure improper payments from the first year.
   - Spending doubled in the month after Treasury allowed self-attestation (Congressional Research Service, Emergency Rental Assistance report, 2023) [EV-HOU-150].
   - Neighborhood-data verification and landlord applications were associated with more success (UC Berkeley and University of Pennsylvania researchers under contract to HUD, published in 2026 under the second Trump administration) [EV-HOU-152]. That evaluation is contested on overall effects (Collinson and others, National Bureau of Economic Research, 2025) [EV-HOU-153]. Because no independent study yet supports those two rules, and the evaluation was published under the second Trump administration, they rest on that one evaluation and judgment; self-attestation rests on the Congressional Research Service's account [EV-HOU-150].
   - Improper payments went unmeasured (Treasury Inspector General, 2024 and 2025) [EV-HOU-154] [EV-HOU-182].
6. **Public housing redevelopment.** Repair sound buildings first. Where buildings are redeveloped, replace every unit and guarantee residents the right to return, with a tenant-based voucher as their alternative.
   - HOPE VI redevelopment returned few original residents (Popkin and others, Urban Institute, 2004) [EV-HOU-122].
   - Children who left distressed Chicago high-rises with vouchers did better as adults (Chyn, 2018) [EV-HOU-121].
   - "Repair first" is judgment; the evidence bears on the right to return and the voucher alternative.
   - *Current law:* the Rental Assistance Demonstration, the main route by which public housing is now redeveloped, is permanent, its cap on total conversions rises from 455,000 to 555,000 units, and HUD must publish each year how many residents stay or return (ROAD to Housing Act, 2026) [EV-HOU-231]. The right to return should cover these conversions and use that yearly reporting.
7. **No residency-length rules in social housing.** HOU-8 and the guarantee should not favor people by how long they have lived in an area.
   - Vienna requires two years at a Vienna address and gives longer-term residents preference (City of Vienna) [EV-HOU-164]. That keeps out newcomers and homeless people (Friesenecker and Kazepov, 2021) [EV-HOU-162].
   - U.S. voucher rules bar residency requirements and length-of-residence preferences (HUD voucher rules, 24 CFR 982.207) [EV-HOU-189].
   - Whether fair-housing law would bar them in a new program is for section 4.
8. **The investor limit (HOU-7): make it permanent now, or leave the ROAD to Housing Act as enacted (HOU-7B)?**
   - *Current law.* Large investors (for-profit owners of at least 350 single-family homes) may not buy more from January 7, 2027. The ban is repealed on January 7, 2042 (ROAD to Housing Act, 2026) [EV-HOU-222]. It has wide exceptions, including build-to-rent and renovate-to-rent [EV-HOU-223].
   - *Reporting is already law.* Investors report their holdings by city to HUD each year, and GAO and HUD report on the ban's effects 2 and 10 years after it starts, in 2029 and 2037 (ROAD to Housing Act, 2026) [EV-HOU-224]. HOU-7's added reporting would duplicate this, so the choice is only about the sunset.
   - *The evidence is mixed.* Rents rose where merging institutional landlords overlapped (Gurun and others, 2023) [EV-HOU-138]; investors raise rents when they buy (Lee and Wylie, Federal Reserve Bank of Philadelphia, 2024) [EV-HOU-139]; their effect on access to ownership was limited (Giacoletti and others, Federal Reserve Bank of Philadelphia, 2025) [EV-HOU-140]. No study of the ban itself exists yet.
   - *What you chose, and what this would change.* You chose HOU-7: remove the sunset and add reporting. The earlier draft of this section recommended no change. This recommendation would change your choice.
   - *Recommendation: HOU-7B.* Leave the ban as enacted and decide whether to make it permanent after the 2037 reports, five years before it lapses. The ban lasts beyond the plan's 2030-39 window, the GAO and HUD reports arrive in time and continue after the ban ends, and nobody has yet evaluated the ban. That is judgment, not evidence. (Removing the sunset would ride the same regular bill as HOU-6's transportation condition, so floor time is not an argument either way.)
   - *Against:* the project's durability rule avoids sunsets on permanent policy (`legacy/domains/domain-housing.md`, HOU-7), and a later Congress could simply let the ban lapse.
   - *For Espen (yes or no):* leave the investor limit as enacted and decide after the 2037 reports (HOU-7B)? A "no" keeps HOU-7's main point: the regular bill removes the 2042 sunset. Its added reporting would still be dropped as already law, which is a change to HOU-7 under either answer.

## How the choices fit together

Taken together, the recommendations make one design:
- **A guarantee for the lowest-income renters, staged within the legacy money** (forks 2 and 8). HOU-4A's million awards over 2030-33 reach people without a home first, then the first families with children; HOU-4D's $135 billion then enrolls the rest of the extremely low-income families with children with severe problems at up to 300,000 a year from 2034, in a stated order, so that help is a right for the whole group from 2037. Later groups follow as the budget model finds the money.
- **Delivered to fit the market** (fork 1): vouchers with neighborhood payment limits, source-of-income protection and search help where homes are available; awards attached to new and acquired homes where they are not, HOU-4A's later cohorts included.
- **Backed by lasting supply** (forks 3 and 4): HOU-3C's state grants and federal loans at their legacy amounts, opened to buying and preserving existing buildings; permanent affordability; public housing repair with a right to return; a narrower tax credit; zoning rewards paid for homes built through the ROAD to Housing Act's Innovation Fund, funded and opened to states; and a small federal builder for places where state channels fail.
- **Caught early** (fork 6): a standing emergency-rent fund for renters at risk, with tested delivery rules.
- **Housing First for homelessness** (fork 5), with a recovery option people can choose.
- **On top of current law in 2029.** The ROAD to Housing Act is the baseline: its reward fund, its CDBG reallocation, its investor limit and its program changes stay, and this plan adds the money and the pieces it lacks (`road-act.md`).
- **Before section 4.** Each piece waits on Espen's decision on its memo or list item.

**What reopening the legacy items changed.** Weighed as options, the legacy amounts held up: HOU-4A's count, pace and mandatory funding, HOU-4D's $135 billion and HOU-3C's channels and amounts are each recommended as they stand. What changes is how they connect:
- *A guarantee in place of a fixed count* (fork 2). The same money, aimed at named groups, makes help a right for those groups by about 2037 instead of a second million awards handed out through waiting lists.
- *Attached awards and loans as one tool* (forks 1 and 3). Attached awards supply the rent that lets HOU-3C's loan-financed homes serve the poorest renters; that is why the loan-heavy split works. If Espen keeps vouchers everywhere (1A), the better fit is more grants (3.3C).
- *Acquisition as the bridge in time* (fork 3, part 3). Bought buildings give attached awards homes before new building is finished.
- *The balance between help and building.* About $297 billion of rental help over FY2030-39 (HOU-4A's $162.2 billion working midpoint with administration, and HOU-4D's $135 billion) against about $75 billion of scored construction capital that puts about $386 billion to work. Moving the grant channel into help would buy about 370,000 households a decade of help; this dossier does not recommend it, because the markets where vouchers fail are the ones that need the homes.

**Fairness and fiscal tests (OUT-11).**

| Item | D4 class | D3 reach |
| --- | --- | --- |
| HOU-4A, HOU-4D and the guarantee (forks 2, 8) | Permanent: paid for from FY2040. Under fork 2's recommendation, HOU-4D's stage is a right, so its cost follows take-up | Bottom two income fifths |
| Standing emergency-rent fund (fork 6, if chosen) | Permanent: paid for from FY2040 | Bottom two income fifths |
| One-time emergency aid (HOU-1) | One-time: no FY2040 claim; counts in the ten-year total | Bottom two income fifths |
| Tax credits (HOU-2) | Permanent tax expenditure: paid for from FY2040 | Mostly low incomes; the middle-income credit reaches the third and fourth fifths |
| HOU-3 grants, HOU-5 repair | Time-limited capital: borrowed inside the envelope (C21, C31). Acquisition under fork 3, part 3 stays inside the same amounts | Low incomes |
| HOU-3 loans, HOU-9 lending | Scored at subsidy cost; operating and equity costs are the claim | Low and middle incomes |

The project's long-term model already fails the FY2040 test after the October 24 adoptions (legacy governing decisions, D4). The guarantee is the largest permanent claim in this dossier, so its phase-in and its financing must be decided together; section 6 does that with the budget model.

**Immigration (OUT-07).** The supply side depends on the construction workforce (fork 7), and newcomers add to demand where they settle [EV-HOU-053] [EV-HOU-183]. The two dossiers should test their designs together.

## Housekeeping

- **HOU-4A, HOU-4D and HOU-3C in the agenda.** PR #73 (`DEC-2026-10-30-02`) moves HOU-4A from `decided` to `chosen`, adds HOU-4D as `chosen` at L1 (its cohort, award count and phase-in not chosen), and notes that HOU-3C stays `chosen` as a working choice. This section reads them that way. If Espen decides fork 2 as recommended, the next charter PR should rename HOU-4D to say what it buys ("Guarantee for extremely low-income families with children, from 2034, within $135B FY2030-39"); if Espen decides fork 3, part 3 as recommended, HOU-3C's name gains "including acquisition and preservation". New options Espen chooses here (such as fork 6's standing fund) get rows in the same PR.
- **HOU-7 and HOU-7B.** Both rows exist in `agenda/agenda.csv` and both are `chosen`, though they are alternatives; HOU-7B's name ("Investor limit permanent / leave ROAD as enacted") is the old register's label for the pair. After Espen answers point 8, the next charter PR should name HOU-7B "Leave the ROAD to Housing Act's investor limit as enacted" and mark only the chosen one. Agenda edits are tier 3, so this section makes none.
- **HOU-6's name and design.** If Espen chooses fork 4's revised 4B, HOU-6 becomes "Fund and extend the ROAD to Housing Act's Innovation Fund; transportation condition", and its CDBG condition is dropped. The same charter PR records it.

## Evidence still needed

| Claim | Source | Status |
| --- | --- | --- |
| Evaluations of recovery housing and treatment-linked housing for people with active addiction | National Academies of Sciences, Engineering, and Medicine, *Permanent Supportive Housing* (2018); recovery-housing studies | Not yet read; fork 5 rests on the trials without it |
| Voucher costs per household by income group and market, current year | HUD budget justifications; CBO | Fork 2 uses the FY2023 account average as a rough guide |
| Lease-up and rent effects of project-based vouchers | HUD research; academic studies | Needed for fork 1's share of attached awards |
| Acquisition of existing buildings by public and nonprofit owners: cost and outcomes | Academic and agency evaluations | The October 26 direction names acquisition, and fork 3, part 3 now recommends funding it; no evidence in the register yet |
| Homeless households (not people), on a night and over a year | HUD's homelessness reports, households tables | Fork 2's split of HOU-4A between people without a home and families is an assumption without it |
| Development cost per affordable home, new and acquired | Tax-credit cost studies; GAO; state housing finance agencies | Needed to turn HOU-3C's capital into a count of homes (fork 3, part 3) |
| What state revolving funds can absorb a year | CRS on the clean water and drinking water state revolving funds (the legacy file's about $13 billion a year) | 3.3C's feasibility rests on the legacy file's figure, not the register |
| Loan subsidy rate for a federal housing construction loan program | CBO credit-subsidy estimate | HOU-3C's $75 billion score assumes 2-10% (legacy estimate) |
| Evidence on public development corporations in the U.S. | Independent evaluations | Montgomery County's fund is uncorroborated [EV-HOU-141] |
| Share of voucher holders covered by state and local source-of-income laws | A current count by voucher holder, from HUD data matched to the Inspector General's list [EV-HOU-247] | Point 2 gives only the number of laws |
| Fair-housing law on residency preferences in a new federal program | Fair Housing Act case law; HUD guidance | Section 4 |
| Rural, tribal and Native housing (NAHASDA) | HUD, tribal housing research | Not covered in sections 1-3. The ROAD to Housing Act's rural provisions are mapped in `road-act.md` [EV-HOU-217] [EV-HOU-239] [EV-HOU-240]; evidence on outcomes is still missing |
| Effects of the ROAD to Housing Act's Innovation Fund and Build Now; HUD's first Build Now growth rates | HUD notices and data; later evaluations | Neither tool is funded or evaluated yet; fork 4 rests on the earlier zoning evidence |
| Evaluation of the investor limit | GAO and HUD reports due 2029 and 2037 [EV-HOU-224] | Not yet due; point 8 rests on earlier studies |

## Questions for Espen

Seven decision memos, one per fork, in `memos/`:
1. `memos/1-help-or-homes.md`: how to place new rental help in tight and loose markets.
2. `memos/2-how-broad.md`: how broad the rental guarantee should be.
3. `memos/3-production.md`: three parts: tax credits and lasting affordability; the federal builder of last resort; the construction capital (HOU-3C).
4. `memos/4-zoning.md`: what the zoning fund pays for.
5. `memos/5-homelessness.md`: Housing First and a recovery option.
6. `memos/6-prevention.md`: a standing emergency-rent fund or a one-time package.
7. `memos/8-who-first.md`: who the guarantee reaches first.

Memos 1, 2, 3 and 8 now weigh the legacy rental-help and construction designs (HOU-4A, HOU-4D, HOU-3C) as options (`DEC-2026-10-30-02`). Memo 2 recommends changing what HOU-4D buys; memo 1 recommends attaching part of HOU-4A's later cohorts in tight markets; memo 3 recommends keeping HOU-3C's amounts and adding acquisition.

Also a yes or no on fork 7 and on each of the eight points under "Recommended without a memo". On point 8 the recommendation has changed: leave the Act's investor limit as enacted (HOU-7B) rather than remove its 2042 sunset now (HOU-7, as chosen).
