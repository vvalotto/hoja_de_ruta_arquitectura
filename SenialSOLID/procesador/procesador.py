"""
Define la clase procesador de la senial
"""
from SenialSOLID.modelo.senial import *


class Procesador:
    """
    Constructor: Inicializa la clase
    """
    def __init__(self):
        self._senial_procesada = Senial()
    
    def procesar_senial(self, senial):
        """
        Metodo que realiza el procesamiento de la senial
        :param senial: a procesar
        :return:
        """
        print("Procesando...")
        for i in range(0, senial.obtener_tamanio()):
            self._senial_procesada.poner_valor(senial.obtener_valor(i) * 2)
    
    def obtener_senial_procesada(self):
        """
        Devuelve la senial procesada
        :return:
        """
        return self._senial_procesada
