"""
Inference service for spam classification
"""
import logging
import numpy as np
from typing import Tuple, Dict

from app.models.model_loader import model_loader

logger = logging.getLogger(__name__)


class SpamClassifier:
    """Service class for spam email classification"""
    
    def __init__(self):
        """Initialize the classifier with the loaded model"""
        self.model = model_loader.model
        self.classes = ['safe', 'spam']  # Assuming binary classification
        
    def predict(self, text: str) -> Tuple[str, float, Dict[str, float]]:
        """
        Predict whether an email is spam or safe
        
        Args:
            text: Email text to classify
            
        Returns:
            Tuple of (prediction, confidence, probabilities)
            - prediction: 'spam' or 'safe'
            - confidence: confidence score for the prediction
            - probabilities: dict with probability for each class
        """
        try:
            # Get prediction and probabilities
            prediction_idx = self.model.predict([text])[0]
            probabilities = self.model.predict_proba([text])[0]
            
            # Map to class labels
            prediction = self.classes[prediction_idx]
            confidence = float(probabilities[prediction_idx])
            
            # Create probability dictionary
            prob_dict = {
                self.classes[i]: float(prob) 
                for i, prob in enumerate(probabilities)
            }
            
            logger.info(
                f"Prediction: {prediction} (confidence: {confidence:.2f})"
            )
            
            return prediction, confidence, prob_dict
            
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            raise Exception(f"Failed to make prediction: {str(e)}")


# Global classifier instance
spam_classifier = SpamClassifier()
