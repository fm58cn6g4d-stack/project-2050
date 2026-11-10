# Memo 5: What the public plan pays hospitals, doctors and drug makers

Role: decision memo for Espen, fork 5 of the health design (`../3-design.md`). Status: decided by Espen, November 10, 2026 (`DEC-2026-11-10-09`): **B, a glide path to about 1.15 times Medicare with global budgets for rural and safety-net hospitals, plus the Medicare Advantage fix at MedPAC's lower estimate**. Later: the faster transition is softened for hospitals by a capped transition fund and a revenue floor for rural and safety-net hospitals, keeping the five-year glide (`DEC-2026-11-10-11` direction, `DEC-2026-11-10-13`); ownership stays as it is with targeted guardrails, and S. 1506's profit bar and public capital budget are not adopted (`DEC-2026-11-10-12`). Sources are named in plain text; bracketed tags point to the evidence register (`../evidence.json`); "the coverage model" is this project's exploratory analysis (`models/tools/health-coverage/results.md`).

**This memo decides the payment rates of the public plan (memo 1's A), of each stage (B), or of the single plan (C), and how fast they move.** It also covers Medicare Advantage while it exists. It is the most consequential number in the design: in the coverage model, moving the single plan's rate from 1.0 to 1.4 times Medicare moves the federal cost from about $2.7 trillion to $4.9 trillion a year in 2032.

## Why it matters

- Employers and private insurers paid on average 254% of Medicare's rates for hospital care in 2022 (RAND, 2024) [EV-CAR-131]. U.S. prices, not use of care, explain most of the spending gap with peers (Peterson-KFF Health System Tracker, 2025) [EV-CAR-129].
- Lower rates cut spending and supply together: CBO's lower-rate scenario cut national spending 9% but supply 2% (CBO, 2022) [EV-CAR-220].
- Capped rates have worked without driving hospitals out: Oregon's 200%-of-Medicare cap for its state employee plan saved 4% in two years with all 24 hospitals staying in network (Health Affairs, 2024) [EV-CAR-262] [EV-CAR-263]; Montana's plan paid 220-250% with no closures (National Academy for State Health Policy, 2021) [EV-CAR-265]. Washington's public option, with an aggregate cap of 160%, cut premiums little (Washington State Health Care Authority, 2025) [EV-CAR-235] [EV-CAR-236].
- Maryland's all-payer rate setting cut hospital spending 4.1% for Medicare and slowed commercial hospital spending growth (CMS evaluation, 2020) [EV-CAR-259].

## The options

**A. Medicare's rates from the start.**
- *Cost:* the lowest; the coverage model's single plan at 1.0 times Medicare costs about $2.7 trillion a year in new federal spending in 2032, and national spending falls.
- *Risk:* hospitals that depend on commercial payments lose most; supply falls, and rural and safety-net hospitals are most exposed. Mercatus's $32.6 trillion estimate already assumes payments more than 40% below private rates (Mercatus Center, 2018) [EV-CAR-226], so its cost would be higher still if rates had to rise to keep hospitals open.

**B. A glide path to a target just above Medicare, with global budgets where markets are thin (recommended).**
- *How:* rates start at a blend near today's average across payers and move over five years to about 1.15 times Medicare for hospitals (doctors at Medicare's rates plus primary-care and rural add-ons); rural, critical-access and safety-net hospitals get fixed yearly global budgets during and after the move, on Maryland's model (CMS evaluation, 2020) [EV-CAR-259]; drug prices are negotiated for all drugs, extending the 2022 law's Medicare negotiation.
- *Cost:* the coverage model's project-central single plan uses 1.15 times Medicare: about $3.5 trillion a year in new federal spending in 2032, with national spending about $95 billion higher (long-term care included). The public option's rate in A or B's early stages would start at about 1.2 to 1.6 times Medicare and move toward the same target.
- *Why:* it captures most of the price gap the evidence identifies, protects the hospitals most at risk, and gives providers years to adjust; it is the design CBO's analysis suggests limits the supply loss (CBO, 2022) [EV-CAR-220].

**C. All-payer rate setting without a single payer.** A national version of Maryland: every payer pays the same regulated rate, set state by state.
- *For:* lowers prices for everyone, including employer plans; works under memo 1's A or D.
- *Against:* never tried nationally; Maryland's savings came with rising spending outside hospitals in some years (CMS evaluation, 2022) [EV-CAR-261].

**D. Negotiated rates with a cap on commercial hospital prices (legacy HLT-5).** The public plan negotiates; commercial hospital prices are capped at 200% of Medicare.
- *For:* closest to the evidence from Oregon and the state employee simulation, which found a 200% cap would save state plans about $7.1 billion nationally while margins barely moved (Health Affairs, 2024) [EV-CAR-264].
- *Against:* leaves prices at twice Medicare's; fits only memo 1's A.

## Medicare Advantage while it exists

MedPAC estimates Medicare pays 14% more, about $76 billion, for Advantage enrollees in 2026 than for similar people in traditional Medicare (MedPAC, 2026) [EV-CAR-135], and 20% in 2025 under its earlier method (MedPAC, 2025) [EV-CAR-266]; the insurers' trade group disputes the coding estimate (AHIP, 2025) [EV-CAR-267]. The legacy design counted on capturing all of it (HLT-6, $1.4-2.5 trillion of savings over 2030-39) and paid for much of the plan with it. **Recommended under every option:** fix coding and benchmarks on MedPAC's method, and count the savings at MedPAC's lower 2026 estimate, not legacy's full capture, testing the low end. Under single-payer, Advantage plans end at the endpoint.

## Recommendation

**B, the glide path to about 1.15 times Medicare with global budgets for rural and safety-net hospitals,** plus the Medicare Advantage fix. The target is a working figure: section 4 sets it by service, and the first stages (memo 2) test whether it holds supply.

**What would change this:** hospital closures or rising waits in the first waves would slow the glide path; evidence that hospitals hold at lower rates (as in Oregon and Montana) would lower the target.

## Questions for you

1. Which payment approach: A (Medicare's rates), B (glide path to about 1.15 times Medicare with global budgets; recommended), C (all-payer rate setting), D (negotiation plus a 200% commercial cap)?
2. Medicare Advantage: fix on MedPAC's method and count savings at its lower 2026 estimate (recommended)?
