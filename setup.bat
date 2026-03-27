@echo off
REM Phishing Detector Setup Script for Windows

echo.
echo ========================================
echo   Phishing Email Detector - Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [1/4] Python found. Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [2/4] Training the model...
python train_model.py
if %errorlevel% neq 0 (
    echo Error: Failed to train model
    pause
    exit /b 1
)

echo.
echo [3/4] Setup complete!
echo.
echo Choose an option:
echo   1. Run Web App (Flask)
echo   2. Run CLI Interface
echo   3. Exit
echo.

set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo Starting Flask web app...
    echo Opening http://127.0.0.1:5000 in your browser...
    start http://127.0.0.1:5000
    python app.py
) else if "%choice%"=="2" (
    echo Starting CLI interface...
    python cli.py
) else (
    echo Goodbye!
)

pause
