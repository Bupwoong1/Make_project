# Make.com Automation Rules

## Blueprint Files
Make.com scenarios are exported/imported as `.blueprint.json` files. Each sub-project keeps its blueprints in its own `blueprints/` directory.

### UALR Blueprints (`ualr_email_automation/blueprints/`)
| File | Purpose |
|------|---------|
| UALR_Complete_All_8_Majors.blueprint.json | UALR email automation — all 8 majors (★ primary) |
| UALR_Prospective_Student_Email_Automation.blueprint.json | UALR email (base version) |
| UALR_Complete_6_Additional_Majors.json | Config for additional majors |

### ML Blueprints (`ml_customer_prediction/blueprints/`)
| File | Purpose |
|------|---------|
| ML_Customer_Purchase_Prediction_READY.blueprint.json | ML prediction + email (★ primary) |
| ML_Customer_Purchase_Prediction_WITH_IMAGES.blueprint.json | ML prediction + email with product images |
| ML_Customer_Purchase_Prediction.blueprint.json | ML prediction (base version) |

### Archived Blueprints
- `ml_customer_prediction/old/` — Earlier iteration blueprints (reference only)

## Blueprint Structure
Make.com blueprint JSON contains:
- `modules[]` — Ordered list of scenario modules
- Each module has: `id`, `module` (type), `mapper` (configuration), `metadata`
- Router modules contain `routes[]` with filter conditions
- Variable references use `{{moduleId.fieldName}}` syntax

## Editing Rules
- NEVER manually edit blueprint JSON unless absolutely necessary
- Prefer editing in Make.com UI and re-exporting
- When manual edits are needed:
  - Validate JSON syntax after editing (`python -m json.tool < file.json`)
  - Preserve module IDs (changing them breaks connections)
  - Preserve metadata section
  - Test import into Make.com after changes

## Two Sub-Projects

### 1. UALR Email Automation (`ualr_email_automation/`)
- **Trigger**: Google Sheets (Watch Rows) — new form submissions
- **Flow**: Read row → Router (8 routes, one per major) → Send email + Update sheet
- **Filter**: "contains" match on major field (supports multiple selections)
- **8 Majors**: Accounting, Business Analytics, Business Information Systems, Economics, Finance, International Business, Management, Marketing
- **Blueprints**: `ualr_email_automation/blueprints/`
- **Templates**: `ualr_email_automation/templates/`
- **Setup guides**: `docs/3-reference/UALR_SETUP_INSTRUCTIONS.md`, `docs/3-reference/UALR_Google_Form_Setup_Guide.md`

### 2. ML Customer Prediction (`ml_customer_prediction/`)
- **Trigger**: Google Sheets (Watch Rows) — customer data
- **Flow**: Read row → HTTP POST to Flask API → Parse JSON → Router (send_now/send_soon/wait) → Send email + Update sheet
- **Requires**: Flask API running + ngrok tunnel active
- **Blueprints**: `ml_customer_prediction/blueprints/`
- **Templates**: `ml_customer_prediction/templates/`
- **Setup guide**: `docs/3-reference/SETUP_GUIDE.md`, `docs/3-reference/MAKE_SETUP_INSTRUCTIONS.md`
