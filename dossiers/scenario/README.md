# Political scenario

Role: the project's political planning scenario: what the 2026 elections produced, what the published analysis says about why, and a framework of questions for 2027-28 and for the 2029 plan. Status: draft (stage B, step 1), as of November 8, 2026. Results are still being counted; every figure carries its date and source, and `1-results.md` lists what to recheck.

This is not a flagship dossier, so it does not follow the nine-section template. It sits under `dossiers/` because "Where things live" (`charter/STANDARDS.md`) has no folder for scenario work and a new top-level folder would be a charter change (tier 3). Whether it should get its own row there is a question for Espen (`3-framework-2027-28.md`, question 10).

| File | What |
| --- | --- |
| `1-results.md` | The results record, kept apart by certainty: called races, uncalled races with a clear projection, genuinely open races; then margins, shifts from 2024, turnout and state changes |
| `2-analysis.md` | The exit polls and AP VoteCast (data), and the analysts' competing readings of why (analysis) |
| `3-framework-2027-28.md` | Who holds which levers in 2027-28, the vehicles, what counts as success, how the two years feed the 2029 plan, what could change the picture, and the open questions for Espen. Questions and options, not decisions. Includes a check of the two input docs |
| `4-2029-plan.md` | What the results mean for the legacy decisions D1, D2, D3, D4, D8 and D9 and for the stage order in `charter/PLAN.md`: flagged changes, none made |
| `5-senate-2028.md` | The 2028 Senate map and history; its first-iteration estimate is superseded by `senate-model-2028.md` |
| `senate-model-2028.md` | The seat-by-seat 2028 Senate model: inputs, scenarios, tipping points, Espen's priors tested, the Murkowski branches, and what each Senate size means for the 2029 plan (options and questions) |
| `senate-model-outputs.md` | The tables `tools/senate_model.py --write` generates (do not edit by hand); `senate-model-fec-cash.csv` holds the FEC cash-on-hand extract |
| `2030-2034-control.md` | Senate control through the 2033-34 Congress: the 2030 and 2032 classes, chained from the 2028 model |
| `house-model-2028.md` | The 2028 House on the current maps and the 2029 trifecta, chained to the Senate model's runs (`tools/house_model.py`; tables in `house-model-outputs.md`) |
| `house-stress-test-2029.md` | D1 stress test: a Democratic president and Senate with a Republican House; what passes, what the reconciliation slot becomes, which flagships move (analysis) |
| `redistricting-2030-model.md` | Who holds the 2031 redistricting pens in twelve states, on the shared national swing, and DEM-2 Titles I-II's value in 2032 House seats (`tools/redistricting_2030.py`; tables in `redistricting-2030-outputs.md`) |
| `model-credibility.md` | Credibility check of the scenario models: a 2018-2024 back-test, the environment prior stress-tested, the five assumptions that matter most with leading indicators (`tools/backtest.py`; tables in `model-credibility-outputs.md`; data in `model-credibility-data.json`) |
| `2027-races.md` | The 2027 off-cycle races (governors, legislatures, state supreme courts, the Minnesota Senate special, mayors, ballot measures) and the 2027 decisions that move the 2028 House map |
| `2027-scorecard.md` | The pre-registered 2027 scorecard: the on-track result for D+3.0 in each November 2027 contest, a fixed rule for moving the 2028 prior, the effect on P(trifecta), P(55+) and P(D House 2033), and the signals that should change the plan (`tools/scorecard_2027.py`; tables in `2027-scorecard-outputs.md`; the 2017-2026 special-election series in `specials-2017-2026.csv`, built by `tools/specials_extract.py`) |
| `2027-28-playbook.md` | The 2027-28 governing playbook as options: federal levers, governors and trifectas, courts and executive-defiance risks; each with odds (analysis) and its effect on 2028 conditions |
| `2028-outlook.md` | 2028 as scenarios with drivers: the presidential fields, the House map, governor races, what moves the national environment |
| `compounding-2029-2050.md` | How the 2026 result and 2027-28 paths change the 2029 plan and the long run (pre-built bills, the 2029 starting point, stage order, courts, the census, redistricting, durable majorities); questions for Espen |
| `2027-28-stress-tests.md` | Three rounds of hard questions on the files above, the research and revisions, and the combined next questions |
| `2028-republican-branch.md` | If a Republican wins in 2028 and Democrats keep the Senate: what survives of the 2029 plan and what the project could do |
| `compounding-prebuild.md` | The pre-build pipeline: for each flagship, what a 2027-28 House bill would contain, its vehicle and its lock-in risk |
| `compounding-redistricting.md` | Redistricting through 2032: the 2028 redraws, what DEM-2 is worth in seats, who draws in 2031, the states ranked |
| `compounding-defense.md` | The defense lock-in: three FY2028 paths and their effect on NSC-1A's 2030-39 base (script in `tools/`) |
| `memo-defense-baseline-and-dem2.md` | Decision memo for Espen: what defense is counted against in the fiscal tests; whether DEM-2 is written severable, and in what order |

**Time frame.** Under `DEC-2026-10-29-01` the plan is a governing program from January 2029. 2027-28 is one of its two labeled exceptions, and the work here on 2027-28 is that exception: it serves the 2029 plan and does not replace it.

**Nothing here is decided.** No housing memo is decided and no 2029 design choice is final (`dossiers/home/3-design.md`). Changes this folder flags for `charter/` or `legacy/governing/` are tier 3 and wait for Espen.

**Sources.** News, wire and analyst pages are licensed, so they enter the library only as citation rows (`library/catalog.csv`, `SRC-` IDs), with short quotations at most. Each figure names its source and the date it was read. Where outlets disagree, both are given.
