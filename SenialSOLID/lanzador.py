__author__ = 'Victor Valotto'
__version__ = '7.0.0'

"""
Persistencia
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
        persistidor_adquisicion = Configurador.persistidor_adquisicion
        persistidor_procesamiento = Configurador.persistidor_procesamiento

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

        Lanzador.tecla()
        print('Se persiste la señal adquirida')
        persistidor_adquisicion.persistir(senial_adquirida, senial_adquirida.id)
        print('Señal Guardada')

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        mi_procesador.procesar(senial_adquirida)
        senial_procesada = mi_procesador.obtener_senial_procesada()

        Lanzador.tecla()
        print('Se persiste la señal procesada')
        senial_procesada.comentario = input('Descripcion de la señal procesada:')
        senial_procesada.id = int(input('Identificacion (nro entero)'))
        persistidor_procesamiento.persistir(senial_procesada, senial_procesada.id)
        print('Señal Guardada')

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        adquirida = persistidor_adquisicion.recuperar(definir_senial_adquirir(), senial_adquirida.id)
        procesada = persistidor_procesamiento.recuperar(definir_senial_procesar(), senial_procesada.id)
        mi_visualizador.mostrar_datos(adquirida)
        print('----->')
        mi_visualizador.mostrar_datos(procesada)
        print('----->')

        print("Fin Programa")
        exit()


if __name__ == "__main__":
    Lanzador().ejecutar()
