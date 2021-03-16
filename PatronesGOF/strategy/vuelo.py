from abc import abstractmethod, ABCMeta


class Vuelo(metaclass=ABCMeta):

    @abstractmethod
    def volar(self):
        pass


class VueloConAlas(Vuelo):

    def volar(self):
        print('Yo vuelo')


class SinVuelo(Vuelo):

    def volar(self):
        print('No puedo volar')


class VueloPotenciado(Vuelo):

    def volar(self):
        print('Vuelo como un cohete')
