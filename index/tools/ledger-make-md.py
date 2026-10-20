import json
d = json.load(open('ledger.json')); s = d['summary']
paths = json.load(open('paths.json'))
old = open('2029-trifecta-master-ledger.md').read()
def sect(name):
    i = old.index('## ' + name); j = old.find('\n## ', i + 3)
    return old[i: j if j > 0 else len(old)].rstrip() + '\n'
transport = sect('Transportation: the Moving America plan').replace("M1 and M2", "MOV-29 and MOV-30")
sources = sect('Outside sources used for estimates')
g = s['gf_claims']; r = s['base_revenue']
f = lambda x: (("−" if x < 0 else "") + f"${abs(x):.2f}T")
pth = {p['path'][0]: p for p in paths}
PREV_GAP = 4.11; PREV_AFTER = 0.15  # after Espen's Oct 20 morning decisions, before Decision Brief 1
r2 = [b for b in s['by_rail'] if b['rail'] == 'R2'][0]
out = []
A = out.append
A("# 2029 Trifecta Master Ledger\n")
A("Full rebuild, Oct 20, 2026 (after batch 4), with the education batch the same evening and Espen's decisions later that day · Espen Swanson · [Live dashboard](https://claude.ai/artifact/RDuHM7DqCwvLUtVaB4ANMs)\n")
A("This is the full rebuild the governing doc called for once every domain had a file: batches 1-4 plus the two canonical-until-converted files (Moving America, and Safe Everywhere through domain-public-safety.md). **Every row is keyed by its domain-file ID** (HLT-1, CLI-5, IMM-1 ...). The old ledger IDs (H1, E11, DEM1 ...) are kept in a crosswalk column, which ends the DEM0-DEM13 / DEM-1-DEM-20 collision. The accounting rule from the Oct 19 revenue audit still holds: channel revenue is shown at gross and never netted against general-fund outlays, and the gap comes from the general-fund column alone. **Education batch (Oct 20, evening):** education now has its own domain file (domains/domain-education.md); FAM-4 splits into EDU-1 and EDU-5 at the same total, and four education rows are new. The climate durability review and the Talarico scenario stress test add options only (no rows). **Later on Oct 20:** the carbon fee takes the durability path, D4 is read to allow borrowing for climate capital, the estate-tax option is restated as the increment beyond G9, and DEM-1F is adopted. index/options-register.md lists every option once.\n")
A(f"**Bottom line.** The agenda asks the general fund for about {f(g['mid'])} net over 2030-39 ({f(s['gf_gross_outlays'])} of outlays less {f(-s['gf_gross_savings'])} of savings) against {f(r['mid'])} from the top-end base: a gap of **{f(s['gap_mid'])}** at the midpoint. **Decision Brief 1 (Oct 20)** set the planning basis: Package B's revenue (C18, C35, C19b, C20) and four borrowing readings (C21, C31, C32, C37) are accepted with C30, leaving **{f(s['gap_after_accepted'])}**. The program trims in the next brief (up to $0.69T) and the recommended top-end sprint package (C38, about $0.89T) would close the rest; taking every open option leaves **{f(s['gap_after_cuts'])}** (it was {f(PREV_AFTER)}). Alternatives (C19 to C19b, C29 to C37) are listed but not summed. The range is {f(g['lo'])} to {f(g['hi'])} of claims and a gap of {f(s['gap_lo'])} to {f(s['gap_hi'])} (a stress bound). **D2 is decided: graduated cloture (F)**, adopted in week one of 2029, with the talking filibuster (C) as the opening offer and the carve-out (G) as the fallback. The calendar needs **{pth['F']['days']} Senate floor days under F against {s['floor_budget']}** ({s['floor_days_needed']} under majority cloture, E; {pth['C']['days']} under C).\n")
A("All dollar figures are ten-year totals for 2030-39 in trillions. \"Estimate\" means Claude's estimate where no doc or score exists; \"proposal\" means an author's figure sized against current programs, not a score. Reconciliation bills count 15 floor days plus 2 for the budget resolution; the 163-day budget is 148 discretionary days plus about 15 freed by Block 1's nomination caps.\n")
A("**Not in any total (unscored or not chosen):** CLI-7 disaster and flood insurance (rough $0.05-0.15T), CRT-5 Article I immigration court (~$0.03T), EXE-14B tariff claim ($1.5-1.9T), DEM-3's chamber capital, DEM-6's statehood fiscal effect, CAP-13, LAB-4's indirect effects, LAB-3's Medicaid rate effect, AI-6 (held), the contingent cannabis excise (PS2), the NDAA's floor time; and, new Oct 20, the EDU-9B education fund and its contribution (ED1, held), the climate durability options CLI-9 to CLI-13 (about $1.8-1.9T net if all were taken, session estimate; about $0.35-0.45T of it borrowing-eligible under the Oct 20 D4 reading), CLI-7C's reinsurance exposure, HOU-9, REV-E2, and the Talarico-derived options (SS-10, AI-4E, AI-4F, REV-SC1 to SC3, LAB-8B, LAB-9D, DEM-2E, RTS-3E, CRT-P4, EXE-18C).\n")
A("## What changed with Decision Brief 1 (Oct 20)\n")
A("| Change | Source | Effect on the general-fund gap (mid) |\n| --- | --- | --- |")
for row in [
 ("D2 decided: graduated cloture (F) with Block 3, week one 2029; C with a 15-day backstop as the opening offer; G as fallback. Reconciliation stays as now; R3 vs R4 is decided with the adoption resolution", "Decision Brief 1; Senate Rules Reform: Options", "0 (F needs 170 floor days against 163)"),
 ("Package B accepted as the planning basis: C18, C35, C19b (75th-percentile exclusion cap, new row) and C20; C19 at the median becomes the fallback", "Decision Brief 1; domain-revenue.md", "Accepted: −$2.10T"),
 ("Borrowing readings accepted: C21, C31, C32 and C37 (C37 in place of C29)", "Decision Brief 1; D4", "Accepted: −$0.25T"),
 ("Top-end scoring sprint: REV-TS1 to TS11 (162(m), FDII repeal above the small-business threshold, fossil preferences, earnings stripping, spin-offs, trusts, retirement balances, partnership basis, like-kind, carried interest, crypto), net of a 10% haircut, as option C38; TS12 (28% itemized cap) held in reserve; SC3 narrowed to crop insurance", "domain-revenue.md; Treasury FY2025 Green Book via ITEP; CBO via CRFB", "Option: −$0.89T (0.60-1.14)"),
 ("D4 revision directed (loosen deficit financing while keeping a long-term arc toward solvency): options drafted in the governing doc; nothing changed in the ledger until parameters are chosen", "Governing doc", "0"),
]: A("| " + " | ".join(row) + " |")
A("\n## What changed later on Oct 20 (Espen's decisions)\n")
A("| Change | Source | Effect on the general-fund gap (mid) |\n| --- | --- | --- |")
for row in [
 ("Carbon fee takes the durability session's price path ($25 a ton in 2030 rising to ~$100 by 2037), road fuels still exempt (D7); C1 $1.25T to $1.35T; dividend $1.00T to $1.08T; transition share $0.25T to $0.27T. Options re-lettered (old path is REV-C1B; convergence REV-C1D stays open, not adopted)", "domain-revenue.md; domain-climate.md", "−$0.02T (CLI-5's residual falls with the larger transition share)"),
 ("D4 read to allow borrowing for time-limited climate capital; new option C37 (CLI-5F: keep CLI-5 whole, borrow ~$0.10T of capital lines), an alternative to C29 (now $0.13T), not summed", "domain-climate.md; governing doc", "0 (options)"),
 ("Estate tax: G9 already reverses most of the 2025 law's $15M exemption, so E1/C35 is restated from $0.35T to the ~$0.15T increment beyond G9", "domain-revenue.md; ACTEC on JCT's estimate", "Options −$0.20T; gap after every option −$0.05T to about +$0.15T"),
 ("DEM-1F adopted (DEM-1 after R1, enacted by spring 2030; target moves from Feb to mid-2029); DEM-1E (registration at benefit-delivery points) adopted into Title I", "domain-democracy.md", "0"),
 ("Standing disbursement authority adopted as a design rule; statute EXE-18 with EXE-18B (pointer to CAP-4's auto-CR) and EXE-18C (debt limit, option)", "governing doc; domain-executive-power.md", "0"),
 ("Stress-test proposals filed: DEM-2E, RTS-3E, LAB-8B, LAB-9D, CRT-P4; AI workforce options cross-listed in domain-labor.md; EDU-9C and EDU-9D retired as duplicates", "domain files", "0"),
 ("index/options-register.md added: every option once, with overlap and exclusivity groups", "index/", "0"),
]: A("| " + " | ".join(row) + " |")
A("\n## What changed in the education batch (Oct 20, evening)\n")
A("| Change | Source | Effect on the general-fund gap (mid) |\n| --- | --- | --- |")
for row in [
 ("Education gets its own domain file; FAM-4 ($0.65T) splits into EDU-1 (Title I and IDEA, carrying EDU-2, $0.33T) and EDU-5 (Pell, SAVE and PSLF, $0.32T); legacy F4 maps to both", "domain-education.md; domain-family.md", "0"),
 ("EDU-3 universal school meals and Summer EBT at current reimbursement rates (new)", "domain-education.md; Transforming Education analysis", "+$0.27T"),
 ("EDU-4 educator pipeline surge, front-loaded ahead of FAM-2's pre-K hiring (new)", "domain-education.md", "+$0.03T"),
 ("EDU-7 prospective repeal of the federal scholarship tax credit (new; a saving)", "domain-education.md", "−$0.04T"),
 ("EDU-8 AI in education, student data and education research (EDU-10), appropriations; EDU-8's rules ride AI-1 and EDU-6's Education Department protections are proposed to ride CAP-8, at no extra days", "domain-education.md; AI education bill analysis", "+$0.015T"),
 ("Options C35 (REV-E1, estate tax at 2009 parameters, $0.35T) and C36 (EDU-3B, meals at community-eligibility scale, $0.19T) added; ED1 (the education contribution behind EDU-9B) added to the revenue menu, held", "domain-revenue.md; domain-education.md", "Options total +$0.54T"),
 ("Climate durability review folded as options only: CLI-9 to CLI-13, new options under CLI-1 and CLI-3 to CLI-8, REV-C1B to C1E, REV-C2B, REV-E2", "domain-climate.md; domain-revenue.md", "0"),
 ("Talarico scenario stress test filed; options HOU-9, SS-10, AI-4E, AI-4F, AI-5B, CLI-7C, EDU-5D and REV-SC1 to SC3; DEM-1F and other proposals recorded for the files that own them", "frameworks/scenario-stress-test-talarico-2029-2037.md", "0"),
 ("Incidence model re-run (v1.3): education rows; scenarios G (EDU-9B as closer) and H (C35)", "index/revenue-household-incidence-model.md", "Q4 on scenario B: +$779 (was +$546)"),
]: A("| " + " | ".join(row) + " |")
A("\n## What changed in the full rebuild (Oct 20)\n")
A("| Change | Source | Effect on the general-fund gap (mid) |\n| --- | --- | --- |")
for row in [
 ("Rows keyed by domain-file IDs; legacy IDs kept as a crosswalk column; merged zero-cost rows (DEM2, DEM6, DEM9, DEM12, E10, S4) folded into the rows that carry them", "Governing doc next step; batch 2 conflict row", "0"),
 ("Housing restated: HOU-3C's direct loans at subsidy cost, HOU-2 sized; E6 split into an R2 title (HOU-1, $0.47T) and a floor bill (HOU-7, 3 days)", "domain-housing.md", "−$0.13T"),
 ("Labor: LAB-5 credit split from E8 onto R2; LAB-8 apprenticeships added", "domain-labor.md", "+$0.03T"),
 ("LAB-9 national service added (new permanent program; moved from DEM-15 at Espen's request)", "domain-labor.md", "+$0.12T"),
 ("Climate: E1-E5 become CLI-1 to CLI-7; CLI-4 rides CLI-3; E5 split into CLI-6 and CLI-7 (4 days each); CLI-7 unscored", "domain-climate.md", "0 (CLI-4 adds $0.01T at the high end only)"),
 ("Competition: merger-review channel sized (~$0.004T a side); COM-6 added", "domain-competition.md", "0"),
 ("Immigration: IMM-3 processing (~$0.01T) added to E11", "domain-immigration.md", "+$0.01T"),
 ("AI: E12 split into the AI bill (AI-1, 5 days, ~$0.02T) and AI-4 wage insurance on R3 ($0.20T); AI-9 journalism credit on R2 ($0.02T)", "domain-ai.md", "+$0.04T"),
 ("National security: A2 becomes NSC-1 with a base definition; F6 becomes NSC-10 ($0.07T); NSC-8 preparedness added ($0.02T)", "domain-national-security.md", "+$0.015T"),
 ("Democracy and civic life: DEM-11 election funding (+$0.02T), DEM-16 civic education (+$0.01T), DEM-17 community capital fund (+$0.03T, borrowing allowed as C32), DEM-13 rides DEM-1", "domain-democracy.md", "+$0.06T"),
 ("Public safety: S5 moves from appropriations to R3 (SAF-10A, −3 floor days); PS1 restated to durable sources ($0.09T), dropping deployment savings and Crime Victims Fund receipts", "domain-public-safety.md; bill summary", "+$0.02T"),
 ("Rights and amendments: RTS-1 to RTS-4 carry S1-S2 unchanged; domain-amendments.md has no ledger rows", "domain-rights.md; domain-amendments.md", "0"),
 ("Options: C21 shrinks to $0.06T (HOU-3C); C31 (HOU-5 repair as capital), C32 (DEM-17 as capital), C33 (LAB-9B) and C34 (SAF-10D) added; C13 superseded", "Domain files", "Options total unchanged at $3.64T"),
 ("Incidence model re-run (v1.2): housing, the public-safety package, LAB-8 and LAB-9 updated", "index/revenue-household-incidence-model.md", "Q4 on scenario B: +$546 (was +$463)"),
]: A("| " + " | ".join(row) + " |")
A("\nEarlier rebuild records (the Oct 19 audit rebuild and the batch 2 refresh) are in earlier versions of this file and in index/revenue-assignment-audit.md; their resolutions are carried in the conflicts table below.\n")
A("## By domain\n\n| Domain | Rows | General fund low | Mid | High | Floor days |\n| --- | --- | --- | --- | --- | --- |")
for x in s['by_domain']: A(f"| {x['domain']} | {x['rows']} | {x['gf_lo']:.2f} | {x['gf_mid']:.2f} | {x['gf_hi']:.2f} | {x['floor_days']} |")
A(f"| **Total** | | **{g['lo']:.2f}** | **{g['mid']:.2f}** | **{g['hi']:.2f}** | **{s['regular_floor_days']}** (+{s['recon_days']} for R1-R3) |\n")
A("## Channels at gross\n\nEach dedicated channel's revenue and outlays, kept out of the general-fund gap. Every row that reaches households enters the D3 household net test. The proposed education fund (EDU-9B, held) is not a channel until chosen.\n")
A("| Channel | Revenue mid | Revenue range | Outlays mid | Outlay range | Note |\n| --- | --- | --- | --- | --- | --- |")
for c in s['channels']: A(f"| {c['channel']} | {c['rev_mid']:.2f} | {c['rev_lo']:.2f}-{c['rev_hi']:.2f} | {c['out_mid']:.2f} | {c['out_lo']:.2f}-{c['out_hi']:.2f} | {c['note']} |")
A("")
A(transport)
A("## By vehicle\n\n| Vehicle | Rows | General-fund net ($T) | Floor days |\n| --- | --- | --- | --- |")
for b in s['by_rail']: A(f"| {b['rail_name']} | {b['bills']} | {b['net_mid']:.2f} | {b['floor_days']} |")
A(f"\nR2 is the heaviest vehicle ({r2['bills']} rows, about ${r2['net_mid']:.1f}T): it carries housing, the labor credits, national service, the journalism credit, veterans health and now five education rows (EDU-1, EDU-3, EDU-4, EDU-5, EDU-7) beside health upgrades, child care, leave, the clean-energy credits and the dividend. If R1 is lost (D5), its contents move here too. The Talarico stress test suggests universal meals (EDU-3) would be felt sooner on R1, but R2's fall-2029 timing still reaches the 2030-31 school year before the midterm.\n")
A("## Options still open\n\nRevenue options that reach the middle must pass the D3 household net test.\n")
A("| # | Change | Closes ($T) | Saves (days) | Kind | Why |\n| --- | --- | --- | --- | --- | --- |")
for c in d['cuts']: A(f"| {c['id']} | {c['change']} | {c['saves_tn'] if c['saves_tn'] else ''} | {c['saves_days'] if c['saves_days'] else ''} | {c['kind']} | {c['why']} |")
A(f"\nTaking every option brings the midpoint gap to {f(s['gap_after_cuts'])}, without a payroll tax, a VAT or new tariffs. On the planning basis (Package B and the borrowing readings accepted) the gap is about $1.46T; the next brief's trims and the sprint package C38 would close it with a small cushion, thin against the dynamic sensitivity below. C19 and C29 are alternatives to accepted rows and are not summed; index/options-register.md lists which options exclude or overlap each other. One risk sits outside the range: G8 failing to score on its vehicle (+$0.40T). The largest unscored claim not in any total is CLI-7 (rough $0.05-0.15T). The held education fund (EDU-9B) would relieve the general fund of about $2.0T in exchange for a middle-reaching contribution; it is a D3 and D4 decision, not an option on this list.\n")
A("## Dynamic sensitivity (not in any total)\n")
A(f"Every figure in this ledger is conventionally scored, and D4 counts no dynamic revenue. This table asks what macroeconomic feedback would do if the agenda were scored the way the Talarico scenario model was (it booked $0.6-0.9T of feedback on a partly deficit-financed package). Under CBO/JCT-style conventions the feedback sums to **{f(s['dynamic_mid'])}** (range {f(s['dynamic_lo'])} to {f(s['dynamic_hi'])}): the paid-for base case raises about $7T from corporations and top earners, where dynamic scoring takes revenue back, and gives up the short-run lift a deficit buys. Under Talarico-style assumptions (larger care and investment responses, smaller capital-tax drag) it is about **{f(s['dynamic_optimistic'])}**. On the conventional mid, the gap after every option would be about {f(round(s['gap_after_cuts']-s['dynamic_mid'],2))} instead of {f(s['gap_after_cuts'])}. All rows are Claude's estimates, not scores. The positive rows grow after 2039 (immigration, pre-K and education, investment), so a 2040-49 view would likely be net positive even under conventional assumptions.\n")
A("| # | Effect | Rows | Low | Mid | High | Talarico-style | Basis |\n| --- | --- | --- | --- | --- | --- | --- | --- |")
for r in d['dynamic']: A(f"| {r['id']} | {r['effect']} | {r['rows']} | {r['lo']:+.2f} | {r['mid']:+.2f} | {r['hi']:+.2f} | {r['optimistic']:+.2f} | {r['basis']} |")
A(f"| | **Total** | | **{s['dynamic_lo']:+.2f}** | **{s['dynamic_mid']:+.2f}** | **{s['dynamic_hi']:+.2f}** | **{s['dynamic_optimistic']:+.2f}** | |\n")
A("**What it implies.** The dynamic risk sits in the top-end base, which supports keeping GX's 15% haircut and preferring base broadening (G11, G6) to rate increases; among the open options C18 carries the most dynamic risk and C35 almost none.\n")
A("## Floor time under the D2 paths\n\nD2 was decided Oct 20 (Decision Brief 1): F, graduated cloture with Block 3's minority guarantees. C (with a 15-day backstop) is the opening offer to institutionalist holdouts and G the written fallback; E stays as an upper bound on speed. Days are the first Congress's needs against its 163-day budget, counting the three reconciliation bills and the rules vote. Each path's per-bill cost is my estimate from the Senate Rules doc.\n")
A("| Path | Senate floor days | Contested regular-order bills that pass | Over (+) or under (−) the 163-day budget |\n| --- | --- | --- | --- |")
for p in paths: A(f"| {p['path']} | {p['days']} | {p['bills']} of {p['of']} | {p['over_first']} |")
A(f"\nThere are {pth['E']['of']} contested regular-order bills; the education batch adds none (EDU-6 is proposed to ride CAP-8 and EDU-8's rules ride AI-1). Under G only the carve-out (DEM-1 with its riders, DEM-5, DEM-6) passes, and the other 17 bills stay ◐ items for a later rules change. Under D1 there is no 2033 queue except the second-term package, so the overrun closes through D2, merges (CLI-6 into CLI-3 and CLI-7 into a 2027-28 60-vote vehicle would save about 9 days under F, estimate) or more floor days.\n")
A("**Path C sensitivity (Oct 20, Talarico stress test).** The scenario's contested bills under a talking filibuster took 19-31 days each (mean about 24), not 15. At 20 days per top fight path C needs about 241 days, and at 25 about 271 (estimate, from ledger-paths.py); swapping in the bills the minority is proud to block (IMM-1, RTS-3) changes the total by about a day. Moving Social Security to a negotiated bill (SS-10) would save about 17 days at 25 per fight.\n")
A("""## Calendar under the scenario stipulations

- **2029-30:** a trifecta. **2031-32:** a House possibly lost or narrowed; Senate and White House hold. **2033-36:** a trifecta again, on the condition that the electoral and civil-rights package is in force before the 2031 redistricting.
- **Assumed done before 2029:** the Bipartisan American Affordability and Jobs Act of 2026 (sources/permitting-aaja-2026-analysis.md); CLI-3 carries the CES in statute with the Sec. 1401 override.
- **Must pass in the first trifecta (Espen, Oct 19):** HLT-3, CLI-6 and CLI-7 (old E5), IMM-1 (E11), AI-1 and AI-4 (E12). **Ideally also:** COM-1 (E9), SAF-1 (S3), LAB-1 (E7).
- **Before the 2031 maps:** DEM-1 (with DEM-2's commissions and mid-decade ban, carrying the 2034 exception), must pass by mid-2030. DEM-1F adopted Oct 20: the floor after R1 is signed (mid-2029), enacted by spring 2030; the D2 rules change (F) is adopted in week one, well before it.
- **Second trifecta (rail T2):** DEM-3 (House size), DEM-4 (STV) and DEM-9 (presidential method, amendment vehicle AMD-3) as one package: run on in 2032, enacted 2033, one-off 2034 redraw. The climate durability review's 2032-36 lock-in measures would ride the 2033-36 reconciliation bills if taken up.
- **Accepted Oct 19 and built in:** merges C23-C26 (living wage into the labor bill, junk fees into competition, background checks into SAF-1, congressional capacity into CAP-8), the C27 fast track (INT-1, CAP-8) and C28's nomination caps (+15 days).
""")
A("## Crosswalk: legacy ledger IDs to domain IDs\n\n| Legacy ID | Now |\n| --- | --- |")
cw = {}
for b in d['bills']:
    for leg in [x.strip() for x in b['legacy'].split(',')]:
        if leg and leg != '—': cw.setdefault(leg, []).append(b['id'])
extra = {"DEM2":"DEM-1 (INT-2 rides it)","DEM6":"CRT-P1","DEM9":"EXE-1","DEM12":"CAP-8","E10":"COM-1 (COM-5)","S4":"SAF-1 (SAF-5)"}
order = lambda k: (k.rstrip('0123456789'), int(''.join(ch for ch in k if ch.isdigit()) or 0))
for k in sorted(list(cw)+list(extra), key=order):
    A(f"| {k} | {', '.join(cw[k]) if k in cw else extra[k]} |")
A("\nNew rows with no legacy ID: LAB-8, LAB-9, AI-9, DEM-11, DEM-16, DEM-17, NSC-8, CLI-7 (from E5); and, in the education batch, EDU-3, EDU-4, EDU-7, EDU-8.\n")
A("## Conflicts between docs\n\n| Topic | One doc says | Another says | Status |\n| --- | --- | --- | --- |")
for c in d['conflicts']: A(f"| {c['topic']} | {c['one_doc']} | {c['other_doc']} | {c['resolution']} |")
A("")
A("## Master register\n\nGross outlays and own revenue are shown separately; the three general-fund columns are what the gap sums. A row fully inside a dedicated channel shows zero there.\n")
A("| ID | Legacy | Bill | Vehicle | Channel | Gross outlay mid (range) | Own revenue mid (channel) | General fund mid | GF low | GF high | Days | Felt by Nov 2030 | Durability | Basis | Note | Source |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for b in d['bills']:
    own = f"{b['own_rev_mid']:.3f} ({b['own_rev_channel']})" if b['own_rev_mid'] else ""
    A(f"| {b['id']} | {b['legacy']} | {b['bill']} | {b['rail']} | {b['channel']} | {b['cost_mid']:.2f} ({b['cost_lo']:.2f}-{b['cost_hi']:.2f}) | {own} | {b['gf_mid']:.3f} | {b['gf_lo']:.3f} | {b['gf_hi']:.3f} | {b['floor_days']} | {b['felt_by_midterm']} | {b['durability']} | {b['basis']} | {b['basis_note']} | {b['source']} |")
A("")
A("## Revenue menu\n\n| ID | Option | Channel | Mid ($T) | Low | High | In base | Reaches the middle | Legal risk | Overlap | Source |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for v in d['revenue']: A(f"| {v['id']} | {v['option']} | {v['channel']} | {v['mid']:.3f} | {v['lo']:.3f} | {v['hi']:.3f} | {v['in_base']} | {v['reaches_middle']} | {v['legal_risk']} | {v['overlap']} | {v['source']} |")
A("")
A("""## Where the inputs live (Oct 20 file layout)

- governing/: Governing Decisions (project copy; the live doc wins)
- domains/: batch 1 domain-revenue.md, domain-health.md, domain-family.md, domain-social-security.md; batch 2 domain-democracy.md, domain-courts.md, domain-executive-power.md, domain-integrity.md, domain-capacity.md; batch 3 domain-climate.md, domain-housing.md, domain-labor.md, domain-competition.md; batch 4 domain-immigration.md, domain-rights.md, domain-public-safety.md, domain-ai.md, domain-national-security.md, domain-amendments.md; education batch (Oct 20) domain-education.md. Canonical until converted: transportation-moving-america-act-2031-draft-2.md. public-safety-safe-everywhere.md is now the evidence base behind domain-public-safety.md (move to sources/ pending)
- index/: this ledger (generated; never edit by hand), the tools that build it, the revenue assignment audit and the household incidence model
- staging/: unified-reform-inventory-current.md (every section now has a domain home; rows become pointers)
- frameworks/: adds scenario-stress-test-talarico-2029-2037.md (Oct 20)
- sources/: adds climate-durability-pathway-session-findings.md, education-transforming-education-act-analysis-and-trust-fund.md, education-ai-education-and-workforce-readiness-act-analysis.md and scenario-talarico-2029-2037.md (Oct 20)
- archive/: adds the two PROJECT 2029 docs (Oct 20), ideas only, flagged for a later read for anything still useful
""")
A(sources)
open('2029-trifecta-master-ledger-v2.md','w').write("\n".join(out))
print(len("\n".join(out)))
