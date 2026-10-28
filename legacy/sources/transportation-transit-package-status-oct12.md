# Transit package — status and decisions

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/transit-package-status.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


> **Calendar and name (2026-10-12):** the 2031 bill covers **FY2032-36**, and its working title is the **Moving America Act of 2031**. ATRA is division C, ARCA division D. 250-Plus runs through FY2031. See `sources/transportation-calendar-fy2032-36.md`. The merge handoff is `sources/transportation-atra-merge-contribution-oct12.md`, and the merge prompt is `archive/transportation-merge-session-prompt-oct12.md`.

Built 2026-10-04; verification 2026-10-05; second pass and rebase 2026-10-12; checked against CBO's Sept 30, 2026 estimate of H.R. 8870 on 2026-10-12. Counterpart to ARCA. Everything here is revisable; the numbers come from `index/tools/transportation/transit_fiscal_model.py`.

## Products

| Product | Where |
| --- | --- |
| Package section-by-section (250-Plus, reconciliation, 2031 reauthorization, Divisions A-F) | https://claude.ai/code/artifact/fb14029c-152b-4727-9ae3-b2f055c8b6f7 |
| Bill architecture doc: American Transit Renewal Act of 2031 | https://claude.ai/code/artifact/6eded0d5-40fc-433a-b940-8d8ca015f581 |
| Delivery pipeline grid (64 projects, 13 systems, FY2026-46) | https://claude.ai/artifact/9NB4tkaPEjxBtUVjLRwQCJ |
| System-expansion map (2036 / 2045 / 2055) | https://claude.ai/artifact/CAwpF9wA6TwKqLsUYcfoaY |
| Fiscal model | `index/tools/transportation/transit_fiscal_model.py` (run with `--json` for output) |
| Operating-tier apportionment | `index/tools/transportation/transit_apportionment.py` + data `index/tools/transportation/ntd_uza_2024.py` |
| Pipeline dataset behind the grid and map | `index/tools/transportation/transit_pipeline_data.py` |

## CBO estimate of H.R. 8870 (Sept 30, 2026), what it changed

- Confirmed: obligation limitations $470.7B FY2027-31 (FHWA + FTA + ~$2.0-2.2B/yr NHTSA/FMCSA); CIG $15B; Amtrak $31.1B; rail grants $27.6B; current-law HTF receipts match the model to the decimal ($49.1B FY2029).
- Total authorized $579.3B = $470.7B limitations + $108.6B other, incl. Bridge Investment Program $10B, multimodal freight $6B, National Infrastructure Grants $10B (sec. 7105) — general fund, outside the model.
- WMATA: $150M in FY2031 only (was carried as $0.75B). 250-Plus transit now $102.8B authorized, ~$99.8B delivered.
- EV fee: runs through FY2036, goes to the general fund (not the HTF); gross $16.8B, net $12.4B FY2026-36. Model now uses CBO gross collections.
- HTF cumulative shortfall end FY2031 under the bill: highway $99.5B, transit $48.2B (baseline $86.0B / $45.2B). Through FY2030: $71.2B / $36.8B. Highway account dry in FY2028.
- RRIF cap: H.R. 8870 raises $35B → $50B; ARCA proposes $150B.

## Base case (from 2026-10-12)

- **Per-mile yield:** rate x FHWA vehicle-miles (3.32T in 2025, +0.5%/yr), all vehicles, nominal cents, 10% collection cost.
- **Highways:** H.R. 8870 as introduced, $72.9B-77.6B/yr FY2027-31, then +2.5%/yr, plus NHTSA/FMCSA ($2.0-2.5B/yr, CBO limitation less FHWA and FTA) folded into the Highway Account's need (decided 2026-10-12).
- **Cap:** 0.206% is this project's benchmark (ARCA's own 0.192% rule restated), not a CBO or statutory limit. Espen is fine exceeding it. Binding constraints: reconciliation instructions (sized to CBO's net-of-offset score), PAYGO, Byrd.
- **Fee schedule:** 1.0 cent in FY2029, +0.2/yr, 3.6 cents in FY2042; fuel taxes displaced linearly over the same 14 years.
- **Shares of new revenue (arch C):** 35 / 50 / 15 kept (decided). On FY2032-36 the equal-coverage answer is 34.7 / 53.7 / 11.6, with renewal coverage FY2042-46 of 73 / 70 / 79%. Transit gap left for the later EV redesign.

## Results on the base case (arch C, scenario B, NHTSA/FMCSA included; FY2032-36 calendar)

- **The bill, FY2032-36:** $908.80B. Highways and safety $430.35B, transit $224.42B, rail $254.03B.
- **Dedicated revenue:** $531.71B (316.25 / 147.20 / 68.26).
- **General fund:** $377.09B. Expansion is $126.70B; renewal transfers are $250.39B (114.10 / 43.72 / 92.57).
- **All-in GF draw:**
  - FY2027-28: 0.171%;
  - FY2029-31: 0.154% (FY2030 peak 0.197%, FY2031 0.081%);
  - **FY2032-36: 0.174% (peak 0.177% FY2034)**;
  - FY2037-41: 0.123%; FY2042-46: 0.123%.
  - Benchmark 0.206%.
- **Room:** $3.1B FY2030; $48.1B FY2031; $12.4-16.6B/yr FY2032-36.
- **CBO basis:** 0.219% FY2030; 0.193-0.203% FY2032-36.
- **Scenario C:** FY2032-36 0.190% (peak 0.193%).
- **Equal-coverage shares:** 34.7 / 53.7 / 11.6. Renewal coverage under 35/50/15 is 73 / 70 / 79.
- **ARCA alone:** 0.121% / 0.122% / 0.069% / 0.068%.
- **Full set:** `sources/transportation-calendar-fy2032-36.md`.

## ARCA handoff

- `archive/transportation-arca-handoff-prompt-oct12.md`: decisions, CBO findings, numbers and edits to carry into the ARCA chat.

## 250-Plus proposal change

- Two-account transfer of $108.0B ($71.2B highway + $36.8B transit, CBO's shortfall through FY2030). Under Espen's 2026-bill discipline rule it is not grown to $147.7B for FY2031: nothing in 250-Plus may be sized to the later program. Reconciliation cannot transfer GF money, and the highway account runs dry in FY2028.

## Operating tier apportionment (FY2031, $6.0B; NTD 2024, ACS 2019-23; 183 UZAs >= 200k)

- 0.5% State floor replaced with a ceiling: no area > 25% of net operating cost; excess reapportioned. Old floor moved $344M/yr to 18 States.
- Tier = 11.9% of national net operating cost ($50.6B). New York 27.7%. Areas over 5M: 54.5% of tier vs 56.6% of net cost; under 1M: 14.9% vs 10.0%.
- Caveat: agencies assigned wholly to primary UZA.

## Chapter 53 conforming amendments (doc Title VII, secs. 711-716)

- 711 planning targets; 712 5311(g)(2)(A) 50% → 80%; 713 5324(g) waiver; 714 5329(g)(2)(C); 715 stale cross-refs (5339(a)(5) (L)→(M); 5340(b) → 5338(a)(2)(O)); 716 5338(c)(1)(B) takedown excludes 5307(i).
- Drafting rule: cite 5338(a)(2) by program, not letter.

## Joint terminals (sec. 606 / SEC. 109)

- Renewal attributed by share of train movements; expansion by share of added train movements. Chicago 79% commuter movements. $6.0B planning figure.

## Accessibility (sec. 605)

- ~965 of 3,447 rail transit stations inaccessible (2021). No national cost; bill requires FTA to publish one.

## Open items

- Decide whether H.R. 8870's $26B GF grants count against the benchmark.
- Read 49 CFR parts 625, 630, 673 against Titles II and III.
- Scope the five terminal projects; set sec. 606 project by project.
- Rerun apportionment with FTA's multi-area splits.
- Check H.R. 8870 sec. 3023 against enrolled text.
- Apply the ARCA handoff in the ARCA chat.
- WMATA sentence in ATRA doc's 250-Plus note was absorbed into a source link during the CBO edit; tidy formatting.
