TFIDF_CONFIG = {
    'max_features': 5000,
    'min_df': 1,
    'max_df': 0.8,
    'lowercase': True,
    'stop_words': 'english',
    'ngram_range': (1, 2)
}

TRAINING_CONFIG = {
    'data_path': 'data/sample_emails.csv',
    'test_size': 0.2,
    'random_state': 42,
    
    'naive_bayes': {
        'alpha': 1.0
    },
    
    'logistic_regression': {
        'max_iter': 1000,
        'random_state': 42,
        'C': 1.0
    }
}

MODEL_CONFIG = {
    'model_dir': 'models',
    'tfidf_file': 'tfidf_vectorizer.pkl',
    'naive_bayes_file': 'naive_bayes_model.pkl',
    'logistic_regression_file': 'logistic_regression_model.pkl'
}

FLASK_CONFIG = {
    'host': '127.0.0.1',
    'port': 5000,
    'debug': True,
    'max_content_length': 1000000
}

PREDICTION_CONFIG = {
    'default_model': 'naive_bayes',
    
    'high_risk_threshold': 0.8,
    'medium_risk_threshold': 0.5,
    
    'min_email_length': 10,
    'max_email_length': 100000
}

LOGGING_CONFIG = {
    'log_predictions': False,
    'log_file': 'predictions.log',
    'log_level': 'INFO'
}

PHISHING_INDICATORS = {
    'urgent_words': ['urgent', 'immediately', 'asap', 'now', 'quickly'],
    'verification_words': ['verify', 'confirm', 'validate', 'authenticate'],
    'threat_words': ['locked', 'suspended', 'closed', 'disabled', 'compromised'],
    'action_words': ['click', 'update', 'reset', 'confirm', 'validate'],
}

LEGITIMATE_INDICATORS = {
    'greeting': ['hello', 'hi', 'dear'],
    'thanks': ['thanks', 'thank you', 'appreciate'],
    'professional': ['regards', 'sincerely', 'best'],
    'schedule': ['meeting', 'call', 'conference', 'schedule'],
}

CACHE_CONFIG = {
    'enable_cache': False,
    'cache_max_size': 1000,
    'cache_ttl': 3600
}

def get_model_path(model_type='naive_bayes'):
    import os
    if model_type == 'naive_bayes':
        filename = MODEL_CONFIG['naive_bayes_file']
    else:
        filename = MODEL_CONFIG['logistic_regression_file']
    return os.path.join(MODEL_CONFIG['model_dir'], filename)


def get_tfidf_path():
    import os
    return os.path.join(MODEL_CONFIG['model_dir'], MODEL_CONFIG['tfidf_file'])


def get_risk_level(is_phishing, confidence):
    if not is_phishing:
        return 'LOW'
    elif confidence > PREDICTION_CONFIG['high_risk_threshold']:
        return 'HIGH'
    elif confidence > PREDICTION_CONFIG['medium_risk_threshold']:
        return 'MEDIUM'
    else:
        return 'LOW'


if __name__ == "__main__":
    print("Configuration loaded successfully!")
    print(f"Model Directory: {MODEL_CONFIG['model_dir']}")
    print(f"Flask Host: {FLASK_CONFIG['host']}:{FLASK_CONFIG['port']}")
    print(f"Default Model: {PREDICTION_CONFIG['default_model']}")
