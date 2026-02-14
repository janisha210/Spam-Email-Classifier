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
    
    def __init__(self, model_filename: str = "spam_model.pkl"):
        """
        Initialize the model loader
        
        Args:
            model_filename: Name of the pickled model file
        """
        self.model_filename = model_filename
        self._model = None
        self.load_error = None
        
    def load_model(self):
        """
        Load the trained model from disk, searching multiple locations.
        """
        if self._model is not None:
            return self._model
            
        # List of potential paths to check
        # 1. Standard backend path relative to this file
        # 2. Vercel: root/backend/spam_model.pkl (relative to CWD)
        # 3. Vercel: root/spam_model.pkl (if flattened)
        # 4. Immediate CWD
        base_path = Path(__file__).resolve().parent.parent.parent
        
        potential_paths = [
            base_path / self.model_filename,                 # backend/spam_model.pkl (from structure)
            Path.cwd() / "backend" / self.model_filename,    # backend/spam_model.pkl (from CWD)
            Path.cwd() / self.model_filename,                # spam_model.pkl (in CWD)
            Path("/var/task/backend") / self.model_filename, # Vercel Lambda specific
        ]
        
        checked_paths = []
        
        try:
            found_path = None
            for path in potential_paths:
                checked_paths.append(str(path))
                if path.exists():
                    found_path = path
                    break
            
            if not found_path:
                # Log listing of current directory for debugging
                cwd_files = list(Path.cwd().glob('**/*'))
                raise FileNotFoundError(
                    f"Model file '{self.model_filename}' not found. Checked: {checked_paths}. "
                    f"CWD: {Path.cwd()}. Files in CWD: {[str(f) for f in cwd_files[:20]]}"
                )
        
            logger.info(f"Loading model from {found_path}")
            with open(found_path, 'rb') as f:
                self._model = pickle.load(f)
            logger.info("Model loaded successfully")
            self.load_error = None
            return self._model
            
        except Exception as e:
            self.load_error = str(e)
            logger.error(f"Failed to load model: {str(e)}")
            raise Exception(f"Model load failed: {str(e)}")
    
    @property
    def model(self):
        """Get the loaded model (lazy loading)"""
        if self._model is None:
            try:
                self.load_model()
            except:
                pass # check load_error instead
        return self._model
    
    def is_loaded(self) -> bool:
        """Check if model is loaded"""
        return self._model is not None


# Global model loader instance
model_loader = ModelLoader()
