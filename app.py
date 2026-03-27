from flask import Flask, render_template, request, jsonify
from detector import PhishingDetector
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

try:
    detector = PhishingDetector(model_type='naive_bayes')
except Exception as e:
    detector = None
    print(f"Warning: {e}")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    if not data or 'email_text' not in data:
        return jsonify({'error': 'No email text provided'}), 400
    
    if detector is None:
        return jsonify({'error': 'Model not loaded. Run train_model.py first.'}), 500
    
    email_text = data['email_text'].strip()
    
    if len(email_text) < 10:
        return jsonify({'error': 'Email text must be at least 10 characters'}), 400
    
    try:
        result = detector.predict(email_text)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/compare', methods=['POST'])
def compare():
    data = request.get_json()
    
    if not data or 'email_text' not in data:
        return jsonify({'error': 'No email text provided'}), 400
    
    email_text = data['email_text'].strip()
    
    if len(email_text) < 10:
        return jsonify({'error': 'Email text must be at least 10 characters'}), 400
    
    try:
        nb_detector = PhishingDetector(model_type='naive_bayes')
        lr_detector = PhishingDetector(model_type='logistic_regression')
        
        nb_result = nb_detector.predict(email_text)
        lr_result = lr_detector.predict(email_text)
        
        return jsonify({
            'naive_bayes': nb_result,
            'logistic_regression': lr_result
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    model_loaded = detector is not None
    return jsonify({
        'status': 'ok',
        'model_loaded': model_loaded
    }), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
