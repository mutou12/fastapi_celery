from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    APP_NAME: str = "hk with FastAPI and Celery"
    CELERY_BROKER_URL: str = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND: str = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    return Settings()
