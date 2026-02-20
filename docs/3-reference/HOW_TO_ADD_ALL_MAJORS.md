# How to Add All 8 Majors to Your Blueprint

## Quick Overview

You currently have a blueprint with **2 majors** (Accounting and Business Analytics).
You need to add **6 more majors** (Business Information Systems, Economics, Finance, International Business, Management, Marketing).

---

## Option 1: Use Make.com Interface (Easiest)

### Step-by-Step Instructions:

1. **Import the existing blueprint** to Make.com
   - File: `UALR_Prospective_Student_Email_Automation.blueprint.json`

2. **Find the Router module** (it's the blue diamond shape after Google Sheets)

3. **For each of the 6 remaining majors, do this:**

   **A. Right-click on the router → "Add another route"**

   **B. Add a FILTER to the new route:**
   - Click "Set up a filter"
   - Label: "[Major Name] Major" (e.g., "Finance Major")
   - Condition:
     - Field 1: `{{1.3}}` (the Major Preference column)
     - Operator: **contains** (not equals!)
     - Field 2: Type the major name exactly (e.g., "Finance")
   - Click OK

   **C. Add an EMAIL module after the filter:**
   - Click the + button after filter
   - Search for "Email"
   - Select "Send an Email"
   - Configure:
     - Connection: Select your email account
     - To: `{{1.2}}` (student email)
     - Subject: `UALR School of Business - [Major Name] Program`
     - Content Type: HTML
     - Content: Copy HTML from the file `UALR_Complete_6_Additional_Majors.json` for that specific major

   **D. Add an UPDATE SHEET module:**
   - Click the + button after email module
   - Search for "Google Sheets"
   - Select "Update a Row"
   - Configure:
     - Connection: Select your Google Sheets connection
     - Spreadsheet: Select your form responses spreadsheet
     - Sheet: Form Responses 1
     - Row Number: `{{1.__ROW_NUMBER__}}`
     - Column 4 (Email Status): `Email Sent - {{now}}`

4. **Repeat Step 3 for all 6 majors:**
   - Business Information Systems
   - Economics
   - Finance
   - International Business
   - Management
   - Marketing

5. **Test the automation:**
   - Submit test forms for each major
   - Verify emails are received
   - Check that spreadsheet updates

---

## Option 2: Manually Edit JSON (Advanced)

### For Technical Users:

1. **Open** `UALR_Prospective_Student_Email_Automation.blueprint.json` in a text editor (VS Code recommended)

2. **Find the router section** - Search for `"id": 2` and `"routes":`

3. **Copy the route structure** from `UALR_Complete_6_Additional_Majors.json`

4. **Add each route** to the `routes` array (6 new routes total)

5. **Update these values in each new route:**
   - Change `"id"` to unique numbers (5-18, incrementing by 1 for each module)
   - Update `"__IMTCONN__"` with your actual connection IDs
   - Update `"spreadsheetId"` with your actual spreadsheet ID
   - Update `"account"` with your email account ID

6. **Save** the file

7. **Re-import** to Make.com

---

## Complete Major List with Key Points

### 1. ✅ Accounting (Already in blueprint)
- CPA-ready curriculum
- Expert CPA faculty
- Beta Alpha Psi

### 2. ✅ Business Analytics (Already in blueprint)
- 35% job growth
- Data analytics skills
- $58K-$174K salary

### 3. ⭐ Business Information Systems (TO ADD)
- 377,500 annual jobs
- SQL & programming
- $59K-$136K salary

### 4. ⭐ Economics (TO ADD)
- Law school preparation
- Research opportunities
- Policy analysis

### 5. ⭐ Finance (TO ADD)
- 3 specialization tracks
- CFA Level I prep
- Banking & wealth management

### 6. ⭐ International Business (TO ADD)
- Global marketplace
- Interdisciplinary approach
- Multinational careers

### 7. ⭐ Management (TO ADD)
- 4 specialization areas
- Leadership development
- Executive networking

### 8. ⭐ Marketing (TO ADD)
- Digital marketing & sales
- AI-powered marketing
- Real-world projects

---

## Important: Filter Configuration

### ⚠️ Use "contains" NOT "equals"!

Since students can select MULTIPLE majors using checkboxes, you must use:

**Correct:**
```
{{1.3}} contains "Finance"
```

**Incorrect:**
```
{{1.3}} equals "Finance"
```

**Why?**
If a student selects "Finance, Accounting, Marketing", the cell value will be:
```
Finance, Accounting, Marketing
```

Using "contains" ensures they get ALL three emails.

---

## Visual Blueprint Structure

```
[Google Sheets Trigger]
         ↓
    [Router] ──→ [Filter: Accounting] → [Email: Accounting] → [Update Sheet]
         ├──→ [Filter: Business Analytics] → [Email: Bus Analytics] → [Update Sheet]
         ├──→ [Filter: BIS] → [Email: BIS] → [Update Sheet]
         ├──→ [Filter: Economics] → [Email: Economics] → [Update Sheet]
         ├──→ [Filter: Finance] → [Email: Finance] → [Update Sheet]
         ├──→ [Filter: Int'l Business] → [Email: Int'l Bus] → [Update Sheet]
         ├──→ [Filter: Management] → [Email: Management] → [Update Sheet]
         └──→ [Filter: Marketing] → [Email: Marketing] → [Update Sheet]
```

---

## Email Template Locations

All HTML email templates are in:
📄 `UALR_Complete_6_Additional_Majors.json`

Each route contains:
- Filter configuration
- Complete HTML email template
- Google Sheets update configuration

---

## Testing Checklist

After adding all majors, test each one:

- [ ] Business Information Systems email sends correctly
- [ ] Economics email sends correctly
- [ ] Finance email sends correctly
- [ ] International Business email sends correctly
- [ ] Management email sends correctly
- [ ] Marketing email sends correctly
- [ ] Multiple major selections work (e.g., selecting "Finance, Marketing" sends 2 emails)
- [ ] Google Sheet updates with "Email Sent" status
- [ ] All emails display correctly on mobile
- [ ] All "Learn More" links work
- [ ] Contact information is correct

---

## Quick Start: 5-Minute Setup

1. ✅ Import blueprint to Make.com
2. ✅ Connect Google Sheets
3. ✅ Connect Email
4. ⭐ Right-click router → Add 6 new routes
5. ⭐ For each route:
   - Set filter: `{{1.3}} contains "[Major Name]"`
   - Add email module with HTML template
   - Add update sheet module
6. ✅ Test with sample form submission
7. ✅ Activate automation

**Time estimate:** 5-10 minutes per major = 30-60 minutes total

---

## Need Help?

### Common Questions:

**Q: Where do I get the HTML templates?**
A: They're in `UALR_Complete_6_Additional_Majors.json` - copy/paste into each email module.

**Q: How do I know my connection IDs?**
A: Make.com will auto-populate these when you select connections in the interface. If editing JSON manually, check existing modules for the IDs.

**Q: What if a student selects all 8 majors?**
A: They'll receive all 8 emails! The router will trigger every route where the filter matches.

**Q: Can I customize the email templates?**
A: Yes! Edit the HTML in each email module. The styling is inline CSS, so it's easy to modify colors, fonts, etc.

**Q: How do I add the UALR logo?**
A: Upload your logo to a web host (or use Make.com's file storage), get the URL, and add this to each template's header:
```html
<img src="YOUR_LOGO_URL" alt="UALR" style="max-width: 250px;">
```

---

## Files You Need

1. **UALR_Prospective_Student_Email_Automation.blueprint.json** - Starting point (2 majors)
2. **UALR_Complete_6_Additional_Majors.json** - All 6 additional email templates
3. **UALR_Google_Form_Setup_Guide.md** - Google Form configuration
4. **UALR_SETUP_INSTRUCTIONS.md** - Complete setup guide
5. **HOW_TO_ADD_ALL_MAJORS.md** - This file!

---

## Success Metrics

Once fully implemented, you should see:
- ✅ 8 active routes in your Make.com scenario
- ✅ All 8 emails sending automatically
- ✅ Google Sheet updating with timestamps
- ✅ Students receiving emails within 15-30 minutes
- ✅ No errors in Make.com execution history

---

**Ready to get started?** Follow Option 1 (Make.com Interface) for the easiest setup!

**Questions?** Check the troubleshooting section in `UALR_SETUP_INSTRUCTIONS.md`

---

**Last Updated:** January 2025
**Estimated Setup Time:** 30-60 minutes
**Difficulty:** Beginner to Intermediate
