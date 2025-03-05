from fastapi import FastAPI
from celery import Celery
from config import get_settings

def create_celery(settings) -> Celery:
    try:
        celery = Celery(
            settings.APP_NAME,
            backend=settings.CELERY_RESULT_BACKEND,
            broker=settings.CELERY_BROKER_URL,
        )
        return celery
    except Exception as e:
        print(f"Error creating Celery instance: {e}")
        raise

def create_app() -> FastAPI:
    app = FastAPI()

    # Load configuration
    settings = get_settings()

    # Register routers
    from routers import api_router
    app.include_router(api_router)

    # # Attach settings to the app (if needed)
    app.settings = settings
    app.celery = create_celery()
    # app.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    return app