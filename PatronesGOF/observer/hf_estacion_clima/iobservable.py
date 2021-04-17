"""
Definición de la Inferfaz del Objeto observable
"""


from abc import abstractmethod


class Observable:

    @abstractmethod
    def registrar_observador(self, observador):
        pass

    @abstractmethod
    def remover_observador(self, observador):
        pass

    @abstractmethod
    def notificar_observador(self):
        pass

