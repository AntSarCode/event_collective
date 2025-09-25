from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Event Collective API"
    debug: bool = False

    # security / auth
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # database
    database_url: str

    # cors
    allowed_origins: str | None = None  # comma-separated list in env

    # pydantic v2 settings config
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

