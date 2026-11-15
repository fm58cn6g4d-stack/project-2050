"""Health financing: who pays for health care now and under the single plan, year by year, and what each financing
package does to the federal budget and to households.

Role: the analysis behind `dossiers/foundations/health-financing.md`, the stage E memo that prices and finances the
single health plan (HLT-1 to HLT-8) from a fresh start; it replaces part B of `checkpoint-financing.md`. Status:
exploratory analysis, November 15, 2026. It books nothing and changes no adopted input; every figure is project
arithmetic on the project's own models, not an official score.

What it does, in order:
  * the coverage model's Medicare line rebased to CBO's February 2026 figure (`coverage(rebase=True)`): the project's
    baseline is CBO's (DEC-2026-11-08-03), and CMS's older projection, which the model starts from, is $157B higher
    in 2032. `seam()` runs the decided path both ways; the difference is what the booked federal cost reads high;
  * national health spending by payer, today and under the plan, with every dollar assigned to a named payer
    (`payers()`), at the 2032 full-scale year, in FY2040 and year by year FY2030-40 (`payer_path()`);
  * the amount to finance, year by year: the booked health rows (`legacy/sources/recovery-budget-audit.csv`, case
    `mixed`) with the seam taken out (`need_path()`);
  * the financing packages (`package()`), FY2040 and year by year, with rates a reader can multiply, the HX
    accounting, the employer side alone and with HI's 1.45%, and the top rate on wages;
  * households: per fifth and top 1% (D3 keys, `models/tools/household/keys.csv`), the spread inside each fifth
    and who loses (`micro()`), and worked examples (`examples()`).

What it reads (all read only): the care dossier's path (`dossiers/care/tools/health_path.py`) and the booking
(`health_booking.py`); the budget model's generated paths and audit; its per-point yields
(`models/tools/recovery-budget/assumptions.json`); the household model's 2029 households.

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
YEARS = list(range(2030, 2041))
HEALTH_ROWS = ("HLT-1", "HLT-2", "HLT-3", "HLT-5", "HLT-6", "HLT-7", "HLT-8", "HX")
HLT4_HEALTH_2040 = 18.8      # health's parts of HLT-4 in FY2040 (care 6-cost.md, part 5); the window is booking()'s
COVERAGE_GROUPS = ("medicare", "medicaid", "employer", "individual", "uninsured")

# ---- working assumptions (each stated in the memo) ------------------------------------------------------------
STATE_SHARE_BOOKED = 0.5     # memo 3 B's working figure (care 6-cost.md, part 4)
VAT_POINT_DECADE_TN = 0.84   # broad VAT per point, FY2030-39, before any rebate: CBO's 5% broad base, $4.2T (legacy menu)
# CBO's February 2026 baseline, Table 3-2 (EV-CAR-718): Medicare's FY2032 mandatory outlays and offsetting receipts.
CBO_MEDICARE_GROSS_2032 = 1866.597
CBO_MEDICARE_RECEIPTS_2032 = 340.393
# Federal coverage in the employer cell (FEHB, TRICARE, the VA): the booking lowers HX by 50 of the cell's 680 (2032;
# health_booking.FEDCOV_REVENUE_2032). The same share of the employer money is the government paying itself, so the
# premiums that become pay, HX and any employer contribution are all taken at (1 - 50/680) of the cell's figures.
FEDCOV_K = 1 - HB.FEDCOV_REVENUE_2032 / 680.0
# The combined top federal rate on wages before health, with the plan's decided and booked measures (statutory, both
# halves of payroll taxes, as legacy/domains/domain-revenue.md, "Combined top rates"): 39.6% income tax (G9), 12.4%
# Social Security above $250,000 (SS-1, DEC-2026-11-12-06), 5% Medicare (H1b), and the booked income contributions,
# 4 points above $100,000/$200,000 and 2 above $20,000/$40,000. The handover notes' 50.6% left out SS-1.
TOP_RATE_BEFORE_HEALTH = 39.6 + 12.4 + 5.0 + 4.0 + 2.0
# Share of all pay below the Social Security wage base, person by person: the CPS gives 0.863 (wages_cap over wages,
# household model, 2029); the CPS top-codes earnings (the top 1% has 9% of wages in it against the legacy key's 12%),
# so take 3 points off. Working assumption for the capped employer base.
CAP_SHARE = 0.83
# Where the avoidance allowance (assumptions.json `tax.additional_yield_haircut`, 20%) falls (handover notes, part
# 2): central none below the top fifth (IRS tax gap, EV-CAR-719; Gruber and Saez, EV-CAR-720); "elastic" Gruber and
# Saez's taxable-income elasticities by fifth; "even" the first draft's method.
AVOID_WEIGHTS = {"central": (0.0, 0.0, 0.0, 0.0, 1.0), "elastic": (0.18, 0.18, 0.18, 0.11, 0.57),
                 "even": (1.0, 1.0, 1.0, 1.0, 1.0)}
TOP1_BASE_SHARE_IRS = 29.0   # the top 1%'s share of the broad base on IRS data (EV-CAR-721), approximate
TOP1_ELASTICITY = 0.25       # top-1% elasticity of reported income for the stacking check (Saez, Slemrod and Giertz's
                             # range 0.12-0.4; working figure)
FIRST_TIER_TARGET = 5.5      # Espen's "mid single digits" (November 15), the middle of the lead's 5-6%
VAT_REBATE_SHARE = 0.25      # a per-person rebate of a quarter of the VAT's gross yield, paid from it


def _read(path):
    with open(os.path.join(ROOT, path), newline="") as f:
        return list(csv.DictReader(f))


# ---- the budget side ---------------------------------------------------------------------------------------------

def audit_lines():
    """Booked rows by line and fiscal year, case `mixed` ($ billion; a cost positive)."""
    out = {}
    for r in _read("legacy/sources/recovery-budget-audit.csv"):
        if r["case"] != "mixed":
            continue
        y = int(r["year"])
        if 2030 <= y <= Y:
            d = out.setdefault(r["line"], {})
            d[y] = d.get(y, 0.0) + float(r["primary_deficit_change_bn"])
    return out


def paths():
    return {int(r["year"]): r for r in _read("models/data/recovery-budget-paths.csv") if r["case"] == "mixed"}


def plan_gap():
    rows = paths()
    gap = float(rows[Y]["agenda_gf_primary_bn"])
    return dict(gap_2040=gap, gdp_2040=float(rows[Y]["gdp_bn"]), gdp_2034=float(rows[2034]["gdp_bn"]),
                share=100 * gap / float(rows[Y]["gdp_bn"]),
                decade=sum(float(rows[y]["agenda_gf_primary_bn"]) for y in range(2030, 2040)),
                gdp={y: float(rows[y]["gdp_bn"]) for y in YEARS})


def per_point(gap, year=Y):
    """Yields per point in `year` ($ billion), on the budget model's own parameters. The broad and high income tiers
    are what is collected after the 20% allowance; the payroll point is gross."""
    with open(os.path.join(HERE, "recovery-budget", "assumptions.json")) as f:
        A = json.load(f)
    t, e = A["tax"], A["education"]
    r = gap["gdp"][year] / gap["gdp_2034"]
    return dict(broad_income=(1 - t["additional_yield_haircut"]) * t["broad_threshold_per_point_2034_bn"] * r,
                high_income=(1 - t["additional_yield_haircut"]) * t["high_threshold_per_point_2034_bn"] * r,
                payroll_gross=e["payroll_per_point_2030_bn"] * (1 + e["payroll_growth"]) ** (year - 2030),
                vat=VAT_POINT_DECADE_TN * 1000 / 10 * r, gdp_ratio=r, haircut=t["additional_yield_haircut"])


# ---- the coverage model, booked and rebased ------------------------------------------------------------------------

def coverage(rebase=True):
    """The decided variant on the coverage model; with `rebase`, Medicare's 2032 spending and its federal net are CBO's
    (gross mandatory outlays; gross less premiums and other receipts) instead of CMS's projection and the subsidy
    table. Returns a health_path()-like dict that health_booking's household functions accept."""
    hp = HB.health_path()
    if not rebase:
        return hp
    HP, I, B, P = hp["HP"], hp["I"], hp["B"], hp["P"]
    I2 = dict(I, sub_medicare=CBO_MEDICARE_GROSS_2032 - CBO_MEDICARE_RECEIPTS_2032)
    B2 = dict(B, S=dict(B["S"], medicare=CBO_MEDICARE_GROSS_2032),
              nhe0=B["nhe0"] - (B["S"]["medicare"] - CBO_MEDICARE_GROSS_2032))
    return dict(hp, I=I2, B=B2)


def seam():
    """The decided path's net federal cost (model basis, before the employer contribution) with Medicare as booked and
    rebased to CBO, by fiscal year; the difference is what the booked federal cost reads high ($ billion)."""
    out = {}
    for name, rb in (("booked", False), ("rebased", True)):
        c = coverage(rb)
        HP = c["HP"]
        s, _ = HP.path(c["I"], c["B"], c["P"], HP.rate_path(HP.hospital_start(c["I"], c["B"])))
        out[name] = {y: s[y]["total"] for y in YEARS}
    out["difference"] = {y: out["rebased"][y] - out["booked"][y] for y in YEARS}
    g = [HB.health_path()["HP"].groups(c["I"], c["B"], c["P"])[0] for c in (coverage(False), coverage(True))]
    out["by_group_2032"] = {k: g[1][k] - g[0][k] for k in g[0]}
    return out


def need_path(sm=None):
    """The amount to finance by fiscal year: the booked health rows (HLT-4's health parts only) and HX, as booked and
    with the seam taken out ($ billion)."""
    L = audit_lines()
    hlt4 = dict(zip(range(2030, 2040), HB.booking()["hlt4_path"]))
    hlt4[Y] = HLT4_HEALTH_2040
    sm = sm or seam()
    out = {}
    for y in YEARS:
        rows = {r: L.get(r, {}).get(y, 0.0) for r in HEALTH_ROWS}
        rows["HLT-4 (health's parts)"] = hlt4[y]
        spending = sum(v for k, v in rows.items() if k != "HX")
        out[y] = dict(rows=rows, spending=spending, hx=rows["HX"], booked=spending + rows["HX"],
                      seam=sm["difference"][y], net=spending + rows["HX"] + sm["difference"][y])
    return out


def _fy(cal):
    return {y: 0.25 * cal.get(y - 1, 0.0) + 0.75 * cal.get(y, 0.0) for y in YEARS}


def moved_shares(c):
    """Each coverage group's share in the plan by fiscal year times the model's growth (2032 = 1), on the booking's
    fiscal-year blend: the multiplier on a group's 2032 full-scale amount."""
    HP, I, B, P = c["HP"], c["I"], c["B"], c["P"]
    _, _, _, f = HP.groups(I, B, P)
    gf = c["gf"]
    cal = {k: {} for k in COVERAGE_GROUPS}
    for y in range(2029, Y + 1):
        sh = HP.shares_moved(y, f["child_share_moving"])
        sh["employer"] = HP.employer_share(y, f["child_share_employer"])
        for k in COVERAGE_GROUPS:
            cal[k][y] = sh[k] * gf.get(y, 0.0)
    return {k: _fy(v) for k, v in cal.items()}


def group_payers(c):
    """2032 full scale: each coverage group's change in spending by payer when it moves into the plan ($ billion; a
    fall negative). Federal is spending (the tax exclusion is HX, a revenue); 'other' is everything the model's payers
    leave over, named in payers()."""
    HP, I, B, P = c["HP"], c["I"], c["B"], c["P"]
    M = HP.M
    S = B["S"]
    net, cost, today, f = HP.groups(I, B, P)
    full = HP.model_full(I, B, P)
    hh = HB.household_removed(c)["by_group"]
    ltc, ltc_fed = f["medicaid_ltc_kept"], f["medicaid_ltc_kept_federal"]
    R = f["state_moe"]
    state_moved = S["medicaid"] - ltc - (I["sub_medicaid"] - ltc_fed)
    emp = full["private_flows_removed_bn"]["employer_premiums"]
    unins0 = sum(B["cells0"]["uninsured"])
    new_n = max(0.0, unins0 - I["sp_residual_unins"] * B["pop"])
    displaced = new_n * max(0.0, B["unins_total_pp"] - B["oop_pp"]["unins"]) / 1000
    nat_total = full["nhe_bn"] - B["nhe0"]
    nat = dict(f["national_change"])
    nat["uninsured"] = nat_total - sum(nat.values())
    fed = {"medicare": net["medicare"], "medicaid": net["medicaid"], "employer": cost["employer"],
           "individual": net["individual"], "uninsured": net["uninsured"]}
    out = {}
    for g in COVERAGE_GROUPS:
        d = dict(federal=fed[g], employers=-emp if g == "employer" else 0.0, households=-hh[g],
                 states=-(state_moved - R) if g == "medicaid" else 0.0,
                 uncompensated_care=-displaced if g == "uninsured" else 0.0)
        d["other"] = nat[g] - sum(d.values())
        d["national"] = nat[g]
        out[g] = d
    return out, dict(state_moved=state_moved, R=R, emp=emp, displaced=displaced, ltc=ltc, ltc_fed=ltc_fed,
                     tau=f["tau"], exclusion=I["sub_esi"], nat_total=nat_total)


def payers(c, g40):
    """National health spending by who pays it, today and under the plan before its new financing, 2032 full scale,
    both columns adding to national health spending, with every dollar on a named payer; and FY2040 at `g40` times
    2032. $ billion."""
    HP, I, B, P = c["HP"], c["I"], c["B"], c["P"]
    M = HP.M
    S = B["S"]
    full = HP.model_full(I, B, P)
    sp = full["single_payer"]
    _, x = group_payers(c)
    hh0, hh1 = M.run(I, {}, B)["household"], full["household"]
    src = hh0["by_source"]
    prem = {s: src[s]["people"] * src[s]["premium_pp"] / 1000 for s in src}
    oop_counted = sum(src[s]["people"] * src[s]["oop_pp"] / 1000 for s in src)
    medicare_prem = sum(v for s, v in prem.items() if s.startswith("medicare"))
    gr = B["gross"]
    overlap = (gr["esi"] + gr["ng_sub"] + gr["ng_unsub"] - sum(B["cells0"]["esi"]) - sum(B["cells0"]["ng_sub"])
               - sum(B["cells0"]["ng_unsub"])) * B["P_phi"] / 1000
    phi_left = S["phi"] - x["emp"] - prem["esi"] - prem["ng_sub"] - prem["ng_unsub"] - I["sub_ptc"]
    fed_net_medicare = CBO_MEDICARE_GROSS_2032 - CBO_MEDICARE_RECEIPTS_2032
    # today's spending on the four lines the plan takes over that the model's own payers don't cover, line by line
    lines = {
        "medicare_cms_above_cbo": S["medicare"] - CBO_MEDICARE_GROSS_2032,
        "medicare_outside_subsidy_table": fed_net_medicare - I["sub_medicare"],
        "medicare_other_receipts": CBO_MEDICARE_RECEIPTS_2032 - medicare_prem,
        "private_premiums_people_counted_twice": overlap,
        "private_premiums_other": phi_left - overlap,
        "out_of_pocket_other": S["oop"] - oop_counted,
    }
    fed0 = I["sub_medicare"] + I["sub_medicaid"] + I["sub_ptc"]
    st0 = S["medicaid"] - I["sub_medicaid"]
    four = S["medicare"] + S["medicaid"] + S["phi"] + S["oop"]
    unassigned = four - fed0 - st0 - x["emp"] - hh0["total_bn"]
    assert abs(sum(lines.values()) - unassigned) < 1e-6
    seam_ = lines["medicare_cms_above_cbo"] + lines["medicare_outside_subsidy_table"]
    # named payers for the real part (working split, stated in the memo): Medicare's other receipts are enrollees'
    # premiums above the model's $3,500 average and the states' Part D payments; double-counted private coverage is
    # premiums employers and workers pay (at the model's employer share of private premiums); the rest households'
    es = x["emp"] / (x["emp"] + prem["esi"])
    named = dict(households=lines["medicare_other_receipts"] + (1 - es) * lines["private_premiums_people_counted_twice"]
                 + lines["private_premiums_other"] + lines["out_of_pocket_other"],
                 employers=es * lines["private_premiums_people_counted_twice"])
    today = {"federal": fed0 + seam_, "states": st0, "employers": x["emp"] + named["employers"],
             "households": hh0["total_bn"] + named["households"], "others_uncompensated_care": x["displaced"],
             "other_health_spending": S["other"] - x["displaced"]}
    plan = {"federal": sp["plan_outlay_bn"] - x["R"] + x["ltc_fed"], "states": x["R"] + x["ltc"] - x["ltc_fed"],
            "employers": 0.0, "households": hh1["total_bn"], "others_uncompensated_care": 0.0,
            "other_health_spending": S["other"] - x["displaced"]}
    change = {k: plan[k] - today[k] for k in today}
    stop = {k: -change[k] for k in ("states", "employers", "households", "others_uncompensated_care")}
    out = dict(today_2032=today, plan_2032=plan, change_2032=change, lines_2032=lines, seam_2032=seam_,
               unassigned_2032=unassigned, named_split_2032=named, employer_share_private=es,
               nhe_2032=dict(today=sum(today.values()), plan=sum(plan.values()), model_today=B["nhe0"],
                             model_plan=full["nhe_bn"]),
               scale_2040=g40, today_2040={k: v * g40 for k, v in today.items()},
               plan_2040={k: v * g40 for k, v in plan.items()},
               identity_2032=dict(new_federal=change["federal"], others_stop_paying=sum(stop.values()),
                                  national_saving=sum(today.values()) - sum(plan.values()), **stop))
    return out


def payer_path(c, gp=None):
    """Year by year FY2030-40: the change in national health spending by payer as the waves move (model basis: the
    coverage groups only, before the booked items the model does not price), $ billion."""
    gp = gp or group_payers(c)[0]
    ms = moved_shares(c)
    keys = ("federal", "states", "employers", "households", "uncompensated_care", "other", "national")
    return {y: {k: sum(gp[g][k] * ms[g][y] for g in COVERAGE_GROUPS) for k in keys} for y in YEARS}


def flow_path(c):
    """By fiscal year: premiums and out-of-pocket costs households stop paying, employer premiums that stop (all
    employers, and without federal coverage), HX as booked, and the states' former Medicaid spending for the people
    who have moved ($ billion)."""
    inc = HB.incidence()
    hp = HB.health_path()
    hh = HB.household_removed(hp)
    HP, gf = hp["HP"], hp["gf"]
    cal = {}
    for y in range(2029, Y + 1):
        sh = HP.shares_moved(y)
        sh["employer"] = HP.employer_share(y, hp["kids"])
        cal[y] = sum(hh["by_group"][k] * sh[k] for k in hh["by_group"]) * gf.get(y, 0.0)
    h7h = _fy(cal)
    xf = HB.excl_full(hp)
    _, x = group_payers(c)
    ms = moved_shares(c)
    L = audit_lines()
    out = {}
    for y in YEARS:
        emp = hp["excl"][y] * hp["employer_premiums"] / xf
        out[y] = dict(households=h7h[y], employers_all=emp, employers=FEDCOV_K * emp, hx=-L["HX"].get(y, 0.0),
                      states_moved=x["state_moved"] * ms["medicaid"][y])
    assert abs(out[Y]["households"] - inc["fy2040"]["H7h"]) < 1e-6
    return out


def sensitivities(c):
    """Savings levers on the coverage model's groups (2032 full scale): administration and drug prices."""
    HP, I, B, P = c["HP"], c["I"], c["B"], c["P"]
    base = sum(HP.groups(I, B, P)[0].values())
    out = {}
    for name, key, val in [("admin_3pct", "sp_admin", 0.03), ("admin_8pct", "sp_admin", 0.08),
                           ("drugs_23pct", "sp_drug_cut", 0.23), ("drugs_5pct", "sp_drug_cut", 0.05)]:
        J = dict(I)
        J[key] = val
        B2 = HP.M.build_base(J)
        if "S" in B and B["S"]["medicare"] != B2["S"]["medicare"]:
            B2 = dict(B2, S=dict(B2["S"], medicare=B["S"]["medicare"]))
        out[name] = sum(HP.groups(J, B2, P)[0].values()) - base
    return base, out


# ---- households ----------------------------------------------------------------------------------------------------

def _line_rule(single, joint):
    def rule(u, L):
        from params import econ
        f = econ("cpiu", L["year"] - 1) / econ("cpiu", 2024)
        line = (joint if u["t_fs"] == "joint" else single) * f
        return max(u["t_agi"] - line, 0.0)
    return rule


def avoidance_key(K, base_key, weights):
    sh, t1 = K[base_key]
    w = [s * x for s, x in zip(sh, weights)]
    q = [100 * x / sum(w) for x in w]
    return q, (q[4] * t1 / sh[4] if sh[4] else 0.0)


_CACHE = {}


def keys():
    """D3 quintile keys, the FY2040 household count, incomes by fifth on three measures, the CPS-grown broad base,
    and the per-household values for the spread inside each fifth (micro())."""
    if "keys" in _CACHE:
        return _CACHE["keys"]
    import budget
    import provisions as P
    from params import econ
    B = budget.baseline(2029)
    K, _ = P.model_keys(B)
    P.RULES["income_line"] = _line_rule(20000, 40000)
    P.RULES["income_high"] = _line_rule(100000, 200000)
    P.RULES["agi"] = lambda u, L: u["t_agi"]
    K["income_line"] = P.micro_shares(B, "rule:income_line")
    hs, _ = P.micro_shares(B, "rule:income_high")
    K["income_high"] = (hs, K["surtax"][1])
    for name, w in AVOID_WEIGHTS.items():
        K[f"avoid_{name}"] = avoidance_key(K, "income_line", w)
        K[f"avoid_high_{name}"] = avoidance_key(K, "income_high", w)
    g = (econ("households", 2036) / econ("households", 2032)) ** 0.25 - 1
    hh2040 = P.mid_window_households(B) * (1 + g) ** (Y - 2034.5)
    gap = plan_gap()
    gdp_2029 = float(paths()[2029]["gdp_bn"])
    H = B["households"]
    n29 = sum(h["weight"] for h in H)
    grow = gap["gdp_2040"] / gdp_2029 / (hh2040 / n29)
    vals = {"agi": P.household_base(B, "rule:agi"), "base": P.household_base(B, "rule:income_line"),
            "high": P.household_base(B, "rule:income_high")}
    sel = [(f"Q{q}", lambda h, q=q: h["g5"] == q) for q in range(1, 6)] + [("T1", lambda h: h["top1"])]
    inc = {m: {} for m in ("expanded", "agi", "base")}
    for g_, s in sel:
        w = sum(h["weight"] for h in H if s(h))
        inc["expanded"][g_] = grow * sum(h["weight"] * h["expanded"] for h in H if s(h)) / w
        for m in ("agi", "base"):
            inc[m][g_] = grow * sum(h["weight"] * vals[m][h["hh"]] for h in H if s(h)) / w
    cps_base = grow * sum(h["weight"] * vals["base"][h["hh"]] for h in H) * hh2040 / n29 / 1e9
    _CACHE["keys"] = (K, hh2040, inc, cps_base, dict(B=B, H=H, n29=n29, grow=grow, vals=vals))
    return _CACHE["keys"]


def per_household(rows, K, hh):
    """Net dollars per household in FY2040 by fifth and for the top 1%, for rows of (label, $ billion, key)."""
    out = {g: 0.0 for g in GROUPS + ["T1"]}
    for _, bn, key in rows:
        sh, t1 = K[key]
        for g, s in zip(GROUPS, sh):
            out[g] += bn * 1e9 * s / 100 / (hh * 0.2)
        out["T1"] += bn * 1e9 * t1 / 100 / (hh * 0.01)
    return {g: round(v) for g, v in out.items()}


def income_rows(collected, pp, tier="broad", avoid="central", label="Health contribution on income", h=None):
    """An income contribution that collects `collected` ($ billion) as the statutory charge (on the base's key) and
    the part avoidance keeps from being collected (on the avoidance key)."""
    h = pp["haircut"] if h is None else h
    statutory = collected / (1 - h)
    key = "income_line" if tier == "broad" else "income_high"
    akey = f"avoid_{avoid}" if tier == "broad" else f"avoid_high_{avoid}"
    return [(f"{label}: the statutory charge", -statutory, key),
            (f"{label}: less what avoidance keeps from being collected ({round(100 * h)}%)", statutory * h, akey)]


def relief_rows(f40):
    """Health before its financing, FY2040 (aligned with the booking: federal coverage out of the employer money)."""
    return [("Premiums and out-of-pocket costs households stop paying", f40["households"], "health_hh"),
            ("Employer premiums that become pay", f40["employers"], "employer_cov"),
            ("Tax on former premiums, both shares (HX)", -f40["hx"], "exclusion_end")]


def employer_rows(f40, tau, share, base):
    """The employer side at `share` of former premiums (private and state and local employers). `base`: 'premiums'
    (on each employer's former premiums, HLT-7.18; borne by the workers who had the coverage), 'payroll' (all pay, the
    HI base) or 'payroll_cap' (pay up to the Social Security wage base, person by person). Pay that does not rise is
    not taxed, so HX falls by the exclusion's rate on it."""
    gross = share * f40["employers"]
    key = {"premiums": "employer_cov", "payroll": "wages", "payroll_cap": "wages_cap"}[base]
    hx_key = "exclusion_end" if base == "premiums" else key
    return [(f"Employer health contribution, {round(100 * share)}% of former premiums ({base})", -gross, key),
            ("Less tax on pay that no longer rises (HX falls)", gross * tau, hx_key)], gross * (1 - tau)


def employer_rate(f40, share, base, pp):
    """The employer contribution as a rate on pay: all employers' former premiums over all pay (uncapped) or over pay
    below the wage base. Federal payroll pays it too, intragovernmentally."""
    r = share * f40["employers_all"] / pp["payroll_gross"]
    return r / CAP_SHARE if base == "payroll_cap" else r


def package(ctx, emp_share=1.0, emp_base="payroll", state_share=1.0, first=None, second=0.0, close="first",
            vat_rebate=VAT_REBATE_SHARE, savings=0.0, label="", need=None, f40=None, pp=None, high_avoid=None):
    """A whole health financing package, FY2040 (or another year, with `need`, `f40` and `pp` for it). The closing
    item (`close`: 'first' tier, 'vat', 'second' tier or 'employer' share) is solved so the package covers the need
    exactly; the others are as given."""
    need = ctx["need"] if need is None else need
    f40 = ctx["f40"] if f40 is None else f40
    pp = ctx["pp"] if pp is None else pp
    tau, K, hh = ctx["tau"], ctx["K"], ctx["hh"]
    point = 0.1 * f40["states_moved"]
    extra = (state_share - STATE_SHARE_BOOKED) * 10 * point
    h2 = pp["haircut"] if high_avoid is None else high_avoid
    got2 = second * pp["high_income"] / (1 - pp["haircut"]) * (1 - h2)
    first_got = (first or 0.0) * pp["broad_income"]
    if close == "employer":
        rest_emp = need - savings - extra - got2 - first_got
        emp_share = rest_emp / (f40["employers"] * (1 - tau))
    emp, emp_net = employer_rows(f40, tau, emp_share, emp_base)
    rest = need - savings - emp_net - extra
    vat_gross = 0.0
    if close == "first":
        first_got = rest - got2
        first = first_got / pp["broad_income"]
    elif close == "vat":
        vat_gross = (rest - got2 - first_got) / (1 - vat_rebate)
    elif close == "second":
        got2 = rest - first_got
        second = got2 / (1 - h2) * (1 - pp["haircut"]) / pp["high_income"]
    rows = relief_rows(f40) + emp
    if first_got:
        rows += income_rows(first_got, pp, label="First tier")
    if got2:
        st2 = got2 / (1 - h2)
        rows += [("Second tier: the statutory charge", -st2, "income_high"),
                 (f"Second tier: less what avoidance keeps from being collected ({round(100 * h2)}%)", st2 * h2,
                  "avoid_high_central")]
    if vat_gross:
        rows += [("Value-added tax, gross", -vat_gross, "consumption"),
                 ("Per-person rebate", vat_gross * vat_rebate, "persons")]
    e_rate = employer_rate(f40, emp_share, emp_base, pp) if emp_base != "premiums" else 0.0
    o = dict(label=label, emp_share=emp_share, emp_base=emp_base, state_share=state_share, close=close,
             savings=savings, need=need, rest=rest, employer_gross=-emp[0][1], employer_net=emp_net,
             hx_kept=f40["hx"] - emp[1][1], state_extra=extra, first=first or 0.0, second=second,
             vat_rate=vat_gross / pp["vat"], vat_gross=vat_gross, vat_rebate=vat_rebate if vat_gross else 0.0,
             employer_rate=e_rate, employer_rate_with_hi=e_rate + 1.45 if e_rate else 0.0,
             household_collected=first_got + got2 + vat_gross * (1 - vat_rebate), rows=rows)
    o["top_rate_on_wages"] = TOP_RATE_BEFORE_HEALTH + o["first"] + o["second"]
    o["top_rate_with_employer"] = o["top_rate_on_wages"] + (e_rate if emp_base == "payroll" else 0.0)
    if K is not None:
        o["households"] = per_household(rows, K, hh)
        o["detail"] = [(lb, round(bn), per_household([(lb, bn, k)], K, hh)) for lb, bn, k in rows]
        o["avoidance_range"] = {alt: per_household([(lb, bn, k.replace("_central", f"_{alt}")) for lb, bn, k in rows],
                                                   K, hh) for alt in ("elastic", "even")}
        o["bottom_four_ahead"] = min(o["households"][g] for g in GROUPS[:4]) > 0
    return o


# The packages (memo part 4). Recommended: A. Every package puts the employer contribution on each worker's pay up to
# the Social Security wage base (memo part 3.1): like the premium it replaces, it does not rise with a top earner's
# pay, so it adds nothing to the top rate on wages; the uncapped HI base is a sensitivity.
PACKAGES = {
    "A": dict(label="Premiums become contributions: employers and states keep paying what they pay now; one "
                    "household contribution", emp_share=1.0, emp_base="payroll_cap", state_share=1.0, close="first"),
    "B": dict(label="Mid-single digits with a rebated value-added tax", emp_share=1.0, emp_base="payroll_cap",
              state_share=1.0, first=FIRST_TIER_TARGET, close="vat"),
    "C": dict(label="Mid-single digits with employers paying more than their former premiums", emp_base="payroll_cap",
              state_share=1.0, first=FIRST_TIER_TARGET, close="employer"),
    "D": dict(label="Mid-single digits with a top tier", emp_share=1.0, emp_base="payroll_cap", state_share=1.0,
              first=FIRST_TIER_TARGET, close="second"),
}


def package_path(ctx, spec, need_p, flows_p, gap):
    """A package year by year, FY2030-40: each source's yield on that year's movers, and the household side scaled to
    close each year's need in the FY2040 package's proportions, with its rates."""
    o40 = package(ctx, **spec)
    out = {}
    for y in YEARS:
        pp = per_point(gap, y)
        f = flows_p[y]
        need = need_p[y]["net"]
        point = 0.1 * f["states_moved"]
        extra = (o40["state_share"] - STATE_SHARE_BOOKED) * 10 * point
        emp_net = o40["emp_share"] * f["employers"] * (1 - ctx["tau"])
        sav = o40["savings"] * (need_p[y]["net"] / need_p[Y]["net"]) if o40["savings"] else 0.0
        rest = need - emp_net - extra - sav
        s = max(rest, 0.0) / o40["household_collected"] if o40["household_collected"] else 0.0
        out[y] = dict(need=need, employers=emp_net, employer_gross=o40["emp_share"] * f["employers"], states=extra,
                      savings=sav, households=rest, scale=s,
                      first=o40["first"] * s * ctx["pp"]["broad_income"] / pp["broad_income"],
                      second=o40["second"] * s * ctx["pp"]["high_income"] / pp["high_income"],
                      vat=o40["vat_rate"] * s * ctx["pp"]["vat"] / pp["vat"])
    return out


def micro(ctx, o):
    """The spread inside each fifth: every household's net effect, FY2040, each row's quintile amount spread over the
    fifth's households in proportion to the household's own amount of that row's base, so the fifths' averages are
    exactly per_household()'s. Returns losers by fifth (millions of FY2040 households, share) and their profile."""
    K, hh = ctx["K"], ctx["hh"]
    _, _, _, _, X = keys()
    H, n29, vals = X["H"], X["n29"], X["vals"]
    pp_ = ctx["pp_person"]
    def health(h):
        nm = h["n_medicaid"]
        nmc = h["n_medicare"]
        ne = h["n_employer_cov"]
        nk = h["n_marketplace"]
        nu = max(h["numper"] - nm - nmc - ne - nk, 0.0)
        return ne * pp_["esi"] + nk * pp_["ng"] + nm * pp_["medicaid"] + nmc * pp_["medicare"] + nu * pp_["uninsured"]
    base_of = {"health_hh": health, "employer_cov": lambda h: h["n_employer_cov"],
               "exclusion_end": lambda h: h["n_employer_cov"], "wages": lambda h: h["wages"],
               "wages_cap": lambda h: h["wages_capped"], "income_line": lambda h: vals["base"][h["hh"]],
               "income_high": lambda h: vals["high"][h["hh"]], "consumption": lambda h: max(h["expanded"], 0.0),
               "persons": lambda h: h["numper"], "capital": lambda h: max(h["capital"], 0.0)}
    for a in AVOID_WEIGHTS:
        base_of[f"avoid_{a}"] = base_of["income_line"]
        base_of[f"avoid_high_{a}"] = base_of["income_high"]
    scale = hh / n29
    net = {h["hh"]: 0.0 for h in H}
    for _, bn, key in o["rows"]:
        sh, _ = K[key]
        f = base_of[key]
        for q in range(1, 6):
            Hq = [h for h in H if h["g5"] == q]
            tot = sum(h["weight"] * f(h) for h in Hq)
            amt = bn * 1e9 * sh[q - 1] / 100
            for h in Hq:
                v = f(h) if tot > 0 else 1.0
                net[h["hh"]] += amt * v / ((tot if tot > 0 else sum(x["weight"] for x in Hq)) * scale)
    out = {}
    for q in range(1, 6):
        Hq = [h for h in H if h["g5"] == q]
        w = sum(h["weight"] for h in Hq)
        lw = sum(h["weight"] for h in Hq if net[h["hh"]] < 0)
        out[f"Q{q}"] = dict(losers_m=lw * scale / 1e6, share=100 * lw / w,
                            avg=sum(h["weight"] * net[h["hh"]] for h in Hq) / w)
    T = [h for h in H if h["top1"]]
    out["T1"] = dict(losers_m=sum(h["weight"] for h in T if net[h["hh"]] < 0) * scale / 1e6,
                     share=100 * sum(h["weight"] for h in T if net[h["hh"]] < 0) / sum(h["weight"] for h in T))
    L = [h for h in H if net[h["hh"]] < 0 and h["g5"] <= 4]
    lw = sum(h["weight"] for h in L) or 1.0
    prof = dict(
        medicare_only=sum(h["weight"] for h in L if h["n_medicare"] > 0 and h["n_employer_cov"] == 0) / lw,
        no_coverage_costs_counted=sum(h["weight"] for h in L if h["n_employer_cov"] + h["n_marketplace"]
                                      + h["n_medicare"] == 0) / lw,
        employer_coverage=sum(h["weight"] for h in L if h["n_employer_cov"] > 0) / lw,
        workers_without_job_coverage=sum(h["weight"] for h in L if h["wages"] > 0 and h["n_employer_cov"] == 0) / lw,
        median_loss=sorted(-net[h["hh"]] for h in L)[len(L) // 2] if L else 0.0)
    out["all_losers_m"] = sum(out[f"Q{q}"]["losers_m"] for q in range(1, 6))
    out["bottom_four_losers_m"] = sum(out[f"Q{q}"]["losers_m"] for q in range(1, 5))
    out["profile_bottom_four"] = prof
    return out


def stacking_check(o, K, pp, e=TOP1_ELASTICITY):
    """What the top 1%'s part of the contribution really adds at that top rate: the static charge on the top 1% falls
    with reported income, ((1 - t1) / (1 - t0)) ** e, and the income taxes already on that income fall with it (the
    fiscal externality), at the plan's top rate on wages before health (63%). Every health charge on the last dollar
    of pay counts, the employer contribution included when its base is uncapped. Returns the share of the top 1%'s
    static charge actually collected."""
    t0 = TOP_RATE_BEFORE_HEALTH / 100
    t1 = o["top_rate_with_employer"] / 100        # every health charge on a top earner's last dollar of pay
    shrink = (max(1 - t1, 0.0) / (1 - t0)) ** e
    d = t1 - t0
    collected = t1 * shrink - t0        # the new charges on the smaller base, less the old taxes lost on it
    return dict(shrink=shrink, static=d, collected=collected, share=collected / d if d else 0.0)


HEALTH_GROWTH = 0.054   # CMS's projection of national health spending, 2025-34, a year (EV-CAR-056)


def stacking_adjusted(ctx, spec, e=TOP1_ELASTICITY):
    """The package re-solved when the top 1% yields only what stacking_check() finds on the health charges at its
    margin (the first and second tiers, and the employer contribution when uncapped), instead of the central
    allowance: the shortfall is added to the need and the closing item re-solved. Returns (package, shortfall $B)."""
    o = package(ctx, **spec)
    K = ctx["K"]
    marginal = ("First tier: the statutory charge", "Second tier: the statutory charge")
    rows = [(lb, bn, k) for lb, bn, k in o["rows"] if lb in marginal
            or (o["emp_base"] == "payroll" and lb.startswith("Employer health contribution"))]
    static = sum(-bn * K[k][1] / 100 for _, bn, k in rows)
    credits = sum(bn * K[k][1] / 100 for lb, bn, k in o["rows"] if "avoidance keeps" in lb)
    assumed = static - credits
    share = stacking_check(o, K, ctx["pp"], e)["share"]
    lost = max(assumed - share * static, 0.0)
    return package(ctx, **dict(spec, need=o["need"] + lost)), lost


def examples(ctx, o, growth_gap):
    """Worked examples in today's (2026) dollars at FY2040's rates, with health costs at FY2040's relation to income:
    KFF's 2026 premiums (EV-CAR-722) and the coverage model's per-person out-of-pocket costs, copays and Medicare
    premiums (2032 basis, taken back to 2026 at HEALTH_GROWTH), all times `growth_gap` (health costs per person over
    incomes, 2026 to FY2040). Full pass-through (total pay fixed, HX's convention); tax on pay that changes and on the
    former pre-tax premium share at the household's federal bracket plus both halves of payroll tax (15.3%). The lines
    are taken as $20,000/$40,000 and $100,000/$200,000 in today's dollars. Households below the top fifth bear no
    avoidance. The self-employed pay the employer contribution on 92.35% of net earnings, as SECA does."""
    r1, r2, v, er = o["first"] / 100, o["second"] / 100, o["vat_rate"] / 100, o["employer_rate"] / 100
    gg = growth_gap
    back = (1 + HEALTH_GROWTH) ** (2032 - 2026)
    inc_back = (1 + ctx["income_growth"]) ** (Y - 2026)
    persons_2040 = ctx["persons_2029"] * ctx["hh"] / ctx["n29"]
    rebate_pp = o["vat_gross"] * o["vat_rebate"] * 1e9 / persons_2040 / inc_back if o["vat_gross"] else 0.0
    copay = gg * ctx["pp_person"]["copay"] / back
    oop = {k: gg * x / back for k, x in ctx["oop_pp"].items()}
    med_prem = gg * 3500 / back
    ng_prem = gg * 11768 / back
    cases = [
        dict(name="Single worker, $45,000 pay, single job coverage", cash=45000, agi=45000, wages=45000, joint=False,
             people=1, er_prem=9804 - 1672, ee_prem=1672, own=0, oop=oop["esi"], m=0.12, consume=0.95),
        dict(name="Single worker, $45,000 pay, employer offers no coverage, uninsured today", cash=45000, agi=45000,
             wages=45000, joint=False, people=1, er_prem=0, ee_prem=0, own=0, oop=oop["uninsured"], m=0.12,
             consume=0.95),
        dict(name="Family of four, $90,000 pay, family job coverage", cash=90000, agi=90000, wages=90000, joint=True,
             people=4, er_prem=28303 - 7471, ee_prem=7471, own=0, oop=4 * oop["esi"], m=0.12, consume=0.9),
        dict(name="Family of four, $160,000 pay, family job coverage", cash=160000, agi=160000, wages=160000,
             joint=True, people=4, er_prem=28303 - 7471, ee_prem=7471, own=0, oop=4 * oop["esi"], m=0.22,
             consume=0.8),
        dict(name="Retired couple on Medicare, $60,000 (Social Security $36,000, pension $24,000)", cash=60000,
             agi=24000 + 9000, wages=0, joint=True, people=2, er_prem=0, ee_prem=0, own=2 * med_prem,
             oop=2 * oop["medicare"], m=0.12, consume=0.95),
        dict(name="Retired couple on Medicare, $110,000 (Social Security $50,000, pension and savings $60,000)",
             cash=110000, agi=60000 + 42500, wages=0, joint=True, people=2, er_prem=0, ee_prem=0, own=2 * med_prem,
             oop=2 * oop["medicare"], m=0.22, consume=0.85),
        dict(name="Self-employed single person, $70,000 net, buys an individual-market plan", cash=70000,
             agi=70000 - 5000, wages=0, se=70000, joint=False, people=1, er_prem=0, ee_prem=0, own=ng_prem,
             oop=oop["ng_unsub"], m=0.22, consume=0.9),
    ]
    out = []
    for c in cases:
        line1, line2 = (40000, 200000) if c["joint"] else (20000, 100000)
        prem_today = gg * (c["ee_prem"]) + c["own"]
        stop = prem_today + c["oop"] - copay * c["people"]
        tax_ee = -(c["m"] + 0.153) * gg * c["ee_prem"]       # the former pre-tax premium share is now taxable (HX)
        er_saved = gg * c["er_prem"]
        er_new = er * c["wages"]
        pay_change = er_saved - er_new
        tax_pay = -(c["m"] + 0.153) * pay_change
        base1, base2 = max(c["agi"] - line1, 0), max(c["agi"] - line2, 0)
        contrib = -(r1 * base1 + r2 * base2)
        se_contrib = -er * 0.9235 * c.get("se", 0)
        vat = (-v * c["consume"] * c["cash"] + rebate_pp * c["people"]) if v else 0.0
        net = stop + tax_ee + pay_change + tax_pay + contrib + se_contrib + vat
        out.append(dict(name=c["name"], premiums_stop=round(prem_today), out_of_pocket_stop=round(c["oop"]),
                        copays=round(-copay * c["people"]), stop_paying=round(stop), hx_on_worker_share=round(tax_ee),
                        employer_saves=round(er_saved), employer_pays=round(er_new), pay_change=round(pay_change),
                        tax_on_pay_change=round(tax_pay), agi=c["agi"], base=round(base1), base2=round(base2),
                        rate1=o["first"], rate2=o["second"], contribution=round(contrib),
                        self_employed=round(se_contrib), vat=round(vat), net=round(net),
                        net_share=round(100 * net / c["cash"], 1)))
    return out


def context():
    if "ctx" in _CACHE:
        return _CACHE["ctx"]
    gap = plan_gap()
    c = coverage(True)
    sm = seam()
    need_p = need_path(sm)
    flows_p = flow_path(c)
    pp = per_point(gap)
    K, hh, incomes, cps_base, X = keys()
    gp, x = group_payers(c)
    HP = c["HP"]
    M = HP.M
    h0 = M.run(c["I"], {}, c["B"])["household"]["by_source"]
    sp = HP.model_full(c["I"], c["B"], c["P"])["household"]["by_source"]["sp"]["oop_pp"]
    cp = sum(sp) / len(sp) if isinstance(sp, list) else sp
    ng_n = h0["ng_sub"]["people"] + h0["ng_unsub"]["people"]
    tot = lambda s: h0[s]["premium_pp"] + h0[s]["oop_pp"]  # noqa: E731
    # Medicaid enrollees pay no copays (below 200% of poverty, memo 4 C)
    pp_person = dict(esi=tot("esi") - cp, medicaid=tot("medicaid"), medicare=tot("medicare") - cp,
                     uninsured=tot("uninsured") - cp,
                     ng=(h0["ng_sub"]["people"] * tot("ng_sub") + h0["ng_unsub"]["people"] * tot("ng_unsub")) / ng_n
                     - cp, copay=cp)
    def cpi(y):
        from params import econ
        return econ("cpiu", min(y, 2036)) * 1.023 ** max(y - 2036, 0)   # CBO's later years at 2.3% a year
    ctx = dict(gap=gap, c=c, seam=sm, need_p=need_p, flows_p=flows_p, pp=pp, K=K, hh=hh, incomes=incomes,
               cps_base=cps_base, gp=gp, x=x, tau=x["tau"], need=need_p[Y]["net"], f40=flows_p[Y],
               pp_person=pp_person, oop_pp={s: h0[s]["oop_pp"] for s in h0},
               price_2032=cpi(2032) / cpi(2026), price_2040=cpi(2040) / cpi(2026),
               income_growth=X["grow"] ** (1 / (Y - 2029)) - 1, n29=X["n29"],
               persons_2029=sum(h["weight"] * h["numper"] for h in X["H"]))
    _CACHE["ctx"] = ctx
    return ctx


def run():
    ctx = context()
    gap, c, pp, K, hh = ctx["gap"], ctx["c"], ctx["pp"], ctx["K"], ctx["hh"]
    g40 = ctx["need"] and (HB.incidence()["fy2040"]["H7w"] / HB.incidence()["full_scale"]["employer_premiums"])
    P = {k: package(ctx, **s) for k, s in PACKAGES.items()}
    base, sens = sensitivities(c)
    sav = -(sens["admin_3pct"] + sens["drugs_23pct"]) * g40
    S = {
        "A_with_savings": package(ctx, **dict(PACKAGES["A"], savings=sav)),
        "B_with_savings": package(ctx, **dict(PACKAGES["B"], savings=sav)),
        "A_booked_seam": package(ctx, **dict(PACKAGES["A"], need=ctx["need_p"][Y]["booked"])),
        "A_employers_65": package(ctx, **dict(PACKAGES["A"], emp_share=0.65)),
        "A_states_80": package(ctx, **dict(PACKAGES["A"], state_share=0.8)),
        "A_states_50": package(ctx, **dict(PACKAGES["A"], state_share=0.5)),
        "A_states_0": package(ctx, **dict(PACKAGES["A"], state_share=0.0)),
        "A_employer_uncapped": package(ctx, **dict(PACKAGES["A"], emp_base="payroll")),
        "A_employer_on_premiums": package(ctx, **dict(PACKAGES["A"], emp_base="premiums")),
        "A_first_4_with_hi": package(ctx, **dict(PACKAGES["B"], first=FIRST_TIER_TARGET - 1.45)),
        "D_top_avoidance_60": package(ctx, **dict(PACKAGES["D"], high_avoid=0.6)),
        "B_first_6": package(ctx, **dict(PACKAGES["B"], first=6.0)),
        "B_first_5": package(ctx, **dict(PACKAGES["B"], first=5.0)),
    }
    # the first draft's package on the corrected method, for the trace (employers 65% on payroll, states 80%)
    S["first_draft"] = package(ctx, emp_share=0.65, state_share=0.8, need=ctx["need_p"][Y]["booked"])
    paths_ = {k: package_path(ctx, PACKAGES[k], ctx["need_p"], ctx["flows_p"], gap) for k in P}
    rc = payers(c, g40)
    rc_booked = payers(coverage(False), g40)
    micro_ = {k: micro(ctx, P[k]) for k in P}
    micro_["A_states_80"] = micro(ctx, S["A_states_80"])
    micro_["A_employer_uncapped"] = micro(ctx, S["A_employer_uncapped"])
    statutory = P["A"]["rows"]
    st_charge = -[bn for lb, bn, _ in statutory if lb.startswith("First tier: the statutory")][0]
    base_2040 = st_charge / (P["A"]["first"] / 100)
    sh, t1 = K["income_line"]
    implied = {g_: base_2040 * 1e9 * s / 100 / (hh * 0.2) for g_, s in zip(GROUPS, sh)}
    implied["T1"] = base_2040 * 1e9 * t1 / 100 / (hh * 0.01)
    # health costs per person grow with CMS's projection of national health spending, 5.4% a year (EV-CAR-056), against
    # nominal income per household on the model's path (2029 to FY2040)
    gg = ((1 + HEALTH_GROWTH) / (1 + ctx["income_growth"])) ** (Y - 2026)
    ex = {k: examples(ctx, P[k], gg) for k in P}
    tc = {k: topcode_check(P[k], K, hh) for k in P}
    stk = {k: stacking_check(P[k], K, pp) for k in P}
    stk["A_employer_uncapped"] = stacking_check(S["A_employer_uncapped"], K, pp)
    adj = {}
    for name, spec in (("A", PACKAGES["A"]), ("A_employer_uncapped", dict(PACKAGES["A"], emp_base="payroll")),
                       ("B", PACKAGES["B"])):
        for e in (0.12, TOP1_ELASTICITY, 0.4):
            o_, lost = stacking_adjusted(ctx, spec, e)
            adj[f"{name}@{e}"] = dict(lost=lost, first=o_["first"], vat=o_["vat_rate"], households=o_["households"])
    pt = {k: passthrough_check(ctx, P[k]) for k in ("A",)}
    pt["first_draft"] = passthrough_check(ctx, S["first_draft"])
    hi = dict(rate=2.9, yield_2040=2.9 * pp["payroll_gross"], addl_rate=0.9)
    return dict(gap=gap, need_path=ctx["need_p"], seam=ctx["seam"], flows_path=ctx["flows_p"], per_point=pp,
                tau=ctx["tau"], households_2040=hh, keys={k: K[k] for k in ("health_hh", "employer_cov",
                                                                            "exclusion_end", "wages", "wages_cap",
                                                                            "income_line", "income_high",
                                                                            "avoid_central", "consumption",
                                                                            "persons")},
                incomes_2040={m: {k: round(v) for k, v in d.items()} for m, d in ctx["incomes"].items()},
                base_2040=dict(statutory_bn=base_2040, cps_grown_bn=ctx["cps_base"], per_household=implied),
                packages=P, sensitivities=S, savings_2040=sav, sens_2040={k: v * g40 for k, v in sens.items()},
                package_paths=paths_, payers=rc, payers_booked=rc_booked, payer_path=payer_path(c, ctx["gp"]),
                group_payers_2032=ctx["gp"], micro=micro_, examples=ex, growth_gap=gg, topcode=tc, stacking=stk,
                passthrough=pt, hi=hi, stacking_adjusted=adj, g40=g40, pp_person=ctx["pp_person"],
                before_financing=per_household(relief_rows(ctx["f40"]), K, hh))


def topcode_check(o, K, hh, top1_share=TOP1_BASE_SHARE_IRS):
    sh, t1 = K["income_line"]
    scale = (100 - top1_share) / (100 - t1)
    q = [s * scale for s in sh[:4]] + [sh[4] * scale + (top1_share - t1 * scale)]
    return per_household(o["rows"], dict(K, income_line=(q, top1_share)), hh)


def passthrough_check(ctx, o, p=0.5):
    """If employers pass only `p` of their net saving (former premiums less the contribution) into pay (Anand,
    EV-CAR-299), workers lose that pay and its tax, owners keep it less corporate tax (21%), and the household
    contribution rises to replace the lost tax. At 100% employers keep no net saving, so nothing depends on it."""
    f = ctx["f40"]
    kept = (1 - p) * max(f["employers"] - o["employer_gross"], 0.0)
    rate = f["hx"] / (f["employers"] / (1 - HB.health_path()["I"]["esi_employee_share"]))
    lost = kept * (rate - 0.21)
    rows = [("Pay that does not rise", -kept, "employer_cov"), ("Tax not paid on it", kept * rate, "exclusion_end"),
            ("Profit kept, after corporate tax", kept * 0.79, "capital")] + income_rows(lost, ctx["pp"])
    d = per_household(rows, ctx["K"], ctx["hh"])
    return dict(kept=kept, lost_tax=lost, extra_points=lost / ctx["pp"]["broad_income"],
                households={g: o["households"][g] + d[g] for g in d})


def main():
    r = run()
    if "--json" in sys.argv:
        print(json.dumps(r, indent=1, default=float))
        return
    n = r["need_path"]
    print("Need by FY (booked, seam, net):")
    for y in YEARS:
        print(" ", y, round(n[y]["spending"]), round(n[y]["hx"]), round(n[y]["booked"]), round(n[y]["seam"]),
              round(n[y]["net"]), {k: round(v) for k, v in n[y]["rows"].items()})
    print("Seam by group 2032:", {k: round(v) for k, v in r["seam"]["by_group_2032"].items()},
          "decade", round(sum(r["seam"]["difference"][y] for y in range(2030, 2040))))
    for y in YEARS:
        print("flows", y, {k: round(v) for k, v in r["flows_path"][y].items()})
    print("per point", {k: round(v, 2) for k, v in r["per_point"].items()}, "tau", round(r["tau"], 4), "g40",
          round(r["g40"], 4))
    for name in ("payers_booked", "payers"):
        rc = r[name]
        print(name)
        for col in ("today_2032", "plan_2032", "change_2032", "today_2040", "plan_2040"):
            print("  ", col, {k: round(v) for k, v in rc[col].items()}, round(sum(rc[col].values())))
        print("   lines", {k: round(v) for k, v in rc["lines_2032"].items()}, "seam", round(rc["seam_2032"]),
              "named", {k: round(v) for k, v in rc["named_split_2032"].items()})
        print("   identity", {k: round(v) for k, v in rc["identity_2032"].items()})
    for g, d in r["group_payers_2032"].items():
        print("group", g, {k: round(v) for k, v in d.items()})
    for y in YEARS:
        print("payer path", y, {k: round(v) for k, v in r["payer_path"][y].items()})
    for name in ("packages", "sensitivities"):
        for k, o in r[name].items():
            print(name, k, f"first {o['first']:.2f} second {o['second']:.2f} vat {o['vat_rate']:.2f} "
                  f"emp {o['emp_share']:.3f} rate {o['employer_rate']:.2f} (+HI {o['employer_rate_with_hi']:.2f}) "
                  f"top {o['top_rate_on_wages']:.1f}/{o['top_rate_with_employer']:.1f} net {o['employer_net']:.0f} "
                  f"hxkept {o['hx_kept']:.0f} st {o['state_extra']:.0f} hh {o['household_collected']:.0f}",
                  o["households"], "ahead" if o["bottom_four_ahead"] else "")
    for k in r["packages"]:
        print("detail", k)
        for d in r["packages"][k]["detail"]:
            print("    ", d)
        print("  avoid", r["packages"][k]["avoidance_range"])
        print("  topcode", r["topcode"][k], "stacking", {a: round(b, 3) for a, b in r["stacking"][k].items()})
        print("  micro", {q: ({a: round(b, 2) for a, b in v.items()} if isinstance(v, dict) else round(v, 2))
                          for q, v in r["micro"][k].items()})
        for e in r["examples"][k]:
            print("  ex", e)
        for y, v in r["package_paths"][k].items():
            print("  path", y, {a: round(b, 2) for a, b in v.items()})
    print("micro A states 80", r["micro"]["A_states_80"])
    print("micro A uncapped", r["micro"]["A_employer_uncapped"])
    for k, v in r["stacking_adjusted"].items():
        print("stacking adjusted", k, {a: (round(b, 2) if not isinstance(b, dict) else b) for a, b in v.items()})
    print("passthrough", r["passthrough"])
    print("incomes", r["incomes_2040"], "base", {k: round(v) for k, v in r["base_2040"]["per_household"].items()},
          round(r["base_2040"]["statutory_bn"]), round(r["base_2040"]["cps_grown_bn"]))
    print("savings", round(r["savings_2040"]), {k: round(v) for k, v in r["sens_2040"].items()}, "hi", r["hi"],
          "growth gap", round(r["growth_gap"], 3), "pp person", {k: round(v) for k, v in r["pp_person"].items()})
    print("before financing", r["before_financing"])


if __name__ == "__main__":
    main()
