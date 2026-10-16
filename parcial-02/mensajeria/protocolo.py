"""
PARCIAL 2 - Nivel 1 (20 pts) · Framing

TCP es un flujo de bytes, no de mensajes. Cada mensaje viaja así:

    4 bytes con la longitud del cuerpo (big-endian)  +  el cuerpo en UTF-8

Complete los TODO. No cambie los nombres ni las firmas: las pruebas, el
servidor y los clientes importan estas tres funciones.

Requisitos:
  1. El prefijo es struct.pack("!I", n), donde n es la longitud EN BYTES del
     cuerpo ya codificado.
  2. recibir_exacto llama a recv() EN BUCLE hasta completar los n bytes.
  3. UTF-8 explícito al codificar y al decodificar.
  4. Si recv() devuelve bytes vacíos, la conexión se cerró: se devuelve None.

Se comprueba con:   python3 prueba_n1.py   (desde la carpeta parcial2/)
"""

import socket
import struct


def recibir_bytes(sock, cantidad):
    buffer = bytearray()

    while len(buffer) < cantidad:
        bloque = sock.recv(cantidad - len(buffer))

        if bloque == b"":
            return None

        buffer += bloque

    return bytes(buffer)


def enviar_mensaje(sock: socket.socket, mensaje: str) -> None:
    """Envía un mensaje UTF-8 precedido por su tamaño."""
    datos = mensaje.encode("utf-8")
    cabecera = struct.pack("!I", len(datos))

    sock.sendall(cabecera + datos)


def recibir_mensaje(sock: socket.socket) -> str | None:
    """Lee un mensaje recibido y devuelve su contenido como texto."""

    cabecera = recibir_bytes(sock, 4)
    if cabecera is None:
        return None

    tamano = struct.unpack("!I", cabecera)[0]

    datos = recibir_bytes(sock, tamano)
    if datos is None:
        return None

    return datos.decode("utf-8")