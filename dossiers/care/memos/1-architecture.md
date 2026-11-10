# Memo 1: Single-payer, a public option, or a staged path

Role: decision memo for Espen, fork 1 of the health design (`../3-design.md`). Status: for Espen's decision; nothing here is adopted. Sources are named in plain text; bracketed tags point to the evidence register (`../evidence.json`). Cost and coverage figures marked "the coverage model" are this project's exploratory analysis (`models/tools/health-coverage/results.md`, 2032 unless noted), not an official score.

**This memo decides the shape of the health system the plan builds from 2029.** On November 9 you asked for "a serious look at medicare for all ... (not just a public option or 'medicare for all who want it')" (`DEC-2026-11-09-07`). So single-payer gets the same evidence, cost, coverage and transition work here as the legacy design, a public option on top of restored coverage (HLT-1, HLT-3), which under `DEC-2026-10-30-02` is a working choice, weighed as option A.

## The question

In January 2029, CBO expects 36.6 million people uninsured (CBO, 2026) [EV-CAR-020], after the 2025 law's Medicaid cuts and the end of the enhanced premium credits (section 1, part 8). What should the plan build: a public plan alongside private insurance, one public plan for everyone, or a path from the first to the second?

## What the evidence says, in five lines

1. Coverage saves lives and money troubles (Miller, Johnson and Wherry, Quarterly Journal of Economics, 2021; Oregon Health Insurance Experiment, National Bureau of Economic Research, 2013) [EV-CAR-200] [EV-CAR-202].
2. Every extra step drops eligible people (Shepard and Wagner, American Economic Review, 2025; KFF on the Medicaid unwinding, 2026) [EV-CAR-206] [EV-CAR-210]; one plan with automatic enrollment avoids steps by design.
3. Single-payer's national cost turns on what it pays providers and what it covers: estimates run from 13% less (Galvani and others, The Lancet, 2020) [EV-CAR-230] to about 13% more (Urban Institute, 2019) [EV-CAR-223]. CBO's range for 2030 is $0.7 trillion lower to $0.3 trillion higher (CBO, 2020) [EV-CAR-218].
4. Its federal cost is very large in every estimate, because it takes over what employers, households and states pay now: $1.5 to $3.0 trillion more in 2030 (CBO, 2020) [EV-CAR-218].
5. State public options have done little without a firm cap on provider rates (Washington State Health Care Authority, 2025) [EV-CAR-235]; state single-payer plans failed on financing (VTDigger, 2014; NPR, 2022) [EV-CAR-245] [EV-CAR-249].

## The options

**A. Restore coverage and add a public option (the legacy design, HLT-1 and HLT-3).**
- *What it is:* repeal the 2025 law's coverage cuts and restore the enhanced credits (2029-30), then a public plan paying Medicare-based rates, sold on and off the marketplaces from 2031, with automatic enrollment of the uninsured. Employer coverage stays.
- *For people:* about 14.5 million still uninsured in 2032, against 37.2 million under current law (the coverage model). Premiums and deductibles stay; employer plans are unchanged.
- *Cost:* about $240 billion a year of new federal spending in 2032, about $2.6 trillion over FY2030-39, with national spending roughly unchanged (the coverage model). The legacy file priced HLT-1 and HLT-3 together at $3.85-4.85 trillion over 2030-39 (`legacy/domains/domain-health.md`). The gap between the two is not yet reconciled; section 6 will reconcile it.
- *Risks:* Washington's experience says the plan saves little unless its rates are capped [EV-CAR-235]; hospitals fight the rate (Colorado Association of Health Plans, 2025) [EV-CAR-241]. Millions stay uninsured, and the system stays complicated for the people in it.

**B. A staged path to single-payer, with the endpoint written into the 2029 law (recommended).**
- *What it is:* the same first steps as A (restoration, then the public plan with automatic enrollment), plus Medicare's age lowered to 60 in 2031 and 50 in 2035, children enrolled, and every remaining group moved into one Medicare program by a date set in the 2029 statute (2037 as the working date). Each stage starts on its date unless Congress votes to delay it. Memo 2 sets the order.
- *For people:* about 11 to 14 million uninsured in 2032, falling to the single-payer level (about 3.6 million, people not yet enrolled or not covered because of immigration status: section 3, point 3) once the endpoint is reached (the coverage model). People see the system change in steps they can plan around.
- *Cost:* about $250 billion a year of new federal spending in 2032 while only the first wave has moved, rising as groups move, to single-payer's level at the endpoint. Over FY2030-39: about $26 trillion if the path reaches single-payer in 2037, about $21 trillion if it reaches it in 2040 (project arithmetic on the coverage model's growth path, moving in a straight line from 2030), against about $27 trillion for C. Moving employer groups last (memo 2) puts most of the cost in the final years, so the 2037 path lands between those two figures. The endpoint date is therefore mainly a choice about money in the 2030s: by FY2040 every single-payer path costs about $5 trillion a year (project arithmetic). The tax that pays for it rises in steps too, which the financing settlement sets.
- *Why recommended:* it puts single-payer into law while each step is small enough to build, staff and pay for; it tests the payment rates (memo 5) and Medicare's capacity on younger groups before everyone moves; and it gives the financing settlement a decade, not two years, to replace premiums with taxes. The main risk is that a later Congress stops the path; writing the stages as automatic, rather than as later votes, is the defense.

**C. Single-payer Medicare for All, enacted in 2029 and in force by about 2033.**
- *What it is:* one public plan for every resident, comprehensive benefits and no premiums, replacing private insurance for covered services, phased in over about four years after enactment.
- *For people:* about 3.6 million uninsured in 2032 (the coverage model): people not yet enrolled or not covered because of immigration status (section 3, point 3). No premiums, deductibles or networks. The household money that now goes to premiums and out-of-pocket costs, about $1.7 trillion in 2032, and employers' $1.5 trillion, are replaced by taxes (the coverage model).
- *Cost:* about $3.3 trillion a year of new federal spending in 2032 at full scale (the coverage model; CBO's comparable range, grown to 2032, is about $1.7 to $3.3 trillion, and the model runs high against it), about $27 trillion over FY2030-39 with a 2032-35 phase-in. National spending changes from about $140 billion less to about $45 billion more, depending on payment rates and long-term care (the coverage model).
- *Risks:* new taxes on the scale of the premiums they replace, about $3.3 trillion in 2032, enacted at once; demand outrunning supply, with longer waits (CBO, 2020) [EV-CAR-219]; about 600,000 insurance jobs and many more in billing to transition (Bureau of Labor Statistics, 2026; Economic Policy Institute, 2020) [EV-CAR-233] [EV-CAR-232]; and the legislative risk of passing it all in one Congress. Taiwan shows a fast launch can work (Reinhardt, BMJ, 2008) [EV-CAR-250]; Vermont shows how one can fail on the tax (VTDigger, 2014) [EV-CAR-245].

**D. Universal coverage through automatic enrollment and all-payer rates, keeping private insurers.**
- *What it is:* everyone is automatically enrolled in a default public plan unless they have other coverage; private and employer plans continue but every payer pays hospitals the same regulated rates, on the Maryland model; no single payer.
- *For people:* near-universal coverage without moving people out of employer plans; prices fall for everyone.
- *Cost:* between A and C: federal cost near A's plus the default plan's enrollees; national spending falls with the rate setting (Maryland's all-payer model cut Medicare hospital spending 4.1%: CMS evaluation, 2020) [EV-CAR-259].
- *Risks:* the Netherlands, Switzerland and Germany reach universal coverage this way, but with a mandate and heavy regulation (Commonwealth Fund, 2009 and 2020) [EV-CAR-255] [EV-CAR-256]; national all-payer rate setting has never been tried in the U.S. Not costed in the coverage model.

## Consequences at a glance (2032, the coverage model)

| | A. Public option | B. Staged (2032 status) | C. Single-payer | D. Universal multi-payer |
| --- | --- | --- | --- | --- |
| Uninsured | 14.5 million | 11.4-14.0 million, then about 3.6 million at the endpoint | 3.6 million | Not modeled; near A to C |
| New federal cost, 2032 | about $240 billion | about $250 billion, rising to C's level by the endpoint | about $3.3 trillion | Not modeled |
| FY2030-39 federal | about $2.6 trillion | about $21-26 trillion (endpoint 2040 or 2037) | about $27 trillion | Not modeled |
| National spending | about flat | about flat, then C's | about $140 billion less to $45 billion more | Lower |
| Premiums and deductibles | Stay | Fall as groups move | End | Stay, lower |
| Ready to launch | 2031 | 2031 first stage | About 2033 | Untested |

**Fiscal rule** (`DEC-2026-11-10-05`): this choice is mainly about money, so it comes to you. B and C each need new revenue on the scale of the premiums they replace; the coverage model reports the amount to be financed and does not allocate the tax. That is the financing settlement's work, under the rule that households below the top come out ahead (D3).

## Recommendation

**B, a staged path with the endpoint in law.** It is the most likely of the single-payer options to arrive intact, and the one most consistent with "guide, don't police": automatic enrollment at every stage, no new paperwork, and a system that ends up simple for the people in it. If you prefer to keep single-payer as a goal rather than a statutory endpoint, A with B's automatic stages is the fallback; if you want the fastest route to universal coverage and accept the transition risk, C.

**What would change this:** a 2027-28 deal that restores the credits early (A's first step done); a Senate too narrow for the stages to be written as automatic; or evidence from the first stages that Medicare's rates (memo 5) leave providers short.

## Questions for you

1. Which shape: A, B (recommended), C or D?
2. If B: is 2037 the right working date for the endpoint (about $26 trillion over FY2030-39), a later date such as 2040 (about $21 trillion), or the date left for the financing settlement?
