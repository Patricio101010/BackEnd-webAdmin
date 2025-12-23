# config/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_SERVER: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_DRIVER: str

    class Config:
        env_file = "config/.env"

settings = Settings()
