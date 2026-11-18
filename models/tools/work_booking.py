#!/usr/bin/env python3
"""work_booking.py: the work dossier's booking in the adopted inputs, derived from the dossier's path.

Role: the one place the work rows, year-by-year shapes, perms and ten-year amounts are computed (work's booking,
tier 3; dossiers/work/6-cost.md part 9). Status: current. It reads the dossier's fiscal-year path
(dossiers/work/tools/work_path.py, LINES) and returns the numbers that models/data/inputs/ (ledger-bills.csv,
ledger-revenue.csv, fiscal-years.csv, fiscal-profiles.csv, funds-ss-offbudget.csv, incidence-rows.csv) hold.
test_fiscal_work.py checks that the inputs equal them, so a change to the dossier's path shows up as a failing
test, not a silent drift.

    python3 models/tools/work_booking.py           # the rows and the totals
    python3 models/tools/work_booking.py --json    # the same as JSON
    python3 models/tools/work_booking.py --write   # patch the inputs (ledger, revenue, years, profiles, SS series)

What is booked (central path, $ billion by federal fiscal year; a cost positive):
- Four booked rows change: LAB-1 (the floor's indirect effect, CBO's net, on the rules bill), LAB-5 (the small-
  business credit, DEC-2026-11-18-22), LAB-8 (apprenticeship) and LAB-9 (civic service, without the gated tranche).
- Spending rows added: LAB-4.09 (the 14(c) grant), LAB-3 (the standards boards office and the wage commission),
  LAB-7.05 (outreach grants), LAB-11 (Extended Benefits in ordinary years, state administration, the conformity
  grant), LAB-18 (wage insurance, its administration, the hours field, and the lines Espen decided on November 18:
  work-connected good-cause quits, their misuse and the records-based offer) and LAB-19 (the displacement measure).
- Revenue rows, each its own base-revenue row (6-cost.md, "Counting rules"): LAB-11T (the income-tax offset on
  employers' larger UI taxes, a loss), LAB-18T (income tax on wage insurance, a gain) and LAB-2P (civil penalties,
  a gain).
- Social Security's funds: the same UI deduction takes payroll tax from the trust funds (WRK-UI-SS, off budget,
  funds-ss-offbudget.csv's second series, % of taxable payroll).
- Not booked: the gated service tranche (LAB-9.03) and the standby displacement trigger (LAB-19.04, 19.05), both
  contingent and zero unless an event occurs; Extended Benefits in a downturn; the UI trust funds' own lines
  (employer-financed, net zero on the general fund); the AmeriCorps grantees' match (not federal); the three W10
  provisions (no federal line).
- Rails are unchanged: the dossier's "R1" is its own name for the money act of mid-2029, which the ledger's R2
  (summer 2029) already holds; no rail, vote or calendar row moves.
"""
import csv
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
INPUTS = os.path.join(ROOT, "models", "data", "inputs")
W = list(range(2030, 2040))
GROW = "gdp"

# (ledger id, path lines, kind, ledger cat, label for a new row, rail, target month)
SPENDING = [
    ("LAB-1", ["floor"], "change", "out_disc_nondefense", None),
    ("LAB-5", ["credit"], "change", "out_other_mandatory", None),
    ("LAB-8", ["apprenticeship"], "change", "out_disc_nondefense", None),
    ("LAB-9", ["service"], "change", "out_other_mandatory", None),
    ("LAB-4.09", ["14c"], "new", "out_other_mandatory", "14(c) transition grant (LAB-4.09)"),
    ("LAB-3", ["boards"], "new", "out_disc_nondefense",
     "Standards boards office and the wage commission (LAB-3, LAB-4.04)"),
    ("LAB-7.05", ["outreach"], "new", "out_disc_nondefense", "Wage and safety outreach grants (LAB-7.05)"),
    ("LAB-11", ["eb", "ui_admin", "conformity"], "new", "out_other_mandatory",
     "Unemployment insurance on the general fund: Extended Benefits in ordinary years, state administration, "
     "conformity grant (LAB-11)"),
    ("LAB-18", ["wi", "wi_admin", "hours", "quits", "quits_misuse", "wi_offer"], "new", "out_other_mandatory",
     "Wage insurance, its administration, the hours field, good-cause quits and the records-based offer (LAB-18)"),
    ("LAB-19", ["measure"], "new", "out_disc_nondefense",
     "Displacement measure: occupation in wage records and BLS's yearly report (LAB-19.01, 19.03)"),
]
REVENUE = [
    ("LAB-11T", ["ui_offset"], "Income-tax offset on employers' larger unemployment taxes (LAB-11.05)", "rev_individual"),
    ("LAB-18T", ["wi_tax"], "Income tax on wage insurance (LAB-18.02)", "rev_individual"),
    ("LAB-2P", ["penalties"], "Civil penalties under the labor act and wage law (LAB-2.01, 7.04, 13.01)",
     "rev_individual"),
]
SS_LINE = "ui_offset_ss"
RAIL = {"LAB-1": "FLOOR", "LAB-3": "APPROPS", "LAB-7.05": "APPROPS", "LAB-19": "APPROPS"}   # the rest R2
LEDGER_COLS = ["id", "legacy_id", "bill", "domain", "source", "rail", "channel", "cost_lo", "cost_mid", "cost_hi",
               "own_revenue_mid", "basis", "note", "floor_days", "felt_months", "durability", "target"]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def path_module():
    tools = os.path.join(ROOT, "dossiers", "work", "tools")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    return _load("work_path", os.path.join(tools, "work_path.py"))


def fiscal():
    return _load("wrk_fiscal", os.path.join(HERE, "fiscal-model.py"))


def r(x, n=4):
    return round(x + 0.0, n)


def _sum(by, ids, which, k):
    return sum(by[i][which][k] for i in ids)


def perm_for(F, B, v2039, v2040):
    """The perm that makes a years row's FY2040 equal v2040 (row_path: FY2039 x perm x growth)."""
    if abs(v2039) < 1e-12:
        return 0.0
    g = F.growth_index(B, GROW)
    return v2040 / (v2039 * g[2040] / g[2039])


def booking():
    P, F = path_module(), fiscal()
    B = F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    by = {ln["id"]: ln for ln in P.LINES}
    booked = {i for _, ids, *_ in SPENDING for i in ids} | {i for _, ids, *_ in REVENUE for i in ids}
    unbooked = {ln["id"] for ln in P.LINES} - booked - {SS_LINE}
    years, fy2040, perms, ledger, revenue, meta = {}, {}, {}, {}, {}, {}
    for rid, ids, how, cat, label in SPENDING:
        c = [_sum(by, ids, "central", k) for k in range(11)]
        lo, hi = sorted([P.dec([_sum(by, ids, "low", k) for k in range(11)]) / 1000,
                         P.dec([_sum(by, ids, "high", k) for k in range(11)]) / 1000])
        mid = r(P.dec(c) / 1000, 3)
        ledger[rid] = (r(lo, 3), mid, r(hi, 3))
        years[rid] = [r(c[k], 4) for k in range(10)]
        fy2040[rid] = c[10]
        s = sum(years[rid])
        v39 = years[rid][9] * (mid * 1000 / s if s else 0)
        perms[rid] = perm_for(F, B, v39, c[10])
        meta[rid] = (how, cat, label)
    for rid, ids, label, cat in REVENUE:
        c = [_sum(by, ids, "central", k) for k in range(11)]
        lo_c, hi_c = P.dec([_sum(by, ids, "low", k) for k in range(11)]), P.dec([_sum(by, ids, "high", k) for k in range(11)])
        years[rid] = [r(c[k], 4) for k in range(10)]
        fy2040[rid] = c[10]
        m = -sum(years[rid]) / 1000                         # revenue: a gain is positive in ledger-revenue.csv
        ends = sorted([-lo_c / 1000, -hi_c / 1000])
        revenue[rid] = (r(ends[0]), r(m), r(ends[1]))
        s = sum(years[rid])
        v39 = years[rid][9]
        perms[rid] = perm_for(F, B, v39, c[10])
        meta[rid] = ("revenue", cat, label)
    # Social Security: the UI deduction's payroll-tax loss, as % of taxable payroll (funds-ss-economics.csv)
    ss = by[SS_LINE]["central"]
    econ = {int(x["year"]): float(x["taxable_payroll_bn"]) for x in csv.DictReader(open(os.path.join(INPUTS, "funds-ss-economics.csv")))}
    ss_pct = {}
    for k, y in enumerate(range(2030, 2041)):
        base = econ.get(y)
        if base is None:        # the economics file interpolates geometrically between its years
            lo_y = max(t for t in econ if t <= y)
            hi_y = min(t for t in econ if t >= y)
            base = econ[lo_y] if lo_y == hi_y else econ[lo_y] * (econ[hi_y] / econ[lo_y]) ** ((y - lo_y) / (hi_y - lo_y))
        ss_pct[y] = r(100 * ss[k] / base, 4)
    tn = lambda lst: sum(lst) / 1000  # noqa: E731
    spend_w = sum(ledger[k][1] for k in ledger)
    rev_w = sum(v[1] for v in revenue.values())
    gf_2040 = sum(fy2040.values())
    totals = dict(spending_window=spend_w, revenue_window=-rev_w, net_window=spend_w - rev_w,
                  net_fy2040=gf_2040, ss_window=tn(ss[:10]), ss_fy2040=ss[10])
    return dict(years=years, fy2040=fy2040, perms=perms, ledger=ledger, revenue=revenue, meta=meta,
                ss_pct=ss_pct, totals=totals, unbooked=sorted(unbooked))


# ---------------------------------------------------------------------------------------------------------------
# Writing the inputs (the booking PR's one-time patch; the test then holds them equal)
def _patch(fn, rows, key="id", match=None, keep=()):
    """Replace the fields of the matching rows (keeping the columns in `keep` for an existing row) and append the
    rest. Every untouched line stays byte for byte as it was."""
    raw = open(fn, encoding="utf-8").read().split("\n")
    trail = raw[-1] == ""
    if trail:
        raw = raw[:-1]
    cols = next(csv.reader([raw[0]]))
    todo = {r_[key]: r_ for r_ in rows}

    def line(d):
        import io
        out = io.StringIO()
        csv.writer(out, lineterminator="").writerow([d.get(c, "") for c in cols])
        return out.getvalue()

    for n, text in enumerate(raw[1:], start=1):
        if not text.strip():
            continue
        d = dict(zip(cols, next(csv.reader([text]))))
        if d.get(key) in todo and (match is None or d.get(match[0]) == match[1]):
            new = todo.pop(d[key])
            for k, v in new.items():
                if k in cols and k not in keep:
                    d[k] = v
            raw[n] = line(d)
    for d in todo.values():
        raw.append(line(d))
    open(fn, "w", encoding="utf-8").write("\n".join(raw) + ("\n" if trail else ""))


ASM_YEARS = "ASM-WINDOW ASM-SIGN ASM-INCREMENT ASM-CALIB-MID ASM-PROF-YEARS ASM-GDP-PATH"


def _spec_rows(b, ends):
    """The budget model's provision specs (models/data/budget/provisions.csv) for work's new rows."""
    out = []
    appr = {"LAB-3", "LAB-7.05", "LAB-19"}
    for rid, (how, cat, label) in b["meta"].items():
        if how == "new":
            if rid in appr:
                kind = dict(kind="discretionary", vehicle="regular_appropriations", vehicle_source="ledger rail APPROPS",
                            appropriation="annual", budget_authority="spendout", spendout_group="nondefense",
                            asm=ASM_YEARS + " ASM-SPENDOUT ASM-SPENDOUT-NORM ASM-BA-LEADS-OUTLAYS")
            else:
                kind = dict(kind="mandatory", vehicle="reconciliation", vehicle_source="ledger rail R2",
                            appropriation="direct_spending", budget_authority="outlays", spendout_group="",
                            asm=ASM_YEARS + " ASM-BA-EQUALS-OUTLAYS")
            end = ends.get(rid, "")
            out.append(dict(id=rid, table="bill", parent="", label=label, in_model="yes", category=cat,
                            kind=kind["kind"], vehicle=kind["vehicle"], vehicle_source=kind["vehicle_source"],
                            appropriation=kind["appropriation"], budget_authority=kind["budget_authority"],
                            spendout_group=kind["spendout_group"], method="years", start="2030", ramp="1",
                            indexation=GROW, indexation_basis="model", expiry=end or "none",
                            expiry_basis="stated" if end else "model", continues_after_2039=f"{b['perms'][rid]:.6f}",
                            fade="0.0", unified="same", asm_ids=kind["asm"],
                            notes="Profile: section 6's central path (fiscal-years.csv), the work booking (dossiers/work/6-cost.md part 9)"))
        elif how == "revenue":
            out.append(dict(id=rid, table="base_revenue", parent="", label=label, in_model="yes", category=cat,
                            kind="revenue", vehicle="unknown", vehicle_source="", appropriation="none",
                            budget_authority="none", spendout_group="", method="years", start="2030", ramp="1",
                            indexation=GROW, indexation_basis="model", expiry="none", expiry_basis="model",
                            continues_after_2039=f"{b['perms'][rid]:.6f}", fade="0.0", unified="same", asm_ids=ASM_YEARS,
                            notes="Profile: section 6's central path (fiscal-years.csv), the work booking (dossiers/work/6-cost.md part 9) | Booked on the general fund in the base"))
    return out


def _patch_specs(b, ends):
    fn = os.path.join(ROOT, "models", "data", "budget", "provisions.csv")
    new = _spec_rows(b, ends)
    ids = {n["id"] for n in new}
    # the four booked rows keep their spec but take the years method and the fitted perm
    for rid in ("LAB-1", "LAB-5", "LAB-8", "LAB-9"):
        raw = open(fn, encoding="utf-8").read().split("\n")
        cols = next(csv.reader([raw[0]]))
        for n_, text in enumerate(raw[1:], start=1):
            if not text.strip():
                continue
            d = dict(zip(cols, next(csv.reader([text]))))
            if d["id"] == rid and d["table"] == "bill":
                d["method"] = "years"
                d["continues_after_2039"] = f"{b['perms'][rid]:.6f}"
                toks = [t for t in d["asm_ids"].split() if t not in ("ASM-PROF-DEFAULT", "ASM-PROF-RAMP", "ASM-PROF-YEARS")]
                toks.insert(toks.index("ASM-CALIB-MID") + 1, "ASM-PROF-YEARS")
                d["asm_ids"] = " ".join(toks)
                if "work booking" not in d["notes"]:
                    d["notes"] = (d["notes"] + " | " if d["notes"] else "") + "Year shape from the work booking (fiscal-years.csv; dossiers/work/6-cost.md part 9)"
                import io
                o = io.StringIO()
                csv.writer(o, lineterminator="").writerow([d.get(c, "") for c in cols])
                raw[n_] = o.getvalue()
                open(fn, "w", encoding="utf-8").write("\n".join(raw))
                break
    _patch(fn, new, key="id", match=None)


SS_ROW = ('WRK-UI-SS,"Employers\' larger unemployment taxes: payroll tax lost on the deduction (LAB-11.05)",direct,,,2031,,,,'
          'LAB-11T,"decided and booked (work); work_path.py\'s ui_offset_ss line (dossiers/work/6-cost.md part 2; $43.3B over '
          'FY2030-39) as % of taxable payroll in funds-ss-offbudget.csv\'s wrk_ui_pct_payroll; revenue only (employers deduct '
          'state UI taxes; no matching benefit change); ledger_rows links the on-budget offset on the same deduction"')


def _write_ss(b):
    fn = os.path.join(INPUTS, "funds-ss-offbudget.csv")
    rows = list(csv.DictReader(open(fn, newline="", encoding="utf-8")))
    for r_ in rows:
        r_["wrk_ui_pct_payroll"] = f"{b['ss_pct'][int(r_['year'])]:.4f}"
    with open(fn, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["year", "loss_pct_payroll", "wrk_ui_pct_payroll", "basis"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    fp = os.path.join(INPUTS, "funds-ss-provisions.csv")
    t = open(fp, encoding="utf-8").read()
    if "\nWRK-UI-SS," not in t:
        open(fp, "w", encoding="utf-8").write(t.rstrip("\n") + "\n" + SS_ROW + "\n")


def write_inputs(b):
    note_y = "work_booking.py: section 6's central path (dossiers/work/tools/work_path.py), $B by federal fiscal year"
    led, prof, yrs, rev, prev, ends = [], [], [], [], [], {}
    for rid, (lo, mid, hi) in b["ledger"].items():
        how, cat, label = b["meta"][rid]
        row = dict(id=rid, cost_lo=f"{lo:.3f}", cost_mid=f"{mid:.3f}", cost_hi=f"{hi:.3f}")
        if how == "new":
            row.update(legacy_id="—", bill=label, domain="Labor", source="dossiers/work/6-cost.md",
                       rail=RAIL.get(rid, "R2"), channel="General fund", own_revenue_mid="0", basis="estimate",
                       note="Work's booking (dossiers/work/6-cost.md part 9; work_booking.py)", floor_days="0",
                       felt_months="12", durability="70", target="2029-summer")
        else:
            row["basis"] = "estimate"
            row["note"] = "Work's booking (dossiers/work/6-cost.md part 9; work_booking.py)"
        led.append(row)
        nz = [k for k in range(10) if abs(b["years"][rid][k]) > 1e-12]
        end = str(2030 + max(nz)) if nz and max(nz) < 9 and how == "new" else ""
        ends[rid] = end
        prof.append(dict(table="bill", id=rid, cat=cat, ramp="1", grow=GROW, end=end, perm=f"{b['perms'][rid]:.6f}",
                         basis="Section 6's central path (fiscal-years.csv); perm fitted so FY2040 is the path's (work booking)"))
        yrs.append({"id": rid, **{f"y{2030 + k}": f"{b['years'][rid][k]:g}" for k in range(10)}, "note": note_y})
    for rid, (lo, mid, hi) in b["revenue"].items():
        how, cat, label = b["meta"][rid]
        rev.append(dict(id=rid, option=label, channel="General fund", lo=f"{lo:g}", mid=f"{mid:g}", hi=f"{hi:g}",
                        in_base="yes", legal_risk="Low", overlap="", source="dossiers/work/6-cost.md part 9; work_booking.py",
                        reaches_middle="no"))
        prev.append(dict(table="base revenue", id=rid, cat=cat, ramp="1", grow=GROW, perm=f"{b['perms'][rid]:.6f}",
                         basis="Section 6's central path (fiscal-years.csv); perm fitted so FY2040 is the path's, then GDP (work booking)"))
        yrs.append({"id": rid, **{f"y{2030 + k}": f"{b['years'][rid][k]:g}" for k in range(10)}, "note": note_y})
    _patch(os.path.join(INPUTS, "ledger-bills.csv"), led)
    _patch_specs(b, ends)
    _write_ss(b)
    _patch(os.path.join(INPUTS, "fiscal-profiles.csv"), prof, match=("table", "bill"), keep=("cat", "start", "ramp", "end"))
    _patch(os.path.join(INPUTS, "fiscal-profiles.csv"), prev, match=("table", "base revenue"))
    _patch(os.path.join(INPUTS, "fiscal-years.csv"), yrs)
    _patch(os.path.join(INPUTS, "ledger-revenue.csv"), rev)


if __name__ == "__main__":
    b = booking()
    if "--json" in sys.argv:
        print(json.dumps(b, indent=1, default=str))
    elif "--write" in sys.argv:
        write_inputs(b)
        print("inputs patched")
    else:
        for k, v in b["years"].items():
            print(f"{k:10s} {sum(v)/1000:8.4f}T  FY2040 {b['fy2040'][k]:7.2f}  perm {b['perms'][k]:.6f}")
        print("ledger", b["ledger"])
        print("revenue", b["revenue"])
        print("ss_pct", b["ss_pct"])
        print("totals", {k: round(v, 4) for k, v in b["totals"].items()})
        print("unbooked lines", b["unbooked"])
