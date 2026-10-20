# Domain file: Immigration (IMM)

Canonical as of Oct 19, 2026 (batch 4). This file covers legalization, legal immigration and the backlogs, asylum and border processing, interior enforcement, birthright citizenship and naturalization, and USCIS delivery. On substance it replaces Bill Book 15, ledger row E11 and staging inventory row 19.1. The immigration court is designed in domain-courts.md CRT-5 and is referenced here, not restated.

All figures are ten-year totals for 2030-39, in trillions unless marked. Basis tags: **sourced**, **scaled** and **estimate** (mine). Survival at 51 (Dec. D1): ✔ survives, ◐ needs a D2 majority-precedent path, ✖ needs 60, 67 or Republican votes. Espen's Oct 19 call puts E11 among the bills that **must** pass in the first trifecta.

## Summary

| ID | Program | Chosen design | General-fund net (low / mid / high) | Vehicle | @51 | Floor days | Felt by Nov 2030? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IMM-1 | Earned legalization | Tiered: Dreamers, TPS holders and farmworkers get a direct green-card path; residents of 10+ years with clean records get a five-year path; registration opens within 180 days | -0.25 / -0.15 / -0.05 (together with IMM-2) | FL | ◐ | 12 (one bill, IMM-1 to IMM-6) | Partly (registration and work permits, not green cards) |
| IMM-2 | Legal immigration and backlogs | Recapture unused green cards; spouses and minor children of permanent residents exempt from caps; per-country caps lifted; statutory H-1B fee and wage-ranked selection; agricultural and care-worker visas | inside IMM-1 | FL | ◐ | 0 | No |
| IMM-3 | Asylum and border processing | Asylum merits decided by USCIS asylum officers within 180 days; regional processing abroad; statutory refugee floor; port-of-entry screening technology | 0.00 / 0.01 / 0.02 | FL | ◐ | 0 | Partly |
| IMM-4 | Interior enforcement | Enforcement priorities, detention standards and a detention-capacity cap in statute; officer identification; phased mandatory E-Verify after legalization registration closes | 0 (see note) | FL | ◐ | 0 | Yes |
| IMM-5 | Birthright citizenship and naturalization | Codify *Trump v. Barbara* in 8 U.S.C. 1401; procedural limits on denaturalization; naturalization fee waivers | 0.00 / 0.00 / 0.01 | FL | ◐ | 0 | Yes |
| IMM-6 | Delivery | USCIS rebuilt (about 12,000 hires); a statutory processing-time target; an Office of New Americans | in CAP-7 (USCIS, $40B) plus fees | FL / AP | ◐ | 0 | Partly |
| | **General-fund total** | | **-0.25 / -0.14 / -0.02** | | | **12** | |

The ledger carries E11 at -$0.15T and 12 floor days. This file keeps both. It adds IMM-3's processing costs (about $0.01T, estimate) and moves no total by more than that. IMM-1 and IMM-2 are scored together because almost all of the revenue comes from the people they bring into the formal economy.

## Where things stand (world state, Oct 2026)

- **Border.** Border Patrol recorded 98,708 southwest-border apprehensions in FY2026 and zero releases for the year. Nationwide encounters were 379,243, the lowest annual figure on record (preliminary DHS/CBP data, Oct 16, 2026, via Voz). The 2029 problem is not a border surge. It is the interior system and the backlogs.
- **Detention.** ICE held 65,765 people on about July 20, 2026. About 70% had no criminal conviction (Deseret; Latin Times, Sept 2026, from ICE data). The monthly average was 71,937 in January 2026. ICE recorded 356,389 removals in FY2026 through July 11 (Latin Times, from ICE).
- **Money.** The One Big Beautiful Bill Act (July 2025) funded 10,000 more ICE officers and about $45B for detention capacity. That is enough to hold about 100,000 people at once (WJLA, Nov 2025; officer figure from domain-courts.md). It also capped immigration judges at 800. Most of that money is multi-year mandatory funding that runs out before or around FY2029 (my reading; check the expiry dates). So detention capacity in 2030-39 is an appropriations choice, not something CBO's baseline extends.
- **Birthright citizenship.** *Trump v. Barbara* (June 30, 2026) held Executive Order 14160 unconstitutional. The Fourteenth Amendment covers children born to temporarily or unlawfully present parents. Roberts wrote for five justices on the constitutional ground. Kavanaugh concurred only in the judgment, on 8 U.S.C. 1401(a) "unless and until" Congress changes it. Thomas, Alito and Gorsuch dissented (CRS LSB11468, Aug 2026). The CRS report notes that the Born in the USA Act would codify the holding.
- **TPS.** On June 25, 2026, the Supreme Court let the administration end TPS for about 350,000 Haitians and about 7,000 Syrians. It held that non-constitutional claims about terminations are not reviewable. DHS is now asking lower courts to lift their remaining orders (Bloomberg Law, June 30, 2026).
- **DACA.** There were 436,350 active recipients on June 30, 2026, down by nearly 100,000 since January 2025. USCIS processes renewals only, and 125,282 are pending. The Fifth Circuit's January 2025 ruling would end work permits for Texas's 82,410 recipients, but it is not yet in effect. On April 24, 2026, the BIA held that DACA alone does not stop removal proceedings (National Immigration Forum, Oct 2026).
- **H-1B fee.** The $100,000 proclamation fee was struck down on June 8, 2026 (D. Mass.) as a tax Congress had not authorized. DHS proposed a $103,265 fee by rule on Aug 25, 2026 (CDF Labor Law, Aug 2026). Whatever happens in that litigation, Congress holds the pen on fees of this size.
- **Bipartisan floor.** The Dignity Act (Salazar and Democratic co-sponsors) proposes legal status without a citizenship path. Republican leaders called it dead on arrival in April 2026 (Daily Signal, Apr 12, 2026). Salazar broke with the administration on enforcement in a September 2026 campaign ad (Florida Phoenix). There is a small Republican pool, but not 60 votes.

## IMM-1. Earned legalization

**Design.** Modeled on the U.S. Citizenship Act framework (Bill Book 15), in three tiers:

| Tier | Who | Path |
| --- | --- | --- |
| A | Dreamers (arrived as children, with a schooling, work or service test), TPS holders as of a cutoff date, farmworkers with a work history | Green card on approval; citizenship after three years |
| B | Residents continuously present 10+ years before the cutoff, with clean records | Provisional status with a work permit; green card after five years; then the normal naturalization clock |
| C | Everyone else present before the cutoff | Not covered by the baseline; see options |

- **Vetting:** biometrics and background checks for every applicant, with bars for serious crimes.
- **Fees and back taxes:** application fees cover processing, as USCIS fees do now. Back taxes are owed only on income already earned, a design choice that keeps the tier B application cost from becoming a bar.
- **Registration window:** 18 months, opening within 180 days of enactment.

**Why tiers.** Tier A has the broadest public support and the longest residence. Tier B is where most of the long-settled population sits. Tier C is the hardest vote, and leaving it to a later bill keeps E11 passable at 52-54 without dropping the pathway.

**Options.**

| Option | Design | Note |
| --- | --- | --- |
| IMM-1A (chosen) | Tiers A and B | As above |
| IMM-1B | Tier A only | The likeliest version to find Republican votes if D2 fails; leaves most of the long-settled population out |
| IMM-1C | Dignity Act model: legal status and work permits for long-term residents, restitution payments, no citizenship path | The Republican-sponsored floor; trades citizenship for status. Use only as a G-path fallback |
| IMM-1D | Tiers A, B and C (full U.S. Citizenship Act) | The most complete; the hardest floor vote |

**Cost.** The ledger's -$0.15T, with a range of -$0.25T to -$0.05T (estimate), comes from CBO's score of S. 744 (2013), which cut deficits by about $175B in its first decade (sourced, via the ledger). That figure has not been rescored. Two things push the real number toward the low end: today's fully employed labor market, and the bill's lack of a guest-worker expansion on S. 744's scale. Benefit bars push the other way. The baseline bars tier B from means-tested federal benefits for five years, on the S. 744 model; ACA subsidies and FAM-1's child credit follow their own rules, set in those files. **Needs a real score**, to be done together with CRT-5 (the courts file asks for the same).

**Vehicle.** FL. The Senate parliamentarian rejected three legalization designs for the 2021 reconciliation bill (my knowledge; not re-checked). So legalization is not a reconciliation item.

## IMM-2. Legal immigration and the backlogs

**Design.**

- **Recapture:** green cards that went unused in past years because of processing delays go back into the pool.
- **Family:** spouses and minor children of permanent residents are exempt from the numerical caps.
- **Per-country caps:** lifted for employment-based visas over three years.
- **H-1B:** selection is ranked by offered wage instead of a lottery. A fee set in statute (about $5,000 to $10,000 by employer size, estimate) is retained by USCIS and a training fund. This replaces the fee fight that ended in the June 2026 ruling with a fee Congress actually authorized.
- **Sectoral visas:** expanded agricultural visas with year-round eligibility, and a care-worker visa tied to FAM-2's child-care workforce and HLT-4's long-term-care workforce.

**Note.** The H-1B fee is a small new channel (about $0.01-0.02T, estimate). It funds adjudication and training, not the general fund.

## IMM-3. Asylum and border processing

**Design.**

- **Asylum:** USCIS asylum officers decide merits within 180 days, on the 2022 Asylum Processing Rule model, now put in statute. Denials go to CRT-5's Article I court.
- **Processing abroad:** regional processing centers so that claims can be filed before a dangerous journey.
- **Refugees:** a statutory floor for annual refugee admissions (about 50,000, estimate), so the ceiling can no longer drop to near zero by proclamation. The President still sets the ceiling above the floor.
- **Ports of entry:** screening technology for fentanyl and contraband at the ports, where most of it enters (my knowledge; widely reported), instead of new wall construction.
- **Alternatives to detention:** case management for families and people with no criminal record.

**Cost.** About $0.01T, range $0 to $0.02T (estimate), for the asylum officer corps and regional processing beyond what IMM-6's USCIS line covers.

## IMM-4. Interior enforcement

**Design.**

- **Priorities in statute:** national security, public safety and recent unlawful entry come first, with the reasons recorded for each arrest outside them.
- **Detention:** standards enforceable by detainees in court; a statutory cap on average daily detention (about 30,000, estimate) with a waiver for emergencies reported to Congress; alternatives to detention as the default for those not in the priority groups.
- **Officers:** visible identification and no masked arrests except in documented undercover work. One statute is referenced from both this file and domain-executive-power.md, the same pattern as Safe Everywhere and EXE.
- **Protected places:** no enforcement at schools, places of worship, hospitals or courthouses without a warrant or exigent circumstances.
- **E-Verify:** mandatory for all employers, phased in by size only after tier A and B registration closes, with worker protections against wrongful non-confirmation.

**The pairing (design rule 4).** E-Verify is the moderate wing's ask and the bill's answer to "legalization invites the next wave." Sequencing it after registration closes means it cannot be turned against people the bill is legalizing.

**Cost note.** Shrinking detention from about 65,000 toward the 30,000 cap would cost less than current levels. But OBBBA's detention money is time-limited, so it is not in the 2030-39 baseline. That means no savings can be booked. This row is zero against the baseline (estimate).

**Options.**

| Option | Design | Note |
| --- | --- | --- |
| IMM-4A (chosen) | Priorities, standards and a cap in statute, inside a restructured ICE | Changes conduct without a reorganization fight |
| IMM-4B | Bill Book 15's DHS split: customs enforcement retained; interior enforcement replaced by a Humanitarian Processing Service | The second version, folded here. A larger reorganization, a harder vote, and an easy target for the trust gap |
| IMM-4C | Priorities by executive guidance only | Reversible by the next administration; fails design rule 2 |

## IMM-5. Birthright citizenship and naturalization

**Design.**

- **Codify *Barbara*:** amend 8 U.S.C. 1401 to state the Court's holding in its own words. Kavanaugh's concurrence rests on that statute, so writing it down closes the one route he left open. This follows the Born in the USA Act model.
- **Denaturalization:** clear and convincing evidence in a judicial proceeding, a statute of limitations, and no civil denaturalization drives based on quotas.
- **Naturalization:** fee waivers below 200% of poverty, and an English-and-civics test kept at the 2008 standard.

## IMM-6. Delivery

**Design.**

- **Staffing:** USCIS rebuilt with about 12,000 hires (Bill Book 15), a statutory target of six months for standard benefit applications, and online filing for every form.
- **Funding:** fees fund most adjudication. The CAP-7 USCIS line ($40B over 2030-39, estimate) funds the hiring surge for IMM-1's registration. A further $6B from CAP-7's reserve is proposed for the asylum officer corps and refugee processing (see the capacity note).
- **Integration:** an Office of New Americans for English classes, credential recognition and integration grants (appropriations).

## Survival at 51 (D1 stress test)

- **Under F or C:** the bill passes with every vote at 52-54 if D2 holds, but it carries the most defection risk of any first-Congress bill after statehood (Bill Book 15's war game).
- **Under G (carve-out only):** the bill fails. IMM-5's codification might ride the democracy package as a citizenship-definition provision, but that is a stretch of "democracy and elections" (my judgment). IMM-1B with IMM-4 might find 60 votes in a different Senate, not this one.
- **At 51 without D2:** almost nothing here survives. The exceptions are the executive pieces: USCIS processing guidance, enforcement priorities by memo, TPS designations, refugee ceilings and parole. All of them are reversible.

## Dependencies

- **Courts.** CRT-5's Article I immigration court decides IMM-3's denials and removal cases. The two need one score.
- **Executive power.** Officer identification (IMM-4) is the same statute as the federal law-enforcement identification row (staging 5.11).
- **Family and health.** FAM-1's child credit, FAM-2's child-care workforce and HLT-4's care workforce interact with the care-worker visa and the benefit bars.
- **Labor.** E-Verify and the sectoral visas carry wage and labor standards that follow domain-labor.md.
- **Revenue.** The general-fund effect is negative (savings). The new H-1B fee is a small channel. Nothing reaches households, so nothing enters the D3 test except IMM-5's fee waivers, which are a benefit.

## Capacity note (design rule 6)

| Agency | Rows | Source of funds (2030-39) |
| --- | --- | --- |
| USCIS | IMM-1, IMM-2, IMM-5, IMM-6 | CAP-7 USCIS line ($40B, estimate) plus fees |
| USCIS asylum division and refugee processing | IMM-3 | **Proposed: $6B from CAP-7's batch 4 reserve** (estimate) |
| Immigration court | IMM-3, IMM-4 | CRT-5 (about $0.03T, estimate) |
| CBP Office of Field Operations | IMM-3 port screening | Inside IMM-3's cost |

## Design-rule check

| Rule | How this file meets it |
| --- | --- |
| Reciprocity | Enforcement priorities and detention standards bind every administration equally |
| Durable instruments | Legalization is the most durable act in the agenda: green cards are not revocable by a future Congress. Priorities, caps and the refugee floor are in statute |
| Legibility | Named tiers, a registration window with a start date, and a published processing-time target |
| Pairing | E-Verify travels with legalization, phased after registration |
| Supply with demand | USCIS capacity is funded before the registration window opens |
| Capacity first | USCIS, the asylum corps and CRT-5 are named and funded |
| Write for this Court | IMM-5 codifies *Barbara*'s holding in the statute Kavanaugh relied on |
| One version per policy | The DHS split (Bill Book 15) is folded in as IMM-4B |
| Every number has a basis | The -$0.15T is a scaled 2013 score and needs a fresh one |

## Second versions found and folded

| Policy | Versions | Resolution |
| --- | --- | --- |
| DHS enforcement structure | Bill Book 15 and the unified agenda (Humanitarian Processing Service); this file's priorities-and-cap design | IMM-4A chosen; the split is IMM-4B |
| Immigration courts | Bill Book 15's "more judges"; CRT-5's Article I court | One home, CRT-5 |
| Officer identification | Staging 5.11; IMM-4 | One statute, referenced from both files |

## Crosswalk

| Old row | New home |
| --- | --- |
| Ledger E11; Bill Book 15; staging 19.1 | IMM-1 to IMM-6 |
| Unified agenda "DHS Restructuring" | IMM-4B (option) |
| Staging 4.5 (immigration court) | CRT-5 (unchanged) |
| **New rows needed at the rebuild** | IMM-3's ~$0.01T inside E11; the H-1B fee channel (~$0.01-0.02T, estimate) |

## Open items

1. **Rescore E11** against current law and the 2030-39 window, together with CRT-5.
2. **Check OBBBA's ICE and detention expiry dates.** If any money runs past FY2029, IMM-4's cap produces bookable savings.
3. **Tier C:** decide whether to hold it for a later bill or include it (IMM-1D).
4. **Refugee floor size:** about 50,000 is an estimate, chosen to sit below every ceiling set from 1980 to 2016 (my knowledge; not re-checked).

## Sources

- [Voz, DHS FY2026 border data (Oct 16, 2026)](https://voz.us/en/politics/261016/40031/dhs-reports-95-drop-in-arrests-at-the-southwest-border-in-2026.html)
- [Deseret News, ICE detention bookings (July 22, 2026)](https://www.deseret.com/politics/2026/07/22/ice-detention-centers-reach-record-bookings-in-june-for-trump-immigration-crackdown/)
- [Latin Times, ICE removals and detainee convictions (Sept 9, 2026)](https://www.latintimes.com/ice-says-its-deported-356000-people-this-year-while-70-detainees-have-no-conviction-599101)
- [WJLA, record ICE custody and OBBBA detention funding (Nov 25, 2025)](https://wjla.com/news/nation-world/record-levels-of-migrants-in-ice-custody-as-deportations-and-arrests-hit-record-pace-immigration-us-mexico-border-cbp)
- [CRS LSB11468, *Trump v. Barbara* (Aug 13, 2026)](https://www.everycrsreport.com/reports/LSB11468.html)
- [Bloomberg Law, DHS seeks to lift court orders on TPS (June 30, 2026)](https://news.bloomberglaw.com/employment/dhs-seeks-to-lift-court-orders-preserving-immigrant-protections)
- [National Immigration Forum, current status of DACA (Oct 2026)](https://forumtogether.org/article/current-status-of-daca-explainer/)
- [CDF Labor Law, $100,000 H-1B fee, take two (Aug 26, 2026)](https://www.cdflaborlaw.com/blog/100000-h-1b-visa-fee-take-two)
- [Daily Signal, Republicans on the Dignity Act (Apr 12, 2026)](https://www.dailysignal.com/2026/04/12/republicans-indicate-bipartisan-amnesty-bill-dead-on-arrival/)
- [Florida Phoenix, Salazar campaign ad (Sept 17, 2026)](https://floridaphoenix.com/2026/09/17/maria-salazar-breaks-with-trump-on-immigration-enforcement-in-campaign-ad/)
- domains/domain-courts.md CRT-5 and its sources (TRAC, EOIR, the Rebalancing review)
- archive/wargame-floor-time-bill-book.html, Bill 15 (ideas only); index/2029-trifecta-master-ledger.md, E11
