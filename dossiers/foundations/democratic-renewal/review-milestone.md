# Democratic renewal: L2/L3 milestone review

Role: the independent milestone review of the democratic renewal foundation ("a democracy and a government that work for the 21st century"; `charter/PLAN.md` 3.2 and 5, "Review"; `charter/STANDARDS.md`, "Milestone review"), stage F. The reviewer wrote none of the dossier. It tries to break the work on four fronts: weak evidence, missing populations, optimistic assumptions and cheaper alternatives. It also:
- applies the design lens (`DEC-2026-11-09-13`);
- checks the fiscal-rule report against `DEC-2026-11-10-05`;
- checks every decided item against `DEC-2026-11-17-40` to `-99`;
- checks section 9 against sections 1 to 8;
- tests the load-bearing legal claims against the texts in `library/text/`;
- reproduces section 6 from `models/tools/democratic_renewal_cost.py` and section 7's pace check from `models/tools/democratic_renewal_pace.py`.

Status: current, as of main at commit `87a14c9` (November 18, 2026, after #438). Line numbers are at that commit. Reviewer: Claude Code, `session_01UQzgBvsSQkmSMPaZW91qpt`. **This review changes nothing in the dossier.** Every fix below is a later step, sized for one session; the booking follows the fixes (`charter/STANDARDS.md`, "Milestone review").

Espen's decisions (`DEC-2026-11-17-40` to `-99`) are settled. Where a decided choice has a cost or gap the dossier does not show, this review asks Espen; it does not argue the choice. Five items are open and provisional, not defects in themselves: section 5's four fixes (D2), the voting floor's dates (D3), CAP-7's pace (D4), section 8's 13-Justice review point (D5) and INT-1.01's self-directed accounts (D1). Under `DEC-2026-11-10-07`, a clearly bounded uncertainty is not a defect.

## Verdicts

| Level | What it needs (`charter/PLAN.md` 3.2) | Verdict |
| --- | --- | --- |
| **L2, design** | Key parameters chosen (who, what, how much, who administers), with the main alternatives weighed | **Pass** (record fixes only, none blocking) |
| **L3, specified** | Provisions section by section; evidence for each load-bearing claim; a cost range validated by models with stated limits; a delivery plan | **Not yet: close.** Two blockers |

**Why L2 passes.** Thirteen memos weigh two to four options at each fork, with legacy designs as options and outside scores where any exist (CBO on H.R. 1, the Freedom to Vote Act, the JUDGES Act and the ETHICS Act). Fifty points are decided one by one. Every memo's status line says decided, with the right `DEC-` IDs. `agenda/agenda.csv` holds 120 rows for the foundation: 100 at L2 and 20 at L1, the L1 rows being the directions (DEM-3, DEM-4, DEM-9, CAP-10 and their options), the pointers and the held items. None is at L3.

**Why L3 is not yet.** Most of L3 is in place:
- 137 provisions with parameters, vehicle, agency and evidence, a groups table, a design-lens table and a consistency table (section 4);
- who runs each provision, a dated timeline, remedies, states' roles, rural delivery and four provisional fixes (section 5);
- booked rows, contingency and unbooked lines that reproduce from the tools to the decimal, apart from three small slips (section 6; "Checks run"; C-6), with the pace check's base the one real problem (F-1);
- a vote simulator, a capacity model, a hiring-pace check, objections from left, right, officials and courts, and every provision checked (section 7);
- triggers, fallbacks and hard stops (section 8).

The blockers:
1. **DEM-12.01 has no constitutional footing on the page** (L-1). Restoring federal voting rights on release from prison sets *who may vote*. The Court held in 2013 that the Elections Clause "empowers Congress to regulate how federal elections are held, but not who may vote in them" (*Arizona v. Inter Tribal Council*, `library/text/dr7-scotus-arizona-v-itca-2013.txt`:62, :557; the case the dossier itself cites for the floor, EV-DEM-359). The Fourteenth Amendment, section 2, exempts from its representation penalty a state's denial of the vote "for participation in rebellion, or other crime", which *Richardson v. Ramirez* (1974) read to permit felony disenfranchisement. The dossier names no power for DEM-12.01, lists it in no court-risk table and promises it for "any federal election held at least 180 days after enactment" (`9-public-case.md`:26; `5-delivery.md`:228). That is an unsupported claim stated as settled.
2. **The court-forum provisions send the same suit to two courts, and no one sizes the load** (L-2). A pre-enforcement challenge to a final rule goes to the D.C. Circuit within 60 days (CRT-7.01, `4-specification.md`:259). The same suit, if it seeks vacatur or other relief beyond the parties, goes to a three-judge district court with direct appeal to the Supreme Court (CRT-3.01, 3.02, :255-256), and CRT-9.01 makes "set aside" mean vacatur and sends "such cases" to those courts (:287). The plan's own laws are channelled the same way (DEM-1.13, :69). Nowhere does the dossier count the three-judge panels or the direct appeals this creates, against a Court whose docket CRT-11.02 also makes partly mandatory (:262). That is an inconsistent commitment and a missing delivery mechanism for the courts.

**What can reach L3 once those land.** Every provision can. The other findings are fixes or notes. The D4 figure (F-1) must be restated before Espen answers D4, but D4 is provisional and booking has not happened, so it does not block L3.

## How this review was done

- **Read in full.** `charter/STANDARDS.md`; the board; `charter/PLAN.md` 3.2 and 5; `dossiers/TEMPLATE.md`; `dossiers/shared-rules.md`; the README, sections 3 to 9, `provisions.json` by script, the note `notes/espen-questions-2026-11-17.md` by search; the "For the board" notes and reviews on #434 and #438; the three precedent reviews (immigration, housing, transportation).
- **Read by search.** Sections 1 and 2; memos 1 to 13 where sections 4 to 9 draw on them, and their status lines; `capacity-needs-inventory.md`; `evidence.json`; `agenda/agenda.csv`; `charter/decisions.md` rows `-40` to `-99`; the four legacy domain files.
- **Legal texts.** *Arizona v. Inter Tribal Council*, *Brnovich*, *Buckley*, *FEC v. Cruz*, *SEC v. Jarkesy*, *Crawford*, *Purcell*, *Stern*, *Wellness* and *Freytag* (`library/text/dr7-scotus-*.txt`).
- **Mechanical checks, by four Standard subagents; the reviewer spot-checked each finding used here against the files:**
  - the decided items against `DEC-2026-11-17-40` to `-99` across sections 3 to 9, `provisions.json`, the agenda rows, the README and memo status lines;
  - every number in section 9 against sections 1 to 8;
  - section 6 and section 7 part 1.3 rerun from the two tools, and the booked rows from a rebuilt budget model;
  - the legacy domain files against the dossier (where it departs without saying why).
- **New research:** one search, on the citizenship check's accuracy for naturalized citizens (M-1). The repository was checked first (`DEC-2026-11-13-15`): neither the register nor section 1 holds it.

## Checks run

**Section 6, from `democratic_renewal_cost.py`** (`python3 -B models/tools/democratic_renewal_cost.py`, plus `--json` and `--check`, which passes). The tool reads `legacy/sources/recovery-budget-audit.csv` (case `mixed`). A rebuilt budget model in a scratch copy regenerated that audit file and `models/data/recovery-budget-paths.csv` byte for byte.

| Figure | Section 6 | Reproduced | Verdict |
| --- | --- | --- | --- |
| Booked rows, FY2030-39 and FY2040 (`6-cost.md`:32, :190) | $507.2 billion; $50.0 billion | 507.18; 49.98 | Match |
| Share of the FY2040 gap (:190) | 8.3% of $602.7 billion | 8.29% of 602.69 | Match |
| Firm, and memo 10's contingency (:82, :191-192) | $434.3 billion; $0 to $72.9 billion; $0 to $4.7 billion | 434.3; 43.2 + 29.68; 4.70 | Match |
| Unbooked lines (:116-120, :193) | $19.4 billion (10.8-28.8); $2.54 billion (1.4-3.8) | 19.42 (10.81-28.79); 2.54 (1.39-3.78) | Match |
| Net of CRT-P1's room (:195) | $12.5 billion; $1.6 billion | 12.55; 1.59 | Match |
| IRS yield net of its allowance (:94, :200) | −$150 billion; −$20.5 billion | −150.0; −20.54 | Match |
| IMM-1 split, FY2036-39 (:63, :146) | −$4.3 billion | −4.30; 0.78 × 5.549 = 4.33 | Match |
| IMM-1 split, FY2040 (:63, :146) | −$0.9 billion (−0.7 to −1.05) | 78% of −1.062 is −0.83; the tool hardcodes a year shape that gives −0.90 | **Slip** (C-6) |
| DEM-1 and DEM-16 rows, FY2036 and FY2039 (:23, :25) | 1.0 and 1.1 | 1.05 and 1.175 | **Slip**: 1.1 and 1.2 (C-6); totals unaffected |

**Section 7, from `democratic_renewal_pace.py`** (`python3 -B models/tools/democratic_renewal_pace.py`, plus `--check`, which passes).

| Figure | Section 7 | Reproduced | Verdict |
| --- | --- | --- | --- |
| Booked CAP-7 by year and as a share of its run rate (`7-validation.md`:60-61) | 8.6, 17.8, 27.7, 28.7; 33%, 67%, 100% | 8.56, 17.77, 27.66, 28.71; 0.33, 0.67, 1.00 | Match |
| The review's midpoint path (:62) | 78.8 (FY2030-33); 254.6 | 78.76; 254.58 (`capacity-review/review.py`) | Match |
| Part G at the working pace (:63-64) | 227.3 (range 207.9-236.9) | 227.3 (207.9-236.9) | Match |
| Not spent in FY2030-39 (:68) | about $52 billion (42-71) | 51.9 (42.3-71.3) | Match |
| "About $22 billion (range $13-42 billion) is timing" (:69) | 22 (13-42) | 22.2 (12.6-41.6) | Arithmetic matches; **the base does not** (F-1) |
| "Every run reaches the full $32.5 billion by FY2034" (:69) | every run | The fifth-a-year runs reach full rate in FY2035 | **Wrong for three of nine runs**; FY2040 unchanged in all (C-6) |
| Net hiring needed (:71) | 13,500 a year (10,800-18,000); IRS 7,500 | the same | Match |

**Neither tool has a unit test;** each has only a `--check` mode, and the cost tool's asserts cover a few headlines, not the year-by-year rows. Both docstrings state their limits (draft scenarios; working assumptions; ranges are bounds, not probabilities), which meets L3's "stated limits".

**The decided items** (`DEC-2026-11-17-40` to `-99`). Every option and amount matches across sections 3 to 9, `provisions.json`, the agenda rows and the memo status lines, with the stale text listed in C-1 to C-4. `provisions.json` holds 137 provisions; exactly six carry a provisional element (INT-1.01, CAP-7.02, CRT-5.03, DEM-1.13, DEM-11.01, CAP-13.01), and these match section 4. The register holds 367 entries, as the README says.

## 1. The decisions, carried out

| Decision | Where | Verdict |
| --- | --- | --- |
| Memo 1 B, the records-first floor; the voter card (`-40`, `-99` a); DEM-11 at about $2 billion a year as block grant plus equipment fund (`-41`, `-94`) | DEM-1.01 to 1.15, DEM-11.01 to 11.03 | Faithful. Missing groups (M-1 to M-4); the citizenship check's legal footing (L-3) |
| Memo 2 B, severable titles; no DEM-1D (`-42`, `-43`) | DEM-1.16 to 1.19 | Faithful. The reach of *Callais* is understated for Title II and III-B (L-4) |
| Memo 3 D, the ban from enactment (`-44`, `-45`) | DEM-2.01 to 2.06 | Faithful |
| Memo 4 part 1 B, part 2 A (`-46`, `-47`) | INT-5.01, INT-15.01 | Faithful. The match's range differs between `6-cost.md`:47 ($4-12 billion) and :106 and section 9 ($4-8 billion, up to $12 billion) (C-5) |
| Memo 5 B (`-48`) | INT-7.01, DEM-1.15 | Faithful |
| Memo 6 A, automatic penalties, Espen's terms (`-49`, `-50`, `-99` c) | INT-1.01 to 1.06 | Faithful. Penalties on spouses and executive officials (L-6); section 9 states the retirement exclusion flat against D1 (E-3) |
| Memo 7 A, P2 with P4, 71 judgeships; sitting Justices severable; not held to 2033 (`-51` to `-53`) | CRT-1.01, CRT-15.01 to 15.03 | Faithful. "Each President gets two appointments a term" overstates (L-5) |
| Memo 8 A with an inspector general (`-54`) | CRT-2.01 to 2.03, INT-12.01, 12.02 | Faithful |
| Memo 9 part 1 A′ (`-97`); part 2 changed (`-56`); part 3 B (`-57`) | CRT-5.01 to 5.10, CRT-20.01 | Faithful. The bankruptcy analogy needs its reference structure (L-7). Section 3 still carries the all-temporary −$5.5 billion as if undecided (C-2) |
| Memo 10 B and B (`-58`, `-59`), with `-99` g | CAP-7S.01, 7S.02, CAP-7.01 to 7.05, CAP-11.01 | Faithful (fix 1 is provisional, D2). The release rule's one-year wait cuts against CAP-7.03 (D-1) |
| Memo 11 B on Espen's framing (`-60`) | CAP-19.01 to 19.06 | Faithful. Section 3 still calls it "the proposal" (C-2) |
| Memo 12 B and B (`-61`, `-62`) | CAP-8.01, 9.01, 4.01 | Faithful |
| Memo 13 A with the staged path (`-63`, `-99` h) | DEM-3.01, 4.01, 4.02, 9.01 | Faithful |
| Points 1 to 50 (`-64` to `-93`, `-98`) | Throughout | Faithful. Point 1 (DEM-12.01) lacks a stated power (L-1); point 24 (INT-6.01) has an unstated sanction (L-8); point 46's CAP-12 is placed in two rows (C-5) |
| The note's directions (`-99` a to t) | As cited in section 4 | Faithful |

## 2. Findings

IDs:
- L: legal and constitutional;
- F: fiscal report and the money;
- M: missing populations;
- O: optimistic assumptions;
- A: cheaper alternatives;
- D: design lens;
- W: weak evidence;
- E: section 9 against sections 1 to 8;
- G: legacy departures not explained;
- C: consistency and record.

Severity: **blocker** (blocks L3), **fix** (a later step should do it), **note** (record only). Each finding names the decision it would inform.

### L. Legal and constitutional

**L-1. DEM-12.01, restored voting rights, rests on no stated power. Blocker.**
- *Where.* `4-specification.md`:75 (DEM-12.01, "a person convicted of a crime may vote in federal elections once released"); `5-delivery.md`:228 and `9-public-case.md`:26 (in force for any federal election 180 days after enactment); `9-public-case.md`:107-122 (absent from "What a court could strike").
- *The texts.* *Inter Tribal Council*: "the Elections Clause empowers Congress to regulate how federal elections are held, but not who may vote in them. The latter is the province of the States" (`library/text/dr7-scotus-arizona-v-itca-2013.txt`:62, :557-560). It ties the federal electorate to the state's own qualifications (Art. I, sec. 2; the Seventeenth Amendment). The Fourteenth Amendment, section 2, exempts from its representation penalty a denial of the vote "for participation in rebellion, or other crime", which the Court read in *Richardson v. Ramirez* (1974) to permit felony disenfranchisement. *Oregon v. Mitchell* (1970), the precedent for a federal voting-age rule in federal elections, rested on a lone vote under the Elections Clause that *Inter Tribal Council* now cuts against. None of this is in the register or the dossier.
- *The scenario.* The democracy act passes in April 2030. A state that bars people on parole from voting sues to block DEM-12.01 before November 2030. The three-judge court (DEM-1.13) holds it outside the Elections Clause. The plan has promised it publicly (section 9, the brief) with no line on the risk.
- *Why blocking.* A decided commitment that the dossier states as settled has a legal obstacle the dossier's own lead case states. An unsupported claim stated as settled is a defect (`charter/STANDARDS.md`, "What needs an answer now").
- *Fix (no new decision; this carries out point 1).*
  - Name the power in DEM-12.01: Congress's enforcement powers under the Fourteenth Amendment, section 5, and the Fifteenth, section 2, on a findings record of the racial origin and effect of felony disenfranchisement laws (*Hunter v. Underwood*, 1985, struck Alabama's for intentional discrimination). Add register entries for *Richardson*, *Hunter* and *Mitchell* from their texts.
  - Make DEM-12.01 its own severable section, with the notice and pretrial access (which are manner rules) severable from the restoration.
  - Keep a state track as the fallback (most states already restore on release).
  - Add a row to section 9's court table and section 8's legal events, and say "on enactment, if it survives" in the brief.
  - The same review belongs on DEM-1.03's preregistration (a manner rule, low risk) and on the floor's application to presidential elections (L-3).

**L-2. Two forums for the same suit, and the courts' load unsized. Blocker.**
- *Where.* CRT-7.01 (`4-specification.md`:259): rule challenges to the D.C. Circuit within 60 days, collateral attack barred. CRT-3.01, 3.02 (:255-256): any action seeking relief beyond the parties to a randomly drawn three-judge district court, direct appeal to the Supreme Court. CRT-9.01 (:287): "set aside" means vacatur, and "such cases go to the three-judge courts". DEM-1.13 (:69): the democracy act's challenges the same way. CRT-11.02 (:262): statutory circuit splits become appeals the Court must decide.
- *The scenario.* In 2032 a trade group files a pre-enforcement APA challenge to a new rule and asks for vacatur. Under CRT-7.01 it must be in the D.C. Circuit within 60 days; under CRT-3.02 and 9.01 it must be before a three-judge district court. The government moves to dismiss in each, and the first year of every plan rule is spent on forum. Separately, every APA vacatur suit nationwide now needs three judges and carries a direct appeal: no section counts how many, what that does to district judges' time (part of the case for the 71 judgeships) or to the Court's mandatory docket.
- *Why blocking.* Two provisions commit the same case to different courts; and a court reform with no delivery count is a missing delivery mechanism.
- *Fix (no new decision).* An order rule in CRT-3.02: where a statute channels review to a court of appeals (CRT-7.01, the Hobbs Act, Clean Air Act 307(b)), that court hears it, and CRT-3.02 covers district-court actions only. In section 5, a count of the cases that would go to three-judge courts (the Administrative Office's caseload tables for APA and nationwide-relief suits; a register entry) and the direct appeals; and in section 7 a line on whether CRT-11.02's mandatory appeals plus CRT-3.02's direct appeals exceed the Court's merits docket (56 signed opinions in OT2024, `4-specification.md`:262). *It would inform:* points 26, 29, 31 and 33 as specified, not as decided.

**L-3. The floor's reach beyond congressional elections, and the citizenship rule, are stated with more confidence than the case allows. Fix.**
- *Presidential elections.* The floor governs "federal elections", which include the choice of presidential electors. *Inter Tribal Council* reads the Elections Clause as reaching congressional elections and points to Article II, sec. 1, cl. 2, under which each state appoints electors "in such Manner as the Legislature thereof may direct" (`dr7-scotus-arizona-v-itca-2013.txt`:561-563). Section 7 says only that "the parts that rest on other powers, presidential elections and the enforcement clauses, are severable by part" (`7-validation.md`:166); no provision says which parts those are or on which power each rests. *Fix:* a table in section 4 (or a note under DEM-1.13) of which floor rules apply to presidential electors, on what power (Art. II, sec. 1, cl. 4; *Burroughs v. United States*, 1934; the enforcement clauses), and the severability unit for each. Practical exposure is small because states run both contests on one ballot, which the fix should say.
- *Documentary proof.* Section 7 says the Court "held Arizona could not add documentary proof" to the federal form "on its own" (`7-validation.md`:184), and section 9 cites the case for the floor (`9-public-case.md`:91). The same opinion kept the state's power to deny registration "based on information in their possession" and warned "it would raise serious constitutional doubts if a federal statute precluded a State from obtaining the information necessary to enforce its voter qualifications" (`dr7-scotus-arizona-v-itca-2013.txt`:57-64). DEM-1.08 bars documents a voter "must bring" (`4-specification.md`:64). *Fix:* write in DEM-1.08 that a state may use any record it holds, and that a flagged voter may answer with any evidence, a document included, at the voter's choice; and say in section 7 that this is what keeps the rule inside *Inter Tribal Council*. No change to the decision.

**L-4. *Callais*'s reach to Title II and III-B is understated. Fix.**
- Section 4 reads *Callais* as resting on "constitutional as well as statutory grounds" (`4-specification.md`:87). If that reading holds, the same reasoning reaches Title II's preclearance standard, which bars changes by their effect, and III-B's burden shift once a prima facie case is made (:88). Section 9 says that if III-A falls, "the intent title and preclearance stand" (`9-public-case.md`:113), and section 8 treats Title II's risk only as its coverage formula (`8-change-our-minds.md`:33).
- *Fix:* in section 8, part 2 and section 9's table, add "preclearance's effect standard struck on *Callais*'s constitutional reasoning", with the fallback (an intent-based preclearance trigger, or AMD-5). Cite *Brnovich* correctly as a reading of the statute that Title III-A may change (section 7's answer at `7-validation.md`:174 is right; `library/text/dr7-scotus-brnovich-2021.txt`:119, :219).

**L-5. Term limits: one overstatement. Fix.** Section 9 says "seats open two years apart, so each President gets two appointments a term" (`9-public-case.md`:97; also `7-validation.md`:206). That holds only once every sitting Justice has left, which depends on CRT-15.02 surviving, or on deaths and retirements; on CRT-15.01 alone the schedule takes decades and the first statutory term ends about 2047 (`9-public-case.md`:119). Say "once the transition ends". Also: senior Justices would still hold the office, so 28 U.S.C. 1's "a Chief Justice ... and eight associate justices" (EV-DEM-343) must be amended to count active Justices, which CRT-15.01 should say (`4-specification.md`:270 says only that the Court "stays at nine").

**L-6. The stock ban's penalty reaches people Article I, section 5 does not. Fix.** INT-1.04 computes the penalty from filings and collects it "by the chamber's ethics office from pay", with a Justice Department suit only after 90 days (`4-specification.md`:172). For members, each chamber's power to punish its members is a sound base. But the ban also covers spouses, dependent children and executive officials (INT-1.01, :169), who draw no congressional pay and are not subject to that power. *Jarkesy* holds a civil penalty "designed to punish or deter" is legal relief (`dr7-scotus-sec-v-jarkesy-2024.txt`:101-102); for non-members, the administrative collection step before any court is the exposed part. *Fix:* say that for anyone other than a member the penalty is collected only by the Justice Department's suit in district court, with a jury if asked (CRT-10.01's own rule), and that the ethics office's computation is a notice, not a judgment.

**L-7. The bankruptcy-court analogy rests on a structure the court does not copy. Fix.** Bankruptcy judges sit as "units" of district courts because the district courts hold original jurisdiction over bankruptcy cases and refer them (28 U.S.C. 1334, 157), which is what kept the 1984 scheme inside *Northern Pipeline* and *Stern* (EV-DEM-366). CRT-5.01 makes the immigration court a unit of the district court (`4-specification.md`:202), but no provision gives district courts jurisdiction over removal cases or a reference and withdrawal mechanism. Section 7 rightly notes that *Jarkesy* lists "immigration law" as a public-rights category (`dr7-scotus-sec-v-jarkesy-2024.txt`:141; `7-validation.md`:217), so the public-rights risk is lower than CRT-5.10 frames it; the exposed point is the structure, not the subject. *Fix:* add to CRT-5.01 the district court's jurisdiction and the reference (or an express statement that the court is an adjunct exercising jurisdiction Congress vests in it directly, with the risk named). Section 9's fallback "an Article I court (memo 9 A)" (`9-public-case.md`:120) is the design section 7 says *Slaughter* weakens (`7-validation.md`:219); say so where the fallback is named.

**L-8. Campaign finance: two calibrations. Fix.**
- *INT-8.01, the coordination presumption.* Section 4 says it "stays inside what *NRSC* left standing" (`4-specification.md`:157). *NRSC* struck party limits; it vouches for nothing else. *Buckley* treats spending as a contribution when it is "prearranged or coordinated" with the candidate (`dr7-scotus-buckley-v-valeo-1976.txt`:1714). *Cruz* calls a prophylaxis-upon-prophylaxis approach "a significant indicator that the regulation may not be necessary" and requires "record evidence or legislative findings" (`dr7-scotus-fec-v-cruz-2022.txt`:646-661). A presumption on "any two" of four tests, one being "supports one candidate", sweeps in independent spending. Section 7 already says it may be struck. *Fix:* drop "stays inside what *NRSC* left standing"; require a findings record in the act, as *Cruz* asks; and say which pairs of tests are likeliest to hold (staff or family plus candidate fundraising) and which are not (one candidate plus shared vendors).
- *INT-6.01, tax returns.* A condition "of filing as a candidate with the FEC" (`4-specification.md`:159) is not optional: every candidate over the statutory threshold must file. The provision gives no sanction for a candidate who refuses, and section 3's own note that ballot access "raises a qualifications question" (`3-design.md`:185) applies to whatever sanction is chosen. *Fix:* state the sanction (a civil penalty, or loss of public financing only), with the risk named.

**L-9. Statehood and the compact. Note.** DEM-5.01 admits the state by statute with the residual district's electors "directed by statute" (`4-specification.md`:127). The Justice Department's Office of Legal Counsel has twice advised that the Twenty-third Amendment makes this harder than an admission act (1963, 1987), and section 2 lists the question as evidence still needed (`2-what-works.md`:395). Section 9 should not imply it is settled; a court-risk row is enough.

### F. The money and the fiscal-rule report

**F-1. D4's "$22 billion" mixes two bases, and its revenue side is unpriced. Fix, before Espen answers D4.**
- *The base.* The pace tool builds part G's allocation at the hiring pace from a no-ramp full-rate path: $32.5 billion in FY2040 deflated at 3.78% a year, which sums to **$266.6 billion** over FY2030-39 (the tool prints it: "at full rate from FY2030 with no ramp: 266.6"). It then compares the paced result, $227.3 billion, with part G's stated **$249.5 billion**, which already carries the review's ramp (`models/tools/democratic_renewal_pace.py`:37-38, :114-115). The $22.2 billion is therefore the difference between a doubly ramped path and a singly ramped one. On one basis the pace effect is larger: about $39 billion against the tool's own no-ramp path, or about $37 billion if the paced result is scaled to $249.5 billion (reviewer's arithmetic from the tool's output). It could also be smaller: about $17 billion against part G's allocation laid on the booked ramp. Section 7 does not disclose the $266.6 billion base.
- *Less or later.* CAP-7.02 says "money stays available, so a slow year does not lose it" (`4-specification.md`:313). The pace check says the shortfall is "timing" and "no change in FY2040" (`7-validation.md`:69). Both cannot hold: if the unspent money stays available, it is spent after FY2039, or it sits as a third unclaimed balance beside the two contingencies; if FY2040 does not change, it is never spent. D4 says "less" (`7-validation.md`:327; README:62; `9-public-case.md`:135); section 9 says "spent later within 2030-39" (:59) and "spent later" (:155); section 8 says "reached later" (`8-change-our-minds.md`:101). This is #438's reviewer nit, but it is more than wording: it decides where the money goes.
- *The revenue side.* D4 lags the IRS's enforcement yield (G8) with the allocation (`7-validation.md`:72), and sections 6 and 7 say "a slow path delays the yield more than it saves outlays" (`6-cost.md`:94). G8 nets $150 billion over FY2030-39. Section 6 part 7, which prices the provisional items, does not price D4 at all (`6-cost.md`:171-182), and the README says section 6 finds the fourth "changes timing only" (`README.md`:58). A two-year lag of G8's net yield would cost very roughly $30-40 billion of revenue in the window (reviewer's arithmetic: about two years of the ramp's net yield, never modeled), more than the outlay change.
- *Fix.* In the pace tool, compare like with like (part G's own year path against the same path ramped by hiring), state the base in section 7, and recompute the range. Say what happens to an unspent balance (it lapses, joins memo 10's contingency, or is spent after FY2039) and make CAP-7.02's "stays available" agree. Price G8's lag in section 6 part 7 and restate D4 as net of it. Then re-word D4 in all places (README, sections 7, 8, 9). *It would inform:* D4.

**F-2. The fiscal-rule report meets `DEC-2026-11-10-05`. Note.** Section 6 part 8 gives the yearly cost (peak about $63 billion in FY2033), the permanent cost from FY2040 ($50.0 billion booked, $2.5 billion unbooked) and the share of the margin (8.3% booked, 0.42% unbooked), on one basis, and sends the one money question (two contingencies holding about $173 billion unclaimed) to stage G without gating. Two loose phrases: "almost all of it is the agency rebuild" (`6-cost.md`:204; `9-public-case.md`:57) is 74% ($377.2 of $507.2 billion); and "about 0.3%" (`6-cost.md`:204) is the table's 0.26%.

**F-3. CAP-12 sits in two rows. Fix (at booking).** Section 6 lists CAP-12 in CAP-8's row (`6-cost.md`:29) and in CAP-7S and CAP-7's allocation (:65), and part G's cross-cutting line carries the digital service corps (`3-design.md`:122). The review's $3.7 billion (EV-DEM-329) may be counted twice. Say which row carries it.

### M. Missing populations

**M-1. Naturalized citizens and the records check. Fix.** DEM-1.08 checks citizenship against "SSA's citizenship data, USCIS's verification service, passport records" (`4-specification.md`:64). SSA records citizenship when a number is issued and relies on people to report a later naturalization, so its data lag for naturalized citizens; election officials warned DHS in December 2025 that the expanded SAVE check risks flagging "older Americans, naturalized citizens, and voters like married women who have changed their names", and Texas gave 2,724 flagged voters 30 days to prove citizenship (reported by NPR, Votebeat and Georgia Public Broadcasting, 2025; not yet in the register). The design keeps a flagged voter registered until a person decides, which bounds the harm, but the notices fall on a known group. *Fix:* in DEM-1.08, check USCIS naturalization records and passport records before an SSA non-match can flag anyone; count expected flags in section 7 (register entries from the SAVE reports and SSA's own caveat that its data "isn't a definitive record"). *It would inform:* memo 1 B as specified.

**M-2. Voters without a fixed address. Fix.** Registration from records, the notice to decline, the voter card and the cure notice all go by mail (DEM-1.01, 1.07, 1.09). Homeless voters, people on reservations with nontraditional addresses and people who move often are reached by none of them; `grep` finds no "homeless" in the dossier, and the only tribal mention is the ID list. *Fix:* a line in DEM-1.01 and 1.07 for a description of residence or a shelter or tribal office as mailing point (as HAVA's form allows), and a row in section 4's groups table.

**M-3. Language minorities and voters with disabilities. Fix.** No provision says the floor's notices (registration, decline, voter card, cure) follow Section 203's language rules, which *Callais* does not touch; `grep` finds no "language minority" or "Section 203". No provision of the floor names accessible voting or accessible mail ballots for voters with disabilities. *Fix:* one line each in DEM-1.01, 1.05 and 1.09, citing Section 203 and the ADA and HAVA standards, and a groups-table row.

**M-4. Overseas and military voters. Note.** The floor's receipt rule and cure process (DEM-1.05, 1.09) do not say how they meet UOCAVA's own deadlines; a sentence that UOCAVA's rules govern where they are more generous closes it.

**M-5. Who the stock ban leaves out. Question for Espen.** The decided coverage (memo 6 A) is members and their families and the top executive officials. Senior congressional staff, federal judges and Federal Reserve officials are not covered by the ban; judges and Federal Reserve officials get disclosure only (INT-12.01, 12.02). Judges are the group whose financial conflicts the dossier itself documents (131 judges in 685 matters, EV-DEM-229). This is a scope choice, so it goes to Espen as a question, not a fix.

### O. Optimistic assumptions

**O-1. The voter card's cost and its photo stations. Fix.** "Well under $0.1 billion a year" (`4-specification.md`:63) for a card mailed to every registrant (about 170 million at 2024's 73.6%) is plausible for printing and postage, but the optional photo is taken free at "an SSA field office" among others, and SSA is the agency part G's dated needs strain first (paid leave by mid-2030; callbacks averaged 108.6 minutes in FY2025, EV-DEM-106). *Fix:* price the card (cards, postage, a photo share; a register entry for a comparable state card) and drop SSA field offices as a photo site, or count the workload in SSA's line. *It would inform:* the `-99` a direction as specified.

**O-2. The 180-day tier and the 2030 election. Note (D3 is provisional).** The barrier-removing rules govern November 2030 only if the act is law by about May 7, 2030 (`5-delivery.md`:228); "spring 2030 the outer date" puts enactment at that edge. A state that must reprint ID rules, mail rules and list-maintenance rules in summer 2030 is exactly the *Purcell* setting section 7 cites (`7-validation.md`:236; EV-DEM-362), though *Purcell* binds courts, not Congress. Section 8 should give the trigger: enactment after a set date moves the first covered election to 2032.

**O-3. The three-judge courts' load.** See L-2.

### A. Cheaper alternatives

**A-1. The citizenship check could use SAVE as it exists. Note.** DEM-1.08 asks states to match SSA, USCIS and passport records under CAP-19.02. DHS's SAVE, expanded in 2025, already queries USCIS and SSA records for election offices (to confirm its terms and passport coverage with a register entry). Using it, with M-1's order rule and CAP-19.02's no-enforcement-use rule written into the agreement, is existing machinery (`DEC-2026-11-13-08`) and could replace part of DEM-11.03's $0.2-0.5 billion build. Section 5 should weigh it.

**A-2. The two delivery contingencies. Note.** Memo 10 decided its contingency (`-58`), and section 6 already sends the overlap with the October 26 allowance to stage G (`6-cost.md`:92). The cheaper path, one contingency in one lane, is stage G's. No new question.

**A-3. The three-judge rule's scope. Note.** A rule that sends only suits seeking relief against federal action beyond the parties *outside* the D.C. Circuit's channelled review would achieve point 26's forum aim with fewer panels; L-2's fix may make this the drafting answer.

### D. Design lens

**D-1. The release rule's one-year wait penalizes the agency that most needs help. Fix (D2 and D4 touch it).** CAP-7.02 holds an agency's next tranche for a year when it is below 75% of its path (`4-specification.md`:313); CAP-7.03 says a program that misses its measures gets "a corrective plan reviewed by the delivery unit, not a cut" (:315). Section 7 finds the booked money path runs at about twice the working hiring pace (`7-validation.md`:67). If agencies' published paths follow the booked ramp, most will be below 75% in FY2031 and the wait will bite widely, delaying the hiring the money is meant to buy. *Fix:* set each agency's published path on the working pace (which D4 assumes anyway), and make the response to a shortfall the delivery unit's corrective plan first, the one-year wait only after two missed quarters with no plan (working choice for the fix step). This keeps memo 10 B's release-against-hiring and drops a deadline that does not earn its burden.

**D-2. The accountability layers. Note.** Quarterly counts (CAP-7.02), quarterly delivery measures (CAP-7.03), quarterly reports to Congress (CAP-7.04), GAO's yearly audit of every hiring path and release (CAP-7.05), OPM's quarterly time-to-hire (CAP-11.01) and inspectors general all report on the same hires. Espen asked for these (`-99` g). Section 5 should say which reports are one data feed, so agencies report once.

**D-3. Section 4's design-lens table covers voters and officials, not agencies, courts or states.** The burden of D-1, L-2's three-judge panels and the voter card's mailing on election offices belongs in it. Fix with D-1.

### W. Weak evidence

**W-1. Carried from #438.** "The 2024 bill passed the Senate by unanimous consent" (`4-specification.md`:45, :242) cites EV-DEM-044, which says only that Congress approved it and the President vetoed it. Add a source or drop the phrase. Section 1 says a court "did not reinstate" the 17 inspectors general (`1-problem.md`:31); EV-DEM-036 says the eight plaintiffs. Fix.

**W-2. Legal claims without register entries. Fix with L-1 and L-9.** *Richardson v. Ramirez*, *Hunter v. Underwood*, *Oregon v. Mitchell*, *Burroughs* and the OLC statehood opinions.

**W-3. Section 9's derived figures.** "About one eligible citizen in four was not registered" (`9-public-case.md`:11, :73) is 100 − 73.6 = 26.4%, which counts the 14.1% who did not answer (EV-DEM-001's context); the 28.0 million floor (EV-DEM-002) is about 12%. Say "about one in four, counting people who did not answer". "Trust is near its floor" (:18) is a judgment; "three times in seven months, including a 42-day government-wide gap" (:20) is right only if the reader knows the third gap was one department. Fix.

### E. Section 9 against sections 1 to 8

The trace found every cost, date and evidence figure in section 9 in sections 1 to 8, with these exceptions:
- **E-1.** The $22 billion is worded as "spent later within 2030-39" (`9-public-case.md`:59) and "would be spent later" (:155, with no D4 label), against D4's "less" (:135). F-1.
- **E-2.** DEM-12.01 is promised without a court-risk row (L-1).
- **E-3.** "Retirement accounts are never covered" (:38) is stated flat; D1 would cover new individual-stock purchases in self-directed accounts. Say "plan-managed retirement accounts".
- **E-4.** "Each President gets two appointments a term" (:97) (L-5).
- **E-5.** "Citizenship ... the check is from records by 2032" (:81) lacks D3's provisional label.
- **E-6.** Undated promises: DEM-11's money (:29; first grants within 60 days of enactment, provisional), the voter card's first mailings (:28; 2030 in section 5), Congress's capacity money (:54; FY2030).
- **E-7.** The source table gives sections and parts, not lines; its row for 3,300,793 pending cases cites CRT-5.06, which says "3.3 million" (the exact figure is in `1-problem.md` and the immigration register).

Fix all in one pass with F-1.

### G. Legacy departures not explained

From a sweep of `legacy/domains/domain-democracy.md`, `domain-courts.md`, `domain-integrity.md` and `domain-capacity.md` against the dossier. Explained departures (memo options, cited legacy lines) are not listed.

The sweep counted about 168 legacy designs, parameters, open items and cautions. About 98 are carried as they are and 51 depart with a reason stated (each memo's "Inherited assumptions, traced" table does most of this work). Every changed legacy dollar figure is explained. No capacity entity disappears from part G. Nine of the ten legacy open items in `domain-democracy.md` are carried or decided. What is left:

**G-1. Legal cautions the legacy files named and the dossier drops. Fix (with fix step 4).**
- *Preclearance.* Legacy requires a record "contemporaneous, violation-based and non-formulaic" and says "no guarantee of judicial survival is claimed" (`domain-democracy.md`:84). Section 4 calls a recalculated formula the answer to *Shelby County* (`4-specification.md`:86; `7-validation.md`:175), and the no-survival caveat sits only on III-A. Section 9's "could be struck" (`9-public-case.md`:115) is right; sections 4 and 7 should match it (with L-4).
- *The Justices' code.* Legacy names Justice Alito's view that no provision lets Congress regulate the Court, "period", and rates the binding code "Low-Medium" (`domain-courts.md`:75, :81). CRT-2.01 says "the Court adopts a binding code within a year" (`4-specification.md`:251) with no risk named. The same holds for emergency orders: legacy warns "dictating the substance of reasoning is the vulnerable part, and the predictable failure mode is boilerplate" (`domain-courts.md`:98), while CRT-4.01 adds a 30-day deadline and "no precedential weight" for unexplained orders (`4-specification.md`:257). Espen added the deadline (point 27), so it stays; the risk and the boilerplate failure belong in sections 7 to 9's court tables.
- *The immigration court after* Slaughter. Legacy calls removal protection "the vulnerable point" (`domain-courts.md`:104). CRT-5.02 says flatly that *Slaughter* "does not reach" judges removable only by judges (`4-specification.md`:203; `7-validation.md`:218), while the dossier's own entry on *Slaughter* (EV-DEM-037's CRS source) says the Court left open inferior officers and non-Article III courts. Say "likely does not reach", and fix section 9's fallback (L-7).

**G-2. Delivery cautions dropped. Fix.**
- *CAP-7 is an increment over a baseline.* Legacy: the line "only means what it says if baseline funding holds ... a staffing floor alone does not prevent a hostile appropriator from offsetting the increment" (`domain-capacity.md`:114). CAP-7.01 and 7.02 have no maintenance-of-baseline rule. A later Congress or OMB could cut each agency's base by the increment. *Fix:* a baseline-maintenance condition on CAP-7's money (the increment is released only while the agency's base appropriation holds, with a notice to Congress if it falls), or say why not.
- *CAP-7S is finite.* Legacy: finite multi-year money with written agency return cases (`domain-capacity.md`:107, :207). CAP-7S.01 is "available on enactment and until spent" (`4-specification.md`:310) with no bar on paying running costs from the surge and no last obligation date. *Fix:* both, in one line.
- *The House chamber.* Legacy: "the chamber seats about 448", and a rebuild "has to start in the first Congress for a 2034 seating to be physically possible" (`domain-democracy.md`:132). DEM-3.01 keeps the 2032 election open for a larger House (`4-specification.md`:115). Say that 2032 is physically possible only up to about 448 seats or with a temporary arrangement, and that the Architect's report (due 2030) decides it.

**G-3. Design choices changed without a stated reason. Fix (one line each) or note.**
- *Compact consent.* Legacy: "Do not ask for congressional consent ... Under *U.S. Steel v. Multistate Tax Commission*, asking concedes that consent is required" (`domain-democracy.md`:197). Espen's decision is "consent to be considered, with a trifecta" (`-98`), which stands; DEM-8.01 should name the concession risk so that the later consideration weighs it.
- *Venue.* Legacy sent suits seeking relief beyond the parties to the D.C. district court or a three-judge court, by amending 28 U.S.C. 1391(e) (`domain-courts.md`:88); CRT-3.02 keeps only the three-judge court drawn from the circuit. Say why (likely to avoid making one district the prize); this joins L-2. The same file warns that channelling rule review to the D.C. Circuit "makes the D.C. Circuit's composition a political prize" (`domain-courts.md`:132), which CRT-7.01 does not mention.
- *The stock ban's scope.* Legacy covers the President, the Vice President and the Cabinet (`domain-integrity.md`:15, :46); INT-1.01 adds every Senate-confirmed official (`4-specification.md`:169), with OGE's workload, and memo 6 calls itself "legacy INT-1A". Say why, or note it as a working choice inside memo 6 A.
- *INT-15's union asymmetry.* Legacy calls it "the first objection" and leaves a member-consent rule open (`domain-integrity.md`:138); section 4 sends it to legal review without a reason. Note.

**G-4. Smaller items dropped silently. Note.** The legacy direction of October 23 for an assisted 2030 registration route for beneficiaries, with offline service and timely correction (`domain-democracy.md`:364), which section 5's 2032 date for registration from records makes more relevant; the six target states for the compact (:196); that DEM-2E "is not a substitute for winning the 2030 governorships" (:126); the immigration court's A-file access and bond hearings (`domain-courts.md`:102; they sit in the immigration dossier's legacy notes, not its specification); the stock ban's "no attached provisions" floor guard (`domain-integrity.md`:48-50); biennial budgeting and the Merkley-Daines fast track (`domain-capacity.md`:79). Each needs a sentence: carried, rejected or left to its home dossier.

### C. Consistency and record

**C-1. Stale status text. Fix.** `4-specification.md`:3 says "sections 8 and 9 are not yet written". `README.md`:9 says the 118 rows are "all L1", and its family table (CRT 34, CAP 19) predates CRT-20 and CAP-19; the note's row says "For Espen" (`README.md`:37) against the note's own "recommendations accepted". Memos 1 to 5, 7, 8, 10 and 12 list their agenda rows as "(all L1)" on line 3; the rows are at L2.

**C-2. Section 3's undecided tense. Fix.** `3-design.md`:84 and :88 still carry memo 9 part 2's all-temporary −$5.5 billion "if decided"; it was decided with a change (−$4.3 billion, :21). :243 calls memo 11 "the proposal ... until Espen decides". The "Where each row is decided" table (:217-238) omits CAP-19 and CRT-20. Label the forks table "as sent" or update it.

**C-3. Small items already on the board.** Memo 9's two counts of immigration judges (557 and 753) and memo 7's "34 states" (section 4's consistency table says corrected, `4-specification.md`:485; check memo 7 itself).

**C-4. D5's wording.** `9-public-case.md`:267 (source table) reads as if the 13-Justice option is provisional; only its review point is (D5). Fix in the section 9 pass.

**C-5. Figures that differ by place. Fix.** The match: "$4-12 billion" (`6-cost.md`:47) against "$4-8 billion, up to $12 billion" (:106; `9-public-case.md`:95). Statute tracking: $0.06-0.12 billion (`4-specification.md`:422) against $0.09 billion, 0.05-0.13 (`6-cost.md`:70); the library line: $5-10 billion (`4-specification.md`:417) against $7.8 billion, 5.2-10.5, indexed (`6-cost.md`:54). The last two are harmless; say "indexed" in section 4.

**C-6. Tool and table slips. Fix.** `6-cost.md`:23 and :25, FY2036 and FY2039 (1.1 and 1.2, not 1.0 and 1.1). IMM-1's FY2040 split: 78% of −$1.06 billion is −$0.83 billion, not −$0.9 billion (`6-cost.md`:63, :146; the tool's hardcoded year shape). `7-validation.md`:69: the fifth-a-year runs reach full rate in FY2035, not FY2034. Add a unit test for each tool that pins the published tables.

## 3. Fix steps, in order

Each is sized for one later session (Most capable unless marked). None needs a new decision from Espen except where a question below says so.

1. **D4 restated** (F-1, E-1). Rebase the pace tool, state the base and recompute the range; say where an unspent balance goes and make CAP-7.02 agree; price G8's lag in section 6 part 7; reword D4 and the "$22 billion" in the README and sections 7, 8 and 9. Do this first: D4 is on Espen's decision sheet now. Tests for both tools (C-6) in the same step.
2. **The legal footing of the floor** (L-1, L-3, W-2). DEM-12.01's power, findings and severability; the presidential-electors table; DEM-1.08's records-and-evidence rule; register entries for *Richardson*, *Hunter*, *Mitchell* and *Burroughs*; section 8's legal events and section 9's court table. Clears blocker 1.
3. **The court-forum rules** (L-2, A-3). CRT-3.02's order rule with CRT-7.01; a count of three-judge cases and direct appeals with a register source; section 7's line on the Court's mandatory docket. Clears blocker 2.
4. **The other legal calibrations** (L-4 to L-9). *Callais* and Title II; the term-limit wording and 28 U.S.C. 1; the stock ban's collection for non-members; the immigration court's jurisdiction and reference; INT-8.01's findings and INT-6.01's sanction; statehood's court-risk row.
5. **Missing populations and the voter card** (M-1 to M-4, O-1, A-1). The check order and flag count; addresses, languages, disability and UOCAVA lines; the card priced and SSA's role removed or counted; SAVE weighed. Standard tier with a Most capable check of the M-1 wording.
6. **The design lens on the rebuild** (D-1 to D-3, G-2). The release rule's response to a shortfall; one data feed for the reports; the burden table widened. Touches D2's fix 1 and D4, so it follows step 1 and Espen's answers.
7. **Section 9 pass** (E-2 to E-7, W-3, F-2's wording, C-4). After steps 1 to 6, so the public case follows the fixed sections.
8. **Record clean-up** (C-1 to C-3, C-5, F-3, W-1, G-3 and G-4). Standard tier. G-1 goes with step 4 and G-2 with step 6.
9. **Re-check and booking** (`charter/STANDARDS.md`, "Milestone review"). The L3 re-check on the close-out PR, then the booking step (`6-cost.md` part 9), after Espen's answers to D1 to D5 and the questions below.

## 4. Questions for Espen

Kept apart from the fixes. Each is a decided choice with a cost or gap the dossier does not show; none argues the choice.

1. **D4 should wait for fix step 1.** The "about $22 billion less" on the decision sheet is on two different bases, may be $17-39 billion on one basis, and leaves out the IRS revenue that lags with it (perhaps $30-40 billion over FY2030-39, unmodeled). *Recommended:* hold D4 until it is restated; nothing is booked meanwhile.
2. **The stock ban's reach (memo 6 A).** Senior congressional staff, federal judges and Federal Reserve officials are not covered by the ban; judges and Federal Reserve officials get disclosure only. Should a later step weigh adding any of them? (No cost; a scope choice.)
3. **DEM-12.01 if its power fails.** If the fix step finds no enforcement-clause record strong enough, is a state track (with the notice and pretrial access kept federal) an acceptable fallback, or should the plan carry the federal rule and accept the court risk? *Recommended:* carry the federal rule as a severable section, with the state track behind it.

## 5. What this review did not do

- It did not re-run the vote simulator or the immigration model; section 7's figures for them are taken as the subagent reproduced the immigration split (`immigration_model.term_increment`, −$5.55 billion and −$1.06 billion).
- It did not read sections 1 and 2 line by line; their evidence enters only where sections 3 to 9 rely on it.
- It added no register entries; fix steps 2 and 5 do.
