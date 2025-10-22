from fastapi import FastAPI
from app.database import engine, Base
from app.routes import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Usuarios")

app.include_router(user_routes.router)
