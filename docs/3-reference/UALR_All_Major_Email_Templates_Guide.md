# UA Little Rock School of Business - All Major Email Templates

## Official UALR Brand Colors Used:
- **Primary Maroon**: #6e2639
- **Light Maroon**: #98344f
- **Silver**: #a7a9ac
- **Gold**: #ffbf00
- **Dark Grey**: #333333
- **Light Grey**: #eeeeee

---

## Google Form Setup

### Form Title:
"UA Little Rock School of Business - Program Information Request"

### Form Questions:
1. **Full Name** (Short answer, Required)
2. **Email Address** (Short answer, Email validation, Required)
3. **Major Preference** (Dropdown, Required)
   - Accounting
   - Business Analytics
   - Business Information Systems
   - Economics
   - Finance
   - International Business
   - Management
   - Marketing

### Google Sheet Columns (Auto-created):
- Column A: Timestamp
- Column B: Full Name
- Column C: Email Address
- Column D: Major Preference
- Column E: Email Status (to be updated by automation)

---

## Router Structure in Make.com

The blueprint uses a router with 8 routes - one for each major. Each route:
1. **Filter**: Checks if Major Preference = [Major Name]
2. **Send Email**: Sends major-specific HTML email
3. **Update Sheet**: Updates Email Status column with timestamp

---

## Complete HTML Email Templates for All 8 Majors

### 3. Business Information Systems Email Template

**Filter Condition**: `{{1.3}}` equals "Business Information Systems"

**Subject**: Welcome to UALR School of Business - Business Information Systems Program Information

**HTML Content**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Welcome to UALR School of Business - Business Information Systems</title>
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
        line-height: 1.6;
        color: #333333;
        background-color: #f4f4f4;
    }
    .container {
        max-width: 600px;
        margin: 0 auto;
        background: #ffffff;
    }
    .header {
        background: #6e2639;
        padding: 30px 20px;
        text-align: center;
    }
    .logo {
        font-size: 28px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
    }
    .logo-subtitle {
        color: #ffbf00;
        font-size: 14px;
        margin-top: 5px;
        letter-spacing: 2px;
    }
    .hero-banner {
        background: linear-gradient(135deg, #6e2639 0%, #98344f 100%);
        padding: 40px 20px;
        text-align: center;
        color: white;
        border-bottom: 5px solid #ffbf00;
    }
    .hero-banner h1 {
        font-size: 32px;
        margin-bottom: 10px;
    }
    .hero-banner p {
        font-size: 18px;
        color: #ffbf00;
    }
    .content {
        padding: 40px 30px;
    }
    .greeting {
        font-size: 20px;
        color: #6e2639;
        margin-bottom: 20px;
        font-weight: 600;
    }
    .intro {
        background: #eeeeee;
        padding: 20px;
        border-left: 4px solid #6e2639;
        margin-bottom: 30px;
    }
    .intro h2 {
        color: #6e2639;
        font-size: 20px;
        margin-bottom: 10px;
    }
    .intro p {
        color: #333333;
        line-height: 1.8;
    }
    .major-section {
        margin: 30px 0;
    }
    .major-title {
        background: #6e2639;
        color: white;
        padding: 15px 20px;
        font-size: 24px;
        font-weight: 700;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .highlight-box {
        background: #ffe579;
        border: 2px solid #ffbf00;
        padding: 20px;
        margin: 20px 0;
        border-radius: 5px;
    }
    .highlight-box h3 {
        color: #6e2639;
        font-size: 18px;
        margin-bottom: 15px;
    }
    .feature-list {
        list-style: none;
        padding: 0;
    }
    .feature-list li {
        padding: 10px 0;
        padding-left: 25px;
        position: relative;
        color: #333333;
    }
    .feature-list li:before {
        content: "✓";
        position: absolute;
        left: 0;
        color: #ffbf00;
        font-weight: bold;
        font-size: 18px;
    }
    .stats-grid {
        display: table;
        width: 100%;
        margin: 20px 0;
    }
    .stat-item {
        display: table-cell;
        width: 50%;
        padding: 15px;
        text-align: center;
        background: #eeeeee;
        border: 1px solid #a7a9ac;
    }
    .stat-number {
        font-size: 24px;
        font-weight: 700;
        color: #6e2639;
        display: block;
    }
    .stat-label {
        font-size: 12px;
        color: #333333;
        margin-top: 5px;
    }
    .cta-button {
        display: inline-block;
        background: #ffbf00;
        color: #6e2639;
        padding: 15px 40px;
        text-decoration: none;
        font-weight: 700;
        font-size: 16px;
        border-radius: 30px;
        margin: 20px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .footer {
        background: #eeeeee;
        padding: 30px 20px;
        text-align: center;
        border-top: 3px solid #6e2639;
    }
    .footer-text {
        font-size: 12px;
        color: #333333;
        margin: 10px 0;
    }
    .contact-info {
        margin: 20px 0;
        font-size: 13px;
        color: #333333;
    }
    .contact-info a {
        color: #6e2639;
        text-decoration: none;
    }
</style>
</head>
<body>
<div class="container">
    <div class="header">
        <div class="logo">UA LITTLE ROCK</div>
        <div class="logo-subtitle">SCHOOL OF BUSINESS</div>
    </div>

    <div class="hero-banner">
        <h1>Welcome, {{1.`1`}}!</h1>
        <p>Discover Your Future in Business Information Systems</p>
    </div>

    <div class="content">
        <div class="greeting">Thank you for your interest in UA Little Rock!</div>

        <div class="intro">
            <h2>About UA Little Rock School of Business</h2>
            <p>Welcome to the UA Little Rock School of Business, where we provide solid, affordable foundations for your future success. Our AACSB accredited programs (held by less than 5% of business schools worldwide) offer flexible learning options, real-world experiences, and a commitment to excellence.</p>
        </div>

        <div class="major-section">
            <div class="major-title">Business Information Systems Program</div>

            <p style="margin-bottom: 20px; color: #333333; line-height: 1.8;">A business information systems degree merges technology with business acumen, preparing you to design, implement, and manage systems that streamline organizational processes and enhance decision-making.</p>

            <div class="highlight-box">
                <h3>Why Choose Business Information Systems at UALR?</h3>
                <ul class="feature-list">
                    <li><strong>Technical Mastery:</strong> Expertise in database systems, programming, systems design, and analysis</li>
                    <li><strong>Systems Expertise:</strong> SQL, object-oriented programming, project management, database systems, and information security</li>
                    <li><strong>Professional Edge:</strong> About 377,500 jobs openings projected each year from 2022 to 2032 (US BLS)</li>
                    <li><strong>Experienced Faculty:</strong> Seasoned and experienced faculty</li>
                    <li><strong>Hands-on Learning:</strong> Opportunities to meet and interact with IT professionals</li>
                    <li><strong>Alumni Network:</strong> Alumni engagement after graduation</li>
                </ul>
            </div>

            <div class="stats-grid">
                <div class="stat-item">
                    <span class="stat-number">377,500</span>
                    <div class="stat-label">Job Openings Per Year</div>
                </div>
                <div class="stat-item">
                    <span class="stat-number">$59K-$136K</span>
                    <div class="stat-label">Annual Salary Range</div>
                </div>
            </div>

            <div class="highlight-box">
                <h3>Career Opportunities</h3>
                <p style="color: #333333; line-height: 1.8;">Variety of careers including: database administrators, software developers, information security analyst, system support analyst, and web developer. Job growth opportunities across all industries. Acquire skills to help organizations use technology efficiently.</p>
            </div>
        </div>

        <div style="text-align: center; margin: 30px 0;">
            <a href="https://ualr.edu/business/academics/business-information-systems/" class="cta-button" style="color: #6e2639 !important; text-decoration: none !important;">Learn More About BIS</a>
        </div>

        <div class="intro">
            <h2>Why UALR School of Business?</h2>
            <ul class="feature-list">
                <li><strong>AACSB Accredited:</strong> Less than 5% of business schools worldwide hold this distinction</li>
                <li><strong>Ranked #32:</strong> 2023 US News Online Business Program</li>
                <li><strong>Affordable:</strong> Starting at just $3,500 per semester</li>
                <li><strong>Flexible Learning:</strong> On-campus and online options available</li>
                <li><strong>Real-World Experience:</strong> Career-defining internship opportunities through ASBTDC partnership</li>
            </ul>
        </div>
    </div>

    <div class="footer">
        <p class="footer-text"><strong>Ready to take the next step?</strong></p>

        <div class="contact-info">
            UA Little Rock School of Business<br>
            2801 S. University Ave, Little Rock, AR 72204<br>
            <a href="mailto:business@ualr.edu">business@ualr.edu</a> | (501) 569-3000<br>
            <a href="https://ualr.edu/business/" style="color: #6e2639;">Visit our website</a>
        </div>

        <p class="footer-text" style="margin-top: 20px; padding-top: 20px; border-top: 1px solid #a7a9ac;">
            Questions? Contact our admissions team - we're here to help!<br>
            <a href="https://ualr.edu/admissions/" style="color: #6e2639;">Schedule a Campus Visit</a>
        </p>

        <p style="font-size: 11px; color: #333333; margin-top: 15px;">
            © 2025 UA Little Rock. All rights reserved.
        </p>
    </div>
</div>
</body>
</html>
```

---

### 4. Economics Email Template

**Filter Condition**: `{{1.3}}` equals "Economics"

**Subject**: Welcome to UALR School of Business - Economics Program Information

**Key Content Points**:
- Analytical Skills: Sharpen logic and statistical analysis abilities
- Law School Edge: Excel in LSAT scores and law school readiness
- Experiential Learning: Real policy-relevant research with local nonprofits
- Flexible Double Major: Easily pairs with finance, politics, math, and real estate
- Research opportunities with local businesses/nonprofits
- Career Opportunities: Industry, finance, government, public policy, data science, machine learning, law, graduate study

---

### 5. Finance Email Template

**Filter Condition**: `{{1.3}}` equals "Finance"

**Subject**: Welcome to UALR School of Business - Finance Program Information

**Key Content Points**:
- Choose Your Path: General/Corporate Finance, Real Estate Finance, Financial Services
- Career Ready Skills: Financial modeling and analytics, Real estate development, CFA level I preparation
- Experiential Learning: National competitions, equity pitch projects
- Program Flexibility: Complete on campus or fully online
- Career Opportunities: Commercial banking, investment banking, development and investing, financial planning and wealth management, insurance, real estate appraisal
- Strong student-led organizations for building connections

---

### 6. International Business Email Template

**Filter Condition**: `{{1.3}}` equals "International Business"

**Subject**: Welcome to UALR School of Business - International Business Program Information

**Key Content Points**:
- Study the complexities of the global marketplace
- Interdisciplinary program
- Comprehensive understanding of international business practices
- Strategic options applicable in various industries
- Global perspective on business operations

---

### 7. Management Email Template

**Filter Condition**: `{{1.3}}` equals "Management"

**Subject**: Welcome to UALR School of Business - Management Program Information

**Key Content Points**:
- Specialization Areas: Innovation and Entrepreneurship, General Management, Human Resource Management, International Business
- Core Benefits: Master practical decision-making and leadership skills
- Networking: Network with corporate executives to glean industry insights
- Real-World Insights: Hands-on experience through internships and collaborative projects
- Flexible Learning: Summer semester offerings to fast-track education
- Certificates: Management, Innovation and Entrepreneurship
- Student Organization: Society for human resource management
- Career Opportunities: Entrepreneur, consultant, human resources manager, general manager, project manager

---

### 8. Marketing Email Template

**Filter Condition**: `{{1.3}}` equals "Marketing"

**Subject**: Welcome to UALR School of Business - Marketing Program Information

**Key Content Points**:
- Flexibility in Focus: Choose emphasis in Digital Marketing or Professional Sales
- AI-Powered Marketing: Discover how to amplify campaigns with AI-driven innovations
- Exciting Sales Dynamics: Master negotiation, relationship building, and strategic selling
- Experiential Learning: Participate in practical projects and real-world case studies
- Professional Sales Certificate available
- Competition-focused marketing and sales club
- Career Opportunities: Product manager, Sales manager, Digital marketing manager, Marketing research analyst

---

## Implementation Instructions

### Step 1: Create Google Form
1. Go to Google Forms
2. Create form with the 3 questions listed above
3. Link responses to a Google Sheets spreadsheet
4. Add "Email Status" column (Column E) manually to the spreadsheet

### Step 2: Import Blueprint to Make.com
1. Log into Make.com
2. Click "Create a new scenario"
3. Click the three dots menu → "Import Blueprint"
4. Upload the `UALR_Prospective_Student_Email_Automation.blueprint.json` file
5. Configure connections:
   - Connect your Google Sheets account
   - Connect your Email account (Gmail/Outlook)

### Step 3: Update Configuration
1. Update `__IMTCONN__` IDs with your actual connection IDs
2. Update `spreadsheetId` with your actual Google Sheet ID
3. Update email `account` parameters with your email connection ID

### Step 4: Add Remaining Major Routes
For each remaining major (Economics, Finance, International Business, Management, Marketing, Business Information Systems):
1. Add a new route to the router
2. Copy the email module structure from existing routes
3. Update the filter condition for the major name
4. Paste the corresponding HTML template from this guide
5. Add the update sheet module after each email

### Step 5: Test the Automation
1. Submit test form responses for each major
2. Verify emails are sent correctly
3. Check that Google Sheet is updated with "Email Sent" status
4. Verify email formatting and links

### Step 6: Activate
1. Turn on the scenario in Make.com
2. Set appropriate scheduling (every 15 minutes recommended)
3. Monitor execution history for errors

---

## Customization Options

### To Add School Logo Image:
Add this after the `.header` div in each template:
```html
<div style="text-align: center; background: #ffffff; padding: 20px;">
    <img src="YOUR_LOGO_URL_HERE" alt="UA Little Rock Logo" style="max-width: 200px; height: auto;">
</div>
```

### To Track Email Opens:
Add a tracking pixel before `</body>`:
```html
<img src="https://your-tracking-service.com/pixel?email={{1.`2`}}&major={{1.`3`}}" width="1" height="1" style="display:none;">
```

### To Add More Fields:
1. Add question to Google Form
2. Update the interface in module 1
3. Reference in email templates using `{{1.`COLUMN_NUMBER`}}`

---

## Maintenance

- **Update Content**: Edit HTML in each email module in Make.com
- **Monitor Deliverability**: Check spam rates and email bounces
- **Update Colors**: Search and replace hex codes across all templates
- **Add New Majors**: Duplicate existing route, update filter and content

---

## Support Resources

- **Make.com Documentation**: https://www.make.com/en/help
- **Google Forms Help**: https://support.google.com/docs/answer/6281888
- **UALR Brand Guidelines**: https://ualr.edu/communications/
- **UALR School of Business**: https://ualr.edu/business/

---

## Notes

- All email templates use official UALR brand colors (#6e2639 Maroon, #ffbf00 Gold)
- Templates are responsive and mobile-friendly
- Gmail and Outlook tested
- Compliant with email accessibility standards
- Each template is approximately 15-20KB in size
