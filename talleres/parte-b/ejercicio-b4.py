### B4. Reiniciar un hilo. Para reiniciar un hilo, primero se debe crear un nuevo objeto de hilo y luego iniciar ese nuevo hilo. No se puede reiniciar un hilo que ya ha terminado su ejecución, por eso es necesario crear un nuevo hilo para ejecutar la misma función nuevamente.

import threading

hilo = threading.Thread(target=print, args=("hola",))

hilo.start()

hilo.join()

print(hilo.is_alive())

hilo2 = threading.Thread(target=print, args=("hola",))
hilo2.start()
hilo2.join()