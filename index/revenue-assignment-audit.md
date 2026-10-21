# Revenue assignment audit

Oct 20, 2026 · Espen Swanson · live doc: https://claude.ai/code/artifact/2b824a7e-c87d-4b21-a1d0-411c000dfeb1

Filed in index/ because this audits the layer the ledger indexes — how the domain files assign revenue to claims — rather than setting policy. It is not generated from the domain files, so unlike the ledger it is edited by hand.

The audit found seven overlaps; two were outright double-assignments of the same dollar, worth about $0.8T together. Findings 1, 2, 3, 4, 6 and 7 are resolved in the domain files and the ledger. Finding 5 (Medicare Advantage capture resting on one estimate) is open and waits on a score; G8's vehicle risk is the one risk still outside the ledger's range.

## Scope and method

Sources: the governing decisions (governing/project-2050-governing-decisions.md), the domain files, index/2029-trifecta-master-ledger.md, staging/unified-reform-inventory-current.md, domains/transportation-moving-america-act-2031-draft-2.md and domains/public-safety-safe-everywhere.md. The two source tables were read only where a domain file points at them. Figures are the ledger's current midpoints over 2030-39 in $T.

An overlap here means one of four things:

1. **Double assignment.** One instrument's revenue is credited to two channels, or counted against two claims.
2. **Unpriced stacking.** Two instruments fall on the same tax base and neither score is reduced for the other.
3. **Invisibility.** An instrument's revenue or its outlay appears in no channel and no total, because it was netted to zero or because it sits outside the general fund.
4. **Orphan claim.** A cost a file acknowledges appears against no revenue.

Not checked: whether the underlying CBO, Treasury, JCT, SSA, TPC and CRFB scores are correctly stated or still current. This is an internal-consistency audit against D3, D4 and D7, not a re-sourcing of the figures. Arithmetic in the base and gap tables was recomputed; where it fails, that is reported below.

## Summary

| # | Overlap | Kind | Size (mid, $T) | Certain? | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | REV-H1b credited to Medicare HI in domain-health.md and to the general fund in domain-revenue.md | Double assignment | 0.50 | Yes | **Resolved**: H1b is in the general-fund base only |
| 2 | Carbon border adjustment inside REV-C1 and again as CLI-5's "own revenue" | Double assignment | 0.30 | Likely | **Resolved**: carved out as REV-C2, financing CLI-5 directly |
| 3 | HI holds about $1.2T against a stated need of $0.8-0.9T | Stranded revenue | 0.30 | Yes, as arithmetic | **Resolved**: D4 keeps HI whole on a 75-year window; the ~$0.3T is HI's reserve |
| 4 | SS-2, REV-H1b, G3 and G9 stack on high-income investment income | Unpriced stacking | 0.2-0.5 | Direction yes, size no | **Resolved**: 15% haircut on H1b (inside GX) and on SS-2 (OX); a joint behavioral score is still wanted |
| 5 | Full Medicare Advantage capture funds a general-fund cut and HI's solvency on one unscored estimate | Concentration | 1.95 total | Estimate flagged in file | **Open**: needs a score |
| 6 | Channel revenue and outlays netted to zero or shown nowhere | Visibility | ~7 at gross | Yes | **Resolved**: the ledger shows every channel at gross |
| 7 | Paid-leave general-fund backstop, and G8's vehicle risk | Orphan claim | 0.5 / 0.4 | Yes | Backstop **replaced** (step-up and repayable loan); G8 **decided**, risk outside the range |

Findings 1 and 2 were the only ones where the same dollar was spent twice, and both are resolved. The rest were places where the channel design is sound but the arithmetic had no home.

## 1. REV-H1b is credited to the general fund only (resolved)

REV-H1b (Medicare and net investment income rates to 5% above $400K, about $0.50T) sits in the general-fund base, because HLT-6's Medicare Advantage share plus REV-H1a already cover HI. The audit found domain-health.md still crediting the combined REV-H1 (about $1.0T) to HI while domain-revenue.md counted H1b in the base.

**Current arrangement:** domain-health.md credits HI with REV-H1a (about $0.50T) plus HI's share of HLT-6 (about $0.70T) only, and keeps REV-H1b in the general-fund base, as domain-revenue.md does. The base is $5.71 / 6.37 / 7.12T including H1b, and staging inventory row 11.1 carries the same split.

## 2. The carbon border adjustment is counted once (resolved)

REV-C1's original design included a border adjustment on imports, and the Thriving Economy add-ons (now CLI-5) also counted the border adjustment and methane fees as "their own revenue." The same dollars sat in the dividend's base and in CLI-5's financing.

**Current arrangement:** the border adjustment is **REV-C2**, its own channel, financing CLI-5 directly.

| | Current (mid, $T) | Note |
| --- | --- | --- |
| REV-C1 gross | 1.35 (1.20-1.50) | Domestic fee, $25 a ton in 2030 rising to ~$100 by 2037; road fuels exempt (D7) |
| Dividend (80%) | 1.08 | CLI-2 |
| Transition share (20%) | 0.27 | To CLI-5 |
| REV-C2 border adjustment | 0.20 (0.15-0.25) | Counted once, to CLI-5; includes methane and industrial fees |
| CLI-5 financing | 0.27 + 0.20 = 0.47 | Against ~$0.60T of add-ons; the ~$0.13T residual is on the general fund, and C37 borrows ~$0.10T of its capital lines |

**Why this over the alternative.** Folding the border adjustment into REV-C1 and trimming the add-ons to the 20% share would add about $0.30T to the general-fund gap, because the add-ons would have to find financing elsewhere. The carve-out resolves the double count with **no effect on the general-fund gap** — the same dollars move from the dividend to the add-ons, inside the carbon channel. The rejected option is recorded in domain-revenue.md's options-not-chosen table.

**What it costs.** Keeping the border adjustment out of the dividend's base means about $0.16T less dividend over ten years (80% of REV-C2), roughly $48 a person a year or $120 for a household of 2.5. That is a distributional cost, not a fiscal one, and it lands on the quintile the D3 test is least sure about: the fourth quintile gets a smaller dividend and bears the border adjustment's pass-through with no rebate behind it. The incidence model carries both (the $1.08T dividend, and REV-C2 as a full pass-through cost).

**Governing doc.** D7 shows the two instruments separately: REV-C1 (~$1.35T) and REV-C2 (~$0.20T), with about 80% of REV-C1 rebated.

**Open:** REV-C2's $0.15-0.25T is scaled from a combined Thriving Economy figure for the border adjustment and methane fees, so methane fees are not additional money unless REV-C2 is re-sized. Sizing the two separately would firm up both REV-C2 and CLI-5.

**Deployment savings.** Safe Everywhere's revenue package once counted savings from ending domestic military deployments. Those savings sit inside a defense envelope NSC-1 holds flat, so domain-public-safety.md drops them from PS1 unless NSC-1 is cut by the same amount; they are not counted as public-safety revenue anywhere.

## 3. Medicare HI holds more than its ten-year need (resolved)

HI receives REV-H1a (~$0.50T) plus its share of HLT-6 (~$0.70T, range $0.5-0.9T) — about $1.20T against a ten-year need of $0.8-0.9T over 2030-39.

D4 keeps HI whole on a **75-year window**, the Trustees' standard and the basis of the 0.56%-of-payroll gap, because the HI shortfall grows after 2039. Against that window $1.2T over ten years is not too much. **Current arrangement:** the roughly $0.3T above the ten-year need is HI's reserve, not swept to the general fund and not counted in the $10.97T of claims or the $6.37T base. It also hedges finding 5: if Medicare Advantage capture lands low, HI's share falls toward $0.5T and the reserve absorbs it.

The $0.8-0.9T need is derived from the $85-100B annual shortfall, not from 0.56% of payroll directly. The two reconcile because HI's taxable payroll is uncapped and therefore much larger than OASDI's; applied to OASDI payroll the same percentage gives roughly $0.65T. domain-health.md carries that derivation.

## 4. High-income investment income carries four instruments, all haircut (resolved)

| Instrument | Channel | Mid ($T) | Falls on |
| --- | --- | --- | --- |
| G3 | General fund | 0.30 | Ordinary income above $400K |
| G9 | General fund | 1.45 | 2025-cut reversal above $450K |
| REV-H1b | General fund | 0.50 | Investment income above $400K |
| SS-2 | Social Security trust fund | ~1.1 before OX | Investment income above $400K |

The revenue file's stacking table puts the combined federal statutory rate on interest and ordinary investment income above $400K at about 57%, near 70% with California's top rate, and names the risk: past the peak, avoidance eats the scored revenue.

**Current arrangement:** GX takes 15% off G11, G6, G9 and H1b (−$0.495T, in the base), and OX takes the same 15% off SS-2 inside the Social Security channel, so the haircut covers both channels and an avoidance response on the shared base no longer falls unpriced on the trust fund. The ledger's dynamic sensitivity (DY1) adds a separate, unsummed reading of the same risk across the top-end base.

**Still wanted:** a joint score of SS-2 and H1b with behavior. SS-2 is 29-36% of the D8 baseline's gap closure; if its yield comes in low, the closer D8 still has to choose (SS-5 recommended) gets larger. The revenue file lists the design levers (SS-2 at 6.2%, dropping H1b, phasing SS-1 from $400K).

## 5. Medicare Advantage capture carries two channels on one estimate (open)

Full MA capture cuts general-fund health costs by ~$1.25T, supplies HI with ~$0.70T, and is most of why the D6-trimmed package scores $1.2T below the go-big bill as written. The first two are different dollars and the third restates them, so this is not a double count.

It is a concentration. The incremental capture over the go-big baseline ($0.6-1.1T) is an estimate, and the 42% Part A split is an estimate. Together they carry a general-fund saving and a trust fund's solvency. If capture lands at the low end, the general fund loses and HI's cushion goes with it in the same stroke. No other row has that property.

**Fix:** nothing structural, but this is the one row where a real score changes more than its own number. It belongs at the top of the scoring queue with the Child Tax Credit. domain-health.md flags it.

## 6. Every channel is shown at gross (resolved)

The rule is that trust-fund and other dedicated-channel revenues and outlays are counted separately from general-fund inflows and outflows — separately, not left out. The audit found the rule had drifted into "if it does not touch the general fund, it is not shown," and that netting collapsed instruments that raise and spend money in the same channel into one figure, usually zero.

**Current arrangement:** the accounting rule is written into domain-revenue.md's chosen design, and the ledger shows each channel's revenue and outlays at gross, apart from the general-fund gap.

| Channel | Revenue (mid, $T) | Outlays (mid, $T) | Where it shows |
| --- | --- | --- | --- |
| Social Security | 2.83 | 0.25 | SS-1 row and the channel table (D8 baseline) |
| Medicare HI | 1.20 | 0.85 | H1a row; HLT-6's Part A share; channel table (finding 3) |
| Paid leave | 0.90 | 0.90 | P1 row and FAM-3's gross outlay |
| Carbon fee | 1.35 | 1.35 | C1 row; CLI-2's $1.08T dividend plus the $0.27T transition share |
| Carbon border adjustment | 0.20 | 0.60 | C2 row; CLI-5's gross add-ons, residual to the general fund (finding 2) |
| Surface transportation | 0.39 | 0.39 | MR1-MR6 receipts; MOV-29 and MOV-30 general-fund top-ups counted separately |
| Public safety | 0.09 | 0.12 | PS1 row; SAF-10's gross outlay, residual (~$2.9B a year) to the general fund |
| Merger review | 0.004 | 0.004 | MF1 row; funds an equal enforcement increase (COM-2) |
| Immigration fees | 0.015 | 0.015 | IF1 row (IMM-2) |
| Small-dollar matching | — | — | No channel: INT-5B pays the match from general revenue, inside DEM-1's general-fund row |

Netting also made the agenda look smaller than it is. At gross the channels carry about $7.0T of revenue beyond the general fund's $10.97T of claims. None belongs in the general-fund gap, but all of it lands on identifiable households, and the payroll, carbon, fuel-tax and alcohol channels reach the middle directly. The incidence model takes each of them as a row.

**Still open:** methane fees are not sized apart from REV-C2 (finding 2).

## 7. Orphan claims

**The paid-leave backstop (replaced).** FAM-3 nets to about zero on the general fund: $0.9T of cost against $0.9T from the 0.6% contribution, but cost runs $0.6-1.4T, and JCT's break-even is 0.85% of wages at FMLA take-up. An open general-fund backstop for high take-up would have been a $0.45-0.55T claim in no total. **Current arrangement (FAM-3A):** the contribution steps up automatically by 0.05 points when the fund's reserve falls below a year of benefits, to a cap of 0.85% (about $1.28T at the cap, estimate); only the very high case (about $0.12T) needs a bridge, a repayable Treasury loan to the fund. There is no general-fund backstop.

**G8's vehicle risk (decided).** IRS enforcement sits in the base at $0.4T with the ledger's note that CBO may not score it as revenue on a given vehicle. CBO conventionally does not credit enforcement revenue in reconciliation, so $0.4T of the base may be unavailable in precisely the vehicles the base is meant to pay for.

**Current arrangement:** G8 counts in the base, carrying that note on the row and under the base table; G8 should not be the last $0.4T of a pay-for, and it moves with the IRS share of CAP-7 (cost in CAP-7, revenue in G8). Whether G8 is net of CAP-7's IRS allocation is unchecked. Quoting the base without G8 is filed as not chosen.

## The published range

The midpoints and the range both reconcile.

**What checks out.** The base total of $5.71 / 6.37 / 7.12T sums correctly across its rows including GX. General-fund claims of $10.97T reconcile to the by-vehicle table ($3.58 + $4.29 + $1.46 + $1.16 + $0.48 = $10.97T). The gap of $4.60T is right. The closing path is right: accepted revenue of $3.53T (Package B: C18 $0.62T, C35 $0.15T, C19b $0.66T, C20 $0.67T; C38 $0.89T; C39-C41 $0.54T) plus $1.15T of borrowing inside the D4-B envelope (C21, C30, C31, C32, C37 and C42), giving −$0.08T.

**How the range is built.** The ledger shows each row's gross outlay and own (channel) revenue in their own columns, and its general-fund low and high columns are true bounds, so the range rebuilds from the table: claims of $7.68T to $15.42T and a gap of $0.56T to $9.71T, a stress bound that takes every row's high at once. The rows the audit found using low and high for gross figures now read:

| Row | Gross outlay mid (range) | Own revenue (channel) | General fund mid (low-high) |
| --- | --- | --- | --- |
| FAM-3 paid leave | 0.90 (0.60-1.40) | 0.90 (paid-leave fund) | 0.00 (0.00-0.00) |
| SS-1 Social Security | 0.25 (0.15-0.35) | 3.00 (Social Security trust fund) | 0.00 (0.00-0.00) |
| CLI-2 Climate Dividend | 1.08 (0.96-1.20) | 1.35 (carbon fee) | 0.00 (0.00-0.00) |
| CLI-5 add-ons | 0.60 (0.30-1.00) | 0.47 (carbon border adjustment) | 0.13 (0.00-0.61) |
| SAF-10 Safe Everywhere | 0.12 (0.11-0.14) | 0.09 (public safety) | 0.03 (0.01-0.06) |
| MOV-29 Moving America 2029 | 0.26 (0.26-0.26) | 0.29 (surface transportation) | 0.26 (0.26-0.26) |
| MOV-30 Moving America 2030 | 0.09 (0.09-0.09) | 0.095 (surface transportation) | 0.09 (0.09-0.09) |

**Why it matters.** The claim that the high end of the cost range can be closed only by a broad-based tax is the argument for keeping a VAT or an uncapped payroll contribution on the menu. With the range built from real per-row bounds, that claim can be tested against the $9.71T stress-bound gap; the midpoints remain the planning figures.

## Net effect on the gap

| Adjustment | Effect on the −$0.08T after accepted options |
| --- | --- |
| Finding 1, H1b in the general fund only | 0 |
| Finding 2, border adjustment as REV-C2 | 0 to the general fund; about −$0.16T of dividend |
| Finding 3, HI's ~$0.3T kept as reserve (75-year window) | 0 (not available to sweep) |
| Finding 6, channels shown at gross | 0 to the general fund |
| Finding 7, paid-leave step-up and repayable loan | 0 |
| Finding 7, G8 unscorable on its vehicle | +0.40 |
| **Adjusted gap, bad case** | **about +0.32** |
| **Adjusted gap, good case** | **about −0.08** |

The accepted path clears the good case and falls about $0.32T short of the bad one; G8 is the one risk outside the ledger's range. The REV-C2 carve-out took the largest of the original risks off the fiscal side and onto the distributional side, where the incidence model carries it. The ledger's conventional dynamic sensitivity (about −$0.56T, unsummed, since D4 counts no dynamic revenue) is a separate reading of the top-end base's risk.

## What is left to do

1. **Scores** — incremental MA capture with its 42% Part A split (finding 5), and the Child Tax Credit against current law.
2. **Joint score** — SS-2 and REV-H1b with behavior (finding 4).
3. **G8** — whether it is net of CAP-7's IRS allocation, and which vehicle can score it (finding 7).
4. **REV-C2** — size the border adjustment and methane fees separately (finding 2).

## What this does not touch

The channel architecture holds up. One fund per permanent benefit with a natural stream, the general fund for everything else, no new trust funds for pay-fors — applied consistently, and both genuine double-assignments came from edits that landed in one file and not its neighbours, not from the design. GX and OX show the project prices an overlap across channels.

The household net test remains the binding constraint on the closing path. The incidence model is built on the post-carve-out figures (a $1.08T dividend, and the border adjustment's pass-through counted as a cost with no rebate behind it); on scenario Q every income group below the top comes out ahead, with the fourth quintile at about +$1,114 a year.
