
### C3. Un pool de procesos sin guarda. En el proceso pool, cada tarea se ejecuta en un proceso separado y no se guarda el resultado de la función `cuadrado`. Por lo tanto, el programa imprime una lista vacía `[]` porque no hay resultados que mostrar. Para obtener los resultados, se debe almacenar el resultado de `pool.map()` en una variable y luego imprimir esa variable.


from concurrent.futures import ProcessPoolExecutor


def cuadrado(n):
    return n * n

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as pool:
        print(list(pool.map(cuadrado, range(4))))