import pickle
import os
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


class PhishingDetector:
    
    def __init__(self, model_dir='models', model_type='naive_bayes'):
        if not os.path.isabs(model_dir):
            model_dir = os.path.join(SCRIPT_DIR, model_dir)
        
        self.model_dir = model_dir
        self.model_type = model_type
        self.tfidf = None
        self.model = None
        self.load_models()
    
    def load_models(self):
        try:
            with open(os.path.join(self.model_dir, 'tfidf_vectorizer.pkl'), 'rb') as f:
                self.tfidf = pickle.load(f)
            
            if self.model_type == 'naive_bayes':
                model_file = 'naive_bayes_model.pkl'
            else:
                model_file = 'logistic_regression_model.pkl'
            
            with open(os.path.join(self.model_dir, model_file), 'rb') as f:
                self.model = pickle.load(f)
            
            print(f"Models loaded successfully (using {self.model_type})")
        except FileNotFoundError as e:
            print(f"Error: Model files not found. Please run train_model.py first.")
            raise e
    
    def predict(self, email_text):
        email_tfidf = self.tfidf.transform([email_text])
        
        prediction = self.model.predict(email_tfidf)[0]
        
        probabilities = self.model.predict_proba(email_tfidf)[0]
        confidence = float(np.max(probabilities))
        
        classes = self.model.classes_
        class_prob = {}
        for idx, cls in enumerate(classes):
            class_prob[cls] = float(probabilities[idx])
        
        if prediction == 'phishing':
            risk_level = 'HIGH' if confidence > 0.8 else 'MEDIUM'
        else:
            risk_level = 'LOW'
        
        return {
            'prediction': prediction,
            'risk_level': risk_level,
            'confidence': round(confidence, 4),
            'probabilities': class_prob,
            'is_phishing': prediction == 'phishing'
        }
    
    def predict_batch(self, email_texts):
        results = []
        for email in email_texts:
            results.append(self.predict(email))
        return results


def predict_email(email_text, model_type='naive_bayes'):
    detector = PhishingDetector(model_type=model_type)
    return detector.predict(email_text)


if __name__ == "__main__":
    detector = PhishingDetector()
    
    test_emails = [
        "Click here to verify your account immediately! Your account will be closed in 24 hours!",
        "Hi John, Thanks for the email. Looking forward to our meeting tomorrow.",
        "URGENT: Confirm your password now to avoid account suspension!",
        "Hello, Here's the report you requested. Please review and provide feedback."
    ]
    
    print("Testing Phishing Detector\n" + "="*50 + "\n")
    
    for i, email in enumerate(test_emails, 1):
        print(f"Test {i}:")
        print(f"Email: {email[:80]}...")
        result = detector.predict(email)
        print(f"Prediction: {result['prediction'].upper()}")
        print(f"Risk Level: {result['risk_level']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Probabilities: {result['probabilities']}")
        print()
