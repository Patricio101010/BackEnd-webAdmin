 # Rutas organizadas por módulo
 from fastapi import APIRouter,depends, HTTPException,status
 from services.usuarios_service import UsuariosService
 from models.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioOut
 from api.dependencies import get_usuarios_service

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/", response_model=UsuarioOut)
async def create_user(user: UsuarioCreate, service: UsuariosService = Depends(get_usuarios_service)):
    return await service.create_user(user)

@router.put("/{user_id}", response_model=UsuarioOut)
async def update_user(user_id: int, user: UsuarioUpdate, service: UsuariosService = Depends(get_usuarios_service)):
    return await service.update_user(user_id, user)

@router.delete("/{user_id}", response_model=UsuarioOut)
async def delete_user(user_id: int, service: UsuariosService = Depends(get_usuarios_service)):
    return await service.delete_user(user_id)
