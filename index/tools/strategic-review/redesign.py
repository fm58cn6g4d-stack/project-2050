#!/usr/bin/env python3
"""Separate financing requirements and climate screens; never writes canonical inputs."""
import argparse
import copy
import hashlib
import importlib.util
import json
import subprocess
import tempfile
from pathlib import Path

from analyze import ROOT, HERE, analyze


def run():
    a = json.loads((HERE / 'redesign-assumptions.json').read_text())
    first = analyze()
    spec = importlib.util.spec_from_file_location('fiscal_redesign', ROOT / 'index/tools/fiscal-model.py')
    f = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f)
    B = f.read_baseline(ROOT / 'index/data/fiscal-baseline.csv')
    model = json.loads((ROOT / 'build/fiscal-model.json').read_text())
    base = model['results']['DEC']['years']
    ledger = json.loads((ROOT / 'build/ledger.json').read_text())
    revenue = {r['id']: r['mid'] for r in ledger['revenue']}
    cuts = {r['id']: r['saves_tn'] for r in ledger['cuts']}
    years = list(range(2026, 2057))
    zero = {y: 0.0 for y in years}

    def path(rid, amount):
        profile = f.PR.REVENUE[rid] if rid in f.PR.REVENUE else f.PR.CUTS[rid]
        return f.row_path(B, amount, profile, rid)

    joint = {y: first['cases'][1]['gap_path_bn'][str(y)] - base[str(y)]['gf_primary'] for y in years}
    extra = [path(rid, amount) for rid, amount in a['extra_low_receipts_tn'].items()]
    g11 = path('G11', revenue['G11'])
    deeper = {y: joint[y] + sum(p[y] for p in extra) + (a['g11_post2039_loss_fraction'] * g11[y] if y >= 2040 else 0) for y in years}
    replacement_parts = [path(rid, cuts[rid]) for rid in a['replacement_rows']]
    replacement = {y: sum(p[y] for p in replacement_parts) for y in years}
    ramp = {y: min(1, max(0, (y - 2029) / 5)) for y in years}
    housing = first['housing'][0]['path_bn']
    service = {y: B[y]['gdp'] * a['service_space_gdp_percent'] / 100 * ramp[y] for y in years}
    scopes = {'Existing agenda': zero, 'Plus housing tranche': housing,
              'Housing plus service space': {y: housing[y] + service[y] for y in years}}
    cases = []
    for architecture, removed in [('Retain existing taxes', zero), ('Replace C19b and C20', replacement)]:
        for stress, lost in [('Central', zero), ('Joint low cases', joint), ('Deeper sensitivity', deeper)]:
            for scope, spending in scopes.items():
                pre = {y: base[str(y)]['gf_primary'] + removed[y] + lost[y] + spending[y] for y in years}
                binding = max(range(2040, 2057), key=lambda y: pre[y] / B[y]['gdp'])
                minimum = max(0, 100 * pre[binding] / B[binding]['gdp'])
                target = minimum + a['maturity_margin_gdp_percent']
                receipts = {y: target / 100 * B[y]['gdp'] * ramp[y] for y in years}
                delta = {y: removed[y] + lost[y] + spending[y] - receipts[y] for y in years}
                gf = {y: base[str(y)]['gf_primary'] + delta[y] for y in years}
                unified = {y: base[str(y)]['prog_primary'] + delta[y] for y in years}
                gi, gd = f.debt_roll(B, gf)
                pi, pd = f.debt_roll(B, unified)
                # Increment-only rate sensitivity: not a shock to all federal debt.
                _, gd_hi = f.debt_roll(B, gf, shift=1.0)
                margins = {y: -100 * pd[y] / B[y]['gdp'] for y in (2035, 2045, 2056)}
                cases.append(dict(architecture=architecture, stress=stress, scope=scope,
                    minimum_net_gdp_percent=minimum, binding_year=binding, target_net_gdp_percent=target,
                    new_receipts_2030_39_tn=sum(receipts[y] for y in range(2030, 2040))/1000,
                    replaced_receipts_2030_39_tn=sum(removed[y] for y in range(2030, 2040))/1000,
                    fy2040_new_receipts_bn=receipts[2040], fy2040_gf_gap_bn=gf[2040],
                    gf_10yr_primary_tn=sum(gf[y] for y in range(2030, 2040))/1000,
                    gf_2056_debt_gdp_percent=100*gd[2056]/B[2056]['gdp'],
                    gf_2056_debt_rate_plus1_gdp_percent=100*gd_hi[2056]/B[2056]['gdp'],
                    maturity_pass=all(gf[y] <= 1e-8 for y in range(2040,2057)),
                    unified_debt_below_baseline=all(pd[y] <= 1e-8 for y in range(2030,2057)),
                    unified_margin_widening=margins[2035] < margins[2045] < margins[2056],
                    incremental_interest_nonpositive_check_years=all(pi[y] <= 1e-8 for y in (2035,2045,2056)),
                    gf_path_bn=gf, new_receipts_path_bn=receipts))

    cfg = json.loads((ROOT / 'build/carbon-config.json').read_text())
    originals = {c['id']: c for c in cfg['cases']}
    jobs = []
    for name, source, change, world in [
        ('selected', 'full', {}, {}), ('grid', 'full', {'grid': True}, {}),
        ('nuclear', 'full', {'nuclear': True}, {}),
        ('grid_and_nuclear', 'full', {'grid': True, 'nuclear': True}, {}),
        ('without_credits', 'full', {'credits': False}, {}),
        ('grid_without_credits', 'full', {'credits': False, 'grid': True}, {}),
        ('fee_repeal', 'nofee', {}, {}), ('grid_fee_repeal', 'nofee', {'grid': True}, {}),
        ('grid_weak_delivery', 'full', {'grid': True}, a['climate']['weak_grid_world']),
        ('grid_double_cost', 'full', {'grid': True}, a['climate']['expensive_grid_world'])]:
        c = copy.deepcopy(originals[source]); c['id'] = name; c['policy'].update(change)
        for k in ('mc', 'households', 'householdsBase'): c.pop(k, None)
        conf = {'world': dict(cfg['world'], **world), 'cases': [c]}
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / 'config.json'; file.write_text(json.dumps(conf))
            out = subprocess.run(['node', str(ROOT/'index/tools/carbon/p2050-run.js'), str(file)], check=True, capture_output=True, text=True)
        jobs.append((name, conf, json.loads(out.stdout)['cases'][name]))
    selected = {r['year']: r for r in jobs[0][2]}
    climate = []
    for name, config, rows in jobs:
        yr = {r['year']: r for r in rows}
        window = range(2030,2051)
        avoided = sum(selected[y]['energy'] - yr[y]['energy'] for y in window) / 1000
        cost = sum(yr[y]['credits'] - selected[y]['credits'] for y in window)
        climate.append(dict(name=name, clean_share_2035_pct=100*yr[2035]['cleanShare'],
            extra_avoided_energy_co2_2030_50_gt=avoided, extra_model_spend_2030_50_bn_2025=cost,
            model_spend_per_extra_tonne_2025_dollars=cost/avoided if avoided > 0 and cost > 0 else None,
            net_ghg_2050_mt=yr[2050]['ghgNet'], config=config,
            years=[{key: row[key] for key in ('year', 'energy', 'ghgNet', 'credits', 'cleanShare')} for row in rows]))
    hashes = dict(first['source_sha256'])
    for p in ['index/tools/strategic-review/redesign.py', 'index/tools/strategic-review/redesign-assumptions.json',
              'index/tools/strategic-review/analyze.py', 'build/carbon-config.json',
              'index/tools/carbon/p2050-run.js', 'index/tools/carbon/cfd-model.js',
              'index/tools/carbon/cfd-households.js', 'index/tools/carbon/cfd-cex-2024.json']:
        hashes[p] = hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
    return dict(assumptions=a, fiscal=cases, climate=climate, source_sha256=hashes)


def render(r):
    lines = ['# Fiscal redesign and climate screening: first results', '',
        'Generated by `index/tools/strategic-review/redesign.py`; exploratory, not adopted. Read with [the first-pass brief](fiscal-redesign-and-participation-2026-10-26.md).', '',
        '## Financing requirements', '',
        'These are required **net new receipts**, not tax rates or scored yields. Replacement cases remove $1.33T of already-counted C19b/C20 receipts first. Receipts ramp over 2030–34; the target adds an illustrative 0.1% GDP maturity margin to the maximum primary gap over FY2040–56. That margin is not a new fiscal rule. Dollar figures here are nominal.', '',
        '| Existing taxes | Stress | Scope | Minimum net (% GDP) | With margin (% GDP) | New receipts 2030–39 ($T) | FY2040 receipts ($B) |',
        '| --- | --- | --- | ---: | ---: | ---: | ---: |']
    for c in r['fiscal']:
        lines.append(f"| {c['architecture']} | {c['stress']} | {c['scope']} | {c['minimum_net_gdp_percent']:.3f} | {c['target_net_gdp_percent']:.3f} | {c['new_receipts_2030_39_tn']:.2f} | {c['fy2040_new_receipts_bn']:.1f} |")
    lines += ['', 'Joint low cases reuse the prior $0.70T loss. The deeper sensitivity adds $0.29T from C38 and $0.25T from G9, plus half of G11’s projected receipts **only from 2040**. GX remains unchanged: no reclaimed overlap revenue and no extra general avoidance haircut. This is not a joint tax score or probability band.', '',
        'Housing reuses the two-million-additional-award illustration. Service space is an unallocated **cost** allowance of 0.1% GDP, reaching full size in 2034; it is not priced participation, care, adaptation or agency readiness. Care entitlement and additional housing/grid capital are excluded.', '',
        'The JSON also reports GF primary paths and debt using the existing interest function, plus existing unified debt/interest comparisons. All cases meet the maturity margin by construction. Dedicated-fund paths, investment-envelope classification and incomplete cash schedules are inherited. D3 is untested for unidentified financing. These are **not full D4 or solvency approvals**. The extra interest-rate sensitivity applies to the GF increment alone, not all federal debt.', '',
        '## Climate portfolio screen', '',
        'Differences are relative to the selected model package over 2030–50. Spending is the model’s `credits` accumulator, which includes assumed grid/nuclear program costs; **constant 2025 dollars, undiscounted**. It is neither a full federal score nor social resource cost. Energy CO2 excludes other greenhouse gases; net GHG endpoints are retained in JSON. A ratio does not establish a budget-neutral swap.', '',
        '| Case | Clean power 2035 (%) | Extra energy CO2 avoided (Gt) | Extra modeled spending ($B) | Spending / extra tonne ($) |',
        '| --- | ---: | ---: | ---: | ---: |']
    for c in r['climate']:
        ratio = c['model_spend_per_extra_tonne_2025_dollars']
        ratio_text = f'{ratio:.0f}' if ratio is not None else '—'
        lines.append(f"| {c['name']} | {c['clean_share_2035_pct']:.1f} | {c['extra_avoided_energy_co2_2030_50_gt']:.3f} | {c['extra_model_spend_2030_50_bn_2025']:.1f} | {ratio_text} |")
    lines += ['', 'The grid cases assume delivery improvements; spending alone does not generate them. Doubling grid cost changes accounting without changing the physical pathway. The weak-delivery case changes three physical parameters together. Credits-off removes the entire modeled restoration bundle and is a diagnostic, not a recommendation to repeal all credits. The nuclear option includes hydro/fusion support and is not a reactor-only comparison. Adaptation, reliability value, regional congestion, air-quality benefits, workforce feasibility and full incidence are not scored.', '',
        'Configuration, annual results, units, assumptions and source hashes are preserved in the JSON. No canonical input or baseline output is overwritten.', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--output', type=Path, default=ROOT/'sources/fiscal-redesign-first-results')
    args = p.parse_args(); result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    args.output.with_suffix('.md').write_text(render(result))
