# The single health plan: an independent cost review, and financing that passes the take-home test

Role: the stage E memo that tries to break `health-financing.md`'s cost estimate, then redesigns the financing around Espen's take-home test (November 15). Status: **outline, in progress (draft PR)**. Nothing here is booked. Corrections to the booked rows and adopted inputs go to a later tier-3 booking PR.

## Outline (the one page, first push)

**Why this memo.** Espen, November 15: "costs are simply coming out way too high", and the plan has to "cut costs on the 'visible' side of the ledger for workers", meaning the money they see leave their paycheck and wallet. A raise from the employer doesn't count.

**Part 1. Cost review: why does the plan save only about 6%?**
- A line-by-line audit of the code behind the $8.4 trillion gross cost (`health_path.groups()`, the coverage model's `run_single_payer()`, `health_financing.system_view()`), with each repricing step rebuilt by service and payer from CMS's 2024 spending table (Table 19: hospital, physician, drugs and so on, for each payer).
- **Errors found so far (being sized):**
  1. **The newly covered are priced at an average that includes Medicare enrollees.** About $13,500 a person in 2032 at plan prices, against about $8,100 for a person moving from an employer plan. The uninsured are almost all under 65.
  2. **Physicians are priced at the hospital rate** (#386's part 1.2b), 1.15 instead of about 1.05.
  3. **Medicaid's hospital payments are taken at its physician fee index (0.72 of Medicare).** With supplemental payments, Medicaid pays hospitals close to Medicare's rates. So the cost of "raising Medicaid to the plan's rates" is overstated.
  4. **A Medicaid seam, like the Medicare one.** CMS's Medicaid growth path puts 2032 Medicaid about $110B above what CBO's February 2026 baseline implies. It also inflates the states' share, and with it package A's states' payment.
  5. **Checks in the other direction:** each payer's hospital share (the model uses one national share for all, which overstates commercial prices and so the private savings); Medicare enrollees' out-of-pocket costs repriced at commercial prices; nursing-home and over-the-counter out-of-pocket spending moved into the plan.
- **Every driver** gets the plan's assumption, the evidence, the FY2040 effect on gross cost, national spending and the household rate, the risk to quality and access, and a grade. The drivers are: hospital rates and the glide, physicians, administration, drugs, copays and induced use, Medicaid's rates, the newly covered, long-term care, the growth path, the other payers, double counting, and provider-side administrative savings. The literature: Urban 2019, CBO 2020, Galvani 2020, PERI 2018, RAND, Mercatus 2018, Yale and later work, OECD and Commonwealth Fund prices.
- An independent subagent re-derives the headline figures, and part 1 records what it found.

**Part 2. Financing that passes the take-home test.**
- **The test:** for typical workers, what visibly leaves take-home pay and wallet under the plan (the household contribution, any worker payroll charge, copays) must be less than today's (their premium share plus out-of-pocket costs). The grid: single and family, $25,000 to $200,000 of AGI, with job coverage, without it, and with a plan of their own. It reports the share passing at each income, and who fails and why.
- **Employers:** at or below what they would otherwise spend; small firms and firms that offered no coverage treated gently.
- **General revenue from other streams** for what remains after the cost fixes, each stream priced with its evidence and checked for overlap with what the plan has already booked: corporate taxes, a wealth tax, a financial transactions tax, capital gains taxed as ordinary income and at death, loopholes and the tax gap. Warren 2019 is the model. Health has first call on the plan's revenue (Espen), so the memo shows what that takes from the other flagships.
- **A household contribution that typical workers don't see,** for example one that starts above a high line. Its rate is shown three ways.
- **Two to four packages**, each with: its take-home grid; the single worker at $72,000; net effects by fifth; loser counts; employer burden by firm size; durability (visible costs, growth against income, legal risk); and the plan-wide gap.

**Presentation:** a reference card and glossary at the top; "In plain terms" first; households in 2026 dollars, budget totals in FY2040 nominal dollars; AGI throughout; every rate as the rate, the dollars and the share of AGI; today against the plan like with like.

**Code:** `models/tools/health_cost_review.py`, with `models/tools/test_health_cost_review.py`.
