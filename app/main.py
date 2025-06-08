# app/main.py
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# Импортируем роутер
# и корутину для создания первого суперюзера
from app.api.routers import main_router
from app.core.init_db import create_first_superuser

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутер
app.include_router(main_router)


@app.on_event("startup")
async def startup():
    await create_first_superuser()
