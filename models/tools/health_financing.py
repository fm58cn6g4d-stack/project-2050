"""Health financing: who pays for health care now and under the single plan, year by year, and what each financing
package does to the federal budget and to households.

Role: the analysis behind `dossiers/foundations/health-financing.md`, the stage E memo that prices and finances the
single health plan (HLT-1 to HLT-8) from a fresh start; it replaces part B of `checkpoint-financing.md`. Status:
exploratory analysis, November 15, 2026 (revised the same day in #386). It books nothing and changes no adopted
input; every figure is project arithmetic on the project's own models, not an official score.

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
    and who loses (`micro()`), and worked examples (`examples()`);
  * the fix for households that lose cash and the employer contribution's protections (#386): the phase-in for
    employers with no 2028 coverage (`no_offer()`, `phase_left()`), the worker transition credit (`credit_key()`),
    the low-pay line as the alternative (`line_variant()`), and the incidence checks: what the pass-through and
    wage-maintenance rules cover (`employer_split()`), pay that holds (`pay_holds_check()`) and savings employers
    keep (`savings_kept_check()`).

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
# The Medicare payroll tax (HI): 1.45% from workers and 1.45% from employers on all pay, 2.9% on self-employment
# income. In the whole-system packages it is repealed at the January 2035 endpoint and its money raised by the plan's
# own contributions instead (memo part 3.3); its yield is taken as 2.9 times the budget model's payroll point
# (approximate; the 0.9% Additional Medicare Tax and H1b stay as they are). The halves are split evenly.
HI_RATE = 2.9
HI_ENDPOINT = {y: (0.0 if y < 2035 else (0.75 if y == 2035 else 1.0)) for y in range(2030, 2041)}  # fiscal years
LOW_PAY_LINE = 20000         # the low-pay exemption option: the first $20,000 of each worker's pay (2025 dollars,
                             # price-indexed) is outside the employer contribution
# The phase-in for employers that reported no group coverage for 2028, the last full year before the law (memo part
# 2.6; Forms 1095-B and 1095-C, W-2 box 12 DD): their rate is a tenth of the full rate in calendar 2035 and rises by a
# tenth a year, full from 2044.
PHASE_IN_START, PHASE_IN_YEARS = 2035, 10
NO_OFFER_WORKER_SHARE = 0.08  # KFF 2026: 92% of workers are at firms offering health benefits (EV-CAR-295)
# The worker transition credit (memo part 2.7): for people who had earnings in 2028 and neither employer coverage nor
# an individual-market plan that year (the IRS's 2028 Forms W-2, Schedules SE and Forms 1095-A, 1095-B and 1095-C).
# Refundable, claimed on the income tax return and paid through the year by lower withholding: `share` of the
# employer health contribution charged on their pay (W-2s and Schedule SE), phased out with the household's AGI
# between `start` and `end` (single; joint lines twice these; 2025 dollars, price-indexed, as the other lines). Full
# from the January 2035 endpoint through 2044, then a fifth less each year, ending after 2049.
WORKER_CREDIT = dict(share=1.0, start=60000, end=120000, nocov_only=True)
CREDIT_LAST_FULL, CREDIT_STEPDOWN = 2044, 5


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


def _band_unit(u, L, line=None):
    """A tax unit's pay between the low-pay line and the Social Security wage base, person by person (2029)."""
    from params import econ
    line = (LOW_PAY_LINE if line is None else line) * econ("cpiu", L["year"] - 1) / econ("cpiu", 2024)
    base = L["ss_wage_base"]
    own = [u["wage_h"] + max(u["se_h"], 0), u["wage_s"] + max(u["se_s"], 0), u["dep_wages"]]
    return sum(max(min(x, base) - line, 0.0) for x in own)


def _earners(u):
    return sum(1 for x in (u["wage_h"] + max(u["se_h"], 0), u["wage_s"] + max(u["se_s"], 0), u["dep_wages"]) if x > 0)


def _draw(u):
    """A fixed pseudo-random number in [0, 1) for a tax unit (Knuth's multiplicative hash of its id), so the draw of
    units whose employer offered no coverage in 2028 is the same on every run."""
    return ((int(u["tid"]) * 2654435761) % 2 ** 32) / 2 ** 32


def no_offer():
    """The workers whose employers offered no coverage in 2028, drawn from the CPS's units with pay in the band and
    no employer coverage: KFF's 8% of workers (EV-CAR-295) at the band pay per worker of those units, as a share of
    all band pay; units are drawn at the rate that gives that share. Registers the key `wages_band_nooffer`."""
    if "no_offer" in _CACHE:
        return _CACHE["no_offer"]
    import provisions as P
    K, _, _, _, X = keys()
    B = X["B"]
    L = B["law"]
    U = B["units"]
    band = {u["tid"]: _band_unit(u, L) for u in U}
    nocov = [u for u in U if u["n_employer_cov"] == 0 and band[u["tid"]] > 0]
    tot_band = sum(u["weight"] * band[u["tid"]] for u in U)
    tot_earn = sum(u["weight"] * _earners(u) for u in U if band[u["tid"]] > 0)
    nc_band = sum(u["weight"] * band[u["tid"]] for u in nocov)
    nc_earn = sum(u["weight"] * _earners(u) for u in nocov)
    ratio = (nc_band / nc_earn) / (tot_band / tot_earn)
    s_no = NO_OFFER_WORKER_SHARE * ratio
    p = s_no * tot_band / nc_band
    drawn = {u["tid"] for u in nocov if _draw(u) < p}
    P.RULES["wages_band_nooffer"] = lambda u, L: _band_unit(u, L) if u["tid"] in drawn else 0.0
    K["wages_band_nooffer"] = P.micro_shares(B, "rule:wages_band_nooffer")
    v = P.household_base(B, "rule:wages_band_nooffer")
    EXTRA_BASES["wages_band_nooffer"] = lambda h: v[h["hh"]]
    got = sum(h["weight"] * v[h["hh"]] for h in X["H"]) / tot_band
    _CACHE["no_offer"] = dict(share=got, target=s_no, pay_ratio=ratio, draw_rate=p, nocov_share=nc_band / tot_band,
                              drawn=drawn)
    return _CACHE["no_offer"]


def _credits(credit):
    """The credits a package carries: none, one (a dict) or several (a list)."""
    return [] if not credit else (list(credit) if isinstance(credit, (list, tuple)) else [credit])


def phase_left(y):
    """The share of the full rate that employers with no 2028 coverage do not yet pay, fiscal year `y` (none before
    the endpoint, when there is no payroll-based contribution)."""
    if y < PHASE_IN_START:
        return 0.0
    cal = lambda c: min(max(c - PHASE_IN_START + 1, 0) / PHASE_IN_YEARS, 1.0)  # noqa: E731
    on = HI_ENDPOINT.get(y, 1.0)             # FY2035 has three quarters of a year of the contribution
    charged = 0.25 * (cal(y - 1) if y - 1 >= PHASE_IN_START else 0.0) + 0.75 * cal(y)
    return 1.0 - charged / on


def credit_key(start, end, left=0.0, nocov_only=False):
    """The worker health credit's base: each tax unit's band pay (the contribution's base), less what employers with
    no 2028 coverage do not yet charge (`left`), times its phase-out factor on AGI (lines price-indexed from 2025;
    joint twice single). Registers the key and returns (name, the base over all band pay)."""
    name = f"credit_{start}_{end}_{round(left, 6)}_{int(nocov_only)}"
    if name in _CACHE:
        return name, _CACHE[name]
    import provisions as P
    from params import econ
    K, _, _, _, X = keys()
    B = X["B"]
    drawn = no_offer()["drawn"]
    def rule(u, L):
        f = econ("cpiu", L["year"] - 1) / econ("cpiu", 2024) * (2 if u["t_fs"] == "joint" else 1)
        a0, a1 = start * f, end * f
        ph = 1.0 if u["t_agi"] <= a0 else max(0.0, (a1 - u["t_agi"]) / (a1 - a0))
        if nocov_only and u["n_employer_cov"] + u["n_marketplace"] > 0:   # no employer or individual-market plan
            return 0.0
        return _band_unit(u, L) * ph * ((1 - left) if u["tid"] in drawn else 1.0)
    P.RULES[name] = rule
    K[name] = P.micro_shares(B, "rule:" + name)
    v = P.household_base(B, "rule:" + name)
    EXTRA_BASES[name] = lambda h: v[h["hh"]]
    tot = sum(h["weight"] * X["vals"]["band"][h["hh"]] for h in X["H"])
    _CACHE[name] = sum(h["weight"] * v[h["hh"]] for h in X["H"]) / tot
    return name, _CACHE[name]


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
    P.RULES["wages_band"] = _band_unit
    K["wages_band"] = P.micro_shares(B, "rule:wages_band")
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
            "high": P.household_base(B, "rule:income_high"), "band": P.household_base(B, "rule:wages_band")}
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


def employer_rows(f40, tau, share, base, hi_er=0.0):
    """The employer side at `share` of former premiums (private and state and local employers). `base`: 'premiums'
    (on each employer's former premiums, HLT-7.18; borne by the workers who had the coverage), 'payroll' (all pay, the
    HI base) or 'payroll_cap' (pay up to the Social Security wage base, person by person). Pay that does not rise is
    not taxed, so HX falls by the exclusion's rate on it."""
    prem = share * f40["employers"]
    key = {"premiums": "employer_cov", "payroll": "wages", "payroll_cap": "wages_cap", "payroll_band": "wages_band"}[base]
    hx_key = "exclusion_end" if base == "premiums" else key
    # `hi_er`: the employer's half of the repealed HI tax, raised by the same contribution; HI was deductible and so is
    # the contribution, so it changes no other tax
    return [(f"Employer health contribution ({base})", -(prem + hi_er), key),
            ("Less tax on pay that no longer rises (HX falls)", prem * tau, hx_key)], prem * (1 - tau) + hi_er


def employer_rate(f40, share, base, pp, hi_er=0.0):
    """The employer contribution as a rate on its base: its yield (with federal payroll, which pays it too,
    intragovernmentally) over all pay, pay up to the wage base, or pay between the low-pay line and the wage base."""
    r = (share * f40["employers_all"] + hi_er) / pp["payroll_gross"]
    return r / {"payroll": 1.0, "payroll_cap": CAP_SHARE, "payroll_band": band_share()}[base]


def band_share():
    """Share of all pay between the low-pay line and the wage base, person by person: the CPS's share less the
    top-coding allowance applied to the capped base (CAP_SHARE over the CPS's capped share)."""
    _, _, _, _, X = keys()
    H = X["H"]
    w = sum(h["weight"] * h["wages"] for h in H)
    cap = sum(h["weight"] * h["wages_capped"] for h in H)
    band = sum(h["weight"] * X["vals"]["band"][h["hh"]] for h in H)
    return band / w * CAP_SHARE / (cap / w)


def package(ctx, emp_share=1.0, emp_base="payroll", state_share=1.0, first=None, second=0.0, close="first",
            vat_rebate=VAT_REBATE_SHARE, savings=0.0, label="", need=None, f40=None, pp=None, high_avoid=None,
            replace_hi=True, hi=None, hi_er_share=0.5, phase_in=0.0, credit=None):
    """A whole health financing package, FY2040 (or another year, with `need`, `f40` and `pp` for it). The closing
    item (`close`: 'first' tier, 'vat', 'second' tier or 'employer' share) is solved so the package covers the need
    exactly; the others are as given. With `replace_hi` (the whole-system packages), the HI payroll tax is repealed and
    its money raised by the employer contribution (the employer's half) and the household side (the rest).
    `phase_in`: the share of the full rate that employers with no 2028 coverage do not yet pay (phase_left()); the pay
    it leaves is taxed. `credit`: the worker health credit (WORKER_CREDIT's form), a share of the contribution charged
    on each worker's pay, phased out with AGI; both are paid by the closing item."""
    need = ctx["need"] if need is None else need
    f40 = ctx["f40"] if f40 is None else f40
    pp = ctx["pp"] if pp is None else pp
    hi = (HI_RATE * pp["payroll_gross"] if hi is None else hi) if replace_hi else 0.0
    hi_er = hi * hi_er_share
    fed_need = need
    # the tax effects of repealing HI (the independent cross-check, memo part 8): the worker's half that the employer
    # contribution raises instead leaves taxable cash pay, so income and Social Security tax on it fall (tau less HI's
    # own 2.9 points); and HX's remainder no longer carries HI's 2.9 points on the former pre-tax premium share
    hi_tax = ((ctx["tau"] - HI_RATE / 100) * hi * max(hi_er_share - 0.5, 0.0)
              + (HI_RATE / 100 / ctx["tau"]) * (f40["hx"] - ctx["tau"] * f40["employers"]) * (hi / (HI_RATE *
                                                                                                    pp["payroll_gross"])
                                                                                              if hi else 0.0))
    need = need + hi + hi_tax
    tau, K, hh = ctx["tau"], ctx["K"], ctx["hh"]
    point = 0.1 * f40["states_moved"]
    extra = (state_share - STATE_SHARE_BOOKED) * 10 * point
    h2 = pp["haircut"] if high_avoid is None else high_avoid
    got2 = second * pp["high_income"] / (1 - pp["haircut"]) * (1 - h2)
    # the pay workers used to put into premiums before tax is now in AGI, so it widens the household contribution's
    # base (the independent cross-check, memo part 8): its yield per point rises by 1% of it, after the allowance
    newly = max(f40["hx"] - tau * f40["employers"], 0.0) / tau
    pp = dict(pp, broad_income=pp["broad_income"] + newly * 0.01 * (1 - pp["haircut"]))
    first_got = (first or 0.0) * pp["broad_income"]
    # the phase-in and the credit, each per dollar of the employer contribution's premium part
    s_no = no_offer()["share"] if phase_in else 0.0
    credits = _credits(credit)
    ckeys = [credit_key(c["start"], c["end"], phase_in, c.get("nocov_only", False)) for c in credits]
    crs = [c["share"] * r for c, (_, r) in zip(credits, ckeys)]
    cr = sum(crs)
    if close == "employer":
        rest_emp = need - savings - extra - got2 - first_got
        emp_share = (rest_emp - hi_er) / (f40["employers"] * ((1 - tau) * (1 - phase_in * s_no) - cr))
    emp, emp_net = employer_rows(f40, tau, emp_share, emp_base, hi_er)
    prem = emp_share * f40["employers"]
    d = phase_in * s_no * prem
    cbn = cr * prem
    ckey = ckeys[0][0] if ckeys else None
    adds = []
    if d:
        adds += [("Phase-in for employers with no coverage in 2028: contribution not yet charged", d,
                  "wages_band_nooffer"), ("Less tax on the pay it leaves", -tau * d, "wages_band_nooffer")]
    for c, (k, _), x in zip(credits, ckeys, crs):
        adds += [("Worker transition credit" if c.get("nocov_only") else "Low-pay worker credit", x * prem, k)]
    emp_net -= d * (1 - tau)
    rest = need - savings - emp_net - extra + cbn
    vat_gross = 0.0
    if close == "first":
        first_got = rest - got2
        first = first_got / pp["broad_income"]
    elif close == "vat":
        vat_gross = (rest - got2 - first_got) / (1 - vat_rebate)
    elif close == "second":
        got2 = rest - first_got
        second = got2 / (1 - h2) * (1 - pp["haircut"]) / pp["high_income"]
    rows = relief_rows(f40) + emp + adds
    if hi:
        rows.insert(3, ("Medicare payroll tax (HI) ends, both halves", hi, "wages"))
    n_fixed = len(rows)
    if first_got:
        on_newly = first / 100 * newly * (1 - pp["haircut"])
        pp_old = dict(pp, broad_income=pp["broad_income"] - newly * 0.01 * (1 - pp["haircut"]))
        rows += income_rows(first_got - on_newly, pp_old, label="First tier")
        rows += [("First tier on pay formerly put into premiums before tax, now in income", -on_newly,
                  "exclusion_end")]
    if got2:
        st2 = got2 / (1 - h2)
        rows += [("Second tier: the statutory charge", -st2, "income_high"),
                 (f"Second tier: less what avoidance keeps from being collected ({round(100 * h2)}%)", st2 * h2,
                  "avoid_high_central")]
    if vat_gross:
        rows += [("Value-added tax, gross", -vat_gross, "consumption"),
                 ("Per-person rebate", vat_gross * vat_rebate, "persons")]
    e_rate = employer_rate(f40, emp_share, emp_base, pp, hi_er) if emp_base != "premiums" else 0.0
    o = dict(label=label, emp_share=emp_share, emp_base=emp_base, state_share=state_share, close=close,
             savings=savings, need=fed_need, hi=hi, hi_tax=hi_tax, hi_er=hi_er, hi_er_share=hi_er_share,
             need_with_hi=need, rest=rest, employer_gross=-emp[0][1] - d,
             employer_premium_part=prem, employer_net=emp_net, phase_in=phase_in, phase_in_bn=d,
             no_offer_share=s_no, credit=credit, credit_key=ckey, credit_bn=cbn, credit_per_dollar=cr,
             n_fixed_rows=n_fixed,
             hx_kept=f40["hx"] - emp[1][1], state_extra=extra, first=first or 0.0, second=second,
             vat_rate=vat_gross / pp["vat"], vat_gross=vat_gross, vat_rebate=vat_rebate if vat_gross else 0.0,
             employer_rate=e_rate, employer_rate_with_hi=e_rate + 1.45 if e_rate else 0.0,
             household_collected=first_got + got2 + vat_gross * (1 - vat_rebate), rows=rows)
    o["top_rate_on_wages"] = TOP_RATE_BEFORE_HEALTH - (HI_RATE if hi else 0.0) + o["first"] + o["second"]
    o["top_rate_with_employer"] = o["top_rate_on_wages"] + (e_rate if emp_base == "payroll" else 0.0)
    if K is not None:
        o["households"] = per_household(rows, K, hh)
        o["detail"] = [(lb, round(bn), per_household([(lb, bn, k)], K, hh)) for lb, bn, k in rows]
        o["avoidance_range"] = {alt: per_household([(lb, bn, k.replace("_central", f"_{alt}")) for lb, bn, k in rows],
                                                   K, hh) for alt in ("elastic", "even")}
        o["bottom_four_ahead"] = min(o["households"][g] for g in GROUPS[:4]) > 0
    return o


# The packages (memo part 4). Recommended: A.
PACKAGES = {
    "A": dict(label="One employer contribution and one household contribution, sized to the whole system",
              emp_share=1.0, close="first"),
    "B": dict(label="A household rate of 5.5%, with a rebated value-added tax", emp_share=1.0,
              first=FIRST_TIER_TARGET, close="vat"),
    "C": dict(label="A household rate of 5.5%, with a larger employer contribution", first=FIRST_TIER_TARGET,
              close="employer"),
    "D": dict(label="A household rate of 5.5%, with a top tier", emp_share=1.0, first=FIRST_TIER_TARGET,
              close="second"),
}
# Every package (memo part 2): the 2.9% payroll tax on all pay is kept as the plan's own health payroll contribution
# (it falls on top pay, where the capped employer contribution does not; folding it into the employer contribution
# is a sensitivity); the employer contribution on each worker's pay between the low-pay line and the Social Security
# wage base; states at 100% of their former Medicaid spending for the people who move; the phase-in for employers
# with no 2028 coverage (FY2040 is 57.5% of the way in) and the worker transition credit (memo parts 2.6 and 2.7).
COMMON = dict(emp_base="payroll_band", state_share=1.0, replace_hi=False, phase_in=phase_left(Y), credit=WORKER_CREDIT)
BEFORE_FIX = dict(phase_in=0.0, credit=None)     # package A as merged in #385
for _k in PACKAGES:
    PACKAGES[_k] = dict(COMMON, **PACKAGES[_k])



def replaced_path(c):
    """By fiscal year: the federal money the plan replaces (Medicare net of premiums, Medicaid's federal share outside
    long-term care, premium credits) and the states' booked 50% payment, for the groups that have moved ($ billion)."""
    HP, I, B, P = c["HP"], c["I"], c["B"], c["P"]
    _, _, _, f = HP.groups(I, B, P)
    ms = moved_shares(c)
    rep = {"medicare": I["sub_medicare"], "medicaid": I["sub_medicaid"] - f["medicaid_ltc_kept_federal"],
           "individual": I["sub_ptc"]}
    return {y: dict(federal=sum(v * ms[g][y] for g, v in rep.items()), states_booked=f["state_moe"] * ms["medicaid"][y])
            for y in YEARS}


def system_view(ctx, o, y=Y, row=None):
    """The whole system's gross cost in fiscal year `y` and the package's sources that pay it ($ billion): the gross
    cost is the booked health spending (rebased) plus the federal money and the states' payment it nets. The sources
    add to it exactly: federal general revenue already spent on these programs (net of the repealed HI tax), the
    states' payment, the employer contribution, the household side (net of the worker health credit), HX's remainder
    and any savings."""
    n, rp_ = ctx["need_p"][y], ctx["replaced_p"][y]
    gross = n["spending"] + n["seam"] + rp_["federal"] + rp_["states_booked"]
    f = ctx["flows_p"][y]
    if row is None:      # FY2040, from the package itself
        hi, emp, extra, sav = o["hi"], o["employer_gross"], o["state_extra"], o["savings"]
        hh_ = o["household_collected"] - o["credit_bn"]          # net of the worker health credit paid back
        lost = (o["employer_premium_part"] - o["phase_in_bn"]) * ctx["tau"] + o["hi_tax"]
    else:                # a year of package_path()
        hi, emp, extra, sav = row["hi"], row["employer_gross"], row["states"], row["savings"]
        hh_ = row["households"] - row["credit"]
        lost = (row["employer_gross"] - row["hi"] * o["hi_er_share"]) * ctx["tau"] + row["hi_tax"]
    # when HI is kept, its 2.9% on all pay is the plan's own health payroll contribution from the endpoint (before it,
    # HI pays Medicare's claims for the people still in Medicare, outside the plan)
    kept = 0.0 if o["hi"] else HI_RATE * per_point(ctx["gap"], y)["payroll_gross"] * HI_ENDPOINT[y]
    src = dict(federal_general_revenue=rp_["federal"] - hi - kept, health_payroll_contribution=kept,
               states=rp_["states_booked"] + extra, employers=emp,
               households=hh_, hx_remainder=f["hx"] - lost, savings=sav)
    return dict(gross=gross, sources=src, hi_repealed=hi, check=sum(src.values()) - gross)


def line_variant(ctx, spec, line):
    """The package with the employer contribution's low-pay line at `line` instead of $20,000 (same total, so a higher
    rate on a narrower band), with its loser counts. Returns (package, micro, the rate in the band)."""
    import provisions as P
    K, _, _, _, X = keys()
    B, H, vals = X["B"], X["H"], X["vals"]
    keep_k, keep_v = K["wages_band"], dict(vals["band"])
    name = f"wages_band_{line}"
    P.RULES[name] = lambda u, L: _band_unit(u, L, line)
    try:
        K["wages_band"] = P.micro_shares(B, "rule:" + name)
        vals["band"].update(P.household_base(B, "rule:" + name))
        tot = sum(h["weight"] * vals["band"][h["hh"]] for h in H)
        o = package(ctx, **spec)
        m = micro(ctx, o)
    finally:
        K["wages_band"] = keep_k
        vals["band"].clear()
        vals["band"].update(keep_v)
    tot0 = sum(h["weight"] * vals["band"][h["hh"]] for h in H)
    return o, m, o["employer_rate"] * tot0 / tot


def design_levers(c, g40):
    """Effects on FY2040's cost of changes to the decided design (memo part 6), each on the coverage model's 2032
    full-scale groups scaled by g40, with everything else as decided ($ billion; a saving negative)."""
    HP, I, B, P = c["HP"], c["I"], c["B"], c["P"]
    base = sum(HP.groups(I, B, P)[0].values())
    out = {}
    t0 = HP.TARGET
    try:
        for t in (1.05, 1.10, 1.20):
            HP.TARGET = t
            out[f"rate_{t:.2f}"] = (sum(HP.groups(I, B, P, hosp_rate=t)[0].values()) - base) * g40
    finally:
        HP.TARGET = t0
    for name, key, val in [("admin_3pct", "sp_admin", 0.03), ("admin_4pct", "sp_admin", 0.04),
                           ("copays_none", "sp_cs_low_rate", 0.0), ("drugs_23pct", "sp_drug_cut", 0.23)]:
        J = dict(I)
        J[key] = val
        B2 = HP.M.build_base(J)
        B2 = dict(B2, S=dict(B2["S"], medicare=B["S"]["medicare"]), nhe0=B["nhe0"])
        out[name] = (sum(HP.groups(J, B2, P)[0].values()) - base) * g40
    return out


def growth_hold(ctx, extra=0.01, start=2037):
    """A national health budget that holds the plan's spending growth to nominal GDP growth plus `extra` from `start`
    (memo part 6): the FY2040 saving on the gross cost, against the model's growth path ($ billion)."""
    gp, gdp = ctx["growth"], ctx["gap"]["gdp"]
    g0 = ctx["gross_2036"]
    plan = g0 * gp[Y] / gp[2036]
    held = g0 * (gdp[Y] / gdp[2036]) * (1 + extra) ** (Y - start + 1)
    return held - plan, plan


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
        hi = HI_RATE * pp["payroll_gross"] * HI_ENDPOINT[y] if o40["hi"] else 0.0
        prem = o40["emp_share"] * f["employers"]
        left = phase_left(y) if o40["phase_in"] else 0.0
        d = left * o40["no_offer_share"] * prem
        if o40["credit"] and y >= PHASE_IN_START:   # the credit starts with the payroll-based contribution
            cr = sum(c["share"] * credit_key(c["start"], c["end"], left, c.get("nocov_only", False))[1]
                     for c in _credits(o40["credit"]))
            cbn = cr * prem * HI_ENDPOINT[y]
        else:
            cbn = 0.0
        emp_net = prem * (1 - ctx["tau"]) - d * (1 - ctx["tau"]) + hi * o40["hi_er_share"]
        sav = o40["savings"] * (need_p[y]["net"] / need_p[Y]["net"]) if o40["savings"] else 0.0
        ht = o40["hi_tax"] * (hi / o40["hi"]) if o40["hi"] else 0.0
        rest = need + hi + ht - emp_net - extra - sav + cbn
        s = max(rest, 0.0) / o40["household_collected"] if o40["household_collected"] else 0.0
        out[y] = dict(need=need, hi=hi, hi_tax=ht, employers=emp_net,
                      employer_gross=prem - d + hi * o40["hi_er_share"], phase_in=d, phase_left=left, credit=cbn,
                      states=extra,
                      savings=sav, households=rest, scale=s,
                      first=o40["first"] * s * ctx["pp"]["broad_income"] / pp["broad_income"],
                      second=o40["second"] * s * ctx["pp"]["high_income"] / pp["high_income"],
                      vat=o40["vat_rate"] * s * ctx["pp"]["vat"] / pp["vat"])
    return out


EXTRA_BASES = {}   # name -> function of a household record, for keys built from the households themselves


def household_key(name, f):
    """Register a key built from the 2029 households themselves: the fifths' and the top 1%'s shares of the weighted
    base f(h), for per_household(), and f itself for micro()'s spread."""
    K, _, _, _, X = keys()
    H = X["H"]
    tot = sum(h["weight"] * f(h) for h in H) or 1.0
    sh = [100 * sum(h["weight"] * f(h) for h in H if h["g5"] == q) / tot for q in range(1, 6)]
    t1 = 100 * sum(h["weight"] * f(h) for h in H if h["top1"]) / tot
    K[name] = (sh, t1)
    EXTRA_BASES[name] = f
    return sum(h["weight"] * f(h) for h in H)


def micro(ctx, o):
    """The spread inside each fifth: every household's net effect, FY2040, each row's quintile amount spread over the
    fifth's households in proportion to the household's own amount of that row's base, so the fifths' averages are
    exactly per_household()'s. Returns losers by fifth (millions of FY2040 households, share) and their profile."""
    K, hh = ctx["K"], ctx["hh"]
    _, _, _, _, X = keys()
    H, n29 = X["H"], X["n29"]
    base_of = _bases(ctx)
    scale = hh / n29
    net = {h["hh"]: 0.0 for h in H}
    for _, bn, key in o["rows"]:
        for k, v in row_amounts(ctx, bn, key, base_of).items():
            net[k] += v
    return _losers(ctx, net)


def _bases(ctx):
    """Each key's base in a household, for the spread inside each fifth."""
    _, _, _, _, X = keys()
    vals = X["vals"]
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
               "wages_cap": lambda h: h["wages_capped"], "wages_band": lambda h: vals["band"][h["hh"]],
               "income_line": lambda h: vals["base"][h["hh"]],
               "income_high": lambda h: vals["high"][h["hh"]], "consumption": lambda h: max(h["expanded"], 0.0),
               "persons": lambda h: h["numper"], "capital": lambda h: max(h["capital"], 0.0)}
    for a in AVOID_WEIGHTS:
        base_of[f"avoid_{a}"] = base_of["income_line"]
        base_of[f"avoid_high_{a}"] = base_of["income_high"]
    base_of.update(EXTRA_BASES)
    return base_of


def row_amounts(ctx, bn, key, base_of=None):
    """One row's dollars in each household, FY2040: its fifth's amount spread over the fifth's households in
    proportion to each household's base."""
    base_of = _bases(ctx) if base_of is None else base_of
    K, hh = ctx["K"], ctx["hh"]
    _, _, _, _, X = keys()
    H, n29 = X["H"], X["n29"]
    scale = hh / n29
    sh, _ = K[key]
    f = base_of[key]
    out = {}
    for q in range(1, 6):
        Hq = [h for h in H if h["g5"] == q]
        tot = sum(h["weight"] * f(h) for h in Hq)
        amt = bn * 1e9 * sh[q - 1] / 100
        for h in Hq:
            v = f(h) if tot > 0 else 1.0
            out[h["hh"]] = amt * v / ((tot if tot > 0 else sum(x["weight"] for x in Hq)) * scale)
    return out


def _losers(ctx, net):
    """Losers by fifth (millions of FY2040 households, share), each fifth's average and the losers' profile, from each
    household's net dollars."""
    _, _, _, _, X = keys()
    H, n29 = X["H"], X["n29"]
    scale = ctx["hh"] / n29
    grow = X["grow"]
    out = {}
    for q in range(1, 6):
        Hq = [h for h in H if h["g5"] == q]
        w = sum(h["weight"] for h in Hq)
        lw = sum(h["weight"] for h in Hq if net[h["hh"]] < 0)
        # net is in FY2040 dollars, so income is taken at FY2040's scale too (the 2029 income times `grow`; before
        # this fix the test compared FY2040 dollars with 2029 incomes, which overstated the counts)
        big = lambda t: sum(h["weight"] for h in Hq if net[h["hh"]] < -t * max(h["expanded"] * grow, 1.0))  # noqa: E731
        out[f"Q{q}"] = dict(losers_m=lw * scale / 1e6, share=100 * lw / w,
                            avg=sum(h["weight"] * net[h["hh"]] for h in Hq) / w,
                            lose_2pct_m=big(0.02) * scale / 1e6, lose_5pct_m=big(0.05) * scale / 1e6)
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
        median_loss=_wmedian([(-net[h["hh"]], h["weight"]) for h in L]))
    out["all_losers_m"] = sum(out[f"Q{q}"]["losers_m"] for q in range(1, 6))
    out["bottom_four_losers_m"] = sum(out[f"Q{q}"]["losers_m"] for q in range(1, 5))
    out["bottom_four_lose_5pct_m"] = sum(out[f"Q{q}"]["lose_5pct_m"] for q in range(1, 5))
    out["profile_bottom_four"] = prof
    out["_net"] = net
    return out


def _wmedian(pairs):
    """The weighted median of (value, weight) pairs."""
    if not pairs:
        return 0.0
    pairs = sorted(pairs)
    half, run = sum(w for _, w in pairs) / 2, 0.0
    for v, w in pairs:
        run += w
        if run >= half:
            return v
    return pairs[-1][0]


def employer_split(ctx, o):
    """At each household, FY2040: the employer premiums that become pay against the employer contribution charged on
    its pay (both before tax). Where premiums are larger, the pass-through rule makes the employer pay the difference
    into pay ('owed'); where the contribution is larger, the wage-maintenance rule stops the employer cutting pay
    rates, so the difference can come only out of future raises ('restraint'). Returns the totals ($ billion) and
    each household's restraint."""
    _, _, _, _, X = keys()
    H, scale = X["H"], ctx["hh"] / X["n29"]
    b = _bases(ctx)
    lab = {"Employer premiums that become pay": "cov", "Employer health contribution": "emp",
           "Phase-in for employers with no coverage in 2028: contribution not yet charged": "phase"}
    amt = {"cov": {}, "emp": {}, "phase": {}}
    for lb, bn, key in o["rows"]:
        for k, v in lab.items():
            if lb.startswith(k):
                amt[v] = row_amounts(ctx, bn, key, b)
    owed, restraint, per, per_owed = 0.0, 0.0, {}, {}
    for h in H:
        k = h["hh"]
        d = amt["cov"].get(k, 0.0) + amt["emp"].get(k, 0.0) + amt["phase"].get(k, 0.0)
        per[k] = max(-d, 0.0)
        per_owed[k] = max(d, 0.0)
        owed += h["weight"] * max(d, 0.0)
        restraint += h["weight"] * max(-d, 0.0)
    return dict(owed_bn=owed * scale / 1e9, restraint_bn=restraint * scale / 1e9, per=per, per_owed=per_owed)


def savings_kept_check(ctx, o, p=0.5, corp=0.21):
    """The pessimistic side: employers that save (former premiums above their contribution) pass only `p` of the
    saving into pay (Anand, EV-CAR-299, for the reverse case). Workers lose that pay and the tax on it is not paid,
    owners keep it after corporate tax, and the household rate rises to replace the lost tax. Returns the re-solved
    rate and households, and the loser counts."""
    sp = employer_split(ctx, o)
    po = sp["per_owed"]
    name = "savings_kept_owed"
    household_key(name, lambda h: po[h["hh"]])
    x = (1 - p) * sp["owed_bn"]
    tau = ctx["tau"]
    lost = x * (tau - corp)
    rows = [("Pay that does not rise where employers save", -x, name), ("Tax not paid on it", tau * x, name),
            ("Kept by owners, after corporate tax", (1 - corp) * x, "capital")]
    more = income_rows(lost, ctx["pp"])
    d = per_household(rows + more, ctx["K"], ctx["hh"])
    m = micro(ctx, dict(o, rows=o["rows"] + rows + more))
    return dict(kept_bn=x, tax_lost_bn=lost, first=o["first"] + lost / ctx["pp"]["broad_income"],
                households={g: o["households"][g] + d[g] for g in d}, micro=m)


def pay_holds_check(ctx, o, corp=0.21):
    """If pay holds where the contribution is above the employer's former premiums (the restraint in employer_split()
    never happens), employers bear that difference instead of their workers: their workers keep the pay and pay tax on
    it, owners bear it after corporate tax, and the household rate falls by the net tax gained. The worker transition
    credit is still paid. Returns the re-solved package and its loser counts."""
    sp = employer_split(ctx, o)
    per = sp["per"]
    name = "pay_holds_restraint"
    household_key(name, lambda h: per[h["hh"]])
    x = sp["restraint_bn"]
    tau = ctx["tau"]
    gained = x * (tau - corp)
    rows = [("Pay that holds where the contribution exceeds former premiums", x, name),
            ("Tax on the pay that holds", -tau * x, name), ("Borne by owners, after corporate tax", -(1 - corp) * x,
                                                             "capital")]
    lower = income_rows(-gained, ctx["pp"])
    o2 = dict(o, rows=o["rows"] + rows + lower)
    d = per_household(rows + lower, ctx["K"], ctx["hh"])
    m = micro(ctx, o2)
    return dict(restraint_bn=x, owed_bn=sp["owed_bn"], tax_gained_bn=gained,
                first=o["first"] - gained / ctx["pp"]["broad_income"],
                households={g: o["households"][g] + d[g] for g in d}, micro=m)


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


HEALTH_GROWTH_TOTAL = 0.054   # CMS's projection of national health spending, 2025-34, a year (EV-CAR-056)


def _pop_growth():
    """Population growth a year, 2026-36: CBO's civilian population aged 16 and over (the household model's CBO
    series), the proxy for turning total health spending growth into growth per person (the review of #385)."""
    from params import econ
    return (econ("population_civ_16yo", 2036) / econ("population_civ_16yo", 2026)) ** 0.1 - 1


# health spending per person: CMS's total growth less population growth
HEALTH_GROWTH = (1 + HEALTH_GROWTH_TOTAL) / (1 + _pop_growth()) - 1


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
             consume=0.95, no_offer=True, nocov=True),
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
    # the lines are price-indexed while these examples hold incomes at today's dollars of income, so in these terms
    # the lines shrink by prices over incomes, 2026 to FY2040 (the independent cross-check, memo part 8)
    lf = ctx["price_2040"] / inc_back
    payroll_t = 0.124 + (0.0 if o["hi"] else HI_RATE / 100)   # both halves of payroll tax that remain on pay
    out = []
    for c in cases:
        line1, line2 = ((40000, 200000) if c["joint"] else (20000, 100000))
        line1, line2 = line1 * lf, line2 * lf
        prem_today = gg * (c["ee_prem"]) + c["own"]
        stop = prem_today + c["oop"] - copay * c["people"]
        tax_ee = -(c["m"] + payroll_t) * gg * c["ee_prem"]   # the former pre-tax premium share is now taxable (HX)
        # the employer's base: pay up to the wage base, less the low-pay line where the package has it ($184,500 is
        # the 2026 Social Security wage base)
        cap = lambda x: min(x, 184500) - (LOW_PAY_LINE * lf if o["emp_base"] == "payroll_band" else 0)  # noqa: E731
        base_e = (x if o["emp_base"] == "payroll" else max(cap(x), 0.0)) if (x := c["wages"]) else 0.0
        hi_ee = HI_RATE / 200 * c["wages"] if o["hi"] else 0.0       # the worker's HI half, repealed
        er_saved = gg * c["er_prem"] + (HI_RATE / 200 * c["wages"] if o["hi"] else 0.0)
        # employers with no 2028 coverage pay only the phased-in part of the rate in FY2040
        er_new = er * base_e * ((1 - o["phase_in"]) if c.get("no_offer") else 1.0)
        pay_change = er_saved - er_new
        tax_pay = -(c["m"] + payroll_t) * pay_change
        # AGI after the plan: the pay change and the former pre-tax premium share are now in it
        agi = c["agi"] + pay_change + gg * c["ee_prem"]
        base1, base2 = max(agi - line1, 0), max(agi - line2, 0)
        contrib = -(r1 * base1 + r2 * base2)
        se = 0.9235 * c.get("se", 0)
        se_base = (se if o["emp_base"] == "payroll" else max(min(se, 184500) - (LOW_PAY_LINE * lf if o["emp_base"] ==
                                                                                      "payroll_band" else 0), 0.0))
        se_contrib = -er * se_base + (HI_RATE / 100 * se if o["hi"] else 0.0)   # SECA's HI part ends
        vat = (-v * c["consume"] * c["cash"] + rebate_pp * c["people"]) if v else 0.0
        # the worker transition credit: the contribution charged on the pay of someone with no employer coverage in
        # 2028, phased out with AGI (its lines price-indexed like the others)
        credit = 0.0
        for cr in _credits(o["credit"]):
            if c.get("nocov") or not cr.get("nocov_only"):
                a0, a1 = (cr["start"] * lf * (2 if c["joint"] else 1), cr["end"] * lf * (2 if c["joint"] else 1))
                ph = 1.0 if agi <= a0 else max(0.0, (a1 - agi) / (a1 - a0))
                credit += cr["share"] * ph * (er_new + er * se_base)
        net = stop + tax_ee + hi_ee + pay_change + tax_pay + contrib + se_contrib + vat + credit
        out.append(dict(name=c["name"], premiums_stop=round(prem_today), out_of_pocket_stop=round(c["oop"]),
                        copays=round(-copay * c["people"]), stop_paying=round(stop), hx_on_worker_share=round(tax_ee),
                        employer_saves=round(er_saved), employer_pays=round(er_new), pay_change=round(pay_change),
                        tax_on_pay_change=round(tax_pay), worker_hi_ends=round(hi_ee), employer_base=round(base_e),
                        agi=round(agi), lines=round(line1), base=round(base1), base2=round(base2),
                        rate1=o["first"], rate2=o["second"], contribution=round(contrib),
                        self_employed=round(se_contrib), vat=round(vat), credit=round(credit), net=round(net),
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
    ctx["replaced_p"] = replaced_path(c)
    n40, r40 = need_p[2036], ctx["replaced_p"][2036]
    ctx["gross_2036"] = n40["spending"] + n40["seam"] + r40["federal"] + r40["states_booked"]
    gf = HB.health_path()["gf"]
    ctx["growth"] = {y: gf[y] for y in YEARS}
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
        "A_employer_capped_no_low_pay_line": package(ctx, **dict(PACKAGES["A"], emp_base="payroll_cap")),
        "A_hi_folded": package(ctx, **dict(PACKAGES["A"], replace_hi=True, hi_er_share=1.0)),
        "A_hi_split": package(ctx, **dict(PACKAGES["A"], replace_hi=True, hi_er_share=0.5)),
        "D_top_avoidance_60": package(ctx, **dict(PACKAGES["D"], high_avoid=0.6)),
        "B_first_6": package(ctx, **dict(PACKAGES["B"], first=6.0)),
        "B_first_5": package(ctx, **dict(PACKAGES["B"], first=5.0)),
        # the fix's parts and its alternatives (memo parts 2.6, 2.7 and 4.3)
        "A_before_fix": package(ctx, **dict(PACKAGES["A"], **BEFORE_FIX)),
        "A_phase_in_only": package(ctx, **dict(PACKAGES["A"], credit=None)),
        "A_credit_only": package(ctx, **dict(PACKAGES["A"], phase_in=0.0)),
        "A_credit_75pct": package(ctx, **dict(PACKAGES["A"], credit=dict(WORKER_CREDIT, share=0.75))),
        "A_credit_50_100k": package(ctx, **dict(PACKAGES["A"], credit=dict(WORKER_CREDIT, start=50000,
                                                                               end=100000))),
        "A_credit_all_workers": package(ctx, **dict(PACKAGES["A"], credit=dict(WORKER_CREDIT, nocov_only=False))),
        "A_credit_all_workers_half": package(ctx, **dict(PACKAGES["A"], credit=dict(WORKER_CREDIT, share=0.5,
                                                                                        nocov_only=False))),
        # the long run, once the phase-in and the transition credit have ended, priced on FY2040's economy (A as
        # merged), with a permanent credit for every low-paid worker as the alternative (memo part 9): the
        # contribution on their pay, phased out between $30,000 and $60,000
        "A_long_run_low_pay_credit": package(ctx, **dict(PACKAGES["A"], phase_in=0.0, credit=dict(
            share=1.0, start=30000, end=60000, nocov_only=False))),
    }
    # the first draft's package on the corrected method, for the trace (employers 65% on payroll, states 80%)
    S["first_draft"] = package(ctx, emp_share=0.65, state_share=0.8, emp_base="payroll", replace_hi=False,
                               need=ctx["need_p"][Y]["booked"])
    paths_ = {k: package_path(ctx, PACKAGES[k], ctx["need_p"], ctx["flows_p"], gap) for k in P}
    rc = payers(c, g40)
    rc_booked = payers(coverage(False), g40)
    micro_ = {k: micro(ctx, P[k]) for k in P}
    micro_["A_states_80"] = micro(ctx, S["A_states_80"])
    for k in ("A_employer_uncapped", "A_employer_capped_no_low_pay_line", "A_hi_folded", "A_with_savings",
              "A_before_fix", "A_phase_in_only", "A_credit_only", "A_credit_75pct", "A_credit_50_100k",
              "A_credit_all_workers", "A_credit_all_workers_half", "A_long_run_low_pay_credit"):
        micro_[k] = micro(ctx, S[k])
    # the low-pay line at $30,000 instead of the credit (memo part 4.3)
    o30, m30, r30 = line_variant(ctx, dict(PACKAGES["A"], credit=None), 30000)
    S["A_line_30k_no_credit"] = o30
    micro_["A_line_30k_no_credit"] = m30
    split = employer_split(ctx, P["A"])
    split.pop("per")
    split.pop("per_owed")
    holds = pay_holds_check(ctx, P["A"])
    kept = savings_kept_check(ctx, P["A"])
    levers = design_levers(c, g40)
    gh = {e: growth_hold(ctx, e) for e in (0.0, 0.01)}
    # the design memos' recommendations (memo part 6): administration booked at 4% (target 3%) and a national budget
    # holding growth to GDP plus 1 point from 2037; both lower the need, closed by the household rate
    design_saving = -(levers["admin_4pct"] + gh[0.01][0])
    S["A_with_design_memos"] = package(ctx, **dict(PACKAGES["A"], savings=design_saving))
    micro_["A_with_design_memos"] = micro(ctx, S["A_with_design_memos"])
    views = {k: system_view(ctx, P[k]) for k in P}
    path_views = {y: system_view(ctx, P["A"], y, paths_["A"][y]) for y in YEARS}
    statutory = P["A"]["rows"]
    st_charge = -[bn for lb, bn, _ in statutory if lb.startswith("First tier: the statutory")][0]
    base_2040 = st_charge / (P["A"]["first"] / 100)
    sh, t1 = K["income_line"]
    implied = {g_: base_2040 * 1e9 * s / 100 / (hh * 0.2) for g_, s in zip(GROUPS, sh)}
    implied["T1"] = base_2040 * 1e9 * t1 / 100 / (hh * 0.01)
    # health costs per person grow with CMS's projection of national health spending, 5.4% a year (EV-CAR-056), less
    # population growth, against nominal income per household on the model's path (2029 to FY2040)
    gg = ((1 + HEALTH_GROWTH) / (1 + ctx["income_growth"])) ** (Y - 2026)
    ex = {k: examples(ctx, P[k], gg) for k in P}
    ex["A_before_fix"] = examples(ctx, S["A_before_fix"], gg)
    tc = {k: topcode_check(P[k], K, hh) for k in P}
    stk = {k: stacking_check(P[k], K, pp) for k in P}
    stk["A_employer_uncapped"] = stacking_check(S["A_employer_uncapped"], K, pp)
    adj = {}
    for name, spec in (("A", PACKAGES["A"]), ("A_employer_uncapped", dict(PACKAGES["A"], emp_base="payroll")),
                       ("A_employer_capped_no_low_pay_line", dict(PACKAGES["A"], emp_base="payroll_cap")),
                       ("B", PACKAGES["B"])):
        for e in (0.12, TOP1_ELASTICITY, 0.4, 0.57):
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
                group_payers_2032=ctx["gp"], micro={k: {a: b for a, b in v.items() if a != "_net"}
                                                    for k, v in micro_.items()}, examples=ex, growth_gap=gg, topcode=tc, stacking=stk,
                passthrough=pt, hi=hi, stacking_adjusted=adj, views=views, path_views=path_views, levers=levers,
                growth_hold=gh, band_share=band_share(), replaced_path=ctx["replaced_p"], g40=g40, pp_person=ctx["pp_person"],
                before_financing=per_household(relief_rows(ctx["f40"]), K, hh),
                no_offer={k: v for k, v in no_offer().items() if k != "drawn"},
                phase_left={y: phase_left(y) for y in YEARS}, line_30k_rate=r30, employer_split=split,
                pay_holds=dict(holds, micro={k: v for k, v in holds["micro"].items() if k != "_net"}),
                savings_kept=dict(kept, micro={k: v for k, v in kept["micro"].items() if k != "_net"}))


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
    kept = (1 - p) * max(f["employers"] - o["employer_premium_part"], 0.0)
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
    for k in ("A_employer_uncapped", "A_employer_capped_no_low_pay_line", "A_hi_folded", "A_with_savings"):
        print("micro", k, {q: (round(v["losers_m"], 1) if isinstance(v, dict) and "losers_m" in v else v)
                           for q, v in r["micro"][k].items() if q != "profile_bottom_four"})
    for k, v in r["views"].items():
        print("view", k, round(v["gross"]), {a: round(b) for a, b in v["sources"].items()}, round(v["check"], 6))
    for y, v in r["path_views"].items():
        print("path view", y, round(v["gross"]), {a: round(b) for a, b in v["sources"].items()}, round(v["check"], 6))
    print("levers", {k: round(v) for k, v in r["levers"].items()}, "growth hold",
          {k: (round(a), round(b)) for k, (a, b) in r["growth_hold"].items()}, "band share", round(r["band_share"], 4))
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
