from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator

class Settings(BaseSettings):
    DATABASE_URL: str
    ALLOWED_ORIGINS: str = "http://localhost:3000"

    @field_validator("DATABASE_URL")
    @classmethod
    def fix_postgres_suffix(cls, v: str) -> str:
        pass
        # TODO:
#     DATABASE_URL = os.getenv("DATABASE_URL")
# if not DATABASE_URL:
#     print("Error: Database URL not found")
# elif DATABASE_URL.startswith("postgresql://"):
#     # SQLAlchemy requires postgresql+psycopg2:// for Postgres
#     DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)