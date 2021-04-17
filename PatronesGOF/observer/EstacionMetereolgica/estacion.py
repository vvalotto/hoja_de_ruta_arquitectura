from hf_estacion_clima.mediciones import *
import time


class DatosClimaticos:

    def __init__(self):
        self._temperatura = Temperatura()
        self._humedad = Humedad()
        self._presion = Presion()

    def obtener_medicion(self):
        while True:
            self._temperatura.leer()
            self._humedad.leer()
            self._presion.leer()

            #visualizador_condiciones_actuales.actualizar()
            #visualizador_estaditicas.actualizar()
            #visualizador_pronostico.actualizar()

            time.sleep(5)



