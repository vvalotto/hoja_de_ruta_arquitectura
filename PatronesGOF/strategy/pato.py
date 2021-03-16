from abc import ABCMeta, abstractmethod


class Graznido:

    @abstractmethod
    def graznar(self):
        pass


class Volador:

    @abstractmethod
    def volar(self):
        pass


class Pato(metaclass=ABCMeta):

    def __init__(self):
        pass

    @staticmethod
    def nadar():
        print('Estoy nadando...')

    @abstractmethod
    def mostrar(self):
        pass


class PatoReal(Pato, Graznido, Volador):

    def graznar(self):
        print('Cuac!!!')

    def volar(self):
        print('Puedo Volar...')

    def mostrar(self):
        print('Yo soy un pato real')


class PatoModelado(Pato, Graznido, Volador):

    def graznar(self):
        print('Cuac!!!')

    def volar(self):
        print('Puedo Volar...')

    def mostrar(self):
        print('Yos un pato modelado')


class PatoDeGoma(Pato, Graznido):

    def graznar(self):
        print('Sssscuac!!!')

    def mostrar(self):
        print('Yos un pato de goma')


class PatoDeMadera(Pato):

    def mostrar(self):
        print('Yos un pato de goma')
