from functools import lru_cache
import pydantic


class Settings(pydantic.BaseSettings):
    app_name: str = "Event Collective Backend"
    debug: bool = False
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


