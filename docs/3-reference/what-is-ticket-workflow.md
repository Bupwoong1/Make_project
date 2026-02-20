## TICKETS Workflow

**CRITICAL**: Ticket system is a main workflow that defines how this project should be managed. Each ticket defines a task request from the user. Each ticket is assigned to have its own directory under docs/tickets/.

Each ticket has sequence number of the format TD000X (in regex ^TD\d{4}$, starting with TD, followed by 4 digits 0-padded incremented by 1).

Under each ticket directory like docs/tickets/TD000X/, the following documents should be managed. These documents should have FIXED naming. The number suggests the order of tasks.

```
docs/tickets/TD000X
├── 1-definition.md
├── 2-plan.md
├── 3-spec.md
├── 4-features.md
├── 5-progress-and-issues.md
└── 6-final.md
```

- `1-definition.md`: This definition file contains the task objective, related requirements, out-of-scope items (for clarification if any) and success criteria if any.

- `2-plan.md`: Based on `1-definition.md`, plan how to tackle given task. The plan should be concise. This plan should NOT contain time estimation. Need to add this ticket name to docs/tickets/index.md when this file is created.

- `3-spec.md`: Based on previous documents `1-definition.md` and `2-plan.md`, define specifications. You need to clearly define input and output format, major error cases. The specification should be have enough details for code generation.

- `4-features.md`: Based on previous documents, define testable features with testing steps as follows:

**Format:**
```json
[
  {
    "category": "functional",
    "description": "Brief description of the feature and what this test verifies",
    "steps": [
      "Step 1: Navigate to relevant page",
      "Step 2: Perform action",
      "Step 3: Verify expected result"
    ],
    "passes": false
  },
  {
    "category": "style",
    "description": "Brief description of UI/UX requirement",
    "steps": [
      "Step 1: Navigate to page",
      "Step 2: Take screenshot",
      "Step 3: Verify visual requirements"
    ],
    "passes": false
  }
]
```

**Requirements for `4-features.md`:**
- Both "functional" and "style" categories
- Mix of narrow tests (2-5 steps) and comprehensive tests (10+ steps)
- Order features by priority: fundamental features first
- ALL tests start with "passes": false
- Cover every feature in the spec exhaustively
- **IMPORTANT**: review `4-features.md` features if they are absolutely needed. eliminate features that are duplicated or tested by combination of earlier features

- `5-progress-and-issues.md`: Write current progress and all identified issues during implementation and testing. Do not write testing pass/fail in this file. Update "passes" fields directly in `4-features.md`.

- `6-final.md`: Once all tests pass in `4-features.md` file, generate the final reports on this task. Summarize all events happened in this ticket. Address remaining issues identified. You may suggest next steps. Keep it simple and ultra consice.

**IMPORTANT**: DO NOT USE TICKET NUMBER (e.g. TD0064) AS PART OF CLASS, VARIABLE, FUNCTION, MODULE, AND/OR SCRIPT NAME. ONLY USE IT IN COMMENTS OR DOCSTRING AS REFERENCE.
**CRITICAL**: While working on a ticket, if the user requests some changes to codebase, always append them to `1-definion.md` (or rewrite the sections if explicitly requested) first, then update `2-plan.md` and `3-spec.md` before applying the changes to the codebase. Always remember documentation first before implementation.

### TICKETS Index

To maintain index of all tickets, each ticket name should be indexed in docs/tickets/index.md. The content of the docs/tickets/index.md should be EXACTLY the following:

```
TD0001 {Brief Name of the task}
TD0002 {Brief Name of the task}
TD0003 {Brief Name of the task}
...
```

No other content should be included. The new ticket MUST BE ADDED when creating `2-plan.md` file for the first time for that ticket.

### TICKETS Workflow Archive for Older Tickets

Older tickets are moved to docs/tickets/archive/. If a ticket directory is not found under docs/tickets/, you should look for docs/tickets/archive/TD000X.
