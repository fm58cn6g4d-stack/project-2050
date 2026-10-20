#!/usr/bin/env python3
"""fiscal-model.py: the Project 2050 long-term fiscal model.

Three layers, each usable alone:
  1. Baseline (all of government): index/data/fiscal-baseline.csv (from fiscal-data.py):
     CBO history FY1962-2025, FY2026 actuals, CBO's Feb 2026 baseline to 2036 and its
     long-term projection to 2056, plus post-February adjustments (tariff ruling).
  2. Program (the agenda, as increments over that baseline): every ledger row from
     ledger.json, spread across years with the profiles in fiscal-profiles.py and calibrated
     so each row's FY2030-39 sum equals its ledger midpoint.
  3. Debt dynamics: interest on the program's own borrowing at CBO's projected rates, total
     debt held by the public, net interest, deficits, the fiscal gap, and the D4 tests.

Run after ledger-build.py. Writes fiscal-model.json and fiscal-paths.csv next to it.
All amounts are billions of nominal dollars by fiscal year unless a column says % of GDP.
"""
import csv, json, os, importlib.util, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("profiles", os.path.join(HERE, "fiscal-profiles.py"))
PR = importlib.util.module_from_spec(spec); spec.loader.exec_module(PR)

Y0, Y1 = 2026, 2056          # model years
W0, W1 = 2030, 2039          # ledger window
CPI = {y: 2.26 if y <= 2036 else 2.3 for y in range(2026, 2057)}   # CBO Feb 2026 CPI-U path (rounded)

PBS = ["C18", "C35", "C19b", "C20", "C38"]
DEC = PBS + ["C39", "C40", "C41"]              # decided in Decision Brief 2 (Oct 20): TS12, HP1, HP3; no trims
TRIMS = ["C5", "C17", "C33", "C34", "C36"]    # declined in Decision Brief 2; kept for reference
SCENARIOS = [
    # id, label, cut options included, extra settings
    ("BASE", "Current-law baseline (CBO Feb 2026, adjusted)", None, {}),
    ("GROSS", "Program spending with the top-end base only (no new options)", [], {}),
    ("PB", "Package B (C18, C35, C19b, C20)", ["C18", "C35", "C19b", "C20"], {}),
    ("PB+S", "Package B + sprint package (C38)", PBS, {}),
    ("DEC", "Decided (Decision Brief 2): Package B + sprint + TS12, HP1, HP3 (C39-C41); no trims", DEC, {}),
    ("DEC+ENV", "Decided, plus new time-limited investments filling the D4-B envelope room left after the borrowing readings and CAP-7S", DEC, {"envelope": 0.5, "net_of_borrow": True}),
    ("DEC-DYN", "Decided, with CBO-style dynamic feedback (about -$0.56T)", DEC, {"dynamic": "mid"}),
    ("DEC-R1", "Decided, with interest rates 1 point higher on all debt from 2030", DEC, {"rate_shift": 1.0}),
    ("BASE-R1", "Baseline with interest rates 1 point higher from 2030", None, {"rate_shift": 1.0}),
    ("DEC+TRIMS", "Decided plus the five trims declined in Decision Brief 2 (reference only)", DEC + TRIMS, {}),
]


def read_baseline(path):
    B = {}
    with open(path) as f:
        for r in csv.DictReader(f):
            y = int(r["year"])
            B[y] = {k: (float(v) if v not in ("", None) and k != "source" else v) for k, v in r.items()}
    return B


def growth_index(B, key):
    if key == "gdp":
        return {y: B[y]["gdp"] for y in B if y >= Y0}
    if key == "cpi":
        idx, v = {}, 100.0
        for y in range(Y0, Y1 + 1):
            if y > Y0: v *= 1 + CPI[y] / 100
            idx[y] = v
        return idx
    if key in ("special_ss",):
        return {y: B[y]["rev_payroll"] for y in B if y >= Y0}
    return {y: B[y][key] for y in B if y >= Y0}


def row_path(B, mid10, prof, rid=None):
    """Annual path (billions) whose FY2030-39 sum equals mid10 (trillions)."""
    if rid in PR.YEARS:
        vals = PR.YEARS[rid]; s = sum(vals)
        out = {y: 0.0 for y in range(Y0, Y1 + 1)}
        for i, y in enumerate(range(W0, W1 + 1)): out[y] = vals[i] * (mid10 * 1000 / s if s else 0)
        g = growth_index(B, prof.get("grow", "gdp"))
        for y in range(W1 + 1, Y1 + 1): out[y] = out[W1] * prof.get("perm", 1.0) * g[y] / g[W1]
        return out
    start, ramp = prof.get("start", W0), prof.get("ramp", 1)
    end, perm, fade = prof.get("end"), prof.get("perm", 1.0), prof.get("fade", 0.0)
    g = growth_index(B, prof.get("grow", "gdp"))
    raw = {}
    for y in range(Y0, Y1 + 1):
        ph = 0.0 if y < start else min(1.0, (y - start + 1) / ramp)
        if end and y > end: ph = 0.0
        raw[y] = ph * g[y] / g[W0]
    s = sum(raw[y] for y in range(W0, W1 + 1))
    scale = (mid10 * 1000 / s) if s else 0.0
    out = {}
    for y in range(Y0, Y1 + 1):
        if y < W0:
            out[y] = 0.0
        elif y <= W1:
            out[y] = raw[y] * scale
        else:
            if prof.get("grow") == "special_ss":
                gg = growth_index(B, "gdp")
                out[y] = out[W1] * gg[y] / gg[W1] * (1 - 0.015) ** (y - W1)
            else:
                out[y] = perm * scale * (g[y] / g[W0]) * (1 - fade) ** (y - W1)
    return out


def marginal_rate(B, y, shift=0.0):
    """Rate on the program's incremental debt: the higher of CBO's average rate on debt and a
    40/60 bill/10-year-note blend through 2036 (new borrowing is at market rates), then the
    long-term baseline's implied average rate."""
    r = B[y]
    if y <= 2036:
        blend = 0.4 * r["bill3m"] + 0.6 * r["note10"]
        base = max(r["cbo_avg_rate"], blend)
    else:
        base = r["implied_rate"]
    return (base + (shift if y >= W0 else 0.0)) / 100


def debt_roll(B, primary, shift=0.0, start_balance=0.0, start_year=Y0):
    """Accumulate an increment to debt with interest (half a year of interest on the current
    year's flow). Returns (interest, balance) dicts."""
    D, I, prev = {}, {}, start_balance
    for y in range(start_year, Y1 + 1):
        r = marginal_rate(B, y, shift)
        I[y] = r * prev + r * primary.get(y, 0.0) / 2
        prev = prev + primary.get(y, 0.0) + I[y]
        D[y] = prev
    return I, D


def build(ledger_path, baseline_path):
    L = json.load(open(ledger_path))
    B = read_baseline(baseline_path)
    bills = {b["id"]: b for b in L["bills"]}
    rev = {r["id"]: r for r in L["revenue"]}
    cuts = {c["id"]: c for c in L["cuts"]}
    checks = []

    # ---- program rows ----
    rows = []  # each: id, label, group, cat, gf path, unified path
    for bid, b in bills.items():
        prof = PR.BILLS.get(bid)
        if prof is None:
            checks.append(f"MISSING PROFILE for bill {bid}; defaulted to ramp 1, GDP growth")
            prof = dict(cat="out_other_mandatory", ramp=1, grow="gdp")
        gf = b["gf_mid"]
        uni = b["net_mid"] if bid == "SS-1" else (0.0 if prof.get("unified_zero") else gf)
        rows.append(dict(id=bid, label=b["bill"], group="spending", cat=prof["cat"],
                         gf=row_path(B, gf, prof, bid), uni=row_path(B, uni, prof, bid), basis=prof.get("basis", "")))
    for rid, r in rev.items():
        if r["in_base"] != "Yes" or r["channel"] != "General fund":
            continue
        prof = PR.REVENUE.get(rid)
        if prof is None:
            checks.append(f"MISSING PROFILE for base revenue {rid}"); prof = dict(cat="rev_individual", ramp=1, grow="rev_individual")
        p = row_path(B, -r["mid"], prof, rid)
        rows.append(dict(id=rid, label=r["option"], group="base revenue", cat=prof["cat"], gf=p, uni=p, basis=prof.get("basis", "")))
    opt_rows = {}
    for cid, c in cuts.items():
        prof = PR.CUTS.get(cid)
        if prof is None:
            checks.append(f"MISSING PROFILE for option {cid}"); continue
        if prof["kind"] == "borrow":
            continue
        p = row_path(B, -c["saves_tn"], prof, cid)
        opt_rows[cid] = dict(id=cid, label=c["change"], group=prof["kind"], cat=prof["cat"], gf=p, uni=p, basis=prof.get("basis", ""))
    # borrowing the D4-B envelope already holds (accepted borrow lines: C21, C30-C32, C37, C42)
    borrow_used = sum(c["saves_tn"] for c in L["cuts"] if c["kind"].startswith("Borrow (accepted"))
    # dynamic sensitivity (not in any ledger total)
    dyn_mid = -sum(d["mid"] for d in L["dynamic"])       # + raises the deficit
    dyn = row_path(B, dyn_mid, dict(cat="rev_individual", start=W0, ramp=10, grow="gdp"))

    # calibration check against the ledger
    s = lambda p: sum(p[y] for y in range(W0, W1 + 1)) / 1000
    gf_claims = sum(s(r["gf"]) for r in rows if r["group"] == "spending")
    base_rev = -sum(s(r["gf"]) for r in rows if r["group"] == "base revenue")
    later = sum(b["gf_mid"] for b in L["bills"] if b["rail"] in ("LATER", "T2"))
    checks.append(f"Calibration: program claims {gf_claims:.3f}T = ledger {L['summary']['gf_claims']['mid']}T + {later:.3f}T of later-Congress rows the ledger leaves out of first-Congress claims (MOV-31, DEM-3), which the long-term model includes; base revenue {base_rev:.2f}T (ledger {L['summary']['base_revenue']['mid']}T)")

    # ---- baseline (adjusted) ----
    cbo_debt_2026 = 32095.165  # CBO Feb 2026 end-FY2026 projection
    adj_primary = {y: B[y]["adj_deficit"] for y in range(Y0, Y1 + 1)}
    E_I, E_D = debt_roll(B, adj_primary, 0.0, start_balance=B[2026]["debt_public"] - cbo_debt_2026, start_year=2027)

    def baseline(shift=0.0):
        """Adjusted current-law path. A rate shift (percentage points, from 2030) raises the
        rate on all debt and the extra interest compounds."""
        out, sD = {}, 0.0
        for y in range(Y0, Y1 + 1):
            b = B[y]
            if y == Y0:
                out[y] = dict(gdp=b["gdp"], rev=b["rev_total"], prim_out=b["out_primary"], interest=b["out_net_interest"], debt=b["debt_public"])
                continue
            s_ = shift / 100 if y >= W0 else 0.0
            prev_core = B[y - 1]["debt_public"] + (E_D.get(y - 1, B[2026]["debt_public"] - cbo_debt_2026) if y - 1 >= 2026 else 0.0)
            sI = s_ * prev_core + (marginal_rate(B, y) + s_) * sD
            sD = sD + sI
            out[y] = dict(gdp=b["gdp"], rev=b["rev_total"] - adj_primary[y], prim_out=b["out_primary"],
                          interest=b["out_net_interest"] + E_I.get(y, 0.0) + sI,
                          debt=b["debt_public"] + E_D.get(y, 0.0) + sD)
        for y in out:
            o = out[y]; o["deficit"] = o["prim_out"] + o["interest"] - o["rev"]; o["primary_deficit"] = o["prim_out"] - o["rev"]
        return out

    # ---- scenarios ----
    results = {}
    for sid, label, opts, cfg in SCENARIOS:
        shift = cfg.get("rate_shift", 0.0)
        base = baseline(shift)
        res = dict(id=sid, label=label, options=opts, years={})
        if opts is None:
            prog_uni = {y: 0.0 for y in range(Y0, Y1 + 1)}; prog_gf = dict(prog_uni)
        else:
            use = rows + [opt_rows[o] for o in opts if o in opt_rows]
            prog_uni = {y: sum(r["uni"][y] for r in use) for y in range(Y0, Y1 + 1)}
            prog_gf = {y: sum(r["gf"][y] for r in use) for y in range(Y0, Y1 + 1)}
            if cfg.get("dynamic"):
                for y in prog_uni: prog_uni[y] += dyn[y]; prog_gf[y] += dyn[y]
            if cfg.get("envelope"):
                env = {y: cfg["envelope"] / 100 * (1.0 if y <= 2034 else max(0.0, (2040 - y) / 6)) * B[y]["gdp"] for y in range(W0, 2041)}
                scale = 1.0
                if cfg.get("net_of_borrow"):  # fill only the room the ledger's borrowing lines leave
                    tot = sum(env[y] for y in range(W0, W1 + 1)) / 1000
                    scale = max(0.0, (tot - borrow_used) / tot)
                for y, v in env.items():
                    prog_uni[y] += v * scale; prog_gf[y] += v * scale
        PI, PD = debt_roll(B, prog_uni, shift)
        GI, GD = debt_roll(B, prog_gf, shift)
        for y in range(Y0, Y1 + 1):
            b = base[y]; g = b["gdp"]
            tot_def = b["deficit"] + prog_uni[y] + PI[y]
            tot_debt = b["debt"] + PD[y]
            res["years"][y] = dict(
                gdp=g, base_deficit=b["deficit"], base_debt=b["debt"], base_interest=b["interest"],
                prog_primary=prog_uni[y], prog_interest=PI[y], prog_debt=PD[y],
                gf_primary=prog_gf[y], gf_interest=GI[y], gf_debt=GD[y],
                deficit=tot_def, debt=tot_debt, interest=b["interest"] + PI[y],
                rev=b["rev"], out=b["prim_out"] + b["interest"] + prog_uni[y] + PI[y],
                deficit_pct=100 * tot_def / g, debt_pct=100 * tot_debt / g,
                interest_pct=100 * (b["interest"] + PI[y]) / g,
                base_debt_pct=100 * b["debt"] / g, prog_debt_pct=100 * PD[y] / g,
                gf_debt_pct=100 * GD[y] / g, prog_primary_pct=100 * prog_uni[y] / g,
                gf_primary_pct=100 * prog_gf[y] / g)
        results[sid] = res

    # ---- fiscal gap: constant primary improvement from 2030 that brings 2056 debt/GDP to a target ----
    def fiscal_gap(res, target_pct, shift=0.0):
        unit = {y: 0.01 * res["years"][y]["gdp"] for y in range(W0, Y1 + 1)}
        _, UD = debt_roll(B, unit, shift)
        eff = UD[Y1]
        need = res["years"][Y1]["debt"] - target_pct / 100 * res["years"][Y1]["gdp"]
        return need / eff
    for sid, label, opts, cfg in SCENARIOS:
        r = results[sid]; sh = cfg.get("rate_shift", 0.0)
        r["fiscal_gap_hold_2029"] = fiscal_gap(r, r["years"][2029]["debt_pct"], sh)
        r["fiscal_gap_100"] = fiscal_gap(r, 100.0, sh)

    # ---- D4 tests (D4-B as decided in Decision Brief 2, Oct 20) ----
    env10 = sum(0.005 * (1.0 if y <= 2034 else max(0.0, (2040 - y) / 6)) * B[y]["gdp"] for y in range(W0, W1 + 1)) / 1000
    def tests(r):
        Yd = r["years"]
        win = lambda k: sum(Yd[y][k] for y in range(W0, W1 + 1))
        t = {}
        t["gf_10yr_primary"] = win("gf_primary") / 1000
        t["unified_10yr_primary"] = win("prog_primary") / 1000
        t["unified_10yr_with_interest"] = (win("prog_primary") + win("prog_interest")) / 1000
        # 1. permanent programs paid for at maturity: GF balance in FY2040 and every later year at or below zero
        t["gf_2039_pct"] = Yd[2039]["gf_primary_pct"]; t["gf_2040_pct"] = Yd[2040]["gf_primary_pct"]
        t["gf_2045_pct"] = Yd[2045]["gf_primary_pct"]
        t["gf_worst_2040_56_pct"] = max(Yd[y]["gf_primary_pct"] for y in range(2040, Y1 + 1))
        t["maturity_pass"] = t["gf_worst_2040_56_pct"] <= 1e-9
        # 2. investment envelope: 0.5% of GDP to 2034, tapering to zero by 2040; holds the accepted borrowing lines
        t["envelope_10yr"] = env10; t["envelope_used"] = borrow_used; t["envelope_room"] = env10 - borrow_used
        # 3. guardrails against the real (CBO, adjusted) baseline
        t["below_baseline_every_year"] = all(Yd[y]["prog_debt"] <= 1e-9 for y in range(W0, Y1 + 1))
        t["margin_pts"] = {y: Yd[y]["base_debt_pct"] - Yd[y]["debt_pct"] for y in (2035, 2045, 2056)}
        t["margin_widening"] = t["margin_pts"][2045] > t["margin_pts"][2035] and t["margin_pts"][2056] > t["margin_pts"][2045]
        t["interest_pct"] = {y: Yd[y]["interest_pct"] for y in (2035, 2045, 2056)}
        t["base_interest_pct"] = {y: 100 * Yd[y]["base_interest"] / Yd[y]["gdp"] for y in (2035, 2045, 2056)}
        t["interest_below_baseline"] = all(t["interest_pct"][y] <= t["base_interest_pct"][y] + 1e-9 for y in (2035, 2045, 2056))
        # information only (not guardrails under the decided rule)
        t["prog_debt_pct"] = {y: Yd[y]["prog_debt_pct"] for y in (2034, 2039, 2045, 2050, 2056)}
        t["gf_debt_pct"] = {y: Yd[y]["gf_debt_pct"] for y in (2034, 2039, 2045, 2050, 2056)}
        pk2 = max(range(W0, Y1 + 1), key=lambda y: Yd[y]["debt_pct"])
        t["total_debt_peak_year"] = pk2
        return t
    for r in results.values():
        if r["options"] is not None: r["tests"] = tests(r)

    # ---- composition (all of government, % of GDP) for the planning picture ----
    def comp(sid, y):
        use = rows + ([opt_rows[o] for o in results[sid]["options"] if o in opt_rows] if results[sid]["options"] else [])
        cats = ["rev_individual", "rev_payroll", "rev_corporate", "rev_customs", "rev_other",
                "out_social_security", "out_medicare_net", "out_health_other", "out_other_mandatory",
                "out_disc_defense", "out_disc_nondefense"]
        g = B[y]["gdp"]; c = {}
        for k in cats:
            base_v = B[y][k]
            add = sum(r["uni"][y] for r in use if r["cat"] == k) if results[sid]["options"] is not None else 0.0
            # revenue rows carry negative signs (deficit convention): flip for revenue categories
            v = base_v - add if k.startswith("rev_") else base_v + add
            c[k] = 100 * v / g
        return c
    composition = {sid: {y: comp(sid, y) for y in (2026, 2034, 2039, 2045, 2056)} for sid in ("BASE", "DEC")}

    return dict(results=results, rows=rows, opt_rows=opt_rows, dyn=dyn, checks=checks, composition=composition, B=B, ledger_summary=L["summary"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=os.path.join(HERE, "ledger.json"))
    ap.add_argument("--baseline", default=os.path.join(HERE, "..", "data", "fiscal-baseline.csv"))
    a = ap.parse_args()
    M = build(a.ledger, a.baseline)
    out = {k: v for k, v in M.items() if k not in ("B",)}
    for r in out["rows"] + list(out["opt_rows"].values()):
        r["gf"] = {y: round(v, 3) for y, v in r["gf"].items()}; r["uni"] = {y: round(v, 3) for y, v in r["uni"].items()}
    json.dump(out, open(os.path.join(HERE, "fiscal-model.json"), "w"), indent=1, default=float)
    with open(os.path.join(HERE, "fiscal-paths.csv"), "w", newline="") as f:
        w = csv.writer(f)
        cols = ["gdp", "base_deficit", "base_debt", "prog_primary", "prog_interest", "prog_debt", "gf_primary", "gf_debt",
                "deficit", "debt", "interest", "deficit_pct", "debt_pct", "interest_pct", "base_debt_pct", "prog_debt_pct", "gf_debt_pct"]
        w.writerow(["scenario", "year"] + cols)
        for sid, r in M["results"].items():
            for y, v in r["years"].items():
                w.writerow([sid, y] + [round(v[c], 3) for c in cols])
    for c in M["checks"]: print(c)
    for sid, r in M["results"].items():
        Yd = r["years"]
        print(f"{sid:8s} debt% 2029 {Yd[2029]['debt_pct']:.1f} 2034 {Yd[2034]['debt_pct']:.1f} 2039 {Yd[2039]['debt_pct']:.1f} 2045 {Yd[2045]['debt_pct']:.1f} 2056 {Yd[2056]['debt_pct']:.1f} | prog debt% 2039 {Yd[2039]['prog_debt_pct']:.2f} 2056 {Yd[2056]['prog_debt_pct']:.2f} | gap(hold) {r['fiscal_gap_hold_2029']:.2f}")


if __name__ == "__main__":
    main()
