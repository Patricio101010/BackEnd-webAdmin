# database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.models.user import Base  # tu modelo base

DATABASE_URL = "postgresql+asyncpg://admin:admin@localhost:5432/mi_bd"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Crear tablas
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
