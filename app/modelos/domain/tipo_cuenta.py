# models/domain/tipo_cuenta.py
from sqlalchemy import Column, Integer, String, CHAR
from db.database import Base

class TipoCuenta(Base):
    __tablename__ = "TipoCuenta"

    IdTipoCuenta = Column(Integer, primary_key=True, index=True)
    Descripcion = Column(String(200), nullable=False)
    Estado = Column(CHAR(1), nullable=False)
