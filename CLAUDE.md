# CLAUDE.md

## Core Rules
- Do what has been asked; nothing more, nothing less.
- NEVER create files unless absolutely necessary. Prefer editing existing files.
- NEVER proactively create documentation files (*.md) unless explicitly requested.
- Documentation is a core deliverable. Update docs after discussion, planning, implementation, and testing.

## Repository Directory Structure
```
CLAUDE.md                          # Claude Code policies and rules (Do not update unless specified)
docs/
├── 1-prd/                         # Product Requirements (Do not update unless specified)
│   └── FINAL_IMPLEMENTATION_SUMMARY.md
├── 2-current/                     # Design/system docs reflecting current implementation
├── 3-reference/                   # Operational guides and setup instructions
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
    ├── archive/                   # Completed older tickets
    ├── TD000X/                    # Active ticket directories
    └── index.md                   # Index of all ticket numbers and titles
ualr_email_automation/             # UALR Email Automation (Sub-project 1)
├── blueprints/                    # Make.com blueprint JSON files
│   ├── UALR_Complete_All_8_Majors.blueprint.json (★ primary)
│   └── UALR_Prospective_Student_Email_Automation.blueprint.json
├── templates/                     # UALR-branded HTML email templates
│   ├── UALR_Concise_Email_Template_Example.html
│   ├── Accounting_Email_Logo_Fixed.html
│   └── International_Business_Email_*.html
└── resources/                     # Brochures, reference materials
ml_customer_prediction/            # ML Customer Prediction (Sub-project 2)
├── blueprints/                    # Make.com blueprint JSON files
│   ├── ML_Customer_Purchase_Prediction_READY.blueprint.json (★ primary)
│   └── ML_Customer_Purchase_Prediction_WITH_IMAGES.blueprint.json
├── templates/                     # Category-specific HTML email templates
│   ├── email_electronics.html
│   ├── email_fashion.html
│   ├── email_beauty.html
│   ├── email_home_garden.html
│   └── email_sports.html
├── old/                           # Archived blueprint iterations
├── ml_prediction_api.py           # Flask ML prediction API (main entry point)
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

## References
- **MUST READ**: docs/3-reference/what-is-ticket-workflow.md
- docs/3-reference/how-to-test-make-project.md
- docs/1-prd/FINAL_IMPLEMENTATION_SUMMARY.md (project overview)

## Agents
- Actively use agents in `.claude/agents/` for matching tasks. Give detailed instructions.

## Development
@.claude/instructions/api.md
@.claude/instructions/automation.md
@.claude/instructions/templates.md

## Ticket Workflow
@.claude/instructions/orchestrator.md
