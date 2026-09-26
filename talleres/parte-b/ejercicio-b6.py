### B6. Estado por instancia y estado de clase. R. Es necesario imprimir 3 3 6 porque total es un atributo de instancia propio de cada hilo (3 para cada uno), mientras que eventos es una lista a nivel de clase compartida por todas las instancias, acumulando así las 3 iteraciones de ambos hilos (3 + 3 = 6).

import threading


class Contador(threading.Thread):
    def _init_(self, nombre):
        super()._init_(name=nombre)
        self.total = 0
        self.eventos = [] 

    def run(self):
        for _ in range(3):
            self.total += 1
            self.eventos.append(self.name)

a, b = Contador("a"), Contador("b")

for h in (a, b):
    h.start()

for h in (a, b):
    h.join()

print(a.total, b.total, len(a.eventos))