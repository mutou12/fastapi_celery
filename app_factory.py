from fastapi import FastAPI
from celery import Celery
from config import get_settings

def create_celery(settings) -> Celery:
    # 尝试创建Celery实例
    try:
        # 创建Celery实例，传入应用名称、结果后端和消息代理
        celery = Celery(
            settings.APP_NAME,
            backend=settings.CELERY_RESULT_BACKEND,
            broker=settings.CELERY_BROKER_URL,
        )
        # 返回Celery实例
        return celery
    # 捕获异常
    except Exception as e:
        # 打印异常信息
        print(f"Error creating Celery instance: {e}")
        # 抛出异常
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