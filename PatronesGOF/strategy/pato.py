from abc import ABCMeta, abstractmethod


class Graznido:

    @staticmethod
    def graznar():
        print('Cuac!!!')


class Volador:

    @staticmethod
    def volar():
        print('Estoy volando...')


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

    def mostrar(self):
        print('Yo soy un pato real')


class PatoModelado(Pato, Graznido, Volador):

    def mostrar(self):
        print('Yos un pato modelado')


class PatoDeGoma(Pato):

    def graznar(self):
        print('Sssscuac!!!')

    def mostrar(self):
        print('Yos un pato de goma')


class PatoDeMadera(Pato):

    def mostrar(self):
        print('Yos un pato de goma')
