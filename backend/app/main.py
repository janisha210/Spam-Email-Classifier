"""
FastAPI main application
"""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.models.model_loader import model_loader

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for startup and shutdown events
    """
    # Startup: Load model
    logger.info("Starting up application...")
    try:
        model_loader.load_model()
        logger.info("Model loaded successfully during startup")
    except Exception as e:
        logger.error(f"Failed to load model during startup: {str(e)}")
        logger.warning("Application will start but predictions may fail")
    
    yield
    
    # Shutdown
    logger.info("Shutting down application...")


# Create FastAPI app
app = FastAPI(
    title="Spam Email Classifier API",
    description="Machine learning API for classifying emails as spam or safe",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)


@app.get("/", tags=["root"])
async def root():
    """Root endpoint"""
    return {
        "message": "Spam Email Classifier API",
        "docs": "/docs",
        "health": "/api/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
