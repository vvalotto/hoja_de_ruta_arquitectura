"""
Clase Paciente
"""

from .persona import *


class Paciente(Persona):

    @property
    def obra_social_nombre(self):
        return self._obras_social_nombre

    @obra_social_nombre.setter
    def obra_social_nombre(self, valor):
        self._obras_social_nombre = valor

    @property
    def obra_social_id(self):
        return self._obras_social_id

    @obra_social_id.setter
    def obra_social_id(self, valor):
        self._obras_social_id = valor

    def __init__(self):
        super().__init__()
        self._obras_social_nombre = None
        self._obras_social_id = None

    def __str__(self):
        return str(self.nombre_y_apellido)
