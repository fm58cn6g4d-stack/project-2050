# Decision Brief 1: Senate Rules and Closing the Gap

Oct 20, 2026 · prepared for Espen · live doc: https://claude.ai/artifact/STTq2kjhUfzJUYJUy8VafV

## Decisions recorded (Espen, Oct 20)

| # | Decision | Outcome |
| --- | --- | --- |
| 1 | D2 path | **Agreed:** F with Block 3, adopted week one 2029; C with a 15-day backstop as the opening offer; G as fallback |
| 2 | Reconciliation | **Agreed:** R1 now; R3 vs R4 decided with D2's adoption resolution |
| 3 | Revenue closers | **Executed:** Package B (C18, C35, C19b, C20) is the planning basis; the scoring sprint is done (below) |
| 4 | Borrowing | **Agreed:** C21, C31, C32, C37. Espen also directed a broader loosening of the deficit-financing rule, keeping the long-term arc toward solvency, sustainability, wellbeing and fairness; D4 options are drafted in the governing doc (D4-B, a fiscal-arc rule, recommended), parameters pending |

**Where the gap stands now.** About $1.46T on the planning basis, before the program trims (next brief, up to $0.69T) and the sprint package below.

## Scoring sprint results: top-end candidates

Scaled to 2030-39 from Treasury's FY2025 Green Book (via ITEP) unless marked; all scored before the 2025 tax law, so TS1-TS3 need fresh scores. Home: domain-revenue.md.

| ID | Option | 2030-39 mid (range) |
| --- | --- | --- |
| REV-TS1 | Sec. 162(m) $1M pay-deduction limit for every employee of every C corporation | 0.34 (0.25-0.40) |
| REV-TS2 | Repeal the foreign-derived deduction (FDII/FDDEI) for C corporations above the sec. 448(c) small-business receipts test (~$31M, indexed); smaller C corporations keep it (added Oct 20; pass-throughs never had it) | 0.19 (0.11-0.29) |
| REV-TS3 | End fossil-fuel preferences and dual-capacity rules (takes REV-SC3's fossil piece) | 0.13 |
| REV-TS4 | Limit multinationals' excess interest deductions | 0.05 |
| REV-TS5 | Close tax-free spin-off abuses | 0.05 |
| REV-TS6 | Trust and GRAT reforms (20% overlap haircut with REV-E1 and G9) | 0.10 |
| REV-TS7 to TS11 | Large retirement balances, partnership basis shifting, like-kind exchanges, carried interest, crypto wash sales | 0.03 / 0.02 / 0.025 / 0.02 / 0.03 |
| REV-TSX | 10% overlap, avoidance and baseline haircut | −0.10 |
| **C38** | **Sprint package** | **0.89 (0.60-1.14)** |

**Held in reserve:** REV-TS12, a 28% cap on the value of itemized deductions above $450K (about 0.25-0.55; the 2025 law already caps that value at 35% for the top bracket; unscored); REV-SC1, a 45% bracket above $5M (0.18).

**Effect.** The planning-basis gap of $1.46T falls to about $0.57T with the sprint package, or about −$0.12T (a small cushion) with the trims as well. On the household test (scenario P: Package B plus the sprint), every group below the top comes out ahead. The fourth quintile nets about +$1,304 a year on average and is still behind in 2030 (about −$1,509). 72% of new general-fund revenue comes from the top 1% and corporations.

**Next:** confirm C38 once TS1-TS3 are rescored; Decision Brief 2 (program trims and scope); choose D4-B's parameters.

## What this brief asks you to decide

Four calls, in this order, because each changes what the next one has to do:

1. **D2, the Senate rules path:** which rule the plan is built on (today it is only a modeling basis).
2. **The reconciliation dial:** keep reconciliation as it is, or narrow it later.
3. **The revenue closers:** how much of the remaining gap to close with options that reach the upper middle (C19 or C19b, C20), on top of the top-end options (C18, C35).
4. **The borrowing readings:** confirm the four time-limited capital lines (C21, C31, C32, C37) that D4 now allows.

The program-scope trims (C5, C17, C33, C34, C36) and the related scope choices (LAB-9, CAP-7, NSC-1) are the next brief. All figures are ten-year totals for 2030-39 in trillions unless marked. Ledger figures are from index/2029-trifecta-master-ledger.md (Oct 20, later rebuild); household figures from index/revenue-household-incidence-model.md (v1.4). Everything tagged estimate is Claude's.

## 1. D2: which Senate rule the plan is built on

**Why it matters.** Every regular-order item tagged ◐ (about 20 contested bills, including DEM-1, IMM-1, HLT-3, LAB-1, RTS-1 and SS-1) passes or fails on this choice, and the floor calendar is built on it.

| Path | How a contested bill passes | First-Congress floor days (budget 163) | Contested bills that pass | Reciprocity |
| --- | --- | --- | --- | --- |
| A. Merkley-Daines as written | 60 votes, less dead time | n/a | Only those with 7-8 Republicans | Keeps the minority veto |
| B. Cloture at 55 | 55 votes | n/a | Those with 1-3 Republicans; party-line bills fail | Keeps a smaller veto |
| C. Talking filibuster with a speech budget | Majority once opponents' speeches run out | 211 at ~15 days per top fight; ~241-271 at the Talarico model's observed 20-25 days | All 20, if the majority holds through 5-6 multi-week fights | Strongest of the majoritarian paths: the minority pays in time |
| D. Uncapped talking filibuster | Majority only when opponents stop | Unbounded on the minority's chosen bills | All but the minority's top priorities | Minority keeps a veto it must physically defend |
| E. Full elimination | Majority after normal debate | 164 | All 20 | Weakest |
| F. Graduated cloture (current primary) | 60, 57, 54, then a majority, about a day apart | 170 | All 20, ~4.5 days each | Removes the veto with a short delay, plus guaranteed amendments |
| G. Carve-out only (failure case) | Majority for democracy and election bills; 60 otherwise | 73 | 3 of 20 (DEM-1, DEM-5, DEM-6) | Narrowest claim |

Sources: "Senate Rules Reform: Options" (Oct 19) for the designs; ledger-paths.py for the day counts; the Talarico stress test for C's pace.

**What changed since the options doc was written.**
- **C's arithmetic got worse.** The stress test's pace (19-31 days per contested bill, mean about 24) puts C at roughly 265-270 days against 163. C as drafted cannot carry the first Congress without its optional backstop. With the 15-session-day backstop it becomes a slower F (about 211 days), still about 48 days over.
- **DEM-1 now comes after R1 (DEM-1F).** The rules vote no longer has to precede a February voting-rights bill, but it must still come before DEM-1's floor time in mid-2029. The options doc's "week one" adoption still works and is safest: the majority is largest then, and R1 doesn't need it.
- **The lame duck comes first.** Merkley and Daines seek a two-thirds vote on Block 1 after the Nov 3 election. If it passes, Block 1 is already in force in 2029 and the 2029 fight is only over the final-passage rule. Re-check this after the lame duck.

**Recommendation: decide F, with Block 3's minority guarantees, adopted in week one of 2029; keep C-with-backstop as the opening offer to institutionalist holdouts, and G as the written fallback.** F is the only majoritarian path that fits near the 163-day budget (170 days; the remaining overrun closes through merges). Its guaranteed amendments and equal time are what make it defensible in the minority. Offering C with a 15-day backstop first gives holdouts a version where the minority visibly can grind. If they take it, the cost is about 41 extra floor days, which would push one or two contested bills into 2030.

**What deciding it changes.** D2 moves from Open to Decided (F). The ◐ tags stay, but the floor plan stops carrying three alternatives. The 2027-28 drafting work (CAP-18) gets a concrete rules resolution to write.

## 2. The reconciliation dial

| Variant | Rule | Effect |
| --- | --- | --- |
| R1 (as now) | Any Byrd-compliant fiscal change | All three 2029-30 vehicles work as planned |
| R3, narrowed from Jan 2031 | Deficit reduction only, after the 2029-30 bills | Most credible reciprocal version; the 2033-36 trifecta's fiscal bills would need regular order under F |
| R4, narrowed from Jan 2037 | Same rule, when the stipulated Democratic presidency ends | Keeps every Democratic fiscal bill through 2036; a weaker reciprocity claim |

**Recommendation: R1 now, and decide R3 vs R4 together with D2's adoption resolution.** Narrowing only makes sense once a majoritarian path for regular order exists. If F is adopted, R3 is affordable: the 2033-36 fiscal agenda could move under F at about 4.5 days a bill. If D2 lands on C or G, keep R4 or R1, because reconciliation is then the only reliable path.

## 3. Closing the gap: how far up the income scale the closers reach

**Where the gap stands.** General-fund claims are about $10.48T against a $6.37T top-end base, a $4.11T gap, or $3.81T after C30 (accepted). Taking every option on the list leaves about $0.15T. But most of the remaining distance comes from just two options that reach the upper middle.

| Step | Options | Closes | Gap left |
| --- | --- | --- | --- |
| Start (after C30) | | | 3.81 |
| More top-end revenue | C18 (top brackets +1, gains +2, LIFO repeal) 0.62; C35 (estate tax beyond G9) 0.15 | 0.77 | 3.04 |
| Borrowing readings (part 4) | C21, C31, C32, C37 | 0.25 | 2.79 |
| Program trims (next brief) | C5, C17, C33, C34, C36 | 0.69 | 2.10 |
| **What's left for the middle-reaching closers** | C19 (exclusion cap at the median) 1.25; C20 (1-point surtax above $100K/$200K) 0.67 | up to 1.92 | 0.18 |

**The finding.** Even with every top-end option, every borrowing reading and every trim, about $2.1T remains, and the menu has only two ways to close it: C19 and C20, which both reach the upper middle. So the real choice is between three things: accepting the middle-reaching closers, finding new top-end revenue that isn't on the menu yet, or shrinking or phasing the agenda.

**The packages, with the household test (D3).** Fourth-quintile net is the average dollars per household per year over 2030-39; every quintile below the top stays positive in all four.

| Package | Middle-reaching closers | Gap left | Q4 net, 10-yr avg | Q4 in 2030 | Note |
| --- | --- | --- | --- | --- | --- |
| A. Every option (ledger basis) | C19 + C20 | 0.18 | +$756 | −$1,823 | Passes D3 narrowly; 2030 is negative before the midterm |
| B. Softer cap | C19b (75th percentile, 0.66) + C20 | 0.77 | +$1,451 | −$1,244 | About $0.6T still to find |
| C. No exclusion cap | C20 only | 1.43 | +$2,229 | — | About $1.4T to find |
| D. Top-end only | neither | 2.10 | +$2,373 | −$477 | About $2.1T to find; the agenda as written can't close without it |

**The dynamic sensitivity widens it.** On CBO/JCT-style conventions, macroeconomic feedback is about −$0.56T (range −$1.42T to +$0.28T, estimate), most of it from the top-end taxes. It isn't counted under D4, but it argues against planning to the last $0.15T.

**Candidates to fill the rest without reaching the middle (none scored yet):**
- REV-SC1, a 45% bracket above $5M (~0.18, scenario figure).
- REV-SC2, pass-through and deferred-compensation reform (~0.35, scenario figure). Overlaps H1a, and also SS-5, the recommended Social Security closer, so the same base can't be used for both.
- REV-SC3, crop insurance and fossil-subsidy repeal (~0.10, scenario figure).
- Not on any list yet: capping the value of itemized deductions for top earners, carried interest, like-kind exchanges, and a larger corporate minimum tax. Each needs a score and an overlap check against G9 and GX.
- Phasing the largest claims (health $4.4T, family $2.1T) by a year or two is the other lever. It trades felt-by-2030 delivery for ten-year cost.

**Recommendation: Package B as the planning basis, plus a scoring sprint on the top-end candidates to cover the remaining ~$0.6T.** Package B passes the household test with more room (+$1,451 for the fourth quintile, and a smaller 2030 dip). C19b hits a smaller group: plans above the 75th percentile of premiums, mostly the most generous employer plans. If the sprint finds less than $0.6T, the choice comes back as C19 at the median versus phasing. Package A remains the fallback.

## 4. The borrowing readings

D4 now allows borrowing for time-limited capital. Four options apply that reading:

| Option | What borrowing finances | Closes |
| --- | --- | --- |
| C21 | HOU-3C's state revolving-fund grants | 0.06 |
| C31 | HOU-5's ten-year public housing repair | 0.06 |
| C32 | DEM-17's time-limited community capital fund | 0.03 |
| C37 | CLI-5's adaptation-finance and minerals-offtake lines (instead of trimming CLI-5 under C29) | 0.10 |

**Recommendation: accept all four.** Each is a time-limited capital line of the kind D4 now names (C30 and the Oct 20 climate reading). C37 replaces C29: CLI-5 is kept whole at about $0.03T of residual.

## Your calls

| # | Decision | Recommended | Alternatives |
| --- | --- | --- | --- |
| 1 | D2 path | F with Block 3, week one 2029; C-with-backstop as the opening offer; G as fallback | C, G, or keep D2 open |
| 2 | Reconciliation | R1 now; R3 vs R4 decided with D2's adoption | R4 now; R1 indefinitely |
| 3 | Revenue closers | Package B (C18, C35, C19b, C20) plus a scoring sprint for ~$0.6T of top-end candidates | A (C19 at median), C, D plus phasing |
| 4 | Borrowing | Accept C21, C31, C32, C37 | Take C29 instead of C37 |

Once you decide, the ledger, the options register, the governing doc (D2 and the decision log) and the dashboard update in one pass.

## Sources

- Senate Rules Reform: Options (https://claude.ai/code/artifact/0f226c46-5ce8-4bec-9a54-c5fd7e7a5629), Oct 19, 2026, and its sources (the Merkley-Daines "To Save the Senate" proposal, Oct 8, 2026; The Hill; Roll Call; Daily Signal)
- index/2029-trifecta-master-ledger.md and index/tools/ledger-paths.py (Oct 20, later rebuild)
- index/revenue-household-incidence-model.md, v1.4 (scenarios B, C, D and the year paths)
- index/options-register.md; domains/domain-revenue.md (C18-C20, REV-SC1 to SC3, REV-E1)
- frameworks/scenario-stress-test-talarico-2029-2037.md (path C pace)
