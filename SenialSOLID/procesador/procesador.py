"""
Define la clase procesador de la senial
Cambio 1:
Uso de la funcion map para calcular valores de la lista
"""
from SenialSOLID.modelo.senial import *


class Procesador:
    """
    Constructor: Inicializa la clase
    """
    def __init__(self):
        self._senial_procesada = Senial()
    
    def procesar_senial(self, senial, tipo_procesamiento, parametro):
        """
        Metodo que realiza el procesamiento de la senial
        :param senial: a procesar
        :param tipo_procesamiento: define que tipo de calculo hay que haces
        :param parametro: parametro relacionado con tipo de procesamiento
        :return:
        """
        print("Procesando...")
        if tipo_procesamiento == "amplificar":
            self._amplificacion = parametro
            self._senial_procesada._valores = list(map(self.funcion_doble, senial._valores))
        elif tipo_procesamiento == "umbral":
            self._umbral = parametro
            self._senial_procesada._valores = list(map(self.funcion_umbral, senial._valores))
        else:
            return Exception()
        return
    
    def obtener_senial_procesada(self):
        """
        Devuelve la senial procesada
        :return:
        """
        return self._senial_procesada

    def funcion_doble(self, valor):
        """
        Funcion que retorna el doble de valor de entrada
        :param valor:
        :return:
        """
        return valor * self._amplificacion

    def funcion_umbral(self, valor):
        """
        Funcion que filtra valores con un umbral
        :param valor:
        :return:
        """
        return valor if valor < self._umbral else 0
