"""
Ejemplos básicos
"""

"""
class Identificacion:

    tipo = None
    numero = None

    def __str__(self):
        return str(self.tipo) + ":" + str(self.numero)
"""


class Identificacion:

    @property
    def tipo(self):
        return self.__tipo

    @property
    def numero(self):
        return self.__numero

    def __init__(self, tipo, numero):
        self.__tipo = tipo
        self.__numero = numero

    def __str__(self):
        return self.__tipo + ":" + str(self.__numero)


