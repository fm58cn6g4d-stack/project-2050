# A home you can keep: L2/L3 milestone review

Role: the independent milestone review of the housing dossier (`charter/PLAN.md` 3.2 and 5, "Review"; `charter/STANDARDS.md`, "Milestone review"), board row 6. The reviewer wrote none of the dossier. It tries to break the work on four tests (weak evidence, missing populations, optimistic assumptions, cheaper alternatives), applies the design lens (`DEC-2026-11-09-13`) and checks internal consistency. Status: current, as of main at commit `077a953` (November 10, 2026, after PR #181, the rural fold-in). Reviewer: Claude Code, `session_01UQzgBvRTi5eLrx7Nkrv7Tq`. It changes nothing in the dossier: every fix below is for a later step, which the lead assigns.

Decided items (`DEC-` entries) are Espen's decisions. Where this review finds that one has a weakness or a cost the dossier understates, it says so under "For Espen"; it does not treat a decision as an error.

## Verdicts

| Level | What it needs (`charter/PLAN.md` 3.2) | Verdict |
| --- | --- | --- |
| **L2, design** | Key parameters chosen (who, what, how much, who administers), with the main alternatives weighed | **Pass with fixes** |
| **L3, specified** | Provisions section by section (eligibility, benefit, administration, phase-in, remedies); evidence for each load-bearing claim; a cost range validated by models with stated limits; a delivery plan | **Not yet** |

**Why L2 passes with fixes.** Every fork has two to four options weighed on evidence, with "keep the legacy design" as an explicit option where `DEC-2026-10-30-02` asks for it, and Espen has decided each one (`DEC-2026-11-09-01` to `DEC-2026-11-10-02`). The memos are good decision documents: plain, sourced, and honest about where a recommendation rests on judgment. The fixes are about the record, not the design. Section 3's forks 1-8 still read as open recommendations and do not record the decisions; its summary still describes options Espen did not choose (finding C-1). A few parameters are still open, more than the two the board lists (C-2).

**Why L3 is not yet.** Three of the four L3 parts are close. Section 4 specifies 56 provisions with eligibility, amounts, vehicle, agency and current-law changes. Section 5 is a real delivery plan. Most load-bearing claims have graded evidence. The blockers:
1. **The cost is not yet model-validated.** Section 6 is careful arithmetic laid over the budget model's published paths, and it says so (`6-cost.md:9`). Its 13 proposed ledger and model changes (`6-cost.md:374-401`) are tier 3 and none is made, so the model still books housing at about $0.71 trillion and $65 billion in FY2040, against the dossier's $0.78 trillion and about $96 billion. L3 asks for a cost range validated by models. Fix: the tier-3 PR and a model run of the D4 tests (O-6).
2. **Some provisions are not yet specified.** Stage 3's eligibility (age 62 and over, and the severe-problems test) is open (`6-cost.md:428-429`). Search help's design research has not been done (`4-specification.md:190-195`). Several other parameters are still waiting on Espen (C-2).
3. **Section 9 claims a few things sections 1-8 do not support** (E-1 to E-5, W-1). Section 9 must never run ahead of sections 1-8.
4. **Stale headline figures across five files** (C-3 to C-6). They are quick to fix, but a reader of the README or section 8 gets the wrong cost and the wrong gap today.

**What can reach L3 once the fixes land.** Most provisions can: the rules (HOU-4.01 to 4.06, HOU-4.09, HOU-4.11, HOU-4.13), stage 1 and stage 2 (HOU-4A.01, HOU-4D.01), the emergency fund (HOU-1D.01 to .04, once question 4 and the HOU-1D.04 question are answered), the capital (HOU-3C.01 to .06), zoning (HOU-6.01, 6.02), the credits (HOU-2D.01 to .04, once the rural boost is answered), and HOU-10 to HOU-14. Expect these to stay at L2 until their gaps close:
- HOU-4.08 (stage 3): eligibility not set;
- HOU-4.07 (search help): design research owed;
- HOU-4.10 and HOU-4.12: placeholders with no per-place or per-tenant cost evidence;
- HOU-9A.01: placeholder capital and no evaluation of a U.S. public developer;
- HOU-5.01 and HOU-8.01: legacy working choices that section 3 did not re-weigh.

## How this review was done

- Read the charter (standards, board, plan sections 3 and 5, the decision log), the template, sections 1-9, memos 1-13 and 3b, the research notes, `road-act.md`, `road-funding.md`, `provisions.json` and `dossiers/foundations/rural-delivery.md`. `evidence.json` was read selectively, for the entries behind load-bearing claims.
- Two subagents ran mechanical cross-checks: amounts, limits and statuses across sections 4-9, `provisions.json`, `agenda/agenda.csv` and `charter/decisions.md`; and the grades behind load-bearing claims. The reviewer checked what they reported against the files before using it.
- The reviewer re-added section 6's table (`6-cost.md:46-80`): the outlays sum to $661 billion and the FY2040 column to about $91 billion, matching its total row.
- `bash .github/scripts/run-checks.sh` passes on `077a953`. The registry checker lists about 55 analysis entries without independent corroboration or contested; the load-bearing ones are under "Weak evidence".

## Findings

Each finding has an ID, where it is, what goes wrong, and a severity. **Blocking** means blocking for L3; **not blocking** means fix when convenient. Line numbers are at `077a953`.

### 1. Weak evidence

The register itself is in good order. Every ID cited in sections 6 and 9 resolves, and none of them is an uncorroborated analysis. About half are grade A data. The weak points sit outside the register: section 6's largest inputs are untagged judgments, which are grade D or E in substance. Section 9 then repeats several of them as facts.

**W-1. Section 9 states as fact several figures that are judgment.** Blocking for section 9. The figures:
- 1.4 million households a year reached by the emergency fund (`9-public-case.md:38`, `:99`);
- 1.4 million buyers helped (O-4);
- 220,000-330,000 homes repaired a year (`:50`);
- about $3 billion of FY2040 cost from the property-tax match (`:68`);
- about 1.0 million net new homes with the zoning reward (`:148`).

Each rests on one or more inputs that section 6 or 4 marks as judgment:
- the emergency fund's $3,500 a household;
- the repair cost of $12,000-18,000 a home, against grants of up to $25,000 plus $15,000;
- the pace at which states join the tax match, and its 2-4 million owners at $500-1,000 each (`6-cost.md:258`; the one tag, EV-HOU-670, supports only the growth rate);
- the zoning reward's 1.5% supply rise, about twice the best U.S. estimate of 0.8% within three to nine years [EV-HOU-177] (`4-specification.md:449`).

*Fix:* in section 9, say "about" with the range and "on our estimates", or drop the figure. Under the template, a project estimate is shown as one.

**W-2. The emergency fund's reach is untested against the register's own data.** Not blocking.
- Section 6 prices help at about $3,500 a household (`6-cost.md:153`).
- The 2021-22 program's two rounds, $25 billion and $21.55 billion, reached 5.35 million households [EV-HOU-150]. That is roughly $8,700 a household, before netting out administration and unspent money.
- At that rate, $5 billion reaches about 0.6 million households a year, not 1.4 million. The four-month cap narrows the gap, but section 7's "holds on cost" (`7-validation.md:120-122`) does not test it.
- *Fix:* section 6 shows the per-household figure against the 2021 program's and sizes reach as a range.

**W-3. The Section 502 cost rests on an untagged OMB rate from the second Trump administration.** Not blocking; fix before L3.
- *Where:* `6-cost.md:292` and `memos/13-rural.md:30`, `:74`. They use OMB's FY2026 subsidy rate of about 13%, and treat guaranteed loans as earning more in fees than they cost.
- *The problem:* neither figure has an `EV-` entry in the housing register; the source is cited only in `rural-delivery.md`. OMB's FY2026 rates are executive-branch estimates issued in 2025. Under `DEC-2026-10-30-01` they need their administration named and an independent check, such as CBO's credit estimates for the same accounts. They also underpin memo 13's "a staffing problem, not a money problem".
- *Also:* EV-HOU-777, the staffing claim memo 13's recommendation B rests on, is USDA's own FY2027 budget judgment ("historically low staffing"), graded A data. The staff counts in it are data; the judgment is the administration's.

**W-4. Several grades do not match the kind of evidence.** Not blocking.
- **EV-HOU-779 and EV-HOU-780:** letters from members of Congress, graded B. B means experimental or peer-reviewed. The facts they relay should be C, or A where USDA's own bulletin confirms them.
- **EV-HOU-344:** a USICH announcement whose own context says it has "a stake", graded A. It drives section 6's lease-lag input (`6-cost.md:35`).
- **EV-HOU-552:** HUD's 2025 FHA actuarial report (second Trump administration), graded A data. Its stress-test result (4.42%) is model output, so analysis. FHA's "room" for the premium cut leans on it with no independent check.
- **EV-HOU-679:** the reverse-mortgage "no scored cost" (`6-cost.md:259`) rests on the same kind of HUD model.

**W-5. Section 7's "holds" on cost per voucher compares section 6 with its own source.** Not blocking.
- *Where:* `7-validation.md:131` checks the $17,000 against "$15,800-18,000 from HUD's 2023 figure". That is EV-HOU-370, the same source section 6 used.
- *The independent figures:* CBO's $9,400 for 2019 [EV-HOU-391] and Urban's $9,200 [EV-HOU-392] are older and lower. The explanation section 7 gives (rent growth, poorer and larger households) is reasonable, but it is an explanation, not a benchmark.
- *Fix:* section 7 brings CBO's figure forward on the rent index and shows the gap.

**W-6. Two of section 9's messages say more than their sources.** Not blocking.
- **Message 5** (`9-public-case.md:99`) says "two studies". EV-HOU-108 and EV-HOU-109 share an author, and EV-HOU-109 is an interview with the trial's authors; the journal article was not read. Say "one research team, in two places".
- **The landlord answer** (`:119`) says "few did where the law forbade it". The source gives 31% in Newark and 15% in Washington [EV-HOU-093], at five sites, uncorroborated. 31% is not few. Say "far fewer", and cite EV-HOU-094 for the law's effect.

**W-7. Untagged numbers carry weight.** Not blocking. In section 6:
- the 90% lease-up and 85% take-up (judgment, marked);
- every spend-out rate;
- the credits' $0.10 trillion (legacy HOU-2B) and the loans' 5% subsidy rate (legacy);
- the about $200 billion a year of FHA purchase loans (`6-cost.md:240`);
- "two-thirds of older voucher holders report a disability (not in the register)" (`6-cost.md:142`), which is the basis for the unpriced stage 3 risk;
- the 57% search rate, which is tagged in section 7 but not where section 6 uses it (`6-cost.md:23`).

*Also:* `6-cost.md:158` cites EV-HOU-150 for "2% of households paid twice". That figure is GAO's (SRC-1061) and is not in EV-HOU-150's passage. Section 7 gives 0.2-0.5 million net new homes from the capital (`7-validation.md:91`), section 4 0.3-0.7 million (`4-specification.md:457`). Pick one.

*Fix:* tag the material ones as D or E register entries with their ranges, so the checker sees them.

**W-8. Handled well.**
- Second Trump administration analysis is presented as that administration's view and carries no recommendation: the Housing First order (EV-HOU-173), the HUD-funded rental aid evaluation, and the immigration reading kept out of the brief (`9-public-case.md:209`).
- The CAPABLE fade and the credits' crowd-out are disclosed.
- The 0.17-0.26 million added owners is labeled judgment.

### 2. Missing populations

**M-1. People leaving prison or jail have no route, and screening rules for the new awards are not set.** Not blocking.
- *Where:* the order of reach (`4-specification.md:135-147`) and the shared rules (`4-specification.md:84-102`). No section mentions reentry; the dossier's only mention of criminal records is the right to return in public housing redevelopment (`4-specification.md:481`).
- *Failure:* a man leaving prison to a relative's couch is a single adult, doubled up, so not in stage 1, whose doubled-up test covers families with children only (`DEC-2026-11-09-12`). If he leaves to the street, stage 1 takes him in principle. But the new awards run through housing agencies under current voucher screening, with its mandatory bans and the agencies' own criminal-record policies. So the plan's lowest-barrier design could still turn him away at the agency door.
- *Fix:* a section 4 rule limiting criminal-record screening for the new awards to the statutory minimum, as HOU-5.02 already does on return. Name people leaving prison, jails and other institutions with nowhere to go in HOU-4.03's plain test. Add the evidence to the register; none is there now.

**M-2. Young people leaving foster care are not named.** Not blocking.
- *Where:* the order of reach. Foster care appears only in down payment help's first-generation priority (`4-specification.md:595`).
- *Failure:* an 18-to-24-year-old aging out with no family to stay with is a single adult. They fall in stage 1 only if literally homeless. Current law's Foster Youth to Independence vouchers are not mentioned or built on.
- *Fix:* count youth leaving foster care without a home in stage 1's plain test, and note how the existing vouchers fit.

**M-3. Single adults and older renters who are not disabled still have no rental route in the 2030s.** Known and partly decided. Not blocking.
- *Where:* `4-specification.md:140`; `7-validation.md:20` (about 1.75 million older extremely low-income renters with severe problems); `7-validation.md:489`, question 7 (single adults and families just above the line, still open).
- *Failure:* the largest group with worst case needs, single nonfamily households at 2.80 million (`1-problem.md`, "Single adults"), gets only the emergency fund. Section 9 says so honestly (`9-public-case.md:73`, `:137`).
- *Fix:* Espen's section 7 question 7 is still open. It belongs on the "For Espen" list, not in a later section.

**M-4. Rural tribal areas: the USDA channel's reach onto trust land is unresearched.** Not blocking.
- *Where:* `4-specification.md:915` says Section 502 on trust land and USDA's Native American relending pilot are "not yet researched". The tribal set-asides (HOU-4.13) cover HUD money only.
- *Failure:* a tribal family on trust land in a rural county gets the HUD set-asides, but the plan's largest new rural buying channel (HOU-14.02) may not reach them, because loans secured on trust land are hard to underwrite (`4-specification.md:281`). Section 1 still has no rural or tribal figures (`1-problem.md`, "Still missing").
- *Fix:* the later step `4-specification.md:915` names, before L3 for HOU-14.02.

**M-5. Immigrant eligibility is unstated for the new owner and buyer programs.** Not blocking.
- *Where:* shared rule 3 (`4-specification.md:92`) covers HOU-4, HOU-4A and HOU-4D, and leaves HOU-1D to the immigration flagship. It says nothing for HOU-10.01, HOU-12.01, HOU-13.01 or HOU-14.
- *Failure:* those programs promise "a signed statement, no further papers". If default federal-benefit rules apply, each needs a status check, and that check is a document requirement the design says it doesn't have. It could also exclude mixed-status owner families the rental side protects (`DEC-2026-11-09-10`).
- *Fix:* add each new program to shared rule 3 with its working answer, and send the question to the immigration flagship's table.

**M-6. Disabled owners and older disabled renters.**
- *Disabled owners* are largely covered: the repair fund's accessibility work (HOU-12.01, HOU-12.04) and the tax match (HOU-13.01) both include disabled owners up to 80% of area median income. Nothing to fix.
- *Older disabled renters* are unpriced and undecided (`6-cost.md:142`, question 2), and they may be as many as the under-62 group. See "For Espen", item 3.

### 3. Optimistic assumptions

**O-1. Stage 1 may absorb the first million, so stage 2's count is probably understated.** Blocking (it moves the FY2040 and FY2041 tests).
- *Where:* stage 2's central count of 1.2 million rests on memo 2's split: HOU-4A's million reaches people without a home and "about half a million" of stage 2's families first (`3-design.md:155`, "this dossier's assumption"; `6-cost.md:96`).
- *The problem:* since `DEC-2026-11-09-12`, stage 1 has no cap and includes doubled-up families with children. Section 7 warned that stage 1 "could take every award and push stage 2 back" (`7-validation.md:16`). Section 5's timeline still says "2033: stage 1 served, stage 2 begun" (`5-delivery.md:180`).
- *Failure:* if the first million reaches few of stage 2's renter families, the remainder is nearer the full 1.717 million than 1.2 million. At section 6's own rates (85% apply, 90% lease, about $25,000 a family in FY2040; `6-cost.md:215`), that is roughly $9 billion a year more from FY2040. FY2041's margin is about $11 billion (`6-cost.md:19`). This is the reviewer's arithmetic, on section 6's inputs.
- *Fix:* section 6 restates stage 2's count with stage 1 uncapped, and shows a reading where the first million goes almost entirely to stage 1. Section 5 fixes the timeline row.

**O-2. Lease-up at 90%, central, against 67% in the only precedent measured the same way.** Not blocking for cost; blocking for how section 9 states reach (E-2).
- *Where:* `6-cost.md:34`, `:117-123`; `7-validation.md:59` ("at risk").
- *What holds:* section 6's case that 90% is the cautious case for the fiscal rule is right. Reporting households housed as a range (2.2-2.7 million) is also right.
- *What doesn't:* the 75% reading is the low end of that range. At EHV's 67%, or the 57% search-success rate, reach falls to about 1.5-2.0 million (`6-cost.md:107-108`), and the duty to house protects only stage 2 from 2037.
- *Fix:* none in the design. The public range should say what its low end assumes (E-2).

**O-3. The FY2041 pass is fragile, and section 9 states it without its conditions.** Blocking for section 9; not for the design.
- *Where:* `6-cost.md:19`, `:298`; `9-public-case.md:68`, `:113`.
- *What it rests on:* the margin is about $11 billion. It rests on the recovery budget's revenue path, whose tax rates are exploratory and whose financing is not adopted (`6-cost.md:318`, `ASM-REC-EXPLORATORY`). Interest on the added borrowing is left out (`6-cost.md:7`).
- *What it leaves out:* each of these is in the dossier and none is in the central case:
  - stage 2's count (O-1), about +$9 billion;
  - the credits' FY2040 run rate, which could be $22 billion rather than $15 billion (`6-cost.md:371`), +$7 billion;
  - stage 3 for disabled renters 62 and over, unpriced and possibly as large as the under-62 group (`6-cost.md:142`).
- *Failure:* any two of these erase the margin. Section 9's "From 2041 the rule passes" would then be wrong in public.
- *Fix:* section 6 lists these as named risks to FY2041 beside the high case. Section 9 says "passes on the central figures, which leave out ...", or drops the FY2041 line.

**O-4. Down payment help: the 1.4 million buyers assumes an average of $20,000, but the rule is the greater of $20,000 or 10% of price.** Not blocking.
- *Where:* `4-specification.md:596`; `6-cost.md:239`; `9-public-case.md:48`. The bill's text is "the greater of $20,000 or 10%" [EV-HOU-525].
- *Failure:* for any home above $200,000, 10% is more than $20,000, and a state may add 25% for new homes. There is no price limit on the home.
  - A buyer at 160% of area median income in a high-cost area, buying at $600,000, can receive $60,000-75,000.
  - With a fixed $28.5 billion, the average is likely well above $20,000, so the count of buyers is likely well below 1.4 million.
  - The money concentrates in exactly the expensive markets where the London and Bavaria evidence says buyer help raises prices [EV-HOU-545] [EV-HOU-546].
- *Fix:* section 6 recomputes the buyer count at a realistic average price, and section 9 follows. Whether to cap the amount is for Espen ("For Espen", item 4).

**O-5. Staffing and build pace.** Not blocking; for section 5.
- *HUD:* the plan launches at once 250,000 awards a year, a new lending office for $300 billion of loans, an emergency-fund network, the repair fund and new reporting duties.
  - HUD lost about 2,500 staff in 2025 and hired 193 [EV-HOU-340].
  - Its staffing after the rebuild surge "has no settled line" (`5-delivery.md:54`).
  - The 0.5% set-aside is the only assured federal staffing for these programs.
- *Rural Development:* the plan adds about 2,000 staff in three years (`4-specification.md:827`) while scaling direct loans five- to seven-fold. Nearly a fifth of the existing direct portfolio is delinquent; that figure comes from a news investigation, not an official release [EV-HOU-701].
- *Revolving funds:* states run the funds at $10-11 billion a year from 2032 with no evidence of readiness (`5-delivery.md:89`). The four-year spend-out (`6-cost.md:54`) is judgment.
- *Fix:* section 5 gives each new program a staffing number and a hiring path, and says which launches move a year if hiring lags. Section 6 gives a slower-spend reading for the capital.

**O-6. The budget model has not run the plan.** Blocking (L3's cost part).
- *Where:* `6-cost.md:9-10`, `:374-401`. The model's benchmarks have not all passed. The provision-level figures are arithmetic, not a score. The 13 changes are proposals.
- *Fix:* the tier-3 ledger PR, then a model run of FY2040-42 and the high case.
- **Done (fix step 7):** the tier-3 PR books section 6's provisions and the models are rerun. The model books housing at $0.81 trillion over FY2030-39 and $111 billion of permanent cost in FY2040. Plan-wide, the recovery budget's FY2040 balance goes from a $4.5 billion margin to a $50.8 billion shortfall, FY2041's from $49.6 billion to a $7.3 billion shortfall, and FY2042 keeps a $37.8 billion margin (`6-cost.md`, 3.2). The high case stays section 6's arithmetic, since the model computes midpoints only (`ASM-CALIB-MID`). Under `DEC-2026-11-10-05` these readings go to the financing settlement.

**O-7. Prices under buyer subsidies, and the FHA cut.** Not blocking.
- *Down payment help:* the price watch is a review trigger, "well above their region's for two years" (`4-specification.md:605`). It has no number, and it reads prices only after two years.
- *FHA cut:* the premium cut goes to every FHA purchase loan, about 650,000 a year, with no income or price limit (`6-cost.md:240`). It is permanent, at about $3 billion a year from FY2040.
- *Evidence:* the register has no estimate of how many added owners either produces in the U.S. The 0.17-0.26 million added owners is judgment (`6-cost.md:239`).
- *Fix:* a numeric trigger in section 8, and the FHA question under "For Espen", item 4.

### 4. Cheaper alternatives

**A-1. The rural high-cost credit boost mostly duplicates what states can already do.** For Espen, item 2.
- Current law already lets a state housing credit agency give the 30% boost to any building it designates, except bond-financed ones [EV-HOU-461]. Most rural tax-credit buildings are 9% deals inside the state's cap, so they can already get it.
- A statutory rural designation adds the boost automatically, so it needs no state judgment. But within a fixed 9% allocation, more credit per rural home means fewer homes elsewhere in the same state.
- Its only new reach is rural bond-financed buildings. Section 6 does not price it, and section 4's count of 40,000 homes for the rural and tribal boosts together is judgment (`4-specification.md:439`).
- The cheaper path: leave the rural boost out, and publish each state's use of its existing designation power in rural areas.

**A-2. Down payment help with a flat cap.** For Espen, item 4.
- A flat cap of $20,000-25,000, as the 2021 bill and most state programs use, would reach more buyers for the same $28.5 billion, and less of it would go into prices in tight markets (O-4).
- A second option: a price limit at FHA's area loan limit, the rule HOU-3C.05 already uses for its homes for sale (`4-specification.md:631`).

**A-3. Time-limit the FHA premium cut.** For Espen, item 4.
- It is the only permanent line in memos 9-10 (about $3 billion a year from FY2040; `6-cost.md:247`).
- A cut through FY2039 with a renewal review would take about $3 billion off the FY2040 gap and keep the help through the decade.

**A-4. Search help: fund the cheapest proven core first.** Not blocking.
- Search help is $8 billion (3-17) at $2,000 an award, "pending the design research section 4 still owes" (`6-cost.md:37`).
- Until that research lands, the cheaper course is to fund the parts with evidence: pre-inspection, already law [EV-HOU-232]; deposits and fees; and the Seattle and King County counseling model [EV-HOU-091]. The rest can be added on the evaluation.

**A-5. What is already the cheaper path, and should stay.**
- Rural Development's staff at about $0.35 billion a year buy most of the rural channel's reach (`6-cost.md:291`).
- The FY2029 bridge counted inside the plan's money (`DEC-2026-11-10-01`).
- Tribal set-asides as shares of existing money.
- The repair fund without a whole-house code standard (`4-specification.md:696`).
- Each is a cheaper design reaching most of the same people. No change.

### 5. Design lens (`DEC-2026-11-09-13`)

The dossier applies the lens well. Section 4's list of simplifications (`4-specification.md:12-19`) is real:
- one plain test for stage 1;
- self-statements with checks after award;
- government records as proof of disability;
- an annual cap in place of episode limits;
- counseling offered, not required;
- review triggers in place of quotas throughout HOU-10 to HOU-14.

Four places where a requirement's burden is not yet shown to earn its place, or where a check could still cost a family its help:

**L-1. "Checked after award" never says what happens when a check fails.** Not blocking, but fix before L3.
- *Where:* stage 2's severe-problems statement (`4-specification.md:317`) and deemed approval (`4-specification.md:326`) are both checked after award. The emergency fund says errors are recovered from grantees, "never by evicting tenants over honest mistakes" (`4-specification.md:380`), but the guarantee has no such rule.
- *Failure:* a later administration uses post-award checks to end help for families whose statement was honest but imprecise.
- *Fix:* write HOU-1D.03's rule into HOU-4D.01. Help ends only for fraud, and honest errors are corrected going forward.

**L-2. The production target's state shares (For Espen, item 1).** A share of the count for each state is close to a quota, which the lens disfavors. It only earns its place if it does a job; here, its one job is to trigger the federal builder.

**L-3. The landlord loans' rent term.**
- *What it asks:* yearly rent increases at or below the lower of 5% or inflation for three years, tracked per unit (`4-specification.md:716`).
- *Why it may not earn its place:* it is lighter than Pennsylvania's rules, which left that program nearly unused [EV-HOU-655], but it is still a compliance task for small landlords and grantees, with no evidence of its own.
- *Fix:* section 8 watches take-up; if loans go unused, drop the term to a no-pass-through rule only.

**L-4. HOU-4.04's tight-market test runs two measures plus a list, and its data are missing in rural places.**
- *What it asks:* vacancy at or below 4% for two years, or lease-up under 50% in 180 days (`4-specification.md:152`). Nonmetro counties have no annual vacancy reading (`4-specification.md:161`).
- *Why it matters:* this is acceptable, since it binds HUD, not families. But the lease-up test alone would be simpler and works everywhere.

### 6. Internal consistency

Amounts, limits and statuses for every decided parameter agree across sections 4-9, `provisions.json` and `charter/decisions.md`. The subagent checked about 30 parameters; the reviewer spot-checked a third. No HOU agenda row claims L3, and every provision's parent row exists. The problems are stale figures and open items that are not where Espen will see them.

**C-1. Section 3 does not record its decisions.** Blocking for L2's record.
- *What it still says:* forks 1-8 end in "Recommendation" with no "Decided" line (`3-design.md:126`, `:180`, `:236-238`, `:279`). Fork 3 part 1 still recommends 3.1B, though Espen chose D (`DEC-2026-11-09-08`).
- *Stale text:* "How the choices fit together" says "a narrower tax credit" and "Before section 4. Each piece waits on Espen's decision" (`3-design.md:459`, `:463`). The "Questions for Espen" list at the end is all decided.
- *Missing:* memo 3b and memo 13 have no pointer in section 3. The addendum parts 1 and 2 do carry "Decided" lines (`3-design.md:440`, `:447`).
- *Fix:* add a "Decided" line to each fork, as the addendum has, and an addendum pointer for memo 13.

**C-2. Open items are more than the two the board names.** Blocking for L3. The board and README name two parameters "still proposed" (`charter/PROGRESS.md:36`; README open question 1). Still open in the dossier:
- HOU-1D.04: whether HOU-1A's construction gap money is dropped or added to HOU-3C (`4-specification.md:389`, `:994`). `provisions.json` and the glance table (`4-specification.md:44`) call it "decided".
- Section 6, questions 2, 3, 4, 6, 7 and 8 (`6-cost.md:428-434`): stage 3 at 62 and over, stage 3's severe-problems test, the emergency fund's size, the zoning reward after 2039, stage 2's take-up assumption and the fee rate. Each changes cost or coverage. None has a `DEC-` entry, and section 6 prices its recommendation as if adopted.
- Section 7, questions 7 (single adults and families just above the line), 8 (a social housing pilot target) and 9 (child care and voucher rent) (`7-validation.md:489-491`).
- *Fix:* one consolidated list for Espen, in the README and on the board. "For Espen" below recommends an order.

**C-3. Stale headlines in the README.**
- `README.md:32` gives section 6 as $0.65 trillion, $90 billion and a $20-28 billion gap; the current figures are $0.78 trillion, about $96 billion and $26.4-37 billion.
- `README.md:30` says "35 provisions"; there are 56.
- `README.md:3` and `:10` stop at `DEC-2026-11-09-11` and HOU-9; memos 9-13, HOU-10 to HOU-14 and `DEC-2026-11-10-01`/`-02` are missing.
- Not blocking, but the README is what a cold session reads first.

**C-4. Stale figures in sections 4, 6, 7 and 8.** Not blocking. Fix each in place.

| Where | Says | Current |
| --- | --- | --- |
| `4-specification.md:967` | FY2040 about $90 billion | about $96 billion |
| `4-specification.md:992` | $0.65 trillion and $90 billion | $0.78 trillion and about $96 billion |
| `6-cost.md:364` | gap "stays at about $20 billion ($28 billion)" | $26.4 billion ($37 billion) |
| `6-cost.md:427` | gap "on this revision's figures" $20/28 billion | $26.4/37 billion |
| `6-cost.md:14-15` | opens on $0.65 trillion and $90 billion, reaching $0.78 trillion only at the end | Lead with $0.78 trillion (about $0.59-1.10 trillion) and about $96 billion, then show the steps |
| `8-change-our-minds.md:148` | $20 billion and $28 billion, unlabeled | $26.4 billion, $37 billion; FY2041 about +$11 billion |
| `8-change-our-minds.md:159` | tribal shares about $13 billion | about $14 billion |
| `7-validation.md:385`, `:391` | $0.77 trillion, $26/36 billion, FY2041 +$12 billion | memo 13 omitted: $0.78 trillion, $26.4/37 billion, +$11 billion |

**C-5. Statuses still "proposed" for decided items.**

| Where | Says | Current |
| --- | --- | --- |
| `7-validation.md:134-135`, `:467`, `:487` | production targets proposed | decided, `DEC-2026-11-09-17` |
| `5-delivery.md:342` | tribal sizes proposed | decided, `-16` |
| `5-delivery.md:220` | the wider backstop is "a question for Espen" | decided, `-10` |
| `provisions.json`, HOU-4A.01, HOU-1D.03, HOU-3C.01 | tribal shares "proposed 3%" and "proposed 5%" | decided |
| `provisions.json`, HOU-1D.01 | keeps the old episode limits beside the annual cap that replaced them | annual cap only |
| `4-specification.md:48`, `:56` (glance table) | "Decided" for HOU-3C.04 and HOU-2D.01 | each still has a part proposed, for Espen |

Not blocking.

**C-6. Smaller items.**
- Section 6's FY2040 figures "79" and "90" mean different things in the table, where they are spending only (`6-cost.md:80`), and in the brief, where they include credits (`6-cost.md:15`).
- `road-funding.md:37` gives HOU-11.01 at $350 million through FY2039; FY2039 is $150 million.
- The agenda's HOU-10 note still says a "135-150%" income limit, without `DEC-2026-11-09-24`'s 140% and 160%.
- Not blocking.

### 7. Section 9 against sections 1-8

Section 9 follows the dossier closely: almost every number in the brief traces to section 6 or 4, and its "can say / can't say" table is a model of restraint. Four places run ahead.

**E-1. The FY2040 gap is not "mostly" the three items named.** Blocking for section 9.
- *Where:* `9-public-case.md:113` says the gap is "mostly from opening stage 2 to families with no home of their own, FHA's lower premium and the property-tax match".
- *What section 6 says:* those three are about $14 billion of $26.4 billion. Section 6 names stage 3 "the largest single reason" (`6-cost.md:146`); the standing emergency fund and stage 2's true timing are the rest (`6-cost.md:15`, `:342`). Line 68 lists the three without "mostly", which is accurate.
- *Fix:* name the largest pieces, or drop "mostly".

**E-2. "It reaches about 2.7 million households" breaks section 9's own rule.** Blocking for section 9.
- *Where:* `9-public-case.md:123` and `:73` say 2.7 million alone. The can-say table forbids "2.7 million alone, as a sure thing" (`9-public-case.md:146`).
- *Fix:* say "about 2.2 to 2.7 million", here and at line 73.

**E-3. "From 2041 the rule passes" needs its conditions.** Blocking for section 9 (O-3). Fix: `9-public-case.md:68`, `:113`.

**E-4. The one-paragraph case and the can-say table say $0.77 trillion; the brief says $0.78 trillion.** Not blocking (`9-public-case.md:87`, `:149`).

**E-5. Figures that are judgment are stated as facts** (W-1). Blocking for section 9: the emergency fund's 1.4 million a year, the 1.4 million buyers (O-4), the repair count, the tax match's $3 billion and the 1.0 million net new homes.

**E-6. "Within what other rich countries spend on housing allowances."** Not blocking.
- *Where:* `9-public-case.md:66`, `:111`.
- *The problem:* the about $96 billion includes tax credits, an FHA premium cut and a property-tax match. Those are not housing allowances, the OECD category of [EV-HOU-159]. The comparison holds for the rental help alone.
- *Fix:* compare the rental help lines only, or say "housing support".

## For Espen

Plain words, with options. Each is your call; the review recommends one.

**1. How to count each state's share of the "homes the plan pays for" target** (held for this review; `4-specification.md:462`).
- *What it does:* the target is about 1.3 million homes over 2030-39. The state share matters for one thing: the small federal builder may build only where a state has "missed its share" (HOU-9A.01). The share is never a reason to withhold money.
- *The options:*
  - **(a) As proposed:** each state's share of homes equals its share of the money. It is simple, but money buys fewer homes where building costs more. California or New York would "miss" every year and Mississippi would not, so the builder trigger would fire by cost, not by effort.
  - **(b) Recommended:** each state's expected count is its money divided by its own cost per home, from the cost reports state agencies already file for tax-credit buildings. A state "misses" when it finishes well under that count for two years running. It is fair across high- and low-cost states and adds no new paperwork.
  - **(c) No state shares:** publish each state's homes and cost per home. HUD picks the builder's sites from the tight-market list after a published review. This is the lightest, but it gives the builder no clear trigger.

**2. The rural high-cost credit boost** (held for this review; HOU-2D.01, `4-specification.md:551`).
- *What it would do:* call rural areas "high-cost" so their tax-credit buildings automatically get 30% more credit.
- *What current law already does:* states can already give that boost to any rural building that isn't bond-financed [EV-HOU-461], and most rural tax-credit buildings aren't. Within each state's fixed credit amount, extra credit for rural homes means fewer homes elsewhere in the state. It has not been priced, and its home count is a guess.
- *The options:*
  - **(a) Recommended: leave it out,** and have states publish how often they already use the boost in rural places. If rural deals still don't get built, revisit in the 2034 credit review.
  - **(b) Add it as proposed:** automatic, for every rural building.
  - **(c) Add it for bond-financed rural buildings only,** the one group states can't help today.

**3. Stage 3 for disabled renters: does it include people 62 and over, and does it use stage 2's "severe problems" test?** (`6-cost.md`, questions 2 and 3, still open).
- *Why it matters:* this is the largest unpriced cost in the plan. Including older disabled renters could roughly double stage 3, adding perhaps $9-14 billion a year from about 2040. It would also cover many of the older renters the plan otherwise leaves out.
- *The options:*
  - **(a)** Under 62 only, as priced.
  - **(b) Recommended:** include 62 and over, keep the severe-problems test shown by the household's own statement, and price it before the financing settlement.
  - **(c)** Decide with the care flagship and leave stage 3 unspecified until then. That keeps stage 3 at L2.

**4. Should first-time buyer help be capped?** (A-2, A-3, O-4).
- *What the rule says now:* up to $20,000 or 10% of the price, whichever is more, with no price limit.
- *What that means:* a high-income buyer of an expensive home can get $60,000 or more. The fixed $28.5 billion then helps fewer people, mostly in the costly markets where help raises prices most.
- *The options:*
  - **(a)** Keep it as is.
  - **(b) Recommended:** a flat cap of $25,000, or $30,000 for a newly built home, plus FHA's loan limit as the most the home can cost. It reaches more buyers and pushes prices less.
  - **(c)** Keep 10% but add the price limit only.
- *A related choice:* make FHA's lower premium run through 2039 with a review, instead of permanently. That would take about $3 billion a year off the 2040 gap.

**5. Six other open questions that change cost or coverage.** They are in section 6 (questions 4, 6, 7 and 8), section 7 (questions 7, 8 and 9) and section 4 (HOU-1D.04). Each has a recommendation in its section, and none is decided yet. The lead can put them to you as one short list.

## What the next steps should do (for the lead)

In order; each is small.
1. **Record and refresh.**
   - Section 3: add the "Decided" lines (C-1).
   - README and board: refresh the README and put every open item on one list (C-2, C-3).
   - Sections 4-8 and `provisions.json`: fix the stale figures and statuses (C-4 to C-6).
   - Tier: Standard. One routine PR.
2. **Section 6 and 5 fixes.**
   - Section 6: stage 2's count with stage 1 uncapped (O-1); named risks to FY2041 (O-3); the buyer count at a realistic average (O-4); a slower capital spend reading (O-5).
   - Section 5: the timeline row, and staffing numbers by program (O-5).
   - Tier: Most capable.
3. **Section 4 additions.**
   - Reentry and foster youth in the plain test, with screening limits (M-1, M-2).
   - Immigrant eligibility for the new owner programs (M-5).
   - Honest-error protection in HOU-4D.01 (L-1).
   - The evidence these need.
   - Tier: Most capable.
4. **Section 9** follows steps 2 and 3 (E-1 to E-6, W-1, W-6).
5. **Evidence register tidy-up** (W-3, W-4, W-7): tag OMB's subsidy rate with its administration and a CBO check; regrade the letters and the USICH announcement; add D or E entries for section 6's material judgments. Tier: Standard.
6. **Espen's answers** to "For Espen" items 1-5, recorded as `DEC-` entries.
7. **The tier-3 ledger PR and a model run** (O-6). This is the last L3 blocker. **Done** (`6-cost.md`, 3.2). Then a short L3 re-check by a reviewer, limited to the blocking findings above.
