"""
Define la interfaz para los tipos que observan cambios en los tipos observados
"""


from abc import abstractmethod


class Observador(object):

    @abstractmethod
    def actualizar(self, temperatura, humedad, presion):
        pass


class Visualizador(object):

    @abstractmethod
    def visualizar(self):
        pass
