// Regression checks for the Carbon Dividend Model. Run: node cfd-tests.js (with cfd-model.js alongside).
const M = require('./cfd-model.js'); const w = M.world(); let fail = 0;
const ok = (name, cond, detail) => { console.log((cond ? 'PASS ' : 'FAIL ') + name + (detail ? '  [' + detail + ']' : '')); if (!cond) fail++; };
const near = (a, b, tol) => Math.abs(a - b) <= tol;
const base = M.simulate(M.NOFEE, w), fee = M.simulate({ permitYear: 2027 }, w), baseP = M.simulate({ ...M.NOFEE, permitYear: 2027 }, w);
// 2025 calibration against EIA
ok('2025 energy CO2 ~ 4,904 Mt', near(base[0].energy, 4904, 15), base[0].energy.toFixed(0));
ok('2025 power CO2 ~ 1,485 Mt', near(base[0].power, 1485, 10), base[0].power.toFixed(0));
ok('2025 coal generation ~ 753 TWh', near(base[0].gen.coal, 753, 15), base[0].gen.coal.toFixed(0));
ok('2025 EV sales share 7.8%', near(base[0].evShare, 0.078, 0.001));
// no-policy path inside published ranges
const pc = (a, b) => 100 * (a / b - 1);
ok('power 2025-40 within Rhodium -24..-48%', pc(base[15].power, base[0].power) < -24 && pc(base[15].power, base[0].power) > -48, pc(base[15].power, base[0].power).toFixed(0));
ok('transport 2025-40 within Rhodium -12..-22%', pc(base[15].transport, base[0].transport) < -12 && pc(base[15].transport, base[0].transport) > -22, pc(base[15].transport, base[0].transport).toFixed(0));
ok('energy CO2 2025-50 within EIA -11..-38%', pc(base[25].energy, base[0].energy) < -11 && pc(base[25].energy, base[0].energy) > -38, pc(base[25].energy, base[0].energy).toFixed(0));
// accounting identities, every case and year
const cases = { fee, all: M.simulate({ permitYear: 2027, credits: true, grid: true, nuclear: true, standards: true }, w), base };
for (const k in cases) { let bal = true, pos = true, rev = true, bud = true;
  for (const r of cases[k]) { const g = Object.values(r.gen).reduce((a, c) => a + c, 0);
    if (Math.abs(g + r.unserved - r.G) > 0.02 * r.G) bal = false;
    for (const v of [r.power, r.transport, r.industry, r.buildings, r.process, r.methane, r.gross, r.perShare]) if (!(v >= 0)) pos = false;
    if (Math.abs(Object.values(r.rev).reduce((a, c) => a + c, 0) - r.gross) > 1e-6) rev = false;
    if (Math.abs(r.pool + r.transition + r.net * 0.9 * 0.015 - r.net) > 1e-6 * Math.max(1, r.net)) bud = false; }
  ok(k + ': generation balances demand', bal); ok(k + ': no negative outputs', pos); ok(k + ': revenue sources sum to gross', rev); ok(k + ': dividend + transition + admin = net', bud); }
// behaviour that must hold
ok('fee lowers emissions every year from 2030', fee.slice(5).every((r, i) => r.energy < baseP[i + 5].energy));
ok('fee removes coal by 2036', (fee[11].gen.coal || 0) < 10, (fee[11].gen.coal || 0).toFixed(0));
ok('fee builds gas with capture', fee[15].cap.ccs > 20, fee[15].cap.ccs.toFixed(0) + ' GW in 2040');
ok('wind+solar build never exceeds grid access', fee.every(r => r.build.built <= r.build.grid + 1e-6));
ok('permitting reform raises grid access', fee[10].build.grid > M.simulate({}, w)[10].build.grid);
ok('higher fee -> lower emissions', M.simulate({ permitYear: 2027, startPrice: 80 }, w)[10].energy < fee[10].energy);
ok('credits raise EV share', M.simulate({ permitYear: 2027, credits: true }, w)[10].evShare > fee[10].evShare);
ok('nuclear program builds reactors', cases.all[25].cap.nuc > 110, cases.all[25].cap.nuc.toFixed(0) + ' GW in 2050');
ok('Monte Carlo is reproducible', M.monteCarlo({}, null, 5, 7)[4].pol[10].energy === M.monteCarlo({}, null, 5, 7)[4].pol[10].energy);
// no dead levers: with everything on, at the default and at a high fee, each measure still matters
for (const hi of [{}, { startPrice: 100, step: 15 }]) {
  const full = Object.assign({ permitYear: 2027, credits: true, grid: true, nuclear: true, standards: true }, hi), tag = hi.startPrice ? ' (high fee)' : '';
  const cum = p => M.simulate(p, w).reduce((a, r) => a + r.covered, 0), F = M.simulate(full, w), cF = F.reduce((a, r) => a + r.covered, 0);
  for (const k of ['credits', 'grid', 'nuclear', 'standards']) { const c = cum(Object.assign({}, full, { [k]: false })); ok('removing ' + k + ' raises emissions' + tag, c > cF + 50, ((c - cF) / 1000).toFixed(2) + ' Gt'); }
  const noStd = M.simulate(Object.assign({}, full, { standards: false }), w);
  ok('standards raise EV sales with everything on' + tag, F[25].evShare > noStd[25].evShare + 0.02, (100 * noStd[25].evShare).toFixed(0) + '% -> ' + (100 * F[25].evShare).toFixed(0) + '%');
  ok('power emissions stay non-negative and fall with the fee' + tag, F[25].power >= 0 && F[25].power < 200, F[25].power.toFixed(0) + ' Mt');
}
ok('higher fee raises EV sales even with standards on', M.simulate({ permitYear: 2027, standards: true, startPrice: 100, step: 15 }, w)[13].evShare > M.simulate({ permitYear: 2027, standards: true }, w)[13].evShare + 0.0003);
ok('vehicle rule reaches about 100% of sales by 2050', M.simulate({ permitYear: 2027, standards: true }, w)[25].evShare > 0.97);
ok('long-duration storage and hydrogen appear under the fee', (fee[25].gen.ldes || 0) > 5 && (fee[25].gen.h2 || 0) > 1, (fee[25].gen.ldes || 0).toFixed(0) + ' and ' + (fee[25].gen.h2 || 0).toFixed(0) + ' TWh in 2050');
ok('no hydrogen burned without a fee or credit', baseP.every(r => (r.gen.h2 || 0) < 0.5));
console.log(fail ? fail + ' FAILED' : 'all passed'); process.exit(fail ? 1 : 0);
