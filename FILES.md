# 📋 Project Files Reference

Complete guide to all files in the Phishing Email Detector project.

## Core Application Files

### `app.py` - Flask Web Application
**Purpose**: Main web application entry point
- Starts Flask development server
- Provides REST API endpoints
- Routes requests to the detector
- Serves HTML templates
- Error handling and health checks

**Key Endpoints**:
- `GET /` - Serve web UI
- `POST /api/predict` - Predict single email
- `POST /api/compare` - Compare both models
- `GET /health` - Health check

**Run**: `python app.py`

---

### `detector.py` - Detection Module
**Purpose**: Core ML detection logic
- `PhishingDetector` class for predictions
- Loads pre-trained models and vectorizer
- Provides single and batch prediction
- Calculates confidence scores
- Determines risk levels

**Main Class**: `PhishingDetector`
- `__init__()` - Initialize with model type
- `predict()` - Predict single email
- `predict_batch()` - Predict multiple emails
- `load_models()` - Load trained models

**Run**: `python detector.py` (tests the detector)

---

### `train_model.py` - Model Training
**Purpose**: Train ML models on email dataset
- Loads email CSV data
- Creates TF-IDF vectorizer
- Trains Naive Bayes and Logistic Regression
- Evaluates model performance
- Saves trained models to disk

**Creates**:
- `models/tfidf_vectorizer.pkl`
- `models/naive_bayes_model.pkl`
- `models/logistic_regression_model.pkl`

**Run**: `python train_model.py`

---

### `cli.py` - Command-Line Interface
**Purpose**: Interactive CLI for email analysis
- Interactive terminal interface
- Model selection dropdown
- Batch file processing mode
- Pretty-printed results

**Modes**:
- Interactive: `python cli.py`
- Batch: `python cli.py data/test_emails.txt`

**Run**: `python cli.py`

---

## Configuration & Setup Files

### `config.py` - Configuration Settings
**Purpose**: Centralized configuration
- TF-IDF parameters
- Model training settings
- Flask app settings
- Prediction thresholds
- Logging configuration
- Phishing/legitimate indicators

**Key Sections**:
- `TFIDF_CONFIG` - NLP settings
- `TRAINING_CONFIG` - ML parameters
- `FLASK_CONFIG` - Web app settings
- `PREDICTION_CONFIG` - Thresholds

---

### `requirements.txt` - Python Dependencies
**Purpose**: List of required Python packages
- flask==2.3.3
- pandas==2.0.3
- scikit-learn==1.3.1
- numpy==1.24.3

**Install**: `pip install -r requirements.txt`

---

### `setup.bat` - Windows Setup Script
**Purpose**: Automated setup for Windows
- Check Python installation
- Install dependencies
- Train models
- Launch web app or CLI

**Run**: `setup.bat`

---

### `setup.sh` - Mac/Linux Setup Script
**Purpose**: Automated setup for Mac/Linux
- Same as setup.bat but for Unix systems
- Auto-open browser for web app

**Run**: `bash setup.sh`

---

## Data Files

### `data/sample_emails.csv` - Training Dataset
**Format**: CSV with 2 columns
- `text` - Email content
- `label` - "phishing" or "legitimate"

**Contains**: 30 sample emails (15 phishing, 15 legitimate)

**Use**: Training data for the ML models

---

### `data/test_emails.txt` - Test Emails
**Format**: Plain text with `---` separator between emails
**Contains**: 10 diverse test emails
**Use**: Batch testing with CLI

---

### `models/` - Trained Models Directory
**Auto-generated after running `train_model.py`**

**Contains**:
- `tfidf_vectorizer.pkl` - TF-IDF encoder
- `naive_bayes_model.pkl` - Naive Bayes classifier
- `logistic_regression_model.pkl` - Logistic Regression classifier

**Size**: ~1-5 MB combined

---

## Web Interface Files

### `templates/index.html` - Web UI Template
**Purpose**: HTML UI for the Flask app
- Single Page Application (SPA)
- 3 tabs: Analyzer, Compare, About
- JavaScript for API calls
- Modern CSS styling
- Responsive design

**Features**:
- Email text input
- Real-time prediction
- Risk level display
- Model comparison
- Probability visualization

**Serves at**: http://127.0.0.1:5000

---

### `static/` - Static Assets Directory
**Purpose**: Store CSS, JavaScript, images
**Currently**: Empty (CSS in HTML for now)
**Future**: Static files for scaling

---

## Documentation Files

### `README.md` - Full Documentation
**Contains**:
- Project overview
- Installation instructions
- Usage guide
- API documentation
- Model explanations
- Troubleshooting
- Future enhancements

**Read this for**: Complete reference

---

### `QUICKSTART.md` - Quick Start Guide
**Contains**:
- 2-minute setup
- Interface options
- Example usage
- Common tasks
- Troubleshooting cheat sheet

**Read this for**: Fast onboarding

---

### `example.py` - Usage Examples
**Purpose**: Demonstrate programmatic usage
**Examples**:
1. Single prediction
2. Batch prediction
3. Model comparison
4. Risk assessment
5. Threshold filtering

**Run**: `python example.py`

---

### `.gitignore` - Git Ignore Rules
**Purpose**: Exclude files from git
- Python cache files
- Virtual environments
- Trained models
- Log files
- IDE settings

---

## Directory Structure Summary

```
phishing-detector/
│
├── 📄 Core Application
│   ├── app.py                    # Flask web server
│   ├── detector.py               # ML detector class
│   ├── train_model.py            # Model training
│   ├── cli.py                    # CLI interface
│   └── config.py                 # Configuration
│
├── 💾 Data
│   └── data/
│       ├── sample_emails.csv     # Training data
│       └── test_emails.txt       # Test data
│
├── 🤖 Models (auto-generated)
│   └── models/
│       ├── tfidf_vectorizer.pkl
│       ├── naive_bayes_model.pkl
│       └── logistic_regression_model.pkl
│
├── 🎨 Web Interface
│   ├── templates/
│   │   └── index.html            # Flask template
│   └── static/                   # CSS/JS/Images
│
├── 📦 Setup & Config
│   ├── requirements.txt          # Dependencies
│   ├── setup.bat                 # Windows setup
│   └── setup.sh                  # Mac/Linux setup
│
├── 📚 Documentation
│   ├── README.md                 # Full docs
│   ├── QUICKSTART.md             # Quick start
│   ├── example.py                # Code examples
│   └── FILES.md                  # This file
│
└── ⚙️ Other
    └── .gitignore               # Git exclusions
```

## File Dependencies

```
train_model.py
    ├─ data/sample_emails.csv
    └─ generates: models/*.pkl

app.py
    ├─ detector.py
    ├─ models/*.pkl
    └─ templates/index.html

detector.py
    └─ models/*.pkl

cli.py
    ├─ detector.py
    └─ models/*.pkl

example.py
    ├─ detector.py
    └─ models/*.pkl
```

## Typical Workflow

1. **First Time**:
   ```bash
   pip install -r requirements.txt    # Install deps
   python train_model.py              # Train models
   ```

2. **Run Application**:
   ```bash
   python app.py                       # Web app
   # OR
   python cli.py                       # CLI
   ```

3. **Test/Explore**:
   ```bash
   python example.py                   # Run examples
   ```

4. **Update Models**:
   ```bash
   # Edit data/sample_emails.csv
   python train_model.py              # Retrain
   ```

## File Sizes

Approximate sizes:
- `requirements.txt`: < 1 KB
- `detector.py`: ~5 KB
- `train_model.py`: ~5 KB
- `app.py`: ~3 KB
- `cli.py`: ~4 KB
- `config.py`: ~5 KB
- `templates/index.html`: ~15 KB
- `data/sample_emails.csv`: ~10 KB
- `models/` (after training): ~2-5 MB

**Total (without models)**:  ~50 KB
**Total (with models)**:     ~2-5 MB

---

## Next Steps

- **Get Started**: Read [QUICKSTART.md](QUICKSTART.md)
- **Full Guide**: Read [README.md](README.md)
- **See Examples**: Run `python example.py`
- **Launch App**: Run `python app.py`

---

Last Updated: March 2026
