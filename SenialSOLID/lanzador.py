#!/usr/local/bin/python3.4
"""
Solucion Requerimiento 2 - Impacto en los componentes clientes del procesador
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
        Programa principal
        """

        '''
        Se prepara el programa
        '''
        Lanzador.informar_versiones()
        Lanzador.tecla()
        opcion = Lanzador.seleccionar_procesador()

        '''
        Se instancian las clases que participan del procesamiento
        '''
        mi_adquisidor = Adquisidor(5)
        if opcion == '1':
            '''Si es para amplificar pasa el valor a amplificar'''
            mi_procesador = Procesador(2)
        elif opcion == '2':
            '''Si es umbral pasa el valor de umbral'''
            mi_procesador = Procesador(5)
        else:
            mi_procesador = None

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        '''Paso 1 - Se obtiene la senial'''
        mi_adquisidor.leer_senial()
        senial_adquirida = mi_adquisidor.obtener_senial_adquirida()
        Lanzador.tecla()

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")

        try:
            if opcion == '1':
                mi_procesador.procesar_senial(senial_adquirida)
            elif opcion == '2':
                mi_procesador.procesar_senial_con_umbral(senial_adquirida)
            else:
                print('Sin procesador selecionado')
                print("Fin Programa - NoOCP")
                exit()

        except Exception():
            print("Error al procesar")
            print("Fin Programa - NoOCP")
            exit()

        senial_procesada = mi_procesador.obtener_senial_procesada()
        Lanzador.tecla()

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        Visualizador().mostrar_datos(senial_procesada)
        print("Fin Programa - SRP")


if __name__ == "__main__":
    Lanzador().ejecutar()
