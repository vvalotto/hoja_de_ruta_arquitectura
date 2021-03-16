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

    @staticmethod
    def volar():
        print('Estoy volando...')

    @abstractmethod
    def mostrar(self):
        pass


class PatoReal(Pato):

    def mostrar(self):
        print('Yo soy un pato real')


class PatoModelado(Pato):

    def mostrar(self):
        print('Yos un pato modelado')


class PatoDeGoma(Pato):

    def graznar(self):
        print('Sssscuac!!!')

    def mostrar(self):
        print('Yos un pato de goma')

    def volar(self):
        raise Exception('No puedo volar')


class PatoDeMadera(Pato):

    def graznar(self):
        raise Exception('No puedo graznar')

    def mostrar(self):
        print('Yos un pato de goma')

    def volar(self):
        raise Exception('No puedo volar')