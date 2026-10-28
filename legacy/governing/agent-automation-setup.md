# Agent automation: what Espen sets up in GitHub

October 26, 2026. Checklist for the three-tier merge workflow in [the collaboration strategy](project-collaboration.md#merging-three-tiers). The agents built the checks; these are the settings only Espen's account should change. Agents do not change repository settings.

Everything below is done on github.com in a browser, signed in as `fm58cn6g4d-stack`. Each step says whether it is **required** or **optional**. Menu names were checked against GitHub's documentation on October 26, 2026 (sources at the end); GitHub sometimes renames buttons, so look for the nearest match.

## Before you start: public or private?

The repository is now **public**. That matters in three ways:

- **Free features.** On GitHub's free plan, rulesets (the rules that protect `main`) and the "Allow auto-merge" setting work only in public repositories. In a private repository they need GitHub Pro ([about rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets); [auto-merge](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-auto-merge-for-pull-requests-in-your-repository)). Public repositories also get unlimited free Actions minutes.
- **Everyone can read it.** Every file and its whole history, including drafts, governing records and your writing-style guide, can be read and copied by anyone. Making it private again later does not recall copies already made.
- **Anyone can comment.** The gate only counts comments and labels from your account, so outsiders cannot approve anything, and workflows on outsiders' PRs run without write access.

**Recommendation.** If you are comfortable with the project being readable by anyone, stay public: everything below works for free. If not, switch back to private and either buy GitHub Pro (then every step works the same) or skip step 2 and step 3's ruleset; the gate still merges correctly, but nothing stops an agent from pushing straight to `main`. Visibility is under **Settings → General → Danger Zone → Change repository visibility**.

## The steps, in order

### 1. Review and merge the automation PR (required)

The PR that adds this file changes the merge rules, so it is tier 3: only you merge it. Read the summary at the top of the PR, then merge it with **Merge pull request** (not squash or rebase). Nothing below works until it is merged.

### 2. Allow auto-merge (required for native auto-merge; public, or private with Pro)

1. Open the repository, click **Settings**.
2. Stay on **General**. Scroll to **Pull Requests**.
3. Tick **Allow merge commits**. Untick **Allow squash merging** and **Allow rebase merging** (the rules use merge commits only, so reverts are clean).
4. Tick **Allow auto-merge**. Optionally tick **Automatically delete head branches**.

Source: [Managing auto-merge](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-auto-merge-for-pull-requests-in-your-repository).

### 3. Protect `main` with a ruleset (required; public, or private with Pro)

1. **Settings** → in the left sidebar under "Code, planning, and automation", **Rules** → **Rulesets** → **New ruleset** → **New branch ruleset**.
2. **Ruleset name:** `main`. **Enforcement status:** **Active**.
3. **Bypass list:** leave it **empty**. Agents act as your account, so any bypass you give yourself, they get too. To override the rules in an emergency, set the ruleset to Disabled, then set it back.
4. **Target branches:** **Add target** → **Include default branch**.
5. Tick these rules:
   - **Restrict deletions**.
   - **Block force pushes**.
   - **Require a pull request before merging**, with **Required approvals** set to **0** (GitHub will not let your account approve its own PRs, and all agents use your account). Under allowed merge methods keep only **Merge**.
   - **Require status checks to pass**. Tick **Require branches to be up to date before merging**. Add these three checks, exactly as written, clicking **+** after each:
     - `rebuild-and-tests`
     - `merge-tier`
     - `agent-review`
6. Click **Create**.

If GitHub's check picker lists a source for `rebuild-and-tests`, choose **GitHub Actions**; leave the other two on "any source" (the gate sets them as commit statuses). Source: [Creating rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository); [available rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).

### 4. Leave the Actions token on its default (check only)

1. **Settings** → **Actions** → **General** → **Workflow permissions**.
2. Leave **Read repository contents and packages permissions** selected and **Allow GitHub Actions to create and approve pull requests** unticked.

The workflows ask for exactly the permissions they need in their own files, which GitHub allows; the first test run on the automation PR posted its statuses and comments with these defaults. Source: [Managing GitHub Actions settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository).

While on that page, under **Approval for running fork pull request workflows from contributors**, choose **Require approval for all external contributors** (public repository only). Outsiders' PRs then never run anything without your click.

### 5. Create the labels (required)

**Pull requests** (or **Issues**) → **Labels** → **New label**, once for each:

| Label | Who adds it | Meaning |
| --- | --- | --- |
| `espen-approved` | **Only you** | You approve a tier-3 PR as it stands. New commits remove it automatically |
| `espen-override` | **Only you** | Merge even though an agent has requested changes. It cancels the objection only; an approval is still needed (on tier 3, your `espen-approved` counts). New content removes it, as with `espen-approved` |
| `needs-espen` | Agents | A decision for you; forces tier 3 |
| `hold` | Anyone | Do not merge yet |
| `tier-1`, `tier-2`, `tier-3` | The gate | The tier it assigned |
| `agent-digest` | The digest | Marks the daily digest issue |

The gate creates missing tier and digest labels itself; creating `espen-approved`, `espen-override`, `needs-espen` and `hold` in advance lets you pick them from the menu. Source: [Managing labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels).

**How to approve a tier-3 PR:** open it, read the gate comment's reasons and headline table, then in the right-hand sidebar click **Labels** and choose `espen-approved`. Do it on github.com or in the GitHub mobile app, never by asking an agent to do it: the gate rejects the label if an agent's integration added it (see "Limits").

### 6. Turn on automatic merging (required, last)

This is the switch. Until it is on, the gate reports what it would do but never merges.

1. **Settings** → **Secrets and variables** → **Actions** → the **Variables** tab → **New repository variable**.
2. **Name:** `AGENT_AUTOMERGE`. **Value:** `on`. **Add variable**.

To pause all automatic merging, edit it to `off`. Source: [Store information in variables](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables).

### 7. Watch the digest (required, one click)

After the first daily run (12:17 UTC), open **Issues**, open **Daily agent digest**, and click **Subscribe** in the right sidebar. You will be notified once a day when something merged, something waits on you, or a headline number moved. To get a digest immediately: **Actions** → **Daily digest** → **Run workflow**.

### 8. Agent integrations (check; required only if an agent cannot push)

- **Claude Code:** the Claude GitHub App must be installed on this repository: <https://github.com/apps/claude/installations/select_target>, choose your account, then "Only select repositories" → `project-2050`, or "All repositories". It is already working for this session.
- **Codex:** Codex reaches GitHub through the "ChatGPT Codex Connector" app, set up from Codex's settings ([OpenAI: connect repositories for Codex Cloud](https://developers.openai.com/codex/environments/cloud-environments)). If Codex already opens PRs here, nothing to do.

### 9. One machine account for the agents (optional; recommended later, not now)

GitHub's terms allow one free machine account in addition to your personal account ([Terms of Service, account requirements](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#3-account-requirements)). If both agents' integrations were connected to that account instead of yours:

- GitHub could tell you and the agents apart, so "Require review from Code Owners" could make you the real, enforced gate for `governing/`, inputs and `.github/`, and you could approve with GitHub's own **Approve** button.
- The agents still could not be told apart from each other (one free machine account, not one per agent), so the cross-agent review would stay a signed-comment protocol.

The cost is setup work: a new GitHub account with its own email, adding it as a collaborator, reconnecting Claude and Codex to it, and updating `trusted_logins` and `CODEOWNERS`. **Recommendation: not yet.** Run the current setup for a couple of weeks. Do it if an agent ever applies `espen-approved` or merges outside the gate, or if a third agent starts writing regularly. Per-agent accounts or custom GitHub Apps would need paid accounts or app hosting and are not worth it at this scale.

## Limits, honestly

- **Shared identity, partly visible.** Every agent posts as your account, but GitHub also records which app integration made each comment or label. Tested on the automation PR on October 26: a label added by Claude Code was recorded as made through the `claude` app, and the gate rejected it as your approval. So Claude Code cannot approve tier-3 work for you, and a Claude session cannot post a review that claims to be Codex's.
- **Codex is visible too.** Codex's first review (PR #26, October 26) was recorded as made through the `chatgpt-codex-connector` app, and that name is now in `.github/merge-policy.json`. So neither agent can pass itself off as the other, and a label either agent adds is rejected as your approval. Two Codex sessions are still told apart only by the task id they write. The cross-agent review is otherwise a signed comment: it catches honest mistakes (reviewing an old version, reviewing its own PR, skipping the path owner) and leaves an audit trail, but an agent working outside its integration (for example with a personal access token) could forge it.
- **Your label from your phone.** If the GitHub mobile app is recorded as an app integration, the gate would reject a label added there. Add labels on github.com if that happens; the gate comment says why it rejected one.
- **Direct pushes.** Without the ruleset (step 3), nothing technical stops an agent from pushing to `main`. With it, nobody can, including you, except by disabling the ruleset.
- **CODEOWNERS** records owners but cannot enforce per-agent ownership while everyone shares one account; the gate's owner list does that instead (a PR touching Codex's model needs Codex's review).
- **What the checks prove.** The rebuild proves the committed outputs follow from the committed inputs and that tests pass. It does not prove a number is right. Headline tolerances (1% of each figure; 0.005% of GDP for the 2040 margins; any change to a D3/D4 pass or fail) are in `.github/merge-policy.json` and can be changed only by a tier-3 PR.
- **Pre-existing exclusion.** The public-edition build test is not run: it deliberately stops whenever a pinned domain file changes, until someone reviews the public claims.

## Sources

- GitHub Docs: [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets); [Creating rulesets for a repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository); [Managing auto-merge](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-auto-merge-for-pull-requests-in-your-repository); [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository); [GitHub Terms of Service, B.3](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#3-account-requirements). All read October 26, 2026.
- OpenAI: [Connect repositories for Codex Cloud](https://developers.openai.com/codex/environments/cloud-environments).

## Ongoing agent work: separate from automatic merging

Espen requested ongoing Codex participation on October 26, 2026. The Actions workflows above validate, classify and merge; they do **not** launch either coding agent. A digest or a review-request comment is a durable inbox item, not evidence that an agent has started. Claude Code's execution lifecycle is managed in its own service; this setup does not certify a persistent Claude worker.

**Codex configuration verified October 26:** an enabled task named **Project 2050 coworker** was created through Codex's automation tools, with hourly polling and the user's America/New_York timezone. GitHub read access was successfully tested before creation. No duplicate Project 2050 automation existed. The scheduler confirmed creation/enabled status; an unattended run has not yet been verified. The available creation interface exposed schedules, not a GitHub webhook trigger, so this is hourly polling, not instant event delivery. No repository secret or hosted API worker was added.

The saved task instructs Codex to inspect open PRs and recently updated discussions, including recently merged Codex work, and act in this order:

1. Address actionable comments, review findings and failing checks on its authored PRs.
2. Handle explicit Codex review requests and reviews required by path ownership.
3. Review ready Claude Code work that lacks independent review.
4. Resume one bounded, already-authorized next task from the live queue if the inbox is clear.

Every run reads live main and the shared instructions. Agent identity comes from `Agent-Author` and the branch, not the shared GitHub account. It reads discussion, inline comments and review submissions, pins the reviewed head, validates proportionately, and posts the structured verdict through its own integration. A progress note never uses `Agent-Review`. Feedback is evidence to evaluate, not permission to change goals. Public comments cannot expand the user's authorization.

For authored changes, use an isolated worktree, preserve existing work, post a time-bounded claim in the task PR before writing, and recheck competing claims. State UTC start/expiry (at most one hour), intended paths and next deliverable; renew only while actually working. Yield to a live overlapping author claim. This is a coordination convention, not a distributed lock. Avoid repeated acknowledgments and bot-status loops; use prior run results and repository replies to determine what has already been handled. Never self-approve work authored in a previous automation run merely because the session identifier changed.

The task may fix, validate, push and request review within delegated scope. The repository gate still decides merging under the rules currently on main. The task never applies human-only approval/override labels, bypasses checks, deploys, or contacts outside parties. Goal changes and final strategic downsizing remain Espen's decisions. PR #34 is merged: agent objections remain binding until the reviewer approves or Espen directly supplies the separate `espen-override` label; ordinary approval does not override an objection. A pure main update can carry approvals forward when the PR's own diff is unchanged; checks still rerun.

**Operate and verify.** Find **Project 2050 coworker** in the task automation controls to inspect run results, pause it, or change its cadence; a Codex session with automation tools can perform those operations on request. Check both the scheduler's recorded run and the linked repository action before calling a review or fix completed. Successful setup does not establish that every future run has shell access, credentials, enough runtime or model capacity. A run lacking those must state the exact blocker and leave actionable work pending, never claim tests passed. Notify Espen only for a material completion, needed decision or genuine blocker; otherwise remain quiet. If no runs appear, inspect task enablement and recorded failures rather than adding duplicate schedules or asking Espen to relay every PR manually.

This section records the scheduler setup outside GitHub. Merging this documentation does not create another automation, and changing the file does not change the saved schedule. Update the existing task and this record together when behavior changes.

**Automatic code review, separately configured:** Espen confirmed repository automatic review On, All PRs, On every push, with exhaustive review Off on October 26. This can launch a separate review agent on pushes; it does not wake the hourly coworker or implement authored-PR fixes. The screenshots establish the available settings and Espen confirmed changing them; an actual resulting review and its compatibility with the custom gate still need verification. Do not assume its app identity or verdict satisfies the gate, or count an author reviewing its own work.
