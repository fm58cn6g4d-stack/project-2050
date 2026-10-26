# ATRA merge contribution — state of the transit side and the shared divisions, for the 2031 merge

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/atra-merge-contribution.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Written 2026-10-12 by the ATRA session, for the merge session. This session's own work exists in four places; nothing else from it survives:

- this file;
- the ATRA doc (artifact `6eded0d5-40fc-433a-b940-8d8ca015f581`, rev 159);
- the package section-by-section (artifact `fb14029c-152b-4727-9ae3-b2f055c8b6f7`, rev ~104);
- `index/tools/transportation/transit_fiscal_model.py`.

> **Calendar update (later on 2026-10-12):** the 2031 bill now covers **FY2032-36**, not FY2031-35. Its working title is the **Moving America Act of 2031**. `sources/transportation-calendar-fy2032-36.md` holds the decision, the conventions and the full restated figure set. This file has been restated to match; where any older doc says FY2031-35, read FY2032-36 and take the figures from the calendar file.

I read `sources/transportation-arca-status-oct12.md` (ARCA rev 309) before writing. Where this file contradicts it, the contradiction is marked **[vs ARCA]**.

Every figure here comes from a run of `index/tools/transportation/transit_fiscal_model.py` as saved alongside this file. The base case is architecture C, scenario B, with NHTSA/FMCSA included. Rerun the model rather than trusting the prose.

---

## 0. Read this first — three things the documents won't tell you

1. **FY2031 was authorized twice — now resolved.** 250-Plus covers FY2027-31, and the 2031 bill now covers **FY2032-36** (Espen, Oct 12). Conventions are in `sources/transportation-calendar-fy2032-36.md`:
   - program tables keep their nominal amounts, one year later (~2.5% real cut, flagged);
   - FY2031 is a 250-Plus year for every mode;
   - aviation and diesel schedules shift a year;
   - the per-mile schedule is unchanged.

   Two consequences the merge must carry:
   - **The FY2031 cliff.** Rail drops from ~$37B to $13.3B and transit from $40.2B to $20.7B, with $48B of benchmark room that year. Recommendation: extend the 2030 reconciliation package's availability through FY2031.
   - **The 250-Plus transfer stays at $108.0B** (through FY2030), under Espen's 2026-bill discipline rule: nothing in 250-Plus is sized to anything in these documents. See `sources/transportation-arca-status-oct12.md`.
2. **How the highway division defines "renewal" moves the incremental shares more than anything else left open.** Division A sec. 101(f) defines renewal for transit and rail, but not for highways. The model treats the whole highway program as renewal. Each 5% of the highway program classed as expansion lowers highways' equal-coverage share by about 3.3 points:
   - 100% renewal: 34.7 / 53.7 / 11.6;
   - 95% renewal: 31.4 / 55.8 / 12.8;
   - 90% renewal: 27.9 / 58.0 / 14.1.

   The 35 / 50 / 15 split was settled by Espen against the 100%-renewal answer. If division B calls capacity grants expansion (as the package doc's sec. 1105 proposes), the drafted shares drift further from the rule they are meant to follow.
3. **The 0.206% figure is a benchmark in prose but a trigger in drafted statute.** Espen decided on Oct 12 that the 0.206% is the project's own rule, not CBO's or statute's, and they are fine exceeding it. But drafted sec. 108(b) still makes 0.206% a hard trigger that cuts expansion obligations.
   - On the FY2032-36 calendar no scenario reaches it in the bill years: B peaks at 0.177%, C at 0.193%. But FY2030 (0.197%) and a light-duty-only fee (0.209% in FY2030) come close or over.
   - The merged doc must still decide whether sec. 108(b) keeps a number (and which), or becomes report-and-recommend.

---

## 1. The highway division

### Status

The highway division was **never drafted.** It exists only as a proposed section-by-section in the package doc (Division B). It is sized from the model's highway line and marked "proposed framework." No statutory text exists. The project has read H.R. 8870's highway title only in summary (APTA's table, CBO's estimate, secondary trackers), never the conference text.

### Recommendation: hybrid

Incorporate H.R. 8870's title I, as enacted in 250-Plus, by reference: its program structure, apportionment formulas and set-asides. Then draft only the amendments the shared trust fund requires.

- A drafted highway title is a 300-page job the project has no basis for.
- Incorporation alone leaves three things undone that the other divisions depend on:
  - the renewal/expansion definition for sec. 101(f);
  - the FY2032-36 authorization levels;
  - the per-mile coordination with States.
- So: one title of about eleven sections amending title 23, with H.R. 8870 doing the rest. Say so plainly in the division's lead paragraph.

### Division letters

Use the letters the package doc already uses. The ATRA and ARCA docs both cross-reference them. The six divisions are:

- **A** — Surface Transportation Trust Fund and Revenue (Ways and Means; Finance);
- **B** — Federal-Aid Highways and Highway Safety (T&I; EPW, Commerce);
- **C** — Public Transportation, the American Transit Renewal Act (T&I; Banking);
- **D** — Intercity Passenger Rail, the American Rail Competitiveness Act (T&I; Commerce). This matches arca-status;
- **E** — Research, Data and Project Delivery: about $1.0B, outside the model, mostly proposed; it closes the permitting gaps the paired 2026 permitting act left;
- **F** — Budget Discipline and General Provisions.

### Authorization levels (model; FY2031 is 250-Plus at H.R. 8870's level; the bill continues it at +2.5% a year from FY2032)

| $B | FY2032 | FY2033 | FY2034 | FY2035 | FY2036 | Total |
| --- | --- | --- | --- | --- | --- | --- |
| FHWA | 79.58 | 81.57 | 83.60 | 85.69 | 87.84 | 418.28 |
| NHTSA + FMCSA | 2.30 | 2.35 | 2.41 | 2.47 | 2.53 | 12.07 |
| Division B total | 81.87 | 83.92 | 86.02 | 88.17 | 90.37 | **430.35** |

- H.R. 8870 (250-Plus) is $72.9B (FY2027) to $77.6B (FY2031) for FHWA: the sec. 1102 limitation plus $0.639B a year exempt.
- Division B continues it at 2.5% a year from FY2032. The 2.5% is ARCA's inflation assumption, used as a placeholder, not a sizing.

### NHTSA and FMCSA

- They are paid from the Highway Account, and the model folds them into the account's need (decided Oct 12).
- The figure is derived, not read from H.R. 8870: CBO's total obligation limitation ($470.7B FY2027-31, Table 5) minus FHWA's limitation minus FTA's contract authority. That gives $2.04B (FY2027) rising to $2.24B (FY2031), then $2.30-2.53B a year in FY2032-36.
- The split between NHTSA and FMCSA is unknown. Get it from H.R. 8870 titles IV and V.

### Proposed sections (package doc Division B; none drafted)

| Sec. | Provision | FY2032-36 | Basis |
| --- | --- | --- | --- |
| 1101 | Authorizations and obligation limitation from the Highway Account | $418.3B FHWA | Model's highway line |
| 1102 | Apportioned formula programs (NHPP, STBG, HSIP, CMAQ, freight, metropolitan planning) at H.R. 8870 shares | ~$328.1B | H.R. 8870 sec. 1101(a)(1), $60.9B in FY2031, grown from FY2032 |
| 1103 | Bridge formula program | ~$49.6B | H.R. 8870 $9.2B a year, grown |
| 1104 | Federal lands and tribal, emergency relief, TIFIA, administration, discretionary capacity grants | ~$40.6B | Residual |
| 1105 | **Highway renewal programs defined for div. A sec. 101(f)**: apportioned formula programs and bridge are renewal; discretionary capacity grants are expansion | policy | **The hole in sec. 101(f)** — see §0.2 |
| 1106 | Fix-it-first: a State below its own NHPP pavement or bridge target for two reporting periods applies a rising share of NHPP to preservation | policy | Parallel to ATRA 5326(e), no withholding |
| 1107 | STBG/CMAQ flex to chapter 53 and intercity rail capital as of right; STBG usable for a State's share of a joint facility under div. A sec. 109 | policy | Continues 23 U.S.C. 104(f), 133 |
| 1108 | Per-mile coordination: States may collect the div. A sec. 102 charge with a state road-user charge under one account; Treasury reimburses collection cost | policy | Ties to div. A sec. 111 |
| 1109 | Vulnerable road user HSIP set-aside, continued and indexed | policy | IIJA special rule |
| 1110 | PROTECT resilience as an NHPP set-aside | within 1102 | Continues IIJA |
| 1111 | Unit-cost and delivery reporting, projects over $100M, same database as transit and rail | policy | Mirrors ARCA 705, ATRA 705 |
| 1112 | H.R. 8870 general-fund grants subject to appropriation: Bridge Investment Program $2B/yr, multimodal freight $1.2B/yr, National Infrastructure Grants $2B/yr (sec. 7105) | ~$28.0B authorized FY2032-36 (grown) | Outside the fund and the model; **benchmark question open** |
| 1201 | NHTSA: highway safety programs, sec. 402, vehicle safety | ~$12.1B with FMCSA | CBO limitation residual |
| 1301 | FMCSA: MCSAP and operations | in 1201 figure | — |

### Renewal vs expansion for div. A secs. 107 and 108

- **The model counts the entire highway program, safety included, as renewal.** Nothing in the highway account is cut first under sec. 108, and all of it continues under sec. 107.
- Sec. 1105 proposes treating discretionary capacity grants as expansion, but no figure was ever put on them. I don't know what share of the ~$40.6B in sec. 1104 is capacity grants.
- The merge session should pick a dollar figure, then rerun `solve_incremental_shares()` with `highway_need` scaled accordingly (§0.2).

### Not scoped

- Apportionment formula changes.
- NHPP/STBG sub-allocation.
- Any highway policy beyond sections 1105-1111.
- Tolling and Interstate System reconstruction.
- Freight (beyond carrying H.R. 8870).
- Federal lands.
- Emergency relief reform.
- TIFIA terms. ARCA has RRIF terms; TIFIA has none.
- NHTSA and FMCSA policy.
- Highway-side Buy America.
- Workforce.
- Whether the $26B of sec. 1112 counts against the benchmark (it is $5.2-5.7B a year against $12.4-16.6B of room in FY2032-36).

---

## 2. Division A

### Drafted (ATRA doc, "Drafted text: sections 101, 108 and 109"), verbatim

```
SEC. 101. SURFACE TRANSPORTATION TRUST FUND.

(a) REDESIGNATION.—Section 9503 of the Internal Revenue Code of 1986 is
amended by striking "Highway Trust Fund" each place it appears and inserting
"Surface Transportation Trust Fund".

(b) ACCOUNTS.—The Fund shall consist of a Highway Account, the Mass Transit
Account established by section 9503(e), and an Intercity Passenger Rail
Account.

(c) BASE AMOUNTS.—For fiscal year 2029 and each fiscal year thereafter there
shall be credited to the Highway Account and to the Mass Transit Account,
before any amount is credited under subsection (d), an amount equal to the
amount credited to that account for fiscal year 2028, increased by the
percentage change in the Consumer Price Index for All Urban Consumers since
fiscal year 2028. If receipts are less than the sum of the two base amounts,
each account shall be credited in proportion to its base amount.

(d) NEW REVENUE.—Of amounts credited to the Fund for a fiscal year in excess
of the base amounts under subsection (c)—
  (1) 35 percent shall be credited to the Highway Account;
  (2) 50 percent shall be credited to the Mass Transit Account; and
  (3) 15 percent shall be credited to the Intercity Passenger Rail Account.

(e) RAIL-SPECIFIC RECEIPTS.—Taxes received under sections 4283 and
4041(a)(1)(C)(iii) shall be credited to the Intercity Passenger Rail Account
and shall not be taken into account under subsection (c) or (d).

(f) RENEWAL FIRST.—Amounts in an account shall be available for the
expansion programs of that account only to the extent they exceed the amounts
made available for that fiscal year for its renewal programs. For purposes of
this Act—
  (1) the renewal programs of the Mass Transit Account are those under
  sections 5305, 5307, 5310, 5311, 5312, 5314, 5324, 5326, 5329, 5337, 5339
  and 5340 of title 49, United States Code;
  (2) the renewal programs of the Intercity Passenger Rail Account are those
  under titles II, IV through VII and X of the American Rail Competitiveness
  Act and sections 302, 304, 305 and 306 of that Act; and
  (3) the expansion programs are those under section 5309 of title 49,
  section 606 of this Act, and sections 303, 310, 311 and 312 of the American
  Rail Competitiveness Act.

(g) MASS TRANSIT ACCOUNT EXPENDITURES.—Section 9503(e)(3) of such Code is
amended by striking "capital or capital related expenditures (including
capital expenditures for new projects)" and inserting "expenditures
authorized under chapter 53 of title 49, United States Code".

(h) RESETTING THE SHARES.—Not later than 18 months before the expiration of
each authorization, the Secretary of the Treasury and the Secretary of
Transportation shall report to the Committees the percentages under
subsection (d) that would result in dedicated receipts covering an equal
share of the renewal programs of each account over the following 10 fiscal
years.

SEC. 108. SOLVENCY AND GENERAL FUND DISCIPLINE.

(a) REPORT.—The Secretary and the Director of the Congressional Budget
Office shall jointly report each year the amount by which obligations for
all programs of the three accounts and for programs under section 105 are
projected to exceed receipts credited to the Fund, as a percentage of gross
domestic product.

(b) TRIGGER.—If that percentage is projected to exceed 0.206 percent for a
fiscal year, the Secretary shall reduce amounts available for obligation for
that fiscal year for the expansion programs described in section 101(f)(3),
in proportion to the amounts otherwise available for each, by the amount of
the excess.

(c) RENEWAL PROTECTED.—No reduction under this section or by reason of a
projected shortfall in an account shall be made to a renewal program until
amounts available for the expansion programs of that account have been
reduced to zero.

(d) EXECUTED AGREEMENTS.—A reduction under this section shall not apply to
an amount obligated under a full funding grant agreement or a contingent
commitment executed before the date of the report.

SEC. 109. JOINT FACILITIES.

Amounts in the Mass Transit Account and the Intercity Passenger Rail Account
may be obligated for a facility used by both public transportation and
intercity passenger rail transportation, each in proportion to—
  (1) for the rehabilitation or replacement of an existing facility, the
  share of train movements at the facility in the most recent fiscal year
  made by the services that account supports; and
  (2) for an expansion of the capacity of a facility, the share of the
  additional train movements the project is projected to make possible
  that will be made by those services,
as determined by the Secretary using the method of section 5309(q)(4) of
title 49, United States Code.
```

**Defects in the drafted text that the merge must fix:**

- **101(f)(2) title references are stale [vs ARCA].** ARCA now has thirteen titles, and the package doc classes D-IV through D-XIII as renewal. Replace with "titles II and IV through XIII of division D, and sections 302, 304, 305 and 306 of division D." The model already assumes this: rail renewal is everything except secs. 303, 310, 311 and 312, which is $160.83B.
- **101(f) has no highway paragraph.** Add a (4) that cross-references div. B sec. 1105. Without it, sec. 108(c)'s order of cuts is undefined for the Highway Account.
- **101(f)(3) and 108 must name the merged sections.** "Section 606 of this Act" becomes "section 606 of division C," and "sections 303… of the American Rail Competitiveness Act" becomes "…of division D."
- **101(e):** the IRC section numbers for the aviation surcharge (4283) and the rail diesel tax are carried from ARCA's draft. They have not been checked against the Code.
- **108(b):** see §0.3. The number is a policy choice now, not a constraint.

### The other sections

| Sec. | Status | What exists and where |
| --- | --- | --- |
| 102 Per-mile road user charge | **Not drafted.** Specified only | 1.0¢ in FY2029, +0.2¢ a year, 3.6¢ in FY2042; all vehicle-miles; nominal cents (not indexed). Fuel taxes phased down linearly over FY2029-42, ending the year the fee reaches 3.6¢. New IRC chapter needed |
| 103 Fuel taxes and EV fee | **Not drafted** | Fuel taxes extended past Sept 30, 2028 and indexed during the phase-down. EV/PHEV fee $130/$35, +$5 a year to $200 (ARCA's Choice 2). H.R. 8870 sec. 1129's Sept 30, 2036 expiry (the bill's last day) struck, and receipts credited to the fund (H.R. 8870 sends them to the general fund; the 2029 package moves them). Espen plans a larger EV redesign later; treat 103 as provisional |
| 104 Rail-specific taxes | ARCA doc has text for ARCA secs. 102-104; check there | Aviation segment surcharge $4 FY2032 → $12 FY2036, capped at $16 by FY2046; rail diesel 15¢/7.5¢ from FY2032 (10¢/5¢ for FY2030-31 from the 2030 package); corridor surcharge $12 on city pairs with a funded corridor. All credited to the rail account outside the split (101(e)) |
| 105 General-fund programs | **Not drafted.** Specified | Mandatory appropriations, FY2032-36: CIG sec. 401 $27.50B, sec. 606 $6.00B, ARCA secs. 303/310/311/312 $93.20B; $126.7B in all. Full obligation on execution requires amending 49 U.S.C. 5338(d)(2) — **non-tradeable** |
| 106 Contract authority and contingent commitments | ARCA SEC. 106 drafted in ARCA doc; extend to all three accounts | Contract authority on enactment for every account; contingent commitments to FY2046 capped at 60% of a year's authorization; ARCA's $25B readiness reserve (106(e), now with a 30% design threshold per arca-status) subject to sec. 108 |
| 107 Continuation | ARCA rewrote its sec. 107 statute (arca-status); adopt that text for all three accounts | Each account's renewal programs continue at FY2036 levels, indexed, if reauthorization lapses. Rail renewal is $37.1B in FY2036 |
| 110 Renewal-shortfall transfers | **Not started** | General-fund transfers equal to each account's projected renewal shortfall: highways $114.1B (safety included), transit $43.7B, rail $92.6B; $250.4B over FY2032-36. The IIJA precedent; not reconciliation-eligible. Draft on the IIJA model: a single appropriation to each account, in a fixed sum by account |
| 111 Per-mile administration | **Not started.** Position below | — |

### Section 111: position, not yet statutory text

The fee's political risk is surveillance, not price. At 3.6¢ the fee is about $48 a year above ARCA's schedule for a car driven 12,000 miles. Section 111 should make the following points in so many words.

1. **Base: odometer only.** The charge is computed from the difference between two odometer readings. No other information about a vehicle's movement may be collected, required or retained. Location, route, time-of-day and trip data are barred outright, including data offered voluntarily through a private vendor, for purposes of this section. No device may be required.
2. **Collection: Treasury, through the States.** The charge is a federal excise imposed on the registered owner and payable annually.
   - Default collection is at State registration renewal, with the odometer read at registration or inspection.
   - A State that signs a collection agreement collects and remits, keeping an administrative allowance.
   - In a State that declines, Treasury collects directly on a self-reported, verified reading.
   - Use H.R. 8870 sec. 1129's EV-fee machinery as the template: 99% remitted, 1% kept, 125% withholding of apportionments for non-remittance from FY2028. That machinery passed T&I 62-2.
3. **Commercial vehicles.** Heavy vehicles report mileage through the International Fuel Tax Agreement and the HVUT (Form 2290) channel they already use. No new collection system for carriers.
4. **Cost allowance.** Up to 10% of collections may cover collection costs, including payments to States. That is the model's `PER_MILE_ADMIN = 0.10` (ARCA cites 5-13%).
   - At 13%, peaks rise to 0.201% (FY2030) and 0.182% (FY2032-36).
   - The allowance should be a ceiling, reviewed by GAO after three years.
5. **Data rules.**
   - Readings are kept no longer than needed to verify payment (three years).
   - Readings are exempt from disclosure and unavailable to law enforcement without a warrant.
   - No sale or sharing of readings.
   - Private right of action for violations.
6. **No State duplication.** The federal charge is national and flat, so no interstate apportionment is needed. Div. B sec. 1108 lets a State run its own road-user charge in the same account.

---

## 3. Decisions made in discussion, beyond `sources/transportation-transit-package-status-oct12.md`

The status doc (rewritten Oct 12, after the CBO pass) carries most decisions. These are the ones it lacks or states without reasoning:

- **The 2031 bill covers FY2032-36; working title the Moving America Act of 2031** (Espen, after this file's first version flagged the double-authorized FY2031). Full conventions and figures are in `sources/transportation-calendar-fy2032-36.md`.
- **Recs accepted by Espen** (Oct 12):
  - hybrid highway division with all of division B treated as renewal except sec. 1112;
  - scenario B;
  - sec. 310 as the single terminal program, with sec. 606 retargeted outside the five nodes at $3.0B.

- **Corridor ID sunset concession dropped from 250-Plus.**
  - Espen thought it unlikely and not worth trading for.
  - Division D makes Corridor ID permanent, and an extension act can move the October 1, 2031 date if the 2031 bill slips. That is cheaper than spending Senate trade capital on it.
  - Removed from the package doc; arca-status confirms the ARCA side.
- **250-Plus rail and transit tables now distinguish what is written from what is guaranteed** (Espen's comment). Rail:
  - H.R. 8870 as written guarantees nothing ($62.4B, all subject to appropriation).
  - 250-Plus authorizes about $73.3B and guarantees $22.0B (30%) through the Senate trade: NEC $6.0B, National Network $10.0B, Partnership $6.0B. Delivered is about $60B.

  Transit runs the other way:
  - $87.6B of contract authority is guaranteed as written.
  - The deal adds only $5.0B of the $15.0B CIG authorization.
- **The 0.206% is the project's benchmark, and exceeding it is acceptable** (Espen). Its origin: ARCA's own 0.192% rule (the FY2026 general-fund draw on surface programs), restated to count annual appropriations.
  - What binds Congress is the size of the reconciliation instructions, PAYGO and the Byrd rule.
  - Instructions must be sized to CBO's net-of-offset score: new excise receipts less about 25% for income and payroll taxes. That score is $56.3B more than the transfer measure over FY2032-36.
- **NHTSA/FMCSA folded into the Highway Account's need** (Espen). This raised every draw about 0.005-0.006 points and the bill total to $898.3B (now $908.8B on the FY2032-36 calendar).
- **35 / 50 / 15 kept** (Espen). The transit gap (renewal coverage now 73 / 70 / 79 on FY2032-36) waits for the EV redesign.
  - I had recommended 33 / 53 / 14 after the CBO EV recalibration, then withdrew the recommendation when Espen said the EV fee will be redesigned.
  - **Reopen it only if the highway renewal definition moves the solve** (§0.2).
- **250-Plus transfer: two accounts, $108.0B** ($71.2B highway, $36.8B transit), sized to CBO's cumulative shortfall through FY2030.
  - This replaced a ~$53B transit-only transfer, which would have left the highway account dry in FY2028 and lost the highway votes.
  - Reconciliation can't make the transfer later.
- **Changed my mind:**
  - **Joint terminals.** ATRA had a 30% transit share for terminals; it is now the train-movement rule (sec. 109). The 30% was wrong by any measure of use.
  - **Operating-tier state floor.** The 0.5% state floor was replaced by a 25%-of-net-operating-cost ceiling. The floor moved $344M a year to 18 States and gave Boise $30M against $1M of net cost.
  - **Fee start.** It moved from 0.6¢ to 1.0¢ because of House highway levels, not ARCA's anchor.

---

## 4. Current numbers

### ATRA canonical authorization table, FY2032-36 (scenario B; nominal amounts as drafted, carried one year later; R = renewal, X = expansion; TF = Mass Transit Account, GF = mandatory general fund)

| Sec. | Program | | | FY32 | FY33 | FY34 | FY35 | FY36 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 201 | Service operating assistance (new 5307(i)) | R | TF | 6.00 | 6.50 | 7.00 | 7.50 | 8.00 | 35.00 |
| 301 | State of good repair formula (5337) | R | TF | 5.20 | 5.40 | 5.60 | 5.80 | 6.00 | 28.00 |
| 302 | Backlog retirement schedule (new 5337(g)) | R | TF | 6.00 | 6.15 | 6.30 | 6.46 | 6.62 | 31.53 |
| 303 | Asset management enforcement (5326) | R | TF | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.50 |
| 304 | Transit resilience | R | TF | 0.60 | 0.60 | 0.60 | 0.60 | 0.60 | 3.00 |
| 401 | Capital Investment Grants (5309) | X | GF | 4.50 | 5.00 | 5.50 | 6.00 | 6.50 | 27.50 |
| 501 | Workforce | R | TF | 0.50 | 0.55 | 0.60 | 0.60 | 0.60 | 2.85 |
| 601 | Urbanized area formula, capital (5307, 5340) | R | TF | 10.00 | 10.40 | 10.80 | 11.20 | 11.70 | 54.10 |
| 602 | Buses and bus facilities (5339) | R | TF | 2.60 | 2.70 | 2.80 | 2.90 | 3.00 | 14.00 |
| 603 | Rural, tribal, intercity bus (5311) | R | TF | 1.40 | 1.45 | 1.50 | 1.55 | 1.60 | 7.50 |
| 604 | Seniors and people with disabilities (5310) | R | TF | 0.60 | 0.62 | 0.64 | 0.66 | 0.68 | 3.20 |
| 605 | All Stations Accessibility | R | TF | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 5.00 |
| 606 | Joint transit-rail facilities | X | GF | 1.00 | 1.20 | 1.40 | 1.40 | 1.00 | 6.00 |
| 607 | Ferries | R | TF | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 1.00 |
| 608 | Emergency relief, quick release (5324) | R | TF | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.50 |
| 701 | Planning, research, safety, FTA capacity | R | TF | 0.90 | 0.92 | 0.95 | 0.97 | 1.00 | 4.74 |
| | **Total** | | | **40.70** | **42.89** | **45.09** | **47.04** | **48.70** | **224.42** |

- Renewal is $190.92B and expansion $33.50B.
- Scenario A (no operating tier) totals $189.42B; scenario C (tier doubled) totals $259.42B.
- Title totals: I (shared, no money), II $35.00B, III $63.03B, IV $27.50B, V $2.85B, VI $91.30B, VII $4.74B.

### Reconciliation, transit ($32.0B)

| Line | Authority | FY2029 | FY2030 |
| --- | --- | --- | --- |
| Operating transition grants (MOE at 3-year average; service hours ≥95% of base) | 5307 | 4.00 | 5.00 |
| State of good repair, shovel-ready backlog | 5337 | 4.00 | 6.00 |
| Bus and railcar replacement (firm orders) | 5339, 5337 | 3.00 | 1.00 |
| Station accessibility (rail transit and commuter stations) | 5337, ASAP | — | 3.00 |
| CIG, executed agreements plus projects signing by the obligation deadline | 5309 | — | 3.00 |
| Credit subsidy, transit and joint development | TIFIA | 1.00 | 1.00 |
| Workforce and FTA capacity | 5314, admin | — | 1.00 |
| **Total** | | **12.00** | **20.00** |

- Every capital line carries obligation and expenditure deadlines (Byrd).
- Rail is $48.5B ($35.0B package one, $13.5B package two); see arca-status.

### 250-Plus transit baseline, FY2027-31 (FY2031 is now 250-Plus's year, not the bill's: transit $20.71B)

| Line | Authorized | Guaranteed | Delivered |
| --- | --- | --- | --- |
| Mass Transit Account contract authority, sec. 3023 (16.868 / 17.205 / 17.527 / 17.835 / 18.157) | $87.6B | all | $87.6B |
| CIG, sec. 3007 | $15.0B | $5.0B (Senate trade) | $12.0B (rest at 70%) |
| WMATA, sec. 3109 | $0.15B, FY2031 only (CBO) | none | $0.15B |
| **Total** | **$102.8B** | **$92.6B (90%)** | **$99.8B** |

- That is about 8% below IIJA nominal and 18% below real.
- Proposed additions to the vehicle: annual reporting of capital used on operations; a two-account transfer of **$108.0B** ($71.2B highway + $36.8B transit, CBO's shortfall through FY2030). Under the 2026-bill discipline rule it is not grown to cover FY2031; restoring the 5337(f) railcar program ($1.5B) as the trade for the fare-evasion condition.

### Model status

- `index/tools/transportation/transit_fiscal_model.py` in the project is current as of this file. I corrected two stale print/assumption labels (WMATA 0.75 → 0.15; the 0.8¢ note) and saved it with this file.
- Changes on Oct 12:
  - the CBO calibration (`EV_CBO`, WMATA, `CBO_OL`);
  - `safety_program()` and `highway_need()` with `INCLUDE_SAFETY = True`;
  - section 9h (excise-offset basis) and section 9i (safety on/off);
  - the benchmark note at `CAP_ALL_IN`.
- Run `python3 transit_fiscal_model.py` for every table; `--json` writes `transit_model_output.json`.

Key outputs, scenario B, on the FY2032-36 calendar (`BILL_START = 2032`; `calendar(2031)` reproduces the old framing):

- **Draw:**
  - FY2029-31: 0.154% (FY2029 0.190%, FY2030 0.197%, FY2031 0.081%);
  - **FY2032-36: 0.174% (peak 0.177% FY2034)**;
  - FY2037-41: 0.123%;
  - FY2042-46: 0.123%.
- **Room:** FY2030 $3.1B; FY2031 $48.1B; FY2032-36 $12.4-16.6B a year.
- **CBO basis:** FY2030 0.219%; FY2032-36 0.193-0.203%.
- **FY2032-36:** dedicated 316.25 / 147.20 / 68.26; general fund 114.10 / 77.22 / 185.77; total program $908.80B.

---

## 5. Position on the two unresolved variables

### Shares: keep 35 / 50 / 15 in the text, conditional on division B

- Espen settled 35 / 50 / 15, and against the current solve (33.9 / 53.9 / 12.2) it is within 1-4 points.
- The rule in sec. 101(h) resets the shares each reauthorization anyway.
- **But the highway renewal definition can move the solve by more than the gap Espen accepted** (§0.2).
  - If div. B sec. 1105 puts more than about 5% of the highway program in expansion, highways' equal-coverage share falls below 31%. 35 is then hard to defend as following the rule.
  - The fix is either to keep the whole highway program as renewal (simplest, and what the model does), or to rerun and reset.
- My recommendation: **classify all of division B as renewal except sec. 1112's general-fund grants**, which are outside the fund anyway. Keep 35 / 50 / 15, and say in the doc that the shares follow the rule within 1-4 points.

### 49 U.S.C. 5307 operating eligibility: scenario B

| | Transit FY2032-36 | Split transit / rail | Draw FY2032-36 (peak) | Room FY2032-36 |
| --- | --- | --- | --- | --- |
| B (drafted) | $224.42B | 46.9 / 53.1 | 0.174% (0.177%) | $12.4-16.6B |
| C (tier doubled) | $259.42B | 50.5 / 49.5 | 0.190% (0.193%, FY2034) | ~$5B in FY2034 |

Why B (accepted by Espen on Oct 12). On the FY2032-36 calendar C now fits, so the case is policy, not fit:

1. **It is already drafted and apportioned.** Sec. 201's new 5307(i) runs $6.0B rising to $8.0B: 50% vehicle revenue hours, 30% trips, 20% low-income, a 25%-of-net-operating-cost ceiling, and maintenance-of-effort and service-floor conditions. On 2024 NTD data the first-year tier is 11.9% of national net operating cost. New York's share (27.7%) equals its share of that cost.
2. **C uses most of the margin.** It leaves about $5B a year at the FY2034 peak, which is ARCA's $25B reserve and nothing else. B leaves $7.4-11.6B a year after the reserve, and that headroom is the protection against the fee risks (light-duty-only, collection cost).
3. **Federal share.** B holds the federal share of large-system operating cost near its 2024 level (~17%) as relief money ends. C roughly doubles it, which raises the substitution risk the maintenance-of-effort (MOE) rule exists to contain.
4. **The tier is the largest tradeable dial ($4-8B a year).** Starting at B leaves room to trade down to the first fallback round ($4.0B flat) without breaking the bill. Starting at C invites a cut to B anyway.

If Espen later wants C, it fits the benchmark in FY2032-36. The cost is ARCA's reserve headroom and the fee-risk margin.

---

## 6. Open items, and contradictions with ARCA

### ATRA's own open items

- Read 49 CFR parts 625, 630 and 673 against Titles II and III.
- Get FTA to publish a national cost for legacy rail-station accessibility (sec. 605). Only system figures exist: MTA ~$35B, SEPTA $2.4B, CTA $2.1B.
- Rerun the 5307(i) apportionment with FTA's multi-area splits; agencies are currently assigned wholly to their primary urbanized area.
- Check H.R. 8870 sec. 3023 against enrolled text (APTA table plus a quotation of sec. 3023 only).
- The 49 U.S.C. 5338(a)(2) lettering may change under H.R. 8870. Cite programs by name, not letter (conforming secs. 711-716).
- Fix the WMATA sentence in the ATRA doc's 250-Plus note, which got absorbed into a source link.
- Unverified pipeline facts: Red Line Extension 2030 opening; Honolulu $10.08B and Mar 2031 vs Apr 2032; IndyGo cost; Red-Blue Connector; RPM next phases.

### Contradictions and double counts with ARCA

| # | Issue | ARCA | ATRA | Recommendation |
| --- | --- | --- | --- | --- |
| 1 | **Joint terminals — double count** | Sec. 310 $20.20B for five nodes: Chicago $9.0B, NY Penn/Sunnyside $4.0B, Washington $3.5B, LA $0.7B, Atlanta $3.0B | Sec. 606 $6.0B "for transit's share" of the same nodes | See below |
| 2 | Rail renewal titles in 101(f)(2) | Thirteen titles; D-IV to XIII renewal | 101(f)(2) says "titles II, IV through VII and X" | Rewrite to "II and IV through XIII of division D" |
| 3 | Highway renewal undefined | — | 101(f) has no highway paragraph | Add (4) → div. B sec. 1105 |
| 4 | 108(b) trigger at 0.206% | Treats 0.206% as a benchmark (rev 309) | Statute still a hard trigger | Decide: keep a number, change it, or report-only. No bill year reaches it on the FY2032-36 calendar; FY2030 is the tight year |
| 5 | Station accessibility in reconciliation | $3.0B "station access and ADA backlog" (Amtrak-served) | $3.0B rail transit and commuter stations | Not a double count if the classes are named; name them in both lines |
| 6 | NEC access charges | Sec. 1103 adds a repair component to charges eight commuter authorities pay | Operating tier and 5337(g) backlog | The added charge is an eligible 5337(g) backlog cost where the asset is in the baseline; one sentence in each division (and 49 U.S.C. 24905(c)) |
| 7 | Buy America on jointly funded equipment | Sec. 704 moves rail to 75%; sec. 1201 pool, one standard | 5323(j) >70% domestic content plus US final assembly | ATRA sec. 706: the pool's standard governs jointly funded orders; 5323(j) untouched otherwise. The rail Buy America provisions (22905(a), 24305(f)) were quoted from ARCA and **not re-read** |
| 8 | Rail account creation date | Fiscal-envelope section: 2028; reconciliation section: 2030 (as of ATRA's last read) | Model: rail credited from FY2029 under architecture C | Confirm ARCA rev 309 fixed this; if not, FY2029 (the 2029 revenue title) |
| 9 | FY2031 overlap | — | — | **Resolved:** bill is FY2032-36 (`sources/transportation-calendar-fy2032-36.md`); ARCA chat applying it |
| 10 | Trust-fund cash-flow model | Still $185.43B, standalone fund, $143.0B/$132B transfer (arca-status) | ATRA has none of its own; the model is a budget-authority model, not cash-flow | Superseded; the merged doc has no cash-flow model until one is rebuilt on $898.3B |

**Joint terminals: arithmetic and recommendation.** The sec. 109 rule, applied to renewal of the four existing terminals with use shares as the proxy (79% Chicago movements; 92% NY riders; 45,000 of 61,500 at Washington; 20,000 of 22,900 at LA), puts about **$14.0B of ARCA's $17.2B existing-terminal work** on the transit account. That is if all of it is renewal.

- Expansion is attributed by *added* movements, which will skew intercity at Chicago, Washington and Atlanta. So the true transit share lies between roughly $3B and $14B, depending on each project's scope.
- Atlanta's $3.0B has no transit share to compute; there is no intercity terminal yet.

Recommendation:

- **One program for the five nodes, not two.** Sec. 310 stays the single authorization at $20.20B. Sec. 109 decides which account books each obligation, so a transit-account share of a sec. 310 project draws on the Mass Transit Account, not on new money.
- **Retarget sec. 606** (accepted by Espen) to joint facilities outside the five sec. 310 nodes (Denver Union Station, Seattle King Street, Portland Union Station and others). Cut it to $3.0B, the first fallback round's level.
- That removes up to $6.0B of double-counted general-fund expansion and saves $3.0B of it. Rerun the model with sec. 606 at 0.6 a year.
- Flag it under "Assumptions not yet approved." The alternative is a sec. 310/606 split set project by project, which needs terminal scoping that hasn't been done.

---

## 7. Which sections survive the merge

| Section | Better base | Fold in from the other |
| --- | --- | --- |
| **Fiscal envelope** | **ATRA's "The fiscal envelope, and the trust fund architecture."** It was rebuilt on the model (three architectures, four choices, "what breaks this," the sensitivity table and the chart). Its chart widget `d23901d2-eb78` is current. The merge prompt says ARCA's is the better base; I disagree for the architecture and the draw | From ARCA: the fee-sizing table (now on the model's aviation basis per arca-status), the fit table, and the "how self-financing" restatement (now 27% FY2032-36 → 50% FY2042-46). Retire both docs' parity-envelope sections into one paragraph: parity is a policy statement, not a constraint, and ARCA's 2.27 ratio is gone |
| **Byrd analysis** | **The package doc's "What the Byrd rule allows" table.** It already covers both modes and uses the deadline rule | From each architecture doc: the mode-specific package tables. Transit's spend-out test and conditions. Rail's RRIF scoring note |
| **250-Plus baseline** | **The package doc's 250-Plus section.** One section, both modes, relabeled guaranteed vs written, CBO-checked, HTF shortfall, the $26B of general-fund grants | From ATRA: "What the House bill already does" (operating eligibility in secs. 3005/3006/3012, Streamlined Starts, the fare-evasion withholding) and the three proposed additions. From ARCA: riders carried and the RRIF changes |
| **Political path** | **ARCA's.** Coalition table, Texas line, committee map. Its coalition figures need restating to canonical (arca-status item 10) | From ATRA: "The 2027-28 positioning window" and "the forcing event, read from transit's side" (the administration's stated aim to end the Mass Transit Account in 2028); the transit coalition rows; the four non-tradeable transit provisions |
| **Fallback tiers** | **Neither alone; build one three-mode table** | ATRA's three rounds (−$30.0B / −$30.0B / −$34.4B → $194.4B / $164.4B / $130.0B; the third round is IIJA in FY2031 dollars with a three-year operating bridge). ARCA's fallback list, with sec. 107 now continuation. Highways: no fallback was ever scoped |

Also duplicated, collapse to one:

- the two "statutes both bills amend" lists. ATRA's: 26 U.S.C. 9503; 49 U.S.C. 5309(q); 5302(15) untouched; 24905(c) needs one sentence in each;
- the two "assumptions and sensitivities" sections;
- the two FY2036-reauthorization outlook sections.
