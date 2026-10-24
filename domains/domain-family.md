# Domain file: Family benefits (FAM)

Canonical. This file covers the Child Tax Credit, child care and pre-K, and paid leave; education lives in domains/domain-education.md, and FAM-4 stays below as a pointer so the ID is stable. It replaces the Bill Book's family sheets (06, 07, 20, 25) and Beyond Health Care on substance. All figures are ten-year totals for 2030-39 in trillions. Basis tags: **sourced**, **scaled** (a cited score moved to 2030-39) or **estimate** (mine).

## Summary

| ID | Program | Chosen design | Net cost (low / mid / high) | Channel | Vehicle | Felt by Nov 2030? |
| --- | --- | --- | --- | --- | --- | --- |
| FAM-1 | Child Tax Credit | $3,600 under 6 and $3,000 ages 6-17; fully refundable; paid monthly; indexed | 1.3 / 1.5 / 1.8 | General fund | R1 | Yes |
| FAM-2 | Child care and pre-K | Phased: universal pre-K and a lowest-income tier first, then the full 7%-of-income cap from 2032 | 0.4 / 0.6 / 0.9 | General fund | R2 | Partly (pre-K) |
| FAM-3 | Paid family and medical leave | 12 weeks of social insurance with a 0.6% contribution split between employer and worker, stepping automatically toward 0.85% if the reserve runs low | 0.0 to the general fund at every point (the fund carries ±$0.4T; a repayable Treasury loan bridges any shortfall above the cap) | Paid-leave fund | R2 | No (benefits from 2031) |
| FAM-4 | Education | Pointer: lives in domains/domain-education.md (EDU-1, EDU-2, EDU-5) | — | — | — | — |
| | **General-fund total** | | **1.70 / 2.10 / 2.70** | | | |

The total leaves out education's $0.45 / 0.65 / 0.85T (EDU-1 and EDU-5), which the education file counts.

## FAM-1. Child Tax Credit

**Design.** The credit builds on current law, which made a $2,200 credit permanent in 2025 (partly refundable, indexed). It raises the credit to $3,600 for children under 6 and $3,000 for ages 6-17 and makes it fully refundable, so the lowest-income families get the whole amount. Payments go out monthly through the IRS, and the 2021 phase-outs apply ($150K joint for the increase). It is paid for in R1 by the corporate-rate row under the revenue file's pairing rule.

**Drafting note (payments do not stop).** A refundable credit is paid under Treasury's permanent appropriation for refundable credits, so monthly payments continue through a lapse in appropriations. The Talarico scenario model credits that standing disbursement authority with defeating a shutdown; the statute should say so expressly for the advance monthly payments, as CLI-2 does for the dividend.

**Cost.** About $1.5T, range $1.3T to $1.8T (scaled).
- **The anchor against current law:** the Tax Policy Center put the 2025 American Family Act at about **$1.4T for FY2026-35, measured against today's $2,200 credit** (TPC, June 2026). That design is larger per child: $3,600 to $6,360 by age, inflation-adjusted. It also cuts higher-income families to $2,000.
- **Our design against it:** ours pays less per child, which lowers the cost. It keeps $2,200 at higher incomes, which raises it. Moving the window to 2030-39 raises it too.
- **Older scores, for context:** CBO put the permanent 2021 design at $1.6T for 2022-31, and CRFB at about $1.7T through 2033. Both are measured against older laws.

A score of this exact design is still needed.

**Options.**

| Option | Design | Cost | Basis |
| --- | --- | --- | --- |
| FAM-1A (chosen) | Full 2021 design, monthly | 1.5 | scaled |
| FAM-1D | The 2025 American Family Act (larger, with a baby bonus; higher incomes cut to $2,000) | About 1.7 | scaled (TPC $1.4T, FY2026-35) |
| FAM-1B | Supplement only: +$500 for most children and +$1,500 under 6, on top of current law | About 0.45 | scaled (CRFB $380B through 2033) |
| FAM-1C | Full refundability of the current $2,200 credit only | About 0.3-0.5 | estimate |

**Why A.** The 2021 credit cut child poverty sharply in its first months. The ledger also shows it is the fastest benefit to be felt (about five months after enactment), and monthly payments make it legible. B is the fallback if R1 can't carry A's cost. The Talarico stress test adds a reason to keep the credit near-universal: a universal child benefit resists the deservingness frame that a means-tested one invites.

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

**Financing option.** EDU-9B (domain-education.md) would move FAM-2's money into a dedicated education fund financed by an uncapped payroll contribution, under the frame "school starts at three." It is not chosen: Espen deferred it to a revenue strategy session on payroll raisers, where its D3 and D4 questions are taken up.

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
- **Education:** EDU-4 staffs FAM-2's pre-K build-out; EDU-9B would finance it.
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
