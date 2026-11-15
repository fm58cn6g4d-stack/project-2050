"""Health financing for the stage E settlement checkpoint memo: who pays for health care now and under the single plan,
what each financing option yields in FY2040, and what it does to households by income.

Role: the analysis behind `dossiers/foundations/checkpoint-financing.md` (part B) and its memos F1 to F3
(`dossiers/foundations/memos/`). Status: exploratory analysis, revised November 15, 2026: the household tables charge
the income contribution's statutory amount on its own base (AGI above the line) and put the budget model's avoidance
allowance where avoidance happens (`avoidance_key`); a lower-rate package with a two-tier contribution
(`packages`, `memo_options`); and the full accounting of national health spending by payer, today and under the plan
(`reconciliation`). It books nothing and changes no adopted input; every figure is project arithmetic on the project's
own models, not an official score.

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

# Where the budget model's avoidance allowance (assumptions.json, `tax.additional_yield_haircut`, 20% of the static
# yield) falls, by D3 quintile: weights on each quintile's share of the statutory charge (working assumption, memo part
# B3). Central: none below the top fifth. The base is AGI, so itemized deductions cannot shrink it; withheld,
# third-party-reported wages are misreported at about 1% against 55% for income nobody reports (IRS, EV-CAR-719); and
# the measured response of income below the top is small (broad income: about zero; taxable income 0.11 to 0.18) against
# 0.57 at the top (Gruber and Saez, EV-CAR-720). "elastic" puts Gruber and Saez's taxable-income elasticities on every
# quintile (an upper bound for the middle; Q1-Q3 are below their $50,000 line in 1992 dollars, Q4 between, Q5 above);
# "even" is the first draft's method (an even share of the shortfall on every dollar of base), shown for comparison.
AVOID_WEIGHTS = {"central": (0.0, 0.0, 0.0, 0.0, 1.0), "elastic": (0.18, 0.18, 0.18, 0.11, 0.57),
                 "even": (1.0, 1.0, 1.0, 1.0, 1.0)}
# The top 1%'s share of the broad base on IRS data (sensitivity): tax year 2022, the top 1% of returns had 22.4% of
# $14.75T of AGI (EV-CAR-721); less the lines (about $18,000/$36,000 in 2022 dollars, most of it below the top half),
# about 29% of the base above them, against the CPS's 12% (the CPS top-codes). Project arithmetic, approximate.
TOP1_BASE_SHARE_IRS = 29.0
# CBO's February 2026 baseline, Table 3-2 (EV-CAR-718): Medicare's FY2032 mandatory outlays and offsetting receipts
# (premiums and other payments, mostly enrollees' Part B and D premiums, with the states' Part D payments), $ billion.
CBO_MEDICARE_GROSS_2032 = 1866.597
CBO_MEDICARE_RECEIPTS_2032 = 340.393


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


def reconciliation(g40):
    """National health spending by who pays it, today and under the plan before its new financing, at the coverage
    model's full scale (2032, decided variant), with both columns adding to national health spending; the part of
    today's spending on the four lines the plan takes over (Medicare, Medicaid, private insurance, out of pocket) that
    the model names no payer for, split into what is real spending with a real payer and what is a seam in the
    model's own accounts; and the same table on FY2040's scale. $ billion."""
    hp = HB.health_path()
    HP, I, B, P = hp["HP"], hp["I"], hp["B"], hp["P"]
    M = HP.M
    S = B["S"]
    full = HP.model_full(I, B, P)
    sp = full["single_payer"]
    _, _, _, f = HP.groups(I, B, P)
    ltc, ltc_fed = f["medicaid_ltc_kept"], f["medicaid_ltc_kept_federal"]
    R = f["state_moe"]
    hh0 = M.run(I, {}, B)["household"]
    hh1 = full["household"]
    emp = full["private_flows_removed_bn"]["employer_premiums"]
    unins0 = sum(B["cells0"]["uninsured"])
    new_n = max(0.0, unins0 - I["sp_residual_unins"] * B["pop"])
    displaced = new_n * max(0.0, B["unins_total_pp"] - B["oop_pp"]["unins"]) / 1000
    fed0 = I["sub_medicare"] + I["sub_medicaid"] + I["sub_ptc"]
    st0 = S["medicaid"] - I["sub_medicaid"]
    four = S["medicare"] + S["medicaid"] + S["phi"] + S["oop"]
    unassigned = four - fed0 - st0 - emp - hh0["total_bn"]
    today = {"federal": fed0, "states": st0, "employers": emp, "households": hh0["total_bn"],
             "unassigned": unassigned, "other": S["other"]}
    plan = {"federal": sp["plan_outlay_bn"] - R + ltc_fed, "states": R + ltc - ltc_fed, "employers": 0.0,
            "households": hh1["total_bn"], "unassigned": 0.0, "other": S["other"] - displaced}
    # the unassigned part, line by line
    src_ = hh0["by_source"]
    prem = {s: src_[s]["people"] * src_[s]["premium_pp"] / 1000 for s in src_}
    oop_counted = sum(src_[s]["people"] * src_[s]["oop_pp"] / 1000 for s in src_)
    medicare_prem = sum(v for s, v in prem.items() if s.startswith("medicare"))
    g = B["gross"]
    overlap = (g["esi"] + g["ng_sub"] + g["ng_unsub"] - sum(B["cells0"]["esi"]) - sum(B["cells0"]["ng_sub"])
               - sum(B["cells0"]["ng_unsub"])) * B["P_phi"] / 1000
    phi_left = S["phi"] - emp - prem["esi"] - prem["ng_sub"] - prem["ng_unsub"] - I["sub_ptc"]
    cbo_net = CBO_MEDICARE_GROSS_2032 - CBO_MEDICARE_RECEIPTS_2032
    seam = {
        "medicare_cms_above_cbo": S["medicare"] - CBO_MEDICARE_GROSS_2032,
        "medicare_outside_subsidy_table": cbo_net - I["sub_medicare"],
        "medicare_receipts_not_counted": CBO_MEDICARE_RECEIPTS_2032 - medicare_prem,
        "private_premiums_people_counted_twice": overlap,
        "private_premiums_other": phi_left - overlap,
        "out_of_pocket_other": S["oop"] - oop_counted,
    }
    assert abs(sum(seam.values()) - unassigned) < 1e-6
    model_gap = seam["medicare_cms_above_cbo"] + seam["medicare_outside_subsidy_table"]
    real = unassigned - model_gap
    # what a Medicare dollar costs in the plan (repricing, more use, administration, less copays), to price the gap
    k = HP.groups(I, B, P)[1]["medicare"]
    S2 = dict(S, medicare=S["medicare"] - 1.0)
    B2 = dict(B, S=S2)
    k2 = HP.groups(I, B2, P)[1]["medicare"]
    per_dollar = k - k2
    # CMS's figure above CBO's is priced through the plan; the spending outside CBO's subsidy table is federal money the
    # plan replaces but the booking does not credit
    fed_gap_2032 = seam["medicare_cms_above_cbo"] * per_dollar + seam["medicare_outside_subsidy_table"]
    change = {k_: plan[k_] - today[k_] for k_ in today}
    out = dict(today_2032=today, plan_2032=plan, change_2032=change,
               nhe_2032=dict(today=sum(today.values()), plan=sum(plan.values()), model_today=B["nhe0"],
                             model_plan=full["nhe_bn"]),
               displaced_2032=displaced, unassigned_2032=unassigned, seam_2032=seam, model_gap_2032=model_gap,
               real_unassigned_2032=real, medicare_dollar_in_plan=per_dollar, federal_cost_high_by_2032=fed_gap_2032,
               scale_2040=g40,
               today_2040={k_: v * g40 for k_, v in today.items()}, plan_2040={k_: v * g40 for k_, v in plan.items()},
               federal_cost_high_by_2040=fed_gap_2032 * g40)
    # the identity: new federal spending = what every other payer stops paying, less the national saving
    out["identity_2032"] = dict(
        new_federal=change["federal"], households=-change["households"], employers=-change["employers"],
        states=-change["states"], unassigned=unassigned, others_uncompensated_care=displaced,
        national_saving=-(sum(plan.values()) - sum(today.values())))
    return out


def per_point(gap):
    """FY2040 yields per point ($ billion), on the budget model's own parameters."""
    A = json.load(open(os.path.join(HERE, "recovery-budget", "assumptions.json")))
    t, e = A["tax"], A["education"]
    gdp_ratio = gap["gdp_2040"] / gap["gdp_2034"]
    broad = (1 - t["additional_yield_haircut"]) * t["broad_threshold_per_point_2034_bn"] * gdp_ratio
    high = (1 - t["additional_yield_haircut"]) * t["high_threshold_per_point_2034_bn"] * gdp_ratio
    payroll_gross = e["payroll_per_point_2030_bn"] * (1 + e["payroll_growth"]) ** (Y - 2030)
    vat = VAT_POINT_DECADE_TN * 1000 / 10 * gdp_ratio   # the decade's average year taken as FY2034's scale
    return dict(broad_income=broad, high_income=high, payroll_gross=payroll_gross, vat=vat, gdp_ratio=gdp_ratio,
                haircut=t["additional_yield_haircut"])


# ---- the household side ----------------------------------------------------------------------------------------

def _line_rule(single, joint):
    """AGI above a line ($ single, $ joint) in 2025 dollars, price-indexed to the model year: the base of the budget
    model's income contributions (assumptions.json, `tax.note`: broad above $20,000/$40,000, high above
    $100,000/$200,000)."""
    def rule(u, L):
        from params import econ
        f = econ("cpiu", L["year"] - 1) / econ("cpiu", 2024)
        line = (joint if u["t_fs"] == "joint" else single) * f
        return max(u["t_agi"] - line, 0.0)
    return rule


_income_line_rule = _line_rule(20000, 40000)


def avoidance_key(K, base_key, weights):
    """Where the avoidance allowance on `base_key`'s contribution falls: each quintile's share of the statutory charge
    times its weight (AVOID_WEIGHTS), normalized; the top 1% takes its share of the top fifth's part in proportion to
    its share of the charge there."""
    sh, t1 = K[base_key]
    w = [s * x for s, x in zip(sh, weights)]
    q = [100 * x / sum(w) for x in w]
    return q, (q[4] * t1 / sh[4] if sh[4] else 0.0)


def keys():
    """D3 quintile keys (percent of the amount by quintile, and the top 1%'s share) on the 2029 households, the FY2040
    household count, and each quintile's FY2040 incomes on three measures: expanded income (the D3 ranking measure:
    cash income plus the employer's payroll tax), AGI, and the broad contribution's base (AGI above the line)."""
    import budget
    import provisions as P
    from params import econ
    B = budget.baseline(2029)
    K, _ = P.model_keys(B)
    P.RULES["income_line"] = _income_line_rule
    P.RULES["income_high"] = _line_rule(100000, 200000)
    P.RULES["agi"] = lambda u, L: u["t_agi"]
    K["income_line"] = P.micro_shares(B, "rule:income_line")
    hs, _ = P.micro_shares(B, "rule:income_high")
    K["income_high"] = (hs, K["surtax"][1])   # the top 1%'s share: keys.csv's surtax convention (the CPS top-codes)
    for name, w in AVOID_WEIGHTS.items():
        K[f"avoid_{name}"] = avoidance_key(K, "income_line", w)
        K[f"avoid_high_{name}"] = avoidance_key(K, "income_high", w)
    g = (econ("households", 2036) / econ("households", 2032)) ** 0.25 - 1
    hh2040 = P.mid_window_households(B) * (1 + g) ** (Y - 2034.5)
    gap = plan_gap()
    gdp_2029 = float(next(r for r in _read("models/data/recovery-budget-paths.csv")
                          if r["case"] == "mixed" and r["year"] == "2029")["gdp_bn"])
    n29 = sum(h["weight"] for h in B["households"])
    grow = gap["gdp_2040"] / gdp_2029 / (hh2040 / n29)    # nominal GDP per household, 2029 to FY2040
    H = B["households"]
    vals = {"agi": P.household_base(B, "rule:agi"), "base": P.household_base(B, "rule:income_line")}
    groups = [(f"Q{q}", lambda h, q=q: h["g5"] == q) for q in range(1, 6)] + [("T1", lambda h: h["top1"])]
    inc = {m: {} for m in ("expanded", "agi", "base")}
    for g_, sel in groups:
        w = sum(h["weight"] for h in H if sel(h))
        inc["expanded"][g_] = grow * sum(h["weight"] * h["expanded"] for h in H if sel(h)) / w
        for m in ("agi", "base"):
            inc[m][g_] = grow * sum(h["weight"] * vals[m][h["hh"]] for h in H if sel(h)) / w
    cps_base_2040 = grow * sum(h["weight"] * vals["base"][h["hh"]] for h in H) * hh2040 / n29 / 1e9
    return K, hh2040, inc, cps_base_2040


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


def income_rows(collected, pp, tier="broad", avoid="central", label="Health contribution on income"):
    """An income contribution that collects `collected` ($ billion, after the avoidance allowance) as two rows: the
    statutory charge (the rate times the base before any response, on the base's own key) and the tax not collected
    because of avoidance and reduced reporting (the allowance, on the avoidance key). The two net to `collected`."""
    h = pp["haircut"]
    statutory = collected / (1 - h)
    key = "income_line" if tier == "broad" else "income_high"
    akey = f"avoid_{avoid}" if tier == "broad" else f"avoid_high_{avoid}"
    return [(f"{label}: the statutory charge", -statutory, key),
            (f"{label}: less what avoidance keeps from being collected ({round(100 * h)}%)", statutory * h, akey)]


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


def finish(o, K, hh):
    o["households"] = per_household(o["rows"], K, hh)
    o["detail"] = [(label, round(bn), per_household([(label, bn, key)], K, hh)) for label, bn, key in o["rows"]]
    o["avoidance_range"] = {}
    for alt in ("elastic", "even"):
        rows = [(lb, bn, k.replace("_central", f"_{alt}")) for lb, bn, k in o["rows"]]
        o["avoidance_range"][alt] = per_household(rows, K, hh)
    return o


# The recommended package (memo part B4): employers at 100% of former premiums, on payroll after the endpoint (F2 C);
# states at 100% (F3 C); households on a two-tier income contribution (F1 D): a second tier of SECOND_TIER points on AGI
# above $100,000/$200,000 (the budget model's high line, on top of its 4 booked points), and a first tier on AGI above
# $20,000/$40,000 that closes the rest (about 10% at the recommendation).
SECOND_TIER = 4.7
REC = dict(emp_share=1.0, emp_base="payroll", state_share=1.0, side="D")
# Combined top federal rate on wages before health's contribution, with the plan's booked measures: the 39.6% bracket
# (G9 reverses the 2025 cuts above $450,000), Medicare's and the investment tax at 5% above $400,000 (H1b), and the
# booked 4 points above $100,000/$200,000 and 2 above $20,000/$40,000 (part A2). Project arithmetic.
TOP_RATE_BEFORE_HEALTH = 39.6 + 5.0 + 4.0 + 2.0


def household_side(side, collected, pp, second=SECOND_TIER, high_avoid=None):
    """Memo F1's household-side options, collecting `collected` ($ billion after avoidance). Returns (rows, rates)."""
    if side == "A":
        return income_rows(collected, pp), (collected / pp["broad_income"], 0.0)
    if side == "B":
        return [("Worker payroll contribution", -collected, "wages")], (collected / pp["payroll_gross"], 0.0)
    if side == "C":
        half = collected / 2
        rebate = 0.25 * half   # a per-person rebate of a quarter of the VAT's yield, paid from it
        return (income_rows(half, pp) + [("VAT, gross", -(half + rebate), "consumption"),
                                          ("Per-person rebate", rebate, "persons")],
                (half / pp["broad_income"], (half + rebate) / pp["vat"]))
    if side == "D":
        h = pp["haircut"] if high_avoid is None else high_avoid
        statutory2 = second * pp["high_income"] / (1 - pp["haircut"])     # the second tier's charge before response
        got2 = statutory2 * (1 - h)
        first = (collected - got2) / pp["broad_income"]
        rows = income_rows(collected - got2, pp, label="First tier") + [
            ("Second tier: the statutory charge", -statutory2, "income_high"),
            (f"Second tier: less what avoidance keeps from being collected ({round(100 * h)}%)", statutory2 * h,
             "avoid_high_central")]
        return rows, (first, second)
    raise ValueError(side)


def package(fl, need, pp, K, hh, point, emp_share, emp_base, state_share, side, savings=0.0, label="",
            second=SECOND_TIER, high_avoid=None):
    """A whole health financing package, FY2040: the employer side at `emp_share` of former premiums on `emp_base`,
    the states at `state_share`, optional savings booked against the need, and the household side `side` (F1) closing
    the rest."""
    emp, emp_net = employer_rows(fl, emp_share, emp_base)
    extra = (state_share - STATE_SHARE_BOOKED) * 10 * point
    rest = need - savings - emp_net - extra
    inc, rates = household_side(side, rest, pp, second, high_avoid)
    o = finish(dict(label=label, emp_share=emp_share, emp_base=emp_base, state_share=state_share, side=side,
                    savings=savings, rest=rest, employer_net=emp_net, state_extra=extra, rates=rates,
                    payroll_rate=emp_share * fl["fy2040"]["employers"] / pp["payroll_gross"],
                    states_relief=fl["fy2040"]["states"] - extra, rows=relief_rows(fl) + emp + inc), K, hh)
    o["bottom_four_ahead"] = min(o["households"][g] for g in GROUPS[:4]) > 0
    # the health contribution's points on a top earner's last dollar of pay (a VAT is left out: it is not on pay)
    o["top_rate_on_wages"] = TOP_RATE_BEFORE_HEALTH + rates[0] + (rates[1] if side == "D" else 0.0)
    return o


def memo_options(fl, need, pp, K, hh, point):
    """Memos F1 to F3: each fork's options with the other two at the recommended package (REC)."""
    f1 = {s: package(fl, need, pp, K, hh, point, REC["emp_share"], REC["emp_base"], REC["state_share"], s)
          for s in "ABCD"}
    f2 = {k: package(fl, need, pp, K, hh, point, share, base, REC["state_share"], REC["side"])
          for k, share, base in [("A", 0.65, "payroll"), ("B", 0.65, "premiums"), ("C", 1.0, "payroll"),
                                 ("D", 0.0, "payroll")]}
    f3 = {k: package(fl, need, pp, K, hh, point, REC["emp_share"], REC["emp_base"], share, REC["side"])
          for k, share in [("A", 0.5), ("B", 0.8), ("C", 1.0), ("D", 0.0)]}
    return f1, f2, f3


def packages(fl, need, pp, K, hh, point, sens):
    """The package choice (memo part B4): the first draft's recommendation on the corrected method, and the lower-rate
    package (employers and states at 100%) with one rate, with two tiers (recommended), and with two tiers and the
    states at 80%; then sensitivities on the recommended package."""
    savings = -(sens["admin_3pct"] + sens["drugs_23pct"])     # FY2040, positive = less need
    P = {
        "A": package(fl, need, pp, K, hh, point, 0.65, "payroll", 0.8, "A",
                     label="The first draft's: employers 65%, states 80%, one income rate"),
        "B": package(fl, need, pp, K, hh, point, 1.0, "payroll", 1.0, "A",
                     label="Lower rate: employers 100%, states 100%, one income rate"),
        "C": package(fl, need, pp, K, hh, point, 1.0, "payroll", 1.0, "D",
                     label="Lower rate, two tiers: employers 100%, states 100%"),
        "D": package(fl, need, pp, K, hh, point, 1.0, "payroll", 0.8, "D",
                     label="Two tiers, states kept at 80%: employers 100%"),
    }
    S = {
        "C_with_savings": package(fl, need, pp, K, hh, point, 1.0, "payroll", 1.0, "D", savings=savings),
        "B_with_savings": package(fl, need, pp, K, hh, point, 1.0, "payroll", 1.0, "A", savings=savings),
        "A_with_savings": package(fl, need, pp, K, hh, point, 0.65, "payroll", 0.8, "A", savings=savings),
        # the second tier loses 60% of its static yield to avoidance instead of 20% (its base is mostly the top 1%)
        "C_top_avoidance_60": package(fl, need, pp, K, hh, point, 1.0, "payroll", 1.0, "D", high_avoid=0.6),
    }
    return P, S, savings


def first_tier_search(fl, need, pp, K, hh, point, emp_share, state_share, savings=0.0):
    """For the lower-rate package: each second-tier rate from 0 in 1-point steps up to the point where the first tier
    would vanish, with the first tier that closes the rest, and whether every fifth below the top comes out ahead."""
    rows = []
    s = 0.0
    while True:
        o = package(fl, need, pp, K, hh, point, emp_share, "payroll", state_share, "D", savings=savings, second=s)
        if o["rates"][0] < 0:
            break
        rows.append(dict(first=o["rates"][0], second=s, top_rate=o["top_rate_on_wages"], households=o["households"],
                         ahead=o["bottom_four_ahead"]))
        s += 1.0
    return rows


def passthrough_check(fl, pkg, K, hh, pp, p=0.5):
    """If employers pass only `p` of their net premium saving (what they stop paying less their contribution) into pay
    (Anand, EV-CAR-299: compensation moves about $0.52 per dollar of premium), the rest stays as profit: workers who had
    coverage lose that pay and its tax, owners gain it less corporate tax (21%), and the federal side makes up the lost
    tax with a higher household contribution (first tier, or the single rate). FY2040, per household."""
    f = fl["fy2040"]
    gross = pkg["emp_share"] * f["employers"]
    kept = (1 - p) * max(f["employers"] - gross, 0.0)
    hx_rate = f["hx_gross"] / f["employers"]
    lost_tax = kept * (hx_rate - 0.21)
    rows = [("Pay that does not rise", -kept, "employer_cov"), ("Tax not paid on it", kept * hx_rate, "exclusion_end"),
            ("Profit kept, after corporate tax", kept * (1 - 0.21), "capital")] + income_rows(lost_tax, pp)
    d = per_household(rows, K, hh)
    return dict(kept=kept, lost_tax=lost_tax, extra_points=lost_tax / pp["broad_income"],
                households={g: pkg["households"][g] + d[g] for g in d})


def topcode_check(pkg, K, hh, top1_share=TOP1_BASE_SHARE_IRS):
    """The broad tier's statutory charge re-keyed with the top 1% at its IRS share of the base (TOP1_BASE_SHARE_IRS)
    instead of the CPS's, the difference taken from the other households in proportion (a sensitivity)."""
    sh, t1 = K["income_line"]
    scale = (100 - top1_share) / (100 - t1)
    q = [s * scale for s in sh[:4]] + [sh[4] * scale + (top1_share - t1 * scale)]
    K2 = dict(K, income_line=(q, top1_share))
    rows = [r for r in pkg["rows"]]
    return per_household(rows, K2, hh)


def run():
    gap = plan_gap()
    need = health_need()
    fl = flows()
    base, sens = sensitivities()
    pp = per_point(gap)
    K, hh, incomes, cps_base = keys()
    g = need["net"] / base       # the booking's FY2040 over the model's 2032 net (care 6-cost.md scales the same way)
    point = STATE_POINT_2032 * fl["g_2040"]
    sens40 = {k: v * fl["g_2040"] for k, v in sens.items()}
    f1, f2, f3 = memo_options(fl, need["net"], pp, K, hh, point)
    P, S, savings = packages(fl, need["net"], pp, K, hh, point, sens40)
    before = per_household(relief_rows(fl), K, hh)
    # the broad tier's statutory base, as the budget model's yield implies it, per household (package A's rate)
    a = P["A"]
    statutory_a = a["rest"] / (1 - pp["haircut"])
    base_2040 = statutory_a / (a["rates"][0] / 100)
    sh, t1 = K["income_line"]
    implied_base = {g_: base_2040 * 1e9 * s / 100 / (hh * 0.2) for g_, s in zip(GROUPS, sh)}
    implied_base["T1"] = base_2040 * 1e9 * t1 / 100 / (hh * 0.01)
    return dict(gap=gap, need={k: v for k, v in need.items() if k not in ("lines", "decade")}, flows=fl,
                sensitivities_2040=sens40, savings_2040=savings, per_point=pp,
                households_2040=hh, keys={k: K[k] for k in ("health_hh", "employer_cov", "exclusion_end", "wages",
                                                          "income_line", "income_high", "avoid_central",
                                                          "avoid_elastic", "avoid_even", "avoid_high_central",
                                                          "consumption", "persons")},
                before_financing=before,
                incomes_2040={m: {k: round(v) for k, v in d.items()} for m, d in incomes.items()},
                base_2040=dict(statutory_bn=base_2040, cps_grown_bn=cps_base, per_household=implied_base,
                               statutory_charge_bn=statutory_a, avoided_bn=statutory_a * pp["haircut"]),
                state_point_2040=point, f1=f1, f2=f2, f3=f3, packages=P, package_sensitivities=S,
                second_tier_search=first_tier_search(fl, need["net"], pp, K, hh, point, 1.0, 1.0),
                passthrough={k: passthrough_check(fl, P[k], K, hh, pp) for k in P},
                topcode={k: topcode_check(P[k], K, hh) for k in P},
                reconciliation=reconciliation(fl["g_2040"]),
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
    print("Stop paying FY2040:", {k: round(v) for k, v in fl["fy2040"].items()})
    print("Per point FY2040:", {k: round(v, 2) for k, v in pp.items()})
    print("Sensitivities FY2040:", {k: round(v) for k, v in r["sensitivities_2040"].items()})
    print(f"Households FY2040 {r['households_2040'] / 1e6:.1f}M; state point {r['state_point_2040']:.1f}")
    print("Incomes FY2040:", r["incomes_2040"])
    b = r["base_2040"]
    print(f"Broad base FY2040: {b['statutory_bn']:.0f} (CPS grown {b['cps_grown_bn']:.0f}); per household",
          {k: round(v) for k, v in b["per_household"].items()})
    rc = r["reconciliation"]
    for col in ("today_2032", "plan_2032", "change_2032", "today_2040", "plan_2040"):
        print(col, {k: round(v) for k, v in rc[col].items()}, round(sum(rc[col].values())))
    print("Unassigned 2032:", {k: round(v) for k, v in rc["seam_2032"].items()}, round(rc["unassigned_2032"]),
          "model gap", round(rc["model_gap_2032"]), "displaced", round(rc["displaced_2032"]),
          f"federal cost high by {rc['federal_cost_high_by_2032']:.0f} (2032), {rc['federal_cost_high_by_2040']:.0f}"
          " (FY2040)")
    print("Identity 2032:", {k: round(v) for k, v in rc["identity_2032"].items()})
    for name in ("packages", "package_sensitivities", "f1", "f2", "f3"):
        for k, o in r[name].items():
            print(name, k, [round(x, 2) for x in o["rates"]], f"payroll {o['payroll_rate']:.2f}",
                  f"top {o['top_rate_on_wages']:.1f}", o["households"], "ahead" if o["bottom_four_ahead"] else "")
    print("Package A detail:")
    for d in r["packages"]["A"]["detail"]:
        print("  ", d)
    print("Package C detail:")
    for d in r["packages"]["C"]["detail"]:
        print("  ", d)
    print("Avoidance ranges A:", r["packages"]["A"]["avoidance_range"], "C:", r["packages"]["C"]["avoidance_range"])
    print("Half pass-through:", {k: (round(v["extra_points"], 2), v["households"]) for k, v in r["passthrough"].items()})
    print("Top 1% at IRS share:", r["topcode"])
    for s in r["second_tier_search"]:
        print("second tier", s["second"], round(s["first"], 2), round(s["top_rate"], 1), s["households"], s["ahead"])


if __name__ == "__main__":
    main()
