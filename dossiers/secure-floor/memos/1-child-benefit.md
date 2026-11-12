# Memo 1: The child benefit, its design and whom it reaches

Role: decision memo for Espen, forks 1 and 2 of the secure floor (`../README.md`, "Forks for S3"; `../3-design.md`). Status: **decided** (`DEC-2026-11-12-06`): part 1 **A**, the American Family Act with no earnings test (point 1 yes) and **without** the $2,200 floor (point 2 no), so the bill's own phase-out applies; part 2 **B**, the child's own ID only, paid to the parent the child lives with. Specified in `../4-specification.md` (FAM-1.01 to 1.11); repriced without the floor in `../6-cost.md`, part 1 (about $1.85 trillion over FY2030-39 and $209 billion in FY2040; the floor was worth about $0.05 trillion). The text below is the memo as Espen decided it; its recommendation of the floor was declined. Sources are named in plain text; bracketed tags point to the evidence register (`../evidence.json`). Costs marked "judgment" are this dossier's working assumptions, with their basis in `../3-design.md`, "What the options cost".

**Decision line.** Recommended: **A, the American Family Act (FAM-1D), with no earnings test, keeping today's $2,200 credit as a floor above its phase-out; part 2: B, the child's own ID only, paid to the parent the child lives with.** Cost: about **$1.9 trillion over FY2030-39 (range $1.7-2.1 trillion), about $220 billion in FY2040 (range $195-245 billion)**, against the January 2029 law. Evidence: official data on the 2021 credit; quasi-experimental studies on hardship; contested simulations on work.

**This memo decides how large the child benefit is, how it is shaped, and which children it reaches.** Memo 2 decides how it is delivered; memo 7 decides how it fits with other programs' income tests.

## The question

In 2029 the child credit will be $2,200 a child, indexed, but a family must earn about $2,500 before any is refundable, and the refundable part tops out at $1,700 (Public Law 119-21) [EV-SEC-003] [EV-SEC-006]. You adopted the American Family Act on October 24, 2026 (`legacy/governing/project-2050-governing-decisions.md`, "Family package adopted") [EV-SEC-690]. That adoption is a working choice to weigh here, not a decision of this plan (`DEC-2026-10-30-02`). Four designs are on the table:
- the American Family Act, the one you chose;
- a Canada-style benefit, larger at the bottom and tapered by income from the middle;
- the 2021 expanded credit;
- full refundability of today's $2,200 credit and nothing more.

Part 2 asks which children it reaches: the 2025 law's Social Security number rule, and who is paid.

## Why it matters

- **Child poverty is back where it was.** 13.4% of children were poor on the Supplemental Poverty Measure in 2025, about 9.66 million (Census, 2026) [EV-SEC-019] [EV-SEC-020], against 5.2% in 2021, the year of the monthly credit (Census, 2022) [EV-SEC-202].
- **Today's credit skips the children who need it most.** 17 million to 19 million children get less than the full credit because their parents earn too little (Tax Policy Center, 2025; Columbia's Center on Poverty and Social Policy, 2025) [EV-SEC-011] [EV-SEC-601]. In the legacy model, children in deep poverty receive about $527 of credit on average (legacy model review, 2026) [EV-SEC-675].
- **The number rule shuts out citizen children.** About 500,000 children lose the credit because no parent has a work-eligible Social Security number (Bipartisan Policy Center, citing the Tax Policy Center, 2025) [EV-SEC-016].

## What the evidence says, in five lines

1. **A large, monthly, fully refundable credit cuts child poverty fast** (official data): the 2021 credit's expansion alone moved 2.1 million children out of poverty (Census, 2022) [EV-SEC-204], and the first monthly payment cut food insufficiency by about a quarter (Shafer and others, 2022; quasi-experimental) [EV-SEC-209], and monthly payments did so where a lump sum did not (Parolin and others, 2023) [EV-SEC-210].
2. **The work effect is contested** (both sides in section 2, part A.2): studies of the 2021 payments find none (Ananat and others, 2022) [EV-SEC-212]; simulations of a permanent credit predict 367,000 to 1.5 million parents leaving work (Bastian, 2022; Corinth and others, 2021) [EV-SEC-219] [EV-SEC-218]. Even the largest prediction leaves child poverty about a fifth lower.
3. **A work requirement buys little work**: removing one from a California credit caused very few mothers to leave work (Goldin and others; quasi-experimental) [EV-SEC-224].
4. **Canada shows a benefit with no phase-in can keep child poverty lower for years** (international practice): 16.3% in 2015 to 10.7% in 2023 (Statistics Canada) [EV-SEC-240], with no labor supply response in one study (Baker, Messacar and Stabile, 2023) [EV-SEC-241].
5. **Cash for very young children has not yet shown developmental gains in a trial** (Baby's First Years, 2025; randomized) [EV-SEC-227]. The case rests on poverty and hardship, not on quick child-development effects.

## Part 1. The design

**A. The American Family Act (FAM-1D; recommended).**
- **What it does.** $300 a month for each child 6 to 17 and $360 for each child under 6, with $2,400 in a newborn's first month, fully refundable, paid monthly and indexed (H.R. 2763, S. 1393, 2025) [EV-SEC-262]. It phases down by 5% of income above $150,000 for couples ($112,500 for others), and again above $400,000 [EV-SEC-263]. Two changes from the bill: no family gets less than today's $2,200 indexed credit (point 2 in section 3), and no earnings test (point 1).
- *Where tried:* the 2021 credit, for one year, at similar amounts [EV-SEC-200]. No permanent US version.
- *For people:* a single mother of two, ages 3 and 8, with $14,000 of earnings gets $660 a month, against about $1,725 a year today, 15% of earnings above $2,500 [EV-SEC-262] [EV-SEC-006] (project arithmetic).
- *Cost:* about $1.9 trillion over FY2030-39 (range $1.7-2.1 trillion), the legacy planning range [EV-SEC-690]; about $220 billion in FY2040 (judgment, the range grown at 2.5% a year).
  - *Benchmarks:* the Tax Policy Center puts the bill at about $1.4 trillion over FY2026-35 against current law [EV-SEC-266]; moved four years later and grown, about $1.6-1.7 trillion (project arithmetic). PolicyEngine puts it at $2.5 trillion over 2025-34 against an older baseline [EV-SEC-267]. The legacy range sits between them.
- *Child poverty:* the legacy model, with one million vouchers, puts it at 8.73% (moderate delivery) to 8.09% (full), from 13.40% [EV-SEC-692]. Columbia's Center on Poverty and Social Policy puts the credit alone at 13.3% to 8.8% for 2024 [EV-SEC-268]. **With the largest predicted work response**, the cut is about a third smaller: about 10% (project arithmetic on Corinth and others' 34% to 22% [EV-SEC-218]).
- *Political risk:* the largest cost of the four; the 2021 version lapsed after a year. It is the House and Senate Democrats' bill [EV-SEC-260] [EV-SEC-261].
- *Burden:* none beyond memo 2's delivery.

**B. A Canada-style benefit.**
- **What it does.** A larger amount for the poorest families, say $7,000-8,000 a year under 6 and $6,000 for older children, tapered by 7 to 23 cents a dollar of family income from about $40,000, as Canada's is [EV-SEC-234] [EV-SEC-235], paid monthly on the prior year's return.
- *Where tried:* Canada since 2016 [EV-SEC-236].
- *For people:* the same mother gets about the same as under A. A couple with two children earning $70,000 gets several thousand dollars less than under A.
- *Cost:* about $0.6-1.0 trillion over FY2030-39 more than current law; about $75-110 billion in FY2040 (judgment). The Century Foundation and the Center on Budget and Policy Priorities each put a Canada-style design at about $50-80 billion a year more than the credit it would replace (2018-2020) [EV-SEC-604] [EV-SEC-605].
- *Child poverty:* the Century Foundation's simulation cuts it from 13.5% to 6.4% [EV-SEC-604]; CBPP finds more than half [EV-SEC-605]. These are advocacy groups' simulations against an older baseline, but they agree that B is the most poverty-cutting per dollar.
- *Political risk:* families in the middle get less than under A, and the taper adds 7 to 23 cents a dollar exactly where the earned income credit, SNAP and premium credits already phase out (memo 7) [EV-SEC-557].
- *Burden:* the same as A.

**C. The 2021 expanded credit (FAM-1A).**
- **What it does.** $3,600 under 6 and $3,000 for 6 to 17, fully refundable, monthly [EV-SEC-200].
- *Cost:* about $1.5 trillion over FY2030-39 (legacy, scaled) [EV-SEC-691]. CBO put a permanent 2021 credit at $1.6 trillion over 2022-31 (via CRFB, 2021) [EV-SEC-606] [EV-SEC-607]; CRFB's own model gave $1.19 trillion [EV-SEC-606]. Against the 2029 law's $2,200 credit, the increment is smaller than either.
- *Child poverty:* about 10.3% in the legacy model (moderate delivery, fewer vouchers) [EV-SEC-674].
- *Why not recommended:* it pays less than A for every child and has no newborn payment, at a similar cost.

**D. Full refundability of today's $2,200 credit only (FAM-1C).**
- **What it does.** Removes the earnings test, so every child gets the $2,200 [EV-SEC-001].
- *Cost:* about $0.3-0.5 trillion over FY2030-39 (legacy estimate) [EV-SEC-691]; about $35-50 billion in FY2040 (judgment). The Century Foundation put full refundability at $23 billion a year in 2020 [EV-SEC-603]. The Tax Policy Center's $48.5 billion over FY2025-34 is a narrower change that keeps a phase-in [EV-SEC-600].
- *Child poverty:* about 1.2 million fewer poor children (CBPP, 2026) [EV-SEC-602]; a 22% cut (Century Foundation, 2020) [EV-SEC-603].
- *Why consider it:* the cheapest single change against deep poverty, and the floor under every other option. *Why not recommended alone:* $183 a month is about a third of what the 2021 credit paid a young child.

## Part 2. Whom it reaches

| Option | What it does | Children reached | Cost | Recommended |
| --- | --- | --- | --- | --- |
| A. The 2025 law | The child and at least one parent need a work-eligible Social Security number [EV-SEC-005] | About 500,000 citizen children excluded [EV-SEC-016] | — | |
| **B. The child's own ID only** | The child needs a taxpayer identification number; no parent rule, as the American Family Act provides [EV-SEC-264] | The 500,000, and children of mixed-status families | About $2-3 billion a year (judgment: 500,000 children at about $4,000-5,000) | **Yes** |
| C. Every resident child | No ID test; residence shown by records (memo 2) | All resident children | Larger and unbounded in the register | |

- **Why B.** It is the bill's own rule. It reaches citizen children whose parents lack a number, without opening the credit to children with no record at all. The 2025 House text would have excluded about 2 million (JCT, via the Tax Policy Center) [EV-SEC-015]. Immigrant eligibility is shared rule 3, owned by the immigration flagship. B is this dossier's proposal to that table.
- **Who is paid.** The parent the child lives with most of the year, on that parent's attestation, with an even split for shared custody (point 3). Today the credit goes to whoever claims the child on a return. How Canada chooses the payee is not yet in the register (`../3-design.md`, "Evidence still needed").

## Against the bills

| Bill | What it does | Match or diverge with A, and why |
| --- | --- | --- |
| **American Family Act**, H.R. 2763 and S. 1393 (2025) [EV-SEC-260] [EV-SEC-262] | The design above | **Match.** A adds the $2,200 floor above the phase-out and drops nothing |
| **Current law**, P.L. 119-21 [EV-SEC-259] | $2,200 with an earnings phase-in and the parent number rule | **Diverge:** A removes both; D removes only the phase-in |
| **ARPA 2021** [EV-SEC-200] | $3,600 and $3,000, monthly, one year | **Diverge:** that is C |
| **Tax Relief for American Families and Workers Act**, H.R. 7024 (2024) [EV-SEC-269] [EV-SEC-271] | Raised the refundable cap, kept the phase-in; passed the House 357-70 | **Diverge:** keeps the earnings test that A drops; CBO about $33 billion [EV-SEC-272] |
| **Family Security Act and 2.0** (Romney, 2021-22) [EV-SEC-273] [EV-SEC-275] | $350 and $250 a month through SSA, paid for by ending other credits; 2.0 adds a $10,000 earnings floor | **Diverge** on funding and the earnings floor. TPC and Urban put 2.0 at 14% to 12.4% child poverty for just under $45 billion a year [EV-SEC-615]; Niskanen at 1.1 million children [EV-SEC-614] |
| **Canada Child Benefit** [EV-SEC-234] | Income-tested from about $40,000, no phase-in | **Diverge:** that is B |

## Consequences at a glance

| | **A. American Family Act** | B. Canada-style | C. 2021 design | D. Full refundability only |
| --- | --- | --- | --- | --- |
| Single parent, two children (3 and 8), $14,000 | $660 a month | About the same | $550 a month | $367 a month |
| Couple, two children, $70,000 | $660 a month | Less, by the taper | $550 a month | $367 a month (as today) |
| FY2030-39 cost | about $1.9 trillion (1.7-2.1) | about $0.6-1.0 trillion | about $1.5 trillion | about $0.3-0.5 trillion |
| FY2040 | about $220 billion | about $75-110 billion | about $170 billion | about $35-50 billion |
| Child poverty, no work response | about 8.7% (legacy model) | 6.4% (Century Foundation, older base) | about 10.3% (legacy model) | about 1.2 million fewer poor |
| Adds to the stacked phase-out | No (starts at $150,000) | Yes, 7-23 cents from about $40,000 | No | No |
| Closest bill | American Family Act | none in Congress | ARPA | Economic Mobility Act (2019, cited by TCF) |

Costs are against the January 2029 law; poverty figures come from different models and years and are not strictly comparable (`../3-design.md`, "The child-poverty re-run").

**Fiscal rule** (`DEC-2026-11-10-05`): A and B reach the poorest children at very different cost, so this choice comes to you partly as a money question. The cost is reported to the financing settlement; nothing is trimmed here.

## Recommendation: A, with no earnings test and the $2,200 floor; part 2 B

- **It is the design you chose, and it holds up.** It pays the most to the youngest children, it is monthly, and it removes the earnings test that shuts out the poorest children.
- **It is universal, like Social Security.** It phases out only above $150,000, so it adds nothing to the stacked phase-outs low- and middle-income families face (memo 7). Universal programs keep their support (section 2, part D.1) [EV-SEC-116].
- **B cuts more poverty per dollar, and that is the real alternative.** It would cost perhaps half as much. It would also add a new phase-out of 7 to 23 cents for families from about $40,000, exactly where the stack is worst, and pay middle-income families less. If the financing settlement cannot carry A, B is the fallback, not D.
- **D is the floor of every option.** Removing the earnings test is the cheapest single change against deep poverty, and A, B and C all include it.
- **Part 2 B** reaches citizen children their parents' status now excludes, with the bill's own rule.

**What would change this:** a financing settlement that cannot carry A (toward B); a study of a permanent credit showing a large work response (toward a smaller benefit, not an earnings test, since the test excludes the poorest); immigration's eligibility table choosing another rule (part 2).

## If you decide

- **Under A:** section 4 writes FAM-1D into the 2029 reconciliation bill, effective for tax year 2030, with the $2,200 floor and the child-ID rule; the budget model keeps its $1.9 trillion booking. The child-poverty re-run (section 6) uses A.
- **Under B:** section 4 writes a new benefit; the household model checks the taper against memo 7's ceiling.
- **Under C or D:** the same vehicle, with C's or D's amounts.
- **The agenda.** FAM-1D moves toward L3; B would need a new agenda item.
