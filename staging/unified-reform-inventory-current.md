# Unified Reform Inventory: current version

Oct 20, 2026 · built from archive/ideas-unified-reform-inventory-oct13.md (Oct 13) and checked against governing/project-2050-governing-decisions.md and the domain files

**Role.** The old inventory is ideas only. This file is its current replacement, and every domain now has a canonical file, so the rows here are pointers to the domain files, kept as the crosswalk (each domain file's crosswalk table names the rows it replaces). **Where a row and its domain file differ, the domain file governs.** The arrow (→) in a row names its domain-file ID.

**Scenario.** Dec. D1: planned for 52-54 Senate seats; every row is tagged for whether it survives at 51; 56+ is upside. Dec. D2 (Senate rules) is decided: path F, graduated cloture with minority guarantees, adopted in week one of 2029; path C is the opening offer and path G the written fallback. Every ◐ row depends on that rules change holding.

## How to read the tables

| Column | Values |
| --- | --- |
| ID | Inventory ID (section.row); the domain-file ID follows the arrow. “Ledger X” is a legacy ledger row ID (H1, E4, D10 ...): the ledger now keys every row by its domain-file ID and keeps the legacy IDs in a crosswalk column. “Dec. D#” means a Governing Decision; “cut C#” means a ledger option (index/data/inputs/ledger-cuts.csv). |
| Vehicle | **R1 / R2 / R3** reconciliation vehicles from Dec. D5. **FL** regular-order bill on the Senate floor. **AP** annual appropriations or funding set there. **RU** Senate or House rules or practice (the old legend used [R] for this). **X** executive action or a declared norm. **ST** state level. **A** constitutional amendment. **T** treaty or international agreement. **—** operations, no vote. |
| Wave | ⓪ before the trifecta (2026-28) · ① first Congress, 2029-30 · ② second term or later · ⟳ continuous |
| @51 | ✔ survives at 51: reconciliation, state, executive, House-only or no Senate dependence. ◐ needs a D2 majority-precedent path (C, D, E, F or G) and holds at 51 only if that rules change holds with at most one defection (the Senate doc finds 52-54 absorbs 2-4); under path A or B it needs Republican votes. ✖ needs 60, 67 (amendment or treaty) or Republican votes in any scenario. |
| Numbers | Tagged in the notes: sourced (a cited document), scaled (a cited figure moved to a window or size), est. (my estimate). Default window is 2030-39, in trillions. |

## Where the canonical files already are

| Domain | Canonical home | Rows here |
| --- | --- | --- |
| Health | domains/domain-health.md (HLT-1 to HLT-6, add-ons A1-A4; sources/health-go-big-bill-detail-and-financing.md stays as the provision source) | 10.6-10.8 |
| Revenue | domains/domain-revenue.md (REV-G, H, O, P, C, E, SC, TS, HP; sources/revenue-channels-and-full-menu.md stays as the source tables) | 10.3, 11.1 |
| Transportation | transportation-moving-america-act-2031-draft-2.md, canonical until converted (ledger MOV-29 to MOV-31) | 10.15, 10.16, 18.10 |
| Public safety | domains/domain-public-safety.md (SAF-1 to SAF-11); domains/public-safety-safe-everywhere.md is its evidence base | 3.6, 5.10, 13.9, 19.4-19.6 |
| Carbon price | Dec. D7, built as REV-C1 and REV-C2 in domains/domain-revenue.md; the dividend is CLI-2 | 10.3 |
| Social Security | domains/domain-social-security.md (SS-1 to SS-10) | 10.14 |
| Family benefits | domains/domain-family.md (FAM-1 to FAM-3; FAM-4 points to education) | 10.2, 10.9, 10.10 |
| Education | domains/domain-education.md (EDU-1 to EDU-10) | 9.5, 10.11 |
| Representation, elections and civic life | domains/domain-democracy.md (DEM-1 to DEM-20; DEM-3, DEM-4 and DEM-9 are one second-term package) | 2.1-2.18, 3.1-3.12, 15.2-15.6 |
| Courts and administrative law | domains/domain-courts.md (CRT-1 to CRT-19, tiers T1-T3) | 4.1-4.19 |
| Executive power | domains/domain-executive-power.md (EXE-1 to EXE-18) | 5.1-5.17 |
| Anti-corruption and money in politics | domains/domain-integrity.md (INT-1 to INT-17; INT-5B pays the small-dollar match from general revenue) | 6.1-6.10, 7.1-7.8 |
| Congressional capacity and the successor state | domains/domain-capacity.md (CAP-1 to CAP-18; CAP-7S and CAP-7 carry D9's agency rebuild) | 8.1-8.10, 9.1-9.10 |
| Discretionary envelopes | Dec. D9: the agency rebuild in CAP-7S and CAP-7; defense in NSC-1 | 9.1, 16.8 |
| Climate and energy | domains/domain-climate.md (CLI-1 to CLI-13) | 9.7, 10.5, 14.1-14.10 |
| Housing | domains/domain-housing.md (HOU-1 to HOU-9) | 10.13 |
| Labor | domains/domain-labor.md (LAB-1 to LAB-9) | 11.4, 11.5, 11.7, 14.8, 15.1 |
| Competition | domains/domain-competition.md (COM-1 to COM-6) | 10.12, 11.2, 11.3, 11.6, 11.8 |
| AI and the information environment | domains/domain-ai.md (AI-1 to AI-11) | 10.4, 12.1-12.7, 13.1-13.8 |
| National security | domains/domain-national-security.md (NSC-1 to NSC-11) | 16.1-16.8 |
| Amendments | domains/domain-amendments.md (AMD-1 to AMD-11) | 17.1-17.11 |
| Immigration | domains/domain-immigration.md (IMM-1 to IMM-6) | 19.1 |
| Rights | domains/domain-rights.md (RTS-1 to RTS-4) | 19.2, 19.3 |

## 1. The enabling layer (Decision D2: path F)

D2 is decided (Decision Brief 1): path F, graduated cloture with Block 3's minority guarantees, adopted in week one of 2029; path C with a 15-day backstop is the opening offer and path G the written fallback; reconciliation stays as now. Rows 1.1-1.7 are the paths in “Senate Rules Reform: Options” (live page), which governs their design. Every ◐ in the file assumes a majority-precedent path (C, D, E, F or G). Under A or B those rows would need Republican votes: the Senate doc estimates 7-8 at A and 1-3 at B, at 52-54 seats.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Path A. Merkley-Daines as written: no cloture on motions to proceed, amendments or nominations; no intervening day; post-cloture time 30 to 12 hours; suspension calendar at two-thirds; one-day bipartisan fast track; two-day appropriations fast track. Final passage stays at 60 | RU | ⓪ | ✖ | Source: Merkley-Daines “To Save the Senate” (Oct 8, 2026) and the Senate doc. A rules change needs 67 to end debate (lame duck 2026 or 2029). The old rows “reform post-cloture time” and “fix the motion to proceed” are this path’s Block 1. |
| 1.2 | Path B. Cloture lowered to 55, plus Block 1 (the 1975 two-thirds to three-fifths change is the precedent) | RU | ① | ✖ | At 52-54 seats it needs 1-3 Republicans per bill (Senate doc, est.). A minority veto survives without showing up. |
| 1.3 | Path C. Talking filibuster with a speech budget: blockers need 41 present and voting, quorum presumed, 10 amendments per side, dilatory motions limited, optional majority-cloture backstop after N session days | RU | ① | ◐ | Replaces the old “restore the talking filibuster, burden on 41.” Senate doc: a minority can hold a bill about 2-5 weeks (est.). Strongest reciprocity answer among the options that restore majority governance. **D2: the opening offer**, with a 15-day backstop. |
| 1.4 | Path D. Uncapped talking filibuster | RU | ① | ◐ | The minority can block indefinitely (the 1964 filibuster ran 60 working days); likely stalls its top fights, such as DC statehood and election law. Modeled for completeness. |
| 1.5 | Path E. Full elimination: majority cloture after normal debate | RU | ① | ◐ | Fastest and least reciprocal: a future Republican majority gets the same power with no delay. About 30 floor days for 20 contested bills (Senate doc, est.). |
| 1.6 | Path F. Graduated cloture: 60, 57, 54, then a majority over four votes, about 4.5 session days, with minority guarantees | RU | ① | ◐ | The declining-threshold model from Instruments and Consequences. About 90 floor days for 20 contested bills (Senate doc, est.); bipartisan committee-reported bills skip the ladder. **D2: decided**, with 1.8's guarantees; the ledger counts 172 first-Congress floor days under F against 163. |
| 1.7 | Path G. Democracy-and-elections carve-out only (nominations-precedent model) | RU | ① | ◐ | **D2: the written fallback.** Under G only the carve-out (DEM-1 with its riders, DEM-5, DEM-6) passes (ledger path table). Nineteen Months puts expected enactments at 8.1 of 27 bills against 26.3 with full reform (as cited in the Dec. D2 table). |
| 1.8 | Minority guarantees and reciprocity: 10 guaranteed germane amendments per side, no filling the tree, equal time, and a rule that applies “without regard to which party holds the majority,” stated on the record | RU | ① | ◐ | Merges the old “reciprocity declaration” row into the rule text (Senate doc sec. 301-303). Block 3; adopted with F under D2. |
| 1.9 | Reconciliation dial: R1 as now, R2 narrowed to deficit reduction now, or R3 narrowed from January 2031 | RU | ② | ◐ | D2: reconciliation stays as now; any narrowing variant is settled with the adoption resolution. Dec. D5 routes the fiscal agenda through three reconciliation bills, so narrowing before summer 2030 would remove the backstop. Senate doc: only the January 2031 variant fits, and only beside a working majority path. |
| 1.10 | Parliamentarian transparency: publish the Parliamentarian’s advisory reasoning | RU | ① | ◐ | Narrowed. The old row “reform the Byrd rule’s application” is dropped because Dec. D4 leaves the Byrd rule unchanged. Flagged for confirmation. |
| 1.11 | House: restore a functioning Rules Committee and open-amendment norms | RU | ② | ✔ | House rule, majority only. Unchanged. |
| 1.12 | Blue slip for district judges: bind or abolish | RU | ① | ✔ | A committee-chair practice, so no floor vote. HELD: fails the reciprocity test as stated because the minority loses a veto on nominees in its states. Draft a bind-not-abolish form (notice and hearing) and pair with phased judgeships (4.1). |

## 2. Representation and apportionment

**Pointer: canonical in domains/domain-democracy.md (DEM-1 to DEM-10). House size (2.1), STV (2.3) and the presidential method (2.15) are one second-term package, run on in 2032 and enacted in 2033.** Instruments and Consequences corrections override the old inventory here (Governing Decisions, document roles). Rows 2.15-2.17 are new from that review.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 2.1 | House enlargement by statute to about 692 members on the cube-root rule, with automatic decennial recalculation (about 480,000 constituents per member against about 760,000 now) | FL | ① | ◐ | Replaces the Wyoming rule (about 585, phased over three cycles), which stays as a named option: Wyoming ties House size to the smallest state’s growth. Basis: Instruments and Consequences #1 (scaled; arithmetic not re-checked). The ledger's DEM-3 (old D10) carries about 692. → DEM-3. |
| 2.2 | House chamber and office capacity project: reconstruction or a distributed-voting architecture, started in the first Congress | AP | ① | ◐ | NEW. The chamber seats about 448 (Instruments #1). Time-limited capital, so borrowing is allowed under Dec. D4. Unscored. → DEM-3. |
| 2.3 | Multi-member districts by single transferable vote: repeal 2 U.S.C. sec. 2c; five-member districts wherever population permits, three only where geography forces it | FL | ① | ◐ | Instruments #2: magnitude decides whether third parties appear. HOLD until the Section 2 modeling is rerun on the post-Callais baseline (ledger cut C14). Do not ship without 2.15. Ledger D11. → DEM-4. |
| 2.4 | Federally mandated independent redistricting commissions for congressional maps (Elections Clause) | FL | ① | ◐ | Rucho invited and Moore v. Harper protected the approach. Urgency is up: Texas, California, Missouri and North Carolina adopted new maps, Florida and Tennessee redrew after Callais, and Virginia’s map was blocked from certification (Ballotpedia, May 2026; NCSL). Ledger D1. → DEM-2. |
| 2.5 | Ban mid-decade congressional redistricting | FL | ① | ◐ | NEW and reciprocal by construction. The Redistricting Reform Act of 2025 pairs commissions with this ban; introduced Sept 2025, not enacted (secondary source; confirm bill text). → DEM-2 (carries the 2034 exception). |
| 2.6 | Extend commission requirements to state legislative districts through conditional funding | FL | ① | ◐ | HELD. No Elections Clause hook for state maps, and the spending-power lever is NFIB-exposed (Instruments, Institutions). A candidate for the state track. → DEM-2D. |
| 2.7 | DC statehood; the admission act directs the residual district’s electors to the national popular vote winner, or leaves them unappointed | FL | ① | ◐ | Ledger D3. The 23rd Amendment gives Congress authority over the manner of appointment (Instruments #7), so repeal (17.6) becomes hygiene. → DEM-5. |
| 2.8 | Binding Puerto Rico status plebiscite with a pre-commitment to honor the result | FL | ① | ◐ | Ledger D4. → DEM-6. |
| 2.9 | Voting delegates for Guam, the Virgin Islands, American Samoa and the Northern Marianas, sequenced rather than gestured at | FL | ② | ◐ | Sequencing added by Instruments Part II. → DEM-7. |
| 2.10 | Tribal congressional representation and enforceable consultation standards | FL | ② | ◐ | Unchanged. → DEM-7. |
| 2.11 | Codify the statehood admission procedure so it stops being ad hoc | FL | ② | ◐ | Unchanged. → DEM-7. |
| 2.12 | National Popular Vote Compact to 270: 19 jurisdictions with 222 electoral votes; 48 needed; Arizona, Michigan, New Hampshire, Nevada, Pennsylvania and Wisconsin (65 EV) are the live targets | ST | ⟳ | ✔ | Sourced: nationalpopularvote.com (April 2026) and NPR (Apr 14, 2026, Virginia’s signing). The old row named PA, MI, AZ plus WI or NV; NPV now also lists NH. → DEM-8. |
| 2.13 | Compact: pass a resolution confirming that no congressional consent is required; hold consent in reserve as a response to litigation | FL | ① | ◐ | Replaces “seek proactive consent.” Under U.S. Steel v. Multistate Tax Commission, asking concedes consent is required (Instruments #6). → DEM-8. |
| 2.14 | Tighten the compact’s withdrawal blackout window | ST | ① | ✔ | The compact’s softest joint (Radical Means). Needs re-enactment by members. → DEM-8. |
| 2.15 | Presidential election method: national ranked-choice voting or a two-round runoff, written into the popular-vote amendment and the compact’s operative language | A | ② | ✖ | NEW and load-bearing. A multi-party House from STV plus a plurality-winner president is the most unstable configuration in comparative politics (Instruments, Part II). The compact as enacted awards electors to the plurality winner, so this needs member-state re-enactment. Decided Oct 19 (Espen): handled with 2.1 and 2.3 as one second-term package. → DEM-9. |
| 2.16 | Presidential primary calendar reform (now set by party rules) | FL | ② | ◐ | NEW (Instruments Part II). → DEM-9. |
| 2.17 | Fusion voting authorization | ST | ⟳ | ✔ | NEW (Instruments Part II); banned in most states; a lower-cost path to multi-party dynamics. → DEM-10. |
| 2.18 | Ranked-choice voting and open primaries, framed as anti-corruption | ST | ⟳ | ✔ | A deposit toward STV (Radical Means, rule 1). → DEM-10. |

## 3. Voting rights and elections

**Pointer: canonical in domains/domain-democracy.md.** The old inventory listed an affirmative right to vote in both this section and the amendments; it now sits only at 17.5.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 3.1 | John Lewis Voting Rights Advancement Act: preclearance on a modern coverage formula | FL | ① | ◐ | Answers Shelby County. Ledger D1 (Freedom to Vote family). → DEM-1 Title II. |
| 3.2 | Legislative response to Callais (decided April 29, 2026, 6-3): restore a results test for Section 2, authorize race-conscious remedial districting, and build a Fifteenth Amendment enforcement record | FL | ① | ◐ | Per the syllabus, Section 2 now requires a strong inference of intentional discrimination (Rebalancing, Part I). Risk: Fourteenth Amendment strict scrutiny of race-conscious remedies. Alabama’s case was the first to apply the Callais test (NCSL). → DEM-1 Title III. |
| 3.3 | Federal floor: early voting, no-excuse mail voting, same-day registration, automatic registration | FL | ① | ◐ | Ledger D1. → DEM-1 Title I. |
| 3.4 | Permanent, indexed election-administration funding | AP | ① | ◐ | Mandatory only if a reconciliation-eligible committee can carry it (unchecked); otherwise appropriations. Capacity first. → DEM-11. |
| 3.5 | Federal felony re-enfranchisement on release | FL | ① | ◐ | Unchanged. → DEM-12. |
| 3.6 | Election-worker protection: threat-assessment grants, address privacy, a threat statute fitting the 2023 true-threats standard, threats prosecutors | FL | ① | ◐ | The old criminal-penalty and private-cause-of-action rows are options there. → SAF-8 (domain-public-safety.md); DEM-14 points to it. |
| 3.7 | Ban partisan purges; standardize list-maintenance procedure | FL | ① | ◐ | Unchanged. → DEM-1 Title I. |
| 3.8 | Paper-ballot and risk-limiting-audit requirements | FL | ① | ◐ | Unchanged. → DEM-1 Title I. |
| 3.9 | Election Day as a federal holiday, or mandatory paid time to vote | FL | ② | ◐ | Unchanged. → DEM-13. |
| 3.10 | Voting rights for pretrial detainees; polling access in jails | FL | ② | ◐ | Consistent with the danger-not-wealth pretrial rule in Safe Everywhere plank 7. → DEM-12. |
| 3.11 | Certification as a ministerial act: harden what the ECRA left as ordinary statute | FL | ① | ◐ | Unchanged. → DEM-1 Title I. |
| 3.12 | Presidential transition integrity: mandatory GSA ascertainment triggers | FL | ① | ◐ | Unchanged. → DEM-1 Title I. |

## 4. Courts and administrative law

**Pointer: canonical in domains/domain-courts.md (CRT-1 to CRT-19).** Tiers follow Rebalancing the Three Branches: T1 integrity and capacity first, T2 statutory repairs, T3 structural reform used deliberately. This section is the staging draft the domain file replaced. Every row carries severability and a record for this Court (design rule 7).

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 4.1 | [T1] Phased judgeships: 66 district seats on the JUDGES Act lineage, with effective dates straddling at least two presidential terms | FL | ① | ◐ | Replaces “66 per the Judicial Conference.” The 2024 bill (63 permanent, 3 temporary, ten years) passed the Senate by unanimous consent and was vetoed Dec 23, 2024, because each party wants seats only when it expects to fill them (Rebalancing). Ledger D7. |
| 4.2 | [T1] Ethics and recusal: binding code with disclosure, gift, travel and amicus-funding rules; recusal decided by the Court’s own members with published reasons; enforcement through disclosure, referral to Congress and appropriations conditions | FL | ① | ◐ | Replaces “enforceable recusal review panel”: outside override of recusal is where the Court’s resistance is likeliest (Alito: “no provision ... period,” Rebalancing). Option: outside review panel, higher legal risk. One judiciary bill (ledger D6; cut C11). |
| 4.3 | [T1] Statutory random district-wide case assignment and venue reform; three-judge courts with direct appeal for challenges seeking relief beyond the parties | FL | ① | ◐ | Codifies the Judicial Conference’s March 2024 policy, which is guidance only (N.D. Tex. declined). Also the forum for challenges to this reform package (Instruments #5). Concentrates stakes in D.D.C. |
| 4.4 | [T1] Emergency-docket transparency: written explanation and recorded votes for any stay or injunction grant, no precedential weight for unexplained orders, codified stay standards, public statistics | FL | ① | ◐ | Grant rate for the federal government in Trump’s second term: 67% (SCOTUSblog) to 83% (Ballotpedia) depending on counting (Rebalancing). Dictating the substance of reasoning is the vulnerable part. |
| 4.5 | [T1] Article I immigration court (Real Courts, Rule of Law Act of 2026: H.R. 7836, S. 5094), designed to survive Trump v. Slaughter: placed clearly outside the executive, fixed terms with for-cause removal on the Tax Court model, a fallback into the judicial branch; plus restored Article III habeas and de novo review of law and mixed questions | FL | ① | ◐ | Rebalancing #12. About 3.1 million cases pending (TRAC, end of Aug 2026); OBBBA capped immigration judges at 800. Pairs with ledger E11. → CRT-5 (about $0.03T, unscored). |
| 4.6 | [T1] Judicial records and cameras: a Presidential Records Act-style regime for justices’ papers with a long embargo, live audio and video, searchable disclosure reports | FL | ② | ◐ | The old “cameras and same-day audio” row, widened (Rebalancing #19). |
| 4.7 | [T2] Channel review of rules into one court (the D.C. Circuit) with a short filing window; claims accrue at publication (a Corner Post fix); channeling stated explicitly so Axon carve-outs hold | FL | ① | ◐ | Rebalancing’s top-tier statutory repair. Models: Clean Air Act sec. 307(b), the Hobbs Act; Yakus upheld the type. |
| 4.8 | [T2] Answer Loper Bright with statute-specific express delegations drafted into every statute; a general APA “Chevron” codification is held as a messaging option | FL | ① | ◐ | Rebalancing #6: a general deference mandate invites a direct fight with the Court. The Thriving Economy “Restore Chevron” bill is the messaging version, folded here as an option. The old row sat in the state-capacity section. → CRT-8; templates drafted under CAP-18. |
| 4.9 | [T2] Remedies after CASA: authorize APA vacatur, specify when universal relief is available, and route it to three-judge courts with expedited review | FL | ① | ◐ | Symmetrical, so it binds both parties’ administrations. CASA rests on statutory interpretation, so Congress holds the pen. |
| 4.10 | [T2] Penalties after Jarkesy: district-court penalty actions, or restructure within the public-rights limits | FL | ② | ◐ | NEW (Rebalancing #21). |
| 4.11 | [T2] Docket reform: restore some mandatory jurisdiction, add a certiorari screening division, limit certiorari before judgment | FL | ② | ◐ | NEW (Rebalancing #16). 56 signed-opinion cases in OT2024 against more than 160 a year in the 1980s (Chemerinsky via SCOTUSblog). |
| 4.12 | [T2] Specialized Article III regulatory court on the Federal Circuit model | FL | ② | ◐ | NEW option, paired with 4.7. The Commerce Court (1910-13) is the cautionary case. |
| 4.13 | [T2] Circuit realignment on neutral criteria (population, filings per judgeship) | FL | ② | ◐ | Ninth Circuit: 67.1 million people and 29 judgeships; Fifth: 17 judgeships (CRS R48242 via Rebalancing). A split drawn for ideological balance invites retaliation. |
| 4.14 | [T2] Statutory repairs for specific decisions: VRA (3.2), reproductive rights (19.2), Clean Water Act and Clean Air Act sec. 111 clarifications (climate file), agency adjudication | FL | ① | ◐ | Pointer row; each lives in its own domain. → CRT-14. |
| 4.15 | [T3] Judicial term limits: 18-year terms, a vacancy every two years, prospective for newly appointed justices with a severable retroactive provision, Article III tenure and salary preserved, no deemed Senate consent | FL | ① | ◐ | Instruments #4 and Rebalancing #9. Bites after about 18 years: speed traded for durability. Pairs with the amendment (17.2). Polling: 79% support (Marquette, Sept 2-9, 2026). Ledger D7. |
| 4.16 | [T3] Court expansion held as a pre-committed response only to invalidation of the term-limits statute, with structural insurance: aggressive severability, a three-judge court with direct appeal, term limits bundled into the larger judiciary bill | FL | ① | ◐ | Fails the reciprocity test as an opening move; the coercion objection is named, not solved (Instruments #5). Marquette: expansion 53/47 overall and 35% of Republicans. A last line, not a first. |
| 4.17 | [T3] Jurisdiction-stripping restraint: declared, not exercised | X | ② | ✔ | A self-binding norm, no statute. Stripping carries very high escalation risk and sends cases to state courts (Rebalancing #4). |
| 4.18 | [T3] Impeachment reserved for corruption and serious misconduct, never for rulings | X | ⟳ | ✔ | The Chase norm; stated as a declared standard. |
| 4.19 | State supreme court selection reform; end partisan judicial elections | ST | ⟳ | ✔ | Unchanged. |

## 5. Executive power

**Pointer: canonical in domains/domain-executive-power.md (EXE-1 to EXE-18).** Trump v. Slaughter (June 29, 2026) overruled Humphrey’s Executor, so for-cause removal protection for officers who exercise executive power is no longer a safe design tool; rows that relied on it are redesigned with structure or placement outside the executive (Rebalancing #21). Learning Resources v. Trump (Feb 20, 2026) held that IEEPA does not authorize tariffs. Every constraint on the presidency needs a fast path with a short sunset and mandatory reporting, or it breaks the first time it binds badly (Instruments, Part III).

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 5.1 | National Emergencies Act reform: emergencies lapse without affirmative congressional approval, with an explicit short fast path | FL | ① | ◐ | Ledger D8. |
| 5.2 | War powers restoration with a funding-cutoff default | FL | ① | ◐ | Ledger D9; merged into this package (cut C10). |
| 5.3 | Anti-impoundment: a statutory cause of action for the intended recipient (state, grantee, contractor), not congressional standing; options: disbursement deadlines with deemed apportionment, termination only for cause, no rescission except by law, district-court jurisdiction with expedited review, no new grant conditions, third-party fiscal agents | FL | ① | ◐ | Instruments #8 (Raines v. Byrd). Second version folded in: the Thriving Economy Chapter 9 “Trump-proofing” provisions, including the NIH v. APHA split between the Court of Federal Claims and district courts. The House can attach some as FY2028-29 appropriations provisions (18.9). |
| 5.4 | Insurrection Act reform: defined triggers, judicial review, time limits | FL | ① | ◐ | Unchanged. |
| 5.5 | Inspector general independence: notice to Congress and stated reasons for removal, enforced through appropriations | FL | ① | ◐ | The old design, for-cause removal only, is Slaughter-exposed. |
| 5.6 | Close Vacancies Act workarounds for acting officials | FL | ① | ◐ | Unchanged. |
| 5.7 | Publish OLC opinions and end secret law | FL | ① | ◐ | The executive version is in the bridge (5.17); statute makes it durable. |
| 5.8 | Pardon reform: disclosure and a bribery carve-out; a self-pardon ban may need an amendment | FL | ① | ◐ | Clemency is a constitutional power, so statutory limits are exposed (my analysis; not in the project docs). |
| 5.9 | Presidential Succession Act reform; clarify 25th Amendment sec. 4 procedure; continuity of government for mass-casualty events | FL | ② | ◐ | The continuity piece is NEW (Instruments, Part II). |
| 5.10 | Domestic military deployment limits and Posse Comitatus clarification | FL | ① | ◐ | One statute, in EXE, referenced from SAF-2 (“keep soldiers out of routine policing”). The deployment savings stay inside NSC-1's flat defense envelope and are not counted as public-safety revenue. Niskanen: the Guard in DC cut petty property crime but not violent crime. |
| 5.11 | Federal law-enforcement identification requirements; ban on unmarked detentions | FL | ① | ◐ | Unchanged. |
| 5.12 | Tariff authority reclaimed: with IEEPA out after Learning Resources, narrow the sec. 232 and sec. 301 delegations with congressional-approval triggers | FL | ② | ◐ | Current tariffs are in CBO's baseline, so keeping them raises no new revenue (domain-revenue.md); repealing them (EXE-14B) would be a $1.5-1.9T claim, unscored and in no total. → EXE-14. |
| 5.13 | Special counsel independence by structure: judicial appointment or placement outside the executive, plus appropriations and reporting conditions, not for-cause removal | FL | ① | ◐ | Slaughter redesign of the old “special counsel independence codified.” |
| 5.14 | Politicized-prosecution safeguards: give DOJ contact policy statutory force | FL | ① | ◐ | Unchanged. |
| 5.15 | Presidential immunity: statutory pieces only (evidentiary procedures, IG strengthening, criminal statutes that expressly reach presidential conduct); the amendment is held (17.7) | FL | ② | ◐ | Congress cannot overrule Trump v. United States by statute (Rebalancing #21). |
| 5.16 | Independent agencies after Slaughter: rebuild bipartisan commissions with staggered terms, partisan balance, quorum rules and appropriations or reporting conditions; move quasi-judicial functions to Article III or Article I bodies | FL | ① | ◐ | NEW cross-cutting design rule. Touches the FEC (7.3), FERC and NRC (Thriving Economy treats an independent FERC as fundamental), the FCC (12.6) and the FTC. |
| 5.17 | Day-one executive bridge, pre-drafted in opposition: rescind Schedule Policy/Career placements, publish OLC opinions, restore OMB ecosystem-valuation guidance, finalize the OSHA heat rule, reinstate the BLM Public Lands Rule | X | ① | ✔ | Reversible by design: a bridge to the statutes above, not a substitute (design rule 2). The old inventory had almost nothing in the executive column. Items beyond Schedule P/C come from the Thriving Economy map. → EXE-17 for the Schedule P/C rescission. |

## 6. Anti-corruption

**Pointer: canonical in domains/domain-integrity.md (INT-1 to INT-17).**

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 6.1 | Stock ownership and trading ban for members, spouses and dependents, extended to the President, Vice President and Cabinet; divest or blind trust; packaged with congressional staffing (8.1) | FL | ① | ◐ | World: the House passed the narrower Stop Insider Trading Act 232-198 on July 22, 2026 (no new purchases, notice before sales, SAVE America Act provisions attached); Democrats called it a Trojan horse; the Senate Homeland Security Committee advanced a ban in July; Trump and Jeffries back a ban in principle (NOTUS). Some version may enact before 2029, so this row is the floor the Democratic version must hold. Ledger D5. → INT-1. |
| 6.2 | Extend executive-branch revolving-door cooling-off periods | FL | ① | ◐ | Unchanged. |
| 6.3 | Emoluments clauses enforced by statute with a private cause of action | FL | ① | ◐ | Unchanged. |
| 6.4 | Mandatory tax disclosure for presidential and vice-presidential candidates | FL | ① | ◐ | Unchanged. |
| 6.5 | Beneficial-ownership transparency enforced; close the CTA carve-outs | FL | ① | ◐ | Unchanged. → INT-9. |
| 6.6 | Close lobbying-registration loopholes; register shadow lobbying | FL | ① | ◐ | Unchanged. |
| 6.7 | Foreign agent registration reform with real enforcement capacity | FL | ② | ◐ | Unchanged. → INT-11. |
| 6.8 | Financial disclosure extended to senior judiciary and Federal Reserve officials | FL | ② | ◐ | The judiciary half overlaps 4.2; one bill. |
| 6.9 | Ban paid speech and post-service compensation from regulated entities | FL | ② | ◐ | Unchanged. |
| 6.10 | Procurement integrity: bar contractors with adjudicated fraud findings | FL | ② | ◐ | Unchanged. |

## 7. Money in politics

**Pointer: canonical in domains/domain-integrity.md.** NRSC v. FEC (June 30, 2026, 6-3) struck down federal limits on party coordinated expenditures and overruled Colorado II. Contribution limits, earmarking rules and the coordination rules for outside groups stand (Wiley, Skadden, Covington). The Rebalancing review lists the outcome as unconfirmed; it is now known. The anti-corruption amendment is at 17.1.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 7.1 | 6:1 small-dollar matching with voluntary spending caps, no trigger-based matching (Arizona Free Enterprise) | FL | ① | ◐ | Buckley-compatible; ledger D1. A permanent program, paid for at maturity under Dec. D4. **INT-5B: paid from general revenue, with no matching channel or fines surcharge.** Public financing is a parallel track that builds toward nothing (Radical Means, rule 1). → INT-5. |
| 7.2 | DISCLOSE Act | FL | ① | ◐ | Folded into Freedom to Vote (cut C9); ledger D2. Disclosure survives “exacting scrutiny” (Rebalancing). → INT-2. |
| 7.3 | FEC restructuring: an odd-numbered commission or a separated enforcement bureau, designed without relying on removal protection (5.16) | FL | ① | ◐ | Slaughter redesign; goal unchanged. → INT-7; the FEC is named in D9's extended agency list (CAP-7, about $3B). |
| 7.4 | Coordination rules for outside groups tightened; single-candidate super PACs treated as coordinated | FL | ① | ◐ | Narrowed after NRSC: party coordination limits are gone, outside-group rules stand. Spend no floor time on party limits. → INT-8. |
| 7.5 | Shareholder approval requirements for corporate political spending | FL | ② | ◐ | Unchanged in the inventory. Designed in INT-15: Congress can act for public companies through the Securities Exchange Act (S. 530 model); the states can act for corporations chartered in them; First Amendment footing flagged for legal review. |
| 7.6 | Foreign-influenced corporation spending ban (majority-foreign-owned entities) | FL | ② | ◐ | Bluman v. FEC is the precedent (Rebalancing). |
| 7.7 | Montana-style charter-forfeiture initiatives in every initiative state | ST | ⟳ | ✔ | Builds the legal theory that artificial persons are not citizens (Radical Means). |
| 7.8 | State-level public-financing programs as proof of concept | ST | ⟳ | ✔ | Unchanged. |

## 8. Congressional capacity

**Pointer: canonical in domains/domain-capacity.md (CAP-1 to CAP-6, CAP-14 to CAP-17).** A larger House on 1970s staffing is worse than a 435-member one (old inventory).

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 8.1 | Personal and committee staff budgets restored to real 1979 levels; fix pay compression; packaged with the stock ban (6.1) so accountability buys capacity | AP | ① | ◐ | Instruments #15. House committee staff fell from 2,001 (1994) to 1,317 (1995) (CRS via Rebalancing). → CAP-1. |
| 8.2 | Re-establish the Office of Technology Assessment | AP | ① | ◐ | Peak budget $21.3M, staff cap 143; the Modernization Committee endorsed an improved OTA unanimously (Rebalancing). The Takano-Foster-Casten-Beyer bill would rename it the Congressional Office of Technology. → CAP-2. |
| 8.3 | Restore CRS and GAO to at least 1992 levels and rebuild CBO capacity | AP | ① | ◐ | GAO 5,062 (1992) to 2,989 (2015); CRS 838 to 609 (Brookings via Rebalancing; counts vary by method). → CAP-3. |
| 8.4 | Biennial budgeting and an automatic continuing resolution at prior-year levels, with an escalating congressional penalty: no recess, no non-appropriations floor business, suspended member travel | FL | ① | ◐ | Instruments #9: the penalty falls on the body that failed, not on programs. Option: the Merkley-Daines two-day appropriations fast track (path A, sec. 108). → CAP-4. |
| 8.5 | Restore transparent, competitively awarded, capped earmarks | FL | ① | ◐ | Unchanged. → CAP-5. |
| 8.6 | Member housing allowance: the cost of DC residence is a de facto wealth filter | AP | ② | ◐ | Package with 6.1 to blunt the “Congress pays itself” optics. → CAP-14. |
| 8.7 | Legislative-branch technology modernization; unified drafting and scoring systems | AP | ② | ◐ | Unchanged. → CAP-15. |
| 8.8 | Committee jurisdiction realignment for AI, climate and cyber | RU | ② | ✔ | The House side can move in a January 2027 rules package (18.9). → CAP-16. |
| 8.9 | A nonpartisan office that tracks judicial readings of statutes and drafts override legislation | AP | ② | ◐ | NEW (Rebalancing #20); the Ledbetter and Civil Rights Act of 1991 pattern. → CAP-6. |
| 8.10 | Legal-culture investments: congressional clerkships, drafting clinics, legislation courses | X | ⟳ | ✔ | NEW (Rebalancing #20); mostly outside the federal budget. → CAP-17. |

## 9. State capacity and the successor state

**Pointer: canonical in domains/domain-capacity.md (CAP-7 to CAP-13, CAP-18).** Dec. D9: an agency rebuild with statutory staffing floors for the agencies delivery depends on, in two rows: CAP-7S, a front-loaded surge (~$0.6T over FY2030-35, borrowed inside the D4-B envelope as C42), and CAP-7, a sustained increase (~0.12% of GDP from FY2032, ~$0.49T in the window). D9's agency list: IRS service, SSA, HUD, FTA, USCIS, CDC, NOAA, Education and USAID, plus CMS, OPM, the EAC, the FEC and the integrity-enforcement units. Increments over baseline appropriations; estimates, accepted by Espen as working figures, with the per-agency split in CAP-7 and a bottom-up agency review to come.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 9.1 | Agency rebuild: a front-loaded surge (~$0.6T over FY2030-35) plus a sustained increase (~0.12% of GDP from FY2032), with statutory staffing floors | AP | ① | ◐ | Dec. D9 replaces the old +28% nondefense envelope (ledger A1; cut C2). The surge is borrowed inside the D4-B envelope (C42); the sustained line is paid for at maturity. Mandatory funding for named functions through reconciliation is possible where Byrd-eligible (unchecked). Design rule 6: every delivery item names its agency. → CAP-7S, CAP-7. |
| 9.2 | Civil service modernization: real performance management and real political insulation | FL | ① | ◐ | A prerequisite for every ramp time (Radical Means). After Slaughter, insulation rests on career-employee protections and structure, not for-cause removal of officers. → CAP-9. |
| 9.3 | Prohibit Schedule Policy/Career (the rebranded Schedule F) by statute | FL | ① | ◐ | World: OPM published the final rule Feb 6, 2026; it took effect in March 2026; OPM estimates about 50,000 positions, 2% of the workforce; the President places positions by executive order (CRS LSB11412; Federal Register). The old row said “Schedule F prohibition codified”; the rule now exists, and its executive rescission is in 5.17. → CAP-8. |
| 9.4 | Successor architecture for demolished development functions | FL | ① | ◐ | Draft in opposition (9.10). USAID’s funding sits in 9.1. → CAP-10. |
| 9.5 | Successor architecture for education functions, with enforcement separated from policy | FL | ① | ◐ | Pairs with EDU-1 and EDU-5; EDU-6's Education Department protections are proposed to ride CAP-8. → CAP-10. |
| 9.6 | Federal hiring reform: time-to-hire targets, direct-hire authority, salary flexibility | FL | ① | ◐ | Unchanged. → CAP-11. |
| 9.7 | Permitting and environmental review reform | FL | ① | ◐ | Three wordings folded as options: (A) the old inventory’s categorical exclusions, deadline enforcement and judicial-review limits; (B) the Thriving Economy package of technology-neutral review, a ban on retroactive permit or lease cancellation, expedited challenges that keep third-party standing, and FERC authority over national-interest lines; (C) ledger E3. B is bipartisan-capable. The 2026-28 permitting deal (AAJA) is stipulated as enacted (D1). → CLI-3 and CLI-6, with AAJA. |
| 9.8 | Federal technology procurement reform; in-house engineering capacity | FL | ② | ◐ | Unchanged. → CAP-12. |
| 9.9 | State and local capacity grants: implementation is where federal policy dies | AP | ② | ◐ | Supply with demand (design rule 5). → CAP-13 (unsourced, about $0.03T). |
| 9.10 | Draft all successor legislation in opposition, 2027-28, so text exists on day one, including the express-delegation templates (4.8) | X | ⓪ | ✔ | Unchanged in substance. → CAP-18. |

## 10. Delivery (pointers to the domain files and ledger rows)

Each row points to its domain file and ledger row; the domain file governs, and the ledger carries the decisions. Delivery rides reconciliation and structure rides the floor (Radical Means). Legibility and recurring-beats-one-time are standing design rules (rule 3), not rows.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 10.1 | Reconciliation vehicles per Dec. D5: R1 on the FY2029 resolution (about week 8 of 2029), R2 on FY2030 (fall 2029), R3 on FY2031 (summer 2030); if the FY2029 slot is lost, R1’s contents move to R2 | R1/R2/R3 | ① | ✔ | Fallback cost: first Child Tax Credit checks slip from mid-2029 to mid-2030 and the 2029 transportation act moves to fall 2029 (Dec. D5 table). Three bills are a precondition for Moving America’s 2030 act. |
| 10.2 | FAM-1 Child Tax Credit: $3,600 under 6 and $3,000 ages 6-17, fully refundable, paid monthly, indexed, paired with the corporate-rate row in R1 | R1 | ① | ✔ | domain-family.md FAM-1: about $1.5T, range $1.3-1.8T, 2030-39 (scaled from TPC's American Family Act score; needs a fresh score against current law, which already has a $2,200 credit). Fallbacks: FAM-1B supplement only (about $0.45T), FAM-1C refundability only. Dec. D3: counted in the household net test. Felt about five months after enactment. → FAM-1. |
| 10.3 | REV-C1 Economy-wide carbon fee and dividend: $25 a ton in 2030 rising to about $100 by 2037, upstream on coal, gas and non-transport petroleum; gasoline and diesel exempt; 80% dividend, 20% transition and low-income help; domestic fee only. REV-C2, the border adjustment, is carved out and finances the Thriving Economy add-ons (10.5, 14.10) | R2 | ① | ✔ | Dec. D7 as built in domain-revenue.md: REV-C1 raises $1.20-1.50T (mid $1.35T, est., 2030-39), dividend about $1.08T, transition share about $0.27T; REV-C2 raises about $0.15-0.25T (mid $0.20T) and rides R3 with the add-ons. Keeping the border adjustment out of REV-C1 counts it once (revenue audit finding 2) and costs the dividend about $0.16T, roughly $48 a person a year, which the incidence model carries. REV-C2 is scaled from Thriving Economy’s $120-240B for the border adjustment with methane and industrial fees, so methane fees are not additional to it. The base shrinks as emissions fall, so these fund rebates and time-limited spending, not permanent programs. → REV-C1, REV-C2, CLI-2. |
| 10.4 | AI dividend: a levy on frontier compute or AI-attributable revenue, rebated per capita; open whether it shares the carbon dividend’s channel | R2/R3 | ② | ◐ | Instruments #11 picks the levy over a data royalty or a sovereign equity stake. Unscored; Byrd eligibility unchecked. Legibility asks for one visible dividend channel, so decide whether to merge. → AI-6 (held). |
| 10.5 | Utility relief as a named line on the bill, not a credit to the utility: LIHEAP and Weatherization expansion, a permanent LIHWAP | R3 | ① | ✔ | Thriving Economy mandatory-spending list; Dec. D5 puts its add-ons in R3. The carbon fee’s 20% share (10.3) is the natural funding source. Ledger E4. → CLI-5. |
| 10.6 | Health (domain-health.md, Dec. D6): HLT-1 Restore, HLT-4 Medicaid and safety net, HLT-6 Medicare payment reform (R1); HLT-2 Medicare upgrades with dental, vision and hearing and no eligibility change (R2) | R1/R2 | ① | ✔ | domain-health.md: base package net about $3.7T mid (range $2.2-5.2T), 2030-39, about $1.2T below the go-big bill as written ($4.85T mid) because Medicare at 60 moves out ($0.30-0.36T) and all Medicare Advantage overpayment is captured (a further $0.6-1.1T). HLT-1 $2.45T, HLT-2 $1.07T, HLT-4 $0.63T, HLT-6 -$1.95T (mid), of which about $0.7T (est.) accrues to Medicare HI and -$1.25T to the general fund. The ledger's HLT-2 excludes Medicare at 60. → HLT-1, HLT-2, HLT-4, HLT-6. |
| 10.7 | Health regular-order titles: HLT-3 public option guarantee with auto-enrollment; HLT-5 prices and market power (hospital cap at 200% of Medicare, commercial drug negotiation and $2,000 cap, PBM and insurer divestitures) | FL | ① | ◐ | domain-health.md: HLT-3 $1.90T, HLT-5 -$0.40T (merged into the HLT-3 bill), 10 floor days together; survives at 51 only with the D2 rules change and every vote; D1 lists HLT-3 among the bills that must pass in the first trifecta. The go-big file's Title V also carried a non-compete ban; its one home is COM-4. → HLT-3, HLT-5. |
| 10.8 | Medicare buy-in add-ons, each scored separately and not in the base: HLT-A2 at 60 ($0.30-0.36T, sourced) or HLT-A3 at 55 (about $0.6-0.9T, est., needs a score); dental (HLT-A1) is scored separately but kept in the base | R2 | ① | ✔ | Dec. D6; domain-health.md. An add-on rides R2 with HLT-2 if it can be paid for there, otherwise R3 or later. HLT-A4 (Medicare for Kids, Medicare at Home) each need a broad-based tax and are not in the plan. → HLT-A1 to A4. |
| 10.9 | FAM-2 Child care and pre-K, phased: universal voluntary pre-K and a lowest-income tier (free below 75% of state median income) with supply grants and wage parity in 2030-31, then the 7%-of-income cap for families up to 250% of state median from 2032 | R2 | ① | ✔ | domain-family.md: about $0.6T, range $0.4-0.9T, 2030-39 (scaled from CRFB $475-800B through 2031). Options: FAM-2B full cap from 2030 ($0.9T), FAM-2C pre-K only ($0.2-0.3T). The phasing is the file author’s choice under design rule 5, not a Decision; flip to B if leading with the full cap is preferred. FAM-2D adds the omnibus pre-K standards. Felt partly (pre-K) by Nov 2030. → FAM-2. |
| 10.10 | FAM-3 Paid family and medical leave: 12 weeks of social insurance, two-thirds wage replacement up to a cap, 0.6% contribution split between employer and worker, its own fund, stepping automatically toward 0.85% if the reserve falls below a year of benefits, with a repayable Treasury loan instead of a general-fund backstop | R2 | ① | ✔ | domain-family.md: cost about $0.9T (range $0.6-1.4T, est.; CBO $547B for a 12-week FAMILY Act design), revenue about $0.9T (up to about $1.28T at the cap), nothing from the general fund (revenue audit finding 7). A worker earning $60,000 pays $180 a year, up to $255 at the cap (counted in the D3 test). Options: FAM-3B fully general-fund, FAM-3C 4 weeks, FAM-3D 0.85% from the start, FAM-3E the open general-fund backstop. Benefits start 2031, so not felt by Nov 2030. → FAM-3. |
| 10.11 | Education and opportunity (Title I to $26B, IDEA glide path to 40%, Pell maximum $9,500 indexed, SAVE and PSLF in statute), mandatory funding; plus Veterans Health and Capacity | R2 | ① | ✔ | domain-education.md: EDU-1 (Title I and IDEA, carrying EDU-2) about $0.33T and EDU-5 (Pell, SAVE and PSLF) about $0.32T, 2030-39, unscored (SAVE and PSLF $0.1-0.3T is the sensitive piece); the education file adds EDU-3 (universal meals, $0.27T), EDU-4 and EDU-7. Veterans Health and Capacity: NSC-10, $0.07T, estimate. Family general-fund total across FAM-1 to FAM-3: $1.70 / 2.10 / 2.70T. → EDU-1, EDU-5; NSC-10. |
| 10.12 | Junk-fee ban: cheap, broad, badly attributed; do it anyway | FL | ① | ◐ | Ledger E10. Write attribution into the statute. → COM-5 (merged into the competition bill, C24). |
| 10.13 | Housing production and permitting: emergency aid, construction capital, vouchers and LIHTC in R2; zoning conditions on the regular floor | R2 | ① | ✔ | domain-housing.md: the R2 title (HOU-1, about $0.47T, est.) and a floor bill (HOU-7, 3 days); HOU-3C's construction capital is state revolving-fund grants (borrowed, C21) plus direct loans at subsidy cost, and HOU-5's repair is borrowed (C31). Wave ① because Dec. D5 puts housing in R2. The zoning conditions are ◐. Supply with demand. → HOU-1 to HOU-8. |
| 10.14 | Social Security (domain-social-security.md, Dec. D8): SS-1 12.4% above $250K with a benefit credit; SS-2 12.4% on investment income above $400K; SS-3 higher minimum benefit; SS-4 CPI-E; regular-order bill in spring 2030 | FL | ① | ◐ | Barred from reconciliation (sec. 310(g)). Against the 2026 Trustees gap of 4.42% of payroll (depletion 2034, 83% payable): SS-1 +2.30, SS-2 +1.17 before and about +0.99 after a 15% stacking haircut (ledger OX), SS-3 -0.11, SS-4 -0.33 (estimates on SSA's 2026 scores, index/dedicated-funds.md); baseline net about +2.85, or about 64% of the gap, with depletion moved to about 2062. It does not reach balance; closers SS-5 to SS-9 cover the remaining 1.6 points, and the file recommends baseline plus SS-5 (S-corp and limited-partner investment income, +0.87; about 84% with it, depletion about 2081) as an option, not yet decided. Ten-year trust-fund revenue about $2.8T mid after the haircut (SS-1 about $1.9T, SS-2 about $0.75-1.2T). SS-2 stacks with REV-H1b on investment income above $400K; both carry the haircut. SS-10 (a bipartisan 67-vote track) is an option to test. → SS-1 to SS-10. |
| 10.15 | Moving America: the 2029 reconciliation act (R1) and the 2030 act (R3); fuel-tax steps are the only tax on gasoline and diesel (Dec. D7); the Highway Trust Fund stays whole (Dec. D4) | R1/R3 | ① | ✔ | Ledger MOV-29 (net deficit reduction about $33.3B, FY2029-38) and MOV-30 (about $4.2B, FY2030-39); project estimates, not CBO or JCT scores. Their general-fund top-ups (~$0.35T) are time-limited capital borrowed under D4 (C30). MOV-30 is scored on the wrong window if carried on the FY2031 resolution and needs rescoring. The 2028 extension is at 18.10. |
| 10.16 | Moving America Act of 2031: authorization (expansion appropriations, contract authority, privacy, continuation) | FL | ② | ◐ | Ledger MOV-31: $0.12-0.17T from the general fund, FY2032-36 (project estimate). |

## 11. Economic structure and the revenue base

Delivery is mostly transfers, which is the submerged-state failure mode; structure is how to avoid it (old inventory).

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 11.1 | Revenue base (domain-revenue.md, Dec. D3, D4): REV-G1 corporate 21% to 28%, G3 top rate 39.6% above $400K, G11 annual mark-to-market for the very top (replacing G4’s 25% minimum tax, ledger C22), G5 buyback tax and corporate minimum, G6 gains at death, G7 foreign income, G8 IRS enforcement, G9 reverse 2025 cuts above $450K, G10 financial transaction tax, H1b Medicare and investment-income rates to 5% above $400K, less the GX overlap; new general-fund revenue comes from the top 1% and corporations | R1/R2 | ① | ✔ | domain-revenue.md: base total $5.71 / 6.37 / 7.12T, 2030-39 (scaled mostly from Treasury and CBO; G8 and G9 estimates). Channel split: REV-H1a (pass-through extension, about $0.5T) plus HLT-6’s Part A share (about $0.7T) go to Medicare HI; REV-H1b (about $0.5T) is in the general-fund base, not HI. G8 counts in the base but CBO may not score it on a given vehicle; whether it is net of the IRS allocation in CAP-7 is unchecked. R1 carries G1, G7, G9; R2 carries G3, G11, G5, G6, G10 and the carbon fee. G11 is the most legally exposed row (Moore, realization) and never pays alone for a permanent program. Ledger: general-fund claims about $10.97T mid against the $6.37T base, a gap of about $4.60T. Under D4-B (Decision Brief 2) it is closed by accepted revenue of $3.53T (Package B: C18 top-end rates, C35 estate tax, C19b employer-exclusion cap at the 75th percentile, C20 $100K/$200K surtax; the sprint package C38; C39-C41, REV-TS12, HP1 and HP3) and $1.15T of time-limited lines borrowed inside the investment envelope (C21, C30-C32, C37, C42), leaving about −$0.08T; no program trims are taken. The surtax and exclusion cap reach upper-middle households; the incidence model's scenario Q puts every quintile below the top ahead (Q4 about +$1,087 a year). Stacking on investment income above $400K is priced: a 15% haircut on H1b (inside GX) and on SS-2 (OX). D4 keeps HI whole on a 75-year window, so its ~$0.3T surplus stays as reserve. → REV-G1 to G11, H1b, GX. |
| 11.2 | Non-compete ban: codify the FTC rule | FL | ① | ◐ | Second version: also in the health bill’s Title V. One home: COM-4; HLT-5 references it. Ledger E9. → COM-4. |
| 11.3 | Merger review standards and enforcement funding; antitrust in labor markets, with monopsony as an enforcement priority | FL | ② | ◐ | Ledger E9; funded by merger-filing fees (MF1). → COM-1, COM-2, COM-3. |
| 11.4 | Sectoral bargaining and the PRO Act: Byrd-ineligible, slow, schedule honestly | FL | ② | ◐ | Ledger E7: no federal cost (est.); the labor bill takes 8 floor days. Sectoral bargaining (LAB-3B) is held. → LAB-1, LAB-2, LAB-3, LAB-7. |
| 11.5 | Living wage ($17, then indexed) and a small-business credit | FL | ① | ◐ | Ledger E8: the credit rides reconciliation (R2); the mandate needs the regular floor. → LAB-4 (mandate), LAB-5 (credit). |
| 11.6 | Financial regulation restoration: leverage and stress-test authority | FL | ② | ◐ | Held in domain-competition.md (could join COM-6), for Espen's call. |
| 11.7 | Corporate governance: board representation for workers | FL | ② | ◐ | Held in domain-labor.md (codetermination), for Espen's call. |
| 11.8 | Public banking option; postal financial services | FL | ② | ◐ | Held in domain-competition.md, for Espen's call. |

## 12. Information environment

**Pointer: canonical in domains/domain-ai.md (AI-7 to AI-10).**

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 12.1 | Local journalism support through payroll credits conditioned on ownership: exclude private-equity-controlled chains, weight toward nonprofit and locally held outlets, add a one-time conversion fund | R2/R3 | ① | ◐ | Instruments #12; not content regulation. Ledger AI-9, about $0.02T (est., R2); Byrd-eligible if it is a pure tax credit (unchecked). → AI-9. |
| 12.2 | Platform transparency, researcher data access, default-setting requirements and age-appropriate design | FL | ① | ◐ | Instruments #13 (Moody v. NetChoice). Replaces “Section 230 reform limited to algorithmic amplification,” which is dropped. → AI-7. |
| 12.3 | Synthetic-media disclosure in political advertising | FL | ① | ◐ | Rides DEM-1. Fraud-side AI offenses are SAF-9. → AI-8. |
| 12.4 | Public media funding insulated from the appropriations cycle | FL | ② | ◐ | → AI-10. |
| 12.5 | Ad-targeting restrictions for political advertising | FL | ② | ◐ | First Amendment exposure is higher than at 12.2 (my estimate). Held in domain-ai.md. |
| 12.6 | Media ownership concentration limits restored | FL | ② | ◐ | Needs an FCC design that survives Slaughter (5.16). Held in domain-ai.md. |
| 12.7 | Government transparency: FOIA processing capacity and a statutory presumption of disclosure | FL | ① | ◐ | The old row was executive action; the durable form is statute (design rule 2). → AI-10. |

## 13. AI governance

**Pointer: canonical in domains/domain-ai.md (AI-1 to AI-6, AI-11).** D1 puts AI-1 and AI-4 among the bills that must pass in the first trifecta, so ledger cut C13 (moving AI governance to 2031) is not taken.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 13.1 | Compute and capability reporting thresholds | FL | ① | ◐ | Ledger E12; the AI bill, about $0.02T (est.), 5 floor days. → AI-1. |
| 13.2 | Labor transition authority triggered by measured displacement | FL | ① | ◐ | Ledger E12: wage insurance and training accounts on R3 ($0.20T, est.). A candidate funding source is the AI levy (10.4). → AI-4. |
| 13.3 | Resolve federal preemption deliberately rather than by default | FL | ① | ◐ | → AI-2. |
| 13.4 | Pre-deployment evaluation requirements for frontier systems | FL | ② | ◐ | → AI-3. |
| 13.5 | Public compute and public model capacity | AP | ② | ◐ | → AI-5. |
| 13.6 | Liability allocation for autonomous systems | FL | ② | ◐ | Held in domain-ai.md. |
| 13.7 | Due-process requirements for algorithmic decisions in government | FL | ② | ◐ | → AI-5. |
| 13.8 | International coordination on frontier safety | T | ② | ✖ | Executive agreements are ✔; a treaty is ✖ (domain-ai.md). |
| 13.9 | AI-enabled fraud and impersonation: verification, a federal offense for cloned voices and likenesses, defensive AI | FL | ① | ◐ | → SAF-9 (domain-public-safety.md). |

## 14. Climate as a democracy problem

**Pointer: canonical in domains/domain-climate.md (CLI-1 to CLI-13).** Source: the Thriving Economy map, stages 3a (reconciliation) and 3b (60 votes or a rules change). The map attaches no scores, so dollar figures here come from ledger rows or are unscored.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 14.1 | Rebuild disaster response as a legitimacy asset: a cabinet-level FEMA with Senate-confirmed leadership and its own IG, a mitigation set-aside of $1 per $1 of disaster supplemental, a Universal Survivor Application, permanent CDBG-DR | FL | ① | ◐ | The Thriving Economy counteroffer to the FEMA Review Council (final report May 2026). Also negotiable in 2027-28 at 60 votes (18.10). → CLI-7, CLI-8. |
| 14.2 | Property-insurance backstop: a means-tested Climate Insurance and Recovery Affordability Program, NFIP premium support, resilience revolving loan funds | R3 | ① | ✔ | Thriving Economy mandatory-spending list; Dec. D5 puts its add-ons in R3. Unscored. → CLI-7 (CLI-7B moves it to R3). |
| 14.3 | Insurance data partnership with a Treasury backstop; climate-risk disclosure at sale or lease; forward-looking risk in GSE, FHA and VA underwriting | FL | ② | ◐ | Thriving Economy 3b; partisan and Byrd-ineligible. → CLI-7, CLI-8. |
| 14.4 | Managed retreat: a permanent voluntary relocation program with buyouts, receiving-community investment and revenue bridges for origin towns | R3 | ② | ✔ | Thriving Economy 3a. The map flags a tension with its rural-development goals. → option CLI-5C. |
| 14.5 | Grid reliability and interconnection reform: connect-and-manage or consolidated interconnection with study deadlines, Order 1920 codified, a large-load ratepayer floor | FL | ① | ◐ | Ledger E3 and E5. → CLI-6. |
| 14.6 | Adaptation finance for local governments: CPRG reappropriated, STAG expanded, a Clean Energy State Revolving Fund | R3 | ② | ✔ | The CPRG round drew more than $30B in requests for about $4.5B (Thriving Economy). → CLI-5 (adaptation finance, borrowed under C37). |
| 14.7 | Supply-chain resilience for medical and critical goods: minerals price floors, federal offtake, a Strategic Resource Reserve | R3 | ② | ✔ | Some pieces are bipartisan now (Thriving Economy, stage 1b). → CLI-5 (minerals offtake, borrowed under C37). |
| 14.8 | Heat and extreme-weather labor standards: codify OSHA’s heat rule | FL | ① | ◐ | The executive version is in the bridge (5.17). → LAB-6 (domain-labor.md). |
| 14.9 | Restore and expand clean-energy credits (25C, 25D, 30D, 25E, 30C, the Clean Electricity ITC, a transmission ITC, 45X) as refundable, direct-pay and point-of-sale | R2 | ① | ✔ | Ledger E1: $0.9T, 2030-39 (scaled; OBBBA repeal saved $571B, 2025-34, per CRFB). The transmission ITC and 45X live in CLI-5. → CLI-1. |
| 14.10 | Thriving Economy add-ons: transmission ITC, 45X expansions, resilience credits, agricultural R&D | R3 | ① | ✔ | Ledger E4: about $0.60T gross (range $0.3-1.0T, est.), financed by D7’s 20% transition share (~$0.27T) and REV-C2 (~$0.20T); about $0.13T falls on the general fund at the midpoint, and C37 (accepted) borrows for the ~$0.10T of capital lines, so CLI-5 is kept whole rather than trimmed (C29). → CLI-5 (CLI-5F). |

## 15. Civic infrastructure

**Pointer: canonical in domains/domain-democracy.md (DEM-16 to DEM-20); national service in domains/domain-labor.md (LAB-9).**

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 15.1 | Universal national service option, paid with an education benefit, with cross-regional and cross-class placement written into the statute | FL | ① | ◐ | Instruments #14: mixing is the mechanism. A permanent program, paid for at maturity under D4-B. LAB-9D (Decision Brief 2): bipartisan authorization first, LAB-9A's R2 money as fallback; the ledger keeps LAB-9A's ~$0.12T. → LAB-9. |
| 15.2 | Civic education funding tied to participation outcomes | FL | ② | ◐ | → DEM-16. |
| 15.3 | Public space, library and community infrastructure investment | AP | ② | ◐ | Time-limited capital, borrowed inside the D4-B envelope (C32, accepted). → DEM-17. |
| 15.4 | Deliberative democracy pilots: citizens’ assemblies on referred questions | FL | ② | ◐ | → DEM-18. |
| 15.5 | Protect the citizen initiative process from legislative nullification | ST | ⟳ | ✔ | → DEM-19. |
| 15.6 | Limit state preemption of local government | ST | ⟳ | ✔ | → DEM-20. |

## 16. The international order and defense

**Pointer: canonical in domains/domain-national-security.md (NSC-1 to NSC-11).** The old inventory called this a second agenda. It stays thin by design.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 16.1 | Alliance architecture: burden-sharing formalized rather than improvised | T | ② | ✖ | Executive agreement is ✔; treaty-level changes stay ✖. → NSC-3. |
| 16.2 | Trade: a successor framework to a WTO with a non-functional appellate body | T | ② | ✖ | Held. See 5.12 for tariff authority. → NSC-6. |
| 16.3 | Development finance rebuilt for a post-USAID landscape | FL | ② | ◐ | USAID’s funding is inside the agency rebuild (9.1). → NSC-4 with CAP-10. |
| 16.4 | Pandemic preparedness and IHR reform | T | ② | ✖ | → NSC-8 (~$0.02T, est.). |
| 16.5 | Sanctions policy reform: multilateral by default, sunset clauses | FL | ② | ◐ | → NSC-5. |
| 16.6 | Treaty ratification reform: congressional-executive agreements as the working default | FL | ② | ◐ | → NSC-6. |
| 16.7 | Climate finance commitments made durable against political reversal | T | ② | ✖ | Domestic statutory commitments are ◐. → NSC-9. |
| 16.8 | Defense: roughly flat in real terms, with any increase paid for inside the defense budget | AP | ① | ◐ | Dec. D9; NSC-1A confirmed (Decision Brief 2), with a study of reducing defense over time to come. Replaces ledger A2 (+3.2%) and cut C1. NDAA-driven. → NSC-1. |

## 17. Amendments, in ratification order

**Pointer: canonical in domains/domain-amendments.md (AMD-1 to AMD-11; row 17.n is AMD-n).** Sequenced by coalition breadth, not importance. Realistically this list holds one plausible amendment in twenty years (old inventory), so the first ratification is chosen as the proof of concept. Every amendment row is ✖ at any Senate size.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 17.1 | Anti-corruption and campaign finance: the ratification pathfinder | A | ⟳ | ✖ | 75-80% support, cross-partisan, no small-state disadvantage; if it cannot reach 38 states, none can (Radical Means). |
| 17.2 | Judicial term limits: constitutionalize the statute (4.15) | A | ⟳ | ✖ | Welch-Manchin (2024) and H.J.Res. 174 (119th Congress). Support: 79% (Marquette, Sept 2026) against the old inventory’s “about 70%.” |
| 17.3 | National popular vote (Bayh-Celler lineage), carrying presidential ranked-choice voting or a runoff (2.15) | A | ⟳ | ✖ | The real opposition is seven swing states, not twenty-five small ones (Radical Means). |
| 17.4 | Senate suspensive veto on the Parliament Act model: equal suffrage kept, the absolute veto removed | A | ⟳ | ✖ | Largest available gain, highest legal variance; held option. |
| 17.5 | An affirmative individual right to vote | A | ⟳ | ✖ | Appeared twice in the old inventory; now once. |
| 17.6 | 23rd Amendment repeal | A | ⟳ | ✖ | Hygiene after the statutory fix in 2.7. |
| 17.7 | Presidential-immunity amendment, only if Trump v. United States proves unworkable | A | ⟳ | ✖ | The 2024 “No One Is Above the Law” proposal (Rebalancing). |
| 17.8 | Legislative override or a supermajority to invalidate statutes, only inside an amendment package | A | ⟳ | ✖ | The statutory version is likely unconstitutional and the highest escalation risk (Rebalancing #17). Held. |
| 17.9 | Convention procedure statute: delegate apportionment and voting rules, which Article V leaves open | FL | ② | ◐ | NEW (Instruments, Part II). |
| 17.10 | Ratification operations: name the 38 target states and sequence by coalition; model legislation and an interstate legislator coordination body; bilateral candidate pledge machinery extracted in primaries | ST | ⟳ | ✔ | Unchanged. |
| 17.11 | Convention applications drafted with subject limits and rescission triggers: leverage, not intent | ST | ⟳ | ✔ | The Seventeenth Amendment moved partly because a convention call sat a state or two from triggering (Radical Means). |

## 18. The 2026-28 groundwork (as of Oct 19, 2026; Election Day is Nov 3)

“0” items happen before the trifecta, under a Trump veto and the 60-vote Senate.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 18.1 | Win 52-54 Senate seats (Dec. D1); Class 2 seats run through January 2033 and are the senators who vote on the enabling layer; tag everything at 51; treat 56+ as upside | — | ⓪ | ✔ | Unchanged in substance; the target was “52+.” |
| 18.2 | Flip either chamber to freeze the FY2029 slot; if it is not frozen, R1’s contents move to R2 (Dec. D5) | — | ⓪ | ✔ | Radical Means: a divided Congress cannot adopt a budget resolution, so a flip freezes the slot. |
| 18.3 | Watch the Merkley-Daines lame-duck push: a rules change needs 67 to end debate, and Daines retires in January; the outcome is step 0 of D2 | RU | ⓪ | ✖ | Senate doc. Daines’s departure costs persuasion more than arithmetic. |
| 18.4 | Extract public rules-reform commitments in 2027 while they are cheap, aimed at a set of paths rather than one | — | ⓪ | ✔ | Reworded for D2. |
| 18.5 | Announce the reciprocal nominations standard out loud | — | ⓪ | ✔ | Unchanged. |
| 18.6 | Put NPVIC commitments on state legislative candidate questionnaires this fall and target the compact states’ chambers as one operation with the Senate map | ST | ⓪ | ✔ | NPV: the six target states hold 65 electoral votes and 48 are needed (April 2026 status; the Daily Signal, Oct 3, 2026, still shows 48 short). |
| 18.7 | Build hearing records on House size (cube root) and STV in the 2027-28 Senate | — | ⓪ | ✔ | Reworded for 2.1 and 2.3. |
| 18.8 | Pre-draft in opposition: successor-agency legislation (9.10), the day-one executive bridge (5.17) and reconciliation text for R1-R3 | X | ⓪ | ✔ | Thriving Economy: committees can mark up stage 3 bills in 2028. |
| 18.9 | If the House flips: FY2028-29 appropriations that restore cancelled awards and carry the Trump-proofing provisions (5.3), oversight records, and a January 2027 rules package that re-creates a climate select committee | AP | ⓪ | ✖ | The rules package and hearings are ✔ (House-only); appropriations face the veto and 60 votes. |
| 18.10 | Must-pass vehicles at 60 votes: farm bill, surface transportation (IIJA authorizations run to Dec 11, 2026), NFIP, WRDA, NDAA, FAA in 2028; plus the Highway Trust Fund extension before Sept 30, 2028 that Moving America needs | FL | ⓪ | ✖ | CRS (Sept 14, 2026) via the Thriving Economy map. The general-fund transfer in the extension is unsized (ledger); the fund runs dry in 2028 (revenue file, CBO). |
| 18.11 | Pre-draft state-level fallbacks for each federal reform, so a Court loss becomes a state campaign rather than a dead end | ST | ⓪ | ✔ | NEW (Instruments, Part IV #5). |

## 19. Rights, immigration and public safety

**Pointer: canonical in domains/domain-immigration.md, domains/domain-rights.md and domains/domain-public-safety.md.** The old inventory had no rows for these. They are listed so the inventory covers the whole ledger; each home file governs.

| ID | Item | Vehicle | Wave | @51 | Basis, ties and changes from the old inventory |
| --- | --- | --- | --- | --- | --- |
| 19.1 | Comprehensive immigration reform | FL | ① | ◐ | Ledger E11: about -$0.14T, est.; 12 floor days. D1: must pass in the first trifecta. Pairs with 4.5 (CRT-5). → IMM-1 to IMM-6. |
| 19.2 | Reproductive Freedom Act | FL | ① | ◐ | Ledger S1. → RTS-1 (RTS-2 its appropriations half). |
| 19.3 | Equality Act | FL | ① | ◐ | Ledger S2. → RTS-3. |
| 19.4 | Justice and public-safety reform: cannabis, sentencing, policing | FL | ① | ◐ | Ledger S3; Bill Book 24 folds in as options. → SAF-2 (policing), SAF-11 (sentencing, cannabis, reentry). |
| 19.5 | Universal background checks | FL | ① | ◐ | Ledger S4; Bill Book 16 folds in as an option. → SAF-5. |
| 19.6 | Safe Everywhere federal titles: clearance, hiring with standards, prevention, anti-fraud, Safety Compacts | AP | ① | ◐ | Ledger SAF-10: about $12.1B a year by title plus $0.8B one-time, 2030-39 about $0.11-0.14T; the domain file's chosen design (SAF-10A) makes it mandatory spending in R3 (Byrd unchecked), which governs over this row's AP tag; its durable revenue sources (PS1) raise about $9.2B a year ($0.09T), leaving a general-fund residual of about $0.03T (proposals, not sourced estimates). The alcohol tax is in the incidence model. → SAF-10. |

# Analysis

## Counts (computed from the tables above)

208 rows. The old inventory said “roughly 190 items” (its own estimate).

| @51 tag | Rows | Share |
| --- | --- | --- |
| ✔ survives at 51 | 45 | 22% |
| ◐ needs a D2 majority-precedent path | 144 | 69% |
| ✖ needs 60, 67 or Republican votes | 19 | 9% |

| Vehicle group | Rows | Share |
| --- | --- | --- |
| Regular-order statute | 121 | 58% |
| Reconciliation (R1-R3) | 20 | 10% |
| Appropriations or mandatory funding | 15 | 7% |
| Senate or House rules | 14 | 7% |
| State level | 13 | 6% |
| Constitutional amendment | 9 | 4% |
| Executive action or declared norm | 6 | 3% |
| Treaty | 5 | 2% |
| Operations (no vote) | 5 | 2% |

| Wave | Rows |
| --- | --- |
| ⓪ | 13 |
| ① | 115 |
| ② | 60 |
| ⟳ | 20 |

Regular-order bills in the first Congress (FL, ①): 80. The ledger groups them into 21 contested regular-order bills and counts the first Congress at 172 Senate floor days under path F against a budget of 163.

## What the dual tag shows

- **At 51 the base package is reconciliation, state work and executive action.** Only the ✔ rows survive without a rules change, and most of them are the R1-R3 delivery rows in Section 10, the revenue base, state-level compact and reform work, and executive bridges.
- **Structural reform lives or dies on D2.** The ◐ rows are the large majority. D2's path F carries them at 52-54 seats if the rules change holds; under path A or B (60 or 55 votes) they would need Republicans, 7-8 at A and 1-3 at B (Senate doc estimate).
- **Reconciliation’s sorting power is intact.** What moves money rides R1-R3 and what changes a rule takes the floor; the ✔/◐ split is that sort. The reconciliation dial (1.9) is the only D2 item that could take the ✔ rows away; D2 leaves reconciliation as now.

## Rows that survive at 51 (✔)

| ID | Row |
| --- | --- |
| 1.11 | House |
| 1.12 | Blue slip for district judges |
| 2.12 | National Popular Vote Compact to 270 |
| 2.14 | Tighten the compact’s withdrawal blackout window |
| 2.17 | Fusion voting authorization |
| 2.18 | Ranked-choice voting and open primaries, framed as anti-corruption |
| 4.17 | [T3] Jurisdiction-stripping restraint |
| 4.18 | [T3] Impeachment reserved for corruption and serious misconduct, never for rulings |
| 4.19 | State supreme court selection reform |
| 5.17 | Day-one executive bridge, pre-drafted in opposition |
| 7.7 | Montana-style charter-forfeiture initiatives in every initiative state |
| 7.8 | State-level public-financing programs as proof of concept |
| 8.8 | Committee jurisdiction realignment for AI, climate and cyber |
| 8.10 | Legal-culture investments |
| 9.10 | Draft all successor legislation in opposition, 2027-28, so text exists on day one, including the express-delegation... |
| 10.1 | Reconciliation vehicles per Dec. D5 |
| 10.2 | FAM-1 Child Tax Credit |
| 10.3 | REV-C1 Economy-wide carbon fee and dividend |
| 10.5 | Utility relief as a named line on the bill, not a credit to the utility |
| 10.6 | Health (domain-health.md, Dec. D6) |
| 10.8 | Medicare buy-in add-ons, each scored separately and not in the base |
| 10.9 | FAM-2 Child care and pre-K, phased |
| 10.10 | FAM-3 Paid family and medical leave |
| 10.11 | FAM-4 Education and opportunity (Title I to $26B, IDEA glide path to 40%, Pell maximum $9,500 indexed, SAVE and PSLF... |
| 10.13 | Housing production and permitting |
| 10.15 | Moving America |
| 11.1 | Revenue base (domain-revenue.md, Dec. D3, D4) |
| 14.2 | Property-insurance backstop |
| 14.4 | Managed retreat |
| 14.6 | Adaptation finance for local governments |
| 14.7 | Supply-chain resilience for medical and critical goods |
| 14.9 | Restore and expand clean-energy credits (25C, 25D, 30D, 25E, 30C, the Clean Electricity ITC, a transmission ITC,... |
| 14.10 | Thriving Economy add-ons |
| 15.5 | Protect the citizen initiative process from legislative nullification |
| 15.6 | Limit state preemption of local government |
| 17.10 | Ratification operations |
| 17.11 | Convention applications drafted with subject limits and rescission triggers |
| 18.1 | Win 52-54 Senate seats (Dec. D1) |
| 18.2 | Flip either chamber to freeze the FY2029 slot |
| 18.4 | Extract public rules-reform commitments in 2027 while they are cheap, aimed at a set of paths rather than one |
| 18.5 | Announce the reciprocal nominations standard out loud |
| 18.6 | Put NPVIC commitments on state legislative candidate questionnaires this fall and target the compact states’... |
| 18.7 | Build hearing records on House size (cube root) and STV in the 2027-28 Senate |
| 18.8 | Pre-draft in opposition |
| 18.11 | Pre-draft state-level fallbacks for each federal reform, so a Court loss becomes a state campaign rather than a dead end |

## What changed from the old inventory, and why

| Old inventory | Current treatment | Driver |
| --- | --- | --- |
| Legend used [R] for Senate/House rules and had no reconciliation marker | Rules are RU; R1, R2, R3 mark the three reconciliation vehicles | Dec. D5 |
| Enabling layer led with a talking filibuster, a carve-out fallback and full elimination as a sequence | Seven paths (A-G); D2 decided F, with C as the opening offer and the carve-out (G) as the written fallback; reconciliation dial and Parliamentarian transparency added | Dec. D2; Senate Rules Reform: Options |
| “Reform the Byrd rule’s application” | Narrowed to publishing the Parliamentarian’s advice | Dec. D4 (Byrd rule unchanged) |
| Abolish or bind the blue slip | Held: fails the reciprocity test as stated | Design rule 1 |
| House to about 585 on the Wyoming rule | About 692 on the cube-root rule; chamber capital project added; Wyoming stays an option | Instruments #1 |
| STV in districts of three to five | Five where population permits; hold until Section 2 modeling is rerun after Callais | Instruments #2; Callais |
| Seek proactive congressional consent for the compact | Confirm consent is not required; hold consent in reserve; compact status updated to 222 electoral votes | Instruments #6; NPV status |
| (absent) presidential election method | Added as 2.15; STV is held without it; decided Oct 19 that House size, STV and the method are one second-term package | Instruments, Part II and IV; Espen, Oct 19 |
| 23rd Amendment repeal as a separate item | Statutory fix inside the DC admission act; repeal kept as hygiene | Instruments #7 |
| Callais response as a generic item | Restated on the April 29, 2026 holding | Rebalancing; CRS; NCSL |
| Courts: 66 judgeships, a recusal review panel, term limits for all justices | Tiered T1-T3; judgeships phased across terms; recusal decided by the Court with published reasons; term limits prospective and severable; expansion only as a deterrent | Rebalancing; Instruments #4-#5 |
| Executive power: for-cause protections, congressional standing to sue, tariffs as a generic reclaim | Redesigned after Slaughter; grantee cause of action; tariff row restated after Learning Resources; fast-path rule; day-one bridge added | Slaughter; Instruments #8; Learning Resources |
| Stock ban as a standalone item | Floor stated against the July 2026 House bill; packaged with staffing | NOTUS; Instruments #15 |
| Coordination rules tightened generally | Narrowed to outside groups after NRSC v. FEC | NRSC v. FEC (June 30, 2026) |
| Schedule F prohibition codified | Restated against the final OPM rule; executive rescission added to the bridge | OPM final rule (Feb 6, 2026) |
| Delivery section listed policies with its own designs | Pointers to domain files and ledger rows with the decisions applied: health (D6), carbon (D7), Social Security (D8), vehicles (D5) | Dec. D5-D8 |
| “Public option and Medicare at 55” | Go-big bill canonical; Medicare buy-in a separately scored add-on | Dec. D6 |
| Carbon fee and dividend with gasoline inside it | Economy-wide fee excluding gasoline and diesel; about 80/20 | Dec. D7 |
| No Social Security row | Added as a spring 2030 regular-order bill with a flagged scoring problem | Dec. D8; 2026 Trustees |
| Wealth and capital income taxation as the funding base | Mark-to-market, basis repeal, gains parity and a corporate minimum; D3 distribution check run in the incidence model | Dec. D3; Instruments #10; design rule 7 |
| AI dividend with three options and no choice | A per-capita-rebated levy on compute or AI revenue | Instruments #11 |
| Local journalism payroll credit; Section 230 reform | Ownership-conditioned credit; transparency and design mandates instead of liability | Instruments #12-#13 |
| National service option | Cross-regional, cross-class placement written into statute | Instruments #14 |
| Six amendments | Eight plus a convention-procedure statute; all ✖ at any Senate size | Rebalancing; Instruments |
| Groundwork written in 2026 before the Merkley-Daines plan | Updated to Oct 19, 2026; adds the lame-duck push, must-pass vehicles, the Trust Fund extension and state fallbacks | Senate doc; Thriving Economy; Moving America |
| No rows for rights, immigration, public safety, health or transportation | Section 19 and pointers added so the inventory covers the ledger | Ledger; Safe Everywhere |
| Small-dollar match financed by an unsized fines surcharge | Paid from general revenue; channel and FS1 retired (7.1) | INT-5B, Espen, Oct 19 |

## Second versions found, and where each is folded

| Policy | Versions | Folded into |
| --- | --- | --- |
| Permitting reform | Old inventory (categorical exclusions, deadlines); Thriving Economy package; ledger E3 | domain-climate.md: AAJA (stipulated) plus CLI-3 and CLI-6 (9.7) |
| Chevron and deference | Thriving Economy “Restore Chevron” bill and the Stop Corporate Capture and EXPERTS bills; Rebalancing’s express delegations | Courts file (4.8; CRT-8) |
| Anti-impoundment | Inventory (congressional standing); Instruments (grantee cause of action); Thriving Economy chapter 9 provisions | Executive-power file (5.3) |
| Election-worker protection | Inventory 3.6; Safe Everywhere plank 8 | SAF-8 (DEM-14 points to it) |
| Domestic military deployments | Inventory 5.10; Safe Everywhere plank 2 and its revenue package | One statute in EXE, referenced from SAF-2; the savings are not counted in PS1 |
| Non-compete ban | Inventory 11.2; go-big health bill Title V | COM-4; HLT-5 references it |
| Carbon pricing | Old inventory fee and dividend; Moving America fuel taxes; Thriving Economy border adjustment | Settled by Dec. D7 (10.3) |
| House size | Inventory and ledger D10 (about 585); Instruments (about 692) | Democracy file; 692 adopted, 585 kept as an option (DEM-3B) |
| Defense envelope | Ledger A2 (+3.2%); Dec. D9 | Dec. D9 wins (16.8) |
| Social Security | Bill Book expansion (ledger F5); Dec. D8 baseline | Dec. D8 wins (10.14) |
| Right to vote | Listed in sections 3 and 17 of the old inventory | Once, at 17.5 |
| Rows IDs | Ledger democracy rows D0-D13 share names with Decisions D1-D9 | The ledger keys every row by its domain-file ID (DEM-1 ...); the legacy IDs sit only in its crosswalk column |
| Shareholder approval for political spending | Inventory 7.5 (Unchanged); a corporate-governance route around Citizens United | INT-15: federal route through the Securities Exchange Act, state route as fallback (INT-17) |

## Conflicts with Decisions, and how each was handled

| Decision | Conflict | Handling |
| --- | --- | --- |
| D2 | Old enabling layer recommended a path | Modeled as paths A-G; D2 decided F (Decision Brief 1) |
| D4 | Old “reform the Byrd rule’s application” | Narrowed to publishing advice (1.10). Needs your confirmation |
| D3 | Old wealth-tax funding base; Safe Everywhere’s alcohol-tax change; fuel steps, the carbon fee and a leave contribution now allowed | Revenue base replaced (11.1); the incidence model runs the D3 check on the whole agenda (scenario Q: every quintile below the top ahead) |
| D6 | Old ledger H2 included Medicare at 60; old row said Medicare at 55 | Buy-in is a scored add-on (10.6, 10.8); the ledger's HLT-2 excludes it |
| D7 | Old ledger E2 included gasoline ($2.15T) | D7 exempts gasoline and diesel: REV-C1 about $1.35T on the durability path plus REV-C2 about $0.20T (10.3) |
| D8 | The old 3.8% gap was the 2025 figure | D8 uses the 2026 Trustees' 4.42%; the baseline closes about 64% on SSA's 2026 scores and does not reach balance on its own (10.14) |
| D9 | Ledger A1 and A2; the agency list omitted agencies the domain files depend on | Replaced by 9.1 (CAP-7S and CAP-7) and 16.8 (NSC-1A); the governing doc carries the extended agency list |
| D5 | Housing sat in ②; reconciliation narrowing is a D2 dial | Housing moved to ① in R2 (10.13); narrowing placed after R3 (1.9) |
| D1 | Old plan assumed a full-reform upside case | Every row is tagged at 51 |

## What the full list reveals

- **The proportions are still statute-heavy.** Regular-order statutes are 58% of rows, state level 6%, amendments 4%, executive action or norms 3%, treaties 2%. The old inventory said about 60% statutory, 20% state, 12% amendments and under 5% executive or international (its own estimate). The executive column is bigger now (the bridge, norms and the post-Slaughter redesigns), but Congress is still the default instrument.
- **Slaughter changes the design space more than any other 2026 event.** Five rows (5.5, 5.13, 5.16, 7.3, 12.6) depend on bodies that can no longer lean on removal protection; they are redesigned with structure or placement.
- **Two 2026 decisions weaken old rows:** Callais narrows what Section 2 guarantees (3.2, 2.3), and NRSC removes party-coordination limits (7.4).
- **Capacity still gates the list.** Sections 8 and 9 plus Dec. D9’s agency rebuild (the CAP-7S surge and the sustained CAP-7) are the precondition for most of Section 10; domain-capacity.md allocates it by agency as an unsourced first split, pending a bottom-up review.
- **The first-Congress calendar is still over budget.** Under path F the ledger counts 172 floor days against 163; this file supplies the ✔ list, and the overrun closes through merges or more floor days.
- **Still thin:** federalism (the conditional-funding lever is NFIB-exposed at 2.6), the opposition’s counter-moves (partly addressed by 2.5, 4.16 and 18.11), cost and financing of Sections 7, 8, 12 and 15 (unscored), and failure modes when the Court strikes several items at once.

## Held or dropped

- Rotation or lottery panels for the Court (weak precedent, likely hostile: Rebalancing #10)
- A statutory supermajority vote to invalidate statutes (likely unconstitutional; amendment only, 17.8)
- Section 230 liability reform limited to amplification (Moody v. NetChoice; replaced by 12.2)
- A federal wealth tax (replaced by 11.1)
- Seeking proactive congressional consent for the compact (replaced by 2.13)
- Any party-coordination limit (NRSC)

## Updates to make elsewhere

**Domain files**

1. domain-health.md: a real score for HLT-6's Medicare Advantage capture and its 42% Part A split (revenue audit finding 5).
2. domain-family.md: a fresh CTC score against current law ($2,200 credit); confirm the FAM-2 phasing choice, the only baseline there not taken from a Decision.
3. domain-social-security.md: choose D8's closer (SS-5 recommended) and test SS-10's 67-vote premise.
4. domain-capacity.md: refine CAP-7S and CAP-7 through the bottom-up agency review (open item 2 there).
5. domain-public-safety.md: the title-by-title Byrd check for SAF-10A.

**Moving America**

6. MOV-30 needs rescoring on the FY2031-40 window if carried on the FY2031 resolution.

**Sources**

7. Rebalancing the Three Branches: its caveat that NRSC v. FEC is unconfirmed is out of date (decided June 30, 2026, 6-3). It is a source record, so the correction lives here and in section 7.

## Sources used for world-state claims

- National Popular Vote, state status (April 2026) and NPR/WLRN, Apr 14, 2026: 19 jurisdictions, 222 electoral votes. Daily Signal, Oct 3, 2026: still 48 short.
- NOTUS and Gray DC (Sept 10, 2026), NBC Palm Springs (July 22, 2026): House stock-trading vote 232-198 and the Senate committee action.
- Ballotpedia (May 11, 2026), NCSL tracker, Voting Rights Lab, MultiState: mid-decade redistricting and Callais effects.
- OPM final rule, Federal Register Feb 6, 2026; CRS LSB11412 (Mar 26, 2026): Schedule Policy/Career.
- Boston College CRR (June 16, 2026), CRS IF13256, CRFB, Academy of Actuaries: 2026 Trustees 4.42% deficit and the 2034 combined-funds depletion.
- Wiley, Skadden, Covington, Mayer Brown (June-July 2026): NRSC v. FEC, decided June 30, 2026, 6-3.
- Project files: Governing Decisions (live doc rev 66), Senate Rules Reform: Options (rev 34), Rebalancing the Three Branches, Thriving Economy map, Instruments and Consequences, Radical Means, the master ledger, the go-big and revenue files, Safe Everywhere.
