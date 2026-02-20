---
description: Ticket workflow orchestration. Load when user mentions a ticket number (TD00XX) or wants to start/continue a ticket-based development workflow.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - Task
---

# Ticket Workflow Orchestrator

You are continuing work on a long-running autonomous development task iteratively documented by the ticket workflow. This is a FRESH context window — you have no memory of previous sessions.

If the user mentions any ticket number to get started, follow the steps below.

## STEP 1: GET YOUR BEARINGS (MANDATORY)

Read these documents to orient yourself:
- `docs/3-reference/what-is-ticket-workflow.md`
- `docs/3-reference/how-to-test-make-project.md`
- All ticket documents in the ticket directory
- Git commit history (especially for current ticket number)

If the user requests additional tasks not in the mentioned ticket, append them to `1-definition.md` and update all downstream documents.

**IMPORTANT**: If the user's new request is not part of the latest ticket, ask whether to create a new ticket `1-definition.md`. If the user declines (usually because the task is trivial), proceed without ticket documentation.

## STEP 2: TICKET-HANDLER AGENT

The `ticket-handler` agent processes the ticket workflow. Assign the ticket to it if the ticket is not completed (some feature tests have `passes: false`).

Your main task is to **monitor** the ticket-handler agent and re-invoke it as needed. The agent may not finish the entire workflow in a single session due to context window limits. All progress is written in ticket documents. After the agent finishes, check status by reading `4-features.md`, `5-progress-and-issues.md`, and `6-final.md`.

## STEP 3: INCOMPLETE FEATURE TESTS

If features still have `passes: false` with no blocking issues, invoke another ticket-handler agent to continue.

If the ticket-handler reports a blocking issue, investigate yourself first to confirm. Report to the user if confirmed. If you can solve it, fix it and continue the workflow.

## STEP 4: COMPLETED FEATURE TESTS

If all features pass, the ticket workflow is complete. Verify all ticket documentation is ready and report back to the user.
