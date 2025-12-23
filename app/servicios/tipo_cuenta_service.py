# services/tipo_cuenta_service.py
from repositorios.tipo_cuenta_repository import TipoCuentaRepository
from modelos.schemas.tipo_cuenta_schema import TipoCuentaCreate

class TipoCuentaService:
    def __init__(self, repo: TipoCuentaRepository):
        self.repo = repo

    def listar_tipos(self, Activos: bool):
        return self.repo.get_all(Activos)

    def obtener_tipo(self, id_tipo_cuenta: int):
        return self.repo.get_by_id(id_tipo_cuenta)

    def crear_tipo(self, tipo_data: TipoCuentaCreate):
        return self.repo.create(tipo_data)

    def actualizar_tipo(self, id_tipo_cuenta: int, tipo_data: TipoCuentaCreate):
        return self.repo.update(id_tipo_cuenta, tipo_data)

    def eliminar_tipo(self, id_tipo_cuenta: int):
        return self.repo.delete(id_tipo_cuenta)
