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


# ---- 2025 as enacted -------------------------------------------------------------------------------------------
LAW_2025 = {
    "year": 2025,
    # sec. 1(j) brackets: upper edges of the 10, 12, 22, 24, 32 and 35% brackets (Rev. Proc. 2024-40, sec. 3.01)
    "rates": [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
    "brackets": {"joint": [23850, 96950, 206700, 394600, 501050, 751600],
                 "single": [11925, 48475, 103350, 197300, 250525, 626350],
                 "hoh": [17000, 64850, 103350, 197300, 250500, 626350]},
    # capital gains and qualified dividends: top of the 0% and 15% bands (sec. 1(h), 1(j)(5))
    "cg_brackets": {"joint": [96700, 600050], "single": [48350, 533400], "hoh": [64750, 566700]},
    # standard deduction (sec. 63(c)(7) as amended by P.L. 119-21 sec. 70102) and the additional amount at 65
    "std": {"joint": 31500, "single": 15750, "hoh": 23625},
    "std_aged": {"joint": 1600, "single": 2000, "hoh": 2000},
    # P.L. 119-21 sec. 70103: $6,000 a person 65 or older, 2025-2028, phased out at 6% of MAGI above $75,000/$150,000
    "senior_deduction": 6000, "senior_phaseout": {"joint": 150000, "single": 75000, "hoh": 75000},
    # child tax credit (sec. 24 as amended by P.L. 119-21 sec. 70104)
    "ctc": 2200, "ctc_refundable": 1700, "ctc_odc": 500, "ctc_earn_floor": 2500, "ctc_refund_rate": 0.15,
    "ctc_phaseout": {"joint": 400000, "single": 200000, "hoh": 200000}, "ctc_phaseout_rate": 0.05,
    # earned income credit (sec. 32; Rev. Proc. 2024-40 sec. 3.07): by number of qualifying children 0, 1, 2, 3+
    "eitc_rate": [0.0765, 0.34, 0.40, 0.45], "eitc_po_rate": [0.0765, 0.1598, 0.2106, 0.2106],
    "eitc_earned": [8490, 12730, 17880, 17880],
    "eitc_po_start": {"joint": [17730, 30470, 30470, 30470], "single": [10620, 23350, 23350, 23350]},
    "eitc_invest_limit": 11950, "eitc_childless_ages": (25, 64),
    # payroll taxes (secs. 3101, 3111, 1401, 1411); the wage base is SSA's for 2025
    "ss_rate": 0.062, "hi_rate": 0.0145, "ss_wage_base": 176100,
    "addl_hi_rate": 0.009, "addl_hi_threshold": {"joint": 250000, "single": 200000, "hoh": 200000},
    "niit_rate": 0.038, "niit_threshold": {"joint": 250000, "single": 200000, "hoh": 200000},
    # taxable Social Security (sec. 86): base and adjusted base amounts, not indexed
    "ss_base": {"joint": 32000, "single": 25000, "hoh": 25000},
    "ss_adj_base": {"joint": 44000, "single": 34000, "hoh": 34000},
    # HHS poverty guideline, 48 states (90 FR 5917): one person and each additional person
    "fpl": (15650, 5500),
    # SNAP, FY2025 (USDA FNS cost-of-living adjustment, October 2024): maximum allotment by household size 1-8,
    # standard deduction by size (1-3, 4, 5, 6+), the 20% earned income deduction, the 30% benefit reduction rate,
    # the excess shelter deduction's cap for households without an elderly or disabled member, gross test 130%
    "snap_max": [292, 536, 768, 975, 1158, 1390, 1536, 1756], "snap_std": [204, 204, 204, 217, 254, 291],
    "snap_earn_ded": 0.20, "snap_brr": 0.30, "snap_shelter_cap": 712, "snap_gross_test": 1.30,
    "snap_min_benefit": 23,
}


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
