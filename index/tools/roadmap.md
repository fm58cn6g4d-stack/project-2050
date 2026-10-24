# Tools roadmap

What the modeling tools do now, and candidate upgrades. Project-wide priorities are in [the shared queue](../../sources/project-work-queue.md); this roadmap does not set their order. Each item names what it answers for Espen. Update this file when an item lands; the tools readme says how to run what exists.

## In place

| Tool | What it answers |
| --- | --- |
| `run-all.sh` | Rebuilds the common suite from `index/data/inputs/` and shows what changed |
| Transportation model (`transportation/`) | Moving America's program, receipts, general-fund draw and act scores; tested against Draft 2 on every run |
| Ledger (`ledger-build.py`, `ledger-make-md.py`) | General-fund claims against the base, the gap after accepted options, vehicles, channels at gross |
| Floor paths (`ledger-paths.py`) | Legacy fixed-day crosswalk under each D2 path; current scheduling uses calendar scenarios |
| Incidence model (`incidence-*.py`) | D3: who comes out ahead, by quintile, on the decided package and its variants, by year |
| Long-term fiscal model (`fiscal-*.py`) | D4-B: run rate from 2040, the investment envelope, debt and interest against CBO's baseline to 2056 |
| Consistency check (`check-project.py`) | Stale figures and phrases in documents, unknown IDs, ledger rows against their domain files, scaled figures re-run |
| Window rescaler (`window.py`) | A figure from another budget window in 2030-39 terms |
| Vote simulator (`votes-model.py`) | The odds each package and bill passes under each D2 path, by seat count and holdouts; what the packages lose in the trim |
| Dedicated-fund engine (`funds-model.py`) | Social Security and HI over 75 years (D8, SS-5), the paid-leave fund's step-up and loan, the Highway Trust Fund's accounts, the carbon dividend by year, the rate EDU-9B would need |
| Carbon model (`carbon-model.py`, `carbon/`) | Emissions by sector to 2050 under D7 and the companion measures, REV-C1's receipts and the dividend by year, the size of REV-C2 and a methane fee, what the road-fuel exemption gives up, with uncertainty bands |
| Dashboard data (`dashboard-data.py`) | The live ledger dashboard's data files, regenerated on each run |
| Surge funding (`capacity-funding.py`) | Immediate legal availability, unpriced FY2029 cash and overlap/eligibility limits; not an acceleration score |
| Scenario calendar (`calendar/`) | Conditional preparation/floor/bicameral/delivery comparisons; uncalibrated ranges |
| Child poverty (`child-poverty/`) | Verified CPS measurement and bounded conditional agenda experiments; independent runner, no future forecast |

## Candidate upgrades, subject to a concrete claim or decision

1. **Uncertainty and shared packages.** One packages file that the ledger, incidence and fiscal models all read (today each keeps its own scenario list). Then a simulation of the gap and the D3 and D4 tests with correlated draws (the Medicare Advantage savings split between the general fund and HI, revenue overlap, take-up) and discrete risks (G8 failing to score, leave take-up), reporting the chance each test passes rather than one midpoint.
2. **Model upgrades.**
   - *Incidence v2:* D3's pass/fail at years five and ten; the top 10%, 1% and 0.1%; leave at the 0.85% cap; EXE-14B's tariff repeal; typical households inside the fourth quintile; published TPC and CBO distribution tables in place of pattern keys.
   - *Reconciliation vehicle checker:* each bill's Byrd out-year test (permanent spending against revenue on the same bill), PAYGO, the pairing rule, and a Byrd register of provisions at risk. It will use the R2 revenue placement (Oct 20).
   - *Dedicated funds:* a year-by-year Trustees HI table in place of the summary rates; an SSA score of the D8 package as a whole (interactions) and of SS-10.
   - *Fiscal fixes:* health provisions' start years, demographic growth for the benefit rows, interest-rate feedback, an AI payroll stress case, the debt-limit date, a fiscal-impulse view, contingent liabilities (Judgment Fund, reinsurance), and NSC-1's alternative bases.

## Retired

The two code-handoff notes from Oct 19 set up a chat-to-Code workflow through the claude.ai Project; the repo replaced it on Oct 20. Their jobs are done or carried above: Job 0 (reproduce) is `run-all.sh`; Job 1 (linter) and Job 2 (reconcile) are `check-project.py`; Job 3 (one-command rebuild, incidence reading the ledger) is `run-all.sh` with `incidence-rows.csv`; Job 4 (incidence v2) is item 2 above. The notes are in git history.

## Scenario calendar integration

`index/calendar-scenarios.md` and `index/calendar-scenario-explorer.html` are the current scenario presentation; `index/calendar-delivery-opportunities.md` keeps possible felt effects separate. Inputs: `index/data/inputs/calendar-scenarios.json` and the live bill inventory; milestone evidence: `sources/calendar-delivery-milestones.csv`; runner/tests: `index/tools/calendar/`. `run-all.sh` regenerates them and dashboard/calendar.json. The 172/163 display is legacy provenance. New numeric ranges are illustrative; vote parameters and fiscal/benefit profiles are unchanged. See `sources/calendar-model-review-and-integration.md` for review findings and limits.

## Child-poverty research tool: October 24 conditional agenda analysis

index/tools/child-poverty now includes the verified CPS baseline, tax/claimant audit, official parameter extracts, 102-test suite and completed conditional agenda analysis. agenda_analysis.py executes eight joint 2030/2034 phasing cases and 42 sensitivities using all 160 replicates and discrete receipt/household-allocation mixtures. A matched source-year EITC/ACTC removal comparator passes Census public-use/internal tolerances. report_agenda.py generates index/child-poverty-agenda-analysis.html and sources/family-child-poverty-agenda-effects.md from the checked results. It runs independently of run-all.sh and does not change fiscal inputs or replace D3/D4. These are static conditional effects, not future current-law poverty forecasts; observed source resources/credits are preserved, and legal coverage/delivery/proxy inputs remain assumptions. Espen explicitly directed against overbuilding a speculative forecast. More precise legal, delivery, administrative-alignment, employment and whole-package estimates are refinements rather than prerequisites for using this bounded analysis.
