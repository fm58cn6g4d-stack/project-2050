# Prompt for the ATRA chat — write your state to the project before the merge

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/atra-state-dump-prompt.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Paste this into the ATRA chat.

---

We're going to merge ARCA and ATRA into a single Surface Transportation Reauthorization Act of 2031 document, in a separate session. That session can read the project and both architecture docs, but it **cannot read this conversation.** So anything we settled here in discussion and never wrote down is about to be lost.

Your job in this turn is to get it written down. Write to the project at `sources/transportation-atra-merge-contribution-oct12.md`, and use these headings exactly so it lines up with the ARCA side (`sources/transportation-arca-status-oct12.md`, which is already written in this shape).

Before you start, read `sources/transportation-arca-status-oct12.md` — the ARCA doc was brought into line with the October 12 handoff and is now at rev 309, so some of what you remember about it is stale. Flag anything in your contribution that contradicts it.

## 1. The highway division — this is the priority

Nothing about the highway scoping exists in the project yet, and it is the single biggest hole in the merged bill: roughly $430.35B of an $908.8B package with no drafted title. Write down everything you have:

- Whether it is a drafted division, an incorporation of H.R. 8870's title by reference, or something in between — and which you recommend
- Its division letter, and what that makes ARCA and ATRA
- Authorization levels by year, and how they relate to H.R. 8870's $72.9B-77.6B FY2027-31
- Where NHTSA and FMCSA sit (the model folds their ~$2.0-2.5B/yr into the Highway Account's need)
- Any drafted statutory text, verbatim
- Which programs you treated as renewal and which as expansion for division A sections 107 and 108
- What you have *not* scoped

## 2. Division A

Sections 101, 108 and 109 were drafted in the ATRA doc. For each of 102, 103, 104, 106, 107, 110 and 111: drafted, partly drafted, or not started — and paste any text that exists. Section 111 (per-mile administration) matters most; if you have a position on Treasury collection, the bar on location data, odometer-only reads, State collection agreements or the 10 percent cost allowance, write it down even if it is not in statutory form.

## 3. Decisions made in conversation that are not in `sources/transportation-transit-package-status-oct12.md`

That doc was last written 2026-10-12. Anything decided after it, or decided in discussion and never filed, goes here — with the reasoning, not just the conclusion. Include anything where you changed your mind.

## 4. Current numbers

- ATRA's canonical authorization table as it stands now, by section and year, with the five-year total
- The reconciliation lines
- The 250-Plus transit baseline
- Whether `index/tools/transportation/transit_fiscal_model.py` in the project is current, or has been edited since

## 5. Your position on the two unresolved variables

- **The transit/rail split and the incremental shares.** The bill text says 35 / 50 / 15; the model's equal-renewal-coverage solution is 35 / 54 / 12. Where do you come out, and what does the highway scoping do to it?
- **49 U.S.C. 5307 operating eligibility.** Scenario B or C, and why. This moves the combined FY2032-36 draw from 0.174% to 0.190% and the split by about four points, so it has to be settled before the merge rather than during it.

## 6. Open items, and known contradictions with ARCA

List yours. Then list every place you know ATRA and ARCA still disagree — the joint terminals (sec. 310's $20.20B against sec. 606's $6.0B over the same five nodes) are the obvious one, but name any other double counts, conflicting figures or incompatible definitions.

## 7. Which sections should survive the merge

Both documents independently carry a fiscal-envelope section, a Byrd-rule analysis, a 250-Plus baseline section, a political-path section and a fallback-tier section. For each, say which document's version is the better base and what has to be folded in from the other. The merged doc gets one of each.

---

Write it, then tell me in two or three lines what the merge session most needs to know that it would not guess from the documents. Don't rebuild the ATRA doc — this is a handoff file, not a rewrite.
