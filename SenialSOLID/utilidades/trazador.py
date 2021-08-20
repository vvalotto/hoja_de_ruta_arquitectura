from abc import ABCMeta, abstractmethod


class BaseTrazador(metaclass=ABCMeta):

    @abstractmethod
    def trazar(self, entidad, accion, mensaje):
        pass