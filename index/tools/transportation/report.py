#!/usr/bin/env python3
"""Prints every figure Draft 2 carries, in the same layout as legacy/final_v3.py (the test compares the two).
Run from anywhere:  python3 index/tools/transportation/report.py   (add --json PATH to write ledger figures)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import moving_america as MA
from moving_america import Model, Design, PERIODS, G1112, RESERVE, gdp, need, legacy, ev_fee, EXCISE_OFFSET

def main(out=print):
    m = Model(); d = m.d; B = d.scenario
    yrs = range(2032, 2037); cap = MA.CAP_ALL_IN
    rows = m.period_rows(B)
    out("PERIODS")
    for r in rows:
        a, b = PERIODS[r["period"]]; ys = range(a, b + 1)
        p1112 = max((m.allocate(t)["gf_total"] + G1112[t]) / gdp(t) for t in ys)
        cov = "/".join(f"{r['ded'][k] / r['prog'][k]:.0%}" for k in r["ded"])
        prog = "/".join(f"{v:.2f}" for v in r["prog"].values()); ded = "/".join(f"{v:.2f}" for v in r["ded"].values())
        gf = "/".join(f"{v:.2f}" for v in r["gf"].values())
        out(f" {r['period']}: {r['gf_pct_avg']:.3%}/{r['gf_pct_peak']:.3%}({r['peak_year']}) +1112 {p1112:.3%} "
            f"cbo {max(m.cbo_basis(t) for t in ys):.3%} cov {cov} | prog {prog} ded {ded} gf {gf} trapped {r['trapped']:.1f}")
    for a, b in ((2032, 2036), (2037, 2041), (2042, 2046)):
        out(" rencov " + str(a) + " " + "/".join(f"{v:.0%}" for v in m.renewal_coverage(a, b).values()))
    out(f" self-suff {m.self_sufficient()}")
    out(f" $/yr 32-36 {round(sum(rows[2]['gf'].values()) / 5, 1)} 42-46 {round(sum(rows[4]['gf'].values()) / 5, 1)} "
        f"ded/yr42-46 {round(sum(rows[4]['ded'].values()) / 5, 1)}")
    out("BY YEAR")
    for t in range(2029, 2037):
        a = m.allocate(t); room = cap * gdp(t) - a["gf_total"]
        out(f" {t}: prog {'/'.join(f'{v:.2f}' for v in a['prog'].values())} draw {a['gf_pct']:.3%} room {room:.2f} "
            f"-1112 {room - G1112[t]:.2f} -res {room - G1112[t] - RESERVE.get(t, 0):.2f} "
            f"allin {(a['gf_total'] + G1112[t] + RESERVE.get(t, 0)) / gdp(t):.3%}")
    out("TOPUPS")
    tu = m.topups(); T = [0, 0, 0, 0]; TU = {}
    for t in yrs:
        x = tu[t]; TU[t] = (round(x["hwy"], 2), round(x["tra"], 2), round(x["rail"], 2))
        T = [T[0] + x["hwy"], T[1] + x["tra"], T[2] + x["rail"], T[3] + x["exp"]]
        out(f" {t}: {x['hwy']:.2f} / {x['tra']:.2f} / {x['rail']:.2f}  exp {x['exp']:.2f}")
    out(f" totals {[round(x, 2) for x in T]} GF {round(sum(T), 2)}")
    act29 = sum(sum(TU[t]) for t in (2032, 2033, 2034)) + TU[2035][0] + TU[2035][1]; act30 = TU[2035][2] + sum(TU[2036])
    out(f" 2029 act top-ups {act29:.2f}  2030 act {act30:.2f}")
    out("REVENUE BY SOURCE (clean-car column + totals)")
    for t in range(2029, 2037):
        c = MA.components(t, d); out(f" {t}: cleancar {c['cp']:.2f} total {c['total']:.1f}")
    for a, b in ((2032, 2036), (2037, 2041), (2042, 2046)):
        ys = range(a, b + 1); cp = sum(m.P0.cp(t) for t in ys); tot = sum(MA.components(t, d)["total"] for t in ys)
        pr = sum(m.P1(t) - m.P0(t) for t in ys)
        out(f" FY{a}-{b}: cleancar {cp:.1f} total ex prem {tot:.1f} prem {pr:.1f} total {tot + pr:.1f}")
    out(f" check ded FY32-36 {round(sum(sum(m.allocate(t)['ded'].values()) for t in yrs), 2)}")
    s29 = MA.score_2029(m)
    out(f" 2029 act clean-car score {s29['clean_car']:.1f}; gross {s29['gross']:.1f} net {s29['net']:.1f}")
    out("SENS")
    for lab, kw in MA.SENSITIVITIES.items():
        dd = Design(**kw); mm = Model(dd); sc = dd.scenario
        rr = mm.period_rows(sc); cov = mm.renewal_coverage(2042, 2046, sc).values()
        out(f" {lab}: {rr[2]['gf_pct_avg']:.3%}/{rr[2]['gf_pct_peak']:.3%} allin {mm.all_in_peak(sc):.3%} "
            f"42-46 {rr[4]['gf_pct_avg']:.3%} cov {'/'.join(f'{c:.0%}' for c in cov)} GF {sum(rr[2]['gf'].values()):.1f}")
    gdp5 = sum(gdp(t) for t in yrs); GF = sum(rows[2]["gf"].values())
    for lab, cut in MA.FALLBACK_CUTS.items(): out(f" fallback {lab} {(GF - cut) / gdp5:.3%}")
    # A-7, on the governing design. (The old final_v3.py solved this on its last sensitivity's revenue path and
    # printed 50.5/37.6/12.0; restated Oct 20, 2026.)
    out(f" share solve {governing_share_solve()}")
    P1 = m.P1
    for t in (2031, 2036, 2046):
        out(f" rates {t} clean c/mi {round(P1.rg(t) / 40, 2)} EV$ {round(P1.rg(t) / 40 * 120)} hybrid40$ {round(P1.gr(t) * 3)} "
            f"gas25$ {round(P1.gr(t) * 4.8)} PHEV40%$ {round(P1.gr(t) * 1.8 + 0.3 * P1.rg(t) / 40 * 120)}")
    return m

def governing_share_solve():
    return {k: round(v * 100, 1) for k, v in Model().solve_shares()[0].items()}

def figures():
    """The figures Draft 2 and the ledger carry, as one dictionary."""
    m = Model(); rows = m.period_rows(); tu = m.topups()
    lr = MA.ledger_rows(m)
    p = {r["period"]: r for r in rows}
    return dict(
        program_fy32_36=round(sum(p["FY2032-36"]["prog"].values()), 2),
        dedicated_fy32_36=round(sum(p["FY2032-36"]["ded"].values()), 2),
        general_fund_fy32_36=round(sum(p["FY2032-36"]["gf"].values()), 2),
        expansion_fy32_36=round(sum(x["exp"] for x in tu.values()), 2),
        topups_fy32_36=round(sum(x["hwy"] + x["tra"] + x["rail"] for x in tu.values()), 2),
        draw_avg_fy32_36=round(p["FY2032-36"]["gf_pct_avg"] * 100, 3), draw_peak_fy32_36=round(p["FY2032-36"]["gf_pct_peak"] * 100, 3),
        draw_all_in_peak=round(m.all_in_peak() * 100, 3), draw_avg_fy42_46=round(p["FY2042-46"]["gf_pct_avg"] * 100, 3),
        renewal_coverage_fy42_46={k: round(v * 100) for k, v in m.renewal_coverage(2042, 2046).items()},
        ledger=lr,   # full precision; ledger-build.py rounds to the precision Draft 2 prints
        share_solve_governing=governing_share_solve(),
    )

if __name__ == "__main__":
    if "--json" in sys.argv:
        path = sys.argv[sys.argv.index("--json") + 1]
        json.dump(figures(), open(path, "w"), indent=1)
        print("wrote", path)
    else:
        main()
