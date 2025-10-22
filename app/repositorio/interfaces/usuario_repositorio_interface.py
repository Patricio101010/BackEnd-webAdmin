from abs import ABC, abstractmethod
from typing import List, Optional
from models.dominio.usuario import Usuario

class UsuarioRepositorioInterface(ABC):

    @abstractmethod
    def crear_usuario(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def obtener_usuario(self, usuario_id: int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def obtener_todos_los_usuarios(self) -> List[Usuario]:
        pass

    @abstractmethod
    def actualizar_usuario(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def eliminar_usuario(self, usuario_id: int) -> None:
        pass