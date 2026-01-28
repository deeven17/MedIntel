# backend/api/index.py
# This file acts as the entry point for Vercel serverless functions
# Import your main FastAPI app from the actual main.py

from main import app  # ← nee main.py lo unna 'app' ni import chestundi

# Vercel requires this exact name for Python functions
# No need to run uvicorn here – Vercel handles it