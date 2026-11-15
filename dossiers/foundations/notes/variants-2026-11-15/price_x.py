"""Design X: W's structure (R% of all AGI plus S points above $205,400/$256,750) with a low-income exemption: none at
or below 138% of poverty, phased in linearly in AGI/FPL to the full rate at 200% (charge = R% x AGI x
(AGI/FPL - 1.38)/0.62 in the band). Reassignment may go negative (a surplus). Run from models/tools; nothing in the
repository is changed."""
import json
import os
import sys

sys.path.insert(0, ".")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import health_cost_review as R  # noqa: E402
import health_financing as HF  # noqa: E402
import price_u as PU  # noqa: E402
import price_w as PW  # noqa: E402

LO, HI = 1.38, 2.00
CUR = {"n": 1, "exempt": True}


def fpl(n):
    return R.fpl200(n) / 2


def phase(agi, n):
    if not CUR["exempt"]:
        return 1.0
    x = agi / fpl(max(n, 1))
    return 0.0 if x <= LO else (1.0 if x >= HI else (x - LO) / (HI - LO))


def contribution_X(agi, fs, o):
    j = "joint" if fs == "joint" else "single"
    return (PW.CUR["R"] / 100 * max(agi, 0.0) * phase(agi, CUR["n"])
            + PW.CUR["S"] / 100 * max(agi - PW.SUR26[j], 0.0))


_vis = PU.visible_U


def visible_X(agi, fs, persons, *a, **k):
    CUR["n"] = persons
    return _vis(agi, fs, persons, *a, **k)


def comp_base(ctx, r, s):
    _, _, _, _, X = HF.keys()
    igrow = X["grow"] / ctx["price_2040"]
    tot = 0.0
    for u in X["B"]["units"]:
        a = u["t_agi"] * igrow
        j = "joint" if u["t_fs"] == "joint" else "single"
        tot += u["weight"] * (r * max(a, 0.0) * phase(a, u["n_people"]) + s * max(a - PW.SUR26[j], 0.0))
    return tot / 1e9


class XLine(PW.WLine):
    def __enter__(self):
        import provisions as P
        ctx, r, s = self.ctx, self.r, self.s
        K, _, _, _, X = HF.keys()
        B, vals = X["B"], X["vals"]
        igrow = X["grow"] / ctx["price_2040"]
        old = R.LINE_HIGH
        b_old = sum(u["weight"] * max(u["t_agi"] * igrow - old["joint" if u["t_fs"] == "joint" else "single"], 0.0)
                    for u in X["B"]["units"]) / 1e9
        ratio = comp_base(ctx, r, s) / b_old
        sur = HF._line_rule(PW.SUR25["single"], PW.SUR25["joint"])
        P.RULES["x_comp"] = lambda u, L: (r * max(u["t_agi"], 0.0) * phase(u["t_agi"] * igrow, u["n_people"])
                                          + s * sur(u, L))
        sh, t1_cps = P.micro_shares(B, "rule:x_comp")
        self.keep = {k: K[k] for k in K if k == "income_high" or k.startswith("avoid_high_")}
        self.keep_v = dict(vals["high"])
        self.keep_pp = ctx["pp"]
        self.keep_c = R.contribution
        t1 = min(K["income_high"][1] * (r + s) / ratio, sh[4])
        K["income_high"] = (sh, t1)
        for a, w in HF.AVOID_WEIGHTS.items():
            K[f"avoid_high_{a}"] = HF.avoidance_key(K, "income_high", w)
        vals["high"].clear()
        vals["high"].update(P.household_base(B, "rule:x_comp"))
        ctx["pp"] = dict(self.keep_pp, high_income=self.keep_pp["high_income"] * ratio)
        PW.CUR.update(R=r, S=s)
        R.contribution = contribution_X
        return dict(ratio=ratio, pp_comp=ctx["pp"]["high_income"], t1=t1, t1_cps=t1_cps, shares=sh)


def price_X(ctx, case, spec, lost, r, s):
    with XLine(ctx, r, s) as info:
        out = PU.price_U(ctx, case, dict(spec, second=1.0), lost)
        out["low_grid"] = PW.low_grid(ctx, dict(first=0.0, second=1.0))
    out.update(R=r, S=s, line=info)
    out.pop("rate", None)
    return out


def main():
    PU.take_home_U = PW.take_home_W
    PU.visible_U = visible_X
    ctx = HF.context()
    case = R.cost_cases(R._g40())["design"]
    E = R.PACKAGES2["E"][2]
    o_m4 = R.health_package(ctx, case, dict(E, second=4.0))
    lost = PU.lost_revenue(ctx, o_m4)
    orig = R.health_package

    def hp(*a, **k):                       # let reassignment go negative: the tier stays as set
        R.max = lambda x, y: x
        try:
            return orig(*a, **k)
        finally:
            R.__dict__.pop("max", None)
    R.health_package = hp
    res = {"lost": lost}
    pp_hi = ctx["pp"]["high_income"]
    for k, (r, s) in {"X1": (4.0, 5.0), "X2": (4.0, 4.0), "X3": (3.0, 5.0)}.items():
        res[k] = price_X(ctx, case, E, lost, r, s)
        # the exemption's cost: the yield (after the 20% haircut) at R without it, less with it
        CUR["exempt"] = False
        full = comp_base(ctx, r, 0.0)
        CUR["exempt"] = True
        ex = comp_base(ctx, r, 0.0)
        res[k]["exemption_cost_bn"] = (full - ex) * res[k]["line"]["pp_comp"] / comp_base(ctx, r, s)
        res[k]["exemption_cost_statutory_bn"] = res[k]["exemption_cost_bn"] / (1 - ctx["pp"]["haircut"])
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
