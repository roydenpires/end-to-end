"""
ASGI entry point for Azure App Service.
The FastAPI app is imported from the app module.
"""

from app.main import api

# This is the ASGI application that App Service will run.
# Configure your App Service startup command to:
# gunicorn --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 app_run:api

__all__ = ["api"]
