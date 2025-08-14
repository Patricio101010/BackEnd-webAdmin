from fastapi import FastAPI
from app.routes import user
from app.database import init_db

app = FastAPI()

app.include_router(user.router)

@app.on_event("startup")
async def startup():
    await init_db()
