"""The provision interface: booked provisions, distributed to household groups by incidence keys.

Role: the household model's link to the federal budget model (`MODEL-CARD.md`, "Provision interface"). Status: working.

Each row of `models/data/inputs/incidence-rows.csv` (adopted input, read only) books an amount over FY2030-39, a formula
over ledger IDs read from the budget model's `ledger.json`, and splits it across one or more incidence keys. A key gives
the shares of the amount falling on each income quintile and on the top 1%. This module supplies the keys two ways:
  * `legacy`: the shares typed in `incidence-keys.csv` (adopted input), as the legacy incidence model uses them;
  * `model`: for each key `keys.csv` marks `micro`, the shares are measured on the 2029 baseline households (a
    household field, or a provision rule from `rules.py` computed tax unit by tax unit); the rest keep the legacy key.
The arithmetic after the keys is the legacy model's, so with `legacy` keys and its 140 million households this module
reproduces the retired legacy incidence model's last results exactly (tested against `test-data/`); `d3.py` builds
the D3 report and the budget model's readers on it.
"""
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, "..")
sys.path.insert(0, TOOLS)
import scenarios as SF  # noqa: E402  (models/tools/scenarios.py, shared with the fiscal and legacy incidence models)
from inputs import read, num  # noqa: E402

from distribution import assign  # noqa: E402
from params import econ, per_household  # noqa: E402
from rules import RULES  # noqa: E402

GROUPS = ["Q1", "Q2", "Q3", "Q4", "Q5"]
LEGACY_HH = 140e6
LEGACY_INC = {"Q1": 23e3, "Q2": 60e3, "Q3": 105e3, "Q4": 180e3, "Q5": 520e3, "T1": 4.3e6, "Q5x": 0}


def ledger_values(path):
    with open(path) as f:
        L = json.load(f)
    v = {b["id"]: b["cost_mid"] for b in L["bills"]}
    v.update({r["id"]: r["mid"] for r in L["revenue"]})
    v.update({c["id"]: c["saves_tn"] for c in L["cuts"]})
    return v


def amount(formula, ledger):
    expr = re.sub(r"\[([^\]]+)\]", lambda m: repr(ledger[m.group(1)]), formula)
    return round(eval(expr, {"__builtins__": {}}), 10)


def parts(spec, x):
    out = []
    for p in spec.split(";"):
        k, _, e = p.strip().partition(" ")
        out.append((k, eval(e, {"__builtins__": {}}, {"x": x}) if e else x))
    return out


def rows(ledger):
    """(package rows, options) as the legacy model reads them."""
    pkg, opts = [], {}
    for r in read("incidence-rows.csv"):
        amt = amount(r["amount"], ledger)
        ps = parts(r["parts"], amt)
        if r["set"] == "package":
            pkg.append((r["id"], r["label"], r["side"], amt, ps, r["basis"]))
        else:
            opts[r["id"]] = (r["side"], amt, ps, r["label"])
    return pkg, opts


def legacy_keys():
    return {r["key"]: ([num(r[q]) for q in ("q1", "q2", "q3", "q4", "q5")], num(r["top1"]))
            for r in read("incidence-keys.csv")}


def key_specs():
    with open(os.path.join(HERE, "keys.csv"), newline="") as f:
        return {r["key"]: r for r in csv.DictReader(f)}


def household_base(B, base):
    """Each household's amount of `base`: a sum of household fields ('a+b') or a rule over its tax units."""
    hh = {h["hh"]: h for h in B["households"]}
    vals = {k: 0.0 for k in hh}
    if base.startswith("rule:"):
        fn = RULES[base[5:]]
        for u in B["units"]:
            vals[u["hh"]] += fn(u, B["law"])
    else:
        for k, h in hh.items():
            vals[k] = sum(h[f] for f in base.split("+"))
    return vals


def micro_shares(B, base):
    """Shares (percent) of `base` by D3 quintile, and the top 1%'s share, on the baseline households."""
    H = B["households"]
    if "g5" not in H[0]:
        assign(H, "size_adjusted")
    vals = household_base(B, base)
    tot = sum(h["weight"] * vals[h["hh"]] for h in H)
    sh = [100 * sum(h["weight"] * vals[h["hh"]] for h in H if h["g5"] == g) / tot for g in range(1, 6)]
    t1 = 100 * sum(h["weight"] * vals[h["hh"]] for h in H if h["top1"]) / tot
    return sh, t1


def model_keys(B):
    K = legacy_keys()
    out, source = {}, {}
    for k, spec in key_specs().items():
        if spec["method"] == "micro":
            sh, t1 = micro_shares(B, spec["base"])
            if spec.get("top1") == "legacy":     # the CPS cannot see the top 1% for this base (keys.csv says why)
                t1 = K[k][1]
            out[k] = (sh, t1)
            source[k] = "micro"
        else:
            out[k] = K[k]
            source[k] = "legacy"
    missing = set(K) - set(out)
    if missing:
        raise SystemExit(f"keys.csv lacks keys {sorted(missing)}")
    return out, source


def dist(ps, K):
    out = {g: 0.0 for g in GROUPS}
    out["T1"] = 0.0
    for key, amt in ps:
        sh, t1 = K[key]
        assert abs(sum(sh) - 100) < 1e-6, key
        for g, s in zip(GROUPS, sh):
            out[g] += amt * s / 100
        out["T1"] += amt * t1 / 100
    return out


def run(pkg, opts_table, opts, drop, K, hh=LEGACY_HH, inc=LEGACY_INC):
    """Net dollars per household per year, 2030-39 average, by group (the legacy model's `run`)."""
    def per_hh(tn, g):
        n = hh * (0.01 if g == "T1" else (0.19 if g == "Q5x" else 0.2))
        return tn * 1e12 / 10 / n
    rs = [r for r in pkg if r[0] not in drop]
    for o in opts:
        side, amt, ps, label = opts_table[o]
        rs.append((o, label, side, amt, ps, "ledger option"))
    tot = {"cost": {}, "benefit": {}}
    lines = []
    for rid, label, side, amt, ps, basis in rs:
        d = dist(ps, K)
        lines.append((rid, label, side, amt, d))
        for g, v in d.items():
            tot[side][g] = tot[side].get(g, 0) + v
    for side in tot:
        tot[side]["Q5x"] = tot[side]["Q5"] - tot[side]["T1"]
    res = {}
    for g in GROUPS + ["Q5x", "T1"]:
        b, c = tot["benefit"][g], tot["cost"][g]
        res[g] = dict(benefit=round(per_hh(b, g)), cost=round(per_hh(c, g)), net=round(per_hh(b - c, g)),
                      pct=round(100 * per_hh(b - c, g) / inc[g], 1) if inc.get(g) else None)
    return res, lines


def scenarios():
    return SF.incidence(SF.load())


def mid_window_households(B):
    """Households in the middle of FY2030-39: the model's 2029 count (the CPS's, grown with CBO's households) grown on
    to the FY2034-35 average with CBO's households (CBO, February 2026). The CPS counts more households than CBO's
    series (137.1 million in 2025 against 132.4 million); the model keeps the survey's level, so a key's shares and the
    count it is divided by describe the same population."""
    n = sum(h["weight"] for h in B["households"])
    return n * (econ("households", 2034) + econ("households", 2035)) / 2 / econ("households", B["year"])


def model_incomes(B):
    """Average expanded cash income by group in 2029, grown to the window's middle (FY2034-35) with nominal GDP per
    household; the legacy model typed its own 2034 estimates."""
    H = B["households"]
    f = (per_household("gdp", 2034, 2029) + per_household("gdp", 2035, 2029)) / 2
    out = {}
    for g in range(1, 6):
        w = sum(h["weight"] for h in H if h["g5"] == g)
        out[f"Q{g}"] = f * sum(h["weight"] * h["expanded"] for h in H if h["g5"] == g) / w
    w = sum(h["weight"] for h in H if h["top1"])
    out["T1"] = f * sum(h["weight"] * h["expanded"] for h in H if h["top1"]) / w
    out["Q5x"] = 0
    return out
