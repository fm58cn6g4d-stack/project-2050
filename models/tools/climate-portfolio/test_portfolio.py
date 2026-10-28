"""Checks for the climate portfolio comparison. Run after `bash models/tools/run-all.sh`:
python3 models/tools/climate-portfolio/test_portfolio.py
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import portfolio as P

a = json.loads((HERE / 'assumptions.json').read_text())
cfg = json.loads((ROOT / 'build/carbon-config.json').read_text())
conf = P.build_config(a, cfg)
runs = P.run_model(conf)
res = {x['id']: x for x in P.analyse(a, runs)}
fails = []
def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok: fails.append(name)

# 1. The selected case reproduces the carbon model's own decided package exactly.
ref = json.loads(subprocess.run(['node', str(ROOT / 'models/tools/carbon/p2050-run.js'), str(ROOT / 'build/carbon-config.json')],
                                check=True, capture_output=True, text=True).stdout)['cases']['full']
mine = runs['cases']['selected']
check('selected case reproduces carbon-model.py case full',
      all(abs(r['energy'] - m['energy']) < 1e-9 and abs(r['credits'] - m['credits']) < 1e-9 for r, m in zip(ref, mine)))

# 2. Each case differs from its comparison only where it should.
check('selected has zero deltas', abs(res['selected']['extra_outlays_bn_2025']['2030_50']) < 1e-9
      and abs(res['selected']['extra_avoided_energy_co2_gt']['2030_50']) < 1e-9)
check('doubling grid cost changes cost, not emissions',
      abs(res['grid_double_cost']['extra_avoided_energy_co2_gt']['2030_50'] - res['grid']['extra_avoided_energy_co2_gt']['2030_50']) < 1e-9
      and abs(res['grid_double_cost']['extra_outlays_bn_2025']['2030_39'] - res['grid']['extra_outlays_bn_2025']['2030_39'] - 120) < 1e-6)
check('weak delivery avoids less than full delivery',
      0 < res['grid_weak_delivery']['extra_avoided_energy_co2_gt']['2030_50'] < res['grid']['extra_avoided_energy_co2_gt']['2030_50'])

# 3. Credit-group removals save money and lose tons; their cost parameters actually remove cost.
for k in ('drop_vehicle_credits', 'drop_heatpump_credit', 'drop_power_credits'):
    x = res[k]
    check(f'{k} saves outlays and loses tons', x['extra_outlays_bn_2025']['2030_39'] < 0 and x['extra_avoided_energy_co2_gt']['2030_50'] < 0)
parts = sum(res[k]['extra_avoided_energy_co2_gt']['2030_50'] for k in ('drop_vehicle_credits', 'drop_heatpump_credit', 'drop_power_credits', 'drop_industry_credits'))
check('credit groups interact: drop-one losses do not sum to the whole bundle',
      abs(parts - res['drop_all_credits']['extra_avoided_energy_co2_gt']['2030_50']) > 0.05)

# 4. Unpriced cases never report a cost per ton.
for k, x in res.items():
    if not x['priced']:
        check(f'{k} has no cost per ton', x['cost_per_extra_ton_undiscounted'] is None and x['saving_per_ton_lost'] is None)

# 5. Portfolios are not additive (so no one should sum rows).
g, w, gw = (res[k]['extra_avoided_energy_co2_gt']['2030_50'] for k in ('grid', 'wx_expand', 'grid_wx'))
check('grid + retrofits differs from the sum of the parts', abs(gw - (g + w)) > 0.01)

# 6. Committed outputs match a fresh run.
built = (ROOT / 'build/climate-portfolio/climate-portfolio-model-results.md')
committed = ROOT / 'legacy/sources/climate-portfolio-model-results.md'
if built.exists() and committed.exists():
    check('committed report matches the build', built.read_text() == committed.read_text())

print('all passed' if not fails else f'{len(fails)} failed')
sys.exit(1 if fails else 0)
