#!/usr/bin/env python3
"""Seat-by-seat simulation of the 2028 Senate elections, and a 2030-2032 control projection.

Role: the model behind dossiers/scenario/senate-model-2028.md and 2030-2034-control.md. It supersedes the
arithmetic in senate_2028_sim.py (kept for the record). Status: exploratory scenario model (stage B,
November 8, 2026). It is this project's own analysis, not a published forecast, and not a core model in
models/. Every input below names its source (SRC- IDs in library/catalog.csv); every number that is a
judgment rather than a measurement is marked ASSUMPTION, with the range tested in the sensitivity runs.

Method, in one paragraph. Each race's expected Democratic margin is the state's lean (a weighted blend of
its 2020 and 2024 presidential margins and its 2026 statewide results, each measured against that year's
national margin), plus the national environment E (the Democratic presidential margin in that year), plus a
candidate effect (incumbency and the incumbent's own record against the state's lean, shrunk toward zero).
Each simulated election draws a national presidential error, a Senate-wide ticket-splitting error, one
error per region (so neighbouring states move together) and one per race. Uncertain candidacies (Kelly,
Grassley, Johnson) are drawn per run. Alaska has its own ranked-choice submodel with four Murkowski branches.
Seats not up in 2028 include three that are still uncertain: the 2026 Alaska and Mississippi races
(uncalled) and Minnesota's November 2027 special election for Klobuchar's seat.

  python3 dossiers/scenario/tools/senate_model.py            print the headline tables
  python3 dossiers/scenario/tools/senate_model.py --write    regenerate dossiers/scenario/senate-model-outputs.md
  python3 dossiers/scenario/tools/test_senate_model.py       run the tests

Standard library only. Deterministic: every run is seeded.
"""
import math
import os
import random
import statistics as st
import sys

# --------------------------------------------------------------------------------------------------
# 1. National margins (Democratic minus Republican, points)
# --------------------------------------------------------------------------------------------------
NAT = {
    2020: 4.46,   # Biden 51.31 - Trump 46.85 [SRC-0575]
    2022: -2.6,   # House vote, D 47.4 R 50.0, Brookings Vital Statistics table 2-2 [SRC-0570]
    2024: -1.48,  # Trump popular-vote margin [SRC-0459]
    2026: 12.9,   # House vote, D 55.7 R 42.8, Cook tracker, unofficial (1-results.md) [SRC-0464]
}

# House-vote swing against the president's party at each midterm, 1990-2026 (points of margin).
# Brookings table 2-2 (1988-2024) [SRC-0570]; 2026 from Cook (1-results.md) [SRC-0464].
# 1990 0.1 (D+7.8 to D+7.9); 1994 12.2; 1998 0.5; 2002 -4.3; 2006 9.0; 2010 17.2; 2014 6.5; 2018 9.6;
# 2022 5.6; 2026 15.4.
MIDTERM_SWINGS = [0.1, 12.2, 0.5, -4.3, 9.0, 17.2, 6.5, 9.6, 5.6, 15.4]

# Change in the national presidential margin from one election to the next, 1992-2024 [SRC-0588]:
# 1992 D+5.6, 1996 D+8.5, 2000 D+0.5, 2004 R+2.5, 2008 D+7.3, 2012 D+3.9, 2016 D+2.1, 2020 D+4.5, 2024 R+1.5.
PRES_MARGINS = [5.6, 8.5, 0.5, -2.5, 7.3, 3.9, 2.1, 4.5, -1.5]

# --------------------------------------------------------------------------------------------------
# 2. State inputs
# --------------------------------------------------------------------------------------------------
# 2020 presidential D margin by state [SRC-0575]; 2024 [SRC-0459].
P20 = {
    'AL': -25.46, 'AK': -10.06, 'AZ': 0.30, 'AR': -27.62, 'CA': 29.16, 'CO': 13.50, 'CT': 20.07,
    'DE': 18.97, 'FL': -3.36, 'GA': 0.23, 'HI': 29.46, 'ID': -30.77, 'IL': 16.99, 'IN': -16.07,
    'IA': -8.20, 'KS': -14.63, 'KY': -25.94, 'LA': -18.61, 'ME': 9.07, 'MD': 33.21, 'MA': 33.46,
    'MI': 2.78, 'MN': 7.12, 'MS': -16.54, 'MO': -15.39, 'MT': -16.37, 'NE': -19.06, 'NV': 2.39,
    'NH': 7.35, 'NJ': 15.94, 'NM': 10.79, 'NY': 23.13, 'NC': -1.34, 'ND': -33.34, 'OH': -8.03,
    'OK': -33.08, 'OR': 16.08, 'PA': 1.16, 'RI': 20.78, 'SC': -11.68, 'SD': -26.16, 'TN': -23.21,
    'TX': -5.58, 'UT': -20.48, 'VT': 35.42, 'VA': 10.11, 'WA': 19.20, 'WV': -38.93, 'WI': 0.63,
    'WY': -43.39,
}
P24 = {
    'AL': -30.47, 'AK': -13.13, 'AZ': -5.53, 'AR': -30.64, 'CA': 20.14, 'CO': 10.99, 'CT': 14.51,
    'DE': 14.70, 'FL': -13.10, 'GA': -2.20, 'HI': 23.11, 'ID': -36.49, 'IL': 10.90, 'IN': -18.96,
    'IA': -13.21, 'KS': -16.12, 'KY': -30.53, 'LA': -22.01, 'ME': 6.90, 'MD': 28.54, 'MA': 25.20,
    'MI': -1.40, 'MN': 4.20, 'MS': -22.90, 'MO': -18.41, 'MT': -19.90, 'NE': -20.50, 'NV': -3.10,
    'NH': 2.78, 'NJ': 5.90, 'NM': 6.00, 'NY': 12.60, 'NC': -3.21, 'ND': -36.45, 'OH': -11.21,
    'OK': -34.26, 'OR': 14.30, 'PA': -1.71, 'RI': 13.80, 'SC': -17.87, 'SD': -29.19, 'TN': -29.72,
    'TX': -13.70, 'UT': -21.59, 'VT': 31.51, 'VA': 5.80, 'WA': 18.22, 'WV': -41.90, 'WI': -0.86,
    'WY': -45.80,
}
# 2026 statewide D margins against a Republican, unofficial, NBC and AP via 1-results.md [SRC-0574]
# [SRC-0483] [SRC-0445]: (margin, 'S' Senate or 'G' governor, party of an incumbent on the ballot or None).
# Races against an independent (NE, MT, SD, ID) are left out. Mississippi (Colom about +0.3) and Alaska
# (Peltola +0.3 on first choices) are uncalled.
M26 = {
    'AL': [(-9.4, 'S', None), (-4.0, 'G', None)], 'AK': [(0.3, 'S', 'R')], 'AZ': [(13.1, 'G', 'D')],
    'AR': [(-11.9, 'S', 'R'), (-15.3, 'G', 'R')], 'CA': [(31.0, 'G', None)],
    'CO': [(25.4, 'S', 'D'), (27.8, 'G', None)], 'CT': [(19.2, 'G', 'D')], 'DE': [(27.1, 'S', 'D')],
    'FL': [(-2.9, 'S', 'R'), (-1.3, 'G', None)], 'GA': [(18.0, 'S', 'D'), (8.6, 'G', None)],
    'HI': [(45.2, 'G', 'D')], 'IL': [(24.3, 'S', None), (23.5, 'G', 'D')],
    'IA': [(4.1, 'S', None), (11.0, 'G', None)], 'KS': [(5.0, 'S', 'R'), (0.6, 'G', None)],
    'KY': [(-12.1, 'S', None)], 'LA': [(-1.8, 'S', None)], 'ME': [(6.1, 'S', 'R')], 'MD': [(31.6, 'G', 'D')],
    'MA': [(31.2, 'S', 'D')], 'MI': [(7.0, 'S', None)], 'MN': [(10.1, 'S', None)], 'MS': [(0.3, 'S', 'R')],
    'NV': [(7.6, 'G', 'R')], 'NH': [(13.7, 'S', None), (-4.3, 'G', 'R')], 'NJ': [(27.3, 'S', 'D')],
    'NM': [(26.5, 'S', 'D')], 'NY': [(19.6, 'G', 'D')], 'NC': [(19.6, 'S', None)],
    'OH': [(4.8, 'S', 'R'), (7.9, 'G', None)], 'OK': [(-17.9, 'S', None), (-6.0, 'G', None)],
    'OR': [(19.4, 'S', 'D'), (9.6, 'G', 'D')], 'PA': [(22.1, 'G', 'D')], 'RI': [(37.5, 'S', 'D')],
    'SC': [(4.5, 'S', 'R'), (-4.5, 'G', None)], 'TN': [(-12.2, 'S', 'R'), (-2.5, 'G', None)],
    'TX': [(12.1, 'S', None), (7.1, 'G', 'R')], 'VA': [(22.8, 'S', 'D')], 'WV': [(-20.4, 'S', 'R')],
    'WI': [(8.0, 'G', None)], 'WY': [(-30.5, 'S', None)],
}


def adjusted_2026(s, prm):
    """2026 statewide margin for state s, net of incumbency, governor races weighted down (round 2).

    Governor races deviate from presidential lean about four points more than Senate races (Split Ticket,
    2014 and 2018) [SRC-0589], so they get weight gov_w; an incumbent on the ballot is worth inc (Senate) or
    inc_gov (governor) points, removed before the margin is used as a measure of the state's lean."""
    vals = M26.get(s)
    if not vals:
        return None
    num = den = 0.0
    for mg, kind, incp in vals:
        sign = {'D': 1, 'R': -1, None: 0}[incp]
        adj = mg - sign * (prm['inc'] if kind == 'S' else prm['inc_gov'])
        w = 1.0 if kind == 'S' else prm['gov_w']
        num += w * adj
        den += w
    return num / den


REGION = {  # ASSUMPTION: regional blocs whose errors are shared (see the model note in the dossier)
    'rust': ['WI', 'PA', 'OH', 'IA', 'MI', 'MN', 'NH', 'ME'],
    'sun': ['AZ', 'NV', 'GA', 'NC', 'FL', 'TX'],
    'plains': ['KS', 'MO', 'IN', 'OK', 'SD', 'ND', 'NE'],
    'south': ['AL', 'AR', 'KY', 'LA', 'SC', 'TN', 'MS', 'WV'],
    'mountain': ['AK', 'ID', 'UT', 'MT', 'WY'],
    'blue': ['CA', 'CO', 'CT', 'HI', 'IL', 'MD', 'NY', 'OR', 'VT', 'WA', 'DE', 'MA', 'NJ', 'NM', 'RI',
             'VA'],
}
REGION_OF = {s: r for r, ss in REGION.items() for s in ss}

# --------------------------------------------------------------------------------------------------
# 3. Parameters (ASSUMPTIONS with tested ranges)
# --------------------------------------------------------------------------------------------------
BASE_PARAMS = {
    'w20': 0.20, 'w24': 0.50, 'w26': 0.30,  # lean weights; tested 2026 weight 0.15-0.45
    'inc': 2.0,        # incumbency advantage, points of margin; tested 1.0-3.5
    'shrink': 0.40,    # share of a candidate's past over/underperformance that carries over; 0.2-0.6
    'cap': 6.0,        # cap on any candidate effect, points
    'sd_nat': 2.0,     # presidential national error around the scenario's E; 1.5-3.0
    'sd_tick': 1.0,    # Senate-wide ticket-splitting error
    'sd_reg': 2.5,     # regional error; 1.5-3.5
    'sd_race': 5.0,    # race error for an incumbent; 4-6
    'sd_open': 2.5,    # extra race error for an open seat (combined in quadrature)
    'ec_bias': 1.0,    # Democrats need E > ec_bias to win the Electoral College; 0-3
    'inc_gov': 3.0,    # incumbent-governor advantage removed from 2026 governor margins; 2-5 (round 2)
    'gov_w': 0.5,      # weight of a 2026 governor race relative to a Senate race in the 2026 lean (round 2)
}

# Seats not up in 2028 that are certain (Class 1 and Class 2 Democratic-caucus seats, excluding the three
# uncertain ones): 18 Class 1 (19 less Klobuchar's) + 19 called Class 2 = 37. See CLASS1 and CLASS2 below.
CERTAIN_D_NOT_UP = 37
UNCERTAIN_NOT_UP = {  # P(D) for each; ASSUMPTION drawn from 1-results.md (AK, MS) and section 1 (MN)
    'AK-2026': 0.78,  # Peltola leans, about 75-80% (1-results.md)
    'MS-2026': 0.87,  # Colom, about 85-90% (1-results.md)
    'MN-2027': 0.90,  # special election November 2, 2027 (Minn. Stat. 204D.28) [SRC-0578]; tested 0.8-0.95
}

# --------------------------------------------------------------------------------------------------
# 4. The 2028 races
# --------------------------------------------------------------------------------------------------
# Each race: party holding it in 2027, holder, p_run (chance the incumbent is the nominee; 1.0 if known),
# and 'record': the holder's own past result used for the candidate effect, as (year, D margin, was the
# holder an incumbent then). None means no usable D-v-R record; 'c' overrides the candidate effect.
# 2022 Senate margins [SRC-0565]; 2024 [SRC-0576]; 2026 [SRC-0574].
RACES = {
    'AL': dict(p='R', who='Britt', rec=(2022, -35.7, False)),
    'AK': dict(p='R', who='Murkowski', alaska=True),
    'AZ': dict(p='D', who='Kelly', rec=(2022, 4.9, True), p_run=0.75),     # weighing a presidential run [SRC-0581]
    'AR': dict(p='R', who='Boozman', rec=(2022, -34.8, True)),
    'CA': dict(p='D', who='Padilla', rec=(2022, 22.2, True)),
    'CO': dict(p='D', who='Bennet', rec=(2022, 14.6, True)),               # lost the 2026 governor primary [SRC-0580]
    'CT': dict(p='D', who='Blumenthal', rec=(2022, 15.0, True)),
    'FL': dict(p='R', who='Moody', c=-0.6),                                # appointed; won 2026 special 1.6 behind the governor ticket
    'GA': dict(p='D', who='Warnock', rec=(2022, 2.8, True)),               # runoff margin
    'HI': dict(p='D', who='Schatz', rec=(2022, 45.2, True)),
    'ID': dict(p='R', who='Crapo', rec=(2022, -32.0, True)),
    'IL': dict(p='D', who='Duckworth', rec=(2022, 15.3, True)),
    'IN': dict(p='R', who='Young', rec=(2022, -20.7, True)),
    'IA': dict(p='R', who='Grassley', rec=(2022, -12.2, True), p_run=0.35),  # decides in 2027, age 95 in 2028 [SRC-0572]
    'KS': dict(p='R', who='Moran', rec=(2022, -23.0, True)),
    'KY': dict(p='R', who='Paul', rec=(2022, -23.6, True)),
    'LA': dict(p='R', who='Kennedy', c=-2.0),                              # 2022 jungle primary, no D-v-R margin
    'MD': dict(p='D', who='Van Hollen', rec=(2022, 31.6, True)),
    'MO': dict(p='R', who='Schmitt', rec=(2022, -13.2, False)),
    'NV': dict(p='D', who='Cortez Masto', rec=(2022, 0.8, True)),
    'NH': dict(p='D', who='Hassan', rec=(2022, 9.2, True)),
    'NY': dict(p='D', who='Schumer', rec=(2022, 14.0, True)),
    'NC': dict(p='R', who='Budd', rec=(2022, -3.2, False)),
    'ND': dict(p='R', who='Hoeven', c=-2.0),                               # 2022 opponent mainly an independent
    'OH': dict(p='D', who='Brown', rec=(2024, -3.6, True)),                # 2024 loss ran 7.6 ahead of Harris
    'OK': dict(p='R', who='Lankford', rec=(2022, -32.2, True)),
    'OR': dict(p='D', who='Wyden', rec=(2022, 14.9, True)),
    'PA': dict(p='D', who='Fetterman', c=0.0, extra_sd=3.0),              # see the dossier: brand and primary risk
    'SC': dict(p='R', who='Scott', rec=(2022, -25.9, True)),
    'SD': dict(p='R', who='Thune', rec=(2022, -43.4, True)),
    'TN*': dict(p='R', who='Blackburn appointee', c=-1.0, st='TN'),       # special for the term to 2031 [SRC-0582]
    'UT': dict(p='R', who='Lee', c=-2.0),                                  # 2022 opponent an independent (McMullin)
    'VT': dict(p='D', who='Welch', rec=(2022, 40.4, False)),
    'WA': dict(p='D', who='Murray', rec=(2022, 14.5, True)),
    'WI': dict(p='R', who='Johnson', rec=(2022, -1.0, True), p_run=0.25),  # says he does not want a fourth term [SRC-0586]
}


def state_of(key):
    return RACES.get(key, {}).get('st', key.rstrip('*'))


def lean(s, prm=BASE_PARAMS):
    """State lean in points of D margin relative to the nation (positive = more Democratic)."""
    l20 = P20[s] - NAT[2020]
    l24 = P24[s] - NAT[2024]
    a26 = adjusted_2026(s, prm)
    if a26 is not None:
        l26 = a26 - NAT[2026]
        w = prm['w20'] + prm['w24'] + prm['w26']
        return (prm['w20'] * l20 + prm['w24'] * l24 + prm['w26'] * l26) / w
    return (prm['w20'] * l20 + prm['w24'] * l24) / (prm['w20'] + prm['w24'])


def expected_record(s, year):
    """What a generic candidate of each party would have got in that state and year (D margin)."""
    if year in (2020, 2024):
        return {2020: P20, 2024: P24}[year][s]           # concurrent presidential margin
    mid = 0.5 * ((P20[s] - NAT[2020]) + (P24[s] - NAT[2024]))
    return NAT[year] + mid


def candidate_effect(key, prm=BASE_PARAMS, races=None):
    """Candidate effect toward D when the holder is the nominee (points)."""
    r = (races or RACES)[key]
    if 'c' in r:
        return r['c']
    sign = 1 if r['p'] == 'D' else -1
    year, margin, was_inc = r['rec']
    over = margin - expected_record(state_of(key), year)
    resid = over - (sign * prm['inc'] if was_inc else 0.0)
    resid = max(-12.0, min(12.0, resid))
    c = sign * prm['inc'] + prm['shrink'] * resid
    return max(-prm['cap'], min(prm['cap'], c))


# --------------------------------------------------------------------------------------------------
# 5. Alaska: Murkowski branches under the top-four primary and ranked-choice general election
# --------------------------------------------------------------------------------------------------
# Calibration to 2022 [SRC-0565]: first choices Murkowski 43.4, Tshibaka 42.6, Chesbro (D) 10.4, Kelley 2.9.
# With about 45% of voters on the Democratic side (two-party), Murkowski took about 77% of the Democratic
# side and about 16% of the Republican side. ASSUMPTIONS for 2028 (ranges in the dossier):
AK_BRANCHES = {
    # a: share of D-side voters ranking Murkowski first (a range: it falls when Democrats field a strong
    # candidate); b: share of R-side voters; dem: a serious Democrat is on the ballot; caucus: whom a
    # Murkowski win counts for.
    # Round 3: her standing with Alaska progressives fell from net +54 to net -21 in 2025 [SRC-0590], so the
    # D-side share is lower than 2022's 0.77 unless she breaks with her party.
    'R':      dict(a=(0.35, 0.70), b=0.14, dem=True, caucus='R'),   # Republican, against Dunleavy and a Democrat
    'I-D':    dict(a=(0.80, 0.92), b=0.12, dem=False, caucus='D'),  # independent pledged to caucus with Democrats
    'I-none': dict(a=(0.55, 0.80), b=0.13, dem=True, caucus='I'),   # independent caucusing with neither
    'retire': dict(a=(0.0, 0.0), b=0.0, dem=True, caucus=None),     # open seat: a Democrat against Dunleavy
}
# ASSUMPTION. Round 3 lowered I-D from 10% to 6%: she endorsed Sullivan against Peltola in January 2026 "to keep
# in the majority" [SRC-0591] and opposes weakening the filibuster [SRC-0592]; she is 71 in 2028.
AK_WEIGHTS = {'R': 0.56, 'I-D': 0.06, 'I-none': 0.08, 'retire': 0.30}
# Chance Measure 2 (repeal of the top-four and ranked-choice system) passes. Round 4: No leads 106,040 to
# 98,460 (51.85%) with about 205,000 counted [SRC-0594]; about 60,000 early and absentee ballots remain, the
# kinds that leaned toward keeping the system in 2024 [SRC-0561]. Yes would need about 56% of them.
AK_P_REPEAL = 0.04
# Second-choice transfers. 2022 round by round [SRC-0565]: Murkowski 43.4 -> 53.7 after Kelley's and Chesbro's
# votes moved, so roughly three in four Chesbro ballots went to her. ASSUMPTIONS for 2028:
T_DEM_TO_M, T_DEM_TO_R = 0.75, 0.07
T_M_D_TO_DEM, T_M_R_TO_R, T_M_R_TO_DEM = 0.80, 0.50, 0.15
T_R_TO_M, T_R_TO_DEM = 0.55, 0.05


def alaska_outcome(m, branch, rcv=True, rng=None, r_primary_win=0.3):
    """Return (caucus of the winner: 'D', 'R' or 'I'; effective D-caucus margin; who won: 'M', 'D' or 'R').

    m is the margin a generic Democrat would get against a generic Republican (Dunleavy) in that run."""
    p = min(0.95, max(0.05, 0.5 + m / 200.0))     # D-side two-party share
    br = AK_BRANCHES[branch]
    if branch == 'retire':
        return ('D' if m > 0 else 'R'), m, ('D' if m > 0 else 'R')
    lo, hi = br['a']
    a = (lo + hi) / 2 if rng is None else rng.uniform(lo, hi)
    b = br['b']
    caucus = br['caucus']
    murk = a * p + b * (1 - p)
    dem = (1 - a) * p if br['dem'] else 0.0      # with no serious Democrat these voters mostly exhaust
    rep = (1 - b) * (1 - p)
    shares = {'M': murk, 'D': dem, 'R': rep}
    if not rcv:
        # closed primaries and plurality (Measure 2 passes): a Republican Murkowski must win the primary
        if branch == 'R':
            lost = (rng.random() > r_primary_win) if rng is not None else True
            if lost:
                if rng is not None and rng.random() < 0.5:
                    caucus = 'I'      # runs as a write-in or independent, as in 2010
                else:
                    return ('D' if m > 0 else 'R'), m, ('D' if m > 0 else 'R')
            else:
                # she is the Republican nominee: Dunleavy is off the general ballot, and most of his
                # Republican-side voters back the nominee (ASSUMPTION 0.85; the rest split or abstain)
                shares = {'M': murk + 0.85 * rep, 'D': dem + 0.05 * rep}
        if not br['dem']:
            shares.pop('D')
    else:
        if br['dem']:
            low = min(shares, key=shares.get)
            if low == 'D':
                shares['M'] += T_DEM_TO_M * dem
                shares['R'] += T_DEM_TO_R * dem
            elif low == 'M':
                shares['D'] += T_M_D_TO_DEM * a * p + T_M_R_TO_DEM * b * (1 - p)
                shares['R'] += T_M_R_TO_R * b * (1 - p)
            else:
                shares['M'] += T_R_TO_M * rep
                shares['D'] += T_R_TO_DEM * rep
            shares.pop(low)
        else:
            shares.pop('D')
    who = max(shares, key=shares.get)
    winner = caucus if who == 'M' else who
    dside = shares.get('D', 0.0) + (shares.get('M', 0.0) if caucus == 'D' else 0.0)
    total = sum(shares.values())
    if dside == 0.0:     # no D-caucus candidate in the final round: rank the seat by the generic margin
        return winner, min(-0.1, m), who
    return winner, 100.0 * (2 * dside - total) / max(1e-9, total), who


# --------------------------------------------------------------------------------------------------
# 6. Simulation of 2028
# --------------------------------------------------------------------------------------------------
def simulate_2028(env, n=20000, seed=2028, prm=None, overrides=None, ak_branch=None, ak_rcv=None,
                  env_sd=0.0, races=None, uncertain=None):
    """Simulate n elections at national environment env (D presidential margin, points).

    env_sd > 0 draws the environment itself (for presidential-winner conditioning). overrides maps race
    keys to extra points toward D (scenario tests). Returns a dict of results."""
    prm = dict(BASE_PARAMS, **(prm or {}))
    races = races or RACES
    unc = dict(UNCERTAIN_NOT_UP, **(uncertain or {}))
    rng = random.Random(seed)
    keys = list(races)
    base_m = {k: lean(state_of(k), prm) + (overrides or {}).get(k, 0.0) for k in keys}
    ceff = {k: (candidate_effect(k, prm, races) if not races[k].get('alaska') else 0.0) for k in keys}
    regions = sorted(REGION)
    out = dict(seats=[], dpres=[], wins={k: 0 for k in keys}, tip51={}, tip50={}, tip60={}, ak={},
               ind=[], env=[], draws=[], dwon=[])
    for _ in range(n):
        e = env + (rng.gauss(0, env_sd) if env_sd else 0.0)
        nat = rng.gauss(0, prm['sd_nat'])
        pres = e + nat
        dpres = pres > prm['ec_bias']
        tick = rng.gauss(0, prm['sd_tick'])
        reg = {r: rng.gauss(0, prm['sd_reg']) for r in regions}
        draws = {k: rng.random() < unc[k] for k in sorted(unc)}
        base = CERTAIN_D_NOT_UP + sum(draws.values())
        margins = {}
        ind = 0
        for k in keys:
            r = races[k]
            s = state_of(k)
            runs = rng.random() < r.get('p_run', 1.0)
            sd = prm['sd_race']
            if r.get('extra_sd'):
                sd = math.hypot(sd, r['extra_sd'])
            if r.get('alaska'):
                m = base_m[k] + pres + tick + reg[REGION_OF[s]] + rng.gauss(0, math.hypot(sd, prm['sd_open']))
                br = ak_branch or _pick(rng, AK_WEIGHTS)
                rcv = ak_rcv if ak_rcv is not None else (rng.random() >= AK_P_REPEAL)
                win, em, who = alaska_outcome(m, br, rcv=rcv, rng=rng)
                out['ak'][(br, who, win)] = out['ak'].get((br, who, win), 0) + 1
                if win == 'I':
                    ind += 1
                margins[k] = (em, win == 'D')
                continue
            c = ceff[k] if runs else 0.0
            if not runs:
                sd = math.hypot(sd, prm['sd_open'])
            m = base_m[k] + pres + tick + reg[REGION_OF[s]] + c + rng.gauss(0, sd)
            margins[k] = (m, m > 0)
        dwins = sum(1 for k in keys if margins[k][1])
        for k in keys:
            if margins[k][1]:
                out['wins'][k] += 1
        seats = base + dwins
        out['seats'].append(seats)
        out['dpres'].append(dpres)
        out['ind'].append(ind)
        out['env'].append(pres)
        out['draws'].append(draws)
        out['dwon'].append(frozenset(k for k in keys if margins[k][1]))
        order = sorted(keys, key=lambda k: -margins[k][0])
        for need, tab in ((51 - base, out['tip51']), (50 - base, out['tip50']), (60 - base, out['tip60'])):
            if 1 <= need <= len(order):
                t = order[need - 1]
                tab[t] = tab.get(t, 0) + 1
    out['n'] = n
    return out


def _pick(rng, weights):
    x = rng.random()
    acc = 0.0
    for k in sorted(weights):
        acc += weights[k]
        if x < acc:
            return k
    return sorted(weights)[-1]


def summarize(out, cond=None):
    """Seat distribution summary; cond is None, 'D' (Democratic president) or 'R'."""
    idx = [i for i in range(out['n']) if cond is None or out['dpres'][i] == (cond == 'D')]
    if not idx:
        return None
    seats = sorted(out['seats'][i] for i in idx)
    m = len(seats)

    def q(p):
        return seats[min(m - 1, int(p * m))]

    def pr(k):
        return sum(1 for s in seats if s >= k) / m
    ctrl = sum(1 for i in idx if out['seats'][i] >= 51 or (out['seats'][i] == 50 and out['dpres'][i])) / m
    return dict(n=m, share=m / out['n'], mean=st.mean(seats), p5=q(0.05), med=q(0.5), p95=q(0.95),
                p50=pr(50), p51=pr(51), p52=pr(52), p55=pr(55), p58=pr(58), p60=pr(60), ctrl=ctrl)


# --------------------------------------------------------------------------------------------------
# 7. 2030 and 2032: the Class 1 and Class 2 seats
# --------------------------------------------------------------------------------------------------
# Class 1, elected 2024, up 2030 [SRC-0576]: holder party and 2024 D margin (vs the main opponent).
# King (ME) and Sanders (VT) are independents who caucus with Democrats. Minnesota's seat is filled in the
# November 2027 special and the Tennessee seat in the November 2028 special; both are up again in 2030.
CLASS1 = {
    'AZ': ('D', 2.4), 'CA': ('D', 17.8), 'CT': ('D', 18.8), 'DE': ('D', 17.1), 'FL': ('R', -12.8),
    'HI': ('D', 32.7), 'IN': ('R', -19.8), 'ME': ('D', 17.5), 'MD': ('D', 11.8), 'MA': ('D', 19.8),
    'MI': ('D', 0.3), 'MN': ('D', 15.7), 'MS': ('R', -26.2), 'MO': ('R', -13.8), 'MT': ('R', -7.1),
    'NE': ('R', -6.7), 'NV': ('D', 1.7), 'NJ': ('D', 9.6), 'NM': ('D', 10.2), 'NY': ('D', 17.5),
    'ND': ('R', -33.0), 'OH': ('R', -3.6), 'PA': ('R', -0.2), 'RI': ('D', 19.8), 'TN': ('R', -29.6),
    'TX': ('R', -8.5), 'UT': ('R', -30.8), 'VT': ('D', 31.1), 'VA': ('D', 9.0), 'WA': ('D', 18.5),
    'WV': ('R', -41.5), 'WI': ('D', 0.8), 'WY': ('R', -51.0),
}
CLASS1_VS_IND = {'NE'}  # Fischer's 2024 opponent was an independent (Osborn)
CLASS1_OPEN = {'MN', 'TN'}   # holders new since 2024 (2027 and 2028 special winners): no 2024 record used
# Class 2, elected 2026, up 2032 (1-results.md) [SRC-0444] [SRC-0445]: holder party and 2026 D margin.
CLASS2 = {
    'TX': ('D', 12.1), 'NC': ('D', 19.6), 'SC': ('D', 4.5), 'KS': ('D', 5.1), 'IA': ('D', 4.1),
    'ME': ('D', 6.1), 'GA': ('D', 18.0), 'MI': ('D', 7.0), 'NH': ('D', 13.7), 'MN': ('D', 10.1),
    'IL': ('D', 24.3), 'VA': ('D', 22.8), 'NJ': ('D', 27.3), 'NM': ('D', 26.5), 'CO': ('D', 25.4),
    'OR': ('D', 19.4), 'DE': ('D', 27.1), 'MA': ('D', 31.2), 'RI': ('D', 37.5), 'MS': ('D', 0.3),
    'AK': ('D', 0.3), 'LA': ('R', -1.8), 'NE': ('R', -6.2), 'AL': ('R', -9.4), 'MT': ('R', -10.6),
    'AR': ('R', -11.9), 'KY': ('R', -12.1), 'TN': ('R', -12.2), 'OK': ('R', -17.9), 'WV': ('R', -20.4),
    'SD': ('R', -21.0), 'ID': ('R', -23.0), 'WY': ('R', -30.5),
}
CLASS2_UNCERTAIN = {'MS', 'AK'}   # holder depends on the uncalled 2026 count
CLASS2_VS_IND = {'NE', 'MT', 'SD', 'ID'}  # 2026 opponent an independent: no D-v-R record used


def class_effect(s, party, margin, year, prm, open_seat=False, vs_ind=False):
    """Candidate effect for a Class 1 or 2 holder, from the holder's own last race."""
    sign = 1 if party == 'D' else -1
    if open_seat or vs_ind:
        return sign * prm['inc'] * (0.5 if open_seat else 1.0)
    if year == 2026:
        exp = NAT[2026] + 0.5 * ((P20[s] - NAT[2020]) + (P24[s] - NAT[2024]))
    else:
        exp = P24[s]
    resid = max(-12.0, min(12.0, (margin - exp) - sign * prm['inc'] * 0.5))
    c = sign * prm['inc'] + prm['shrink'] * resid
    return max(-prm['cap'], min(prm['cap'], c))


def p_retire_class(s):
    return 0.12  # ASSUMPTION: about one seat in eight opens per cycle; open seats lose the candidate effect


# Statehood (round 4). DEM-5 (D.C.) and DEM-6 (Puerto Rico, a binding plebiscite first) are in the agenda as
# regular-order bills (◐ at 51: they need D2). ASSUMPTIONS: D.C.'s two senators caucus with Democrats; Puerto
# Rico's two split by its own politics (both D 45%, one each 25%, both R 30%), since its statehood party is
# led by Republicans at the national level. Seats are added from the Congress named; terms are not modeled.
PR_SPLIT = ((2, 0.45), (1, 0.25), (0, 0.30))


def simulate_chain(env28, n=20000, seed=2030, prm=None, env_sd=3.0, midterm=None, stipulate=False,
                   overrides=None, statehood=None, statehood_from=2033, c2_retire=None, c2_shrink=None, c2_bonus=None):
    """2028 -> 2030 -> 2032 chain. Returns per-run D-caucus seats after each election and presidency flags.

    midterm: (mean, sd) of the swing against the president's party in 2030; default from MIDTERM_SWINGS.
    stipulate: condition on a Democratic president elected in 2028 and re-elected in 2032 (D1).
    statehood: None, 'DC' or 'DC+PR', seated from statehood_from (2031 or 2033).
    c2_retire / c2_shrink: override the Class 2 retirement chance and carry-over (the "retention" lever)."""
    prm = dict(BASE_PARAMS, **(prm or {}))
    mt_mean = st.mean(MIDTERM_SWINGS) if midterm is None else midterm[0]
    mt_sd = st.stdev(MIDTERM_SWINGS) if midterm is None else midterm[1]
    diffs = [b - a for a, b in zip(PRES_MARGINS, PRES_MARGINS[1:])]
    pres_sd = st.stdev(diffs)
    # Simulate 2028 with the full seat model, keeping each run's seat count, environment and Alaska result.
    o28 = simulate_2028(env28, n=n, seed=seed, prm=prm, env_sd=env_sd, overrides=overrides)
    rng = random.Random(seed + 1)
    regions = sorted(REGION)
    c1 = {s: (lean(s, prm), class_effect(s, p, m, 2024, prm, open_seat=s in CLASS1_OPEN, vs_ind=s in CLASS1_VS_IND))
          for s, (p, m) in CLASS1.items()}
    prm2 = dict(prm, shrink=c2_shrink) if c2_shrink is not None else prm
    c2 = {s: (lean(s, prm), class_effect(s, p, m, 2026, prm2, vs_ind=s in CLASS2_VS_IND)) for s, (p, m) in CLASS2.items()}
    half = prm['inc'] * 0.5
    res = dict(s28=[], s30=[], s32=[], dpres28=[], dpres32=[], e30=[], e32=[], kept=0, w32=[], h32=[])
    for i in range(n):
        s28 = o28['seats'][i]
        e28 = o28['env'][i]
        dp28 = o28['dpres'][i]
        if stipulate and not dp28:
            continue
        # 2030 midterm: the president's party loses ground
        swing = rng.gauss(mt_mean, mt_sd)
        e30 = e28 - swing if dp28 else e28 + swing
        # Seats not up in 2030: everything except Class 1. Count D-caucus seats in Class 2 and 3 from the
        # 2028 run: s28 minus the Class 1 D seats held then (18 certain + MN special draw, approximated).
        dr = o28['draws'][i]
        won = o28['dwon'][i]
        # Holders that depend on this run: Minnesota (2027 special) and Tennessee (2028 special)
        holder1 = {'MN': 'D' if dr['MN-2027'] else 'R', 'TN': 'D' if 'TN*' in won else 'R'}
        # Class 1 Democratic seats held going into 2030: 18 certain, Minnesota (2027 special) and a
        # Democratic Tennessee special winner (2028), which s28 already counts and 2030 contests again
        d_c1_before = 18 + dr['MN-2027'] + ('TN*' in won)
        not_up30 = s28 - d_c1_before
        reg = {r: rng.gauss(0, prm['sd_reg']) for r in regions}
        tick = rng.gauss(0, prm['sd_tick'])
        d30 = 0
        for s, (L, c) in c1.items():
            if s in holder1:
                c = half if holder1[s] == 'D' else -half
            inc_runs = rng.random() > p_retire_class(s)
            sd = prm['sd_race'] if inc_runs else math.hypot(prm['sd_race'], prm['sd_open'])
            m = L + e30 + tick + reg[REGION_OF[s]] + (c if inc_runs else 0.0) + rng.gauss(0, sd)
            d30 += m > 0
        s30 = not_up30 + d30
        new = 0
        if statehood:
            new = 2 + (_pick_split(rng) if statehood == 'DC+PR' else 0)
        if statehood and statehood_from == 2031:
            s30 += new
        # 2032 presidential year: environment drifts from 2028
        e32 = e28 + rng.gauss(-0.9, pres_sd)
        dp32 = e32 > prm['ec_bias']
        if stipulate and not dp32:
            continue
        holder2 = {'AK': 'D' if dr['AK-2026'] else 'R', 'MS': 'D' if dr['MS-2026'] else 'R'}
        d_c2_before = 19 + dr['AK-2026'] + dr['MS-2026']
        not_up32 = s30 - d_c2_before
        reg = {r: rng.gauss(0, prm['sd_reg']) for r in regions}
        tick = rng.gauss(0, prm['sd_tick'])
        d32 = 0
        won32 = set()
        for s, (L, c) in c2.items():
            if s in holder2:
                c = prm['inc'] if holder2[s] == 'D' else -prm['inc']
            inc_runs = rng.random() > (p_retire_class(s) if c2_retire is None else c2_retire)
            sd = prm['sd_race'] if inc_runs else math.hypot(prm['sd_race'], prm['sd_open'])
            m = L + e32 + tick + reg[REGION_OF[s]] + (c if inc_runs else 0.0) + rng.gauss(0, sd)
            m += (c2_bonus or {}).get(s, 0.0)
            d32 += m > 0
            if m > 0:
                won32.add(s)
        s32 = not_up32 + d32
        if statehood and statehood_from == 2033:
            s32 += new
        res['s28'].append(s28)
        res['s30'].append(s30)
        res['s32'].append(s32)
        res['dpres28'].append(dp28)
        res['dpres32'].append(dp32)
        res['e30'].append(e30)
        res['e32'].append(e32)
        res['w32'].append(frozenset(won32))
        res['h32'].append(frozenset(s for s, (p, _) in CLASS2.items() if (holder2.get(s, p)) == 'D'))
    res['kept'] = len(res['s28'])
    return res


def _pick_split(rng):
    x = rng.random()
    acc = 0.0
    for seats, p in PR_SPLIT:
        acc += p
        if x < acc:
            return seats
    return 0


def drivers_2032(res, cond28='D'):
    """For each Democratic-held Class 2 seat: P(held in 2032), and its share of all 2032 losses."""
    idx = [i for i in range(res['kept']) if cond28 is None or res['dpres28'][i] == (cond28 == 'D')]
    lost = {}
    held = {}
    for i in idx:
        for s in res['h32'][i]:
            held[s] = held.get(s, 0) + 1
            if s not in res['w32'][i]:
                lost[s] = lost.get(s, 0) + 1
    tot = sum(lost.values()) or 1
    rows = [(s, 1 - lost.get(s, 0) / held[s], lost.get(s, 0) / tot, lost.get(s, 0) / len(idx)) for s in held]
    return sorted(rows, key=lambda r: -r[2])


def chain_table(res, cond28=None):
    idx = [i for i in range(res['kept']) if cond28 is None or res['dpres28'][i] == (cond28 == 'D')]
    m = len(idx)
    rows = []
    for key, label in (('s28', 'January 2029'), ('s30', 'January 2031'), ('s32', 'January 2033')):
        v = [res[key][i] for i in idx]
        rows.append((label, st.mean(v), sum(x >= 50 for x in v) / m, sum(x >= 51 for x in v) / m,
                     sum(x >= 55 for x in v) / m, sum(x >= 60 for x in v) / m))
    # "through each Congress": the seat floor held continuously from 2029
    thru = []
    for upto in (('s28',), ('s28', 's30'), ('s28', 's30', 's32')):
        thru.append(tuple(sum(all(res[k][i] >= t for k in upto) for i in idx) / m for t in (50, 55, 60)))
    return m, rows, thru


# --------------------------------------------------------------------------------------------------
# 8. Scenarios and report
# --------------------------------------------------------------------------------------------------
SCENARIOS = [  # (label, env, env_sd)
    ('R+3', -3.0, 0.0), ('Neutral', 0.0, 0.0), ('D+3', 3.0, 0.0), ('D+6', 6.0, 0.0),
    ('2026 repeat (D+13)', 13.0, 0.0),
]
PRIOR = ('Evidence-weighted prior, D+3 with SD 4.5', 3.0, 4.5)  # ASSUMPTION, see the dossier

# Espen's priors, as a scenario: Ohio stays the most exposed seat, and Arizona, Georgia and Nevada are
# safe-leaning in a neutral year. Implemented as extra points toward D for AZ, GA and NV (sized so each is
# about 80% in a neutral year), and North Carolina and Wisconsin as "very solid" pickups (+3 each).
ESPEN_OVERRIDES = {'AZ': 3.0, 'GA': 2.5, 'NV': 5.5, 'NC': 3.0, 'WI': 3.0}


def fmt_pct(x):
    return '%d%%' % round(100 * x) if x >= 0.005 else '<1%' if x > 0 else '0'


def report(n=20000):
    L = []
    w = L.append
    w('# Senate model outputs (generated)\n')
    w('Role: the tables `tools/senate_model.py --write` produces, read by `senate-model-2028.md` and '
      '`2030-2034-control.md`. Status: generated; do not edit by hand. Every figure is this project\'s '
      'exploratory scenario arithmetic, not a forecast. n = %d simulated elections per row, seeded.\n' % n)
    w('## 1. Inputs as computed\n')
    w('| Race | Holder | Lean | Candidate effect | P(incumbent is nominee) | P(D) neutral | P(D) D+3 |')
    w('| --- | --- | --- | --- | --- | --- | --- |')
    neutral = simulate_2028(0.0, n=n)
    d3 = simulate_2028(3.0, n=n)
    for k in sorted(RACES, key=lambda k: -neutral['wins'][k]):
        r = RACES[k]
        c = 'branch model' if r.get('alaska') else '%+.1f' % candidate_effect(k)
        w('| %s | %s (%s) | %+.1f | %s | %s | %s | %s |' % (
            k, r['who'], r['p'], lean(state_of(k)), c, fmt_pct(r.get('p_run', 1.0)),
            fmt_pct(neutral['wins'][k] / n), fmt_pct(d3['wins'][k] / n)))
    w('\n## 2. Democratic-caucus seats in January 2029, by national environment\n')
    w('| Environment | Mean | 90% range | P(≥50) | P(≥51) | P(≥52) | P(≥55) | P(≥58) | P(≥60) | P(D president) | P(D control) |')
    w('| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |')
    runs = {}
    for label, e, sd in SCENARIOS + [PRIOR]:
        o = simulate_2028(e, n=n, env_sd=sd)
        runs[label] = o
        s = summarize(o)
        dp = sum(o['dpres']) / n
        w('| %s | %.1f | %d-%d | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            label, s['mean'], s['p5'], s['p95'], fmt_pct(s['p50']), fmt_pct(s['p51']), fmt_pct(s['p52']),
            fmt_pct(s['p55']), fmt_pct(s['p58']), fmt_pct(s['p60']), fmt_pct(dp), fmt_pct(s['ctrl'])))
    w('\n## 3. By presidential winner (evidence-weighted prior)\n')
    w('| Winner | Share of runs | Mean seats | 90% range | P(≥50) | P(≥51) | P(≥55) | P(≥60) | P(D control) |')
    w('| --- | --- | --- | --- | --- | --- | --- | --- | --- |')
    for cond in ('D', 'R'):
        s = summarize(runs[PRIOR[0]], cond)
        w('| %s president | %s | %.1f | %d-%d | %s | %s | %s | %s | %s |' % (
            'Democratic' if cond == 'D' else 'Republican', fmt_pct(s['share']), s['mean'], s['p5'], s['p95'],
            fmt_pct(s['p50']), fmt_pct(s['p51']), fmt_pct(s['p55']), fmt_pct(s['p60']), fmt_pct(s['ctrl'])))
    w('\n## 4. Tipping-point seats (evidence-weighted prior)\n')
    w('The seat that delivers the 50th, 51st or 60th Democratic-caucus seat when the races are ranked by '
      'margin; share of runs in which each race is that seat.\n')
    o = runs[PRIOR[0]]
    w('| Race | 50th seat | 51st seat | 60th seat |')
    w('| --- | --- | --- | --- |')
    tot50 = sum(o['tip50'].values()) or 1
    tot51 = sum(o['tip51'].values()) or 1
    tot60 = sum(o['tip60'].values()) or 1
    ranked = sorted(set(o['tip51']) | set(o['tip50']) | set(o['tip60']), key=lambda k: -o['tip51'].get(k, 0))
    for k in ranked[:12]:
        w('| %s | %s | %s | %s |' % (k, fmt_pct(o['tip50'].get(k, 0) / tot50), fmt_pct(o['tip51'].get(k, 0) / tot51),
                                     fmt_pct(o['tip60'].get(k, 0) / tot60)))
    w('\nThe 60th seat, ranked: ' + ', '.join('%s %s' % (k, fmt_pct(v / tot60)) for k, v in
                                           sorted(o['tip60'].items(), key=lambda kv: -kv[1])[:8]) + '.\n')
    w('## 5. Espen\'s priors as a scenario\n')
    w('Extra points toward Democrats: %s.\n' % ', '.join('%s %+.1f' % kv for kv in sorted(ESPEN_OVERRIDES.items())))
    w('| Environment | Model: mean seats | Priors: mean seats | Model P(hold AZ, GA and NV) | Priors P(hold all three) | Model P(win NC and WI) | Priors P(win both) |')
    w('| --- | --- | --- | --- | --- | --- | --- |')
    for label, e in (('Neutral', 0.0), ('D+3', 3.0)):
        a = simulate_2028(e, n=n, seed=77)
        b = simulate_2028(e, n=n, seed=77, overrides=ESPEN_OVERRIDES)
        ja = joint(e, n, None, ('AZ', 'GA', 'NV'))
        jb = joint(e, n, ESPEN_OVERRIDES, ('AZ', 'GA', 'NV'))
        pa = joint(e, n, None, ('NC', 'WI'))
        pb = joint(e, n, ESPEN_OVERRIDES, ('NC', 'WI'))
        w('| %s | %.1f | %.1f | %s | %s | %s | %s |' % (label, summarize(a)['mean'], summarize(b)['mean'],
                                                        fmt_pct(ja), fmt_pct(jb), fmt_pct(pa), fmt_pct(pb)))
    pri = simulate_2028(0.0, n=n, seed=77, overrides=ESPEN_OVERRIDES)
    w('\nPer seat in a neutral year, model against priors: ' + '; '.join(
        '%s %s against %s' % (k, fmt_pct(neutral['wins'][k] / n), fmt_pct(pri['wins'][k] / n))
        for k in ('OH', 'AZ', 'GA', 'NV', 'NC', 'WI')) + '.\n')
    w('\nDemocratic-held seats ranked by P(D) in a neutral year (model):\n')
    held = [k for k in RACES if RACES[k]['p'] == 'D']
    w('| Seat | P(D) neutral | P(D) D+3 |')
    w('| --- | --- | --- |')
    for k in sorted(held, key=lambda k: neutral['wins'][k])[:6]:
        w('| %s | %s | %s |' % (k, fmt_pct(neutral['wins'][k] / n), fmt_pct(d3['wins'][k] / n)))
    w('\n## 6. Alaska: the Murkowski branches\n')
    w('Who wins the Alaska seat (Murkowski / the Democrat / Dunleavy or another Republican), and the share of '
      'runs in which the winner caucuses with Democrats, by branch and national environment.\n')
    w('| Branch | Voting system | Neutral: M / D / R; D caucus | D+3 | D+6 |')
    w('| --- | --- | --- | --- | --- |')
    for br in ('R', 'I-D', 'I-none', 'retire'):
        for rcv in (True, False):
            cells = []
            for e in (0.0, 3.0, 6.0):
                o2 = simulate_2028(e, n=n // 2, seed=99, ak_branch=br, ak_rcv=rcv)
                tot = sum(o2['ak'].values())
                got = {x: sum(v for (b2, who, wv), v in o2['ak'].items() if who == x) / tot for x in 'MDR'}
                dc = sum(v for (b2, who, wv), v in o2['ak'].items() if wv == 'D') / tot
                cells.append('%s / %s / %s; %s' % (fmt_pct(got['M']), fmt_pct(got['D']), fmt_pct(got['R']), fmt_pct(dc)))
            w('| %s | %s | %s |' % (br, 'top four + RCV' if rcv else 'repealed (closed primary, plurality)', ' | '.join(cells)))
    w('\nMixture weights (assumption): %s; P(repeal) %s.\n' % (
        ', '.join('%s %s' % (k, fmt_pct(v)) for k, v in sorted(AK_WEIGHTS.items())), fmt_pct(AK_P_REPEAL)))
    w('## 6b. The "wild map": Republican-held seats by environment\n')
    w('| Seat | Neutral | D+3 | D+6 | 2026 repeat (D+13) |')
    w('| --- | --- | --- | --- | --- |')
    wild = ['NC', 'WI', 'IA', 'AK', 'FL', 'KS', 'SC', 'MO', 'IN', 'UT', 'LA']
    envruns = {e: (neutral if e == 0.0 else d3 if e == 3.0 else simulate_2028(e, n=n)) for e in (0.0, 3.0, 6.0, 13.0)}
    for k in wild:
        w('| %s (%s) | %s |' % (k, RACES[k]['who'], ' | '.join(fmt_pct(envruns[e]['wins'][k] / n) for e in (0.0, 3.0, 6.0, 13.0))))
    w('\nExpected Republican-held seats won: ' + '; '.join('%s %.1f' % (lab, sum(envruns[e]['wins'][k] for k in RACES if RACES[k]['p'] == 'R') / n)
                                                         for lab, e in (('neutral', 0.0), ('D+3', 3.0), ('D+6', 6.0), ('D+13', 13.0))) + '.\n')
    w('## 7. Sensitivity (D+3, mean seats and P(≥55))\n')
    w('| Change | Mean seats | P(≥55) | P(≥60) | P(D control) |')
    w('| --- | --- | --- | --- | --- |')
    for label, prm, unc in [
        ('Base', {}, {}),
        ('2026 weight 0.15', {'w26': 0.15}, {}), ('2026 weight 0.45', {'w26': 0.45}, {}),
        ('Incumbency 1.0', {'inc': 1.0}, {}), ('Incumbency 3.5', {'inc': 3.5}, {}),
        ('Carry-over 0.2', {'shrink': 0.2}, {}), ('Carry-over 0.6', {'shrink': 0.6}, {}),
        ('Race error 4', {'sd_race': 4.0}, {}), ('Race error 6', {'sd_race': 6.0}, {}),
        ('Regional error 1.5', {'sd_reg': 1.5}, {}), ('Regional error 3.5', {'sd_reg': 3.5}, {}),
        ('AK and MS 2026 both R', {}, {'AK-2026': 0.0, 'MS-2026': 0.0}),
        ('AK and MS 2026 both D', {}, {'AK-2026': 1.0, 'MS-2026': 1.0}),
        ('MN 2027 special lost', {}, {'MN-2027': 0.0}),
        ('Electoral College bias 0', {'ec_bias': 0.0}, {}), ('Electoral College bias 3', {'ec_bias': 3.0}, {}),
        ('Governor incumbency 5, weight 1.0', {'inc_gov': 5.0, 'gov_w': 1.0}, {}),
    ]:
        s = summarize(simulate_2028(3.0, n=n // 2, seed=5, prm=prm, uncertain=unc))
        w('| %s | %.1f | %s | %s | %s |' % (label, s['mean'], fmt_pct(s['p55']), fmt_pct(s['p60']), fmt_pct(s['ctrl'])))
    w('\n## 8. Control through 2033: the 2030 and 2032 classes\n')
    for label, e, cond, stip in (('Evidence-weighted prior, Democratic president elected in 2028', 3.0, 'D', False),
                                 ('D1 stipulation: Democratic president 2029-2037', 3.0, None, True),
                                 ('Near-neutral 2028 (SD 2), Democratic president', 0.0, 'D', False)):
        res = simulate_chain(e, n=n, env_sd=4.5 if e == 3.0 else 2.0, stipulate=stip)
        m, rows, thru = chain_table(res, cond)
        w('**%s** (%d runs)\n' % (label, m))
        w('| After the election of | Seated | Mean D seats | P(≥50) | P(≥51) | P(≥55) | P(60+) |')
        w('| --- | --- | --- | --- | --- | --- | --- |')
        for (lab, mean, a, b, c, d), yr in zip(rows, (2028, 2030, 2032)):
            w('| %d | %s | %.1f | %s | %s | %s | %s |' % (yr, lab, mean, fmt_pct(a), fmt_pct(b), fmt_pct(c), fmt_pct(d)))
        w('\nHeld in every Congress from January 2029 (50+ / 55+ / 60+): the 2029-30 Congress %s / %s / %s; '
          'through the 2031-32 Congress %s / %s / %s; through the 2033-34 Congress %s / %s / %s.\n' % tuple(fmt_pct(x) for t in thru for x in t))
    mt = MIDTERM_SWINGS
    w('Midterm swing against the president\'s party (1990-2026): mean %.1f, SD %.1f points. '
      'Presidential-year drift SD %.1f.\n' % (st.mean(mt), st.stdev(mt), st.stdev([b - a for a, b in zip(PRES_MARGINS, PRES_MARGINS[1:])])))
    return '\n'.join(L) + '\n'


# --------------------------------------------------------------------------------------------------
# 9. Round 4: the D2-F whip count, the Minnesota 2027 special, and the 2032 levers
# --------------------------------------------------------------------------------------------------
# P(a senator votes against graduated cloture, D2-F) — ASSUMPTIONS anchored on public statements where found:
# Fetterman now defends the filibuster ("horribly wrong" to have opposed it, July 2026) [SRC-0595]; Hamilton
# (KS) would keep the 60-vote threshold and Cooper (NC) has praised it as a firewall against "bad
# legislation" [SRC-0596]; Talarico [SRC-0597] and Stratton favor ending it. Every Democrat then serving
# except Manchin and Sinema voted on January 19, 2022 to change the rule for voting-rights bills [SRC-0598];
# 35 of them sit in the 2027 caucus, and get 0.02-0.10. Others are judgment calls by state and stated
# profile; unknown red-state freshmen get 0.25-0.40.
WHIP_C1 = {'AZ': 0.10, 'CA': 0.05, 'CT': 0.03, 'DE': 0.05, 'HI': 0.03, 'ME': 0.05, 'MD': 0.05, 'MA': 0.02,
           'MI': 0.15, 'MN': 0.10, 'NV': 0.05, 'NJ': 0.05, 'NM': 0.03, 'NY': 0.03, 'RI': 0.03, 'VT': 0.02,
           'VA': 0.05, 'WA': 0.03, 'WI': 0.03}
WHIP_C2 = {'TX': 0.02, 'NC': 0.60, 'SC': 0.35, 'KS': 0.85, 'IA': 0.30, 'ME': 0.25, 'GA': 0.03, 'MI': 0.05,
           'NH': 0.15, 'MN': 0.03, 'IL': 0.02, 'VA': 0.08, 'NJ': 0.03, 'NM': 0.03, 'CO': 0.10, 'OR': 0.02,
           'DE': 0.10, 'MA': 0.02, 'RI': 0.05, 'MS': 0.40, 'AK': 0.35}
WHIP_C3 = {'AZ': 0.10, 'CA': 0.03, 'CO': 0.05, 'CT': 0.03, 'GA': 0.03, 'HI': 0.02, 'IL': 0.03, 'MD': 0.03,
           'NV': 0.08, 'NH': 0.10, 'NY': 0.05, 'OH': 0.05, 'OR': 0.03, 'PA': 0.68, 'VT': 0.05, 'WA': 0.03,
           # pickups of Republican-held seats: new senators from Trump-won states
           'NC': 0.25, 'WI': 0.20, 'IA': 0.30, 'FL': 0.30, 'AK': 0.40, 'KS': 0.40, 'TN*': 0.40}
WHIP_OTHER = 0.35   # any other pickup
WHIP_NAMED = {('C3', 'PA'), ('C2', 'KS'), ('C2', 'NC')}   # positions on record; not scaled in the sensitivity
EXPOSED32 = {s: 2.0 for s in ('MS', 'SC', 'KS', 'IA', 'AK', 'TX')}


def whip_d2f(o, seed=11, scale=1.0):
    """For each 2028 run: (seats, opponents of D2-F among Democrats, D president). Returns lists."""
    rng = random.Random(seed)
    out = []
    for i in range(o['n']):
        dr = o['draws'][i]
        opp = 0
        for s, p in WHIP_C1.items():
            if s == 'MN' and not dr['MN-2027']:
                continue
            opp += rng.random() < min(1.0, p * scale)
        for s, p in WHIP_C2.items():
            if (s == 'AK' and not dr['AK-2026']) or (s == 'MS' and not dr['MS-2026']):
                continue
            opp += rng.random() < (p if ('C2', s) in WHIP_NAMED else min(1.0, p * scale))
        for k in o['dwon'][i]:
            p = WHIP_C3.get(k, WHIP_OTHER)
            opp += rng.random() < (p if ('C3', k) in WHIP_NAMED else min(1.0, p * scale))
        out.append((o['seats'][i], opp, o['dpres'][i]))
    return out


def d2f_summary(o, cond='D', seed=11, scale=1.0):
    rows = [r for r in whip_d2f(o, seed, scale) if cond is None or r[2] == (cond == 'D')]
    m = len(rows)
    passes = sum(1 for s, opp, dp in rows if s - opp >= (50 if dp else 51)) / m
    return dict(n=m, opp=st.mean(r[1] for r in rows), margin=st.mean(r[0] - (50 if r[2] else 51) for r in rows),
                p_pass=passes, p_opp_ge5=sum(1 for r in rows if r[1] >= 5) / m)


def p_mn_2027(e27, prm=BASE_PARAMS, appointee=1.0):
    """P(Democrats hold Klobuchar's seat in the November 2027 special) at a national environment e27."""
    sd = math.sqrt(prm['sd_race'] ** 2 + prm['sd_open'] ** 2 + prm['sd_reg'] ** 2 + prm['sd_nat'] ** 2)
    m = lean('MN', prm) + e27 + appointee
    return 0.5 * (1 + math.erf(m / sd / math.sqrt(2)))


def report_round4(n=20000):
    L = []
    w = L.append
    w('## 9. Round 4: Minnesota\'s 2027 special\n')
    w('Minnesota lean %+.1f (2020 D+7.1, 2024 D+4.2, 2026 Senate D+10.1 open). P(Democrats hold) by the 2027 '
      'national environment, with an appointee running as a weak incumbent (+1):\n' % lean('MN'))
    w('| 2027 environment | R+3 | Even | D+3 | D+8 | D+13 |')
    w('| --- | --- | --- | --- | --- | --- |')
    w('| P(D) | ' + ' | '.join(fmt_pct(p_mn_2027(e)) for e in (-3, 0, 3, 8, 13)) + ' |')
    w('\nWhat losing it does to January 2029 (mean seats, P(≥55), P(D control)):\n')
    w('| Environment | Minnesota held | Minnesota lost |')
    w('| --- | --- | --- |')
    for label, e, sd in (('Neutral', 0.0, 0.0), ('D+3', 3.0, 0.0), ('D+6', 6.0, 0.0), (PRIOR[0], 3.0, 4.5)):
        a = summarize(simulate_2028(e, n=n // 2, seed=21, env_sd=sd, uncertain={'MN-2027': 1.0}))
        b = summarize(simulate_2028(e, n=n // 2, seed=21, env_sd=sd, uncertain={'MN-2027': 0.0}))
        w('| %s | %.1f; %s; %s | %.1f; %s; %s |' % (label, a['mean'], fmt_pct(a['p55']), fmt_pct(a['ctrl']),
                                                   b['mean'], fmt_pct(b['p55']), fmt_pct(b['ctrl'])))
    w('\n## 10. Round 4: the D2-F whip count against the Senate\n')
    w('Opponents drawn per run from the whip table in the script (assumptions anchored on public statements); '
      'D2-F passes if Democratic seats minus opponents reach 50 with a Democratic Vice President (51 without).\n')
    w('| Environment | Mean seats | Mean opponents | Mean margin before defections | P(5+ opponents) | P(D2-F has the votes) |')
    w('| --- | --- | --- | --- | --- | --- |')
    for label, e, sd, cond in (('Neutral, Democratic president', 0.0, 0.0, 'D'), ('D+3, Democratic president', 3.0, 0.0, 'D'),
                               ('D+6, Democratic president', 6.0, 0.0, 'D'), (PRIOR[0] + ', Democratic president', 3.0, 4.5, 'D')):
        o = simulate_2028(e, n=n // 2, seed=31, env_sd=sd)
        s = d2f_summary(o, cond)
        w('| %s | %.1f | %.1f | %.1f | %s | %s |' % (label, summarize(o, cond)['mean'], s['opp'], s['margin'],
                                                    fmt_pct(s['p_opp_ge5']), fmt_pct(s['p_pass'])))
    o = simulate_2028(3.0, n=n // 2, seed=31, env_sd=4.5)
    w('\nSensitivity (evidence-weighted, Democratic president): unnamed senators\' probabilities halved, P(votes) %s '
      '(mean opponents %.1f); doubled, %s (%.1f). Fetterman, Hamilton and Cooper are held at their stated positions.\n' % (
          fmt_pct(d2f_summary(o, 'D', scale=0.5)['p_pass']), d2f_summary(o, 'D', scale=0.5)['opp'],
          fmt_pct(d2f_summary(o, 'D', scale=2.0)['p_pass']), d2f_summary(o, 'D', scale=2.0)['opp']))
    w('\n## 11. Round 4: what drives the 2032 drop, and what would change it\n')
    w('Evidence-weighted prior, Democratic president elected in 2028. Each Democratic-held Class 2 seat: '
      'P(held in 2032), and its share of all Democratic 2032 losses.\n')
    base = simulate_chain(3.0, n=n, env_sd=4.5)
    w('| Seat | P(held) | Share of losses | Expected loss |')
    w('| --- | --- | --- | --- |')
    for s, ph, share, el in drivers_2032(base)[:10]:
        w('| %s | %s | %s | %.2f |' % (s, fmt_pct(ph), fmt_pct(share), el))
    w('\nLevers (same runs; held 50+ means in every Congress through 2033-34):\n')
    w('| Lever | Mean seats Jan 2031 | Mean seats Jan 2033 | P(≥50) Jan 2033 | Held 50+ through 2033-34 | Held 55+ through 2033-34 |')
    w('| --- | --- | --- | --- | --- | --- |')
    levers = [
        ('Base', {}),
        ('Mild 2030 midterm (half the usual penalty)', {'midterm': (st.mean(MIDTERM_SWINGS) / 2, st.stdev(MIDTERM_SWINGS))}),
        ('Every 2026 winner runs again (no Class 2 retirements)', {'c2_retire': 0.0}),
        ('Retention: 2026 winners keep 60% of their overperformance', {'c2_shrink': 0.6}),
        ('Candidate and campaign strength: +2 points in the six most exposed seats', {'c2_bonus': EXPOSED32}),
        ('D.C. statehood, seated January 2031', {'statehood': 'DC', 'statehood_from': 2031}),
        ('D.C. and Puerto Rico, seated January 2031', {'statehood': 'DC+PR', 'statehood_from': 2031}),
        ('D.C. and Puerto Rico, seated January 2033', {'statehood': 'DC+PR', 'statehood_from': 2033}),
        ('D.C. and Puerto Rico 2031, a mild midterm and +2 in the exposed seats',
         {'statehood': 'DC+PR', 'statehood_from': 2031, 'c2_bonus': EXPOSED32,
          'midterm': (st.mean(MIDTERM_SWINGS) / 2, st.stdev(MIDTERM_SWINGS))}),
    ]
    for label, kw in levers:
        res = simulate_chain(3.0, n=n, env_sd=4.5, **kw)
        m, rows, thru = chain_table(res, 'D')
        w('| %s | %.1f | %.1f | %s | %s | %s |' % (label, rows[1][1], rows[2][1], fmt_pct(rows[2][2]),
                                                  fmt_pct(thru[2][0]), fmt_pct(thru[2][1])))
    return '\n'.join(L) + '\n'


def joint(env, n, overrides, seats, seed=77):
    """P(Democrats win every seat in `seats`) at environment env."""
    prm = dict(BASE_PARAMS)
    rng = random.Random(seed)
    base_m = {k: lean(state_of(k), prm) + (overrides or {}).get(k, 0.0) for k in seats}
    hits = 0
    regions = sorted(REGION)
    for _ in range(n):
        pres = env + rng.gauss(0, prm['sd_nat'])
        tick = rng.gauss(0, prm['sd_tick'])
        reg = {r: rng.gauss(0, prm['sd_reg']) for r in regions}
        ok = True
        for k in seats:
            r = RACES[k]
            runs = rng.random() < r.get('p_run', 1.0)
            sd = prm['sd_race'] if runs else math.hypot(prm['sd_race'], prm['sd_open'])
            m = base_m[k] + pres + tick + reg[REGION_OF[state_of(k)]] + (candidate_effect(k) if runs else 0) + rng.gauss(0, sd)
            ok = ok and m > 0
        hits += ok
    return hits / n


if __name__ == '__main__':
    text = report() + '\n' + report_round4()
    if '--write' in sys.argv:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'senate-model-outputs.md')
        with open(path, 'w') as f:
            f.write(text)
        print('wrote', os.path.normpath(path))
    else:
        print(text)
