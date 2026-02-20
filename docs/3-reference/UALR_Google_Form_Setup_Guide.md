# UA Little Rock School of Business - Google Form Setup

## 📝 Complete Google Form Configuration

---

## Form Header

### **Form Title:**
```
UA Little Rock School of Business
Program Information Request
```

### **Form Description:**
```
Thank you for your interest in the UA Little Rock School of Business!

We're excited to help you explore our AACSB-accredited programs. Please complete this brief form, and we'll send you detailed information about the major(s) you're interested in.

• Ranked #32 in U.S. News Online Business Programs (2023)
• Tuition starting at just $3,500 per semester
• $200,000+ in annual scholarships available
• Flexible on-campus and online learning options

Questions? Contact us at business@ualr.edu or (501) 569-3000
```

---

## Form Questions

### **Question 1: Full Name**

**Question Type:** Short answer

**Question Text:**
```
Full Name *
```

**Help Text (optional):**
```
Please enter your first and last name
```

**Settings:**
- ✅ Required
- Response validation: None

---

### **Question 2: Email Address**

**Question Type:** Short answer

**Question Text:**
```
Email Address *
```

**Help Text (optional):**
```
We'll send program information to this email address
```

**Settings:**
- ✅ Required
- ✅ Response validation: Text → Email address
- Error message: "Please enter a valid email address"

---

### **Question 3: Major Preferences**

**Question Type:** Checkboxes (allows multiple selections)

**Question Text:**
```
Which major(s) are you interested in learning more about? *
(Check all that apply)
```

**Help Text (optional):**
```
Select all programs you'd like to receive information about. You can choose more than one!
```

**Checkbox Options:**
1. ☐ Accounting
2. ☐ Business Analytics
3. ☐ Business Information Systems
4. ☐ Economics
5. ☐ Finance
6. ☐ International Business
7. ☐ Management
8. ☐ Marketing

**Settings:**
- ✅ Required
- Minimum selections: 1
- Data validation: "Select at least 1 option"

---

### **Question 4 (Optional): Phone Number**

**Question Type:** Short answer

**Question Text:**
```
Phone Number (Optional)
```

**Help Text (optional):**
```
If you'd like an admissions counselor to contact you by phone, please provide your number
```

**Settings:**
- ⬜ Not required
- Response validation: None (or Text → Phone number)

---

### **Question 5 (Optional): Expected Graduation Year**

**Question Type:** Dropdown

**Question Text:**
```
When do you plan to start your program? (Optional)
```

**Dropdown Options:**
1. Fall 2025
2. Spring 2026
3. Summer 2026
4. Fall 2026
5. Spring 2027
6. Not sure yet

**Settings:**
- ⬜ Not required

---

### **Question 6 (Optional): How did you hear about us?**

**Question Type:** Multiple choice

**Question Text:**
```
How did you hear about UA Little Rock School of Business? (Optional)
```

**Multiple Choice Options:**
1. ○ Google Search
2. ○ Social Media
3. ○ Friend/Family Recommendation
4. ○ High School Counselor
5. ○ College Fair
6. ○ UALR Website
7. ○ Other

**Settings:**
- ⬜ Not required

---

## Form Settings Configuration

### **Presentation Settings:**

1. Click the "Settings" gear icon at the top
2. Go to "Presentation" tab:
   - ✅ Show progress bar
   - ✅ Shuffle question order: OFF
   - ✅ Show link to submit another response

**Confirmation Message:**
```
Thank you for your interest in UA Little Rock School of Business!

We've received your information request. You'll receive detailed program information about your selected major(s) via email within the next 15-30 minutes.

In the meantime, feel free to explore our website at ualr.edu/business

Questions? Contact us:
📧 business@ualr.edu
📞 (501) 569-3000
```

---

### **Responses Settings:**

1. Go to "Responses" tab in Settings:
   - ✅ Collect email addresses: OFF (we're already collecting it as a question)
   - ✅ Limit to 1 response: OFF (allow multiple inquiries)
   - ✅ Edit after submit: OFF
   - ✅ See summary charts and text responses: ON

2. Click "Select response destination" (green Sheets icon)
   - Create a new spreadsheet
   - Name it: "UALR Prospective Students - [Current Year]"

---

## Google Sheet Setup (After Linking Form)

### **Automatic Columns Created:**
- Column A: Timestamp
- Column B: Full Name
- Column C: Email Address
- Column D: Which major(s) are you interested in learning more about? (Check all that apply)
- Column E: Phone Number (Optional) - if added
- Column F: When do you plan to start your program? (Optional) - if added
- Column G: How did you hear about UA Little Rock School of Business? (Optional) - if added

### **Manual Column to Add:**

After the form creates the spreadsheet, manually add:

**Column H (or next available):** Email Status

**Header Text:** `Email Status`

**Purpose:** The Make.com automation will update this column with timestamps when emails are sent

**Sample values:**
- "Email Sent - 2025-01-15 10:30 AM"
- "Email Sent - 2025-01-15 11:45 AM"

---

## Form Styling (Optional)

### **Theme Customization:**

1. Click the palette icon at the top
2. **Header Style:** Choose "Header image"
3. Upload UALR School of Business header image (if available)
4. **Theme Color:** Select custom color
   - Primary Color: `#6e2639` (UALR Maroon)
   - Background Color: `#ffffff` (White)
   - Font Style: "Modern" or "Classic"

### **Custom Header Image Dimensions:**
- Recommended size: 1600 x 400 pixels
- Format: JPG or PNG
- Content: UA Little Rock School of Business logo/building

---

## Form Sharing Options

### **Share Link Settings:**

1. Click "Send" button at top right
2. Select link icon (</>)
3. ✅ Shorten URL (using Google's URL shortener)
4. Copy the link

**Suggested Short URL Structure:**
- `bit.ly/ualr-business-info`
- `ualr.edu/business-inquiry` (if you have domain redirect access)

### **Where to Share the Form:**

1. **UALR School of Business Website**
   - Add as "Request Information" button
   - Include in footer
   - Popup on major program pages

2. **Social Media**
   - Facebook, Instagram, Twitter bio links
   - LinkedIn posts
   - YouTube video descriptions

3. **Email Signatures**
   - Faculty and staff email signatures
   - Admissions team emails

4. **Print Materials**
   - QR code on brochures
   - Business cards
   - Campus event flyers

5. **Recruitment Events**
   - College fairs
   - High school visits
   - Virtual open houses

---

## Testing Checklist

Before going live, test the form:

- [ ] Submit test response with your email
- [ ] Check that data appears correctly in Google Sheet
- [ ] Verify all required fields work properly
- [ ] Test email validation
- [ ] Confirm checkbox selections save correctly
- [ ] Test on mobile device
- [ ] Verify confirmation message displays
- [ ] Check Make.com automation triggers
- [ ] Confirm email is received with correct major info
- [ ] Verify "Email Status" column updates in sheet

---

## Form Analytics & Monitoring

### **View Form Responses:**

1. Open Google Form
2. Click "Responses" tab
3. View:
   - **Summary:** Charts and aggregate data
   - **Individual:** Each submission
   - **Spreadsheet:** All data in linked sheet

### **Key Metrics to Track:**

- Total form submissions
- Submissions by major (which majors are most popular)
- Response rate over time
- Peak submission times
- Conversion from form to email sent

### **Google Sheets Formula Examples:**

**Count total submissions:**
```
=COUNTA(B2:B)
```

**Count emails sent:**
```
=COUNTIF(H2:H,"Email Sent*")
```

**Most popular major:**
```
=MODE(D2:D)
```

---

## Advanced: Multiple Major Selection Handling

### **Important Note About Checkboxes:**

When a student selects multiple majors (e.g., "Accounting, Finance, Management"), the Google Form will save them in ONE cell as comma-separated values:

**Example Cell Value:**
```
Accounting, Finance, Management
```

### **Make.com Router Modification Needed:**

Instead of using exact match (`equals`), you'll need to use `contains` in your filters:

**Filter for Accounting emails:**
- Condition: `{{1.3}}` **contains** `Accounting`

**Filter for Finance emails:**
- Condition: `{{1.3}}` **contains** `Finance`

This way, if someone selects both Accounting AND Finance, they'll receive BOTH emails!

### **Alternative: Separate the Majors in Make.com**

Add a "Text Parser" module after Google Sheets:
1. Split the text by delimiter: `, ` (comma + space)
2. This creates an array of majors
3. Add an "Iterator" module to loop through each major
4. Send one email per major selected

**Flow would be:**
```
Google Sheets → Text Parser → Iterator → Router → Send Emails
```

---

## Troubleshooting Common Issues

### **Issue: Form not linked to Make.com**
**Solution:** Ensure the Google Sheet is properly connected in Make.com Module 1

### **Issue: Checkbox data looks messy**
**Solution:** Use "contains" filter instead of "equals" in Make.com router

### **Issue: Students not receiving emails**
**Solution:**
- Check spam folder
- Verify email validation is working
- Check Make.com execution history

### **Issue: Duplicate submissions**
**Solution:** Consider adding response validation or using Google's "Limit to 1 response" per account

---

## Sample Pre-filled Form Link

You can create pre-filled links for specific campaigns:

**Example for Accounting Major:**
1. Fill out the form
2. Click three dots → "Get pre-filled link"
3. Select "Accounting" checkbox
4. Copy link
5. Use for Accounting-specific marketing

**Use cases:**
- Email campaigns targeting specific majors
- Landing pages for major-specific ads
- QR codes at departmental events

---

## Form Maintenance Schedule

### **Weekly:**
- Review new submissions
- Check email delivery success rate
- Monitor for spam submissions

### **Monthly:**
- Export responses for reporting
- Update major descriptions if content changes
- Review and respond to any questions in optional fields

### **Quarterly:**
- Update scholarship amounts
- Refresh ranking information
- Update contact information if changed
- Review and optimize based on analytics

### **Annually:**
- Archive previous year's responses
- Create new spreadsheet for new academic year
- Update program offerings if majors added/removed
- Review entire automation workflow

---

## Sample QR Code Setup

To generate a QR code for print materials:

1. Use [QR Code Generator](https://www.qr-code-generator.com/)
2. Select "URL" type
3. Paste your Google Form link
4. Customize:
   - Add UALR logo in center
   - Use maroon color (#6e2639)
5. Download high-resolution PNG
6. Add to brochures with text: "Scan to Request Program Information"

---

## Compliance & Privacy

### **CAN-SPAM Compliance:**

Ensure all automated emails include:
- ✅ Clear sender identification (UALR School of Business)
- ✅ Accurate subject lines
- ✅ Physical mailing address
- ✅ Unsubscribe mechanism (if sending multiple emails)

### **FERPA & Data Privacy:**

- Store form responses securely
- Only share with authorized admissions staff
- Delete old submissions per university policy
- Don't share student emails with third parties

### **Form Privacy Statement (Optional Addition):**

Add at bottom of form description:
```
Privacy Notice: Your information will only be used to send you program details and
will not be shared with third parties. For questions about our privacy policy,
visit ualr.edu/privacy
```

---

## Quick Reference Summary

| Setting | Value |
|---------|-------|
| **Form Type** | Google Forms |
| **Questions** | 3 Required (Name, Email, Majors) + 3 Optional |
| **Major Selection** | Checkboxes (multiple selection allowed) |
| **Email Validation** | Yes (built-in) |
| **Response Limit** | Unlimited |
| **Confirmation Message** | Custom (see above) |
| **Linked Sheet** | Auto-created + manual "Email Status" column |
| **Theme Color** | #6e2639 (Maroon) |
| **Automation Trigger** | New row in sheet → Make.com |

---

**Ready to create your form?**

1. Go to [forms.google.com](https://forms.google.com)
2. Click "Blank form"
3. Follow this guide step-by-step
4. Test before launching!

**Questions?** Contact UALR IT or Make.com support.

---

**Last Updated:** January 2025
**Version:** 1.0
**Created for:** UA Little Rock School of Business
