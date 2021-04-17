"""
Definiciones de los diferentes tipos de visualizadores de las variables del clima
"""

from .iobservador import *
from .iobservable import *


class VisualizadorCondicionesActuales(Observador, Visualizador):
    '''
    Visualizador de condiciones actuales de datos climáticos
    '''
    def __init__(self, datos_clima):
        self._humedad = None
        self._temperatura = None
        self._presion = None

        self._datos_clima = datos_clima
        datos_clima.registrar_observador(self)
        return

    def actualizar(self, temperatura, humedad, presion):
        self._humedad = humedad
        self._temperatura = temperatura
        self.visualizar()
        return

    def visualizar(self):
        print("Condiciones actuales: " + str(self._temperatura) +
              " C grados y " + str(self._humedad) + " % de humedad")
        return


class VisualizadorPronostico(Observador, Visualizador):

    def __init__(self, datos_clima):
        self._humedad = None
        self._ultima_medicion_humedad = None

        self._datos_clima = datos_clima
        datos_clima.registrar_observador(self)
        return

    def actualizar(self, temperatura, humedad, presion):
        self._ultima_medicion_humedad = self._humedad
        self._humedad = humedad
        self.visualizar()
        return

    def visualizar(self):

        if self._ultima_medicion_humedad is None:
            print("No hay pronostico es la primer medición")
            return

        if self._humedad > self._ultima_medicion_humedad:
            print("Tiempo mejorando")

        elif self._humedad == self._ultima_medicion_humedad:
            print("Sigue todo igual")

        elif self._humedad < self._ultima_medicion_humedad:
            print("Puede ser que refresque")
        return


class VisualizadorEstadisticas(Observador, Visualizador):

    def __init__(self, datos_clima):

        self._temperatura_maxima = 0.0
        self._temperatura_minima = 200
        self._temperatura_sum = 0.0
        self._cantidad_lecturas = 0

        self._datos_clima = datos_clima
        datos_clima.registrar_observador(self)
        return

    def actualizar(self, temperatura, humedad, presion):

        self._temperatura_sum += temperatura
        self._cantidad_lecturas += 1

        if temperatura > self._temperatura_maxima:
            self._temperatura_maxima = temperatura

        if temperatura < self._temperatura_minima:
            self._temperatura_minima = temperatura

        self.visualizar()
        return

    def visualizar(self):
        print("Temperatura Prom/Max/Min: "
              + str(self._temperatura_sum / self._cantidad_lecturas) + "/"
              + str(self._temperatura_maxima) + "/"
              + str(self._temperatura_minima))
        return


class VisualizadorIndiceCalor(Observador, Visualizador):

    def __init__(self, datos_clima):

        self._indice_calor = 0.0

        self._datos_clima = datos_clima
        datos_clima.registrar_observador(self)
        return

    def _calcular_indice_calor(self, t, rh):

        indice_calor = (16.923 + (0.185212 * t)) + \
                    (5.37941 * rh) - \
                    (0.100254 * t * rh) + \
                    (0.00941695 * (t * t)) + \
                    (0.00728898 * (rh * rh)) + \
                    (0.000345372 * (t * t * rh)) - \
                    (0.000814971 * (t * rh * rh)) + \
                    (0.0000102102 * (t * t * rh * rh)) - \
                    (0.000038646 * (t * t * t)) + \
                    (0.0000291583 * (rh * rh * rh)) + \
                    (0.00000142721 * (t * t * t * rh)) + \
                    (0.000000197483 * (t * rh * rh * rh)) - \
                    (0.0000000218429 * (t * t * t * rh * rh)) + \
                    (0.000000000843296 * (t * t * rh * rh * rh)) - \
                    (0.0000000000481975 * (t * t * t * rh * rh * rh))

        return indice_calor

    def actualizar(self, temperatura, humedad, presion):

        self._indice_calor = self._calcular_indice_calor(temperatura,
                                                         humedad)
        self.visualizar()
        return

    def visualizar(self):

        print("Indice de calor: " + str(self._indice_calor) + "\n")
        return
