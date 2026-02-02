from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    app_name: str = "Finanza API"

    # SQLite file
    sqlite_db: str = "finanza.db"

    @property
    def database_url(self) -> str:
        return f"sqlite:///{BASE_DIR}/{self.sqlite_db}"

    jwt_secret: str = "CHANGE_ME"
    jwt_algorithm: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
