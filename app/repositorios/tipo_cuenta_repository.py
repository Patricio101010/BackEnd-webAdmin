# repositories/tipo_cuenta_repository.py
from .base_repository import BaseRepository
from modelos.domain.tipo_cuenta import TipoCuenta
from modelos.schemas.tipo_cuenta_schema import TipoCuentaCreate

class TipoCuentaRepository(BaseRepository):
    def get_all(self, Activos: bool):
        try:
            Idestado = 'A'
            query = self.db.query(TipoCuenta)
            if Activos is not None:
                if Activos:
                    query = query.filter(TipoCuenta.Estado == Idestado)
                else:
                    query = query.filter(TipoCuenta.Estado != Idestado)
            return query.all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al consultar tipos de cuenta: {str(e)}")

    def get_by_id(self, id_tipo_cuenta: int):
        try:
            return self.db.query(TipoCuenta).filter(TipoCuenta.IdTipoCuenta == id_tipo_cuenta).first()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al consultar tipo de cuenta: {str(e)}")

    def create(self, tipo_cuenta: TipoCuentaCreate):
        nuevo_tipo = TipoCuenta(
            Descripcion=tipo_cuenta.Descripcion,
            Estado=tipo_cuenta.Estado
        )
        self.db.add(nuevo_tipo)
        self.db.commit()
        self.db.refresh(nuevo_tipo)
        return nuevo_tipo

    def update(self, id_tipo_cuenta: int, tipo_cuenta: TipoCuentaCreate):
        existente = self.get_by_id(id_tipo_cuenta)
        if not existente:
            return None
        existente.Descripcion = tipo_cuenta.Descripcion
        existente.Estado = tipo_cuenta.Estado
        self.db.commit()
        self.db.refresh(existente)
        return existente

    def delete(self, id_tipo_cuenta: int):
        existente = self.get_by_id(id_tipo_cuenta)
        if not existente:
            return None
        self.db.delete(existente)
        self.db.commit()
        return existente
