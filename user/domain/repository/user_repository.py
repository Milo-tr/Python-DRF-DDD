from abc import ABC, abstractmethod
from user.domain.usuario import Usuario

class UserRepository(ABC):

    @abstractmethod
    def crear_usuario(self, usuario: Usuario) -> Usuario:
        ...

    @abstractmethod
    def obtener_usuarios(self, filtro: dict) -> list[Usuario]:
        ...

    @abstractmethod
    def obtener_usuario_por_id(self, usuario_id: str) -> Usuario:
        ...

    @abstractmethod
    def eliminar_usuario(self, usuario_id: str) -> None:
        ...

    @abstractmethod
    def actualizar_usuario(self, usuario: Usuario) -> Usuario:
        ...