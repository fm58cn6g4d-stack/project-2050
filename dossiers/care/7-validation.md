# Care you can count on, part A (health): validation

Role: section 7 of the care dossier, health part: the model runs behind sections 4-6, how they compare with outside estimates, what they miss, who the design reaches, the strongest objections and the signs of failure. Status: draft (stage D, step 4, PR 2), on `DEC-2026-11-10-09`, `-11` and `-12`. Figures marked "project arithmetic" come from `tools/health_path.py` on the coverage model (`models/tools/health-coverage/`, exploratory).

## 1. Against outside figures

| Check | Our figure | Outside figure | Reading |
| --- | --- | --- | --- |
| The plan's federal cost at full scale | About $2.71 trillion in 2032 (the decided variant; `6-cost.md`, part 1) | CBO's 2020 single-payer options: $1.5 to $3.0 trillion in 2030 [EV-CAR-218], about $1.66 to $3.32 trillion grown to 2032 (`results.md`, BM-1a) | Inside the range, in its upper half. The model's own corners miss BM-1a (its CBO-like variant is $3.44 trillion), so the model runs high against CBO; read the figure as an upper-middle estimate |
| National spending | About $491 billion lower in 2032 (about 6%; Medicaid's long-term care stays at current-law cost, board row D-4c) | CBO: $0.7 trillion lower to $0.3 trillion higher in 2030 [EV-CAR-218]; Urban: 6% lower (income-related cost sharing) to about 13% higher (no cost sharing, long-term care) [EV-CAR-224] [EV-CAR-223]; the Lancet: 13% lower [EV-CAR-230] | Inside every range, at the low edge of Urban's; the design's rate target and copays put it on the lower side, as Urban's "lite" design is |
| Federal cost relative to current federal health spending | 149% higher (the model's project-central variant, BM-6a) | Urban 2019: 138% (lite) to 257% (enhanced) [EV-CAR-222] [EV-CAR-224] | Passes (indicative only: Urban's baseline is not in the register) |
| Restoration | 9.9 million fewer uninsured in 2032 from the Medicaid and marketplace provisions | CBO: about 10 million in 2034 [EV-CAR-038] [EV-CAR-025] [EV-CAR-049] | Passes, but in-sample: the model's restore flows are set from CBO's estimates (BM-2) |
| Enhanced credits' cost | $65 billion in 2032 | CBO: about $350 billion over ten years [EV-CAR-029], about $37.5 billion in 2032 | **Miss** (BM-3b): the model overstates the credits. The decided path keeps them for plan year 2030 only, so the error is about $40 billion in FY2030 and none after |
| The group split | Groups sum to $2,712 billion | The model's own single-plan run: $2,712 billion | Reproduces the model exactly (`health_path.py`) |
| Advantage overpayment | Savings at 14%, about $76 billion in 2026 | MedPAC 2026 [EV-CAR-135]; MedPAC's earlier method, 20% [EV-CAR-266]; the insurers' trade group disputes the coding estimate [EV-CAR-267] | The low end of the independent estimates, as point 5 decided |

**What the benchmarks do not test.** No independent estimate exists for a staged path with this order and these dates. The path's year-by-year figures rest on the model's 2032 group split grown on one path, so the window total is as good as that split and growth path, and no better.

## 2. What the models miss

| Missing | Direction | Size or note | What would answer it |
| --- | --- | --- | --- |
| Supply limits and waits beyond a fixed share of unmet demand | Lower spending, longer waits | CBO expects demand to exceed supply under single payer [EV-CAR-219]; the model leaves half the extra demand unmet (`sp_unmet_share`) | Wave 1's data on waits (section 8) |
| Copays by income | Distribution only | The model spreads the plan's $189 billion of copays across every income band; the design charges none below 200% of poverty (HLT-7.06), so low-income bands read too high in part 4 and higher bands too low | A copay schedule run through the model's bands |
| Hospital-by-hospital effects, and what hospitals collect for the uninsured today | Distribution, and the sign of the total | `6-cost.md`, part 3 uses national averages of rates and payer mix, and a range for the uninsured's current payments (35% self-pay to all current care); MedPAC's margins by type point the same way [EV-CAR-336] [EV-CAR-337] | Medicare cost reports (2032, HLT-7.15); uncompensated-care and DSH data |
| Long-term care | Higher cost when part B decides | The model's working figure is $200 billion a year (2032; range $100-400 billion) | Part B |
| People without status | Higher cost | The 3.6 million left uninsured include them; covering them is the immigration flagship's decision (point 3) | Shared rule 3 |
| Employer wages | Revenue | Ending premiums raises taxable wages only as far as pay rises; about half of premium cost passes into pay (Anand, 2017) [EV-CAR-299]. The exclusion revenue assumes the former premiums, less the contribution, all become wages. That is CBO's convention (total compensation fixed); at half pass-through of the employer-paid share the revenue is about $242 billion lower at full scale in 2032, or $85 billion with the contribution at 65% (`6-cost.md`, part 6) | The settlement's revenue estimate |
| Behavior of states and employers before their cohort | Cost timing | Employers or states might cut coverage early; HLT-7.04 forbids it and HLT-7.18 charges the contribution | Implementation data |
| Interest and economic feedback | Higher deficit before financing | Neither model computes interest on the plan; no growth or labor-supply effect | The budget model, once booked |
| Fiscal versus calendar years | Fixed | `health_path.py` now blends calendar years into fiscal years (a quarter and three quarters), as the budget model books; the calendar-year count read about $1.1 trillion high over FY2030-39 (review F-2) | — |
| The federal systems | Small | The IHS, VA and TRICARE are held at baseline; the plan's payments to their facilities are not priced | HLT-7.24's open items |
| The territories | Higher cost | The model is CBO's 50-state and D.C. baseline; the territories' residents are priced outside it (`6-cost.md`, part 2; HLT-7.28) | Territory-level spending data |
| TRICARE, the VA and FEHB inside the employer cell | Employer savings and contribution read high | The model's employment-based cell includes them; TRICARE and the VA continue and FEHB's contribution is intragovernmental (`6-cost.md`, part 4) | The model's cell shares |

## 3. How it lands with the rest of the plan

- **The financing settlement.** The amount to be financed, about $2.0 trillion at full scale in 2032 and $3.1 trillion in FY2040 after the employer contribution (`6-cost.md`, part 4), is far larger than any other dossier's. Health's financing is the settlement's main task.
- **Housing.** Rule 7 (services that make housing work) is unchanged until part B; Medicaid's home and community services continue (HLT-7.07). Rural Development's offices are shared with housing's rebuild (HLT-8.01; `DEC-2026-11-10-02`).
- **The workforce (part D).** The design's demand rise and rate cuts both bear on supply; part D sizes the workforce the endpoint needs.
- **Rights.** The Hyde Amendment's end (RTS-2) sits beside the Reproductive Freedom Act (RTS-1), which keeps the conscience laws.
- **Capacity.** CMS's build depends on the agency rebuild (CAP-7S, CAP-7).

## 4. Reach: for whom

**Household cost per person, 2032** (premiums and out-of-pocket costs, before the new taxes; the coverage model; all people in each band, the uninsured included):

| Income (share of poverty) | People (millions) | Today (current law) | The plan at full scale |
| --- | --- | --- | --- |
| Below 138% | 79 | $2,149 | $470 |
| 138-250% | 64 | $4,225 | $545 |
| 250-400% | 69 | $5,111 | $624 |
| 400% and up | 144 | $6,583 | $668 |

The plan column spreads copays evenly across bands (part 2); under HLT-7.06 people below 200% of poverty pay none, so the lowest two rows are lower and the top two somewhat higher than shown. Employers' premium payments, about $1.55 trillion, are not in either column. Who pays the new taxes is the settlement's (D3).

**Who gains first:**
- the uninsured, the individual market and every child, from January 1, 2031;
- people on Medicare, from 2031, with a $5,000 cap and hearing and vision coverage, then dental from 2033 (HLT-2.01);
- people 60 to 64, from 2031 (HLT-2.04);
- Medicaid enrollees and workers with employer coverage, from 2033-35;
- everyone else on January 1, 2035.

**Outcomes it serves:**
- **OUT-03** (care people can count on): about 3.6 million uninsured at the endpoint against 37.2 million under current law in 2032 (project arithmetic; CBO, 2026) [EV-CAR-051].
- **OUT-02** (planning beyond the next paycheck): no deductibles or premiums, and a $1,000 yearly copay cap (working figure). That bears on medical debt, $88 billion on credit records in 2021 [EV-CAR-116].
- **OUT-01** (child poverty): every child covered from 2031.
- **OUT-08** (time and freedom): coverage no longer tied to a job. Job lock was large before the ACA [EV-CAR-300] and small since [EV-CAR-301].

## 5. Objections answered

**"The taxes would be enormous."** The plan replaces premiums rather than adding cost on top. National spending is about $491 billion lower at full scale, and households and employers stop paying about $3.1 trillion a year of premiums and out-of-pocket costs (2032; project arithmetic). The new revenue needed is large: about $2.0 trillion in 2032 terms after the employer contribution. Section 6 reports it rather than hiding it; Vermont's plan stopped when its tax became visible [EV-CAR-245]. The staged path gives the settlement six years from enactment to put the revenue in place.

**"Waits will grow."** They may. CBO expects demand to outrun supply [EV-CAR-219]. The design answers with copays above 200% of poverty where supply is tightest (HLT-7.06), a rate above Medicare's (HLT-7.10), and part D's workforce plan. Wave 1 is a test: section 8 says what would slow the waves.

**"Hospitals will close."** On national averages, hospital revenue as a whole changes little: gains from Medicaid, Medicare and the newly insured offset most or all of the commercial cut, leaving hospitals as a whole between about 4% lower and 1% higher after the glide (`6-cost.md`, part 3). The risk is concentrated in hospitals with high commercial shares and thin margins. Rural and safety-net hospitals get global budgets (HLT-7.11), and the transition fund (HLT-7.15, decided in `DEC-2026-11-10-13`) reaches them first. Since 2010, 87 rural hospitals have closed outright [EV-CAR-338] without a plan of this kind.

**"People like their employer coverage."** Most rate their own coverage well [EV-CAR-305] [EV-CAR-306]. But 29% of the employer-covered were underinsured in 2026 [EV-CAR-109], its cost comes out of pay [EV-CAR-296] [EV-CAR-299], and it reaches lower-wage workers least [EV-CAR-295]. Support for Medicare for All was 52% even if it ended private insurers, while opposition rose to 76% when people heard of possible delays in care and to 64% when they heard of higher taxes (KFF, 2026) [EV-CAR-308]. The design meets both worries in public: waits by testing in wave 1, taxes by replacing premiums.

**"The government can't run it."** Medicare enrolled 19 million people from records in 1966 [EV-CAR-310]. HealthCare.gov's failed launch recovered in two months [EV-CAR-311] [EV-CAR-312]. The Medicaid unwinding failed on paperwork [EV-CAR-210] [EV-CAR-313], which is why the plan enrolls from records and renews without forms (HLT-7.02).

**"Single-payer estimates are all over the place."** They are: from 13% less national spending [EV-CAR-230] to 13% more [EV-CAR-223], and from $1.5 to $3.0 trillion of federal cost in 2030 [EV-CAR-218]. The range comes mostly from payment rates and benefits, which this design fixes (1.15 times Medicare; memo 4 C). Section 6, part 6 shows what each assumption moves.

**"Why not just a public option?"** Washington's public option, with rates capped at 160% of Medicare in aggregate, cut premiums little [EV-CAR-235]; and a public option leaves about 14.5 million uninsured in 2032 on the model (memo 1 A).

## 6. Signs of failure

Published counts, each with what it would trigger (none is a gate; `DEC-2026-11-09-13`):
- Readiness reports show a wave's systems untested six months before its date: Congress decides whether to delay that wave (section 8).
- Waits for specialists in wave 1 rise beyond a published benchmark: hold the rate glide and raise primary-care and workforce spending before wave 2.
- Hospitals in global budgets or the fund cut emergency, obstetric or behavioral health services: CMS reviews the budget or the award.
- Enrollment from records misses a group (newborns, people who move, people without tax records): add a record source, not an application.
- The settlement's revenue is not enacted 18 months before the endpoint: section 8's fallback.
