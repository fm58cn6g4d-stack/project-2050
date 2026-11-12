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

Statuses: pass, fail (outside tolerance), bounded (outside tolerance, with the cause shown by
the benchmark itself and the size of the miss carried as a stated range on every reading that
depends on it; the entry's "bound" says what), pending (the source is not in the library, or the
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
import build_data as BD   # noqa: E402

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
    "nondefense": {"title": "Title II, State, Foreign Operations", "ba": 3700, "one_account": 3500,   # Foreign Military Financing (H.R. 6126, Title II)
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

CBO_ROT_DEBT_SERVICE_10YR = {"productivity": 40, "labor_force": 20}   # Table 2, debt service, FY2027-36
# CBO's 2025 workbook (61183, January 2025 baseline), illustrative sheets 5 and 6: the same 0.1-point
# scenarios from FY2025, billions by year of the shock (k = 1 is FY2025), and the baseline's fiscal-year
# GDP. Used only for the cross-vintage check in SE-2.
ROT_2025 = {
    "gdp": [30136.1, 31341.3, 32538.1, 33764.5, 35047.1, 36393.7, 37792.1, 39252.4, 40767.9, 42330.4, 43936.5],
    "productivity": dict(rev=[-4.219, -11.04, -18.894, -27.509, -36.963, -47.412, -58.82, -71.374, -84.974, -99.661, -115.773],
                         man=[-0.023, -0.486, -1.061, -1.901, -2.476, -3.312, -4.229, -5.332, -6.691, -8.041, -9.694],
                         rate=[-0.596, -2.314, -4.533, -7.337, -10.657, -14.574, -18.938, -23.798, -28.932, -34.53, -40.346]),
    "labor_force": dict(rev=[-1.649, -4.283, -7.2, -10.373, -13.878, -17.782, -22.053, -26.788, -31.961, -37.56, -43.764],
                        man=[0.281, 0.74, 1.211, 1.733, 2.29, 2.856, 3.532, 4.482, 5.455, 6.303, 7.304],
                        rate=[-0.3, -1.101, -2.174, -3.507, -5.131, -7.009, -9.071, -11.442, -13.92, -16.604, -19.399]),
}


def growth_vintage_2025(M):
    """SE-2's cross-vintage check: growth_path run on shares from CBO's 2025 workbook instead of 62257."""
    FM, B = M["_FM"], M["B"]
    out = {}
    for f in ("productivity", "labor_force"):
        sh = {f: {k: dict(rev=ROT_2025[f]["rev"][k - 1] / ROT_2025["gdp"][k - 1], man=ROT_2025[f]["man"][k - 1] / ROT_2025["gdp"][k - 1],
                          rate=ROT_2025[f]["rate"][k - 1] / ROT_2025["gdp"][k - 1], gap=0.0) for k in range(1, 12)}}
        gp = FM.growth_path(B, f, -0.1, 2026, shares=sh)
        out[f] = sum(gp[y]["deficit"] for y in range(2027, 2037))
    return out


UPLOADS = [
]


# ---------------------------------------------------------------- the benchmarks

def _bm(id, group, name, status, value, target, tolerance, source, why, unit="", miss=None, detail=None, bound=None):
    return dict(id=id, group=group, name=name, status=status, value=value, target=target,
                tolerance=tolerance, unit=unit, miss=miss, source=source, why=why, detail=detail or [], bound=bound)


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
    # spent out at B2's shares, plus, for nondefense, outlays with no discretionary BA)
    for grp in ("defense", "nondefense"):
        pairs = P.cbo_discretionary_outlays(grp)
        yrs = sorted(pairs)
        gaps = {y: pairs[y][0] / pairs[y][1] - 1 for y in yrs}
        wy = max(gaps, key=lambda y: abs(gaps[y]))
        tot_gap = sum(pairs[y][0] for y in yrs) / sum(pairs[y][1] for y in yrs) - 1
        scale = next(float(r["scale"]) for r in D.table("spendout-discretionary-cbo") if r["group"] == grp)
        if grp == "defense":
            why = ("Tests B3's spend-out method (provisions.cbo_discretionary_outlays, ASM-SPENDOUT) against CBO's own conversion of "
                   "budget authority into outlays: CBO's projected discretionary defense budget authority, account by account, goes in; "
                   "outlays FY%d-%d come out. The defense shares are CBO's own rates, the average of its spend-out of three regular "
                   "defense acts (FY2014, FY2017 and FY2023 NDAA estimates; B2's build_data.CBO_DEFENSE_ACTS), used without fitting or "
                   "scaling, so this is **out of sample**: nothing was set to make these years match. The years start in FY2030 because "
                   "the five shares need four earlier years of CBO budget authority, which starts in FY2026. Five percent in each year "
                   "allows for the acts' mix differing from the baseline's and would catch a wrong rate." % (yrs[0], yrs[-1]))
            det = ["Over FY%d-%d the shares give %+.2f%% of CBO's total, unfitted. Largest year FY%d: %.0f against CBO's %.0f billion." % (
                yrs[0], yrs[-1], 100 * tot_gap, wy, pairs[wy][0], pairs[wy][1]),
                "Earlier reading: until B6's spend-out fix, defense used a four-year fit to OMB's FY1993-2019 totals (44%, 34%, 24% "
                "and -4%), scaled by 1.009 to these same CBO years, so this benchmark passed in-sample (+0.9% in its largest year, "
                "FY2029-36). The fit's negative fourth share was the defect behind PS-4a's 103%."]
        else:
            why = ("Tests B3's spend-out method (provisions.cbo_discretionary_outlays, on B2's CBO-calibrated nondefense shares, ASM-SPENDOUT) "
                   "against CBO's own conversion of budget authority into outlays: CBO's projected discretionary nondefense budget authority, "
                   "account by account, goes in; outlays FY%d-%d come out, with the outlays of accounts that have no discretionary budget "
                   "authority added separately. Five percent in each year is about twice the fit error of B2's historical timing (3.3%% of "
                   "mean outlays after ground transportation is set aside), so it allows for the fit and would catch a wrong rate. "
                   "**This is partly in-sample.** B2 set the shares' overall level (one scale factor, %.3f) so that, over these same "
                   "years, they give CBO's outlays. So the total is fitted, not tested; what is tested is the year-by-year timing, "
                   "which comes from OMB's history (FY1993-2019), not from CBO." % (yrs[0], yrs[-1], scale))
            det = ["Over FY%d-%d the method gives %+.2f%% of CBO's total (fitted). Largest year FY%d: %.0f against CBO's %.0f billion." % (
                yrs[0], yrs[-1], 100 * tot_gap, wy, pairs[wy][0], pairs[wy][1])]
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
        if grp == "nondefense":
            out[-1]["in_sample"] = True
    # PS-4c first (PS-4a's status depends on it): CBO's spend-out of regular defense acts, each
    # act against the average of the other two (leave one out), so no act tests rates it helped set
    acts = BD.CBO_DEFENSE_ACTS
    cum = lambda xs: [sum(xs[:k + 1]) for k in range(len(xs))]
    per = {k: [o / ba for o in outs] for k, (_, ba, outs) in acts.items()}
    loo = {}
    for k in per:
        others = [per[j] for j in per if j != k]
        avg = [sum(p[i] for p in others) / len(others) for i in range(5)]
        loo[k] = [100 * (a - b) for a, b in zip(cum(avg), cum(per[k]))]
    worst_act = max(loo, key=lambda k: max(abs(g) for g in loo[k]))
    worst_gap = max(loo[worst_act], key=abs)
    ps4c_ok = all(abs(g) <= 10 for v in loo.values() for g in v[:4])
    lib_d = P._spendout("defense")
    ps4c = _bm("PS-4c", "Published scores",
               "CBO: outlays by year from a regular year's defense budget authority (three NDAA estimates, each against the other two)",
               "pass" if ps4c_ok else "fail",
               "largest gap %+.1f points (%s, year %d)" % (worst_gap, worst_act, loo[worst_act].index(worst_gap) + 1),
               "CBO's cumulative share spent, each act", "within 10 points of each act's cumulative share in each of the first four years",
               "CBO cost estimates of the National Defense Authorization Acts for FY2014 (S. 1197, July 25, 2013; SRC-2454), FY2017 "
               "(H.R. 4909, May 11, 2016; SRC-2455) and FY2023 (H.R. 7900, in H. Rept. 117-397; SRC-2456), Table 1, the base-budget line: "
               "the year's specified authorization and CBO's estimated outlays from it in years 1-5. Read through a search tool on "
               "November 12, 2026, as Espen allowed on November 8",
               "Tests the library's defense spend-out where it should hold: a full year of regular defense appropriations, which CBO "
               "spends out \"using historical spend-out rates\". The library's defense shares are the average of these three acts "
               "(B2, ASM-SPENDOUT), so each act is checked against the average of the other two only; that keeps it out of sample. "
               "Ten points, as for PS-4a and PS-4b.",
               unit="cumulative share of budget authority",
               miss=None if ps4c_ok else "%+.1f points" % worst_gap,
               detail=["CBO's cumulative share spent by the end of years 1-5: " + "; ".join(
                   "%s %s" % (k, ", ".join("%.0f%%" % (100 * v) for v in cum(per[k]))) for k in per) + ".",
                   "The library's shares (the three-act average): " + ", ".join("%.1f%%" % (100 * v) for v in lib_d) +
                   " by year of spending; %.0f%% within five years. CBO's tables stop at year 5; the rest (about 3%%) is left out, "
                   "so the library's budget authority for a defense row is about 3%% above its five-year outlays." % (100 * sum(lib_d)),
                   "Leave-one-out gaps by year (points): " + "; ".join("%s %s" % (k, ", ".join("%+.1f" % g for g in v)) for k, v in loo.items()) + "."])
    # PS-4: one act's new budget authority spent out by the library, against CBO's own spend-out
    for grp, letter in (("defense", "a"), ("nondefense", "b")):
        c = CBO_SUPPLEMENTAL_2024[grp]
        ba = {2024 + k: (c["ba"] / 1000.0 if k == 0 else 0.0) for k in range(10)}   # billions; later years zero
        lib = P.spendout_apply(ba, grp)
        lib_share = [lib.get(2024 + k, 0.0) * 1000.0 / c["ba"] for k in range(4)]
        cbo_share = [v / c["ba"] for v in c["outlays"][:4]]
        lc, cc = cum(lib_share), cum(cbo_share)
        gaps = [100 * (lc[k] - cc[k]) for k in range(4)]
        wk = max(range(4), key=lambda k: abs(gaps[k]))
        ok = all(abs(g) <= 10 for g in gaps)
        if grp == "defense":
            why_mix = ("Title I is weighted to procurement and research (replacing defense articles sent to Israel, buying Iron Dome "
                       "and David's Sling, developing Iron Beam), which spend more slowly than a regular year's mix of pay, operations "
                       "and procurement. CBO's own regular-act rates miss this act by about as much (PS-4c's three acts average "
                       "%s by the end of years 1-4)." % ", ".join("%.0f%%" % (100 * v) for v in cum([sum(per[k][i] for k in per) / len(per) for i in range(4)])))
            bound = ("A single defense row's year-by-year outlays and budget authority carry a range of %.0f points of its budget "
                     "authority in any of its first four years (this act's largest gap), more for a row that is mostly procurement or "
                     "research. Ten-year totals are unaffected; the average rate holds for a regular year's mix (PS-4c, %s)." % (
                         max(abs(g) for g in gaps), "pass" if ps4c_ok else "fail"))
            status = "pass" if ok else ("bounded" if ps4c_ok else "fail")
        else:
            why_mix = ("Title II is $3,500 million of Foreign Military Financing for Israel out of $3,700 million (95%%; H.R. 6126 as passed "
                       "by the House, Title II); the rest is $200 million for diplomatic programs and emergencies. CBO records nearly all "
                       "of that financing as spent in the first year, an account-specific treatment no average nondefense rate can "
                       "reproduce: B2's nondefense shares spend %.0f%% in the first year, as OMB's history of all nondefense "
                       "appropriations does." % (100 * P._spendout("nondefense")[0]))
            bound = ("A single nondefense row's year-by-year outlays and budget authority carry a range of up to %.0f points of its "
                     "budget authority in its first years when the row is one account with its own outlay rule (foreign military "
                     "financing, grants paid on award, loans), and are not validated for a regular nondefense act: no CBO estimate of "
                     "one is benchmarked yet. The average's timing is tested only against CBO's projected totals (PS-3b, partly "
                     "in-sample). Ten-year totals are unaffected." % max(abs(g) for g in gaps))
            # bounded only while the title is essentially one account with its own outlay rule
            status = "pass" if ok else ("bounded" if c["one_account"] / c["ba"] >= 0.9 else "fail")
        out.append(_bm("PS-4" + letter, "Published scores",
                       "CBO: outlays by year from one appropriations act's new %s budget authority (2024 Israel security supplemental, %s)" % (grp, c["title"]),
                       status,
                       "spent by end of year 1-4: " + ", ".join("%.0f%%" % (100 * v) for v in lc),
                       "CBO: " + ", ".join("%.0f%%" % (100 * v) for v in cc),
                       "within 10 points of CBO's cumulative share in each of the first four years",
                       "CBO, Estimated Budgetary Effects of the Israel Security Supplemental Appropriations Act, 2024 (November 1, 2023; SRC-1170), "
                       "fetched from cbo.gov on November 8, 2026 through a search tool, as Espen allowed that day",
                       "Tests the library's spend-out (provisions.spendout_apply, on B2's %s shares, ASM-SPENDOUT) on a single act: "
                       "one year of new budget authority goes in, and the share spent by the end of each year comes out, against CBO's own "
                       "estimate for the same money. Cumulative shares measure timing without depending on the act's size. Ten points allows "
                       "for one act differing from the average pattern the shares are fit to; a bigger gap means the library would misplace "
                       "that kind of spending by a year or more. *Bounded*, not passed, when the miss comes from the act's own mix of "
                       "programs rather than from the rates: the status says the timing of such a row is uncertain by the stated range, "
                       "not that it is right." % grp,
                       unit="share of budget authority", miss="%+.0f points by end of year %d" % (gaps[wk], wk + 1) if not ok else None,
                       bound=bound if status == "bounded" else None,
                       detail=["CBO by year (millions): " + ", ".join(str(v) for v in c["outlays"]) + " from $%s million." % format(c["ba"], ","),
                               "This is one emergency supplemental, not a regular appropriation. The library uses one set of shares for every "
                               "%s row; a single act's programs can spend much faster or slower. %s" % (grp, why_mix),
                               ("Before B6's spend-out fix the library's defense shares were a four-year fit to OMB's totals with a negative "
                                "fourth share, which spent 103% of this act by the end of year 3 and took some back in year 4 (+21 points by "
                                "end of year 3). CBO's own rates remove that defect: every share is positive and the money is spent once."
                                if grp == "defense" else
                                "The library's nondefense shares are unchanged by B6's spend-out fix; their four shares were already positive."),
                               "The two FY2026 House estimates Espen uploaded (H.R. 6938, H.R. 7006) were checked first: they report FY2026 only, "
                               "with prior years' appropriations mixed into the outlays, so they can't test timing."]))
    out.append(ps4c)
    return out


MATURITY = os.path.join(ROOT, "models", "data", "budget", "treasury-maturity.csv")


def unrepriced_by_year():
    """From Treasury's maturity table alone: the share of the debt outstanding when a shock starts
    that is still at its old rate, averaged over each year of the shock. The table gives the share
    at each quarter-end; between quarter-ends it is taken as a straight line."""
    with open(MATURITY) as f:
        S = [float(r["share_unrepriced"]) for r in csv.DictReader(f)]
    out = {}
    for k in range(1, (len(S) - 1) // 4 + 1):
        pts = S[4 * (k - 1):4 * k + 1]
        out[k] = (pts[0] / 2 + sum(pts[1:-1]) + pts[-1] / 2) / 4
    return out


def shifted_interest(M, shift_pts, start):
    """Added net interest, {year: billions}, when every rate is shift_pts higher from fiscal year start,
    by the fiscal model's stated stress method (ASM-RATE-SHIFT, ASM-RATE-ROLLOVER), rewritten here
    from the written rule rather than called: the debt outstanding at the end of start-1 reaches the
    higher rate only as it matures (Treasury's maturity structure); debt borrowed since pays it in
    full; and the added interest is borrowed at the program's rate plus the shift. The debt path is the
    model's own baseline (BASE); FY2025's is the actual, so a shock can start as early as FY2026."""
    FM, B, base = M["_FM"], M["B"], M["results"]["BASE"]["years"]
    debt = lambda y: base[y]["debt"] if y in base else B[y]["debt_public"]
    still_old = unrepriced_by_year()
    out, sD, s_ = {}, 0.0, shift_pts / 100
    D0 = debt(start - 1)
    for y in range(start, 2057):
        new_rate_debt = max(0.0, debt(y - 1) - D0 * still_old.get(y - start + 1, 0.0))
        sI = s_ * new_rate_debt + (FM.marginal_rate(B, y) + s_) * sD
        sD += sI
        out[y] = sI
    return out


def bm_sensitivity(M):
    R = M["results"]
    out = []
    # The re-implementation must reproduce the model's own +1-point case exactly before it is used.
    r1 = shifted_interest(M, 1.0, 2030)
    check = max(abs(r1.get(y, 0.0) - (R["BASE-R1"]["years"][y]["interest"] - R["BASE"]["years"][y]["interest"])) for y in range(2027, 2057))
    if check > FLOAT:
        raise AssertionError("shifted_interest does not reproduce BASE-R1 (largest gap %.3g billion)" % check)
    got = shifted_interest(M, 0.1, 2026)
    old = {}   # the method before B6, for the record: all of last year's debt repriced at once
    sD = 0.0
    for y in range(2026, 2057):
        sI = 0.001 * (R["BASE"]["years"][y - 1]["debt"] if y > 2026 else M["B"][2025]["debt_public"]) + (M["_FM"].marginal_rate(M["B"], y) + 0.001) * sD
        sD += sI
        old[y] = sI
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
    out.append(_bm("SE-1", "Sensitivity", "Interest rates 0.1 point higher on all debt from FY2026: added net interest",
                   "pass" if ok else "fail", "FY2027-36 total %.0f; FY2027 %.0f, FY2036 %.0f" % (tot, got[2027], got[2036]),
                   "CBO: total %d; FY2027 %d, FY2036 %d" % (CBO_ROT_INTEREST_10YR, CBO_ROT_INTEREST[2027], CBO_ROT_INTEREST[2036]),
                   "ten-year total within 15%, and each year within 25%",
                   "CBO, How Changes in Economic Conditions Might Affect the Federal Budget: 2026 to 2036 (publication 62257, April 2026), "
                   "Table 3, on the February 2026 baseline; Espen's November 8 upload (PR #121). Treasury, Monthly Statement of the Public "
                   "Debt, September 30, 2026, for the maturity structure (models/data/budget/treasury-maturity.csv)",
                   "The model's stress cases (DEC-R1, BASE-R1) raise every rate by one point from FY2030. Here the same method, rewritten "
                   "from its written rule and checked to give BASE-R1 to the dollar, is run on CBO's own scenario: every rate 0.1 point "
                   "higher each year from FY2026, CBO's first year, on the model's baseline. That compares like with like, with no scaling. "
                   "FY2026 itself is not compared, because the model's FY2026 is the actual year and CBO's FY2026 shock is partial. "
                   "As in CBO's rules of thumb, the higher rate reaches the debt outstanding at the start only as it is refinanced, "
                   "on Treasury's maturity structure (ASM-RATE-ROLLOVER); new borrowing pays it in full. CBO says its rules of thumb are "
                   "roughly symmetrical and scalable up to one point. The total gets 15% for CBO's rounding and the model's simpler rate "
                   "rule; each year gets 25%, because the stress case is read year by year (the guardrails in 2035, 2045 and 2056), so "
                   "timing matters as well as the total. Revenue effects (Federal Reserve remittances, under $5 billion a year in CBO's "
                   "table) are left out of both sides.",
                   unit="$B", miss="; ".join(misses) or None,
                   detail=["Model by year: " + ", ".join("FY%d %.0f" % (y, got[y]) for y in yrs) + ".",
                           "CBO by year: " + ", ".join("FY%d %d" % (y, CBO_ROT_INTEREST[y]) for y in yrs) + ".",
                           "Before B6 the model applied the higher rate to all of last year's debt at once. On this scenario that method gave "
                           "$%.0f billion over FY2027-36 and $%.0f billion in FY2027 (from a FY2027 start, B4's run: $502 billion and $32 billion), "
                           "against CBO's $383 billion and $14 billion. Phasing the rate in as debt rolls over is B6's fix (item 1)." % (
                               sum(old[y] for y in yrs), old[2027]),
                           "In the model's own +1 point case (BASE-R1), the phased method adds $%.0f billion in FY2030, the first year, and $%.0f "
                           "billion over FY2030-39." % (r1[2030], sum(r1[y] for y in range(2030, 2040))),
                           "Cross-check: CBO's 2025 workbook (61183, January 2025 baseline) gives %+.2f billion in FY2026 for the same "
                           "scenario. Those are the figures in Espen's old CBO scorer (SRC-0203), so that table came from it." % ROT_2025_INTEREST_FY2026]))
    vint = growth_vintage_2025(M)
    for sid, factor, want, label in (("SE-2a", "productivity", CBO_ROT_PRODUCTIVITY_10YR, "productivity"),
                                     ("SE-2b", "labor_force", CBO_ROT_LABOR_10YR, "labor force")):
        gp = M["_FM"].growth_path(M["B"], factor, -0.1, 2026)
        # independent arithmetic: each year's deficit is its parts, and the debt grows by the deficits
        worst = max(abs(gp[y]["deficit"] - (-gp[y]["rev"] + gp[y]["man"] + gp[y]["rate"] + gp[y]["debt_service"])) for y in gp)
        if worst > FLOAT:
            raise AssertionError("growth_path's deficit is not the sum of its parts (%.3g)" % worst)
        got = sum(gp[y]["deficit"] for y in yrs)
        ds = sum(gp[y]["debt_service"] for y in yrs)
        cbo_ds = CBO_ROT_DEBT_SERVICE_10YR[factor]
        miss = got / want - 1
        out.append(_bm(sid, "Sensitivity", "Slower growth (%s growth 0.1 point a year slower from FY2026): added deficits, FY2027-36" % label,
                       "pass" if abs(miss) <= 0.15 else "fail", round(got, 1), want, "ten-year total within 15%",
                       "CBO, How Changes in Economic Conditions Might Affect the Federal Budget: 2026 to 2036 (publication 62257, April 2026), "
                       "Tables 1 and 2; Espen's November 8 upload (PR #121); copied into models/data/budget/cbo-rules-of-thumb.csv",
                       "B6 (item 2) gives the model a growth link (fiscal-model.py, growth_path; ASM-GROWTH-LINK): CBO's own effects on "
                       "revenue, mandatory spending and interest rates, as shares of GDP by year of the shock, scaled to the size of the "
                       "change; the model then borrows the added deficits at its own rate. **This is in-sample.** The link is taken from "
                       "the same CBO table it is checked against, so the benchmark tests only the model's debt service on the added "
                       "deficits ($%.0f billion against CBO's $%d billion) and the bookkeeping, not how well the link predicts. "
                       "Fifteen percent is the same allowance as SE-1's total." % (ds, cbo_ds),
                       unit="$B", miss=None if abs(miss) <= 0.15 else "%+.0f%%" % (100 * miss),
                       detail=["Model by year: " + ", ".join("FY%d %.0f" % (y, gp[y]["deficit"]) for y in yrs) + ".",
                               "Out of sample, across vintages: the same method calibrated to CBO's 2025 workbook (61183, January 2025 "
                               "baseline) and applied to the February 2026 baseline gives $%.0f billion, %+.0f%% from CBO's 2026 figure. "
                               "CBO's own rules of thumb moved that much between the two baselines, mostly through a larger effect of lower "
                               "interest rates in 2026. Read any growth reading with that much uncertainty." % (vint[factor], 100 * (vint[factor] / want - 1)),
                               "Not modeled: program rows indexed to GDP would also shrink with slower growth; the link moves the baseline only."]))
        out[-1]["in_sample"] = "bookkeeping only"   # the link is CBO's table itself (#132's review)
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
            r["id"], r["name"], r["status"], _in_sample_label(r), _fmt(r["value"]), (" (%s)" % r["unit"]) if r["unit"] and r["value"] is not None else "",
            _fmt(r["target"]), r["tolerance"], r["miss"] or "—"))
    return "\n".join(lines)


def _in_sample_label(r):
    """ (partly in-sample) for a calibrated level; (in-sample: bookkeeping only) where the method is
    the target's own table, so only the arithmetic around it is tested (SE-2a, SE-2b)."""
    v = r.get("in_sample")
    return "" if not v else (" (in-sample: %s)" % v if isinstance(v, str) else " (partly in-sample)")


def counts_line(results):
    c = _counts(results)
    line = "%d benchmarks: %s." % (len(results), ", ".join("%d %s" % (c[k], k) for k in ("pass", "bounded", "fail", "pending", "info") if c.get(k)))
    part = [r["id"] for r in results if r.get("in_sample") is True and r["status"] == "pass"]
    book = [r["id"] for r in results if isinstance(r.get("in_sample"), str) and r["status"] == "pass"]
    if part:
        line += (" %s %s partly in-sample: calibrated to the same CBO figures %s checked against, so only part is tested "
                 "(the entry says which part)." % (", ".join(part), "is" if len(part) == 1 else "are", "it is" if len(part) == 1 else "they are"))
    if book:
        line += (" %s %s in-sample, bookkeeping only: the method is the target's own CBO table, so the pass tests the arithmetic "
                 "and debt service around it, not how well it predicts." % (" and ".join(book), "is" if len(book) == 1 else "are"))
    return line


def milestone_line(results):
    """The workflow's "benchmarks before trust" gate: passed only when nothing fails and nothing is
    pending. A bounded benchmark is resolved, not passed: the readings it covers carry its range."""
    open_ = [r["id"] for r in results if r["status"] in ("fail", "pending")]
    bnd = [r["id"] for r in results if r["status"] == "bounded"]
    if not open_ and not bnd:
        return "**Milestone status: passed.** Every benchmark passes."
    if not open_:
        return ("**Milestone status: passed, with %s bounded.** No benchmark fails or is pending. %s %s outside %s tolerance for a "
                "cause the benchmark itself shows, and the readings that depend on %s carry %s stated range (`MODEL-CARD.md`, \"What is "
                "bounded\")." % (", ".join(bnd), ", ".join(bnd), "is" if len(bnd) == 1 else "are", "its" if len(bnd) == 1 else "their",
                                  "it" if len(bnd) == 1 else "them", "its" if len(bnd) == 1 else "their"))
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
         "**How to read it.** *pass*: within the stated tolerance. *fail*: outside it; the miss column gives the size. *bounded*: outside it, "
         "for a cause the benchmark itself shows (such as one act's mix of programs), with the miss carried as a stated range on every "
         "reading that depends on it; the entry's bound says what. *pending*: there is "
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
              ] + (["- **Bound:** %s" % r["bound"]] if r.get("bound") else []) + [
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
            self.assertIn(r["status"], ("pass", "bounded", "fail", "pending", "info"), r["id"])
            if r["status"] == "bounded":
                self.assertTrue(r["miss"] and r["bound"], r["id"] + " is bounded without its miss and its stated range")
            for k in ("source", "tolerance", "why", "name"):
                self.assertTrue(r[k], "%s has no %s" % (r["id"], k))
            if r["status"] == "fail":
                self.assertTrue(r["miss"], r["id"] + " fails without saying by how much")
            if r["status"] == "pending":
                self.assertIn("ending", r["source"], r["id"] + " is pending without saying why")

    def test_required_groups(self):
        groups = {r["group"] for r in RESULTS}
        self.assertEqual(groups, {"Baseline", "Accounting identities", "Published scores", "Sensitivity", "Trust funds"})
        scored = [r for r in RESULTS if r["group"] == "Published scores" and r["status"] in ("pass", "bounded", "fail")]
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
