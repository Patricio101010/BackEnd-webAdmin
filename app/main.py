# main.py
from fastapi import FastAPI
from api.routes import tipo_cuenta   # importa tus rutas

app = FastAPI(title="Finanzas Personales API")

# registrar rutas
app.include_router(tipo_cuenta.router)

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}
