# 🚀 Quick Commands Reference

## Setup & Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Train models (MUST run before using detector)
python train_model.py
```

## Run Application

### Web App (Recommended)
```bash
python app.py
# Opens: http://127.0.0.1:5000
```

### Command-Line Interface
```bash
# Interactive mode
python cli.py

# Batch mode (analyze file)
python cli.py data/test_emails.txt
```

### Examples
```bash
# Run all usage examples
python example.py
```

## Python API

### Single Prediction
```python
from detector import PhishingDetector

detector = PhishingDetector()
result = detector.predict("Click here to verify your account!")

print(result['prediction'])      # 'phishing'
print(result['confidence'])       # 0.95
print(result['risk_level'])       # 'HIGH'
```

### Batch Prediction
```python
from detector import PhishingDetector

detector = PhishingDetector()
emails = ["Email 1", "Email 2", "Email 3"]
results = detector.predict_batch(emails)
```

### Quick Prediction
```python
from detector import predict_email

result = predict_email("Your suspicious email text here")
```

### Switch Models
```python
# Use Logistic Regression instead
detector = PhishingDetector(model_type='logistic_regression')
result = detector.predict(email_text)
```

## API Endpoints (Flask)

### Predict Email
```bash
curl -X POST http://127.0.0.1:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"email_text":"Click here now!"}'
```

### Compare Models
```bash
curl -X POST http://127.0.0.1:5000/api/compare \
  -H "Content-Type: application/json" \
  -d '{"email_text":"Your email here"}'
```

### Health Check
```bash
curl http://127.0.0.1:5000/health
```

## Automated Setup

### Windows
```bash
setup.bat
# Installs deps, trains models, launches app/CLI
```

### Mac/Linux
```bash
bash setup.sh
# Same as above for Unix systems
```

## Common Tasks

### Train with New Data
```bash
# 1. Add emails to data/sample_emails.csv
# 2. Run training
python train_model.py
```

### Test Detector
```python
from detector import PhishingDetector

detector = PhishingDetector()

# Test legitimate
legit = detector.predict("Hi, how are you?")
print(legit['prediction'])  # 'legitimate'

# Test phishing
phish = detector.predict("VERIFY NOW OR ACCOUNT LOCKED!")
print(phish['prediction'])  # 'phishing'
```

### Filter by Confidence
```python
from detector import PhishingDetector

detector = PhishingDetector()
result = detector.predict(email_text)

if result['confidence'] > 0.9:
    print("Very confident prediction")
elif result['confidence'] > 0.7:
    print("Moderately confident")
else:
    print("Low confidence - review manually")
```

### Check Model Status
```bash
# Verify models exist
# If no files in models/ folder, run: python train_model.py

ls models/              # Mac/Linux
dir models              # Windows
```

## Development

### Run Tests
```bash
python example.py       # Run all examples
```

### View Model Details
```python
from detector import PhishingDetector
import pickle

# Load model directly
with open('models/naive_bayes_model.pkl', 'rb') as f:
    model = pickle.load(f)
    print(f"Classes: {model.classes_}")
```

### Profile Code
```bash
# Time the prediction
python -m timeit "from detector import PhishingDetector; \
d = PhishingDetector(); d.predict('test')"
```

## Troubleshooting Commands

### Check Python Version
```bash
python --version
# Expected: Python 3.8 or higher
```

### Verify Dependencies
```bash
pip list | grep -E "(flask|pandas|scikit-learn|numpy)"
```

### Clear Cache
```bash
# Remove Python cache
rm -rf __pycache__      # Mac/Linux
rmdir /s __pycache__    # Windows
```

### Retrain Models
```bash
# Complete retrain
rm -rf models/          # Delete old models
python train_model.py   # Retrain
```

## Interactive Testing

### Test in Python Shell
```bash
python

>>> from detector import PhishingDetector
>>> d = PhishingDetector()
>>> r = d.predict("Click here!")
>>> print(r)
{'prediction': 'phishing', ...}
>>> exit()
```

### Test API with curl
```bash
# POST prediction
curl -X POST http://127.0.0.1:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"email_text":"Win free money now!"}'

# Get health status
curl http://127.0.0.1:5000/health
```

## Performance Tips

### Speed up Predictions
```python
# Reuse detector instance
detector = PhishingDetector()  # Create once

# Use batch prediction for multiple emails
results = detector.predict_batch(email_list)  # Faster
```

### Reduce Model Size
Edit `config.py` - reduce `max_features` in TFIDF_CONFIG:
```python
'max_features': 2000,  # Reduced from 5000
```

Then retrain:
```bash
python train_model.py
```

## Git & Version Control

### Initialize Git
```bash
git init
git add .
git commit -m "Initial phishing detector"
```

### Ignore Models
```bash
# Already in .gitignore
# Models large files won't be tracked
```

## Deployment

### Run on Different Port
Edit `app.py`:
```python
app.run(port=8000)  # Changed from 5000
```

### Production Mode
```bash
# Disable debug
python -c "
from app import app
app.run(debug=False, host='0.0.0.0', port=5000)
"
```

---

## Quick Reference Table

| Task | Command |
|------|---------|
| Install | `pip install -r requirements.txt` |
| Train | `python train_model.py` |
| Web App | `python app.py` |
| CLI | `python cli.py` |
| Examples | `python example.py` |
| Test API | `curl http://127.0.0.1:5000/health` |
| Setup (Win) | `setup.bat` |
| Setup (Unix) | `bash setup.sh` |

---
