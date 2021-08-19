__author__ = 'Victor Valotto'
__version__ = '1.2.0'

"""
Configura las clases que se usaran en el programa
Se comporta como un Factory de las clases
"""
from procesador.procesador import *
from adquisidor.adquisidor import *
from visualizador.visualizador import *
from persistidor.contexto import *
from persistidor.repositorio import *

from modelo.senial import *


def definir_senial_adquirir():
    """
    Define el tipo de estructura para la señal a adquirir
    :return:
    """
    return SenialPila(5)


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
    return AdquisidorArchivo("adquisidor/datos.txt", definir_senial_adquirir())


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


def definir_contexto(recurso):
    """
    Los contexto son:
    Almancenar en archivos txt
    Almacenar en archivos pickle
    :param recurso:
    :return:
    """
    return ContextoArchivo(recurso)


def definir_repositorio(contexto):
    return RepositorioSenial(contexto)


class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """

    # Configura los contextos de datos
    ctx_datos_adquisicion = definir_contexto('./tmp/datos/adq')
    ctx_datos_procesamiento = definir_contexto('./tmp/datos/pro')
    # Configura los repositorios de las entidades a usar
    rep_adquisicion = definir_repositorio(ctx_datos_adquisicion)
    rep_procesamiento = definir_repositorio(ctx_datos_procesamiento)

    # Se configura el tipo de adquisidor
    adquisidor = definir_adquisidor()
    # Se configura el tipo de procesador
    procesador = definir_procesador()
    # Se configura el visualizador
    visualizador = definir_visualizador()

