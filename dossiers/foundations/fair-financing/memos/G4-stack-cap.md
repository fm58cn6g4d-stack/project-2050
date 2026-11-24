# Memo G4: The cap on the capital-income stack

**Decided:** C1, `DEC-2026-11-20-08`. Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 4 of stage G's batch ([`README.md`](README.md); [`../2-settlement.md`](../2-settlement.md) part 3; `../1-audit.md` part C, item 11). Status: **provisional, drafted on the recommendation, November 20, 2026.** Not decided, not booked. Figures are FY2040 nominal $B on the project's exploratory models, not official scores. Every cost is the revenue a cap gives up on the ledger's own scoring, from the stack note's menu (`../../notes/stack-2026-11-16.md` part 4), and is priced by `models/tools/financing-protection/packages.py`.

## The question

The plan stacks several taxes on the same investment income at the top. Above $1 million of income, gains and dividends are taxed as ordinary income (HS3) at up to 45% (C43), plus the 5% investment-income tax (H1b), 12.4% for Social Security (SS-2), the income contributions and the health contribution's surcharge. On top of that sit a yearly wealth tax of 2% above $50 million and 3% above $1 billion (HS2) and, for billionaires, gains taxed every year as they accrue (G11).

On a 6% return, the wealth tax alone takes 33 points of the return at 2% and 50 points at 3%. Together, the charge on the last dollar of return is **105-109% for anyone above $50 million who is taxed on the return each year, and 126% for billionaires** (stack note, 2.4). A charge above 100% means holding a taxable, easily valued asset loses money. That is when avoidance, moves into hard-to-value private holdings, giving and expatriation pay most [EV-CAR-736] [EV-CAR-738].

**Already decided:** Espen approved the wealth tax with the instruction that "stage G caps the wealth and accrual taxes together" (`DEC-2026-11-15-16`). So the question is which cap, not whether to have one.

## The options

| | Design | Gap cost, FY2040 (range) | Gap cost, FY2030-39 | Highest combined charge after it |
| --- | --- | --- | --- | --- |
| **B1** | Drop the 3% tier: 2% on all wealth above $50M | +16 (13-20) | +131 | Billionaires 126% → 109%; still above 100% |
| **C1 (recommended)** | A ceiling: the wealth tax is cut, taxpayer by taxpayer, so that it plus the federal income taxes on a 6% return on the same wealth never exceed 100% of that return | **+40 (30-55)** | **+328** | 100% by construction |
| **D2** | Billionaires pay the larger of G11 or the wealth tax, not both | +50 (35-75) | +410 | Billionaires about 76% in up years; $50M-$1B unchanged at 105-109% |
| **D1** | Income taxes on capital credited against the wealth tax, so it becomes a minimum tax on wealth | +100 (80-120) | +820 | About 76% |

**B1, drop the 3% tier.**
- *Cost:* the cheapest, at $16B. At high avoidance (ε = 25%) it may even raise revenue (stack note, part 4).
- *What it fixes:* only the billionaires' extra tier. Everyone between $50M and $1B taxed each year stays above 100%.
- *Burden:* none added.
- *It does not meet the instruction,* because the combined charge still passes 100%.

**C1, a ceiling at 100% of a 6% imputed return (recommended).**
- *Cost:* $40B (30-55) in FY2040.
- *What it fixes:* no holder's combined federal charge passes 100% of a normal return.
- *Burden:* small. The wealth-tax return already values the assets. The ceiling adds one line: 6% of net worth, less the year's federal income taxes on capital, caps the wealth tax.
- *What it leaves:* a charge up to 100% is still very high. For holders with returns above 6% the cap doesn't bind. Avoidance at the top is still the main risk to HS2's $150B (stack note 3.3).

**D2, the larger of G11 or the wealth tax for billionaires.**
- *Cost:* $50B (35-75).
- *What it fixes:* the 126% billionaire case. It leaves the $50M-$1B group above 100%, so on its own it doesn't meet the instruction.
- *Burden:* low. One comparison on the billionaire return.

**D1, a minimum tax on wealth.**
- *Cost:* $100B (80-120), two-thirds of HS2.
- *What it fixes:* everything. The combined charge is the larger of the two layers, at most about 76%.
- *Burden:* the simplest rule to explain.
- *Revenue:* most of the wealth tax's money is gone. It mostly reaches holders whose income-tax bill is low: those who defer gains or hold assets with low cash yields.

## Recommendation

**C1**, a ceiling at 100% of a 6% imputed return. It is the cheapest design that meets the instruction for everyone, and it keeps most of HS2's revenue.
- It adds one line to a return the wealth tax already needs.
- It costs $40B in FY2040 and $77B in FY2056, which the settlement's package covers (memo G3's VAT rate includes it).

**What would change this:**
- If Espen wants the wealth tax to be defensible as a minimum tax in court, or simpler to explain, then **D1**. It costs $60B more in FY2040, about 0.65 more points of memo G3's VAT.
- If evidence of high avoidance firms up (Switzerland's 43% per point, not Saez and Zucman's 8%), then B1 plus C1 together: dropping the 3% tier may cost little or nothing.

**Not a cap on wages.** The wage stack is 68.3% at $500K and 72.7% at $20M in FY2040 (stack note, part 1). A statutory ceiling there (F5) would cost $110-430B. It is not in this memo. The settlement treats the yield at the top as a working assumption with a range instead (`../2-settlement.md` part 5).

## Consequences of each option for real households

- No household below about $50 million of net worth is touched by any of these options.
- Under **C1**, a household with $200 million in listed shares earning 6% ($12 million) pays federal income taxes of about $8.6 million on it. The wealth tax ($3.0 million at 2% above $50M) is capped at $3.4 million, the room left below $12 million, so here the ceiling doesn't bind. A billionaire taxed every year under G11 is where it binds: there the wealth tax is cut to whatever room is left below 100%. The ceiling uses a 6% imputed return, not the year's actual return, so a bad year can't be used to escape the wealth tax.
- Under **D1**, the same household pays the larger of $8.6 million or $3.0 million, so the wealth tax adds nothing in that year.

## Question for you

**G4.** Cap the wealth tax and the accrual taxes together with **C1**, a ceiling at 100% of a 6% imputed return (recommended; +$40B in FY2040), or B1, D2 or D1?
