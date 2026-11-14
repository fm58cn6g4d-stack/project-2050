# Clean power: re-review on the energy model

Role: the re-review of the clean power dossier on the new energy and climate model, `MOD-energy` (`models/tools/energy/`, M4 part 2, #347), which Espen asked for before the booking (`DEC-2026-11-13-12`: book once, after this re-review and its fixes). It runs the decided set end to end on the new model, compares the results with sections 4-9, settles the questions the milestone review (`review-milestone.md`, #344) and its fixes (#346) left for it, and lists what the booking (tier 3) must use. Status: current, as of main at `9578318` (after #347 and #348). Reviewer: Claude Code, `session_01UQzgButU9bQRw8o2Tq3QvS`, who also wrote the milestone review and its fixes. The model is not edited here: one finding about it went to the M4 session and the lead (R-2). This PR also carries the fixes.

## Verdict

**The dossier holds on the new model.** Its arithmetic and the model's run of the decided set agree within 1-2% on every line they share:

| Line, nominal $ billion | Dossier (`tools/clean_power_path.py`, booked basis) | Energy model (`results.json`, decided set) |
| --- | --- | --- |
| Carbon price receipts, FY2030-39 (FY2040) | 1,203 (166) | 1,191 (167) |
| Transition share, FY2030-39 (FY2040) | 241 (33) | 238 (33) |
| Offset on the combustion price, border adjustment and methane fee, FY2030-39 | 306 | 307 |
| Dividend per adult, 2035 | $439 | $409 |

The general fund's figures barely move: about **$1.85 trillion over FY2030-39 and $146 billion in FY2040** (+$0.04 trillion and −$18.5 billion against the booked rows). Only the transition guarantee's timing changed. The model moves five things the dossier carried on judgment or on the legacy model, and settles the two questions left for it:

| | Before (#346) | On the energy model | Section |
| --- | --- | --- | --- |
| Clean power, 2035 / 2040 | 75% / 91% (legacy, with permitting) | **73% / 88%**, 92% in 2045 | R-1 |
| The standard's capped payments | $0.11 trillion; $29 billion in 2040 | **$0.16 trillion; $41 billion in FY2040** ($0.07 trillion and $21 billion with permitting) | R-1 |
| Energy CO2 below 2005, 2035 | 40-48% (judgment) | **about 41%** (band 39-42%); net GHG 43% | R-7 |
| Dividend per adult, 2035 | about $439 | **about $409** (a couple about $820) | R-5 |
| Carbon channel, 2035, lowest to highest fifth | +62, +46, −6, −154, −654 | **+106, +91, +11, −186, −850** | R-8 |
| The credits' cost risk over the booking | up to +$0.74 trillion | **about +$0.27 trillion** (+$0.43 trillion with the builder's extra credits) | R-6 |
| The transition guarantee | $12 billion; $1.7 billion in FY2040 | **$14 billion; $0.7 billion in FY2040** (coal closes by 2035) | R-9 |
| The transition share after FY2039 | open | **the waterfall, then a remainder of about $23 billion a year: for Espen** | R-3 |
| The builders' borrowing | open | **time-limited capital, repaid from rates; net cost is forgiveness only** | R-4 |

## How it was done

- Read the model's card, `results.md` and `results.json` at `9578318`, and the engine's retail-price and standard code (`engine/cfd-model.js`).
- Ran `dossiers/clean-power/tools/clean_power_path.py`. It now reads the model's `results.json` and prints the comparison above (`m4_compare`). The model's own run (`run.py`) was not rerun here; its outputs are committed and drift-checked by the rebuild.
- Checked the ledger's treatment of the fee, the dividend and the transition share in `models/tools/ledger-build.py` and the booked audit lines.

## Findings

**R-1. The standard's payments, settled: $0.16 trillion over FY2030-39 and $41 billion in FY2040.**
- On the energy model the decided set reaches 73% clean power in 2035, 88% in 2040 and 92% in 2045. It is held back by grid access, not price, as on the legacy model. Suppliers pay the $40 cap on the shortfall: $9 billion in 2032, rising to $41 billion in FY2040, then $20-36 billion a year to 2050.
- **Reconciling the three figures:**
  - #346's $0.11 trillion came from the legacy carbon model, which assumes the 2026-28 permitting package in every run.
  - The energy model with the package gives $0.07 trillion and $21 billion. That is lower than the legacy figure because its standby builder adds lines.
  - The $234 billion the reviewer quoted is the model's layer before the standby builder.
  - The dossier now carries the energy model's figure without the package (the 2029 law), with the package case as the low end.
- **The offset.** The model applies none ("a capped compliance payment, not a tax"). The payments are a cost to suppliers collected by Treasury, like a fee, so the plan's convention (`DEC-2026-11-12-08`) points to applying the 24.4%: about $39 billion over FY2030-39 and $10 billion in FY2040. That is the booking's call (tier 3). It is noted in `6-cost.md`, parts 2 and 6.
- **Fixed:** CLI-3A.02 and the consistency table; `6-cost.md`, part 2 and part 6 (6a), and part 7; `7-validation.md`, parts 1 and 2; section 8's trigger (about 12 points short in 2040).

**R-2. The model's retail price leaves out the standard's payments. Reported to the M4 session and the lead; the dossier states it.**
- In the engine, adding the 100% standard leaves the 2040 retail price unchanged (15.0 cents before and after), though suppliers pay about $41 billion that year.
- The engine passes the standard to costs as a credit price: fossil generators pay it, clean generators receive it. The capped payments to Treasury never enter the average cost (`engine/cfd-model.js`, the `vc` term against `cesAcpBn`).
- Passed through, they add about two-thirds of a cent a kilowatt-hour by 2040: about $29 billion in 2025 dollars over about 4,500 TWh, roughly 4% of an average bill.
- So the model's headline, a 2040 price equal to current law's 14.7 cents, understates bills by that much.
- This does not change a decision, and the money returns through the bill credit. But section 9's bill answer must not lean on "no increase by 2040", and the household table's electricity column is low by the same amount.
- **Fixed in the dossier:** `7-validation.md`, parts 2 and 4. The model's fix is the M4 session's.

**R-3. The transition share after FY2039: the waterfall is decided, the remainder is Espen's.**
- **How the ledger books it.** `models/tools/ledger-build.py` books CLI-2's outlay as the whole carbon fee. The 20% transition share finances the add-ons (CLI-5) through FY2039. From FY2040 the add-ons end, but the share still counts as spent: about $33 billion a year that funds nothing.
- **The waterfall** (CLI-2A.04, point 5, decided) pays the guarantee and the bill credit from the share first: about $10.6 billion in FY2040.
- **The remainder,** about $23 billion a year, has no named use in any decision.
- **The default.** Held as general-fund receipts, which is how the money stands unless a law spends it, it lowers clean power's FY2040 cost from about $146 billion to about $113 billion. That is about −$52 billion against the booking instead of −$18.5 billion.
- **Alternatives:** raise the dividend from FY2040 (to 100% of combustion receipts less the waterfall), or a standing transition and adaptation fund.
- Which one is a choice about who gets money, so it goes to Espen (below). The booking should record the waterfall and hold the remainder as receipts until Espen answers.
- **Fixed:** `6-cost.md`, parts 2, 4, 6 (6d) and 7; the README's open question.

**R-4. The builders' borrowing: time-limited capital, repaid from rates.**
- **How the model counts it.** It represents the standby builder of last resort (CLI-10.03, `DEC-2026-11-13-10`) as its federal grid program at half strength (`assumptions.csv`, `grid_standby_scale`, range 25-100%). It counts about $161 billion over FY2030-39 against it, inside its credit figure. Of that, about $6 billion a year (2025 dollars) is the program's own cost, which overlaps the second tranche (CLI-10.01, $60 billion). The rest is the extra wind, solar and storage its lines connect, which earn credits.
- **For the booking:**
  - book TVA's, Bonneville's, WAPA's and the eastern corporation's line capital as time-limited capital (D4-B), with outlays as built and rate repayments over the lines' lives;
  - count as net cost only expected forgiveness of unrepaid balances [EV-CLP-465] [EV-CLP-466];
  - do not book the model's program cost on top of the second tranche;
  - put the extra credited generation under CLI-1's risk.
- **Fixed:** `6-cost.md`, part 6 (6e) and part 7.

**R-5. Receipts, the offset and the dividend reconcile; the dividend is a little smaller.**
- Combustion receipts under memo 1 B are $1,191 billion against the dossier's $1,203 billion on the booked basis, and the offset matches to the billion (table above).
- The dividend per adult is $409 in 2035 against the dossier's $439, because the model prices industry at an assumed 80% covered share (70-90%; `assumptions.csv`, `ind_cover`). No count of combustion CO2 above the 25,000-ton threshold is in the evidence yet.
- The model's receipts run 26% above CBO's on CBO's price path (its PR-2 benchmark fails). The engine cuts emissions slowly in its first decade, so the receipts and the dividend are the high side of a range.
- **Fixed:** CLI-2A.01, "Who this reaches" and the consistency table; sections 7 and 9 ($410; a couple $820); the PR-2 caution in section 7, part 2.
- Process receipts ($265 billion against the booked $244 billion) and the border adjustment ($45 billion against $30 billion) are the booking's to update.

**R-6. The credits' cost risk is smaller than the legacy model said.**
- The model counts the decided set's credits at about $1.03 trillion over FY2030-39 before the standby builder, and $1.19 trillion with the extra credited generation its lines connect. That is against the booked $0.76 trillion: a risk of about +$0.27 trillion, or +$0.43 trillion with the builder.
- The legacy model's $1.50 trillion gave +$0.74 trillion.
- The model's power credits stop at its emissions trigger, not CLI-1A.02's 60% step, so this is a cross-check, not a score.
- **Fixed:** `6-cost.md`, part 2.

**R-7. Emissions: about 41% below 2005 in 2035.**
- Energy CO2 is 41% below 2005 in 2035 and 52% in 2040; net greenhouse gases 43% in 2035 and 66% in 2050. The uncertainty band is 39-42%, a floor on the real uncertainty.
- The judged 40-48% is replaced. The decided set sits at its low end, because the standard's level barely matters when the grid is the limit, and buildings respond through the clean-heat standard only as equipment turns over.
- Memo 1 A's economy-wide fee would have added almost nothing by 2035.
- The Energy Policy Simulator check Espen ran stands as the model reports it: current law within 3 points (BL-3); the simulator's wider package 43% from 2025 to 2035 against the decided set's 30% (PK-1).
- **Fixed:** `7-validation.md`, parts 1 and 5; section 9 ("about 41%").

**R-8. Who comes out ahead: the same shape, by more at the bottom.**
- On the model's household module in 2035, the lowest fifth is +$106, the second +$91, the middle +$11, the fourth −$186 and the highest −$850 (2025 dollars, carbon channel).
- The model nets the credits out of retail prices, so electricity costs households less than in the legacy read.
- The standard's payments are not in its electricity column (R-2). They return to lower- and moderate-income households through the bill credit.
- **Fixed:** `7-validation.md`, part 4, and the illustrative households.

**R-9. The coal and gas fleets: closures come early.**
- On the model the decided set leaves 31 GW of coal in 2030 and none by 2035, against 127 and 89 GW under current law.
- Gas plants stay open and run less: capacity rises from 591 to 699 GW by 2040 while generation halves.
- So the transition guarantee's closures come early and are mostly coal: the same 80,000 workers over FY2030-39 as before, but 14,000 a year in 2030-34 and 2,000 a year in 2035-39 (judgment on the model's fleet path).
- Repriced: about $14 billion over FY2030-39 and $0.7 billion in FY2040, against $12 billion and $1.7 billion. The FY2040 decided set falls by $1 billion.
- **Fixed:** `tools/clean_power_path.py` (`PROFILE`); `6-cost.md`, parts 1, 4 and 5; sections 7 and 9 ("about $14 billion").

**R-10. Not answered by the model.**
- **Bills by region.** The engine is one national market. Section 7, part 2 keeps the regional caution.
- **The bill credit's matched households.** The 2027-28 preparation match answers it.
- **The guarantee's cost** beyond the closures. The dossier prices it.

## What the booking (tier 3) must use

1. **The energy model's `results.json` `provisions`** for:
   - the year shapes of REV-C1A/C1G, C1P, C2, C3 and CX;
   - the standard's payments (CLI-3A.02: $160 billion, $41 billion in FY2040), as a receipt and an outlay to the bill credit, with the 24.4% offset if the booking applies it (R-1).
2. **The dossier's booked-basis changes** (`tools/clean_power_path.py`) against the ledger: memo 1 B's offset saving and lost add-on financing, memo 4 B's second tranche, memo 5 B's bill credit, and memo 7 B on the new closure profile. They reconcile with the model within 1-2%.
3. **Receipts as the high side of a range** (PR-2 +26%); the ledger's midpoints below the model, as today.
4. **The transition share from FY2040:**
   - CLI-2's outlay at 80% of C1;
   - the waterfall's draws for the guarantee and the bill credit;
   - the remainder as general-fund receipts until Espen directs it (R-3).
5. **The builders' capital** as time-limited capital with rate repayments, net cost only expected forgiveness; no double count with the second tranche; the extra credited generation under CLI-1's risk (R-4).
6. **The credits:** the booked CLI-1, with the model's +$0.27-0.43 trillion as the disclosed risk (R-6).
7. **The household model's D3 test** on the model's carbon-channel distribution (R-8), adding the standard's payments to electricity once the model passes them through (R-2).

## For Espen

**One question: where the transition share's remainder goes after FY2039.**

From 2040 the 20% transition share of the carbon price raises about $33 billion a year. As decided, it pays the worker guarantee and the energy bill credit first, about $11 billion. Nothing says where the other $23 billion or so goes. We recommend keeping it in the general budget, which lowers clean power's yearly cost from about $146 billion to about $113 billion. The alternatives are to add it to the Climate Dividend, about $80 more a year per adult in 2040, or to put it in a standing fund for transition and disaster preparation.
