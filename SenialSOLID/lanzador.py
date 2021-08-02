#!/usr/local/bin/python3.4
"""

"""
import os
import adquisidor
import procesador
import visualizador
import modelo

from adquisidor.adquisidor import *
from procesador.procesador import *
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
    def seleccionar_procesador():
        """
        Pide al usuario la seleccion del tipo de procesador
        """
        os.system("clear")
        print("Seleccionar tipo de procesamiento:")
        print("1 > Valor Doble")
        print("2 > Umbral")
        while True:
            op = input('Opcion: ')
            if op in ['1', '2']:
                break
        return op

    @staticmethod
    def ejecutar():
        """
        Se instancian las clases que participan del procesamiento
        """
        Lanzador.informar_versiones()
        Lanzador.tecla()
        opcion = Lanzador.seleccionar_procesador()
        tipo_procesamiento = None
        parametro = None

        mi_adquisidor = Adquisidor(5)
        mi_procesador = Procesador()

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        '''Paso 1 - Se obtiene la senial'''
        mi_adquisidor.leer_senial()
        senial_adquirida = mi_adquisidor.obtener_senial_adquirida()
        Lanzador.tecla()

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        if opcion == '1':
            tipo_procesamiento = "amplificar"
            parametro = 2
        elif opcion == '2':
            tipo_procesamiento = "umbral"
            parametro = 5
        else:
            print('Sin procesador selecionado')
            print("Fin Programa - NoOCP")
            exit()

        try:
            mi_procesador.procesar_senial(senial_adquirida, tipo_procesamiento, parametro)
        except Exception():
            print("Error al procesar")
            print("Fin Programa - NoOCP")
            exit()

        senial_procesada = mi_procesador.obtener_senial_procesada()
        Lanzador.tecla()

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        Visualizador().mostrar_datos(senial_procesada)
        print("Fin Programa - NoOCP")


if __name__ == "__main__":
    Lanzador().ejecutar()
