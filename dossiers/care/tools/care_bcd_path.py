#!/usr/bin/env python3
"""Fiscal-year path for care parts B-D as decided (`DEC-2026-11-11-02` to `-06`), for section 6
(`dossiers/care/6bcd-cost.md`).

Not a model and not an official score. It takes the decided pieces from `care_repricing.py` (part B,
memo 17's options, the state shares) and the calendar or program-year figures sections 3b, 3c and 3d give,
lays each on a year-by-year path, and converts to federal fiscal years. Judgment is labeled. Run:

    python3 dossiers/care/tools/care_bcd_path.py

Conventions:
- Nominal $ billion, federal cost, against current law; a cost is positive.
- Calendar-year lines become fiscal years as health's path does (`health_path.py`): FY y takes a quarter of
  calendar year y-1 and three quarters of calendar year y (FY2035 starts October 2034).
- Medicaid match lines (the bridge) are already fiscal-year amounts: the points apply from FY2030.
- Child care and pre-K run on school or program years that start in the fall (2030-31 is the first). A
  program year starting in the fall of y falls almost entirely in FY y+1, so it is counted there.
- Readings are (low, central, high), pairing each piece's low and high, as the part files do.
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('care_repricing', HERE / 'care_repricing.py')
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

G = R.GROWTH
CY = range(2029, 2041)
FY = range(2030, 2041)
WINDOW = range(2030, 2040)


def three(f):
    return tuple(f(i) for i in range(3))


def fy_from_cy(cy):
    return {y: 0.25 * cy.get(y - 1, 0.0) + 0.75 * cy.get(y, 0.0) for y in FY}


def fy_from_py(py):
    return {y: py.get(y - 1, 0.0) for y in FY}


# ---------------- Part B ----------------
users3 = three(lambda i: R.NEW_USERS_2ADL[i] * R.RETAINED[i])
cost3 = three(lambda i: R.COST_EACH_2ADL[i] * R.COST_LIFT[i])
newb = three(lambda i: users3[i] * cost3[i] / 1e9)                         # new-user line, 2035
first6b = three(lambda i: (R.RELIEF_2035[i] + R.RICHER_2035[i]) / 1e9 + newb[i])


def part_b(i):
    lines = {k: {} for k in ('bridge', 'memo6b', 'below_line', 'opt2', 'opt4', 'memo8c', 'opt5', 'state_option')}
    bridge_share = (0.6, 1.0, 1.0)[i]   # low: entry points only (6 of 10); central and high: up to 10
    for y in range(2030, 2035):          # fiscal years (Medicaid match)
        lines['bridge'][y] = 24.0 * G ** (y - 2030) * bridge_share
    for y in range(2035, 2041):          # calendar years from January 1, 2035
        t = y - 2035
        lines['memo6b'][y] = first6b[i] * G ** t
        lines['below_line'][y] = -R.medicaid_home(y) * R.ramp(y, R.ATTRITION_2040[i]) / 1e9
        lines['opt2'][y] = -0.07 * (R.RICHER_2035[i] / 1e9 + newb[i]) * G ** t
        lines['opt4'][y] = -newb[i] * {0: 0.5, 1: 0.2 * G}.get(t, 0.0)
        lines['memo8c'][y] = R.MEMO8C_2035[i] / 1e9 * G ** t
        lines['opt5'][y] = -8.0 * G ** t
        lines['state_option'][y] = -lines['below_line'][y] * R.FMAP_REGULAR
    return lines


# Small part B items the decided total leaves out (judgment; 3b points 2-4 and 6)
def part_b_small():
    out = {}
    for y in range(2030, 2041):
        v = 0.3                                      # point 3, no estate recovery: under $0.5B a year
        if y <= 2034:
            v += 0.45 + 4.0 + 0.1                    # point 2 MFP $0.45B; point 4 limits $2-6B; point 6 demo
        out[y] = v
    return out                                       # fiscal-year basis (Medicaid)


# ---------------- Part C (program years) ----------------
CC90 = {2030: 20.0, 2031: 45.0, 2032: 65.0, 2033: 85.0}     # 3c: $20B in 2030, $85B at maturity (2033)
r_cc = (110.0 / 85.0) ** (1 / 6)                              # to 3c's $110B in FY2040 (program year 2039)
for py in range(2034, 2041):
    CC90[py] = 85.0 * r_cc ** (py - 2033)
PREK = {2030: 10.0, 2031: 30.0, 2032: 46.0, 2033: 60.0}       # 3c: about $60B at maturity; 3s everywhere 2033-34
r_pk = (80.0 / 60.0) ** (1 / 6)                               # to 3c's $80B in FY2040
for py in range(2034, 2041):
    PREK[py] = 60.0 * r_pk ** (py - 2033)
FACILITIES = {py: 5.0 for py in range(2030, 2035)}            # 3c point 7


def part_c(i):
    scale = (0.62, 1.0, 1.5)[i]          # 3c's range: about $0.85-2.0T on $1.32T
    cut = {py: -10.0 * G ** (py - 2033) for py in range(2033, 2041)}   # 80% from the fourth year (2033-34)
    # Labor grown with wages, not prices (3d, "What is and isn't counted"): about two-thirds of child care
    # cost is labor; care wages assumed to run about 1% a year above prices from 2030 (judgment).
    wage = {py: (CC90[py] + cut.get(py, 0.0)) * (2 / 3) * (1.01 ** (py - 2030) - 1) for py in CC90}
    return {'child_care': {k: v * scale for k, v in CC90.items()},
            'state_share_cut': {k: v * scale for k, v in cut.items()},
            'pre_k': {k: v * scale for k, v in PREK.items()},
            'facilities': dict(FACILITIES),
            'wage_growth_fix': {k: v * scale for k, v in wage.items()}}


# ---------------- Part D ----------------
def part_d(i):
    lift = R.FLOOR_LIFT[i]
    floor_bridge = {y: R.medicaid_home(y) * R.LABOR_SHARE * lift * (R.FMAP_REGULAR + R.BRIDGE_POINTS) / 1e9
                    for y in range(2030, 2035)}                                   # calendar years
    base35 = (R.medicaid_home(2035) + R.RICHER_2035[i] + users3[i] * cost3[i]) / 1e9
    floor_plan = {y: (base35 * R.LABOR_SHARE * lift + R.NURSING_HOMES_2035 / 1e9) * G ** (y - 2035)
                  for y in range(2035, 2041)}
    # memo 17 option 4 delays some new users' hours, so the floor on those hours is delayed too (not in #250)
    floor_opt4 = {2035: -newb[i] * 0.5 * R.LABOR_SHARE * lift, 2036: -newb[i] * 0.2 * G * R.LABOR_SHARE * lift}
    # memo 15 B on program years, at 90% federal, then the child care share (80%) from 2033-34.
    # Anchors (judgment, from memo 15 and 3d): the floor alone about $10B a year at maturity, scaled by the
    # program's size before then; about $25B in 2033; parity (option A's level, $45B in 2032-33 growing to
    # $60B in FY2040 at 90%) reached in the 2036-37 school year.
    a_level = lambda py: 45.0 * (60.0 / 45.0) ** ((py - 2033) / 7)
    p90 = {2030: 10.0 * 20 / 85, 2031: 10.0 * 45 / 85, 2032: 15.0, 2033: 25.0}
    for k, py in enumerate((2034, 2035, 2036)):
        p90[py] = 25.0 + (a_level(2036) - 25.0) * (k + 1) / 3
    for py in range(2037, 2041):
        p90[py] = a_level(py)
    pscale = (0.6, 1.0, 1.4)[i]          # memo 15's range, $15-35B on $25B in 2033
    parity = {py: v * pscale * (0.8 / 0.9 if py >= 2033 else 1.0) for py, v in p90.items()}
    staffing = {y: 1.5 for y in range(2031, 2035)}                                 # memo 16 C, calendar
    for y in range(2035, 2041):
        staffing[y] = 6.0 * (7.0 / 6.0) ** ((y - 2035) / 5)
    points = {y: 2.0 for y in range(2030, 2041)}                                  # points 5 and 7
    return {'floor_bridge': floor_bridge, 'floor_plan': floor_plan, 'floor_opt4': floor_opt4,
            'parity_py': parity, 'staffing': staffing, 'points': points}


def fy_lines(i):
    b, c, d = part_b(i), part_c(i), part_d(i)
    out = {}
    out['B bridge (point 1)'] = {y: b['bridge'].get(y, 0.0) for y in FY}
    for k in ('memo6b', 'below_line', 'state_option', 'opt2', 'opt4', 'memo8c', 'opt5'):
        out['B ' + k] = fy_from_cy(b[k])
    for k in ('child_care', 'state_share_cut', 'pre_k', 'facilities'):
        out['C ' + k] = fy_from_py(c[k])
    out['D floor, bridge (memo 14)'] = fy_from_cy(d['floor_bridge'])
    out['D floor, plan (memo 14)'] = fy_from_cy(d['floor_plan'])
    out['D parity (memo 15)'] = fy_from_py(d['parity_py'])
    out['D staffing (memo 16)'] = fy_from_cy(d['staffing'])
    out['D points 5 and 7'] = fy_from_cy(d['points'])
    extra = {'B small items (points 2-4, 6)': {y: part_b_small().get(y, 0.0) for y in FY},
             'C wage growth in labor (3d)': fy_from_py(c['wage_growth_fix']),
             'D floor delayed with option 4': fy_from_cy(d['floor_opt4'])}
    return out, extra, (b, c, d)


def tot(series, years=WINDOW):
    return sum(series.get(y, 0.0) for y in years)


def main():
    lines, extra, raw = fy_lines(1)
    print('CARE PARTS B-D AS DECIDED: FEDERAL COST BY FISCAL YEAR ($ billion, central)')
    hdr = ''.join(f'{y:>7}' for y in FY)
    print(f'{"line":36}{hdr}  FY30-39')
    parts = {'B': 0, 'C': 0, 'D': 0}
    part_fy = {p: {y: 0.0 for y in FY} for p in parts}
    for k, s in lines.items():
        print(f'{k:36}' + ''.join(f'{s.get(y, 0):7.1f}' for y in FY) + f'  {tot(s):7.0f}')
        for y in FY:
            part_fy[k[0]][y] += s.get(y, 0.0)
    print()
    for p in 'BCD':
        s = part_fy[p]
        print(f'{"part " + p + ", decided pieces":36}' + ''.join(f'{s[y]:7.1f}' for y in FY) + f'  {tot(s):7.0f}')
    allp = {y: sum(part_fy[p][y] for p in 'BCD') for y in FY}
    print(f'{"ALL THREE, decided pieces":36}' + ''.join(f'{allp[y]:7.1f}' for y in FY) + f'  {tot(allp):7.0f}')
    print()
    print('Corrections and items outside the decided figures (FY basis)')
    for k, s in extra.items():
        print(f'{k:36}' + ''.join(f'{s.get(y, 0):7.1f}' for y in FY) + f'  {tot(s):7.0f}')
    allx = {y: allp[y] + sum(s.get(y, 0.0) for s in extra.values()) for y in FY}
    print(f'{"ALL THREE, with them":36}' + ''.join(f'{allx[y]:7.1f}' for y in FY) + f'  {tot(allx):7.0f}')

    # Calendar-year reading the part files and memo 17 use, rebuilt from the same pieces
    b, c, d = raw
    cy_b = sum(sum(v for y, v in b[k].items() if y <= 2039) for k in b)
    cy_c = sum(sum(v for y, v in c[k].items() if y <= 2039) for k in ('child_care', 'state_share_cut', 'pre_k', 'facilities'))
    cy_d = (sum(d['floor_bridge'].values()) + sum(v for y, v in d['floor_plan'].items() if y <= 2039)
            + sum(v for y, v in d['parity_py'].items() if y <= 2039)
            + sum(v for y, v in d['staffing'].items() if y <= 2039) + sum(v for y, v in d['points'].items() if y <= 2039))
    print()
    print('Calendar or program years 2030-39, the part files\' basis (rebuilt here): '
          f'B {cy_b / 1e3:.2f}T, C {cy_c / 1e3:.2f}T, D {cy_d / 1e3:.2f}T, all {(cy_b + cy_c + cy_d) / 1e3:.2f}T '
          '(decided figures: B 1.90, C 1.32, D 0.58, all 3.80)')

    # Ranges
    print()
    print('Ranges (low, central, high): FY2030-39 $T; FY2040 $B')
    for i, name in enumerate(('low', 'central', 'high')):
        l, x, _ = fy_lines(i)
        s = {y: sum(v.get(y, 0.0) for v in l.values()) for y in FY}
        sx = {y: s[y] + sum(v.get(y, 0.0) for v in x.values()) for y in FY}
        pb = {p: sum(tot(v) for k, v in l.items() if k[0] == p) for p in 'BCD'}
        p40 = {p: sum(v.get(2040, 0) for k, v in l.items() if k[0] == p) for p in 'BCD'}
        print(f'  {name:8} decided pieces {tot(s) / 1e3:.2f}T, {s[2040]:.0f}B | with corrections and items '
              f'{tot(sx) / 1e3:.2f}T, {sx[2040]:.0f}B | by part FY30-39 ' +
              ', '.join(f'{p} {pb[p] / 1e3:.2f}' for p in 'BCD') + ' | FY2040 ' +
              ', '.join(f'{p} {p40[p]:.0f}' for p in 'BCD'))

    # States' share, central (what states pay toward these parts; not federal cost)
    print()
    print("States' payments, central ($B): long-term care maintenance of effort from 2035; the bridge floor's "
          'state share 2030-34; child care and pre-K shares')
    moe35 = R.STATE_LTC_SHARE * (R.medicaid_home(2035) + R.MEDICAID_INST_2023 * G ** 12) * 0.5 / 1e9
    print(f'  long-term care MOE, CY2035 {moe35:.0f}; FY2040 {moe35 * G ** 5:.0f} (indexed with the line)')
    fb = {y: R.medicaid_home(y) * R.LABOR_SHARE * R.FLOOR_LIFT[1] * (1 - R.FMAP_REGULAR - R.BRIDGE_POINTS) / 1e9
          for y in range(2030, 2035)}
    print(f'  bridge floor, states, 2030-34: {sum(fb.values()):.0f} in all')
    print('  child care states (at maturity, 2033): about 20; pre-K states (their 14.4 included): about 34')

    # Netting against what is booked now (no booking here; section 6, part 5 lists the rows a booking changes)
    print()
    net = booked_netting(lines, allp)
    for k, v in net.items():
        print(f'  {k}: FY2030-39 {v[0]:.0f}B; FY2040 {v[1]:.0f}B')


# What the budget model books today for these parts (read from `build/fiscal-model.json` and
# `models/data/recovery-budget.json` after `bash models/tools/run-all.sh` at commit aa6b250; $ billion, FY2030-40).
HLT4_BOOKED = [17.6, 37.1, 56.9, 56.1, 54.0, 51.7, 52.8, 54.9, 57.2, 59.7, 62.3]       # the whole HLT-4 row
HLT4_YEAR_SHAPED = [0.95 + 2.85, 0.65 + 7.84, 12.25, 9.58, 5.54, 1.16, 0, 0, 0, 0, 0]   # fiscal-years.csv rows 11-12
LTC_SHARE = 0.3194 / (0.3194 + 0.1378)        # long-term care's share of HLT-4's two profile components
EDU_CARE = [12.0, 23.3, 45.3, 88.0, 93.6, 99.6, 106.0, 106.0, 106.0, 106.0, 106.0]       # EDU-9B fund, care component


def booked_netting(lines, allp):
    yrs = list(FY)
    ltc = {y: (HLT4_BOOKED[k] - HLT4_YEAR_SHAPED[k]) * LTC_SHARE for k, y in enumerate(yrs)}
    edu = dict(zip(yrs, EDU_CARE))
    part = lambda p: {y: sum(s.get(y, 0.0) for k, s in lines.items() if k[0] == p) for y in yrs}
    b, c, d = part('B'), part('C'), part('D')
    parity = lines['D parity (memo 15)']
    d_ltc = {y: d[y] - parity.get(y, 0.0) for y in yrs}
    w = lambda s: (sum(s[y] for y in WINDOW), s[2040])
    out = {
        "HLT-4's long-term care component, as booked (retired by a booking)": w(ltc),
        'Long-term care lines a booking adds (part B and part D in home care and nursing homes)':
            w({y: b[y] + d_ltc[y] for y in yrs}),
        '  net change on the general fund': w({y: b[y] + d_ltc[y] - ltc[y] for y in yrs}),
        "EDU-9B fund's care component, as booked (child care and pre-K, case mixed)": w(edu),
        'Child care and pre-K lines a booking adds (part C and memo 15)': w({y: c[y] + parity.get(y, 0.0) for y in yrs}),
        '  net change, wherever part C is booked': w({y: c[y] + parity.get(y, 0.0) - edu[y] for y in yrs}),
        'All three, net change against what is booked': w({y: allp[y] - ltc[y] - edu[y] for y in yrs}),
    }
    return out

if __name__ == '__main__':
    main()
