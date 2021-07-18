"""
Turno
"""

import datetime


class Turno:

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, valor):
        self.__dia = valor

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, valor):
        self.__hora = valor

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, valor):
        self.__paciente = valor
        if self.__paciente != "" or self.__paciente is not None:
            self.__estado = "ocupado"
        else:
            self.__estado = "vacio"

    @property
    def aviso(self):
        return self.__aviso

    @aviso.setter
    def aviso(self, valor):
        self.__aviso = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def evento(self):
        evento = datetime.datetime(self.__dia.year, self.__dia.month, self.__dia.day,
                                   self.__hora.hour, self.__hora.minute, self.__hora.second, 0)
        return evento

    def __init__(self):
        self.__dia = None
        self.__hora = None
        self.__paciente = None
        self.__aviso = "sin aviso"
        self.__estado = "vacio"
