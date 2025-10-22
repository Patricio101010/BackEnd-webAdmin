from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    Nombre: str
    Email: EmailStr
    Telefono: Optional[str] = None
    Estado: Optional[str] = "A"

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    IdUsuario: int
    FechaCreacion: datetime

    class Config:
        orm_mode = True
