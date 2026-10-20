"""Dedicated-fund engine: year-by-year balances for the funds the general-fund ledger leaves out.

  Social Security (OASDI, 75 years), Medicare HI (75 years, summary level), the paid-leave fund (FAM-3),
  the Highway Trust Fund's three accounts (from the transportation model), the carbon channel (REV-C1, C2),
  and the held education fund (EDU-9B, if it is taken up).

Inputs: index/data/inputs/funds-*.csv (the 2026 Trustees tables and this model's parameters), ledger.json,
fiscal-model.json and moving-america.json from the same run. Writes funds.json and dedicated-funds.md.
Dollar figures are nominal $B a year unless marked; ten-year sums are 2030-39 in $T.
"""
import json, math, os, sys
from inputs import read, num

HERE = os.path.dirname(os.path.abspath(__file__))
for d in (os.path.join(HERE, "transportation"), os.path.join(HERE, "..", "index", "tools", "transportation")):
    if os.path.exists(os.path.join(d, "moving_america.py")): sys.path.insert(0, d)
import moving_america as ma

def _val(s):
    try: return num(s)
    except ValueError: return s.strip()
P = {r["key"]: _val(r["value"]) for r in read("funds-parameters.csv")}
L = json.load(open("ledger.json"))
FM = json.load(open("fiscal-model.json"))
REV = {r["id"]: r for r in L["revenue"]}
BILL = {b["id"]: b for b in L["bills"]}
YEARS = range(2026, 2101)
W = range(2030, 2040)

# ---------- Trustees economics: payroll, GDP and the trust-fund interest rate, interpolated geometrically ----------
RATES = {int(r["year"]): (float(r["income_rate"]), float(r["cost_rate"])) for r in read("funds-ss-rates.csv")}
ECON = {int(r["year"]): (float(r["taxable_payroll_bn"]), float(r["gdp_bn"]), float(r["interest_factor"])) for r in read("funds-ss-economics.csv")}
ECON[2025] = (ECON[2026][0] / (ECON[2027][0] / ECON[2026][0]), ECON[2026][1] / (ECON[2027][1] / ECON[2026][1]), 1.0)

def _geo(t, k):
    ys = sorted(ECON)
    if t in ECON: return ECON[t][k]
    if t > ys[-1]:
        a, b = ys[-2], ys[-1]
        return ECON[b][k] * (ECON[b][k] / ECON[a][k]) ** ((t - b) / (b - a))
    a = max(y for y in ys if y < t); b = min(y for y in ys if y > t)
    return ECON[a][k] * (ECON[b][k] / ECON[a][k]) ** ((t - a) / (b - a))

def payroll(t): return _geo(t, 0)
def gdp(t): return _geo(t, 1)
def ifac(t): return _geo(t, 2)
def rate(t): return ifac(t) / ifac(t - 1) - 1

# ---------- Social Security ----------
def ss_provisions():
    """Each provision as a change in the income rate (+) or cost rate (-) from its start year, in % of payroll.
    Shape: 'level', or 'rising' (linear from the start level to a higher level by the end year, then flat).
    Scaled so the 75-year present value equals the provision's actuarial value; where the ledger carries an
    in-window dollar figure, the start level is set from it and the slope from the actuarial value."""
    out = {}
    for r in read("funds-ss-provisions.csv"):
        out[r["id"]] = dict(av=float(r["actuarial_value"]), side=r["side"], shape=r["shape"], start=int(r["start"]),
                            ramp_end=int(r["ramp_end"]) if r["ramp_end"] else None,
                            window_bn=eval_ledger(r["window_ledger"]) if r["window_ledger"] else None,
                            label=r["label"], basis=r["basis"])
    return out

def eval_ledger(expr):
    """'O2+OX' -> the ledger's midpoint sum, in $B."""
    return 1000 * sum(REV[i.strip()]["mid"] for i in expr.split("+"))

PV = {t: 1 / ifac(t) for t in range(2025, 2102)}
PVPAY = sum(payroll(t) * PV[t] for t in YEARS)

def shape_fn(p, a, b):
    """Level a in the start year, rising linearly to a+b by ramp_end (b = 0 for level)."""
    def f(t):
        if t < p["start"]: return 0.0
        if p["shape"] == "level" or not p["ramp_end"]: return a
        x = min((t - p["start"]) / (p["ramp_end"] - p["start"]), 1.0)
        return a + b * x
    return f

def calibrate(p):
    """Solve for the start level a and the rise b: the 75-year value always matches; where the ledger has a
    ten-year figure, the 2030-39 dollars match it too (two equations, two unknowns)."""
    unit_a = shape_fn(p, 1.0, 0.0)
    unit_b = shape_fn(p, 0.0, 1.0) if p["shape"] == "rising" else (lambda t: 0.0)
    pv = lambda f: sum(f(t) / 100 * payroll(t) * PV[t] for t in YEARS)
    target = p["av"] / 100 * PVPAY
    if p["window_bn"] is not None and p["shape"] == "rising":
        s = lambda f: sum(f(t) / 100 * payroll(t) for t in W)
        a11, a12, a21, a22 = s(unit_a), s(unit_b), pv(unit_a), pv(unit_b)
        det = a11 * a22 - a12 * a21
        a = (p["window_bn"] * a22 - a12 * target) / det
        b = (a11 * target - a21 * p["window_bn"]) / det
        return shape_fn(p, a, b)
    unit = (lambda t: unit_a(t) + unit_b(t)) if p["shape"] == "rising" else unit_a
    k = target / pv(unit)
    return lambda t: k * unit(t)

SSP = ss_provisions()
SSF = {i: calibrate(p) for i, p in SSP.items()}
SS_SCEN = {"Current law": [], "D8 baseline": ["SS-1", "SS-2", "SS-3", "SS-4"], "D8 + SS-5": ["SS-1", "SS-2", "SS-3", "SS-4", "SS-5"]}

def run_ss(ids):
    R = P["ss_reserve_2025"]; rows = []; depl = None
    for t in YEARS:
        inc, cost = RATES[t]
        for i in ids:
            d = SSF[i](t)
            if SSP[i]["side"] == "income": inc += d
            else: cost += d
        pay = payroll(t); r = rate(t)
        start = R
        net = (inc - cost) / 100 * pay
        R = R * (1 + r) + net * (1 + r / 2)
        tfr = start / (cost / 100 * pay) * 100
        if R < 0 and depl is None:
            depl = t; payable = inc / cost
        rows.append(dict(year=t, income=inc, cost=cost, reserve=R, tfr=tfr))
    # actuarial balance over 2026-2100 (Trustees' summarized rates, with the ending-fund target)
    pv_inc = sum(r["income"] / 100 * payroll(r["year"]) * PV[r["year"]] for r in rows) + P["ss_reserve_2025"]
    pv_cost = sum(r["cost"] / 100 * payroll(r["year"]) * PV[r["year"]] for r in rows) + rows[-1]["cost"] / 100 * payroll(2101) * PV[2100]
    bal = (pv_inc - pv_cost) / PVPAY * 100
    last = [r["tfr"] for r in rows[-6:]]
    sustainable = depl is None and last[-1] >= 100 and last[-1] >= last[0] - 0.5
    return dict(rows=rows, depletion=depl, payable=(payable * 100 if depl else None), balance=bal, sustainable=sustainable)

ss = {k: run_ss(v) for k, v in SS_SCEN.items()}
base_gap = -ss["Current law"]["balance"]
for k in ss: ss[k]["closed"] = (ss[k]["balance"] - ss["Current law"]["balance"]) / base_gap * 100
ss_window = {i: sum(SSF[i](t) / 100 * payroll(t) for t in W) / 1000 for i in SSF}

# ---------- Medicare HI (summary level: the Trustees' cost and income rates, interpolated) ----------
HI = read("funds-hi-rates.csv")
def _lin(pts, t):
    ys = sorted(pts)
    if t <= ys[0]: return pts[ys[0]]
    if t >= ys[-1]: return pts[ys[-1]]
    a = max(y for y in ys if y <= t); b = min(y for y in ys if y >= t)
    return pts[a] if a == b else pts[a] + (pts[b] - pts[a]) * (t - a) / (b - a)
HI_COST = {int(r["year"]): float(r["cost_rate"]) for r in HI if r["cost_rate"]}
HI_INC = {int(r["year"]): float(r["income_rate"]) for r in HI if r["income_rate"]}
def hi_payroll(t): return payroll(t) * P["hi_payroll_ratio"]

def hi_sources():
    """REV-H1a and HLT-6's Part A share, spread over 2030-39 on a ramp, then held as a share of HI payroll."""
    ramp = [float(x) for x in str(P["hi_ramp"]).split("/")]
    tot = (REV["H1a"]["mid"] + P["hi_hlt6_share_tn"]) * 1000
    w = {t: ramp[t - 2030] * hi_payroll(t) for t in W}
    s = tot / sum(w.values())
    out = {t: s * w[t] / hi_payroll(t) * 100 for t in W}           # % of HI payroll
    return lambda t: 0.0 if t < 2030 else out.get(t, out[2039])

HIS = hi_sources()
def run_hi(with_program):
    R = P["hi_reserve_2025"]; depl = None; rows = []
    for t in YEARS:
        inc = _lin(HI_INC, t) + (HIS(t) if with_program else 0); cost = _lin(HI_COST, t)
        pay = hi_payroll(t); r = rate(t)
        R = R * (1 + r) + (inc - cost) / 100 * pay * (1 + r / 2)
        if R < 0 and depl is None: depl = t; payable = inc / cost
        rows.append(dict(year=t, income=inc, cost=cost, reserve=R))
    PVH = sum(hi_payroll(t) * PV[t] for t in YEARS)
    bal = (sum((r["income"] - r["cost"]) / 100 * hi_payroll(r["year"]) * PV[r["year"]] for r in rows) + P["hi_reserve_2025"]
           - rows[-1]["cost"] / 100 * hi_payroll(2101) * PV[2100]) / PVH * 100
    return dict(rows=rows, depletion=depl, payable=(payable * 100 if depl else None), balance=bal)
hi = {"Current law": run_hi(False), "With HI's program sources": run_hi(True)}
hi_window = sum(HIS(t) / 100 * hi_payroll(t) for t in W) / 1000

# ---------- Paid leave (FAM-3): 0.6% from 2030, benefits from 2031, automatic step-up to 0.85%, Treasury loan ----------
def run_leave(case):
    b = BILL["FAM-3"]; target = {"low": b["cost_lo"], "mid": b["cost_mid"], "high": b["cost_hi"]}[case] * 1000
    ramp = [float(x) for x in P["leave_ramp"].split("/")]
    ben_shape = {t: (ramp[t - 2031] if t - 2031 < len(ramp) else 1.0) * payroll(t) for t in range(2031, 2101) if t <= 2039}
    mature = target / sum(ben_shape.values())                     # mature cost, share of payroll
    def ben(t): return 0.0 if t < 2031 else (ramp[t - 2031] if t - 2031 < len(ramp) else 1.0) * mature * payroll(t)
    rt = P["leave_rate"]; R = 0.0; loan = 0.0; rows = []; first_step = None; peak_loan = 0.0
    for t in range(2030, 2061):
        if t > 2030:
            nxt = ben(t)
            res = R - loan
            if res < P["leave_low_years"] * nxt and rt < P["leave_cap"] - 1e-9:
                rt = round(rt + P["leave_step"], 4); first_step = first_step or t
            elif res > P["leave_high_years"] * nxt and rt > P["leave_rate"] + 1e-9:
                rt = round(rt - P["leave_step"], 4)
        r = rate(t)
        R = R * (1 + r) + (rt / 100 * payroll(t) - ben(t))
        if R < 0: loan += -R; R = 0.0
        loan *= 1 + r
        if loan > 0 and R > 0:
            pay = min(loan, R); loan -= pay; R -= pay
        peak_loan = max(peak_loan, loan)
        rows.append(dict(year=t, rate=rt, receipts=rt / 100 * payroll(t), benefits=ben(t), reserve=R, loan=loan))
    win = [x for x in rows if x["year"] in W]
    return dict(case=case, mature_cost=mature * 100, rows=rows, first_step=first_step, peak_loan=peak_loan,
                loan_2039=next(x["loan"] for x in rows if x["year"] == 2039), loan_2050=next(x["loan"] for x in rows if x["year"] == 2050),
                receipts_w=sum(x["receipts"] for x in win) / 1000, benefits_w=sum(x["benefits"] for x in win) / 1000,
                at_cap_w=sum(P["leave_cap"] / 100 * payroll(t) for t in W) / 1000,
                at_start_w=sum(P["leave_rate"] / 100 * payroll(t) for t in W) / 1000)
leave = {c: run_leave(c) for c in ("low", "mid", "high")}

# ---------- Highway Trust Fund (from the transportation model) ----------
M = ma.Model()
htf = []
for t in range(2029, 2047):
    a = M.allocate(t)
    htf.append(dict(fy=t, **{f"{k}_{m}": a[k][m] for k in ("ded", "prog", "gf", "trapped") for m in ("hwy", "tra", "rail")}))

# ---------- Carbon channel (REV-C1, REV-C2) ----------
PH = {r["id"]: r for r in read("incidence-phase-in.csv")}
cw = [float(PH["C1"][f"y{t}"]) for t in W]
c1 = {t: REV["C1"]["mid"] * 1000 * w / sum(cw) for t, w in zip(W, cw)}
c2 = {t: REV["C2"]["mid"] * 1000 * w / sum(cw) for t, w in zip(W, cw)}
def pop(t): return P["pop_2030_m"] * (1 + P["pop_growth"]) ** (t - 2030)
carbon = [dict(year=t, c1=c1[t], c2=c2[t], dividend=P["carbon_dividend_share"] * c1[t],
               transition=(1 - P["carbon_dividend_share"]) * c1[t],
               per_person=P["carbon_dividend_share"] * c1[t] * 1e9 / (pop(t) * 1e6)) for t in W]

# ---------- EDU-9B (held): payroll contribution + estate component against the session's spending path ----------
EPATH = {2030: 142, 2033: 264, 2036: 301, 2040: 327, 2049: 442}
def edu_out(t): return _geo_pts(EPATH, t)
def _geo_pts(pts, t):
    ys = sorted(pts)
    if t in pts: return pts[t]
    a = max(y for y in ys if y < t); b = min(y for y in ys if y > t)
    return pts[a] * (pts[b] / pts[a]) ** ((t - a) / (b - a))
def run_edu(rate_pts, estate_w_tn):
    e0 = estate_w_tn * 1000 / sum((1 + P["edu_estate_growth"]) ** (t - 2030) for t in W)
    R = 0.0; trough = (1e9, None); rows = []
    for t in range(2030, 2050):
        rec = rate_pts * P["edu_point_2030_bn"] * (1 + P["edu_base_growth"]) ** (t - 2030) + e0 * (1 + P["edu_estate_growth"]) ** (t - 2030)
        R = R * (1 + rate(t)) + rec - edu_out(t)
        if R < trough[0]: trough = (R, t)
        rows.append(dict(year=t, receipts=rec, outlays=edu_out(t), reserve=R))
    return dict(rate=rate_pts, rows=rows, trough=trough, reserve_2049=R)
def solve_edu(estate):
    lo, hi_ = 0.8, 3.0
    for _ in range(40):
        m = (lo + hi_) / 2
        if run_edu(m, estate)["trough"][0] >= 0: hi_ = m
        else: lo = m
    return hi_
edu = {"E1 counted ($0.35T)": P["edu_estate_e1_tn"], "E1's new money only ($0.15T)": P["edu_estate_new_tn"]}
edu_runs = {k: dict(need=solve_edu(v), at128=run_edu(1.28, v), at140=run_edu(1.40, v)) for k, v in edu.items()}
FR = {r["id"]: r for r in FM["rows"]}
edu_relief = sum(FR[i]["gf"][str(t)] for i in ("FAM-2", "EDU-1", "EDU-3", "EDU-4") for t in W) / 1000
edu_out_w = sum(edu_out(t) for t in W) / 1000

# ---------- outputs ----------
def tn(x): return f"{x:.2f}"
out = dict(ss={k: {kk: vv for kk, vv in v.items() if kk != "rows"} | {"tfr": {r["year"]: round(r["tfr"]) for r in v["rows"] if r["year"] % 10 == 0}} for k, v in ss.items()},
           ss_window_tn={k: round(v, 3) for k, v in ss_window.items()},
           hi={k: {kk: vv for kk, vv in v.items() if kk != "rows"} for k, v in hi.items()}, hi_window_tn=round(hi_window, 3),
           leave={k: {kk: vv for kk, vv in v.items() if kk != "rows"} for k, v in leave.items()},
           htf=htf, carbon=carbon,
           edu={k: dict(need=round(v["need"], 2), trough_128=v["at128"]["trough"], trough_140=v["at140"]["trough"],
                        reserve_2049_128=v["at128"]["reserve_2049"], reserve_2049_140=v["at140"]["reserve_2049"]) for k, v in edu_runs.items()},
           edu_relief_tn=edu_relief, edu_outlays_w_tn=edu_out_w)
json.dump(out, open("funds.json", "w"), indent=1, default=float)

L_ = []
w = L_.append
cl = ss["Current law"]
w("# Dedicated funds: year-by-year balances\n")
w("*Generated by `index/tools/funds-model.py` (run by `run-all.sh`); do not edit by hand. Inputs: `index/data/inputs/funds-*.csv` (the 2026 Trustees tables and this model's parameters), the ledger, the long-term fiscal model and the transportation model from the same run.*\n")
w("The general-fund ledger counts only general-fund money. This file follows the funds it leaves out: Social Security and Medicare HI over 75 years, the paid-leave fund, the Highway Trust Fund's three accounts, the carbon channel, and the held education fund (EDU-9B). Dollar figures are nominal; ten-year sums are 2030-39 in trillions.\n")

w("## Social Security (D8)\n")
w(f"**Check against the Trustees.** Run on the 2026 Trustees' intermediate rates, the model puts combined-fund depletion in **{cl['depletion']}** with **{cl['payable']:.0f}%** of benefits payable, and the 75-year actuarial balance at **{cl['balance']:.2f}%** of taxable payroll. The Trustees report 2034, 83% and −4.42% (sourced). The model's balance is the Trustees' summarized-rate formula on their annual rates, so a small difference is rounding in the published rates and the interest path.\n")
w("**Provisions.** Each is entered as a change in the income or cost rate from its start year, scaled so its 75-year value matches its score; where the ledger carries a ten-year dollar figure (SS-1's O1, SS-2's O2 less the OX haircut), the starting level is set from that figure and the rise from the score, so the two agree. Interactions between provisions are ignored, as in the domain file.\n")
w("| ID | Change | 75-year value (% of payroll) | Shape | 2030-39 ($T) | In 2031 / 2050 / 2090 (% of payroll) | Basis |")
w("| --- | --- | --- | --- | --- | --- | --- |")
for i, p in SSP.items():
    f = SSF[i]
    w(f"| {i} | {p['label']} | {'+' if p['side']=='income' else '−'}{p['av']:.2f} | {p['shape']} | {ss_window[i]:.2f} | {f(2031):.2f} / {f(2050):.2f} / {f(2090):.2f} | {p['basis']} |")
w("")
w("| Scenario | Depletion | Payable then | 75-year balance | Share of the gap closed | Sustainable solvency | Trust fund ratio 2040 / 2060 / 2080 / 2100 |")
w("| --- | --- | --- | --- | --- | --- | --- |")
for k, v in ss.items():
    t = {r["year"]: r["tfr"] for r in v["rows"]}
    tf = " / ".join(f"{max(t[y],0):.0f}%" for y in (2040, 2060, 2080, 2100))
    pay = f"{v['payable']:.0f}%" if v["depletion"] else "—"
    w(f"| {k} | {v['depletion'] or 'none by 2100'} | {pay} | {v['balance']:+.2f} | {v['closed']:.0f}% | {'yes' if v['sustainable'] else 'no'} | {tf} |")
w("")
d8 = ss["D8 baseline"]; d5 = ss["D8 + SS-5"]
w(f"**Reading.** The D8 baseline closes about {d8['closed']:.0f}% of the gap (the domain file's 65-72%, estimate) and moves depletion from {cl['depletion']} to {d8['depletion'] or 'beyond 2100'}. With SS-5 it closes {d5['closed']:.0f}% (domain file: 86-92%) and depletion moves to {d5['depletion'] or 'beyond 2100'}. The trust fund ratio is the reserve at the start of a year over that year's cost; 'sustainable' means no depletion through 2100 and a ratio of at least 100% that is not falling at the end, the Trustees' test. All three readings are estimates: the shapes over time are this model's, and only an SSA score of the package would replace them. SS-10 (the bipartisan trade) is not modeled; it needs an SSA score of its pieces.\n")

w("## Medicare HI (summary level)\n")
hc, hp = hi["Current law"], hi["With HI's program sources"]
w(f"Rates are the 2026 Trustees' HI cost and income rates at the years they publish, interpolated between (sourced); HI's taxable payroll is taken as {P['hi_payroll_ratio']:.2f} times OASDI's because it is uncapped (estimate). **Check:** the model puts depletion in **{hc['depletion']}** with {hc['payable']:.0f}% payable and a 75-year balance of **{hc['balance']:.2f}%**, against the Trustees' 2033, 89% and −0.56% (sourced).\n")
gain = hp["balance"] - hc["balance"]
w(f"**With the program.** HI's sources in the program are REV-H1a (${REV['H1a']['mid']:.1f}T) and HLT-6's Part A share (${P['hi_hlt6_share_tn']:.1f}T, estimate), ${hi_window:.2f}T in 2030-39, held at the same share of HI payroll after 2039 (estimate). They improve the 75-year balance by **{gain:+.2f}%** of HI payroll, against the Trustees' 0.56% gap"
  + (", so they close it on this reading" if gain >= 0.56 else f", leaving about {0.56-gain:.2f}% for a further HI source") + f"; on the model's own rates HI then depletes in {hp['depletion'] or 'no year before 2100'}"
  + f" and the balance is {hp['balance']:+.2f}%. Because the model's current-law balance is {hc['balance']-(-0.56):+.2f} points off the Trustees', the gain (not the model's absolute balance) is the reading to use; a year-by-year Trustees HI table would sharpen it.\n")

w("## Paid leave (FAM-3)\n")
lm = leave["mid"]
w(f"The contribution starts at {P['leave_rate']:.2f}% of covered payroll in 2030 (Trustees' taxable payroll used as the base, estimate) and benefits start in 2031, ramping over {len(P['leave_ramp'].split('/'))} years. Benefit cost is set so 2030-39 benefits match the ledger's FAM-3 range (${BILL['FAM-3']['cost_lo']:.1f}T / ${BILL['FAM-3']['cost_mid']:.1f}T / ${BILL['FAM-3']['cost_hi']:.1f}T). The rule: when the reserve is below {P['leave_low_years']:.0f} year of next year's benefits the rate steps up {P['leave_step']:.2f} points the next January, to {P['leave_cap']:.2f}%; above {P['leave_high_years']:.1f} years it steps back down; a shortfall at the cap is a Treasury loan repaid with interest.\n")
w(f"**Check:** at {P['leave_rate']:.2f}% the contribution raises ${lm['at_start_w']:.2f}T in 2030-39 (ledger P1: ${REV['P1']['mid']:.2f}T) and ${lm['at_cap_w']:.2f}T at the cap (ledger: ${REV['P1']['hi']:.2f}T).\n")
w("| Take-up case | Mature cost (% of payroll) | First step-up | Rate 2035 / 2039 / 2050 | Receipts 2030-39 | Benefits 2030-39 | Treasury loan owed 2039 / 2050 ($B) |")
w("| --- | --- | --- | --- | --- | --- | --- |")
for c, v in leave.items():
    rr = {x["year"]: x for x in v["rows"]}
    w(f"| {c} | {v['mature_cost']:.2f}% | {v['first_step'] or 'never'} | {rr[2035]['rate']:.2f}% / {rr[2039]['rate']:.2f}% / {rr[2050]['rate']:.2f}% | ${v['receipts_w']:.2f}T | ${v['benefits_w']:.2f}T | {v['loan_2039']:.0f} / {v['loan_2050']:.0f} |")
w("")
hl = leave["high"]
w(f"**Reading.** At low and middle take-up the fund pays its way at or near 0.60%. At high take-up the mature cost ({hl['mature_cost']:.2f}% of payroll) is above the {P['leave_cap']:.2f}% cap, so the loan never stops growing: the bridge is not temporary in that case, and a design choice is needed (a higher cap, a benefit adjustment, or the general-fund backstop FAM-3E). In the window the loan reaches ${hl['loan_2039']:.0f}B (the domain file's about $120B, estimate).")
w("")

w("## Highway Trust Fund (Moving America)\n")
w("From the transportation model (`transportation/moving_america.py`, Draft 2's design): each account's dedicated receipts against its program, the general-fund top-up where receipts fall short, and receipts trapped in an account above its program. $B by fiscal year.\n")
w("| FY | Highway: receipts / program / top-up | Transit: receipts / program / top-up | Rail: receipts / program / top-up | Trapped |")
w("| --- | --- | --- | --- | --- |")
for h in htf:
    if h["fy"] in (2029, 2030, 2031, 2032, 2034, 2036, 2038, 2040, 2042, 2044, 2046):
        w(f"| {h['fy']} | " + " | ".join(f"{h['ded_'+m]:.0f} / {h['prog_'+m]:.0f} / {h['gf_'+m]:.0f}" for m in ("hwy", "tra", "rail")) + f" | {sum(h['trapped_'+m] for m in ('hwy','tra','rail')):.0f} |")
w("")
MAJ = json.load(open("moving-america.json"))
rc = MAJ["renewal_coverage_fy42_46"]
last = htf[-1]
w(f"Where an account's receipts fall short of its program, the gap is a general-fund top-up, counted in the ledger (MOV-29, MOV-30 and the later-Congress MOV-31), so no account runs a deficit; the top-ups shrink to ${sum(last['gf_'+m] for m in ('hwy','tra','rail')):.0f}B in FY{last['fy']}. Programs here include expansion; on renewal alone, FY2042-46 receipts cover {rc['hwy']}% of highway, {rc['tra']}% of transit and {rc['rail']}% of rail renewal (the transportation model). D4 keeps the Highway Trust Fund whole for 75 years; on Draft 2's figures that holds for renewal from the 2040s on, with expansion still drawing on the general fund.\n")

w("## Carbon channel (D7)\n")
w(f"REV-C1 (${REV['C1']['mid']:.2f}T) spread over 2030-39 on the fee's durability path (price times a falling emissions index, the C1 profile in `incidence-phase-in.csv`); REV-C2 (${REV['C2']['mid']:.2f}T) on the same path. {P['carbon_dividend_share']*100:.0f}% of C1 is the dividend (CLI-2), the rest the transition share (to CLI-5). The dividend per person uses a population of {P['pop_2030_m']:.0f} million in 2030 growing {P['pop_growth']*100:.1f}% a year (estimate).\n")
w("| Year | C1 ($B) | Dividend ($B) | Per person ($) | Family of four ($) | Transition ($B) | C2 ($B) |")
w("| --- | --- | --- | --- | --- | --- | --- |")
for c in carbon:
    w(f"| {c['year']} | {c['c1']:.0f} | {c['dividend']:.0f} | {c['per_person']:.0f} | {4*c['per_person']:,.0f} | {c['transition']:.0f} | {c['c2']:.0f} |")
w(f"| 2030-39 ($T) | {sum(c['c1'] for c in carbon)/1000:.2f} | {sum(c['dividend'] for c in carbon)/1000:.2f} | | | {sum(c['transition'] for c in carbon)/1000:.2f} | {sum(c['c2'] for c in carbon)/1000:.2f} |")
w("")

w("## Education fund (EDU-9B, held)\n")
w(f"Not chosen; Espen deferred it to a revenue strategy session on payroll raisers. The fund is modeled as the session designed it: an uncapped payroll contribution (${P['edu_point_2030_bn']:.0f}B a point in 2030, growing {P['edu_base_growth']*100:.0f}% a year), an estate component growing {P['edu_estate_growth']*100:.0f}% a year, and the session's spending path (${EPATH[2030]}B in 2030 to ${EPATH[2049]}B in 2049, ${edu_out_w:.2f}T in 2030-39). Reserves earn the trust-fund rate. The rate needed is the lowest that keeps the reserve at or above zero through 2049 without borrowing.\n")
w("| Estate component | Rate needed (points) | At 1.28: trough / reserve 2049 ($B) | At 1.40: trough / reserve 2049 ($B) |")
w("| --- | --- | --- | --- |")
for k, v in edu_runs.items():
    a, b = v["at128"], v["at140"]
    w(f"| {k} | {v['need']:.2f} | {a['trough'][0]:+.0f} ({a['trough'][1]}) / {a['reserve_2049']:+.0f} | {b['trough'][0]:+.0f} ({b['trough'][1]}) / {b['reserve_2049']:+.0f} |")
w("")
w(f"The domain file estimates about 1.4 points with REV-E1 counted, and slightly above with only its new money (estimate). General-fund relief if taken up: FAM-2, EDU-1, EDU-3 and EDU-4 leave the general fund, ${edu_relief:.2f}T in 2030-39 on the long-term model's rows (domain file: $1.23T), plus the current spending the fund absorbs (about $0.77T, estimate).\n")

open("dedicated-funds.md", "w").write("\n".join(L_))
print(f"Leave mid first step {leave['mid']['first_step']}. SS current law: depletion {cl['depletion']}, balance {cl['balance']:.2f}; D8 {d8['closed']:.0f}% closed; +SS-5 {d5['closed']:.0f}%. HI {hc['depletion']} {hc['balance']:.2f}")
