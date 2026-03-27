# ⚡ Quick Start Guide

Get the phishing detector running in **2 minutes**!

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## 1. Install Dependencies
```bash
pip install -r requirements.txt
```

## 2. Train the Model
```bash
python train_model.py
```
This creates the trained models in the `models/` folder.

## 3. Choose Your Interface

### Option A: Web Interface (Recommended)
```bash
python app.py
```
- Opens at: **http://127.0.0.1:5000**
- Beautiful UI with 3 tabs
- Paste email text and get instant results

### Option B: Command-Line Interface
```bash
python cli.py
```
- Interactive terminal interface
- Type or paste emails for analysis
- Compare different models side-by-side

### Option C: Python Code
```python
from detector import PhishingDetector

detector = PhishingDetector()
result = detector.predict("Your email text here")

print(result['prediction'])      # 'phishing' or 'legitimate'
print(result['confidence'])       # 0.95 (95% confidence)
print(result['risk_level'])       # 'HIGH', 'MEDIUM', or 'LOW'
```

## 4. Test Sample Emails

Try the included examples:
```bash
python example.py
```

This demonstrates:
- Single prediction
- Batch prediction
- Model comparison
- Risk assessment

## Example Outputs

**Phishing Email:**
```
⚠️  PHISHING
Prediction: PHISHING
Risk Level: HIGH
Confidence: 95.32%
```

**Legitimate Email:**
```
✅ LEGITIMATE
Prediction: LEGITIMATE
Risk Level: LOW
Confidence: 98.45%
```

## API Endpoints (if running Flask)

### Predict an email
```bash
curl -X POST http://127.0.0.1:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"email_text":"Your email here"}'
```

### Compare models
```bash
curl -X POST http://127.0.0.1:5000/api/compare \
  -H "Content-Type: application/json" \
  -d '{"email_text":"Your email here"}'
```

## Automated Setup (Windows/Mac/Linux)

**Windows:**
```bash
setup.bat
```

**Mac/Linux:**
```bash
bash setup.sh
```

These scripts automatically:
1. Install dependencies
2. Train models
3. Let you choose interface (Web/CLI)

## Project Structure
```
phishing-detector/
├── data/                 # Email dataset
├── models/              # Trained models (auto-generated)
├── templates/           # HTML templates
├── app.py               # Flask web app
├── detector.py          # Detection module
├── cli.py               # Command-line interface
├── train_model.py       # Model training
├── example.py           # Usage examples
├── requirements.txt     # Dependencies
└── README.md            # Full documentation
```

## Model Performance

The detector uses:
- **TF-IDF**: Feature extraction from emails
- **Naive Bayes**: Fast, good for text
- **Logistic Regression**: Balanced approach

Both models are trained and can be compared to find the best predictions.

## Common Tasks

**Train model with new data:**
```bash
python train_model.py
```

**Get just the result programmatically:**
```python
from detector import predict_email
result = predict_email("Click here to verify account!")
print(f"Is Phishing: {result['is_phishing']}")
```

**Batch process emails:**
```python
from detector import PhishingDetector
detector = PhishingDetector()
results = detector.predict_batch([email1, email2, email3])
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | Run `pip install -r requirements.txt` |
| Models not found | Run `python train_model.py` first |
| Port 5000 in use | Change port in `app.py` to 5001+ |
| Python not found | Ensure Python 3.8+ is installed |

## Need More Help?

Check the full [README.md](README.md) for:
- Detailed API documentation
- Model explanations
- Advanced usage
- Improvement tips

---

**You're ready! 🚀** Pick an interface and start detecting phishing emails!
