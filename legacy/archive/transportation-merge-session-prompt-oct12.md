# Prompt for the merge session — build the unified Moving America Act of 2031

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/merge-session-prompt.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Run this **after** `sources/transportation-atra-merge-contribution-oct12.md` exists in the project. If it isn't there, stop and tell me.

---

I'm Espen Swanson — first-year MA at Johns Hopkins SAIS, formerly on Rep. Suzanne Bonamici's staff, targeting Senate committee staff work. I've built two complete bills in parallel sessions and I want them merged into one document.

**You cannot read either of those conversations.** Everything durable is in this project and in three published artifacts. That's the whole of what you have, and it is enough.

## What exists

| Source | Where | What it is |
| --- | --- | --- |
| ARCA architecture doc | artifact `518f3bb4-2063-42e2-9b4b-1936f8d19ca8` | Intercity passenger rail, thirteen titles, $254.03B. **Rev 354**, corrected to the FY2032-36 calendar |
| ATRA architecture doc | artifact `6eded0d5-40fc-433a-b940-8d8ca015f581` | Public transportation, $224.42B. Division A secs. 101, 108 and 109 are drafted here. Banner and canonical table on FY2032-36; prose still has FY2031-35 survivors |
| Package section-by-section | artifact `fb14029c-152b-4727-9ae3-b2f055c8b6f7` | 250-Plus, the reconciliation packages, the 2031 bill, Divisions A-F. **Read this first** — the division letters are assigned in it. Framework tables restated to FY2032-36; prose may still have FY2031-35 survivors |
| `sources/transportation-arca-status-oct12.md` | project | What ARCA is, what was fixed, every open item, and the merge blockers. **Your best single starting point** |
| `sources/transportation-atra-merge-contribution-oct12.md` | project | ATRA's equivalent: the highway scoping, division A status and drafted text, decisions, positions, contradictions with ARCA |
| `sources/transportation-calendar-fy2032-36.md` | project | The fiscal-year decision, the bill's name, and the restated figures |
| `index/tools/transportation/transit_fiscal_model.py` | project | The fiscal model, re-keyed to FY2032-36 (`BILL_START = 2032`). **Run it, don't recompute by hand** |
| `frameworks/transportation-transit-rail-split.md` | project | The split framework. Carries a superseded-numbers banner — read the reasoning, ignore the ratios |
| `sources/transportation-transit-package-status-oct12.md`, `transit-context-notes.md` | project | Earlier state; partly superseded by the contribution doc |
| `index/tools/transportation/transit_apportionment.py`, `ntd_uza_2024.py`, `transit_pipeline_data.py` | project | Supporting models |

The corridor pipeline grids and the network maps are **out of scope.** Don't merge them, don't cite their contents as authority, don't rebuild them.

## The bill

**Working title: the Moving America Act of 2031.** The divisions keep their own short titles — the American Transit Renewal Act is division C, the American Rail Competitiveness Act is division D. Convention: "the Moving America Act of 2031 (the 2031 bill)."

## The fiscal-year convention — get this right first

**BUILD America 250 / 250-Plus authorizes FY2027-31, with FY2031 as its final year. The Moving America Act authorizes FY2032-36. The next bill authorizes FY2037-41, and the second decade runs FY2037-46.**

Both bills were originally drafted with the 2031 bill mislabelled FY2031-35, which double-authorized FY2031. That is corrected in the ARCA doc and in the model. **Assume it survives somewhere in the ATRA doc and in the package section-by-section, and check.**

Authorization levels are unchanged in nominal terms and read as FY2032 dollars. They were not re-indexed and should not be.

Dates that follow:

- sec. 106(c) commitments run to FY2046;
- the sec. 106(e) readiness reserve lapses September 30, 2036 and is released over FY2032-36;
- sec. 107 continues renewal programs at FY2036 levels;
- the sec. 303 readiness window is 2034-2036.

The FY2028 account floors in sec. 101(c)(1) and the FY2045 statutory parity backstop are unchanged. The glide path reaches parity in FY2042 and beats the backstop.

**FY2031 is a 250-Plus year for every mode:** highways $77.64B FHWA + $2.24B safety, transit $20.70B, rail $13.3B.

## Already decided by Espen (October 12) — carry these, don't reopen

The ATRA side recommended these and Espen accepted them. Record each in "Assumptions not yet approved" as **decided**, with the alternative, so a reader sees the choice. Then build on it.

- **Division structure and letters:**
  - A — revenue and trust fund;
  - B — highways and highway safety;
  - C — public transportation (ATRA);
  - D — intercity passenger rail (ARCA);
  - E — research, data and project delivery;
  - F — budget discipline and general provisions.
- **Highway division: hybrid.** Incorporate H.R. 8870's highway title (as enacted in 250-Plus) by reference. Draft only the amending sections the shared trust fund needs. The contribution doc proposes about eleven, secs. 1101-1112 plus 1201 and 1301.
  - **All of division B counts as renewal** for div. A secs. 101(f), 107 and 108, except sec. 1112's general-fund grants.
  - That keeps the equal-coverage solve at 34.7 / 53.7 / 11.6. Each 5% of the highway program classed as expansion would cut highways' solved share by about 3.3 points.
- **49 U.S.C. 5307 operating eligibility: scenario B,** the drafted conditional tier at $35.00B. It's decided on policy grounds (federal share, substitution risk, the trade-down dial), since C now also fits.
- **Incremental shares: 35 / 50 / 15 stays in the text.** The transit gap against the equal-coverage solve waits for a later redesign of the EV fee's place in the system.
- **Joint terminals:**
  - ARCA sec. 310 ($20.20B) is the single program for the five nodes, and div. A sec. 109's train-movement rule decides which account books each obligation.
  - ATRA sec. 606 is retargeted to joint facilities outside those five nodes and cut to **$3.0B** ($0.6B a year). Rerun the model with that change before carrying any total. It reduces transit expansion by $3.0B over FY2032-36.
- **The 0.206% is a benchmark,** this project's own rule, neither CBO's nor statute's. Exceeding it is acceptable. What binds is the reconciliation instructions (sized to CBO's net-of-offset score), PAYGO and the Byrd rule. Drafted sec. 108(b) still writes 0.206% in as a hard trigger. Decide whether it keeps a number, changes it, or becomes report-and-recommend (open question 11).

## Decide, don't ask

**Make the defensible call on each open question and flag it** — don't stop and ask me. I'd rather review decisions than answer questions one at a time.

**How to flag.** One section near the top — "Assumptions not yet approved" — listing each call, the alternative, and what changes if I overturn it. Then a bold inline marker at each place the assumption does work, so I can find every consequence of a decision from the one list.

### The open questions, in order of how much they move

Questions 2, 3, 4 and 8 below are **settled by the section above.** Write them up as decided rather than deciding them again.

1. **The FY2028 forcing event — the largest unverified premise in the design.**
   - Every reauthorization since 1982 has extended the expiring fuel taxes to at least the end of its own authorization period. IIJA extended them through September 30, 2028.
   - A 2026 bill covering FY2027-31 would ordinarily push them to FY2031 or FY2032. That would delete the FY2028 forcing event the whole revenue architecture is built on.
   - **Carry the FY2028 event as the base case** (it is current law, and the design is coherent on it) and **put this at the top of the assumptions section.**
   - Do not re-model the variant; it is hours of work and out of scope here. Say plainly what it would do:
     - the per-mile fee starts FY2032;
     - there are no FY2029-31 rail receipts;
     - rail coverage in FY2032-36 falls well under 27 percent;
     - division A's revenue title becomes the first structural surface revenue bill rather than a reform of one.
   - The ARCA doc has the full passage under "The largest unverified premise in this design."
2. **The transit/rail split and the incremental shares.** *Decided above.* Bill text says 35 / 50 / 15. Equal renewal coverage in FY2042-46 solves to 34.7 / 53.7 / 11.6.
3. **49 U.S.C. 5307 operating eligibility.** *Decided above: scenario B.* On the corrected calendar, C takes the FY2032-36 draw from 0.174% to 0.190%, which now *fits* under the benchmark with about $5B a year to spare. The case for B rests on policy, not affordability.
4. **Division structure and letters, and the highway division.** *Decided above.*
5. **Division A sections 102, 103, 104, 106, 107, 110 and 111.** Draft what the contribution docs leave missing. Section 111 is the one most likely to decide whether the fee survives: per-mile administration, Treasury collection, odometer-only reads, a bar on location data, a State collection-agreement option, a 10 percent cost allowance. The contribution doc has a position to draft from.
6. **The FY2031 cliff.**
   - Rail drops from ~$37B in FY2030 to $13.3B in FY2031, then rises to $39.95B in FY2032. Transit falls from $40.2B to $20.70B.
   - There is ~$48B of benchmark room in FY2031.
   - The ARCA doc and the ATRA contribution both recommend the 2030 reconciliation package carry availability through FY2031, with obligation and expenditure deadlines. Confirm or replace that.
7. **The $4.19B trapped in the Mass Transit Account in FY2031.**
   - The three-way split starts FY2029, but transit and rail programs don't scale until FY2032, so transit's dedicated receipts ($24.9B) exceed its 250-Plus program ($20.70B).
   - Division A has to dispose of it: carry it forward as an opening balance, or delay the split to FY2032 and forgo it.
8. **The joint terminals.** *Decided above.* Show the arithmetic.
   - Commuter trains run 79 percent of movements at Chicago Union Station.
   - The sec. 109 rule applied to renewal at the four existing terminals puts up to ~$14.0B of ARCA's $17.2B existing-terminal work on the transit account.
   - Washington Union Station's figures are unverified, and Atlanta has no intercity terminal.
9. **Whether H.R. 8870's $26B of general-fund grants count against the 0.206 percent benchmark.** $26B against $12-17B of annual headroom is not a rounding error.
10. **The illustrative Tier 1 allocation and the per-corridor cap.**
    - The table still sums to $40.00B against section 303's $55.00B, leaving $15B unallocated. The $14.0B cap was 35 percent of $40B.
    - Two choices: deepen the five corridors or admit a sixth; and keep the cap a percentage (rising to $19.25B) or fix it in dollars.
11. **Section 108(b)'s number.** Now that 0.206% is a benchmark, the drafted hard trigger can keep a number, change it, or become report-and-recommend. No bill year reaches 0.206% on the corrected calendar. FY2030 (0.197%) and a light-duty-only fee (0.209% in FY2030) are the tight cases.

## The 2026-bill discipline rule — do not break this

**Nothing in BUILD America 250-Plus may be sized to anything in these documents.** Lawmakers in December 2026 do not have the FY2032-46 program in front of them; the model does, and it leaked that knowledge backwards more than once.

- **H.R. 8870 as written contains no general-fund transfer.** It authorizes contract authority against accounts CBO projects will run dry (highway in FY2028, transit in FY2027) and does not fix them. The model's FY2027-31 general-fund column is an inference about what Congress would have to do later, mostly through annual appropriations, not a provision of any bill.
- **The 250-Plus transfer ask stays at $108.0B** ($71.2B highway + $36.8B transit, CBO's shortfall through FY2030). Do **not** grow it to the $147.7B that the shortfall through FY2031 would justify. A 2026 Congress patches to the cash in front of it, in increments.
- **Nothing in FY2032-46 depends on the transfer's size.** The rail account's FY2029-31 receipts come from the per-mile fee, not from a 2026 patch.
  - What the size does affect is whether the accounts are solvent on the day the Moving America Act starts. If they are not, sec. 101(c)(1)'s FY2028 floors are credited against receipts already spoken for.
  - That risk is real and unmodelled.

## Figures that govern — carry these, don't re-derive them

FY2032-36, architecture C / scenario B base case, **before** the sec. 606 cut to $3.0B. Rerun after applying it.

**Program:** total **$908.80B**.

- Highways and safety $430.35B, transit $224.42B, rail $254.03B.
- Division E is about $1.0B, outside the model.
- Up to $25B of ARCA readiness authority on top, contingent.

ARCA by year: 39.95 / 47.29 / 52.07 / 56.13 / 58.59. Title II $59.95B, Title III $160.45B, Titles IV-XIII $33.63B. ATRA by year: 40.70 / 42.89 / 45.09 / 47.04 / 48.70.

**How it is paid for ($B):**

| | Highways | Transit | Rail | Total |
| --- | --- | --- | --- | --- |
| Program | 430.35 | 224.42 | 254.03 | 908.80 |
| Dedicated | 316.25 | 147.20 | 68.26 | 531.71 |
| General fund | 114.10 | 77.22 | 185.77 | 377.09 |
| of which expansion (mandatory approps) | — | 33.50 | 93.20 | 126.70 |
| of which div. A sec. 110 renewal transfers | 114.10 | 43.72 | 92.57 | 250.39 |

**General-fund draw against the 0.206% benchmark** (a benchmark this project adopted, neither CBO's nor statute's):

- FY2027-28: 0.171%;
- FY2029-31: 0.154% (peak 0.197% in FY2030);
- **FY2032-36: 0.174% (peak 0.177% in FY2034)**;
- FY2037-41: 0.123% (peak 0.132%);
- FY2042-46: 0.123% (peak 0.124%).

ARCA alone: 0.121 / 0.122 / 0.069 / 0.068.

**On CBO's net-of-offset basis** (new excise net of ~25% income and payroll offset): FY2030 0.219%; **FY2032-36 0.193-0.203%, under the benchmark in every year.** It was over on the old calendar.

**Headroom:** FY2032-36 $12.4-16.6B a year. After the $25B reserve at $5B a year, $7.4-11.6B.

**Whole-program coverage by dedicated revenue** (highways / transit / rail):

| Period | Coverage |
| --- | --- |
| FY2029-31 | 70 / 75 / 17 |
| FY2032-36 | 73 / 66 / 27 |
| FY2037-41 | 75 / 65 / 48 |
| FY2042-46 | 73 / 59 / 50 |

- In FY2042-46 overall, there are ~$143B a year of dedicated receipts against ~$223B of programs. **No surface account is self-financing.**
- Rail renewal programs in FY2036 are $37.1B, which is what sec. 107 continuation carries.

**Revenue:**

- **Per-mile fee:** 1.0¢ FY2029, rising 0.2¢ a year to 3.6¢ FY2042. Priced on 3,323.8B FHWA vehicle-miles growing 0.5%, all vehicles, 10% collection cost.
- **Aviation segment surcharge:** $4 FY2032 → $12 FY2036 → capped at $16 by FY2046.
- **Rail diesel:** 10¢/5¢ for FY2030-31, 15¢/7.5¢ from FY2032.
- **EV fee:** EV $130 / PHEV $35, escalating to $200. Made permanent and redirected to the fund by div. A sec. 103.
- **Reconciliation FY2029-30:** rail $48.5B, transit $32.0B.

**Two models are superseded and must not be carried forward:**

- ARCA's trust-fund cash-flow model. It was scored on an obsolete $185.43B program, a standalone rail trust fund, and a $143.0B/$132B transfer.
- Its $115B ten-year deficit figure.

Re-run the cash-flow model if you can. If not, say plainly that the merged bill has no cash-flow model and no CBO-style score, and that both are needed before it can be scored.

**ARCA's own validation rows are retired, not relabelled:** affordability 0.105 / 0.099 / 0.019 / 0.001, and dedicated revenue $9.4B / $83.7B / $165.9B / $244.5B. The method behind them froze highways and transit at CBO baseline outlays and counted no continuing appropriations for either. The ARCA doc carries a note recording them and why. Don't resurrect them. (The model can still reproduce them on the old calendar with `calendar(2031)`, for the record only.)

## How to work

**Don't read both architecture docs end to end.** They're roughly 450KB between them. You'd spend the context window reading and produce a flattened summary of two bills rather than one bill. Instead:

1. Read `sources/transportation-arca-status-oct12.md`, `sources/transportation-atra-merge-contribution-oct12.md`, `sources/transportation-calendar-fy2032-36.md` and the package section-by-section. That's your map.
2. Create the unified doc's skeleton — title, byline, one pending block per section — as your **first** document call, before further research, so I can see the plan while you work.
3. Then fill it section by section, pulling text out of the two source docs **selectively**, by search and by block, not whole.
4. Use subagents for extraction: one per division, each returning normalized sections rather than raw document. Keep your own context for drafting and for keeping the numbers straight.
5. Run the model rather than trusting any figure quoted in prose, including figures quoted in the contribution docs or in this prompt.

## The document

One doc. Suggested skeleton — change it if the contribution docs imply better:

1. What this is, and the division map
2. The fiscal architecture — **one** section: the envelope, the 0.206% benchmark, the revenue package, the trust fund, the fit table.
   - ARCA's fiscal-envelope section is one candidate base. The ATRA contribution argues its own (rebuilt on the model, with the architectures, choices, sensitivities and chart) is the better base for the architecture and the draw, with ARCA's fee-sizing and fit tables folded in.
   - Weigh both and fold in the model's figures and the highway denominator.
3. Division A — revenue and trust fund, secs. 101-111, with drafted text
4. Division B — highways and safety (hybrid, per the decision above)
5. Division C — public transportation
6. Division D — intercity passenger rail
7. Divisions E and F
8. **One** canonical combined authorization table, all three modes, by year and by section
9. The 2029-30 reconciliation packages and the Byrd analysis — one section
10. The BUILD America 250-Plus baseline and the FY2031 cliff — one section
11. Political path — one section
12. Fallback tiers — one section
13. Assumptions not yet approved
14. Open items
15. Sources

Both documents independently carry sections 9 through 12. In the merged doc each becomes **one** section, written once from both modes' figures. If you leave two of any of them, the document contradicts itself.

Every internal cross-reference has to be re-pointed — ARCA's "section 303" becomes "section 303 of division D." Script it rather than doing it by hand, and check the result.

## How I work

Challenge me. Both bills improved most where a premise of mine failed — the fiscal-year error above was caught that way, and it moved real conclusions.

- If a figure in either contribution doc doesn't survive contact with the model, say so rather than carrying it.
- Verify arithmetic in code.
- Be concrete about statute. "Amend 5307 to permit operating assistance" is not a provision; give me the amendment.
- When you flag an assumption, say which conclusions are actually sensitive to it, not just that it exists.

Audit at the end: one pass across the whole document for stale figures, duplicated sections, broken cross-references and totals that don't sum. On the ARCA side that pass caught:

- a missing $38.20B of table rows;
- a $15B allocation that no longer matched its section;
- three internally inconsistent annual columns;
- a fee basis that contradicted itself.

Assume yours finds comparable things.
