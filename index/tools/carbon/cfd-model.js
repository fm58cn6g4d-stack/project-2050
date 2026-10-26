// Carbon Dividend Model v2: structural simulation (no DOM). Real 2025$. Emissions in Mt CO2e.
// Stocks of power plants, vehicles, heating equipment and industrial capture are tracked year by year;
// operators dispatch and investors choose technologies on cost, including the expected fee.
// SOURCED = published figure. ASSUMED = my judgment, listed on the page. CALIBRATED = set so the no-fee run matches history or published baselines.
const CFD = (() => {
  const Y0 = 2025, Y1 = 2050;
  const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
  const logistic = x => 1 / (1 + Math.exp(-x));
  const EF = { coal: 0.0953, gas: 0.0531 }; // t CO2 per MMBtu (SOURCED: EIA coefficients)

  // ---------- central world: every uncertain input lives here ----------
  const WORLD = {
    // fuel prices (SOURCED: EIA STEO June 2026, 2025 values)
    gasPower: 3.9, coalPower: 2.42, coalVom: 4, emCal: 1.024, /* CALIBRATED to EIA 2025 coal output and power CO2 */ gasoline: 3.4, diesel: 3.9, jet: 2.4, gasBldg: 12.5, gasInd: 5.0,
    elecRes: 17.3, elecCom: 13.4, elecInd: 8.6, // cents/kWh
    // power fleet 2025 (SOURCED: EIA; gas CC/CT split and storage ASSUMED)
    cap: { coal: 170, cc: 290, ct: 222, nuc: 99, wind: 154, solar: 151, stor: 43.6, ccs: 0 },
    gen2025: 4429, hydroOther: 279, loadGrowth: 0.011, // SOURCED: EIA 2025 generation; AEO2026 growth 0.9-1.6%/yr
    cf: { wind: 0.36, solar: 0.225, newWind: 0.40, newSolar: 0.26, nuc: 0.92 },
    // new-build cost, $/kW 2025$ (SOURCED: EIA AEO2023 table x CPI; cross-checked to Lazard 2025 LCOE ranges)
    capex: { solar: 1350, wind: 1900, cc: 1400, ct: 1000, ccs: 3450, stor: 1300, nuc: 8500 },
    fom: { solar: 19, wind: 33, cc: 15, ct: 9, ccs: 34, stor: 46, nuc: 150, coal: 50 },
    decline: { solar: 0.02, wind: 0.007, stor: 0.03 }, // ASSUMED annual real cost decline
    fcr: 0.085, // ASSUMED fixed charge rate
    // ---- build pipeline (replaces fixed annual build caps) ----
    // SOURCED: EIA planned 2026 additions (solar 43.4 GW; wind ~10); LBNL Queued Up 2025 (408 GW with interconnection agreements; solar 68%, wind 19% of the generation queue;
    //   median request-to-operation over 4 years); LBNL developer survey (one-third of siting applications cancelled);
    //   Princeton REPEAT and DOE Needs Study (about 26 GW/yr of wind and solar per percentage point of annual transmission growth; ~1%/yr recently, ~2% long-run average);
    //   GE Vernova (turbine output 20 GW/yr rising to 30 by 2030, sold out through 2030).
    pipe0: { solar: 278, wind: 79 }, icTime: 4, attr: 0.33, withdraw: 0.05,
    k0: { solar: 45, wind: 12 }, kGrow: { solar: 0.25, wind: 0.15 }, kShrink: 0.05,
    txBase: 1.0, txLag: 0.25, gridPerPt: 26, gridBase: 24, gridRetire: 0.5, // gridBase is CALIBRATED so 2026 matches EIA's planned additions; gridRetire (reuse of retired plants' grid connections) ASSUMED
    gasK: [12, 34],
    // firm low-carbon options. SOURCED: DOE Advanced Nuclear Liftoff 2024 (SMR first-of-a-kind ~$13,000/kW, nth-of-a-kind large reactor ~$8,300/kW, first commercial SMRs mid-2030s,
    //   13 GW/yr needed by 2041 for 200 GW by 2050); ORNL (1.41 GW of new conduit hydropower potential). Build ramps and learning rate ASSUMED.
    kFirm0: { ccs: 2, nuc: 1 }, kFirmGrow: { ccs: 0.25, nuc: 0.25 }, firmStart: { ccs: 2032, nuc: 2033 },
    nucCapex0: 13000, nucFloor: 6800, nucLearn: 0.08, nucVar: 11,
    // federal grid build-out program (ASSUMED scale; direction SOURCED: Berkeley/GridLab find advanced conductors can quadruple capacity added by 2035, in 18-36 months per project)
    gpTx: 0.8, gpRecon: 15, gpCost: 12,
    // advanced nuclear, fusion and hydro program (ASSUMED design): 40% investment credit and federal loans for new reactors, first-unit cost share, fusion R&D, marine and conduit hydro support
    npItc: 0.40, npFcr: 0.015, npGrow: 0.08, npFusion: 2, npConduit: 1.41, npWaveCap: 8, npWave0: 0.03, npWaveGrow: 0.35,
    floor: { solar: 20, wind: 8.5 }, pipeline: { solar: 43.4, wind: 10 }, // CALIBRATED floor: state mandates and contracted projects; 2026-27 pipeline SOURCED (EIA)
    // long-duration storage. SOURCED: DOE Long Duration Energy Storage Liftoff 2023 (multi-day systems: $1,900-2,500/kW and 45% round trip today; $1,100/kW and 55-60% needed by 2030;
    //   supply chain of 3 GW/yr by 2030 and 10-15 by 2035). ASSUMED: the cost target is only partly met ($1,500/kW in 2035), supply starts at 1 GW/yr in 2030.
    ldes: { capex0: 2200, capex35: 1500, decline: 0.015, rte0: 0.45, rte1: 0.57, fom: 25, k0: 1, kGrow: 0.3, kMax: 15, start: 2030 },
    // batteries. SOURCED: NREL 2025 (4-hour system $334/kWh in 2024, $243 in 2035, $178 in 2050; of which power equipment about 28%). ASSUMED: new batteries lengthen from 4 hours to 8 by 2038, so 8-hour-plus systems are the norm for new installations by 2040, and to 10 by 2050.
    //   storChem: new chemistries (sodium-ion, iron-based) make the energy part 30% cheaper than NREL's lithium-ion path by 2040. SOURCED direction: IEA says sodium-ion can cost 30% less than lithium iron phosphate; a 2025 bottom-up study finds only 3% by 2035.
    storDur38: 8, storDurEnd: 10, storChem: 0.30,
    // hydrogen burned in gas plants. Price path ASSUMED inside published ranges (IEA $2-4/kg from renewables; ICCT median $5.90 in 2050; BloombergNEF $0.80-1.00): $5/kg delivered in 2030, $2.50 in 2050.
    //   Supply available to power plants ASSUMED: 1 Mt in 2032 rising to 15 Mt in 2050 (DOE's national strategy aims at 50 Mt for all uses). cr: restored 45V credit, $/kg.
    h2: { p30: 5, p50: 2.5, s32: 1, s50: 15, cr: 3 },
    coalSched: 4, // GW/yr scheduled coal retirements (ASSUMED)
    q45: 85, ts: 25, // SOURCED: 45Q credit; CBO transport+storage cost
    elecElast: -0.12, siteScale: 12, dispSpeed: 0.3, vfSolar: 2.2, vfWind: 0.8, curtSlope: 0.6, // ASSUMED; siteScale reflects the spread of Lazard's LCOE ranges
    // light-duty vehicles (SOURCED: FHWA VM-1 2024, Cox 2025 EV share, BNEF pack price, KBB prices)
    ldvSales: 16, evShare2025: 0.078, pack: 108, packDecline: 0.05, packFloor: 60, battKWh: 75, mpgNew: 28, mpgGrowth: 0.008,
    evBeta: 0.06, evNet: 0.42, evNetSales: 0.45, payback: 6, vmtElast: -0.10, mpgElast: 0.2, // ASSUMED/CALIBRATED behavioral parameters
    // trucks, aviation, other (SOURCED shares: EPA Fast Facts 2022)
    trkBeta: 6, trkPrem0: 0.45, trkPremEnd: 0.15, trkAsc: -3.0, trkElast: -0.10, avElast: -0.15,
    // buildings (ASSUMED/CALIBRATED)
    hpPrem: 8, hpBeta: 0.15, hpAsc: -1.02, bldgElast: -0.10, bldgTrend: -0.002,
    // industry (SOURCED: NETL capture costs x CPI + CBO T&S; subsector shares ASSUMED from DOE roadmap)
    htShare: 0.45, htCost: 150, htMax: 0.8, safCost: [220, 400], safMax: [0.1, 0.5], stdSoft: 0.06, stdMpg: 0.01, /* high-temperature heat: 56% of process heat is above 200C (Energy Innovation); cost per ton from Columbia CGEP (capture ~$60, blue hydrogen ~$120, green ~$370). Jet fuel: ICCT ~EUR200/t for waste oils, RFF $142-478/t for ethanol-to-jet. stdSoft, stdMpg ASSUMED */
    indElast: -0.15, ccsCostMult: 1, ccsRate: 0.10, lowTempShare: 0.15, refShare: 0.17, indTrend: 0.006, /* SOURCED: EIA AEO2026 Table 18, industrial direct CO2 grows 0.7% a year */
    // methane abatement scale (SOURCED: EPA 2014 U.S. marginal abatement curves)
    ch4Scale: 1,
    // border adjustment. SOURCED: BEA supply-use tables (2017 detail scaled to 2022 summary) x EPA emission factors per dollar.
    //   Exports: 211 Mt CO2e at U.S. intensity. Imports: 226 Mt if foreign producers matched U.S. intensity; 284 Mt (219 to 374) with ASSUMED per-product foreign/U.S. ratios (border.py). EPA's per-dollar import factors are not used: they compare broad foreign sectors with specific U.S. products.
    impEmb: 284, expEmb: 211, originCredit: 0.15, // originCredit ASSUMED
    // permitting reform at full effect (build limits SOURCED: Princeton REPEAT unconstrained vs 1%/yr transmission; rest ASSUMED)
    pmTx: 1.0, pmIc: 1.5, pmAttr: 0.05, pmFloor: 0.25, pmValue: 0.25, pmCurt: 0.05, gpCurt: 0.05, /* ASSUMED: long-distance lines let more wind and solar be used before output is wasted */ pmCcs: 0.5, // transmission growth back to ~2%/yr (its 1978-2020 average), faster interconnection, fewer federal-nexus cancellations
    feeTx: 0.15, crTx: 0.3, crK: 0.05, // ASSUMED: a fee strengthens the case for new lines; the credit bill includes a transmission investment credit and manufacturing credits
    // restored credits (SOURCED: IRA statutory values; take-up and pass-through ASSUMED)
    // Project 2050 companion measures (all ASSUMED magnitudes): CLI-3 Clean Energy Standard as a tradable-credit shadow price on fossil MWh, adjusted each year toward the target
    //   path and capped at the alternative compliance payment; CLI-6 grid statute (interregional transfer minimums) as extra transmission growth and a higher share of wind and solar
    //   usable before output is wasted; CLI-5 Weatherization able to fund heat pumps as extra conversions of fossil-heated low-income homes.
    cesAcp: 40, cesGain: 300, gsTx: 0.3, gsCurt: 0.02, wxHomes: 0.25,
    crItc: 0.38, crPtc: 34, crEv: 6800, crEvTake: 0.85, crUsed: 1000, crTruck: 0.08, crHp: 6.9, crPack: 15, crYears: 10, crCharge: 0.03, crInd: 0.15, // ITC and PTC include average bonus adders (ASSUMED 8 points and 10%)
    crTruckCost: 20000, crHpCost: 3000, // average 45W and 25C credit per sale ($), so a case that removes one credit can also remove its cost
    crPowerTrigger: 383, crVehYears: null, zevPath: null, zevTrkPath: null, // power-credit phase-out trigger (Mt power CO2); vehicle credits' own term (null: crYears); optional statutory zero-emission sales schedules {year: share}
  };
  // Monte Carlo ranges [low, high] around the central value (triangular)
  const RANGES = {
    gasPower: [3.0, 5.5], loadGrowth: [0.008, 0.016], 'decline.solar': [0.005, 0.035], 'decline.stor': [0.01, 0.05],
    gridPerPt: [18, 36], gridBase: [16, 32], gridRetire: [0.2, 0.8], icTime: [3, 5.5], attr: [0.2, 0.45], 'kGrow.solar': [0.15, 0.35], 'kGrow.wind': [0.08, 0.25], txBase: [0.7, 1.3], pmTx: [0.5, 1.5], 'kFirm0.ccs': [1, 4], 'kFirmGrow.ccs': [0.12, 0.35], 'kFirmGrow.nuc': [0.12, 0.35], nucLearn: [0, 0.15], nucCapex0: [10000, 16000], gpTx: [0.4, 1.2], gpRecon: [8, 30], 'floor.solar': [10, 30], 'floor.wind': [4, 13],
    packDecline: [0.02, 0.08], evBeta: [0.04, 0.09], evNet: [0.25, 0.6], evNetSales: [0.25, 0.65], packFloor: [45, 70], crCharge: [0.01, 0.05], payback: [4, 10], vmtElast: [-0.2, -0.05],
    trkPremEnd: [0.05, 0.3], hpPrem: [5, 12], hpBeta: [0.08, 0.25], bldgElast: [-0.2, -0.05],
    indElast: [-0.3, -0.05], ccsCostMult: [0.8, 1.6], ccsRate: [0.05, 0.15], ch4Scale: [0.7, 1.2],
    impEmb: [219, 374], expEmb: [170, 230], gasoline: [2.9, 4.2],
    pmValue: [0.1, 0.4], feeTx: [0, 0.3], crTx: [0.1, 0.5], crEvTake: [0.6, 1.0],
    indTrend: [0.002, 0.009],
    siteScale: [8, 18], dispSpeed: [0.15, 0.5], vfSolar: [1.5, 3.0], vfWind: [0.5, 1.2], curtSlope: [0.4, 0.9], coalSched: [2, 7], fcr: [0.07, 0.10],
    'capex.solar': [1100, 1700], 'capex.wind': [1600, 2500], lowTempShare: [0.08, 0.25], htCost: [100, 250], 'ldes.capex35': [1100, 2200], 'h2.p50': [1.5, 4.5], 'h2.s50': [5, 30], storDur38: [5, 10], storChem: [0.03, 0.45], storDurEnd: [8, 14], htShare: [0.35, 0.55], stdSoft: [0.03, 0.1], trkBeta: [4, 9], mpgElast: [0.1, 0.3], 'cf.newSolar': [0.23, 0.29],
  };

  // EPA inventory 2022 (SOURCED: Inventory 1990-2022, Table 2-1), Mt CO2e
  const INV = { cement: 41.9, steel: 40.7, ngCO2: 36.5, petCO2: 22.0, petchem: 28.8, ammonia: 12.6, lime: 12.2, waste: 12.4, carbonates: 10.4, neu: 116.0,
    ch4Gas: 173.1, ch4Oil: 39.6, ch4Coal: 50.0, ch4Landfill: 119.8, n2oInd: 10.7, hfc: 178.1, bunkers: 83.2 };
  const E25 = { power: 1485, transport: 1871, industry: 960, buildings: 587 }; // SOURCED: EIA 2025
  const TR = { ldv: 0.572, trk: 0.228, av: 0.094, oth: 0.106 }; // SOURCED: EPA Fast Facts
  const NET2005 = 6536, NET2025 = 5360, E2005 = 5999; // SOURCED: EPA net 2005; Rhodium 2025 (18% below); EIA: 2023 energy CO2 (4,799) was 20% below 2005
  const HFC_BASE = 304, hfcCap = y => y <= 2028 ? 0.6 : y <= 2033 ? 0.3 : y <= 2035 ? 0.2 : 0.15; // SOURCED: AIM Act schedule
  const FOOT = [3.8, 5.3, 6.2, 7.3, 8.2, 9.5, 10.2, 12.1, 14.5, 20.7]; // SOURCED: Fremstad & Paul 2019
  const SCC = { '2.5': [140, 170, 200], '2.0': [230, 270, 310], '1.5': [380, 430, 480] }; // SOURCED: EPA 2023, 2020$
  const pop = y => y <= 2036 ? 349 + 0.8 * (y - 2026) : 357 + 0.35 * (y - 2036); // SOURCED: CBO 2026 endpoints

  const POLICY = {
    startYear: 2030, startPrice: 40, step: 8, stepType: 'linear', ratchet: true, ratchetExtra: 4,
    target2035: 0.35, target2050: 0.55, freezeAt: 0.85,
    dividendShare: 0.90, offset: 0.25, admin: 0.015, sccRate: '2.0',
    cover: { process: true, methane: true, fgas: true, border: true, bunkers: false }, fgasRate: 0.2,
    credits: false, permitYear: null, standards: false, grid: false, nuclear: false, // companion measures: restored clean energy tax credits from 2030; permitting reform enacted in permitYear
    ces: null, gridStatute: false, weatherize: false, // Project 2050: ces = { start, target, year } (CLI-3: 80% clean electricity by 2035); CLI-6; CLI-5 Weatherization
    childShare: 0.5, // dividend shares: adult 1, child childShare (Project 2050's CLI-2A: 1, equal per person)
    roadExempt: false, roadPath: null, othRoad: 0.5, // Project 2050 (D7): gasoline and diesel outside the fee; roadPath(y) = their own per-gallon tax increase as $/t (real), e.g. Moving America's fuel steps; othRoad = share of 'other transport' CO2 that is road-type fuel (ASSUMED)
  };

  // ---------- power: screening-curve dispatch on a linear residual load-duration curve ----------
  const NB = 40;
  function tranches(S, w, P, y) {
    const inc = Math.max(P, y <= (S.q45End || 2035) + 12 ? w.q45 : 0); // capture incentive per stored ton (fee avoided or 45Q, not both); 45Q pays for 12 years
    const t = [];
    const lam = S.cesL || 0; // Clean Energy Standard: a fossil MWh needs credits it must buy ($/MWh)
    const add = (k, gw, hr, fuel, ef, vom, avail, extra) => { if (gw > 0.01) t.push({ k, gw: gw * avail, hr, ef: hr * ef, vc: hr * fuel + vom + P * hr * ef + lam + (extra || 0) }); };
    add('coal', S.coal * 0.3, 9.8, w.coalPower, EF.coal, w.coalVom, 0.8); add('coal', S.coal * 0.4, 10.5, w.coalPower, EF.coal, w.coalVom, 0.8); add('coal', S.coal * 0.3, 11.6, w.coalPower, EF.coal, w.coalVom, 0.8);
    add('cc', S.cc * 0.35, 6.5, w.gasPower, EF.gas, 2.1, 0.87); add('cc', S.cc * 0.4, 7.0, w.gasPower, EF.gas, 2.1, 0.87); add('cc', S.cc * 0.25, 7.7, w.gasPower, EF.gas, 2.1, 0.87);
    add('ct', S.ct * 0.5, 10.0, w.gasPower, EF.gas, 5, 0.9); add('ct', S.ct * 0.5, 11.5, w.gasPower, EF.gas, 5, 0.9);
    const capt = 7.124 * EF.gas * 0.9;
    if (S.ccs > 0.01) t.push({ k: 'ccs', gw: S.ccs * 0.85, hr: 7.124, ef: 7.124 * EF.gas * 0.1, vc: 7.124 * w.gasPower + 6.6 + w.ts * capt + P * 7.124 * EF.gas - inc * capt + 0.1 * lam });
    return t.sort((a, b) => a.vc - b.vc);
  }
  function dispatch(S, G, P, w, y) {
    const windE = S.windE, solE = S.solE, nucE = S.nuc * w.cf.nuc * 8.76;
    const storE = S.storE || S.stor * 4, dur = storE / S.stor, storShift = storE * 0.365, stC = Math.min(0.85, 0.6 + 0.05 * (dur - 4)); // TWh/yr shifted; longer batteries shift more and count for more at the peak
    const vs = (windE + solE) / G, thr = 0.42 + w.pmCurt * (S.phi || 0) + w.gpCurt * (S.gp || 0) + w.gsCurt * (S.gs || 0) + Math.min(Math.min(0.2, 0.13 * dur / 4), 3 * storShift / G);
    const curt = clamp(w.curtSlope * (vs - thr), 0, 0.5);
    const vre = (windE + solE) * (1 - curt);
    const R = Math.max(0, G - nucE - (w.hydroOther + (S.hyd || 0)) - vre), avg = R / 8.76;
    const solShare = solE / G, credS = clamp(0.35 - 1.2 * solShare, 0.04, 0.35);
    const peak = G / 8.76 * 1.5;
    let Lmax = peak - S.nuc * w.cf.nuc - (w.hydroOther + (S.hyd || 0)) / 8.76 - S.wind * 0.12 - S.solar * credS - S.stor * stC;
    Lmax = Math.max(Lmax, avg * 1.2); const Lmin = Math.max(0, 2 * avg - Lmax), tau = Math.min(1, 2 * avg / Lmax);
    const T = tranches(S, w, P, y), gen = {}, hrs = 8760 / NB, surplus = (windE + solE) * curt;
    if ((S.ldes || 0) > 0.01) T.unshift({ k: 'ldes', gw: S.ldes * 0.9, hr: 0, ef: 0, vc: 5, eLeft: surplus * (S.ldesRte || 0.45) }); // long-duration storage: charged only from wind and solar output that would otherwise be wasted
    let emis = 0, vcost = 0, priceSum = 0, unserved = 0; const margin = T.map(() => 0);
    for (let b = 0; b < NB; b++) {
      const x = (b + 0.5) / NB, L = Lmin > 0 ? Lmax - (Lmax - Lmin) * x : Math.max(0, Lmax * (1 - x / tau)); let rem = L, price = 0;
      for (let i = 0; i < T.length && rem > 1e-9; i++) { const g = T[i].eLeft === undefined ? Math.min(T[i].gw, rem) : Math.min(T[i].gw, rem, T[i].eLeft * 1000 / hrs); if (T[i].eLeft !== undefined) T[i].eLeft -= g * hrs / 1000; rem -= g; price = T[i].vc; T[i]._g = (T[i]._g || 0) + g * hrs / 1000; }
      if (rem > 1e-9) { price = 250; unserved += rem * hrs / 1000; }
      priceSum += price;
      T.forEach((t, i) => { margin[i] += Math.max(0, price - t.vc) * hrs / 1000; });
    }
    // hydrogen: gas plants burn it instead of gas where it is cheaper including the fee, up to the supply available
    let h2Mt = 0; const H = S.h2, gasT = T.filter(t => (t.k === 'cc' || t.k === 'ct') && (t._g || 0) > 0);
    if (H && gasT.length) { const sh = t => logistic(t.hr * (w.gasPower + P * EF.gas - H.mm) / w.siteScale), want = gasT.reduce((a, t) => a + t._g * sh(t) * t.hr, 0), f = Math.min(1, H.mt * 134 / Math.max(1e-9, want));
      gasT.forEach(t => { t._h = t._g * sh(t) * f; h2Mt += t._h * t.hr / 134; }); }
    T.forEach(t => { const g = t._g || 0, h = t._h || 0; gen[t.k] = (gen[t.k] || 0) + g - h; if (h) gen.h2 = (gen.h2 || 0) + h; emis += (g - h) * t.ef * w.emCal; vcost += g * (t.vc - P * t.ef - (t.k === 'ccs' ? 0.1 : t.k === 'ldes' ? 0 : 1) * (S.cesL || 0)) + (h ? h * t.hr * (H.mm - w.gasPower) : 0); });
    const curtNet = Math.max(0, curt - (gen.ldes || 0) / (S.ldesRte || 0.45) / Math.max(1, windE + solE));
    const firm = S.nuc * w.cf.nuc + (w.hydroOther + (S.hyd || 0)) / 8.76 + (S.coal * 0.8 + S.cc * 0.87 + S.ct * 0.9 + S.ccs * 0.85) + S.wind * 0.12 + S.solar * credS + S.stor * stC + (S.ldes || 0) * 0.9;
    const coalCF = S.coal > 0.5 ? (gen.coal || 0) / (S.coal * 8.76) : 0;
    // marginal cost of the dearest running coal and cc tranche (for displacement decisions)
    return { gen, emis, vcost, price: priceSum / NB, curt, vs, solShare, windShare: windE / G, firm, peak, coalCF, T, margin, unserved, storShift, surplus, curtNet, h2Mt, stC,
      windE, solE, nucE, vre };
  }

  const pathAt = (p, yy) => { const ks = Object.keys(p).map(Number).sort((a, b) => a - b); if (yy < ks[0]) return 0; for (let i = ks.length - 1; i >= 0; i--) if (yy >= ks[i]) return i === ks.length - 1 ? p[ks[i]] : p[ks[i]] + (p[ks[i + 1]] - p[ks[i]]) * (yy - ks[i]) / (ks[i + 1] - ks[i]); return 0; };
  function expected(pol, y) { // investors look ten years ahead on the statutory schedule (no ratchet)
    if (y < pol.startYear - 1 || pol.startPrice <= 0) return 0; let s = 0;
    for (let k = 0; k < 10; k++) { const yy = Math.max(y + k, pol.startYear), n = yy - pol.startYear; s += (y + k < pol.startYear) ? 0 : (pol.stepType === 'linear' ? pol.startPrice + pol.step * n : pol.startPrice * Math.pow(1 + pol.step / 100, n)); }
    return s / 10;
  }

  // ---------- one simulation ----------
  function simulate(polIn, w, pricePath) {
    const pol = Object.assign({}, POLICY, polIn); pol.cover = Object.assign({}, POLICY.cover, polIn && polIn.cover);
    const S = Object.assign({}, w.cap); S.storE = S.stor * 4; S.ldes = 0; let KL = null; S.windE = S.wind * w.cf.wind * 8.76; S.solE = S.solar * w.cf.solar * 8.76;
    // vehicles: cohorts by age
    const AG = 36, surv = a => 1 / (1 + Math.exp((a - 17) / 4));
    const hist = [0.078, 0.081, 0.076, 0.058, 0.032, 0.018, 0.015, 0.012, 0.01, 0.006]; // EV share of sales, 2025 back to 2016 (2025 SOURCED; earlier ASSUMED)
    const ice = [], ev = [], mpg = [];
    for (let a = 0; a < AG; a++) { const n = w.ldvSales * surv(a), e = hist[a] || 0; ev.push(n * e); ice.push(n * (1 - e)); mpg.push(w.mpgNew * Math.pow(0.988, a)); }
    const vw = a => Math.max(0.35, 1.3 - 0.03 * a);
    const soft = (std, mkt) => std <= 0 ? mkt : Math.min(0.99, std + w.stdSoft * Math.log(1 + Math.exp((mkt - std) / w.stdSoft))); // carmakers differ: some are held up by the standard even when the average is above it
    let hiT = 0, saf = 0, sLag1 = null, sLag2 = null, infra = 0, ldvScale = null, evAsc = null, trkE = 0.005, hp = 0, lowT = 0, indEff = 0, bEff = 0, capNew = 0, fomBase = null, avg0 = null, retailAdj = 0;
    const ccsS = { gasproc: 0, ammonia: 0, cement: 0, steel: 0, refH2: 0 };
    let KC = null, KN = null, nucCum = 1, wave = 0, tx = null, PS = null, PW = null, KS = null, KW = null, bld = { want: 0, ready: 0, grid: 0, industry: 0, built: 0, tx: 0 }, credNext = 0, load0 = 0, powerPrev = 9999, windElig = [], credCost = 0, price = 0, missedPrev = false, frozen = false, ratchetYears = 0, cumAb = 0, e2029 = null, elecLoadPrev = 0, dElast = 0;
    const rows = [];
    let cesBase = null; const clampT = yy => { const c = pol.ces, b = cesBase === null ? 0.45 : cesBase; if (c.year2 && yy > c.year) return yy >= c.year2 ? c.target2 : c.target + (c.target2 - c.target) * (yy - c.year) / (c.year2 - c.year); return yy >= c.year ? c.target : b + (c.target - b) * (yy - (c.start - 1)) / (c.year - (c.start - 1)); };
    for (let y = Y0; y <= Y1; y++) {
      const n = y - Y0;
      // --- fee ---
      if (pricePath) price = pricePath(y);
      else if (y < pol.startYear) price = 0;
      else if (y === pol.startYear) price = pol.startPrice;
      else if (!frozen) { const ex = pol.ratchet && missedPrev ? pol.ratchetExtra : 0; if (ex) ratchetYears++; price += (pol.stepType === 'linear' ? pol.step : price * pol.step / 100) + ex; }
      const P = price, Pe = pricePath ? (pricePath(y) + pricePath(Math.min(Y1, y + 5)) + pricePath(Math.min(Y1, y + 9))) / 3 : Math.max(expected(pol, y), P);
      const dRes = retailAdj, eRes = w.elecRes + dRes, eCom = w.elecCom + dRes, eInd = w.elecInd + dRes; // cents/kWh

      const credPower = credNext;
      const phi = pol.permitYear ? clamp((y - pol.permitYear) / 4, 0, 1) : 0; S.phi = phi; S.gp = pol.grid ? clamp((y - 2031) / 6, 0, 1) : 0; S.gs = pol.gridStatute ? clamp((y - 2030) / 4, 0, 1) : 0; S.q45End = pol.credits ? 2045 : 2035; // current law: construction must start by end-2032, so plants online by about 2035; the credit bill extends it ten years
      const crOn = pol.credits && y >= 2030, cy = y - (2030 + w.crYears), crCons = !crOn ? 0 : cy < 0 ? 1 : cy === 0 ? 0.75 : cy === 1 ? 0.5 : 0, // consumer credits: ten years, then 75% and 50%
         crPow = crOn && (y < 2032 || powerPrev > w.crPowerTrigger); // IRA phase-out: power CO2 at 25% of 2022
      const erode = Math.pow(1.025, -(y - 2029)); credCost = 0;
      const cyV = y - (2030 + (w.crVehYears == null ? w.crYears : w.crVehYears)), crVeh = !crOn ? 0 : cyV < 0 ? 1 : cyV === 0 ? 0.75 : cyV === 1 ? 0.5 : 0; // vehicle credits (30D, 25E, 30C, 45W) may end before the other consumer credits
      // --- light-duty vehicles ---
      const road = yy => pol.roadExempt ? (pol.roadPath ? pol.roadPath(Math.min(Y1, yy)) : 0) : null;
      const PR = pol.roadExempt ? road(y) : P, PRe = pol.roadExempt ? (road(y) + road(y + 5) + road(y + 9)) / 3 : Pe; // road-fuel price signal
      const gasP = w.gasoline + 0.0085 * PR, gasPe = w.gasoline + 0.0085 * PRe;
      const packP = Math.max(w.packFloor, w.pack * Math.pow(1 - w.packDecline, n)) - (crCons ? w.crPack : 0);
      const evCr = crVeh * (w.crEv * erode * w.crEvTake + w.crUsed);
      const prem = w.battKWh * packP * 1.4 - 5000 - evCr;
      if (crVeh && y > 2030) infra += w.crCharge * crVeh; // restored charging credit: lasting improvement in charging access
      const mpgN = w.mpgNew * Math.pow(1 + w.mpgGrowth, n) * Math.pow(gasPe / w.gasoline, w.mpgElast) * (pol.standards ? Math.pow(1 + w.stdMpg, clamp(y - 2031, 0, 9)) : 1); // the standard is grams per mile, so gasoline cars improve too
      const save = w.payback * (12000 / mpgN * gasPe - 12000 * 0.30 * eRes / 100);
      const stockEV = ev.reduce((a, b) => a + b, 0), stock = stockEV + ice.reduce((a, b) => a + b, 0);
      const uCost = -w.evBeta * (prem - save) / 1000, uNet = w.evNet * Math.log((stockEV / stock) / 0.02) + (sLag1 === null ? 0 : w.evNetSales * Math.log(((sLag1 + sLag2) / 2) / w.evShare2025)) + infra;
      if (evAsc === null) evAsc = Math.log(w.evShare2025 / (1 - w.evShare2025)) - uCost - uNet;
      const stdLdv = pol.standards && w.zevPath ? pathAt(w.zevPath, y) : pol.standards && y >= 2032 ? (y <= 2037 ? 0.25 + 0.05 * (y - 2032) : y <= 2040 ? 0.5 + 0.17 * (y - 2037) / 3 : Math.min(1, 0.67 + 0.033 * (y - 2040))) : 0; // successor rules: 100% by 2050
      const evS = y === Y0 ? w.evShare2025 : soft(stdLdv, logistic(evAsc + uCost + uNet));
      sLag2 = sLag1 === null ? evS : sLag1; sLag1 = evS;
      if (y > Y0) { for (let a = AG - 1; a > 0; a--) { const r = surv(a) / surv(a - 1); ice[a] = ice[a - 1] * r; ev[a] = ev[a - 1] * r; mpg[a] = mpg[a - 1]; } ice[0] = w.ldvSales * (1 - evS); ev[0] = w.ldvSales * evS; mpg[0] = mpgN; }
      if (crCons) credCost += w.ldvSales * evS * (evCr + crCons * 45 * w.battKWh * 0.6) / 1000; // 30D plus 45X on domestic cells, $bn
      const vmtF = Math.pow(gasP / w.gasoline, w.vmtElast);
      let gal = 0, evKWh = 0;
      for (let a = 0; a < AG; a++) { gal += ice[a] * vw(a) * 10.8 * vmtF / mpg[a]; evKWh += ev[a] * vw(a) * 10.8 * 0.30; } // million veh x thousand miles = bn miles
      if (ldvScale === null) ldvScale = E25.transport * TR.ldv / gal;
      const ldv = gal * ldvScale;
      // --- trucks, aviation, other ---
      const dslP = w.diesel + 0.0102 * PR, dslPe = w.diesel + 0.0102 * PRe;
      const tprem = w.trkPrem0 + (w.trkPremEnd - w.trkPrem0) * Math.min(1, n / 15) - crVeh * w.crTruck * erode;
      const stdTrk = pol.standards && w.zevTrkPath ? pathAt(w.zevTrkPath, y) : pol.standards && y >= 2032 ? (y <= 2037 ? 0.05 + 0.05 * (y - 2032) : Math.min(0.65, 0.30 + 0.027 * (y - 2037))) : 0; // successor rules: 65% by 2050
      const trkS = soft(stdTrk, logistic(w.trkAsc + w.trkBeta * (dslPe / 6.8 - 2.0 * eCom / 100 - tprem)));
      if (y > Y0) trkE += (trkS - trkE) / 14;
      if (crVeh) credCost += crVeh * 0.55 * trkS * w.crTruckCost * erode / 1000; // 45W: 0.55m truck sales (ASSUMED), $20k average
      const trk = E25.transport * TR.trk * Math.pow(1.005, n) * (1 - trkE) * Math.pow(dslP / w.diesel, w.trkElast);
      const trkTWh = E25.transport * TR.trk * Math.pow(1.005, n) * trkE / 0.0102 / 6.8 * 2.0 / 1000; // Mt -> bn gal -> bn mi -> TWh
      if (y > Y0) saf += 0.15 * (w.safMax[0] * logistic((Pe - w.safCost[0]) / 40) + w.safMax[1] * logistic((Pe - w.safCost[1]) / 80) - w.safMax[0] * logistic(-w.safCost[0] / 40) - w.safMax[1] * logistic(-w.safCost[1] / 80) - saf); // low-carbon jet fuel: waste oils first (limited supply), then alcohol-to-jet and synthetic
      const av = E25.transport * TR.av * Math.pow(1.005, n) * Math.pow((w.jet + 0.00957 * P * (1 - saf)) / w.jet, w.avElast) * (1 - saf);
      const oth = E25.transport * TR.oth * Math.pow(dslP / w.diesel, -0.1);
      const transport = ldv + trk + av + oth;
      const petIdx = (ldv + trk + av) / (E25.transport * (1 - TR.oth));

      // --- buildings: heating stock turnover ---
      const fossH = (w.gasBldg + EF.gas * 1000 * Pe / 1000) / 0.85, hpH = ((eRes + eCom) / 2) / 100 * 293.07 / 2.8;
      const hpS = logistic(w.hpAsc - w.hpBeta * (hpH + w.hpPrem - crCons * w.crHp * erode - fossH));
      if (crCons) credCost += crCons * 84 * (1 - hp) / 18 * hpS * w.crHpCost * erode / 1000; // 25C: 84m fossil-heated homes (ASSUMED from RECS shares)
      if (y > Y0) hp += (1 - hp) / 18 * hpS + (pol.weatherize && y >= 2031 ? w.wxHomes / 84 * (1 - hp) : 0); // CLI-5: Weatherization funds heat pumps, about wxHomes million low-income homes a year
      if (pol.weatherize && y >= 2031) credCost += 0; // its cost is CLI-5's ledger row, not modeled here
      bEff += 0.2 * ((1 - Math.pow((w.gasBldg + 53.1 * P / 1000) / w.gasBldg, w.bldgElast)) - bEff);
      const bBase = E25.buildings * Math.pow(1 + w.bldgTrend, n);
      const buildings = bBase * (1 - hp) * (1 - bEff);
      const hpTWh = bBase * hp / EF.gas * 0.85 / 2.8 / 3.412; // Mt -> TBtu -> TWh

      // --- industry: efficiency, low-temperature electrification, capture ---
      const iBase = E25.industry * Math.pow(1 + w.indTrend, n);
      const refining = iBase * w.refShare * (0.4 + 0.6 * petIdx);
      const otherInd = iBase * (1 - w.refShare);
      indEff += 0.15 * ((1 - Math.pow((7 + 0.06 * P) / 7, w.indElast)) - indEff);
      const heatGap = (eInd / 100 * 293.07 / 3 + 2) - (w.gasInd / 0.8); // $/MMBtu useful heat, heat pump vs gas boiler
      const ltCost = heatGap / (EF.gas / 0.8); // $/t abated before the fee
      const cRate = w.ccsRate * (1 + 0.3 * phi);
      const indCr = crOn && cy < 2 ? w.crInd : 0; // industrial investment credits and grants
      lowT += cRate * (logistic((Pe - ltCost * (1 - indCr)) / 15) - lowT);
      const inc = Math.max(Pe, y <= S.q45End ? w.q45 : 0);
      const cCost = { gasproc: 16.1, ammonia: 19.0, cement: 60.8, steel: 65.9, refH2: 57.3 }; // SOURCED: NETL 2018$
      for (const k in ccsS) { const c = (cCost[k] * 1.27 + w.ts) * w.ccsCostMult * (1 - indCr); if (y > Y0) ccsS[k] += cRate * (logistic((inc - c) / 12) - ccsS[k]); }
      if (y > Y0) hiT += cRate * 0.5 * (logistic((Pe - w.htCost * (1 - indCr)) / 40) - logistic(-w.htCost / 40) - hiT); // furnaces and kilns: capture, hydrogen or electric heat; slow because the equipment lasts decades
      const ltAb = otherInd * w.lowTempShare * lowT, htAb = otherInd * w.htShare * w.htMax * Math.max(0, hiT);
      const refAb = refining * 0.25 * 0.9 * ccsS.refH2;
      const ccsAb = { refH2: refAb, cement: INV.cement * 0.9 * ccsS.cement, steel: INV.steel * 0.6 * ccsS.steel, gasproc: INV.ngCO2 * 0.9 * ccsS.gasproc, ammonia: INV.ammonia * 0.9 * ccsS.ammonia };
      const credInd = indCr * (Math.max(0, ltCost) * ltAb + w.htCost * htAb + Object.keys(ccsAb).reduce((a, k) => a + (cCost[k] * 1.27 + w.ts) * w.ccsCostMult * ccsAb[k], 0)) / 1000; // ESTIMATE of industrial support cost ($bn): its share of abatement cost on abated tons; reported only, not in credits
      const industry = (refining - refAb) + (otherInd - ltAb - htAb) * (1 - indEff);
      const ltTWh = ltAb / (EF.gas / 0.8) / 3 / 3.412;
      const proc = { cement: INV.cement * (1 - 0.9 * ccsS.cement), steel: INV.steel * (1 - 0.6 * ccsS.steel), ngCO2: INV.ngCO2 * (1 - 0.9 * ccsS.gasproc), ammonia: INV.ammonia * (1 - 0.9 * ccsS.ammonia),
        other: INV.petCO2 + INV.petchem + INV.lime + INV.waste + INV.carbonates + INV.neu * (0.5 + 0.5 * petIdx) };
      const process = proc.cement + proc.steel + proc.ngCO2 + proc.ammonia + proc.other;
      const stored = refAb + INV.cement * 0.9 * ccsS.cement + INV.steel * 0.6 * ccsS.steel + INV.ngCO2 * 0.9 * ccsS.gasproc + INV.ammonia * 0.9 * ccsS.ammonia;

      // --- power: demand, dispatch, then retirement and investment for next year ---
      const elecLoad = evKWh + trkTWh + hpTWh + ltTWh;
      dElast += 0.3 * ((1 - Math.pow(Math.max(0.5, (13.2 + dRes) / 13.2), w.elecElast)) - dElast);
      if (y === Y0) load0 = elecLoad;
      const G = w.gen2025 * Math.pow(1 + w.loadGrowth, n) * (1 - dElast) + (elecLoad - load0) * 1.05;
      const L = w.ldes, h2Cr = pol.credits && y >= 2030 ? w.h2.cr * (y <= 2040 ? 1 : clamp((2045 - y) / 5, 0, 1)) : 0; // restored hydrogen credit: ten years of output for plants started in the 2030s
      S.ldesRte = L.rte0 + (L.rte1 - L.rte0) * clamp((y - 2025) / 10, 0, 1);
      S.h2 = y >= 2032 ? { mm: (w.h2.p30 * Math.pow(w.h2.p50 / w.h2.p30, clamp((y - 2030) / 20, 0, 1)) - h2Cr) / 0.134, mt: w.h2.s32 + (w.h2.s50 - w.h2.s32) * (y - 2032) / 18 } : null;
      const d = dispatch(S, G, P, w, y);
      const power = d.emis; credCost += d.h2Mt * h2Cr;
      const fossG = (d.gen.coal || 0) + (d.gen.cc || 0) + (d.gen.ct || 0) + 0.1 * (d.gen.ccs || 0), cleanShare = 1 - fossG / G;
      if (pol.ces && y === pol.ces.start - 1) cesBase = cleanShare;
      const cesTgt = pol.ces && y >= pol.ces.start ? clampT(y) : null, cesAcpBn = cesTgt !== null && (S.cesL || 0) >= w.cesAcp - 1e-6 ? Math.max(0, cesTgt - cleanShare) * G * w.cesAcp / 1000 : 0;
      if (fomBase === null) fomBase = S.coal * w.fom.coal;
      const fixed = capNew + (S.coal * w.fom.coal - fomBase) / 1000;                  // $bn/yr vs 2025
      const avgCost = (d.vcost + P * d.emis + fixed * 1000) / G;                       // $/MWh
      if (avg0 === null) avg0 = avgCost;
      const retailNext = (avgCost - avg0) / 10;                                         // cents/kWh

      // --- non-CO2 and other covered sources ---
      // methane price ($/t CO2e). Project 2050 (REV-C3): a separate methane fee, mf = { start, mult, floor, ogShare, coal, landfill }: the carbon fee times mult (3 = pricing methane
      //   on its 20-year warming potential), never below the restored IRA charge (floor, $/t CO2e), on oil and gas facilities above the size threshold (ogShare of the
      //   sector's methane), coal mines and, optionally, landfills. Without mf, cover.methane prices all three sources at the carbon fee, as the original model did.
      const mf = pol.methaneFee, Pm = mf && y >= mf.start ? (mf.path ? mf.path(y) : Math.max(P * mf.mult, mf.floor || 0)) : 0; // mf.path(y): a set schedule ($/t CO2e, real) instead of a multiple of the carbon fee
      const pOG = mf ? Pm : (pol.cover.methane ? P : 0), pCoal = mf ? (mf.coal ? Pm : 0) : pOG, pLF = mf ? (mf.landfill ? Pm : 0) : pOG, cov = mf ? mf.ogShare : 1;
      const mAb = pOG;
      const abOG = x => w.ch4Scale * (0.27 * (1 - Math.exp(-x / 10)) + 0.045 * Math.min(1, x / 15) + 0.135 * Math.min(1, x / 100));
      const ogAb = abOG(mAb);
      const coalIdx = (d.gen.coal || 0) / 753;
      // certification (Project 2050, REV-C3): a covered facility that certifies, on independent audit and measurement, that it meets the leak-prevention standards
      //   (leak detection and repair, no routine venting or flaring) is exempt; its methane falls by cert.abate. The certified share of covered methane rises from cert.s0 to cert.s1 by cert.year.
      const ct = mf && mf.cert && y >= mf.start ? mf.cert : null, cSh = ct ? ct.s0 + (ct.s1 - ct.s0) * clamp((y - mf.start) / (ct.year - mf.start), 0, 1) : 0;
      const ogBase = (INV.ch4Gas + INV.ch4Oil) * cov;
      const ch4OGc = ogBase * (1 - cSh) * (1 - Math.min(0.6, ogAb)), ch4OGcert = ogBase * cSh * (1 - (ct ? ct.abate : 0));
      const ch4OG = ch4OGc + ch4OGcert + (INV.ch4Gas + INV.ch4Oil) * (1 - cov);
      const ch4Coal = INV.ch4Coal * (0.15 + 0.85 * coalIdx) * (1 - w.ch4Scale * (0.06 * (pCoal > 0 ? 1 : 0) + 0.38 * Math.min(1, pCoal / 60)));
      const ch4LF = INV.ch4Landfill * (1 - w.ch4Scale * 0.11 * Math.min(1, pLF / 50));
      const n2o = INV.n2oInd * (1 - (pol.cover.process ? 0.55 * Math.min(1, P / 20) + 0.17 * Math.min(1, P / 100) : 0));
      const hfcCons = HFC_BASE * hfcCap(y), hfcEmis = INV.hfc * (0.35 + 0.65 * (0.5 * hfcCap(y) + 0.5 * hfcCap(y - 8)) / 0.6);
      const methane = ch4OG + ch4Coal + ch4LF;

      // --- totals, revenue, dividend ---
      const energy = power + transport + industry + buildings;
      const coveredOther = process + methane + n2o + hfcEmis;
      const ghgNet = energy + coveredOther + (NET2025 - (E25.power + E25.transport + E25.industry + E25.buildings) - rows0Other(w));
      const imp = w.impEmb * Math.pow(1 + 0.06 * P / 100, -0.5);
      const rev = { power: P * power, transport: pol.roadExempt ? P * (av + oth * (1 - pol.othRoad)) : P * transport, industry: P * industry, buildings: P * buildings,
        process: pol.cover.process ? P * (process + n2o) : 0, methane: mf ? pOG * ch4OGc + pCoal * ch4Coal + pLF * ch4LF : (pol.cover.methane ? P * methane : 0),
        fgas: pol.cover.fgas ? P * pol.fgasRate * hfcCons : 0,
        border: pol.cover.border ? P * (imp * (1 - w.originCredit) - w.expEmb * (industry + process) / (E25.industry + rows0Proc())) : 0, // export rebates shrink as U.S. industry cleans up
        bunkers: pol.cover.bunkers ? P * INV.bunkers : 0 };
      for (const k in rev) rev[k] /= 1000; // $bn
      const gross = Object.values(rev).reduce((a, b) => a + b, 0);
      const net = gross * (1 - pol.offset), poolD = (gross - (mf ? rev.methane : 0)) * (1 - pol.offset) * pol.dividendShare * (1 - pol.admin); // a separate methane fee (REV-C3) does not feed the dividend
      const pp = pop(y), cs = pol.childShare, perShare = poolD * 1000 / (pp * (1 - (1 - cs) * 0.23)); // under-19s are about 23% of the population
      if (y === 2029) e2029 = energy;
      const t35 = E2005 * (1 - pol.target2035), t50 = E2005 * (1 - pol.target2050);
      const target = e2029 !== null && y >= pol.startYear ? (y <= 2035 ? e2029 + (t35 - e2029) * (y - 2029) / 6 : t35 + (t50 - t35) * Math.min(1, (y - 2035) / 15)) : null;
      missedPrev = target !== null && energy > target; frozen = energy <= E2005 * (1 - pol.freezeAt);
      const fMean = FOOT.reduce((a, b) => a + b, 0) / 10, costPc = net * 1000 / pp, divPc = poolD * 1000 / pp;
      rows.push({ year: y, price: P, power, transport, ldv, industry, buildings, energy, process, methane, n2o, hfc: hfcEmis, covered: energy + coveredOther, ghgNet, target,
        below2005: 1 - energy / E2005, ghgBelow2005: 1 - ghgNet / NET2005, rev, gross, net, pool: poolD, transition: net * (1 - pol.dividendShare), perShare, childShare: cs, family4: perShare * (2 + 2 * cs),
        gen: Object.assign({ nuclear: d.nucE, hydro: w.hydroOther + (S.hyd || 0), wind: d.windE * (1 - d.curt), solar: d.solE * (1 - d.curt) }, d.gen), G, cap: Object.assign({}, S), coalCF: d.coalCF,
        credits: credCost + credPower, credInd, cleanShare, methanePrice: Pm, cesPrice: S.cesL || 0, cesTarget: cesTgt, cesAcp: cesAcpBn, creditsPower: credPower, build: bld, evShare: evS, evStock: stockEV / stock, trkE, hp, lowT, ccs: Object.assign({}, ccsS), stored, elecLoad, retail: 13.2 + dRes, wholesale: d.price,
        gasoline: 0.0085 * PR, feeGasoline: pol.roadExempt ? 0 : 0.0085 * P, natgas: 0.0551 * P, elecDelta: dRes, deciles: FOOT.map(f => divPc - costPc * f / fMean), pop: pp, unserved: d.unserved, missed: missedPrev });

      // --- investment for next year (uses the expected fee) ---
      const dx = Math.abs(Pe - P) > 0.5 ? dispatch(S, G, Pe, w, y) : d;
      const nn = n + 1;
      if (tx === null) { tx = w.txBase; PS = w.pipe0.solar; PW = w.pipe0.wind; KS = w.k0.solar; KW = w.k0.wind; }
      const crNext = pol.credits && y + 1 >= 2030 && (y + 1 < 2032 || power > w.crPowerTrigger);
      const stItc = crNext ? w.crItc : (y + 1 <= 2033 ? 0.3 : y + 1 === 2034 ? 0.225 : y + 1 === 2035 ? 0.15 : 0); // storage credit survives to 2035 under current law
      const cS0 = w.capex.solar * Math.pow(1 - w.decline.solar, nn), cSt0 = w.capex.stor * Math.pow(1 - w.decline.stor, nn);
      const cS = cS0 * (crNext ? 1 - w.crItc : 1), cW = w.capex.wind * Math.pow(1 - w.decline.wind, nn), cSt = cSt0 * (1 - stItc);
      const ptcLev = crNext ? w.crPtc * 0.59 : 0, pmF = 1 + w.pmFloor * phi;
      const lc = (cx, fom, cf) => (cx * w.fcr + fom) / (cf * 8.76);
      const vfS = clamp(1 - w.vfSolar * (1 - w.pmValue * phi) * d.solShare + 3 * d.storShift / G, 0.25, 1), vfW = clamp(1 - w.vfWind * (1 - w.pmValue * phi) * d.windShare, 0.4, 1);
      const ctFirm = (w.capex.ct * w.fcr + w.fom.ct) / 8.76; // $/MWh-equivalent of firming one average kW
      const mc = 1 - Math.min(0.8, 2 * d.curtNet); // marginal curtailment is about twice the average
      const effS = lc(cS, w.fom.solar, w.cf.newSolar) / vfS / mc + 0.25 * ctFirm, effW = (lc(cW, w.fom.wind, w.cf.newWind) - ptcLev) / vfW / mc + 0.3 * ctFirm;
      const capt = 7.124 * EF.gas * 0.9, incE = Math.max(Pe, y + 1 <= S.q45End ? w.q45 : 0);
      const effCC0 = lc(w.capex.cc, w.fom.cc, 0.6) + 6.37 * w.gasPower + 2.1 + Pe * 6.37 * EF.gas;
      const effCCS = lc(w.capex.ccs * w.ccsCostMult, w.fom.ccs, 0.8) + 7.124 * w.gasPower + 6.6 + w.ts * capt + Pe * 7.124 * EF.gas - incE * capt;
      const lamN = S.cesL || 0;
      const effCC = (pol.standards && y + 1 >= 2033 ? Math.max(effCC0, effCCS) + 5 : effCC0) + lamN; // rule: new baseload gas needs capture; CES credits for fossil output
      const nucCx = Math.max(w.nucFloor, w.nucCapex0 * Math.pow(nucCum, Math.log2(1 - w.nucLearn)));
      const nucItc = pol.nuclear && y + 1 >= 2030 ? w.npItc : (y + 1 <= 2033 ? 0.3 : y + 1 === 2034 ? 0.225 : y + 1 === 2035 ? 0.15 : 0); // current law keeps the nuclear credit to 2035
      const nucFcr = w.fcr - (pol.nuclear && y + 1 >= 2030 ? w.npFcr : 0);
      const effN = (nucCx * (1 - nucItc) * nucFcr + w.fom.nuc) / (w.cf.nuc * 8.76) + w.nucVar;
      const best = Math.min(effS, effW, effCC, effCCS, effN);
      // coal retirement: scheduled, plus economic when going-forward cost exceeds the cheapest replacement
      const coalT = dx.T.filter(t => t.k === 'coal'), coalVC = coalT.length ? coalT.reduce((a, t) => a + t.vc, 0) / coalT.length : 0;
      const coalGF = coalVC + w.fom.coal / (Math.max(0.15, dx.coalCF) * 8.76);
      let ret = Math.min(S.coal, w.coalSched) + S.coal * 0.15 * logistic((coalGF - best) / 8) + (dx.coalCF < 0.15 ? S.coal * 0.15 : 0);
      if (pol.standards && y + 1 >= 2033) ret += S.coal / Math.max(1, 2040 - y); // reinstated power plant rule: unabated coal out by 2040
      ret = Math.min(S.coal, ret); S.coal -= ret;
      // energy need next year and economic displacement of running fossil plant
      const need = Math.max(0, w.gen2025 * Math.pow(1 + w.loadGrowth, nn) - w.gen2025 * Math.pow(1 + w.loadGrowth, n)) + Math.max(0, elecLoad - elecLoadPrev) + ret * dx.coalCF * 8.76 * 0.5;
      elecLoadPrev = elecLoad;
      const sc = 9, ws = [Math.exp(-effS / sc), Math.exp(-effW / sc), Math.exp(-effCC / sc), Math.exp(-effCCS / sc), y + 1 >= w.firmStart.nuc ? Math.exp(-effN / sc) : 0], wsum = ws.reduce((a, b) => a + b, 0);
      // displacement: running fossil output that a new plant would undercut, tranche by tranche (coal first once the fee bites)
      const fossilRun = dx.T.filter(t => (t._g || 0) > 0.5 && t.k !== 'ccs' && t.k !== 'ldes');
      const disp = eff => fossilRun.reduce((a, t) => a + t._g * logistic((t.vc - eff) / w.siteScale), 0);
      const dW = ws[0] + ws[1] + ws[3] + ws[4], dS = w.dispSpeed * disp(effS) * ws[0] / dW, dWd = w.dispSpeed * disp(effW) * ws[1] / dW, util = t => clamp(t._g / (t.gw * 8.76), 0.02, 1),
        dispFirm = (fix, vr, cfMax) => fossilRun.reduce((a, t) => a + t._g * logistic((t.vc - (fix / (Math.min(cfMax, util(t)) * 8.76) + vr)) / w.siteScale), 0), // a new firm plant only earns the hours the plant it replaces was running
        dfC = dispFirm(w.capex.ccs * w.ccsCostMult * w.fcr + w.fom.ccs, effCCS - lc(w.capex.ccs * w.ccsCostMult, w.fom.ccs, 0.8), 0.8), dfN = dispFirm(nucCx * (1 - nucItc) * nucFcr + w.fom.nuc, w.nucVar, w.cf.nuc),
        dC = w.dispSpeed * dfC * ws[3] / dW, dN = w.dispSpeed * dfN * ws[4] / dW;
      // what investors want to build
      const wantS = Math.max(nn <= 2 ? w.pipeline.solar : w.floor.solar * pmF, (need * ws[0] / wsum + dS) / (w.cf.newSolar * 8.76));
      const wantW = Math.max(nn <= 2 ? w.pipeline.wind : w.floor.wind * pmF, (need * ws[1] / wsum + dWd) / (w.cf.newWind * 8.76));
      // what can actually be built: mature projects, industry capacity, grid access
      const gp = pol.grid ? clamp((y + 1 - 2029) / 3, 0, 1) : 0;
      tx += w.txLag * (w.txBase + w.pmTx * phi + (crNext ? w.crTx : 0) + (Pe > 1 ? w.feeTx : 0) + w.gpTx * gp + w.gsTx * (S.gs || 0) - tx);
      const T = w.icTime - w.pmIc * phi, at = w.attr - w.pmAttr * phi;
      const readyS = PS / T * (1 - at), readyW = PW / T * (1 - at);
      const grid = w.gridBase + w.gridPerPt * tx + w.gridRetire * ret + w.gpRecon * gp;
      // scarce grid connections are shared in proportion to the energy each technology would deliver; unused share passes to the other
      const eW = wantW * w.cf.newWind, eS = wantS * w.cf.newSolar;
      let mW = Math.min(wantW, readyW, KW, grid * eW / (eW + eS)), mS = Math.min(wantS, readyS, KS, grid - mW);
      mW = Math.min(wantW, readyW, KW, grid - mS);
      bld = { want: wantS + wantW, ready: readyS + readyW, grid, industry: KS + KW, built: mS + mW, tx };
      PS += wantS * 1.2 / (1 - at) - mS / (1 - at) - w.withdraw * PS; PW += wantW * 1.2 / (1 - at) - mW / (1 - at) - w.withdraw * PW;
      PS = Math.max(0, PS); PW = Math.max(0, PW);
      const kg = crNext ? w.crK : 0, gk = (m, K, g) => K * (1 + (m / K > 0.85 ? g + kg : m / K < 0.6 ? -w.kShrink : 0));
      KS = gk(mS, KS, w.kGrow.solar); KW = gk(mW, KW, w.kGrow.wind);
      const gasK = w.gasK[0] + (w.gasK[1] - w.gasK[0]) * clamp((y + 1 - 2027) / 4, 0, 1);
      // firm options: their first-pass share, plus the wind and solar energy the grid could not connect
      const wantE = (wantS * w.cf.newSolar + wantW * w.cf.newWind) * 8.76, U = Math.max(0, wantE - (mS * w.cf.newSolar + mW * w.cf.newWind) * 8.76);
      const needVRE = need * (ws[0] + ws[1]) / wsum, uNeed = U * Math.min(1, needVRE / Math.max(1, wantE)), uDisp = U - uNeed;
      const wf = ws[2] + ws[3] + ws[4], wl = ws[3] + ws[4] || 1e-9;
      const mCC = Math.min(gasK, (need * ws[2] / wsum + uNeed * ws[2] / wf) / (0.6 * 8.76));
      if (KC === null) { KC = w.kFirm0.ccs; KN = w.kFirm0.nuc; }
      const pmC = 1 + w.pmCcs * phi;
      const wantC = (need * ws[3] / wsum + uNeed * ws[3] / wf + dC + Math.min(uDisp, w.dispSpeed * dfC) * ws[3] / wl) / (0.8 * 8.76);
      const wantN = (need * ws[4] / wsum + uNeed * ws[4] / wf + dN + Math.min(uDisp, w.dispSpeed * dfN) * ws[4] / wl) / (w.cf.nuc * 8.76);
      const mCCS = y + 1 < w.firmStart.ccs ? 0 : Math.min(KC * pmC, wantC), mN = y + 1 < w.firmStart.nuc ? 0 : Math.min(KN, wantN);
      if (y + 1 >= w.firmStart.ccs) KC *= 1 + (mCCS / (KC * pmC) > 0.85 ? w.kFirmGrow.ccs : 0);
      if (y + 1 >= w.firmStart.nuc) KN = Math.min(15, KN * (1 + (mN / KN > 0.85 ? w.kFirmGrow.nuc + (pol.nuclear ? w.npGrow : 0) : 0))); // DOE: 13 GW/yr by 2041
      S.nuc += mN; nucCum += mN;
      // advanced hydro under the program: conduit potential built out over a decade, wave from demonstrations
      if (pol.nuclear && y + 1 >= 2031) { const c = y + 1 <= 2040 ? w.npConduit / 10 : 0, wv = Math.min(w.npWave0 * Math.pow(1 + w.npWaveGrow, y + 1 - 2031), Math.max(0, w.npWaveCap - wave)); wave += wv; S.hyd = (S.hyd || 0) + c * 0.5 * 8.76 + wv * 0.3 * 8.76; }
      S.solar += mS; S.solE += mS * w.cf.newSolar * 8.76; S.wind += mW; S.windE += mW * w.cf.newWind * 8.76; S.cc += mCC; S.ccs += mCCS;
      // storage follows solar; firm capacity shortfall filled by turbines or storage on cost
      // long-duration storage replaces gas plants that run few hours, as far as there is wasted wind and solar output to charge it
      const lCx = y + 1 <= 2035 ? L.capex0 + (L.capex35 - L.capex0) * clamp((y + 1 - 2028) / 7, 0, 1) : L.capex35 * Math.pow(1 - L.decline, y + 1 - 2035);
      if (KL === null) KL = L.k0;
      const dfL = dispFirm(lCx * (1 - stItc) * w.fcr + L.fom, 5, 0.35), room = Math.max(0, d.surplus * S.ldesRte - (d.gen.ldes || 0));
      const mL = y + 1 < L.start ? 0 : Math.min(KL, Math.min(w.dispSpeed * dfL, room) / (0.25 * 8.76));
      if (y + 1 >= L.start) KL = Math.min(L.kMax, KL * (1 + (mL / KL > 0.85 ? L.kGrow : 0)));
      S.ldes += mL;
      const durN = y + 1 <= 2038 ? 4 + (w.storDur38 - 4) * clamp((y + 1 - 2028) / 10, 0, 1) : w.storDur38 + (w.storDurEnd - w.storDur38) * (y + 1 - 2038) / 12, durF0 = 0.28 + 0.72 * durN / 4, durF = 0.28 + 0.72 * durN / 4 * (1 - w.storChem * clamp((y + 1 - 2030) / 10, 0, 1)), // new chemistries cut the cost of the energy part below NREL's lithium-ion path
         stCN = Math.min(0.85, 0.6 + 0.05 * (durN - 4)); // new batteries get longer; cost per kW rises with the energy added
      let mSt = mS * 0.35 * durF0 / durF, mCT = 0; // the same spending buys more storage when it is cheaper
      const peakN = (G * (1 + w.loadGrowth)) / 8.76 * 1.5, credS2 = clamp(0.35 - 1.2 * d.solShare, 0.04, 0.35);
      const firmN = S.nuc * w.cf.nuc + (w.hydroOther + (S.hyd || 0)) / 8.76 + S.coal * 0.8 + S.cc * 0.87 + S.ct * 0.9 + S.ccs * 0.85 + S.wind * 0.12 + S.solar * credS2 + S.stor * d.stC + mSt * stCN + S.ldes * 0.9;
      const short = Math.max(0, peakN * 1.13 - firmN);
      if (short > 0) { const kCT = (w.capex.ct * w.fcr + w.fom.ct + 0.08 * 8.76 * Pe * 10.5 * EF.gas) / 0.9, kSt = (cSt * durF * w.fcr + w.fom.stor) / stCN, sh = logistic((kSt - kCT) / 12); mCT = Math.min(short * sh / 0.9, Math.max(0, gasK - mCC)); mSt += (short - mCT * 0.9) / stCN; } // turbines beyond the supply limit are replaced by storage
      const rpl = S.stor / 18, avgD = S.storE / S.stor; // batteries last about 18 years (ASSUMED); worn-out ones are replaced like for like in power, at the duration then on sale
      S.storE += rpl * (durN - avgD);
      S.ct += mCT; S.stor += mSt; S.storE += mSt * durN;
      capNew += (mS * cS + mW * cW + mCC * w.capex.cc + mCCS * w.capex.ccs * w.ccsCostMult + mCT * w.capex.ct + mSt * cSt * durF + mL * lCx * (1 - stItc) + mN * nucCx * (1 - nucItc)) * w.fcr / 1000 + mN * w.fom.nuc / 1000
        + (mS * w.fom.solar + mW * w.fom.wind + mCC * w.fom.cc + mCCS * w.fom.ccs + mCT * w.fom.ct + mSt * w.fom.stor + mL * L.fom) / 1000;
      // credit outlays booked to next year's row: investment credits at build, wind production credit for ten years
      if (crNext) { windElig.push({ twh: mW * w.cf.newWind * 8.76, end: y + 11 }); credNext = (mS * cS0 + mSt * cSt0 * durF + mL * lCx) * w.crItc / 1000; } else credNext = 0;
      if (pol.nuclear && y + 1 >= 2030) credNext += mN * nucCx * w.npItc / 1000 + (y + 1 < 2040 ? w.npFusion + 1 : 0); // reactor credit, fusion R&D, hydro support ($1bn/yr ASSUMED)
      if (pol.grid && y + 1 >= 2030 && y + 1 < 2040) credNext += w.gpCost;
      if (crNext) credNext += 9; // transmission investment credit: 30% of about $30bn a year (ASSUMED)
      credNext += windElig.filter(c => c.end > y + 1).reduce((a, c) => a + c.twh, 0) * w.crPtc / 1000;
      powerPrev = power; retailAdj = retailNext;
      if (pol.ces && y + 1 >= pol.ces.start) { // credit price moves toward the level that meets next year's target path, capped at the alternative compliance payment
        const tgt = clampT(y + 1), sh = cleanShare;
        S.cesL = clamp((S.cesL || 0) + w.cesGain * (tgt - sh), 0, w.cesAcp);
      }
    }
    rows.ratchetYears = ratchetYears;
    return rows;
  }
  function rows0Proc() { return INV.cement + INV.steel + INV.ngCO2 + INV.ammonia + INV.petCO2 + INV.petchem + INV.lime + INV.waste + INV.carbonates + INV.neu; }
  // non-energy covered sources in the base year (for the residual in the economy-wide figure)
  function rows0Other(w) {
    return INV.cement + INV.steel + INV.ngCO2 + INV.ammonia + INV.petCO2 + INV.petchem + INV.lime + INV.waste + INV.carbonates + INV.neu
      + INV.ch4Gas + INV.ch4Oil + INV.ch4Coal + INV.ch4Landfill + INV.n2oInd + INV.hfc;
  }

  // ---------- worlds: central, scenario levers, Monte Carlo ----------
  const getP = (o, k) => k.split('.').reduce((a, b) => a[b], o);
  const setP = (o, k, v) => { const p = k.split('.'); const last = p.pop(); p.reduce((a, b) => a[b], o)[last] = v; };
  const clone = o => JSON.parse(JSON.stringify(o));
  function world(levers) {
    const w = clone(WORLD); if (!levers) return w;
    if (levers.gas != null) w.gasPower = levers.gas;
    if (levers.load != null) w.loadGrowth = levers.load;
    if (levers.tech === 'fast') { w.decline.solar = 0.035; w.decline.stor = 0.05; w.packDecline = 0.08; w.kGrow.solar = 0.35; w.kGrow.wind = 0.22; w.gridPerPt = 32; w.evNet = 0.5; w.evNetSales = 0.55; w.hpPrem = 6; w.ccsCostMult = 0.85; w.trkPremEnd = 0.07; }
    if (levers.tech === 'slow') { w.decline.solar = 0.005; w.decline.stor = 0.01; w.packDecline = 0.02; w.kGrow.solar = 0.15; w.kGrow.wind = 0.08; w.gridPerPt = 20; w.evNet = 0.3; w.evNetSales = 0.3; w.hpPrem = 11; w.ccsCostMult = 1.5; w.trkPremEnd = 0.28; }
    return w;
  }
  function rng(seed) { let s = seed >>> 0; return () => { s = (s + 0x6D2B79F5) | 0; let t = Math.imul(s ^ (s >>> 15), 1 | s); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
  function draw(base, r) {
    const w = clone(base);
    for (const k in RANGES) { const [lo, hi] = RANGES[k], m = clamp(getP(base, k), lo, hi), u = r(), f = (m - lo) / (hi - lo);
      setP(w, k, u < f ? lo + Math.sqrt(u * (hi - lo) * (m - lo)) : hi - Math.sqrt((1 - u) * (hi - lo) * (hi - m))); }
    return w;
  }
  const NOFEE = { startPrice: 0, step: 0, ratchet: false };
  const baseOf = pol => Object.assign({}, pol, NOFEE, { credits: false, standards: false, grid: false, nuclear: false, permitYear: pol && pol.permitYear && pol.permitYear < 2029 ? pol.permitYear : null });
  function run(pol, levers) { const w = world(levers); return { pol: simulate(pol, w), base: simulate(baseOf(pol), w) }; }
  function monteCarlo(pol, levers, N, seed) {
    const base = world(levers), r = rng(seed || 7), out = [];
    for (let i = 0; i < (N || 120); i++) { const w = draw(base, r); out.push({ pol: simulate(pol, w), base: simulate(baseOf(pol), w) }); }
    return out;
  }
  function scc(y, rate) { const t = SCC[rate], x = clamp((y - 2030) / 10, 0, 2), i = Math.min(1, Math.floor(x)); return (t[i] + (t[i + 1] - t[i]) * (x - i)) * 1.24; }
  return { WORLD, RANGES, POLICY, INV, E25, E2005, NET2005, simulate, run, monteCarlo, world, dispatch, scc, NOFEE, baseOf };
})();
if (typeof module !== 'undefined') module.exports = CFD;
