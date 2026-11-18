"""The wage floor meets income support: how much of memo 1 B's raise a typical family keeps.

Role: section 7's household test of the wage floor (LAB-4.01) against the plan's income support
(`dossiers/work/7-validation.md`, part 1B). Status: draft (stage F). It answers the question sections 1 and 2 left
for the household model (`1-problem.md`, A.6; `2-what-works.md`, A.4): of each dollar the floor adds to a family's
pay, how much is left after payroll tax, income tax and credits, SNAP and (in 2030-34) the premium credit, under the
January 2029 law and under the plan's decided layers.

It reuses the household model's typical-family calculator (`models/tools/household/families.py`: `budget` for the
2029 law, `plan_budget` for every plan layer the 65-cent check uses: FAM-1's child benefit, INC-1.01, INC-2 and
INC-2.02's 45% earnings deduction, paid leave's worker share and, in 2030-34, the premium credit). It changes nothing
in that model and writes no file.

Conventions (working assumptions, labeled):
  * Dollars are 2029 dollars, the calculator's year. The floor's $17.00 on January 1, 2035 is deflated with the
    model's own price path (CBO, February 2026; `params.price_factor`): $17.00 in 2035 is about $14.87 in 2029
    dollars. Without the act, a worker held at the federal $7.25 is at about $6.34 in 2029 dollars by 2035, since
    $7.25 is not indexed.
  * Hours: full time is 2,080 a year; half time 1,040. Hours are held fixed: no job or hours loss here (part 5's
    objection, "jobs", takes the range of evidence). A worker who loses the job altogether is shown at zero earnings.
  * Starting wages: a worker at the federal floor in one of the 20 states where it binds (`1-problem.md`, A.2), and a
    worker at $12.00 an hour in 2029 dollars in a state with its own indexed floor, who gains less.
  * The plan's single plan (HLT-7) ends Medicaid's and the marketplace's cliffs from 2035; at 2029 law those cliffs
    are reported apart (`families.cliffs`), not inside the rates.
Run: `python3 dossiers/work/tools/floor_household.py` (add `--md` for the tables in 7-validation.md's form).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "models", "tools", "household"))

import families as F  # noqa: E402
from params import law, price_factor  # noqa: E402

DEFLATE_2035 = price_factor(2035) / price_factor(2029)   # 2035 prices in 2029 dollars
FLOOR_2035 = 17.00 / DEFLATE_2035                         # LAB-4.01's last step, in 2029 dollars
HELD_725 = 7.25 / DEFLATE_2035                            # the federal floor without the act, 2035, 2029 dollars
START = {"at the federal $7.25": HELD_725, "at $12.00 in an indexing state": 12.00}
HOURS = {"full time": 2080, "half time": 1040}
SHELTER = 1400 * 1.107                                    # the ceiling check's $1,400 rent, 2029 dollars

CASES = [
    ("2029 law", lambda f, e: F.budget(f, e, 2029)),
    ("2029 law, with the rent", lambda f, e: F.budget(f, e, 2029, shelter=SHELTER)),
    ("the plan, 2035 on", lambda f, e: F.plan_budget(f, e, period="2035")),
    ("the plan, 2035 on, with the rent", lambda f, e: F.plan_budget(f, e, period="2035", shelter=SHELTER)),
]
# 2030-34, at the third step ($12.50 in 2032), on the marketplace: the premium credit still phases out
STEP_2032 = 12.50 / (price_factor(2032) / price_factor(2029))
HELD_2032 = 7.25 / (price_factor(2032) / price_factor(2029))


def kept(fn, f, w0, w1, hours):
    a, b = fn(f, w0 * hours), fn(f, w1 * hours)
    raise_ = (w1 - w0) * hours
    return {"raise": raise_, "net0": a["net"], "net1": b["net"], "gain": b["net"] - a["net"],
            "share": (b["net"] - a["net"]) / raise_,
            "layers": {k: (b[k] - a[k]) for k in ("payroll", "income_tax", "snap", "ptc_contribution")}}


def run():
    out = []
    for fk, f in F.FAMILIES.items():
        for sk, w0 in START.items():
            for hk, h in HOURS.items():
                row = {"family": f["label"], "start": sk, "hours": hk, "w0": w0, "w1": FLOOR_2035}
                for ck, fn in CASES:
                    row[ck] = kept(fn, f, w0, FLOOR_2035, h)
                out.append(row)
    return out


def marketplace_2032():
    """The third step in 2032 for a family on the marketplace, plan layers 2030-34, against 2029 law."""
    res = []
    for fk, f in F.FAMILIES.items():
        for hk, h in HOURS.items():
            law_ = kept(lambda f_, e: F.budget(f_, e, 2029, marketplace=True), f, HELD_2032, STEP_2032, h)
            plan = kept(lambda f_, e: F.plan_budget(f_, e, period="2030-34", marketplace=True), f, HELD_2032,
                        STEP_2032, h)
            res.append((f["label"], hk, law_, plan))
    return res


def job_loss():
    """Net resources at zero earnings, and at half time at the new floor, 2029 law against the plan (2035 on)."""
    res = []
    for fk, f in F.FAMILIES.items():
        z_law, z_plan = F.budget(f, 0, 2029)["net"], F.plan_budget(f, 0, period="2035")["net"]
        ft_law = F.budget(f, FLOOR_2035 * 2080, 2029)["net"]
        ft_plan = F.plan_budget(f, FLOOR_2035 * 2080, period="2035")["net"]
        res.append((f["label"], z_law, z_plan, ft_law, ft_plan))
    return res


def poverty_share(f, net):
    """Net resources as a share of the 2029 federal poverty guideline for the family's size (a reference line only:
    the SPM threshold differs, and the plan's in-kind help, child care and health care, is not in `net`)."""
    L = law(2029)
    return net / F.fpl(L, f["size"])


def main():
    md = "--md" in sys.argv
    print(f"Floor in 2035, 2029 dollars: ${FLOOR_2035:.2f}; $7.25 held to 2035: ${HELD_725:.2f}; "
          f"2032 step ${STEP_2032:.2f} against ${HELD_2032:.2f}")
    rows = run()
    keys = [c for c, _ in CASES]
    if md:
        print("| Family | Starting wage | Hours | Raise a year | " + " | ".join(f"Kept: {k}" for k in keys) + " |")
        print("| --- | --- | --- | --- | " + " | ".join("---" for _ in keys) + " |")
    for r in rows:
        cells = [f"${r[k]['gain']:,.0f} ({100 * r[k]['share']:.0f}%)" for k in keys]
        if md:
            print(f"| {r['family']} | {r['start']} | {r['hours']} | ${r[keys[0]]['raise']:,.0f} | "
                  + " | ".join(cells) + " |")
        else:
            print(r["family"], "|", r["start"], "|", r["hours"], "| raise", round(r[keys[0]]["raise"]), "|",
                  " | ".join(f"{k}: {c}" for k, c in zip(keys, cells)))
            for k in keys:
                print("    ", k, {x: round(v) for x, v in r[k]["layers"].items()})
    print()
    print("2030-34 on the marketplace, the third step ($12.50 in 2032) against $7.25 held:")
    for lab, hk, a, b in marketplace_2032():
        print(f"  {lab}, {hk}: raise ${a['raise']:,.0f}; 2029 law keeps ${a['gain']:,.0f} ({100 * a['share']:.0f}%),"
              f" the plan keeps ${b['gain']:,.0f} ({100 * b['share']:.0f}%); premium layer law "
              f"{a['layers']['ptc_contribution']:,.0f}, plan {b['layers']['ptc_contribution']:,.0f}")
    print()
    print("Net resources (cash, after tax and SNAP), full time at the floor and with no job:")
    for (lab, z_law, z_plan, ft_law, ft_plan), f in zip(job_loss(), F.FAMILIES.values()):
        print(f"  {lab}: no job, 2029 law ${z_law:,.0f} ({100 * poverty_share(f, z_law):.0f}% of the guideline),"
              f" the plan ${z_plan:,.0f} ({100 * poverty_share(f, z_plan):.0f}%); full time at the floor, 2029 law"
              f" ${ft_law:,.0f} ({100 * poverty_share(f, ft_law):.0f}%), the plan ${ft_plan:,.0f}"
              f" ({100 * poverty_share(f, ft_plan):.0f}%)")
    print()
    print("Cliffs outside the rates at 2029 law:", "; ".join(f"{a} at {b}" for a, b in F.cliffs()))
    L = law(2029)
    for f in F.FAMILIES.values():
        e = FLOOR_2035 * 2080
        print(f"  {f['label']}: full time at the floor earns ${e:,.0f}, {100 * e / F.fpl(L, f['size']):.0f}% of "
              f"the 2029 guideline")


if __name__ == "__main__":
    main()
