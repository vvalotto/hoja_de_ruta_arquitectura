from abc import ABCMeta, abstractmethod

class Graznido(metaclass=ABCMeta):

    @abstractmethod
    def graznar(self):
        pass


class GraznidoSilencioso(Graznido):

    def graznar(self):
        print('<< Silencio >>')


class GraznidoFuerte(Graznido):

    def graznar(self):
        print("Graznido Fuerte")


class GraznidoChirrido(Graznido):

    def graznar(self):
        print("Chirrido")

