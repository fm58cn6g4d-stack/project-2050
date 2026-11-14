// MOD-energy's engine driver: runs Espen's carbon model (models/tools/carbon/cfd-model.js) on the cases run.py writes,
// and prints JSON with every row field the energy model's accounts read. Role: a thin driver, like the carbon model's own
// p2050-run.js, with more fields and households against any base case. Usage: node engine.js config.json > runs.json
const fs = require('fs');
const M = require('../carbon/cfd-model.js');
const HH = require('../carbon/cfd-households.js');
const CEX = JSON.parse(fs.readFileSync(__dirname + '/../carbon/cfd-cex-2024.json', 'utf8'));
const cfg = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const path = tbl => tbl ? (y => tbl[String(y)] != null ? tbl[String(y)] : 0) : null;
const KEEP = ['year', 'price', 'power', 'transport', 'ldv', 'industry', 'buildings', 'energy', 'process', 'methane', 'n2o', 'hfc', 'ghgNet',
  'below2005', 'ghgBelow2005', 'rev', 'gross', 'credits', 'methanePrice', 'cleanShare', 'cesPrice', 'cesAcp', 'evShare', 'hp', 'pop',
  'retail', 'wholesale', 'elecDelta', 'feeHeat', 'stored', 'G'];
const slim = rows => rows.map(r => Object.fromEntries(KEEP.map(k => [k, r[k]])));
function polOf(c) {
  const p = JSON.parse(JSON.stringify(c.policy || {}));
  if (p.roadPath) p.roadPath = path(p.roadPath);
  if (p.methaneFee && p.methaneFee.path) p.methaneFee.path = path(p.methaneFee.path);
  return p;
}
const setP = (o, k, v) => { const p = k.split('.'); const last = p.pop(); p.reduce((a, b) => a[b], o)[last] = v; };
const worldOf = extra => { const w = M.world(); for (const k in Object.assign({}, cfg.world || {}, extra || {})) setP(w, k, Object.assign({}, cfg.world || {}, extra || {})[k]); return w; };
const out = { cases: {}, households: {}, mc: {} }, full = {};
for (const c of cfg.cases) {
  const rows = M.simulate(polOf(c), worldOf(c.world), path(c.price));
  full[c.id] = rows; out.cases[c.id] = slim(rows);
}
for (const c of cfg.cases.filter(x => x.households)) {
  const yr = c.households.year, r = full[c.id].find(x => x.year === yr), b = full[c.households.base].find(x => x.year === yr);
  out.households[c.id] = HH.group(r, b, full[c.id][0], CEX.quintile, 0);
}
// Monte Carlo over the carbon model's uncertain inputs, with the same triangular draws as its own monteCarlo
for (const c of cfg.cases.filter(x => x.mc)) {
  const base = worldOf(c.world), runs = [];
  let s = cfg.mcSeed >>> 0; const rnd = () => { s = (s + 0x6D2B79F5) | 0; let t = Math.imul(s ^ (s >>> 15), 1 | s); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  for (let i = 0; i < cfg.mcDraws; i++) {
    const wi = JSON.parse(JSON.stringify(base));
    for (const k in M.RANGES) { const [lo, hi] = M.RANGES[k], parts = k.split('.'), get = o => parts.reduce((a, b) => a[b], o);
      const m = Math.max(lo, Math.min(hi, get(base))), u = rnd(), f = (m - lo) / (hi - lo);
      const v = u < f ? lo + Math.sqrt(u * (hi - lo) * (m - lo)) : hi - Math.sqrt((1 - u) * (hi - lo) * (hi - m));
      parts.slice(0, -1).reduce((a, b) => a[b], wi)[parts[parts.length - 1]] = v; }
    runs.push(M.simulate(polOf(c), wi, path(c.price)).map(x => ({ year: x.year, energy: x.energy, ghgNet: x.ghgNet, rev: x.rev, cesAcp: x.cesAcp })));
  }
  out.mc[c.id] = runs;
}
out.constants = { E2005: M.E2005, NET2005: M.NET2005, E25: M.E25 };
process.stdout.write(JSON.stringify(out));
