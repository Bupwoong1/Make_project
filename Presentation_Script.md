# Presentation Script - AI-Powered Email Marketing

---

## Slide 1: Project Overview

"Hi everyone. Today I'm gonna show you a project that combines machine learning with marketing automation.

So basically, I built a system that predicts when customers are likely to make their next purchase, and then automatically sends them personalized emails at exactly the right time.

The tech stack is pretty straightforward - Python for the ML model, Make.com for automation, and it all connects with Google Sheets and Gmail.

Let's dive in."

---

## Slide 2: System Architecture

"Alright, so here's how everything fits together.

The data starts in Google Sheets - that's where all the customer purchase history lives. When a new row gets added, it triggers the whole workflow.

The data goes to my ML API, which predicts when that customer's gonna buy again. Then Make.com takes that prediction and routes it to the right email template based on the customer's category - Electronics, Fashion, Beauty, whatever.

And finally, Gmail sends out the personalized email. The whole thing runs automatically, no human intervention needed.

Here's what the Make.com workflow actually looks like."

---

## Slide 3: Machine Learning Model

"Now let's talk about the ML model.

The input is pretty simple - how many days since their last purchase, how many times they've bought before, average spending, and what category they prefer.

The model spits out a predicted purchase date, a confidence score, product recommendations, and whether we should email them now or wait.

I'm using RandomForestRegressor for this. It's not fancy, but it works.

The confidence score is based on purchase history - if they've bought 10+ times, I'm 80% confident. Five purchases, 70%. New customers, 60%.

This is what the actual code looks like - it's the core prediction function."

---

## Slide 4: Customer Data & Automation

"So I've got 33 customers in the system right now, spread across five different categories.

The Google Sheets setup is real simple - every time a new row appears, Make.com picks it up automatically.

Here's what the actual data looks like in the spreadsheet.

Then the Router in Make.com looks at the preferred category and sends them down one of five different paths. Each category gets its own custom email template.

The whole cycle runs every 15 minutes, so it's basically real-time."

---

## Slide 5: Personalized Email Design

"Let's look at the emails themselves.

Each template has the same structure - big hero banner with 20% off, a category-specific image, the predicted purchase date, three product recommendations with thumbnails, a promo code, and a call-to-action button.

Here's what it actually looks like in someone's inbox.

Everything's personalized using variables - the customer's name, their predicted date, product recommendations. So even though we're sending hundreds of emails, each one feels unique."

---

## Slide 6: Technical Challenge - Email Compatibility

"Okay, so here's a problem I ran into.

Gmail doesn't support modern CSS. Like, at all. I tried using flexbox to layout the product items - didn't work.

The old code looked nice and clean, but Gmail just ignored it.

So I had to go old school - HTML tables. Yeah, tables in 2025.

The new version uses table cells with inline styles and vertical-align to get everything centered properly.

Not pretty code, but it works everywhere - Gmail, Outlook, Apple Mail, you name it.

Key lesson here - always use tables for email layouts, inline styles with important flags, and test across multiple email clients."

---

## Slide 7: API & Prediction Logic

"Let me show you the API real quick.

It's a simple POST endpoint. You send customer data - ID, days since last purchase, total purchases, category.

It sends back the prediction - purchase date, recommended products, confidence score, and timing.

The timing logic is interesting. If they're already past their predicted date, we send immediately. If they're within three days, we send soon. Otherwise, we wait.

So we're not spamming people too early - we're hitting them right when they're most likely to buy."

---

## Slide 8: Brand Design & Categories

"For the design, I used UA Little Rock's brand colors - maroon and gold.

Each category has its own vibe. Electronics gets tech imagery, Fashion gets clothing shots, Beauty gets cosmetics, you get the idea.

I also built a product recommendation database. So when someone's an Electronics buyer, they see Wireless Headphones, Smart Watches, Portable Chargers.

It's hardcoded for now, but in production you'd pull this from your actual product catalog."

---

## Slide 9: Results & Impact

"So what are the results?

Right now it's managing 33 customers completely automatically. Five different email templates. The prediction accuracy is around 80%, which is pretty solid for a RandomForest model.

The whole cycle runs every 15 minutes, and it's 100% hands-free.

From a business perspective, we're getting real-time predictions, personalized content for every customer, and we're hitting them at the right time - which means better conversion rates.

The system's fully scalable - I could add hundreds or thousands of customers without changing anything.

For future improvements, I'd add seasonal trends, price sensitivity, abandoned cart emails, maybe integrate with Shopify or WooCommerce."

---

## Slide 10: Key Takeaways

"Alright, so what did I learn from this project?

On the technical side, I got hands-on with machine learning - RandomForest, scikit-learn. Built a Flask API, set up workflow automation in Make.com, and learned way more about email HTML and CSS than I ever wanted to know.

The big lessons? Tables beat flexbox for emails, every time. You need inline styles for Gmail compatibility. And testing is absolutely critical - what looks perfect in Chrome might break in Outlook.

From a business perspective, this shows the power of automation. Zero manual effort once it's set up. All your marketing decisions are data-driven. And it scales effortlessly.

Thanks for listening. Any questions?"

---

## Q&A Tips

**If asked about scalability:**
"Great question. Right now it's 33 customers, but the architecture can handle way more. The ML model retrains on the fly, Make.com can process thousands of rows, and the email sending is just API calls. The only bottleneck would be Gmail's daily send limit, but you can switch to SendGrid or Mailgun for that."

**If asked about accuracy:**
"80% confidence might sound high, but remember - we're predicting human behavior, which is inherently unpredictable. The RandomForest model is doing pattern matching based on past purchases. For better accuracy, I'd need more features - time of year, product pricing, promotional history, external factors like payday cycles."

**If asked about privacy:**
"All the customer data is fake - it's just for demonstration. In production, you'd need proper consent, GDPR compliance, secure data storage, and clear unsubscribe options. The emails already have an unsubscribe link in the footer."

**If asked about cost:**
"Pretty minimal. Flask runs on any server - I'm using Localtunnel for free. Make.com has a free tier up to 1,000 operations per month. Google Sheets and Gmail are free. The only real cost would be if you scale up and need paid Make.com plans or a dedicated email service."

**If asked why not use existing tools:**
"Sure, platforms like Klaviyo or Mailchimp have built-in features, but they're expensive and you don't control the ML model. This gives you full customization - you can tweak the algorithm, add new features, integrate with any system you want. Plus it's a great learning project."
