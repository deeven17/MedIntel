# backend/api/index.py
import os
import sys

# Current folder (backend/api) ni sys.path ki add cheyyi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main import app
    print("Successfully imported app from main.py")  # debug kosam
except ImportError as e:
    print(f"IMPORT ERROR: {str(e)}")
    raise
except Exception as e:
    print(f"OTHER ERROR: {str(e)}")
    raise