from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add the backend directory to sys.path
# This allows importing from the backend package
sys.path.append(os.path.join(os.path.dirname(__file__), '../backend'))

from app.main import app

# Vercel Serverless Function handler
# Vercel will look for 'app' variable by default
