"""Typical families: the cents lost from each added dollar of earnings, layer by layer, at 2029 law.

Role: the household model's family-type calculator, the baseline for the secure floor's 65-cent ceiling (INC-5.02,
shared rule 2) (`MODEL-CARD.md`, "Typical families"). Status: working for current law; the plan's layers are a preview
until part 2 checks them against the dossier's specification.

The three family types INC-5.02 names: a single parent with two children (ages 4 and 8), a married couple with two
children (one earner), and a single adult (age 30). Earnings are wages; there is no other income. At each point the
marginal rate is 1 minus the change in net resources over a $1,000 raise, split by layer:
  * payroll: the employee's 7.65% (the employer's half is not in the family's budget);
  * income tax after credits: the regular tax, the child credit (with its refundable part) and the earned income
    credit, from `tax.py`;
  * SNAP, on federal rules: gross income 130% of poverty (or a state's broad-based categorical eligibility, up to
    200%), the 20% earnings deduction, the standard deduction, an optional excess shelter deduction, 30% of net
    income;
  * the premium tax credit, for families buying marketplace coverage (2029 law: the 2010 act's schedule, 100% to
    400% of poverty; the 2026 applicable percentages, Rev. Proc. 2025-25, held for 2029, assumption A-9).
Medicaid and CHIP are cliffs, not rates, and are listed apart. Housing's 30% rent rule is outside the ceiling.
"""
from params import law
from tax import unit_tax
from rules import afa_child_benefit, cdctc_rate, childless_eitc_2021, guarantee_charge

FAMILIES = {
    "single_parent_2": {"label": "Single parent, two children", "fs_code": 4, "age_h": 32, "age_s": -1,
                        "kids_u6": 1, "kids_6_16": 1, "size": 3},
    "married_2": {"label": "Married couple, two children (one earner)", "fs_code": 1, "age_h": 35, "age_s": 35,
                  "kids_u6": 1, "kids_6_16": 1, "size": 4},
    "single_adult": {"label": "Single adult", "fs_code": 5, "age_h": 30, "age_s": -1, "kids_u6": 0, "kids_6_16": 0,
                     "size": 1},
}
# Premium credit: applicable percentage at the edges of each band of income as a share of poverty (2026 figures)
PTC_BANDS = [(1.00, 2.10, 2.10), (1.33, 3.14, 4.19), (1.50, 4.19, 6.60), (2.00, 6.60, 8.44), (2.50, 8.44, 9.96),
             (3.00, 9.96, 9.96), (4.00, None, None)]


def fpl(L, size):
    return L["fpl"][0] + L["fpl"][1] * (size - 1)


def unit(f, earnings):
    z = {k: 0 for k in ("se_h", "se_s", "interest", "dividends", "rent", "capgain", "pension", "ss", "ssi", "tanf",
                        "uc", "vet", "disab_surv", "other", "child_support_rcvd", "dep_wages", "dep_other_income",
                        "n_dep_17", "n_dep_18", "n_dep_19_23_student", "n_dep_other")}
    z.update({"filestat": f["fs_code"], "age_h": f["age_h"], "age_s": f["age_s"], "wage_h": earnings, "wage_s": 0,
              "n_dep_u6": f["kids_u6"], "n_dep_6_16": f["kids_6_16"], "n_dep": f["kids_u6"] + f["kids_6_16"]})
    return z


def snap(L, f, earnings, bbce=False, shelter=0.0, other_income=0.0):
    """Annual SNAP benefit (federal rules, the 48 states). `shelter` is monthly rent and utilities."""
    n = f["size"]
    gross = (earnings + other_income) / 12
    line = fpl(L, n) / 12
    if gross > (2.0 if bbce else L["snap_gross_test"]) * line:
        return 0.0
    std = L["snap_std"][min(max(n - 3, 0), 3)] if n >= 4 else L["snap_std"][0]
    adj = gross - L["snap_earn_ded"] * earnings / 12 - std
    excess = min(max(shelter - 0.5 * adj, 0), L["snap_shelter_cap"]) if shelter else 0.0
    net = max(adj - excess, 0)
    if not bbce and net > line:
        return 0.0
    ben = L["snap_max"][n - 1] - L["snap_brr"] * net
    if ben <= 0:
        return 0.0
    if n <= 2:
        ben = max(ben, L["snap_min_benefit"])
    return 12 * ben


def ptc_contribution(L, f, income):
    """The family's required contribution for the benchmark plan (dollars a year); None outside 100-400%."""
    x = income / fpl(L, f["size"])
    if x < 1.0 or x > 4.0:
        return None
    for (lo, a, b), (hi, _, _) in zip(PTC_BANDS, PTC_BANDS[1:]):
        if lo <= x < hi or (x == 4.0 and hi == 4.0):
            pct = a + (b - a) * (x - lo) / (hi - lo)
            return pct / 100 * income
    return None


def budget(f, earnings, year=2029, bbce=False, shelter=0.0, marketplace=False, plan=False, snap_earn_ded=None):
    L = law(year)
    if snap_earn_ded is not None:
        L = dict(L, snap_earn_ded=snap_earn_ded)
    u = unit(f, earnings)
    t = unit_tax(u, L)
    income_tax = t["income_tax"]
    if plan:
        # preview of two plan layers: FAM-1's child benefit in place of section 24, and INC-1.01's childless credit
        u.update({"t_" + k: v for k, v in t.items()})
        income_tax -= afa_child_benefit(u, L)
        if not (f["kids_u6"] + f["kids_6_16"]):
            income_tax += t["eitc"] - childless_eitc_2021(L, earnings, t["agi"], t["fs"], [f["age_h"]])
    payroll = t["fica_ee"]
    s = snap(L, f, earnings, bbce, shelter)
    contrib = ptc_contribution(L, f, t["agi"]) if marketplace else None
    return {"earnings": earnings, "payroll": payroll, "income_tax": income_tax, "snap": s,
            "ptc_contribution": contrib or 0.0, "ptc_eligible": contrib is not None,
            "net": earnings - payroll - income_tax + s - (contrib or 0.0)}


def marginal_rates(f, year=2029, points=(0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0), step=1000, **kw):
    L = law(year)
    out = []
    for p in points:
        e = p * fpl(L, f["size"])
        a, b = budget(f, e, year, **kw), budget(f, e + step, year, **kw)
        layer = {k: 100 * (b[k] - a[k]) / step for k in ("payroll", "income_tax")}
        layer["snap"] = -100 * (b["snap"] - a["snap"]) / step
        layer["ptc"] = 100 * (b["ptc_contribution"] - a["ptc_contribution"]) / step
        out.append({"pct_poverty": round(100 * p), "earnings": round(e), **{k: round(v, 1) for k, v in layer.items()},
                    "total": round(100 * (1 - (b["net"] - a["net"]) / step), 1)})
    return out


def cliffs(year=2029):
    """Where help ends at a line instead of phasing out (shares of poverty)."""
    return [("Medicaid for adults in expansion states", "138%"), ("SNAP's gross income test, without the broad option", "130%"),
            ("The premium tax credit", "400%"), ("CHIP and Medicaid for children", "state lines, usually 200-300%")]


# ---- The 65-cent ceiling check (INC-5.02, shared rule 2): every plan layer -------------------------------------------
# The plan's layers on a typical family's added dollar, from the dossiers' decided designs:
#   * payroll: the employee's 7.65%, plus paid leave's worker share (FAM-3.04: 0.3% from 2030, up to 0.55% at the
#     1.10% ceiling);
#   * income tax: 2029 law, with FAM-1's child benefit in place of section 24 (`rules.afa_child_benefit`) and, for the
#     single adult, INC-1.01's childless credit; INC-1.02 changes nothing for these families;
#   * SNAP on federal rules: INC-2 restores the rules before P.L. 119-21, which for these families' rates are the
#     rules `snap` already applies, and INC-2.02 raises the earned income deduction from 20% to 45% (Espen's option D,
#     DEC-2026-11-13-03; `PLAN_SNAP_EARN_DED`); INC-5.01 keeps the child benefit out of SNAP's income; with and
#     without the excess shelter deduction;
#   * the premium tax credit, for a family on the marketplace, in 2030-34 only: the single plan (HLT-7) ends it from
#     2035 and charges no premium; its copays start at 200% of poverty (HLT-7.06), a line, listed with the cliffs;
#   * child care's charge (FAM-2.01, full from July 2032) for the child under 5, net of INC-4's refundable credit on the
#     charge: free at or below 85% of state median income, rising to 7% of income at 150%. Where that line falls
#     depends on the state; the check uses the lowest state median income the CPS gives (`low_smi4`), where the charge
#     reaches furthest down. In a typical state the charge starts above 300% of poverty for these families.
# Housing's 30% rent rule is outside the ceiling (INC-5.02).
CEILING = 65.0
CEILING_POINTS = tuple(x / 100 for x in range(50, 301, 25))
LEAVE_WORKER = (0.003, 0.0055)          # FAM-3.04: half of 0.6% at the start, half of the 1.10% ceiling
PLAN_SNAP_EARN_DED = 0.45               # INC-2.02: 7 U.S.C. 2014(e)(2)'s 20% to 45% (DEC-2026-11-13-03)
# FAM-2.01's charge and section 21's rate have one home, `rules.py` (INC-4's rule uses them too)
care_charge = guarantee_charge
care_credit_rate = cdctc_rate


def plan_budget(f, earnings, period="2035", shelter=0.0, marketplace=False, smi4=None, leave=LEAVE_WORKER[0],
                snap_earn_ded=PLAN_SNAP_EARN_DED):
    """A family's budget under every plan layer (above). `period` is "2030-34" (the premium credit still runs) or
    "2035" (the single plan); `smi4` the state median income for four (None: no paid care for the child under 5);
    `snap_earn_ded` SNAP's earned income deduction (INC-2.02's 45%; 0.20 gives the set before DEC-2026-11-13-03)."""
    L = law(2029)
    b = budget(f, earnings, 2029, shelter=shelter, marketplace=marketplace and period == "2030-34", plan=True,
               snap_earn_ded=snap_earn_ded)
    t = unit_tax(unit(f, earnings), L)
    b["payroll"] += leave * earnings
    charge = 0.0
    if smi4 and f["kids_u6"]:
        gross = care_charge(t["agi"], f["size"], smi4)
        charge = gross - care_credit_rate(t["agi"], t["fs"]) * min(gross, 3000)
    b["care"] = charge
    b["net"] = earnings - b["payroll"] - b["income_tax"] + b["snap"] - b["ptc_contribution"] - charge
    return b


def plan_rates(f, step=1000, points=CEILING_POINTS, **kw):
    L = law(2029)
    out = []
    for p in points:
        e = p * fpl(L, f["size"])
        a, b = plan_budget(f, e, **kw), plan_budget(f, e + step, **kw)
        r = {k: round(100 * (b[k] - a[k]) / step, 1) for k in ("payroll", "income_tax", "care")}
        r["snap"] = round(-100 * (b["snap"] - a["snap"]) / step, 1)
        r["ptc"] = round(100 * (b["ptc_contribution"] - a["ptc_contribution"]) / step, 1)
        out.append({"pct_poverty": round(100 * p), "earnings": round(e), **r,
                    "total": round(100 * (1 - (b["net"] - a["net"]) / step), 1)})
    return out


CEILING_CASES = [
    ("2035 on, no shelter deduction", {"period": "2035"}),
    ("2035 on, with a $1,400 rent in SNAP's shelter deduction", {"period": "2035", "shelter": 1400 * 1.107}),
    ("2030-34 on the marketplace, no shelter deduction", {"period": "2030-34", "marketplace": True}),
    ("2030-34 on the marketplace, with the rent", {"period": "2030-34", "marketplace": True, "shelter": 1400 * 1.107}),
]


def ceiling_check(low_smi4, mid_smi4, snap_earn_ded=PLAN_SNAP_EARN_DED):
    """INC-5.02's test for each family and case: the highest combined rate at 50-300% of poverty, where it falls, and
    whether it is at or below 65 cents. A step that crosses a line (a figure above 100, or a fall in SNAP to zero) is a
    cliff, reported apart, not a rate. `snap_earn_ded=0.20` gives the decided set before INC-2.02."""
    res = {}
    for k, f in FAMILIES.items():
        res[k] = {}
        for label, kw in CEILING_CASES:
            for smi_label, smi in (("lowest-income state", low_smi4), ("typical state", mid_smi4)):
                rows = plan_rates(f, smi4=smi, snap_earn_ded=snap_earn_ded, **kw)
                rates_ = [r for r in rows if r["total"] <= 100]
                cliffs = [r["pct_poverty"] for r in rows if r["total"] > 100]
                top = max(rates_, key=lambda r: r["total"])
                res[k][f"{label} | {smi_label}"] = {
                    "rows": rows, "max": top["total"], "at": top["pct_poverty"], "cliffs": cliffs,
                    "over": [r["pct_poverty"] for r in rates_ if r["total"] > CEILING], "pass": top["total"] <= CEILING}
            # paid leave at its 1.10% ceiling, the lowest-income state
            rows = plan_rates(f, smi4=low_smi4, leave=LEAVE_WORKER[1], snap_earn_ded=snap_earn_ded, **kw)
            top = max((r for r in rows if r["total"] <= 100), key=lambda r: r["total"])
            res[k][f"{label} | leave at its ceiling"] = {"max": top["total"], "at": top["pct_poverty"],
                                                         "pass": top["total"] <= CEILING}
    return res
