"""Clean power: the decided set on the general fund, by federal fiscal year, against the booked legacy climate rows.

Role: section 6's arithmetic (`dossiers/clean-power/6-cost.md`). A dossier tool, not a booking: it reads the budget model's
booked climate rows (case `mixed`) from `legacy/sources/recovery-budget-audit.csv`, reads the carbon model for memo 1 B's
coverage (`coverage_read.py`), and adds the decided changes as working assumptions, each labeled below. Nothing here
changes `models/`. Nominal $ billion, a cost positive, FY y runs from October of y-1.

Run from the repository root (needs node for the carbon model read):
    python3 dossiers/clean-power/tools/clean_power_path.py
"""
import csv, os, sys

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
    rows = {r: {y: 0.0 for y in Y} for r in BOOKED}
    with open(os.path.join(ROOT, "legacy/sources/recovery-budget-audit.csv")) as f:
        for r in csv.DictReader(f):
            if r["case"] == "mixed" and r["line"] in rows and int(r["year"]) in Y:
                rows[r["line"]][int(r["year"])] = float(r["primary_deficit_change_bn"])
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
# above today's LIHEAP in 2030 dollars (EV-CLP-035, EV-CLP-038), grown 2.2% a year: about $9.7B in FY2040.
BILLS = {y: 0.0 for y in W}
BILLS[2040] = round(8.0 * 1.022 ** 10, 1)


# ---- 5. Memo 7 B: the transition guarantee, on Espen's parameters ---------------------------------------------------
# Every input is a working assumption (judgment unless an evidence ID is named). 2030 dollars, then 3% a year wage growth.
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
    train_months=12, train_cost=20000,
    db_waiver=170000,           # Treasury's cost of the plan paying an unreduced pension from layoff (about 7 years early)
    tax_per_year=0.15,          # $B of local property tax lost each year as closures accumulate (plants, mines, refineries)
    refi_subsidy=0.25,          # $B: Treasury's credit cost on ratepayer-backed refinancing bonds over the window
    admin=0.05,                 # administration as a share of payments (state UI agencies as Labor's agents)
)


def guarantee_per_cohort():
    g = G
    n = g["workers_per_year"] * g["take_up"]
    top = 0.9 - (1 - g["gap"])                                                      # 0.20 of old hourly pay
    wi = top * g["hours"] * g["months_paid"] / 12 * g["pay"]
    tr = ((0.9 - g["ui"]) * 6 + 0.9 * (g["train_months"] - 6)) / 12 * g["pay"] + g["train_cost"] + top * g["hours"] * g["pay"]
    old = g["share_db"] * g["db_waiver"] + (1 - g["share_db"]) * 2 * (0.9 - g["ui"] / 4) * g["pay"]
    rest = n * (1 - g["share_55"])
    workers = n * g["share_55"] * old + rest * g["share_job"] * wi + rest * g["share_train"] * tr
    return workers * (1 + g["admin"]) / 1e9                                          # $B, 2030 dollars, per year's closures


def memo7():
    per = guarantee_per_cohort()
    out = {}
    for y in Y:
        grow = 1.03 ** (y - 2030)
        # worker payments: each year's closures are paid over about two years; the first year's cohort half in FY2030
        workers = per * grow * (0.5 if y == 2030 else 1.0)
        # places: replacement starts at the full lost tax and falls 10 points a year for ten years, cohort by cohort
        places = sum(G["tax_per_year"] * max(0.0, 1 - 0.1 * (y - c)) for c in range(2030, y + 1)) * 1.02 ** (y - 2030)
        refi = G["refi_subsidy"] / 10 if y <= 2039 else 0.0
        out[y] = workers + places + refi
    return out


# ---- 6. Assemble --------------------------------------------------------------------------------------------------
PLAN_GAP_FY2040 = 4256.6     # plan-wide FY2040 general-fund primary gap, $B short, case `mixed` (models/data/recovery-budget-paths.csv)
GDP_FY2040 = 54167.0


def main():
    rows = booked()
    model = coverage_read.run()
    share = {y: model[y]["share_B"] for y in Y}
    cx, c5 = memo1(rows, share)
    g7 = memo7()
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
    chg = {y: cx[y] + c5[y] + GRID2[y] + BILLS[y] + g7[y] for y in Y}
    tot = {y: tot_b[y] + chg[y] for y in Y}
    print(f"{'CHANGE vs booked':28s}" + fmt(chg))
    print(f"{'DECIDED SET':28s}" + fmt(tot))
    print(f"\nshare_B by year: " + " ".join(f"{y}:{share[y]:.3f}" for y in Y))
    print(f"memo 7 B per year's closures (2030 dollars): ${guarantee_per_cohort():.2f}B")
    print(f"FY2040: decided set ${tot[2040]:.1f}B = {100 * tot[2040] / GDP_FY2040:.2f}% of GDP; "
          f"{100 * tot[2040] / PLAN_GAP_FY2040:.1f}% of the plan-wide gap (${PLAN_GAP_FY2040}B); change {chg[2040]:+.1f}B "
          f"= {100 * chg[2040] / PLAN_GAP_FY2040:+.2f}% of the gap")
    d35 = model[2035]
    print(f"Dividend per adult 2035 (nominal): package ${d35['dividend_adult_package']:.0f}, B ${d35['dividend_adult_B']:.0f}")
    return dict(rows=rows, cx=cx, c5=c5, grid2=GRID2, bills=BILLS, g7=g7, change=chg, total=tot, share=share)


if __name__ == "__main__":
    main()
