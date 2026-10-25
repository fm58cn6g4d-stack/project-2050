"""fiscal-profiles.py: year profiles for every ledger row the long-term model uses.

The ledger scores everything as 2030-39 totals. The long-term model needs annual paths, so
each row gets a profile here. The model calibrates every profile so its FY2030-39 sum equals
the ledger's ten-year midpoint exactly; the profile only decides how that total is spread
across the window and how the row runs on after 2039. Every profile is an estimate (basis
noted) until a domain file supplies a year-by-year score; when one does, put it in YEARS.

Fields
  cat     baseline category the row adds to (see fiscal-data.py), so the all-of-government
          view stays in CBO's categories. Outlay rows use out_*, revenue rows rev_*.
  start   first fiscal year with any effect (default 2030)
  ramp    years to full phase-in from start (1 = full in the first year)
  grow    growth index: "gdp", "cpi", or a baseline category name (the row then keeps a
          constant share of that category: health rows track CBO's health spending,
          revenue rows track their tax base, including bracket creep)
  end     last year of a time-limited line (None = permanent)
  perm    share of the 2039 run rate that continues after 2039 (1.0 = all; time-limited
          capital and temporary credits carry less)
  fade    after 2039, the continuing part shrinks this share a year (e.g. credits that phase
          down as clean energy saturates)

Sign convention: positive = raises the deficit. Ledger outlay rows are costs (positive),
revenue rows are entered as negatives, savings as negatives.
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inputs import read, num, opt

# The profiles are in index/data/inputs/fiscal-profiles.csv (one row per ledger row; table = bill, base revenue
# or option) and the year-by-year overrides in fiscal-years.csv. A blank cell takes the default above.
BILLS, REVENUE, CUTS = {}, {}, {}
for r in read("fiscal-profiles.csv"):
    p = {}
    for k, conv in (("kind", str), ("cat", str), ("start", num), ("ramp", num), ("grow", str), ("end", num),
                    ("perm", num), ("fade", num), ("unified_zero", lambda v: v == "yes"), ("basis", str)):
        v = opt(r, k, conv)
        if v is not None: p[k] = v
    {"bill": BILLS, "base revenue": REVENUE, "option": CUTS}[r["table"]][r["id"]] = p

# Explicit year-by-year paths that override a profile (billions, 2030-39)
YEARS = {r["id"]: [num(r[f"y{y}"]) for y in range(2030, 2040)] for r in read("fiscal-years.csv")}

# An aggregate bill can contain different permanent/growth paths. Amounts are
# disjoint ledger shares, not additional rows of spending.
COMPONENTS = {}
for r in read("fiscal-components.csv"):
    p={"cat":r["cat"], "start":num(r["start"]), "ramp":num(r["ramp"]),
       "grow":r["grow"], "perm":num(r["perm"]), "basis":r["basis"]}
    COMPONENTS.setdefault(r["owner"],[]).append((r["component"],num(r["mid10"]),p))
