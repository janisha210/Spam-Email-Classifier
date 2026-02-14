"""
Model loader module for loading the trained spam classifier
"""
import pickle
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


class ModelLoader:
    """Handles loading and caching of the trained ML model"""
    
    def __init__(self, model_path: str = "spam_model.pkl"):
        """
        Initialize the model loader
        
        Args:
            model_path: Path to the pickled model file
        """
        # Use absolute path relative to this file to ensure model is found
        # backend/app/models/model_loader.py -> backend/spam_model.pkl
        base_dir = Path(__file__).resolve().parent.parent.parent
        self.model_path = base_dir / model_path
        self._model = None
        
    def load_model(self):
        """
        Load the trained model from disk
        
        Returns:
            The loaded scikit-learn pipeline
            
        Raises:
            FileNotFoundError: If model file doesn't exist
            Exception: If model loading fails
        """
        if self._model is not None:
            logger.info("Returning cached model")
            return self._model
            
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model file not found at {self.model_path}. "
                "Please ensure spam_model.pkl exists in the backend directory."
            )
        
        try:
            logger.info(f"Loading model from {self.model_path}")
            with open(self.model_path, 'rb') as f:
                self._model = pickle.load(f)
            logger.info("Model loaded successfully")
            return self._model
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise Exception(f"Error loading model: {str(e)}")
    
    @property
    def model(self):
        """Get the loaded model (lazy loading)"""
        if self._model is None:
            self.load_model()
        return self._model
    
    def is_loaded(self) -> bool:
        """Check if model is loaded"""
        return self._model is not None


# Global model loader instance
model_loader = ModelLoader()
