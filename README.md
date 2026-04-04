# Phishing Email Detector

A machine learning-based NLP application to detect phishing emails and distinguish them from legitimate emails. Includes both CLI and Flask web interface.

## Features

✅ **NLP-Based Detection** - Uses TF-IDF vectorization for feature extraction
✅ **Multiple ML Models** - Naive Bayes and Logistic Regression classifiers
✅ **Web Interface** - Beautiful Flask web app for easy usage
✅ **Model Comparison** - Compare predictions from different models side-by-side
✅ **Confidence Scores** - Get prediction confidence and probability distributions
✅ **Risk Assessment** - Automatic risk level classification (LOW, MEDIUM, HIGH)

## Tech Stack

- **Python 3.8+**
- **Scikit-learn** - Machine Learning library
- **Pandas** - Data processing
- **Flask** - Web framework
- **TF-IDF** - Text feature extraction

## Project Structure

```
phishing-detector/
├── data/
│   └── sample_emails.csv          # Training dataset
├── models/                         # Trained models (generated after training)
│   ├── tfidf_vectorizer.pkl
│   ├── naive_bayes_model.pkl
│   └── logistic_regression_model.pkl
├── templates/
│   └── index.html                  # Web UI template
├── train_model.py                  # Model training script
├── detector.py                     # Detection module
├── app.py                          # Flask web application
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Installation

### 1. Clone or Download the Project

```bash
cd phishing-detector
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Quick Start

### Step 1: Train the Models

```bash
python train_model.py
```

This will:
- Load the sample dataset from `data/sample_emails.csv`
- Split data into training and test sets (80/20)
- Train both Naive Bayes and Logistic Regression models
- Evaluate models on test set
- Save trained models to `models/` directory

**Expected Output:**
```
Loaded 30 emails
Class distribution:
phishing     15
legitimate   15

Training set size: 24
Test set size: 6

Creating TF-IDF vectorizer...
TF-IDF shape: (24, 1234)

Training Naive Bayes model...
Naive Bayes Accuracy: 1.0000
Naive Bayes Precision: 1.0000
Naive Bayes Recall: 1.0000
Naive Bayes F1-Score: 1.0000

Training Logistic Regression model...
Logistic Regression Accuracy: 1.0000
...
Models saved to 'models/' directory
```

### Step 2: Test the Detector (Optional)

```bash
python detector.py
```

This will test the detector with sample emails and show predictions.

### Step 3: Run the Web App

```bash
python app.py
```

Then open your browser and go to: **http://127.0.0.1:5000**

## Usage

### Web Interface

1. **Analyzer Tab**: Paste email text and click "Analyze Email"
   - Shows prediction (PHISHING or LEGITIMATE)
   - Displays risk level (LOW, MEDIUM, HIGH)
   - Shows confidence score and probability distribution

2. **Compare Models Tab**: Compare results from both ML models
   - See if both models agree
   - Useful for understanding model behavior

3. **About Tab**: Learn more about the detector

### Python API (Programmatic Use)

```python
from detector import PhishingDetector

# Initialize detector
detector = PhishingDetector(model_type='naive_bayes')

# Predict single email
email = "Click here to verify your account immediately!"
result = detector.predict(email)

print(result)
# Output:
# {
#     'prediction': 'phishing',
#     'risk_level': 'HIGH',
#     'confidence': 0.9876,
#     'probabilities': {'phishing': 0.9876, 'legitimate': 0.0124},
#     'is_phishing': True
# }
```

### Command Line Usage

```python
from detector import predict_email

# Quick prediction
result = predict_email("Your account will be closed in 24 hours!")
print(f"Prediction: {result['prediction']}")
print(f"Confidence: {result['confidence']}")
```

## Model Performance

The models are trained on a sample dataset and achieve good accuracy. For production use, train on a larger and more diverse dataset.

**Training Metrics:**
- **Naive Bayes**: High recall (catch more phishing), may have false positives
- **Logistic Regression**: Balanced precision and recall

## API Endpoints

### POST `/api/predict`
Predict if an email is phishing or legitimate.

**Request:**
```json
{
    "email_text": "Your email content here..."
}
```

**Response:**
```json
{
    "prediction": "phishing",
    "risk_level": "HIGH",
    "confidence": 0.95,
    "probabilities": {
        "phishing": 0.95,
        "legitimate": 0.05
    },
    "is_phishing": true
}
```

### POST `/api/compare`
Compare predictions from both models.

**Request:**
```json
{
    "email_text": "Your email content here..."
}
```

**Response:**
```json
{
    "naive_bayes": { ... },
    "logistic_regression": { ... }
}
```

### GET `/health`
Check if the app and models are loaded.

## Features Explained

### TF-IDF Vectorization
- Converts text to numerical features
- Gives higher weight to words that are more important
- Parameters: max_features=5000, ngram_range=(1,2)

### Machine Learning Models

1. **Naive Bayes**
   - Fast and simple
   - Works well for text classification
   - Good for imbalanced datasets

2. **Logistic Regression**
   - Linear classification
   - Provides probability estimates
   - Better for balanced datasets

### Risk Level Classification
- **HIGH**: Phishing prediction with confidence > 80%
- **MEDIUM**: Phishing prediction with confidence ≤ 80%
- **LOW**: Legitimate prediction

## Improving the Detector

To improve accuracy:

1. **Larger Dataset**: Use thousands of real phishing and legitimate emails
2. **Better Features**: Add domain analysis, URL patterns, sender information
3. **Advanced Models**: Try SVM, Random Forest, Neural Networks
4. **Hyperparameter Tuning**: Optimize TF-IDF and model parameters
5. **Cross-validation**: Use k-fold cross-validation for better evaluation

## Adding Your Own Data

1. Add emails to `data/sample_emails.csv` in CSV format:
```csv
text,label
"Your email content here",phishing
"Another email",legitimate
```

2. Retrain the model:
```bash
python train_model.py
```

## Troubleshooting

**Error: Model files not found**
- Run `python train_model.py` first to train and save models

**Port 5000 already in use**
- Change the port in `app.py`: `app.run(port=5001)`

**TensorFlow/CUDA errors**
- Not needed for this project, can safely ignore
- If issue persists, try: `pip install --upgrade pandas scikit-learn`


## Future Enhancements

- [ ] Add URL and domain analysis
- [ ] Integrate with email clients
- [ ] Database for email history
- [ ] Real-time model updates
- [ ] Advanced spam detection
- [ ] Deep learning models (LSTM, BERT)
