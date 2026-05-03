# GitHub PR Workflow Quick Reference

## Your Workflow Sequence (with clarification)

```
1. Draft pull request (created locally or via web)
   ↓
2. Resolve conflict in web editor
   └─ Click "Accept incoming change" or "current change" (blue link)
   └─ Commit merge
   ↓
3. Draft pull request ready for review
   └─ Click "Ready for review" button (web UI)
   └─ Then "Merge pull request"
   └─ Confirm merge
   └─ Delete branch
```

---

## How to See All Commit Messages

### 1. **In GitHub Web UI**

Go to **Commits** tab on the PR:
```
Your PR page
  → "Commits" tab (next to "Files changed")
  → Scroll through all commit messages
```

Or click individual commits to see full diffs.

### 2. **In Terminal (CLI)**

After cloning and checking out the branch:

```bash
# View commits on this branch only (not in main)
git log main..HEAD --oneline

# View all commits with full messages
git log main..HEAD

# View commits with stats (files changed per commit)
git log main..HEAD --stat

# View in one-line format (compact)
git log main..HEAD --oneline

# View commits authored by you
git log main..HEAD --author="Your Name" --oneline
```

### 3. **Comparing Branches**

```bash
# See what commits are in feature-branch but not in main
git log main..feature-branch --oneline

# See commits in reverse (newest first, which is default)
git log main..feature-branch --reverse --oneline

# Count total commits in a PR
git log main..feature-branch --oneline | wc -l
```

### 4. **GitHub CLI** (gh)

```bash
# View PR commits from CLI
gh pr view PR_NUMBER --json commits

# Get all commit messages in a PR
gh pr view PR_NUMBER --json commits --jq '.commits[].message'

# View full diff with commits
gh pr diff PR_NUMBER
```

---

## Best Practices for Commit Messages

When pushing commits that will go through Symphony (agent-generated) or manual PR:

```
# Good commit message format (follows convention)
feature: add user authentication
fix: resolve infinite loop in payment retry
chore: bump dependencies
test: add coverage for edge cases in auth module
docs: update API documentation

# Each commit should be:
- Atomic (one logical change per commit)
- Testable (tests should pass after this commit)
- Readable (first line ≤ 50 chars, body ≤ 72 chars)
```

### View by Type:

```bash
# See all feature commits
git log main..HEAD --grep="^feature:" --oneline

# See all fixes
git log main..HEAD --grep="^fix:" --oneline

# See commits by date range
git log main..HEAD --since="2 weeks ago" --until="1 week ago" --oneline
```

---

## Workflow Integration with Symphony

Once you add Symphony, agent PRs will auto-generate commits. To review them:

```bash
# 1. Fetch latest (agent may have pushed while you slept)
git fetch origin

# 2. Checkout agent-created branch
git checkout symphony/SYM-42-implement-user-auth

# 3. See all commits agent made
git log main..HEAD --oneline

# 4. Review full diffs per commit
git log main..HEAD --stat

# 5. If good, approve in GitHub UI; if not, add comment
# Symphony agent will see feedback and retry
```

---

## Symphony-Specific: Handling Multi-Commit PRs

Since agents run continuously, they may produce multiple commits before the PR is ready:

```bash
# Scenario: Agent has made 5 commits, you want to squash to 1
# (Do this BEFORE approving, or agent will retry)

# View the commits
git log main..HEAD --oneline

# Option A: Squash commits via rebase (interactive)
git rebase -i main~5

# Option B: Let GitHub handle it
# In PR UI: "Squash and merge" ← automatically squashes all commits

# Symphony respects your approval policy:
# If you set "human_review" in WORKFLOW.md, agent STOPS at PR
# You decide: merge-as-is, squash, or request changes
```

---

## Cheat Sheet: Commit Commands

| Command | What it does |
|---------|-------------|
| `git log HEAD --oneline` | Your current branch commits |
| `git log main..HEAD --oneline` | Commits on branch not in main |
| `git log --oneline -n 10` | Last 10 commits |
| `git log --author="Name"` | Commits by specific person |
| `git log --since="2 weeks ago"` | Recent commits |
| `git log --grep="fix:"` | Search commit messages |
| `git show <commit-hash>` | View specific commit (message + diff) |
| `gh pr view --json commits` | PR commits via CLI |
| `gh pr diff` | Full PR diff with commit boundaries |

---

## Example: Full PR Review Flow

```bash
# 1. PR created by agent, you get notification

# 2. Fetch and check it out locally
git fetch origin
git checkout origin/symphony/SYM-42

# 3. See what agent did
git log main..HEAD --oneline
# Output:
# a1b2c3d test: add auth tests
# d4e5f6a feat: implement JWT verification
# g7h8i9j refactor: extract token validation

# 4. See full code changes per commit
git log main..HEAD --stat
# Shows files changed per commit

# 5. Run tests locally to verify
npm test

# 6. Approve in GitHub
# Go to PR → "Approve" button (or request changes)

# 7. Merge (you can also squash if needed)
# GitHub UI: "Squash and merge" button
```

---

## Sync to Your SaaS Workflow

In your spec-driven MVP workflow:

1. **Linear issue** = work unit
2. **GitHub branch** = agent workspace (Symphony creates per-issue)
3. **Commits** = agent's proof of work
4. **PR review** = your human gate before merge

Each commit should map to a logical test-covered change. Review before merging to ensure quality (especially early, while tuning the prompt).

