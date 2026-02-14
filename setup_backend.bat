@echo off
echo ========================================
echo   Spam Email Classifier - Backend Setup
echo ========================================
echo.

cd backend

echo [1/4] Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/4] Creating sample model...
python create_sample_model.py
if %errorlevel% neq 0 (
    echo Error: Failed to create sample model
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo To start the backend server, run:
echo   cd backend
echo   venv\Scripts\activate
echo   python -m app.main
echo.
pause
