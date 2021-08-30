from .senial import *


class FactorySenial(object):

    def __int__(self):
        pass

    @staticmethod
    def obtener_senial(tipo_senial, tamanio):

        tamanio = int(tamanio)
        senial = None
        if tipo_senial == 'basica':
            senial = SenialLista(tamanio)

        elif tipo_senial == 'pila':
            senial = SenialPila(tamanio)

        elif tipo_senial == 'cola':
            senial = SenialCola(tamanio)

        return senial
