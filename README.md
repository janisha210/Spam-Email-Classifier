# 🛡️ Spam Email Classifier

A full-stack AI-powered spam email classifier built with **FastAPI** backend and **React** frontend. Uses machine learning (TF-IDF + Multinomial Naive Bayes) to detect spam emails with confidence scores.

![Tech Stack](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## ✨ Features

- 🤖 **ML-Powered Classification**: TF-IDF vectorization + Multinomial Naive Bayes
- 📊 **Confidence Scores**: Get detailed probability distributions
- ⚡ **Real-time Analysis**: Instant classification results
- 🎨 **Premium UI**: Beautiful dark theme with smooth animations
- 📱 **Responsive Design**: Works perfectly on all devices
- 🔒 **Privacy First**: All processing happens locally
- 🏗️ **Modular Architecture**: Clean separation of concerns

## 🏗️ Architecture

### Backend Structure
```
backend/
├── app/
│   ├── models/
│   │   └── model_loader.py      # Model loading & caching
│   ├── services/
│   │   └── inference.py         # Prediction logic
│   ├── api/
│   │   └── routes.py            # API endpoints
│   ├── schemas/
│   │   └── prediction.py        # Pydantic models
│   └── main.py                  # FastAPI application
├── requirements.txt
└── spam_model.pkl               # Trained ML model
```

### Frontend Structure
```
frontend/
├── src/
│   ├── components/
│   │   ├── Header.jsx           # App header
│   │   ├── Footer.jsx           # App footer
│   │   ├── SpamClassifier.jsx   # Main classifier
│   │   ├── ResultCard.jsx       # Result display
│   │   └── LoadingSpinner.jsx   # Loading state
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css                # Design system
├── index.html
├── vite.config.js
└── package.json
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 16+** and **npm** (for frontend)
- **pip** (Python package manager)

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the sample model** (if you don't have spam_model.pkl)
   ```bash
   python create_sample_model.py
   ```
   
   This creates a trained TF-IDF + MultinomialNB pipeline with sample data.

5. **Run the FastAPI server**
   ```bash
   python -m app.main
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at: `http://localhost:8000`
   - API Docs: `http://localhost:8000/docs`
   - Health Check: `http://localhost:8000/api/health`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

   The app will be available at: `http://localhost:5173`

## 📡 API Endpoints

### POST `/api/predict`
Classify an email as spam or safe.

**Request Body:**
```json
{
  "text": "Congratulations! You've won a prize. Click here now!"
}
```

**Response:**
```json
{
  "prediction": "spam",
  "confidence": 0.95,
  "probabilities": {
    "safe": 0.05,
    "spam": 0.95
  }
}
```

### GET `/api/health`
Check API and model status.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

## 🎯 Usage

1. **Start both servers** (backend on port 8000, frontend on port 5173)
2. **Open the app** in your browser at `http://localhost:5173`
3. **Enter email text** in the textarea or try a sample
4. **Click "Analyze Email"** to get instant results
5. **View results** with confidence scores and probability distribution

## 🧪 Using Your Own Model

To use your own trained model:

1. **Train your model** using scikit-learn:
   ```python
   from sklearn.feature_extraction.text import TfidfVectorizer
   from sklearn.naive_bayes import MultinomialNB
   from sklearn.pipeline import Pipeline
   import pickle

   # Create pipeline
   pipeline = Pipeline([
       ('tfidf', TfidfVectorizer()),
       ('classifier', MultinomialNB())
   ])

   # Train on your data
   pipeline.fit(X_train, y_train)

   # Save the model
   with open('spam_model.pkl', 'wb') as f:
       pickle.dump(pipeline, f)
   ```

2. **Place `spam_model.pkl`** in the `backend/` directory

3. **Restart the backend server**

## 🎨 Design Features

- **Premium Dark Theme**: Modern, eye-catching color palette
- **Glassmorphism Effects**: Frosted glass UI elements
- **Smooth Animations**: Micro-interactions for better UX
- **Color-Coded Results**: Visual distinction between spam/safe
- **Responsive Layout**: Mobile-first design approach
- **Custom Typography**: Inter font family for clarity

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework
- **Pydantic**: Data validation using Python type hints
- **Scikit-learn**: Machine learning library
- **Uvicorn**: ASGI server

### Frontend
- **React 18**: UI library
- **Vite**: Build tool and dev server
- **Vanilla CSS**: Custom design system
- **Google Fonts**: Inter typography

## 📝 Model Details

The default model uses:
- **TF-IDF Vectorization**: Converts text to numerical features
- **Multinomial Naive Bayes**: Probabilistic classifier
- **Binary Classification**: Spam (1) vs Safe (0)

The sample model is trained on basic examples and should be replaced with a production model trained on a larger dataset.

## 🔧 Configuration

### Backend Configuration
Edit `backend/app/main.py` to configure:
- CORS origins
- Server host/port
- Model path

### Frontend Configuration
Edit `frontend/vite.config.js` to configure:
- Dev server port
- API proxy settings

## 📦 Building for Production

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm run build
npm run preview
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Scikit-learn for ML capabilities
- React team for the UI library
- Vite for the blazing-fast build tool

---

**Built with ♥ using FastAPI & React**
