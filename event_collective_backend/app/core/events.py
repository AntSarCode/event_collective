from fastapi import FastAPI
from app.database import init_models

def register_events(app: FastAPI):
    @app.on_event("startup")
    def startup_event():
        init_models()

    @app.on_event("shutdown")
    def shutdown_event():
        print("Shutting down cleanly.")
