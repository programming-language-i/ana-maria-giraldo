### B3. Una excepción en el pool. R. El metodo pool.submit() lanza una excepción de tipo ZeroDivisionError, ya que se está intentando dividir un número entre cero. La excepción se propaga al hilo principal y no se maneja dentro del hilo del pool, lo que provoca que el programa termine con un error.

from concurrent.futures import ThreadPoolExecutor


def dividir(a, b):
    return a / b


with ThreadPoolExecutor() as pool:
    futuro = pool.submit(dividir, 1, 0)
print("listo")