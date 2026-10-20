# Moving Project 2050 work between chat and Code: start here

## The idea
One set of files (the Project) is the shared home. Chat is where decisions get made. Code is where mechanical jobs get run. Code reads a rulebook (code-handoff-claude-md.md, filed in the project at index/tools/) that keeps it from touching policy files, and it leaves a log (index/tools/code-log.md) so chat can see what happened.

| Stays in chat | Goes to Code |
| --- | --- |
| Anything touching a Decision (D1-D9), option design, domain-file conversion | Linting the project against the design rules |
| Choosing between two numbers | Reconciling script tables against domain files |
| Reviewing what Code found | Regenerating the ledger in one command |
| | The D3 incidence model, later |

## Step 1: two-minute test (decides everything else)
Start a Claude Code session attached to Project 2050 (if Code offers a project choice; I can't see its menus from chat). Paste Prompt A below. If Code can run project_info and shows the project's file list, you're on the easy route and need nothing else.

**Prompt A (paste into Code):**
> This is the Project 2050 project. Run project_info, then read index/tools/code-handoff-claude-md.md with project_read and follow it. Do Job 0 only, then stop and report.

## If Code can't see the project
Tell me, and I'll switch to the folder route. You make a folder (say Documents/Project 2050) and add it to this chat from the "+" menu, "Add folder". Then I copy in the roughly fifteen files Code needs and put the rulebook in as CLAUDE.md, so Code finds it automatically when you open that folder. That copy is a big one-time job in chat, which is why it's the fallback.

## Running it
1. Job 0 first. It only reproduces the current numbers, so it is cheap and proves the setup works.
2. After each job Code stops and reports in about ten lines. Say "go" for the next one. Job 4 (the incidence model) is where most of the spend will be, so Code is told to ask first.
3. Use a Sonnet-class model for Jobs 0-3 (mostly mechanical). Consider a stronger one for Job 4. Check your usage meter between jobs; I can't see it or predict cost.

## Coming back to chat
Say "Code finished [job]". I'll read index/tools/code-log.md and the reports it filed, then bring back anything that touches a decision as options. If you edit a domain file or the live Governing doc in chat while Code is running, tell Code to re-pull before its next job. Its rulebook already makes it re-check a file before pushing.

## Two housekeeping items I found
- Your saved project instructions are slightly behind the live doc: they leave out D4's two readings and show D8 as 70-77% (live doc: 65-72% after the haircut). The code block in the live doc is current; re-paste from there.
- D9's extended agency list exists only in the project copy of the governing doc, not the live one. Say which should stand.
