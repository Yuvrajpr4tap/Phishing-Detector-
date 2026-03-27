from detector import PhishingDetector


def example_single_prediction():
    print("="*60)
    print("Example 1: Single Email Prediction")
    print("="*60 + "\n")
    
    detector = PhishingDetector(model_type='naive_bayes')
    
    email = """
    URGENT! Your account has been locked. Click here immediately to verify your identity.
    Your account will be permanently closed in 24 hours. Do not ignore this message.
    """
    
    result = detector.predict(email)
    
    print(f"Email: {email.strip()}\n")
    print(f"Prediction: {result['prediction'].upper()}")
    print(f"Risk Level: {result['risk_level']}")
    print(f"Confidence: {result['confidence']*100:.2f}%")
    print(f"Is Phishing: {result['is_phishing']}")
    print()


def example_batch_prediction():
    print("="*60)
    print("Example 2: Batch Email Prediction")
    print("="*60 + "\n")
    
    detector = PhishingDetector()
    
    emails = [
        "Hi John, Are you available for a meeting tomorrow at 2 PM?",
        "VERIFY YOUR ACCOUNT NOW! Click link to confirm card details!",
        "The quarterly earnings report has been published. Here's the link.",
        "Congratulations! You've won a prize! Click here to claim!"
    ]
    
    results = detector.predict_batch(emails)
    
    for i, (email, result) in enumerate(zip(emails, results), 1):
        print(f"Email {i}: {email[:50]}...")
        print(f"  → Prediction: {result['prediction'].upper()}")
        print(f"  → Confidence: {result['confidence']*100:.2f}%\n")


def example_both_models():
    print("="*60)
    print("Example 3: Compare Both Models")
    print("="*60 + "\n")
    
    email = "Confirm your password immediately or your account will be suspended!"
    
    nb_detector = PhishingDetector(model_type='naive_bayes')
    nb_result = nb_detector.predict(email)
    
    lr_detector = PhishingDetector(model_type='logistic_regression')
    lr_result = lr_detector.predict(email)
    
    print(f"Email: {email}\n")
    print("Naive Bayes:")
    print(f"  Prediction: {nb_result['prediction'].upper()}")
    print(f"  Confidence: {nb_result['confidence']*100:.2f}%")
    print(f"  Probabilities: {nb_result['probabilities']}\n")
    
    print("Logistic Regression:")
    print(f"  Prediction: {lr_result['prediction'].upper()}")
    print(f"  Confidence: {lr_result['confidence']*100:.2f}%")
    print(f"  Probabilities: {lr_result['probabilities']}\n")
    

    agreement = nb_result['prediction'] == lr_result['prediction']
    print(f"Models agree: {agreement}")
    print()


def example_risk_assessment():
    print("="*60)
    print("Example 4: Risk Assessment Details")
    print("="*60 + "\n")
    
    detector = PhishingDetector()
    
    test_cases = [
        ("Hello! How are you doing?", "Legitimate"),
        ("Your account is locked. Click here to unlock!", "Suspicious"),
        ("Can we schedule a meeting?", "Legitimate")
    ]
    
    for email, expected in test_cases:
        result = detector.predict(email)
        
        print(f"Email: {email}")
        print(f"Expected: {expected}")
        print(f"Prediction: {result['prediction'].upper()}")
        print(f"Confidence: {result['confidence']*100:.2f}%")
        print(f"Risk Level: {result['risk_level']}")
        
        if result['prediction'] == 'phishing':
            correct = expected == 'Suspicious'
        else:
            correct = expected == 'Legitimate'
        
        status = "✓ Correct" if correct else "✗ Incorrect"
        print(f"Status: {status}\n")


def example_threshold_filtering():
    print("="*60)
    print("Example 5: Confidence Threshold Filtering")
    print("="*60 + "\n")
    
    detector = PhishingDetector()
    
    emails = [
        "Click here immediately!",
        "Hi, how are you?",
        "Verify your account now!",
        "Let's schedule a call.",
        "URGENT: Confirm your details!"
    ]
    
    threshold = 0.7
    
    results = detector.predict_batch(emails)
    
    print(f"Filtering results with confidence threshold > {threshold*100:.0f}%\n")
    
    high_confidence_phishing = []
    for email, result in zip(emails, results):
        if result['is_phishing'] and result['confidence'] > threshold:
            high_confidence_phishing.append((email, result['confidence']))
            print(f"⚠️  HIGH CONFIDENCE PHISHING: {email[:50]}...")
            print(f"   Confidence: {result['confidence']*100:.2f}%\n")
    
    print(f"Total high-confidence phishing detected: {len(high_confidence_phishing)}")
    print()


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  Phishing Detector - Usage Examples")
    print("="*60 + "\n")
    
    example_single_prediction()
    example_batch_prediction()
    example_both_models()
    example_risk_assessment()
    example_threshold_filtering()
    
    print("="*60)
    print("  All examples completed! Check the code for more details.")
    print("="*60 + "\n")
