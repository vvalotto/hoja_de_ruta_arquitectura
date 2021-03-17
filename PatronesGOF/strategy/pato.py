from vuelo import *
from graznido import *

from abc import  ABCMeta, abstractmethod


class Pato(metaclass=ABCMeta):

    vuelo = None
    graznido = None

    def __init__(self):
        pass

    @abstractmethod
    def visualizar(self):
        pass

    def hacer_graznido(self):
        self.graznido.graznar()

    def realizar_vuelo(self):
        self.vuelo.volar()

    def nadar(self):
        print ('Todos los patos nadan')


class PatoReal(Pato):

    def __init__(self):
        super().__init__()
        self.vuelo = VueloConAlas()
        self.graznido = GraznidoFuerte()

    def visualizar(self):
        print('Yos un pato real')


class PatoModelado(Pato):

    def __init__(self):
        super().__init__()
        self.vuelo = VueloConAlas()
        self.graznido = GraznidoSilencioso()

    def visualizar(self):
        print('Yos un pato modelado')
