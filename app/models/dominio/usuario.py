from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime
from app.database import Base

class Usuario(Base):
    __tablename__ = "Usuario"
    
    IdUsuario = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String, nullable=False)
    FechaCreacion = Column(DateTime, default=datetime.utcnow)
    Email = Column(String, nullable=False, unique=True, index=True)
    Telefono = Column(String, nullable=True)
    Estado = Column(String, default="A")  # A: Activo, I: Inactivo

