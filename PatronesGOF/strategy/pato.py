from abc import ABCMeta, abstractmethod


class Pato(metaclass=ABCMeta):

    def __init__(self):
        pass

    @staticmethod
    def graznar():
        print('Cuac!!!')

    @staticmethod
    def nadar():
        print('Estoy nadando...')

    @abstractmethod
    def mostrar(self):
        pass


class PatoReal(Pato):

    def mostrar(self):
        print('Yo soy un pato real')


class PatoModelado(Pato):

    def mostrar(self):
        print('Yos un pato modelado')
