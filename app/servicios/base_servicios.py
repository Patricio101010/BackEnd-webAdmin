# Servicio base con operaciones CRUD
from typing import Generic, TypeVar, List, Optional
from repository.base_repositorio import BaseRepositorio

modeltype = TypeVar('modeltype', bound=BaseRepositorio)
createschema = TypeVar('createschema')
updateschema = TypeVar('updateschema')

class BaseServicios(Generic[modeltype, createschema, updateschema]):
    def __init__(self, repositorio: BaseRepositorio):
        self.repositorio = repositorio

    async def get_all(self) -> List[modeltype]:
        return await self.repositorio.get_all()

    async def get_by_id(self, id: int) -> Optional[modeltype]:
        return await self.repositorio.get_by_id(id)

    async def create(self, obj_in: createschema) -> modeltype:
        return await self.repositorio.create(obj_in)

    async def update(self, id: int, obj_in: updateschema) -> Optional[modeltype]:
        return await self.repositorio.update(id, obj_in)

    async def delete(self, id: int) -> Optional[modeltype]:
        return await self.repositorio.delete(id)