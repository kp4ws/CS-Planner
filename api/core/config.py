from typing import Union, Any
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from dotenv import find_dotenv

class Settings(BaseSettings):
    DATABASE_URL: str
    ALLOWED_ORIGINS: Union[str, list[str]] = ["http://localhost:3000"]
    PROJECT_NAME: str = "TODO: Backpack Pal API"
    VERSION: str = "0.1.0"
    APP_ENV: str = "development"
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @field_validator("DATABASE_URL")
    @classmethod
    def fix_postgres_suffix(settings_class, raw_url_value: str) -> str:
        """
        Ensures the Postgres URL uses the 'psycopg2' driver required by SQLAlchemy.
        """
        if raw_url_value and raw_url_value.startswith("postgresql://"):
            # SQLAlchemy requires postgresql+psycopg2:// for Postgres
            return raw_url_value.replace("postgresql://", "postgresql+psycopg2://", 1)
        return raw_url_value
    
    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def split_allowed_origins(settings_class, raw_csv_origins: Any) -> list[str]:
        """
        Ensures ALLOWED_ORIGINS is split into a list of strings
        """
        if isinstance(raw_csv_origins, str) and raw_csv_origins.strip():
            return [origin.strip() for origin in raw_csv_origins.split(",")]
        if isinstance(raw_csv_origins, list):
            return raw_csv_origins
        return []
    
    model_config = SettingsConfigDict(env_file=find_dotenv(), 
                                      env_file_encoding="utf-8",
                                      extra="ignore")

settings = Settings()