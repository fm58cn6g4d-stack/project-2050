"""Provision rules the household model computes household by household, for incidence keys and poverty effects.

Role: the household model's rule-based provisions (`MODEL-CARD.md`, "Provision interface"). Status: working: FAM-1's
child benefit, C20's surtax and the secure floor's INC-1, INC-3 and INC-4 (M3 part 2). INC-2 and INC-5 need no rule:
their keys are household fields (`keys.csv`).

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


def childless_eitc_2021(L, earned, agi, fs, ages, invest=0.0):
    """INC-1.01: the 2021 childless credit (ARPA sec. 9621), indexed to prices from 2021: $1,502 maximum, 15.3% in and
    out, phase-in to $9,820, phase-out from $11,610 ($17,550 joint), from age 19 with no upper limit (the rule for
    full-time students under 24 is not applied: the CPS's head-of-unit enrollment is not in the extract). The
    investment income limit is the 2029 law's."""
    f = econ("cpiu", L["year"] - 1) / 270.970                      # BLS CPI-U annual 2021 = 270.970
    if not any(a >= 19 for a in ages) or invest > L["eitc_invest_limit"]:
        return 0.0
    earn_end, po = 9820 * f, (17550 if fs == "joint" else 11610) * f
    c = min(0.153 * earned, 0.153 * earn_end) - 0.153 * max(max(agi, earned) - po, 0)
    return max(c, 0.0)


def _earned(u):
    return u["wage_h"] + u["wage_s"] + u["se_h"] + u["se_s"]


def _invest(u):
    return u["interest"] + u["dividends"] + u["capgain"] + max(u["rent"], 0)


def eitc_kids(u):
    """The earned income credit's qualifying children in the extract: under 19, and students under 24."""
    return u["n_dep_u6"] + u["n_dep_6_16"] + u["n_dep_17"] + u["n_dep_18"] + u["n_dep_19_23_student"]


def inc1_childless_eitc(u, L):
    """INC-1 (`DEC-2026-11-12-06`, memo 3 part 1 B): INC-1.01's credit in place of today's for units with no
    qualifying child, at full take-up (a new benefit, `MODEL-CARD.md`), less the 2029 law's credit as the baseline paid
    it. INC-1.02, one qualifying-child definition, moves no money on the CPS under the reading this rule takes: the
    Census already assigns each child to one tax unit by residence, the definition's aim (`inc1_02_age_aligned` measures
    the other reading)."""
    if eitc_kids(u):
        return 0.0
    new = childless_eitc_2021(L, _earned(u), u["t_agi"], u["t_fs"], [u["age_h"], u["age_s"]], _invest(u))
    return new - u["t_eitc"]


def inc1_02_age_aligned(u, L):
    """INC-1.02's other reading, for the record, not a key: if the credit's age test were aligned to the child
    benefit's (children under 18), children 18 and students 19-23 would stop qualifying. The unit's change in its
    credit (negative is a loss); the childless credit is INC-1.01's."""
    from tax import eitc
    old = eitc_kids(u)
    new = u["n_dep_u6"] + u["n_dep_6_16"] + u["n_dep_17"]
    if old == new or u["filestat"] == 6:          # unchanged, or a nonfiler the baseline pays no credit (A-6)
        return 0.0
    ages = [u["age_h"], u["age_s"]]
    if new:
        credit = eitc(_earned(u), u["t_agi"], _invest(u), new, u["t_fs"], ages, L)
    else:
        credit = childless_eitc_2021(L, _earned(u), u["t_agi"], u["t_fs"], ages, _invest(u))
    return credit - u["t_eitc"]


def ssi_exclusions_indexed(u, L):
    """INC-3.02 (point 8): SSI's $20 general and $65 earned income exclusions indexed to prices from their 2029 value.
    Each recipient with other income gains the general exclusion's increase; each with earnings also gains half the
    earned exclusion's (earnings above it count at 50%). Shown at the window's middle, 2034 prices over 2029; only the
    shares are used. A couple's shared exclusion and deemed parental income are treated per recipient."""
    d = econ("cpiu", 2034) / econ("cpiu", L["year"]) - 1
    with_income = min(u["n_ssi"], u["n_ssi_unearned"] + u["n_ssi_earn"])
    return 12 * d * (20 * with_income + 65 / 2 * u["n_ssi_earn"])


SMI_SIZE = {1: 0.52, 2: 0.68, 3: 0.84, 4: 1.00, 5: 1.16, 6: 1.32}     # HHS's state median income size adjustment


def state_median(size, smi4):
    """State median income for a family of `size`, from the four-person line and HHS's size factors."""
    return smi4 * SMI_SIZE.get(size, 1.32 + 0.03 * (size - 6))


def guarantee_charge(income, size, smi4):
    """FAM-2.01's charge for care of a child under 5 (`DEC-2026-11-11-03`): free at or below 85% of state median
    income, then a rate rising in a straight line to 7% of income at 150% (care's working choice), 7% above."""
    smi = state_median(size, smi4)
    x = income / smi
    return 0.07 * income * min(max((x - 0.85) / (1.5 - 0.85), 0.0), 1.0)


def cdctc_rate(agi, fs):
    """Section 21(a)(2) as P.L. 119-21 sec. 70405 left it: 50%, less a point per $2,000 above $15,000 down to 35%, then
    a point per $2,000 ($4,000 joint) above $75,000 ($150,000 joint) down to 20%. Not indexed."""
    r = max(50 - -(-max(agi - 15000, 0) // 2000), 35)
    start, step = (150000, 4000) if fs == "joint" else (75000, 2000)
    return max(r - -(-max(agi - start, 0) // step), 20) / 100


def cdctc_refundable(u, L, spend_scale=1.0, school_age_netted=0.0):
    """INC-4.01, rescoped (Espen, November 13, option B): the dependent care credit made refundable, for care no other
    program pays for. It counts only what a family pays itself: neither the child care guarantee (FAM-2.01) nor the
    school-age block grant the plan keeps (CCDF for children 5 to 12, FAM-2.04) pays a dollar twice.
    The unit's child care spending (the CPS's, `SPM_CHILDCAREXPNS`, given to the tax units of its SPM unit with
    children under 13) is what the family paid out of pocket while working: the survey asks what was paid, and the
    subsidies families receive, CCDF's among them, are not in it. So the school-age care it reports is already net of
    what CCDF pays for the children it reaches, and the block grant's reach under the plan is today's (FAM-2.04 keeps
    its school-age share at the FY2029 level, indexed to prices); that care counts in full. Care for children under 5
    counts only up to the guarantee's charge (`guarantee_charge`), since the guarantee pays the rest.
    Limits: $3,000 or $6,000, and the lower earner's earnings on a joint return. The gain is the part of the credit
    above the tax before credits (today it is nonrefundable and comes before the child credit), at full take-up.
    Care for a disabled adult is not in the CPS.

    Two sensitivities, not the central case: `spend_scale` scales the reported spending (the survey under-reports
    it), and `school_age_netted` removes that share of school-age spending for units at or below 85% of state median
    income, CCDF's income line, as if the survey had reported care before CCDF's payments."""
    q = u["n_dep_u5"] + u["n_dep_5_12"]
    if not q or u.get("childcare", 0) <= 0:
        return 0.0
    spend = u["childcare"] * spend_scale
    under5 = spend * u["n_dep_u5"] / q
    school = spend - under5
    if school_age_netted and u["t_agi"] <= 0.85 * state_median(u["n_people"], L["smi4"]):
        school *= 1 - school_age_netted
    expense = school + min(under5, guarantee_charge(u["t_agi"], u["n_people"], L["smi4"]))
    joint = u["t_fs"] == "joint"
    earn = min(u["wage_h"] + u["se_h"], u["wage_s"] + u["se_s"]) if joint else u["wage_h"] + u["se_h"]
    expense = min(expense, 3000 if q == 1 else 6000, max(earn, 0))
    credit = cdctc_rate(u["t_agi"], u["t_fs"]) * expense
    return max(credit - u["t_tax_before_credits"], 0.0) if credit > 0 else 0.0


RULES = {"afa_child_benefit": afa_child_benefit, "surtax_100k": surtax_100k,
         "inc1_childless_eitc": inc1_childless_eitc, "ssi_exclusions_indexed": ssi_exclusions_indexed,
         "cdctc_refundable": cdctc_refundable}
