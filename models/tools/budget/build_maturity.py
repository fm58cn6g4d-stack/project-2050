#!/usr/bin/env python3
"""build_maturity.py: the maturity structure of Treasury marketable debt, for the interest-rate stress.

Role: writes models/data/budget/treasury-maturity.csv from the Treasury's Monthly Statement of the
Public Debt (MSPD), Table III (detail of marketable Treasury securities outstanding), for one month-end.
Status: current (budget piece B6, item 1). The fiscal model reads the file to phase a rate shock in as
debt rolls over (ASM-RATE-ROLLOVER); it never calls the API itself.

The file holds, by quarter after the record date, the amount of marketable debt that matures (or, for
floating-rate notes, resets) in that quarter, and the share of the whole that is still at its old rate
at the end of the quarter. Floating-rate notes reset weekly to the 13-week bill rate, so they count as
repricing at once (quarter 0). TIPS count by maturity like other notes and bonds. Amounts are the
outstanding amount Treasury reports (face value, TIPS with their inflation adjustment), in billions.

Source: Bureau of the Fiscal Service, fiscaldata.treasury.gov, dataset "Monthly Statement of the Public
Debt", table mspd_table_3_market. US government work, public domain.

Usage (from the repository root):
  python3 models/tools/budget/build_maturity.py                 # fetch and write
  python3 models/tools/budget/build_maturity.py --check         # fetch and compare with the committed file
  python3 models/tools/budget/build_maturity.py --json FILE     # use a saved API response instead of fetching
"""
import argparse, csv, datetime as dt, io, json, os, sys, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OUT = os.path.join(ROOT, "models", "data", "budget", "treasury-maturity.csv")
RECORD_DATE = "2026-09-30"   # end of FY2026, the model's first year
API = ("https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_3_market"
       "?filter=record_date:eq:%s&page[size]=10000")
QUARTERS = 124               # 31 years: the longest bond outstanding matures within 30


def fetch(record_date):
    with urllib.request.urlopen(API % record_date, timeout=60) as r:
        return json.load(r)


def build(rows, record_date):
    t0 = dt.date.fromisoformat(record_date)
    by_q = [0.0] * (QUARTERS + 1)
    total_line = None
    for r in rows:
        if r["security_class1_desc"] == "Total Marketable":
            total_line = float(r["outstanding_amt"]) / 1000
        if r["maturity_date"] == "null" or r["outstanding_amt"] == "null":
            continue   # subtotal lines, and reopenings Treasury reports on the original issue's line
        amt = float(r["outstanding_amt"]) / 1000
        if r["security_class1_desc"] == "Floating Rate Notes":
            q = 0
        else:
            days = (dt.date.fromisoformat(r["maturity_date"]) - t0).days
            q = max(0, -(-days * 4 // 365))   # the quarter it matures in: 1 = within three months
        if q > QUARTERS:
            raise ValueError("security matures beyond %d quarters: %s" % (QUARTERS, r["maturity_date"]))
        by_q[q] += amt
    tot = sum(by_q)
    if total_line is not None and abs(tot - total_line) > 0.01 * total_line:
        raise ValueError("securities sum to %.1f billion, Treasury's total line is %.1f" % (tot, total_line))
    out, left = [], tot
    for q, a in enumerate(by_q):
        left -= a
        out.append(dict(quarter=q, years=q / 4, maturing_bn=round(a, 3), share_unrepriced=round(max(left, 0.0) / tot, 6)))
    return out, tot, total_line


def write(rows, f):
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["quarter", "years", "maturing_bn", "share_unrepriced"])
    for r in rows:
        w.writerow([r["quarter"], r["years"], "%.3f" % r["maturing_bn"], "%.6f" % r["share_unrepriced"]])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--json")
    a = ap.parse_args()
    data = json.load(open(a.json)) if a.json else fetch(RECORD_DATE)
    rows, tot, line = build(data["data"], RECORD_DATE)
    buf = io.StringIO(); write(rows, buf)
    wam = sum(r["years"] * r["maturing_bn"] for r in rows) / tot
    print("marketable debt %s: %.1f billion (Treasury's total line %.1f); average years to repricing %.2f"
          % (RECORD_DATE, tot, line or float("nan"), wam))
    if a.check:
        same = open(OUT).read() == buf.getvalue()
        print("treasury-maturity.csv " + ("matches" if same else "DIFFERS"))
        sys.exit(0 if same else 1)
    open(OUT, "w").write(buf.getvalue())


if __name__ == "__main__":
    main()
