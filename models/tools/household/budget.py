"""The baseline household budget: income, the main benefits and federal taxes for every unit in the CPS extract.

Role: the household model's core (`MODEL-CARD.md`, "What it measures"). Status: working.

`baseline(year)` returns three linked lists:
  * tax units, with the model's own federal income and payroll taxes under `params.law(year)`;
  * SPM units, with SPM resources rebuilt from the Census's elements but with the model's taxes in place of the
    Census tax model's (`resources_model`) and, for comparison, the Census's own (`resources_census`);
  * households, with the budget the distribution tables use.
At 2025 with the Census's taxes, `resources_census` reproduces `SPM_RESOURCES` exactly (tested).

Money is dollars a year in the target year's prices. Benefits are the survey's reported or Census-imputed values
(SNAP, housing, school meals, WIC and energy help as Census values them for the SPM), uprated; the model does not yet
simulate eligibility for them (`MODEL-CARD.md`, "What it does not do").
"""
from collections import defaultdict

from data import load
from params import law
from tax import unit_tax
import snap2025

CASH_TRANSFERS = ("ss", "ssi", "tanf", "uc", "vet")
NONCASH = ("snap", "housing", "school_lunch", "wic", "energy")


def market_income(u):
    return (u["wage_h"] + u["wage_s"] + u["se_h"] + u["se_s"] + u["interest"] + u["dividends"] + u["rent"]
            + u["capgain"] + u["pension"] + u["disab_surv"] + u["dep_wages"])


def cash_income(u):
    """Pre-tax cash income: market income plus cash transfers and other cash (the CPS's total money income)."""
    return (market_income(u) + sum(u[k] for k in CASH_TRANSFERS) + u["other"] + u["child_support_rcvd"]
            + u["dep_other_income"])


def baseline(year=2029, takeup="census", snap_law=True):
    """`takeup='census'` withholds refundable credits from units the Census tax model marks as nonfilers
    (assumption A-6); `takeup='full'` pays every unit its statutory credits. `snap_law=False` keeps SNAP at prior law
    (the survey's own rules), for comparison with P.L. 119-21's changes (`snap2025.py`, A-8)."""
    L = dict(law(year))
    units, spm, hhs = load(year)
    snap_summary = snap2025.apply(spm, year if snap_law else 2025)
    units25 = load(2025)[0] if year != 2025 else units
    by_spm = defaultdict(list)
    for u, u25 in zip(units, units25):
        t = unit_tax(u, L, refundable=(takeup == "full" or u["filestat"] != 6))
        u.update({"t_" + k: v for k, v in t.items()})
        u["market"] = market_income(u)
        u["cash"] = cash_income(u)
        u["cash_delta"] = u["cash"] - cash_income(u25)
        by_spm[u["spm"]].append(u)
    spm_index = {}
    for s in spm:
        us = by_spm.get(s["spm"], [])
        totval = s["totval"] + sum(u["cash_delta"] for u in us)
        noncash = sum(s[k] for k in NONCASH)
        exp = s["work_childcare"] + s["medical"] + s["child_support_paid"]
        s["totval_y"] = totval
        s["fedtax_model"] = sum(u["t_income_tax"] for u in us)
        s["fica_model"] = sum(u["t_fica_ee"] + u["t_se_tax"] for u in us)
        # the Census's own taxes, held at their 2025 share of cash income when aged (comparison only)
        scale = totval / s["totval"] if year != 2025 and s["totval"] > 0 else 1.0
        s["resources_census"] = totval + noncash - (s["fedtax"] + s["fica"]) * scale - s["sttax"] - exp
        s["resources_model"] = totval + noncash - s["fedtax_model"] - s["fica_model"] - s["sttax"] - exp
        spm_index[s["spm"]] = s
        # child care spending to the tax units with children under 13 (the care credit's, INC-4's rule)
        q = [u["n_dep_u5"] + u["n_dep_5_12"] for u in us]
        for u, k in zip(us, q):
            u["childcare"] = s["childcare"] * k / sum(q) if sum(q) else 0.0
    # national median cash income of four-person SPM units, standing in for state median income (FAM-2.01's lines)
    four = sorted((s["totval_y"], s["weight"]) for s in spm if s["numper"] == 4)
    half, acc = sum(w for _, w in four) / 2, 0.0
    for v, w in four:
        acc += w
        if acc >= half:
            L["smi4"] = v
            break
    hh_index = {h["hh"]: h for h in hhs}
    for h in hhs:
        h.update({k: 0.0 for k in ("market", "cash", "income_tax", "payroll", "payroll_er", "state_tax", "eitc",
                                   "ctc", "n_medicaid", "n_medicare", "n_employer_cov", "n_marketplace",
                                   "wages", "wages_capped", "capital", "ss", "children", "adults", "ssi_dep", "snap_prior",
                                   "snap_cut", *CASH_TRANSFERS,
                                   *NONCASH)})
    for u in units:
        h = hh_index[u["hh"]]
        h["market"] += u["market"]; h["cash"] += u["cash"]
        h["income_tax"] += u["t_income_tax"]; h["payroll"] += u["t_payroll"]; h["payroll_er"] += u["t_fica_er"]
        h["eitc"] += u["t_eitc"]; h["ctc"] += u["t_ctc_total"]
        for k in ("n_medicaid", "n_medicare", "n_employer_cov", "n_marketplace"):
            h[k] += u[k]
        for k in CASH_TRANSFERS:
            h[k] += u[k]
        h["ssi_dep"] += u["ssi_dep"]
        base = L["ss_wage_base"]
        h["wages"] += u["wage_h"] + u["wage_s"] + u["se_h"] + u["se_s"] + u["dep_wages"]
        h["wages_capped"] += (min(u["wage_h"] + max(u["se_h"], 0), base) + min(u["wage_s"] + max(u["se_s"], 0), base)
                              + u["dep_wages"])
        h["capital"] += u["interest"] + u["dividends"] + max(u["rent"], 0) + u["capgain"]
    for s in spm:
        h = hh_index[s["hh"]]
        for k in NONCASH:
            h[k] += s[k]
        h["snap_prior"] += s["snap_prior_law"]                  # SNAP before P.L. 119-21 (A-8), INC-2's key
        h["snap_cut"] += s["snap_prior_law"] - s["snap"]
        h["state_tax"] += s["sttax"]
        # persons by age, on the household's own weight (person weights differ slightly within a household)
        if s["weight"] > 0:
            h["children"] += s["numkids"]; h["adults"] += s["numadults"]
    for h in hhs:
        h["expanded"] = h["cash"] + h["payroll_er"]          # TPC-style: the employer's payroll tax counted as income
        h["federal_tax"] = h["income_tax"] + h["payroll"]
        h["net"] = h["cash"] + sum(h[k] for k in NONCASH) - h["income_tax"] - (h["payroll"] - h["payroll_er"]) - h["state_tax"]
        h["size_adjusted"] = h["expanded"] / max(h["numper"], 1) ** 0.5
    return {"year": year, "law": L, "units": units, "spm": spm, "households": hhs, "snap_law": snap_summary}
