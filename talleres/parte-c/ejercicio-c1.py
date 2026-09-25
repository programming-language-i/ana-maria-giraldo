### C1. Descarga por herencia. R. Hay error de sintaxis, se debe agregar `super().__init__()` en el método `__init__` de la clase `Descarga` para inicializar correctamente la clase base `Thread`. Esto asegura que el hilo se configure correctamente antes de iniciar la ejecución del método `run`.

import threading


class Descarga(threading.Thread):
    def __init__(self, archivo):
        super().__init__()
        self.archivo = archivo

    def run(self):
        print("descargando", self.archivo)

Descarga("a.zip").start()