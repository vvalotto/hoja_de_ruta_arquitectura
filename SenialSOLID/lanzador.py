#!/usr/local/bin/python3.4
"""
Ejemplo de solucion para el SRP, donde las responsabilidades se dividen
entre diferentes clases separadas en diferentes módulos a implementar.
"""
import os
import adquisidor
import procesador
import visualizador
import modelo

from configurador import *

from adquisidor.adquisidor import *
from visualizador.visualizador import *


class Lanzador:
    """
    Programa Lanzador
    """
    def __init__(self):
        pass

    @staticmethod
    def tecla():
        """
        Funcion que solicita un tecla para continuar
        """
        while True:
            if input('C para continuar> ') == "C":
                break
        return

    @staticmethod
    def informar_versiones():
        os.system("clear")
        print("Versiones de los componenetes")
        print("adquisidor: " + adquisidor.__version__)
        print("procesador: " + procesador.__version__)
        print("visualizador: " + visualizador.__version__)
        print("modelo: " + modelo.__version__)

    @staticmethod
    def ejecutar():
        """
        Programa principal
        """

        '''
        Se prepara el programa
        '''
        Lanzador.informar_versiones()
        Lanzador.tecla()

        '''
        Se instancian las clases que participan del procesamiento
        '''
        mi_adquisidor = Adquisidor(5)
        mi_procesador = Configurador.procesador

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        '''Paso 1 - Se obtiene la senial'''
        mi_adquisidor.leer_senial()
        senial_adquirida = mi_adquisidor.obtener_senial_adquirida()
        Lanzador.tecla()

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        mi_procesador.procesar(senial_adquirida)
        senial_procesada = mi_procesador.obtener_senial_procesada()
        Lanzador.tecla()

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        Visualizador().mostrar_datos(senial_procesada)
        print("Fin Programa - OCP")


if __name__ == "__main__":
    Lanzador().ejecutar()
