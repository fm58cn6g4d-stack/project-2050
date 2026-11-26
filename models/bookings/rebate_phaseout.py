"""rebate_phaseout.py: memo G30, the VAT rebate's income limit (G24.1, DEC-2026-11-25-15).

Role: prices the options for limiting G24 B's VAT rebate ($150 a point for every adult, 2040 dollars) to people below
an income threshold, on the same tools that price G24 B (`fiscal_revision.py`). For each option it reports:
  * the share of the rebate's cost kept, on the household model's tax units (AGI in the take-home test's FY2040
    incomes, at today's prices, the same units as the AGI surtax's $100K/$200K): every adult in a unit (head,
    spouse and adult dependents) gets the rebate in full below the threshold, falling in a straight line to nothing
    across the phase-out range;
  * the VAT rate that closes memo G23's goal B with G19 B's sources (G24 B's mix 2), re-solved with the rebate's
    cost per point scaled by that share (`fiscal_revision.plug_rate`);
  * the take-home test at that rate (workers ahead, and those below 200% of poverty), with G19 B's top-end sources
    (OUT, DED, SUR) counted as fiscal_revision.take_home_mix counts them, and each worker unit's rebate phased out on its own AGI (`fiscal_revision.TakeHome`, adults as there: head and spouse);
  * by fifth of households (D3's groups), the VAT a household pays and the rebate it gets back, FY2040.
The threshold and range are held at the same share of incomes over time (indexed to incomes). Project arithmetic on
exploratory models, not official scores. Nothing booked.

Run after the common rebuild:  python3 models/bookings/rebate_phaseout.py [--write]
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(Path(__file__).resolve().parent)]
import fiscal_revision as FR  # noqa: E402

OUT = ROOT / 'dossiers/foundations/fair-financing/notes/rebate-phaseout-results.md'
FIFTHS = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')

# (label, single and head-of-household threshold, joint threshold, phase-out width single, joint), $ of AGI
OPTIONS = (
    ('No limit (G24 B as decided)', None, None, 0, 0),
    ('$100K single / $200K joint (your idea)', 100_000, 200_000, 20_000, 40_000),
    ('$75K / $150K', 75_000, 150_000, 20_000, 40_000),
    ('$60K / $120K', 60_000, 120_000, 20_000, 40_000),
    ('$40K / $80K', 40_000, 80_000, 20_000, 40_000),
)


def factor(agi, fs, opt):
    """The share of the rebate a unit keeps."""
    _, ts, tj, ws, wj = opt
    if ts is None:
        return 1.0
    t, w = (tj, wj) if fs == 'joint' else (ts, ws)
    return min(1.0, max(0.0, 1.0 - (agi - t) / w))


def unit_adults(u):
    return 1 + (u['age_s'] >= 0) + u['n_dep_18'] + u['n_dep_19_23_student'] + u['n_dep_other']


class PhasedTakeHome(FR.TakeHome):
    """fiscal_revision.TakeHome with each unit's rebate phased out on its own AGI."""
    opt = OPTIONS[0]

    def run(self, R, vat_rate=0.0, top_bn=0.0, carb_bn=0.0, carb_div_bn=0.0):
        HC, price = self.HC, self.hctx['price_2040']
        o = HC.unified_package(self.hctx, self.case, HC.unified_spec(R=R, S=5.0 + self.fold, hi=2.5, form='linear'))
        reb_adult = vat_rate * FR.REBATE_PER_POINT_2040 / price
        top_k = top_bn * 1e9 / price / self.excess_total if self.excess_total else 0.0
        n = ahead = n_low = ahead_low = 0.0
        for u in self.units:
            if not HC._is_worker(u):
                continue
            members = self.hh_units[u['hh']]
            share = max(u['n_people'], 1) / sum(max(v['n_people'], 1) for v in members)
            q = 'Q%d' % self.g5.get(u['hh'], 3)
            n_ad = max(u['n_people'] - u['n_dep'], 1)
            agi = u['t_agi'] * self.igrow
            fs = 'joint' if u['t_fs'] == 'joint' else 'single'
            extra = (vat_rate * self.per_point[q] / price * share - reb_adult * n_ad * factor(agi, fs, self.opt)
                     + top_k * self.excess(u))
            nn = max(u['n_people'], 1)
            kind = 'job' if u['n_employer_cov'] > 0 else ('own' if u['n_marketplace'] > 0 else
                                                         ('medicaid' if u['n_medicaid'] > 0 else
                                                          ('medicare' if u['n_medicare'] > 0 else 'uninsured')))
            prem = u['premiums_paid'] * self.hgrow
            oop = self.oop
            oo = (u['n_employer_cov'] * oop['esi'] + u['n_marketplace'] * oop['ng_sub'] + u['n_medicaid'] * oop['medicaid']
                  + u['n_medicare'] * oop['medicare']
                  + max(nn - u['n_employer_cov'] - u['n_marketplace'] - u['n_medicaid'] - u['n_medicare'], 0)
                  * oop['uninsured']) + u['n_medicare'] * self.partb
            today, plan = HC.visible(agi, fs, nn, kind, prem if kind == 'job' else 0.0,
                                     oo + (prem if kind != 'job' else 0.0), o, HC.fpl200(nn),
                                     earn=HC.earn_unit(u) * self.igrow, low2=False)
            w = u['weight']
            ok = plan + extra <= today
            n += w
            ahead += w * ok
            if agi / (HC.fpl200(nn) / 2) < 2:
                n_low += w
                ahead_low += w * ok
        return dict(workers=round(100 * ahead / n, 1), below_200fpl=round(100 * ahead_low / n_low, 1))


def kept(th, opt):
    """Share of the rebate's adults kept, all units and by fifth (adult-weighted, the phase-out counted)."""
    tot, keep = {}, {}
    for u in th.units:
        fs = 'joint' if u['t_fs'] == 'joint' else 'single'
        a = u['weight'] * unit_adults(u)
        q = 'Q%d' % th.g5.get(u['hh'], 3)
        for g in (q, 'all'):
            tot[g] = tot.get(g, 0.0) + a
            keep[g] = keep.get(g, 0.0) + a * factor(u['t_agi'] * th.igrow, fs, opt)
    return {g: keep[g] / tot[g] for g in tot}


def build():
    B = FR.base()
    bk = B['bk']
    pp = FR.FP.per_point(FR.K.Context())
    G, _ = FR.goals(B)
    goal = G['B']['goal']
    mat = FR.Mature()
    th = PhasedTakeHome(mat)
    gross, reb0 = FR.K.VAT_POINT_2040, FR.vat_point(bk, 2040)[1]
    base_rebate = FR.REBATE_PER_POINT_2040
    hh40 = mat.households(2040)
    fixed = FR.source_paths(bk, ('OUT', 'DED', 'SUR'))
    top = sum(p[2040] for k, p in fixed.items() if FR.SOURCES[k][6] == 'surtax')   # as fiscal_revision.take_home_mix
    rows = []
    try:
        for opt in OPTIONS:
            k = kept(th, opt)
            FR.REBATE_PER_POINT_2040 = base_rebate * k['all']
            rate = FR.plug_rate(bk, B['ph3'], goal, ('OUT', 'DED', 'SUR'), 'VAT', 2035, pp)
            net, reb = FR.vat_point(bk, 2040)
            FR.REBATE_PER_POINT_2040 = base_rebate
            th.opt = opt
            t = th.run(FR.FP.R_BOOKED, rate, top)
            fifth = {}
            for q in FIFTHS:   # FY2040, $ a household, nominal: VAT paid at the rate, rebate received
                vat = rate * th.per_point[q]
                rb = rate * reb0 * 1e9 * mat.share['adults'][q] * k[q] / (hh40 * 0.2)   # D3's adults key, as fiscal_revision
                fifth[q] = (vat, rb)
            rows.append(dict(opt=opt, kept=k, rate=rate, net=net, reb=reb, take=t, fifth=fifth))
    finally:
        FR.REBATE_PER_POINT_2040 = base_rebate
        th.opt = OPTIONS[0]
    return dict(rows=rows, gross=gross, reb0=reb0, top=top, base=th.run(FR.FP.R_BOOKED))


def pct(x):
    return '%.0f%%' % (100 * x)


def money(v):
    return '${:,.0f}'.format(v)


def markdown(d):
    L = ['# The VAT rebate\'s income limit (memo G30 results)', '',
         'Generated by `models/bookings/rebate_phaseout.py --write` after the common rebuild. Read with '
         '[`../memos/G30-rebate-phase-out.md`](../memos/G30-rebate-phase-out.md). G24 B\'s mix (G19 B\'s deduction limits '
         'and AGI surtax, then a rebated VAT from FY2035) on memo G23\'s goal B, re-solved for each limit; the take-home '
         'test and the fifths in FY2040. Thresholds are AGI at today\'s prices on FY2040 incomes, the units of the AGI '
         'surtax\'s $100K/$200K, indexed to incomes. Heads of household take the single figures. Project arithmetic on '
         'exploratory models, not official scores. Nothing booked.', '',
         'A VAT point raises $%.1fB net in FY2040 before the rebate; the rebate for every adult costs $%.1fB a point.' % (
             d['gross'], d['reb0']), '',
         '## 1. The options', '',
         '| Limit | Phase-out (single / joint) | Rebate kept | Rebate a point ($B) | Net a point ($B) | VAT rate (FY2035 on) '
         '| Workers ahead | Below 200% of poverty |',
         '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for r in d['rows']:
        lab, ts, tj, ws, wj = r['opt']
        rng = '—' if ts is None else '$%dK-%dK / $%dK-%dK' % (ts // 1000, (ts + ws) // 1000, tj // 1000, (tj + wj) // 1000)
        L.append('| %s | %s | %s | %.1f | %.1f | %.2f%% | %.1f%% | %.1f%% |' % (
            lab, rng, pct(r['kept']['all']), r['reb'], r['net'], r['rate'], r['take']['workers'], r['take']['below_200fpl']))
    b = d['base']
    L += ['', 'The take-home test counts G19 B\'s deduction limits, AGI surtax and the outside fix ($%.1fB in FY2040), as `fiscal_revision.take_home_mix` does.' % d['top']]
    L += ['', 'Without the VAT (the plan as booked, R at 3.80%%): %.1f%% of workers ahead, %.1f%% below 200%% of poverty.' % (
        b['workers'], b['below_200fpl']), '',
          '## 2. The rebate against the VAT, by fifth of households (FY2040, $ a household, nominal)', '',
          'Each cell: VAT paid at the option\'s rate / rebate received (the share of the VAT it gives back).', '',
          '| Limit | ' + ' | '.join(FIFTHS) + ' |', '| --- |' + ' --- |' * len(FIFTHS)]
    for r in d['rows']:
        cells = []
        for q in FIFTHS:
            v, rb = r['fifth'][q]
            cells.append('%s / %s (%s)' % (money(v), money(rb), pct(rb / v)))
        L.append('| %s | %s |' % (r['opt'][0], ' | '.join(cells)))
    L += ['', '## 3. The share of each fifth\'s adults who keep the rebate', '',
          '| Limit | ' + ' | '.join(FIFTHS) + ' | All |', '| --- |' + ' --- |' * (len(FIFTHS) + 1)]
    for r in d['rows']:
        L.append('| %s | %s | %s |' % (r['opt'][0], ' | '.join(pct(r['kept'][q]) for q in FIFTHS), pct(r['kept']['all'])))
    return '\n'.join(L) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    a = ap.parse_args()
    md = markdown(build())
    if a.write:
        OUT.write_text(md)
        print('wrote', OUT.relative_to(ROOT))
    else:
        print(md)


if __name__ == '__main__':
    main()
