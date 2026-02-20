# ML-Based Customer Purchase Prediction System
## Complete Setup Guide with Fictitious Data

---

## 📋 Overview

This demo system uses **Machine Learning** to predict when customers will make their next purchase and automatically sends personalized marketing emails through Make.com automation.

### What's Included:
1. ✅ **Fictitious Customer Data** (30 sample customers)
2. ✅ **ML Prediction API** (Python Flask with scikit-learn)
3. ✅ **Make.com Blueprint** (Automation workflow)
4. ✅ **Complete Setup Instructions**

---

## 🚀 Quick Start Guide

### Step 1: Prepare Your Environment

#### Option A: Local Setup (Recommended for Testing)

1. **Install Python 3.8+**
   - Download from: https://www.python.org/downloads/
   - Verify: `python --version`

2. **Install Dependencies**
   ```bash
   cd Make_project
   pip install -r requirements.txt
   ```

3. **Run the ML API**
   ```bash
   python ml_prediction_api.py
   ```

   You should see:
   ```
   ============================================================
   ML Purchase Prediction API Server
   ============================================================
   Training ML model...
   Model trained successfully!
   Starting server on http://localhost:5000
   ============================================================
   ```

4. **Test the API**
   Open a new terminal and test:
   ```bash
   curl -X POST http://localhost:5000/predict \
   -H "Content-Type: application/json" \
   -d "{\"customer_id\":\"C001\",\"customer_email\":\"test@email.com\",\"customer_name\":\"Test User\",\"days_since_last_purchase\":15,\"total_purchases\":10,\"avg_purchase_amount\":250,\"preferred_category\":\"Electronics\"}"
   ```

#### Option B: Google Colab (Free, No Installation)

1. Upload `ml_prediction_api.py` to Google Colab
2. Install packages:
   ```python
   !pip install flask pandas numpy scikit-learn flask-ngrok
   ```
3. Run the notebook
4. Use ngrok to expose the URL (see below)

---

### Step 2: Expose Your Local API to the Internet

Make.com needs a public URL to call your API. Use **ngrok** (free):

1. **Download ngrok**
   - Visit: https://ngrok.com/download
   - Sign up for free account
   - Download and install

2. **Run ngrok**
   ```bash
   ngrok http 5000
   ```

3. **Copy the Public URL**
   You'll see something like:
   ```
   Forwarding: https://abc123.ngrok-free.app -> http://localhost:5000
   ```

   Copy the `https://abc123.ngrok-free.app` URL - you'll need it for Make.com!

---

### Step 3: Setup Google Sheets

1. **Create a New Google Sheet**
   - Go to: https://sheets.google.com
   - Create new spreadsheet
   - Name it: "Customer Purchase Data"

2. **Add Column Headers** (Row 1):
   ```
   A: customer_id
   B: customer_email
   C: customer_name
   D: purchase_date
   E: product_category
   F: purchase_amount
   G: days_since_last_purchase
   H: total_purchases
   I: avg_purchase_amount
   J: preferred_category
   K: email_sent_date
   L: predicted_purchase_date
   M: email_status
   N: confidence_score
   ```

3. **Import Sample Data**
   - Open `customer_purchase_data.csv`
   - Copy all data
   - Paste into Google Sheet starting at row 2

4. **Get Spreadsheet ID**
   - Look at the URL: `https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID/edit`
   - Copy `YOUR_SPREADSHEET_ID`

---

### Step 4: Configure Make.com

1. **Import Blueprint**
   - Go to: https://www.make.com
   - Login/Signup
   - Click "Scenarios" → "Create a new scenario"
   - Click the "..." menu → "Import Blueprint"
   - Upload: `ML_Customer_Purchase_Prediction.blueprint.json`

2. **Configure Connections**

   **Module 1: Google Sheets (Watch Rows)**
   - Click on the module
   - Add Google connection
   - Replace `YOUR_SPREADSHEET_ID` with your actual ID
   - Select "Sheet1"

   **Module 2: HTTP (Send ML Prediction Request)**
   - Click on the module
   - Replace `YOUR_ML_API_URL` with your ngrok URL
   - Example: `https://abc123.ngrok-free.app/predict`
   - Headers already configured (Content-Type: application/json)

   **Module 5 & 7: Email**
   - Click on email modules
   - Add your email connection (Gmail/SMTP)
   - Customize email content if desired

   **Module 6 & 8: Google Sheets (Update Row)**
   - Replace `YOUR_SPREADSHEET_ID` with your actual ID

3. **Test the Scenario**
   - Click "Run once"
   - Watch the flow execute
   - Check for errors

4. **Schedule the Scenario**
   - Click the clock icon
   - Set schedule (e.g., every 15 minutes, daily, etc.)
   - Turn ON the scenario

---

## 🧪 Testing the Complete System

### Test 1: API Health Check

```bash
curl http://localhost:5000/health
```

Expected Response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2024-10-27T00:00:00"
}
```

### Test 2: Single Customer Prediction

```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "customer_id": "C001",
  "customer_email": "john.smith@email.com",
  "customer_name": "John Smith",
  "days_since_last_purchase": 15,
  "total_purchases": 10,
  "avg_purchase_amount": 250.00,
  "preferred_category": "Electronics"
}'
```

Expected Response:
```json
{
  "customer_id": "C001",
  "customer_email": "john.smith@email.com",
  "customer_name": "John Smith",
  "predicted_days_until_next_purchase": 12,
  "predicted_purchase_date": "2024-11-08",
  "should_send_email": true,
  "confidence_score": 0.8,
  "recommended_products": ["Wireless Headphones", "Smart Watch", "Portable Charger"],
  "email_timing": "send_now",
  "preferred_category": "Electronics",
  "analysis": {
    "days_since_last_purchase": 15,
    "total_purchases": 10,
    "avg_purchase_amount": 250.0,
    "customer_segment": "Regular"
  }
}
```

### Test 3: Batch Prediction

```bash
curl -X POST http://localhost:5000/batch_predict \
-H "Content-Type: application/json" \
-d '{
  "customers": [
    {
      "customer_id": "C001",
      "customer_email": "john@email.com",
      "customer_name": "John",
      "days_since_last_purchase": 15,
      "total_purchases": 10,
      "avg_purchase_amount": 250,
      "preferred_category": "Electronics"
    },
    {
      "customer_id": "C002",
      "customer_email": "sarah@email.com",
      "customer_name": "Sarah",
      "days_since_last_purchase": 7,
      "total_purchases": 15,
      "avg_purchase_amount": 95,
      "preferred_category": "Fashion"
    }
  ]
}'
```

### Test 4: Make.com Integration

1. Add a new row to your Google Sheet with test customer data
2. Wait for Make.com to trigger (or click "Run once")
3. Check your email inbox for the personalized marketing email
4. Verify the Google Sheet was updated with prediction results

---

## 📊 Understanding the ML Model

### How It Works:

1. **Training Data**: The model is trained on historical purchase patterns
   - Days since last purchase
   - Total number of purchases
   - Average purchase amount

2. **Prediction**: Random Forest Regressor predicts:
   - Days until next purchase
   - Confidence score
   - Optimal email timing

3. **Segmentation**: Customers are classified:
   - **VIP**: 20+ purchases, $200+ average
   - **Premium**: 15+ purchases, $150+ average
   - **Regular**: 10+ purchases
   - **Growing**: 5+ purchases
   - **New**: Less than 5 purchases

4. **Email Timing Logic**:
   - **send_now**: Customer likely to purchase very soon
   - **send_soon**: Customer approaching purchase window
   - **wait**: Too early to send email

---

## 🎯 Workflow Diagram

```
┌─────────────────────┐
│  Google Sheets      │
│  (Customer Data)    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Make.com Trigger   │
│  (New/Updated Row)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  HTTP POST Request  │
│  → ML API           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  ML Model Predicts  │
│  Next Purchase      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Parse JSON         │
│  Response           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Router (Condition) │
│  Check email_timing │
└─────┬────────┬──────┘
      │        │
      │        └─────────────┐
      │                      │
      ▼                      ▼
┌──────────────┐    ┌─────────────────┐
│ Send Now     │    │ Send Soon       │
│ (High Prior) │    │ (Medium Prior)  │
└──────┬───────┘    └────────┬────────┘
       │                     │
       ▼                     ▼
┌──────────────────────────────┐
│  Send Personalized Email     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Update Google Sheets        │
│  (Track Email Sent)          │
└──────────────────────────────┘
```

---

## 🔧 Troubleshooting

### Issue 1: API Not Starting
```
Error: Port 5000 already in use
```
**Solution**: Use a different port
```bash
# In ml_prediction_api.py, change:
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue 2: Module Import Error
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Install requirements
```bash
pip install -r requirements.txt
```

### Issue 3: ngrok URL Not Working
```
Failed to connect to ngrok
```
**Solution**:
1. Check if ngrok is running
2. Verify the URL is correct
3. Check firewall settings
4. Try restarting ngrok

### Issue 4: Make.com Connection Failed
```
HTTP 404 or Connection Timeout
```
**Solution**:
1. Verify API is running locally
2. Check ngrok URL is correct and active
3. Test API directly with curl
4. Check ngrok hasn't expired (free tier resets URLs)

### Issue 5: Google Sheets Not Updating
```
No data appears in columns K-N
```
**Solution**:
1. Verify spreadsheet ID is correct
2. Check Google Sheets connection permissions
3. Ensure columns K-N exist
4. Check module mapping configuration

---

## 📈 Customization Options

### 1. Adjust ML Model Thresholds

Edit `ml_prediction_api.py`:

```python
# Change customer segmentation
def get_customer_segment(total_purchases, avg_amount):
    if total_purchases > 30 and avg_amount > 300:  # More strict VIP
        return "VIP"
    # ... customize other segments
```

### 2. Modify Email Templates

Edit the blueprint JSON or directly in Make.com:
- Change email subject lines
- Customize HTML templates
- Add more dynamic content
- Include product images

### 3. Add More Features to ML Model

Edit `ml_prediction_api.py`:

```python
# Add more training features
training_data = {
    'days_since_last': [...],
    'total_purchases': [...],
    'avg_amount': [...],
    'season': [...],  # New feature
    'day_of_week': [...],  # New feature
    'days_until_next': [...]
}
```

### 4. Integrate with Other Services

Add more modules in Make.com:
- **Slack notifications** when high-value customer predicted
- **CRM updates** (Salesforce, HubSpot)
- **SMS marketing** for urgent predictions
- **Google Analytics** event tracking

---

## 🌐 Google Cloud Production Deployment (Optional)

For production use, deploy to Google Cloud:

### Option 1: Google Cloud Run

```bash
# 1. Create Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ml_prediction_api.py .
CMD ["python", "ml_prediction_api.py"]

# 2. Deploy
gcloud run deploy ml-prediction-api \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Option 2: Google Cloud Functions

```bash
# Deploy as serverless function
gcloud functions deploy predict_purchase \
  --runtime python39 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point predict_next_purchase
```

### Option 3: Vertex AI

Use Google's managed ML platform:
1. Upload training data to BigQuery
2. Train AutoML model in Vertex AI
3. Deploy model endpoint
4. Update Make.com to call Vertex AI endpoint

---

## 💰 Cost Estimation

### Free Tier (Demo):
- **ML API**: Free (local/Colab)
- **ngrok**: Free tier (with limitations)
- **Google Sheets**: Free
- **Make.com**: Free tier (1000 operations/month)
- **Total**: $0/month

### Production (Google Cloud):
- **Cloud Run**: ~$5-20/month (depends on traffic)
- **Vertex AI**: ~$50-200/month (depends on predictions)
- **BigQuery**: ~$5-10/month (data storage)
- **Make.com Pro**: $9-29/month
- **Total**: ~$69-259/month

---

## 📚 Additional Resources

- **Make.com Documentation**: https://www.make.com/en/help
- **Flask Documentation**: https://flask.palletsprojects.com/
- **scikit-learn**: https://scikit-learn.org/
- **Google Cloud AI**: https://cloud.google.com/products/ai
- **ngrok Documentation**: https://ngrok.com/docs

---

## 🎓 Learning Path

1. **Beginner**: Use this demo as-is with fictitious data
2. **Intermediate**: Customize email templates and ML thresholds
3. **Advanced**: Replace with real customer data and retrain model
4. **Expert**: Deploy to Google Cloud and integrate with CRM

---

## 📞 Support & Questions

If you encounter issues:
1. Check the troubleshooting section
2. Review API logs for errors
3. Test each component individually
4. Verify all configurations match your setup

---

## ✅ Success Checklist

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] ML API running locally
- [ ] API health check passes
- [ ] ngrok exposing local API
- [ ] Google Sheet created with correct columns
- [ ] Sample data imported
- [ ] Make.com account created
- [ ] Blueprint imported
- [ ] All connections configured
- [ ] Test run successful
- [ ] Email received
- [ ] Google Sheet updated with predictions

---

## 🎉 Congratulations!

You now have a fully functional ML-based customer purchase prediction system with automated marketing emails!

**Next Steps:**
1. Let the system run for a few days
2. Analyze the prediction accuracy
3. Adjust thresholds based on results
4. Scale up with real customer data
5. Deploy to production when ready

---

*Generated for Make.com ML Integration Demo - 2025*
