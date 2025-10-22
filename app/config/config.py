# Variables de entorno y configuración

"""Configuración de la aplicación."""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database configuration    
    DATABASE_URL: str = "sqlite:///./test.db"

    # security
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"


ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

# app
app_name: str = "FinanzasAPI"
debug_mode: bool = False


class Config:
    env_file = ".env"

    settings = Settings()
