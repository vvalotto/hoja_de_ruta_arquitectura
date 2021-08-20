__author__ = 'Victor Valotto'
__version__ = '7.0.0'

"""
NoISP 
"""

import adquisidor
import procesador
import visualizador
import persistidor
import modelo

from configurador import *

from datetime import datetime


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
        print("persistidor: " + persistidor.__version__)
        print("modelo: " + modelo.__version__)
        print("Senial_SOLID:" + __version__)

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
        mi_adquisidor = Configurador.adquisidor
        mi_procesador = Configurador.procesador
        mi_visualizador = Configurador.visualizador
        repositorio_adquisicion = Configurador.rep_adquisicion
        repositorio_procesamiento = Configurador.rep_procesamiento

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        '''Paso 1 - Se obtiene la senial'''
        mi_adquisidor.leer_senial()
        senial_adquirida = mi_adquisidor.obtener_senial_adquirida()
        senial_adquirida.fecha_adquisicion = datetime.now().date()
        senial_adquirida.comentario = input('Descripcion de la señal:')
        senial_adquirida.id = int(input('Identificacion (nro entero)'))
        print('Fecha de lectura: {0}'.format(senial_adquirida.fecha_adquisicion))
        print('Cantidad de valores obtenidos {0}'.format(senial_adquirida.cantidad))

        repositorio_adquisicion.auditar(senial_adquirida, "Senial Adquirida")
        Lanzador.tecla()
        print('Se persiste la señal adquirida')
        repositorio_adquisicion.guardar(senial_adquirida)
        print('Señal Guardada')
        repositorio_adquisicion.auditar(senial_adquirida, "Senial Guardada")

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        mi_procesador.procesar(senial_adquirida)
        senial_procesada = mi_procesador.obtener_senial_procesada()
        senial_procesada.comentario = input('Descripcion de la señal procesada:')
        senial_procesada.id = int(input('Identificacion (nro entero)'))

        repositorio_procesamiento.auditar(senial_procesada, "Senial Procesada")
        Lanzador.tecla()
        print('Se persiste la señal procesada')
        repositorio_procesamiento.guardar(senial_procesada)
        print('Señal Guardada')
        repositorio_procesamiento.auditar(senial_procesada, "Senial Guardada")

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        adquirida = repositorio_adquisicion.obtener(definir_senial_adquirir(), senial_adquirida.id)
        procesada = repositorio_procesamiento.obtener(definir_senial_procesar(), senial_procesada.id)
        mi_visualizador.mostrar_datos(adquirida)
        print('----->')
        mi_visualizador.mostrar_datos(procesada)
        print('----->')

        print("Fin Programa - NoISP")
        exit()


if __name__ == "__main__":
    Lanzador().ejecutar()
