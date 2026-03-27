import sys
from detector import PhishingDetector


def print_separator(char='=', length=60):
    print(char * length)


def print_result(result):
    print()
    print_separator()
    
    prediction = result['prediction'].upper()
    is_phishing = result['is_phishing']
    icon = '⚠️  PHISHING' if is_phishing else '✅ LEGITIMATE'
    
    print(f"\n{icon}")
    print(f"\nPrediction: {prediction}")
    print(f"Risk Level: {result['risk_level']}")
    print(f"Confidence: {result['confidence']*100:.2f}%")
    
    print(f"\nProbabilities:")
    for label, prob in result['probabilities'].items():
        print(f"  {label.capitalize()}: {prob*100:.2f}%")
    
    print()
    print_separator()


def main():
    print()
    print_separator('*', 60)
    print("        Phishing Email Detector - CLI".center(60))
    print_separator('*', 60)
    print()
    
    model_choice = input("Select model (1=Naive Bayes, 2=Logistic Regression) [1]: ").strip()
    model_type = 'logistic_regression' if model_choice == '2' else 'naive_bayes'
    
    print(f"\nInitializing {model_type} model...")
    try:
        detector = PhishingDetector(model_type=model_type)
    except Exception as e:
        print(f"Error: {e}")
        print("Please run 'python train_model.py' first to train the model.")
        sys.exit(1)
    
    print("Model loaded successfully!\n")
    
    while True:
        print()
        email_text = input("Paste email text (or 'quit' to exit):\n> ").strip()
        
        if email_text.lower() == 'quit':
            print("\nGoodbye! Stay safe from phishing! 🔐")
            break
        
        if len(email_text) < 10:
            print("⚠️  Email text must be at least 10 characters long.")
            continue
        
        print("\nAnalyzing...")
        result = detector.predict(email_text)
        print_result(result)


def batch_mode(file_path):
    print(f"Processing emails from: {file_path}")
    
    detector = PhishingDetector()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            emails = f.read().split('\n---\n')
        
        print(f"Found {len(emails)} emails\n")
        
        results = detector.predict_batch(emails)
        
        phishing_count = sum(1 for r in results if r['is_phishing'])
        legitimate_count = len(results) - phishing_count
        
        print(f"Results: {phishing_count} phishing, {legitimate_count} legitimate")
        print(f"Accuracy: {(1 - phishing_count/len(results))*100:.1f}% legitimate\n")
        
        for i, result in enumerate(results, 1):
            print(f"Email {i}: {result['prediction'].upper()} (Confidence: {result['confidence']*100:.2f}%)")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        batch_mode(sys.argv[1])
    else:
        main()
