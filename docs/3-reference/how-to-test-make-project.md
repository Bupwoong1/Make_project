## TESTING REQUIREMENTS

**CRITICAL**: ALL testing must use appropriate verification methods for each component type. Never mark a test as passing without evidence.

### Flask API Testing

**Start the API server:**
```bash
cd ml_customer_prediction
python ml_prediction_api.py
# Runs on http://localhost:8080
```

**Health check:**
```bash
curl http://localhost:8080/health
```

**Single prediction test:**
```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d @ml_customer_prediction/test_request.json
```

**Batch prediction test:**
```bash
curl -X POST http://localhost:8080/batch_predict \
  -H "Content-Type: application/json" \
  -d '{"customers": [...]}'
```

**Error handling test:**
```bash
# Missing required fields
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{}'

# Invalid data types
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"days_since_purchase": "not_a_number"}'
```

**Response validation checklist:**
- [ ] HTTP status code is correct (200, 400, 500)
- [ ] Response body is valid JSON
- [ ] All expected fields present (predicted_days, confidence, segment, email_timing, recommended_products)
- [ ] Field types are correct (float, str, list)
- [ ] Confidence score is in expected range (0.6-0.9)
- [ ] Customer segment is one of: VIP, Premium, Regular, Growing, New
- [ ] Email timing is one of: send_now, send_soon, wait

### Make.com Blueprint Validation

**JSON syntax check:**
```bash
python -m json.tool < BLUEPRINT_FILE.blueprint.json > /dev/null
```

**Structure validation:**
- [ ] Blueprint JSON parses without errors
- [ ] `modules` array exists and is non-empty
- [ ] Each module has `id`, `module` (type string), and `mapper` fields
- [ ] Module connections form a valid chain (no orphaned modules)

**Router validation:**
- [ ] Router module has `routes` array
- [ ] Each route has a `filter` with valid condition
- [ ] Filter `name` matches intended routing logic
- [ ] All routes lead to valid downstream modules

**Variable mapping validation:**
- [ ] All `{{N.field}}` references point to valid module IDs
- [ ] Referenced fields exist in the source module's output
- [ ] No broken variable references

**End-to-end (requires Make.com account):**
1. Import blueprint into Make.com
2. Configure all module connections (Google Sheets, Gmail, HTTP)
3. Run scenario once with test data
4. Verify each module executes without error
5. Check final output (email sent, sheet updated)

### HTML Email Template Verification

**Well-formed HTML:**
- Open template file in a web browser
- Check for rendering errors or broken layout

**Template variable check:**
```bash
# Find all variable placeholders
grep -o '{{[^}]*}}' TEMPLATE_FILE.html
```
- [ ] All variables are documented
- [ ] No orphan variables (referenced but never populated)
- [ ] Variable syntax matches Make.com format: `{{N.fieldName}}`

**Responsive design:**
- Open in browser, resize to 320px width (mobile)
- Check layout doesn't break
- Text remains readable
- CTA buttons are tappable size

**Email client compatibility:**
- Send test email to Gmail
- Send test email to Outlook
- Verify rendering in both clients
- Check images load correctly
- Verify links work

### ngrok Integration Testing

**Full integration test sequence:**

1. **Start Flask API:**
```bash
cd ml_customer_prediction
python ml_prediction_api.py
# Verify: curl http://localhost:8080/health
```

2. **Start ngrok tunnel:**
```bash
ngrok http 8080
# Note the public URL: https://xxxx.ngrok-free.app
```

3. **Test public URL:**
```bash
curl https://xxxx.ngrok-free.app/health
curl -X POST https://xxxx.ngrok-free.app/predict \
  -H "Content-Type: application/json" \
  -d @test_request.json
```

4. **Update Make.com HTTP module:**
- Open Make.com scenario
- Update HTTP module URL to new ngrok URL
- Save scenario

5. **Run Make.com scenario once:**
- Use "Run once" button
- Verify all modules execute successfully
- Check email was sent
- Check Google Sheet was updated

### Test Data

| File | Purpose |
|------|---------|
| `ml_customer_prediction/test_request.json` | Sample single prediction request |
| `ml_customer_prediction/customer_purchase_data.csv` | 33 sample customers for batch testing |
| `ml_customer_prediction/test_api.py` | Minimal Flask health check server |

### Customer Data Fields

| Field | Type | Example |
|-------|------|---------|
| customer_id | str | "CUST001" |
| customer_email | str | "john@example.com" |
| customer_name | str | "John Smith" |
| days_since_purchase | int | 15 |
| total_purchases | int | 25 |
| avg_purchase_amount | float | 89.50 |
| preferred_category | str | "Electronics" |

### UALR Email Automation Testing

**Google Form → Make.com flow:**
1. Submit a test Google Form response
2. Verify new row appears in linked Google Sheet
3. Wait for Make.com trigger to fire (or use "Run once")
4. Verify router selects correct major route
5. Verify email is sent with correct major-specific content
6. Verify Google Sheet status column is updated

**Major routing validation:**
- Test each of the 8 majors individually
- Test multiple major selection (if supported)
- Verify correct email template is used per major

### Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| ngrok URL expired | Free tier URLs change on restart | Restart ngrok, update Make.com HTTP URL |
| Flask API not responding | Server not running | `python ml_prediction_api.py` |
| Make.com 404 error | Wrong ngrok URL in HTTP module | Update URL in Make.com |
| Email not sent | Gmail connection expired | Re-authorize Gmail in Make.com |
| Blueprint import fails | Invalid JSON | `python -m json.tool < file.json` to check |
