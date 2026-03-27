#!/bin/bash
# Phishing Detector Setup Script for Mac/Linux

echo ""
echo "========================================"
echo "   Phishing Email Detector - Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed"
    exit 1
fi

echo "[1/4] Python found. Installing dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo ""
echo "[2/4] Training the model..."
python3 train_model.py
if [ $? -ne 0 ]; then
    echo "Error: Failed to train model"
    exit 1
fi

echo ""
echo "[3/4] Setup complete!"
echo ""
echo "Choose an option:"
echo "  1. Run Web App (Flask)"
echo "  2. Run CLI Interface"
echo "  3. Exit"
echo ""

read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo "Starting Flask web app..."
        if command -v open &> /dev/null; then
            open http://127.0.0.1:5000
        else
            echo "Open http://127.0.0.1:5000 in your browser"
        fi
        python3 app.py
        ;;
    2)
        echo "Starting CLI interface..."
        python3 cli.py
        ;;
    *)
        echo "Goodbye!"
        ;;
esac
