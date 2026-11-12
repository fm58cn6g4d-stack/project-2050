#!/usr/bin/env python3
"""The decided child benefit (FAM-1D, DEC-2026-11-12-06) against the 2029 law, by tax year.

Role: secure floor section 6's pricing of what Espen's November 12 decision changed in
memo 1 A: the American Family Act **without** today's $2,200 credit as a floor, so the
bill's own phase-out applies (H.R. 2763 sec. 24A(b)(2): 5% above $150,000 joint or
$112,500 other, down to $166.67 a month a child, and 5% again above $400,000 joint or
$300,000 other). Status: draft (board row S4). A static, annual-exposure analogue on the
official CPS ASEC 2026 public-use file (income year 2025), built on the legacy
child-poverty tool's reader (`models/tools/child-poverty/agenda_analysis.py`); not a
score, no behavior, full take-up. Raw data stay outside the repository.

It reports, for tax years 2030-2040:
  * the floor's value: what the decided design pays less than the 2029 law's $2,200
    indexed credit, summed over the families who would get less (these families lose
    against the 2029 law; the floor would have held them harmless);
  * children in those families;
  * the gross annual cost of the design against the source-year credits (a check
    against the Tax Policy Center's $1.4 trillion over FY2026-35, EV-SEC-266);
  * the value of the $500 credit for other dependents (sec. 24(h)(4)), which the bill's
    termination of section 24 would end (H.R. 2763 sec. 2(c)).

Working assumptions (labeled, DEC-2026-11-10-07):
  * prices: CBO's CPI-U path to 2036 (`models/data/budget/cbo-economic.csv`), then 2.3%
    a year (judgment);
  * real AGI growth: 1.0% a year from 2025 for every tax unit (judgment, range 0.5-1.5%),
    so more families cross the unindexed $400,000 line and the $166.67 base erodes;
  * the child population is held at the source year's (the budget model's FAM-1 profile
    holds it "roughly flat").

Run: python3 dossiers/secure-floor/tools/afa_floor.py --archive /path/to/asecpub26csv.zip
"""
import argparse
import csv
import io
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'models/tools/child-poverty'))
from agenda_analysis import parse_archive  # noqa: E402

YEARS = range(2030, 2041)
REAL_GROWTH = 0.010
LATE_CPI = 0.023


def cpi_path():
    with open(ROOT / 'models/data/budget/cbo-economic.csv') as f:
        cpi = {int(r['year']): float(r['cpiu']) for r in csv.DictReader(f)}
    for y in range(max(cpi) + 1, 2042):
        cpi[y] = cpi[y - 1] * (1 + LATE_CPI)
    return cpi


def law_credit(n, agi, filing, idx_2024):
    """2029 law: $2,200 a child indexed after 2025 on the prior year's CPI over 2024's,
    rounded down to $100; $400,000 or $200,000 unindexed, $50 per $1,000. Used for
    families above $100,000 only, where the earnings phase-in does not bind."""
    per_child = 2200 + (int(2200 * (idx_2024 - 1) / 100) * 100 if idx_2024 > 1 else 0)
    line = 400000 if filing == 'joint' else 200000
    over = max(0, agi - line)
    return max(0, n * per_child - 50 * -(-over // 1000))


def afa_credit(ages, agi, filing, idx_2024, idx_2022):
    """H.R. 2763, annual exposure: $300 (6-17) and $360 (under 6) a month indexed from 2024;
    the 800% newborn month is left out (it matters below the lines, not here). Initial
    threshold indexed from 2022 (rounded to $5,000); base $166.67 and secondary threshold
    unindexed."""
    monthly = 300 + round(300 * (idx_2024 - 1) / 10) * 10
    gross = sum(12 * monthly * (1.2 if a < 6 else 1.0) for a in ages)
    first = (150000 if filing == 'joint' else 112500)
    first += round(first * (idx_2022 - 1) / 5000) * 5000
    second = 400000 if filing == 'joint' else 300000
    base = 12 * 166.67 * len(ages)
    cut = min(max(0, gross - base), 0.05 * max(0, second - first), 0.05 * max(0, agi - first))
    return max(0, gross - cut - 0.05 * max(0, agi - second))


def adult_dependents(archive):
    """Weighted adults claimed as dependents (DEP_STAT points to a claimant)."""
    total = 0.0
    with zipfile.ZipFile(archive) as z, z.open('pppub26.csv') as f:
        for r in csv.DictReader(io.TextIOWrapper(f)):
            if int(r['A_AGE']) >= 18 and int(r['DEP_STAT']) > 0:
                total += float(r['MARSUPWT']) / 100
    return total


def run(archive):
    data = parse_archive(archive)
    cpi = cpi_path()
    cpi[2022] = cpi[2023] * 292.655 / 304.702  # BLS annual CPI-U 2022 and 2023, on CBO's 2023 level
    units = []
    for uid, taxes in data['taxes_by_unit'].items():
        w = data['units'][uid]['weight']
        for t in taxes:
            u = data['units'][uid]
            units.append((w, t['child_ages'], t['agi'], t['filing'], t['nonrefundable'] + t['refundable'],
                          u['SPM_RESOURCES'] < u['SPM_POVTHRESHOLD']))
    children = sum(w * len(a) for w, a, *_ in units)
    i24, i22 = cpi[2024] / cpi[2024], cpi[2024] / cpi[2022]  # tax year 2025 uses 2024's CPI
    gross_2025 = sum(w * (afa_credit(a, agi, f, i24, i22) - base) for w, a, agi, f, base, _ in units)
    # SPM-poor children in families the decided design pays less than the 2029 law
    # (source year, 2025 dollars): if this is about zero, declining the floor leaves poverty unchanged.
    poor_losing = sum(w * len(a) for w, a, agi, f, _, poor in units if poor and agi >= 100000
                      and law_credit(len(a), agi, f, 1.0) > afa_credit(a, agi, f, i24, i22))
    adults = adult_dependents(archive)
    rows = []
    for y in YEARS:
        i24, i22 = cpi[y - 1] / cpi[2024], cpi[y - 1] / cpi[2022]  # prior year's CPI
        grow = (1 + REAL_GROWTH) ** (y - 2025) * cpi[y] / cpi[2025]
        floor, kids, families = 0.0, 0.0, 0.0
        for w, ages, agi, filing, _, _ in units:
            nominal_agi = agi * grow
            if nominal_agi < 100000:
                continue
            gap = law_credit(len(ages), nominal_agi, filing, i24) - afa_credit(ages, nominal_agi, filing, i24, i22)
            if gap > 0:
                floor += w * gap
                kids += w * len(ages)
                families += w
        rows.append(dict(tax_year=y, floor_value_bn=round(floor / 1e9, 2),
                         children_below_2029_law_m=round(kids / 1e6, 2),
                         families_below_2029_law_m=round(families / 1e6, 2),
                         other_dependent_credit_bn=round(adults * 500 / 1e9, 2)))
    return dict(source='CPS ASEC 2026 public use (income year 2025), official Census archive',
                children_claimed_m=round(children / 1e6, 2),
                gross_cost_2025_dollars_full_takeup_bn=round(gross_2025 / 1e9, 1),
                adults_claimed_as_dependents_m=round(adults / 1e6, 2),
                poor_children_in_families_below_2029_law_source_year=round(poor_losing),
                assumptions=dict(real_agi_growth=REAL_GROWTH, cpi_after_2036=LATE_CPI),
                tax_years=rows)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    p.add_argument('--archive', type=Path, required=True)
    print(json.dumps(run(p.parse_args().archive), indent=1))
