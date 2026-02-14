"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, Field


class EmailRequest(BaseModel):
    """Request schema for email classification"""
    text: str = Field(
        ..., 
        min_length=1,
        description="Email text to classify",
        examples=["Congratulations! You've won a free prize. Click here to claim now!"]
    )


class PredictionResponse(BaseModel):
    """Response schema for prediction results"""
    prediction: str = Field(
        ...,
        description="Classification result: 'spam' or 'safe'",
        examples=["spam"]
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1",
        examples=[0.95]
    )
    probabilities: dict[str, float] = Field(
        ...,
        description="Probability distribution for each class",
        examples=[{"safe": 0.05, "spam": 0.95}]
    )
