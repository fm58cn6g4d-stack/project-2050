#!/usr/bin/env python3
"""democratic_renewal_booking.py: the democratic renewal foundation's booking in the adopted inputs, derived from
the dossier's cost and pace tools.

Role: the one place the foundation's booked rows, year shapes, perms and ten-year amounts are computed (democratic
renewal's booking, tier 3; dossiers/foundations/democratic-renewal/6-cost.md, part 9). Status: current. It reads
democratic_renewal_cost.py (the unbooked lines' paths) and democratic_renewal_pace.py (decision-sheet item D4, option B,
`DEC-2026-11-18-14`) and returns the numbers that models/data/inputs/ (ledger-bills.csv, ledger-revenue.csv,
fiscal-years.csv, fiscal-profiles.csv) and models/data/budget/provisions.csv hold. test_fiscal_democratic_renewal.py
checks that the inputs equal them, so a change to either tool shows up as a failing test, not a silent drift.

    python3 models/tools/democratic_renewal_booking.py           # the rows and the totals
    python3 models/tools/democratic_renewal_booking.py --json    # the same as JSON
    python3 models/tools/democratic_renewal_booking.py --write   # patch the inputs

What is booked ($ billion by federal fiscal year, a cost positive):
- Two new spending rows for the lines section 6 priced and sent to stage G unbooked: DEM-17.02 (the permanent
  library line) and CRT-20.01 (civil legal aid through the Legal Services Corporation), each an annual appropriation.
- D4, option B (`DEC-2026-11-18-14`): part G's allocation inside CAP-7 on the hiring pace, and the IRS's enforcement
  yield (G8) lagged with it. Two new rows of their own, so no adopted row's amount or profile changes: CAP-7P (a
  negative spending row: less CAP-7 outlay in FY2030-33) and G8P (a base-revenue row: the yield lost with it). Both
  are zero in FY2040. They are timing rows against the booked ramp, not savings: the booking's ceiling is unchanged
  (memo 10's contingency stays inside CAP-7's $279.2B, as decided).
- Labels and notes only (no amount): CRT-P1 names its room for CRT-5.09, the immigration court's structure (reading (a)
  of 6-cost.md part 4; the line stays unbooked, DEC-2026-11-17-97), CAP-8 carries CAP-6.01 (statute tracking, about $0.09B), and the
  CAP-7S and CAP-7 notes say memo 10's delivery contingency is inside the booked amount, not added.
- Not booked: IMM-1's rebooking for memo 9 part 2 (about -$4.3B over FY2036-39; `DEC-2026-11-17-56` says any change to
  IMM-1's booking is a later tier-3 change and no DEC row decides it), the House seats for a new state (contingent on
  an admission act), the chamber build, the October 26 allowance, #404's residual (stage G).
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
INPUTS = os.path.join(ROOT, "models", "data", "inputs")
YEARS = list(range(2030, 2041))
W = list(range(2030, 2040))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


WB = _load("work_booking_helpers", os.path.join(HERE, "work_booking.py"))     # _patch, perm_for, fiscal(), r()
DRC = _load("drc_booking", os.path.join(HERE, "democratic_renewal_cost.py"))
PACE = _load("drp_booking", os.path.join(HERE, "democratic_renewal_pace.py"))
r = WB.r

LIBRARY = "DEM-17.02, the permanent library line"
AID = "CRT-20.01, civil legal aid through LSC"
# (ledger id, domain, label, rail, source line)
SPENDING = [
    ("DEM-17.02", "Democracy", "Public libraries: the permanent library line (DEM-17.02)", LIBRARY),
    ("CRT-20.01", "Courts", "Civil legal aid through the Legal Services Corporation (CRT-20.01)", AID),
    ("CAP-7P", "Capacity", "CAP-7.01 on the hiring pace: part G's allocation spent as staff are hired, a timing row "
     "against CAP-7's booked ramp (DEC-2026-11-18-14)", "pace_outlay"),
]
REVENUE = [
    ("G8P", "IRS enforcement yield lagged with the IRS's hiring (G8; DEC-2026-11-18-14)", "rev_individual", "pace_g8"),
]
RAIL = "APPROPS"
# The existing rows that take a label or note and no amount.
LABELS = {
    "CRT-P1": dict(bill="Courts package: term limits, phased judgeships, random assignment, ethics (DEM6 merged, C11), "
                        "and room for the Article I immigration court's structure (CRT-5.09)",
                   note="Democratic renewal booking (dossiers/foundations/democratic-renewal/6-cost.md part 4): the row's "
                        "contents (CRT-1 to CRT-4, CRT-6 to CRT-15) cost about $0.5-0.7B over FY2030-39; CRT-5.09, the "
                        "court's structure, about $6.9B (range $3.2-9.7B), fits inside the rest, so the amount is "
                        "unchanged; CRT-5.09 stays unbooked as a line (DEC-2026-11-17-97) and its reading (a) or (b) is "
                        "stage G's. The judge teams and counsel are in IMM-1 (immigration booking)"),
}
NOTES_ADD = {
    "CAP-8": "Democratic renewal booking: CAP-6.01 (statute tracking, about $0.09B over FY2030-39) rides this row with "
             "no change in amount (6-cost.md part 9).",
    "CAP-7S": "Democratic renewal booking: memo 10's delivery contingency (CAP-7S.02, DEC-2026-11-17-58), about "
              "$43.2B on part G's basis, is inside this booked amount, not added; the surge must be obligated by "
              "September 30, 2036 (DEC-2026-11-18-32).",
    "CAP-7": "Democratic renewal booking: memo 10's delivery contingency (CAP-7S.02), about $29.7B on part G's own path "
             "and $35.3B on this ramp, is inside this booked amount, not added. The hiring-pace timing (D4 option B, "
             "DEC-2026-11-18-14) is the separate row CAP-7P, with the IRS's yield lag in G8P (6-cost.md part 9).",
}


def fiscal():
    return WB.fiscal()


def path_list(p):
    return [p[y] for y in YEARS]


def booking():
    F = fiscal()
    B = F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    un = DRC.summary()["unbooked"]                # the lines that stay unbooked after this booking
    unb = DRC.PRICED
    pace = PACE.booking_paths()
    d4 = PACE.summary()["d4"]
    paths = {}                                    # id -> (lo, mid, hi) lists over 2030-40, cost positive
    for rid, _dom, _lab, src in SPENDING:
        if src in unb:
            lo, mid, hi = (path_list(p) for p in unb[src])
            paths[rid] = (lo, mid, hi)
    outlay = [-pace["outlay"][y] for y in YEARS]                           # less outlay: a negative cost
    paths["CAP-7P"] = ([x * d4["outlay_range"][1] / d4["outlay_effect"] for x in outlay], outlay,
                       [x * d4["outlay_range"][0] / d4["outlay_effect"] for x in outlay])
    loss = [pace["g8_loss"][y] for y in YEARS]                             # less revenue: a positive cost
    paths["G8P"] = ([x * d4["g8_lag_range"][0] / d4["g8_lag"] for x in loss], loss,
                    [x * d4["g8_lag_range"][1] / d4["g8_lag"] for x in loss])
    years, fy2040, perms, ledger, revenue, meta = {}, {}, {}, {}, {}, {}
    for rid, dom, label, _src in SPENDING:
        lo, c, hi = paths[rid]
        mid = r(sum(c[:10]) / 1000, 3)               # the ledger carries spending rows to $1 billion (ledger.json)
        ends = sorted([r(sum(lo[:10]) / 1000, 3), r(sum(hi[:10]) / 1000, 3)])
        ledger[rid] = (ends[0], mid, ends[1])
        years[rid] = [r(c[k], 4) for k in range(10)]
        fy2040[rid] = c[10]
        s = sum(years[rid])
        v39 = years[rid][9] * (mid * 1000 / s if s else 0)
        perms[rid] = round(WB.perm_for(F, B, v39, c[10]), 6) + 0.0
        meta[rid] = ("new", "out_disc_nondefense", label, dom)
    for rid, label, cat, _src in REVENUE:
        lo, c, hi = paths[rid]
        years[rid] = [r(c[k], 4) for k in range(10)]
        fy2040[rid] = c[10]
        m = r(-sum(c[:10]) / 1000, 4)                               # revenue: a gain is positive in ledger-revenue.csv
        ends = sorted([r(-sum(lo[:10]) / 1000, 4), r(-sum(hi[:10]) / 1000, 4)])
        revenue[rid] = (ends[0], m, ends[1])
        s = sum(years[rid])
        v39 = years[rid][9] * (m * -1000 / s if s else 0)
        perms[rid] = round(WB.perm_for(F, B, v39, c[10]), 6) + 0.0
        meta[rid] = ("revenue", cat, label, "Capacity")
    spend_w = sum(v[1] for v in ledger.values())
    rev_w = sum(v[1] for v in revenue.values())
    t = dict(spending_window=spend_w, revenue_window=-rev_w, net_window=spend_w - rev_w,
             net_fy2040=sum(fy2040.values()),
             lines={k: sum(years[k]) for k in years},
             library_and_aid_window=ledger["DEM-17.02"][1] + ledger["CRT-20.01"][1],
             pace_outlay_window=ledger["CAP-7P"][1], pace_g8_window=-revenue["G8P"][1])
    unbooked_after = sorted(un)
    return dict(years=years, fy2040=fy2040, perms=perms, ledger=ledger, revenue=revenue, meta=meta, totals=t,
                unbooked=unbooked_after, labels=LABELS, notes_add=NOTES_ADD)


# ---------------------------------------------------------------------------------------------------------------
# Writing the inputs (the booking PR's one-time patch; the test then holds them equal)
def _spec_rows(b):
    asm = (WB.ASM_YEARS + " ASM-SPENDOUT ASM-SPENDOUT-NORM ASM-BA-LEADS-OUTLAYS")
    out = []
    for rid, (how, cat, label, dom) in b["meta"].items():
        note = ("Profile: the foundation's path (fiscal-years.csv), democratic renewal's booking "
                "(dossiers/foundations/democratic-renewal/6-cost.md part 9)")
        if how == "new":
            out.append(dict(id=rid, table="bill", parent="", label=label, in_model="yes", category=cat,
                            kind="discretionary", vehicle="regular_appropriations", vehicle_source="ledger rail APPROPS",
                            appropriation="annual", budget_authority="spendout", spendout_group="nondefense",
                            method="years", start="2030", ramp="1", indexation=WB.GROW, indexation_basis="model",
                            expiry="none", expiry_basis="model", continues_after_2039=f"{b['perms'][rid]:.6f}",
                            fade="0.0", unified="same", asm_ids=asm,
                            notes=note + (" | A timing row against CAP-7's booked ramp, zero in FY2040" if rid == "CAP-7P" else "")))
        else:
            out.append(dict(id=rid, table="base_revenue", parent="", label=label, in_model="yes", category=cat,
                            kind="revenue", vehicle="unknown", vehicle_source="", appropriation="none",
                            budget_authority="none", spendout_group="", method="years", start="2030", ramp="1",
                            indexation=WB.GROW, indexation_basis="model", expiry="none", expiry_basis="model",
                            continues_after_2039=f"{b['perms'][rid]:.6f}", fade="0.0", unified="same",
                            asm_ids=WB.ASM_YEARS, notes=note + " | Booked on the general fund in the base; a timing row "
                            "against G8's booked ramp, zero in FY2040"))
    return out


def _append_notes(fn, adds):
    import csv
    raw = open(fn, encoding="utf-8").read().split("\n")
    cols = next(csv.reader([raw[0]]))
    for n_, text in enumerate(raw[1:], start=1):
        if not text.strip():
            continue
        d = dict(zip(cols, next(csv.reader([text]))))
        if d["id"] in adds and adds[d["id"]] not in d["note"]:
            import io
            d["note"] = (d["note"] + " " if d["note"] else "") + adds[d["id"]]
            o = io.StringIO()
            csv.writer(o, lineterminator="").writerow([d.get(c, "") for c in cols])
            raw[n_] = o.getvalue()
    open(fn, "w", encoding="utf-8").write("\n".join(raw))


def write_inputs(b):
    note_y = ("democratic_renewal_booking.py: the unbooked lines' paths (democratic_renewal_cost.py) and D4 option B "
              "(democratic_renewal_pace.py), $B by federal fiscal year")
    led, prof, yrs, rev, prev = [], [], [], [], []
    for rid, (lo, mid, hi) in b["ledger"].items():
        how, cat, label, dom = b["meta"][rid]
        led.append(dict(id=rid, legacy_id="—", bill=label, domain=dom, source="dossiers/foundations/democratic-renewal/6-cost.md",
                        rail=RAIL, channel="General fund", cost_lo=f"{lo:g}", cost_mid=f"{mid:g}", cost_hi=f"{hi:g}",
                        own_revenue_mid="0", basis="estimate",
                        note="Democratic renewal's booking (dossiers/foundations/democratic-renewal/6-cost.md part 9; "
                             "democratic_renewal_booking.py)",
                        floor_days="0", felt_months="12", durability="60", target="2029-12"))
        prof.append(dict(table="bill", id=rid, cat=cat, ramp="1", grow=WB.GROW, end="", perm=f"{b['perms'][rid]:.6f}",
                         basis="The foundation's path (fiscal-years.csv); perm fitted so FY2040 is the path's (democratic renewal booking)"))
        yrs.append({"id": rid, **{f"y{2030 + k}": f"{b['years'][rid][k]:g}" for k in range(10)}, "note": note_y})
    for rid, (lo, mid, hi) in b["revenue"].items():
        how, cat, label, dom = b["meta"][rid]
        rev.append(dict(id=rid, option=label, channel="General fund", lo=f"{lo:g}", mid=f"{mid:g}", hi=f"{hi:g}",
                        in_base="yes", legal_risk="Low", overlap="",
                        source="dossiers/foundations/democratic-renewal/6-cost.md part 9; democratic_renewal_booking.py",
                        reaches_middle="no"))
        prev.append(dict(table="base revenue", id=rid, cat=cat, ramp="1", grow=WB.GROW, perm=f"{b['perms'][rid]:.6f}",
                         basis="The foundation's path (fiscal-years.csv); perm fitted so FY2040 is the path's (democratic renewal booking)"))
        yrs.append({"id": rid, **{f"y{2030 + k}": f"{b['years'][rid][k]:g}" for k in range(10)}, "note": note_y})
    lb = os.path.join(INPUTS, "ledger-bills.csv")
    WB._patch(lb, led)
    WB._patch(lb, [dict(id=k, **v) for k, v in b["labels"].items()])
    _append_notes(lb, b["notes_add"])
    WB._patch(os.path.join(ROOT, "models", "data", "budget", "provisions.csv"), _spec_rows(b), key="id")
    WB._patch(os.path.join(INPUTS, "fiscal-profiles.csv"), prof, match=("table", "bill"), keep=("cat", "start", "ramp", "end"))
    WB._patch(os.path.join(INPUTS, "fiscal-profiles.csv"), prev, match=("table", "base revenue"))
    WB._patch(os.path.join(INPUTS, "fiscal-years.csv"), yrs)
    WB._patch(os.path.join(INPUTS, "ledger-revenue.csv"), rev)


if __name__ == "__main__":
    b = booking()
    if "--json" in sys.argv:
        print(json.dumps(b, indent=1, default=str))
    elif "--write" in sys.argv:
        write_inputs(b)
        print("inputs patched")
    else:
        for k, v in b["years"].items():
            print(f"{k:10s} {sum(v)/1000:9.4f}T  FY2040 {b['fy2040'][k]:7.3f}  perm {b['perms'][k]:.6f}")
        print("ledger", b["ledger"])
        print("revenue", b["revenue"])
        print("totals", {k: (round(v, 4) if not isinstance(v, dict) else {a: round(c, 3) for a, c in v.items()})
                         for k, v in b["totals"].items()})
        print("unbooked lines after this booking", b["unbooked"])
