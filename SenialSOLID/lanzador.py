"""
Ejemplo de solucion para el SRP, donde las responsabilidades se dividen
entre diferentes clases.
"""
import os
from senial_solid.adquisidor import *
from senial_solid.procesador import *
from senial_solid.visualizador import *


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

    @staticmethod
    def ejecutar():
        """
        Se instancian las clases que participan del procesamiento
        """
        adquisidor = Adquisidor(5)
        procesador = Procesador()
        visualizador = Visualizador()

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        '''Paso 1 - Se obtiene la senial'''
        adquisidor.leer_senial()
        senial_adquirida = adquisidor.obtener_senial_adquirida()
        Lanzador.tecla()

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        procesador.procesar_senial(senial_adquirida)
        senial_procesada = procesador.obtener_senial_procesada()
        Lanzador.tecla()

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        visualizador.mostrar_datos(senial_procesada)
        print("Fin Programa - SRP")


if __name__ == "__main__":
    Lanzador().ejecutar()