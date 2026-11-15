"""Price package E with the household tier at 6% of AGI above $40,000 (V1: per return; V2: $40K single / $80K couple).
Run from models/tools. No repository files are changed; the swap is in memory, restored in `finally`."""
import json
import sys

sys.path.insert(0, ".")
import health_cost_review as R  # noqa: E402
import health_financing as HF  # noqa: E402


UNCLIP = False


def price(ctx, case, spec):
    if UNCLIP:   # let reassignment go negative (a surplus) so the tier stays at its set rate; scoped to this call
        R.max = lambda a, b: a
    try:
        o = R.health_package(ctx, case, spec)
    finally:
        R.__dict__.pop("max", None)
    m = HF.micro(ctx, o)
    th = R.take_home_micro(ctx, o)
    G = R.grid(ctx, o)
    grid = {f"{g['household']} {g['agi']}": (round(g["today"]), round(g["plan"]))
            for g in G if g["kind"] == "job" and g["agi"] in (55000, 72000, 90000, 110000, 150000)}
    return dict(second=o["second"], household_collected=o["household_collected"], credit=o["credit_bn"],
                reassigned=o["reassigned"], plan_gap_2040=70.0 + o["reassigned"], households=o["households"],
                losers=m["bottom_four_losers_m"], losers5=m["bottom_four_lose_5pct_m"],
                losers_by_fifth={q: round(m[q]["losers_m"], 2) for q in HF.GROUPS},
                take_home_all=th["all"], take_home=th["by_agi"], by_kind=th["by_kind"], kind_share=th["kind_share"], T=R.household_T(ctx, o), grid=grid,
                check=R._sources(ctx, o, case)["check"])


def micro_base(ctx, single, joint):
    """sum weight x max(AGI grown to FY2040 (2026 $) - line, 0) over the household model's tax units ($B)."""
    _, _, _, _, X = HF.keys()
    igrow = X["grow"] / ctx["price_2040"]
    tot = 0.0
    for u in X["B"]["units"]:
        line = joint if u["t_fs"] == "joint" else single
        tot += u["weight"] * max(u["t_agi"] * igrow - line, 0.0)
    return tot / 1e9


def variant(ctx, case, spec, name, single25, joint25):
    import provisions as P
    K, _, _, _, X = HF.keys()
    B, vals = X["B"], X["vals"]
    old_line = dict(R.LINE_HIGH)
    b_old = micro_base(ctx, old_line["single"], old_line["joint"])
    b_new = micro_base(ctx, single25 * 1.027, joint25 * 1.027)
    ratio = b_new / b_old
    # the spread: a new rule, the same form and indexing as income_high's (_line_rule(100000, 200000))
    P.RULES[name] = HF._line_rule(single25, joint25)
    sh, t1_cps = P.micro_shares(B, "rule:" + name)
    t1_leg = K["income_high"][1]
    t1 = t1_leg / ratio            # the top 1%'s dollars above the line held, the base scaled as the yield is
    keep = {k: K[k] for k in K if k == "income_high" or k.startswith("avoid_high_")}
    keep_v = dict(vals["high"])
    keep_pp = ctx["pp"]
    try:
        K["income_high"] = (sh, t1)
        for a, w in HF.AVOID_WEIGHTS.items():
            K[f"avoid_high_{a}"] = HF.avoidance_key(K, "income_high", w)
        vals["high"].clear()
        vals["high"].update(P.household_base(B, "rule:" + name))
        ctx["pp"] = dict(keep_pp, high_income=keep_pp["high_income"] * ratio)
        R.LINE_HIGH.update(single=single25 * 1.027, joint=joint25 * 1.027)
        out = price(ctx, case, spec)
    finally:
        K.update(keep)
        vals["high"].clear()
        vals["high"].update(keep_v)
        ctx["pp"] = keep_pp
        R.LINE_HIGH.update(old_line)
    out.update(base_old=b_old, base_new=b_new, ratio=ratio, pp_old=keep_pp["high_income"],
               pp_new=keep_pp["high_income"] * ratio, haircut=keep_pp["haircut"], fifth_shares=sh,
               fifth_shares_old=keep["income_high"][0], t1=t1, t1_cps=t1_cps, t1_old=t1_leg,
               line_2026=(single25 * 1.027, joint25 * 1.027))
    # check: the 2029 micro yield per point grown to FY2040 against the budget model's
    hh, n29 = ctx["hh"], X["n29"]
    out["micro_pp_old_fy40_net"] = 0.01 * b_old * hh / n29 * ctx["price_2040"] * (1 - keep_pp["haircut"])
    return out


def main():
    ctx = HF.context()
    g40 = R._g40()
    case = R.cost_cases(g40)["design"]
    E = R.PACKAGES2["E"][2]
    res = {"E": price(ctx, case, E)}
    res["E"].update(pp=ctx["pp"]["high_income"], haircut=ctx["pp"]["haircut"])
    for k, r in (("M4", 4.0), ("M5", 5.0), ("V2", 6.0)):
        res[k] = variant(ctx, case, dict(E, second=r), "income_40k_v2", 40000, 80000)
    res["E_again"] = price(ctx, case, E)          # restored state reproduces E
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
