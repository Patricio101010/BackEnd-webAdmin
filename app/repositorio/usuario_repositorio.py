from sqlalchemy.orm import Session
from app.modelos.usuario_modelo import Usuario as UsuarioModelo 
from repositorio.base_repositorio import BaseRepositorio
from repositorio.interface.usuario_interface_repositorio import IUsuarioRepositorio

class UsuarioRepositorio(BaseRepositorio[UsuarioModelo], IUsuarioRepositorio):

    def __init__(self, db: Session):
        super().__init__(db)

    def crear_usuario(self, usuario: UsuarioModelo) -> UsuarioModelo:
        return self.crear(usuario)

    def obtener_usuario(self, usuario_id: int) -> Optional[UsuarioModelo]:
        return self.obtener(usuario_id)

    def obtener_todos_los_usuarios(self) -> List[UsuarioModelo]:
        return self.obtener_todos()

    def actualizar_usuario(self, usuario: UsuarioModelo) -> UsuarioModelo:
        return self.actualizar(usuario)

    def eliminar_usuario(self, usuario_id: int) -> None:
        usuario = self.obtener(usuario_id)
        if usuario:
            self.eliminar(usuario)
