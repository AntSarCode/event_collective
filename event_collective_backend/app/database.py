import os
from typing import Optional
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

def _normalize_pg_url(url: Optional[str]) -> str:
    if not url:
        raise RuntimeError('DATABASE_URL is not set.')
    if url.startswith('postgres://'):
        url = 'postgresql://' + url[len('postgres://'):]
    u = urlparse(url)
    if (u.hostname or '').endswith('render.com'):
        q = dict(parse_qsl(u.query))
        q.setdefault('sslmode', 'require')
        url = urlunparse(u._replace(query=urlencode(q)))
    if not url.startswith('postgresql+psycopg2://'):
        url = url.replace('postgresql://', 'postgresql+psycopg2://')
    return url

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(_normalize_pg_url(DATABASE_URL), pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_models() -> None:
    from app.models import calendar, contact_message, event, gallery, message, review, service, user  # noqa: F401
    Base.metadata.create_all(bind=engine)

__all__ = ['engine', 'SessionLocal', 'Base', 'get_db', 'init_models']
