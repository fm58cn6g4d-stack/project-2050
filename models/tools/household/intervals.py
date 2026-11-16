#!/usr/bin/env python3
"""Sampling intervals for the household model's headline outputs, from the CPS ASEC's 160 replicate weights.

Role: the household model's uncertainty step (`MODEL-CARD.md`, "Sampling uncertainty"). Status: working.

The Census Bureau publishes 160 replicate person weights with the CPS ASEC (`asec_csv_repwgt_2026.csv`, inside the
same archive as the extract: `extract.py`'s SHA-256). Its method is successive difference replication: each output is
recomputed with every replicate weight in place of the full-sample weight, and

    SE = sqrt(4/160 x sum over r of (estimate_r - estimate_0)^2),   90% interval = estimate +/- 1.645 x SE,

where estimate_0 uses the replicate file's base weight (`pwwgt0`). The archive is 139 MB and the replicate file
holds 22 million numbers, so neither is committed: this step reads the archive, writes the small `intervals.json`
(committed), and `run.py` reports it in `results.md`, section 9. Run from the repository root:

  python3 models/tools/household/intervals.py --archive /path/to/asecpub26csv.zip

Each record's replicate weight follows the weight the model already uses for it (the Census's own definitions, checked
on the file: `HSUP_WGT` is the householder's person weight, `SPM_WEIGHT` the SPM unit head's):
  * tax units: the head's (the first filer by line number, as `extract.py` picks it);
  * households: the householder's;
  * SPM units: the head's for the poverty gap, and the sums of members' weights by age group for poverty rates;
all aged to 2029 with the same household factor as the full-sample weights (`data.py`, A-2).

What the intervals cover: sampling error only, the error from surveying about 135,000 people rather than everyone.
They hold each record's own computed amounts (taxes, poverty status, a package's charge) fixed and reweight; group
cut points, quintile membership, measured keys and household counts are recomputed in every replicate. Two
weight-dependent calibrations are held at their full-sample values: SNAP's work-rule probabilities (A-8) and the
state-median stand-in (A-10). Neither moves a headline output by more than a few hundredths of a point. Not covered:
nonsampling error (under-reporting, top-coding, the model's own assumptions), which is larger for most outputs.

The take-home pass rates are `health_cost_review.take_home_micro`'s, computed for the package specifications in
`TAKE_HOME`, with the package itself (its rates and lines) held fixed: the question is how many of the country's
workers pass a given design, not how a design picked on another sample would differ.
"""
import argparse
import csv
import datetime
import hashlib
import io
import json
import math
import os
import subprocess
import sys
import zipfile
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))

from extract import SHA256, SOURCE_URL  # noqa: E402

R = 160
Z90 = 1.645
REPLICATE_MEMBER = "asec_csv_repwgt_2026.csv"
OUT = os.path.join(HERE, "intervals.json")

# The take-home specifications reported (health_cost_review.unified_spec arguments; S is 5 plus H1b's fold-in)
TAKE_HOME = {
    "recommended_2.25": dict(R=2.25, hi=2.5, form="linear"),
    "alternative_2.5": dict(R=2.5, hi=2.5, form="linear"),
}


def sdr(theta0, reps):
    """Successive difference replication: the standard error from the base-weight estimate and the 160 replicates."""
    reps = np.asarray(reps, dtype=float)
    return math.sqrt(4.0 / len(reps) * float(np.sum((reps - theta0) ** 2)))


def summarize(value, theta0, reps):
    se = sdr(theta0, reps)
    return {"value": value, "se": se, "lo90": value - Z90 * se, "hi90": value + Z90 * se,
            "half90": Z90 * se, "replicate_base": theta0}


# ----------------------------------------------------------------------------------------------------------------------
# Replicate weights, aligned to the extract's records

def _rows(zf, member, cols):
    with zf.open(member) as raw:
        r = csv.reader(io.TextIOWrapper(raw, encoding="latin-1", newline=""))
        head = next(r)
        idx = [head.index(c) for c in cols]
        for line in r:
            yield [line[k] for k in idx]


def replicate_weights(archive):
    """Arrays of shape (records, 161), column 0 the base weight `pwwgt0`, for the extract's tax units, SPM units (the
    head's, and member sums by age group) and households, keyed as `data.load` orders them."""
    h = hashlib.sha256()
    with open(archive, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    if h.hexdigest() != SHA256:
        raise SystemExit(f"archive hash {h.hexdigest()} is not the recorded {SHA256}")
    zf = zipfile.ZipFile(archive)
    rep_cols = ["h_seq", "PPPOS"] + [f"pwwgt{k}" for k in range(R + 1)]
    reps = {}
    for line in _rows(zf, REPLICATE_MEMBER, rep_cols):
        reps[(int(line[0]), int(line[1]))] = np.array(line[2:], dtype=float)
    cols = ["PH_SEQ", "PPPOS", "A_LINENO", "TAX_ID", "DEP_STAT", "SPM_ID", "A_AGE", "PERRP", "SPM_HEAD", "MARSUPWT"]
    unit_people = defaultdict(list)
    spm_head, spm_sum = {}, defaultdict(lambda: np.zeros((4, R + 1)))
    hh_head, hh_sum = {}, defaultdict(lambda: np.zeros(R + 1))
    worst = 0.0
    n = 0
    for p in _rows(zf, "pppub26.csv", cols):
        hh, pos, line, tid, dep, sid, age = (int(float(x)) for x in p[:7])
        w = reps.pop((hh, pos))                     # KeyError if a person lacks replicate weights
        worst = max(worst, abs(w[0] - int(p[9]) / 100))
        n += 1
        unit_people[(hh, tid)].append((line, dep, w))
        g = 1 if age < 18 else (3 if age >= 65 else 2)
        s = spm_sum[sid]
        s[0] += w
        s[g] += w
        if p[8] == "1":
            spm_head[sid] = w
        if p[7] in ("40", "41") and hh not in hh_head:
            hh_head[hh] = w
        hh_sum[hh] += w
    if reps:
        raise SystemExit(f"{len(reps)} replicate records match no person")
    units = {}
    for key, ps in unit_people.items():
        ps.sort(key=lambda t: t[0])
        filers = [t for t in ps if t[1] == 0] or ps[:1]
        units[key] = filers[0][2]
    return {"units": units, "spm_head": spm_head, "spm_groups": dict(spm_sum), "households": hh_head,
            "hh_people": dict(hh_sum), "persons": n, "max_base_weight_difference": worst}


def aligned(RW, B):
    """The replicate arrays in the order of the baseline's records, aged with the baseline's weight factor."""
    from params import uprating
    f = uprating(B["year"])["weight"] if B["year"] != 2025 else 1.0
    U = np.array([RW["units"][(u["hh"], u["tid"])] for u in B["units"]]) * f
    S = np.array([RW["spm_head"][s["spm"]] for s in B["spm"]]) * f
    G = np.array([RW["spm_groups"][s["spm"]] for s in B["spm"]]) * f      # (spm, 4, 161)
    H = np.array([RW["households"][h["hh"]] for h in B["households"]]) * f
    return U, S, G, H


# ----------------------------------------------------------------------------------------------------------------------
# Estimators: each takes the baseline and weight arrays (one column per replicate) and returns {metric: array}

def poverty_metrics(B, S, G, resources):
    """SPM rates (percent) by age group, poor people (millions) and the gap ($ billion), one value per column."""
    spm = B["spm"]
    poor = np.array([s[resources] < s["threshold"] for s in spm], dtype=float)
    out = {}
    for k, name in enumerate(("all", "children", "18_64", "65_plus")):
        out[f"rate_{name}"] = 100 * (poor @ G[:, k, :]) / G[:, k, :].sum(axis=0)
    out["poor_all_m"] = (poor @ G[:, 0, :]) / 1e6
    out["poor_children_m"] = (poor @ G[:, 1, :]) / 1e6
    gap = np.array([max(s["threshold"] - s[resources], 0) for s in spm])
    out["gap_bn"] = (gap @ S) / 1e9
    return out


def groups(rank, W, n=5):
    """Group (1..n) and top-1% flags for every record in every column, on equal weighted counts (`distribution.assign`'s
    midpoint rule, recomputed per column)."""
    order = np.argsort(rank, kind="stable")
    Ws = W[order]
    cum = np.cumsum(Ws, axis=0) - Ws / 2
    mid = cum / Ws.sum(axis=0)
    g = np.minimum((mid * n).astype(int) + 1, n)
    top = mid >= 0.99
    G = np.empty_like(g)
    T = np.empty_like(top)
    G[order] = g
    T[order] = top
    return G, T


def _by_group(values, W, G, T, n=5):
    """Weighted sums of `values` by group (rows 0..n-1), then the top 1% (row n), one column per replicate."""
    out = np.zeros((n + 1, W.shape[1]))
    vw = values[:, None] * W
    for q in range(1, n + 1):
        out[q - 1] = np.where(G == q, vw, 0).sum(axis=0)
    out[n] = np.where(T, vw, 0).sum(axis=0)
    return out


def tax_rate_metrics(B, H):
    """D3 average federal tax rates (income tax and payroll, percent of expanded cash income) by quintile and the
    top 1%."""
    hs = B["households"]
    G, T = groups(np.array([h["size_adjusted"] for h in hs]), H)
    inc = _by_group(np.array([h["expanded"] for h in hs]), H, G, T)
    it = _by_group(np.array([h["income_tax"] for h in hs]), H, G, T)
    pr = _by_group(np.array([h["payroll"] for h in hs]), H, G, T)
    out = {}
    for i, lab in enumerate(["Q1", "Q2", "Q3", "Q4", "Q5", "T1"]):
        out[f"income_tax_rate_{lab}"] = 100 * it[i] / inc[i]
        out[f"federal_rate_{lab}"] = 100 * (it[i] + pr[i]) / inc[i]
    return out


def d3_metrics(B, H, ledger_path):
    """Net dollars per household per year, FY2030-39, by D3 quintile and the top 1%, on the model's keys: every
    measured key, the household count and the groups' incomes recomputed in each replicate (`provisions.py`)."""
    import provisions as P
    from params import per_household
    hs = B["households"]
    G, T = groups(np.array([h["size_adjusted"] for h in hs]), H)
    led = P.ledger_values(ledger_path)
    pkg, opts = P.rows(led)
    S = P.scenarios()
    KL = P.legacy_keys()
    specs = P.key_specs()
    bases = {k: np.array([v for v in _ordered(P.household_base(B, s["base"]), hs)])
             for k, s in specs.items() if s["method"] == "micro"}
    sums = {k: _by_group(v, H, G, T) for k, v in bases.items()}
    expd = _by_group(np.array([h["expanded"] for h in hs]), H, G, T)
    cnt = _by_group(np.ones(len(hs)), H, G, T)
    ratio = P.mid_window_households(B) / sum(h["weight"] for h in hs)
    f = (per_household("gdp", 2034, 2029) + per_household("gdp", 2035, 2029)) / 2
    out = defaultdict(lambda: np.zeros(H.shape[1]))
    for c in range(H.shape[1]):
        K = dict(KL)
        for k, sm in sums.items():
            tot = sm[:5, c].sum()
            t1 = 100 * sm[5, c] / tot
            if specs[k].get("top1") == "legacy":
                t1 = KL[k][1]
            K[k] = ([100 * sm[q, c] / tot for q in range(5)], t1)
        inc = {f"Q{q + 1}": f * expd[q, c] / cnt[q, c] for q in range(5)}
        inc["T1"] = f * expd[5, c] / cnt[5, c]
        inc["Q5x"] = 0
        hh = H[:, c].sum() * ratio
        for name, (o, drop) in S.items():
            res = P.run(pkg, opts, o, drop, K, hh, inc)[0]
            tag = name.split(".")[0]
            for g in P.GROUPS + ["T1"]:
                out[f"{tag}_net_{g}"][c] = res[g]["net"]
    return dict(out)


def _ordered(vals, hs):
    return [vals[h["hh"]] for h in hs]


def take_home_metrics(U):
    """`health_cost_review.take_home_micro`'s pass shares (percent) for each `TAKE_HOME` package, with the tax units'
    weights replaced column by column. The package is built once, on the full sample."""
    import health_cost_review as HC
    import health_financing as HF
    ctx = HF.context()
    case = HC.cost_cases(HC._g40())["design"]
    fold = HC.h1b_restated(ctx)["fold_into_s_points"]
    X = HF.keys()[4]
    units = X["B"]["units"]
    if len(units) != U.shape[0]:
        raise SystemExit("health_financing's baseline units do not match the extract")
    saved = [u["weight"] for u in units]
    pkgs = {k: HC.unified_package(ctx, case, HC.unified_spec(S=5.0 + fold, **v)) for k, v in TAKE_HOME.items()}
    pkgs["package_E"] = HC.health_package(ctx, case, HC.PACKAGES2["E"][2])
    out = defaultdict(lambda: np.zeros(U.shape[1]))
    full = {}
    try:
        for c in range(-1, U.shape[1]):
            if c >= 0:
                for u, w in zip(units, U[:, c]):
                    u["weight"] = float(w)
            for k, o in pkgs.items():
                th = HC.take_home_micro(ctx, o)
                vals = {f"{k}_workers": th["all"], f"{k}_workers_below_200fpl": th["below_200fpl"]}
                if k != "package_E":
                    vals[f"{k}_workers_with_low2"] = HC.take_home_micro(ctx, o, low2=True)["all"]
                    vals[f"{k}_others"] = HC.take_home_micro(ctx, o, who="others")["all"]
                for m, v in vals.items():
                    if c < 0:
                        full[m] = v
                    else:
                        out[m][c] = v
    finally:
        for u, w in zip(units, saved):
            u["weight"] = w
    return full, dict(out)


# ----------------------------------------------------------------------------------------------------------------------

def _full(B, fn, *args):
    """The estimator on the model's own full-sample weights (one column)."""
    return {k: float(v[0]) for k, v in fn(B, *args).items()}


def run(archive, ledger_path, with_take_home=True):
    from budget import baseline
    RW = replicate_weights(archive)
    res = {"method": "successive difference replication, 160 replicates: SE = sqrt(4/160 x sum (est_r - est_0)^2); "
                     "90% interval = estimate +/- 1.645 SE; sampling error only",
           "source": SOURCE_URL, "archive_sha256": SHA256, "replicate_member": REPLICATE_MEMBER,
           "persons_joined": RW["persons"], "max_base_weight_difference": round(RW["max_base_weight_difference"], 4),
           "metrics": {}}
    for year in (2025, 2029):
        B = baseline(year)
        U, S, G, H = aligned(RW, B)
        own_S = np.array([[s["weight"]] for s in B["spm"]])
        own_G = np.array([[[s[k]] for k in ("w_people", "w_children", "w_18_64", "w_65")] for s in B["spm"]])
        own_H = np.array([[h["weight"]] for h in B["households"]])
        blocks = {}
        res_names = ["resources_model"] + (["resources_census"] if year == 2025 else [])
        for rn in res_names:
            blocks[f"poverty_{year}_{rn.split('_')[1]}"] = (poverty_metrics, (S, G, rn), (own_S, own_G, rn))
        if year == 2029:
            blocks["tax_rates_2029_d3"] = (tax_rate_metrics, (H,), (own_H,))
            if ledger_path:
                blocks["d3_net_per_household"] = (d3_metrics, (H, ledger_path), (own_H, ledger_path))
        for name, (fn, rep_args, own_args) in blocks.items():
            reps = fn(B, *rep_args)
            own = _full(B, fn, *own_args)
            res["metrics"][name] = {m: summarize(own[m], float(v[0]), v[1:]) for m, v in reps.items()}
        if year == 2029 and with_take_home:
            full, reps = take_home_metrics(U)
            res["metrics"]["take_home"] = {m: summarize(full[m], float(v[0]), v[1:]) for m, v in reps.items()}
            res["take_home_specs"] = {k: dict(v, S="5 + H1b's fold-in") for k, v in TAKE_HOME.items()}
    try:
        res["model_commit"] = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                                             cwd=HERE).stdout.strip()
    except OSError:
        res["model_commit"] = ""
    res["run_date"] = datetime.date.today().isoformat()
    if ledger_path:
        import provisions as P
        res["ledger_sha256"] = hashlib.sha256(json.dumps(P.ledger_values(ledger_path), sort_keys=True)
                                              .encode()).hexdigest()
    return res


def _round(x):
    if isinstance(x, dict):
        return {k: _round(v) for k, v in x.items()}
    if isinstance(x, float):
        return round(x, 4)
    return x


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--archive", required=True)
    ap.add_argument("--ledger", default=os.path.join(HERE, "..", "..", "..", "build", "ledger.json"))
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--no-take-home", action="store_true")
    a = ap.parse_args()
    led = a.ledger if os.path.exists(a.ledger) else None
    res = run(a.archive, led, not a.no_take_home)
    with open(a.out, "w") as f:
        json.dump(_round(res), f, indent=1, sort_keys=True)
        f.write("\n")
    print("intervals written to", a.out)


if __name__ == "__main__":
    main()
