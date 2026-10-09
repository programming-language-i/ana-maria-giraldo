import pickle

mensaje = { "emisor": "felipe", "contenido": "Hola", "etiqueta": ("a", "b")}

datos = pickle.dumps(mensaje)

print(datos)

print("\n")

copia= pickle.loads(datos)
print(copia)