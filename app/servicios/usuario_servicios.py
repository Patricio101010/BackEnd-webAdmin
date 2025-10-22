from typing import Generic, TypeVar, List, Optional
from repository.usuario_repositorio import UsuarioRepositorio
from servicios.base_servicios import BaseServicios
from models.schemas.usuario_schema import UsuarioCreateSchema, UsuarioUpdateSchema, usuarioReponse
from core.seguridad import hash_password

class UsuarioServicios(BaseServicios[UsuarioRepositorio, UsuarioCreateSchema, UsuarioUpdateSchema]):
    def __init__(self, repositorio: UsuarioRepositorio):
        super().__init__(repositorio)

    async def create_user(self, user_create: UsuarioCreateSchema) -> usuarioReponse:
        user_create.password = hash_password(user_create.password)
        user = await self.repositorio.create(user_create)
        return usuarioReponse.from_orm(user)

    async def update_user(self, user_id: int, user_update: UsuarioUpdateSchema) -> Optional[usuarioReponse]:
        user = await self.repositorio.get_by_id(user_id)
        if not user:
            return None
        user_update.password = hash_password(user_update.password)
        await self.repositorio.update(user_id, user_update)
        return usuarioReponse.from_orm(user)

    async def delete_user(self, user_id: int) -> Optional[usuarioReponse]:
        user = await self.repositorio.get_by_id(user_id)
        if not user:
            return None
        await self.repositorio.delete(user_id)
        return usuarioReponse.from_orm(user)
