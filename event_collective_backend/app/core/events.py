from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine, init_models


def register_events(app: FastAPI) -> None:
    @app.on_event("startup")
    def startup_event() -> None:
        # Ensure DB schema is present and DB is reachable (SYNC engine)
        init_models()
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

    @app.on_event("shutdown")
    def shutdown_event() -> None:
        # Nothing special needed for sync engine
        pass
