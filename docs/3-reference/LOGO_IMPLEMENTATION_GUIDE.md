# UALR Logo Implementation Guide

## Official UALR Logo for Email Templates

### 📥 Download the Logo

**Official Logo URL:**
```
https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png
```

**How to Download:**
1. Right-click on the link above
2. Save the image to your computer
3. Upload to a web hosting service or use the direct URL

---

## Method 1: Use Direct URL (Quickest)

You can use the official UALR logo URL directly in your email templates.

### Update Each Email Template:

**Find this section in each email module:**
```html
<div class="header">
    <div class="logo">UA LITTLE ROCK</div>
    <div class="logo-subtitle">SCHOOL OF BUSINESS</div>
</div>
```

**Replace with:**
```html
<div class="header">
    <img src="https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png"
         alt="UA Little Rock Logo"
         style="max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;">
    <div class="logo-subtitle">SCHOOL OF BUSINESS</div>
</div>
```

**Adjust the header CSS by adding:**
```css
.header {
    background: #6e2639;
    padding: 25px;
    text-align: center;
}
.header img {
    max-width: 200px;
    height: auto;
    display: block;
    margin: 0 auto 10px auto;
}
```

---

## Method 2: Upload to Your Own Server (Recommended)

For better control and reliability:

### Step 1: Download the Logo
1. Go to: https://ualr.edu/communications/logos-and-wordmarks/
2. Right-click the vertical RGB logo
3. Save as: `ualr-logo.png`

### Step 2: Upload to Your Server
Upload the logo to:
- Your website's image folder
- Google Drive (make publicly viewable)
- Dropbox (get public link)
- Make.com file storage
- AWS S3, Cloudinary, or other CDN

### Step 3: Get the Public URL
Example URLs:
- Your server: `https://yourschool.edu/images/ualr-logo.png`
- Google Drive: `https://drive.google.com/uc?id=YOUR_FILE_ID`
- Dropbox: `https://dl.dropboxusercontent.com/YOUR_PATH/ualr-logo.png`

### Step 4: Update Email Templates
Replace the text logo with:
```html
<img src="YOUR_LOGO_URL_HERE"
     alt="UA Little Rock Logo"
     style="max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;">
```

---

## Method 3: Base64 Embedded (Most Reliable)

For 100% reliability across all email clients:

### Convert Logo to Base64:
1. Download the logo
2. Go to https://www.base64-image.de/
3. Upload your logo image
4. Copy the base64 string
5. Use in email template:

```html
<img src="data:image/png;base64,YOUR_BASE64_STRING_HERE"
     alt="UA Little Rock Logo"
     style="max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;">
```

**Note:** Base64 increases email size but guarantees the logo displays.

---

## Complete Updated Header HTML

### With Logo Image:

```html
<div class="header" style="background: #6e2639; padding: 25px; text-align: center;">
    <img src="https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png"
         alt="UA Little Rock Logo"
         style="max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;">
    <div style="color: #ffbf00; font-size: 13px; margin-top: 5px; letter-spacing: 1.5px; font-weight: 600;">
        SCHOOL OF BUSINESS
    </div>
</div>
```

---

## How to Update All 8 Email Templates in Make.com

### Quick Update Process:

1. **Open your Make.com scenario**

2. **For EACH of the 8 email modules** (Accounting, Business Analytics, BIS, Economics, Finance, International Business, Management, Marketing):

   **A. Click the email module**

   **B. Find the HTML content field**

   **C. Search for (Ctrl+F):**
   ```html
   <div class="header">
       <div class="logo">UA LITTLE ROCK</div>
   ```

   **D. Replace with:**
   ```html
   <div class="header">
       <img src="https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png"
            alt="UA Little Rock Logo"
            style="max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;">
   ```

   **E. Click OK to save**

3. **Test the scenario** with a sample form submission

4. **Verify the logo displays** in the received email

---

## Logo Sizing Guidelines

### Recommended Sizes:

**Email Header:**
- Width: 180-220px (optimal for mobile)
- Max width: 250px
- Height: Auto (maintains aspect ratio)

**Email Footer (if you want to add a small logo):**
- Width: 80-100px
- Max width: 120px

### CSS for Responsive Logo:

```css
.header img {
    max-width: 200px;
    width: 100%;
    height: auto;
    display: block;
    margin: 0 auto 10px auto;
}

@media only screen and (max-width: 480px) {
    .header img {
        max-width: 150px;
    }
}
```

---

## Alternative: Text Logo with Background Image

If you prefer the text logo but want to add a subtle background:

```html
<div class="header" style="background: #6e2639 url('LOGO_URL') no-repeat center top; background-size: 80px auto; padding-top: 100px;">
    <div class="logo">UA LITTLE ROCK</div>
    <div class="logo-subtitle">SCHOOL OF BUSINESS</div>
</div>
```

---

## Testing Checklist

After adding the logo, test on:

- [ ] Gmail (Desktop)
- [ ] Gmail (Mobile App)
- [ ] Outlook (Desktop)
- [ ] Outlook (Web)
- [ ] Apple Mail (iPhone)
- [ ] Apple Mail (Mac)
- [ ] Yahoo Mail
- [ ] AOL Mail

**Common Issues:**

1. **Logo doesn't display in Gmail:**
   - Use direct URL or base64
   - Ensure URL is https://

2. **Logo too large on mobile:**
   - Reduce max-width to 180px
   - Add mobile media query

3. **Logo blocked by email client:**
   - Base64 embedding prevents this
   - Or use trusted domain

---

## Brand Compliance

Per UALR Brand Guidelines:

✅ **DO:**
- Use official logo files
- Maintain aspect ratio
- Use on maroon (#6e2639) or white background
- Keep clear space around logo

❌ **DON'T:**
- Distort or stretch logo
- Change logo colors
- Add effects or filters
- Use old or unofficial logos

---

## Quick Reference

| Method | Reliability | Setup Time | Best For |
|--------|------------|------------|----------|
| **Direct URL** | Good | 1 min | Quick deployment |
| **Your Server** | Excellent | 10 min | Long-term use |
| **Base64** | Perfect | 15 min | Maximum compatibility |

---

## Sample: Complete Email with Logo

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    .header {
        background: #6e2639;
        padding: 25px;
        text-align: center;
    }
    .header img {
        max-width: 200px;
        height: auto;
        display: block;
        margin: 0 auto 10px auto;
    }
    .logo-subtitle {
        color: #ffbf00;
        font-size: 13px;
        margin-top: 10px;
        letter-spacing: 1.5px;
        font-weight: 600;
    }
</style>
</head>
<body>
<div class="header">
    <img src="https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png"
         alt="UA Little Rock Logo">
    <div class="logo-subtitle">SCHOOL OF BUSINESS</div>
</div>
<!-- Rest of email content -->
</body>
</html>
```

---

## Need Help?

If the logo doesn't display or you encounter issues:

1. Check that the URL is accessible (open in browser)
2. Verify https:// protocol is used
3. Test with base64 embedding
4. Contact UALR Communications for alternative logo files
5. Check Make.com community forums for email image issues

---

**Official Logo Source:** https://ualr.edu/communications/logos-and-wordmarks/
**Brand Guidelines:** https://ualr.edu/communications/

**Last Updated:** January 2025
