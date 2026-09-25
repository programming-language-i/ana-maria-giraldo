### C2. Tres tareas "concurrentes". R. No se ve la concurrencia porque el método `start()` de la clase `Tarea` está bloqueando la ejecución del hilo principal durante 1 segundo antes de imprimir el mensaje. Esto hace que las tareas se ejecuten de manera secuencial en lugar de concurrente, ya que cada tarea espera a que la anterior termine antes de continuar. Se cambia start por run para que se ejecute de manera concurrente.

import threading
import time


class Tarea(threading.Thread):
    def run(self):
        time.sleep(1)
        print(self.name, "lista")


inicio = time.perf_counter()
tareas = [Tarea(name=f"t{i}") for i in range(3)]
for t in tareas:
    t.start()
print(f"{time.perf_counter() - inicio:.1f} s")
for t in tareas:
    t.join()