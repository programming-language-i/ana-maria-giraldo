## B5. Procesos y una lista global. R. Es necesaria una lista vacía para cada subproceso se ejecute en un espacio de memoria completamente aislado y opera sobre su propia copia de la lista resultados, dejando la variable global del proceso principal intacta.

import multiprocessing


def calcular(n, resultados):
    resultados.append(n * n)

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        resultados = manager.list() 
        procesos = [multiprocessing.Process(target=calcular, args=(n, resultados)) for n in range(4)]
        
        for p in procesos:
            p.start()
        for p in procesos:
            p.join()
            
        print(list(resultados))