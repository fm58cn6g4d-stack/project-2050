"""Master ledger for Project 2050's 2029-30 trifecta agenda (full rebuild Oct 20, 2026; education batch the same day).

Every row is keyed by its domain-file ID; the legacy ledger ID (H1, E11, DEM1 ...) is kept
in its own column as a crosswalk. All dollar figures are ten-year totals for 2030-39 in
trillions. Positive cost = adds to deficit before financing; negative = savings.
basis: "sourced" (taken or scaled from a cited figure in a Project 2050 doc),
       "scaled" (outside source scaled to 2030-39), "estimate" (my estimate),
       "proposal" (an author's proposal sized against current programs, not a score).

Education batch (Oct 20, evening): FAM-4 moves to domains/domain-education.md and splits into
EDU-1 (K-12 formula funding, carrying EDU-2) and EDU-5 (higher education) at the same totals;
new rows EDU-3 (universal school meals), EDU-4 (educator pipeline), EDU-7 (voucher tax-credit
repeal, a saving) and EDU-8 (AI in education, student data and research, appropriations).
Climate durability options (CLI-9 to CLI-13) and Talarico-scenario options are not chosen and
add no rows; they appear in CONFLICTS and in the revenue menu where they carry a revenue figure.

Decisions later on Oct 20 (Espen): REV-C1 takes the durability session's price path ($25 rising to
~$100 by 2037, road fuels still exempt), so C1 is $1.35T and CLI-2's dividend $1.08T; D4 lets
borrowing finance time-limited climate capital (new alternative cut C37, exclusive with C29);
REV-E1/C35 restated as the increment beyond G9 (~$0.15T); DEM-1F adopted (DEM-1 after R1).
Cuts listed in ALT_CUTS are alternatives to another cut and are not summed.
"""
import csv, json

BUDGET_DAYS = 163  # 148 discretionary days (unified inventory) + 15 freed by Block 1's nomination caps (C28, hedged; estimate)
RECON_DAYS = 15    # floor days per reconciliation bill (frameworks/radical-means-moderate-ends.md)
RESOLUTION_DAYS = 2  # budget resolution vote-a-rama per vehicle (estimate)

RAILS = {
    "R1": "Reconciliation I (FY2029 resolution, spring 2029)",
    "R2": "Reconciliation II (FY2030 resolution, fall 2029)",
    "R3": "Reconciliation III (FY2031 resolution, summer 2030)",
    "FLOOR": "Regular order (needs majority cloture)",
    "APPROPS": "Annual appropriations",
    "LATER": "After the 2029-30 window",
    "T2": "Second trifecta (2033-36)",
}

# id, legacy ledger id, bill, domain, source file, rail, channel, lo, mid, hi, own_rev_mid, basis, note,
# floor days, months to felt impact (after enactment), durability 0-100, target enactment (YYYY-MM)
B = [
 # ---- Health (domain-health.md) ----
 ("HLT-1","H1","Health I: Restore (repeal H.R. 1 cuts, permanent ACA credits, coverage gap)","Health","domain-health.md","R1","General fund",2.25,2.45,2.65,0,"sourced","Go-big tab, Title I","0",9,75,"2029-04"),
 ("HLT-2","H2","Health II: Medicare upgrades ($5,000 cap, dental/vision/hearing, physician pay); Medicare at 60 is a scored add-on (D6)","Health","domain-health.md","R2","General fund",0.9,1.07,1.24,0,"sourced","Go-big Title II less Medicare at 60 ($0.30-0.36T); dental kept in","0",24,85,"2029-10"),
 ("HLT-3","H3","Health III: Public option guarantee with auto-enrollment (carries HLT-5)","Health","domain-health.md","FLOOR","General fund",1.6,1.9,2.2,0,"sourced","Go-big Title III; needs D2; must pass in the first trifecta (Espen, Oct 19)","8",18,78,"2030-02"),
 ("HLT-4","H4","Health IV: Medicaid, long-term care, safety net","Health","domain-health.md","R1","General fund",0.4,0.625,0.85,0,"sourced","Go-big tab, Title IV; LAB-3's home-care wage floor adds an unscored Medicaid rate cost","0",9,75,"2029-04"),
 ("HLT-5","H5","[Rides HLT-3 (C12)] Health V: Prices and market power (hospital cap, commercial drug prices)","Health","domain-health.md","FLOOR","General fund",-0.45,-0.40,-0.35,0,"sourced","Go-big tab, Title V (savings); the non-compete ban lives in COM-4","0",24,60,"2030-02"),
 ("HLT-6","H6","Health VI: Medicare payment reform (all MA overpayment captured, 50 drugs/yr, site-neutral), general-fund share","Health","domain-health.md","R1","General fund",-1.6,-1.25,-0.9,0,"estimate","Total -$1.4 to -2.5T; ~$0.7T (0.5-0.9) accrues to HI and is credited there","0",24,70,"2029-04"),
 # ---- Family (domain-family.md) ----
 ("FAM-1","F1","Permanent expanded Child Tax Credit, monthly and fully refundable","Family","domain-family.md","R1","General fund",1.3,1.5,1.8,0,"scaled","TPC: American Family Act $1.4T FY2026-35 vs current law ($2,200 credit)","0",5,72,"2029-04"),
 ("FAM-2","F2","Child care and universal pre-K, phased (pre-K and lowest-income tier first; full 7% cap from 2032)","Family","domain-family.md","R2","General fund",0.4,0.6,0.9,0,"scaled","CRFB: $475-800B through 2031 if permanent; phasing saves ~$0.3T. FAM-2D carries the Bonamici pre-K standards (Oct 20)","0",20,80,"2029-10"),
 ("FAM-3","F3","Paid family and medical leave, 12 weeks, social insurance, 0.6% contribution stepping toward 0.85%","Family","domain-family.md","R2","Paid-leave fund",0.6,0.9,1.4,0.9,"estimate","CBO $547B (BBB-era design); JCT break-even 0.85%; 0.6% raises ~$0.9T","0",14,78,"2029-10"),
 # ---- Education (domain-education.md; new Oct 20, replaces FAM-4) ----
 ("EDU-1","F4","K-12 and special education formula funding as mandatory spending: Title I to $26B; IDEA on a statutory path to the 40% federal share (carries EDU-2); IDEA restraint-and-seclusion rules as conditions on the new money","Education","domain-education.md","R2","General fund",0.25,0.33,0.43,0,"estimate","Split from FAM-4 at the same total (Title I ~$0.08T, IDEA $0.20-0.30T); unscored","0",13,70,"2029-10"),
 ("EDU-3","—","Universal free school meals and Summer EBT at $60 a month, at current reimbursement rates, indexed","Education","domain-education.md","R2","General fund",0.22,0.27,0.33,0,"estimate","New Oct 20. Session estimate +$22B a year over current (2026 dollars, at the Senate's 2026 rates), grown to 2030-39; unscored","0",11,85,"2029-10"),
 ("EDU-4","—","Educator pipeline surge: teacher residencies (~50,000 a year), registered teaching apprenticeships, Grow Your Own; front-loaded for special education, bilingual and early childhood","Education","domain-education.md","R2","General fund",0.02,0.03,0.05,0,"estimate","New Oct 20; time-limited surge 2030-36 that tapers; supplies FAM-2's pre-K hiring (design rule 5)","0",14,60,"2029-10"),
 ("EDU-5","F4","Higher education: Pell maximum to $9,500, indexed, increment mandatory; SAVE-style income-driven repayment and PSLF fixes in statute","Education","domain-education.md","R2","General fund",0.20,0.32,0.42,0,"estimate","Split from FAM-4 at the same total (Pell $0.12-0.17T, SAVE/PSLF $0.10-0.30T); unscored","0",13,60,"2029-10"),
 ("EDU-7","—","Repeal the federal tax-credit scholarship (P.L. 119-21 sec. 70411) prospectively","Education","domain-education.md","R2","General fund",-0.06,-0.04,-0.02,0,"estimate","New Oct 20; revenue gain shown as a saving; no JCT figure found; depends on state opt-in","0",3,70,"2029-10"),
 ("EDU-8","—","AI in education, student data and education research: AI literacy and educator grants, student data-breach portal and edtech risk framework, NEED Act research center and IES (EDU-8, EDU-10)","Education","domain-education.md","APPROPS","General fund",0.01,0.015,0.025,0,"estimate","New Oct 20; Bonamici AI bill Titles I, III (education parts) and V plus the omnibus's research center; rules ride AI-1","0",24,45,"2029-12"),
 # ---- Social Security (domain-social-security.md) ----
 ("SS-1","F5","Social Security: solvency first, targeted increase (D8 baseline, SS-1 to SS-4)","Retirement","domain-social-security.md","FLOOR","Social Security trust fund",0.15,0.25,0.35,3.0,"estimate","Revenue $1.9T ($250K, scaled CBO) + ~$1.1T (investment income, estimate) less OX; 75-yr: closes ~65-72% of the 4.42% gap","8",12,92,"2030-06"),
 # ---- Climate (domain-climate.md) ----
 ("CLI-1","E1","Clean-energy credits restored (refundable, direct pay, point of sale; CEIC extended)","Climate","domain-climate.md","R2","General fund",0.6,0.9,1.1,0,"scaled","CRFB $571B (2025-34) scaled to ~$0.70T plus ~$0.2T of expansions; may overlap CLI-5 by up to ~$0.2T (open)","0",12,56,"2029-10"),
 ("CLI-2","E2","Climate Dividend: delivery of REV-C1 (80% per person, quarterly, paid before the fee reaches prices)","Climate","domain-climate.md; domain-revenue.md (REV-C1)","R2","Carbon fee",0.96,1.08,1.20,1.35,"estimate","Fee $1.20-1.50T on the durability path ($25 rising to ~$100 by 2037, chosen Oct 20), after the REV-C2 carve-out; outlay shown is the 80% dividend; the 20% transition share (~$0.27T) is credited to CLI-5","0",6,56,"2029-10"),
 ("CLI-3","E3","Clean Energy Standard in statute plus AAJA fixes (Sec. 1401 override, Judgment Fund cap, 401 and rail fixes); carries CLI-4 Clean Air Act restoration","Climate","domain-climate.md","FLOOR","General fund",0.0,0.02,0.06,0,"estimate","CLI-4 rides at no extra days; not Byrd-eligible","6",36,56,"2030-01"),
 ("CLI-5","E4","Thriving Economy add-ons (transmission ITC for plan-selected lines, 45X, resilience credit, LIHEAP/WAP/LIHWAP, ag R&D, minerals, adaptation)","Climate","domain-climate.md; domain-revenue.md (REV-C2)","R3","Carbon border adjustment",0.3,0.6,1.0,0.45,"estimate","Financed by REV-C1's 20% share (~$0.27T) plus REV-C2 (~$0.20T); residual to the general fund. CLI-5B (cut C29) sizes it to ~$0.47T; CLI-5F (cut C37, under the Oct 20 D4 reading) borrows for its ~$0.10T of capital lines instead","0",18,60,"2030-07"),
 ("CLI-6","E5","Grid and utility statute (transfer minimums, PBR standard, utility lobbying ban, RTO governance, large-load floor extension)","Climate","domain-climate.md","FLOOR","General fund",0.0,0.0,0.01,0,"estimate","Half of old E5's 8 days","4",36,50,"2030-05"),
 ("CLI-7","E5","Disaster response and flood insurance, with CLI-8 climate risk (cabinet FEMA, mitigation set-aside, NFIP with premium support, floodplain standard)","Climate","domain-climate.md","FLOOR","General fund",0.0,0.0,0.0,0,"estimate","UNSCORED: rough order $0.05-0.15T (premium support, set-aside), not in any total; 60-vote attempt in 2027-28 first","4",30,55,"2030-05"),
 # ---- Housing (domain-housing.md) ----
 ("HOU-1","E6","Housing reconciliation title: emergency aid, tax credits, construction capital (state revolving funds + $300B direct loans), 400,000 vouchers, public housing repair, supply fund, social housing pilot (HOU-1 to HOU-6 fund, HOU-8)","Housing","domain-housing.md","R2","General fund",0.34,0.47,0.62,0,"estimate","HOU-3C decided Oct 19: direct loans at subsidy cost; HOU-2 sized for the first time","0",18,60,"2029-10"),
 ("HOU-7","E6","Housing floor bill: zoning conditions on new transportation and CDBG money (HOU-6), institutional-investor limit made permanent (HOU-7)","Housing","domain-housing.md","FLOOR","None",0,0,0,0,"estimate","Conditions on new money only (NFIB)","3",36,50,"2030-03"),
 # ---- Labor (domain-labor.md) ----
 ("LAB-1","E7","Labor bill: PRO Act core, enforcement after Slaughter, sectoral boards, living wage mandate, heat standard, wage theft (LAB-1 to LAB-4, LAB-6, LAB-7)","Labor","domain-labor.md","FLOOR","None",0,0,0.01,0,"estimate","LAB-4's indirect budget effects unscored; E8's mandate merged here (C23)","8",30,47,"2030-03"),
 ("LAB-5","E8","Small-business wage transition credit (pays out only once LAB-4 is law)","Labor","domain-labor.md","R2","General fund",0.05,0.1,0.15,0,"estimate","Split from E8; contingent effective date","0",9,87,"2029-10"),
 ("LAB-8","—","Registered apprenticeships for construction, energy and care","Labor","domain-labor.md","R2","General fund",0.02,0.03,0.05,0,"estimate","New row: three files named apprenticeships unsized","0",12,70,"2029-10"),
 ("LAB-9","—","National service: universal paid service year with an education award, cross-regional and cross-class placement in statute","Labor","domain-labor.md","R2","General fund",0.06,0.12,0.2,0,"estimate","New permanent program (moved from DEM-15, Oct 19); ~$35K a slot, ramp to 250,000 new slots; needs a pay-for and a Byrd check","0",12,72,"2029-10"),
 # ---- Competition (domain-competition.md) ----
 ("COM-1","E9","Competition bill: merger law, enforcers and HSR fees, platforms, non-compete ban, junk fees, CFPB durability (COM-1 to COM-6; E10 merged, C24)","Competition","domain-competition.md","FLOOR","Merger review",0.004,0.004,0.02,0.004,"estimate","HSR fee increase ~$0.004T, kept by the enforcers (sized for the first time); COM-6 remittance effect up to $0.01T","5",24,50,"2030-03"),
 # ---- Immigration (domain-immigration.md) ----
 ("IMM-1","E11","Immigration bill: tiered legalization, backlogs and H-1B fee, asylum processing, enforcement priorities and detention cap, birthright codification, USCIS delivery (IMM-1 to IMM-6)","Immigration","domain-immigration.md","FLOOR","General fund",-0.25,-0.14,-0.02,0,"estimate","S.744 CBO pattern (~$175B first decade), not rescored; IMM-3 adds ~$0.01T; score with CRT-5. Must pass in the first trifecta","12",12,82,"2029-09"),
 # ---- AI and information (domain-ai.md) ----
 ("AI-1","E12","AI bill: frontier transparency, floor preemption, pre-deployment evaluation, government use, platform transparency, public media and FOIA (AI-1 to AI-3, AI-5, AI-7, AI-10); carries EDU-8's education rules","AI","domain-ai.md","FLOOR","General fund",0.0,0.02,0.06,0,"estimate","Must pass in the first trifecta (cut C13 superseded); AI-8 rides DEM-1; EDU-8's rules (student data, edtech procurement limits) ride as a title at no extra days","5",24,50,"2030-05"),
 ("AI-4","E12","AI and work: displacement-triggered wage insurance and training accounts","AI","domain-ai.md","R3","General fund",0.1,0.2,0.4,0,"estimate","E12's $0.20T; benefit can ride R3 (Byrd unchecked); AI-6 levy is the natural pay-for once scored","0",24,60,"2030-07"),
 ("AI-9","—","Local journalism payroll credit conditioned on ownership, plus a conversion fund","AI","domain-ai.md","R2","General fund",0.01,0.02,0.04,0,"estimate","Instruments #12; Byrd-eligible if a pure credit (unchecked)","0",12,60,"2029-10"),
 # ---- Democracy and civic life (domain-democracy.md) ----
 ("D2-RULES","DEM0","Senate rules reform (D2 open: seven options)","Democracy","Senate Rules Reform: Options","FLOOR","None",0,0,0,0,"estimate","Enabling vote","4",0,40,"2029-01"),
 ("DEM-1","DEM1","Electoral and civil-rights package: Freedom to Vote floor, John Lewis VRAA, Callais response, 6:1 match (INT-5B), DISCLOSE (INT-2); carries DEM-2, DEM-12, DEM-13","Democracy","domain-democracy.md; domain-integrity.md","FLOOR","General fund",0,0.01,0.04,0,"estimate","Must pass by mid-2030 (D1). DEM-1F adopted Oct 20: floor after R1 is signed, enacted by spring 2030. DEM-1E (registration at benefit-delivery points) adopted into Title I. Proposed riders not yet adopted: SAF-8's election-worker half, AI-8","10",21,55,"2029-07"),
 ("DEM-5","DEM3","D.C. statehood","Democracy","domain-democracy.md","FLOOR","None",0,0,0,0,"estimate","AMD-6 (23rd repeal) is hygiene","5",16,95,"2029-03"),
 ("DEM-6","DEM4","Puerto Rico Status Act (with DEM-7 territorial and tribal representation)","Democracy","domain-democracy.md","FLOOR","None",0,0,0.01,0,"estimate","Statehood's fiscal effect unscored","3",20,88,"2029-03"),
 ("DEM-11","—","Election administration funding: permanent indexed formula line","Democracy","domain-democracy.md","APPROPS","General fund",0.01,0.02,0.04,0,"estimate","Unsourced; mandatory if Byrd-eligible (unchecked)","0",12,60,"2029-12"),
 ("DEM-16","—","Civic education grants tied to participation outcomes","Democracy","domain-democracy.md","APPROPS","General fund",0.0,0.01,0.02,0,"estimate","Batch 4 follow-up (staging 15.2)","0",24,55,"2029-12"),
 ("DEM-17","—","Public space, libraries and community infrastructure capital fund (time-limited)","Democracy","domain-democracy.md","R3","General fund",0.02,0.03,0.05,0,"estimate","Time-limited capital: borrowing allowed under D4 (option C32)","0",24,65,"2030-07"),
 ("DEM-3","DEM10","House enlargement (cube-root rule, ~692 seats); second-term package with DEM-4 and DEM-9","Democracy","domain-democracy.md","T2","General fund",0,0.01,0.02,0,"estimate","Run on it in 2032, enact 2033, one-off 2034 redraw; chamber capital unscored","4",46,80,"2033-03"),
 ("DEM-4","DEM11","Fair Representation Act (STV) with the presidential method (DEM-9, amendment vehicle AMD-3); second-term package","Democracy","domain-democracy.md","T2","None",0,0,0,0,"estimate","Section 2 modeling rerun first (C14); fallback DEM-4C or 4D still to choose","5",46,60,"2033-03"),
 # ---- Integrity (domain-integrity.md) ----
 ("INT-1","DEM5","[Fast track C27] Government ethics and anti-corruption (stock ban, divestiture, IGs; INT-1, INT-3, INT-4, INT-6)","Integrity","domain-integrity.md","FLOOR","None",0,0,0,0,"estimate","Packaged with CAP-1 and CAP-14","1",6,58,"2029-05"),
 # ---- Courts (domain-courts.md) ----
 ("CRT-P1","DEM7","Courts package: term limits, phased judgeships, random assignment, ethics (DEM6 merged, C11)","Courts","domain-courts.md","FLOOR","General fund",0,0.01,0.02,0,"estimate","CRT-5 (Article I immigration court, ~$0.03T) unscored; score with IMM-1","6",12,50,"2029-07"),
 # ---- Executive power (domain-executive-power.md) ----
 ("EXE-1","DEM8","Executive-power guardrails: emergencies, impoundment, Insurrection Act, pardons, tariffs, war powers (DEM9 merged, C10)","Executive power","domain-executive-power.md","FLOOR","None",0,0,0,0,"estimate","EXE-14B tariff claim ($1.5-1.9T) unscored; Iran architecture to re-scope against the June 15, 2026 agreement","6",3,50,"2029-05"),
 # ---- Capacity (domain-capacity.md) ----
 ("CAP-8","DEM13","[Fast track C27] Civil service modernization, successor agencies and congressional capacity (CAP-1 to CAP-6, CAP-8 to CAP-12, CAP-14, CAP-15; DEM12 merged, C26); proposed to carry EDU-6's Education Department protections","Capacity","domain-capacity.md","FLOOR","General fund",0.02,0.04,0.07,0,"estimate","Congressional capacity ($0.03T) plus civil service ($0.01T); staffing money sits in CAP-7. EDU-6 (bar on moving ED functions by interagency agreement) proposed to ride, pending Espen","2",12,57,"2029-06"),
 ("CAP-7","A1","Sustained capacity increase with staffing floors: a permanent addition to the D9 agencies' funding, about 0.12% of GDP from FY2032 (restructured Oct 20, Decision Brief 2)","Capacity","domain-capacity.md; Governing Decisions D9","APPROPS","General fund",0.40,0.49,0.60,0,"estimate","Restructured Oct 20 (Espen): the even ten-year line becomes a front-loaded surge (CAP-7S) plus this lasting increase, lower than the surge. ~$15B in 2030, ~$50B by 2033, ~$65B in 2040 (0.12% of GDP, estimate; 0.10% and 0.148% are the alternatives). Per-agency split pro rata to CAP-7's table","0",12,40,"2029-12"),
 ("CAP-7S","A1","Agency rebuild surge: the ~$0.6T rebuild line front-loaded into 2030-35 (hiring backlog, training, systems and facilities), time-limited (Decision Brief 2)","Capacity","domain-capacity.md; Governing Decisions D9","APPROPS","General fund",0.45,0.60,0.75,0,"estimate","Reallocated Oct 20 (Espen) from an even ten-year spread: ~$70B, $120B, $130B, $120B, $100B, $60B over FY2030-35, then zero (estimate). Time-limited, so borrowing-eligible inside the D4-B envelope (C42). Batch 4 proposes $31B of the $37B reserve, pending Espen. Absorption is the risk: CAP-11's hiring reform gates it","0",12,40,"2029-12"),
 # ---- National security (domain-national-security.md) ----
 ("NSC-1","A2","Defense roughly flat in real terms from an FY2029 base excluding one-time reconciliation money","National security","domain-national-security.md; Governing Decisions D9","APPROPS","General fund",0.0,0.0,0.3,0,"estimate","High end = a one-time +3.2% level increase; base definition is Espen's call (NSC-1A/B/C)","0",12,40,"2029-12"),
 ("NSC-8","—","Pandemic preparedness and biodefense: BARDA and CDC preparedness lines; WHO withdrawal by act of Congress only","National security","domain-national-security.md","APPROPS","General fund",0.01,0.02,0.03,0,"estimate","Gives CAP-7's $15B CDC placeholder its named work","0",12,55,"2029-12"),
 ("NSC-10","F6","Veterans health and capacity (12,000 clinicians, claims, rural care)","National security","domain-national-security.md","R2","General fund",0.04,0.07,0.12,0,"estimate","Bill Book 26; moved from the family rows","0",10,90,"2029-10"),
 # ---- Rights (domain-rights.md) ----
 ("RTS-1","S1","Reproductive Freedom Act (statutory right, medication abortion floor, contraception, IVF, travel, EMTALA); RTS-2 riders via appropriations","Rights","domain-rights.md","FLOOR","None",0,0,0.01,0,"estimate","RTS-2 Hyde riders ~0-0.01","4",3,38,"2029-04"),
 ("RTS-3","S2","Equality Act with civil-rights enforcement restoration (RTS-3, RTS-4)","Rights","domain-rights.md","FLOOR","None",0,0,0.01,0,"estimate","Athletics provision is Espen's call (RTS-3A vs 3B)","3",3,65,"2029-06"),
 # ---- Public safety (domain-public-safety.md) ----
 ("SAF-1","S3","Safe Everywhere Act (rules): clearance, standards and liability, background checks, pretrial, public-servant protection, fraud duties, sentencing and cannabis (SAF-1, 2, 5, 7-9 rules, SAF-11; S4 merged, C25)","Public safety","domain-public-safety.md","FLOOR","None",0,0,0.01,0,"estimate","Bill Books 16 and 24 folded in","6",8,70,"2029-11"),
 ("SAF-10","S5","Safety Compacts and the Safe Everywhere funding titles, as mandatory spending (SAF-10A)","Public safety","domain-public-safety.md; sources/public-safety-safe-everywhere-bill-summary.md","R3","Public safety",0.11,0.122,0.14,0.09,"proposal","$12.1B a year by title plus $0.8B one-time; moved from APPROPS to R3 (Byrd unchecked). Own revenue is durable sources only (~$9.2B a year)","0",12,65,"2030-07"),
 # ---- Transportation (transportation-moving-america-act-2031-draft-2.md, canonical until converted) ----
 ("MOV-29","M1","Moving America: 2029 reconciliation act (fuel-tax steps, clean-vehicle charge, rail and transit package one, FY2032-35 renewal top-ups)","Transportation","transportation-moving-america-act-2031-draft-2.md","R1","General fund top-ups; trust-fund revenue",0.25674,0.25674,0.25674,0.290,"sourced","$47.0B package + $209.74B top-ups; revenue $290.0B net (FY2029-38); project estimates","0",6,75,"2029-05"),
 ("MOV-30","M2","Moving America: 2030 reconciliation act (weight-distance charge, rail diesel, aviation surcharge, package two, FY2035-36 top-ups)","Transportation","transportation-moving-america-act-2031-draft-2.md","R3","General fund top-ups; trust-fund revenue",0.09083,0.09083,0.09083,0.095,"sourced","$33.5B package + $57.33B top-ups; revenue $95.0B net (FY2030-39); rescore on FY2031-40","0",6,70,"2030-07"),
 ("MOV-31","L1","Moving America Act of 2031 (authorization)","Transportation","transportation-moving-america-act-2031-draft-2.md","LATER","General fund",0.1247,0.1247,0.1747,0,"sourced","$123.70B expansion and ~$1B div. E from the general fund, FY2032-36","0",30,70,"2031-09"),
]

REV = [
 # id, option, channel, lo, mid, hi, in_base, legal risk, overlap note, source, reaches_middle
 ("G1","Corporate rate 21% to 28%","General fund",1.6,1.65,1.75,True,"Low","","Go-big tab (Treasury; CBO $135.7B per point)",False),
 ("H1a","Extend the 3.8% investment-income tax to active pass-through income, credited to HI","Medicare HI",0.5,0.5,0.5,False,"Low","With HI's ~$0.7T share of HLT-6 MA savings, covers HI's ~$0.8-0.9T need (est.)","Revenue tab (CBO $440B 2026-35)",False),
 ("H1b","Medicare and investment-income tax rates to 5% above $400K","General fund",0.5,0.5,0.5,True,"Low","Stacks with SS-1/SS-2 (top rates ~57% federal)","Revenue tab (Treasury via CRFB $412B 2025-34)",False),
 ("G3","Top rate back to 39.6% above $400K","General fund",0.3,0.3,0.3,True,"Low","Overlaps G9","Go-big tab (Treasury)",False),
 ("G4","25% minimum tax on households over $100M (replaced by G11, Oct 19)","General fund",0.55,0.58,0.6,False,"High (Moore)","Overlaps G6","Go-big tab (Treasury)",False),
 ("G11","Full mark-to-market for billionaires (Wyden design); replaces G4 in the base (C22)","General fund",0.55,0.65,0.8,True,"Medium-High (realization; deferral-charge fallback)","Replaces G4; trims G6","JCT $557B 2022-31 (preliminary), my 2030-39 estimate",False),
 ("G5","Buyback tax to 4%; corporate minimum to 21%","General fund",0.4,0.4,0.4,True,"Low","","Go-big tab (Treasury)",False),
 ("G6","Tax capital gains at death above an exemption","General fund",0.7,0.7,0.7,True,"Medium","Overlaps G4; the education trust-fund design's stepped-up-basis piece is this row, not new revenue","Revenue tab (CBO)",False),
 ("G7","Tax foreign income at the full corporate rate","General fund",0.41,0.41,0.41,True,"Low","","Revenue tab (CBO)",False),
 ("G8","IRS enforcement restored","General fund",0.2,0.4,0.6,True,"Low","CBO may not score it on a given vehicle; whether it is net of the IRS allocation in CAP-7 is unchecked","Revenue tab",False),
 ("G9","Reverse 2025 tax cuts above $450K (net of the 39.6% row)","General fund",1.2,1.45,1.7,True,"Low","Overlaps G3. Includes reversing most of the 2025 law's permanent $15M estate exemption (~$0.2-0.3T, scaled from JCT via ACTEC); E1 counts only the increment beyond it","Go-big tab (TPC via Deseret), less G3",False),
 ("G10","Financial transaction tax at 0.01%","General fund",0.4,0.4,0.4,True,"Low","","Revenue tab (CBO)",False),
 ("GX","Overlap and avoidance adjustment for stacked high-income options (15% of G11, G6, G9 and H1b)","General fund",-0.555,-0.495,-0.4425,True,"","My estimate (audit finding 4)","Revenue tab caution: options overlap",False),
 ("E1","Restore the estate tax at 2009 parameters ($3.5M exemption, 45%), exemption frozen in nominal terms, counted as the increment beyond G9 (REV-E1; option C35)","General fund",0.05,0.15,0.25,False,"Low","Increment beyond G9, which already takes the exemption back to ~$7M (restated Oct 20); gross vs current law ~$0.35T. Stacks with G6 (gains at death); dedicated to education only under EDU-9B","Estimate: education trust-fund session ($30-50B a year with step-up repeal) less G6's step-up piece and G9's estate piece",False),
 ("C1","Carbon fee at $25/ton in 2030 rising to ~$100 by 2037 (durability path, chosen Oct 20), gasoline and diesel exempt, domestic fee only (D7, REV-C1A)","Carbon fee",1.20,1.35,1.50,False,"Low","80% ($1.08T) to the dividend (CLI-2); 20% ($0.27T) to CLI-5. Options: REV-C1B (old $50 + 5% path, $1.25T), C1C (escalator), C1D (road-fuel convergence, open, not adopted), C1E (gasoline phase-in, conflicts with D7), C1F (Talarico path)","Durability session ~$1.8T economy-wide less gasoline (~$0.27T) and REV-C2 (estimate)",True),
 ("C2","Carbon border adjustment on imports, with export rebates (REV-C2)","Carbon border adjustment",0.15,0.20,0.25,False,"Medium (trade law)","Finances CLI-5; includes methane and industrial fees. REV-C2B (clean product standard) is a regulatory option with no revenue","Thriving Economy map (combined figure), estimate",True),
 ("PS1","Safe Everywhere revenue title, durable sources: alcohol at $16/proof gallon (~$7B/yr), fraud-prevention assessment ($1.2B), firearms excise doubled (~$0.6B), $10 background-check fee (~$0.3B), kiosk and data-broker fees (~$0.1B)","Public safety",0.08,0.09,0.10,False,"Low-Medium (firearms charges after Bruen)","Deployment savings (~$1.1B/yr) dropped: double count against flat defense. CVF False Claims receipts (~$0.75B/yr) dropped: general-fund money moved, not raised. Alcohol enters the D3 test; SAF-R2 swaps it for top-end revenue","Bill summary (proposals); alcohol scaled from CBO 2016 option ($70B/10 yrs)",True),
 ("PS2","Cannabis excise receipts if legalization passes separately (SAF Sec. 1209, contingent)","Cannabis excise (contingent)",0.008,0.02,0.053,False,"Low","Not in any total; would close SAF-10's residual at the middle case","Bill summary: CBO MORE Act score (low), author's middle, Tax Foundation 2016 (high)",True),
 ("MF1","HSR merger-filing fee increase, kept by the FTC and DOJ Antitrust (COM-2)","Merger review",0.004,0.004,0.004,False,"Low","Funds an equal enforcement increase; nets to zero","domain-competition.md (estimate)",False),
 ("IF1","Statutory H-1B fee retained by USCIS and a training fund (IMM-2)","Immigration fees",0.01,0.015,0.02,False,"Low","Spent within receipts on adjudication and training; employers, not households","domain-immigration.md (estimate)",False),
 ("AI6","AI revenue instrument: compute levy or token-consumption tax, rebated (AI-6, held)","AI levy (held)",0,0,0,False,"Low","Unscored and held; the natural pay-for for AI-4 if the rebate is under 100%","domain-ai.md; Instruments #11",True),
 ("ED1","Education contribution: 1.28-1.4 points of an uncapped payroll contribution dedicated to an education fund (EDU-9B, held; not chosen)","Education fund (proposed)",1.95,2.10,2.30,False,"Low","Reaches every worker (~$830-900 a year at the median wage if all on the worker); needs D3 and D4 decisions; would move ~$1.2T of general-fund claims (FAM-2, EDU-1, EDU-3, EDU-4) into the fund","Education trust-fund session: ~$135B per point in 2030 growing 4%; CRFB ~$1.3T per point 2026-35",True),
 ("SC1","45% bracket on income above $5M (Talarico scenario; held in reserve as the first fallback if TS12 scores low, Decision Brief 2)","General fund",0.1,0.18,0.25,False,"Low","Stacks with G3/G9; inside GX's logic","Scenario figure (Talarico model), not a score",False),
 ("SC2","Pass-through and deferred-compensation reform (Talarico scenario)","General fund",0.2,0.35,0.45,False,"Low","Overlaps H1a and SS-5 on the same pass-through base","Scenario figure (Talarico model), not a score",False),
 ("SC3","Crop insurance reform (Talarico scenario; the fossil piece moved to TS3, Oct 20)","General fund",0.03,0.05,0.10,False,"Low","Farm-state cost; pairs with CLI-13's conditioned payments","Scenario figure (Talarico model, $0.20T with fossil repeal), not a score",False),
 ("TS1","Sec. 162(m) $1M pay-deduction limit for every employee of every C corporation (REV-TS1, sprint, accepted in principle Oct 20)","General fund",0.25,0.34,0.40,False,"Low","Interacts with G1","Treasury FY2025 Green Book via ITEP ($272B 2025-34), scaled",False),
 ("TS2","Repeal the foreign-derived deduction, FDII/FDDEI, for C corporations above the sec. 448(c) small-business receipts test (REV-TS2, sprint; full repeal is REV-TS2A, +$0.01T)","General fund",0.11,0.19,0.29,False,"Low (trade-law positive)","2025 law changed FDII; needs a fresh score","Green Book via ITEP ($158B), scaled",False),
 ("TS3","End fossil-fuel tax preferences, the dual-capacity rules and the foreign oil and gas income rules (REV-TS3, sprint, accepted in principle Oct 20; takes SC3's fossil piece)","General fund",0.09,0.13,0.17,False,"Low","Margin overlap with REV-C2; the carbon fee shrinks the domestic base late in the window","Treasury FY2025 Green Book table: $35.3B domestic + $71.6B dual capacity + $3.4B foreign oil and gas = $110.2B (2025-34), scaled to 2030-39",False),
 ("TS4","Limit multinationals' excess interest deductions (REV-TS4, sprint)","General fund",0.03,0.05,0.07,False,"Low","","Green Book via ITEP ($40B), scaled",False),
 ("TS5","Close tax-free spin-off abuses (REV-TS5, sprint)","General fund",0.03,0.05,0.06,False,"Low","","Green Book via ITEP ($44B), scaled",False),
 ("TS6","Trust and GRAT reforms (REV-TS6, sprint)","General fund",0.07,0.10,0.12,False,"Low","Overlaps E1 and G9's estate piece (20% haircut applied)","Green Book via ITEP ($97B), scaled",False),
 ("TS7","Limit very large retirement balances for high earners (REV-TS7, sprint)","General fund",0.03,0.03,0.03,False,"Low","","Green Book via ITEP ($24B), scaled",False),
 ("TS8","Stop partnership basis shifting (REV-TS8, sprint)","General fund",0.02,0.02,0.02,False,"Low","","Green Book via ITEP ($15B), scaled",False),
 ("TS9","Limit like-kind exchange deferral to $500K of gain (REV-TS9, sprint)","General fund",0.025,0.025,0.025,False,"Low","","Green Book via ITEP ($20B), scaled",False),
 ("TS10","Tax carried interest as ordinary income (REV-TS10, sprint)","General fund",0.02,0.02,0.02,False,"Low","Mostly reached already by C18 and G9","CBO via CRFB ($15B, 2026-35)",False),
 ("TS11","Wash-sale rules for digital assets (REV-TS11, sprint)","General fund",0.03,0.03,0.03,False,"Low","","Green Book via ITEP ($26B), scaled",False),
 ("TSX","Sprint overlap, avoidance and post-2025-law baseline haircut (10% of TS1-TS11)","General fund",-0.10,-0.10,-0.10,False,"","Estimate","Estimate",False),
 ("TS12","Cap itemized deductions' value at 28% above $450K (REV-TS12; accepted Oct 20, Decision Brief 2, as option C39)","General fund",0.25,0.40,0.55,False,"Low","Overlaps G3, G9, C18, SALT; the 2025 law already caps the value at 35% for the top bracket; needs a joint score","Estimate; no current score",False),
 ("HP1","CEO-to-median-worker pay-ratio surtax on corporations with receipts over $100M: +0.5 points above 50:1 rising to +5 above 500:1, contract and franchise workers counted in the median (REV-HP1; accepted Oct 20, Decision Brief 2, as option C40)","General fund",0.04,0.08,0.15,False,"Low","Stacks on G1","Sponsor estimate $150B/10 yrs (Tax Excessive CEO Pay Act FAQ, 2025), unscored; haircut ~50%",False),
 ("HP2","Limit the corporate deduction for stock options to the book expense (REV-HP2; folded into REV-TS1's drafting, Decision Brief 2)","General fund",0.01,0.02,0.04,False,"Low","Largely overlaps TS1 for pay above $1M; not counted separately","JCT $25B (2012-21, Levin-Brown), scaled and net of TS1",False),
 ("HP3","21% excise on public-company pay above $1M to the five highest-paid officers, extending sec. 4960, pay defined as in 162(m) (REV-HP3; accepted Oct 20, Decision Brief 2, as option C41)","General fund",0.03,0.06,0.10,False,"Low","On top of TS1's deduction denial; behavioral response large","Estimate (about 7,500 officers at S&P 1500 firms; proposal)",False),
 ("W1","1% payroll contribution, no cap","General fund",1.6,1.6,1.6,False,"Low","Allowed under D3 only if the net test passes. ED1 is the same base dedicated to education","Revenue tab (CBO)",True),
 ("W2","Cap the employer health exclusion at the median premium","General fund",1.1,1.25,1.4,False,"Low","Overlaps hospital price cap","Revenue tab (CBO)",True),
 ("W3","5% value-added tax, narrow base","General fund",2.8,2.8,2.8,False,"Low","Regressive without a rebate","Revenue tab (CBO)",True),
 ("W4","1-point surtax on income above $100K/$200K","General fund",0.67,0.67,0.67,False,"Low","","Revenue tab (CBO)",True),
 ("T1","Keep current tariffs (Section 232 and 301, post-Learning Resources)","General fund",0.0,0.0,0.0,False,"Medium (301 challenges)","In CBO's baseline: no new revenue. Repeal would be a new claim of ~$1.5-1.9T (est.)","CRFB (Jul 2026), Tax Foundation, Penn Wharton (Oct 2026)",True),
 ("O1","Social Security tax on earnings above $250K, with a benefit credit (SS-1)","Social Security trust fund",1.9,1.9,1.9,False,"Low","Cannot fund general-fund programs","Revenue tab (CBO via CRFB, no-credit design)",False),
 ("O2","12.4% Social Security tax on investment income above $400K (SS-2)","Social Security trust fund",0.9,1.1,1.4,False,"Low","Stacks with H1b (audit finding 4)","Estimate; SSA scored the $200K/$250K version at +1.93% of payroll (2023)",False),
 ("OX","Avoidance haircut on SS-2 (15%), matching GX on the same base","Social Security trust fund",-0.21,-0.165,-0.135,False,"","Audit finding 4","Estimate",False),
 ("P1","Paid-leave contribution, 0.6% split employer/employee, stepping toward 0.85% (FAM-3)","Paid-leave fund",0.85,0.9,1.28,False,"Low","High end is the 0.85% cap; above it a repayable Treasury loan bridges","Estimate: 0.6% of ~$15T a year of covered wages",True),
 ("MR1","Fuel taxes permanent and indexed, ten 3-cent Fix-It-First steps with a price pause (2029 act)","Surface transportation trust fund",0.3804,0.3804,0.3804,False,"Low","Upper bound: no demand response","Moving America Draft 2 (FY2029-38)",True),
 ("MR2","Clean-vehicle per-mile charge, cars and trucks (2029 act)","Surface transportation trust fund",0.0294,0.0294,0.0294,False,"Low","Odometer only","Moving America Draft 2",True),
 ("MR3","Zero-emission truck excise at 4%; EV fee ended after FY2030 (2029 act)","Surface transportation trust fund",-0.0231,-0.0231,-0.0231,False,"Low","Revenue losses","Moving America Draft 2",False),
 ("MR4","Weight-distance charge replacing the heavy-vehicle use tax (2030 act)","Surface transportation trust fund",0.0534,0.0534,0.0534,False,"Low","Net of use-tax repeal","Moving America Draft 2 (FY2030-39)",False),
 ("MR5","Rail diesel tax and aviation segment surcharge (2030 act)","Surface transportation trust fund",0.0733,0.0733,0.0733,False,"Low","Rail account only","Moving America Draft 2 (FY2030-39)",True),
 ("MR6","Income and payroll tax offset on new excises (25%)","Surface transportation trust fund",-0.1284,-0.1284,-0.1284,False,"","Scoring convention","Moving America Draft 2",False),
]

CONFLICTS = [
 # resolved in earlier rebuilds (kept as the record; legacy IDs in parentheses where they appear)
 ("Revenue envelope","The Governing Agenda says ~$4.6T funds the whole program","That $4.6T counts Social Security cap revenue, which can only go to its trust fund","Resolved (D4): revenue is counted by channel"),
 ("Health design","War game: public option plus Medicare at 55","Go-big tab: public option plus Medicare at 60","Resolved (D6): go-big bill canonical; buy-in a scored add-on"),
 ("Medicare tax revenue","Go-big Package A spends Medicare and investment-income taxes on new benefits","Revenue tab names the same taxes as HI's fix","Resolved (D4): H1a plus HI's MA share keep HI whole; H1b in the general-fund base"),
 ("Social Security","Bill Book: lifting the cap funds an expansion","Revenue tab: that alone closes about half the gap","Resolved (D8): solvency first; closer still to choose (SS-5 recommended)"),
 ("Carbon revenue","Bill Book: fee returned as a dividend","Thriving Economy: carbon revenue for programs","Resolved (D7): 80% dividend (CLI-2), 20% transition (CLI-5)"),
 ("Reconciliation slots","War game: two packages","Radical Means: a third slot exists","Resolved (D5): three vehicles with a fallback"),
 ("Pay-for pairing","Package A pairs the Child Tax Credit with the billionaire minimum tax","Nineteen Months rates that tax the least durable item","Open: pair the most durable benefit with the most durable revenue (corporate rate)"),
 ("Floor time","Inventory: ~148 discretionary floor days","First-Congress statutory items exceed the budget","Open: depends on D2 and the cut list"),
 ("2028 extension","Moving America needs a 60-vote extension by Sept 30, 2028","The Highway Trust Fund runs dry in 2028","Open: a 2027-28 priority; size the transfer now"),
 ("Permitting law and the general fund","AAJA Secs. 1401-1402 pay damages from the Judgment Fund without appropriation","A fossil-permit action after 2029 could cost billions per project","Addressed in CLI-3 (damages cap); contingent cost remains until enacted"),
 ("Permitting law and passenger rail","AAJA's ESA exemption covers highway and transit, not FRA rail","Moving America's rail program gets less relief","Resolved in CLI-3 (rail fixes)"),
 ("Methane fees","domain-revenue.md lists methane fees as unsized financing beyond REV-C2","REV-C2's scaled figure already includes them","Open: not additional unless REV-C2 is re-sized"),
 ("Moving America financing","MOV-29 and MOV-30 are $0.35T of general-fund outlays","D4 allows borrowing only for time-limited capital","Resolved Oct 19 (C30 accepted)"),
 ("Investment-income stacking","GX haircut G11, G6 and G9 only","SS-2 and H1b stack unhaircut","Resolved Oct 19: 15% haircut on H1b (GX) and SS-2 (OX)"),
 ("DEM-4 and DEM-9","STV shipping into a plurality-president configuration","Instruments warns against it","Resolved Oct 19: one second-term package; fallback DEM-4C or 4D still to choose"),
 # new in the full rebuild (Oct 20)
 ("Row IDs","Ledger bill rows were H1-H6, F1-F6, E1-E12, DEM0-DEM13, S1-S5, A1-A2, M1-M2, L1","Domain files use HLT-, FAM-, CLI-, DEM-# and other IDs; DEM0-DEM13 collided with DEM-1 to DEM-20","Resolved Oct 20: every row is keyed by its domain-file ID; legacy IDs kept in a crosswalk column"),
 ("Clean-energy credit overlap","CLI-1 carries E1's $0.9T","The transmission ITC and 45X moved to CLI-5; E1 may have counted them","Open: CLI-1 may be overstated by up to ~$0.2T; check at rescore"),
 ("Disaster and flood insurance","CLI-7 is a first-Congress floor row","It is unscored (rough $0.05-0.15T)","Open: not in any total until scored"),
 ("Public-safety deployment savings","PS1 counted ending domestic deployments (~$1.1B/yr) as channel revenue","NSC-1 holds defense flat, so the savings stay inside defense","Resolved Oct 20 (domain-public-safety.md): dropped from PS1 unless NSC-1 is cut by the same amount"),
 ("Crime Victims Fund receipts","PS1's package counted False Claims Act receipts (~$0.75B/yr)","Those receipts otherwise reach the Treasury","Resolved Oct 20: counted as a general-fund cost, not channel revenue"),
 ("Safe Communities Trust Fund","SAF bill Sec. 1208 creates a trust fund for its receipts","D4 bars a trust fund just to hold a pay-for","Open (Espen's call): domain file recommends dropping it and funding SAF-10 as mandatory spending"),
 ("Public-safety vehicle","Ledger S5 was annual appropriations","SAF-10A makes the Compact stream mandatory in R3","Applied Oct 20 (the domain file's chosen design); Byrd check title by title still open"),
 ("Housing construction capital","Ledger E6 counted a $250B grant fund; C21 borrowed for it","HOU-3C (decided Oct 19) uses ~$72B of grants plus $300B of direct loans at subsidy cost","Resolved: HOU-1 row at $0.47T mid; C21 shrinks to ~$0.06T"),
 ("AI timing","Cut C13 would move AI governance to 2031","Espen's Oct 19 call: E12 must pass in the first trifecta","Resolved: C13 superseded; AI-1 and AI-4 stay first-Congress"),
 ("National service","Staging 15.1 had no ledger row","LAB-9 is a new permanent program (~$0.12T)","Resolved Oct 20 (Decision Brief 2): LAB-9D (bipartisan authorization first, LAB-9A's R2 money as fallback); paid for at maturity under D4-B; score and Byrd check still open"),
 ("D9 agency list, batch 4","CAP-7's reserve held $37B for batch 4","Batch 4 files propose $31B (USCIS asylum, civil-rights offices, CAISI, ATF/NICS, State)","Open: pending Espen; live D9 list still to extend"),
 ("Immigration court and immigration bill","CRT-5 (~$0.03T) is unscored","IMM-1 relies on it","Open: score the two together"),
 ("NDAA floor time","Most NSC rows ride the annual NDAA","The 163-day budget does not list the NDAA","Open: decide whether the budget already accounts for it"),
 ("Safe Everywhere file role","domains/public-safety-safe-everywhere.md was canonical until converted","domain-public-safety.md now governs","Open housekeeping: move it to sources/ (content unchanged)"),
 # new in the education batch and the Oct 20 reviews
 ("Education's home","FAM-4 held education inside the family file","Education was the framework's blind spot (Espen, Oct 20)","Resolved Oct 20: domains/domain-education.md (EDU-1 to EDU-10); FAM-4 is a pointer; legacy F4 maps to EDU-1 and EDU-5 at the same total"),
 ("Two pre-K designs","FAM-2: universal pre-K, phased, inside child care","Bonamici omnibus: universal pre-K through HHS, 1,020 hours, pay parity, BA in 7 years, 100% federal share stepping to 60%","Folded Oct 20: FAM-2 stays the home; the omnibus standards are FAM-2D (option); EDU-9B would move FAM-2's financing into an education fund"),
 ("Education trust fund and D4","EDU-9B: an uncapped 1.28-1.4 point payroll contribution plus the estate tax in a dedicated education fund","D4: no new trust fund just to hold a pay-for; a trust fund only where a permanent benefit has a natural revenue stream","Deferred (Espen, Oct 20) to a revenue strategy session on payroll raisers: the payroll piece is arguable on the FAM-3 pattern; dedicating the estate tax fails the rule as written"),
 ("Education trust fund and D3","EDU-9B's contribution reaches every worker (~$830-900 a year at the median wage)","D3: every group below the top must come out ahead; middle-reaching options go through the incidence model","Tested Oct 20 (incidence v1.3, scenario G): see the incidence doc; a decision, not a default"),
 ("Estate tax and G6","The education session's estate component includes ending stepped-up basis","REV-G6 (gains at death, $0.70T) is already in the base","Resolved Oct 20: REV-E1 is the estate tax alone; the step-up piece is G6 and is not counted twice"),
 ("Estate tax and G9","REV-E1/C35 was counted at ~$0.35T against current law","G9's reversal of 2025 relief above $450K already includes most of the permanent $15M estate exemption (~$0.2-0.3T)","Resolved Oct 20: E1/C35 restated as the increment beyond G9 (~$0.15T); G9's note says so; never sum the gross figures"),
 ("Payroll raisers","Seven payroll-type raisers sit in different files (REV-P1, REV-ED1, W1, SS-7, SS-1, SS-2, REV-H1a)","W1 and REV-ED1 are the same base; SS-7 and the leave step-up stack on every worker","Open (Espen, Oct 20): revisit EDU-9B's structure with the other payroll raisers in a later revenue strategy session; listed in domain-revenue.md under REV-ED1"),
 ("Payment continuity","Recurring payments could stop in a shutdown","Talarico model: standing disbursement authority made a shutdown fail","Resolved Oct 20: adopted as a design rule; statute EXE-18 (auto-CR at CAP-4; debt limit EXE-18C, option)"),
 ("Universal meals","No ledger row carried school meals","Both education sources and the Talarico scenario lead with universal meals","Added Oct 20 as EDU-3 ($0.27T, chosen); EDU-3B (community eligibility expansion) is the smaller option (C36)"),
 ("Climate durability package and D4","The durability session's expanded plan is ~$2.5T gross, ~$1.8-1.9T net, largely unpaid","D4: permanent programs fully paid for; borrowing only for time-limited capital","Partly resolved Oct 20: climate capital is borrowing-eligible (Espen); ~$0.35-0.45T of the package qualifies; credits and transfers still need pay-fors. Judgment Fund decided Oct 20 (Decision Brief 2): CLI-9 scored at full expected cost when obligated; AAJA damages carried as a disclosed contingent-liability line, bounded by CLI-3's cap. CLI-9 to CLI-13 remain options"),
 ("Road fuels and D7","The durability session phases gasoline into the fee from 2032","D7 taxes road fuels only through Moving America","Resolved Oct 20 (Espen): D7 kept for road fuels; the session's price path adopted for REV-C1; REV-C1D (convergence) open, not adopted"),
 ("Reinsurance exposure","CLI-7C (federal reinsurance backstop) and the Talarico scenario's $400B facility","Contingent exposure is off-score; one bad season can draw $150-200B","Open: if chosen, price premiums to expected loss with a repayable Treasury line (FAM-3 pattern)"),
 ("DEM-1 timing","The ledger targets DEM-1 for Feb 2029","Talarico stress test: leading with a process fight before any benefit is felt cost the most seats; D1 only needs DEM-1 by mid-2030","Resolved Oct 20: DEM-1F adopted (floor after R1, enacted by spring 2030); the D2 vote must precede DEM-1's floor time in mid-2029"),
 ("Social Security path","D8: regular-order bill in spring 2030 (needs D2 or 60)","Talarico stress test and the real Warren-Moreno framework: a 67-vote deal is available because OASI depletes in Q4 2032","Open: SS-10 (bipartisan framework) filed as an option; D8 stands unless Espen changes it. To do (Oct 20): test whether the 67-vote premise holds and compare SS-10A-C with D8 and its closers"),
 ("Talking-filibuster pace","Path C assumes six minority top fights at ~15 days each (211 days)","Talarico stress test: contested bills under a talking filibuster took 19-31 days (mean ~24); at 24-25 days path C needs ~265-270 days","Resolved Oct 20: the sensitivity is in ledger-paths.py and informed D2 (F decided); SS-10 would move Social Security off the contested list"),
 ("Senate rules path (D2)","D2 open; F primary, C alternate, G failure case","Talarico pace puts C at ~265-270 days; F at 170","Resolved Oct 20 (Decision Brief 1): F with Block 3, adopted week one 2029; C with a 15-day backstop as the opening offer to holdouts; G the written fallback; reconciliation as now, R3 vs R4 decided with the adoption resolution"),
 ("Closing the gap","Every option reached the middle through C19 (median exclusion cap) and C20","~$2.1T remained after every top-end option, borrowing reading and trim","Resolved Oct 20: Package B (C18, C35, C19b, C20) accepted as the planning basis; sprint package C38 (REV-TS1 to TS11, ~$0.90T) recommended; C19 is the fallback"),
 # Decision Brief 2 (Oct 20)
 ("Agency rebuild timing","CAP-7 spread ~$0.6T evenly over 2030-39 as increments (~$60B a year)","Espen (Oct 20): an even spread is close to useless; a rebuild needs a concentrated infusion paired with sustained funding","Resolved Oct 20: CAP-7S surge (~$0.6T, FY2030-35, borrowing-eligible inside the D4-B envelope) plus CAP-7 sustained (~0.12% of GDP from FY2032, permanent). Sizing accepted by Espen as working figures; the bottom-up per-agency review may revise it"),
 ("Program trims","Five trims (C5, C17, C33, C34, C36) were the menu for closing the run-rate gap","They are small at maturity (~0.09% of GDP in 2040; C5 nothing after 2039) and each costs a design rule or the fourth quintile","Resolved Oct 20 (Decision Brief 2): all declined; C39-C41 (TS12, HP1, HP3) cover the run rate instead. Trims may be revisited later"),
 ("Defense envelope over time","NSC-1A holds defense flat in real terms from the FY2029 base","Espen (Oct 20): explore ways to cut defense over time","Open (later in the project): a defense-reduction study; NSC-1A stands meanwhile"),
 ("D4 and deficit financing","D4: borrowing only for time-limited capital","Espen (Oct 20): open to loosening deficit-financing rules more broadly while keeping the long-term arc toward solvency, sustainability, wellbeing and fairness","Resolved Oct 20 (Decision Brief 2): D4-B adopted. Permanent programs paid for at maturity (FY2040 and every later year); an investment envelope of 0.5% of GDP to 2034 tapering to zero by 2040, holding the borrowing readings and CAP-7S; guardrails measured against the real (CBO, adjusted) baseline, not the program's own debt; Judgment Fund-backed contracts counted")
]

CUTS = [
 # id, change, dollars saved mid ($T), floor days saved, kind, rationale
 ("C5","Start Medicare dental after the budget window (dental stays in the package)",0.3,0,"Declined (Decision Brief 2)","Go-big tab: about $0.3T; pure timing (nothing after 2039), so it does not help D4-B's maturity test; D6 keeps dental in"),
 ("C17","Hold the agency rebuild to the low end of the D9 direction",0.1,0,"Declined (Decision Brief 2)","$0.5T instead of $0.6T; declined Oct 20 (too small to matter, too valuable to lose); superseded by CAP-7's restructuring into a surge (CAP-7S) and a sustained line"),
 ("C18","More top-end revenue not yet in the base: top four brackets +1 point, capital gains and dividends +2 points, LIFO repeal",0.62,0,"Revenue (accepted, planning basis)","Package B, Decision Brief 1 (Espen, Oct 20); top four brackets and gains"),
 ("C21","Finance HOU-3's state revolving-fund grants by borrowing (time-limited capital, D4)",0.06,0,"Borrow (accepted)","D4 time-limited capital; accepted in Decision Brief 1 (Oct 20)"),
 ("C19","Cap the employer health exclusion at the median premium",1.25,0,"Revenue (fallback to C19b)","Median cap; the fallback if the sprint package falls short (Decision Brief 1)"),
 ("C19b","Cap the employer health exclusion at the 75th percentile of premiums (Package B)",0.66,0,"Revenue (accepted, planning basis)","Package B, Decision Brief 1 (Oct 20): CBO alternative scaled; Q4 +$1,451 on the incidence model"),
 ("C38","Top-end scoring sprint package REV-TS1 to TS11 net of a 10% haircut: 162(m) to all employees, FDII repeal above the small-business threshold, fossil preferences, earnings stripping, spin-offs, trusts and GRATs, large retirement balances, partnership basis, like-kind, carried interest, crypto wash sales",0.89,0,"Revenue (accepted, Decision Brief 2)","Scaled from Treasury's FY2025 Green Book (pre-2025-law baseline); TS1-TS3 need fresh scores; range 0.60-1.14; REV-HP2 folded into TS1's drafting"),
 ("C29","Size CLI-5 to its carbon-channel financing (~$0.47T), CLI-5B",0.13,0,"Shrink (alternative to C37)","Not taken: C37 accepted instead (Oct 20)"),
 ("C37","Keep CLI-5 whole and finance its adaptation-finance and minerals-offtake lines (~$0.10T) by borrowing as time-limited climate capital (CLI-5F, D4 reading Oct 20)",0.10,0,"Borrow (accepted)","Accepted in Decision Brief 1 (Oct 20) in place of C29; CLI-5 kept whole"),
 ("C30","Treat Moving America's 2029-30 renewal top-ups and capital packages as time-limited capital financed by borrowing (D4)",0.30,0,"Borrow (accepted)","Accepted by Espen Oct 19"),
 ("C20","1-point surtax on income above $100K/$200K",0.67,0,"Revenue (accepted, planning basis)","Package B (Oct 20); upper-middle; passes D3 on the incidence model"),
 ("C31","Treat HOU-5's ten-year public housing repair as time-limited capital financed by borrowing (D4)",0.06,0,"Borrow (accepted)","D4 time-limited capital; accepted in Decision Brief 1 (Oct 20)"),
 ("C32","Finance DEM-17's time-limited community-infrastructure fund by borrowing (D4)",0.03,0,"Borrow (accepted)","D4 time-limited capital; accepted in Decision Brief 1 (Oct 20)"),
 ("C33","National service at appropriations scale (LAB-9B, ~150,000 slots)",0.07,0,"Declined (Decision Brief 2)","LAB-9B ~$0.05T instead of LAB-9A's $0.12T; less durable. LAB-9D chosen instead (bipartisan authorization first, LAB-9A's R2 money as fallback); the ledger keeps LAB-9A's cost until an authorization passes"),
 ("C34","Safe Everywhere lean version (SAF-10D, ~$8B a year)",0.03,0,"Declined (Decision Brief 2)","Revenue then covers it without a general-fund residual (estimate)"),
 ("C35","Restore the estate tax at 2009 parameters with a frozen exemption (REV-E1), increment beyond G9",0.15,0,"Revenue (accepted, planning basis)","Package B (Oct 20); top 0.2% of estates; counted beyond G9"),
 ("C36","Universal meals at community-eligibility scale instead (EDU-3B)",0.19,0,"Declined (Decision Brief 2)","EDU-3B ~$0.08T instead of EDU-3A's $0.27T; keeps the paperwork and the stigma universal meals remove (new Oct 20)"),
 ("C39","Cap itemized deductions' value at 28% above $450K (REV-TS12)",0.40,0,"Revenue (accepted, Decision Brief 2)","Unscored estimate (0.25-0.55); needs a joint score with G3, G9, C18 and SALT; the only single item that covers the year-ten run rate"),
 ("C40","CEO-to-median-worker pay-ratio corporate surtax (REV-HP1), contractors counted in the median",0.08,0,"Revenue (accepted, Decision Brief 2)","Sponsor estimate haircut ~50% (0.04-0.15); high-pay guardrail"),
 ("C41","21% excise on public-company top-five officers' pay above $1M (REV-HP3), pay defined as in 162(m)",0.06,0,"Revenue (accepted, Decision Brief 2)","Estimate (0.03-0.10); scored on top of TS1; high-pay guardrail"),
 ("C42","Finance CAP-7S, the time-limited agency rebuild surge, by borrowing inside the D4-B investment envelope",0.60,0,"Borrow (accepted, D4-B envelope)","Decision Brief 2 (Oct 20): the envelope (0.5% of GDP to 2034, tapering to zero by 2040, ~$1.6T) holds C21, C30-C32, C37 and this line"),
]

# How each bill's cost reaches the general fund (accounting rule, Oct 19):
#  all = every outlay is general-fund; residual = the channel pays first, the general fund backstops (floored at zero); none = inside a channel
# Dynamic sensitivity (added Oct 20, later). NOT in any total: the ledger and D4 stay on
# conventional scoring. Each row is a macroeconomic feedback on the general fund over 2030-39 in $T,
# positive = improves the budget, under CBO/JCT-style conventions (low, mid, high), plus an
# "optimistic" mid under Talarico-model-style assumptions. All are Claude's estimates.
# id, effect, rows it applies to, lo, mid, hi, optimistic mid, basis
DYNAMIC = [
 ("DY1","Taxes on corporations and top earners: lower investment and more avoidance than GX's 15% haircut assumes (6-12% of ~$7T of top-end and corporate revenue incl. C18, C35)","G1, G3, G5-G11, H1b, C18, C35",-1.00,-0.60,-0.30,-0.35,"Estimate; JCT's 2017 dynamic score recovered roughly a quarter of that law's cost (from memory), reversed here at a lower rate because conventional scores and GX already include avoidance. G1 (corporate rate) is the largest drag; G11 and G6 (base broadening) drag least"),
 ("DY2","Health coverage: richer subsidies and coverage reduce labor supply somewhat (CBO's ACA convention)","HLT-1, HLT-3",-0.25,-0.15,-0.05,-0.05,"Estimate on CBO's ACA labor-supply convention"),
 ("DY3","Child tax credit without a work requirement","FAM-1",-0.12,-0.07,-0.02,0.0,"Estimate; small labor-supply effect"),
 ("DY4","Living wage ($17, then two-thirds of the median)","LAB-4",-0.12,-0.07,-0.02,-0.02,"Scaled from CBO's 2021 Raise the Wage score ($54B deficit increase for $15 by 2025)"),
 ("DY5","Carbon fee, net of the dividend: small output drag","REV-C1, CLI-2",-0.10,-0.07,-0.03,-0.03,"Estimate"),
 ("DY6","Child care, pre-K and paid leave: higher parental (mostly maternal) employment","FAM-2, FAM-3, EDU-1",0.15,0.22,0.30,0.40,"domain-education.md's $25-45B a year of federal revenue at maturity, ramped with FAM-2 and pre-K"),
 ("DY7","Public investment: clean energy, transit, R&D, education (productivity gains mostly after 2039)","CLI-1, CLI-5, MOV-29, MOV-30, EDU-1, EDU-5",0.05,0.12,0.20,0.30,"Estimate"),
 ("DY8","Immigration: legalization raises measured employment and wages","IMM-1, IMM-2",0.02,0.06,0.15,0.20,"CBO's 2013 S.744 score: $197B deficit cut with labor-supply effects vs $175B without (via CRFB, CBPP); smaller here without S.744's guest-worker expansion"),
 ("DY9","Deficit path: fully paid for under D4, so little crowding out or interest effect either way","All",-0.05,0.0,0.05,0.10,"Estimate; the Talarico model's $1.2-1.5T deficit is what earned it a short-run boost the base case forgoes"),
]

GF_RULE = {"FAM-3":"none","CLI-5":"residual","SAF-10":"residual","DEM-1":"all","COM-1":"residual",
           "MOV-29":"all","MOV-30":"all","SS-1":"none","CLI-2":"none"}
OWN_RANGE = {"FAM-3":(0.85,0.9,1.28),"CLI-5":(0.39,0.47,0.55),"SAF-10":(0.08,0.09,0.10),"SS-1":(2.8,3.0,3.3),
             "CLI-2":(1.20,1.35,1.50),"MOV-29":(0.290,0.290,0.290),"MOV-30":(0.095,0.095,0.095),"COM-1":(0.004,0.004,0.004)}
ALT_CUTS = {"C29","C19"}  # alternatives to an accepted cut (C29 vs C37, C19 vs C19b); listed, never summed
DECLINED = {"C5","C17","C33","C34","C36"}  # declined in Decision Brief 2 (Oct 20); kept as the record, never summed
OWN_CHANNEL = {"MOV-29":"Surface transportation trust fund","MOV-30":"Surface transportation trust fund"}

def channels(bills):
    """Gross revenue and gross outlay per channel, never netted against the general fund."""
    rv = {}
    for r in REV:
        if r[6] or r[2]=="General fund": continue
        rv.setdefault(r[2],[0,0,0]); rv[r[2]] = [a+b for a,b in zip(rv[r[2]],(r[3],r[4],r[5]))]
    rows = []
    def add(ch, rev, out, note):
        rows.append(dict(channel=ch, rev_lo=round(rev[0],3), rev_mid=round(rev[1],3), rev_hi=round(rev[2],3),
                         out_lo=round(out[0],3), out_mid=round(out[1],3), out_hi=round(out[2],3), note=note))
    by = {b["id"]:b for b in bills}
    o = lambda i: (by[i]["cost_lo"],by[i]["cost_mid"],by[i]["cost_hi"])
    add("Social Security (OASDI)", rv["Social Security trust fund"], o("SS-1"), "D8 baseline; closes ~65-72% of the 4.42% gap after the haircut; revenue stays in the trust fund")
    add("Medicare HI", (0.5+0.5,0.5+0.7,0.5+0.9), (0.8,0.85,0.9), "H1a ($0.5T) plus HLT-6's Part A share (~$0.7T, est.); D4 read on a 75-year window, so the ~$0.3T is HI's reserve")
    add("Paid-leave fund", rv["Paid-leave fund"], o("FAM-3"), "Step-up toward 0.85% and a repayable Treasury loan; no general-fund backstop")
    st = rv["Surface transportation trust fund"]
    add("Surface transportation trust fund", st, st, "Receipts net of the 25% offset; spent within receipts; general-fund top-ups counted in MOV-29 and MOV-30")
    add("Carbon fee (REV-C1)", rv["Carbon fee"], rv["Carbon fee"], "80% dividend (CLI-2, ~$1.00T) plus 20% transition share to CLI-5 (~$0.25T)")
    add("Carbon border adjustment (REV-C2)", rv["Carbon border adjustment"], o("CLI-5"), "Outlay is CLI-5's gross add-ons, financed by REV-C2 plus REV-C1's transition share; residual to the general fund")
    add("Public safety", rv["Public safety"], o("SAF-10"), "Durable sources only (alcohol, fraud assessment, firearms, fees); residual (~$2.9B a year) to the general fund")
    add("Merger review", rv["Merger review"], (0.004,0.004,0.004), "HSR fee increase funds an equal enforcement increase (COM-2)")
    add("Immigration fees", rv["Immigration fees"], rv["Immigration fees"], "Statutory H-1B fee spent on adjudication and training (IMM-2)")
    return rows

def felt_by_mid(x):
    return x <= 22  # Nov 2030 = month 22 (Jan 2029 = 0)

def main():
    bills = []
    for r in B:
        (i,legacy,name,dom,src,rail,chan,lo,mid,hi,own,basis,note,days,felt,dur,tgt) = r
        y,m = map(int,tgt.split("-"))
        fm = (y-2029)*12 + (m-1) + felt
        bills.append(dict(id=i,legacy=legacy,bill=name,domain=dom,source=src,rail=rail,rail_name=RAILS[rail],channel=chan,
            cost_lo=lo,cost_mid=mid,cost_hi=hi,own_revenue=own,net_mid=round(mid-own,3),
            basis=basis,basis_note=note,floor_days=int(days),felt_months=felt,durability=dur,target=tgt,
            felt_by_midterm="Yes" if felt_by_mid(fm) else "No"))
    in_window = [b for b in bills if b["rail"] not in ("LATER","T2")]
    for b in bills:
        rule = GF_RULE.get(b["id"], "all" if b["channel"].startswith("General fund") or b["channel"]=="None" else "none")
        rlo,rmid,rhi = OWN_RANGE.get(b["id"], (b["own_revenue"],)*3)
        b["own_rev_lo"],b["own_rev_mid"],b["own_rev_hi"] = rlo,rmid,rhi
        b["own_rev_channel"] = OWN_CHANNEL.get(b["id"], b["channel"] if rule!="all" else "")
        b["gf_rule"] = rule
        if rule=="all": g = (b["cost_lo"],b["cost_mid"],b["cost_hi"])
        elif rule=="residual": g = (max(0,b["cost_lo"]-rhi), max(0,b["cost_mid"]-rmid), max(0,b["cost_hi"]-rlo))
        else: g = (0,0,0)
        b["gf_lo"],b["gf_mid"],b["gf_hi"] = [round(x,3) for x in g]
        b["net_mid"] = b["gf_mid"] if rule!="none" else round(b["cost_mid"]-b["own_revenue"],3)
    with open("bills.csv","w",newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(bills[0].keys())); w.writeheader(); w.writerows(bills)
    gf = [b for b in in_window if b["gf_rule"]!="none"]
    claims = {k: round(sum(b["gf_"+k] for b in gf),2) for k in ("lo","mid","hi")}
    gross_out = round(sum(b["gf_mid"] for b in gf if b["gf_mid"]>0),2)
    gross_sav = round(sum(b["gf_mid"] for b in gf if b["gf_mid"]<0),2)
    base = [r for r in REV if r[6] and r[2]=="General fund"]
    rev = {k: round(sum(r[j] for r in base),2) for k,j in (("lo",3),("mid",4),("hi",5))}
    floor_days = sum(b["floor_days"] for b in in_window)
    recon_vehicles = sorted({b["rail"] for b in in_window if b["rail"].startswith("R")})
    recon_days = len(recon_vehicles)*(RECON_DAYS+RESOLUTION_DAYS)
    total_days = floor_days + recon_days
    by_rail = {}
    for b in in_window:
        d = by_rail.setdefault(b["rail"], dict(rail=b["rail"], rail_name=b["rail_name"], bills=0, net_mid=0.0, floor_days=0))
        d["bills"] += 1
        if b in gf: d["net_mid"] = round(d["net_mid"] + b["net_mid"],3)
        d["floor_days"] += b["floor_days"]
    for r in recon_vehicles: by_rail[r]["floor_days"] += RECON_DAYS+RESOLUTION_DAYS
    by_domain = {}
    for b in in_window:
        d = by_domain.setdefault(b["domain"], dict(domain=b["domain"], rows=0, gf_lo=0.0, gf_mid=0.0, gf_hi=0.0, floor_days=0))
        d["rows"] += 1; d["floor_days"] += b["floor_days"]
        for k in ("lo","mid","hi"): d["gf_"+k] = round(d["gf_"+k] + b["gf_"+k],3)
    accepted = [c for c in CUTS if "accepted" in c[4]]
    summed = [c for c in CUTS if c[0] not in ALT_CUTS | DECLINED]
    cut_dollars = round(sum(c[2] for c in summed),2)
    summary = dict(
        gf_claims=claims, base_revenue=rev, gap_mid=round(claims["mid"]-rev["mid"],2),
        gap_lo=round(claims["lo"]-rev["hi"],2), gap_hi=round(claims["hi"]-rev["lo"],2),
        floor_days_needed=total_days, floor_budget=BUDGET_DAYS, floor_over=total_days-BUDGET_DAYS,
        regular_floor_days=floor_days, recon_days=recon_days, recon_vehicles=recon_vehicles,
        by_rail=list(by_rail.values()), by_domain=sorted(by_domain.values(), key=lambda d:-d["gf_mid"]),
        cut_dollars=cut_dollars, cut_days=sum(c[3] for c in summed),
        accepted_dollars=round(sum(c[2] for c in accepted),2),
        gap_after_accepted=round(claims["mid"]-rev["mid"]-sum(c[2] for c in accepted),2),
        gap_after_cuts=round(claims["mid"]-rev["mid"]-cut_dollars,2),
        days_after_cuts=total_days-sum(c[3] for c in summed),
        borrow_dollars=round(sum(c[2] for c in accepted if c[4].startswith("Borrow")),2),
        revenue_accepted=round(sum(c[2] for c in accepted if c[4].startswith("Revenue")),2),
        felt_by_midterm=sum(1 for b in in_window if b["felt_by_midterm"]=="Yes"), bills_in_window=len(in_window),
        gf_gross_outlays=gross_out, gf_gross_savings=gross_sav, channels=channels(bills),
        dynamic_lo=round(sum(r[3] for r in DYNAMIC),2), dynamic_mid=round(sum(r[4] for r in DYNAMIC),2),
        dynamic_hi=round(sum(r[5] for r in DYNAMIC),2), dynamic_optimistic=round(sum(r[6] for r in DYNAMIC),2),
    )
    json.dump(dict(summary=summary, bills=bills,
                   revenue=[dict(id=r[0],option=r[1],channel=r[2],lo=r[3],mid=r[4],hi=r[5],in_base="Yes" if r[6] else "No",reaches_middle="Yes" if r[10] else "No",legal_risk=r[7],overlap=r[8],source=r[9]) for r in REV],
                   conflicts=[dict(topic=c[0],one_doc=c[1],other_doc=c[2],resolution=c[3]) for c in CONFLICTS],
                   cuts=[dict(id=c[0],change=c[1],saves_tn=c[2],saves_days=c[3],kind=c[4],why=c[5]) for c in CUTS],
                   dynamic=[dict(id=r[0],effect=r[1],rows=r[2],lo=r[3],mid=r[4],hi=r[5],optimistic=r[6],basis=r[7]) for r in DYNAMIC]),
              open("ledger.json","w"), indent=1)
    print(json.dumps({k:v for k,v in summary.items() if k not in ("channels","by_rail","by_domain")}, indent=1))
    for d in summary["by_domain"]: print(d)
    for d in summary["by_rail"]: print(d)

if __name__ == "__main__":
    main()
