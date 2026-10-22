
import socket
import threading


class RegistroClientes:
    """Administra las conexiones de los usuarios activos."""

    def __init__(self) -> None:
        self.clientes: dict[str, socket.socket] = {}
        self.lock = threading.Lock()

    def insertar(
        self,
        nombre: str,
        conexion: socket.socket,
    ) -> bool:
        """Registra al usuario si su nombre está disponible."""

        with self.lock:
            nombre_normalizado = nombre.casefold()

            for existente in self.clientes:
                if existente.casefold() == nombre_normalizado:
                    return False

            self.clientes[nombre] = conexion
            return True

    def buscar(
        self,
        nombre: str,
    ) -> socket.socket | None:
        """Busca la conexión de un usuario."""

        with self.lock:
            for existente, conexion in self.clientes.items():
                if existente.casefold() == nombre.casefold():
                    return conexion

            return None

    def borrar(self, nombre: str) -> None:
        """Elimina al usuario del registro."""

        with self.lock:
            for existente in list(self.clientes):
                if existente.casefold() == nombre.casefold():
                    del self.clientes[existente]
                    break

    def destinatarios(
        self,
        excepto: str,
    ) -> list[tuple[str, socket.socket]]:
        """Obtiene los clientes excepto el remitente."""

        with self.lock:
            return [
                (nombre, conexion)
                for nombre, conexion in self.clientes.items()
                if nombre.casefold() != excepto.casefold()
            ]
