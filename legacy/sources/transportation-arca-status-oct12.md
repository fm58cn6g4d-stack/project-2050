# ARCA — status after the transit handoff and the FY2032-36 calendar correction

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/arca-status.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Applied 2026-10-12 from `archive/transportation-arca-handoff-prompt-oct12.md`. Doc: [American Rail Competitiveness Act of 2031 — Full Bill Architecture](https://claude.ai/code/artifact/518f3bb4-2063-42e2-9b4b-1936f8d19ca8), now at rev 354. Every figure re-verified against `index/tools/transportation/transit_fiscal_model.py` (rerun, not recomputed by hand).

## Applied

| Handoff item | What changed in the doc |
| --- | --- |
| 1. One 2031 bill | ARCA is division D; Title I heading is now "The rail account and contract authority"; lead paragraph rewritten; no standalone fund anywhere |
| 2. Architecture C | SEC. 101 rewritten: three accounts, FY2028 floors, 35 / 50 / 15 of the increment, renewal before expansion, rail subaccounts, aviation and diesel credited outside the split. Choice 3 table replaced. Mermaid flow redrawn |
| 3-4. Per-mile fee and yield basis | 1.0¢ FY2029 → 3.6¢ FY2042; the 2.4¢ = $44B anchor replaced with the FHWA vehicle-mile basis (2.4¢ ≈ $80B gross; receipts replaced at ~1.4¢) |
| 5. Highway denominator | H.R. 8870 levels and NHTSA/FMCSA now carried in the affordability text |
| 6. No $132B transfer | All seven mentions either removed or relabelled superseded; replaced by $93.20B mandatory expansion + $92.6B div. A sec. 110 renewal transfers |
| 7. Section 107 | Rewritten as continuation of every account's renewal programs at FY2035 levels; the $12B rail-only floor retired in the statute, the section-by-section table, the guarantee list, the phasing table and the fallback-tier list |
| 8. Section 108 | Expansion-first, not proportional; executed agreements exempt; sec. 106(e) expressly subject; sec. 106(b) obligation-limitation distribution made consistent |
| 9. 0.206% as a benchmark | Restated in the cap paragraph, the fit table, Choice 4 and SEC. 101(i). CBO-basis line added (FY2030 0.219%, FY2032-36 0.193-0.203%) |
| 10. Joint facilities | 30% transit-share placeholder deleted; movement-share rule and the Chicago 79% figure added; chapter 53 bar deleted with the old SEC. 101(d) |
| 11. Byrd rule | Greenfield capital moved from "barred in practice" to "available with obligation and expenditure deadlines" (ARP sec. 3401); the GF-transfer row reframed; both instructions now go to Finance and Ways and Means as well as Commerce |
| 12. 250-Plus | Rail table rebuilt with the four requested column labels; Corridor ID sunset extension traded away in three places; H.R. 8870's $26B of general-fund grants added with the benchmark question flagged |
| RRIF | "$50B as raised by H.R. 8870" in five places; secs. 10513 and 10515 and the Amtrak/compact/TOD/shipper eligibility added |
| Numbers restated | Affordability rows, dedicated-coverage rows, the fit table, the fee-sizing table, the scoring paragraph, and the self-financing claim (withdrawn) |

## Errors found during the pass, beyond the handoff list

- **Title II annual column was internally inconsistent.** Sec. 204's five-year figure had been corrected to $13.10B but its annual stayed at $3.00B, and the title total read $13.11B a year against a canonical $11.99B. Fixed sec. 203 ($5.90B → $4.70B / $0.94B), sec. 205 ($6.65B → $4.15B / $0.83B), sec. 204 annual ($3.00B → $2.62B) and the total ($11.99B).
- **Title III table was missing secs. 310, 311 and 312 entirely** — $38.20B of the title. Added, and sec. 303 corrected $40.00B → $55.00B. The table now sums to the canonical $160.45B.
- **The illustrative Tier 1 allocation still sums to $40.00B**, and the per-corridor cap of $14.0B was 35 percent of that. Flagged in the doc rather than re-derived: $15B is unallocated and the cap is a live choice (percentage, which rises to $19.25B, or fixed in dollars).
- **Coalition table was stale throughout** — sec. 201 at $24.8B against a canonical $27.00B, sec. 203 at $5.9B, and a Texas line downstream of the $40B Tier 1 allocation.
- **Non-federal match figure was stale.** With sec. 303 at $55B and a 50 percent share, the match is $55B not $40B, and total capital in motion $375-400B not $290-315B.
- **Aviation yield basis conflicted with itself.** The fee-sizing table priced $1 a segment at roughly $0.85B on 940 million 2031 enplanements at 1.5 percent growth; the model uses $0.70B on 696 million FY2025 enplanements at 2.15 percent. Reconciled onto the model's basis and the discrepancy stated.
- **"How self-financing is this" section** reported user fees at 13 percent in FY2031 rising to 30 percent by FY2035. Restated to 26 percent FY2032-36 and 50 percent by FY2042-46, with the highway (73-75 percent) and transit (58-63 percent) comparisons.
- **Section 106 still said "titles II through IX"** in two places after the bill grew to thirteen titles.
- **Section 106(e)'s retargeting to Tier 1 design maturity** was described in prose but absent from the statutory text. Written in as a 30 percent design threshold — this closes a long-flagged open item.

## The fiscal-year correction (applied second, 2026-10-12)

The ATRA chat caught the largest error in either bill: **the 2031 reauthorization authorizes FY2032-36, not FY2031-35.** BUILD America 250 runs FY2027-31 with FY2031 as its final year, so a bill enacted in 2031 starts the following fiscal year.

This was live in the model, not only in the prose. The old version had highways at H.R. 8870 levels through FY2031 while transit and rail were already at ARCA and ATRA levels in that same year, and the rail 250-Plus baseline covered only FY2027-30 — four years of a five-year bill. `index/tools/transportation/transit_fiscal_model.py` has been re-keyed and re-run; its header records the change. Periods are now FY2027-28, FY2029-31, FY2032-36, FY2037-41, FY2042-46.

**Treatment of the levels.** Authorization amounts are unchanged in nominal terms and now read as FY2032 dollars. They were not re-indexed: the bottom-up costing behind them was never dated to a precise dollar-year, and a 2.5 percent re-index would churn every table in both bills for a change well inside the estimating error on corridor capital. This is a declared assumption, not an oversight.

**What moved, on the arch C / scenario B base case:**

| Figure | Old (FY2031-35) | Corrected (FY2032-36) |
| --- | --- | --- |
| ARCA + ATRA draw, authorization period | 0.185% avg, 0.189% peak FY2033 | **0.174% avg, 0.177% peak FY2034** |
| Preceding period | FY2029-30: 0.194% avg | FY2029-31: **0.154% avg** (peak still 0.197% FY2030) |
| Second decade | 0.130% then 0.127% | **0.123% then 0.123%** |
| ARCA alone, authorization period | 0.130% | **0.122%** |
| On CBO's net-of-offset basis | 0.204-0.214% — over the benchmark in three of five years | **0.193-0.203% — under it in all five** |
| Headroom under the benchmark | $6.9-11.2B/yr | **$12.4-16.6B/yr** |
| Rail dedicated / general fund | $65.7B / $188.4B | **$68.3B / $185.8B** |
| Transit dedicated / general fund | $139.9B / $84.5B | **$147.2B / $77.2B** |
| Highway program / dedicated | $419.85B / $306.0B | **$430.35B / $316.25B** |
| 2031 bill total | $898.3B | **$908.8B** |
| Combined rail + transit envelope | $306.1B | **$313.7B** |
| Sec. 110 renewal transfers (hwy / transit / rail) | 113.9 / 51.0 / 95.2 | **114.1 / 43.7 / 92.6**, $250.4B in all |
| Equal-coverage incremental shares | 34 / 54 / 12 | **35 / 54 / 12** — highway's 35% now exactly right |

Two mechanisms do most of that work: one more year of nominal GDP growth in the denominator, and the per-mile fee standing one notch further up its ramp in every year of the bill — 1.6 cents in FY2032 where the old window assumed 1.4 cents in FY2031. **The correction makes the program materially more affordable, and retires the CBO-basis breach inside the bill's own window.**

**And it surfaced a new design gap.** The three-way split takes effect at the FY2028 forcing event, but transit and rail programs do not scale until FY2032. In FY2031 the Mass Transit Account's dedicated receipts ($24.9B) exceed its 250-Plus program ($20.7B), leaving **$4.19 billion with nowhere to go.** Division A has to dispose of it — carry it forward as an opening balance, or delay the split's effective date to FY2032 and forgo it. This is the defensible replacement for the superseded "$11 billion opening balance" claim, which came from the retired cash-flow model.

**Statutory dates shifted:** sec. 106(c)(1) commitments to FY2046; sec. 106(e)(3) lapse to September 30, 2036; sec. 107(a) continuation at FY2036 levels; the sec. 303 readiness window to 2034-2036. The sec. 205 ADA deadline stays at FY2036, which is now the bill's final year rather than one year past it. The FY2028 account floors in sec. 101(c)(1) are unchanged, as is the FY2045 statutory parity backstop — the glide path now reaches parity in FY2042 and beats it.

## The ATRA calendar prompt — checked item by item

Against `sources/transportation-calendar-fy2032-36.md`, items 1, 3 (model), 4 and 5 were already applied in the first pass. Items 2, 6 and 7, the name, and the revenue-schedule cells in the doc were not, and are now.

| Item | Status |
| --- | --- |
| 1. Relabel canonical and title tables FY2032-36 | Done — 14 relabels, nominal amounts by year unchanged |
| 2. FY2031 its own 250-Plus figure | **Done, and the number is $13.3B, not $13.7B** (see below) |
| 3. Aviation $4 FY2032 → $12 FY2036 → $16 cap FY2046; diesel 10¢/5¢ FY2030-31, 15¢/7.5¢ FY2032 | Done — model in the first pass, the Choice 2 table cells in this one |
| 4. Sec. 107 at FY2036, sec. 106 commitments to FY2046, reserve over FY2032-36, out-year rows | Done; the reserve's FY2032-36 release and the $7.4-11.6B residual headroom added |
| 5. Affordability and fit-table figures | Done. One correction: **ARCA alone FY2029-31 is 0.121%, not 0.122%** |
| 6. The FY2031 cliff and the Corridor ID sunset | Added |
| 7. Leave ARCA's validation rows on the original calendar | Handled, but by retiring rather than relabelling — see below |
| 8. Update this file | Done |
| The name | Added: ARCA is **division D of the Moving America Act of 2031** |

**ARCA's FY2031 250-Plus rail figure is $13.3 billion.** It is the residual of the delivered total in ARCA's own 250-Plus table: $59.6B across FY2027-31 less $46.3B delivered in FY2027-30 (10.5 / 11.0 / 11.9 / 12.9). The transit model's $13.7B came from rounding the delivered total to $60B. `index/tools/transportation/transit_fiscal_model.py` now carries $13.3B, which is also why **ARCA alone in FY2029-31 reads 0.121%, not the 0.122% in the calendar file** — that row is sensitive to the FY2031 rail baseline and nothing else.

**On item 7.** ARCA's original affordability rows (0.105 / 0.099 / 0.019 / 0.001) and dedicated-revenue rows ($9.4B / $83.7B / $165.9B / $244.5B) are retired from the doc rather than relabelled onto the new calendar. The calendar is not the reason: the method behind them froze highways and transit at CBO baseline outlays, skipped fuel-tax displacement, and counted no continuing general-fund appropriations for either, while the benchmark's numerator counts all three. A note in the doc records what they were, that they reproduce at 0.111 / 0.098 / 0.019 / 0.002 on ARCA's own method, and why the method was replaced. Nothing is lost, but anyone looking for the rows themselves will find the note instead.

## The 2026-bill discipline rule (Espen, 2026-10-12)

**Nothing in BUILD America 250-Plus may be sized to anything in these documents.** Lawmakers in December 2026 do not have the FY2032-46 program in front of them; the model does, and it kept leaking that knowledge backwards. Three consequences, now written into the ARCA doc's 250-Plus section:

1. **H.R. 8870 as written contains no general-fund transfer.** It authorizes contract authority against accounts CBO projects will run dry — highway in FY2028, transit in FY2027 — and does not fix them. The model's FY2027-31 general-fund column is an inference about what Congress would have to do later, mostly through annual appropriations, not a provision of any bill.
2. **The 250-Plus transfer ask stays at $108.0B** ($71.2B highway + $36.8B transit, CBO's shortfall through FY2030). This rejects the calendar file's recommendation to grow it to $147.7B now that FY2031 is 250-Plus's last year. A 2026 Congress patches to the cash in front of it, in increments, as it did repeatedly between 2008 and 2014.
3. **Nothing in FY2032-46 depends on the transfer's size.** The rail account's FY2029-31 receipts come from the per-mile fee enacted at the FY2028 forcing event, and the $4.19B accumulating in the Mass Transit Account in FY2031 is fee revenue. What the transfer size does affect is whether the highway and transit accounts are solvent on the day the Moving America Act starts — and if not, division A section 101(c)(1)'s FY2028 floors are credited against receipts already spoken for. **That risk is real and unmodelled.**

## Open questions carried into the merge

Ordered by how much each moves. The merge session is told to decide each one and flag it rather than stop; this is the list it works from.

1. **The FY2028 forcing event — the largest unverified premise in either bill.** Every reauthorization since 1982 has extended the expiring fuel taxes to at least the end of its own authorization period, and IIJA extended the HTF excises through September 30, 2028. A 2026 bill covering FY2027-31 would ordinarily push them to FY2031 or FY2032 — which deletes the FY2028 forcing event the whole revenue architecture rests on. If it goes: the per-mile fee starts FY2032, the rail account has no FY2029-31 receipts, "the account opens already funded" goes away along with the $4.19B transit balance, rail's FY2032-36 coverage falls well below 27 percent, and division A's revenue title becomes the first structural surface revenue bill rather than a reform of one. Carried as the base case because the FY2028 expiration is current law and the design is coherent on it. **Not modelled the other way. It should be before the bill is scored.** Full passage in the ARCA doc under "The largest unverified premise in this design."
2. **The transit/rail split and the incremental shares.** Drafted 35 / 50 / 15; equal renewal coverage in FY2042-46 solves to 34.7 / 53.7 / 11.6. The highway scoping may move it again.
3. **49 U.S.C. 5307 operating eligibility.** On the corrected calendar scenario C now *fits* under the benchmark (0.190% average, ~$5B a year of room), so the case for scenario B rests on policy — federal share, substitution risk, the trade-down dial — not on affordability. That is a change from the old calendar and should be decided on the policy grounds.
4. **Division structure and letters**, and how the highway division is carried: drafted, incorporated by reference, or hybrid.
5. **Division A sections 102, 103, 104, 106, 107, 110 and 111.** Sec. 111, per-mile administration, is the one most likely to decide whether the fee survives.
6. **The FY2031 cliff.** Rail ~$37B (FY2030) → $13.3B (FY2031) → $39.95B (FY2032); transit $40.2B → $20.70B. ~$48B of benchmark room in FY2031. Recommendation in the doc: the 2030 package carries availability through FY2031 with obligation and expenditure deadlines.
7. **The $4.19B trapped in the Mass Transit Account in FY2031.** Carry forward as an opening balance, or delay the three-way split to FY2032 and forgo it.
8. **The joint terminals.** Sec. 310's $20.20B against ATRA sec. 606's $6.00B over the same five nodes. Washington Union Station's commuter figures unverified; Atlanta has no intercity terminal.
9. **Whether H.R. 8870's $26B of general-fund grants count against the 0.206 percent benchmark.** $26B against $12-17B of annual headroom.
10. **The Tier 1 allocation and the per-corridor cap.** The illustrative table still sums to $40.00B against sec. 303's $55.00B; $15B unallocated, and the $14.0B cap was 35 percent of the old figure.
11. **The cash-flow model and a CBO-style score of divisions A and B.** Both superseded, neither replaced.
12. **Titles V-IX statutory text**, and sec. 302's formula and the sec. 310 project list under the joint-facility rule.

## What has to happen before ARCA and ATRA merge into one doc

*(Written before the calendar correction. Items 1-6 below still stand; the open-question list above is the current one.)*

Ordered by whether it blocks the merge or merely follows it.

### Blocking — the merged doc cannot be internally consistent without these

1. **Settle the transit/rail split and the incremental shares.** ARCA's $254.03B and ATRA's $224.42B were sized independently. The bill text says 35 / 50 / 15; the model's equal-renewal-coverage solution is 35 / 54 / 12. Division A section 110's renewal transfers ($114.1B / $43.7B / $92.6B) move with whichever is chosen. Everything downstream — coverage ratios, the benchmark table, the parity narrative — is keyed to this.
2. **Resolve the 49 U.S.C. 5307 operating-eligibility question.** ATRA scenario B ($35B tier) versus C ($70B tier) changes the combined draw from 0.174% to 0.190% in FY2032-36 and moves the split by about four points. It is the largest single unresolved variable in either bill.
3. **Decide the division structure, and what happens to highways.** ARCA is division D; ATRA presumably becomes B or C. But $430.35B of the $908.8B is the highway division and **nobody has drafted or scoped it.** Either the merged doc incorporates H.R. 8870's highway title by reference and says so plainly, or it is a surface transportation bill with a hole where 47 percent of the money sits. This is a structural decision, not a drafting task, and every cross-reference depends on it.
4. **Draft the remaining division A sections.** 101, 108 and 109 exist. Missing: 102, 103, 104, 106, 107, 110, 111. Division A is the merged bill's spine; it cannot open with seven placeholders. Section 111 (per-mile administration — Treasury collection, odometer-only reads, a bar on location data, State collection agreements, a 10 percent cost allowance) is both the hardest and the one most likely to decide whether the fee survives.
5. **Re-run the trust-fund cash-flow model.** Still on $185.43B, a standalone fund and the $143.0B/$132B transfer. In two separate docs this is a flagged gap; in one doc the fiscal section is shared, and a shared section cannot carry a superseded rail-only model.
6. **Produce one CBO-style score of divisions A and B.** The $115B ten-year deficit effect is withdrawn and nothing replaces it. Two documents can each flag the gap; one document needs the number.

### Should be done with the merge, not after

7. **Collapse the duplicated sections.** Both docs independently carry a fiscal-envelope section, a Byrd-rule analysis, a 250-Plus baseline section, a political-path section and a fallback-tier section. In one doc each must become one section, written once from both modes' figures — otherwise the merged doc contradicts itself in five places.
8. **Scope the joint terminals and set the sec. 310 / sec. 606 split project by project.** $20.20B and $6.0B currently describe the same five nodes from two sides. Separately that is an open item; together it is a visible double count. Washington Union Station's commuter figures are unverified and Atlanta has no intercity terminal to split.
9. **Re-point every cross-reference.** ARCA's internal "section 303" becomes "section 303 of division D," and ATRA's likewise. Mechanical, large, and worth scripting rather than doing by hand.
10. **Re-derive the Tier 1 allocation and the per-corridor cap at $55.00B**, and the coalition table's Texas line with it.

### Follows the merge

11. Titles V-IX of ARCA still need statutory text; sec. 302's formula and the sec. 310 project list need redrafting under the joint-facility rule.
12. Decide whether H.R. 8870's $26B of general-fund grants count against the 0.206 percent benchmark. $26B against $12-17B of annual headroom is not a rounding error.
13. The four artifacts — ARCA's corridor pipeline grid and network map, ATRA's delivery pipeline grid and system map — are two pairs that may or may not merge. The rail map's funding annotations still show sec. 303 at $40B and reference the old trust-fund structure; the grid notes still cite 49 U.S.C. 24911 rather than 24712(g)(2).
