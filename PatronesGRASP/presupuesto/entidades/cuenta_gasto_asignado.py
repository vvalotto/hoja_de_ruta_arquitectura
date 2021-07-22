"""
Clases que componen el gasto limite asignado que se asignara a cada gerencia por casa cuenta
(Modelo resumido)
"""


class CuentaGastoAsignado:

    @property
    def id(self):
        return self.__identificacion

    @property
    def gasto_asignado(self):
        return self.__gasto_asignado

    def __init__(self, identificacion, gasto_asignado):
        self.__identificacion = identificacion
        self.__gasto_asignado = gasto_asignado


class GastoGerenciaAsignado:

    def __init__(self):
        self.__cuentas = []

    def agregar_cuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def obtener_cuentas(self):
        return self.__cuentas
