# TD0003: Feature Tests

## Test 1: Blueprint JSON Validity
```json
{
  "test": "Blueprint JSON parses without errors after modification",
  "command": "python -m json.tool < ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json > /dev/null",
  "expected": "Exit code 0",
  "passes": true
}
```

## Test 2: All 8 Modules Have Unit Mark
```json
{
  "test": "All 8 email modules use School of Business unit mark from GitHub",
  "command": "grep -c 'sob_unit_mark.png' ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json",
  "expected": "Count = 8",
  "passes": true
}
```

## Test 3: Visual Rendering — Logo Visible
```json
{
  "test": "Unit mark renders clearly with matching background color",
  "method": "Browser screenshot of preview HTML files",
  "expected": "White unit mark seamlessly blends with #6b0733 header background in all 8 modules",
  "passes": true
}
```

## Test 4: Visual Rendering — Layout Integrity
```json
{
  "test": "Overall email layout renders correctly with no broken elements",
  "method": "Browser screenshot full page for each module",
  "expected": "Header, content, stats, CTA button, footer all render correctly",
  "passes": true
}
```
