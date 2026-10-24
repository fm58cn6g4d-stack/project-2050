import json
d = json.load(open('ledger.json')); s = d['summary']
paths = json.load(open('paths.json'))
mv = json.load(open('moving-america.json'))   # written by run-all.sh from index/tools/transportation/
L = mv['ledger']; r1 = lambda k: round(L[k], 1); r2_ = lambda k: round(L[k], 2)
mov = {b['id']: b for b in d['bills']}
transport = f"""## Transportation: the Moving America plan

Moving America (Draft 2) moves most of its money and all of its revenue through two reconciliation acts inside the trifecta window, then authorizes the program in a 2031 bill. Both acts cut deficits on the plan's own scoring, so transportation adds nothing to the general-fund gap. Figures come from the transportation model (index/tools/transportation/).

| Vehicle | In the ledger | Spending | Revenue (net of 25% offset) | Net | Window |
| --- | --- | --- | --- | --- | --- |
| 2028 extension (60 votes, before the trifecta) | Conflict row | Transfer to keep both accounts solvent through FY2031, not yet sized | Current rates extended one year | Unsized | — |
| 2029 reconciliation act | MOV-29, Reconciliation I | ${r1('act29_package')}B rail and transit package + ${r2_('act29_topups')}B FY2032-35 renewal top-ups | ${r1('act29_net')}B (${r1('act29_gross')}B gross): fuel taxes permanent, indexed, ten 3¢ steps; clean-vehicle per-mile charge; truck excises | ~${r1('act29_net') - r1('act29_package') - r2_('act29_topups'):.1f}B deficit reduction | FY2029-38 |
| 2030 reconciliation act | MOV-30, Reconciliation III | ${r1('act30_package')}B package two + ${r2_('act30_topups')}B FY2035-36 top-ups | ${r1('act30_net')}B (${r1('act30_gross')}B gross): weight-distance charge, rail diesel, aviation surcharge | ~${r1('act30_net') - r1('act30_package') - r2_('act30_topups'):.1f}B deficit reduction | FY2030-39 as drafted; needs rescoring on FY2031-40 if carried on the FY2031 resolution |
| Moving America Act of 2031 | MOV-31, after the window | ${mv['program_fy32_36']:.2f}B FY2032-36; ${r2_('expansion_authority'):.2f}B expansion and ~$1B division E from the general fund | Restates the 2029-30 revenue | ${mov['MOV-31']['cost_lo']:.2f}-{mov['MOV-31']['cost_hi']:.2f}T general fund | FY2032-36 |

Two consequences for the rest of the agenda: the third reconciliation bill is not optional, because the 2030 act needs it, and the fuel-tax steps (first one Oct 1, 2029) reach most households, so they count in the D3 household net test.
"""
sources = """## Outside sources used for estimates

- [Tax Foundation, making the expanded CTC permanent](https://taxfoundation.org/blog/expanded-child-tax-credit-permanent/): $1.56T, 2022-31
- [CRFB, House child care plan if made permanent](https://crfb.org/blogs/house-child-care-plan-cost-could-double-if-made-permanent): $475-800B through 2031
- [American Action Forum, paid leave and the reconciliation bill](https://www.americanactionforum.org/daily-dish/paid-leave-and-the-reconciliation-bill/): CBO $547B; JCT 0.85% break-even
- [SSA Office of the Chief Actuary, Sanders letter, Feb 2023](https://www.ssa.gov/OACT/solvency/BSanders_20230213.pdf): provision scores used in domain-social-security.md
- [American Action Forum, FAMILY Act costs](https://www.americanactionforum.org/research/the-fiscal-implications-of-the-family-act-how-new-paid-leave-benefits-increase-leave-taking-and-drive-up-estimated-program-costs/): 0.39-0.86% of wages a year
- [CRFB, breaking down the One Big Beautiful Bill](https://crfb.org/blogs/breaking-down-one-big-beautiful-bill): $571B from clean-energy credit repeal, 2025-34 (House version)
- [CBO, budget option 52284: increase all taxes on alcoholic beverages to $16 per proof gallon (2016)](https://www.cbo.gov/budget-options/2016/52284): $70B over ten years, scaled in SAF's revenue title
- Everything else comes from Project 2050's own docs, named in each row; transportation figures are Moving America Draft 2's own estimates, not a CBO or JCT score. Education figures are the education sessions' estimates built from CBO, CRS and CRFB published figures (sources/education-transforming-education-act-analysis-and-trust-fund.md), not scores.
"""
g = s['gf_claims']; r = s['base_revenue']
f = lambda x: (("−" if x < 0 else "") + f"${abs(x):.2f}T")
pth = {p['path'][0]: p for p in paths}
r2 = [b for b in s['by_rail'] if b['rail'] == 'R2'][0]
out = []
A = out.append
A("# 2029 Trifecta Master Ledger\n")
A("Generated from index/data/inputs/ by index/tools/run-all.sh · Espen Swanson · [Live dashboard](https://claude.ai/artifact/RDuHM7DqCwvLUtVaB4ANMs)\n")
A("One row per bill or title in the agenda, keyed by its domain-file ID (HLT-1, CLI-5, IMM-1 ...), with the old ledger ID kept in a crosswalk column. Channel revenue is shown at gross and never netted against general-fund outlays; the gap comes from the general-fund column alone. index/options-register.md lists every option once, with the ones that exclude or overlap each other. The decisions behind these figures are in governing/project-2050-governing-decisions.md and the decision briefs.\n")
A(f"**Bottom line.** The agenda asks the general fund for about {f(g['mid'])} net over 2030-39 ({f(s['gf_gross_outlays'])} of outlays less {f(-s['gf_gross_savings'])} of savings) against {f(r['mid'])} from the top-end base: a gap of **{f(s['gap_mid'])}** at the midpoint. **D4 is decided (Decision Brief 2, Oct 20): the fiscal-arc rule, D4-B.** Permanent programs are paid for at maturity (FY2040 and every later year); time-limited investments may be borrowed for inside an envelope of 0.5% of GDP to 2034, tapering to zero by 2040 (about $1.6T); guardrails are measured against the real baseline. The accepted revenue (Package B, the sprint package C38, and C39-C41: TS12, HP1, HP3) is {f(s['revenue_accepted'])}, and the accepted borrowing lines (C21, C30-C32, C37 and C42, CAP-7S's rebuild surge) are {f(s['borrow_dollars'])}, inside the envelope. That leaves **{f(s['gap_after_accepted'])}** over ten years{', so the ten-year general-fund deficit is the envelope borrowing and nothing more' if s['gap_after_accepted'] <= 0.005 else ' still to close, so the ten-year general-fund deficit is the envelope borrowing plus that remainder'}; index/fiscal-long-term-model.md tests whether the run rate is covered from 2040. **No program trims are taken** (C5, C17, C33, C34 and C36 declined). Alternatives (C19 to C19b, C29 to C37) are listed but not summed. The range is {f(g['lo'])} to {f(g['hi'])} of claims and a gap of {f(s['gap_lo'])} to {f(s['gap_hi'])} (a stress bound). **D2 is decided: graduated cloture (F)**, adopted in week one of 2029, with the talking filibuster (C) as the opening offer and the carve-out (G) as the fallback. The legacy fixed-duration crosswalk reports **{pth['F']['days']} Senate floor days under F against {s['floor_budget']}** ({s['floor_days_needed']} under majority cloture, E; {pth['C']['days']} under C).\n")
A("All dollar figures are ten-year totals for 2030-39 in trillions. \"Estimate\" means Claude's estimate where no doc or score exists; \"proposal\" means an author's figure sized against current programs, not a score. Legacy crosswalk only: reconciliation was charged 15 days plus 2 for its resolution; 163 was an assumed net budget. Neither is a validated current capacity estimate. Use index/calendar-scenarios.md for the current method.\n")
A("**Surge timing (Oct 21):** all CAP-7S funding targets R1 and is available immediately as multi-year money. FY2029 cash is unpriced; totals retain the old cash proxy pending agency costing and do not certify accelerated-path D4 compliance. See index/capacity-funding-model.md. R1 routing assumes eligibility; Byrd/jurisdiction checks remain open.\n")
A("**Not in any total (unscored or not chosen):** CLI-7 disaster and flood insurance (rough $0.05-0.15T), CRT-5 Article I immigration court (~$0.03T), EXE-14B tariff claim ($1.5-1.9T), DEM-3's chamber capital, DEM-6's statehood fiscal effect, CAP-13, LAB-4's indirect effects, LAB-3's Medicaid rate effect, AI-6 (held), the contingent cannabis excise (PS2), the NDAA's floor time, the EDU-9B education fund and its contribution (ED1, held), the climate durability options CLI-9 to CLI-13 (about $1.8-1.9T net if all were taken, session estimate; about $0.35-0.45T of it borrowing-eligible as time-limited climate capital under D4-B), CLI-7C's reinsurance exposure, HOU-9, REV-E2, and the Talarico-derived options (SS-10, AI-4E, AI-4F, REV-SC1 to SC3, LAB-8B, DEM-2E, RTS-3E, CRT-P4, EXE-18C). REV-SC1 is held in reserve as the first fallback if TS12 scores low; REV-HP2 is folded into TS1's drafting.\n")
A("**Approved calendar update (Oct 23):** Congress begins January 3, before the January 20 presidential term. Preparation and other priorities can move early/in parallel. R1 targets administration weeks 3–4 (February preferred, March latest); DEM-1 floor consideration begins by March 2029 at latest, with an explicit recovery decision if R1 slips. R2 targets summer 2029 using FY2030 instructions; R3 remains summer 2030. SS retains spring 2030. Seasonal input targets preserve windows rather than invent months. Capacity reservations are not proof of dated feasibility. MOV-31 remains second Congress from January 2031; it was already excluded from 172. Its duration and first-Congress reserve remain unknown. See sources/calendar-c-development.md and sources/post-pilot-integration-handoff.md.\n")
A("**Current calendar method:** index/calendar-scenarios.md and its explorer compare conditional schedules. index/calendar-delivery-opportunities.md screens possible initial effects separately; every legacy felt label remains Unverified. Earlier passage creates opportunity, not a verified receipt date.\n")
A("**Approved health development (Oct 23):** develop component-level 2029 restoration and January-2030 HLT-2 hearing/vision; compare summer R2 with earlier preparation against possible R1 authority while protecting rapid R1. The legacy 24-month field is not a verified CMS minimum. Current restoration, hearing/vision, dental and HLT-3 launch inputs remain the adopted baseline; no incremental score or CMS launch plan is complete. See [canonical health alternatives](../domains/domain-health.md#earlier-delivery-alternatives-development-approved-october-23) and [health evidence and next work](../sources/health-2029-restoration-and-2030-medicare-option.md).\n")
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
A(f"\nR2 is the heaviest vehicle ({r2['bills']} rows, about ${r2['net_mid']:.1f}T): it carries housing, the labor credits, national service, the journalism credit, veterans health and five education rows (EDU-1, EDU-3, EDU-4, EDU-5, EDU-7) beside health upgrades, child care, leave, the clean-energy credits and the dividend. If R1 is lost (D5), its contents move here too. The Talarico stress test suggests universal meals (EDU-3) would be felt sooner on R1, but R2 now targets summer 2029; actual 2030-31 service delivery still requires a separate implementation path.\n")
A("## Options still open\n\nRevenue options that reach the middle must pass the D3 household net test.\n")
A("| # | Change | Closes ($T) | Saves (days) | Kind | Why |\n| --- | --- | --- | --- | --- | --- |")
for c in d['cuts']: A(f"| {c['id']} | {c['change']} | {c['saves_tn'] if c['saves_tn'] else ''} | {c['saves_days'] if c['saves_days'] else ''} | {c['kind']} | {c['why']} |")
A(f"\nWith every accepted row, the midpoint gap over ten years is {f(s['gap_after_cuts'])}: the general fund's ten-year deficit is the {f(s['borrow_dollars'])} of time-limited lines borrowed inside the D4-B envelope, and its run rate is covered from 2040 (index/fiscal-long-term-model.md). Declined trims and alternatives (C5, C17, C33, C34, C36; C19, C29) are listed but not summed; index/options-register.md lists which options exclude or overlap each other. One risk sits outside the range: G8 failing to score on its vehicle (+$0.40T). The largest unscored claim not in any total is CLI-7 (rough $0.05-0.15T). The held education fund (EDU-9B) would relieve the general fund of about $2.0T in exchange for a middle-reaching contribution; it is a D3 and D4 decision, not an option on this list.\n")
A("## Dynamic sensitivity (not in any total)\n")
A(f"Every figure in this ledger is conventionally scored, and D4 counts no dynamic revenue. This table asks what macroeconomic feedback would do if the agenda were scored the way the Talarico scenario model was (it booked $0.6-0.9T of feedback on a partly deficit-financed package). Under CBO/JCT-style conventions the feedback sums to **{f(s['dynamic_mid'])}** (range {f(s['dynamic_lo'])} to {f(s['dynamic_hi'])}): the paid-for base case raises about $7T from corporations and top earners, where dynamic scoring takes revenue back, and gives up the short-run lift a deficit buys. Under Talarico-style assumptions (larger care and investment responses, smaller capital-tax drag) it is about **{f(s['dynamic_optimistic'])}**. On the conventional mid, the ten-year gap after every accepted row would be about {f(round(s['gap_after_cuts']-s['dynamic_mid'],2))} instead of {f(s['gap_after_cuts'])}. All rows are Claude's estimates, not scores. The positive rows grow after 2039 (immigration, pre-K and education, investment), so a 2040-49 view would likely be net positive even under conventional assumptions.\n")
A("| # | Effect | Rows | Low | Mid | High | Talarico-style | Basis |\n| --- | --- | --- | --- | --- | --- | --- | --- |")
for r in d['dynamic']: A(f"| {r['id']} | {r['effect']} | {r['rows']} | {r['lo']:+.2f} | {r['mid']:+.2f} | {r['hi']:+.2f} | {r['optimistic']:+.2f} | {r['basis']} |")
A(f"| | **Total** | | **{s['dynamic_lo']:+.2f}** | **{s['dynamic_mid']:+.2f}** | **{s['dynamic_hi']:+.2f}** | **{s['dynamic_optimistic']:+.2f}** | |\n")
A("**What it implies.** The dynamic risk sits in the top-end base, which supports keeping GX's 15% haircut and preferring base broadening (G11, G6) to rate increases; among the open options C18 carries the most dynamic risk and C35 almost none.\n")
A("## Legacy floor-time crosswalk under the D2 paths\n\nD2 is decided (Decision Brief 1): F, graduated cloture with Block 3's minority guarantees. C (with a 15-day backstop) is the opening offer to institutionalist holdouts and G the written fallback; E stays as an upper bound on speed. Legacy days compare fixed assumptions against an assumed 163-day allowance, counting the three reconciliation bills and the rules vote. Each path's per-bill cost is my estimate from the Senate Rules doc.\n")
A("| Path | Senate floor days | Contested regular-order bills that pass | Over (+) or under (−) the 163-day budget |\n| --- | --- | --- | --- |")
for p in paths: A(f"| {p['path']} | {p['days']} | {p['bills']} of {p['of']} | {p['over_first']} |")
A(f"\nThere are {pth['E']['of']} contested regular-order bills (EDU-6 is proposed to ride CAP-8 and EDU-8's rules ride AI-1, at no extra days). Under G only the carve-out (DEM-1 with its riders, DEM-5, DEM-6) passes, and the other 17 bills stay ◐ items for a later rules change. Under D1 there is no 2033 queue except the second-term package, so the legacy overrun is not an approved deferral. Current scenario comparisons assess all scope against demand, capacity, readiness and contingency ranges. Calendar C retains the full CLI-7/8 fallback; earlier passage gets credit only for enacted coverage. CLI-3/6 net saving and additional reserve remain unknown; a six-day combined bill would illustrate 4.5 days saved, not validate that duration.\n")
A(f"**Path C sensitivity (Talarico stress test).** The scenario's contested bills under a talking filibuster took 19-31 days each (mean about 24), not 15. At 20 days per top fight path C needs about {pth['C']['days'] + 6 * 5} days, and at 25 about {pth['C']['days'] + 6 * 10} (estimate, from ledger-paths.py); swapping in the bills the minority is proud to block (IMM-1, RTS-3) changes the total by about a day. Moving Social Security to a negotiated bill (SS-10) would save about 17 days at 25 per fight.\n")
A("""## Calendar under the scenario stipulations

- **2029-30:** a trifecta. **2031-32:** a House possibly lost or narrowed; Senate and White House hold. **2033-36:** a trifecta again, on the condition that the electoral and civil-rights package is in force before the 2031 redistricting.
- **Assumed done before 2029:** the Bipartisan American Affordability and Jobs Act of 2026 (sources/permitting-aaja-2026-analysis.md); CLI-3 carries the CES in statute with the Sec. 1401 override.
- **Must pass in the first trifecta:** HLT-3, CLI-6 and CLI-7, IMM-1, AI-1 and AI-4. **Ideally also:** COM-1, SAF-1, LAB-1.
- **Before the 2031 maps:** DEM-1 (with DEM-2's commissions and mid-decade ban, carrying the 2034 exception), must pass by mid-2030. Under DEM-1F it takes the floor with floor consideration starting no later than March 2029 (normally after early R1 signature; a delay triggers recovery, not automatic postponement) and is enacted by spring 2030; the D2 rules change (F) is adopted in week one, well before it.
- **Second trifecta (rail T2):** DEM-3 (House size), DEM-4 (STV) and DEM-9 (presidential method, amendment vehicle AMD-3) as one package: run on in 2032, enacted 2033, one-off 2034 redraw. The climate durability review's 2032-36 lock-in measures would ride the 2033-36 reconciliation bills if taken up.
- **Built in:** merges C23-C26 (living wage into the labor bill, junk fees into competition, background checks into SAF-1, congressional capacity into CAP-8), the C27 fast track (INT-1, CAP-8) and C28's nomination caps (+15 days).
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
A("\nRows with no legacy ID: LAB-8, LAB-9, AI-9, DEM-11, DEM-16, DEM-17, NSC-8, CLI-7 (from E5), EDU-3, EDU-4, EDU-7, EDU-8, CAP-7S.\n")
A("## Conflicts between docs\n\n| Topic | One doc says | Another says | Status |\n| --- | --- | --- | --- |")
for c in d['conflicts']: A(f"| {c['topic']} | {c['one_doc']} | {c['other_doc']} | {c['resolution']} |")
A("")
A("## Master register\n\nGross outlays and own revenue are shown separately; the three general-fund columns are what the gap sums. A row fully inside a dedicated channel shows zero there.\n")
A("| ID | Legacy | Bill | Vehicle | Channel | Gross outlay mid (range) | Own revenue mid (channel) | General fund mid | GF low | GF high | Days | Felt evidence by Nov 2030 | Durability | Basis | Note | Source |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for b in d['bills']:
    own = f"{b['own_rev_mid']:.3f} ({b['own_rev_channel']})" if b['own_rev_mid'] else ""
    A(f"| {b['id']} | {b['legacy']} | {b['bill']} | {b['rail']} | {b['channel']} | {b['cost_mid']:.2f} ({b['cost_lo']:.2f}-{b['cost_hi']:.2f}) | {own} | {b['gf_mid']:.3f} | {b['gf_lo']:.3f} | {b['gf_hi']:.3f} | {b['floor_days']} | {b['felt_by_midterm']} | {b['durability']} | {b['basis']} | {b['basis_note']} | {b['source']} |")
A("")
A("## Revenue menu\n\n| ID | Option | Channel | Mid ($T) | Low | High | In base | Reaches the middle | Legal risk | Overlap | Source |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for v in d['revenue']: A(f"| {v['id']} | {v['option']} | {v['channel']} | {v['mid']:.3f} | {v['lo']:.3f} | {v['hi']:.3f} | {v['in_base']} | {v['reaches_middle']} | {v['legal_risk']} | {v['overlap']} | {v['source']} |")
A("")
A("""## Where the inputs live

- governing/: the governing decisions (repo copy of the live doc) and the decision briefs
- domains/: one canonical file per domain (domain-revenue.md, domain-health.md, domain-family.md, domain-social-security.md, domain-education.md, domain-democracy.md, domain-courts.md, domain-executive-power.md, domain-integrity.md, domain-capacity.md, domain-climate.md, domain-housing.md, domain-labor.md, domain-competition.md, domain-immigration.md, domain-rights.md, domain-public-safety.md, domain-ai.md, domain-national-security.md, domain-amendments.md), plus transportation-moving-america-act-2031-draft-2.md (canonical until converted) and public-safety-safe-everywhere.md (the evidence base behind domain-public-safety.md)
- index/: this ledger and the other generated files; data/inputs/ (the tables this ledger is built from); tools/ (the scripts); the options register and the revenue assignment audit (hand-written)
- staging/: unified-reform-inventory-current.md (rows point to the domain files)
- frameworks/: reasoning, not policy (Radical Means, Instruments and Consequences, the Talarico stress test, the transit-rail split)
- sources/: outside inputs behind the domain files
- archive/: ideas only, never current sources
""")
A(sources)
open('2029-trifecta-master-ledger-v2.md','w').write("\n".join(out))
print(len("\n".join(out)))
