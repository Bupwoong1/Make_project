# TD0002: Feature Tests

## Test 1: Blueprint JSON Validity
```json
{
  "test": "Blueprint JSON parses without errors after URL modification",
  "command": "python -m json.tool < ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json > /dev/null",
  "expected": "Exit code 0, no error output",
  "passes": true
}
```

## Test 2: No Old URL Pattern Remaining
```json
{
  "test": "No /academics/ URLs remain in blueprint CTA links",
  "command": "grep -c 'ualr.edu/business/academics/' ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json",
  "expected": "Count = 0",
  "passes": true
}
```

## Test 3: All 8 New URLs Present
```json
{
  "test": "All 8 correct department URLs present in blueprint",
  "urls": [
    "ualr.edu/business/department/accounting/",
    "ualr.edu/bis/business-analytics/",
    "ualr.edu/business/department/business-information-systems/",
    "ualr.edu/business/department/economics/",
    "ualr.edu/business/department/finance/",
    "ualr.edu/business/department/international-business/",
    "ualr.edu/business/department/management/",
    "ualr.edu/business/department/marketing-and-advertising/"
  ],
  "expected": "All 8 URLs found (1 match each)",
  "passes": true
}
```

## Test 4: HTTP Accessibility
```json
{
  "test": "All 8 CTA URLs return HTTP 200 with no redirect",
  "method": "HTTP HEAD request to each URL",
  "expected": "8/8 return 200, final URL matches request URL",
  "passes": true
}
```
