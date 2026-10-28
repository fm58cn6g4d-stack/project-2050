import { useState, useCallback } from "react";

// ─── ERROR BOUNDARY handled via renderCrash state in main component ─────────

// Safe number helpers — never let NaN/Infinity reach .toFixed()
const safeNum = (v) => { const n = Number(v); return isFinite(n) ? n : 0; };
const safeFix = (v, d=1) => safeNum(v).toFixed(d);

// Sanitize bill text before sending to API:
// 1. Replace backticks (statutory quoting convention) with single quotes
// 2. Normalize Unicode dashes/quotes to ASCII equivalents
// 3. Truncate to 25000 chars to handle full-length bills
const sanitizeBill = (text) => text
  .replace(/`/g, "'")
  .replace(/‘|’/g, "'")   // curly single quotes
  .replace(/“|”/g, '"')   // curly double quotes
  .replace(/–|—/g, '-')   // en-dash, em-dash
  .replace(/ /g, ' ')          // non-breaking space
  .slice(0, 25000);

// ─── CBO FEBRUARY 2026 BASELINE (Table 1-1) ─────────────────────────────────
const BASELINE = {
  years: [2026,2027,2028,2029,2030,2031,2032,2033,2034,2035],
  gdp:   [31902,33315,34666,36010,37391,38813,40277,41796,43373,45012],
  revenues: [5596,5885,6071,6320,6595,6869,7130,7391,7669,7972],
  mandatory: [4529,4783,5005,5067,5375,5582,5835,6277,6437,6545],
  discretionary: [1880,1882,1929,1948,1989,2024,2063,2111,2147,2187],
  netInterest: [1039,1108,1218,1324,1432,1548,1670,1784,1904,2019],
  deficits: [-1853,-1887,-2080,-2020,-2201,-2286,-2439,-2781,-2819,-2779],
};

// Rules of Thumb (per 0.1 pp change, 2026-2035, from CBO workbook)
const ROT = {
  productivity: { deficit: [-8.53,-13.98,-19.52,-25.84,-32.50,-39.80,-47.81,-56.59,-66.30,-77.19] },
  laborForce:   { deficit: [-4.06,-6.57,-9.21,-12.02,-15.09,-18.55,-22.57,-27.09,-31.85,-37.45] },
  interestRate: { netInterest: [13.34,18.69,23.74,28.61,33.52,38.08,42.90,47.43,52.25,56.95],
                  revenue: [-2.57,-1.68,-0.88,-0.17,0.50,1.01,1.51,1.93,2.29,2.64] },
};

// Medicaid per-enrollee federal costs ($), base year 2026
const MEDICAID = {
  aca_adults:   { cost: 7500,  fmap: 0.90, growth: 0.045, label: "ACA Expansion Adults" },
  trad_adults:  { cost: 4650,  fmap: 0.675,growth: 0.063, label: "Traditional Adults" },
  children:     { cost: 1980,  fmap: 0.675,growth: 0.057, label: "Children" },
  disabled:     { cost: 19480, fmap: 0.675,growth: 0.049, label: "Blind/Disabled" },
  aged:         { cost: 15180, fmap: 0.675,growth: 0.040, label: "Aged" },
};

const DISC_SPENDOUT = [0.25,0.25,0.25,0.10,0.05,0.03,0.02,0.01,0.01,0.01];
const DEBT_SERVICE_RATE = 0.038; // ~3.8% on marginal new debt

// ─── SCORING ENGINE ──────────────────────────────────────────────────────────

function scoreProvision(prov, yearIndex) {
  try { return _scoreProvision(prov, yearIndex); }
  catch(e) { console.warn("scoreProvision error", e); return 0; }
}
function _scoreProvision(prov, yearIndex) {
  const { type, params = {} } = prov;
  const yr = yearIndex; // 0 = FY2026
  const gdpFactor = (1 + 0.033) ** yr; // ~3.3% nominal GDP growth

  switch (type) {
    case "medicaid_expansion": {
      const cat = MEDICAID[params.category] || MEDICAID["aca_adults"];
      const enrollment = safeNum(params.enrollmentMillion || 1) * 1e6;
      const enrollmentRamp = yr === 0 ? 0.5 : Math.min(1.0, 0.5 + yr * 0.2);
      const costThisYear = cat.cost * (1 + cat.growth) ** yr;
      return safeNum(enrollment * enrollmentRamp * costThisYear * cat.fmap / 1e9);
    }
    case "medicaid_restriction": {
      const cat = MEDICAID[params.category] || MEDICAID["aca_adults"];
      const enrollment = safeNum(params.enrollmentMillion || 1) * 1e6;
      const stateOffset = 0.50; // CBO: states replace ~50% of lost fed funds
      const netEnrollmentReduction = enrollment * (1 - stateOffset);
      const costThisYear = cat.cost * (1 + cat.growth) ** yr;
      return -netEnrollmentReduction * costThisYear * cat.fmap / 1e9;
    }
    case "medicare_change": {
      const perBeneficiary = 16300 * (1.05) ** yr;
      const benMillion = params.beneficiaryMillion || 0;
      const rateChangePct = params.paymentRateChange || 0;
      return (benMillion * 1e6 * perBeneficiary * 0.0 +
              BASELINE.mandatory[yr] * 0.28 * (rateChangePct / 100)) / 1e0; // rough
    }
    case "social_security": {
      const benefitChangePct = params.benefitRateChange || 0;
      const ssBase = yr === 0 ? 1250 : 1250 * (1.04) ** yr; // $1.25T → grows ~4%/yr
      return ssBase * (benefitChangePct / 100);
    }
    case "snap_change": {
      const enrollment = safeNum(params.enrollmentMillion || 1) * 1e6;
      const perPersonMonthly = 212 * (1.025) ** yr; // ~$212/mo, grows with inflation
      return enrollment * perPersonMonthly * 12 / 1e9 * (params.direction === "decrease" ? -1 : 1);
    }
    case "new_program_mandatory": {
      const yearOneCost = (params.annualCostBillion || 1) * gdpFactor;
      return yearOneCost;
    }
    case "discretionary_new": {
      const ba = params.budgetAuthorityBillion || 0;
      return ba * DISC_SPENDOUT[yr];
    }
    case "discretionary_change": {
      const change = params.annualChangeBillion || 0;
      return change * gdpFactor;
    }
    case "revenue_individual_tax": {
      const baseRevenue = BASELINE.revenues[yr] * 0.49; // ~49% from individual income taxes
      const rateChangePct = params.rateChangePct || 0;
      const eti = 0.25; // CBO ETI central estimate
      const behavioralOffset = 1 - eti; // behavioral reduction in tax base
      return baseRevenue * (rateChangePct / 100) * behavioralOffset * -1; // negative = revenue increase
    }
    case "revenue_corporate_tax": {
      const baseRevenue = BASELINE.revenues[yr] * 0.072; // ~7.2% corporate
      const rateChangePct = params.rateChangePct || 0;
      return baseRevenue * (rateChangePct / 100) * 0.80 * -1;
    }
    case "revenue_payroll_tax": {
      const baseRevenue = BASELINE.revenues[yr] * 0.326; // ~32.6% payroll
      const rateChangePct = params.rateChangePct || 0;
      return baseRevenue * (rateChangePct / 100) * -1;
    }
    case "revenue_new_fee": {
      const annualRevenue = (params.annualRevenueBillion || 0) * gdpFactor;
      return -annualRevenue; // negative = reduces deficit
    }
    case "irs_enforcement": {
      // CBO uses ~$0.30–0.40 revenue per $1 enforcement spending net
      const enforcementBA = params.budgetAuthorityBillion || 0;
      return -(enforcementBA * 0.35) + enforcementBA * DISC_SPENDOUT[yr]; // net: rev gain offset by cost
    }
    case "immigration_restriction": {
      // Fewer workers → less payroll + income taxes, slightly more SS/Medicare costs
      const laborForceReductionPct = params.laborForceReductionPct || 0.1;
      const baseRev = BASELINE.revenues[yr] * 0.40; // labor-sensitive revenues
      return baseRev * (laborForceReductionPct / 100) * 0.8; // deficit increases ~80% of rev loss
    }
    case "tariff_change": {
      const tradeBase = 418; // FY2026 customs duties baseline ~$418B
      const rateChangePct = params.rateChangePct || 0;
      const tradeElasticity = -0.75;
      const netEffect = -(tradeBase * (rateChangePct / 100) * (1 + tradeElasticity));
      return netEffect * (1.025) ** yr;
    }
    case "direct_spending": {
      const cost = (params.annualCostBillion || 0);
      return cost * gdpFactor;
    }
    default:
      return (params.annualCostBillion || params.annualEffectBillion || 0) * gdpFactor;
  }
}

function computeDebtServiceAdder(cumulativeDeficitChange) {
  // Each dollar of additional deficit adds ~3.8% annual interest cost
  return cumulativeDeficitChange * DEBT_SERVICE_RATE;
}

function runScoringEngine(provisions) {
  try { return _runScoringEngine(provisions); }
  catch(e) { console.error("scoring engine error", e);
    return { byYear: BASELINE.years.map(y=>({year:y,mandatoryChange:0,discretionaryChange:0,revenueChange:0,deficitChange:0,totalDeficitChange:0})),
      total1yr:0, total5yr:0, total10yr:0, uncertaintyMultiplier:0.3 }; }
}
function _runScoringEngine(provisions) {
  const results = {
    byYear: BASELINE.years.map((yr, i) => {
      let mandatoryChange = 0, discretionaryChange = 0, revenueChange = 0;
      const mandatoryTypes = new Set(["medicaid_expansion","medicaid_restriction","medicare_change",
        "social_security","snap_change","new_program_mandatory","direct_spending","immigration_restriction"]);
      const discTypes = new Set(["discretionary_new","discretionary_change","irs_enforcement"]);
      const revTypes = new Set(["revenue_individual_tax","revenue_corporate_tax","revenue_payroll_tax","revenue_new_fee"]);

      for (const prov of provisions) {
        const effect = scoreProvision(prov, i);
        if (mandatoryTypes.has(prov.type)) mandatoryChange += effect;
        else if (discTypes.has(prov.type)) discretionaryChange += effect;
        else if (revTypes.has(prov.type)) revenueChange += effect;
        else if (prov.type === "tariff_change") revenueChange += -Math.abs(effect) * (effect >= 0 ? 1 : -1);
        else mandatoryChange += effect; // default
      }

      const deficitChange = mandatoryChange + discretionaryChange + revenueChange;
      return { year: yr, mandatoryChange, discretionaryChange, revenueChange, deficitChange };
    }),
  };

  // Add debt service on cumulative deficit changes
  let cumulative = 0;
  results.byYear = results.byYear.map(row => {
    cumulative += row.deficitChange;
    const dsAdder = computeDebtServiceAdder(cumulative);
    return { ...row, debtService: dsAdder * 0.038, totalDeficitChange: row.deficitChange + dsAdder * 0.01 };
  });

  results.total1yr = results.byYear[0]?.totalDeficitChange || 0;
  results.total5yr = results.byYear.slice(0,5).reduce((s,r) => s + r.totalDeficitChange, 0);
  results.total10yr = results.byYear.reduce((s,r) => s + r.totalDeficitChange, 0);
  results.uncertaintyMultiplier = provisions.some(p => p.confidence === "low") ? 0.5 :
    provisions.some(p => p.confidence === "medium") ? 0.3 : 0.15;

  return results;
}

// ─── CLAUDE API CALL ─────────────────────────────────────────────────────────

// ─── PASS 1: Statutory language stripper ─────────────────────────────────────
// Short, fast prompt — reads raw bill text and returns plain-English provision summaries.
// No JSON, no scoring schema — just clean budget-relevant descriptions.
const EXTRACT_PROMPT = [
  "You are a federal budget analyst reading legislation to identify its fiscal provisions.",
  "",
  "Read the bill and list ONLY the provisions that have direct federal budget effects (spending, revenue, or borrowing). Ignore findings sections, definitions, reporting requirements with no dollar amounts, and purely technical amendments.",
  "",
  "For each fiscal provision write one line:",
  "PROVISION: [short title] | [plain English description of what it spends/cuts/raises and how much if specified] | [fiscal years affected if known]",
  "",
  "Example:",
  "PROVISION: DOE Water Power R&D Authorization | Reauthorizes DOE discretionary grants for hydropower and marine energy R&D at $300M/year | FY2026-2030",
  "PROVISION: User Fee | Creates new annual FDA user fee of $50K per critical drug | Ongoing",
  "",
  "List only provisions, nothing else. If the bill has no direct federal fiscal effects, write: NO FISCAL PROVISIONS."
].join("\n");

// ─── PASS 2: CBO scoring schema ──────────────────────────────────────────────
// Takes the clean provision list from Pass 1, applies full CBO methodology.
const SYSTEM_PROMPT = [
  "You are a CBO senior budget analyst scoring legislative provisions.",
  "CBO baseline: February 2026. Window: FY2026-FY2035.",
  "",
  "PROVISION TYPES (use exactly one per provision):",
  "medicaid_expansion | medicaid_restriction | medicare_change | social_security | snap_change | new_program_mandatory | discretionary_new | discretionary_change | revenue_individual_tax | revenue_corporate_tax | revenue_payroll_tax | revenue_new_fee | irs_enforcement | immigration_restriction | tariff_change | direct_spending",
  "",
  "CONFIDENCE: use only exactly: high, medium, or low. Never use medium-high or other variants.",
  "",
  "PARAMS RULES - CRITICAL:",
  "- params must contain ONLY numeric values. No strings, no prose, no explanations.",
  "- Use only these numeric keys as applicable:",
  "  annualCostBillion, budgetAuthorityBillion, annualChangeBillion, enrollmentMillion,",
  "  rateChangePct, annualRevenueBillion, laborForceReductionPct, paymentRateChange,",
  "  benefitRateChange, beneficiaryMillion",
  "- For medicaid also include: category (string: aca_adults|trad_adults|children|disabled|aged)",
  "- Multi-year totals: divide by years to get annual. e.g. $300B/10yr = annualCostBillion:30",
  "- If amount unknown: use a reasonable CBO-analogous estimate",
  "",
  "KEY PARAMETERS:",
  "- Medicaid ACA adults: $7,500/enrollee/yr (90% FMAP); trad adults: $4,650 (67.5%)",
  "- Medicare: $16,300/beneficiary/yr; SS outlays: $1.25T FY2026",
  "- Discretionary spendout Y1=25%, Y2=50%, Y3+=75%",
  "- ETI individual 0.25; corporate 0.20; IRS net return $0.35/$1",
  "",
  "OUTPUT RULES - CRITICAL:",
  "- Return a raw JSON object ONLY. Absolutely no markdown fences, no ```json, no ``` anywhere.",
  "- No text before or after the JSON. Start with { and end with }.",
  "- Keep description, cboAnalogy, scoringCaveat short (under 100 chars each).",
  '- Schema: {"billTitle":"","summary":"","scoringBaseline":"CBO February 2026","provisions":[{"id":"p1","title":"","type":"","direction":"","confidence":"","params":{},"description":"","cboAnalogy":"","scoringCaveat":""}],"macroFlags":{"gdpEffect":"","gdpMagnitude":"","laborForceEffect":"","notes":""},"conventionalScore":""}'
].join("\n");




// ─── FORMATTING HELPERS ───────────────────────────────────────────────────────

const fmt = (n) => {
  if (n === null || n === undefined) return "—";
  const abs = Math.abs(n);
  const str = abs >= 1000 ? `$${(abs/1000).toFixed(1)}T` : `$${abs.toFixed(1)}B`;
  return n < 0 ? `(${str})` : str;
};

const fmtSign = (n) => {
  if (n === null || n === undefined) return "—";
  const abs = Math.abs(n);
  const str = abs >= 1000 ? `${(abs/1000).toFixed(1)}T` : `${abs.toFixed(1)}B`;
  if (Math.abs(n) < 0.05) return "—";
  return n > 0 ? `+$${str}` : `-$${str}`;
};

const effectClass = (n) => Math.abs(n) < 0.05 ? "neutral" : n > 0 ? "cost" : "save";

// ─── SAMPLE BILLS ─────────────────────────────────────────────────────────────

const SAMPLES = [
  {
    label: "Pharma Supply Chain Resilience Act",
    text: `The Pharmaceutical Supply Chain Resilience Act requires:
1. The FDA to identify all manufacturers of critical drugs with facilities in climate-risk zones
2. Any drug with >50% production concentration at a single facility must establish redundant manufacturing capacity at a geographically separate site within 3 years
3. HHS establishes a Strategic Pharmaceutical Reserve with a minimum 6-month supply of 200 critical drugs
4. $2.5 billion in grants over 5 years for domestic manufacturing facility construction or expansion
5. A new FDA user fee of $50,000 per critical drug annually to fund the monitoring program
6. New mandatory reporting requirements; FDA enforcement staff expanded by 200 positions`
  },
  {
    label: "Coastal Resilience & Ocean Health Act",
    text: `The Coastal Resilience and Ocean Health Act of 2026 would:
1. Appropriate $1.8 billion over 5 years for NOAA coastal resilience grants to state and local governments
2. Create a new $400 million revolving loan fund within NOAA for fishery adaptation projects
3. Expand the Marine Protected Areas program to cover an additional 15% of U.S. EEZ, with a dedicated enforcement budget of $80 million annually
4. Provide $600 million for offshore wind infrastructure research grants through DOE
5. Establish a new entitlement: payments to commercial fishing operations displaced by offshore wind development, capped at $50 million per year
6. Increase NOAA's base discretionary authorization by $300 million per year`
  },
  {
    label: "Systems Resilience Act (White House Office)",
    text: `The Systems Resilience Act would:
1. Establish a White House Office of Systemic Resilience (WOSR) with a staff of 75 and budget of $35 million per year
2. Require all federal agencies to produce annual compounding risk assessments mapping climate, democratic erosion, public health, and supply chain vulnerabilities
3. Create an interagency Resilience Coordination Fund ($500 million mandatory) for cross-agency resilience projects
4. Direct FEMA to develop a National Cascading Disaster Protocol with $200 million in discretionary funding
5. Establish a National Resilience Dashboard requiring real-time data sharing across agencies (IT appropriation: $150 million)
6. New grant program: $300 million/yr for state resilience planning offices`
  },
];

// ─── DIRECTION BADGE ──────────────────────────────────────────────────────────

const ProvisionBadge = ({ type }) => {
  const colors = {
    medicaid_expansion: "#e07b39",
    medicaid_restriction: "#4a9",
    medicare_change: "#e07b39",
    social_security: "#e07b39",
    snap_change: "#e07b39",
    new_program_mandatory: "#c94",
    discretionary_new: "#c94",
    discretionary_change: "#9ab",
    revenue_individual_tax: "#5a8",
    revenue_corporate_tax: "#5a8",
    revenue_payroll_tax: "#5a8",
    revenue_new_fee: "#5a8",
    irs_enforcement: "#6a9",
    immigration_restriction: "#8ab",
    tariff_change: "#ab8",
    direct_spending: "#c94",
  };
  const labels = {
    medicaid_expansion: "Mandatory ↑",
    medicaid_restriction: "Mandatory ↓",
    medicare_change: "Medicare",
    social_security: "Soc. Security",
    snap_change: "SNAP",
    new_program_mandatory: "New Mandatory",
    discretionary_new: "Discretionary ↑",
    discretionary_change: "Discretionary Δ",
    revenue_individual_tax: "Revenue ↑",
    revenue_corporate_tax: "Corp. Revenue",
    revenue_payroll_tax: "Payroll Tax",
    revenue_new_fee: "Fee/User Charge",
    irs_enforcement: "IRS Enforcement",
    immigration_restriction: "Immigration",
    tariff_change: "Tariff",
    direct_spending: "Direct Spending",
  };
  const col = colors[type] || "#888";
  return (
    <span style={{
      background: col + "22", color: col,
      border: `1px solid ${col}44`,
      borderRadius: 3, padding: "2px 7px", fontSize: 11,
      fontFamily: "monospace", fontWeight: 600, letterSpacing: 0.5,
      whiteSpace: "nowrap",
    }}>
      {labels[type] || type}
    </span>
  );
};

const ConfidenceDot = ({ level }) => {
  const colors = { high: "#4a9", medium: "#c94", low: "#c44" };
  return (
    <span style={{ color: colors[level] || "#888", fontSize: 11, fontFamily: "monospace" }}>
      {level === "high" ? "● HIGH" : level === "medium" ? "● MED" : "● LOW"}
    </span>
  );
};

// ─── MAIN COMPONENT ───────────────────────────────────────────────────────────

export default function CBOScorer() {
  const newSection = (id) => ({ id, title: "Section " + id, text: "" });
  const [sections, setSections] = useState([newSection(1)]);
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState(null);
  const [sectionResults, setSectionResults] = useState([]);
  const [scores, setScores] = useState(null);
  const [error, setError] = useState(null);
  const [rawDebug, setRawDebug] = useState(null);
  const [activeTab, setActiveTab] = useState("input");
  const [renderCrash, setRenderCrash] = useState(null);
  const [loadingMsg, setLoadingMsg] = useState("");
  const [loadingProgress, setLoadingProgress] = useState({ current: 0, total: 0 });

  const addSection = () => {
    setSections(prev => [...prev, newSection(prev.length + 1)]);
  };
  const removeSection = (id) => {
    setSections(prev => prev.filter(s => s.id !== id));
  };
  const updateSection = (id, field, value) => {
    setSections(prev => prev.map(s => s.id === id ? { ...s, [field]: value } : s));
  };

  const callAPI = async (sysprompt, userMsg, maxTok=6000) => {
    const body = { model: "claude-sonnet-4-6", max_tokens: maxTok,
      messages: [{ role: "user", content: userMsg }] };
    if (sysprompt) body.system = sysprompt;

    let response;
    try {
      response = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
    } catch(fetchErr) {
      throw new Error(`fetch() threw: ${fetchErr.message}`);
    }

    let raw = "";
    try { raw = await response.text(); }
    catch(textErr) { raw = `response.text() threw: ${textErr.message}`; }
    setRawDebug(`HTTP ${response.status} | ok=${response.ok}\n\n${raw.slice(0, 2000)}`);

    if (!response.ok) throw new Error(`HTTP ${response.status}: ${raw.slice(0, 300)}`);
    let data;
    try { data = JSON.parse(raw); }
    catch(e) { throw new Error(`Response not JSON (${raw.slice(0,100)})`); }
    if (data.error) throw new Error(`API: ${JSON.stringify(data.error).slice(0,200)}`);
    return data;
  };

  const testConnection = useCallback(async () => {
    setLoading(true); setError(null); setRawDebug(null);
    try {
      const data = await callAPI("You are a helpful assistant.", "Say exactly: CONNECTION OK", 50);
      const text = data.content?.[0]?.text || "(no text)";
      setRawDebug(prev => (prev||"") + "\n\nMODEL SAID: " + text);
      setError(null);
    } catch(e) {
      setError("Connection test failed: " + e.message);
    } finally { setLoading(false); }
  }, []);

  // Score a single chunk of provision lines → returns provisions array
  const scoreChunk = async (lines, billContext, chunkLabel) => {
    const data = await callAPI(
      SYSTEM_PROMPT,
      "Score these provisions. Context: " + billContext + "\n\nProvisions:\n" + lines.join("\n"),
      8000
    );
    const text = data.content?.[0]?.text || "";
    if (!text) throw new Error("Empty response for chunk: " + chunkLabel);
    const stripped = text.replace(/^```json\s*/,"").replace(/^```\s*/,"").replace(/```\s*$/,"").trim();
    const start = stripped.indexOf("{");
    const end = stripped.lastIndexOf("}");
    if (start === -1 || end === -1) throw new Error("No JSON for chunk: " + chunkLabel);
    let parsed;
    try { parsed = JSON.parse(stripped.slice(start, end+1)); }
    catch(pe) { throw new Error("JSON failed (" + chunkLabel + "): " + pe.message); }
    return parsed.provisions || [];
  };

  // Score one section through full Pass 1 + Pass 2 pipeline
  const scoreSection = async (section, sectionIdx, totalSections) => {
    const cleanText = sanitizeBill(section.text);
    const label = section.title || ("Section " + section.id);

    setLoadingMsg("Section " + (sectionIdx+1) + "/" + totalSections + " — " + label + ": extracting provisions...");

    // Pass 1: extract plain-English provision list
    const pass1Data = await callAPI(
      EXTRACT_PROMPT,
      "Extract the fiscal provisions from this bill section titled \"" + label + "\":\n\n" + cleanText,
      2000
    );
    const summary = pass1Data.content?.[0]?.text || "";
    if (!summary || summary.includes("NO FISCAL PROVISIONS")) {
      return { sectionId: section.id, title: label, provisions: [], noFiscal: true };
    }

    // Pass 2: score in chunks of 15
    const allLines = summary.split("\n").filter(l => l.trim().startsWith("PROVISION:"));
    const billContext = label + ": " + cleanText.slice(0, 200);
    const CHUNK_SIZE = 15;
    const chunks = allLines.length > 0
      ? Array.from({ length: Math.ceil(allLines.length / CHUNK_SIZE) }, (_, i) => allLines.slice(i*CHUNK_SIZE, (i+1)*CHUNK_SIZE))
      : [summary.split("\n").slice(0, 20)];

    let provisions = [];
    for (let ci = 0; ci < chunks.length; ci++) {
      setLoadingMsg("Section " + (sectionIdx+1) + "/" + totalSections + " — " + label + ": scoring chunk " + (ci+1) + "/" + chunks.length + "...");
      const chunkProvs = await scoreChunk(chunks[ci], billContext, label + " chunk " + ci);
      provisions = provisions.concat(chunkProvs);
    }

    return { sectionId: section.id, title: label, provisions, noFiscal: false };
  };

  const analyze = useCallback(async () => {
    const activeSections = sections.filter(s => s.text.trim().length > 0);
    if (activeSections.length === 0) return;
    setLoading(true); setError(null); setRawDebug(null);
    setSectionResults([]); setAnalysis(null); setScores(null);
    setLoadingProgress({ current: 0, total: activeSections.length });
    try {
      const results = [];
      for (let i = 0; i < activeSections.length; i++) {
        setLoadingProgress({ current: i + 1, total: activeSections.length });
        const result = await scoreSection(activeSections[i], i, activeSections.length);
        results.push(result);
      }

      setLoadingMsg("Assembling unified results...");

      // Merge all provisions, re-sequence IDs
      let allProvisions = [];
      results.forEach(r => {
        const offset = allProvisions.length;
        r.provisions.forEach((p, j) => {
          allProvisions.push({ ...p, id: "p" + (offset + j + 1), _section: r.title });
        });
      });

      const scoredSections = results.map(r => {
        const engine = runScoringEngine(r.provisions);
        return { ...r, engine };
      });
      setSectionResults(scoredSections);

      const merged = {
        billTitle: activeSections.length === 1
          ? (activeSections[0].title || "Analyzed Legislation")
          : "Legislative Package (" + activeSections.length + " sections)",
        summary: activeSections.length === 1
          ? "Single-section legislation with " + allProvisions.length + " scored provisions."
          : "Multi-section legislative package with " + activeSections.length + " sections and " + allProvisions.length + " total provisions scored against the CBO February 2026 baseline.",
        scoringBaseline: "CBO February 2026",
        provisions: allProvisions,
        macroFlags: { gdpEffect: "mixed", gdpMagnitude: "large (>0.5% GDP)", laborForceEffect: "mixed", notes: "Package scored section-by-section; macro interactions between sections not modeled." },
        conventionalScore: "requires judgment"
      };

      try {
        const engineResult = runScoringEngine(allProvisions);
        setAnalysis(merged);
        setScores(engineResult);
        setActiveTab("results");
      } catch(re) { setRenderCrash(re.message); }
    } catch(e) {
      setError(e.message || "Unknown error");
    } finally {
      setLoading(false);
      setLoadingMsg("");
      setLoadingProgress({ current: 0, total: 0 });
    }
  }, [sections]);

  const totalDeficitChange10yr = scores?.total10yr || 0;
  const uncertaintyRange = scores ? Math.abs(scores.total10yr) * scores.uncertaintyMultiplier : 0;

  const styles = {
    app: {
      minHeight: "100vh",
      background: "#0d1117",
      color: "#e8e6e0",
      fontFamily: "'Georgia', 'Times New Roman', serif",
    },
    header: {
      background: "#0a1628",
      borderBottom: "2px solid #1c3d6e",
      padding: "18px 32px",
      display: "flex", alignItems: "center", gap: 16,
    },
    logo: {
      width: 36, height: 36, borderRadius: "50%",
      background: "linear-gradient(135deg,#1c3d6e,#2a5a9e)",
      display: "flex", alignItems: "center", justifyContent: "center",
      fontSize: 16, fontWeight: 700, color: "#d4a017",
      fontFamily: "monospace", flexShrink: 0,
    },
    title: { fontSize: 20, fontWeight: 700, color: "#e8e6e0", letterSpacing: 0.5 },
    subtitle: { fontSize: 12, color: "#7a8a9a", marginTop: 2, fontFamily: "monospace" },
    badge: {
      background: "#1c3d6e22", border: "1px solid #1c3d6e",
      color: "#6a9cc0", fontSize: 10, padding: "2px 8px",
      borderRadius: 3, fontFamily: "monospace", letterSpacing: 0.5,
      marginLeft: "auto",
    },
    main: { maxWidth: 1200, margin: "0 auto", padding: "28px 24px" },
    tabs: {
      display: "flex", gap: 0, marginBottom: 28,
      borderBottom: "1px solid #1c3d6e",
    },
    tab: (active) => ({
      padding: "10px 24px", cursor: "pointer",
      background: "none", border: "none",
      color: active ? "#d4a017" : "#6a8aa0",
      borderBottom: active ? "2px solid #d4a017" : "2px solid transparent",
      fontFamily: "Georgia, serif", fontSize: 14,
      fontWeight: active ? 600 : 400, letterSpacing: 0.5,
      transition: "all 0.15s",
    }),
    card: {
      background: "#0f1923", border: "1px solid #1c3d6e",
      borderRadius: 6, padding: 24, marginBottom: 20,
    },
    cardTitle: {
      fontSize: 13, fontFamily: "monospace", fontWeight: 600,
      color: "#6a9cc0", letterSpacing: 1, textTransform: "uppercase",
      marginBottom: 14,
    },
    textarea: {
      width: "100%", minHeight: 220,
      background: "#060c14", border: "1px solid #1c3d6e",
      color: "#d4d0c8", borderRadius: 4, padding: 16,
      fontFamily: "monospace", fontSize: 13, lineHeight: 1.7,
      resize: "vertical", outline: "none",
      boxSizing: "border-box",
    },
    sampleBtn: {
      background: "#0a1628", border: "1px solid #1c3d6e44",
      color: "#6a9cc0", padding: "6px 14px",
      borderRadius: 4, cursor: "pointer", fontSize: 12,
      fontFamily: "monospace", transition: "all 0.15s",
    },
    analyzeBtn: {
      background: loading ? "#1c3d6e44" : "linear-gradient(135deg,#1c3d6e,#2a5a9e)",
      color: loading ? "#6a8aa0" : "#e8e6e0",
      border: "none", padding: "13px 40px",
      borderRadius: 4, cursor: loading ? "default" : "pointer",
      fontSize: 14, fontWeight: 600, letterSpacing: 0.5,
      fontFamily: "monospace", transition: "all 0.15s",
      marginTop: 16,
    },
    summaryGrid: {
      display: "grid", gridTemplateColumns: "1fr 1fr 1fr",
      gap: 16, marginBottom: 20,
    },
    summaryCell: {
      background: "#0a1628", border: "1px solid #1c3d6e",
      borderRadius: 6, padding: "18px 20px", textAlign: "center",
    },
    table: {
      width: "100%", borderCollapse: "collapse",
      fontFamily: "monospace", fontSize: 12,
    },
    th: {
      padding: "8px 12px", textAlign: "right",
      background: "#0a1628", color: "#6a9cc0",
      borderBottom: "1px solid #1c3d6e",
      fontSize: 11, letterSpacing: 0.5,
    },
    thLeft: {
      padding: "8px 12px", textAlign: "left",
      background: "#0a1628", color: "#6a9cc0",
      borderBottom: "1px solid #1c3d6e",
      fontSize: 11, letterSpacing: 0.5,
    },
    td: {
      padding: "7px 12px", textAlign: "right",
      borderBottom: "1px solid #1c2d3e11",
      color: "#c0bdb5",
    },
    tdLeft: {
      padding: "7px 12px", textAlign: "left",
      borderBottom: "1px solid #1c2d3e11",
      color: "#c0bdb5",
    },
    cost: { color: "#e07b39" },
    save: { color: "#5a9e7a" },
    neutral: { color: "#7a8a9a" },
  };

  const renderSummaryVal = (val, size = 28) => {
    const abs = Math.abs(val);
    const str = abs >= 1000 ? `$${(abs/1000).toFixed(1)}T` : `$${abs.toFixed(1)}B`;
    const label = val > 0.05 ? "DEFICIT INCREASE" : val < -0.05 ? "DEFICIT REDUCTION" : "ROUGHLY NEUTRAL";
    const color = val > 0.05 ? "#e07b39" : val < -0.05 ? "#5a9e7a" : "#7a8a9a";
    return (
      <>
        <div style={{ fontSize: size, fontWeight: 700, color, fontFamily: "monospace", letterSpacing: -0.5 }}>
          {Math.abs(val) < 0.05 ? "—" : (val > 0 ? "+" : "−") + str}
        </div>
        <div style={{ fontSize: 10, color: "#6a8aa0", marginTop: 4, letterSpacing: 0.5 }}>{label}</div>
      </>
    );
  };

  if (renderCrash) return (
    <div style={{padding:40,background:"#0d1117",minHeight:"100vh",color:"#e8e6e0",fontFamily:"monospace"}}>
      <div style={{background:"#1a0a0a",border:"1px solid #8b2020",borderRadius:6,padding:24,maxWidth:700}}>
        <div style={{color:"#e05050",fontWeight:700,marginBottom:8}}>⚠ RENDER ERROR</div>
        <div style={{color:"#c08080",fontSize:12,wordBreak:"break-all",marginBottom:16}}>{renderCrash}</div>
        <button onClick={()=>{ setRenderCrash(null); setAnalysis(null); setScores(null); setError(null); }}
          style={{background:"#1c3d6e",border:"none",color:"#e8e6e0",padding:"8px 20px",
            borderRadius:4,cursor:"pointer",fontFamily:"monospace"}}>
          Reset
        </button>
      </div>
    </div>
  );

  return (
    <div style={styles.app}>
      {/* ── Header ── */}
      <div style={styles.header}>
        <div style={styles.logo}>CBO</div>
        <div>
          <div style={styles.title}>Legislative Budget Scoring Engine</div>
          <div style={styles.subtitle}>
            Calibrated to CBO February 2026 Baseline · FY2026–2035
          </div>
        </div>
        <div style={styles.badge}>ANALYTICAL TOOL · NOT OFFICIAL CBO OUTPUT</div>
      </div>

      <div style={styles.main}>
        {/* ── Global Error Banner ── */}
        {error && (
          <div style={{
            background: "#1a0a0a", border: "1px solid #8b2020",
            borderRadius: 6, padding: "16px 20px", marginBottom: 20,
          }}>
            <div style={{ fontFamily: "monospace", fontSize: 12,
              color: "#e05050", fontWeight: 700, marginBottom: 6 }}>
              ⚠ SCORING ERROR
            </div>
            <div style={{ fontFamily: "monospace", fontSize: 12,
              color: "#c08080", wordBreak: "break-all", marginBottom: rawDebug ? 12 : 0 }}>
              {error}
            </div>
            {rawDebug && (
              <>
                <div style={{ fontFamily: "monospace", fontSize: 11,
                  color: "#6a4a4a", marginBottom: 4 }}>
                  RAW API RESPONSE (first 2000 chars):
                </div>
                <pre style={{
                  fontFamily: "monospace", fontSize: 10, color: "#7a6a6a",
                  background: "#100808", padding: 10, borderRadius: 4,
                  overflowX: "auto", maxHeight: 200, overflow: "auto",
                  whiteSpace: "pre-wrap", wordBreak: "break-all", margin: 0,
                }}>
                  {rawDebug}
                </pre>
              </>
            )}
          </div>
        )}

        {/* ── Tabs ── */}
        <div style={styles.tabs}>
          {[["input","Input & Analysis"],["results","Score Results"],["methodology","Methodology"]].map(([id,label]) => (
            <button key={id} style={styles.tab(activeTab===id)} onClick={() => setActiveTab(id)}>
              {label}
            </button>
          ))}
        </div>

        {/* ── INPUT TAB ── */}
        {activeTab === "input" && (
          <>
            {/* Section inputs */}
            {sections.map((sec, idx) => (
              <div key={sec.id} style={styles.card}>
                <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 12 }}>
                  <div style={{ fontFamily: "monospace", fontSize: 11, color: "#6a9cc0",
                    letterSpacing: 1, textTransform: "uppercase", flex: 1 }}>
                    Section {idx + 1}
                  </div>
                  <input
                    style={{ background: "#060c14", border: "1px solid #1c3d6e44",
                      color: "#d4d0c8", borderRadius: 3, padding: "4px 10px",
                      fontFamily: "monospace", fontSize: 12, width: 220, outline: "none" }}
                    value={sec.title}
                    onChange={e => updateSection(sec.id, "title", e.target.value)}
                    placeholder="Section title (e.g. Healthcare)"
                  />
                  {sections.length > 1 && (
                    <button
                      onClick={() => removeSection(sec.id)}
                      style={{ background: "none", border: "1px solid #3a1a1a",
                        color: "#7a4a4a", borderRadius: 3, padding: "4px 10px",
                        cursor: "pointer", fontFamily: "monospace", fontSize: 11 }}>
                      ✕ Remove
                    </button>
                  )}
                </div>
                <textarea
                  style={{ ...styles.textarea, minHeight: 160 }}
                  placeholder={"Paste bill text, legislative summary, or list of provisions for " + (sec.title || "this section") + "..."}
                  value={sec.text}
                  onChange={e => updateSection(sec.id, "text", e.target.value)}
                />
                <div style={{ fontSize: 11, color: sec.text.length > 24000 ? "#c94" : "#4a6a7a",
                  fontFamily: "monospace", marginTop: 5 }}>
                  {sec.text.length > 0 && (sec.text.length.toLocaleString() + " chars" + (sec.text.length > 24000 ? " — will be truncated to 25,000" : ""))}
                </div>
              </div>
            ))}

            {/* Add Section + Sample buttons */}
            <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 16, alignItems: "center" }}>
              <button
                onClick={addSection}
                disabled={loading}
                style={{ background: "#0a1628", border: "1px solid #1c3d6e",
                  color: "#6a9cc0", padding: "9px 18px", borderRadius: 4,
                  cursor: "pointer", fontFamily: "monospace", fontSize: 12,
                  fontWeight: 600, letterSpacing: 0.5 }}>
                + ADD SECTION
              </button>
              <span style={{ fontSize: 11, color: "#4a6a7a", fontFamily: "monospace" }}>SAMPLES →</span>
              {SAMPLES.map(s => (
                <button key={s.label} style={styles.sampleBtn}
                  onClick={() => {
                    setSections([{ id: 1, title: s.label, text: s.text }]);
                  }}>
                  {s.label}
                </button>
              ))}
            </div>

            {/* Progress bar when running */}
            {loading && loadingProgress.total > 1 && (
              <div style={{ ...styles.card, padding: "14px 20px", marginBottom: 16 }}>
                <div style={{ fontFamily: "monospace", fontSize: 11, color: "#6a9cc0",
                  marginBottom: 8, letterSpacing: 0.5 }}>
                  PROCESSING {loadingProgress.current}/{loadingProgress.total} SECTIONS
                </div>
                <div style={{ background: "#060c14", borderRadius: 3, height: 6, overflow: "hidden" }}>
                  <div style={{
                    background: "linear-gradient(90deg,#1c3d6e,#2a7acc)",
                    height: "100%", borderRadius: 3,
                    width: (loadingProgress.total > 0
                      ? (loadingProgress.current / loadingProgress.total * 100)
                      : 0) + "%",
                    transition: "width 0.4s ease"
                  }} />
                </div>
              </div>
            )}

            {/* Score + Test buttons */}
            <div style={{ display: "flex", gap: 10, alignItems: "center", flexWrap: "wrap", marginBottom: 20 }}>
              <button style={styles.analyzeBtn} onClick={analyze} disabled={loading}>
                {loading
                  ? "⟳ " + (loadingMsg || "ANALYZING...")
                  : "▶ SCORE " + (sections.filter(s=>s.text.trim()).length > 1
                      ? sections.filter(s=>s.text.trim()).length + " SECTIONS"
                      : "LEGISLATION")}
              </button>
              <button style={{...styles.analyzeBtn, background:"#0a1628",
                border:"1px solid #1c3d6e44", color:"#6a9cc0", padding:"13px 20px"}}
                onClick={testConnection} disabled={loading}>
                TEST API
              </button>
              {sections.filter(s=>s.text.trim()).length > 1 && (
                <div style={{ fontFamily: "monospace", fontSize: 11, color: "#5a7a9a" }}>
                  {sections.filter(s=>s.text.trim()).length} sections ·{" "}
                  {sections.filter(s=>s.text.trim()).reduce((n,s)=>n+s.text.length,0).toLocaleString()} total chars
                </div>
              )}
            </div>

            {/* Baseline Quick Reference */}
            <div style={styles.card}>
              <div style={styles.cardTitle}>CBO February 2026 Baseline — Quick Reference</div>
              <div style={{ overflowX: "auto" }}>
                <table style={styles.table}>
                  <thead>
                    <tr>
                      <th style={styles.thLeft}>Category</th>
                      {BASELINE.years.map(y => <th key={y} style={styles.th}>{y}</th>)}
                      <th style={styles.th}>10-Yr Total</th>
                    </tr>
                  </thead>
                  <tbody>
                    {[
                      ["GDP"          , BASELINE.gdp],
                      ["Total Revenues", BASELINE.revenues],
                      ["Mandatory"    , BASELINE.mandatory],
                      ["Discretionary", BASELINE.discretionary],
                      ["Net Interest" , BASELINE.netInterest],
                      ["Total Deficit(−)", BASELINE.deficits],
                    ].map(([label, vals]) => (
                      <tr key={label}>
                        <td style={styles.tdLeft}>{label}</td>
                        {vals.map((v,i) => <td key={i} style={styles.td}>{fmt(v)}</td>)}
                        <td style={{...styles.td, color: "#d4a017"}}>
                          {fmt(vals.reduce((a,b)=>a+b,0))}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              <div style={{ fontSize: 11, color: "#4a6a7a", marginTop: 8, fontFamily: "monospace" }}>
                Billions of dollars. Source: CBO, The Budget and Economic Outlook 2026–2036 (Feb 2026).
              </div>
            </div>
          </>
        )}

        {/* ── RESULTS TAB ── */}
        {activeTab === "results" && (
          !analysis ? (
            <div style={{ ...styles.card, textAlign: "center", padding: 60 }}>
              <div style={{ fontSize: 48, marginBottom: 16 }}>∅</div>
              <div style={{ color: "#6a8aa0", fontFamily: "monospace", fontSize: 13 }}>
                No analysis yet. Enter legislation in the Input tab and click Score Legislation.
              </div>
            </div>
          ) : (
            <>
              {/* Bill Header */}
              <div style={{ ...styles.card, background: "#0a1628" }}>
                <div style={{ fontSize: 18, fontWeight: 700, color: "#d4a017", marginBottom: 6 }}>
                  {analysis.billTitle || "Untitled Legislation"}
                </div>
                <div style={{ fontSize: 13, color: "#a0aab4", lineHeight: 1.7, marginBottom: 14 }}>
                  {analysis.summary}
                </div>
                <div style={{ display: "flex", gap: 20, flexWrap: "wrap" }}>
                  <div style={{ fontFamily: "monospace", fontSize: 11, color: "#6a9cc0" }}>
                    BASELINE: {analysis.scoringBaseline || "CBO Feb 2026"}
                  </div>
                  <div style={{ fontFamily: "monospace", fontSize: 11, color: "#6a9cc0" }}>
                    PROVISIONS: {analysis.provisions?.length || 0} identified
                  </div>
                  <div style={{ fontFamily: "monospace", fontSize: 11, color:
                    analysis.conventionalScore?.includes("high") ? "#5a9e7a" :
                    analysis.conventionalScore?.includes("requires") ? "#c94" : "#c44" }}>
                    CONFIDENCE: {analysis.conventionalScore?.toUpperCase() || "UNKNOWN"}
                  </div>
                </div>
              </div>

              {/* 10-Year Summary Totals */}
              <div style={styles.summaryGrid}>
                {[
                  ["1-Year Effect",   scores?.total1yr,   "FY2026"],
                  ["5-Year Total",    scores?.total5yr,   "FY2026–2030"],
                  ["10-Year Total",   scores?.total10yr,  "FY2026–2035"],
                ].map(([label, val, period]) => (
                  <div key={label} style={styles.summaryCell}>
                    <div style={{ fontSize: 11, color: "#6a8aa0", fontFamily: "monospace",
                      letterSpacing: 0.5, marginBottom: 8 }}>{label.toUpperCase()}</div>
                    {renderSummaryVal(val || 0, 24)}
                    <div style={{ fontSize: 10, color: "#4a6a7a", marginTop: 6, fontFamily: "monospace" }}>
                      {period}
                    </div>
                  </div>
                ))}
              </div>

              {/* Per-Section Breakdown */}
              {sectionResults.length > 1 && (
                <div style={styles.card}>
                  <div style={styles.cardTitle}>By-Section Breakdown</div>
                  <div style={{ overflowX: "auto" }}>
                    <table style={styles.table}>
                      <thead>
                        <tr>
                          <th style={styles.thLeft}>Section</th>
                          <th style={styles.th}>Provisions</th>
                          <th style={styles.th}>1-Year</th>
                          <th style={styles.th}>5-Year</th>
                          <th style={styles.th}>10-Year</th>
                          <th style={styles.thLeft}>Primary Effect</th>
                        </tr>
                      </thead>
                      <tbody>
                        {sectionResults.map(sr => {
                          const eng = sr.engine;
                          const col = Math.abs(eng.total10yr) < 0.1 ? "#4a6a7a"
                            : eng.total10yr > 0 ? "#e07b39" : "#5a9e7a";
                          const noFiscal = sr.noFiscal || sr.provisions.length === 0;
                          return (
                            <tr key={sr.sectionId}>
                              <td style={{ ...styles.tdLeft, fontWeight: 600, color: "#d4a017" }}>
                                {sr.title}
                              </td>
                              <td style={{ ...styles.td, color: "#6a9cc0" }}>
                                {noFiscal ? "—" : sr.provisions.length}
                              </td>
                              <td style={{ ...styles.td, color: col }}>
                                {noFiscal ? "No fiscal provisions" : fmtSign(eng.total1yr)}
                              </td>
                              <td style={{ ...styles.td, color: col }}>
                                {noFiscal ? "—" : fmtSign(eng.total5yr)}
                              </td>
                              <td style={{ ...styles.td, fontWeight: 700, color: col }}>
                                {noFiscal ? "—" : fmtSign(eng.total10yr)}
                              </td>
                              <td style={{ ...styles.tdLeft, fontSize: 11, color: "#7a8a9a" }}>
                                {noFiscal ? "Administrative/procedural only" : (
                                  eng.total10yr > 0 ? "Net spending increase" :
                                  eng.total10yr < 0 ? "Net deficit reduction" : "Roughly neutral"
                                )}
                              </td>
                            </tr>
                          );
                        })}
                        <tr style={{ background: "#0a1628", borderTop: "1px solid #1c3d6e" }}>
                          <td style={{ ...styles.tdLeft, fontWeight: 700, color: "#d4a017" }}>TOTAL PACKAGE</td>
                          <td style={{ ...styles.td, color: "#6a9cc0", fontWeight: 700 }}>
                            {analysis?.provisions?.length || 0}
                          </td>
                          <td style={{ ...styles.td, fontWeight: 700,
                            color: (scores?.total1yr||0) > 0 ? "#e07b39" : "#5a9e7a" }}>
                            {fmtSign(scores?.total1yr || 0)}
                          </td>
                          <td style={{ ...styles.td, fontWeight: 700,
                            color: (scores?.total5yr||0) > 0 ? "#e07b39" : "#5a9e7a" }}>
                            {fmtSign(scores?.total5yr || 0)}
                          </td>
                          <td style={{ ...styles.td, fontWeight: 700,
                            color: (scores?.total10yr||0) > 0 ? "#e07b39" : "#5a9e7a" }}>
                            {fmtSign(scores?.total10yr || 0)}
                          </td>
                          <td style={{ ...styles.tdLeft, fontSize: 11, color: "#7a8a9a" }}>
                            {sectionResults.length} sections combined
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              )}

              {/* Uncertainty Range */}
              {scores && Math.abs(scores.total10yr) > 0.1 && (
                <div style={{ ...styles.card, background: "#0a1220",
                  borderColor: "#c9400022", marginBottom: 20 }}>
                  <div style={{ fontFamily: "monospace", fontSize: 12, color: "#c94" }}>
                    ◈ UNCERTAINTY RANGE (10-year, ±{safeFix(scores.uncertaintyMultiplier*100,0)}%)
                  </div>
                  <div style={{ fontFamily: "monospace", fontSize: 14, color: "#d4a017", marginTop: 6 }}>
                    {fmtSign((scores.total10yr)*(1-scores.uncertaintyMultiplier))} to {fmtSign((scores.total10yr)*(1+scores.uncertaintyMultiplier))}
                  </div>
                  <div style={{ fontSize: 11, color: "#6a7a8a", marginTop: 4 }}>
                    CBO typically presents uncertainty ranges for cost estimates. This range reflects provision-level confidence assessments.
                    Actual CBO score would incorporate additional program-specific detail.
                  </div>
                </div>
              )}

              {/* 10-Year Budget Effect Table */}
              <div style={styles.card}>
                <div style={styles.cardTitle}>Budget Effects by Category — FY2026–FY2035</div>
                <div style={{ overflowX: "auto" }}>
                  <table style={styles.table}>
                    <thead>
                      <tr>
                        <th style={styles.thLeft}>Category</th>
                        {BASELINE.years.map(y => <th key={y} style={styles.th}>{y}</th>)}
                        <th style={{ ...styles.th, color: "#d4a017" }}>2026–35</th>
                      </tr>
                    </thead>
                    <tbody>
                      {[
                        ["Mandatory Outlays",   "mandatoryChange"],
                        ["Discretionary Outlays","discretionaryChange"],
                        ["Revenue Effect",      "revenueChange"],
                      ].map(([label, key]) => {
                        const row = scores?.byYear?.map(r => r[key]) || BASELINE.years.map(()=>0);
                        const total = row.reduce((a,b)=>a+b,0);
                        const isRev = key === "revenueChange";
                        return (
                          <tr key={label}>
                            <td style={styles.tdLeft}>{label}</td>
                            {row.map((v,i) => (
                              <td key={i} style={{
                                ...styles.td,
                                color: Math.abs(v)<0.05 ? "#4a6a7a" :
                                  (isRev ? (v<0?"#5a9e7a":"#e07b39") : (v>0?"#e07b39":"#5a9e7a"))
                              }}>
                                {Math.abs(v)<0.05 ? "—" : (v>0?"+":"")+safeFix(v,1)}
                              </td>
                            ))}
                            <td style={{
                              ...styles.td, fontWeight: 700,
                              color: Math.abs(total)<0.1 ? "#4a6a7a" :
                                (isRev ? (total<0?"#5a9e7a":"#e07b39") : (total>0?"#e07b39":"#5a9e7a"))
                            }}>
                              {Math.abs(total)<0.1 ? "—" : (total>0?"+":"")+safeFix(total,1)}
                            </td>
                          </tr>
                        );
                      })}

                      <tr style={{ background: "#0a1628" }}>
                        <td style={{ ...styles.tdLeft, fontWeight: 700, color: "#d4a017" }}>
                          Net Deficit Effect
                        </td>
                        {scores?.byYear?.map((r,i) => (
                          <td key={i} style={{
                            ...styles.td, fontWeight: 700,
                            color: Math.abs(r.totalDeficitChange)<0.05 ? "#4a6a7a" :
                              r.totalDeficitChange > 0 ? "#e07b39" : "#5a9e7a"
                          }}>
                            {Math.abs(r.totalDeficitChange)<0.05 ? "—" :
                              (r.totalDeficitChange>0?"+":"") + r.totalDeficitChange.toFixed(1)}
                          </td>
                        ))}
                        <td style={{ ...styles.td, fontWeight: 700, color: "#d4a017" }}>
                          {scores ? ((scores.total10yr>0?"+":"") + scores.total10yr.toFixed(1)) : "—"}
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div style={{ fontSize: 11, color: "#4a6a7a", marginTop: 8, fontFamily: "monospace" }}>
                  Billions of dollars. Positive = deficit increase. Includes estimated debt service effect.
                  Conventional scoring; dynamic effects shown below.
                </div>
              </div>

              {/* Provisions Detail */}
              <div style={styles.card}>
                <div style={styles.cardTitle}>Provision-Level Analysis</div>
                {analysis.provisions?.map((prov, idx) => {
                  const yr0Effect = scoreProvision(prov, 0);
                  const yr4Effect = scoreProvision(prov, 4);
                  return (
                    <div key={prov.id || idx} style={{
                      borderBottom: "1px solid #1c3d6e22",
                      paddingBottom: 16, marginBottom: 16,
                    }}>
                      <div style={{ display: "flex", alignItems: "flex-start",
                        gap: 10, marginBottom: 8, flexWrap: "wrap" }}>
                        <ProvisionBadge type={prov.type} />
                        <ConfidenceDot level={prov.confidence} />
                        <span style={{ fontSize: 14, fontWeight: 600,
                          color: "#e8e6e0", flex: 1, minWidth: 200 }}>
                          {prov.title}
                        </span>
                        {prov._section && sectionResults.length > 1 && (
                          <span style={{ fontSize: 10, color: "#4a6a7a",
                            fontFamily: "monospace", alignSelf: "center",
                            background: "#0a1628", padding: "2px 7px", borderRadius: 3,
                            border: "1px solid #1c3d6e33" }}>
                            {prov._section}
                          </span>
                        )}
                      </div>
                      <div style={{ fontSize: 12, color: "#8a9aaa",
                        marginBottom: 8, lineHeight: 1.6 }}>
                        {prov.description}
                      </div>
                      <div style={{ display: "flex", gap: 20, flexWrap: "wrap" }}>
                        <div style={{ fontFamily: "monospace", fontSize: 11 }}>
                          <span style={{ color: "#4a6a7a" }}>FY2026: </span>
                          <span style={{ color: Math.abs(yr0Effect)<0.05?"#4a6a7a":yr0Effect>0?"#e07b39":"#5a9e7a" }}>
                            {Math.abs(yr0Effect)<0.05 ? "Minimal" : fmtSign(yr0Effect)}
                          </span>
                        </div>
                        <div style={{ fontFamily: "monospace", fontSize: 11 }}>
                          <span style={{ color: "#4a6a7a" }}>FY2030: </span>
                          <span style={{ color: Math.abs(yr4Effect)<0.05?"#4a6a7a":yr4Effect>0?"#e07b39":"#5a9e7a" }}>
                            {Math.abs(yr4Effect)<0.05 ? "Minimal" : fmtSign(yr4Effect)}
                          </span>
                        </div>
                        {prov.cboAnalogy && (
                          <div style={{ fontFamily: "monospace", fontSize: 11, color: "#6a9cc0" }}>
                            Analogy: {prov.cboAnalogy}
                          </div>
                        )}
                      </div>
                      {prov.scoringCaveat && (
                        <div style={{ marginTop: 6, fontSize: 11, color: "#7a6040",
                          background: "#c9400011", padding: "4px 10px", borderRadius: 3,
                          borderLeft: "2px solid #c9400044" }}>
                          ⚠ {prov.scoringCaveat}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>

              {/* Macroeconomic Flags */}
              {analysis.macroFlags && (
                <div style={{ ...styles.card, background: "#0a1220" }}>
                  <div style={styles.cardTitle}>Macroeconomic Effects</div>
                  <div style={{ display: "flex", gap: 20, flexWrap: "wrap", marginBottom: 10 }}>
                    {[
                      ["GDP Effect", analysis.macroFlags.gdpEffect, analysis.macroFlags.gdpMagnitude],
                      ["Labor Force", analysis.macroFlags.laborForceEffect, null],
                    ].map(([label, val, mag]) => (
                      <div key={label} style={{ fontFamily: "monospace", fontSize: 12 }}>
                        <span style={{ color: "#6a8aa0" }}>{label}: </span>
                        <span style={{
                          color: val==="positive"||val==="increase" ? "#5a9e7a" :
                                 val==="negative"||val==="decrease" ? "#e07b39" : "#7a8a9a"
                        }}>
                          {val?.toUpperCase()} {mag ? `(${mag})` : ""}
                        </span>
                      </div>
                    ))}
                  </div>
                  <div style={{ fontSize: 12, color: "#7a8a9a", lineHeight: 1.6 }}>
                    {analysis.macroFlags.notes}
                  </div>
                  <div style={{ marginTop: 10, fontSize: 11, color: "#4a6a7a", fontFamily: "monospace" }}>
                    Note: CBO requires dynamic scoring (macro feedback) only for legislation with gross budgetary
                    effects &gt;0.25% of GDP (~$80B) in any single year. Dynamic effects shown for context only.
                  </div>
                </div>
              )}
            </>
          )
        )}

        {/* ── METHODOLOGY TAB ── */}
        {activeTab === "methodology" && (
          <>
            <div style={styles.card}>
              <div style={styles.cardTitle}>Scoring Methodology & Parameters</div>
              <div style={{ fontSize: 13, color: "#9aaabb", lineHeight: 1.8, marginBottom: 16 }}>
                This tool applies CBO's published scoring methodology and the February 2026 budget baseline.
                It mimics CBO's <strong style={{color:"#d4a017"}}>conventional scoring</strong> approach, which holds nominal GDP
                constant and incorporates microeconomic behavioral responses, but does not run CBO's
                proprietary models (HISIM2, the individual microsimulator, or INFORUM).
              </div>

              {/* Rules of Thumb */}
              <div style={{ marginBottom: 24 }}>
                <div style={{ fontSize: 12, fontFamily: "monospace", color: "#6a9cc0",
                  letterSpacing: 0.5, marginBottom: 12 }}>
                  RULES OF THUMB (per 0.1 percentage point change, 2026–2035 total)
                </div>
                <table style={styles.table}>
                  <thead>
                    <tr>
                      <th style={styles.thLeft}>Scenario</th>
                      <th style={styles.th}>5-Year Effect</th>
                      <th style={styles.th}>10-Year Effect</th>
                      <th style={styles.thLeft}>Primary Channel</th>
                    </tr>
                  </thead>
                  <tbody>
                    {[
                      ["Productivity growth 0.1pp slower","−$100B","−$388B","Revenue loss + lower interest rates"],
                      ["Labor force growth 0.1pp slower","−$47B","−$184B","Revenue loss + higher mandatory outlays"],
                      ["Interest rates 0.1pp higher","−$122B","−$351B","Higher net interest costs"],
                      ["Inflation+rates 0.1pp higher","−$104B","−$324B","Mixed: revenue gain offset by outlay rises"],
                    ].map(([sc,y5,y10,ch]) => (
                      <tr key={sc}>
                        <td style={styles.tdLeft}>{sc}</td>
                        <td style={{...styles.td, color: "#5a9e7a"}}>{y5}</td>
                        <td style={{...styles.td, color: "#5a9e7a"}}>{y10}</td>
                        <td style={{...styles.tdLeft, fontSize:11, color:"#7a8a9a"}}>{ch}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
                <div style={{fontSize:11,color:"#4a6a7a",marginTop:6,fontFamily:"monospace"}}>
                  Source: CBO, How Changes in Economic Conditions Might Affect the Federal Budget: 2025 to 2035 (Jan 2025).
                  Negative = deficit decreases (improvement). Rules approximate CBO's broader models; valid for ±0.5pp productivity,
                  ±0.75pp labor force, ±1.0pp interest/inflation changes.
                </div>
              </div>

              {/* Medicaid Parameters */}
              <div style={{ marginBottom: 24 }}>
                <div style={{ fontSize: 12, fontFamily: "monospace", color: "#6a9cc0",
                  letterSpacing: 0.5, marginBottom: 12 }}>
                  MEDICAID PER-ENROLLEE FEDERAL COSTS (Base FY2026)
                </div>
                <table style={styles.table}>
                  <thead>
                    <tr>
                      <th style={styles.thLeft}>Category</th>
                      <th style={styles.th}>Fed Cost/Enrollee</th>
                      <th style={styles.th}>Federal Match</th>
                      <th style={styles.th}>Annual Growth</th>
                    </tr>
                  </thead>
                  <tbody>
                    {Object.entries(MEDICAID).map(([k,v]) => (
                      <tr key={k}>
                        <td style={styles.tdLeft}>{v.label}</td>
                        <td style={styles.td}>${v.cost.toLocaleString()}</td>
                        <td style={styles.td}>{(v.fmap*100).toFixed(1)}%</td>
                        <td style={styles.td}>{(v.growth*100).toFixed(1)}%</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
                <div style={{fontSize:11,color:"#4a6a7a",marginTop:6,fontFamily:"monospace"}}>
                  Federal share only. States replace ~50% of lost federal funds when FMAP is reduced (CBO behavioral assumption).
                  ACA expansion FMAP is fixed by statute at 90%; standard FMAP varies by state.
                </div>
              </div>

              {/* Key Elasticities */}
              <div>
                <div style={{ fontSize: 12, fontFamily: "monospace", color: "#6a9cc0",
                  letterSpacing: 0.5, marginBottom: 12 }}>
                  KEY ELASTICITIES & PARAMETERS
                </div>
                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
                  {[
                    ["Elasticity of Taxable Income (individual)","0.25 central; 0.12–0.50 range"],
                    ["Labor supply substitution elasticity","0.24 (Solow); 0.29 (life-cycle)"],
                    ["Capital gains realization elasticity","−0.79 (permanent)"],
                    ["Corporate income ETI","~0.20"],
                    ["IRS enforcement return (net)","~$0.35 revenue per $1 spent"],
                    ["State offset: Medicaid FMAP reduction","~50% (states replace half of lost funds)"],
                    ["Discretionary spendout Y1/Y2/Y3","25% / 50% / 75% of BA"],
                    ["Dynamic scoring threshold",">0.25% of GDP (~$80B) in any year"],
                    ["Fiscal multiplier: gov't purchases","0.5–2.5 (economy-dependent)"],
                    ["Fiscal multiplier: transfers","0.4–2.1 (economy-dependent)"],
                  ].map(([param, val]) => (
                    <div key={param} style={{ background: "#0a1628",
                      border: "1px solid #1c3d6e22", borderRadius: 4,
                      padding: "10px 14px" }}>
                      <div style={{ fontSize: 11, color: "#6a8aa0", fontFamily: "monospace",
                        marginBottom: 4 }}>{param}</div>
                      <div style={{ fontSize: 13, color: "#d4a017", fontFamily: "monospace" }}>
                        {val}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Calibration Benchmarks */}
            <div style={styles.card}>
              <div style={styles.cardTitle}>Calibration Benchmarks — Landmark CBO Scores</div>
              <table style={styles.table}>
                <thead>
                  <tr>
                    <th style={styles.thLeft}>Legislation</th>
                    <th style={styles.th}>Year</th>
                    <th style={styles.th}>10-Year Deficit Effect</th>
                    <th style={styles.thLeft}>Key Scoring Features</th>
                  </tr>
                </thead>
                <tbody>
                  {[
                    ["Affordable Care Act","2010","-$124B (reduces)","$848B subsidies offset by $491B Medicare + $486B revenue"],
                    ["Tax Cuts & Jobs Act","2017","+$1,455B conventional","Revenue loss of $1.65T; $194B outlay savings from mandate repeal"],
                    ["American Rescue Plan","2021","+$1,900B","87% spent in first 2 years; COVID-era spending"],
                    ["Infrastructure/IIJA","2021","+$256B","$415B discretionary; $110B direct spending cuts; $50B revenue"],
                    ["CHIPS & Science Act","2022","+$79B","$54B direct + $24B tax credit revenue loss"],
                    ["Inflation Reduction Act","2022","-$238B (reduces)","$313B corporate min tax + $124B IRS vs $386B climate spending"],
                    ["Fiscal Responsibility Act","2023","-$1,500B (reduces)","Discretionary caps + $188B interest savings"],
                    ["IRA Energy Credits (revised)","2023","-$730–786B actual","3× original $270B estimate — demand-driven credit underestimate"],
                  ].map(([leg,yr,effect,notes]) => (
                    <tr key={leg}>
                      <td style={styles.tdLeft}>{leg}</td>
                      <td style={{...styles.td, color:"#6a9cc0"}}>{yr}</td>
                      <td style={{...styles.td, color: effect.includes("-") ? "#5a9e7a" : "#e07b39", fontWeight:600}}>
                        {effect}
                      </td>
                      <td style={{...styles.tdLeft, fontSize:11, color:"#7a8a9a"}}>{notes}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div style={{ ...styles.card, background: "#0a1220",
              borderColor: "#1c3d6e66", fontSize: 12, color: "#6a7a8a",
              lineHeight: 1.7 }}>
              <div style={{ fontFamily: "monospace", color: "#5a6a7a",
                marginBottom: 8, fontSize: 11, letterSpacing: 0.5 }}>
                IMPORTANT LIMITATIONS
              </div>
              This tool produces structured analytical estimates, not official CBO cost estimates.
              It cannot replicate CBO's proprietary HISIM2 health insurance model, individual microsimulator,
              or INFORUM macroeconomic model. Results should be treated as order-of-magnitude approximations
              for internal planning purposes. For official scoring, legislation must be referred to the
              Congressional Budget Office through committee chairs.
              Sources: CBO Budget and Economic Outlook Feb 2026; Rules of Thumb Workbook (cbo.gov/publication/61198);
              HISIM2 documentation; CBO GitHub (github.com/US-CBO).
            </div>
          </>
        )}
      </div>
    </div>
  );
}
