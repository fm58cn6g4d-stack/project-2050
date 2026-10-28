# The 2031 bill covers FY2032-36 — decision, name, and the restated figures

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/calendar-fy2032-36.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Decided by Espen on 2026-10-12. This **supersedes every "FY2031-35" figure** in:

- the ATRA doc;
- the ARCA doc;
- the package section-by-section;
- `sources/transportation-transit-package-status-oct12.md`;
- `sources/transportation-atra-merge-contribution-oct12.md`;
- `archive/transportation-arca-handoff-prompt-oct12.md`;
- `sources/transportation-arca-status-oct12.md`.

All figures below come from `index/tools/transportation/transit_fiscal_model.py` after the shift (`BILL_START = 2032`). Run the model rather than trusting prose.

## The decision

- **BUILD America 250-Plus** (December 2026) covers FY2027-31, through September 30, 2031.
- **The 2031 bill covers FY2032-36.** It must be enacted by September 30, 2031, which still makes it "of 2031." There is no overlap and no supersession clause.
- The earlier framing double-authorized FY2031: 250-Plus's last year and the 2031 bill's first. The model had silently assumed the 2031 bill replaced FY2031.

## The name

**Working title: the Moving America Act of 2031.**

- It is a short umbrella that sits over the division short titles without colliding with them:
  - the American Transit Renewal Act (division C);
  - the American Rail Competitiveness Act (division D).
- It doesn't echo a recent bill closely. MAP-21 was "Moving Ahead for Progress," and H.R. 2 (2020) was the "Moving Forward Act." Check for conflicts before using it publicly.

Alternatives if Espen prefers:

- **Fix It First, Build It Next Act.** Sells the renewal-first rule, which is the bill's organizing idea.
- **Surface Transportation Renewal and Investment Act.** Plain and descriptive.

Convention for both chats and the merge: "the Moving America Act of 2031 (the 2031 bill)." The divisions keep their short titles.

## The conventions the shift uses

1. **Program tables keep their nominal amounts, one year later.**
   - Every canonical table drafted for FY2031-35 is relabeled FY2032-36 with the same dollars by year. That includes ATRA's $224.42B (40.70 / 42.89 / 45.09 / 47.04 / 48.70) and ARCA's $254.03B (39.95 / 47.29 / 52.07 / 56.13 / 58.59).
   - That is a ~2.5% real reduction. It is **(A), flagged**: inside the sizing's precision, and it avoids reopening every line.
   - If Espen would rather hold real value, multiply every line by 1.025. The draw rises about 0.004 points.
2. **Highways continue H.R. 8870's FY2031 level at 2.5% a year from FY2032**, so FY2031 itself is 250-Plus.
   - NHTSA/FMCSA is grown the same way from its FY2031 residual.
3. **FY2031 is a 250-Plus year for every mode.**
   - Transit is $20.70B (contract authority $18.16B + CIG $2.40B delivered + WMATA $0.15B).
   - Rail is **$13.3B** delivered: ARCA's 250-Plus delivered total of $59.6B less $46.3B in FY2027-30 (set by the ARCA chat; the model carries it).
   - Highways are $77.64B FHWA + $2.24B safety.
4. **Revenue schedules:**
   - **Unchanged:** per-mile fee 1.0¢ FY2029 → 3.6¢ FY2042; fuel-tax displacement over the same span; EV fee per CBO through FY2036.
   - **Shifted:**
     - aviation segment surcharge $4 in FY2032 → $12 in FY2036 → capped at $16 by FY2046;
     - rail diesel 10¢/5¢ for FY2030-31 (the 2030 package), 15¢/7.5¢ from FY2032.
5. **Reporting periods:** FY2027-28, **FY2029-31** (reconciliation plus 250-Plus's last year), **FY2032-36** (the bill), FY2037-41, FY2042-46.
6. **Statutory dates that move with it:**
   - continuation under div. A sec. 107 at **FY2036** levels;
   - contingent commitments (sec. 106) to **FY2046**;
   - ARCA's $25B readiness reserve released over **FY2032-36**;
   - sec. 101(c) base amounts still FY2028;
   - the equal-coverage report under sec. 101(h) is due 18 months before **September 30, 2036**.
7. **ARCA's validation sections** (its revenue rows, its 0.105 / 0.099 affordability rows) are reproduced on the **old** calendar, `calendar(2031)` in the model. They are ARCA's original figures and stay as they were.

## Restated figures (architecture C, scenario B, NHTSA/FMCSA included)

### The bill, FY2032-36 ($B)

| | FY2032 | FY2033 | FY2034 | FY2035 | FY2036 | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Highways, FHWA | 79.58 | 81.57 | 83.60 | 85.69 | 87.84 | 418.28 |
| NHTSA + FMCSA | 2.30 | 2.35 | 2.41 | 2.47 | 2.53 | 12.07 |
| **Division B** | 81.87 | 83.92 | 86.02 | 88.17 | 90.37 | **430.35** |
| **Division C** (ATRA) | 40.70 | 42.89 | 45.09 | 47.04 | 48.70 | **224.42** |
| **Division D** (ARCA) | 39.95 | 47.29 | 52.07 | 56.13 | 58.59 | **254.03** |
| **Total** | 162.52 | 174.10 | 183.18 | 191.34 | 197.66 | **908.80** |

- Up to $25B of ARCA readiness authority sits on top, contingent.
- Division E is about $1.0B, outside the model.

### How it is paid for, FY2032-36

| $B | Highways | Transit | Rail | Total |
| --- | --- | --- | --- | --- |
| Program | 430.35 | 224.42 | 254.03 | 908.80 |
| Dedicated (fund $495.5B + aviation/diesel $36.2B) | 316.25 | 147.20 | 68.26 | 531.71 |
| General fund | 114.10 | 77.22 | 185.77 | 377.09 |
| of which expansion (mandatory approps) | — | 33.50 | 93.20 | 126.70 |
| of which div. A sec. 110 renewal transfers | 114.10 | 43.72 | 92.57 | 250.39 |

Expansion is:

- **transit:** sec. 401 CIG $27.50B + sec. 606 $6.00B;
- **rail:** secs. 303, 310, 311, 312.

### General-fund draw against the 0.206% benchmark

| Period | Average | Peak |
| --- | --- | --- |
| FY2027-28 | 0.171% | 0.173% (FY2027) |
| FY2029-31 | 0.154% | 0.197% (FY2030); FY2029 0.190%, FY2031 0.081% |
| **FY2032-36** | **0.174%** | **0.177% (FY2034)** |
| FY2037-41 | 0.123% | 0.132% (FY2037) |
| FY2042-46 | 0.123% | 0.124% (FY2042) |

- **Room under the benchmark:**
  - FY2029 $5.7B; FY2030 $3.1B; FY2031 $48.1B;
  - FY2032-36 $12.4-16.6B a year ($14.9 / 12.4 / 12.5 / 13.6 / 16.6);
  - after ARCA's reserve at $5B a year, $7.4-11.6B.
- **CBO basis** (new excise net of a ~25% income/payroll offset):
  - FY2030 0.219%; FY2031 0.104%;
  - **FY2032-36 0.193-0.203%, under the benchmark in every year.** It was over in the old calendar.
- **Scenario C** (5307 operating tier doubled): FY2032-36 average 0.190%, peak 0.193% (FY2034). It now fits with about $5B a year of room.
- **Scenario A** (no tier): FY2032-36 average 0.157%, peak 0.161%.
- **Fee start:**
  - 0.6¢ breaches in FY2029-31 by $14.3B (FY2030 0.228%);
  - 0.8¢ breaches by $2.7B (FY2030 0.213%);
  - neither breaches in FY2032-36. FY2030, not the bill, is now what forces the 1.0¢ start.
- **Sensitivities** (peaks, FY2029-30 / FY2032-36):
  - light-duty-only fee: 0.209% / 0.194%;
  - 13% collection cost: 0.201% / 0.182%;
  - both: 0.212% / 0.198%.
- **ARCA alone, all-in:** FY2029-31 0.121%; FY2032-36 0.122%; FY2037-41 0.069%; FY2042-46 0.068%.

### Coverage and shares

- **Whole-program coverage** by dedicated revenue (highways / transit / rail):
  - FY2029-31: 70 / 75 / 17;
  - FY2032-36: 73 / 66 / 27;
  - FY2037-41: 75 / 65 / 48;
  - FY2042-46: 73 / 59 / 50.
- **Equal-renewal-coverage shares** (FY2042-46): **34.7 / 53.7 / 11.6** (scenario B). The drafted text stays **35 / 50 / 15**.
  - Renewal coverage under the draft: 73 / 70 / 79.
  - Under the earlier 30 / 50 / 20: 71 / 70 / 88.
  - If 5% or 10% of the highway program is classed as expansion, the solve becomes 31.4 / 55.8 / 12.8 or 27.9 / 58.0 / 14.1.
- **Architectures, FY2042-46:**
  - A (standalone rail fund) 99 / 28 / 33, $1.8B trapped;
  - B (ARCA's original sec. 101) 73 / 16 / 107, $16.0B trapped.
- **FY2042-46 overall:** dedicated receipts about $143B a year against $223B of programs.
- **Rail renewal programs in FY2036:** $37.1B. This is what sec. 107 continuation carries.

### What the shift changes in the argument

1. **The bill fits more easily.**
   - The fee has had three years to grow before the bill's first year, while program tables stayed nominal.
   - The FY2032-36 draw falls from 0.185% to 0.174%, and the CBO-basis figure drops under the benchmark.
   - Scenario C becomes affordable on the benchmark ($5B a year of room). **The case for scenario B now rests on policy, not on fit:** federal share, substitution risk, and the trade-down dial.
2. **FY2031 becomes a cliff year.**
   - Rail falls from about $37B in FY2030 (250-Plus plus reconciliation) to $13.3B in FY2031, then to $39.95B in FY2032.
   - Transit falls from $40.2B (250-Plus plus the 2030 package) to $20.7B.
   - FY2031 has $48B of room under the benchmark.
   - **Recommendation:** the 2030 reconciliation package (or a third, FY2031 tranche) carries availability through FY2031. That is still inside the Byrd window, with obligation deadlines.
3. **The 250-Plus general-fund transfer stays at $108.0B.** It is $71.2B highway + $36.8B transit, CBO's shortfall through FY2030. This file's first version proposed growing it to $147.7B, CBO's shortfall through FY2031. **Espen has since set the 2026-bill discipline rule:** nothing in 250-Plus may be sized to anything in these documents, and a 2026 Congress patches to the cash in front of it. So the $147.7B is withdrawn. See `sources/transportation-arca-status-oct12.md`, "The 2026-bill discipline rule."
4. **The Corridor ID new-selection sunset (October 1, 2031) now falls exactly on the bill's first day.** Division D makes the program permanent from FY2032, so there's no gap if the bill is enacted on time. An extension act covers a slip.

## For the ARCA chat — applied 2026-10-12 (kept for the record; see `sources/transportation-arca-status-oct12.md`)

> The 2031 bill now covers FY2032-36, not FY2031-35, and its working title is the Moving America Act of 2031. Read `sources/transportation-calendar-fy2032-36.md` in the project and apply it to the ARCA doc:
>
> 1. Relabel the canonical table and every title table FY2032-36, keeping the nominal amounts by year (39.95 / 47.29 / 52.07 / 56.13 / 58.59 = $254.03B).
> 2. Give FY2031 its own 250-Plus figure. The model assumes about $13.7B delivered; replace it with ARCA's own and tell me the number so the model can carry it.
> 3. Move the aviation surcharge to $4 FY2032 → $12 FY2036 → $16 cap by FY2046, and the rail diesel to 10¢/5¢ for FY2030-31 and 15¢/7.5¢ from FY2032.
> 4. Restate:
>    - sec. 107 continuation at FY2036 levels;
>    - sec. 106 contingent commitments to FY2046;
>    - the $25B readiness reserve over FY2032-36;
>    - the out-year rows as FY2037-41 and FY2042-46.
> 5. Replace the affordability and fit-table figures with the restated ones in that file:
>    - ARCA alone 0.122 / 0.122 / 0.069 / 0.068;
>    - combined FY2032-36 0.174% (peak 0.177%);
>    - CBO basis 0.193-0.203%;
>    - rail dedicated $68.26B; rail general fund $185.77B ($92.57B renewal transfer + $93.20B expansion);
>    - coverage FY2042-46 50% whole program, 79% renewal.
> 6. Note the FY2031 cliff, and that the Corridor ID sunset now coincides with the bill's start.
> 7. Leave ARCA's own validation rows (0.105 / 0.099 / 0.019 / 0.001 and the dedicated-revenue rows) on the original calendar. They are ARCA's figures, reproduced as drafted.
> 8. Update `sources/transportation-arca-status-oct12.md` when done.
