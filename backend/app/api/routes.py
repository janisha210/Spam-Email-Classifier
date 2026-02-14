"""
API routes for spam classification
"""
import logging
from fastapi import APIRouter, HTTPException, status

from app.schemas.prediction import EmailRequest, PredictionResponse
from app.services.inference import spam_classifier

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["prediction"])


@router.post(
    "/predict",
    response_model=PredictionResponse,
    status_code=status.HTTP_200_OK,
    summary="Classify email as spam or safe",
    description="Accepts email text and returns classification with confidence score"
)
async def predict_spam(request: EmailRequest) -> PredictionResponse:
    """
    Predict whether an email is spam or safe
    
    Args:
        request: EmailRequest containing the email text
        
    Returns:
        PredictionResponse with prediction, confidence, and probabilities
        
    Raises:
        HTTPException: If prediction fails
    """
    try:
        prediction, confidence, probabilities = spam_classifier.predict(
            request.text
        )
        
        return PredictionResponse(
            prediction=prediction,
            confidence=confidence,
            probabilities=probabilities
        )
        
    except Exception as e:
        logger.error(f"Prediction endpoint error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {str(e)}"
        )


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health check endpoint"
)
async def health_check():
    """Check if the API and model are ready"""
    from app.models.model_loader import model_loader
    
    return {
        "status": "healthy",
        "model_loaded": model_loader.is_loaded(),
        "model_error": model_loader.load_error if hasattr(model_loader, 'load_error') else None
    }
