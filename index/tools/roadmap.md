# Tools roadmap

What the modeling tools do now, and what is planned next, in order. Each item names what it answers for Espen. Update this file when an item lands; the tools readme says how to run what exists.

## In place

| Tool | What it answers |
| --- | --- |
| `run-all.sh` | Rebuilds every generated file from `index/data/inputs/` and shows what changed |
| Transportation model (`transportation/`) | Moving America's program, receipts, general-fund draw and act scores; tested against Draft 2 on every run |
| Ledger (`ledger-build.py`, `ledger-make-md.py`) | General-fund claims against the base, the gap after accepted options, vehicles, channels at gross |
| Floor paths (`ledger-paths.py`) | Senate floor days under each D2 path against the 163-day budget |
| Incidence model (`incidence-*.py`) | D3: who comes out ahead, by quintile, on the decided package and its variants, by year |
| Long-term fiscal model (`fiscal-*.py`) | D4-B: run rate from 2040, the investment envelope, debt and interest against CBO's baseline to 2056 |
| Consistency check (`check-project.py`) | Stale figures and phrases in documents, unknown IDs, ledger rows against their domain files, scaled figures re-run |
| Window rescaler (`window.py`) | A figure from another budget window in 2030-39 terms |
| Dashboard data (`dashboard-data.py`) | The live ledger dashboard's data files, regenerated on each run |

## Next, in order

1. **Vote simulator.** Port the war-game simulator (`archive/wargame-trifecta-2029-simulator.jsx`) to Python on the ledger's rows: the odds each bill passes under paths F, C and G, the R1-R3 packages' fragility (a package fails on the union of its members' objections), and a Senate roster the Nov 3 re-baseline can change in one place.
2. **Dedicated-fund engine.** Year-by-year balances for the funds the general-fund ledger leaves out: the paid-leave fund and its step-up toward 0.85%; Social Security and Medicare HI over 75 years (the module D8 and SS-5 need); the Highway Trust Fund's three accounts; the carbon fee's dividend and transition channel; the held education fund (EDU-9B) if it is taken up.
3. **Uncertainty and shared packages.** One packages file that the ledger, incidence and fiscal models all read (today each keeps its own scenario list). Then a simulation of the gap and the D3 and D4 tests with correlated draws (the Medicare Advantage savings split between the general fund and HI, revenue overlap, take-up) and discrete risks (G8 failing to score, leave take-up), reporting the chance each test passes rather than one midpoint.
4. **Model upgrades.**
   - *Incidence v2:* D3's pass/fail at years five and ten; the top 10%, 1% and 0.1%; leave at the 0.85% cap; EXE-14B's tariff repeal; typical households inside the fourth quintile; published TPC and CBO distribution tables in place of pattern keys.
   - *Reconciliation vehicle checker:* each bill's Byrd out-year test (permanent spending against revenue on the same bill), PAYGO, the pairing rule, and a Byrd register of provisions at risk. It will use the R2 revenue placement (Oct 20).
   - *Fiscal fixes:* health provisions' start years, demographic growth for the benefit rows, interest-rate feedback, an AI payroll stress case, the debt-limit date, a fiscal-impulse view, contingent liabilities (Judgment Fund, reinsurance), and NSC-1's alternative bases.

## Retired

The two code-handoff notes from Oct 19 set up a chat-to-Code workflow through the claude.ai Project; the repo replaced it on Oct 20. Their jobs are done or carried above: Job 0 (reproduce) is `run-all.sh`; Job 1 (linter) and Job 2 (reconcile) are `check-project.py`; Job 3 (one-command rebuild, incidence reading the ledger) is `run-all.sh` with `incidence-rows.csv`; Job 4 (incidence v2) is item 4 above. The notes are in git history.
