# Domain file: Health (HLT)

Canonical. This file applies Governing Decision D6 to the go-big bill. sources/health-go-big-bill-detail-and-financing.md stays as the provision-level source and the household tables. All figures are ten-year totals for 2030-39 in trillions; ranges come from the go-big tab unless tagged estimate.

## Chosen design: the go-big bill, trimmed (D6, option B)

| ID | Title | Main provisions | Low | Mid | High | Vehicle | Floor days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HLT-1 | Restore | Repeal the H.R. 1 Medicaid and marketplace cuts; make the enhanced ACA credits permanent; close the coverage gap | 2.25 | 2.45 | 2.65 | R1 | 0 |
| HLT-2 | Medicare upgrades | $5,000 cap in traditional Medicare; dental, vision and hearing (kept in); physician pay indexed. **No eligibility change** | 0.90 | 1.07 | 1.24 | R2 | 0 |
| HLT-3 | Public option guarantee | Medicare-rate public plan on and off the marketplaces; automatic enrollment; richer cost-sharing help; the firewall removed | 1.60 | 1.90 | 2.20 | Regular order | 8 |
| HLT-4 | Medicaid, long-term care, safety net | HCBS down payment and care workforce; children's continuous coverage; Medicaid dental; health centers doubled; 14,000 residency slots; Momnibus; Title X | 0.40 | 0.63 | 0.85 | R1 | 0 |
| HLT-5 | Prices and market power | Commercial drug negotiation and $2,000 cap; hospital prices capped at 200% of Medicare; PBM and insurer divestitures | −0.45 | −0.40 | −0.35 | Regular order (merged into HLT-3) | 2 |
| HLT-6 | Medicare payment reform | **All** Medicare Advantage overpayment captured (coding and benchmarks); 50 negotiated drugs a year; site-neutral payment | −2.50 | −1.95 | −1.40 | R1 | 0 |
| | **Base package, net (all channels)** | | **2.2** | **3.7** | **5.2** | | **10** |
| | *of which the general fund* | | *3.1* | *4.4* | *5.7* | | |

The net is about $1.2T below the go-big bill as written at the midpoint ($4.85T). Two changes produce it:
- **Medicare at 60 moves out:** $0.30T to $0.36T.
- **Full Medicare Advantage capture:** saves $0.6T to $1.1T more (go-big tab).

## Add-ons, scored separately

Each add-on carries its own score, so it can be added or dropped without reopening the bill.

| ID | Add-on | Cost | Basis | In the base? |
| --- | --- | --- | --- | --- |
| HLT-A1 | Dental in traditional Medicare | Part of HLT-2's $0.55-0.65T dental, vision and hearing line. Starting dental after the window would save about $0.3T (C5, **declined, Decision Brief 2**: pure timing, nothing after 2039) | sourced (go-big tab) | **Yes, kept in, on schedule** |
| HLT-A2 | Medicare at 60 | $0.30T to $0.36T; about 7M enrollees, 0.4M newly insured | sourced (go-big tab) | No |
| HLT-A3 | Medicare at 55 | About $0.6T to $0.9T, my estimate (roughly twice the 60-64 cohort, with higher take-up among 55-59 early retirees). Needs a score | estimate | No |
| HLT-A4 | Medicare for Kids / Medicare at Home | Each needs a broad-based tax (go-big tab) | sourced (qualitative) | No |

An add-on rides R2 with HLT-2 if it can be paid for there. Otherwise it waits for R3 or a later Congress.

## Financing by channel (D4)

- **General fund:** HLT-1 to HLT-6 net of HI's share (about $4.4T at the midpoint) is paid from the revenue domain's base. The pairing rule puts HLT-1 with the corporate rate and the 2025-cut reversal in R1.
- **Medicare HI:** HI is kept whole (D4) by **REV-H1a** (the 3.8% investment-income tax extended to active pass-through income, about $0.5T) plus HI's share of HLT-6's Medicare Advantage savings (about $0.7T). **REV-H1b** (the 5% Medicare and investment-income rate above $400K, about $0.5T) sits in the **general-fund base, not in HI**; domains/domain-revenue.md governs. HI revenue is not spent on new benefits.
  - Only REV-H1a is credited to HI; counting the whole of REV-H1 (about $1.0T) there would assign REV-H1b's $0.5T twice, to HI and to the general-fund base.
  - Together the two HI sources raise about $100B a year by the early 2030s, roughly the HI shortfall at depletion ($85B in 2033).
  - **HLT-6 channel split (estimate).** Of HLT-6's $1.95T midpoint savings, the pieces split as follows:
    - Medicare Advantage reform is about $1.57T. HI's share is about 42%, since Part A is roughly that share of MA payments.
    - Drug negotiation ($0.12-0.22T) falls on Part D (SMI, general fund).
    - Site-neutral payment ($0.19-0.23T) falls mostly on Part B, with a small HI share.

    That puts about **$0.7T (range $0.5-0.9T) in HI** and about **$1.25T in the general fund**. CRFB's attribution of $550B of 2027-36 overpayment to HI is consistent with this. The ledger's HLT-6 row carries only the general-fund share.
  - **HI sources and need.** HI receives this $0.7T plus REV-H1a (about $0.5T). That totals about $1.2T against an estimated $0.8-0.9T needed to close the 0.56%-of-payroll gap in the window. The surplus is why REV-H1b sits in the general fund (domains/domain-revenue.md).
    - *HI's need and reserve.* The $0.8-0.9T need is derived from the $85-100B annual shortfall rather than directly from 0.56% of payroll; the two reconcile because HI's taxable payroll is uncapped and so much larger than OASDI's. D4 is read on a **75-year window** for HI, the Trustees' standard and the basis of the 0.56% gap, because the HI shortfall grows after 2039. The roughly $0.3T surplus is therefore kept as HI's reserve, not swept to the general fund. It also hedges the concentration risk below: if Medicare Advantage capture lands low, HI's share falls toward $0.5T and the surplus is what absorbs it.
    - *Concentration risk (revenue audit).* The incremental MA capture ($0.6-1.1T over the go-big baseline) and the 42% Part A split are both estimates, and together they carry a general-fund saving and HI's solvency at once. If capture lands at the low end, the general fund loses and HI's cushion goes with it in the same stroke. No other row in the ledger has that property, which puts a real score for HLT-6 at the top of the scoring queue.
- **Part B premiums:** about a quarter of HLT-2's new benefits is covered automatically by premiums, raising Part B about $18 a month (go-big tab).
- **Visibility (accounting rule, domains/domain-revenue.md).** Every channel shows its revenue and its outlays at gross. The ledger's channel table carries HI's sources (REV-H1a plus HLT-6's Part A share, about $1.2T) against its need (about $0.85T); the HLT-6 bill row carries only the general-fund share.

## Options not chosen

| Option | Design | Net, 2030-39 | Why not |
| --- | --- | --- | --- |
| A. Go-big as written | All six titles, Medicare at 60, MA capture at a third to 60% | $3.6T to $6.1T | D6 |
| C. War-game version | Public option plus Medicare at 55 | Unscored | D6; the war-game docs are ideas only |
| Single-payer | Not modeled | n/a | Outside the 52-54-seat planning case (D1) |

## Survival at 51 (D1 stress test)

| Title | Survives at 51? | Why |
| --- | --- | --- |
| HLT-1, HLT-4, HLT-6 | Yes | Reconciliation; the restoration is the strongest-polling piece |
| HLT-2 | Probably | Reconciliation; the Part B premium increase is the attack line |
| HLT-3, HLT-5 | Only with D2's rules change and every vote | Regular order; the hospital lobby is the swing |

## Felt dates

- Restoration lands in the 2030 plan year, before the midterm.
- Hearing and vision start in 2031 and dental phases in from 2033.
- The public option opens for plan year 2031, with auto-enrollment in 2032.

Under the adopted launch schedule, HLT-1 and part of HLT-4 are the main pre-November-2030 delivery candidates. This is not a verified reach or household-receipt finding; component-level earlier alternatives are being developed below.

## Dependencies

- **D2:** HLT-3 and HLT-5 need the rules change.
- **D5:** if R1 is lost, HLT-1, HLT-4 and HLT-6 move to R2. Recalculate restoration delivery against the summer-2029 R2 target; the earlier one-year-slip statement is not a validated revised forecast. Adopted health launch dates remain unchanged.
- **Capacity:** CMS delivery spans HLT-1 to HLT-6, not only auto-enrollment. CAP-7S's full multi-year surge is immediately available on enactment, targeting R1 in FY2029 (Espen, Oct 21). Continuing operations use CAP-7 or a reconciled HLT allowance. See domain-capacity.md's CMS annex and sources/health-cms-implementation-cost-register.csv. HLT administrative components and FY2029 cash remain unpriced; do not add CAP funding to embedded administration twice. Provider participation and enrollment safeguards need explicit design; no date or benefit change is adopted.
- **Revenue:** the channel assignment of REV-H1a and REV-H1b is governed by domains/domain-revenue.md.

## Design-rule check

| Rule | How this file meets it |
| --- | --- |
| Durable instruments | Permanent credits; auto-enrollment; statutory price caps |
| Legibility | The $5,000 cap, the $2,000 drug cap and the public plan are named, visible benefits |
| Pairing | The public option (structural) moves with the restoration and premium relief (material) |
| Supply with demand | 14,000 residency slots and doubled health centers move with the coverage expansions |
| Capacity first | CMS annex covers all six titles; immediate R1 surge availability targeted; recurring operations/state costs separated; delivery dates remain targets requiring validation |
| Write for this Court | Taxing and spending power; severability between titles |
| Every number has a basis | Go-big tab ranges; HLT-A3 is my estimate; the HLT-6 split and the HI need are estimates, flagged above |

## Sources

- sources/health-go-big-bill-detail-and-financing.md (title and provision ranges, Medicare Advantage capture, Medicare at 60, the dental delay, Part B premiums) and its cited sources.
- sources/revenue-channels-and-full-menu.md: the HI gap (0.56% of payroll, Q2 2033 depletion, $85B shortfall in 2033) and the HI revenue rows.
- domains/domain-revenue.md: governs the channel assignment of REV-H1a and REV-H1b.
- index/revenue-assignment-audit.md: the HI channel assignment and the open items flagged above.

**Calendar evidence note (October 23):** Earlier felt/floor-day labels in this file are planning assumptions unless tied to an adopted effective date. Current scenario scheduling is in `index/calendar-scenarios.md`; the separate delivery-opportunity screen is in `index/calendar-delivery-opportunities.md`. Earlier enactment does not itself establish implementation, reach or household receipt. Adopted designs, launch dates and fiscal profiles are unchanged.

## Earlier delivery alternatives: development approved October 23

The adopted dates above remain the baseline. Espen approved development and integration of the following alternatives; no new effective date, benefit scope, vehicle or fiscal profile has been selected. The evidence and detailed comparison live in [the health acceleration assessment](../sources/health-2029-restoration-and-2030-medicare-option.md), which supports this canonical option record rather than creating another policy version.

| Existing policy | Alternative to develop | Required decision evidence |
| --- | --- | --- |
| HLT-1; restoration elements of HLT-4 | Deliver feasible existing-program repairs during 2029 rather than apply one January-2030 wait to the whole title | Separate premium assistance, eligibility/renewal repairs, reenrollment, existing grants, coverage-gap infrastructure and care supply. Specify lawful prospective dates, any express retroactive remedy, state participation, first receipt and reach. |
| HLT-2 hearing and vision | January 2030 launch after summer-2029 R2, with preparation before enactment | Actual statutory/rulemaking, payment, provider/supplier, contractor claims/testing and beneficiary-information schedule; marginal costs and Part B effects; named blockers and a responsible fallback. |
| HLT-2 authority/vehicle | Compare earlier R1 authority if it buys necessary implementation time without jeopardizing fast R1 | Instructions, jurisdiction and Byrd review; added preparation burden, score and financing across vehicles; FY2029 administrative cash and overlap with CAP-7S. No vehicle change is adopted. |

HLT-2's 24-month legacy lag is not a verified implementation minimum. Do not apply the shortest restoration path to the full HLT-1/4 bundle, or use one title-wide lag to rule out individual earlier benefits. A reduced allowance or exams-only service is not equivalent to the chosen hearing/vision benefits; any staging must disclose excluded services and people and requires Espen's decision. Dental remains in the package on its adopted phase. HLT-3 availability and automatic-enrollment dates remain 2031 and 2032.

Next work: one component schedule and launch specification, separating legal authority, operational availability, first household receipt, broad reach and full rollout; one incremental score/financing bridge, including FY2029. Retain 2031 hearing/vision as the fallback pending that review. The adopted fiscal totals and launch inputs are unchanged.


## Completed health-delivery research: October 24 reconciliation

The [completed bridge reconciliation](../sources/health-delivery-resource-bridge.md) supports distinct 2029 HLT-1/4 restoration paths and identifies MA payment-cycle dependencies for January-2030 hearing/vision. The report conditionally favors early R1 authority, but did not analyze the existing Original-Medicare payment bridge under 42 CFR 422.109(c). The [decision packet](../sources/health-hearing-vision-decision-packet.md) compares both R2 payment subroutes with early R1 and the adopted 2031 fallback. No date, benefit, vehicle, cost or input is changed. The [component register](../sources/health-delivery-component-register.csv) records conditional component schedules and remedy questions; its proposed dates are not adopted effective dates or certified readiness. The packet recommends protecting R1 on present evidence and testing the existing payment bridge before bespoke R2 MA machinery; full benefit parameters, marginal costs and specialist clearance remain unresolved.

**October 24 packet review approval:** Espen selected 1A/2A/3A/4A: protect rapid R1, examine the existing Original-Medicare bridge first, pursue feasible component-level 2029 restoration, and develop reinstatement plus potential retroactive coverage/claims repair with lookback and costs returned for decision. These development directions are recorded in [the governing decisions](../governing/project-2050-governing-decisions.md#health-packet-review-decisions-approved-october-24). They do not select new launch dates, benefit parameters, eligibility or financing.
