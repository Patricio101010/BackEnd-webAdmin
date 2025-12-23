# models/schemas/tipo_cuenta_schema.py
from typing import List, Optional
from pydantic import BaseModel

class Respuesta(BaseModel):
    codigo: int
    mensaje: str
    
class TipoCuentaBase(BaseModel):
    Descripcion: str
    Estado: str

# class TipoCuentaResponse(TipoCuentaBase):
#     IdTipoCuenta: int
#     respuesta: Respuesta
    
class TipoCuentaSingleResponse(BaseModel): 
    tipoCuenta: Optional[TipoCuentaBase]
    respuesta: Respuesta
    
class TipoCuentaListResponse(BaseModel):
    tipoCuenta: Optional[List[TipoCuentaBase]]
    respuesta: Respuesta

class TipoCuentaCreate(TipoCuentaBase):
    class Config: from_attributes = True