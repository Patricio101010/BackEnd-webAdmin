from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User

async def create_user(db: AsyncSession, name: str, email: str):
    new_user = User(name=name, email=email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
