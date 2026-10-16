"""
PARCIAL 2 - Nivel 2 · Servidor concurrente

    python3 -m mensajeria.servidor            escucha en el puerto 8000
    python3 -m mensajeria.servidor 8050       o en el que se le diga

Tal como está, el servidor acepta conexiones y no hace nada con ellas. Falta
el hilo por conexión y la atención del cliente.

Requisitos:
  1. Un hilo por conexión. El hilo principal solo acepta.
  2. La primera trama del cliente es su nombre. El servidor responde "OK" y lo
     registra, o responde "ERROR: nombre en uso" y cierra la conexión.
  3. Cada trama siguiente se retransmite a todos los demás como
     "emisor: contenido".
  4. El envío va FUERA del lock: se copia la lista de destinatarios bajo el
     lock y se envía después.
  5. Una desconexión no tumba nada: si un cliente se va, con aviso o a la
     fuerza, su entrada se borra del registro y los demás siguen. Un
     destinatario al que ya no se puede enviar también se retira.
  6. SO_REUSEADDR y `with` para los sockets.

Se comprueba con:   python3 prueba_n2.py   (desde la carpeta parcial2/)

Nivel 3: copie este archivo, ya resuelto, a mensajeria/servidor_json.py y
trabaje sobre la copia.
"""

import socket
import sys
import threading

from mensajeria.protocolo import enviar_mensaje, recibir_mensaje
from mensajeria.registro import RegistroClientes

HOST = "127.0.0.1"
PUERTO = 8000

bloqueo_envio = threading.Lock()


def enviar_a_todos(
    registro: RegistroClientes, usuario: str, mensaje_texto: str
) -> None:
    """Reenvía un mensaje a todos los clientes excepto al remitente."""
    
    contenido = f"{usuario}: {mensaje_texto}"

    with bloqueo_envio:
        for _, conexion in registro.destinatarios(excepto=usuario):
            try:
                enviar_mensaje(conexion, contenido)
            except OSError:
                pass


def gestionar_cliente(
    conexion: socket.socket,
    direccion: tuple[str, int],
    registro: RegistroClientes,
) -> None:
    """Gestiona la comunicación de un cliente."""

    usuario = None
    conectado = False

    try:
        usuario = recibir_mensaje(conexion)

        if usuario is None:
            return

        if not usuario.strip():
            with bloqueo_envio:
                enviar_mensaje(conexion, "ERROR")
            return

        with bloqueo_envio:
            conectado = registro.insertar(usuario, conexion)

            if not conectado:
                enviar_mensaje(conexion, "ERROR: nombre en uso")
                return

            enviar_mensaje(conexion, "OK")

        print(f"{usuario} conectado desde {direccion}")

        while True:
            mensaje = recibir_mensaje(conexion)

            if mensaje is None:
                break

            enviar_a_todos(registro, usuario, mensaje)

    except (OSError, UnicodeDecodeError) as e:
        print(f"Error con {direccion}: {e}")

    finally:
        if conectado:
            registro.borrar(usuario)
            print(f"{usuario} desconectado")

        conexion.close()


def main() -> None:
    puerto_actual = int(sys.argv[1]) if len(sys.argv) > 1 else PUERTO

    registro = RegistroClientes()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, puerto_actual))
        servidor.listen()

        print(f"Servidor escuchando en {HOST}:{puerto_actual}")

        while True:
            conexion, direccion = servidor.accept()

            threading.Thread(
                target=gestionar_cliente,
                args=(conexion, direccion, registro),
                daemon=True,
            ).start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServidor detenido")
