# 📁 Project Structure

```
Spam email classifier/
│
├── 📄 README.md                    # Comprehensive documentation
├── 📄 QUICKSTART.md                # Quick start guide
│
├── 🔧 setup_backend.bat            # Backend setup script (Windows)
├── 🔧 setup_frontend.bat           # Frontend setup script (Windows)
├── 🚀 start_backend.bat            # Start backend server
├── 🚀 start_frontend.bat           # Start frontend server
│
├── 🐍 backend/                     # FastAPI Backend
│   ├── 📄 .gitignore
│   ├── 📄 requirements.txt         # Python dependencies
│   ├── 📄 create_sample_model.py  # Model creation script
│   ├── 📄 spam_model.pkl          # Trained ML model (created by script)
│   │
│   └── 📁 app/                    # Application package
│       ├── 📄 __init__.py
│       ├── 📄 main.py             # FastAPI app & CORS config
│       │
│       ├── 📁 models/             # Model management
│       │   └── 📄 model_loader.py # Load & cache ML model
│       │
│       ├── 📁 services/           # Business logic
│       │   └── 📄 inference.py    # Prediction service
│       │
│       ├── 📁 api/                # API routes
│       │   └── 📄 routes.py       # /predict & /health endpoints
│       │
│       └── 📁 schemas/            # Data validation
│           └── 📄 prediction.py   # Pydantic models
│
└── ⚛️ frontend/                    # React Frontend
    ├── 📄 .gitignore
    ├── 📄 package.json             # Node dependencies
    ├── 📄 vite.config.js           # Vite configuration
    ├── 📄 index.html               # HTML entry point
    │
    └── 📁 src/                     # Source code
        ├── 📄 main.jsx             # React entry point
        ├── 📄 App.jsx              # Main app component
        ├── 📄 App.css              # App styles
        ├── 📄 index.css            # Design system & global styles
        │
        └── 📁 components/          # React components
            ├── 📄 Header.jsx       # App header
            ├── 📄 Header.css
            ├── 📄 Footer.jsx       # App footer
            ├── 📄 Footer.css
            ├── 📄 SpamClassifier.jsx    # Main classifier UI
            ├── 📄 SpamClassifier.css
            ├── 📄 ResultCard.jsx        # Results display
            ├── 📄 ResultCard.css
            ├── 📄 LoadingSpinner.jsx    # Loading state
            └── 📄 LoadingSpinner.css
```

## 🎯 Key Files Explained

### Backend

| File | Purpose |
|------|---------|
| `app/main.py` | FastAPI application with CORS and lifespan management |
| `app/models/model_loader.py` | Loads and caches the ML model |
| `app/services/inference.py` | Handles prediction logic |
| `app/api/routes.py` | API endpoints (/predict, /health) |
| `app/schemas/prediction.py` | Pydantic schemas for validation |
| `create_sample_model.py` | Creates a sample TF-IDF + NB model |

### Frontend

| File | Purpose |
|------|---------|
| `src/main.jsx` | React app entry point |
| `src/App.jsx` | Main app layout |
| `src/index.css` | Design system with CSS variables |
| `components/SpamClassifier.jsx` | Main classifier with form & API calls |
| `components/ResultCard.jsx` | Color-coded result display |
| `components/LoadingSpinner.jsx` | Loading animation |
| `components/Header.jsx` | App header with logo |
| `components/Footer.jsx` | App footer |

## 🔄 Data Flow

```
User Input (Frontend)
    ↓
SpamClassifier Component
    ↓
POST /api/predict (API Request)
    ↓
FastAPI Routes (routes.py)
    ↓
Inference Service (inference.py)
    ↓
Model Loader (model_loader.py)
    ↓
TF-IDF + MultinomialNB Pipeline
    ↓
Prediction + Confidence
    ↓
Pydantic Response Schema
    ↓
JSON Response
    ↓
ResultCard Component (Frontend)
    ↓
User sees color-coded result!
```

## 🎨 Component Hierarchy

```
App
├── Header
│   ├── Logo Icon
│   ├── Title & Tagline
│   └── ML Badge
│
├── SpamClassifier (Main Content)
│   ├── Card Header
│   ├── Email Textarea
│   ├── Sample Buttons
│   ├── Action Buttons
│   │   ├── Analyze Button (with LoadingSpinner)
│   │   └── Clear Button
│   ├── Error Message (conditional)
│   ├── ResultCard (conditional)
│   │   ├── Result Header (icon + text)
│   │   ├── Confidence Bar
│   │   ├── Probability Distribution
│   │   └── Safety Tip
│   └── Info Cards (3 feature cards)
│
└── Footer
    ├── Tech Stack Info
    └── Copyright
```
