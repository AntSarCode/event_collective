from fastapi import FastAPI
from app.database import engine
from app.core.init_db import init_db
from sqlalchemy.ext.asyncio import AsyncSession


def register_events(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        async with AsyncSession(bind=engine) as session:
            await init_db(session)

    @app.on_event("shutdown")
    async def shutdown_event():
        print("Shutting down cleanly.")
