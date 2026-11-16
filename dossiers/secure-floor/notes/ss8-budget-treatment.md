# SS-8: how the budget would record the trust funds' stock purchases

Role: research note on the known gap "SS-8 is booked at zero" (`charter/PROGRESS.md`, "Known gaps"; `../6-cost.md`, part 4; `models/tools/budget/MODEL-CARD.md`; `ASM-SS-FALLBACK`). It sets out the rules CBO and OMB apply to federal purchases of stock, what each would book for SS-8.01 as specified, and which decisions a different answer would change. Status: **research note, November 16, 2026. It proposes a working assumption and books nothing.** The figures in parts 3 and 4 are project arithmetic on the booked fund run, not scores. Bracketed tags point to `../evidence.json`.

## Bottom line

- **The default rule makes a stock purchase an outlay.** OMB's budget circular records a purchase of a non-Federal security, equity or debt, as an outlay equal to its price in the year bought [EV-SEC-711]. CBO scored President Clinton's 1999 plan, which put trust-fund money into an index fund, that way [EV-SEC-715], and GAO read the rules the same way in 1998 [EV-SEC-714].
- **The Railroad Retirement precedent shows the default can be changed by law.** The 2001 act made the Railroad Retirement trust's purchases and sales a means of financing, overriding the circular [EV-SEC-706]. CBO and OMB then agreed to count its dividends, interest and gains or losses, realized or not, as they occur, and to project its returns at the Treasury rate [EV-SEC-707] [EV-SEC-708].
- **So on CBO's and OMB's practice, SS-8 adds nothing to projected deficits once its law carries the Railroad Retirement clause.** That is what the model books now: zero. Without the clause, the default rule would add about **$0.5-0.6 trillion to the unified deficit over FY2030-39 and $24-46 billion in FY2040**. Counting the expected return above Treasury's rate, which neither scorekeeper does, would show a saving of about $0.09-0.11 trillion and $23 billion.
- **Proposed working assumption:** the Railroad Retirement treatment, written into SS-8.01's statute; budget rows at zero; debt held by the public about $0.7 trillion higher by the end of 2039, matched by the stocks held; the expected excess return counted only in the trust funds' 75-year measure. **No decision of Espen's changes.** One drafting line is needed in SS-8.01 (part 5).

## 1. The question

SS-8.01 puts up to 20% of the combined trust funds' reserves into a broad index of US stocks under an independent board, phased in from 2032 as the package's reserves grow (`../4-specification.md`, SS-8.01). The Social Security trust funds now hold only Treasury securities. To buy stocks, a fund would redeem Treasury securities, and the Treasury would borrow the cash from the public. So the government as a whole would owe more to the public and own an equal value of stocks. The question is how the budget would count that swap, and the stocks' returns.

Three treatments are possible:
1. **Outlays.** The purchase is spending; sales and dividends are receipts.
2. **Means of financing.** The purchase is a swap of assets, as borrowing is; only returns, gains and losses reach the deficit.
3. **Only returns above Treasury's rate counted.** This is the credit-reform analogue: the purchase is not spending, but the expected return above Treasury's rate is booked as a saving, on the model of a loan program with a negative subsidy.

## 2. The rules, with their sources

| Precedent | Rule | What reaches the deficit | Source |
| --- | --- | --- | --- |
| **The default (OMB Circular A-11)** | "The budget treats an investment in a non-Federal security (equity or debt security) as a purchase of an asset", with an outlay equal to the price in the year of purchase; sale proceeds are offsetting collections or receipts. The circular names credit reform and TARP's statutes as the exceptions | The purchase price at once; sales, dividends and interest as receipts; unrealized gains never | [EV-SEC-711]; CBO's description [EV-SEC-709]; GAO's [EV-SEC-714] |
| **National Railroad Retirement Investment Trust (2001), the nearest** | By statute, "notwithstanding section 20" of A-11, the Trust's purchases and sales of non-Federal assets "(other than gains or losses from such transactions)" are a means of financing. CBO and OMB agreed to recognize gains and losses in the year prices change, realized or not, and to record dividends and interest as offsetting receipts. In projections both use the Treasury rate: they subtract the equity premium | In history, actual income, gains and losses. In the baseline and in scores, the Treasury-rate return, so a purchase scores at zero | [EV-SEC-706] [EV-SEC-707] [EV-SEC-708]; OMB lists the Trust's net purchases among the means of financing [EV-SEC-711] |
| **The Railroad Retirement estimate before the clause** | CBO's estimate of the bill, made on the A-11 rule, showed the first transfer to the Trust as $15,320 million of outlays in 2002 and negative outlays of $460 million to $920 million a year after, against zero under the clause | Shows the size of the gap between the two treatments | [EV-SEC-710] |
| **Thrift Savings Plan** | Outside the budget. The government holds the money as a true trustee for individual employees, in deposit funds it does not own; CBO: the Plan is administered solely for its beneficiaries and holds investments "in a fiduciary capacity for private owners". | Nothing from the investments | [EV-SEC-712] [EV-SEC-713] |
| **Federal credit reform (1990)** | Loan and guarantee cash flows are a means of financing; the outlay is the subsidy cost, the present value of expected cash flows at Treasury rates | Expected net cost at a Treasury discount rate. Applied to stocks, the expected equity premium would show as a saving; CBO says Treasury-rate discounting "could result in reported valuations that significantly exceeded the economic value of those investments" | [EV-SEC-712] [EV-SEC-709] |
| **TARP (2008)** | Equity purchases scored under credit reform, but with the discount rate "adjusted for market risks" | Market-price purchases score near zero; the equity premium is not counted as a saving | [EV-SEC-717]; CBO's fair-value reasoning [EV-SEC-716] |
| **CBO on Social Security equity investment** | 1999: the President's plan to buy $280 billion of stock for the trust funds was scored as reducing the surplus by that amount, on the cash rule [EV-SEC-715]. 2003: CBO set out the cash and means-of-financing treatments, said the choice "requires political judgment", and held that once risk is priced, "the returns on private securities would be no greater than the returns on government securities" [EV-SEC-708] [EV-SEC-709]. Its rule for the baseline is the Railroad Retirement one: a Treasury rate | No projected gain from the equity premium | [EV-SEC-708] [EV-SEC-709] [EV-SEC-715] |

**Where the sources disagree.** CBO's view that risk-adjusted stock returns equal Treasury's is standard finance and is shared by OMB's practice for the Railroad Retirement trust [EV-SEC-707]. Advocates of equity investment count the expected return instead: the Cassidy-Kaine sponsors' claim that their fund pays 65% of the obligation rests on it [EV-SEC-467]. Both views are honest about different things. The expected return is the right figure for the trust funds' likely path, which is what the 75-year measure and SS-7.01's trigger read. The Treasury-rate figure is the right one for what the budget can promise, since the premium is a payment for risk that taxpayers and beneficiaries carry. The note keeps them apart (part 4).

**What none of the precedents settles.** No precedent applies to Social Security itself. The trust funds are off-budget, and SS-8's purchases would be off-budget too. That leaves the on-budget totals, and the project's general-fund reading, unaffected under every treatment (part 4). Whether CBO would apply the Railroad Retirement treatment to Social Security without a statutory clause is not known. CBO's own estimate of the Railroad Retirement bill used the cash rule, and CBO wrote that without the clause it and OMB "might have used cash-basis accounting" [EV-SEC-710]. So the clause should be in the bill.

## 3. SS-8 as booked: how much stock, and when

The base is the budget model's booked fund run for the decided package (case `mixed`; `models/data/recovery-budget.json`, combined OASDI reserves at the end of each calendar year): $1.60 trillion in 2032, $2.38 trillion in 2035, $3.68 trillion in 2039 and $4.07 trillion in 2040. That run carries SS-7.01's one point from 2037 and SS-8 at zero. SS-8.01 does not fix a phase-in pace, so two cases bound it: **20% at once from 2032**, and **4 points a year, reaching 20% in 2036**. Calendar years stand for fiscal years. The equity premium over Treasury is 3%, the figure `../6-cost.md` part 4 uses, with dividends at 2% of holdings.

| | 2032 | 2035 | 2039 | 2040 |
| --- | --- | --- | --- | --- |
| Reserves (booked run) | $1,600B | $2,383B | $3,677B | $4,066B |
| Stocks held, 20% at once | $320B | $477B | $735B | $813B |
| Stocks held, phased to 2036 | $64B | $381B | $735B | $813B |
| As a share of GDP | 0.2-0.8% | 0.8-1.1% | 1.4% | 1.5% |

Both cases end the decade with about $0.7 trillion in stocks, so the treatments' ranges below come mostly from the premium, not the pace. The expected excess return is about $23 billion in 2040, 0.12% of taxable payroll. That is inside the +0.05 to +0.2 that `../6-cost.md` part 4 gives SS-8's 75-year effect, so this note confirms that range rather than revising it. The legacy +0.5 to +1.0 [EV-SEC-697] would need reserves several times larger, as the milestone review found.

## 4. How each treatment would book SS-8

Positive figures raise the deficit. "Unified" is CBO's headline deficit and the project's unified reading, which the D4 debt guardrails use (`models/tools/budget/CONVENTIONS.md`, section 3 and choice 5). The general-fund reading, which the D4 maturity test uses, excludes the trust funds. It is **zero under every treatment**. The general fund pays the same interest whether the debt is held by the trust funds or by the public; only who holds it changes.

| Treatment | Unified, FY2030-39 | Unified, FY2040 | General fund | Debt held by the public, end of 2039 | Trust funds' 75-year measure |
| --- | --- | --- | --- | --- | --- |
| **1. Outlays (A-11's default; no clause)** | **+$0.49 to +$0.62 trillion**: purchases less dividends. Gains are recorded only when stocks are sold | **+$24 to +$46 billion** | 0 | +$0.7 trillion, all of it through the deficit | Unchanged by the treatment: +0.05 to +0.2 at the expected return |
| **2. Means of financing (the Railroad Retirement clause), projected at Treasury's rate** | **0 in projections.** The interest on the extra public debt (about $0.13-0.16 trillion) is matched by the stocks' Treasury-rate return, recorded as offsetting receipts. Actual results show up as they happen, a gain or loss each year | **0** | 0 | +$0.7 trillion through the means of financing, matched by about $0.7 trillion of stocks | Same |
| **3. Only returns above Treasury's rate counted (credit reform at a Treasury rate)** | **−$0.09 to −$0.11 trillion**, the expected premium booked as a saving | **−$23 billion** | 0 | +$0.7 trillion through the means of financing | Same |
| *TARP's market-risk rate, or fair value* | *0, as in treatment 2* | *0* | *0* | *As in treatment 2* | *Same* |
| *Thrift Savings Plan model (outside the budget)* | *Not available: the reserves, and their gains and losses, are the government's* [EV-SEC-713] | | | | |

How to read the table:
- **Treatment 1's range** comes from the premium. At a 3% premium the stocks grow in value, so less new money is needed to hold 20%: $0.49-0.54 trillion net over FY2030-39. At no premium it is $0.59-0.62 trillion. In FY2040 it is $24 billion at the premium and $46 billion without it. The extra public debt's interest is not added on top: the model's interest on program borrowing already follows a cash-basis outlay. It is real under every treatment; only treatment 2 records an offset for it.
- **Treatment 2 is what the model books now.** At zero, SS-8's row is already right for projected deficits under the Railroad Retirement practice. What zero leaves out is the swap of debt for stocks, about $0.7 trillion by 2039 and $0.8 trillion in 2040 (1.5% of GDP). Debt held by the public rises by that much without a deficit, as it does for student loans.
- **Treatment 3 is not CBO's or OMB's practice for stock.** CBO calls this the appearance of "arbitrage profits" [EV-SEC-708]. TARP's statute rules it out for equity [EV-SEC-717]. It is shown only as the low end.
- **The trust funds' own measure is a separate question.** The Trustees' and SSA's actuaries' 75-year projections are made on expected returns, not risk-adjusted ones. On that measure SS-8 adds its +0.05 to +0.2 whatever the budget treatment, and SS-7.01's trigger reads those reports. How SSA's actuaries would project the stocks' return is not in the register (part 7).

## 5. What a different treatment would change

Treated under "What needs an answer now" (`charter/STANDARDS.md`):

| Decision | Would a different treatment change it? | How to treat it |
| --- | --- | --- |
| Memo 6 C, SS-8 with SS-7.01 as the fallback (`DEC-2026-11-12-06`, `-13`, `-16`) | **No.** The budget treatment changes how the swap is reported, not the real resources. GAO: the government's "fundamental fiscal position would be largely unchanged" [EV-SEC-714]. The case for C rests on the 75-year measure, which no treatment moves | Not reopened |
| SS-8.01's text: whether the act carries the Railroad Retirement clause | **Yes.** Without the clause the default rule (treatment 1) can apply, and the scored unified deficit is about $0.5-0.6 trillion higher over FY2030-39 [EV-SEC-710] [EV-SEC-711] | **Decide now, as a working choice in the specification.** It is a drafting term of a decided commitment, not a fork. Add a sentence to SS-8.01: the board's purchases and sales of non-Federal securities are a means of financing for budget purposes, with income, gains and losses recorded as offsetting receipts in the year they occur. The 2001 act's section 105(c) is the model [EV-SEC-706]. Not this note's file to edit; for the lead to place (For the board) |
| The booking (`../6-cost.md`, part 6, item 5; `ASM-SS-FALLBACK`) | **Only in what is disclosed.** Zero stays the booked row on the working assumption | **Use a working assumption** (part 6). The booking can proceed; this does not block it |
| The D4 debt guardrails (unified; choice 5) | **Possibly, under treatment 1 only.** About $50-60 billion a year (about 0.1-0.15% of GDP) on the unified deficit; nothing on the general fund | **Leave it open** while the clause is the working choice. It matters only if the 2030 act is written without the clause; then the guardrail test should be re-run with treatment 1's path. Debt held by the public is higher by about $0.7 trillion under every treatment; a guardrail that reads gross debt sees it, one that reads debt net of financial assets does not. Report it as a memo line |
| The D4 maturity test (general fund) | **No.** Zero under every treatment | None |
| SS-8's share and SS-7.01's start (working choices, `../8-change-our-minds.md`) | **No.** They turn on the expected return, the trust-fund measure | Unchanged; SSA's score (point 12) settles the yield |

## 6. Proposed working assumption (not booked)

- **Value.** SS-8.01 carries a Railroad Retirement-style means-of-financing clause. Budget rows: **0** on the unified and general-fund readings over FY2030-39 and in FY2040, as now. Memo lines:
  - debt held by the public about **$0.7 trillion** higher at the end of 2039 and **$0.8 trillion** in 2040, matched by the stocks held;
  - the expected excess return, about **$23 billion in 2040**, counted only on the trust funds' 75-year measure (+0.05 to +0.2% of payroll), never on the unified reading.
- **Basis.** The 2001 statute [EV-SEC-706]; CBO's and OMB's practice under it, recording actual gains and losses and projecting at the Treasury rate [EV-SEC-707] [EV-SEC-708]; OMB's current listing of the Trust's purchases among the means of financing [EV-SEC-711]; CBO's and TARP's refusal to count the equity premium as a saving [EV-SEC-708] [EV-SEC-716] [EV-SEC-717].
- **Range.** High: treatment 1, +$0.49 to +$0.62 trillion over FY2030-39 and +$24 to +$46 billion in FY2040 on the unified reading, if the act is written without the clause. Low: treatment 3, −$0.09 to −$0.11 trillion and −$23 billion, which no scorekeeper would use for stock. General fund: zero across the range.
- **Cost of being wrong.** If the clause is left out or struck, the unified deficit is reported about $50-60 billion a year higher in the 2030s. The real fiscal position does not change, and nothing moves on the general fund. If actual returns fall short of Treasury's, treatment 2 records the loss in the year it happens, a unified cost that the model does not carry today. That market risk is what SS-7.01's fallback covers on the trust-fund side.
- **How the booking should carry it, when the lead books it.** Keep SS-8's unified and general-fund rows at 0. Add the debt-for-stocks swap as a disclosed memo line beside the D4 debt table. Put the expected excess return only into the fund engine's 75-year balance, and keep it out of the trust-fund revenue that feeds the unified reading. Otherwise the model would count the equity premium as deficit reduction, which is treatment 3.

## 7. Evidence still needed

- CBO's cost estimate for H.R. 1140 (May 24, 2001) itself, cited here only through CBO's 2003 paper [EV-SEC-710].
- The Fiscal Year 2003 *Analytical Perspectives*, pp. 439-440, OMB's own statement of the Treasury-rate projection [EV-SEC-708, note 2].
- A current CBO or OMB line showing the Trust's gains and losses in recent outlays, such as a Monthly Budget Review entry, to confirm the practice still holds as CRS described it in 2022 [EV-SEC-707].
- How SSA's actuaries would project the stocks' return for SS-8.01: their real equity return and any risk adjustment. Point 12's whole-package score should ask for it.
- CBO's 1999 analysis from CBO's own copy; the register quotes Tax Notes' reproduction [EV-SEC-715].

## For the board

- **Done:** the SS-8 budget-treatment research. Twelve evidence entries (EV-SEC-706 to 717) on eight new sources (SRC-3996 to 3999, 3628, 3629, 3666, 3667). The rules: the default makes purchases outlays; the Railroad Retirement clause makes them a means of financing, with returns projected at Treasury's rate. Proposed working assumption: zero on the budget rows as booked, a disclosed $0.7 trillion debt-for-stocks memo line, and the excess return only on the 75-year measure.
- **Next, for the lead:** add the means-of-financing sentence to SS-8.01 in `../4-specification.md`, and name it in `../6-cost.md` part 4. Close the known gap on the board; `ASM-SS-FALLBACK`'s note and `MODEL-CARD.md` can then say "settled as a working assumption" at the booking's next touch (tier 3).
- **For Espen:** nothing. No decision changes.
