# Revenue assignment audit

Oct 19, 2026 · Espen Swanson · live doc: https://claude.ai/code/artifact/2b824a7e-c87d-4b21-a1d0-411c000dfeb1

Filed in index/ because this audits the layer the ledger indexes — how the domain files assign revenue to claims — rather than setting policy. It is not generated from the domain files, so unlike the ledger it is edited by hand.

Seven overlaps sat in the files as of Oct 19; two were outright double-assignments of the same dollar, worth about $0.8T together. Findings 1, 2, 6 and 7 are now applied in the domain files. Findings 3, 4 and 5 are open.

## Scope and method

Audited as current sources: the Governing Decisions live doc (rev 100), the four batch 1 domain files, index/2029-trifecta-master-ledger.md (interim refresh, Oct 13 figures for uncovered domains), staging/unified-reform-inventory-current.md, domains/transportation-moving-america-act-2031-draft-2.md and domains/public-safety-safe-everywhere.md. The two source tables were read only where a domain file points at them.

An overlap here means one of four things:

1. **Double assignment.** One instrument's revenue is credited to two channels, or counted against two claims.
2. **Unpriced stacking.** Two instruments fall on the same tax base and neither score is reduced for the other.
3. **Invisibility.** An instrument's revenue or its outlay appears in no channel and no total, because it was netted to zero or because it sits outside the general fund.
4. **Orphan claim.** A cost a file acknowledges appears against no revenue.

Not checked: whether the underlying CBO, Treasury, JCT, SSA, TPC and CRFB scores are correctly stated or still current. This is an internal-consistency audit against D3, D4 and D7, not a re-sourcing of the figures. Arithmetic in the base and gap tables was recomputed; where it fails, that is reported below.

## Summary

| # | Overlap | Kind | Size (mid, $T) | Certain? | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | REV-H1b credited to Medicare HI in domain-health.md and to the general fund in domain-revenue.md | Double assignment | 0.50 | Yes | **Applied** in domain-health.md; staging inventory row 11.1 still stale |
| 2 | Carbon border adjustment inside REV-C1 and again as E4's "own revenue" | Double assignment | 0.30 | Likely | **Decided Oct 19** — carved out as REV-C2, financing E4 directly |
| 3 | HI holds about $1.2T against a stated need of $0.8-0.9T; the surplus is booked nowhere | Stranded revenue | 0.30 | Yes, as arithmetic | **Open** — needs D4's window for "kept whole" |
| 4 | SS-2, REV-H1b, G3 and G9 stack on high-income investment income; GX covers only G4, G6 and G9 | Unpriced stacking | 0.2-0.5 | Direction yes, size no | **Open** — recorded in the stacking section |
| 5 | Full Medicare Advantage capture funds a general-fund cut and HI's solvency on one unscored estimate | Concentration | 1.95 total | Estimate flagged in file | **Open** — needs a score |
| 6 | Three revenue streams appear in no channel; five more are netted to zero and disappear | Visibility | ~5 netted, 0.11 missing | Yes | **Applied** — accounting rule and ten channels in domain-revenue.md |
| 7 | Paid-leave general-fund backstop, and G8's vehicle risk | Orphan claim | 0.5 / 0.4 | Yes | G8 **decided**; backstop open |

Findings 1 and 2 were the only ones where the same dollar was spent twice, and both are now resolved. The rest are places where the channel design is sound but the arithmetic has no home.

## 1. REV-H1b was credited to two channels (applied)

The Oct 19 channel split moved REV-H1b (Medicare and net investment income rates to 5% above $400K) back to the general fund, because HLT-6's Medicare Advantage share plus REV-H1a already cover HI. domain-revenue.md carries that change and its $6.38T base includes H1b.

domain-health.md did not. Its "Financing by channel" section still read: "REV-H1 (the 5% Medicare and investment-income rate above $400K, plus closing the pass-through gap, about $1.0T) is credited to HI." Three bullets later the same file gave the current version. Both paragraphs were live in the same canonical file.

**Applied Oct 19:** domain-health.md now credits HI with REV-H1a plus the HLT-6 share only, keeps REV-H1b in the general-fund base, and carries a line recording what the superseded version said.

**Still open:** staging inventory row 11.1 carries the same stale split ("REV-H1 ... about $1.0T ... credited to Medicare HI") and the pre-split base total of $5.31 / 5.88 / 6.49T, which is exactly $0.50T below the current $5.81 / 6.38 / 6.99T. Row 11.1 is what the batch 2 files will read, so it should be corrected before they are sized.

## 2. The carbon border adjustment was counted twice (decided)

REV-C1's design included a border adjustment on imports, and its $1.35-1.6T gross was the fee including it. Under D7 that gross split 80/20: about $1.16T to the dividend, about $0.29T to transition and the Thriving Economy add-ons.

Ledger E4 then said it was paid by the 20% carbon share plus "its own revenue" of about $0.3T. The Thriving Economy map's own revenue is the border adjustment and methane fees, $120-240B. The staging inventory spotted this at row 10.3 and nothing downstream acted on it. E4 netted to $0.01T only because roughly $0.6T of financing was assumed against roughly $0.6T of add-ons.

**Decided Oct 19: carve it out.** The border adjustment leaves REV-C1 and becomes **REV-C2**, its own channel, financing the Thriving Economy add-ons directly.

| | Before | After |
| --- | --- | --- |
| REV-C1 gross | $1.35-1.6T (mid $1.45T) | $1.20-1.35T (mid $1.25T) |
| Dividend (80%) | ~$1.16T | ~$1.00T |
| Transition share (20%) | ~$0.29T | ~$0.25T |
| REV-C2 border adjustment | inside REV-C1, and again in E4 | ~$0.20T, counted once, to E4 |
| E4 financing | ~$0.29T + ~$0.3T double-counted | ~$0.25T + ~$0.20T + methane fees |

**Why this over the alternative.** Folding the border adjustment into REV-C1 and trimming the add-ons to the 20% share would have added about $0.30T to the general-fund gap, because the add-ons would have had to find financing elsewhere. The carve-out resolves the double count with **no effect on the general-fund gap** — the same dollars move from the dividend to the add-ons, inside the carbon channel. The rejected option is recorded in domain-revenue.md's options-not-chosen table.

**What it costs.** The dividend falls by about $0.16T over ten years, roughly $48 a person a year or $120 for a household of 2.5. That is a distributional cost, not a fiscal one, and it lands on the quintile the D3 test is least sure about. It tightens the fourth quintile twice: a smaller dividend, and the border adjustment's pass-through now sitting on the cost side with no rebate behind it. Both are written into domain-revenue.md's first-pass table and must be carried into the incidence model.

**Knock-on.** D7 states the carbon gross as $1.35-1.6T with about 80% rebated, a figure that included the border adjustment. The live Governing Decisions doc was updated Oct 19 to show the two instruments separately; the two still sum to $1.35-1.6T. The project copy at governing/ needs re-filing from the live doc.

**Open:** the $0.15-0.25T split between the border adjustment and methane fees is an estimate from a combined Thriving Economy figure. Sizing the two separately would firm up both REV-C2 and E4.

**Watch item.** Safe Everywhere's revenue package counts savings from ending domestic military deployments, and staging inventory row 5.10 notes that is one statute referenced from both Safe Everywhere and the executive-power file. If the batch 2 executive-power file books those savings too, that is a third double-assignment. Those savings also sit inside a defense envelope D9 already holds flat, so they are not new money unless the envelope drops.

## 3. Medicare HI holds more than it needs ($0.30T, open)

HI receives REV-H1a (~$0.50T) plus its share of HLT-6 (~$0.70T, range $0.5-0.9T) — about $1.20T against a stated need of $0.8-0.9T over 2030-39.

The surplus did one job: it is the stated reason REV-H1b returned to the general fund. Having done that it disappears. It is not swept back, not held as a named reserve, and not counted in the $9.53T of claims or the $6.38T base.

The ambiguity is in D4. "Existing dedicated funds kept whole" does not say over what window. Against the ten-year need HI is over-funded by $0.3T; against the 0.56%-of-payroll 75-year gap, $1.2T over ten years is not obviously too much, because the HI shortfall grows after the window. The files never say which test applies.

The $0.8-0.9T need is derived from the $85-100B annual shortfall, not from 0.56% of payroll as the basis tag implies. The two reconcile because HI's taxable payroll is uncapped and therefore much larger than OASDI's; applied to OASDI payroll the same percentage gives roughly $0.65T and a visibly larger surplus. That derivation is now written into domain-health.md.

**Fix:** state the window D4 keeps a fund whole on. Ten years means crediting less of HLT-6 to HI and moving the difference to the general fund, which shrinks the gap. Seventy-five years means recording the surplus as intentional.

## 4. High-income investment income carries four instruments, three haircut (open)

REV-GX takes 15% off G4, G6 and G9, which is exactly the −$0.41T in the base. Nothing is taken off the larger collision the revenue file documents two sections earlier.

| Instrument | Channel | Mid ($T) | Falls on |
| --- | --- | --- | --- |
| G3 | General fund | 0.30 | Ordinary income above $400K |
| G9 | General fund | 1.45 | 2025-cut reversal above $450K |
| REV-H1b | General fund | 0.50 | Investment income above $400K |
| SS-2 | Social Security trust fund | 1.10 | Investment income above $400K |

The revenue file's stacking table puts the combined federal statutory rate on interest and ordinary investment income above $400K at about 57%, near 70% with California's top rate, and names the risk: past the peak, avoidance eats the scored revenue. Neither SS-2's score nor H1b's is reduced for the other.

Two consequences. The general fund is probably over-booked by some fraction of $0.5T. More seriously under D4, the haircut that exists sits only in the general fund, so an avoidance response on the same base would cut trust-fund revenue that nothing protects. SS-2 is 29-36% of the D8 baseline's gap closure; if its yield comes in low, the closer D8 still has to choose gets larger.

**Fix:** extend a GX-style adjustment across channels, or score SS-2 and H1b jointly. The revenue file already lists the design levers (SS-2 at 6.2%, dropping H1b, phasing SS-1 from $400K); each needs re-scoring with behavior before the gap is treated as settled.

## 5. Medicare Advantage capture carries two channels on one estimate (open)

Full MA capture cuts general-fund health costs by ~$1.25T, supplies HI with ~$0.70T, and is most of why the D6-trimmed package scores $1.2T below the go-big bill as written. The first two are different dollars and the third restates them, so this is not a double count.

It is a concentration. The incremental capture over the go-big baseline ($0.6-1.1T) is an estimate, and the 42% Part A split is an estimate. Together they carry a general-fund saving and a trust fund's solvency. If capture lands at the low end, the general fund loses and HI's cushion goes with it in the same stroke. No other row has that property.

**Fix:** nothing structural, but this is the one row where a real score changes more than its own number. It belongs at the top of the scoring queue with the Child Tax Credit. Now flagged in domain-health.md.

## 6. Revenue that is real but invisible (applied)

The stated rule is that trust-fund revenues and outlays are counted separately from general-fund inflows and outflows. The rule as applied had drifted into something weaker: if an instrument does not touch the general fund, it stops being shown at all. Separate accounting and no accounting are not the same thing.

| Channel | Revenue visible? | Outlays visible? | Where it fails |
| --- | --- | --- | --- |
| Social Security | Yes (O1, O2) | Partly | F5's net of −$2.75T mixes trust-fund revenue and benefit cost in one cell |
| Medicare HI | Yes (H1a) | No | HI's share of HLT-6 is named in prose, never as a row |
| Paid leave | Yes (P1) | No | FAM-3 nets to zero; the $0.9T of benefits never appears |
| Carbon fee | Yes (C1) | Partly | The dividend sits inside E2 as a net of zero |
| Carbon border adjustment | Was inside C1 | No | Now REV-C2, a channel of its own (finding 2) |
| Surface transportation | Yes (MR1-MR6) | Partly | M1 and M2 show as net deficit reduction; the $290B and $95B of receipts and the packages they fund are collapsed |
| Public safety | No | Partly | About $11B a year of alcohol tax, fraud assessment and firearms charges appears nowhere; S5 shows cost only |
| Competition | No | n/a | Merger-filing fees fund E9; E9 nets to zero by assumption |
| Small-dollar matching | No | Partly | The fines surcharge funds DEM1's 6:1 match; the surcharge is named in a note and nowhere else |

Three channels had no row of any kind. The partial failures are the more common problem: netting. An instrument that raises money and spends it in the same channel collapses to one net figure, usually zero, and both halves disappear at once.

Netting also makes the agenda look smaller than it is. Add the channels back at gross and it moves roughly $5T beyond the general fund's $9.53T: ~$3.0T of Social Security revenue, $1.2T into HI, $0.9T of leave contributions and benefits, $1.25T of carbon fee and $1.00T of dividend, $0.20T of border adjustment, ~$0.5T of transportation receipts. None belongs in the general-fund gap; all of it lands on identifiable households, and five of the ten channels reach the middle directly. Instruments netted out of the ledger are the ones most likely to be missed when the D3 incidence model is built.

**Applied Oct 19:** the accounting rule is written into domain-revenue.md's chosen-design section, the channel table runs ten rows with gross sizes, and the outlays the rule now owes are listed beneath it.

**Still open:** merger fees, the fines surcharge and methane fees are unsized, and the ledger's gross revenue and gross outlay columns wait on the rebuild.

## 7. Orphan claims

**The paid-leave backstop (open).** FAM-3 nets to about zero: $0.9T of cost against $0.9T from the 0.6% contribution. But cost runs $0.6-1.4T against revenue of $0.85-0.95T, and the design gives the fund a general-fund backstop for higher-than-expected take-up. At the high end that is roughly $0.45-0.5T of general-fund claim in no total. The file's own sourcing makes this the likely case rather than the tail: JCT's break-even is 0.85% of wages at FMLA take-up and the file notes higher take-up assumptions run far above that. The chosen rate is 0.6%. FAM-3D (12 weeks at 0.85%) is already drafted and would close it.

**G8's vehicle risk (decided).** IRS enforcement sits in the base at $0.4T with the ledger's note that it is "scored as revenue only in some vehicles." CBO conventionally does not credit enforcement revenue in reconciliation, so $0.4T of the base may be unavailable in precisely the vehicles the base is meant to pay for.

*Decided Oct 19:* G8 counts in the base, carrying a note that CBO may not score it as revenue. domain-revenue.md now says so on the row and under the base table, adds that G8 should not be the last $0.4T of a pay-for, and records that G8 moves with the IRS share of the D9 rebuild line (cost in Ledger A1, revenue in G8). "Quote the base at $5.98T excluding G8" is filed as not chosen.

## The published range does not reproduce

The midpoints reconcile cleanly. The range does not, and two live conclusions rest on it.

**What checks out.** The base total of $5.81 / 6.38 / 6.99T sums correctly across all eleven rows including GX. General-fund claims of $9.53T reconcile to the by-vehicle table ($3.29 + $3.90 + $1.73 + $0.01 + $0.61 = $9.54T). The gap of $3.15T is right. The closing path is right: $0.62 + $1.25 + $0.67 + $0.30 + $0.10 = $2.94T, plus C21's $0.25T and C22's $0.07T, giving −$0.11T as stated.

**What does not.** Summing the ledger's low column across general-fund rows gives about $9.4T, not the stated $6.13T. The high column gives about $17.3T, not $13.91T. Neither bound rebuilds from the published table.

Seven rows use low and high for something other than a range, and in each the midpoint falls outside its own bounds:

| Row | Net (mid) | Low | High | What the columns appear to hold |
| --- | --- | --- | --- | --- |
| F3 paid leave | 0.00 | 0.60 | 1.40 | Gross cost, before the contribution |
| F5 Social Security | −2.75 | 0.15 | 0.35 | Benefit cost only; the −2.75 is trust-fund revenue |
| E2 carbon fee | 0.00 | 1.16 | 1.16 | The dividend, not a range |
| E4 add-ons | 0.01 | 0.30 | 1.00 | Gross add-on cost |
| S5 Safe Everywhere | 0.01 | 0.11 | 0.14 | Ten-year cost; the 0.01 looks like an annual figure |
| M1 Moving America 2029 | −0.03 | 0.26 | 0.26 | Spending, not net |
| M2 Moving America 2030 | −0.00 | 0.09 | 0.09 | Spending, not net |

Each is a row where a gross figure and a net figure both exist and the table has three columns to hold them. Defensible per row, unusable in aggregate.

**Why it matters.** Both domain-revenue.md and the ledger argued that "the high end of the cost range ($13.9T) is not closed by anything short of a broad-based tax." That is the argument for keeping a VAT or an uncapped payroll contribution on the menu, and it rests on a bound that cannot be derived from the table beneath it. It may well be right — a genuine high case built from real per-row highs plausibly does exceed what top-end revenue can reach — but as it stands the conclusion is unauditable, and under the project's own rule a range is a number.

**Fix:** split gross and net into separate columns at the rebuild, or flag rows whose low and high are not bounds, then restate the range. Until then treat $6.1-13.9T as an assertion and the midpoints as the only figures that audit. domain-revenue.md now carries that caveat.

## Net effect on the gap

| Adjustment | Effect on the $3.15T gap |
| --- | --- |
| Finding 1, domain-revenue.md's version standing (applied) | 0 |
| Finding 2, border adjustment carved out as REV-C2 (decided) | 0 to the general fund; −$0.16T of dividend |
| Finding 3, HI swept to a ten-year need | −0.30 |
| Finding 6, channels made visible (applied) | 0 to the general fund |
| Finding 7, paid-leave backstop at the high case | +0.45 |
| Finding 7, G8 unscorable on its vehicle | +0.40 |
| **Adjusted gap, bad case** | **about 3.7** |
| **Adjusted gap, good case** | **about 2.85** |

The recommended closing path raises about $2.94T. It clears the good case and falls roughly $0.75T short of the bad one. The path's headroom is thinner than the −$0.11T in the ledger suggests, because two of these risks are not in the range at all. The REV-C2 decision took the largest of them off the fiscal side and moved it onto the distributional side, where the incidence model now has to carry it.

## What is left to do

1. **Staging inventory row 11.1** — still carries the superseded REV-H1 split and the pre-split base total. Correct before batch 2 files are sized.
2. **Governing Decisions** — the live doc's D7 now shows REV-C1 and REV-C2 separately; the project copy at governing/ needs re-filing from it, and the live doc's hierarchy table and embedded draft instructions still use the old `claude/` paths.
3. **Ledger rebuild** — revenue rows on the $6.38T base; REV-C1 at $1.25T with a $1.00T dividend; a REV-C2 row at $0.20T financing E4; gross revenue and gross outlay columns per channel; and the restated range. Generated from code, not editable here.
4. **Decisions that are yours** — D4's window for "kept whole," whether FAM-3 moves to the 0.85% break-even rate, and whether to build the incidence model now.
5. **Scores** — incremental MA capture with its 42% Part A split, the Child Tax Credit against current law, and the border adjustment separated from methane fees. 

## What this does not touch

The channel architecture holds up. One fund per permanent benefit with a natural stream, the general fund for everything else, no new trust funds for pay-fors — applied consistently, and both genuine double-assignments came from edits that landed in one file and not its neighbours, not from the design. The GX row shows the project already knows how to price an overlap; the gap is that it has only been done once, inside a single channel.

The household net test remains the binding constraint on the closing path and still needs the incidence model. The REV-C2 decision changes two of its inputs, so the model should be built on the post-carve-out figures: a $1.00T dividend, and a border-adjustment pass-through counted as a cost with no rebate behind it.
