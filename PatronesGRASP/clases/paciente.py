"""
Clase Paciente
"""

from .persona import *


class Paciente(Persona):

    @property
    def obra_social_nombre(self):
        return self.__obras_social_nombre

    @property
    def obra_social_id(self):
        return self.__obras_social_id

    def __init__(self, nombre, documento, fecha_de_nacimiento, genero, obra_social, os_id):
        super().__init__(nombre, documento, fecha_de_nacimiento, genero)
        self.__obras_social_nombre = obra_social
        self.__obras_social_id = os_id

