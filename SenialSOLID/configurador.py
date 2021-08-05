"""
Configura la clase que se usara
"""
from adquisidor.adquisidor import *
from procesador.procesador import *
from visualizador.visualizador import *


def definir_adquisidor():
    """
    Los adquisidores son:
    Adquisidor por Consola
    Adquisidor por Archivo
    :return:
    """
    return AdquisidorConsola(5)


def definir_procesador():
    """
    Los procesadores son:
    Procesador Amplificador
    Procesador con Umbral
    :return:
    """
    return ProcesadorAmplificador(4)


def definir_visualizador():
    return Visualizador()


class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    # Se configura el tipo de adquisidor
    adquisidor = definir_adquisidor()
    # Se configura el tipo de procesador
    procesador = definir_procesador()
    # Se configura el visualizador
    visualizador = definir_visualizador()

    def __init__(self):
        pass
