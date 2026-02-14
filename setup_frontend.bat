@echo off
echo ========================================
echo   Spam Email Classifier - Frontend Setup
echo ========================================
echo.

cd frontend

echo [1/2] Installing dependencies...
call npm install
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    echo Make sure Node.js and npm are installed
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo To start the frontend server, run:
echo   cd frontend
echo   npm run dev
echo.
pause
