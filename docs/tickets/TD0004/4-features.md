# TD0004: Feature Tests

## Test 1: Blueprint JSON Validity
```json
{
  "test": "Blueprint JSON parses without errors after content modification",
  "command": "python -m json.tool < ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json > /dev/null",
  "expected": "Exit code 0",
  "passes": true
}
```

## Test 2: No Inaccurate Claims Remain
```json
{
  "test": "Critical inaccurate claims removed from all 8 modules",
  "checks": [
    "No '100% Online' in Finance module",
    "No '4 Specializations' in Management module",
    "No 'All professors are CPAs' in Accounting module",
    "No '377,500' in BIS module",
    "No '$58K-$174K' in Business Analytics module"
  ],
  "expected": "Zero matches for each check",
  "passes": true
}
```

## Test 3: Updated Stats Present
```json
{
  "test": "All 8 modules have updated statistics",
  "checks": [
    "Business Analytics shows '#10' or 'STEM'",
    "BIS shows '317K' or '317,700'",
    "Finance shows '$510K' or 'Student Fund'",
    "Management shows '3' emphases not '4'"
  ],
  "expected": "All updated values present",
  "passes": true
}
```

## Test 4: Visual Rendering Check
```json
{
  "test": "All 8 preview emails render correctly with updated content",
  "method": "Browser screenshot of each preview HTML",
  "expected": "Content readable, layout intact, no overflow or broken elements",
  "passes": true
}
```
