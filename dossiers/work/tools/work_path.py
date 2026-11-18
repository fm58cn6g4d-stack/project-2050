#!/usr/bin/env python3
"""The work flagship's lines on federal fiscal years, FY2030-40.

Role: section 6's path (`dossiers/work/6-cost.md`). Status: draft (stage F). Project
arithmetic on the anchors in sections 3 to 5 and the memos, as decided in
DEC-2026-11-17-01 to -36, -95 and -96; not a score. Nothing here is booked.
Run:  python3 dossiers/work/tools/work_path.py            (tables in Markdown)
      python3 dossiers/work/tools/work_path.py --check    (coverage and sum checks)
      python3 dossiers/work/tools/work_path.py --booking-scenario [--apply <copy root>]
                                                          (section 7 part 1C's model rows)
      python3 dossiers/work/tools/work_path.py --ui-options
                                  (the UI standard's options for Espen, 6-cost.md)
Revised in the milestone review's fix step 1: the UI trust-fund line is derived from
LAB-11.01's standard (ui_factors), wage insurance from its chain (wi_steady, wi_ramp),
and the AmeriCorps grantees' match is reported as a non-federal line.

Conventions (6-cost.md, "Counting rules"):
  * nominal $ billion, federal cost against the January 2029 law, a cost positive;
  * FY y runs from October of y-1; a calendar-year amount CY y lands 0.75 in FY y and
    0.25 in FY y+1 (as care's, health's and the secure floor's paths count);
  * every line has a central, low and high path; ranges are bounds summed line by line,
    not probability intervals, and the lines are not independent;
  * each line carries a `basis` (where it sits): general-fund spending, a revenue effect,
    the indirect effect of the wage floor (CBO's net of spending and revenue), the UI trust
    funds, Social Security (off budget), non-federal money (`nonfed`, reported only),
    agency capacity (CAP-7, democratic renewal's booked lines), and a `kind`: firm, contingent (zero unless an event or a gate occurs)
    or provisional (drafted on the recommendation, for Espen).
Growth and anchors are labeled judgment (DEC-2026-11-10-07); each line's basis is in its
comment and in 6-cost.md.
"""
import json
import os
import sys

YEARS = list(range(2030, 2041))
WINDOW = list(range(2030, 2040))
HERE = os.path.dirname(os.path.abspath(__file__))
PROVISIONS = os.path.join(HERE, "..", "provisions.json")

WAGE_G = 0.035   # nominal wage growth (section 4 uses 3.5% median growth)
PRICE_G = 0.025  # prices, for appropriated amounts and AmeriCorps' cost rules
UI_G = 0.04      # UI benefits: wages plus labor force

# Booked in the budget model, case `mixed` (legacy/sources/recovery-budget-audit.csv,
# column primary_deficit_change_bn), on main at f56c052, FY2030-40.
BOOKED = {
    "LAB-5": [0.0, 15.2, 15.7, 16.3, 16.9, 17.6, 18.2, 0, 0, 0, 0],
    "LAB-8": [1.3, 2.7, 2.8, 2.9, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 3.8],
    "LAB-9": [2.9, 6.0, 9.4, 13.0, 13.5, 14.0, 14.5, 15.0, 15.6, 16.2, 16.8],
    "AI-4": [0.0, 7.0, 14.6, 22.7, 23.6, 24.5, 25.4, 26.4, 27.4, 28.4, 29.5],
}
PLAN_GAP_FY2040 = 602.6884200832942   # agenda_gf_primary_bn, case mixed, FY2040
GDP_FY2040 = 54167.0                  # gdp_bn, case mixed, FY2040


def cy_to_fy(cy):
    """Calendar-year amounts to fiscal years: FY y = 0.75 CY y + 0.25 CY y-1."""
    return [0.75 * cy.get(y, 0.0) + 0.25 * cy.get(y - 1, 0.0) for y in YEARS]


def grow(base, base_year, g, start, end=2040):
    return {y: base * (1 + g) ** (y - base_year) for y in range(start, end + 1)}


def scale(path, f):
    return [v * f for v in path]


# ---------------------------------------------------------------------------------
# The lines. Each: id, label, provisions, basis, kind, central/low/high FY2030-40.
# ---------------------------------------------------------------------------------
LINES = []


def line(lid, label, provisions, basis, kind, central, low, high, vehicle, note):
    LINES.append(dict(id=lid, label=label, provisions=provisions, basis=basis, kind=kind,
                      central=central, low=low, high=high, vehicle=vehicle, note=note))


# 1. The wage floor's indirect budget effect (memo 1 B): CBO's net of spending and revenue.
# CBO: +$54B over 2021-31 for $15 by 2025, about 61% of 2025's median [EV-WRK-032]
# [EV-WRK-078]; memo 1 B's $17 is about half the median in 2035. Shape follows the steps
# (2030-35) and the bite; about $5.5B in FY2040 (section 3: $3-8B; 0 to +$0.08T).
_floor = [0.3, 0.8, 1.5, 2.3, 3.2, 4.0, 4.6, 4.9, 5.1, 5.3, 5.5]
line("floor", "The wage floor's indirect effect on the budget (CBO's net method)",
     ["LAB-4.01", "LAB-4.02", "LAB-4.03", "LAB-4.06", "LAB-4.07", "LAB-4.08"],
     "indirect", "firm", _floor, [0.0] * 11,
     [v * 80 / sum(_floor[:10]) for v in _floor[:10]] + [8.0],
     "Labor act", "Scaled from CBO's 2021 score; spending and revenue together")

# 2. The small-business credit (LAB-5.01), bottom-up. Each step's added wage cost at
# employers under 50 workers, for the four quarters after the step (CY, $B): step 1
# ($9.50) about $1.0B, step 2 ($11.00) $3.5B, step 3 ($12.50) $6.0B (judgment: workers
# below each step in the states still at $7.25, about 40% of them at small employers),
# times 50%, 35% and 20%. Claimed on the quarterly Form 941, so CY->FY.
_credit_cy = {2030: 0.5 * 1.0, 2031: 0.35 * 3.5, 2032: 0.20 * 6.0}
_credit = cy_to_fy(_credit_cy)
line("credit", "Small-business transition credit, first three steps (revenue effect)",
     ["LAB-5.01"], "revenue", "firm", _credit, scale(_credit, 0.5), scale(_credit, 2.5),
     "R1 (contingent on the labor act's steps)",
     "Tax credit; the trust funds held harmless by general-fund transfer")

# 3. The 14(c) transition grant (LAB-4.09): $1-3B over five years, FY2030-34.
line("14c", "14(c) transition grant to VR and developmental disability agencies", ["LAB-4.09"],
     "gf", "firm", [0.4] * 5 + [0.0] * 6, [0.2] * 5 + [0.0] * 6, [0.6] * 5 + [0.0] * 6,
     "R1", "Section 4: $1-3B over five years")

# 4. Standards boards office and the wage commission (LAB-3.01-3.04, LAB-4.04):
# commission staff about $15M; boards office 100-200 staff at about $0.25M each; about
# $5-10M a year for each board's hearings, one board in 2030 rising to about ten by the
# late 2030s (judgment). Appropriated.
_boards = [0.05, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.14, 0.15]
line("boards", "Standards boards office and the wage commission",
     ["LAB-3.01", "LAB-3.02", "LAB-3.04", "LAB-4.04"], "gf_disc", "firm", _boards,
     scale(_boards, 0.6), [v * 3.0 / sum(_boards[:10]) for v in _boards[:10]] + [0.4],
     "Labor act; annual appropriations", "Section 3: $1-3B and $0.2-0.4B in FY2040")

# 5. Outreach grants (LAB-7.05): about $50M a year from FY2030, indexed.
_outreach = [0.05 * (1 + PRICE_G) ** (y - 2030) for y in YEARS]
line("outreach", "Wage and safety outreach grants", ["LAB-7.05"], "gf_disc", "firm",
     _outreach, scale(_outreach, 0.5), scale(_outreach, 2.0), "Annual appropriations",
     "Section 4's working assumption")

# 6. Unemployment insurance, the trust funds' side (LAB-11.01-11.03, 11.07), derived from
# LAB-11.01's standard (milestone review O-1). Regular state benefits today are about
# $38B a year at FY2025 levels: OMB's $41.8B for subfunction 603 [EV-WRK-413] less about
# $3-4B of state administration [EV-WRK-309] and federal workers' and veterans' benefits
# that the subfunction also carries (judgment for the second part); DOL's third quarter of
# 2026, $9.2B, a seasonally light quarter, is consistent [EV-WRK-451]. The standard
# multiplies them by four factors (bounds in brackets, all judgment unless tagged):
#  (1) replacement: the weekly benefit becomes 75% of high-quarter weekly pay, capped at
#      two-thirds of the state average weekly wage (SAWW). Recipients' benefits replace
#      43% of their wages today [EV-WRK-302]; at a $491 average weekly benefit
#      [EV-WRK-451] that puts their wage near 0.72 of SAWW ($1,142 against about $1,550-
#      1,640 [EV-WRK-453]). With recipients' wages lognormal around that mean (log-sd 0.5
#      [0.4-0.6]) and high-quarter pay 1.05 times average weekly pay [1.0-1.15], the
#      average replacement becomes about 68% [63-75%], about 1.58 times today's;
#  (2) more claimants, from part-time coverage, the $1,000 / $1,500 test, the latest
#      quarter, ABC coverage and compelling-reason quits: first payments +20% [10-25%];
#      the 2009 modernization incentives moved them 6-10% at most [EV-WRK-377]. New
#      claimants earn less, so each draws about 70% [60-80%] of the average benefit;
#  (3) the 26-week floor in the 16 states that pay fewer weeks [EV-SEC-048], about a tenth
#      of today's weeks: weeks +4% [3-6%];
#  (4) longer claims as benefits rise: a duration elasticity of 0.25 [0.1-0.38], between
#      the pandemic-era 0.06-0.22 [EV-WRK-370] and the pre-pandemic U.S. median of 0.38
#      [EV-WRK-368].
# Weekly recipients rise about 1.4 times: recipiency from 29% toward 40%, memo 7's figure.
# Benefits rise about 2.1 times: about +$42B a year at FY2025 levels, from benefit weeks
# beginning January 1, 2031; grown 4% a year (ui_factors() prints the factors).
UI_BASE_FY2025 = 38.0


def _ui_replacement(rate=0.75, cap=2 / 3, mean=0.72, sigma=0.5, hq=1.05):
    """Average replacement of recipients' wages under min(rate x high-quarter pay, cap x SAWW)."""
    from math import exp, log
    from statistics import NormalDist
    nd = NormalDist()
    a = rate * hq
    mu = log(mean) - sigma ** 2 / 2
    t = (log(cap / a) - mu) / sigma
    return (a * exp(mu + sigma ** 2 / 2) * nd.cdf(t - sigma) + cap * (1 - nd.cdf(t))) / mean


UI_CASES = {  # replacement inputs; more claimants and their benefit weight; floor; elasticity
    "central": dict(sigma=0.5, hq=1.05, claims=0.20, weight=0.70, floor=0.04, elast=0.25),
    "low": dict(sigma=0.6, hq=1.0, claims=0.10, weight=0.60, floor=0.03, elast=0.10),
    "high": dict(sigma=0.4, hq=1.15, claims=0.25, weight=0.80, floor=0.06, elast=0.38),
}


def ui_factors(case="central", rate=0.75):
    """(replacement, its ratio to today's 43%, benefit multiplier, weekly-recipient multiplier)."""
    from math import exp, log
    c = UI_CASES[case]
    rep = _ui_replacement(rate, sigma=c["sigma"], hq=c["hq"])
    r = rep / 0.43
    dur = (1 + c["floor"]) * exp(c["elast"] * log(r))
    return rep, r, r * (1 + c["claims"] * c["weight"]) * dur, (1 + c["claims"]) * dur


def ui_increase(case="central", rate=0.75):
    """Added regular benefits a year at FY2025 levels, $B."""
    return UI_BASE_FY2025 * (ui_factors(case, rate)[2] - 1)


def _tf(level):
    return cy_to_fy(grow(level, 2025, UI_G, 2031))


_UI = {w: ui_increase(w) for w in ("central", "low", "high")}
_R = {w: ui_factors(w)[1] for w in ("central", "low", "high")}
line("ui_tf", "UI regular benefits from the state trust funds (employer-financed)",
     ["LAB-11.01", "LAB-11.02", "LAB-11.03", "LAB-11.07"], "trust", "firm",
     _tf(_UI["central"]), _tf(_UI["low"]), _tf(_UI["high"]),
     "R1 (conditions on the FUTA credit)",
     "Matched by employers' state UI taxes over the cycle")
line("ui_tax", "Employers' state UI taxes on the larger base (receipts, matching the benefits)",
     ["LAB-11.05"], "trust", "firm", scale(_tf(_UI["central"]), -1),
     scale(_tf(_UI["high"]), -1), scale(_tf(_UI["low"]), -1), "R1",
     "Inside the trust funds; sign negative. The cycle average: in any one year states "
     "build or draw down reserves, so the two lines match over the cycle, not each year")

# 7. Extended Benefits at 100% federal with the new triggers (LAB-11.04), on the budget
# model's basis (no recession in the projection): the states whose own three-month rate
# sits near 5.5% in ordinary years trigger on part of the time (judgment). About $3.0B in
# CY2031 (range $1.0-6.0B), growing 4%: OMB scored the FY2017 budget's Extended Benefits
# reform (fully federal, new triggers) at $36.7B over 2017-26 on a path with no
# recession [EV-WRK-438], about $3.7B a year. That $3.0B is at today's weekly benefits;
# each Extended Benefits week pays the regular weekly amount, so the line is scaled by the
# standard's replacement factor (about 1.58, range 1.46-1.75; line 6). The number of
# weeks is held (judgment: more claimants and the 26-week floor roughly offset in who
# reaches Extended Benefits).
_eb0 = cy_to_fy(grow(3.0, 2031, UI_G, 2031))
_eb = scale(_eb0, _R["central"])
line("eb", "Extended Benefits, federal share, ordinary years", ["LAB-11.04"], "gf", "firm",
     _eb, scale(_eb0, _R["low"] / 3.0), scale(_eb0, 2.0 * _R["high"]), "R1",
     "No recession, as in CBO's projection; a downturn is the contingent line")
# A moderate two-year downturn: about two million exhaustees a year at about 30 weeks, at
# about $1,000-1,150 a week in the mid-to-late 2030s on the standard's benefit levels (project
# arithmetic: $491 in 2026 [EV-WRK-451] times about 1.58, grown with wages): about $60B a
# year, $120B over the downturn, more in a deeper one (judgment).
line("eb_recession", "Extended Benefits in one moderate two-year downturn (contingent)",
     ["LAB-11.04"], "gf", "contingent", [0.0] * 11, [0.0] * 11,
     [0.0] * 5 + [0.0, 0.0, 60.0, 60.0, 0.0, 0.0], "R1",
     "Zero in the projection; up to about $120B if a downturn falls in the window")

# 8. State UI administration (LAB-11.06, 11.08): the floor restores about $0.38B a year
# above FY2026's $2.76B [EV-WRK-309] [EV-WRK-308], indexed; plus the larger program's
# workload above the floor, about $0.4B a year from 2031 (range $0.2-0.8B; judgment).
# Workload follows claims and weeks, not the benefit's size: weekly recipients rise about
# 1.4 times on line 6's factors (1.2-1.6), the 40% this line was sized on, so it stands.
_admin_floor = [0.38 * (1 + PRICE_G) ** (y - 2026) for y in YEARS]
_admin_work = [0.0] + cy_to_fy(grow(0.4, 2031, UI_G, 2031))[1:]
_admin = [a + b for a, b in zip(_admin_floor, _admin_work)]
line("ui_admin", "State UI administration: the floor and the larger program's workload",
     ["LAB-11.06", "LAB-11.08"], "gf_disc", "firm", _admin,
     [a + 0.5 * b for a, b in zip(_admin_floor, _admin_work)],
     [a + 2.0 * b for a, b in zip(_admin_floor, _admin_work)],
     "Annual appropriations (the FUTA-financed administration account)",
     "Counted on the general fund, the cautious reading, as memo 7 did")

# 9. The conformity and systems grant (LAB-11.09): $1-2B over FY2030-32.
line("conformity", "UI conformity and systems grant", ["LAB-11.09"], "gf", "firm",
     [0.5, 0.5, 0.5] + [0.0] * 8, [1 / 3] * 3 + [0.0] * 8, [2 / 3] * 3 + [0.0] * 8, "R1",
     "Section 5: 53 jurisdictions at about $20-40M each")

# 10. Hours in quarterly wage records (LAB-18.06, way iii; decided): the hours part of
# the one-time grant for the new fields, FY2031-33.
line("hours", "Hours in state wage records, one-time grant", ["LAB-18.06"], "gf", "firm",
     [0.0, 0.05, 0.1, 0.05] + [0.0] * 7, [0.0, 0.03, 0.05, 0.02] + [0.0] * 7,
     [0.0, 0.1, 0.2, 0.1] + [0.0] * 7, "R1", "Section 5's $0.2-0.5B, less occupation's part")

# 11. Wage insurance benefits (LAB-18.01-18.05, 18.07): separations from January 1, 2031;
# payments start on reemployment within 12 months and run up to two years. The chain
# (milestone review O-2; each step judgment unless tagged):
#   about 1.1M long-tenured workers displaced a year [EV-WRK-315] (layoffs only: plant
#   closings, slack work, abolished positions);
#   x 1.15 for long-tenured discharges not for misconduct, which LAB-18.03 makes eligible
#   and the displacement survey does not count (range 1.05-1.30: no register entry counts
#   them; misconduct is the narrow willful standard [EV-WRK-416]);
#   x 0.88 under the pay cap; x 0.6 reemployed within a year (66.1% by the survey date
#   [EV-WRK-315]); x 0.5 paid less [EV-WRK-317]; x 0.6 take-up with the automatic offer
#   -> about 0.20M new recipients a year; x 1.6 years each -> about 0.32M on the rolls;
#   x about $6,250 a year in 2033 ($6,000-6,500) -> about $2.0B a year in steady state.
# The ramp is built from the cohorts (wi_ramp()). The path grows about 3% a year: wages
# (WAGE_G) plus the labor force (0.5%), less about 1% as more payments reach the $10,000
# cap, which is fixed until the commission's 2035 report (LAB-18.02); indexing it then
# would raise growth toward 4% (not assumed).
WI_CHAIN = dict(displaced=1.1, discharge=1.15, under_cap=0.88, reemployed=0.6, lower=0.5,
                takeup=0.6, years=1.6, pay_2033=6.25)
WI_G = WAGE_G + 0.005 - 0.01


def wi_steady(chain=WI_CHAIN):
    """(new recipients a year, on the rolls, $B a year at 2033 payment levels)."""
    c = chain
    new = c["displaced"] * c["discharge"] * c["under_cap"] * c["reemployed"] * c["lower"] \
        * c["takeup"]
    return new, new * c["years"], new * c["years"] * c["pay_2033"]


def wi_ramp():
    """Share of the steady-state rolls paid in each FY2030-40, from monthly cohorts:
    separations from January 2031, reemployment spread evenly over 12 months, payments
    lasting 1.2 to 2.0 years (1.6 on average)."""
    m0 = 2031 * 12  # January 2031, in months
    durs = [14.4 + 9.6 * (k + 0.5) / 8 for k in range(8)]  # 1.2-2.0 years, in months
    flow = {}
    for m in range(2029 * 12, 2041 * 12):
        on = 0.0
        for s in range(m0, m + 1):          # separation month
            for u in range(12):             # months to reemployment
                start = s + u + 1
                on += sum(1.0 for d in durs if start <= m < start + d) / len(durs) / 12
        flow[m] = on / (WI_CHAIN["years"] * 12)   # share of steady-state rolls
    out = []
    for y in YEARS:  # FY y: October y-1 to September y
        out.append(sum(flow[m] for m in range((y - 1) * 12 + 9, y * 12 + 9)) / 12)
    return [v / out[-1] for v in out]  # whole months round durations up; steady state = 1


_wi_ss = wi_steady()[2]
_wi = [s * _wi_ss * (1 + WI_G) ** (y - 2033) for s, y in zip(wi_ramp(), YEARS)]
line("wi", "Wage insurance benefits", ["LAB-18.01", "LAB-18.02", "LAB-18.04", "LAB-18.05",
                                       "LAB-18.07"],
     "gf", "firm", _wi, scale(_wi, 0.5), scale(_wi, 1.6), "R1",
     "Memo 8 B's $2-4B a year, re-derived with take-up and the 12-month window")

# 12. Wage insurance administration (LAB-18.06's employer route, 18.08's statement):
# about 10% of benefits (8-12%), on the state UI administration ratio [EV-WRK-309]
# [EV-WRK-413], plus about $0.15B of set-up in FY2030 and FY2031. Not inside memo 8's
# $2-4B, which counted payments only.
_wi_admin = [0.15, 0.15 + 0.1 * _wi[1]] + [0.1 * v for v in _wi[2:]]
line("wi_admin", "Wage insurance administration, including the monthly statement",
     ["LAB-18.08"], "gf", "firm", _wi_admin,
     [0.1, 0.1 + 0.08 * _wi[1] * 0.5] + [0.08 * v * 0.5 for v in _wi[2:]],
     [0.2, 0.2 + 0.12 * _wi[1] * 1.6] + [0.12 * v * 1.6 for v in _wi[2:]], "R1",
     "Section 5's new line; the statement itself is LAB-18.08 (provisional)")

# 13. Apprenticeship grants (LAB-8.01-8.07): new starts rise from 311,035 (FY2025)
# [EV-WRK-349], held there through FY2029, to 600,000 by FY2034 (LAB-8.04), then grow
# 0.5% a year. Funded starts: the four sectors' share of today's starts (about 55%,
# judgment) plus 90% of the growth. Up to $12,000 (2030 dollars, indexed): $4,000 in the
# year of the start, $4,000 the next year for the about 75% still in training, $4,000 at
# completion three years on for the about 45% who complete [EV-WRK-350]; less about 2%
# for care training already paid by HLT-10.06 (LAB-8.07).
def _apprenticeship(per=12.0, share=0.55, growth_share=0.9, retain=0.75, complete=0.45):
    starts = {}
    for y in range(2027, 2041):
        if y < 2030:
            total = 311.035
        elif y <= 2034:
            total = 311.035 + (600 - 311.035) * (y - 2029) / 5
        else:
            total = 600 * 1.005 ** (y - 2034)
        starts[y] = share * 311.035 + growth_share * (total - 311.035) if y >= 2030 else 0.0
    out = []
    for y in YEARS:
        idx = (1 + PRICE_G) ** (y - 2030)
        third = per / 3
        v = starts[y] * third + starts.get(y - 1, 0) * third * retain \
            + starts.get(y - 3, 0) * third * complete
        out.append(v * idx / 1000 * 0.98)
    return out


_app = _apprenticeship()
line("apprenticeship", "Apprenticeship grants: instalments, completion, instructors, supports",
     ["LAB-8.01", "LAB-8.02", "LAB-8.03", "LAB-8.04", "LAB-8.06", "LAB-8.07"], "gf", "firm",
     _app, scale(_app, 0.7), scale(_app, 1.6), "R1",
     "Memo 8 C's $4-7B a year at full scale, re-derived with attrition and the ramp")

# 14. National service, civic positions (LAB-9.01, 9.02, 9.04-9.06): 30,000 more a year
# from FY2030 to 150,000 in FY2034. Federal cost per position: AmeriCorps' $25,200 per
# member service year (FY2026, indexed) [EV-WRK-398], plus the education award at the
# maximum Pell grant, $7,395, flat in nominal terms as the baseline holds it
# [EV-WRK-399], plus about 5% for child care and the agency (judgment).
def _civic_per(y):
    return (25.2 * (1 + PRICE_G) ** (y - 2026)) * 1.05 + 7.395


_civic_n = {y: min(30 * (y - 2029), 150) for y in YEARS}
_civic = [_civic_n[y] * _civic_per(y) / 1000 for y in YEARS]
line("service", "National service: 150,000 more civic positions", ["LAB-9.01", "LAB-9.02",
                                                                   "LAB-9.04", "LAB-9.05",
                                                                   "LAB-9.06"],
     "gf", "firm", _civic, scale(_civic, 0.85), scale(_civic, 1.15),
     "Authorization (appropriated) or R1's fallback",
     "Memo 9 C at the decided scale; the ramp is section 4's")

# 14b. The grantees' match (LAB-9.01's working assumption; milestone review O-5). The
# federal $25,200 is a maximum per member service year [EV-WRK-398]; grantees pay the
# rest of program costs, an overall share of 24% in grant years 1-3, 26%, 28%, then 30%
# from year 10 [EV-WRK-454]. With the federal share at the maximum, the match per position
# is the federal grant times s / (1 - s). Each year's 30,000 new positions are counted as
# new grants that climb the schedule (central); all at 30% (high); a fifth less where
# rural and distressed communities use the waiver (low). Not federal cost: reported beside
# LAB-9, never added. Federalizing it for the new positions would add the same amount.
def _match_share(grant_year):
    return 0.24 if grant_year <= 3 else 0.26 if grant_year <= 6 else 0.28 if grant_year <= 9 \
        else 0.30


def _match(y, share=None):
    grant = 25.2 * (1 + PRICE_G) ** (y - 2026)
    total = 0.0
    for start in range(2030, min(y, 2034) + 1):  # 30,000 positions added each year
        s = share if share is not None else _match_share(y - start + 1)
        total += 30 * grant * s / (1 - s)
    return total / 1000


_svc_match = [_match(y) for y in YEARS]
line("service_match", "National service: the grantees' match (non-federal, reported only)",
     ["LAB-9.01"], "nonfed", "firm", _svc_match, scale(_svc_match, 0.8),
     [_match(y, 0.30) for y in YEARS], "Grantees, states and host organizations",
     "45 CFR 2521.60's schedule; not a federal cost")

# 15.The service-to-apprenticeship tranche (LAB-9.03): opens only when the gate is met,
# 2035 on the working ramp; 25,000 in FY2035 and 50,000 from FY2036 at about $35,000-
# 45,000 a position (2026 dollars; the note's part e).
def _tranche_per(y, per=40.0):
    return (per - 7.395) * (1 + PRICE_G) ** (y - 2026) + 7.395


_tr_n = {y: (25 if y == 2035 else 50 if y > 2035 else 0) for y in YEARS}
_tranche = [_tr_n[y] * _tranche_per(y) / 1000 for y in YEARS]
line("tranche", "Service-to-apprenticeship tranche, gated (contingent)", ["LAB-9.03"],
     "gf", "contingent", _tranche, [0.0] * 11,
     [_tr_n[y] * _tranche_per(y, 45.0) / 1000 for y in YEARS], "As LAB-9",
     "Zero unless the gate is met; shown from zero to the full tranche")

# 16. The labor act's civil penalties (LAB-2.01, 7.04, 13.01, 7.08, 15.01): receipts.
# CBO put the 2019 bill's labor-board penalties at $39M over ten years [EV-WRK-176]; the
# wage-law penalties are larger with 1,200 investigators (judgment: about $50M a year).
_pen = [0.0] + [-0.05] * 10
line("penalties", "Civil penalties under the labor act and wage law (receipts)",
     ["LAB-2.01", "LAB-7.04", "LAB-13.01"], "revenue", "firm", _pen, scale(_pen, 3.0),
     scale(_pen, 0.2), "Labor act", "A revenue gain; never netted against a spending line")

# 17. The income and payroll tax offset on employers' larger UI taxes, less the income
# tax on the larger benefits (LAB-11.05 with 11.01): higher employer taxes lower taxable
# wages (the 25% convention); on the general fund about 15 points of it fall on income
# tax, and about 10 points come back as income tax on the larger, taxable benefits, so
# about 5% of the tax increase (range 2-10%) is a general-fund loss. The payroll part,
# about 8%, falls on Social Security (line 18).
line("ui_offset", "Income-tax offset on employers' larger UI taxes, net of tax on benefits",
     ["LAB-11.05"], "revenue", "firm", scale(_tf(_UI["central"]), 0.05),
     scale(_tf(_UI["low"]), 0.02), scale(_tf(_UI["high"]), 0.10), "R1",
     "A revenue loss to the general fund")
line("ui_offset_ss", "Payroll-tax offset on employers' larger UI taxes (Social Security)",
     ["LAB-11.05"], "ss", "firm", scale(_tf(_UI["central"]), 0.08),
     scale(_tf(_UI["low"]), 0.05), scale(_tf(_UI["high"]), 0.10), "R1", "Off budget")

# 18. Income tax on wage insurance, which is taxable as wages (INC-5.01): about 10% of
# payments (8-12%).
line("wi_tax", "Income tax on wage insurance payments (receipts)", ["LAB-18.02"], "revenue",
     "firm", scale(_wi, -0.10), scale(_wi, -0.12 * 1.6), scale(_wi, -0.08 * 0.5), "R1",
     "A revenue gain")

# ---- Provisional items, priced on their recommendations (for Espen) ----------------
# 19. Work-connected good-cause quits in wage insurance (LAB-18.03's working reading):
# about 7% more recipients (3-12%), with administration.
line("quits", "Wage insurance for work-connected good-cause quits (provisional)",
     ["LAB-18.03"], "gf", "provisional", scale(_wi, 0.07 * 1.1), scale(_wi, 0.03 * 0.5),
     scale(_wi, 0.12 * 1.6 * 1.1), "R1", "LAB-18.03, for Espen")

# 20. Memo 10 part 1 C: occupation in wage records (its part of the one-time grant) and
# BLS's yearly displacement report with an annual survey, about $20-50M a year.
_bls = [0.0, 0.02, 0.03] + [0.035 * (1 + PRICE_G) ** (y - 2033) for y in range(2033, 2041)]
_occ = [0.0, 0.05, 0.1, 0.05] + [0.0] * 7
line("measure", "Displacement measure: occupation field and BLS's report (provisional)",
     ["LAB-19.01", "LAB-19.02", "LAB-19.03"], "gf", "provisional",
     [a + b for a, b in zip(_bls, _occ)],
     [a * 0.6 + b * 0.5 for a, b in zip(_bls, _occ)],
     [a * 1.5 + b * 2.0 for a, b in zip(_bls, _occ)], "R1 and appropriations",
     "Memo 10 part 1 C, for Espen")

# 21. Memo 10 part 2 C: the standby trigger, zero while off, capped at $5B a year, from
# about 2035 (contingent and provisional).
line("trigger", "Standby displacement trigger (contingent and provisional)",
     ["LAB-19.04", "LAB-19.05"], "gf", "contingent-provisional", [0.0] * 11, [0.0] * 11,
     [0.0] * 5 + [5.0] * 6, "R1", "Zero while off; up to the cap when on")

# ---- Agency capacity: democratic renewal's booked CAP-7 lines (reported, not added) --
_cap = lambda lo, hi, fy40lo, fy40hi: (lo, hi, fy40lo, fy40hi)
CAPACITY = [
    ("NLRB staff", "LAB-2.05", "$1.0-1.4 billion", "$0.10-0.15 billion",
     "Replaces the review's $1.9 billion (range $1.3-3.3 billion) [EV-DEM-330]"),
    ("FMCS mediators and panels", "LAB-1.05", "$0.1-0.2 billion", "$0.01-0.02 billion",
     "Not in democratic renewal's table: a written need"),
    ("Wage and Hour and OSHA", "LAB-7.01 to 7.03; LAB-6.01; LAB-12, 13, 15", "$2.4-4.0 billion",
     "$0.3-0.5 billion", "Inside Labor's $4.6 billion [EV-DEM-329]"),
    ("OSHA above the table's +700", "LAB-7.01", "inside the line above", "about $0.08 billion",
     "A written need against the contingency"),
    ("Office of Apprenticeship registration staff", "LAB-8.04", "not yet sized", "not yet sized",
     "Labor's 2027-28 staffing plan sizes it"),
    ("FLRA and agency labor relations", "LAB-16.01", "small", "small", "Listed for CAP-7"),
]

# Provisions with no federal budget line of their own, and why (6-cost.md, part 4).
NO_LINE = {
    "LAB-4.05": "executive action; contractors' costs within agencies' appropriations",
    "LAB-4.10": "territories' schedules: a mandate, no federal outlay (provisional)",
    "LAB-1.01": "rules; the Board's workload is CAP-7's (LAB-2.05)",
    "LAB-1.02": "rules", "LAB-1.03": "rules", "LAB-1.04": "rules", "LAB-1.06": "rules",
    "LAB-1.07": "coverage test (labor act)", "LAB-1A.01": "rules (separate title)",
    "LAB-2.02": "private right; courts' workload small", "LAB-2.03": "rules",
    "LAB-2.04": "rules", "LAB-2.06": "executive action",
    "LAB-1.05": "FMCS's cost is CAP-7's (written need)",
    "LAB-2.05": "CAP-7 (democratic renewal's booked lines)",
    "LAB-3.03": "seam: care's rates (HLT-10.04), booked there",
    "LAB-16.01": "restored bargaining; FLRA's load is CAP-7's",
    "LAB-6.01": "regulation; employers' costs, OSHA's staff in CAP-7",
    "LAB-6.02": "executive action", "LAB-6.03": "State Plan rule",
    "LAB-7.01": "CAP-7 (Wage and Hour and OSHA)",
    "LAB-7.02": "inside CAP-7's staff", "LAB-7.03": "inside CAP-7's staff",
    "LAB-7.06": "remedies", "LAB-7.07": "coverage test (wage law)",
    "LAB-7.08": "rule on employers", "LAB-7.09": "right",
    "LAB-12.01": "coverage; a Medicaid effect if the 2013 rule is gone by 2029 (part 3)",
    "LAB-12.02": "rule on employers", "LAB-15.01": "rule on employers",
    "LAB-14.01": "no mandate (provisional)", "LAB-17.01": "no requirement (provisional)",
    "LAB-8.05": "redirects existing WIOA money",
    "LAB-11.10": "self-financed by the reduced credit if authorized; contingent (part 2)",
}


def totals(kinds=("firm",), bases=("gf", "gf_disc", "revenue", "indirect"), which="central"):
    out = [0.0] * 11
    for ln in LINES:
        if ln["kind"] in kinds and ln["basis"] in bases:
            out = [a + b for a, b in zip(out, ln[which])]
    return out


def dec(p):
    return sum(p[:10])


def fmt(v):
    if abs(v) < 0.005:
        return "0.0"
    return f"{v:.1f}" if abs(v) >= 1 else f"{v:.2f}"


def table():
    rows = ["| Line | Provisions | Basis | Kind | " + " | ".join(str(y) for y in WINDOW)
            + " | **FY2030-39** | **2040** | Range FY2030-39 | Range 2040 |",
            "| --- " * (4 + 10 + 4) + "|"]
    for ln in LINES:
        c, lo, hi = ln["central"], ln["low"], ln["high"]
        lo_d, hi_d = sorted([dec(lo), dec(hi)])
        lo_4, hi_4 = sorted([lo[10], hi[10]])
        rows.append(f"| {ln['label']} | {', '.join(ln['provisions'])} | {ln['basis']} | "
                    f"{ln['kind']} | " + " | ".join(fmt(v) for v in c[:10])
                    + f" | **{fmt(dec(c))}** | **{fmt(c[10])}** | {fmt(lo_d)} to {fmt(hi_d)}"
                    f" | {fmt(lo_4)} to {fmt(hi_4)} |")
    return "\n".join(rows)


def summary():
    s = {}
    gf_b = ("gf", "gf_disc", "revenue", "indirect")
    for name, kinds in [("firm", ("firm",)),
                        ("contingent", ("contingent",)),
                        ("provisional", ("provisional",)),
                        ("contingent_provisional", ("contingent-provisional",))]:
        s[name] = {w: totals(kinds, gf_b, w) for w in ("central", "low", "high")}
    for name, bases in [("spending", ("gf", "gf_disc")), ("revenue", ("revenue",)),
                        ("indirect", ("indirect",)), ("trust", ("trust",)), ("ss", ("ss",))]:
        s[name] = {w: totals(("firm",), bases, w) for w in ("central", "low", "high")}
    booked = [sum(BOOKED[k][i] for k in ("LAB-5", "LAB-8", "LAB-9")) for i in range(11)]
    s["booked_lab"] = booked
    return s


def booking_rows():
    """Ledger midpoints a booking would carry ($T, FY2030-39; low/mid/high)."""
    pick = {"LAB-4 indirect (DY4 or LAB-1)": ["floor"], "LAB-5": ["credit"],
            "LAB-4.09": ["14c"], "LAB-3 and 4.04": ["boards"], "LAB-7.05": ["outreach"],
            "LAB-11 (general-fund spending)": ["eb", "ui_admin", "conformity"],
            "LAB-11 tax offset (revenue row)": ["ui_offset"],
            "LAB-18 (spending)": ["wi", "wi_admin", "hours"],
            "LAB-18 income tax (revenue row)": ["wi_tax"],
            "Penalties (revenue row)": ["penalties"], "LAB-8": ["apprenticeship"],
            "LAB-9": ["service"], "LAB-9.03 (contingent)": ["tranche"]}
    out = []
    by = {ln["id"]: ln for ln in LINES}
    for row, ids in pick.items():
        vals = []
        for w in ("low", "central", "high"):
            vals.append(sum(dec(by[i][w]) for i in ids) / 1000)
        f40 = sum(by[i]["central"][10] for i in ids)
        out.append((row, sorted([vals[0], vals[2]])[0], vals[1], sorted([vals[0], vals[2]])[1], f40))
    return out


def check():
    ids = {p["id"] for p in json.load(open(PROVISIONS))}
    covered = set(NO_LINE)
    for ln in LINES:
        covered |= set(ln["provisions"])
        for w in ("central", "low", "high"):
            assert len(ln[w]) == 11, (ln["id"], w)
    missing, stray = ids - covered, covered - ids
    assert not missing, f"provisions with no line: {sorted(missing)}"
    assert not stray, f"unknown provisions: {sorted(stray)}"
    assert len(ids) == 84, len(ids)
    for ln in LINES:  # every central inside its range
        for i in range(11):
            lo, hi = sorted([ln["low"][i], ln["high"][i]])
            assert lo - 1e-9 <= ln["central"][i] <= hi + 1e-9, (ln["id"], YEARS[i])
    # The derivations reproduce the figures section 6 quotes (milestone review O-1, O-2).
    assert abs(ui_increase() - 41.7) < 0.05 and abs(_R["central"] - 1.58) < 0.005
    new, rolls, ss = wi_steady()
    assert abs(new - 0.20) < 0.005 and abs(rolls - 0.32) < 0.005 and abs(ss - 2.0) < 0.01
    assert abs(_wi[4] / (ss * (1 + WI_G)) - 1) < 1e-3  # FY2034: the first full year
    assert all(abs(a + b) < 1e-9 for a, b in zip(by_id("ui_tf")["central"],
                                                  by_id("ui_tax")["central"]))
    print(f"OK: {len(ids)} provisions, {len(LINES)} lines, {len(NO_LINE)} with no line.")


def by_id(lid):
    return next(ln for ln in LINES if ln["id"] == lid)


# ---------------------------------------------------------------------------------
# Question for Espen (6-cost.md, "Questions for Espen", item 1): the 75% replacement
# rate kept from 2031, phased in, or held lower. Each option on the same basis as the
# lines above: the trust funds (employer-financed) and the general fund (Extended
# Benefits in ordinary years, scaled by the option's replacement; the 5% income-tax
# offset), with Social Security's 8% payroll offset off budget.
# Run:  python3 dossiers/work/tools/work_path.py --ui-options
# ---------------------------------------------------------------------------------
UI_OPTIONS = {
    "A. 75% from 2031, as decided": {2031: 0.75},
    "B. 60% in 2031, 65% in 2032, 70% in 2033, 75% from 2034": {2031: 0.60, 2032: 0.65,
                                                               2033: 0.70, 2034: 0.75},
    "C. 50% in 2031, rising about 3 points a year to 75% in 2039": {
        2031 + k: round(0.50 + 0.25 * k / 8, 4) for k in range(9)},
    "D. 60% from 2031, permanently": {2031: 0.60},
}


def ui_option(rates, case="central"):
    """(trust-fund benefits, general fund, Social Security) by FY2030-40, $B."""
    def rate(cy):
        return rates[max(y for y in rates if y <= cy)] if cy >= min(rates) else None
    tf_cy, r_cy = {}, {}
    for cy in range(2031, 2041):
        tf_cy[cy] = ui_increase(case, rate(cy)) * (1 + UI_G) ** (cy - 2025)
        r_cy[cy] = ui_factors(case, rate(cy))[1]
    tf = cy_to_fy(tf_cy)
    eb3 = {cy: 3.0 * (1 + UI_G) ** (cy - 2031) * r_cy[cy] for cy in range(2031, 2041)}
    gf = [a + 0.05 * b for a, b in zip(cy_to_fy(eb3), tf)]
    return tf, gf, scale(tf, 0.08)


def print_ui_options():
    print("| Option | Trust funds FY2031-39 | Trust funds FY2040 | General fund FY2030-39 "
          "| General fund FY2040 | Social Security FY2030-39 | Permanent, FY2025 levels |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for name, rates in UI_OPTIONS.items():
        tf, gf, ss = ui_option(rates)
        lo, hi = ui_option(rates, "low")[0], ui_option(rates, "high")[0]
        final = rates[max(rates)]
        print(f"| {name} | {dec(tf):.0f} ({dec(lo):.0f}-{dec(hi):.0f}) | {tf[10]:.1f} | "
              f"{dec(gf):.1f} | {gf[10]:.1f} | {dec(ss):.1f} | "
              f"{ui_increase('central', final):.0f} ({ui_increase('low', final):.0f}-"
              f"{ui_increase('high', final):.0f}) |")


# ---------------------------------------------------------------------------------
# The booking scenario: the rows section 7, part 1C ran through the budget model in a
# scratch copy (the reviewer's second note on #431). Four booked rows change and eight
# are added, each on its central FY2030-39 path; the tranche (contingent) is left out.
# Every row is entered as an outlay (out_*), as the scratch run did; at booking the
# revenue rows go on rev_* lines (7-validation.md, part 1C, "What the run needs").
# Nothing here writes to models/ unless --apply is given a scratch copy's root.
# Run:  python3 dossiers/work/tools/work_path.py --booking-scenario
#       python3 dossiers/work/tools/work_path.py --booking-scenario --apply <copy root>
# ---------------------------------------------------------------------------------
SCENARIO = [
    # (ledger id, lines, change or new, profile cat, ledger label for a new row)
    ("LAB-1", ["floor"], "change", "out_disc_nondefense", None),
    ("LAB-5", ["credit"], "change", "out_other_mandatory", None),
    ("LAB-8", ["apprenticeship"], "change", "out_disc_nondefense", None),
    ("LAB-9", ["service"], "change", "out_other_mandatory", None),
    ("LAB-4.09", ["14c"], "new", "out_other_mandatory", "14(c) transition grant (LAB-4.09)"),
    ("LAB-3", ["boards"], "new", "out_disc_nondefense",
     "Standards boards office and the wage commission (LAB-3, LAB-4.04)"),
    ("LAB-7.05", ["outreach"], "new", "out_disc_nondefense",
     "Wage and safety outreach grants (LAB-7.05)"),
    ("LAB-11", ["eb", "ui_admin", "conformity"], "new", "out_other_mandatory",
     "Unemployment insurance on the general fund: Extended Benefits, administration, "
     "conformity grant (LAB-11)"),
    ("LAB-11T", ["ui_offset"], "new", "out_other_mandatory",
     "Income-tax offset on employers' larger UI taxes (LAB-11.05; a revenue row at booking)"),
    ("LAB-18", ["wi", "wi_admin", "hours"], "new", "out_other_mandatory",
     "Wage insurance, its administration and the hours field (LAB-18)"),
    ("LAB-18T", ["wi_tax"], "new", "out_other_mandatory",
     "Income tax on wage insurance (LAB-18.02; a revenue row at booking)"),
    ("LAB-2P", ["penalties"], "new", "out_other_mandatory",
     "Civil penalties under the labor act and wage law (a revenue row at booking)"),
]
LEDGER_COLS = ["id", "legacy_id", "bill", "domain", "source", "rail", "channel", "cost_lo",
               "cost_mid", "cost_hi", "own_revenue_mid", "basis", "note", "floor_days",
               "felt_months", "durability", "target"]
PROFILE_COLS = ["table", "id", "kind", "cat", "start", "ramp", "grow", "end", "perm", "fade",
                "unified_zero", "basis"]


def booking_scenario():
    """(change or new, ledger row, profile row, year row) for each SCENARIO entry."""
    by = {ln["id"]: ln for ln in LINES}
    out = []
    for rid, ids, how, cat, label in SCENARIO:
        path = {w: [sum(by[i][w][k] for i in ids) for k in range(11)]
                for w in ("central", "low", "high")}
        lo, hi = sorted([dec(path["low"]) / 1000, dec(path["high"]) / 1000])
        mid = dec(path["central"]) / 1000
        r3 = lambda v: f"{round(v, 3) + 0.0:.3f}"  # no "-0.000"
        ledger = dict(id=rid, cost_lo=r3(lo), cost_mid=r3(mid), cost_hi=r3(hi))
        if how == "new":
            ledger.update(legacy_id="—", bill=label, domain="Labor",
                          source="dossiers/work/6-cost.md", rail="R2", channel="General fund",
                          own_revenue_mid="0", basis="estimate",
                          note="Scratch booking scenario (work_path.py --booking-scenario)",
                          floor_days="0", felt_months="12", durability="70",
                          target="2029-summer")
        nonzero = [k for k in range(10) if abs(path["central"][k]) > 1e-12]
        ends = bool(nonzero) and max(nonzero) < 9
        profile = dict(table="bill", id=rid, kind="", cat=cat, start="", ramp="1", grow="gdp",
                       end=str(2030 + max(nonzero)) if ends else "",
                       perm="0.0" if ends else "", fade="", unified_zero="",
                       basis="Scratch booking scenario: section 6's central path")
        years = {"id": rid, **{f"y{2030 + k}": f"{path['central'][k]:.4f}" for k in range(10)},
                 "note": "work_path.py --booking-scenario: section 6's central path, $B"}
        out.append((how, ledger, profile, years))
    return out


def _patch_csv(fn, rows, match=None):
    """Replace the fields of rows whose id matches (and match's column); append the rest."""
    import csv
    with open(fn, newline="") as f:
        rdr = csv.DictReader(f)
        cols, old = rdr.fieldnames, list(rdr)
    todo = {r["id"]: r for r in rows}
    for r in old:
        if r["id"] in todo and (match is None or r.get(match[0]) == match[1]):
            for k, v in todo.pop(r["id"]).items():
                if k in cols:
                    r[k] = v
    for r in todo.values():
        old.append({c: r.get(c, "") for c in cols})
    with open(fn, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(old)


def print_booking_scenario(apply_root=None):
    import csv
    rows = booking_scenario()
    out = csv.writer(sys.stdout, lineterminator="\n")
    print("# ledger-bills.csv: four rows changed (id and cost columns only) and eight added")
    out.writerow(LEDGER_COLS)
    for how, led, _, _ in rows:
        out.writerow([led.get(c, "(unchanged)" if how == "change" else "") for c in LEDGER_COLS])
    print("\n# fiscal-profiles.csv (table = bill; replaces the four rows' profiles)")
    out.writerow(PROFILE_COLS)
    for _, _, prof, _ in rows:
        out.writerow([prof[c] for c in PROFILE_COLS])
    print("\n# fiscal-years.csv ($ billion, FY2030-39; the model then grows FY2040 on with GDP)")
    ycols = ["id"] + [f"y{y}" for y in WINDOW] + ["note"]
    out.writerow(ycols)
    for _, _, _, yr in rows:
        out.writerow([yr[c] for c in ycols])
    print("""
# To rerun section 7, part 1C, in a scratch copy (never in the working tree):
#   git worktree add --detach <scratch> origin/main
#   python3 dossiers/work/tools/work_path.py --booking-scenario --apply <scratch>
#   cd <scratch>
#   sed -i 's#budget/test_provisions.py 2>&1 | tail -1#& || true#' models/tools/run-all.sh
#   bash models/tools/run-all.sh
#   python3 -c "import json; r = json.load(open('build/recovery-budget.json'))['cases']['mixed']['rows']; \\
#     g = {x['year']: x['agenda_gf_primary_bn'] for x in r}; print(round(g[2040], 1), round(sum(g[y] for y in range(2030, 2040)), 1))"
# Expected: 613.5 and 3747.4, against main's 602.7 and 3,773.4 ($ billion; +10.85 and -26.0;
# before the milestone fix 609.7 and 3719.4).
# Two checks fail by design and stop the suite unless step 6a is made non-fatal as above:
# the provision specs (step 6a; the new rows have none) and health financing's pinned
# plan-wide gap (step 8c, after build/recovery-budget.json is written).
# Then remove the copy: git worktree remove --force <scratch>""")
    if apply_root:
        inp = os.path.join(apply_root, "models", "data", "inputs")
        _patch_csv(os.path.join(inp, "ledger-bills.csv"), [r[1] for r in rows])
        _patch_csv(os.path.join(inp, "fiscal-profiles.csv"), [r[2] for r in rows],
                   match=("table", "bill"))
        _patch_csv(os.path.join(inp, "fiscal-years.csv"), [r[3] for r in rows])
        print(f"\n# applied to {inp}")


def main():
    if "--check" in sys.argv:
        check()
        return
    if "--ui-options" in sys.argv:
        print_ui_options()
        return
    if "--booking-scenario" in sys.argv:
        root = None
        if "--apply" in sys.argv:
            root = os.path.abspath(sys.argv[sys.argv.index("--apply") + 1])
            if root == os.path.abspath(os.path.join(HERE, "..", "..", "..")):
                sys.exit("--apply writes model inputs: give it a scratch copy, not this tree")
        print_booking_scenario(root)
        return
    print(table())
    s = summary()
    print()
    for k in ("spending", "revenue", "indirect", "firm", "contingent", "provisional",
              "contingent_provisional", "trust", "ss"):
        c, lo, hi = s[k]["central"], s[k]["low"], s[k]["high"]
        print(f"{k:24s} FY2030-39 {dec(c):8.1f} ({min(dec(lo),dec(hi)):.1f} to "
              f"{max(dec(lo),dec(hi)):.1f})  FY2040 {c[10]:7.2f} ({min(lo[10],hi[10]):.1f} to "
              f"{max(lo[10],hi[10]):.1f})  by year " + " ".join(f"{v:.1f}" for v in c))
    b = s["booked_lab"]
    f = s["firm"]["central"]
    print(f"booked LAB-5+8+9          FY2030-39 {dec(b):8.1f}  FY2040 {b[10]:.1f}")
    print(f"net change (firm-booked)  FY2030-39 {dec(f)-dec(b):8.1f}  FY2040 {f[10]-b[10]:.2f}")
    t = s["contingent"]["central"]
    print(f"firm + tranche FY2040 {f[10]+t[10]:.2f}; share of gap firm {f[10]/PLAN_GAP_FY2040:.2%},"
          f" with tranche {(f[10]+t[10])/PLAN_GAP_FY2040:.2%}; % GDP {f[10]/GDP_FY2040:.3%}")
    print()
    for r in booking_rows():
        print(f"{r[0]:32s} {r[1] + 0.0:.3f} / {r[2] + 0.0:.3f} / {r[3] + 0.0:.3f}   "
              f"FY2040 {r[4]:.2f}")


if __name__ == "__main__":
    main()


def subtable(ids, total=None):
    """Markdown rows for the named lines, with an optional bold total row."""
    by = {ln["id"]: ln for ln in LINES}
    rows = []
    agg = {w: [0.0] * 11 for w in ("central", "low", "high")}
    for i in ids:
        ln = by[i]
        c, lo, hi = ln["central"], ln["low"], ln["high"]
        for w in agg:
            agg[w] = [a + b for a, b in zip(agg[w], ln[w])]
        ld, hd = sorted([dec(lo), dec(hi)])
        l4, h4 = sorted([lo[10], hi[10]])
        rows.append(f"| {ln['label']} | {', '.join(ln['provisions'])} | "
                    + " | ".join(fmt(v) for v in c[:10])
                    + f" | **{fmt(dec(c))}** | **{fmt(c[10])}** | {fmt(ld)} to {fmt(hd)} | {fmt(l4)} to {fmt(h4)} |")
    if total:
        c, lo, hi = agg["central"], agg["low"], agg["high"]
        ld, hd = sorted([dec(lo), dec(hi)])
        l4, h4 = sorted([lo[10], hi[10]])
        rows.append(f"| **{total}** | | " + " | ".join(f"**{fmt(v)}**" for v in c[:10])
                    + f" | **{fmt(dec(c))}** | **{fmt(c[10])}** | **{fmt(ld)} to {fmt(hd)}** | **{fmt(l4)} to {fmt(h4)}** |")
    return "\n".join(rows)


if __name__ == "__main__" and "--parts" in sys.argv:
    SPEND = ["14c", "boards", "outreach", "eb", "ui_admin", "conformity", "hours", "wi",
             "wi_admin", "apprenticeship", "service"]
    REV = ["credit", "ui_offset", "wi_tax", "penalties"]
    print(subtable(SPEND, "Spending lines")); print(subtable(REV, "Revenue effects"))
    print(subtable(["floor"], "Indirect effect"))
    print(subtable(SPEND + REV + ["floor"], "Work on the general fund, firm lines"))
    print(); print(subtable(["ui_tf", "ui_tax"], "Trust funds, net"))
    print(subtable(["ui_offset_ss"]))
    print(); print(subtable(["tranche", "eb_recession", "trigger"], "Contingent lines"))
    print(); print(subtable(["quits", "measure"], "Provisional lines"))
