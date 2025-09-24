from app.database import SessionLocal

db = SessionLocal()

db.commit(); db.close()
