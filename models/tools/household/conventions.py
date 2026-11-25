"""The CBO-convention check: the household model's distribution conventions set against CBO's, one step at a time.

Role: part of the household model's benchmarks (`MODEL-CARD.md`, "Distribution conventions" and "The CBO-convention
check"). Status: working.

CBO's *The Distribution of Household Income, 2022* (January 2026, cbo.gov/publication/61911, SRC-4802) ranks
households by income before transfers and taxes (market income, including employers' payroll taxes and health
premiums, plus Social Security, Medicare, unemployment insurance and workers' compensation), divided by the square
root of household size, into quintiles holding equal numbers of people; households with negative income are in no
quintile; and the same income is the denominator of its average tax rates. The D3 convention ranks households by
expanded cash income (all cash income plus the employer's payroll tax) over the square root of household size, in
quintiles of equal numbers of households.

`steps(B, ledger_path)` moves from D3 to CBO one convention at a time on the 2029 baseline households:
  0. D3 as it is;
  1. quintiles of equal numbers of people;
  2. CBO's income without the health values: SSI and TANF (means-tested cash) out, negative incomes out of the groups;
  3. Medicare and employers' health premiums added at working values (`MEDICARE_2029`, `ESI_EMPLOYER_RATIO`), since
     the CPS records neither.
At each step it reports average federal tax rates (income and payroll), the share of households that change quintile
from D3, and scenario Q's net per household on the model's keys re-measured on that step's groups (the typed keys
stay as they are, since they were typed on no convention the model can move). Per-household amounts divide each
group's total by its own household count, since equal-people groups hold unequal numbers of households.

What it cannot reach: CBO also counts corporate and excise taxes, adds tax-return data at the top and corrects the
survey's under-reported transfers. Those are data, not conventions; the benchmark table in `MODEL-CARD.md` covers them.
"""
import provisions as P
from distribution import assign
from params import constant, per_household

# Medicare's value per enrollee in 2029: CBO's 2032 spending per enrollee, $19,500 fee-for-service and $20,900 in
# Medicare Advantage (EV-CAR-061), at about $20,200, brought back three years at 4.8% a year per person (the per-person
# health growth `health_cost_review.py` uses). A working value; CBO values Medicare at its average cost to government.
MEDICARE_2029 = constant("medicare.cost_per_enrollee_2032") / (1 + constant("medicare.growth_per_person")) ** 3
# Employers' premiums: the worker paid 26.4% of the 2026 family premium (KFF, EV-CAR-111 and EV-CAR-112), so each dollar
# of premium a job-covered tax unit reports paying stands for 0.736/0.264 dollars the employer paid.
ESI_EMPLOYER_RATIO = (1 - constant("esi.worker_share")) / constant("esi.worker_share")
# CBO's published 2022 rates (table 9, recorded on the model card): lowest quintile and top 1%, income tax / payroll
CBO_2022 = {"Q1": (-10.1, 9.5), "T1": (23.9, 2.0)}


def _incomes(B):
    hs = B["households"]
    esi = {}
    for u in B["units"]:
        if u["n_employer_cov"] > 0 and u["n_marketplace"] == 0:
            esi[u["hh"]] = esi.get(u["hh"], 0.0) + u["premiums_paid"] * ESI_EMPLOYER_RATIO
    for h in hs:
        h["cbo_cash"] = h["expanded"] - h["ssi"] - h["tanf"]
        h["cbo_health"] = h["n_medicare"] * MEDICARE_2029 + esi.get(h["hh"], 0.0)
        h["cbo_full"] = h["cbo_cash"] + h["cbo_health"]


STEPS = [
    ("0. D3: expanded cash income, equal households", "expanded", "units", False),
    ("1. Equal numbers of people", "expanded", "people", False),
    ("2. CBO's income before the health values (SSI and TANF out, negative incomes out)", "cbo_cash", "people", True),
    ("3. Medicare and employers' premiums added (CBO's income before transfers and taxes)", "cbo_full", "people", True),
]


def _group(hs, income, by, drop_negative):
    """Sets h['cg'] (1..5, or 0 for a household in no group) and h['ct1']."""
    keep = [h for h in hs if not (drop_negative and h[income] < 0)]
    for h in hs:
        h["cg"], h["ct1"] = 0, False
        h["_rank"] = h[income] / max(h["numper"], 1) ** 0.5
    assign(keep, "_rank", by=by)
    for h in keep:
        h["cg"], h["ct1"] = h["g5"], h["top1"]


def _rates(hs, income):
    out = {}
    for lab, sel in [(f"Q{q}", lambda h, q=q: h["cg"] == q) for q in range(1, 6)] + [("T1", lambda h: h["ct1"])]:
        g = [h for h in hs if sel(h)]
        inc = sum(h["weight"] * h[income] for h in g)
        it = sum(h["weight"] * h["income_tax"] for h in g)
        pr = sum(h["weight"] * h["payroll"] for h in g)
        out[lab] = {"income_tax": round(100 * it / inc, 1), "payroll": round(100 * pr / inc, 1),
                    "households_m": round(sum(h["weight"] for h in g) / 1e6, 1),
                    "people_m": round(sum(h["weight"] * h["numper"] for h in g) / 1e6, 1)}
    return out


def _net_q(B, pkg, opts, scen, KL, specs, bases):
    """Scenario Q on the step's groups: measured keys re-measured, typed keys kept; net per household by group."""
    hs = B["households"]
    K = dict(KL)
    for k, vals in bases.items():
        tot = sum(h["weight"] * vals[h["hh"]] for h in hs if h["cg"])
        sh = [100 * sum(h["weight"] * vals[h["hh"]] for h in hs if h["cg"] == q) / tot for q in range(1, 6)]
        t1 = KL[k][1] if specs[k].get("top1") == "legacy" else \
            100 * sum(h["weight"] * vals[h["hh"]] for h in hs if h["ct1"]) / tot
        K[k] = (sh, t1)
    o, drop = scen
    _, lines = P.run(pkg, opts, o, drop, K)
    ratio = P.mid_window_households(B) / sum(h["weight"] for h in hs)
    n = {f"Q{q}": ratio * sum(h["weight"] for h in hs if h["cg"] == q) for q in range(1, 6)}
    n["T1"] = ratio * sum(h["weight"] for h in hs if h["ct1"])
    tot = {g: 0.0 for g in n}
    for rid, label, side, amt, d in lines:
        for g in n:
            tot[g] += d[g] * (1 if side == "benefit" else -1)
    return {g: round(tot[g] * 1e12 / 10 / n[g]) for g in n}


def steps(B, ledger_path):
    hs = B["households"]
    _incomes(B)
    saved = [(h["g5"], h["top1"]) for h in hs]
    led = P.ledger_values(ledger_path)
    pkg, opts = P.rows(led)
    S = P.scenarios()
    qname = next(n for n in S if n.startswith("Q."))
    KL = P.legacy_keys()
    specs = P.key_specs()
    bases = {k: P.household_base(B, s["base"]) for k, s in specs.items() if s["method"] == "micro"}
    out, d3_group = [], None
    try:
        for label, income, by, neg in STEPS:
            _group(hs, income, by, neg)
            if d3_group is None:
                d3_group = {h["hh"]: h["cg"] for h in hs}
            w = sum(h["weight"] for h in hs)
            moved = sum(h["weight"] for h in hs if h["cg"] != d3_group[h["hh"]]) / w
            out.append({"step": label, "income": income, "rates": _rates(hs, income),
                        "moved_from_d3_pct": round(100 * moved, 1),
                        "no_group_pct": round(100 * sum(h["weight"] for h in hs if not h["cg"]) / w, 2),
                        "net_q": _net_q(B, pkg, opts, S[qname], KL, specs, bases)})
    finally:
        for h, (g, t) in zip(hs, saved):
            h["g5"], h["top1"] = g, t
            for k in ("cg", "ct1", "_rank"):
                h.pop(k, None)
    f = (per_household("gdp", 2034, 2029) + per_household("gdp", 2035, 2029)) / 2
    tot_inc = {k: round(sum(h["weight"] * h[k] for h in hs) / 1e12, 2) for k in ("expanded", "cbo_cash", "cbo_full")}
    return {"steps": out, "income_tn_2029": tot_inc, "medicare_2029": round(MEDICARE_2029),
            "esi_employer_ratio": round(ESI_EMPLOYER_RATIO, 3), "cbo_2022": CBO_2022, "gdp_per_hh_factor": round(f, 4),
            "scenario": qname}
