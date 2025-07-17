from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import get_settings

settings = get_settings()

# Create Async Engine
engine = create_async_engine(settings.database_url, echo=settings.debug)

# Create Session Factory
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

# Dependency
async def get_db():
    async with async_session() as session:
        yield session

__all__ = ["engine", "async_session", "get_db"]
