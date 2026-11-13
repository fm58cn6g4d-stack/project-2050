"""Provision rules the household model computes household by household, for incidence keys and poverty effects.

Role: the household model's rule-based provisions (`MODEL-CARD.md`, "Provision interface"). Status: working for the
two rules below; the secure floor's INC-1 to INC-5 join in part 2.

Each rule takes a baseline tax unit (with its `t_` tax fields) and the baseline law, and returns the unit's change in
resources from the provision, in dollars a year (positive is a gain). They are static: no behavior, full take-up of
new benefits.
"""
from params import econ


def afa_child_benefit(u, L):
    """FAM-1 (the decided child benefit, FAM-1D, `DEC-2026-11-12-06`): the American Family Act's credit (H.R. 2763
    sec. 24A) in place of section 24, at annual exposure, as `dossiers/secure-floor/tools/afa_floor.py` prices it:
    $300 a month (6-17) and $360 (under 6), indexed from 2024 in $10 steps; 5% phase-outs above $150,000 joint or
    $112,500 other (indexed from 2022 in $5,000 steps) down to $166.67 a month a child, and again above $400,000 joint or
    $300,000 other. No earnings requirement; the newborn month is left out. The credit for other dependents ends with
    section 24 (`DEC-2026-11-12-09`)."""
    kids_u6 = u["n_dep_u6"]
    kids = kids_u6 + u["n_dep_6_16"] + u["n_dep_17"]
    y = L["year"]
    i24 = econ("cpiu", y - 1) / econ("cpiu", 2024)
    i22 = econ("cpiu", y - 1) / econ("cpiu", 2024) * 313.689 / 292.655   # BLS CPI-U annual 2024 over 2022
    monthly = 300 + round(300 * (i24 - 1) / 10) * 10
    gross = 12 * monthly * (kids - kids_u6) + 12 * monthly * 1.2 * kids_u6
    joint = u["t_fs"] == "joint"
    first = 150000 if joint else 112500
    first += round(first * (i22 - 1) / 5000) * 5000
    second = 400000 if joint else 300000
    agi = u["t_agi"]
    floor = 12 * 166.67 * kids
    cut = min(max(gross - floor, 0), 0.05 * max(second - first, 0), 0.05 * max(agi - first, 0))
    afa = max(gross - cut - 0.05 * max(agi - second, 0), 0)
    return afa - u["t_ctc_total"]


def surtax_100k(u, L):
    """C20, the 1-point surtax on income above $100,000 ($200,000 joint), on AGI (a loss, so negative)."""
    line = 200000 if u["t_fs"] == "joint" else 100000
    return -0.01 * max(u["t_agi"] - line, 0)


RULES = {"afa_child_benefit": afa_child_benefit, "surtax_100k": surtax_100k}
