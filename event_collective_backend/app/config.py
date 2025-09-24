from __future__ import annotations

import os
from functools import lru_cache
from typing import List, Optional

try:
    from pydantic_settings import BaseSettings  # type: ignore
except Exception:  # pragma: no cover
    from pydantic import BaseSettings  # type: ignore


class Settings(BaseSettings):
    # App basics
    ENV: str = os.getenv("ENV", "production")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me")

    # Networking
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "10000"))  # Render default

    # CORS
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")

    # Database
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")

    # Optional Integrations
    STRIPE_PUBLIC_KEY: Optional[str] = os.getenv("STRIPE_PUBLIC_KEY")
    STRIPE_SECRET_KEY: Optional[str] = os.getenv("STRIPE_SECRET_KEY")

    class Config:  # Pydantic v1
        env_file = ".env"
        case_sensitive = False

    model_config = {  # Pydantic v2
        "env_file": ".env",
        "case_sensitive": False,
    }

    @property
    def cors_origins(self) -> List[str]:
        raw = (self.ALLOWED_ORIGINS or "").strip()
        if not raw or raw == "*":
            return ["*"]
        return [o.strip() for o in raw.split(",") if o.strip()]


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Cached settings loader so we don't rebuild on every import."""
    return Settings()  # type: ignore[arg-type]


__all__ = ["Settings", "get_settings"]
