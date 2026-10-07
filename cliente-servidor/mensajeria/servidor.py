import socket
import threading

HOST = "127.0.0.1"
PORT = 8000

def recibir_mensajes(cliente):
    while True:
        try:
            datos = cliente.recv(1024)

            if not datos:
                print("\nConexión cerrada")
                break

            print(f"\n{datos.decode()}")
            print("> ", end="", flush=True)

        except:
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))

    nombre = input("Nombre: ")
    cliente.sendall(nombre.encode("utf-8"))

    hilo = threading.Thread(
        target=recibir_mensajes,
        args=(cliente,),
        daemon=True
    )
    hilo.start()

    while True:
        mensaje = input("> ")

        if mensaje == "0":
            break

        cliente.sendall(mensaje.encode("utf-8"))