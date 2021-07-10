from PatronesGRASP.clases.nombre import Nombre
from PatronesGRASP.clases.identificacion import Identificacion


"""
Clase Persona
"""

from datetime import date


class Persona:

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__nombre.apellido

    @property
    def fecha_de_nacimiento(self):
        return self.__fecha_de_nacimiento

    @property
    def genero(self):
        return self.__genero

    @property
    def documento(self):
        return self.__documento


    @property
    def apellidos_y_nombres(self):
        return self.__nombre.apellidos_y_nombres()

    @property
    def edad(self):
        return int((date.today() - self.__fecha_de_nacimiento).days / 365)

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        self.__telefono = valor

    def __init__(self, nombre, documento, fecha_de_nacimiento, genero):
        self.__nombre = nombre
        self.__documento = documento
        self.__fecha_de_nacimiento = fecha_de_nacimiento
        self.__genero = genero
        self.__telefono = None

    def __str__(self):
        return str(self.__nombre)
