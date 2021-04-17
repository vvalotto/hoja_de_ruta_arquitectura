from abc import ABCMeta, abstractmethod

import datetime


class Observador(metaclass=ABCMeta):

    @abstractmethod
    def notificar(self, marcado):
        pass


class ObservadorTiempoUSA(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def notificar(self, marcado):
        tiempo = datetime.datetime.fromtimestamp(int(marcado)).strftime('%Y-%m-%d %I:%M:$%p')
        print('Observador', self.nombre, 'dice: ', tiempo)


class ObservadorTiempoEUT(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def notificar(self, marcado):
        tiempo = datetime.datetime.fromtimestamp(int(marcado)).strftime('%Y-%m-%d %H:%M%S')
        print('Observador', self.nombre, 'dice: ', tiempo)