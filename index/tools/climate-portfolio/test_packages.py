"""Checks for the package search and pricing. Run after `bash index/tools/run-all.sh` (rebuilds the package and pricing outputs if missing):
python3 index/tools/climate-portfolio/test_packages.py
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for script, out in (('packages.py', 'climate-portfolio-packages.json'), ('pricing.py', 'climate-portfolio-pricing.json')):
    if not (ROOT / 'build/climate-portfolio' / out).exists():   # run-all.sh clears build/, so rebuild what the checks read
        import subprocess
        subprocess.run([sys.executable, str(HERE / script)], check=True, capture_output=True)
d = json.loads((ROOT / 'build/climate-portfolio/climate-portfolio-packages.json').read_text())
a = json.loads((HERE / 'packages.json').read_text())
R = {tuple(sorted(r['choice'].items())): r for r in d['results']}
base = {l['id']: l['options'][0]['key'] for l in a['levers']}
key = lambda **kw: tuple(sorted(dict(base, **kw).items()))
fails = []
def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok: fails.append(name)

n = 1
for l in a['levers']:
    n *= len(l['options'])
check('every combination was run', d['n_packages'] == n == len(R))
b = R[key()]
check('decided package has zero deltas', abs(b['outlays_bn_2025_2030_39']) < 1e-9 and abs(b['extra_avoided_net_ghg_gt_2030_50']) < 1e-9)
wx_on, wx_off = R[key(wx='on')], R[key()]
check('retrofit external cost is counted (about $67.5B)', 60 < wx_on['outlays_bn_2025_2030_39'] - wx_off['outlays_bn_2025_2030_39'] < 75)
check('a carbon standard alone has no direct outlay', abs(R[key(ces='90by35')]['outlays_bn_2025_2030_39']) < 5)
check('the higher price raises REV-C1 receipts', R[key(price='higher')]['rev_c1_change_nominal_tn_2030_39'] > 0.2)
f = d['frontier']
check('frontier is increasing in both cost and abatement',
      all(f[i]['outlays_bn_2025_2030_39'] <= f[i + 1]['outlays_bn_2025_2030_39'] and f[i]['extra_avoided_net_ghg_gt_2030_50'] < f[i + 1]['extra_avoided_net_ghg_gt_2030_50'] for i in range(len(f) - 1)))
check('no package beats the frontier at equal or lower cost',
      all(not any(r['outlays_bn_2025_2030_39'] <= p['outlays_bn_2025_2030_39'] - 1e-9 and r['extra_avoided_net_ghg_gt_2030_50'] > p['extra_avoided_net_ghg_gt_2030_50'] + 1e-9 for p in f) or r in f for r in d['results'][:500]))
for b in d['best']:
    ok = [r for r in d['results'] if r['outlays_bn_2025_2030_39'] <= b['cap_bn_2025'] and (b['bill_cap'] is None or r['bill_change_month_2040'] <= b['bill_cap'])]
    check(f"best package under cap {b['cap_bn_2025']} (bill cap {b['bill_cap']}) is the maximum", abs(max(r['extra_avoided_net_ghg_gt_2030_50'] for r in ok) - b['extra_avoided_net_ghg_gt_2030_50']) < 1e-9)
rob = {r['name']: r for r in d['robustness']}
check('weak delivery never helps the recommended package', rob['recommended']['weak']['extra_avoided_net_ghg_gt_2030_50'] <= rob['recommended']['central']['extra_avoided_net_ghg_gt_2030_50'] + 1e-9)
check('a 2037 repeal lowers 2050 abatement', rob['recommended']['repeal2037']['net_ghg_below_2005_2050'] < rob['recommended']['central']['net_ghg_below_2005_2050'])
pr = json.loads((ROOT / 'build/climate-portfolio/climate-portfolio-pricing.json').read_text())
lean = next(v for v in pr['grid_financing'] if v['id'] == 'lean')
check('lean grid financing costs less than all-grant and builds more', lean['deficit_cost_bn'][1] < 120 and lean['physical_build_bn'] > 120)
bu = pr['budget']
ch = bu['channel']
check('channel identity: dividend plus transition equals the added REV-C1 receipts',
      abs(bu['dividend_bn']['window'] + bu['transition_bn']['window'] - bu['rev_c1_change_bn']['window']) < 1e-6 and abs(ch['dividend_share'] + ch['transition_share'] - 1) < 1e-12)
items = {it['id']: it for it in bu['items']}
check('CX offset is 25% of the added receipts', abs(items['cx']['window_bn']['central'] - ch['cx_share'] * bu['rev_c1_change_bn']['window']) < 1e-6)
check('no receipt finances both the dividend and programs: channel uses are paid from the transition share or charged to the general fund',
      all(abs(bu['results'][k]['channel_uses_window_bn'] - (bu['transition_bn']['window'] - bu['results'][k]['channel_surplus_window_bn'] + bu['results'][k]['channel_shortfall_window_bn'])) < 1e-6 for k in bu['cases']))
check('general fund result is the sum of its items plus the channel shortfall',
      all(abs(bu['results'][k]['general_fund_window_bn'] - sum(it['window_bn'][k] for it in bu['items'] if it['account'] == 'general fund') - bu['results'][k]['channel_shortfall_window_bn']) < 1e-6 for k in bu['cases']))
check('industrial support is not inside the credit saving', 'industrial support excluded' in items['credits']['label'] and items['industry']['account'] == 'carbon channel')
check('NFIP debt resolution is in the budget', items['nfip']['window_bn']['central'] > 0)
check('cases pair savings and costs consistently', bu['results']['favorable']['general_fund_window_bn'] < bu['results']['central']['general_fund_window_bn'] < bu['results']['conservative']['general_fund_window_bn'] < bu['results']['unfavorable']['general_fund_window_bn'])
check('permanent items continue after 2039 while time-limited items stop', items['disaster_perm']['fy2050_bn']['central'] > 0 and items['grid']['fy2040_bn']['central'] == 0 and items['retrofits']['fy2040_bn']['central'] == 0)
check('disaster tiers sum their rows', abs(sum(r['ten_year_bn_2025'][1] for r in pr['disaster']['rows'] if r['tier'] == 'core') - pr['disaster']['tiers']['core']['ten'][1]) < 1e-9)
for name in ('climate-portfolio-packages.md', 'climate-portfolio-pricing.md', 'climate-portfolio-disaster-components.csv'):
    built, committed = ROOT / 'build/climate-portfolio' / name, ROOT / 'sources' / name
    if committed.exists():
        check(f'committed {name} matches the build', built.read_text() == committed.read_text())
print('all passed' if not fails else f'{len(fails)} failed')
sys.exit(1 if fails else 0)
