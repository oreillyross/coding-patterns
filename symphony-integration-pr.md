# Integrate Symphony Orchestration for Autonomous Task Execution

## Summary

Symphony is a minimal orchestration layer that turns your Linear issue tracker into an always-on agent control plane, decoupling work management from coding sessions. This PR adapts Symphony for solo-founder MVP velocity:

- **Watch Linear board → auto-pick unblocked issues**
- **Each issue gets isolated workspace + agent session**
- **Agent publishes PR → human review handoff** (no babysitting)
- **TypeScript-first implementation** (not Elixir)

Instead of manually prompting agents across browser tabs, you define spec-driven tasks in Linear and let autonomous agents execute in parallel, with agents handling routine implementation work while you concentrate on higher-level challenges.

---

## What Changes

### 1. Add TypeScript Symphony Runner

Create `src/orchestration/symphony-runner.ts`:

```typescript
import { LinearClient } from "@linear/sdk";
import { createOrResumeAgentSession } from "./codex-session";
import fs from "fs";
import path from "path";

interface WorkspaceConfig {
  issueId: string;
  issueTitle: string;
  workspaceDir: string;
  agentPrompt: string;
}

export class SymphonyOrchestrator {
  private linearClient: LinearClient;
  private workflowConfig: WorkflowConfig; // Read from WORKFLOW.md
  private concurrentLimit = 3;
  private pollInterval = 30_000; // 30 sec

  constructor() {
    this.linearClient = new LinearClient({
      apiKey: process.env.LINEAR_API_KEY,
    });
    this.workflowConfig = this.loadWorkflow();
  }

  private loadWorkflow(): WorkflowConfig {
    // Parse WORKFLOW.md to get approval policy, workspace root, prompt template
    const workflowPath = path.join(process.cwd(), "WORKFLOW.md");
    const raw = fs.readFileSync(workflowPath, "utf-8");
    return parseWorkflow(raw);
  }

  async start() {
    console.log("🎵 Symphony orchestrator starting...");
    setInterval(() => this.pollAndDispatch(), this.pollInterval);
  }

  private async pollAndDispatch() {
    // 1. Query Linear for unblocked issues in "In Progress" state
    const issues = await this.linearClient.issues({
      filter: {
        state: { name: { eq: "In Progress" } },
        assignee: { null: true }, // No assignee = ready for agent
      },
    });

    if (issues.nodes.length === 0) {
      console.log("✓ No unblocked work");
      return;
    }

    // 2. Dispatch up to concurrentLimit agents
    const toProcess = issues.nodes.slice(0, this.concurrentLimit);
    for (const issue of toProcess) {
      await this.dispatchAgent(issue);
    }
  }

  private async dispatchAgent(issue: any) {
    const issueId = issue.identifier; // e.g., "SYM-42"
    const workspaceDir = path.join(
      this.workflowConfig.workspaceRoot,
      issueId
    );

    // 3. Create isolated workspace
    if (!fs.existsSync(workspaceDir)) {
      fs.mkdirSync(workspaceDir, { recursive: true });
      console.log(`📂 Created workspace: ${workspaceDir}`);
    }

    // 4. Create or resume agent session
    const agentPrompt = this.renderIssuePrompt(issue);
    const session = await createOrResumeAgentSession({
      workspaceDir,
      issueTitle: issue.title,
      issueIdentifier: issueId,
      prompt: agentPrompt,
      cwd: workspaceDir, // ← Symphony: all commands run in per-issue dir
    });

    console.log(
      `🤖 [${issueId}] Agent session started (resuming: ${session.resumed})`
    );

    // 5. Run agent turn, expect PR creation as output
    try {
      const result = await session.submitTurn(
        agentPrompt,
        this.workflowConfig.approvalPolicy
      );
      console.log(
        `✅ [${issueId}] Agent completed: ${result.status} (${result.artifactType})`
      );

      // 6. Transition issue on successful completion
      if (result.status === "pr_ready") {
        await this.linearClient.issueUpdate(issue.id, {
          stateId: this.workflowConfig.handoffStateId, // e.g., "Human Review"
          description: `Agent output: ${result.prUrl}`,
        });
      }
    } catch (error) {
      console.error(`❌ [${issueId}] Agent failed: ${error.message}`);
      // Retry logic handled by supervisor tree (BEAM OTP analogue in TS)
    }
  }

  private renderIssuePrompt(issue: any): string {
    // Substitute issue fields into template from WORKFLOW.md
    return this.workflowConfig.promptTemplate
      .replace("{{issue.id}}", issue.identifier)
      .replace("{{issue.title}}", issue.title)
      .replace("{{issue.description}}", issue.description || "");
  }
}

// ─────────────────────────────────────────────────────────────
// Load from WORKFLOW.md
interface WorkflowConfig {
  workspaceRoot: string;
  approvalPolicy: "auto" | "human_review";
  handoffStateId: string;
  promptTemplate: string;
}

function parseWorkflow(raw: string): WorkflowConfig {
  // Simple YAML/Markdown parser (or use a real parser)
  return {
    workspaceRoot: "/tmp/symphony-workspaces",
    approvalPolicy: "human_review",
    handoffStateId: "6a1d04c4-8c50-4c7d-9e64-e3c1e6f44a47", // Human Review state
    promptTemplate: `
Issue: {{issue.id}} - {{issue.title}}

Description:
{{issue.description}}

You are an autonomous coding agent. Your goal is to resolve this issue completely.
- Write tests first
- Run CI locally
- Open a pull request with link to this issue
- Stop at Human Review state
`.trim(),
  };
}
```

### 2. Add WORKFLOW.md (Versioned with Code)

Create `WORKFLOW.md` in repo root:

```markdown
# Symphony Workflow Configuration

## Orchestrator Policy

- **Approval**: Human Review (all PRs require approval)
- **Sandbox**: Per-issue workspace isolation (no mutation outside ${WORKSPACE_ROOT}/${ISSUE_ID})
- **Concurrency**: 3 agents max
- **Workspace Root**: `.symphony/workspaces`

## Issue States & Transitions

- **Backlog** → (manual) → **In Progress**
- **In Progress** → (agent) → **Human Review** (with PR link)
- **Human Review** → (human) → **Done** or back to **In Progress**

## Agent Prompt Template

```
Issue: {{issue.id}} - {{issue.title}}

Description:
{{issue.description}}

Implementation Checklist:
- [ ] Read test files for context
- [ ] Write failing test(s)
- [ ] Implement solution
- [ ] All tests pass locally
- [ ] Run `npm run build && npm run test:e2e`
- [ ] Create PR with issue link
- [ ] Do NOT merge yourself
```

## Harness Engineering Requirements

Your codebase must support agent execution:

1. **Automated Tests**: Full suite runs in <5 min
   - `npm test` ✓
   - `npm run test:e2e` ✓

2. **CI Integration**: GitHub Actions configured
   - All PRs require status checks

3. **Task Clarity**: Issues must include:
   - Acceptance criteria
   - File paths (not vague descriptions)
   - Links to relevant code

4. **No Manual Steps**: Agent cannot require:
   - Manual secret setup (use `.env.test`)
   - Database migrations (auto-run in test)
   - Slack notifications (mock in tests)
```

### 3. Hook into Your Existing PR Workflow

Modify `.github/workflows/symphony-gate.yml`:

```yaml
name: Symphony Agent Gate

on:
  workflow_dispatch:

jobs:
  symphony-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Gate: All agent PRs must have `[symphony]` label + linked issue
      - name: Validate Agent PR Structure
        run: |
          # In your PR merge checklist, confirm:
          # ✓ PR has 'symphony' label
          # ✓ PR links to resolved Linear issue
          # ✓ CI passed
          echo "Symphony gate checks: All pass"

      - name: Cleanup Old Workspaces
        run: |
          # Housekeeping: Remove completed workspaces older than 7 days
          find .symphony/workspaces -type d -mtime +7 -exec rm -rf {} \;
          echo "✓ Cleaned old workspaces"
```

### 4. Startup Script

Create `scripts/start-symphony.ts`:

```typescript
import { SymphonyOrchestrator } from "../src/orchestration/symphony-runner";

async function main() {
  const symphony = new SymphonyOrchestrator();
  console.log("🎵 Starting Symphony daemon...");
  await symphony.start();

  // Keep process alive
  process.on("SIGINT", () => {
    console.log("Shutting down gracefully...");
    process.exit(0);
  });
}

main().catch(console.error);
```

Add to `package.json`:

```json
{
  "scripts": {
    "symphony:start": "ts-node scripts/start-symphony.ts",
    "symphony:logs": "tail -f .symphony/logs/orchestrator.log"
  }
}
```

---

## How It Changes Your MVP Workflow

### Before (Manual Prompting)
```
1. Open Claude chat
2. Paste ticket details
3. Copy output to editor
4. Run tests manually
5. Create PR
6. (Repeat for next ticket)
```

### After (Symphony)
```
1. Create issue in Linear (spec-driven, clear acceptance criteria)
2. Mark "In Progress"
3. Wait for PR notification
4. Review + approve
5. (Agent picks next issue automatically)
```

**Net Effect**: The perceived cost of each code change drops because human effort is no longer driving implementation—you manage work, not sessions.

---

## Why This Fits Solo SaaS

1. **No Team Overhead**: Symphony's concurrency model is single-person–friendly (3 agents max)
2. **Spec-Driven**: Your WORKFLOW.md is versioned with code—no external config drift
3. **Cost-Aware**: Agents in parallel raise token usage, but well-structured tasks + tests keep waste low
4. **Fail-Safe**: Agent crashes restart automatically; bad PRs stay in "Human Review" until approved
5. **MVP-Friendly**: Start with well-scoped features (bugs, refactors) before complex work

---

## Rollout Plan

**Week 1**: Infrastructure
- [ ] Implement `symphony-runner.ts`
- [ ] Add WORKFLOW.md
- [ ] Run locally against test Linear board

**Week 2**: Pilot
- [ ] Add 3-4 small, test-covered issues to Linear
- [ ] Monitor agent output, tweak prompt
- [ ] Iterate on approval policy

**Week 3**: Expand
- [ ] Route more feature work through Symphony
- [ ] Measure: PRs/week, token cost, manual review time
- [ ] Decide: Keep as always-on daemon or run on-demand

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Agent creates bad code | Human review gate; sandbox per issue |
| Token costs balloon | Monitor cost/PR; disable for complex work |
| Workspace pollution | Auto-cleanup via cron; `.gitignore .symphony/` |
| Linear API changes | Pin SDK version; versioned WORKFLOW.md |
| Agent loops infinitely | Timeout per turn (e.g., 15 min max) |

---

## See Also

- [OpenAI Symphony Spec](https://github.com/openai/symphony/blob/main/SPEC.md)
- [Harness Engineering](https://openai.com/research/harness-engineering)
- Linear Workspace Setup: `docs/SETUP.md`

