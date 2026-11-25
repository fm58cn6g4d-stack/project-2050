"""Federal tax and benefit rules for the household model, for the source year (2025) and the baseline year (2029).

Role: the household model's law parameters and uprating factors (`MODEL-CARD.md`, "Rules modeled"). Status: working.

2025 is the law as enacted: the 2017 act's rates and brackets made permanent, and the 2025 reconciliation act's
standard deduction, child credit and temporary deductions (P.L. 119-21, "OBBBA"), with the IRS's 2025 inflation
figures (Rev. Proc. 2024-40, as amended by P.L. 119-21). 2029 is current law as it will stand: the same permanent
structure indexed to 2029, and the act's 2025-2028 deductions (the $6,000 senior deduction, tips, overtime, car-loan
interest) expired. Indexing follows the code's method in outline (chained CPI-U for the twelve months ending August of
the prior year, against the base year): CBO's February 2026 fiscal-year chained CPI-U for FY2028 over FY2024 stands in
for those twelve-month averages (labeled assumption, `MODEL-CARD.md` A-3). Rounding follows the code's step for each
amount (sec. 1(f)(7), 24(i), 32(j)(2)).
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CBO = os.path.join(HERE, "..", "..", "data", "cbo", "economic_economic_projections_fiscal_2026-02.csv")


def _cbo():
    out = {}
    with open(CBO) as f:
        for r in csv.DictReader(f):
            out[(int(r["date"]), r["variable"])] = float(r["value"])
    return out


ECON = _cbo()


def econ(var, year):
    return ECON[(year, var)]


def index_factor(year):
    """Tax-year indexing from 2025 values: C-CPI-U for the year ending August of year-1 over that ending August 2024."""
    return econ("chained_cpiu", year - 1) / econ("chained_cpiu", 2024)


def rdown(x, step):
    return int(x // step) * step


# ---- 2025 as enacted: read from parameters.csv (the toolkit's parameter schema, models/schema/README.md) -----------
PARAMETERS = os.path.join(HERE, "parameters.csv")


def _read_parameters():
    with open(PARAMETERS, newline="") as f:
        return list(csv.DictReader(f))


PARAM_ROWS = _read_parameters()
VALUES = {r["id"]: r for r in PARAM_ROWS}


def _number(s):
    x = float(s)
    return int(x) if x == int(x) and "." not in s and "e" not in s.lower() else x


def constant(pid):
    """One input of the parameter file by its id (a number)."""
    return _number(VALUES[pid]["value"])


def _build_law_2025():
    """Rebuild the law dictionary from the 'law' rows. An id is a key and then the path to the value: an integer is a
    1-based position in a list, a word a key of a dictionary (`brackets.joint.1`, `std.hoh`, `ctc`)."""
    out = {"year": 2025}
    for r in PARAM_ROWS:
        if r["group"] != "law":
            continue
        key, *path = r["id"].split(".")
        node, slot = out, key
        for p in path:
            if p.isdigit():
                if not isinstance(node.get(slot), list):
                    node[slot] = []
                node, slot = node[slot], int(p) - 1
                while len(node) <= slot:
                    node.append(None)
            else:
                if not isinstance(node.get(slot), dict):
                    node[slot] = {}
                node, slot = node[slot], p
        node[slot] = _number(r["value"])
    for k in ("eitc_childless_ages", "fpl"):
        out[k] = tuple(out[k])
    return out


LAW_2025 = _build_law_2025()


def law(year):
    """Current law for a tax year. 2025 as enacted; later years indexed from 2025 with the temporary items expired."""
    if year == 2025:
        return LAW_2025
    f = index_factor(year)
    L = {k: v for k, v in LAW_2025.items()}
    L["year"] = year
    L["brackets"] = {fs: [rdown(b * f, 50 if fs == "joint" else 25) for b in bs] for fs, bs in LAW_2025["brackets"].items()}
    L["cg_brackets"] = {fs: [rdown(b * f, 50 if fs == "joint" else 25) for b in bs] for fs, bs in LAW_2025["cg_brackets"].items()}
    L["std"] = {fs: rdown(v * f, 50) for fs, v in LAW_2025["std"].items()}
    L["std_aged"] = {fs: rdown(v * f, 50) for fs, v in LAW_2025["std_aged"].items()}
    L["senior_deduction"] = 6000 if year <= 2028 else 0          # P.L. 119-21 sec. 70103: tax years 2025-2028
    L["ctc"] = rdown(2200 * f, 100)                                # sec. 24(i): base year 2024, $100 steps
    L["ctc_refundable"] = rdown(1700 * f, 100)
    L["eitc_earned"] = [rdown(v * f, 10) for v in LAW_2025["eitc_earned"]]
    L["eitc_po_start"] = {fs: [rdown(v * f, 10) for v in vs] for fs, vs in LAW_2025["eitc_po_start"].items()}
    L["eitc_invest_limit"] = rdown(11950 * f, 50)
    # SSA's wage base follows average wages: CBO's wages per payroll job stand in for SSA's AWI (assumption A-4)
    L["ss_wage_base"] = rdown(176100 * wage_factor(year - 2) / wage_factor(2023), 300)
    p = price_factor(year)
    L["fpl"] = (round(15650 * p, -1), round(5500 * p, -1))
    sp = econ("cpiu", year) / econ("cpiu", 2025)                  # FY to FY: SNAP's year starts in October
    L["snap_max"] = [round(v * sp) for v in LAW_2025["snap_max"]]
    L["snap_std"] = [round(v * sp) for v in LAW_2025["snap_std"]]
    L["snap_shelter_cap"] = round(712 * sp)
    L["snap_min_benefit"] = round(23 * sp)
    return L


# ---- uprating the 2025 survey year to a later year (assumption A-2) ---------------------------------------------
def price_factor(year, base=2025):
    return econ("cpiu", year) / econ("cpiu", base)


def wage_factor(year, base=2025):
    """Average wage per payroll job, CBO."""
    return (econ("wages_and_salaries", year) / econ("empl_payroll_nf", year)) / (
        econ("wages_and_salaries", base) / econ("empl_payroll_nf", base))


def per_household(var, year, base=2025):
    return (econ(var, year) / econ("households", year)) / (econ(var, base) / econ("households", base))


def uprating(year):
    """Factor for each income and expense type, 2025 to `year`, and the weight factor (households)."""
    p, w = price_factor(year), wage_factor(year)
    return {
        "weight": econ("households", year) / econ("households", 2025),
        "wages": w, "se": w, "uc": w, "dep_wages": w,
        "interest": per_household("interest_inc_pers", year),
        "dividends": per_household("dividend_inc_pers", year),
        "rent": per_household("rental_inc_adj", year),
        "capgain": per_household("gdp", year),
        "pension": p, "ss": p, "ssi": p, "vet": p, "disab_surv": p, "other": p, "child_support": p,
        "tanf": 1.0,                       # the TANF block grant is fixed in dollars
        "snap": p, "school_lunch": p, "wic": p, "energy": p, "housing": p,
        "work_childcare": p, "child_support_paid": p,
        "medical": econ("cpiu_medical_price_index", year) / econ("cpiu_medical_price_index", 2025),
        "premiums": econ("cpiu_medical_price_index", year) / econ("cpiu_medical_price_index", 2025),
        "threshold": per_household("pce", year),   # assumption A-5: SPM thresholds move with spending per household
        "state_tax": w,
    }
