"""Reads the hand-entered input tables in models/data/inputs/ (CSV, one row per line, opens in any spreadsheet).
The scripts in models/tools/ load their tables through this module; run-all.sh copies it into build/ with them."""
import csv, os, re
from decimal import Decimal, ROUND_HALF_UP
HERE = os.path.dirname(os.path.abspath(__file__))

def path(name):
    """models/data/inputs/<name>, found from models/tools/ or from build/ (where run-all.sh runs the copies)."""
    for d in (os.environ.get("P2050_INPUTS"), os.path.join(HERE, "..", "data", "inputs"), os.path.join(HERE, "..", "models", "data", "inputs")):
        if d and os.path.exists(os.path.join(d, name)): return os.path.normpath(os.path.join(d, name))
    raise FileNotFoundError(f"models/data/inputs/{name}")

def read(name):
    with open(path(name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def num(s):
    """A number as typed: 2 stays an integer, 2.0 a decimal (the generated files print them differently)."""
    s = s.strip()
    return int(s) if re.fullmatch(r"-?\d+", s) else float(s)

def flag(s):
    return {"yes": True, "no": False}[s.strip().lower()]

def opt(row, key, conv=str):
    """A blank cell means 'not set' (the script's default applies)."""
    v = row.get(key, "").strip()
    return None if v == "" else conv(v)


def money_sum(values, places=2):
    """Sum decimal input amounts and round once, half away from zero for display.

    Binary summation around a half-cent can vary with interpreter summation
    algorithms. This is presentation precision, not a change to policy inputs.
    """
    total = sum((Decimal(str(v)) for v in values), Decimal(0))
    return float(total.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP))
