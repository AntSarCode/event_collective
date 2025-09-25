from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.core.security import get_password_hash

async def init_db(session: AsyncSession):
    admin_exists = await session.execute(
        select(User).filter(User.is_admin == True)
    )
    if not admin_exists.scalars().first():
        admin = User(
            username="admin",
            email="admin@example.com",
            is_admin=True,
            hashed_password=get_password_hash("admin123")
        )
        session.add(admin)
        await session.commit()
