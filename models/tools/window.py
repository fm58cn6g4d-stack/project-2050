"""Window rescaler: moves a ten-year (or any multi-year) total from one budget window to another.

A figure scored for 2025-34 is not the same money in 2030-39: the economy and the tax base are larger. This
scales by the ratio of the growth index summed over each window, from CBO's February 2026 path in
models/data/fiscal-baseline.csv. The index is nominal GDP by default; a baseline category (rev_individual,
rev_corporate, out_medicare_net ...) tracks that base instead. The result is a scaled figure, not a score.

    python3 models/tools/window.py 272 2025-34                 # $272B over 2025-34, in 2030-39 terms
    python3 models/tools/window.py 1.4 2026-35 --index rev_individual
    python3 models/tools/window.py 557 2022-31 --to 2030-39
"""
import csv, os, sys

def _baseline():
    here = os.path.dirname(os.path.abspath(__file__))
    for p in (os.path.join(here, "..", "data", "fiscal-baseline.csv"), os.path.join(here, "..", "models", "data", "fiscal-baseline.csv"),
              "fiscal-baseline.csv"):
        if os.path.exists(p):
            with open(p, newline="") as f:
                return {int(r["year"]): r for r in csv.DictReader(f)}
    raise FileNotFoundError("models/data/fiscal-baseline.csv")
BASE = None

def window(s):
    """'2025-34' or (2025, 2034) -> (2025, 2034)."""
    if isinstance(s, tuple): return s
    a, b = s.replace("FY", "").split("-")
    a = int(a); b = int(b) if len(b) == 4 else int(str(a)[:4 - len(b)] + b)
    return a, b

def total(index, w):
    global BASE
    BASE = BASE or _baseline()
    a, b = window(w)
    return sum(float(BASE[y][index]) for y in range(a, b + 1))

def rescale(amount, frm, to="2030-39", index="gdp"):
    """amount over window frm, expressed over window to, by the ratio of the index's sums."""
    return amount * total(index, to) / total(index, frm)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2 or args[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    amt, frm = float(args[0]), args[1]
    to = args[args.index("--to") + 1] if "--to" in args else "2030-39"
    ix = args[args.index("--index") + 1] if "--index" in args else "gdp"
    r = rescale(amt, frm, to, ix)
    print(f"{amt:g} over {frm} = {r:.4g} over {to} (x{r / amt:.3f}, by {ix})")
