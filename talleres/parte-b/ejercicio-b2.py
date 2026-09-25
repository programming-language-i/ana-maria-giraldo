### B2. Daemon con `finally` R. El programa tarda unos 0.5 segundos en ejecutarse. Porque el hilo se ejecuta como un hilo daemon, lo que significa que el hilo principal no espera a que termine el hilo daemon antes de finalizar la ejecución del programa. Por lo tanto, el hilo daemon se interrumpe antes de que pueda completar su tarea y ejecutar el bloque `finally`.

import threading
import time


def guardar():
    try:
        time.sleep(2)
        print("guardado")
    finally:
        print("archivo cerrado")


threading.Thread(target=guardar, daemon=True).start()
time.sleep(0.5)
print("fin")