"""Design U: one personal health contribution on AGI above $40K/$80K (2025 $) replacing the worker's 1.45% HI and the
0.9% additional Medicare tax; the employer keeps M4's band contribution plus its 1.45% HI (one contribution, two
brackets). Run from models/tools. Nothing in the repository is changed; swaps are restored in `finally`."""
import json
import os
import sys

sys.path.insert(0, ".")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import health_cost_review as R  # noqa: E402
import health_financing as HF  # noqa: E402
import price_variant as PV  # noqa: E402

AMT_RATE, AMT_THR = 0.009, {"joint": 250000, "single": 200000}   # statutory, not indexed
S25, J25 = 40000, 80000
LOW = {"single": 20000 * 1.027, "joint": 40000 * 1.027}             # the booked 2 points' line, 2026 $


def fsj(fs):
    return "joint" if fs == "joint" else "single"


def earn_unit(u):
    return u["wage_h"] + u["wage_s"] + 0.9235 * (max(u["se_h"], 0) + max(u["se_s"], 0))


def worker_hi_today(earn, fs, price):
    """Worker HI and the additional Medicare tax, 2026 $ in FY2040 (threshold nominal, so /price)."""
    return 0.0145 * earn + AMT_RATE * max(earn - AMT_THR[fsj(fs)] / price, 0.0)


def visible_U(agi, fs, persons, kind, prem_share, oop, o, fpl, earn, price, low2=False):
    """Today: premium share + out of pocket + worker HI + 0.9%. Plan: unified contribution, copays and income and
    Social Security tax (6.2%, no HI) on the pay that used to be premiums. Returns today, plan, today's HI part."""
    hi = worker_hi_today(earn, fs, price)
    cp = 0.0 if (agi < fpl or kind == "medicaid") else R.COPAY_2040 * persons
    agi_plan = agi + (prem_share if kind == "job" else 0.0)
    tax_prem = prem_share * (R._marginal(max(agi_plan - R.STD[fsj(fs)], 0), fs) + 0.062) if kind == "job" else 0.0
    plan = R.contribution(agi_plan, fs, o) + cp + tax_prem
    if low2:
        plan += 0.02 * max(agi_plan - LOW[fsj(fs)], 0.0)
    return prem_share + oop + hi, plan, hi


def take_home_U(ctx, o):
    g, oop = R._setup_visible(ctx)
    K, _, _, _, X = HF.keys()
    price = ctx["price_2040"]
    hgrow = 1.048 ** 11 / price
    igrow = X["grow"] / price
    bands = [(0, 25e3), (25e3, 50e3), (50e3, 75e3), (75e3, 100e3), (100e3, 150e3), (150e3, 200e3), (200e3, 1e12)]
    res = {b: [0.0, 0.0] for b in bands}
    bykind = {}
    for u in X["B"]["units"]:
        earn = u["wage_h"] + u["wage_s"] + max(u["se_h"], 0) + max(u["se_s"], 0)
        if earn <= 0 or (u["age_h"] >= 65 and u["n_medicare"] > 0 and u["wage_h"] <= 0):
            continue
        agi = u["t_agi"] * igrow
        fs = fsj(u["t_fs"])
        n = max(u["n_people"], 1)
        kind = "job" if u["n_employer_cov"] > 0 else ("own" if u["n_marketplace"] > 0 else
                                                      ("medicaid" if u["n_medicaid"] > 0 else
                                                       ("medicare" if u["n_medicare"] > 0 else "uninsured")))
        prem = u["premiums_paid"] * hgrow
        oo = (u["n_employer_cov"] * oop["esi"] + u["n_marketplace"] * oop["ng_sub"] + u["n_medicaid"] * oop["medicaid"]
              + u["n_medicare"] * oop["medicare"]
              + max(n - u["n_employer_cov"] - u["n_marketplace"] - u["n_medicaid"] - u["n_medicare"], 0)
              * oop["uninsured"])
        today, plan, _ = visible_U(agi, fs, n, kind, prem if kind == "job" else 0.0,
                                   oo + (prem if kind != "job" else 0.0), o, R.fpl200(n), earn_unit(u) * igrow, price)
        ok = plan <= today
        for b in bands:
            if b[0] <= agi < b[1]:
                res[b][0] += u["weight"]
                res[b][1] += u["weight"] * ok
        bk = bykind.setdefault(kind, [0.0, 0.0])
        bk[0] += u["weight"]
        bk[1] += u["weight"] * ok
    tot = sum(v[0] for v in res.values())
    return dict(by_agi={f"{int(b[0] / 1e3)}-{int(min(b[1], 1e9) / 1e3)}K": 100 * v[1] / v[0] for b, v in res.items()},
                by_kind={k: 100 * v[1] / v[0] for k, v in bykind.items()},
                all=100 * sum(v[1] for v in res.values()) / tot)


def grid_U(ctx, o, low2=False):
    _, oop = R._setup_visible(ctx)
    price = ctx["price_2040"]
    out = {}
    for hh_, fs, n in (("single", "single", 1), ("family", "joint", 4)):
        for agi in (55000, 72000, 90000, 110000, 150000):
            prem = R.KFF_SHARE[hh_] * R.REAL_HEALTH_2040
            today, plan, hi = visible_U(agi, fs, n, "job", prem, oop["esi"] * n, o, R.fpl200(n), agi, price, low2)
            out[f"{hh_} {agi}"] = (round(today), round(plan), round(hi))
    return out


def T_U(ctx, o, low2=False):
    R._setup_visible(ctx)
    prem, oo = 2100 * R.REAL_HEALTH_2040, 1950 * R.REAL_HEALTH_2040
    agi = 72000 - 2100
    today, plan, hi = visible_U(agi, "single", 1, "job", prem, oo, o, R.fpl200(1), agi, ctx["price_2040"], low2)
    c = R.contribution(agi + prem, "single", o)
    return dict(today=today, today_hi=hi, plan=plan, contribution=c, copays=R.COPAY_2040,
                tax_on_premium=plan - c - R.COPAY_2040 - (0.02 * max(agi + prem - LOW["single"], 0) if low2 else 0))


def lost_revenue(ctx, o_m4):
    """FY2040 $B: worker HI on today's pay, the 0.9%, and worker HI on former pre-tax premiums (in HX)."""
    _, _, _, _, X = HF.keys()
    scale = ctx["hh"] / X["n29"] / 1e9
    grow = X["grow"]
    W_hf = HF.HI_RATE / 2 * ctx["pp"]["payroll_gross"]
    W_micro = sum(u["weight"] * 0.0145 * earn_unit(u) * grow for u in X["B"]["units"]) * scale
    amt_hh = {}
    a29 = 0.0
    for u in X["B"]["units"]:
        e = earn_unit(u)
        thr = AMT_THR[fsj(u["t_fs"])]
        amt_hh[u["hh"]] = amt_hh.get(u["hh"], 0.0) + AMT_RATE * max(e * grow - thr, 0.0)
        a29 += u["weight"] * AMT_RATE * max(e - thr, 0.0)
    A = sum(h["weight"] * amt_hh.get(h["hh"], 0.0) for h in X["H"]) * scale
    HF.household_key("amt_u", lambda h: amt_hh.get(h["hh"], 0.0))
    hxp = 0.0145 * o_m4["hx_kept"] / ctx["tau"]
    return dict(W=W_hf, W_micro=W_micro, A=A, A_2029_bn=a29 / 1e9, hxp=hxp, total=W_hf + A + hxp,
                payroll_gross=ctx["pp"]["payroll_gross"], tau=ctx["tau"], hx_kept=o_m4["hx_kept"])


def price_U(ctx, case, spec, lost):
    keep = ctx["need"]
    ctx["need"] = keep + lost["total"]
    try:
        o = R.health_package(ctx, case, spec)
    finally:
        ctx["need"] = keep
    o["rows"] = o["rows"] + [("Worker HI (1.45%) ends", lost["W"], "wages"),
                             ("Additional Medicare tax (0.9%) ends", lost["A"], "amt_u"),
                             ("Worker HI on former pre-tax premiums ends (HX)", lost["hxp"], "exclusion_end")]
    o["households"] = HF.per_household(o["rows"], ctx["K"], ctx["hh"])
    m = HF.micro(ctx, o)
    th = take_home_U(ctx, o)
    return dict(rate=o["second"], collected=o["household_collected"], reassigned=o["reassigned"],
                gap=70 + o["reassigned"], employer_rate_band=o["employer_rate_statutory"],
                employer_gross=o["employer_gross"], take_home=th, T=T_U(ctx, o), T2=T_U(ctx, o, True),
                grid=grid_U(ctx, o), grid2=grid_U(ctx, o, True),
                losers=m["bottom_four_losers_m"], losers5=m["bottom_four_lose_5pct_m"], households=o["households"])


def main():
    ctx = HF.context()
    case = R.cost_cases(R._g40())["design"]
    E = R.PACKAGES2["E"][2]
    res = {}
    with PV_line(ctx, "income_40k_v2", S25, J25) as info:
        o_m4 = R.health_package(ctx, case, dict(E, second=4.0))
        lost = lost_revenue(ctx, o_m4)
        res["lost"] = lost
        res["line"] = info
        # M4 for reference, in the old convention and in U's (both sides with worker HI)
        m4 = PV.price(ctx, case, dict(E, second=4.0))
        res["M4"] = dict(rate=4.0, collected=m4["household_collected"], reassigned=m4["reassigned"],
                         gap=m4["plan_gap_2040"], employer_rate_band=o_m4["employer_rate_statutory"],
                         employer_gross=o_m4["employer_gross"], take_home=dict(all=m4["take_home_all"],
                         by_agi=m4["take_home"], by_kind=m4["by_kind"]), T=m4["T"], grid=m4["grid"],
                         losers=m4["losers"], losers5=m4["losers5"])
        o4 = dict(first=0.0, second=4.0)
        res["M4"]["T2"] = R.household_T(ctx, o4)["plan"] + 0.02 * max(69900 + 2100 * R.REAL_HEALTH_2040 - LOW["single"], 0)
        g4 = {f"{g['household']} {g['agi']}": round(g["plan"] + 0.02 * max(g["agi"] + (R.KFF_SHARE[g["household"]]
              * R.REAL_HEALTH_2040) - LOW["single" if g["household"] == "single" else "joint"], 0))
              for g in R.grid(ctx, o4) if g["kind"] == "job" and g["agi"] in (55000, 72000, 90000, 110000, 150000)}
        res["M4"]["grid2"] = g4
        u2 = price_U(ctx, case, dict(E, second=5.0), lost)
        r1 = 5.0 + (u2["reassigned"] - res["M4"]["reassigned"]) / ctx["pp"]["high_income"]
        res["U1"] = price_U(ctx, case, dict(E, second=r1), lost)
        res["U2"] = u2
    with PV_line(ctx, "income_30k_60k", 30000, 60000) as info30:
        res["line30"] = info30
        pp30 = ctx["pp"]["high_income"]
        t = price_U(ctx, case, dict(E, second=5.0), lost)
        for name, target in (("U1-30", res["M4"]["reassigned"]), ("U2-30", u2["reassigned"])):
            r = 5.0 + (t["reassigned"] - target) / pp30
            res[name] = price_U(ctx, case, dict(E, second=r), lost)
    print(json.dumps(res, indent=1, default=float))


class PV_line:
    """The $40K/$80K line swapped in (as price_variant.variant does), restored on exit."""
    def __init__(self, ctx, name, s25, j25):
        self.a = (ctx, name, s25, j25)

    def __enter__(self):
        import provisions as P
        ctx, name, s25, j25 = self.a
        K, _, _, _, X = HF.keys()
        B, vals = X["B"], X["vals"]
        self.old_line = dict(R.LINE_HIGH)
        ratio = PV.micro_base(ctx, s25 * 1.027, j25 * 1.027) / PV.micro_base(ctx, self.old_line["single"],
                                                                             self.old_line["joint"])
        P.RULES[name] = HF._line_rule(s25, j25)
        sh, _ = P.micro_shares(B, "rule:" + name)
        self.keep = {k: K[k] for k in K if k == "income_high" or k.startswith("avoid_high_")}
        self.keep_v = dict(vals["high"])
        self.keep_pp = ctx["pp"]
        K["income_high"] = (sh, K["income_high"][1] / ratio)
        for a, w in HF.AVOID_WEIGHTS.items():
            K[f"avoid_high_{a}"] = HF.avoidance_key(K, "income_high", w)
        vals["high"].clear()
        vals["high"].update(P.household_base(B, "rule:" + name))
        ctx["pp"] = dict(self.keep_pp, high_income=self.keep_pp["high_income"] * ratio)
        R.LINE_HIGH.update(single=s25 * 1.027, joint=j25 * 1.027)
        return dict(ratio=ratio, pp_new=ctx["pp"]["high_income"], line_2026=(s25 * 1.027, j25 * 1.027))

    def __exit__(self, *exc):
        ctx = self.a[0]
        K, _, _, _, X = HF.keys()
        K.update(self.keep)
        X["vals"]["high"].clear()
        X["vals"]["high"].update(self.keep_v)
        ctx["pp"] = self.keep_pp
        R.LINE_HIGH.update(self.old_line)
        return False


if __name__ == "__main__":
    main()
