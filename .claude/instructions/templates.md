# HTML Email Template Rules

## Template Locations

### ML Category Templates (`ml_customer_prediction/templates/`)
| File | Category |
|------|----------|
| email_electronics.html | Electronics products |
| email_fashion.html | Fashion products |
| email_beauty.html | Beauty products |
| email_home_garden.html | Home & Garden products |
| email_sports.html | Sports products |
| email_template_final.html | Final design (legacy/reference) |
| email_template_marketing.html | Marketing design (legacy/reference) |
| email_template_professional.html | Professional design (legacy/reference) |

### UALR Major Templates (`ualr_email_automation/templates/`)
| File | Purpose |
|------|---------|
| UALR_Concise_Email_Template_Example.html | UALR branded example |
| email_template_ualr.html | Base UALR template |
| Accounting_Email_Logo_Fixed.html | Accounting major (verified) |
| Accounting_Email_With_Logo.html | Accounting major (with logo) |
| International_Business_Email_Fixed.html | International Business (verified) |
| International_Business_Email_VERIFIED.html | International Business (final) |

- Also embedded directly in UALR blueprint JSON (inside email module HTML fields)
- Guide: `docs/3-reference/UALR_All_Major_Email_Templates_Guide.md`

## Design Standards

### ML Category Templates
- Max width: 600px
- Mobile-responsive
- Compatible: Gmail, Outlook, Apple Mail

### UALR Templates
- Max width: 600px
- Brand colors: Maroon #6e2639, Gold #ffbf00, Silver #a7a9ac, Light Grey #eeeeee
- Must include: Personalized greeting, major-specific content, quick stats, CTA button
- Logo: Official UALR logo URL (see `docs/3-reference/LOGO_IMPLEMENTATION_GUIDE.md`)

## Template Variables
- Templates use Make.com variable syntax: `{{N.fieldName}}`
- Common ML variables: customer_name, customer_email, predicted_purchase_date, recommended_products, preferred_category
- UALR variables: student name, email, selected major(s)

## Editing Rules
- Maintain inline CSS (email clients strip `<style>` blocks inconsistently)
- Test in multiple email clients after changes
- Keep templates under 100KB
- Use web-safe fonts only
- Images: use absolute URLs, provide alt text
- Do NOT use JavaScript in email templates
