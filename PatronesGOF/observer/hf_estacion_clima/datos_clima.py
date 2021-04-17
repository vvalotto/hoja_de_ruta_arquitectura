"""
Elemento observable correspondiente a los datos del clima
"""

from .iobservable import *


class DatosClima(Observable):
    """
    Tipo que define quienes son los
    obsevadores para notificar los cambios
    """
    def __init__(self):
        self._presion = None
        self._humedad = None
        self._temperatura = None
        self._observadores = []
        return

    def registrar_observador(self, observador):
        self._observadores.append(observador)
        return

    def remover_observador(self, observador):
        self._observadores.remove(observador)
        return

    def notificar_observador(self):
        for un_obsevador in self._observadores:
            un_obsevador.actualizar(self._temperatura,
                                    self._humedad,
                                    self._presion)
        return

    def informar_cambios_mediciones(self):
        '''
        Cada vez que hay un cambio en alguna variable se debe
        notificar a los observadores
        :return:
        '''
        self.notificar_observador()
        return

    def poner_mediciones(self, temperatura, humedad, presion):
        '''
        Se actualizan el estado de las variables de la medicion y
        se genera la notificación a quien corresponda
        :param temperatura:
        :param humedad:
        :param presion:
        :return:
        '''
        self._humedad = humedad
        self._presion = presion
        self._temperatura = temperatura
        self.informar_cambios_mediciones()
        return




