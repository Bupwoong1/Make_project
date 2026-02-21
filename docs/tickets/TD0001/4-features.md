# TD0001: Feature Tests

## Test 1: Blueprint JSON Validity
```json
{
  "test": "Blueprint JSON parses without errors after modification",
  "command": "python -m json.tool < ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json > /dev/null",
  "expected": "Exit code 0, no error output",
  "passes": false
}
```

## Test 2: All 8 Modules Have Image Logo
```json
{
  "test": "All 8 email modules contain <img> tag with UALR logo URL",
  "command": "grep -c 'ua-little-rock-v-rgb.png' ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json",
  "expected": "Count = 8 (one per email module)",
  "passes": false
}
```

## Test 3: No Text Logo Remaining
```json
{
  "test": "No email modules still use text-only logo div",
  "command": "grep -c '<div class=.logo.>UA LITTLE ROCK</div>' ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json",
  "expected": "Count = 0 (all text logos replaced)",
  "passes": false
}
```

## Test 4: Template Files Synchronized
```json
{
  "test": "Standalone HTML template files also updated with image logo",
  "files": [
    "ualr_email_automation/templates/Accounting_Email_Logo_Fixed.html",
    "ualr_email_automation/templates/email_template_ualr.html"
  ],
  "expected": "Each file contains <img> tag with UALR logo URL",
  "passes": false
}
```
