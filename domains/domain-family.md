# Domain file: Family benefits (FAM)

Canonical. This file covers the Child Tax Credit, child care and pre-K, and paid leave; education lives in domains/domain-education.md, and FAM-4 stays below as a pointer so the ID is stable. It replaces the Bill Book's family sheets (06, 07, 20, 25) and Beyond Health Care on substance. All figures are ten-year totals for 2030-39 in trillions. Basis tags: **sourced**, **scaled** (a cited score moved to 2030-39) or **estimate** (mine).

## Summary

| ID | Program | Chosen design | Net cost (low / mid / high) | Channel | Vehicle | Felt by Nov 2030? |
| --- | --- | --- | --- | --- | --- | --- |
| FAM-1 | Child Tax Credit | American Family Act (FAM-1D): monthly refundable credit, larger young-child benefit and first-month newborn payment; indexed | 1.7 / 1.9 / 2.1 | General fund | R1 | Yes |
| FAM-2 | Child care and pre-K | Phased: universal pre-K and a lowest-income tier first, then the full 7%-of-income cap from 2032 | 0.4 / 0.6 / 0.9 | General fund | R2 | Partly (pre-K) |
| FAM-3 | Paid family and medical leave | 12 weeks of social insurance with a 0.6% contribution split between employer and worker, stepping automatically toward 0.85% if the reserve runs low | 0.0 to the general fund at every point (the fund carries ±$0.4T; a repayable Treasury loan bridges any shortfall above the cap) | Paid-leave fund | R2 | No (benefits from 2031) |
| FAM-4 | Education | Pointer: lives in domains/domain-education.md (EDU-1, EDU-2, EDU-5) | — | — | — | — |
| | **General-fund total** | | **2.10 / 2.50 / 3.00** | | | |

The total leaves out education's $0.45 / 0.65 / 0.85T (EDU-1 and EDU-5), which the education file counts.

## FAM-1. Child Tax Credit

**Design (Espen, October 24).** FAM-1D, the American Family Act, replaces FAM-1A as the chosen credit. The introduced H.R.2763/S.1393 design uses a monthly base of $300 for ages 6–17, $360 under six and $2,400 in the first month of life, before indexing. A full first twelve-month exposure is $6,360, not a guaranteed calendar-year award to every infant. Preserve the Act's inflation, income-phaseout, taxpayer-identification, monthly eligibility and advance-payment structure in subsequent specification; the model's annual analogue is not exact bill text. R1 and the existing effective-date framework remain; no new launch date is selected.

The policy preserves purchasing power from the AFA's source-vintage amounts, rather than resetting those amounts as unindexed 2030 face values. Exact statutory CPI base/lag/rounding, monthly custody/birth exposure and tax/ODC coordination need faithful model mapping; identification must not be inferred from survey citizenship. Delivery improvement is necessary in every design. The old FAM-1A remains a historical comparator and fallback alternative, not a second adopted credit.

**Drafting note (payments do not stop).** A refundable credit is paid under Treasury's permanent appropriation for refundable credits, so monthly payments continue through a lapse in appropriations. The Talarico scenario model credits that standing disbursement authority with defeating a shutdown; the statute should say so expressly for the advance monthly payments, as CLI-2 does for the dividend.

**Working cost:** $1.7–2.1T over 2030–39, midpoint $1.9T, replacing the old $1.5T midpoint. This is a rough planning range, not an exact CBO/JCT score. The source anchor remains TPC's approximately $1.4T for the AFA in FY2026–35; the later window, inflation and exact policy/baseline need reconciliation. New permanent financing remains unresolved under D4; the old R1 corporate-revenue pairing does not establish spare money. See the [adoption and architecture bridge](../sources/family-adoption-architecture-bridge.md).

**Options.**

| Option | Design | Cost | Basis |
| --- | --- | --- | --- |
| FAM-1A (previous baseline; alternative) | Full 2021 design, monthly | 1.5 | historical scaled estimate |
| FAM-1D (chosen October 24) | American Family Act; monthly, indexed, newborn and young-child enhancements | 1.7 / 1.9 / 2.1 | rough planning estimate; exact score pending |
| FAM-1B | Supplement only: +$500 for most children and +$1,500 under 6, on top of current law | About 0.45 | scaled (CRFB $380B through 2033) |
| FAM-1C | Full refundability of the current $2,200 credit only | About 0.3-0.5 | estimate |

**Why D now.** Espen adopted the AFA after comparing family outcomes and rough costs, alongside one million new rental-assistance awards. The monthly refundable design remains; the larger real benefit strengthens adequacy. The conditional annual analogue supports this direction but does not certify the exact statute, full-agenda poverty effect, financing or delivery. The alternative A and supplement B remain available for explicit future decisions; neither is an automatic scope reduction.

## FAM-2. Child care and universal pre-K

**Design.** The design rule on supply with demand favors phasing, because subsidies outrun slots otherwise:
- **2030-31:** universal voluntary pre-K for 3- and 4-year-olds, a lowest-income tier (free care below 75% of state median income), supply grants, and wage parity for care workers.
- **From 2032:** the full cap at 7% of income for families up to 250% of state median income, once supply grants have built slots.

It is mandatory funding, so it doesn't depend on annual appropriations.

**Cost.** About $0.6T phased, range $0.4T to $0.9T (scaled). CRFB put the 2021 version at $475B to $800B through 2031 if made permanent, and mature-program years cost more. Phasing saves about $0.3T against the full design from 2030.

**Options.**

| Option | Design | Cost | Basis |
| --- | --- | --- | --- |
| FAM-2A (chosen) | Phased | 0.6 | scaled |
| FAM-2B | Full 7% cap from 2030 | 0.9 (0.5-1.2) | scaled |
| FAM-2C | Pre-K only | About 0.2-0.3 | estimate |
| FAM-2D (Bonamici omnibus) | FAM-2A with the omnibus's pre-K standards: at least 1,020 hours a year; staff pay on par with K-12; lead teachers holding a BA within seven years; at least 4% to tribes; localities may apply directly if their state opts out; federal share 100% for the first years, stepping to 60% | Same in-window path if the federal share follows FAM-2A's phasing; the omnibus's 100%-to-2034 share is ~+0.1-0.2 | session estimate (NIEER prices high-quality full-day pre-K with pay parity at ~$12,500 a child; 5.78M unserved 3- and 4-year-olds) |

**Note.** This is the one baseline in this file I chose rather than took from a decision: phasing follows design rule 5 and the felt-date evidence. Flip it to B if you'd rather lead with the full cap.

**Why the under-3 tier matters (education session).** A pre-K expansion without an under-3 expansion actively worsens infant and toddler care by pulling staff toward the better-paid end, the standard critique of the Build Back Better design. FAM-2A's lowest-income tier and supply grants from 2030 answer it; FAM-2C (pre-K only) is exposed to it.

**Quality decides the return.** At scale, pre-K's benefit-cost ratio lands nearer 2-to-1 or 3-to-1 than Perry Preschool's 7-to-1, and quality decides whether a program lands near Boston (college-going up) or Tennessee (negative by sixth grade) (education session). FAM-2D's standards are the quality lever; EDU-4 builds the workforce two to three years ahead of the hiring peak; EDU-10 evaluates.

**Financing history.** The October 20 deferral of EDU-9B was superseded by Espen's full-package adoption. Exact contribution rates and the current-law care boundary remain for decision; the institution's adoption does not itself establish a D3 or D4 pass.

**Education financing adoption.** Espen adopted the full EDU-9B benefit package and separate payroll institution. FAM-2 remains the policy home; its costs move through the [component education reconciliation](../index/recovery-budget.md), without adding the old $0.60T a second time. The current reference retains CCDF/Head Start/PDG outside the fund and treats care as incremental; consolidation and actual replacement overlaps need an explicit boundary decision. The source's changing federal share imposes state obligations and requires reconciliation; alternative federal-share floors are research, not adopted changes. See [EDU-9B](domain-education.md#edu-9b-adopted-the-full-education-fund-benefit-package).

## FAM-3. Paid family and medical leave

**Design.** Twelve weeks of family and medical leave, paid as social insurance (the FAMILY Act model). Wage replacement is progressive, starting at about two-thirds of wages up to a cap. Administration sits in SSA or a new office with state partnerships, and existing state programs can opt in. Leave is a permanent benefit with a natural revenue stream, so under the trust-fund rule it gets its own fund. Higher-than-expected take-up is handled inside the fund, not by the general fund: the contribution steps up automatically, and a repayable Treasury loan bridges any gap above the cap.

**Cost and revenue.**
- **Cost:** about $0.9T, range $0.6T to $1.4T (estimate). CBO put a 12-week FAMILY Act-based design at $547B over ten years. JCT's break-even rate is 0.85% of wages at FMLA take-up, and higher take-up assumptions run far above that.
- **Revenue:** the contribution of 0.6% of wages (0.3% each side) raises about $0.9T (estimate, on about $15T a year of covered wages).

**Automatic step-up.** The rate starts at 0.6% (0.3% each side). If the fund's reserve falls below one year of projected benefits, the rate steps up by 0.05 points (split evenly) at the next January, to a cap of 0.85%, the JCT break-even at FMLA take-up; it steps back down once the reserve exceeds 18 months. At the cap the contribution raises about $1.28T (estimate), against $0.6-1.4T of cost, so only the very high case (about $0.12T) needs the bridge: a Treasury loan to the fund, repaid with interest from later contributions. There is no open general-fund backstop (FAM-3E), which at high take-up would be a $0.45-0.55T claim counted in no total.

**Household test (D3).** A worker earning $60,000 pays $180 a year at 0.6%, and up to $255 if the rate reaches the cap. The test counts this against the insured benefit, the Child Tax Credit and health savings, and should be run at both rates.

**Options.**

| Option | Design | Cost | Basis |
| --- | --- | --- | --- |
| FAM-3A (chosen) | 12 weeks, 0.6% contribution with an automatic step-up toward 0.85% and a repayable Treasury loan (no general-fund backstop) | 0 to the general fund | estimate |
| FAM-3E | 12 weeks, 0.6% contribution, open general-fund backstop | Net about 0; up to +0.55 at high take-up | estimate |
| FAM-3B | 12 weeks, fully general-fund | 0.9 | estimate |
| FAM-3C | 4 weeks, general-fund (the 2021 Build Back Better end point) | About 0.3 | estimate |
| FAM-3D | 12 weeks at 0.85% from the start (fully self-financed at FMLA take-up) | Net below 0; costs the fourth quintile more up front | estimate (JCT rate) |

## FAM-4. Education (pointer)

Education lives in domains/domain-education.md. Title I and IDEA are EDU-1 and EDU-2 (ledger row EDU-1, $0.33T); Pell and SAVE/PSLF are EDU-5 ($0.32T); FAM-4E and FAM-4F are EDU-5B and EDU-5C. The education file adds universal school meals (EDU-3), the educator pipeline (EDU-4), the scholarship-credit repeal (EDU-7), AI in education and student data (EDU-8), research and evaluation (EDU-10) and the financing options (EDU-9). Ledger legacy ID F4 maps to EDU-1 and EDU-5.

## Survival at 51 (D1 stress test)

All three ride reconciliation and survive at 51, as long as R1 and R2 hold and the financing holds. FAM-1 is the most exposed to a single defector on cost, which is why FAM-1B exists.

## Dependencies

- **D5:**
  - If R1 is lost, FAM-1 moves to R2. Reassess first-check timing against the summer-2029 R2 target; the earlier mid-2029-to-mid-2030 slip was an old planning assumption, not a validated new payment schedule.
  - FAM-2 and FAM-3 ride R2.
- **Capacity:**
  - **IRS:** monthly payments.
  - **SSA or a leave office:** the leave program.
  - **HHS and the states:** child care slots.

  IRS and SSA are named in CAP-7's per-agency split (domains/domain-capacity.md); HHS's child care administration is not yet a CAP-7 line.
- **Education:** EDU-4 staffs FAM-2's pre-K build-out; the adopted EDU-9B institution carries its financing, with exact rates and transfers unresolved.
- **Revenue:** FAM-1 is paired with REV-G1 in R1. FAM-3's contribution needs the D3 net test.

## Design-rule check

| Rule | How this file meets it |
| --- | --- |
| Durable instruments | Mandatory spending throughout; the permanent credit; leave as social insurance |
| Legibility | A monthly named check; a named leave benefit; pre-K seats |
| Supply with demand | Child care phased behind supply grants; EDU-4's pipeline ahead of pre-K hiring |
| Capacity first | IRS, SSA and HHS named; IRS and SSA carried in CAP-7 |
| One version per policy | Pre-K lives only in FAM-2; the omnibus's design is FAM-2D |
| Every number has a basis | Tagged above |

## Sources

- [Tax Policy Center, American Family Act (June 1, 2026)](https://taxpolicycenter.org/taxvox/american-family-act-would-mark-significant-investment-low-and-moderate-income-families): $1.4T for FY2026-35 against current law
- [Peter G. Peterson Foundation, CTC and EITC costs](https://pgpf.org/article/what-are-the-costs-of-permanently-expanding-the-ctc-and-the-eitc): CBO, $1.6T for 2022-31
- [CRFB, Build Your Own Child Tax Credit](https://crfb.org/blogs/build-your-own-child-tax-credit-web-based-version) (Aug 2023): $1.7T for the 2021 design and $380B for the supplement option, through 2033
- [American Action Forum, paid leave and the reconciliation bill](https://www.americanactionforum.org/daily-dish/paid-leave-and-the-reconciliation-bill/): CBO $547B; 0.4% CBO-linked rate; JCT 0.85% break-even
- Child care: CRFB's $475-800B through 2031, as carried in the original ledger
- sources/education-transforming-education-act-analysis-and-trust-fund.md: FAM-2D's standards, the under-3 critique and the scale-up evidence

**Calendar evidence note (October 23):** Earlier felt/floor-day labels in this file are planning assumptions unless tied to an adopted effective date. Current scenario scheduling is in `index/calendar-scenarios.md`; the separate delivery-opportunity screen is in `index/calendar-delivery-opportunities.md`. Earlier enactment does not itself establish implementation, reach or household receipt. Adopted designs, launch dates and fiscal profiles are unchanged.
