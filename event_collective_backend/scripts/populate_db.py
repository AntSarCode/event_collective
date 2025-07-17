from app.database import engine
from app.models import base
import asyncio

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(base.Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())

