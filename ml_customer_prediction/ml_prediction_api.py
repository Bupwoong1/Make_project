"""
ML-Based Customer Purchase Prediction API
Uses simple ML model to predict next purchase timing
For Make.com integration demo
"""

from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

app = Flask(__name__)

# Initialize ML model (in production, load pre-trained model)
model = None

def train_simple_model():
    """
    Train a simple ML model on fictitious data
    Predicts days until next purchase based on customer behavior
    """
    # Training data (fictitious historical patterns)
    training_data = {
        'days_since_last': [5, 10, 15, 20, 30, 45, 60, 7, 14, 21, 28, 35, 50, 3, 8, 12, 25, 40, 55, 70],
        'total_purchases': [20, 15, 10, 8, 6, 5, 4, 18, 12, 10, 9, 7, 5, 25, 22, 16, 11, 8, 6, 3],
        'avg_amount': [100, 150, 200, 250, 300, 350, 400, 120, 180, 220, 280, 320, 380, 90, 110, 160, 240, 310, 370, 420],
        'days_until_next': [7, 10, 14, 18, 25, 35, 45, 8, 12, 16, 20, 28, 38, 5, 9, 13, 22, 32, 42, 50]
    }

    df = pd.DataFrame(training_data)
    X = df[['days_since_last', 'total_purchases', 'avg_amount']]
    y = df['days_until_next']

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model

# Train model on startup
print("Training ML model...")
model = train_simple_model()
print("Model trained successfully!")

@app.route('/', methods=['GET'])
def root():
    """Root endpoint"""
    return jsonify({
        'message': 'ML Purchase Prediction API',
        'version': '1.0',
        'endpoints': {
            'health': '/health',
            'predict': '/predict (POST)',
            'batch_predict': '/batch_predict (POST)'
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/predict', methods=['POST'])
def predict_next_purchase():
    """
    Predict next purchase timing for a customer

    Expected JSON payload:
    {
        "customer_id": "C001",
        "customer_email": "customer@email.com",
        "customer_name": "John Doe",
        "days_since_last_purchase": 15,
        "total_purchases": 10,
        "avg_purchase_amount": 250.00,
        "preferred_category": "Electronics"
    }

    Returns:
    {
        "customer_id": "C001",
        "customer_email": "customer@email.com",
        "predicted_days_until_next_purchase": 12,
        "predicted_purchase_date": "2024-11-08",
        "should_send_email": true,
        "confidence_score": 0.85,
        "recommended_products": ["Product A", "Product B"],
        "email_timing": "send_now"
    }
    """
    try:
        data = request.json

        # Extract features
        days_since = data.get('days_since_last_purchase', 0)
        total_purchases = data.get('total_purchases', 0)
        avg_amount = data.get('avg_purchase_amount', 0)
        customer_email = data.get('customer_email', '')
        customer_name = data.get('customer_name', '')
        customer_id = data.get('customer_id', '')
        preferred_category = data.get('preferred_category', 'General')

        # Prepare features for prediction
        features = np.array([[days_since, total_purchases, avg_amount]])

        # Make prediction
        predicted_days = int(model.predict(features)[0])

        # Calculate predicted purchase date
        predicted_date = (datetime.now() + timedelta(days=predicted_days)).strftime('%Y-%m-%d')

        # Determine if email should be sent (if predicted purchase is within 7 days)
        should_send_email = days_since >= (predicted_days - 3)

        # Calculate confidence score (simplified)
        if total_purchases > 15:
            confidence = 0.9
        elif total_purchases > 10:
            confidence = 0.8
        elif total_purchases > 5:
            confidence = 0.7
        else:
            confidence = 0.6

        # Determine email timing
        if days_since >= predicted_days:
            email_timing = "send_now"
        elif days_since >= (predicted_days - 3):
            email_timing = "send_soon"
        else:
            email_timing = "wait"

        # Recommend products based on category
        category_recommendations = {
            'Electronics': ['Wireless Headphones', 'Smart Watch', 'Portable Charger'],
            'Fashion': ['Summer Collection', 'Designer Handbag', 'Premium Sneakers'],
            'Beauty': ['Anti-Aging Serum', 'Luxury Skincare Set', 'Organic Face Mask'],
            'Home & Garden': ['Smart Home Device', 'Garden Tool Set', 'Decorative Plants'],
            'Sports': ['Fitness Tracker', 'Yoga Mat', 'Protein Supplements']
        }

        recommended_products = category_recommendations.get(preferred_category, ['Special Offer Items'])

        # Prepare response
        response = {
            'customer_id': customer_id,
            'customer_email': customer_email,
            'customer_name': customer_name,
            'predicted_days_until_next_purchase': predicted_days,
            'predicted_purchase_date': predicted_date,
            'should_send_email': should_send_email,
            'confidence_score': confidence,
            'recommended_products': recommended_products,
            'email_timing': email_timing,
            'preferred_category': preferred_category,
            'analysis': {
                'days_since_last_purchase': days_since,
                'total_purchases': total_purchases,
                'avg_purchase_amount': avg_amount,
                'customer_segment': get_customer_segment(total_purchases, avg_amount)
            }
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Error processing prediction request'
        }), 400

def get_customer_segment(total_purchases, avg_amount):
    """Determine customer segment based on behavior"""
    if total_purchases > 20 and avg_amount > 200:
        return "VIP"
    elif total_purchases > 15 and avg_amount > 150:
        return "Premium"
    elif total_purchases > 10:
        return "Regular"
    elif total_purchases > 5:
        return "Growing"
    else:
        return "New"

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    """
    Process multiple customers at once

    Expected JSON payload:
    {
        "customers": [
            {customer_data_1},
            {customer_data_2},
            ...
        ]
    }
    """
    try:
        data = request.json
        customers = data.get('customers', [])

        results = []
        for customer in customers:
            # Create a mock request for each customer
            with app.test_request_context(json=customer):
                response = predict_next_purchase()
                if response.status_code == 200:
                    results.append(response.json)

        return jsonify({
            'total_customers': len(customers),
            'predictions': results,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Error processing batch prediction'
        }), 400

if __name__ == '__main__':
    print("="*60)
    print("ML Purchase Prediction API Server")
    print("="*60)
    print("Endpoints:")
    print("  GET  /health          - Health check")
    print("  POST /predict         - Single customer prediction")
    print("  POST /batch_predict   - Multiple customer predictions")
    print("="*60)
    print("\nStarting server on http://localhost:8080")
    print("Use ngrok to create public URL for Make.com integration")
    print("Example: ngrok http 8080")
    print("="*60)

    app.run(debug=False, host='127.0.0.1', port=8080)
