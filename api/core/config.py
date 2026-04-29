from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from dotenv import find_dotenv

class Settings(BaseSettings):
    DATABASE_URL: str
    #Pydantic automatically parses CSV strings into lists, so we don't need to use split()
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]
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
    
    model_config = SettingsConfigDict(env_file=find_dotenv(), 
                                      env_file_encoding="utf-8",
                                      extra="ignore")

settings = Settings()