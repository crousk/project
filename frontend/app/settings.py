from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class DatabaseSettings(BaseSettings):
    PGHOST: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: int = 5432

class Settings(DatabaseSettings):
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()