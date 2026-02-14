# 🚀 Quick Start Guide

## First Time Setup

### Option 1: Using Setup Scripts (Recommended for Windows)

1. **Setup Backend**
   - Double-click `setup_backend.bat`
   - Wait for installation to complete

2. **Setup Frontend** (requires Node.js)
   - Double-click `setup_frontend.bat`
   - Wait for installation to complete

### Option 2: Manual Setup

#### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python create_sample_model.py
```

#### Frontend
```bash
cd frontend
npm install
```

## Running the Application

### Option 1: Using Start Scripts (Windows)

1. **Start Backend** - Double-click `start_backend.bat`
2. **Start Frontend** - Double-click `start_frontend.bat`
3. **Open Browser** - Go to http://localhost:5173

### Option 2: Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate          # Windows
python -m app.main
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

## Accessing the Application

- **Frontend UI**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health

## Testing the Classifier

1. Open http://localhost:5173 in your browser
2. Try the sample emails or paste your own
3. Click "Analyze Email"
4. View the results with confidence scores!

## Troubleshooting

### Backend Issues

**Problem**: `Module not found` errors
- **Solution**: Make sure virtual environment is activated and dependencies are installed
  ```bash
  cd backend
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

**Problem**: `Model file not found`
- **Solution**: Create the sample model
  ```bash
  python create_sample_model.py
  ```

**Problem**: Port 8000 already in use
- **Solution**: Change the port in `backend/app/main.py` or kill the process using port 8000

### Frontend Issues

**Problem**: `npm: command not found`
- **Solution**: Install Node.js from https://nodejs.org/

**Problem**: Dependencies installation fails
- **Solution**: Clear npm cache and try again
  ```bash
  npm cache clean --force
  npm install
  ```

**Problem**: Cannot connect to backend
- **Solution**: Make sure backend is running on http://localhost:8000

## Next Steps

1. **Replace the sample model** with your own trained model
2. **Customize the UI** by editing files in `frontend/src/`
3. **Add more features** like email history, batch processing, etc.
4. **Deploy to production** using services like Heroku, Vercel, or AWS

## Need Help?

Check the main README.md for detailed documentation and architecture information.
