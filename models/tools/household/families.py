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
from rules import afa_child_benefit, childless_eitc_2021

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


def budget(f, earnings, year=2029, bbce=False, shelter=0.0, marketplace=False, plan=False):
    L = law(year)
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
