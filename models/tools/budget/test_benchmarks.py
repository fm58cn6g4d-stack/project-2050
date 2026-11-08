#!/usr/bin/env python3
"""test_benchmarks.py: the benchmarks for the federal budget model (budget workflow piece B4).

Role: the evidence that the budget model can be trusted, and where it can't yet. Each benchmark
compares something the model computes with a published figure or an accounting rule, and states
its source, its tolerance and why that tolerance. Status: current. run-all.sh runs it after the
dedicated-funds engine (step 6e), because it reads that run's build/ledger.json and
build/funds.json. Standard library only.
Run from the repo root, after bash models/tools/run-all.sh:
    python3 models/tools/budget/test_benchmarks.py

What a run does:
  1. Computes every benchmark (BENCHMARKS below) and writes the results page and its data,
     build/budget-benchmarks.md and build/budget-benchmarks.json, and the model card with its
     generated results block, build/budget-model-card.md. run-all.sh compares them with
     models/tools/budget/benchmarks.md, benchmarks.json and MODEL-CARD.md (drift check), so a
     result that changes shows up in the PR.
  2. Runs the unit tests below. They fail if a benchmark is malformed or if any accounting identity
     breaks (run-all's drift check, not this file, catches committed pages that are out of date). They do not fail when a
     published-score, sensitivity or trust-fund benchmark misses its target: a miss is a result,
     reported on the page with its size. Nothing here tunes the model or a tolerance to pass.

Statuses: pass, fail (outside tolerance), pending (the source is not in the library, or the
model can't compute the quantity yet; the page says which), info (reported, no target).
Every tolerance was set in this file before it was committed and is explained beside it.
"""
import csv, importlib.util, io, json, os, sys, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.normpath(os.path.join(HERE, ".."))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
BUILD = os.environ.get("P2050_BUILD", os.path.join(ROOT, "build"))
sys.path.insert(0, HERE)
import data as D          # noqa: E402
import provisions as P    # noqa: E402

LEDGER = os.path.join(BUILD, "ledger.json")
FUNDS = os.path.join(BUILD, "funds.json")
BASELINE = os.path.join(ROOT, "models", "data", "fiscal-baseline.csv")
PAGE, DATA_OUT, CARD = "benchmarks.md", "benchmarks.json", "MODEL-CARD.md"
BUILD_NAMES = {PAGE: "budget-benchmarks.md", DATA_OUT: "budget-benchmarks.json", CARD: "budget-model-card.md"}
CARD_START, CARD_END = "<!-- generated:results:start -->", "<!-- generated:results:end -->"
FLOAT = 1e-6   # $1,000 in billions: the accounting identities hold to floating-point error


def fiscal_model():
    if TOOLS not in sys.path:
        sys.path.insert(0, TOOLS)
    sp = importlib.util.spec_from_file_location("fiscal_model_b4", os.path.join(TOOLS, "fiscal-model.py"))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- published figures used as targets
# Each is copied from the source, which is cited; the code fetches nothing.

# JCT's estimates of making the temporary provisions of Public Law 119-21 permanent, billions by
# fiscal year, against CBO's January 2025 baseline, excluding interest. CBO letter of August 4,
# 2025 (publication 61466, SRC-1093), Table 2, read from the PDF Espen uploaded on November 8
# (library/intake/2026-11-08/cbo/61466-DebtService.pdf, PR #121). The four household deductions are
# sections 70103 (seniors), 70201 (tips), 70202 (overtime) and 70203 (car-loan interest).
JCT_FOUR_DEDUCTIONS = {2029: 33, 2030: 68, 2031: 69, 2032: 70, 2033: 71, 2034: 73}   # sum of the four rows; FY2029-34 384
JCT_ALL_TEN = {2029: 42, 2030: 108, 2031: 151, 2032: 157, 2033: 163, 2034: 166}       # Table 2's total row; FY2029-34 787
# CBO's debt service on P.L. 119-21 over FY2025-34: $789 billion with the ten provisions made
# permanent, $718 billion as enacted (same letter, SRC-1093; 2028-lame-duck.md, "Interest").
CBO_DEBT_SERVICE_WITH, CBO_DEBT_SERVICE_ENACTED = 789, 718

# Trustees' 2026 intermediate figures, as funds-model.py prints them beside its own (lines 306, 335)
TRUSTEES_OASDI = {"depletion": 2034, "payable": 83, "balance": -4.42}
TRUSTEES_HI = {"depletion": 2033, "payable": 89, "balance": -0.56}
# Context only, not a target: CBO's own projection of the HI trust fund (The Long-Term Budget Outlook:
# 2026 to 2056, data file 51119-2026-02-25, sheet "3. HI Trust Fund Inc Exp Bal", note: "exhausted
# during fiscal year 2040"), from Espen's November 8 upload (library/intake/2026-11-08/cbo/, PR #121).
CBO_HI_EXHAUSTION = 2040

# CBO's estimate of the Israel Security Supplemental Appropriations Act, 2024 (November 1, 2023; relative
# to CBO's May 2023 baseline), millions of dollars by fiscal year: one year of new emergency budget
# authority and CBO's outlays from it, year by year. Fetched from
# https://www.cbo.gov/system/files/2023-11/CBO_Estimate_for_the_Israel_Security_Supp_Approp_Act_2024.pdf
# on November 8, 2026 through a search tool, as Espen allowed that day; cited, not saved.
CBO_SUPPLEMENTAL_2024 = {
    "defense": {"title": "Title I, Defense", "ba": 10600,
                "outlays": [5629, 1373, 1659, 1107, 520, 177, 66, 18, 0, 0]},
    "nondefense": {"title": "Title II, State, Foreign Operations", "ba": 3700,
                   "outlays": [3583, 60, 33, 15, 5, 2, 1, 0, 0, 0]},
}

# CBO's rules of thumb for the February 2026 baseline: How Changes in Economic Conditions Might Affect
# the Federal Budget: 2026 to 2036 (publication 62257, April 2026), Tables 2 and 3, billions by fiscal
# year, each for a change of 0.1 percentage point every year. From Espen's November 8 upload
# (library/intake/2026-11-08/cbo/62257-Rules-of-Thumb.pdf, PR #121). CBO rounds each year to $1 billion;
# the ten-year totals are CBO's own.
CBO_ROT_INTEREST = {   # Table 3, interest rates 0.1 point higher: total change in net interest outlays
    2026: 6, 2027: 14, 2028: 20, 2029: 25, 2030: 31, 2031: 36, 2032: 41, 2033: 46, 2034: 51, 2035: 57, 2036: 62}
CBO_ROT_INTEREST_10YR = 383            # FY2027-36, Table 3
CBO_ROT_PRODUCTIVITY_10YR = 317        # FY2027-36 added deficit, productivity growth 0.1 point slower (Table 2)
CBO_ROT_LABOR_10YR = 166               # FY2027-36 added deficit, labor force growth 0.1 point slower (Table 2)
# Cross-check only: the 2025 workbook (61183, January 2025 baseline) gives net interest +13.34 in FY2026
# for the same 0.1-point scenario. Those are the numbers in Espen's old CBO scorer (SRC-0203, the ROT
# table), which confirms where that table came from.
ROT_2025_INTEREST_FY2026 = 13.34

UPLOADS = [
]


# ---------------------------------------------------------------- the benchmarks

def _bm(id, group, name, status, value, target, tolerance, source, why, unit="", miss=None, detail=None):
    return dict(id=id, group=group, name=name, status=status, value=value, target=target,
                tolerance=tolerance, unit=unit, miss=miss, source=source, why=why, detail=detail or [])


def bm_baseline():
    """BL-1: cite B2's reproduction test by running it, not by repeating it."""
    import test_data
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_data.Reproduction)
    res = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
    bad = len(res.failures) + len(res.errors)
    return _bm("BL-1", "Baseline", "The baseline equals CBO's February 2026 projections plus the documented adjustments",
               "pass" if bad == 0 and res.testsRun > 0 else "fail",
               "B2's %d reproduction tests: %d pass" % (res.testsRun, res.testsRun - bad),
               "every cell of models/data/fiscal-baseline.csv, FY1962-2056", "exact (the file's three decimals; the unrounded values are the same floating-point numbers)",
               "CBO, *The Budget and Economic Outlook: 2026 to 2036* and *The Long-Term Budget Outlook: 2026 to 2056* (February 2026), "
               "from CBO's data files; the FY2026 actuals and the ADJ-T1 and ADJ-T2 tariff adjustments in models/data/budget/post-february.csv",
               "B2's test (models/tools/budget/test_data.py, class Reproduction, run-all step 5b) rebuilds the adopted baseline from the data "
               "layer alone. This benchmark runs that test and reports it; it does not repeat it. One baseline, reproduced exactly, is "
               "the foundation every other figure stands on.",
               miss=None if bad == 0 else "%d tests fail" % bad)


def bm_identities(M):
    R, B = M["results"], M["B"]
    out = []
    # ID-1: deficit = outlays - revenue
    worst = max(abs(Y["deficit"] - (Y["out"] - Y["rev"])) for r in R.values() for Y in r["years"].values())
    out.append(_bm("ID-1", "Accounting identities", "Deficit equals outlays minus revenue, every year and scenario",
                   "pass" if worst <= FLOAT else "fail", worst, 0.0, "$1,000 (1e-6 billion): floating-point error only",
                   "Accounting definition (CBO's deficit is total outlays less total revenues)",
                   "The fiscal model builds the deficit from its parts in two places; they must agree to rounding error. "
                   "Checked for all %d scenarios, FY2026-2056." % len(R), unit="$B, largest gap"))
    # ID-2: the program's own debt grows by its deficit and interest, nothing else
    worst = 0.0
    for r in R.values():
        Y = r["years"]
        for y in range(2027, 2057):
            worst = max(worst, abs(Y[y]["prog_debt"] - Y[y - 1]["prog_debt"] - Y[y]["prog_primary"] - Y[y]["prog_interest"]),
                        abs(Y[y]["gf_debt"] - Y[y - 1]["gf_debt"] - Y[y]["gf_primary"] - Y[y]["gf_interest"]))
    out.append(_bm("ID-2", "Accounting identities", "The program's added debt grows by exactly its added deficit (spending, revenue and interest)",
                   "pass" if worst <= FLOAT else "fail", worst, 0.0, "$1,000 (1e-6 billion)",
                   "Accounting definition: debt(t) = debt(t-1) + deficit(t) + other means of financing; the program has no other means of financing",
                   "Checked on both bases (unified and general fund) for every scenario. The program's debt is what decides the D4 guardrails, "
                   "so it must not leak or gain anything outside its own deficits.", unit="$B, largest gap"))
    # ID-3: total debt; the residual is CBO's other means of financing, the same in every scenario
    # CBO's residual from the adopted baseline as the model reads it (fiscal-baseline.csv, to $1 million)
    cbo_def = {y: B[y]["out_primary"] + B[y]["out_net_interest"] - B[y]["rev_total"] for y in B}
    cbo_debt = {y: B[y]["debt_public"] for y in B}
    cbo_debt[2026] = D.by_year("cbo-ten-year")[2026]["proj_debt_held_by_public"]   # CBO's projection, not the FY2026 actual
    cbo_resid = {y: cbo_debt[y] - cbo_debt[y - 1] - cbo_def[y] for y in range(2027, 2057)}
    worst, base_resid = 0.0, None
    for sid, r in R.items():
        Y = r["years"]
        resid = {y: Y[y]["debt"] - Y[y - 1]["debt"] - Y[y]["deficit"] for y in range(2027, 2057)}
        if sid == "BASE":
            base_resid = resid
        worst = max([worst] + [abs(resid[y] - cbo_resid[y]) for y in resid])
    ten = sum(base_resid[y] for y in range(2027, 2037))
    big = max(range(2027, 2057), key=lambda y: abs(base_resid[y]))
    out.append(_bm("ID-3", "Accounting identities", "Debt held by the public: the residual after deficits is CBO's own other means of financing, in every scenario",
                   "pass" if worst <= FLOAT else "fail", worst, 0.0, "$1,000 (1e-6 billion)",
                   "CBO February 2026 ten-year and long-term projections of debt and deficits, as stored in the adopted baseline (models/data/fiscal-baseline.csv, to $1 million)",
                   "CBO's debt grows by more or less than its deficits because of other means of financing (mainly the cash flows of federal "
                   "credit programs such as student loans). The model takes CBO's debt path, so it carries that residual. The test is that the "
                   "residual is exactly CBO's, FY2027-2056, in every scenario: the tariff adjustments, the program and the interest-rate cases add none.",
                   unit="$B, largest gap from CBO's residual",
                   detail=["The residual itself (reported, not tested): %+.0f billion in total over FY2027-36; largest single year %d, %+.1f billion. "
                           "FY2026 is left out because its debt is the preliminary actual (models/data/budget/post-february.csv). The model carries the "
                           "gap between that actual and CBO's projection for FY2026 (%+.0f billion) into every later year, with interest, as a deficit, not as "
                           "other financing; so CBO's FY2027 residual is measured from CBO's own FY2026 projection." % (ten, big, base_resid[big], B[2026]["debt_public"] - cbo_debt[2026])]))
    # ID-4a: program interest recomputed from the stated rates
    FM = M["_FM"]
    worst = 0.0
    for sid, label, opts, cfg in FM.SCENARIOS:
        if opts is None:
            continue
        shift = cfg.get("rate_shift", 0.0)
        Y, prev = R[sid]["years"], 0.0
        for y in range(2026, 2057):
            b = B[y]
            if y <= 2036:
                rate = max(b["cbo_avg_rate"], 0.4 * b["bill3m"] + 0.6 * b["note10"])
            else:
                rate = b["implied_rate"]
            rate = (rate + (shift if y >= 2030 else 0.0)) / 100
            want = rate * prev + rate * Y[y]["prog_primary"] / 2
            worst = max(worst, abs(want - Y[y]["prog_interest"]))
            prev = prev + Y[y]["prog_primary"] + want
    out.append(_bm("ID-4a", "Accounting identities", "Interest on the program's borrowing follows from its debt and the stated rates",
                   "pass" if worst <= FLOAT else "fail", worst, 0.0, "$1,000 (1e-6 billion)",
                   "The model's stated rate rules, CONVENTIONS.md section 10: ASM-RATE-MARGINAL, ASM-RATE-LT, ASM-RATE-HALFYEAR, ASM-RATE-SHIFT; "
                   "CBO's February 2026 rates (3-month bill, 10-year note, average rate on debt)",
                   "Recomputed here from the written rules, independently of fiscal-model.py's code: interest = rate x last year's added debt "
                   "+ rate x half of this year's added deficit, at the higher of CBO's average rate and a 40/60 bill-note blend through 2036 "
                   "and the baseline's implied rate after, plus one point from 2030 in the R1 cases.", unit="$B, largest gap"))
    # ID-4b: the baseline's own interest against CBO's average rate
    gaps = {y: B[y]["implied_rate"] - B[y]["cbo_avg_rate"] for y in range(2027, 2037)}
    wy = max(gaps, key=lambda y: abs(gaps[y]))
    out.append(_bm("ID-4b", "Accounting identities", "The baseline's net interest is consistent with its debt and CBO's average interest rate",
                   "pass" if abs(gaps[wy]) <= 0.25 else "fail", round(gaps[wy], 3), 0.0,
                   "0.25 percentage point in every year FY2027-36", "CBO February 2026 ten-year file: net interest, debt held by the public, average interest rate on debt",
                   "Net interest divided by last year's debt (the implied rate) should sit close to CBO's own average rate. They differ by definition: "
                   "CBO's rate is on debt held by the public averaged over the year, while net interest also nets other interest paid and received, "
                   "and last year's debt is lower than the year's average. A quarter point allows for that and would still catch a units or year-alignment error.",
                   unit="points, largest gap (implied minus CBO)", miss=None if abs(gaps[wy]) <= 0.25 else round(abs(gaps[wy]) - 0.25, 3),
                   detail=["Largest gap in FY%d: implied %.2f%%, CBO %.3f%%." % (wy, B[wy]["implied_rate"], B[wy]["cbo_avg_rate"])]))
    # ID-5: nominal = real x deflator; nominal = share of GDP x GDP
    base = D.adopted_baseline()
    nominal = {y: r["out_total"] for y, r in base.items()}
    worst = 0.0
    for idx in ("gdp_price_index", "cpiu"):
        d = D.deflator(idx)
        for by in (D.DEFAULT_BASE_YEAR, 2030):
            real = D.to_real(nominal, by, idx)
            worst = max([worst, abs(real[by] - nominal[by]) / nominal[by]] +
                        [abs(real[y] * d[y] / d[by] - v) / v for y, v in nominal.items()])
    pct, g = D.to_pct_gdp(nominal), D.gdp()
    worst = max([worst] + [abs(pct[y] * g[y] / 100 - v) / v for y, v in nominal.items()])
    out.append(_bm("ID-5", "Accounting identities", "Nominal equals real times the deflator, and share of GDP times GDP (B2's two conversions)",
                   "pass" if worst <= 1e-12 else "fail", worst, 0.0, "relative error 1e-12",
                   "models/data/budget/deflators.csv (CBO's CPI-U and GDP price index) and the baseline's GDP; data.to_real and data.to_pct_gdp",
                   "Every real-dollar and share-of-GDP figure must come back to the same nominal dollars. Checked on total outlays, FY1962-2056, "
                   "for both price indexes and two base years.", unit="largest relative error"))
    return out


def bm_published(M):
    FM, B = M["_FM"], M["B"]
    out = []
    # PS-1: timing of a permanent tax provision, by the library's own method
    PB = P.baseline()
    prof = {"start": 2030, "ramp": 1, "grow": "rev_individual"}   # ASM-PROF-REVENUE: the project's default for a revenue row
    path = P.profile_path(PB, 1.0, prof)
    window = range(2030, 2035)
    tot = sum(JCT_FOUR_DEDUCTIONS[y] for y in window)          # FY2030-34
    scale = tot / sum(path[y] for y in window)
    got = {y: path[y] * scale for y in window}
    gaps = {y: got[y] / JCT_FOUR_DEDUCTIONS[y] - 1 for y in window}
    wy = max(gaps, key=lambda y: abs(gaps[y]))
    worst = abs(gaps[wy])
    cpi = P.profile_path(PB, 1.0, dict(prof, grow="cpi"))
    cs = tot / sum(cpi[y] for y in window)
    out.append(_bm("PS-1", "Published scores", "JCT: extending P.L. 119-21's four household deductions; the library's timing of a permanent revenue provision",
                   "pass" if worst <= 0.05 else "fail", ", ".join("FY%d %.1f" % (y, got[y]) for y in window),
                   ", ".join("FY%d %d" % (y, JCT_FOUR_DEDUCTIONS[y]) for y in window),
                   "5% in each year", "JCT estimates in CBO's letter of August 4, 2025 (publication 61466, SRC-1093), Table 2, from the PDF in Espen's November 8 upload (PR #121)",
                   "The library doesn't estimate how much a provision costs: it takes a total and spreads it over the years. So the test "
                   "of the library is the spreading. The FY2030-34 total JCT gives ($%d billion) goes in; the library's method (provisions.profile_path) "
                   "with the project's default spec for a revenue row (full from the start, growing with individual income tax receipts, "
                   "permanent: ASM-PROF-REVENUE) puts out the yearly amounts, compared with JCT's in every year. Five percent allows for JCT's "
                   "rounding to the billion and the different baseline (January 2025). Over a five-year window it can't tell growth rates apart "
                   "by less than about two points a year, so the growth gap below is reported as a finding, not tested." % tot,
                   unit="$B", miss="%+.1f%% in FY%d" % (100 * gaps[wy], wy) if worst > 0.05 else None,
                   detail=["Largest yearly gap: FY%d, %+.1f%%." % (wy, 100 * gaps[wy]),
                           "JCT's amounts grow about %.1f%% a year, FY2030-34; the default spec grows %.1f%% a year, the speed of individual income tax receipts. "
                           "A likely reason: the deductions are fixed dollar amounts ($25,000 of tips, $12,500 of overtime, $10,000 of car-loan "
                           "interest, $6,000 for each senior), so their cost would grow more slowly than the tax base; whether the statute indexes "
                           "them was not checked here. For a provision like this the default spec front-loads too little and back-loads too much." % (
                               100 * ((JCT_FOUR_DEDUCTIONS[2034] / JCT_FOUR_DEDUCTIONS[2030]) ** 0.25 - 1),
                               100 * ((path[2034] / path[2030]) ** 0.25 - 1)),
                           "For comparison only (not the test): the same spec growing with CPI-U gives FY2030 %.1f and FY2034 %.1f." % (cpi[2030] * cs, cpi[2034] * cs)]))
    # PS-2: debt service on the ten-provision extension
    prim = dict(JCT_ALL_TEN)
    I, _ = FM.debt_roll(B, prim, 0.0)
    got = sum(I[y] for y in range(2025, 2035) if y in I)
    want = CBO_DEBT_SERVICE_WITH - CBO_DEBT_SERVICE_ENACTED
    miss = got / want - 1
    out.append(_bm("PS-2", "Published scores", "CBO: interest cost of extending P.L. 119-21's ten temporary provisions, FY2025-34",
                   "pass" if abs(miss) <= 0.15 else "fail", round(got, 1), want, "15%",
                   "CBO's letter of August 4, 2025 (publication 61466, SRC-1093): debt service $789 billion with the extension, $718 billion without; "
                   "Table 2 for the deficits, every year FY2029-34; from the PDF in Espen's November 8 upload (PR #121)",
                   "Tests the model's interest method (fiscal-model.py, debt_roll: market rates on new borrowing, half a year of interest on "
                   "each year's new deficit) against CBO's own debt-service estimate for the same deficits. JCT's deficits go in, year by year; "
                   "the model's interest comes out. Fifteen percent allows for one known difference: CBO used its January 2025 interest rates "
                   "and the model uses February 2026's. (Until the PDF arrived, FY2031-33 were set equal; Table 2's own years now go in.)",
                   unit="$B", miss="%+.0f%%" % (100 * miss) if abs(miss) > 0.15 else None,
                   detail=["Model interest by year: " + ", ".join("FY%d %.1f" % (y, I[y]) for y in range(2029, 2035)) + ".",
                           "The model is %+.0f%% from CBO. A higher figure is the cautious direction: the model's rate on new borrowing is at least the market blend." % (100 * miss),
                           "Table 2 gives the debt service only for the act and the extension together (by year: FY2026 14 rising to FY2034 155), "
                           "so the extension's own $%d billion is CBO's two totals differenced, not a yearly series." % want]))
    # PS-3: discretionary spend-out against CBO's projected outlays, read the way the library reads
    # discretionary money (provisions.cbo_discretionary_outlays: CBO's account-level budget authority
    # spent out at B2's CBO-calibrated shares, plus, for nondefense, outlays with no discretionary BA)
    for grp in ("defense", "nondefense"):
        pairs = P.cbo_discretionary_outlays(grp)
        yrs = sorted(pairs)
        gaps = {y: pairs[y][0] / pairs[y][1] - 1 for y in yrs}
        wy = max(gaps, key=lambda y: abs(gaps[y]))
        tot_gap = sum(pairs[y][0] for y in yrs) / sum(pairs[y][1] for y in yrs) - 1
        scale = next(float(r["scale"]) for r in D.table("spendout-discretionary-cbo") if r["group"] == grp)
        why = ("Tests B3's spend-out method (provisions.cbo_discretionary_outlays, on B2's CBO-calibrated shares, ASM-SPENDOUT) "
               "against CBO's own conversion of budget authority into outlays: CBO's projected discretionary %s budget authority, "
               "account by account, goes in; outlays FY%d-%d come out%s. Five percent in each year is about twice the fit error of "
               "B2's historical timing (%s of mean outlays), so it allows for the fit and would catch a wrong rate. "
               "**This is partly in-sample.** B2 set the shares' overall level (one scale factor, %.3f) so that, over these same "
               "years, they give CBO's outlays. So the total is fitted, not tested; what is tested is the year-by-year timing, "
               "which comes from OMB's history (FY1993-2019), not from CBO." %
               (grp, yrs[0], yrs[-1], ", with the outlays of accounts that have no discretionary budget authority added separately"
                if grp == "nondefense" else "", "2.2%" if grp == "defense" else "3.3% after ground transportation is set aside", scale))
        det = ["Over FY%d-%d the method gives %+.2f%% of CBO's total (fitted). Largest year FY%d: %.0f against CBO's %.0f billion." % (
            yrs[0], yrs[-1], 100 * tot_gap, wy, pairs[wy][0], pairs[wy][1])]
        if grp == "nondefense":
            ba, cbo_out = D.cbo_series("ba_disc_nondefense"), D.cbo_series("out_disc_nondefense")
            raw = sorted((r for r in D.table("spendout-discretionary") if r["group"] == grp), key=lambda r: int(r["year_of_spending"]))
            raw = [float(r["share"]) for r in raw]
            norm = [v / sum(raw) for v in raw]
            def old(shares):
                return {y: sum(shares[k] * ba[y - k] for k in range(len(shares))) / cbo_out[y] - 1 for y in range(2029, 2037)}
            o_norm, o_raw = old(norm), old(raw)
            det.append("Earlier reading (#113): before B3's fix (#118), the library rescaled B2's OMB-fit nondefense shares, which add to "
                       "1.10, down to one, and added nothing for highway and transit. That fell %.1f%% short in FY2029 and failed. With "
                       "B2's OMB-fit shares as stored, the FY2029 gap was %+.1f%%: the extra tenth stood in for outlays whose budget authority "
                       "isn't discretionary (B2 measured about $94 billion a year, $87 billion of it in function 400: highways, transit, "
                       "airports). #118 now carries those outlays on their own, which is what this benchmark reads." % (
                           -100 * o_norm[2029], 100 * o_raw[2029]))
        out.append(_bm("PS-3" + ("a" if grp == "defense" else "b"), "Published scores",
                       "CBO: discretionary %s outlays from budget authority (February 2026 baseline)" % grp,
                       "pass" if abs(gaps[wy]) <= 0.05 else "fail", "%+.1f%%" % (100 * gaps[wy]), "CBO's outlays, FY%d-%d" % (yrs[0], yrs[-1]),
                       "5% in each year", "CBO February 2026 baseline by budget account (US-CBO/cbo-data spending_detail, models/data/budget/cbo-spending-by-function.csv)",
                       why, unit="largest yearly gap", miss="%+.1f%% in FY%d" % (100 * gaps[wy], wy) if abs(gaps[wy]) > 0.05 else None, detail=det))
        out[-1]["in_sample"] = True
    # PS-4: one act's new budget authority spent out by the library, against CBO's own spend-out
    for grp, letter in (("defense", "a"), ("nondefense", "b")):
        c = CBO_SUPPLEMENTAL_2024[grp]
        ba = {2024 + k: (c["ba"] / 1000.0 if k == 0 else 0.0) for k in range(10)}   # billions; later years zero
        lib = P.spendout_apply(ba, grp)
        lib_share = [lib.get(2024 + k, 0.0) * 1000.0 / c["ba"] for k in range(4)]
        cbo_share = [v / c["ba"] for v in c["outlays"][:4]]
        cum = lambda xs: [sum(xs[:k + 1]) for k in range(len(xs))]
        lc, cc = cum(lib_share), cum(cbo_share)
        gaps = [100 * (lc[k] - cc[k]) for k in range(4)]
        wk = max(range(4), key=lambda k: abs(gaps[k]))
        ok = all(abs(g) <= 10 for g in gaps)
        out.append(_bm("PS-4" + letter, "Published scores",
                       "CBO: outlays by year from one appropriations act's new %s budget authority (2024 Israel security supplemental, %s)" % (grp, c["title"]),
                       "pass" if ok else "fail",
                       "spent by end of year 1-4: " + ", ".join("%.0f%%" % (100 * v) for v in lc),
                       "CBO: " + ", ".join("%.0f%%" % (100 * v) for v in cc),
                       "within 10 points of CBO's cumulative share in each of the first four years",
                       "CBO, Estimated Budgetary Effects of the Israel Security Supplemental Appropriations Act, 2024 (November 1, 2023; SRC-1170), "
                       "fetched from cbo.gov on November 8, 2026 through a search tool, as Espen allowed that day",
                       "Tests the library's spend-out (provisions.spendout_apply, on B2's CBO-calibrated %s shares, ASM-SPENDOUT) on a single act: "
                       "one year of new budget authority goes in, and the share spent by the end of each year comes out, against CBO's own "
                       "estimate for the same money. Cumulative shares measure timing without depending on the act's size. Ten points allows "
                       "for one act differing from the average pattern the shares are fit to; a bigger gap means the library would misplace "
                       "that kind of spending by a year or more." % grp,
                       unit="share of budget authority", miss="%+.0f points by end of year %d" % (gaps[wk], wk + 1) if not ok else None,
                       detail=["CBO by year (millions): " + ", ".join(str(v) for v in c["outlays"]) + " from $%s million." % format(c["ba"], ","),
                               "This is one emergency supplemental, not a regular appropriation. The library uses one set of shares for every "
                               "%s row, fit to the average of all such spending; a single act's programs can spend much faster or slower. "
                               "The result shows how far one act can sit from that average, which is a limit on the library's per-row timing "
                               "rather than proof that the average is wrong (PS-3 tests the average)." % grp,
                               ("The library's defense shares spend %.0f%% of the money by the end of year 3 and take some back in year 4, "
                                "because B2's year-4 defense share is negative and is used as stored (ASM-SPENDOUT-NORM)." % (100 * max(lc))
                                if grp == "defense" and max(lc) > 1.0 else "The library's shares spend the money evenly over four years; CBO spends this act's almost at once."),
                               "The two FY2026 House estimates Espen uploaded (H.R. 6938, H.R. 7006) were checked first: they report FY2026 only, "
                               "with prior years' appropriations mixed into the outlays, so they can't test timing."]))
    return out


def shifted_interest(M, shift_pts, start):
    """Added net interest, {year: billions}, when every rate is shift_pts higher from fiscal year start,
    by the fiscal model's own stress method (fiscal-model.py, baseline()): the shift applies to all of
    last year's debt at once, and the added interest compounds at the market rate plus the shift.
    Year 2026 is the model's fixed starting year, so a shock can start in FY2027 at the earliest."""
    FM, B, base = M["_FM"], M["B"], M["results"]["BASE"]["years"]
    out, sD = {}, 0.0
    for y in range(2027, 2057):
        s_ = shift_pts / 100 if y >= start else 0.0
        sI = s_ * base[y - 1]["debt"] + (FM.marginal_rate(B, y) + s_) * sD
        sD += sI
        out[y] = sI
    return out


def bm_sensitivity(M):
    R = M["results"]
    out = []
    # The re-implementation must reproduce the model's own +1-point case exactly before it is used.
    r1 = shifted_interest(M, 1.0, 2030)
    check = max(abs(r1[y] - (R["BASE-R1"]["years"][y]["interest"] - R["BASE"]["years"][y]["interest"])) for y in range(2027, 2057))
    if check > FLOAT:
        raise AssertionError("shifted_interest does not reproduce BASE-R1 (largest gap %.3g billion)" % check)
    got = shifted_interest(M, 0.1, 2027)
    yrs = range(2027, 2037)
    tot = sum(got[y] for y in yrs)
    gaps = {y: got[y] / CBO_ROT_INTEREST[y] - 1 for y in yrs}
    wy = max(gaps, key=lambda y: abs(gaps[y]))
    tgap = tot / CBO_ROT_INTEREST_10YR - 1
    ok = abs(tgap) <= 0.15 and all(abs(g) <= 0.25 for g in gaps.values())
    misses = []
    if abs(tgap) > 0.15:
        misses.append("ten-year total %+.0f%%" % (100 * tgap))
    bad = [y for y in yrs if abs(gaps[y]) > 0.25]
    if bad:
        misses.append("%d of 10 years outside 25%% (largest FY%d, %+.0f%%)" % (len(bad), wy, 100 * gaps[wy]))
    base = R["BASE"]["years"]
    out.append(_bm("SE-1", "Sensitivity", "Interest rates 0.1 point higher on all debt from FY2027: added net interest",
                   "pass" if ok else "fail", "FY2027-36 total %.0f; FY2027 %.0f, FY2036 %.0f" % (tot, got[2027], got[2036]),
                   "CBO: total %d; FY2027 %d, FY2036 %d" % (CBO_ROT_INTEREST_10YR, CBO_ROT_INTEREST[2027], CBO_ROT_INTEREST[2036]),
                   "ten-year total within 15%, and each year within 25%",
                   "CBO, How Changes in Economic Conditions Might Affect the Federal Budget: 2026 to 2036 (publication 62257, April 2026), "
                   "Table 3, on the February 2026 baseline; Espen's November 8 upload (PR #121)",
                   "The model's stress cases (DEC-R1, BASE-R1) raise every rate by one point from FY2030. Here the same method, reproduced "
                   "exactly (it gives BASE-R1 to the dollar), is run on CBO's own scenario: every rate 0.1 point higher each year, on CBO's "
                   "baseline, from FY2027 (the first year the model can shock). That is the closest comparison the model allows, with no scaling. It is not exact: CBO's scenario starts in FY2026, a year earlier, so CBO's figure for each year has had one more year to phase in. That makes the comparison kinder to the model, not harsher. CBO says its "
                   "rules of thumb are roughly symmetrical and scalable up to one point. The total gets 15% for CBO's rounding and the "
                   "model's simpler rate rule; each year gets 25%, because the stress case is read year by year (the guardrails in "
                   "2035, 2045 and 2056), so timing matters as well as the total. Revenue effects (Federal Reserve remittances, under "
                   "$5 billion a year in CBO's table) are left out of both sides.",
                   unit="$B", miss="; ".join(misses) or None,
                   detail=["Model by year: " + ", ".join("FY%d %.0f" % (y, got[y]) for y in yrs) + ".",
                           "CBO by year: " + ", ".join("FY%d %d" % (y, CBO_ROT_INTEREST[y]) for y in yrs) + ".",
                           "Why they differ: the model applies the higher rate to all of last year's debt at once (fiscal-model.py, baseline()), "
                           "so its first-year effect is 0.1%% of about $%.1f trillion. CBO phases the higher rate in as maturing debt is refinanced, "
                           "so its effect starts lower and grows as the debt turns over. The model is higher in every year, by most at the start, "
                           "which is the cautious direction. Whether to phase rates in is a method choice for B6, not a change made here." % (base[2026]["debt"] / 1000),
                           "In the model's own +1 point case (BASE-R1), the same method adds $%.0f billion in FY2030, the first year, and $%.0f "
                           "billion over FY2030-39." % (r1[2030], sum(r1[y] for y in range(2030, 2040))),
                           "Cross-check: CBO's 2025 workbook (61183, January 2025 baseline) gives %+.2f billion in FY2026 for the same "
                           "scenario. Those are the figures in Espen's old CBO scorer (SRC-0203), so that table came from it." % ROT_2025_INTEREST_FY2026]))
    out.append(_bm("SE-2", "Sensitivity", "Slower growth (productivity or labor force 0.1 point a year slower): added deficits",
                   "fail", "0 for both (the model has no growth response)",
                   "CBO, FY2027-36: productivity %d, labor force %d" % (CBO_ROT_PRODUCTIVITY_10YR, CBO_ROT_LABOR_10YR),
                   "ten-year total within 15% for each scenario",
                   "CBO, How Changes in Economic Conditions Might Affect the Federal Budget: 2026 to 2036 (publication 62257, April 2026), "
                   "Table 2; Espen's November 8 upload (PR #121)",
                   "The model takes CBO's baseline revenue and spending as given in dollars. It has no input for slower growth, so its added "
                   "deficit is zero where CBO's is $%d billion (productivity) and $%d billion (labor force) over FY2027-36. That is a "
                   "missing capability, not a calibration error: building a growth response is for B6 or later, calibrated to these tables. "
                   "Fifteen percent is the same allowance as SE-1's total." % (CBO_ROT_PRODUCTIVITY_10YR, CBO_ROT_LABOR_10YR),
                   unit="$B", miss="-100%% for both: 0 against %d and %d" % (CBO_ROT_PRODUCTIVITY_10YR, CBO_ROT_LABOR_10YR),
                   detail=["Program rows indexed to GDP would also shrink with slower growth; the model has no way to feed that in either."]))
    return out


def bm_trust_funds():
    out = []
    if not os.path.exists(FUNDS):
        raise unittest.SkipTest("no build/funds.json: run bash models/tools/run-all.sh first")
    F = json.load(open(FUNDS))
    for id, name, got, want in (("TF-1", "Social Security (OASDI combined): current law", F["ss"]["Current law"], TRUSTEES_OASDI),
                                ("TF-2", "Medicare Hospital Insurance: current law", F["hi"]["Current law"], TRUSTEES_HI)):
        dy = got["depletion"] - want["depletion"]
        dp = got["payable"] - want["payable"]
        db = got["balance"] - want["balance"]
        ok = dy == 0 and abs(dp) <= 1.0 and abs(db) <= 0.05
        misses = [m for m, bad in (("depletion %+d year" % dy, dy != 0), ("payable %+.1f points" % dp, abs(dp) > 1.0),
                                   ("balance %+.2f points of payroll" % db, abs(db) > 0.05)) if bad]
        out.append(_bm(id, "Trust funds", name, "pass" if ok else "fail",
                       "depletion %d, %.0f%% payable, balance %.2f%%" % (got["depletion"], got["payable"], got["balance"]),
                       "depletion %d, %d%% payable, balance %.2f%%" % (want["depletion"], want["payable"], want["balance"]),
                       "depletion year exact; payable within 1 point; 75-year balance within 0.05 point of taxable payroll",
                       "2026 Social Security and Medicare Trustees Reports, intermediate assumptions, as recorded in models/data/inputs/funds-*.csv "
                       "and printed beside the model's figures by models/tools/funds-model.py (lines 306 and 335; legacy/index/dedicated-funds.md)",
                       "funds-model.py already runs this check against the Trustees on every run and prints it; this benchmark reads its output "
                       "(build/funds.json) and applies a stated tolerance. The engine uses the Trustees' own annual rates, so it should land on their "
                       "figures to within rounding: the tolerances are the published rounding (whole percent payable) plus a small allowance for the "
                       "balance, which funds-model.py says differs only by \"rounding in the published rates and the interest path\".",
                       miss=", ".join(misses) or None,
                       detail=(["funds-model.py's own page says the HI check is off and that the program's gain, not the absolute balance, is "
                                "the reading to use (legacy/index/dedicated-funds.md, Medicare HI).",
                                "Which reference: the Trustees. The engine runs on the Trustees' own cost and income rates, so their projection is "
                                "the one it should reproduce, and the miss is against them. CBO projects HI exhausted during FY%d (Long-Term Budget "
                                "Outlook data, February 2026; Espen's November 8 upload, PR #121), %d years after the Trustees and %d after the "
                                "model. That gap is a difference between the two forecasters' assumptions, not a check on the engine, so it is "
                                "context, not a target." % (CBO_HI_EXHAUSTION, CBO_HI_EXHAUSTION - want["depletion"], CBO_HI_EXHAUSTION - got["depletion"])]
                               if id == "TF-2" else [])))
    v = F["ss_validation"]
    worst = max(v, key=lambda r: abs(r["model"] - r["ssa"]))
    gap = worst["model"] - worst["ssa"]
    out.append(_bm("TF-3", "Trust funds", "SSA's own scores of seven Social Security provisions, rebuilt by the engine",
                   "pass" if all(abs(r["model"] - r["ssa"]) <= 0.05 for r in v) else "fail", round(gap, 3), 0.0,
                   "0.05 point of taxable payroll for each provision",
                   "SSA Office of the Chief Actuary, single-provision estimates on the 2026 Trustees' basis (models/data/inputs/funds-ss-ssa-runs.csv)",
                   "funds-model.py rebuilds seven of SSA's own provision scores from the same tax bases it uses for the plan's Social Security "
                   "provisions. SSA publishes them to 0.01 point; 0.05 allows for that and the engine's fitted tail.",
                   unit="points, largest gap", detail=["Largest gap: %s, model %+.3f against SSA %+.2f." % (worst["label"], worst["model"], worst["ssa"])]))
    return out


def model_facts():
    """Counts the model card states, generated so they can't go stale."""
    S = P.specs()
    scored = [s for s in S.values() if s["in_model"] == "yes"]
    unk = {f: sum(1 for s in scored if s[f] == "unknown") for f in ("vehicle", "appropriation", "budget_authority")}
    model_only = {f: sum(1 for s in scored if s[f] == "model") for f in ("indexation_basis", "expiry_basis")}
    return dict(specs=len(S), scored=len(scored), unknown=unk, model_only=model_only)


def run_all():
    if not os.path.exists(LEDGER):
        raise unittest.SkipTest("no build/ledger.json: run bash models/tools/run-all.sh first")
    FM = fiscal_model()
    M = FM.build(LEDGER, BASELINE)
    M["_FM"] = FM
    return ([bm_baseline()] + bm_identities(M) + bm_published(M) + bm_sensitivity(M) + bm_trust_funds())


# ---------------------------------------------------------------- the pages

def _fmt(v):
    if v is None:
        return "—"
    if isinstance(v, float):
        return "%.3g" % v if abs(v) < 0.01 and v != 0 else ("%.2f" % v if abs(v) < 100 else "%.0f" % v)
    return str(v)


def _counts(results):
    c = {}
    for r in results:
        c[r["status"]] = c.get(r["status"], 0) + 1
    return c


def summary_table(results):
    lines = ["| ID | Benchmark | Result | Model | Target | Tolerance | Miss |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in results:
        lines.append("| %s | %s | **%s**%s | %s%s | %s | %s | %s |" % (
            r["id"], r["name"], r["status"], " (partly in-sample)" if r.get("in_sample") else "", _fmt(r["value"]), (" (%s)" % r["unit"]) if r["unit"] and r["value"] is not None else "",
            _fmt(r["target"]), r["tolerance"], r["miss"] or "—"))
    return "\n".join(lines)


def counts_line(results):
    c = _counts(results)
    line = "%d benchmarks: %s." % (len(results), ", ".join("%d %s" % (c[k], k) for k in ("pass", "fail", "pending", "info") if c.get(k)))
    ins = [r["id"] for r in results if r.get("in_sample") and r["status"] == "pass"]
    if ins:
        line += (" %d of the passes (%s) are partly in-sample: their level was calibrated to the same CBO figures they are checked "
                 "against, so only their timing is tested." % (len(ins), ", ".join(ins)))
    return line


def milestone_line(results):
    """The workflow's "benchmarks before trust" gate: passed only when nothing fails and nothing is pending."""
    open_ = [r["id"] for r in results if r["status"] in ("fail", "pending")]
    if not open_:
        return "**Milestone status: passed.** Every benchmark passes."
    return ("**Milestone status: not passed.** %s %s not yet resolved, so B4 does not yet meet the workflow's \"benchmarks before trust\" "
            "condition. These results are a diagnostic report; readings that depend on the open benchmarks stay out of decision and public "
            "figures (`MODEL-CARD.md`, \"What is not yet validated\")." % (", ".join(open_), "is" if len(open_) == 1 else "are"))


def page(results):
    w = ["# Budget model benchmarks: results",
         "",
         "Role: the current result of every benchmark of the federal budget model (piece B4 of `models/tools/budget/WORKFLOW.md`). "
         "Status: generated by `models/tools/budget/test_benchmarks.py` on every run of `models/tools/run-all.sh`; do not edit by hand. "
         "The same results are in `benchmarks.json` for other tools. What the benchmarks mean, and the model's limits, are in `MODEL-CARD.md`.",
         "",
         "**How to read it.** *pass*: within the stated tolerance. *fail*: outside it; the miss column gives the size. *pending*: there is "
         "no target yet, because the source isn't in the library or the model can't compute the quantity. A miss is reported, never fixed "
         "by changing the model or the tolerance.",
         "",
         counts_line(results),
         "",
         milestone_line(results),
         "",
         summary_table(results),
         ""]
    group = None
    for r in results:
        if r["group"] != group:
            group = r["group"]
            w += ["## " + group, ""]
        w += ["### %s. %s" % (r["id"], r["name"]), "",
              "- **Result:** %s%s" % (r["status"], (". Miss: " + r["miss"]) if r["miss"] else ""),
              "- **Model:** %s%s" % (_fmt(r["value"]), (" (%s)" % r["unit"]) if r["unit"] and r["value"] is not None else ""),
              "- **Target:** %s" % _fmt(r["target"]),
              "- **Tolerance:** %s" % r["tolerance"],
              "- **Source:** %s" % r["source"],
              "- **Why:** %s" % r["why"]]
        w += ["- %s" % d for d in r["detail"]]
        w.append("")
    w += ["## Documents for Espen to upload", "",
          "www.cbo.gov's bot check blocks direct downloads from agent sessions (403). Since November 8 Espen allows agents to fetch CBO "
          "documents through search tools instead; an upload (`library/fetch_public.py --file`) also works. CBO's own GitHub "
          "data repository (`US-CBO/cbo-data`, commit 284a956) was checked first, and so were the 16 CBO files Espen uploaded on November 8 "
          "(PR #121), and CBO documents fetched through search tools where needed.", ""]
    w += ["%d. %s. *Unlocks:* %s" % (i + 1, d, u) for i, (d, u) in enumerate(UPLOADS)] or ["None outstanding: every benchmark has its source."]
    return "\n".join(w) + "\n"


def data_json(results):
    return json.dumps({"role": "Budget model benchmark results (B4), generated by models/tools/budget/test_benchmarks.py; do not edit by hand.",
                       "counts": _counts(results),
                       "milestone_passed": not any(r["status"] in ("fail", "pending") for r in results),
                       "open": [r["id"] for r in results if r["status"] in ("fail", "pending")], "benchmarks": results,
                       "uploads": [{"document": d, "unlocks": u} for d, u in UPLOADS]}, indent=1, sort_keys=False, default=float) + "\n"


def card(results, facts, template):
    a, b = template.index(CARD_START) + len(CARD_START), template.index(CARD_END)
    u, mo = facts["unknown"], facts["model_only"]
    block = ["", "*This block is generated by `test_benchmarks.py` from the latest run; the rest of the card is written by hand.*", "",
             counts_line(results), "", milestone_line(results), "",
             summary_table(results), "",
             "Unknown fields in the %d provision specs the model scores (B3, `provisions.md`): vehicle %d, appropriation type %d, "
             "budget authority %d. The growth index is the model's own assumption, not the law's, for %d rows, and the end year for %d." % (
                 facts["scored"], u["vehicle"], u["appropriation"], u["budget_authority"], mo["indexation_basis"], mo["expiry_basis"]), ""]
    return template[:a] + "\n".join(block) + template[b:]


def write(results, out_dir=BUILD):
    with open(os.path.join(HERE, CARD)) as f:
        template = f.read()
    texts = {PAGE: page(results), DATA_OUT: data_json(results), CARD: card(results, model_facts(), template)}
    for k, t in texts.items():
        with open(os.path.join(out_dir, BUILD_NAMES[k]), "w") as f:
            f.write(t)
    return texts


# ---------------------------------------------------------------- tests

def setUpModule():
    global RESULTS, TEXTS
    RESULTS = run_all()
    TEXTS = write(RESULTS)


class Benchmarks(unittest.TestCase):
    def test_well_formed(self):
        ids = [r["id"] for r in RESULTS]
        self.assertEqual(len(ids), len(set(ids)))
        for r in RESULTS:
            self.assertIn(r["status"], ("pass", "fail", "pending", "info"), r["id"])
            for k in ("source", "tolerance", "why", "name"):
                self.assertTrue(r[k], "%s has no %s" % (r["id"], k))
            if r["status"] == "fail":
                self.assertTrue(r["miss"], r["id"] + " fails without saying by how much")
            if r["status"] == "pending":
                self.assertIn("ending", r["source"], r["id"] + " is pending without saying why")

    def test_required_groups(self):
        groups = {r["group"] for r in RESULTS}
        self.assertEqual(groups, {"Baseline", "Accounting identities", "Published scores", "Sensitivity", "Trust funds"})
        scored = [r for r in RESULTS if r["group"] == "Published scores" and r["status"] in ("pass", "fail")]
        self.assertGreaterEqual(len(scored), 2, "at least two published estimates must be reproduced or missed, not pending")

    def test_baseline_and_identities_hold(self):
        """These are accounting, not estimates: any failure is a bug, and fails the run."""
        for r in RESULTS:
            if r["group"] in ("Baseline", "Accounting identities"):
                self.assertEqual(r["status"], "pass", "%s: %s (%s)" % (r["id"], r["name"], r["miss"] or r["value"]))

    def test_sensitivity_targets_are_cbos_2026_rules(self):
        for r in RESULTS:
            if r["group"] == "Sensitivity":
                self.assertIn("62257", r["source"], r["id"] + ": targets come from CBO's 2026 rules of thumb, not SRC-0203's leads")


if __name__ == "__main__":
    unittest.main()
