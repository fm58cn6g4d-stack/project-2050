# ARCA update instructions — from the transit (ATRA) and package work, October 12, 2026

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/arca-handoff-2026-10-12.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Paste this into the ARCA chat. It lists what the transit work and CBO's September 30 estimate of H.R. 8870 changed for ARCA, what I've decided, and the edits to make. All figures come from `index/tools/transportation/transit_fiscal_model.py` in the project. Rerun it rather than computing by hand.

Reference docs:
- Package section-by-section (250-Plus, reconciliation, 2031 bill, Divisions A-F): https://claude.ai/code/artifact/fb14029c-152b-4727-9ae3-b2f055c8b6f7
- ATRA architecture doc: https://claude.ai/code/artifact/6eded0d5-40fc-433a-b940-8d8ca015f581
- Status and decisions: `sources/transportation-transit-package-status-oct12.md`

## 1. Decisions already made (don't relitigate; apply them)

1. **One 2031 bill.** ARCA becomes Division D of the Surface Transportation Reauthorization Act of 2031, and keeps its short title. Its Title I (revenue and trust fund) moves to the shared Division A (Ways and Means / Finance).
2. **Trust fund architecture C.** One Surface Transportation Trust Fund (26 U.S.C. 9503 redesignated) with three accounts: Highway, Mass Transit and Intercity Passenger Rail.
   - The highway and transit accounts are first credited with their FY2028 receipts, CPI-indexed.
   - Receipts above those floors split **35% highways / 50% transit / 15% rail**.
   - Within each account, renewal is paid before expansion.
   - ARCA's five rail accounts become subaccounts of the rail account.
   - I've kept 35/50/15 even though the equal-coverage answer is now 34/54/12. The EV fee is due for a larger redesign later.
3. **Per-mile fee.** 1.0 cent in FY2029, rising 0.2 cents a year to 3.6 cents in FY2042, on all vehicle-miles. Fuel taxes phase down over the same 14 years. Collection cost is 10%.
   - ARCA's schedule (0.6 cents, reaching 3.6 cents in FY2044) is retired.
   - The reason is House highway levels, not ARCA's yield anchor.
4. **Yield basis.** Price the fee on FHWA vehicle-miles: 3,323.8B in 2025, growing 0.5% a year.
   - ARCA's anchor ("2.4 cents replaces ~$44B") is wrong: 2.4 cents grosses about $80B. Receipts are replaced at about 1.4 cents.
5. **Highway denominator.** H.R. 8870 levels: $72.9B–77.6B a year FY2027-31, then +2.5% a year. NHTSA and FMCSA (about $2.0–2.5B a year) are now counted in the Highway Account's need.
6. **No $132B general-fund transfer into a rail fund.** Rail expansion becomes mandatory general-fund appropriations for sections 303, 310, 311 and 312 ($93.20B over FY2031-35). The renewal shortfall is covered by Division A section 110 transfers to each account, the IIJA precedent.
7. **Section 107.** ARCA's $12B rail-only floor is replaced by continuation of every account's renewal programs at FY2035 levels if reauthorization lapses.
8. **Section 108.** The trigger cuts expansion first and renewal last, not proportionally. Executed agreements are exempt. Section 106(e)'s $25B readiness reserve goes expressly under the trigger.
9. **The 0.206% cap is a benchmark, not a law.**
   - Neither CBO nor statute sets it. ARCA set 0.192% (the FY2026 general-fund draw on surface programs) as its own discipline rule. The model restates that as 0.206% so annual appropriations are counted the same way.
   - I'm fine exceeding it. Describe it as a benchmark everywhere, never as a CBO limit.
   - The real constraints are the reconciliation instructions, PAYGO and the Byrd rule. CBO scores new excise receipts net of about 25% for lost income and payroll taxes, and the instructions have to be sized to that score.
10. **Joint facilities (Division A sec. 109).**
    - Transit and rail accounts both pay for shared facilities. Renewal is split by share of train movements; expansion by share of added train movements.
    - Delete ARCA's bar on chapter 53 uses at joint facilities.
    - ARCA's 30% transit-share placeholder for terminals is wrong. Commuter trains run 79% of movements at Chicago and carry about 85–94% of riders at the four existing terminals.
11. **Byrd rule for reconciliation.** Capital grants for projects not yet under agreement, Capital Investment Grants included, are reconciliation-eligible if they carry obligation and expenditure deadlines (the ARP sec. 3401 precedent).
    - ARCA's Byrd table says greenfield capital is "barred in practice." Change it to "available with obligation and expenditure deadlines."
12. **250-Plus.**
    - Drop the Corridor ID sunset extension (October 1, 2031 to 2033) as a Senate concession. Division D makes Corridor ID permanent, and an extension act can move the date if the 2031 bill slips.
    - Ask for a two-account general-fund transfer of $108.0B ($71.2B highway, $36.8B transit), sized to CBO's shortfall through FY2030. This replaces a transit-only transfer.

## 2. What CBO's September 30, 2026 estimate of H.R. 8870 means for ARCA

- **Confirmed.**
  - Amtrak grants $31.065B FY2027-31 (NEC + National Network).
  - Rail infrastructure grants $27.605B (Partnership Program + CRISI).
  - Railroad crossing elimination $3.65B.
  - FRA operations and research $1.80B.
  - So ARCA's H.R. 8870 column (~$62.4B) is right.
- **RRIF.**
  - H.R. 8870 raises the outstanding-principal cap from $35B to **$50B**. It extends RRIF eligibility to Amtrak and to interstate compacts for equipment pools, transit-oriented development within half a mile of stations, and freight shipper facilities.
  - It also lets rail grants pay credit risk premiums (sec. 10513) and authorizes $250M for RRIF credit assistance (sec. 10515).
  - ARCA's $150B cap should be described as "from $50B (as raised by H.R. 8870)."
- **Other general-fund grants rail can reach.** National Infrastructure Grants, $10B (sec. 7105), are open to Amtrak in partnership. Multimodal freight is $6B.
- **Trust fund.**
  - Cumulative shortfall at the end of FY2031 is $99.5B (highway) and $48.2B (transit). The highway account runs dry in FY2028, the transit account in FY2027.
  - The EV fee runs through FY2036 and goes to the **general fund**, not the HTF: $16.8B gross, $12.4B net.
  - Any ARCA text that says the EV fee expires after FY2035 or feeds the trust fund is wrong for 250-Plus. Division A moves it into the fund.
- **Model receipts reproduce CBO's Table 6 to the decimal** ($49.1B current-law receipts in FY2029).

## 3. Numbers to restate in ARCA (base case: scenario B, architecture C, NHTSA/FMCSA included)

| Item | Old ARCA figure | Replace with |
| --- | --- | --- |
| Affordability, ARCA alone, all-in (FY2029-30 / 31-35 / 36-40 / 41-45) | 0.105% / 0.099% / 0.019% / 0.001% | 0.149% / 0.130% / 0.072% / 0.068% |
| ARCA + ATRA together, average (peak) | — | FY2029-30 0.194% (0.197% FY2030); FY2031-35 0.185% (0.189% FY2033); FY2036-40 0.130%; FY2041-45 0.127% |
| Room under the 0.206% benchmark | — | FY2030 $3.1B; FY2031-35 $6.9B–11.2B a year; after the $25B reserve at $5B a year, $1.9B–6.2B |
| CBO-basis (net of excise offset) | — | FY2030 0.219%; FY2031-35 0.204–0.214% |
| ARCA's dedicated-revenue rows on vehicle-miles (ARCA's own shares and schedule) | as drafted | +21% / +13% / +8% / +3% by period |
| Rail dedicated coverage of whole program, FY2041-45 | 107% (8–28% share) | 50% (15% of new receipts); renewal programs 78% |
| Rail account dedicated receipts FY2031-35 | — | $65.7B (15% share + aviation and diesel taxes $35.5B) |
| Rail general fund FY2031-35 | $132B transfer | $188.4B = $95.2B renewal transfer (Div. A sec. 110) + $93.2B mandatory expansion |
| Expansion vs renewal in ARCA | — | 37% / 63%: $93.20B (secs. 303, 310, 311, 312) vs $160.83B |
| 2031 bill total FY2031-35 | — | $898.3B: highways and safety $419.85B, transit $224.42B, rail $254.03B |

The old 0.105/0.099/0.019/0.001 rows can still be reproduced by ARCA's own method (0.111/0.098/0.019/0.002). But that method freezes highways and transit at CBO baseline outlays, skips fuel-tax displacement, and counts no continuing general-fund appropriations for them, even though the cap's numerator counts them. Retire it or label it.

## 4. Edits to make in the ARCA doc

1. **Rewrite Title I to point to Division A.**
   - Delete the standalone rail trust fund text, the 8/15/22/28% rail share of all receipts, the $132B transfer and the proportional trigger.
   - Replace them with a short summary of Division A sections 101–111 and the cross-references above.
   - Keep ARCA's sections 102–104 revenue provisions (aviation segment fee, rail diesel tax, corridor surcharge) as Division A section 104, credited to the rail account outside the three-way split.
2. **Pick one aviation fee schedule.** ARCA's reconciliation section raises a fee "$4 to $9" in 2030 and steps it to $12. Its envelope section starts a surcharge at $4 in FY2031. The model uses $4 in FY2031 rising to $12 in FY2035, capped at $16 by FY2045. Reconciliation package two uses a 10/5-cent diesel tax; the 2031 bill raises it to 15/7.5 cents. Make every section agree.
3. **Correct the title tables to the canonical table.** The canonical table governs: sec. 203 $4.70B (title table says $5.90B), sec. 205 $4.15B (says $6.65B), sec. 303 $55.00B (says $40.00B). Canonical by year: $39.95B, $47.29B, $52.07B, $56.13B, $58.59B = $254.03B, plus up to $25B readiness reserve.
4. **Fix the Byrd table** (decision 11).
5. **Restate the affordability and fiscal sections** with the section 3 numbers.
   - Call 0.206% a benchmark.
   - Add the CBO-basis line.
   - Drop the claim that rail becomes self-financing. No surface account does: FY2041-45 dedicated receipts are about $141B a year against $220B of programs.
6. **Retire the parity-envelope ratio (2.27).** Against an envelope of 75% of highways, rail's share would make ARCA 3.1 times its allotment. That is an artifact of the envelope. Keep parity as a policy statement; the binding test is renewal covered, the general-fund benchmark, and expansion giving first.
7. **Section 310 terminals ($20.20B).** Restate under the joint-facility rule. Transit's share is set project by project; ATRA section 606 carries $6.0B as a planning figure. Each terminal needs scoping (open item).
8. **Section 302 formula and the section 310 project list.** Redraft under the new joint-facility rule. Titles V–IX statutory text is still to draft.
9. **250-Plus section.**
   - Relabel the rail table: "H.R. 8870 as written: authorized, none guaranteed"; "250-Plus: authorized"; "250-Plus: of which guaranteed (Senate trade)"; "Delivered (assumed rate on the unguaranteed rest)."
   - Under the table, note that H.R. 8870 guarantees nothing for rail ($62.4B of authorizations). 250-Plus raises that to about $73.3B and guarantees $22.0B (30%): NEC $6.0B, National Network $10.0B, Partnership Program $6.0B. Delivered is about $60B.
   - Remove the Corridor ID sunset concession.
10. **RRIF text** (section 2 above).
11. **Reconciliation rail titles.** Keep the amounts: package one $35.0B, package two $13.5B, $48.5B in all. Add obligation and expenditure deadlines to each capital line, and send both instructions to Finance and Ways and Means as well as Commerce. Lines:
    - **Package one:** RRIF credit risk premium $6.0B; electrification and trainsets $9.0B; state of good repair $8.0B; long-distance fleet $5.5B; Corridor ID $3.5B; station ADA $3.0B.
    - **Package two:** RRIF $4.0B; grade crossings $4.0B; electrification $3.0B; workforce $2.5B.
12. **Section 106(e) readiness reserve.** State that it sits under the section 108 trigger and is released on gate clearance. It fits at $5B a year in FY2031-35 with $1.9B–6.2B to spare against the benchmark.

## 5. Open items still on the table

- Division A sections 102–104, 106, 107, 110 and 111 in statutory text (101, 108 and 109 are drafted in the ATRA doc).
- Section 111 per-mile administration: Treasury collection, a bar on location data (odometer reads only), a state collection-agreement option and a 10% cost allowance. This is the provision most likely to decide whether the fee survives.
- Scope the five terminals and set transit/rail shares project by project. Washington Union Station's commuter figures are unverified; Atlanta has no intercity terminal yet.
- Decide whether to count H.R. 8870's $26B of general-fund grants (Bridge Investment Program, multimodal freight, National Infrastructure Grants) against the benchmark.
- A CBO-style score of Divisions A and B.
