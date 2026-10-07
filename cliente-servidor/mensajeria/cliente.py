import socket
import threading

HOST = "127.0.0.1"
PORT = 8000


def recibir_mensajes(cliente):
    while True:
        try:
            datos = cliente.recv(1024)

            if not datos:
                print("\nSe perdió la conexión con el servidor.")
                break

            print(f"\n{datos.decode('utf-8')}")
            print("> ", end="", flush=True)

        except ConnectionResetError:
            print("\nEl servidor cerró la conexión.")
            break

        except Exception as e:
            print(f"\nError: {e}")
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    try:
        cliente.connect((HOST, PORT))

        nombre = input("Ingresa tu nombre: ")

        cliente.sendall(nombre.encode("utf-8"))

        print("Conectado al servidor.")
        print("Escribe mensajes. Usa '0' para salir.")

        hilo = threading.Thread(
            target=recibir_mensajes,
            args=(cliente,),
            daemon=True
        )
        hilo.start()

        while True:
            mensaje = input("> ")

            if mensaje == "0":
                print("Desconectando...")
                break

            cliente.sendall(mensaje.encode("utf-8"))

    except ConnectionRefusedError:
        print("No se pudo conectar al servidor.")

    except Exception as e:
        print(f"Error: {e}")