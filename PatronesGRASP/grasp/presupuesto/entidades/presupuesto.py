"""

"""

from .cuenta_presupuesto import *


class Presupuesto:

    def __init__(self, gerencia):
        self.__sector = gerencia
        self.__estado = "Creado"
        self.__anio = 2021
        self.__cuentas = []

    def agregar_cuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def obtener_cuenta(self, identificacion):
        for cuenta in self.__cuentas:
            if cuenta.id == identificacion:
                return cuenta
            else:
                return None

    def eliminar_cuenta(self, identificacion):
        pass

    def obtener_presupuesto(self):
        pass
