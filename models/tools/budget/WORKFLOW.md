# Federal budget model: workflow

Role: how Project 2050 builds the federal budget model of `charter/PLAN.md` 3.4. It names the pieces, how they fit together, the order and owners, and how each piece is checked. Status: proposed November 8, 2026 by the strategy session, for Espen's approval. Nothing here changes the adopted inputs (`models/data/inputs/`), the selected baseline or any published figure. Those changes come later as tier-3 PRs, one decision at a time.

## What Espen asked for

- **One model of the whole federal budget.** It covers spending, revenue, deficits and debt year by year: regular, supplemental and advance appropriations; mandatory spending; reconciliation; trust funds; and interest. Every figure can be read in nominal dollars, in real (inflation-adjusted) dollars and as a share of GDP.
- **Visible assumptions.** Each one is written down where it can be read, not buried in code.
- **A quick view** of how a proposed policy change moves the fiscal trajectory.
- **Grounds for trust:** consistent, prudent handling that can be checked.

## Where things stand

The project already has a working long-term fiscal model (`models/tools/fiscal-model.py`, built on `fiscal-data.py`, `fiscal-profiles.py`, the ledger and the dedicated-funds engine). Codex built most of it and leads it today (`charter/PLAN.md`, roles); see "Ownership" below for the proposed change. It answers the D4 questions well. Five gaps stand between it and what Espen asked for:

1. **No budget-concept layer.** A program is a ten-year midpoint from the ledger, spread over years by a phase-in profile. The model doesn't record:
   - whether the money is budget authority or outlays, or how fast it spends out;
   - whether a program is discretionary or mandatory;
   - which vehicle carries it: regular, supplemental (emergency) or advance appropriations, or reconciliation;
   - whether it expires.

   Spending can't yet be shown the way Congress enacts it.
2. **Assumptions live in code.** The baseline adjustments (ADJ-T1, ADJ-T2 and the FY2026 actuals in `fiscal-data.py`), the rounded CPI path and interest rates (`fiscal-model.py`), the phase-in profiles and the counting conventions are all scattered. The defense memo (`dossiers/scenario/memo-defense-baseline-and-dem2.md`) shows the cost: NSC-1A reads $0 because defense is measured against CBO's baseline, and nothing on the page says so.
3. **Real versus nominal isn't consistent.** Amounts are nominal, CPI is one rounded rate, and no deflator series is kept for real-dollar views.
4. **Scenarios are kept separately in each model** (ledger, incidence and fiscal), as `models/tools/roadmap.md` item 1 notes.
5. **Trust rests on accounting tests.** The tests prove the arithmetic adds up. They don't show the model reproduces CBO's own numbers or known CBO and JCT scores.

Espen's old CBO scorer (SRC-0203, `library/intake/2026-10-28/old-sessions/Claude built CBO scorer tool/cbo-scorer.jsx`) is worth two ideas:
- a library of typed provisions, each with its own scoring method (discretionary spend-out tables, per-enrollee costs, rate changes);
- CBO's rules of thumb for how deficits respond to interest rates, productivity and labor force.

Its approach of having a language model read bill text and produce a score should not be carried over: the result can't be checked.

## The pieces

| # | Piece | What it produces | Depends on | Owner | Tier |
| --- | --- | --- | --- | --- | --- |
| **B1** | **Conventions and assumptions register** | `models/tools/budget/CONVENTIONS.md`: how the project counts, in plain language (baseline rules, budget authority and outlays, the categories, real and nominal, the scoring window, dynamic effects, how a policy is measured against the baseline). `models/data/budget/assumptions.csv`: every assumption now in the model, with an `ASM-` ID, its value, where it lives in code, its source, who decided it and how much it matters. A generated plain-language page lists them. The registry checker resolves `ASM-` IDs. | Nothing | Claude worker, Most capable; Codex reviews | 1 for the register; conventions that change a commitment go to Espen as memos |
| **B2** | **Budget data layer and baseline reproduction** | `models/data/budget/`: CBO's February 2026 baseline by category, with budget authority and outlays where CBO or OMB publishes them; OMB historical tables for spend-out patterns; deflators (CPI-U, GDP price index) as series. A loader and a test that **reproduces the adopted baseline** (`models/data/fiscal-baseline.csv`) to the dollar, so no second baseline exists. | Nothing (B1 in parallel) | Claude worker, Most capable; Codex reviews | 1 |
| **B3** | **Provision scoring library** | `models/tools/budget/`: a typed provision format that records category, budget authority, spend-out, phase-in, indexation, vehicle and expiry, with a scoring method per type (from the CBO scorer's ideas and the existing profiles). A crosswalk gives every current ledger row a provision spec. Calibrated so each row's 2030-39 total still equals its ledger midpoint: no headline figure moves. | B1, B2 | Claude worker, Most capable; Codex reviews | 1; changing any ledger figure is tier 3 |
| **B4** | **Benchmarks and model card** | Tests that the model reproduces CBO's baseline; reproduces two or three published CBO or JCT scores (for example, Public Law 119-21 and one appropriations act) within stated tolerances; keeps the accounting identities (deficit equals outlays minus revenue; debt grows by the deficit plus other means of financing); and responds to interest and growth shocks as CBO's rules of thumb say. Plus a model card: purpose, limits, known errors. | B2, B3 | Claude worker, Most capable; **independent milestone review by Codex** | 1 |
| **B5** | **Fiscal viewer** | A page Espen can open: deficits, debt, interest and spending by category to 2056, in nominal, real and %GDP terms. Scenarios side by side. Each assumption links to its `ASM-` entry. A "what changed since the last run" view. Built from generated files only, so it never holds numbers of its own. | B2 (first version from today's `fiscal-paths.csv`); B3 for the full version | Claude worker, Standard | 2 |
| **B6** | **Integration** | `fiscal-model.py` reads the new layer and library in place of its in-code constants. One shared scenario file for the ledger, incidence and fiscal models. | B1–B4 | The budget model's owner: a Claude worker if PR #106 is approved, otherwise Codex. **Independent milestone review by Codex** either way | 3 |
| **B7** | **Decisions for Espen** | Short memos, one choice each: the defense reference (the existing memo); a possible lame-duck revenue adjustment (`dossiers/scenario/2028-lame-duck.md`, section 4); and any convention in B1 that changes what the plan commits to. | B1 | Lead or strategy session | 3 |

## How the pieces fit

```
B1 conventions + assumptions ─┐
                              ├─> B3 provision library ─> B4 benchmarks ─> B6 integration (Codex)
B2 data layer + baseline ─────┘                                              │
        └──────────────> B5 viewer (first version on today's outputs) <──────┘
B1 ──> B7 decision memos for Espen (any time)
```

**Shared interfaces**, which every piece uses and no piece changes alone:
- **IDs:** `ASM-` for assumptions (B1 defines the format); ledger and agenda IDs as today; provision specs keyed by ledger ID.
- **Units:** billions of nominal dollars by federal fiscal year. Real dollars are always derived from B2's deflator series in one function, never computed ad hoc. %GDP uses B2's GDP series.
- **Categories:** B2 publishes the category list (CBO's, with OMB's budget authority and outlay detail where available). B3, B4 and B5 use it as is.
- **The baseline:** one only, the adopted one. B2 reproduces it; nothing selects another. Changing it is B7 and tier 3.

## Order, sized for the usage limits

The account hit its five-hour usage limit overnight, and at most three Claude sessions work at once. The lead is running stage C and the reviewer wakes every three hours. So at most two budget workers run at a time:

1. **Now:** B1 and B2 in parallel. They write different files.
2. **When B1 and B2 have PRs up:** B3, then B5's first version, which needs only today's outputs.
3. **When B3 is in review:** B4.
4. **When B4 merges:** B6, by the model's owner (see "Ownership"), with Codex's review requested through a PR comment. B7 memos go to Espen whenever B1 surfaces a choice.

Each worker reports to the strategy session (`session_01UQzgBuA3EdnR7Dx4kUq1un`). The strategy session starts the next piece and tells the lead when each one lands.

## How the work is checked

- **Every piece:** `bash .github/scripts/run-checks.sh` passes; the PR carries `Agent-Author`. The reviewer session, or Codex where its review matters most (B2, B3, B4), signs off at the current head.
- **No silent moves, by test:** the merge gate alone doesn't guarantee this. It treats a headline change under 1% as tier 2 and doesn't see per-row ledger totals. So each piece ships its own **exact-equality tests**, run by `run-checks.sh`:
  - B2: the adopted baseline (`models/data/fiscal-baseline.csv`) is reproduced to the cent;
  - B3: every ledger row's FY2030-39 total, and `models/data/fiscal-paths.csv`, are unchanged;
  - B6: the same tests, rerun after integration.

  A figure that has to move is a project decision for Espen: a tier-3 PR with the reason, labeled `needs-espen`, whatever tier the gate assigns.
- **Benchmarks before trust:** nothing new feeds a public or decision figure until B4's benchmarks pass.
- **Assumptions are cited:** after B1, every assumption the model uses has an `ASM-` entry, and the checker fails on an uncited one once B6 lands.

## Ownership

Espen has said the budget model and its shared inputs can come back to Claude from Codex if that's easier.

**Recommendation: move them to Claude**, and keep Codex as the independent reviewer of B4 (benchmarks) and B6 (integration). That change is its own decision, in PR #106 (tier 3), so Espen can take this workflow without it.

- **Why move:** Codex's reviews keep stopping at its usage limits (PRs #75 and #77). Claude sessions are building B1–B5, and integration needs that same context. Handing B6 across vendors through PR notes would be the slowest, most error-prone step in the plan.
- **Why keep Codex involved:** Codex wrote most of the current fiscal model. Its review of the benchmarks and the integration is the check most likely to catch a Claude-side mistake, and the gate already relies on a second vendor for independence.
- **Unchanged either way:** changing adopted inputs in `models/data/inputs/` is Espen's decision, and fair financing stays Codex's.

## Decisions for Espen

1. **Approve this workflow**, which approves this PR. B1 and B2 have started; they change nothing adopted, so they're safe to stop or redirect if the plan changes.
2. **Ownership** (PR #106): move the budget model to Claude, with Codex reviewing (recommended), or keep it with Codex.
3. **Defense reference** (`memo-defense-baseline-and-dem2.md`, choice a): already waiting on the board.
4. Later, as B1 surfaces them: the conventions that change what the plan commits to.
