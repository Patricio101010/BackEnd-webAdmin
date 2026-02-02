# ruta app/api/routes/health.py
from fastapi import APIRouter

# Definir el enrutador de ""health""
router = APIRouter(prefix="/health", tags=["Health"])

# Endpoint de verificación de ""health""
@router.get("/")

# Respuesta simple para indicar que el servicio está funcionando correctamente
async def health():
    return {"status": "ok"}
