"""Health financing for the stage E settlement checkpoint memo: who pays for health care now and under the single plan,
what each financing option yields in FY2040, and what it does to households by income.

Role: the analysis behind `dossiers/foundations/checkpoint-financing.md` (part B) and its memos F1 to F3
(`dossiers/foundations/memos/`). Status: exploratory analysis, November 14, 2026. It books nothing and changes no
adopted input; every figure is project arithmetic on the project's own models, not an official score.

What it reads (all read only):
  * the health coverage model through the care dossier's path (`dossiers/care/tools/health_path.py`) and the booking
    (`models/tools/health_booking.py`): national spending, the money that stops flowing, the household rows;
  * the budget model's generated files: the plan-wide gap (`models/data/recovery-budget-paths.csv`, case `mixed`) and
    the booked rows by line (`legacy/sources/recovery-budget-audit.csv`);
  * the budget model's per-point yields (`models/tools/recovery-budget/assumptions.json`: the broad income contribution
    above $20,000/$40,000 and the education fund's payroll point);
  * the household model's 2029 households (`models/tools/household/`): the D3 quintile keys.

Run: `python3 models/tools/health_financing.py` (prints the tables) or `--json`.
"""
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "household"))

import health_booking as HB  # noqa: E402

GROUPS = ["Q1", "Q2", "Q3", "Q4", "Q5"]
Y = 2040
HEALTH_ROWS = ("HLT-1", "HLT-2", "HLT-3", "HLT-4", "HLT-5", "HLT-6", "HLT-7", "HLT-8", "HX")
# HLT-4 holds health's safety-net parts and care's long-term care parts; care's 6-cost.md, part 5, gives health's
# share in FY2040 as 18.8 of the row's 21.1 ($ billion).
HLT4_HEALTH_2040 = 18.8

# Working assumptions of this analysis (each with its basis; the memo states them).
STATE_SHARE_BOOKED = 0.5   # memo 3 B's working figure (care 6-cost.md, part 4)
STATE_POINT_2032 = 45.0    # each 10 points of the states' share, $ billion in 2032 (care 6-cost.md, part 4)
VAT_POINT_DECADE_TN = 0.84 # a broad VAT, FY2030-39, per point: legacy menu 5% broad base $4.2T, before any rebate
                           # (legacy/domains/domain-revenue.md; checkpoint memo, first draft, part 4)


def _read(path):
    with open(os.path.join(ROOT, path), newline="") as f:
        return list(csv.DictReader(f))


def budget_lines():
    """FY2040 and FY2030-39 by audit line, case `mixed` ($ billion)."""
    y40, dec = {}, {}
    for r in _read("legacy/sources/recovery-budget-audit.csv"):
        if r["case"] != "mixed":
            continue
        y, v = int(r["year"]), float(r["primary_deficit_change_bn"])
        if y == Y:
            y40[r["line"]] = y40.get(r["line"], 0.0) + v
        if 2030 <= y <= 2039:
            dec[r["line"]] = dec.get(r["line"], 0.0) + v
    return y40, dec


def plan_gap():
    rows = {int(r["year"]): r for r in _read("models/data/recovery-budget-paths.csv") if r["case"] == "mixed"}
    gap = float(rows[Y]["agenda_gf_primary_bn"])
    return dict(gap_2040=gap, gdp_2040=float(rows[Y]["gdp_bn"]), gdp_2034=float(rows[2034]["gdp_bn"]),
                share=100 * gap / float(rows[Y]["gdp_bn"]),
                decade=sum(float(rows[y]["agenda_gf_primary_bn"]) for y in range(2030, 2040)))


def health_need():
    """The single plan's booked net cost in FY2040 (HLT-1 to HLT-8 and HX; HLT-4's health share only)."""
    y40, dec = budget_lines()
    spend = sum(y40.get(r, 0.0) for r in HEALTH_ROWS if r not in ("HX", "HLT-4")) + HLT4_HEALTH_2040
    return dict(spending=spend, hx=y40["HX"], net=spend + y40["HX"], lines=y40, decade=dec)


def flows():
    """Who pays: the coverage model's 2032 full-scale flows for the decided variant, and FY2040 on the booking's path."""
    hp = HB.health_path()
    HP, I, B, P = hp["HP"], hp["I"], hp["B"], hp["P"]
    full = HP.model_full(I, B, P)
    net, cost, today, f = HP.groups(I, B, P)
    hh = HB.household_removed(hp)
    inc = HB.incidence()
    S = B["S"]
    nhe0 = sum(S.values())
    ltc, ltc_fed = f["medicaid_ltc_kept"], f["medicaid_ltc_kept_federal"]
    state_mcd = S["medicaid"] - I["sub_medicaid"]                 # states' Medicaid spending, the model's basis
    state_moved = S["medicaid"] - ltc - (I["sub_medicaid"] - ltc_fed)
    g = inc["fy2040"]["H7w"] / inc["full_scale"]["employer_premiums"]  # FY2040 over 2032, HX's moved-share path
    out = dict(
        nhe_2032=dict(today=nhe0, plan=full["nhe_bn"], change=full["nhe_bn"] - nhe0),
        plan_2032=dict(gross=full["single_payer"]["plan_gross_bn"], copays=full["single_payer"]["cost_sharing_bn"],
                       outlay=full["single_payer"]["plan_outlay_bn"], admin=full["single_payer"]["admin_bn"],
                       new_use=full["single_payer"]["new_use_bn"], replaced_federal=I["sub_medicare"]
                       + (I["sub_medicaid"] - ltc_fed) + I["sub_ptc"], states=f["state_moe"],
                       net_spending=full["single_payer"]["plan_outlay_bn"] - f["state_moe"]
                       - (I["sub_medicare"] + I["sub_medicaid"] - ltc_fed + I["sub_ptc"]),
                       exclusion=I["sub_esi"], net_model=sum(net.values())),
        stop_paying_2032=dict(households=hh["total"], employers=inc["full_scale"]["employer_premiums"],
                              states=state_moved - f["state_moe"]),
        states_2032=dict(medicaid_today=state_mcd, moved=state_moved, pay=f["state_moe"], ltc_kept=ltc - ltc_fed),
        national_change_by_group_2032=dict(f["national_change"], newly_covered=full["single_payer"]["new_use_bn"]),
        tau=f["tau"], exclusion_rate_on_employer_premiums=I["sub_esi"] / inc["full_scale"]["employer_premiums"],
        g_2040=g,
        fy2040=dict(households=inc["fy2040"]["H7h"], employers=inc["fy2040"]["H7w"], hx_gross=inc["fy2040"]["H7x"],
                    states=(state_moved - f["state_moe"]) * g, nhe_change=(full["nhe_bn"] - nhe0) * g),
        by_group_2032=dict(today=today, plan=cost, net=net, people=f["people"]),
    )
    return out


def sensitivities():
    """Savings levers on the coverage model's groups (2032 full scale), scaled to FY2040 as care's 6-cost.md, part 6,
    does (FY2040 over 2032 on the decided path)."""
    hp = HB.health_path()
    HP, I, B, P = hp["HP"], hp["I"], hp["B"], hp["P"]
    base = sum(HP.groups(I, B, P)[0].values())
    out = {}
    for name, key, val in [("admin_3pct", "sp_admin", 0.03), ("admin_8pct", "sp_admin", 0.08),
                           ("drugs_23pct", "sp_drug_cut", 0.23), ("drugs_5pct", "sp_drug_cut", 0.05)]:
        J = dict(I)
        J[key] = val
        out[name] = sum(HP.groups(J, HP.M.build_base(J), P)[0].values()) - base
    return base, out


def per_point(gap):
    """FY2040 yields per point ($ billion), on the budget model's own parameters."""
    A = json.load(open(os.path.join(HERE, "recovery-budget", "assumptions.json")))
    t, e = A["tax"], A["education"]
    gdp_ratio = gap["gdp_2040"] / gap["gdp_2034"]
    broad = (1 - t["additional_yield_haircut"]) * t["broad_threshold_per_point_2034_bn"] * gdp_ratio
    payroll_gross = e["payroll_per_point_2030_bn"] * (1 + e["payroll_growth"]) ** (Y - 2030)
    vat = VAT_POINT_DECADE_TN * 1000 / 10 * gdp_ratio   # the decade's average year taken as FY2034's scale
    return dict(broad_income=broad, payroll_gross=payroll_gross, vat=vat, gdp_ratio=gdp_ratio)


# ---- the household side ----------------------------------------------------------------------------------------

def _income_line_rule(u, L):
    """AGI above $20,000 ($40,000 joint) in 2025 dollars, price-indexed to the model year: the base of the budget model's
    broad income contribution (assumptions.json, `tax.note`)."""
    from params import econ
    f = econ("cpiu", L["year"] - 1) / econ("cpiu", 2024)
    line = (40000 if u["t_fs"] == "joint" else 20000) * f
    return max(u["t_agi"] - line, 0.0)


def keys():
    """D3 quintile keys (percent of the amount by quintile, and the top 1%'s share) on the 2029 households, and the
    FY2040 household count."""
    import budget
    import provisions as P
    from params import econ
    B = budget.baseline(2029)
    K, _ = P.model_keys(B)
    P.RULES["income_line"] = _income_line_rule
    K["income_line"] = P.micro_shares(B, "rule:income_line")
    g = (econ("households", 2036) / econ("households", 2032)) ** 0.25 - 1
    hh2040 = P.mid_window_households(B) * (1 + g) ** (Y - 2034.5)
    gap = plan_gap()
    gdp_2029 = float(next(r for r in _read("models/data/recovery-budget-paths.csv")
                          if r["case"] == "mixed" and r["year"] == "2029")["gdp_bn"])
    n29 = sum(h["weight"] for h in B["households"])
    grow = gap["gdp_2040"] / gdp_2029 / (hh2040 / n29)    # nominal GDP per household, 2029 to FY2040
    H = B["households"]
    inc = {}
    for q in range(1, 6):
        w = sum(h["weight"] for h in H if h["g5"] == q)
        inc[f"Q{q}"] = grow * sum(h["weight"] * h["expanded"] for h in H if h["g5"] == q) / w
    w = sum(h["weight"] for h in H if h["top1"])
    inc["T1"] = grow * sum(h["weight"] * h["expanded"] for h in H if h["top1"]) / w
    return K, hh2040, inc


def per_household(rows, K, hh):
    """Net dollars per household in FY2040 by quintile and for the top 1%, for rows of (label, $ billion, key); a
    positive amount is a gain."""
    out = {g: 0.0 for g in GROUPS + ["T1"]}
    for _, bn, key in rows:
        sh, t1 = K[key]
        for g, s in zip(GROUPS, sh):
            out[g] += bn * 1e9 * s / 100 / (hh * 0.2)
        out["T1"] += bn * 1e9 * t1 / 100 / (hh * 0.01)
    return {g: round(v) for g, v in out.items()}


def relief_rows(fl):
    """Health before its financing, FY2040: premiums and out-of-pocket costs households stop paying, employer premiums
    that become pay (HX's full pass-through) and the tax on that pay (scenario Q-H7's rows)."""
    f = fl["fy2040"]
    return [("Premiums and out-of-pocket costs households stop paying", f["households"], "health_hh"),
            ("Employer premiums that become pay", f["employers"], "employer_cov"),
            ("Tax on that pay (HX)", -f["hx_gross"], "exclusion_end")]


def employer_rows(fl, share, base):
    """The employer side at `share` of former employer premiums. `base` 'premiums': a contribution on each employer's
    former premiums (HLT-7.18 as designed; borne by the workers who had the coverage, in place of the pay rise);
    'payroll': the same gross yield as a contribution on all pay (borne by all workers). Either way the pay that does
    not rise is not taxed, so HX falls by the exclusion's rate on it (care 6-cost.md, part 4)."""
    f = fl["fy2040"]
    gross = share * f["employers"]
    lost_hx = gross * fl["tau"]
    key = "employer_cov" if base == "premiums" else "wages"
    hx_key = "exclusion_end" if base == "premiums" else "wages"
    rows = [(f"Employer contribution, {round(100 * share)}% of former premiums ({base})", -gross, key),
            ("Less tax on pay that no longer rises", lost_hx, hx_key)]
    return rows, gross - lost_hx


def options(fl, need, pp, K, hh, state_extra):
    """Memo F1's household-side options, each with memo F2's recommended employer side (65%, on payroll after the
    endpoint) and memo F3's recommended states' share. Returns the yields, rates and household effects."""
    emp, emp_net = employer_rows(fl, 0.65, "payroll")
    rest = need - emp_net - state_extra
    base = relief_rows(fl) + emp
    out = {}
    pts = rest / pp["broad_income"]
    out["A"] = dict(label="Income-based health contribution (AGI above $20,000/$40,000)", rate=pts,
                    rows=base + [("Health contribution on income", -rest, "income_line")])
    pts_w = rest / pp["payroll_gross"]
    out["B"] = dict(label="Worker payroll contribution on all earnings", rate=pts_w,
                    rows=base + [("Worker payroll contribution", -rest, "wages")])
    half = rest / 2
    vat_pts = half / pp["vat"]
    rebate = 0.25 * half   # a per-person rebate of a quarter of the VAT's yield, paid from it
    out["C"] = dict(label="Half income contribution, half a VAT with a per-person rebate",
                    rate=(half / pp["broad_income"], vat_pts),
                    rows=base + [("Health contribution on income", -half, "income_line"),
                                 ("VAT, gross", -(half + rebate), "consumption"),
                                 ("Per-person rebate", rebate, "persons")])
    # D: the employer pays all of its former premiums (on payroll) and households the rest on income
    emp_d, emp_d_net = employer_rows(fl, 1.0, "payroll")
    rest_d = need - emp_d_net - state_extra
    out["D"] = dict(label="Employers pay all of their former premiums (payroll); households the rest on income",
                    rate=rest_d / pp["broad_income"],
                    rows=relief_rows(fl) + emp_d + [("Health contribution on income", -rest_d, "income_line")],
                    employer_net=emp_d_net)
    for o in out.values():
        o["households"] = per_household(o["rows"], K, hh)
        o["detail"] = [(label, round(bn), per_household([(label, bn, key)], K, hh)) for label, bn, key in o["rows"]]
    return dict(employer_net=emp_net, rest=rest, options=out)


def employer_options(fl, need, pp, K, hh, state_extra):
    """Memo F2: the employer side, each with the income-based household contribution (memo F1, A) closing the rest
    and memo F3's recommended states' share, FY2040."""
    out = {}
    for name, share, base in [("A", 0.65, "payroll"), ("B", 0.65, "premiums"), ("C", 1.0, "payroll"),
                              ("D", 0.0, "payroll")]:
        rows, net = employer_rows(fl, share, base)
        rest = need - net - state_extra
        rows = relief_rows(fl) + rows + [("Health contribution on income", -rest, "income_line")]
        out[name] = dict(share=share, base=base, net=net, income_points=rest / pp["broad_income"],
                         payroll_rate=share * fl["fy2040"]["employers"] / pp["payroll_gross"],
                         households=per_household(rows, K, hh))
    return out


def state_options(fl, need, pp, K, hh, emp_net):
    """Memo F3: the states' share; the federal income contribution adjusts. States' own taxes are not modeled."""
    point = STATE_POINT_2032 * fl["g_2040"]
    out = {}
    for name, share in [("A", 0.5), ("B", 0.8), ("C", 1.0), ("D", 0.0)]:
        extra = (share - STATE_SHARE_BOOKED) * 10 * point
        rest = need - emp_net - extra
        emp, _ = employer_rows(fl, 0.65, "payroll")
        rows = relief_rows(fl) + emp + [("Health contribution on income", -rest, "income_line")]
        out[name] = dict(share=share, extra=extra, states_relief=fl["fy2040"]["states"] - extra,
                         income_points=rest / pp["broad_income"], households=per_household(rows, K, hh))
    return out


def run():
    gap = plan_gap()
    need = health_need()
    fl = flows()
    base, sens = sensitivities()
    pp = per_point(gap)
    K, hh, incomes = keys()
    g = need["net"] / base       # the booking's FY2040 over the model's 2032 net (care 6-cost.md scales the same way)
    state_point_2040 = STATE_POINT_2032 * fl["g_2040"]
    state_extra = 3 * state_point_2040   # memo F3's recommendation: from 50% to 80%
    opts = options(fl, need["net"], pp, K, hh, state_extra)
    before = per_household(relief_rows(fl), K, hh)
    return dict(gap=gap, need={k: v for k, v in need.items() if k not in ("lines", "decade")}, flows=fl,
                sensitivities_2040={k: v * fl["g_2040"] for k, v in sens.items()}, per_point=pp,
                households_2040=hh, keys={k: K[k] for k in ("health_hh", "employer_cov", "exclusion_end", "wages",
                                                          "income_line", "consumption", "persons")},
                before_financing=before, incomes_2040={k: round(v) for k, v in incomes.items()}, state_point_2040=state_point_2040, state_extra=state_extra,
                f1=opts, f2=employer_options(fl, need["net"], pp, K, hh, state_extra),
                f3=state_options(fl, need["net"], pp, K, hh, opts["employer_net"]),
                payroll_rate_65=0.65 * fl["fy2040"]["employers"] / pp["payroll_gross"],
                rest_of_plan_2040=gap["gap_2040"] - need["net"], scale=g)


def main():
    r = run()
    if "--json" in sys.argv:
        print(json.dumps(r, indent=1, default=float))
        return
    gp, nd, fl, pp = r["gap"], r["need"], r["flows"], r["per_point"]
    print(f"Plan-wide gap FY2040 {gp['gap_2040']:.1f} ({gp['share']:.2f}% of GDP); FY2030-39 {gp['decade']:.0f}")
    print(f"Health net FY2040 {nd['net']:.1f} (spending {nd['spending']:.1f}, HX {nd['hx']:.1f}); "
          f"rest of plan {r['rest_of_plan_2040']:.1f}")
    n = fl["nhe_2032"]
    print(f"NHE 2032 today {n['today']:.0f}, plan {n['plan']:.0f}, change {n['change']:.0f}")
    print("Stop paying 2032:", {k: round(v) for k, v in fl["stop_paying_2032"].items()})
    print("Stop paying FY2040:", {k: round(v) for k, v in fl["fy2040"].items()})
    print("Plan 2032:", {k: round(v) for k, v in fl["plan_2032"].items()})
    print("States 2032:", {k: round(v) for k, v in fl["states_2032"].items()})
    print("Per point FY2040:", {k: round(v, 2) for k, v in pp.items()})
    print("Sensitivities FY2040:", {k: round(v) for k, v in r["sensitivities_2040"].items()})
    print(f"Households FY2040 {r['households_2040'] / 1e6:.1f}M; state point {r['state_point_2040']:.1f}; "
          f"payroll rate at 65% {r['payroll_rate_65']:.2f} points")
    print("Before financing:", r["before_financing"])
    print("Incomes FY2040:", r["incomes_2040"], "income key", r["keys"]["income_line"])
    for d in r["f1"]["options"]["A"]["detail"]:
        print("  A:", d)
    f1 = r["f1"]
    print(f"F1: employer net {f1['employer_net']:.0f}; rest {f1['rest']:.0f}")
    for k, o in f1["options"].items():
        print(k, o["label"], o["rate"], o["households"])
    for k, o in r["f2"].items():
        print("F2", k, round(o["net"]), round(o["income_points"], 2), round(o["payroll_rate"], 2), o["households"])
    for k, o in r["f3"].items():
        print("F3", k, round(o["extra"]), round(o["states_relief"]), round(o["income_points"], 2), o["households"])


if __name__ == "__main__":
    main()
