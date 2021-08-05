"""
Configura la clase que se usara
"""
from procesador.procesador import *


def definir_procesador():
    """
    Los procesador son:
    Procesador Amplificador
    Procesador con Umbral
    :return:
    """
    return ProcesadorAmplificador(4)


class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    # Se configura el tipo de procesador
    procesador = definir_procesador()

    def __init__(self):
        pass
