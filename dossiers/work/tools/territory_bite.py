#!/usr/bin/env python3
"""The wage floor's bite in the territories and in low-wage state areas, 2030-36.

Role: the bite tables for LAB-4.10, revised for Espen's November 18 answer W9
(DEC-2026-11-18-09: the national schedule everywhere, slower where an abrupt rise is
dangerous; slow_floor) (`dossiers/work/5-delivery.md`, part 5;
`dossiers/work/4-specification.md`, LAB-4.10; question 2 in `3-design.md`). Status:
draft (stage F, the milestone review's fix step 2). Project arithmetic, not a forecast.
Run:  python3 dossiers/work/tools/territory_bite.py           (tables in Markdown)
      python3 dossiers/work/tools/territory_bite.py --check   (spot checks)

Method (the dossier's own, memo 1 "How far each target reaches"): the bite is the floor
divided by the local median hourly wage. Each median is grown from its latest published
year at a working assumption of 3.5% a year (range 3-4%; judgment), the rate memo 1 uses
for the national median, by whole years from the data year (as memo 1 grows May 2025's
$24.51 to about $34.6 in 2035). Puerto Rico's OEWS median grew about 4.5% a year from
May 2019 to May 2023 ($10.13 to $12.09) against 4.8% nationally ($19.14 to $23.11), so
the territories' medians are grown at the national rate (EV-WRK-464, 455, 465, 461). The floor is
the LAB-4.01 step in force on January 1 of the year; from 2036 it rises with the national
median (LAB-4.02).

Medians (all jobs, part-time included):
  national          $23.11  May 2023 OEWS   EV-WRK-461  (memo 1 uses May 2025's $24.51,
                                                         EV-WRK-078; both are shown)
  Puerto Rico       $12.09  May 2023 OEWS   EV-WRK-455
  San Juan metro    $12.74  May 2023 OEWS   EV-WRK-456
  PR nonmetro       $11.42  May 2023 OEWS   EV-WRK-457  (20,480 jobs only)
  Guam              $16.02  May 2023 OEWS   EV-WRK-458
  Virgin Islands    $19.42  May 2023 OEWS   EV-WRK-459
  N. Mariana Is.     $9.97  Feb 2021 CNMI Prevailing Wage Study  EV-WRK-460 (no OEWS)
  Mississippi       $18.03  May 2023 OEWS   EV-WRK-462
  NW Miss. nonmetro $16.50  May 2023 OEWS   EV-WRK-463
American Samoa has no published median (BLS does not survey it); its industry minimums
include $5.78 (garment) and $6.36 (fish canning) from September 30, 2024 (EV-WRK-467, 474), so
no bite is computed.
"""
import sys

STEPS = {2030: 9.50, 2031: 11.00, 2032: 12.50, 2033: 14.00, 2034: 15.50, 2035: 17.00}
G, G_LO, G_HI = 0.035, 0.03, 0.04

AREAS = [  # name, median, data year
    ("United States", 23.11, 2023),
    ("Puerto Rico", 12.09, 2023),
    ("San Juan metro area", 12.74, 2023),
    ("Puerto Rico nonmetro area", 11.42, 2023),
    ("Guam", 16.02, 2023),
    ("U.S. Virgin Islands", 19.42, 2023),
    ("Northern Mariana Islands", 9.97, 2021),
    ("Mississippi", 18.03, 2023),
    ("Northwest Mississippi nonmetro area", 16.50, 2023),
]
YEARS = list(range(2030, 2037))
CAP = 0.75  # the danger line: the floor at most 75% of the local median in a year
SLOW_STEP = 1.00  # the slower path's minimum rise a year (Espen's W9, DEC-2026-11-18-09)


def median(m0, y0, y, g=G):
    return m0 * (1 + g) ** (y - y0)


def national_floor(y, g=G):
    """LAB-4.01's step, then LAB-4.02's indexing to the national median (rounded up to $0.05)."""
    if y <= 2035:
        return STEPS[y]
    f = STEPS[2035]
    for _ in range(2036, y + 1):
        f = -(-round(f * (1 + g) * 100) // 5) * 5 / 100  # up to the next $0.05
    return f


def capped_floor(m0, y0, y, g=G, cap=CAP):
    """Option B: the national floor, but no more than `cap` of the latest local median,
    rounded down to $0.05, never below the first step's $9.50 once it is in force.
    The median used for January of year y is the one published the spring before
    (data year y-1), grown here at g."""
    nat = national_floor(y, g)
    c = int(cap * median(m0, y0, y - 1, g) * 20) / 20
    return min(nat, max(c, STEPS[2030]))


def slow_floor(m0, y0, y, g=G, cap=CAP, step=SLOW_STEP):
    """The national schedule everywhere, slower where the bite is high (W9's draft): each
    January the jurisdiction's rate is the national rate, unless that is above `cap` of
    the local median published the spring before; then it is the larger of last year's
    rate plus a rise (`step`, or from 2036 the national rate's own rise plus $0.25 if that is
    more, so the gap always closes) and `cap` of that median (rounded down to $0.05), never above the
    national rate. Once back on the national rate it stays there. Every jurisdiction joins; the rule names no
    territory, so it reads the same after a territory becomes a state."""
    rate, slowed = 7.25, False
    for yy in range(2030, y + 1):
        nat = national_floor(yy, g)
        c = int(cap * median(m0, y0, yy - 1, g) * 20) / 20
        if nat <= c or (slowed and rate >= national_floor(yy - 1, g) - 1e-9):
            rate = nat  # on the national schedule, and once back on it, it stays
        else:
            rise = max(step, nat - national_floor(yy - 1, g) + 0.25) if yy > 2035 else step
            slowed, rate = True, min(nat, max(rate + rise, c))
    return rate


def join_year(m0, y0, g=G, end=2060):
    """The first year the slower path is back at the national rate (None if never slower)."""
    below = [y for y in range(2030, end) if slow_floor(m0, y0, y, g) < national_floor(y, g) - 1e-9]
    return max(below) + 1 if below else None


def table(fn, label, g=G):
    rows = [f"| Area | {' | '.join(str(y) for y in YEARS)} |",
            "| --- |" + " --- |" * len(YEARS)]
    for name, m0, y0 in AREAS:
        cells = []
        for y in YEARS:
            f = fn(m0, y0, y, g)
            cells.append(f"{100 * f / median(m0, y0, y, g):.0f}%")
        rows.append(f"| {name} | {' | '.join(cells)} |")
    return f"**{label}**\n\n" + "\n".join(rows)


def main():
    if "--check" in sys.argv:
        # memo 1's anchor: $24.51 (May 2025) grown to 2035 is about $34.6
        assert abs(median(24.51, 2025, 2035) - 34.57) < 0.05
        # the review's figure: $17 is near Puerto Rico's whole median in 2035
        assert 0.90 < 17 / median(12.09, 2023, 2035) < 0.95
        assert national_floor(2036) == 17.60  # LAB-4.02's "about $17.60 in 2036"
        assert slow_floor(16.02, 2023, 2035) == 17.00  # Guam: the national schedule
        assert slow_floor(12.09, 2023, 2035) < 17.00   # Puerto Rico: slower
        assert slow_floor(12.09, 2023, 2045) == national_floor(2045)  # ... and joins
        print("territory_bite: checks pass")
        return
    nat = lambda m0, y0, y, g: national_floor(y, g)
    print("Floor, national schedule:", ", ".join(f"{y} ${national_floor(y):.2f}" for y in YEARS))
    print()
    print(table(nat, "Option A: the national schedule (LAB-4.01, 4.02), bite at 3.5% growth"))
    for g in (G_LO, G_HI):
        print()
        print(table(nat, f"Option A at {g:.0%} median growth", g))
    print()
    print("**Option B: the national schedule capped at 75% of the territory's median**\n")
    print(f"| Territory | {' | '.join(str(y) for y in YEARS)} |")
    print("| --- |" + " --- |" * len(YEARS))
    for name, m0, y0 in AREAS[1:2] + AREAS[4:7]:
        cells = [f"${capped_floor(m0, y0, y):.2f} ({100 * capped_floor(m0, y0, y) / median(m0, y0, y):.0f}%)"
                 for y in YEARS]
        print(f"| {name} | {' | '.join(cells)} |")
    print()
    print("**Drafted (W9): the national schedule everywhere, slower where the bite would pass 75%**\n")
    yrs = YEARS + [2038, 2040]
    print(f"| Area | {' | '.join(str(y) for y in yrs)} | Joins the national rate |")
    print("| --- |" + " --- |" * (len(yrs) + 1))
    for name, m0, y0 in AREAS[1:2] + AREAS[4:7] + AREAS[7:8]:
        cells = [f"${slow_floor(m0, y0, y):.2f} ({100 * slow_floor(m0, y0, y) / median(m0, y0, y):.0f}%)"
                 for y in yrs]
        j = join_year(m0, y0)
        print(f"| {name} | {' | '.join(cells)} | {j or 'never slower'} |")
    print()
    for g in (G_LO, G_HI):
        print(f"At {g:.0%} growth: Puerto Rico joins in {join_year(12.09, 2023, g)}, "
              f"the Northern Mariana Islands in {join_year(9.97, 2021, g)}")
    print()
    print("Option B at 3% and 4% growth, Puerto Rico, 2035:",
          ", ".join(f"{g:.0%}: ${capped_floor(12.09, 2023, 2035, g):.2f}" for g in (G_LO, G_HI)))


if __name__ == "__main__":
    main()
