import React, { useState, useMemo } from "react";

/* ============================================================
   FLOOR TIME — A 2029 Senate + House Trifecta War Game
   Field data current as of June 10, 2026.
   Senate baseline: 53 R – 47 D (incl. King & Sanders, caucus D).
   House baseline:  ~220 R – 215 D; 218 needed for a majority.
   ============================================================ */

const C = {
  bg: "#0C1320", panel: "#121C2E", panelEdge: "#1E2B42",
  parchment: "#EDE6D6", parchDim: "#B7AE99", brass: "#C9A227",
  dem: "#3E6FB0", demBright: "#5E92D8", gop: "#B0413E", gopBright: "#D4625F",
  ind: "#8E6FB0", green: "#5FA877", amber: "#D9A441", red: "#C75B5B",
  teal: "#3F9C8E",
};
const serif = "'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif";
const mono = "ui-monospace,'SF Mono','Cascadia Mono',Menlo,Consolas,monospace";
const PKG_COLOR = { A: C.teal, B: C.ind };

/* ---------------- 2026 SENATE MAP (candidates as fielded) ---------------- */
const TARGETS_26 = [
  { id: "ME", state: "Maine", dem: "Graham Platner", gop: "Sen. Susan Collins (inc.)",
    note: "Platner won the June 9 primary 78–17 over Mills. RCV general.",
    rating: "Toss-up", archetype: "progressive", collins: true, defFlip: true, defMargin: 2 },
  { id: "NC", state: "North Carolina", dem: "Fmr. Gov. Roy Cooper", gop: "Michael Whatley",
    note: "Open seat (Tillis retiring). Cooper has led most public polling.",
    rating: "Lean D", archetype: "moderate", defFlip: true, defMargin: 4 },
  { id: "OH", state: "Ohio (special)", dem: "Fmr. Sen. Sherrod Brown", gop: "Sen. Jon Husted (appt.)",
    note: "Special for the Vance seat. Winner is up again in 2028.",
    rating: "Toss-up", archetype: "solid", special: true, defFlip: true, defMargin: 1.5 },
  { id: "IA", state: "Iowa", dem: "Rep. Josh Turek", gop: "Rep. Ashley Hinson",
    note: "Open (Ernst retiring). Turek won June 2; Cook moved race to Lean R.",
    rating: "Lean R", archetype: "moderate", defFlip: false, defMargin: 2 },
  { id: "TX", state: "Texas", dem: "Rep. James Talarico", gop: "AG Ken Paxton",
    note: "Talarico won March 3; Paxton beat Cornyn in the runoff w/ Trump.",
    rating: "Lean R", archetype: "moderate", defFlip: false, defMargin: 1.5 },
  { id: "AK", state: "Alaska", dem: "Fmr. Rep. Mary Peltola", gop: "Sen. Dan Sullivan (inc.)",
    note: "Peltola won statewide in 2022. RCV general; primary Aug 18.",
    rating: "Lean R", archetype: "moderate", defFlip: false, defMargin: 1 },
  { id: "NE", state: "Nebraska", dem: "Dan Osborn (Ind.)", gop: "Gov. Pete Ricketts (inc.)",
    note: "Independent rematch model. Caucuses D, high-independence.",
    rating: "Likely R", archetype: "populist", independent: true, defFlip: false, defMargin: 1 },
  { id: "MT", state: "Montana", dem: "Dem. nominee (Bankhead)", gop: "GOP nominee (Alme)",
    note: "Open (Daines off ballot) — first open seat since 1976.",
    rating: "Likely R", archetype: "populist", defFlip: false, defMargin: 1 },
  { id: "FL", state: "Florida (special)", dem: "Dem. nominee (Aug 18)", gop: "Sen. Ashley Moody (appt.)",
    note: "Special for the Rubio seat; winner up again in 2028.",
    rating: "Likely R", archetype: "moderate", special: true, defFlip: false, defMargin: 1 },
];
const DEFENDS_26 = [
  { id: "GA", state: "Georgia", dem: "Sen. Jon Ossoff (inc.)", gop: "Collins/Dooley (runoff Jun 16)",
    note: "One of two D seats in a 2024 Trump state.", rating: "Toss-up", archetype: "moderate", defHold: true, defMargin: 2.5 },
  { id: "MI", state: "Michigan", dem: "Dem. nominee (Aug 4)", gop: "Mike Rogers (presumptive)",
    note: "Open (Peters retiring). Stevens / El-Sayed / McMorrow primary.", rating: "Toss-up", archetype: "moderate", defHold: true, defMargin: 2 },
  { id: "MN", state: "Minnesota", dem: "Dem. nominee (Aug 11)", gop: "GOP nominee",
    note: "Open (Smith retiring). Flanagan–Craig primary.", rating: "Likely D", archetype: "solid", defHold: true, defMargin: 6 },
  { id: "NH", state: "New Hampshire", dem: "Rep. Chris Pappas (presumptive)", gop: "GOP nominee (Sept 8)",
    note: "Open (Shaheen retiring).", rating: "Lean D", archetype: "moderate", defHold: true, defMargin: 4 },
];
const TARGETS_28_STATIC = [
  { id: "WI28", state: "Wisconsin", gop: "Sen. Ron Johnson", note: "Three-term incumbent in a presidential electorate.", rating: "Toss-up", archetype: "moderate", defFlip: true, defMargin: 2 },
  { id: "NC28", state: "North Carolina", gop: "Sen. Ted Budd", note: "Second NC race in two cycles.", rating: "Lean R", archetype: "moderate", defFlip: false, defMargin: 1.5 },
  { id: "IA28", state: "Iowa", gop: "Grassley seat", note: "Grassley would be 95; open-seat probability high.", rating: "Likely R", archetype: "moderate", defFlip: false, defMargin: 1 },
  { id: "MO28", state: "Missouri", gop: "Sen. Eric Schmitt", note: "Reach target; populist-lane model.", rating: "Likely R", archetype: "populist", defFlip: false, defMargin: 1 },
];
const DEFENDS_28 = [
  { id: "GA28", state: "Georgia", dem: "Sen. Raphael Warnock", rating: "Toss-up", archetype: "solid", defHold: true, defMargin: 2 },
  { id: "AZ28", state: "Arizona", dem: "Sen. Mark Kelly", rating: "Lean D", archetype: "moderate", defHold: true, defMargin: 3 },
  { id: "NV28", state: "Nevada", dem: "Sen. Cortez Masto", rating: "Lean D", archetype: "moderate", defHold: true, defMargin: 2 },
  { id: "NH28", state: "New Hampshire", dem: "Sen. Maggie Hassan", rating: "Lean D", archetype: "moderate", defHold: true, defMargin: 3 },
  { id: "PA28", state: "Pennsylvania", dem: "Fetterman seat", rating: "Toss-up", archetype: "moderate", defHold: true, defMargin: 2 },
  { id: "CO28", state: "Colorado", dem: "Appointed seat (Bennet→Gov.)", rating: "Likely D", archetype: "solid", defHold: true, defMargin: 6 },
];
const HOUSE_BELLWETHERS_26 = [
  "AZ-01", "AZ-06", "CA-13", "CA-22", "CO-08", "IA-01", "ME-02", "MI-07", "MI-10", "NE-02",
  "NV-01", "NV-03", "NY-04", "NY-17", "OR-05", "PA-07", "PA-08", "PA-10", "VA-02", "WA-03",
];

const PRECEDENTS = [
  { yr: 1933, pres: "F. Roosevelt", sen: "59 D", hou: "313 D", majors100: 15, note: "Crisis session; 15 major laws in 100 days." },
  { yr: 1965, pres: "L. Johnson", sen: "68 D", hou: "295 D", majors100: 4, note: "Landslide; Medicare/ESEA moving by day 100, signed by August." },
  { yr: 1981, pres: "R. Reagan", sen: "53 R", hou: "192 R*", majors100: 1, note: "*minority House; budget reconciliation as the agenda's spine." },
  { yr: 2009, pres: "B. Obama", sen: "58→60 D", hou: "257 D", majors100: 3, note: "ARRA, Lilly Ledbetter, CHIP inside 100 days." },
  { yr: 2021, pres: "J. Biden", sen: "50+VP D", hou: "222 D", majors100: 1, note: "Rescue Plan via reconciliation; rest queued." },
  { yr: 2025, pres: "D. Trump", sen: "53 R", hou: "220 R", majors100: 0, note: "Executive action + CRA; major bill after day 100." },
];

/* THE AGENDA — recon: 'full' fiscal | 'partial' (only the fiscal core is recon-able) | 'none' (Byrd-ineligible) */
const BILLS = [
  { id: "ftv", name: "Freedom to Vote + John Lewis VRAA", recon: "none", democracy: true, houseSweep: 0.22,
    desc: "National voting standards, automatic registration, redistricting rules, preclearance restoration, plus small-dollar public matching (6:1). Rides the democracy carve-out.",
    defect: { solid: 0.005, moderate: 0.04, populist: 0.10, progressive: 0.0 }, gopPool: 1, gopProb: 0.30, salience: 10 },
  { id: "ces", name: "Clean Energy Standard & Carbon Dividend Act", recon: "partial", houseSweep: 0.38,
    desc: "80×35 clean electricity standard, federal transmission-permitting authority and NEPA reform (9→4 yrs), DOE loan authority and $900B in domestic-content clean-energy credits, plus an economy-wide carbon fee returned as a quarterly Clean Energy Dividend check — a felt benefit that buys the bill a constituency.",
    defect: { solid: 0.01, moderate: 0.14, populist: 0.26, progressive: 0.0 }, gopPool: 2, gopProb: 0.10, salience: 9 },
  { id: "pro", name: "PRO Act & Sectoral Bargaining", recon: "none", houseSweep: 0.38,
    desc: "Full PRO Act (ABC test, card-check, striker protections, right-to-work override) combined with sectoral bargaining frameworks and portable benefits; paired with NLRB and OSHA executive action.",
    defect: { solid: 0.01, moderate: 0.18, populist: 0.04, progressive: 0.0 }, gopPool: 2, gopProb: 0.12, salience: 8 },
  { id: "pub", name: "Public Option / Medicare at 55", recon: "partial", houseSweep: 0.42,
    desc: "ACA public plan + Medicare buy-in at 55, plus Medicare dental/vision/hearing and long-term-care benefits, Medicaid expansion completion, and expanded drug-price negotiation as the fiscal core.",
    defect: { solid: 0.01, moderate: 0.25, populist: 0.12, progressive: 0.0 }, gopPool: 0, gopProb: 0, salience: 9 },
  { id: "care", name: "Universal Pre-K & Child Care", recon: "full", houseSweep: 0.20,
    desc: "Federal-state pre-K match, child-care subsidy cap at 7% of income.",
    defect: { solid: 0.005, moderate: 0.08, populist: 0.08, progressive: 0.0 }, gopPool: 1, gopProb: 0.10, salience: 8 },
  { id: "hou", name: "Housing Abundance & Supply Act", recon: "partial", houseSweep: 0.18,
    desc: "Builds on the ROAD to Housing Act (enacted July 2026 \u2014 deregulation with no money): adds the capital ROAD lacked \u2014 a $250B revolving construction-loan fund, LIHTC expansion, public-housing capital, 400k vouchers \u2014 and the HUD staffing to actually execute ROAD's 35 stalled directives. Capital onto already-reformed zoning converts to units far more efficiently.",
    defect: { solid: 0.005, moderate: 0.06, populist: 0.08, progressive: 0.01 }, gopPool: 4, gopProb: 0.20, salience: 8 },
  { id: "imm", name: "Comprehensive Immigration Reform", recon: "none", houseSweep: 0.62,
    desc: "Pathway for Dreamers/TPS/farmworkers/10-year residents, asylum overhaul (180-day timeline), visa modernization, and DHS restructuring — separating customs from interior enforcement into a Humanitarian Processing Service.",
    defect: { solid: 0.02, moderate: 0.30, populist: 0.45, progressive: 0.0 }, gopPool: 4, gopProb: 0.12, salience: 7 },
  { id: "gun", name: "Universal Background Checks", recon: "none", houseSweep: 0.45,
    desc: "Point-of-sale checks for all transfers; charleston-loophole closure.",
    defect: { solid: 0.01, moderate: 0.10, populist: 0.35, progressive: 0.0 }, gopPool: 4, gopProb: 0.18, salience: 7 },
  { id: "tax", name: "Billionaire Minimum Income Tax", recon: "full", houseSweep: 0.30,
    desc: "25% minimum on >$100M households incl. unrealized gains; IRS funding.",
    defect: { solid: 0.01, moderate: 0.20, populist: 0.05, progressive: 0.0 }, gopPool: 0, gopProb: 0, salience: 7 },
  { id: "dc", name: "D.C. Statehood", recon: "none", democracy: true, houseSweep: 0.38,
    desc: "Admission of Douglass Commonwealth. Art. IV §3 needs only simple majorities — the 60-vote wall is the filibuster rule, not a constitutional threshold.",
    defect: { solid: 0.02, moderate: 0.30, populist: 0.50, progressive: 0.0 }, gopPool: 0, gopProb: 0, salience: 6 },
  { id: "ctc", name: "Permanent Expanded Child Tax Credit", recon: "full", houseSweep: 0.25,
    desc: "$3,000–3,600/child, fully refundable, paid monthly — the 2021 ARP credit made permanent. The moderate resistance is the old work-requirement fight.",
    defect: { solid: 0.01, moderate: 0.18, populist: 0.15, progressive: 0.0 }, gopPool: 1, gopProb: 0.10, salience: 9 },
  { id: "rev", name: "Corporate & High-Income Tax Fairness Act", recon: "full", houseSweep: 0.30,
    desc: "Corporate rate increase, top marginal bracket, carried-interest close, capital-gains reform. The rate hikes are where the Sinema-lane moderates balk.",
    defect: { solid: 0.02, moderate: 0.25, populist: 0.05, progressive: 0.0 }, gopPool: 0, gopProb: 0, salience: 6 },
  { id: "wage", name: "Living Wage & Small-Business Transition Act", recon: "none", houseSweep: 0.30,
    desc: "$17 then indexed to two-thirds of the median, with a longer small-employer phase-in, a regional circuit-breaker for low-wage rural counties, a refundable small-business transition credit, and a recession off-ramp. The wage mandate is Byrd-barred and needs full reform; the small-business credit can ride reconciliation.",
    defect: { solid: 0.02, moderate: 0.25, populist: 0.20, progressive: 0.0 }, gopPool: 2, gopProb: 0.10, salience: 8 },
  { id: "fees", name: "Junk Fees & Consumer Protection Act", recon: "none", houseSweep: 0.15,
    desc: "Bans hidden fees on tickets, hotels, banking, telecom; all-in pricing. Felt immediately at checkout; unusually bipartisan.",
    defect: { solid: 0.005, moderate: 0.08, populist: 0.05, progressive: 0.0 }, gopPool: 4, gopProb: 0.20, salience: 6 },
  { id: "cft", name: "Campaign Finance Transparency (DISCLOSE)", recon: "none", democracy: true, houseSweep: 0.20,
    desc: "Dark-money disclosure, beneficial-ownership of political spending, coordination rules. Rides the democracy carve-out as part of the Freedom to Vote family.",
    defect: { solid: 0.005, moderate: 0.06, populist: 0.08, progressive: 0.0 }, gopPool: 1, gopProb: 0.10, salience: 5 },
  { id: "eth", name: "Government Ethics & Anti-Corruption Act", recon: "none", houseSweep: 0.28,
    desc: "Congressional stock-trading ban, executive divestiture (codifying the Day-1 EO), revolving-door limits, IG protections, emoluments penalties, and a multi-agency enforcement reorientation. Good-government, not election mechanics — no democracy carve-out.",
    defect: { solid: 0.03, moderate: 0.18, populist: 0.10, progressive: 0.02 }, gopPool: 3, gopProb: 0.18, salience: 7 },
  { id: "scotus", name: "Supreme Court Ethics & Accountability Act", recon: "none", houseSweep: 0.30,
    desc: "Binding code of conduct, recusal standards, gift/travel disclosure. Contentious on separation-of-powers grounds; no carve-out, party-line.",
    defect: { solid: 0.02, moderate: 0.28, populist: 0.15, progressive: 0.0 }, gopPool: 0, gopProb: 0, salience: 5 },
  { id: "anti", name: "Antitrust Enforcement & Competition Act", recon: "partial", houseSweep: 0.30,
    desc: "Merger-review overhaul, updated competition standards, and an FTC/DOJ enforcement-funding core that can ride reconciliation. Cross-ideological — some populist-right support.",
    defect: { solid: 0.02, moderate: 0.25, populist: 0.05, progressive: 0.0 }, gopPool: 3, gopProb: 0.15, salience: 6 },
  { id: "repro", name: "Reproductive Freedom Act", recon: "none", houseSweep: 0.30,
    desc: "Codify Roe's protections nationally (WHPA), protect contraception and IVF, shield interstate travel and providers. Party-line with narrow pro-choice GOP crossover; faces post-Dobbs commerce-clause litigation.",
    defect: { solid: 0.005, moderate: 0.15, populist: 0.12, progressive: 0.0 }, gopPool: 2, gopProb: 0.15, salience: 9 },
  { id: "eq", name: "Equality Act", recon: "none", houseSweep: 0.28,
    desc: "Sexual orientation and gender identity added to federal civil-rights law — employment, housing, credit, public accommodations — codifying and extending Bostock.",
    defect: { solid: 0.005, moderate: 0.12, populist: 0.18, progressive: 0.0 }, gopPool: 2, gopProb: 0.12, salience: 7 },
  { id: "pfml", name: "Paid Family & Medical Leave", recon: "full", houseSweep: 0.18,
    desc: "12 weeks of paid family and medical leave as a national social-insurance program — the FAMILY Act model. Fully fiscal (payroll-financed benefit), reconciliation-eligible.",
    defect: { solid: 0.005, moderate: 0.10, populist: 0.08, progressive: 0.0 }, gopPool: 1, gopProb: 0.10, salience: 8 },
  { id: "cj", name: "Justice & Public Safety Reform Act", recon: "none", houseSweep: 0.45,
    desc: "Federal cannabis legalization with expungement, sentencing reform (retroactive crack parity, mandatory-minimum relief), and national policing standards (qualified-immunity reform, decertification registry). Tough-on-crime defection risk; libertarian-right crossover on cannabis.",
    defect: { solid: 0.02, moderate: 0.25, populist: 0.30, progressive: 0.0 }, gopPool: 3, gopProb: 0.12, salience: 7 },
  { id: "edu", name: "Education & Opportunity Act", recon: "full", houseSweep: 0.12,
    desc: "Title I roughly doubled ($11.2B\u2192$26B), a statutory path to full 40% IDEA funding, Pell raised to $9,500, and SAVE/PSLF restoration. Overwhelmingly fiscal — a clean reconciliation rider.",
    defect: { solid: 0.005, moderate: 0.06, populist: 0.06, progressive: 0.0 }, gopPool: 1, gopProb: 0.10, salience: 6 },
  { id: "vets", name: "Veterans Health & Capacity Act", recon: "full", houseSweep: 0.05,
    desc: "12,000 new VA mental-health clinicians, claims-processing overhaul to a 125-day target, rural community-care expansion. The most bipartisan bill on the board.",
    defect: { solid: 0.005, moderate: 0.02, populist: 0.02, progressive: 0.0 }, gopPool: 8, gopProb: 0.50, salience: 6 },
  { id: "wp", name: "War Powers & Iran Accountability Act", recon: "none", houseSweep: 0.15,
    desc: "First-ever congressional-notification framework before military strikes, sunset provisions on AUMFs, and the Iran ceasefire/oversight architecture. Constitutional-prerogative crossover from the anti-war right.",
    defect: { solid: 0.01, moderate: 0.08, populist: 0.05, progressive: 0.0 }, gopPool: 4, gopProb: 0.20, salience: 6 },
  { id: "ss", name: "Social Security Expansion Act", recon: "none", houseSweep: 0.25,
    desc: "Across-the-board benefit increase, a more accurate elderly cost-of-living index, and lifting the payroll cap on earnings above $250K. Section 310(g) explicitly bars Social Security changes from reconciliation \u2014 a second Byrd-style wall; regular order only.",
    defect: { solid: 0.01, moderate: 0.18, populist: 0.05, progressive: 0.0 }, gopPool: 1, gopProb: 0.05, salience: 8 },
  { id: "pr", name: "Puerto Rico Status Act", recon: "none", democracy: true, houseSweep: 0.30,
    desc: "A binding, federally sponsored referendum among statehood, independence, and sovereignty in free association \u2014 with Congress committed to honor the result. Self-determination for 3.2 million disenfranchised citizens.",
    defect: { solid: 0.015, moderate: 0.15, populist: 0.25, progressive: 0.0 }, gopPool: 2, gopProb: 0.15, salience: 5 },
];
const BILL_BY_ID = Object.fromEntries(BILLS.map((b) => [b.id, b]));

/* Reform-vote propensity by archetype, split by depth.
   These represent ORDINARY party discipline on a procedural rules vote, which is
   much higher than discipline on a contested policy bill — senators rarely cross
   their own leadership on the rules themselves. The genuinely hard resistance to
   reform (the Manchin/Sinema-style holdouts) is captured separately by the
   holdout slider below, not re-encoded here. Carve-out propensities are still
   set >= full-reform propensities for every archetype, which guarantees the
   monotonicity property: the harder reform can never make a democracy bill's
   odds worse than the carve-out's. */
const REFORM_P_CARVEOUT = { solid: 0.995, progressive: 0.998, moderate: 0.92, populist: 0.80, institutionalist: 0.65 };
const REFORM_P_FULL     = { solid: 0.99,  progressive: 0.995, moderate: 0.85, populist: 0.65, institutionalist: 0.50 };
const HOUSE_FRONTLINE = 34;
const HOUSE_DRAG = 0.11;

function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const cl = (v, a, b) => Math.max(a, Math.min(b, v));
const pct = (x) => `${Math.round(x * 100)}%`;
const caution = (m) => cl(1 + (5 - m) * 0.07, 0.7, 1.6);
const memObjP = (bill, m) => cl((bill.defect[m.archetype] ?? bill.defect.moderate) * caution(m.margin) * (m.ind ? 1.35 : 1), 0, 0.95);

/* ============================================================
   CORE SIMULATION (pure) — Senate × House → enactment.
   Reconciliation privilege flows ONLY through package membership;
   a package is one bill bundling many provisions, so a member is a
   No on the package if they'd oppose ANY bundled provision.
   ============================================================ */
function runSim({ dSeats, roster, houseD, fmode, reconAssign, demWH, holdouts, seed, N }) {
  const rng = mulberry32(seed);
  const solidCount = dSeats - roster.length;
  const pkgBills = { A: [], B: [] };
  BILLS.forEach((b) => { if (b.recon !== "none" && (reconAssign[b.id] === "A" || reconAssign[b.id] === "B")) pkgBills[reconAssign[b.id]].push(b); });
  const packagedIds = new Set([...pkgBills.A, ...pkgBills.B].map((b) => b.id));

  const ctr = {}; BILLS.forEach((b) => { ctr[b.id] = { senFull: 0, house: 0, enFull: 0 }; });
  const pkgCtr = { A: { sen: 0, house: 0, en: 0 }, B: { sen: 0, house: 0, en: 0 } };
  let cCarve = 0, cFull = 0;

  for (let t = 0; t < N; t++) {
    // Per-bill regular-order Senate yes-counts + per-member objection matrix (for package unions)
    const billYes = {}; BILLS.forEach((b) => { billYes[b.id] = solidCount - (rng() < b.defect.solid * solidCount ? 1 : 0); });
    const obj = roster.map((m) => {
      const o = {};
      BILLS.forEach((b) => { const objected = rng() < memObjP(b, m); o[b.id] = objected; if (!objected) billYes[b.id] += 1; });
      return o;
    });
    // Reform tallies
    let rvC = Math.round(solidCount * REFORM_P_CARVEOUT.solid), rvF = Math.round(solidCount * REFORM_P_FULL.solid);
    roster.forEach((m) => { if (rng() < (REFORM_P_CARVEOUT[m.archetype] ?? 0.72)) rvC++; if (rng() < (REFORM_P_FULL[m.archetype] ?? 0.58)) rvF++; });
    rvC -= holdouts; rvF -= holdouts;
    const carveAvail = rvC >= 50 && demWH, fullAvail = rvF >= 50 && demWH;
    if (carveAvail) cCarve++; if (fullAvail) cFull++;

    // Regular-order pass for every bill (no recon privilege here)
    BILLS.forEach((b) => {
      let cross = 0; for (let g = 0; g < Math.max(0, b.gopPool); g++) if (rng() < b.gopProb) cross++;
      const total = billYes[b.id] + cross;
      const carved = (fmode === "carveout" && b.democracy) || (fmode === "majority");
      const reformAvail = b.democracy ? carveAvail : fullAvail;
      const cloture = carved ? (reformAvail ? total >= 50 : total >= 60) : total >= 60;
      const floor = total >= 51 || (total === 50 && demWH);
      const passFull = cloture && floor;
      let hDef = 0; for (let f = 0; f < HOUSE_FRONTLINE; f++) if (rng() < b.houseSweep * HOUSE_DRAG) hDef++;
      const housePass = houseD >= 218 && (houseD - hDef) >= 218;
      if (passFull) ctr[b.id].senFull++;
      if (housePass) ctr[b.id].house++;
      if (passFull && housePass) ctr[b.id].enFull++;
    });

    // Packages: union-of-objections fragility, simple-majority floor, no GOP crossover
    (["A", "B"]).forEach((P) => {
      const bills = pkgBills[P]; if (!bills.length) return;
      let pYes = solidCount;
      roster.forEach((m, i) => { if (!bills.some((b) => obj[i][b.id])) pYes += 1; });
      const pSenate = pYes >= 51 || (pYes === 50 && demWH);
      let hDef = 0; for (let f = 0; f < HOUSE_FRONTLINE; f++) { if (bills.some((b) => rng() < b.houseSweep * HOUSE_DRAG)) hDef++; }
      const pHouse = houseD >= 218 && (houseD - hDef) >= 218;
      const pEnact = pSenate && pHouse;
      if (pSenate) pkgCtr[P].sen++; if (pHouse) pkgCtr[P].house++; if (pEnact) pkgCtr[P].en++;
    });
  }

  const bills = BILLS.map((b) => {
    const enFull = ctr[b.id].enFull / N;
    const senFull = ctr[b.id].senFull / N;
    const house = ctr[b.id].house / N;
    const pkg = packagedIds.has(b.id) ? reconAssign[b.id] : null;
    const enCore = pkg ? pkgCtr[pkg].en / N : enFull; // packaged → fiscal core rides the package
    const headline = pkg ? enCore : enFull;
    return { ...b, enFull, senFull, house, enCore, pkg, headline };
  });
  const expectedEnacted = bills.reduce((a, b) => a + b.headline, 0);
  const packages = (["A", "B"]).map((P) => ({
    id: P, bills: pkgBills[P].map((b) => b.id),
    sen: pkgCtr[P].sen / N, house: pkgCtr[P].house / N, en: pkgCtr[P].en / N,
  }));
  return { bills, expectedEnacted, reformCarveout: cCarve / N, reformFull: cFull / N, packages };
}

/* expected enactments only — for the fast sensitivity sweep */
function expOnly(p) { return runSim({ ...p, N: 1200 }).expectedEnacted; }

/* ============================================================ */
export default function TrifectaSimulator() {
  const init = (arr, key) => Object.fromEntries(arr.map((r) => [r.id, { on: r[key], margin: r.defMargin }]));
  const [flips26, setFlips26] = useState(() => init(TARGETS_26, "defFlip"));
  const [holds26, setHolds26] = useState(() => init(DEFENDS_26, "defHold"));
  const [flips28, setFlips28] = useState(() => ({ ...init(TARGETS_28_STATIC, "defFlip"), OH28: { on: false, margin: 2 }, FL28: { on: false, margin: 1.5 } }));
  const [holds28, setHolds28] = useState(() => init(DEFENDS_28, "defHold"));
  const [house26, setHouse26] = useState(6);
  const [house28, setHouse28] = useState(0);
  const [demWH, setDemWH] = useState(true);
  const [fmode, setFmode] = useState("status");
  const [reconAssign, setReconAssign] = useState({ ctc: "A", tax: "A", care: "B", rev: "B" });
  const [holdouts, setHoldouts] = useState(1);
  const [seed, setSeed] = useState(20290120);
  const [tab, setTab] = useState("map");
  const [sens, setSens] = useState(null);

  const setRace = (setter) => (id, patch) => setter((s) => ({ ...s, [id]: { ...s[id], ...patch } }));
  const reconEligible = BILLS.filter((b) => b.recon !== "none");
  const cycleAssign = (id) => setReconAssign((s) => {
    const cur = s[id] || "none";
    const next = cur === "none" ? "A" : cur === "A" ? "B" : "none";
    return { ...s, [id]: next };
  });

  /* Senate composition */
  const comp = useMemo(() => {
    let d = 43; const roster = [];
    DEFENDS_26.forEach((r) => { if (holds26[r.id].on) { d++; roster.push({ archetype: r.archetype, margin: holds26[r.id].margin }); } });
    TARGETS_26.forEach((r) => { if (flips26[r.id].on) { d++; roster.push({ archetype: r.archetype, margin: flips26[r.id].margin, ind: !!r.independent }); } });
    const ohDem26 = flips26.OH.on, flDem26 = flips26.FL.on;
    let d29 = d;
    DEFENDS_28.forEach((r) => { if (!holds28[r.id].on) d29--; });
    TARGETS_28_STATIC.forEach((r) => { if (flips28[r.id].on) { d29++; roster.push({ archetype: r.archetype, margin: flips28[r.id].margin }); } });
    if (!ohDem26 && flips28.OH28.on) { d29++; roster.push({ archetype: "moderate", margin: flips28.OH28.margin }); }
    if (!flDem26 && flips28.FL28.on) { d29++; roster.push({ archetype: "moderate", margin: flips28.FL28.margin }); }
    roster.push({ archetype: "institutionalist", margin: 8 }, { archetype: "moderate", margin: 6 }, { archetype: "moderate", margin: 7 });
    const dSeats = d29, rSeats = 100 - dSeats;
    const margins = [
      ...TARGETS_26.filter((r) => flips26[r.id].on).map((r) => flips26[r.id].margin),
      ...TARGETS_28_STATIC.filter((r) => flips28[r.id].on).map((r) => flips28[r.id].margin),
    ];
    const mandate = margins.length ? margins.reduce((a, b) => a + b, 0) / margins.length : 0;
    const control = dSeats > 50 || (dSeats === 50 && demWH);
    return { dSeats, rSeats, roster, mandate, control, ohDem26, flDem26, flipCount: margins.length };
  }, [flips26, holds26, flips28, holds28, demWH]);

  const house = useMemo(() => {
    const dSeats = cl(215 + house26 + house28, 150, 300);
    return { dSeats, rSeats: 435 - dSeats, control: dSeats >= 218, cushion: dSeats - 218 };
  }, [house26, house28]);

  const trifecta = comp.control && house.control && demWH;

  const simParams = useMemo(() => ({
    dSeats: comp.dSeats, roster: comp.roster, houseD: house.dSeats, fmode, reconAssign, demWH, holdouts, seed,
  }), [comp, house, fmode, reconAssign, demWH, holdouts, seed]);

  const mc = useMemo(() => runSim({ ...simParams, N: 4000 }), [simParams]);

  const windowModel = useMemo(() => {
    if (!trifecta) return null;
    const sCush = comp.dSeats - 50, hCush = house.cushion;
    const reformOn = fmode !== "status";
    const slots100 = cl(Math.round(1 + sCush * 0.35 + hCush * 0.04 + (reformOn ? 1 : 0) + (comp.mandate > 4 ? 1 : 0)), 1, 6);
    const windowMonths = cl(Math.round(14 + sCush * 0.7 + hCush * 0.06 + (comp.mandate - 3) * 0.6), 12, 22);
    return { slots100, windowMonths, sCush, hCush };
  }, [trifecta, comp, house, fmode]);

  const sequenced = useMemo(() => {
    if (!windowModel) return [];
    return [...mc.bills].sort((a, b) => b.headline * b.salience - a.headline * a.salience).slice(0, windowModel.slots100).map((b) => b.id);
  }, [mc, windowModel]);

  /* Sensitivity sweep (on demand) */
  const runSensitivity = () => {
    const base = simParams;
    const baseE = expOnly({ ...base, N: 2000 });
    const moves = [];
    const addMember = (roster, arch, margin, ind) => [...roster, { archetype: arch, margin, ind: !!ind }];
    const rmOne = (roster, arch) => { const i = roster.findIndex((m) => m.archetype === arch); return i < 0 ? roster : [...roster.slice(0, i), ...roster.slice(i + 1)]; };
    // Senate target flips (off → on)
    [...TARGETS_26.map((r) => ({ ...r, st: flips26[r.id] })), ...TARGETS_28_STATIC.map((r) => ({ ...r, st: flips28[r.id] }))].forEach((r) => {
      if (r.st && !r.st.on) {
        const e = expOnly({ ...base, dSeats: base.dSeats + 1, roster: addMember(base.roster, r.archetype, r.st.margin, r.independent) });
        moves.push({ label: `Flip ${r.state}`, kind: "gain", delta: e - baseE });
      }
    });
    // Exposed defends (on → if lost)
    [...DEFENDS_26.map((r) => ({ ...r, st: holds26[r.id] })), ...DEFENDS_28.map((r) => ({ ...r, st: holds28[r.id] }))].forEach((r) => {
      if (r.st && r.st.on) {
        const e = expOnly({ ...base, dSeats: base.dSeats - 1, roster: rmOne(base.roster, r.archetype) });
        moves.push({ label: `Lose ${r.state}`, kind: "risk", delta: e - baseE });
      }
    });
    // House levers
    moves.push({ label: "+5 House seats", kind: "gain", delta: expOnly({ ...base, houseD: base.houseD + 5 }) - baseE });
    moves.push({ label: "−5 House seats", kind: "risk", delta: expOnly({ ...base, houseD: base.houseD - 5 }) - baseE });
    // Reform postures
    if (fmode !== "carveout") moves.push({ label: "Adopt democracy carve-out", kind: "gain", delta: expOnly({ ...base, fmode: "carveout" }) - baseE });
    if (fmode !== "majority") moves.push({ label: "Adopt full filibuster reform", kind: "gain", delta: expOnly({ ...base, fmode: "majority" }) - baseE });
    moves.sort((a, b) => Math.abs(b.delta) - Math.abs(a.delta));
    setSens({ baseE, moves: moves.slice(0, 9) });
  };

  /* Presets */
  const applyPreset = (name) => {
    const setAll = (t26, h26, t28, h28, hN26, hN28, wh, fm, assign, hold) => {
      setFlips26((s) => Object.fromEntries(Object.entries(s).map(([k, v]) => [k, { ...v, on: t26.includes(k) }])));
      setHolds26((s) => Object.fromEntries(Object.entries(s).map(([k, v]) => [k, { ...v, on: h26.includes(k) }])));
      setFlips28((s) => Object.fromEntries(Object.entries(s).map(([k, v]) => [k, { ...v, on: t28.includes(k) }])));
      setHolds28((s) => Object.fromEntries(Object.entries(s).map(([k, v]) => [k, { ...v, on: h28.includes(k) }])));
      setHouse26(hN26); setHouse28(hN28); setDemWH(wh); setFmode(fm); setReconAssign(assign); setHoldouts(hold); setSens(null);
    };
    const D26 = ["GA", "MI", "MN", "NH"], D28 = ["GA28", "AZ28", "NV28", "NH28", "PA28", "CO28"];
    const A2 = { ctc: "A", tax: "A", care: "B", rev: "B" };
    if (name === "status") setAll([], D26, [], D28, 0, 0, false, "status", A2, 1);
    if (name === "split") setAll(["ME", "NC", "OH", "IA"], D26, ["WI28", "NC28"], D28, -3, 0, true, "status", A2, 1);
    if (name === "narrow") setAll(["ME", "NC", "OH"], D26, ["WI28"], D28, 4, 0, true, "status", A2, 1);
    if (name === "governing") setAll(["ME", "NC", "OH", "IA", "AK"], D26, ["WI28", "NC28"], D28, 10, 5, true, "carveout", A2, 1);
    if (name === "wave") setAll(["ME", "NC", "OH", "IA", "TX", "AK", "NE"], D26, ["WI28", "NC28", "IA28"], D28, 18, 12, true, "majority", A2, 0);
  };

  /* UI primitives */
  const Panel = ({ title, eyebrow, children, right }) => (
    <section className="rounded-lg p-5 mb-6" style={{ background: C.panel, border: `1px solid ${C.panelEdge}` }}>
      <div className="flex items-baseline justify-between mb-1 gap-3">
        <div>{eyebrow && <div className="text-xs tracking-widest uppercase" style={{ color: C.brass, fontFamily: mono }}>{eyebrow}</div>}
          <h2 className="text-xl" style={{ fontFamily: serif, color: C.parchment }}>{title}</h2></div>
        {right}
      </div>{children}
    </section>
  );
  const Toggle = ({ on, set }) => (
    <button onClick={() => set(!on)} className="relative rounded-full text-xs font-bold transition-colors"
      style={{ width: 76, height: 28, fontFamily: mono, background: on ? C.dem : C.gop, color: C.parchment, border: `1px solid ${C.panelEdge}` }} aria-pressed={on}>
      <span className="absolute top-0.5 transition-all rounded-full flex items-center justify-center" style={{ left: on ? 46 : 3, width: 24, height: 22, background: C.bg, color: on ? C.demBright : C.gopBright }}>{on ? "D" : "R"}</span>
      <span className="absolute top-1" style={{ left: on ? 10 : 34, fontSize: 10, opacity: 0.9 }}>{on ? "DEM" : "GOP"}</span>
    </button>
  );
  const Bar = ({ p, color }) => (<div className="h-2 rounded-full w-full" style={{ background: C.panelEdge }}><div className="h-2 rounded-full transition-all" style={{ width: `${p * 100}%`, background: color }} /></div>);
  const grade = (p) => p >= 0.85 ? ["A", C.green] : p >= 0.65 ? ["B", C.green] : p >= 0.45 ? ["C", C.amber] : p >= 0.25 ? ["D", C.amber] : ["F", C.red];

  const RaceCard = ({ r, st, onSet, flipMode }) => {
    const on = st.on; const winLabel = flipMode ? (on ? "flips D" : "holds R") : (on ? "holds D" : "flips R");
    return (
      <div className="rounded-md p-3" style={{ background: C.bg, border: `1px solid ${on ? C.dem : C.panelEdge}` }}>
        <div className="flex items-start justify-between gap-2">
          <div>
            <div className="flex items-center gap-2 flex-wrap">
              <span style={{ fontFamily: serif, color: C.parchment, fontSize: 16 }}>{r.state}</span>
              <span className="text-[10px] px-1.5 py-0.5 rounded" style={{ fontFamily: mono, background: C.panelEdge, color: C.parchDim }}>{r.rating}</span>
              {r.special && <span className="text-[10px] px-1.5 py-0.5 rounded" style={{ fontFamily: mono, background: C.panelEdge, color: C.amber }}>SPECIAL</span>}
            </div>
            <div className="text-xs mt-1" style={{ color: C.parchDim, fontFamily: mono }}>
              <span style={{ color: r.independent ? C.ind : C.demBright }}>{r.dem || "Dem nominee"}</span>{" vs "}<span style={{ color: C.gopBright }}>{r.gop}</span>
            </div>
            {r.note && <div className="text-[11px] mt-1 leading-snug" style={{ color: C.parchDim }}>{r.note}</div>}
          </div>
          <div className="flex flex-col items-end gap-1 shrink-0">
            <Toggle on={on} set={(v) => onSet(r.id, { on: v })} />
            <span className="text-[10px]" style={{ fontFamily: mono, color: on ? C.demBright : C.gopBright }}>{winLabel}</span>
          </div>
        </div>
        <div className="flex items-center gap-2 mt-2">
          <span className="text-[10px] w-24" style={{ fontFamily: mono, color: C.parchDim }}>win margin</span>
          <input type="range" min={0.5} max={12} step={0.5} value={st.margin} onChange={(e) => onSet(r.id, { margin: parseFloat(e.target.value) })} className="flex-1" style={{ accentColor: on ? C.dem : C.gop }} />
          <span className="text-xs w-12 text-right" style={{ fontFamily: mono, color: C.parchment }}>+{st.margin.toFixed(1)}</span>
        </div>
      </div>
    );
  };

  const Hemicycle = ({ d, total = 100, label }) => {
    const rows = total > 200 ? [40, 52, 64, 76, 88, 100] : [12, 16, 20, 24, 28];
    const seats = [];
    rows.forEach((n, ri) => { const rad = 64 + ri * (total > 200 ? 20 : 26); for (let i = 0; i < n; i++) { const a = Math.PI - (Math.PI * i) / (n - 1); seats.push({ x: 200 + rad * Math.cos(a), y: 180 - rad * Math.sin(a), angle: a }); } });
    seats.sort((s1, s2) => s2.angle - s1.angle);
    const ratio = total / seats.length; const dDraw = Math.round(d / ratio);
    return (
      <svg viewBox="0 0 400 195" className="w-full" role="img" aria-label={label}>
        {seats.map((s, i) => <circle key={i} cx={s.x} cy={s.y} r={total > 200 ? 4 : 8} fill={i < dDraw ? C.dem : C.gop} opacity={0.85} />)}
        <line x1="200" y1="56" x2="200" y2="184" stroke={C.parchDim} strokeDasharray="3 4" strokeWidth="1" />
        <text x="200" y="48" textAnchor="middle" fill={C.parchDim} fontSize="9" fontFamily={mono}>{total > 200 ? "218 — control" : "50 — control"}</text>
        {total <= 200 && (() => { const s60 = seats[59]; return (<><line x1={s60.x} y1={s60.y - 14} x2={s60.x} y2={s60.y + 14} stroke={C.brass} strokeWidth="1.5" /><text x={s60.x} y={s60.y - 18} textAnchor="middle" fill={C.brass} fontSize="9" fontFamily={mono}>60 — cloture</text></>); })()}
      </svg>
    );
  };

  const tabs = [["map", "I · The Map"], ["window", "II · The Window"], ["agenda", "III · The Agenda"]];
  const pkgOf = (id) => reconAssign[id] && reconAssign[id] !== "none" ? reconAssign[id] : null;

  return (
    <div className="min-h-screen pb-16" style={{ background: C.bg, color: C.parchment }}>
      <header className="px-6 pt-8 pb-4 max-w-5xl mx-auto">
        <div className="text-xs tracking-[0.3em] uppercase" style={{ fontFamily: mono, color: C.brass }}>A 2029 Trifecta War Game · field data as of June 10, 2026</div>
        <h1 className="text-4xl mt-1" style={{ fontFamily: serif, fontWeight: 600 }}>Floor Time</h1>
        <p className="text-sm mt-2 max-w-2xl leading-relaxed" style={{ color: C.parchDim }}>
          Build a Congress from the 2026 and 2028 maps — both chambers — then stress-test the first legislative
          window of a January 2029 Democratic trifecta against historical first-100-days precedents and a
          two-chamber Monte Carlo enactment model. These eighteen bills are the legislative core of the wider
          Ossoff–Moore governing agenda; the program's executive actions, foreign-policy reconstruction, and
          constitutional-amendment work sit outside a passage model by nature and live in the unified-agenda companion.
        </p>
        <div className="flex flex-wrap gap-2 mt-4">
          {[["status", "Status quo"], ["split", "Senate flips, House doesn't"], ["narrow", "Narrow trifecta"], ["governing", "Governing majority"], ["wave", "Blue wave"]].map(([id, label]) => (
            <button key={id} onClick={() => applyPreset(id)} className="text-xs px-3 py-1.5 rounded transition-colors" style={{ fontFamily: mono, background: C.panel, color: C.parchDim, border: `1px solid ${C.panelEdge}` }}>{label}</button>
          ))}
        </div>
      </header>

      <div className="sticky top-0 z-10 px-6 py-3" style={{ background: `${C.bg}F0`, borderBottom: `1px solid ${C.panelEdge}`, backdropFilter: "blur(6px)" }}>
        <div className="max-w-5xl mx-auto flex flex-wrap items-center gap-x-5 gap-y-2">
          <div style={{ fontFamily: mono }} className="text-sm"><span style={{ color: C.parchDim }}>SEN </span><span style={{ color: C.demBright, fontWeight: 700 }}>{comp.dSeats}D</span><span style={{ color: C.parchDim }}>·</span><span style={{ color: C.gopBright, fontWeight: 700 }}>{comp.rSeats}R</span>{comp.dSeats === 50 && demWH && <span className="text-[10px] ml-1" style={{ color: C.brass }}>+VP</span>}</div>
          <div style={{ fontFamily: mono }} className="text-sm"><span style={{ color: C.parchDim }}>HOUSE </span><span style={{ color: C.demBright, fontWeight: 700 }}>{house.dSeats}D</span><span style={{ color: C.parchDim }}>·</span><span style={{ color: C.gopBright, fontWeight: 700 }}>{house.rSeats}R</span></div>
          <div className="text-xs px-2 py-1 rounded" style={{ fontFamily: mono, background: trifecta ? "#15301F" : "#33181A", color: trifecta ? C.green : C.red, border: `1px solid ${trifecta ? C.green : C.red}` }}>{trifecta ? "TRIFECTA" : comp.control && house.control ? "CONGRESS, NO WH" : comp.control || house.control ? "ONE CHAMBER" : "NO MAJORITY"}</div>
          {trifecta && <div className="text-xs px-2 py-1 rounded" style={{ fontFamily: mono, background: C.panelEdge, color: C.brass }}>E[enacted] {mc.expectedEnacted.toFixed(1)}/{BILLS.length}</div>}
          <label className="flex items-center gap-2 text-xs cursor-pointer" style={{ fontFamily: mono, color: C.parchDim }}><input type="checkbox" checked={demWH} onChange={(e) => setDemWH(e.target.checked)} style={{ accentColor: C.brass }} /> Dem WH 2029</label>
          <div className="flex gap-1 ml-auto">{tabs.map(([id, label]) => (<button key={id} onClick={() => setTab(id)} className="text-xs px-3 py-1.5 rounded transition-colors" style={{ fontFamily: mono, background: tab === id ? C.panelEdge : "transparent", color: tab === id ? C.parchment : C.parchDim, border: `1px solid ${tab === id ? C.brass : C.panelEdge}` }}>{label}</button>))}</div>
        </div>
      </div>

      <main className="max-w-5xl mx-auto px-6 pt-6">
        <Panel title="The Chambers" eyebrow="Composition · 119th Congress, Jan 2029">
          <div className="grid md:grid-cols-2 gap-4">
            <div className="rounded-md p-2" style={{ background: C.bg, border: `1px solid ${C.panelEdge}` }}>
              <div className="text-xs mb-1" style={{ fontFamily: mono, color: C.parchDim }}>SENATE · net {comp.dSeats - 47 >= 0 ? "+" : ""}{comp.dSeats - 47} D from 47</div>
              <Hemicycle d={comp.dSeats} total={100} label={`Senate: ${comp.dSeats} D`} />
            </div>
            <div className="rounded-md p-2" style={{ background: C.bg, border: `1px solid ${C.panelEdge}` }}>
              <div className="text-xs mb-1" style={{ fontFamily: mono, color: C.parchDim }}>HOUSE · net {house.dSeats - 215 >= 0 ? "+" : ""}{house.dSeats - 215} D from 215</div>
              <Hemicycle d={house.dSeats} total={435} label={`House: ${house.dSeats} D`} />
            </div>
          </div>
        </Panel>

        {tab === "map" && (
          <>
            <Panel title="House — net seat change" eyebrow="Both cycles · 218 for a majority">
              <div className="space-y-5">
                {[["2026 midterm", house26, setHouse26, -15, 40], ["2028 presidential", house28, setHouse28, -25, 30]].map(([label, val, setter, lo, hi]) => (
                  <div key={label}>
                    <div className="flex justify-between text-xs mb-1" style={{ fontFamily: mono }}><span style={{ color: C.parchDim }}>{label} — Dem net seats</span><span style={{ color: val >= 0 ? C.demBright : C.gopBright }}>{val >= 0 ? "+" : ""}{val}</span></div>
                    <input type="range" min={lo} max={hi} step={1} value={val} onChange={(e) => setter(parseInt(e.target.value))} className="w-full" style={{ accentColor: C.dem }} />
                  </div>
                ))}
                <div className="text-[11px] leading-snug" style={{ color: C.parchDim }}>
                  Resulting House: <span style={{ color: C.parchment, fontFamily: mono }}>{house.dSeats} D</span> —{" "}
                  {house.control ? <span style={{ color: C.green }}>majority, cushion of {house.cushion} {house.cushion === 1 ? "seat" : "seats"} above 218</span> : <span style={{ color: C.red }}>short of 218 — partisan bills die in the lower chamber</span>}. The cushion absorbs frontline defections on sweeping bills (Tab III).
                </div>
                <div className="rounded-md p-3" style={{ background: C.bg, border: `1px solid ${C.panelEdge}` }}>
                  <div className="text-[10px] uppercase tracking-wider mb-2" style={{ fontFamily: mono, color: C.brass }}>Representative 2026 battleground districts</div>
                  <div className="flex flex-wrap gap-1.5">{HOUSE_BELLWETHERS_26.map((d) => <span key={d} className="text-[10px] px-1.5 py-0.5 rounded" style={{ fontFamily: mono, background: C.panelEdge, color: C.parchDim }}>{d}</span>)}</div>
                  <div className="text-[10px] mt-2" style={{ color: C.parchDim }}>Illustrative anchors. 2025–26 redistricting (TX, OH, CA, MO and others) is still reshaping the battlefield — the sliders are the real control.</div>
                </div>
              </div>
            </Panel>
            <Panel title="2026 Senate — Republican-held targets" eyebrow="Midterm · Nov 3 2026"><div className="grid md:grid-cols-2 gap-3">{TARGETS_26.map((r) => <RaceCard key={r.id} r={r} st={flips26[r.id]} onSet={setRace(setFlips26)} flipMode />)}</div></Panel>
            <Panel title="2026 Senate — Democratic defends" eyebrow="Four open or exposed seats"><div className="grid md:grid-cols-2 gap-3">{DEFENDS_26.map((r) => <RaceCard key={r.id} r={r} st={holds26[r.id]} onSet={setRace(setHolds26)} />)}</div></Panel>
            <Panel title="2028 Senate — Class 3 targets" eyebrow="Presidential cycle">
              <div className="grid md:grid-cols-2 gap-3">
                {TARGETS_28_STATIC.map((r) => <RaceCard key={r.id} r={{ ...r, dem: "Dem nominee" }} st={flips28[r.id]} onSet={setRace(setFlips28)} flipMode />)}
                {!comp.ohDem26 && <RaceCard r={{ id: "OH28", state: "Ohio (again)", dem: "Dem nominee", gop: "2026 special winner (R)", rating: "Toss-up", note: "Husted held the 2026 special here, so the seat is up again." }} st={flips28.OH28} onSet={setRace(setFlips28)} flipMode />}
                {!comp.flDem26 && <RaceCard r={{ id: "FL28", state: "Florida (again)", dem: "Dem nominee", gop: "2026 special winner (R)", rating: "Likely R", note: "Moody held the 2026 special here, so the seat is up again." }} st={flips28.FL28} onSet={setRace(setFlips28)} flipMode />}
              </div>
            </Panel>
            <Panel title="2028 Senate — Democratic defends" eyebrow="The Warnock–Kelly–Cortez Masto class"><div className="grid md:grid-cols-2 gap-3">{DEFENDS_28.map((r) => <RaceCard key={r.id} r={{ ...r, gop: "GOP nominee" }} st={holds28[r.id]} onSet={setRace(setHolds28)} />)}</div></Panel>
          </>
        )}

        {tab === "window" && (
          <>
            <Panel title="The First Hundred Days" eyebrow="II · Precedent">
              <div className="overflow-x-auto"><table className="w-full text-sm" style={{ fontFamily: mono }}>
                <thead><tr className="text-left text-[11px] uppercase tracking-wider" style={{ color: C.brass }}><th className="py-2 pr-3">Year</th><th className="pr-3">President</th><th className="pr-3">Senate</th><th className="pr-3">House</th><th className="pr-3">Major laws ≤100d</th><th>Pattern</th></tr></thead>
                <tbody>{PRECEDENTS.map((p) => (<tr key={p.yr} style={{ borderTop: `1px solid ${C.panelEdge}` }}><td className="py-2 pr-3" style={{ color: C.parchment }}>{p.yr}</td><td className="pr-3" style={{ color: C.parchDim }}>{p.pres}</td><td className="pr-3" style={{ color: C.parchDim }}>{p.sen}</td><td className="pr-3" style={{ color: C.parchDim }}>{p.hou}</td><td className="pr-3"><div className="flex items-center gap-2"><span style={{ color: C.parchment }}>{p.majors100}</span><div className="flex gap-0.5">{Array.from({ length: p.majors100 }).map((_, i) => <span key={i} className="inline-block w-2 h-3 rounded-sm" style={{ background: C.brass }} />)}</div></div></td><td className="text-[11px] leading-snug" style={{ color: C.parchDim }}>{p.note}</td></tr>))}</tbody>
              </table></div>
            </Panel>
            <Panel title="Your Window" eyebrow="II · Projection">
              {!trifecta ? (
                <div className="text-sm py-6 text-center" style={{ color: C.parchDim }}>No trifecta under this map. A legislative window needs all three: Senate majority, House majority, and the White House. {!house.control && "The House is short of 218 — fix that on Tab I. "}{!comp.control && "The Senate is short of a majority. "}{!demWH && "The White House box is unchecked. "}</div>
              ) : (
                <>
                  <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    {[["Senate cushion", `${windowModel.sCush > 0 ? "+" : ""}${windowModel.sCush}`, "votes past 50 — floor defections you can survive"], ["House cushion", `${windowModel.hCush > 0 ? "+" : ""}${windowModel.hCush}`, "seats past 218 — frontline defections you can absorb"], ["Major-bill slots, days 1–100", windowModel.slots100, "floor-time capacity given both cushions, mandate, rules"], ["Effective window", `~${windowModel.windowMonths} mo`, "before midterm gravity closes it (Obama ~18; Biden ~14)"]].map(([k, v, d]) => (<div key={k} className="rounded-md p-4" style={{ background: C.bg, border: `1px solid ${C.panelEdge}` }}><div className="text-3xl" style={{ fontFamily: serif, color: C.brass }}>{v}</div><div className="text-xs mt-1" style={{ fontFamily: mono, color: C.parchment }}>{k}</div><div className="text-[11px] mt-1 leading-snug" style={{ color: C.parchDim }}>{d}</div></div>))}
                  </div>
                  <p className="text-[12px] mt-4 leading-relaxed" style={{ color: C.parchDim }}>Mandate proxy (avg. flip margin): <span style={{ color: C.parchment, fontFamily: mono }}>+{comp.mandate.toFixed(1)} pts</span> across <span style={{ color: C.parchment, fontFamily: mono }}>{comp.flipCount}</span> Senate flips. Productivity is front-loaded, reconciliation is the spine of anything fiscal, and non-budget priorities that miss the first year rarely recover. FDR's 15 laws were a crisis artifact on a 313-seat House; the modern ceiling under regular order is Obama's three.</p>
                </>
              )}
            </Panel>
          </>
        )}

        {tab === "agenda" && (
          <>
            <Panel title="Rules of the Chamber" eyebrow="III · Cloture posture" right={<button onClick={() => setSeed((s) => s + 1)} className="text-xs px-3 py-1.5 rounded" style={{ fontFamily: mono, border: `1px solid ${C.brass}`, color: C.brass, background: "transparent" }}>Re-roll ↻</button>}>
              <div className="flex flex-wrap gap-2">
                {[["status", "60-vote status quo", "Cloture at 60 for everything outside reconciliation."], ["carveout", "Democracy carve-out", "Majority cloture for voting-rights & statehood only; 60 elsewhere."], ["majority", "Full talking-filibuster reform", "Majority cloture chamber-wide. Subsumes the carve-out by definition."]].map(([id, label, d]) => (
                  <button key={id} onClick={() => setFmode(id)} className="text-left rounded-md p-3 flex-1 min-w-[200px] transition-colors" style={{ background: fmode === id ? C.panelEdge : C.bg, border: `1px solid ${fmode === id ? C.brass : C.panelEdge}` }}><div className="text-sm" style={{ fontFamily: serif, color: fmode === id ? C.brass : C.parchment }}>{label}</div><div className="text-[11px] mt-1" style={{ color: C.parchDim }}>{d}</div></button>
                ))}
              </div>
              <div className="text-[10px] mt-2 leading-snug" style={{ fontFamily: mono, color: C.parchDim }}>Unified-agenda pathway: democracy carve-out on Day 3 → talking-filibuster restoration in Month 3 → full elimination by Month 14 after a documented pattern of obstruction. The three postures above are the endpoints of that sequence.</div>
              {fmode !== "status" && (() => {
                const feas = fmode === "majority" ? mc.reformFull : mc.reformCarveout;
                const lab = fmode === "majority" ? "full talking-filibuster reform" : "the democracy carve-out";
                const fc = (p) => p > 0.70 ? C.green : p > 0.45 ? C.amber : C.red;
                return (<div className="mt-3 text-xs rounded-md p-3" style={{ fontFamily: mono, background: C.bg, border: `1px solid ${C.panelEdge}`, color: C.parchDim }}>
                  Probability your caucus produces 50 votes for <span style={{ color: C.parchment }}>{lab}</span>: <span style={{ color: fc(feas), fontWeight: 700 }}>{pct(feas)}</span>.
                  {fmode === "majority" ? <span> Adopting full reform necessarily carries the carve-out (<span style={{ color: fc(mc.reformCarveout), fontWeight: 700 }}>{pct(mc.reformCarveout)}</span>), so voting-rights and statehood are scored against that easier bar — never <em>harder</em> under full reform.</span> : <span> Full reform with this caucus would run <span style={{ color: fc(mc.reformFull), fontWeight: 700 }}>{pct(mc.reformFull)}</span>.</span>}
                </div>);
              })()}
              <div className="mt-3 rounded-md p-3" style={{ background: C.bg, border: `1px solid ${C.panelEdge}` }}>
                <div className="flex justify-between text-xs mb-1" style={{ fontFamily: mono }}><span style={{ color: C.parchDim }}>Immovable reform holdouts (hard No on any rules change)</span><span style={{ color: holdouts > 0 ? C.amber : C.green }}>{holdouts}</span></div>
                <input type="range" min={0} max={3} step={1} value={holdouts} onChange={(e) => setHoldouts(parseInt(e.target.value))} className="w-full" style={{ accentColor: C.amber }} />
                <div className="text-[10px] mt-1 leading-snug" style={{ color: C.parchDim }}>Represents genuinely immovable senators — the Manchin/Sinema problem — layered on top of ordinary caucus discipline, which is now modeled as high on procedural votes. A large majority absorbs a couple of holdouts comfortably; a bare 50–51 majority cannot survive any.</div>
              </div>
            </Panel>

            <Panel title="Reconciliation packages" eyebrow="III · Two budget vehicles, 2029">
              <div className="text-[12px] mb-3 leading-snug" style={{ color: C.parchDim }}>
                Calendar 2029 offers two reconciliation vehicles (FY-29, FY-30). Each is a <em>single bill that bundles many fiscal provisions</em> and rides past the filibuster on a simple majority — but a member is a No on the whole package if they object to <em>any</em> bundled piece, so every addition makes the package more fragile. That's the go-big-vs-go-lean tension that defined BBB (one mega-package, collapsed) versus the IRA (leaner, survived). Click a bill to move it between Package A, Package B, and unbundled. Only fiscal bills are eligible; voting rights, the PRO Act, immigration, background checks, and D.C. statehood are Byrd-ineligible and must go through regular order.
              </div>
              <div className="flex flex-wrap gap-2 mb-3">
                {reconEligible.map((b) => {
                  const p = pkgOf(b.id);
                  const col = p ? PKG_COLOR[p] : C.parchDim;
                  return (<button key={b.id} onClick={() => cycleAssign(b.id)} className="text-xs px-3 py-2 rounded text-left transition-colors" style={{ fontFamily: mono, background: p ? C.bg : C.bg, color: col, border: `1px solid ${p ? col : C.panelEdge}` }}>
                    <div>{p ? `◆ Package ${p}` : "○ unbundled"}</div>
                    <div className="text-[10px] opacity-80" style={{ color: C.parchment }}>{b.name}</div>
                    <div className="text-[10px] opacity-60">{b.recon === "full" ? "fully fiscal" : "fiscal core only"}</div>
                  </button>);
                })}
              </div>
              <div className="grid sm:grid-cols-2 gap-3">
                {mc.packages.map((P) => (
                  <div key={P.id} className="rounded-md p-3" style={{ background: C.bg, border: `1px solid ${P.bills.length ? PKG_COLOR[P.id] : C.panelEdge}` }}>
                    <div className="flex justify-between items-baseline">
                      <div style={{ fontFamily: serif, color: PKG_COLOR[P.id] }}>Package {P.id}{P.id === "A" ? " · FY-29" : " · FY-30"}</div>
                      <div className="text-[10px]" style={{ fontFamily: mono, color: C.parchDim }}>{P.bills.length} {P.bills.length === 1 ? "provision" : "provisions"}</div>
                    </div>
                    {P.bills.length === 0 ? <div className="text-[11px] mt-2" style={{ color: C.parchDim }}>empty</div> : (
                      <>
                        <div className="text-[11px] mt-1 leading-snug" style={{ color: C.parchDim }}>{P.bills.map((id) => BILL_BY_ID[id].name).join(" + ")}</div>
                        <div className="mt-2 text-[11px]" style={{ fontFamily: mono }}>
                          <div className="flex justify-between mb-1"><span style={{ color: C.parchDim }}>package enacts (both chambers)</span><span style={{ color: grade(P.en)[1] }}>{pct(P.en)}</span></div>
                          <Bar p={P.en} color={grade(P.en)[1]} />
                          <div className="text-[10px] mt-1" style={{ color: C.parchDim }}>Senate {pct(P.sen)} · House {pct(P.house)}{P.bills.length >= 3 && <span style={{ color: C.amber }}> · bundling {P.bills.length} pieces is straining the coalition</span>}</div>
                        </div>
                      </>
                    )}
                  </div>
                ))}
              </div>
            </Panel>

            <Panel title={`The Agenda — ${BILLS.length} Bills, 4,000 Trials Each`} eyebrow="III · Two-chamber Monte Carlo" right={trifecta && <div className="text-right"><div className="text-2xl" style={{ fontFamily: serif, color: C.brass }}>{mc.expectedEnacted.toFixed(1)}<span className="text-sm" style={{ color: C.parchDim }}>/{BILLS.length}</span></div><div className="text-[10px]" style={{ fontFamily: mono, color: C.parchDim }}>expected enactments</div></div>}>
              {!trifecta ? (
                <div className="text-sm py-6 text-center" style={{ color: C.parchDim }}>Enactment needs all three levers. {!house.control && "The House is short of 218 — even a filibuster-proof Senate can't enact a bill the House won't pass. "}{!comp.control && "The Senate lacks a majority. "}{!demWH && "No Democratic president to sign. "}Return to Tab I.</div>
              ) : (
                <div className="space-y-3">
                  {mc.bills.map((b) => {
                    const [g, gc] = grade(b.headline); const inWindow = sequenced.includes(b.id);
                    const senShown = b.pkg ? mc.packages.find((P) => P.id === b.pkg).sen : b.senFull;
                    return (
                      <div key={b.id} className="rounded-md p-4" style={{ background: C.bg, border: `1px solid ${inWindow ? C.brass : C.panelEdge}` }}>
                        <div className="flex flex-wrap items-baseline justify-between gap-2">
                          <div className="flex items-center gap-2"><span className="text-2xl w-8 text-center" style={{ fontFamily: serif, color: gc }}>{g}</span><div><div style={{ fontFamily: serif, color: C.parchment }}>{b.name}</div><div className="text-[11px]" style={{ color: C.parchDim }}>{b.desc}</div></div></div>
                          <div className="flex gap-1.5 items-center flex-wrap justify-end">
                            {inWindow && <span className="text-[10px] px-1.5 py-0.5 rounded" style={{ fontFamily: mono, background: "#2A2410", color: C.brass }}>100-DAY SLOT</span>}
                            {b.pkg ? <span className="text-[10px] px-1.5 py-0.5 rounded" style={{ fontFamily: mono, background: C.panelEdge, color: PKG_COLOR[b.pkg] }}>PACKAGE {b.pkg}</span> : <span className="text-[10px] px-1.5 py-0.5 rounded" style={{ fontFamily: mono, background: C.panelEdge, color: b.recon !== "none" ? C.amber : C.parchDim }}>{b.recon !== "none" ? "RECON-ELIGIBLE · UNBUNDLED" : "REGULAR ORDER"}</span>}
                            {((fmode === "carveout" && b.democracy) || fmode === "majority") && <span className="text-[10px] px-1.5 py-0.5 rounded" style={{ fontFamily: mono, background: C.panelEdge, color: C.brass }}>MAJ. CLOTURE</span>}
                            {b.democracy && <span className="text-[10px] px-1.5 py-0.5 rounded" style={{ fontFamily: mono, background: C.panelEdge, color: C.ind }}>DEMOCRACY</span>}
                          </div>
                        </div>
                        <div className="grid sm:grid-cols-3 gap-3 mt-3 text-[11px]" style={{ fontFamily: mono }}>
                          <div><div className="flex justify-between mb-1"><span style={{ color: C.parchDim }}>Senate {b.pkg ? `(pkg ${b.pkg})` : "(cloture)"}</span><span style={{ color: C.parchment }}>{pct(senShown)}</span></div><Bar p={senShown} color={C.brass} /></div>
                          <div><div className="flex justify-between mb-1"><span style={{ color: C.parchDim }}>House (majority)</span><span style={{ color: C.parchment }}>{pct(b.house)}</span></div><Bar p={b.house} color={C.dem} /></div>
                          <div><div className="flex justify-between mb-1"><span style={{ color: C.parchDim }}>Enacted (both)</span><span style={{ color: C.parchment }}>{pct(b.headline)}</span></div><Bar p={b.headline} color={gc} /></div>
                        </div>
                        <div className="flex flex-wrap gap-x-4 gap-y-1 text-[10px] mt-2" style={{ fontFamily: mono, color: C.parchDim }}>
                          {b.recon === "partial" && b.pkg && <span>fiscal core rides Package {b.pkg}; the full regulatory bill would need regular order ({pct(b.enFull)})</span>}
                          {b.recon !== "none" && !b.pkg && <span style={{ color: C.amber }}>no vehicle assigned — needs 60 votes / reform like any policy bill</span>}
                          {b.houseSweep >= 0.4 && <span style={{ color: house.cushion < 8 ? C.amber : C.parchDim }}>high House-sweep ({b.houseSweep.toFixed(2)}) — sensitive to your cushion of {house.cushion}</span>}
                          {b.gopPool > 0 && !b.pkg && <span>GOP pool: {b.gopPool} @ {pct(b.gopProb)}{flips26.ME.on && b.gopPool > 0 && b.id !== "dc" ? "" : ""}</span>}
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </Panel>

            {trifecta && (
              <Panel title="Leverage board" eyebrow="III · Sensitivity analysis" right={<button onClick={runSensitivity} className="text-xs px-3 py-1.5 rounded" style={{ fontFamily: mono, border: `1px solid ${C.brass}`, color: C.brass, background: "transparent" }}>{sens ? "Recompute" : "Find highest-leverage moves"}</button>}>
                {!sens ? (
                  <div className="text-sm py-4" style={{ color: C.parchDim }}>Run the sweep to rank every available move — each off target, each exposed defend, House swings, and reform postures — by its marginal effect on expected enactments, holding everything else fixed.</div>
                ) : (
                  <div>
                    <div className="text-[11px] mb-3" style={{ fontFamily: mono, color: C.parchDim }}>Baseline: <span style={{ color: C.parchment }}>{sens.baseE.toFixed(2)}</span> expected enactments. Each bar is the change from this baseline if you made that one move.</div>
                    <div className="space-y-2">
                      {sens.moves.map((m, i) => {
                        const mag = Math.abs(m.delta); const w = cl(mag / 2.5, 0.02, 1); const pos = m.delta >= 0;
                        const col = pos ? C.green : C.red;
                        return (<div key={i} className="flex items-center gap-3">
                          <span className="text-[11px] w-48 shrink-0" style={{ fontFamily: mono, color: C.parchment }}>{m.label}</span>
                          <div className="flex-1 h-4 rounded relative" style={{ background: C.bg, border: `1px solid ${C.panelEdge}` }}><div className="h-4 rounded" style={{ width: `${w * 100}%`, background: col, opacity: 0.7 }} /></div>
                          <span className="text-[11px] w-16 text-right" style={{ fontFamily: mono, color: col }}>{pos ? "+" : ""}{m.delta.toFixed(2)}</span>
                        </div>);
                      })}
                    </div>
                    <div className="text-[10px] mt-3" style={{ color: C.parchDim }}>Computed at 1,200 trials/scenario, so small differences (±0.1) are noise. Green = gain from a flip/reform; red = loss if an exposed seat falls.</div>
                  </div>
                )}
              </Panel>
            )}

            <Panel title="Reading the Board" eyebrow="III · Notes from the cloakroom">
              <ul className="text-[12px] space-y-2 leading-relaxed" style={{ color: C.parchDim }}>
                <li>• <span style={{ color: C.parchment }}>Enactment is a two-chamber AND-gate.</span> A bill needs the Senate (cloture or a package) and the House (simple majority) on the same trial. A filibuster-proof Senate buys nothing if the House is at 217.</li>
                <li>• <span style={{ color: C.parchment }}>Reconciliation now bundles.</span> Each vehicle is one bill carrying many provisions; a member who objects to any piece is a No on the whole thing, so a fat package is fragile. Split across A and B to lower per-package risk, or go big and gamble — the BBB-vs-IRA choice.</li>
                <li>• <span style={{ color: C.parchment }}>Privilege comes only from a vehicle.</span> A reconciliation-eligible bill left unbundled gets no filibuster bypass — it needs 60 votes like any policy bill.</li>
                <li>• <span style={{ color: C.parchment }}>Full reform never lowers a democracy bill.</span> Chamber-wide reform contains the carve-out, so John Lewis VRAA and D.C. statehood are scored against the easier carve-out bar in both reform modes.</li>
                <li>• <span style={{ color: C.parchment }}>D.C. statehood faces no constitutional supermajority.</span> Article IV §3 admits states by simple majority; the 60-vote wall is purely the Senate's cloture rule.</li>
                <li>• <span style={{ color: C.parchment }}>The democracy carve-out is narrow.</span> Only election mechanics qualify — voting rights, statehood, and campaign-finance disclosure. Government ethics, Supreme Court ethics, and antitrust are good-government reforms, not election law, so under a <em>pure</em> carve-out they still need 60 votes. Only full reform frees them.</li>
                <li>• <span style={{ color: C.parchment }}>Some things can't ride reconciliation at all.</span> The minimum wage is Byrd-barred (the parliamentarian struck it from the 2021 ARP), so it can't hide in a package no matter how you bundle — it lives or dies on the floor at whatever the cloture threshold is.</li>
                <li>• <span style={{ color: C.parchment }}>Social Security is its own wall.</span> Section 310(g) of the Budget Act bars any Social Security change from reconciliation outright — so the expansion, like the minimum wage, lives or dies on the floor at whatever the cloture threshold is.</li>
              </ul>
            </Panel>
          </>
        )}

        <footer className="text-[10px] mt-8 leading-relaxed" style={{ fontFamily: mono, color: C.parchDim }}>
          MODEL ASSUMPTIONS — Candidate fields current as of June 10, 2026; pending: GA GOP runoff (Jun 16), MI/MN primaries (Aug 4 & 11), AK & FL primaries (Aug 18), NH primary (Sep 8). House net-seat sliders are abstractions over 435 districts amid active 2025–26 redistricting; the listed battlegrounds are illustrative. Senate defection probabilities, House sweep/drag parameters, archetypes, crossover pools, reconciliation bundling fragility, reform holdouts, and the 100-day capacity formula are modeling judgments, not empirical estimates. A Democratic presidency in 2029 is an assumed input. 4,000 Monte Carlo trials per bill (1,200 in the sensitivity sweep), seeded for reproducibility — re-roll to resample. This is a war game, not a forecast.
        </footer>
      </main>
    </div>
  );
}
