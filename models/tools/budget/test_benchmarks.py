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
# Each is copied from the repository's own record of the source, which is cited; none is fetched.

# JCT's estimates of making the temporary provisions of Public Law 119-21 permanent, billions by
# fiscal year, against CBO's January 2025 baseline, excluding interest. CBO letter of August 4,
# 2025, Table 2 (SRC-1093), as transcribed in dossiers/scenario/2028-lame-duck.md, section 1. The
# transcription has FY2029, FY2030, FY2034 and the FY2029-34 total, not FY2031-33.
JCT_FOUR_DEDUCTIONS = {"fy2029": 33, "fy2030": 68, "fy2034": 73, "fy2029_34": 384}   # tips, overtime, car loans, seniors
JCT_ALL_TEN = {"fy2029": 42, "fy2030": 108, "fy2034": 166, "fy2029_34": 787}
# CBO's debt service on P.L. 119-21 over FY2025-34: $789 billion with the ten provisions made
# permanent, $718 billion as enacted (same letter, SRC-1093; 2028-lame-duck.md, "Interest").
CBO_DEBT_SERVICE_WITH, CBO_DEBT_SERVICE_ENACTED = 789, 718

# Trustees' 2026 intermediate figures, as funds-model.py prints them beside its own (lines 306, 335)
TRUSTEES_OASDI = {"depletion": 2034, "payable": 83, "balance": -4.42}
TRUSTEES_HI = {"depletion": 2033, "payable": 89, "balance": -0.56}

# Leads only, not targets: the "ROT" table in Espen's old CBO scorer (SRC-0203,
# library/intake/2026-10-28/old-sessions/Claude built CBO scorer tool/cbo-scorer.jsx, line 33),
# labeled "per 0.1 pp change, 2026-2035, from CBO workbook". The workbook is not in the library,
# so these numbers are shown for orientation and no benchmark passes or fails on them.
LEAD_ROT = {
    "interest_net_interest_per_0.1pt": [13.34, 18.69, 23.74, 28.61, 33.52, 38.08, 42.90, 47.43, 52.25, 56.95],
    "productivity_deficit_per_0.1pt": [-8.53, -13.98, -19.52, -25.84, -32.50, -39.80, -47.81, -56.59, -66.30, -77.19],
    "labor_force_deficit_per_0.1pt": [-4.06, -6.57, -9.21, -12.02, -15.09, -18.55, -22.57, -27.09, -31.85, -37.45],
}

UPLOADS = [
    ("CBO's rules-of-thumb workbook for the February 2026 baseline: how deficits change if interest "
     "rates, productivity growth or labor-force growth differ from CBO's projections (released with "
     "*The Budget and Economic Outlook: 2026 to 2036*, on cbo.gov's budget and economic data page)",
     "SE-1, SE-2: turns the sensitivity benchmarks from pending into pass or fail. SRC-0203's numbers "
     "say they came from this workbook; they can't be checked without it."),
    ("CBO's letter of August 4, 2025 to Senator Merkley, *Effects on Deficits and the Debt of Public "
     "Law 119-21 and of Making Certain Tax Policies in the Act Permanent* (publication 61466, the PDF "
     "with Table 2)",
     "PS-1, PS-2: the full FY2025-34 annual figures. The repository records only FY2029, FY2030, "
     "FY2034 and the totals, so PS-2 assumes FY2031-33 are equal (SRC-1093 is a citation row, not a saved copy)."),
    ("A CBO cost estimate for a recent full-year appropriations act, with budget authority and "
     "estimated outlays by year (for example, the act of November 2025 that ended the shutdown and "
     "carried three full-year FY2026 bills, or any later full-year FY2026 act)",
     "PS-4: a published appropriations score for the spend-out method, account by account."),
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
    tot = JCT_FOUR_DEDUCTIONS["fy2029_34"] - JCT_FOUR_DEDUCTIONS["fy2029"]          # FY2030-34
    scale = tot / sum(path[y] for y in window)
    got30, got34 = path[2030] * scale, path[2034] * scale
    m30 = got30 / JCT_FOUR_DEDUCTIONS["fy2030"] - 1
    m34 = got34 / JCT_FOUR_DEDUCTIONS["fy2034"] - 1
    worst = max(abs(m30), abs(m34))
    cpi = P.profile_path(PB, 1.0, dict(prof, grow="cpi"))
    cs = tot / sum(cpi[y] for y in window)
    out.append(_bm("PS-1", "Published scores", "JCT: extending P.L. 119-21's four household deductions; the library's timing of a permanent revenue provision",
                   "pass" if worst <= 0.05 else "fail", "FY2030 %.1f, FY2034 %.1f" % (got30, got34),
                   "FY2030 %d, FY2034 %d" % (JCT_FOUR_DEDUCTIONS["fy2030"], JCT_FOUR_DEDUCTIONS["fy2034"]),
                   "5% in each year", "JCT estimates in CBO's letter of August 4, 2025, Table 2 (SRC-1093), as transcribed in dossiers/scenario/2028-lame-duck.md, section 1",
                   "The library doesn't estimate how much a provision costs: it takes a ten-year total and spreads it over the years. So the test "
                   "of the library is the spreading. The FY2030-34 total JCT gives ($%d billion) goes in; the library's method (provisions.profile_path) "
                   "with the project's default spec for a revenue row (full from the start, growing with individual income tax receipts, "
                   "permanent: ASM-PROF-REVENUE) puts out the yearly amounts. Five percent allows for JCT's rounding to the billion and "
                   "the different baseline (January 2025). Over a five-year window it can't tell growth rates apart by less than about two "
                   "points a year, so the growth gap below is reported as a finding, not tested." % tot,
                   unit="$B", miss="%+.1f%% in FY2030, %+.1f%% in FY2034" % (100 * m30, 100 * m34) if worst > 0.05 else None,
                   detail=["JCT's amounts grow about %.1f%% a year, FY2030-34; the default spec grows %.1f%% a year, the speed of individual income tax receipts. "
                           "A likely reason: the deductions are fixed dollar amounts ($25,000 of tips, $12,500 of overtime, $10,000 of car-loan "
                           "interest, $6,000 for each senior), so their cost would grow more slowly than the tax base; whether the statute indexes "
                           "them was not checked here. For a provision like this the default spec front-loads too little and back-loads too much." % (
                               100 * ((JCT_FOUR_DEDUCTIONS["fy2034"] / JCT_FOUR_DEDUCTIONS["fy2030"]) ** 0.25 - 1),
                               100 * ((path[2034] / path[2030]) ** 0.25 - 1)),
                           "For comparison only (not the test): the same spec growing with CPI-U gives FY2030 %.1f and FY2034 %.1f." % (cpi[2030] * cs, cpi[2034] * cs),
                           "Only four of JCT's ten years are recorded in the repository (see uploads)."]))
    # PS-2: debt service on the ten-provision extension
    fy3133 = (JCT_ALL_TEN["fy2029_34"] - JCT_ALL_TEN["fy2029"] - JCT_ALL_TEN["fy2030"] - JCT_ALL_TEN["fy2034"]) / 3
    prim = {2029: JCT_ALL_TEN["fy2029"], 2030: JCT_ALL_TEN["fy2030"], 2031: fy3133, 2032: fy3133, 2033: fy3133, 2034: JCT_ALL_TEN["fy2034"]}
    I, _ = FM.debt_roll(B, prim, 0.0)
    got = sum(I[y] for y in range(2025, 2035) if y in I)
    want = CBO_DEBT_SERVICE_WITH - CBO_DEBT_SERVICE_ENACTED
    miss = got / want - 1
    out.append(_bm("PS-2", "Published scores", "CBO: interest cost of extending P.L. 119-21's ten temporary provisions, FY2025-34",
                   "pass" if abs(miss) <= 0.15 else "fail", round(got, 1), want, "15%",
                   "CBO's letter of August 4, 2025 (SRC-1093): debt service $789 billion with the extension, $718 billion without; JCT's Table 2 for the deficits",
                   "Tests the model's interest method (fiscal-model.py, debt_roll: market rates on new borrowing, half a year of interest on "
                   "each year's new deficit) against CBO's own debt-service estimate for the same deficits. JCT's deficits go in; the model's "
                   "interest comes out. Fifteen percent allows for two known differences: CBO used its January 2025 interest rates and the "
                   "model uses February 2026's, and FY2031-33 are not recorded, so they are set equal (%.0f billion each, which matches JCT's total). "
                   "The tolerance was chosen in this PR; the reviewer should say if it is too loose." % fy3133,
                   unit="$B", miss="%+.0f%%" % (100 * miss) if abs(miss) > 0.15 else None,
                   detail=["Model interest by year: " + ", ".join("FY%d %.1f" % (y, I[y]) for y in range(2029, 2035)) + ".",
                           "The model is %+.0f%% from CBO. A higher figure is the cautious direction: the model's rate on new borrowing is at least the market blend." % (100 * miss)]))
    # PS-3: discretionary spend-out against CBO's projected outlays
    for grp, ba_cat, out_cat in (("defense", "ba_disc_defense", "out_disc_defense"), ("nondefense", "ba_disc_nondefense", "out_disc_nondefense")):
        ba, cbo_out = D.cbo_series(ba_cat), D.cbo_series(out_cat)
        got = P.spendout_apply(ba, grp)
        yrs = range(2028, 2037)
        gaps = {y: got[y] / cbo_out[y] - 1 for y in yrs}
        wy = max(gaps, key=lambda y: abs(gaps[y]))
        tot_gap = sum(got[y] for y in yrs) / sum(cbo_out[y] for y in yrs) - 1
        why = ("Tests B3's spend-out method (provisions.spendout_apply, on B2's estimated shares, ASM-SPENDOUT) against CBO's own "
               "conversion of budget authority into outlays: CBO's projected discretionary %s budget authority, FY2025-36, goes in; "
               "outlays FY2028-36 come out (the first three years need budget authority from before FY2025, so they are left out). "
               "Five percent in each year is about twice B2's fit error (%s of mean outlays), so it allows for the fit and would catch a wrong rate." %
               (grp, "2.2%" if grp == "defense" else "3.6%"))
        det = ["Over FY2028-36 the method gives %+.1f%% of CBO's total. Largest year FY%d: %.0f against CBO's %.0f billion." % (100 * tot_gap, wy, got[wy], cbo_out[wy])]
        if grp == "nondefense":
            det.append("A known cause, from B2's README (\"Spend-out\"): nondefense discretionary outlays include highway and transit spending "
                       "whose budget authority is mandatory contract authority, so it is not in the discretionary budget authority that goes in. "
                       "B3 also rescales the nondefense shares, which add to 1.10, down to one.")
        out.append(_bm("PS-3" + ("a" if grp == "defense" else "b"), "Published scores",
                       "CBO: discretionary %s outlays from budget authority (February 2026 baseline)" % grp,
                       "pass" if abs(gaps[wy]) <= 0.05 else "fail", "%+.1f%%" % (100 * gaps[wy]), "CBO's outlays, FY2028-36", "5% in each year",
                       "CBO February 2026 ten-year baseline, discretionary budget authority and outlays (models/data/budget/cbo-ten-year.csv)", why,
                       unit="largest yearly gap", miss="%+.1f%% in FY%d" % (100 * gaps[wy], wy) if abs(gaps[wy]) > 0.05 else None, detail=det))
    out.append(_bm("PS-4", "Published scores", "CBO: cost estimate for a full-year appropriations act", "pending", None, None, "to be set with the source",
                   "Pending source: not in the library, and www.cbo.gov returns 403 to agent sessions (see uploads)",
                   "A published appropriations score, with budget authority and outlays by year and account, would test the spend-out method "
                   "on the kind of bill the plan's discretionary rows will be. Pending source."))
    return out


def bm_sensitivity(M):
    R = M["results"]
    b, r1 = R["BASE"]["years"], R["BASE-R1"]["years"]
    d, d1 = R["DEC"]["years"], R["DEC-R1"]["years"]
    extra = [r1[y]["interest"] - b[y]["interest"] for y in range(2030, 2040)]
    extra_dec = [d1[y]["interest"] - d[y]["interest"] for y in range(2030, 2040)]
    lead = [10 * v for v in LEAD_ROT["interest_net_interest_per_0.1pt"]]
    out = [_bm("SE-1", "Sensitivity", "Interest rates 1 point higher on all debt: added net interest", "pending",
               "year 1 %.0f, year 5 %.0f, year 10 %.0f; ten-year %.0f" % (extra[0], extra[4], extra[9], sum(extra)), None,
               "to be set with the source",
               "Pending source: CBO's rules of thumb for the February 2026 baseline (not in the library; see uploads)",
               "The model's BASE-R1 case raises the rate on all debt by one point from FY2030. CBO's rule of thumb raises all rates by a "
               "tenth of a point (scaled here by ten) from the first projection year. Until CBO's workbook is in the library there is no "
               "target, so the result is shown without a pass or fail.", unit="$B",
               detail=["Model, baseline (FY2030-39, years 1-10 of the shock): " + ", ".join("%.0f" % v for v in extra) + ".",
                       "Model, decided program (DEC-R1 less DEC): year 1 %.0f, year 10 %.0f, ten-year %.0f." % (extra_dec[0], extra_dec[9], sum(extra_dec)),
                       "Lead only, not a target (SRC-0203, ten times its per-0.1-point figures for FY2026-35): " + ", ".join("%.0f" % v for v in lead) +
                       "; ten-year %.0f." % sum(lead),
                       "What the comparison already suggests: the model reprices all debt at once (fiscal-model.py, baseline(): the shift applies to "
                       "last year's whole debt), so its year-1 effect is a full point on about $%.1f trillion. CBO's rules of thumb phase the higher "
                       "rate in as debt matures and is refinanced. If the workbook confirms that, the model overstates the early effect, which is "
                       "the cautious direction for the plan's stress case (CONVENTIONS.md, choice 4)." % (b[2029]["debt"] / 1000)])]
    out.append(_bm("SE-2", "Sensitivity", "Slower growth (productivity or labor force 0.1 point a year lower): added deficits", "pending",
                   None, None, "to be set with the source",
                   "Pending source and a model capability: CBO's rules of thumb (not in the library; see uploads)",
                   "The model takes CBO's baseline revenue and spending as given in dollars. It has no way to slow the economy, so it has no "
                   "response to compare. Only program rows indexed to GDP would move. Building one is for B6 or later, and needs CBO's rules "
                   "of thumb to calibrate.",
                   detail=["Lead only, not a target (SRC-0203, per 0.1 point, FY2026-35 ten-year sum; its table lowers deficits, read here as faster growth, "
                           "so slower growth would raise them by about as much): productivity %.0f, labor force %.0f billion of added deficit." % (
                       -sum(LEAD_ROT["productivity_deficit_per_0.1pt"]), -sum(LEAD_ROT["labor_force_deficit_per_0.1pt"]))]))
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
                                "the reading to use (legacy/index/dedicated-funds.md, Medicare HI)."] if id == "TF-2" else [])))
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
        lines.append("| %s | %s | **%s** | %s%s | %s | %s | %s |" % (
            r["id"], r["name"], r["status"], _fmt(r["value"]), (" (%s)" % r["unit"]) if r["unit"] and r["value"] is not None else "",
            _fmt(r["target"]), r["tolerance"], r["miss"] or "—"))
    return "\n".join(lines)


def counts_line(results):
    c = _counts(results)
    return "%d benchmarks: %s." % (len(results), ", ".join("%d %s" % (c[k], k) for k in ("pass", "fail", "pending", "info") if c.get(k)))


def page(results):
    w = ["# Budget model benchmarks: results",
         "",
         "Role: the current result of every benchmark of the federal budget model (piece B4 of `models/tools/budget/WORKFLOW.md`, PR #104 until it merges). "
         "Status: generated by `models/tools/budget/test_benchmarks.py` on every run of `models/tools/run-all.sh`; do not edit by hand. "
         "The same results are in `benchmarks.json` for other tools. What the benchmarks mean, and the model's limits, are in `MODEL-CARD.md`.",
         "",
         "**How to read it.** *pass*: within the stated tolerance. *fail*: outside it; the miss column gives the size. *pending*: there is "
         "no target yet, because the source isn't in the library or the model can't compute the quantity. A miss is reported, never fixed "
         "by changing the model or the tolerance.",
         "",
         counts_line(results),
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
          "www.cbo.gov refuses agent sessions (403), so these come in as uploads (`library/fetch_public.py --file`).", ""]
    w += ["%d. %s. *Unlocks:* %s" % (i + 1, d, u) for i, (d, u) in enumerate(UPLOADS)]
    return "\n".join(w) + "\n"


def data_json(results):
    return json.dumps({"role": "Budget model benchmark results (B4), generated by models/tools/budget/test_benchmarks.py; do not edit by hand.",
                       "counts": _counts(results), "benchmarks": results,
                       "uploads": [{"document": d, "unlocks": u} for d, u in UPLOADS]}, indent=1, sort_keys=False, default=float) + "\n"


def card(results, facts, template):
    a, b = template.index(CARD_START) + len(CARD_START), template.index(CARD_END)
    u, mo = facts["unknown"], facts["model_only"]
    block = ["", "*This block is generated by `test_benchmarks.py` from the latest run; the rest of the card is written by hand.*", "",
             counts_line(results), "",
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

    def test_leads_are_not_targets(self):
        for r in RESULTS:
            if r["group"] == "Sensitivity":
                self.assertIsNone(r["target"], r["id"] + ": SRC-0203's numbers are leads, not targets")


if __name__ == "__main__":
    unittest.main()
