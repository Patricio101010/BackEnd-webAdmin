from typing import Generic, TypeVar, List, Optional
from sqlalchemy.orm import Session
from db.database import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepositorio(Generic[ModelType]):

    def __init__(self, db: Session):
        self.db = db

    def crear(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def obtener(self, obj_id: int) -> Optional[ModelType]:
        return self.db.query(ModelType).filter(ModelType.id == obj_id).first()

    def obtener_todos(self) -> List[ModelType]:
        return self.db.query(ModelType).all()

    def actualizar(self, obj: ModelType) -> ModelType:
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def eliminar(self, obj: ModelType) -> None:
        self.db.delete(obj)
        self.db.commit()