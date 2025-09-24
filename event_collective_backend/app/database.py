import os
from typing import AsyncGenerator, Optional
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

def _to_asyncpg_url(url: Optional[str]) -> str:
    """Ensure the DATABASE_URL is asyncpg-compatible for SQLAlchemy async usage.
    Accepts common forms like `postgres://` or `postgresql://` and upgrades to
    `postgresql+asyncpg://` if needed.
    """
    if not url:
        raise RuntimeError("DATABASE_URL is not set. Provide it via environment variables.")

    # Render commonly supplies postgresql://
    if url.startswith("postgres://"):
        # SQLAlchemy doesn't recognize postgres://; upgrade scheme
        return url.replace("postgres://", "postgresql+asyncpg://", 1)

    if url.startswith("postgresql://") and "+asyncpg" not in url:
        return url.replace("postgresql://", "postgresql+asyncpg://", 1)

    return url

DATABASE_URL = _to_asyncpg_url(os.getenv("DATABASE_URL"))

POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "5"))
MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", "10"))
POOL_PRE_PING = os.getenv("DB_POOL_PRE_PING", "true").lower() != "false"

engine = create_async_engine(
    DATABASE_URL,
    future=True,
    pool_pre_ping=POOL_PRE_PING,
    pool_size=POOL_SIZE,
    max_overflow=MAX_OVERFLOW,
)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency that yields an AsyncSession and ensures closure."""
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            # Explicit close is safe/clear; context manager also handles it
            await session.close()

async def init_models() -> None:
    """Create tables on startup if they don't exist.
    Import models inside the function so metadata is fully populated before create_all.
    """
    # Import all models to register with Base.metadata
    from app.models import calendar, contact_message, event, gallery, message, review, service, user  # noqa: F401

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

__all__ = [
    "engine",
    "SessionLocal",
    "Base",
    "get_db",
    "init_models",
]
