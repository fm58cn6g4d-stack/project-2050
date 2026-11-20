"""The settlement's risk screen: the recommended package under each risk the settlement names, one at a time.

Role: the risk table of `dossiers/foundations/fair-financing/2-settlement.md` part 5. Each row reruns the recommended
package (`packages.PACKAGES['recommended']`) with one risk added and reports the general-fund gap it leaves in FY2040,
FY2045 and FY2056, and the VAT points that would cover it in FY2040. Status: exploratory screen for a provisional
draft; nothing adopted or booked.

Run after the common rebuild:  python3 models/tools/financing-protection/screen.py [--markdown]

The quintile diagnostics that lived here (the pre-PR26 `household_diagnostic` grid of credits and tax points) are
retired: D3 runs in `packages.py` on the package the gap books. They are in Git history.
"""
import argparse
import json

import packages as K

def vat_path(ctx):
    """The recommended package's VAT adjustment path (negative: revenue)."""
    vat = next(o for o in K.resolve(ctx, K.PACKAGES['recommended']) if o['label'].startswith('VAT'))
    return next(v for k, v in vat['adjust'].items() if k.startswith('VAT'))


# Each risk: (label, basis, options added to the recommended package)
def risks(ctx):
    top = ['G1', 'G3', 'G9', 'C18', 'C43', 'H1b', 'GX']
    wage_stack = {y: sum(ctx.line(r)[y] for r in top) for y in K.YEARS}
    # The stack note (part 3): the wage stack's top tier yields 60-64% of statutory revenue at the working elasticity
    # (0.25) against the 80-85% booked; up to about $140B in FY2040 on a rough, unverified reading. Scaled here as that
    # share of the top rows' path.
    k_stack = 140.0 / -wage_stack[2040]
    return [
        ('Without D2, the national health budget', 'DEC-2026-11-15-08; never achieved [EV-CAR-742]',
         [K.OPTIONS['without_d2'](ctx)]),
        ('Without HS2, the wealth tax', 'legal risk high (Moore, 2024, left it open); its fallback is mostly G11\'s base',
         [K.OPTIONS['without_hs2'](ctx)]),
        ('Without D2 and HS2', 'both', [K.OPTIONS['without_d2'](ctx), K.OPTIONS['without_hs2'](ctx)]),
        ('The wage stack yields at the working elasticity', 'stack note part 3: about $140B in FY2040 (rough)',
         [dict(label='Wage stack at 0.25', adjust={'Wage stack yield': K.scaled(wage_stack, -k_stack)})]),
        ('The avoidance allowance stays at 20% on the base rate', '1-audit.md item 9; the range\'s top',
         [dict(label='Avoidance back to 20%', adjust={'Avoidance reverted': K.scaled(
             K.OPTIONS['avoidance_by_tier'](ctx)['adjust']['Avoidance allowance by tier'], -1)})]),
        ('The stack cap costs its high end (C1 at $55B)', 'stack note part 4',
         [dict(label='Cap high', adjust={'Cap high end': K.scaled(ctx.line('HS2'), -15.0 / -ctx.line('HS2')[2040])})]),
        ('C3A, the clean electricity compliance payments, vanish', '1-audit.md item 43: suppliers comply',
         [dict(label='Without C3A', adjust={'Without C3A': K.scaled(ctx.line('C3A'), -1)})]),
        ('The VAT yields 15% less', "compliance and base erosion beyond CBO's broad base",
         [dict(label='VAT -15%', adjust={'VAT shortfall': K.scaled(vat_path(ctx), -0.15)})]),
        ('The HI grant correction is not confirmed', 'the accounting item for G5 to check',
         [dict(label='HI grant kept', kw=dict(hi_grant_points=K.m.A['hi']['gf_support_payroll_points']))]),
        ('Pre-2025-law scores come in 10% low', '1-audit.md item 22: about $4.9T of the decade\'s revenue rests on them',
         [dict(label='Old scores -10%', adjust={'Old scores': K.scaled(
             {y: sum(ctx.line(r)[y] for r in ('G1', 'G3', 'G5', 'G6', 'G7', 'G10', 'G11', 'H1a', 'H1b', 'C18', 'C38',
                                               'New indexed income contributions')) for y in K.YEARS}, -0.10)})]),
    ]


def build():
    ctx = K.Context()
    rec = K.resolve(ctx, K.PACKAGES['recommended'])
    # The HI-grant risk overrides an argument the package sets: drop the package's own setting for that row.
    base = K.price(ctx, rec, 'recommended')
    rows = []
    for label, basis, extra in risks(ctx):
        opts = rec + extra
        if any('hi_grant_points' in o.get('kw', {}) for o in extra):
            opts = [o for o in rec if 'hi_grant_points' not in o.get('kw', {})] + [
                o for o in extra if 'hi_grant_points' not in o.get('kw', {})]
        f = K.price(ctx, opts, label)
        per_point = K.VAT_POINT_2040
        rows.append(dict(risk=label, basis=basis, gap={y: f['gap'][y] for y in (2040, 2045, 2056)},
                         gap_2030_39=f['gap_2030_39'], vat_points_2040=round(max(0.0, f['gap'][2040] - max(0.0, base['gap'][2040])) / per_point, 2)))
    return dict(status='exploratory risk screen on the provisional recommended package', base=base, rows=rows)


def markdown(d):
    b = d['base']
    L = ['## Risks to the recommended package', '',
         'Each row adds one risk to the recommended package (`packages.py`, `recommended`). Gap in $B; a positive gap is '
         'a shortfall. VAT points: what would cover the added FY2040 shortfall at about $%.0fB a point. Generated by '
         '`models/tools/financing-protection/screen.py --markdown`.' % K.VAT_POINT_2040, '',
         '| Risk | Basis | FY2040 | FY2045 | FY2056 | FY2030-39 | VAT points to cover FY2040 |',
         '| --- | --- | --- | --- | --- | --- | --- |',
         '| None (the package as recommended) | | %.1f | %.1f | %.1f | %.1f | 0 |' % (b['gap'][2040], b['gap'][2045], b['gap'][2056], b['gap_2030_39'])]
    for r in d['rows']:
        L.append('| %s | %s | %.1f | %.1f | %.1f | %.1f | %.2f |' % (r['risk'], r['basis'], r['gap'][2040], r['gap'][2045],
                                                                   r['gap'][2056], r['gap_2030_39'], r['vat_points_2040']))
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--markdown', action='store_true')
    d = build()
    print(markdown(d) if ap.parse_args().markdown else json.dumps(d, indent=1, default=str))
