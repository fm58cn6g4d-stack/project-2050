# Adopted family package: architecture and model bridge

October 24, 2026 · Espen's policy adoption, prepared for integration in PR #18. Source main: `31d2e584d790c6dc6e3c243e1643b1ab3a8d050e`; continues comparison commit `d6f90b6e3e19b8cc206760254d9fcd4847848cd3`. This document reconciles the approved choice; canonical governing/FAM/HOU records remain the policy homes. No merge approval is inferred.

## Selected scope and retained boundaries

Espen adopted the **American Family Act credit plus one million total new voucher awards**, with broader assistance for all proxy-eligible renters retained as an **optional add-on to explore**. The one million replaces 400,000; it is not one million on top of 400,000. Broader assistance is not included in the base and any later expansion must be priced relative to the million already selected.

| Architecture home | Reconciliation |
| --- | --- |
| FAM-1 / option FAM-1D | AFA replaces FAM-1A as chosen. Monthly refundability, larger young-child benefit, first-month newborn payment and source-vintage inflation protection. Use the AFA's actual eligibility, identification, income and payment structure in faithful subsequent specification. The introduced bill's historical effective dates do not silently backdate Project benefits. |
| HOU-4 / option HOU-4A | One million new awards with mandatory funding. Preserve the 2030–33 phase-in window: 250,000 annually. Awards and successful leases remain distinct; ongoing assistance continues thereafter. Existing target population retained; no broader proxy-based legal eligibility adopted. |
| HOU-4C | Optional broader-assistance development, potentially approaching all eligible renters once eligibility is actually specified. Model proxies, full-scale leases, cost and financing are not adopted facts. |
| FAM-2A, EDU-3A and FAM-3A | Existing care/pre-K, meals/summer and leave policies retained. Better delivery is necessary across designs; model receipt percentages are not policy targets. |
| D5 / vehicles and dates | Credit stays in R1; housing stays in R2. Preserve rapid R1 and existing effective-date framework; no new floor days, vehicle merger or launch delay inferred. Larger policy still needs text-specific reconciliation and delivery review. |
| Capacity and housing supply | Reuse IRS/HUD/state/local machinery and existing capacity packages; quantify marginal needs and avoid double counting. Retain housing capital/repair/supply programs and provider/workforce support. One million awards do not establish a million available leases. |
| D3/D4 and channel boundaries | Retained. No new revenue instrument, borrowing permission, HI transfer or dynamic revenue adopted. New scope is selected; a compliant financing package is still incomplete. |

The AFA annual model mapping preserves the source-vintage face-value purchasing power, rather than assigning the old amounts anew in 2030. It is not exact legislative arithmetic: the statute's separate CPI base years, lag, rounding, monthly child exposure, income elections, IDs, ODC and reconciliation must be mapped faithfully. Survey citizenship is not an identification-status proxy. The policy choice resolves which design to pursue; it does not convert missing microdata/legal detail into measured eligibility.

## Working cost and single ownership

All costs below are nominal 2030–39 planning amounts, not an official common-baseline score. The rough chat estimates supported a choice, not a claim of precision. Use the rough AFA range with its midpoint as a transparent working input, and scale the existing voucher range for the unchanged phase-in window:

| Item | Previous midpoint | Adopted working low / mid / high | Midpoint change | Ledger owner |
| --- | ---: | ---: | ---: | --- |
| Credit | $1.50T | $1.70 / $1.90 / $2.10T | +$400B | FAM-1 replaces its prior cost |
| New vouchers | $60B | $100 / $150 / $187.5B | +$90B | HOU-4 cost remains inside aggregate HOU-1 |
| Aggregate housing reconciliation title | $470B | $400 / $560 / $732.5B | +$90B | HOU-1; do not add HOU-4 again |
| Credit + care/pre-K + meals + vouchers subtotal | $2.43T | $2.42 / $2.92 / $3.5175T | +$490B | Informational subtotal, not a new ledger row |

The subtotal's full low/high bounds vary shared care/meals costs too, so they are wider than the earlier rough $2.7–3.2T comparison that held shared components near their midpoints. These are not confidence intervals. The earlier $1.7T AFA option point was a scaled estimate; the $1.9T working midpoint explicitly uses the discussed $1.7–2.1T planning range pending a real score. Do not claim the former $1.5T and $1.7T values established an exact $200B increment.

Within the housing fiscal model, `fiscal-components.csv` preserves the old $470B title path separately from the $90B additional assistance. The latter ramps over four years, grows with CPI and remains 100% permanent. Applying the old title's 55% post-2039 continuation share to all the added vouchers would silently discard recurring costs. Components must sum to the aggregate ledger midpoint, and tests reject mismatches. No extra bill row or capital-borrowing line was created.

## Financing and distribution: the adoption changes the result

With existing revenue unchanged, the working midpoint raises general-fund claims from about **$11.10T to $11.59T**. The top-end base remains **$5.99T**; the initial gap becomes **$5.60T**. Existing accepted revenue of **$3.71T** and accepted investment borrowing of **$1.15T** leave about **$0.74T** over the window. The **additional family midpoint is $0.49T**; the $0.74T is the total remaining gap after those existing arrangements, not the new program's cost.

The regenerated DEC fiscal case has an FY2040 GF primary shortfall of about **$53.7B, or 0.099% of GDP**, compared with the old roughly $3.3B surplus. **D4's maturity test now fails under the working inputs.** Ten-year GF primary deficit is about $2.03T and modeled total debt reaches about 155.1% of GDP in 2056 against the baseline's 180.2%. Debt remaining below baseline does not satisfy the separate requirement to fund permanent programs at maturity. These results still use the old CAP-7S cash proxy and uncertain scores.

The next financing choice must supply a supported recurring revenue/offset path, reviewed jointly with other claims and D3, through the relevant vehicle. It cannot use capital-envelope room, the HI reserve, unselected tax options or dynamic revenue as an automatic pay-for. The adoption is recorded in full rather than suppressed to preserve an earlier pass result; the funding decision remains open and consequential.

The regenerated aggregate incidence screen remains positive for the bottom four quintiles on the ten-year average; Q4 is approximately +$1,373 per household annually. Existing credit/housing allocation keys are retained as **provisional** distribution proxies. They do not map AFA-specific high-income credit losses, legal exclusions, within-quintile winners/losers or any new pay-for. The generated report now flags that limitation. A more faithful household/incidence bridge is required before claiming full D3 verification for a newly financed package.

## Current poverty inputs and upgrade sequence

`index/tools/child-poverty/adopted-package.json` explicitly maps FAM-1D/AFA and one million awards to the current annual-exposure research analogue. `comparison_analysis.py` now produces selected-package moderate/enhanced/full cases and later-year cases alongside historical comparisons. Read its [generated selected-package section](family-comparison-model-checks.md#adopted-afa-plus-one-million-award-package); these are partial-agenda conditional results, not a whole-agenda forecast or exact statutory score.

The selected annual analogue gives **8.73% / 8.34% / 8.09% child poverty** under moderate/enhanced/full delivery, respectively (deep poverty about **1.97% / 1.85% / 1.78%**). These compare with the earlier moderate result of 10.29% but change both credit and housing scale; enhanced/full also change assumed delivery. At the filed conditional maturity stages, selected-package poverty is 8.73% in the 2034 moderate reference, 8.34% in the 2040 enhanced illustration and 8.09% in the 2050 full-receipt illustration. Those dates are not forecasts; the population/real valuation reference remains 2034.

The original `agenda-assumptions.json`, eight-case/42-sensitivity result and source-year baseline remain unchanged as historical research. Their Markdown/HTML renderer now labels the FAM-1A/400,000 experiment and links to current selection, rather than presenting it as the adopted package. The public family example now uses the AFA's gross face-value arithmetic for ages three/eight: $7,920 annually, $660 monthly before indexing, not that amount as new income above existing benefits.

Prioritize the next upgrades by what could change a decision:

1. **Exact AFA mapping and new phasing:** statutory CPI/rounding and source-year anchor, monthly birth/custody exposure, current-law credit/ODC replacement, income elections, identification and reconciliation. Recompute the selected package's early phased-year cases; the old 2030 results remain historical, not current-package predictions.
2. **Credible broader household inputs:** calibrated health out-of-pocket effects including premiums, net taxes/transfers/earnings and event-specific leave benefits, with overlap and uncertainty explicit. The tested overlay contract exists; missing estimates are not filled with arbitrary gains.
3. **Rental reach and capacity:** update actual eligibility beyond the income/waitlist proxies, award allocation, lease-up, rents, administration and supply responses at one million awards; price an optional HOU-4C addition relative to that base. The full proxy-pool case is a boundary, not a forecast or implemented entitlement.
4. **Later-year paths and outcomes:** retain explicit conditional 2040/2050 stages and same-scenario baselines. Improve demographic/net-resource paths only when sourced; do not age today's sample into a future child population or assume accumulated improvements. Track housing security, usable care, payment reliability and hardship alongside annual SPM.
5. **Join poverty, fiscal and incidence evidence:** keep household resource changes separate from federal costs; obtain common-baseline scores and calibrated distribution, then use the existing fiscal/incidence tools for a proposed pay-for. No model's success certifies the others.

This is a bounded research sequence, not authority to build a large future forecast, restart completed pilots, issue records requests or write full operating manuals. The immediate priority is the selected package's financing and faithful core model mapping; optional broader assistance remains a separately reviewable choice.

## Validation and integration status

Canonical/option/input changes are reconciled on one task branch. Common products are rebuilt through `run-all.sh --write`; independent poverty/health products through their generators. New fiscal-component tests verify the ledger sum, full permanence of the additional assistance and rejection of mismatch. Poverty tests retain the source/comparator and historical reproduction boundaries while testing the selected-package input. Executed: 117 poverty tests plus the existing regression/ZIP/CLI/synthetic runner; three fiscal-component tests; nine health boundary tests; stored eight-case/42-sensitivity checks; current national selected-package run; historical sixteen-case preservation, source-hash, count/award/lease and generator-render checks; common rebuild and whitespace/link validation. The consistency report has zero stale live headlines; the prior four ID flags, one register mismatch, four ledger/domain flags and two table findings remain, with two dated historical headline passages retained. A fiscal CSV line-ending normalization is generated by its writer and changes no numerical results.

Raw uploaded Census files remain outside GitHub. The committed upload manifest records member hashes and distinguishes the new local ZIP from the unavailable original Census container; source baseline fields and historical reference cases reproduce. No external review, official score, calibrated whole-agenda result or automatic approval of new financing is claimed. PR #18 remains unmerged pending authorization.
