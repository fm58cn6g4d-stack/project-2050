// Household module. Spending data: BLS Consumer Expenditure Survey 2024 (deciles, quintiles, region, type of area) and 2023-24 (region by income).
// For one group of households it returns the fee cost through gasoline, home heating fuel, electricity and everything else, and the dividend.
const HH = (() => {
  // r: policy row, b: no-policy row, r0: 2025 row, T: a CEX table, i: column index, all: the all-households column (table T, index 0)
  function one(r, b, r0, T, i, off) {
    const k = 1 - off, P = r.price;
    const gasoline = T.gasoline[i] * ((r.feeGasoline != null ? r.feeGasoline : 0.0085 * P) / 3.40) * (r.ldv / r0.ldv) * k; // zero when road fuels are outside the fee (Project 2050, D7)            // fee per gallon over price, times remaining fuel use
    const heat = (T.gas[i] * (0.0551 * P / 15.29) + T.oil[i] * 0.0025 * P) * (r.buildings / r0.buildings) * k; // gas per Mcf; fuel oil and propane ~2.5 kg CO2 per dollar (ASSUMED)
    const elec = T.elec[i] * (r.retail - b.retail) / 17.3;                                   // change in the retail price against no policy
    return { gasoline, heat, elec, energy: T.gasoline[i] + T.gas[i] + T.oil[i] + T.elec[i] };
  }
  function group(r, b, r0, T, off) {
    const cuN = r.pop / 2.4, total = r.net * 1000 / cuN;                              // $ per household, national average (2.4 people per household)
    const a = one(r, b, r0, T, 0, off), indAll = Math.max(0, total - a.gasoline - a.heat - a.elec);
    return T.cols.map((name, i) => { const x = one(r, b, r0, T, i, off);
      const other = indAll * (T.exp[i] - x.energy) / (T.exp[0] - a.energy);
      const dividend = r.perShare * (T.people[i] - 0.5 * T.kids[i]);
      const cost = x.gasoline + x.heat + x.elec + other;
      return { name, gasoline: x.gasoline, heat: x.heat, elec: x.elec, other, cost, dividend, net: dividend - cost, pctInc: T.inc[i] ? 100 * (dividend - cost) / T.inc[i] : null }; });
  }
  return { group };
})();
if (typeof module !== 'undefined') module.exports = HH;
