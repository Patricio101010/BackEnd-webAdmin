from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schema import UserCreate, UserRead
from app.services.user_service import create_user
from app.database import get_db  # más abajo lo crearemos

router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user.name, user.email)
