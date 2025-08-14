from fastapi import FastAPI

app = FastAPI(
    title="Finanza Web App",
    description="API para gestión de finanzas personales",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}
