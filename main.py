from fastapi import FastAPI
from app.routes import user_routes

app = FastAPI(title="Mi API con FastAPI y SQLAlchemy")

# Incluir rutas
app.include_router(user_routes.router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "API corriendo correctamente"}
