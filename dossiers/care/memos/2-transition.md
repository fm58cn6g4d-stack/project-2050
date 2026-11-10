# Memo 2: The transition

Role: decision memo for Espen, fork 2 of the health design (`../3-design.md`). Status: decided by Espen, November 10, 2026: by payer, with children in the first wave, and yes to all five protections (`DEC-2026-11-10-09`); **employer groups move with Medicaid in wave 2 (2033-35), required, with employers paying a contribution until the financing settlement's payroll contribution takes effect**, and the endpoint is 2035 (option B in `../research-s1506-comparison.md`, part b; `DEC-2026-11-10-11`). This replaces the wave 3 order below. Espen's direction: soften the faster transition for hospitals, especially rural providers, by adjusting the payment glide path and/or adding transition funding (sections 4-6 specify it). Sources are named in plain text; bracketed tags point to the evidence register (`../evidence.json`); "the coverage model" is this project's exploratory analysis (`models/tools/health-coverage/results.md`).

**This memo decides how people, workers and providers get from today's system to the one memo 1 chooses.** Its first part (the order) matters for memo 1's options B and C. Its second part (the protections) applies to every option, including A.

## Part 1: in what order do people move?

Applies if you choose a staged path (memo 1, B) or single-payer (C). Under C the stages are compressed into about four years; under B they run to the endpoint date.

**A. By age.** Children and people 50 to 64 first (Medicare at 60 in 2031, at 50 in 2035, children with them), then everyone else at the endpoint.
- *For:* uses Medicare's own machinery; older adults gain most and cost most to private plans; reaching Medicare at 65 already cuts deaths among the severely ill (Card, Dobkin and Maestas, 2009) [EV-CAR-268].
- *Against:* without automatic enrollment only about half of the newly eligible join (CBO, 2022) [EV-CAR-207], and most 60-64-year-olds with employer coverage keep it (Urban Institute, 2022) [EV-CAR-209]; age steps mostly move people between payers. Leaves working-age adults, the most uninsured group (Census, 2026) [EV-CAR-102], for last.

**B. By payer (recommended, with children in the first wave).**
- *Wave 1 (2031):* the uninsured, the individual market and children, automatically enrolled in the public plan from records the government holds; Medicare's age lowered to 60.
- *Wave 2 (2033-35):* Medicaid enrollees move in, with states paying a fixed maintenance-of-effort amount (memo 3); employers may buy in for their workers.
- *Wave 3 (by the endpoint, 2037 as the working date):* employer groups move in; employer premiums become a contribution set by the financing settlement (memo 3).
- *For:* reaches the uninsured first, where coverage does the most good (Miller, Johnson and Wherry, Quarterly Journal of Economics, 2021) [EV-CAR-200]; each wave has a clear administrative source (tax records, Medicaid files, employer payroll); employer coverage, the largest and best-functioning part, moves last, after the public plan has a track record.
- *Against:* for some years people in the same income band are in different plans; employers may drop coverage early once the public plan is open, which raises federal cost before the financing is in place (memo 3 addresses this with a transitional contribution).

**C. All at once on a set date** after a two- to four-year build (Taiwan's 1995 launch was of this kind).
- *For:* one change, simple to explain; Taiwan moved from about 57% to nearly everyone insured overnight (Reinhardt, BMJ, 2008) [EV-CAR-250].
- *Against:* the whole new tax and the whole demand increase land in one year; CBO expects demand to outrun supply (CBO, 2020) [EV-CAR-219]; Vermont's plan stopped when the full tax became visible (VTDigger, 2014) [EV-CAR-245].

**Recommendation: B, by payer, with children in the first wave.** It is the order in which each step serves the most people for the least disruption, and it matches the design lens: enrollment is automatic at every wave, from records the government already holds (KFF, 2024) [EV-CAR-211].

## Part 2: protections during the change (every option)

These are recommended as a package; you can say yes or no to each.

1. **No gap in anyone's coverage.** A person moves only when the new plan is active for them; enrollment is automatic, renewal is yearly at most and from records (the 2025 law's six-month checks and work requirement are repealed in the first bill: section 3, point 2). *Why:* procedural loss drove 69% of disenrollments in the unwinding (KFF, 2026) [EV-CAR-210]. *Cost:* in the restoration cost.
2. **Help for insurance and billing workers.** About 601,800 people work for health insurers (Bureau of Labor Statistics, 2026) [EV-CAR-233]; estimates of all redundant insurance and billing jobs run to 1.8 million gross, about 2% added to national layoffs if spread over four years (Economic Policy Institute, 2020) [EV-CAR-232]. *Recommended:* wage replacement and health coverage for up to three years, training, and first claim on the new plan's administrative jobs, on the model of earlier trade-adjustment programs. *Cost:* a working assumption of $5-15 billion a year during waves 2-3, to be priced in section 6. *Burden:* eligibility by employer records, not individual proof.
3. **A payment glide path for providers.** Rates move from today's blend toward the target in memo 5 over five years, with fixed global budgets for rural and safety-net hospitals during the move (Maryland's model: CMS evaluation, 2020) [EV-CAR-259]. *Why:* CBO finds lower rates reduce supply (CBO, 2022) [EV-CAR-220].
4. **Employers keep contributing until their workers move.** A transitional contribution equal to a share of current premiums, so early dropping doesn't shift cost to the federal budget (memo 3).
5. **States keep paying a share.** A fixed maintenance-of-effort payment, with half their current Medicaid spending for the people who move as the working figure (memo 3); in the coverage model that lowers federal cost by about $300 billion a year at full scale, and the final share is left to the financing settlement.

## What can wait

- **The exact wave dates.** Working dates above; section 5 (delivery) fixes them against CMS's capacity, which the legacy capacity work found was the binding constraint (`legacy/sources/health-cms-capacity-review-2026-10-21.md`). *Treatment:* working assumption.
- **The worker-help formula.** Study in section 4, using the trade-adjustment record. *Treatment:* working assumption, $5-15 billion a year.

## Questions for you

1. If B or C in memo 1: the order by age (A), by payer with children first (B, recommended), or all at once (C)?
2. The five protections: yes to all (recommended), or which not?
