__author__ = 'Victor Valotto'
__version__ = '1.0.0'

"""
Configura las clases que se usaran en el programa
Se comporta como un Factory de las clases
"""
from procesador.procesador import *
from adquisidor.adquisidor import *
from visualizador.visualizador import *
from modelo.senial import *


def definir_senial_adquirir():
    """
    Define el tipo de estructura para la señal a adquirir
    :return:
    """
    return SenialLista(5)


def definir_senial_procesar():
    """
    Define el tipo de estructura para la señal a procesar
    :return:
    """
    return SenialLista(5)


def definir_adquisidor():
    """
    Los adquisidores son:
    Adquisidor por Consola
    Adquisidor por Archivo
    :return:
    """
    return AdquisidorConsola(definir_senial_adquirir())


def definir_procesador():
    """
    Los procesadores son:
    Procesador Amplificador
    Procesador con Umbral
    :return:
    """
    return ProcesadorAmplificador(definir_senial_procesar(), 4)


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
