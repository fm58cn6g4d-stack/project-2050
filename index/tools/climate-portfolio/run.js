// Climate portfolio driver for the carbon model: like ../carbon/p2050-run.js, but each case may carry its own world
// overrides, and rows keep the extra fields the portfolio comparison needs (power-side outlays, retail price).
// Usage: node run.js config.json > runs.json
const fs = require('fs');
const M = require('../carbon/cfd-model.js');
const HH = require('../carbon/cfd-households.js');
const CEX = JSON.parse(fs.readFileSync(__dirname + '/../carbon/cfd-cex-2024.json', 'utf8'));
const cfg = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const path = tbl => tbl ? (y => tbl[String(y)] != null ? tbl[String(y)] : 0) : null;
const keep = ['year', 'price', 'power', 'transport', 'industry', 'buildings', 'energy', 'ghgNet', 'below2005', 'ghgBelow2005',
  'rev', 'gross', 'pool', 'perShare', 'credits', 'creditsPower', 'cleanShare', 'cesAcp', 'evShare', 'hp', 'retail', 'elecDelta', 'pop'];
const slim = rows => rows.map(r => Object.fromEntries(keep.map(k => [k, r[k]])));
function polOf(c) {
  const p = Object.assign({}, c.policy);
  if (p.roadPath) p.roadPath = path(p.roadPath);
  if (p.methaneFee && p.methaneFee.path) p.methaneFee = Object.assign({}, p.methaneFee, { path: path(p.methaneFee.path) });
  return p;
}
const setP = (o, k, v) => { const p = k.split('.'); const last = p.pop(); p.reduce((a, b) => a[b], o)[last] = v; };
const worldOf = extra => { const w = M.world(); for (const src of [cfg.world || {}, extra || {}]) for (const k in src) setP(w, k, src[k]); return w; };
const byId = Object.fromEntries(cfg.cases.map(c => [c.id, c]));
const run = c => M.simulate(polOf(c), worldOf(c.world), path(c.price));
const out = { cases: {}, households: {} };
for (const c of cfg.cases) {
  const rows = run(c);
  out.cases[c.id] = slim(rows);
  if (c.households) {
    const b = run(byId[c.householdsBase]).find(x => x.year === c.households);
    out.households[c.id] = HH.group(rows.find(x => x.year === c.households), b, rows[0], CEX.quintile, c.policy.offset || 0);
  }
}
process.stdout.write(JSON.stringify(out));
