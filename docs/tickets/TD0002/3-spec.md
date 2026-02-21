# TD0002: Spec

## Before (Blueprint JSON escaped format)
```
href=\\\"https://ualr.edu/business/academics/accounting/\\\"
href=\\\"https://ualr.edu/business/academics/business-analytics/\\\"
href=\\\"https://ualr.edu/business/academics/business-information-systems/\\\"
href=\\\"https://ualr.edu/business/academics/economics/\\\"
href=\\\"https://ualr.edu/business/academics/finance/\\\"
href=\\\"https://ualr.edu/business/academics/international-business/\\\"
href=\\\"https://ualr.edu/business/academics/management/\\\"
href=\\\"https://ualr.edu/business/academics/marketing/\\\"
```

## After (Blueprint JSON escaped format)
```
href=\\\"https://ualr.edu/business/department/accounting/\\\"
href=\\\"https://ualr.edu/bis/business-analytics/\\\"
href=\\\"https://ualr.edu/business/department/business-information-systems/\\\"
href=\\\"https://ualr.edu/business/department/economics/\\\"
href=\\\"https://ualr.edu/business/department/finance/\\\"
href=\\\"https://ualr.edu/business/department/international-business/\\\"
href=\\\"https://ualr.edu/business/department/management/\\\"
href=\\\"https://ualr.edu/business/department/marketing-and-advertising/\\\"
```

## Unchanged Links (Footer - already correct)
- `mailto:business@ualr.edu` — email, no change needed
- `https://ualr.edu/business/` — 200 OK, no redirect
- `https://ualr.edu/admissions/` — 200 OK, no redirect
