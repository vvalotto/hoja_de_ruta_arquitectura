"""
Fabrica de tipos de adquisidor
"""
from .adquisidor import *


class FactoryAdquisidor(object):

    @staticmethod
    def obtener_adquisidor(tipo_adquisidor, senial, params):

        adquisidor = None
        if tipo_adquisidor == 'simple':
            adquisidor = AdquisidorConsola(senial)

        elif tipo_adquisidor == 'archivo':
            ubicacion = str(params[0])
            adquisidor = AdquisidorArchivo(ubicacion, senial)

        elif tipo_adquisidor == 'senoidal':
            adquisidor = AdquisidorSenoidal(senial)

        return adquisidor
