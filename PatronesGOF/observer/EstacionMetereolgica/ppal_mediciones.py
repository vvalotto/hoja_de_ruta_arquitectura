import time
from hf_estacion_clima.mediciones import *


t = Temperatura()
h = Humedad()
p = Presion()

while True:
    t.leer()
    p.leer()
    h.leer()

    print(str(t.medicion) + " grados")
    print(str(h.medicion) + " %")
    print(str(p.medicion) + 'HP')

    time.sleep(5)