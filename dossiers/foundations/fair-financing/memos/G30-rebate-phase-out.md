# Memo G30: The VAT rebate's income limit

Role: decision memo for Espen. It is G24.1's open point: you chose to limit the VAT rebate to people below an income threshold (`DEC-2026-11-25-15`), and the threshold was to be proposed to you. Status: **provisional, not decided. Nothing booked.** Figures come from [`../notes/rebate-phaseout-results.md`](../notes/rebate-phaseout-results.md), written by `models/bookings/rebate_phaseout.py`. That script runs the same tools that price G24 B (`fiscal_revision.py` and the household model's tax units). These are project figures on exploratory models, not official scores.

## The question

G24 B (`DEC-2026-11-25-14`) adds a VAT from FY2035, with a rebate of $150 a point for every adult. The rebate is the VAT on the first $15,000 of each adult's spending. You wrote:

> "G24.1 VAT rebate income threshold: propose one. Maybe about 100,000 for a single person or 200,000 for a couple filing jointly? Idk and I'm open to lowering that significantly or refining. It's a partial rebate anyways, right?"

A lower limit means fewer people get the rebate, so each VAT point raises more and the rate can be lower. That was your aim: "If that moves the rate lower a bit that's good, but the overall goal should still be fiscal solvency." Every option below closes the same debt goal (G23 B) with the same money. Only the rate and who gets the rebate change.

## First: yes, it is a partial rebate

The rebate gives back only part of the VAT, even for the poorest households. FY2040, with no limit, at the VAT's current rate:

| Fifth of households | VAT paid a year | Rebate | Share given back |
| --- | --- | --- | --- |
| Lowest | $1,444 | $904 | 63% |
| Second | $2,247 | $1,064 | 47% |
| Middle | $3,049 | $1,148 | 38% |
| Fourth | $3,851 | $1,186 | 31% |
| Top | $5,456 | $1,202 | 22% |

- **Why it's partial:** it covers the VAT on the first $15,000 an adult spends. Most households spend more than that.
- **Who it's worth most to:** the rebate is about the same in dollars for everyone, so it matters most at the bottom. For the top fifth it is a fifth of what they pay.
- **The rate has moved since G24.** On today's booking, G24 B's VAT is **3.92%**, not about 4.9% as in memo G24. Memo G24's figures date from November 25. Before this PR's HEX fix it was 3.75%.

## The options

Below the threshold every adult in the tax unit gets the full rebate. Above it the rebate falls in a straight line to nothing across the phase-out range: $20,000 for a single person, $40,000 for a couple. A head of household uses the single figures.

Thresholds are in today's dollars, the same units as the AGI surtax's $100K/$200K, and rise with incomes.

| Limit (single / joint) | Phase-out range | Share of the rebate's cost kept | Net a VAT point | **VAT rate** | Workers ahead (take-home test) | Workers below 200% of poverty ahead |
| --- | --- | --- | --- | --- | --- | --- |
| No limit (G24 B as decided) | — | 100% | $48.2B | **3.92%** | 53.1% | 93.5% |
| $100K / $200K (your idea) | $100-120K / $200-240K | 79% | $57.2B | **3.30%** | 54.4% | 94.6% |
| $75K / $150K | $75-95K / $150-190K | 69% | $61.4B | **3.08%** | 54.5% | 95.1% |
| **$60K / $120K (recommended)** | **$60-80K / $120-160K** | **61%** | **$64.7B** | **2.92%** | **54.5%** | **95.4%** |
| $40K / $80K | $40-60K / $80-120K | 47% | $70.5B | **2.68%** | 54.2% | 95.8% |

The take-home test counts the VAT and the rebate, and G19 B's deduction limits, AGI surtax and the outside fix ($313B in FY2040). With none of these, 69.0% of workers are ahead, and 99.5% of those below 200% of poverty; the target is 85-90%.

**Who keeps the rebate:**

| Limit | Lowest fifth | Second | Middle | Fourth | Top |
| --- | --- | --- | --- | --- | --- |
| $100K / $200K | 100% | 100% | 99% | 81% | 22% |
| $75K / $150K | 100% | 99% | 92% | 51% | 12% |
| $60K / $120K | 100% | 98% | 78% | 32% | 10% |
| $40K / $80K | 99% | 86% | 45% | 15% | 7% |

What each option does:
- **Your $100K / $200K** takes the rebate from about a fifth of its cost, almost all of it in the top fifth. The rate falls by 0.6 of a point. Nearly everyone in the bottom three fifths keeps it.
- **$75K / $150K and $60K / $120K** reach into the fourth fifth. The rate falls by 0.8-1.0 points. Each limit lowers the VAT for everyone, so low-income workers come out a little better (95.1-95.4% ahead, against 93.5%), and so do workers overall.
- **$40K / $80K** gives the lowest rate, 2.68%. But it takes the rebate from more than half of the middle fifth, and workers overall do slightly worse than at $60K. The middle fifth pays $1,733 a household net of the rebate, more than under any limit from $60K to $100K ($1,562-1,614). Past $60K, lowering the limit starts to cost the middle more in rebate than it saves them in rate.

**Low-income workers gain at every limit**, because they keep the whole rebate and pay a lower VAT. In the lowest fifth the rebate still gives back 62-63% of the VAT.

**The phase-out adds to marginal tax rates inside its range.** At 2.92%, the rebate is about $440 an adult. Losing it over $20,000 is about 2.2 cents on each extra dollar for a single person, and the same for a couple over $40,000. A narrower range would mean a steeper rate; a wider one costs more.

## What a limit changes in how it is paid

G24's rebate needed no application and no income test. It was paid with the child benefit, Social Security and SSI, or as a refundable credit. With a limit it needs an income figure: last year's AGI from the tax return.
- People who don't file, nearly all below any of these limits, would still get it automatically.
- People whose income falls during the year would claim the difference on their next return, as with the 2020-21 recovery rebates.

## Recommendation

**$60K single / $120K joint, phased out over $60-80K / $120-160K.**
- **The rate:** 2.92%, a full point below the rebate for everyone (3.92%).
- **Households, net of the rebate:** the second fifth pays least here ($899, against $1,183 with no limit). The middle fifth pays $1,601, close to its best ($1,562 at $75K), and far below $1,901 with no limit.
- **Workers:** tied with $75K for the most workers ahead (54.5%, against 53.1% with no limit), and more low-income workers ahead (95.4%, against 93.5%). Of the two, it has the lower rate.
- **Who keeps it:** everyone in the bottom two fifths, and nearly four in five in the middle. The rebate goes mostly to the people it does the most for.
- **Your $100K / $200K is a sound, milder choice.** It takes the rebate almost only from the top fifth and still lowers the rate by 0.6 of a point.
- **I would not go to $40K / $80K.** Its rate is only 0.24 points lower than $60K's, and it takes the rebate from most of the middle fifth.

**Fiscal solvency doesn't depend on the choice.** Each option closes the same debt goal; the limit decides only how the load is shared.

## Limits of these figures

- The take-home test counts the rebate for the head and spouse of each worker's tax unit. The rebate's cost counts every adult, adult dependents included.
- Incomes are FY2040's on the household model's 2029 tax units, grown as the take-home test grows them. Spending by fifth uses D3's consumption key, not each household's own spending.
- There is no response to the limit, such as people timing income to stay below it.
- Households' VAT is counted gross, as D3 counts it: the Treasury's net yield over 0.75, since a VAT also lowers income and payroll tax receipts. A lower rate cuts that gross figure by more than the net, so every fifth pays a little less net of the rebate under any of the limits than with none. The Treasury's money is the same in every option.

## The question for you

**G24.1's threshold:** $60K single / $120K joint, phased out over the next $20K / $40K (recommended)? Or your $100K / $200K, or $75K / $150K, or $40K / $80K?
