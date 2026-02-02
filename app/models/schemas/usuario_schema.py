from pydantic import BaseModel, EmailStr

# Esquemas Pydantic para la creación y respuesta de usuarios
class UsuarioCreate(BaseModel):
    email: EmailStr
    nombre: str

# Esquema para la respuesta de usuario
class UsuarioResponse(BaseModel):
    id: int
    email: EmailStr
    nombre: str
    
    # Configuración para que Pydantic pueda trabajar con objetos ORM
    class Config:
        from_attributes = True
