"""Clean power: the decided set on the general fund, by federal fiscal year, against the booked legacy climate rows.

Role: section 6's arithmetic (`dossiers/clean-power/6-cost.md`). A dossier tool and the booking's source: it reads the budget model's
climate rows as booked before clean power's booking (case `mixed`, frozen from `legacy/sources/recovery-budget-audit.csv` at
main `59e5773` in `booked-before.csv`, so the booking does not feed back into its own basis), reads the carbon model for memo 1 B's
coverage (`coverage_read.py`), and adds the decided changes as working assumptions, each labeled below. Nothing here
changes `models/`. Nominal $ billion, a cost positive, FY y runs from October of y-1.

Run from the repository root (needs node for the carbon model read):
    python3 dossiers/clean-power/tools/clean_power_path.py
"""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
import coverage_read  # noqa: E402

W = list(range(2030, 2040))
Y = W + [2040]

# ---- 1. The booked legacy climate rows (budget model, case `mixed`) -------------------------------------------------
BOOKED = ["CLI-1", "CLI-9", "CLI-3", "CLI-10G", "CLI-5", "CLI-5L", "CLI-5W", "CLI-7", "CLI-7K", "CLI-7C", "CLI-7N",
          "CLI-13A", "CLI-13F", "CLI-2O", "CX", "CXP"]
GROUPS = [("Fee and dividend accounting", ["CLI-2O", "CX", "CXP"]), ("Credits and industry", ["CLI-1", "CLI-9"]),
          ("Standards", ["CLI-3"]), ("Grid", ["CLI-10G"]), ("Bills and add-ons", ["CLI-5", "CLI-5L", "CLI-5W"]),
          ("Adaptation", ["CLI-7", "CLI-7K", "CLI-7C", "CLI-7N"]), ("Farms and forests", ["CLI-13A", "CLI-13F"])]


def booked():
    """The booked legacy climate rows before clean power's booking (case `mixed`, nominal $B, a cost positive)."""
    rows = {}
    with open(os.path.join(HERE, "booked-before.csv")) as f:
        for r in csv.DictReader(f):
            rows[r["line"]] = {y: float(r["y%d" % y]) for y in Y}
    assert set(rows) == set(BOOKED), sorted(set(rows) ^ set(BOOKED))
    return rows


# ---- 2. Memo 1 part 1 B: the price on power plants and large industry --------------------------------------------
# The ledger books REV-C1 at $1.90T over FY2030-39 (ledger-revenue.csv, C1), REV-C2 at $0.03T and REV-C3 at $0.022T; CX is
# JCT's 24.4% offset on all three (DEC-2026-11-12-08), on the carbon model's year shape (fiscal-years.csv). Under B only
# power and industry pay the combustion price: each year's REV-C1 falls by (1 - share_B), share_B read from the carbon model.
#  - CX falls with it (a saving to the general fund).
#  - CLI-5's add-ons lose 20% of the lost receipts as financing through FY2039 (a cost); the booking ends the add-ons with
#    the window, so nothing booked changes from FY2040 on (6-cost.md, part 2, says what that leaves out).
#  - The border adjustment (REV-C2) covers the same goods either way; the methane fee (REV-C3) is unchanged; process
#    emissions stay priced, so the O5 bridge (CLI-2O, CXP) is kept as booked (the booking step reruns its accounts).
C1, C2, C3 = 1.90, 0.03, 0.022
C1_SHARE_OF_CX = C1 / (C1 + C2 + C3)
OFFSET = 0.244


def memo1(rows, share):
    cx, c5 = {}, {}
    for y in Y:
        c1_y = rows["CX"][y] / OFFSET * C1_SHARE_OF_CX          # booked REV-C1 receipts that year
        lost = c1_y * (1 - share[y])                            # receipts no longer charged under B
        cx[y] = -OFFSET * lost
        c5[y] = 0.2 * lost if y <= 2039 else 0.0
    return cx, c5


# ---- 3. Memo 4 part 1 B: the second grid tranche and the builder of last resort -------------------------------------
# Working assumption on the legacy first tranche's ratio (EV-CLP-717: $145B of instruments for about $32B of deficit cost),
# applied to the second tranche's $280B ($40B grants, $200B loans, $40B contracts): about $60B at subsidy cost, released only
# on milestones, so none before FY2033; time-limited capital (D4-B), ending with the window like CLI-10G. Range $0-80B.
GRID2 = {2030: 0, 2031: 0, 2032: 0, 2033: 3, 2034: 6, 2035: 8, 2036: 9, 2037: 10, 2038: 11, 2039: 13, 2040: 0}

# ---- 4. Memo 5 B: the automatic bill credit ---------------------------------------------------------------------------
# Inside the booked add-ons' energy line through FY2039 (EV-CLP-721: $0.12T for LIHEAP, Weatherization and water help;
# the credit's added cost is about $0.08T). From FY2040 the credit is permanent and the add-ons are not: about $8B a year
# above today's LIHEAP in 2030 dollars (EV-CLP-035, EV-CLP-038), grown 2.2% a year: about $9.9B in FY2040.
# Working assumptions (judgment): reach rises in proportion to money (three times the money, three times today's 17%
# reach); 2.2% a year is a price-growth assumption for energy bills, not a sourced figure. Who is matched and the average
# credit are in 6-cost.md, memo 5 B (milestone review O-2).
BILLS = {y: 0.0 for y in W}
BILLS[2040] = round(8.0 * 1.022 ** 10, 1)


# ---- 4b. The clean standard's payments (CLI-3A.02): received by Treasury and paid out through bill protection and the bill
# credit, so they net to zero, except JCT's 24.4% offset on them as a new fee (DEC-2026-11-12-08, part 4), settled by the
# booking: by year from the energy model (models/tools/energy/results.json, provisions CLI-3A.02).
def acp_offset():
    res = json.load(open(os.path.join(ROOT, "models", "tools", "energy", "results.json")))
    by = res["provisions"]["CLI-3A.02"]["by_year"]
    return {y: -OFFSET * float(by[str(y)]) for y in Y}


# ---- 5. Memo 7 B: the transition guarantee, on Espen's parameters ---------------------------------------------------
# Every input is a working assumption (judgment unless an evidence ID is named). 2030 dollars, then 3% a year wage growth.
# Closure timing (re-review on MOD-energy, DEC-2026-11-13-12): on models/tools/energy/ the decided set leaves 31 GW of coal
# in 2030 and none by 2035 (127 and 89 GW under current law), while gas capacity stays open and runs less (591 GW in 2030,
# 699 GW in 2040). So covered closures come early: the same 80,000 workers over FY2030-39 as before, but 14,000 a year in
# 2030-34 (coal plants and mines) and 2,000 a year in 2035-39 (refineries, gas processing, the last mines). Judgment on the
# model's fleet path; the count of workers at plants and mines likely to close is still "Evidence still needed".
PROFILE = {y: (14000 if y <= 2034 else 2000) for y in range(2030, 2041)}

G = dict(
    workers_per_year=8000,      # covered layoffs a year, contractors included: coal plants (172 GW in May 2025, 145 GW scheduled by end-2028 [EV-CLP-508]; ~140 GW left in 2030 closes by 2040,
                                # ~0.18 jobs/MW, +25% contractors), coal mines (part of 44,060 [EV-CLP-500]), refineries and gas plants
    take_up=0.85,               # automatic from payroll records and closure notices; some leave the labor force or move on at once
    share_55=0.25,              # workers 55 and older at layoff (the pension bridge)
    share_db=0.6,               # of them, with a defined-benefit pension
    share_job=0.65,             # of the rest: re-employed within the two years (wage insurance)
    share_train=0.25,           # of the rest: training (the rest draw unemployment benefits only)
    pay=90000,                  # average prior pay, after the cap at twice the median wage
    gap=0.30,                   # new hourly wage 30% below old [EV-CLP-517] [EV-CLP-518]; the top-up fills to 90%: 20% of old
    hours=0.8,                  # hours worked as a share of the old schedule (the top-up counts hours up to the old schedule)
    months_paid=20,             # months of the two years with a job, after a search
    ui=0.35,                    # unemployment benefits as a share of capped prior pay, for 6 months (counted toward the 90%)
    train_months=12,            # months of training paid at 90% (judgment)
    train_cost=20000,           # the retraining account's cap, CLI-11.03 [EV-CLP-529]
    db_waiver=170000,           # Treasury's cost of the plan paying an unreduced pension from layoff (about 7 years early)
    tax_per_year=0.15,          # $B of local property tax lost each year as closures accumulate (plants, mines, refineries)
    refi_subsidy=0.25,          # $B: Treasury's credit cost on ratepayer-backed refinancing bonds over the window
    admin=0.05,                 # administration as a share of payments (state UI agencies as Labor's agents; judgment)
)


def guarantee_per_cohort(workers=None):
    g = G
    n = (workers if workers is not None else g["workers_per_year"]) * g["take_up"]
    top = 0.9 - (1 - g["gap"])                                                      # 0.20 of old hourly pay
    wi = top * g["hours"] * g["months_paid"] / 12 * g["pay"]
    tr = ((0.9 - g["ui"]) * 6 + 0.9 * (g["train_months"] - 6)) / 12 * g["pay"] + g["train_cost"] + top * g["hours"] * g["pay"]
    old = g["share_db"] * g["db_waiver"] + (1 - g["share_db"]) * 2 * (0.9 - g["ui"] / 4) * g["pay"]
    rest = n * (1 - g["share_55"])
    workers = n * g["share_55"] * old + rest * g["share_job"] * wi + rest * g["share_train"] * tr
    return workers * (1 + g["admin"]) / 1e9                                          # $B, 2030 dollars, per year's closures


def memo7():
    out = {}
    for y in Y:
        grow = 1.03 ** (y - 2030)
        # worker payments: each year's closures are paid over about two years: half in the year of closure, half the next
        # (judgment: closures spread through the year), on the closure profile above
        cur, prev = PROFILE[y], PROFILE.get(y - 1, 0)
        workers = (0.5 * guarantee_per_cohort(cur) + 0.5 * guarantee_per_cohort(prev)) * grow
        # places: replacement starts at the full lost tax and falls 10 points a year for ten years, cohort by cohort;
        # local tax grows 2% a year (judgment: assessed values roughly with prices)
        places = sum(G["tax_per_year"] * PROFILE[c] / 8000 * max(0.0, 1 - 0.1 * (y - c)) for c in range(2030, y + 1)) * 1.02 ** (y - 2030)
        refi = G["refi_subsidy"] / 10 if y <= 2039 else 0.0
        out[y] = workers + places + refi
    return out


def m4_compare(rows, share, model):
    """The re-review on MOD-energy (DEC-2026-11-13-12): this tool's booked-basis arithmetic against the energy model's run
    of the decided set (models/tools/energy/results.json, written by its run.py). Reads, never runs, the energy model."""
    f = os.path.join(ROOT, "models/tools/energy/results.json")
    if not os.path.exists(f):
        return None
    R = json.load(open(f))
    dec, pv = R["scenarios"]["decided"], R["provisions"]
    w, f40 = dec["window_2030_39"], dec["fy2040"]
    c1 = {y: rows["CX"][y] / OFFSET * C1_SHARE_OF_CX * share[y] for y in Y}
    s = lambda d: sum(d[y] for y in W)
    out = dict(
        c1=(s(c1), c1[2040], w["c1"], f40["c1"]),
        transition=(0.2 * s(c1), 0.2 * c1[2040], w["transition"], f40["transition"]),
        offset_on_c1_c2_c3=((s(c1) + 30.0 + 22.0) * OFFSET, None, (w["c1"] + w["c2"] + w["c3"]) * OFFSET, None),
        standard_payments=(None, None, -pv["CLI-3A.02"]["fy2030_39"], -pv["CLI-3A.02"]["fy2040"]),
        dividend_per_adult=(model[2035]["dividend_adult_B"], None, dec["per_adult"]["2035"], None),
    )
    print("\nRe-review on MOD-energy (this tool | the energy model; FY2030-39, FY2040; nominal $B):")
    for k, v in out.items():
        fmt = lambda x: "    —" if x is None else f"{x:8.1f}"
        print(f"  {k:22s}" + " ".join(fmt(x) for x in v))
    return out


# ---- 6. Assemble --------------------------------------------------------------------------------------------------
def plan_gap_fy2040():
    """The plan-wide FY2040 general-fund primary gap ($B short) and GDP, case `mixed`, read from the budget model's paths
    file at the current head (not hard-coded: milestone review F-1)."""
    with open(os.path.join(ROOT, "models/data/recovery-budget-paths.csv")) as f:
        for r in csv.DictReader(f):
            if r["case"] == "mixed" and r["year"] == "2040":
                return float(r["agenda_gf_primary_bn"]), float(r["gdp_bn"])
    raise SystemExit("recovery-budget-paths.csv has no mixed FY2040 row")


PLAN_GAP_FY2040, GDP_FY2040 = plan_gap_fy2040()


def compute():
    """The decided set's changes against the booked rows, by fiscal year (the booking reads this)."""
    rows = booked()
    model = coverage_read.run()
    share = {y: model[y]["share_B"] for y in Y}
    cx, c5 = memo1(rows, share)
    g7 = memo7()
    ts = {y: (0.2 * rows["CX"][y] / OFFSET * C1_SHARE_OF_CX * share[y] if y >= 2040 else 0.0) for y in Y}
    held = {y: (-ts[y] if ts[y] else 0.0) for y in Y}
    acp = acp_offset()
    chg = {y: cx[y] + c5[y] + GRID2[y] + BILLS[y] + g7[y] + held[y] for y in Y}   # section 6's decided changes
    chg_all = {y: chg[y] + acp[y] for y in Y}                                     # and the payments' offset
    c1 = {y: rows["CX"][y] / OFFSET * C1_SHARE_OF_CX * share[y] for y in Y}   # REV-C1 under B, booked basis
    return dict(rows=rows, model=model, share=share, cx=cx, c5=c5, grid2=GRID2, bills=BILLS, g7=g7, ts=ts,
                held=held, acp=acp, change=chg, change_all=chg_all, c1=c1)


def main():
    P = compute()
    rows, model, share, cx, c5, g7 = P["rows"], P["model"], P["share"], P["cx"], P["c5"], P["g7"]
    s = lambda d: sum(d[y] for y in W)
    fmt = lambda d: " ".join(f"{d[y]:7.1f}" for y in Y) + f" | {s(d):8.1f} {d[2040]:7.1f}"
    print("FY                          " + " ".join(f"{y:>7}" for y in Y) + " |  2030-39    2040")
    tot_b = {y: sum(rows[r][y] for r in BOOKED) for y in Y}
    for name, rs in GROUPS:
        print(f"{name:28s}" + fmt({y: sum(rows[r][y] for r in rs) for y in Y}))
    print(f"{'BOOKED TOTAL':28s}" + fmt(tot_b))
    print(f"{'memo 1 B: CX offset':28s}" + fmt(cx))
    print(f"{'memo 1 B: add-ons financing':28s}" + fmt(c5))
    print(f"{'memo 4 B: tranche 2 + builder':28s}" + fmt(GRID2))
    print(f"{'memo 5 B: bill credit':28s}" + fmt(BILLS))
    print(f"{'memo 7 B: guarantee':28s}" + fmt(g7))
    # DEC-2026-11-13-13 (option A): from FY2040 the ledger's CLI-2 outlay is the dividend (80% of C1)
    # plus the waterfall's draws, which are the memo 5 B and 7 B rows above; the rest of the 20%
    # transition share stays in the general fund. Through FY2039 the share finances the add-ons.
    ts, held, chg = P["ts"], P["held"], P["change"]
    print(f"{'DEC-13-13 A: share to GF':28s}" + fmt(held))
    print(f"{'CLI-3A.02: offset on paymts':28s}" + fmt(P["acp"]))
    chg = P["change_all"]
    tot = {y: tot_b[y] + chg[y] for y in Y}
    print(f"{'CHANGE vs booked':28s}" + fmt(chg))
    print(f"{'DECIDED SET':28s}" + fmt(tot))
    print(f"\nshare_B by year: " + " ".join(f"{y}:{share[y]:.3f}" for y in Y))
    print(f"memo 7 B per 8,000 closures (2030 dollars): ${guarantee_per_cohort():.2f}B")
    print(f"FY2040: decided set ${tot[2040]:.1f}B = {100 * tot[2040] / GDP_FY2040:.2f}% of GDP; "
          f"{100 * tot[2040] / PLAN_GAP_FY2040:.1f}% of the plan-wide gap (${PLAN_GAP_FY2040:.1f}B); change {chg[2040]:+.1f}B "
          f"= {100 * chg[2040] / PLAN_GAP_FY2040:+.2f}% of the gap")
    print(f"Transition share in FY2040 under B (20% of the receipts still raised): ${ts[2040]:.1f}B; "
          f"waterfall {BILLS[2040] + g7[2040]:.1f}B; remainder {ts[2040] - BILLS[2040] - g7[2040]:.1f}B")
    d35 = model[2035]
    print(f"Dividend per adult 2035 (nominal): package ${d35['dividend_adult_package']:.0f}, B ${d35['dividend_adult_B']:.0f}")
    m4_compare(rows, share, model)
    return dict(rows=rows, cx=cx, c5=c5, grid2=GRID2, bills=BILLS, g7=g7, held=held, change=chg, total=tot, share=share)


if __name__ == "__main__":
    main()
