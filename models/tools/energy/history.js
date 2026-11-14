// HI-1's driver: runs the engine's power dispatch (engine/cfd-model.js, dispatch) on each historical year's measured fleet,
// generation and fuel prices, with no carbon price, and prints its coal and gas generation and CO2. Usage: node history.js years.json
const fs = require('fs');
const M = require('./engine/cfd-model.js');
const years = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = years.map(Y => {
  const w = M.world(); Object.assign(w, Y.world);
  const S = Object.assign({ ccs: 0, ldes: 0, hyd: 0, phi: 0, gp: 0, gs: 0, cesL: 0 }, Y.S);
  S.storE = S.stor * 4;
  const d = M.dispatch(S, Y.G, 0, w, Y.year);
  return { year: Y.year, co2: d.emis, coal: d.gen.coal || 0, gas: (d.gen.cc || 0) + (d.gen.ct || 0), curt: d.curt, unserved: d.unserved };
});
process.stdout.write(JSON.stringify(out));
