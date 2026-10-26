# Climate-centered development finance: buying verified mitigation abroad toward 2035

**Context.** Claude Code, October 26, 2026. Policy IDs: NSC-9 (climate finance, today only a pointer at $0), DEV-P (development programs, accepted October 26), CLI-13, REV-C2 and REV-C3, and the 2035 benchmark decided October 26. Branch `claude/climate-international`, built on PR #26. Status: Espen's decisions of October 26 recorded (counting rule, scale delegated, treaty strategy); for review.

**Files.** This analysis; the generated pricing in [climate-portfolio-international-pricing.md](climate-portfolio-international-pricing.md), from `index/tools/climate-portfolio/international.py` and `international.json`.

## The short answer

**Loss-and-damage payments can't count toward the 2035 goal, but paying for verified emission cuts abroad can, and for 2035 it is far cheaper than the last domestic tons.**

- **Loss and damage** pays for harm that has already happened (rebuilding after floods, relocating communities). It reduces no emissions, so no accounting system lets it count toward an emissions target. It belongs in the plan as climate finance, on its own line.
- **Mitigation results** are a different thing: verified tons of methane, deforestation or coal emissions cut in another country, which the United States pays for. Under Article 6 of the Paris Agreement, these "internationally transferred mitigation outcomes" count toward the buyer's national target when the host country subtracts them from its own accounts (a "corresponding adjustment"), so the same ton is never claimed twice.
- **The cost.** In the mid case the US could buy about **510 Mt a year by 2035** at about **$31 a ton**, including an integrity reserve:
  - about **$15.6B in 2035**;
  - about **$114B over 2030-39** (2025 dollars; $0.14T nominal).

  That adds about **8 points** to the 2035 result. Under Espen's 50% domestic floor, though, international tons count only once domestic action reaches 50% below 2005.
  - **The two floor measures are now inside Package A** (Oct 26): a clean-heat standard and clean-industry support at 50%. With the approved $150 price in the baseline, domestic action reaches about 50.2% in the mid case (49.1-52.0%), and the counted total is about **58%** below 2005 (49.1 / 58.0 / 67.0%). In the low case the floor is still missed, and no international tons count.
  - Before the floor measures were added, domestic action reached 49.6% in the mid case, just short of the floor.

  Reaching 61% needs about 750 Mt, which only the high-supply case reaches. Reaching 66% needs about 1.1 Gt.
- **Against domestic action:** beyond Package A, the next domestic steps add about one point in 2035 for about $160B of outlays plus higher bills. The 2035 gap is mostly about how slowly vehicles, furnaces and plants get replaced, which money can't speed up much in nine years. International purchases are roughly ten times cheaper per 2035 point.

Your instinct that development aid will increasingly be organized around climate fits the evidence. The cheapest international tons (oil and gas methane, forests, early coal retirement) are also energy-security, public-health and rural-livelihood programs.

## Why it is cheap, and why it is less cheap than it looks

**Physical supply is large.**
- **Methane.** The IEA finds about 70% of fossil-fuel methane abatable with existing technology, nearly 85 Mt of methane (roughly 2.4 Gt CO2e), and about 30% at no net cost at 2025 prices.
- **Forests.** Jurisdictional programs sell at roughly $10-20 a ton. Nepal's January 2026 agreement with the LEAF Coalition is up to 4 Mt for up to $55M.
- **Early coal retirement.** Deals like ADB's Cirebon-1 (retiring in 2035 instead of 2042) target large avoided emissions.

**But four things raise the real cost and limit the volume:**
1. **Integrity.** A 2024 review of 2,346 projects (Probst et al., *Nature Communications*) found that under 16% of claimed offset reductions were real: 11% for cookstoves, 25% for avoided deforestation and 68% for HFC-23. This design pays only for results measured after the fact at jurisdiction or facility scale. It excludes legacy project credits and adds a 10-40% integrity reserve.
2. **The market barely exists.** As of May 2026, 128 bilateral Article 6 agreements had produced five completed transfers, about 65,000 tons. Hundreds of millions of tons a year by 2035 requires the US to act as an anchor buyer, with long-term purchase contracts signed early and delivered through multilateral development banks.
3. **Additionality.** Methane cuts that already pay for themselves would happen anyway if a country simply regulated. Payments should buy speed, measurement and jurisdiction-wide baselines, not tons a host would cut regardless.
4. **The US has left the treaty system.**
   - The Paris withdrawal took effect January 27, 2026.
   - A January 7, 2026 memorandum ordered withdrawal from the UNFCCC itself. Its withdrawal article takes effect one year after notice, so probably early 2027; I could not confirm the date.
   - Article 6 transfers count toward a national target only for a Party. Rejoining Paris takes 30 days once the US is again a UNFCCC Party. UNFCCC accession takes 90 days, so instruments deposited together give Paris effect after about 90 days. Whether a president can rejoin the UNFCCC without a new Senate vote is legally contested, because the Senate consented in 1992.
   - Until then, purchases can still be contracted, and hosts can still make corresponding adjustments for them, but they count only under the project's own benchmark accounting, not a UN-recognized target.

## Recommended design: three windows under NSC-9

**1. International Mitigation Results Program (counts toward 2035, with limits).** The US contracts with governments and national companies for verified results.
- **What it buys:** methane cut against jurisdiction-wide baselines with satellite verification; jurisdictional forest results under ART-TREES-type standards; early coal retirement through results contracts; Article 6.2 programs in industry and power; small volumes of durable removals.
- **How it pays:** for delivered, measured tons only, under multi-year purchase agreements signed with contract authority (the CLI-9 tool), so signed contracts survive a hostile administration. New purchases could still stop.
- **Rules:**
  - The host makes a corresponding adjustment where it is a Party.
  - No cookstove, legacy CDM or voluntary-market project credits.
  - Indigenous and local community safeguards and benefit-sharing.
  - Clawback for reversals; an integrity reserve.
  - Public reporting of domestic and international tons separately.
- **Size:** about 510 Mt a year by 2035 (225-980), ramping from about 50 Mt in 2030. That is about $15.6B in 2035 ($3.6-60B) and $114B over 2030-39 ($26-437B).
- **Counting rule (decided by Espen; applied as a threshold):** international tons count toward the 2035 benchmark only when domestic reductions reach at least 50% below 2005. Package A plus CLI-13 reaches about 50.2% in the mid case now that the floor measures are inside it (49.6% without them). International tons do not count toward the 2050 net-zero goal, which is met at home with removals. After 2035, purchases taper as domestic cuts and removals grow. The pricing holds the full 2035 volume through 2039, which is conservative for cost.

**2. Loss and damage (climate finance, never emissions).** A US contribution of about $1-3B a year (about $20B over 2030-39) to the Fund for Responding to Loss and Damage.
- The fund had about $768M pledged from 28 countries, $250M available against up to $3B of requests, and first disbursements slipping to the end of 2026.
- The US pledged $17.5M in 2023.

**3. Adaptation through a climate-centered DEV-P.** Reorganize the restored development programs (DEV-P, about $92B over FY2030-39) around climate resilience: water, agriculture, health systems and disaster preparedness. This changes priorities, not cost. Add about $2-6B a year of dedicated adaptation finance on top (about $40B over 2030-39).

**Climate finance context.** COP29 set at least $300B a year by 2035 from developed countries. ODI puts a US fair share at about 45%, counting public, multilateral and mobilized private money. The three windows together, about $22B a year by 2035 in the mid case, would be the largest US public climate finance ever. They would still be well below that fair share, which also assumes large multilateral and private flows. Whether results purchases also count as climate finance to the host is debated, so this analysis counts them only once, toward emissions.

## Financing and the budget

**2030-39, 2025 dollars, mid (range):**
- Mitigation results: $114B ($26-437B).
- Loss and damage: $20B ($10-30B).
- Adaptation above DEV-P: $40B ($20-60B).
- Total: **about $174B** (about $0.21T nominal).

**Financing, after the corrected PR #26 budget.** The reviews of PR #26 established the rule under D7: 80% of added carbon receipts go to the dividend, and the general fund bears a 25% tax offset. Carbon receipts are therefore not free money.
- **Mitigation results (about $0.14T nominal mid).** After clean-industry contracts and forests, only about $49B of the transition share remains (central case). So results purchases need one of these:
  - Espen's option 3 from the allocation file: keeping process-emissions receipts outside the dividend frees about $198B over 2030-39. The same $198B is also a candidate for the climate package's own general-fund cost (about $89B central, PR #26). The two uses compete: together they need about $233B, so about $35B would still need a general-fund source.
  - A general-fund source in the revenue work.
  - The leftover transition share plus a smaller purchase volume, about 200 Mt in 2035 (about 53% overall).
- **Loss and damage and adaptation (about $0.07T nominal).** General fund, as ten-year commitments. D4 treats a standing commitment as permanent and paid for at maturity; making them time-limited would need a renewal vote. Part could come from REV-C2's border adjustment, a "carbon club" design in which partners that price carbon are exempt.

**Results purchases are not capital**, so they are not borrowing-eligible under D4-B; they are financed from receipts as above.

## Interactions and layering

- **Methane:** domestic REV-C3 plus international methane purchases plus REV-C2's border adjustment form a coherent methane-and-carbon club. Importers face a charge unless their producers cut leaks, and US payments help them do it.
- **Forests:** international forest results complement CLI-13's domestic forests. Both need permanence buffers.
- **Development aid:** the same institutions deliver DEV-P and the results program: the re-established development agency, DFC, and MDB partnerships. Climate becomes the organizing frame, as you suggested, without a second bureaucracy.
- **Domestic ambition:** the domestic floor stops purchases from replacing Package A, whose standards and grid are what make 2050 reachable.

## Durability and politics

- **Durability:**
  - Signed multi-year purchase agreements backed by contract authority survive a hostile administration.
  - Treaty participation is the weak point. A future withdrawal stops UN recognition, but contracted tons still exist, and corresponding adjustments still keep them out of hosts' accounts where hosts are Parties.
- **Politics:**
  - Expect "paying other countries instead of cutting at home". The domestic floor and transparent split answer it.
  - Methane and coal deals can be framed as energy security and competitiveness, because they cut the leakiest foreign gas and the coal plants that undercut US manufacturers.
  - Forest deals need strong safeguards against "carbon colonialism" criticism.

## Decisions

**Espen, October 26:**
1. **Counting: agreed.** Verified international mitigation counts toward the 2035 benchmark only above a 50% domestic floor. It is reported separately from domestic cuts and does not count toward 2050 net zero.
2. **Scale: "pick most defensible."**
3. **Treaties:** "yes rejoin paris, and rejoin UNFCCC if withdrawal has occurred by then (or halt withdrawal if in progress)."

**Decided under the delegation: scale.** The most defensible choice is **the mid case as the contracted plan, with a conditional route toward 61%.**
- **Contract for the mid case.** That is about 510 Mt a year by 2035, at about $31 a ton including the integrity reserve: about $15.6B in 2035 and $114B over 2030-39 (2025 dollars). With the floor measures now inside Package A, it gives a counted total of about 58% below 2005; without them, none of the international tons would count in the mid case.
- **Why not plan on 61% now.** The Article 6 market has delivered about 65,000 tons in total. Most legacy credits overstated their results. The 750 Mt case needs every source near its high end. Planning on it would make the 2035 claim depend on volumes no one has yet shown can be delivered with integrity.
- **The conditional route.** Purchases scale toward about 750 Mt (61%) only if independently verified deliveries reach at least 250 Mt a year by 2032 with reversals under 5%. If they do, contract authority rises to fund the extra tons, about $10-15B more a year by 2035, subject to financing.
- **If deliveries fall short,** the plan reports the shortfall rather than counting weaker credits.

**Treaty strategy (decided by Espen; design proposed under the delegation; executive-power and NSC files to integrate):**
- **Paris.** Rejoin in 2029 by instrument of acceptance. It takes effect 30 days after deposit (Article 21), which requires the US to be a UNFCCC Party.
- **UNFCCC, two cases:**
  - *Withdrawal still pending in January 2029:* rescind the notice before it takes effect, which stops the withdrawal.
  - *Withdrawal complete:* re-accede. Withdrawal takes effect one year after notice (Article 25), so it will probably have taken effect in early 2027. Re-accession takes effect 90 days after deposit.
- **The legal contingency (Senate).** The administration would rely on the 1992 Senate advice and consent as still authorizing membership. If that is challenged, it should also seek a fresh Senate resolution, or a statute approving membership.
- **Until the US is again a Party,** purchases continue under the project's own benchmark accounting, with host corresponding adjustments wherever hosts are Parties, so no ton is double-claimed. The 2035 claim is labeled "project benchmark" rather than "NDC" until re-entry is complete.
- **First NDC on re-entry.** Submit an NDC for 2035 that states the domestic floor and the international share separately.

**Proposed under the project-coworker delegation (now that 1-3 are settled):**
- the three windows under NSC-9;
- the integrity rules;
- purchase contracts under contract authority;
- the scale rule above.

**Still open for Espen:** how to finance the results purchases. They depend on his pending decision on the carbon-fee increment (keeping process-emissions receipts outside the dividend would cover the mid case) or on a general-fund source. Loss and damage and adaptation are general-fund items. As standing commitments they are permanent under D4, about $8B in FY2040 and $10B in FY2050 (nominal, mid), and belong in the maturity test beside the climate package's run rate.

## Limits

- **Estimates.** Volumes and prices are planning estimates from sourced anchors; the low and high cases combine low or high volumes with low or high prices.
- **Unknown availability.** How many high-integrity tons are actually available by 2035 is the largest unknown.
- **Unconfirmed dates.** I could not confirm the UNFCCC withdrawal's effective date or the Fund for Responding to Loss and Damage's 2026 pledge total.
- **Domestic baseline.** The domestic figure comes from one structural model, which responds more slowly than the large published models in its first decade. A faster model would shrink the gap and the purchases needed.

## Sources

- IEA, [Global Methane Tracker 2026, key findings](https://www.iea.org/reports/global-methane-tracker-2026/key-findings).
- Probst et al., [Systematic assessment of the achieved emission reductions of carbon crediting projects](https://doaj.org/article/e3ff0db656564f889739ce9531b53363), *Nature Communications* 15:9562 (2024).
- AlliedOffsets, [Article 6 revenue case](https://blog.alliedoffsets.com/what-article-6-means-for-host-countries-the-revenue-case-in-numbers) (agreements and transfers to May 2026); [Columbia CGEP on operationalizing Article 6](https://www.energypolicy.columbia.edu/publications/how-to-fully-operationalize-article-6-of-the-paris-agreement/).
- Morgan Lewis, [COP30 key outcomes for carbon markets](https://www.morganlewis.com/pubs/2025/12/cop30-key-outcomes-for-carbon-markets).
- UN-REDD, [Nepal's LEAF agreement](https://www.un-redd.org/post/turning-point-jurisdictional-redd-nepal); [LEAF Coalition](https://www.leafcoalition.org/home).
- Eco-Business, [Loss and damage fund faces $2.8bn gap](https://www.eco-business.com/news/loss-and-damage-fund-faces-us28bn-gap-as-first-projects-move-ahead/).
- ODI, [Did COP29 end with a good NCQG decision?](https://odi.org/en/insights/did-cop29-end-with-a-good-new-collective-quantified-goal-decision/); [Carbon Brief on the US fair share](https://www.carbonbrief.org/analysis-us-falling-32bn-short-on-fair-share-of-100bn-climate-finance-goal/).
- WRI, [The United States withdraws from the UNFCCC](https://www.wri.org/news/statement-united-states-withdraws-unfccc); [Jurist, January 2026 memorandum](https://www.jurist.org/news/2026/01/trump-orders-us-withdrawal-from-66-international-organizations-including-un-climate-bodies/).
- BNN Bloomberg, [Indonesia speeds up closing of a Java coal plant](https://www.bnnbloomberg.ca/indonesia-speeds-up-landmark-closing-of-java-coal-plant-1.2006793).
- Project: [climate portfolio allocation](climate-portfolio-allocation.md), [package results](climate-portfolio-packages.md), [capacity review round 2](capacity-recovery-other-agencies-review.md) (DEV-P), [domain-national-security.md](../domains/domain-national-security.md) (NSC-9).
