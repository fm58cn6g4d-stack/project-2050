# Stage G step 8c: the debt-path rule, the debt limit and the central rules

Role: the budget-process part of the fiscal path review (`DEC-2026-11-24-14` to `-18`), the last part of stage G step 8. It designs the debt-path rule that memos G15 B and G19 B lean on, keeps the debt limit apart from it, examines the central rules (D3, D4 and D4-B), and reads fiscal rules abroad and the US record as evidence for the design. Its forks are memos G20 to G22, **decided November 25, 2026** (`DEC-2026-11-25-06` to `-11`): G20 B, G21 A and yes to each of G22's four points. The strategy memo is [`6-strategy-memo.md`](6-strategy-memo.md). Status: **stage G step 8c, November 24, 2026; G20 to G22 decided November 25 and written in by step 9** (part 6.1 is D4's rewrite and D3's new test years as proposal text). The rule's path follows G15's redraft, memo [G23](memos/G23-debt-path-redraft.md), provisional until Espen confirms it in batch 4 ([`7-batch3-revision.md`](7-batch3-revision.md)). **Nothing here is booked, and nothing new is priced here:** every figure for the plan comes from step 8a ([`4-fiscal-path.md`](4-fiscal-path.md) parts 1-2, #483) or step 8b (parts 3-6 and memos G15-G19, #484, merged). This PR also carries the three non-blocking fixes from #484's review to G15, G17 and G19, at the lead's request.

Units: federal fiscal years, nominal $B or % of GDP. Project arithmetic on exploratory models, not official scores.

**The rules this part keeps** (Espen's directions, `DEC-2026-11-24-14` to `-18`): a populist start in 2029 with no early middle-class revenue (`-18`); no VAT (`DEC-2026-11-20-07`); Social Security's and Medicare's long-run finances out of scope (`-16`); and step 8a's hard rule, that a debt goal is met on the conventional score, with "works as designed" and dynamic savings counted only once they show up in measured results.

## In plain terms

1. **What the rule is for.** Memo G15 B holds debt flat at about 117% of GDP from FY2040 and steps it toward 100% "as results allow". Memo G19 B enacts later broad revenue early, with steps the rule can cancel. Both need a rule that says what "results allow" means, who decides and what happens in a recession.
2. **The recommended rule (G20 B)** sets a path for debt as a share of GDP and enacts G19's revenue steps in the first Congress, on by default. Each October the trustees certify two measured facts: where debt ended the year against the path, and whether a recession test has tripped. When debt runs a point below the path for two years, half the lead lowers the path for good, and the other half can defer a tax step or lower the health contribution. When debt runs a point above, nothing is cut automatically: deferred steps take effect, and the President must send a plan that Congress votes on under a fast-track procedure. In a recession or declared emergency the rule stands aside.
3. **It doesn't make the goal cheaper.** On CBO's rates the ladder's money is all needed to hold debt flat, so the rule defers nothing and moves nothing toward 100%. Debt goes below about 117% only if results beat CBO's assumptions: rates below CBO's, or health costs below D2's cap. If rates run a point higher, the ladder falls 1.3 to 1.6 points of GDP short and the return procedure starts.
4. **Why no automatic cuts.** The one US rule that cut by formula against deficit targets, Gramm-Rudman-Hollings, was missed every year it ran and was evaded with timing tricks (part 2.1). Rules that cut automatically tighten in bad years, and a later Congress that wants smaller programs could use the formula as cover. The rules that have worked best, the 1990 Budget Enforcement Act at home and expenditure rules abroad, control what each new law does, measure the cycle and keep a recognized escape clause.
5. **Four promises meet in one place.** G15 B, G16 B, G18 D′ and G19 B each promise to use "results beating the path": to lower debt, to lower the health contribution, and to cancel tax steps. As written, they promise the same dollar three times. The rule sets the order: half to lower the path, then defer a tax step not yet started, then lower the health contribution, then suspend a step already in force. The lead should see this before #484 goes to Espen (part 7).
6. **The debt limit is a separate question.** The limit governs paying bills Congress has already run up, not new spending, and it now stands at $41.1 trillion, to be reached again in FY2027 on CRS's reading [EV-FIN-016] [EV-FIN-017]. The recommendation (G21 A) is to repeal it in 2029, by regular order under the Senate's decided graduated-cloture rule, and let the debt-path rule be the anchor. A delegated suspension (the 2011 model) is the fallback. The Fourteenth Amendment and the platinum coin are last-resort arguments with real legal and market risk, not a plan.
7. **The central rules.** Three changes are offered as forks (G22): extend D3's household test to the mature years, since the later broad revenue lands there; replace D4's debt guardrail against CBO's current-law path with the debt-path rule; and give investment no standing carve-out after FY2039, with room earned only while debt is on its path.

## Part 1. What the rule has to do

**What leans on it.**
- **G15 B** (debt held flat as a share of GDP from FY2040, at about 117%): "then stepped toward 100% by a debt-path rule as results allow". It costs 0.85% of GDP in FY2040 and 1.03% in FY2056, about $461B and $982B; nothing at r − g of −0.5 and 2.1-2.4% of GDP at +1.5 (`4-fiscal-path.md` part 3).
- **G16 B** (the health contribution's base rate R held at 3.80% to FY2040, then lowered toward 3.25% by a trigger on certified savings) and **G18 D′** (G8's step-down measured against the debt goal's path): both step R down "only when the trustees certify a surplus beyond the debt goal's path".
- **G19 B** (from FY2037, itemized-deduction limits and a larger carbon fee first, an AGI surtax from FY2040 if needed, R last): "each step can be switched off by the debt-path rule if results beat the goal". About $430-460B in FY2040.
- **G13 A** (decided, `DEC-2026-11-24-08`): if D2 misses, R steps up a quarter point a year. It is already in law text (`2-settlement.md` part 7.1). The debt rule must not count the same overrun twice.
- **Step 8a's rate stress** (`4-fiscal-path.md` part 1.5): a shock of 100 to 200 basis points from FY2035 lifts FY2056 debt on the booked path to 157-186% and "undoes any goal unless the plan responds". 8a named "a trigger … that steps up automatically if the average rate on the debt runs a set margin above the plan's assumption" as the case for this part.

**What it must not do.**
- Ask anything of the middle class before the ladder's dates (`-18`).
- Cut programs by formula. A cut that waits for debt to run high lands in the years after a shock, and a hostile Congress could use it as cover (the brief; part 2).
- Count dynamic or "works as designed" savings before they show up (the hard rule).
- Touch Social Security's or Medicare's long-run finances (`-16`). The trust funds' surpluses lower debt held by the public (`4-fiscal-path.md` part 1.1); the rule measures debt that way, as 8a does, and sets its path knowing the trust funds' scheduled flows. After FY2056, as the Social Security reserve is drawn down, that reading will need revisiting at the rule's ten-year review.

**Three tensions it has to settle.**
1. *Measured or projected.* Measured results can't be gamed with a forecast, but they arrive late, and a tax step has to be decided a year before it starts. The rule uses measured debt for every test, and allows a projection only as a second lock on a giveback, never to trigger one.
2. *Credible or flexible.* A step that is on by default is scored and believed; a step that needs a vote to start isn't. But a default-on step in a recession is procyclical. The escape clause settles it.
3. *Who gets the upside.* Paying debt down and giving money back draw on the same gains (point 5 above). The rule has to say in what order.

## Part 2. What the record shows

### 2.1 The United States

| Rule | What it did | What happened | Lesson for the design |
| --- | --- | --- | --- |
| **Gramm-Rudman-Hollings** (1985, 1987) | Deficit targets each year, enforced by automatic across-the-board cuts | FY1991's target was $64B; OMB's estimate was $147.3B, which would have cut defense and nondefense programs by $41.7B each [EV-FIN-051]; facing it, the President and congressional leaders agreed a five-year, $500B deficit reduction plan [EV-FIN-084]. The deficit was measured in one August "snapshot", so outlays could be moved outside it, and one-time asset sales could meet a target with nothing lasting changed [EV-FIN-052]. In every year the law ran the deficit exceeded its legal target, on one scholar's account (Allen Schick, 1997) [EV-FIN-053]. The 1987 act pushed the balanced-budget date from FY1991 to FY1993 [EV-FIN-052]. | Targets on an annual outcome, enforced by cuts, invite timing games and are dropped when they bite. |
| ***Bowsher v. Synar*** (1986) | Struck GRH's trigger: the Comptroller General, removable by Congress, "may not be entrusted with executive powers" [EV-FIN-054] | Congress moved the trigger to a report by OMB's director [EV-FIN-084] | Whoever certifies a trigger that executes the law must be an executive officer. CBO and GAO can check; they can't certify. |
| **Budget Enforcement Act** (1990-2002) | Caps on discretionary appropriations and pay-as-you-go for new laws, in place of deficit targets; PAYGO didn't reach laws already in effect [EV-FIN-083] | Schick (1997): GRH failed because it targeted the deficit, and the BEA succeeded because it didn't [EV-FIN-053]. It effectively ended when Congress zeroed the PAYGO balances in December 2002 [EV-FIN-083] | Control what each new law does, not the outcome. This is D4's logic too. One scholar's view; no CBO or GAO assessment was found. |
| **Statutory PAYGO** (2010) | A sequester if new laws add to the deficit | Never once ordered; about $12.07T excluded or wiped from the five-year scorecard and $17.07T from the ten-year since 2010 [EV-FIN-055] | A sequester Congress can switch off is switched off. Don't rest the rule's force on one. |
| **Budget Control Act** (2011) | Discretionary caps, and a sequester when the "supercommittee" failed | Congress raised the caps three times (2013, 2015, 2018), by $439B over 2014-19 (CBO) [EV-FIN-056] | Caps held in rough form but were renegotiated whenever they bound. |
| **Scheduled changes** | Laws that schedule a later tax rise or cut | The medical device tax was suspended twice and repealed in 2019 [EV-FIN-058]; 17 laws overrode Medicare's scheduled physician cuts from 2003 to 2014 [EV-FIN-057] | The ladder's real risk. Part 3.2 answers it. |
| **Automatic stabilizers** | Taxes fall and benefits rise in a downturn, with no vote | CBO: they raised deficits by about 0.3% of potential GDP a year on average over 1976-2025, and are projected to lower deficits by 0.2% in 2026-29 [EV-FIN-059] | They are the rule's best friend: let them run, and keep the rule out of their way. |

### 2.2 Abroad

| Country | The rule | Credibility | Procyclicality | Gaming |
| --- | --- | --- | --- | --- |
| **Switzerland** (debt brake, 2003) | Ordinary spending capped at receipts adjusted by a cyclical factor [EV-FIN-031]; overruns booked to a compensation account; extraordinary spending needs a qualified majority of both chambers and is repaid over six years [EV-FIN-032] | The federal debt ratio fell from 25.3% (2003) to 13.5% (2019), though the administrator itself credits growth and receipts too [EV-FIN-033]. Adopted by referendum. | Built to avoid it: the cyclical factor lets the stabilizers run. | The extraordinary channel is the release valve; COVID's repayment deadline was extended to 2035 [EV-FIN-033]. The rule's own administrator is the source. |
| **Sweden** (surplus target, expenditure ceiling, debt anchor) | Net lending of one-third of 1% of GDP over a cycle, balance from 2027; a 35% debt anchor [EV-FIN-034] | A deviation must be explained in the budget with a route back to the target, and an independent Fiscal Policy Council assesses it [EV-FIN-035] | The government's own reason for a cycle-average target: an annual one "would need to be pro-cyclical" [EV-FIN-034] | "Comply or explain" works where the political culture honors it. |
| **United Kingdom** (fiscal rules, OBR since 2010) | Current budget in surplus in 2029-30; debt (net financial liabilities) falling by 2029-30; the Chancellor may suspend them in a shock after asking the OBR [EV-FIN-036] | The OBR's forecasts are the anchor. When the September 2022 "mini-budget" went ahead without one [EV-FIN-038], the Bank of England had to buy gilts, warning of "a material risk to UK financial stability" [EV-FIN-039] | The OBR calls today's margins "very small" against forecast uncertainty (£15B) [EV-FIN-040], so every forecast change forces a reaction. | The charter doesn't define a shock, so suspension is the Treasury's call, and long forecast horizons let debt rise for most of the period (Institute for Government) [EV-FIN-037]. Rules defined on forecasts are only as good as the forecaster. |
| **European Union** (revised framework, April 2024) | One indicator, net expenditure, which automatic stabilizers don't affect [EV-FIN-041]; debt must fall at least 1 point a year above 90% of GDP and half a point between 60% and 90% [EV-FIN-042]; general and national escape clauses [EV-FIN-043] | Too new to judge. Under the old rules, national rules were met about half the time in 1995-2015 (IMF) [EV-FIN-047] | Designed to leave room for counter-cyclical policy [EV-FIN-041] | The national clause was activated for 15 states' defense spending in July 2025, up to 1.5% of GDP a year to 2028 [EV-FIN-043]: a category carved out by vote. |
| **Germany** (2025 reform of its debt brake) | A €500B infrastructure fund outside the brake; defense above 1% of GDP excluded; the Länder allowed 0.35% of GDP [EV-FIN-049] | The Bundesbank: with unlimited room for defense borrowing, sound finances "are not guaranteed" [EV-FIN-050] | — | The broader the definition of investment, the more likely its protection "would prove ineffective" (Bundesbank) [EV-FIN-050]; nothing requires the new room to go to productive investment (European Commission) [EV-FIN-049]. |

**Across countries** (the IMF's staff, who generally favor rules; one publisher, so these entries corroborate each other only where an independent source does too):
- Nominal deficit caps are "potentially procyclical", forcing cuts in bad times without stopping loosening in good ones; expenditure ceilings avoid that in good times [EV-FIN-045]. Sweden's government reaches the same conclusion [EV-FIN-034].
- Without well-designed escape clauses, rules are "put in abeyance" after large shocks [EV-FIN-046].
- Measuring the cycle has no agreed method, which "opens avenues to circumventing the rule" [EV-FIN-046]. That is why the rule here uses a measured unemployment test, not an estimated cyclically adjusted balance.
- Rules without political buy-in invite creative accounting and off-budget operations, and formal compliance has squeezed public investment and social spending [EV-FIN-044].
- Countries with more independent fiscal councils have smaller deficits and better compliance [EV-FIN-048]. The US already has one in CBO, so the design gives CBO the cross-check role the OBR and the Swedish council play.

**What the design takes from the record.**
1. **Test measured outcomes over a cycle, or control legislation; don't test annual forecasts.** GRH and the UK show what forecast-based annual tests invite.
2. **No automatic cuts.** GRH's sequester and statutory PAYGO's were never allowed to bite; the threat was supposed to work and didn't.
3. **A measured escape clause, named in advance.** The IMF's finding, and the cost of the UK's undefined "shock".
4. **No standing carve-outs.** Germany's and the EU's are the current lesson.
5. **An independent check.** CBO's reading published beside the trustees', with no legal effect of its own (*Bowsher v. Synar*; part 3.8).

## Part 3. The debt-path rule, as decided (memo G20 B, `DEC-2026-11-25-06`)

Plain version first, then the specification.

**In one paragraph.** The law sets a path for debt held by the public as a share of GDP: from FY2040, flat at the FY2039 level (about 117%, G15 B). It also enacts, in the first Congress, the later broad revenue G19 B lists, each step on a date and on by default. Each autumn the trustees certify two measured numbers: where debt ended the fiscal year against the path, and whether the economy is in a recession by a published test. If debt has run at least a point below the path for two years, half of that lead lowers the path for good, toward 100%, and the other half may defer a revenue step not yet started or step the health contribution down. If debt runs a point above the path for two years, nothing is cut automatically: every deferred step takes effect, and the President must send a plan to get back on the path, which Congress votes on under a fast-track procedure. In a recession or a declared emergency the rule stands aside: no step starts, the automatic stabilizers run, and the path restarts from where debt stands two years after the recession ends.

### 3.1 Target and measure

1. **The measure** is federal debt held by the public at the end of each fiscal year (Treasury's September figures), divided by nominal GDP for that fiscal year (the Bureau of Economic Analysis's four quarters). It is 8a's measure (`4-fiscal-path.md` part 1.1), so the trust funds' surpluses lower it. Both numbers are measured, not projected, so the test can't be met with an optimistic forecast.
2. **The path, FY2040 on:** as drafted, the measured ratio for FY2039 (on the booked path, 116.9%), held flat. Espen asked for G15 B to be "a little more aggressive on debt" (`DEC-2026-11-25-01`), so the path is redrafted as a falling one in memo [G23](memos/G23-debt-path-redraft.md); the rule's mechanics below don't change with it, only the path they measure against.
3. **The ratchet toward 100%:** the path only moves down (part 3.3), never up except by the escape clause's restart (part 3.6) or by a new law. At 100% it stops: further gains are returned (part 3.3) until Congress sets a new path. The rule is reviewed by law every ten years, the first in 2041, with CBO's long-term outlook.
4. **Before FY2040** the rule is in force only for the ladder's start dates (part 3.2). The trustees publish debt against the booked plan's path from FY2030, as a dry run, so the first real test isn't the first time anyone sees the table. D4-B's arc governs FY2030-39 as decided (part 6).

### 3.2 The ladder: revenue steps enacted early, on by default

The steps are G19 B's, in its order, enacted in the first Congress with their dates in law:
- **Step 1, FY2037:** limits on itemized deductions beyond C39, and a larger carbon fee with the dividend kept (about $230-460B in FY2040 between them; G19's table).
- **Step 2, FY2040:** an AGI surtax (about $167-225B).
- **The health contribution's base rate is not a ladder step.** It moves only by G13's backstop (if D2 misses) and by G16 B and G18 D′'s step-down, which this rule's finding drives (part 3.3).

**On by default.** A step takes effect on its date unless a finding defers it. That is what makes the money count: a step in law is in CBO's current-law baseline and in the plan's score, and a later Congress has to vote to stop it rather than vote to start it. A step that waits for a finding to switch it on is scored at zero and is easily never switched on.

**The ladder's real risk is that a later Congress delays it.** Scheduled increases in US law have a poor record: the medical device tax was suspended twice and then repealed [EV-FIN-058], and Medicare's scheduled physician cuts were overridden by 17 laws before they were repealed [EV-FIN-057]. Nothing in a statute stops a later Congress from doing the same. Three things make it harder here: the steps are enacted early, with their dates, so stopping one is a scored tax cut that the plan's own D4 test reports (statutory PAYGO is a weak guard: Congress has excluded or wiped about $12 trillion from its five-year scorecard since 2010 and no sequester has ever been ordered [EV-FIN-055]); the rule's own deferral gives a lawful way to stop a step when it isn't needed, which takes away the usual argument for a waiver; and the order in part 3.3 sends the first gains back to households, so the people the ladder reaches see it move both ways.

**Deferral, one year at a time.** A step not yet in force is deferred by a year when, in the October twelve months before its date:
- measured debt has run at least 1 point of GDP below the path for the last two fiscal years (before FY2040, below the booked plan's path for those years); and
- the trustees' five-year projection, on CBO's latest economic assumptions and current law with the step removed, keeps debt at or below the path in every year.

A deferred step stays in law and is tested again the next year. It is never repealed by finding, only by Congress.

### 3.3 When results beat the path: the split

This is the one place where four memos' promises meet. G15 B steps the target toward 100% "as results allow"; G16 B and G18 D′ step the health contribution down on "a surplus beyond the debt goal's path"; G19 B lets the rule switch off a step "if results beat the goal". All four draw on the same thing: debt running below the path. Without an order they promise the same dollar three times (part 7).

The rule's order, when measured debt has run at least 1 point below the path for two fiscal years:
1. **Half of the lead lowers the path, for good** (rounded down to half a point). That is G15 B's step toward 100%.
2. **The other half may be returned,** in this order, each only if the trustees' projection shows the lowered path still met for five years without it:
   - (a) defer a ladder step not yet in force (a tax not raised keeps the populist start, `DEC-2026-11-24-18`);
   - (b) step the health contribution's base rate down a quarter point, never below 3.25% (G16 B, G18 D′: take-home, `DEC-2026-11-24-12`);
   - (c) suspend a ladder step already in force, last in, first out.
3. One move a year. The lead is measured afresh the next October against the lowered path.

**What it does on 8a's and 8b's numbers** (nothing new priced; `4-fiscal-path.md` parts 1.3, 1.4 and 3):
- **At CBO's rates (r − g +0.44),** holding debt flat from FY2040 needs about $461B in FY2040, and G19 B's ladder raises about $430-460B after the outside fix and phasing. So the ladder is all needed: nothing is deferred, nothing returned, and the path stays at about 117%. **On the central estimate the rule doesn't move debt toward 100%.** Only results better than CBO's do.
- **At r − g −0.5,** holding flat costs nothing and the ladder's about 0.8% of GDP would all run ahead of the path. Under the split about half (about 0.4% of GDP) goes to the path. Under 100% by FY2055 needs 0.36% of GDP on that reading, so half the ladder would get debt there, and the other half comes back to households.
- **At r − g +1.5,** holding flat needs about 2.1-2.4% of GDP, so the full ladder falls 1.3-1.6 points short. Debt runs above the path and the return procedure (part 3.4) starts.
- **WAD-H1,** health a quarter point a year below D2's cap (about $77B in FY2040 and $777B in FY2056; `4-fiscal-path.md` part 5.4), enters the rule only as it shows up in measured debt. It counts toward nothing up front (the hard rule).

### 3.4 When debt runs above the path: no automatic cuts

When measured debt has run at least 1 point above the path for two fiscal years, outside an escape:
1. Nothing is deferred and nothing is returned; every deferred step takes effect on the next January 1.
2. **A return plan.** The President's next budget must include legislation that brings projected debt back to the path within five years, on CBO's score. It is introduced in both chambers within 15 days and gets a guaranteed up-or-down vote within 60 session days, under expedited procedures written into the act as an exercise of each chamber's rulemaking power (the model is the procedures Congress has used for base closures and trade agreements). Congress may substitute its own plan of the same size.
3. **No sequester.** Nothing is cut by formula. The rule's force is that the money is already in law (the ladder), that the plan's own D4 test reports the gap, and that the vote can't be avoided.

**Why no automatic cuts.** A rule that cuts spending when debt runs high cuts hardest in the years after a shock, when receipts are weak, which is procyclical. It also hands a future Congress that wants smaller programs a lever to cut them while saying the formula did it. Gramm-Rudman-Hollings, the one US rule built on automatic cuts against deficit targets, was missed every year and evaded with timing shifts and one-time sales (part 2.1). Option C (memo G20) adds automatic base-rate steps instead of cuts; part 4 sets out why it isn't recommended.

### 3.5 The rate-shock watch

A rate shock reaches the debt ratio slowly, as old debt rolls over; by the time measured debt is a point above the path, several years of higher interest are locked in (8a's +100bp shock adds about 4 points to FY2040 debt and 24 by FY2056; `4-fiscal-path.md` part 1.5). So the rule watches the rate too:
- If the average interest rate on marketable Treasury debt (Treasury's monthly table) runs 0.75 points or more above the path's assumption for four quarters, the trustees publish a five-year projection at once.
- If it shows debt more than 1 point above the path within five years, deferrals and step-downs stop and the return plan (part 3.4, item 2) starts early.
- It never triggers a tax step or a cut by itself. A rate move can be the Federal Reserve's, a global one or a bout of market fear; the response should be a law that Congress chooses with the facts in front of it, not a formula.

### 3.6 The escape clause

The rule stands aside, in full, in either case:
- **A recession, on a measured test:** the three-month average of the national unemployment rate (the Bureau of Labor Statistics) rises 0.5 points or more above its low in the previous twelve months, Claudia Sahm's trigger [EV-FIN-060]. No vote and no forecast is needed.
- **A declared emergency:** a joint resolution naming the emergency, its expected cost and a period of up to two years, renewable by another resolution (a war, a pandemic, a disaster beyond the existing funds).

While it stands aside:
- no ladder step starts (its date slides a year at a time), no test is run and nothing is returned;
- the automatic stabilizers run in full: unemployment insurance, the child benefit, SNAP and the single plan's coverage, and the progressive tax system;
- the backstop for D2 (G13) keeps running, since it is about health's own path, not the cycle.

**The restart.** The escape ends two full fiscal years after the recession test switches off (or the emergency period ends). The path restarts at the measured ratio in that year and the ratchet resumes from there. Debt taken on in a recession isn't clawed back by formula, which would cut or tax in the recovery. G20's point 3 offers the alternative: a glide back, recovering half of the jump over ten years, as Switzerland's amortization rule does for emergency spending [EV-FIN-032] (part 2.2).

### 3.7 Investment

Everything borrowed counts in the measure, investment included. There is no carve-out after FY2039:
- D4-B's envelope (up to 0.5% of GDP a year to 2034, tapering to zero by 2040) already lets the plan borrow for time-limited investment with a written return case through FY2039 (part 6).
- A permanent carve-out for "investment" is the easiest part of a rule to game. Spending is relabeled to fit it, and the debt it leaves is just as real to the bond market. The IMF's staff find that formal compliance with rules has squeezed public investment where there was no carve-out and invited creative accounting where there was [EV-FIN-044]; Germany's 2025 exemptions are the current example [EV-FIN-049] [EV-FIN-050] (part 2.2).
- Memo G22, point 3, offers earned investment room after FY2039 instead: a new envelope by law, only while debt is at or below the path, inside the path.

### 3.8 Who certifies, and how

- **The trustees** who already certify D2 (G13) and G18 D′'s step certify the rule's two findings, in one annual report each October: debt against the path, and the escape status. One body, one report. They are executive officers, because a trigger that executes the law can't be certified by an officer Congress controls: the Supreme Court struck Gramm-Rudman-Hollings' trigger for exactly that (*Bowsher v. Synar*, 1986) [EV-FIN-054]. Their membership isn't yet set anywhere in the repository: G5, G8 and G13 name "the plan's fund trustees" but not who they are. The rule needs it set, and this part proposes the Secretary of the Treasury as managing trustee with the Secretaries of Health and Human Services and of Labor, as Social Security's board is built. Public trustees with protection from removal, the usual answer, are on weaker ground after *Trump v. Slaughter* (2026) overruled what was left of *Humphrey's Executor* [EV-FIN-064]. So the design doesn't lean on the certifiers' independence. It leans on the next two points.
- **The findings are arithmetic on published data:** Treasury's debt, BEA's GDP and BLS's unemployment. The only projection is the five-year check that guards a deferral or a step-down, and it uses CBO's economic assumptions, not the administration's.
- **CBO publishes its own reading** in the same week, as a check with no legal effect. A CBO disagreement can't hold back a certified finding: that would give a legislative-branch agency a hand in executing the law, which *Bowsher v. Synar* rules out [EV-FIN-054]. What guards against a politicized certifier instead:
  - **The inputs are fixed in the statute.** Every test reads published measures (Treasury's debt, BEA's GDP, BLS's unemployment rate), and the one projection, the five-year check that guards a deferral or a step-down, must use CBO's latest published economic assumptions and current law. The trustees choose no input.
  - **A giveback waits 60 days.** A deferral or step-down takes effect no sooner than 60 days after the certification, with the trustees' table and CBO's beside it. If they differ, the trustees publish a reconciliation in that time, and Congress may stop the giveback by joint resolution under the act's expedited procedure (part 3.4), which, like any law, goes to the President.
  - **The escape clause** applies only on BLS's measured test or a declared emergency, never on a projection.
  So a politicized certifier has no input to bend, and a giveback it certifies wrongly is public for two months before it takes effect.
- **The statistics have to be trusted.** A rule keyed to measured data is only as good as the agencies that measure it. The President's removal of the BLS commissioner in August 2025, which former BLS officials said undermines the credibility of federal statistics, is the warning [EV-FIN-061] [EV-FIN-062]. The plan should pair the rule with statutory protection for the principal statistical agencies' heads and release schedules (a point for democratic renewal's next touch, not priced here).
- **Legal footing:** contingent legislation. Congress sets the path, the steps, the tests and the order; the trustees find facts (*Field v. Clark*, 1892; *J.W. Hampton v. United States*, 1928; as G5 and G13). If a finding is challenged, the default applies on its date.
- **Burden:** one table added to an annual report the trustees already publish, and one CBO table. No new agency.

### 3.9 With D4 and the plan's other triggers

- **D4 stays the rule for the plan's own laws:** permanent programs paid for at maturity, tested in FY2040 and every later year on the general fund. It governs what each bill must do. The debt-path rule governs the result for the whole budget, interest and all. The plan needs both: D4 alone let debt reach 133% because current law's deficits weren't the plan's to pay (`4-fiscal-path.md` part 1); the debt rule alone would let a new program be paid for with the ladder's money.
- **The debt-path rule replaces D4's third test** (guardrails against CBO's current-law path, with no test on the plan's own debt). That is a change to a central rule, so it is memo G22's point 2, not assumed here.
- **G13's backstop comes first.** If D2 misses, G13's steps close health's overrun on their own trigger; the debt rule measures what is left. The two never count the same shortfall.
- **The thin years.** On the booked package the general fund's margin in FY2040-44 is $0.4-6B a year, so any one risk breaks D4's test in those years (`2-settlement.md` part 5). The debt rule's one-point band is about $540B of debt in FY2040, so a $50-100B miss would take several years to reach it. That is the point of a stock rule with a band: it doesn't force a reaction to every year's noise, but it doesn't let a lasting miss go unanswered either.

## Part 4. The options for the rule (memo G20)

| | Form | When debt beats the path | When it runs above | In a recession | Main risk |
| --- | --- | --- | --- | --- | --- |
| A | **Report and explain** (the Swedish model): a target path in law; the trustees and CBO publish the gap; the President's budget explains any deviation and the route back | Nothing automatic | Nothing automatic | Explained | No force in a Congress that doesn't honor it; G19's steps would need a vote to cancel and G15's step toward 100% has no mechanism |
| **B (recommended)** | **A measured debt path with a cancellable revenue ladder** (part 3) | Half lowers the path; half defers a step or lowers R | Deferred steps take effect; a return plan with a guaranteed vote; no cuts | Stands aside; restarts from where debt is | A later Congress repeals the ladder; the central case moves nothing toward 100% |
| C | **B plus automatic tax steps when behind:** if no return law passes within a year, R rises a quarter point a year until debt is back within a point of the path | As B | As B, then R steps up | Stands aside | Middle-class rises by formula outside a recession; R is also G13's backstop instrument, so take-home could fall well below 69% if both run |
| D | **A Swiss-style expenditure ceiling:** total spending outside the stabilizers capped at structural receipts each year | Spending room rises | Spending must be cut to the ceiling | Adjusted by an estimated cycle | Cuts by formula; needs an estimated cyclical adjustment the IMF says invites circumvention [EV-FIN-046]; fits a budget mostly made of annual appropriations, which the US one isn't |

**Not offered:** a Gramm-Rudman-style sequester against deficit or debt targets. The record is in part 2.1, and the brief rules it out.

**Why B.** It is the only form that makes G15 B's step toward 100% and G19 B's cancellable steps mean something while keeping the brief's two constraints: nothing cut by formula, and nothing automatic for a hostile Congress to use. A gives up the ladder's force; C adds middle-class tax rises by formula, which defeats the populist start and stacks on G13's backstop; D cuts by formula.

**What B can't do.** It can't stop a later Congress from repealing the ladder. No statute can. The rule's defenses are political: the money is in law and scored, the deferral gives a lawful off switch so a waiver isn't needed, and the giveback order lets households see the rule work in their favor too.

## Part 5. The debt limit (memo G21)

The debt limit is not a fiscal rule. It caps the borrowing needed to pay for spending and tax laws Congress has already passed, so it doesn't restrain new commitments; GAO says the process "creates an unnecessary risk of U.S. default" and recommends replacing it with an approach that links debt decisions to spending and revenue decisions when they are made (GAO, 2026) [EV-FIN-026]. This part keeps it apart from the debt-path rule: the rule says how much the plan borrows; the limit only decides whether Treasury may pay for it.

**Where it stands.**
- The 2025 reconciliation law raised the limit by $5.0 trillion, to $41.1 trillion (CRS) [EV-FIN-016]. CRS reads recent projections as reaching it sometime in FY2027 [EV-FIN-017]. The scenario dossier expects the leverage moment in late 2027, beside the FY2028 bills (`../../scenario/2027-28-playbook.md`), and asks whether to seek a raise that lasts into 2030 (`../../scenario/compounding-2029-2050.md`).
- Congress has changed it 104 times since the Second World War (CRS) [EV-FIN-018].
- **What standoffs cost.** GAO estimates the 2011-2023 impasses added roughly $107-161 million in immediate borrowing costs, with harder-to-measure long-term costs on top (GAO, 2026) [EV-FIN-025]. In 2011 the S&P 500 fell about 17% around the debate and consumer confidence 22% from June to August (Obama administration Treasury, 2013, an interested party) [EV-FIN-027]. S&P cut the US rating in 2011, citing "political brinksmanship" and the debt ceiling as a bargaining chip [EV-FIN-028]; Fitch did in 2023, citing "repeated debt-limit political standoffs" [EV-FIN-029].
- **The decided Senate rule** (legacy D2, graduated cloture from the first week of 2029) means a repeal can pass by regular order after a fixed delay, with no need to fit it into reconciliation.

**The options** (statutory first; the constitutional arguments last, because they carry legal risk):

| | What | How it would pass in 2029 | For | Against |
| --- | --- | --- | --- | --- |
| **A (recommended)** | **Repeal** 31 U.S.C. 3101's dollar limit; Treasury borrows what enacted law requires | Regular order under graduated cloture; a dollar-amount raise in the first reconciliation bill as a bridge if needed | Ends the default threat for good; the debt-path rule becomes the anchor; GAO's recommendation goes further in the same direction [EV-FIN-026] | "Democrats abolished the debt limit" is an easy attack; a later Congress can reinstate it |
| B | **Tie it to the budget resolution** (a statutory "Gephardt rule"): adopting the budget resolution deems the matching limit passed | As A; a House rule alone can be repealed each Congress | Keeps a recorded decision on borrowing, at the moment the budget is set | The House rule triggered in only 17 of its 33 years, because it was suspended or no resolution passed [EV-FIN-021], and was repealed in 2023 [EV-FIN-020]; the Senate has no equivalent |
| C | **A delegated suspension** (the 2011 model): the President certifies the need; the limit rises unless Congress passes a joint resolution of disapproval, which the President can veto | As A | Keeps a vote and a veto; in 2011 the Senate rejected disapproval 45-52 [EV-FIN-022] | Still a vote the opposition can use to message; a hostile President and Congress together could block it |
| D | **The constitutional arguments**: the Fourteenth Amendment's Public Debt Clause, or a platinum coin | Executive action, not a law | Available if Congress won't act | The Court has construed the clause once, and how it applies to the limit is unclear (CRS) [EV-FIN-023]; previous administrations and many legal experts have rejected it [EV-FIN-019]; in 2013 the Treasury and the Fed rejected the coin [EV-FIN-024]. Debt issued under a contested authority could itself shake the market the plan most needs |

**Decided: A, repeal, in 2029, with C as the fallback** (`DEC-2026-11-25-07`) if the votes for outright repeal aren't there. D is never the plan. It is an argument a government may need in a crisis, and a 2029 government should say plainly now that it would not rely on it, so markets don't price the chance of a contested default.

**Denmark** is the usual comparison: its ceiling was raised in 2010, with all major parties' support, to stay far above outstanding debt and out of day-to-day politics, and from 1993 to 2010 debt was never within Dkr 140 billion of it (Peterson Institute, 2011, dated) [EV-FIN-030]. That is option A's effect with a number left in the statute; it is a reasonable fallback wording if repeal itself becomes the attack line.

**With the 2027-28 strategy.** This is a 2029 recommendation. What to seek in 2027-28 (a raise sized to last into 2030, which the scenario dossier asks about) stays board question 0a's.

## Part 6. The central rules

Espen allowed the review to examine the project's central rules and propose changes where they serve "long-term sustainable progressivism" (`DEC-2026-11-24-14`). The rules, as decided (`legacy/governing/project-2050-governing-decisions.md`, D3 and D4):
- **D3:** every income group below the top comes out ahead on net, checked by household net effect, and new general-fund revenue comes mostly from the top 1% and corporations. On the booked settlement every fifth below the top comes out ahead (Q4 +$5,525 a household a year over FY2030-39) and the revenue-mix test reads 65% over the decade (`2-settlement.md` part 3).
- **D4 (D4-B, the fiscal arc):** (1) permanent programs paid for at maturity, tested in FY2040 and every later year; (2) time-limited investments with a written return case borrowed inside an envelope of up to 0.5% of GDP a year through 2034, tapering to zero by 2040; (3) guardrails against CBO's current-law path, with no test on the program's own debt; (4) trust funds kept whole, no dynamic revenue counted; (5) Judgment Fund contracts counted.

**What the review found.**
1. **D3 is tested on the decade, and the later revenue lands after it.** G19 B's ladder starts in FY2037 and is mostly felt from FY2040, outside the window D3 tests; the mature years are only reported. About 0.8% of GDP of new broad revenue from the late 2030s (`4-fiscal-path.md` part 6) is not checked against D3's promise. This part prices nothing new, so it doesn't say whether Q4 stays ahead; it says the test should be run before the ladder is enacted. The revenue-mix half of D3 can't hold in those years by design: broad revenue is not top-end revenue.
2. **D4's third test no longer fits a debt goal.** "No test on the program's own debt" was Espen's reading when the plan paid only for itself (D4, Decision Brief 2). G15 asks for a test on the plan's own debt. Keeping the old guardrail beside the new one would be harmless but meaningless: debt below current law's path (180% of GDP in FY2056) is met with 47 points to spare on the booked plan.
3. **D4's annual test is thin in FY2040-44.** The margin is $0.4-6B a year, and every single risk breaks it (`2-settlement.md` part 5). That doesn't need changing: D4 is a planning test, and the debt rule's band, about $540B of debt in FY2040, is what keeps a lasting miss visible without forcing a reaction to every year's noise (part 3.9).
4. **D4-B's envelope ends in 2040, and nothing replaces it.** After FY2039 any investment is ordinary spending. That is right for a rule that counts all debt (part 3.7), but it means a later public investment push has no room except inside the path.
5. **D4's "no dynamic revenue counted" is the hard rule, already.** Step 8a's hard rule extends it to "works as designed" savings and says measured results may count through a trigger. The debt rule makes that concrete: measured debt carries whatever growth or health savings really happened.

**Proposed as forks (memo G22, each decided on its own):**
- **G22.1, D3 in the mature years: yes (recommended).** Keep D3's quintile test on FY2030-39 and add the same test in FY2040 and FY2050, with everything counted, including G19's ladder at its default. If a fifth below the top falls behind, the ladder's order changes (the carbon fee's dividend first, the AGI surtax's threshold up) before it is enacted. Keep the revenue-mix test on the decade only, where the populist start lives, and say so.
- **G22.2, D4's guardrail replaced by the debt-path rule: yes, if G15 B and G20 B are chosen.** The current-law guardrail is retired; the plan's own debt is tested.
- **G22.3, investment after FY2039: no standing carve-out; room earned (recommended).** A new investment envelope after FY2039 only by a new law, only for investments with a written return case, and only while measured debt is at or below the path, inside it.
- **G22.4, the hard rule written into D4: yes (recommended).** D4's "no dynamic revenue is counted" becomes: no dynamic or "works as designed" saving counts toward a test up front; measured results count through the debt rule's findings and the triggers that read them.

**Not proposed:** loosening D4's paid-for-at-maturity test, or replacing D3's principle. Both are what make the plan's progressivism durable: a permanent program that isn't paid for is the easiest for a successor to cut, and a plan whose middle class falls behind loses the voters it needs for the long term.

### 6.1 The rules as decided: D4's rewrite and D3's test years (proposal text)

Espen decided G22's four points on November 25 (`DEC-2026-11-25-08` to `-11`). The rules' original text is in `legacy/governing/project-2050-governing-decisions.md` (D3 and D4), which is read-only, so the rules as amended live here and in the decision log. Where the two differ, the decision log and this text govern. Changes against the legacy text are marked **new**.

**D4. The fiscal rule (D4-B, as amended).**
1. *Paid for at maturity:* permanent programs' year-ten run rate is covered, tested in FY2040 (FY2039 net of time-limited lines) and every later year, on the general fund. The ten-year sum is not the test. (Unchanged.)
2. *Investment envelope:* time-limited investments with a written return case may be borrowed for up to 0.5% of GDP a year through 2034, tapering to zero by 2040. Unused room does not carry forward, and the envelope is available only while test 1 passes. (Unchanged through FY2039.) **New (G22.3): after FY2039 there is no standing envelope or carve-out for investment.** A new envelope may be created only by a new law, only for investments with a written return case, and only while measured debt is at or below the debt path; its borrowing counts inside the path, like all other borrowing.
3. **New (G22.2): the debt path, in place of the current-law guardrails.** Federal debt held by the public, measured at the end of each fiscal year as a share of GDP, is held at or below the path the debt-path rule sets (G20 B; part 3), tested on the measured figures from FY2040. The path is G15's (as redrafted in memo G23 and confirmed by Espen). The old guardrails (total debt below CBO's current-law path every year and by more each decade; net interest below the baseline's share of GDP) are retired as tests. The trustees' report may still show them beside the path, for comparison.
4. *Trust funds and scoring:* Social Security, Medicare HI and the Highway Trust Fund are kept whole, read on a 75-year window for the social-insurance funds. No new trust fund is created just to hold a pay-for. Fairness follows D3. **New (G22.4), replacing "no dynamic revenue is counted": no dynamic, "works as designed" or other projected saving counts toward any test up front. Measured results count only through the debt-path rule's findings and the triggers that read them** (G16 B's and G18 D′'s step-down of the health contribution, G20 B's deferrals).
5. *Judgment Fund:* CLI-9's contracts are scored at full expected cost when obligated; AAJA's damages are a disclosed contingent-liability line, bounded by CLI-3's cap. (Unchanged.)

The Byrd rule stays as it is.

**D3. The household test (as amended).** "More money in middle-class pockets; the uber-wealthy pay their fair share." For every income group below the top, the agenda's combined taxes, fees and benefits must leave households better off on net. New general-fund revenue must come mostly from the top 1% and corporations.
- **The quintile test** runs over FY2030-39 (unchanged) **and, new (G22.1), in FY2040 and FY2050**, with everything counted, including any later revenue step at its scheduled default. If any fifth below the top falls behind in either year, the step's design changes before it is enacted: a larger rebate or dividend first, then a higher threshold.
- **The revenue-mix test** (mostly from the top 1% and corporations) stays a test of FY2030-39 only, with the mature-year share reported (G3b, `DEC-2026-11-20-07`). Later broad revenue can't pass it by design, and the decade is where the populist start lives (`DEC-2026-11-24-18`).
- *How the mature years are read:* the household model runs to FY2039. Step 9 reads FY2040 and FY2050 as the booked FY2039 position carried forward with income per household, plus each new step's incidence in that year (`7-batch3-revision.md` part 4). A full mature-year run of the household model is a later model step.

## Part 7. What the rule changes for G15 B, G16 B, G18 D′ and G19 B

#484 has merged. At the lead's request this PR makes each change below in the memos themselves, so Espen gets one consistent batch, along with the three fixes from #484's review (G15 and G19 say where the rule lives and what B means without it; G19 A nets the $28B outside fix, about $433B with R about 5.7%; G17's years read FY2035-39). What was found, and how each memo now reads:
1. **One upside, three claims.** As drafted, G15 B steps the target toward 100% "as results allow", G16 B and G18 D′ step R down on "a surplus beyond the debt goal's path", and G19 B switches off a step "if results beat the goal". The rule's order (part 3.3) reconciles them, but G15, G16, G18 and G19 now each say they share the upside under that order.
2. **On the central estimate, G15 B stays at about 117%.** The ladder's money is all needed to hold debt flat at CBO's rates, so the step toward 100% happens only if results beat CBO's assumptions (part 3.3). G15 now says B stays at about 117% on CBO's rates.
3. **G16 B's "two steps by FY2042-44" depends on the order.** Under the split, a WAD-H1 saving first lowers the path by half, and only the other half can step R down. G16 now says so: about one step by FY2042-44 on its example, not two, unless Espen puts take-home ahead of the path (G20's point 1).
4. **G19 B's enactment date.** Its table says each step is "enacted by FY2033"; its recommendation and question say "the first Congress" (2029-30). The rule assumes the first Congress, which is what makes the steps a vote the plan takes while it has the votes. G19's table now says the first Congress (2029-30).
5. **G15 B and G19 B's starting years.** G15 B says nothing is asked before FY2040; G19 B starts its first step in FY2037. The rule works either way (the FY2037 step lowers the debt carried into FY2040, and with it the path), G15 now says the goal's test starts in FY2040 and nothing new reaches the middle class before FY2037, when G19's first steps begin.
6. **G18 D′'s floor and G13.** G18 D′ never steps R below 3.25%; G13 steps R up if D2 misses. The rule nets G13's steps out first (part 3.9), so a D2 miss and a debt shortfall don't both raise R for the same dollars.

## Part 8. The decision batch (decided November 25, 2026)

Memos [G20](memos/G20-debt-path-rule.md), [G21](memos/G21-debt-limit.md) and [G22](memos/G22-central-rules.md) are in `memos/`. Espen decided each on its own on November 25 (`DEC-2026-11-25-06` to `-11`), each as recommended; none is booked. The strategy memo ([`6-strategy-memo.md`](6-strategy-memo.md)) is not a fork: its recommendations are for Espen to read and redirect, not to decide item by item.

| Memo | Question | Decided |
| --- | --- | --- |
| G20 | The debt-path rule's form | **B**: a measured debt path with a cancellable revenue ladder, no automatic cuts, a measured escape clause; points 1-3 (the split, the giveback order, the restart) |
| G21 | The debt limit | **A**: repeal in 2029, the delegated suspension as the fallback; never rely on the constitutional arguments |
| G22 | The central rules | **G22.1** D3 in the mature years: yes; **G22.2** D4's guardrail replaced by the debt path: yes; **G22.3** no standing investment carve-out after FY2039: yes; **G22.4** the hard rule written into D4: yes (part 6.1) |

## Evidence still needed

- **A CBO or GAO assessment of the 1990 Budget Enforcement Act's record.** The register has one scholar's 1997 testimony [EV-FIN-053]; GAO's 1993 report (AFMD-93-38) was found but not read.
- **CRS's current versions of R43389 and RL31967** (the versions saved predate 2023 and 2025).
- **The Cadillac tax's delays and repeal** (P.L. 116-94) from a primary source; only search snippets were seen.
- **Sweden's original 1% surplus target** from an official source.
- **An OLC opinion on the Fourteenth Amendment option,** if one exists; none was found.
- **The trustees' membership** in the health dossier's fund text, which this part proposes (part 3.8).

## Method and sources

- **Sources:** CRS reports and GAO's 2026 report on the debt limit, saved as text; the Supreme Court's opinions in *Trump v. Wilcox*, *Trump v. Cook* and *Trump v. Slaughter*, saved; the Swiss, Swedish, UK, EU and German sources and the IMF, cited as citation rows (their licenses don't allow saving). Four Standard-tier subagents gathered quotations with Firecrawl (Exa was out of credits, `DEC-2026-11-12-02`); every quotation from a saved text is anchored in it and checked by the registry checker, and the citation rows' quotations were matched by the subagents against the fetched page text and are for the reviewer to spot-check. CBO was read through a fetch tool, not downloaded (`DEC-2026-11-08-10`).
- **Executive-branch analysis** (`DEC-2026-10-30-01`): the Obama administration Treasury's 2013 paper is used for market data only and labeled as an interested party; the second Trump administration's claims about the BLS data are recorded as its view; the Treasury advisory committee's July 2025 report is the dealers' and investors' view.
- **Figures for the plan** are step 8a's and 8b's; no new model run.
