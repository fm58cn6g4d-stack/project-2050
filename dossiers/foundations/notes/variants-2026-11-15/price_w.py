"""Design W: R% of all AGI from the first dollar plus S points on AGI above $200K/$250K (2025 $, x1.027 to 2026 $),
replacing the worker's 1.45% HI and the 0.9%; employers as in U; everything else as in M4. Run from models/tools.
Nothing in the repository is changed; every swap is restored."""
import json
import os
import sys

sys.path.insert(0, ".")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import health_cost_review as R  # noqa: E402
import health_financing as HF  # noqa: E402
import price_u as PU  # noqa: E402

SUR25 = {"single": 200000, "joint": 250000}
SUR26 = {k: v * 1.027 for k, v in SUR25.items()}
CUR = {"R": 0.0, "S": 0.0}
S_CAP = 15.0


def contribution_W(agi, fs, o):
    j = "joint" if fs == "joint" else "single"
    return CUR["R"] / 100 * max(agi, 0.0) + CUR["S"] / 100 * max(agi - SUR26[j], 0.0)


def comp_base(ctx, r, s):
    _, _, _, _, X = HF.keys()
    igrow = X["grow"] / ctx["price_2040"]
    tot = 0.0
    for u in X["B"]["units"]:
        a = u["t_agi"] * igrow
        j = "joint" if u["t_fs"] == "joint" else "single"
        tot += u["weight"] * (r * max(a, 0.0) + s * max(a - SUR26[j], 0.0))
    return tot / 1e9


class WLine:
    """The composite base r*AGI + s*(AGI above the surcharge line) as the 'second tier' at 1 point."""
    def __init__(self, ctx, r, s):
        self.ctx, self.r, self.s = ctx, r, s

    def __enter__(self):
        import provisions as P
        ctx, r, s = self.ctx, self.r, self.s
        K, _, _, _, X = HF.keys()
        B, vals = X["B"], X["vals"]
        old = R.LINE_HIGH
        b_old = sum(u["weight"] * max(u["t_agi"] * X["grow"] / ctx["price_2040"]
                                      - old["joint" if u["t_fs"] == "joint" else "single"], 0.0)
                    for u in X["B"]["units"]) / 1e9
        ratio = comp_base(ctx, r, s) / b_old
        sur = HF._line_rule(SUR25["single"], SUR25["joint"])     # same indexing as income_high's rule
        P.RULES["w_comp"] = lambda u, L: r * max(u["t_agi"], 0.0) + s * sur(u, L)
        sh, t1_cps = P.micro_shares(B, "rule:w_comp")
        self.keep = {k: K[k] for k in K if k == "income_high" or k.startswith("avoid_high_")}
        self.keep_v = dict(vals["high"])
        self.keep_pp = ctx["pp"]
        self.keep_c = R.contribution
        # the top 1%'s dollars: (r + s) times their dollars above the old line, the base scaled as the yield is
        t1 = min(K["income_high"][1] * (r + s) / ratio, sh[4])
        K["income_high"] = (sh, t1)
        for a, w in HF.AVOID_WEIGHTS.items():
            K[f"avoid_high_{a}"] = HF.avoidance_key(K, "income_high", w)
        vals["high"].clear()
        vals["high"].update(P.household_base(B, "rule:w_comp"))
        ctx["pp"] = dict(self.keep_pp, high_income=self.keep_pp["high_income"] * ratio)
        CUR.update(R=r, S=s)
        R.contribution = contribution_W
        return dict(ratio=ratio, pp_comp=ctx["pp"]["high_income"], t1=t1, t1_cps=t1_cps, shares=sh)

    def __exit__(self, *exc):
        K, _, _, _, X = HF.keys()
        K.update(self.keep)
        X["vals"]["high"].clear()
        X["vals"]["high"].update(self.keep_v)
        self.ctx["pp"] = self.keep_pp
        R.contribution = self.keep_c
        return False


def reass(ctx, case, spec, lost, r, s):
    with WLine(ctx, r, s):
        keep = ctx["need"]
        ctx["need"] = keep + lost["total"]
        try:
            return R.health_package(ctx, case, dict(spec, second=1.0))["reassigned"]
        finally:
            ctx["need"] = keep


def pp_unit(ctx, r, s):
    """$B a year per point of the composite (r, s), after the haircut."""
    with WLine(ctx, r, s) as i:
        return i["pp_comp"]


def solve(ctx, case, spec, lost, target, r=None, s=None):
    """Solve R (s given) or S (r given) so booked revenue reassigned equals target. Linear in each."""
    if r is None:
        r0 = 2.0
        f0 = reass(ctx, case, spec, lost, r0, s)
        per = pp_unit(ctx, 1.0, 0.0)
        return r0 + (f0 - target) / per, s
    s0 = 2.0
    f0 = reass(ctx, case, spec, lost, r, s0)
    per = pp_unit(ctx, 0.0, 1.0)
    return r, s0 + (f0 - target) / per


def take_home_W(ctx, o):
    """PU.take_home_U plus the pass share of workers below 200% of poverty."""
    _, oop = R._setup_visible(ctx)
    _, _, _, _, X = HF.keys()
    price = ctx["price_2040"]
    hgrow, igrow = 1.048 ** 11 / price, X["grow"] / price
    bands = [(0, 25e3), (25e3, 50e3), (50e3, 75e3), (75e3, 100e3), (100e3, 150e3), (150e3, 200e3), (200e3, 1e12)]
    res = {b: [0.0, 0.0] for b in bands}
    bykind, low = {}, [0.0, 0.0]
    for u in X["B"]["units"]:
        earn = u["wage_h"] + u["wage_s"] + max(u["se_h"], 0) + max(u["se_s"], 0)
        if earn <= 0 or (u["age_h"] >= 65 and u["n_medicare"] > 0 and u["wage_h"] <= 0):
            continue
        agi = u["t_agi"] * igrow
        fs = "joint" if u["t_fs"] == "joint" else "single"
        n = max(u["n_people"], 1)
        kind = "job" if u["n_employer_cov"] > 0 else ("own" if u["n_marketplace"] > 0 else
                                                      ("medicaid" if u["n_medicaid"] > 0 else
                                                       ("medicare" if u["n_medicare"] > 0 else "uninsured")))
        prem = u["premiums_paid"] * hgrow
        oo = (u["n_employer_cov"] * oop["esi"] + u["n_marketplace"] * oop["ng_sub"] + u["n_medicaid"] * oop["medicaid"]
              + u["n_medicare"] * oop["medicare"]
              + max(n - u["n_employer_cov"] - u["n_marketplace"] - u["n_medicaid"] - u["n_medicare"], 0)
              * oop["uninsured"])
        today, plan, _ = PU.visible_U(agi, fs, n, kind, prem if kind == "job" else 0.0,
                                      oo + (prem if kind != "job" else 0.0), o, R.fpl200(n),
                                      PU.earn_unit(u) * igrow, price)
        ok = plan <= today
        for b in bands:
            if b[0] <= agi < b[1]:
                res[b][0] += u["weight"]
                res[b][1] += u["weight"] * ok
        bk = bykind.setdefault(kind, [0.0, 0.0])
        bk[0] += u["weight"]
        bk[1] += u["weight"] * ok
        if agi < R.fpl200(n):
            low[0] += u["weight"]
            low[1] += u["weight"] * ok
    tot = sum(v[0] for v in res.values())
    return dict(by_agi={f"{int(b[0] / 1e3)}-{int(min(b[1], 1e9) / 1e3)}K": 100 * v[1] / v[0] for b, v in res.items()},
                by_kind={k: 100 * v[1] / v[0] for k, v in bykind.items()},
                all=100 * sum(v[1] for v in res.values()) / tot, below_200fpl=100 * low[1] / low[0],
                below_200fpl_share=100 * low[0] / tot)


def low_grid(ctx, o):
    _, oop = R._setup_visible(ctx)
    price = ctx["price_2040"]
    out = {}
    for hh_, fs, n in (("single", "single", 1), ("family", "joint", 4)):
        for agi in (15000, 25000, 40000, 55000):
            for kind in ("job", "uninsured", "medicaid", "own"):
                if kind == "job":
                    prem, oo = R.KFF_SHARE[hh_] * R.REAL_HEALTH_2040, oop["esi"] * n
                elif kind == "uninsured":
                    prem, oo = 0.0, oop["uninsured"] * n
                elif kind == "medicaid":
                    prem, oo = 0.0, oop["medicaid"] * n
                else:
                    sub = R._aca_share(agi, n)
                    full = R.MKT_PREM[hh_]
                    prem = (min(full, sub) if sub is not None else full) * R.REAL_HEALTH_2040
                    oo = oop["ng_sub"] * n
                today, plan, hi = PU.visible_U(agi, fs, n, kind, prem if kind == "job" else 0.0,
                                               oo + (prem if kind != "job" else 0.0), o, R.fpl200(n), agi, price)
                out[f"{hh_} {agi} {kind}"] = dict(today=round(today), prem=round(prem), oop=round(oo), hi=round(hi),
                                                  plan=round(plan), passes=plan <= today)
    return out


def price_W(ctx, case, spec, lost, r, s):
    with WLine(ctx, r, s) as info:
        out = PU.price_U(ctx, case, dict(spec, second=1.0), lost)
        o = dict(first=0.0, second=1.0)
        out["low_grid"] = low_grid(ctx, o)
    out.update(R=r, S=s, line=info, sur_2026=SUR26)
    out.pop("rate", None)
    return out


def main():
    PU.take_home_U = take_home_W
    ctx = HF.context()
    case = R.cost_cases(R._g40())["design"]
    E = R.PACKAGES2["E"][2]
    o_m4 = R.health_package(ctx, case, dict(E, second=4.0))   # hx_kept does not depend on the household tier
    lost = PU.lost_revenue(ctx, o_m4)
    prev = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "outU30.json")))
    t288, t507 = prev["M4"]["reassigned"], prev["U2"]["reassigned"]
    res = {"lost": lost, "targets": (t288, t507)}
    plan = {"W1": dict(s=2.0, target=t288), "W2": dict(s=4.0, target=t288), "W3": dict(r=3.0, target=t288),
            "W4": dict(s=4.0, target=t507)}
    for k, p in plan.items():
        r, s = solve(ctx, case, E, lost, p["target"], p.get("r"), p.get("s"))
        capped = False
        if s > S_CAP:
            s, capped = S_CAP, True
        res[k] = price_W(ctx, case, E, lost, r, s)
        res[k]["capped"] = capped
        res[k]["target"] = p["target"]
    # the take-home check on M4 and U2 for the below-200% share, for reference
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
