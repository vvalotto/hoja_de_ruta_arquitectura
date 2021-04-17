"""
Ejemplo de uso del patron Observer
Programa principal
"""

from hf_estacion_clima.datos_clima import *
from hf_estacion_clima.visualizadores import *
from hf_estacion_clima.mediciones import  *
import time

t = Temperatura()
h = Humedad()
p = Presion()


# Se crea la instancia de la estación de medición
estacion_datos_clima = DatosClima()
visores = []

# Se crea un visualizador de condiciones climaticas y se suscribe a la estación
visores.append(VisualizadorCondicionesActuales(estacion_datos_clima))

# Recupera las mediciones de los parametros climaticos
while True:
    t.leer()
    p.leer()
    h.leer()


    # La estación de clima actualiza los datos del clima
    print("")
    estacion_datos_clima.poner_mediciones(t.medicion, h.medicion, p.medicion)

    time.sleep(5)
