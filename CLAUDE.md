# CLAUDE.md

## Repository Directory Structure
```
CLAUDE.md                          # Project policies (this file)
.claude/
├── agents/                        # Specialized sub-agents
│   ├── code-mapper.md             # Code-map and spec document creator
│   ├── ticket-handler.md          # Ticket workflow implementer
│   └── ticket-codemap-inspector.md # Implementation verifier
├── rules/                         # Auto-loaded every session
│   ├── core.md                    # Core behavior rules
│   ├── blueprint-protection.md    # Make.com blueprint safety
│   └── testing.md                 # Testing requirements
├── skills/                        # Selectively loaded context
│   ├── flask-api/SKILL.md         # Flask API development rules
│   ├── make-automation/SKILL.md   # Make.com blueprint rules
│   ├── html-templates/SKILL.md    # HTML email template rules
│   └── ticket-workflow/SKILL.md   # Ticket orchestration
├── settings.json                  # Shared hooks (git-tracked)
└── settings.local.json            # Personal permissions (git-ignored)
docs/
├── 1-prd/                         # Product Requirements
│   └── FINAL_IMPLEMENTATION_SUMMARY.md
├── 2-current/                     # Code-maps and specs (current state)
├── 3-reference/                   # Operational guides
│   ├── what-is-ticket-workflow.md
│   ├── how-to-create-codemap.md
│   ├── how-to-test-make-project.md
│   ├── SETUP_GUIDE.md
│   ├── UALR_SETUP_INSTRUCTIONS.md
│   ├── UALR_Google_Form_Setup_Guide.md
│   ├── MAKE_SETUP_INSTRUCTIONS.md
│   ├── HOW_TO_ADD_ALL_MAJORS.md
│   ├── LOGO_IMPLEMENTATION_GUIDE.md
│   └── UALR_All_Major_Email_Templates_Guide.md
└── tickets/                       # Ticket documents
    ├── archive/
    ├── TD000X/
    └── index.md
ualr_email_automation/             # Sub-project 1: UALR Email Automation
├── blueprints/                    # Make.com blueprints
├── templates/                     # UALR-branded HTML email templates
└── resources/                     # Brochures, reference materials
ml_customer_prediction/            # Sub-project 2: ML Customer Prediction
├── blueprints/                    # Make.com blueprints
├── templates/                     # Category-specific HTML email templates
├── old/                           # Archived blueprint iterations
├── ml_prediction_api.py           # Flask ML prediction API
├── test_api.py                    # API test server
├── test_request.json              # Sample API request
├── customer_purchase_data.csv     # Sample customer data (33 customers)
└── requirements.txt               # Python dependencies
```

## Project Overview
Two independent sub-projects managed under one repository:

1. **UALR Email Automation** (`ualr_email_automation/`): Google Form → Make.com → personalized emails for 8 business majors
2. **ML Customer Prediction** (`ml_customer_prediction/`): Flask API (Random Forest) → Make.com → targeted marketing emails

Tech stack: Flask (Python), Make.com, Google Sheets, ngrok, HTML email templates.

## Architecture

### Context Loading Strategy
- **Rules** (`.claude/rules/`): Auto-loaded every session. Core behavior, blueprint protection, testing requirements.
- **Skills** (`.claude/skills/`): Loaded on demand by agents or when context matches. Flask API, Make.com, HTML templates, ticket workflow.
- **Agents** (`.claude/agents/`): Specialized sub-agents with tool restrictions and skill preloading. Delegate tasks to them.

### References
- **MUST READ**: `docs/3-reference/what-is-ticket-workflow.md`
- `docs/3-reference/how-to-test-make-project.md`
- `docs/1-prd/FINAL_IMPLEMENTATION_SUMMARY.md` (project overview)
