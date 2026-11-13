#!/usr/bin/env python3
"""Care's base under the status rule: health and long-term care cover people with lawful or registered status.

Role: the one place care's corrections for people with no immigration status are computed (`DEC-2026-11-12-19` for
health, `DEC-2026-11-13-01` for long-term care, `DEC-2026-11-13-02` for hospitals' uncompensated care; `dossiers/care/6-cost.md` part 2b and `6bcd-cost.md` part 2b).
Status: current. Project arithmetic, not an official score. Run:

    python3 dossiers/care/tools/status_rule.py

Care's booked base covered everyone but a 1% residual (`sp_residual_unins`, about 3.55 million people in health) and,
for long-term care from 2035, every resident. Under the status rule, people with no status are covered by neither:
they keep emergency care as today (EMTALA and Emergency Medicaid at their January 2029 terms). A filing receipt under
the immigration act counts as status (IMM-1.10, IMM-1.21). Who has no status in each fiscal year comes from the
immigration model (`dossiers/immigration/tools/immigration_model.py`): the people eligible for status or registration
less those who have filed (known people file first, on their notices), so it falls as filing proceeds. People who
arrive without status after the act is signed are not counted, as in the immigration model; they would add to every
line here.

Four corrections, each against what care's path already counts, so nothing is counted twice:
1. **Health, coverage removed** (HLT-7): people with no status beyond the residual's status share (the immigration
   model's `without_status_m`, 2.25 million), at care's average newly covered person on care's own path
   (`immigration_model.care_base_correction`, which runs `health_path.py` with the residual changed). A saving.
2. **Health, Emergency Medicaid kept** (HLT-7): care's plan replaces the federal Medicaid money it absorbs, and that
   money includes Emergency Medicaid, the only Medicaid payment made for people with no status. Under the rule it keeps
   flowing for everyone with no status, the residual's 2.25 million included, so the replaced money is that much
   smaller. Added back on the share of Medicaid that has moved into the plan (wave 1's children, then thirds in
   2033-35), at CBO's per-person federal spending from CMS-64 data [EV-CAR-704] over MPI's count [EV-IMM-005]. A cost.
3. **Health, hospital uncompensated-care payment kept** (HLT-7; `DEC-2026-11-13-02`): care's plan also replaces
   Medicaid's disproportionate share hospital (DSH) money. A federal uncompensated-care payment to hospitals continues
   for the emergency care they give people the plan does not cover, sized to today's DSH-type share for those
   patients: the federal DSH allotment per uninsured person [EV-CAR-710], brought to FY2025's allotment [EV-CAR-707]
   and grown with the CPI-U as the allotments are; times the share of DSH that pays for uninsured patients rather than
   Medicaid shortfall [EV-CAR-709] [EV-CAR-708]; times the use of hospital care by people with no status against the
   average uninsured person [EV-CAR-711] [EV-CAR-712]; over everyone with no status, the residual included, on the
   share of Medicaid that has moved into the plan (as for Emergency Medicaid). A cost.
4. **Long-term care** (HLT-9, HLT-10): only the benefit's new users are affected. The states' relief, the richer
   budgets and the hold-harmless reach people already on Medicaid home care, and Medicaid has barred people with no
   status since 1996 (except emergency care) [EV-CAR-008]. The new-user line (net of options 2 and 4), the care
   floor on new users' hours and the care part of institutional care (net of option 5) are lowered by the share of
   their users who have no status: their share of the population times their relative need, which is low because
   only about 1% of unauthorized immigrants are 65 or older [EV-CAR-705] [EV-CAR-706]. A saving.

Immigration's IMM-1 table line already prices only lawful residents above care's base (memo 3's added immigrants,
refugees, returnees), on the same per-person path: those people are not in this file's counts, so the two do not
overlap.

Readings are (low, central, high) cost, as in `care_bcd_path.py`: the low reading pairs the immigration model's low
inputs (more people without status), the lower Emergency Medicaid and DSH figures and the higher need factors. Care's own
long-term care pieces stay at their central reading here, so the readings vary only who has no status and their need.
"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
IMM = os.path.normpath(os.path.join(HERE, '..', '..', 'immigration', 'tools'))
for p in (HERE, IMM):
    if p not in sys.path:
        sys.path.insert(0, p)

FY = range(2030, 2041)
WINDOW = range(2030, 2040)
CASES = ('low', 'central', 'high')

INPUTS = {
    # (low-cost reading, central, high-cost reading, basis)
    'em_federal_pp_2023': (110.0, 165.0, 310.0,
                           "EV-CAR-704: CBO, Emergency Medicaid $3,775 million in FY2023 ($3,110 million in FY2019, $7,050 "
                           "million in FY2021, the high), at the regular federal share of about 60% that applies from "
                           "October 2026 (EV-CAR-009; care_repricing.FMAP_REGULAR), over MPI's 13.7 million unauthorized "
                           "residents (EV-IMM-005); $ per person a year. Some of it pays for lawful immigrants in the "
                           "five-year wait, so the per-person figure for people with no status is if anything high"),
    'em_growth': (0.055, 0.055, 0.055, "assumption: part B's nominal health growth (care_repricing.GROWTH)"),
    'dsh_fed_pp_2025': (546.0, 546.0, 546.0,
                        "EV-CAR-710: Urban, federal DSH allotment of $429.00 per uninsured person in FY2019 ($12,590.7 "
                        "million), scaled to FY2025's $16,024.3 million (EV-CAR-707); $ per uninsured person a year. The "
                        "FY2019 uninsured count is kept, so if anything low. Unreduced: under the January 2029 law the "
                        "only remaining reduction is FY2028's (EV-CAR-707 context)"),
    'dsh_growth': (0.023, 0.023, 0.023, "the CPI-U, by which unreduced allotments grow (EV-CAR-707); fiscal-model.py's "
                                         "CBO path, 2.26-2.3%"),
    'dsh_uninsured_share': (0.30, 0.50, 0.69,
                            "share of DSH that pays for uninsured patients rather than Medicaid shortfall: KFF/Urban's "
                            "50% assumption for 2017, MACPAC's 69% from 2014 audits (EV-CAR-709); about 27% in expansion "
                            "states and 88% in the others in SPRY 2019 audits (EV-CAR-708), so about 0.3 low"),
    'dsh_relative_use': (0.50, 0.75, 1.00,
                         "assumption: hospital care used by a person with no status against the average uninsured "
                         "person. Uninsured immigrants spent $459 against $629 for the US-born uninsured, about 0.73 "
                         "(EV-CAR-711); unauthorized immigrants' inpatient spending among users is about half the "
                         "US-born figure, but their likelihood of uncompensated care is not significantly different "
                         "(EV-CAR-712)"),
    'ltc_need_home': (0.45, 0.30, 0.15,
                      "assumption: need for the home benefit's three-activity test among people with no status, against "
                      "the population average. About two-thirds of new users are 65 or older (judgment); 1% of "
                      "unauthorized immigrants are, against about 13% of everyone in 2011 and more since (EV-CAR-705, EV-CAR-706), so that "
                      "part is about 0.05-0.1; working-age people with no status are about as likely as other working-age "
                      "people to need care, but younger (72% are 19 to 44, EV-CAR-706): about 0.7-0.8 for the under-65 "
                      "third. Together about 0.3"),
    'ltc_need_institution': (0.20, 0.10, 0.05,
                             "assumption: the same for nursing-home stays, where 84% of residents have three or more "
                             "limitations and most are 65 or older (EV-CAR-647): close to the 65-and-older ratio"),
    'pop_growth': (0.005, 0.005, 0.005, "assumption: the coverage model's 2032 population (355.2 million, the Social "
                                          "Security area population, EV-CAR-051) grown 0.5% a year"),
}


def val(name, i):
    return INPUTS[name][i]


def _mods():
    IM = importlib.import_module('immigration_model')
    HP = importlib.import_module('health_path')
    return IM, HP


def fy_from_cy(cy):
    return {y: 0.25 * cy.get(y - 1, 0.0) + 0.75 * cy.get(y, 0.0) for y in FY}


def no_status(i):
    """People with no status by fiscal year, million: beyond the health residual's share, and all of them."""
    IM, _ = _mods()
    case = CASES[i]
    v = lambda n: IM.val(n, case)  # noqa: E731
    u = IM.uscis(case)
    eligible = v('tier_b_m') + v('tier_a_outside_b_m') + v('registered_m')
    cum, beyond, total = 0.0, {}, {}
    for y in FY:
        cum += u['filings_by_year'][y] if y < 2040 else 0.0
        total[y] = max(0.0, eligible - cum) if y >= 2031 else 0.0
        beyond[y] = max(0.0, total[y] - v('without_status_m')) if y >= 2031 else 0.0
    return beyond, total


def population(y, i):
    return 355.2 * (1 + val('pop_growth', i)) ** (y - 2032)


def health(i=1):
    """HLT-7's correction, $ billion by fiscal year: coverage removed, Emergency Medicaid and the DSH-type share kept."""
    IM, HP = _mods()
    corr = IM.care_base_correction(CASES[i])
    beyond, total = no_status(i)
    assert all(abs(beyond[y] - corr['people'][y]) < 1e-9 for y in FY)     # one count of people, the model's
    removed = {y: corr['saving'][y] for y in FY}
    I, B, P = HP.setup()
    _, _, _, f = HP.groups(I, B, P)
    cal = {y: HP.shares_moved(y, f['child_share_moving'])['medicaid'] for y in range(2029, 2041)}
    moved = fy_from_cy(cal)
    pp = {y: val('em_federal_pp_2023', i) * (1 + val('em_growth', i)) ** (y - 2023) / 1000 for y in FY}   # $ thousand
    kept = {y: total[y] * pp[y] * moved[y] for y in FY}          # million people x $ thousand = $ billion
    # DEC-2026-11-13-02: hospitals keep today's DSH-type federal share for the care of people the plan does not cover
    dsh_pp = {y: val('dsh_fed_pp_2025', i) * val('dsh_uninsured_share', i) * val('dsh_relative_use', i)
              * (1 + val('dsh_growth', i)) ** (y - 2025) / 1000 for y in FY}                      # $ thousand
    dsh = {y: total[y] * dsh_pp[y] * moved[y] for y in FY}
    return dict(removed=removed, em_kept=kept, dsh_kept=dsh, net={y: removed[y] + kept[y] + dsh[y] for y in FY},
                people_beyond=beyond, people_all=total, medicaid_moved=moved, dsh_pp=dsh_pp)


def ltc(i=1):
    """HLT-9's and HLT-10's corrections, $ billion by fiscal year (negative: savings)."""
    R = importlib.import_module('care_repricing')
    G = R.GROWTH
    c = 1                     # care's own pieces at their central reading; the readings vary who has no status
    users = R.NEW_USERS_2ADL[c] * R.RETAINED[c]
    newb = users * R.COST_EACH_2ADL[c] * R.COST_LIFT[c] / 1e9      # care_bcd_path.newb[1]
    _, total = no_status(i)
    home, floor, inst = {}, {}, {}
    for y in range(2035, 2041):
        t = y - 2035
        opt4 = {0: 0.5, 1: 0.2 * G}.get(t, 0.0)
        new_home = newb * G ** t * (1 - 0.07) - newb * opt4               # memo 6 B's new users, options 2 and 4
        new_floor = newb * R.LABOR_SHARE * R.FLOOR_LIFT[c] * (G ** t - opt4)   # memo 14 on their hours
        care_part = R.MEMO8C_2035[c] / 1e9 * G ** t - 8.0 * G ** t       # memo 8 C, net of option 5
        share = total[y] / population(y, i)
        home[y] = -new_home * share * val('ltc_need_home', i)
        floor[y] = -new_floor * share * val('ltc_need_home', i)
        inst[y] = -care_part * share * val('ltc_need_institution', i)
    users_no_status = {y: users / 1e6 * total[y] / population(y, i) * val('ltc_need_home', i) for y in range(2035, 2041)}
    return dict(home=fy_from_cy(home), floor=fy_from_cy(floor), institutional=fy_from_cy(inst),
                users_m=users_no_status)


def w(s):
    return sum(s.get(y, 0.0) for y in WINDOW), s.get(2040, 0.0)


def main():
    print("CARE'S BASE UNDER THE STATUS RULE ($ billion by fiscal year; a cost positive)")
    print('  ' + ' '.join(f'{y:>7}' for y in FY) + '   FY30-39')
    h = health(1)
    for k in ('people_beyond', 'people_all'):
        print(f'{k:14}' + ' '.join(f'{h[k][y]:7.2f}' for y in FY) + '   (million)')
    for k in ('removed', 'em_kept', 'dsh_kept', 'net'):
        print(f'{"health " + k:14}' + ' '.join(f'{h[k][y]:7.1f}' for y in FY) + f'   {w(h[k])[0]:7.1f}')
    L = ltc(1)
    for k in ('home', 'floor', 'institutional'):
        print(f'{"ltc " + k:14}' + ' '.join(f'{L[k].get(y, 0):7.2f}' for y in FY) + f'   {w(L[k])[0]:7.2f}')
    print('  long-term care new users with no status, calendar years (thousand): ' +
          ', '.join(f'{y} {v * 1000:.0f}' for y, v in L['users_m'].items()))
    print()
    print('Readings (low, central, high cost): FY2030-39 and FY2040, $ billion')
    for i, name in enumerate(CASES):
        hh, ll = health(i), ltc(i)
        lt = {y: sum(ll[k].get(y, 0.0) for k in ('home', 'floor', 'institutional')) for y in FY}
        print(f'  {name:8} health removed {w(hh["removed"])[0]:7.1f} / {w(hh["removed"])[1]:6.1f}; '
              f'Emergency Medicaid kept {w(hh["em_kept"])[0]:5.1f} / {w(hh["em_kept"])[1]:4.1f}; '
              f'DSH-type share kept {w(hh["dsh_kept"])[0]:5.1f} / {w(hh["dsh_kept"])[1]:4.1f}; '
              f'health net {w(hh["net"])[0]:7.1f} / {w(hh["net"])[1]:6.1f}; long-term care {w(lt)[0]:6.2f} / {w(lt)[1]:5.2f}')


if __name__ == '__main__':
    main()
