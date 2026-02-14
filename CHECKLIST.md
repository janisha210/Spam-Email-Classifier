# ✅ Setup Checklist

Follow this checklist to get your spam email classifier running!

## Prerequisites

### Required
- [ ] **Python 3.8 or higher** installed
  - Check: Open terminal and run `python --version`
  - Download: https://www.python.org/downloads/

### Optional (for Frontend)
- [ ] **Node.js 16 or higher** installed
  - Check: Open terminal and run `node --version`
  - Download: https://nodejs.org/

## Backend Setup

- [ ] Navigate to project directory
- [ ] Run `setup_backend.bat` (or follow manual steps below)

### Manual Backend Setup
- [ ] Open terminal in `backend` folder
- [ ] Create virtual environment: `python -m venv venv`
- [ ] Activate virtual environment: `venv\Scripts\activate` (Windows)
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Create sample model: `python create_sample_model.py`
- [ ] Verify model file exists: `spam_model.pkl`

## Frontend Setup (Optional)

- [ ] Ensure Node.js is installed
- [ ] Run `setup_frontend.bat` (or follow manual steps below)

### Manual Frontend Setup
- [ ] Open terminal in `frontend` folder
- [ ] Install dependencies: `npm install`
- [ ] Wait for installation to complete

## Running the Application

### Start Backend
- [ ] Run `start_backend.bat` OR
- [ ] Manual: 
  - [ ] Open terminal in `backend` folder
  - [ ] Activate venv: `venv\Scripts\activate`
  - [ ] Run: `python -m app.main`
- [ ] Verify backend is running: Open http://localhost:8000/docs
- [ ] Check health endpoint: http://localhost:8000/api/health

### Start Frontend (if Node.js installed)
- [ ] Run `start_frontend.bat` OR
- [ ] Manual:
  - [ ] Open terminal in `frontend` folder
  - [ ] Run: `npm run dev`
- [ ] Verify frontend is running: Open http://localhost:5173

## Testing the Application

### Test Backend API (using FastAPI docs)
- [ ] Go to http://localhost:8000/docs
- [ ] Click on POST /api/predict
- [ ] Click "Try it out"
- [ ] Enter test email text:
  ```
  Congratulations! You've won a prize. Click here now!
  ```
- [ ] Click "Execute"
- [ ] Verify you get a response with prediction, confidence, and probabilities

### Test Frontend UI (if running)
- [ ] Go to http://localhost:5173
- [ ] Verify the page loads with dark theme
- [ ] Click "Spam Example" button
- [ ] Click "Analyze Email" button
- [ ] Verify you see a red result card showing "Spam Detected"
- [ ] Click "Safe Example" button
- [ ] Click "Analyze Email" button
- [ ] Verify you see a green result card showing "Safe Email"

## Troubleshooting

### Backend Issues
- [ ] If "Module not found": Reinstall dependencies
- [ ] If "Model not found": Run `python create_sample_model.py`
- [ ] If "Port in use": Change port in `app/main.py` or kill process on port 8000
- [ ] If virtual env issues: Delete `venv` folder and recreate

### Frontend Issues
- [ ] If npm not found: Install Node.js
- [ ] If dependencies fail: Run `npm cache clean --force` then `npm install`
- [ ] If can't connect to API: Ensure backend is running on port 8000
- [ ] If port in use: Change port in `vite.config.js`

## Verification

### Backend Verification
- [ ] FastAPI docs accessible at http://localhost:8000/docs
- [ ] Health check returns `{"status": "healthy", "model_loaded": true}`
- [ ] POST /api/predict returns valid predictions
- [ ] No error messages in terminal

### Frontend Verification
- [ ] Page loads without errors
- [ ] All components visible (header, form, footer)
- [ ] Sample buttons work
- [ ] Analyze button triggers API call
- [ ] Results display correctly
- [ ] No console errors in browser (F12 → Console)

## Next Steps

Once everything is working:
- [ ] Read README.md for detailed documentation
- [ ] Explore the code structure
- [ ] Try customizing the UI colors
- [ ] Train your own model with real data
- [ ] Add new features

## Success Criteria

You've successfully set up the application when:
- ✅ Backend server runs without errors
- ✅ API endpoints respond correctly
- ✅ Frontend loads and displays properly
- ✅ Email analysis works end-to-end
- ✅ Results show correct spam/safe classification

## Getting Help

If you encounter issues:
1. Check the error messages carefully
2. Review QUICKSTART.md for common solutions
3. Verify all prerequisites are installed
4. Check that both servers are running
5. Look at browser console for frontend errors
6. Check terminal output for backend errors

## Notes

- Keep both terminal windows open while using the app
- Backend must be running for frontend to work
- You can use the backend API without the frontend
- Sample model is for demonstration - replace with production model for real use

---

**Happy Coding! 🎉**
