# ML Prediction API Development Rules

## Location
All ML API code lives in `ml_customer_prediction/`.

## Package Manager
- Use `pip` with `requirements.txt`. Run from sub-project directory:
```bash
cd ml_customer_prediction
pip install -r requirements.txt
```

## Running the API
```bash
cd ml_customer_prediction
python ml_prediction_api.py
# Server starts on http://localhost:8080
# For Make.com integration: ngrok http 8080
```

## Coding Style
- Synchronous functions (Flask, not async)
- Keep each function short and modular
- Follow standard Python conventions (PEP 8)
- ALL Flask API code in `ml_customer_prediction/ml_prediction_api.py` (single-file architecture)

## Key Dependencies
| Package | Purpose |
|---------|---------|
| Flask | REST API framework |
| pandas | Data manipulation |
| numpy | Numerical operations |
| scikit-learn | ML model (RandomForestRegressor) |
| Werkzeug | WSGI utilities (Flask dependency) |

## API Endpoints
| Endpoint | Method | Purpose |
|----------|--------|---------|
| / | GET | Root info |
| /health | GET | Health check |
| /predict | POST | Single customer prediction |
| /batch_predict | POST | Batch predictions |

## Testing
- Test with curl or Python requests library
- Sample request: `ml_customer_prediction/test_request.json`
- Sample data: `ml_customer_prediction/customer_purchase_data.csv`
- Test server: `ml_customer_prediction/test_api.py` (minimal Flask health check)
- No unit test framework unless explicitly requested

## ngrok Integration
- The API must be exposed via ngrok for Make.com to reach it
- Default port: 8080
- ngrok command: `ngrok http 8080`
- Update Make.com HTTP module URL when ngrok URL changes
