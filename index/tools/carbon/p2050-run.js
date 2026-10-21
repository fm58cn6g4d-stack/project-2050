// Project 2050 driver for the carbon model: runs the cases in a config file written by carbon-model.py and prints JSON.
// Usage: node p2050-run.js config.json > carbon-runs.json
const fs = require('fs');
const M = require('./cfd-model.js');
const HH = require('./cfd-households.js');
const CEX = JSON.parse(fs.readFileSync(__dirname + '/cfd-cex-2024.json', 'utf8'));
const cfg = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const path = tbl => tbl ? (y => tbl[String(y)] != null ? tbl[String(y)] : 0) : null;
const keep = ['year', 'price', 'power', 'transport', 'ldv', 'industry', 'buildings', 'energy', 'process', 'methane', 'n2o', 'hfc', 'ghgNet',
  'below2005', 'ghgBelow2005', 'rev', 'gross', 'pool', 'perShare', 'credits', 'evShare', 'hp', 'pop', 'gasoline', 'retail', 'stored'];
const slim = rows => rows.map(r => Object.fromEntries(keep.map(k => [k, r[k]])));
function polOf(c) {
  const p = Object.assign({}, c.policy);
  if (p.roadPath) p.roadPath = path(p.roadPath);
  return p;
}
const out = { cases: {}, mc: {}, households: {} };
const w = M.world();
for (const c of cfg.cases) {
  const rows = M.simulate(polOf(c), w, path(c.price));
  out.cases[c.id] = slim(rows);
  if (c.households) {
    const r = rows.find(x => x.year === c.households), r0 = rows[0];
    const b = M.simulate(polOf(cfg.cases.find(x => x.id === c.householdsBase)), w, path(cfg.cases.find(x => x.id === c.householdsBase).price)).find(x => x.year === c.households);
    out.households[c.id] = HH.group(r, b, r0, CEX.quintile, c.policy.offset || 0);
  }
}
for (const c of cfg.cases.filter(x => x.mc)) {
  const base = M.world(), N = cfg.mcDraws, seed = cfg.mcSeed;
  // same draws as CFD.monteCarlo, with this case's price path
  const runs = [];
  let s = seed >>> 0; const r = () => { s = (s + 0x6D2B79F5) | 0; let t = Math.imul(s ^ (s >>> 15), 1 | s); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  for (let i = 0; i < N; i++) {
    const wi = JSON.parse(JSON.stringify(base));
    for (const k in M.RANGES) { const [lo, hi] = M.RANGES[k], parts = k.split('.'), get = o => parts.reduce((a, b) => a[b], o);
      const m = Math.max(lo, Math.min(hi, get(base))), u = r(), f = (m - lo) / (hi - lo);
      const v = u < f ? lo + Math.sqrt(u * (hi - lo) * (m - lo)) : hi - Math.sqrt((1 - u) * (hi - lo) * (hi - m));
      const last = parts[parts.length - 1]; parts.slice(0, -1).reduce((a, b) => a[b], wi)[last] = v; }
    const rows = M.simulate(polOf(c), wi, path(c.price));
    runs.push(rows.map(x => ({ year: x.year, energy: x.energy, ghgNet: x.ghgNet, gross: x.gross, rev: x.rev })));
  }
  out.mc[c.id] = runs;
}
process.stdout.write(JSON.stringify(out));
